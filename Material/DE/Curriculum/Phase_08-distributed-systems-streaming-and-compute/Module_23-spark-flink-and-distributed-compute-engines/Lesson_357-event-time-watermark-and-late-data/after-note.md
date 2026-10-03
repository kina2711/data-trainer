# Phase 8: Distributed Systems, Streaming and Compute
# Module 23: Spark, Flink and Distributed Compute Engines
# Lesson 357: Event time, watermark and late data

## Thực hành

**Nhiệm vụ.** Sinh dòng sự kiện có phân bố độ trễ thực tế gồm một phần đuôi rất muộn. Chạy với ba mức mốc nước; với mỗi mức, đo độ trễ tới khi có kết quả, tỉ lệ sự kiện bị bỏ, và kích thước trạng thái. Chọn một mức và nêu lý do. Cài chính sách cho sự kiện quá muộn và chứng minh chúng được đếm và ghi nhận chứ bỏ.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi chọn tham số từ số đo chứ từ giá trị mặc định. Kiểm bằng ba mức mốc nước; đạt khi mỗi mức có cặp số độ trễ với tỉ lệ sự kiện bị bỏ, và sự kiện quá muộn không bị bỏ im lặng.

**Điều kiện đạt.** Ba mức mốc nước có cặp số độ trễ với tỉ lệ bỏ cùng kích thước trạng thái, và sự kiện quá muộn được đếm và ghi nhận.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Xử lý theo thời gian tới rồi chạy lại ra kết quả khác · đặt mốc nước theo giá trị mặc định · bỏ sự kiện muộn im lặng · bỏ qua ảnh hưởng của mốc nước lên kích thước trạng thái.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/245-event-time-watermark-and-late-data.md`
- Nội dung học thuật: `note.md` cùng thư mục.
