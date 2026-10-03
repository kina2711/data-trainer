# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 265: Documentation Exposures and Lineage Artifacts

## Mục tiêu bài học

**Năng lực cần chứng minh.** Khai báo tài liệu và bên tiêu thụ đầy đủ, và chặn được mô hình công khai thiếu tài liệu ở cửa hợp nhất.

**Điều kiện hoàn thành.** Ba vi phạm bị chặn ở cửa hợp nhất, và dòng dõi trả lời được câu hỏi ảnh hưởng từ một cột nguồn tới bảng điều khiển.

> [!abstract] Câu hỏi trung tâm
> Documentation, exposures và lineage artifacts cần kết hợp thế nào để người dùng tìm đúng owner, meaning, dependency và freshness thay vì chỉ xem một DAG đẹp?

## 1. Documentation là contract cho người đọc

Model/column/source descriptions nói grain, key, meaning, unit/timezone, update/delete behavior, freshness, limitations và owner. Docs block tái dùng long-form explanation nhưng không được biến thành copy chung vô nghĩa. Warehouse introspection có thể liệt kê cột chưa được mô tả; “xuất hiện trong docs” khác “được document”. Coverage check cần denominator và criticality, không chỉ phần trăm tổng.

## 2. Exposure nối tới consumption

Exposure mô tả dashboard, notebook, analysis, ML hay application downstream, cùng owner và declared dependencies. Nó giúp select/test ancestors và làm blast-radius visible. Manual exposure stale nếu owner không cập nhật; automatic exposure phụ thuộc integration/metadata coverage. URL/maturity không chứng minh usage hoặc correctness. So declared exposures với query/BI inventory và ghi unknown consumers.

## 3. Lineage có nhiều lớp

Graph lineage từ `ref`/`source` mô tả declared resource edges; compiled SQL/static analysis có thể bổ sung column lineage; warehouse query history thấy observed consumption. Dynamic SQL, external tools, copied tables và manual exports tạo gaps. Một DAG model-level không cho biết column meaning hay runtime freshness. Report lineage confidence/source và timestamp, không vẽ một đồ thị rồi gọi complete.

## 4. Artifact generation và freshness

Generated docs/artifacts thuộc exact project parse/compile/run and warehouse state. Pin invocation/version/target, publish immutable build or fingerprint, and refresh cadence. Stale docs nguy hiểm hơn no docs khi relation changed. CI checks missing descriptions, owners, tests/exposures and broken links; production job generates metadata after successful state. Secrets/PII samples không đi vào descriptions/artifacts.

## 5. Impact analysis

Khi column/model đổi, combine manifest parent/child edges, exposures, version refs, query history và owner confirmation. Rank critical consumers; absence from one source is not zero impact. Produce change dossier with affected nodes, unknowns, migration owners and evidence date. Test selection based lineage then validates representative downstream outputs. Documentation alone không thay consumer acceptance.

## 6. Retrieval lab

Đưa cho reviewer ba câu hỏi: dataset này có grain/owner gì; dashboard nào phụ thuộc; column đổi sẽ ảnh hưởng đâu. Họ chỉ dùng generated docs/artifacts and exposure inventory. Measure answer correctness/time and missing edges. Inject stale description, undeclared BI query and dynamic dependency. Đạt khi system signals uncertainty instead of confidently returning incomplete lineage.

## 7. Ma trận kiểm chứng từng mệnh đề

Trong `Documentation Exposures and Lineage Artifacts`, mỗi claim phải nối được tới input boundary, compiled hoặc executed artifact, trạng thái trước–sau, failure signal và independent oracle. Một command kết thúc với exit code 0 không tự chứng minh dữ liệu đúng, đầy đủ hoặc phù hợp với consumer contract. Protocol nền của bài này: Dùng project/fixture nhỏ có exact boundary và owner; capture source, compiled/runtime artifacts, relations và consumer-facing diff; đối soát bằng alternate computation hoặc inventory độc lập.

### 7.1. Documentation probe 1: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ

