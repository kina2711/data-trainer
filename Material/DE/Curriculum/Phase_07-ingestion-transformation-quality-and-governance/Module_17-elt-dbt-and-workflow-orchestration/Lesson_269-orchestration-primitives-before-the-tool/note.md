# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 269: Orchestration Primitives Before the Tool

## Mục tiêu bài học

**Năng lực cần chứng minh.** Phân biệt phụ thuộc dữ liệu với thứ tự chạy trong một đồ thị cho trước và thay giả định thời gian bằng tín hiệu.

**Điều kiện hoàn thành.** Phân đúng ≥ 6/8 cạnh, mức song song tăng thêm được đo, và mọi giả định thời gian được thay bằng tín hiệu dữ liệu.

> [!abstract] Câu hỏi trung tâm
> Những primitives nào phải được định nghĩa trước khi chọn orchestrator để retries, dependencies, state và backfill không bị giao phó cho UI mặc định?

## 1. Unit of work và identity

Task là bounded operation với explicit input/output, idempotency identity, timeout và owner. Run instance gắn logical data interval/input version, không chỉ start timestamp. Workflow graph nêu true data/control dependencies; thứ tự tiện mắt không thành edge. Asset/dataset trigger và time schedule khác semantics. Operator implementation không được giấu grain/checkpoint contract.

## 2. State machine

Task/run states gồm queued/running/success/failed/skipped/upstream-failed/retrying and platform-specific states. Define which are terminal, which permit publish, and how leaf/trigger rules affect workflow success. Airflow warns leaf with permissive trigger rule can make DagRun success despite middle failure; publication gate must depend on critical invariants, not last box color. Persist external publication/checkpoint state outside scheduler metadata where necessary.

## 3. Retries timeouts concurrency

Retry only classified transient failures, with bounded attempts/backoff/jitter/deadline; operation must absorb replay. Timeout and heartbeat detect hung work but kill can occur after external commit. Pools/quotas/concurrency protect source and destination; priority and backfill isolation prevent starvation. Nested retries share budget. A scheduler retry setting cannot create idempotency in API/database side effects.

## 4. Dependency sensors events

Polling sensor needs interval, timeout and definitive readiness oracle; file existence alone may precede completeness. Event/asset trigger needs identity, dedup, replay and missed-event reconciliation. Cross-workflow dependency should pass versioned artifact/interval, not infer latest. Dynamic mapping controls cardinality and partial failure. XCom/message metadata is not bulk data channel or durable data catalog.

## 5. Backfill catchup recovery

Backfill creates runs for historical intervals with controlled ordering/concurrency and code/source-version policy. Catchup semantics derive schedules/intervals, not arbitrary loop dates. Recovery chooses clear/retry, rerun interval, resume checkpoint or rebuild candidate. Manual marking success without artifact evidence creates false history. Runbook includes scheduler DB loss, duplicate trigger, partial publish and stale sensor.

## 6. Tool evaluation

Score ability to express these primitives, inspect state, isolate queues, version deployments, retain lineage/logs, test DAGs, recover and integrate secrets/access. Proof-of-concept injects task crash after commit, missing event, long queue, backfill overlap and branch skip. Compare operational burden and exit path. Choose tool after semantics; otherwise defaults become accidental architecture.

## 7. Ma trận kiểm chứng từng mệnh đề

Trong `Orchestration Primitives Before the Tool`, mỗi claim phải nối được tới input boundary, compiled hoặc executed artifact, trạng thái trước–sau, failure signal và independent oracle. Một command kết thúc với exit code 0 không tự chứng minh dữ liệu đúng, đầy đủ hoặc phù hợp với consumer contract. Protocol nền của bài này: Dựng artifact/workflow fixture có exact versions và intervals; inject one failure or changed assumption; capture resolved graph/state/query IDs or scheduler context and compare with independent coverage oracle.

### 7.1. Orchestration probe 1: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ

**Mệnh đề cần kiểm.** Orchestration probe 1: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ.

