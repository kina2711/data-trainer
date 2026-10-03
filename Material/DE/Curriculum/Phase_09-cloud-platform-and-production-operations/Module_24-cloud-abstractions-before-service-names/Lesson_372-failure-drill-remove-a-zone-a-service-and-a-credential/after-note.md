# Phase 9: Cloud Platform and Production Operations
# Module 24: Cloud Abstractions before Service Names
# Lesson 372: Failure drill - remove a zone, a service and a credential

## Thực hành

**Nhiệm vụ.** Viết hành vi kỳ vọng cho sáu tình huống trước khi chạy. Chạy từng cái trên lát cắt nền tảng. Ghi ba số cho mỗi tình huống. Với tình huống hạn mức, chứng minh cảnh báo nổ trước khi chạm trần. Với cú sốc chi phí, tính lại chi phí trên mỗi đơn vị và đề xuất thiết kế lại. Sửa sổ tay vận hành theo chênh lệch quan sát được.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đo năng lực vận hành dưới sự cố cùng dưới ràng buộc chi phí. Kiểm bằng sáu tình huống; đạt khi ít nhất năm phục hồi trong mục tiêu thời gian đã đặt và cú sốc chi phí có phương án thiết kế lại kèm số đo trên mỗi đơn vị.

**Điều kiện đạt.** ≥ 5/6 tình huống phục hồi trong mục tiêu thời gian, cú sốc chi phí có phương án thiết kế lại kèm số đo trên mỗi đơn vị, và sổ tay được sửa.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Viết hành vi kỳ vọng sau khi thấy kết quả · xử lý cú sốc chi phí bằng cách tắt tính năng · bỏ tình huống mặt phẳng điều khiển vì khó dựng · không đo mức suy giảm mà chỉ đo phục hồi.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/260-failure-drill-remove-a-zone-a-service-and-a-credential.md`
- Nội dung học thuật: `note.md` cùng thư mục.
