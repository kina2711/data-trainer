# Phase 5: Modeling, Semantics and Analytical Product
# Module 12: Semantic Layer and Metrics Engineering
# Lesson 171: Ambiguous Joins and the Chasm Trap

## Mục tiêu bài học

**Năng lực cần chứng minh.** Tái hiện bẫy vực bằng số và chặn nó bằng một trong ba cách, chứng minh tổng trở lại đúng.

**Điều kiện hoàn thành.** Mức thổi phồng được định lượng, cả ba cách sửa đều cho tổng khớp tổng thật, và hai đường kết cho hai con số khác nhau được chỉ ra.

> [!abstract] Câu hỏi trung tâm
> Hai đường join hợp lệ về cú pháp hoặc hai fact tables cùng qua một dimension làm metric sai như thế nào, và phải chặn ở graph/query plan ra sao?

## 1. Hai lỗi khác nhau nhưng cùng im lặng

Ambiguous join xuất hiện khi semantic graph có nhiều path giữa source metric và requested dimension; mỗi path có thể hợp lệ kỹ thuật nhưng mang role khác. Chasm trap xuất hiện khi hai fact-like sets độc lập cùng nối qua một dimension và bị join trong cùng rowset trước aggregate. Cả hai thường không gây SQL error. Kết quả có thể gần “hợp lý”, nên validation phải dựa trên grain, cardinality và oracle totals thay vì nhìn dashboard.

## 2. Phép toán của bẫy vực

Với mỗi customer k, orders có m_k rows và tickets có n_k rows. Join qua customer tạo m_k × n_k combinations. SUM(order_amount) bị lặp n_k lần; ticket measure bị lặp m_k lần. Nếu một phía có zero rows, inner join còn làm mất population. Grand total có thể vừa nhân vừa mất theo keys khác nhau. `DISTINCT amount` không sửa vì hai orders hợp lệ có thể cùng amount; distinct business key chỉ giúp một metric cụ thể và có thể che model sai.

## 3. Ba cách sửa và điều kiện

Cách một: aggregate mỗi fact về common grain như customer-month rồi join aggregates; phải bảo đảm dimensions/filters cần thiết còn tồn tại. Cách hai: correlated subquery hoặc lateral computation cho từng dimension row; semantics rõ nhưng có thể đắt và optimizer-dependent. Cách ba: hai queries độc lập rồi merge ở presentation/common grain; tránh row multiplication nhưng cần alignment key, missing-side policy và consistent filters. Không có cách nào đúng nếu common grain hoặc population chưa được công bố.

## 4. Bẫy hố và mất dòng

Fan trap thường mô tả một đường one-to-many tiếp tục one-to-many làm aggregate cấp trên bị nhân; chasm nhấn hai facts cùng dimension. Roadmap còn gọi “bẫy hố” cho trường hợp đi sai hướng làm mất rows. Tên gọi giữa tools có thể khác, nên note dùng invariant: join phải bảo toàn population và multiplicity đã khai. Outer/inner choice, filter placement và optional relationship quyết định mất dòng; kiểm unmatched ledger bên cạnh fanout.

## 5. Nhiều path là nhiều meaning

Order nối customer qua purchaser; shipment nối customer qua recipient; support ticket nối qua requester. Query “tickets theo customer của order” có thể muốn purchaser, recipient hoặc requester. Path ngắn nhất không phải mặc định đúng. Graph phải có role-qualified entities/dimensions, allowed paths hoặc metric-specific constraints. Khi không đủ thông tin, engine nên reject và yêu cầu chọn role thay vì chọn deterministic nhưng sai.

## 6. Thiết kế fixture định lượng

Tạo customer A có 2 orders và 3 tickets, B có 1 order và 0 tickets, C có 0 orders và 2 tickets. Gán amounts khác nhau nhưng có một cặp bằng nhau để bắt lỗi DISTINCT. Tính oracle riêng từ mỗi fact. Chạy inner, left và full alignment; lưu rows per customer, distinct fact keys, unmatched, sums và inflation factor. Với ambiguous path, tạo purchaser khác recipient để hai paths cho kết quả quan sát được khác.

