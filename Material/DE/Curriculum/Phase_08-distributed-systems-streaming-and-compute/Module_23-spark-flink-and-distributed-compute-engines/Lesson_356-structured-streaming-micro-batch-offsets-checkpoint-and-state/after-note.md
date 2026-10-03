# Phase 8: Distributed Systems, Streaming and Compute
# Module 23: Spark, Flink and Distributed Compute Engines
# Lesson 356: Structured streaming - micro-batch, offsets, checkpoint and state

## Thực hành

**Nhiệm vụ.** Dựng công việc dòng có phép gộp theo cửa sổ. Chạy vài giờ và đo kích thước trạng thái theo thời gian; chứng minh nó phình khi chưa có hết hạn. Đặt cơ chế hết hạn và đo lại. Giết công việc và khôi phục từ điểm kiểm tra; đối soát kết quả. Xoá điểm kiểm tra và chỉ ra hậu quả. Thử đổi lược đồ trạng thái và ghi lại phản ứng.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là tiếp tục đúng chỗ và trạng thái có trần. Kiểm bằng phép thử giết và đo trạng thái; đạt khi khôi phục không mất và không trùng ngoài giới hạn đã nêu, và kích thước trạng thái ổn định sau khi đặt hết hạn.

**Điều kiện đạt.** Khôi phục từ điểm kiểm tra không mất và không trùng ngoài giới hạn đã nêu, và kích thước trạng thái ổn định sau khi đặt hết hạn.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Coi mô hình theo lô nhỏ là dòng chảy từng bản ghi · để trạng thái không có cơ chế hết hạn · xoá điểm kiểm tra để khởi động lại sạch · đổi lược đồ trạng thái mà không có kế hoạch.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/244-structured-streaming-micro-batch-offsets-checkpoint-and-state.md`
- Nội dung học thuật: `note.md` cùng thư mục.
