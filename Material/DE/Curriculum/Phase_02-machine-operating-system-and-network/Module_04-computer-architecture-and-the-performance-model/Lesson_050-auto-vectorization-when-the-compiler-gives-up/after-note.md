# Phase 1: Engineering Foundation
# Module 4: Computer Architecture and the Performance Model
# Lesson 50: Auto-vectorization - when the compiler gives up

## Thực hành

**Nhiệm vụ.** Viết ba vòng lặp bị từ chối vì ba lý do khác nhau. Bật báo cáo tối ưu hoá và ghi lại lý do từ chối của từng cái. Viết lại từng vòng lặp để gỡ nguyên nhân. Xác nhận trong báo cáo và trong mã máy sinh ra rằng nó đã dùng lệnh véctơ. Đo thời gian trước sau và đối chiếu kết quả tính để chứng minh không đổi.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có bằng chứng hai lớp là báo cáo trình biên dịch và số đo thời gian. Kiểm bằng ba vòng lặp; đạt khi cả ba chuyển từ bị từ chối sang được véctơ hoá với kết quả tính không đổi.

**Điều kiện đạt.** Ba vòng lặp chuyển từ bị từ chối sang được véctơ hoá theo báo cáo, có số đo trước sau, và kết quả tính không đổi.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đoán trình biên dịch có véctơ hoá hay không · viết lệnh đặc thù tập lệnh trước khi đọc báo cáo · sửa vòng lặp mà không kiểm kết quả giữ nguyên · dùng cờ tối ưu hoá làm đổi ngữ nghĩa số thực mà không nói rõ.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/050-auto-vectorization-compiler-gives-up.md`
- Nội dung học thuật: `note.md` cùng thư mục.
