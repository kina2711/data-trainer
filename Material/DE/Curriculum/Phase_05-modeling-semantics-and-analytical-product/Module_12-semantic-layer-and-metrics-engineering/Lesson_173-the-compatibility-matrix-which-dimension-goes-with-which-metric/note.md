# Phase 5: Modeling, Semantics and Analytical Product
# Module 12: Semantic Layer and Metrics Engineering
# Lesson 173: The Compatibility Matrix - Which Dimension Goes with Which Metric

## Mục tiêu bài học

**Năng lực cần chứng minh.** Dựng ma trận tương thích cho bộ chỉ số và cưỡng chế được nó bằng máy với thông báo giải thích.

**Điều kiện hoàn thành.** Năm truy vấn không hợp lệ bị chặn kèm giải thích, năm truy vấn hợp lệ chạy được, và ma trận xuất ra dạng tài liệu đọc được.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào biến khả năng slice một metric theo dimension thành ma trận ba trạng thái có lý do và được engine cưỡng chế?

## 1. Ma trận là projection của contract và graph

Rows là metric versions, columns là qualified dimensions. Ô không được điền theo trực giác; nó được suy từ reachability, path cardinality, grain compatibility, additivity, population/time và access policy. Ma trận là artifact dẫn xuất nhưng phải version/fingerprint cùng source graph. Manual override cần reason, owner và test vì có thể che lỗi model.

## 2. Ba trạng thái

Valid: có path được phép, bảo toàn metric contract và aggregation. Invalid: không có safe semantic interpretation hoặc policy cấm; engine phải reject. Conditional: chỉ hợp lệ với role/path, grain, filter, allocation, time operator hoặc pre-aggregation cụ thể. Conditional không phải ghi chú mơ hồ; nó phải compile thành machine rule hoặc saved query template có parameters/constraints.

## 3. Ba nhóm không tương thích

Unreachable: dimension không nối tới metric entity. Reachable-but-wrong-grain: path tồn tại nhưng dimension coarse/many-side làm mất nghĩa hoặc fanout. Non-additive: dimension/time rollup yêu cầu operator metric không hỗ trợ. Bổ sung hai nhóm thực tế: semantic mismatch dù key join được, và authorization/privacy restriction. Lý do phải có stable code để documentation và engine message nhất quán.

## 4. Cưỡng chế và thông báo

Trước query execution, planner kiểm requested metrics × dimensions. Invalid cell trả error gồm metric, dimension, rule code, violated invariant và alternatives: role-qualified dimension, allowed grain, saved query hoặc metric khác. Conditional cell yêu cầu condition được thỏa và hiện trong generated SQL. Không silently drop dimension, choose another path hoặc return NULLs vì người dùng không biết question đã đổi.

## 5. Không chặn nhầm

Mỗi invalid test có valid sibling thay đúng một yếu tố. Ví dụ `ending_balance × day` với SUM invalid, nhưng `ending_balance × day` với last-value query có thể valid; `revenue × ticket_tag` invalid without bridge, valid với allocated tag contract. Test coverage đếm valid, invalid, conditional, unreachable và regression across versions. Tỷ lệ block cao không phải dấu hiệu tốt nếu consumers không trả lời được câu hỏi hợp lệ.

## 6. Tài liệu cho người dùng

Export matrix ở dạng searchable: metric description, dimensions, status, reason, path/role, constraints, examples và owner. Hiển thị dimensions queryable từ engine metadata nhưng thêm business wording. Generated docs phải mang build timestamp và graph/contract version; bản cũ không được trông như current truth. M13 dùng matrix cho discoverability, nhưng source of truth vẫn là versioned semantic config/contracts.

## 7. Bài lab 8 × 6

Chọn eight metrics gồm additive, ratio, balance, distinct và cumulative; six dimensions gồm direct, role-playing, many-side, time, unreachable và restricted. Ma trận 48 cells phải có justification templates nhưng review từng exception. Chạy năm valid/five invalid và ít nhất two conditional queries; lưu compile/rejection output cùng generated docs snapshot.

## 8. Ma trận kiểm chứng từng mệnh đề

Mọi mệnh đề dưới đây cần fixture, invariant, independent oracle và output lưu được. Compile thành công hoặc con số nhìn hợp lý không đủ làm bằng chứng.

### 8.1. matrix rows phải gắn metric version

**Mệnh đề cần kiểm.** matrix rows phải gắn metric version.

**Cách kiểm.** Sinh matrix 8×6 từ graph/additivity/policy, test five valid, five invalid và conditional cases. So engine metadata/rejections với expected reason codes và exported documentation. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.2. dimension names phải qualified theo entity role

**Mệnh đề cần kiểm.** dimension names phải qualified theo entity role.

**Cách kiểm.** Sinh matrix 8×6 từ graph/additivity/policy, test five valid, five invalid và conditional cases. So engine metadata/rejections với expected reason codes và exported documentation. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.3. valid cần safe path và aggregation

**Mệnh đề cần kiểm.** valid cần safe path và aggregation.

**Cách kiểm.** Sinh matrix 8×6 từ graph/additivity/policy, test five valid, five invalid và conditional cases. So engine metadata/rejections với expected reason codes và exported documentation. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.4. invalid cần stable reason code

