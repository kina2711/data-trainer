# Phase 2: Machine, Operating System and Network
# Module 5: Operating Systems, Concurrency and Linux
# Lesson 71: Tracing a program with strace and perf

## Thực hành

**Nhiệm vụ.** Cho ba chương trình: một treo khi khởi động, một bận CPU bất thường, một chậm vì gọi hệ thống quá nhiều. Với mỗi cái, chọn công cụ, chạy, và định vị nguyên nhân. Với chương trình treo, chỉ ra chính xác lời gọi hệ thống nó đang chờ.

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective là chọn công cụ theo câu hỏi rồi đọc kết quả, kỹ năng dùng lại suốt phần vận hành. Kiểm bằng ba chương trình có ba triệu chứng; đạt khi chọn đúng công cụ ít nhất hai và định vị đúng nguyên nhân.

**Điều kiện đạt.** Chọn đúng công cụ ≥ 2/3 trường hợp và định vị đúng nguyên nhân, kể cả chỉ ra lời gọi mà chương trình treo đang chờ.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dùng theo dõi lời gọi hệ thống cho chương trình bận CPU · chạy công cụ theo dõi trên sản xuất lúc tải cao · đọc kết quả mà không đếm theo lời gọi · bỏ qua thời gian nằm trong lời gọi.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/071-tracing-a-program-with-strace-and-perf.md`
- Nội dung học thuật: `note.md` cùng thư mục.
