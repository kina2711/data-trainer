# Phase 9: Cloud Platform and Production Operations
# Module 25: Containers, Infrastructure as Code and Kubernetes
# Lesson 385: Config, secrets, volumes and stateful workloads

## Thực hành

**Nhiệm vụ.** Gắn cấu hình theo cả hai cách và so: cập nhật giá trị rồi xem cách nào cần dựng lại đơn vị chạy. Lấy bí mật từ kho bên ngoài. Kiểm bí mật không xuất hiện trong nhật ký, trong biến môi trường in ra, hay trong đặc tả đối tượng. Chạy một khối lượng công việc có trạng thái ba bản sao; giết một bản và quan sát danh tính cùng ổ đĩa được giữ. Viết một đoạn nêu rõ phần sao chép dữ liệu ai lo.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective gồm một giới hạn phải phát biểu đúng. Kiểm bằng phép thử cập nhật cộng bài lập luận; đạt khi cấu hình cập nhật được không dựng lại đơn vị chạy, bí mật không lộ trong nhật ký hay danh sách tiến trình, và giới hạn về sao chép dữ liệu được nêu đúng.

**Điều kiện đạt.** Cấu hình cập nhật được không dựng lại đơn vị chạy, bí mật không lộ ở cả ba nơi kiểm, và giới hạn về sao chép dữ liệu được nêu đúng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đưa bí mật vào biến môi trường rồi in ra nhật ký · tin bí mật ở dạng mặc định đã được mã hoá thật · nghĩ chạy cơ sở dữ liệu theo dạng có trạng thái là đã có sẵn sàng cao · gắn ổ đĩa chung cho nhiều bản sao cần ghi.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/273-config-secrets-volumes-and-stateful-workloads.md`
- Nội dung học thuật: `note.md` cùng thư mục.
