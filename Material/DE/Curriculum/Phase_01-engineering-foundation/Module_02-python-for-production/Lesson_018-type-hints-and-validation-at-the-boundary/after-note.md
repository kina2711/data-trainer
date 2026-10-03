# Phase 1: Engineering Foundation
# Module 2: Python for Production
# Lesson 18: Type hints and validation at the boundary

## Thực hành

**Nhiệm vụ.** Thêm chú thích kiểu cho gói ở lesson 17 tới khi bộ kiểm tĩnh sạch. Thêm xác thực lúc chạy tại ranh giới đọc tệp. Đưa vào 10 bản ghi sai hình dạng và chứng minh cả 10 bị chặn ở ranh giới với thông báo nêu rõ trường nào sai. Chứng minh mã bên trong không còn kiểm lại kiểu.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective gồm hai cơ chế khác nhau mà người học hay gộp làm một. Kiểm bằng bộ kiểm tĩnh cộng thí nghiệm dữ liệu bẩn; đạt khi bộ kiểm sạch và dữ liệu sai hình dạng bị chặn ngay tại ranh giới.

**Điều kiện đạt.** Bộ kiểm tĩnh sạch, 10 bản ghi sai đều bị chặn tại ranh giới với thông báo nêu đúng trường, và mã bên trong không kiểm lại kiểu.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Tưởng chú thích kiểu kiểm được dữ liệu lúc chạy · xác thực rải khắp mã · dùng từ điển cho bản ghi có cấu trúc · tắt bộ kiểm tĩnh vì nhiều cảnh báo.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/018-type-hints-validation-boundary.md`
- Nội dung học thuật: `note.md` cùng thư mục.
