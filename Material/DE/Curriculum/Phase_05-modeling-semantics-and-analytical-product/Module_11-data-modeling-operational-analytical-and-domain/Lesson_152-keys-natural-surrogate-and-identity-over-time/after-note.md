# Phase 5: Modeling, Semantics and Analytical Product
# Module 11: Data Modeling - Operational, Analytical and Domain
# Lesson 152: Keys - natural, surrogate and identity over time

## Thực hành

**Nhiệm vụ.** Thiết kế khoá cho bảng chiều khách hàng. Xử lý ba ca: mã khách đổi, mã khách được cấp lại cho người khác, và hai bản ghi được xác định là cùng một người. Với mỗi ca, chứng minh dữ liệu lịch sử vẫn truy được và đối soát theo khoá nghiệp vụ vẫn khớp.

Chỉ chạy profiling, merge/backfill hoặc schema experiments trên dataset thử nghiệm/versioned snapshot. Không sửa identity mapping, history, keys hoặc production mart để minh họa. Lưu input snapshot, SQL/notebook, assumptions, counts/control totals và diff trước–sau.

## Kiểm tra cuối bài

1. Phát biểu grain và invariant chính.
2. Nêu phản ví dụ làm thiết kế sai cho kết quả hợp lệ cú pháp.
3. Chỉ ra phần nào là source fact và phần nào là curriculum synthesis.
4. Đề xuất phép kiểm dữ liệu tái chạy được.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một thiết kế có ca biên cụ thể kiểm được. Kiểm bằng ba ca biên; đạt khi cả ba được xử lý đúng và đối soát theo khoá nghiệp vụ vẫn khớp sau khi gộp.

**Điều kiện đạt.** Ba ca biên được xử lý đúng, dữ liệu lịch sử vẫn truy được, và đối soát theo khoá nghiệp vụ khớp sau khi gộp.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Bỏ khoá nghiệp vụ vì đã có khoá thay thế · băm từ cột có thể thiếu giá trị · giả định mã nghiệp vụ không bao giờ được cấp lại · xử lý gộp danh tính bằng cách xoá một bản ghi.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/40-keys-natural-surrogate-and-identity-over-time.md`
- Nội dung học thuật: `note.md` cùng thư mục.
