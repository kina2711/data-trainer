# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 16: Data Ingestion and Integration Engineering
# Lesson 236: Rate Limits Retry Budgets and Source Protection

## Thực hành

**Nhiệm vụ.** Dựng nguồn mô phỏng có hạn mức, có trả lỗi tạm thời ngẫu nhiên và có đồng hồ đặt lại ở múi giờ khác. Cài lớp gọi có phân loại lỗi, ngân sách thử lại, lùi dần có nhiễu, và điều chỉnh đồng thời. Chạy tải và đo số lần vượt hạn mức. Tái hiện phản hồi thất lạc sau một yêu cầu ghi và chứng minh không nhân đôi.

Lưu source boundary, fixture hashes, versions, requests/queries, checkpoints, raw outputs, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu entity/change contract.
2. Tái hiện một assumption failure.
3. Chứng minh checkpoint/retry không tạo silent gap.
4. Đối soát bằng key và typed hash.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu đo được ở phía nguồn. Kiểm bằng phép thử tải; đạt khi không lần nào vượt hạn mức, số lần thử lại nằm trong ngân sách, và không có tác dụng phụ trùng lặp.

**Điều kiện đạt.** Không lần nào vượt hạn mức nguồn dưới tải, số lần thử lại trong ngân sách, và phản hồi thất lạc không tạo tác dụng phụ trùng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Thử lại không giới hạn · thử lại lỗi vĩnh viễn · lùi dần không có nhiễu nên các tiến trình đồng loạt quay lại · chạy nạp bù chung hạn mức với lần chạy hằng ngày.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/124-rate-limits-retry-budgets-source-protection.md`
- Nội dung học thuật: `note.md` cùng thư mục.
