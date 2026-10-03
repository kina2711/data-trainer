# Phase 1: Engineering Foundation
# Module 2: Python for Production
# Lesson 30: A resilient worker - retry, backoff, idempotency and shutdown

## Mục tiêu bài học

**Năng lực cần chứng minh.** Viết một tiến trình xử lý đạt bốn tính chất và chứng minh bằng thí nghiệm giết tiến trình rằng không mất và không trùng việc.

**Điều kiện hoàn thành.** Sau 20 lần giết và khởi động lại, đối soát khớp tuyệt đối; lỗi dữ liệu không bị thử lại; và tắt có kiểm soát xong trong hạn.


# A resilient worker - retry, backoff, idempotency and shutdown

**Tóm tắt bản chất:** worker claim item, check identity, execute side effect, persist outcome/checkpoint, ack; retry dùng classification/backoff/jitter Sai boundary ở `worker bền vững với retry budget, idempotency và graceful shutdown` làm kết quả có vẻ đúng trong happy path nhưng không chịu được failure hoặc changed constraint.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, kiểm chứng và áp dụng worker bền vững với retry budget, idempotency và graceful shutdown?

## Nỗi Đau & Động Lực

worker claim item, check identity, execute side effect, persist outcome/checkpoint, ack; retry dùng classification/backoff/jitter Với `wiki.de-foundation.resilient-worker-retry-backoff-idempotency-shutdown`, điểm phải khóa là state transition và invariant; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Không có mô hình này, lỗi thường lộ ở consumer sau cùng: output sai, latency vọt, resource không được giải phóng hoặc lịch sử không còn tái hiện được. Chi phí thật của `A resilient worker - retry, backoff, idempotency and shutdown` vì thế nằm ở thời gian chẩn đoán và phạm vi phục hồi, không nằm ở số dòng syntax.

## Cơ Chế Tác Động

exactly-once không tự có qua network; idempotency key scope/payload phải rõ; shutdown deadline giới hạn cleanup Với `wiki.de-foundation.resilient-worker-retry-backoff-idempotency-shutdown`, điểm phải khóa là identity, ownership và boundary; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hãy tách declared state, executed state và published state của `worker bền vững với retry budget, idempotency và graceful shutdown`. Một command thành công chỉ là executed signal; muốn kết luận cần đối soát consumer-visible invariant và trạng thái còn lại sau restart hoặc replay.

## Bản Đồ Quyết Định

ack trước persist làm mất work; retry permanent error; duplicate key với payload khác bị coi là replay Với `wiki.de-foundation.resilient-worker-retry-backoff-idempotency-shutdown`, điểm phải khóa là failure path và recovery; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Quy tắc mặc định cho `A resilient worker - retry, backoff, idempotency and shutdown` là chọn phương án đơn giản nhất qua được hard constraints, rồi ghi rõ điều kiện đảo. Bảng quyết định tối thiểu gồm workload, identity, state owner, time/memory budget, failure domain và khả năng rollback.

## Case Study Thực Chiến: A resilient worker - retry, backoff, idempotency and shutdown

state machine và durable ledger trước loop; bound retries/queue; poison item quarantine Với `wiki.de-foundation.resilient-worker-retry-backoff-idempotency-shutdown`, điểm phải khóa là decision trade-off và reversal trigger; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Case dùng fixture nhỏ nhưng phải giữ cơ chế chi phối. Trước khi chạy, learner viết expected transition; sau khi chạy, họ đối chiếu raw artifact với oracle và giải thích mọi khác biệt thay vì sửa expected cho khớp output.

## Góc Khuất & Ngộ Nhận

input identity, attempts, transitions, external side effects, checkpoints và shutdown reconciliation Với `wiki.de-foundation.resilient-worker-retry-backoff-idempotency-shutdown`, điểm phải khóa là evidence package và oracle; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

**Hiểu lầm:** Happy path chạy nhanh nghĩa là thiết kế đúng. **Thực tế:** ack trước persist làm mất work; retry permanent error; duplicate key với payload khác bị coi là replay **Vì sao nghe hợp lý:** case nhỏ thường không chạm capacity, concurrency, failure hoặc version boundary.

**Hiểu lầm:** Tool hoặc API tự bảo đảm semantics. **Thực tế:** guarantee chỉ tồn tại trong scope và state đã công bố. **Vì sao nghe hợp lý:** syntax che mất protocol phía dưới.

## Nếu Bạn Dạy Lại Điều Này...

kill ở mỗi transition và replay same/different payload Với `wiki.de-foundation.resilient-worker-retry-backoff-idempotency-shutdown`, điểm phải khóa là changed-constraint transfer; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hook dạy lại bắt đầu bằng một dự đoán dễ sai về `worker bền vững với retry budget, idempotency và graceful shutdown`. Bài tập seed đổi đúng một constraint, yêu cầu learner giữ hoặc đảo quyết định và chỉ ra evidence nào đủ mạnh để thuyết phục một reviewer không tham dự buổi học.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `A resilient worker - retry, backoff, idempotency and shutdown` là: input identity, attempts, transitions, external side effects, checkpoints và shutdown reconciliation Mỗi probe nối input boundary với failure signal và oracle có thể bác bỏ kết luận.

### Probe 1: state transition và invariant

**Mệnh đề cần kiểm.** worker claim item, check identity, execute side effect, persist outcome/checkpoint, ack; retry dùng classification/backoff/jitter

