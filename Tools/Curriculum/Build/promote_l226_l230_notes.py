#!/usr/bin/env python3
"""Build source-grounded L226-L230 Iceberg operation notes."""
from __future__ import annotations

import argparse
import json
import re

import promote_l221_l225_notes as base
from format_knowledge_notes import normalize_markdown
from promote_l201_l205_notes import Lesson

ROOT, PACK, WIKI = base.ROOT, base.PACK, base.WIKI
MODULE = base.MODULE
IS = base.IS
IR = "src.web.apache-iceberg-reliability"
IE = "src.web.apache-iceberg-evolution"
IM = "src.web.apache-iceberg-maintenance"
AV = "src.standard.apache-avro-1.12"
PG = "src.standard.protobuf-proto3-guide"
CR = "src.web.confluent-schema-evolution"
ISL = base.ISL
IRL = "SRC-APACHE-ICEBERG-RELIABILITY"
IEL = "SRC-APACHE-ICEBERG-EVOLUTION"
IML = "SRC-APACHE-ICEBERG-MAINTENANCE"
AVL = "SRC-APACHE-AVRO-1-12-SPEC"
PGL = "SRC-PROTOBUF-PROTO3-GUIDE"
CRL = "SRC-CONFLUENT-SCHEMA-EVOLUTION"

