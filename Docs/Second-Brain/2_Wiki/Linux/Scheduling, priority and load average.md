---
note_id: wiki.de-foundation.scheduling-priority-and-load-average
concept_key: ck.de.scheduling-priority-and-load-average
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
primary_question: Làm thế nào mô hình, đo và ra quyết định đúng về Scheduling, priority and load average?
source_ids:
  - src.book.tlpi.2010
  - src.docs.linux-kernel-runtime
relationships:
  builds_on: [wiki.de-foundation.user-mode-kernel-mode-and-the-process-lifecycle]
  prerequisite_of: [wiki.de-foundation.memory-virtual-resident-shared-and-oom]
  related_to: []
aliases: [Scheduling, priority and load average]
tags: [wiki/linux, de-foundation, module-5]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/062-scheduling-priority-and-load-average.md
---

# Scheduling, priority and load average

**Tóm tắt bản chất:** Phân biệt máy nghẽn CPU với máy nghẽn vào ra chỉ bằng chỉ số hệ thống, không cần đọc mã. Cơ chế chỉ có giá trị khi workload, version, state owner và failure boundary đã được khóa; một con số đẹp ngoài bốn điều kiện đó không đủ để ra quyết định.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, đo và ra quyết định đúng về Scheduling, priority and load average?

## Problem Definition and Operational Relevance

Kết luận CPU bận vì tải trung bình cao · so tải trung bình mà quên số lõi · bỏ qua phần chờ vào ra trong mức dùng CPU. Đây không phải danh sách lỗi cú pháp. Mỗi lỗi làm người vận hành chọn nhầm owner hoặc chữa symptom ở layer sau, khiến thời gian phục hồi tăng dù command vừa chạy trả về thành công.

Năng lực cần giữ sau bài là: Phân biệt máy nghẽn CPU với máy nghẽn vào ra chỉ bằng chỉ số hệ thống, không cần đọc mã. Nếu learner chỉ nhắc lại định nghĩa nhưng không phân biệt được hai state gần nhau trên số đo, bài chưa đạt.

## Mechanism

Bộ lập lịch quyết định tiến trình nào chạy khi nào, và hiểu nó giải thích vài chỉ số hay bị đọc sai. Lát thời gian và tính công bằng; độ ưu tiên và giá trị nhường. Chỉ số tải trung bình là chỉ số bị hiểu sai nhiều nhất trên Linux: nó đếm cả tiến trình đang chạy lẫn tiến trình đang chờ vào ra không ngắt được, nên **tải trung bình cao không đồng nghĩa CPU bận**; một máy đĩa hỏng có tải trung bình rất cao trong khi CPU rảnh. Cách đọc đúng: so tải trung bình với số lõi, rồi đối chiếu với tỉ lệ CPU chờ vào ra để biết đang nghẽn ở đâu. Mức dùng CPU chia theo loại và ý nghĩa của từng loại, đặc biệt phần chờ vào ra và phần bị đánh cắp trên máy ảo. Độ dài hàng đợi chạy. Ba tình huống mà thêm tiến trình làm mọi thứ chậm đi thay vì nhanh lên.

Tách ba lớp khi đọc cơ chế `wiki.de-foundation.scheduling-priority-and-load-average`: declared state là điều cấu hình hoặc API yêu cầu; executed state là việc runtime thực sự làm; consumer-visible state là điều client hay operator quan sát. Ba lớp có thể lệch nhau vì cache, buffering, retry, scheduling, queue hoặc failure giữa hai transition. Evidence phải chỉ ra lớp nào đang được đo.

## Decision Framework

| Bước | Câu hỏi phải khóa | Điều kiện đạt |
|---|---|---|
| Observe | Khóa process, resource, file descriptor và time window | Không trộn symptom giữa hai owner |
| Probe | Dùng phép đo read-only hẹp nhất | Probe phân biệt được hai giả thuyết |
| Contain | Giảm harm trước mutation | Có rollback và state snapshot |
| Escalate | Chuyển owner khi boundary đã chứng minh | Evidence đủ tái hiện |

Quy tắc mặc định là chọn phép giải thích đơn giản nhất qua được hard constraints, rồi viết trước reversal trigger. Với `Scheduling, priority and load average`, absence of error không phải pass; pass cần observation đúng grain, một oracle độc lập và changed-constraint case đủ làm model có cơ hội thất bại.

