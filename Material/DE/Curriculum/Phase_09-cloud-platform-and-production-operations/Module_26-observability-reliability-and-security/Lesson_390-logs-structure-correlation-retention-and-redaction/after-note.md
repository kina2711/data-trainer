# Phase 9: Cloud Platform and Production Operations
# Module 26: Observability, Reliability and Security
# Lesson 390: Logs - structure, correlation, retention and redaction

## Thực hành

**Nhiệm vụ.** Thống nhất lược đồ nhật ký cho ba dịch vụ. Truyền định danh tương quan qua cả lời gọi trực tiếp lẫn hàng đợi. Chạy 100 yêu cầu và truy vấn nhật ký theo định danh; đếm số yêu cầu nối đủ chặng. Cài che dữ liệu tại nơi sinh và chạy bộ quét tìm dữ liệu nhạy cảm. Đặt lấy mẫu cùng thời hạn giữ và tính chi phí.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có hai tiêu chí nghiệm thu kiểm được bằng truy vấn. Kiểm bằng phép thử tương quan cộng bộ quét; đạt khi 100 yêu cầu qua hàng đợi đều nối đủ chặng, và bộ quét không tìm thấy dữ liệu nhạy cảm trong nhật ký.

**Điều kiện đạt.** 100 yêu cầu qua hàng đợi đều nối đủ chặng, bộ quét không tìm thấy dữ liệu nhạy cảm, và chi phí nhật ký được tính.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Để định danh tương quan rơi mất ở ranh giới hàng đợi · che dữ liệu ở nơi lưu thay vì nơi sinh · ghi toàn bộ thân yêu cầu vào nhật ký · giữ mọi nhật ký vô thời hạn.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/278-logs-structure-correlation-retention-and-redaction.md`
- Nội dung học thuật: `note.md` cùng thư mục.
