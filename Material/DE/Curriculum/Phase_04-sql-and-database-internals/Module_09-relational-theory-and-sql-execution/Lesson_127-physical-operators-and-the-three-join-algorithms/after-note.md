# Phase 4: SQL and Database Internals
# Module 9: Relational Theory and SQL Execution
# Lesson 127: Physical operators and the three join algorithms

## Thực hành

**Nhiệm vụ.** Tạo bốn tình huống khác nhau về kích thước hai bên và sự có mặt của chỉ mục. Với mỗi cái, viết dự đoán thuật toán kết trước khi chạy, rồi đọc kế hoạch để đối chiếu. Giảm bộ nhớ làm việc tới khi thấy tràn đĩa trong kế hoạch và đo mức chậm đi.

Lưu SQL, seed/workload, dự đoán trước khi chạy, plan dạng máy đọc được, output thô, đối soát và thông số môi trường. Chỉ chạy DDL/spill/load test trong môi trường cô lập với lock/statement timeout; ảnh chụp không thay artifact tái chạy.

## Kiểm tra cuối bài

1. Nested loop phù hợp trường hợp nào?
2. Hash batches lớn hơn một nói gì?
3. Index-only scan vẫn fetch heap khi nào?
4. work_mem nhân theo operations ra sao?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective nối kiến thức tự cài ở lesson 40 với lựa chọn thật của engine. Kiểm bằng bốn tình huống; đạt khi dự đoán đúng ít nhất ba và giải thích đúng trường hợp tràn đĩa.

**Điều kiện đạt.** Dự đoán đúng ≥ 3/4 tình huống, và chỉ ra được dấu hiệu tràn đĩa trong kế hoạch kèm số đo mức chậm đi.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Nghĩ một thuật toán kết luôn nhanh hơn · bỏ qua bộ nhớ làm việc · không phân biệt quét chỉ mục với quét chỉ mục có phủ · kết luận mà không đọc kế hoạch.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/15-physical-operators-and-join-algorithms.md`
- Nội dung học thuật: `note.md` cùng thư mục.
