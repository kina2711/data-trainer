# Phase 2: Machine, Operating System and Network
# Module 5: Operating Systems, Concurrency and Linux
# Lesson 66: Readiness against completion - partial I/O, cancellation and io_uring awareness

## Thực hành

**Nhiệm vụ.** Viết bên gửi và bên nhận trao đổi thông điệp lớn hơn bộ đệm ổ cắm. Chạy 10.000 lượt dưới tải và đếm số thông điệp bị cắt hoặc ghép sai khi chưa xử lý đọc thiếu, rồi sửa bằng cách đóng khung và lặp tới đủ. Huỷ một thao tác giữa chừng sau khi đã ghi một phần và mô tả trạng thái bên kia nhìn thấy. Viết một đoạn nêu điều kiện mà giao diện theo hàng đợi đáng cân nhắc.

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có một ca hỏng đặc trưng chỉ lộ ra dưới tải. Kiểm bằng phép thử thông điệp lớn; đạt khi không thông điệp nào bị cắt hay ghép sai qua 10.000 lượt và ca huỷ giữa chừng được mô tả đúng hậu quả.

**Điều kiện đạt.** Không thông điệp nào bị cắt hay ghép sai qua 10.000 lượt, và hậu quả của huỷ giữa chừng được mô tả đúng ở phía bên kia.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Giả định một lần gọi đọc trả về trọn thông điệp · không đóng khung thông điệp · tin rằng huỷ bỏ hoàn tác được tác dụng phụ đã gửi đi · chọn giao diện mới vì nghe hiện đại.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/066-readiness-against-completion-partial-i-o-cancellation-and-io-uring-awareness.md`
- Nội dung học thuật: `note.md` cùng thư mục.
