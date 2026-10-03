# Phase 3: Software and Backend Engineering
# Module 8: Backend and API Engineering
# Lesson 103: Transaction boundaries and the unit of work

## Mục tiêu bài học

**Năng lực cần chứng minh.** Đặt đúng ranh giới giao dịch cho ba ca sử dụng và chứng minh không còn trạng thái dở dang khi lỗi giữa chừng.

**Điều kiện hoàn thành.** Ba ca sử dụng không để lại trạng thái dở dang khi lỗi, số truy vấn mỗi yêu cầu trong ngưỡng, và tái hiện được hồ kết nối cạn.

> [!abstract] Câu hỏi trung tâm
> Một use case ghi nhiều bảng, gọi repository và có thể phát sinh tác động bên ngoài. Phần nào phải commit cùng nhau, tầng nào sở hữu quyết định đó, và bằng chứng nào cho thấy lỗi giữa chừng không để lại trạng thái dở dang?

## Bắt đầu từ invariant, không bắt đầu từ API của ORM

Ranh giới giao dịch trả lời một câu hỏi nghiệp vụ: những thay đổi nào phải cùng thành công hoặc cùng thất bại để trạng thái sau use case vẫn hợp lệ? `BEGIN`, `COMMIT`, decorator hay context manager chỉ là phương tiện cài đặt câu trả lời đó.

Ví dụ use case xác nhận đơn hàng phải đồng thời đổi trạng thái đơn, ghi reservation và tạo audit record. Nếu ba thay đổi thuộc cùng một database và invariant yêu cầu chúng xuất hiện như một đơn vị, ba thay đổi phải nằm trong cùng local transaction. Nếu mỗi repository tự commit, lỗi ở bước thứ ba sẽ để lại hai thay đổi đầu tiên dù use case chưa hoàn tất.

Một boundary tốt có bốn đặc điểm:

1. bao trọn các database change cần atomic cùng nhau;
2. không bao trọn thời gian chờ không cần thiết;
3. có owner rõ ràng chịu trách nhiệm commit hoặc rollback;
4. có phép thử tiêm lỗi chứng minh trạng thái cuối.

## Năm khái niệm thường bị trộn

| Khái niệm | Phạm vi | Trách nhiệm |
|---|---|---|
| Business transaction | mục tiêu nghiệp vụ có thể kéo dài qua nhiều bước hoặc request | mô tả điều người dùng muốn hoàn tất |
| Application use case | một lần điều phối cụ thể trong ứng dụng | kiểm quyền, gọi domain, repository và outbound port |
| Database transaction | một atomic boundary do database quản lý | commit hoặc rollback thay đổi trong resource đó |
| Unit of Work | pattern theo dõi và điều phối persistence change | flush, commit, rollback và concurrency bookkeeping |
| Session/connection | resource kỹ thuật | giữ state giao tiếp với database và thực thi statement |

Business transaction không mặc nhiên là database transaction. Quy trình “đăng ký tài khoản rồi xác minh email” có thể kéo dài nhiều phút; không được giữ database transaction mở qua lúc chờ người dùng. Ngược lại, một use case ngắn có thể cần một database transaction bao trọn nhiều repository call.

> [!source-fact]
> Fowler định nghĩa Unit of Work là pattern theo dõi object bị tác động trong một business transaction, rồi điều phối việc ghi thay đổi và xử lý concurrency. Định nghĩa này nói về trách nhiệm của pattern, không yêu cầu một class hay framework cụ thể. *Unit of Work*, martinfowler.com, truy cập 2026-09-28.

## Aggregate boundary và transaction boundary

Aggregate gom các domain object phải giữ invariant nhất quán tức thời. Aggregate root là cổng thay đổi. Quy tắc hữu dụng là một transaction nên sửa càng ít aggregate càng tốt; nếu một use case thường xuyên phải khóa và sửa nhiều aggregate, cần kiểm lại model, invariant và ownership.

Quy tắc này không có nghĩa “một aggregate bằng một bảng”. Một aggregate có thể ánh xạ vào nhiều bảng. Repository nên phục vụ aggregate hoặc use case ổn định, không máy móc tạo một repository cho mỗi table.

