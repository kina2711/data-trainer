#!/usr/bin/env python3
"""Build source-grounded L221-L225 Parquet and Iceberg notes."""
from __future__ import annotations

import argparse
import json
import re

import promote_l216_l220_notes as previous
from format_knowledge_notes import normalize_markdown
from promote_l201_l205_notes import Lesson

ROOT = previous.ROOT
PACK = previous.PACK
WIKI = previous.WIKI
MODULE = ROOT / "Material/DE/Curriculum/Phase_06-analytical-storage-and-query-engines/Module_15-file-serialization-and-open-table-formats"

PF = "src.spec.apache-parquet-file-format"
PI = "src.spec.apache-parquet-page-index"
PE = "src.web.apache-parquet-encodings"
DP = "src.web.duckdb-parquet-pushdown"
DZ = "src.web.duckdb-zonemaps"
IS = "src.spec.apache-iceberg-current"
II = "src.web.apache-iceberg-introduction"
FD = "src.book.reis-housley-fundamentals-data-engineering"

PFL = "SRC-APACHE-PARQUET-FILE-FORMAT"
PIL = "SRC-APACHE-PARQUET-PAGE-INDEX"
PEL = "SRC-APACHE-PARQUET-ENCODINGS"
DPL = "SRC-DUCKDB-PARQUET-PUSHDOWN"
DZL = "SRC-DUCKDB-ZONEMAPS"
ISL = "SRC-APACHE-ICEBERG-SPEC"
IIL = "SRC-APACHE-ICEBERG-INTRODUCTION"
FDL = "SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING"

