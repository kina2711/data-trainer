# Phase 10: System Design, AI Boundary and Trajectory
# Module 27: System Design Progression
# Lesson 407: Invariants and consistency boundaries

## Thực hành

**Nhiệm vụ.** Với hai thiết kế, liệt kê ít nhất năm bất biến mỗi cái. Với từng bất biến, chỉ ra nó được cưỡng chế ở đâu và chuyện gì xảy ra nếu hai thành phần liên quan nằm hai phân vùng. Phân loại mọi kho dữ liệu thành nguồn sự thật hay dẫn xuất, và mô tả đường dựng lại cho từng cái dẫn xuất. Với mỗi chỗ nhất quán cuối cùng, viết hợp đồng mức cũ tối đa.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi suy ranh giới từ bất biến chứ đặt theo thói quen. Kiểm bằng bài phân tích; đạt khi mỗi bất biến chỉ ra đúng ranh giới cưỡng chế nó, mọi dữ liệu dẫn xuất có đường dựng lại, và mọi nhất quán cuối cùng có hợp đồng mức cũ.

**Điều kiện đạt.** Mỗi bất biến chỉ ra đúng ranh giới cưỡng chế, mọi dữ liệu dẫn xuất có đường dựng lại, và mọi nhất quán cuối cùng có hợp đồng mức cũ.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Coi bộ nhớ đệm là nguồn sự thật · nói cuối cùng nhất quán mà không có hợp đồng mức cũ · đặt ranh giới phân vùng trước khi phát biểu bất biến · không có đường dựng lại cho dữ liệu dẫn xuất.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/295-invariants-and-consistency-boundaries.md`
- Nội dung học thuật: `note.md` cùng thư mục.
