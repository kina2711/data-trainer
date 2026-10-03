# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 253: dbt Mental Model Parse Compile Run Build

## Mục tiêu bài học

**Năng lực cần chứng minh.** Phân biệt bốn pha theo đồ thị, hành động và hiện vật, và đọc được câu lệnh SQL đã kết xuất.

**Điều kiện hoàn thành.** Bảng bốn lệnh đúng ở cả ba cột, và câu lệnh kết xuất của một mô hình được đối chiếu đầy đủ với mã nguồn.

> [!abstract] Câu hỏi trung tâm
> Parse, compile, run và build tạo ra graph, SQL, relations và test evidence khác nhau thế nào?

## 1. Project là graph resource

dbt đọc models, sources, tests, snapshots, macros và properties để tạo graph có unique IDs, configs và dependencies. `ref` và `source` vừa resolve relation vừa tạo edge. File tồn tại không đồng nghĩa node enabled; conditional config, target và packages làm graph thay đổi. Manifest là representation của invocation, không phải database truth. Debugging bắt đầu bằng node identity, selection và effective config thay vì chỉ mở SQL file.

## 2. Parse không chạy business SQL

Parse kiểm project structure, render parse-time context và xây manifest. Nó có thể phát hiện YAML, config, reference hoặc macro problems nhưng không chứng minh compiled SQL hợp lệ trên warehouse, quyền tồn tại hay dữ liệu đúng. Partial parsing/cache tối ưu startup và cần xem như versioned state; khi nghi stale, tái tạo clean artifact. Parse success chỉ đóng gate graph/config, không đóng gate execution.

## 3. Compile là executable intent

Compile render Jinja, resolve refs/sources và tạo SQL theo target/adapter context. Đọc compiled output để review predicates, quoting, schema names và macro expansion. Compile có thể cần introspection khi macro gọi warehouse, nên ranh giới không phải luôn offline tuyệt đối. Compiled SQL vẫn chưa chứng minh relation tạo thành công, transaction semantics, row results hay cost. Lưu source SQL cùng compiled artifact và manifest fingerprint.

## 4. Run tạo model relations

`run` thực thi selected models theo DAG và materialization macros; nó không mặc nhiên chạy mọi data test. Node success nói command/materialization hoàn tất, chưa nói business invariant đúng. Hooks, grants và adapter transaction behavior mở thêm failure windows. Selection có thể để upstream/downstream cũ. `run_results` và warehouse query history phải nối được tới invocation và exact compiled code.

## 5. Build phối hợp resource types

`build` chạy resources được chọn gồm models, tests, snapshots hoặc seeds theo graph-aware order và có skip behavior khi upstream fail. Nó tiện cho CI nhưng không thay test design: thiếu test vẫn xanh. Selection semantics quyết định scope. Tách compile failure, execution error, data-test failure, warning và skipped node; một summary pass không đủ để nói toàn project đã được kiểm.

## 6. Four-gate lab

Tạo project nhỏ có ref lỗi, macro compile sai, model runtime error, data invariant fail và downstream node. Chạy parse, compile, run và build trên selection cố định; capture manifest, compiled/run SQL, run_results và relations. Lập bảng command nào phát hiện lỗi nào và lỗi nào lọt qua. Đạt khi learner dự báo đúng artifacts/state trước khi chạy và không nhầm compile success với data correctness.

## 7. Ma trận kiểm chứng từng mệnh đề

Trong `dbt Mental Model Parse Compile Run Build`, mỗi claim phải nối được tới input boundary, compiled hoặc executed artifact, trạng thái trước–sau, failure signal và independent oracle. Một command kết thúc với exit code 0 không tự chứng minh dữ liệu đúng, đầy đủ hoặc phù hợp với consumer contract. Protocol nền của bài này: Dựng fixture và project tối thiểu có exact graph/input boundary; chạy command hoặc protocol theo thứ tự, rồi đối soát relation, key set, typed hash và business invariant với full/reference computation.

### 7.1. dbt-lifecycle probe 1: command, graph scope, artifact, warehouse effect và blind spot phải rõ

**Mệnh đề cần kiểm.** dbt-lifecycle probe 1: command, graph scope, artifact, warehouse effect và blind spot phải rõ.

