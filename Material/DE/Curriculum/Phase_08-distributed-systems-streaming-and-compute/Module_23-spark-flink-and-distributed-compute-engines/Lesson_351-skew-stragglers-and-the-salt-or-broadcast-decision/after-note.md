# Phase 8: Distributed Systems, Streaming and Compute
# Module 23: Spark, Flink and Distributed Compute Engines
# Lesson 351: Skew, stragglers and the salt-or-broadcast decision

## Thực hành

**Nhiệm vụ.** Tạo lệch tải bằng một khoá chiếm phần lớn số dòng. Chạy và ghi phân bố thời gian tác vụ; chỉ ra trung bình che hiện tượng thế nào. Thử cả ba cách xử lý, đo thời gian và đối soát kết quả với bản gốc. Tạo thêm hai tình huống có triệu chứng giống nhưng nguyên nhân là máy yếu và thu dọn rác; phân biệt bằng số đo.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi phân biệt lệch tải với hai nguyên nhân giống triệu chứng. Kiểm bằng ba tình huống; đạt khi chẩn đoán đúng cả ba và bản sửa lệch tải cho kết quả khớp bản gốc với thời gian giảm có số đo.

**Điều kiện đạt.** Chẩn đoán đúng cả ba tình huống bằng số đo, và bản sửa lệch tải khớp kết quả gốc với thời gian giảm có số đo.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đánh giá bằng thời gian tác vụ trung bình · thêm phần ngẫu nhiên vào khoá mà không đối soát · tăng số phân vùng để chữa lệch tải · nhầm tác vụ chậm do máy yếu với lệch tải.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/239-skew-stragglers-and-the-salt-or-broadcast-decision.md`
- Nội dung học thuật: `note.md` cùng thư mục.
