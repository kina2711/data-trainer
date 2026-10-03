#!/usr/bin/env python3
"""Build source-grounded L206-L210 pruning, execution and MPP notes."""
from __future__ import annotations

import argparse
import json
import re

import promote_l201_l205_notes as previous
from format_knowledge_notes import normalize_markdown
from promote_l201_l205_notes import Lesson

ROOT = previous.ROOT
BASE = previous.M14
PACK = previous.PACK
WIKI = previous.WIKI

DD = "src.book.kleppmann-ddia.1e"
DP = "src.web.duckdb-parquet-pushdown"
DZ = "src.web.duckdb-zonemaps"
TD = "src.web.trino-dynamic-filtering"
X1 = "src.paper.monetdb-x100-hyper-pipelining"
MA = "src.paper.abadi-materialization-strategies"
LL = "src.web.llvm-auto-vectorization"
IN = "src.web.intel-intrinsics-guide"
CS = "src.paper.cstore-column-oriented-dbms"
PR = "src.paper.presto-sql-on-everything"
TR = "src.web.trino-distributed-plans"

DDL = "SRC-KLEPPMANN-DDIA-1E"
DPL = "SRC-DUCKDB-PARQUET-PUSHDOWN"
DZL = "SRC-DUCKDB-ZONEMAPS"
TDL = "SRC-TRINO-DYNAMIC-FILTERING"
X1L = "SRC-MONETDB-X100-HYPER-PIPELINING"
MAL = "SRC-ABADI-MATERIALIZATION-STRATEGIES"
LLL = "SRC-LLVM-AUTO-VECTORIZATION"
INL = "SRC-INTEL-INTRINSICS-GUIDE"
CSL = "SRC-CSTORE-COLUMN-ORIENTED-DBMS"
PRL = "SRC-PRESTO-SQL-ON-EVERYTHING"
TRL = "SRC-TRINO-DISTRIBUTED-PLANS"


