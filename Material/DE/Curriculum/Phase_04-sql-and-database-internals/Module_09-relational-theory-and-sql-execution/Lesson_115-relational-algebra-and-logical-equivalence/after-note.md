# Phase 4: SQL and Database Internals
# Module 9: Relational Theory and SQL Execution
# Lesson 115: Relational algebra and logical equivalence

## Thực hành

**Nhiệm vụ.** Cho ba truy vấn viết kém. Với mỗi cái, viết lại theo một phép biến đổi tương đương, đối soát kết quả khớp tuyệt đối, và so chi phí. Với một truy vấn, viết hai cách khác nhau về hình thức và chứng minh bộ tối ưu cho cùng kế hoạch.

Lưu SQL, seed data, prediction trước khi chạy, output thô, đối soát và giải thích theo rule. Ảnh chụp không thay artifact chạy lại được.

## Kiểm tra cuối bài

1. Set và bag semantics khác gì?
2. Pushdown qua outer join có điều kiện gì?
3. EXISTS khác inner join thế nào?
4. Chứng minh equivalence bằng gì?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một phép biến đổi có kết quả kiểm được bằng kế hoạch và số đo. Kiểm bằng ba truy vấn; đạt khi ít nhất hai bản viết lại cho cùng kết quả và chi phí thấp hơn đo được.

**Điều kiện đạt.** ≥ 2/3 bản viết lại cho kết quả khớp tuyệt đối với chi phí thấp hơn, và chứng minh được hai cách viết cho cùng kế hoạch.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Tối ưu bằng cách đổi thứ tự mệnh đề trong truy vấn · bỏ phép chọn phân biệt mà đổi kết quả · tin rằng cách viết quyết định thứ tự thực thi.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/03-relational-algebra-and-logical-equivalence.md`
- Nội dung học thuật: `note.md` cùng thư mục.
