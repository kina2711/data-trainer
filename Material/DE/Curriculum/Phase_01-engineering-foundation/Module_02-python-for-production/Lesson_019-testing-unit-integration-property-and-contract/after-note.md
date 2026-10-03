# Phase 1: Engineering Foundation
# Module 2: Python for Production
# Lesson 19: Testing - unit, integration, property and contract

## Thực hành

**Nhiệm vụ.** Viết cả bốn loại phép kiểm cho gói ở lesson 18. Giảng viên tiêm năm lỗi vào mã. Chạy bộ kiểm và ghi lỗi nào bị bắt bởi loại nào. Cố định thời gian và ngẫu nhiên, chạy bộ kiểm 20 lần liên tiếp và chứng minh kết quả không đổi.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective đòi chọn đúng loại phép kiểm cho từng mục tiêu, chứ tăng độ phủ. Kiểm bằng bài tiêm lỗi; đạt khi bộ kiểm bắt được ít nhất bốn trong năm lỗi và phép kiểm tính chất bắt ít nhất một ca mà phép kiểm đơn vị bỏ sót.

**Điều kiện đạt.** Bộ kiểm bắt ≥ 4/5 lỗi tiêm, phép kiểm tính chất bắt ≥ 1 ca mà phép kiểm đơn vị bỏ sót, và 20 lần chạy cho kết quả giống nhau.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Thay thế cả thành phần bên trong · viết phép kiểm phụ thuộc thời gian thật · chạy theo độ phủ · bỏ phép kiểm tích hợp vì chậm.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/019-testing-unit-integration-property-contract.md`
- Nội dung học thuật: `note.md` cùng thư mục.