LESSONS = (
    Lesson(
        206,
        "Lesson_206-zone-maps-statistics-and-pruning",
        "Zone Maps Statistics and Pruning",
        "94-zone-maps-statistics-pruning.md",
        "wiki.olap.zone-maps-statistics-pruning",
        "Pruning được chứng minh ở partition, file, row-group, page và runtime như thế nào, đồng thời tránh cắt nhầm dữ liệu vì statistics hoặc comparison semantics không tương thích?",
        (DP, DZ, TD),
        (DPL, DZL, TDL),
        (
            ("Pruning là phép chứng minh không thể khớp", "Metadata cho một unit lưu trữ mô tả miền có thể xuất hiện: partition value, min/max, null count, value count, bloom/page index hoặc statistics khác. Với predicate và semantics đã biết, engine chỉ được bỏ unit khi chứng minh không row nào có thể thỏa. Min/max cho `x = 50` bỏ block `[100,200]` nhưng phải đọc block `[1,100]` dù 50 không tồn tại; false positive làm đọc thừa, false negative làm sai kết quả và không được chấp nhận. 'Không đọc' có thể rẻ nhất cho query chọn lọc, nhưng full scan hoặc uncorrelated filter có pruning bằng zero."),
            ("Năm tầng cần phân biệt", "Partition pruning loại directories/partitions từ transform/value đã công bố. File pruning dùng manifest/file statistics. Row-group/stripe pruning dùng min/max/bloom của nhóm rows; page pruning hẹp hơn khi format và reader hỗ trợ page index. Runtime/dynamic pruning lấy values/range từ build side của join rồi đẩy về split enumeration hoặc file reader. Một plan có filter pushdown không chứng minh mọi tầng đã hoạt động. Báo candidate units, planned units, opened files, read row groups/pages, bytes và rows sau filter ở từng boundary có counter."),
            ("Ordering quyết định độ chồng lấn", "Nếu events được sắp theo event_time, min/max của row groups theo time thường hẹp và ít chồng; time-range query bỏ phần lớn groups. Nếu account_id phân tán ngẫu nhiên, mỗi group có thể chứa gần cả miền account và zonemap kém chọn lọc. Correlation có thể không hoàn hảo nhưng vẫn hữu ích. Row-group size tạo trade-off: group nhỏ cho statistics mịn và parallelism nhiều hơn, đồng thời tăng metadata/header và task overhead; group lớn nén tốt hơn nhưng min/max rộng. Không chọn size chỉ từ một query."),
            ("Predicate blockers không phải danh sách tuyệt đối", "Bọc column trong function, implicit/explicit cast hoặc expression không trực tiếp có thể ngăn rewrite/pushdown, nhưng không phải engine nào cũng thất bại: optimizer có thể constant-fold, invert monotonic function hoặc normalize cast an toàn. `DATE(ts)=d`, `CAST(id AS VARCHAR)='42'` và arithmetic expression phải được xác minh trên đúng engine/version. Sửa bằng range typed đúng hoặc generated/partition field chỉ sau khi kiểm semantics timezone/null. Sargability là phép tương tự hữu ích, nhưng pruning metadata không hoàn toàn giống B-tree index lookup."),
            ("Statistics safety và comparison semantics", "Writer/reader phải thống nhất physical type, logical annotation, ordering, collation, timezone và NaN rules. Truncated string bounds, binary collation, decimal scale hoặc timestamp rebasing có thể làm statistics không usable. An toàn là fail open: đánh dấu unknown và đọc unit, không dùng metadata nghi ngờ để skip. Stale metadata trong mutable systems cần transaction/snapshot consistency. Lab phải có boundary values, null, NaN, unicode/collation, negative numbers và timestamps quanh DST; so pruned result với full-scan oracle."),
            ("Dynamic filtering có chi phí", "Trino tạo dynamic filter từ join build side khi planner, connector và reader hỗ trợ. Small/selective build có thể thu distinct set; vượt threshold có thể chuyển min/max hoặc bỏ collection. Thu thập, phân phối và chờ filter tiêu tốn CPU/time; filter đến trễ thì probe splits đã đọc. `dynamicFilterAssignments` trong plan chỉ chứng minh planner intent. EXPLAIN ANALYZE, QueryInfo và connector counters mới cho biết accepted values, completed filters, splits/row groups skipped và wait time."),
            ("Lab sáu query và hai layouts", "Tạo cùng data/hash ở layout time-sorted và shuffled; ghi row-group size, statistics support và cache state. Sáu queries gồm direct range/equality, function-wrapped, type mismatch, non-monotonic expression và join-derived filter. Dùng full-scan/no-pruning oracle để kiểm result hash. Với mỗi query lưu plan, candidate/read/skipped units, bytes, metadata time và wall/CPU. Tỷ lệ cắt là `1 - read_units/candidate_units`, nhưng cần kèm bytes vì units khác kích thước. Ba sửa đổi đạt khi correctness giữ nguyên và counters chứng minh tăng pruning, không chỉ thời gian giảm."),
        ),
        (
            "pruning chỉ skip khi chứng minh unit không thể match",
            "min max cho phép false positive nhưng không false negative",
            "partition file row-group page runtime là năm tầng khác nhau",
            "filter pushdown annotation không chứng minh physical skip",
            "ordering làm hẹp hoặc rộng min max ranges",
            "row-group size cân granularity compression parallelism metadata",
            "function wrapper có thể hoặc không chặn tùy optimizer",
            "typed range rewrite phải giữ timezone và null semantics",
            "sargability analogy không đồng nhất B-tree với zonemap",
            "statistics không tương thích phải fail open",
            "full-scan oracle phát hiện cắt nhầm",
            "dynamic filter cần planner connector reader cùng hỗ trợ",
            "dynamic filter đến trễ có thể không tiết kiệm scan",
            "pruning ratio cần đi cùng bytes",
            "query nhanh không chứng minh pruning đang xảy ra",
        ),
    ),
    Lesson(
        207,
        "Lesson_207-vectorized-execution-and-late-materialization",
        "Vectorized Execution and Late Materialization",
        "95-vectorized-execution-late-materialization.md",
        "wiki.olap.vectorized-execution-late-materialization",
        "Vector batches, selection vectors, late materialization và encoded execution giảm overhead ở đâu, và query shape nào làm từng cơ chế mất lợi thế?",
        (DD, X1, MA),
        (DDL, X1L, MAL),
        (
            ("Ba execution granularities", "Tuple-at-a-time/Volcano gọi operator qua interface cho từng row, linh hoạt và pipeline tốt nhưng trả chi phí dispatch, function call, type handling và branch mỗi row. Full-column/array-at-a-time giảm dispatch nhưng materialize intermediates lớn, tăng memory traffic và làm mất cache locality. Vectorized execution truyền batch vừa cache qua operator primitives, amortize call overhead nhưng giữ pipeline. X100 dùng mô hình này để phân tích overhead; batch size không phải hằng số một nghìn và optimum phụ thuộc tuple width, operators, cache và machine."),
            ("Data chunk và selection representation", "Một vector/chunk chứa column arrays, validity/null mask và count. Filter có thể trả selection vector chứa row positions thay vì copy payload; downstream operators dereference chỉ rows sống. Dense selection đôi khi quét mask/bitmap tốt hơn index vector; sparse selection tiết kiệm work nhưng gather ngẫu nhiên có thể tốn cache/TLB. Selection composition qua nhiều filters cần giữ row identity và bounds. Null mask là semantics, không chỉ overhead: SQL three-valued logic phải giống scalar oracle ở filter, join và aggregation."),
            ("Late materialization", "Late materialization đọc/filter trên columns cần sớm, giữ positions/selection, rồi lấy projected columns cho rows sống. Nó giảm bytes và tuple construction khi filter chọn ít rows và deferred columns rộng. Giá phải trả gồm position tracking, random gathers, reconstruction, cache misses và complexity qua joins/sorts. Nếu selectivity cao, output cần hầu hết columns, positions mất order/locality hoặc complex nested values phải decode, early materialization có thể thắng. Paper materialization cung cấp taxonomy; lựa chọn phải theo pipeline, không thành khẩu hiệu."),
            ("Encoded execution", "Dictionary equality có thể map constant sang code rồi so integer codes; RLE aggregate có thể nhân value với run length; bitmap AND/OR có thể xử lý compressed representation. Chỉ operators và encoding combinations có implementation tương ứng mới tránh decode. Dictionary của hai chunks có thể khác codebooks; range/order trên dictionary codes chỉ đúng khi dictionary order có contract. Expressions/UDFs thường buộc decode/type conversion. Plan/profile hoặc source documentation phải chứng minh encoded path; file nén nhỏ không tự chứng minh compute-on-encoded-data."),
            ("Pipeline, blocking operators và code generation", "Scan-filter-project có thể fusion/pipeline batches. Sort, hash-build, global aggregation hoặc exchange là blocking/semi-blocking boundaries và có thể materialize/spill. Runtime code generation/JIT là cơ chế khác: fuse expressions và specialize types để giảm virtual dispatch; engine có thể vectorized không JIT, JIT tuple-at-a-time hoặc kết hợp. Compilation latency có thể không đáng cho query ngắn. Lesson giữ four mechanisms riêng: batching, selection, late materialization, encoded execution; codegen chỉ là boundary nhận biết."),
            ("UDF và type-boundary", "Opaque UDF call có thể phá predicate pushdown, operator fusion, auto-vectorization và null propagation; callback per row đưa dispatch trở lại hot loop. Vectorized UDF có batch interface nhưng vẫn tốn serialization/copy hoặc language-runtime boundary. Built-in expression có semantics/implementation engine biết nên tối ưu sâu hơn. So UDF với built-in phải giữ exact semantics, null/error behavior và type; compiler có thể constant-fold một bên. Counter gồm calls, batches, rows/call, CPU cycles, allocations và conversions."),
            ("Bốn reversal cases", "Filter giữ gần hết rows: late fetch/gather overhead có thể không bù bytes. Complex/nested column: decoding/materialization dominate và vector primitive ít. Opaque UDF: batching còn nhưng call/conversion chặn tight loop. Bảng rất hẹp hoặc dataset nhỏ: overhead setup/selection/JIT có thể lớn hơn saved work. Mỗi case vẽ pipeline trước-sau, nêu expected counter rồi đo. Correctness oracle gồm result hash, null behavior, order nếu contract yêu cầu và floating-point tolerance có lý do."),
        ),
        (
            "tuple at a time trả dispatch overhead mỗi row",
            "full-column processing có intermediate memory traffic",
            "vector batch size tối ưu phụ thuộc cache và tuple width",
            "selection vector giữ positions thay vì copy payload",
            "dense mask và sparse index có trade-off khác nhau",
            "null mask phải giữ SQL three-valued logic",
            "late materialization thắng mạnh khi selectivity thấp và deferred columns rộng",
            "high selectivity có thể làm early materialization tốt hơn",
            "gather ngẫu nhiên làm mất locality",
            "encoded execution là operator encoding specific",
            "dictionary codes giữa chunks không mặc nhiên so được",
            "blocking operator tạo materialization boundary",
            "JIT khác vectorized execution",
            "opaque UDF có thể phá fusion và batching",
            "built-in và UDF benchmark phải giữ semantics giống nhau",
        ),
    ),
    Lesson(
        208,
        "Lesson_208-vectorized-execution-is-not-simd",
        "Vectorized Execution Is Not SIMD",
        "96-vectorized-execution-not-simd.md",
        "wiki.olap.vectorized-execution-not-simd",
        "Làm sao tách batching ở query engine khỏi compiler auto-vectorization và SIMD instructions, rồi đo contribution mà không giả định hai speedup cộng tuyến tính?",
        (X1, LL, IN),
        (X1L, LLL, INL),
        (
            ("Ba tầng thường bị gọi cùng một chữ", "Engine vectorization là API/dataflow theo batch: operator nhận nhiều values mỗi call. Compiler vectorization biến scalar IR loops thành vector IR/instructions nếu legality và cost model cho phép. SIMD là ISA hardware thực thi một instruction trên nhiều lanes. Batch loop tạo contiguous, type-specialized code dễ auto-vectorize nhưng không đảm bảo SIMD; batching vẫn giảm dispatch/branch/type overhead khi compiler sinh scalar instructions. Ngược lại, một scalar-looking library function có thể gọi SIMD kernel mà engine không dùng vector batches."),
            ("Thiết kế ba cấu hình", "A: tuple/row-at-a-time scalar baseline. B: cùng batch operator nhưng compile với loop/SLP vectorization disabled và xác minh no-SIMD trong optimization remarks/assembly. C: batch operator với target ISA và vectorization enabled hoặc explicit SIMD kernel. Giữ algorithm, data layout, null semantics, compiler version/optimization, threads, CPU affinity và frequency policy. Nếu A dùng code path khác nhiều ngoài batching, chênh A-B không chỉ batching. B-C cũng gồm compiler transformations liên quan; báo limitations thay vì đặt tên tuyệt đối."),
            ("Contribution có interaction", "Có thể báo `batch_gain = T_A/T_B` và `simd_increment = T_B/T_C` hoặc saved cycles, nhưng total speedup không bằng cộng hai phần trăm vì mechanisms tương tác. SIMD profitability thay khi batching đổi loop length, branch shape, alignment và cache behavior. Thêm factorial design batch on/off × SIMD on/off nếu implementation cho phép; interaction term làm rõ synergy/antagonism. Nếu row-at-a-time+SIMD không có ý nghĩa kỹ thuật, ghi missing cell. Kết luận bám configurations, không nói batching đóng góp một tỷ lệ cố định."),
            ("Batch size và cache", "Batch quá nhỏ không amortize calls/setup; trip count ngắn làm vector loop dành nhiều thời gian cho checks/tail. Batch lớn tăng working set, cache misses, latency, memory pressure và có thể làm downstream buffer/spill. Test logarithmic sizes quanh engine default, không chỉ bốn con số tùy ý. Báo cycles/row, instructions/row, branches/misses, cache/TLB misses, bandwidth và wall time. Optimum có thể khác giữa filter, aggregation, strings và wide rows."),
            ("Masks, nulls, tails và branches", "Selection/null mask ở engine có thể được compiler hạ thành predication/writemask hoặc scalar branches. SIMD tail xử lý bằng scalar epilogue, masked lanes hoặc vector-length mechanism tùy ISA/compiler. Branch-heavy predicate có thể vectorize qua masks, nhưng divergent work vẫn thực hiện lanes hoặc tạo compaction cost. LLVM diagnostics cho biết missed reason; Intel guide minh họa writemask ở ISA cụ thể. Không gán mọi branch cho SIMD failure nếu assembly cho predicated path."),
            ("Memory access và gather", "Contiguous aligned loads phù hợp lanes; selection indices có thể đòi gather, vốn có latency/throughput và cache behavior khác. Sparse positions làm lanes sử dụng thấp; dictionary codes/bit-packed values cần unpack trước hoặc kernel specialized. Khi memory bandwidth saturates, nhiều SIMD lanes không giảm wall time tương ứng. Đo bytes/cycle và bandwidth cùng vector instruction count. CPU counters phụ thuộc PMU/model và multiplexing; ghi counter definitions, runs, variance và permissions."),
            ("Semantics và floating point", "Integer sum có overflow contract; floating reduction đổi association khi vectorized nên bitwise result có thể khác. LLVM chỉ cho phép một số floating reductions khi semantics/flags cho phép hoặc dùng ordered reduction chậm hơn. Không bật fast-math chỉ để benchmark đẹp nếu product cần IEEE/NaN/signed-zero behavior. Verify exact integer/hash và documented tolerance/ULP cho float. Null lanes và exceptions phải giữ error model; masked lane không được đọc out-of-bounds."),
            ("Lab có proof của code path", "Tạo sum/filter kernels với null/no-null và branch/simple variants. Lưu source hash, compiler flags, target CPU, optimization remarks và disassembly snippet/count để chứng minh configuration. Chạy sizes/batches randomized, warm-up và repeated trials; pin core nếu được phép. Dùng perf/stat tương đương cho cycles, instructions, branches, cache misses và vector counters có giải thích. Kết quả đạt khi tách batch/SIMD bằng counterfactual có proof, giải thích small-batch loss và giữ correctness; elapsed time một mình không đủ."),
        ),
        (
            "engine vectors compiler vectors và SIMD lanes là ba tầng",
            "batching có lợi ngay cả khi không có SIMD",
            "compiler remarks hoặc assembly chứng minh code path",
            "disabled auto-vectorization cần kiểm cả loop và SLP",
            "batch gain và SIMD increment có interaction",
            "factorial design tốt hơn cộng phần trăm",
            "small batch làm setup và tail overhead chiếm tỷ trọng lớn",
            "large batch có thể vượt cache working set",
            "selection mask có thể thành predication hoặc branch",
            "tail có scalar epilogue hoặc masked lanes",
            "branch-heavy code không mặc nhiên không vectorize",
            "gather làm locality và lane utilization giảm",
            "memory bandwidth có thể che SIMD benefit",
            "floating reduction có semantics reordering",
            "cycles per row cần frequency affinity và variance context",
        ),
    ),
    Lesson(
        209,
        "Lesson_209-partitioning-clustering-and-sort-order",
        "Partitioning Clustering and Sort Order",
        "97-partitioning-clustering-sort-order.md",
        "wiki.olap.partitioning-clustering-sort-order",
        "Chọn partition transform, clustering và sort order bằng cách cân pruning, file size, metadata, write maintenance và workload mix như thế nào?",
        (DP, CS, PR),
        (DPL, CSL, PRL),
        (
            ("Ba lớp bố trí", "Partitioning đặt rows vào logical/physical groups bằng transform như day/month/bucket/category và cho coarse pruning từ metadata. Bucketing/hash distribution gom keys theo buckets nhưng không tạo range order. Clustering/sort sắp hoặc đồng vị trí rows trong partition/file/row groups để min/max hẹp, compression và locality tốt hơn. Thuật ngữ sản phẩm khác nhau; lesson luôn ghi unit và guarantee. 'Clustered' có thể chỉ tương quan, không phải globally sorted. Partitioning table khác distributed hash partitioning giữa MPP workers."),
            ("High cardinality là risk, không định luật", "Partition theo user_id/order_id có thể tạo rất nhiều partitions/directories/files, nhưng số file còn phụ thuộc writers, ingest batches, target file size và format/table service; không phải cứ high-cardinality là tự động hàng triệu file. Điều cần đo là active partition count per write, files/partition, size distribution và metadata/split cost. Low-cardinality key cũng thất bại nếu một partition quá lớn hoặc skew. Chọn transform/granularity để partitions đủ lớn, lifecycle quản được và filter phổ biến có thể prune."),
            ("Small-file penalty", "Mỗi file thêm metadata row/manifest/metastore entry, list/open/range requests, split scheduling, footer read, task setup và thường có row groups nhỏ nên compression/scan kém. Object storage latency và coordinator scheduling có thể làm query metadata-bound trước khi đọc nhiều bytes. Song song nhiều files đôi khi tăng throughput, nên 'ít file hơn luôn tốt' cũng sai. Báo count, p10/p50/p90 size, files opened, listing/planning time, splits/tasks, bytes/read requests và scan/CPU. Compaction giảm files nhưng tạo write/compute cost và concurrency semantics."),
            ("Sort order đa cột", "Lexicographic sort ưu tiên cột đầu; cột sau chỉ ordered trong equal-prefix groups. Vì thế time→customer khác customer→time cho ranges khác nhau. Analogy với composite index giúp nhớ prefix, nhưng zonemap lưu per-column min/max nên vẫn có thể hưởng partial correlation ngoài strict prefix; mức lợi phải đo. Sort tăng RLE/compression ở leading columns và pruning ranges, đồng thời tốn sort/merge, có thể giảm write throughput và làm query theo key khác tệ hơn."),
            ("Clustering drift và maintenance", "Append data không theo key, late events, updates và compaction có thể làm clustering degrade. Một table tạo ban đầu sorted không bảo đảm six months later vẫn correlated. Theo dõi overlap/depth, min-max width, files touched/query, pruning ratio và reclustering backlog/cost tùy engine. Maintenance policy có trigger và budget, không chạy định kỳ mù. Recluster/optimize cần snapshot correctness, concurrent-write behavior và rollback/cleanup; Trino/Presto paper cảnh báo enumeration/small-file overhead nhưng implementation operation tùy connector."),
            ("Workload-weighted decision", "Liệt kê query families với frequency, scanned horizon, filter columns/selectivity, join/group keys, SLA và concurrency. Thêm ingest/update pattern, retention, late data, compaction window và cost. Candidate score không chỉ average query time: p95, bytes, files, metadata time, write amplification và storage. Một daily partition có thể tốt cho 30-day ranges nhưng tệ nếu millions tiny tenants write each hour. Reversal trigger gồm query mix shift, partition size vượt/thiếu target, small-file count hoặc maintenance budget."),
            ("Ba phương án thí nghiệm", "A partition coarse theo low-cardinality/time transform. B partition theo high-cardinality key với cùng writer concurrency/batch để lộ fragmentation thực. C coarse partition cộng sort/cluster theo frequent filter. Giữ same data/hash/format/codec/target file settings; nếu systems tự coalesce, ghi actual files thay assumptions. Năm queries gồm partition equality/range, leading sort filter, second sort filter, unrelated filter và full scan. Tách metadata/planning khỏi scan/execution; đo write/compaction cost."),
            ("Quyết định và remediation", "Chọn phương án trên Pareto frontier, không dựa một truy vấn thắng nhất. Nếu B tạo small files, remediation có thể đổi transform, buffer writes, target size hoặc compaction; không chỉ tăng coordinator. Nếu C giúp query nhưng sort cost phá freshness, giảm clustering depth hoặc asynchronous maintenance. Document layout version/effective snapshot; layout migration có dual-read/rewrite validation và old files cleanup. Done khi cả pruning benefit và file/maintenance penalty có số, correctness bằng nhau và lựa chọn nối workload."),
        ),
        (
            "partition bucketing clustering sort là concepts khác nhau",
            "high cardinality là fragmentation risk không deterministic file count",
            "low cardinality vẫn có skew và oversized partition",
            "active partitions per write quan trọng hơn domain cardinality đơn lẻ",
            "small files tăng metadata open split task overhead",
            "nhiều files đôi khi tăng parallelism",
            "file size distribution tốt hơn chỉ average",
            "compaction có write cost và concurrency semantics",
            "multi-column sort ưu tiên leading key",
            "composite-index analogy có giới hạn với zonemaps",
            "sort order ảnh hưởng compression và pruning",
            "clustering degrade khi append late data",
            "layout decision cần weighted query families",
            "metadata time phải tách scan time",
            "layout migration cần version và cleanup evidence",
        ),
    ),
    Lesson(
        210,
        "Lesson_210-mpp-coordinator-fragments-and-exchange",
        "MPP - Coordinator Fragments and Exchange",
        "98-mpp-coordinator-fragments-exchange.md",
        "wiki.olap.mpp-fragments-exchange",
        "Đọc distributed plan từ coordinator qua fragments/tasks/exchanges như thế nào để dự đoán network, skew, critical path và hiệu ứng tăng số worker?",
        (PR, TR, CS),
        (PRL, TRL, CSL),
        (
            ("Từ SQL tới work graph", "Coordinator parse/analyze/optimize, tạo distributed plan, quản stage/task/split scheduling và thu trạng thái; workers scan qua connectors và chạy operators. Fragment/stage là subplan ngăn bởi exchange; mỗi stage có tasks trên một hoặc nhiều workers, mỗi task có drivers/operators. Tên khác nhau giữa engines nhưng graph cần đọc theo source splits, operator pipeline, distribution boundary và sink. Coordinator không nhất thiết xử lý data rows chính, nhưng planning, metadata, scheduling và final gather có thể thành bottleneck."),
            ("Exchange modes", "Gather đưa partitions về một/few consumer, thường cho final aggregation/order/result. Repartition/hash gửi mỗi row theo key để cùng key gặp cùng worker cho join/group. Broadcast/replicate gửi build input tới mọi workers, tránh shuffle probe nhưng nhân bytes/memory. Round-robin/arbitrary cân rows khi không cần key. Local exchange chỉ rearrange giữa threads/tasks cùng node; remote exchange qua network hoặc spooled storage. Plan phải ghi input/output rows/bytes, partition keys, fanout và materialization/backpressure."),
            ("Exchange không phải network duy nhất", "Roadmap nói exchange là chỗ duy nhất dữ liệu đi qua mạng; điều này sai với scans từ object storage/remote connectors, broadcast control/data, spill/exchange storage, result transfer và service traffic. Remote exchange thường là intermediate network boundary lớn và controllable, nên được soi đầu tiên nhưng không duy nhất. Tách source-read bytes, exchange bytes, spill bytes và output bytes. Network estimate trong EXPLAIN có thể là cost-model unit/estimate; runtime stage/task counters mới là observation."),
            ("Local/co-located join", "Nếu both sides có compatible hash partitioning trên exact join keys, hash function/version, bucket count/mapping và data validity, engine có thể colocate join, giảm repartition. Partition pruning/storage layout không tự đồng nghĩa worker distribution. Small build có thể broadcast tốt hơn, nhưng phải fit memory trên mỗi worker sau filter. Partial aggregation trước exchange giảm rows/bytes nếu groups compress nhiều; high-cardinality groups có thể giảm ít. Dynamic filtering có thể prune probe nhưng đến trễ hoặc threshold-limited."),
            ("Skew và stragglers", "Hash key hot/null/default làm một partition lớn; range partitions có uneven distribution; source splits/files cũng skew. Stage completion bị worker/task chậm nhất giữ critical path. Average rows/task che max/p99, CPU time, blocked time, peak memory, spill và output bytes. Salting, split hot keys, broadcast small side, two-phase aggregation hoặc better partition keys có trade-offs và correctness. Thêm nodes không sửa một hot partition nếu partitioning/granularity không đổi; có thể tăng scheduling/network overhead."),
            ("Strong scaling và weak scaling", "Gấp đôi workers với fixed data/query là strong scaling; ideal half time chỉ khi parallel fraction lớn, đủ splits và overhead nhỏ. Serial/coordinator/final gather, exchange, skew, remote storage bandwidth và startup tạo Amdahl limit. Weak scaling tăng data cùng workers và hỏi time có giữ gần constant; Gustafson-style reasoning áp cho scaled problem, không chứng minh fixed job linear speedup. Báo speedup `T1/Tp`, efficiency `speedup/p`, cost/work và per-stage critical path. Một run nhanh hơn do cache/autoscaling không phải scaling proof."),
            ("Estimates và actuals", "EXPLAIN cho fragment/distribution và estimated rows/bytes/cost; missing/stale stats làm chọn broadcast/repartition hoặc join order sai. EXPLAIN ANALYZE/UI cho actual input/output, tasks, CPU/scheduled/blocked time, memory, network/spill và skew tùy engine. Estimate-vs-actual ratio ở exchange input/build side quan trọng hơn total query only. Plan text có `RemoteExchange` chứng minh boundary, không chứng minh bytes là bottleneck. Capture query ID, engine/config, connector, cluster size và runtime JSON."),
            ("Lab ba layouts và node counts", "Cùng query/data chạy: both sides colocated compatible; one/both sides mismatched cần repartition; small filtered build broadcast. Với mỗi plan đánh dấu fragments, local/remote exchanges, keys/modes, estimated và actual bytes, task skew. Chạy p và 2p workers sau warm-up với fixed data, đồng thời một weak-scaling case nếu resource cho phép. Dự đoán trước critical stage và speedup interval; sau run giải thích deviation bằng counters. Kết luận đạt nếu nhận đúng boundaries và 2/3 predictions trong tolerance đã đặt, không đổi layout giữa prediction và run."),
        ),
        (
            "coordinator lập plan schedule và có thể bottleneck metadata",
            "fragment boundary thường tương ứng remote exchange",
            "local exchange khác remote exchange",
            "gather repartition broadcast round robin có semantics khác",
            "exchange không phải nguồn network bytes duy nhất",
            "source scan và result output phải đo riêng",
            "colocated join cần compatible partition contract",
            "storage partition không tự đồng nghĩa worker distribution",
            "broadcast nhân build memory trên mỗi worker",
            "partial aggregation giảm shuffle chỉ khi groups coalesce",
            "skew cần max p99 task counters không dùng average",
            "thêm node không chia được hot partition cố định",
            "strong scaling fixed work khác weak scaling scaled work",
            "Amdahl limit gồm coordinator gather exchange và skew",
            "plan estimate không thay runtime actual counters",
        ),
    ),
)


