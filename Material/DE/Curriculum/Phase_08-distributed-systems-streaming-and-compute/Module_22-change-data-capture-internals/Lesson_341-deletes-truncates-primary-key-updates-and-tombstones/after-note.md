# Phase 8: Distributed Systems, Streaming and Compute
# Module 22: Change Data Capture Internals
# Lesson 341: Deletes, truncates, primary key updates and tombstones

## Thực hành

**Nhiệm vụ.** Thực hiện bốn thao tác trên nguồn: xoá, cắt bảng, cập nhật khoá chính, và xoá theo tầng nhiều nghìn hàng. Sau mỗi thao tác, đối soát tập khoá và số lượng giữa nguồn và đích. Với cập nhật khoá chính, chứng minh không còn hàng mồ côi. Với cắt bảng, chỉ ra hệ có sinh sự kiện không và xử lý tường minh. Đo dồn ứ khi xoá theo tầng.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có bốn ca biên với tiêu chí nghiệm thu bằng đối soát. Kiểm bằng bốn thao tác tiêm; đạt khi đích khớp nguồn về tập khoá và số lượng sau cả bốn, và ca cắt bảng được xử lý tường minh.

**Điều kiện đạt.** Đích khớp nguồn về tập khoá và số lượng sau cả bốn thao tác, không còn hàng mồ côi, và ca cắt bảng có xử lý tường minh.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Bỏ qua sự kiện xoá · coi cập nhật khoá chính là một lần sửa thường · giả định cắt bảng sinh sự kiện mức hàng · không đo dồn ứ khi có thao tác hàng loạt.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/229-deletes-truncates-primary-key-updates-and-tombstones.md`
- Nội dung học thuật: `note.md` cùng thư mục.
