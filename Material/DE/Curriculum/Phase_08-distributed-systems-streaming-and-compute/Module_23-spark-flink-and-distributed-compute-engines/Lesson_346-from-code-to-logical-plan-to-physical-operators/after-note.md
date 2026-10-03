# Phase 8: Distributed Systems, Streaming and Compute
# Module 23: Spark, Flink and Distributed Compute Engines
# Lesson 346: From code to logical plan to physical operators

## Thực hành

**Nhiệm vụ.** Với ba truy vấn có hình dạng khác nhau, xuất cả kế hoạch logic, kế hoạch đã tối ưu và kế hoạch vật lý. Dự đoán số giai đoạn từ số bước trao đổi trước khi chạy, rồi đối chiếu. Làm thống kê lạc hậu và quan sát kế hoạch đổi thế nào. Chèn một hàm do người dùng viết và chỉ ra bộ tối ưu mất khả năng gì.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi dự đoán từ kế hoạch rồi kiểm bằng thực tế. Kiểm bằng ba truy vấn; đạt khi dự đoán đúng số giai đoạn ở ít nhất hai và chỉ ra đúng vị trí mọi bước trao đổi dữ liệu.

**Điều kiện đạt.** Dự đoán đúng số giai đoạn ở ≥ 2/3 truy vấn, và mọi bước trao đổi dữ liệu được chỉ đúng vị trí trong kế hoạch.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đọc kế hoạch logic rồi kết luận về cách chạy · bỏ qua bước trao đổi khi đếm giai đoạn · chạy với thống kê lạc hậu · chèn hàm tự viết vào chỗ cần đẩy điều kiện xuống.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/234-from-code-to-logical-plan-to-physical-operators.md`
- Nội dung học thuật: `note.md` cùng thư mục.
