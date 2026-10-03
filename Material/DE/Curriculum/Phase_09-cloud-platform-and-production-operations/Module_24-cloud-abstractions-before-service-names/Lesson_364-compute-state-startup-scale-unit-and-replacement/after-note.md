# Phase 9: Cloud Platform and Production Operations
# Module 24: Cloud Abstractions before Service Names
# Lesson 364: Compute - state, startup, scale unit and replacement

## Thực hành

**Nhiệm vụ.** Cho ba khối lượng công việc; trả lời bốn câu hỏi cho từng cái rồi chọn dạng tính toán. Triển khai một cái theo nhóm tự mở rộng dùng ảnh bất biến. Giết một đơn vị và đo thời gian tới khi đơn vị thay thế phục vụ được. Chứng minh không có trạng thái nằm lại trên đơn vị bị giết. Đo khởi động nguội của một hàm không máy chủ.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu bằng diễn tập mất máy. Kiểm bằng phép thử giết; đạt khi dịch vụ tự thay thế đơn vị đã mất và không dữ liệu nào nằm lại trên đơn vị đó.

**Điều kiện đạt.** Đơn vị bị giết được thay thế tự động với thời gian đo được, và không dữ liệu nào nằm lại trên đơn vị đó.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Lưu trạng thái trên đĩa cục bộ của máy tự mở rộng · sửa cấu hình trên máy đang chạy thay vì dựng ảnh mới · chọn hàm không máy chủ cho việc chạy dài · bỏ qua khởi động nguội khi hứa độ trễ.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/252-compute-state-startup-scale-unit-and-replacement.md`
- Nội dung học thuật: `note.md` cùng thư mục.
