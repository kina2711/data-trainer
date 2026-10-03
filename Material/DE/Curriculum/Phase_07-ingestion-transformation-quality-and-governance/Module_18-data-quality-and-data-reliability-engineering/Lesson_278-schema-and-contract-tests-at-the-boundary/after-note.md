# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 18: Data Quality and Data Reliability Engineering
# Lesson 278: Schema and contract tests at the boundary

## Thực hành

**Nhiệm vụ.** Viết hợp đồng bên sản xuất và bên tiêu thụ cho hai tài sản. Cài phép kiểm hợp đồng chạy ở cả hai phía trong tích hợp liên tục. Tiêm ba thay đổi phá vỡ khác loại và xác nhận bị chặn kèm thông báo chỉ rõ bên tiêu thụ nào ảnh hưởng. Rà mọi miễn trừ đang có và bổ sung chủ sở hữu, lý do, hạn cùng biện pháp bù.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một cửa chặn hai phía có tiêu chí nghiệm thu bằng phép thử tiêm. Kiểm bằng ba thay đổi phá vỡ; đạt khi cả ba bị chặn ở phía sản xuất và mọi miễn trừ đang có đều đủ bốn phần.

**Điều kiện đạt.** Ba thay đổi phá vỡ bị chặn ở phía sản xuất kèm danh sách bên tiêu thụ ảnh hưởng, và mọi miễn trừ đủ bốn phần.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chỉ chạy phép kiểm hợp đồng ở phía tiêu thụ · miễn trừ không có hạn · không liệt kê bên tiêu thụ ảnh hưởng khi chặn · coi lược đồ khớp là hợp đồng được tôn trọng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/166-schema-and-contract-tests-at-the-boundary.md`
- Nội dung học thuật: `note.md` cùng thư mục.
