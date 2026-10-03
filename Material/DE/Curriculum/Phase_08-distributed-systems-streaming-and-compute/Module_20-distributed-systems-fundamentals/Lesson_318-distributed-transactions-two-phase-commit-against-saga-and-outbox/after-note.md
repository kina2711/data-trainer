# Phase 8: Distributed Systems, Streaming and Compute
# Module 20: Distributed Systems Fundamentals
# Lesson 318: Distributed transactions - two-phase commit against saga and outbox

## Thực hành

**Nhiệm vụ.** Cài cùng một quy trình đặt hàng gồm thanh toán và trừ kho theo cả ba cách. Với mỗi cách, giết tiến trình tại từng ranh giới và ghi trạng thái cuối. Tái hiện ca điều phối viên chết sau pha chuẩn bị và đo thời gian tài nguyên bị khoá. Lập ma trận hỏng ba cách nhân các ranh giới. Chọn một cách cho một bối cảnh và nêu trạng thái trung gian mà nghiệp vụ phải chấp nhận.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi so ba mô hình hỏng chứ ba cách cài đặt. Kiểm bằng ma trận hỏng; đạt khi mỗi cách có hành vi ghi rõ tại mọi ranh giới hỏng và ca điều phối viên chết được tái hiện thật.

**Điều kiện đạt.** Ma trận hỏng đầy đủ cho cả ba cách tại mọi ranh giới, ca điều phối viên chết được tái hiện kèm thời gian khoá đo được.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dùng chốt hai pha mà không tính ca điều phối viên chết · viết thao tác bù bằng cách hoàn tác kỹ thuật thay vì bù nghĩa nghiệp vụ · gửi thông điệp ngoài giao dịch cục bộ · tuyên bố nguyên tử xuyên hệ.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/206-distributed-transactions-two-phase-commit-against-saga-and-outbox.md`
- Nội dung học thuật: `note.md` cùng thư mục.
