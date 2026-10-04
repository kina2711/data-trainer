---
note_id: wiki.de-foundation.memory-virtual-resident-shared-and-oom
concept_key: ck.de.memory-virtual-resident-shared-and-oom
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
primary_question: Làm thế nào mô hình, đo và ra quyết định đúng về Memory - virtual, resident, shared and OOM?
source_ids:
  - src.book.tlpi.2010
  - src.docs.linux-kernel-runtime
relationships:
  builds_on: [wiki.de-foundation.scheduling-priority-and-load-average]
  prerequisite_of: [wiki.de-foundation.filesystems-inodes-file-descriptors-and-leaks]
  related_to: []
aliases: [Memory - virtual, resident, shared and OOM]
tags: [wiki/linux, de-foundation, module-5]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/063-memory-virtual-resident-shared-and-oom.md
---

# Memory - virtual, resident, shared and OOM

**Tóm tắt bản chất:** Chọn đúng chỉ số để trả lời câu hỏi một tiến trình dùng bao nhiêu bộ nhớ, và đọc được bản ghi của bộ giết khi cạn bộ nhớ. Cơ chế chỉ có giá trị khi workload, version, state owner và failure boundary đã được khóa; một con số đẹp ngoài bốn điều kiện đó không đủ để ra quyết định.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, đo và ra quyết định đúng về Memory - virtual, resident, shared and OOM?

## Problem Definition and Operational Relevance

Dùng bộ nhớ ảo để đánh giá mức dùng · cộng bộ nhớ thường trú của nhiều tiến trình dùng chung thư viện · hoảng vì bộ nhớ trống thấp · không biết tìm bản ghi bộ giết ở đâu. Đây không phải danh sách lỗi cú pháp. Mỗi lỗi làm người vận hành chọn nhầm owner hoặc chữa symptom ở layer sau, khiến thời gian phục hồi tăng dù command vừa chạy trả về thành công.

Năng lực cần giữ sau bài là: Chọn đúng chỉ số để trả lời câu hỏi một tiến trình dùng bao nhiêu bộ nhớ, và đọc được bản ghi của bộ giết khi cạn bộ nhớ. Nếu learner chỉ nhắc lại định nghĩa nhưng không phân biệt được hai state gần nhau trên số đo, bài chưa đạt.

## Mechanism

Câu hỏi tiến trình này dùng bao nhiêu bộ nhớ không có một câu trả lời duy nhất, và chọn sai chỉ số dẫn tới kết luận sai. Bốn chỉ số và ý nghĩa: bộ nhớ ảo là không gian địa chỉ đã đăng ký và thường lớn vô lý nên gần như vô dụng để đánh giá; bộ nhớ thường trú là phần thật đang trong RAM; bộ nhớ chia sẻ bị đếm nhiều lần khi cộng các tiến trình; và kích thước tập làm việc là phần thật sự đang được dùng. Bộ nhớ khả dụng khác bộ nhớ trống: phần bộ đệm trang tính là dùng nhưng giải phóng được ngay, nên **bộ nhớ trống thấp không phải vấn đề**, và đây là báo động giả phổ biến nhất. Bộ giết khi cạn bộ nhớ: khi nào kích hoạt, chọn nạn nhân theo điểm số nào, và cách đọc bản ghi của nó trong nhật ký nhân; nối lại tình huống tác vụ bị giết ở tầng container sẽ gặp ở M25.

Tách ba lớp khi đọc cơ chế `wiki.de-foundation.memory-virtual-resident-shared-and-oom`: declared state là điều cấu hình hoặc API yêu cầu; executed state là việc runtime thực sự làm; consumer-visible state là điều client hay operator quan sát. Ba lớp có thể lệch nhau vì cache, buffering, retry, scheduling, queue hoặc failure giữa hai transition. Evidence phải chỉ ra lớp nào đang được đo.

## Decision Framework

| Bước | Câu hỏi phải khóa | Điều kiện đạt |
|---|---|---|
| Observe | Khóa process, resource, file descriptor và time window | Không trộn symptom giữa hai owner |
| Probe | Dùng phép đo read-only hẹp nhất | Probe phân biệt được hai giả thuyết |
| Contain | Giảm harm trước mutation | Có rollback và state snapshot |
| Escalate | Chuyển owner khi boundary đã chứng minh | Evidence đủ tái hiện |

Quy tắc mặc định là chọn phép giải thích đơn giản nhất qua được hard constraints, rồi viết trước reversal trigger. Với `Memory - virtual, resident, shared and OOM`, absence of error không phải pass; pass cần observation đúng grain, một oracle độc lập và changed-constraint case đủ làm model có cơ hội thất bại.

## Worked Case: Memory - virtual, resident, shared and OOM

