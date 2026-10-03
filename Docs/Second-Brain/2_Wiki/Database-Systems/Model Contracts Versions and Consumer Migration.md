---
note_id: wiki.transformation.model-contracts-versions-migration
note_type: concept-deep-dive
status: canonical
approved_by: second-brain-owner
approved_at: 2026-10-03
approval_scope: all-registered-notes
canonical_since: 2026-10-03
language: vi
created: 2026-10-02
last_verified: 2026-10-02
editorial_pass: humanized-v3
primary_question: Contract và model version phối hợp thế nào để bắt shape drift sớm nhưng vẫn cho consumer một migration window đo được?
source_ids:
  - src.web.dbt-model-contracts
  - src.web.dbt-model-versions
  - src.book.reis-housley-fundamentals-data-engineering
aliases: [Model Contracts Versions and Consumer Migration]
tags: [wiki/transformation, dbt, orchestration, reliability]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/152-model-contracts-versions-consumer-migration.md
relationships:
  builds_on: []
  prerequisite_of: []
  related_to: []

---
# Model Contracts Versions and Consumer Migration

> [!abstract] Câu hỏi trung tâm
> Contract và model version phối hợp thế nào để bắt shape drift sớm nhưng vẫn cho consumer một migration window đo được?

## 1. Contract bảo vệ shape có giới hạn

Enforced model contract kiểm declared column names, data types và constraints được hỗ trợ trước/khi build theo tool/platform. Nó không chứng minh business meaning, completeness, freshness hay metric correctness. Constraint enforcement khác theo warehouse; một constraint có thể informational. Contract file và compiled DDL phải được review cùng adapter version. Không quảng bá contract thành data quality toàn diện.

## 2. Breaking change taxonomy

Remove/rename column, incompatible type/nullability, grain/key, meaning/unit/timezone, row filtering và SLA/access có thể phá consumer. Chỉ nhóm đầu dễ được shape contract bắt. Semantic change giữ schema y nguyên vẫn cần version/migration. Classify additive-compatible, behavior-compatible, deprecating và breaking theo consumer evidence. `select *` khiến additive column cũng có thể break output shape.

## 3. Khi nào version

Version model khi consumer ngoài quyền kiểm soát cần tiếp tục dùng old contract trong lúc migration; không version mọi refactor nội bộ. Nhiều live versions tăng compute/storage/docs/testing. Latest ref đổi theo maintainer; critical consumer có thể pin explicit version. Prerelease cho shadow validation. Version decision ghi expected lifetime, owner và sunset condition, tránh v1/v2 tồn tại vô hạn.

## 4. Migration window

Publish vNext beside current, build compatibility matrix, dual-run/reconcile representative periods và thông báo diff/deprecation date. Inventory consumers bằng refs, exposures, query history và owner confirmation; không coi lineage khai báo là đầy đủ. Consumer test, update và sign-off theo risk. Chuyển latest chỉ sau gates; old version tiếp tục monitored. Removal có explicit zero-usage/waiver evidence and rollback.

## 5. Compatibility adapters

Khi feasible, compatibility view hoặc alias giúp old schema map sang new, nhưng có expiry và tests. Không dùng shim để che meaning change không thể chuyển đổi. Backfill history, defaults và null mapping cần policy. Cross-version metrics được so cùng boundary. Access/grants và documentation thuộc migration, không chỉ SQL. Cost của serving both versions được đo.

## 6. Failure rehearsal

Inject undeclared column/type change để contract fail; inject semantic unit change để chứng minh shape contract vẫn pass. Deploy prerelease, pin one consumer, leave another on latest, then rollback latest pointer. Capture warnings, compiled artifacts, relations and consumer results. Đạt khi owner chứng minh migration/rollback without synchronized flag day và nêu phần contract không bắt được.

## 7. Ma trận kiểm chứng từng mệnh đề

