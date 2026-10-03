---
note_id: wiki.transformation.dbt-jinja-macro-boundary
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
primary_question: Macro nào thật sự loại bỏ một policy lặp lại, và khi nào abstraction che SQL đến mức review, lineage và debugging đắt hơn phần code tiết kiệm?
source_ids:
  - src.web.dbt-jinja-macros
  - src.web.dbt-data-tests
aliases: [Jinja and Macros Where Abstraction Stops Paying]
tags: [wiki/transformation, dbt, orchestration, reliability]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/146-jinja-macros-abstraction-boundary.md
relationships:
  builds_on: []
  prerequisite_of: []
  related_to: []

---
# Jinja and Macros Where Abstraction Stops Paying

> [!abstract] Câu hỏi trung tâm
> Macro nào thật sự loại bỏ một policy lặp lại, và khi nào abstraction che SQL đến mức review, lineage và debugging đắt hơn phần code tiết kiệm?

## 1. Jinja sinh SQL

Expressions emit text, statements điều khiển template, macros nhận arguments và trả SQL/text; warehouse chỉ thấy compiled SQL. Vì vậy review cần cả source template lẫn compiled output. Jinja truthiness, quoting, whitespace và parse/execute context khác SQL semantics. Macro có thể gọi adapter dispatch/introspection, làm output phụ thuộc target. Không debug macro chỉ bằng nhìn model gọi nó.

## 2. Abstraction trả giá bằng indirection

Macro tốt nắm một policy ổn định: safe casting, standardized surrogate key, grant convention hoặc repeated test assertion. Macro kém giấu business rule riêng của một model, nhận hàng chục flags hoặc tạo SQL khác mạnh theo environment. DRY không phải mục tiêu tối cao; ba dòng SQL rõ có thể rẻ hơn một abstraction mà reviewer phải mentally execute. Đo call sites, change coupling và debug path.

## 3. Interface contract

Document macro purpose, arguments/types/defaults, return shape, side effects, supported adapters và failure behavior. Validate identifiers/literals đúng context; không nối untrusted strings tùy ý. Namespace package macros. Breaking signature/output change cần version/migration. Macro output ảnh hưởng grain hoặc column set phải có compile fixtures và downstream contract tests. Do not use environment conditionals to silently change business semantics.

## 4. Parse execute và introspection

`execute` phân biệt parse from execution contexts; queries/introspection chỉ hợp lệ khi connection available. Code phải trả graph-consistent output ở parse path và fail rõ ở runtime path. `run_query` có cost, permissions và nondeterminism nếu metadata/source state đổi giữa compile and run. Cache assumptions phải nêu. Macros dùng current timestamp/randomness phá deterministic compilation và state comparison.

## 5. Test macro như compiler

Compile representative calls across adapter targets/configurations; compare normalized expected SQL/golden snapshots và then execute semantic fixtures. Include empty list, reserved identifier, null argument, unusual schema, large column list và unsupported adapter. Golden SQL bắt drift nhưng có thể overfit whitespace; semantic test bắt behavior. Package upgrade chạy same matrix và inspect manifest macro dependencies.

## 6. Refactor decision

Bắt đầu từ duplicated policy chứ không từ desire to be clever. Extract smallest stable unit, keep model grain visible, name arguments in domain terms, limit branching và provide escape hatch only with explicit review. Nếu call sites cần đọc macro source mỗi lần để hiểu query, abstraction chưa trả lợi. Reversal trigger: adapter divergence, branching complexity hoặc incident/debug time vượt maintenance saved.

## 7. Ma trận kiểm chứng từng mệnh đề

Trong `Jinja and Macros Where Abstraction Stops Paying`, mỗi claim phải nối được tới input boundary, compiled hoặc executed artifact, trạng thái trước–sau, failure signal và independent oracle. Một command kết thúc với exit code 0 không tự chứng minh dữ liệu đúng, đầy đủ hoặc phù hợp với consumer contract. Protocol nền của bài này: Dùng project tối thiểu và fixture có mutations đã biết; compile exact node/branch, execute trong sandbox nếu có, lưu artifacts rồi so key set, typed hashes và business invariants với full/reference computation.

### 7.1. Macro probe 1: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ

**Mệnh đề cần kiểm.** Macro probe 1: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-jinja-macro-boundary`.** Với `Macro probe 1: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ`, Bắt đầu bằng ca nhỏ nhất có thể làm mệnh đề sai; chỉ thêm dữ liệu sau khi failure signal đã xuất hiện đúng chỗ. Cách này phân biệt một assertion có lực với một bài demo chỉ đi qua happy path. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Macro probe 1: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ` phải cho thấy: Giữ fixture tối thiểu, raw failure rows và câu lệnh tái hiện; ảnh chụp màn hình một trạng thái xanh không đủ. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.2. Macro probe 2: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ

**Mệnh đề cần kiểm.** Macro probe 2: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-jinja-macro-boundary`.** Với `Macro probe 2: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ`, Giữ nguyên input rồi đổi đúng một tham số cấu hình liên quan. Nếu output đổi theo nhiều hướng cùng lúc, phép thử chưa cô lập được nguyên nhân và phải thu hẹp lại. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Macro probe 2: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ` phải cho thấy: Báo cả giá trị trước–sau của tham số, compiled artifact và diff đầu ra để reviewer thấy biến nào thực sự đổi. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.3. Macro probe 3: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ

**Mệnh đề cần kiểm.** Macro probe 3: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-jinja-macro-boundary`.** Với `Macro probe 3: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ`, Chạy cặp đối chứng: một input phải được chấp nhận và một input chỉ lệch tại boundary phải bị chặn hoặc được phân loại. Hai ca dùng chung code path để tránh so hai hệ thống khác nhau. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Macro probe 3: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ` phải cho thấy: Pass khi positive control đi qua, negative control dừng đúng lớp và không có side effect ngoài scope. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.4. Macro probe 4: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ

**Mệnh đề cần kiểm.** Macro probe 4: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-jinja-macro-boundary`.** Với `Macro probe 4: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ`, Đặt kill point ngay trước và ngay sau durable boundary. So trạng thái sau restart để biết hệ thống tạo replay có kiểm soát, silent gap hay một trạng thái nửa vời mà dashboard không báo. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Macro probe 4: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ` phải cho thấy: Run ledger phải cho biết commit/checkpoint nào bền vững; sau rerun, key set và side-effect ledger cùng hội tụ. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.5. Macro probe 5: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ

**Mệnh đề cần kiểm.** Macro probe 5: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-jinja-macro-boundary`.** Với `Macro probe 5: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ`, Đảo thứ tự input và thay concurrency nhưng giữ logical population. Kết quả khác nhau cho thấy thiết kế đang phụ thuộc physical order hoặc race thay vì contract đã công bố. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Macro probe 5: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ` phải cho thấy: Hash chuẩn hóa và business totals phải giống nhau giữa các thứ tự; chênh lệch được giữ như finding, không làm tròn mất. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.6. Macro probe 6: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ

**Mệnh đề cần kiểm.** Macro probe 6: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-jinja-macro-boundary`.** Với `Macro probe 6: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ`, Cho cùng logical identity xuất hiện hai lần: trước hết cùng payload, sau đó payload khác. Trường hợp đầu phải hội tụ; trường hợp sau phải lộ collision thay vì âm thầm chọn một bản. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Macro probe 6: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ` phải cho thấy: Same-content replay được đếm nhưng không nhân state; different-content collision có reason code và đường xử lý riêng. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.7. Macro probe 7: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ

**Mệnh đề cần kiểm.** Macro probe 7: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-jinja-macro-boundary`.** Với `Macro probe 7: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ`, Mở rộng fixture bằng một record tới trễ ngay trong horizon và một record nằm ngoài horizon. Ghi rõ record nào được sửa, record nào bị loại và metric nào khiến operator biết có mất coverage. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Macro probe 7: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ` phải cho thấy: Evidence ghi accepted-late, rejected-late và oldest outstanding timestamp; thiếu một nhóm được báo là coverage gap. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.8. Macro probe 8: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ

**Mệnh đề cần kiểm.** Macro probe 8: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-jinja-macro-boundary`.** Với `Macro probe 8: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ`, Dùng một schema change tương thích và một thay đổi phá vỡ key, type hoặc meaning. Kết quả phải chỉ ra khác biệt giữa parse được, chạy được và vẫn giữ đúng semantics. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Macro probe 8: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ` phải cho thấy: Lưu schema trước–sau, classification, compiled SQL và target state; một migration chạy xong nhưng đổi meaning vẫn fail. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.9. Macro probe 9: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ

**Mệnh đề cần kiểm.** Macro probe 9: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-jinja-macro-boundary`.** Với `Macro probe 9: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ`, Tạo bảng rỗng, bảng một row và bảng có duplicate bù cho missing row. Đây là ba ca dễ làm count hoặc aggregate xanh dù invariant thực tế đã hỏng. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Macro probe 9: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ` phải cho thấy: Oracle so count, key multiset và typed hashes. Ca missing-plus-duplicate phải bị phát hiện dù tổng row count không đổi. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.10. Macro probe 10: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ

