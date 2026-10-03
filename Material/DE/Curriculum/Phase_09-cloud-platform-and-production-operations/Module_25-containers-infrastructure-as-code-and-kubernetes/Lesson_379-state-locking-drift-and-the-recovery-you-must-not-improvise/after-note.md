# Phase 9: Cloud Platform and Production Operations
# Module 25: Containers, Infrastructure as Code and Kubernetes
# Lesson 379: State, locking, drift and the recovery you must not improvise

## Thực hành

**Nhiệm vụ.** Dựng trạng thái từ xa có mã hoá, khoá và phiên bản. Chạy hai lần áp dụng song song và xác nhận bị chặn. Sửa tay một tài nguyên trên đám mây rồi chạy phát hiện trôi; quyết định hoàn tác hay nhập vào mã. Mô phỏng mất tệp trạng thái và phục hồi từ phiên bản trước; đối soát danh sách tài nguyên thật với trạng thái sau phục hồi.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là phục hồi được mà không mất tài nguyên. Kiểm bằng ba tình huống; đạt khi trôi được phát hiện tự động, khoá chặn được áp dụng song song, và phục hồi trạng thái không làm mất hay tạo trùng tài nguyên nào.

**Điều kiện đạt.** Áp dụng song song bị khoá chặn, trôi cấu hình được phát hiện tự động, và phục hồi trạng thái không làm mất hay tạo trùng tài nguyên nào.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Để tệp trạng thái trên máy cá nhân · sửa tay tệp trạng thái mà không sao lưu · bỏ qua trôi cấu hình tới khi lần áp dụng sau hoàn tác nó · để lộ giá trị nhạy cảm trong đầu ra.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/267-state-locking-drift-and-the-recovery-you-must-not-improvise.md`
- Nội dung học thuật: `note.md` cùng thư mục.
