---
note_id: wiki.de-foundation.cache-lines-locality-cache-cliff
concept_key: ck.de.cache-lines-locality-cache-cliff
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
primary_question: Làm thế nào mô hình, kiểm chứng và áp dụng cache line, spatial/temporal locality và cache cliff?
source_ids:
  - src.book.patterson-hennessy-cod.5e
relationships:
  builds_on: [wiki.de-foundation.memory-hierarchy-cost-model]
  prerequisite_of: [wiki.de-foundation.row-major-vs-column-major-layout]
  related_to: []
aliases: [Cache lines, locality and the cache cliff]
tags: [wiki/computer-architecture, de-foundation, module-4]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/046-cache-lines-locality-cache-cliff.md
---

# Cache lines, locality and the cache cliff

**Tóm tắt bản chất:** memory moves blocks; sequential access reuses line; temporal reuse helps before eviction; working set over capacity raises misses Sai boundary ở `cache line, spatial/temporal locality và cache cliff` làm kết quả có vẻ đúng trong happy path nhưng không chịu được failure hoặc changed constraint.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, kiểm chứng và áp dụng cache line, spatial/temporal locality và cache cliff?

## Nỗi Đau & Động Lực

memory moves blocks; sequential access reuses line; temporal reuse helps before eviction; working set over capacity raises misses Với `wiki.de-foundation.cache-lines-locality-cache-cliff`, điểm phải khóa là state transition và invariant; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Không có mô hình này, lỗi thường lộ ở consumer sau cùng: output sai, latency vọt, resource không được giải phóng hoặc lịch sử không còn tái hiện được. Chi phí thật của `Cache lines, locality and the cache cliff` vì thế nằm ở thời gian chẩn đoán và phạm vi phục hồi, không nằm ở số dòng syntax.

## Cơ Chế Tác Động

line size/cache capacity not portable constant; prefetch and associativity complicate simple model Với `wiki.de-foundation.cache-lines-locality-cache-cliff`, điểm phải khóa là identity, ownership và boundary; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hãy tách declared state, executed state và published state của `cache line, spatial/temporal locality và cache cliff`. Một command thành công chỉ là executed signal; muốn kết luận cần đối soát consumer-visible invariant và trạng thái còn lại sau restart hoặc replay.

## Bản Đồ Quyết Định

false sharing, conflict misses, pointer chasing and stride wasting lines Với `wiki.de-foundation.cache-lines-locality-cache-cliff`, điểm phải khóa là failure path và recovery; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Quy tắc mặc định cho `Cache lines, locality and the cache cliff` là chọn phương án đơn giản nhất qua được hard constraints, rồi ghi rõ điều kiện đảo. Bảng quyết định tối thiểu gồm workload, identity, state owner, time/memory budget, failure domain và khả năng rollback.

## Case Study Thực Chiến: Cache lines, locality and the cache cliff

prefer contiguous batched access; change layout/tiling when counters and sweep show miss-bound behavior Với `wiki.de-foundation.cache-lines-locality-cache-cliff`, điểm phải khóa là decision trade-off và reversal trigger; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Case dùng fixture nhỏ nhưng phải giữ cơ chế chi phối. Trước khi chạy, learner viết expected transition; sau khi chạy, họ đối chiếu raw artifact với oracle và giải thích mọi khác biệt thay vì sửa expected cho khớp output.

## Góc Khuất & Ngộ Nhận

stride/working-set sweep, cache misses, cycles/item and target hardware metadata Với `wiki.de-foundation.cache-lines-locality-cache-cliff`, điểm phải khóa là evidence package và oracle; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

**Hiểu lầm:** Happy path chạy nhanh nghĩa là thiết kế đúng. **Thực tế:** false sharing, conflict misses, pointer chasing and stride wasting lines **Vì sao nghe hợp lý:** case nhỏ thường không chạm capacity, concurrency, failure hoặc version boundary.

