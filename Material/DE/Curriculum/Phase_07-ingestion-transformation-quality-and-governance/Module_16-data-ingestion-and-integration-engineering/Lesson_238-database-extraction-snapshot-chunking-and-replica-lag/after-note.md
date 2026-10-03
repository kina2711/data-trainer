# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 16: Data Ingestion and Integration Engineering
# Lesson 238: Database Snapshot Chunking and Replica Boundary

## Thực hành

**Nhiệm vụ.** Trích xuất một bảng lớn theo lô chia bằng khoá có chỉ mục, kích thước lô điều chỉnh động. Đo trên nguồn: thời gian truy vấn, số kết nối, độ dài giao dịch mở và mức phình phiên bản. So với một bản chia theo độ lệch. Chuyển sang trích xuất từ bản sao, tạo độ trễ nhân tạo và chứng minh ranh giới tính theo trạng thái bản sao cho kết quả đúng.

Lưu source boundary, fixture hashes, versions, requests/queries, checkpoints, raw outputs, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu entity/change contract.
2. Tái hiện một assumption failure.
3. Chứng minh checkpoint/retry không tạo silent gap.
4. Đối soát bằng key và typed hash.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có hai ràng buộc: đúng dữ liệu và không hại nguồn. Kiểm bằng cặp số đo; đạt khi đối soát khớp nguồn tại ranh giới đã chốt và mọi số đo tác động nằm dưới ngưỡng thoả thuận.

**Điều kiện đạt.** Đối soát khớp nguồn tại ranh giới đã chốt, và mọi số đo tác động lên nguồn dưới ngưỡng thoả thuận.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chia lô theo độ lệch · giữ một giao dịch mở suốt lần trích xuất · tính ranh giới theo đồng hồ khi đọc từ bản sao · không đo tác động lên nguồn.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/126-database-snapshot-chunking-replica-boundary.md`
- Nội dung học thuật: `note.md` cùng thư mục.
