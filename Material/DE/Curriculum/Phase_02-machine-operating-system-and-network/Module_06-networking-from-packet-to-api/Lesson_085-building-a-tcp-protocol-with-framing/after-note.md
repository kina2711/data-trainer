# Phase 2: Machine, Operating System and Network
# Module 6: Networking from Packet to API
# Lesson 85: Building a TCP protocol with framing

## Thực hành

**Nhiệm vụ.** Viết máy chủ lặp lại có đóng khung theo độ dài. Cố ý cài bản đọc thiếu và tái hiện dữ liệu hỏng khi tải cao. Sửa. Tiêm ba tình huống: ngắt giữa chừng, gửi rất chậm, và thông điệp vượt giới hạn. Chứng minh máy chủ xử lý đúng cả ba mà không treo và không cạn bộ nhớ.

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một cài đặt có ba ca biên kiểm được. Kiểm bằng ba phép thử hỏng; đạt khi cả ba được xử lý đúng và tái hiện được lỗi đọc thiếu ở bản chưa sửa.

**Điều kiện đạt.** Ba tình huống hỏng đều được xử lý đúng, và tái hiện được dữ liệu hỏng ở bản đọc thiếu.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Giả định một lần đọc trả về đúng một thông điệp · không giới hạn kích thước thông điệp · treo vô hạn với máy khách gửi chậm · không đóng khung mà dựa vào kích thước gói.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/085-building-a-tcp-protocol-with-framing.md`
- Nội dung học thuật: `note.md` cùng thư mục.
