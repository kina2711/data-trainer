# Phase 5: Modeling, Semantics and Analytical Product
# Module 12: Semantic Layer and Metrics Engineering
# Lesson 174: Semantic Models in MetricFlow

## Mục tiêu bài học

**Năng lực cần chứng minh.** Khai báo mô hình ngữ nghĩa cho ba bảng mart sao cho mọi khai báo truy được về hợp đồng.

**Điều kiện hoàn thành.** Ba mô hình biên dịch sạch, và mọi độ đo cùng chiều dẫn được về một dòng cụ thể trong hợp đồng.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào ánh xạ mart và metric contracts vào MetricFlow hiện hành, validate cấu hình và giữ traceability mà không trộn legacy spec?

## 1. Khóa version và môi trường

MetricFlow commands/syntax khác giữa dbt platform v1/v2 và self-hosted. Trước khi viết YAML, ghi dbt engine, release track, MetricFlow version, adapter/warehouse và command prefix. Current spec đặt semantic annotations trong model YAML và simple metrics mang aggregation/expression; legacy examples dùng semantic_models/measures/type_params khác. Không trộn hai spec trong một bài.

## 2. Nền là mart đã kiểm

Semantic model trỏ tới dbt model/mart có declared grain, keys, time và quality tests. Đặt trên raw events buộc semantic layer gánh deduplication, identity resolution và unstable schema; config compile vẫn có thể cho số sai. Mỗi semantic node có lineage về mart contract và source. Nếu một mart chứa multiple grains, nên sửa mart hoặc tách semantic exposure trước khi khai metrics.

## 3. Entities

Entities biểu diễn identifiers/traversal points với primary/unique/foreign roles theo current product concepts. Type phải khớp actual uniqueness/cardinality; primary label không tạo constraint trong warehouse. Test duplicates/nulls và temporal uniqueness ở mart. Same-named entity qua models phải cùng meaning/namespace hoặc có mapping rõ. Intentionally role-playing identities cần distinct semantic names.

## 4. Dimensions và time

Categorical dimensions có business meaning/domain; time dimensions có granularity và timezone semantics. Model có metrics cần aggregation time dimension theo current documentation, metric có thể override khi contract cho phép. Derived semantics/expression chỉ dùng khi không làm ẩn transform phức tạp cần test ở mart. Dimension availability được suy theo graph; presence trong table không tự làm nó queryable với mọi metric.

## 5. Simple và advanced metrics

Current simple metric gắn aggregation/expression nơi dữ liệu nằm; ratio/derived/cumulative cross-model metrics có dependencies riêng. Contract mapping table phải nối population/filter/grain/time/aggregation/owner với exact YAML fields hoặc external governance field. Nếu product không có field cho owner/interpretation limit, lưu adjacent governed metadata và giữ common ID; không bỏ khỏi contract.

## 6. Validate theo nhiều tầng

`dbt parse` cập nhật semantic artifacts; command validate kiểm semantic configuration và một số warehouse checks tùy environment. Sau đó list metrics/dimensions/entities, compile representative queries và chạy oracle reconciliation. Parse/validate clean chỉ là schema/config gate. Cố ý wrong entity type, missing time config và invalid dependency để ghi actual diagnostics của exact version.

## 7. Traceability ba mart

Cho mỗi entity/dimension/simple metric, ghi contract section, mart column/expression, tests và owner. Ba mart phải cover direct fact, role-playing dimension và a second fact to expose path constraints. Review generated semantic manifest/OSI artifact khi applicable. Secret/token không đưa vào note; command transcript phải redact credentials và warehouse identifiers nếu sensitive.

## 8. Ma trận kiểm chứng từng mệnh đề

Mọi mệnh đề dưới đây cần fixture, invariant, independent oracle và output lưu được. Compile thành công hoặc con số nhìn hợp lý không đủ làm bằng chứng.

### 8.1. environment/version phải được ghi trước syntax

