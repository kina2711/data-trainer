# Phase 9: Cloud Platform and Production Operations
# Module 26: Observability, Reliability and Security
# Lesson 399: Disaster recovery - RPO, RTO and a restore into a clean environment

## Thực hành

**Nhiệm vụ.** Lập kế hoạch phục hồi có thứ tự theo bản đồ phụ thuộc. Phục hồi toàn hệ vào một môi trường sạch; bấm giờ và ghi lại mọi thứ thiếu. Đối soát dữ liệu sau phục hồi. So hai con số đo được với mục tiêu và giải thích chênh lệch. Diễn tập một lỗi logic lan ra mọi bản sao và phục hồi theo thời điểm.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective có tiêu chí nghiệm thu là một lần phục hồi thật chứ một kế hoạch. Kiểm bằng diễn tập; đạt khi hệ phục vụ lại được trong môi trường sạch, dữ liệu đối soát khớp, và chênh lệch giữa số đo với mục tiêu được giải thích.

**Điều kiện đạt.** Hệ phục vụ lại được trong môi trường sạch với hai con số đo thật, dữ liệu đối soát khớp, và chênh lệch so với mục tiêu được giải thích.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Coi sao chép là phương án chống thảm hoạ · phục hồi vào môi trường cũ · bỏ bước đối soát dữ liệu sau phục hồi · không thử ca lỗi logic lan ra mọi bản sao.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/287-disaster-recovery-rpo-rto-and-a-restore-into-a-clean-environment.md`
- Nội dung học thuật: `note.md` cùng thư mục.
