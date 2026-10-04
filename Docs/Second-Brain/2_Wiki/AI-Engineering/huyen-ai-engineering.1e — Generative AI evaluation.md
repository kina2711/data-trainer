---
note_id: wiki.book.huyen-ai-engineering.1e.generative-ai-evaluation
concept_key: ck.book.huyen-ai-engineering.1e.generative-ai-evaluation
concept_key_status: canonical
note_type: concept-deep-dive
status: canonical
approved_by: second-brain-owner
approved_at: 2026-10-03
approval_scope: all-registered-notes
canonical_since: 2026-10-03
language: vi
created: 2026-10-03
last_verified: 2026-10-03
review_after: 2027-04-03
editorial_pass: humanized-v3
primary_question: Khi nào dùng Generative AI evaluation, quyết định nào nó hỗ trợ và bằng chứng nào bác bỏ được kết luận?
source_ids:
  - src.book.huyen-ai-engineering.1e
relationships:
  builds_on: [wiki.book.huyen-ai-engineering.1e.agents-tools-and-control-flow]
  prerequisite_of: [wiki.book.huyen-ai-engineering.1e.safety-latency-cost-and-observability]
  related_to: []
aliases: [huyen-ai-engineering.1e — Generative AI evaluation]
tags: [wiki/ai-engineering, book-derived, decision]
reference_path: Material/Shared/Knowledge-Notes/PACK-CURATED-BOOKS-01/huyen-ai-engineering.1e/05-generative-ai-evaluation.md
---

# huyen-ai-engineering.1e: Generative AI evaluation

**Tóm tắt bản chất:** Eval kết hợp deterministic checks, model grading có calibration và human review cho high-risk cases. Note này biến ý tưởng thành decision protocol có thể kiểm tra, không biến lời tác giả thành chân lý ngoài bối cảnh.

## Problem Definition and Operational Relevance

Vấn đề mà **Generative AI evaluation** giải quyết không phải thiếu thuật ngữ. Đó là lúc người làm dữ liệu phải chọn một hành động nhưng input, boundary và cost of error còn lẫn vào nhau. Khi bỏ qua boundary, một rule đúng trong ví dụ của *AI Engineering* bị kéo sang workload khác và tạo kết luận tự tin hơn bằng chứng.

Cái giá của lỗi `huyen-ai-engineering.1e.5` quanh **Generative AI evaluation** xuất hiện ở consumer: quyết định sai population, tối ưu nhầm metric, mất khả năng replay hoặc không biết lúc nào cần đảo lựa chọn. Vì vậy note khóa bốn thứ trước: claim, conditions, observable artifact và falsifier. Locator gốc cho phần này là **PDF 232-240**; locator chỉ dẫn tới vùng cần đọc lại, không thay thế việc kiểm source khi claim có tác động cao.

## Mechanism

Eval kết hợp deterministic checks, model grading có calibration và human review cho high-risk cases.

Với `huyen-ai-engineering.1e.5`, cơ chế của **Generative AI evaluation** được tách thành sáu bước. (1) Xác định decision và owner. (2) Khóa population, identity, grain và time boundary. (3) Ghi input/precondition cùng unknown có impact-if-wrong. (4) Áp rule hoặc framework ở đúng scope. (5) Tạo observable artifact: bảng, query, model card, dashboard state, run log hoặc decision record. (6) Đối soát bằng oracle không dùng chung assumption với implementation chính.

Phần của tác giả cho `huyen-ai-engineering.1e.5` là khái niệm và trade-off nằm trong `SRC-HUYEN-AI-ENGINEERING-1E` tại PDF 232-240. Phần synthesis của pack là việc chuyển nó thành protocol sáu bước và evidence checklist. Hai lớp này cố ý tách nhau: synthesis có thể thay đổi theo destination, còn attribution và locator không được thay.

## Decision Framework

| Điều kiện | Chọn | Tránh | Bằng chứng |
|---|---|---|---|
| Preconditions rõ và failure recoverable | Áp dụng bounded pilot | Rollout rộng | Fixture, baseline, rollback |
| Unknown đổi semantics | Dừng để xác minh | Tự điền mặc định | Owner, impact-if-wrong |
| Hai option cùng qua hard constraints | Chọn option đơn giản/reversible | Weighted score che hard failure | ADR ngắn, revisit signal |
| Dữ liệu thiếu nhưng coverage đo được | Kết luận có điều kiện | Impute âm thầm | Missing report, sensitivity |
| Consumer harm cao | Tăng independent review | Dùng output như advisory nhẹ | Approval, audit trail |

