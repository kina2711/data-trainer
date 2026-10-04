---
note_id: wiki.de-foundation.threads-shared-memory-races-locks
concept_key: ck.de.threads-shared-memory-races-locks
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
primary_question: Làm thế nào mô hình, kiểm chứng và áp dụng threads, shared memory, race và lock ownership?
source_ids:
  - src.docs.python-3.14-stdlib-runtime
  - src.book.tlpi.2010
relationships:
  builds_on: [wiki.de-foundation.profiling-before-optimising]
  prerequisite_of: [wiki.de-foundation.processes-isolation-serialization-cost]
  related_to: []
aliases: [Threads - shared memory, races and locks]
tags: [wiki/python, de-foundation, module-2]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/022-threads-shared-memory-races-locks.md
---

# Threads - shared memory, races and locks

**Tóm tắt bản chất:** threads chia sẻ heap; interleaving giữa read-modify-write phá invariant; lock serializes critical section theo ownership Sai boundary ở `threads, shared memory, race và lock ownership` làm kết quả có vẻ đúng trong happy path nhưng không chịu được failure hoặc changed constraint.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, kiểm chứng và áp dụng threads, shared memory, race và lock ownership?

## Problem Definition and Operational Relevance

threads chia sẻ heap; interleaving giữa read-modify-write phá invariant; lock serializes critical section theo ownership Với `wiki.de-foundation.threads-shared-memory-races-locks`, điểm phải khóa là state transition và invariant; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Không có mô hình này, lỗi thường lộ ở consumer sau cùng: output sai, latency vọt, resource không được giải phóng hoặc lịch sử không còn tái hiện được. Chi phí thật của `Threads - shared memory, races and locks` vì thế nằm ở thời gian chẩn đoán và phạm vi phục hồi, không nằm ở số dòng syntax.

## Mechanism

GIL không phải data-race contract; I/O releases và C extensions đổi scheduling; lock không sửa protocol sai Với `wiki.de-foundation.threads-shared-memory-races-locks`, điểm phải khóa là identity, ownership và boundary; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hãy tách declared state, executed state và published state của `threads, shared memory, race và lock ownership`. Một command thành công chỉ là executed signal; muốn kết luận cần đối soát consumer-visible invariant và trạng thái còn lại sau restart hoặc replay.

## Decision Framework

deadlock do order, race hiếm do timing, lock quá rộng gây convoy và throughput collapse Với `wiki.de-foundation.threads-shared-memory-races-locks`, điểm phải khóa là failure path và recovery; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Quy tắc mặc định cho `Threads - shared memory, races and locks` là chọn phương án đơn giản nhất qua được hard constraints, rồi ghi rõ điều kiện đảo. Bảng quyết định tối thiểu gồm workload, identity, state owner, time/memory budget, failure domain và khả năng rollback.

## Worked Case: Threads - shared memory, races and locks

dùng thread cho blocking I/O khi shared-state contract nhỏ; lock theo invariant và global order Với `wiki.de-foundation.threads-shared-memory-races-locks`, điểm phải khóa là decision trade-off và reversal trigger; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Case dùng fixture nhỏ nhưng phải giữ cơ chế chi phối. Trước khi chạy, learner viết expected transition; sau khi chạy, họ đối chiếu raw artifact với oracle và giải thích mọi khác biệt thay vì sửa expected cho khớp output.

## Limits and Common Errors

seeded schedule hooks, invariant counters, lock wait time và deadlock watchdog Với `wiki.de-foundation.threads-shared-memory-races-locks`, điểm phải khóa là evidence package và oracle; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

**Hiểu lầm:** Happy path chạy nhanh nghĩa là thiết kế đúng. **Thực tế:** deadlock do order, race hiếm do timing, lock quá rộng gây convoy và throughput collapse **Vì sao nghe hợp lý:** case nhỏ thường không chạm capacity, concurrency, failure hoặc version boundary.

**Hiểu lầm:** Tool hoặc API tự bảo đảm semantics. **Thực tế:** guarantee chỉ tồn tại trong scope và state đã công bố. **Vì sao nghe hợp lý:** syntax che mất protocol phía dưới.

