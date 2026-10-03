#!/usr/bin/env python3
"""Normalize and lint Markdown knowledge notes without changing semantic content."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_ROOTS = (
    REPO_ROOT / "Material/DE/Reference/Library/Knowledge-Notes",
    REPO_ROOT / "Docs/Second-Brain",
)

BLOCK_PREFIX = re.compile(
    r"^(?:#{1,6}\s|[-*_]{3,}\s*$|[-+*]\s|\d+[.)]\s|\|(?:.*\|)?\s*$|"
    r"```|~~~|>\s?|\$\$\s*$|\[\^[^]]+\]:|<[/!A-Za-z]|:::)"
)
LATEX_COMMAND = re.compile(r"\\(?:approx|frac|sum|prod|lambda|mu|rho|theta|leftarrow|rightarrow|qquad|times|text|ldots|min|max)\b")


def _join(parts: list[str]) -> str:
    return " ".join(part.strip() for part in parts if part.strip())


def normalize_markdown(text: str) -> str:
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    out: list[str] = []
    paragraph: list[str] = []
    quote: list[str] = []
    list_item: list[str] = []
    list_indent = ""
    in_fence = False
    in_math = False
    in_frontmatter = bool(lines and lines[0].strip() == "---")
    frontmatter_closed = False

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            out.append(_join(paragraph))
            paragraph = []

    def flush_quote() -> None:
        nonlocal quote
        if quote:
            out.append("> " + _join(quote))
            quote = []

    def flush_list() -> None:
        nonlocal list_item, list_indent
        if list_item:
            first = list_item[0].strip()
            rest = _join(list_item[1:])
            out.append(list_indent + first + ((" " + rest) if rest else ""))
            list_item = []
            list_indent = ""

    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()

        if in_frontmatter:
            out.append(line)
            if stripped == "---" and len(out) > 1:
                in_frontmatter = False
                frontmatter_closed = True
            continue

        if stripped.startswith(("```", "~~~")):
            flush_paragraph(); flush_quote(); flush_list()
            out.append(line)
            in_fence = not in_fence
            continue
        if in_fence:
            out.append(line)
            continue

        if stripped in {r"\[", r"\]"}:
            stripped = "$$"
            line = "$$"

        if stripped == "$$":
            flush_paragraph(); flush_quote(); flush_list()
            out.append("$$")
            in_math = not in_math
            continue
        if in_math:
            out.append(line)
            continue

        if not stripped:
            flush_paragraph(); flush_quote(); flush_list()
            if out and out[-1] != "":
                out.append("")
            continue

        if re.match(r"^>\s*\[![^]]+\]", line):
            flush_paragraph(); flush_quote(); flush_list()
            out.append(line)
            continue
        if line.startswith(">"):
            flush_paragraph(); flush_list()
            content = line[1:].strip()
            if content:
                quote.append(content)
            else:
                flush_quote(); out.append(">")
            continue
        flush_quote()

        bullet = re.match(r"^(\s*)([-+*]\s+|\d+[.)]\s+)(.*)$", line)
        if bullet:
            flush_paragraph(); flush_list()
            list_indent = bullet.group(1)
            list_item = [bullet.group(2) + bullet.group(3)]
            continue

        if list_item and (line.startswith("  ") or not BLOCK_PREFIX.match(stripped)):
            list_item.append(stripped)
            continue
        flush_list()

        if BLOCK_PREFIX.match(stripped) or line.startswith("    "):
            flush_paragraph()
            out.append(line)
            continue

        paragraph.append(stripped)

    flush_paragraph(); flush_quote(); flush_list()
    while out and out[-1] == "":
        out.pop()
    normalized = "\n".join(out) + "\n"
    normalized = re.sub(r"(?m)^## (?:\d+\.\s+)?Reference\s*$", "## Reference", normalized)
    normalized = re.sub(r"(?m)^## (?:\d+\.\s+)?Key takeaways\s*$", "## Key takeaways", normalized)
    return normalized


def lint_markdown(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    if re.search(r"(?m)^\\[\[\]]\s*$", text):
        errors.append("legacy display-math delimiter \\[ or \\]")
    if text.count("$$") % 2:
        errors.append("unbalanced $$ delimiter")
    if text.count("```") % 2:
        errors.append("unbalanced fenced code block")
    normalized = normalize_markdown(text)
    if normalized != text:
        errors.append("non-canonical paragraph wrapping")

    path_text = path.as_posix()
    is_knowledge_note = "/2_Wiki/" in path_text or "/Knowledge-Notes/" in path_text
    if is_knowledge_note and len(re.findall(r"(?m)^## Reference\s*$", text)) != 1:
        errors.append("knowledge note must contain exactly one canonical ## Reference heading")
    if is_knowledge_note and len(re.findall(r"(?m)^## Key takeaways\s*$", text)) != 1:
        errors.append("knowledge note must contain exactly one canonical ## Key takeaways heading")
    if is_knowledge_note and len(re.findall(r"(?m)^## Source coverage\s*$", text)) != 1:
        errors.append("knowledge note must contain exactly one canonical ## Source coverage heading")

    in_fence = False
    in_math = False
    for number, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        if stripped.startswith(("```", "~~~")):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if stripped == "$$":
            in_math = not in_math
            continue
        candidate = re.sub(r"`[^`]*`|\$[^$\n]+\$", "", line)
        if not in_math and LATEX_COMMAND.search(candidate):
            errors.append(f"LaTeX command outside math at line {number}")
    return errors


def note_paths(roots: list[Path]) -> list[Path]:
    return sorted({path for root in roots for path in root.rglob("*.md")})


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("paths", nargs="*", type=Path)
    args = parser.parse_args()
    roots = [path if path.is_absolute() else REPO_ROOT / path for path in args.paths] or list(DEFAULT_ROOTS)
    failures = 0
    changed = 0
    for path in note_paths(roots):
        original = path.read_text(encoding="utf-8")
        if args.check:
            errors = lint_markdown(path, original)
            if errors:
                failures += 1
                print(f"FAIL {display_path(path)}: {'; '.join(errors)}")
        else:
            normalized = normalize_markdown(original)
            if normalized != original:
                path.write_text(normalized, encoding="utf-8")
                changed += 1
                print(f"FORMAT {display_path(path)}")
    if args.check:
        print(f"checked={len(note_paths(roots))} failed={failures}")
        return 1 if failures else 0
    print(f"checked={len(note_paths(roots))} changed={changed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
