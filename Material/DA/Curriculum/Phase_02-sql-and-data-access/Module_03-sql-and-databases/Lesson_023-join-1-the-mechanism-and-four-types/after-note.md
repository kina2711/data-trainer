# Phase 2: Data Analyst
# Module 3: SQL and Databases
# Lesson 23: JOIN (1) - the mechanism and four types

## Thực hành

**Nhiệm vụ.** Tính bằng tay kết quả của bốn kiểu `JOIN` trên cặp bảng 4×3, ghi ra giấy, rồi chạy máy đối chiếu từng dòng.

Giữ input snapshot, grain, identity, version, raw output, reconciliation và limitation.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài xây cơ chế; thao tác trên dữ liệu thật nằm ở lesson 24. Kiểm bằng bài tính tay: tính đủ bốn kết quả `JOIN` trên bảng 4×3 trước khi chạy máy, rồi đối chiếu. Sai lệch giữa tính tay và kết quả máy là dấu hiệu mô hình cơ chế chưa đúng.

**Điều kiện đạt.** Bốn bảng kết quả tính tay khớp hoàn toàn với kết quả máy, kể cả số dòng và các dòng có `NULL`.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 40 phút đọc nguồn tham chiếu và tự giải thích lại · 25 phút trả lời bốn câu kiểm tra · 15 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Hình dung `JOIN` bằng biểu đồ Venn nên không giải thích được nhân bản dòng · giả định `LEFT JOIN` luôn giữ nguyên số dòng bảng trái · nhầm bản số quan hệ với kiểu `JOIN`.

## Reference
- Knowledge note: `Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/023-join-1-the-mechanism-and-four-types.md`
