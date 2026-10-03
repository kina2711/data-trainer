# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 16: Data Ingestion and Integration Engineering
# Lesson 242: Source to Landing Reconciliation

## Thực hành

**Nhiệm vụ.** Với ba nguồn, chạy cả bốn bậc đối soát tại một ranh giới bất biến. Tiêm ba lỗi: mất một lô, trùng một lô, và một cột bị làm tròn khác. Chứng minh bậc nào phát hiện được lỗi nào. Chuẩn hoá giá trị trước khi băm và chỉ ra chênh lệch giả biến mất. Viết ngân sách chênh lệch kèm người duyệt.

Lưu source boundary, fixture hashes, versions, requests/queries, checkpoints, raw outputs, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu entity/change contract.
2. Tái hiện một assumption failure.
3. Chứng minh checkpoint/retry không tạo silent gap.
4. Đối soát bằng key và typed hash.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi chứng minh tính đầy đủ chứ đưa dấu hiệu. Kiểm bằng bốn bậc cho ba nguồn; đạt khi bậc hai chỉ đúng khoá lệch, và mọi chênh lệch còn lại có nguyên nhân được nêu tên chứ bỏ qua.

**Điều kiện đạt.** Bốn bậc chạy cho cả ba nguồn, ba lỗi tiêm được quy đúng bậc phát hiện, và mọi chênh lệch còn lại có nguyên nhân nêu tên.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đối soát bằng lấy mẫu rồi kết luận đầy đủ · băm mà không chuẩn hoá · đếm hai bên ở hai thời điểm khác nhau · tự đặt ngân sách chênh lệch được chấp nhận.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/130-source-to-landing-reconciliation.md`
- Nội dung học thuật: `note.md` cùng thư mục.