VERIFY = {
    206: "Giữ dataset/hash cố định; chạy full-scan oracle và từng pruning level, lưu candidate/read/skipped units, bytes, plan/runtime counters. Inject function, cast, comparison and stale/unknown-statistics cases.",
    207: "Vẽ pipeline và materialization points; đo row, batch, selection, early/late and built-in/UDF variants bằng result oracle, calls, batches, bytes, allocations, CPU/cache counters.",
    208: "Chạy controlled factorial/three-path build; lưu compiler flags, optimization remarks, assembly proof, batch sizes, perf counters and correctness. Báo interaction thay vì cộng speedup tuyến tính.",
    209: "Ghi cùng data theo ba layouts; đo partition/file distribution, listing/planning, splits, bytes, p95 query, write/compaction cost và correctness. Thay query mix hoặc ingest granularity để tìm reversal.",
    210: "Capture distributed plan và runtime JSON; đánh dấu fragments/exchanges, source/exchange/spill/output bytes, task skew, critical stage. Chạy fixed-data p/2p và một scaled-data case nếu có.",
}

QUERIES = {
    206: ["Phân biệt partition file row-group page và dynamic pruning thế nào?", "Tại sao function wrapper không phải lúc nào cũng chặn pruning?", "Cách phát hiện pruning cắt nhầm dữ liệu là gì?"],
    207: ["Selection vector giảm copy nhưng tạo chi phí nào?", "Khi nào late materialization thua early materialization?", "Encoded execution có áp cho mọi operator không?"],
    208: ["Vectorized execution khác SIMD ở tầng nào?", "Tách batch gain và SIMD increment bằng cấu hình nào?", "Vì sao speedup batching và SIMD không cộng tuyến tính?"],
    209: ["High-cardinality partition có luôn tạo hàng triệu file không?", "Small-file penalty gồm những counter nào?", "Sort order nhiều cột ảnh hưởng pruning thế nào?"],
    210: ["Exchange có phải nơi duy nhất dữ liệu qua mạng không?", "Khi nào colocated join thực sự tránh repartition?", "Phân biệt strong scaling và weak scaling trong MPP thế nào?"],
}