LESSONS = (
    Lesson(
        221,
        "Lesson_221-parquet-internals-row-group-column-chunk-page",
        "Parquet File Row Group Column Chunk and Page",
        "109-parquet-file-row-group-column-chunk-page.md",
        "wiki.storage.parquet-file-row-group-column-chunk-page",
        "Đọc footer Parquet thế nào để phân biệt đơn vị bố trí, pruning và I/O thực tế?",
        (PF, PE, DP, FD),
        (PFL, PEL, DPL, FDL),
        (
            ("Bốn tầng vật lý", "Một Parquet file chứa nhiều row groups. Trong mỗi row group, mỗi leaf column có một column chunk liên tục; column chunk lại gồm data pages và có thể có dictionary page. Page là đơn vị encoding/compression nhỏ, row group là horizontal partition logic của file, còn column chunk là phần dữ liệu của một cột trong đúng row group. Gọi row group là block lưu trữ vật lý hoặc gọi page là cột đều làm sai phép đo. Nested field được hạ xuống leaf columns kèm definition/repetition levels, nên số cột logic và số column chunks không luôn trùng cách người học nhìn schema."),
            ("Footer và đường đọc", "File bắt đầu và kết thúc bằng magic bytes; ngay trước magic cuối là độ dài footer và FileMetaData. Reader thường lấy phần đuôi để biết schema, row groups, column chunk offsets, codecs, encodings, statistics và các index locations có mặt. Footer cho biết nơi cần đọc, không phải bằng chứng bytes đã đi qua network. Một engine có thể prefetch, cache, coalesce ranges hoặc đọc metadata qua catalog. Báo cáo phải tách logical bytes, compressed bytes, requested ranges, transferred bytes và bytes decoded."),
            ("Statistics và pruning boundary", "Min, max, null count và distinct count nếu có được gắn ở scope cụ thể. Row-group statistics có thể loại cả row group khi predicate chứng minh không giao miền; page index có thể loại pages khi writer tạo index và reader sử dụng. Thiếu statistics, truncated bounds, NaN, null semantics hoặc collation khác làm pruning yếu hay không an toàn. Statistics là conservative evidence: giữ thêm false positives được, bỏ false negatives thì sai dữ liệu. Footer inspection phải ghi cột nào có statistic và scope nào thực sự được reader dùng."),
            ("Kích thước row group", "Row group lớn tăng sequential I/O và thường cải thiện compression do nhiều giá trị chung, nhưng writer cần buffer lớn hơn, selective query có granularity thô hơn và parallelism bị giới hạn khi có ít groups. Row group nhỏ tăng scheduling/metadata overhead và có thể làm dictionary kém hiệu quả, nhưng tạo nhiều đơn vị pruning và tasks. Con số 512 MB–1 GB trong tài liệu Parquet gắn bối cảnh HDFS; object store, memory, query selectivity và engine concurrency cần benchmark riêng. Quyết định phải dựa vào workload, không sao chép default."),
            ("Page, encoding và codec", "Writer chọn encoding theo page/column behavior; dictionary có thể fallback, RLE/delta/plain phục vụ shapes khác nhau. Sau encoding, codec nén page hoặc chunk theo format/version. Page size cân bằng header overhead, decoding granularity và point/range read. Page không nhất thiết là network I/O request: engine có thể đọc range lớn chứa nhiều pages. Footer chỉ mô tả selected metadata; xác nhận encoding bằng metadata tool, xác nhận decode/I/O bằng profiler hoặc engine counters."),
            ("Lab ba cấu hình", "Ghi cùng canonical dataset với ba target row-group sizes bằng một writer/version đã pin. Đọc footer, ghi file size, group count, rows/group, column compressed/uncompressed sizes, encodings, statistics và page-index presence. Chạy full scan, projection-only, selective filter và combined query ở cold/warm states được định nghĩa. Đối soát typed result hash trước performance. Chọn cấu hình bằng bytes transferred, pruned groups/pages, peak memory và latency distribution; nếu metric page pruning không quan sát được thì ghi unknown, không suy từ latency."),
        ),
        tuple(f"Parquet hierarchy probe {i}: scope, metadata, counterexample và observed I/O phải khớp" for i in range(1, 16)),
    ),
    Lesson(
        222,
        "Lesson_222-encoding-choice-statistics-and-pushdown",
        "Parquet Statistics and Pushdown Evidence",
        "110-parquet-statistics-pushdown-evidence.md",
        "wiki.storage.parquet-statistics-pushdown-evidence",
        "Chứng minh riêng projection pushdown, row-group pruning và page skipping bằng bằng chứng nào?",
        (PF, PI, PE, DP, DZ),
        (PFL, PIL, PEL, DPL, DZL),
        (
            ("Ba cơ chế độc lập", "Projection pushdown bỏ đọc leaf columns không cần cho output, predicate hoặc join. Filter pushdown chuyển predicate xuống scan để metadata hay reader loại dữ liệu sớm. Pruning là hệ quả ở một granularity: partition, file, row group hay page. Một query chọn ít cột và lọc hẹp có thể dùng cả hai; muốn quy công phải dựng cells projection-only, filter-only, both và neither. Optimizer plan chỉ chứng minh intent; scan counters, requested ranges và result oracle mới chứng minh execution."),
            ("Encoding khác compression", "PLAIN, dictionary, RLE/bit-packing và delta encodings biến đổi representation theo data type/pattern. Codec như Snappy, Zstd hoặc gzip nén encoded bytes ở lớp khác. Dictionary giúp repeated low-cardinality values nhưng dictionary page có thể quá lớn hoặc writer fallback. Sorted data có thể hỗ trợ delta/RLE và tight min/max cùng lúc; không được gán toàn bộ lợi ích cho encoding. Lab giữ codec cố định khi so encoding, rồi giữ encoding/writer policy cố định khi so codec."),
            ("Statistics có điều kiện", "Min/max chỉ loại unit khi predicate và ordering semantics cho phép chứng minh miền không giao. Null count hỗ trợ một số null predicates; distinct count không phải exact index. Strings có thể bị truncate; timestamps/decimals cần physical/logical interpretation; NaN phá trực giác ordering. Writer có thể omit statistics vì size hoặc type; reader có thể bỏ qua metadata không đáng tin. Mỗi claim nêu writer, format version, field, metadata presence và exact predicate."),
            ("Page index", "ColumnIndex giữ value bounds/null pages; OffsetIndex nối row indices với page offsets để reader căn các projected columns. Ordered columns cho phép binary search; unordered columns thường scan bounds. Index nằm tách khỏi row group để full scans không bắt buộc trả I/O/deserialization cost. Đây không phải secondary index và không trả row location toàn bảng. Page index là optional; compatibility với older readers và generated metadata phải được kiểm bằng file inspection cùng reader counters."),
            ("Thiết kế attribution", "Bốn file configurations gồm unsorted/no page index, sorted, page-indexed và sorted+indexed. Trên từng file chạy query matrix: all columns/no filter; narrow columns/no filter; all columns/selective filter; narrow columns/selective filter. Mỗi run khóa cache state, concurrency, projection, predicate, repetition và output hash. Contribution không nhất thiết cộng tuyến tính do metadata, prefetch, decompression và cache interactions; nếu tổng riêng lệch phép đo both thì báo interaction thay vì ép cộng."),
            ("Kết luận writer policy", "Writer policy chỉ được chọn sau khi đo workload mix, file count, row-group/page geometry, selectivity, CPU, bytes và memory. Sort key cải thiện bounds nhưng tốn shuffle/sort và có thể gây skew. Page index tăng metadata/write work; lợi ích phụ thuộc reader support. Recommendation ghi threshold và reversal: selectivity đổi, reader không dùng index, ingest SLA bị vi phạm hoặc storage/CPU cost đổi. Dùng same semantic dataset và versioned configuration để quyết định có thể tái hiện."),
        ),
        tuple(f"Pushdown attribution probe {i}: plan intent, metadata presence, scan counters và result oracle phải tách riêng" for i in range(1, 16)),
    ),
    Lesson(
        223,
        "Lesson_223-nested-schemas-timestamps-and-decimal-interoperability",
        "Nested Timestamp and Decimal Interoperability",
        "111-nested-timestamp-decimal-interoperability.md",
        "wiki.storage.nested-timestamp-decimal-interoperability",
        "Round-trip nested data, timestamp và decimal qua nhiều engine thế nào để phát hiện sai nghĩa?",
        (PF, IS, FD),
        (PFL, ISL, FDL),
        (
            ("Interoperability là typed equality", "Cùng đọc được file chỉ chứng minh parser chấp nhận bytes. Interoperability cần canonical logical schema, value semantics và equality oracle. So row count hoặc aggregate có thể che nested order, null versus empty, precision loss và timezone shift. Fixture phải có stable row key; mỗi engine xuất canonical representation để so từng field. Mismatch được phân loại thành schema mapping, writer encoding, reader conversion, API representation hoặc application normalization."),
            ("Nested levels", "Parquet lưu leaf values cùng definition levels để biểu diễn optionality và repetition levels để biểu diễn list boundaries trong cấu trúc lồng. Các LIST/MAP encodings lịch sử và generated schemas có thể khác shape dù nhìn gần giống. Fixture phải phân biệt missing parent, null child, empty list, list containing null, empty map và nested repeated records. Flatten rồi rebuild không phải oracle nếu nó làm mất parent/position identity. So canonical JSON có explicit states và stable ordering rule."),
            ("Timestamp semantics", "Timestamp cần unit, timezone adjustment contract và meaning. Milliseconds, microseconds và nanoseconds khác precision; một engine có thể truncate hoặc reject. Instant with offset, local wall-clock time và calendar date là ba concepts. DST gap/overlap, pre-epoch values, leap-related boundaries và writer timezone cần fixture. Legacy INT96 có engine-specific behavior; nếu xuất hiện phải pin reader options. So epoch instant cho instant fields và local components plus zone policy cho local fields."),
            ("Decimal semantics", "Decimal mang precision và scale; physical storage có thể là int32, int64 hoặc fixed/byte array. Reader mapping sang binary floating point làm mất exactness. Fixture gồm max/min precision, trailing zeros, negative, rounding boundary và overflow. Equality business có thể quan tâm numeric value hoặc representation scale; contract phải chọn. Writer không được silently round nếu policy yêu cầu reject. Canonical oracle dùng unscaled integer cùng scale hoặc decimal string chuẩn hóa theo rule đã công bố."),
            ("Cross-engine matrix", "Chọn ít nhất hai engines nhưng ghi exact versions, connectors, session timezone, schema options và language driver. Mỗi engine vừa làm writer vừa làm reader để tạo W_A→R_A, W_A→R_B, W_B→R_A, W_B→R_B. Lưu file hash, footer schema, inferred schema, typed output và warnings. Một mismatch được sửa ở writer contract nếu có thể; workaround chỉ ở reader phải được ghi như compatibility debt và có test ngăn regression."),
            ("Automation", "Golden corpus nhỏ nhưng bao phủ states được version control cùng expected canonical values. Pipeline đọc tất cả files bằng tất cả supported readers, normalize theo contract rồi diff per key/field. Negative fixtures phải reject: decimal overflow, unsupported timestamp precision, invalid nested schema. Khi nâng engine/library, chạy lại matrix trước deploy. Không tự regenerate expected output bằng code đang được kiểm; owner duyệt thay đổi oracle và ghi migration rationale."),
        ),
        tuple(f"Interoperability probe {i}: writer-reader version, typed fixture, canonical value và mismatch class phải hiện đủ" for i in range(1, 16)),
    ),
    Lesson(
        224,
        "Lesson_224-object-store-limits-and-why-a-table-format-exists",
        "Object Store File Format and Table Format Boundaries",
        "112-object-store-file-table-format-boundaries.md",
        "wiki.storage.object-store-file-table-format-boundaries",
        "Object store, file format và table format giải quyết ba lớp vấn đề khác nhau ra sao?",
        (IS, II, FD),
        (ISL, IIL, FDL),
        (
            ("Ba lớp contract", "Object store quản lý immutable-like objects, keys, versions/listing và request semantics. File format như Parquet định nghĩa bytes, schema/metadata trong một file và cách reader tìm column chunks/pages. Table format định nghĩa tập files nào tạo thành table state, schema/partition evolution, snapshots và commit protocol. Compute engine thực thi query/write; catalog giữ hoặc điều phối current metadata pointer. Trộn lớp dẫn tới khẳng định sai như Parquet tự cung cấp transaction hoặc object-store directory tự là table."),
            ("Directory listing không phải table state", "Nếu reader liệt kê prefix để suy table, nó có thể thấy files từ lần ghi chưa hoàn tất, files bị bỏ lại, duplicate retries hoặc mixed schema generations. Ngay cả khi object listing hiện có strong consistency, listing vẫn không biết business transaction boundary. Rename-directory pattern có thể đắt, không atomic hoặc không khả dụng theo backend. Table state cần explicit commit marker/pointer và immutable metadata lineage, thay vì lấy sự hiện diện vật lý làm publication decision."),
            ("Failure window", "Một writer thường tạo data files trước khi công bố. Nếu chết giữa chừng, physical objects tồn tại nhưng chưa committed. Directory reader có thể đưa chúng vào scan và tạo partial batch; snapshot reader chỉ dùng files referenced bởi committed metadata. Ngược lại, xóa physical file đang được snapshot reference sẽ phá read/time travel. Lab tiêm failure sau từng boundary, so object count, referenced-file set và table row count. Orphan chỉ được xác định bằng reachability cộng retention, không bằng tuổi đơn giản."),
            ("Cơ chế table format", "Iceberg theo dõi files trong snapshots. Table metadata trỏ snapshots; snapshot trỏ manifest list; manifest list trỏ manifests; manifests ghi data/delete files và metrics. Commit công bố state bằng atomic swap của metadata pointer. Readers giữ snapshot loaded; writers dùng optimistic concurrency và validation. Hidden partitioning tách logical predicate khỏi path convention. Field IDs cho phép rename/reorder an toàn hơn name-based projection. Mỗi guarantee phải gắn mechanism này, không dùng nhãn ACID một mình."),
            ("Điều table format không giải", "Format không tự cấp quyền object store/catalog, không chạy compaction, không bảo đảm mọi engine hỗ trợ feature/version, không xử lý data quality/business correctness và không tạo backup/DR. Atomicity thường ở table boundary; multi-table transaction tùy catalog/engine. Snapshot retention và orphan cleanup có thể xóa khả năng time travel nếu cấu hình sai. Encryption, PII deletion, cost, lock/catalog availability và writer bugs vẫn là trách nhiệm platform/operations."),
            ("Bài phân loại và mô tả guarantee", "Phân mười thành phần vào storage, file format, table format và ghi thêm engine/catalog khi cần. Dựng writer tạo files rồi dừng trước commit; đối chiếu prefix-based read với snapshot read bằng exact file set và row hash. Mô tả guarantee theo subject, mechanism, boundary và failure behavior: ai công bố, pointer nào đổi, reader thấy snapshot nào, retry/conflict ra sao. Kết luận chỉ áp dụng cho implementation/version đã chạy; chưa chạy lab thì ghi protocol."),
        ),
        tuple(f"Layer-boundary probe {i}: component owner, publication rule, failure window và unsupported guarantee phải rõ" for i in range(1, 16)),
    ),
    Lesson(
        225,
        "Lesson_225-the-metadata-tree-snapshot-manifest-list-manifest",
        "Iceberg Metadata Tree and Snapshot Lineage",
        "113-iceberg-metadata-tree-snapshot-lineage.md",
        "wiki.storage.iceberg-metadata-tree-snapshot-lineage",
        "Truy một data file hoặc một dòng từ current metadata pointer về snapshot và manifest như thế nào?",
        (IS, II),
        (ISL, IIL),
        (
            ("Gốc cây metadata", "Catalog/table registration cung cấp current metadata location theo implementation contract. Metadata JSON giữ schema versions, partition specs, sort orders, properties, snapshot log, current snapshot ID và snapshot entries. Thay đổi table state tạo metadata file mới rồi atomically đổi pointer. File cũ vẫn tồn tại để history/recovery theo retention. Đọc một JSON bất kỳ trong directory không chứng minh nó current; phải bắt đầu từ catalog pointer hoặc version-hint contract đã xác minh."),
            ("Snapshot và manifest list", "Snapshot đại diện table state tại một thời điểm và chứa snapshot ID, parent, sequence/timestamp, operation summary cùng manifest-list location. Mỗi snapshot có một manifest list. Manifest-list rows mô tả manifests, content type, partition summaries, file counts và sequence metadata; planner dùng summaries để loại manifests không liên quan. Snapshot không sao chép danh sách mọi data file trực tiếp, giúp metadata slow-changing được reuse giữa commits."),
            ("Manifest entries", "Manifest liệt kê data hoặc delete files cùng status added/existing/deleted, snapshot/sequence lineage, partition tuple, record count, sizes, column metrics và file path. Live table set được diễn giải theo snapshot/manifests và status/sequence rules, không bằng union mù của mọi manifest từng thấy. Metrics hỗ trợ pruning nhưng bounds/null/NaN semantics và field IDs phải đúng. Delete files tham gia scan planning theo content/version rules; bỏ chúng khỏi trace có thể làm đọc thừa rows."),
            ("Từ row về snapshot", "Một row không mang snapshot ID như business column mặc định. Trace bắt đầu từ query snapshot, xác định planned data file, row position/key rồi tìm manifest entry chứa file; manifest-list row chứa manifest; snapshot entry chứa manifest-list. Nếu file được reuse across snapshots, row thuộc state của nhiều snapshots. Câu đúng là row visible in snapshot X qua file F, không phải file/row được sinh duy nhất bởi X nếu lineage không chứng minh."),
            ("Pruning nhiều tầng", "Predicate được bind vào field IDs và transforms. Partition summaries có thể bỏ manifests; manifest file metrics có thể bỏ data files; Parquet row-group/page metadata tiếp tục bỏ units trong file. Hidden partitioning cho planner transform logical predicate mà user không viết path partition. Mỗi tầng có false-positive boundary và counters khác nhau. Báo cáo ghi candidates trước/sau từng tầng; số file cuối cùng mở không tự cho biết tầng nào tạo lợi ích."),
            ("Lab ba commits", "Tạo table, ghi ba commits với stable row IDs và thay đổi phân vùng có kiểm soát. Capture catalog pointer, metadata JSON hashes, current/parent snapshots, manifest-list rows, manifest entries và data-file footers. Chọn một row; trace query snapshot→manifest list→manifest→data file→row key. Chạy partition predicate, ghi manifests/data files bị loại trước mở file. Time travel về từng snapshot và đối soát canonical key set. Không sửa metadata bằng tay; mọi claim lưu exact locator/hash."),
        ),
        tuple(f"Metadata-lineage probe {i}: pointer, snapshot, manifest list, manifest entry và data-file evidence phải nối được" for i in range(1, 16)),
    ),
)

