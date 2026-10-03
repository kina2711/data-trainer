# Phase 5: Modeling, Semantics and Analytical Product
# Module 13: Analytical Data Product and Self-service
# Lesson 188: Product Anatomy - What Makes a Dataset a Product

## Mục tiêu bài học

**Năng lực cần chứng minh.** Chấm một tập dữ liệu theo tám thuộc tính và chỉ ra nó ở mức trưởng thành nào.

**Điều kiện hoàn thành.** Chấm đúng ≥ 2/3 tập dữ liệu theo tám thuộc tính kèm bằng chứng, và sáu khái niệm được phân loại bằng ví dụ thật.

> [!abstract] Câu hỏi trung tâm
> Một dataset cần những đặc tính vận hành nào để trở thành analytical data product, và rubric trưởng thành phải dựa trên bằng chứng nào?

## 1. Sáu artifact không đồng nghĩa

Dataset là collection dữ liệu; mart là modeled dataset cho analytical use; dashboard là presentation; semantic model định nghĩa query meaning; metric API là serving interface; data product là owned lifecycle unit cung cấp value qua một hay nhiều interfaces. Một product có thể chứa mart, semantic/API và docs; một dashboard có thể tiêu thụ nhiều products. Gọi mọi table là product làm mất ranh giới ownership và service obligations.

## 2. Tám thuộc tính như evidence rubric

Named accountable owner; identified consumers/use cases; stable public interface; explicit contract; service commitments; usable documentation/discovery; access policy; lifecycle/deprecation plan. Mỗi ô pass cần artifact/observation: owner with decision rights, consumer registry, schema/API version, tests/SLO dashboards, access negative test, deprecation record. Checkbox “có docs” không đủ nếu consumer không trả lời được grain/freshness.

## 3. Data mesh source và curriculum synthesis

Dehghani nêu discoverability, security, understandability, trustworthiness, domain ownership và interfaces phù hợp personas; product gồm code, data/metadata và infrastructure. Rubric tám thuộc tính trong bài tổng hợp thêm contract, service level và retirement evidence từ software/data engineering. Không gán danh sách tám mục nguyên văn cho data mesh. Data product có thể tồn tại ngoài data mesh.

## 4. Ranh giới product và domain

Boundary theo cohesive business capability/use cases, không theo mỗi table hoặc toàn warehouse. Product có input dependencies, transformations, outputs/interfaces, metadata, policies và operating ownership. Single accountable domain/team tránh ownership khuếch tán, nhưng composite product có upstream contracts. Boundary quá nhỏ gây catalog noise; quá lớn làm owner và SLO mơ hồ. Dùng change coupling, consumer cohorts và independent lifecycle để kiểm.

## 5. Ba mức trưởng thành có điều kiện

Level 1 documented asset: owner/interface/meaning cơ bản, còn manual support và weak SLO. Level 2 operated product: automated tests, SLO/alerts, access controls, consumer feedback, version/deprecation. Level 3 ecosystem-ready: standardized interfaces/metadata, discoverability, portability/composability, policy automation và measured adoption. Level không là danh hiệu; mỗi capability có evidence và có thể khác mức. Không đòi Level 3 cho use case nhỏ.

## 6. Kế hoạch chết là dấu hiệu lifecycle

Product plan gồm deprecation triggers: no active decision, replacement adopted, compliance/cost change hoặc owner withdrawal. Inventory consumers, parallel/replacement path, retention/archive, notices, removal proof và restore boundary. Không có retirement plan khiến unused tables/jobs/docs sống vô hạn. Nhưng có plan không có nghĩa auto-delete; legal retention, audit và reproducibility có thể yêu cầu preserve snapshot.

## 7. Chấm ba assets

Chọn dataset raw, curated mart và dashboard/semantic product. Với từng thuộc tính, ghi pass/fail/partial, locator, owner và consequence. Phân loại artifact type trước khi chấm product maturity. Chọn missing attribute gây risk lớn nhất dựa use case, không mặc định deprecation luôn cao nhất. Đề xuất next smallest evidence-producing change và changed-consumer test.

