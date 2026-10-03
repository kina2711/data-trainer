# Phase 4: SQL and Database Internals
# Module 9: Relational Theory and SQL Execution
# Lesson 131: Sargability, parameters and plan stability

## Thực hành

**Nhiệm vụ.** Cho sáu truy vấn, mỗi cái phá chỉ mục theo một cách. Tìm và sửa từng cái, kiểm chứng bằng kế hoạch. Trên bảng có dữ liệu lệch, chạy truy vấn tham số hoá với giá trị hiếm trước rồi giá trị phổ biến sau, và chứng minh kế hoạch không đổi dù đáng lẽ phải đổi.

Lưu SQL, dữ liệu sinh, tham số, dự đoán trước khi chạy, plan dạng máy đọc được, output thô, đối soát và thông số môi trường. Chỉ chạy `EXPLAIN ANALYZE`, DML, tải dữ liệu, thao tác cache, `pageinspect` hoặc extension trong PostgreSQL thử nghiệm cô lập; không dùng production để tạo cold cache hay benchmark. Ảnh chụp không thay artifact tái chạy.

## Kiểm tra cuối bài

1. Sargability phải được chứng minh bằng evidence nào?
2. PostgreSQL chọn generic và custom plan theo cơ chế nào?
3. Vì sao optional-filter pattern có thể làm generic plan khó tối ưu?
4. Parameterization và plan specialization cùng tồn tại thế nào?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective gồm một hiện tượng khó tái hiện mà nhiều người chưa từng thấy. Kiểm bằng sáu truy vấn cộng một thí nghiệm; đạt khi tìm đúng ít nhất năm chỗ phá chỉ mục và tái hiện được hiện tượng kế hoạch xấu theo tham số.

**Điều kiện đạt.** Tìm đúng ≥ 5/6 chỗ phá chỉ mục và sửa được, và tái hiện được hiện tượng kế hoạch xấu theo tham số với số đo chênh lệch.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Bọc hàm quanh cột lọc · ghép chuỗi giá trị vào câu lệnh · giả định kế hoạch luôn tối ưu cho mọi tham số · đổ lỗi cho engine khi kế hoạch đóng băng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/19-sargability-parameters-and-plan-stability.md`
- Nội dung học thuật: `note.md` cùng thư mục.
