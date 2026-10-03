# Phase 4: SQL and Database Internals
# Module 9: Relational Theory and SQL Execution
# Lesson 122: Recursive CTEs for hierarchies and graphs

## Thực hành

**Nhiệm vụ.** Trên bảng cây tổ chức, viết ba truy vấn đệ quy: liệt kê toàn bộ cấp dưới, truy ngược chuỗi quản lý, và tính tổng ngân sách theo nhánh. Chèn một chu trình vào dữ liệu và chứng minh truy vấn có chống chu trình vẫn dừng còn bản không có thì treo. Với bài recursion, mọi truy vấn cố ý không kết thúc phải chạy trong môi trường cô lập dưới `statement_timeout`; không được để query treo không kiểm soát.

Lưu SQL, seed data, dự đoán trước khi chạy, output thô, đối soát độc lập và giải thích theo rule. Ảnh chụp không thay artifact chạy lại được.

## Kiểm tra cuối bài

1. Anchor và working table phối hợp ra sao?
2. UNION vì sao không luôn chặn cycle?
3. SEARCH có điều khiển evaluation order không?
4. Unsafe recursion phải được thử dưới lớp bảo vệ nào?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một kỹ thuật cụ thể có ba điều kiện an toàn kiểm được. Kiểm bằng ba bài toán cộng một tập dữ liệu có chu trình; đạt khi cả ba đúng và truy vấn không treo trên dữ liệu có chu trình.

**Điều kiện đạt.** Ba truy vấn cho kết quả đúng, và bản có chống chu trình dừng được trên dữ liệu có chu trình trong khi bản không có thì treo.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Quên điều kiện dừng · không chống chu trình · không đặt giới hạn độ sâu · dùng đệ quy cho đồ thị rất lớn mà chưa cân nhắc bảng đường đi tính sẵn.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/10-recursive-ctes-for-hierarchies-and-graphs.md`
- Nội dung học thuật: `note.md` cùng thư mục.
