# Phase 4: SQL and Database Internals
# Module 10: Storage Engine and Database Operations
# Lesson 133: Pages, heap files and the buffer pool

## Thực hành

**Nhiệm vụ.** Dùng công cụ khảo sát trang của PostgreSQL để xem một trang thật: phần đầu, con trỏ dòng, và dữ liệu. Chèn thêm dòng và quan sát trang đổi. Đo tỉ lệ trúng hồ đệm cho một truy vấn ở hai trạng thái đệm nguội và đệm ấm. Giải thích vì sao đo lần hai luôn nhanh hơn.

Lưu SQL, dữ liệu sinh, tham số, dự đoán trước khi chạy, plan dạng máy đọc được, output thô, đối soát và thông số môi trường. Chỉ chạy `EXPLAIN ANALYZE`, DML, tải dữ liệu, thao tác cache, `pageinspect` hoặc extension trong PostgreSQL thử nghiệm cô lập; không dùng production để tạo cold cache hay benchmark. Ảnh chụp không thay artifact tái chạy.

## Kiểm tra cuối bài

1. Ba vùng chính của một heap page PostgreSQL là gì?
2. FSM và VM nằm ở đâu so với main fork?
3. Shared read khác physical storage read thế nào?
4. Vì sao buffer hit ratio không thể đứng một mình làm chỉ số hiệu năng?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài mở module, nối kiến thức lưu trữ ở M4 với cấu trúc bên trong cơ sở dữ liệu. Kiểm bằng bài khảo sát trang thật cộng bài giải thích; đạt khi đọc đúng ba thành phần của trang và giải thích đúng hai tầng đệm.

**Điều kiện đạt.** Đọc đúng ba thành phần của một trang thật, và giải thích đúng hai tầng đệm kèm số đo tỉ lệ trúng ở hai trạng thái.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Nghĩ cơ sở dữ liệu đọc theo dòng · nhầm hồ đệm với bộ đệm trang hệ điều hành · đo hiệu năng trên đệm ấm rồi kết luận · bỏ qua tỉ lệ trúng hồ đệm.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/21-pages-heap-files-and-buffer-pool.md`
- Nội dung học thuật: `note.md` cùng thư mục.
