# Phase 4: SQL and Database Internals
# Module 9: Relational Theory and SQL Execution
# Lesson 114: NULL and three-valued logic

## Thực hành

**Nhiệm vụ.** Cho 15 biểu thức chứa `NULL` trong sáu ngữ cảnh. Viết dự đoán trước, chạy, đối chiếu. Trên một bảng có cột thiếu dữ liệu, tính trung bình theo ba cách xử lý khác nhau và so ba kết quả. Viết một câu cho mỗi cách nêu nó phù hợp nghĩa nghiệp vụ nào.

Lưu SQL, seed data, prediction trước khi chạy, output thô, đối soát và giải thích theo rule. Ảnh chụp không thay artifact chạy lại được.

## Kiểm tra cuối bài

1. Vì sao WHERE loại UNKNOWN?
2. NOT IN có NULL hỏng thế nào?
3. AVG dùng denominator nào?
4. Khi nào COALESCE làm sai nghĩa?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một kỹ năng dự đoán kiểm được ngay, và là nguồn lỗi âm thầm nên phải kiểm kỹ. Kiểm bằng bài dự đoán 15 biểu thức; đạt khi đúng ≥ 13 và giải thích được bằng logic ba trạng thái.

**Điều kiện đạt.** Dự đoán đúng ≥ 13/15 biểu thức, và ba cách tính trung bình được gán đúng nghĩa nghiệp vụ.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dùng `= NULL` thay vì `IS NULL` · thay mọi `NULL` bằng số không · quên rằng điều kiện khác giá trị loại luôn dòng `NULL` · gộp ba nghĩa làm một.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/02-null-and-three-valued-logic.md`
- Nội dung học thuật: `note.md` cùng thư mục.
