# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 269: Orchestration Primitives Before the Tool

## Thực hành

**Nhiệm vụ.** Cho một đồ thị tám cạnh trong đó vài cạnh chỉ là thứ tự chạy chứ phụ thuộc dữ liệu. Phân loại từng cạnh và vẽ lại đồ thị chỉ giữ phụ thuộc dữ liệu; đo mức song song tăng thêm. Tìm mọi chỗ đang giả định nguồn xong theo giờ và thay bằng một tín hiệu dữ liệu sẵn sàng.

Chỉ dùng fixture/sandbox được phép. Lưu input snapshot hoặc data interval, versions, commands, compiled SQL, run artifacts, query IDs, state trước–sau, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant và input boundary.
2. Phân biệt parse, compile, execute và publish evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài lý thuyết đặt từ vựng chung trước khi chọn công cụ. Kiểm bằng bài phân tích một đồ thị; đạt khi phân đúng ít nhất sáu trong tám cạnh và mọi giả định thời gian được thay bằng tín hiệu dữ liệu.

**Điều kiện đạt.** Phân đúng ≥ 6/8 cạnh, mức song song tăng thêm được đo, và mọi giả định thời gian được thay bằng tín hiệu dữ liệu.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Nối các việc theo thứ tự thuận tiện rồi gọi đó là phụ thuộc · lập lịch theo giờ dựa trên niềm tin nguồn đã xong · nhầm kỳ dữ liệu với thời điểm chạy · để tác dụng phụ ngoài ranh giới việc.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/157-orchestration-primitives-before-tool.md`
- Nội dung học thuật: `note.md` cùng thư mục.
