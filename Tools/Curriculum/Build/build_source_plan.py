#!/usr/bin/env python3
"""Build the one-time source plan; this makes no claim that sources were read."""

from __future__ import annotations

import json
from collections import defaultdict
from datetime import date
from pathlib import Path

from source_blueprint_v2 import COURSES, MODULE_COURSE, MODULE_PACK, PACKS

ROOT = Path(__file__).resolve().parents[3]
ACADEMIC = ROOT / "Tools/Curriculum/Manifests/Academic"


def src(sid, title, authority, kind, access, url, locator, *, version="living", local_path=None, note=""):
    return {"id": sid, "title": title, "authority": authority, "kind": kind,
            "access": access, "url": url, "version": version, "locator": locator,
            "local_path": local_path, "reading_status": "candidate-unread",
            "provenance_status": "official-route-verified", "note": note}


SOURCES = [
    src("SRC-MSL-DA", "Training for Data Analysts", "Microsoft Learn", "course", "online-official", "https://learn.microsoft.com/en-us/training/career-paths/data-analyst", "Learning paths theo vai trò Data Analyst"),
    src("SRC-MS-EXCEL", "Excel help & learning", "Microsoft Support", "documentation", "online-official", "https://support.microsoft.com/en-us/excel", "Formulas; import and analyze; PivotTables"),
    src("SRC-MS-PQ", "Power Query documentation", "Microsoft Learn", "documentation", "online-official", "https://learn.microsoft.com/en-us/power-query/", "Transformations; M language; query folding"),
    src("SRC-MS-PBI", "Power BI learning path directory", "Microsoft Learn", "course", "online-official", "https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-learning-path-directory", "Paths 6–7; accessibility; performance"),
    src("SRC-PG17", "PostgreSQL 17 Documentation", "PostgreSQL Global Development Group", "documentation", "online-official", "https://www.postgresql.org/docs/17/", "Parts I–III; SQL; indexes; concurrency; performance", version="17"),
    src("SRC-OPENINTRO", "OpenIntro Statistics", "OpenIntro", "book", "download-open", "https://www.openintro.org/book/os/", "Official PDF and datasets", note="Tải PDF từ trang tác giả."),
    src("SRC-NIST-STAT", "NIST/SEMATECH e-Handbook of Statistical Methods", "NIST", "handbook", "download-open", "https://www.itl.nist.gov/div898/handbook/", "EDA; process modeling; tests; uncertainty", note="Có bản chương PDF chính thức."),
    src("SRC-PANDAS", "pandas User Guide", "pandas project", "documentation", "online-official", "https://pandas.pydata.org/docs/user_guide/", "IO; indexing; missing data; groupby; merge; time series"),
    src("SRC-PYTHON", "Python 3 Documentation", "Python Software Foundation", "documentation", "online-official", "https://docs.python.org/3/", "Tutorial; library reference; language reference"),
    src("SRC-GOOGLE-TW", "Technical Writing Courses", "Google for Developers", "course", "online-official", "https://developers.google.com/tech-writing", "Technical Writing One and Two"),
    src("SRC-KIMBALL", "The Data Warehouse Toolkit", "Wiley", "book", "purchase-or-library", "https://www.wiley.com/en-us/The+Data+Warehouse+Toolkit%3A+The+Definitive+Guide+to+Dimensional+Modeling%2C+3rd+Edition-p-9781118530801", "Chapters xác định sau khi có bản hợp pháp", version="3rd edition"),
    src("SRC-STORY", "Storytelling with Data", "Wiley", "book", "purchase-or-library", "https://www.wiley.com/en-us/Storytelling+with+Data%3A+A+Data+Visualization+Guide+for+Business+Professionals-p-9781119002253", "Chapters xác định sau khi có bản hợp pháp"),
    src("SRC-TOCE", "Trustworthy Online Controlled Experiments", "Cambridge University Press", "book", "purchase-or-library", "https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/D97B26382EB0EB2DC2019A7A7B518F59", "Chapters xác định sau khi có bản hợp pháp"),
    src("SRC-AMPLITUDE", "Product Analytics documentation", "Amplitude", "documentation", "online-official", "https://www.amplitude.com/docs/analytics/product-analytics", "Activation; engagement; retention; funnels; cohorts"),
    src("SRC-PROGIT", "Pro Git", "Git project / Apress", "book", "download-open", "https://git-scm.com/book/en/v2", "Chapters 1–3, 5, 7, 10", version="2nd edition", note="Creative Commons; có EPUB/PDF chính thức."),
    src("SRC-GOOGLE-ENG", "Google Engineering Practices Documentation", "Google", "documentation", "local-official", "https://google.github.io/eng-practices/", "Code review guides", local_path="Material/DE/Reference/Library/knowledge/eng-practices/README.md"),
    src("SRC-SEGOOGLE", "Software Engineering at Google", "Google / O'Reilly", "book", "online-official", "https://abseil.io/resources/swe-book", "Culture; processes; tools; testing; build"),
    src("SRC-ODS", "Open Data Structures", "Pat Morin", "book", "download-open", "https://opendatastructures.org/", "Lists; queues; hash tables; trees; graphs; sorting", note="Bản HTML/PDF miễn phí từ tác giả."),
    src("SRC-N2T", "Nand2Tetris", "Nand2Tetris project", "course", "download-open", "https://www.nand2tetris.org/course", "Projects 1–6; lecture slides", note="Tài liệu chính thức miễn phí cho mục đích phi lợi nhuận."),
    src("SRC-COD", "Computer Organization and Design", "Patterson & Hennessy / Morgan Kaufmann", "book", "local-rights-review", "https://www.elsevier.com/books/computer-organization-and-design-mips-edition/patterson/978-0-12-407726-3", "Chapters xác định sau khi kiểm quyền và đọc", version="5th edition", local_path="Material/DE/Reference/Library/knowledge/hardware/Computer Organization and Design 5E - Patterson Hennessy - 0124077269.pdf", note="Tệp có sẵn; cần owner xác nhận quyền sử dụng."),
    src("SRC-OSTEP", "Operating Systems: Three Easy Pieces", "Arpaci-Dusseau & Arpaci-Dusseau", "book", "download-open", "https://pages.cs.wisc.edu/~remzi/OSTEP/", "Virtualization; concurrency; persistence", version="1.10", note="PDF chương miễn phí từ tác giả."),
    src("SRC-LINUX-MAN", "Linux man-pages project", "Linux man-pages project", "documentation", "online-official", "https://www.kernel.org/doc/man-pages/", "Processes; files; sockets; epoll; io_uring"),
    src("SRC-PY-ASYNC", "Coroutines and Tasks", "Python Software Foundation", "documentation", "online-official", "https://docs.python.org/3/library/asyncio-task.html", "TaskGroup; cancellation; timeout; structured concurrency"),
    src("SRC-IOURING", "io_uring(7)", "Linux man-pages / liburing", "specification", "online-official", "https://man7.org/linux/man-pages/man7/io_uring.7.html", "Submission/completion queues; asynchronous I/O"),
    src("SRC-RFC9293", "RFC 9293: Transmission Control Protocol", "IETF", "standard", "download-open", "https://www.rfc-editor.org/rfc/rfc9293.html", "TCP state machine; reliability; flow control"),
    src("SRC-RFC9110", "RFC 9110: HTTP Semantics", "IETF", "standard", "download-open", "https://www.rfc-editor.org/rfc/rfc9110.html", "Methods; status codes; caching; intermediaries"),
    src("SRC-RFC8446", "RFC 8446: TLS 1.3", "IETF", "standard", "download-open", "https://www.rfc-editor.org/rfc/rfc8446.html", "Handshake; keys; alerts; security properties"),
    src("SRC-OPENAPI", "OpenAPI Specification", "OpenAPI Initiative", "standard", "online-official", "https://spec.openapis.org/oas/latest.html", "Document structure; paths; schemas; security"),
    src("SRC-OWASP-API", "OWASP API Security Top 10", "OWASP", "standard", "online-official", "https://owasp.org/API-Security/editions/2023/en/0x11-t10/", "API risks and mitigations", version="2023"),
    src("SRC-DBT", "dbt Developer Hub", "dbt Labs", "documentation", "online-official", "https://docs.getdbt.com/", "Models; tests; documentation; semantic layer; metrics"),
    src("SRC-DUCKDB", "DuckDB documentation and publications", "DuckDB Foundation", "documentation", "online-official", "https://duckdb.org/why_duckdb", "Execution format; vectorized execution; storage; optimizer"),
    src("SRC-CLICKHOUSE", "ClickHouse Documentation", "ClickHouse", "documentation", "online-official", "https://clickhouse.com/docs", "Architecture; MergeTree; query optimization"),
    src("SRC-PARQUET", "Apache Parquet documentation and format", "Apache Software Foundation", "specification", "online-official", "https://parquet.apache.org/docs/", "File format; metadata; encodings; logical types"),
    src("SRC-AVRO", "Apache Avro Specification", "Apache Software Foundation", "specification", "online-official", "https://avro.apache.org/docs/current/specification/", "Schema; binary encoding; schema resolution"),
    src("SRC-ICEBERG", "Apache Iceberg Table Specification", "Apache Software Foundation", "specification", "online-official", "https://iceberg.apache.org/spec/", "Snapshots; manifests; partition evolution; concurrency"),
    src("SRC-DELTA", "Delta Lake Protocol", "Delta Lake project", "specification", "online-official", "https://github.com/delta-io/delta/blob/master/PROTOCOL.md", "Transaction log; protocol versions; table features"),
    src("SRC-AIRBYTE", "Airbyte Documentation", "Airbyte", "documentation", "online-official", "https://docs.airbyte.com/", "Replication; connectors; reliability"),
    src("SRC-SINGER", "Singer Specification", "Singer / Meltano", "specification", "online-official", "https://hub.meltano.com/singer/spec/", "SCHEMA; RECORD; STATE messages"),
    src("SRC-AIRFLOW", "Apache Airflow Core Concepts", "Apache Software Foundation", "documentation", "online-official", "https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/", "Architecture; DAGs; tasks; scheduling; retry; backfill"),
    src("SRC-GX", "Great Expectations Documentation", "Great Expectations", "documentation", "online-official", "https://docs.greatexpectations.io/docs/", "Expectations; validation; checkpoints; data docs"),
    src("SRC-OPENLINEAGE", "OpenLineage Specification", "OpenLineage project", "standard", "online-official", "https://openlineage.io/docs/spec/object-model/", "Jobs; runs; datasets; facets; naming"),
    src("SRC-W3C-PROV", "W3C PROV Family", "W3C", "standard", "download-open", "https://www.w3.org/TR/prov-overview/", "PROV-DM; PROV-O; PROV-N; constraints"),
    src("SRC-DDIA", "Designing Data-Intensive Applications, Second Edition", "O'Reilly Media", "book", "purchase-or-library", "https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/", "Chapters xác định sau khi có bản hợp pháp", version="2nd edition, 2026", note="Không dùng bản first edition có tên z-lib trong Library."),
    src("SRC-KAFKA", "Apache Kafka Documentation", "Apache Software Foundation", "documentation", "online-official", "https://kafka.apache.org/documentation/", "Design; protocol; operations; streams"),
    src("SRC-EVENT-SYSTEMS", "Designing Event-Driven Systems", "Ben Stopford / Confluent", "book", "local-official", "https://forum.confluent.io/t/free-book-designing-event-driven-systems/72", "Event streams; event sourcing; CQRS; streaming services", local_path="Material/DE/Reference/Library/knowledge/System-Design/20220311-EB-Designing_Event_Driven_Systems.pdf", note="Bản ebook miễn phí do Confluent phát hành; tệp local chưa đọc."),
    src("SRC-DEBEZIUM", "Debezium Documentation", "Debezium project", "documentation", "online-official", "https://debezium.io/documentation/reference/stable/", "Architecture; connectors; offsets; snapshots; guarantees"),
    src("SRC-SPARK", "Apache Spark Documentation", "Apache Software Foundation", "documentation", "online-official", "https://spark.apache.org/docs/latest/", "SQL; RDD; execution; tuning; structured streaming"),
    src("SRC-FLINK", "Apache Flink Documentation", "Apache Software Foundation", "documentation", "online-official", "https://nightlies.apache.org/flink/flink-docs-stable/", "Architecture; state; time; checkpoints; backpressure"),
    src("SRC-AWS-WAF", "AWS Well-Architected Framework", "Amazon Web Services", "framework", "download-open", "https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html", "Pillars; trade-offs; review process"),
    src("SRC-GCP-WAF", "Google Cloud Well-Architected Framework", "Google Cloud", "framework", "online-official", "https://cloud.google.com/architecture/framework", "Operational excellence; security; reliability; cost; performance"),
    src("SRC-AZURE-WAF", "Azure Well-Architected Framework", "Microsoft", "framework", "online-official", "https://learn.microsoft.com/en-us/azure/well-architected/", "Pillars; workloads; review"),
    src("SRC-DOCKER", "Docker Documentation", "Docker", "documentation", "online-official", "https://docs.docker.com/", "Images; containers; storage; networking; build"),
    src("SRC-TERRAFORM", "Terraform Documentation", "HashiCorp", "documentation", "online-official", "https://developer.hashicorp.com/terraform/docs", "Language; state; modules; workflow"),
    src("SRC-K8S", "Kubernetes Documentation", "Kubernetes project / CNCF", "documentation", "online-official", "https://kubernetes.io/docs/home/", "Workloads; services; config; storage; security; operations"),
    src("SRC-SRE", "Site Reliability Engineering", "Google", "book", "online-official", "https://sre.google/sre-book/table-of-contents/", "SLOs; monitoring; toil; incidents; capacity"),
    src("SRC-OTEL", "OpenTelemetry Documentation and Specification", "OpenTelemetry / CNCF", "standard", "online-official", "https://opentelemetry.io/docs/concepts/", "Signals; instrumentation; propagation; sampling"),
    src("SRC-NIST-CSF", "Cybersecurity Framework 2.0", "NIST", "framework", "download-open", "https://www.nist.gov/cyberframework", "Govern; identify; protect; detect; respond; recover", version="2.0"),
    src("SRC-NIST-AIRMF", "Artificial Intelligence Risk Management Framework", "NIST", "framework", "download-open", "https://www.nist.gov/itl/ai-risk-management-framework", "Govern; map; measure; manage", version="1.0"),
    src("SRC-OWASP-LLM", "OWASP Top 10 for LLM Applications", "OWASP", "standard", "online-official", "https://genai.owasp.org/llm-top-10/", "Risks; mitigations; testing"),
    src("SRC-OPENAI", "OpenAI API Documentation", "OpenAI", "documentation", "online-official", "https://developers.openai.com/api/docs", "Models; tools; evals; safety; production practices"),
]


