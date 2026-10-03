# Phase 4: SQL and Database Internals
# Module 10: Storage Engine and Database Operations
# Lesson 145: Backup, PITR and what a backup is not

## Thực hành

**Nhiệm vụ.** Phỏng vấn một người đóng vai nghiệp vụ để chốt hai mục tiêu. Từ đó suy ra tần suất sao lưu đầy đủ, tần suất lưu nhật ký, và thời gian giữ. Lập danh mục mọi thứ phải sao lưu ngoài dữ liệu. Ước lượng dung lượng và chi phí lưu trữ cho ba tháng.

Chỉ chạy backup/restore, fault injection, lock workload hoặc schema experiment trong môi trường cô lập có dữ liệu giả và đường xoá/khôi phục rõ. Không restore đè, đổi retention, kill process hoặc chạy destructive command trên production. Lưu exact version, config, script, raw log, operation ledger và kết quả đối soát.

## Kiểm tra cuối bài

1. Nêu contract và failure boundary chính.
2. Thiết kế phép kiểm có đối chứng và artifact tái chạy.
3. Chỉ ra một phát biểu phụ thuộc PostgreSQL hoặc phương pháp modeling.
4. Nêu stop condition bảo vệ dữ liệu và môi trường.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài lý thuyết chuẩn bị cho buổi diễn tập ở lesson 146. Kiểm bằng bản kế hoạch; đạt khi hai mục tiêu được nối với tần suất sao lưu cụ thể và nêu đủ bốn thứ hay quên.

**Điều kiện đạt.** Hai mục tiêu được nối với tần suất cụ thể, danh mục nêu đủ bốn thứ ngoài dữ liệu, và có ước lượng dung lượng ba tháng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Kỹ thuật tự đặt hai mục tiêu · chỉ sao lưu dữ liệu mà quên cấu hình và bí mật · đặt thời gian giữ nhật ký ngắn hơn khoảng cách giữa hai lần sao lưu đầy đủ · chưa từng tính dung lượng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/33-backup-pitr-and-what-a-backup-is-not.md`
- Nội dung học thuật: `note.md` cùng thư mục.
