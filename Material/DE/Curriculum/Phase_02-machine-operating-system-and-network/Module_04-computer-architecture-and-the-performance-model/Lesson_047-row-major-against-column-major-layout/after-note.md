# Phase 1: Engineering Foundation
# Module 4: Computer Architecture and the Performance Model
# Lesson 47: Row-major against column-major layout

## Thực hành

**Nhiệm vụ.** Dựng cùng dữ liệu 40 cột ở hai bố trí. Chạy hai truy vấn: tính tổng một cột, và đọc nguyên 100 bản ghi. Đo cả bốn ô. Tính tỉ lệ băng thông lãng phí của bố trí theo dòng ở truy vấn thứ nhất và so với chênh lệch thời gian đo được.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi quy chênh lệch đo được về cơ chế nạp dòng đệm. Kiểm bằng bảng đo hai bố trí nhân hai loại truy vấn; đạt khi cả bốn ô có số và giải thích đúng chiều đảo ngược ở truy vấn đọc cả bản ghi.

**Điều kiện đạt.** Bảng bốn ô đủ số đo, tỉ lệ băng thông lãng phí giải thích được chênh lệch, và chiều đảo ngược ở truy vấn thứ hai được chỉ ra.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Kết luận bố trí cột luôn nhanh hơn · so hai bố trí ở hai kích thước dữ liệu khác nhau · bỏ qua truy vấn đọc cả bản ghi nên không thấy chiều ngược.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/047-row-major-vs-column-major-layout.md`
- Nội dung học thuật: `note.md` cùng thư mục.
