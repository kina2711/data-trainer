# Phase 8: Distributed Systems, Streaming and Compute
# Module 22: Change Data Capture Internals
# Lesson 343: Slot retention, lag and the source disk risk

## Thực hành

**Nhiệm vụ.** Dựng ba chỉ số và đặt cảnh báo theo thời gian còn lại. Dừng bên tiêu thụ và để khe phình; xác nhận cảnh báo nổ đúng lúc. Chạy quy trình phục hồi theo thứ tự và đo thời gian tới khi nhật ký được giải phóng. Ở môi trường cách ly, thực hiện một lần bỏ khe rồi chụp lại vào không gian riêng, đối soát trước khi hoán đổi.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đo năng lực vận hành dưới một rủi ro có thể làm sập hệ chính. Kiểm bằng tình huống tái hiện; đạt khi cảnh báo nổ trước ngưỡng thời gian thoả thuận và quy trình phục hồi không cần bỏ khe.

**Điều kiện đạt.** Cảnh báo nổ trước ngưỡng thời gian thoả thuận, phục hồi hoàn tất không cần bỏ khe, và lần chụp lại ở môi trường cách ly có đối soát trước khi hoán đổi.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đặt cảnh báo theo phần trăm đĩa · bỏ khe để tắt cảnh báo · chụp lại đè lên trạng thái đang phục vụ · không đo thời gian còn lại nên không biết còn bao lâu để xử lý.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/231-slot-retention-lag-and-the-source-disk-risk.md`
- Nội dung học thuật: `note.md` cùng thư mục.
