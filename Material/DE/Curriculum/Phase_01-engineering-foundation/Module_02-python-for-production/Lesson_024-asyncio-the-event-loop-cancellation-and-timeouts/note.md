# Phase 1: Engineering Foundation
# Module 2: Python for Production
# Lesson 24: Asyncio - the event loop, cancellation and timeouts

## Mục tiêu bài học

**Năng lực cần chứng minh.** Viết một trình thu thập bất đồng bộ có giới hạn đồng thời, hết giờ và huỷ bỏ đúng, không có lời gọi chặn nào trong vòng lặp.

**Điều kiện hoàn thành.** Không lời gọi chặn nào trong vòng lặp, hết giờ kích hoạt đúng ngưỡng, và sau khi huỷ thì mọi kết nối đã đóng.


# Asyncio - the event loop, cancellation and timeouts

**Tóm tắt bản chất:** task chạy tới await rồi nhường loop; cancellation được inject tại suspension; timeout biến deadline thành cancellation context Sai boundary ở `asyncio event loop, cooperative scheduling, cancellation và timeout` làm kết quả có vẻ đúng trong happy path nhưng không chịu được failure hoặc changed constraint.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, kiểm chứng và áp dụng asyncio event loop, cooperative scheduling, cancellation và timeout?

## Nỗi Đau & Động Lực

task chạy tới await rồi nhường loop; cancellation được inject tại suspension; timeout biến deadline thành cancellation context Với `wiki.de-foundation.asyncio-event-loop-cancellation-timeouts`, điểm phải khóa là state transition và invariant; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Không có mô hình này, lỗi thường lộ ở consumer sau cùng: output sai, latency vọt, resource không được giải phóng hoặc lịch sử không còn tái hiện được. Chi phí thật của `Asyncio - the event loop, cancellation and timeouts` vì thế nằm ở thời gian chẩn đoán và phạm vi phục hồi, không nằm ở số dòng syntax.

## Cơ Chế Tác Động

blocking call chặn toàn loop; cancellation là control flow cần cleanup; timeout cục bộ không tự tạo end-to-end deadline Với `wiki.de-foundation.asyncio-event-loop-cancellation-timeouts`, điểm phải khóa là identity, ownership và boundary; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hãy tách declared state, executed state và published state của `asyncio event loop, cooperative scheduling, cancellation và timeout`. Một command thành công chỉ là executed signal; muốn kết luận cần đối soát consumer-visible invariant và trạng thái còn lại sau restart hoặc replay.

## Bản Đồ Quyết Định

swallow CancelledError làm shutdown treo; unbounded create_task tăng memory; timeout ngoài không dừng side effect ngoài Với `wiki.de-foundation.asyncio-event-loop-cancellation-timeouts`, điểm phải khóa là failure path và recovery; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Quy tắc mặc định cho `Asyncio - the event loop, cancellation and timeouts` là chọn phương án đơn giản nhất qua được hard constraints, rồi ghi rõ điều kiện đảo. Bảng quyết định tối thiểu gồm workload, identity, state owner, time/memory budget, failure domain và khả năng rollback.

## Case Study Thực Chiến: Asyncio - the event loop, cancellation and timeouts

dùng async cho nhiều I/O chờ; bọc blocking code; truyền deadline và giữ cancellation-safe cleanup Với `wiki.de-foundation.asyncio-event-loop-cancellation-timeouts`, điểm phải khóa là decision trade-off và reversal trigger; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Case dùng fixture nhỏ nhưng phải giữ cơ chế chi phối. Trước khi chạy, learner viết expected transition; sau khi chạy, họ đối chiếu raw artifact với oracle và giải thích mọi khác biệt thay vì sửa expected cho khớp output.

## Góc Khuất & Ngộ Nhận

loop lag, task census, deadline, cancellation latency và external side-effect ledger Với `wiki.de-foundation.asyncio-event-loop-cancellation-timeouts`, điểm phải khóa là evidence package và oracle; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

**Hiểu lầm:** Happy path chạy nhanh nghĩa là thiết kế đúng. **Thực tế:** swallow CancelledError làm shutdown treo; unbounded create_task tăng memory; timeout ngoài không dừng side effect ngoài **Vì sao nghe hợp lý:** case nhỏ thường không chạm capacity, concurrency, failure hoặc version boundary.

**Hiểu lầm:** Tool hoặc API tự bảo đảm semantics. **Thực tế:** guarantee chỉ tồn tại trong scope và state đã công bố. **Vì sao nghe hợp lý:** syntax che mất protocol phía dưới.

## Nếu Bạn Dạy Lại Điều Này...

cancel trước/sau durable write để kiểm state và retry contract Với `wiki.de-foundation.asyncio-event-loop-cancellation-timeouts`, điểm phải khóa là changed-constraint transfer; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hook dạy lại bắt đầu bằng một dự đoán dễ sai về `asyncio event loop, cooperative scheduling, cancellation và timeout`. Bài tập seed đổi đúng một constraint, yêu cầu learner giữ hoặc đảo quyết định và chỉ ra evidence nào đủ mạnh để thuyết phục một reviewer không tham dự buổi học.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `Asyncio - the event loop, cancellation and timeouts` là: loop lag, task census, deadline, cancellation latency và external side-effect ledger Mỗi probe nối input boundary với failure signal và oracle có thể bác bỏ kết luận.

