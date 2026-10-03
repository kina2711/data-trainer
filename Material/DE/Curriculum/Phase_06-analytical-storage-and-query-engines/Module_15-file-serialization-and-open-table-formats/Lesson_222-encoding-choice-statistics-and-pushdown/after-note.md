# Phase 6: Analytical Storage and Query Engines
# Module 15: File, Serialization and Open Table Formats
# Lesson 222: Parquet Statistics and Pushdown Evidence

## Thực hành

**Nhiệm vụ.** Ghi bảng với bốn cấu hình: không sắp xếp, sắp theo cột lọc, có chỉ mục trang, và cả hai. Chạy truy vấn chọn ít cột kèm điều kiện lọc hẹp. Với mỗi cấu hình, đo byte đọc khi chỉ bật đẩy cột, khi chỉ bật đẩy điều kiện, và khi bật cả hai. Chứng minh phần đóng góp cộng lại xấp xỉ phép đo đầy đủ.

Chỉ dùng fixture tổng hợp và môi trường cô lập. Lưu input/schema hashes, versions, commands, metadata, plans, counters, outputs, logs và limitations.

## Kiểm tra cuối bài

1. Nêu identity và granularity trung tâm.
2. Đưa một counterexample làm metadata/plan bị hiểu quá mức.
3. Phân biệt semantic correctness với performance evidence.
4. Nêu một reversal condition cho thiết kế.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective đòi tách hai cơ chế thường bị gộp. Kiểm bằng bốn cấu hình đo song song; đạt khi phần đóng góp của mỗi cơ chế được tách riêng và tổng khớp phép đo đầy đủ.

**Điều kiện đạt.** Phần đóng góp của hai cơ chế được tách riêng ở cả bốn cấu hình, và tổng khớp phép đo đầy đủ trong sai số thoả thuận.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Gộp hai cơ chế đẩy xuống thành một số đo · sắp xếp theo cột không dùng để lọc · tin thống kê tồn tại là cắt tỉa hoạt động · ghi cột phân bố rải đều rồi mong cắt tỉa.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/110-parquet-statistics-pushdown-evidence.md`
- Nội dung học thuật: `note.md` cùng thư mục.
