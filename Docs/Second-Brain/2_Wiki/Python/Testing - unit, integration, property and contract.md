---
note_id: wiki.de-foundation.testing-unit-integration-property-contract
concept_key: ck.de.testing-unit-integration-property-contract
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
primary_question: Làm thế nào mô hình, kiểm chứng và áp dụng test portfolio theo failure boundary thay vì pyramid đếm số lượng?
source_ids:
  - src.book.sommerville-software-engineering.10e
  - src.docs.python-3.14-stdlib-runtime
relationships:
  builds_on: [wiki.de-foundation.type-hints-validation-boundary]
  prerequisite_of: [wiki.de-foundation.structured-logging-correlation-actionable-errors]
  related_to: []
aliases: [Testing - unit, integration, property and contract]
tags: [wiki/python, de-foundation, module-2]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/019-testing-unit-integration-property-contract.md
---

# Testing - unit, integration, property and contract

**Tóm tắt bản chất:** unit cô lập decision, integration kiểm adapter, property tìm lớp input, contract khóa producer-consumer semantics Sai boundary ở `test portfolio theo failure boundary thay vì pyramid đếm số lượng` làm kết quả có vẻ đúng trong happy path nhưng không chịu được failure hoặc changed constraint.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, kiểm chứng và áp dụng test portfolio theo failure boundary thay vì pyramid đếm số lượng?

## Nỗi Đau & Động Lực

unit cô lập decision, integration kiểm adapter, property tìm lớp input, contract khóa producer-consumer semantics Với `wiki.de-foundation.testing-unit-integration-property-contract`, điểm phải khóa là state transition và invariant; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Không có mô hình này, lỗi thường lộ ở consumer sau cùng: output sai, latency vọt, resource không được giải phóng hoặc lịch sử không còn tái hiện được. Chi phí thật của `Testing - unit, integration, property and contract` vì thế nằm ở thời gian chẩn đoán và phạm vi phục hồi, không nằm ở số dòng syntax.

## Cơ Chế Tác Động

test double phải đứng ở boundary thật; property không thay example cụ thể; contract không chứng minh implementation nội bộ Với `wiki.de-foundation.testing-unit-integration-property-contract`, điểm phải khóa là identity, ownership và boundary; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hãy tách declared state, executed state và published state của `test portfolio theo failure boundary thay vì pyramid đếm số lượng`. Một command thành công chỉ là executed signal; muốn kết luận cần đối soát consumer-visible invariant và trạng thái còn lại sau restart hoặc replay.

## Bản Đồ Quyết Định

mock chi tiết implementation làm refactor vỡ; integration quá rộng không chỉ ra cause; property thiếu oracle chỉ tạo noise Với `wiki.de-foundation.testing-unit-integration-property-contract`, điểm phải khóa là failure path và recovery; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Quy tắc mặc định cho `Testing - unit, integration, property and contract` là chọn phương án đơn giản nhất qua được hard constraints, rồi ghi rõ điều kiện đảo. Bảng quyết định tối thiểu gồm workload, identity, state owner, time/memory budget, failure domain và khả năng rollback.

## Case Study Thực Chiến: Testing - unit, integration, property and contract

chọn test nhỏ nhất tái hiện risk, rồi bổ sung một test ở boundary nơi lỗi có thể thoát Với `wiki.de-foundation.testing-unit-integration-property-contract`, điểm phải khóa là decision trade-off và reversal trigger; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Case dùng fixture nhỏ nhưng phải giữ cơ chế chi phối. Trước khi chạy, learner viết expected transition; sau khi chạy, họ đối chiếu raw artifact với oracle và giải thích mọi khác biệt thay vì sửa expected cho khớp output.

## Góc Khuất & Ngộ Nhận

fixture/seed, assertion reason, coverage theo requirement và mutation/counterexample evidence Với `wiki.de-foundation.testing-unit-integration-property-contract`, điểm phải khóa là evidence package và oracle; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

**Hiểu lầm:** Happy path chạy nhanh nghĩa là thiết kế đúng. **Thực tế:** mock chi tiết implementation làm refactor vỡ; integration quá rộng không chỉ ra cause; property thiếu oracle chỉ tạo noise **Vì sao nghe hợp lý:** case nhỏ thường không chạm capacity, concurrency, failure hoặc version boundary.

**Hiểu lầm:** Tool hoặc API tự bảo đảm semantics. **Thực tế:** guarantee chỉ tồn tại trong scope và state đã công bố. **Vì sao nghe hợp lý:** syntax che mất protocol phía dưới.

