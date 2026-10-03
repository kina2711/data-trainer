---
note_id: wiki.da.choosing-a-topic-and-writing-the-spec
concept_key: ck.da.choosing-a-topic-and-writing-the-spec
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
primary_question: Làm sao áp dụng Choosing a topic and writing the spec và chứng minh kết quả không xanh giả?
source_ids:
  - src.web.govuk-data-analytics-tools-guidance
  - src.book.knaflic-storytelling-with-data.1e
relationships:
  builds_on: [wiki.da.data-analyst-interviews]
  prerequisite_of: [wiki.da.execution-and-mid-point-review]
  related_to: []
aliases: [Choosing a topic and writing the spec]
tags: [wiki/data-analysis, data-analyst, module-11]
reference_path: Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/083-choosing-a-topic-and-writing-the-spec.md
---

# Choosing a topic and writing the spec

**Tóm tắt bản chất:** Bốn tiêu chí của một đề khả thi: có dữ liệu thật truy cập được, có câu hỏi nghiệp vụ thật, có một quyết định cụ thể phía sau, và phạm vi hoàn thành được trong 3 tuần. Ba nguồn đề: dữ liệu công khai của Việt Nam, dữ liệu công ty đang làm có xin phép, hoặc bộ dữ liệu của khoá nhưng đặt câu hỏi mới chưa trả lời trong các bài trước. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Nỗi Đau & Động Lực

L083 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **Choosing a topic and writing the spec**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Viết một đặc tả dự án đủ sáu bước của lesson 5 và bảo vệ nó qua bốn tiêu chí khả thi. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Cơ Chế Tác Động

Bốn tiêu chí của một đề khả thi: có dữ liệu thật truy cập được, có câu hỏi nghiệp vụ thật, có một quyết định cụ thể phía sau, và phạm vi hoàn thành được trong 3 tuần. Ba nguồn đề: dữ liệu công khai của Việt Nam, dữ liệu công ty đang làm có xin phép, hoặc bộ dữ liệu của khoá nhưng đặt câu hỏi mới chưa trả lời trong các bài trước.

Cơ chế của `choosing-a-topic-and-writing-the-spec` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Chọn đề theo mức độ sẵn có của dữ liệu thay vì theo quyết định phía sau · phạm vi rộng hơn mức làm được trong 3 tuần · câu hỏi đã được trả lời trong một bài của khoá. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Bản Đồ Quyết Định

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L083: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành “Đặc tả đủ sáu bước và được duyệt qua cả bốn tiêu chí khả thi.”. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Case Study Thực Chiến: Choosing a topic and writing the spec

Bài thực hành dùng nhiệm vụ thật của roadmap: Viết đặc tả dự án đủ sáu bước của lesson 5. Bảo vệ đề trước giảng viên qua bốn tiêu chí. Chỉ đề được duyệt mới làm tiếp.

Trước khi thao tác ở `Choosing a topic and writing the spec`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L083 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Output của `Choosing a topic and writing the spec` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Chọn đề theo mức độ sẵn có của dữ liệu thay vì theo quyết định phía sau · phạm vi rộng hơn mức làm được trong 3 tuần · câu hỏi đã được trả lời trong một bài của khoá. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L083 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1 — `population`.** Bốn tiêu chí của một đề khả thi: có dữ liệu thật truy cập được, có câu hỏi nghiệp vụ thật, có một quyết định cụ thể phía sau, và phạm vi hoàn thành được trong 3 tuần. Ba nguồn đề: dữ liệu công khai của Việt Nam, dữ liệu công ty đang làm có xin phép, hoặc bộ dữ liệu của khoá nhưng đặt câu hỏi mới chưa trả lời trong các bài trước.

**Thiết kế.** Probe 1 của L083 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L083.1.** Đối soát `population` bằng đường tính khác implementation chính của `choosing-a-topic-and-writing-the-spec`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2 — `grain`.** Viết một đặc tả dự án đủ sáu bước của lesson 5 và bảo vệ nó qua bốn tiêu chí khả thi.

**Thiết kế.** Probe 2 của L083 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L083.2.** Đối soát `grain` bằng đường tính khác implementation chính của `choosing-a-topic-and-writing-the-spec`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3 — `identity`.** Chọn đề theo mức độ sẵn có của dữ liệu thay vì theo quyết định phía sau · phạm vi rộng hơn mức làm được trong 3 tuần · câu hỏi đã được trả lời trong một bài của khoá.

**Thiết kế.** Probe 3 của L083 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L083.3.** Đối soát `identity` bằng đường tính khác implementation chính của `choosing-a-topic-and-writing-the-spec`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4 — `time cutoff`.** Đặc tả đủ sáu bước và được duyệt qua cả bốn tiêu chí khả thi.

**Thiết kế.** Probe 4 của L083 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L083.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `choosing-a-topic-and-writing-the-spec`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5 — `missing versus zero`.** Bốn tiêu chí của một đề khả thi: có dữ liệu thật truy cập được, có câu hỏi nghiệp vụ thật, có một quyết định cụ thể phía sau, và phạm vi hoàn thành được trong 3 tuần. Ba nguồn đề: dữ liệu công khai của Việt Nam, dữ liệu công ty đang làm có xin phép, hoặc bộ dữ liệu của khoá nhưng đặt câu hỏi mới chưa trả lời trong các bài trước.

