# Phase 2: Machine, Operating System and Network
# Module 6: Networking from Packet to API
# Lesson 82: Proxies, load balancers and what they hide

## Thực hành

**Nhiệm vụ.** Dựng một proxy đảo đứng trước hai bản sao dịch vụ. Đặt hạn chờ của proxy ngắn hơn thời gian xử lý của dịch vụ và quan sát máy khách nhận lỗi gì. Tắt một bản sao và quan sát kiểm tra sức khoẻ loại nó ra. Thử kiểm tra sức khoẻ chỉ kiểm tiến trình còn sống trong khi dịch vụ đã mất kết nối cơ sở dữ liệu.

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Objective là nhận ra nguồn gây nhầm lẫn khi chẩn đoán qua nhiều chặng. Kiểm bằng ba kiến trúc; đạt khi chỉ đúng ít nhất hai chặng có hạn chờ riêng và nêu đúng cách xác minh.

**Điều kiện đạt.** Chỉ đúng ≥ 2/3 chặng có hạn chờ riêng, và chứng minh được kiểm tra sức khoẻ sai loại không phát hiện dịch vụ đã hỏng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Nghĩ lỗi đến từ ứng dụng trong khi proxy cắt trước · dùng kiểm tra sức khoẻ chỉ kiểm tiến trình · bật phiên dính mà không cần · quên rằng lớp trung gian che địa chỉ máy khách thật.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/082-proxies-load-balancers-and-what-they-hide.md`
- Nội dung học thuật: `note.md` cùng thư mục.
