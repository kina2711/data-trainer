# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 262: The Incremental Failure Matrix

## Thực hành

**Nhiệm vụ.** Viết hành vi kỳ vọng cho sáu chế độ hỏng trước khi chạy. Với ba mô hình tăng dần, tái hiện từng chế độ hỏng và ghi lại kết quả thật. Đối soát đích với nguồn sau mỗi lần phục hồi. Chuyển sáu phép thử thành phép thử tự động chạy trong tích hợp liên tục. Sửa mọi ô không khớp kỳ vọng.

Chỉ dùng fixture/sandbox được phép. Lưu input snapshot hoặc data interval, versions, commands, compiled SQL, run artifacts, query IDs, state trước–sau, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant và input boundary.
2. Phân biệt parse, compile, execute và publish evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là tiêu chí ra của module, nên nghiệm thu là toàn bộ ma trận đạt. Kiểm bằng ma trận sáu nhân ba; đạt khi mọi ô có kết quả khớp hành vi kỳ vọng và cả sáu chế độ chạy được tự động.

**Điều kiện đạt.** Toàn bộ 18 ô khớp hành vi kỳ vọng viết trước, và sáu phép thử chạy được tự động trong tích hợp liên tục.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Viết hành vi kỳ vọng sau khi thấy kết quả · nạp lại toàn bộ để chữa ô không khớp thay vì tìm nguyên nhân · bỏ chế độ xoá vì nguồn chưa xoá · chạy ma trận bằng tay một lần rồi thôi.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/150-incremental-failure-matrix.md`
- Nội dung học thuật: `note.md` cùng thư mục.
