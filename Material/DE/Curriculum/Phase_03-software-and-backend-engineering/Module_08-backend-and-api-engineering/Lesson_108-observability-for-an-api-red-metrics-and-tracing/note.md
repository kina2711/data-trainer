# Phase 3: Software and Backend Engineering
# Module 8: Backend and API Engineering
# Lesson 108: Observability for an API - RED metrics and tracing

## Mục tiêu bài học

**Năng lực cần chứng minh.** Dựng bộ chỉ số và theo vết đủ để trả lời ba câu hỏi chẩn đoán mà không cần đọc mã.

**Điều kiện hoàn thành.** Trả lời được ≥ 2/3 câu hỏi chẩn đoán chỉ bằng bảng điều khiển và theo vết, và điểm sẵn sàng đổi trạng thái khi mất cơ sở dữ liệu.

> [!abstract] Câu hỏi trung tâm
> Khi một endpoint chậm hoặc lỗi, operator phải trả lời: request nào bị ảnh hưởng, lỗi nằm ở chặng nào, tần suất và tail latency ra sao, dependency nào chiếm critical path, và instance có còn nên nhận traffic không. Telemetry phải được thiết kế để trả lời các câu ấy, không chỉ để lấp dashboard.

## Monitoring và observability

Monitoring theo dõi câu hỏi đã biết bằng signal và threshold định trước. Observability là khả năng suy ra trạng thái bên trong từ output quan sát được, kể cả với câu hỏi chưa dự đoán chính xác. Hai khái niệm bổ sung nhau.

Cài Prometheus, log collector và tracing SDK chưa tự tạo observability. Nếu route label sai, trace context đứt, log không có correlation hoặc sampling bỏ đúng failure hiếm, tool vẫn không trả lời được “vì sao”.

> [!source-fact]
> *Cloud Native Go* định nghĩa observability như system property và phân biệt nó với việc đơn thuần cài công cụ; Chapter 11, PDF 365–373.

## Bốn signal và vai trò

| Signal | Tốt cho | Giới hạn |
|---|---|---|
| Metrics | xu hướng, tỷ lệ, alert, SLO trên tập request | mất chi tiết từng request; label cardinality hữu hạn |
| Logs | event rời, error context, audit và state transition | tìm tương quan khó nếu thiếu identity; volume lớn |
| Traces | critical path và quan hệ nhân quả của một request | sampling; missing span; overhead |
| Baggage/context | truyền metadata cần liên kết qua hop | không phải nơi chứa secret; làm tăng payload/cardinality |

OpenTelemetry gọi traces, metrics, logs và baggage là signals/concepts có thể phối hợp. Không signal nào thay toàn bộ signal khác.

## RED là điểm bắt đầu cho request-driven service

RED gồm:

- **Rate**: số request theo đơn vị thời gian;
- **Errors**: số/tỷ lệ request không đạt outcome contract;
- **Duration**: phân bố thời gian xử lý.

Ba signal phải được tách theo route chuẩn hóa, method/operation và outcome class. Không dùng raw path `/users/123` làm label; dùng route template `/users/{id}` để tránh cardinality theo user.

Rate không chỉ là traffic. So rate nhận, hoàn tất, rejected và retry attempts giúp thấy queue/load amplification. Error không chỉ là `5xx`; domain failure, timeout, cancellation và degraded outcome cần taxonomy phù hợp contract.

## Định nghĩa denominator trước error rate

Error rate phụ thuộc tập request:

$$
error\_rate = \frac{failed\_requests}{eligible\_requests}
$$

Cần nói rõ:

- health checks có nằm trong denominator không;
- client cancellation tính thế nào;
- validation `4xx` là lỗi service, lỗi caller hay tách series;
- retry attempt hay logical request được đếm;
- streaming request hoàn tất khi nào;
- degraded response có được coi là success đầy đủ không.

Nếu không, hai dashboard cùng tên “error rate” có thể cho kết luận trái nhau.

