# Phase 8: Distributed Systems, Streaming and Compute
# Module 20: Distributed Systems Fundamentals
# Lesson 317: Leases, fencing tokens and the returning old leader

## Thực hành

**Nhiệm vụ.** Dựng dịch vụ cấp hợp đồng thuê và một tài nguyên dùng chung. Tạm dừng tiến trình giữ khoá lâu hơn hạn thuê rồi cho chạy tiếp; ghi lại dữ liệu hỏng. Thêm thẻ chặn tăng dần và cưỡng chế ở phía tài nguyên; chạy lại và chứng minh yêu cầu cũ bị từ chối. Thử cưỡng chế ở phía khách và chỉ ra vì sao không đủ.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có một ca hỏng cụ thể phải tái hiện được trước khi sửa. Kiểm bằng phép thử tạm dừng tiến trình; đạt khi ca hỏng được tái hiện kèm bằng chứng dữ liệu sai, và bản có thẻ chặn từ chối đúng mọi yêu cầu cũ.

**Điều kiện đạt.** Ca hai tiến trình cùng ghi được tái hiện kèm bằng chứng dữ liệu sai, và bản có thẻ chặn từ chối đúng 100% yêu cầu mang số cũ.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dùng hợp đồng thuê mà không có thẻ chặn · cưỡng chế thẻ chặn ở phía khách · đặt hạn thuê ngắn hơn thời gian tạm dừng có thể xảy ra · giả định tiến trình không bao giờ bị tạm dừng lâu.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/205-leases-fencing-tokens-and-the-returning-old-leader.md`
- Nội dung học thuật: `note.md` cùng thư mục.
