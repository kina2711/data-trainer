# Phase 5: Modeling, Semantics and Analytical Product
# Module 12: Semantic Layer and Metrics Engineering
# Lesson 184: Capstone - A Governed Revenue Semantic Product

## Mục tiêu bài học

**Năng lực cần chứng minh.** Nộp sản phẩm ngữ nghĩa đủ chín hạng mục với 15 chỉ số thuộc năm loại, không vi phạm sáu điều kiện tự động không đạt.

**Điều kiện hoàn thành.** Chín hạng mục đầy đủ với ≥ 15 chỉ số thuộc ≥ 5 loại và ≥ 3 mô hình ngữ nghĩa, mọi chỉ số khớp đối soát độc lập ở ba mức gộp nhân sáu ca đối chứng, di trú phá vỡ hoàn tất có bản ghi khai tử, và không vi phạm sáu điều kiện tự động không đạt.

> [!abstract] Câu hỏi trung tâm
> Một governed revenue semantic product cần những artifacts, proofs và adversarial checks nào để chứng minh 15 metrics có thể được dùng và thay đổi an toàn?

## 1. Product boundary trước metrics

Chốt business process revenue, included/excluded events, currencies, legal entities, booking/recognition/refund time, source systems, consumers và non-goals. Revenue không đồng nhất bookings, billings, cash hay recognized revenue. Dataset fixture và contract phải cho thấy cancelled, refunded, partial, late và corrected transactions. Nếu boundary chưa duyệt, 15 formulas chỉ là technical outputs chưa có business authority.

## 2. Portfolio 15 metrics năm loại

Tối thiểu gồm additive amount/count, ratio, derived, cumulative và semi/non-additive snapshot/distinct. Mỗi metric có stable ID/version, population, grain, time, aggregation, dimensions compatibility, owner, security class và interpretation limits. Tránh đạt số lượng bằng aliases hoặc đổi tên cùng formula. Coverage matrix nối metric types với failure modes và consumer questions.

## 3. Ba semantic models và join proof

Models có declared grain/entities/time; cross-model query buộc đi qua nhiều joins và role-qualified paths. Paper proof ghi multiplicity, common grain, row counts, distinct base keys, unmatched và control totals. Generated SQL cùng representative execution plan được review cho population/path/aggregation/time. Compiler green không thay independent oracle.

## 4. Ba tầng test và fixed fixture

Definition/static gate; correctness/reconciliation; integration/serving/security. Fixed fixture phủ null, duplicate, refund, late arrival, SCD change và fiscal boundary. Fifteen metrics × three grains × six cases tạo 270 metric-cell assertions nếu mọi metric áp cả 18 cells; exceptions phải có reason, không âm thầm bỏ. Oracle do reviewer khác viết từ contract và atomic sources.

## 5. Serving và security

Hai consumer types gửi canonical equivalent requests và so values/cutoff/version. Metric-, row- và column-level policies có negative tests; inference control ghi threat assumptions. Cache key/isolation mang security context và semantic version; definition/policy change invalidates old entries. p95, freshness, hit rate, concurrency và cost/query được đo trên workload định nghĩa trước.

## 6. Breaking migration và lifecycle

Chọn một metric có meaningful v2, không tạo breaking change giả. Chạy v1/v2 parallel trên same dataset/cycle, lập delta report, notify/approve consumers, cut over alias và hoàn tất deprecation record. Catalog giữ five states và three owner roles. Reviewer đổi grain, cutoff hoặc business rule; impact analysis phải tìm downstream metrics, cached artifacts, tests và consumers trước khi sửa.

## 7. Sáu automatic-fail gates

Thiếu population/time/grain/owner; silent double count; dashboard consensus là correctness evidence duy nhất; overwrite formula; cache thiếu security/version context; compiler green không reconciliation. Gate report cần artifact locator và exact failing invariant. Presentation không cứu fail. Final dossier gồm nine deliverables, hashes, environment, unresolved risks và owner approvals; lab completion không được gọi production certification.

## 8. Ma trận kiểm chứng từng mệnh đề

Mỗi mệnh đề dưới đây cần observation, fixture hoặc artifact có thể lưu. Tên công nghệ, consensus hoặc output nhìn hợp lý không tự là bằng chứng.

### 8.1. revenue boundary phải phân biệt booking billing cash recognition

**Mệnh đề cần kiểm.** revenue boundary phải phân biệt booking billing cash recognition.

**Cách kiểm.** Audit nine deliverables bằng hashes và traceability; chạy fixed six-case reconciliation, join proof, two-consumer parity, negative access/cache tests và breaking migration drill trên synthetic environment. Với riêng mệnh đề này, ghi input/context, expected observation, failure signal và boundary làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu contract/decision version, fixture hoặc interview evidence, command/checklist output, reviewer và artifact hash. Nếu chưa thực hiện lab, trạng thái chỉ là protocol; không ghi thành kết quả đã quan sát.

### 8.2. 15 metrics phải thuộc at least five types

