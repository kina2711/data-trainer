# Phase 2: Machine, Operating System and Network
# Module 5: Operating Systems, Concurrency and Linux
# Lesson 69: Services with systemd and the journal

## Thực hành

**Nhiệm vụ.** Đóng gói tiến trình xử lý ở lesson 67 thành một dịch vụ. Giết nó và xác nhận tự khởi động lại. Làm nó chết ngay khi khởi động và xác nhận giới hạn số lần chặn được vòng lặp. Đọc nhật ký theo dịch vụ và lọc theo mã theo dõi. Đưa một bí mật vào đúng cách và kiểm tài khoản thường không đọc được.

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một cấu hình vận hành kiểm được bằng thí nghiệm giết tiến trình. Kiểm bằng ba phép thử; đạt khi dịch vụ tự khởi động lại, vòng lặp khởi động bị chặn, và nhật ký truy được theo mã theo dõi.

**Điều kiện đạt.** Dịch vụ tự khởi động lại sau khi bị giết, vòng lặp khởi động bị chặn theo giới hạn, và nhật ký lọc được theo mã theo dõi.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đặt chính sách luôn khởi động lại mà không giới hạn số lần · chạy dịch vụ bằng quyền quản trị · ghi nhật ký vào tệp riêng thay vì luồng chuẩn · đặt bí mật thẳng trong tệp định nghĩa dịch vụ.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/069-services-with-systemd-and-the-journal.md`
- Nội dung học thuật: `note.md` cùng thư mục.
