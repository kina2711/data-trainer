# Phase 5: Modeling, Semantics and Analytical Product
# Module 11: Data Modeling - Operational, Analytical and Domain
# Lesson 150: Declaring the grain before the columns

## Thực hành

**Nhiệm vụ.** Cho năm bảng có dữ liệu thật, không kèm tài liệu. Với mỗi bảng, suy ra hạt từ dữ liệu, viết phát biểu, rồi kiểm bằng cách đếm dòng theo tập khoá tuyên bố. Với bảng nào phát biểu sai, sửa lại và kiểm lần nữa. Ghi lại bảng nào có hạt khác với tên bảng gợi ý.

Chỉ chạy profiling, merge/backfill hoặc schema experiments trên dataset thử nghiệm/versioned snapshot. Không sửa identity mapping, history, keys hoặc production mart để minh họa. Lưu input snapshot, SQL/notebook, assumptions, counts/control totals và diff trước–sau.

## Kiểm tra cuối bài

1. Phát biểu grain và invariant chính.
2. Nêu phản ví dụ làm thiết kế sai cho kết quả hợp lệ cú pháp.
3. Chỉ ra phần nào là source fact và phần nào là curriculum synthesis.
4. Đề xuất phép kiểm dữ liệu tái chạy được.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có phép kiểm chứng khách quan bằng truy vấn, chứ dựa vào cảm nhận. Kiểm bằng phép đếm trùng; đạt khi cả năm phát biểu được dữ liệu xác nhận hoặc bị bác bỏ và sửa lại đúng.

**Điều kiện đạt.** Cả năm phát biểu được kiểm bằng phép đếm, và mọi phát biểu sai đều được phát hiện rồi sửa đúng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Tin tên bảng nói đúng hạt · phát biểu hạt rồi không kiểm bằng dữ liệu · nhầm hạt với khoá chính · chấp nhận phát biểu có từ mơ hồ như thông tin hay dữ liệu.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/38-declaring-the-grain-before-the-columns.md`
- Nội dung học thuật: `note.md` cùng thư mục.
