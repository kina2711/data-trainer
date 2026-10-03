# Phase 1: Engineering Foundation
# Module 1: Engineering Thinking, Git and Debugging
# Lesson 7: Collaboration - small commits, review and release discipline

## Thực hành

**Nhiệm vụ.** Chia nhỏ một thay đổi lớn thành bốn commit một mục đích, mỗi commit có thông điệp nói vì sao. Nộp yêu cầu hợp nhất đủ mô tả, phạm vi ảnh hưởng, cách kiểm chứng và ghi chú lùi. Rà soát yêu cầu của một học viên khác theo ba câu hỏi bắt buộc và ghi ít nhất một rủi ro. Tạo một thay đổi có kèm sửa cấu trúc dữ liệu, lùi mã về bản trước, và ghi lại chuyện gì xảy ra với dữ liệu đã đổi. Viết kế hoạch tương thích cho phép mã cũ và mã mới cùng chạy, rồi lùi lại lần nữa và chứng minh lần này lùi được.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là hai vai trong cùng một quy trình, kiểm được bằng sản phẩm của cả hai phía. Kiểm bằng một vòng nộp và rà soát chéo cộng một phép thử lùi; đạt khi yêu cầu đủ bốn phần, bản rà soát nêu được ít nhất một rủi ro thật, và phép thử lùi cho thấy đúng chỗ lùi mã không đủ.

**Điều kiện đạt.** Bốn commit đều một mục đích và có lý do, yêu cầu hợp nhất đủ bốn phần, bản rà soát nêu được ít nhất một rủi ro thật, và phép thử lùi chỉ ra đúng chỗ lùi mã không đủ với kế hoạch tương thích làm lần lùi thứ hai thành công.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Một commit khổng lồ cho cả tính năng · thông điệp commit chép lại tên tệp đã sửa · rà soát chỉ soi phong cách · bỏ ghi chú lùi · coi lùi mã là lùi được toàn bộ khi thay đổi có kèm sửa cấu trúc dữ liệu.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/007-collaboration-small-commits-review-release-discipline.md`
- Nội dung học thuật: `note.md` cùng thư mục.