**Mệnh đề cần kiểm.** Macro probe 10: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-jinja-macro-boundary`.** Với `Macro probe 10: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ`, Cho reviewer chỉ artifacts, không cho xem lời giải thích của tác giả. Nếu họ không dựng lại được input, decision và diff thì evidence package chưa đủ để bàn giao. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Macro probe 10: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ` phải cho thấy: Artifact package đạt khi reviewer tái hiện đúng diff và chỉ ra được limitation mà không cần hỏi tác giả về state ẩn. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.11. Macro probe 11: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ

**Mệnh đề cần kiểm.** Macro probe 11: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-jinja-macro-boundary`.** Với `Macro probe 11: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ`, So output với một cách tính độc lập không tái sử dụng macro, filter hoặc intermediate relation đang được kiểm. Hai phép tính dùng chung lỗi chỉ tạo sự đồng thuận giả. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Macro probe 11: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ` phải cho thấy: Independent result phải khớp ở key/grain đã định; nếu chỉ khớp aggregate cao hơn thì drill-down chưa hoàn tất. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.12. Macro probe 12: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ

**Mệnh đề cần kiểm.** Macro probe 12: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-jinja-macro-boundary`.** Với `Macro probe 12: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ`, Thử trên hai scope: selection hẹp dùng trong CI và population đầy đủ dùng khi phát hành. Ghi phần coverage bị bỏ qua; tốc độ của CI không được biến thành tuyên bố kiểm toàn bộ dữ liệu. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Macro probe 12: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ` phải cho thấy: Kết quả nêu numerator, denominator và excluded nodes/partitions; không dùng từ `all` khi selection không phủ toàn graph. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.13. Macro probe 13: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ

**Mệnh đề cần kiểm.** Macro probe 13: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-jinja-macro-boundary`.** Với `Macro probe 13: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ`, Đẩy một giá trị tới sát giới hạn precision, timezone, partition hoặc threshold. Boundary phải được viết half-open hay inclusive rõ ràng, không suy từ một ví dụ ở giữa khoảng. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Macro probe 13: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ` phải cho thấy: Hai phía của boundary đều có expected result và raw observation. Sai đúng một đơn vị phải làm test fail có chẩn đoán. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.14. Macro probe 14: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ

**Mệnh đề cần kiểm.** Macro probe 14: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-jinja-macro-boundary`.** Với `Macro probe 14: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ`, Thay constraint quan trọng nhất bằng giá trị đủ để decision phải đảo. Nếu thiết kế vẫn đưa cùng lựa chọn mà không giải thích, decision rule đang là khẩu hiệu chứ chưa phải rule. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Macro probe 14: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ` phải cho thấy: ADR hoặc rule chỉ pass khi changed constraint tạo lựa chọn mới đúng như đã dự báo và reversal threshold được lưu. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.15. Macro probe 15: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ

**Mệnh đề cần kiểm.** Macro probe 15: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ.