**Mệnh đề cần kiểm.** environment/version phải được ghi trước syntax.

**Cách kiểm.** Khóa environment/version, map three tested marts sang current spec, chạy parse/validate/list/compile phù hợp môi trường và negative config cases. Reconcile representative metrics với independent oracle. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.2. current và legacy spec không được trộn

**Mệnh đề cần kiểm.** current và legacy spec không được trộn.

**Cách kiểm.** Khóa environment/version, map three tested marts sang current spec, chạy parse/validate/list/compile phù hợp môi trường và negative config cases. Reconcile representative metrics với independent oracle. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.3. semantic model nên đặt trên tested mart

**Mệnh đề cần kiểm.** semantic model nên đặt trên tested mart.

**Cách kiểm.** Khóa environment/version, map three tested marts sang current spec, chạy parse/validate/list/compile phù hợp môi trường và negative config cases. Reconcile representative metrics với independent oracle. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.4. primary entity label không tạo database uniqueness

**Mệnh đề cần kiểm.** primary entity label không tạo database uniqueness.

**Cách kiểm.** Khóa environment/version, map three tested marts sang current spec, chạy parse/validate/list/compile phù hợp môi trường và negative config cases. Reconcile representative metrics với independent oracle. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.5. entity type cần data test

**Mệnh đề cần kiểm.** entity type cần data test.

**Cách kiểm.** Khóa environment/version, map three tested marts sang current spec, chạy parse/validate/list/compile phù hợp môi trường và negative config cases. Reconcile representative metrics với independent oracle. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.6. role-playing entities cần semantic names

**Mệnh đề cần kiểm.** role-playing entities cần semantic names.

**Cách kiểm.** Khóa environment/version, map three tested marts sang current spec, chạy parse/validate/list/compile phù hợp môi trường và negative config cases. Reconcile representative metrics với independent oracle. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.7. time dimension phải trace về contract role

**Mệnh đề cần kiểm.** time dimension phải trace về contract role.

**Cách kiểm.** Khóa environment/version, map three tested marts sang current spec, chạy parse/validate/list/compile phù hợp môi trường và negative config cases. Reconcile representative metrics với independent oracle. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.8. dimension presence không đồng nghĩa queryable everywhere

**Mệnh đề cần kiểm.** dimension presence không đồng nghĩa queryable everywhere.

**Cách kiểm.** Khóa environment/version, map three tested marts sang current spec, chạy parse/validate/list/compile phù hợp môi trường và negative config cases. Reconcile representative metrics với independent oracle. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.9. simple metric giữ aggregation/expression current spec

**Mệnh đề cần kiểm.** simple metric giữ aggregation/expression current spec.

**Cách kiểm.** Khóa environment/version, map three tested marts sang current spec, chạy parse/validate/list/compile phù hợp môi trường và negative config cases. Reconcile representative metrics với independent oracle. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.10. advanced metric dependencies cần validate

**Mệnh đề cần kiểm.** advanced metric dependencies cần validate.

**Cách kiểm.** Khóa environment/version, map three tested marts sang current spec, chạy parse/validate/list/compile phù hợp môi trường và negative config cases. Reconcile representative metrics với independent oracle. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.11. missing governance fields cần adjacent metadata

**Mệnh đề cần kiểm.** missing governance fields cần adjacent metadata.

**Cách kiểm.** Khóa environment/version, map three tested marts sang current spec, chạy parse/validate/list/compile phù hợp môi trường và negative config cases. Reconcile representative metrics với independent oracle. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.12. parse khác semantic validate

**Mệnh đề cần kiểm.** parse khác semantic validate.

**Cách kiểm.** Khóa environment/version, map three tested marts sang current spec, chạy parse/validate/list/compile phù hợp môi trường và negative config cases. Reconcile representative metrics với independent oracle. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.13. validate khác business reconciliation

**Mệnh đề cần kiểm.** validate khác business reconciliation.

