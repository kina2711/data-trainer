# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 273: Control-plane diagnosis - the required incident list

## Thực hành

**Nhiệm vụ.** Tái hiện sáu sự cố trên hệ đã dựng. Với mỗi cái, chạy đường truy vết ba chặng và ghi lại bằng chứng ở mỗi chặng. Sửa và đo lại. Với sự cố phân tích tệp định nghĩa, đo thời gian phân tích trước và sau khi giảm số tệp hoặc bỏ mã chạy lúc phân tích. Ghi mỗi sự cố thành một mục trong sổ tay vận hành.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi chẩn đoán có phương pháp trong một hệ nhiều thành phần. Kiểm bằng sáu sự cố tái hiện; đạt khi truy đúng chặng gây ra ở ít nhất năm và sửa được ít nhất bốn với số đo trước sau.

**Điều kiện đạt.** Truy đúng chặng gây ra ở ≥ 5/6 sự cố, ≥ 4 sự cố được sửa với số đo trước sau, và mỗi sự cố có một mục trong sổ tay.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đoán nguyên nhân từ triệu chứng mà không truy vết · sửa bằng cách khởi động lại rồi coi là xong · cho ứng dụng ghi thẳng vào bảng siêu dữ liệu · không ghi sự cố vào sổ tay.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/161-control-plane-diagnosis-the-required-incident-list.md`
- Nội dung học thuật: `note.md` cùng thư mục.
