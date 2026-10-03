# Phase 6: Analytical Storage and Query Engines
# Module 15: File, Serialization and Open Table Formats
# Lesson 225: Iceberg Metadata Tree and Snapshot Lineage

## Thực hành

**Nhiệm vụ.** Dựng một bảng và ghi ba lần. Mở tệp siêu dữ liệu, danh sách kê khai và kê khai của từng ảnh chụp, ghi lại nội dung. Chọn một dòng dữ liệu và truy ngược về tệp dữ liệu, kê khai, ảnh chụp. Chạy truy vấn có lọc theo phân vùng và chỉ ra bao nhiêu tệp bị loại ở tầng kê khai trước khi mở tệp nào.

Chỉ dùng fixture tổng hợp và môi trường cô lập. Lưu input/schema hashes, versions, commands, metadata, plans, counters, outputs, logs và limitations.

## Kiểm tra cuối bài

1. Nêu identity và granularity trung tâm.
2. Đưa một counterexample làm metadata/plan bị hiểu quá mức.
3. Phân biệt semantic correctness với performance evidence.
4. Nêu một reversal condition cho thiết kế.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi đọc cấu trúc thật thay vì mô tả nó. Kiểm bằng bài truy ngược; đạt khi truy đúng đường từ dòng dữ liệu về ảnh chụp và giải thích đúng nơi cắt tỉa siêu dữ liệu xảy ra.

**Điều kiện đạt.** Truy đúng đường từ một dòng dữ liệu về ảnh chụp qua đủ bốn tầng, và số tệp bị loại ở tầng kê khai được đo.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Học cấu trúc qua sơ đồ mà không mở tệp thật · nhầm ảnh chụp với phiên bản lược đồ · bỏ qua vai trò của danh mục · không đo số tệp bị loại ở tầng siêu dữ liệu.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/113-iceberg-metadata-tree-snapshot-lineage.md`
- Nội dung học thuật: `note.md` cùng thư mục.