QUERIES = {
    221: ["Parquet row group column chunk page khác nhau thế nào?", "Footer Parquet cho biết gì?", "Chọn row-group size bằng số đo nào?"],
    222: ["Projection pushdown khác filter pruning thế nào?", "Parquet page index gồm gì?", "Làm sao quy công bytes saved cho pushdown?"],
    223: ["Timestamp Parquet lệch giữa engines vì sao?", "Decimal round trip kiểm thế nào?", "Nested null empty missing khác nhau ra sao?"],
    224: ["Object store file format table format khác nhau thế nào?", "Table format giải partial visibility bằng cơ chế gì?", "Iceberg không bảo đảm những gì?"],
    225: ["Iceberg metadata tree gồm những tầng nào?", "Trace row về snapshot thế nào?", "Manifest pruning khác Parquet pruning ra sao?"],
}

NEW = (
    (PF, "1_Nguon/Standards/SRC-APACHE-PARQUET-FILE-FORMAT.md", "https://parquet.apache.org/docs/file-format/", "Apache-2.0-public-documentation"),
    (PI, "1_Nguon/Standards/SRC-APACHE-PARQUET-PAGE-INDEX.md", "https://parquet.apache.org/docs/file-format/pageindex/", "Apache-2.0-public-documentation"),
    (IS, "1_Nguon/Standards/SRC-APACHE-ICEBERG-SPEC.md", "https://iceberg.apache.org/spec/", "Apache-2.0-public-specification"),
)


