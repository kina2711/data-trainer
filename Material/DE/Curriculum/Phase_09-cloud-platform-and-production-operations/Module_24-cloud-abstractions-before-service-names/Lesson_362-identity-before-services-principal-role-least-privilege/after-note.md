# Phase 9: Cloud Platform and Production Operations
# Module 24: Cloud Abstractions before Service Names
# Lesson 362: Identity before services - principal, role, least privilege

## Thực hành

**Nhiệm vụ.** Với ba khối lượng công việc, bắt đầu từ chính sách rỗng và thêm quyền theo từng lỗi từ chối thật; ghi lại lý do cho mỗi quyền. Chuyển toàn bộ sang danh tính cho khối lượng công việc và xoá mọi khoá tĩnh. Chạy sáu phép thử hai chiều và đối chiếu với bản ghi kiểm toán. Chạy một bộ quét chặn khoá tĩnh trong kho mã.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu bằng phép thử hai chiều chứ bằng rà soát chính sách. Kiểm bằng sáu phép thử; đạt khi ba phép thử được phép thành công, ba phép thử bị từ chối đúng, và không khoá tĩnh nào tồn tại trong kho mã.

**Điều kiện đạt.** Ba phép thử được phép thành công và ba phép thử bị từ chối đúng, mỗi quyền có lý do ghi lại, và bộ quét không tìm thấy khoá tĩnh nào.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Bắt đầu bằng ký tự đại diện rồi định thu hẹp sau · dùng tài khoản cao nhất cho việc thường ngày · để khoá tĩnh trong biến môi trường của kho mã · không chạy phép thử bị từ chối.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/250-identity-before-services-principal-role-least-privilege.md`
- Nội dung học thuật: `note.md` cùng thư mục.
