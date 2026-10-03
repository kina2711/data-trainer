# Phase 1: Engineering Foundation
# Module 2: Python for Production
# Lesson 21: Profiling before optimising

## Thực hành

**Nhiệm vụ.** Nhận một chương trình xử lý dữ liệu chạy chậm. Đo CPU, bộ nhớ và vào ra. Viết dự đoán nút thắt trước khi đo, rồi đối chiếu. Sửa đúng một chỗ, đo lại, ghi mức cải thiện. Chạy lại bộ kiểm để chứng minh kết quả không đổi. Cố ý chạy một phép so sánh sai cách và chỉ ra nó sai ở đâu.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective là truy từ tổng thời gian về một hàm cụ thể bằng dữ liệu đo. Kiểm bằng cặp số đo trước sau; đạt khi định vị đúng nút thắt và cải thiện đo được mà kết quả không đổi.

**Điều kiện đạt.** Định vị đúng nút thắt bằng số đo, cải thiện có số, bộ kiểm vẫn xanh, và chỉ ra được chỗ sai của phép so sánh sai cách.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Tối ưu theo cảm giác · sửa nhiều chỗ cùng lúc · so sánh không có giai đoạn khởi động · tối ưu một hàm chiếm 2% tổng thời gian.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/021-profiling-before-optimising.md`
- Nội dung học thuật: `note.md` cùng thư mục.