NEW_SOURCES = (
    {"source_id": X1, "record_path": "1_Nguon/Papers/SRC-MONETDB-X100-HYPER-PIPELINING.md", "canonical_url": "https://cs.brown.edu/courses/cs227/archives/2008/Papers/ColumnStores/MonetDB.pdf", "captured": "2026-10-01", "rights": "public-research-paper"},
    {"source_id": MA, "record_path": "1_Nguon/Papers/SRC-ABADI-MATERIALIZATION-STRATEGIES.md", "canonical_url": "https://www.cs.umd.edu/~abadi/papers/abadiicde2007.pdf", "captured": "2026-10-01", "rights": "IEEE-paper-public-author-copy"},
    {"source_id": LL, "record_path": "1_Nguon/Web/SRC-LLVM-AUTO-VECTORIZATION.md", "canonical_url": "https://llvm.org/docs/Vectorizers.html", "captured": "2026-10-01", "rights": "LLVM-project-documentation"},
    {"source_id": IN, "record_path": "1_Nguon/Web/SRC-INTEL-INTRINSICS-GUIDE.md", "canonical_url": "https://www.intel.com/content/www/us/en/docs/intrinsics-guide/index.html", "captured": "2026-10-01", "rights": "public-vendor-documentation"},
    {"source_id": DZ, "record_path": "1_Nguon/Web/SRC-DUCKDB-ZONEMAPS.md", "canonical_url": "https://duckdb.org/docs/stable/guides/performance/indexing", "captured": "2026-10-01", "rights": "public-web-documentation"},
    {"source_id": TD, "record_path": "1_Nguon/Web/SRC-TRINO-DYNAMIC-FILTERING.md", "canonical_url": "https://trino.io/docs/current/admin/dynamic-filtering.html", "captured": "2026-10-01", "rights": "public-project-documentation"},
    {"source_id": PR, "record_path": "1_Nguon/Papers/SRC-PRESTO-SQL-ON-EVERYTHING.md", "canonical_url": "https://trino.io/Presto_SQL_on_Everything.pdf", "captured": "2026-10-01", "rights": "public-research-paper"},
    {"source_id": TR, "record_path": "1_Nguon/Web/SRC-TRINO-DISTRIBUTED-PLANS.md", "canonical_url": "https://trino.io/docs/current/sql/explain.html", "captured": "2026-10-01", "rights": "public-project-documentation"},
)


