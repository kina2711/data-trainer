# Phase 3: Software and Backend Engineering
# Module 8: Backend and API Engineering
# Lesson 109: The outbox pattern - one atomic write

## Mục tiêu bài học

**Năng lực cần chứng minh.** Cài mẫu hộp thư đi và chứng minh bằng thí nghiệm giết tiến trình rằng cơ sở dữ liệu và luồng sự kiện không lệch nhau.

**Điều kiện hoàn thành.** Bản ngây thơ có mức lệch đo được, bản hộp thư đi không thiếu sự kiện nào qua 20 lần giết, và bảng hộp thư được dọn tự động.

> [!abstract] Câu hỏi trung tâm
> Một request vừa phải thay đổi trạng thái trong database vừa phải phát event. Nếu process chết giữa hai thao tác, làm thế nào để không tạo trạng thái “đã ghi nhưng không có event” hoặc “có event nhưng chưa ghi”?

## 1. Dual write là lỗi mô hình, không phải lỗi hiếm

Đoạn mã `UPDATE database; publish message;` chứa hai commit point độc lập. Nếu database commit xong rồi broker timeout hoặc process chết, state đã đổi nhưng downstream không biết. Đảo thứ tự thành publish trước rồi update chỉ đổi hướng sai lệch: consumer có thể xử lý event của một transaction sau đó rollback. Retry không khôi phục được sự thật vì caller không biết publish đã thành công trước khi connection đứt hay chưa.

Bốn trạng thái phải được liệt kê trước khi chọn giải pháp:

| DB | Broker | Ý nghĩa |
|---|---|---|
| chưa commit | chưa publish | không có thay đổi |
| commit | chưa publish | mất event |
| chưa commit | publish | event ma |
| commit | publish | trường hợp mong muốn |

Distributed transaction có thể hợp nhất commit point khi cả hai resource tham gia protocol, nhưng làm tăng coupling, availability cost và operational complexity. Transactional outbox chọn một nguồn chân lý cục bộ: database.

## 2. Invariant của outbox

Business row và outbox row được ghi trong **cùng local database transaction**. Commit thành công thì cả hai cùng tồn tại; rollback thì cả hai cùng mất. Relay chạy riêng, đọc outbox rồi publish. Invariant cốt lõi là:

$$
business\_commit \iff outbox\_intent\_exists
$$

Đây chưa phải `exactly once`. Nó chỉ loại bỏ khoảng hở giữa business write và việc ghi nhận ý định phát message. Khoảng hở publish vẫn tồn tại và được xử lý bằng at-least-once cùng deduplication.

## 3. Schema phải giữ đủ ý nghĩa

Một outbox row tối thiểu cần `event_id`, aggregate/resource ID, event type, payload hoặc payload reference, schema version, occurred-at, created-at và ordering key. Trạng thái relay có thể là `pending/published/failed`, kèm attempt count, next-attempt-at, published-at và error class.

`event_id` phải ổn định qua retry. Không sinh ID mới mỗi lần relay phát lại. Payload nên là snapshot của contract tại thời điểm transaction, không dựng lại từ business table sau đó vì state có thể đã đổi. Schema version giúp consumer giải mã rõ ràng. Không đưa secret hoặc trường không thuộc public event contract vào payload.

## 4. Transaction boundary đúng

Handler bắt đầu transaction, kiểm invariant, thay đổi business row, insert outbox row rồi commit. Không gọi broker trong transaction: network wait kéo dài lock và vẫn không đưa broker vào local atomicity. Cũng không enqueue background task chỉ trong memory; process chết sau commit sẽ làm mất task.

Nếu một command được retry với idempotency key, transaction nên kiểm deduplication state và tạo cùng logical result. Nếu command duplicate tạo hai outbox row khác nhau, consumer phải suy đoán ý định mà producer lẽ ra đã giữ.

## 5. Relay và claim protocol

Polling relay lặp: chọn batch sẵn sàng, claim, publish, ghi kết quả. Nhiều worker không được vô tình cùng claim tất cả row. Với PostgreSQL, một thiết kế có thể dùng row lock và `SKIP LOCKED`, hoặc lease có owner/expiry. Đây là lựa chọn triển khai, không phải thuộc tính phổ quát của pattern.

