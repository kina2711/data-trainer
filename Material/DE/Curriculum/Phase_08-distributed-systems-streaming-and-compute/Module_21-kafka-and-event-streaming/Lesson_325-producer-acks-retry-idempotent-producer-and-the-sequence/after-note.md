# Phase 8: Distributed Systems, Streaming and Compute
# Module 21: Kafka and Event Streaming
# Lesson 325: Producer - acks, retry, idempotent producer and the sequence

## Thực hành

**Nhiệm vụ.** Với ba cấu hình xác nhận khác nhau, tính trước lượng mất và số bản trùng tối đa. Chạy tải rồi giết người dẫn phân vùng; đếm bản ghi mất và bản ghi trùng thật, đối chiếu với tính toán. Bật bên sản xuất luỹ đẳng và đo lại số bản trùng. Đo ảnh hưởng của gom lô, nén và thời gian chờ lên thông lượng cùng độ trễ.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi nối cấu hình với một con số về rủi ro. Kiểm bằng ba cấu hình đo song song; đạt khi số đo khớp con số tính trước trong sai số thoả thuận ở cả ba.

**Điều kiện đạt.** Số đo mất và trùng khớp tính toán ở cả ba cấu hình, và bên sản xuất luỹ đẳng đưa số bản trùng về không trong phạm vi phiên.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dùng mức xác nhận thấp rồi tuyên bố không mất · thử lại mà không bật chế độ luỹ đẳng · tăng số yêu cầu đang bay mà không xét thứ tự · chỉnh ba nút gom lô mà không đo.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/213-producer-acks-retry-idempotent-producer-and-the-sequence.md`
- Nội dung học thuật: `note.md` cùng thư mục.