**Hiểu lầm:** Tool hoặc API tự bảo đảm semantics. **Thực tế:** guarantee chỉ tồn tại trong scope và state đã công bố. **Vì sao nghe hợp lý:** syntax che mất protocol phía dưới.

## Nếu Bạn Dạy Lại Điều Này...

change stride and add competing array mapping to same sets Với `wiki.de-foundation.cache-lines-locality-cache-cliff`, điểm phải khóa là changed-constraint transfer; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hook dạy lại bắt đầu bằng một dự đoán dễ sai về `cache line, spatial/temporal locality và cache cliff`. Bài tập seed đổi đúng một constraint, yêu cầu learner giữ hoặc đảo quyết định và chỉ ra evidence nào đủ mạnh để thuyết phục một reviewer không tham dự buổi học.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `Cache lines, locality and the cache cliff` là: stride/working-set sweep, cache misses, cycles/item and target hardware metadata Mỗi probe nối input boundary với failure signal và oracle có thể bác bỏ kết luận.

### Probe 1: state transition và invariant

**Mệnh đề cần kiểm.** memory moves blocks; sequential access reuses line; temporal reuse helps before eviction; working set over capacity raises misses

**Thiết kế phép thử cho `wiki.de-foundation.cache-lines-locality-cache-cliff`.** Với `wiki.de-foundation.cache-lines-locality-cache-cliff`, tạo positive và negative control chỉ khác một điều kiện; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề cần kiểm.** line size/cache capacity not portable constant; prefetch and associativity complicate simple model

**Thiết kế phép thử cho `wiki.de-foundation.cache-lines-locality-cache-cliff`.** Với `wiki.de-foundation.cache-lines-locality-cache-cliff`, tạo boundary case ngay trước và sau ngưỡng; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề cần kiểm.** false sharing, conflict misses, pointer chasing and stride wasting lines

**Thiết kế phép thử cho `wiki.de-foundation.cache-lines-locality-cache-cliff`.** Với `wiki.de-foundation.cache-lines-locality-cache-cliff`, tạo replay cùng identity với state khác; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** prefer contiguous batched access; change layout/tiling when counters and sweep show miss-bound behavior

**Thiết kế phép thử cho `wiki.de-foundation.cache-lines-locality-cache-cliff`.** Với `wiki.de-foundation.cache-lines-locality-cache-cliff`, tạo failure inject trước và sau durable transition; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề cần kiểm.** stride/working-set sweep, cache misses, cycles/item and target hardware metadata

**Thiết kế phép thử cho `wiki.de-foundation.cache-lines-locality-cache-cliff`.** Với `wiki.de-foundation.cache-lines-locality-cache-cliff`, tạo changed scale làm cost model đổi; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề cần kiểm.** change stride and add competing array mapping to same sets

**Thiết kế phép thử cho `wiki.de-foundation.cache-lines-locality-cache-cliff`.** Với `wiki.de-foundation.cache-lines-locality-cache-cliff`, tạo adversarial order hoặc skew; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề cần kiểm.** memory moves blocks; sequential access reuses line; temporal reuse helps before eviction; working set over capacity raises misses

**Thiết kế phép thử cho `wiki.de-foundation.cache-lines-locality-cache-cliff`.** Với `wiki.de-foundation.cache-lines-locality-cache-cliff`, tạo fresh environment không cache; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề cần kiểm.** line size/cache capacity not portable constant; prefetch and associativity complicate simple model

**Thiết kế phép thử cho `wiki.de-foundation.cache-lines-locality-cache-cliff`.** Với `wiki.de-foundation.cache-lines-locality-cache-cliff`, tạo independent oracle không dùng chung implementation; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề cần kiểm.** false sharing, conflict misses, pointer chasing and stride wasting lines

**Thiết kế phép thử cho `wiki.de-foundation.cache-lines-locality-cache-cliff`.** Với `wiki.de-foundation.cache-lines-locality-cache-cliff`, tạo partial progress rồi restart; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** prefer contiguous batched access; change layout/tiling when counters and sweep show miss-bound behavior

