# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 19: Metadata Engineering, Catalog, Lineage and Governance
# Lesson 305: Certification, deprecation and the expiry rule

## Thực hành

**Nhiệm vụ.** Dựng vòng đời năm trạng thái với danh mục điều kiện chứng nhận kiểm tự động, gồm tình trạng chất lượng từ M18 và quyền sở hữu đã xác nhận. Đưa ba tài sản qua vòng đời, trong đó một cái chỉ có tài liệu đầy đủ mà chưa đạt chất lượng và phải bị chặn. Đẩy đồng hồ qua ngày rà soát và chứng minh tự hạ cấp. Khai tử một tài sản với thời hạn và theo dõi mức dùng tới khi về không.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là chặn đúng và tự hạ cấp đúng. Kiểm bằng ba tài sản đi qua vòng đời; đạt khi tài sản thiếu điều kiện bị chặn chứng nhận, tài sản quá hạn tự hạ cấp, và tài sản khai tử không còn người dùng khi gỡ.

**Điều kiện đạt.** Tài sản thiếu điều kiện bị chặn chứng nhận, tài sản quá ngày rà soát tự hạ cấp, và tài sản khai tử về không người dùng trước khi gỡ.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chứng nhận dựa trên tài liệu đầy đủ · chứng nhận không có ngày rà soát · gỡ tài sản khi còn người dùng · không nói rõ chứng nhận bảo đảm điều gì.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/193-certification-deprecation-and-the-expiry-rule.md`
- Nội dung học thuật: `note.md` cùng thư mục.
