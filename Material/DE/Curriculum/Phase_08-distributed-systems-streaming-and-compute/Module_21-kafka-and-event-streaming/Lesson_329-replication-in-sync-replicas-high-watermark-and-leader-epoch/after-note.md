# Phase 8: Distributed Systems, Streaming and Compute
# Module 21: Kafka and Event Streaming
# Lesson 329: Replication - in-sync replicas, high watermark and leader epoch

## Thực hành

**Nhiệm vụ.** Dựng cụm ba máy chủ, hệ số sao chép ba. Với ba tổ hợp mức xác nhận và ngưỡng bản sao đồng bộ tối thiểu, tính trước lượng mất tối đa. Giết người dẫn rồi giết thêm một nút theo sau; đếm bản ghi đã xác nhận mà mất. Bật bầu chọn không sạch, tái hiện ca mất dữ liệu đã xác nhận. Đo độ trễ giữa lúc ghi và lúc đọc được.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi nối ba tham số thành một con số rủi ro. Kiểm bằng ba tổ hợp; đạt khi lượng mất đo được khớp tính toán ở cả ba và ca bầu chọn không sạch được tái hiện kèm số bản ghi mất.

**Điều kiện đạt.** Lượng mất đo được khớp tính toán ở cả ba tổ hợp, và ca bầu chọn không sạch được tái hiện kèm số bản ghi đã xác nhận bị mất.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đặt mức xác nhận toàn bộ với ngưỡng bản sao đồng bộ bằng một · bật bầu chọn không sạch mà không coi là quyết định nghiệp vụ · giả định bản ghi ghi xong là đọc được ngay · bỏ theo dõi số phân vùng thiếu bản sao.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/217-replication-in-sync-replicas-high-watermark-and-leader-epoch.md`
- Nội dung học thuật: `note.md` cùng thư mục.
