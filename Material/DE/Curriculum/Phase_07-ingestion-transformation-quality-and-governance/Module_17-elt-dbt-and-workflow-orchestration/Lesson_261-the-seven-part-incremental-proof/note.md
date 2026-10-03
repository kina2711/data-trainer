# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 261: The Seven Part Incremental Proof

## Mục tiêu bài học

**Năng lực cần chứng minh.** Viết chứng minh bảy phần cho ba mô hình tăng dần, mỗi phần kèm một phép kiểm chạy được.

**Điều kiện hoàn thành.** Ba mô hình có đủ bảy phần, mỗi phần dẫn tới một phép kiểm tự động, và rà soát chéo không tìm thấy giả định chưa kiểm.

> [!abstract] Câu hỏi trung tâm
> Bảy phần bằng chứng nào đủ để bảo vệ claim rằng incremental model hội tụ với full recomputation trong phạm vi đã công bố?

## 1. 1. Grain và identity

Viết một row output đại diện điều gì, key nào ổn định và NULL/duplicate được xử lý ra sao. Unique key trong config chỉ là input cho materialization; nó không chứng minh source slice unique. Proof có fixture làm key đổi, key trùng và same key different version. Nếu model chứa history, identity phải gồm valid-time/version thay vì entity key đơn. Không chốt grain thì mọi kiểm row count, merge và delete phía sau đều không có nghĩa.

## 2. 2. Change capture boundary

Nêu field hoặc log position chọn changed population, ordering/tie rule, timezone, precision, lookback và retention. Chứng minh every relevant insert/update/delete xuất hiện hoặc liệt kê operation ngoài scope. `max(updated_at)` trên target không phải boundary nếu output timestamp bị transform. Source snapshot/interval và checkpoint được lưu typed, cùng schema/config version. Ca same timestamp ở boundary phải được replay hoặc tie-break deterministically.

## 3. 3. Affected-state closure

Một changed row có thể làm thay đổi nhiều output rows qua joins, windows, aggregates hoặc dedup. Xác định closure từ changed inputs tới toàn bộ keys/partitions cần recompute. Với lifetime metric, closure có thể là customer chứ không phải order. Với rank/window, peer partition cần mở rộng. Proof dùng dependency examples để cho thấy filter sớm vẫn giữ đủ context, hoặc chọn partition rebuild khi delta algebra quá khó bảo vệ.

## 4. 4. Mutation semantics

Lập bảng insert, in-place update, backdated correction, hard/soft delete, restore, duplicate delivery và schema/logic change. Mỗi mutation map tới append, update, invalidate, partition replace hoặc full refresh. Absence trong một incremental slice không phải delete. Logic change thường không phát event ở source nên cần migration/backfill decision riêng. Không được gọi model correct khi chỉ chứng minh append-only case trong khi source mutable.

## 5. 5. Determinism và idempotency

Stable key, total ordering, canonical timezone/decimal/null và deterministic functions làm cùng logical input tạo cùng accepted state. Kill trước/sau merge, publication và checkpoint; rerun phải hội tụ. Audit/notification/hook cũng có operation identity. Nếu warehouse files hoặc timestamps khác nhưng consumer-visible rows tương đương, proof nêu observation boundary thay vì đòi byte identity không cần thiết.

## 6. 6. Full-equivalence oracle

Tại fixed source boundary, build full result từ clean target rồi chạy incremental history dẫn tới cùng boundary. So schema, key set, typed row hash, delete/current-history state và business aggregates. Oracle không tái sử dụng incremental filter đang kiểm. Chạy nhiều mutation sequences và input orders. Mismatch được phân loại, không làm tròn hoặc bỏ qua bằng aggregate cao hơn. Periodic production reconciliation dùng cùng logic nhưng có cost/coverage statement.

## 7. 7. Operability và reversal

Proof kết thúc bằng metrics: scanned input/target, affected rows, lateness beyond horizon, duplicate/collision, reconciliation residual, runtime/cost và full-refresh duration. Runbook nêu bootstrap, schema drift, checkpoint repair, backfill, rollback và when-to-full-refresh. Reversal trigger rõ: change fraction, mutation type, late horizon hoặc maintenance burden vượt threshold. Không có recovery owner thì design mới chỉ chạy được, chưa vận hành được.

## 7. Ma trận kiểm chứng từng mệnh đề