def folder(lesson: Lesson):
    return BASE / lesson.directory


def frontmatter(lesson: Lesson) -> str:
    sources = "\n".join(f"  - {source}" for source in lesson.sources)
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
tags: [wiki/database-systems, olap, query-execution, performance]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/{lesson.filename}
---
"""


def deep_note(lesson: Lesson) -> str:
    parts = [frontmatter(lesson), f"# {lesson.title}\n\n> [!abstract] Câu hỏi trung tâm\n> {lesson.question}\n"]
    for index, (heading, body) in enumerate(lesson.core, 1):
        parts.append(f"\n## {index}. {heading}\n\n{body}\n")
    parts.append("\n## 8. Ma trận kiểm chứng từng mệnh đề\n\nMỗi mệnh đề hiệu năng cần counterfactual, correctness oracle và counter ở đúng tầng. Elapsed time, plan label hoặc tên công nghệ riêng lẻ không đủ quy nguyên nhân.\n")
    for index, probe in enumerate(lesson.probes, 1):
        parts.append(
            f"\n### 8.{index}. {probe}\n\n"
            f"**Mệnh đề cần kiểm.** {probe}.\n\n"
            f"**Cách kiểm.** {VERIFY[lesson.number]} Với mệnh đề này, ghi engine/compiler/format version, data shape, controlled variables, expected counter, failure signal và boundary làm kết luận không còn đúng.\n\n"
            "**Bằng chứng đạt.** Lưu generator/hash, configuration, query/source, plan/profile/compiler proof, raw counters, result oracle, repetitions và reviewer. Nếu chưa chạy lab được phép, chỉ ghi protocol; không biến expected result thành số đo đã quan sát.\n"
        )
    parts.append(
        """
