# Phase 5: Modeling, Semantics and Analytical Product
# Module 13: Analytical Data Product and Self-service
# Lesson 186: Question Decomposition and the Metric Tree

## Thực hành

**Nhiệm vụ.** Từ một quyết định đã chốt ở lesson 185, dựng cây chỉ số ba tầng. Với mỗi lá, ghi đội sở hữu và đòn bẩy cụ thể họ tác động được. Với mỗi nút, trỏ tới hợp đồng tương ứng. Đánh dấu chỉ số nào là dẫn dắt và chỉ số nào là kết quả.

Chỉ dùng fixture, contexts và principals thử nghiệm có phiên bản. Không đổi metric production, xóa version cũ, chạy query tốn kém hoặc dùng dữ liệu nhạy cảm. Lưu input, version, artifact hashes, raw results, approvals mô phỏng và limitations.

## Kiểm tra cuối bài

1. Nêu decision hoặc invariant trung tâm.
2. Đưa một phản ví dụ làm lựa chọn hiện tại sai.
3. Phân biệt evidence độc lập với implementation output.
4. Nêu owner, gate và artifact cần để hoàn thành.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có phép thử khách quan ở mọi lá. Kiểm bằng rà soát cây; đạt khi mọi lá có chủ và đòn bẩy, và mọi nút dẫn được tới một hợp đồng chỉ số.

**Điều kiện đạt.** Mọi lá có chủ và đòn bẩy cụ thể, mọi nút dẫn tới một hợp đồng, và chỉ số dẫn dắt được đánh dấu tách khỏi chỉ số kết quả.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Phân rã tới mức không ai tác động được · để lá không có chủ · dựng cây chỉ toàn chỉ số kết quả · đặt tên chỉ số mà không có hợp đồng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/74-question-decomposition-metric-tree.md`
- Nội dung học thuật: `note.md` cùng thư mục.
