# Phase 6: Analytical Storage and Query Engines
# Module 15: File, Serialization and Open Table Formats
# Lesson 220: Four Cell Schema Compatibility Gate

## Thực hành

**Nhiệm vụ.** Dựng bộ bản ghi vàng cho một hợp đồng. Viết bộ kiểm chạy đủ bốn ô ma trận trên ba phiên bản lược đồ. Đưa vào tích hợp liên tục có cửa chặn. Tiêm ba thay đổi phá vỡ khác loại và xác nhận cả ba bị chặn kèm thông báo chỉ rõ ô nào hỏng. Chọn mức tương thích cho hợp đồng và nêu thứ tự triển khai kéo theo.

Chỉ dùng fixture tổng hợp và môi trường cô lập. Lưu schema/source hashes, versions, commands, raw bytes, outputs, logs và limitations.

## Kiểm tra cuối bài

1. Nêu identity và compatibility boundary trung tâm.
2. Đưa một ca parse sạch nhưng sai nghĩa.
3. Nêu counterexample đảo quyết định.
4. Phân biệt configured intent với observed evidence.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một cửa chặn tự động có tiêu chí nghiệm thu bằng phép thử tiêm. Kiểm bằng ba thay đổi phá vỡ tiêm; đạt khi cả ba bị chặn và mỗi ô của ma trận có kết quả rõ.

**Điều kiện đạt.** Ba thay đổi phá vỡ đều bị chặn kèm thông báo chỉ đúng ô hỏng, và mức tương thích chọn kèm thứ tự triển khai.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chỉ kiểm ô bên ghi mới với bên đọc mới · không có bản ghi vàng nên mỗi lần kiểm một bộ dữ liệu khác · chọn mức tương thích mà không suy ra thứ tự triển khai · để sổ đăng ký ở chế độ không cưỡng chế.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/108-four-cell-schema-compatibility-gate.md`
- Nội dung học thuật: `note.md` cùng thư mục.
