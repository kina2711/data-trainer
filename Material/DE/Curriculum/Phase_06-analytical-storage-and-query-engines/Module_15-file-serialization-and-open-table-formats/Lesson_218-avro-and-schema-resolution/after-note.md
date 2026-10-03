# Phase 6: Analytical Storage and Query Engines
# Module 15: File, Serialization and Open Table Formats
# Lesson 218: Avro Writer Reader Schema Resolution

## Thực hành

**Nhiệm vụ.** Định nghĩa lược đồ có đủ giá trị rỗng, mặc định, dấu thời gian và số thập phân. Thực hiện bốn thay đổi: thêm trường có mặc định, bỏ trường, đổi tên trường, và đổi kiểu. Với mỗi cái, dự đoán kết quả rồi kiểm. Tạo một thay đổi giải mã sạch nhưng đổi nghĩa và chỉ ra vì sao không có lỗi nào được báo.

Chỉ dùng fixture tổng hợp và môi trường cô lập. Lưu schema/source hashes, versions, commands, raw bytes, outputs, logs và limitations.

## Kiểm tra cuối bài

1. Nêu identity và compatibility boundary trung tâm.
2. Đưa một ca parse sạch nhưng sai nghĩa.
3. Nêu counterexample đảo quyết định.
4. Phân biệt configured intent với observed evidence.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective đòi phân biệt hai mức tương thích mà một mức không có thông báo lỗi. Kiểm bằng bốn thay đổi; đạt khi dự đoán đúng kết quả cả bốn và chỉ ra được ca giải mã sạch nhưng sai nghĩa.

**Điều kiện đạt.** Dự đoán đúng kết quả cả bốn thay đổi, và ca giải mã sạch nhưng sai nghĩa được chỉ ra kèm giải thích.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đổi tên trường mà không đặt bí danh · thêm trường bắt buộc không có mặc định · coi giải mã không lỗi là tương thích · kiểm tương thích chỉ theo một chiều.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/106-avro-writer-reader-schema-resolution.md`
- Nội dung học thuật: `note.md` cùng thư mục.