**Thiết kế phép thử.** Với `dbt-lifecycle probe 1: command, graph scope, artifact, warehouse effect và blind spot phải rõ`, Bắt đầu bằng ca nhỏ nhất có thể làm mệnh đề sai; chỉ thêm dữ liệu sau khi failure signal đã xuất hiện đúng chỗ. Cách này phân biệt một assertion có lực với một bài demo chỉ đi qua happy path. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `dbt-lifecycle probe 1: command, graph scope, artifact, warehouse effect và blind spot phải rõ` phải cho thấy: Giữ fixture tối thiểu, raw failure rows và câu lệnh tái hiện; ảnh chụp màn hình một trạng thái xanh không đủ. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.2. dbt-lifecycle probe 2: command, graph scope, artifact, warehouse effect và blind spot phải rõ

**Mệnh đề cần kiểm.** dbt-lifecycle probe 2: command, graph scope, artifact, warehouse effect và blind spot phải rõ.

**Thiết kế phép thử.** Với `dbt-lifecycle probe 2: command, graph scope, artifact, warehouse effect và blind spot phải rõ`, Giữ nguyên input rồi đổi đúng một tham số cấu hình liên quan. Nếu output đổi theo nhiều hướng cùng lúc, phép thử chưa cô lập được nguyên nhân và phải thu hẹp lại. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `dbt-lifecycle probe 2: command, graph scope, artifact, warehouse effect và blind spot phải rõ` phải cho thấy: Báo cả giá trị trước–sau của tham số, compiled artifact và diff đầu ra để reviewer thấy biến nào thực sự đổi. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.3. dbt-lifecycle probe 3: command, graph scope, artifact, warehouse effect và blind spot phải rõ

**Mệnh đề cần kiểm.** dbt-lifecycle probe 3: command, graph scope, artifact, warehouse effect và blind spot phải rõ.

**Thiết kế phép thử.** Với `dbt-lifecycle probe 3: command, graph scope, artifact, warehouse effect và blind spot phải rõ`, Chạy cặp đối chứng: một input phải được chấp nhận và một input chỉ lệch tại boundary phải bị chặn hoặc được phân loại. Hai ca dùng chung code path để tránh so hai hệ thống khác nhau. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `dbt-lifecycle probe 3: command, graph scope, artifact, warehouse effect và blind spot phải rõ` phải cho thấy: Pass khi positive control đi qua, negative control dừng đúng lớp và không có side effect ngoài scope. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.4. dbt-lifecycle probe 4: command, graph scope, artifact, warehouse effect và blind spot phải rõ

**Mệnh đề cần kiểm.** dbt-lifecycle probe 4: command, graph scope, artifact, warehouse effect và blind spot phải rõ.

**Thiết kế phép thử.** Với `dbt-lifecycle probe 4: command, graph scope, artifact, warehouse effect và blind spot phải rõ`, Đặt kill point ngay trước và ngay sau durable boundary. So trạng thái sau restart để biết hệ thống tạo replay có kiểm soát, silent gap hay một trạng thái nửa vời mà dashboard không báo. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `dbt-lifecycle probe 4: command, graph scope, artifact, warehouse effect và blind spot phải rõ` phải cho thấy: Run ledger phải cho biết commit/checkpoint nào bền vững; sau rerun, key set và side-effect ledger cùng hội tụ. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.5. dbt-lifecycle probe 5: command, graph scope, artifact, warehouse effect và blind spot phải rõ

**Mệnh đề cần kiểm.** dbt-lifecycle probe 5: command, graph scope, artifact, warehouse effect và blind spot phải rõ.

**Thiết kế phép thử.** Với `dbt-lifecycle probe 5: command, graph scope, artifact, warehouse effect và blind spot phải rõ`, Đảo thứ tự input và thay concurrency nhưng giữ logical population. Kết quả khác nhau cho thấy thiết kế đang phụ thuộc physical order hoặc race thay vì contract đã công bố. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `dbt-lifecycle probe 5: command, graph scope, artifact, warehouse effect và blind spot phải rõ` phải cho thấy: Hash chuẩn hóa và business totals phải giống nhau giữa các thứ tự; chênh lệch được giữ như finding, không làm tròn mất. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.6. dbt-lifecycle probe 6: command, graph scope, artifact, warehouse effect và blind spot phải rõ