Trong `Model Contracts Versions and Consumer Migration`, mỗi claim phải nối được tới input boundary, compiled hoặc executed artifact, trạng thái trước–sau, failure signal và independent oracle. Một command kết thúc với exit code 0 không tự chứng minh dữ liệu đúng, đầy đủ hoặc phù hợp với consumer contract. Protocol nền của bài này: Dùng project/fixture nhỏ có exact boundary và owner; capture source, compiled/runtime artifacts, relations và consumer-facing diff; đối soát bằng alternate computation hoặc inventory độc lập.

### 7.1. Contract-version probe 1: change class, enforcement, consumer inventory, migration gate và rollback phải rõ

**Mệnh đề cần kiểm.** Contract-version probe 1: change class, enforcement, consumer inventory, migration gate và rollback phải rõ.

**Thiết kế phép thử cho `wiki.transformation.model-contracts-versions-migration`.** Với `Contract-version probe 1: change class, enforcement, consumer inventory, migration gate và rollback phải rõ`, Bắt đầu bằng ca nhỏ nhất có thể làm mệnh đề sai; chỉ thêm dữ liệu sau khi failure signal đã xuất hiện đúng chỗ. Cách này phân biệt một assertion có lực với một bài demo chỉ đi qua happy path. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Contract-version probe 1: change class, enforcement, consumer inventory, migration gate và rollback phải rõ` phải cho thấy: Giữ fixture tối thiểu, raw failure rows và câu lệnh tái hiện; ảnh chụp màn hình một trạng thái xanh không đủ. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.2. Contract-version probe 2: change class, enforcement, consumer inventory, migration gate và rollback phải rõ

**Mệnh đề cần kiểm.** Contract-version probe 2: change class, enforcement, consumer inventory, migration gate và rollback phải rõ.

**Thiết kế phép thử cho `wiki.transformation.model-contracts-versions-migration`.** Với `Contract-version probe 2: change class, enforcement, consumer inventory, migration gate và rollback phải rõ`, Giữ nguyên input rồi đổi đúng một tham số cấu hình liên quan. Nếu output đổi theo nhiều hướng cùng lúc, phép thử chưa cô lập được nguyên nhân và phải thu hẹp lại. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Contract-version probe 2: change class, enforcement, consumer inventory, migration gate và rollback phải rõ` phải cho thấy: Báo cả giá trị trước–sau của tham số, compiled artifact và diff đầu ra để reviewer thấy biến nào thực sự đổi. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.3. Contract-version probe 3: change class, enforcement, consumer inventory, migration gate và rollback phải rõ

**Mệnh đề cần kiểm.** Contract-version probe 3: change class, enforcement, consumer inventory, migration gate và rollback phải rõ.

**Thiết kế phép thử cho `wiki.transformation.model-contracts-versions-migration`.** Với `Contract-version probe 3: change class, enforcement, consumer inventory, migration gate và rollback phải rõ`, Chạy cặp đối chứng: một input phải được chấp nhận và một input chỉ lệch tại boundary phải bị chặn hoặc được phân loại. Hai ca dùng chung code path để tránh so hai hệ thống khác nhau. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Contract-version probe 3: change class, enforcement, consumer inventory, migration gate và rollback phải rõ` phải cho thấy: Pass khi positive control đi qua, negative control dừng đúng lớp và không có side effect ngoài scope. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.4. Contract-version probe 4: change class, enforcement, consumer inventory, migration gate và rollback phải rõ

**Mệnh đề cần kiểm.** Contract-version probe 4: change class, enforcement, consumer inventory, migration gate và rollback phải rõ.

**Thiết kế phép thử cho `wiki.transformation.model-contracts-versions-migration`.** Với `Contract-version probe 4: change class, enforcement, consumer inventory, migration gate và rollback phải rõ`, Đặt kill point ngay trước và ngay sau durable boundary. So trạng thái sau restart để biết hệ thống tạo replay có kiểm soát, silent gap hay một trạng thái nửa vời mà dashboard không báo. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Contract-version probe 4: change class, enforcement, consumer inventory, migration gate và rollback phải rõ` phải cho thấy: Run ledger phải cho biết commit/checkpoint nào bền vững; sau rerun, key set và side-effect ledger cùng hội tụ. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.5. Contract-version probe 5: change class, enforcement, consumer inventory, migration gate và rollback phải rõ