**Thiết kế.** Probe 5 của L083 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L083.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `choosing-a-topic-and-writing-the-spec`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6 — `duplicate`.** Viết một đặc tả dự án đủ sáu bước của lesson 5 và bảo vệ nó qua bốn tiêu chí khả thi.

**Thiết kế.** Probe 6 của L083 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L083.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `choosing-a-topic-and-writing-the-spec`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7 — `join fan-out`.** Chọn đề theo mức độ sẵn có của dữ liệu thay vì theo quyết định phía sau · phạm vi rộng hơn mức làm được trong 3 tuần · câu hỏi đã được trả lời trong một bài của khoá.

**Thiết kế.** Probe 7 của L083 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L083.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `choosing-a-topic-and-writing-the-spec`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8 — `changed definition`.** Đặc tả đủ sáu bước và được duyệt qua cả bốn tiêu chí khả thi.

**Thiết kế.** Probe 8 của L083 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L083.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `choosing-a-topic-and-writing-the-spec`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9 — `independent oracle`.** Bốn tiêu chí của một đề khả thi: có dữ liệu thật truy cập được, có câu hỏi nghiệp vụ thật, có một quyết định cụ thể phía sau, và phạm vi hoàn thành được trong 3 tuần. Ba nguồn đề: dữ liệu công khai của Việt Nam, dữ liệu công ty đang làm có xin phép, hoặc bộ dữ liệu của khoá nhưng đặt câu hỏi mới chưa trả lời trong các bài trước.

**Thiết kế.** Probe 9 của L083 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L083.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `choosing-a-topic-and-writing-the-spec`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10 — `replay`.** Viết một đặc tả dự án đủ sáu bước của lesson 5 và bảo vệ nó qua bốn tiêu chí khả thi.

**Thiết kế.** Probe 10 của L083 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L083.10.** Đối soát `replay` bằng đường tính khác implementation chính của `choosing-a-topic-and-writing-the-spec`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11 — `fresh snapshot`.** Chọn đề theo mức độ sẵn có của dữ liệu thay vì theo quyết định phía sau · phạm vi rộng hơn mức làm được trong 3 tuần · câu hỏi đã được trả lời trong một bài của khoá.

**Thiết kế.** Probe 11 của L083 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L083.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `choosing-a-topic-and-writing-the-spec`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12 — `novel scenario`.** Đặc tả đủ sáu bước và được duyệt qua cả bốn tiêu chí khả thi.

**Thiết kế.** Probe 12 của L083 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L083.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `choosing-a-topic-and-writing-the-spec`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L083?

<details><summary>Đáp án</summary>

Viết một đặc tả dự án đủ sáu bước của lesson 5 và bảo vệ nó qua bốn tiêu chí khả thi.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Chọn đề theo mức độ sẵn có của dữ liệu thay vì theo quyết định phía sau · phạm vi rộng hơn mức làm được trong 3 tuần · câu hỏi đã được trả lời trong một bài của khoá.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Đặc tả đủ sáu bước và được duyệt qua cả bốn tiêu chí khả thi.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.choosing-a-topic-and-writing-the-spec` đã được owner phê duyệt `canonical`; note thuộc canonical registry coverage. Trạng thái này không tự chứng minh learner mastery.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-GOVUK-DATA-ANALYTICS-TOOLS-GUIDANCE]] — `src.web.govuk-data-analytics-tools-guidance`
2. [[SRC-STORYTELLING-WITH-DATA]] — `src.book.knaflic-storytelling-with-data.1e`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-GOVUK-DATA-ANALYTICS-TOOLS-GUIDANCE]] — `src.web.govuk-data-analytics-tools-guidance` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Choosing a topic and writing the spec | các mục cơ chế, case và probe | Đã phủ | ngoài objective L083 |
| [[SRC-STORYTELLING-WITH-DATA]] — `src.book.knaflic-storytelling-with-data.1e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Choosing a topic and writing the spec | các mục cơ chế, case và probe | Đã phủ | ngoài objective L083 |

## Key takeaways
- Viết một đặc tả dự án đủ sáu bước của lesson 5 và bảo vệ nó qua bốn tiêu chí khả thi.
- Đặc tả đủ sáu bước và được duyệt qua cả bốn tiêu chí khả thi.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule — kiểm chứng `wiki.da.choosing-a-topic-and-writing-the-spec`

> [!important] Phân loại mệnh đề
> Với `wiki.da.choosing-a-topic-and-writing-the-spec`, sơ đồ, ví dụ và artifact về **Choosing a topic and writing the spec** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.web.govuk-data-analytics-tools-guidance"] --> B["Khóa boundary"]
    B --> M["Cơ chế: Choosing a topic and writing the spec"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.da.choosing-a-topic-and-writing-the-spec` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **Choosing a topic and writing the spec**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```yaml
concept_id: "wiki.da.choosing-a-topic-and-writing-the-spec"
concept: "Choosing a topic and writing the spec"
primary_question: "Làm sao áp dụng Choosing a topic and writing the spec và chứng minh kết quả không xanh giả?"
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

Artifact của `wiki.da.choosing-a-topic-and-writing-the-spec` buộc người dùng ghi boundary, oracle và reversal trigger cho **Choosing a topic and writing the spec**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

<!-- ATOMIC-EXECUTION-CAPSULE:END -->
