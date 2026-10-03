# Phase 1: Engineering Foundation
# Module 3: Data Structures and Algorithms for Systems
# Lesson 41: Bloom filters and probabilistic membership

## Thực hành

**Nhiệm vụ.** Cài bộ lọc Bloom. Quét số bit trên mỗi phần tử từ 4 tới 16 và số hàm băm từ 1 tới 8. Với mỗi tổ hợp, đo tỉ lệ trả lời nhầm thật trên một triệu phép hỏi và so với giá trị lý thuyết. Chứng minh bằng thực nghiệm không có trường hợp nào trả lời nhầm là không. Đo phần tiết kiệm khi dùng nó làm bộ lọc trước một phép tìm trên đĩa.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là chọn tham số có công thức rồi xác nhận bằng đo. Kiểm bằng bảng quét tham số; đạt khi tỉ lệ nhầm đo được bám sát lý thuyết và không có lần nào trả lời nhầm là không.

**Điều kiện đạt.** Tỉ lệ nhầm đo được bám sát lý thuyết trên lưới tham số, không có lần nào trả lời nhầm là không, và có số đo phần tiết kiệm.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dùng bộ lọc Bloom khi cần câu trả lời chắc chắn · chọn tham số theo cảm tính · quên rằng không xoá được · bỏ qua chi phí tính k hàm băm.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/041-bloom-filters-probabilistic-membership.md`
- Nội dung học thuật: `note.md` cùng thư mục.