MODULE_SOURCES = {
    "DA-M01": ["SRC-MSL-DA", "SRC-GOOGLE-TW"], "DA-M02": ["SRC-MS-EXCEL", "SRC-MS-PQ"],
    "DA-M03": ["SRC-PG17"], "DA-M04": ["SRC-KIMBALL", "SRC-MS-PQ", "SRC-DBT"],
    "DA-M05": ["SRC-OPENINTRO", "SRC-NIST-STAT"], "DA-M06": ["SRC-MS-PBI", "SRC-STORY"],
    "DA-M07": ["SRC-AMPLITUDE", "SRC-NIST-STAT", "SRC-STORY"], "DA-M08": ["SRC-TOCE", "SRC-OPENINTRO", "SRC-NIST-STAT"],
    "DA-M09": ["SRC-PYTHON", "SRC-PANDAS"], "DA-M10": ["SRC-GOOGLE-TW", "SRC-GOOGLE-ENG", "SRC-STORY"],
    "DA-M11": ["SRC-PG17", "SRC-OPENINTRO", "SRC-MS-PBI", "SRC-GOOGLE-TW"],
    "DE-M01": ["SRC-PROGIT", "SRC-GOOGLE-ENG"], "DE-M02": ["SRC-PYTHON", "SRC-PY-ASYNC"],
    "DE-M03": ["SRC-ODS", "SRC-PYTHON"], "DE-M04": ["SRC-N2T", "SRC-COD"],
    "DE-M05": ["SRC-OSTEP", "SRC-LINUX-MAN", "SRC-PY-ASYNC", "SRC-IOURING"],
    "DE-M06": ["SRC-RFC9293", "SRC-RFC9110", "SRC-RFC8446", "SRC-LINUX-MAN"],
    "DE-M07": ["SRC-SEGOOGLE", "SRC-GOOGLE-ENG", "SRC-PROGIT"],
    "DE-M08": ["SRC-OPENAPI", "SRC-OWASP-API", "SRC-RFC9110", "SRC-PG17"],
    "DE-M09": ["SRC-PG17"], "DE-M10": ["SRC-PG17", "SRC-OSTEP"],
    "DE-M11": ["SRC-KIMBALL", "SRC-DDIA"], "DE-M12": ["SRC-DBT", "SRC-KIMBALL"],
    "DE-M13": ["SRC-DDIA", "SRC-DBT", "SRC-MS-PBI"], "DE-M14": ["SRC-DUCKDB", "SRC-CLICKHOUSE", "SRC-COD"],
    "DE-M15": ["SRC-PARQUET", "SRC-AVRO", "SRC-ICEBERG", "SRC-DELTA"],
    "DE-M16": ["SRC-AIRBYTE", "SRC-SINGER", "SRC-RFC9110", "SRC-PY-ASYNC"],
    "DE-M17": ["SRC-DBT", "SRC-AIRFLOW"], "DE-M18": ["SRC-GX", "SRC-DBT", "SRC-OTEL"],
    "DE-M19": ["SRC-OPENLINEAGE", "SRC-W3C-PROV", "SRC-DBT"], "DE-M20": ["SRC-DDIA", "SRC-OSTEP"],
    "DE-M21": ["SRC-KAFKA", "SRC-EVENT-SYSTEMS"], "DE-M22": ["SRC-DEBEZIUM", "SRC-PG17", "SRC-KAFKA", "SRC-EVENT-SYSTEMS"],
    "DE-M23": ["SRC-SPARK", "SRC-FLINK", "SRC-COD"],
    "DE-M24": ["SRC-AWS-WAF", "SRC-GCP-WAF", "SRC-AZURE-WAF"],
    "DE-M25": ["SRC-DOCKER", "SRC-TERRAFORM", "SRC-K8S"],
    "DE-M26": ["SRC-SRE", "SRC-OTEL", "SRC-OWASP-API", "SRC-NIST-CSF"],
    "DE-M27": ["SRC-DDIA", "SRC-SRE", "SRC-SEGOOGLE", "SRC-EVENT-SYSTEMS"],
    "DE-M28": ["SRC-NIST-AIRMF", "SRC-OWASP-LLM", "SRC-OPENAI"],
    "DE-M29": ["SRC-SEGOOGLE", "SRC-SRE", "SRC-GOOGLE-ENG"],
}


