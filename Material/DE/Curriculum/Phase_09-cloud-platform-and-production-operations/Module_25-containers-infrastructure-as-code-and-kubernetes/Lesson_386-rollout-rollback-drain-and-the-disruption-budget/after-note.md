# Phase 9: Cloud Platform and Production Operations
# Module 25: Containers, Infrastructure as Code and Kubernetes
# Lesson 386: Rollout, rollback, drain and the disruption budget

## Thực hành

**Nhiệm vụ.** Chạy tải liên tục trong lúc triển khai phiên bản mới; đo tỉ lệ lỗi và độ trễ. Thực hiện quay lui và đo lại. Rút một nút khi có tải và kiểm không yêu cầu nào bị cắt giữa chừng. Đặt ngân sách gián đoạn quá chặt rồi rút nút; quan sát bế tắc và gỡ bằng cách thêm năng lực hoặc nới ngân sách.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là không yêu cầu nào lỗi trong suốt quá trình. Kiểm bằng phép thử tải liên tục; đạt khi tỉ lệ lỗi bằng không suốt triển khai và quay lui, và bế tắc do ngân sách được tái hiện rồi gỡ.

**Điều kiện đạt.** Tỉ lệ lỗi bằng không suốt triển khai và quay lui, không yêu cầu nào bị cắt khi rút nút, và bế tắc do ngân sách được tái hiện rồi gỡ.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Triển khai mà không chạy tải nên không thấy lỗi · chưa từng thử quay lui · rút nút mà không có tắt có kiểm soát · đặt ngân sách gián đoạn mà không xét năng lực dự phòng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/274-rollout-rollback-drain-and-the-disruption-budget.md`
- Nội dung học thuật: `note.md` cùng thư mục.