## Worked Case: Scheduling, priority and load average

Tạo bốn tình huống tải: bão hoà CPU, chờ vào ra nặng, áp lực bộ nhớ, và nhiều tiến trình chờ được cấp CPU. Với mỗi tình huống, ghi tải trung bình, mức dùng CPU chia theo loại, và độ dài hàng đợi chạy. Phân loại từng tình huống. Chỉ ra tình huống nào có tải trung bình cao mà CPU rảnh.

Trong case `wiki.de-foundation.scheduling-priority-and-load-average`, learner ghi expected transition, input snapshot, version và giới hạn an toàn trước khi chạy. Sau execution, họ giữ raw counter, timestamp, exit status, state trước-sau và giải thích delta bằng mechanism ở trên. Đánh giá không cho phép sửa expected result sau khi nhìn output mà không ghi change record.

Biến thể khó hơn đổi một constraint có khả năng đảo kết luận: workload shape, memory pressure, connection reuse, retry budget, permission hoặc dependency direction. Tầng *phân tích*. Objective là đọc và diễn giải chỉ số đúng, kỹ năng dùng trực tiếp khi trực. Kiểm bằng bốn máy mô phỏng; đạt khi phân loại đúng ít nhất ba và mỗi lần dẫn được chỉ số phân biệt chứ chỉ tải trung bình.

## Limits and Common Errors

**Hiểu lầm:** Kết luận CPU bận vì tải trung bình cao. **Thực tế:** tín hiệu chỉ chứng minh điều nó đo trong đúng scope; state ở layer khác vẫn có thể trái ngược. **Vì sao nghe hợp lý:** happy path nhỏ thường không chạm queue, cache, partial progress hoặc restart.

**Hiểu lầm:** so tải trung bình mà quên số lõi. **Thực tế:** tool và API cung cấp primitive, không tự cấp ownership, deadline, idempotency hay recovery policy. **Vì sao nghe hợp lý:** syntax gọn che mất protocol và lifecycle phía dưới.

Với `wiki.de-foundation.scheduling-priority-and-load-average`, một edge case đáng giữ là observation đúng nhưng diagnosis sai: counter tăng thật, song nguyên nhân điều khiển nằm ở layer trước. Muốn tránh, timeline phải nối trigger tới consumer harm và ghi rõ negative control nào đã loại giả thuyết cạnh tranh.

## Nếu Bạn Dạy Lại Điều Này...

Mở bài bằng một dự đoán dễ sai về `Scheduling, priority and load average`, không mở bằng định nghĩa. Cho hai trace gần giống nhau nhưng khác đúng một state boundary; learner phải chọn probe tiếp theo trước khi được xem đáp án.

Bài tập seed dùng chính lab của DE-L062, sau đó đổi constraint đủ mạnh để buộc giữ hoặc đảo quyết định. Người dạy chấm reasoning chain và evidence, không chấm việc learner đoán đúng tên công cụ.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `Scheduling, priority and load average` dùng điều kiện hoàn thành sau: Phân loại đúng ≥ 3/4 tình huống, và chỉ ra đúng tình huống tải trung bình cao trong khi CPU rảnh. Mỗi probe phải có prediction, failure signal và independent oracle.

### Probe 1: state transition và invariant

**Mệnh đề P1 cần kiểm.** Bộ lập lịch quyết định tiến trình nào chạy khi nào, và hiểu nó giải thích vài chỉ số hay bị đọc sai.

**Thiết kế phép thử cho `wiki.de-foundation.scheduling-priority-and-load-average`.** Với `wiki.de-foundation.scheduling-priority-and-load-average`, tạo positive và negative control chỉ khác một điều kiện; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P1 cần giữ.** Với `wiki.de-foundation.scheduling-priority-and-load-average`, lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề P2 cần kiểm.** Phân biệt máy nghẽn CPU với máy nghẽn vào ra chỉ bằng chỉ số hệ thống, không cần đọc mã.

**Thiết kế phép thử cho `wiki.de-foundation.scheduling-priority-and-load-average`.** Với `wiki.de-foundation.scheduling-priority-and-load-average`, tạo boundary case ngay trước và sau ngưỡng; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P2 cần giữ.** Với `wiki.de-foundation.scheduling-priority-and-load-average`, lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề P3 cần kiểm.** Tầng *phân tích*.

