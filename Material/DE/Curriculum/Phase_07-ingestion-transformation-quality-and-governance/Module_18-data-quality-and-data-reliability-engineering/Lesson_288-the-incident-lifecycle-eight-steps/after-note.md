# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 18: Data Quality and Data Reliability Engineering
# Lesson 288: The incident lifecycle - eight steps

## Thực hành

**Nhiệm vụ.** Nhận một sự cố mô phỏng thuộc một trong chín lớp sự cố: phân vùng thiếu hoặc muộn, trùng lặp, phá vỡ lược đồ, hồi quy logic thầm lặng, hỏng lịch sử chiều, nạp bù dở dang, bảng điều khiển cũ, lộ dữ liệu xuyên khách hàng, và công cụ chất lượng hỏng gây tin nhầm. Chạy tám bước và ghi quyết định từng bước. Liệt kê bên tiêu thụ ảnh hưởng bằng dòng dõi trước khi sửa.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài lý thuyết đặt quy trình cho hai bài thực hành sau. Kiểm bằng bài chạy quy trình; đạt khi tám bước có quyết định ghi lại, bằng chứng được giữ nguyên, và bên tiêu thụ bị ảnh hưởng được liệt kê trước khi sửa.

**Điều kiện đạt.** Tám bước có quyết định ghi lại theo đúng thứ tự, bằng chứng được giữ nguyên, và danh sách bên tiêu thụ lập trước khi sửa.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Sửa dữ liệu trước khi giữ bằng chứng · công bố lại trước khi đối soát · bỏ bước liệt kê bên tiêu thụ · phân tích sau sự cố quy về lỗi cá nhân.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/176-the-incident-lifecycle-eight-steps.md`
- Nội dung học thuật: `note.md` cùng thư mục.