**Mệnh đề cần kiểm.** Contract-version probe 5: change class, enforcement, consumer inventory, migration gate và rollback phải rõ.

**Thiết kế phép thử cho `wiki.transformation.model-contracts-versions-migration`.** Với `Contract-version probe 5: change class, enforcement, consumer inventory, migration gate và rollback phải rõ`, Đảo thứ tự input và thay concurrency nhưng giữ logical population. Kết quả khác nhau cho thấy thiết kế đang phụ thuộc physical order hoặc race thay vì contract đã công bố. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Contract-version probe 5: change class, enforcement, consumer inventory, migration gate và rollback phải rõ` phải cho thấy: Hash chuẩn hóa và business totals phải giống nhau giữa các thứ tự; chênh lệch được giữ như finding, không làm tròn mất. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.6. Contract-version probe 6: change class, enforcement, consumer inventory, migration gate và rollback phải rõ

**Mệnh đề cần kiểm.** Contract-version probe 6: change class, enforcement, consumer inventory, migration gate và rollback phải rõ.

**Thiết kế phép thử cho `wiki.transformation.model-contracts-versions-migration`.** Với `Contract-version probe 6: change class, enforcement, consumer inventory, migration gate và rollback phải rõ`, Cho cùng logical identity xuất hiện hai lần: trước hết cùng payload, sau đó payload khác. Trường hợp đầu phải hội tụ; trường hợp sau phải lộ collision thay vì âm thầm chọn một bản. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Contract-version probe 6: change class, enforcement, consumer inventory, migration gate và rollback phải rõ` phải cho thấy: Same-content replay được đếm nhưng không nhân state; different-content collision có reason code và đường xử lý riêng. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.7. Contract-version probe 7: change class, enforcement, consumer inventory, migration gate và rollback phải rõ

**Mệnh đề cần kiểm.** Contract-version probe 7: change class, enforcement, consumer inventory, migration gate và rollback phải rõ.

**Thiết kế phép thử cho `wiki.transformation.model-contracts-versions-migration`.** Với `Contract-version probe 7: change class, enforcement, consumer inventory, migration gate và rollback phải rõ`, Mở rộng fixture bằng một record tới trễ ngay trong horizon và một record nằm ngoài horizon. Ghi rõ record nào được sửa, record nào bị loại và metric nào khiến operator biết có mất coverage. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Contract-version probe 7: change class, enforcement, consumer inventory, migration gate và rollback phải rõ` phải cho thấy: Evidence ghi accepted-late, rejected-late và oldest outstanding timestamp; thiếu một nhóm được báo là coverage gap. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.8. Contract-version probe 8: change class, enforcement, consumer inventory, migration gate và rollback phải rõ

**Mệnh đề cần kiểm.** Contract-version probe 8: change class, enforcement, consumer inventory, migration gate và rollback phải rõ.

**Thiết kế phép thử cho `wiki.transformation.model-contracts-versions-migration`.** Với `Contract-version probe 8: change class, enforcement, consumer inventory, migration gate và rollback phải rõ`, Dùng một schema change tương thích và một thay đổi phá vỡ key, type hoặc meaning. Kết quả phải chỉ ra khác biệt giữa parse được, chạy được và vẫn giữ đúng semantics. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Contract-version probe 8: change class, enforcement, consumer inventory, migration gate và rollback phải rõ` phải cho thấy: Lưu schema trước–sau, classification, compiled SQL và target state; một migration chạy xong nhưng đổi meaning vẫn fail. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.9. Contract-version probe 9: change class, enforcement, consumer inventory, migration gate và rollback phải rõ

**Mệnh đề cần kiểm.** Contract-version probe 9: change class, enforcement, consumer inventory, migration gate và rollback phải rõ.

