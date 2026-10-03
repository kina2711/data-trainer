# Phase 4: SQL and Database Internals
# Module 9: Relational Theory and SQL Execution
# Lesson 118: Logical query processing order

## Thực hành

**Nhiệm vụ.** Cho tám truy vấn: bốn cái lỗi cú pháp, bốn cái chạy được nhưng sai nghĩa do đặt điều kiện sai bước. Với mỗi cái, chỉ ra bước nào gây ra và sửa. Với hai truy vấn, chứng minh đặt điều kiện ở bước lọc dòng và bước lọc nhóm cho hai kết quả khác nhau.

Lưu SQL, seed data, prediction trước khi chạy, output thô, đối soát và giải thích theo rule. Ảnh chụp không thay artifact chạy lại được.

## Kiểm tra cuối bài

1. Alias tồn tại ở bước nào?
2. WHERE khác HAVING thế nào?
3. Window filter cần query level nào?
4. Logical khác physical order ra sao?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài lý thuyết nền cho toàn phần ngôn ngữ; chưa đòi tối ưu. Kiểm bằng tám truy vấn có lỗi; đạt khi giải thích đúng ít nhất sáu bằng thứ tự xử lý chứ bằng kinh nghiệm.

**Điều kiện đạt.** Giải thích đúng ≥ 6/8 truy vấn bằng thứ tự xử lý, và chứng minh được hai kết quả khác nhau khi đặt điều kiện sai bước.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dùng bí danh trong mệnh đề lọc dòng · đặt điều kiện lọc dòng vào mệnh đề lọc nhóm · tin thứ tự viết là thứ tự chạy · lồng hàm cửa sổ vào điều kiện lọc.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/06-logical-query-processing-order.md`
- Nội dung học thuật: `note.md` cùng thư mục.
