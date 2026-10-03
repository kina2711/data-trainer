# Phase 2: Machine, Operating System and Network
# Module 5: Operating Systems, Concurrency and Linux
# Lesson 72: Distinguishing four kinds of system pressure

## Thực hành

**Nhiệm vụ.** Giảng viên tạo lần lượt bốn loại tải trên một máy, mỗi lần 8 phút. Với mỗi lần, chạy quy trình bốn bước, ghi bộ chỉ số, và kết luận. Với tình huống đĩa đầy, xác định thêm nguyên nhân là tệp thật hay tệp đã xoá còn mở.

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective là chẩn đoán dưới áp lực thời gian, đúng điều kiện khi trực. Kiểm bằng bốn tình huống tiêm sẵn, mỗi tình huống 8 phút; đạt khi chẩn đoán đúng ít nhất ba và mỗi lần dẫn được hai chỉ số nhất quán.

**Điều kiện đạt.** Chẩn đoán đúng ≥ 3/4 tình huống trong giới hạn thời gian, mỗi lần dẫn được hai chỉ số nhất quán.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Kết luận từ một chỉ số · chạy mọi lệnh rồi vẫn không kết luận · nhầm bộ nhớ trống thấp với áp lực bộ nhớ · bỏ qua bước xác định nguyên nhân sâu hơn.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/072-distinguishing-four-kinds-of-system-pressure.md`
- Nội dung học thuật: `note.md` cùng thư mục.
