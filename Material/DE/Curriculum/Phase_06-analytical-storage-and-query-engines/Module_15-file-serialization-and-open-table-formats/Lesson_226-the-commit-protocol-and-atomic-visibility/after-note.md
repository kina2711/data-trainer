# Phase 6: Analytical Storage and Query Engines
# Module 15: File, Serialization and Open Table Formats
# Lesson 226: Iceberg Commit Protocol and Atomic Visibility

## Thực hành

**Nhiệm vụ.** Ghi một lô dữ liệu và dừng tiến trình sau bước hai nhưng trước bước ba. Đếm tệp trên kho đối tượng và đếm dòng bảng thấy được; chứng minh hai số không khớp và bảng vẫn đúng. Xác định đúng tập tệp mồ côi bằng cách đối chiếu với kê khai. Chạy du hành thời gian về ảnh chụp trước đó và đối soát.

Chỉ dùng fixture tổng hợp và môi trường cô lập. Lưu input/schema hashes, versions, commands, metadata, plans, counters, outputs, logs và limitations.

## Kiểm tra cuối bài

1. Nêu publication hoặc identity boundary.
2. Đưa failure/counterexample có thể tái hiện.
3. Phân biệt format guarantee với implementation observation.
4. Nêu reconciliation oracle và reversal condition.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu bằng một thí nghiệm hỏng có chủ ý. Kiểm bằng thí nghiệm dừng giữa chừng; đạt khi bên đọc không thấy dòng nào của lần ghi hỏng và tệp mồ côi được xác định đúng.

**Điều kiện đạt.** Bên đọc không thấy dòng nào của lần ghi hỏng, tập tệp mồ côi được xác định đúng bằng đối chiếu kê khai, và du hành thời gian đối soát khớp.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Xoá tệp lạ trên kho đối tượng bằng tay · cho rằng tệp đã ghi là đã thuộc bảng · dọn tệp mồ côi ngay mà không chờ hết thời hạn giữ · nhầm du hành thời gian với sao lưu.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/114-iceberg-commit-protocol-atomic-visibility.md`
- Nội dung học thuật: `note.md` cùng thư mục.
