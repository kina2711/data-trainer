# Phase 4: SQL and Database Internals
# Module 9: Relational Theory and SQL Execution
# Lesson 121: Subqueries, CTEs and the materialization caveat

## Thực hành

**Nhiệm vụ.** Nhận một truy vấn 80 dòng lồng bốn tầng. Tái cấu trúc thành năm biểu thức bảng chung đặt tên theo hạt. Đối soát kết quả. So kế hoạch và thời gian hai bản. Viết một truy vấn mà biểu thức bảng chung chặn việc đẩy điều kiện lọc và chứng minh bằng kế hoạch.

Lưu SQL, seed data, dự đoán trước khi chạy, output thô, đối soát độc lập và giải thích theo rule. Ảnh chụp không thay artifact chạy lại được.

## Kiểm tra cuối bài

1. CTE logic khác ranh giới vật lý thế nào?
2. Khi nào materialization chặn pushdown?
3. NOT IN gặp NULL có rủi ro gì?
4. Parity bằng EXCEPT ALL hai chiều chứng minh gì?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective gồm cả một cảnh báo về hiệu năng kiểm được bằng kế hoạch. Kiểm bằng bài tái cấu trúc cộng so kế hoạch; đạt khi kết quả khớp tuyệt đối và nhận ra đúng trường hợp vật chất hoá gây chậm.

**Điều kiện đạt.** Kết quả tái cấu trúc khớp tuyệt đối, tên các bước đặt theo hạt, và chỉ ra được bằng kế hoạch trường hợp vật chất hoá chặn tối ưu.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đặt tên biểu thức bảng chung là `t1` hay `tam2` · dùng danh sách giá trị với truy vấn con có `NULL` · giả định biểu thức bảng chung luôn miễn phí · để truy vấn con tương quan trong vòng lặp lớn.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/09-subqueries-ctes-and-materialization.md`
- Nội dung học thuật: `note.md` cùng thư mục.
