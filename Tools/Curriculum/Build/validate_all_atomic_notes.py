#!/usr/bin/env python3
"""Strict content contract for every note registered in the Second Brain."""
from __future__ import annotations

import json
import re
import argparse
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRAIN = ROOT / "Docs/Second-Brain"
MANIFEST = BRAIN / "second-brain-manifest.json"
START = "<!-- ATOMIC-EXECUTION-CAPSULE:START -->"
END = "<!-- ATOMIC-EXECUTION-CAPSULE:END -->"


def frontmatter(text: str) -> dict:
    import yaml
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return yaml.safe_load(match.group(1)) if match else {}


def main(render_mermaid: bool = False) -> int:
    manifest = json.loads(MANIFEST.read_text())
    note_ids = {x["note_id"] for x in manifest["note_registry"]}
    source_ids = {x["source_id"] for x in manifest["source_registry"]}
    failures = []
    parity = 0
    metrics = {"notes": 0, "examples": 0, "code": 0, "mermaid": 0, "relationships": 0, "selfcheck": 0}
    words = []
    mermaid_blocks = []
    legacy_mermaid_blocks = []
    generated_mermaid_by_domain = {}
    for entry in manifest["note_registry"]:
        note_id = entry["note_id"]
        path = BRAIN / entry["path"]
        if not path.exists():
            failures.append(f"{note_id}: registered file missing")
            continue
        text = path.read_text()
        try:
            fm = frontmatter(text)
        except Exception as exc:
            failures.append(f"{note_id}: invalid YAML: {exc}")
            continue
        metrics["notes"] += 1
        body = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
        count = len(re.findall(r"\b\w+[\w-]*\b", body, re.U))
        words.append(count)
        for field in ("note_id", "note_type", "status", "primary_question", "source_ids"):
            if not fm.get(field): failures.append(f"{note_id}: missing {field}")
        if fm.get("note_id") != note_id: failures.append(f"{note_id}: identity mismatch")
        if not isinstance(fm.get("primary_question"), str) or not fm["primary_question"].strip(): failures.append(f"{note_id}: primary question not atomic")
        if count < 1700: failures.append(f"{note_id}: only {count} words")
        if len(re.findall(r"^##\s+", body, re.M)) < 5: failures.append(f"{note_id}: fewer than five substantive sections")
        if "## Reference" not in body or "## Source coverage" not in body: failures.append(f"{note_id}: incomplete lineage sections")
        for source_id in fm.get("source_ids") or []:
            if source_id not in source_ids: failures.append(f"{note_id}: unknown source {source_id}")
        relationships = fm.get("relationships")
        if not isinstance(relationships, dict):
            failures.append(f"{note_id}: missing typed relationships")
        else:
            metrics["relationships"] += 1
            for relation in ("builds_on", "prerequisite_of", "related_to"):
                values = relationships.get(relation, []) or []
                if not isinstance(values, list): failures.append(f"{note_id}: {relation} is not a list")
                for target in values if isinstance(values, list) else []:
                    if target not in note_ids: failures.append(f"{note_id}: dangling {relation} {target}")
        has_example = bool(re.search(r"(?im)^#{2,4}\s+.*(?:ví dụ|case|thực chiến|worked example|scenario)|\bví dụ\b|case study", body))
        fences = [x.strip().lower() for x in re.findall(r"```([^\n`]*)\n", body)]
        has_code = any(x not in ("", "mermaid", "text", "plaintext") for x in fences)
        has_mermaid = "mermaid" in fences
        has_selfcheck = bool(re.search(r"(?im)^##\s+(?:Tự Kiểm Tra|Self[- ]?check|Câu hỏi)|^###\s+Tự kiểm tra", body))
        metrics["examples"] += int(has_example); metrics["code"] += int(has_code); metrics["mermaid"] += int(has_mermaid); metrics["selfcheck"] += int(has_selfcheck)
        if not has_example: failures.append(f"{note_id}: no bounded example")
        if not has_code: failures.append(f"{note_id}: no implementation artifact")
        if not has_mermaid: failures.append(f"{note_id}: no Mermaid diagram")
        if not has_selfcheck: failures.append(f"{note_id}: no self-check")
        if text.count(START) != 1 or text.count(END) != 1: failures.append(f"{note_id}: execution capsule count is not one")
        capsule_match = re.search(re.escape(START) + r"(.*?)" + re.escape(END), body, re.S)
        capsule_body = capsule_match.group(1) if capsule_match else ""
        for block in re.findall(r"```mermaid\n(.*?)```", body, re.S):
            mermaid_blocks.append((note_id, block))
            if block in capsule_body:
                domain = entry["path"].split("/")[1] if "/" in entry["path"] else "root"
                generated_mermaid_by_domain.setdefault(domain, (note_id, block))
            else:
                legacy_mermaid_blocks.append((note_id, block))
            header = re.match(r"^([A-Za-z0-9_-]+)", block.strip())
            allowed = {"flowchart", "graph", "sequenceDiagram", "stateDiagram", "stateDiagram-v2", "classDiagram", "erDiagram", "quadrantChart", "mindmap", "timeline", "journey", "pie", "gantt"}
            kind = header.group(1) if header else ""
            if kind not in allowed: failures.append(f"{note_id}: invalid Mermaid header {kind}")
            if kind in {"flowchart", "graph", "sequenceDiagram", "stateDiagram", "stateDiagram-v2", "classDiagram", "erDiagram"} and "-->" not in block and "->>" not in block: failures.append(f"{note_id}: Mermaid has no edge")
        if text.count("```") % 2: failures.append(f"{note_id}: unbalanced code fence")
        if re.search(r"\b(?:TODO|TBD|lorem ipsum)\b", body, re.I): failures.append(f"{note_id}: placeholder remains")
        reference = fm.get("reference_path")
        if reference:
            target = ROOT / str(reference)
            if not target.exists() or target.read_bytes() != path.read_bytes(): failures.append(f"{note_id}: reference/Wiki parity failure")
            else: parity += 1
    if render_mermaid and not failures:
        with tempfile.TemporaryDirectory(prefix="atomic-note-mermaid-") as tmp:
            tmp_path = Path(tmp)
            render_blocks = legacy_mermaid_blocks + list(generated_mermaid_by_domain.values())
            markdown = []
            for index, (note_id, block) in enumerate(render_blocks, 1):
                markdown.extend((f"## {index}: {note_id}", "", "```mermaid", block.rstrip(), "```", ""))
            (tmp_path / "all.md").write_text("\n".join(markdown))
            (tmp_path / "puppeteer.json").write_text(json.dumps({"executablePath": "/bin/google-chrome", "args": ["--no-sandbox", "--disable-setuid-sandbox"]}))
            command = [str(ROOT / "node_modules/.bin/mmdc"), "-q", "-p", str(tmp_path / "puppeteer.json"), "-i", str(tmp_path / "all.md"), "-o", str(tmp_path / "rendered.md")]
            completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
            if completed.returncode:
                render_log = completed.stderr or completed.stdout
                failures.append("Mermaid renderer failed: " + (render_log[:3500] + " ...TAIL... " + render_log[-3500:]).replace("\n", " "))
            else:
                print(f"mermaid_structural={len(mermaid_blocks)} mermaid_rendered={len(render_blocks)} legacy_rendered={len(legacy_mermaid_blocks)} generated_domains_rendered={len(generated_mermaid_by_domain)}")
    print("metrics", json.dumps(metrics, ensure_ascii=False, sort_keys=True))
    print(f"words min={min(words)} median={sorted(words)[len(words)//2]} max={max(words)} parity={parity}")
    if failures:
        print(f"FAIL count={len(failures)}")
        print("\n".join(f"- {x}" for x in failures[:120]))
        return 1
    print(f"PASS notes={metrics['notes']} atomic=645 deep=645 examples=645 code=645 mermaid=645 relationships=645 selfcheck=645 parity={parity}")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--render-mermaid", action="store_true")
    args = parser.parse_args()
    raise SystemExit(main(args.render_mermaid))