## 9. Quy trình phản biện

1. Vẽ data path và xác định tầng storage, reader, engine, compiler, ISA hoặc network đang được nói tới.
2. Khóa semantics, dataset và correctness oracle trước khi đo performance.
3. Thay một mechanism; giữ các mechanisms còn lại cố định hoặc ghi confounder.
4. Đọc plans/remarks nhưng xác nhận bằng runtime counters hoặc assembly khi phù hợp.
5. Báo distribution và critical path, không dùng một average che skew hoặc tails.
6. Viết reversal case và stop condition trước khi chạy.
7. Chưa có execution evidence thì giữ trạng thái `review`.

## 10. Câu hỏi tự kiểm tra

1. Mechanism nằm ở tầng nào và counter trực tiếp của nó là gì?
2. Kết quả đúng được xác minh độc lập ra sao?
3. Biến nào thực sự đổi giữa hai cấu hình?
4. Overhead cố định, bandwidth, skew hoặc tail nào có thể che kết quả?
5. Constraint nào làm lựa chọn hiện tại phải đảo?
6. Kết luận nào mới là protocol, chưa phải observation?

## 11. Giới hạn và điều chưa cho phép kết luận

- Chưa chạy pruning, vectorization, layout hoặc MPP benchmarks; note mô tả protocol và expected evidence.
- Tài liệu engine/compiler được kiểm ngày 2026-10-01; version, plan format, counters và optimizer support có thể đổi.
- Taxonomy và lab matrices là curriculum synthesis; không gán nguyên văn cho một paper hoặc vendor.
- Microbenchmark không chứng minh production speedup nếu data, concurrency, cache, compiler, storage hoặc network khác.
- Note giữ trạng thái `review` cho tới khi chủ dự án duyệt semantic meaning.
"""
    )
    references = "\n".join(f"{index}. [[{link}]]" for index, link in enumerate(lesson.source_links, 1))
    coverage = "\n".join(
        f"| [[{link}]] | Khái niệm, mechanism hoặc evidence boundary liên quan | Đã đọc locator trong source record; không suy ngoài phạm vi |"
        for link in lesson.source_links
    )
    takeaways = {
        206: "Pruning phải được chứng minh bằng units/bytes skipped và full-scan oracle; filter trong plan chưa đủ.",
        207: "Batching, selection, late materialization và encoded execution có reversal cases riêng; không có cơ chế luôn thắng.",
        208: "Engine vector batches không đồng nghĩa SIMD; contribution cần binary/compiler proof và thiết kế counterfactual có interaction.",
        209: "Layout là bài toán Pareto giữa pruning, metadata, files, write maintenance và workload mix.",
        210: "Distributed plan được đọc qua fragment/exchange/critical path; tăng worker chỉ giúp phần thực sự chia được và không skew.",
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
- Correctness oracle và controlled variables đi trước mọi speedup claim.
- Plan estimate, compiler flag hoặc engine feature không thay runtime evidence.
- Average phải đi cùng tails, skew, bytes/units và critical-path counters.
- Chưa chạy lab thì artifact là giáo trình đã kiểm cấu trúc, không phải benchmark result hay production certification.
"""
    )
    return "".join(parts)


