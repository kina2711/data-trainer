#!/usr/bin/env python3
"""Build source-grounded L201-L205 capstone, gate and OLAP notes."""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path

from format_knowledge_notes import normalize_markdown

ROOT = Path(__file__).resolve().parents[3]
M13 = ROOT / "Material/DE/Curriculum/Phase_05-modeling-semantics-and-analytical-product/Module_13-analytical-data-product-and-self-service"
M14 = ROOT / "Material/DE/Curriculum/Phase_06-analytical-storage-and-query-engines/Module_14-olap-internals-and-analytical-engines"
PACK = ROOT / "Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01"
WIKI = ROOT / "Docs/Second-Brain/2_Wiki/Database-Systems"


@dataclass(frozen=True)
class Lesson:
    number: int
    directory: str
    title: str
    filename: str
    note_id: str
    question: str
    sources: tuple[str, ...]
    source_links: tuple[str, ...]
    core: tuple[tuple[str, str], ...]
    probes: tuple[str, ...]


FD = "src.book.reis-housley-fundamentals-data-engineering"
DB = "src.web.dbt-semantic-models"
UB = "src.web.govuk-usability-benchmarking"
OW = "src.web.owasp-authorization-cheat-sheet"
FA = "src.web.finops-allocation"
KI = "src.book.kimball-ross-data-warehouse-toolkit.3e"
DD = "src.book.kleppmann-ddia.1e"
SI = "src.book.silberschatz-database-system-concepts.7e"
CS = "src.paper.cstore-column-oriented-dbms"
DP = "src.web.duckdb-parquet-pushdown"
DS = "src.web.duckdb-storage-compression"
AP = "src.web.apache-parquet-encodings"

FDL = "SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING"
DBL = "SRC-DBT-SEMANTIC-MODELS"
UBL = "SRC-GOVUK-USABILITY-BENCHMARKING"
OWL = "SRC-OWASP-AUTHORIZATION-CHEAT-SHEET"
FAL = "SRC-FINOPS-ALLOCATION"
KIL = "SRC-KIMBALL-ROSS-DW-TOOLKIT-3E"
DDL = "SRC-KLEPPMANN-DDIA-1E"
SIL = "SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E"
CSL = "SRC-CSTORE-COLUMN-ORIENTED-DBMS"
DPL = "SRC-DUCKDB-PARQUET-PUSHDOWN"
DSL = "SRC-DUCKDB-STORAGE-AND-COMPRESSION"
APL = "SRC-APACHE-PARQUET-ENCODINGS"


