# Phase 8: Distributed Systems, Streaming and Compute
# Module 21: Kafka and Event Streaming
# Lesson 323: Broker internals - segment, index, page cache and retention

## Thực hành

**Nhiệm vụ.** Gửi một lô bản ghi và truy đường đi qua từng chặng: tìm tệp đoạn trên đĩa, xem chỉ mục, quan sát bộ đệm trang, và xác nhận nút theo sau đã kéo về. Tính thời hạn đọc lại từ tốc độ ghi, cấu hình giữ và dung lượng đĩa; đối chiếu với quan sát. Làm đầy đĩa có kiểm soát và ghi lại hành vi của máy chủ.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi đọc trạng thái thật thay vì mô tả kiến trúc. Kiểm bằng bài truy vết cộng bài tính; đạt khi truy đủ các chặng trên hệ thật và thời hạn đọc lại tính được khớp quan sát trong sai số thoả thuận.

**Điều kiện đạt.** Đường đi của bản ghi được truy đủ chặng trên hệ thật, và thời hạn đọc lại tính từ cấu hình khớp quan sát.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Bỏ qua bộ đệm trang khi tính bộ nhớ cần · đặt thời hạn giữ mà không tính dung lượng · không theo dõi dung lượng đĩa · nghĩ thông lượng cao đến từ phần cứng chứ từ cách ghi nối.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/211-broker-internals-segment-index-page-cache-and-retention.md`
- Nội dung học thuật: `note.md` cùng thư mục.