**Thiết kế phép thử cho `wiki.de-foundation.cache-lines-locality-cache-cliff`.** Với `wiki.de-foundation.cache-lines-locality-cache-cliff`, tạo missing evidence phải abstain; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề cần kiểm.** stride/working-set sweep, cache misses, cycles/item and target hardware metadata

**Thiết kế phép thử cho `wiki.de-foundation.cache-lines-locality-cache-cliff`.** Với `wiki.de-foundation.cache-lines-locality-cache-cliff`, tạo reviewer tái hiện từ package; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề cần kiểm.** change stride and add competing array mapping to same sets

**Thiết kế phép thử cho `wiki.de-foundation.cache-lines-locality-cache-cliff`.** Với `wiki.de-foundation.cache-lines-locality-cache-cliff`, tạo constraint đổi đủ để quyết định đảo; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên của `cache line, spatial/temporal locality và cache cliff` nằm ở đâu?

<details><summary>Đáp án</summary>line size/cache capacity not portable constant; prefetch and associativity complicate simple model</details>

2. Failure nào dễ tạo kết quả xanh giả nhất?

<details><summary>Đáp án</summary>false sharing, conflict misses, pointer chasing and stride wasting lines</details>

3. Constraint nào khiến quyết định phải đảo?

<details><summary>Đáp án</summary>change stride and add competing array mapping to same sets</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `Cache lines, locality and the cache cliff` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Mọi kết luận phụ thuộc version, workload, operating system, interpreter/compiler hoặc hardware phải được kiểm lại trên target.
- Concept key `ck.de.cache-lines-locality-cache-cliff` đã được owner phê duyệt `canonical`; note thuộc canonical registry coverage. Trạng thái này không tự chứng minh learner mastery.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-PATTERSON-HENNESSY-COD-5E]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-PATTERSON-HENNESSY-COD-5E]] — `src.book.patterson-hennessy-cod.5e` | Chapter 5 PDF 397–459; Section 6.3 PDF 523–538 | cơ chế và boundary liên quan trực tiếp tới `cache line, spatial/temporal locality và cache cliff` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L046 |

## Key takeaways
- prefer contiguous batched access; change layout/tiling when counters and sweep show miss-bound behavior
- stride/working-set sweep, cache misses, cycles/item and target hardware metadata
- `cache line, spatial/temporal locality và cache cliff` chỉ có nghĩa trong scope, identity, state và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule — kiểm chứng `wiki.de-foundation.cache-lines-locality-cache-cliff`

> [!important] Phân loại mệnh đề
> Với `wiki.de-foundation.cache-lines-locality-cache-cliff`, sơ đồ, ví dụ và artifact về **Cache lines, locality and the cache cliff** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.book.patterson-hennessy-cod.5e"] --> B["Khóa boundary"]
    B --> M["Cơ chế: Cache lines, locality and the cache cliff"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.de-foundation.cache-lines-locality-cache-cliff` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **Cache lines, locality and the cache cliff**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```yaml
concept_id: "wiki.de-foundation.cache-lines-locality-cache-cliff"
concept: "Cache lines, locality and the cache cliff"
primary_question: "Làm thế nào mô hình, kiểm chứng và áp dụng cache line, spatial/temporal locality và cache cliff?"
decision_contract:
  input_boundary: "Ghi population, thời điểm, owner và điều chưa biết"
  hard_constraints:
    - "Không vượt quyền hoặc privacy boundary"
    - "Không dùng cùng một assumption làm cả implementation và oracle"
  accept_when: "Có observation phân biệt được các lựa chọn"
  reversal_trigger: "Một hard constraint sai hoặc evidence mới đổi recommendation"
evidence_to_keep:
  - "input snapshot"
  - "chosen and rejected options"
  - "independent review result"
```

Artifact của `wiki.de-foundation.cache-lines-locality-cache-cliff` buộc người dùng ghi boundary, oracle và reversal trigger cho **Cache lines, locality and the cache cliff**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

<!-- ATOMIC-EXECUTION-CAPSULE:END -->
