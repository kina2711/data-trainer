# Phase 1: Engineering Foundation
# Module 2: Python for Production
# Lesson 23: Processes - isolation, serialization and cost

## Thực hành

**Nhiệm vụ.** Chạy cùng phép tính thiên CPU ở ba kích thước dữ liệu, mỗi kích thước ở hai chế độ tuần tự và nhiều tiến trình. Đo thời gian và bộ nhớ. Tìm điểm giao. Đổi cách chia từ từng phần tử sang theo khối và đo lại phần cải thiện. Giết tiến trình chính và kiểm tiến trình con có mồ côi không.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi cân chi phí song song với phần tiết kiệm, chứ mặc định song song là nhanh. Kiểm bằng bảng ba kích thước công việc; đạt khi chỉ ra đúng điểm giao mà dưới đó tuần tự thắng.

**Điều kiện đạt.** Bảng ba kích thước nhân hai chế độ đủ thời gian và bộ nhớ, chỉ ra đúng điểm giao, và không còn tiến trình mồ côi sau khi giết tiến trình chính.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Song song hoá mọi thứ · chia theo từng phần tử · bỏ qua bộ nhớ khi tăng số tiến trình · để tiến trình con mồ côi khi tiến trình chính chết.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/023-processes-isolation-serialization-cost.md`
- Nội dung học thuật: `note.md` cùng thư mục.
