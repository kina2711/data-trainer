# Phase 9: Cloud Platform and Production Operations
# Module 25: Containers, Infrastructure as Code and Kubernetes
# Lesson 387: Diagnosing ten broken workloads

## Thực hành

**Nhiệm vụ.** Nhận mười khối lượng công việc hỏng thuộc năm nhóm. Với mỗi cái, chạy đúng thứ tự bốn bước và ghi bằng chứng ở bước phát hiện ra nguyên nhân. Sửa bằng cách đổi mã rồi triển khai lại. Bấm giờ từng ca. Lập bảng năm nhóm với dấu hiệu phân biệt để dùng khi trực.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đo năng lực chẩn đoán có phương pháp. Kiểm bằng mười ca; đạt khi chẩn đoán đúng ít nhất tám kèm bằng chứng dẫn ra, và mọi bản sửa đi qua mã chứ thao tác tay.

**Điều kiện đạt.** Chẩn đoán đúng ≥ 8/10 ca kèm bằng chứng dẫn ra, mọi bản sửa đi qua mã, và bảng năm nhóm dấu hiệu phân biệt hoàn chỉnh.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Sửa trực tiếp trên cụm · đọc nhật ký ứng dụng trước khi đọc sự kiện · khởi động lại để xem có hết không · chẩn đoán mà không dẫn bằng chứng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/275-diagnosing-ten-broken-workloads.md`
- Nội dung học thuật: `note.md` cùng thư mục.