**Thiết kế phép thử.** Với `wiki.de-foundation.resilient-worker-retry-backoff-idempotency-shutdown`, tạo positive và negative control chỉ khác một điều kiện; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề cần kiểm.** exactly-once không tự có qua network; idempotency key scope/payload phải rõ; shutdown deadline giới hạn cleanup

**Thiết kế phép thử.** Với `wiki.de-foundation.resilient-worker-retry-backoff-idempotency-shutdown`, tạo boundary case ngay trước và sau ngưỡng; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề cần kiểm.** ack trước persist làm mất work; retry permanent error; duplicate key với payload khác bị coi là replay

**Thiết kế phép thử.** Với `wiki.de-foundation.resilient-worker-retry-backoff-idempotency-shutdown`, tạo replay cùng identity với state khác; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** state machine và durable ledger trước loop; bound retries/queue; poison item quarantine

**Thiết kế phép thử.** Với `wiki.de-foundation.resilient-worker-retry-backoff-idempotency-shutdown`, tạo failure inject trước và sau durable transition; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề cần kiểm.** input identity, attempts, transitions, external side effects, checkpoints và shutdown reconciliation

**Thiết kế phép thử.** Với `wiki.de-foundation.resilient-worker-retry-backoff-idempotency-shutdown`, tạo changed scale làm cost model đổi; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề cần kiểm.** kill ở mỗi transition và replay same/different payload

**Thiết kế phép thử.** Với `wiki.de-foundation.resilient-worker-retry-backoff-idempotency-shutdown`, tạo adversarial order hoặc skew; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề cần kiểm.** worker claim item, check identity, execute side effect, persist outcome/checkpoint, ack; retry dùng classification/backoff/jitter

**Thiết kế phép thử.** Với `wiki.de-foundation.resilient-worker-retry-backoff-idempotency-shutdown`, tạo fresh environment không cache; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề cần kiểm.** exactly-once không tự có qua network; idempotency key scope/payload phải rõ; shutdown deadline giới hạn cleanup

**Thiết kế phép thử.** Với `wiki.de-foundation.resilient-worker-retry-backoff-idempotency-shutdown`, tạo independent oracle không dùng chung implementation; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề cần kiểm.** ack trước persist làm mất work; retry permanent error; duplicate key với payload khác bị coi là replay

**Thiết kế phép thử.** Với `wiki.de-foundation.resilient-worker-retry-backoff-idempotency-shutdown`, tạo partial progress rồi restart; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** state machine và durable ledger trước loop; bound retries/queue; poison item quarantine

**Thiết kế phép thử.** Với `wiki.de-foundation.resilient-worker-retry-backoff-idempotency-shutdown`, tạo missing evidence phải abstain; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề cần kiểm.** input identity, attempts, transitions, external side effects, checkpoints và shutdown reconciliation

**Thiết kế phép thử.** Với `wiki.de-foundation.resilient-worker-retry-backoff-idempotency-shutdown`, tạo reviewer tái hiện từ package; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề cần kiểm.** kill ở mỗi transition và replay same/different payload

**Thiết kế phép thử.** Với `wiki.de-foundation.resilient-worker-retry-backoff-idempotency-shutdown`, tạo constraint đổi đủ để quyết định đảo; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên của `worker bền vững với retry budget, idempotency và graceful shutdown` nằm ở đâu?

<details><summary>Đáp án</summary>exactly-once không tự có qua network; idempotency key scope/payload phải rõ; shutdown deadline giới hạn cleanup</details>

2. Failure nào dễ tạo kết quả xanh giả nhất?

<details><summary>Đáp án</summary>ack trước persist làm mất work; retry permanent error; duplicate key với payload khác bị coi là replay</details>

3. Constraint nào khiến quyết định phải đảo?

<details><summary>Đáp án</summary>kill ở mỗi transition và replay same/different payload</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `A resilient worker - retry, backoff, idempotency and shutdown` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Mọi kết luận phụ thuộc version, workload, operating system, interpreter/compiler hoặc hardware phải được kiểm lại trên target.
- Concept key `ck.de.resilient-worker-retry-backoff-idempotency-shutdown` đang ở trạng thái `proposed`; note không được tính là canonical registry coverage trước khi owner đăng ký key.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-PYTHON-314-STDLIB-RUNTIME]]
2. [[SRC-HUNT-THOMAS-PRAGMATIC-PROGRAMMER-20AE]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-PYTHON-314-STDLIB-RUNTIME]] — `src.docs.python-3.14-stdlib-runtime` | Python 3.14.8 Library Reference; accessed 2026-10-02 | cơ chế và boundary liên quan trực tiếp tới `worker bền vững với retry budget, idempotency và graceful shutdown` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L030 |
| [[SRC-HUNT-THOMAS-PRAGMATIC-PROGRAMMER-20AE]] — `src.book.hunt-thomas-pragmatic-programmer.20ae` | Topic 10 PDF 76–83; Topics 23–25 PDF 148–166; Topic 40 PDF 276–280 | cơ chế và boundary liên quan trực tiếp tới `worker bền vững với retry budget, idempotency và graceful shutdown` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L030 |

## Key takeaways
- state machine và durable ledger trước loop; bound retries/queue; poison item quarantine
- input identity, attempts, transitions, external side effects, checkpoints và shutdown reconciliation
- `worker bền vững với retry budget, idempotency và graceful shutdown` chỉ có nghĩa trong scope, identity, state và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.
