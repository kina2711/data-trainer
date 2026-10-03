---
note_id: wiki.de-foundation.processes-isolation-serialization-cost
concept_key: ck.de.processes-isolation-serialization-cost
concept_key_status: canonical
note_type: concept-deep-dive
status: canonical
approved_by: second-brain-owner
approved_at: 2026-10-03
approval_scope: all-registered-notes
canonical_since: 2026-10-03
language: vi
created: 2026-10-02
last_verified: 2026-10-02
review_after: 2027-04-02
editorial_pass: humanized-v3
primary_question: Làm thế nào mô hình, kiểm chứng và áp dụng process isolation, IPC/serialization và startup cost?
source_ids:
  - src.docs.python-3.14-stdlib-runtime
  - src.book.tlpi.2010
relationships:
  builds_on: [wiki.de-foundation.threads-shared-memory-races-locks]
  prerequisite_of: [wiki.de-foundation.asyncio-event-loop-cancellation-timeouts]
  related_to: []
aliases: [Processes - isolation, serialization and cost]
tags: [wiki/python, de-foundation, module-2]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/023-processes-isolation-serialization-cost.md
---

# Processes - isolation, serialization and cost

**Tóm tắt bản chất:** process có address space riêng; dữ liệu qua pickle/pipe/shared memory; worker lifecycle thêm startup và teardown Sai boundary ở `process isolation, IPC/serialization và startup cost` làm kết quả có vẻ đúng trong happy path nhưng không chịu được failure hoặc changed constraint.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, kiểm chứng và áp dụng process isolation, IPC/serialization và startup cost?

## Nỗi Đau & Động Lực

process có address space riêng; dữ liệu qua pickle/pipe/shared memory; worker lifecycle thêm startup và teardown Với `wiki.de-foundation.processes-isolation-serialization-cost`, điểm phải khóa là state transition và invariant; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Không có mô hình này, lỗi thường lộ ở consumer sau cùng: output sai, latency vọt, resource không được giải phóng hoặc lịch sử không còn tái hiện được. Chi phí thật của `Processes - isolation, serialization and cost` vì thế nằm ở thời gian chẩn đoán và phạm vi phục hồi, không nằm ở số dòng syntax.

## Cơ Chế Tác Động

fork/spawn semantics khác platform; copy-on-write không loại memory cost sau mutation; object phải serializable Với `wiki.de-foundation.processes-isolation-serialization-cost`, điểm phải khóa là identity, ownership và boundary; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hãy tách declared state, executed state và published state của `process isolation, IPC/serialization và startup cost`. Một command thành công chỉ là executed signal; muốn kết luận cần đối soát consumer-visible invariant và trạng thái còn lại sau restart hoặc replay.

## Bản Đồ Quyết Định

large payload copy lấn compute; child leak/zombie; fork state không an toàn từ parent multithreaded Với `wiki.de-foundation.processes-isolation-serialization-cost`, điểm phải khóa là failure path và recovery; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Quy tắc mặc định cho `Processes - isolation, serialization and cost` là chọn phương án đơn giản nhất qua được hard constraints, rồi ghi rõ điều kiện đảo. Bảng quyết định tối thiểu gồm workload, identity, state owner, time/memory budget, failure domain và khả năng rollback.

## Case Study Thực Chiến: Processes - isolation, serialization and cost

dùng process cho CPU-bound/isolation khi task đủ lớn; batch payload và bound pool Với `wiki.de-foundation.processes-isolation-serialization-cost`, điểm phải khóa là decision trade-off và reversal trigger; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Case dùng fixture nhỏ nhưng phải giữ cơ chế chi phối. Trước khi chạy, learner viết expected transition; sau khi chạy, họ đối chiếu raw artifact với oracle và giải thích mọi khác biệt thay vì sửa expected cho khớp output.

## Góc Khuất & Ngộ Nhận

CPU utilization, serialization bytes/time, RSS, startup, exit codes và orphan check Với `wiki.de-foundation.processes-isolation-serialization-cost`, điểm phải khóa là evidence package và oracle; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

**Hiểu lầm:** Happy path chạy nhanh nghĩa là thiết kế đúng. **Thực tế:** large payload copy lấn compute; child leak/zombie; fork state không an toàn từ parent multithreaded **Vì sao nghe hợp lý:** case nhỏ thường không chạm capacity, concurrency, failure hoặc version boundary.

