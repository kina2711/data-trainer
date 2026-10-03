# Phase 2: Machine, Operating System and Network
# Module 4: Computer Architecture and the Performance Model
# Lesson 55: Amdahl, Gustafson and why adding threads stops helping

## Thực hành

**Nhiệm vụ.** Cho bốn chương trình không tăng tốc khi thêm luồng, mỗi cái một nguyên nhân. Với mỗi cái, đo mức dùng lõi, thời gian chờ vào ra, thời gian chờ khoá và băng thông bộ nhớ, rồi chẩn đoán. Với chương trình bị giới hạn bởi phần tuần tự, ước lượng tỉ lệ phần đó từ đồ thị tăng tốc.

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi phân biệt bốn nguyên nhân có biểu hiện bề ngoài giống nhau. Kiểm bằng bốn chương trình tiêm sẵn; đạt khi chẩn đoán đúng ít nhất ba và mỗi lần dẫn được số đo phân biệt.

**Điều kiện đạt.** Chẩn đoán đúng ≥ 3/4 chương trình kèm số đo phân biệt, ước lượng được tỉ lệ phần tuần tự từ đồ thị, và mọi kết luận về tăng tốc đều kèm hiệu suất song song.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Kết luận thiếu CPU vì thấy CPU cao · bỏ qua băng thông bộ nhớ · thêm luồng cho tác vụ chờ đĩa · không đo thời gian chờ khoá.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/055-amdahl-gustafson-and-why-adding-threads-stops-helping.md`
- Nội dung học thuật: `note.md` cùng thư mục.
