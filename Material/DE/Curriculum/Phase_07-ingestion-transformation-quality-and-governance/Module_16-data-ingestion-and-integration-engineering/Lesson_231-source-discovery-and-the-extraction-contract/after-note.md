# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 16: Data Ingestion and Integration Engineering
# Lesson 231: Source Discovery and the Extraction Contract

## Thực hành

**Nhiệm vụ.** Chọn một nguồn thật có tài liệu. Điền hợp đồng trích xuất tám nhóm, phần nào không có trong tài liệu thì ghi là chưa biết chứ đoán. Dò tìm giá trị canh chừng bằng cách thống kê phân bố từng cột. Với mỗi nhóm còn trống, viết một câu mô tả chế độ hỏng nó gây ra.

Lưu source boundary, fixture hashes, versions, requests/queries, checkpoints, raw outputs, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu entity/change contract.
2. Tái hiện một assumption failure.
3. Chứng minh checkpoint/retry không tạo silent gap.
4. Đối soát bằng key và typed hash.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Bài mở module, áp một danh mục phỏng vấn vào nguồn thật. Kiểm bằng rà soát tám nhóm; đạt khi ít nhất sáu nhóm có câu trả lời cụ thể và mỗi nhóm trống kèm một chế độ hỏng dự đoán được.

**Điều kiện đạt.** ≥ 6/8 nhóm có câu trả lời cụ thể, giá trị canh chừng được dò bằng thống kê thật, và mọi nhóm trống kèm chế độ hỏng dự đoán.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Bắt đầu viết trình trích xuất trước khi chốt ngữ nghĩa thay đổi · tin tài liệu nguồn nói đúng về giá trị rỗng · bỏ qua múi giờ của dấu thời gian nguồn · không hỏi cửa sổ thời gian được phép chạy.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/119-source-discovery-extraction-contract.md`
- Nội dung học thuật: `note.md` cùng thư mục.
