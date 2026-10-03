# Phase 4: Data Analyst
# Module 7: Product and Business Analytics
# Lesson 62: Descriptive time series analysis

## Thực hành

**Nhiệm vụ.** Phân rã ba chỉ số trên `DS2`. Xử lý đúng ảnh hưởng của Tết âm lịch dịch chuyển giữa tháng 1 và tháng 2.

Giữ input snapshot, grain, identity, version, raw output, reconciliation và limitation.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Kiểm bằng trường hợp cụ thể có đáp án: `DS2` chứa Tết âm lịch rơi vào tháng 1 ở một năm và tháng 2 ở năm khác. Bài xử lý sai sẽ cho chênh lệch so cùng kỳ rất lớn ở đúng hai tháng đó, nên lỗi định vị được chính xác.

**Điều kiện đạt.** Ba chỉ số được phân rã thành ba thành phần, và so sánh kỳ ở hai tháng có Tết khớp với đáp án sau khi chỉnh ngày lễ dịch chuyển.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 60 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 25 phút trả lời bốn câu kiểm tra · 15 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** So cùng kỳ năm trước theo số tháng mà không chỉnh ngày lễ dịch chuyển · làm mượt bằng cửa sổ dài hơn chu kỳ mùa vụ nên xoá mất tín hiệu · coi điểm gãy do đổi định nghĩa chỉ số là thay đổi thật.

## Reference
- Knowledge note: `Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/062-descriptive-time-series-analysis.md`
