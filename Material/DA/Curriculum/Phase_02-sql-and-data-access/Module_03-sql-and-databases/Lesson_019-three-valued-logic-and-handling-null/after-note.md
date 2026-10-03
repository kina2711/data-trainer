# Phase 2: Data Analyst
# Module 3: SQL and Databases
# Lesson 19: Three-valued logic and handling NULL

## Thực hành

**Nhiệm vụ.** Dự đoán kết quả 15 biểu thức chứa `NULL` và giải thích cả 15. Trên `orders.csv`, xử lý cột `Tinh` thiếu ở 6% số dòng theo ba cách khác nhau và so sánh hậu quả lên giá trị trung bình.

Giữ input snapshot, grain, identity, version, raw output, reconciliation và limitation.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Kiểm hai phần: phần dự đoán 15 biểu thức có đáp án xác định, và phần chọn cách xử lý phải kèm lý do ngữ nghĩa vì cùng một cột `NULL` có thể cần ba cách xử lý khác nhau tuỳ nghĩa.

**Điều kiện đạt.** Dự đoán đúng ≥ 13/15 biểu thức, và ba cách xử lý `NULL` trên `orders.csv` đều có lý do ngữ nghĩa kèm con số hậu quả.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 60 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 25 phút trả lời bốn câu kiểm tra · 15 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dùng `= NULL` thay vì `IS NULL` · thay `NULL` bằng 0 khi nghĩa là chưa nhập · quên `NULL` bị loại khỏi `COUNT(cot)` nhưng không bị loại khỏi `COUNT(*)`.

## Reference
- Knowledge note: `Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/019-three-valued-logic-and-handling-null.md`
