# Phase 5: Modeling, Semantics and Analytical Product
# Module 11: Data Modeling - Operational, Analytical and Domain
# Lesson 153: Dimensional modelling - facts, dimensions and the bus matrix

## Thực hành

**Nhiệm vụ.** Từ mô tả một doanh nghiệp bán lẻ, liệt kê sáu quy trình nghiệp vụ và các chiều. Dựng ma trận xe buýt. Chỉ ra chiều nào dùng ở nhiều quy trình và phải dùng chung. Với một chiều, mô tả cụ thể chuyện gì xảy ra nếu hai mart tự dựng bản riêng.

Chỉ chạy profiling, merge/backfill hoặc schema experiments trên dataset thử nghiệm/versioned snapshot. Không sửa identity mapping, history, keys hoặc production mart để minh họa. Lưu input snapshot, SQL/notebook, assumptions, counts/control totals và diff trước–sau.

## Kiểm tra cuối bài

1. Phát biểu grain và invariant chính.
2. Nêu phản ví dụ làm thiết kế sai cho kết quả hợp lệ cú pháp.
3. Chỉ ra phần nào là source fact và phần nào là curriculum synthesis.
4. Đề xuất phép kiểm dữ liệu tái chạy được.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài lý thuyết đặt khung cho bốn bài thực hành sau. Kiểm bằng ma trận cộng bài lập luận; đạt khi ma trận phủ đủ quy trình và chỉ đúng ít nhất ba chiều phải dùng chung kèm hậu quả nếu không.

**Điều kiện đạt.** Ma trận phủ đủ sáu quy trình, chỉ đúng ≥ 3 chiều phải dùng chung, và mô tả được hậu quả cụ thể khi không dùng chung.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đưa thuộc tính mô tả vào bảng sự kiện · chuẩn hoá bảng chiều vì thấy lặp dữ liệu · dựng mart rời nhau không có chiều dùng chung · vẽ ma trận mà không xác định quy trình nghiệp vụ trước.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/41-dimensional-modeling-facts-dimensions-bus-matrix.md`
- Nội dung học thuật: `note.md` cùng thư mục.
