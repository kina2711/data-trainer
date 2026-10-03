# Phase 8: Distributed Systems, Streaming and Compute
# Module 23: Spark, Flink and Distributed Compute Engines
# Lesson 352: Distributed MIMD and SPMD in a compute engine

## Thực hành

**Nhiệm vụ.** Trên một công việc thật, chỉ ra bằng chứng của từng tầng: số tiến trình thực thi và lõi cho tầng nhiều lệnh nhiều dữ liệu, cùng một mã toán tử chạy trên nhiều phân vùng cho khuôn mẫu một chương trình nhiều dữ liệu, và đường xử lý theo lô trong kế hoạch cho tầng làn véctơ. Ghi phân bố thời gian tác vụ và giải thích vì sao chênh lệch là bình thường. Gán ba mức tăng quan sát được về đúng tầng.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài lý thuyết nối M4 với engine thật, chuẩn bị cho hai bài đo. Kiểm bằng bài truy tầng; đạt khi ba tầng được chỉ ra bằng bằng chứng quan sát được và ba mức tăng được gán đúng tầng.

**Điều kiện đạt.** Ba tầng được chỉ ra bằng bằng chứng quan sát được, và ba mức tăng được gán đúng tầng kèm lý do.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Gộp ba tầng thành một lời giải thích · coi chênh lệch thời gian giữa các tác vụ là lỗi · nói engine nhanh vì dùng lệnh véctơ mà không tách các tầng · nhầm khuôn mẫu một chương trình nhiều dữ liệu với kiến trúc phần cứng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/240-distributed-mimd-and-spmd-in-a-compute-engine.md`
- Nội dung học thuật: `note.md` cùng thư mục.
