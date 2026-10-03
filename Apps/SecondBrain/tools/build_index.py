#!/usr/bin/env python3
"""Build the private browser/desktop search index from canonical Wiki notes."""
from __future__ import annotations

import hashlib
import json
import re
import shutil
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
APP = ROOT / "Apps/SecondBrain"
WEB = APP / "web"
BRAIN = ROOT / "Docs/Second-Brain"
MANIFEST = BRAIN / "second-brain-manifest.json"


def frontmatter(text: str) -> tuple[dict, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        raise ValueError("frontmatter missing")
    return yaml.safe_load(match.group(1)), text[match.end():]


def title_from(body: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", body, re.M)
    return match.group(1).strip() if match else fallback


def domain_from(path: str) -> str:
    parts = Path(path).parts
    return parts[1] if len(parts) > 2 else "General"


def text_excerpt(body: str, limit: int = 240) -> str:
    clean = re.sub(r"```.*?```", " ", body, flags=re.S)
    clean = re.sub(r"<[^>]+>|[#>*_`|\[\]()]", " ", clean)
    clean = re.sub(r"\s+", " ", clean).strip()
    return clean[:limit].rstrip() + ("…" if len(clean) > limit else "")


def copy_vendor() -> None:
    vendor = WEB / "vendor"
    vendor.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / "node_modules/marked/lib/marked.esm.js", vendor / "marked.esm.js")
    shutil.copy2(ROOT / "node_modules/dompurify/dist/purify.es.mjs", vendor / "purify.es.mjs")
    mermaid_source = ROOT / "node_modules/mermaid/dist"
    mermaid_target = vendor / "mermaid"
    mermaid_target.mkdir(parents=True, exist_ok=True)
    shutil.copy2(mermaid_source / "mermaid.esm.min.mjs", mermaid_target / "mermaid.esm.min.mjs")
    chunk_target = mermaid_target / "chunks/mermaid.esm.min"
    chunk_target.mkdir(parents=True, exist_ok=True)
    for source in (mermaid_source / "chunks/mermaid.esm.min").glob("*.mjs"):
        shutil.copy2(source, chunk_target / source.name)


def main() -> int:
    manifest = json.loads(MANIFEST.read_text())
    release = manifest.get("canonical_release") or {}
    if manifest.get("status") != "active-canonical" or release.get("visibility") != "private-local-first":
        raise SystemExit("Refusing to index a non-canonical or non-private manifest")
    notes = []
    seen = set()
    domains = Counter()
    for entry in manifest["note_registry"]:
        path = BRAIN / entry["path"]
        fm, body = frontmatter(path.read_text())
        note_id = entry["note_id"]
        if note_id in seen:
            raise ValueError(f"duplicate note_id: {note_id}")
        if fm.get("status") != "canonical" or entry.get("status") != "canonical":
            raise ValueError(f"non-canonical note: {note_id}")
        seen.add(note_id)
        domain = domain_from(entry["path"])
        domains[domain] += 1
        relationships = fm.get("relationships") or {}
        tags = fm.get("tags") or []
        aliases = fm.get("aliases") or []
        title = title_from(body, note_id)
        notes.append({
            "id": note_id,
            "title": title,
            "domain": domain,
            "path": entry["path"],
            "question": str(fm.get("primary_question", "")),
            "noteType": str(fm.get("note_type", "")),
            "status": "canonical",
            "approvedAt": str(fm.get("approved_at", "")),
            "lastVerified": str(fm.get("last_verified", "")),
            "reviewAfter": str(fm.get("review_after", "")),
            "sourceIds": list(fm.get("source_ids") or []),
            "tags": list(tags if isinstance(tags, list) else [tags]),
            "aliases": list(aliases if isinstance(aliases, list) else [aliases]),
            "relationships": {
                "buildsOn": list(relationships.get("builds_on") or []),
                "prerequisiteOf": list(relationships.get("prerequisite_of") or []),
                "relatedTo": list(relationships.get("related_to") or []),
            },
            "excerpt": text_excerpt(body),
            "body": body.rstrip() + "\n",
            "wordCount": len(re.findall(r"\b\w+[\w-]*\b", body, re.U)),
        })
    notes.sort(key=lambda item: (item["domain"].lower(), item["title"].lower()))
    payload = {
        "schemaVersion": 1,
        "brainVersion": manifest["version"],
        "release": release,
        "stats": {
            "notes": len(notes),
            "sources": len(manifest["source_registry"]),
            "retrievalCases": len(manifest["retrieval_test_set"]),
            "domains": len(domains),
        },
        "domains": [{"name": name, "count": count} for name, count in sorted(domains.items())],
        "notes": notes,
    }
    encoded = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode()
    payload["contentHash"] = hashlib.sha256(encoded).hexdigest()
    target = WEB / "data/brain-index.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n")
    copy_vendor()
    print(f"built notes={len(notes)} domains={len(domains)} bytes={target.stat().st_size} hash={payload['contentHash']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
