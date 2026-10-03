# Phase 10: System Design, AI Boundary and Trajectory
# Module 28: Modern AI Engineering, Bounded
# Lesson 427: Baseline first - when simple search beats retrieval augmentation

## Thực hành

**Nhiệm vụ.** Dựng ba đường cơ sở cho cùng bài toán. Đo trên cùng tập đối chứng với cùng số đo ở lesson 426. Dựng phương án tăng cường truy hồi và đo lại. Tính chi phí trên mỗi truy vấn và số thành phần phải vận hành cho từng phương án. Kết luận bằng cặp cải thiện với chi phí. Tìm một loại câu hỏi mà đường cơ sở thắng.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi biện minh độ phức tạp chứ mặc định chọn nó. Kiểm bằng bài so; đạt khi ba đường cơ sở có số đo trên cùng tập đối chứng, và quyết định dùng hay không dùng phương án phức tạp dẫn được từ cặp cải thiện với chi phí.

**Điều kiện đạt.** Ba đường cơ sở có số đo trên cùng tập đối chứng, quyết định dẫn từ cặp cải thiện với chi phí, và một loại câu hỏi mà đường cơ sở thắng được chỉ ra.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Bắt đầu từ phương án phức tạp nhất · so hai phương án trên hai tập dữ liệu khác nhau · bỏ chi phí vận hành khỏi so sánh · kết luận bằng cảm nhận về chất lượng câu trả lời.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/315-baseline-first-when-simple-search-beats-retrieval-augmentation.md`
- Nội dung học thuật: `note.md` cùng thư mục.
