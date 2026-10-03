# Phase 2: Data Analyst
# Module 3: SQL and Databases
# Lesson 27: Window functions (2) - running totals and period comparison

## Thực hành

**Nhiệm vụ.** Báo cáo 24 tháng trên `DS2` có đủ ba chỉ số. Đối chiếu khớp với bản làm bằng Excel.

Giữ input snapshot, grain, identity, version, raw output, reconciliation và limitation.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Kiểm bằng đối chiếu chéo công cụ: kết quả phải khớp với bản làm bằng Excel. Dữ liệu `DS2` có chứa tháng khuyết, nên bài không xử lý kỳ khuyết sẽ lệch ở đúng những tháng đó và lộ ra khi đối chiếu.

**Điều kiện đạt.** Báo cáo 24 tháng khớp với bản đối chứng bằng Excel ở cả ba chỉ số, gồm cả các tháng khuyết giao dịch.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 60 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 25 phút trả lời bốn câu kiểm tra · 15 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Bỏ qua tháng khuyết nên so kỳ lệch một bậc · dùng `RANGE` khi cần `ROWS` · dựa vào khung mặc định của `LAST_VALUE`.

## Reference
- Knowledge note: `Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/027-window-functions-2-running-totals-and-period-comparison.md`
