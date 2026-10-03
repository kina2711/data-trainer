# Phase 8: Distributed Systems, Streaming and Compute
# Module 21: Kafka and Event Streaming
# Lesson 333: Security, quota and multi-tenancy

## Thực hành

**Nhiệm vụ.** Bật mã hoá đường truyền và xác thực. Cấp quyền tối thiểu cho hai đội. Chạy phép thử phủ định: mỗi đội thử đọc và ghi chủ đề của đội kia. Đặt hạn mức. Cho một đội đọc lại toàn bộ chủ đề lớn trong khi đội kia đang chạy tải bình thường; đo độ trễ của đội kia trước và trong lúc đọc lại. Xoay thông tin xác thực không gián đoạn.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là cách ly đo được dưới tải. Kiểm bằng phép thử đọc lại; đạt khi bên bị ảnh hưởng giữ độ trễ trong cam kết, và phép thử phủ định về quyền bị chặn hết.

**Điều kiện đạt.** Phép thử phủ định bị chặn hết, độ trễ của đội không liên quan giữ trong cam kết suốt lần đọc lại, và xoay thông tin xác thực không gây gián đoạn.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Cấp quyền theo chủ đề mà quên quyền nhóm · không đặt hạn mức nên một đội chiếm hết băng thông · dùng chung một tài khoản cho nhiều đội · xoay thông tin xác thực bằng cách dừng dịch vụ.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/221-security-quota-and-multi-tenancy.md`
- Nội dung học thuật: `note.md` cùng thư mục.
