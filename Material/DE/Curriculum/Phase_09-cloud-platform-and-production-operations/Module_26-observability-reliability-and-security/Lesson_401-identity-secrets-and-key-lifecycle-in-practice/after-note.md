# Phase 9: Cloud Platform and Production Operations
# Module 26: Observability, Reliability and Security
# Lesson 401: Identity, secrets and key lifecycle in practice

## Thực hành

**Nhiệm vụ.** Viết sáu phép thử phủ định gồm truy cập tài nguyên của khách hàng khác qua cả giao diện chính lẫn một đường phụ. Chạy và xác nhận bị chặn. Thực hiện xoay thông tin xác thực khi dịch vụ đang chạy và đo gián đoạn. Thu hồi một mã thông báo trước hạn và chứng minh nó không dùng được nữa. Dùng đường thoát khẩn cấp và xác nhận có cảnh báo cùng bản ghi.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu bằng phép thử phủ định và một thao tác vận hành thật. Kiểm bằng sáu phép thử phủ định cộng một lần xoay; đạt khi cả sáu bị chặn đúng và xoay không gây gián đoạn.

**Điều kiện đạt.** Sáu phép thử phủ định bị chặn đúng gồm cả đường phụ, xoay không gây gián đoạn, và mã thông báo thu hồi trước hạn không dùng được.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Kiểm đăng nhập mà quên kiểm quyền sở hữu tài nguyên · đặt thời hạn mã thông báo dài vì tiện · chưa từng thử xoay · để đường thoát khẩn cấp không sinh cảnh báo.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/289-identity-secrets-and-key-lifecycle-in-practice.md`
- Nội dung học thuật: `note.md` cùng thư mục.
