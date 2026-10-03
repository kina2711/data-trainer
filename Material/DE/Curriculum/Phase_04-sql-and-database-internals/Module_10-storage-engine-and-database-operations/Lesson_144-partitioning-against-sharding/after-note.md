# Phase 4: SQL and Database Internals
# Module 10: Storage Engine and Database Operations
# Lesson 144: Partitioning against sharding

## Thực hành

**Nhiệm vụ.** Phân vùng một bảng 50 triệu dòng theo tháng. Đo chênh lệch byte quét giữa truy vấn có và không có điều kiện trên khoá phân vùng. Xoá một tháng bằng thao tác phân vùng và so thời gian với lệnh xoá thường. Cho ba tình huống và quyết định phân vùng hay phân mảnh.

Chỉ thực hiện trên database/cluster thử nghiệm cô lập, có seed và đường khôi phục. Không giữ lock dài, ép vacuum, đổi isolation/durability, kill node, promote hay rebalance trên production. Lưu script, cấu hình, operation-ID ledger, raw counters và log; ảnh chụp không thay artifact tái chạy.

## Kiểm tra cuối bài

1. Nêu contract và failure boundary của cơ chế.
2. Dựng schedule hoặc topology nhỏ nhất tái hiện lỗi.
3. Chọn ba chỉ số phân biệt triệu chứng với nguyên nhân.
4. Nêu một phát biểu chỉ đúng cho PostgreSQL và nguồn kiểm.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi phân biệt hai kỹ thuật và chống việc phân mảnh quá sớm. Kiểm bằng ba tình huống trong đó ít nhất hai chỉ cần phân vùng; đạt khi chọn đúng cả ba và nêu đúng khoá chia.

**Điều kiện đạt.** Có số đo chênh lệch byte quét khi cắt phân vùng, và ba tình huống được quyết định đúng kèm khoá chia.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Phân mảnh khi phân vùng đủ · chọn khoá phân vùng không xuất hiện trong điều kiện lọc · thiết kế để mọi truy vấn phải hỏi mọi mảnh · bỏ qua chi phí cân bằng lại.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/32-partitioning-versus-sharding.md`
- Nội dung học thuật: `note.md` cùng thư mục.