**Thiết kế phép thử cho `wiki.transformation.model-contracts-versions-migration`.** Với `Contract-version probe 9: change class, enforcement, consumer inventory, migration gate và rollback phải rõ`, Tạo bảng rỗng, bảng một row và bảng có duplicate bù cho missing row. Đây là ba ca dễ làm count hoặc aggregate xanh dù invariant thực tế đã hỏng. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Contract-version probe 9: change class, enforcement, consumer inventory, migration gate và rollback phải rõ` phải cho thấy: Oracle so count, key multiset và typed hashes. Ca missing-plus-duplicate phải bị phát hiện dù tổng row count không đổi. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.10. Contract-version probe 10: change class, enforcement, consumer inventory, migration gate và rollback phải rõ

**Mệnh đề cần kiểm.** Contract-version probe 10: change class, enforcement, consumer inventory, migration gate và rollback phải rõ.

**Thiết kế phép thử cho `wiki.transformation.model-contracts-versions-migration`.** Với `Contract-version probe 10: change class, enforcement, consumer inventory, migration gate và rollback phải rõ`, Cho reviewer chỉ artifacts, không cho xem lời giải thích của tác giả. Nếu họ không dựng lại được input, decision và diff thì evidence package chưa đủ để bàn giao. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Contract-version probe 10: change class, enforcement, consumer inventory, migration gate và rollback phải rõ` phải cho thấy: Artifact package đạt khi reviewer tái hiện đúng diff và chỉ ra được limitation mà không cần hỏi tác giả về state ẩn. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.11. Contract-version probe 11: change class, enforcement, consumer inventory, migration gate và rollback phải rõ

**Mệnh đề cần kiểm.** Contract-version probe 11: change class, enforcement, consumer inventory, migration gate và rollback phải rõ.

**Thiết kế phép thử cho `wiki.transformation.model-contracts-versions-migration`.** Với `Contract-version probe 11: change class, enforcement, consumer inventory, migration gate và rollback phải rõ`, So output với một cách tính độc lập không tái sử dụng macro, filter hoặc intermediate relation đang được kiểm. Hai phép tính dùng chung lỗi chỉ tạo sự đồng thuận giả. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Contract-version probe 11: change class, enforcement, consumer inventory, migration gate và rollback phải rõ` phải cho thấy: Independent result phải khớp ở key/grain đã định; nếu chỉ khớp aggregate cao hơn thì drill-down chưa hoàn tất. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.12. Contract-version probe 12: change class, enforcement, consumer inventory, migration gate và rollback phải rõ

**Mệnh đề cần kiểm.** Contract-version probe 12: change class, enforcement, consumer inventory, migration gate và rollback phải rõ.

**Thiết kế phép thử cho `wiki.transformation.model-contracts-versions-migration`.** Với `Contract-version probe 12: change class, enforcement, consumer inventory, migration gate và rollback phải rõ`, Thử trên hai scope: selection hẹp dùng trong CI và population đầy đủ dùng khi phát hành. Ghi phần coverage bị bỏ qua; tốc độ của CI không được biến thành tuyên bố kiểm toàn bộ dữ liệu. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Contract-version probe 12: change class, enforcement, consumer inventory, migration gate và rollback phải rõ` phải cho thấy: Kết quả nêu numerator, denominator và excluded nodes/partitions; không dùng từ `all` khi selection không phủ toàn graph. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.13. Contract-version probe 13: change class, enforcement, consumer inventory, migration gate và rollback phải rõ

**Mệnh đề cần kiểm.** Contract-version probe 13: change class, enforcement, consumer inventory, migration gate và rollback phải rõ.

