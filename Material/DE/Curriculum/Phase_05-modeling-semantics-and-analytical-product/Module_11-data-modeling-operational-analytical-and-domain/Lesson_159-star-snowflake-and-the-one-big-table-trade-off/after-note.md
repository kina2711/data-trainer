# Phase 5: Modeling, Semantics and Analytical Product
# Module 11: Data Modeling - Operational, Analytical and Domain
# Lesson 159: Star, snowflake and the one-big-table trade-off

## Thực hành

**Nhiệm vụ.** Dựng cùng dữ liệu ở cả ba bố trí. Chạy bộ năm truy vấn chuẩn và đo thời gian cùng dung lượng. Ước lượng chi phí thay đổi bằng cách đếm số chỗ phải sửa khi đổi một định nghĩa. Khảo sát mức dễ hiểu bằng cách nhờ một người chưa biết lược đồ viết một truy vấn và tính giờ.

Chỉ chạy profiling, merge/backfill hoặc schema experiments trên dataset thử nghiệm/versioned snapshot. Không sửa identity mapping, history, keys hoặc production mart để minh họa. Lưu input snapshot, SQL/notebook, assumptions, counts/control totals và diff trước–sau.

## Kiểm tra cuối bài

1. Phát biểu grain và invariant chính.
2. Nêu phản ví dụ làm thiết kế sai cho kết quả hợp lệ cú pháp.
3. Chỉ ra phần nào là source fact và phần nào là curriculum synthesis.
4. Đề xuất phép kiểm dữ liệu tái chạy được.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi so đa tiêu chí có số đo chứ theo quy tắc chung. Kiểm bằng bảng ba bố trí nhân bốn tiêu chí; đạt khi hai tiêu chí đầu có số đo thật và lựa chọn có hai điều kiện đảo ngược.

**Điều kiện đạt.** Bảng ba bố trí nhân bốn tiêu chí có số ở hai tiêu chí đầu, và lựa chọn kèm hai điều kiện đảo ngược cụ thể.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chọn bông tuyết để tiết kiệm dung lượng mà không đo phép kết thêm · dựng bảng rộng mà không có tầng giữ định nghĩa · so ba bố trí chỉ bằng tốc độ.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/47-star-snowflake-one-big-table-trade-off.md`
- Nội dung học thuật: `note.md` cùng thư mục.
