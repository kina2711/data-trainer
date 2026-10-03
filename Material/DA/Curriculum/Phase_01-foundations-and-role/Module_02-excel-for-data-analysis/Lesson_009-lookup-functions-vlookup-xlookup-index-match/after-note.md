# Phase 1: Data Analyst
# Module 2: Excel for Data Analysis
# Lesson 9: Lookup functions - VLOOKUP, XLOOKUP, INDEX-MATCH

## Thực hành

**Nhiệm vụ.** Ghép bảng đơn hàng 2.000 dòng với bảng sản phẩm. Trong dữ liệu có 14 mã sản phẩm không khớp. Truy nguyên và phân loại cả 14 theo nhóm nguyên nhân.

Giữ input snapshot, grain, identity, version, raw output, reconciliation và limitation.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Phần khó của bài không phải viết hàm mà là truy nguyên vì sao một mã không khớp — mã bị đổi, khoảng trắng thừa, hay khác biệt chữ hoa chữ thường. Kiểm bằng báo cáo truy nguyên: mỗi mã không khớp phải được gán một nguyên nhân có bằng chứng, không chấp nhận gán chung.

**Điều kiện đạt.** Cả 14 mã không khớp được gán nguyên nhân có bằng chứng, và tổng sau ghép khớp với tổng trước ghép.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 60 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 25 phút trả lời bốn câu kiểm tra · 15 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Bỏ đối số tra cứu chính xác của `VLOOKUP` · bọc `IFERROR` quanh `#N/A` trước khi truy nguyên · dùng `VLOOKUP` rồi chèn cột làm hỏng chỉ số.

## Reference
- Knowledge note: `Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/009-lookup-functions-vlookup-xlookup-index-match.md`
