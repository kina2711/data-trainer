# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 16: Data Ingestion and Integration Engineering
# Lesson 244: Connector Landscape Build Adopt or Buy

## Thực hành

**Nhiệm vụ.** Cho ba nguồn có ngữ nghĩa khác nhau, trong đó một nguồn có xoá cứng. Chấm ba nhóm công cụ theo mười tiêu chí. Với công cụ được chọn, kiểm bằng thực nghiệm ít nhất năm tiêu chí gồm hành vi khi lược đồ đổi và hành vi khi nguồn xoá bản ghi. Viết bản ghi quyết định nêu rõ trách nhiệm nào vẫn thuộc về đội.

Lưu source boundary, fixture hashes, versions, requests/queries, checkpoints, raw outputs, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu entity/change contract.
2. Tái hiện một assumption failure.
3. Chứng minh checkpoint/retry không tạo silent gap.
4. Đối soát bằng key và typed hash.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi phân biệt trách nhiệm vận hành với trách nhiệm về tính đúng. Kiểm bằng bản ghi quyết định ba nguồn; đạt khi mỗi lựa chọn có ít nhất năm tiêu chí được kiểm bằng thực nghiệm chứ bằng tài liệu.

**Điều kiện đạt.** Mỗi lựa chọn có ≥ 5 tiêu chí kiểm bằng thực nghiệm, và bản ghi quyết định nêu rõ trách nhiệm về tính đúng vẫn thuộc đội.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chọn công cụ theo danh sách nguồn được hỗ trợ · tin tài liệu về hành vi lệch lược đồ · giả định công cụ xử lý xoá đúng · coi dùng dịch vụ quản lý là hết trách nhiệm đối soát.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/132-connector-landscape-build-adopt-buy.md`
- Nội dung học thuật: `note.md` cùng thư mục.
