# Phase 1: Engineering Foundation
# Module 3: Data Structures and Algorithms for Systems
# Lesson 35: Hash tables - collisions, load factor and resize

## Thực hành

**Nhiệm vụ.** Cài cả hai cách xử lý va chạm. Đo thời gian tra cứu ở năm mức hệ số tải. Đo chi phí của một lần cấp lại. Thay hàm băm tốt bằng một hàm băm kém có chủ ý và đo lại. Tạo một tập khoá cố tình va chạm và đo mức suy biến.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi nối tham số cấu hình với hành vi quan sát được. Kiểm bằng bảng đo nhiều hệ số tải cộng thí nghiệm va chạm; đạt khi đường cong đúng dạng và thí nghiệm va chạm cho thấy suy biến.

**Điều kiện đạt.** Bảng đo năm mức hệ số tải cho đường cong đúng dạng, và tập khoá va chạm làm tra cứu suy biến có số chứng minh.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Coi bảng băm là hộp đen · để hệ số tải rất cao · dùng địa chỉ mở mà không xử lý bia mộ khi xoá · giả định hàm băm mặc định luôn an toàn.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/035-hash-tables-collisions-load-factor-resize.md`
- Nội dung học thuật: `note.md` cùng thư mục.
