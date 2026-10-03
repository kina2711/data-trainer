# Phase 4: SQL and Database Internals
# Module 9: Relational Theory and SQL Execution
# Lesson 132: SQL tuning project - five slow queries

## Thực hành

**Nhiệm vụ.** Nhận năm truy vấn chậm. Với mỗi cái, nộp kế hoạch trước và sau, bốn con số, và câu dẫn chứng. Đối soát kết quả từng truy vấn với bản gốc. Rà soát chéo: một học viên khác chọn một tối ưu bất kỳ và bạn phải chỉ ra quan sát dẫn tới nó.

Lưu SQL, dữ liệu sinh, tham số, dự đoán trước khi chạy, plan dạng máy đọc được, output thô, đối soát và thông số môi trường. Chỉ chạy `EXPLAIN ANALYZE`, DML, tải dữ liệu, thao tác cache, `pageinspect` hoặc extension trong PostgreSQL thử nghiệm cô lập; không dùng production để tạo cold cache hay benchmark. Ảnh chụp không thay artifact tái chạy.

## Kiểm tra cuối bài

1. Vì sao bằng nhau về row count chưa chứng minh result parity?
2. Một tuning dossier tối thiểu cần những artifacts nào?
3. One-variable discipline giúp thiết lập quan hệ nhân quả ra sao?
4. Khi nào một cải thiện trên staging chưa đủ để rollout production?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module thành một quy trình tối ưu có bằng chứng. Kiểm bằng bảng trước sau cộng đối soát kết quả; đạt khi ít nhất bốn truy vấn đạt ngưỡng và mọi kết quả khớp tuyệt đối.

**Điều kiện đạt.** ≥ 4/5 truy vấn đạt ngưỡng, mọi kết quả khớp tuyệt đối với bản gốc, và mọi tối ưu dẫn được về một quan sát trong kế hoạch.

## Bài làm sau buổi học

**Nhiệm vụ.** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Lỗi cần chủ động loại trừ.** Thêm chỉ mục cho mọi truy vấn · sửa nhiều thứ cùng lúc · tối ưu làm đổi kết quả · nộp số mà không nộp kế hoạch.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/20-sql-tuning-project-five-slow-queries.md`
- Nội dung học thuật: `note.md` cùng thư mục.
