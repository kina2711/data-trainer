# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 271: Mastering one orchestrator - Airflow or Dagster

## Thực hành

**Nhiệm vụ.** Dựng đồ thị điều phối cho đường dẫn đã có ở M16 và dbt, trên bộ điều phối đã chọn. Chứng minh mọi xử lý nặng chạy ở hệ ngoài chứ trong tiến trình lập lịch. Đo mức tăng của cơ sở dữ liệu siêu dữ liệu hoặc nhật ký sự kiện sau 100 lần chạy. Cố ý truyền một tập dữ liệu lớn qua kênh siêu dữ liệu và ghi lại hậu quả.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là năng lực dựng trên một công cụ tới mức vận hành. Kiểm bằng rà soát kiến trúc cộng phép thử tải; đạt khi không có xử lý dữ liệu nặng trong mặt điều khiển và đồ thị chạy đúng với dữ liệu thật.

**Điều kiện đạt.** Đồ thị chạy đúng với dữ liệu thật, không có xử lý nặng trong mặt điều khiển, và mức tăng siêu dữ liệu sau 100 lần chạy được đo.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Học hai bộ điều phối cùng lúc tới mức sản xuất · chạy phép biến đổi nặng trong tiến trình lập lịch · truyền dữ liệu qua kênh siêu dữ liệu · để hai nguồn sự thật về điều phối giữa dbt và bộ điều phối.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/159-mastering-one-orchestrator-airflow-or-dagster.md`
- Nội dung học thuật: `note.md` cùng thư mục.
