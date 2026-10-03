# Phase 2: Machine, Operating System and Network
# Module 4: Computer Architecture and the Performance Model
# Lesson 57: Linking the model to databases

## Thực hành

**Nhiệm vụ.** Cho bốn tình huống truy vấn với tỉ lệ dòng lấy ra khác nhau, từ 0,01% tới 40% bảng. Với mỗi tình huống, ước lượng số lần đọc ngẫu nhiên nếu dùng chỉ mục và số lần đọc tuần tự nếu quét, rồi dự đoán bộ tối ưu chọn cách nào. Ước lượng độ rẽ nhánh và chiều cao cây chỉ mục cho một bảng một triệu dòng.

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài nối, chuẩn bị trực tiếp cho M9 và M10; chưa đòi vận hành cơ sở dữ liệu. Kiểm bằng bài lập luận trên bốn tình huống; đạt khi giải thích đúng ít nhất ba bằng chi phí đọc chứ bằng quy tắc thuộc lòng.

**Điều kiện đạt.** Giải thích đúng ≥ 3/4 tình huống bằng ước lượng số lần đọc, và tính đúng chiều cao cây chỉ mục.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Cho rằng có chỉ mục thì luôn nên dùng chỉ mục · bỏ qua tỉ lệ dòng lấy ra · quên rằng tra chỉ mục còn phải đọc thêm dòng dữ liệu · học quy tắc thay vì tính chi phí.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/057-linking-the-model-to-databases.md`
- Nội dung học thuật: `note.md` cùng thư mục.
