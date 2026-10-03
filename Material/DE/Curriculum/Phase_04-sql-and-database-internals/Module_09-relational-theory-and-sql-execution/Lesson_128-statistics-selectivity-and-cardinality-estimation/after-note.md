# Phase 4: SQL and Database Internals
# Module 9: Relational Theory and SQL Execution
# Lesson 128: Statistics, selectivity and cardinality estimation

## Thực hành

**Nhiệm vụ.** Tạo ba tình huống: thống kê cũ sau khi nạp lớn, dữ liệu lệch nặng, và hai cột tương quan. Với mỗi cái, chạy kế hoạch có phân tích và so số dòng ước lượng với thực tế. Chữa bằng cách phù hợp và đo lại tỉ lệ sai. Ghi bảng trước sau.

Lưu SQL, seed/workload, dự đoán trước khi chạy, plan dạng máy đọc được, output thô, đối soát và thông số môi trường. Chỉ chạy DDL/spill/load test trong môi trường cô lập với lock/statement timeout; ảnh chụp không thay artifact tái chạy.

## Kiểm tra cuối bài

1. MCV và histogram giữ thông tin gì?
2. Giả định độc lập hỏng khi nào?
3. Extended statistics có ba loại nào?
4. Error factor được đo ra sao?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective là chẩn đoán nguyên nhân gốc của phần lớn truy vấn chậm. Kiểm bằng ba tình huống ước lượng sai; đạt khi phát hiện cả ba và chữa được ít nhất hai với tỉ lệ sai giảm rõ rệt.

**Điều kiện đạt.** Phát hiện đúng cả ba tình huống, và tỉ lệ sai ước lượng giảm rõ rệt ở ≥ 2/3 sau khi chữa.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Thêm chỉ mục để chữa ước lượng sai · không cập nhật thống kê sau khi nạp lớn · bỏ qua giả định độc lập · so thời gian mà không so số dòng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/16-statistics-selectivity-and-cardinality-estimation.md`
- Nội dung học thuật: `note.md` cùng thư mục.
