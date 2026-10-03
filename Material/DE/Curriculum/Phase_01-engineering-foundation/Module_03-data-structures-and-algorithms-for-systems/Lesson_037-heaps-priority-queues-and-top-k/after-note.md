# Phase 1: Engineering Foundation
# Module 3: Data Structures and Algorithms for Systems
# Lesson 37: Heaps, priority queues and top-k

## Thực hành

**Nhiệm vụ.** Trên tệp 5 GB, lấy 100 bản ghi lớn nhất bằng hai cách: sắp xếp toàn bộ rồi cắt, và đống giữ kích thước 100. Đo thời gian và bộ nhớ đỉnh của cả hai. So dựng đống một lần với chèn lần lượt trên một triệu phần tử.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là chọn cấu trúc theo ràng buộc bộ nhớ và chứng minh bằng số đo. Kiểm bằng cặp số đo bộ nhớ; đạt khi bản dùng đống giữ bộ nhớ theo N chứ theo kích thước dữ liệu.

**Điều kiện đạt.** Bản dùng đống giữ bộ nhớ đỉnh theo N và cho cùng kết quả, kèm số đo so với cách sắp xếp toàn bộ.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Sắp xếp toàn bộ để lấy vài phần tử · dùng đống khi cần thứ tự đầy đủ · chèn lần lượt thay vì dựng một lần · bỏ qua bộ nhớ khi so.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/037-heaps-priority-queues-top-k.md`
- Nội dung học thuật: `note.md` cùng thư mục.
