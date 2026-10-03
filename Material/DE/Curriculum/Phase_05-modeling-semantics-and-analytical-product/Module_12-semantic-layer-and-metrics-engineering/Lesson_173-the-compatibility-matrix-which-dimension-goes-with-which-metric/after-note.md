# Phase 5: Modeling, Semantics and Analytical Product
# Module 12: Semantic Layer and Metrics Engineering
# Lesson 173: The Compatibility Matrix - Which Dimension Goes with Which Metric

## Thực hành

**Nhiệm vụ.** Dựng ma trận cho tám chỉ số nhân sáu chiều, mỗi ô ghi một trong ba trạng thái kèm lý do cho ô không hợp lệ. Cưỡng chế bằng công cụ. Chạy mười truy vấn gồm năm hợp lệ và năm không, kiểm phản ứng từng cái. Xuất ma trận thành tài liệu cho người dùng.

Chỉ chạy join fixtures, MetricFlow validation/compile và execution plans trên dataset/môi trường thử nghiệm có version. Không chạy query tốn kém hoặc thay semantic configuration production. Redact credentials; lưu config/tool version, seed, commands, raw output và diff.

## Kiểm tra cuối bài

1. Phát biểu grains, identities và expected cardinalities.
2. Nêu phản ví dụ cho fanout, lost population hoặc ambiguous path.
3. Phân biệt parse, validate, compile và business reconciliation.
4. Đề xuất independent oracle cùng valid/invalid controls.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu hai chiều: chặn đúng cái sai và không chặn nhầm cái đúng. Kiểm bằng mười truy vấn; đạt khi mọi ô không hợp lệ bị chặn có giải thích và không ô hợp lệ nào bị chặn nhầm.

**Điều kiện đạt.** Năm truy vấn không hợp lệ bị chặn kèm giải thích, năm truy vấn hợp lệ chạy được, và ma trận xuất ra dạng tài liệu đọc được.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Để người dùng tự phát hiện chiều không dùng được · chặn mà không giải thích lý do · đánh dấu hợp lệ cho mọi ô để tránh phiền · không xuất ma trận thành tài liệu.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/61-metric-dimension-compatibility-matrix.md`
- Nội dung học thuật: `note.md` cùng thư mục.
