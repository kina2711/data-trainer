# Phase 10: System Design, AI Boundary and Trajectory
# Module 27: System Design Progression
# Lesson 412: Sequence 4 - an analytical platform

## Thực hành

**Nhiệm vụ.** Thiết kế một trong ba bài toán bậc bốn. Với mỗi chặng, viết hợp đồng vào ra và đường chạy lại. Đặt chốt đối soát và chỉ ra một chênh lệch giả định được quy về đoạn nào. Tính năng lực cho chặng tốn nhất. Nêu cách cách ly tính toán giữa các khối lượng công việc.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective đòi tính đầy đủ chứ một sơ đồ luồng. Kiểm bằng rà soát thiết kế; đạt khi mỗi chặng có hợp đồng vào ra cùng đường chạy lại, và chốt đối soát đặt đủ để quy chênh lệch về một đoạn.

**Điều kiện đạt.** Mỗi chặng có hợp đồng vào ra và đường chạy lại, và chốt đối soát đủ để quy một chênh lệch giả định về đúng đoạn.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Vẽ luồng mà không có chốt đối soát · bỏ đường chạy lại ở một chặng · để mọi khối lượng công việc dùng chung một cụm tính toán · bỏ quản trị và quyền sở hữu khỏi thiết kế.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/300-sequence-4-an-analytical-platform.md`
- Nội dung học thuật: `note.md` cùng thư mục.