LESSONS = (
    Lesson(
        201,
        "Lesson_201-capstone-a-governed-customer-health-data-product",
        "Capstone - A Governed Customer Health Data Product",
        "89-capstone-governed-customer-health-data-product.md",
        "wiki.data-product.customer-health-capstone",
        "Một customer-health data product cần những artifact, phép thử và failure gates nào để chứng minh decision traceability, semantic correctness, self-service, access control và lifecycle readiness?",
        (FD, DB, UB, OW, FA),
        (FDL, DBL, UBL, OWL, FAL),
        (
            ("Bài toán và ranh giới của sản phẩm", "Capstone bắt đầu từ một quyết định có thật trong tình huống giả lập: đội Customer Success chọn tài khoản cần can thiệp trong tuần, không phải từ mong muốn tạo dashboard sức khỏe khách hàng. Product boundary ghi population là tài khoản B2B đang hoạt động, observation cutoff, excluded segments, data latency và action branches. `customer_health_score` chỉ là một tín hiệu tổng hợp; người làm phải công bố components, trọng số, missing-data behavior và nơi human review có quyền đảo kết quả. Không dùng score cho từ chối dịch vụ, định giá hoặc quyết định pháp lý nếu chưa có approval và fairness analysis tương ứng."),
            ("Tám hạng mục là một chuỗi bằng chứng", "Hạng mục 1 là decision statement bốn phần và metric tree có owner ở từng lá. Hạng mục 2 là traceability matrix năm mắt từ decision đến question, concept, field/metric và test/evidence. Hạng mục 3 là contract năm phần cho product và contract sáu phần cho metric trọng yếu. Hạng mục 4 là public interface tối thiểu, gồm grain, keys, fields, time/freshness, examples và compatibility. Hạng mục 5 là documentation hierarchy với interpretation limits. Hạng mục 6 là access policy parity trên BI, SQL, API. Hạng mục 7 là hai vòng task-based usability. Hạng mục 8 là cost-to-serve cùng keep/optimize/merge/retire analysis. Thiếu một mắt xích làm bằng chứng downstream mất căn cứ."),
            ("Mô hình và ngữ nghĩa customer health", "Chốt grain trước columns: một row cho account tại một snapshot cutoff hay một account-day. Events như ticket, usage và invoice phải aggregate về grain đó bằng window công bố; joins cần multiplicity proof để không nhân đôi. Metric contract nêu population, expression, time basis, exclusions, null/late-data behavior và owner. Health score version là public semantic version, không sửa đè trọng số. Ground truth không được giả định: churn/renewal là lagging outcome và chịu can thiệp; capstone đánh giá correctness của computation và use boundary, không tuyên bố predictive validity khi chưa có study."),
            ("Kiểm soát truy cập và dữ liệu thử", "Policy matrix ghi persona, resource, action, condition và expected decision. Customer Success xem account trong region được giao; analyst có aggregate access; service principal chỉ chạy approved export. Chạy positive và negative cases ở BI, SQL, API, gồm expired role, cross-region row, restricted field và cached response. Fixture dùng synthetic identifiers và giả lập distribution; masked production copy không tự trở thành an toàn. Export tạo bản sao mới nên cần retention, owner và egress rule. Access log phải phân biệt denied, empty authorized result và system error."),
            ("Hai vòng usability có protocol cố định", "Tác vụ đại diện gồm tìm đúng product, xác định account cần review, giải thích score components, nhận ra stale cutoff và từ chối một kết luận ngoài phạm vi. Ghi completion correctness, time, abandonment, assistance và confident-wrong outcome. Vòng hai sửa information architecture hoặc interface từ findings vòng một rồi chạy protocol tương đương. Điều kiện roadmap 'cải thiện ít nhất ba số' là gate học tập; với mẫu nhỏ, chênh lệch không chứng minh cải thiện population hay causal effect. Correctness và safety là guardrail: thời gian giảm nhưng hiểu sai tăng là regression."),
            ("Chi phí và vòng đời", "Cost table tách build/refresh compute, storage, serving và labor/operations; direct, shared và unallocated phải reconcile trong tolerance. Unit cost dùng active decision hoặc reviewed account có định nghĩa, không dùng access grants. Retirement analysis kiểm long-cadence consumers, scheduled accounts, exports và compliance retention. Product đi qua proposed, build, certified, operate, deprecated, removed bằng evidence gates. Capstone chỉ tạo hồ sơ đủ để review trong môi trường học; không tự cấp chứng nhận production."),
            ("Bốn automatic-fail gates", "Gate 1: metric không trace được về decision và action branch. Gate 2: không có executed usability evidence, chỉ có kế hoạch hoặc ảnh giao diện. Gate 3: thiếu interpretation limits cụ thể, làm consumer không biết kết luận bị cấm. Gate 4: dùng vanity signal như dashboard count, access count hoặc page views làm bằng chứng adoption/self-service. Mỗi gate ghi exact artifact, invariant bị vi phạm và remediation; presentation đẹp không bù được. Reviewer còn kiểm independent reconciliation, negative access test và raw evidence, vì tám hạng mục có thể đủ tên nhưng rỗng nội dung."),
        ),
        (
            "decision statement có decider cadence và action branches",
            "metric tree có owner ở mọi lá",
            "traceability matrix nối decision đến test evidence",
            "grain của customer health snapshot được khóa trước join",
            "score version không bị sửa đè",
            "predictive validity không được suy từ computation correctness",
            "public interface nêu interpretation limits",
            "BI SQL API cùng policy intent qua negative tests",
            "synthetic fixture không chứa production identifier",
            "usability task có correct answer và confident-wrong outcome",
            "ba số cải thiện trong mẫu nhỏ không chứng minh causal effect",
            "cost table reconcile direct shared unallocated",
            "retirement inventory tìm long-cadence consumers",
            "automatic-fail gate không được presentation miễn trừ",
            "capstone review không phải production certification",
        ),
    ),
    Lesson(
        202,
        "Lesson_202-gate-5-defend-a-metric-definition-and-prove-self-service",
        "Gate 5 - Defend a Metric Definition and Prove Self-Service",
        "90-gate-5-metric-definition-self-service.md",
        "wiki.data-product.gate-5-metric-self-service",
        "Cổng Phase 5 phải tổ chức đề, oracle, đối soát, chấm điểm và automatic-fail như thế nào để đo năng lực bảo vệ metric thay vì khả năng trình diễn?",
        (KI, DB, UB),
        (KIL, DBL, UBL),
        (
            ("Cổng đo năng lực tích hợp", "Gate 5 không dạy kiến thức mới. Nó kiểm chuỗi năng lực từ M11 đến M13: grain và keys; dimensional model và time behavior; metric contract; join/fanout proof; compatibility; documentation và task-based self-service. Người học nhận một case, atomic tables, edge-case fixture và consumer task. Output là hồ sơ có thể đối soát, không phải slide. Hội đồng đánh giá exact version của definitions, SQL, fixture và usability record; mọi sửa đổi sau giờ làm bài được đánh dấu riêng."),
            ("Phần A: grain và phép đếm", "Với mỗi table, thí sinh viết một câu grain có entity, event/snapshot và time basis; chỉ ra candidate key hoặc uniqueness expectation. Phép đếm gồm row count, distinct business key, duplicate groups, null key và unmatched relationships. Grain statement không được mô tả column list. Một bảng account-month và account-event có thể cùng chứa account_id nhưng không cùng grain. Điểm chỉ được cấp khi statement khớp observations trên fixture; nếu data vi phạm, thí sinh phải phân biệt intended contract với observed defect."),
            ("Phần B: hợp đồng và oracle độc lập", "Ba metrics cần contract sáu phần: population, expression, time, grain/aggregation, exclusions/edge behavior và owner/version. Hội đồng viết reconciliation query từ contract và atomic sources, không đọc implementation query trước. So numerator, denominator, final value và included key set ở ba aggregation levels. Tolerance chỉ dùng khi data type/rounding contract cho phép; exact integer counts không được che lệch bằng tolerance. Mismatch tạo diff rows để chẩn đoán, không chỉ một boolean fail."),
            ("Phần C và D: fanout cùng compatibility", "Fanout proof theo bốn bước: chốt base grain, phân tích join multiplicity, so row/distinct-key/control totals trước-sau, rồi sửa bằng pre-aggregation, dedup contract hoặc bridge weighting. Một chasm trap được cài sẵn để phát hiện việc join hai fact streams qua dimensions rồi aggregate. Compatibility matrix là artifact cưỡng chế được: metric × dimension/path, allow/deny/conditional, reason code và test query. Declared compatibility mà compiler không enforce vẫn cần test; compiler denial sai cũng là defect."),
            ("Phần E: tự phục vụ bằng task evidence", "Người thứ hai thực hiện tác vụ từ discovery tới kết quả và explain-back mà không nhận lời giải miệng. Ghi task success đúng, time, abandonment/assistance và confidence-versus-correctness; access grant, dashboard count hoặc click không thay thế. Protocol nêu participant profile, starting point, product version và allowed help. Một người dùng được hệ thống nhưng hiểu sai grain là failure. Dữ liệu cá nhân của participant chỉ thu khi có consent và retention rule; trong lớp ưu tiên observer sheet không chứa thông tin thừa."),
            ("Phần F và phiên chất vấn", "Reviewer chọn ngẫu nhiên một metric và yêu cầu truy ngược về decision, action branch, concept, field, test và consumer limitation. Tiếp đó thay một constraint: cutoff đổi, late event xuất hiện, dimension effective time đổi hoặc population loại một segment. Thí sinh phải chỉ ra artifacts/tests bị ảnh hưởng trước khi sửa SQL. Chất vấn không chấm sự tự tin; điểm dựa trên causal chain, artifact locator và khả năng nói 'chưa đủ bằng chứng'. Reviewer không tiết lộ oracle query cho tới khi bản nộp đã được fingerprint."),
            ("Rubric và automatic zero", "Tổng 100 điểm: A20, B25, C20, D15, E15, F5; đạt tổng ít nhất 70, đồng thời B và C mỗi phần ít nhất 60%. Một metric không khớp oracle làm phần B của metric đó bằng zero, không kéo toàn bài về zero nếu rubric không nói vậy. Silent double count hoặc thiếu fanout proof bị xử lý trong C. Vanity evidence làm E bằng zero. Rubric cần examples cho full/partial/no credit, two-reviewer calibration và appeal bằng artifact, tránh chấm theo phong cách trình bày."),
        ),
        (
            "gate không đưa nội dung mới",
            "grain statement có entity event snapshot và time basis",
            "observed defect khác intended contract",
            "oracle được viết độc lập từ contract",
            "reconciliation so included key set không chỉ final scalar",
            "tolerance chỉ dùng khi contract cho phép",
            "fanout proof có before after counts",
            "chasm trap dùng hai fact streams",
            "compatibility matrix có reason code và executable test",
            "compiler green không thay reconciliation",
            "self-service task cần explain-back correctness",
            "access count và dashboard count không chứng minh self-service",
            "changed constraint test đánh giá impact analysis",
            "rubric chấm evidence không chấm sự tự tin",
            "automatic zero áp đúng phần đã công bố",
        ),
    ),
    Lesson(
        203,
        "Lesson_203-oltp-against-olap-the-workload-is-the-difference",
        "OLTP and OLAP - Workload Before Product Name",
        "91-oltp-olap-workload-before-product-name.md",
        "wiki.olap.oltp-olap-workload-shape",
        "Phân loại OLTP, OLAP và vùng lai bằng workload shape như thế nào, rồi suy ra yêu cầu storage, execution và isolation mà không dựa vào nhãn sản phẩm?",
        (DD, SI, CS),
        (DDL, SIL, CSL),
        (
            ("Workload là vector, không phải nhãn", "Ghi ít nhất năm chiều: rows touched/query, columns touched/query, read/write mix và mutation shape, latency/throughput target, concurrent sessions. Bổ sung history horizon, query predictability, consistency/freshness và burst pattern khi chúng đổi lựa chọn. OLTP điển hình point/range nhỏ, cập nhật từ user input, tail latency thấp và concurrency cao. OLAP điển hình quét/aggregate nhiều rows, projection hẹp, bulk/stream ingest và latency tính bằng giây. Đây là profiles, không phải luật: workload cụ thể có thể nằm giữa hoặc có nhiều classes đồng thời."),
            ("Từ vector tới bottleneck", "Point lookup phụ thuộc index traversal, random access, latch/lock/MVCC và log durability; scan lớn phụ thuộc bytes read, sequential bandwidth, decompression, memory bandwidth, CPU cache và parallel aggregation. Rows và columns phải quy về byte/operation estimates: mười columns kiểu rộng có thể lớn hơn năm mươi boolean columns. Concurrency biến một query nhanh thành workload quá tải qua queueing. p50 không thay p95/p99; average bytes không cho thấy spill hoặc skew. Phân loại tốt dự đoán resource saturation, không chỉ gọi tên OLTP/OLAP."),
            ("Hệ quả kiến trúc", "Workload point-update thường ưu tiên row locality, indexes, WAL, fine-grained concurrency và bounded transactions. Workload scan ưu tiên column projection, encoding/compression, vectorized operators, zone/partition pruning và batch writes. C-Store trình bày một thiết kế read-optimized với projections, compressed columns và tách write/read structures; đó là một kiến trúc cụ thể, không phải định nghĩa OLAP. SQL interface giống nhau không làm storage path giống nhau. Một engine có thể có row và column representations cho classes khác nhau."),
            ("Tách tải và tính nhất quán", "Chạy analytic query trên primary có thể tranh CPU, memory, buffer cache, I/O và locks với transactions. Read replica tách một phần compute nhưng không tự xóa tác động: WAL generation/retention, replay lag, network, storage, failover readiness và long snapshots vẫn cần đo. Warehouse/lakehouse thêm ingestion lag và reconciliation boundary. Quyết định tách hệ ghi freshness tolerance, source impact, failure isolation, data contract và cost; không mặc định copy là miễn phí hoặc luôn cần."),
            ("HTAP và vùng lai", "Hybrid transactional/analytical processing có thể dùng dual engines, column replicas, in-memory structures hoặc workload isolation. Hệ lai giảm movement/freshness gap trong một số cases nhưng vẫn có resource governance, update propagation, consistency và cost trade-offs. Một operational dashboard quét vài triệu rows mỗi phút có thể là analytical workload dù nằm trong ứng dụng. Một lookup trong warehouse vẫn là point query. Phân loại theo từng query class và service-level objective, không gán toàn database một nhãn duy nhất."),
            ("Ba dấu hiệu đặt nhầm", "Dấu hiệu 1: query plan/read metrics cho thấy scan lớn trên hệ có tail-latency transaction đang tăng. Dấu hiệu 2: hàng nghìn point updates/upserts nhỏ vào cấu trúc tối ưu batch tạo write amplification/merge pressure và freshness queue. Dấu hiệu 3: một hệ phải đồng thời giữ p99 mili giây và phục vụ unbounded ad-hoc scans nhưng không có admission control/workload isolation. Triệu chứng chưa đủ kết luận; cần correlate query class với resource, lag, latency và business deadline."),
            ("Bài phân loại có đối chứng", "Sáu cases gồm checkout write, account lookup, daily revenue scan, customer-360 interactive query, near-real-time anomaly aggregate và bulk correction. Mỗi case chấm năm chiều bằng range có unit, chỉ ra unknowns, chọn architecture và reversal conditions. Hai cases ranh giới phải có điều kiện đẩy sang mỗi phía. Benchmark dùng cùng logical dataset/query/answer, ghi engine/version, indexes/layout, cache state, concurrency và bytes read. Kết quả chỉ áp cho cấu hình đó; không biến một lần đo thành tuyên bố engine phổ quát."),
        ),
        (
            "OLTP OLAP là workload profiles không phải product labels",
            "rows touched cần đổi thành bytes và operations",
            "column width làm số cột không đủ dự đoán bytes",
            "tail latency và concurrency thuộc workload contract",
            "point lookup và scan lớn có bottleneck khác nhau",
            "SQL interface chung không chứng minh storage path chung",
            "read replica chỉ tách một phần resource contention",
            "replica lag và WAL retention vẫn là operational cost",
            "warehouse separation thêm freshness boundary",
            "HTAP không xóa isolation và propagation trade-offs",
            "operational dashboard có thể mang analytical workload",
            "point query trong warehouse không biến thành OLTP system",
            "misplacement cần correlate query class với saturation",
            "benchmark phải khóa cache concurrency và physical design",
            "reversal conditions quan trọng hơn tên công nghệ",
        ),
    ),
    Lesson(
        204,
        "Lesson_204-row-and-column-layout",
        "Row and Column Layout - Isolating Physical Layout",
        "92-row-column-layout-isolating-physical-layout.md",
        "wiki.olap.row-column-layout-isolation",
        "Thiết kế phép đo nào cô lập phần đóng góp của row/column layout khỏi compression, pruning, cache, metadata và khác biệt engine?",
        (DD, SI, CS, DP),
        (DDL, SIL, CSL, DPL),
        (
            ("Logical table và physical layout", "Row layout đặt fields của một tuple gần nhau trong page/record, thuận lợi khi lấy hoặc sửa phần lớn fields của ít rows. Column layout đặt values cùng column thành contiguous column chunks/segments trong row groups, thuận lợi cho projection hẹp trên nhiều rows. Triển khai hiện đại không nhất thiết tạo một OS file cho mỗi column; Parquet có row groups, column chunks và pages trong file. Row identity được giữ qua position/definition levels và metadata. Vì vậy mô hình 'mỗi cột một tệp' chỉ là hình minh họa."),
            ("Projection saving không bằng tỷ lệ cột", "Bytes cần đọc phụ thuộc physical width, variable-length offsets, null/definition metadata, dictionary, page/header/footer, row-group boundaries, prefetch và filesystem/object-store ranges. Chọn 3/100 columns không đảm bảo đọc 3% file. Nếu ba columns chiếm 40% encoded bytes, lower bound đã khác. Engine có thể đọc metadata cho mọi query và fetch page lớn hơn requested slice. Phép đo phải có expected bytes từ metadata và observed bytes theo một định nghĩa rõ, rồi giải thích residual."),
            ("Cô lập biến layout", "Dùng cùng logical generator, row count, data values, column types/order và query semantics. Tắt compression hoặc dùng uncompressed format ở cả hai; tắt/neutralize filter pruning bằng full-row predicate hoặc không predicate; không dùng index/materialized view. Chạy cold-cache và warm-cache rounds riêng, cố định threads/memory và randomized query order. So within one engine/reader nếu có thể; nếu dùng hai engines, kết luận là whole-stack result chứ không riêng layout. Lưu file sizes, explain plan, projected columns và scan bytes."),
            ("Bốn projection widths", "Query 1, 3, 10 và 100 columns trên bảng 100 columns nhưng chọn columns có encoded width đã biết. Tạo hai series: contiguous narrow columns và mixed-width columns để chứng minh column count không đủ. Row layout kỳ vọng read bytes gần phẳng khi scan tất cả rows vì records chứa fields đi kèm, nhưng buffer/page behavior vẫn gây lệch. Column layout kỳ vọng tăng theo tổng physical bytes của selected column chunks cộng fixed overhead; không ép tuyến tính tuyệt đối theo số cột."),
            ("Update cost cần mô hình đúng", "Khẳng định 'update một row phải chạm mọi tệp cột' quá rộng. Engine có thể dùng delta store, delete bitmap, MVCC update segments, append-new-version hoặc rewrite column pages/row groups; update một field không nhất thiết rewrite mọi column file ngay. Chi phí có thể xuất hiện trễ ở merge/compaction và read amplification. Lab phải đo foreground latency, bytes written/WAL, storage delta và background merge over a defined window. So final correctness và space reclamation, không chỉ statement latency."),
            ("Lợi ích ngoài I/O", "Values cùng type/pattern cải thiện encoding; compact columns đưa nhiều values vào cache và hỗ trợ vectorized loops/SIMD. Nhưng projection pushdown, compression và vectorization là mechanisms tách biệt dù thường đi cùng column stores. Bài này giữ compression off để đo layout; vectorized execution có thể còn khác giữa readers và phải ghi như confounder. Reconstruct full rows từ nhiều columns có gather/materialization cost; `SELECT *` hoặc point fetch có thể làm row layout cạnh tranh tốt hơn."),
            ("Đọc kết quả và giữ giới hạn", "Bảng kết quả có logical rows, projected logical bytes, file bytes, storage bytes fetched, engine scan bytes, elapsed CPU/wall time, cache state và repetitions. Median cùng dispersion thay một run. Nếu bytes không như dự đoán, kiểm projection pushdown trong plan, page/range granularity, cache và instrumentation trước khi kết luận. Done khi người học quy phần tiết kiệm cho layout với residual được giải thích, đồng thời tách rõ compression/pruning. Không kết luận mọi column store nhanh hơn mọi row store."),
        ),
        (
            "column layout thường dùng row groups column chunks và pages",
            "ba trên một trăm cột không đồng nghĩa ba phần trăm bytes",
            "physical width và metadata thuộc byte model",
            "projection pushdown khác filter pruning",
            "compression phải tắt khi cô lập layout",
            "cold cache và warm cache là hai experiments",
            "khác engine làm kết quả thành whole stack comparison",
            "query order cần randomized để giảm warmup bias",
            "mixed-width columns phá giả định tuyến tính theo count",
            "row-layout scan bytes chỉ kỳ vọng gần phẳng trong setup",
            "column-layout bytes tăng theo selected chunks cộng overhead",
            "update một row không mặc nhiên rewrite mọi column file",
            "delta store chuyển chi phí sang merge hoặc read path",
            "vectorization là confounder riêng với layout",
            "full-row reconstruction có gather materialization cost",
        ),
    ),
    Lesson(
        205,
        "Lesson_205-encoding-and-compression",
        "Encoding and Compression - Choosing from Data Shape",
        "93-encoding-compression-choosing-data-shape.md",
        "wiki.olap.encoding-compression-data-shape",
        "Chọn encoding và block codec theo distribution, order, range, nulls và execution path như thế nào, rồi chứng minh bằng size, decode throughput và query measurements?",
        (DD, AP, DS, CS),
        (DDL, APL, DSL, CSL),
        (
            ("Encoding và compression là hai lớp", "Encoding biểu diễn values bằng cấu trúc khai thác semantics/pattern: dictionary indices, runs, frame-of-reference/bit packing, deltas hoặc definition/null levels. General block codec như LZ4/Zstd nhận byte stream sau encoding và tìm redundancy rộng hơn. Format có thể xếp hai lớp; metadata phải ghi encoding/codec để reader giải mã. So `PLAIN+Zstd` với `dictionary+Zstd` khác cả encoding; không được gán toàn bộ chênh lệch cho codec. CPU cost gồm encode, decode và khả năng operator làm việc trước/full materialization."),
            ("Dictionary phụ thuộc economics của dictionary", "Dictionary lưu distinct values rồi thay mỗi occurrence bằng index. Nó thường tốt khi distinct set nhỏ so với rows và values đủ rộng, nhưng 'low cardinality' cần định lượng: dictionary bytes, index bit width, page scope, fallback và access pattern. Cột gần unique có dictionary overhead và random lookup/cache cost. Distribution skew có thể giúp dù cardinality tuyệt đối không rất thấp. Benchmark báo distinct count/ratio, value lengths, dictionary size, index width và fallback pages; không chỉ ratio cuối."),
            ("RLE phụ thuộc runs và sort order", "Run-length encoding lưu value hoặc code cùng run length, nên hiệu quả dựa average/percentile run length, không chỉ cardinality. Cùng value frequencies nhưng shuffle ngẫu nhiên phá runs; sort theo column tạo runs dài. Sort toàn row để giữ alignment, không sort từng column độc lập. Primary sort key thường hưởng mạnh nhất; keys sau có runs ngắn dần. Thay sort order còn đổi pruning, ingest/merge cost và queries khác, nên improvement RLE không đủ quyết định sort key."),
            ("Bit packing và delta", "Bit packing cần width đủ cho value range hoặc frame-of-reference residual; một outlier có thể nâng width của block/page. Partition thành miniblocks giúp thích nghi nhưng thêm headers. Delta lưu differences; monotonic timestamp chỉ là case thuận lợi, điều kiện thật là deltas có range nhỏ/predictable. Parquet DELTA_BINARY_PACKED dùng minimum delta và per-miniblock bit widths, khác mô tả đơn giản 'timestamp tăng thì delta tốt'. Signed mapping, first value, padding và exceptions đều có cost. Báo block size và outlier behavior."),
            ("Null representation và semantics", "Null bitmap/definition levels tách presence khỏi payload, nhưng null distribution vẫn ảnh hưởng RLE/bit packing và filters. SQL NULL khác empty string, zero hoặc missing nested field; encoding không được làm mất distinction. Nested Parquet dùng repetition/definition levels, phức tạp hơn một bitmap. Null-heavy column có thể nhỏ nhưng query `IS NULL` vẫn phụ thuộc statistics/operator. Fixture cần all-null, alternating-null, long null runs và sparse non-null cases; verify decoded equality trước performance."),
            ("Decode speed và compute on encoded data", "Giảm bytes có thể tăng speed khi I/O/memory bandwidth là bottleneck, nhưng codec mạnh có thể chuyển bottleneck sang CPU. 'Nén mạnh nhất không nhanh nhất' là khả năng, không phải quy luật. Dictionary comparisons, bitmap operations hoặc RLE aggregates có thể chạy trên encoded representation nếu engine/operator hỗ trợ; không mặc định mọi expression làm vậy. Inspect plan/profile/source documentation hoặc microbenchmark operator-specific. Đo encode time, size, decode throughput, query CPU/wall, bytes read và peak memory."),
            ("Ma trận thí nghiệm", "Tạo ít nhất bốn columns: low-cardinality shuffled strings; same values sorted into runs; narrow-range integers có outliers; monotonic timestamps có jitter. Thêm null patterns. Với mỗi candidate encoding và codec level, xác minh round-trip hash/count/min/max, lấy encoded size, total file/page metadata, encode/decode time và representative query time. Randomize run order, warm-up riêng, lặp nhiều lần. Nếu writer không cho force encoding, dùng format inspection để ghi actual selection hoặc một encoder harness nhỏ; không giả option đã được áp. Chọn per-column configuration theo Pareto frontier và workload constraint."),
        ),
        (
            "encoding khác general block compression",
            "dictionary cần tính dictionary bytes và index width",
            "low cardinality không có một ngưỡng phổ quát",
            "RLE phụ thuộc run length và row sort order",
            "sort mỗi column độc lập làm mất row alignment",
            "bit width phụ thuộc range và outliers trong block",
            "delta hiệu quả khi residual deltas có range nhỏ",
            "Parquet delta dùng blocks miniblocks và minimum delta",
            "null bitmap không được đồng nhất null với zero",
            "nested definition levels phức tạp hơn một null bitmap",
            "codec mạnh nhất không mặc nhiên chậm hay nhanh nhất",
            "compute on encoded data là engine operator specific",
            "round-trip correctness đi trước benchmark",
            "actual writer encoding phải được inspect",
            "lựa chọn cuối dựa Pareto frontier và workload constraints",
        ),
    ),
)


