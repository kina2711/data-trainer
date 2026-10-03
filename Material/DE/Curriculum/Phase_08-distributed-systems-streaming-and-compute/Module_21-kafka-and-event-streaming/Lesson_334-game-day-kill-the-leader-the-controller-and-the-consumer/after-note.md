# Phase 8: Distributed Systems, Streaming and Compute
# Module 21: Kafka and Event Streaming
# Lesson 334: Game day - kill the leader, the controller and the consumer

## Thực hành

**Nhiệm vụ.** Viết hành vi kỳ vọng cho tám tình huống. Chạy từng cái trên cụm có tải. Ghi ba số cho mỗi tình huống. Đối soát số bản ghi ở đích với nguồn sau mỗi lần phục hồi. Nộp sổ tay gồm độ trễ tiêu thụ, thiếu bản sao, đầy đĩa, bản ghi độc và phá vỡ lược đồ.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module thành năng lực vận hành có số đo. Kiểm bằng tám tình huống; đạt khi ít nhất bảy phục hồi với đối soát khớp và không lần nào dùng lối tắt đặt lại vị trí về cuối.

**Điều kiện đạt.** ≥ 7/8 tình huống phục hồi với đối soát khớp, ba số đo đầy đủ cho mỗi tình huống, và sổ tay có đủ năm mục bắt buộc.

## Bài làm sau buổi học

**Nhiệm vụ.** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Lỗi cần chủ động loại trừ.** Đặt lại vị trí về cuối để hết cảnh báo · viết hành vi kỳ vọng sau khi thấy kết quả · bỏ tình huống mất số đông điều khiển vì khó dựng · không đối soát sau phục hồi.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/222-game-day-kill-the-leader-the-controller-and-the-consumer.md`
- Nội dung học thuật: `note.md` cùng thư mục.
