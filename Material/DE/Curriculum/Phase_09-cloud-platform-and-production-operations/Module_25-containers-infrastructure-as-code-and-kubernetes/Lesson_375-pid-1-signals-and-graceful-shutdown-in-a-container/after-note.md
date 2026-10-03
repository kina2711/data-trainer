# Phase 9: Cloud Platform and Production Operations
# Module 25: Containers, Infrastructure as Code and Kubernetes
# Lesson 375: PID 1, signals and graceful shutdown in a container

## Thực hành

**Nhiệm vụ.** Viết một tiến trình xử lý có việc kéo dài vài giây. Đóng gói theo hai cách: chạy trực tiếp và chạy qua một lớp vỏ. Dừng vùng chứa 100 lần ở cả hai cách và đếm số việc bị cắt ngang. Thêm xử lý tín hiệu và tắt có kiểm soát. Kiểm tiến trình con mồ côi. Chuyển sang chạy bằng người dùng không đặc quyền với hệ tệp chỉ đọc.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là không mất việc khi dừng. Kiểm bằng phép thử dừng; đạt khi 100 lần dừng đều hoàn tất việc đang dở, và bản chạy qua lớp vỏ được chứng minh là bị cắt ngang.

**Điều kiện đạt.** 100 lần dừng đều hoàn tất việc đang dở ở bản đúng, và bản chạy qua lớp vỏ được chứng minh bị cắt ngang kèm số việc mất.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chạy tiến trình qua một lớp vỏ nên tín hiệu không tới · không xử lý tín hiệu kết thúc · đặt thời gian chờ ngắn hơn việc dài nhất · chạy bằng người dùng cao nhất.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/263-pid-1-signals-and-graceful-shutdown-in-a-container.md`
- Nội dung học thuật: `note.md` cùng thư mục.
