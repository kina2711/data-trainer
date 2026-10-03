# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 18: Data Quality and Data Reliability Engineering
# Lesson 289: Repair, backfill and restatement

## Thực hành

**Nhiệm vụ.** Nhận hai sự cố: một phân vùng thiếu và một hồi quy logic thầm lặng. Với mỗi cái, chạy thử không ghi, sửa trong đích cách ly, đối soát, thăng cấp, rồi thực hiện quay lại. Ghi chính sách trình bày lại kèm người duyệt và cách báo bên tiêu thụ. Ghi lại dấu vết đã sửa gì và bởi ai.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là đối soát đạt trước công bố và quay lại được sau đó. Kiểm bằng hai sự cố sửa đầy đủ; đạt khi cả hai đối soát đạt ở đích cách ly trước khi thăng cấp và quay lại thực hiện được.

**Điều kiện đạt.** Hai sự cố đều đối soát đạt ở đích cách ly trước khi thăng cấp, quay lại thực hiện được, và dấu vết sửa được ghi đầy đủ.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Sửa thẳng vào bảng phục vụ · công bố lại trước khi đối soát · nạp lại toàn bộ để chữa mà không truy nguyên nhân · sửa hạ nguồn khi nguồn vẫn còn sai.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/177-repair-backfill-and-restatement.md`
- Nội dung học thuật: `note.md` cùng thư mục.
