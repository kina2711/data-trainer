# Phase 5: Modeling, Semantics and Analytical Product
# Module 12: Semantic Layer and Metrics Engineering
# Lesson 177: Testing a Semantic Layer - Definition and Static Tests

## Thực hành

**Nhiệm vụ.** Viết bộ kiểm tra cho năm quy tắc định nghĩa và ba quy tắc cấu trúc đồ thị. Đưa vào quy trình tích hợp liên tục có cửa chặn hợp nhất. Nộp năm yêu cầu hợp nhất vi phạm năm quy tắc khác nhau và xác nhận cả năm bị chặn ở đúng quy tắc.

Chỉ chạy join fixtures, MetricFlow validation/compile và execution plans trên dataset/môi trường thử nghiệm có version. Không chạy query tốn kém hoặc thay semantic configuration production. Redact credentials; lưu config/tool version, seed, commands, raw output và diff.

## Kiểm tra cuối bài

1. Phát biểu grains, identities và expected cardinalities.
2. Nêu phản ví dụ cho fanout, lost population hoặc ambiguous path.
3. Phân biệt parse, validate, compile và business reconciliation.
4. Đề xuất independent oracle cùng valid/invalid controls.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một cửa chặn tự động có tiêu chí nghiệm thu bằng phép thử tiêm. Kiểm bằng năm vi phạm tiêm; đạt khi cả năm bị chặn và không khai báo hợp lệ nào bị chặn nhầm.

**Điều kiện đạt.** Năm vi phạm đều bị chặn ở đúng quy tắc, và không khai báo hợp lệ nào bị chặn nhầm.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chỉ kiểm bằng cách chạy truy vấn · không chặn hợp nhất nên kiểm tra chỉ để tham khảo · viết kiểm tra cần dữ liệu nên chạy chậm và bị tắt · bỏ quy tắc bắt buộc có chủ sở hữu.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/65-semantic-layer-definition-static-tests.md`
- Nội dung học thuật: `note.md` cùng thư mục.
