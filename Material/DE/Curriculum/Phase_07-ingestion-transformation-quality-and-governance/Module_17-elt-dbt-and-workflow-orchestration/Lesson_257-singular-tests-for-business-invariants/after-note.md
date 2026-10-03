# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 257: Singular Tests for Business Invariants

## Thực hành

**Nhiệm vụ.** Viết bốn phép kiểm thuộc bốn nhóm bất biến. Với mỗi cái, tiêm đúng loại lỗi nó nhắm tới và xác nhận nó đỏ. Chạy cả bốn trên 30 ngày dữ liệu sạch và đếm số lần báo giả. Sửa cho tới khi không còn báo giả. Viết một phép kiểm đối soát giữa mô hình phục vụ với vùng thô.

Chỉ dùng fixture/sandbox được phép. Lưu input snapshot hoặc data interval, versions, commands, compiled SQL, run artifacts, query IDs, state trước–sau, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant và input boundary.
2. Phân biệt parse, compile, execute và publish evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu hai chiều. Kiểm bằng phép thử tiêm cộng phép thử trên dữ liệu sạch; đạt khi cả bốn bắt đúng lỗi tương ứng và không cái nào báo giả trên 30 ngày dữ liệu sạch.

**Điều kiện đạt.** Bốn phép kiểm bắt đúng lỗi nhắm tới và không báo giả trên 30 ngày dữ liệu sạch.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Viết phép kiểm trả về đúng sai nên không điều tra được · không thử trên dữ liệu sạch nên không biết tỉ lệ báo giả · viết hàng trăm phép kiểm ồn · nhầm phép kiểm chất lượng với phép kiểm đơn vị.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/145-singular-tests-business-invariants.md`
- Nội dung học thuật: `note.md` cùng thư mục.
