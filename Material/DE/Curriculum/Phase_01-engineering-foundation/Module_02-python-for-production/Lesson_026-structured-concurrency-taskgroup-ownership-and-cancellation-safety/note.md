# Phase 1: Engineering Foundation
# Module 2: Python for Production
# Lesson 26: Structured concurrency - TaskGroup, ownership and cancellation safety

## Mục tiêu bài học

**Năng lực cần chứng minh.** Dựng phạm vi đồng thời có cấu trúc đạt bốn bảo đảm và chứng minh không còn tác vụ mồ côi khi tắt.

**Điều kiện hoàn thành.** Số tác vụ còn sống và số kết nối rò đều bằng không ở cả ba kịch bản, và bản không có cấu trúc được định lượng số tác vụ mồ côi.


# Structured concurrency - TaskGroup, ownership and cancellation safety

**Tóm tắt bản chất:** child tasks sống trong lexical scope; group chờ tất cả, propagate failure và cancel siblings theo contract Sai boundary ở `TaskGroup và structured concurrency cho ownership/cancellation safety` làm kết quả có vẻ đúng trong happy path nhưng không chịu được failure hoặc changed constraint.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, kiểm chứng và áp dụng TaskGroup và structured concurrency cho ownership/cancellation safety?

## Nỗi Đau & Động Lực

child tasks sống trong lexical scope; group chờ tất cả, propagate failure và cancel siblings theo contract Với `wiki.de-foundation.structured-concurrency-taskgroup-ownership-cancellation`, điểm phải khóa là state transition và invariant; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Không có mô hình này, lỗi thường lộ ở consumer sau cùng: output sai, latency vọt, resource không được giải phóng hoặc lịch sử không còn tái hiện được. Chi phí thật của `Structured concurrency - TaskGroup, ownership and cancellation safety` vì thế nằm ở thời gian chẩn đoán và phạm vi phục hồi, không nằm ở số dòng syntax.

## Cơ Chế Tác Động

structured scope không tự làm side effect atomic; exception groups cần phân loại; cleanup vẫn phải idempotent Với `wiki.de-foundation.structured-concurrency-taskgroup-ownership-cancellation`, điểm phải khóa là identity, ownership và boundary; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hãy tách declared state, executed state và published state của `TaskGroup và structured concurrency cho ownership/cancellation safety`. Một command thành công chỉ là executed signal; muốn kết luận cần đối soát consumer-visible invariant và trạng thái còn lại sau restart hoặc replay.

## Bản Đồ Quyết Định

child giữ resource ngoài scope; sibling cancellation che partial commit; catch rộng làm group báo success Với `wiki.de-foundation.structured-concurrency-taskgroup-ownership-cancellation`, điểm phải khóa là failure path và recovery; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Quy tắc mặc định cho `Structured concurrency - TaskGroup, ownership and cancellation safety` là chọn phương án đơn giản nhất qua được hard constraints, rồi ghi rõ điều kiện đảo. Bảng quyết định tối thiểu gồm workload, identity, state owner, time/memory budget, failure domain và khả năng rollback.

## Case Study Thực Chiến: Structured concurrency - TaskGroup, ownership and cancellation safety

dùng group khi children cùng một operation/failure fate; tách detached service có explicit supervisor Với `wiki.de-foundation.structured-concurrency-taskgroup-ownership-cancellation`, điểm phải khóa là decision trade-off và reversal trigger; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Case dùng fixture nhỏ nhưng phải giữ cơ chế chi phối. Trước khi chạy, learner viết expected transition; sau khi chạy, họ đối chiếu raw artifact với oracle và giải thích mọi khác biệt thay vì sửa expected cho khớp output.

## Góc Khuất & Ngộ Nhận

child census, start/finish/cancel timestamps, resource ledger và ExceptionGroup mapping Với `wiki.de-foundation.structured-concurrency-taskgroup-ownership-cancellation`, điểm phải khóa là evidence package và oracle; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

**Hiểu lầm:** Happy path chạy nhanh nghĩa là thiết kế đúng. **Thực tế:** child giữ resource ngoài scope; sibling cancellation che partial commit; catch rộng làm group báo success **Vì sao nghe hợp lý:** case nhỏ thường không chạm capacity, concurrency, failure hoặc version boundary.

**Hiểu lầm:** Tool hoặc API tự bảo đảm semantics. **Thực tế:** guarantee chỉ tồn tại trong scope và state đã công bố. **Vì sao nghe hợp lý:** syntax che mất protocol phía dưới.

## Nếu Bạn Dạy Lại Điều Này...

một child fail giữa ba child, một child cleanup fail để kiểm propagation Với `wiki.de-foundation.structured-concurrency-taskgroup-ownership-cancellation`, điểm phải khóa là changed-constraint transfer; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hook dạy lại bắt đầu bằng một dự đoán dễ sai về `TaskGroup và structured concurrency cho ownership/cancellation safety`. Bài tập seed đổi đúng một constraint, yêu cầu learner giữ hoặc đảo quyết định và chỉ ra evidence nào đủ mạnh để thuyết phục một reviewer không tham dự buổi học.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `Structured concurrency - TaskGroup, ownership and cancellation safety` là: child census, start/finish/cancel timestamps, resource ledger và ExceptionGroup mapping Mỗi probe nối input boundary với failure signal và oracle có thể bác bỏ kết luận.

