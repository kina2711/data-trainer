# Phase 8: Distributed Systems, Streaming and Compute
# Module 23: Spark, Flink and Distributed Compute Engines
# Lesson 359: End-to-end guarantee - source replay, state restore and sink

## Thực hành

**Nhiệm vụ.** Dựng cùng một đường dòng chảy với ba loại đích. Với mỗi cái, phát biểu bảo đảm đầu cuối trước khi thử. Giết tiến trình 50 lần ở các ranh giới khác nhau; đếm bản ghi mất và trùng ở đích rồi đối chiếu với phát biểu. Thêm một bước gọi dịch vụ ngoài và chỉ ra vì sao nó luôn là ít nhất một lần.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi phát biểu có điều kiện thay vì tuyên bố. Kiểm bằng ba cấu hình đích; đạt khi phát biểu khớp kết quả đo ở cả ba và cấu hình đích chỉ thêm mới được nêu rõ không đạt được đúng một lần.

**Điều kiện đạt.** Phát biểu khớp kết quả đo ở cả ba cấu hình sau 50 lần giết, và cấu hình đích chỉ thêm mới được nêu rõ giới hạn.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Tuyên bố đúng một lần vì engine hỗ trợ · bỏ qua đích khi phát biểu bảo đảm · dùng đích chỉ thêm mới rồi mong không trùng · không nêu giả định lỗi.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/247-end-to-end-guarantee-source-replay-state-restore-and-sink.md`
- Nội dung học thuật: `note.md` cùng thư mục.
