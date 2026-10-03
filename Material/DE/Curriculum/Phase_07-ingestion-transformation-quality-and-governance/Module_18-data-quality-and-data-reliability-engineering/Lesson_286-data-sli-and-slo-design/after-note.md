# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 18: Data Quality and Data Reliability Engineering
# Lesson 286: Data SLI and SLO design

## Thực hành

**Nhiệm vụ.** Chọn ba hành trình người dùng khác mức trọng yếu. Với mỗi cái, định nghĩa chỉ số phục vụ và cam kết đủ bốn phần. Nhờ một học viên khác tính độc lập ba cam kết trên cùng dữ liệu và so con số. Tạo một tình huống công việc xanh mà cam kết vẫn vỡ, và giải thích vì sao. Đặt ngân sách sai sót và nêu quyết định nó chi phối.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective đòi đặt cam kết theo người dùng chứ theo công việc. Kiểm bằng phép thử hai người tính độc lập; đạt khi ba cam kết cho cùng con số ở hai người và mỗi cam kết dẫn được về một hành trình người dùng.

**Điều kiện đạt.** Ba cam kết cho cùng con số khi hai người tính độc lập, mỗi cam kết dẫn về một hành trình người dùng, và tình huống công việc xanh mà cam kết vỡ được tái hiện.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đặt cam kết theo công việc chạy · không nêu phần loại trừ nên hai người tính khác nhau · đặt cam kết bằng năng lực hiện có · bỏ chỉ số về tính đúng vì khó đo.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/174-data-sli-and-slo-design.md`
- Nội dung học thuật: `note.md` cùng thư mục.