**Mệnh đề cần kiểm.** Documentation probe 1: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ.

**Thiết kế phép thử.** Với `Documentation probe 1: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ`, Bắt đầu bằng ca nhỏ nhất có thể làm mệnh đề sai; chỉ thêm dữ liệu sau khi failure signal đã xuất hiện đúng chỗ. Cách này phân biệt một assertion có lực với một bài demo chỉ đi qua happy path. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Documentation probe 1: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ` phải cho thấy: Giữ fixture tối thiểu, raw failure rows và câu lệnh tái hiện; ảnh chụp màn hình một trạng thái xanh không đủ. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.2. Documentation probe 2: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ

**Mệnh đề cần kiểm.** Documentation probe 2: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ.

**Thiết kế phép thử.** Với `Documentation probe 2: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ`, Giữ nguyên input rồi đổi đúng một tham số cấu hình liên quan. Nếu output đổi theo nhiều hướng cùng lúc, phép thử chưa cô lập được nguyên nhân và phải thu hẹp lại. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Documentation probe 2: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ` phải cho thấy: Báo cả giá trị trước–sau của tham số, compiled artifact và diff đầu ra để reviewer thấy biến nào thực sự đổi. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.3. Documentation probe 3: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ

**Mệnh đề cần kiểm.** Documentation probe 3: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ.

**Thiết kế phép thử.** Với `Documentation probe 3: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ`, Chạy cặp đối chứng: một input phải được chấp nhận và một input chỉ lệch tại boundary phải bị chặn hoặc được phân loại. Hai ca dùng chung code path để tránh so hai hệ thống khác nhau. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Documentation probe 3: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ` phải cho thấy: Pass khi positive control đi qua, negative control dừng đúng lớp và không có side effect ngoài scope. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.4. Documentation probe 4: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ

**Mệnh đề cần kiểm.** Documentation probe 4: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ.

**Thiết kế phép thử.** Với `Documentation probe 4: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ`, Đặt kill point ngay trước và ngay sau durable boundary. So trạng thái sau restart để biết hệ thống tạo replay có kiểm soát, silent gap hay một trạng thái nửa vời mà dashboard không báo. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Documentation probe 4: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ` phải cho thấy: Run ledger phải cho biết commit/checkpoint nào bền vững; sau rerun, key set và side-effect ledger cùng hội tụ. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.5. Documentation probe 5: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ

**Mệnh đề cần kiểm.** Documentation probe 5: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ.

**Thiết kế phép thử.** Với `Documentation probe 5: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ`, Đảo thứ tự input và thay concurrency nhưng giữ logical population. Kết quả khác nhau cho thấy thiết kế đang phụ thuộc physical order hoặc race thay vì contract đã công bố. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Documentation probe 5: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ` phải cho thấy: Hash chuẩn hóa và business totals phải giống nhau giữa các thứ tự; chênh lệch được giữ như finding, không làm tròn mất. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.6. Documentation probe 6: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ

**Mệnh đề cần kiểm.** Documentation probe 6: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ.

**Thiết kế phép thử.** Với `Documentation probe 6: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ`, Cho cùng logical identity xuất hiện hai lần: trước hết cùng payload, sau đó payload khác. Trường hợp đầu phải hội tụ; trường hợp sau phải lộ collision thay vì âm thầm chọn một bản. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Documentation probe 6: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ` phải cho thấy: Same-content replay được đếm nhưng không nhân state; different-content collision có reason code và đường xử lý riêng. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.7. Documentation probe 7: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ

**Mệnh đề cần kiểm.** Documentation probe 7: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ.

