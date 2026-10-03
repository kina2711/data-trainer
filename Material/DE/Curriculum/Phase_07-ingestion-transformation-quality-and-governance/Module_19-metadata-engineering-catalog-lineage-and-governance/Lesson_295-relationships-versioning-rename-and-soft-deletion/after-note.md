# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 19: Metadata Engineering, Catalog, Lineage and Governance
# Lesson 295: Relationships, versioning, rename and soft deletion

## Thực hành

**Nhiệm vụ.** Dựng đồ thị có đủ bảy loại quan hệ cho 30 tài sản. Thực hiện ba thao tác: đổi tên một bảng, xoá một bảng còn bên tiêu thụ, và đổi lược đồ hai lần. Sau mỗi thao tác, truy lịch sử và danh sách bên tiêu thụ. Viết phép kiểm chặn cạnh treo và chặn chu trình ở nơi không cho phép.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là truy được lịch sử sau ba thao tác phá hoại. Kiểm bằng ba thao tác; đạt khi sau cả ba vẫn truy được lược đồ cũ và danh sách bên tiêu thụ, và không có cạnh treo.

**Điều kiện đạt.** Sau ba thao tác vẫn truy được lược đồ cũ và danh sách bên tiêu thụ, và phép kiểm không tìm thấy cạnh treo nào.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Xử lý đổi tên như xoá rồi tạo mới · xoá cứng bản ghi tài sản · cho phép gắn thuộc tính tuỳ ý · không kiểm cạnh treo sau mỗi lần thu thập.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/183-relationships-versioning-rename-and-soft-deletion.md`
- Nội dung học thuật: `note.md` cùng thư mục.
