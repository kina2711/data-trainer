# Phase 3: Software and Backend Engineering
# Module 7: Software Design and Delivery
# Lesson 98: Deployment strategies and rollback

## Thực hành

**Nhiệm vụ.** Cho ba tình huống có ràng buộc khác nhau về tài nguyên, rủi ro và khả năng quan sát. Chọn chiến lược cho từng cái kèm lý do. Triển khai một phiên bản có lỗi bằng cách phát hành dần, phát hiện qua chỉ số, và lùi lại. Đo thời gian từ lúc triển khai tới lúc lùi xong.

#### Rollback drill đo được

Một diễn tập tối thiểu:

1. ghi release ID, stable digest và candidate digest;
2. khởi chạy tải có request ID;
3. deploy candidate chứa lỗi test có kiểm soát;
4. phát hiện bằng alert thật, không báo miệng;
5. ghi `detection_time`, `decision_time`, `rollback_start`, `recovery_time`;
6. rollback theo runbook;
7. xác minh error rate, latency và business invariant trở về baseline;
8. kiểm tra request đang bay, queue và dữ liệu viết trong khoảng lỗi;
9. lưu bằng chứng và action item.

Chỉ đo “kubectl báo rollout complete” là thiếu. Recovery hoàn tất khi user-facing signal và data invariant phục hồi.

#### Ba tình huống lựa chọn

| Ràng buộc | Lựa chọn hợp lý | Lý do |
|---|---|---|
| dịch vụ nội bộ, downtime 10 phút được phép, capacity sát trần | recreate | đơn giản; không đủ capacity chạy đôi |
| API quan trọng, đủ 2× capacity, switch route nhanh, DB compatible | blue-green | rollback routing nhanh |
| user-facing, telemetry theo version tốt, lỗi có thể chỉ xuất hiện ở tải thật | canary | giới hạn blast radius và học theo nấc |

Đây là đáp án theo ràng buộc, không phải ranking cố định.

#### Thiết kế rollback drill

Drill phải có hypothesis và success criteria trước khi bắt đầu:

```yaml
hypothesis: lỗi candidate làm business_error_rate vượt 1% trong 2 phút
detection_slo: 3m
decision_slo: 2m
recovery_slo: 5m
data_invariant: no duplicate task transition
rollback_precondition: old reader accepts all writes from candidate
```

Timeline tách `time-to-detect`, `time-to-decide`, `time-to-execute` và `time-to-verify`. Nếu tổng recovery chậm, biết bottleneck nằm ở alert, quyền phê duyệt, automation hay warm-up.

## Kiểm tra cuối bài

#### Bài tự kiểm tra

1. Vì sao liveness không nên fail chỉ vì database tạm thời mất kết nối?
2. Blue-green vẫn có thể tạo side effect kép qua thành phần dùng chung nào?
3. Canary cần minimum sample và control cohort ra sao?
4. Khi nào automatic pause phù hợp hơn automatic rollback?
5. Vì sao rollback image không đảo được external side effect?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi chọn theo ràng buộc tài nguyên và rủi ro, rồi chứng minh bằng diễn tập. Kiểm bằng bài chọn cộng diễn tập lùi; đạt khi chọn đúng ba tình huống và lùi hoàn tất trong hạn đã đặt.

**Điều kiện đạt.** Chọn đúng chiến lược cho cả ba tình huống, và diễn tập lùi hoàn tất trong hạn với số đo thời gian.


## Bài làm sau buổi học

**Nhiệm vụ.** Viết ghi chú chín phần; Làm lại lab từ đầu, không nhìn hướng dẫn, rồi làm phần mở rộng; Trả lời bốn câu kiểm tra; Nhật ký lỗi.

**Lỗi cần chủ động loại trừ.** Chọn phát hành dần mà không có chỉ số để quan sát · lùi mã khi lược đồ đã đổi một chiều · chưa bao giờ diễn tập lùi · dùng cờ tính năng rồi không bao giờ dọn.

Bài làm phải kèm lệnh tái hiện, đầu ra kiểm chứng và một đoạn giải thích ngắn cho mỗi quyết định kỹ thuật. Không chấp nhận ảnh chụp màn hình thay cho artifact có thể chạy lại.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-SOFTWARE-DESIGN-BOOK-01/10-deployment-strategies-and-rollback.md`
- Nội dung lý thuyết của bài: `note.md` cùng thư mục.
