# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 18: Data Quality and Data Reliability Engineering
# Lesson 290: False positives, coverage and quality debt

## Thực hành

**Nhiệm vụ.** Đo tỉ lệ báo giả trong 30 ngày, chạy lại ánh xạ rủi ro với quy tắc, và lập sổ nợ chất lượng gồm miễn trừ hết hạn cùng quy tắc đang tắt. Với mọi phép kiểm có bộ lọc, đối chiếu số dòng nó xét với số dòng bảng và tìm ca che dữ liệu hỏng. Gỡ những quy tắc không còn phủ rủi ro nào.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi đánh giá chính hệ kiểm chứ dữ liệu. Kiểm bằng ba chỉ số cộng bài rà phạm vi; đạt khi ba chỉ số có số đo và mọi phép kiểm có bộ lọc thu hẹp đều được đối chiếu số dòng xét.

**Điều kiện đạt.** Ba chỉ số sức khoẻ có số đo, mọi phép kiểm có bộ lọc được đối chiếu số dòng xét, và sổ nợ chất lượng có chủ cùng hạn.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Coi phép kiểm xanh là dữ liệu sạch mà không xem phạm vi · để miễn trừ hết hạn nằm mãi · thêm quy tắc mà không bao giờ gỡ · đo độ phủ bằng số lượng quy tắc.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/178-false-positives-coverage-and-quality-debt.md`
- Nội dung học thuật: `note.md` cùng thư mục.
