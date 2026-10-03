# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 19: Metadata Engineering, Catalog, Lineage and Governance
# Lesson 296: Ingestion architecture - the six-step harvest

## Thực hành

**Nhiệm vụ.** Cài bộ nối cho hiện vật của công cụ biến đổi và cho sự kiện của bộ điều phối. Chạy đủ sáu bước. Chạy lại năm lần với thời điểm bắt đầu chồng chéo và có lần bị giết giữa chừng; so đồ thị cuối với đồ thị của một lần chạy sạch. Tiêm một lỗi về danh tính và một cạnh treo, xác nhận bước kiểm bắt được.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là trạng thái đồ thị hội tụ sau nhiều lần chạy. Kiểm bằng phép thử chạy lại; đạt khi đồ thị sau năm lần chạy chồng chéo khớp đồ thị sau một lần chạy sạch và bước kiểm phát hiện được lỗi tiêm.

**Điều kiện đạt.** Đồ thị sau năm lần chạy chồng chéo khớp đồ thị của một lần chạy sạch, và bước kiểm bắt được cả hai lỗi tiêm.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Bỏ bước kiểm nên danh mục đầy mà sai · thu thập không luỹ đẳng nên chạy lại sinh bản trùng · suy đoán quan hệ khi nguồn đã khai báo tường minh · không phát sự kiện thay đổi nên chỉ mục tìm kiếm lệch với đồ thị.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/184-ingestion-architecture-the-six-step-harvest.md`
- Nội dung học thuật: `note.md` cùng thư mục.
