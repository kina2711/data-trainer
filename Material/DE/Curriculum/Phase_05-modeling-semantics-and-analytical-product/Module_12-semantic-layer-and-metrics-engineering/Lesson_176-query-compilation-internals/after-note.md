# Phase 5: Modeling, Semantics and Analytical Product
# Module 12: Semantic Layer and Metrics Engineering
# Lesson 176: Query Compilation Internals

## Thực hành

**Nhiệm vụ.** Giảng viên đưa ba tình huống: một kết quả lạ do đường kết, một do phép gộp, và một truy vấn chậm. Với mỗi cái, truy các bước biên dịch để tìm bước gây ra. Với truy vấn chậm, dựng bảng tổng hợp tính sẵn hoặc chỉnh khai báo, đo thời gian trước sau.

Chỉ chạy join fixtures, MetricFlow validation/compile và execution plans trên dataset/môi trường thử nghiệm có version. Không chạy query tốn kém hoặc thay semantic configuration production. Redact credentials; lưu config/tool version, seed, commands, raw output và diff.

## Kiểm tra cuối bài

1. Phát biểu grains, identities và expected cardinalities.
2. Nêu phản ví dụ cho fanout, lost population hoặc ambiguous path.
3. Phân biệt parse, validate, compile và business reconciliation.
4. Đề xuất independent oracle cùng valid/invalid controls.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective là chẩn đoán xuyên tầng từ câu hỏi tới SQL. Kiểm bằng ba tình huống; đạt khi truy đúng bước gây ra ở ít nhất hai và cải thiện được truy vấn chậm có số đo.

**Điều kiện đạt.** Truy đúng bước gây ra ở ≥ 2/3 tình huống, và truy vấn chậm cải thiện có số đo mà kết quả không đổi.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đổ lỗi cho công cụ khi nguyên nhân là khai báo · sửa bằng cách viết SQL tay ngoài tầng ngữ nghĩa · dựng bảng tổng hợp cho chỉ số không cộng được · không đo trước sau.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/64-query-compilation-internals.md`
- Nội dung học thuật: `note.md` cùng thư mục.