Default của **Generative AI evaluation** là thử ở boundary nhỏ nhất tạo ra observation phân biệt được hai lựa chọn. Nếu experiment không thể làm recommendation đảo trong bất kỳ kết quả nào, nó không giảm uncertainty và không đáng chạy.

## Worked Case: áp dụng Generative AI evaluation dưới ràng buộc thay đổi

Một nhóm AI áp dụng **Generative AI evaluation** cho trợ lý nội bộ. Eval set tách retrieval, generation và end-to-end task success; nhóm lưu prompt, model, corpus snapshot, latency, cost và groundedness. Điểm trung bình tăng nhưng câu hỏi quyền truy cập thất bại; rollout dừng ở nhóm pilot cho đến khi guardrail và audit trail đạt.

Biến thể khó hơn của `huyen-ai-engineering.1e.5` đổi constraint quanh **Generative AI evaluation**: deadline từ một tuần xuống hai giờ, hoặc volume tăng 100 lần. Đội không được giảm ngưỡng correctness để kịp hạn. Họ giảm phạm vi câu trả lời, giữ hard constraints và ghi phần chưa kiểm là unknown. Đây là transfer test: dùng cùng reasoning nhưng output khác vì cost, reversibility và evidence budget đã đổi.

## Limits and Common Errors

**Hiểu lầm:** Framework trong *AI Engineering* là checklist áp dụng nguyên xi. **Thực tế:** Eval kết hợp deterministic checks, model grading có calibration và human review cho high-risk cases. **Vì sao nghe hợp lý:** tên framework làm các bước trông độc lập với population, version và organization context.

**Hiểu lầm `huyen-ai-engineering.1e.5-B`:** Có nhiều metric hoặc test quanh **Generative AI evaluation** hơn luôn làm kết luận chắc hơn. **Thực tế:** checks dùng chung data-generating assumption có thể sai đồng thời. **Vì sao nghe hợp lý:** số lượng output tạo cảm giác triangulation dù không có oracle độc lập.

**Hiểu lầm `huyen-ai-engineering.1e.5-C`:** Một case thành công của **Generative AI evaluation** chứng minh cơ chế tổng quát. **Thực tế:** case chỉ chứng minh observation trong fixture, version và scale đã chạy. **Vì sao nghe hợp lý:** narrative hoàn chỉnh che những changed constraints chưa xuất hiện.

Edge case `huyen-ai-engineering.1e.5-selection` của **Generative AI evaluation** là selection: dữ liệu quan sát được có thể chỉ là phần đã qua filter, instrumentation hoặc survivor process. Edge case `huyen-ai-engineering.1e.5-delay` tại PDF 232-240 là delayed feedback: output hôm nay chưa có outcome để xác nhận. Cả hai yêu cầu giới hạn claim thay vì thêm tính từ có khả năng.

## Nếu Bạn Dạy Lại Điều Này...

Khi dạy `huyen-ai-engineering.1e.5`, mở bằng hai phương án xử lý **Generative AI evaluation** đều hợp lý và một constraint bị giấu. Người học phải viết decision trước, sau đó hỏi đúng câu làm lộ constraint. Exercise seed đổi một assumption và yêu cầu chỉ ra artifact, oracle, rollback cùng signal khiến quyết định đảo.

## Ma trận kiểm chứng từng mệnh đề

### Probe 1: definition boundary

**Mệnh đề huyen-ai-engineering.1e.5.1.** `Generative AI evaluation` giữ được claim Eval kết hợp deterministic checks, model grading có calibration và human review cho high-risk cases. khi thay đổi `definition boundary` trong scope đã công bố.

**Thiết kế phép thử `huyen-ai-engineering.1e.5.1` cho `definition boundary`.** Tạo control và variant chỉ khác ở `definition boundary`; khóa source snapshot, version, seed, identity, state và expected result trước execution. Với technical artifact, giữ command và raw output. Với decision artifact, giữ input table, chosen option, rejected option và reversal trigger.