**Mệnh đề cần kiểm.** 15 metrics phải thuộc at least five types.

**Cách kiểm.** Audit nine deliverables bằng hashes và traceability; chạy fixed six-case reconciliation, join proof, two-consumer parity, negative access/cache tests và breaking migration drill trên synthetic environment. Với riêng mệnh đề này, ghi input/context, expected observation, failure signal và boundary làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu contract/decision version, fixture hoặc interview evidence, command/checklist output, reviewer và artifact hash. Nếu chưa thực hiện lab, trạng thái chỉ là protocol; không ghi thành kết quả đã quan sát.

### 8.3. aliases không tính là type coverage

**Mệnh đề cần kiểm.** aliases không tính là type coverage.

**Cách kiểm.** Audit nine deliverables bằng hashes và traceability; chạy fixed six-case reconciliation, join proof, two-consumer parity, negative access/cache tests và breaking migration drill trên synthetic environment. Với riêng mệnh đề này, ghi input/context, expected observation, failure signal và boundary làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu contract/decision version, fixture hoặc interview evidence, command/checklist output, reviewer và artifact hash. Nếu chưa thực hiện lab, trạng thái chỉ là protocol; không ghi thành kết quả đã quan sát.

### 8.4. each metric needs six-part contract

**Mệnh đề cần kiểm.** each metric needs six-part contract.

**Cách kiểm.** Audit nine deliverables bằng hashes và traceability; chạy fixed six-case reconciliation, join proof, two-consumer parity, negative access/cache tests và breaking migration drill trên synthetic environment. Với riêng mệnh đề này, ghi input/context, expected observation, failure signal và boundary làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu contract/decision version, fixture hoặc interview evidence, command/checklist output, reviewer và artifact hash. Nếu chưa thực hiện lab, trạng thái chỉ là protocol; không ghi thành kết quả đã quan sát.

### 8.5. three models need declared grain entities time

**Mệnh đề cần kiểm.** three models need declared grain entities time.

**Cách kiểm.** Audit nine deliverables bằng hashes và traceability; chạy fixed six-case reconciliation, join proof, two-consumer parity, negative access/cache tests và breaking migration drill trên synthetic environment. Với riêng mệnh đề này, ghi input/context, expected observation, failure signal và boundary làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu contract/decision version, fixture hoặc interview evidence, command/checklist output, reviewer và artifact hash. Nếu chưa thực hiện lab, trạng thái chỉ là protocol; không ghi thành kết quả đã quan sát.

### 8.6. join proof cần multiplicity and unmatched

**Mệnh đề cần kiểm.** join proof cần multiplicity and unmatched.

**Cách kiểm.** Audit nine deliverables bằng hashes và traceability; chạy fixed six-case reconciliation, join proof, two-consumer parity, negative access/cache tests và breaking migration drill trên synthetic environment. Với riêng mệnh đề này, ghi input/context, expected observation, failure signal và boundary làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu contract/decision version, fixture hoặc interview evidence, command/checklist output, reviewer và artifact hash. Nếu chưa thực hiện lab, trạng thái chỉ là protocol; không ghi thành kết quả đã quan sát.

### 8.7. compiler green không thay oracle

**Mệnh đề cần kiểm.** compiler green không thay oracle.

**Cách kiểm.** Audit nine deliverables bằng hashes và traceability; chạy fixed six-case reconciliation, join proof, two-consumer parity, negative access/cache tests và breaking migration drill trên synthetic environment. Với riêng mệnh đề này, ghi input/context, expected observation, failure signal và boundary làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu contract/decision version, fixture hoặc interview evidence, command/checklist output, reviewer và artifact hash. Nếu chưa thực hiện lab, trạng thái chỉ là protocol; không ghi thành kết quả đã quan sát.

### 8.8. fixed fixture có six edge cases

**Mệnh đề cần kiểm.** fixed fixture có six edge cases.

**Cách kiểm.** Audit nine deliverables bằng hashes và traceability; chạy fixed six-case reconciliation, join proof, two-consumer parity, negative access/cache tests và breaking migration drill trên synthetic environment. Với riêng mệnh đề này, ghi input/context, expected observation, failure signal và boundary làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu contract/decision version, fixture hoặc interview evidence, command/checklist output, reviewer và artifact hash. Nếu chưa thực hiện lab, trạng thái chỉ là protocol; không ghi thành kết quả đã quan sát.

### 8.9. 15x3x6 yields 270 assertions when applicable

**Mệnh đề cần kiểm.** 15x3x6 yields 270 assertions when applicable.

**Cách kiểm.** Audit nine deliverables bằng hashes và traceability; chạy fixed six-case reconciliation, join proof, two-consumer parity, negative access/cache tests và breaking migration drill trên synthetic environment. Với riêng mệnh đề này, ghi input/context, expected observation, failure signal và boundary làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu contract/decision version, fixture hoặc interview evidence, command/checklist output, reviewer và artifact hash. Nếu chưa thực hiện lab, trạng thái chỉ là protocol; không ghi thành kết quả đã quan sát.

