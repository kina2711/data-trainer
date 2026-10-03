# Phase 9: Cloud Platform and Production Operations
# Module 26: Observability, Reliability and Security
# Lesson 396: Error budget, burn rate and the release decision

## Thực hành

**Nhiệm vụ.** Tính ngân sách sai sót cho ba cam kết đã đặt. Dựng cảnh báo hai mức theo tốc độ tiêu. Phát lại ba đoạn dữ liệu lịch sử: một sự cố lớn ngắn, một suy giảm nhỏ kéo dài, và một khoảng bình thường; kiểm phản ứng của từng cảnh báo. Viết chính sách ngân sách và áp vào một quyết định phát hành thật.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là cảnh báo nổ đúng và một quyết định thật được dẫn ra. Kiểm bằng phát lại sự cố; đạt khi cảnh báo nhanh nổ ở sự cố lớn, cảnh báo chậm nổ ở suy giảm kéo dài, và không cái nào nổ trong khoảng bình thường.

**Điều kiện đạt.** Cảnh báo nhanh nổ ở sự cố lớn, cảnh báo chậm nổ ở suy giảm kéo dài, không cái nào nổ ở khoảng bình thường, và một quyết định phát hành được dẫn ra từ ngân sách.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Cảnh báo trên từng ngưỡng riêng lẻ thay vì theo tốc độ tiêu · viết chính sách ngân sách sau khi đã cạn · không có ngoại lệ có người duyệt · coi ngân sách là chỉ số báo cáo.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/284-error-budget-burn-rate-and-the-release-decision.md`
- Nội dung học thuật: `note.md` cùng thư mục.
