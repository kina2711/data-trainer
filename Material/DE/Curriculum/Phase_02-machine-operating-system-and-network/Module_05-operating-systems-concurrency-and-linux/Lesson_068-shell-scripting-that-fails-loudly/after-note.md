# Phase 2: Machine, Operating System and Network
# Module 5: Operating Systems, Concurrency and Linux
# Lesson 68: Shell scripting that fails loudly

## Thực hành

**Nhiệm vụ.** Viết script nạp dữ liệu có tạo thư mục tạm, tải tệp, xử lý, rồi dọn. Tiêm năm lỗi: lệnh thất bại giữa chừng, biến chưa đặt, lỗi trong đường ống, tên tệp có dấu cách, và bị dừng giữa chừng. Chứng minh cả năm được xử lý đúng và thư mục tạm luôn được dọn.

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một tập quy tắc kiểm được bằng thí nghiệm tiêm lỗi. Kiểm bằng năm lỗi tiêm; đạt khi cả năm đều làm script dừng với mã thoát khác không và tài nguyên tạm được dọn.

**Điều kiện đạt.** Năm lỗi đều làm script dừng với mã thoát khác không, và thư mục tạm được dọn trong cả năm trường hợp.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Quên ngoặc kép quanh biến · tin tuỳ chọn dừng khi lỗi bắt được mọi trường hợp · không dọn khi bị dừng giữa chừng · viết 500 dòng shell cho việc cần Python.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/068-shell-scripting-that-fails-loudly.md`
- Nội dung học thuật: `note.md` cùng thư mục.