Chạy ba tiến trình có hồ sơ bộ nhớ khác nhau gồm ánh xạ tệp lớn, cấp phát thật lớn, và dùng chung thư viện. Với mỗi cái, ghi cả bốn chỉ số và giải thích chênh lệch. Đẩy máy tới cạn bộ nhớ, tìm bản ghi của bộ giết trong nhật ký nhân và xác định nạn nhân cùng lý do.

Trong case `wiki.de-foundation.memory-virtual-resident-shared-and-oom`, learner ghi expected transition, input snapshot, version và giới hạn an toàn trước khi chạy. Sau execution, họ giữ raw counter, timestamp, exit status, state trước-sau và giải thích delta bằng mechanism ở trên. Đánh giá không cho phép sửa expected result sau khi nhìn output mà không ghi change record.

Biến thể khó hơn đổi một constraint có khả năng đảo kết luận: workload shape, memory pressure, connection reuse, retry budget, permission hoặc dependency direction. Tầng *phân tích*. Objective đòi chọn đúng công cụ đo cho câu hỏi, chỗ rất dễ kết luận sai. Kiểm bằng bài đo cộng thí nghiệm cạn bộ nhớ; đạt khi chọn đúng chỉ số và đọc đúng nguyên nhân từ nhật ký nhân.

## Limits and Common Errors

**Hiểu lầm:** Dùng bộ nhớ ảo để đánh giá mức dùng. **Thực tế:** tín hiệu chỉ chứng minh điều nó đo trong đúng scope; state ở layer khác vẫn có thể trái ngược. **Vì sao nghe hợp lý:** happy path nhỏ thường không chạm queue, cache, partial progress hoặc restart.

**Hiểu lầm:** cộng bộ nhớ thường trú của nhiều tiến trình dùng chung thư viện. **Thực tế:** tool và API cung cấp primitive, không tự cấp ownership, deadline, idempotency hay recovery policy. **Vì sao nghe hợp lý:** syntax gọn che mất protocol và lifecycle phía dưới.

Với `wiki.de-foundation.memory-virtual-resident-shared-and-oom`, một edge case đáng giữ là observation đúng nhưng diagnosis sai: counter tăng thật, song nguyên nhân điều khiển nằm ở layer trước. Muốn tránh, timeline phải nối trigger tới consumer harm và ghi rõ negative control nào đã loại giả thuyết cạnh tranh.

## Nếu Bạn Dạy Lại Điều Này...

Mở bài bằng một dự đoán dễ sai về `Memory - virtual, resident, shared and OOM`, không mở bằng định nghĩa. Cho hai trace gần giống nhau nhưng khác đúng một state boundary; learner phải chọn probe tiếp theo trước khi được xem đáp án.

Bài tập seed dùng chính lab của DE-L063, sau đó đổi constraint đủ mạnh để buộc giữ hoặc đảo quyết định. Người dạy chấm reasoning chain và evidence, không chấm việc learner đoán đúng tên công cụ.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `Memory - virtual, resident, shared and OOM` dùng điều kiện hoàn thành sau: Chọn đúng chỉ số cho cả ba tiến trình kèm giải thích chênh lệch, và đọc đúng nạn nhân cùng lý do từ nhật ký nhân. Mỗi probe phải có prediction, failure signal và independent oracle.

### Probe 1: state transition và invariant

**Mệnh đề P1 cần kiểm.** Câu hỏi tiến trình này dùng bao nhiêu bộ nhớ không có một câu trả lời duy nhất, và chọn sai chỉ số dẫn tới kết luận sai.

**Thiết kế phép thử cho `wiki.de-foundation.memory-virtual-resident-shared-and-oom`.** Với `wiki.de-foundation.memory-virtual-resident-shared-and-oom`, tạo positive và negative control chỉ khác một điều kiện; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P1 cần giữ.** Với `wiki.de-foundation.memory-virtual-resident-shared-and-oom`, lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề P2 cần kiểm.** Chọn đúng chỉ số để trả lời câu hỏi một tiến trình dùng bao nhiêu bộ nhớ, và đọc được bản ghi của bộ giết khi cạn bộ nhớ.

**Thiết kế phép thử cho `wiki.de-foundation.memory-virtual-resident-shared-and-oom`.** Với `wiki.de-foundation.memory-virtual-resident-shared-and-oom`, tạo boundary case ngay trước và sau ngưỡng; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P2 cần giữ.** Với `wiki.de-foundation.memory-virtual-resident-shared-and-oom`, lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề P3 cần kiểm.** Tầng *phân tích*.

