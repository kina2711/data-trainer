# Phase 9: Cloud Platform and Production Operations
# Module 25: Containers, Infrastructure as Code and Kubernetes
# Lesson 377: Supply chain - minimal base, pinned digest, no secret in a layer

## Thực hành

**Nhiệm vụ.** Dựng quy trình gồm quét lỗ hổng có ngưỡng chặn, sinh bản kê thành phần, và kiểm ghim mã băm. Tiêm ba vi phạm: ảnh nền ghim theo thẻ, một phụ thuộc có lỗ hổng nghiêm trọng, và một bí mật lọt vào lớp. Xác nhận cả ba bị chặn. So số lỗ hổng giữa ảnh nền đầy đủ và ảnh nền tối thiểu. Đặt hạn cho mọi miễn trừ.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một cửa chặn tự động có phép thử tiêm. Kiểm bằng ba vi phạm; đạt khi cả ba bị chặn ở đúng bước, bản kê thành phần sinh được, và mọi miễn trừ có hạn.

**Điều kiện đạt.** Ba vi phạm bị chặn ở đúng bước, bản kê thành phần sinh được, số lỗ hổng giảm có số đo khi đổi ảnh nền, và mọi miễn trừ có hạn.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Quét mà không chặn · ghim ảnh nền theo thẻ · miễn trừ lỗ hổng không có hạn · để nhật ký tích hợp liên tục in ra bí mật.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/265-supply-chain-minimal-base-pinned-digest-no-secret-in-a-layer.md`
- Nội dung học thuật: `note.md` cùng thư mục.
