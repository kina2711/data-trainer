# Phase 9: Cloud Platform and Production Operations
# Module 25: Containers, Infrastructure as Code and Kubernetes
# Lesson 383: Pods, probes, requests and limits

## Thực hành

**Nhiệm vụ.** Đo lượng bộ nhớ và bộ xử lý thật của một dịch vụ dưới tải; đặt yêu cầu và giới hạn từ số đo đó. Tiêm bốn tình huống: giới hạn bộ nhớ quá thấp, giới hạn bộ xử lý quá thấp, thăm dò sẵn sàng nông trên một dịch vụ hỏng, và thăm dò sống quá nhạy dưới tải. Chẩn đoán từng cái bằng sự kiện và số đo. Sửa và đo lại.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective đòi rút tham số từ đo lường và phân biệt hai triệu chứng gần giống. Kiểm bằng bốn tình huống tiêm; đạt khi bốn tình huống được chẩn đoán đúng và giá trị cuối dẫn được từ số đo chứ từ phỏng đoán.

**Điều kiện đạt.** Bốn tình huống được chẩn đoán đúng, và giá trị bốn trường dẫn được từ số đo tải thật.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đặt yêu cầu và giới hạn bằng con số tròn · bỏ giới hạn cho khỏi bị kết thúc · viết thăm dò sẵn sàng chỉ kiểm tiến trình còn sống · đặt thăm dò sống nhạy hơn thăm dò sẵn sàng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/271-pods-probes-requests-and-limits.md`
- Nội dung học thuật: `note.md` cùng thư mục.