**Thiết kế phép thử.** Với `Documentation probe 7: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ`, Mở rộng fixture bằng một record tới trễ ngay trong horizon và một record nằm ngoài horizon. Ghi rõ record nào được sửa, record nào bị loại và metric nào khiến operator biết có mất coverage. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Documentation probe 7: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ` phải cho thấy: Evidence ghi accepted-late, rejected-late và oldest outstanding timestamp; thiếu một nhóm được báo là coverage gap. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.8. Documentation probe 8: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ

**Mệnh đề cần kiểm.** Documentation probe 8: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ.

**Thiết kế phép thử.** Với `Documentation probe 8: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ`, Dùng một schema change tương thích và một thay đổi phá vỡ key, type hoặc meaning. Kết quả phải chỉ ra khác biệt giữa parse được, chạy được và vẫn giữ đúng semantics. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Documentation probe 8: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ` phải cho thấy: Lưu schema trước–sau, classification, compiled SQL và target state; một migration chạy xong nhưng đổi meaning vẫn fail. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.9. Documentation probe 9: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ

**Mệnh đề cần kiểm.** Documentation probe 9: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ.

**Thiết kế phép thử.** Với `Documentation probe 9: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ`, Tạo bảng rỗng, bảng một row và bảng có duplicate bù cho missing row. Đây là ba ca dễ làm count hoặc aggregate xanh dù invariant thực tế đã hỏng. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Documentation probe 9: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ` phải cho thấy: Oracle so count, key multiset và typed hashes. Ca missing-plus-duplicate phải bị phát hiện dù tổng row count không đổi. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.10. Documentation probe 10: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ

**Mệnh đề cần kiểm.** Documentation probe 10: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ.

**Thiết kế phép thử.** Với `Documentation probe 10: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ`, Cho reviewer chỉ artifacts, không cho xem lời giải thích của tác giả. Nếu họ không dựng lại được input, decision và diff thì evidence package chưa đủ để bàn giao. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Documentation probe 10: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ` phải cho thấy: Artifact package đạt khi reviewer tái hiện đúng diff và chỉ ra được limitation mà không cần hỏi tác giả về state ẩn. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.11. Documentation probe 11: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ

**Mệnh đề cần kiểm.** Documentation probe 11: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ.

**Thiết kế phép thử.** Với `Documentation probe 11: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ`, So output với một cách tính độc lập không tái sử dụng macro, filter hoặc intermediate relation đang được kiểm. Hai phép tính dùng chung lỗi chỉ tạo sự đồng thuận giả. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Documentation probe 11: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ` phải cho thấy: Independent result phải khớp ở key/grain đã định; nếu chỉ khớp aggregate cao hơn thì drill-down chưa hoàn tất. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.12. Documentation probe 12: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ

**Mệnh đề cần kiểm.** Documentation probe 12: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ.

**Thiết kế phép thử.** Với `Documentation probe 12: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ`, Thử trên hai scope: selection hẹp dùng trong CI và population đầy đủ dùng khi phát hành. Ghi phần coverage bị bỏ qua; tốc độ của CI không được biến thành tuyên bố kiểm toàn bộ dữ liệu. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Documentation probe 12: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ` phải cho thấy: Kết quả nêu numerator, denominator và excluded nodes/partitions; không dùng từ `all` khi selection không phủ toàn graph. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.13. Documentation probe 13: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ

**Mệnh đề cần kiểm.** Documentation probe 13: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ.

**Thiết kế phép thử.** Với `Documentation probe 13: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ`, Đẩy một giá trị tới sát giới hạn precision, timezone, partition hoặc threshold. Boundary phải được viết half-open hay inclusive rõ ràng, không suy từ một ví dụ ở giữa khoảng. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Documentation probe 13: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ` phải cho thấy: Hai phía của boundary đều có expected result và raw observation. Sai đúng một đơn vị phải làm test fail có chẩn đoán. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.14. Documentation probe 14: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ

**Mệnh đề cần kiểm.** Documentation probe 14: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ.

**Thiết kế phép thử.** Với `Documentation probe 14: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ`, Thay constraint quan trọng nhất bằng giá trị đủ để decision phải đảo. Nếu thiết kế vẫn đưa cùng lựa chọn mà không giải thích, decision rule đang là khẩu hiệu chứ chưa phải rule. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Documentation probe 14: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ` phải cho thấy: ADR hoặc rule chỉ pass khi changed constraint tạo lựa chọn mới đúng như đã dự báo và reversal threshold được lưu. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.15. Documentation probe 15: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ

**Mệnh đề cần kiểm.** Documentation probe 15: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ.

**Thiết kế phép thử.** Với `Documentation probe 15: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ`, Lặp lại phép thử từ môi trường sạch bằng seed và versions đã lưu. Một kết quả chỉ tái hiện được trên workspace của tác giả không đủ làm release evidence. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Documentation probe 15: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ` phải cho thấy: Lần chạy sạch phải tạo cùng canonical state; khác biệt do timestamp, file order hoặc generated IDs phải được loại hoặc giải thích. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

## 8. Quy trình phản biện

Áp dụng sáu bước sau cho `Documentation Exposures and Lineage Artifacts`; nếu một bước không phù hợp, ghi lý do thay vì bỏ qua im lặng.

1. Với `wiki.transformation.documentation-exposures-lineage`, chốt grain, identity, time boundary và consumer-visible invariant trước câu lệnh.
2. Tách parse/compile state, warehouse execution và publication state.
3. Pin dbt core, adapter, warehouse hoặc orchestrator version cùng configuration có ảnh hưởng.
4. Kiểm correctness bằng key set, typed hash và business invariant trước performance.
5. Chạy negative case, kill point hoặc changed assumption; green path đơn lẻ không đủ.
6. Phân loại source fact, project convention, curriculum synthesis và untested hypothesis.

## 9. Câu hỏi tự kiểm tra

1. `Documentation probe 1: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ` sẽ thất bại trước tiên ở boundary nào?
2. Với `Documentation probe 2: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ`, artifact nào là nguồn bằng chứng mạnh nhất?
3. Counterexample nhỏ nhất cho `Documentation probe 3: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ` gồm những row hoặc state nào?
4. `Documentation probe 4: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ` có thể xanh giả trong tình huống nào?
5. Version, adapter, timezone hoặc state nào làm `Documentation probe 5: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ` đổi nghĩa?
6. Phần nào của `Documentation probe 6: retrieval question, metadata source, freshness, missing edge và owner evidence phải rõ` hiện mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `Documentation Exposures and Lineage Artifacts` chưa chạy trên warehouse, dbt project hoặc orchestrator production; các mục kiểm chứng vẫn là protocol và expected evidence.
- Các claim gắn `wiki.transformation.documentation-exposures-lineage` phải kiểm lại theo dbt core, adapter, warehouse và scheduler version được chọn.
- Decision matrix, failure campaign và ngưỡng review là curriculum synthesis, không phải cam kết của vendor.
- Note giữ trạng thái `review` cho tới khi chủ dự án duyệt semantic meaning và learner artifact.

## Reference
1. [[SRC-DBT-DOCUMENTATION]]
2. [[SRC-DBT-EXPOSURES]]
3. [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-DBT-DOCUMENTATION]] | Cơ chế, contract hoặc giới hạn liên quan | Đã đọc locator; claim theo version/configuration |
| [[SRC-DBT-EXPOSURES]] | Cơ chế, contract hoặc giới hạn liên quan | Đã đọc locator; claim theo version/configuration |
| [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]] | Cơ chế, contract hoặc giới hạn liên quan | Đã đọc locator; claim theo version/configuration |

## Key takeaways
- Documentation, exposure và lineage chỉ hữu ích khi có owner, freshness và confidence; một DAG đẹp không chứng minh dependency coverage hoàn chỉnh.
- Với `Documentation Exposures and Lineage Artifacts`, compiled intent và observed state phải được lưu tách biệt; trộn hai lớp sẽ che failure window.
- Oracle của bài phải bám câu hỏi trung tâm: Documentation, exposures và lineage artifacts cần kết hợp thế nào để người dùng tìm đúng owner, meaning, dependency và freshness thay vì chỉ xem một DAG đẹp?
- Các source IDs `src.web.dbt-documentation, src.web.dbt-exposures, src.book.reis-housley-fundamentals-data-engineering` đặt ranh giới cho claim; phần synthesis không được gán nguyên văn cho vendor.
- Trước khi lab chạy, note này là giáo trình đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.
