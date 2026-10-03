# Phase 8: Distributed Systems, Streaming and Compute
# Module 21: Kafka and Event Streaming
# Lesson 328: Offset commit - the two failure windows

## Thực hành

**Nhiệm vụ.** Cài hai bản: ghi vị trí trước khi xử lý và sau khi xử lý. Giết tiến trình 100 lần ở từng bản và đếm số bản ghi mất cùng số bản ghi xử lý lại. Chọn bản gây trùng và thêm đích luỹ đẳng bằng khoá xác định; chạy lại và đối soát. Đọc độ trễ tiêu thụ theo ba cách trong lúc bên tiêu thụ chậm và giải thích ba kết luận khác nhau.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi chứng minh đánh đổi thay vì phát biểu nó. Kiểm bằng hai thí nghiệm giết tiến trình; đạt khi số mất và số trùng được đếm ở hai thứ tự, và bản có đích luỹ đẳng đưa số trùng quan sát được về không.

**Điều kiện đạt.** Hai cửa sổ hỏng có số đo mất và trùng qua 100 lần giết, và bản có đích luỹ đẳng đưa số trùng quan sát được về không.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dùng ghi vị trí tự động rồi suy luận về cửa sổ hỏng · ghi vị trí trước khi xử lý · đọc độ trễ chỉ theo số bản ghi · đặt lại vị trí về cuối để làm sạch cảnh báo mà không đối soát.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/216-offset-commit-the-two-failure-windows.md`
- Nội dung học thuật: `note.md` cùng thư mục.
