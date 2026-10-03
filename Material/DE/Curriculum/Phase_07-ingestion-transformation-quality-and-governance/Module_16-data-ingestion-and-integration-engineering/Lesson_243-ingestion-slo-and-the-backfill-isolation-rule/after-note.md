# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 16: Data Ingestion and Integration Engineering
# Lesson 243: Ingestion SLO and Backfill Isolation Rule

## Thực hành

**Nhiệm vụ.** Dựng bộ bảy chỉ số và đặt cam kết cho ba chỉ số quan trọng nhất. Chạy nạp bù 90 phân vùng đồng thời với lần chạy hằng ngày, có hạn mức và hàng đợi riêng. Đo độ tươi hằng ngày và tải nguồn suốt quá trình. Dừng nạp bù giữa chừng và chứng minh chạy tiếp được từ điểm kiểm tra. Tạo một tình huống sáu chỉ số xanh mà chênh lệch đối soát đỏ.

Lưu source boundary, fixture hashes, versions, requests/queries, checkpoints, raw outputs, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu entity/change contract.
2. Tái hiện một assumption failure.
3. Chứng minh checkpoint/retry không tạo silent gap.
4. Đối soát bằng key và typed hash.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là cam kết hằng ngày giữ được trong lúc nạp bù. Kiểm bằng thí nghiệm chạy song song; đạt khi độ tươi hằng ngày trong cam kết suốt thời gian nạp bù và nguồn không vượt hạn mức.

**Điều kiện đạt.** Độ tươi hằng ngày trong cam kết suốt 90 phân vùng nạp bù, nguồn không vượt hạn mức, và nạp bù tiếp được từ điểm kiểm tra.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chạy nạp bù chung hàng đợi với lần chạy hằng ngày · đặt cam kết theo năng lực hiện có · cảnh báo trên chỉ số không hành động được · nạp bù không có điểm kiểm tra nên dừng là mất hết.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/131-ingestion-slo-backfill-isolation.md`
- Nội dung học thuật: `note.md` cùng thư mục.
