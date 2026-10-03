# Phase 4: SQL and Database Internals
# Module 9: Relational Theory and SQL Execution
# Lesson 120: Aggregation, HAVING and the grain statement

## Thực hành

**Nhiệm vụ.** Viết 20 truy vấn gộp trên dữ liệu thật, mỗi truy vấn nộp kèm phát biểu hạt trước và sau. Với ba truy vấn, dùng cả ba biến thể đếm và giải thích ba con số khác nhau. Đổi bài: người khác đọc phát biểu hạt và kiểm truy vấn có khớp phát biểu không.

Lưu SQL, seed data, dự đoán trước khi chạy, output thô, đối soát độc lập và giải thích theo rule. Ảnh chụp không thay artifact chạy lại được.

## Kiểm tra cuối bài

1. Grain trước và sau GROUP BY khác nhau thế nào?
2. Ba biến thể COUNT trả lời ba câu hỏi nào?
3. WHERE khác HAVING ở đơn vị lọc nào?
4. Vì sao aggregate cuối không sửa fanout?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một kỷ luật phát biểu kiểm được bằng rà soát, và là nền cho toàn phần mô hình hoá sau. Kiểm bằng 20 truy vấn gộp; đạt khi mọi truy vấn có phát biểu hạt đúng và ba biến thể đếm dùng đúng chỗ.

**Điều kiện đạt.** Cả 20 truy vấn có phát biểu hạt đúng và khớp truy vấn, và ba biến thể đếm được giải thích đúng nghĩa.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Bỏ phát biểu hạt vì thấy hiển nhiên · dùng đếm mọi dòng khi cần đếm giá trị phân biệt · báo trung bình trên dữ liệu lệch mà không kèm phân bố · quên rằng gộp đổi hạt nên tổng không còn cộng được như trước.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/08-aggregation-having-and-grain-statement.md`
- Nội dung học thuật: `note.md` cùng thư mục.
