# Phase 9: Cloud Platform and Production Operations
# Module 25: Containers, Infrastructure as Code and Kubernetes
# Lesson 376: Container networking, volumes and the UID mismatch

## Thực hành

**Nhiệm vụ.** Chạy nhiều dịch vụ nối nhau. Truy vết đường đi của một yêu cầu từ máy chủ vào ứng dụng qua ánh xạ cổng và cầu nối; vẽ sơ đồ. Tiêm ba lỗi: sai tên dịch vụ khi phân giải, dữ liệu mất vì không gắn ổ đĩa, và tiến trình không ghi được vì lệch định danh người dùng. Chẩn đoán từng cái bằng số đo chứ đoán.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective gồm một lỗi có triệu chứng gây hiểu nhầm. Kiểm bằng bài truy vết cộng ba lỗi tiêm; đạt khi sơ đồ đường gói khớp truy vết thật và ba lỗi được chẩn đoán đúng nguyên nhân.

**Điều kiện đạt.** Sơ đồ đường gói khớp truy vết thật, và ba lỗi tiêm được chẩn đoán đúng nguyên nhân kèm bằng chứng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Ghi dữ liệu vào lớp ghi của vùng chứa · chẩn đoán quyền bằng tên người dùng thay vì định danh số · mở cổng ra máy chủ khi chỉ cần gọi nội bộ · giả định phân giải tên giữa vùng chứa giống trên máy chủ.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/264-container-networking-volumes-and-the-uid-mismatch.md`
- Nội dung học thuật: `note.md` cùng thư mục.
