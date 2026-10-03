# Phase 8: Distributed Systems, Streaming and Compute
# Module 20: Distributed Systems Fundamentals
# Lesson 312: Replication - single leader, multi leader, leaderless

## Thực hành

**Nhiệm vụ.** Dựng bản sao một người dẫn ở cả chế độ đồng bộ và bất đồng bộ. Đo độ trễ sao chép dưới tải. Giết người dẫn và đếm số phép ghi đã báo thành công nhưng mất. Cho ba bối cảnh khác nhau về yêu cầu mất dữ liệu và độ trễ; chọn kiểu sao chép và tính lượng mất tối đa cho từng cái.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi nối lựa chọn với một con số về rủi ro mất dữ liệu. Kiểm bằng ba bối cảnh cộng phép đo; đạt khi mỗi lựa chọn kèm lượng mất tối đa tính được từ độ trễ đo được.

**Điều kiện đạt.** Ba bối cảnh có lựa chọn kèm lượng mất tối đa tính từ độ trễ đo được, và số phép ghi mất khi giết người dẫn được đếm thật.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dùng sao chép bất đồng bộ rồi tuyên bố không mất dữ liệu · chọn nhiều người dẫn mà chưa có chính sách xung đột · bỏ qua độ trễ sao chép khi tính rủi ro · coi bản sao đọc là bản sao lưu.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/200-replication-single-leader-multi-leader-leaderless.md`
- Nội dung học thuật: `note.md` cùng thư mục.
