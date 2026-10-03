# Phase 2: Machine, Operating System and Network
# Module 6: Networking from Packet to API
# Lesson 84: Designing an API client for data ingestion

## Thực hành

**Nhiệm vụ.** Dựng một máy chủ giả có phân trang, giới hạn tốc độ, lỗi ngẫu nhiên 10%, và chèn thêm bản ghi giữa lúc đang phân trang. Viết trình gọi đạt sáu yêu cầu. Nạp toàn bộ và đối soát số bản ghi với nguồn. Giết tiến trình giữa chừng và chứng minh lần chạy sau tiếp tục đúng chỗ.

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *sáng tạo*. Objective đòi ghép sáu cơ chế thành một thành phần chịu lỗi. Kiểm bằng thí nghiệm nguồn xấu; đạt khi đối soát khớp tuyệt đối dưới cả ba điều kiện lỗi.

**Điều kiện đạt.** Đối soát khớp tuyệt đối dưới cả ba điều kiện lỗi, và sau khi giết tiến trình thì lần chạy sau tiếp tục đúng chỗ.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Phân trang theo số trang trên dữ liệu đang đổi · thử lại mà không có khoá bất biến · đoán thời gian chờ thay vì đọc tiêu đề · không lưu trạng thái nên chạy lại từ đầu.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/084-designing-an-api-client-for-data-ingestion.md`
- Nội dung học thuật: `note.md` cùng thư mục.
