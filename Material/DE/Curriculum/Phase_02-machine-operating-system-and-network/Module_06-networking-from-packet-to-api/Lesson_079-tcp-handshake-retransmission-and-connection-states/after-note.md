# Phase 2: Machine, Operating System and Network
# Module 6: Networking from Packet to API
# Lesson 79: TCP - handshake, retransmission and connection states

## Thực hành

**Nhiệm vụ.** Bắt gói cho ba tình huống: mạng mất gói mô phỏng, dịch vụ từ chối kết nối, và dịch vụ trả về lỗi ứng dụng. Với mỗi bản, chỉ ra gói nào là bằng chứng và phân loại. Đếm số socket ở trạng thái chờ đóng sau khi chạy 10.000 kết nối ngắn, rồi chạy lại với hồ kết nối và đếm lại.

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective là đọc bằng chứng thô, kỹ năng mà không đọc được thì mọi chẩn đoán mạng đều là phỏng đoán. Kiểm bằng ba bản bắt gói; đạt khi phân loại đúng ít nhất hai và chỉ ra được gói cụ thể làm bằng chứng.

**Điều kiện đạt.** Phân loại đúng ≥ 2/3 bản bắt gói kèm gói làm bằng chứng, và số socket chờ đóng giảm rõ rệt khi dùng hồ kết nối.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Nhầm đặt lại kết nối với hết giờ · mở kết nối mới cho mỗi yêu cầu · bỏ qua trạng thái chờ đóng tới khi cạn cổng · kết luận từ nhật ký ứng dụng mà không bắt gói.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/079-tcp-handshake-retransmission-and-connection-states.md`
- Nội dung học thuật: `note.md` cùng thư mục.
