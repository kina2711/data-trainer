# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 263: Snapshots and SCD2 Invariants

## Mục tiêu bài học

**Năng lực cần chứng minh.** Cài ghi lịch sử đạt ba bất biến và chỉ ra ca dùng mà cơ chế này không đủ.

**Điều kiện hoàn thành.** Ba bất biến giữ qua 500 lần cập nhật, và số thay đổi bị bỏ sót giữa hai lần chạy được định lượng.

> [!abstract] Câu hỏi trung tâm
> Snapshot SCD2 cần key, change strategy và temporal invariants nào để lịch sử không overlap, không mất delete và dùng được cho as-of joins?

## 1. Snapshot quan sát state, không phải event log

Snapshot định kỳ so current mutable rows với version đã biết và ghi history kiểu SCD2. Nó chỉ thấy states tại các lần quan sát; hai thay đổi giữa runs có thể co lại thành một. Vì vậy snapshot không tái tạo mọi transaction và không thay CDC/audit log. Contract nêu cadence, source consistency và history fidelity cần thiết. Dùng snapshot cho dimension history, không gọi nó là event stream.

## 2. Unique key là entity identity

Key phải ổn định, unique và non-null trong source scope. Nếu business key tái sử dụng hoặc tenant scope thiếu, history của hai entity bị nối. Key change trông như delete plus insert, không phải rename tự hiểu. Test source uniqueness trước snapshot và lưu collision disposition. Surrogate snapshot record ID khác entity key; as-of join phải dùng entity key cộng valid interval.

## 3. Timestamp và check strategies

Timestamp strategy dựa reliable updated_at advancing on every relevant change; check strategy so configured fields. Timestamp thường dễ chịu hơn khi schema thêm cột nhưng bỏ sót change không cập nhật timestamp. Check all fields nhạy với schema/irrelevant changes; subset có thể bỏ semantic field. Strategy decision ghi producer guarantee, null behavior, precision và schema evolution. Không chọn bằng thói quen.

## 4. Valid-time invariants

Mỗi entity có intervals half-open `[valid_from, valid_to)`, tối đa một current row, không overlap và ordering deterministic. Adjacent gaps chỉ hợp lệ nếu entity thật sự absent và policy cho phép. As-of join dùng event time với interval, không current flag. Processing time của snapshot khác business-effective time; backdated source correction có thể cần custom handling/rebuild. Test exact boundary tại valid_to.

## 5. Hard deletes và invalidation

Current row biến mất khỏi source chỉ được biết nếu snapshot strategy/config xử lý hard delete và source observation đủ. Invalidate current version at detection time không cho biết actual delete time. Tombstone/new-record policy ảnh hưởng as-of consumers. Soft delete là field change và có restore. Retention/source filters có thể tạo false delete; snapshot query phải cover same universe every run.

## 6. SCD2 lab

Fixture gồm insert, two updates, same-timestamp tie, unchanged row, hard delete, soft delete/restore, key collision và schema add. Chạy repeated snapshots, inspect metadata columns và assert no overlap/one-current/as-of results. Reorder runs và fail midway. Compare with source change log oracle để nêu transitions snapshot không thể thấy. Đạt khi limitations được công bố, không chỉ table có nhiều rows.

## 7. Ma trận kiểm chứng từng mệnh đề

Trong `Snapshots and SCD2 Invariants`, mỗi claim phải nối được tới input boundary, compiled hoặc executed artifact, trạng thái trước–sau, failure signal và independent oracle. Một command kết thúc với exit code 0 không tự chứng minh dữ liệu đúng, đầy đủ hoặc phù hợp với consumer contract. Protocol nền của bài này: Dùng project/fixture nhỏ có exact boundary và owner; capture source, compiled/runtime artifacts, relations và consumer-facing diff; đối soát bằng alternate computation hoặc inventory độc lập.

### 7.1. Snapshot probe 1: entity key, observed change, valid interval, delete state và as-of oracle phải rõ

**Mệnh đề cần kiểm.** Snapshot probe 1: entity key, observed change, valid interval, delete state và as-of oracle phải rõ.

