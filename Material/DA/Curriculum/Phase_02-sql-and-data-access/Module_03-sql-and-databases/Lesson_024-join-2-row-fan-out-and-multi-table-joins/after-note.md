# Phase 2: Data Analyst
# Module 3: SQL and Databases
# Lesson 24: JOIN (2) - row fan-out and multi-table joins

## Thực hành

**Nhiệm vụ.** Trên `DS1`, ghép 5 bảng để ra báo cáo doanh thu theo khách hàng × sản phẩm. Chứng minh tổng khớp với tổng tính trực tiếp từ bảng hoá đơn.

Giữ input snapshot, grain, identity, version, raw output, reconciliation và limitation.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Kiểm bằng nghĩa vụ chứng minh: nộp kèm phép đếm trước và sau mỗi phép ghép, và phép đối chiếu tổng doanh thu với tổng tính trực tiếp từ bảng hoá đơn. Truy vấn không kèm bằng chứng không được chấm.

**Điều kiện đạt.** Tổng doanh thu từ truy vấn 5 bảng khớp tuyệt đối với tổng từ bảng hoá đơn, và nộp đủ phép đếm dòng tại mỗi bước ghép.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 60 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 25 phút trả lời bốn câu kiểm tra · 15 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Ghép bảng chi tiết vào bảng tổng rồi cộng cột tổng · đặt điều kiện bảng phải vào `WHERE` sau `LEFT JOIN` · không đếm dòng trước và sau nên không phát hiện nhân bản.

## Reference
- Knowledge note: `Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/024-join-2-row-fan-out-and-multi-table-joins.md`
