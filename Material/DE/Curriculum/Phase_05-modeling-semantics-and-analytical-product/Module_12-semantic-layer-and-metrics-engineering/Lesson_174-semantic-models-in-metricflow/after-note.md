# Phase 5: Modeling, Semantics and Analytical Product
# Module 12: Semantic Layer and Metrics Engineering
# Lesson 174: Semantic Models in MetricFlow

## Thực hành

**Nhiệm vụ.** Khai báo mô hình ngữ nghĩa cho ba bảng mart đã dựng ở M11. Với mỗi độ đo và chiều, ghi rõ nó đến từ phần nào của hợp đồng. Biên dịch và sửa tới sạch. Cố ý khai báo sai loại thực thể và ghi lại thông báo lỗi.

Chỉ chạy join fixtures, MetricFlow validation/compile và execution plans trên dataset/môi trường thử nghiệm có version. Không chạy query tốn kém hoặc thay semantic configuration production. Redact credentials; lưu config/tool version, seed, commands, raw output và diff.

## Kiểm tra cuối bài

1. Phát biểu grains, identities và expected cardinalities.
2. Nêu phản ví dụ cho fanout, lost population hoặc ambiguous path.
3. Phân biệt parse, validate, compile và business reconciliation.
4. Đề xuất independent oracle cùng valid/invalid controls.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là chuyển một thiết kế đã có sang khai báo công cụ, có tiêu chí truy ngược. Kiểm bằng rà soát truy ngược; đạt khi mọi độ đo và chiều dẫn được về một dòng trong hợp đồng và ba mô hình biên dịch sạch.

**Điều kiện đạt.** Ba mô hình biên dịch sạch, và mọi độ đo cùng chiều dẫn được về một dòng cụ thể trong hợp đồng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Khai báo theo cột có sẵn trong bảng · đặt mô hình ngữ nghĩa trên bảng thô · bỏ khai báo chiều thời gian chính · khai báo phép gộp mặc định là cộng cho mọi độ đo.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/62-semantic-models-in-metricflow.md`
- Nội dung học thuật: `note.md` cùng thư mục.