## Nếu Bạn Dạy Lại Điều Này...

inject yield giữa read/write và đảo lock order trong sandbox Với `wiki.de-foundation.threads-shared-memory-races-locks`, điểm phải khóa là changed-constraint transfer; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hook dạy lại bắt đầu bằng một dự đoán dễ sai về `threads, shared memory, race và lock ownership`. Bài tập seed đổi đúng một constraint, yêu cầu learner giữ hoặc đảo quyết định và chỉ ra evidence nào đủ mạnh để thuyết phục một reviewer không tham dự buổi học.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `Threads - shared memory, races and locks` là: seeded schedule hooks, invariant counters, lock wait time và deadlock watchdog Mỗi probe nối input boundary với failure signal và oracle có thể bác bỏ kết luận.

### Probe 1: state transition và invariant

**Mệnh đề cần kiểm.** threads chia sẻ heap; interleaving giữa read-modify-write phá invariant; lock serializes critical section theo ownership

**Thiết kế phép thử cho `wiki.de-foundation.threads-shared-memory-races-locks`.** Với `wiki.de-foundation.threads-shared-memory-races-locks`, tạo positive và negative control chỉ khác một điều kiện; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề cần kiểm.** GIL không phải data-race contract; I/O releases và C extensions đổi scheduling; lock không sửa protocol sai

**Thiết kế phép thử cho `wiki.de-foundation.threads-shared-memory-races-locks`.** Với `wiki.de-foundation.threads-shared-memory-races-locks`, tạo boundary case ngay trước và sau ngưỡng; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề cần kiểm.** deadlock do order, race hiếm do timing, lock quá rộng gây convoy và throughput collapse

**Thiết kế phép thử cho `wiki.de-foundation.threads-shared-memory-races-locks`.** Với `wiki.de-foundation.threads-shared-memory-races-locks`, tạo replay cùng identity với state khác; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** dùng thread cho blocking I/O khi shared-state contract nhỏ; lock theo invariant và global order

**Thiết kế phép thử cho `wiki.de-foundation.threads-shared-memory-races-locks`.** Với `wiki.de-foundation.threads-shared-memory-races-locks`, tạo failure inject trước và sau durable transition; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề cần kiểm.** seeded schedule hooks, invariant counters, lock wait time và deadlock watchdog

**Thiết kế phép thử cho `wiki.de-foundation.threads-shared-memory-races-locks`.** Với `wiki.de-foundation.threads-shared-memory-races-locks`, tạo changed scale làm cost model đổi; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề cần kiểm.** inject yield giữa read/write và đảo lock order trong sandbox

**Thiết kế phép thử cho `wiki.de-foundation.threads-shared-memory-races-locks`.** Với `wiki.de-foundation.threads-shared-memory-races-locks`, tạo adversarial order hoặc skew; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề cần kiểm.** threads chia sẻ heap; interleaving giữa read-modify-write phá invariant; lock serializes critical section theo ownership

**Thiết kế phép thử cho `wiki.de-foundation.threads-shared-memory-races-locks`.** Với `wiki.de-foundation.threads-shared-memory-races-locks`, tạo fresh environment không cache; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề cần kiểm.** GIL không phải data-race contract; I/O releases và C extensions đổi scheduling; lock không sửa protocol sai

**Thiết kế phép thử cho `wiki.de-foundation.threads-shared-memory-races-locks`.** Với `wiki.de-foundation.threads-shared-memory-races-locks`, tạo independent oracle không dùng chung implementation; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề cần kiểm.** deadlock do order, race hiếm do timing, lock quá rộng gây convoy và throughput collapse

**Thiết kế phép thử cho `wiki.de-foundation.threads-shared-memory-races-locks`.** Với `wiki.de-foundation.threads-shared-memory-races-locks`, tạo partial progress rồi restart; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** dùng thread cho blocking I/O khi shared-state contract nhỏ; lock theo invariant và global order

**Thiết kế phép thử cho `wiki.de-foundation.threads-shared-memory-races-locks`.** Với `wiki.de-foundation.threads-shared-memory-races-locks`, tạo missing evidence phải abstain; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề cần kiểm.** seeded schedule hooks, invariant counters, lock wait time và deadlock watchdog

