# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 19: Metadata Engineering, Catalog, Lineage and Governance
# Lesson 302: Impact analysis from a source column to a dashboard

## Thực hành

**Nhiệm vụ.** Chạy ba truy vấn ảnh hưởng từ ba cột nguồn khác nhau tới bảng điều khiển. Đối chiếu kết quả với danh sách đúng xác định bằng tay. Chạy một truy vấn nguyên nhân ngược từ một con số sai. Với mỗi kết quả, kèm chủ sở hữu, mức tin cậy và độ phủ của đồ thị. Dùng kết quả để lập danh sách thông báo cho một lần đổi lược đồ.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu bằng đối chiếu với danh sách đúng. Kiểm bằng ba truy vấn; đạt khi kết quả khớp danh sách đúng ở ít nhất hai và mọi kết quả đều kèm độ phủ của đồ thị.

**Điều kiện đạt.** Kết quả khớp danh sách đúng ở ≥ 2/3 truy vấn, mọi kết quả kèm chủ sở hữu cùng mức tin cậy cùng độ phủ đồ thị.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Trình bày kết quả truy vấn ảnh hưởng như danh sách đầy đủ · bỏ mức tin cậy · không kèm chủ sở hữu nên không báo được ai · bỏ phần không chắc chắn cho kết quả gọn.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/190-impact-analysis-from-a-source-column-to-a-dashboard.md`
- Nội dung học thuật: `note.md` cùng thư mục.
