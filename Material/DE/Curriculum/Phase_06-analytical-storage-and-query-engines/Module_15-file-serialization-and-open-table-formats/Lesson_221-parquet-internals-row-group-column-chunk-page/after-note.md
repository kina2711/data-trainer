# Phase 6: Analytical Storage and Query Engines
# Module 15: File, Serialization and Open Table Formats
# Lesson 221: Parquet File Row Group Column Chunk and Page

## Thực hành

**Nhiệm vụ.** Ghi cùng dữ liệu với ba kích thước nhóm hàng. Đọc siêu dữ liệu chân tệp của cả ba và ghi lại số nhóm hàng, kích thước khối cột và thống kê. Chạy bộ truy vấn và đo byte đọc, số nhóm hàng bị cắt, bộ nhớ đỉnh. Chọn kích thước cho khối lượng công việc và dẫn từ ba số đo.

Chỉ dùng fixture tổng hợp và môi trường cô lập. Lưu input/schema hashes, versions, commands, metadata, plans, counters, outputs, logs và limitations.

## Kiểm tra cuối bài

1. Nêu identity và granularity trung tâm.
2. Đưa một counterexample làm metadata/plan bị hiểu quá mức.
3. Phân biệt semantic correctness với performance evidence.
4. Nêu một reversal condition cho thiết kế.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi nối cấu trúc tệp với số đo hiệu năng. Kiểm bằng ba kích thước nhóm hàng đo song song; đạt khi ba đánh đổi đều có số và lựa chọn dẫn được từ số đó.

**Điều kiện đạt.** Siêu dữ liệu chân tệp của ba phương án được đọc và ghi lại, và lựa chọn kích thước nhóm hàng dẫn được từ ba số đo.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Nhầm đơn vị cắt tỉa với đơn vị đọc · đặt kích thước nhóm hàng theo giá trị mặc định mà không đo · sinh nhóm hàng rất nhỏ rồi ngạc nhiên vì siêu dữ liệu phình · không bao giờ đọc chân tệp thật.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/109-parquet-file-row-group-column-chunk-page.md`
- Nội dung học thuật: `note.md` cùng thư mục.