**Bằng chứng cần giữ cho `huyen-ai-engineering.1e.5.1` và biến `definition boundary`.** Observation, before/after measure, discrepancy, limitation và reviewer conclusion. Probe không đạt nếu expected được sửa sau khi nhìn output, hoặc oracle dùng lại chính transformation đang được kiểm.

### Probe 2: input and preconditions

**Mệnh đề huyen-ai-engineering.1e.5.2.** `Generative AI evaluation` giữ được claim Eval kết hợp deterministic checks, model grading có calibration và human review cho high-risk cases. khi thay đổi `input and preconditions` trong scope đã công bố.

**Thiết kế phép thử `huyen-ai-engineering.1e.5.2` cho `input and preconditions`.** Tạo control và variant chỉ khác ở `input and preconditions`; khóa source snapshot, version, seed, identity, state và expected result trước execution. Với technical artifact, giữ command và raw output. Với decision artifact, giữ input table, chosen option, rejected option và reversal trigger.

**Bằng chứng cần giữ cho `huyen-ai-engineering.1e.5.2` và biến `input and preconditions`.** Observation, before/after measure, discrepancy, limitation và reviewer conclusion. Probe không đạt nếu expected được sửa sau khi nhìn output, hoặc oracle dùng lại chính transformation đang được kiểm.

### Probe 3: decision threshold

**Mệnh đề huyen-ai-engineering.1e.5.3.** `Generative AI evaluation` giữ được claim Eval kết hợp deterministic checks, model grading có calibration và human review cho high-risk cases. khi thay đổi `decision threshold` trong scope đã công bố.

**Thiết kế phép thử `huyen-ai-engineering.1e.5.3` cho `decision threshold`.** Tạo control và variant chỉ khác ở `decision threshold`; khóa source snapshot, version, seed, identity, state và expected result trước execution. Với technical artifact, giữ command và raw output. Với decision artifact, giữ input table, chosen option, rejected option và reversal trigger.

**Bằng chứng cần giữ cho `huyen-ai-engineering.1e.5.3` và biến `decision threshold`.** Observation, before/after measure, discrepancy, limitation và reviewer conclusion. Probe không đạt nếu expected được sửa sau khi nhìn output, hoặc oracle dùng lại chính transformation đang được kiểm.

### Probe 4: counterexample

**Mệnh đề huyen-ai-engineering.1e.5.4.** `Generative AI evaluation` giữ được claim Eval kết hợp deterministic checks, model grading có calibration và human review cho high-risk cases. khi thay đổi `counterexample` trong scope đã công bố.

**Thiết kế phép thử `huyen-ai-engineering.1e.5.4` cho `counterexample`.** Tạo control và variant chỉ khác ở `counterexample`; khóa source snapshot, version, seed, identity, state và expected result trước execution. Với technical artifact, giữ command và raw output. Với decision artifact, giữ input table, chosen option, rejected option và reversal trigger.

**Bằng chứng cần giữ cho `huyen-ai-engineering.1e.5.4` và biến `counterexample`.** Observation, before/after measure, discrepancy, limitation và reviewer conclusion. Probe không đạt nếu expected được sửa sau khi nhìn output, hoặc oracle dùng lại chính transformation đang được kiểm.

### Probe 5: failure mode

**Mệnh đề huyen-ai-engineering.1e.5.5.** `Generative AI evaluation` giữ được claim Eval kết hợp deterministic checks, model grading có calibration và human review cho high-risk cases. khi thay đổi `failure mode` trong scope đã công bố.

**Thiết kế phép thử `huyen-ai-engineering.1e.5.5` cho `failure mode`.** Tạo control và variant chỉ khác ở `failure mode`; khóa source snapshot, version, seed, identity, state và expected result trước execution. Với technical artifact, giữ command và raw output. Với decision artifact, giữ input table, chosen option, rejected option và reversal trigger.

**Bằng chứng cần giữ cho `huyen-ai-engineering.1e.5.5` và biến `failure mode`.** Observation, before/after measure, discrepancy, limitation và reviewer conclusion. Probe không đạt nếu expected được sửa sau khi nhìn output, hoặc oracle dùng lại chính transformation đang được kiểm.

### Probe 6: changed scale

**Mệnh đề huyen-ai-engineering.1e.5.6.** `Generative AI evaluation` giữ được claim Eval kết hợp deterministic checks, model grading có calibration và human review cho high-risk cases. khi thay đổi `changed scale` trong scope đã công bố.

