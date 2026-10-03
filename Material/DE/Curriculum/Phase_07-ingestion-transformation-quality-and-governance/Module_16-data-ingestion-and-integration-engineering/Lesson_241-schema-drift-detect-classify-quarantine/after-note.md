# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 16: Data Ingestion and Integration Engineering
# Lesson 241: Schema Drift Detection Classification and Quarantine

## Thực hành

**Nhiệm vụ.** Đăng ký lược đồ cho ba nguồn. Tiêm sáu thay đổi thuộc ba mức, gồm thêm cột, bỏ cột, đổi kiểu mở rộng, đổi kiểu thu hẹp, đổi tên, và đổi nghĩa mà giữ kiểu. Chứng minh từng cái được phát hiện, phân đúng mức và đi đúng đường xử lý. Sửa một thay đổi phá vỡ rồi nạp lại từ vùng cách ly và đối soát.

Lưu source boundary, fixture hashes, versions, requests/queries, checkpoints, raw outputs, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu entity/change contract.
2. Tái hiện một assumption failure.
3. Chứng minh checkpoint/retry không tạo silent gap.
4. Đối soát bằng key và typed hash.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu bằng phép thử tiêm ba mức. Kiểm bằng sáu thay đổi tiêm; đạt khi phân loại đúng ít nhất năm và không lô nào bị bỏ im lặng.

**Điều kiện đạt.** Phân loại đúng ≥ 5/6 thay đổi, không lô nào bị bỏ im lặng, và lô cách ly nạp lại được với đối soát khớp.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dừng đường nạp khi chỉ có cột mới · để bước biến đổi phát hiện lệch thay vì bước nạp · bỏ lô hỏng thay vì cách ly · không ghi phiên bản lược đồ vào phong bì.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/129-schema-drift-detection-classification-quarantine.md`
- Nội dung học thuật: `note.md` cùng thư mục.