**Thiết kế phép thử cho `wiki.de-foundation.threads-shared-memory-races-locks`.** Với `wiki.de-foundation.threads-shared-memory-races-locks`, tạo reviewer tái hiện từ package; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề cần kiểm.** inject yield giữa read/write và đảo lock order trong sandbox

**Thiết kế phép thử cho `wiki.de-foundation.threads-shared-memory-races-locks`.** Với `wiki.de-foundation.threads-shared-memory-races-locks`, tạo constraint đổi đủ để quyết định đảo; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên của `threads, shared memory, race và lock ownership` nằm ở đâu?

<details><summary>Đáp án</summary>GIL không phải data-race contract; I/O releases và C extensions đổi scheduling; lock không sửa protocol sai</details>

2. Failure nào dễ tạo kết quả xanh giả nhất?

<details><summary>Đáp án</summary>deadlock do order, race hiếm do timing, lock quá rộng gây convoy và throughput collapse</details>

3. Constraint nào khiến quyết định phải đảo?

<details><summary>Đáp án</summary>inject yield giữa read/write và đảo lock order trong sandbox</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `Threads - shared memory, races and locks` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Mọi kết luận phụ thuộc version, workload, operating system, interpreter/compiler hoặc hardware phải được kiểm lại trên target.
- Concept key `ck.de.threads-shared-memory-races-locks` đã được owner phê duyệt `canonical`; note thuộc canonical registry coverage. Trạng thái này không tự chứng minh learner mastery.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-PYTHON-314-STDLIB-RUNTIME]]
2. [[SRC-TLPI-2010]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-PYTHON-314-STDLIB-RUNTIME]]: `src.docs.python-3.14-stdlib-runtime` | Python 3.14.8 Library Reference; accessed 2026-10-02 | cơ chế và boundary liên quan trực tiếp tới `threads, shared memory, race và lock ownership` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L022 |
| [[SRC-TLPI-2010]]: `src.book.tlpi.2010` | process, thread, IPC và lifecycle scopes trong source record | cơ chế và boundary liên quan trực tiếp tới `threads, shared memory, race và lock ownership` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L022 |

## Key takeaways
- dùng thread cho blocking I/O khi shared-state contract nhỏ; lock theo invariant và global order
- seeded schedule hooks, invariant counters, lock wait time và deadlock watchdog
- `threads, shared memory, race và lock ownership` chỉ có nghĩa trong scope, identity, state và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule: kiểm chứng `wiki.de-foundation.threads-shared-memory-races-locks`

> [!important] Phân loại mệnh đề
> Với `wiki.de-foundation.threads-shared-memory-races-locks`, sơ đồ, ví dụ và artifact về **Threads - shared memory, races and locks** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.docs.python-3.14-stdlib-runtime"] --> B["Khóa boundary"]
    B --> M["Cơ chế: Threads - shared memory, races and locks"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.de-foundation.threads-shared-memory-races-locks` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **Threads - shared memory, races and locks**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class WikiDeFoundationThreadsSharedMemoryRacesLEvidence:
    boundary_declared: bool
    independent_oracle: bool
    reversal_trigger: str

    def accepted(self) -> bool:
        return (
            self.boundary_declared
            and self.independent_oracle
            and bool(self.reversal_trigger.strip())
        )

# Concept: Threads - shared memory, races and locks
# Primary question: Làm thế nào mô hình, kiểm chứng và áp dụng threads, shared memory, race và lock ownership?
evidence = WikiDeFoundationThreadsSharedMemoryRacesLEvidence(
    boundary_declared=True,
    independent_oracle=True,
    reversal_trigger="Đảo quyết định khi hard constraint bị vi phạm",
)
assert evidence.accepted()
```

Artifact của `wiki.de-foundation.threads-shared-memory-races-locks` buộc người dùng ghi boundary, oracle và reversal trigger cho **Threads - shared memory, races and locks**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

<!-- ATOMIC-EXECUTION-CAPSULE:END -->
