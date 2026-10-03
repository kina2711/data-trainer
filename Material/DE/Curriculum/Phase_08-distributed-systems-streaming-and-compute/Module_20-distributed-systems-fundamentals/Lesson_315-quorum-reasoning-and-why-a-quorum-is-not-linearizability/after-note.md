# Phase 8: Distributed Systems, Streaming and Compute
# Module 20: Distributed Systems Fundamentals
# Lesson 315: Quorum reasoning, and why a quorum is not linearizability

## Thực hành

**Nhiệm vụ.** Dựng kho khoá giá trị không người dẫn với tham số số đông cấu hình được. Tái hiện ba ca: phép ghi hỏng giữa chừng, hai phép đọc liên tiếp thấy mới rồi cũ, và số đông lỏng làm mất bảo đảm giao nhau. Với mỗi ca, nêu cơ chế còn thiếu. Bật sửa khi đọc và đo nó giảm ca nào, không giảm ca nào.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective nhắm vào một kết luận sai rất phổ biến. Kiểm bằng ba ca tái hiện; đạt khi cả ba được tái hiện bằng dữ liệu và nêu đúng cơ chế còn thiếu cho từng ca.

**Điều kiện đạt.** Ba ca được tái hiện bằng dữ liệu, mỗi ca nêu đúng cơ chế còn thiếu, và hiệu lực của sửa khi đọc được đo theo từng ca.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Kết luận số đông suy ra tuần tự hoá được · bật số đông lỏng mà không nói rõ mất bảo đảm gì · không có cách so phiên bản giữa các bản sao · tin sửa khi đọc chữa được mọi ca.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/203-quorum-reasoning-and-why-a-quorum-is-not-linearizability.md`
- Nội dung học thuật: `note.md` cùng thư mục.
