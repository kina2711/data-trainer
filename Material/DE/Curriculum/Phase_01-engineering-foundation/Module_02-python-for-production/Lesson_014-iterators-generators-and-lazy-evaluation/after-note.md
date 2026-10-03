# Phase 1: Engineering Foundation
# Module 2: Python for Production
# Lesson 14: Iterators, generators and lazy evaluation

## Thực hành

**Nhiệm vụ.** Viết bản nạp toàn bộ xử lý một tệp CSV và đo bộ nhớ đỉnh trên tệp 10 MB, 200 MB và 2 GB. Viết lại bằng hàm sinh và đo lại. Vẽ hai đường. Nối ba hàm sinh thành một chuỗi và chứng minh bộ nhớ vẫn không đổi.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một phép biến đổi mã có kết quả đo được bằng bộ nhớ. Kiểm bằng cặp số đo trên ba kích thước đầu vào; đạt khi bản dòng chảy giữ bộ nhớ gần như không đổi.

**Điều kiện đạt.** Bản dòng chảy giữ bộ nhớ đỉnh gần như không đổi qua cả ba kích thước, trong khi bản nạp toàn bộ tăng tuyến tính.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Gọi hàm chuyển thành danh sách ngay trong chuỗi nên mất tính lười · duyệt bộ lặp hai lần · đo bộ nhớ trung bình thay vì đỉnh · kết luận từ tệp mẫu quá nhỏ.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/014-iterators-generators-lazy-evaluation.md`
- Nội dung học thuật: `note.md` cùng thư mục.
