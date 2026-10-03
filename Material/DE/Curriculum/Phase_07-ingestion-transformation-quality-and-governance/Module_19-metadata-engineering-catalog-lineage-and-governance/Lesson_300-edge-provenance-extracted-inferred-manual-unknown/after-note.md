# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 19: Metadata Engineering, Catalog, Lineage and Governance
# Lesson 300: Edge provenance - extracted, inferred, manual, unknown

## Thực hành

**Nhiệm vụ.** Gắn một trong bốn trạng thái xuất xứ cho mọi cạnh trong đồ thị đã hợp nhất, cạnh suy ra kèm tên luật và độ tin cậy. Viết phép kiểm chặn cạnh không có xuất xứ. Chạy một truy vấn ảnh hưởng và chứng minh kết quả tách phần chắc chắn khỏi phần suy ra và phần không rõ. Đặt ngưỡng độ tin cậy cho quyết định tự động và nêu lý do.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một ràng buộc nhận thức kiểm được bằng truy vấn. Kiểm bằng phép kiểm xuất xứ cộng truy vấn ảnh hưởng; đạt khi không cạnh nào thiếu xuất xứ và truy vấn ảnh hưởng trả về phần không chắc chắn kèm cảnh báo.

**Điều kiện đạt.** Không cạnh nào thiếu xuất xứ, và truy vấn ảnh hưởng tách rõ phần chắc chắn, phần suy ra và phần không rõ.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Vẽ cạnh suy ra như cạnh sự thật · bỏ cạnh không chắc chắn cho đồ thị sạch · không ghi phiên bản luật suy diễn · dùng cạnh độ tin cậy thấp cho quyết định tự động.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/188-edge-provenance-extracted-inferred-manual-unknown.md`
- Nội dung học thuật: `note.md` cùng thư mục.