def folder(lesson: Lesson):
    return MODULE / lesson.directory


def contract(lesson: Lesson):
    note = (folder(lesson) / "note.md").read_text()
    after_path = folder(lesson) / "after-note.md"
    after = after_path.read_text() if after_path.exists() else ""

    def pick(text: str, label: str) -> str:
        match = re.search(rf"(?m)^\*\*{re.escape(label)}\.\*\*\s*(.+)$", text)
        return match.group(1).strip() if match else ""

    old = tuple(pick(note, label) for label in ("Outcome", "Đánh giá", "Lab", "Pitfalls", "Self-study (2,4 giờ)", "Done when"))
    if all(old):
        return old
    tasks = re.findall(r"(?m)^\*\*Nhiệm vụ\.\*\*\s*(.+)$", after)
    return (
        pick(note, "Năng lực cần chứng minh"), pick(after, "Cách đánh giá"),
        tasks[0].strip() if tasks else "", pick(after, "Lỗi cần chủ động loại trừ"),
        tasks[1].strip() if len(tasks) > 1 else "", pick(note, "Điều kiện hoàn thành"),
    )


def front(lesson: Lesson) -> str:
    sources = "\n".join(f"  - {source}" for source in lesson.sources)
    return f"""---
note_id: {lesson.note_id}
note_type: concept-deep-dive
status: review
language: vi
created: 2026-10-02
last_verified: 2026-10-02
editorial_pass: humanized-v1
primary_question: {lesson.question}
source_ids:
{sources}
aliases: [{lesson.title}]
tags: [wiki/storage, parquet, iceberg, interoperability]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/{lesson.filename}
---
"""