**Hiểu lầm:** Tool hoặc API tự bảo đảm semantics. **Thực tế:** guarantee chỉ tồn tại trong scope và state đã công bố. **Vì sao nghe hợp lý:** syntax che mất protocol phía dưới.

## Nếu Bạn Dạy Lại Điều Này...

giảm task size tới điểm process pool chậm hơn sequential Với `wiki.de-foundation.processes-isolation-serialization-cost`, điểm phải khóa là changed-constraint transfer; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hook dạy lại bắt đầu bằng một dự đoán dễ sai về `process isolation, IPC/serialization và startup cost`. Bài tập seed đổi đúng một constraint, yêu cầu learner giữ hoặc đảo quyết định và chỉ ra evidence nào đủ mạnh để thuyết phục một reviewer không tham dự buổi học.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `Processes - isolation, serialization and cost` là: CPU utilization, serialization bytes/time, RSS, startup, exit codes và orphan check Mỗi probe nối input boundary với failure signal và oracle có thể bác bỏ kết luận.

### Probe 1: state transition và invariant

**Mệnh đề cần kiểm.** process có address space riêng; dữ liệu qua pickle/pipe/shared memory; worker lifecycle thêm startup và teardown

**Thiết kế phép thử cho `wiki.de-foundation.processes-isolation-serialization-cost`.** Với `wiki.de-foundation.processes-isolation-serialization-cost`, tạo positive và negative control chỉ khác một điều kiện; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề cần kiểm.** fork/spawn semantics khác platform; copy-on-write không loại memory cost sau mutation; object phải serializable

**Thiết kế phép thử cho `wiki.de-foundation.processes-isolation-serialization-cost`.** Với `wiki.de-foundation.processes-isolation-serialization-cost`, tạo boundary case ngay trước và sau ngưỡng; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề cần kiểm.** large payload copy lấn compute; child leak/zombie; fork state không an toàn từ parent multithreaded

**Thiết kế phép thử cho `wiki.de-foundation.processes-isolation-serialization-cost`.** Với `wiki.de-foundation.processes-isolation-serialization-cost`, tạo replay cùng identity với state khác; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** dùng process cho CPU-bound/isolation khi task đủ lớn; batch payload và bound pool

**Thiết kế phép thử cho `wiki.de-foundation.processes-isolation-serialization-cost`.** Với `wiki.de-foundation.processes-isolation-serialization-cost`, tạo failure inject trước và sau durable transition; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề cần kiểm.** CPU utilization, serialization bytes/time, RSS, startup, exit codes và orphan check

**Thiết kế phép thử cho `wiki.de-foundation.processes-isolation-serialization-cost`.** Với `wiki.de-foundation.processes-isolation-serialization-cost`, tạo changed scale làm cost model đổi; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề cần kiểm.** giảm task size tới điểm process pool chậm hơn sequential

**Thiết kế phép thử cho `wiki.de-foundation.processes-isolation-serialization-cost`.** Với `wiki.de-foundation.processes-isolation-serialization-cost`, tạo adversarial order hoặc skew; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề cần kiểm.** process có address space riêng; dữ liệu qua pickle/pipe/shared memory; worker lifecycle thêm startup và teardown

**Thiết kế phép thử cho `wiki.de-foundation.processes-isolation-serialization-cost`.** Với `wiki.de-foundation.processes-isolation-serialization-cost`, tạo fresh environment không cache; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề cần kiểm.** fork/spawn semantics khác platform; copy-on-write không loại memory cost sau mutation; object phải serializable

**Thiết kế phép thử cho `wiki.de-foundation.processes-isolation-serialization-cost`.** Với `wiki.de-foundation.processes-isolation-serialization-cost`, tạo independent oracle không dùng chung implementation; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề cần kiểm.** large payload copy lấn compute; child leak/zombie; fork state không an toàn từ parent multithreaded

**Thiết kế phép thử cho `wiki.de-foundation.processes-isolation-serialization-cost`.** Với `wiki.de-foundation.processes-isolation-serialization-cost`, tạo partial progress rồi restart; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** dùng process cho CPU-bound/isolation khi task đủ lớn; batch payload và bound pool

