# Phase 2: Machine, Operating System and Network
# Module 6: Networking from Packet to API
# Lesson 86: Diagnosing latency across the whole path

## Thực hành

**Nhiệm vụ.** Giảng viên tạo ba tình huống chậm ở ba chặng khác nhau. Với mỗi cái, đo tách theo chặng, báo phân vị 95, và chỉ ra chặng nút thắt. Đối chiếu số đo phía máy khách với nhật ký phía máy chủ qua mã theo dõi để tách phần mạng khỏi phần xử lý.

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective là phân rã một số đo tổng thành thành phần, kỹ năng dùng lại ở M26. Kiểm bằng ba tình huống chậm; đạt khi chỉ đúng chặng nút thắt ở ít nhất hai và dẫn được số đo của chặng đó.

**Điều kiện đạt.** Chỉ đúng chặng nút thắt ở ≥ 2/3 tình huống kèm số đo, và tách được phần mạng khỏi phần xử lý bằng đối chiếu hai phía.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Báo độ trễ trung bình · chỉ đo ở một phía · kết luận mạng chậm mà chưa bắt gói · bỏ qua chặng phân giải tên.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/086-diagnosing-latency-across-the-whole-path.md`
- Nội dung học thuật: `note.md` cùng thư mục.