### 8.10. exceptions need explicit reason

**Mệnh đề cần kiểm.** exceptions need explicit reason.

**Cách kiểm.** Audit nine deliverables bằng hashes và traceability; chạy fixed six-case reconciliation, join proof, two-consumer parity, negative access/cache tests và breaking migration drill trên synthetic environment. Với riêng mệnh đề này, ghi input/context, expected observation, failure signal và boundary làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu contract/decision version, fixture hoặc interview evidence, command/checklist output, reviewer và artifact hash. Nếu chưa thực hiện lab, trạng thái chỉ là protocol; không ghi thành kết quả đã quan sát.

### 8.11. two consumers need canonical parity

**Mệnh đề cần kiểm.** two consumers need canonical parity.

**Cách kiểm.** Audit nine deliverables bằng hashes và traceability; chạy fixed six-case reconciliation, join proof, two-consumer parity, negative access/cache tests và breaking migration drill trên synthetic environment. Với riêng mệnh đề này, ghi input/context, expected observation, failure signal và boundary làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu contract/decision version, fixture hoặc interview evidence, command/checklist output, reviewer và artifact hash. Nếu chưa thực hiện lab, trạng thái chỉ là protocol; không ghi thành kết quả đã quan sát.

### 8.12. cache needs security and semantic version

**Mệnh đề cần kiểm.** cache needs security and semantic version.

**Cách kiểm.** Audit nine deliverables bằng hashes và traceability; chạy fixed six-case reconciliation, join proof, two-consumer parity, negative access/cache tests và breaking migration drill trên synthetic environment. Với riêng mệnh đề này, ghi input/context, expected observation, failure signal và boundary làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu contract/decision version, fixture hoặc interview evidence, command/checklist output, reviewer và artifact hash. Nếu chưa thực hiện lab, trạng thái chỉ là protocol; không ghi thành kết quả đã quan sát.

### 8.13. breaking migration needs parallel delta approval

**Mệnh đề cần kiểm.** breaking migration needs parallel delta approval.

**Cách kiểm.** Audit nine deliverables bằng hashes và traceability; chạy fixed six-case reconciliation, join proof, two-consumer parity, negative access/cache tests và breaking migration drill trên synthetic environment. Với riêng mệnh đề này, ghi input/context, expected observation, failure signal và boundary làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu contract/decision version, fixture hoặc interview evidence, command/checklist output, reviewer và artifact hash. Nếu chưa thực hiện lab, trạng thái chỉ là protocol; không ghi thành kết quả đã quan sát.

### 8.14. changed constraint requires impact analysis

**Mệnh đề cần kiểm.** changed constraint requires impact analysis.

**Cách kiểm.** Audit nine deliverables bằng hashes và traceability; chạy fixed six-case reconciliation, join proof, two-consumer parity, negative access/cache tests và breaking migration drill trên synthetic environment. Với riêng mệnh đề này, ghi input/context, expected observation, failure signal và boundary làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu contract/decision version, fixture hoặc interview evidence, command/checklist output, reviewer và artifact hash. Nếu chưa thực hiện lab, trạng thái chỉ là protocol; không ghi thành kết quả đã quan sát.

### 8.15. automatic fail cannot be waived by presentation

**Mệnh đề cần kiểm.** automatic fail cannot be waived by presentation.

**Cách kiểm.** Audit nine deliverables bằng hashes và traceability; chạy fixed six-case reconciliation, join proof, two-consumer parity, negative access/cache tests và breaking migration drill trên synthetic environment. Với riêng mệnh đề này, ghi input/context, expected observation, failure signal và boundary làm kết luận không còn đúng.

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
1. [[SRC-DBT-SEMANTIC-MODELS]]
2. [[SRC-KIMBALL-ROSS-DW-TOOLKIT-3E]]
3. [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-DBT-SEMANTIC-MODELS]] | Khái niệm, cơ chế hoặc decision boundary liên quan | Đã đọc locator được ghi trong source record; không suy ngoài phạm vi |
| [[SRC-KIMBALL-ROSS-DW-TOOLKIT-3E]] | Khái niệm, cơ chế hoặc decision boundary liên quan | Đã đọc locator được ghi trong source record; không suy ngoài phạm vi |
| [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]] | Khái niệm, cơ chế hoặc decision boundary liên quan | Đã đọc locator được ghi trong source record; không suy ngoài phạm vi |

## Key takeaways
- Chọn kiến trúc và data product từ decision/constraints, không từ độ mới của công nghệ.
- Metric governance cần versioned evidence, lifecycle gates và owner có quyền rõ.
- Failure matrix chỉ hữu dụng khi mỗi dòng có detector hoặc control kiểm được.
- Capstone là hồ sơ bằng chứng tích hợp, không phải bộ YAML hay dashboard trình diễn.
- Discovery phải cho phép kết luận không xây analytics product.
