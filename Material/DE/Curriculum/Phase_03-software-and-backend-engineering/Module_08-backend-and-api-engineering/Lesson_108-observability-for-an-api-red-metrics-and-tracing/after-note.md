# Phase 3: Software and Backend Engineering
# Module 8: Backend and API Engineering
# Lesson 108: Observability for an API - RED metrics and tracing

## Thực hành

**Nhiệm vụ.** Gắn ba chỉ số chia theo điểm vào và mã trạng thái. Truyền mã yêu cầu xuống hạ nguồn. Dựng theo vết cho tuyến gọi ba chặng. Giảng viên tiêm một sự cố ở một chặng và đặt ba câu hỏi chẩn đoán; trả lời chỉ bằng bảng điều khiển và theo vết. Kiểm điểm sẵn sàng phản ứng đúng khi mất kết nối cơ sở dữ liệu.

#### Instrumentation verification

Một test harness cần:

1. phát request thành công qua ba hop;
2. phát validation error;
3. tiêm dependency timeout;
4. tạo slow request vượt SLO;
5. ngắt DB và phục hồi;
6. thu metric, log, trace và probe transition;
7. dùng chỉ telemetry trả lời ba câu hỏi đã công bố;
8. kiểm không có secret/PII trong output.

Nếu người chẩn đoán phải mở source để biết label `handler="7"` nghĩa gì, telemetry contract chưa đủ.

## Kiểm tra cuối bài

#### Câu hỏi tự kiểm tra

1. RED đo ba đại lượng nào và denominator error là gì?
2. Vì sao average che tail latency?
3. Histogram khác summary ở khả năng aggregation nào?
4. Route label nào gây cardinality explosion?
5. Request ID khác trace ID và idempotency key thế nào?
6. Missing span chứng minh được điều gì?
7. Head sampling và tail sampling đổi coverage ra sao?
8. Exemplars giúp điều tra thế nào?
9. Vì sao database không nên nằm trong liveness check?
10. Readiness phụ thuộc DB cần policy nào để tránh cascade?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective đo bằng khả năng trả lời câu hỏi chứ bằng số lượng biểu đồ. Kiểm bằng ba câu hỏi chẩn đoán trong lúc có sự cố tiêm sẵn; đạt khi trả lời được ít nhất hai chỉ bằng bảng điều khiển và theo vết.

**Điều kiện đạt.** Trả lời được ≥ 2/3 câu hỏi chẩn đoán chỉ bằng bảng điều khiển và theo vết, và điểm sẵn sàng đổi trạng thái khi mất cơ sở dữ liệu.

#### Bằng chứng cho DE-L108

Evidence pack gồm:

1. metric contract với name, type, unit, labels và denominator;
2. dashboard RED tách route/status/outcome;
3. histogram bucket rationale theo SLO;
4. structured-log schema và redaction test;
5. trace ba hop có parent/child/link đúng;
6. exemplar hoặc truy vấn nối metric → trace → log;
7. fault-injection report trả lời ít nhất hai trong ba câu hỏi chỉ bằng telemetry;
8. readiness/liveness transition và recovery timeline khi DB mất.

## Bài làm sau buổi học

**Nhiệm vụ.** Viết ghi chú chín phần; Làm lại lab từ đầu, không nhìn hướng dẫn, rồi làm phần mở rộng; Trả lời bốn câu kiểm tra; Nhật ký lỗi.

**Lỗi cần chủ động loại trừ.** Báo thời gian xử lý trung bình · gộp mọi điểm vào vào một chỉ số · không truyền mã yêu cầu xuống hạ nguồn · để điểm sẵn sàng luôn trả về khoẻ.

Bài làm phải kèm lệnh tái hiện, đầu ra kiểm chứng và giải thích cho từng quyết định kỹ thuật. Không dùng ảnh chụp màn hình thay cho artifact có thể chạy lại.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-SOFTWARE-DESIGN-BOOK-01/20-api-observability-red-metrics-and-tracing.md`
- Nội dung lý thuyết của bài: `note.md` cùng thư mục.