**Cách kiểm.** Khóa environment/version, map three tested marts sang current spec, chạy parse/validate/list/compile phù hợp môi trường và negative config cases. Reconcile representative metrics với independent oracle. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.14. negative config fixture cần lưu diagnostics

**Mệnh đề cần kiểm.** negative config fixture cần lưu diagnostics.

**Cách kiểm.** Khóa environment/version, map three tested marts sang current spec, chạy parse/validate/list/compile phù hợp môi trường và negative config cases. Reconcile representative metrics với independent oracle. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.15. credentials không được xuất hiện trong transcript

**Mệnh đề cần kiểm.** credentials không được xuất hiện trong transcript.

**Cách kiểm.** Khóa environment/version, map three tested marts sang current spec, chạy parse/validate/list/compile phù hợp môi trường và negative config cases. Reconcile representative metrics với independent oracle. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

## 9. Quy trình phản biện

1. Viết population, grain, identities, time và aggregation trước tool syntax.
2. Gắn metric/dimension với qualified entity role và allowed path.
3. Đếm rows, distinct base keys, unmatched và match multiplicity sau từng join edge.
4. Dùng independent oracle từ atomic facts; so intermediate components trước final value.
5. Chạy invalid cases cùng valid siblings để bắt underblocking và overblocking.
6. Khóa exact tool/config/mart versions; compile output và diagnostics là version-specific evidence.
7. Lưu failed runs, limitations và trigger làm certification hết hiệu lực.

## 10. Câu hỏi tự kiểm tra

1. Join path nào được chọn và business role nào biện minh cho nó?
2. Base fact keys có bị nhân hoặc mất sau từng edge không?
3. Dimension có reachable, đúng grain và compatible với aggregation không?
4. Parse/validate/compile/reconciliation xác nhận những lớp khác nhau nào?
5. Generated SQL khác contract ở population, filter, path hay aggregation nào?
6. Bằng chứng nào độc lập với engine output đang được kiểm?

## 11. Giới hạn và điều chưa cho phép kết luận

- Chưa chạy MetricFlow, warehouse queries, execution plans hoặc labs; note mô tả protocol và expected evidence.
- dbt/MetricFlow docs được kiểm ngày 2026-10-01; commands và YAML phụ thuộc engine/version/environment.
- Thuật ngữ fan/chasm có thể khác giữa sản phẩm; invariant của bài là grain, multiplicity, population và semantic path.
- Kimball–Ross và PostgreSQL hỗ trợ modeling/SQL mechanics; compatibility/certification workflow là curriculum synthesis.
- Owner chưa phê duyệt semantic meaning nên note giữ trạng thái `review`.

## Reference
1. [[SRC-DBT-SEMANTIC-MODELS]]
2. [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]]
3. [[SRC-KIMBALL-ROSS-DW-TOOLKIT-3E]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-DBT-SEMANTIC-MODELS]] | Modeling, SQL behavior hoặc current product semantics liên quan | Đã đọc phạm vi có locator; không suy ngoài phạm vi |
| [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]] | Modeling, SQL behavior hoặc current product semantics liên quan | Đã đọc phạm vi có locator; không suy ngoài phạm vi |
| [[SRC-KIMBALL-ROSS-DW-TOOLKIT-3E]] | Modeling, SQL behavior hoặc current product semantics liên quan | Đã đọc phạm vi có locator; không suy ngoài phạm vi |

## Key takeaways
- Join correctness phải được chứng minh bằng grain, multiplicity, unmatched ledger và independent oracle.
- Metric–dimension compatibility là rule ba trạng thái có lý do, không phải danh sách field tùy ý.
- Parse/validate/compile không thay reconciliation với business contract.
- Generated SQL phải được đọc theo population, path, aggregation và time/filter semantics.
- Chưa chạy protocol thì note là tài liệu học thuật có truy nguồn, không phải chứng nhận production.
