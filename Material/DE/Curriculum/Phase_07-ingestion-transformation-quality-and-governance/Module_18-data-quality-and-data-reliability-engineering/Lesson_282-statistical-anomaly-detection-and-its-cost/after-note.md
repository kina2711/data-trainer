# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 18: Data Quality and Data Reliability Engineering
# Lesson 282: Statistical anomaly detection and its cost

## Thực hành

**Nhiệm vụ.** Chọn ba chỉ số có tính mùa vụ khác nhau. Dựng đường cơ sở bằng thống kê bền vững, phân đoạn theo nguồn hoặc theo phân khúc. Chạy trên sáu tháng dữ liệu lịch sử đã gắn nhãn sự cố và sự kiện nghiệp vụ hợp lệ. Tính độ chính xác và độ phủ ở ba mức ngưỡng. Chỉ ra ba chỗ đang định dùng phát hiện thống kê nhưng viết được thành bất biến.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi cân hai loại sai lầm và biết ranh giới dùng của phương pháp. Kiểm bằng cặp số độ chính xác với độ phủ; đạt khi cả ba chỉ số có cặp số đo trên dữ liệu lịch sử và không bất biến nào bị thay bằng phát hiện thống kê.

**Điều kiện đạt.** Ba chỉ số có cặp độ chính xác với độ phủ ở ba mức ngưỡng, và ba trường hợp viết lại được thành bất biến đã được chuyển.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dùng phát hiện thống kê cho thứ biểu diễn được bằng bất biến · dùng trung bình và độ lệch chuẩn trên dữ liệu có giá trị ngoại lai · bỏ tính mùa vụ nên mỗi thứ hai là một sự cố · coi bất thường là bằng chứng lỗi.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/170-statistical-anomaly-detection-and-its-cost.md`
- Nội dung học thuật: `note.md` cùng thư mục.
