# Phase 8: Distributed Systems, Streaming and Compute
# Module 22: Change Data Capture Internals
# Lesson 336: Inside the transaction log - WAL, logical decoding and the replication slot

## Thực hành

**Nhiệm vụ.** Bật giải mã logic trên một cơ sở dữ liệu lab và tạo một khe. Đọc vị trí khởi động lại và vị trí đã xác nhận, giải thích khác biệt. Chạy tải ghi, dừng bên đọc, và đo tốc độ tích luỹ nhật ký. Tính thời gian còn lại tới khi đầy đĩa. Cho bên đọc chạy lại và xác nhận nhật ký được giải phóng.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi quan sát trạng thái thật của nguồn. Kiểm bằng thí nghiệm dừng bên đọc; đạt khi tốc độ tích luỹ được đo theo đơn vị dung lượng trên giờ và thời gian tới khi đầy đĩa tính được.

**Điều kiện đạt.** Tốc độ tích luỹ được đo theo dung lượng trên giờ, thời gian tới khi đầy đĩa tính được, và nhật ký được giải phóng sau khi bên đọc chạy lại.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Tạo khe rồi quên bên đọc · nhầm vị trí khởi động lại với vị trí đã xác nhận · không đo tốc độ tích luỹ nên không đặt được cảnh báo · giả định nguồn tự dọn nhật ký.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/224-inside-the-transaction-log-wal-logical-decoding-and-the-replication-slot.md`
- Nội dung học thuật: `note.md` cùng thư mục.