## 8. Ma trận kiểm chứng từng mệnh đề

Mỗi mệnh đề dưới đây cần observation, fixture hoặc artifact có thể lưu. Tên công nghệ, consensus hoặc output nhìn hợp lý không tự là bằng chứng.

### 8.1. dataset differs from data product

**Mệnh đề cần kiểm.** dataset differs from data product.

**Cách kiểm.** Score three real/synthetic assets on eight attributes with evidence locators. Classify artifact type first, then maturity; test a changed consumer and draft deprecation path without deleting data. Với riêng mệnh đề này, ghi input/context, expected observation, failure signal và boundary làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu contract/decision version, fixture hoặc interview evidence, command/checklist output, reviewer và artifact hash. Nếu chưa thực hiện lab, trạng thái chỉ là protocol; không ghi thành kết quả đã quan sát.

### 8.2. mart differs from dashboard

**Mệnh đề cần kiểm.** mart differs from dashboard.

**Cách kiểm.** Score three real/synthetic assets on eight attributes with evidence locators. Classify artifact type first, then maturity; test a changed consumer and draft deprecation path without deleting data. Với riêng mệnh đề này, ghi input/context, expected observation, failure signal và boundary làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu contract/decision version, fixture hoặc interview evidence, command/checklist output, reviewer và artifact hash. Nếu chưa thực hiện lab, trạng thái chỉ là protocol; không ghi thành kết quả đã quan sát.

### 8.3. semantic model differs from metric API

**Mệnh đề cần kiểm.** semantic model differs from metric API.

**Cách kiểm.** Score three real/synthetic assets on eight attributes with evidence locators. Classify artifact type first, then maturity; test a changed consumer and draft deprecation path without deleting data. Với riêng mệnh đề này, ghi input/context, expected observation, failure signal và boundary làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu contract/decision version, fixture hoặc interview evidence, command/checklist output, reviewer và artifact hash. Nếu chưa thực hiện lab, trạng thái chỉ là protocol; không ghi thành kết quả đã quan sát.

### 8.4. product may expose multiple interfaces

**Mệnh đề cần kiểm.** product may expose multiple interfaces.

**Cách kiểm.** Score three real/synthetic assets on eight attributes with evidence locators. Classify artifact type first, then maturity; test a changed consumer and draft deprecation path without deleting data. Với riêng mệnh đề này, ghi input/context, expected observation, failure signal và boundary làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu contract/decision version, fixture hoặc interview evidence, command/checklist output, reviewer và artifact hash. Nếu chưa thực hiện lab, trạng thái chỉ là protocol; không ghi thành kết quả đã quan sát.

### 8.5. eight attributes require evidence locators

**Mệnh đề cần kiểm.** eight attributes require evidence locators.

**Cách kiểm.** Score three real/synthetic assets on eight attributes with evidence locators. Classify artifact type first, then maturity; test a changed consumer and draft deprecation path without deleting data. Với riêng mệnh đề này, ghi input/context, expected observation, failure signal và boundary làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu contract/decision version, fixture hoặc interview evidence, command/checklist output, reviewer và artifact hash. Nếu chưa thực hiện lab, trạng thái chỉ là protocol; không ghi thành kết quả đã quan sát.

### 8.6. owner needs decision rights

**Mệnh đề cần kiểm.** owner needs decision rights.

**Cách kiểm.** Score three real/synthetic assets on eight attributes with evidence locators. Classify artifact type first, then maturity; test a changed consumer and draft deprecation path without deleting data. Với riêng mệnh đề này, ghi input/context, expected observation, failure signal và boundary làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu contract/decision version, fixture hoặc interview evidence, command/checklist output, reviewer và artifact hash. Nếu chưa thực hiện lab, trạng thái chỉ là protocol; không ghi thành kết quả đã quan sát.

### 8.7. consumer registry names use cases

**Mệnh đề cần kiểm.** consumer registry names use cases.

