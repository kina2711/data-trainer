# Phase 6: Analytical Storage and Query Engines
# Module 15: File, Serialization and Open Table Formats
# Lesson 228: Iceberg Hidden Partition Schema and Field ID Evolution

## Thực hành

**Nhiệm vụ.** Dựng bảng phân vùng ẩn theo tháng, nạp dữ liệu. Đổi quy tắc phân vùng sang theo ngày và nạp tiếp, không ghi lại dữ liệu cũ. Chạy truy vấn phủ cả hai vùng và đối soát với bản tính tay. Đổi tên một cột và chứng minh truy vấn cũ theo tên mới vẫn đọc đúng dữ liệu cũ. Kiểm cắt tỉa còn hoạt động ở cả hai vùng.

Chỉ dùng fixture tổng hợp và môi trường cô lập. Lưu input/schema hashes, versions, commands, metadata, plans, counters, outputs, logs và limitations.

## Kiểm tra cuối bài

1. Nêu publication hoặc identity boundary.
2. Đưa failure/counterexample có thể tái hiện.
3. Phân biệt format guarantee với implementation observation.
4. Nêu reconciliation oracle và reversal condition.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là dữ liệu cũ và mới cùng đọc đúng sau khi đổi quy tắc. Kiểm bằng đối soát bắc qua ranh giới tiến hoá; đạt khi truy vấn phủ cả hai vùng cho kết quả khớp bản tính tay.

**Điều kiện đạt.** Truy vấn phủ cả hai vùng khớp bản tính tay, đổi tên cột không làm hỏng dữ liệu cũ, và cắt tỉa còn hoạt động ở cả hai vùng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Ghi lại toàn bộ dữ liệu cũ khi đổi quy tắc phân vùng · dùng bên đọc dựa theo tên cột · đổi quy tắc phân vùng mà không kiểm cắt tỉa ở vùng cũ · bỏ đối soát bắc qua ranh giới.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/116-iceberg-hidden-partition-schema-field-id-evolution.md`
- Nội dung học thuật: `note.md` cùng thư mục.