## 7. Ranh giới công cụ

MetricFlow mô tả entities như join keys và xây joins từ entity types nhằm tránh fanout/chasm patterns, nhưng khai báo identity/cardinality sai vẫn truyền sai meaning vào graph. Validation/compile thành công chứng minh cấu hình hợp lệ theo engine, không chứng minh source grain hay business role đúng. Vì vậy generated SQL và reconciliation độc lập vẫn là bằng chứng bắt buộc.

## 8. Ma trận kiểm chứng từng mệnh đề

Mọi mệnh đề dưới đây cần fixture, invariant, independent oracle và output lưu được. Compile thành công hoặc con số nhìn hợp lý không đủ làm bằng chứng.

### 8.1. join hai facts qua dimension tạo cross product theo key

**Mệnh đề cần kiểm.** join hai facts qua dimension tạo cross product theo key.

**Cách kiểm.** Dựng two facts và shared dimension với keys 2×3, 1×0, 0×2; tính oracle từ từng fact, đo multiplicity/unmatched/inflation và kiểm ba fixes. Tạo purchaser/recipient paths cho hai answers khác nhau. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.2. inner join có thể vừa nhân vừa làm mất population

**Mệnh đề cần kiểm.** inner join có thể vừa nhân vừa làm mất population.

**Cách kiểm.** Dựng two facts và shared dimension với keys 2×3, 1×0, 0×2; tính oracle từ từng fact, đo multiplicity/unmatched/inflation và kiểm ba fixes. Tạo purchaser/recipient paths cho hai answers khác nhau. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.3. DISTINCT amount không sửa grain

**Mệnh đề cần kiểm.** DISTINCT amount không sửa grain.

**Cách kiểm.** Dựng two facts và shared dimension với keys 2×3, 1×0, 0×2; tính oracle từ từng fact, đo multiplicity/unmatched/inflation và kiểm ba fixes. Tạo purchaser/recipient paths cho hai answers khác nhau. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.4. aggregate-before-join cần common grain

**Mệnh đề cần kiểm.** aggregate-before-join cần common grain.

**Cách kiểm.** Dựng two facts và shared dimension với keys 2×3, 1×0, 0×2; tính oracle từ từng fact, đo multiplicity/unmatched/inflation và kiểm ba fixes. Tạo purchaser/recipient paths cho hai answers khác nhau. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.5. correlated subquery cần kiểm cost và semantics

**Mệnh đề cần kiểm.** correlated subquery cần kiểm cost và semantics.

**Cách kiểm.** Dựng two facts và shared dimension với keys 2×3, 1×0, 0×2; tính oracle từ từng fact, đo multiplicity/unmatched/inflation và kiểm ba fixes. Tạo purchaser/recipient paths cho hai answers khác nhau. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.6. separate queries cần alignment policy

**Mệnh đề cần kiểm.** separate queries cần alignment policy.

**Cách kiểm.** Dựng two facts và shared dimension với keys 2×3, 1×0, 0×2; tính oracle từ từng fact, đo multiplicity/unmatched/inflation và kiểm ba fixes. Tạo purchaser/recipient paths cho hai answers khác nhau. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.7. unmatched ledger phải đi cùng fanout ledger

**Mệnh đề cần kiểm.** unmatched ledger phải đi cùng fanout ledger.

**Cách kiểm.** Dựng two facts và shared dimension với keys 2×3, 1×0, 0×2; tính oracle từ từng fact, đo multiplicity/unmatched/inflation và kiểm ba fixes. Tạo purchaser/recipient paths cho hai answers khác nhau. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.8. shortest path không đồng nghĩa correct path

**Mệnh đề cần kiểm.** shortest path không đồng nghĩa correct path.

**Cách kiểm.** Dựng two facts và shared dimension với keys 2×3, 1×0, 0×2; tính oracle từ từng fact, đo multiplicity/unmatched/inflation và kiểm ba fixes. Tạo purchaser/recipient paths cho hai answers khác nhau. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.9. role-playing entity phải được đặt tên rõ