VERIFY = {
    201: "Dựng synthetic customer/account fixture; kiểm tám artifacts, independent metric reconciliation, three-surface negative access, hai vòng task protocol và cost/lifecycle dossier. Gắn mỗi claim với exact artifact/version.",
    202: "Fingerprint submission rồi chạy examiner-owned oracle ở ba grains, fanout/chasm fixture, executable compatibility tests và task-based self-service observation. Áp rubric/automatic-zero đúng phần đã công bố.",
    203: "Chấm workload vector có unit, đo plans/resources trên cùng logical case và thay concurrency, projection width hoặc freshness constraint. Ghi điều kiện làm architecture choice phải đảo.",
    204: "Giữ logical data/query cố định; tắt compression/pruning, tách cold/warm cache, inspect projected columns và đo logical/file/storage/engine bytes. Với update, theo dõi cả foreground lẫn merge window.",
    205: "Tạo distributions có kiểm soát, force hoặc inspect actual encoding, verify round-trip rồi đo size, encode/decode, query CPU/wall và memory. Đổi order, cardinality, range, null pattern và outlier để tìm reversal point.",
}

QUERIES = {
    201: ["Customer health capstone cần tám hạng mục nào?", "Bốn automatic-fail gates của L201 là gì?", "Vì sao hai vòng usability cải thiện ba số chưa chứng minh causal effect?"],
    202: ["Gate 5 đối soát metric độc lập thế nào?", "Phần B và C của Gate 5 có ngưỡng đạt nào?", "Bằng chứng self-service nào làm phần E bằng zero?"],
    203: ["Năm chiều phân loại OLTP và OLAP là gì?", "Vì sao read replica chưa chắc đã tách hoàn toàn tải phân tích?", "HTAP có xóa trade-off workload isolation không?"],
    204: ["Vì sao chọn 3 trên 100 cột không đồng nghĩa đọc 3 phần trăm bytes?", "Cách cô lập row và column layout khỏi compression pruning là gì?", "Update một row trong column store có luôn rewrite mọi column file không?"],
    205: ["Dictionary encoding thắng theo điều kiện nào?", "RLE phụ thuộc sort order như thế nào?", "Phân biệt encoding và block compression trong Parquet ra sao?"],
}

