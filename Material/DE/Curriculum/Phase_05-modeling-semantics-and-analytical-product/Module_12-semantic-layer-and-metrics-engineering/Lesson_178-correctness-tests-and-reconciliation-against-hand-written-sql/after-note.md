# Phase 5: Modeling, Semantics and Analytical Product
# Module 12: Semantic Layer and Metrics Engineering
# Lesson 178: Correctness Tests and Reconciliation Against Hand-Written SQL

## Thực hành

**Nhiệm vụ.** Với năm chỉ số đã chứng nhận, nhờ một học viên khác viết truy vấn đối soát chỉ từ hợp đồng. Dựng bộ đối chứng cố định phủ đủ sáu ca: giá trị rỗng, trùng, hoàn tiền, tới muộn, chiều biến đổi chậm, và ranh giới kỳ tài chính. So kết quả ở ba mức gộp nhân sáu ca. Đưa bộ đối soát vào quy trình chạy hằng ngày. Đổi một định nghĩa và chạy kiểm hồi quy để liệt kê chính xác cái gì đổi.

Chỉ chạy join fixtures, MetricFlow validation/compile và execution plans trên dataset/môi trường thử nghiệm có version. Không chạy query tốn kém hoặc thay semantic configuration production. Redact credentials; lưu config/tool version, seed, commands, raw output và diff.

## Kiểm tra cuối bài

1. Phát biểu grains, identities và expected cardinalities.
2. Nêu phản ví dụ cho fanout, lost population hoặc ambiguous path.
3. Phân biệt parse, validate, compile và business reconciliation.
4. Đề xuất independent oracle cùng valid/invalid controls.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu khắt khe là khớp tuyệt đối với nguồn độc lập. Kiểm bằng đối soát ba mức nhân sáu ca đối chứng; đạt khi năm chỉ số khớp ở mọi ô trong 18 ô và bộ kiểm chạy tự động.

**Điều kiện đạt.** Năm chỉ số khớp ở cả 18 ô ba mức nhân sáu ca đối chứng, và kiểm hồi quy liệt kê đúng phần thay đổi khi đổi định nghĩa.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Viết truy vấn đối soát bằng cách chép SQL sinh ra · chỉ đối soát ở một mức gộp · bộ đối chứng thiếu ca hoàn tiền hoặc ca chiều biến đổi chậm · đổi bộ đối chứng giữa hai lần chạy nên không quy được hồi quy · không có kiểm hồi quy nên đổi định nghĩa mà không biết ảnh hưởng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/66-correctness-reconciliation-hand-written-sql.md`
- Nội dung học thuật: `note.md` cùng thư mục.
