# Phase 1: Engineering Foundation
# Module 2: Python for Production
# Lesson 25: Coroutine, task and future - the state model

## Mục tiêu bài học

**Năng lực cần chứng minh.** Truy được trạng thái của một tác vụ qua đủ năm giai đoạn và chỉ ra hai cách một lỗi bị nuốt.

**Điều kiện hoàn thành.** Năm trạng thái được quan sát bằng công cụ, và hai ca lỗi bị nuốt được tái hiện cùng chỉ ra cách phát hiện.


# Coroutine, task and future - the state model

**Tóm tắt bản chất:** coroutine object mô tả computation chưa schedule; Task schedule coroutine; Future đại diện eventual result do producer hoàn tất Sai boundary ở `coroutine, Task và Future như ba state/ownership model` làm kết quả có vẻ đúng trong happy path nhưng không chịu được failure hoặc changed constraint.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, kiểm chứng và áp dụng coroutine, Task và Future như ba state/ownership model?

## Nỗi Đau & Động Lực

coroutine object mô tả computation chưa schedule; Task schedule coroutine; Future đại diện eventual result do producer hoàn tất Với `wiki.de-foundation.coroutine-task-future-state-model`, điểm phải khóa là state transition và invariant; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Không có mô hình này, lỗi thường lộ ở consumer sau cùng: output sai, latency vọt, resource không được giải phóng hoặc lịch sử không còn tái hiện được. Chi phí thật của `Coroutine, task and future - the state model` vì thế nằm ở thời gian chẩn đoán và phạm vi phục hồi, không nằm ở số dòng syntax.

## Cơ Chế Tác Động

creating coroutine không chạy nó; task giữ reference/lifecycle; Future thường là integration primitive không phải app API Với `wiki.de-foundation.coroutine-task-future-state-model`, điểm phải khóa là identity, ownership và boundary; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hãy tách declared state, executed state và published state của `coroutine, Task và Future như ba state/ownership model`. Một command thành công chỉ là executed signal; muốn kết luận cần đối soát consumer-visible invariant và trạng thái còn lại sau restart hoặc replay.

## Bản Đồ Quyết Định

forgotten await tạo warning/mất work; fire-and-forget task bị GC hoặc exception không observed Với `wiki.de-foundation.coroutine-task-future-state-model`, điểm phải khóa là failure path và recovery; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Quy tắc mặc định cho `Coroutine, task and future - the state model` là chọn phương án đơn giản nhất qua được hard constraints, rồi ghi rõ điều kiện đảo. Bảng quyết định tối thiểu gồm workload, identity, state owner, time/memory budget, failure domain và khả năng rollback.

## Case Study Thực Chiến: Coroutine, task and future - the state model

caller phải biết ai schedule, await, cancel và collect exception; prefer structured owner Với `wiki.de-foundation.coroutine-task-future-state-model`, điểm phải khóa là decision trade-off và reversal trigger; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Case dùng fixture nhỏ nhưng phải giữ cơ chế chi phối. Trước khi chạy, learner viết expected transition; sau khi chạy, họ đối chiếu raw artifact với oracle và giải thích mọi khác biệt thay vì sửa expected cho khớp output.

## Góc Khuất & Ngộ Nhận

task states, owner registry, exception retrieval và completion/cancellation timeline Với `wiki.de-foundation.coroutine-task-future-state-model`, điểm phải khóa là evidence package và oracle; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

**Hiểu lầm:** Happy path chạy nhanh nghĩa là thiết kế đúng. **Thực tế:** forgotten await tạo warning/mất work; fire-and-forget task bị GC hoặc exception không observed **Vì sao nghe hợp lý:** case nhỏ thường không chạm capacity, concurrency, failure hoặc version boundary.

**Hiểu lầm:** Tool hoặc API tự bảo đảm semantics. **Thực tế:** guarantee chỉ tồn tại trong scope và state đã công bố. **Vì sao nghe hợp lý:** syntax che mất protocol phía dưới.

## Nếu Bạn Dạy Lại Điều Này...

tạo ba computations rồi bỏ owner của một task để quan sát orphan behavior Với `wiki.de-foundation.coroutine-task-future-state-model`, điểm phải khóa là changed-constraint transfer; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hook dạy lại bắt đầu bằng một dự đoán dễ sai về `coroutine, Task và Future như ba state/ownership model`. Bài tập seed đổi đúng một constraint, yêu cầu learner giữ hoặc đảo quyết định và chỉ ra evidence nào đủ mạnh để thuyết phục một reviewer không tham dự buổi học.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `Coroutine, task and future - the state model` là: task states, owner registry, exception retrieval và completion/cancellation timeline Mỗi probe nối input boundary với failure signal và oracle có thể bác bỏ kết luận.

### Probe 1: state transition và invariant

**Mệnh đề cần kiểm.** coroutine object mô tả computation chưa schedule; Task schedule coroutine; Future đại diện eventual result do producer hoàn tất