**Thiết kế phép thử cho `wiki.de-foundation.memory-virtual-resident-shared-and-oom`.** Với `wiki.de-foundation.memory-virtual-resident-shared-and-oom`, tạo replay cùng identity nhưng đổi state; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P3 cần giữ.** Với `wiki.de-foundation.memory-virtual-resident-shared-and-oom`, lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề P4 cần kiểm.** Chạy ba tiến trình có hồ sơ bộ nhớ khác nhau gồm ánh xạ tệp lớn, cấp phát thật lớn, và dùng chung thư viện.

**Thiết kế phép thử cho `wiki.de-foundation.memory-virtual-resident-shared-and-oom`.** Với `wiki.de-foundation.memory-virtual-resident-shared-and-oom`, tạo failure inject trước và sau transition bền vững; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P4 cần giữ.** Với `wiki.de-foundation.memory-virtual-resident-shared-and-oom`, lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề P5 cần kiểm.** Dùng bộ nhớ ảo để đánh giá mức dùng · cộng bộ nhớ thường trú của nhiều tiến trình dùng chung thư viện · hoảng vì bộ nhớ trống thấp · không biết tìm bản ghi bộ giết ở đâu.

**Thiết kế phép thử cho `wiki.de-foundation.memory-virtual-resident-shared-and-oom`.** Với `wiki.de-foundation.memory-virtual-resident-shared-and-oom`, tạo changed scale làm cost model đổi; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P5 cần giữ.** Với `wiki.de-foundation.memory-virtual-resident-shared-and-oom`, lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề P6 cần kiểm.** Chọn đúng chỉ số cho cả ba tiến trình kèm giải thích chênh lệch, và đọc đúng nạn nhân cùng lý do từ nhật ký nhân.

**Thiết kế phép thử cho `wiki.de-foundation.memory-virtual-resident-shared-and-oom`.** Với `wiki.de-foundation.memory-virtual-resident-shared-and-oom`, tạo adversarial order, skew hoặc packet timing; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P6 cần giữ.** Với `wiki.de-foundation.memory-virtual-resident-shared-and-oom`, lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề P7 cần kiểm.** Câu hỏi tiến trình này dùng bao nhiêu bộ nhớ không có một câu trả lời duy nhất, và chọn sai chỉ số dẫn tới kết luận sai.

**Thiết kế phép thử cho `wiki.de-foundation.memory-virtual-resident-shared-and-oom`.** Với `wiki.de-foundation.memory-virtual-resident-shared-and-oom`, tạo fresh environment không cache; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P7 cần giữ.** Với `wiki.de-foundation.memory-virtual-resident-shared-and-oom`, lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề P8 cần kiểm.** Chọn đúng chỉ số để trả lời câu hỏi một tiến trình dùng bao nhiêu bộ nhớ, và đọc được bản ghi của bộ giết khi cạn bộ nhớ.

**Thiết kế phép thử cho `wiki.de-foundation.memory-virtual-resident-shared-and-oom`.** Với `wiki.de-foundation.memory-virtual-resident-shared-and-oom`, tạo independent oracle không dùng chung implementation; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P8 cần giữ.** Với `wiki.de-foundation.memory-virtual-resident-shared-and-oom`, lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề P9 cần kiểm.** Tầng *phân tích*.

**Thiết kế phép thử cho `wiki.de-foundation.memory-virtual-resident-shared-and-oom`.** Với `wiki.de-foundation.memory-virtual-resident-shared-and-oom`, tạo partial progress rồi restart; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P9 cần giữ.** Với `wiki.de-foundation.memory-virtual-resident-shared-and-oom`, lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề P10 cần kiểm.** Chạy ba tiến trình có hồ sơ bộ nhớ khác nhau gồm ánh xạ tệp lớn, cấp phát thật lớn, và dùng chung thư viện.

**Thiết kế phép thử cho `wiki.de-foundation.memory-virtual-resident-shared-and-oom`.** Với `wiki.de-foundation.memory-virtual-resident-shared-and-oom`, tạo missing evidence phải abstain; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P10 cần giữ.** Với `wiki.de-foundation.memory-virtual-resident-shared-and-oom`, lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề P11 cần kiểm.** Dùng bộ nhớ ảo để đánh giá mức dùng · cộng bộ nhớ thường trú của nhiều tiến trình dùng chung thư viện · hoảng vì bộ nhớ trống thấp · không biết tìm bản ghi bộ giết ở đâu.

**Thiết kế phép thử cho `wiki.de-foundation.memory-virtual-resident-shared-and-oom`.** Với `wiki.de-foundation.memory-virtual-resident-shared-and-oom`, tạo reviewer tái hiện từ evidence package; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P11 cần giữ.** Với `wiki.de-foundation.memory-virtual-resident-shared-and-oom`, lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề P12 cần kiểm.** Chọn đúng chỉ số cho cả ba tiến trình kèm giải thích chênh lệch, và đọc đúng nạn nhân cùng lý do từ nhật ký nhân.