def deep(lesson: Lesson) -> str:
    parts = [front(lesson), f"# {lesson.title}\n\n> [!abstract] Câu hỏi trung tâm\n> {lesson.question}\n"]
    for index, (heading, body) in enumerate(lesson.core, 1):
        parts.append(f"\n## {index}. {heading}\n\n{body}\n")
    parts.append("\n## 7. Ma trận kiểm chứng từng mệnh đề\n\nMỗi claim phải chỉ rõ metadata scope, writer/reader version, exact fixture, counterexample và oracle. File parse được, plan có predicate hoặc metadata tồn tại chưa đủ để kết luận physical I/O hay semantic result đúng.\n")
    for index, probe in enumerate(lesson.probes, 1):
        parts.append(f"""
### 7.{index}. {probe}

**Mệnh đề cần kiểm.** {probe}.

**Thiết kế phép thử.** Khóa schema, dataset hash, writer/reader/engine versions, storage backend, cache state và configuration. Tạo positive fixture, boundary fixture và negative/counterexample; thay đổi đúng một biến. Lưu footer hoặc metadata-tree locator, query plan, scan counters, requested/transferred bytes nếu có, typed result hash, logs và run ID. Khi công cụ không quan sát được một tầng, ghi `unknown` thay vì suy từ latency hoặc output count.

**Điều kiện chấp nhận.** Canonical result phải khớp trước khi so hiệu năng. Observation phải lặp lại trên số run đã định, chỉ ra đơn vị bị loại và cơ chế chịu trách nhiệm. Báo riêng source fact, phần tổng hợp của giáo trình và giả định theo implementation. Chưa chạy lab thì mục này là protocol, chưa phải kết quả thực nghiệm.
""")
    references = "\n".join(f"{index}. [[{source}]]" for index, source in enumerate(lesson.source_links, 1))
    coverage = "\n".join(f"| [[{source}]] | Format/table contract, implementation boundary hoặc workload context | Đã đọc locator; không suy ngoài phạm vi |" for source in lesson.source_links)
    parts.append(f"""
## 8. Quy trình phản biện

1. Xác định tầng đang nói: object store, file, table metadata, catalog hay engine.
2. Viết identity và publication boundary trước khi bàn hiệu năng.
3. Tách metadata presence, planner intent, executed pruning và physical I/O.
4. Kiểm semantic result bằng typed oracle trước benchmark.
5. Pin version, configuration, cache state và metric definition.
6. Ghi counterexample, limitation và reversal condition cho recommendation.

## 9. Câu hỏi tự kiểm tra

1. Đơn vị đang xét là file, row group, column chunk, page, manifest hay snapshot?
2. Metadata nào authoritative và lấy từ locator nào?
3. Reader có dùng metadata hay chỉ có khả năng dùng?
4. Parse/decode thành công có che semantic mismatch không?
5. Failure ở trước hay sau publication boundary?
6. Bằng chứng nào còn là protocol chưa chạy?

## 10. Giới hạn và điều chưa cho phép kết luận

- Chưa chạy Parquet footer/page-index lab hoặc Iceberg metadata trace trên engine/catalog thật.
- Đặc tả được kiểm ngày 2026-10-02; implementation behavior phải pin version.
- Matrices và lab protocols là synthesis của giáo trình, không gán nguyên văn cho một nguồn.
- Note giữ trạng thái `review` tới khi chủ dự án duyệt.

## Reference

{references}

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
{coverage}

## Key takeaways

- Mọi claim phải đúng tầng và đúng granularity.
- Metadata hiện diện, planner intent, executed pruning và physical I/O là bốn bằng chứng khác nhau.
- Semantic oracle được kiểm trước performance attribution.
- Chưa chạy lab thì note cung cấp giáo trình và protocol, chưa phải certification cho production.
""")
    return "".join(parts)


