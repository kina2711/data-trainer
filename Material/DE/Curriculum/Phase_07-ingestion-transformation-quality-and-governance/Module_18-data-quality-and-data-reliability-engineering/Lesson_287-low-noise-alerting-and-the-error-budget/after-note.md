# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 18: Data Quality and Data Reliability Engineering
# Lesson 287: Low-noise alerting and the error budget

## Thực hành

**Nhiệm vụ.** Rà toàn bộ cảnh báo đang có, đếm tỉ lệ không hành động được trong 30 ngày. Chuyển các quy tắc dòng từ cảnh báo sang ghi nhận. Dựng cảnh báo theo tốc độ tiêu ngân sách ở hai mức. Bổ sung đủ bốn thuộc tính. Phát lại ba sự cố lịch sử và kiểm cảnh báo có nổ đúng lúc, đúng người. Đo lại tỉ lệ không hành động được.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đo chất lượng cảnh báo bằng tỉ lệ hành động được, chứ bằng độ phủ. Kiểm bằng phát lại sự cố cũ; đạt khi ba sự cố đều sinh cảnh báo đúng chủ sở hữu và tỉ lệ cảnh báo không hành động được giảm có số đo.

**Điều kiện đạt.** Ba sự cố phát lại đều sinh cảnh báo đúng người, mọi cảnh báo có đủ bốn thuộc tính, và tỉ lệ không hành động được giảm có số đo.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Cảnh báo trên từng quy tắc dòng · cảnh báo không có sổ tay xử lý · đặt ngưỡng để bảng theo dõi xanh · im lặng vĩnh viễn thay vì im lặng có hạn.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/175-low-noise-alerting-and-the-error-budget.md`
- Nội dung học thuật: `note.md` cùng thư mục.
