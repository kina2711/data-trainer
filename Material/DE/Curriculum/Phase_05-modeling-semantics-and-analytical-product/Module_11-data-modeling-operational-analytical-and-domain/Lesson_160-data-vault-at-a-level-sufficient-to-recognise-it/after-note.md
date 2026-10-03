# Phase 5: Modeling, Semantics and Analytical Product
# Module 11: Data Modeling - Operational, Analytical and Domain
# Lesson 160: Data Vault at a level sufficient to recognise it

## Thực hành

**Nhiệm vụ.** Cho một lược đồ đã dựng theo phương pháp này; nhận dạng ba thành phần và viết một truy vấn lấy thông tin khách hàng hiện hành, đếm số phép kết cần. Cho ba bối cảnh khác nhau về tần suất đổi lược đồ nguồn, yêu cầu kiểm toán và quy mô đội; quyết định có dùng không.

Chỉ chạy profiling, merge/backfill hoặc schema experiments trên dataset thử nghiệm/versioned snapshot. Không sửa identity mapping, history, keys hoặc production mart để minh họa. Lưu input snapshot, SQL/notebook, assumptions, counts/control totals và diff trước–sau.

## Kiểm tra cuối bài

1. Phát biểu grain và invariant chính.
2. Nêu phản ví dụ làm thiết kế sai cho kết quả hợp lệ cú pháp.
3. Chỉ ra phần nào là source fact và phần nào là curriculum synthesis.
4. Đề xuất phép kiểm dữ liệu tái chạy được.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective là năng lực đánh giá chứ triển khai, đúng phạm vi bản nguồn đặt ra. Kiểm bằng ba bối cảnh; đạt khi quyết định đúng cả ba và nêu đúng chi phí kéo theo ở bối cảnh chọn dùng.

**Điều kiện đạt.** Nhận đúng ba thành phần kèm số phép kết đo được, và quyết định đúng cả ba bối cảnh kèm chi phí kéo theo.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chọn vì nghe chuyên nghiệp · dùng mà không dựng tầng phục vụ ở trên · nghĩ nó thay thế mô hình chiều · bỏ qua chi phí nuôi hai tầng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/48-data-vault-at-recognition-level.md`
- Nội dung học thuật: `note.md` cùng thư mục.
