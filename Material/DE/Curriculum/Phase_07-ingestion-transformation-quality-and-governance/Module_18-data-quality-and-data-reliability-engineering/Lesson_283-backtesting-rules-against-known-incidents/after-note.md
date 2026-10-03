# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 18: Data Quality and Data Reliability Engineering
# Lesson 283: Backtesting rules against known incidents

## Thực hành

**Nhiệm vụ.** Gắn nhãn sáu tháng dữ liệu gồm ba sự cố đã biết và bốn thay đổi nghiệp vụ hợp lệ. Chạy bộ quy tắc và lập bảng bốn ô. Với mỗi sự cố bị bỏ sót, thêm hoặc sửa quy tắc rồi chạy lại. Với mỗi báo giả, thu hẹp phạm vi hoặc hạ mức nghiêm trọng. Nộp bảng ánh xạ rủi ro với quy tắc phủ nó.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective thay phép đếm quy tắc bằng phép đo độ phủ rủi ro. Kiểm bằng bảng bốn ô cộng bảng rủi ro; đạt khi mọi rủi ro trọng yếu có ít nhất một quy tắc phủ và tỉ lệ báo giả nằm dưới ngưỡng thoả thuận.

**Điều kiện đạt.** Mọi rủi ro trọng yếu có quy tắc phủ, ba sự cố lịch sử đều bị bắt sau khi sửa, và tỉ lệ báo giả dưới ngưỡng thoả thuận.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Báo cáo độ phủ bằng số lượng quy tắc · chỉ kiểm ngược trên khoảng có sự cố · giữ quy tắc báo giả nhiều vì nó đã từng bắt đúng một lần · không gắn nhãn thay đổi nghiệp vụ hợp lệ.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/171-backtesting-rules-against-known-incidents.md`
- Nội dung học thuật: `note.md` cùng thư mục.
