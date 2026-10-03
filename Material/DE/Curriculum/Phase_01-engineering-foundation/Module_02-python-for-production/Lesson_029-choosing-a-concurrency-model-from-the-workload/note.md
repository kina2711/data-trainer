# Phase 1: Engineering Foundation
# Module 2: Python for Production
# Lesson 29: Choosing a concurrency model from the workload

## Mục tiêu bài học

**Năng lực cần chứng minh.** Chọn mô hình đồng thời cho bốn khối lượng công việc cho trước, mỗi lần dẫn về một số đo đã tự đo.

**Điều kiện hoàn thành.** Chọn đúng ≥ 3/4 khối lượng công việc với số đo dẫn chứng, và nhận ra đúng trường hợp không nên đồng thời.


# Choosing a concurrency model from the workload

**Tóm tắt bản chất:** mô hình phù hợp phụ thuộc CPU/I-O wait, state sharing, cancellation, isolation và task granularity Sai boundary ở `chọn sequential, threads, processes hay async từ workload` làm kết quả có vẻ đúng trong happy path nhưng không chịu được failure hoặc changed constraint.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, kiểm chứng và áp dụng chọn sequential, threads, processes hay async từ workload?

## Nỗi Đau & Động Lực

mô hình phù hợp phụ thuộc CPU/I-O wait, state sharing, cancellation, isolation và task granularity Với `wiki.de-foundation.choosing-concurrency-model-workload`, điểm phải khóa là state transition và invariant; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Không có mô hình này, lỗi thường lộ ở consumer sau cùng: output sai, latency vọt, resource không được giải phóng hoặc lịch sử không còn tái hiện được. Chi phí thật của `Choosing a concurrency model from the workload` vì thế nằm ở thời gian chẩn đoán và phạm vi phục hồi, không nằm ở số dòng syntax.

## Cơ Chế Tác Động

benchmark phải cùng semantics; library constraints và team operability là hard boundary Với `wiki.de-foundation.choosing-concurrency-model-workload`, điểm phải khóa là identity, ownership và boundary; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hãy tách declared state, executed state và published state của `chọn sequential, threads, processes hay async từ workload`. Một command thành công chỉ là executed signal; muốn kết luận cần đối soát consumer-visible invariant và trạng thái còn lại sau restart hoặc replay.

## Bản Đồ Quyết Định

chọn async vì nhiều request nhưng gọi blocking; chọn process cho task nhỏ; threads với mutable global state Với `wiki.de-foundation.choosing-concurrency-model-workload`, điểm phải khóa là failure path và recovery; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Quy tắc mặc định cho `Choosing a concurrency model from the workload` là chọn phương án đơn giản nhất qua được hard constraints, rồi ghi rõ điều kiện đảo. Bảng quyết định tối thiểu gồm workload, identity, state owner, time/memory budget, failure domain và khả năng rollback.

## Case Study Thực Chiến: Choosing a concurrency model from the workload

lập workload profile rồi chọn simplest model qua constraints; hybrid chỉ khi đo chứng minh Với `wiki.de-foundation.choosing-concurrency-model-workload`, điểm phải khóa là decision trade-off và reversal trigger; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Case dùng fixture nhỏ nhưng phải giữ cơ chế chi phối. Trước khi chạy, learner viết expected transition; sau khi chạy, họ đối chiếu raw artifact với oracle và giải thích mọi khác biệt thay vì sửa expected cho khớp output.

## Góc Khuất & Ngộ Nhận

throughput/latency distribution, CPU, memory, context switches, queue và failure recovery Với `wiki.de-foundation.choosing-concurrency-model-workload`, điểm phải khóa là evidence package và oracle; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

**Hiểu lầm:** Happy path chạy nhanh nghĩa là thiết kế đúng. **Thực tế:** chọn async vì nhiều request nhưng gọi blocking; chọn process cho task nhỏ; threads với mutable global state **Vì sao nghe hợp lý:** case nhỏ thường không chạm capacity, concurrency, failure hoặc version boundary.

**Hiểu lầm:** Tool hoặc API tự bảo đảm semantics. **Thực tế:** guarantee chỉ tồn tại trong scope và state đã công bố. **Vì sao nghe hợp lý:** syntax che mất protocol phía dưới.

## Nếu Bạn Dạy Lại Điều Này...

đổi task từ I/O-heavy sang CPU-heavy để bắt decision đảo Với `wiki.de-foundation.choosing-concurrency-model-workload`, điểm phải khóa là changed-constraint transfer; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hook dạy lại bắt đầu bằng một dự đoán dễ sai về `chọn sequential, threads, processes hay async từ workload`. Bài tập seed đổi đúng một constraint, yêu cầu learner giữ hoặc đảo quyết định và chỉ ra evidence nào đủ mạnh để thuyết phục một reviewer không tham dự buổi học.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `Choosing a concurrency model from the workload` là: throughput/latency distribution, CPU, memory, context switches, queue và failure recovery Mỗi probe nối input boundary với failure signal và oracle có thể bác bỏ kết luận.

### Probe 1: state transition và invariant

