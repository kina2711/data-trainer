# Phase 6: Analytical Storage and Query Engines
# Module 15: File, Serialization and Open Table Formats
# Lesson 227: Iceberg Optimistic Concurrency and Conflict Validation

## Thực hành

**Nhiệm vụ.** Chạy hai bên ghi song song vào cùng bảng ở ba kịch bản. Với mỗi kịch bản, ghi lại thao tác nào thất bại và vì sao. Cài chính sách thử lại phân biệt ba loại. Chứng minh bằng đối soát rằng không thay đổi nào bị mất. Tăng số bên ghi và đo thông lượng sụp ở mức nào.

Chỉ dùng fixture tổng hợp và môi trường cô lập. Lưu input/schema hashes, versions, commands, metadata, plans, counters, outputs, logs và limitations.

## Kiểm tra cuối bài

1. Nêu publication hoặc identity boundary.
2. Đưa failure/counterexample có thể tái hiện.
3. Phân biệt format guarantee với implementation observation.
4. Nêu reconciliation oracle và reversal condition.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi phân biệt ca thử lại an toàn với ca thử lại làm mất dữ liệu. Kiểm bằng ba xung đột tái hiện; đạt khi cả ba được chẩn đoán đúng và không ca nào thử lại làm mất thay đổi.

**Điều kiện đạt.** Ba loại xung đột được chẩn đoán đúng, đối soát chứng minh không mất thay đổi nào, và ngưỡng sụp thông lượng được đo.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Thử lại mọi xung đột · không đối soát sau khi thử lại · chạy bảo trì trong giờ ghi cao điểm · tăng bên ghi để tăng thông lượng khi tranh chấp đã cao.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/115-iceberg-optimistic-concurrency-conflict-validation.md`
- Nội dung học thuật: `note.md` cùng thư mục.
