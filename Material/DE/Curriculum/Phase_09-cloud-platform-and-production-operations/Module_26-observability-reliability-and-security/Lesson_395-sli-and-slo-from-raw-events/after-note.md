# Phase 9: Cloud Platform and Production Operations
# Module 26: Observability, Reliability and Security
# Lesson 395: SLI and SLO from raw events

## Thực hành

**Nhiệm vụ.** Từ nhật ký sự kiện thô, định nghĩa ba chỉ số phục vụ thuộc ba khía cạnh khác nhau, mỗi cái nêu đủ bốn phần. Chọn ngưỡng tốt từ phân bố độ trễ thật và từ dữ liệu hành vi người dùng. Nhờ một học viên khác tính độc lập ba chỉ số trên cùng dữ liệu và so con số. Tạo một tình huống khả dụng cao mà tính đúng thấp.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có phép kiểm chứng khách quan bằng hai người tính độc lập. Kiểm bằng phép thử hai người; đạt khi ba chỉ số cho cùng con số ở hai người và mỗi ngưỡng dẫn được từ dữ liệu hành vi.

**Điều kiện đạt.** Ba chỉ số cho cùng con số khi hai người tính độc lập, ngưỡng dẫn từ dữ liệu hành vi, và tình huống khả dụng cao mà tính đúng thấp được tái hiện.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Bỏ phần loại trừ · chọn ngưỡng bằng con số tròn · chỉ cam kết khả dụng rồi coi là đủ · tính chỉ số phục vụ từ số đo đã gộp thay vì từ sự kiện.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/283-sli-and-slo-from-raw-events.md`
- Nội dung học thuật: `note.md` cùng thư mục.