**Thiết kế phép thử.** Với `Snapshot probe 1: entity key, observed change, valid interval, delete state và as-of oracle phải rõ`, Bắt đầu bằng ca nhỏ nhất có thể làm mệnh đề sai; chỉ thêm dữ liệu sau khi failure signal đã xuất hiện đúng chỗ. Cách này phân biệt một assertion có lực với một bài demo chỉ đi qua happy path. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Snapshot probe 1: entity key, observed change, valid interval, delete state và as-of oracle phải rõ` phải cho thấy: Giữ fixture tối thiểu, raw failure rows và câu lệnh tái hiện; ảnh chụp màn hình một trạng thái xanh không đủ. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.2. Snapshot probe 2: entity key, observed change, valid interval, delete state và as-of oracle phải rõ

**Mệnh đề cần kiểm.** Snapshot probe 2: entity key, observed change, valid interval, delete state và as-of oracle phải rõ.

**Thiết kế phép thử.** Với `Snapshot probe 2: entity key, observed change, valid interval, delete state và as-of oracle phải rõ`, Giữ nguyên input rồi đổi đúng một tham số cấu hình liên quan. Nếu output đổi theo nhiều hướng cùng lúc, phép thử chưa cô lập được nguyên nhân và phải thu hẹp lại. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Snapshot probe 2: entity key, observed change, valid interval, delete state và as-of oracle phải rõ` phải cho thấy: Báo cả giá trị trước–sau của tham số, compiled artifact và diff đầu ra để reviewer thấy biến nào thực sự đổi. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.3. Snapshot probe 3: entity key, observed change, valid interval, delete state và as-of oracle phải rõ

**Mệnh đề cần kiểm.** Snapshot probe 3: entity key, observed change, valid interval, delete state và as-of oracle phải rõ.

**Thiết kế phép thử.** Với `Snapshot probe 3: entity key, observed change, valid interval, delete state và as-of oracle phải rõ`, Chạy cặp đối chứng: một input phải được chấp nhận và một input chỉ lệch tại boundary phải bị chặn hoặc được phân loại. Hai ca dùng chung code path để tránh so hai hệ thống khác nhau. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Snapshot probe 3: entity key, observed change, valid interval, delete state và as-of oracle phải rõ` phải cho thấy: Pass khi positive control đi qua, negative control dừng đúng lớp và không có side effect ngoài scope. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.4. Snapshot probe 4: entity key, observed change, valid interval, delete state và as-of oracle phải rõ

**Mệnh đề cần kiểm.** Snapshot probe 4: entity key, observed change, valid interval, delete state và as-of oracle phải rõ.

**Thiết kế phép thử.** Với `Snapshot probe 4: entity key, observed change, valid interval, delete state và as-of oracle phải rõ`, Đặt kill point ngay trước và ngay sau durable boundary. So trạng thái sau restart để biết hệ thống tạo replay có kiểm soát, silent gap hay một trạng thái nửa vời mà dashboard không báo. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Snapshot probe 4: entity key, observed change, valid interval, delete state và as-of oracle phải rõ` phải cho thấy: Run ledger phải cho biết commit/checkpoint nào bền vững; sau rerun, key set và side-effect ledger cùng hội tụ. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.5. Snapshot probe 5: entity key, observed change, valid interval, delete state và as-of oracle phải rõ

**Mệnh đề cần kiểm.** Snapshot probe 5: entity key, observed change, valid interval, delete state và as-of oracle phải rõ.