**Thiết kế phép thử cho `wiki.de-foundation.scheduling-priority-and-load-average`.** Với `wiki.de-foundation.scheduling-priority-and-load-average`, tạo replay cùng identity nhưng đổi state; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P3 cần giữ.** Với `wiki.de-foundation.scheduling-priority-and-load-average`, lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề P4 cần kiểm.** Tạo bốn tình huống tải: bão hoà CPU, chờ vào ra nặng, áp lực bộ nhớ, và nhiều tiến trình chờ được cấp CPU.

**Thiết kế phép thử cho `wiki.de-foundation.scheduling-priority-and-load-average`.** Với `wiki.de-foundation.scheduling-priority-and-load-average`, tạo failure inject trước và sau transition bền vững; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P4 cần giữ.** Với `wiki.de-foundation.scheduling-priority-and-load-average`, lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề P5 cần kiểm.** Kết luận CPU bận vì tải trung bình cao · so tải trung bình mà quên số lõi · bỏ qua phần chờ vào ra trong mức dùng CPU.

**Thiết kế phép thử cho `wiki.de-foundation.scheduling-priority-and-load-average`.** Với `wiki.de-foundation.scheduling-priority-and-load-average`, tạo changed scale làm cost model đổi; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P5 cần giữ.** Với `wiki.de-foundation.scheduling-priority-and-load-average`, lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề P6 cần kiểm.** Phân loại đúng ≥ 3/4 tình huống, và chỉ ra đúng tình huống tải trung bình cao trong khi CPU rảnh.

**Thiết kế phép thử cho `wiki.de-foundation.scheduling-priority-and-load-average`.** Với `wiki.de-foundation.scheduling-priority-and-load-average`, tạo adversarial order, skew hoặc packet timing; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P6 cần giữ.** Với `wiki.de-foundation.scheduling-priority-and-load-average`, lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề P7 cần kiểm.** Bộ lập lịch quyết định tiến trình nào chạy khi nào, và hiểu nó giải thích vài chỉ số hay bị đọc sai.

**Thiết kế phép thử cho `wiki.de-foundation.scheduling-priority-and-load-average`.** Với `wiki.de-foundation.scheduling-priority-and-load-average`, tạo fresh environment không cache; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P7 cần giữ.** Với `wiki.de-foundation.scheduling-priority-and-load-average`, lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề P8 cần kiểm.** Phân biệt máy nghẽn CPU với máy nghẽn vào ra chỉ bằng chỉ số hệ thống, không cần đọc mã.

**Thiết kế phép thử cho `wiki.de-foundation.scheduling-priority-and-load-average`.** Với `wiki.de-foundation.scheduling-priority-and-load-average`, tạo independent oracle không dùng chung implementation; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P8 cần giữ.** Với `wiki.de-foundation.scheduling-priority-and-load-average`, lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề P9 cần kiểm.** Tầng *phân tích*.

**Thiết kế phép thử cho `wiki.de-foundation.scheduling-priority-and-load-average`.** Với `wiki.de-foundation.scheduling-priority-and-load-average`, tạo partial progress rồi restart; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P9 cần giữ.** Với `wiki.de-foundation.scheduling-priority-and-load-average`, lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề P10 cần kiểm.** Tạo bốn tình huống tải: bão hoà CPU, chờ vào ra nặng, áp lực bộ nhớ, và nhiều tiến trình chờ được cấp CPU.

**Thiết kế phép thử cho `wiki.de-foundation.scheduling-priority-and-load-average`.** Với `wiki.de-foundation.scheduling-priority-and-load-average`, tạo missing evidence phải abstain; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P10 cần giữ.** Với `wiki.de-foundation.scheduling-priority-and-load-average`, lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề P11 cần kiểm.** Kết luận CPU bận vì tải trung bình cao · so tải trung bình mà quên số lõi · bỏ qua phần chờ vào ra trong mức dùng CPU.