**Mệnh đề cần kiểm.** dbt-lifecycle probe 6: command, graph scope, artifact, warehouse effect và blind spot phải rõ.

**Thiết kế phép thử.** Với `dbt-lifecycle probe 6: command, graph scope, artifact, warehouse effect và blind spot phải rõ`, Cho cùng logical identity xuất hiện hai lần: trước hết cùng payload, sau đó payload khác. Trường hợp đầu phải hội tụ; trường hợp sau phải lộ collision thay vì âm thầm chọn một bản. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `dbt-lifecycle probe 6: command, graph scope, artifact, warehouse effect và blind spot phải rõ` phải cho thấy: Same-content replay được đếm nhưng không nhân state; different-content collision có reason code và đường xử lý riêng. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.7. dbt-lifecycle probe 7: command, graph scope, artifact, warehouse effect và blind spot phải rõ

**Mệnh đề cần kiểm.** dbt-lifecycle probe 7: command, graph scope, artifact, warehouse effect và blind spot phải rõ.

**Thiết kế phép thử.** Với `dbt-lifecycle probe 7: command, graph scope, artifact, warehouse effect và blind spot phải rõ`, Mở rộng fixture bằng một record tới trễ ngay trong horizon và một record nằm ngoài horizon. Ghi rõ record nào được sửa, record nào bị loại và metric nào khiến operator biết có mất coverage. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `dbt-lifecycle probe 7: command, graph scope, artifact, warehouse effect và blind spot phải rõ` phải cho thấy: Evidence ghi accepted-late, rejected-late và oldest outstanding timestamp; thiếu một nhóm được báo là coverage gap. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.8. dbt-lifecycle probe 8: command, graph scope, artifact, warehouse effect và blind spot phải rõ

**Mệnh đề cần kiểm.** dbt-lifecycle probe 8: command, graph scope, artifact, warehouse effect và blind spot phải rõ.

**Thiết kế phép thử.** Với `dbt-lifecycle probe 8: command, graph scope, artifact, warehouse effect và blind spot phải rõ`, Dùng một schema change tương thích và một thay đổi phá vỡ key, type hoặc meaning. Kết quả phải chỉ ra khác biệt giữa parse được, chạy được và vẫn giữ đúng semantics. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `dbt-lifecycle probe 8: command, graph scope, artifact, warehouse effect và blind spot phải rõ` phải cho thấy: Lưu schema trước–sau, classification, compiled SQL và target state; một migration chạy xong nhưng đổi meaning vẫn fail. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.9. dbt-lifecycle probe 9: command, graph scope, artifact, warehouse effect và blind spot phải rõ

**Mệnh đề cần kiểm.** dbt-lifecycle probe 9: command, graph scope, artifact, warehouse effect và blind spot phải rõ.

**Thiết kế phép thử.** Với `dbt-lifecycle probe 9: command, graph scope, artifact, warehouse effect và blind spot phải rõ`, Tạo bảng rỗng, bảng một row và bảng có duplicate bù cho missing row. Đây là ba ca dễ làm count hoặc aggregate xanh dù invariant thực tế đã hỏng. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `dbt-lifecycle probe 9: command, graph scope, artifact, warehouse effect và blind spot phải rõ` phải cho thấy: Oracle so count, key multiset và typed hashes. Ca missing-plus-duplicate phải bị phát hiện dù tổng row count không đổi. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.10. dbt-lifecycle probe 10: command, graph scope, artifact, warehouse effect và blind spot phải rõ

**Mệnh đề cần kiểm.** dbt-lifecycle probe 10: command, graph scope, artifact, warehouse effect và blind spot phải rõ.

**Thiết kế phép thử.** Với `dbt-lifecycle probe 10: command, graph scope, artifact, warehouse effect và blind spot phải rõ`, Cho reviewer chỉ artifacts, không cho xem lời giải thích của tác giả. Nếu họ không dựng lại được input, decision và diff thì evidence package chưa đủ để bàn giao. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `dbt-lifecycle probe 10: command, graph scope, artifact, warehouse effect và blind spot phải rõ` phải cho thấy: Artifact package đạt khi reviewer tái hiện đúng diff và chỉ ra được limitation mà không cần hỏi tác giả về state ẩn. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.11. dbt-lifecycle probe 11: command, graph scope, artifact, warehouse effect và blind spot phải rõ

