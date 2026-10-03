# Phase 5: Modeling, Semantics and Analytical Product
# Module 12: Semantic Layer and Metrics Engineering
# Lesson 180: Access Control at the Semantic Layer

## Thực hành

**Nhiệm vụ.** Cài kiểm soát theo chỉ số, theo dòng và theo cột. Viết sáu phép thử phủ định gồm một phép thử suy ra dòng chi tiết từ nhóm một phần tử. Đặt ngưỡng số phần tử tối thiểu và chứng minh đường rò bị chặn. Kiểm rằng cùng chính sách có hiệu lực ở cả ba đường phục vụ.

Chỉ chạy join fixtures, MetricFlow validation/compile và execution plans trên dataset/môi trường thử nghiệm có version. Không chạy query tốn kém hoặc thay semantic configuration production. Redact credentials; lưu config/tool version, seed, commands, raw output và diff.

## Kiểm tra cuối bài

1. Phát biểu grains, identities và expected cardinalities.
2. Nêu phản ví dụ cho fanout, lost population hoặc ambiguous path.
3. Phân biệt parse, validate, compile và business reconciliation.
4. Đề xuất independent oracle cùng valid/invalid controls.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một cơ chế bảo mật kiểm được bằng phép thử phủ định gồm cả đường rò gián tiếp. Kiểm bằng sáu phép thử; đạt khi cả sáu bị chặn đúng và đường rò qua phép gộp được chặn bằng ngưỡng nhóm.

**Điều kiện đạt.** Sáu phép thử phủ định đều bị chặn đúng, đường rò qua nhóm một phần tử bị chặn, và chính sách có hiệu lực ở cả ba đường phục vụ.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Cấu hình quyền ở từng công cụ BI thay vì ở tầng ngữ nghĩa · bỏ qua đường rò qua phép gộp · trả về số đã lọc âm thầm thay vì từ chối · không kiểm chính sách ở mọi đường phục vụ.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/68-access-control-semantic-layer.md`
- Nội dung học thuật: `note.md` cùng thư mục.
