# Phase 5: Modeling, Semantics and Analytical Product
# Module 11: Data Modeling - Operational, Analytical and Domain
# Lesson 157: Slowly changing dimensions, type 0 to type 6

## Thực hành

**Nhiệm vụ.** Cài chiều khách hàng loại hai. Chạy 1000 lần cập nhật thuộc tính, gồm cả cập nhật tới muộn và cập nhật hiệu chỉnh. Chạy hai phép kiểm bất biến. Dựng cùng báo cáo doanh thu theo vùng trên bản loại một và bản loại hai, so hai kết quả cho kỳ lịch sử.

Chỉ chạy profiling, merge/backfill hoặc schema experiments trên dataset thử nghiệm/versioned snapshot. Không sửa identity mapping, history, keys hoặc production mart để minh họa. Lưu input snapshot, SQL/notebook, assumptions, counts/control totals và diff trước–sau.

## Kiểm tra cuối bài

1. Phát biểu grain và invariant chính.
2. Nêu phản ví dụ làm thiết kế sai cho kết quả hợp lệ cú pháp.
3. Chỉ ra phần nào là source fact và phần nào là curriculum synthesis.
4. Đề xuất phép kiểm dữ liệu tái chạy được.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một cài đặt có hai bất biến kiểm được bằng truy vấn. Kiểm bằng hai phép kiểm bất biến cộng đối chứng; đạt khi cả hai bất biến giữ được qua 1000 lần cập nhật và sai lệch của loại một được định lượng.

**Điều kiện đạt.** Hai bất biến giữ được qua 1000 lần cập nhật, và chênh lệch báo cáo giữa loại một và loại hai được định lượng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Ghi đè thuộc tính rồi mất lịch sử · để khoảng hiệu lực chồng nhau · có hai dòng cùng đánh dấu hiện hành · quên xử lý cập nhật tới muộn nên chèn sai thứ tự.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/45-slowly-changing-dimensions-type-0-to-type-6.md`
- Nội dung học thuật: `note.md` cùng thư mục.