> [!source-fact]
> Boyle trình bày aggregate như transaction boundary của các domain object bên trong, repository theo aggregate thay vì theo table, và application service như nơi phối hợp repository cùng transactional guarantee. *Domain-Driven Design with Golang*, Chapter 3–4, PDF 66–88.

## Boundary mặc định nằm ở application service

Application service biết toàn bộ use case: cần đọc gì, thay đổi invariant nào, gọi mấy repository và khi nào có thể trả kết quả. Repository chỉ biết lưu hoặc truy vấn một abstraction; nó không biết thao tác của mình là bước duy nhất hay bước thứ hai trong chuỗi ba bước.

Vì vậy default hợp lý là application layer sở hữu Unit of Work:

```text
inbound adapter
  -> application use case
       -> begin unit of work
       -> load aggregate through repository
       -> execute domain behavior
       -> persist aggregate and audit intent
       -> commit
  <- map result to transport response
```

Repository có thể dùng connection hoặc session do Unit of Work cung cấp. Nó không tự commit khi caller còn cần phối hợp thao tác khác. Domain layer không biết transaction API, ORM session hoặc connection pool.

> [!synthesis]
> “Một use case — một transaction” là default thiết kế của khóa học cho use case ngắn trên một database, tổng hợp từ vai trò application service của Boyle, Unit of Work của Fowler và transaction block của PostgreSQL. Đây không phải luật tuyệt đối: read-only stream dài, chunked batch, workflow nhiều request và thao tác qua nhiều service cần boundary khác.

## State machine của Unit of Work

Unit of Work nên có lifecycle nhìn thấy được:

```text
NEW
  -> ACTIVE
       -> COMMITTING -> COMMITTED
       -> ROLLING_BACK -> ROLLED_BACK
       -> FAILED -> ROLLING_BACK
  -> CLOSED
```

Các invariant cần giữ:

- chỉ commit một lần;
- exception trước commit dẫn tới rollback;
- lỗi commit không được báo thành công;
- close luôn giải phóng connection/session;
- repository trong cùng Unit of Work dùng cùng transaction context;
- object từ Unit of Work này không bị dùng ngầm trong một transaction đồng thời khác.

Một context manager giúp gom đường thành công và đường lỗi:

```python
def confirm_order(command, uow):
    with uow:
        order = uow.orders.get(command.order_id)
        order.confirm(command.actor_id)
        uow.reservations.add_for(order)
        uow.audit.append("order_confirmed", order.id)
        uow.commit()
```

Đoạn mã chỉ minh họa ownership. Cần quyết định rõ context manager auto-commit hay explicit commit. Explicit commit làm điểm thay đổi trạng thái dễ thấy; auto-commit giảm boilerplate nhưng có thể commit ngoài ý định nếu block chứa thêm code.

## Database transaction thực sự bảo đảm điều gì?

Trong PostgreSQL, các statement giữa `BEGIN` và `COMMIT` tạo một transaction block. `ROLLBACK` hủy thay đổi của block. Nếu không mở block tường minh, mỗi statement riêng vẫn chạy trong transaction ngầm. Vì vậy hai lệnh `UPDATE` kế tiếp nhau ở autocommit là hai atomic unit khác nhau, không phải một use case atomic.

Savepoint cho phép quay lại một điểm bên trong transaction nhưng không sống sau khi transaction kết thúc. Nó không phải cơ chế undo cho email đã gửi, request đã gọi sang payment gateway hay event đã publish ngoài database.

> [!source-fact]
> PostgreSQL chỉ commit transaction không lỗi; sau một statement error, transaction vào trạng thái aborted cho tới khi rollback toàn bộ hoặc rollback về savepoint phù hợp. *Mastering PostgreSQL 17*, Chapter 2, PDF 49–55; PostgreSQL Documentation, “Transactions”, truy cập 2026-09-28.

Atomicity cũng không tự chọn isolation level đúng. Transaction vẫn có thể gặp lost update, write skew hoặc serialization failure tùy isolation và access pattern. L103 tập trung vào boundary; concurrency control được xử lý ở L104.

## Flush không đồng nghĩa commit

ORM thường giữ thay đổi trong memory rồi flush SQL trước query hoặc commit. Flush thành công chỉ chứng minh statement đã được database chấp nhận trong transaction hiện tại; transaction vẫn có thể rollback sau đó.