NEW_SOURCES = (
    {"source_id": CS, "record_path": "1_Nguon/Papers/SRC-CSTORE-COLUMN-ORIENTED-DBMS.md", "canonical_url": "https://web.eecs.umich.edu/~mozafari/fall2015/eecs584/papers/c-store.pdf", "captured": "2026-10-01", "rights": "public-research-paper"},
    {"source_id": AP, "record_path": "1_Nguon/Web/SRC-APACHE-PARQUET-ENCODINGS.md", "canonical_url": "https://parquet.apache.org/docs/file-format/data-pages/encodings/", "captured": "2026-10-01", "rights": "Apache-project-public-documentation"},
    {"source_id": DS, "record_path": "1_Nguon/Web/SRC-DUCKDB-STORAGE-AND-COMPRESSION.md", "canonical_url": "https://duckdb.org/docs/stable/internals/storage", "captured": "2026-10-01", "rights": "public-web-documentation"},
    {"source_id": DP, "record_path": "1_Nguon/Web/SRC-DUCKDB-PARQUET-PUSHDOWN.md", "canonical_url": "https://duckdb.org/docs/stable/data/parquet/overview", "captured": "2026-10-01", "rights": "public-web-documentation"},
)


def folder(lesson: Lesson) -> Path:
    return (M13 if lesson.number <= 202 else M14) / lesson.directory


