# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 16: Data Ingestion and Integration Engineering
# Lesson 233: Extraction Pattern Decision Framework

## Thực hành

**Nhiệm vụ.** Cho bốn nguồn với ngữ nghĩa thay đổi khác nhau, trong đó một nguồn có xoá cứng và một nguồn có dấu thời gian không đơn điệu. Chọn mẫu cho từng cái. Với mỗi lựa chọn, liệt kê giả định phải đúng và thiết kế một phép kiểm cho từng giả định. Chỉ ra nguồn nào không dùng được mẫu theo dấu thời gian và vì sao.

Lưu source boundary, fixture hashes, versions, requests/queries, checkpoints, raw outputs, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu entity/change contract.
2. Tái hiện một assumption failure.
3. Chứng minh checkpoint/retry không tạo silent gap.
4. Đối soát bằng key và typed hash.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi nêu giả định chứ chỉ chọn. Kiểm bằng bốn nguồn có ngữ nghĩa khác nhau; đạt khi chọn đúng ít nhất ba và mỗi lựa chọn kèm danh sách giả định kiểm được.

**Điều kiện đạt.** Chọn đúng ≥ 3/4 nguồn, mỗi lựa chọn kèm danh sách giả định, và mỗi giả định có một phép kiểm cụ thể.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Mặc định dùng mốc theo dấu thời gian cho mọi nguồn · chọn chụp toàn bộ vì đơn giản mà không tính tải lên nguồn · dùng phân trang theo độ lệch trên tập đang thay đổi · chọn mẫu trước khi biết ngữ nghĩa xoá.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/121-extraction-pattern-decision-framework.md`
- Nội dung học thuật: `note.md` cùng thư mục.
