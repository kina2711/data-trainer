# Phase 3: Software and Backend Engineering
# Module 7: Software Design and Delivery
# Lesson 92: Error design: expected failure against defect

## Mục tiêu bài học

**Năng lực cần chứng minh.** Phân loại lỗi theo hai trục và cài đặt cách xử lý đúng cho từng ô, chứng minh bằng thí nghiệm tiêm lỗi.

**Điều kiện hoàn thành.** Bảng mười lỗi phân loại đủ hai trục, và bốn lỗi tiêm đều đi đúng đường với khiếm khuyết không bị nuốt.

> [!abstract] Câu hỏi trung tâm
> Khi pipeline hỏng, quyết định “thử lại, cách ly hay dừng” không thể lấy từ tên exception. Cần biết lỗi có thuộc contract hay là khiếm khuyết, có thể biến mất khi thử lại hay không, side effect đã xảy ra tới đâu và caller còn thời gian phục hồi hay không.

## Hai trục độc lập

### Trục A — expected failure hay defect?

- **Expected failure**: kết quả không thành công đã được contract dự liệu; caller có đường xử lý.
- **Defect**: vi phạm assumption, precondition, invariant hoặc bug trong code/configuration; tiếp tục có thể làm sai dữ liệu.

### Trục B — transient hay permanent?

- **Transient**: cùng operation có khả năng thành công sau một khoảng chờ hoặc thay đổi trạng thái ngoài.
- **Permanent với input hiện tại**: lặp lại cùng dữ liệu và điều kiện không làm kết quả đổi.

Hai trục không thay thế nhau. Một expected failure có thể transient hoặc permanent. Một defect có thể chỉ xuất hiện ngắt quãng do race condition nhưng vẫn là defect.

```mermaid
quadrantChart
  x-axis Permanent --> Transient
  y-axis Expected failure --> Defect
  quadrant-1 Defect ngắt quãng: dừng và điều tra
  quadrant-2 Defect ổn định: dừng và sửa
  quadrant-3 Dữ liệu xấu: cách ly hoặc từ chối
  quadrant-4 Phụ thuộc tạm lỗi: retry có giới hạn
```

> [!source-fact]
> Bloch đề xuất dùng checked exception cho điều kiện caller có thể phục hồi và runtime exception cho lỗi lập trình, đồng thời thừa nhận ranh giới đôi khi cần phán đoán. *Effective Java*, Item 70, PDF 317–318. Note giữ decision rule, không áp cơ chế checked exception sang mọi ngôn ngữ.

## Contract quyết định expectedness

“Dữ liệu không hợp lệ” chưa đủ để phân loại. Cùng một hiện tượng có thể khác nhau theo contract:

- API import cho phép dòng bị từ chối và trả rejection report: expected failure;
- cùng dòng lọt qua validator rồi làm domain invariant vỡ: defect ở boundary;
- schema mới đã được contract cho phép: không phải lỗi;
- field bắt buộc mất mà contract nói phải có: expected permanent failure của record hoặc batch.

Expectedness thuộc quan hệ caller–callee, không phải thuộc riêng exception class.

> [!source-fact]
> *The Pragmatic Programmer* tách user-input validation khỏi precondition violation: vi phạm contract giữa module là bug, còn dữ liệu ngoài cần được xử lý theo policy ở boundary. Topic 23, PDF 150–155.

## Transience là giả thuyết phải có cơ sở

Retry chỉ hợp lý khi:

1. failure có xác suất tự hết;
2. operation idempotent hoặc có idempotency key;
3. deadline còn đủ;
4. retry không làm hệ phụ thuộc quá tải hơn;
5. side effect của attempt trước đã biết hoặc được deduplicate;
6. có giới hạn attempt và backoff.

Timeout không tự động là transient an toàn. Nó thường tạo **unknown outcome**: caller không biết server đã commit hay chưa.

