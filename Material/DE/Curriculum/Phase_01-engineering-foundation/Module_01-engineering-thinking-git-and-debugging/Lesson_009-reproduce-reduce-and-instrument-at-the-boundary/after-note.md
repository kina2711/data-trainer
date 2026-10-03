# Phase 1: Engineering Foundation
# Module 1: Engineering Thinking, Git and Debugging
# Lesson 9: Reproduce, reduce and instrument at the boundary

## Thực hành

**Nhiệm vụ.** Nhận một chương trình xử lý CSV có ba lỗi tiêm sẵn: một dòng sai định dạng, một tình huống hết chỗ trống trên đĩa mô phỏng, và một lỗi thiếu quyền. Với mỗi lỗi, tái hiện xác định, thu nhỏ đầu vào, thêm ghi nhật ký ở ranh giới, và nộp bảng giả thuyết có ít nhất ba dòng bị bác bỏ.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective là truy từ triệu chứng về nguyên nhân bằng bằng chứng, kỹ năng nền cho mọi module sau. Kiểm bằng ba lỗi tiêm sẵn; đạt khi chứng minh đúng nguyên nhân ít nhất hai và trường hợp nhỏ nhất thật sự nhỏ.

**Điều kiện đạt.** Chứng minh đúng nguyên nhân ≥ 2/3 lỗi, mỗi lần có ≥ 3 giả thuyết bị bác bỏ bằng bằng chứng, và trường hợp nhỏ nhất dưới 20 dòng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Rải lệnh in khắp mã thay vì đặt ở ranh giới · kết luận lỗi ngẫu nhiên khi chưa cố định biến · thu nhỏ bằng cách xoá mã tới khi không chạy nữa · sửa khi chưa tái hiện được.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/009-reproduce-reduce-instrument-boundary.md`
- Nội dung học thuật: `note.md` cùng thư mục.
