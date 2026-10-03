# Phase 5: Modeling, Semantics and Analytical Product
# Module 12: Semantic Layer and Metrics Engineering
# Lesson 175: Defining Metrics and Reading the Generated SQL

## Thực hành

**Nhiệm vụ.** Khai báo bốn chỉ số theo bốn loại. Với mỗi cái, xuất SQL sinh ra và soi đủ bốn điểm, đối chiếu với hợp đồng. Giảng viên sửa một khai báo cho sai lệch hợp đồng; tìm ra nó chỉ bằng cách đọc SQL. Đọc kế hoạch thực thi của chỉ số tốn nhất.

Chỉ chạy join fixtures, MetricFlow validation/compile và execution plans trên dataset/môi trường thử nghiệm có version. Không chạy query tốn kém hoặc thay semantic configuration production. Redact credentials; lưu config/tool version, seed, commands, raw output và diff.

## Kiểm tra cuối bài

1. Phát biểu grains, identities và expected cardinalities.
2. Nêu phản ví dụ cho fanout, lost population hoặc ambiguous path.
3. Phân biệt parse, validate, compile và business reconciliation.
4. Đề xuất independent oracle cùng valid/invalid controls.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi kiểm chứng đầu ra của công cụ thay vì tin nó. Kiểm bằng bài đọc SQL có danh mục bốn điểm; đạt khi cả bốn chỉ số qua đủ bốn điểm soi và phát hiện được một khai báo sai cài sẵn.

**Điều kiện đạt.** Bốn chỉ số qua đủ bốn điểm soi, và khai báo sai cài sẵn được tìm ra chỉ bằng đọc SQL.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Tin SQL sinh ra là đúng vì công cụ nổi tiếng · chỉ kiểm bằng cách so con số · bỏ qua đường kết được chọn · không bao giờ đọc kế hoạch của SQL sinh ra.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/63-defining-metrics-reading-generated-sql.md`
- Nội dung học thuật: `note.md` cùng thư mục.
