# Phase 10: System Design, AI Boundary and Trajectory
# Module 29: Staff and Principal Trajectory
# Lesson 434: Architecture decision records for irreversible choices

## Thực hành

**Nhiệm vụ.** Chọn ba quyết định khó đảo ngược trong hệ đã dựng. Viết bản ghi cho từng cái. Với mỗi bản, liệt kê ít nhất hai hệ quả xấu cụ thể và một điều kiện xem lại có thể kiểm bằng số đo. Đưa cho một người chưa tham gia quyết định và hỏi họ có hiểu vì sao chọn vậy không. Thay thế một bản ghi cũ và giữ bản cũ.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective đòi trung thực về hệ quả xấu. Kiểm bằng rà soát chéo; đạt khi cả ba bản có ít nhất hai hệ quả xấu cụ thể và điều kiện xem lại kiểm được, và không bản nào viết cho quyết định dễ đảo.

**Điều kiện đạt.** Ba bản ghi có ≥ 2 hệ quả xấu cụ thể và điều kiện xem lại kiểm được bằng số đo, và người chưa tham gia hiểu được lý do chọn.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Viết bản ghi cho mọi quyết định · chỉ liệt kê ưu điểm · sửa bản ghi cũ khi quyết định đổi · viết điều kiện xem lại mơ hồ không kiểm được.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/322-architecture-decision-records-for-irreversible-choices.md`
- Nội dung học thuật: `note.md` cùng thư mục.
