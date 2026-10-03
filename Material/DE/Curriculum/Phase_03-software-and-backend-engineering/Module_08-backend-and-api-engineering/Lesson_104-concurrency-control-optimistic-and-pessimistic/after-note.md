# Phase 3: Software and Backend Engineering
# Module 8: Backend and API Engineering
# Lesson 104: Concurrency control - optimistic and pessimistic

## Thực hành

**Nhiệm vụ.** Cài một điểm cập nhật không có kiểm soát đồng thời. Viết phép kiểm chạy 50 luồng cùng cập nhật và chứng minh có cập nhật bị mất. Cài khoá lạc quan và chạy lại. Cài khoá bi quan và chạy lại. So thông lượng hai cách ở hai mức tỉ lệ xung đột khác nhau.

#### Phép thử đồng thời phải tạo overlap thật

Thread count không chứng minh race xảy ra. Test cần barrier để các worker cùng đọc version cũ trước khi cho ghi:

```text
50 workers
  -> read same resource
  -> wait at barrier
  -> perform update
  -> collect outcome
```

Chạy bản lỗi trước để chứng minh test có khả năng bắt lost update. Sau đó chạy atomic, optimistic và pessimistic variant. Mỗi run đối soát expected final state, số success, số conflict, số retry và audit record.

Nếu dùng ORM, phải bảo đảm mỗi worker có session/transaction riêng. Dùng chung một session giữa thread có thể tạo lỗi framework khác và làm test không đo đúng database concurrency.

## Kiểm tra cuối bài

#### Câu hỏi tự kiểm tra

1. Vì sao hai transaction atomic vẫn có thể tạo lost update?
2. Khi nào atomic SQL statement tốt hơn optimistic version?
3. `row_count = 0` trong versioned update có hai cách hiểu nào?
4. Vì sao retry cùng expected version không giải quyết conflict?
5. Lock được giải phóng ở ranh giới nào?
6. `SKIP LOCKED` phù hợp và không phù hợp ở đâu?
7. Vì sao deadlock phải được coi là failure mode dự kiến?
8. Benchmark nào làm optimistic trông tốt giả tạo?
9. Vì sao thread count chưa chứng minh phép thử tạo overlap?
10. Predicate invariant khác row invariant thế nào?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một cơ chế chỉ kiểm được bằng phép chạy song song, điểm mà phép kiểm thông thường bỏ sót. Kiểm bằng 1000 lần ghi đồng thời; đạt khi không có cập nhật nào bị mất và số lần từ chối khớp số xung đột thật.

**Điều kiện đạt.** Bản chưa sửa mất cập nhật có số chứng minh, cả hai cơ chế đều cho 0 cập nhật mất qua 1000 lần, và có bảng so thông lượng.

#### Bằng chứng cho DE-L104

Evidence pack gồm:

1. test harness 50 worker có barrier và seed cố định;
2. bản không kiểm soát tạo lost update tái hiện được;
3. bản optimistic có version predicate, conflict outcome và bounded retry policy;
4. bản pessimistic có `FOR UPDATE`, lock order và timeout;
5. 1.000 vòng ở mỗi biến thể không vi phạm invariant;
6. bảng throughput/latency ở cold-key và hot-key workload;
7. lock wait, conflict, retry, deadlock và pool metrics;
8. giải thích vì sao cơ chế được chọn cho workload mục tiêu.

## Bài làm sau buổi học

**Nhiệm vụ.** Viết ghi chú chín phần; Làm lại lab từ đầu, không nhìn hướng dẫn, rồi làm phần mở rộng; Trả lời bốn câu kiểm tra; Nhật ký lỗi.

**Lỗi cần chủ động loại trừ.** Chỉ kiểm tuần tự rồi kết luận đúng · dùng khoá bi quan cho mọi thứ · trả lỗi xung đột mà không nói máy khách phải làm gì · giữ khoá qua nhiều yêu cầu.

Bài làm phải kèm lệnh tái hiện, đầu ra kiểm chứng và giải thích cho từng quyết định kỹ thuật. Không dùng ảnh chụp màn hình thay cho artifact có thể chạy lại.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-SOFTWARE-DESIGN-BOOK-01/16-concurrency-control-optimistic-and-pessimistic.md`
- Nội dung lý thuyết của bài: `note.md` cùng thư mục.
