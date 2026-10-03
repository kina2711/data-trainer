# Phase 6: Analytical Storage and Query Engines
# Module 15: File, Serialization and Open Table Formats
# Lesson 230: Gate 6 Metadata Concurrency Compatibility and Engine Evidence

## Thực hành

**Nhiệm vụ.** Buổi 150 phút: 105 phút làm bài độc lập, 45 phút chữa bài. Bài chấm sáu phần: A (20đ) tách bốn phần đóng góp làm hệ cột nhanh, mỗi phần một số đo riêng · B (15đ) chẩn đoán một truy vấn phân tán chậm, phân biệt lệch tải với tràn đĩa với hàng đợi · C (20đ) đọc chuỗi siêu dữ liệu thật và truy một dòng dữ liệu về ảnh chụp · D (20đ) chạy hai bên ghi đồng thời, chỉ ra thao tác nào thất bại và vì sao, chứng minh không mất thay đổi · E (15đ) ma trận tương thích bốn ô cho một thay đổi lược đồ · F (10đ) khuyến nghị engine cho một khối lượng công việc, mọi luận điểm gắn số đo.

Chỉ dùng fixture tổng hợp và môi trường cô lập. Lưu input/schema hashes, versions, commands, metadata, plans, counters, outputs, logs và limitations.

## Kiểm tra cuối bài

1. Nêu publication hoặc identity boundary.
2. Đưa failure/counterexample có thể tái hiện.
3. Phân biệt format guarantee với implementation observation.
4. Nêu reconciliation oracle và reversal condition.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Cổng đo năng lực giải thích cơ chế và vận hành an toàn, nên hình thức là thực hành tại chỗ cộng bảo vệ.

**Điều kiện đạt.** Đạt ≥ 70/100, phần C và D đều ≥ 60%. Xoá tệp dữ liệu bằng tay trong phần D thì phần đó bằng không; khuyến nghị engine không có số đo thì phần F bằng không.

## Bài làm sau buổi học

**Nhiệm vụ.** Không có bài tự học. Nếu không đạt, theo phụ lục khắc phục khi không đạt cổng

**Lỗi cần chủ động loại trừ.** Dùng chữ ACID thay cho mô tả giao thức chốt · so tốc độ giữa lần chạy nóng và lần chạy lạnh · thử lại mọi xung đột ghi · chọn engine bằng danh sách tính năng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/118-gate-6-metadata-concurrency-compatibility-engine-evidence.md`
- Nội dung học thuật: `note.md` cùng thư mục.
