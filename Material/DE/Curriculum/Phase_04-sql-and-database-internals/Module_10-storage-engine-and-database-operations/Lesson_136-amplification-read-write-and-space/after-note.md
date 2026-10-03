# Phase 4: SQL and Database Internals
# Module 10: Storage Engine and Database Operations
# Lesson 136: Amplification - read, write and space

## Thực hành

**Nhiệm vụ.** Chạy cùng một khối lượng công việc ghi nặng trên PostgreSQL và trên một kho dùng cấu trúc gộp theo nhật ký. Đo cả ba đại lượng khuếch đại cho mỗi bên. Lặp lại với khối lượng đọc ngẫu nhiên nặng. Lập bảng và chọn engine cho hai tình huống cho trước.

Chỉ chạy workload, compaction, cấu hình WAL/checkpoint hoặc crash injection trong instance thử nghiệm cô lập có seed/snapshot khôi phục. Không tắt `fsync`, phá cache, kill hoặc ép compaction trên production. Lưu config, raw counters, client operation-ID ledger và log; ảnh chụp không thay artifact tái chạy.

## Kiểm tra cuối bài

1. Ba amplification ratio có numerator/denominator gì?
2. Vì sao cần drain maintenance debt?
3. Durability parity khóa những gì?
4. Negative lookup đo read amplification ra sao?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi chọn theo ba tiêu chí đối nghịch dựa trên số tự đo. Kiểm bằng bảng ba đại lượng nhân hai engine; đạt khi cả sáu ô có số và lựa chọn dẫn được từ bảng.

**Điều kiện đạt.** Bảng ba đại lượng nhân hai engine đủ sáu ô, và lựa chọn cho hai tình huống dẫn được từ số trong bảng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** So hai engine chỉ bằng thông lượng · bỏ qua khuếch đại dung lượng · đo trong lúc gộp tệp đang chạy nên số bị lệch · kết luận một engine tốt hơn mà không nêu khối lượng công việc.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/24-read-write-and-space-amplification.md`
- Nội dung học thuật: `note.md` cùng thư mục.
