# Phase 4: SQL and Database Internals
# Module 10: Storage Engine and Database Operations
# Lesson 135: LSM trees - memtable, SSTable and compaction

## Thực hành

**Nhiệm vụ.** Đọc cấu trúc thư mục dữ liệu của một kho dùng cấu trúc này: quan sát tệp đã sắp xếp, bộ lọc Bloom, và các mức gộp. Kích hoạt một lần gộp và quan sát tải vào ra. Viết dự đoán về ba đại lượng khuếch đại so với cây B trước khi đo ở bài sau.

Chỉ chạy workload, compaction, cấu hình WAL/checkpoint hoặc crash injection trong instance thử nghiệm cô lập có seed/snapshot khôi phục. Không tắt `fsync`, phá cache, kill hoặc ép compaction trên production. Lưu config, raw counters, client operation-ID ledger và log; ảnh chụp không thay artifact tái chạy.

## Kiểm tra cuối bài

1. Memtable cần WAL vì sao?
2. Flush phải giữ read-view invariants nào?
3. Tombstone được drop khi nào?
4. Compaction debt biểu hiện qua metrics nào?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài lý thuyết so sánh hai cấu trúc; phần đo nằm ở lesson 136. Kiểm bằng bài giải thích cộng dự đoán; đạt khi giải thích đúng cơ chế và dự đoán đúng chiều của ba đại lượng khuếch đại.

**Điều kiện đạt.** Giải thích đúng cơ chế biến ghi ngẫu nhiên thành ghi tuần tự, và dự đoán đúng chiều của cả ba đại lượng khuếch đại.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Nghĩ cấu trúc này luôn nhanh hơn · quên rằng xoá không giải phóng dung lượng ngay · bỏ qua tải nền do gộp tệp · dùng cho khối lượng đọc ngẫu nhiên nặng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/23-lsm-trees-memtable-sstable-and-compaction.md`
- Nội dung học thuật: `note.md` cùng thư mục.
