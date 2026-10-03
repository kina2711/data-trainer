#!/usr/bin/env python3
"""Build source-grounded L211-L215 scaling, architecture and cost notes."""
from __future__ import annotations

import argparse
import json

import promote_l206_l210_notes as previous
from format_knowledge_notes import normalize_markdown
from promote_l201_l205_notes import Lesson

ROOT = previous.ROOT
BASE = previous.BASE
PACK = previous.PACK
WIKI = previous.WIKI

AM = "src.paper.amdahl-1967"
GU = "src.paper.gustafson-1988"
PR = "src.paper.presto-sql-on-everything"
TR = "src.web.trino-distributed-plans"
TJ = "src.web.trino-join-distribution"
TS = "src.web.trino-spill"
SF = "src.paper.snowflake-elastic-data-warehouse"
RW = "src.web.redshift-wlm-query-metrics"
RC = "src.web.redshift-concurrency-scaling"
FD = "src.web.finops-data-cloud-platforms"
FU = "src.web.finops-unit-economics"
BQ = "src.web.bigquery-pricing-slots"

AML = "SRC-AMDAHL-1967"
GUL = "SRC-GUSTAFSON-1988"
PRL = "SRC-PRESTO-SQL-ON-EVERYTHING"
TRL = "SRC-TRINO-DISTRIBUTED-PLANS"
TJL = "SRC-TRINO-JOIN-DISTRIBUTION"
TSL = "SRC-TRINO-SPILL"
SFL = "SRC-SNOWFLAKE-ELASTIC-DATA-WAREHOUSE"
RWL = "SRC-REDSHIFT-WLM-QUERY-METRICS"
RCL = "SRC-REDSHIFT-CONCURRENCY-SCALING"
FDL = "SRC-FINOPS-DATA-CLOUD-PLATFORMS"
FUL = "SRC-FINOPS-UNIT-ECONOMICS"
BQL = "SRC-BIGQUERY-PRICING-SLOTS"


