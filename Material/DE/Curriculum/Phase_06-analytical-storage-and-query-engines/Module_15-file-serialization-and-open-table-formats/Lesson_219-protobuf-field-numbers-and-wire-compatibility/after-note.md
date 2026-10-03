# Phase 6: Analytical Storage and Query Engines
# Module 15: File, Serialization and Open Table Formats
# Lesson 219: Protobuf Field Numbers and Wire Compatibility

## Thực hành

**Nhiệm vụ.** Định nghĩa hợp đồng sự kiện. Thực hiện bốn thay đổi gồm đổi tên, thêm trường, bỏ trường có đặt chỗ, và bỏ trường không đặt chỗ rồi dùng lại số hiệu. Mã hoá bằng phiên bản cũ và giải mã bằng phiên bản mới cùng chiều ngược lại. Chỉ ra ca dùng lại số hiệu cho giá trị bị diễn giải sai mà không báo lỗi.

Chỉ dùng fixture tổng hợp và môi trường cô lập. Lưu schema/source hashes, versions, commands, raw bytes, outputs, logs và limitations.

## Kiểm tra cuối bài

1. Nêu identity và compatibility boundary trung tâm.
2. Đưa một ca parse sạch nhưng sai nghĩa.
3. Nêu counterexample đảo quyết định.
4. Phân biệt configured intent với observed evidence.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có một ca hỏng đặc trưng cần tái hiện bằng dữ liệu thật. Kiểm bằng bốn thay đổi cộng ca dùng lại số hiệu; đạt khi dự đoán đúng cả bốn và ca dùng lại số hiệu cho thấy dữ liệu bị diễn giải sai.

**Điều kiện đạt.** Dự đoán đúng cả bốn thay đổi, và ca dùng lại số hiệu cho thấy giá trị bị diễn giải sai mà không có lỗi.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dùng lại số hiệu trường đã bỏ · giả định đổi tên là thay đổi phá vỡ như ở định dạng trước · bỏ qua hành vi của bên trung gian với trường không nhận ra · chỉ kiểm một chiều tương thích.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/107-protobuf-field-numbers-wire-compatibility.md`
- Nội dung học thuật: `note.md` cùng thư mục.
