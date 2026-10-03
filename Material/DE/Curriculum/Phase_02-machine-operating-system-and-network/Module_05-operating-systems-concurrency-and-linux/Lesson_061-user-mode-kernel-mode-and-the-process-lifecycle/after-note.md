# Phase 2: Machine, Operating System and Network
# Module 5: Operating Systems, Concurrency and Linux
# Lesson 61: User mode, kernel mode and the process lifecycle

## Thực hành

**Nhiệm vụ.** Tạo năm tiến trình ở năm trạng thái khác nhau gồm đang chạy, chờ được cấp CPU, chờ vào ra, dừng, và xác sống. Quan sát trạng thái qua công cụ hệ thống và qua hệ tệp ảo của nhân. Phân loại từng cái. Tạo một tiến trình mồ côi và quan sát nó được nhận nuôi.

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài mở module, đặt từ vựng cho phần chẩn đoán sau. Kiểm bằng bài đọc trạng thái trên năm tiến trình thật; đạt khi phân loại đúng ít nhất bốn và nhận ra đúng tiến trình đang ở trạng thái chờ vào ra không ngắt được.

**Điều kiện đạt.** Phân loại đúng ≥ 4/5 trạng thái, và nhận ra đúng tiến trình đang chờ vào ra không ngắt được.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Nhầm chờ vào ra với chờ CPU nên chẩn đoán sai · không biết trạng thái xác sống nghĩa là gì · dùng lệnh liệt kê tiến trình mà không đọc cột trạng thái.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/061-user-mode-kernel-mode-and-the-process-lifecycle.md`
- Nội dung học thuật: `note.md` cùng thư mục.
