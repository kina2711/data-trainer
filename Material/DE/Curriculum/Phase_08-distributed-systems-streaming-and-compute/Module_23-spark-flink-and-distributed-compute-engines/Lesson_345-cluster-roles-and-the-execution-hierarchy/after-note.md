# Phase 8: Distributed Systems, Streaming and Compute
# Module 23: Spark, Flink and Distributed Compute Engines
# Lesson 345: Cluster roles and the execution hierarchy

## Thực hành

**Nhiệm vụ.** Chạy ba công việc có hình dạng khác nhau. Với mỗi cái, mở giao diện theo dõi và ghi số công việc, giai đoạn và tác vụ. Giải thích số tác vụ của mỗi giai đoạn đến từ đâu. Thay đổi số phân vùng đầu vào và xác nhận số tác vụ đổi theo. Kéo một tập dữ liệu lớn về tiến trình điều khiển và quan sát hậu quả.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài mở module, đặt từ vựng. Kiểm bằng bài đọc giao diện theo dõi; đạt khi đếm đúng số giai đoạn và số tác vụ cho ba công việc và giải thích được nguồn gốc của số tác vụ.

**Điều kiện đạt.** Đếm đúng số giai đoạn và tác vụ cho ba công việc, và giải thích được số tác vụ đến từ số phân vùng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Nghĩ số tác vụ do số lõi quyết định · kéo dữ liệu lớn về tiến trình điều khiển · nhầm công việc với giai đoạn · bỏ qua tiến trình điều khiển khi tính năng lực.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/233-cluster-roles-and-the-execution-hierarchy.md`
- Nội dung học thuật: `note.md` cùng thư mục.
