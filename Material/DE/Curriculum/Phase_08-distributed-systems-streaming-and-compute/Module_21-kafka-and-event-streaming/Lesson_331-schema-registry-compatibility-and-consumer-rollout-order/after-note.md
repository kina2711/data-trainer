# Phase 8: Distributed Systems, Streaming and Compute
# Module 21: Kafka and Event Streaming
# Lesson 331: Schema registry, compatibility and consumer rollout order

## Thực hành

**Nhiệm vụ.** Đăng ký lược đồ với mức tương thích chọn trước. Ghi 100.000 bản ghi bằng lược đồ cũ. Thực hiện một thay đổi tương thích và một thay đổi phá vỡ; xác nhận thay đổi phá vỡ bị sổ đăng ký chặn. Triển khai theo đúng thứ tự suy ra từ mức tương thích, với cả hai phía đang chạy tải. Đọc lại toàn bộ nhật ký từ đầu bằng bên tiêu thụ mới và đối soát.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là không gián đoạn ở cả hai phía. Kiểm bằng thí nghiệm triển khai có tải; đạt khi không bên tiêu thụ nào lỗi suốt quá trình và bản ghi cũ trong nhật ký vẫn đọc được sau khi nâng cấp.

**Điều kiện đạt.** Không bên tiêu thụ nào lỗi suốt quá trình triển khai, và bên tiêu thụ mới đọc lại toàn bộ nhật ký cũ với đối soát khớp.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Nâng cấp bên sản xuất trước khi mức tương thích cho phép · đặt sổ đăng ký ở chế độ không cưỡng chế · bỏ bản ghi không giải mã được · quên rằng dữ liệu cũ vẫn nằm trong nhật ký.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/219-schema-registry-compatibility-and-consumer-rollout-order.md`
- Nội dung học thuật: `note.md` cùng thư mục.
