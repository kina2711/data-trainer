# Phase 9: Cloud Platform and Production Operations
# Module 25: Containers, Infrastructure as Code and Kubernetes
# Lesson 380: Modules, environments and the plan review

## Thực hành

**Nhiệm vụ.** Tách mã thành mô đun có kiểm tra đầu vào và ghim phiên bản nhà cung cấp. Dựng quy trình hiển thị kế hoạch trong yêu cầu hợp nhất, chạy kiểm chính sách và ước tính chi phí. Tiêm ba cấu hình cấm gồm mở công khai, chính sách dùng ký tự đại diện, và một hành động thay thế cơ sở dữ liệu. Xác nhận bị chặn. Áp dụng ở môi trường sản xuất có phê duyệt và lưu hiện vật.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một cửa chặn tự động cộng một cửa chặn người. Kiểm bằng ba vi phạm tiêm; đạt khi cả ba bị kiểm chính sách chặn và mọi lần áp dụng ở môi trường sản xuất đều có dấu phê duyệt cùng hiện vật lưu lại.

**Điều kiện đạt.** Ba cấu hình cấm bị chặn bởi kiểm chính sách, và mọi lần áp dụng ở sản xuất có dấu phê duyệt cùng hiện vật lưu lại.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Sao chép mã giữa các môi trường thay vì dùng mô đun · dùng thông tin xác thực cá nhân cho quy trình tự động · áp dụng ở sản xuất không cần phê duyệt · không ghim phiên bản nhà cung cấp.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/268-modules-environments-and-the-plan-review.md`
- Nội dung học thuật: `note.md` cùng thư mục.
