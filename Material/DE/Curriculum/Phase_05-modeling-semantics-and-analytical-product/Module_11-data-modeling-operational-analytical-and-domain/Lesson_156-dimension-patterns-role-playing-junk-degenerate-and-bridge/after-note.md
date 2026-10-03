# Phase 5: Modeling, Semantics and Analytical Product
# Module 11: Data Modeling - Operational, Analytical and Domain
# Lesson 156: Dimension patterns - role-playing, junk, degenerate and bridge

## Thực hành

**Nhiệm vụ.** Cho một lược đồ có cả bốn mẫu. Nhận dạng từng cái. Viết truy vấn gộp qua bảng cầu theo hai cách: không có hệ số phân bổ và có hệ số; so hai kết quả với tổng thật. Tạo khung nhìn chiều vai trò cho ngày đặt và ngày giao.

Chỉ chạy profiling, merge/backfill hoặc schema experiments trên dataset thử nghiệm/versioned snapshot. Không sửa identity mapping, history, keys hoặc production mart để minh họa. Lưu input snapshot, SQL/notebook, assumptions, counts/control totals và diff trước–sau.

## Kiểm tra cuối bài

1. Phát biểu grain và invariant chính.
2. Nêu phản ví dụ làm thiết kế sai cho kết quả hợp lệ cú pháp.
3. Chỉ ra phần nào là source fact và phần nào là curriculum synthesis.
4. Đề xuất phép kiểm dữ liệu tái chạy được.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective gồm một ca dễ sai âm thầm là bảng cầu. Kiểm bằng bài nhận dạng cộng phép đối soát; đạt khi nhận đúng ít nhất ba mẫu và tổng qua bảng cầu khớp tổng thật.

**Điều kiện đạt.** Nhận đúng ≥ 3/4 mẫu, và tổng gộp qua bảng cầu có hệ số phân bổ khớp tổng thật.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Gộp qua bảng cầu mà không phân bổ · tạo một chiều riêng cho mỗi cờ nhị phân · tách mã hoá đơn thành một chiều không có thuộc tính · dùng cùng tên cột cho hai vai của một chiều.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/44-dimension-patterns-role-playing-junk-degenerate-bridge.md`
- Nội dung học thuật: `note.md` cùng thư mục.
