# Phase 8: Distributed Systems, Streaming and Compute
# Module 20: Distributed Systems Fundamentals
# Lesson 311: Time and order - wall clock, monotonic clock and logical clocks

## Thực hành

**Nhiệm vụ.** Dựng kho khoá giá trị hai bản sao. Đặt lệch đồng hồ giữa hai nút. Ghi song song và đếm số cập nhật bị mất với chiến lược dấu thời gian lớn nhất thắng. Cài đồng hồ logic rồi đồng hồ véctơ; chứng minh đồng hồ véctơ phân biệt được đồng thời với nhân quả. Chọn một chính sách giải quyết xung đột tường minh và nêu nó mất thông tin gì.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi nhận ra một lỗi không báo lỗi và sửa bằng cơ chế đúng. Kiểm bằng thí nghiệm lệch đồng hồ; đạt khi số cập nhật bị mất được định lượng và bản dùng đồng hồ véctơ phát hiện đúng mọi cặp sự kiện đồng thời.

**Điều kiện đạt.** Số cập nhật bị mất được định lượng, đồng hồ véctơ phát hiện đúng mọi cặp đồng thời, và chính sách xung đột nêu rõ thông tin bị mất.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dùng đồng hồ treo tường để xác lập thứ tự · dùng đồng hồ đơn điệu để so giữa hai máy · để chính sách xung đột theo mặc định · nghĩ đồng hồ logic đơn phát hiện được đồng thời.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/199-time-and-order-wall-clock-monotonic-clock-and-logical-clocks.md`
- Nội dung học thuật: `note.md` cùng thư mục.
