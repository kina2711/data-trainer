#!/usr/bin/env python3
"""Reconcile owner-provided books without making any content-reading claim."""

from __future__ import annotations

import hashlib
import json
import subprocess
import zipfile
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ACADEMIC = ROOT / "Tools/Curriculum/Manifests/Academic"
TEMP = ROOT / "Material/Reference_temp"
LIBRARY = ROOT / "Material/DE/Reference/Library"

PURCHASE_FILES = {
    "SRC-KIMBALL": "The_Data_Warehouse_Toolkit_The_Definitive_Guide_to_Dimensional_Modeling_-_Ralph_Kimball.pdf",
    "SRC-STORY": "Storytelling_with_Data_-_Cole_Nussbaumer_Knaflic.pdf",
    "SRC-TOCE": "Trustworthy_Online_Controlled_Experiments_-_Ron_Kohavi.pdf",
    "SRC-DDIA": "Designing_Data-Intensive_Apllications_2nd_Edition_-_Martin_Kleppmann.pdf",
    "PACK-DA_FOUNDATIONS-BOOK-01": "Data_Science_for_Business_-_Foster_Provost.pdf",
    "PACK-DA_FOUNDATIONS-BOOK-02": "The_Truthful_Art_Data_Charts_and_Maps_for_Communication_-_Alberto_Cairo.pdf",
    "PACK-PRODUCT_ANALYTICS-BOOK-01": "Lean_Analytics__Use_Data_to_Build_a_Better_-_Alistair_Croll.pdf",
    "PACK-PRODUCT_ANALYTICS-BOOK-02": "Product_Analytics__Applied_Data_Science_Te_-_Joanne_Rodrigues-Craig.pdf",
    "PACK-EXCEL_BI-BOOK-01": "M_Is_for_Data_Monkey_A_Guide_to_the_M_Language_in_Excel_Power_Query_-_Ken_Puls.pdf",
    "PACK-EXCEL_BI-BOOK-02": "The_Definitive_Guide_to_DAX_3E_-_Alberto_Ferrari.pdf",
    "PACK-EXCEL_BI-BOOK-03": "The_Big_Book_of_Dashboards_-_Steve_Wexler.pdf",
    "PACK-STATS_EXPERIMENT-BOOK-02": "Practical_Statistics_for_Data_Scientists_3E_ER_-_Peter_Bruce.pdf",
    "PACK-PYTHON_ENGINEERING-BOOK-01": "Fluent_Python_-_Luciano_Ramalho.pdf",
    "PACK-PYTHON_ENGINEERING-BOOK-02": "Effective-Python-Brett-Slatkin.pdf",
    "PACK-PYTHON_ENGINEERING-BOOK-03": "Python_Concurrency_with_asyncio_Matthew_Fowler.pdf",
    "PACK-ALGORITHMS_ARCH-BOOK-01": "Algorithms_Fourth_Edition.pdf",
    "PACK-OS_NETWORK-BOOK-02": "The_Linux_Programming_Interface_-_Michael_Kerrisk.pdf",
    "PACK-OS_NETWORK-BOOK-03": "Computer_Networking_A_Top-Down_Approach_Global_Edition_8th_Edition_-_James_Kurose.pdf",
    "PACK-SOFTWARE_API-BOOK-02": "API_Design_Patterns_-_JJ_Geewax.pdf",
    "PACK-SOFTWARE_API-BOOK-03": "The_Pragmatic_Programmer_20th_Anniversary_-_Andrew_Hunt.pdf",
    "PACK-DATABASE_MODELING-BOOK-01": "Database_System_Concepts_-_Abraham_Silberschatz.pdf",
    "PACK-DATABASE_MODELING-BOOK-02": "Database_Internals_-_Alex_Petrov.pdf",
    "PACK-OLAP_FORMATS-BOOK-03": "Fundamentals_of_Data_Engineering_-_Joe_Reis.pdf",
    "PACK-PIPELINE_GOV-BOOK-02": "Data_Pipelines_Pocket_Reference_-_James_Densmore.pdf",
    "PACK-PIPELINE_GOV-BOOK-03": "Data_Quality_Fundamentals_-_Barr_Moses.pdf",
    "PACK-DISTRIBUTED_STREAM-BOOK-02": "Kafka_-_Gwen_Shapira.pdf",
    "PACK-DISTRIBUTED_STREAM-BOOK-03": "Streaming_Systems_-_Tyler_Akidau.pdf",
    "PACK-AI_ENGINEERING-BOOK-01": "AI_Engineering_Building_Applications_-_Chip_Huyen.pdf",
    "PACK-AI_ENGINEERING-BOOK-02": "Designing_Machine_Learning_Systems_An_Iterative_Process_for_Production-Ready_Applications_-_Chip_Huyen.pdf",
    "PACK-AI_ENGINEERING-BOOK-03": "Hands-On_Large_Language_Models_-_Jay_Alammar.pdf",
    "PACK-LEADERSHIP-BOOK-02": "The_Staff_Engineers_Path_-_Tanya_Reilly.pdf",
    "PACK-LEADERSHIP-BOOK-03": "Accelerate_-_Jez_Humble.pdf",
}