def hierarchy(lesson: Lesson) -> tuple[str, str]:
    if lesson.number <= 202:
        return "Phase 5: Modeling, Semantics and Analytical Product", "Module 13: Analytical Data Product and Self-service"
    return "Phase 6: Analytical Storage and Query Engines", "Module 14: OLAP Internals and Analytical Engines"


def field(text: str, name: str) -> str:
    match = re.search(rf"(?m)^\*\*{re.escape(name)}\.\*\*\s*(.+)$", text)
    if not match:
        raise ValueError(f"missing field {name}")
    return match.group(1).strip()


def section(text: str, heading: str) -> str:
    match = re.search(rf"(?ms)^## {re.escape(heading)}\n\n(.*?)(?=^## |\Z)", text)
    if not match:
        raise ValueError(f"missing section {heading}")
    return match.group(1).strip()


def contract(lesson: Lesson) -> tuple[str, str, str, str, str, str]:
    note = (folder(lesson) / "note.md").read_text()
    after = (folder(lesson) / "after-note.md").read_text()
    if "**Outcome.**" in note:
        return tuple(field(note, key) for key in ("Outcome", "Đánh giá", "Lab", "Pitfalls", "Self-study (2,4 giờ)", "Done when"))
    return (
        field(section(note, "Mục tiêu bài học"), "Năng lực cần chứng minh"),
        field(section(after, "Tiêu chí hoàn thành"), "Cách đánh giá"),
        field(section(after, "Thực hành"), "Nhiệm vụ"),
        field(section(after, "Bài làm sau buổi học"), "Lỗi cần chủ động loại trừ"),
        field(section(after, "Bài làm sau buổi học"), "Nhiệm vụ"),
        field(section(note, "Mục tiêu bài học"), "Điều kiện hoàn thành"),
    )


