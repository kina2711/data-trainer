# Phase 8: Distributed Systems, Streaming and Compute
# Module 23: Spark, Flink and Distributed Compute Engines
# Lesson 360: Gate 8 - defend a delivery semantic and recover a stateful job

## Thực hành

**Nhiệm vụ.** Buổi 180 phút: 135 phút làm bài độc lập, 45 phút chữa bài. Bài chấm sáu phần: A (20đ) cho một lịch sử thao tác, xác định mô hình nhất quán bị vi phạm kèm chuỗi chứng minh · B (20đ) phát biểu bảo đảm giao nhận đầu cuối của một đường cho trước, nêu nguồn, đích và giả định lỗi, rồi tính số bản trùng và lượng mất tối đa · C (15đ) tái hiện và sửa một ca người dẫn cũ quay lại bằng thẻ chặn · D (20đ) một công việc dòng có trạng thái bị giết; khôi phục từ điểm kiểm tra và đối soát · E (15đ) truy ba tầng song song trên một công việc và quy một mức tăng về đúng tầng · F (10đ) chẩn đoán một công việc chậm và đề xuất đúng một thay đổi có kiểm soát.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Cổng đo năng lực lập luận về bảo đảm và năng lực vận hành dưới hỏng, nên hình thức là thực hành tại chỗ cộng bảo vệ.

**Điều kiện đạt.** Đạt ≥ 70/100, phần B và D đều ≥ 60%. Tuyên bố đúng một lần không nêu nguồn, đích và giả định lỗi thì phần B bằng không; phục hồi bằng cách đặt lại vị trí về cuối thì phần D bằng không.

## Bài làm sau buổi học

**Nhiệm vụ.** Không có bài tự học. Nếu không đạt, theo phụ lục khắc phục khi không đạt cổng

**Lỗi cần chủ động loại trừ.** Coi hết giờ là bên kia đã hỏng · nói đúng một lần mà không nêu ranh giới · đặt lại vị trí tiêu thụ về cuối để phục hồi · đổi cấu hình bộ nhớ trước khi đọc kế hoạch.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/248-gate-8-defend-a-delivery-semantic-and-recover-a-stateful-job.md`
- Nội dung học thuật: `note.md` cùng thư mục.
