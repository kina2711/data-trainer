# Phase 1: Engineering Foundation
# Module 2: Python for Production
# Lesson 26: Structured concurrency - TaskGroup, ownership and cancellation safety

## Thực hành

**Nhiệm vụ.** Viết một dịch vụ mở 50 tác vụ con trong một phạm vi có cấu trúc. Chạy ba kịch bản: một tác vụ con ném ngoại lệ, phạm vi bị huỷ từ ngoài, và nhận tín hiệu tắt. Sau mỗi kịch bản, đếm tác vụ còn sống và bộ mô tả tệp còn mở. Viết một bản không có cấu trúc để so và định lượng số tác vụ mồ côi.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu đếm được là số tác vụ còn sống và số tài nguyên chưa đóng. Kiểm bằng ba kịch bản tắt; đạt khi số tác vụ còn sống bằng không và số kết nối rò bằng không ở cả ba.

**Điều kiện đạt.** Số tác vụ còn sống và số kết nối rò đều bằng không ở cả ba kịch bản, và bản không có cấu trúc được định lượng số tác vụ mồ côi.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Tạo tác vụ rời rồi quên · nuốt tín hiệu huỷ để chạy nốt · dọn dẹp mà không che chắn nên bị huỷ giữa chừng · rời phạm vi khi tác vụ con còn chạy.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/026-structured-concurrency-taskgroup-ownership-cancellation.md`
- Nội dung học thuật: `note.md` cùng thư mục.
