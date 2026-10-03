# Phase 9: Cloud Platform and Production Operations
# Module 25: Containers, Infrastructure as Code and Kubernetes
# Lesson 373: A container is an isolated process

## Thực hành

**Nhiệm vụ.** Chạy một vùng chứa và từ máy chủ tìm tiến trình tương ứng. Kiểm tra bốn không gian tên của nó và so với của máy chủ. Đặt hạn mức bộ xử lý thấp và chạy một tải tính toán; đo mức điều tiết. Đặt hạn mức bộ nhớ thấp và quan sát tiến trình bị kết thúc vì hết bộ nhớ. Ghi lại khác biệt so với chạy trên máy ảo.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài mở module, kiểm bằng quan sát hệ thật chứ bằng lập luận. Kiểm bằng bài quan sát cộng thí nghiệm hạn mức; đạt khi ba không gian tên được chỉ ra bằng công cụ và hiện tượng điều tiết được tái hiện kèm số đo.

**Điều kiện đạt.** Bốn không gian tên được chỉ ra bằng công cụ, và hiện tượng điều tiết cùng bị kết thúc vì hết bộ nhớ được tái hiện kèm số đo.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Coi vùng chứa là máy ảo nhỏ · chạy khối lượng công việc không tin cậy mà không thêm lớp cách ly · không đặt hạn mức nên một vùng chứa ăn hết máy · kết luận chậm mà không kiểm mức điều tiết.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/261-a-container-is-an-isolated-process.md`
- Nội dung học thuật: `note.md` cùng thư mục.
