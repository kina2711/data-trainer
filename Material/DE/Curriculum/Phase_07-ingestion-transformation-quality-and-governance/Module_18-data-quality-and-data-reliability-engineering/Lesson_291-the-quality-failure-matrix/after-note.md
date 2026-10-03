# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 18: Data Quality and Data Reliability Engineering
# Lesson 291: The quality failure matrix

## Thực hành

**Nhiệm vụ.** Lập ma trận bảy dòng đủ ba cột. Với mỗi dòng, cài chốt kiểm soát tự động. Giảng viên tiêm bảy lỗi tương ứng vào hệ và đếm bao nhiêu cái bị phát hiện, mất bao lâu. Với lỗi không bị bắt, bổ sung chốt và tiêm lại. Đưa cả bảy vào bộ kiểm hồi quy.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective tổng hợp toàn module thành một hệ phòng vệ có bằng chứng. Kiểm bằng bảy lỗi tiêm; đạt khi ít nhất sáu bị chốt kiểm soát tương ứng phát hiện tự động.

**Điều kiện đạt.** ≥ 6/7 lỗi tiêm bị phát hiện tự động kèm thời gian phát hiện, và cả bảy chốt kiểm soát nằm trong bộ kiểm hồi quy.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Viết cột chốt kiểm soát mà không cài tự động · bỏ dòng đường dẫn xanh trên nguồn cũ vì nghĩ hiếm · tin bộ kiểm hiện có đã phủ cả bảy · không đo thời gian phát hiện.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/179-the-quality-failure-matrix.md`
- Nội dung học thuật: `note.md` cùng thư mục.
