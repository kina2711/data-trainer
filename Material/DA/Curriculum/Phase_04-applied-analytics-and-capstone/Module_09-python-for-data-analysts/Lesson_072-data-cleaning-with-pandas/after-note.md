# Phase 4: Data Analyst
# Module 9: Python for Data Analysts
# Lesson 72: Data cleaning with pandas

## Thực hành

**Nhiệm vụ.** Làm sạch `orders_dirty.csv` bằng pandas. Kết quả phải khớp từng dòng với bản làm bằng SQL ở lesson 36, và hai lần chạy phải cho kết quả giống hệt.

Giữ input snapshot, grain, identity, version, raw output, reconciliation và limitation.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Kiểm bằng hai điều kiện: chạy hai lần cho kết quả giống hệt, và khớp từng dòng với bản làm bằng SQL ở lesson 36. Điều kiện thứ nhất bắt được lỗi khử trùng không xác định thứ tự, loại lỗi không hiện ra nếu chỉ chạy một lần.

**Điều kiện đạt.** Hai lần chạy cho kết quả giống hệt, và kết quả khớp từng dòng với bản làm bằng SQL ở lesson 36.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 60 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 25 phút trả lời bốn câu kiểm tra · 15 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** `drop_duplicates` trên dữ liệu chưa sắp xếp nên giữ bản ghi khác nhau giữa các lần chạy · `to_datetime` không chỉ định `format` nên pandas tự suy đoán · `fillna(0)` cho cột mà giá trị thiếu nghĩa là chưa nhập.

## Reference
- Knowledge note: `Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/072-data-cleaning-with-pandas.md`
