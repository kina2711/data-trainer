# Phase 5: Modeling, Semantics and Analytical Product
# Module 12: Semantic Layer and Metrics Engineering
# Lesson 172: Fanout - Proving a Metric Is Not Double Counted

## Thực hành

**Nhiệm vụ.** Nhận ba chỉ số đã khai báo sẵn, trong đó một cái đếm trùng. Chạy đủ bốn bước cho từng cái. Với chỉ số có vấn đề, định lượng mức thổi phồng và sửa. Nộp bảng đối soát ba mức gộp cho cả ba.

Chỉ chạy join fixtures, MetricFlow validation/compile và execution plans trên dataset/môi trường thử nghiệm có version. Không chạy query tốn kém hoặc thay semantic configuration production. Redact credentials; lưu config/tool version, seed, commands, raw output và diff.

## Kiểm tra cuối bài

1. Phát biểu grains, identities và expected cardinalities.
2. Nêu phản ví dụ cho fanout, lost population hoặc ambiguous path.
3. Phân biệt parse, validate, compile và business reconciliation.
4. Đề xuất independent oracle cùng valid/invalid controls.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một quy trình kiểm chứng bắt buộc có kết quả nhị phân. Kiểm bằng ba chỉ số trong đó ít nhất một đang đếm trùng; đạt khi phát hiện đúng và hai chỉ số còn lại được chứng minh sạch ở cả ba mức gộp.

**Điều kiện đạt.** Phát hiện đúng chỉ số đếm trùng và định lượng mức thổi phồng, và hai chỉ số còn lại khớp truy vấn viết tay ở cả ba mức gộp.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chỉ đối soát ở mức chi tiết nhất · tin công cụ đã xử lý nhân dòng · bỏ bước đếm dòng trước và sau kết · đối soát với chính truy vấn do công cụ sinh ra thay vì truy vấn viết tay.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/60-fanout-proof-metric-not-double-counted.md`
- Nội dung học thuật: `note.md` cùng thư mục.
