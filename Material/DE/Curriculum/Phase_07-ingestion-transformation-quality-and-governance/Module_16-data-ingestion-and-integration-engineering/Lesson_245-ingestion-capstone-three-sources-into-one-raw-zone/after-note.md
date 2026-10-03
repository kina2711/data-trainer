# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 16: Data Ingestion and Integration Engineering
# Lesson 245: Three Source Ingestion Capstone

## Thực hành

**Nhiệm vụ.** Dựng hệ nạp ba nguồn. Chạy khởi tạo, chạy tăng dần bảy ngày, rồi nạp bù 90 ngày có cách ly. Chạy đối soát bốn bậc cho cả ba nguồn. Giết tiến trình ngẫu nhiên trong mỗi chế độ và chứng minh chạy lại phục hồi đúng. Nộp sổ tay vận hành gồm đặt lại điểm kiểm tra, xoay thông tin xác thực, nguồn hỏng và quy trình chạy lại.

Lưu source boundary, fixture hashes, versions, requests/queries, checkpoints, raw outputs, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu entity/change contract.
2. Tái hiện một assumption failure.
3. Chứng minh checkpoint/retry không tạo silent gap.
4. Đối soát bằng key và typed hash.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module thành một hệ vận hành được. Kiểm bằng đối soát độc lập cộng rà soát sổ tay; đạt khi ba nguồn đối soát khớp trong ngân sách chênh lệch đã duyệt và mọi chế độ chạy lại được.

**Điều kiện đạt.** Ba nguồn đối soát khớp trong ngân sách đã duyệt, ba chế độ vận hành chạy được, và giết tiến trình ở mọi chế độ đều phục hồi đúng.

## Bài làm sau buổi học

**Nhiệm vụ.** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Lỗi cần chủ động loại trừ.** Coi lần chạy thành công là bằng chứng đầy đủ · bỏ chế độ nạp bù vì tốn thời gian · để thông tin xác thực trong mã hoặc nhật ký · chạy lại bằng cách xoá đích rồi nạp lại mà không đối soát.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/133-three-source-ingestion-capstone.md`
- Nội dung học thuật: `note.md` cùng thư mục.
