# Phase 10: System Design, AI Boundary and Trajectory
# Module 27: System Design Progression
# Lesson 419: The changed-constraint defence

## Thực hành

**Nhiệm vụ.** Người chấm đổi lần lượt bốn ràng buộc trên thiết kế đã làm. Với mỗi cái, trả lời ba câu hỏi trong 15 phút, dẫn từ bảng năng lực và bảng chế độ hỏng. Ghi chi phí của việc đổi. Với ràng buộc về tổ chức, chỉ ra phần nào của thiết kế phải bỏ đi thay vì làm chậm hơn.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đo năng lực thích ứng có căn cứ, và nó là tiêu chí ra của module. Kiểm bằng bốn tình huống đổi ràng buộc; đạt khi ít nhất ba lần chỉ đúng phần bị ảnh hưởng dẫn từ bảng năng lực hoặc bảng chế độ hỏng, và không lần nào vẽ lại toàn bộ khi không cần.

**Điều kiện đạt.** ≥ 3/4 lần chỉ đúng phần bị ảnh hưởng dẫn từ hiện vật đã có, mỗi lần kèm chi phí, và không lần nào vẽ lại toàn bộ khi không cần.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Bám vào quyết định cũ vì đã bỏ công · vẽ lại toàn bộ thiết kế khi một ràng buộc đổi · trả lời mà không dẫn từ bảng năng lực · bỏ qua ràng buộc về tổ chức.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/307-the-changed-constraint-defence.md`
- Nội dung học thuật: `note.md` cùng thư mục.
