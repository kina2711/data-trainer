# Phase 10: System Design, AI Boundary and Trajectory
# Module 27: System Design Progression
# Lesson 409: Sequence 1 - a single stateful service

## Thực hành

**Nhiệm vụ.** Thiết kế ba bài toán bậc một. Với mỗi cái, truy một phép ghi và một phép đọc qua mọi thành phần và trả lời bốn câu hỏi. Với bài rút gọn địa chỉ, tính năng lực và chỉ ra khoá nóng. Với bộ giới hạn tốc độ, nêu đánh đổi giữa đếm chính xác với khả dụng khi kho trạng thái chậm. Viết chính sách vô hiệu hoá bộ nhớ đệm.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một thói quen truy vết áp cho mọi thiết kế sau. Kiểm bằng bài truy vết; đạt khi bốn câu hỏi có câu trả lời ở mọi thành phần của cả ba thiết kế và chính sách vô hiệu hoá bộ nhớ đệm được viết ra.

**Điều kiện đạt.** Bốn câu hỏi có câu trả lời ở mọi thành phần của ba thiết kế, và chính sách vô hiệu hoá bộ nhớ đệm được viết ra.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Thêm bộ nhớ đệm mà không có chính sách vô hiệu hoá · bỏ qua khoá nóng · không truy phép đọc riêng khỏi phép ghi · để ranh giới thử lại không xác định.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/297-sequence-1-a-single-stateful-service.md`
- Nội dung học thuật: `note.md` cùng thư mục.
