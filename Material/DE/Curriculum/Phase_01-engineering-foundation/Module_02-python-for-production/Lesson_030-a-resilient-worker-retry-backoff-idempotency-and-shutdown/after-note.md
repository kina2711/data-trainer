# Phase 1: Engineering Foundation
# Module 2: Python for Production
# Lesson 30: A resilient worker - retry, backoff, idempotency and shutdown

## Thực hành

**Nhiệm vụ.** Viết tiến trình xử lý đọc từ hàng đợi có giới hạn và ghi vào tệp kết quả có khoá bất biến. Tiêm lỗi tạm thời và lỗi dữ liệu, chứng minh chỉ loại đầu được thử lại. Giết tiến trình 20 lần ở các thời điểm ngẫu nhiên, khởi động lại, và đối soát kết quả với đầu vào. Gửi tín hiệu dừng và đo thời gian tắt.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *sáng tạo*. Objective đòi ghép bốn cơ chế rời thành một mẫu chạy được dưới sự cố. Kiểm bằng thí nghiệm giết tiến trình 20 lần; đạt khi đối soát khớp tuyệt đối và tắt có kiểm soát hoàn tất trong hạn.

**Điều kiện đạt.** Sau 20 lần giết và khởi động lại, đối soát khớp tuyệt đối; lỗi dữ liệu không bị thử lại; và tắt có kiểm soát xong trong hạn.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Thử lại mọi loại lỗi · thử lại ngay không lùi và không nhiễu · ghi không bất biến rồi sinh trùng khi thử lại · bỏ qua tín hiệu dừng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/030-resilient-worker-retry-backoff-idempotency-shutdown.md`
- Nội dung học thuật: `note.md` cùng thư mục.
