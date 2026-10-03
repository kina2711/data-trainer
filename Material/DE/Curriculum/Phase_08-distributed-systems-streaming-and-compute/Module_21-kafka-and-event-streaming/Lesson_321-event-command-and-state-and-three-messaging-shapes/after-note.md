# Phase 8: Distributed Systems, Streaming and Compute
# Module 21: Kafka and Event Streaming
# Lesson 321: Event, command and state - and three messaging shapes

## Thực hành

**Nhiệm vụ.** Cho tám thông điệp thật trong một hệ; phân loại thành sự kiện, lệnh hay trạng thái và chỉ ra ba cái đang đặt tên sai kèm hệ quả ghép nối. Cho bốn tình huống; chọn hình thái hạ tầng và nêu lý do. Với tình huống chọn nhật ký phân tán, liệt kê ba việc làm được nhờ giữ lại bản ghi.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài mở module, đặt từ vựng. Kiểm bằng bài phân loại cộng bài chọn; đạt khi phân đúng ít nhất sáu trong tám thông điệp và chọn đúng hình thái ở ít nhất ba trong bốn tình huống.

**Điều kiện đạt.** Phân đúng ≥ 6/8 thông điệp kèm hệ quả của ba cái đặt tên sai, và chọn đúng hình thái ở ≥ 3/4 tình huống.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Gọi lệnh là sự kiện · dùng hàng đợi rồi muốn đọc lại · giả định nhật ký phân tán thay được mọi hàng đợi · bỏ qua việc thời hạn giữ quyết định đọc lại được bao xa.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/209-event-command-and-state-and-three-messaging-shapes.md`
- Nội dung học thuật: `note.md` cùng thư mục.
