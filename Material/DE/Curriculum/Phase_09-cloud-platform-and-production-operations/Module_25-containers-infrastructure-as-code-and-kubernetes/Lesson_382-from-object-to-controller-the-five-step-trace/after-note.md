# Phase 9: Cloud Platform and Production Operations
# Module 25: Containers, Infrastructure as Code and Kubernetes
# Lesson 382: From object to controller - the five-step trace

## Thực hành

**Nhiệm vụ.** Gửi một đối tượng triển khai và theo dõi từng bước bằng sự kiện cùng trạng thái của các đối tượng liên quan. Ghi lại thời gian ở mỗi bước. Tạo ba lần triển khai hỏng ở ba bước khác nhau: bị bộ kiểm nạp từ chối, không lập lịch được, và không kéo được ảnh; với mỗi cái, quy về đúng bước chỉ bằng sự kiện và trạng thái.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi quan sát cơ chế thật thay vì mô tả nó. Kiểm bằng bài truy vết; đạt khi năm bước có bằng chứng quan sát được và ba lần triển khai hỏng được quy đúng bước.

**Điều kiện đạt.** Năm bước có bằng chứng quan sát được kèm thời gian, và ba lần triển khai hỏng được quy đúng bước chỉ bằng sự kiện và trạng thái.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Xem nhật ký ứng dụng trước khi xem sự kiện của đối tượng · giả định hệ khôi phục được trạng thái ứng dụng · sửa bằng cách xoá rồi tạo lại mà không tìm nguyên nhân · bỏ qua bước kiểm nạp khi chẩn đoán.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/270-from-object-to-controller-the-five-step-trace.md`
- Nội dung học thuật: `note.md` cùng thư mục.
