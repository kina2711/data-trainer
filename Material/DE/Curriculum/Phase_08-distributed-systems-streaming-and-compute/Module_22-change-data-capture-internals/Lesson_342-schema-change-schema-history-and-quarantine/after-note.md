# Phase 8: Distributed Systems, Streaming and Compute
# Module 22: Change Data Capture Internals
# Lesson 342: Schema change, schema history and quarantine

## Thực hành

**Nhiệm vụ.** Chạy dòng liên tục rồi thực hiện ba thay đổi lược đồ ở nguồn. Với mỗi cái, ghi lại phản ứng của trình kết nối và của bên tiêu thụ. Sau khi đổi xong, đọc lại toàn bộ chủ đề từ đầu và xác nhận dữ liệu cũ giải mã đúng nhờ lịch sử lược đồ. Tạo một sự kiện không giải mã được, xác nhận nó vào vùng cách ly, sửa rồi phát lại.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là đọc lại dữ liệu cũ vẫn đúng sau khi lược đồ đã đổi. Kiểm bằng phép đọc lại; đạt khi dữ liệu trước thay đổi được giải mã đúng, không sự kiện nào bị bỏ im lặng, và sự kiện cách ly phát lại được.

**Điều kiện đạt.** Dữ liệu trước thay đổi giải mã đúng khi đọc lại, không sự kiện nào bị bỏ im lặng, và sự kiện cách ly được phát lại thành công.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Xoá lịch sử lược đồ để dọn dẹp · để sự kiện không giải mã được bị bỏ qua · đổi lược đồ nguồn mà không báo bên tiêu thụ · triển khai sai thứ tự so với mức tương thích.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/230-schema-change-schema-history-and-quarantine.md`
- Nội dung học thuật: `note.md` cùng thư mục.
