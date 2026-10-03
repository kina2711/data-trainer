# Phase 2: Machine, Operating System and Network
# Module 5: Operating Systems, Concurrency and Linux
# Lesson 67: Signals, exit codes and graceful shutdown

## Thực hành

**Nhiệm vụ.** Viết tiến trình xử lý hàng đợi. Cài bắt tín hiệu dừng, hoàn tất việc đang dở, đẩy dữ liệu xuống đĩa rồi thoát. Gửi tín hiệu dừng 20 lần ở thời điểm ngẫu nhiên và đối soát kết quả. Gửi tín hiệu giết cứng và ghi lại khác biệt. Kiểm mã thoát ở ba trường hợp thành công, thất bại và bị giết.

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một cơ chế kiểm được bằng thí nghiệm dừng. Kiểm bằng 20 lần gửi tín hiệu ở thời điểm ngẫu nhiên; đạt khi không lần nào mất việc và mã thoát đúng ở mọi trường hợp.

**Điều kiện đạt.** 20 lần gửi tín hiệu dừng đều không mất việc đang dở, và mã thoát đúng ở cả ba trường hợp.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Không bắt tín hiệu nên bị giết giữa lúc ghi · dọn dẹp quá lâu rồi bị giết cứng · trả mã thoát không khi thực ra thất bại · dùng shell làm tiến trình chính nên tín hiệu không tới được chương trình.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/067-signals-exit-codes-and-graceful-shutdown.md`
- Nội dung học thuật: `note.md` cùng thư mục.
