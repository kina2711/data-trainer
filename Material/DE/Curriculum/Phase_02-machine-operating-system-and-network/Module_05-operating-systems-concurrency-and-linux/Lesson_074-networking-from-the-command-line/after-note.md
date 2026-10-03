# Phase 2: Machine, Operating System and Network
# Module 5: Operating Systems, Concurrency and Linux
# Lesson 74: Networking from the command line

## Thực hành

**Nhiệm vụ.** Giảng viên tạo ba lỗi kết nối: tên miền trỏ sai, dịch vụ không nghe cổng, và tường lửa chặn im lặng. Với mỗi lỗi, chạy đủ năm bước theo thứ tự và ghi bước nào phát hiện ra. Liệt kê socket đang mở và chỉ ra trạng thái chờ đóng nếu có.

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective là một quy trình chẩn đoán có thứ tự, chuẩn bị cho M6. Kiểm bằng ba lỗi kết nối tiêm sẵn; đạt khi phân loại đúng ít nhất hai và chỉ ra bước nào trong năm bước phát hiện ra.

**Điều kiện đạt.** Phân loại đúng ≥ 2/3 lỗi và chỉ ra đúng bước phát hiện, kèm bảng socket đang mở có đọc trạng thái.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Bắt gói ngay từ đầu thay vì kiểm phân giải tên trước · nhầm bị từ chối với hết giờ · bỏ qua bước kiểm ai đang nghe cổng · không biết trạng thái socket nghĩa là gì.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/074-networking-from-the-command-line.md`
- Nội dung học thuật: `note.md` cùng thư mục.