**Thiết kế phép thử.** Với `Snapshot probe 5: entity key, observed change, valid interval, delete state và as-of oracle phải rõ`, Đảo thứ tự input và thay concurrency nhưng giữ logical population. Kết quả khác nhau cho thấy thiết kế đang phụ thuộc physical order hoặc race thay vì contract đã công bố. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Snapshot probe 5: entity key, observed change, valid interval, delete state và as-of oracle phải rõ` phải cho thấy: Hash chuẩn hóa và business totals phải giống nhau giữa các thứ tự; chênh lệch được giữ như finding, không làm tròn mất. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.6. Snapshot probe 6: entity key, observed change, valid interval, delete state và as-of oracle phải rõ

**Mệnh đề cần kiểm.** Snapshot probe 6: entity key, observed change, valid interval, delete state và as-of oracle phải rõ.

**Thiết kế phép thử.** Với `Snapshot probe 6: entity key, observed change, valid interval, delete state và as-of oracle phải rõ`, Cho cùng logical identity xuất hiện hai lần: trước hết cùng payload, sau đó payload khác. Trường hợp đầu phải hội tụ; trường hợp sau phải lộ collision thay vì âm thầm chọn một bản. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Snapshot probe 6: entity key, observed change, valid interval, delete state và as-of oracle phải rõ` phải cho thấy: Same-content replay được đếm nhưng không nhân state; different-content collision có reason code và đường xử lý riêng. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.7. Snapshot probe 7: entity key, observed change, valid interval, delete state và as-of oracle phải rõ

**Mệnh đề cần kiểm.** Snapshot probe 7: entity key, observed change, valid interval, delete state và as-of oracle phải rõ.

**Thiết kế phép thử.** Với `Snapshot probe 7: entity key, observed change, valid interval, delete state và as-of oracle phải rõ`, Mở rộng fixture bằng một record tới trễ ngay trong horizon và một record nằm ngoài horizon. Ghi rõ record nào được sửa, record nào bị loại và metric nào khiến operator biết có mất coverage. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Snapshot probe 7: entity key, observed change, valid interval, delete state và as-of oracle phải rõ` phải cho thấy: Evidence ghi accepted-late, rejected-late và oldest outstanding timestamp; thiếu một nhóm được báo là coverage gap. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.8. Snapshot probe 8: entity key, observed change, valid interval, delete state và as-of oracle phải rõ

**Mệnh đề cần kiểm.** Snapshot probe 8: entity key, observed change, valid interval, delete state và as-of oracle phải rõ.

**Thiết kế phép thử.** Với `Snapshot probe 8: entity key, observed change, valid interval, delete state và as-of oracle phải rõ`, Dùng một schema change tương thích và một thay đổi phá vỡ key, type hoặc meaning. Kết quả phải chỉ ra khác biệt giữa parse được, chạy được và vẫn giữ đúng semantics. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Snapshot probe 8: entity key, observed change, valid interval, delete state và as-of oracle phải rõ` phải cho thấy: Lưu schema trước–sau, classification, compiled SQL và target state; một migration chạy xong nhưng đổi meaning vẫn fail. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.9. Snapshot probe 9: entity key, observed change, valid interval, delete state và as-of oracle phải rõ

**Mệnh đề cần kiểm.** Snapshot probe 9: entity key, observed change, valid interval, delete state và as-of oracle phải rõ.

**Thiết kế phép thử.** Với `Snapshot probe 9: entity key, observed change, valid interval, delete state và as-of oracle phải rõ`, Tạo bảng rỗng, bảng một row và bảng có duplicate bù cho missing row. Đây là ba ca dễ làm count hoặc aggregate xanh dù invariant thực tế đã hỏng. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Snapshot probe 9: entity key, observed change, valid interval, delete state và as-of oracle phải rõ` phải cho thấy: Oracle so count, key multiset và typed hashes. Ca missing-plus-duplicate phải bị phát hiện dù tổng row count không đổi. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.10. Snapshot probe 10: entity key, observed change, valid interval, delete state và as-of oracle phải rõ

**Mệnh đề cần kiểm.** Snapshot probe 10: entity key, observed change, valid interval, delete state và as-of oracle phải rõ.

**Thiết kế phép thử.** Với `Snapshot probe 10: entity key, observed change, valid interval, delete state và as-of oracle phải rõ`, Cho reviewer chỉ artifacts, không cho xem lời giải thích của tác giả. Nếu họ không dựng lại được input, decision và diff thì evidence package chưa đủ để bàn giao. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Snapshot probe 10: entity key, observed change, valid interval, delete state và as-of oracle phải rõ` phải cho thấy: Artifact package đạt khi reviewer tái hiện đúng diff và chỉ ra được limitation mà không cần hỏi tác giả về state ẩn. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.11. Snapshot probe 11: entity key, observed change, valid interval, delete state và as-of oracle phải rõ