**Thiết kế phép thử.** Với `Orchestration probe 1: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ`, Bắt đầu bằng ca nhỏ nhất có thể làm mệnh đề sai; chỉ thêm dữ liệu sau khi failure signal đã xuất hiện đúng chỗ. Cách này phân biệt một assertion có lực với một bài demo chỉ đi qua happy path. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Orchestration probe 1: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ` phải cho thấy: Giữ fixture tối thiểu, raw failure rows và câu lệnh tái hiện; ảnh chụp màn hình một trạng thái xanh không đủ. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.2. Orchestration probe 2: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ

**Mệnh đề cần kiểm.** Orchestration probe 2: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ.

**Thiết kế phép thử.** Với `Orchestration probe 2: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ`, Giữ nguyên input rồi đổi đúng một tham số cấu hình liên quan. Nếu output đổi theo nhiều hướng cùng lúc, phép thử chưa cô lập được nguyên nhân và phải thu hẹp lại. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Orchestration probe 2: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ` phải cho thấy: Báo cả giá trị trước–sau của tham số, compiled artifact và diff đầu ra để reviewer thấy biến nào thực sự đổi. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.3. Orchestration probe 3: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ

**Mệnh đề cần kiểm.** Orchestration probe 3: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ.

**Thiết kế phép thử.** Với `Orchestration probe 3: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ`, Chạy cặp đối chứng: một input phải được chấp nhận và một input chỉ lệch tại boundary phải bị chặn hoặc được phân loại. Hai ca dùng chung code path để tránh so hai hệ thống khác nhau. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Orchestration probe 3: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ` phải cho thấy: Pass khi positive control đi qua, negative control dừng đúng lớp và không có side effect ngoài scope. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.4. Orchestration probe 4: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ

**Mệnh đề cần kiểm.** Orchestration probe 4: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ.

**Thiết kế phép thử.** Với `Orchestration probe 4: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ`, Đặt kill point ngay trước và ngay sau durable boundary. So trạng thái sau restart để biết hệ thống tạo replay có kiểm soát, silent gap hay một trạng thái nửa vời mà dashboard không báo. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Orchestration probe 4: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ` phải cho thấy: Run ledger phải cho biết commit/checkpoint nào bền vững; sau rerun, key set và side-effect ledger cùng hội tụ. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.5. Orchestration probe 5: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ

**Mệnh đề cần kiểm.** Orchestration probe 5: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ.

**Thiết kế phép thử.** Với `Orchestration probe 5: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ`, Đảo thứ tự input và thay concurrency nhưng giữ logical population. Kết quả khác nhau cho thấy thiết kế đang phụ thuộc physical order hoặc race thay vì contract đã công bố. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Orchestration probe 5: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ` phải cho thấy: Hash chuẩn hóa và business totals phải giống nhau giữa các thứ tự; chênh lệch được giữ như finding, không làm tròn mất. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.6. Orchestration probe 6: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ

**Mệnh đề cần kiểm.** Orchestration probe 6: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ.

**Thiết kế phép thử.** Với `Orchestration probe 6: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ`, Cho cùng logical identity xuất hiện hai lần: trước hết cùng payload, sau đó payload khác. Trường hợp đầu phải hội tụ; trường hợp sau phải lộ collision thay vì âm thầm chọn một bản. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Orchestration probe 6: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ` phải cho thấy: Same-content replay được đếm nhưng không nhân state; different-content collision có reason code và đường xử lý riêng. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.7. Orchestration probe 7: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ

**Mệnh đề cần kiểm.** Orchestration probe 7: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ.

**Thiết kế phép thử.** Với `Orchestration probe 7: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ`, Mở rộng fixture bằng một record tới trễ ngay trong horizon và một record nằm ngoài horizon. Ghi rõ record nào được sửa, record nào bị loại và metric nào khiến operator biết có mất coverage. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Orchestration probe 7: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ` phải cho thấy: Evidence ghi accepted-late, rejected-late và oldest outstanding timestamp; thiếu một nhóm được báo là coverage gap. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.8. Orchestration probe 8: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ

**Mệnh đề cần kiểm.** Orchestration probe 8: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ.

**Thiết kế phép thử.** Với `Orchestration probe 8: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ`, Dùng một schema change tương thích và một thay đổi phá vỡ key, type hoặc meaning. Kết quả phải chỉ ra khác biệt giữa parse được, chạy được và vẫn giữ đúng semantics. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Orchestration probe 8: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ` phải cho thấy: Lưu schema trước–sau, classification, compiled SQL và target state; một migration chạy xong nhưng đổi meaning vẫn fail. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.9. Orchestration probe 9: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ

**Mệnh đề cần kiểm.** Orchestration probe 9: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ.

**Thiết kế phép thử.** Với `Orchestration probe 9: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ`, Tạo bảng rỗng, bảng một row và bảng có duplicate bù cho missing row. Đây là ba ca dễ làm count hoặc aggregate xanh dù invariant thực tế đã hỏng. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Orchestration probe 9: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ` phải cho thấy: Oracle so count, key multiset và typed hashes. Ca missing-plus-duplicate phải bị phát hiện dù tổng row count không đổi. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.10. Orchestration probe 10: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ

**Mệnh đề cần kiểm.** Orchestration probe 10: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ.

**Thiết kế phép thử.** Với `Orchestration probe 10: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ`, Cho reviewer chỉ artifacts, không cho xem lời giải thích của tác giả. Nếu họ không dựng lại được input, decision và diff thì evidence package chưa đủ để bàn giao. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Orchestration probe 10: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ` phải cho thấy: Artifact package đạt khi reviewer tái hiện đúng diff và chỉ ra được limitation mà không cần hỏi tác giả về state ẩn. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.11. Orchestration probe 11: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ

**Mệnh đề cần kiểm.** Orchestration probe 11: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ.

**Thiết kế phép thử.** Với `Orchestration probe 11: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ`, So output với một cách tính độc lập không tái sử dụng macro, filter hoặc intermediate relation đang được kiểm. Hai phép tính dùng chung lỗi chỉ tạo sự đồng thuận giả. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Orchestration probe 11: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ` phải cho thấy: Independent result phải khớp ở key/grain đã định; nếu chỉ khớp aggregate cao hơn thì drill-down chưa hoàn tất. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.12. Orchestration probe 12: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ

**Mệnh đề cần kiểm.** Orchestration probe 12: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ.

**Thiết kế phép thử.** Với `Orchestration probe 12: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ`, Thử trên hai scope: selection hẹp dùng trong CI và population đầy đủ dùng khi phát hành. Ghi phần coverage bị bỏ qua; tốc độ của CI không được biến thành tuyên bố kiểm toàn bộ dữ liệu. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Orchestration probe 12: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ` phải cho thấy: Kết quả nêu numerator, denominator và excluded nodes/partitions; không dùng từ `all` khi selection không phủ toàn graph. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.13. Orchestration probe 13: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ

**Mệnh đề cần kiểm.** Orchestration probe 13: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ.

**Thiết kế phép thử.** Với `Orchestration probe 13: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ`, Đẩy một giá trị tới sát giới hạn precision, timezone, partition hoặc threshold. Boundary phải được viết half-open hay inclusive rõ ràng, không suy từ một ví dụ ở giữa khoảng. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Orchestration probe 13: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ` phải cho thấy: Hai phía của boundary đều có expected result và raw observation. Sai đúng một đơn vị phải làm test fail có chẩn đoán. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.14. Orchestration probe 14: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ

**Mệnh đề cần kiểm.** Orchestration probe 14: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ.

**Thiết kế phép thử.** Với `Orchestration probe 14: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ`, Thay constraint quan trọng nhất bằng giá trị đủ để decision phải đảo. Nếu thiết kế vẫn đưa cùng lựa chọn mà không giải thích, decision rule đang là khẩu hiệu chứ chưa phải rule. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Orchestration probe 14: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ` phải cho thấy: ADR hoặc rule chỉ pass khi changed constraint tạo lựa chọn mới đúng như đã dự báo và reversal threshold được lưu. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.15. Orchestration probe 15: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ

**Mệnh đề cần kiểm.** Orchestration probe 15: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ.

**Thiết kế phép thử.** Với `Orchestration probe 15: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ`, Lặp lại phép thử từ môi trường sạch bằng seed và versions đã lưu. Một kết quả chỉ tái hiện được trên workspace của tác giả không đủ làm release evidence. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Orchestration probe 15: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ` phải cho thấy: Lần chạy sạch phải tạo cùng canonical state; khác biệt do timestamp, file order hoặc generated IDs phải được loại hoặc giải thích. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

## 8. Quy trình phản biện

Áp dụng sáu bước sau cho `Orchestration Primitives Before the Tool`; nếu một bước không phù hợp, ghi lý do thay vì bỏ qua im lặng.

1. Với `wiki.orchestration.primitives-before-tool`, chốt grain, identity, time boundary và consumer-visible invariant trước câu lệnh.
2. Tách parse/compile state, warehouse execution và publication state.
3. Pin dbt core, adapter, warehouse hoặc orchestrator version cùng configuration có ảnh hưởng.
4. Kiểm correctness bằng key set, typed hash và business invariant trước performance.
5. Chạy negative case, kill point hoặc changed assumption; green path đơn lẻ không đủ.
6. Phân loại source fact, project convention, curriculum synthesis và untested hypothesis.

## 9. Câu hỏi tự kiểm tra

1. `Orchestration probe 1: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ` sẽ thất bại trước tiên ở boundary nào?
2. Với `Orchestration probe 2: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ`, artifact nào là nguồn bằng chứng mạnh nhất?
3. Counterexample nhỏ nhất cho `Orchestration probe 3: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ` gồm những row hoặc state nào?
4. `Orchestration probe 4: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ` có thể xanh giả trong tình huống nào?
5. Version, adapter, timezone hoặc state nào làm `Orchestration probe 5: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ` đổi nghĩa?
6. Phần nào của `Orchestration probe 6: work identity, state transition, retry/timeout, dependency evidence và recovery phải rõ` hiện mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `Orchestration Primitives Before the Tool` chưa chạy trên warehouse, dbt project hoặc orchestrator production; các mục kiểm chứng vẫn là protocol và expected evidence.
- Các claim gắn `wiki.orchestration.primitives-before-tool` phải kiểm lại theo dbt core, adapter, warehouse và scheduler version được chọn.
- Decision matrix, failure campaign và ngưỡng review là curriculum synthesis, không phải cam kết của vendor.
- Note giữ trạng thái `review` cho tới khi chủ dự án duyệt semantic meaning và learner artifact.

## Reference
1. [[SRC-APACHE-AIRFLOW-DAG-RUNS]]
2. [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]]
3. [[SRC-KLEPPMANN-DDIA-1E]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-APACHE-AIRFLOW-DAG-RUNS]] | Cơ chế, contract hoặc giới hạn liên quan | Đã đọc locator; claim theo version/configuration |
| [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]] | Cơ chế, contract hoặc giới hạn liên quan | Đã đọc locator; claim theo version/configuration |
| [[SRC-KLEPPMANN-DDIA-1E]] | Cơ chế, contract hoặc giới hạn liên quan | Đã đọc locator; claim theo version/configuration |

## Key takeaways
- Orchestrator thực thi primitives đã định nghĩa; retry, UI và DAG không tự tạo idempotency, completeness hoặc recoverability.
- Với `Orchestration Primitives Before the Tool`, compiled intent và observed state phải được lưu tách biệt; trộn hai lớp sẽ che failure window.
- Oracle của bài phải bám câu hỏi trung tâm: Những primitives nào phải được định nghĩa trước khi chọn orchestrator để retries, dependencies, state và backfill không bị giao phó cho UI mặc định?
- Các source IDs `src.web.apache-airflow-dag-runs, src.book.reis-housley-fundamentals-data-engineering, src.book.kleppmann-ddia.1e` đặt ranh giới cho claim; phần synthesis không được gán nguyên văn cho vendor.
- Trước khi lab chạy, note này là giáo trình đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.
