# Phase 8: Distributed Systems, Streaming and Compute
# Module 23: Spark, Flink and Distributed Compute Engines
# Lesson 349: Shuffle - read, write, sort, spill and serialization

## Thực hành

**Nhiệm vụ.** Chạy một công việc có bước xáo trộn lớn dưới bộ nhớ hạn chế. Đo riêng bốn thành phần chi phí cùng mức tràn đĩa và thời gian thu dọn rác. Thử bốn mức số phân vùng sau xáo trộn và vẽ đường thời gian. Giảm chi phí tuần tự hoá bằng cách thay hàm tự viết bằng biểu thức có sẵn và đo lại. Đối soát kết quả.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi phân giải một số tổng thành bốn phần để biết sửa chỗ nào. Kiểm bằng phép đo phân tách; đạt khi bốn thành phần đều có số, và thành phần lớn nhất được giảm với tổng thời gian giảm theo.

**Điều kiện đạt.** Bốn thành phần chi phí đều có số đo, và thành phần lớn nhất giảm kéo tổng thời gian giảm theo với kết quả không đổi.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Tăng bộ nhớ tiến trình thực thi trước khi biết thành phần nào đắt · coi tràn đĩa là lỗi cấu hình · bỏ qua chi phí tuần tự hoá · chọn số phân vùng sau xáo trộn theo mặc định.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/237-shuffle-read-write-sort-spill-and-serialization.md`
- Nội dung học thuật: `note.md` cùng thư mục.