def curriculum(lesson: Lesson, knowledge: str):
    outcome, assessment, lab, pitfalls, homework, done = previous.contract(lesson)
    header = f"# Phase 6: Analytical Storage and Query Engines\n# Module 14: OLAP Internals and Analytical Engines\n# Lesson {lesson.number}: {lesson.title}"
    body = re.sub(r"^---\n.*?\n---\n", "", knowledge, flags=re.S)
    body = re.sub(r"^# .+\n+", "", body, count=1)
    note = f"{header}\n\n## Mục tiêu bài học\n\n**Năng lực cần chứng minh.** {outcome}\n\n**Điều kiện hoàn thành.** {done}\n\n{body}"
    safety = "Chỉ dùng synthetic fixture, local/isolated engines và benchmark host được phép. Không chạy load trên hệ dùng chung, đổi compiler/system settings toàn máy hoặc dùng dữ liệu nhạy cảm. Lưu version, configuration, data hash, commands, raw counters, result oracle, repetitions và limitations."
    questions = "\n".join(
        f"{index}. {question}"
        for index, question in enumerate((
            "Nêu mechanism và tầng thực thi trung tâm.",
            "Đưa một counter trực tiếp và một proxy dễ gây hiểu sai.",
            "Nêu counterexample làm optimization mất tác dụng.",
            "Phân biệt expected result với evidence đã quan sát.",
        ), 1)
    )
    after = f"{header}\n\n## Thực hành\n\n**Nhiệm vụ.** {lab}\n\n{safety}\n\n## Kiểm tra cuối bài\n\n{questions}\n\n## Tiêu chí hoàn thành\n\n**Cách đánh giá.** {assessment}\n\n**Điều kiện đạt.** {done}\n\n## Bài làm sau buổi học\n\n**Nhiệm vụ.** {homework}\n\n**Lỗi cần chủ động loại trừ.** {pitfalls}\n\n## Reference\n\n- Knowledge note: `{(PACK / lesson.filename).relative_to(ROOT)}`\n- Nội dung học thuật: `note.md` cùng thư mục.\n"
    return note, after


def update_manifest(check: bool = False):
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
    data["version"] = "1.0.41"
    data["updated_at"] = "2026-10-01T23:59:00+07:00"
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
