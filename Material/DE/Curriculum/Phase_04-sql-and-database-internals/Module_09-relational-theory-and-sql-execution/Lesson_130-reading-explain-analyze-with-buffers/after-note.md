# Phase 4: SQL and Database Internals
# Module 9: Relational Theory and SQL Execution
# Lesson 130: Reading EXPLAIN ANALYZE with buffers

## Thực hành

**Nhiệm vụ.** Cho năm kế hoạch thực thi của năm truy vấn chậm vì năm nguyên nhân khác nhau. Với mỗi kế hoạch, chạy quy trình bốn bước, định vị nút tốn nhất, và quy nguyên nhân. Với một truy vấn, so thời gian trong kế hoạch với thời gian chạy thật và giải thích chênh lệch.

Lưu SQL, dữ liệu sinh, tham số, dự đoán trước khi chạy, plan dạng máy đọc được, output thô, đối soát và thông số môi trường. Chỉ chạy `EXPLAIN ANALYZE`, DML, tải dữ liệu, thao tác cache, `pageinspect` hoặc extension trong PostgreSQL thử nghiệm cô lập; không dùng production để tạo cold cache hay benchmark. Ảnh chụp không thay artifact tái chạy.

## Kiểm tra cuối bài

1. Vì sao không được cộng thời gian của mọi plan node?
2. Actual rows và time phải diễn giải cùng loops thế nào?
3. Shared read có đồng nghĩa physical disk read không?
4. Node lệch ước lượng đầu tiên giúp định tuyến chẩn đoán ra sao?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective là kỹ năng đọc bằng chứng, điều kiện cho bài dự án ở lesson 132. Kiểm bằng năm kế hoạch; đạt khi định vị đúng nút tốn nhất ở ít nhất bốn và quy đúng nguyên nhân ở ít nhất ba.

**Điều kiện đạt.** Định vị đúng nút tốn nhất ở ≥ 4/5 kế hoạch và quy đúng nguyên nhân ở ≥ 3/5, kèm bốn con số dẫn chứng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đọc kế hoạch từ ngoài vào · chỉ nhìn thời gian mà bỏ số dòng · bỏ qua số khối đọc · so thời gian trong kế hoạch với thời gian chạy thật.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/18-reading-explain-analyze-with-buffers.md`
- Nội dung học thuật: `note.md` cùng thư mục.
