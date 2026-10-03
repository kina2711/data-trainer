# Phase 9: Cloud Platform and Production Operations
# Module 24: Cloud Abstractions before Service Names
# Lesson 369: Secrets, keys and the audit trail

## Thực hành

**Nhiệm vụ.** Chuyển toàn bộ thông tin xác thực sang kho bí mật. Thực hiện một lần xoay khi dịch vụ đang chạy và đo gián đoạn. Mã hoá một tập dữ liệu bằng khoá do mình quản lý; thu hồi quyền dùng khoá và chứng minh dữ liệu không đọc được. Tách tài khoản lưu nhật ký. Tiêm ba vi phạm và xác nhận ba phép kiểm tự động chặn được.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là xoay thật và truy vết thật. Kiểm bằng phép thử xoay cộng truy vết; đạt khi xoay không gây gián đoạn, mọi thao tác nhạy cảm truy được trong nhật ký, và ba phép kiểm tự động chặn đúng vi phạm tiêm.

**Điều kiện đạt.** Xoay thông tin xác thực không gây gián đoạn, thao tác nhạy cảm truy được trong nhật ký, và ba vi phạm tiêm đều bị chặn.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Xoay bằng cách dừng dịch vụ · để khoá mã hoá cùng tài khoản với dữ liệu · lưu nhật ký kiểm toán trong chính tài khoản bị kiểm · coi mã hoá khi lưu là đủ khi thiếu kiểm soát khoá.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/257-secrets-keys-and-the-audit-trail.md`
- Nội dung học thuật: `note.md` cùng thư mục.
