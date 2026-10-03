# Phase 5: Modeling, Semantics and Analytical Product
# Module 11: Data Modeling - Operational, Analytical and Domain
# Lesson 154: Fact types - transaction, periodic and accumulating snapshot

## Thực hành

**Nhiệm vụ.** Cho bốn câu hỏi nghiệp vụ. Chọn loại bảng sự kiện cho từng câu kèm lý do. Dựng bảng ảnh chụp tích luỹ cho vòng đời đơn hàng với năm mốc. Chạy bù 30 ngày và đối soát với bản chạy tuần tự. Tính thời gian trung bình giữa hai mốc bất kỳ.

Chỉ chạy profiling, merge/backfill hoặc schema experiments trên dataset thử nghiệm/versioned snapshot. Không sửa identity mapping, history, keys hoặc production mart để minh họa. Lưu input snapshot, SQL/notebook, assumptions, counts/control totals và diff trước–sau.

## Kiểm tra cuối bài

1. Phát biểu grain và invariant chính.
2. Nêu phản ví dụ làm thiết kế sai cho kết quả hợp lệ cú pháp.
3. Chỉ ra phần nào là source fact và phần nào là curriculum synthesis.
4. Đề xuất phép kiểm dữ liệu tái chạy được.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là chọn theo câu hỏi rồi cài đặt loại khó nhất. Kiểm bằng bốn câu hỏi cộng bài dựng; đạt khi chọn đúng cả bốn và bảng tích luỹ chạy bù cho kết quả khớp tuyệt đối.

**Điều kiện đạt.** Chọn đúng cả bốn câu hỏi, và bảng tích luỹ chạy bù 30 ngày đối soát khớp tuyệt đối.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dùng bảng giao dịch cho câu hỏi về số dư · dựng bảng tích luỹ mà không bất biến khi chạy lại · trộn hai loại vào một bảng · quên rằng số dư không cộng được theo thời gian.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/42-fact-types-transaction-periodic-accumulating.md`
- Nội dung học thuật: `note.md` cùng thư mục.
