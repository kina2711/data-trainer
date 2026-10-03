# Phase 9: Cloud Platform and Production Operations
# Module 26: Observability, Reliability and Security
# Lesson 400: Threat modelling - asset, actor, trust boundary, abuse case

## Thực hành

**Nhiệm vụ.** Với hệ đã dựng ở M24 và M25, chạy bốn bước. Vẽ sơ đồ luồng dữ liệu có ranh giới tin cậy. Viết ít nhất sáu ca lạm dụng, trong đó có ít nhất một từ người trong tổ chức. Xếp hạng theo khả năng và tác động kèm mức không chắc chắn. Ánh xạ rủi ro với chốt kiểm soát theo bốn nhóm và chỉ ra chỗ chỉ có chốt ngăn chặn.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài lý thuyết đặt khung cho hai bài thực hành. Kiểm bằng bảng ánh xạ; đạt khi mọi ranh giới tin cậy được vẽ, ít nhất sáu ca lạm dụng được viết, và mỗi rủi ro lớn có chốt ở ít nhất hai trong bốn nhóm.

**Điều kiện đạt.** Mọi ranh giới tin cậy được vẽ, ≥ 6 ca lạm dụng gồm ít nhất một từ người trong tổ chức, và mỗi rủi ro lớn có chốt ở ≥ 2 nhóm.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dùng danh sách kiểm thay cho mô hình mối đe doạ · bỏ qua tác nhân trong tổ chức · chỉ đặt chốt ngăn chặn · xếp hạng rủi ro bằng con số trông chính xác mà không có căn cứ.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/288-threat-modelling-asset-actor-trust-boundary-abuse-case.md`
- Nội dung học thuật: `note.md` cùng thư mục.
