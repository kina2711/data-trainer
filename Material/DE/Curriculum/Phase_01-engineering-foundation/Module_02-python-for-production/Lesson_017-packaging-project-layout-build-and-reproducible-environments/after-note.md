# Phase 1: Engineering Foundation
# Module 2: Python for Production
# Lesson 17: Packaging - project layout, build and reproducible environments

## Thực hành

**Nhiệm vụ.** Chuyển công cụ CSV ở lesson 11 thành gói có tệp cấu hình dự án. Tạo môi trường ảo và khoá phiên bản. Dựng gói nguồn và gói dựng sẵn. Đưa cho một học viên khác cài trên máy trống từ gói dựng sẵn, chạy, và ghi lại mọi chỗ họ phải hỏi.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là tiêu chí *clone, một lệnh, cùng kết quả* ở mức gói. Kiểm bằng phép thử tái tạo do người khác chạy; đạt khi họ cài và chạy được mà không phải sửa gì.

**Điều kiện đạt.** Người khác cài từ gói dựng sẵn và chạy được trên máy trống mà không phải sửa gì, và môi trường tái tạo cho cùng danh sách phiên bản.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Không khoá phiên bản · để cấu hình đường dẫn tuyệt đối của máy mình · đặt bí mật trong tệp cấu hình rồi nộp vào kho · nhập tương đối lung tung gây nhập vòng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/017-packaging-project-layout-reproducible-environments.md`
- Nội dung học thuật: `note.md` cùng thư mục.