**Mệnh đề cần kiểm.** role-playing entity phải được đặt tên rõ.

**Cách kiểm.** Dựng two facts và shared dimension với keys 2×3, 1×0, 0×2; tính oracle từ từng fact, đo multiplicity/unmatched/inflation và kiểm ba fixes. Tạo purchaser/recipient paths cho hai answers khác nhau. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.10. engine phải reject path ambiguity khi thiếu context

**Mệnh đề cần kiểm.** engine phải reject path ambiguity khi thiếu context.

**Cách kiểm.** Dựng two facts và shared dimension với keys 2×3, 1×0, 0×2; tính oracle từ từng fact, đo multiplicity/unmatched/inflation và kiểm ba fixes. Tạo purchaser/recipient paths cho hai answers khác nhau. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.11. cardinality declaration sai làm planner tự tin sai

**Mệnh đề cần kiểm.** cardinality declaration sai làm planner tự tin sai.

**Cách kiểm.** Dựng two facts và shared dimension với keys 2×3, 1×0, 0×2; tính oracle từ từng fact, đo multiplicity/unmatched/inflation và kiểm ba fixes. Tạo purchaser/recipient paths cho hai answers khác nhau. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.12. oracle phải lấy trực tiếp từng fact

**Mệnh đề cần kiểm.** oracle phải lấy trực tiếp từng fact.

**Cách kiểm.** Dựng two facts và shared dimension với keys 2×3, 1×0, 0×2; tính oracle từ từng fact, đo multiplicity/unmatched/inflation và kiểm ba fixes. Tạo purchaser/recipient paths cho hai answers khác nhau. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.13. test data cần duplicate amounts hợp lệ

**Mệnh đề cần kiểm.** test data cần duplicate amounts hợp lệ.

**Cách kiểm.** Dựng two facts và shared dimension với keys 2×3, 1×0, 0×2; tính oracle từ từng fact, đo multiplicity/unmatched/inflation và kiểm ba fixes. Tạo purchaser/recipient paths cho hai answers khác nhau. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.14. inflation factor phải đo theo key và total

**Mệnh đề cần kiểm.** inflation factor phải đo theo key và total.

**Cách kiểm.** Dựng two facts và shared dimension với keys 2×3, 1×0, 0×2; tính oracle từ từng fact, đo multiplicity/unmatched/inflation và kiểm ba fixes. Tạo purchaser/recipient paths cho hai answers khác nhau. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.15. compiled SQL không chứng minh business correctness

**Mệnh đề cần kiểm.** compiled SQL không chứng minh business correctness.

**Cách kiểm.** Dựng two facts và shared dimension với keys 2×3, 1×0, 0×2; tính oracle từ từng fact, đo multiplicity/unmatched/inflation và kiểm ba fixes. Tạo purchaser/recipient paths cho hai answers khác nhau. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

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
2. [[SRC-KIMBALL-ROSS-DW-TOOLKIT-3E]]
3. [[SRC-POSTGRESQL-17-QUERY-EXPRESSIONS]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-DBT-SEMANTIC-MODELS]] | Modeling, SQL behavior hoặc current product semantics liên quan | Đã đọc phạm vi có locator; không suy ngoài phạm vi |
| [[SRC-KIMBALL-ROSS-DW-TOOLKIT-3E]] | Modeling, SQL behavior hoặc current product semantics liên quan | Đã đọc phạm vi có locator; không suy ngoài phạm vi |
| [[SRC-POSTGRESQL-17-QUERY-EXPRESSIONS]] | Modeling, SQL behavior hoặc current product semantics liên quan | Đã đọc phạm vi có locator; không suy ngoài phạm vi |

## Key takeaways
- Join correctness phải được chứng minh bằng grain, multiplicity, unmatched ledger và independent oracle.
- Metric–dimension compatibility là rule ba trạng thái có lý do, không phải danh sách field tùy ý.
- Parse/validate/compile không thay reconciliation với business contract.
- Generated SQL phải được đọc theo population, path, aggregation và time/filter semantics.
- Chưa chạy protocol thì note là tài liệu học thuật có truy nguồn, không phải chứng nhận production.