LESSONS = (
    Lesson(226, "Lesson_226-the-commit-protocol-and-atomic-visibility", "Iceberg Commit Protocol and Atomic Visibility", "114-iceberg-commit-protocol-atomic-visibility.md", "wiki.storage.iceberg-commit-protocol-atomic-visibility", "Files được ghi trước commit nhưng vì sao reader chỉ thấy một snapshot hoàn chỉnh?", (IS, IR), (ISL, IRL), (
        ("Ba pha của write", "Một write tạo data/delete files và metadata artifacts trước khi table state được công bố. Writer lập candidate snapshot/manifest tree trên base metadata đã load, rồi yêu cầu catalog atomically đổi current metadata location từ base sang candidate. Objects đã upload chưa thuộc table chỉ vì chúng tồn tại. Publication point là successful pointer swap. Tách prepare, validate và commit giúp xác định crash window, retry boundary và orphan candidates."),
        ("Reader snapshot isolation", "Reader resolve current metadata location rồi bind query vào snapshot cụ thể. Writer khác có thể commit sau đó nhưng query đang chạy tiếp tục dùng snapshot đã chọn, trừ khi engine chủ động refresh/replan theo contract khác. Vì snapshot liệt kê complete live file set, reader không directory-list để chắp table state. Atomic visibility là old snapshot hoặc new snapshot; nó không bảo đảm multi-table atomicity, external side effects hay business correctness."),
        ("Crash trước và sau commit", "Crash trước pointer swap để lại unreferenced files/metadata; table vẫn trỏ base snapshot. Crash sau successful swap nhưng trước client nhận response tạo outcome ambiguity: commit có thể đã thành công dù client thấy timeout. Retry mù có thể duplicate logical batch. Recovery phải query table history/snapshot summary hoặc application commit token, reconcile file/row identity rồi mới quyết định retry. Xóa objects theo job ID mà không reachability check có thể phá commit đã thành công."),
        ("Orphan xác định bằng reachability", "Orphan là file không reachable từ retained snapshots/metadata theo format và không thuộc in-flight writer hợp lệ. Tuổi file chỉ là safety guard, không phải proof. Cleanup retention phải lớn hơn maximum write duration, delayed retry, clock uncertainty và operational recovery window. Inventory cần normalize URI schemes/authorities theo tool guidance. Dry run lưu candidate set; trước delete phải refresh metadata và dùng operation/catalog guarantees phù hợp."),
        ("Time travel và rollback", "Retained snapshot history cho phép đọc state cũ hoặc rollback current reference, nhưng không hồi sinh files đã bị retention cleanup. Time travel verifies snapshot content; rollback là mutation tạo/đổi current state theo API semantics. Lab phải phân biệt `SELECT AS OF` với rollback, ghi snapshot IDs và key hashes. Snapshot expiration thay đổi recovery envelope; retention là product/operations decision, không chỉ cost setting."),
        ("Failure-injection lab", "Khóa engine/catalog/object store versions. Ghi batch có unique business keys; dừng sau data files, sau manifests, trước pointer swap và sau swap trước acknowledgment nếu harness cho phép. Ở mỗi điểm ghi object inventory, current metadata pointer, snapshot history, referenced files và canonical key hash. Reader phải thấy base hoặc committed candidate, không partial set. Xác định orphan candidates bằng manifests; time travel về base và current phải đối soát. Chưa chạy được post-commit ambiguity thì ghi limitation."),
    ), tuple(f"Commit-boundary probe {i}: candidate files, base pointer, atomic swap, reader snapshot và recovery decision phải nối được" for i in range(1, 16))),
    Lesson(227, "Lesson_227-optimistic-concurrency-and-conflict-detection", "Iceberg Optimistic Concurrency and Conflict Validation", "115-iceberg-optimistic-concurrency-conflict-validation.md", "wiki.storage.iceberg-optimistic-concurrency-conflict-validation", "Concurrent Iceberg writes xung đột ở đâu và khi nào có thể rebase/retry an toàn?", (IS, IR), (ISL, IRL), (
        ("Optimistic protocol", "Hai writers đọc cùng base metadata, tạo immutable files và candidate metadata độc lập. Chỉ một compare-and-swap current metadata location thắng. Loser không được đổi pointer bằng candidate cũ; nó refresh current state, kiểm operation assumptions rồi re-apply metadata action khi safe. Atomic-swap conflict là concurrency signal, chưa đủ kết luận data conflict. Validation semantics của append, overwrite, row-level delete và rewrite khác nhau."),
        ("Append versus overlapping changes", "Concurrent appends thường có thể rebase vì mỗi bên thêm disjoint new files, miễn operation constraints vẫn đúng. Dynamic overwrite, replace partitions, delete/update hoặc compaction có thể chạm files/rows mà commit khác đã thay đổi. Retry chỉ an toàn khi predicates/files/sequence assumptions được validate trên new base. Gọi mọi conflict là retryable gây lost update; gọi mọi CAS failure là fatal làm giảm concurrency vô ích."),
        ("Ba lớp conflict", "Catalog conflict: current metadata pointer đổi trước swap. File-set conflict: files operation dự định rewrite/delete không còn live hoặc new matching files xuất hiện trong validation scope. Semantic conflict: hai writes hợp lệ ở format layer nhưng vi phạm business uniqueness, balance hoặc version rule. Format validation có thể bắt hai lớp đầu tùy operation/isolation; semantic conflict cần key/invariant reconciliation hoặc upstream coordination."),
        ("Retry budget", "Retry loop có maximum attempts, elapsed deadline, exponential backoff+jitter và classification. Metadata planning có thể reuse manifests/data files nhưng candidate metadata/sequence phải cập nhật theo spec. Thundering herd làm catalog pressure tăng; throughput collapse cần đo commit latency, conflicts/attempt, attempts/commit và abandoned files. Sau budget exhaustion, operation báo failure có evidence; không che bằng infinite retry."),
        ("Không mất thay đổi", "Success của hai clients không đủ chứng minh both effects present. Oracle xây expected key/file delta cho mỗi writer, đọc committed snapshot rồi reconcile union, deletes và invariants. Snapshot summaries hỗ trợ trace nhưng không thay row-level oracle. Với compaction, row/key set giữ nguyên dù files đổi. Với overwrite, explicit conflict policy quyết định serialized result. Test capture base/current/candidate snapshot IDs và exact validation error."),
        ("Concurrency lab", "Chạy append/append, append versus partition overwrite, và compaction versus delete/rewrite trên cùng base barrier. Pin isolation/validation settings. Ghi winner, loser, retry path, files reused, orphans và final key hash. Tăng writers theo steps; đo throughput useful commits, p95 commit latency, conflict ratio và object/metadata amplification. Ngưỡng collapse là workload observation kèm environment, không universal constant. Map mỗi failure sang retry, re-plan hoặc human intervention."),
    ), tuple(f"Concurrency probe {i}: conflict layer, validation assumption, retry class và final-state oracle phải rõ" for i in range(1, 16))),
    Lesson(228, "Lesson_228-hidden-partitioning-partition-evolution-and-schema-field-ids", "Iceberg Hidden Partition Schema and Field ID Evolution", "116-iceberg-hidden-partition-schema-field-id-evolution.md", "wiki.storage.iceberg-hidden-partition-schema-field-id-evolution", "Field IDs và partition specs cho phép dữ liệu cũ/mới cùng tồn tại mà query vẫn đúng thế nào?", (IS, IE), (ISL, IEL), (
        ("Field identity", "Iceberg assigns stable field IDs; data-file projection binds IDs rather than current names/positions. Rename changes display name while preserving ID, nên old files map đúng field. Drop rồi add cùng name tạo identity mới; không được đọc old values như field mới. Reorder không đổi identity. Type widening chỉ trong allowed promotions và partition transforms impose extra restrictions. External files thiếu IDs cần name mapping/careful migration."),
        ("Hidden partitioning", "Partition spec defines transforms from source field IDs: identity, year/month/day/hour, bucket, truncate. Users query logical columns; planner projects predicate through each spec instead of yêu cầu path predicates. Partition values vẫn là metadata dùng pruning nhưng không phải application columns bắt buộc. Transform projection thường conservative, giữ candidate có thể match. Hidden partitioning giảm coupling giữa SQL và physical layout nhưng engine support cần verify."),
        ("Partition evolution", "Đổi month sang day tạo spec mới cho writes mới; old files giữ old spec và layout. Planner split-plans files theo spec ID, derive filter tương ứng rồi union results. Evolution là metadata operation và không eagerly rewrite old files. Performance có thể heterogeneous; correctness oracle phủ boundary giữa old/new regions. Muốn homogenize layout phải compaction/rewrite riêng với cost/recovery plan."),
        ("Schema evolution boundary", "Add, drop, rename, reorder và supported widen changes có format semantics. Default values, nested fields, map keys và partition sources có constraints. Format không phát hiện business meaning change giữ same type/ID, như cents sang dollars. Cross-engine connector có thể expose IDs khác, cache stale schema hoặc write older format version. Compatibility matrix phải có old/new writers/readers và semantic invariants."),
        ("Pruning qua nhiều specs", "Query event_time range được transform thành month domain cho spec cũ và day domain cho spec mới. Manifest partition summaries và file entries dùng spec-specific tuples. Report files/manifests pruned riêng từng spec; total alone che regression ở one region. Boundary values quanh month/day, timezone and transform semantics cần fixtures. Query result phải reconcile canonical source independent of partitioning."),
        ("Evolution lab", "Tạo table partitioned month, load old period; commit spec day, load new period without rewriting old files. Rename field giữ ID và widen allowed type. Capture schemas/specs by ID, metadata tree, file→spec mapping và plans. Query spans both periods plus boundaries; compare key/value hash with hand oracle. Verify old data via new name, no identity leakage after rename, and pruning counters in both specs. Negative test drop+add same name remains distinct."),
    ), tuple(f"Evolution probe {i}: field ID, spec ID, old/new file region, predicate transform và result oracle phải hiện đủ" for i in range(1, 16))),
    Lesson(229, "Lesson_229-maintenance-project-deletes-compaction-and-safe-cleanup", "Iceberg Maintenance Compaction Retention and Cleanup", "117-iceberg-maintenance-compaction-retention-cleanup.md", "wiki.storage.iceberg-maintenance-compaction-retention-cleanup", "Compaction, delete-file maintenance, snapshot expiration và orphan cleanup chạy an toàn theo thứ tự nào?", (IS, IR, IM), (ISL, IRL, IML), (
        ("Bốn công việc khác nhau", "Data-file compaction rewrite many small files into fewer target files. Manifest rewrite reorganizes metadata for planning. Position-delete rewrite compacts/filter dangling delete records; dangling-file removal may remove whole delete files under defined conditions. Snapshot expiration removes history references and can delete files no longer reachable. Orphan cleanup targets unreferenced physical objects. Gộp các lệnh thành một chữ cleanup che khác biệt về correctness, rollback và concurrency."),
        ("Compaction concurrent writes", "Rewrite operation selects input files on base snapshot and produces replacements. Commit validates selected inputs remain valid; concurrent append can coexist, nhưng concurrent delete/rewrite touching inputs may invalidate candidate. On retry, reusable outputs depend on validation and implementation. Final reconciliation requires same logical rows after applying deletes, plus concurrent writer delta exactly once. File count/latency improvement chỉ đo sau correctness."),
        ("Retention envelope", "Snapshot retention derives from time-travel users, rollback RTO, delayed readers/jobs, branch/tag policy, audit/legal holds and maximum incident detection/recovery. Expiring snapshot removes it from metadata; files delete only when no retained reference. Minimum snapshots and age settings interact. Configuration example is not policy. Before expiration capture references, consumers and oldest required snapshot; after expiration verify intended snapshots gone and required ones readable."),
        ("Orphan cleanup safety", "Unreferenced file may belong to in-progress writer. Official guidance warns retention shorter than maximum write duration can corrupt table. Safe lower bound includes longest write, retries, queue pauses, clock skew and operational margin. Normalize paths/schemes carefully. Run dry-run inventory, sample/classify candidates, refresh current tree, execute with bounded prefix and log deletes. Shared files or tables invalidate simple prefix ownership assumptions."),
        ("Delete files", "Equality and position deletes have sequence/application rules. Compaction may materialize deletes into rewritten data files, while rewritePositionDeletes compacts delete files and filters dangling records for selected scope. Removing a delete file still applicable to live data resurrects rows. Oracle must compare business keys/values across snapshots, not raw data-file row counts. Measure delete-file count, metadata size, scan CPU/I/O and read amplification."),
        ("Maintenance project", "Generate small files and delete files with known canonical state. Record baseline snapshots, row hash, file/manifest/delete counts, plan/scan metrics. Run compaction while controlled writer appends; reconcile both effects. Apply snapshot expiration with justified retention, test retained time travel. Dry-run then remove orphans with retention above observed maximum write plus margin. Roll back/read prior retained snapshot where policy permits. Store all operation IDs and exact candidate/deleted lists."),
    ), tuple(f"Maintenance probe {i}: operation scope, retained references, concurrent-write boundary, candidate set và row oracle phải rõ" for i in range(1, 16))),
    Lesson(230, "Lesson_230-gate-6-explain-a-metadata-chain-and-survive-a-concurrent-write", "Gate 6 Metadata Concurrency Compatibility and Engine Evidence", "118-gate-6-metadata-concurrency-compatibility-engine-evidence.md", "wiki.storage.gate6-metadata-concurrency-compatibility-engine-evidence", "Một bài cổng chứng minh được metadata lineage, atomic concurrency, schema compatibility và engine decision ra sao?", (IS, IR, IM, AV, PG, CR), (ISL, IRL, IML, AVL, PGL, CRL), (
        ("Evidence pack", "Candidate nộp immutable evidence pack: environment/versions, dataset/schema hashes, commands/config, current/base snapshot IDs, metadata paths/hashes, plans/counters, raw compatibility bytes và canonical outputs. Screenshots không thay machine-readable artifacts. Mỗi answer claim trỏ artifact/run ID. Files hoặc logs thiếu lineage không được dùng để suy. Gate chấm năng lực giải thích và tái hiện, không chấm độ dài."),
        ("Columnar attribution", "Phần A tách projection pushdown, row-group/file pruning, page skipping và encoding/compression/vectorized execution. Mỗi mechanism có controlled comparison, correctness hash và metric riêng. Latency alone không phân biệt cache/CPU/I/O. Candidate nêu metric unavailable là unknown. Writer geometry/recommendation có workload threshold và reversal condition."),
        ("Distributed diagnosis", "Phần B phân queue delay khỏi execution, skew khỏi uniform saturation, spill khỏi source/network throttling. Timeline đồng bộ stage/task/worker and scheduler metrics. Diagnosis nêu causal chain và counterfactual intervention; symptom list không đạt. Không cần production outage thật; controlled trace/fixture đủ nếu provenance rõ."),
        ("Metadata và concurrent write", "Phần C trace catalog pointer→metadata JSON→snapshot→manifest list→manifest→data/delete file và one row visibility. Phần D chạy concurrent operations, capture base/candidate/current, exact conflict validation, retry path và final-state reconciliation. Xóa file bằng tay phá format invariants nên điểm zero. Atomic visibility chỉ table boundary; candidate phải nêu retained-snapshot/orphan implications."),
        ("Compatibility và engine ADR", "Phần E dùng writer-reader 4-cell matrix plus multi-version history, structural and semantic oracles; Avro defaults/aliases hoặc Protobuf tags được giải thích đúng format. Phần F chọn engine từ workload contract, hard constraints, measured evidence, cost boundary và reversals. Feature list/vendor claim không thay benchmark. Every recommendation has uncertainty and unsupported alternatives."),
        ("Rubric và remediation", "Threshold tổng 70/100 nhưng C,D floor 60% bảo vệ core correctness. Evidence missing, fabricated lab claim hoặc canonical mismatch là critical failure. Reviewer independently replays sample hashes/metadata path and one compatibility cell. Remediation maps failed competency to specific lab, not generic reread. Gate version pins specs/tool versions; owner approval remains separate from test pass."),
    ), tuple(f"Gate-6 probe {i}: claim, artifact locator, independent oracle, critical failure và remediation phải kiểm được" for i in range(1, 16))),
)

