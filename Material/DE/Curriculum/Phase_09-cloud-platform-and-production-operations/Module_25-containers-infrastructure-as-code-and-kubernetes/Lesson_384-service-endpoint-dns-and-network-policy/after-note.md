# Phase 9: Cloud Platform and Production Operations
# Module 25: Containers, Infrastructure as Code and Kubernetes
# Lesson 384: Service, endpoint, DNS and network policy

## Thực hành

**Nhiệm vụ.** Tiêm bốn sự cố: nhãn không khớp bộ chọn, sai cổng, tên dịch vụ sai, và một đơn vị chạy chưa sẵn sàng. Với mỗi cái, chạy chuỗi chẩn đoán theo thứ tự và ghi bằng chứng ở mỗi bước. Đặt chính sách mạng từ chối mặc định rồi mở đúng các đường cần thiết; chạy phép thử phủ định cho mọi cặp dịch vụ.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có một chuỗi chẩn đoán có thứ tự và một cấu hình bảo mật kiểm được. Kiểm bằng bốn sự cố tiêm cộng phép thử phủ định; đạt khi cả bốn được chẩn đoán đúng nguyên nhân và chính sách từ chối mặc định chặn đúng mọi kết nối không được phép.

**Điều kiện đạt.** Bốn sự cố được chẩn đoán đúng theo thứ tự chuỗi, và chính sách từ chối mặc định chặn đúng mọi kết nối không được phép trong phép thử phủ định.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Xem nhật ký ứng dụng trước khi kiểm danh sách điểm cuối · nhầm cổng dịch vụ với cổng vùng chứa · để chính sách mạng mặc định cho phép mọi thứ · sửa bằng cách khởi động lại.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/272-service-endpoint-dns-and-network-policy.md`
- Nội dung học thuật: `note.md` cùng thư mục.
