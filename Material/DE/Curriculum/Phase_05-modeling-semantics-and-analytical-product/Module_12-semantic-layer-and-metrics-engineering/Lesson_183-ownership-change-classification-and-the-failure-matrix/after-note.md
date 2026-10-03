# Phase 5: Modeling, Semantics and Analytical Product
# Module 12: Semantic Layer and Metrics Engineering
# Lesson 183: Ownership, Change Classification and the Failure Matrix

## Thực hành

**Nhiệm vụ.** Lập ma trận bảy chế độ hỏng với đủ bốn cột. Với mỗi dòng, viết một phép kiểm tự động. Giảng viên tiêm bảy lỗi tương ứng, trong đó có một mục đệm dùng lại xuyên người dùng và một công thức bị sửa đè, rồi đếm bao nhiêu cái bị phát hiện. Gán ba vai cho bộ chỉ số đã dựng. Viết phân tích sau sự cố cho một lần số sai công bố ra ngoài.

Chỉ dùng fixture, contexts và principals thử nghiệm có phiên bản. Không đổi metric production, xóa version cũ, chạy query tốn kém hoặc dùng dữ liệu nhạy cảm. Lưu input, version, artifact hashes, raw results, approvals mô phỏng và limitations.

## Kiểm tra cuối bài

1. Nêu decision hoặc invariant trung tâm.
2. Đưa một phản ví dụ làm lựa chọn hiện tại sai.
3. Phân biệt evidence độc lập với implementation output.
4. Nêu owner, gate và artifact cần để hoàn thành.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi tổng hợp các lỗi đã gặp thành một hệ phòng vệ. Kiểm bằng phép thử tiêm bảy lỗi; đạt khi ít nhất sáu bị phép kiểm tự động phát hiện và ba vai được gán rõ.

**Điều kiện đạt.** ≥ 6/7 lỗi tiêm bị phép kiểm tự động phát hiện, ba vai được gán rõ, và phân tích sau sự cố không đổ lỗi cá nhân.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Gán chủ sở hữu nghiệp vụ cho một nhóm thay vì một người · viết cách chặn mà không có phép kiểm tự động · bỏ chế độ hỏng rò rỉ qua phép gộp · bỏ hai chế độ hỏng về đệm và về sửa đè công thức vì chúng không sinh số lạ · phân tích sau sự cố quy về lỗi cá nhân.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/71-ownership-change-classification-failure-matrix.md`
- Nội dung học thuật: `note.md` cùng thư mục.
