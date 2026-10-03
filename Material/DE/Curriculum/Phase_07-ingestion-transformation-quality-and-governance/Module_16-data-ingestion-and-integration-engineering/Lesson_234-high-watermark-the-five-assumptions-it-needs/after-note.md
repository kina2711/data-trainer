# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 16: Data Ingestion and Integration Engineering
# Lesson 234: High Watermark Assumptions and Overlap Deduplication

## Thực hành

**Nhiệm vụ.** Dựng nguồn có đủ năm ca biên: đồng hồ lùi, sửa không cập nhật mốc, nhiều bản ghi trùng giá trị mốc ở ranh giới, xoá cứng, và lần chạy đầu trên đích rỗng. Cài cửa sổ chồng lấn cộng khử trùng. Tính độ rộng cửa sổ từ độ trễ đo được. Đối soát số dòng, tổng và tập khoá với nguồn sau mỗi ca.

Lưu source boundary, fixture hashes, versions, requests/queries, checkpoints, raw outputs, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu entity/change contract.
2. Tái hiện một assumption failure.
3. Chứng minh checkpoint/retry không tạo silent gap.
4. Đối soát bằng key và typed hash.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là đối soát khớp tuyệt đối qua các ca biên. Kiểm bằng năm ca biên tiêm; đạt khi số dòng và tổng khớp nguồn ở cả năm và quy tắc chọn thắng xác định.

**Điều kiện đạt.** Số dòng, tổng và tập khoá khớp nguồn ở cả năm ca biên, và độ rộng cửa sổ chồng lấn dẫn được từ độ trễ đo được.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dùng điều kiện lớn hơn giá trị lớn nhất mà không có cửa sổ chồng lấn · đặt độ rộng cửa sổ bằng một con số tròn không có căn cứ · khử trùng không có quy tắc chọn thắng xác định · bỏ qua ca đích rỗng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/122-high-watermark-assumptions-overlap-deduplication.md`
- Nội dung học thuật: `note.md` cùng thư mục.