QUERIES = {
    226: ["Iceberg atomic visibility hoạt động thế nào?", "Commit timeout ambiguity xử lý ra sao?", "Orphan file xác định bằng gì?"],
    227: ["Iceberg optimistic conflict có mấy lớp?", "Khi nào append retry an toàn?", "Chứng minh concurrent writes không mất update thế nào?"],
    228: ["Iceberg field ID bảo vệ rename thế nào?", "Partition evolution query old new specs ra sao?", "Hidden partitioning có giới hạn gì?"],
    229: ["Iceberg compaction khác snapshot expiration thế nào?", "Orphan cleanup retention lấy từ đâu?", "Delete-file maintenance kiểm correctness ra sao?"],
    230: ["Gate 6 cần evidence gì?", "Metadata chain được chấm ra sao?", "Concurrent write và compatibility critical failures là gì?"],
}

NEW = (
    (IR, "1_Nguon/Web/SRC-APACHE-ICEBERG-RELIABILITY.md", "https://iceberg.apache.org/docs/latest/reliability/", "Apache-2.0-public-documentation"),
    (IE, "1_Nguon/Web/SRC-APACHE-ICEBERG-EVOLUTION.md", "https://iceberg.apache.org/docs/latest/evolution/", "Apache-2.0-public-documentation"),
    (IM, "1_Nguon/Web/SRC-APACHE-ICEBERG-MAINTENANCE.md", "https://iceberg.apache.org/docs/latest/maintenance/", "Apache-2.0-public-documentation"),
)


