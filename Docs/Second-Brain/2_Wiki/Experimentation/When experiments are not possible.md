---
note_id: wiki.da.when-experiments-are-not-possible
concept_key: ck.da.when-experiments-are-not-possible
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
primary_question: Làm sao áp dụng When experiments are not possible và chứng minh kết quả không xanh giả?
source_ids:
  - src.book.kohavi-tang-xu-trustworthy-experiments.1e
  - src.book.openintro-statistics.4e
relationships:
  builds_on: [wiki.da.running-and-interpreting-common-failure-modes]
  prerequisite_of: [wiki.da.environment-jupyter-and-python-basics]
  related_to: []
aliases: [When experiments are not possible]
tags: [wiki/experimentation, data-analyst, module-8]
reference_path: Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/068-when-experiments-are-not-possible.md
---

# When experiments are not possible

**Tóm tắt bản chất:** Ba điều kiện khiến ngẫu nhiên hoá không thực hiện được. Sai khác kép: ý tưởng, giả định xu hướng song song, và cách kiểm tra giả định đó trên dữ liệu trước can thiệp. Chuỗi thời gian gián đoạn. Nhóm đối chứng tổng hợp ở mức nhận biết. Nguyên tắc chung: mỗi phương pháp đi kèm một tập giả định, nên phải nêu và kiểm giả định, và trình bày kết quả với mức chắc chắn thấp hơn thí nghiệm ngẫu nhiên. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Problem Definition and Operational Relevance

L068 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **When experiments are not possible**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Chọn phương pháp suy luận cho một tình huống không thí nghiệm được, nêu giả định của phương pháp, và kiểm giả định đó trên dữ liệu. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Mechanism

Ba điều kiện khiến ngẫu nhiên hoá không thực hiện được. Sai khác kép: ý tưởng, giả định xu hướng song song, và cách kiểm tra giả định đó trên dữ liệu trước can thiệp. Chuỗi thời gian gián đoạn. Nhóm đối chứng tổng hợp ở mức nhận biết. Nguyên tắc chung: mỗi phương pháp đi kèm một tập giả định, nên phải nêu và kiểm giả định, và trình bày kết quả với mức chắc chắn thấp hơn thí nghiệm ngẫu nhiên.

Cơ chế của `when-experiments-are-not-possible` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Dùng sai khác kép mà không kiểm xu hướng song song · trình bày kết quả phương pháp quan sát với mức chắc chắn ngang thí nghiệm · chọn nhóm đối chứng bị ảnh hưởng gián tiếp bởi can thiệp. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Decision Framework

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L068: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành Chọn đúng phương pháp cho ≥ 3/4 tình huống kèm giả định, và phân tích sai khác kép có phần kiểm xu hướng song song trên dữ liệu trước can thiệp.. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Worked Case: When experiments are not possible

Bài thực hành dùng nhiệm vụ thật của roadmap: Bốn tình huống: chọn phương pháp, nêu giả định, chỉ ra cách kiểm. Thực hiện một phân tích sai khác kép đầy đủ có kiểm giả định xu hướng song song.

Trước khi thao tác ở `When experiments are not possible`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L068 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Limits and Common Errors

**Hiểu lầm:** Output của `When experiments are not possible` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Dùng sai khác kép mà không kiểm xu hướng song song · trình bày kết quả phương pháp quan sát với mức chắc chắn ngang thí nghiệm · chọn nhóm đối chứng bị ảnh hưởng gián tiếp bởi can thiệp. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L068 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1: `population`.** Ba điều kiện khiến ngẫu nhiên hoá không thực hiện được. Sai khác kép: ý tưởng, giả định xu hướng song song, và cách kiểm tra giả định đó trên dữ liệu trước can thiệp. Chuỗi thời gian gián đoạn. Nhóm đối chứng tổng hợp ở mức nhận biết. Nguyên tắc chung: mỗi phương pháp đi kèm một tập giả định, nên phải nêu và kiểm giả định, và trình bày kết quả với mức chắc chắn thấp hơn thí nghiệm ngẫu nhiên.

**Thiết kế.** Probe 1 của L068 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L068.1.** Đối soát `population` bằng đường tính khác implementation chính của `when-experiments-are-not-possible`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2: `grain`.** Chọn phương pháp suy luận cho một tình huống không thí nghiệm được, nêu giả định của phương pháp, và kiểm giả định đó trên dữ liệu.

**Thiết kế.** Probe 2 của L068 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L068.2.** Đối soát `grain` bằng đường tính khác implementation chính của `when-experiments-are-not-possible`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3: `identity`.** Dùng sai khác kép mà không kiểm xu hướng song song · trình bày kết quả phương pháp quan sát với mức chắc chắn ngang thí nghiệm · chọn nhóm đối chứng bị ảnh hưởng gián tiếp bởi can thiệp.

**Thiết kế.** Probe 3 của L068 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L068.3.** Đối soát `identity` bằng đường tính khác implementation chính của `when-experiments-are-not-possible`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4: `time cutoff`.** Chọn đúng phương pháp cho ≥ 3/4 tình huống kèm giả định, và phân tích sai khác kép có phần kiểm xu hướng song song trên dữ liệu trước can thiệp.

**Thiết kế.** Probe 4 của L068 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L068.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `when-experiments-are-not-possible`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5: `missing versus zero`.** Ba điều kiện khiến ngẫu nhiên hoá không thực hiện được. Sai khác kép: ý tưởng, giả định xu hướng song song, và cách kiểm tra giả định đó trên dữ liệu trước can thiệp. Chuỗi thời gian gián đoạn. Nhóm đối chứng tổng hợp ở mức nhận biết. Nguyên tắc chung: mỗi phương pháp đi kèm một tập giả định, nên phải nêu và kiểm giả định, và trình bày kết quả với mức chắc chắn thấp hơn thí nghiệm ngẫu nhiên.