def add_v2_sources():
    """Add categorized pack resources and Coursera paths; return IDs by pack/category."""
    kind_to_category = {
        "book": "book", "documentation": "document", "framework": "document",
        "handbook": "document", "specification": "document", "standard": "document",
        "course": "website",
    }
    for item in SOURCES:
        item["category"] = kind_to_category[item["kind"]]
        item["platform"] = None
        item["course_path"] = None

    canonical = {
        (item["category"], item["title"].casefold(), item["url"]): item["id"]
        for item in SOURCES
    }

    pack_ids = {}
    for pack_name, groups in PACKS.items():
        pack_ids[pack_name] = {}
        for category, resources in groups.items():
            ids = []
            for index, resource in enumerate(resources, 1):
                key = (category, resource["title"].casefold(), resource["url"])
                if key in canonical:
                    ids.append(canonical[key])
                    continue
                sid = f"PACK-{pack_name}-{category.upper()}-{index:02d}"
                ids.append(sid)
                SOURCES.append({
                    "id": sid, "title": resource["title"], "authority": resource["authority"],
                    "kind": category, "category": category, "access": resource["access"],
                    "url": resource["url"], "version": "selected-2026-09-26",
                    "locator": resource["locator"], "local_path": None,
                    "reading_status": "candidate-unread",
                    "provenance_status": "official-or-publisher-route-selected",
                    "note": "Module-pack source; page-level locator pending deep reading.",
                    "platform": None, "course_path": None,
                })
                canonical[key] = sid
            pack_ids[pack_name][category] = ids

    course_ids = {}
    for course_id, resource in COURSES.items():
        sid = f"COURSE-{course_id}"
        course_ids[course_id] = sid
        SOURCES.append({
            "id": sid, "title": resource["title"], "authority": resource["authority"],
            "kind": "course", "category": "course", "access": "coursera-enrollment",
            "url": resource["url"], "version": "verified-2026-09-26",
            "locator": resource["locator"], "local_path": None,
            "reading_status": "candidate-unread",
            "provenance_status": "coursera-page-verified",
            "note": "Course path verified at selection time; availability and syllabus can change.",
            "platform": "Coursera", "course_path": resource["locator"],
        })
    return pack_ids, course_ids


