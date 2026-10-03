# Phase 4: SQL and Database Internals
# Module 10: Storage Engine and Database Operations
# Lesson 137: The write-ahead log and group commit

## Thực hành

**Nhiệm vụ.** Chạy tải ghi ở ba cấu hình bền vững khác nhau, đo thông lượng và độ trễ phân vị 95 cho từng cái. Giết tiến trình cơ sở dữ liệu cứng giữa lúc ghi và đếm số giao dịch đã chốt còn lại ở mỗi cấu hình. Quan sát tệp nhật ký lớn lên và điểm kiểm tra làm nó được tái sử dụng.

Chỉ chạy workload, compaction, cấu hình WAL/checkpoint hoặc crash injection trong instance thử nghiệm cô lập có seed/snapshot khôi phục. Không tắt `fsync`, phá cache, kill hoặc ép compaction trên production. Lưu config, raw counters, client operation-ID ledger và log; ảnh chụp không thay artifact tái chạy.

## Kiểm tra cuối bài

1. Hai write-ahead rules là gì?
2. Group commit đổi throughput/latency ra sao?
3. Async commit khác fsync off thế nào?
4. ACK ledger dùng để kiểm điều gì?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective nối một tham số cấu hình với một cam kết ngữ nghĩa và một con số. Kiểm bằng bảng ba mức cộng thí nghiệm mất điện; đạt khi ba cam kết phát biểu đúng và số đo đúng chiều.

**Điều kiện đạt.** Bảng ba cấu hình có cả thông lượng lẫn độ trễ, số giao dịch sống sót đúng với cam kết đã phát biểu ở cả ba mức.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Tắt cam kết bền vững trên hệ sản xuất để tăng tốc · nghĩ chốt theo nhóm làm giảm độ trễ · không thử giết tiến trình nên không biết cam kết thật · bỏ qua quan hệ giữa nhật ký và nhân bản.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/25-write-ahead-log-and-group-commit.md`
- Nội dung học thuật: `note.md` cùng thư mục.
