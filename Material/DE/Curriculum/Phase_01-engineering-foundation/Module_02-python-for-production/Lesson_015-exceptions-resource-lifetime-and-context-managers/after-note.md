# Phase 1: Engineering Foundation
# Module 2: Python for Production
# Lesson 15: Exceptions, resource lifetime and context managers

## Thực hành

**Nhiệm vụ.** Viết một hàm mở kết nối, xử lý, rồi đóng. Gây lỗi giữa chừng 100 lần và đếm số kết nối còn mở. Viết lại bằng trình quản lý ngữ cảnh và đếm lại. Dịch một ngoại lệ thấp tầng sang lỗi có nghĩa ở ranh giới, giữ nguyên nhân gốc, và kiểm bằng cách đọc dấu vết.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là hai tính chất kiểm được bằng thực nghiệm chứ bằng đọc mã. Kiểm bằng thí nghiệm gây lỗi; đạt khi không kết nối nào còn mở sau 100 lần lỗi và mọi lỗi đều lộ ra kèm nguyên nhân gốc.

**Điều kiện đạt.** Sau 100 lần gây lỗi không còn kết nối nào mở, và mọi lỗi ở ranh giới đều giữ được nguyên nhân gốc trong dấu vết.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Bắt mọi ngoại lệ rồi bỏ qua · đóng tài nguyên trong nhánh thành công mà quên nhánh lỗi · dịch lỗi mà mất nguyên nhân gốc · thông báo lỗi chỉ ghi thất bại.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/015-exceptions-resource-lifetime-context-managers.md`
- Nội dung học thuật: `note.md` cùng thư mục.