def curriculum(lesson: Lesson, knowledge: str):
    outcome, assessment, lab, pitfalls, self_study, done = contract(lesson)
    heading = f"# Phase 6: Analytical Storage and Query Engines\n# Module 15: File, Serialization and Open Table Formats\n# Lesson {lesson.number}: {lesson.title}"
    body = re.sub(r"^---\n.*?\n---\n", "", knowledge, flags=re.S)
    body = re.sub(r"^# .+\n+", "", body, count=1)
    note = f"{heading}\n\n## Mục tiêu bài học\n\n**Năng lực cần chứng minh.** {outcome}\n\n**Điều kiện hoàn thành.** {done}\n\n{body}"
    after = f"""{heading}

## Thực hành

**Nhiệm vụ.** {lab}

Chỉ dùng fixture tổng hợp và môi trường cô lập. Lưu input/schema hashes, versions, commands, metadata, plans, counters, outputs, logs và limitations.

## Kiểm tra cuối bài

1. Nêu identity và granularity trung tâm.
2. Đưa một counterexample làm metadata/plan bị hiểu quá mức.
3. Phân biệt semantic correctness với performance evidence.
4. Nêu một reversal condition cho thiết kế.

## Tiêu chí hoàn thành

**Cách đánh giá.** {assessment}

**Điều kiện đạt.** {done}

## Bài làm sau buổi học

**Nhiệm vụ.** {self_study}

**Lỗi cần chủ động loại trừ.** {pitfalls}

## Reference

- Knowledge note: `{(PACK / lesson.filename).relative_to(ROOT)}`
- Nội dung học thuật: `note.md` cùng thư mục.
"""
    return note, after