## Nếu Bạn Dạy Lại Điều Này...

đổi implementation nhưng giữ contract, rồi phá semantics để kiểm test phản ứng đúng Với `wiki.de-foundation.testing-unit-integration-property-contract`, điểm phải khóa là changed-constraint transfer; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hook dạy lại bắt đầu bằng một dự đoán dễ sai về `test portfolio theo failure boundary thay vì pyramid đếm số lượng`. Bài tập seed đổi đúng một constraint, yêu cầu learner giữ hoặc đảo quyết định và chỉ ra evidence nào đủ mạnh để thuyết phục một reviewer không tham dự buổi học.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `Testing - unit, integration, property and contract` là: fixture/seed, assertion reason, coverage theo requirement và mutation/counterexample evidence Mỗi probe nối input boundary với failure signal và oracle có thể bác bỏ kết luận.

### Probe 1: state transition và invariant

**Mệnh đề cần kiểm.** unit cô lập decision, integration kiểm adapter, property tìm lớp input, contract khóa producer-consumer semantics

**Thiết kế phép thử cho `wiki.de-foundation.testing-unit-integration-property-contract`.** Với `wiki.de-foundation.testing-unit-integration-property-contract`, tạo positive và negative control chỉ khác một điều kiện; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề cần kiểm.** test double phải đứng ở boundary thật; property không thay example cụ thể; contract không chứng minh implementation nội bộ

**Thiết kế phép thử cho `wiki.de-foundation.testing-unit-integration-property-contract`.** Với `wiki.de-foundation.testing-unit-integration-property-contract`, tạo boundary case ngay trước và sau ngưỡng; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề cần kiểm.** mock chi tiết implementation làm refactor vỡ; integration quá rộng không chỉ ra cause; property thiếu oracle chỉ tạo noise

**Thiết kế phép thử cho `wiki.de-foundation.testing-unit-integration-property-contract`.** Với `wiki.de-foundation.testing-unit-integration-property-contract`, tạo replay cùng identity với state khác; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** chọn test nhỏ nhất tái hiện risk, rồi bổ sung một test ở boundary nơi lỗi có thể thoát

**Thiết kế phép thử cho `wiki.de-foundation.testing-unit-integration-property-contract`.** Với `wiki.de-foundation.testing-unit-integration-property-contract`, tạo failure inject trước và sau durable transition; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề cần kiểm.** fixture/seed, assertion reason, coverage theo requirement và mutation/counterexample evidence

**Thiết kế phép thử cho `wiki.de-foundation.testing-unit-integration-property-contract`.** Với `wiki.de-foundation.testing-unit-integration-property-contract`, tạo changed scale làm cost model đổi; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề cần kiểm.** đổi implementation nhưng giữ contract, rồi phá semantics để kiểm test phản ứng đúng

**Thiết kế phép thử cho `wiki.de-foundation.testing-unit-integration-property-contract`.** Với `wiki.de-foundation.testing-unit-integration-property-contract`, tạo adversarial order hoặc skew; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề cần kiểm.** unit cô lập decision, integration kiểm adapter, property tìm lớp input, contract khóa producer-consumer semantics

**Thiết kế phép thử cho `wiki.de-foundation.testing-unit-integration-property-contract`.** Với `wiki.de-foundation.testing-unit-integration-property-contract`, tạo fresh environment không cache; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề cần kiểm.** test double phải đứng ở boundary thật; property không thay example cụ thể; contract không chứng minh implementation nội bộ

**Thiết kế phép thử cho `wiki.de-foundation.testing-unit-integration-property-contract`.** Với `wiki.de-foundation.testing-unit-integration-property-contract`, tạo independent oracle không dùng chung implementation; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề cần kiểm.** mock chi tiết implementation làm refactor vỡ; integration quá rộng không chỉ ra cause; property thiếu oracle chỉ tạo noise

**Thiết kế phép thử cho `wiki.de-foundation.testing-unit-integration-property-contract`.** Với `wiki.de-foundation.testing-unit-integration-property-contract`, tạo partial progress rồi restart; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** chọn test nhỏ nhất tái hiện risk, rồi bổ sung một test ở boundary nơi lỗi có thể thoát

**Thiết kế phép thử cho `wiki.de-foundation.testing-unit-integration-property-contract`.** Với `wiki.de-foundation.testing-unit-integration-property-contract`, tạo missing evidence phải abstain; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề cần kiểm.** fixture/seed, assertion reason, coverage theo requirement và mutation/counterexample evidence