Trong SQLAlchemy, Session giữ identity map, theo dõi object thay đổi, flush pending state và quản lý transaction trên connection. Khi commit hoặc rollback hoàn tất, connection được trả về pool. Session là mutable stateful object, không an toàn để dùng đồng thời giữa các thread hoặc task.

> [!source-fact]
> SQLAlchemy mô tả Session như implementation của Unit of Work: thay đổi được ghi nhận, flush trước query hoặc commit, transaction giữ connection và connection trở lại pool khi transaction kết thúc. *SQLAlchemy 2.0 Session Basics*, truy cập 2026-09-28.

Do đó log “flush succeeded” hoặc số row affected chưa phải bằng chứng use case đã commit. Evidence phải lấy ở ranh giới commit hoặc bằng đọc lại từ transaction độc lập.

## External call không rollback cùng database

Giả sử use case thực hiện:

1. mở database transaction;
2. cập nhật order;
3. gọi payment API;
4. ghi audit;
5. commit.

Nếu bước 4 hoặc 5 lỗi sau khi payment đã thành công, database rollback nhưng payment không tự đảo. Giữ external call trong transaction còn làm lock và connection sống suốt network latency. Đưa external call ra sau commit lại tạo cửa sổ database đã commit nhưng call chưa chạy.

Không có cách sắp xếp đơn giản nào biến hai resource độc lập thành một local atomic transaction. Các lựa chọn phải được nêu đúng bản chất:

- lưu intent/outbox cùng database transaction rồi worker thực hiện side effect;
- dùng idempotency key và reconciliation;
- dùng saga với compensating action khi nghiệp vụ cho phép;
- dùng distributed transaction chỉ khi toàn bộ stack và yêu cầu vận hành thật sự hỗ trợ.

> [!source-fact]
> Richardson phân biệt local ACID transaction trong một service với operation trải nhiều service; saga là chuỗi local transaction và việc “lùi” cần compensating transaction vì mỗi bước đã commit riêng. *Microservices Patterns*, Chapter 4, PDF 140–149.

L103 chỉ thiết lập ranh giới vấn đề. Transactional outbox được triển khai ở L109; không dùng tên pattern để che lỗ hổng chưa cài.

## Connection pool là tài nguyên của transaction

Khi transaction bắt đầu làm việc với database, nó thường checkout một connection. Connection đó không phục vụ request khác cho tới khi transaction kết thúc và resource được trả về pool. Vì vậy transaction duration trực tiếp ảnh hưởng khả năng phục vụ đồng thời.

> [!inference]
> Với pool có `P` connection và thời gian giữ connection trung bình `T`, trần throughput gần đúng do pool áp đặt là `P/T` transaction mỗi đơn vị thời gian trước khi xét database capacity. Đây là ứng dụng Little’s Law cho capacity reasoning, không phải cam kết hiệu năng của PostgreSQL hay SQLAlchemy.

Ví dụ pool 20 connection, mỗi transaction giữ 50 ms có trần lý tưởng khoảng 400 transaction/giây. Nếu chèn external call 2 giây vào boundary, cùng pool chỉ còn khoảng 10 transaction/giây; request mới xếp hàng ở pool dù database chưa dùng hết CPU.

Metric cần tách:

- thời gian chờ checkout connection;
- thời gian connection được giữ;
- thời gian query chạy;
- thời gian chờ lock;
- số transaction `idle in transaction`;
- timeout hoặc pool exhaustion count.

Không gom mọi thứ thành “database latency”. Query 5 ms có thể nằm trong request 2 giây nếu connection bị giữ khi gọi hệ ngoài.

## Transaction dài gây hại ngoài việc giữ pool

Transaction dài có thể giữ lock, kéo dài visibility horizon, làm vacuum/reclamation khó tiến, tăng xác suất conflict và khiến rollback tốn hơn. Một transaction “không chạy query” nhưng đang `idle in transaction` vẫn là transaction chưa kết thúc.

PostgreSQL 17 có `transaction_timeout` để chặn transaction vượt thời lượng cấu hình, nhưng timeout chỉ là guardrail. Nó không thay việc sửa ownership và rút external wait khỏi boundary.

> [!source-fact]
> Schönig mô tả `transaction_timeout` như cơ chế kết thúc transaction quá dài và đóng connection; Chapter 2 đồng thời cho thấy lock khiến session khác phải chờ. *Mastering PostgreSQL 17*, PDF 30–34 và 49–62.

