# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 254: Project Layers Staging Intermediate and Marts

## Thực hành

**Nhiệm vụ.** Dựng dự án ít nhất mười mô hình đủ ba tầng. Đưa cho một học viên khác chỉ đọc tệp và tài liệu mô hình, yêu cầu họ ghi ra hạt, chủ sở hữu, nguồn thượng lưu và bên tiêu thụ của từng mô hình. Đếm số mô hình họ xác định đúng cả bốn. Sửa những mô hình họ không xác định được và kiểm lại.

Chỉ dùng fixture/sandbox được phép. Lưu input snapshot hoặc data interval, versions, commands, compiled SQL, run artifacts, query IDs, state trước–sau, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant và input boundary.
2. Phân biệt parse, compile, execute và publish evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có phép thử khách quan là kết quả của người rà soát độc lập. Kiểm bằng phép thử rà soát chéo; đạt khi người rà soát xác định đúng bốn thuộc tính ở ít nhất tám trên mười mô hình.

**Điều kiện đạt.** Người rà soát độc lập xác định đúng bốn thuộc tính ở ≥ 8/10 mô hình chỉ từ tệp và tài liệu.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đặt phép gộp nghiệp vụ ở tầng chuẩn bị · để bên tiêu thụ đọc thẳng tầng trung gian · viết mô hình khổng lồ thay vì tách tầng trung gian · dùng tên cột gốc của nguồn ở tầng phục vụ.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/142-project-layers-staging-intermediate-marts.md`
- Nội dung học thuật: `note.md` cùng thư mục.