**Thiết kế phép thử cho `wiki.transformation.model-contracts-versions-migration`.** Với `Contract-version probe 13: change class, enforcement, consumer inventory, migration gate và rollback phải rõ`, Đẩy một giá trị tới sát giới hạn precision, timezone, partition hoặc threshold. Boundary phải được viết half-open hay inclusive rõ ràng, không suy từ một ví dụ ở giữa khoảng. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Contract-version probe 13: change class, enforcement, consumer inventory, migration gate và rollback phải rõ` phải cho thấy: Hai phía của boundary đều có expected result và raw observation. Sai đúng một đơn vị phải làm test fail có chẩn đoán. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.14. Contract-version probe 14: change class, enforcement, consumer inventory, migration gate và rollback phải rõ

**Mệnh đề cần kiểm.** Contract-version probe 14: change class, enforcement, consumer inventory, migration gate và rollback phải rõ.

**Thiết kế phép thử cho `wiki.transformation.model-contracts-versions-migration`.** Với `Contract-version probe 14: change class, enforcement, consumer inventory, migration gate và rollback phải rõ`, Thay constraint quan trọng nhất bằng giá trị đủ để decision phải đảo. Nếu thiết kế vẫn đưa cùng lựa chọn mà không giải thích, decision rule đang là khẩu hiệu chứ chưa phải rule. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Contract-version probe 14: change class, enforcement, consumer inventory, migration gate và rollback phải rõ` phải cho thấy: ADR hoặc rule chỉ pass khi changed constraint tạo lựa chọn mới đúng như đã dự báo và reversal threshold được lưu. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.15. Contract-version probe 15: change class, enforcement, consumer inventory, migration gate và rollback phải rõ

**Mệnh đề cần kiểm.** Contract-version probe 15: change class, enforcement, consumer inventory, migration gate và rollback phải rõ.