**Mệnh đề cần kiểm.** Snapshot probe 11: entity key, observed change, valid interval, delete state và as-of oracle phải rõ.

**Thiết kế phép thử.** Với `Snapshot probe 11: entity key, observed change, valid interval, delete state và as-of oracle phải rõ`, So output với một cách tính độc lập không tái sử dụng macro, filter hoặc intermediate relation đang được kiểm. Hai phép tính dùng chung lỗi chỉ tạo sự đồng thuận giả. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Snapshot probe 11: entity key, observed change, valid interval, delete state và as-of oracle phải rõ` phải cho thấy: Independent result phải khớp ở key/grain đã định; nếu chỉ khớp aggregate cao hơn thì drill-down chưa hoàn tất. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.12. Snapshot probe 12: entity key, observed change, valid interval, delete state và as-of oracle phải rõ

**Mệnh đề cần kiểm.** Snapshot probe 12: entity key, observed change, valid interval, delete state và as-of oracle phải rõ.

**Thiết kế phép thử.** Với `Snapshot probe 12: entity key, observed change, valid interval, delete state và as-of oracle phải rõ`, Thử trên hai scope: selection hẹp dùng trong CI và population đầy đủ dùng khi phát hành. Ghi phần coverage bị bỏ qua; tốc độ của CI không được biến thành tuyên bố kiểm toàn bộ dữ liệu. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Snapshot probe 12: entity key, observed change, valid interval, delete state và as-of oracle phải rõ` phải cho thấy: Kết quả nêu numerator, denominator và excluded nodes/partitions; không dùng từ `all` khi selection không phủ toàn graph. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.13. Snapshot probe 13: entity key, observed change, valid interval, delete state và as-of oracle phải rõ

**Mệnh đề cần kiểm.** Snapshot probe 13: entity key, observed change, valid interval, delete state và as-of oracle phải rõ.

**Thiết kế phép thử.** Với `Snapshot probe 13: entity key, observed change, valid interval, delete state và as-of oracle phải rõ`, Đẩy một giá trị tới sát giới hạn precision, timezone, partition hoặc threshold. Boundary phải được viết half-open hay inclusive rõ ràng, không suy từ một ví dụ ở giữa khoảng. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Snapshot probe 13: entity key, observed change, valid interval, delete state và as-of oracle phải rõ` phải cho thấy: Hai phía của boundary đều có expected result và raw observation. Sai đúng một đơn vị phải làm test fail có chẩn đoán. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.14. Snapshot probe 14: entity key, observed change, valid interval, delete state và as-of oracle phải rõ

**Mệnh đề cần kiểm.** Snapshot probe 14: entity key, observed change, valid interval, delete state và as-of oracle phải rõ.

**Thiết kế phép thử.** Với `Snapshot probe 14: entity key, observed change, valid interval, delete state và as-of oracle phải rõ`, Thay constraint quan trọng nhất bằng giá trị đủ để decision phải đảo. Nếu thiết kế vẫn đưa cùng lựa chọn mà không giải thích, decision rule đang là khẩu hiệu chứ chưa phải rule. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Snapshot probe 14: entity key, observed change, valid interval, delete state và as-of oracle phải rõ` phải cho thấy: ADR hoặc rule chỉ pass khi changed constraint tạo lựa chọn mới đúng như đã dự báo và reversal threshold được lưu. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.15. Snapshot probe 15: entity key, observed change, valid interval, delete state và as-of oracle phải rõ

**Mệnh đề cần kiểm.** Snapshot probe 15: entity key, observed change, valid interval, delete state và as-of oracle phải rõ.