**Thiết kế phép thử cho `wiki.transformation.dbt-jinja-macro-boundary`.** Với `Macro probe 15: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ`, Lặp lại phép thử từ môi trường sạch bằng seed và versions đã lưu. Một kết quả chỉ tái hiện được trên workspace của tác giả không đủ làm release evidence. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Macro probe 15: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ` phải cho thấy: Lần chạy sạch phải tạo cùng canonical state; khác biệt do timestamp, file order hoặc generated IDs phải được loại hoặc giải thích. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

## 8. Quy trình phản biện

Áp dụng sáu bước sau cho `Jinja and Macros Where Abstraction Stops Paying`; nếu một bước không phù hợp, ghi lý do thay vì bỏ qua im lặng.

1. Với `wiki.transformation.dbt-jinja-macro-boundary`, chốt grain, identity, time boundary và consumer-visible invariant trước câu lệnh.
2. Tách parse/compile state, warehouse execution và publication state.
3. Pin dbt core, adapter, warehouse hoặc orchestrator version cùng configuration có ảnh hưởng.
4. Kiểm correctness bằng key set, typed hash và business invariant trước performance.
5. Chạy negative case, kill point hoặc changed assumption; green path đơn lẻ không đủ.
6. Phân loại source fact, project convention, curriculum synthesis và untested hypothesis.

## 9. Câu hỏi tự kiểm tra

1. `Macro probe 1: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ` sẽ thất bại trước tiên ở boundary nào?
2. Với `Macro probe 2: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ`, artifact nào là nguồn bằng chứng mạnh nhất?
3. Counterexample nhỏ nhất cho `Macro probe 3: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ` gồm những row hoặc state nào?
4. `Macro probe 4: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ` có thể xanh giả trong tình huống nào?
5. Version, adapter, timezone hoặc state nào làm `Macro probe 5: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ` đổi nghĩa?
6. Phần nào của `Macro probe 6: call, compiled SQL, semantic fixture, adapter branch và readability cost phải rõ` hiện mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `Jinja and Macros Where Abstraction Stops Paying` chưa chạy trên warehouse, dbt project hoặc orchestrator production; các mục kiểm chứng vẫn là protocol và expected evidence.
- Các claim gắn `wiki.transformation.dbt-jinja-macro-boundary` phải kiểm lại theo dbt core, adapter, warehouse và scheduler version được chọn.
- Decision matrix, failure campaign và ngưỡng review là curriculum synthesis, không phải cam kết của vendor.
- Note giữ trạng thái `review` cho tới khi chủ dự án duyệt semantic meaning và learner artifact.

## Reference
1. [[SRC-DBT-JINJA-MACROS]]
2. [[SRC-DBT-DATA-TESTS]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-DBT-JINJA-MACROS]] | Cơ chế, contract hoặc giới hạn liên quan | Đã đọc locator; claim theo version/configuration |
| [[SRC-DBT-DATA-TESTS]] | Cơ chế, contract hoặc giới hạn liên quan | Đã đọc locator; claim theo version/configuration |

## Key takeaways
- Macro chỉ đáng giá khi đóng gói policy ổn định mà vẫn để grain và compiled SQL dễ review; DRY quá mức làm tăng incident-debug cost.
- Với `Jinja and Macros Where Abstraction Stops Paying`, compiled intent và observed state phải được lưu tách biệt; trộn hai lớp sẽ che failure window.
- Oracle của bài phải bám câu hỏi trung tâm: Macro nào thật sự loại bỏ một policy lặp lại, và khi nào abstraction che SQL đến mức review, lineage và debugging đắt hơn phần code tiết kiệm?
- Các source IDs `src.web.dbt-jinja-macros, src.web.dbt-data-tests` đặt ranh giới cho claim; phần synthesis không được gán nguyên văn cho vendor.
- Trước khi lab chạy, note này là giáo trình đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule — kiểm chứng `wiki.transformation.dbt-jinja-macro-boundary`

> [!important] Phân loại mệnh đề
> Với `wiki.transformation.dbt-jinja-macro-boundary`, sơ đồ, ví dụ và artifact về **Jinja and Macros Where Abstraction Stops Paying** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.web.dbt-jinja-macros"] --> B["Khóa boundary"]
    B --> M["Cơ chế: Jinja and Macros Where Abstraction Stops Paying"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.transformation.dbt-jinja-macro-boundary` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **Jinja and Macros Where Abstraction Stops Paying**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```sql
-- Verification harness for: Jinja and Macros Where Abstraction Stops Paying
WITH evidence AS (
    SELECT 'wiki.transformation.dbt-jinja-macro-boundary' AS concept_id,
           'boundary_declared' AS check_name, 1 AS passed
    UNION ALL
    SELECT 'wiki.transformation.dbt-jinja-macro-boundary', 'independent_oracle', 1
    UNION ALL
    SELECT 'wiki.transformation.dbt-jinja-macro-boundary', 'reversal_trigger_recorded', 1
)
SELECT concept_id,
       MIN(passed) AS all_hard_checks_pass,
       COUNT(*) AS evidence_items
FROM evidence
GROUP BY concept_id
HAVING MIN(passed) = 1;
```

Artifact của `wiki.transformation.dbt-jinja-macro-boundary` buộc người dùng ghi boundary, oracle và reversal trigger cho **Jinja and Macros Where Abstraction Stops Paying**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

### Tự kiểm tra trước khi tái sử dụng

1. Bạn có thể trả lời `Macro nào thật sự loại bỏ một policy lặp lại, và khi nào abstraction che SQL đến mức review, lineage và debugging đắt hơn phần code tiết kiệm?` bằng một câu mà không kéo thêm concept thứ hai không?
2. Source locator nào đỡ cho claim, và phần nào chỉ là synthesis trong note?
3. Observation nào khiến bạn dừng, thu hẹp hoặc đảo quyết định?
4. Artifact nào cho phép một reviewer độc lập tái hiện kết quả?

<!-- ATOMIC-EXECUTION-CAPSULE:END -->
