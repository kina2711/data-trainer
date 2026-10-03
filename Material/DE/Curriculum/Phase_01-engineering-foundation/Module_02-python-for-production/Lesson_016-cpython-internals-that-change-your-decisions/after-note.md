# Phase 1: Engineering Foundation
# Module 2: Python for Production
# Lesson 16: CPython internals that change your decisions

## Thực hành

**Nhiệm vụ.** Chạy cùng một tác vụ ở ba cấu hình một luồng, nhiều luồng và nhiều tiến trình, trên hai loại khối lượng công việc: một thiên CPU và một thiên vào ra. Lập bảng sáu ô. Giải thích từng ô bằng cơ chế khoá. Tạo một vòng tham chiếu và quan sát bộ nhớ không về cho tới khi bộ dọn chu trình chạy.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Objective là bác bỏ một hiểu lầm phổ biến bằng cơ chế cộng số đo. Kiểm bằng thí nghiệm hai loại khối lượng công việc; đạt khi số đo cho thấy đúng chiều và giải thích đúng vai trò của khoá.

**Điều kiện đạt.** Bảng sáu ô có số đo thật, và giải thích đúng vì sao luồng thắng ở khối lượng công việc thiên vào ra.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Kết luận luồng vô dụng trong Python · dùng nhiều tiến trình cho tác vụ thiên vào ra · bỏ qua chi phí khởi động tiến trình khi so · đo một lần rồi kết luận.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/016-cpython-internals-decisions.md`
- Nội dung học thuật: `note.md` cùng thư mục.
