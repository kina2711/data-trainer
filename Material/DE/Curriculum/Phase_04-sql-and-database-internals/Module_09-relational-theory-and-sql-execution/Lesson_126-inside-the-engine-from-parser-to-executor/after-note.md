# Phase 4: SQL and Database Internals
# Module 9: Relational Theory and SQL Execution
# Lesson 126: Inside the engine - from parser to executor

## Thực hành

**Nhiệm vụ.** Cho sáu hiện tượng gồm lỗi tên cột, truy vấn viết khác nhau ra cùng kế hoạch, kế hoạch đổi sau khi cập nhật thống kê, và ba cái khác. Quy mỗi hiện tượng về một giai đoạn. Đọc cấu hình chi phí của hệ và chỉ ra giả định nào về phần cứng đang được dùng.

Lưu SQL, seed/workload, dự đoán trước khi chạy, plan dạng máy đọc được, output thô, đối soát và thông số môi trường. Chỉ chạy DDL/spill/load test trong môi trường cô lập với lock/statement timeout; ảnh chụp không thay artifact tái chạy.

## Kiểm tra cuối bài

1. Parser khác binder ở lỗi nào?
2. Rewrite khác planner thế nào?
3. Cost units có phải milliseconds không?
4. Tìm node estimation sai đầu tiên ra sao?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài lý thuyết nền cho toàn phần thực thi. Kiểm bằng sáu hiện tượng cần quy về giai đoạn; đạt khi quy đúng ít nhất bốn và giải thích đúng vai trò của ước lượng.

**Điều kiện đạt.** Quy đúng ≥ 4/6 hiện tượng về giai đoạn, và chỉ ra được giả định phần cứng trong cấu hình chi phí.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Nghĩ bộ tối ưu luôn chọn đúng · đổ lỗi cho engine khi nguyên nhân là ước lượng sai · bỏ qua cấu hình chi phí không khớp phần cứng thật.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/14-inside-the-engine-parser-to-executor.md`
- Nội dung học thuật: `note.md` cùng thư mục.