def frontmatter(lesson: Lesson) -> str:
    sources = "\n".join(f"  - {source}" for source in lesson.sources)
    domain_tags = "data-product, assessment" if lesson.number <= 202 else "olap, storage-engine"
    return f"""---
note_id: {lesson.note_id}
note_type: concept-deep-dive
status: review
language: vi
created: 2026-10-01
last_verified: 2026-10-01
editorial_pass: humanized-v1
primary_question: {lesson.question}
source_ids:
{sources}
aliases: [{lesson.title}]
tags: [wiki/database-systems, {domain_tags}]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/{lesson.filename}
---
"""


def deep_note(lesson: Lesson) -> str:
    parts = [frontmatter(lesson), f"# {lesson.title}\n\n> [!abstract] Câu hỏi trung tâm\n> {lesson.question}\n"]
    for index, (heading, body) in enumerate(lesson.core, 1):
        parts.append(f"\n## {index}. {heading}\n\n{body}\n")
    parts.append("\n## 8. Ma trận kiểm chứng từng mệnh đề\n\nMỗi kết luận cần input, observation và failure signal có thể lưu. Tên sản phẩm, file nhỏ, query nhanh hoặc presentation thuyết phục không tự chứng minh cơ chế hay năng lực.\n")
    for index, probe in enumerate(lesson.probes, 1):
        parts.append(
            f"\n### 8.{index}. {probe}\n\n"
            f"**Mệnh đề cần kiểm.** {probe}.\n\n"
            f"**Cách kiểm.** {VERIFY[lesson.number]} Với mệnh đề này, ghi dataset/contract version, environment, controlled variables, expected observation, failure signal và boundary làm kết luận mất hiệu lực.\n\n"
            "**Bằng chứng đạt.** Lưu fixture hoặc source slice, command/query/protocol, raw output, counters/diff, reviewer và artifact hash. Nếu lab chưa chạy trên môi trường được phép, chỉ ghi protocol và expected result; không viết như kết quả đã quan sát.\n"
        )
    parts.append(
        """
## 9. Quy trình phản biện

1. Chốt decision hoặc workload, grain, version và constraints trước khi chọn implementation.
2. Tách logical semantics, physical mechanism, observed metric và business conclusion.
3. Khóa controlled variables; ghi rõ confounders còn lại và instrumentation boundary.
4. Kiểm correctness trước performance, đồng thời giữ negative và changed-constraint cases.
5. Phân loại source fact, curriculum synthesis, engine-specific behavior và untested hypothesis.
6. Dùng raw artifacts và independent oracle khi kết quả do chính implementation sinh ra.
7. Chưa có execution evidence thì giữ trạng thái `review`.

## 10. Câu hỏi tự kiểm tra

1. Invariant, decision hoặc workload characteristic trung tâm là gì?
2. Biến nào được giữ cố định và biến nào được thay đổi?
3. Counter nào đo đúng mechanism thay vì chỉ đo wall-clock?
4. Một kết quả xanh nhưng sai semantics có thể xuất hiện bằng cách nào?
5. Điều kiện nào làm lựa chọn hiện tại phải đảo?
6. Kết luận nào mới là protocol, chưa phải evidence quan sát được?

## 11. Giới hạn và điều chưa cho phép kết luận

- Chưa chạy capstone với người dùng thật, Gate 5 với hội đồng, benchmark engines hoặc compression matrix; note mô tả protocol và expected evidence.
- Tài liệu web được kiểm ngày 2026-10-01; format, encoding support, storage version và engine behavior có thể đổi.
- Rubric, tám hạng mục capstone và ma trận kiểm chứng là curriculum synthesis; không gán nguyên văn cho một nguồn.
- Kết quả microbenchmark chỉ áp cho dataset, version, configuration, cache và workload đã ghi; không chứng minh ưu thế phổ quát.
- Note giữ trạng thái `review` cho tới khi chủ dự án duyệt semantic meaning.
"""
    )
    references = "\n".join(f"{index}. [[{link}]]" for index, link in enumerate(lesson.source_links, 1))
    coverage = "\n".join(
        f"| [[{link}]] | Khái niệm, mechanism hoặc evidence boundary liên quan | Đã đọc locator được ghi trong source record; không suy ngoài phạm vi |"
        for link in lesson.source_links
    )
    takeaways = {
        201: "Capstone là chuỗi bằng chứng tám hạng mục; đủ file nhưng thiếu traceability, usability, limitation hoặc valid adoption evidence vẫn không đạt.",
        202: "Gate 5 đo bằng oracle độc lập, fanout proof và task correctness; compiler xanh hoặc trình bày tự tin không thay bằng chứng.",
        203: "OLTP và OLAP là workload profiles; architecture phải được suy từ rows, columns, mutations, latency và concurrency có unit.",
        204: "Layout chỉ được quy công khi compression, pruning, cache và engine differences đã được kiểm soát hoặc ghi thành confounders.",
        205: "Encoding chọn theo data shape ở block/page và execution path; block codec là lớp riêng, cần đo size lẫn CPU/query behavior.",
    }
    parts.append(
        f"""
## Reference

{references}

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
{coverage}

## Key takeaways

- {takeaways[lesson.number]}
- Correctness, scope và exact version đi trước performance hoặc approval.
- Một proxy dễ lấy không được dùng thay consumer outcome, physical counter hoặc independent reconciliation.
- Counterexample và changed constraint phải làm kết luận đảo khi assumptions không còn đúng.
- Chưa chạy lab thì artifact là giáo trình đã kiểm cấu trúc, không phải chứng nhận production hay benchmark result.
"""
    )
    return "".join(parts)


