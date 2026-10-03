# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 19: Metadata Engineering, Catalog, Lineage and Governance
# Lesson 297: Connector concerns - incremental crawl, partial failure, preserved annotations

## Thực hành

**Nhiệm vụ.** Thêm 20 chú thích thủ công vào các tài sản. Chạy bốn tình huống: quét dở dang, bộ nối trễ, nguồn xoá tài sản, và nâng cấp bộ nối lên phiên bản mới. Sau mỗi tình huống, đếm chú thích còn lại. Viết chính sách ưu tiên nguồn và chứng minh nó chặn ghi đè. Rà quyền của bộ nối và hạ xuống mức chỉ đọc siêu dữ liệu.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có một tiêu chí nghiệm thu đặc trưng là bảo toàn chú thích. Kiểm bằng bốn tình huống; đạt khi cả bốn phục hồi đúng và không chú thích thủ công nào bị ghi đè sau khi dựng lại chỉ mục.

**Điều kiện đạt.** 20 chú thích thủ công còn nguyên sau cả bốn tình huống, chính sách ưu tiên nguồn chặn được ghi đè, và bộ nối chạy bằng quyền chỉ đọc.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Cho bộ nối quyền quản trị sản xuất · để lần thu thập ghi đè mọi trường · dựng lại danh mục từ đầu mà không di trú danh tính và chú thích · quét toàn bộ mỗi giờ làm nguồn quá tải.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/185-connector-concerns-incremental-crawl-partial-failure-preserved-annotations.md`
- Nội dung học thuật: `note.md` cùng thư mục.
