# Phase 2: Machine, Operating System and Network
# Module 6: Networking from Packet to API
# Lesson 80: TLS - certificates, verification and the handshake cost

## Thực hành

**Nhiệm vụ.** Dựng ba tình huống lỗi chứng chỉ. Với mỗi cái, dùng công cụ dòng lệnh xem chuỗi chứng chỉ và xác định nguyên nhân. Với trường hợp thiếu chứng chỉ trung gian, chứng minh trình duyệt gọi được còn thư viện thì lỗi. Đo chi phí bắt tay bằng cách so thời gian yêu cầu đầu với yêu cầu sau trên cùng kết nối.

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective là phân biệt ba lỗi có cùng thông báo mơ hồ. Kiểm bằng ba tình huống; đạt khi phân loại đúng cả ba và giải thích đúng trường hợp thiếu chứng chỉ trung gian.

**Điều kiện đạt.** Phân loại đúng cả ba lỗi chứng chỉ, giải thích đúng trường hợp thiếu chứng chỉ trung gian, và có số đo chi phí bắt tay.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Tắt xác minh chứng chỉ để hết lỗi · kết luận từ thông báo lỗi của thư viện mà không xem chuỗi chứng chỉ · quên chứng chỉ trung gian · đo chi phí bắt tay trên kết nối đã mở sẵn.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/080-tls-certificates-verification-and-the-handshake-cost.md`
- Nội dung học thuật: `note.md` cùng thư mục.
