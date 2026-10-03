# Phase 2: Machine, Operating System and Network
# Module 4: Computer Architecture and the Performance Model
# Lesson 51: Virtual memory, page faults and mmap

## Thực hành

**Nhiệm vụ.** Viết chương trình cấp phát dần bộ nhớ vượt RAM khả dụng. Đo số lỗi trang nhẹ và nặng theo thời gian. Ghi lại thời điểm máy bắt đầu hoán đổi và mức chậm đi. Chạy một chương trình tạo tiến trình con và đo chi phí, giải thích bằng sao chép khi ghi.

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài lý thuyết chuẩn bị cho phần chẩn đoán ở M5; chưa đòi xử lý sự cố. Kiểm bằng bài đo cộng nhận dạng; đạt khi phân biệt đúng hai loại lỗi trang và nhận ra đúng trạng thái hoán đổi qua số đo.

**Điều kiện đạt.** Phân biệt đúng hai loại lỗi trang bằng số đo, và chỉ ra đúng thời điểm bắt đầu hoán đổi kèm mức chậm đi.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Nhầm lỗi trang nhẹ với nặng nên hoảng nhầm · tăng bộ nhớ khi nguyên nhân là ánh xạ tệp · bỏ qua tỉ lệ lỗi trang nặng khi chẩn đoán chậm.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/051-virtual-memory-page-faults-and-mmap.md`
- Nội dung học thuật: `note.md` cùng thư mục.