**Thiết kế phép thử `huyen-ai-engineering.1e.5.6` cho `changed scale`.** Tạo control và variant chỉ khác ở `changed scale`; khóa source snapshot, version, seed, identity, state và expected result trước execution. Với technical artifact, giữ command và raw output. Với decision artifact, giữ input table, chosen option, rejected option và reversal trigger.

**Bằng chứng cần giữ cho `huyen-ai-engineering.1e.5.6` và biến `changed scale`.** Observation, before/after measure, discrepancy, limitation và reviewer conclusion. Probe không đạt nếu expected được sửa sau khi nhìn output, hoặc oracle dùng lại chính transformation đang được kiểm.

### Probe 7: changed time window

**Mệnh đề huyen-ai-engineering.1e.5.7.** `Generative AI evaluation` giữ được claim Eval kết hợp deterministic checks, model grading có calibration và human review cho high-risk cases. khi thay đổi `changed time window` trong scope đã công bố.

**Thiết kế phép thử `huyen-ai-engineering.1e.5.7` cho `changed time window`.** Tạo control và variant chỉ khác ở `changed time window`; khóa source snapshot, version, seed, identity, state và expected result trước execution. Với technical artifact, giữ command và raw output. Với decision artifact, giữ input table, chosen option, rejected option và reversal trigger.

**Bằng chứng cần giữ cho `huyen-ai-engineering.1e.5.7` và biến `changed time window`.** Observation, before/after measure, discrepancy, limitation và reviewer conclusion. Probe không đạt nếu expected được sửa sau khi nhìn output, hoặc oracle dùng lại chính transformation đang được kiểm.

### Probe 8: adversarial case

**Mệnh đề huyen-ai-engineering.1e.5.8.** `Generative AI evaluation` giữ được claim Eval kết hợp deterministic checks, model grading có calibration và human review cho high-risk cases. khi thay đổi `adversarial case` trong scope đã công bố.

**Thiết kế phép thử `huyen-ai-engineering.1e.5.8` cho `adversarial case`.** Tạo control và variant chỉ khác ở `adversarial case`; khóa source snapshot, version, seed, identity, state và expected result trước execution. Với technical artifact, giữ command và raw output. Với decision artifact, giữ input table, chosen option, rejected option và reversal trigger.

**Bằng chứng cần giữ cho `huyen-ai-engineering.1e.5.8` và biến `adversarial case`.** Observation, before/after measure, discrepancy, limitation và reviewer conclusion. Probe không đạt nếu expected được sửa sau khi nhìn output, hoặc oracle dùng lại chính transformation đang được kiểm.

### Probe 9: independent oracle

**Mệnh đề huyen-ai-engineering.1e.5.9.** `Generative AI evaluation` giữ được claim Eval kết hợp deterministic checks, model grading có calibration và human review cho high-risk cases. khi thay đổi `independent oracle` trong scope đã công bố.

**Thiết kế phép thử `huyen-ai-engineering.1e.5.9` cho `independent oracle`.** Tạo control và variant chỉ khác ở `independent oracle`; khóa source snapshot, version, seed, identity, state và expected result trước execution. Với technical artifact, giữ command và raw output. Với decision artifact, giữ input table, chosen option, rejected option và reversal trigger.

**Bằng chứng cần giữ cho `huyen-ai-engineering.1e.5.9` và biến `independent oracle`.** Observation, before/after measure, discrepancy, limitation và reviewer conclusion. Probe không đạt nếu expected được sửa sau khi nhìn output, hoặc oracle dùng lại chính transformation đang được kiểm.

### Probe 10: transfer scenario

**Mệnh đề huyen-ai-engineering.1e.5.10.** `Generative AI evaluation` giữ được claim Eval kết hợp deterministic checks, model grading có calibration và human review cho high-risk cases. khi thay đổi `transfer scenario` trong scope đã công bố.

**Thiết kế phép thử `huyen-ai-engineering.1e.5.10` cho `transfer scenario`.** Tạo control và variant chỉ khác ở `transfer scenario`; khóa source snapshot, version, seed, identity, state và expected result trước execution. Với technical artifact, giữ command và raw output. Với decision artifact, giữ input table, chosen option, rejected option và reversal trigger.