**Cách kiểm.** Score three real/synthetic assets on eight attributes with evidence locators. Classify artifact type first, then maturity; test a changed consumer and draft deprecation path without deleting data. Với riêng mệnh đề này, ghi input/context, expected observation, failure signal và boundary làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu contract/decision version, fixture hoặc interview evidence, command/checklist output, reviewer và artifact hash. Nếu chưa thực hiện lab, trạng thái chỉ là protocol; không ghi thành kết quả đã quan sát.

### 8.8. stable interface needs version policy

**Mệnh đề cần kiểm.** stable interface needs version policy.

**Cách kiểm.** Score three real/synthetic assets on eight attributes with evidence locators. Classify artifact type first, then maturity; test a changed consumer and draft deprecation path without deleting data. Với riêng mệnh đề này, ghi input/context, expected observation, failure signal và boundary làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu contract/decision version, fixture hoặc interview evidence, command/checklist output, reviewer và artifact hash. Nếu chưa thực hiện lab, trạng thái chỉ là protocol; không ghi thành kết quả đã quan sát.

### 8.9. SLO needs measurement window

**Mệnh đề cần kiểm.** SLO needs measurement window.

**Cách kiểm.** Score three real/synthetic assets on eight attributes with evidence locators. Classify artifact type first, then maturity; test a changed consumer and draft deprecation path without deleting data. Với riêng mệnh đề này, ghi input/context, expected observation, failure signal và boundary làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu contract/decision version, fixture hoặc interview evidence, command/checklist output, reviewer và artifact hash. Nếu chưa thực hiện lab, trạng thái chỉ là protocol; không ghi thành kết quả đã quan sát.

### 8.10. documentation needs consumer usability

**Mệnh đề cần kiểm.** documentation needs consumer usability.

**Cách kiểm.** Score three real/synthetic assets on eight attributes with evidence locators. Classify artifact type first, then maturity; test a changed consumer and draft deprecation path without deleting data. Với riêng mệnh đề này, ghi input/context, expected observation, failure signal và boundary làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu contract/decision version, fixture hoặc interview evidence, command/checklist output, reviewer và artifact hash. Nếu chưa thực hiện lab, trạng thái chỉ là protocol; không ghi thành kết quả đã quan sát.

### 8.11. access needs negative test

**Mệnh đề cần kiểm.** access needs negative test.

**Cách kiểm.** Score three real/synthetic assets on eight attributes with evidence locators. Classify artifact type first, then maturity; test a changed consumer and draft deprecation path without deleting data. Với riêng mệnh đề này, ghi input/context, expected observation, failure signal và boundary làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu contract/decision version, fixture hoặc interview evidence, command/checklist output, reviewer và artifact hash. Nếu chưa thực hiện lab, trạng thái chỉ là protocol; không ghi thành kết quả đã quan sát.

### 8.12. data mesh list not identical to curriculum rubric

**Mệnh đề cần kiểm.** data mesh list not identical to curriculum rubric.

**Cách kiểm.** Score three real/synthetic assets on eight attributes with evidence locators. Classify artifact type first, then maturity; test a changed consumer and draft deprecation path without deleting data. Với riêng mệnh đề này, ghi input/context, expected observation, failure signal và boundary làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu contract/decision version, fixture hoặc interview evidence, command/checklist output, reviewer và artifact hash. Nếu chưa thực hiện lab, trạng thái chỉ là protocol; không ghi thành kết quả đã quan sát.

### 8.13. product boundary follows cohesive capability

**Mệnh đề cần kiểm.** product boundary follows cohesive capability.

**Cách kiểm.** Score three real/synthetic assets on eight attributes with evidence locators. Classify artifact type first, then maturity; test a changed consumer and draft deprecation path without deleting data. Với riêng mệnh đề này, ghi input/context, expected observation, failure signal và boundary làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu contract/decision version, fixture hoặc interview evidence, command/checklist output, reviewer và artifact hash. Nếu chưa thực hiện lab, trạng thái chỉ là protocol; không ghi thành kết quả đã quan sát.

### 8.14. maturity levels are capability evidence

**Mệnh đề cần kiểm.** maturity levels are capability evidence.