**Thiết kế.** Probe 5 của L068 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L068.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `when-experiments-are-not-possible`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6: `duplicate`.** Chọn phương pháp suy luận cho một tình huống không thí nghiệm được, nêu giả định của phương pháp, và kiểm giả định đó trên dữ liệu.

**Thiết kế.** Probe 6 của L068 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L068.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `when-experiments-are-not-possible`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7: `join fan-out`.** Dùng sai khác kép mà không kiểm xu hướng song song · trình bày kết quả phương pháp quan sát với mức chắc chắn ngang thí nghiệm · chọn nhóm đối chứng bị ảnh hưởng gián tiếp bởi can thiệp.

**Thiết kế.** Probe 7 của L068 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L068.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `when-experiments-are-not-possible`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8: `changed definition`.** Chọn đúng phương pháp cho ≥ 3/4 tình huống kèm giả định, và phân tích sai khác kép có phần kiểm xu hướng song song trên dữ liệu trước can thiệp.

**Thiết kế.** Probe 8 của L068 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L068.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `when-experiments-are-not-possible`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9: `independent oracle`.** Ba điều kiện khiến ngẫu nhiên hoá không thực hiện được. Sai khác kép: ý tưởng, giả định xu hướng song song, và cách kiểm tra giả định đó trên dữ liệu trước can thiệp. Chuỗi thời gian gián đoạn. Nhóm đối chứng tổng hợp ở mức nhận biết. Nguyên tắc chung: mỗi phương pháp đi kèm một tập giả định, nên phải nêu và kiểm giả định, và trình bày kết quả với mức chắc chắn thấp hơn thí nghiệm ngẫu nhiên.

**Thiết kế.** Probe 9 của L068 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L068.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `when-experiments-are-not-possible`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10: `replay`.** Chọn phương pháp suy luận cho một tình huống không thí nghiệm được, nêu giả định của phương pháp, và kiểm giả định đó trên dữ liệu.

**Thiết kế.** Probe 10 của L068 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L068.10.** Đối soát `replay` bằng đường tính khác implementation chính của `when-experiments-are-not-possible`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11: `fresh snapshot`.** Dùng sai khác kép mà không kiểm xu hướng song song · trình bày kết quả phương pháp quan sát với mức chắc chắn ngang thí nghiệm · chọn nhóm đối chứng bị ảnh hưởng gián tiếp bởi can thiệp.

**Thiết kế.** Probe 11 của L068 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L068.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `when-experiments-are-not-possible`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12: `novel scenario`.** Chọn đúng phương pháp cho ≥ 3/4 tình huống kèm giả định, và phân tích sai khác kép có phần kiểm xu hướng song song trên dữ liệu trước can thiệp.

**Thiết kế.** Probe 12 của L068 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L068.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `when-experiments-are-not-possible`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L068?

<details><summary>Đáp án</summary>

Chọn phương pháp suy luận cho một tình huống không thí nghiệm được, nêu giả định của phương pháp, và kiểm giả định đó trên dữ liệu.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Dùng sai khác kép mà không kiểm xu hướng song song · trình bày kết quả phương pháp quan sát với mức chắc chắn ngang thí nghiệm · chọn nhóm đối chứng bị ảnh hưởng gián tiếp bởi can thiệp.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Chọn đúng phương pháp cho ≥ 3/4 tình huống kèm giả định, và phân tích sai khác kép có phần kiểm xu hướng song song trên dữ liệu trước can thiệp.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.when-experiments-are-not-possible` đã được owner phê duyệt `canonical`; note thuộc canonical registry coverage. Trạng thái này không tự chứng minh learner mastery.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-TRUSTWORTHY-ONLINE-CONTROLLED-EXPERIMENTS]]: `src.book.kohavi-tang-xu-trustworthy-experiments.1e`
2. [[SRC-OPENINTRO-STATISTICS-4E]]: `src.book.openintro-statistics.4e`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-TRUSTWORTHY-ONLINE-CONTROLLED-EXPERIMENTS]]: `src.book.kohavi-tang-xu-trustworthy-experiments.1e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới When experiments are not possible | các mục cơ chế, case và probe | Đã phủ | ngoài objective L068 |
| [[SRC-OPENINTRO-STATISTICS-4E]]: `src.book.openintro-statistics.4e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới When experiments are not possible | các mục cơ chế, case và probe | Đã phủ | ngoài objective L068 |

## Key takeaways
- Chọn phương pháp suy luận cho một tình huống không thí nghiệm được, nêu giả định của phương pháp, và kiểm giả định đó trên dữ liệu.
- Chọn đúng phương pháp cho ≥ 3/4 tình huống kèm giả định, và phân tích sai khác kép có phần kiểm xu hướng song song trên dữ liệu trước can thiệp.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule: kiểm chứng `wiki.da.when-experiments-are-not-possible`

> [!important] Phân loại mệnh đề
> Với `wiki.da.when-experiments-are-not-possible`, sơ đồ, ví dụ và artifact về **When experiments are not possible** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.book.kohavi-tang-xu-trustworthy-experiments.1e"] --> B["Khóa boundary"]
    B --> M["Cơ chế: When experiments are not possible"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.da.when-experiments-are-not-possible` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **When experiments are not possible**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```yaml
concept_id: "wiki.da.when-experiments-are-not-possible"
concept: "When experiments are not possible"
primary_question: "Làm sao áp dụng When experiments are not possible và chứng minh kết quả không xanh giả?"
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

Artifact của `wiki.da.when-experiments-are-not-possible` buộc người dùng ghi boundary, oracle và reversal trigger cho **When experiments are not possible**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

<!-- ATOMIC-EXECUTION-CAPSULE:END -->
