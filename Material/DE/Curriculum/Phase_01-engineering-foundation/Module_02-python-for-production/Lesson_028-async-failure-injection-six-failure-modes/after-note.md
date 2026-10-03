# Phase 1: Engineering Foundation
# Module 2: Python for Production
# Lesson 28: Async failure injection - six failure modes

## Thực hành

**Nhiệm vụ.** Viết sáu phép thử tiêm lỗi chạy tự động. Với mỗi cái, ghi lại bằng chứng quan sát được trước khi phòng thủ, áp phòng thủ, rồi đo lại. Chạy phép thử tắt có kiểm soát nhận tín hiệu kết thúc và chứng minh mọi giao dịch đang dở hoặc hoàn tất hoặc quay lui. Lập bảng sáu hàng gồm cơ chế, bằng chứng và phòng thủ.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective tổng hợp bốn bài trước thành một hệ phòng vệ có bằng chứng. Kiểm bằng sáu phép thử tiêm; đạt khi cả sáu tái hiện được tự động và ít nhất năm có phòng thủ chứng minh bằng số đo trước sau.

**Điều kiện đạt.** Sáu phép thử tiêm chạy tự động, ≥ 5 phòng thủ có số đo trước sau, và tắt có kiểm soát không để giao dịch dở dang.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Thử bằng tay một lần rồi coi là xong · huỷ giữa một giao dịch mà không định nghĩa ranh giới công bố · đo phòng thủ mà không đo trước · bỏ tình huống tín hiệu tắt vì khó tái hiện.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/028-async-failure-injection-six-modes.md`
- Nội dung học thuật: `note.md` cùng thư mục.