**Cách kiểm.** Score three real/synthetic assets on eight attributes with evidence locators. Classify artifact type first, then maturity; test a changed consumer and draft deprecation path without deleting data. Với riêng mệnh đề này, ghi input/context, expected observation, failure signal và boundary làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu contract/decision version, fixture hoặc interview evidence, command/checklist output, reviewer và artifact hash. Nếu chưa thực hiện lab, trạng thái chỉ là protocol; không ghi thành kết quả đã quan sát.

### 8.15. retirement plan respects retention obligations

**Mệnh đề cần kiểm.** retirement plan respects retention obligations.

**Cách kiểm.** Score three real/synthetic assets on eight attributes with evidence locators. Classify artifact type first, then maturity; test a changed consumer and draft deprecation path without deleting data. Với riêng mệnh đề này, ghi input/context, expected observation, failure signal và boundary làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu contract/decision version, fixture hoặc interview evidence, command/checklist output, reviewer và artifact hash. Nếu chưa thực hiện lab, trạng thái chỉ là protocol; không ghi thành kết quả đã quan sát.

## 9. Quy trình phản biện

1. Viết decision, consumer, contract và constraints trước khi chọn tool hoặc implementation.
2. Tách source fact, curriculum synthesis và organizational choice.
3. Dùng counterexample và changed constraint để kiểm quyết định có đảo đúng lúc.
4. Gắn mọi approval/certification với exact version, evidence và scope.
5. Kiểm cả valid path lẫn negative/failure path; không chỉ demo happy path.
6. Ghi limitation của telemetry, test environment và source authority.
7. Chưa có execution evidence thì giữ trạng thái `review`.

## 10. Câu hỏi tự kiểm tra

1. Decision hoặc invariant nào đang được bảo vệ?
2. Evidence nào độc lập với implementation đang được đánh giá?
3. Điều kiện nào làm lựa chọn hiện tại phải đảo?
4. Ai có quyền quyết nghĩa, ai triển khai và ai giữ quy trình?
5. Thay đổi nào ảnh hưởng consumer dù interface vẫn chạy?
6. Failure mode nào còn chưa có automated detector?

## 11. Giới hạn và điều chưa cho phép kết luận

- Chưa chạy các lab, migration, workload benchmark hoặc fault-injection; note mô tả protocol và expected evidence.
- Tài liệu sản phẩm web được kiểm ngày 2026-10-02; feature, syntax, license và integration có thể đổi.
- Các scorecard, lifecycle gates, failure matrix và decision contract là curriculum synthesis từ nguồn đã nêu; không gán nguyên văn cho một tác giả.
- Ví dụ tổ chức không thay discovery thực tế, threat model, cost model hoặc owner approval.
- Note giữ trạng thái `review` cho tới khi chủ dự án duyệt semantic meaning.

## Reference
1. [[SRC-DEHGHANI-DATA-MESH-PRINCIPLES]]
2. [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]]
3. [[SRC-GOVUK-UNDERSTAND-USER-NEEDS]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-DEHGHANI-DATA-MESH-PRINCIPLES]] | Khái niệm, cơ chế hoặc decision boundary liên quan | Đã đọc locator được ghi trong source record; không suy ngoài phạm vi |
| [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]] | Khái niệm, cơ chế hoặc decision boundary liên quan | Đã đọc locator được ghi trong source record; không suy ngoài phạm vi |
| [[SRC-GOVUK-UNDERSTAND-USER-NEEDS]] | Khái niệm, cơ chế hoặc decision boundary liên quan | Đã đọc locator được ghi trong source record; không suy ngoài phạm vi |

## Key takeaways
- Chọn kiến trúc và data product từ decision/constraints, không từ độ mới của công nghệ.
- Metric governance cần versioned evidence, lifecycle gates và owner có quyền rõ.
- Failure matrix chỉ hữu dụng khi mỗi dòng có detector hoặc control kiểm được.
- Capstone là hồ sơ bằng chứng tích hợp, không phải bộ YAML hay dashboard trình diễn.
- Discovery phải cho phép kết luận không xây analytics product.
