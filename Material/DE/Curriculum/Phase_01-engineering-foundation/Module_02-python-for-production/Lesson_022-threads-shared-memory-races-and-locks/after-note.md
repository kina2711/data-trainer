# Phase 1: Engineering Foundation
# Module 2: Python for Production
# Lesson 22: Threads - shared memory, races and locks

## Thực hành

**Nhiệm vụ.** Viết một bộ đếm dùng chung cho 8 luồng và chứng minh kết quả sai. Tăng khả năng tái hiện bằng cách chèn điểm dừng, đạt 10/10 lần sai. Sửa bằng khoá, chạy 1000 lần và xác nhận không sai lần nào. Tạo một khoá chết có chủ ý, chẩn đoán và sửa bằng cách sắp thứ tự lấy khoá.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi biến một lỗi ngẫu nhiên thành lỗi tái hiện được, kỹ năng khó và dùng lại ở M5. Kiểm bằng bài tái hiện cộng sửa; đạt khi tái hiện được 10/10 lần trước khi sửa và 0/1000 lần sau khi sửa.

**Điều kiện đạt.** Tái hiện sai 10/10 lần trước khi sửa, 0/1000 lần sau khi sửa, và chẩn đoán được khoá chết bằng bốn điều kiện.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Kết luận lỗi ngẫu nhiên nên bỏ qua · thêm khoá khắp nơi rồi mất hết tác dụng của nhiều luồng · dùng luồng cho tác vụ thiên CPU · cắt ngang luồng thay vì báo dừng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/022-threads-shared-memory-races-locks.md`
- Nội dung học thuật: `note.md` cùng thư mục.