> [!source-fact]
> Titmus mô tả Retry cho transient fault nhưng ghi rõ thành công sau khi chờ chỉ là khả năng, không phải bảo đảm; implementation cần giới hạn attempt, delay và thường có backoff. *Cloud Native Go*, Chapter 4, PDF 106–108.

## Bảng mười lỗi của pipeline nạp dữ liệu

| # | Hiện tượng | Expected/defect | Transient/permanent | Hành vi mặc định | Bằng chứng cần giữ |
|---:|---|---|---|---|---|
| 1 | tệp chưa xuất hiện đúng giờ | expected | transient tới deadline | poll/backoff rồi fail batch | path, schedule, attempts |
| 2 | thiếu cột bắt buộc | expected | permanent với file | quarantine file | schema version, headers |
| 3 | một dòng sai ngày | expected | permanent với record | quarantine record | file, row, raw value |
| 4 | PostgreSQL connection reset trước query | expected | thường transient | retry có giới hạn | endpoint, attempt, latency |
| 5 | timeout sau `COMMIT` request | expected | outcome unknown | reconcile/idempotent retry | transaction/idempotency ID |
| 6 | unique violation do replay hợp lệ | expected nếu contract định nghĩa | permanent | treat-as-duplicate hoặc report | business key, existing row |
| 7 | unique violation ngoài business key | defect hoặc data-contract breach | permanent | stop partition/batch | constraint, values |
| 8 | `IndexError` trong mapping cố định | defect | permanent cho code path | crash/stop | stack, input locator |
| 9 | invariant `amount >= 0` vỡ sau validation | defect | permanent | crash/stop | normalized object, stack |
| 10 | worker hết bộ nhớ do batch không chặn | defect/capacity design | có thể lặp | stop, giảm batch sau điều tra | RSS, batch size, heap evidence |

Phân loại số 4, 5, 6 và 10 phụ thuộc contract và implementation thực. Bảng phải cho phép trạng thái `unknown` thay vì ép mọi lỗi vào ô chắc chắn.

## Decision table xử lý

| Expectedness | Persistence | Hành vi | Không được làm |
|---|---|---|---|
| expected | transient | retry/backoff trong budget; rồi trả failure rõ | retry vô hạn |
| expected | permanent | reject/quarantine; tiếp tục ở granularity được phép | retry cùng input |
| defect | stable | dừng nhanh, giữ bằng chứng, báo owner | catch rồi chạy tiếp |
| defect | intermittent | dừng hoặc cô lập process; điều tra race/state corruption | gọi đó là transient business failure |

“Tiếp tục” chỉ hợp lệ nếu unit of isolation được định nghĩa: một record, một partition hay cả batch.

## Crash early để bảo vệ dữ liệu

Khi invariant nội bộ vỡ, dừng tại điểm gần nguyên nhân nhất giúp:

- stack trace còn đúng context;
- tránh ghi dữ liệu phái sinh sai;
- không biến defect thành success metric;
- giới hạn blast radius.

> [!source-fact]
> Hunt và Thomas khuyến nghị crash early khi hệ đi vào trạng thái không thể xảy ra; chạy tiếp có thể ghi dữ liệu hỏng. Assertions dành cho điều “không bao giờ được xảy ra”, không thay real error handling. Topics 24–25, PDF 160–166.

Crash process không đồng nghĩa làm mất toàn bộ batch. Checkpoint và replay design phải cho phép khởi động lại từ boundary an toàn.

## Quarantine là một workflow, không phải thư mục rác

Quarantine record cần tối thiểu:

- immutable raw payload hoặc locator tới payload;
- source ID, file, partition, row/offset;
- error code ổn định và error version;
- observed value đã redact nếu nhạy cảm;
- ingestion run ID và timestamp;
- remediation owner và trạng thái;
- replay policy và số lần replay;
- checksum để chứng minh record không bị đổi âm thầm.

Không quarantine defect rồi coi batch thành công. Defect cần làm trạng thái run thất bại hoặc degraded theo policy công khai.

## Retry budget