def folder(lesson: Lesson):
    return MODULE / lesson.directory


def contract(lesson: Lesson):
    note = (folder(lesson) / "note.md").read_text()
    after_path = folder(lesson) / "after-note.md"
    after = after_path.read_text() if after_path.exists() else ""
    def pick(text: str, label: str):
        match = re.search(rf"(?m)^\*\*{re.escape(label)}\.\*\*\s*(.+)$", text)
        return match.group(1).strip() if match else ""
    old = tuple(pick(note, label) for label in ("Outcome", "Đánh giá", "Lab", "Pitfalls", "Self-study (2,4 giờ)", "Done when"))
    if all(old): return old
    tasks = re.findall(r"(?m)^\*\*Nhiệm vụ\.\*\*\s*(.+)$", after)
    return pick(note, "Năng lực cần chứng minh"), pick(after, "Cách đánh giá"), tasks[0] if tasks else "", pick(after, "Lỗi cần chủ động loại trừ"), tasks[1] if len(tasks) > 1 else "", pick(note, "Điều kiện hoàn thành")


def curriculum(lesson: Lesson, knowledge: str):
    outcome, assessment, lab, pitfalls, self_study, done = contract(lesson)
    heading = f"# Phase 6: Analytical Storage and Query Engines\n# Module 15: File, Serialization and Open Table Formats\n# Lesson {lesson.number}: {lesson.title}"
    body = re.sub(r"^---\n.*?\n---\n", "", knowledge, flags=re.S)
    body = re.sub(r"^# .+\n+", "", body, count=1)
    note = f"{heading}\n\n## Mục tiêu bài học\n\n**Năng lực cần chứng minh.** {outcome}\n\n**Điều kiện hoàn thành.** {done}\n\n{body}"
    after = f"{heading}\n\n## Thực hành\n\n**Nhiệm vụ.** {lab}\n\nChỉ dùng fixture tổng hợp và môi trường cô lập. Lưu input/schema hashes, versions, commands, metadata, plans, counters, outputs, logs và limitations.\n\n## Kiểm tra cuối bài\n\n1. Nêu publication hoặc identity boundary.\n2. Đưa failure/counterexample có thể tái hiện.\n3. Phân biệt format guarantee với implementation observation.\n4. Nêu reconciliation oracle và reversal condition.\n\n## Tiêu chí hoàn thành\n\n**Cách đánh giá.** {assessment}\n\n**Điều kiện đạt.** {done}\n\n## Bài làm sau buổi học\n\n**Nhiệm vụ.** {self_study}\n\n**Lỗi cần chủ động loại trừ.** {pitfalls}\n\n## Reference\n\n- Knowledge note: `{(PACK / lesson.filename).relative_to(ROOT)}`\n- Nội dung học thuật: `note.md` cùng thư mục.\n"
    return note, after