**Mệnh đề cần kiểm.** dbt-lifecycle probe 11: command, graph scope, artifact, warehouse effect và blind spot phải rõ.

**Thiết kế phép thử.** Với `dbt-lifecycle probe 11: command, graph scope, artifact, warehouse effect và blind spot phải rõ`, So output với một cách tính độc lập không tái sử dụng macro, filter hoặc intermediate relation đang được kiểm. Hai phép tính dùng chung lỗi chỉ tạo sự đồng thuận giả. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `dbt-lifecycle probe 11: command, graph scope, artifact, warehouse effect và blind spot phải rõ` phải cho thấy: Independent result phải khớp ở key/grain đã định; nếu chỉ khớp aggregate cao hơn thì drill-down chưa hoàn tất. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.12. dbt-lifecycle probe 12: command, graph scope, artifact, warehouse effect và blind spot phải rõ

**Mệnh đề cần kiểm.** dbt-lifecycle probe 12: command, graph scope, artifact, warehouse effect và blind spot phải rõ.

**Thiết kế phép thử.** Với `dbt-lifecycle probe 12: command, graph scope, artifact, warehouse effect và blind spot phải rõ`, Thử trên hai scope: selection hẹp dùng trong CI và population đầy đủ dùng khi phát hành. Ghi phần coverage bị bỏ qua; tốc độ của CI không được biến thành tuyên bố kiểm toàn bộ dữ liệu. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `dbt-lifecycle probe 12: command, graph scope, artifact, warehouse effect và blind spot phải rõ` phải cho thấy: Kết quả nêu numerator, denominator và excluded nodes/partitions; không dùng từ `all` khi selection không phủ toàn graph. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.13. dbt-lifecycle probe 13: command, graph scope, artifact, warehouse effect và blind spot phải rõ

**Mệnh đề cần kiểm.** dbt-lifecycle probe 13: command, graph scope, artifact, warehouse effect và blind spot phải rõ.

**Thiết kế phép thử.** Với `dbt-lifecycle probe 13: command, graph scope, artifact, warehouse effect và blind spot phải rõ`, Đẩy một giá trị tới sát giới hạn precision, timezone, partition hoặc threshold. Boundary phải được viết half-open hay inclusive rõ ràng, không suy từ một ví dụ ở giữa khoảng. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `dbt-lifecycle probe 13: command, graph scope, artifact, warehouse effect và blind spot phải rõ` phải cho thấy: Hai phía của boundary đều có expected result và raw observation. Sai đúng một đơn vị phải làm test fail có chẩn đoán. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.14. dbt-lifecycle probe 14: command, graph scope, artifact, warehouse effect và blind spot phải rõ

**Mệnh đề cần kiểm.** dbt-lifecycle probe 14: command, graph scope, artifact, warehouse effect và blind spot phải rõ.

**Thiết kế phép thử.** Với `dbt-lifecycle probe 14: command, graph scope, artifact, warehouse effect và blind spot phải rõ`, Thay constraint quan trọng nhất bằng giá trị đủ để decision phải đảo. Nếu thiết kế vẫn đưa cùng lựa chọn mà không giải thích, decision rule đang là khẩu hiệu chứ chưa phải rule. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `dbt-lifecycle probe 14: command, graph scope, artifact, warehouse effect và blind spot phải rõ` phải cho thấy: ADR hoặc rule chỉ pass khi changed constraint tạo lựa chọn mới đúng như đã dự báo và reversal threshold được lưu. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.15. dbt-lifecycle probe 15: command, graph scope, artifact, warehouse effect và blind spot phải rõ

**Mệnh đề cần kiểm.** dbt-lifecycle probe 15: command, graph scope, artifact, warehouse effect và blind spot phải rõ.

