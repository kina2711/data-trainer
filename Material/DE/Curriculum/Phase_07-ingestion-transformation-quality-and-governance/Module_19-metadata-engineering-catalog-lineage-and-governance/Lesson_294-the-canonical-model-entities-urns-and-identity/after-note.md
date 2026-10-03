# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 19: Metadata Engineering, Catalog, Lineage and Governance
# Lesson 294: The canonical model - entities, URNs and identity

## Thực hành

**Nhiệm vụ.** Định nghĩa lược đồ thực thể và quy tắc sinh tên định danh chuẩn. Lấy 40 tài sản thật từ bốn hệ và ba môi trường, sinh định danh cho từng cái. Kiểm không có hai tài sản khác nhau nhận cùng định danh và không có một tài sản nhận hai định danh. Tạo một ca trùng danh tính và gộp bằng cơ chế bí danh. So hai cách lưu trữ trên một truy vấn đồ thị điển hình.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là không đụng độ và không chẻ danh tính. Kiểm bằng bài phân giải; đạt khi 40 tài sản từ bốn hệ phân giải đúng, không cặp nào đụng độ, và ca trùng danh tính được gộp đúng.

**Điều kiện đạt.** 40 tài sản phân giải đúng không đụng độ và không chẻ danh tính, và ca trùng được gộp bằng bí danh.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dùng tên bảng làm định danh · bỏ môi trường khỏi định danh nên phát triển và sản xuất lẫn nhau · cho phép cặp khoá giá trị tuỳ ý thay vì mở rộng lược đồ có kiểm soát · không có cơ chế gộp danh tính trùng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/182-the-canonical-model-entities-urns-and-identity.md`
- Nội dung học thuật: `note.md` cùng thư mục.
