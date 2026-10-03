# Phase 1: Engineering Foundation
# Module 3: Data Structures and Algorithms for Systems
# Lesson 39: External merge sort and IO amplification

## Thực hành

**Nhiệm vụ.** Cài sắp xếp ngoài cho tệp 2 GB với ngân sách bộ nhớ 100 MB. Kiểm kết quả đã sắp xếp đúng. Chạy lại ở ba mức bộ nhớ và đo tổng byte đọc cùng ghi. Tính hệ số khuếch đại vào ra cho từng mức và vẽ quan hệ.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một cài đặt có số đo giải thích được bằng cơ chế hai pha. Kiểm bằng bảng ba mức bộ nhớ; đạt khi sắp xếp đúng ở mọi mức và hệ số khuếch đại đo được giảm khi tăng bộ nhớ.

**Điều kiện đạt.** Kết quả sắp xếp đúng ở cả ba mức bộ nhớ, và hệ số khuếch đại vào ra giảm khi tăng bộ nhớ có số chứng minh.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đọc cả tệp vào bộ nhớ · dùng số đoạn trộn quá lớn so với bộ nhớ · chỉ đo thời gian mà không đo byte đọc ghi · không kiểm kết quả đã sắp xếp đúng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/039-external-merge-sort-io-amplification.md`
- Nội dung học thuật: `note.md` cùng thư mục.