**Thiết kế phép thử cho `wiki.de-foundation.testing-unit-integration-property-contract`.** Với `wiki.de-foundation.testing-unit-integration-property-contract`, tạo reviewer tái hiện từ package; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề cần kiểm.** đổi implementation nhưng giữ contract, rồi phá semantics để kiểm test phản ứng đúng

**Thiết kế phép thử cho `wiki.de-foundation.testing-unit-integration-property-contract`.** Với `wiki.de-foundation.testing-unit-integration-property-contract`, tạo constraint đổi đủ để quyết định đảo; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên của `test portfolio theo failure boundary thay vì pyramid đếm số lượng` nằm ở đâu?

<details><summary>Đáp án</summary>test double phải đứng ở boundary thật; property không thay example cụ thể; contract không chứng minh implementation nội bộ</details>

2. Failure nào dễ tạo kết quả xanh giả nhất?

<details><summary>Đáp án</summary>mock chi tiết implementation làm refactor vỡ; integration quá rộng không chỉ ra cause; property thiếu oracle chỉ tạo noise</details>

3. Constraint nào khiến quyết định phải đảo?

<details><summary>Đáp án</summary>đổi implementation nhưng giữ contract, rồi phá semantics để kiểm test phản ứng đúng</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `Testing - unit, integration, property and contract` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Mọi kết luận phụ thuộc version, workload, operating system, interpreter/compiler hoặc hardware phải được kiểm lại trên target.
- Concept key `ck.de.testing-unit-integration-property-contract` đã được owner phê duyệt `canonical`; note thuộc canonical registry coverage. Trạng thái này không tự chứng minh learner mastery.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-SOMMERVILLE-SOFTWARE-ENGINEERING-10E]]
2. [[SRC-PYTHON-314-STDLIB-RUNTIME]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-SOMMERVILLE-SOFTWARE-ENGINEERING-10E]] — `src.book.sommerville-software-engineering.10e` | Chapters 4, 7, 8 và 25; PDF 103–132, 169–212, 228–242, 732–756 | cơ chế và boundary liên quan trực tiếp tới `test portfolio theo failure boundary thay vì pyramid đếm số lượng` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L019 |
| [[SRC-PYTHON-314-STDLIB-RUNTIME]] — `src.docs.python-3.14-stdlib-runtime` | Python 3.14.8 Library Reference; accessed 2026-10-02 | cơ chế và boundary liên quan trực tiếp tới `test portfolio theo failure boundary thay vì pyramid đếm số lượng` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L019 |

## Key takeaways
- chọn test nhỏ nhất tái hiện risk, rồi bổ sung một test ở boundary nơi lỗi có thể thoát
- fixture/seed, assertion reason, coverage theo requirement và mutation/counterexample evidence
- `test portfolio theo failure boundary thay vì pyramid đếm số lượng` chỉ có nghĩa trong scope, identity, state và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule — kiểm chứng `wiki.de-foundation.testing-unit-integration-property-contract`

> [!important] Phân loại mệnh đề
> Với `wiki.de-foundation.testing-unit-integration-property-contract`, sơ đồ, ví dụ và artifact về **Testing - unit, integration, property and contract** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.book.sommerville-software-engineering.10e"] --> B["Khóa boundary"]
    B --> M["Cơ chế: Testing - unit, integration, property and contract"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.de-foundation.testing-unit-integration-property-contract` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **Testing - unit, integration, property and contract**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class WikiDeFoundationTestingUnitIntegrationPropEvidence:
    boundary_declared: bool
    independent_oracle: bool
    reversal_trigger: str

    def accepted(self) -> bool:
        return (
            self.boundary_declared
            and self.independent_oracle
            and bool(self.reversal_trigger.strip())
        )

# Concept: Testing - unit, integration, property and contract
# Primary question: Làm thế nào mô hình, kiểm chứng và áp dụng test portfolio theo failure boundary thay vì pyramid đếm số lượng?
evidence = WikiDeFoundationTestingUnitIntegrationPropEvidence(
    boundary_declared=True,
    independent_oracle=True,
    reversal_trigger="Đảo quyết định khi hard constraint bị vi phạm",
)
assert evidence.accepted()
```

Artifact của `wiki.de-foundation.testing-unit-integration-property-contract` buộc người dùng ghi boundary, oracle và reversal trigger cho **Testing - unit, integration, property and contract**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

<!-- ATOMIC-EXECUTION-CAPSULE:END -->
