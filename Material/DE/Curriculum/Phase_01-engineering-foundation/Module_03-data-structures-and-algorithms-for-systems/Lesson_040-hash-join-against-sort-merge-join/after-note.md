# Phase 1: Engineering Foundation
# Module 3: Data Structures and Algorithms for Systems
# Lesson 40: Hash join against sort-merge join

## Thực hành

**Nhiệm vụ.** Cài phép kết băm và phép kết sắp xếp trộn. Đo thời gian trên lưới gồm ba kích thước dữ liệu nhân hai mức bộ nhớ. Thêm một khoá chiếm 60% dữ liệu và đo lại cả hai. Chạy lại phép kết sắp xếp trộn trên dữ liệu đã sắp xếp sẵn và ghi phần chênh.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi xác định điều kiện áp dụng của hai thuật toán bằng thực nghiệm, chuẩn bị trực tiếp cho M9. Kiểm bằng bảng ba yếu tố; đạt khi tìm ra điểm giao theo ít nhất hai yếu tố và giải thích đúng cơ chế suy giảm.

**Điều kiện đạt.** Tìm được điểm giao theo ≥ 2 yếu tố kèm số đo, và giải thích đúng vì sao phép kết băm suy giảm khi khoá lệch.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Kết luận một cách luôn nhanh hơn · bỏ qua bộ nhớ khi so · không thử dữ liệu lệch khoá · quên rằng dữ liệu đã sắp xếp đổi hẳn kết luận.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/040-hash-join-vs-sort-merge-join.md`
- Nội dung học thuật: `note.md` cùng thư mục.