Trong `The Seven Part Incremental Proof`, mỗi claim phải nối được tới input boundary, compiled hoặc executed artifact, trạng thái trước–sau, failure signal và independent oracle. Một command kết thúc với exit code 0 không tự chứng minh dữ liệu đúng, đầy đủ hoặc phù hợp với consumer contract. Protocol nền của bài này: Dùng project/fixture nhỏ có exact boundary và owner; capture source, compiled/runtime artifacts, relations và consumer-facing diff; đối soát bằng alternate computation hoặc inventory độc lập.

### 7.1. Incremental-proof probe 1: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ

**Mệnh đề cần kiểm.** Incremental-proof probe 1: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ.

**Thiết kế phép thử.** Với `Incremental-proof probe 1: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ`, Bắt đầu bằng ca nhỏ nhất có thể làm mệnh đề sai; chỉ thêm dữ liệu sau khi failure signal đã xuất hiện đúng chỗ. Cách này phân biệt một assertion có lực với một bài demo chỉ đi qua happy path. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Incremental-proof probe 1: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ` phải cho thấy: Giữ fixture tối thiểu, raw failure rows và câu lệnh tái hiện; ảnh chụp màn hình một trạng thái xanh không đủ. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.2. Incremental-proof probe 2: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ

**Mệnh đề cần kiểm.** Incremental-proof probe 2: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ.

**Thiết kế phép thử.** Với `Incremental-proof probe 2: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ`, Giữ nguyên input rồi đổi đúng một tham số cấu hình liên quan. Nếu output đổi theo nhiều hướng cùng lúc, phép thử chưa cô lập được nguyên nhân và phải thu hẹp lại. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Incremental-proof probe 2: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ` phải cho thấy: Báo cả giá trị trước–sau của tham số, compiled artifact và diff đầu ra để reviewer thấy biến nào thực sự đổi. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.3. Incremental-proof probe 3: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ

**Mệnh đề cần kiểm.** Incremental-proof probe 3: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ.

**Thiết kế phép thử.** Với `Incremental-proof probe 3: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ`, Chạy cặp đối chứng: một input phải được chấp nhận và một input chỉ lệch tại boundary phải bị chặn hoặc được phân loại. Hai ca dùng chung code path để tránh so hai hệ thống khác nhau. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Incremental-proof probe 3: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ` phải cho thấy: Pass khi positive control đi qua, negative control dừng đúng lớp và không có side effect ngoài scope. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.4. Incremental-proof probe 4: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ

**Mệnh đề cần kiểm.** Incremental-proof probe 4: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ.

**Thiết kế phép thử.** Với `Incremental-proof probe 4: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ`, Đặt kill point ngay trước và ngay sau durable boundary. So trạng thái sau restart để biết hệ thống tạo replay có kiểm soát, silent gap hay một trạng thái nửa vời mà dashboard không báo. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Incremental-proof probe 4: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ` phải cho thấy: Run ledger phải cho biết commit/checkpoint nào bền vững; sau rerun, key set và side-effect ledger cùng hội tụ. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.5. Incremental-proof probe 5: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ

**Mệnh đề cần kiểm.** Incremental-proof probe 5: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ.

**Thiết kế phép thử.** Với `Incremental-proof probe 5: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ`, Đảo thứ tự input và thay concurrency nhưng giữ logical population. Kết quả khác nhau cho thấy thiết kế đang phụ thuộc physical order hoặc race thay vì contract đã công bố. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Incremental-proof probe 5: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ` phải cho thấy: Hash chuẩn hóa và business totals phải giống nhau giữa các thứ tự; chênh lệch được giữ như finding, không làm tròn mất. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.6. Incremental-proof probe 6: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ

**Mệnh đề cần kiểm.** Incremental-proof probe 6: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ.

**Thiết kế phép thử.** Với `Incremental-proof probe 6: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ`, Cho cùng logical identity xuất hiện hai lần: trước hết cùng payload, sau đó payload khác. Trường hợp đầu phải hội tụ; trường hợp sau phải lộ collision thay vì âm thầm chọn một bản. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Incremental-proof probe 6: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ` phải cho thấy: Same-content replay được đếm nhưng không nhân state; different-content collision có reason code và đường xử lý riêng. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.7. Incremental-proof probe 7: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ

**Mệnh đề cần kiểm.** Incremental-proof probe 7: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ.

