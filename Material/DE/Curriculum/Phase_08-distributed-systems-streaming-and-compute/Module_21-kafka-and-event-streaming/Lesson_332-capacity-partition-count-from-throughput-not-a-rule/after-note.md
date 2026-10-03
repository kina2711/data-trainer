# Phase 8: Distributed Systems, Streaming and Compute
# Module 21: Kafka and Event Streaming
# Lesson 332: Capacity - partition count from throughput, not a rule

## Thực hành

**Nhiệm vụ.** Tính số phân vùng cho một khối lượng công việc cho trước từ bốn yếu tố. Chạy tải với ba mức số phân vùng quanh con số tính được; đo thông lượng, độ trễ phân vị 95, thời gian phục hồi khi giết một máy chủ, và chi phí siêu dữ liệu. Tạo một khoá nóng và chứng minh thêm phân vùng không giúp. Lập kế hoạch di trú nếu phải tăng phân vùng.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi tính từ ràng buộc chứ chọn theo quy tắc. Kiểm bằng phép thử tải ba mức; đạt khi con số tính ra đạt thông lượng mục tiêu và đường cong cho thấy điểm tăng phân vùng bắt đầu phản tác dụng.

**Điều kiện đạt.** Con số tính ra đạt thông lượng mục tiêu trong phép thử, và đường cong ba mức cho thấy điểm tăng phân vùng phản tác dụng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chọn số phân vùng theo một quy tắc chung · tăng phân vùng để chữa khoá nóng · tăng phân vùng tại chỗ mà không có kế hoạch di trú khoá · bỏ thời gian phục hồi khỏi tính toán.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/220-capacity-partition-count-from-throughput-not-a-rule.md`
- Nội dung học thuật: `note.md` cùng thư mục.
