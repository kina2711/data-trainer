# Phase 10: System Design, AI Boundary and Trajectory
# Module 27: System Design Progression
# Lesson 410: Sequence 2 - replicated and partitioned

## Thực hành

**Nhiệm vụ.** Thiết kế dịch vụ thông báo nhiều kênh. Chọn cách phân vùng và cách sao chép kèm lý do. Trả lời ba câu hỏi. Tính lượng dữ liệu mất tối đa từ độ trễ sao chép. Mô tả quy trình tái phân bố có giới hạn tốc độ. Nêu chính sách khử trùng và yêu cầu về thứ tự mà người dùng quan sát được.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective đòi nối lựa chọn sao chép với một con số rủi ro. Kiểm bằng rà soát thiết kế; đạt khi ba câu hỏi có câu trả lời cụ thể, lượng dữ liệu mất tối đa tính được, và cách xử lý khoá nóng được nêu.

**Điều kiện đạt.** Ba câu hỏi có câu trả lời cụ thể, lượng dữ liệu mất tối đa tính được từ độ trễ sao chép, và quy trình tái phân bố có giới hạn tốc độ.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Nói thêm bản sao mà không nói đồng bộ hay bất đồng bộ · bỏ qua ảnh hưởng của tái phân bố lên dịch vụ đang chạy · giả định thứ tự toàn cục · không nêu hành vi khi đọc phải bản sao cũ.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/298-sequence-2-replicated-and-partitioned.md`
- Nội dung học thuật: `note.md` cùng thư mục.