### Probe 1: state transition và invariant

**Mệnh đề cần kiểm.** child tasks sống trong lexical scope; group chờ tất cả, propagate failure và cancel siblings theo contract

**Thiết kế phép thử.** Với `wiki.de-foundation.structured-concurrency-taskgroup-ownership-cancellation`, tạo positive và negative control chỉ khác một điều kiện; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề cần kiểm.** structured scope không tự làm side effect atomic; exception groups cần phân loại; cleanup vẫn phải idempotent

**Thiết kế phép thử.** Với `wiki.de-foundation.structured-concurrency-taskgroup-ownership-cancellation`, tạo boundary case ngay trước và sau ngưỡng; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề cần kiểm.** child giữ resource ngoài scope; sibling cancellation che partial commit; catch rộng làm group báo success

**Thiết kế phép thử.** Với `wiki.de-foundation.structured-concurrency-taskgroup-ownership-cancellation`, tạo replay cùng identity với state khác; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** dùng group khi children cùng một operation/failure fate; tách detached service có explicit supervisor

**Thiết kế phép thử.** Với `wiki.de-foundation.structured-concurrency-taskgroup-ownership-cancellation`, tạo failure inject trước và sau durable transition; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề cần kiểm.** child census, start/finish/cancel timestamps, resource ledger và ExceptionGroup mapping

**Thiết kế phép thử.** Với `wiki.de-foundation.structured-concurrency-taskgroup-ownership-cancellation`, tạo changed scale làm cost model đổi; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề cần kiểm.** một child fail giữa ba child, một child cleanup fail để kiểm propagation

**Thiết kế phép thử.** Với `wiki.de-foundation.structured-concurrency-taskgroup-ownership-cancellation`, tạo adversarial order hoặc skew; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề cần kiểm.** child tasks sống trong lexical scope; group chờ tất cả, propagate failure và cancel siblings theo contract

**Thiết kế phép thử.** Với `wiki.de-foundation.structured-concurrency-taskgroup-ownership-cancellation`, tạo fresh environment không cache; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề cần kiểm.** structured scope không tự làm side effect atomic; exception groups cần phân loại; cleanup vẫn phải idempotent

**Thiết kế phép thử.** Với `wiki.de-foundation.structured-concurrency-taskgroup-ownership-cancellation`, tạo independent oracle không dùng chung implementation; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề cần kiểm.** child giữ resource ngoài scope; sibling cancellation che partial commit; catch rộng làm group báo success

**Thiết kế phép thử.** Với `wiki.de-foundation.structured-concurrency-taskgroup-ownership-cancellation`, tạo partial progress rồi restart; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** dùng group khi children cùng một operation/failure fate; tách detached service có explicit supervisor

**Thiết kế phép thử.** Với `wiki.de-foundation.structured-concurrency-taskgroup-ownership-cancellation`, tạo missing evidence phải abstain; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề cần kiểm.** child census, start/finish/cancel timestamps, resource ledger và ExceptionGroup mapping

**Thiết kế phép thử.** Với `wiki.de-foundation.structured-concurrency-taskgroup-ownership-cancellation`, tạo reviewer tái hiện từ package; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề cần kiểm.** một child fail giữa ba child, một child cleanup fail để kiểm propagation

**Thiết kế phép thử.** Với `wiki.de-foundation.structured-concurrency-taskgroup-ownership-cancellation`, tạo constraint đổi đủ để quyết định đảo; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên của `TaskGroup và structured concurrency cho ownership/cancellation safety` nằm ở đâu?

<details><summary>Đáp án</summary>structured scope không tự làm side effect atomic; exception groups cần phân loại; cleanup vẫn phải idempotent</details>

2. Failure nào dễ tạo kết quả xanh giả nhất?

<details><summary>Đáp án</summary>child giữ resource ngoài scope; sibling cancellation che partial commit; catch rộng làm group báo success</details>

3. Constraint nào khiến quyết định phải đảo?

<details><summary>Đáp án</summary>một child fail giữa ba child, một child cleanup fail để kiểm propagation</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `Structured concurrency - TaskGroup, ownership and cancellation safety` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Mọi kết luận phụ thuộc version, workload, operating system, interpreter/compiler hoặc hardware phải được kiểm lại trên target.
- Concept key `ck.de.structured-concurrency-taskgroup-ownership-cancellation` đang ở trạng thái `proposed`; note không được tính là canonical registry coverage trước khi owner đăng ký key.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-PYTHON-314-STDLIB-RUNTIME]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-PYTHON-314-STDLIB-RUNTIME]] — `src.docs.python-3.14-stdlib-runtime` | Python 3.14.8 Library Reference; accessed 2026-10-02 | cơ chế và boundary liên quan trực tiếp tới `TaskGroup và structured concurrency cho ownership/cancellation safety` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L026 |

## Key takeaways
- dùng group khi children cùng một operation/failure fate; tách detached service có explicit supervisor
- child census, start/finish/cancel timestamps, resource ledger và ExceptionGroup mapping
- `TaskGroup và structured concurrency cho ownership/cancellation safety` chỉ có nghĩa trong scope, identity, state và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.