LESSONS = (
    Lesson(
        211,
        "Lesson_211-mpp-as-distributed-mimd-and-spmd-the-strong-scaling-lab",
        "MPP Strong Scaling - MIMD SPMD Batch and SIMD",
        "99-mpp-strong-scaling-mimd-spmd-batch-simd.md",
        "wiki.olap.mpp-strong-scaling-mimd-spmd-batch-simd",
        "Làm sao truy vết ba tầng parallelism của một MPP query và xác định strong-scaling ceiling bằng evidence thay vì gán mọi speedup cho số worker?",
        (AM, GU, PR, TR),
        (AML, GUL, PRL, TRL),
        (
            ("Bốn khái niệm không đồng cấp", "Flynn MIMD mô tả nhiều processing elements có instruction stream và data stream riêng; trong cụm MPP, workers/tasks có tiến độ và failure mode độc lập. SPMD là programming/execution pattern: nhiều workers chạy cùng program fragment trên partitions khác nhau, nhưng không đồng bộ từng instruction. Vectorized execution là interface theo batch bên trong một task. SIMD là instruction-level execution trên lanes trong một core. Một query có thể đồng thời là distributed MIMD, tổ chức theo SPMD, chạy vector batches và dùng SIMD. Bốn nhãn trả lời bốn câu hỏi; không được cộng chúng thành một con số parallelism duy nhất."),
            ("Strong scaling và đại lượng đo", "Strong scaling giữ nguyên query, input snapshot và output rồi tăng resources. Với thời gian `T_1` và `T_p`, speedup là `S_p = T_1/T_p`; efficiency là `E_p = S_p/p`. Efficiency dưới một không tự chứng minh lỗi: startup, split granularity, coordinator, exchange, contention và measurement noise đều góp phần. Cost thường tăng dù latency giảm, nên báo node-seconds hoặc compute-unit-seconds bên cạnh time. Nếu configuration một node không chạy được vì memory, baseline hợp lệ có thể là số node nhỏ nhất; ký hiệu speedup relative và không gọi nó là `T_1`."),
            ("Amdahl là boundary, không phải diagnosis", "Với fraction song song lý tưởng `f`, upper-bound cổ điển là `1 / ((1-f)+f/p)`. Fraction suy ngược từ timings là effective serial fraction: nó hấp thụ coordinator, communication, barriers, skew, fixed startup và external bandwidth. Nó không chỉ ra nguyên nhân vật lý. Dùng stage/task counters để phân rã compute, blocked/network, source read, spill và final gather. Nếu dataset không vừa cache hoặc engine đổi algorithm khi tăng p, giả định cùng công việc bị phá; đường cong vẫn hữu ích nhưng không còn là thí nghiệm một biến."),
            ("Weak scaling và Gustafson", "Weak scaling tăng input/work cùng resources và hỏi time hoặc throughput per node có giữ ổn định. Gustafson-style scaled speedup phù hợp câu hỏi capacity: với cùng elapsed budget, cụm lớn giải được bài toán lớn hơn bao nhiêu. Nó không thay strong-scaling result cho fixed query. Một hệ có weak scaling tốt nhưng latency một query fixed-size không giảm sau bốn nodes; ngược lại cache locality có thể tạo superlinear point tạm thời. Báo data per worker, output cardinality, query semantics và bottleneck khi so hai curves."),
            ("Barrier và critical path", "Stage kết thúc theo task chậm nhất, không theo average. Remote exchange, final aggregation/order, build completion hoặc explicit materialization tạo synchronization boundaries. Với mỗi stage lưu task duration distribution, max/median ratio, rows/bytes, CPU, scheduled/blocked time, peak memory và spill. Straggler có thể do hot key, uneven files/splits, remote storage, GC, retry, noisy neighbor hoặc hardware. Chênh task time là symptom; chỉ gọi skew khi input/output distribution hoặc key frequency ủng hộ."),
            ("External ceilings", "Thêm workers không tăng source bandwidth nếu object store, connector database, API, metadata service hoặc client sink đã saturated. Coordinator có thể nghẽn planning/scheduling/final result; network bisection và exchange serialization có thể chi phối. Dùng resource-level counters và control query để nhận biết. Nếu aggregate source throughput không tăng từ p=4 tới p=8 trong khi CPU workers idle/blocked, ceiling thuộc upstream path. Nếu one partition/task max giữ nguyên, nghi granularity/skew. Nếu coordinator CPU/queue tăng, không quy cho SIMD hay vector batches."),
            ("Truy xuống batch và SIMD", "Chọn một task trong critical stage, ghi operator pipeline, batch/chunk size, rows/batch và CPU counters. Sau đó dùng engine profile, compiler remarks hoặc disassembly nếu được phép để xác minh vector instructions. Cluster speedup không chứng minh SIMD; SIMD instruction count không chứng minh end-to-end benefit nếu network dominant. Phân tích theo nested boundary: query wall time → stage critical path → task/operator CPU → batch loop → instructions. Mỗi tầng cần counterfactual riêng và correctness oracle giống nhau."),
            ("Lab 1-2-4-8 workers", "Khóa snapshot, query text, statistics, layout, caches, concurrency, engine version, worker shape và output hash. Randomize hoặc interleave node counts, chạy warm-up tách biệt và lặp đủ để báo median cùng dispersion. Với mỗi mức ghi wall time, node-seconds, source/exchange/output bytes, stage/task distributions và retries. Tính speedup/efficiency, xác định đoạn marginal gain giảm. Gán ceiling vào serial/coordinator, communication, skew/granularity hoặc external bottleneck chỉ khi counter trực tiếp thay đổi theo dự đoán. Thêm weak-scaling run riêng; không trộn vào strong-scaling table."),
        ),
        (
            "MIMD là taxonomy của instruction/data streams chứ không phải đồng hồ chung",
            "SPMD tasks có thể tiến triển và hỏng độc lập",
            "batch execution thuộc engine còn SIMD thuộc ISA",
            "strong scaling giữ fixed work và fixed result",
            "relative baseline nhiều node phải được ghi rõ",
            "speedup cần đi cùng parallel efficiency và node-seconds",
            "effective serial fraction không tự chỉ ra root cause",
            "Amdahl upper bound cần giả định cùng algorithm và workload",
            "weak scaling trả lời capacity chứ không trả lời fixed-query latency",
            "superlinear point có thể đến từ cache hoặc algorithm transition",
            "critical path theo max task không theo average",
            "straggler không đồng nghĩa data skew",
            "external source bandwidth có thể tạo ceiling",
            "cluster speedup không chứng minh SIMD",
            "ba tầng phải có evidence riêng rồi mới nối causal chain",
        ),
    ),
    Lesson(
        212,
        "Lesson_212-broadcast-repartition-skew-and-spill",
        "Broadcast Repartition Skew and Spill",
        "100-broadcast-repartition-skew-spill.md",
        "wiki.olap.broadcast-repartition-skew-spill",
        "Phân biệt broadcast, repartition, skew và spill từ plan/runtime counters như thế nào, rồi chọn remediation mà không che nhầm nguyên nhân?",
        (TJ, TS, TR),
        (TJL, TSL, TRL),
        (
            ("Broadcast join", "Build side sau filter được replicate tới workers xử lý probe. Lợi ích là tránh repartition probe side và cho local hash probes. Chi phí gồm network fanout, deserialize/build CPU và một bản hash table trong memory domain của mỗi task/worker tùy engine. Raw table size chưa đủ để quyết định; phải xét build output sau filter/projection, representation overhead, concurrency và per-node limit. Statistics sai có thể chọn broadcast không phù hợp; cap là guardrail, không chứng minh đủ memory. Capture estimated/actual rows-bytes, fanout, peak memory và retries."),
            ("Partitioned join", "Cả hai inputs được hash repartition theo compatible join keys; mỗi partition xây/probe cục bộ. Memory build được chia trên cluster, nhưng network có thể gần tổng bytes của hai sides sau local reductions. Hash semantics phải xử lý null/type/collation nhất quán. Partition count ảnh hưởng parallelism, per-partition overhead và spill granularity. Partitioned join không mặc nhiên chậm hơn broadcast: với build lớn, high concurrency hoặc network topology khác, nó có thể là lựa chọn an toàn và nhanh hơn."),
            ("Skew có nhiều nguồn", "Data skew do hot/null/default key; partition skew do hash/range mapping; split skew do file sizes; compute skew do expression/UDF; environment skew do noisy worker, GC hoặc retry. Symptom là max task/partition vượt median hoặc tail kéo stage, nhưng diagnosis cần input rows/bytes, output expansion, CPU/blocked, spill và key-frequency evidence. Join fanout có thể làm output skew dù inputs cân. Average che nguyên nhân. Báo p50/p95/max, coefficient hoặc max/median và top keys với privacy-safe fixtures."),
            ("Spill lifecycle", "Memory manager revoke/reserve; operator partition/serialize intermediate; write spill; sau đó read/merge/repartition để hoàn thành. Spill giảm peak memory cho operators hỗ trợ nhưng thêm bytes, I/O, CPU compression/encryption và có thể bão hòa shared disks. Phạm vi operator/case được hỗ trợ có giới hạn; một partition khổng lồ vẫn OOM. Spill là cơ chế sống sót có chi phí. Mức chậm có thể rất lớn nhưng không dùng hệ số cố định. Ghi local/remote spill bytes, files, read/write time, disk utilization và peak memory."),
            ("Bốn hiện tượng có thể đồng thời", "Broadcast sai kích thước gây memory pressure rồi spill hoặc OOM. Hot key trong repartition tạo một build partition lớn và chỉ task đó spill. Spill disk contention làm nhiều tasks chậm, nhìn giống broad skew. Vì vậy plan strategy chỉ là điểm đầu. Dựng causal timeline: estimated build → chosen distribution → actual partition distribution → memory reservation → spill → stage tails. Tắt spill để chẩn đoán có thể chuyển thành failure và chỉ chạy trong fixture cô lập; không dùng production."),
            ("Ba nhóm remediation", "Distribution: broadcast build thực sự nhỏ, partition large sides, colocate khi contract tương thích. Data: filter/project sớm, pre-aggregate, split hot keys, salt có controlled fanout hoặc isolate null/defaults. Resource/operator: tăng memory có giới hạn, chỉnh partitions, spill devices/compression, concurrency hoặc fault-tolerant path. Salting cần de-salt/aggregate đúng; replicate hot-key counterpart có memory cost. Tăng memory che symptom nếu root là key skew và không cải thiện max partition proportion."),
            ("Counterfactual diagnosis", "Giữ data/query rồi force hoặc hint broadcast và partitioned chỉ như diagnostic; hints có thể unsupported hoặc đổi semantics kế hoạch ở phiên bản khác. Với skew, so uniform fixture và one-hot fixture cùng row count. Với spill, giữ distribution và giảm memory threshold hoặc tăng build size. Mỗi intervention cần predicted counter: broadcast tăng replicated bytes/memory; repartition tăng exchange; skew tăng task dispersion; spill tăng temp bytes/I/O. Nếu counter không đổi, diagnosis bị bác bỏ."),
            ("Lab bốn ca", "Ca A build nhỏ có broadcast fit; ca B build đủ lớn làm cap/actual memory quan trọng; ca C hot key tạo straggler; ca D memory threshold gây spill trên input cân. Lưu plans, statistics, query ID, task partition metrics, exchange, peak memory, spill, result hash và repetitions. Remediate ít nhất ba ca, so trước/sau bằng cùng fixture. Done không chỉ là query thành công: strategy/counter phải khớp causal story và không làm correctness hoặc concurrency budget xấu đi không ghi nhận."),
        ),
        (
            "broadcast size phải tính sau filter projection và representation overhead",
            "broadcast nhân build state theo worker hoặc task memory domain",
            "partitioned join repartition cả hai sides theo compatible keys",
            "partitioned không mặc nhiên chậm hơn broadcast",
            "plan strategy không chứng minh actual network hay memory",
            "skew có thể đến từ data split compute hoặc environment",
            "max và p95 task metrics quan trọng hơn average",
            "join fanout có thể tạo output skew",
            "spill giảm peak memory nhưng thêm I/O và CPU",
            "spill không bảo đảm mọi large query hoàn tất",
            "một hot partition có thể vừa skew vừa spill",
            "tăng memory không sửa key distribution",
            "salting có correctness và expansion cost",
            "forced strategy chỉ là diagnostic tool",
            "mỗi remediation cần result oracle và before-after counters",
        ),
    ),
    Lesson(
        213,
        "Lesson_213-shared-nothing-against-separated-storage-and-compute",
        "Shared Nothing and Separated Storage Compute",
        "101-shared-nothing-separated-storage-compute.md",
        "wiki.olap.shared-nothing-separated-storage-compute",
        "So sánh shared-nothing với separated storage/compute bằng failure, scaling, cache và metadata boundaries nào để tránh benchmark nóng-lạnh sai?",
        (SF, PR, TR),
        (SFL, PRL, TRL),
        (
            ("Shared-nothing contract", "Mỗi node sở hữu compute, memory và local data partitions; parallel scan tận dụng locality, distributed join dựa distribution contract. Scale/membership change có thể yêu cầu redistribute/rebalance persistent data, nhưng mức độ và online behavior phụ thuộc engine: replication, elastic resize, remote tier hay managed automation có thể thay đổi. Không đồng nhất mọi MPP provisioned system với pure shared-nothing. Đánh giá bằng locality hit, redistribution bytes/time, degraded capacity, recovery semantics và operational procedure."),
            ("Separated storage and compute", "Persistent table data nằm ở shared durable storage; ephemeral/elastic compute đọc ranges và giữ local caches/temp. Compute groups có thể scale và isolate independently trong giới hạn service. Câu 'mọi lần đọc qua network' quá thô: cache hit đọc local, metadata/result cache có thể tránh data scan, còn cache miss đọc remote. Network vẫn là boundary chính để populate cache. Ghi source bytes, local cache bytes/hit, remote requests, temp spill và result reuse; không suy cache state từ runtime một mình."),
            ("Ba lớp cache", "Result cache trả prior result khi text, data freshness, role/session và engine rules phù hợp; data cache giữ table files/columns/blocks; metadata/plan cache giữ catalog/statistics/compiled state. Chúng có invalidation và scope khác nhau. Result-cache hit không đo engine execution. Data-cache warm không bảo đảm metadata warm hoặc warehouse process đã khởi động. Benchmark cần disable/bypass result cache khi có thể, log hit flag, và định nghĩa cold/warm riêng cho từng layer."),
            ("Cold không có một nghĩa duy nhất", "Cold warehouse có thể gồm compute resume/provision, empty local cache, cold object/CDN path, cold metadata/JIT và DNS/TLS setup. Người dùng thường chỉ kiểm một phần. Không được tuyên bố globally cold nếu service không cung cấp eviction/isolated fresh warehouse. Dùng operational definitions: fresh compute identifier, no result-cache hit, first access to immutable snapshot, measured remote bytes. Warm series chạy same snapshot/query family trên same warehouse sau priming. Báo unknown layers thay vì giả vờ kiểm soát."),
            ("Isolation và shared control plane", "Tách compute groups giảm competition CPU/memory/cache giữa workloads, nhưng storage service, catalog, metadata, transaction manager, identity, quota và network có thể vẫn shared. Vì vậy isolation không tuyệt đối. Test cross-workload interference ở compute, remote storage throughput và metadata latency. Một warehouse riêng có thể làm cache duplication và cost tăng. Shared-nothing cũng có WLM queues và resource groups; architecture không tự quyết toàn bộ isolation policy."),
            ("Scaling và data movement", "Pure shared-nothing scale-out cần rebalance persistent partitions hoặc chỉ dùng capacity mới cho future data/replicas tùy product. Shared-data scale-out tránh base-data rebalance nhưng phải provision workers, schedule splits và warm local cache; resize có thể giảm cache affinity. Scale-in cần drain/cancel semantics và temp state handling. So time-to-capacity, bytes moved/read, cache recovery, availability và cost during transition. Không chỉ đo steady-state query."),
            ("Metadata là data path", "Catalog maps snapshots/tables to files, statistics, permissions, transactions và pruning. Shared-data compute phụ thuộc control/metadata services để lập kế hoạch; shared-nothing cũng cần catalogs/coordinators. Bottleneck có thể xuất hiện ở listing, manifest, planning, locks hoặc service quotas trước scan. Capture planning/queue separately from execution, catalog request count/latency nếu có. Cache metadata có consistency contract; stale cache không được dùng để đổi correctness lấy speed."),
            ("Phép đo công bằng", "Chọn immutable snapshot và query suite, khóa engine/version/region/worker shape/concurrency. Tạo four cells: cold-result/cold-data theo operational definition, result-cache disabled; warm-data; explicit result-cache case; resize/resume case. Interleave trials để tránh diurnal drift, log provisioning separately, verify result hash. Với shared-nothing, thêm after-rebalance state. Với shared-data, ghi remote/local bytes. Kết luận cần distributions, cost và reversal conditions; một cold run với một warm run không hợp lệ."),
        ),
        (
            "pure shared nothing gắn persistent partitions với nodes",
            "managed variants có thể không cần full eager rebalance",
            "shared data không có nghĩa mọi read luôn từ remote storage",
            "result data metadata và plan caches phải tách",
            "result cache hit không đo query execution",
            "cold cache cần operational definition",
            "không có eviction authority thì không tuyên bố globally cold",
            "fresh compute có thể thêm provisioning latency",
            "warm cache phải giữ same snapshot và warehouse identity",
            "compute isolation không tách shared metadata storage và quotas",
            "separate warehouses có cache duplication cost",
            "scale out shared data vẫn có provisioning và cache warmup",
            "resize có thể đổi cache affinity",
            "planning metadata time phải tách execution",
            "fair comparison cần interleaved repetitions và result oracle",
        ),
    ),
    Lesson(
        214,
        "Lesson_214-workload-management-concurrency-and-cache",
        "Workload Management Concurrency and Cache",
        "102-workload-management-concurrency-cache.md",
        "wiki.olap.workload-management-concurrency-cache",
        "Tách queueing khỏi execution slowdown dưới concurrency như thế nào, và chọn admission, isolation, scaling hay query tuning dựa trên evidence nào?",
        (RW, RC, SF),
        (RWL, RCL, SFL),
        (
            ("Query lifecycle clock", "Client-observed latency có thể gồm connection/auth, admission queue, planning/compile, execution, result serialization/transfer và retries. Engine elapsed có thể loại client transfer hoặc include planning tùy metric. L214 tối thiểu tách queue time và execution time; nếu available, giữ planning và fetch riêng. Kiểm unit, clock boundary và relation thay vì giả định `elapsed = queue + execution` chính xác tuyệt đối. Redshift SYS fields là một implementation contract, không phải tên field chung."),
            ("Admission control", "Khi arrival rate và service demand vượt capacity, cho mọi query chạy có thể làm cache thrash, memory pressure, spill và context switching khiến throughput giảm. Admission giới hạn running work; excess waits hoặc rejects/deadlines. Queue tăng response time nhưng bảo vệ execution efficiency và failure rate. Policy cần max concurrency, memory/compute allocation, priority/fairness, timeout và backpressure. Little-style reasoning chỉ dùng khi system gần steady state và definitions nhất quán; bursty workload cần distribution/time series."),
            ("Queue bottleneck và heavy-query bottleneck", "Queue-bound case: service time ổn khi chạy, queue time tăng theo load và running slots saturated. Heavy-query case: một query có execution CPU/I/O/spill cao ngay cả khi chạy một mình; queue có thể là hậu quả. Thêm concurrency capacity giúp eligible queued work nếu shared dependency còn headroom; không sửa bad scan/join. Query rewrite giảm service demand và có thể giảm cả queue gián tiếp. Dùng controlled A/B: capacity/admission change với same query, rồi query rewrite với same capacity."),
            ("Isolation và priority", "Tách interactive, ETL, ad-hoc và maintenance vào queues/resource groups/warehouses giảm head-of-line blocking và cho SLO khác nhau. Isolation cứng tăng idle capacity/cache duplication; isolation mềm có noisy-neighbor risk. Priority không tạo resource; nó đổi thứ tự/weight và có starvation risk. Short-query acceleration có classification error. Báo per-class arrival, queue, execution, completion, rejection, resource share và SLO attainment; global average có thể đẹp trong khi một class đói."),
            ("Concurrency scaling", "Một số services route eligible queries sang extra clusters/capacity khi queue hình thành. Điều này giảm queue cho supported work nhưng có startup, limits, eligibility và incremental cost. Query có transaction/temp object/UDF hoặc operation unsupported có thể ở lại main path tùy product. Capture compute_type/cluster, queue before/after, execution, extra capacity time và cost. Không gọi autoscaling thành query tuning; nó phân bổ thêm service capacity."),
            ("Cache làm sai load test", "Result cache có thể trả identical query mà không thực thi; data cache giảm remote I/O; plan cache giảm compilation. Repeating exact SQL làm hit ratio không đại diện dashboard parameter distribution. Với performance execution test, disable/bypass result cache và verify hit flag; prime hoặc randomize data-cache state theo scenario. Với production capacity test, cache là system behavior hợp lệ nhưng workload trace phải đại diện reuse. Báo cache policy và hit by layer."),
            ("Load model và số đo", "Closed-loop virtual users chờ response rồi gửi request tiếp, nên khi latency tăng offered load tự giảm; open-loop schedule giữ arrival rate và lộ queue overload nhưng cần backpressure an toàn. Dùng ramp hoặc stepped arrival, warm-up, fixed window và stop thresholds. Báo throughput, arrivals, running/queued, queue p50/p95/p99, execution p50/p95/p99, errors/timeouts, spill, CPU/memory/I/O và per-class fairness. Coordinated omission phải được xem xét nếu load generator bỏ qua requests đáng lẽ đến trong pause."),
            ("Hai ca và proof of non-transfer", "Ca Q dùng nhiều short queries để slot limit tạo queue nhưng service time ổn; remediation là admission/concurrency capacity hoặc isolation. Ca H dùng một heavy scan/join gây execution time/spill cao ở low concurrency; remediation là pruning/layout/query plan. Áp nhầm: query rewrite trivial không xóa queue nếu arrival vượt capacity; thêm queue slots có thể làm heavy query tranh memory và chậm hơn. Lab đạt khi tách times ở mọi load step, result cache controlled, fix đúng giảm target metric và wrong fix được chạy/giải thích bằng counters."),
        ),
        (
            "client latency có nhiều clock boundaries",
            "queue time và execution time phải có metric definitions",
            "admission queue có thể bảo vệ throughput và memory",
            "queue tăng không tự chứng minh thiếu total compute",
            "heavy query phải tái hiện ở low concurrency",
            "thêm capacity không sửa scan join hoặc spill root cause",
            "query rewrite có thể giảm queue gián tiếp qua service demand",
            "isolation có idle capacity và cache duplication cost",
            "priority không tạo thêm resource",
            "autoscaling chỉ áp cho eligible work và có cost",
            "result cache hit phải được phát hiện riêng",
            "data cache và result cache có scope khác nhau",
            "closed loop che offered-load overload",
            "global average che per-class starvation",
            "wrong-fix experiment là bằng chứng phân biệt diagnosis",
        ),
    ),
    Lesson(
        215,
        "Lesson_215-the-cost-model-of-an-analytical-engine",
        "Analytical Engine Cost Model",
        "103-analytical-engine-cost-model.md",
        "wiki.olap.analytical-engine-cost-model",
        "Xây cost model workload-weighted cho hai pricing models như thế nào để tìm reversal point, allocation boundary và đòn bẩy giảm chi phí thật?",
        (FD, FU, BQ),
        (FDL, FUL, BQL),
        (
            ("Cost model bắt đầu từ workload", "Inventory query/job families với frequency, bytes processed, slot/credit/compute time, concurrency window, cache state, storage footprint/retention, output/egress và SLO. Ba query đại diện chỉ hợp lệ khi có weight từ trace hoặc scenario được ghi rõ. Tính theo period: daily/monthly workload volume, không so một query lẻ. Correctness và latency SLO là constraints; phương án rẻ nhưng không đạt output/SLO không nằm trên feasible frontier."),
            ("Năm thành phần cần unit", "Scan/analysis cost: billed bytes hoặc service-specific processed units. Compute time: runtime × metered rate khi serverless/job model. Provisioned/capacity: allocated units × billed duration dù idle, có minimum/granularity/commitment. Storage: logical/physical/active/long-term bytes × retention. Transfer/egress: source-destination-region path × bytes. Operator TCO thêm engineering/on-call/governance/support; không trộn vào invoice subtotal nhưng phải hiện trong decision total. Mọi term ghi currency, region, date, tax/discount scope."),
            ("Hai pricing archetypes", "On-demand scan model gần `sum(query_frequency × billed_bytes × rate)` với minimum/free-tier/cache exceptions. Capacity model gần `allocated_units × billable_time × rate`, có utilization và commitments. Credit/warehouse model cũng capacity-time nhưng unit conversion, auto-suspend minimum và multi-cluster khác. Một engine có thể kết hợp storage, compute, serverless features và transfer. Model là piecewise function, không phải đơn giá nhân một metric duy nhất."),
            ("Reversal point", "Gọi workload volume `x`. Nếu A có fixed baseline `F_A` và marginal `v_A`, B có `F_B`, `v_B`, equality ở `(F_B-F_A)/(v_A-v_B)` khi denominator khác zero và trong valid pricing segment. Thực tế rates tiered, commitments và concurrency làm nhiều breakpoints; solve từng interval hoặc scenario grid. Sensitivity thay frequency, bytes/query, concurrency, utilization, cache hit và egress. Reversal point là decision boundary, không dự báo nếu inputs không có uncertainty ranges."),
            ("Allocation và shared capacity", "Invoice capacity dùng chung không có natural per-query cost. Allocation có thể theo slot-ms/credit, execution time weighted by size, bytes, reservation/project labels hoặc policy; mỗi cách tạo incentive khác. Idle and shared service cost cần rule: direct, proportional, even, committed owner hoặc unallocated platform. Tách measured usage khỏi allocated cost. Sum allocated phải reconcile invoice within tolerance; nếu không, unit economics không đáng tin."),
            ("Ba đòn bẩy nhưng không có thứ tự phổ quát", "Giảm scanned bytes bằng projection, pruning, clustering/materialization thường giảm on-demand scan cost; trong fixed capacity nó chỉ tạo headroom trừ khi capacity/commitment giảm hoặc workload tăng. Query rewrite giảm compute/service time nhưng có engineering/maintenance cost. Right-size/schedule/auto-suspend giảm allocated idle time nhưng cold-start/cache effects có thể tăng latency/remote bytes. Roadmap nêu thứ tự scan→compute→cluster là heuristic lab, không định luật. Chọn theo marginal cost driver đã đo."),
            ("Guardrails và anomaly control", "Dry-run/estimates, maximum bytes billed, resource monitors, quotas, budgets, alerts và approval gates giảm blast radius; chúng không thay correctness/performance tests. Alert theo absolute spend, rate-of-change và unit cost; failed/retried work phải tính. Hard stop có thể phá pipeline/SLO, nên có exception owner và recovery. Rate card snapshot/versioned, FX/tax/discount/contract sensitivity visible. Không nhúng giá hiện tại vào knowledge invariant."),
            ("Lab cost ledger", "Tạo ledger rows cho three query families × frequency × two pricing models. Pull actual billed bytes, slot/credit/compute time, storage and transfer from telemetry/billing export; operator time là scenario có owner. Reconcile model subtotal với provider export trên sample window. Sweep volume/concurrency/storage/egress để tìm ranking reversal. Apply three interventions one at a time; keep result hash and SLO, calculate absolute and unit-cost delta plus confidence/assumptions. Done khi five terms present, allocation reconciles, reversal is reproducible and no saving is double-counted."),
        ),
        (
            "workload weights cần trace hoặc explicit scenario",
            "cheap option must still satisfy correctness and SLO",
            "scan compute capacity storage transfer phải có unit riêng",
            "invoice subtotal khác fully loaded TCO",
            "operator time cần explicit scope và owner",
            "pricing function thường piecewise không tuyến tính toàn miền",
            "on demand bytes và capacity time có fixed marginal structure khác",
            "reversal point cần valid interval và sensitivity ranges",
            "shared capacity allocation là policy không phải source fact",
            "allocated costs phải reconcile provider invoice",
            "bytes saved không luôn tạo invoice saving dưới fixed commitment",
            "right sizing có thể đổi cold start và cache behavior",
            "guardrail không thay performance correctness test",
            "failed retries và idle capacity vẫn là cost",
            "rate card phải versioned theo date region contract currency",
        ),
    ),
)


