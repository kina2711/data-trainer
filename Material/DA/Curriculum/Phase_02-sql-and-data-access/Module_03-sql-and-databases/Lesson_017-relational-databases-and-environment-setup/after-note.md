# Phase 2: Data Analyst
# Module 3: SQL and Databases
# Lesson 17: Relational databases and environment setup

## Thực hành

**Nhiệm vụ.** Cài đặt PostgreSQL và DBeaver. Nạp `DS1` từ script. Chạy `SELECT` đầu tiên. Tự kiểm tra số bảng và số dòng so với giá trị công bố ở phụ lục C.

Giữ input snapshot, grain, identity, version, raw output, reconciliation và limitation.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Bài thiết lập môi trường, đo được trực tiếp bằng trạng thái hệ thống. Kiểm bằng kết quả chạy lệnh: truy vấn đầu tiên trả về đúng số bảng và số dòng của `DS1`. Không kiểm bằng câu hỏi lý thuyết về ACID; phần ACID được kiểm lại ở lesson 33.

**Điều kiện đạt.** `DS1` nạp xong, số bảng bằng 8 và số dòng khớp giá trị ở phụ lục C.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 40 phút đọc nguồn tham chiếu và tự giải thích lại · 25 phút trả lời bốn câu kiểm tra · 15 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Cài bản có thành phần không cần thiết · không ghi lại mật khẩu superuser lúc cài · dùng kiểu chuỗi cho mọi cột.

## Reference
- Knowledge note: `Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/017-relational-databases-and-environment-setup.md`
