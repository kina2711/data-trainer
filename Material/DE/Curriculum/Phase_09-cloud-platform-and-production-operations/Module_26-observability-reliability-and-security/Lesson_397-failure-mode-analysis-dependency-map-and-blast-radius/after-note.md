# Phase 9: Cloud Platform and Production Operations
# Module 26: Observability, Reliability and Security
# Lesson 397: Failure-mode analysis, dependency map and blast radius

## Thực hành

**Nhiệm vụ.** Lập bản đồ phụ thuộc đầy đủ gồm cả phụ thuộc ngầm. Với mỗi cái, dự đoán hành vi khi nó hỏng và phạm vi ảnh hưởng. Tiêm lỗi cho năm phụ thuộc và so với dự đoán. Chọn hai phụ thuộc cứng và biến thành mềm bằng đệm hoặc chế độ suy giảm; đo lại phạm vi ảnh hưởng. Kiểm năng lực dự phòng bằng một lần chạy tải.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi phân tích trước rồi kiểm bằng thực nghiệm. Kiểm bằng tiêm lỗi phụ thuộc; đạt khi dự đoán khớp thực tế ở ít nhất ba phụ thuộc và hai phụ thuộc cứng được chuyển thành mềm có số đo.

**Điều kiện đạt.** Dự đoán khớp thực tế ở ≥ 3/5 phụ thuộc tiêm lỗi, và hai phụ thuộc cứng chuyển thành mềm với phạm vi ảnh hưởng giảm có số đo.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Bỏ sót phụ thuộc ngầm như phân giải tên và kho bí mật · đo phạm vi ảnh hưởng bằng số máy thay vì tỉ lệ người dùng · dự đoán mà không tiêm lỗi kiểm chứng · coi mọi phụ thuộc là cứng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/285-failure-mode-analysis-dependency-map-and-blast-radius.md`
- Nội dung học thuật: `note.md` cùng thư mục.