VERIFY = {
    211: "Khóa fixed snapshot/query/config; chạy 1, 2, 4, 8 workers, lưu stage/task counters, node-seconds và output hash; thêm weak-scaling series riêng.",
    212: "Chạy broadcast/partitioned, uniform/hot-key và no-spill/spill fixtures; lưu plan, actual rows/bytes, memory, task distribution, spill I/O và result hash.",
    213: "Định nghĩa result/data/metadata cache states; chạy interleaved cold/warm/result-cache/resize cells, lưu remote/local bytes, provisioning, planning và output hash.",
    214: "Dùng controlled stepped load; tách queue/planning/execution/fetch, cache-hit flag, running/queued, per-class tails, errors, spill và throughput; chạy đúng-fix/sai-fix A/B.",
    215: "Dựng versioned rate-card plus workload ledger; reconcile telemetry/billing, sweep scenario variables, solve breakpoints và kiểm result/SLO không đổi sau mỗi optimization.",
}

QUERIES = {
    211: ["Strong scaling khác weak scaling trong MPP thế nào?", "Vì sao cluster speedup không chứng minh SIMD?", "Cách quy strong-scaling ceiling về đúng tầng là gì?"],
    212: ["Broadcast join cần fit memory ở boundary nào?", "Phân biệt skew với spill bằng counter nào?", "Vì sao tăng memory không sửa hot-key skew?"],
    213: ["Cold cache phải được định nghĩa theo những layer nào?", "Shared data có phải mọi read đều qua network không?", "Benchmark shared-nothing và separated compute thế nào cho công bằng?"],
    214: ["Tách queue time và execution time để chọn remediation thế nào?", "Result cache làm sai concurrency test ra sao?", "Cách chứng minh wrong fix không chữa đúng bottleneck là gì?"],
    215: ["Tính reversal point giữa scan pricing và capacity pricing thế nào?", "Vì sao bytes saved chưa chắc giảm invoice?", "Allocation shared capacity cần reconcile ra sao?"],
}

