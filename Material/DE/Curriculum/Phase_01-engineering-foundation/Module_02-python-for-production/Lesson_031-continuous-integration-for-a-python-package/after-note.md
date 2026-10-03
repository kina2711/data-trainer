# Phase 1: Engineering Foundation
# Module 2: Python for Production
# Lesson 31: Continuous integration for a Python package

## Thực hành

**Nhiệm vụ.** Dựng quy trình sáu bước cho gói. Bật cửa chặn hợp nhất. Nộp năm yêu cầu hợp nhất hỏng theo năm cách khác nhau, mỗi cách ứng với một bước, và xác nhận cả năm bị chặn ở đúng bước. Bật bộ nhớ đệm phụ thuộc và đo thời gian trước sau.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một cấu hình có hai ràng buộc đo được là tính chặn và thời gian. Kiểm bằng phép thử nộp mã hỏng; đạt khi mọi loại hỏng đều bị chặn và thời gian chạy dưới ngưỡng.

**Điều kiện đạt.** Năm yêu cầu hỏng đều bị chặn ở đúng bước, thời gian chạy dưới ngưỡng sau khi bật bộ nhớ đệm, và cửa chặn hợp nhất hoạt động.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Cho phép hợp nhất khi quy trình đỏ · đặt bước chậm lên đầu · không quét lịch sử kho · thông báo hỏng không nói hỏng ở bước nào.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/031-continuous-integration-python-package.md`
- Nội dung học thuật: `note.md` cùng thư mục.
