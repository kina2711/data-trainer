# Phase 1: Engineering Foundation
# Module 4: Computer Architecture and the Performance Model
# Lesson 48: Flynn taxonomy - SISD, SIMD, MIMD and where SPMD fits

## Thực hành

**Nhiệm vụ.** Cho tám hệ thống hoặc đoạn mã thật, gồm một vòng lặp véctơ hoá, một bể luồng, một cụm xử lý phân tán, và một engine phân tích. Phân loại từng cái theo bốn khái niệm. Với hai ca có nhiều tầng song song lồng nhau, mô tả từng tầng. Viết một đoạn phân biệt đồng thời với song song bằng một ví dụ của chính mình.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài lý thuyết đặt từ vựng cho năm bài sau; chưa đo gì. Kiểm bằng bài phân loại tám hệ thống; đạt khi phân đúng ít nhất sáu và giải thích được hai ca nằm ở nhiều tầng cùng lúc.

**Điều kiện đạt.** Phân đúng ≥ 6/8 hệ thống, và hai ca song song lồng nhau được mô tả đủ từng tầng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Gọi mọi thứ chạy nhanh là một lệnh nhiều dữ liệu · dùng đồng thời và song song thay nhau · nghĩ một chương trình nhiều dữ liệu là một kiến trúc phần cứng · bỏ qua việc một hệ có thể thuộc nhiều tầng cùng lúc.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/048-flynn-taxonomy-sisd-simd-mimd-spmd.md`
- Nội dung học thuật: `note.md` cùng thư mục.
