#!/usr/bin/env python3
"""Build canonical source identities and processing queues from the supplemental inventory."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


RIGHTS_RISK_MARKERS = ("z-library", "libgen", "oceanofpdf")
TEMP_EXTENSIONS = {".crdownload", ".dtmp"}
RUNTIME_PATH_MARKERS = (
    "/openjdk-18+36_windows-x64_bin/",
    "/spark-3.5.5-bin-hadoop3/",
    "/hadoop-3.3.5/",
)
BATCH_IDS = {
    "/media/kina2711/DATA/DATA/DE/Foundation": "B01-DE-FOUNDATION",
    "/media/kina2711/DATA/DATA/DSA/DSA Common To Share All": "B02-DE-DSA",
    "/media/kina2711/DATA/DATA/DE-DWH-DataLake": "B03-DE-DWH-DATALAKE",
    "/media/kina2711/DATA/DATA/DE-ETL-Transform": "B04-DE-ETL-SPARK",
    "/media/kina2711/DATA/Kafka/apache-kafka": "B05-DE-KAFKA",
    "/media/kina2711/DATA/DATA/Statistic": "B06-DA-STATISTICS",
    "/media/kina2711/DATA/DATA/Domain knowledge": "B07-CROSS-DOMAIN",
    "/media/kina2711/DATA/DATA/Sách": "B08-MIXED-BOOKS",
    "/media/kina2711/DATA/Library": "B09-MIXED-LIBRARY",
    "/media/kina2711/DATA/Disk E/2025/DE_Sách": "B10-DE-BOOKS-2025",
    "/media/kina2711/DATA/Disk E/2025/DE/Sách": "B11-DE-BOOKS-ARCHIVE",
}

ROOT_MODULE_RULES = (
    ("/kafka/apache-kafka/", ("DE-M21",), "root-course-topic", "high"),
    ("/dsa/dsa common to share all/", ("DE-M03",), "root-domain", "high"),
    ("/data/statistic/", ("DA-M05", "DA-M08"), "root-domain", "high"),
    ("/data/domain knowledge/", ("DA-M07", "DE-M11"), "root-domain", "medium"),
    ("/data/de-dwh-datalake/", ("DE-M10", "DE-M11", "DE-M14", "DE-M15"), "root-course-topic", "medium"),
    ("/data/de-etl-transform/", ("DE-M16", "DE-M17", "DE-M23"), "root-course-topic", "medium"),
    ("/data/de/foundation/", ("DE-M01", "DE-M02", "DE-M03", "DE-M04", "DE-M05", "DE-M06"), "root-course-topic", "low"),
)

KEYWORD_MODULE_RULES = (
    (("excel", "power query"), ("DA-M02",), "high"),
    (("power bi", "dashboard", "data visualization", "visualization"), ("DA-M06",), "medium"),
    (("statistics", "statistical", "probability"), ("DA-M05",), "high"),
    (("a b testing", "ab testing", "experiment"), ("DA-M08",), "medium"),
    (("python", "pandas"), ("DA-M09", "DE-M02"), "medium"),
    (("algorithm", "data structure", "leetcode", "dynamic programming", "recursion"), ("DE-M03",), "high"),
    (("computer architecture", "computer organization", "nand", "cpu", "memory hierarchy"), ("DE-M04",), "high"),
    (("operating system", "linux", "concurrency", "thread", "async"), ("DE-M05",), "medium"),
    (("network", "tcp", "http", "dns"), ("DE-M06",), "medium"),
    (("software architecture", "design pattern", "clean code", "git"), ("DE-M07",), "medium"),
    (("backend", "back end", "api", "django", "fastapi"), ("DE-M08",), "medium"),
    (("sql", "relational"), ("DA-M03", "DE-M09"), "medium"),
    (("postgres", "mysql", "database internals", "storage engine", "index"), ("DE-M10",), "high"),
    (("data warehouse", "data warehousing", "dimensional", "kimball", "star schema"), ("DA-M04", "DE-M11"), "high"),
    (("semantic layer", "metric layer", "metrics store"), ("DE-M12",), "high"),
    (("self service", "data product", "analytics product"), ("DE-M13",), "medium"),
    (("olap", "clickhouse", "duckdb", "columnar", "in memory database"), ("DE-M14",), "high"),
    (("parquet", "avro", "orc", "iceberg", "hudi", "delta lake", "data lake"), ("DE-M15",), "high"),
    (("ingestion", "etl", "data pipeline"), ("DE-M16",), "medium"),
    (("dbt", "elt", "airflow", "orchestration", "dagster", "prefect"), ("DE-M17",), "high"),
    (("data quality", "reliability", "great expectations", "reconciliation"), ("DE-M18",), "high"),
    (("metadata", "catalog", "lineage", "governance"), ("DE-M19",), "high"),
    (("distributed system", "data intensive", "consensus", "replication", "sharding"), ("DE-M20",), "medium"),
    (("kafka", "event streaming", "streaming"), ("DE-M21",), "high"),
    (("change data capture", "debezium", "cdc"), ("DE-M22",), "high"),
    (("spark", "flink", "hadoop", "rdd"), ("DE-M23",), "high"),
    (("cloud", "aws", "azure", "gcp"), ("DE-M24",), "medium"),
    (("kubernetes", "docker", "container", "terraform", "infrastructure as code"), ("DE-M25",), "high"),
    (("observability", "security", "sre", "monitoring"), ("DE-M26",), "medium"),
    (("system design",), ("DE-M27",), "high"),
    (("machine learning", "deep learning", "generative ai", "llm"), ("DE-M28",), "medium"),
    (("staff engineer", "principal", "leadership"), ("DE-M29", "DA-M10"), "medium"),
    (("marketing", "banking", "game analytics", "business analytics"), ("DA-M07",), "medium"),
    (("storytelling", "technical writing", "presentation"), ("DA-M10",), "medium"),
)


def normalized(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(char for char in value if not unicodedata.combining(char))
    value = value.casefold().replace("đ", "d")
    return re.sub(r"[^a-z0-9]+", " ", value).strip()


def source_id(digest: str) -> str:
    return f"SUP-{digest[:16].upper()}"


def canonical_score(record: dict[str, object]) -> tuple[int, int, str]:
    path = str(record["path"])
    lowered = path.casefold()
    extension = str(record["extension"])
    score = 0
    if extension in TEMP_EXTENSIONS:
        score -= 10000
    if int(record["size_bytes"]) == 0:
        score -= 5000
    if any(marker in lowered for marker in RIGHTS_RISK_MARKERS):
        score -= 500
    if re.search(r"(?:\(|\b)(?:copy|ban sao|\d+)(?:\)|\b)", lowered):
        score -= 25
    if str(record["kind"]) in {"document-or-book", "note-or-text", "course-transcript"}:
        score += 50
    return score, -len(path), path.casefold()


def companion_key(path: str) -> str | None:
    item = Path(path)
    extension = item.suffix.lower()
    if extension not in {".mp4", ".mkv", ".avi", ".mov", ".webm", ".m4v", ".mp3", ".wav", ".m4a", ".srt", ".vtt"}:
        return None
    stem = re.sub(r"_(?:en|vi|eng|vie)$", "", item.stem, flags=re.IGNORECASE)
    raw = f"{item.parent}|{stem}"
    return "MEDIA-" + hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16].upper()


def module_candidates(paths: list[str], title: str, valid_modules: set[str]) -> list[dict[str, str]]:
    corpus = normalized(" ".join(paths + [title]))
    found: dict[str, dict[str, str]] = {}
    rank = {"low": 1, "medium": 2, "high": 3}
    for marker, modules, basis, confidence in ROOT_MODULE_RULES:
        if normalized(marker) in corpus:
            for module in modules:
                if module in valid_modules:
                    found[module] = {"module_id": module, "basis": basis, "confidence": confidence}
    for terms, modules, confidence in KEYWORD_MODULE_RULES:
        matched = [term for term in terms if normalized(term) in corpus]
        if not matched:
            continue
        for module in modules:
            if module not in valid_modules:
                continue
            candidate = {
                "module_id": module,
                "basis": "filename-path-or-pdf-metadata-keyword:" + matched[0],
                "confidence": confidence,
            }
            previous = found.get(module)
            if previous is None or rank[confidence] > rank[previous["confidence"]]:
                found[module] = candidate
    return sorted(found.values(), key=lambda item: (item["module_id"], item["basis"]))


def rights_status(paths: list[str]) -> str:
    if any(any(marker in path.casefold() for marker in RIGHTS_RISK_MARKERS) for path in paths):
        return "private-reference-only-origin-risk"
    return "private-owner-provided-redistribution-unverified"


def processing_state(
    record: dict[str, object], pdf: dict[str, object] | None, has_transcript: bool
) -> tuple[str, str, str]:
    extension = str(record["extension"])
    kind = str(record["kind"])
    size = int(record["size_bytes"])
    normalized_path = str(record["path"]).replace("\\", "/").casefold()
    if any(marker.casefold() in normalized_path for marker in RUNTIME_PATH_MARKERS):
        return "excluded", "bundled-runtime-distribution", "exclude"
    if extension in TEMP_EXTENSIONS:
        return "rejected", "temporary-or-incomplete", "exclude"
    if size == 0:
        return "rejected", "empty-file", "exclude"
    if extension == ".pdf":
        if not pdf or pdf.get("status") != "parseable":
            return "rejected", "invalid-pdf", "exclude"
        text_status = str(pdf.get("text_layer_status"))
        if text_status == "no-text-in-sampled-pages":
            return "queued", "ocr-required", "P1"
        if text_status in {"partial-text-in-sampled-pages", "sample-extraction-error"}:
            return "queued", "hybrid-pdf-extraction", "P1"
        return "queued", "direct-pdf-text", "P1"
    if kind == "document-or-book":
        return "queued", "format-aware-document-extraction", "P1"
    if kind == "course-transcript":
        return "queued", "direct-transcript", "P0"
    if kind in {"course-video", "course-audio"}:
        if has_transcript:
            return "queued", "transcript-first-media-verification", "P1"
        return "queued", "transcription-required", "P2"
    if kind == "note-or-text":
        return "queued", "direct-text", "P0"
    if kind == "code-or-lab":
        return "companion", "structure-aware-code-review", "P2"
    if kind == "companion-artifact":
        return "companion", "format-aware-companion-review", "P2"
    if kind == "binary-runtime-or-unknown":
        return "excluded", "binary-runtime-or-unknown", "exclude"
    return "triage", "manual-format-triage", "P3"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inventory", required=True, type=Path)
    parser.add_argument("--pdf-structure", required=True, type=Path)
    parser.add_argument("--objectives", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    inventory = json.loads(args.inventory.read_text(encoding="utf-8"))
    pdf_structure = json.loads(args.pdf_structure.read_text(encoding="utf-8"))
    objectives = json.loads(args.objectives.read_text(encoding="utf-8"))
    pdf_by_path = {record["path"]: record for record in pdf_structure["records"]}
    valid_modules = {record["id"] for record in objectives["records"] if record["kind"] == "module"}

    by_hash: dict[str, list[dict[str, object]]] = defaultdict(list)
    for record in inventory["files"]:
        by_hash[str(record["sha256"])].append(record)

    media_groups: dict[str, list[dict[str, object]]] = defaultdict(list)
    for record in inventory["files"]:
        key = companion_key(str(record["path"]))
        if key:
            media_groups[key].append(record)

    manifest_sources: list[dict[str, object]] = []
    state_counts: Counter[str] = Counter()
    mode_counts: Counter[str] = Counter()
    priority_counts: Counter[str] = Counter()
    candidate_module_counts: Counter[str] = Counter()
    queued_candidate_module_counts: Counter[str] = Counter()
    rights_counts: Counter[str] = Counter()
    batch_counts: dict[str, Counter[str]] = defaultdict(Counter)

    for digest, records in sorted(by_hash.items()):
        canonical = max(records, key=canonical_score)
        aliases = sorted(str(record["path"]) for record in records if record is not canonical)
        all_paths = [str(canonical["path"]), *aliases]
        pdf = pdf_by_path.get(str(canonical["path"]))
        title = str((pdf or {}).get("title") or Path(str(canonical["path"])).stem)
        author = (pdf or {}).get("author")
        media_key = companion_key(str(canonical["path"]))
        group = media_groups.get(media_key, []) if media_key else []
        transcript_languages = sorted(
            {
                match.group(1).lower()
                for item in group
                if str(item["extension"]) in {".srt", ".vtt"}
                for match in [re.search(r"_([a-z]{2,3})$", Path(str(item["path"])).stem, re.IGNORECASE)]
                if match
            }
        )
        has_transcript = any(str(item["extension"]) in {".srt", ".vtt"} for item in group)
        state, extraction_mode, priority = processing_state(canonical, pdf, has_transcript)
        rights = rights_status(all_paths)
        candidates = (
            module_candidates(all_paths, title, valid_modules)
            if state not in {"excluded", "rejected"}
            else []
        )
        for candidate in candidates:
            candidate_module_counts[candidate["module_id"]] += 1
            if state == "queued":
                queued_candidate_module_counts[candidate["module_id"]] += 1
        state_counts[state] += 1
        mode_counts[extraction_mode] += 1
        priority_counts[priority] += 1
        rights_counts[rights] += 1
        batch_id = BATCH_IDS.get(str(canonical["root"]), "B99-UNASSIGNED")
        batch_counts[batch_id][state] += 1

        manifest_sources.append(
            {
                "source_id": source_id(digest),
                "sha256": digest,
                "canonical_path": str(canonical["path"]),
                "source_root": canonical["root"],
                "relative_path": canonical["relative_path"],
                "batch_id": batch_id,
                "aliases": aliases,
                "size_bytes": canonical["size_bytes"],
                "format": canonical["extension"],
                "kind": canonical["kind"],
                "title": title,
                "author": author,
                "edition": None,
                "edition_status": "needs-content-verification",
                "pdf_pages": (pdf or {}).get("pages"),
                "pdf_text_layer_status": (pdf or {}).get("text_layer_status"),
                "integrity_status": (pdf or {}).get("status", "not-pdf-structure-checked"),
                "rights_status": rights,
                "visibility": "private",
                "processing_state": state,
                "extraction_mode": extraction_mode,
                "reading_priority": priority,
                "content_evidence_status": "unread",
                "candidate_modules": candidates,
                "mapping_status": "candidate-needs-deep-reading" if candidates else "unmapped",
                "mapping_limitations": "Derived from path, filename or unverified embedded PDF metadata; not content evidence.",
                "companion_group_id": media_key,
                "transcript_languages": transcript_languages,
            }
        )

    output = {
        "schema_version": "1.0",
        "task_id": "book-build-supplemental-source-manifest-2026-09-27",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "inputs": {
            "inventory": str(args.inventory),
            "pdf_structure": str(args.pdf_structure),
            "objectives": str(args.objectives),
        },
        "policy": {
            "source_files_modified": False,
            "exact_duplicates_collapsed_by_sha256": True,
            "aliases_preserved": True,
            "candidate_mapping_is_content_evidence": False,
            "public_redistribution_authorized": False,
            "deep_read_complete_count": 0,
        },
        "summary": {
            "inventoried_file_count": len(inventory["files"]),
            "canonical_source_count": len(manifest_sources),
            "alias_count": sum(len(source["aliases"]) for source in manifest_sources),
            "by_processing_state": dict(sorted(state_counts.items())),
            "by_extraction_mode": dict(sorted(mode_counts.items())),
            "by_priority": dict(sorted(priority_counts.items())),
            "by_rights_status": dict(sorted(rights_counts.items())),
            "by_batch_and_state": {
                batch: dict(sorted(counts.items()))
                for batch, counts in sorted(batch_counts.items())
            },
            "candidate_module_counts": dict(sorted(candidate_module_counts.items())),
            "queued_candidate_module_counts": dict(sorted(queued_candidate_module_counts.items())),
            "unmapped_count": sum(not source["candidate_modules"] for source in manifest_sources),
            "eligible_unmapped_count": sum(
                source["processing_state"] in {"queued", "companion", "triage"}
                and not source["candidate_modules"]
                for source in manifest_sources
            ),
        },
        "sources": manifest_sources,
    }
    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
