# Phase 1: Engineering Foundation
# Module 4: Computer Architecture and the Performance Model
# Lesson 45: The memory hierarchy and the cost model

## Thực hành

**Nhiệm vụ.** Cho ba chương trình, mỗi cái nghẽn ở một tầng khác nhau. Với mỗi cái, đo mức dùng CPU, băng thông bộ nhớ và thời gian chờ vào ra, rồi phân loại nút thắt. Viết bộ số mốc từ chính máy của mình bằng cách đo, không chép từ tài liệu.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Bài mở module, người học đã biết đo từ lesson 21 nên đủ nền để phân loại. Kiểm bằng ba chương trình có ba loại nút thắt khác nhau; đạt khi phân loại đúng cả ba và mỗi lần dẫn được một số đo cụ thể.

**Điều kiện đạt.** Phân loại đúng cả ba nút thắt kèm số đo, và có bộ số mốc đo trên chính máy mình.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Kết luận nghẽn CPU vì thấy CPU cao trong khi thực ra là chờ bộ nhớ · tối ưu thuật toán khi nút thắt là đĩa · dùng số mốc của máy khác.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/045-memory-hierarchy-cost-model.md`
- Nội dung học thuật: `note.md` cùng thư mục.