## Duration phải là distribution

Average che tail. Chín request 10 ms và một request 1.000 ms có trung bình 109 ms nhưng 10% request chịu 1 giây. API cần histogram hoặc distribution cho p50/p95/p99 theo window và traffic đủ lớn.

Prometheus classic histogram đếm observation trong cumulative buckets và cho phép server-side aggregation; summary tính quantile ở client và thường không aggregate quantile giữa instance một cách hợp lệ. Native histogram có model khác và cần kiểm version/support.

> [!source-fact]
> Prometheus “Histograms and summaries” giải thích histogram bucket, summary quantile, lỗi khi lấy trung bình quantile và trade-off aggregation/accuracy; tài liệu cũng cảnh báo các ví dụ version cũ cần kiểm theo bản đang dùng.

## Bucket là một quyết định SLO

Nếu SLO là 95% request dưới 300 ms, histogram phải có bucket boundary hữu ích quanh 300 ms. Bucket quá thưa làm quantile interpolation kém; quá nhiều bucket nhân time series theo mọi label combination.

Để tính tỷ lệ request dưới SLO threshold với classic histogram:

```promql
sum(rate(http_request_duration_seconds_bucket{le="0.3"}[5m]))
/
sum(rate(http_request_duration_seconds_count[5m]))
```

Query chỉ đúng nếu numerator/denominator dùng cùng filter và bucket `le="0.3"` tồn tại. Không copy query khi metric name/units khác.

## Label cardinality là resource constraint

Label tốt có tập giá trị hữu hạn và phục vụ phân tích: route template, method, status class, service, region, deployment. Label nguy hiểm: user ID, request ID, full URL, SQL text, exception message hoặc object ID.

Raw identity nằm ở log/trace có retention và access control, không nằm trong metric label. Cardinality explosion tăng memory, ingestion, query latency và chi phí; đôi khi làm mất chính telemetry lúc sự cố.

## Structured logging

Log event nên là record có schema, không phải câu chữ tự do ghép bằng string. Trường nền:

- timestamp UTC và severity;
- service/version/environment/instance;
- event name và outcome;
- trace ID/span ID/request ID;
- route/operation;
- error class và stable reason code;
- duration, retry attempt hoặc dependency khi liên quan.

Không log raw token, password, secret, full connection string, payload chứa PII hoặc SQL parameters mặc định. Redaction phải test được. Error stack thuộc log hạn chế truy cập, không phải response gửi client.

## Request ID, trace ID và business ID

- request ID định danh một inbound request/attempt tại boundary;
- trace ID nối work qua nhiều hop trong một trace;
- span ID định danh operation trong trace;
- logical operation/idempotency key nối nhiều retry attempt của cùng ý định;
- business ID định danh order/job/resource.

Không dùng chúng thay nhau. Một logical operation có thể có nhiều request/trace do retry. Một trace có nhiều span. Trace ID do client gửi từ trust boundary có thể cần regenerate/validate; nó không phải authorization identity.

## Trace là đồ thị, không phải log dài

Span cần biểu diễn operation có boundary rõ: edge, handler, pool wait, database query, outbound RPC, serialization. Parent/child hoặc link thể hiện quan hệ. Duration child song song không cộng tuyến tính; critical path mới quyết định wall-clock.

Attribute hữu ích:

- route template và method;
- normalized outcome/status;
- peer/dependency name;
- database system/operation, không log statement nhạy cảm vô điều kiện;
- retry attempt và circuit-breaker outcome;
- queue wait/pool wait nếu instrument được.

Span quá nhỏ theo mỗi function tạo noise và overhead. Span quá rộng chỉ ghi “request 2 giây” nhưng không giải thích chặng nào.

## Context propagation qua ba chặng

Client/edge tạo hoặc nhận trace context theo trust policy. Service A tạo server span, outbound client span và inject context. Service B extract, tạo child server span và tiếp tục. Message queue có thể dùng parent hoặc span link tùy semantics.