**Mệnh đề cần kiểm.** mô hình phù hợp phụ thuộc CPU/I-O wait, state sharing, cancellation, isolation và task granularity

**Thiết kế phép thử.** Với `wiki.de-foundation.choosing-concurrency-model-workload`, tạo positive và negative control chỉ khác một điều kiện; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề cần kiểm.** benchmark phải cùng semantics; library constraints và team operability là hard boundary

**Thiết kế phép thử.** Với `wiki.de-foundation.choosing-concurrency-model-workload`, tạo boundary case ngay trước và sau ngưỡng; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề cần kiểm.** chọn async vì nhiều request nhưng gọi blocking; chọn process cho task nhỏ; threads với mutable global state

**Thiết kế phép thử.** Với `wiki.de-foundation.choosing-concurrency-model-workload`, tạo replay cùng identity với state khác; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** lập workload profile rồi chọn simplest model qua constraints; hybrid chỉ khi đo chứng minh

**Thiết kế phép thử.** Với `wiki.de-foundation.choosing-concurrency-model-workload`, tạo failure inject trước và sau durable transition; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề cần kiểm.** throughput/latency distribution, CPU, memory, context switches, queue và failure recovery

**Thiết kế phép thử.** Với `wiki.de-foundation.choosing-concurrency-model-workload`, tạo changed scale làm cost model đổi; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề cần kiểm.** đổi task từ I/O-heavy sang CPU-heavy để bắt decision đảo

**Thiết kế phép thử.** Với `wiki.de-foundation.choosing-concurrency-model-workload`, tạo adversarial order hoặc skew; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề cần kiểm.** mô hình phù hợp phụ thuộc CPU/I-O wait, state sharing, cancellation, isolation và task granularity

**Thiết kế phép thử.** Với `wiki.de-foundation.choosing-concurrency-model-workload`, tạo fresh environment không cache; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề cần kiểm.** benchmark phải cùng semantics; library constraints và team operability là hard boundary

**Thiết kế phép thử.** Với `wiki.de-foundation.choosing-concurrency-model-workload`, tạo independent oracle không dùng chung implementation; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề cần kiểm.** chọn async vì nhiều request nhưng gọi blocking; chọn process cho task nhỏ; threads với mutable global state

**Thiết kế phép thử.** Với `wiki.de-foundation.choosing-concurrency-model-workload`, tạo partial progress rồi restart; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** lập workload profile rồi chọn simplest model qua constraints; hybrid chỉ khi đo chứng minh

**Thiết kế phép thử.** Với `wiki.de-foundation.choosing-concurrency-model-workload`, tạo missing evidence phải abstain; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề cần kiểm.** throughput/latency distribution, CPU, memory, context switches, queue và failure recovery

**Thiết kế phép thử.** Với `wiki.de-foundation.choosing-concurrency-model-workload`, tạo reviewer tái hiện từ package; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề cần kiểm.** đổi task từ I/O-heavy sang CPU-heavy để bắt decision đảo

**Thiết kế phép thử.** Với `wiki.de-foundation.choosing-concurrency-model-workload`, tạo constraint đổi đủ để quyết định đảo; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên của `chọn sequential, threads, processes hay async từ workload` nằm ở đâu?

<details><summary>Đáp án</summary>benchmark phải cùng semantics; library constraints và team operability là hard boundary</details>

2. Failure nào dễ tạo kết quả xanh giả nhất?

<details><summary>Đáp án</summary>chọn async vì nhiều request nhưng gọi blocking; chọn process cho task nhỏ; threads với mutable global state</details>

3. Constraint nào khiến quyết định phải đảo?

<details><summary>Đáp án</summary>đổi task từ I/O-heavy sang CPU-heavy để bắt decision đảo</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `Choosing a concurrency model from the workload` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Mọi kết luận phụ thuộc version, workload, operating system, interpreter/compiler hoặc hardware phải được kiểm lại trên target.
- Concept key `ck.de.choosing-concurrency-model-workload` đang ở trạng thái `proposed`; note không được tính là canonical registry coverage trước khi owner đăng ký key.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-PYTHON-314-STDLIB-RUNTIME]]
2. [[SRC-TLPI-2010]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-PYTHON-314-STDLIB-RUNTIME]] — `src.docs.python-3.14-stdlib-runtime` | Python 3.14.8 Library Reference; accessed 2026-10-02 | cơ chế và boundary liên quan trực tiếp tới `chọn sequential, threads, processes hay async từ workload` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L029 |
| [[SRC-TLPI-2010]] — `src.book.tlpi.2010` | process, thread, IPC và lifecycle scopes trong source record | cơ chế và boundary liên quan trực tiếp tới `chọn sequential, threads, processes hay async từ workload` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L029 |

## Key takeaways
- lập workload profile rồi chọn simplest model qua constraints; hybrid chỉ khi đo chứng minh
- throughput/latency distribution, CPU, memory, context switches, queue và failure recovery
- `chọn sequential, threads, processes hay async từ workload` chỉ có nghĩa trong scope, identity, state và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.
