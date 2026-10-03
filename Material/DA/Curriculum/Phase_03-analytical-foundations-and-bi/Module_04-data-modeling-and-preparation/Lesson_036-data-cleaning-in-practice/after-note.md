# Phase 3: Data Analyst
# Module 4: Data Modeling and Preparation
# Lesson 36: Data cleaning in practice

## Thực hành

**Nhiệm vụ.** Nạp `orders.csv` gồm 50.000 dòng và xử lý đủ bốn bẫy định dạng. Rồi nạp `orders_dirty.csv` gồm 50.005 dòng vào bảng trung chuyển; kết quả phải chứng minh 50.005 = 49.985 bản ghi qua được ép kiểu + 20 bản ghi bị loại, mỗi bản ghi bị loại có lý do ghi rõ. Nếu áp thêm khoá chính và ràng buộc không rỗng thì bảng chính chỉ nhận 49.980 dòng; giải thích chênh lệch 5 dòng.

Giữ input snapshot, grain, identity, version, raw output, reconciliation và limitation.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Kiểm bằng một đẳng thức kiểm chứng được: 50.000 = 49.985 + 15, và mỗi bản ghi trong bảng lỗi phải có lý do ghi rõ. Đẳng thức này bắt được lỗi phổ biến nhất của bài — loại bản ghi hỏng mà không ghi lại.

**Điều kiện đạt.** Đẳng thức 50.000 = 49.985 + 15 kiểm được bằng truy vấn, và cả 15 bản ghi lỗi có lý do ghi rõ.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 60 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 25 phút trả lời bốn câu kiểm tra · 15 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Bỏ qua dòng lỗi trong im lặng nên mất dấu vết · đặt bước lọc trước bước ép kiểu · để công cụ tự suy đoán mã hoá ký tự.

## Reference
- Knowledge note: `Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/036-data-cleaning-in-practice.md`