**Mệnh đề cần kiểm.** invalid cần stable reason code.

**Cách kiểm.** Sinh matrix 8×6 từ graph/additivity/policy, test five valid, five invalid và conditional cases. So engine metadata/rejections với expected reason codes và exported documentation. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.5. conditional phải có machine-checkable condition

**Mệnh đề cần kiểm.** conditional phải có machine-checkable condition.

**Cách kiểm.** Sinh matrix 8×6 từ graph/additivity/policy, test five valid, five invalid và conditional cases. So engine metadata/rejections với expected reason codes và exported documentation. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.6. unreachable khác reachable-wrong-grain

**Mệnh đề cần kiểm.** unreachable khác reachable-wrong-grain.

**Cách kiểm.** Sinh matrix 8×6 từ graph/additivity/policy, test five valid, five invalid và conditional cases. So engine metadata/rejections với expected reason codes và exported documentation. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.7. non-additive dimension phải bị reject hoặc rewrite

**Mệnh đề cần kiểm.** non-additive dimension phải bị reject hoặc rewrite.

**Cách kiểm.** Sinh matrix 8×6 từ graph/additivity/policy, test five valid, five invalid và conditional cases. So engine metadata/rejections với expected reason codes và exported documentation. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.8. authorization restriction không phải join problem

**Mệnh đề cần kiểm.** authorization restriction không phải join problem.

**Cách kiểm.** Sinh matrix 8×6 từ graph/additivity/policy, test five valid, five invalid và conditional cases. So engine metadata/rejections với expected reason codes và exported documentation. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.9. engine không được silently drop dimension

**Mệnh đề cần kiểm.** engine không được silently drop dimension.

**Cách kiểm.** Sinh matrix 8×6 từ graph/additivity/policy, test five valid, five invalid và conditional cases. So engine metadata/rejections với expected reason codes và exported documentation. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.10. error message phải đưa alternative

**Mệnh đề cần kiểm.** error message phải đưa alternative.

**Cách kiểm.** Sinh matrix 8×6 từ graph/additivity/policy, test five valid, five invalid và conditional cases. So engine metadata/rejections với expected reason codes và exported documentation. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.11. valid sibling phát hiện overblocking

**Mệnh đề cần kiểm.** valid sibling phát hiện overblocking.

**Cách kiểm.** Sinh matrix 8×6 từ graph/additivity/policy, test five valid, five invalid và conditional cases. So engine metadata/rejections với expected reason codes và exported documentation. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.12. metadata export cần graph version

**Mệnh đề cần kiểm.** metadata export cần graph version.

**Cách kiểm.** Sinh matrix 8×6 từ graph/additivity/policy, test five valid, five invalid và conditional cases. So engine metadata/rejections với expected reason codes và exported documentation. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.13. manual override cần owner và expiry

**Mệnh đề cần kiểm.** manual override cần owner và expiry.

**Cách kiểm.** Sinh matrix 8×6 từ graph/additivity/policy, test five valid, five invalid và conditional cases. So engine metadata/rejections với expected reason codes và exported documentation. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.14. 48 cells cần review exceptions

**Mệnh đề cần kiểm.** 48 cells cần review exceptions.

**Cách kiểm.** Sinh matrix 8×6 từ graph/additivity/policy, test five valid, five invalid và conditional cases. So engine metadata/rejections với expected reason codes và exported documentation. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

**Bằng chứng đạt.** Lưu contract/graph/config version, seed snapshot, command/SQL, raw output, row/multiplicity ledger và semantic diff. Nếu chưa chạy tool/lab, trạng thái chỉ là test protocol.

### 8.15. documentation không thay source config

**Mệnh đề cần kiểm.** documentation không thay source config.

**Cách kiểm.** Sinh matrix 8×6 từ graph/additivity/policy, test five valid, five invalid và conditional cases. So engine metadata/rejections với expected reason codes và exported documentation. Với mệnh đề này, ghi data shape gây lỗi, expected result và failure signal. Không dùng generated query làm oracle cho chính nó.

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
3. [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-DBT-SEMANTIC-MODELS]] | Modeling, SQL behavior hoặc current product semantics liên quan | Đã đọc phạm vi có locator; không suy ngoài phạm vi |
| [[SRC-KIMBALL-ROSS-DW-TOOLKIT-3E]] | Modeling, SQL behavior hoặc current product semantics liên quan | Đã đọc phạm vi có locator; không suy ngoài phạm vi |
| [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]] | Modeling, SQL behavior hoặc current product semantics liên quan | Đã đọc phạm vi có locator; không suy ngoài phạm vi |

## Key takeaways
- Join correctness phải được chứng minh bằng grain, multiplicity, unmatched ledger và independent oracle.
- Metric–dimension compatibility là rule ba trạng thái có lý do, không phải danh sách field tùy ý.
- Parse/validate/compile không thay reconciliation với business contract.
- Generated SQL phải được đọc theo population, path, aggregation và time/filter semantics.
- Chưa chạy protocol thì note là tài liệu học thuật có truy nguồn, không phải chứng nhận production.