Các điểm hay đứt:

- custom HTTP/RPC client không instrument;
- background task không truyền context;
- proxy xóa header;
- retry tạo trace mới không link attempt;
- async queue bỏ metadata;
- sampling decision không tương thích;
- library dùng thread-local sai trong async runtime.

Phép thử propagation phải gửi một request qua ba hop và query backend để chứng minh cùng trace graph, không chỉ assert header tồn tại trong unit test.

## Sampling và điều không nhìn thấy

Head sampling quyết định sớm, rẻ nhưng có thể bỏ failure hiếm. Tail sampling xem outcome/latency trước quyết định giữ, nhưng cần collector buffer và capacity. Có thể giữ 100% error/slow trace và sample success, song policy phải xử lý overload và privacy.

Missing span không chứng minh component không chạy. Có thể do sampling, exporter mất dữ liệu, process chết trước flush, context đứt hoặc query sai window. Đối chiếu access log, metrics, collector health và downstream evidence.

## Exemplars và liên kết signal

Một histogram observation có thể gắn exemplar trace ID để operator đi từ latency spike tới trace cụ thể. Log mang trace/span ID cho phép chuyển từ trace sang event detail. Resource attributes nối signal với service version và deployment.

Correlation phải được kiểm sau deploy. Nếu metric spike nhưng exemplar không resolve, hoặc log query theo trace ID không có kết quả do field mapping khác, hệ thống chưa đạt objective chẩn đoán.

## Dashboard theo câu hỏi

Dashboard API tối thiểu:

1. traffic rate theo route và outcome;
2. error ratio cùng denominator rõ;
3. p50/p95/p99 hoặc SLO bucket duration;
4. in-flight/queue/pool wait và saturation;
5. dependency latency/error/circuit state;
6. deployment/version annotation;
7. link từ panel sang logs/traces đã giữ filter.

Không gộp mọi route. Endpoint health nhẹ sẽ che endpoint export chậm. Đồng thời dashboard quá chi tiết theo raw ID không scale.

## Ba câu hỏi chẩn đoán mẫu

### Câu hỏi A: Chậm ở service hay dependency?

Xem route p95, chọn exemplar trace, so handler self-time, pool wait và child dependency spans. Kết luận phải nói đúng trace/window, không quy toàn hệ từ một mẫu.

### Câu hỏi B: Error tăng từ deploy hay từ input?

Tách error class/status, so deployment annotation, version attribute và stable reason code. Validation `4xx` tăng cùng một client không giống server `5xx` sau rollout.

### Câu hỏi C: Vì sao endpoint độc lập cũng chậm?

Kiểm shared pool/worker saturation, queue age và L107 bulkhead metrics. Dependency span không xuất hiện ở endpoint độc lập nhưng shared resource wait có thể là nguyên nhân.

## Liveness, readiness và startup

- **Liveness**: process có ở trạng thái cần restart không;
- **Readiness**: instance hiện có nên nhận traffic cho contract được khai báo không;
- **Startup**: ứng dụng đã hoàn tất khởi động ban đầu chưa.

Không biến liveness thành deep dependency check; database outage có thể khiến mọi pod restart và làm sự cố nặng hơn. Readiness có thể phụ thuộc database nếu instance thật sự không phục vụ được critical API khi DB mất, nhưng cần tránh mọi replica đồng loạt rời load balancer gây blackout hoặc retry storm.

Yêu cầu roadmap “readiness đổi khi mất database” phải được cài theo contract cụ thể: endpoint nào cần DB, degraded mode có tồn tại không, threshold/hysteresis ra sao, và external traffic sẽ đi đâu. Không có một health policy đúng cho mọi service.

## Readiness không thay dependency metrics

Boolean ready/unready không cho biết latency, partial failure hay capacity. Cần metric dependency health, pool saturation và breaker state. Readiness là control-plane signal có hậu quả routing; dùng nó làm dashboard duy nhất là mất thông tin.