def curriculum(lesson: Lesson, knowledge: str) -> tuple[str, str]:
    outcome, assessment, lab, pitfalls, homework, done = contract(lesson)
    phase, module = hierarchy(lesson)
    header = f"# {phase}\n# {module}\n# Lesson {lesson.number}: {lesson.title}"
    body = re.sub(r"^---\n.*?\n---\n", "", knowledge, flags=re.S)
    body = re.sub(r"^# .+\n+", "", body, count=1)
    note = f"{header}\n\n## Mục tiêu bài học\n\n**Năng lực cần chứng minh.** {outcome}\n\n**Điều kiện hoàn thành.** {done}\n\n{body}"
    safety = "Chỉ dùng fixture, file và engine thử nghiệm có version; không dùng dữ liệu cá nhân, mở quyền production hoặc chạy benchmark trên hệ dùng chung. Lưu dataset generator/hash, configuration, commands, raw outputs, cache state, reviewer và limitations."
    questions = "\n".join(
        f"{index}. {question}"
        for index, question in enumerate((
            "Nêu decision, invariant hoặc workload characteristic trung tâm.",
            "Đưa một confounder có thể làm kết luận sai.",
            "Phân biệt expected result với evidence đã quan sát.",
            "Nêu counterexample hoặc changed constraint làm lựa chọn phải đảo.",
        ), 1)
    )
    after = f"{header}\n\n## Thực hành\n\n**Nhiệm vụ.** {lab}\n\n{safety}\n\n## Kiểm tra cuối bài\n\n{questions}\n\n## Tiêu chí hoàn thành\n\n**Cách đánh giá.** {assessment}\n\n**Điều kiện đạt.** {done}\n\n## Bài làm sau buổi học\n\n**Nhiệm vụ.** {homework}\n\n**Lỗi cần chủ động loại trừ.** {pitfalls}\n\n## Reference\n\n- Knowledge note: `{(PACK / lesson.filename).relative_to(ROOT)}`\n- Nội dung học thuật: `note.md` cùng thư mục.\n"
    return note, after