**Thiết kế phép thử cho `wiki.de-foundation.memory-virtual-resident-shared-and-oom`.** Với `wiki.de-foundation.memory-virtual-resident-shared-and-oom`, tạo constraint đổi đủ để quyết định đảo; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P12 cần giữ.** Với `wiki.de-foundation.memory-virtual-resident-shared-and-oom`, lưu command hoặc harness, raw observation, transition trước-sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên khiến mô hình `Memory - virtual, resident, shared and OOM` không còn đúng là gì?

<details><summary>Đáp án</summary>Dùng bộ nhớ ảo để đánh giá mức dùng · cộng bộ nhớ thường trú của nhiều tiến trình dùng chung thư viện · hoảng vì bộ nhớ trống thấp · không biết tìm bản ghi bộ giết ở đâu.</details>

2. Evidence nào phân biệt được hai state dễ nhầm?

<details><summary>Đáp án</summary>Tầng *phân tích*. Objective đòi chọn đúng công cụ đo cho câu hỏi, chỗ rất dễ kết luận sai. Kiểm bằng bài đo cộng thí nghiệm cạn bộ nhớ; đạt khi chọn đúng chỉ số và đọc đúng nguyên nhân từ nhật ký nhân.</details>

3. Khi constraint đổi, điều gì quyết định giữ hay đảo lựa chọn?

<details><summary>Đáp án</summary>Chọn đúng chỉ số cho cả ba tiến trình kèm giải thích chênh lệch, và đọc đúng nạn nhân cùng lý do từ nhật ký nhân.</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `Memory - virtual, resident, shared and OOM` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Hành vi phụ thuộc kernel, distribution, library, network path hoặc hardware phải được kiểm lại trên target đã ghi version.
- Concept key `ck.de.memory-virtual-resident-shared-and-oom` đã được owner phê duyệt `canonical`; note thuộc canonical registry coverage. Trạng thái này không tự chứng minh learner mastery.
- Một trace đơn lẻ không chứng minh capacity, reliability hoặc security cho population khác.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-TLPI-2010]]
2. [[SRC-LINUX-KERNEL-RUNTIME-DOCS]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-TLPI-2010]]: `src.book.tlpi.2010` | Chapters 4-39, 49-50, 61 và 63 theo scope record; PDF 113-1418 | mechanism và boundary liên quan trực tiếp tới `Memory - virtual, resident, shared and OOM` | cơ chế, quyết định, case và probe | Đã phủ | phần ngoài objective DE-L063 |
| [[SRC-LINUX-KERNEL-RUNTIME-DOCS]]: `src.docs.linux-kernel-runtime` | PSI, userspace API, io_uring và trace documentation; accessed 2026-10-02 | mechanism và boundary liên quan trực tiếp tới `Memory - virtual, resident, shared and OOM` | cơ chế, quyết định, case và probe | Đã phủ | phần ngoài objective DE-L063 |

## Key takeaways
- Chọn đúng chỉ số để trả lời câu hỏi một tiến trình dùng bao nhiêu bộ nhớ, và đọc được bản ghi của bộ giết khi cạn bộ nhớ.
- Chọn đúng chỉ số cho cả ba tiến trình kèm giải thích chênh lệch, và đọc đúng nạn nhân cùng lý do từ nhật ký nhân.
- `Memory - virtual, resident, shared and OOM` chỉ có nghĩa trong scope, state, identity và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule: kiểm chứng `wiki.de-foundation.memory-virtual-resident-shared-and-oom`

> [!important] Phân loại mệnh đề
> Với `wiki.de-foundation.memory-virtual-resident-shared-and-oom`, sơ đồ, ví dụ và artifact về **Memory - virtual, resident, shared and OOM** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.book.tlpi.2010"] --> B["Khóa boundary"]
    B --> M["Cơ chế: Memory - virtual, resident, shared and OOM"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.de-foundation.memory-virtual-resident-shared-and-oom` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **Memory - virtual, resident, shared and OOM**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```yaml
concept_id: "wiki.de-foundation.memory-virtual-resident-shared-and-oom"
concept: "Memory - virtual, resident, shared and OOM"
primary_question: "Làm thế nào mô hình, đo và ra quyết định đúng về Memory - virtual, resident, shared and OOM?"
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

Artifact của `wiki.de-foundation.memory-virtual-resident-shared-and-oom` buộc người dùng ghi boundary, oracle và reversal trigger cho **Memory - virtual, resident, shared and OOM**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

<!-- ATOMIC-EXECUTION-CAPSULE:END -->
