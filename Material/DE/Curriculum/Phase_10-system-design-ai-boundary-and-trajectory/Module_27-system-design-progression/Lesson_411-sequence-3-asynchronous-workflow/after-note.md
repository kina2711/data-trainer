# Phase 10: System Design, AI Boundary and Trajectory
# Module 27: System Design Progression
# Lesson 411: Sequence 3 - asynchronous workflow

## Thực hành

**Nhiệm vụ.** Thiết kế nền tảng nhật ký. Chỉ ra ranh giới đồng bộ và bất đồng bộ cùng lý do. Viết hợp đồng người dùng cho phần bất đồng bộ gồm cách tra trạng thái và cách báo thất bại. Thiết kế áp lực ngược và chính sách bản ghi độc. Tính năng lực cho phần đệm khi bên tiêu thụ dừng một giờ.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective gồm một hệ quả về hợp đồng mà thiết kế hay bỏ qua. Kiểm bằng rà soát thiết kế; đạt khi ranh giới đồng bộ và bất đồng bộ có lý do, hợp đồng người dùng nêu cách tra trạng thái cùng cách báo thất bại, và áp lực ngược có cơ chế cụ thể.

**Điều kiện đạt.** Ranh giới đồng bộ và bất đồng bộ có lý do, hợp đồng người dùng đủ hai phần, và năng lực đệm khi bên tiêu thụ dừng một giờ tính được.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chuyển sang bất đồng bộ mà không đổi hợp đồng với người dùng · không có cách tra trạng thái · để hàng đợi không giới hạn · bỏ chính sách bản ghi độc.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/299-sequence-3-asynchronous-workflow.md`
- Nội dung học thuật: `note.md` cùng thư mục.