**Bằng chứng cần giữ cho `huyen-ai-engineering.1e.5.10` và biến `transfer scenario`.** Observation, before/after measure, discrepancy, limitation và reviewer conclusion. Probe không đạt nếu expected được sửa sau khi nhìn output, hoặc oracle dùng lại chính transformation đang được kiểm.

## Tự Kiểm Tra Nhanh

1. Claim trung tâm của `Generative AI evaluation` là gì?

<details><summary>Đáp án</summary>

Eval kết hợp deterministic checks, model grading có calibration và human review cho high-risk cases.

</details>

2. Khi nào phải dừng thay vì áp framework?

<details><summary>Đáp án</summary>

Khi unknown làm đổi semantics, blast radius, quyền riêng tư, hard constraint hoặc tiêu chí đạt; ghi owner và impact-if-wrong trước khi tiếp tục.

</details>

3. Bằng chứng nào mạnh hơn một case thành công?

<details><summary>Đáp án</summary>

Control/variant có expected khóa trước, oracle độc lập, changed-constraint test và artifact đủ để reviewer tái hiện.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Locator **PDF 232-240** là vùng đọc đại diện, không phải tuyên bố toàn bộ sách đã được chuyển thành note này.
- Ví dụ là synthesis để kiểm transfer, không phải trải nghiệm production hay case nguyên văn của tác giả.
- Concept key `ck.book.huyen-ai-engineering.1e.generative-ai-evaluation` đã được owner phê duyệt `canonical`; note thuộc canonical registry coverage. Trạng thái này không tự chứng minh learner mastery.
- Nguồn private, copyrighted; không được public hoặc trích dài nếu chưa có authority.

## Reference
1. [[SRC-HUYEN-AI-ENGINEERING-1E]]: `src.book.huyen-ai-engineering.1e`, PDF 232-240.

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-HUYEN-AI-ENGINEERING-1E]]: `src.book.huyen-ai-engineering.1e` | PDF 232-240 | Eval kết hợp deterministic checks, model grading có calibration và human review cho high-risk cases. | mechanism, decision, case, probes | Đã phủ | các chapter và framework khác |

## Key takeaways
- Eval kết hợp deterministic checks, model grading có calibration và human review cho high-risk cases.
- Tách author claim, synthesis và application; không gộp thành một giọng.
- Changed constraint mạnh hơn recall khi kiểm khả năng áp dụng.
- Note kế tiếp theo `prerequisite_of`; output thực tế cần evidence riêng.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule: kiểm chứng `wiki.book.huyen-ai-engineering.1e.generative-ai-evaluation`

> [!important] Phân loại mệnh đề
> Với `wiki.book.huyen-ai-engineering.1e.generative-ai-evaluation`, sơ đồ, ví dụ và artifact về **huyen-ai-engineering.1e: Generative AI evaluation** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.book.huyen-ai-engineering.1e"] --> B["Khóa boundary"]
    B --> M["Cơ chế: huyen-ai-engineering.1e — Generative AI evaluation"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.book.huyen-ai-engineering.1e.generative-ai-evaluation` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **huyen-ai-engineering.1e: Generative AI evaluation**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class WikiBookHuyenAiEngineering1EGenerativeAiEvidence:
    boundary_declared: bool
    independent_oracle: bool
    reversal_trigger: str

    def accepted(self) -> bool:
        return (
            self.boundary_declared
            and self.independent_oracle
            and bool(self.reversal_trigger.strip())
        )

# Concept: huyen-ai-engineering.1e — Generative AI evaluation
# Primary question: Khi nào dùng Generative AI evaluation, quyết định nào nó hỗ trợ và bằng chứng nào bác bỏ được kết luận?
evidence = WikiBookHuyenAiEngineering1EGenerativeAiEvidence(
    boundary_declared=True,
    independent_oracle=True,
    reversal_trigger="Đảo quyết định khi hard constraint bị vi phạm",
)
assert evidence.accepted()
```

Artifact của `wiki.book.huyen-ai-engineering.1e.generative-ai-evaluation` buộc người dùng ghi boundary, oracle và reversal trigger cho **huyen-ai-engineering.1e: Generative AI evaluation**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

<!-- ATOMIC-EXECUTION-CAPSULE:END -->