Health endpoint phải nhẹ, có timeout và không lộ secret/version nội bộ quá mức. Probe traffic được tách khỏi business RED metrics để denominator không méo.

## Failure matrix

| Failure | Triệu chứng | Phép kiểm | Biện pháp |
|---|---|---|---|
| Average-only latency | dashboard xanh nhưng user tail chậm | inject 10% slow requests | histogram + percentile/SLO bucket |
| Route aggregation | endpoint lỗi bị health traffic che | filter route template | bounded route labels |
| High-cardinality metric | TSDB tăng series đột biến | count series by label | chuyển raw ID sang log/trace |
| Broken propagation | trace tách ở hop B | three-hop trace test | instrument inject/extract |
| Log không correlate | trace ID không query được | round-trip link test | schema thống nhất |
| Missing telemetry | không có span lúc crash | kill before flush | metrics/log/collector cross-check |
| Probe cascade | DB down làm mọi pod restart/unready | dependency outage drill | tách liveness, readiness policy có hysteresis |
| Secret leakage | token/payload trong log | seeded-secret scanner | redaction + allowlist fields |

## Giới hạn

- Metric names và query trong note là minh họa; implementation phải theo library/runtime hiện hành.
- Prometheus classic/native histogram và OpenTelemetry SDK thay đổi theo version; phải ghim tài liệu khi triển khai.
- Trace sampling không tạo exhaustive audit; security audit cần pipeline và retention riêng.
- Readiness semantics phụ thuộc service contract và platform routing.
- “Trả lời không đọc code” áp cho câu hỏi đã instrument đủ; không hứa telemetry biết mọi internal state.

## Reference

1. [[SRC-TITMUS-CLOUD-NATIVE-GO-1E]] — observability, instrumentation, tracing, metrics và logging; PDF 365–373, 391–393, 409–412.
2. [[SRC-OPENTELEMETRY-SIGNALS]] — traces, metrics, logs, baggage và khái niệm signal; truy cập 2026-09-28.
3. [[SRC-PROMETHEUS-HISTOGRAMS]] — histogram/summary, bucket, quantile, aggregation và sai lầm lấy trung bình quantile; truy cập 2026-09-28.

## Source coverage

| Source slice | Nội dung phải giữ | Vị trí trong note | Trạng thái |
|---|---|---|---|
| [[SRC-TITMUS-CLOUD-NATIVE-GO-1E]], PDF 365–373, 391–393, 409–412 | observability property, traces, metrics và logs | §§1–2, 8–12 | Đã trình bày cơ chế, không nâng tool thành guarantee |
| [[SRC-OPENTELEMETRY-SIGNALS]] | signal taxonomy và trace context concepts | §§2, 9–13 | Đã dùng theo tài liệu dự án chính thức |
| [[SRC-PROMETHEUS-HISTOGRAMS]] | distribution, quantile, histogram/summary trade-off | §§5–7 | Đã giữ cảnh báo aggregation và version |
| Tổng hợp DE-L108 | RED contract, denominator, dashboard, readiness policy, test harness | §§3–4, 14–20 | Đã ghi thành synthesis và evidence có thể kiểm |

Phạm vi đọc bao phủ metric/log/trace, RED, histogram, propagation, sampling, correlation, health signal và fault-based diagnosis. SLO/error-budget governance đầy đủ được dành cho module vận hành sau.

## Key takeaways

- RED là rate, errors và duration theo route/outcome đã chuẩn hóa; mọi tỷ lệ phải có denominator rõ.
- Duration là distribution; average không đại diện tail và quantile không được cộng/trung bình tùy tiện.
- Metric label phải bounded; request/object identity thuộc log hoặc trace.
- Trace chỉ hữu ích khi context truyền qua boundary và có thể nối metric → trace → log.
- Missing span không chứng minh code path không chạy; phải kiểm telemetry pipeline và signal khác.
- Liveness, readiness và dependency health là ba thứ khác nhau; probe sai có thể khuếch đại outage.