def manifest(check=False):
    path = ROOT / "Docs/Second-Brain/second-brain-manifest.json"
    data = json.loads(path.read_text())
    source_ids = {row[0] for row in NEW}
    data["source_registry"] = [row for row in data["source_registry"] if row.get("source_id") not in source_ids] + [{"source_id": sid, "record_path": record, "canonical_url": url, "captured": "2026-10-02", "rights": rights} for sid, record, url, rights in NEW]
    note_ids = {lesson.note_id for lesson in LESSONS}
    data["note_registry"] = [row for row in data["note_registry"] if row.get("note_id") not in note_ids]
    data["retrieval_test_set"] = [row for row in data["retrieval_test_set"] if row.get("expected_note_id") not in note_ids]
    for lesson in LESSONS:
        data["note_registry"].append({"note_id": lesson.note_id, "path": f"2_Wiki/Database-Systems/{lesson.title}.md", "status": "review", "source_ids": list(lesson.sources), "last_verified": "2026-10-02"})
        data["retrieval_test_set"].extend({"query": query, "expected_note_id": lesson.note_id} for query in QUERIES[lesson.number])
    data.update({"version": "1.0.45", "updated_at": "2026-10-02T23:59:00+07:00"})
    data["layers"]["1_Nguon"]["source_count"] = len(data["source_registry"])
    data["layers"]["2_Wiki"]["note_count"] = len(data["note_registry"])
    expected = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    if check: return [] if path.read_text() == expected else [str(path.relative_to(ROOT))]
    path.write_text(expected); return []


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--check", action="store_true"); args = parser.parse_args(); stale = []
    for lesson in LESSONS:
        knowledge = normalize_markdown(base.deep(lesson)); note, after = curriculum(lesson, knowledge)
        for path, content in ((PACK / lesson.filename, knowledge), (WIKI / f"{lesson.title}.md", knowledge), (folder(lesson) / "note.md", note), (folder(lesson) / "after-note.md", after)):
            if args.check:
                if not path.exists() or path.read_text() != content: stale.append(str(path.relative_to(ROOT)))
            else: path.write_text(content)
    stale += manifest(args.check)
    if stale: print("STALE\n" + "\n".join(stale)); return 1
    print(("checked" if args.check else "written") + f"={len(LESSONS) * 4} stale=0"); return 0


if __name__ == "__main__": raise SystemExit(main())
