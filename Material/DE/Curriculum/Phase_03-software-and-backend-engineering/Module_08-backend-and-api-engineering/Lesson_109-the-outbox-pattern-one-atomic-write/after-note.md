# Phase 3: Software and Backend Engineering
# Module 8: Backend and API Engineering
# Lesson 109: The outbox pattern - one atomic write

## Thực hành

**Nhiệm vụ.** Cài bản ngây thơ ghi cơ sở dữ liệu rồi phát sự kiện, giết tiến trình giữa hai thao tác 20 lần và đếm mức lệch. Cài lại bằng hộp thư đi và lặp thí nghiệm. Xử lý trường hợp phát thành công nhưng đánh dấu thất bại. Thêm việc dọn bảng hộp thư theo lịch.

Bài làm phải lưu lệnh tái hiện, dữ liệu đầu vào, đầu ra thô và assertion của invariant. Mọi kết luận phải chỉ được evidence ID tương ứng; ảnh chụp không thay artifact chạy lại được.

## Kiểm tra cuối bài

1. Failure window nào được outbox loại bỏ, failure window nào vẫn còn?
2. Vì sao published-but-not-marked tạo duplicate hợp lệ?
3. Thiết kế cleanup thế nào để không xoá pending row?
4. Bằng chứng nào cho phép và không cho phép dùng cụm từ exactly-once?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *sáng tạo*. Objective đòi ghép giao dịch với một tiến trình phát riêng thành một mẫu giải bài toán hai hệ. Kiểm bằng 20 lần giết tiến trình; đạt khi số sự kiện phát ra khớp số bản ghi tạo ra, không thiếu.

**Điều kiện đạt.** Bản ngây thơ có mức lệch đo được, bản hộp thư đi không thiếu sự kiện nào qua 20 lần giết, và bảng hộp thư được dọn tự động.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Ghi hai hệ trong hai thao tác rời · dùng giao dịch phân tán khi hộp thư đi đủ · quên dọn bảng hộp thư · giả định bên nhận không bao giờ nhận trùng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-SOFTWARE-DESIGN-BOOK-01/21-transactional-outbox-one-atomic-write.md`
- Nội dung học thuật: `note.md` cùng thư mục.
