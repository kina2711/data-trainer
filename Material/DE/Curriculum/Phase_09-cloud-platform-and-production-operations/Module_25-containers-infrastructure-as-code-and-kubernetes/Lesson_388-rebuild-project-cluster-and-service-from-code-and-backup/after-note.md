# Phase 9: Cloud Platform and Production Operations
# Module 25: Containers, Infrastructure as Code and Kubernetes
# Lesson 388: Rebuild project - cluster and service from code and backup

## Thực hành

**Nhiệm vụ.** Dựng lại toàn bộ trong môi trường sạch, bấm giờ và ghi lại mọi chỗ phải can thiệp tay; mỗi lần can thiệp tay là một thiếu sót phải đưa vào mã rồi làm lại. Phục hồi dữ liệu và đối soát. Thực hiện một lần triển khai và một lần quay lui dưới tải. Bảo vệ bản khai báo: người chấm chỉ vào năm trường bất kỳ và hỏi cơ chế đằng sau.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module thành một phép thử tái tạo. Kiểm bằng dựng lại từ đầu cộng bảo vệ bản khai báo; đạt khi môi trường sạch dựng lại thành công với dữ liệu đối soát khớp, và mọi trường được giải thích bằng cơ chế.

**Điều kiện đạt.** Môi trường sạch dựng lại thành công không can thiệp tay, dữ liệu đối soát khớp, quay lui thử thành công dưới tải, và năm trường bất kỳ được giải thích bằng cơ chế.

## Bài làm sau buổi học

**Nhiệm vụ.** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Lỗi cần chủ động loại trừ.** Chép cấu hình từ môi trường cũ · giữ lại trường trong bản khai báo mà không biết nó làm gì · bỏ bước phục hồi dữ liệu · can thiệp tay rồi không đưa vào mã.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/276-rebuild-project-cluster-and-service-from-code-and-backup.md`
- Nội dung học thuật: `note.md` cùng thư mục.
