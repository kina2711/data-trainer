# Phase 8: Distributed Systems, Streaming and Compute
# Module 23: Spark, Flink and Distributed Compute Engines
# Lesson 354: Strong scaling lab - where scale-out turns negative

## Thực hành

**Nhiệm vụ.** Cố định tập dữ liệu và chạy với ít nhất bốn mức tài nguyên tăng dần. Ở mỗi mức, tính tăng tốc và hiệu suất song song, và tách bốn thành phần thời gian. Xác định mức mà thêm tài nguyên không còn giúp hoặc làm chậm hơn. Quy trần về một trong năm nguyên nhân bằng bằng chứng. Viết khuyến nghị về số tài nguyên kèm ngưỡng chi phí.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi giải thích đường cong chứ chỉ vẽ nó. Kiểm bằng thí nghiệm tăng quy mô; đạt khi bốn thành phần thời gian được tách ở mọi mức, điểm phản tác dụng được xác định, và trần quy về một nguyên nhân có bằng chứng.

**Điều kiện đạt.** Đường hiệu suất song song có số đo ở ≥ 4 mức, bốn thành phần thời gian tách được ở mọi mức, và trần quy về một nguyên nhân có bằng chứng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Báo cáo tăng tốc mà không báo hiệu suất song song · thêm tài nguyên khi trần là nguồn dữ liệu bên ngoài · không tách thời gian nên không biết phần nào tăng · kết luận bằng đồ thị mà không có khuyến nghị.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/242-strong-scaling-lab-where-scale-out-turns-negative.md`
- Nội dung học thuật: `note.md` cùng thư mục.