### Probe 1: state transition và invariant

**Mệnh đề cần kiểm.** task chạy tới await rồi nhường loop; cancellation được inject tại suspension; timeout biến deadline thành cancellation context

**Thiết kế phép thử.** Với `wiki.de-foundation.asyncio-event-loop-cancellation-timeouts`, tạo positive và negative control chỉ khác một điều kiện; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề cần kiểm.** blocking call chặn toàn loop; cancellation là control flow cần cleanup; timeout cục bộ không tự tạo end-to-end deadline

**Thiết kế phép thử.** Với `wiki.de-foundation.asyncio-event-loop-cancellation-timeouts`, tạo boundary case ngay trước và sau ngưỡng; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề cần kiểm.** swallow CancelledError làm shutdown treo; unbounded create_task tăng memory; timeout ngoài không dừng side effect ngoài

**Thiết kế phép thử.** Với `wiki.de-foundation.asyncio-event-loop-cancellation-timeouts`, tạo replay cùng identity với state khác; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** dùng async cho nhiều I/O chờ; bọc blocking code; truyền deadline và giữ cancellation-safe cleanup

**Thiết kế phép thử.** Với `wiki.de-foundation.asyncio-event-loop-cancellation-timeouts`, tạo failure inject trước và sau durable transition; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề cần kiểm.** loop lag, task census, deadline, cancellation latency và external side-effect ledger

**Thiết kế phép thử.** Với `wiki.de-foundation.asyncio-event-loop-cancellation-timeouts`, tạo changed scale làm cost model đổi; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề cần kiểm.** cancel trước/sau durable write để kiểm state và retry contract

**Thiết kế phép thử.** Với `wiki.de-foundation.asyncio-event-loop-cancellation-timeouts`, tạo adversarial order hoặc skew; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề cần kiểm.** task chạy tới await rồi nhường loop; cancellation được inject tại suspension; timeout biến deadline thành cancellation context

**Thiết kế phép thử.** Với `wiki.de-foundation.asyncio-event-loop-cancellation-timeouts`, tạo fresh environment không cache; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề cần kiểm.** blocking call chặn toàn loop; cancellation là control flow cần cleanup; timeout cục bộ không tự tạo end-to-end deadline

**Thiết kế phép thử.** Với `wiki.de-foundation.asyncio-event-loop-cancellation-timeouts`, tạo independent oracle không dùng chung implementation; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề cần kiểm.** swallow CancelledError làm shutdown treo; unbounded create_task tăng memory; timeout ngoài không dừng side effect ngoài

**Thiết kế phép thử.** Với `wiki.de-foundation.asyncio-event-loop-cancellation-timeouts`, tạo partial progress rồi restart; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** dùng async cho nhiều I/O chờ; bọc blocking code; truyền deadline và giữ cancellation-safe cleanup

**Thiết kế phép thử.** Với `wiki.de-foundation.asyncio-event-loop-cancellation-timeouts`, tạo missing evidence phải abstain; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề cần kiểm.** loop lag, task census, deadline, cancellation latency và external side-effect ledger

**Thiết kế phép thử.** Với `wiki.de-foundation.asyncio-event-loop-cancellation-timeouts`, tạo reviewer tái hiện từ package; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề cần kiểm.** cancel trước/sau durable write để kiểm state và retry contract

**Thiết kế phép thử.** Với `wiki.de-foundation.asyncio-event-loop-cancellation-timeouts`, tạo constraint đổi đủ để quyết định đảo; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên của `asyncio event loop, cooperative scheduling, cancellation và timeout` nằm ở đâu?

<details><summary>Đáp án</summary>blocking call chặn toàn loop; cancellation là control flow cần cleanup; timeout cục bộ không tự tạo end-to-end deadline</details>

2. Failure nào dễ tạo kết quả xanh giả nhất?

<details><summary>Đáp án</summary>swallow CancelledError làm shutdown treo; unbounded create_task tăng memory; timeout ngoài không dừng side effect ngoài</details>

3. Constraint nào khiến quyết định phải đảo?

<details><summary>Đáp án</summary>cancel trước/sau durable write để kiểm state và retry contract</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `Asyncio - the event loop, cancellation and timeouts` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Mọi kết luận phụ thuộc version, workload, operating system, interpreter/compiler hoặc hardware phải được kiểm lại trên target.
- Concept key `ck.de.asyncio-event-loop-cancellation-timeouts` đang ở trạng thái `proposed`; note không được tính là canonical registry coverage trước khi owner đăng ký key.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-PYTHON-314-STDLIB-RUNTIME]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-PYTHON-314-STDLIB-RUNTIME]] — `src.docs.python-3.14-stdlib-runtime` | Python 3.14.8 Library Reference; accessed 2026-10-02 | cơ chế và boundary liên quan trực tiếp tới `asyncio event loop, cooperative scheduling, cancellation và timeout` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L024 |

## Key takeaways
- dùng async cho nhiều I/O chờ; bọc blocking code; truyền deadline và giữ cancellation-safe cleanup
- loop lag, task census, deadline, cancellation latency và external side-effect ledger
- `asyncio event loop, cooperative scheduling, cancellation và timeout` chỉ có nghĩa trong scope, identity, state và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.
