# Phase 3: Software and Backend Engineering
# Module 8: Backend and API Engineering
# Lesson 107: Resilience - timeouts, circuit breakers and bulkheads

## Thực hành

**Nhiệm vụ.** Dựng bốn cơ chế. Ba kịch bản: cơ sở dữ liệu chậm gấp mười lần, một phụ thuộc ngoài chết hoàn toàn, và tải gấp năm lần công suất. Với mỗi kịch bản, đo tỉ lệ phục vụ của các điểm vào không phụ thuộc phần hỏng, và kiểm hồ kết nối có cạn không. Thêm vách ngăn tách hồ và đo lại.

#### Ba kịch bản thí nghiệm

#### A. Database chậm gấp mười lần

Tiêm latency vào query path. Đo timeout, pool wait, in-flight, endpoint không dùng DB và cancellation. Sau bulkhead, endpoint không phụ thuộc DB phải giữ service ratio theo ngưỡng đã định.

#### B. External dependency chết hoàn toàn

Trả timeout/connection failure. Quan sát breaker mở, call thật giảm, fail-fast tăng, half-open probe và recovery. Retry attempts phải nằm trong budget.

#### C. Tải gấp năm lần capacity

Đo queue age, rejection, latency và throughput. Chứng minh bounded admission/load shedding giữ phần traffic ưu tiên và không làm pool toàn cục cạn.

#### Đo “suy giảm có kiểm soát”

Không chỉ báo tổng success rate. Tách:

- endpoint phụ thuộc dependency hỏng;
- endpoint độc lập;
- traffic ưu tiên và best-effort;
- original request và retry attempt;
- served, degraded, rejected, timeout;
- pool utilization/wait theo bulkhead;
- breaker state/call prevented;
- deadline remaining tại mỗi hop;
- recovery time sau khi fault được gỡ.

Mục tiêu L107 là phần không phụ thuộc tiếp tục phục vụ, không phải biến dependency failure thành 100% success.

## Kiểm tra cuối bài

#### Câu hỏi tự kiểm tra

1. Deadline khác timeout thế nào?
2. Timeout nào không bao phủ pool acquisition?
3. Khi nào retry làm lỗi nặng hơn?
4. Vì sao retry nhiều tầng khuếch đại tải?
5. Circuit breaker bảo vệ request nào?
6. Half-open cần giới hạn probe vì sao?
7. Bulkhead nên chia theo boundary nào?
8. Queue vô hạn phá bulkhead ra sao?
9. Fallback nào làm sai semantics?
10. Số đo nào chứng minh endpoint độc lập được bảo vệ?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một tập cấu hình kiểm được bằng thí nghiệm hỏng hạ nguồn. Kiểm bằng ba kịch bản hỏng; đạt khi dịch vụ vẫn phục vụ phần không phụ thuộc và không cạn hồ kết nối.

**Điều kiện đạt.** Ba kịch bản hỏng đều giữ được tỉ lệ phục vụ của phần không phụ thuộc, và vách ngăn ngăn được hồ kết nối cạn có số chứng minh.

#### Bằng chứng cho DE-L107

Evidence pack gồm:

1. call graph có deadline/timeout từng hop;
2. error classification và retry matrix;
3. retry budget, backoff và jitter implementation;
4. breaker transition log và state metrics;
5. resource map trước/sau bulkhead;
6. ba fault scenario với cùng workload seed;
7. service ratio của endpoint độc lập và pool-wait evidence;
8. recovery trace sau khi dependency khỏe lại.

## Bài làm sau buổi học

**Nhiệm vụ.** Viết ghi chú chín phần; Làm lại lab từ đầu, không nhìn hướng dẫn, rồi làm phần mở rộng; Trả lời bốn câu kiểm tra; Nhật ký lỗi.

**Lỗi cần chủ động loại trừ.** Không đặt hạn chờ cho lời gọi cơ sở dữ liệu · dùng chung một hồ cho mọi loại truy vấn · thử lại thao tác không bất biến · bộ ngắt mạch không bao giờ đóng lại.

Bài làm phải kèm lệnh tái hiện, đầu ra kiểm chứng và giải thích cho từng quyết định kỹ thuật. Không dùng ảnh chụp màn hình thay cho artifact có thể chạy lại.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-SOFTWARE-DESIGN-BOOK-01/19-resilience-timeouts-circuit-breakers-and-bulkheads.md`
- Nội dung lý thuyết của bài: `note.md` cùng thư mục.