def update_manifest(check: bool = False) -> list[str]:
    path = ROOT / "Docs/Second-Brain/second-brain-manifest.json"
    data = json.loads(path.read_text())
    new_source_ids = {source["source_id"] for source in NEW_SOURCES}
    data["source_registry"] = [source for source in data["source_registry"] if source.get("source_id") not in new_source_ids] + list(NEW_SOURCES)
    note_ids = {lesson.note_id for lesson in LESSONS}
    data["note_registry"] = [note for note in data["note_registry"] if note.get("note_id") not in note_ids]
    data["retrieval_test_set"] = [test for test in data["retrieval_test_set"] if test.get("expected_note_id") not in note_ids]
    for lesson in LESSONS:
        data["note_registry"].append({
            "note_id": lesson.note_id,
            "path": f"2_Wiki/Database-Systems/{lesson.title}.md",
            "status": "review",
            "source_ids": list(lesson.sources),
            "last_verified": "2026-10-01",
        })
        data["retrieval_test_set"].extend({"query": query, "expected_note_id": lesson.note_id} for query in QUERIES[lesson.number])
    data["version"] = "1.0.40"
    data["updated_at"] = "2026-10-01T23:50:00+07:00"
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
    stale: list[str] = []
    for lesson in LESSONS:
        knowledge = normalize_markdown(deep_note(lesson))
        note, after = curriculum(lesson, knowledge)
        targets = (
            (PACK / lesson.filename, knowledge),
            (WIKI / f"{lesson.title}.md", knowledge),
            (folder(lesson) / "note.md", note),
            (folder(lesson) / "after-note.md", after),
        )
        for path, content in targets:
            if args.check:
                if not path.exists() or path.read_text() != content:
                    stale.append(str(path.relative_to(ROOT)))
            else:
                path.write_text(content)
    stale.extend(update_manifest(args.check))
    if stale:
        print("STALE\n" + "\n".join(stale))
        return 1
    print(("checked" if args.check else "written") + f"={len(LESSONS) * 4} stale=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
