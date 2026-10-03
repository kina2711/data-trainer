# Phase 2: Machine, Operating System and Network
# Module 6: Networking from Packet to API
# Lesson 87: Rate limiting and backpressure between services

## Thực hành

**Nhiệm vụ.** Dựng giới hạn tốc độ ở máy chủ và bộ ngắt mạch ở máy khách. Đẩy tải gấp năm lần công suất và đo tỉ lệ phục vụ của phần ưu tiên cao, có và không có giảm tải. Làm máy chủ hỏng hoàn toàn và chứng minh bộ ngắt mạch ngừng gọi thay vì tiếp tục thử.

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là hai cơ chế phòng vệ kiểm được bằng thí nghiệm quá tải. Kiểm bằng phép thử tải gấp năm lần công suất; đạt khi phần ưu tiên cao vẫn được phục vụ và không thành phần nào cạn tài nguyên.

**Điều kiện đạt.** Phần ưu tiên cao vẫn được phục vụ ở mức chấp nhận được khi quá tải, và bộ ngắt mạch ngừng gọi khi máy chủ hỏng hoàn toàn.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Không có giới hạn nên máy chủ sập · thử lại ngay khi bị từ chối · giảm tải ngẫu nhiên thay vì theo ưu tiên · bộ ngắt mạch không bao giờ đóng lại.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/087-rate-limiting-and-backpressure-between-services.md`
- Nội dung học thuật: `note.md` cùng thư mục.