## N+1 query là lỗi boundary quan sát được

N+1 xảy ra khi ứng dụng lấy danh sách bằng một query rồi truy vấn thêm cho từng phần tử. Nó thường ẩn sau lazy loading nên code nhìn ngắn nhưng query count tăng theo kích thước kết quả.

Phép kiểm cần đo query count theo request với dataset có kích thước khác nhau:

| Số order | Kỳ vọng tốt | Dấu hiệu N+1 |
|---:|---:|---:|
| 1 | hằng số nhỏ | khó nhận ra |
| 10 | gần như không đổi | khoảng 11 hoặc 21 query |
| 100 | gần như không đổi | khoảng 101 hoặc 201 query |

Không đặt một ngưỡng tùy ý rồi coi là chân lý. Trước hết xác định access pattern; sau đó chọn eager load, explicit join, batch query hoặc projection. Một query khổng lồ cũng có thể tệ vì nhân bản row và truyền dữ liệu thừa.

## Ba use case để kiểm boundary

### A. Tạo order và line item

Order, line item và audit record cùng thuộc postcondition atomic. Tiêm lỗi sau khi ghi order nhưng trước line item; transaction phải rollback toàn bộ. Đọc lại bằng connection mới phải không thấy order mồ côi.

### B. Chuyển reservation giữa hai owner

Hai update phải cùng commit để tổng quantity không đổi. Tiêm lỗi giữa debit và credit. Ngoài kiểm “không dở dang”, cần chạy cạnh tranh ở L104 vì boundary đúng chưa đủ ngăn anomaly dưới isolation không phù hợp.

### C. Xác nhận order và gửi thông báo

Order state và notification intent có thể ghi atomic vào database; việc gửi thật nằm ngoài local transaction. Tiêm lỗi worker không được làm mất intent, và retry không được gửi side effect trùng nếu downstream yêu cầu idempotency.

## Failure injection phải quan sát từ bên ngoài

Một test chỉ assert `rollback()` được gọi trên mock chưa chứng minh database đã quay lại trạng thái hợp lệ. Phép thử mạnh hơn dùng database thật:

1. tạo fixture có invariant biết trước;
2. mở use case qua public entry point;
3. tiêm lỗi sau từng mutation quan trọng;
4. kết thúc request;
5. đọc lại bằng connection hoặc Unit of Work mới;
6. kiểm invariant, row count, audit/outbox và query count;
7. kiểm pool không mất connection.

Các fault point tối thiểu: trước first write, giữa hai write, sau flush nhưng trước commit, trong commit, và sau commit trước response. Fault sau commit tạo outcome uncertainty: client có thể thấy timeout dù state đã commit. Retry policy phải dựa trên idempotency/reconciliation, không giả định timeout là rollback.

## Observability cho transaction boundary

Một span use case cần có các mốc `uow.begin`, `db.checkout`, `db.query`, `uow.commit` hoặc `uow.rollback`, `db.checkin`. Không log dữ liệu nhạy cảm hoặc SQL parameter nguyên văn nếu có PII.

Các thuộc tính hữu ích:

- use-case name và correlation ID;
- transaction outcome;
- query count và tổng query duration;
- checkout wait và connection hold time;
- rollback reason theo error class;
- rows affected ở mức aggregate;
- external-call duration được chứng minh nằm ngoài transaction.

Log “request failed” không đủ phân biệt lỗi trước commit, lỗi commit hay response bị đứt sau commit.

## Anti-pattern và cách nhận diện

| Anti-pattern | Triệu chứng | Nguyên nhân | Phép sửa |
|---|---|---|---|
| Repository tự commit | trạng thái dở dang giữa nhiều repo | boundary bị chia theo class | application service sở hữu UoW |
| Session toàn cục | object và transaction state rò giữa request | scope không rõ | session/UoW theo use case hoặc request |
| External call trong transaction | pool cạn, lock dài | gom mọi side effect vào atomicity giả | intent/outbox hoặc workflow tách pha |
| Flush được coi là thành công | trả response trước commit | nhầm statement success với transaction success | response sau commit; test bằng connection mới |
| Catch exception rồi tiếp tục | transaction aborted, lệnh sau tiếp tục lỗi | nuốt trạng thái database | rollback hoặc rollback về savepoint có chủ đích |
| Mock-only rollback test | test xanh nhưng row vẫn dở dang | chỉ kiểm interaction | integration test với database thật |
| N+1 không được đo | latency tăng theo số row | lazy load trong vòng lặp | query-count test và load strategy rõ |

