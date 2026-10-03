# Phase 2: Data Analyst
# Module 3: SQL and Databases
# Lesson 25: Subqueries and CTEs

## Thực hành

**Nhiệm vụ.** Nhận một truy vấn 80 dòng lồng bốn tầng, tái cấu trúc thành 5 CTE. Sau đó làm chiều ngược lại: từ một bài toán mới, viết thẳng bằng CTE.

Giữ input snapshot, grain, identity, version, raw output, reconciliation và limitation.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Kiểm hai điều kiện: kết quả trước và sau tái cấu trúc phải khớp từng dòng, và một học viên khác phải giải thích được luồng dữ liệu chỉ bằng cách đọc tên CTE. Điều kiện thứ hai không kiểm được bằng máy nên dùng rà soát chéo.

**Điều kiện đạt.** Kết quả sau tái cấu trúc khớp từng dòng với kết quả gốc, và một học viên khác giải thích được luồng dữ liệu chỉ từ tên CTE.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 60 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 25 phút trả lời bốn câu kiểm tra · 15 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đặt tên CTE theo thao tác nên tên không mang thông tin về hạt · dùng truy vấn con tương quan ở nơi `JOIN` làm được · thay `NOT EXISTS` bằng `NOT IN` trên tập có `NULL`.

## Reference
- Knowledge note: `Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/025-subqueries-and-ctes.md`
