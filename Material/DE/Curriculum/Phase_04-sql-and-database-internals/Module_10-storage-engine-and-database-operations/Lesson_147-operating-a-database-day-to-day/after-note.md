# Phase 4: SQL and Database Internals
# Module 10: Storage Engine and Database Operations
# Lesson 147: Operating a database day to day

## Thực hành

**Nhiệm vụ.** Dựng theo dõi cho sáu việc. Đặt bốn cảnh báo tối thiểu với ngưỡng dẫn từ phân bố đo được chứ số tròn. Giảng viên tiêm bốn sự cố: cạn kết nối, phình bảng, thống kê cũ, và dung lượng tăng nhanh bất thường. Ghi cảnh báo nào phát hiện được và phát hiện trước bao lâu.

Chỉ chạy backup/restore, fault injection, lock workload hoặc schema experiment trong môi trường cô lập có dữ liệu giả và đường xoá/khôi phục rõ. Không restore đè, đổi retention, kill process hoặc chạy destructive command trên production. Lưu exact version, config, script, raw log, operation ledger và kết quả đối soát.

## Kiểm tra cuối bài

1. Nêu contract và failure boundary chính.
2. Thiết kế phép kiểm có đối chứng và artifact tái chạy.
3. Chỉ ra một phát biểu phụ thuộc PostgreSQL hoặc phương pháp modeling.
4. Nêu stop condition bảo vệ dữ liệu và môi trường.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một cấu hình vận hành kiểm được bằng việc phát hiện sự cố trước khi người dùng báo. Kiểm bằng bốn sự cố tiêm sẵn; đạt khi cảnh báo phát hiện ít nhất ba trước khi tác động tới truy vấn.

**Điều kiện đạt.** Cảnh báo phát hiện ≥ 3/4 sự cố trước khi tác động tới truy vấn, và mọi ngưỡng dẫn được từ phân bố đo được.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đặt ngưỡng bằng số tròn · theo dõi dung lượng hiện tại mà không theo dõi tốc độ tăng · không giới hạn số kết nối ở phía ứng dụng · nâng cấp lớn mà không có đường lùi.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/35-operating-a-database-day-to-day.md`
- Nội dung học thuật: `note.md` cùng thư mục.
