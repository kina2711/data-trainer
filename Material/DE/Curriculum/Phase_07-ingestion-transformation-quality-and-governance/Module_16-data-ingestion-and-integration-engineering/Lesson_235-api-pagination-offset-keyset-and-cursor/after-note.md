# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 16: Data Ingestion and Integration Engineering
# Lesson 235: API Offset Keyset and Cursor Pagination

## Thực hành

**Nhiệm vụ.** Dựng một giao diện lập trình mô phỏng có thể chèn và xoá bản ghi giữa các trang. Cài cả ba cách phân trang. Chạy trích xuất trong khi chèn bản ghi ở đầu tập, và so tập khoá thu được với tập khoá đúng. Tái hiện con trỏ hết hạn và phản hồi mã thành công chứa lỗi nghiệp vụ. Chạy lại có điểm kiểm tra sau mỗi trang.

Lưu source boundary, fixture hashes, versions, requests/queries, checkpoints, raw outputs, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu entity/change contract.
2. Tái hiện một assumption failure.
3. Chứng minh checkpoint/retry không tạo silent gap.
4. Đối soát bằng key và typed hash.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là đối soát tập khoá dưới nhiễu. Kiểm bằng phép thử chèn giữa chừng; đạt khi tập khoá thu được khớp tập khoá nguồn tại ranh giới đã chốt, ở cả ba cách phân trang được so.

**Điều kiện đạt.** Tập khoá khớp tập đúng khi có chèn giữa chừng ở cách phân trang được chọn, và hai chế độ hỏng con trỏ được tái hiện cùng xử lý.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dùng phân trang theo độ lệch trên tập đang thay đổi · dừng khi gặp trang rỗng mà không kiểm dấu hiệu kết thúc tường minh · coi mã phản hồi thành công là dữ liệu hợp lệ · không kiểm con trỏ có ghim ảnh chụp hay không.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/123-api-offset-keyset-cursor-pagination.md`
- Nội dung học thuật: `note.md` cùng thư mục.