**Thiết kế phép thử.** Với `wiki.de-foundation.coroutine-task-future-state-model`, tạo positive và negative control chỉ khác một điều kiện; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề cần kiểm.** creating coroutine không chạy nó; task giữ reference/lifecycle; Future thường là integration primitive không phải app API

**Thiết kế phép thử.** Với `wiki.de-foundation.coroutine-task-future-state-model`, tạo boundary case ngay trước và sau ngưỡng; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề cần kiểm.** forgotten await tạo warning/mất work; fire-and-forget task bị GC hoặc exception không observed

**Thiết kế phép thử.** Với `wiki.de-foundation.coroutine-task-future-state-model`, tạo replay cùng identity với state khác; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** caller phải biết ai schedule, await, cancel và collect exception; prefer structured owner

**Thiết kế phép thử.** Với `wiki.de-foundation.coroutine-task-future-state-model`, tạo failure inject trước và sau durable transition; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề cần kiểm.** task states, owner registry, exception retrieval và completion/cancellation timeline

**Thiết kế phép thử.** Với `wiki.de-foundation.coroutine-task-future-state-model`, tạo changed scale làm cost model đổi; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề cần kiểm.** tạo ba computations rồi bỏ owner của một task để quan sát orphan behavior

**Thiết kế phép thử.** Với `wiki.de-foundation.coroutine-task-future-state-model`, tạo adversarial order hoặc skew; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề cần kiểm.** coroutine object mô tả computation chưa schedule; Task schedule coroutine; Future đại diện eventual result do producer hoàn tất

**Thiết kế phép thử.** Với `wiki.de-foundation.coroutine-task-future-state-model`, tạo fresh environment không cache; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề cần kiểm.** creating coroutine không chạy nó; task giữ reference/lifecycle; Future thường là integration primitive không phải app API

**Thiết kế phép thử.** Với `wiki.de-foundation.coroutine-task-future-state-model`, tạo independent oracle không dùng chung implementation; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề cần kiểm.** forgotten await tạo warning/mất work; fire-and-forget task bị GC hoặc exception không observed

**Thiết kế phép thử.** Với `wiki.de-foundation.coroutine-task-future-state-model`, tạo partial progress rồi restart; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** caller phải biết ai schedule, await, cancel và collect exception; prefer structured owner

**Thiết kế phép thử.** Với `wiki.de-foundation.coroutine-task-future-state-model`, tạo missing evidence phải abstain; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề cần kiểm.** task states, owner registry, exception retrieval và completion/cancellation timeline

**Thiết kế phép thử.** Với `wiki.de-foundation.coroutine-task-future-state-model`, tạo reviewer tái hiện từ package; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề cần kiểm.** tạo ba computations rồi bỏ owner của một task để quan sát orphan behavior

**Thiết kế phép thử.** Với `wiki.de-foundation.coroutine-task-future-state-model`, tạo constraint đổi đủ để quyết định đảo; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên của `coroutine, Task và Future như ba state/ownership model` nằm ở đâu?

<details><summary>Đáp án</summary>creating coroutine không chạy nó; task giữ reference/lifecycle; Future thường là integration primitive không phải app API</details>

2. Failure nào dễ tạo kết quả xanh giả nhất?

<details><summary>Đáp án</summary>forgotten await tạo warning/mất work; fire-and-forget task bị GC hoặc exception không observed</details>

3. Constraint nào khiến quyết định phải đảo?

<details><summary>Đáp án</summary>tạo ba computations rồi bỏ owner của một task để quan sát orphan behavior</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `Coroutine, task and future - the state model` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Mọi kết luận phụ thuộc version, workload, operating system, interpreter/compiler hoặc hardware phải được kiểm lại trên target.
- Concept key `ck.de.coroutine-task-future-state-model` đang ở trạng thái `proposed`; note không được tính là canonical registry coverage trước khi owner đăng ký key.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-PYTHON-314-LANGUAGE-REFERENCE]]
2. [[SRC-PYTHON-314-STDLIB-RUNTIME]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-PYTHON-314-LANGUAGE-REFERENCE]] — `src.docs.python-3.14-language-reference` | Python 3.14.8 Language Reference; accessed 2026-10-02 | cơ chế và boundary liên quan trực tiếp tới `coroutine, Task và Future như ba state/ownership model` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L025 |
| [[SRC-PYTHON-314-STDLIB-RUNTIME]] — `src.docs.python-3.14-stdlib-runtime` | Python 3.14.8 Library Reference; accessed 2026-10-02 | cơ chế và boundary liên quan trực tiếp tới `coroutine, Task và Future như ba state/ownership model` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L025 |

## Key takeaways
- caller phải biết ai schedule, await, cancel và collect exception; prefer structured owner
- task states, owner registry, exception retrieval và completion/cancellation timeline
- `coroutine, Task và Future như ba state/ownership model` chỉ có nghĩa trong scope, identity, state và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.
