# Phase 5: Modeling, Semantics and Analytical Product
# Module 13: Analytical Data Product and Self-service
# Lesson 187: Requirements Traceability

## Thực hành

**Nhiệm vụ.** Dựng ma trận truy ngược năm mắt cho sản phẩm đang làm, lưu trong kho mã. Trả lời ba câu hỏi: nguồn này đổi thì quyết định nào ảnh hưởng, quyết định này phụ thuộc những bảng nào, và bảng nào không phục vụ quyết định nào. Đề xuất bỏ những bảng ở câu cuối.

Chỉ dùng fixture, contexts và principals thử nghiệm có phiên bản. Không đổi metric production, xóa version cũ, chạy query tốn kém hoặc dùng dữ liệu nhạy cảm. Lưu input, version, artifact hashes, raw results, approvals mô phỏng và limitations.

## Kiểm tra cuối bài

1. Nêu decision hoặc invariant trung tâm.
2. Đưa một phản ví dụ làm lựa chọn hiện tại sai.
3. Phân biệt evidence độc lập với implementation output.
4. Nêu owner, gate và artifact cần để hoàn thành.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu bằng việc trả lời câu hỏi hai chiều. Kiểm bằng ba câu hỏi truy ngược; đạt khi trả lời đúng cả ba chỉ bằng ma trận và tìm được ít nhất một bảng không phục vụ quyết định nào.

**Điều kiện đạt.** Trả lời đúng cả ba câu hỏi chỉ bằng ma trận, và tìm được ít nhất một bảng không phục vụ quyết định nào.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Lưu ma trận truy ngược trong tài liệu rời nên nó lạc hậu ngay · chỉ truy được một chiều · nhầm lineage kỹ thuật với truy ngược tới quyết định · bỏ mắt câu hỏi nên nhảy thẳng từ quyết định sang chỉ số.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/75-requirements-traceability.md`
- Nội dung học thuật: `note.md` cùng thư mục.
