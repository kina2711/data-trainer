# Phase 9: Cloud Platform and Production Operations
# Module 25: Containers, Infrastructure as Code and Kubernetes
# Lesson 381: Why orchestration, and when a simpler deployment wins

## Thực hành

**Nhiệm vụ.** Triển khai cùng một dịch vụ theo ba cách: máy ảo cùng trình quản lý dịch vụ, dịch vụ vùng chứa được quản lý, và cụm điều phối. Đo thời gian triển khai đầu, thời gian một lần cập nhật, thời gian phục hồi khi mất một máy, và ước lượng giờ công vận hành mỗi tháng. Chọn một cho dự án và nêu hai điều kiện làm lựa chọn đó sai.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective chống lại việc mặc định chọn phương án phức tạp nhất. Kiểm bằng bảng ba cách nhân bốn tiêu chí; đạt khi hai tiêu chí đầu có số đo và lựa chọn kèm hai điều kiện đảo ngược cụ thể.

**Điều kiện đạt.** Ba cách có số đo ở hai tiêu chí đầu cùng ước lượng giờ công vận hành, và lựa chọn kèm hai điều kiện đảo ngược cụ thể.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chọn điều phối vì nó phổ biến · so ba cách mà không tính giờ công vận hành · bỏ qua yêu cầu nâng cấp mặt phẳng điều khiển · khuyến nghị không có điều kiện đảo ngược.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/269-why-orchestration-and-when-a-simpler-deployment-wins.md`
- Nội dung học thuật: `note.md` cùng thư mục.