OTHER_OBSERVED = {
    "SRC-OPENINTRO": TEMP / "OpenIntro_Statistics_4th_ed_-_Christopher_Barr.pdf",
    "SRC-PROGIT": TEMP / "Pro_Git_-_Scott_Chacon.pdf",
    "SRC-COD": LIBRARY / "knowledge/hardware/Computer Organization and Design 5E - Patterson Hennessy - 0124077269.pdf",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def file_record(path: Path) -> dict:
    return {
        "local_path": str(path.relative_to(ROOT)),
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
        "reading_status": "candidate-unread",
    }


def main() -> None:
    catalog = json.loads((ACADEMIC / "source-catalog.json").read_text(encoding="utf-8"))
    by_id = {source["id"]: source for source in catalog["sources"]}
    required = {source["id"] for source in catalog["sources"] if source["access"] == "purchase-or-library"}
    if required != set(PURCHASE_FILES):
        raise SystemExit(f"purchase map mismatch: missing={sorted(required-set(PURCHASE_FILES))}; extra={sorted(set(PURCHASE_FILES)-required)}")

    pdfs = sorted(TEMP.glob("*.pdf"))
    parse_failures = []
    for path in pdfs:
        result = subprocess.run(["pdfinfo", str(path)], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
        if result.returncode:
            parse_failures.append({"path": str(path.relative_to(ROOT)), "error": result.stderr.strip()})
    archive = TEMP / "python-concurrency-with-asyncio-master.zip"
    archive_ok = archive.is_file() and zipfile.is_zipfile(archive)

    records = []
    for source_id, filename in PURCHASE_FILES.items():
        if filename:
            path = TEMP / filename
            status = "acquired-owner-approved" if path.is_file() else "missing"
            record = {"source_id": source_id, "title": by_id[source_id]["title"], "status": status}
            if path.is_file():
                record.update(file_record(path))
        else:
            record = {"source_id": source_id, "title": by_id[source_id]["title"], "status": "missing"}
        records.append(record)

    observed = []
    for source_id, path in OTHER_OBSERVED.items():
        record = {"source_id": source_id, "title": by_id[source_id]["title"], "status": "acquired-owner-approved"}
        record.update(file_record(path))
        observed.append(record)

    roots = []
    for name in ("Computer Science", "knowledge", "book"):
        path = LIBRARY / name
        files = [item for item in path.rglob("*") if item.is_file()]
        roots.append({
            "local_path": str(path.relative_to(ROOT)),
            "owner_description": {
                "Computer Science": "Học liệu chương trình Computer Science tại HCMUT",
                "knowledge": "Học liệu do mentor cung cấp để học chương trình Data Engineer",
                "book": "Sách do owner sưu tầm",
            }[name],
            "academic_approval": "owner-accepted-as-supplemental-source",
            "reading_status": "unread-as-a-collection",
            "redistribution_status": "not-confirmed",
            "file_count": len(files),
            "extensions": dict(Counter((item.suffix.lower() or "<none>") for item in files)),
        })

    counts = Counter(record["status"] for record in records)
    output = {
        "schema_version": 1,
        "generated_on": date.today().isoformat(),
        "task_id": "academic-source-acquisition-reconciliation-v2",
        "owner_approval": {
            "academic_suitability": "accepted-all-provided-books",
            "scope": ["Material/Reference_temp", "Material/DE/Reference/Library/Computer Science", "Material/DE/Reference/Library/knowledge", "Material/DE/Reference/Library/book"],
            "redistribution_rights": "not-confirmed-by-this-approval",
        },
        "validation": {
            "reference_temp_pdf_total": len(pdfs),
            "reference_temp_pdf_parse_pass": len(pdfs) - len(parse_failures),
            "reference_temp_pdf_parse_failures": parse_failures,
            "supporting_zip_integrity": "pass" if archive_ok else "fail",
        },
        "required_purchase_sources": {"counts": dict(counts), "records": records},
        "other_planned_sources_observed": observed,
        "supplemental_roots": roots,
        "content_reading_started": False,
    }
    path = ACADEMIC / "source-acquisition-v2.json"
    path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Đối soát nguồn sách đã tiếp nhận", "",
        "> Đây là kiểm kê tệp và xác nhận của owner; không phải kết quả đọc nội dung.", "",
        "## Kết quả", "",
        f"- PDF trong `Material/Reference_temp`: **{len(pdfs)}**, parse được: **{len(pdfs)-len(parse_failures)}**.",
        f"- Danh sách mua/mượn: **{counts['acquired-owner-approved']}/32 có bản sách**, **{counts['supporting-code-only-book-missing']} chỉ có mã nguồn**, **{counts['missing']} chưa thấy tệp**.",
        "- Owner chấp thuận toàn bộ sách được cung cấp về mặt học thuật.",
        "- Xác nhận này không tự động cấp quyền tái phân phối công khai.", "",
        "## Còn thiếu", "",
    ]
    outstanding = [record for record in records if record["status"] != "acquired-owner-approved"]
    if outstanding:
        lines += ["| Mã | Sách | Trạng thái |", "|---|---|---|"]
        for record in outstanding:
            lines.append(f"| `{record['source_id']}` | {record['title']} | `{record['status']}` |")
    else:
        lines.append("Không còn đầu sách nào thiếu trong danh sách mua/mượn.")
    lines += ["", "## Kho bổ sung đã được owner chấp thuận", "", "| Kho | Số tệp | Mô tả |", "|---|---:|---|"]
    for item in roots:
        lines.append(f"| `{item['local_path']}` | {item['file_count']} | {item['owner_description']} |")
    lines += ["", "## Ranh giới", "",
              "- Các kho bổ sung là nguồn ứng viên; chưa được coi là đã đọc hoặc đã ánh xạ vào từng objective.",
              "- Chương, trang, luận điểm và quyền trích dẫn được xác nhận ở cổng đọc sâu."]
    report = ROOT / "Docs/Operations/SOURCE-ACQUISITION.md"
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"required": 32, "acquired_books": counts["acquired-owner-approved"], "supporting_code_only": counts["supporting-code-only-book-missing"], "missing": counts["missing"], "pdf_parse_failures": len(parse_failures)}, ensure_ascii=False))
    if parse_failures or not archive_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
