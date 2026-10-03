# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 16: Data Ingestion and Integration Engineering
# Lesson 237: File Drop Delivery and Arrival Completeness Protocol

## Thực hành

**Nhiệm vụ.** Cài giao thức bốn bước cho bên gửi và bên nhận. Tiêm bốn ca: tải lên dở dang, tệp trùng tên khác nội dung, tệp hỏng, và lô thiếu một tệp so với kê khai. Chứng minh từng ca bị phát hiện và đi đúng đường xử lý. Chứng minh lô thiếu tệp không được đánh dấu hoàn tất. Đo hiệu ứng của việc gom tệp nhỏ trước khi ghi vùng thô.

Lưu source boundary, fixture hashes, versions, requests/queries, checkpoints, raw outputs, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu entity/change contract.
2. Tái hiện một assumption failure.
3. Chứng minh checkpoint/retry không tạo silent gap.
4. Đối soát bằng key và typed hash.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective đòi phân biệt tệp đã tới với lô đã đủ. Kiểm bằng bốn ca hỏng tiêm; đạt khi cả bốn bị phát hiện, không ca nào bị bỏ im lặng, và lô thiếu tệp không được công bố.

**Điều kiện đạt.** Bốn ca hỏng đều bị phát hiện và đi đúng đường xử lý, và lô thiếu tệp không bao giờ được đánh dấu hoàn tất.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đọc tệp ngay khi sự kiện báo tệp tới · khử trùng bằng tên tệp · coi có đủ sự kiện là có đủ tệp · bỏ tệp hỏng mà không cách ly và không báo chủ sở hữu.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/125-file-drop-delivery-arrival-completeness.md`
- Nội dung học thuật: `note.md` cùng thư mục.