**Thiết kế phép thử.** Với `dbt-lifecycle probe 15: command, graph scope, artifact, warehouse effect và blind spot phải rõ`, Lặp lại phép thử từ môi trường sạch bằng seed và versions đã lưu. Một kết quả chỉ tái hiện được trên workspace của tác giả không đủ làm release evidence. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `dbt-lifecycle probe 15: command, graph scope, artifact, warehouse effect và blind spot phải rõ` phải cho thấy: Lần chạy sạch phải tạo cùng canonical state; khác biệt do timestamp, file order hoặc generated IDs phải được loại hoặc giải thích. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

## 8. Quy trình phản biện

Áp dụng sáu bước sau cho `dbt Mental Model Parse Compile Run Build`; nếu một bước không phù hợp, ghi lý do thay vì bỏ qua im lặng.

1. Với `wiki.transformation.dbt-parse-compile-run-build`, chốt grain, identity, time boundary và consumer-visible invariant trước câu lệnh.
2. Tách parse/compile state, warehouse execution và publication state.
3. Pin dbt core, adapter, warehouse hoặc orchestrator version cùng configuration có ảnh hưởng.
4. Kiểm correctness bằng key set, typed hash và business invariant trước performance.
5. Chạy negative case, kill point hoặc changed assumption; green path đơn lẻ không đủ.
6. Phân loại source fact, project convention, curriculum synthesis và untested hypothesis.

## 9. Câu hỏi tự kiểm tra

1. `dbt-lifecycle probe 1: command, graph scope, artifact, warehouse effect và blind spot phải rõ` sẽ thất bại trước tiên ở boundary nào?
2. Với `dbt-lifecycle probe 2: command, graph scope, artifact, warehouse effect và blind spot phải rõ`, artifact nào là nguồn bằng chứng mạnh nhất?
3. Counterexample nhỏ nhất cho `dbt-lifecycle probe 3: command, graph scope, artifact, warehouse effect và blind spot phải rõ` gồm những row hoặc state nào?
4. `dbt-lifecycle probe 4: command, graph scope, artifact, warehouse effect và blind spot phải rõ` có thể xanh giả trong tình huống nào?
5. Version, adapter, timezone hoặc state nào làm `dbt-lifecycle probe 5: command, graph scope, artifact, warehouse effect và blind spot phải rõ` đổi nghĩa?
6. Phần nào của `dbt-lifecycle probe 6: command, graph scope, artifact, warehouse effect và blind spot phải rõ` hiện mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `dbt Mental Model Parse Compile Run Build` chưa chạy trên warehouse, dbt project hoặc orchestrator production; các mục kiểm chứng vẫn là protocol và expected evidence.
- Các claim gắn `wiki.transformation.dbt-parse-compile-run-build` phải kiểm lại theo dbt core, adapter, warehouse và scheduler version được chọn.
- Decision matrix, failure campaign và ngưỡng review là curriculum synthesis, không phải cam kết của vendor.
- Note giữ trạng thái `review` cho tới khi chủ dự án duyệt semantic meaning và learner artifact.

## Reference
1. [[SRC-DBT-COMMAND-REFERENCE]]
2. [[SRC-DBT-MATERIALIZATIONS]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-DBT-COMMAND-REFERENCE]] | Cơ chế, contract hoặc giới hạn liên quan | Đã đọc locator; claim theo version/configuration |
| [[SRC-DBT-MATERIALIZATIONS]] | Cơ chế, contract hoặc giới hạn liên quan | Đã đọc locator; claim theo version/configuration |

## Key takeaways
- Parse xây graph, compile tạo executable intent, run tạo relations và build phối hợp resources/tests; mỗi command đóng một gate khác nhau và có blind spot riêng.
- Với `dbt Mental Model Parse Compile Run Build`, compiled intent và observed state phải được lưu tách biệt; trộn hai lớp sẽ che failure window.
- Oracle của bài phải bám câu hỏi trung tâm: Parse, compile, run và build tạo ra graph, SQL, relations và test evidence khác nhau thế nào?
- Các source IDs `src.web.dbt-command-reference, src.web.dbt-materializations` đặt ranh giới cho claim; phần synthesis không được gán nguyên văn cho vendor.
- Trước khi lab chạy, note này là giáo trình đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.
