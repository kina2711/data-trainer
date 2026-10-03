# Phase 2: Data Analyst
# Module 3: SQL and Databases
# Lesson 21: CASE WHEN and data classification

## Thực hành

**Nhiệm vụ.** Phân khúc khách hàng theo giá trị đơn. Xoay doanh thu theo tháng thành 12 cột. Đếm số đơn theo trạng thái trên cùng một dòng.

Giữ input snapshot, grain, identity, version, raw output, reconciliation và limitation.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Kiểm bằng ràng buộc số học: tổng các nhóm phải bằng tổng toàn bảng. Ràng buộc này bắt được cả hai lỗi phổ biến — thiếu `ELSE` làm rơi bản ghi, và nhánh chồng lấn làm đếm trùng.

**Điều kiện đạt.** Tổng theo nhóm bằng tổng toàn bảng ở cả ba bài lab, và không nhóm nào chứa bản ghi `NULL` ngoài ý định.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 60 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 25 phút trả lời bốn câu kiểm tra · 15 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Thiếu `ELSE` nên bản ghi không khớp nhánh nào rơi vào `NULL` · thứ tự nhánh làm nhóm rộng nuốt nhóm hẹp · nhánh chồng lấn gây đếm trùng.

## Reference
- Knowledge note: `Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/021-case-when-and-data-classification.md`