Giữ database transaction mở trong khi gọi broker cho phép lock batch nhưng tăng contention. Claim rồi commit trước khi publish giảm lock time nhưng cần lease recovery. Batch quá lớn tăng latency và blast radius; batch quá nhỏ tăng round trip. Cần đo backlog age, batch duration, publish error và attempt count.

## 6. Published-but-not-marked là failure bắt buộc

Relay có thể publish thành công, rồi chết trước `UPDATE outbox SET published_at=...`. Khi khởi động lại, nó phát lại cùng `event_id`. Vì vậy delivery thực tế là at-least-once.

Consumer phải lưu processed-message ID cùng transaction với side effect cục bộ, hoặc downstream operation phải nhận idempotency key. Trình tự “check đã thấy chưa; xử lý; rồi ghi đã thấy” không atomic vẫn race. Nếu external side effect không hỗ trợ idempotency, cần reconciliation hoặc protocol riêng; không được ghi nhãn exactly-once.

## 7. Ordering cần scope rõ

Global order thường vừa đắt vừa không cần. Điều cần thiết thường là per-aggregate order. Có thể lưu aggregate ID và sequence, partition broker theo ordering key, đồng thời consumer phát hiện gap. Nhiều relay đồng thời, retry và broker partition đều có thể thay thứ tự quan sát. Timestamp không phải total-order proof vì clock skew và concurrent transaction.

Nếu event 12 đến trước 11, consumer có thể buffer, reject/retry hoặc áp dụng state-version rule. Policy phải gắn với domain; không có một đáp án chung.

## 8. Retention và cleanup là phần correctness vận hành

Outbox tăng vô hạn làm index phình, vacuum/backup chậm và poll query tệ. Không xoá ngay sau publish nếu cần replay hoặc audit; không giữ vô hạn nếu không có retention requirement. Một policy có thể partition theo thời gian, giữ published rows trong khoảng xác định, archive nếu cần rồi drop partition.

Cleanup phải có metric: oldest pending age, total pending, publish lag, rows deleted, cleanup failure. Xoá theo `created_at` mà bỏ qua trạng thái có thể xoá message chưa phát. Xoá row đang retry cũng phá delivery.

## 9. Thí nghiệm kill-point

Baseline naive chạy 20 lần, chủ động kill sau DB commit trước publish. Mỗi run ghi command ID, business state, broker event và thời điểm kill. Divergence rate là số run DB đã đổi nhưng thiếu event chia tổng run tại kill point.

Sau đó thay bằng outbox. Kill ở ba điểm: trước commit, sau commit trước relay, và sau publish trước mark. Kỳ vọng: điểm một không có business row/outbox; điểm hai có cả hai và relay phục hồi; điểm ba có duplicate cùng event ID nhưng không mất event. Consumer dedup phải chứng minh side effect chỉ xảy ra một lần.

## 10. Điều outbox không giải quyết

Outbox không tự giải quyết schema compatibility, poison message, consumer side effect, authorization, ordering toàn cục, broker retention hoặc multi-database atomicity. Nó cũng không biến asynchronous workflow thành synchronous consistency. Read model có thể trễ và product contract phải thừa nhận.

## 11. Bằng chứng đạt bài

- 20 kill run naive có bảng đối chiếu DB/event và thấy divergence có chủ đích.
- 20 kill run outbox không mất event; duplicate được nhận diện bằng stable event ID.
- Có test published-but-not-marked và consumer side effect không lặp.
- Có metric backlog age, attempts, publish failure và runbook relay stuck.
- Cleanup chạy tự động nhưng không xoá pending/leased row.

## 12. Phân tích failure theo timeline

Một phép thử có giá trị phải đánh dấu chính xác các mốc `T0 begin`, `T1 business write`, `T2 outbox insert`, `T3 commit`, `T4 broker ack`, `T5 mark published`. Kill trước T3 phải để cả business row lẫn outbox row biến mất. Kill từ T3 đến T4 để lại durable intent và relay phải phục hồi. Kill từ T4 đến T5 tạo một lần phát lại có cùng event ID. Nếu event ID thay đổi, phép dedup không còn biết đó là cùng logical message.

