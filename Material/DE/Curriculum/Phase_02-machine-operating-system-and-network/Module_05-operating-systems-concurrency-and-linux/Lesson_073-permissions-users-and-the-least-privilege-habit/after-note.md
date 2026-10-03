# Phase 2: Machine, Operating System and Network
# Module 5: Operating Systems, Concurrency and Linux
# Lesson 73: Permissions, users and the least-privilege habit

## Thực hành

**Nhiệm vụ.** Chạy dịch vụ ở lesson 69 bằng người dùng riêng. Đặt quyền tối thiểu cho thư mục dữ liệu và tệp cấu hình. Thử đọc, ghi và thực thi bằng một tài khoản khác và ghi lại kết quả cả ba. Đặt mặt nạ tạo tệp và kiểm tệp mới sinh ra có quyền đúng.

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một cấu hình bảo mật kiểm được bằng phép thử phủ định. Kiểm bằng ba phép thử truy cập trái phép; đạt khi cả ba bị từ chối và dịch vụ vẫn chạy đúng.

**Điều kiện đạt.** Ba phép thử truy cập trái phép đều bị từ chối, dịch vụ vẫn chạy đúng, và tệp mới sinh ra có quyền đúng theo mặt nạ.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chạy dịch vụ bằng quyền quản trị cho tiện · đặt quyền mở cho mọi người để hết lỗi · quên mặt nạ tạo tệp nên tệp mới sai quyền · đặt quyền mà không thử truy cập trái phép.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/073-permissions-users-and-the-least-privilege-habit.md`
- Nội dung học thuật: `note.md` cùng thư mục.
