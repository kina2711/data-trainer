# Phase 4: SQL and Database Internals
# Module 10: Storage Engine and Database Operations
# Lesson 148: Gate 4 - trace a write and defend an isolation choice

## Thực hành

**Nhiệm vụ.** Buổi 120 phút: 75 phút làm bài độc lập, 45 phút chữa bài. Bài chấm sáu phần: A (20đ) truy đường đi của một lệnh chèn từ câu lệnh tới nhật ký ghi trước, tới trang, tới điểm kiểm tra và tới khôi phục · B (20đ) tối ưu hai truy vấn chậm, mỗi tối ưu dẫn về một quan sát trong kế hoạch và kết quả khớp tuyệt đối · C (20đ) chọn mức cô lập cho hai bất biến cho trước và chứng minh bằng phép kiểm chạy song song · D (20đ) khôi phục về một mốc thời gian và đối soát khớp · E (10đ) chẩn đoán một hệ đang bị chặn bằng khung nhìn khoá · F (10đ) nêu ba chỉ số vận hành phải theo dõi và ngưỡng dẫn từ phân bố.

Chỉ chạy backup/restore, fault injection, lock workload hoặc schema experiment trong môi trường cô lập có dữ liệu giả và đường xoá/khôi phục rõ. Không restore đè, đổi retention, kill process hoặc chạy destructive command trên production. Lưu exact version, config, script, raw log, operation ledger và kết quả đối soát.

## Kiểm tra cuối bài

1. Nêu contract và failure boundary chính.
2. Thiết kế phép kiểm có đối chứng và artifact tái chạy.
3. Chỉ ra một phát biểu phụ thuộc PostgreSQL hoặc phương pháp modeling.
4. Nêu stop condition bảo vệ dữ liệu và môi trường.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Cổng đo năng lực tổng hợp gồm cả một thao tác vận hành có rủi ro thật, nên hình thức là bài làm cộng diễn tập.

**Điều kiện đạt.** Đạt ≥ 70/100, phần C và D đều ≥ 60%. Bất biến chỉ chứng minh bằng phép chạy tuần tự thì phần C bằng không; khôi phục không đối soát thì phần D bằng không.

## Bài làm sau buổi học

**Nhiệm vụ.** Không có bài tự học. Nếu không đạt, theo phụ lục khắc phục khi không đạt cổng

**Lỗi cần chủ động loại trừ.** Chọn mức cô lập theo tên · tối ưu làm đổi kết quả · bỏ phần khôi phục vì tốn thời gian · chứng minh bất biến bằng phép chạy tuần tự.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/36-gate-4-write-trace-isolation-and-recovery.md`
- Nội dung học thuật: `note.md` cùng thư mục.