Broker acknowledgement cũng không chứng minh consumer side effect đã commit. Vì vậy evidence phải tách producer delivery, broker acceptance và consumer outcome. Ba counter độc lập giúp tránh kết luận sai từ việc chỉ đếm message ở topic. Với consumer dùng database, processed-message record và domain mutation phải cùng transaction. Với API ngoài, lưu external operation ID và reconciliation status.

## 13. Vận hành khi relay bị kẹt

Alert không nên chỉ dựa trên số pending vì traffic thấp có thể làm số này nhỏ trong khi message cũ bị kẹt. `oldest_pending_age` so với delivery objective là signal trực tiếp hơn. Runbook kiểm database connectivity, claim lease, poison payload, broker error, credential, partition và deployment version. Pause relay trước khi sửa dữ liệu; không đánh dấu published bằng tay nếu chưa có broker evidence.

Replay phải chọn theo event ID/range, có dry-run, authorization và audit. Nếu replay sau khi consumer đã quên dedup ID do retention ngắn, side effect có thể lặp. Retention producer, broker và consumer dedup phải được thiết kế cùng một recovery window.

## 14. Câu hỏi tự kiểm tra

1. Vì sao local transaction chỉ bảo đảm business row và outbox intent, không bảo đảm consumer đã xử lý?
2. Tại sao relay có thể phát trùng ngay cả khi broker không hỏng?
3. Per-aggregate ordering cần những trường và partition rule nào?
4. Cleanup dựa riêng vào `created_at` có thể làm mất message ra sao?
5. Evidence nào phân biệt “không mất intent” với “exactly-once side effect”?

## 15. Giới hạn và điều chưa cho phép kết luận

- Hai mươi kill run là acceptance evidence trong lab, không phải chứng minh hình thức cho mọi interleaving.
- Pattern không tạo global order, synchronous consistency hoặc atomicity qua nhiều database.
- `SKIP LOCKED`, lease và schema trong note là lựa chọn PostgreSQL-oriented, phải kiểm lại ở DBMS khác.
- Không được gọi delivery exactly-once nếu downstream effect và dedup boundary chưa được chứng minh.

Một giới hạn khác là thay đổi schema event trong thời gian outbox còn backlog. Relay có thể phát payload do phiên bản ứng dụng cũ tạo sau khi producer mới đã triển khai. Consumer vì vậy phải giải mã theo `schema_version`, còn deployment phải kiểm backward/forward compatibility trong đúng retention window. Không được migrate payload cũ bằng cách đọc business row hiện tại vì làm mất snapshot tại thời điểm event phát sinh. Nếu buộc phải backfill, tạo migration có audit, giữ original event ID và chứng minh không tạo thêm business intent.

## Source coverage

| Source slice | Nội dung phải giữ | Vị trí trong note | Trạng thái |
|---|---|---|---|
| [[SRC-RICHARDSON-MICROSERVICES-PATTERNS-1E]], PDF 120–139 | transactional messaging, outbox, relay và duplicate | §§1–6 | Đã trình bày, không đổi at-least-once thành exactly-once |
| [[SRC-MICROSERVICES-IO-TRANSACTIONAL-OUTBOX]] | forces, local atomic write, ordering, idempotent consumer | §§2–7 | Đã giữ giới hạn của pattern |
| [[SRC-MICROSERVICES-IO-POLLING-PUBLISHER]] | polling relay và giới hạn ordering | §§5–7 | Đã phân biệt pattern với claim algorithm |
| Tổng hợp DE-L109 | schema, kill matrix, cleanup, runbook | §§3, 8–13 | Đã gắn thành synthesis và evidence kiểm được |

## Key takeaways
- Outbox hợp nhất business change và ý định phát event trong một local commit.
- Relay vẫn có thể phát lặp; stable event ID và idempotent consumer là bắt buộc.
- Ordering phải định nghĩa theo scope; timestamp không phải bằng chứng total order.
- Retention, backlog metric và cleanup thuộc correctness vận hành.
- Chỉ claim điều đã chứng minh: no lost intent và controlled duplicate, không phải exactly-once tuyệt đối.

## Reference
1. [[SRC-RICHARDSON-MICROSERVICES-PATTERNS-1E]] — PDF 120–139.
2. [[SRC-MICROSERVICES-IO-TRANSACTIONAL-OUTBOX]] — pattern forces và result.
3. [[SRC-MICROSERVICES-IO-POLLING-PUBLISHER]] — polling relay.
