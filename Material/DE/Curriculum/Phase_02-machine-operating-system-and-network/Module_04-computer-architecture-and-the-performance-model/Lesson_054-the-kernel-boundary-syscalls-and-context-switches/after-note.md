# Phase 2: Machine, Operating System and Network
# Module 4: Computer Architecture and the Performance Model
# Lesson 54: The kernel boundary - syscalls and context switches

## Thực hành

**Nhiệm vụ.** Viết chương trình đọc tệp 500 MB theo từng byte, đếm số lời gọi hệ thống và đo thời gian. Viết lại theo khối 64 KB và đo lại cả hai. Chạy một tác vụ tính với số luồng bằng 1, bằng số lõi và gấp 8 lần số lõi; đo thông lượng và số lần chuyển ngữ cảnh.

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một tối ưu có cơ chế rõ và kết quả đo được hai chiều. Kiểm bằng cặp số đo lời gọi và thời gian; đạt khi số lời gọi giảm ít nhất một bậc và thời gian giảm tương ứng.

**Điều kiện đạt.** Số lời gọi hệ thống giảm ≥ 1 bậc sau khi gộp lô với thời gian giảm tương ứng, và bảng ba mức luồng cho thấy điểm quá tải.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Tối ưu thuật toán khi nút thắt là số lời gọi hệ thống · tăng số luồng cho tới khi máy chậm lại · đo thời gian mà không đếm lời gọi nên không biết nguyên nhân.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/054-the-kernel-boundary-syscalls-and-context-switches.md`
- Nội dung học thuật: `note.md` cùng thư mục.
