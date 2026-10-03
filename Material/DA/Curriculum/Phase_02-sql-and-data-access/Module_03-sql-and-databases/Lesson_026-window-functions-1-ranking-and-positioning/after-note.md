# Phase 2: Data Analyst
# Module 3: SQL and Databases
# Lesson 26: Window functions (1) - ranking and positioning

## Thực hành

**Nhiệm vụ.** Ba sản phẩm bán chạy nhất mỗi chi nhánh. Đơn hàng gần nhất của mỗi khách. Chia khách thành 5 nhóm ngũ phân vị theo chi tiêu. Dữ liệu có chứa giá trị trùng ở cả ba bài.

Giữ input snapshot, grain, identity, version, raw output, reconciliation và limitation.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Kiểm bằng bài có cài giá trị trùng: bốn hàm cho bốn kết quả khác nhau trên cùng dữ liệu, nên chọn sai hàm sẽ hiện ra ở số dòng kết quả. Yêu cầu nộp kèm một câu nêu lý do chọn hàm.

**Điều kiện đạt.** Cả ba bài cho số dòng đúng trên dữ liệu có giá trị trùng, và mỗi bài kèm lý do chọn hàm xếp hạng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 60 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 25 phút trả lời bốn câu kiểm tra · 15 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dùng `RANK` khi nghiệp vụ cần đúng N dòng · đặt hàm cửa sổ trong `WHERE` · thiếu `PARTITION BY` nên xếp hạng trên toàn bảng.

## Reference
- Knowledge note: `Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/026-window-functions-1-ranking-and-positioning.md`
