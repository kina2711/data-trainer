# Phase 4: SQL and Database Internals
# Module 9: Relational Theory and SQL Execution
# Lesson 116: ER modelling and what the database should enforce

## Thực hành

**Nhiệm vụ.** Từ mô tả nghiệp vụ một hệ đặt hàng có quan hệ nhiều nhiều, dựng lược đồ đầy đủ ràng buộc. Chèn tám bản ghi sai theo tám cách và chứng minh cả tám bị chặn. Thử ba hành vi xoá bản ghi cha khác nhau và ghi kết quả từng cái.

Lưu SQL, seed data, prediction trước khi chạy, output thô, đối soát và giải thích theo rule. Ảnh chụp không thay artifact chạy lại được.

## Kiểm tra cuối bài

1. Cardinality khác participation thế nào?
2. M:N cần junction vì sao?
3. Delete action là policy gì?
4. Bỏ FK cần controls nào?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một thiết kế có tiêu chí nghiệm thu bằng phép thử chèn dữ liệu sai. Kiểm bằng tám phép thử phủ định; đạt khi cả tám bị chặn và thông báo lỗi nêu đúng ràng buộc.

**Điều kiện đạt.** Tám phép thử phủ định đều bị chặn với thông báo nêu đúng ràng buộc, và ba hành vi xoá được ghi kết quả rõ ràng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Quên bảng nối cho quan hệ nhiều nhiều · bỏ khoá ngoại vì thấy chậm mà chưa đo · đặt hành vi xoá lan toả cho bảng có dữ liệu lịch sử · không thử chèn dữ liệu sai.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/04-er-modelling-and-database-enforcement.md`
- Nội dung học thuật: `note.md` cùng thư mục.
