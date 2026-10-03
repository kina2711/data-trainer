# Phase 5: Modeling, Semantics and Analytical Product
# Module 11: Data Modeling - Operational, Analytical and Domain
# Lesson 158: Valid time, system time, corrections and restatement

## Thực hành

**Nhiệm vụ.** Dựng bảng có cả hai trục thời gian. Tạo một chuỗi sự kiện gồm một lần biết muộn và một lần hiệu chỉnh dữ liệu sai. Trả lời bốn câu hỏi: hai câu về tình trạng thật và hai câu về báo cáo đã công bố. Viết chính sách hiệu chỉnh nêu rõ số đã công bố có đổi không và ai quyết.

Chỉ chạy profiling, merge/backfill hoặc schema experiments trên dataset thử nghiệm/versioned snapshot. Không sửa identity mapping, history, keys hoặc production mart để minh họa. Lưu input snapshot, SQL/notebook, assumptions, counts/control totals và diff trước–sau.

## Kiểm tra cuối bài

1. Phát biểu grain và invariant chính.
2. Nêu phản ví dụ làm thiết kế sai cho kết quả hợp lệ cú pháp.
3. Chỉ ra phần nào là source fact và phần nào là curriculum synthesis.
4. Đề xuất phép kiểm dữ liệu tái chạy được.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi phân biệt hai trục và nhận ra đây là quyết định có bên liên quan. Kiểm bằng bốn câu hỏi hai loại; đạt khi trả lời đúng ít nhất ba và chính sách hiệu chỉnh nêu rõ ai quyết.

**Điều kiện đạt.** Trả lời đúng ≥ 3/4 câu hỏi hai loại, và chính sách hiệu chỉnh nêu rõ hành vi cùng người quyết.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chỉ lưu một trục thời gian · sửa dữ liệu cũ mà không ghi lại đã sửa · đổi số đã công bố mà không báo bên dùng · coi chính sách hiệu chỉnh là quyết định kỹ thuật.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/46-valid-time-system-time-corrections-restatement.md`
- Nội dung học thuật: `note.md` cùng thư mục.