**Thiết kế phép thử.** Với `Snapshot probe 15: entity key, observed change, valid interval, delete state và as-of oracle phải rõ`, Lặp lại phép thử từ môi trường sạch bằng seed và versions đã lưu. Một kết quả chỉ tái hiện được trên workspace của tác giả không đủ làm release evidence. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Snapshot probe 15: entity key, observed change, valid interval, delete state và as-of oracle phải rõ` phải cho thấy: Lần chạy sạch phải tạo cùng canonical state; khác biệt do timestamp, file order hoặc generated IDs phải được loại hoặc giải thích. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

## 8. Quy trình phản biện

Áp dụng sáu bước sau cho `Snapshots and SCD2 Invariants`; nếu một bước không phù hợp, ghi lý do thay vì bỏ qua im lặng.

1. Với `wiki.transformation.snapshots-scd2-invariants`, chốt grain, identity, time boundary và consumer-visible invariant trước câu lệnh.
2. Tách parse/compile state, warehouse execution và publication state.
3. Pin dbt core, adapter, warehouse hoặc orchestrator version cùng configuration có ảnh hưởng.
4. Kiểm correctness bằng key set, typed hash và business invariant trước performance.
5. Chạy negative case, kill point hoặc changed assumption; green path đơn lẻ không đủ.
6. Phân loại source fact, project convention, curriculum synthesis và untested hypothesis.

## 9. Câu hỏi tự kiểm tra

1. `Snapshot probe 1: entity key, observed change, valid interval, delete state và as-of oracle phải rõ` sẽ thất bại trước tiên ở boundary nào?
2. Với `Snapshot probe 2: entity key, observed change, valid interval, delete state và as-of oracle phải rõ`, artifact nào là nguồn bằng chứng mạnh nhất?
3. Counterexample nhỏ nhất cho `Snapshot probe 3: entity key, observed change, valid interval, delete state và as-of oracle phải rõ` gồm những row hoặc state nào?
4. `Snapshot probe 4: entity key, observed change, valid interval, delete state và as-of oracle phải rõ` có thể xanh giả trong tình huống nào?
5. Version, adapter, timezone hoặc state nào làm `Snapshot probe 5: entity key, observed change, valid interval, delete state và as-of oracle phải rõ` đổi nghĩa?
6. Phần nào của `Snapshot probe 6: entity key, observed change, valid interval, delete state và as-of oracle phải rõ` hiện mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `Snapshots and SCD2 Invariants` chưa chạy trên warehouse, dbt project hoặc orchestrator production; các mục kiểm chứng vẫn là protocol và expected evidence.
- Các claim gắn `wiki.transformation.snapshots-scd2-invariants` phải kiểm lại theo dbt core, adapter, warehouse và scheduler version được chọn.
- Decision matrix, failure campaign và ngưỡng review là curriculum synthesis, không phải cam kết của vendor.
- Note giữ trạng thái `review` cho tới khi chủ dự án duyệt semantic meaning và learner artifact.

## Reference
1. [[SRC-DBT-SNAPSHOTS]]
2. [[SRC-KLEPPMANN-DDIA-1E]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-DBT-SNAPSHOTS]] | Cơ chế, contract hoặc giới hạn liên quan | Đã đọc locator; claim theo version/configuration |
| [[SRC-KLEPPMANN-DDIA-1E]] | Cơ chế, contract hoặc giới hạn liên quan | Đã đọc locator; claim theo version/configuration |

## Key takeaways
- Snapshot là sampled state history với SCD2 invariants, không phải transaction log; key, strategy, delete policy và as-of boundary quyết định độ tin cậy.
- Với `Snapshots and SCD2 Invariants`, compiled intent và observed state phải được lưu tách biệt; trộn hai lớp sẽ che failure window.
- Oracle của bài phải bám câu hỏi trung tâm: Snapshot SCD2 cần key, change strategy và temporal invariants nào để lịch sử không overlap, không mất delete và dùng được cho as-of joins?
- Các source IDs `src.web.dbt-snapshots, src.book.kleppmann-ddia.1e` đặt ranh giới cho claim; phần synthesis không được gán nguyên văn cho vendor.
- Trước khi lab chạy, note này là giáo trình đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.