**Thiết kế phép thử cho `wiki.transformation.model-contracts-versions-migration`.** Với `Contract-version probe 15: change class, enforcement, consumer inventory, migration gate và rollback phải rõ`, Lặp lại phép thử từ môi trường sạch bằng seed và versions đã lưu. Một kết quả chỉ tái hiện được trên workspace của tác giả không đủ làm release evidence. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Contract-version probe 15: change class, enforcement, consumer inventory, migration gate và rollback phải rõ` phải cho thấy: Lần chạy sạch phải tạo cùng canonical state; khác biệt do timestamp, file order hoặc generated IDs phải được loại hoặc giải thích. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

## 8. Quy trình phản biện

Áp dụng sáu bước sau cho `Model Contracts Versions and Consumer Migration`; nếu một bước không phù hợp, ghi lý do thay vì bỏ qua im lặng.

1. Với `wiki.transformation.model-contracts-versions-migration`, chốt grain, identity, time boundary và consumer-visible invariant trước câu lệnh.
2. Tách parse/compile state, warehouse execution và publication state.
3. Pin dbt core, adapter, warehouse hoặc orchestrator version cùng configuration có ảnh hưởng.
4. Kiểm correctness bằng key set, typed hash và business invariant trước performance.
5. Chạy negative case, kill point hoặc changed assumption; green path đơn lẻ không đủ.
6. Phân loại source fact, project convention, curriculum synthesis và untested hypothesis.

## 9. Câu hỏi tự kiểm tra

1. `Contract-version probe 1: change class, enforcement, consumer inventory, migration gate và rollback phải rõ` sẽ thất bại trước tiên ở boundary nào?
2. Với `Contract-version probe 2: change class, enforcement, consumer inventory, migration gate và rollback phải rõ`, artifact nào là nguồn bằng chứng mạnh nhất?
3. Counterexample nhỏ nhất cho `Contract-version probe 3: change class, enforcement, consumer inventory, migration gate và rollback phải rõ` gồm những row hoặc state nào?
4. `Contract-version probe 4: change class, enforcement, consumer inventory, migration gate và rollback phải rõ` có thể xanh giả trong tình huống nào?
5. Version, adapter, timezone hoặc state nào làm `Contract-version probe 5: change class, enforcement, consumer inventory, migration gate và rollback phải rõ` đổi nghĩa?
6. Phần nào của `Contract-version probe 6: change class, enforcement, consumer inventory, migration gate và rollback phải rõ` hiện mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `Model Contracts Versions and Consumer Migration` chưa chạy trên warehouse, dbt project hoặc orchestrator production; các mục kiểm chứng vẫn là protocol và expected evidence.
- Các claim gắn `wiki.transformation.model-contracts-versions-migration` phải kiểm lại theo dbt core, adapter, warehouse và scheduler version được chọn.
- Decision matrix, failure campaign và ngưỡng review là curriculum synthesis, không phải cam kết của vendor.
- Note giữ trạng thái `review` cho tới khi chủ dự án duyệt semantic meaning và learner artifact.

## Reference
1. [[SRC-DBT-MODEL-CONTRACTS]]
2. [[SRC-DBT-MODEL-VERSIONS]]
3. [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-DBT-MODEL-CONTRACTS]] | Cơ chế, contract hoặc giới hạn liên quan | Đã đọc locator; claim theo version/configuration |
| [[SRC-DBT-MODEL-VERSIONS]] | Cơ chế, contract hoặc giới hạn liên quan | Đã đọc locator; claim theo version/configuration |
| [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]] | Cơ chế, contract hoặc giới hạn liên quan | Đã đọc locator; claim theo version/configuration |

## Key takeaways
- Contract bắt shape trong phạm vi hỗ trợ, còn version tạo migration window cho breaking change; semantic compatibility vẫn cần consumer evidence.
- Với `Model Contracts Versions and Consumer Migration`, compiled intent và observed state phải được lưu tách biệt; trộn hai lớp sẽ che failure window.
- Oracle của bài phải bám câu hỏi trung tâm: Contract và model version phối hợp thế nào để bắt shape drift sớm nhưng vẫn cho consumer một migration window đo được?
- Các source IDs `src.web.dbt-model-contracts, src.web.dbt-model-versions, src.book.reis-housley-fundamentals-data-engineering` đặt ranh giới cho claim; phần synthesis không được gán nguyên văn cho vendor.
- Trước khi lab chạy, note này là giáo trình đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule — kiểm chứng `wiki.transformation.model-contracts-versions-migration`

> [!important] Phân loại mệnh đề
> Với `wiki.transformation.model-contracts-versions-migration`, sơ đồ, ví dụ và artifact về **Model Contracts Versions and Consumer Migration** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.web.dbt-model-contracts"] --> B["Khóa boundary"]
    B --> M["Cơ chế: Model Contracts Versions and Consumer Migration"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.transformation.model-contracts-versions-migration` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **Model Contracts Versions and Consumer Migration**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```sql
-- Verification harness for: Model Contracts Versions and Consumer Migration
WITH evidence AS (
    SELECT 'wiki.transformation.model-contracts-versions-migration' AS concept_id,
           'boundary_declared' AS check_name, 1 AS passed
    UNION ALL
    SELECT 'wiki.transformation.model-contracts-versions-migration', 'independent_oracle', 1
    UNION ALL
    SELECT 'wiki.transformation.model-contracts-versions-migration', 'reversal_trigger_recorded', 1
)
SELECT concept_id,
       MIN(passed) AS all_hard_checks_pass,
       COUNT(*) AS evidence_items
FROM evidence
GROUP BY concept_id
HAVING MIN(passed) = 1;
```

Artifact của `wiki.transformation.model-contracts-versions-migration` buộc người dùng ghi boundary, oracle và reversal trigger cho **Model Contracts Versions and Consumer Migration**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

### Tự kiểm tra trước khi tái sử dụng

1. Bạn có thể trả lời `Contract và model version phối hợp thế nào để bắt shape drift sớm nhưng vẫn cho consumer một migration window đo được?` bằng một câu mà không kéo thêm concept thứ hai không?
2. Source locator nào đỡ cho claim, và phần nào chỉ là synthesis trong note?
3. Observation nào khiến bạn dừng, thu hẹp hoặc đảo quyết định?
4. Artifact nào cho phép một reviewer độc lập tái hiện kết quả?

<!-- ATOMIC-EXECUTION-CAPSULE:END -->
