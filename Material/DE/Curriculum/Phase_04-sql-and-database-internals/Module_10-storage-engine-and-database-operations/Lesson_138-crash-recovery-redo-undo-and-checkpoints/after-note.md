# Phase 4: SQL and Database Internals
# Module 10: Storage Engine and Database Operations
# Lesson 138: Crash recovery - redo, undo and checkpoints

## Thực hành

**Nhiệm vụ.** Chạy ba tình huống: giết cơ sở dữ liệu khi có giao dịch chưa chốt, khi vừa chốt xong, và đúng lúc đang chốt. Viết dự đoán trước, rồi khởi động lại và đối chiếu. Đo thời gian khôi phục ở hai chu kỳ điểm kiểm tra khác nhau và ghi tải vào ra nền tương ứng.

Chỉ chạy workload, compaction, cấu hình WAL/checkpoint hoặc crash injection trong instance thử nghiệm cô lập có seed/snapshot khôi phục. Không tắt `fsync`, phá cache, kill hoặc ép compaction trên production. Lưu config, raw counters, client operation-ID ledger và log; ảnh chụp không thay artifact tái chạy.

## Kiểm tra cuối bài

1. PostgreSQL khác ARIES undo ở đâu?
2. Checkpoint là point hay interval?
3. Crash trong commit tạo ambiguity nào?
4. Đo recovery trade-off cần counters gì?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi suy kết cục từ cơ chế, rồi kiểm bằng thí nghiệm hỏng. Kiểm bằng ba tình huống cộng bảng hai chu kỳ; đạt khi dự đoán đúng cả ba và bảng cho thấy đúng chiều đánh đổi.

**Điều kiện đạt.** Dự đoán đúng kết cục cả ba tình huống, và bảng hai chu kỳ điểm kiểm tra cho thấy đúng chiều đánh đổi có số.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Nghĩ khôi phục chỉ có làm lại · đặt điểm kiểm tra rất thưa để giảm tải rồi thời gian khôi phục vượt cam kết · không đo thời gian khôi phục bao giờ.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/26-crash-recovery-redo-undo-and-checkpoints.md`
- Nội dung học thuật: `note.md` cùng thư mục.
