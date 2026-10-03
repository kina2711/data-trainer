# Phase 4: SQL and Database Internals
# Module 9: Relational Theory and SQL Execution
# Lesson 113: Relations, keys and functional dependencies

## Thực hành

**Nhiệm vụ.** Cho ba bảng có dữ liệu mẫu. Với mỗi bảng, tìm khoá dự tuyển bằng cách kiểm tính duy nhất trên dữ liệu thật, viết các phụ thuộc hàm quan sát được, và đề xuất ràng buộc. Thêm một đường ghi thứ hai bỏ qua ứng dụng và chứng minh ràng buộc ở cơ sở dữ liệu vẫn chặn được.

Bài làm phải lưu lệnh tái hiện, dữ liệu đầu vào, đầu ra thô và assertion của invariant. Mọi kết luận phải chỉ được evidence ID tương ứng; ảnh chụp không thay artifact chạy lại được.

## Kiểm tra cuối bài

1. Vì sao sample không duplicate không chứng minh candidate key?
2. Phân biệt superkey, candidate key và primary key.
3. Tính attribute closure dùng để làm gì?
4. Vì sao application validation không thay database constraint?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài mở module, đặt từ vựng cho toàn phần nền. Kiểm bằng bài phân tích ba bảng; đạt khi tìm đúng khoá dự tuyển ở ít nhất hai và nêu đúng ràng buộc nên đặt ở tầng cơ sở dữ liệu.

**Điều kiện đạt.** Tìm đúng khoá dự tuyển ở ≥ 2/3 bảng, và chứng minh được ràng buộc ở cơ sở dữ liệu chặn đường ghi thứ hai.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Coi bảng như bảng tính có thứ tự · chọn khoá chính là một cột tăng tự động mà không xác định khoá tự nhiên · để mọi ràng buộc ở tầng ứng dụng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/01-relations-keys-functional-dependencies.md`
- Nội dung học thuật: `note.md` cùng thư mục.