**Thiết kế phép thử.** Với `Incremental-proof probe 7: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ`, Mở rộng fixture bằng một record tới trễ ngay trong horizon và một record nằm ngoài horizon. Ghi rõ record nào được sửa, record nào bị loại và metric nào khiến operator biết có mất coverage. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Incremental-proof probe 7: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ` phải cho thấy: Evidence ghi accepted-late, rejected-late và oldest outstanding timestamp; thiếu một nhóm được báo là coverage gap. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.8. Incremental-proof probe 8: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ

**Mệnh đề cần kiểm.** Incremental-proof probe 8: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ.

**Thiết kế phép thử.** Với `Incremental-proof probe 8: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ`, Dùng một schema change tương thích và một thay đổi phá vỡ key, type hoặc meaning. Kết quả phải chỉ ra khác biệt giữa parse được, chạy được và vẫn giữ đúng semantics. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Incremental-proof probe 8: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ` phải cho thấy: Lưu schema trước–sau, classification, compiled SQL và target state; một migration chạy xong nhưng đổi meaning vẫn fail. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.9. Incremental-proof probe 9: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ

**Mệnh đề cần kiểm.** Incremental-proof probe 9: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ.

**Thiết kế phép thử.** Với `Incremental-proof probe 9: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ`, Tạo bảng rỗng, bảng một row và bảng có duplicate bù cho missing row. Đây là ba ca dễ làm count hoặc aggregate xanh dù invariant thực tế đã hỏng. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Incremental-proof probe 9: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ` phải cho thấy: Oracle so count, key multiset và typed hashes. Ca missing-plus-duplicate phải bị phát hiện dù tổng row count không đổi. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.10. Incremental-proof probe 10: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ

**Mệnh đề cần kiểm.** Incremental-proof probe 10: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ.

**Thiết kế phép thử.** Với `Incremental-proof probe 10: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ`, Cho reviewer chỉ artifacts, không cho xem lời giải thích của tác giả. Nếu họ không dựng lại được input, decision và diff thì evidence package chưa đủ để bàn giao. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Incremental-proof probe 10: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ` phải cho thấy: Artifact package đạt khi reviewer tái hiện đúng diff và chỉ ra được limitation mà không cần hỏi tác giả về state ẩn. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.11. Incremental-proof probe 11: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ

**Mệnh đề cần kiểm.** Incremental-proof probe 11: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ.

**Thiết kế phép thử.** Với `Incremental-proof probe 11: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ`, So output với một cách tính độc lập không tái sử dụng macro, filter hoặc intermediate relation đang được kiểm. Hai phép tính dùng chung lỗi chỉ tạo sự đồng thuận giả. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Incremental-proof probe 11: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ` phải cho thấy: Independent result phải khớp ở key/grain đã định; nếu chỉ khớp aggregate cao hơn thì drill-down chưa hoàn tất. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.12. Incremental-proof probe 12: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ

**Mệnh đề cần kiểm.** Incremental-proof probe 12: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ.

**Thiết kế phép thử.** Với `Incremental-proof probe 12: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ`, Thử trên hai scope: selection hẹp dùng trong CI và population đầy đủ dùng khi phát hành. Ghi phần coverage bị bỏ qua; tốc độ của CI không được biến thành tuyên bố kiểm toàn bộ dữ liệu. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Incremental-proof probe 12: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ` phải cho thấy: Kết quả nêu numerator, denominator và excluded nodes/partitions; không dùng từ `all` khi selection không phủ toàn graph. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.13. Incremental-proof probe 13: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ

**Mệnh đề cần kiểm.** Incremental-proof probe 13: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ.

**Thiết kế phép thử.** Với `Incremental-proof probe 13: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ`, Đẩy một giá trị tới sát giới hạn precision, timezone, partition hoặc threshold. Boundary phải được viết half-open hay inclusive rõ ràng, không suy từ một ví dụ ở giữa khoảng. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Incremental-proof probe 13: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ` phải cho thấy: Hai phía của boundary đều có expected result và raw observation. Sai đúng một đơn vị phải làm test fail có chẩn đoán. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.14. Incremental-proof probe 14: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ

**Mệnh đề cần kiểm.** Incremental-proof probe 14: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ.

**Thiết kế phép thử.** Với `Incremental-proof probe 14: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ`, Thay constraint quan trọng nhất bằng giá trị đủ để decision phải đảo. Nếu thiết kế vẫn đưa cùng lựa chọn mà không giải thích, decision rule đang là khẩu hiệu chứ chưa phải rule. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Incremental-proof probe 14: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ` phải cho thấy: ADR hoặc rule chỉ pass khi changed constraint tạo lựa chọn mới đúng như đã dự báo và reversal threshold được lưu. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.15. Incremental-proof probe 15: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ

**Mệnh đề cần kiểm.** Incremental-proof probe 15: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ.

**Thiết kế phép thử.** Với `Incremental-proof probe 15: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ`, Lặp lại phép thử từ môi trường sạch bằng seed và versions đã lưu. Một kết quả chỉ tái hiện được trên workspace của tác giả không đủ làm release evidence. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Incremental-proof probe 15: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ` phải cho thấy: Lần chạy sạch phải tạo cùng canonical state; khác biệt do timestamp, file order hoặc generated IDs phải được loại hoặc giải thích. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

## 8. Quy trình phản biện

Áp dụng sáu bước sau cho `The Seven Part Incremental Proof`; nếu một bước không phù hợp, ghi lý do thay vì bỏ qua im lặng.

1. Với `wiki.transformation.seven-part-incremental-proof`, chốt grain, identity, time boundary và consumer-visible invariant trước câu lệnh.
2. Tách parse/compile state, warehouse execution và publication state.
3. Pin dbt core, adapter, warehouse hoặc orchestrator version cùng configuration có ảnh hưởng.
4. Kiểm correctness bằng key set, typed hash và business invariant trước performance.
5. Chạy negative case, kill point hoặc changed assumption; green path đơn lẻ không đủ.
6. Phân loại source fact, project convention, curriculum synthesis và untested hypothesis.

## 9. Câu hỏi tự kiểm tra

1. `Incremental-proof probe 1: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ` sẽ thất bại trước tiên ở boundary nào?
2. Với `Incremental-proof probe 2: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ`, artifact nào là nguồn bằng chứng mạnh nhất?
3. Counterexample nhỏ nhất cho `Incremental-proof probe 3: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ` gồm những row hoặc state nào?
4. `Incremental-proof probe 4: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ` có thể xanh giả trong tình huống nào?
5. Version, adapter, timezone hoặc state nào làm `Incremental-proof probe 5: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ` đổi nghĩa?
6. Phần nào của `Incremental-proof probe 6: phần bằng chứng, counterexample, artifact locator và full-equivalence verdict phải rõ` hiện mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `The Seven Part Incremental Proof` chưa chạy trên warehouse, dbt project hoặc orchestrator production; các mục kiểm chứng vẫn là protocol và expected evidence.
- Các claim gắn `wiki.transformation.seven-part-incremental-proof` phải kiểm lại theo dbt core, adapter, warehouse và scheduler version được chọn.
- Decision matrix, failure campaign và ngưỡng review là curriculum synthesis, không phải cam kết của vendor.
- Note giữ trạng thái `review` cho tới khi chủ dự án duyệt semantic meaning và learner artifact.

## Reference
1. [[SRC-DBT-INCREMENTAL-MODELS]]
2. [[SRC-KLEPPMANN-DDIA-1E]]
3. [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-DBT-INCREMENTAL-MODELS]] | Cơ chế, contract hoặc giới hạn liên quan | Đã đọc locator; claim theo version/configuration |
| [[SRC-KLEPPMANN-DDIA-1E]] | Cơ chế, contract hoặc giới hạn liên quan | Đã đọc locator; claim theo version/configuration |
| [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]] | Cơ chế, contract hoặc giới hạn liên quan | Đã đọc locator; claim theo version/configuration |

## Key takeaways
- Incremental correctness cần đủ grain, boundary, affected-state closure, mutations, determinism, full-equivalence và operability; thiếu một phần thì claim chỉ đúng trên happy path.
- Với `The Seven Part Incremental Proof`, compiled intent và observed state phải được lưu tách biệt; trộn hai lớp sẽ che failure window.
- Oracle của bài phải bám câu hỏi trung tâm: Bảy phần bằng chứng nào đủ để bảo vệ claim rằng incremental model hội tụ với full recomputation trong phạm vi đã công bố?
- Các source IDs `src.web.dbt-incremental-models, src.book.kleppmann-ddia.1e, src.book.reis-housley-fundamentals-data-engineering` đặt ranh giới cho claim; phần synthesis không được gán nguyên văn cho vendor.
- Trước khi lab chạy, note này là giáo trình đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.
