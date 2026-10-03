# Phase 1: Engineering Foundation
# Module 2: Python for Production
# Lesson 20: Structured logging, correlation and actionable errors

## Thực hành

**Nhiệm vụ.** Thêm nhật ký có cấu trúc và mã theo dõi vào gói. Chạy trên 10.000 bản ghi trong đó có 3 bản lỗi. Với mỗi bản lỗi, truy toàn bộ đường đi chỉ bằng mã theo dõi và dựng lại chuyện đã xảy ra. Kiểm nhật ký không chứa bí mật bằng một phép quét.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một thiết kế kiểm được bằng phép truy ngược thật. Kiểm bằng bài truy ngược; đạt khi truy được đủ đường đi của bản ghi bằng một truy vấn theo mã theo dõi.

**Điều kiện đạt.** Truy được đủ đường đi của cả 3 bản lỗi bằng một truy vấn theo mã theo dõi, và phép quét không tìm thấy bí mật trong nhật ký.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Ghi nhật ký dạng chuỗi tự do · không có mã theo dõi · để mức gỡ lỗi trong sản xuất · ghi cả bản ghi đầy đủ vào nhật ký gồm cả dữ liệu cá nhân.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/020-structured-logging-correlation-actionable-errors.md`
- Nội dung học thuật: `note.md` cùng thư mục.
