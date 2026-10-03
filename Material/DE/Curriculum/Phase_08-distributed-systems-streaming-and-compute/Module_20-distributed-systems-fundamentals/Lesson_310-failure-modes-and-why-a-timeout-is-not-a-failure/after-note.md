# Phase 8: Distributed Systems, Streaming and Compute
# Module 20: Distributed Systems Fundamentals
# Lesson 310: Failure modes and why a timeout is not a failure

## Thực hành

**Nhiệm vụ.** Dựng một dịch vụ có tác dụng phụ ghi được. Tiêm năm chế độ hỏng bằng lớp mạng giả lập: chậm, mất gói, nhân đôi, đảo thứ tự, và phân vùng. Với ca hết giờ, tạo cả ba kết cục thật và chứng minh trạng thái cuối đúng ở cả ba. Đo số lần tác dụng phụ lặp trước và sau khi thêm khoá chống trùng.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là trạng thái đúng bất kể kết cục thật của lời gọi. Kiểm bằng phép thử tiêm; đạt khi trạng thái cuối đúng ở cả ba khả năng và không tác dụng phụ nào xảy ra hai lần.

**Điều kiện đạt.** Trạng thái cuối đúng ở cả ba kết cục sau hết giờ, và không tác dụng phụ nào xảy ra hai lần qua 1.000 lượt tiêm.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Coi hết giờ là bên kia đã hỏng · thử lại thao tác không luỹ đẳng · giả định mất gói và chậm là một · tin bộ phát hiện hỏng nói đúng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/198-failure-modes-and-why-a-timeout-is-not-a-failure.md`
- Nội dung học thuật: `note.md` cùng thư mục.
