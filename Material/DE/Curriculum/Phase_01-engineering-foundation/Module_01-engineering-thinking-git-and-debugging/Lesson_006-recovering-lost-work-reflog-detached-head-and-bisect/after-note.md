# Phase 1: Engineering Foundation
# Module 1: Engineering Thinking, Git and Debugging
# Lesson 6: Recovering lost work - reflog, detached HEAD and bisect

## Thực hành

**Nhiệm vụ.** Tự gây cả ba tình huống mất việc rồi phục hồi từng cái bằng nhật ký tham chiếu, ghi lại ghi chú phục hồi. Tạo 8 commit, cài một hồi quy ở commit thứ tư, viết một phép kiểm trả mã thoát đúng, rồi chạy chia đôi tự động và xác nhận nó chỉ ra commit 4.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là hai thao tác cứu nguy kiểm được bằng kết quả. Kiểm bằng ba tình huống mất việc cộng một lần chia đôi; đạt khi phục hồi cả ba và chia đôi chỉ đúng commit gây lỗi.

**Điều kiện đạt.** Phục hồi thành công cả ba tình huống có ghi chú, và chia đôi tự động chỉ đúng commit 4.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Không biết nhật ký tham chiếu tồn tại · chia đôi thủ công thay vì dùng phép kiểm tự động · commit quá to nên chia đôi chỉ tới một commit đổi 40 tệp · hoảng rồi clone lại kho.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/006-recovering-lost-work-reflog-detached-head-bisect.md`
- Nội dung học thuật: `note.md` cùng thư mục.
