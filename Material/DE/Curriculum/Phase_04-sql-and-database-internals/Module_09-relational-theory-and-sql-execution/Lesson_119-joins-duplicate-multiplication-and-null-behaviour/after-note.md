# Phase 4: SQL and Database Internals
# Module 9: Relational Theory and SQL Execution
# Lesson 119: Joins, duplicate multiplication and NULL behaviour

## Thực hành

**Nhiệm vụ.** Ghép năm bảng để ra báo cáo doanh thu theo khách và sản phẩm. Đếm dòng sau mỗi bước kết. Đối soát tổng với tổng tính thẳng từ bảng hoá đơn. Cố ý tạo nhân bản dòng và định lượng mức thổi phồng. Đặt điều kiện bảng phải vào mệnh đề lọc dòng và chứng minh kết trái thành kết trong.

Lưu SQL, seed data, prediction trước khi chạy, output thô, đối soát và giải thích theo rule. Ảnh chụp không thay artifact chạy lại được.

## Kiểm tra cuối bài

1. Fanout tính thế nào?
2. LEFT JOIN vẫn nhân row ra sao?
3. DISTINCT che lỗi grain thế nào?
4. Reconciliation cần evidence nào?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một quy trình kiểm chứng bắt buộc chứ chỉ viết đúng cú pháp. Kiểm bằng bài ghép năm bảng; đạt khi tổng khớp tuyệt đối với tổng tính trực tiếp từ bảng gốc.

**Điều kiện đạt.** Tổng khớp tuyệt đối với bản tính trực tiếp, và định lượng được mức thổi phồng của trường hợp nhân bản cố ý.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Không đếm dòng sau khi kết · dùng phép chọn phân biệt để chữa nhân bản thay vì sửa hạt · đặt điều kiện bảng phải sai mệnh đề · quên rằng khoá `NULL` không khớp.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/07-joins-duplicate-multiplication-and-null-behaviour.md`
- Nội dung học thuật: `note.md` cùng thư mục.