NEW_SOURCES = (
    {"source_id": AM, "record_path": "1_Nguon/Papers/SRC-AMDAHL-1967.md", "canonical_url": "https://doi.org/10.1145/1465482.1465560", "captured": "2026-10-01", "rights": "ACM-paper-classroom-use"},
    {"source_id": GU, "record_path": "1_Nguon/Papers/SRC-GUSTAFSON-1988.md", "canonical_url": "https://doi.org/10.1145/42411.42415", "captured": "2026-10-01", "rights": "ACM-research-paper"},
    {"source_id": SF, "record_path": "1_Nguon/Papers/SRC-SNOWFLAKE-ELASTIC-DATA-WAREHOUSE.md", "canonical_url": "https://www.cs.cmu.edu/~15721-f24/papers/Snowflake.pdf", "captured": "2026-10-01", "rights": "author-public-paper-classroom-use"},
    {"source_id": TJ, "record_path": "1_Nguon/Web/SRC-TRINO-JOIN-DISTRIBUTION.md", "canonical_url": "https://trino.io/docs/current/optimizer/cost-based-optimizations.html", "captured": "2026-10-01", "rights": "public-project-documentation"},
    {"source_id": TS, "record_path": "1_Nguon/Web/SRC-TRINO-SPILL.md", "canonical_url": "https://trino.io/docs/current/admin/spill.html", "captured": "2026-10-01", "rights": "public-project-documentation"},
    {"source_id": RW, "record_path": "1_Nguon/Web/SRC-REDSHIFT-WLM-QUERY-METRICS.md", "canonical_url": "https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html", "captured": "2026-10-01", "rights": "public-vendor-documentation"},
    {"source_id": RC, "record_path": "1_Nguon/Web/SRC-REDSHIFT-CONCURRENCY-SCALING.md", "canonical_url": "https://docs.aws.amazon.com/redshift/latest/dg/concurrency-scaling.html", "captured": "2026-10-01", "rights": "public-vendor-documentation"},
    {"source_id": FD, "record_path": "1_Nguon/Web/SRC-FINOPS-DATA-CLOUD-PLATFORMS.md", "canonical_url": "https://www.finops.org/framework/technology-categories/data-cloud-platforms/", "captured": "2026-10-01", "rights": "public-framework-content"},
    {"source_id": BQ, "record_path": "1_Nguon/Web/SRC-BIGQUERY-PRICING-SLOTS.md", "canonical_url": "https://cloud.google.com/bigquery/pricing", "captured": "2026-10-01", "rights": "public-vendor-documentation"},
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
tags: [wiki/database-systems, olap, distributed-query, performance, cost]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/{lesson.filename}
---
"""


def deep_note(lesson: Lesson) -> str:
    parts = [frontmatter(lesson), f"# {lesson.title}\n\n> [!abstract] Câu hỏi trung tâm\n> {lesson.question}\n"]
    for index, (heading, body) in enumerate(lesson.core, 1):
        parts.append(f"\n## {index}. {heading}\n\n{body}\n")
    parts.append("\n## 9. Ma trận kiểm chứng từng mệnh đề\n\nMỗi mệnh đề về latency, scaling, cache, concurrency hoặc cost cần counterfactual, correctness oracle và counter ở đúng boundary. Tên kiến trúc, plan label, elapsed time hoặc rate card riêng lẻ chưa đủ để quy nguyên nhân.\n")
    for index, probe in enumerate(lesson.probes, 1):
        parts.append(
            f"\n### 9.{index}. {probe}\n\n"
            f"**Mệnh đề cần kiểm.** {probe}.\n\n"
            f"**Cách kiểm.** {VERIFY[lesson.number]} Ghi engine/version, workload shape, controlled variables, expected counter, failure signal và reversal condition.\n\n"
            "**Bằng chứng đạt.** Lưu source/query/config hashes, plans/profiles, raw counters, result oracle, repetitions, units và reviewer. Khi lab chưa chạy, chỉ giữ protocol và expected observations; không viết chúng như kết quả thực nghiệm.\n"
        )
    parts.append(
        """
## 10. Quy trình phản biện

1. Viết câu hỏi đo lường và decision cần hỗ trợ trước khi chọn metric.
2. Khóa query semantics, snapshot, output oracle và unit của mọi số.
3. Vẽ boundaries: client, queue, planner, source, worker, exchange, cache, spill và billing.
4. Thay một cơ chế; ghi mọi thay đổi algorithm/config do engine tự thực hiện.
5. Dùng distribution và critical path; không để average che tails hoặc skew.
6. Viết counterexample, reversal condition và stop threshold trước khi chạy.
7. Tách estimate, configured intent, runtime observation và invoice fact.
8. Nếu không kiểm soát được cache, resource hoặc rate contract, ghi giới hạn thay vì kết luận nhân quả.

## 11. Câu hỏi tự kiểm tra

1. Mệnh đề đang nằm ở tầng kiến trúc, scheduler, operator, hardware hay billing?
2. Counter nào quan sát trực tiếp cơ chế đó và proxy nào dễ gây nhầm?
3. Correctness/SLO nào phải giữ trước khi gọi một phương án tốt hơn?
4. Cache, concurrency, statistics, data shape hay rate card nào có thể đảo kết luận?
5. Intervention nào bác bỏ diagnosis hiện tại?
6. Kết luận nào mới là protocol, chưa phải observation?

## 12. Giới hạn và điều chưa cho phép kết luận

- Chưa chạy cluster scaling, join/spill, cache, concurrency hoặc billing reconciliation lab; note mô tả protocol và evidence contract.
- Tài liệu sản phẩm được kiểm ngày 2026-10-01; field, feature, pricing và behavior có thể đổi theo version, region và contract.
- Amdahl, Gustafson, workload matrices và cost equations là mô hình; chúng không thay runtime counters hay invoice export.
- Không suy vendor superiority từ paper hoặc một benchmark; workload, correctness, SLO, operation và price contract phải cùng phạm vi.
- Note giữ trạng thái `review` cho tới khi chủ dự án duyệt semantic meaning.
"""
    )
    references = "\n".join(f"{index}. [[{link}]]" for index, link in enumerate(lesson.source_links, 1))
    coverage = "\n".join(
        f"| [[{link}]] | Khái niệm, mechanism hoặc evidence boundary liên quan | Đã đọc locator trong source record; không suy ngoài phạm vi |"
        for link in lesson.source_links
    )
    takeaways = {
        211: "Strong scaling, weak scaling, MIMD/SPMD, batch và SIMD phải được đo ở các boundary riêng rồi mới nối causal chain.",
        212: "Broadcast, repartition, skew và spill có thể xuất hiện cùng lúc; diagnosis cần timeline và task-level counters.",
        213: "So kiến trúc chỉ hợp lệ khi result, data, metadata cache và provisioning state có operational definition.",
        214: "Queue time và execution time dẫn tới interventions khác nhau; wrong-fix experiment giúp chứng minh diagnosis.",
        215: "Cost comparison là workload-weighted piecewise model có allocation, reconciliation và reversal point, không phải so đơn giá.",
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
- Estimate và configured intent phải được tách khỏi runtime observation và invoice fact.
- Correctness oracle, units, cache state, workload shape và controlled variables đi trước performance/cost claim.
- Average phải đi cùng distributions, tails, critical path và per-class hoặc per-task counters.
- Chưa chạy lab thì artifact là giáo trình đã kiểm cấu trúc, chưa phải benchmark hay production certification.
"""
    )
    return "".join(parts)


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
    data["version"] = "1.0.42"
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
        note, after = previous.curriculum(lesson, knowledge)
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