## Giới hạn

- Note dùng PostgreSQL và SQLAlchemy để làm rõ cơ chế; framework khác có lifecycle khác và phải đọc tài liệu tương ứng.
- Boundary đúng không tự giải quyết isolation anomaly; phần đó thuộc L104.
- Local transaction không tạo atomicity qua database, message broker và external API.
- Công thức capacity chỉ là mô hình gần đúng; pool size phải đo cùng database limit và workload.
- L103 không triển khai outbox, saga hay distributed transaction; chúng chỉ xuất hiện để đánh dấu ranh giới của local Unit of Work.

## Reference

1. [[SRC-BOYLE-DDD-GOLANG-1E]] — aggregate, repository và application service, PDF 66–88.
2. [[SRC-MASTERING-POSTGRESQL-17-6E]] — transaction state, savepoint, timeout và locking, PDF 30–34, 49–62.
3. [[SRC-RICHARDSON-MICROSERVICES-PATTERNS-1E]] — local ACID transaction, saga và compensation, PDF 140–149.
4. [[SRC-POSTGRESQL-TRANSACTIONS]] — transaction block và savepoint; truy cập 2026-09-28.
5. [[SRC-SQLALCHEMY-SESSION-BASICS]] — Session, Unit of Work, flush và pool lifecycle; truy cập 2026-09-28.
6. [[SRC-FOWLER-UNIT-OF-WORK]] — định nghĩa Unit of Work; truy cập 2026-09-28.

## Source coverage

| Source slice | Nội dung phải giữ | Vị trí trong note | Trạng thái |
|---|---|---|---|
| [[SRC-BOYLE-DDD-GOLANG-1E]], PDF 66–88 | aggregate transaction boundary, repository theo aggregate, application service | §§3–4 | Đã trình bày cùng giới hạn mô hình |
| [[SRC-MASTERING-POSTGRESQL-17-6E]], PDF 30–34, 49–62 | transaction state, rollback, savepoint, long transaction và locking | §§6, 9–10 | Đã trình bày cơ chế và tác động vận hành |
| [[SRC-RICHARDSON-MICROSERVICES-PATTERNS-1E]], PDF 140–149 | local ACID boundary, saga và compensation | §8 | Đã dùng để chặn suy luận atomicity xuyên service |
| [[SRC-POSTGRESQL-TRANSACTIONS]], truy cập 2026-09-28 | semantics hiện hành của transaction block | §6 | Đã đối chiếu tài liệu chính thức |
| [[SRC-SQLALCHEMY-SESSION-BASICS]], truy cập 2026-09-28 | implementation Unit of Work, flush, transaction và pool | §§5, 7, 9 | Đã tách implementation khỏi pattern |
| [[SRC-FOWLER-UNIT-OF-WORK]], truy cập 2026-09-28 | định nghĩa pattern | §2 | Đã dùng đúng phạm vi định nghĩa |
| Tổng hợp DE-L103 | default boundary, fault matrix, pool capacity reasoning và evidence pack | §§4, 9, 12–17 | Đã gắn `synthesis` hoặc `inference`; threshold để lab đo |

Phạm vi đọc bao phủ toàn bộ objective L103: boundary ownership, rollback khi lỗi giữa chừng, external side effect, pool exhaustion và N+1 detection. Isolation algorithm, outbox implementation và distributed transaction được loại trừ có chủ đích vì thuộc bài sau.

## Key takeaways

- Chọn transaction boundary từ invariant của use case, không từ số repository hoặc API của ORM.
- Application service thường là owner phù hợp vì nó thấy toàn bộ trình tự; repository không tự commit.
- Flush chưa phải commit, và timeout không chứng minh transaction đã rollback.
- Local database rollback không đảo được external side effect; cần intent, idempotency hoặc reconciliation.
- Transaction giữ connection và có thể giữ lock; external wait trong boundary làm giảm capacity rõ rệt.
- Atomicity phải được chứng minh bằng fault injection và đọc lại từ transaction độc lập.