**Thiết kế phép thử cho `wiki.de-foundation.scheduling-priority-and-load-average`.** Với `wiki.de-foundation.scheduling-priority-and-load-average`, tạo reviewer tái hiện từ evidence package; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P11 cần giữ.** Với `wiki.de-foundation.scheduling-priority-and-load-average`, lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề P12 cần kiểm.** Phân loại đúng ≥ 3/4 tình huống, và chỉ ra đúng tình huống tải trung bình cao trong khi CPU rảnh.

**Thiết kế phép thử cho `wiki.de-foundation.scheduling-priority-and-load-average`.** Với `wiki.de-foundation.scheduling-priority-and-load-average`, tạo constraint đổi đủ để quyết định đảo; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P12 cần giữ.** Với `wiki.de-foundation.scheduling-priority-and-load-average`, lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên khiến mô hình `Scheduling, priority and load average` không còn đúng là gì?

<details><summary>Đáp án</summary>Kết luận CPU bận vì tải trung bình cao · so tải trung bình mà quên số lõi · bỏ qua phần chờ vào ra trong mức dùng CPU.</details>

2. Evidence nào phân biệt được hai state dễ nhầm?

<details><summary>Đáp án</summary>Tầng *phân tích*. Objective là đọc và diễn giải chỉ số đúng, kỹ năng dùng trực tiếp khi trực. Kiểm bằng bốn máy mô phỏng; đạt khi phân loại đúng ít nhất ba và mỗi lần dẫn được chỉ số phân biệt chứ chỉ tải trung bình.</details>

3. Khi constraint đổi, điều gì quyết định giữ hay đảo lựa chọn?

<details><summary>Đáp án</summary>Phân loại đúng ≥ 3/4 tình huống, và chỉ ra đúng tình huống tải trung bình cao trong khi CPU rảnh.</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `Scheduling, priority and load average` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Hành vi phụ thuộc kernel, distribution, library, network path hoặc hardware phải được kiểm lại trên target đã ghi version.
- Concept key `ck.de.scheduling-priority-and-load-average` đã được owner phê duyệt `canonical`; note thuộc canonical registry coverage. Trạng thái này không tự chứng minh learner mastery.
- Một trace đơn lẻ không chứng minh capacity, reliability hoặc security cho population khác.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-TLPI-2010]]
2. [[SRC-LINUX-KERNEL-RUNTIME-DOCS]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-TLPI-2010]]: `src.book.tlpi.2010` | Chapters 4-39, 49-50, 61 và 63 theo scope record; PDF 113-1418 | mechanism và boundary liên quan trực tiếp tới `Scheduling, priority and load average` | cơ chế, quyết định, case và probe | Đã phủ | phần ngoài objective DE-L062 |
| [[SRC-LINUX-KERNEL-RUNTIME-DOCS]]: `src.docs.linux-kernel-runtime` | PSI, userspace API, io_uring và trace documentation; accessed 2026-10-02 | mechanism và boundary liên quan trực tiếp tới `Scheduling, priority and load average` | cơ chế, quyết định, case và probe | Đã phủ | phần ngoài objective DE-L062 |

## Key takeaways
- Phân biệt máy nghẽn CPU với máy nghẽn vào ra chỉ bằng chỉ số hệ thống, không cần đọc mã.
- Phân loại đúng ≥ 3/4 tình huống, và chỉ ra đúng tình huống tải trung bình cao trong khi CPU rảnh.
- `Scheduling, priority and load average` chỉ có nghĩa trong scope, state, identity và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule: kiểm chứng `wiki.de-foundation.scheduling-priority-and-load-average`

> [!important] Phân loại mệnh đề
> Với `wiki.de-foundation.scheduling-priority-and-load-average`, sơ đồ, ví dụ và artifact về **Scheduling, priority and load average** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.book.tlpi.2010"] --> B["Khóa boundary"]
    B --> M["Cơ chế: Scheduling, priority and load average"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.de-foundation.scheduling-priority-and-load-average` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **Scheduling, priority and load average**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```yaml
concept_id: "wiki.de-foundation.scheduling-priority-and-load-average"
concept: "Scheduling, priority and load average"
primary_question: "Làm thế nào mô hình, đo và ra quyết định đúng về Scheduling, priority and load average?"
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

Artifact của `wiki.de-foundation.scheduling-priority-and-load-average` buộc người dùng ghi boundary, oracle và reversal trigger cho **Scheduling, priority and load average**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

<!-- ATOMIC-EXECUTION-CAPSULE:END -->