**Thiết kế phép thử cho `wiki.de-foundation.processes-isolation-serialization-cost`.** Với `wiki.de-foundation.processes-isolation-serialization-cost`, tạo missing evidence phải abstain; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề cần kiểm.** CPU utilization, serialization bytes/time, RSS, startup, exit codes và orphan check

**Thiết kế phép thử cho `wiki.de-foundation.processes-isolation-serialization-cost`.** Với `wiki.de-foundation.processes-isolation-serialization-cost`, tạo reviewer tái hiện từ package; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề cần kiểm.** giảm task size tới điểm process pool chậm hơn sequential

**Thiết kế phép thử cho `wiki.de-foundation.processes-isolation-serialization-cost`.** Với `wiki.de-foundation.processes-isolation-serialization-cost`, tạo constraint đổi đủ để quyết định đảo; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên của `process isolation, IPC/serialization và startup cost` nằm ở đâu?

<details><summary>Đáp án</summary>fork/spawn semantics khác platform; copy-on-write không loại memory cost sau mutation; object phải serializable</details>

2. Failure nào dễ tạo kết quả xanh giả nhất?

<details><summary>Đáp án</summary>large payload copy lấn compute; child leak/zombie; fork state không an toàn từ parent multithreaded</details>

3. Constraint nào khiến quyết định phải đảo?

<details><summary>Đáp án</summary>giảm task size tới điểm process pool chậm hơn sequential</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `Processes - isolation, serialization and cost` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Mọi kết luận phụ thuộc version, workload, operating system, interpreter/compiler hoặc hardware phải được kiểm lại trên target.
- Concept key `ck.de.processes-isolation-serialization-cost` đã được owner phê duyệt `canonical`; note thuộc canonical registry coverage. Trạng thái này không tự chứng minh learner mastery.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-PYTHON-314-STDLIB-RUNTIME]]
2. [[SRC-TLPI-2010]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-PYTHON-314-STDLIB-RUNTIME]] — `src.docs.python-3.14-stdlib-runtime` | Python 3.14.8 Library Reference; accessed 2026-10-02 | cơ chế và boundary liên quan trực tiếp tới `process isolation, IPC/serialization và startup cost` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L023 |
| [[SRC-TLPI-2010]] — `src.book.tlpi.2010` | process, thread, IPC và lifecycle scopes trong source record | cơ chế và boundary liên quan trực tiếp tới `process isolation, IPC/serialization và startup cost` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L023 |

## Key takeaways
- dùng process cho CPU-bound/isolation khi task đủ lớn; batch payload và bound pool
- CPU utilization, serialization bytes/time, RSS, startup, exit codes và orphan check
- `process isolation, IPC/serialization và startup cost` chỉ có nghĩa trong scope, identity, state và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule — kiểm chứng `wiki.de-foundation.processes-isolation-serialization-cost`

> [!important] Phân loại mệnh đề
> Với `wiki.de-foundation.processes-isolation-serialization-cost`, sơ đồ, ví dụ và artifact về **Processes - isolation, serialization and cost** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.docs.python-3.14-stdlib-runtime"] --> B["Khóa boundary"]
    B --> M["Cơ chế: Processes - isolation, serialization and cost"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.de-foundation.processes-isolation-serialization-cost` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **Processes - isolation, serialization and cost**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class WikiDeFoundationProcessesIsolationSerializaEvidence:
    boundary_declared: bool
    independent_oracle: bool
    reversal_trigger: str

    def accepted(self) -> bool:
        return (
            self.boundary_declared
            and self.independent_oracle
            and bool(self.reversal_trigger.strip())
        )

# Concept: Processes - isolation, serialization and cost
# Primary question: Làm thế nào mô hình, kiểm chứng và áp dụng process isolation, IPC/serialization và startup cost?
evidence = WikiDeFoundationProcessesIsolationSerializaEvidence(
    boundary_declared=True,
    independent_oracle=True,
    reversal_trigger="Đảo quyết định khi hard constraint bị vi phạm",
)
assert evidence.accepted()
```

Artifact của `wiki.de-foundation.processes-isolation-serialization-cost` buộc người dùng ghi boundary, oracle và reversal trigger cho **Processes - isolation, serialization and cost**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

<!-- ATOMIC-EXECUTION-CAPSULE:END -->
