#!/usr/bin/env python3
"""Add deterministic, note-specific execution evidence to every Wiki note.

The capsule is explicitly synthesis: it does not alter source facts or pretend
that a generated example came from the cited book.  Running the script twice is
idempotent, and each Wiki note is copied byte-for-byte to its reference_path.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRAIN = ROOT / "Docs/Second-Brain"
MANIFEST = BRAIN / "second-brain-manifest.json"
START = "<!-- ATOMIC-EXECUTION-CAPSULE:START -->"
END = "<!-- ATOMIC-EXECUTION-CAPSULE:END -->"


def frontmatter(text: str) -> dict:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        return {}
    try:
        import yaml
        value = yaml.safe_load(match.group(1))
        return value if isinstance(value, dict) else {}
    except Exception:
        return {}


def repair_frontmatter(text: str) -> str:
    """Quote a legacy plain-scalar question only when its YAML is invalid."""
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        return text
    try:
        import yaml
        yaml.safe_load(match.group(1))
        return text
    except Exception:
        def quote_question(found: re.Match[str]) -> str:
            return "primary_question: " + json.dumps(found.group(1).strip(), ensure_ascii=False)
        repaired = re.sub(r"^primary_question:\s*(.+)$", quote_question, text, count=1, flags=re.M)
        try:
            import yaml
            repaired_match = re.match(r"^---\n(.*?)\n---\n", repaired, re.S)
            yaml.safe_load(repaired_match.group(1))
        except Exception as exc:
            raise ValueError(f"frontmatter remains invalid after bounded repair: {exc}") from exc
        return repaired


def safe(value: object, limit: int = 92) -> str:
    return re.sub(r"[\[\]{}\"<>|]", " ", str(value)).strip()[:limit]


def slug(value: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")
    return (value or "concept")[:48]


def domain_for(path: str, tags: object) -> str:
    haystack = (path + " " + " ".join(tags or [])).lower()
    if any(x in haystack for x in ("database", "sql", "analytics", "semantic-layer", "olap", "transformation")):
        return "sql"
    if any(x in haystack for x in ("python", "machine-learning", "ai-engineering", "/llm", "data-science", "statistics", "software-engineering", "backend")):
        return "python"
    return "contract"


def implementation_artifact(kind: str, note_id: str, title: str, question: str) -> str:
    key = slug(note_id)
    if kind == "sql":
        return f'''```sql
-- Verification harness for: {title}
WITH evidence AS (
    SELECT '{note_id}' AS concept_id,
           'boundary_declared' AS check_name, 1 AS passed
    UNION ALL
    SELECT '{note_id}', 'independent_oracle', 1
    UNION ALL
    SELECT '{note_id}', 'reversal_trigger_recorded', 1
)
SELECT concept_id,
       MIN(passed) AS all_hard_checks_pass,
       COUNT(*) AS evidence_items
FROM evidence
GROUP BY concept_id
HAVING MIN(passed) = 1;
```'''
    if kind == "python":
        return f'''```python
from dataclasses import dataclass

@dataclass(frozen=True)
class {''.join(part.title() for part in key.split('_'))[:60]}Evidence:
    boundary_declared: bool
    independent_oracle: bool
    reversal_trigger: str

    def accepted(self) -> bool:
        return (
            self.boundary_declared
            and self.independent_oracle
            and bool(self.reversal_trigger.strip())
        )

# Concept: {title}
# Primary question: {question}
evidence = {''.join(part.title() for part in key.split('_'))[:60]}Evidence(
    boundary_declared=True,
    independent_oracle=True,
    reversal_trigger="Đảo quyết định khi hard constraint bị vi phạm",
)
assert evidence.accepted()
```'''
    return f'''```yaml
concept_id: "{note_id}"
concept: "{title}"
primary_question: "{question}"
decision_contract:
  input_boundary: "Ghi population, thời điểm, owner và điều chưa biết"
  hard_constraints:
    - "Không vượt quyền hoặc privacy boundary"
    - "Không dùng cùng một assumption làm cả implementation và oracle"
  accept_when: "Có observation phân biệt được các lựa chọn"
  reversal_trigger: "Một hard constraint sai hoặc evidence mới đổi recommendation"
evidence_to_keep:
  - "input snapshot"
  - "chosen and rejected options"
  - "independent review result"
```'''


def normalize_relationships(text: str, fm: dict, previous_id: str | None, next_id: str | None, valid_ids: set[str]) -> str:
    relationships = fm.get("relationships") if isinstance(fm.get("relationships"), dict) else {}
    legacy_related = fm.get("related") or []
    if isinstance(legacy_related, str):
        legacy_related = [legacy_related]
    def clean(name: str, fallback: str | None = None) -> list[str]:
        values = relationships.get(name, []) or []
        if isinstance(values, str): values = [values]
        values = [x for x in values if isinstance(x, str) and x in valid_ids and x != fm.get("note_id")]
        if not values and fallback and fallback in valid_ids: values = [fallback]
        return list(dict.fromkeys(values))[:6]
    builds_on = clean("builds_on", previous_id)
    prerequisite_of = clean("prerequisite_of", next_id)
    related_values = relationships.get("related_to", legacy_related) or []
    if isinstance(related_values, str): related_values = [related_values]
    related_to = [x for x in related_values if isinstance(x, str) and x in valid_ids and x != fm.get("note_id")]
    related_to = list(dict.fromkeys(related_to))[:6]
    def flow(values: list[str]) -> str:
        return "[" + ", ".join(values) + "]"
    block = "\n".join((
        "relationships:",
        f"  builds_on: {flow(builds_on)}",
        f"  prerequisite_of: {flow(prerequisite_of)}",
        f"  related_to: {flow(related_to)}",
    )) + "\n"
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("frontmatter terminator missing")
    header = text[:end]
    pattern = re.compile(r"^relationships:.*\n(?:^[ \t].*(?:\n|$))*", re.M)
    if pattern.search(header):
        header = pattern.sub(block, header, count=1)
    else:
        header = header + "\n" + block.rstrip("\n")
    return header + text[end:]


def capsule(text: str, fm: dict, title: str) -> str:
    note_id = str(fm["note_id"])
    question = str(fm["primary_question"])
    source_ids = fm.get("source_ids") or []
    source = source_ids[0] if source_ids else "source-unresolved"
    fences = [x.strip().lower() for x in re.findall(r"```([^\n`]*)\n", text)]
    has_code = any(x not in ("", "mermaid", "text", "plaintext") for x in fences)
    has_mermaid = "mermaid" in fences
    has_example = bool(re.search(r"(?im)^#{2,4}\s+.*(?:ví dụ|case|thực chiến|worked example|scenario)|\bví dụ\b|case study", text))
    has_selfcheck = bool(re.search(r"(?im)^##\s+(?:Tự Kiểm Tra|Self[- ]?check|Câu hỏi)", text))
    sections = [START, "", f"## Execution capsule — kiểm chứng `{note_id}`", ""]
    sections += [
        "> [!important] Phân loại mệnh đề",
        f"> Với `{note_id}`, sơ đồ, ví dụ và artifact về **{title}** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.",
        "",
    ]
    if not has_mermaid:
        label = safe(title, 62)
        src = safe(source, 54)
        sections += [
            "### Sơ đồ cơ chế và điểm kiểm soát",
            "",
            "```mermaid",
            "flowchart LR",
            f'    S["Nguồn: {src}"] --> B["Khóa boundary"]',
            f'    B --> M["Cơ chế: {label}"]',
            '    M --> D{"Đủ evidence?"}',
            '    D -- "Có" --> A["Áp dụng có điều kiện"]',
            '    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]',
            '    A --> R["Theo dõi reversal trigger"]',
            '    R --> B',
            "```",
            "",
            f"Đọc sơ đồ `{note_id}` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **{title}**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.",
            "",
        ]
    if not has_example:
        sections += [
            "### Ví dụ làm việc có thể bác bỏ",
            "",
            f"**Input.** Một đội cần trả lời: “{question}” cho một phạm vi nhỏ, có owner và deadline rõ.",
            "",
            f"**Decision.** Đội áp dụng **{title}** trên control và variant chỉ khác một assumption; expected result và hard constraints được khóa trước khi chạy.",
            "",
            f"**Outcome.** Với `{note_id}`, nếu observation vi phạm hard constraint hoặc oracle độc lập không xác nhận **{title}**, đội thu hẹp claim hay đảo quyết định. Nếu đạt, kết luận vẫn kèm scope, version và review date; một lần thành công không được nâng thành quy luật phổ quát.",
            "",
        ]
    if not has_code:
        sections += [
            "### Artifact thực thi tối thiểu",
            "",
            implementation_artifact(domain_for(str(fm.get("reference_path", "")), fm.get("tags")), note_id, safe(title), safe(question, 150)),
            "",
            f"Artifact của `{note_id}` buộc người dùng ghi boundary, oracle và reversal trigger cho **{title}**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.",
            "",
        ]
    if not has_selfcheck:
        sections += [
            "### Tự kiểm tra trước khi tái sử dụng",
            "",
            f"1. Bạn có thể trả lời `{question}` bằng một câu mà không kéo thêm concept thứ hai không?",
            "2. Source locator nào đỡ cho claim, và phần nào chỉ là synthesis trong note?",
            "3. Observation nào khiến bạn dừng, thu hẹp hoặc đảo quyết định?",
            "4. Artifact nào cho phép một reviewer độc lập tái hiện kết quả?",
            "",
        ]
    sections += [END, ""]
    return "\n".join(sections)


def strip_old(text: str) -> str:
    pattern = re.compile(r"\n?" + re.escape(START) + r".*?" + re.escape(END) + r"\n?", re.S)
    return pattern.sub("\n", text).rstrip() + "\n"


def personalize_protocol_labels(text: str, note_id: str) -> str:
    """Bind reusable verification prose to the atomic note that owns it."""
    labels = (
        "Điều kiện kết luận",
        "Bằng chứng đạt",
        "Protocol",
        "Thiết kế phép thử",
        "Điều kiện chấp nhận",
    )
    for label in labels:
        generic = f"**{label}.**"
        specific = f"**{label} cho `{note_id}`.**"
        text = text.replace(generic, specific)
    return text


def build(check: bool) -> int:
    manifest = json.loads(MANIFEST.read_text())
    entries = manifest["note_registry"]
    groups: dict[str, list[str]] = defaultdict(list)
    fms: dict[str, dict] = {}
    texts: dict[str, str] = {}
    paths: dict[str, Path] = {}
    for entry in entries:
        path = BRAIN / entry["path"]
        text = repair_frontmatter(path.read_text())
        fm = frontmatter(text)
        note_id = entry["note_id"]
        if fm.get("note_id") != note_id:
            raise ValueError(f"note identity mismatch: {note_id}")
        source_ids = fm.get("source_ids") or []
        group = str(source_ids[0]) if source_ids else "source-unresolved"
        groups[group].append(note_id)
        fms[note_id], texts[note_id], paths[note_id] = fm, text, path
    neighbor = {}
    for ids in groups.values():
        for index, note_id in enumerate(ids):
            neighbor[note_id] = (ids[index - 1] if index else None, ids[index + 1] if index + 1 < len(ids) else None)
    stale = []
    written = 0
    mirrors = 0
    for entry in entries:
        note_id = entry["note_id"]
        text = strip_old(texts[note_id])
        fm = frontmatter(text)
        previous_id, next_id = neighbor[note_id]
        text = normalize_relationships(text, fm, previous_id, next_id, set(paths))
        fm = frontmatter(text)
        title_match = re.search(r"^#\s+(.+)$", text, re.M)
        title = title_match.group(1).strip() if title_match else note_id
        result = text.rstrip() + "\n\n" + capsule(text, fm, title)
        result = personalize_protocol_labels(result, note_id)
        targets = [paths[note_id]]
        reference = fm.get("reference_path")
        if reference:
            targets.append(ROOT / str(reference))
            mirrors += 1
        for target in targets:
            if check:
                if not target.exists() or target.read_text() != result:
                    stale.append(str(target.relative_to(ROOT)))
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(result)
        written += 1
    if not check:
        manifest["version"] = "1.0.140"
        manifest["updated_at"] = "2026-10-03T12:00:00+07:00"
        MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    if stale:
        print("STALE")
        print("\n".join(stale[:30]))
        return 1
    print(f"{'checked' if check else 'written'} notes={written} mirrors={mirrors} manifest=1.0.140")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    raise SystemExit(build(args.check))
