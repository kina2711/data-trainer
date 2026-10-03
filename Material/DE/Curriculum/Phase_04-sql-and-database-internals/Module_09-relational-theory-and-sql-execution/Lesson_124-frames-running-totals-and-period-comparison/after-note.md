# Phase 4: SQL and Database Internals
# Module 9: Relational Theory and SQL Execution
# Lesson 124: Frames, running totals and period comparison

## Thực hành

**Nhiệm vụ.** Dựng báo cáo 24 tháng có ba chỉ số trên dữ liệu cố ý thiếu ba tháng. Đối soát với bản tính độc lập. So kết quả giữa khung đếm theo dòng và khung đếm theo giá trị trên dữ liệu có trùng. Xử lý trường hợp kỳ trước bằng không và nêu nghĩa nghiệp vụ đã chọn.

Lưu SQL, seed data, dự đoán trước khi chạy, output thô, đối soát độc lập và giải thích theo rule. Ảnh chụp không thay artifact chạy lại được.

## Kiểm tra cuối bài

1. ROWS, RANGE và GROUPS khác đơn vị nào?
2. Vì sao phải dựng calendar scaffold?
3. Previous zero phải biểu diễn thế nào?
4. Đối soát rolling metric từng kỳ ra sao?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có một ca biên cụ thể mà bản làm ẩu luôn sai. Kiểm bằng đối soát với bản tính độc lập; đạt khi khớp tuyệt đối kể cả ở các kỳ thiếu dữ liệu.

**Điều kiện đạt.** Ba chỉ số khớp tuyệt đối với bản tính độc lập kể cả ở ba tháng thiếu, và giải thích được khác biệt giữa hai cách đếm khung.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Không dựng bảng lịch nên kỳ rỗng biến mất · dựa vào khung mặc định · nhầm hai cách đếm khung · chia cho không mà không xử lý.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/12-window-frames-running-totals-and-period-comparison.md`
- Nội dung học thuật: `note.md` cùng thư mục.
