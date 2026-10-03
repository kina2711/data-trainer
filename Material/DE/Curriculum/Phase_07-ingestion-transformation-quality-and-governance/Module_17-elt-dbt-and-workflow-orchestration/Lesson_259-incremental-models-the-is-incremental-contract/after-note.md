# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 259: Incremental Models and the is_incremental Contract

## Thực hành

**Nhiệm vụ.** Cài một mô hình tăng dần với khoá duy nhất và điều kiện lọc theo mốc. Chạy trên đích rỗng, rồi chạy tăng dần bảy ngày. Nạp lại toàn bộ trên cùng dữ liệu và so hai kết quả. Cố ý đưa lỗi vào khối lọc và chứng minh nó không lộ ra khi chạy trên đích rỗng. Đo chi phí có và không có giới hạn quét đích.

Chỉ dùng fixture/sandbox được phép. Lưu input snapshot hoặc data interval, versions, commands, compiled SQL, run artifacts, query IDs, state trước–sau, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant và input boundary.
2. Phân biệt parse, compile, execute và publish evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là hai chế độ cho kết quả nhất quán. Kiểm bằng đối chứng; đạt khi kết quả chạy tăng dần bảy ngày khớp kết quả nạp lại toàn bộ trên cùng dữ liệu.

**Điều kiện đạt.** Kết quả chạy tăng dần bảy ngày khớp kết quả nạp lại toàn bộ, và lỗi trong khối lọc được chứng minh là ẩn ở chế độ đầu.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chỉ kiểm mô hình bằng cách chạy trên đích rỗng · lọc nguồn mà không giới hạn quét đích · lấy mốc từ đích rồi cắt đích · không có chính sách nạp lại toàn bộ.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/147-incremental-models-is-incremental-contract.md`
- Nội dung học thuật: `note.md` cùng thư mục.