def manifest(check: bool = False):
    path = ROOT / "Docs/Second-Brain/second-brain-manifest.json"
    data = json.loads(path.read_text())
    source_ids = {source[0] for source in NEW}
    data["source_registry"] = [row for row in data["source_registry"] if row.get("source_id") not in source_ids]
    data["source_registry"].extend({"source_id": sid, "record_path": record, "canonical_url": url, "captured": "2026-10-02", "rights": rights} for sid, record, url, rights in NEW)
    note_ids = {lesson.note_id for lesson in LESSONS}
    data["note_registry"] = [row for row in data["note_registry"] if row.get("note_id") not in note_ids]
    data["retrieval_test_set"] = [row for row in data["retrieval_test_set"] if row.get("expected_note_id") not in note_ids]
    for lesson in LESSONS:
        data["note_registry"].append({"note_id": lesson.note_id, "path": f"2_Wiki/Database-Systems/{lesson.title}.md", "status": "review", "source_ids": list(lesson.sources), "last_verified": "2026-10-02"})
        data["retrieval_test_set"].extend({"query": query, "expected_note_id": lesson.note_id} for query in QUERIES[lesson.number])
    data["version"] = "1.0.44"
    data["updated_at"] = "2026-10-02T23:59:00+07:00"
    data["layers"]["1_Nguon"]["source_count"] = len(data["source_registry"])
    data["layers"]["2_Wiki"]["note_count"] = len(data["note_registry"])
    expected = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    if check:
        return [] if path.read_text() == expected else [str(path.relative_to(ROOT))]
    path.write_text(expected)
    return []


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    stale = []
    for lesson in LESSONS:
        knowledge = normalize_markdown(deep(lesson))
        note, after = curriculum(lesson, knowledge)
        for path, content in ((PACK / lesson.filename, knowledge), (WIKI / f"{lesson.title}.md", knowledge), (folder(lesson) / "note.md", note), (folder(lesson) / "after-note.md", after)):
            if args.check:
                if not path.exists() or path.read_text() != content:
                    stale.append(str(path.relative_to(ROOT)))
            else:
                path.write_text(content)
    stale += manifest(args.check)
    if stale:
        print("STALE\n" + "\n".join(stale))
        return 1
    print(("checked" if args.check else "written") + f"={len(LESSONS) * 4} stale=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
