# Phase 2: Machine, Operating System and Network
# Module 5: Operating Systems, Concurrency and Linux
# Lesson 64: Filesystems, inodes, file descriptors and leaks

## Thực hành

**Nhiệm vụ.** Tạo tình huống đĩa đầy do tệp đã xoá nhưng còn mở; dùng công cụ hệ thống tìm ra tiến trình giữ nó. Chạy một dịch vụ rò rỉ mô tả tệp, quan sát số mô tả tăng theo thời gian, định vị đoạn mã, sửa bằng trình quản lý ngữ cảnh, và chứng minh số mô tả ổn định sau 10.000 yêu cầu.

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective là hai chẩn đoán cụ thể mà người mới gần như luôn bế tắc. Kiểm bằng hai tình huống tiêm sẵn tính giờ; đạt khi tìm ra nguyên nhân cả hai và sửa được rò rỉ có bằng chứng số mô tả tệp không tăng.

**Điều kiện đạt.** Tìm đúng tiến trình giữ tệp đã xoá, và sau khi sửa thì số mô tả tệp ổn định qua 10.000 yêu cầu.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Xoá tệp rồi tưởng đã giải phóng dung lượng · so hai lệnh đo dung lượng mà không biết vì sao khác nhau · tăng giới hạn mô tả tệp thay vì sửa rò rỉ.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/064-filesystems-inodes-file-descriptors-and-leaks.md`
- Nội dung học thuật: `note.md` cùng thư mục.
