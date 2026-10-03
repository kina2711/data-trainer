# Phase 10: System Design, AI Boundary and Trajectory
# Module 27: System Design Progression
# Lesson 414: The failure table and the remove-component test

## Thực hành

**Nhiệm vụ.** Với một thiết kế đã làm, lập bảng chế độ hỏng đủ sáu cột cho mọi thành phần. Chạy phép thử bỏ thành phần cho từng hộp và ghi bảo đảm mất đi. Gỡ mọi hộp không biện minh được và vẽ lại sơ đồ. So số thành phần trước và sau.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi biện minh từng thành phần chứ mô tả chúng. Kiểm bằng hai hiện vật; đạt khi mọi thành phần có ít nhất một dòng trong bảng hỏng kèm hệ quả với dữ liệu, và mọi hộp qua được phép thử bỏ thành phần hoặc bị gỡ.

**Điều kiện đạt.** Mọi thành phần có dòng trong bảng hỏng kèm hệ quả với dữ liệu, và mọi hộp còn lại đều qua phép thử bỏ thành phần.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Bỏ cột hệ quả với dữ liệu · viết ứng phó mà không nói cách phát hiện · giữ thành phần vì kiến trúc tham khảo nào đó có nó · chạy phép thử bỏ thành phần chỉ cho vài hộp.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/302-the-failure-table-and-the-remove-component-test.md`
- Nội dung học thuật: `note.md` cùng thư mục.
