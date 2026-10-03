# Phase 8: Distributed Systems, Streaming and Compute
# Module 22: Change Data Capture Internals
# Lesson 340: Position, offset and checkpoint - three different things

## Thực hành

**Nhiệm vụ.** Dựng đường đầy đủ từ nguồn qua nhật ký phân tán tới đích. Đo riêng ba loại độ trễ dưới tải và vẽ ba đường. Giết trình kết nối 50 lần ở các thời điểm ngẫu nhiên, trong đó có lần sau khi phát và trước khi lưu vị trí. Đếm số sự kiện trùng ở đích. Bật đích luỹ đẳng và đối soát lại.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi tách ba tiến độ thường bị gộp. Kiểm bằng ba số đo cộng thí nghiệm giết; đạt khi ba loại độ trễ được đo riêng và đích vẫn khớp nguồn sau 50 lần giết ngẫu nhiên.

**Điều kiện đạt.** Ba loại độ trễ được đo riêng, và đích khớp nguồn sau 50 lần giết nhờ luỹ đẳng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Gọi chung ba con số là độ trễ · lưu vị trí trình kết nối trước khi sự kiện bền vững ở đường truyền · cố tránh phát lại thay vì làm đích luỹ đẳng · theo dõi một loại độ trễ rồi kết luận cho cả tuyến.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/228-position-offset-and-checkpoint-three-different-things.md`
- Nội dung học thuật: `note.md` cùng thư mục.
