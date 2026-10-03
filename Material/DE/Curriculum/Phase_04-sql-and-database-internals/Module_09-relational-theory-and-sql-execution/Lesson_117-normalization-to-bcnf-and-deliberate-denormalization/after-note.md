# Phase 4: SQL and Database Internals
# Module 9: Relational Theory and SQL Execution
# Lesson 117: Normalization to BCNF, and deliberate denormalization

## Thực hành

**Nhiệm vụ.** Từ một bảng phẳng, tự tạo ra cả ba dị thường bằng dữ liệu thật. Chuẩn hoá từng bước và chỉ ra bước nào chữa dị thường nào. Sau đó chọn một đường đọc và phi chuẩn hoá, đo tác động lên tốc độ đọc, tốc độ ghi và dung lượng. Nêu đường ghi nào chịu trách nhiệm giữ đồng bộ.

Lưu SQL, seed data, prediction trước khi chạy, output thô, đối soát và giải thích theo rule. Ảnh chụp không thay artifact chạy lại được.

## Kiểm tra cuối bài

1. Ba anomaly là gì?
2. 3NF khác BCNF ở đâu?
3. Lossless khác preservation thế nào?
4. Denormalization cần writer nào?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi nối mỗi bước chuẩn hoá với một dị thường cụ thể, chứ áp quy tắc. Kiểm bằng bài chuẩn hoá cộng đo; đạt khi mỗi bước gắn đúng dị thường và phần phi chuẩn hoá có số đo ba chiều.

**Điều kiện đạt.** Ba dị thường được tái hiện và gắn đúng bước chữa, và phần phi chuẩn hoá có số đo cả đọc, ghi lẫn dung lượng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Học thuộc định nghĩa dạng chuẩn mà không nhận ra dị thường trong bảng thật · chuẩn hoá tới mức mọi truy vấn phải kết mười bảng · phi chuẩn hoá mà không có cơ chế giữ đồng bộ.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/05-normalization-to-bcnf-and-deliberate-denormalization.md`
- Nội dung học thuật: `note.md` cùng thư mục.
