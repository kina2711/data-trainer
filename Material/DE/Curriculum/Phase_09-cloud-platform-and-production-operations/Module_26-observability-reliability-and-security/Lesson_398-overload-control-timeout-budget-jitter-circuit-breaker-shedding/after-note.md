# Phase 9: Cloud Platform and Production Operations
# Module 26: Observability, Reliability and Security
# Lesson 398: Overload control - timeout budget, jitter, circuit breaker, shedding

## Thực hành

**Nhiệm vụ.** Chạy tải vượt năng lực hai lần cho một dịch vụ ba chặng. Đo điểm sập của bản chưa có cơ chế. Thêm lần lượt năm cơ chế và đo sau mỗi lần. Đặt ba tham số của ngắt mạch từ số đo chứ mặc định. Phân loại lưu lượng theo mức ưu tiên và chứng minh phần ưu tiên vẫn đúng cam kết khi đang loại bỏ tải.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là hệ giữ được cam kết cho phần lưu lượng ưu tiên. Kiểm bằng phép thử quá tải; đạt khi bản chưa có cơ chế sập, bản có cơ chế giữ tỉ lệ phục vụ trên ngưỡng, và đóng góp của từng cơ chế có số đo.

**Điều kiện đạt.** Bản chưa có cơ chế sập còn bản có cơ chế giữ tỉ lệ phục vụ trên ngưỡng, đóng góp từng cơ chế có số đo, và phần lưu lượng ưu tiên vẫn đúng cam kết.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Thử lại không có ngân sách · đặt tham số ngắt mạch theo giá trị mặc định · dùng một bể tài nguyên chung cho mọi phụ thuộc · loại bỏ tải ngẫu nhiên thay vì theo mức ưu tiên.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/286-overload-control-timeout-budget-jitter-circuit-breaker-shedding.md`
- Nội dung học thuật: `note.md` cùng thư mục.
