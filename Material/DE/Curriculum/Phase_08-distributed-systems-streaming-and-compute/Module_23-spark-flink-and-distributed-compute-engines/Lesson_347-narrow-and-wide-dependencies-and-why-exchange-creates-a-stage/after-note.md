# Phase 8: Distributed Systems, Streaming and Compute
# Module 23: Spark, Flink and Distributed Compute Engines
# Lesson 347: Narrow and wide dependencies, and why exchange creates a stage

## Thực hành

**Nhiệm vụ.** Phân loại mười phép biến đổi vào hai loại. Lấy một công việc có bốn bước xáo trộn; viết lại để giảm ít nhất một bước, chẳng hạn bằng cách gộp phép gộp hoặc đổi thứ tự. Đo thời gian và lượng dữ liệu xáo trộn trước sau. Đối soát kết quả. Giết một tiến trình thực thi và quan sát việc tính lại theo dòng dõi; thêm điểm kiểm tra rồi đo lại.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là số bước xáo trộn giảm mà kết quả không đổi. Kiểm bằng cặp số đo; đạt khi số bước trao đổi giảm ít nhất một, thời gian giảm có số đo, và kết quả đối soát khớp bản gốc.

**Điều kiện đạt.** Số bước trao đổi giảm ≥ 1 với thời gian giảm có số đo, và kết quả đối soát khớp bản gốc tuyệt đối.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Coi ranh giới giai đoạn là quy ước · thêm phép sắp xếp không cần thiết · đặt điểm kiểm tra khắp nơi · sửa mà không đối soát kết quả.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/235-narrow-and-wide-dependencies-and-why-exchange-creates-a-stage.md`
- Nội dung học thuật: `note.md` cùng thư mục.
