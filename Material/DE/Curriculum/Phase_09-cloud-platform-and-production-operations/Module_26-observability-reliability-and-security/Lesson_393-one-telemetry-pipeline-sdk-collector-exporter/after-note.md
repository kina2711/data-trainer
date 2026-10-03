# Phase 9: Cloud Platform and Production Operations
# Module 26: Observability, Reliability and Security
# Lesson 393: One telemetry pipeline - SDK, collector, exporter

## Thực hành

**Nhiệm vụ.** Dựng đường tín hiệu cho ba dịch vụ với một bộ thu gom chung. Đặt che dữ liệu nhạy cảm và lấy mẫu ở bộ thu gom; xác nhận có hiệu lực cho cả ba mà không sửa ứng dụng. Dựng nhịp tim và cảnh báo mất tín hiệu. Dừng bộ thu gom và đo thời gian tới khi phát hiện. Làm đầy hàng đợi của bộ thu gom và quan sát hành vi. Tính chi phí đo lường.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective gồm một yêu cầu về chính hệ đo lường. Kiểm bằng phép thử mất tín hiệu; đạt khi mất tín hiệu được phát hiện trong ngưỡng thoả thuận và che dữ liệu ở bộ thu gom có hiệu lực cho cả ba dịch vụ.

**Điều kiện đạt.** Mất tín hiệu được phát hiện trong ngưỡng thoả thuận, che dữ liệu ở bộ thu gom có hiệu lực cho cả ba dịch vụ, và chi phí đo lường được tính.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đặt logic che dữ liệu trong từng ứng dụng · coi im lặng là hệ đang khoẻ · không theo dõi hàng đợi của bộ thu gom · bỏ chi phí đo lường khỏi ngân sách.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/281-one-telemetry-pipeline-sdk-collector-exporter.md`
- Nội dung học thuật: `note.md` cùng thư mục.