def union(groups):
    seen, result = set(), []
    for group in groups:
        for item in group:
            if item not in seen:
                seen.add(item); result.append(item)
    return result


def main():
    objectives_path = ACADEMIC / "objectives.json"
    data = json.loads(objectives_path.read_text(encoding="utf-8"))
    records = data["records"]
    pack_ids, course_ids = add_v2_sources()
    module_sources_v2 = {}
    for module_id, legacy_ids in MODULE_SOURCES.items():
        pack_name = MODULE_PACK[module_id]
        categorized = pack_ids[pack_name]
        module_sources_v2[module_id] = union([
            categorized["book"], categorized["document"], categorized["website"],
            categorized["video"], [course_ids[MODULE_COURSE[module_id]]], legacy_ids,
        ])
    source_ids = {s["id"] for s in SOURCES}
    modules = {r["id"] for r in records if r["kind"] == "module"}
    unknown = sorted({x for xs in module_sources_v2.values() for x in xs} - source_ids)
    if unknown or modules != set(module_sources_v2) or modules != set(MODULE_PACK) or modules != set(MODULE_COURSE):
        raise SystemExit(f"source map mismatch: unknown={unknown}; missing={sorted(modules-set(module_sources_v2))}; extra={sorted(set(module_sources_v2)-modules)}")
    children = defaultdict(list)
    for r in records:
        if r.get("parent_id"): children[r["parent_id"]].append(r["id"])
    assigned = {}
    for mid, ids in module_sources_v2.items():
        assigned[mid] = ids
        for lesson in children[mid]: assigned[lesson] = ids
    for r in records:
        if r["kind"] == "phase": assigned[r["id"]] = union([assigned[x] for x in children[r["id"]]])
    for programme in ("DA", "DE"):
        assigned[programme] = union([assigned[x] for x in children[programme]])
    missing = [r["id"] for r in records if not assigned.get(r["id"])]
    if missing: raise SystemExit(f"objectives without sources: {missing}")

    catalog = {"schema_version": 2, "generated_on": date.today().isoformat(),
               "status": "selection-v2-complete-reading-not-started",
               "policy": {"source_selection": "Primary standards, official documentation, original research, or books through legitimate publisher/author routes.",
                          "no_content_claim": "Selected does not mean read; chapter/page claims require the deep-reading gate.",
                          "rights": "local-rights-review files cannot support publication until the owner confirms usage rights.",
                          "minimum_per_module_and_lesson": {"book": 3, "document": 3, "website": 3, "video": 3, "course": 1},
                          "course_rule": "At least one Coursera course with a specific module/week locator."},
               "sources": SOURCES}
    (ACADEMIC / "source-catalog.json").write_text(json.dumps(catalog, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    source_by_id = {s["id"]: s for s in SOURCES}
    out = []
    for r in records:
        grouped_ids = defaultdict(list)
        for sid in assigned[r["id"]]:
            grouped_ids[source_by_id[sid]["category"]].append(sid)
        out.append({"objective_id": r["id"], "kind": r["kind"], "programme": r["programme"],
                    "parent_id": r.get("parent_id"), "title": r["title"], "source_ids": assigned[r["id"]],
                    "source_ids_by_category": dict(grouped_ids),
                    "mapping_basis": "module-core-bundle" if r["kind"] in {"module", "lesson"} else "roll-up-of-child-bundles",
                    "locator_status": "pending-deep-reading"})
    counts = defaultdict(int)
    for r in out: counts[r["kind"]] += 1
    plan = {"schema_version": 2, "generated_on": date.today().isoformat(),
            "status": "source-selection-v2-complete-awaiting-owner-acquisition",
            "objective_registry": str(objectives_path.relative_to(ROOT)), "counts": dict(counts), "records": out}
    (ACADEMIC / "source-plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")

    grouped, usage = defaultdict(list), defaultdict(list)
    for s in SOURCES: grouped[s["access"]].append(s)
    for mid, ids in module_sources_v2.items():
        for sid in ids: usage[sid].append(mid)
    lines = ["# Danh sách nguồn cần chuẩn bị", "",
             "> Cổng dừng của Bước 3. Danh sách này chọn nguồn cho toàn bộ DA và DE; chưa có nguồn nào được coi là đã đọc. Sau khi chuẩn bị xong, owner trả lời `done` để bắt đầu đọc sâu.", "",
             "## Phạm vi và nguyên tắc", "",
             f"- Registry được phủ: **{counts['programme']} chương trình · {counts['phase']} phase · {counts['module']} module · {counts['lesson']} bài**.",
             "- Mỗi module và bài có tối thiểu **3 sách · 3 document/spec · 3 website · 3 video · 1 Coursera course có path cụ thể**.",
             "- Bài kế thừa gói nguồn của module để bảo đảm baseline; ánh xạ đủ 525 bài nằm trong `Tools/Curriculum/Manifests/Academic/source-plan.json`.",
             "- Khi đọc sâu, từng bài sẽ khóa chapter/page/section/timestamp riêng và thay nguồn nếu gói module không đủ sát nội dung bài.",
             "- Docs/spec sống được đọc tại nguồn chính thức; không cần tải thủ công nếu chấp nhận đọc trực tuyến.",
             "- Sách thương mại chỉ lấy qua nhà xuất bản, thư viện hoặc bản đã mua hợp pháp.",
             "- Tệp local có nguồn gốc chưa xác nhận không được dùng làm căn cứ xuất bản.",
             "- Chương/trang chính xác được khóa sau khi đọc; bước này chỉ khóa nguồn và phạm vi chủ đề.", "",
             "## Việc owner cần làm", "", "### 1. Mua hoặc mượn thư viện", "",
             "| Mã | Nguồn | Phạm vi dùng | Đường lấy hợp pháp |", "|---|---|---|---|"]
    for s in grouped["purchase-or-library"]:
        lines.append(f"| `{s['id']}` | {s['title']} — {s['authority']} | {', '.join(usage[s['id']])} | [Nhà xuất bản]({s['url']}) |")
    lines += ["", "### 2. Xác nhận quyền sử dụng tệp đang có", "", "| Mã | Tệp | Phạm vi dùng | Yêu cầu |", "|---|---|---|---|"]
    for s in grouped["local-rights-review"]:
        lines.append(f"| `{s['id']}` | `{s['local_path']}` | {', '.join(usage[s['id']])} | Xác nhận bản được mua/cấp phép; nếu không, lấy qua [nhà xuất bản]({s['url']}). |")
    lines += ["", "### 3. Tải bản mở từ trang chính thức", "", "| Mã | Nguồn | Phạm vi dùng | Link chính thức |", "|---|---|---|---|"]
    for s in grouped["download-open"]:
        lines.append(f"| `{s['id']}` | {s['title']} — {s['authority']} | {', '.join(usage[s['id']])} | [Tải/đọc]({s['url']}) |")
    lines += ["", "## Course Coursera theo module", "",
              "| Module | Course | Path bắt buộc |", "|---|---|---|"]
    for mid in sorted(module_sources_v2):
        course = source_by_id[course_ids[MODULE_COURSE[mid]]]
        lines.append(f"| `{mid}` | [{course['title']}]({course['url']}) | {course['course_path']} |")
    lines += ["", "## Kiểm tra định lượng theo module", "",
              "| Module | Book | Document | Website | Video | Coursera |", "|---|---:|---:|---:|---:|---:|"]
    for mid in sorted(module_sources_v2):
        counter = defaultdict(int)
        for sid in module_sources_v2[mid]: counter[source_by_id[sid]["category"]] += 1
        lines.append(f"| `{mid}` | {counter['book']} | {counter['document']} | {counter['website']} | {counter['video']} | {counter['course']} |")
    lines += ["", "## Nguồn đọc trực tuyến, không cần tải thủ công", "",
              "Khi bước đọc sâu bắt đầu, locator sẽ ghi phiên bản hoặc ngày truy cập để tránh nội dung trôi theo thời gian.", "",
              "| Mã | Loại | Nguồn | Phạm vi dùng |", "|---|---|---|---|"]
    for access in ("online-official", "local-official", "online-open"):
        for s in grouped[access]:
            lines.append(f"| `{s['id']}` | {s['category']} | [{s['title']}]({s['url']}) — {s['authority']} | {', '.join(usage[s['id']])} |")
    lines += ["", "## Không dùng ở vòng đọc sâu", "",
              "- Mọi tệp mà `reference-inventory.json` ghi `provenance_status: review-required`.",
              "- Bản DDIA có chuỗi `z-lib` trong tên tệp local: không dùng; thay bằng bản mua/mượn hợp pháp `SRC-DDIA`.",
              "- Tài liệu tổng hợp trong `Computer Science/` vẫn là kho ứng viên cho tới khi xác minh tác giả, phiên bản và quyền sử dụng.", "",
              "## Điều kiện mở Bước 4", "",
              "Owner xác nhận đủ ba nhóm việc trên bằng từ khóa `done`. Nếu một sách chưa lấy được, ghi mã nguồn và phương án thay thế; không mặc nhiên coi là đã có."]
    request = ROOT / "Docs/Operations/SOURCE-REQUEST.md"
    request.write_text("\n".join(lines)+"\n", encoding="utf-8")
    print(json.dumps({"sources": len(SOURCES), "mapped_records": len(out), "counts": dict(counts), "request": str(request.relative_to(ROOT))}, ensure_ascii=False))


if __name__ == "__main__": main()
