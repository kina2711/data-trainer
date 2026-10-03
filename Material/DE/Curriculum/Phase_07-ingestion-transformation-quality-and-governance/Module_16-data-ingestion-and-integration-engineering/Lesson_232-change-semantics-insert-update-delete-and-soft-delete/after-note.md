# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 16: Data Ingestion and Integration Engineering
# Lesson 232: Source Change Semantics and Delete Visibility

## Thực hành

**Nhiệm vụ.** Với bốn thực thể, thiết kế phép dò: chụp hai lần cách nhau và so tập khoá để phát hiện xoá cứng; so nội dung để phát hiện sửa bản ghi cũ; kiểm tính đơn điệu của dấu thời gian. Đối chiếu kết quả với tài liệu nguồn và ghi lại mọi chỗ lệch. Với mỗi thực thể, suy ra yêu cầu kỹ thuật cho bước trích xuất.

Lưu source boundary, fixture hashes, versions, requests/queries, checkpoints, raw outputs, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu entity/change contract.
2. Tái hiện một assumption failure.
3. Chứng minh checkpoint/retry không tạo silent gap.
4. Đối soát bằng key và typed hash.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi kiểm chứng bằng dữ liệu thay vì tin tài liệu. Kiểm bằng phép dò thực nghiệm; đạt khi bốn thực thể có kết luận dựa trên bằng chứng và phát hiện được ít nhất một chỗ tài liệu sai.

**Điều kiện đạt.** Bốn thực thể có kết luận dựa trên bằng chứng thực nghiệm, và ít nhất một chỗ tài liệu sai được phát hiện.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Tin tài liệu nói không có xoá cứng · bỏ qua khả năng lịch sử bị sửa · coi dấu thời gian luôn tăng · kết luận từ một lần chụp duy nhất.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/120-source-change-semantics-delete-visibility.md`
- Nội dung học thuật: `note.md` cùng thư mục.
