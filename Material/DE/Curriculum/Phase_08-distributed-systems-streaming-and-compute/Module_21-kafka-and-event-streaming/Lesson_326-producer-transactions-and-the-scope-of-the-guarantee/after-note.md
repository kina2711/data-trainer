# Phase 8: Distributed Systems, Streaming and Compute
# Module 21: Kafka and Event Streaming
# Lesson 326: Producer transactions and the scope of the guarantee

## Thực hành

**Nhiệm vụ.** Cài luồng đọc từ một chủ đề, xử lý, rồi ghi sang chủ đề khác kèm ghi vị trí, tất cả trong một giao dịch. Giết tiến trình ở từng ranh giới và đếm bản trùng ở đích. Thêm một bước ghi vào cơ sở dữ liệu ngoài và chứng minh nó không được giao dịch bảo vệ; bổ sung cơ chế luỹ đẳng cho bước đó. Đo chi phí độ trễ và thông lượng của giao dịch.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi nêu đúng phạm vi bảo đảm chứ chỉ bật tính năng. Kiểm bằng phép thử giết tiến trình cộng bài phát biểu; đạt khi không bản trùng nào trong phạm vi hệ, và ca ghi ra hệ ngoài được chỉ ra là nằm ngoài bảo đảm kèm cách bù.

**Điều kiện đạt.** Không bản trùng nào trong phạm vi hệ qua mọi ranh giới giết, và bước ghi ra hệ ngoài được chỉ rõ nằm ngoài bảo đảm kèm cơ chế bù.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Tuyên bố đúng một lần đầu cuối nhờ giao dịch · để bên tiêu thụ đọc cả bản chưa chốt · đưa lời gọi dịch vụ ngoài vào trong giao dịch · bật giao dịch mà không đo chi phí.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/214-producer-transactions-and-the-scope-of-the-guarantee.md`
- Nội dung học thuật: `note.md` cùng thư mục.
