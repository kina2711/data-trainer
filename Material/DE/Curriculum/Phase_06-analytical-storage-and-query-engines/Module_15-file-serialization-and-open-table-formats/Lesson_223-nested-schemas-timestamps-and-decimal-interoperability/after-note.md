# Phase 6: Analytical Storage and Query Engines
# Module 15: File, Serialization and Open Table Formats
# Lesson 223: Nested Timestamp and Decimal Interoperability

## Thực hành

**Nhiệm vụ.** Ghi một bảng có cấu trúc lồng nhau, dấu thời gian ở hai độ phân giải, và cột tiền tệ dạng số thập phân. Đọc bằng ít nhất hai engine và so từng giá trị chứ so tổng. Chỉ ra chỗ lệch, chẩn đoán, và chặn bằng cách cố định biểu diễn ở bên ghi. Đưa phép thử vòng tròn vào chạy tự động.

Chỉ dùng fixture tổng hợp và môi trường cô lập. Lưu input/schema hashes, versions, commands, metadata, plans, counters, outputs, logs và limitations.

## Kiểm tra cuối bài

1. Nêu identity và granularity trung tâm.
2. Đưa một counterexample làm metadata/plan bị hiểu quá mức.
3. Phân biệt semantic correctness với performance evidence.
4. Nêu một reversal condition cho thiết kế.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi phát hiện một lệch không báo lỗi giữa hai hệ. Kiểm bằng phép thử vòng tròn; đạt khi phát hiện ít nhất một chỗ lệch, chẩn đoán đúng nguyên nhân, và chặn bằng một ràng buộc ở bên ghi.

**Điều kiện đạt.** Ít nhất một chỗ lệch được phát hiện và chẩn đoán đúng, và phép thử vòng tròn chạy tự động.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** So bằng tổng nên lệch làm tròn bị che · để độ phân giải dấu thời gian do giá trị mặc định quyết · dùng số dấu chấm động cho tiền tệ · kiểm vòng tròn một lần rồi coi như xong.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/111-nested-timestamp-decimal-interoperability.md`
- Nội dung học thuật: `note.md` cùng thư mục.