Một policy có thể viết dưới dạng:

```text
deadline tổng: 30 s
attempt tối đa: 4
backoff: 0.5 s, 1 s, 2 s + jitter
per-attempt timeout: 5 s
retry-on: connection reset trước khi gửi; 429/503 có Retry-After
do-not-retry: validation error; permission denied; syntax error
unknown-outcome: reconcile bằng idempotency key trước attempt mới
```

Retry budget là một phần của error contract. Không đặt nó rải trong adapter và application với hai bộ giá trị khác nhau.

## Failure atomicity

Một operation thất bại nên để state ở trạng thái trước khi gọi, hoặc ở một trạng thái trung gian đã được contract mô tả và có thể phục hồi.

Cách đạt:

- validate trước khi mutate;
- tính phần có thể lỗi trước khi ghi;
- transaction trong một resource boundary;
- staging rồi atomic rename/swap;
- idempotency key và deduplication;
- compensation có giới hạn rõ khi không thể transaction.

> [!source-fact]
> Bloch gọi property “failed invocation để object ở state trước đó” là failure atomicity, và nêu validate trước mutation cùng ordering phần có thể lỗi trước phần mutate. *Effective Java*, Item 76, PDF 328–329.

## Dịch lỗi theo abstraction

Adapter database không để `psycopg.OperationalError` trở thành public application contract.

```python
try:
    repository.save(batch)
except DriverTimeout as cause:
    raise RepositoryOutcomeUnknown(run_id=run_id) from cause
except UniqueViolation as cause:
    raise DuplicateBusinessKey(keys=extract_keys(cause)) from cause
```

Translation giữ hai thứ:

- error type/codes mà caller hiểu;
- original cause và diagnostic metadata cho operator.

> [!source-fact]
> Bloch cảnh báo việc đẩy exception tầng thấp lên làm API lộ implementation detail. Exception translation kèm chaining giữ abstraction phù hợp mà vẫn bảo toàn cause. Item 73, PDF 323–324.

## Error context không dựa vào message text

Một error record hữu dụng có trường máy đọc được:

```text
error_code, category, retryability, outcome_certainty,
source_id, object_key, partition, row_number,
run_id, attempt, operation, timestamp, trace_id, cause_type
```

Không parse message string để điều khiển flow. Message có thể đổi theo phiên bản thư viện và locale.

## Outcome certainty là trục bổ sung

Hai trục của bài giúp quyết định phần lớn hành vi, nhưng distributed side effect cần thêm:

- `not_started`: an toàn thử lại;
- `committed`: không thử lại operation tạo side effect;
- `unknown`: reconcile trước;
- `partially_applied`: chạy repair/compensation theo evidence.

> [!inference]
> Outcome certainty không được ba nguồn trình bày thành cùng một taxonomy. Nó được thêm vì chỉ expected/transient chưa đủ để xử lý timeout sau write; đây là suy luận vận hành của chương trình.

## Error contract cho một port

| Error code | Ý nghĩa | Retry | Side effect | Caller action |
|---|---|---|---|---|
| `SOURCE_NOT_READY` | object chưa xuất hiện | có, tới deadline | không | backoff |
| `SOURCE_SCHEMA_INVALID` | schema không thỏa contract | không | không | quarantine source |
| `RECORD_REJECTED` | record sai domain rule | không | không | quarantine record |
| `REPOSITORY_UNAVAILABLE` | chưa gửi/không kết nối | có giới hạn | không | retry |
| `REPOSITORY_OUTCOME_UNKNOWN` | timeout quanh commit | không ngay | chưa biết | reconcile |
| `INVARIANT_BROKEN` | defect | không | có thể | stop và điều tra |

## Anti-pattern: `except Exception: log; continue`

Đoạn code này xóa phân biệt giữa expected failure và defect:

```python
try:
    process(row)
except Exception as exc:
    logger.warning("bad row: %s", exc)
    continue
```

Hệ quả:

- bug lập trình bị biến thành “dữ liệu xấu”;
- batch báo success thiếu dữ liệu;
- stack/cause có thể mất;
- retryable dependency failure bị bỏ qua;
- metric không phản ánh completeness.

## Ngộ nhận thường gặp

- “Exception được catch là expected”: catchability không nói gì về contract.
- “Timeout thì retry”: timeout có thể là unknown outcome.
- “Lỗi 5xx luôn transient”: misconfiguration hoặc deterministic bug cũng trả 5xx.
- “Một dòng xấu thì cả pipeline phải dừng”: tùy isolation contract và completeness requirement.
- “Quarantine nghĩa là đã xử lý”: record vẫn cần owner, remediation và replay.
- “Crash early làm hệ kém bền”: với invariant vỡ, chạy tiếp mới là rủi ro dữ liệu.

## Source coverage

| Source slice | Nội dung phải giữ | Vị trí trong note | Trạng thái |
|---|---|---|---|
| [[SRC-HUNT-THOMAS-PRAGMATIC-PROGRAMMER-20AE]], Topics 23–25 pp. 148–166 | contract violation, crash early, assertions và exception handling | §§1–3, 6, 9–11, 16 | Đã trình bày ranh giới expected failure/defect và context preservation |
| [[SRC-BLOCH-EFFECTIVE-JAVA-3E]], Items 70–76 pp. 317–329 | checked/unchecked choice, exception translation, chaining và failure atomicity | §§6, 9–11, 13 | Đã trình bày theo abstraction boundary; không biến Java taxonomy thành luật mọi ngôn ngữ |
| [[SRC-TITMUS-CLOUD-NATIVE-GO-1E]], Ch. 4 pp. 99–108 | transient fault, retry, backoff và circuit-breaker context | §§3, 5, 8, 12 | Đã trình bày retry budget và outcome uncertainty |
| Tổng hợp bài DE-L092 | ma trận hai trục, bảng 10 lỗi, quarantine workflow và bốn fault injection | §§4–5, 7, 14–17 | Đã trình bày như synthesis phục vụ pipeline data |

Phân loại transient là giả thuyết theo operation và context. Note không cho phép gắn nhãn cố định chỉ từ tên exception.

## Key takeaways

- Expected failure thuộc contract; defect là vi phạm assumption hoặc bug cần lộ ra.
- Transient/permanent là trục riêng và phải xét cùng deadline, idempotency, side effect.
- Retry không an toàn khi outcome chưa biết; reconcile đứng trước attempt mới.
- Permanent data failure đi vào quarantine có lineage, không đi vào retry loop.
- Lỗi tầng thấp được dịch sang vocabulary tầng trên nhưng giữ cause để điều tra.
- Bằng chứng tốt kiểm cả đường đi của lỗi và state còn lại sau lỗi.

## Giới hạn

- Checked/unchecked của Java chỉ được dùng làm nguồn cho decision rule, không phải API design chung.
- Bảng mười lỗi là mô hình cho pipeline order; owner phải điều chỉnh theo source và SLA thực.
- Chưa chạy fault injection trên code Bài 32.
- Không có ngưỡng retry/backoff phổ quát; con số trong ví dụ là cấu hình giảng dạy.
- Quarantine retention, privacy và access policy cần yêu cầu tổ chức riêng.

## Reference

1. [[SRC-HUNT-THOMAS-PRAGMATIC-PROGRAMMER-20AE]] — David Thomas và Andrew Hunt, *The Pragmatic Programmer*, Topics 23–25, PDF 148–166.
2. [[SRC-BLOCH-EFFECTIVE-JAVA-3E]] — Joshua Bloch, *Effective Java*, Third Edition, Chapter 10, Items 70–76, PDF 317–329.
3. [[SRC-TITMUS-CLOUD-NATIVE-GO-1E]] — Matthew A. Titmus, *Cloud Native Go*, Chapter 4, Circuit Breaker và Retry, PDF 99–108.
