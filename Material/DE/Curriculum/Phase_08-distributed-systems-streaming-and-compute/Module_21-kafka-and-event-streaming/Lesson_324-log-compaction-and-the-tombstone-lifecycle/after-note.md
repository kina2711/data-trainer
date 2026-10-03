# Phase 8: Distributed Systems, Streaming and Compute
# Module 21: Kafka and Event Streaming
# Lesson 324: Log compaction and the tombstone lifecycle

## Thực hành

**Nhiệm vụ.** Dựng một chủ đề chế độ nén biểu diễn trạng thái khách hàng. Ghi chuỗi tạo, cập nhật và xoá. Chạy nén rồi đọc lại từ đầu và đối soát trạng thái dựng lại với nguồn. Đặt thời hạn giữ bia mộ ngắn, dừng một bên tiêu thụ đủ lâu rồi cho chạy lại; đếm số khoá đã xoá mà nó vẫn giữ.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có một ca hỏng cụ thể cần tái hiện. Kiểm bằng đối soát trạng thái dựng lại; đạt khi trạng thái dựng lại khớp nguồn tuyệt đối, và ca bia mộ hết hạn được tái hiện kèm số khoá thừa.

**Điều kiện đạt.** Trạng thái dựng lại khớp nguồn tuyệt đối, và ca bia mộ hết hạn được tái hiện kèm số khoá thừa đếm được.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dùng chế độ nén cho chủ đề chuỗi sự kiện · đặt thời hạn giữ bia mộ ngắn hơn thời gian dừng tối đa của bên tiêu thụ · gửi bản ghi không khoá vào chủ đề nén · không đối soát trạng thái dựng lại.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/212-log-compaction-and-the-tombstone-lifecycle.md`
- Nội dung học thuật: `note.md` cùng thư mục.
