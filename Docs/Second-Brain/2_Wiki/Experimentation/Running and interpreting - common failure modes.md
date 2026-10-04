---
note_id: wiki.da.running-and-interpreting-common-failure-modes
concept_key: ck.da.running-and-interpreting-common-failure-modes
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
primary_question: Làm sao áp dụng Running and interpreting - common failure modes và chứng minh kết quả không xanh giả?
source_ids:
  - src.book.kohavi-tang-xu-trustworthy-experiments.1e
  - src.book.openintro-statistics.4e
relationships:
  builds_on: [wiki.da.sample-size-statistical-power-and-duration]
  prerequisite_of: [wiki.da.when-experiments-are-not-possible]
  related_to: []
aliases: [Running and interpreting - common failure modes]
tags: [wiki/experimentation, data-analyst, module-8]
reference_path: Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/067-running-and-interpreting-common-failure-modes.md
---

# Running and interpreting - common failure modes

**Tóm tắt bản chất:** Nhìn lén và dừng sớm: cơ chế khiến việc kiểm tra hằng ngày rồi dừng khi đạt ngưỡng ý nghĩa làm tăng tỉ lệ dương tính giả, minh hoạ bằng mô phỏng. Vấn đề so sánh bội khi phân tích theo nhiều phân khúc. Bất cân xứng tỉ lệ mẫu là phép kiểm bắt buộc trước khi đọc kết quả. Hiệu ứng mới lạ và hiệu ứng nguyên sơ. Phân biệt kết quả không đạt ngưỡng ý nghĩa với kết luận không có tác dụng. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Problem Definition and Operational Relevance

L067 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **Running and interpreting - common failure modes**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Đọc một báo cáo thí nghiệm và định vị lỗi thiết kế hoặc lỗi phân tích trong đó trước khi chấp nhận kết luận. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Mechanism

Nhìn lén và dừng sớm: cơ chế khiến việc kiểm tra hằng ngày rồi dừng khi đạt ngưỡng ý nghĩa làm tăng tỉ lệ dương tính giả, minh hoạ bằng mô phỏng. Vấn đề so sánh bội khi phân tích theo nhiều phân khúc. Bất cân xứng tỉ lệ mẫu là phép kiểm bắt buộc trước khi đọc kết quả. Hiệu ứng mới lạ và hiệu ứng nguyên sơ. Phân biệt kết quả không đạt ngưỡng ý nghĩa với kết luận không có tác dụng.

Cơ chế của `running-and-interpreting-common-failure-modes` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Bỏ kiểm tra bất cân xứng tỉ lệ mẫu · diễn giải kết quả không đạt ngưỡng thành không có tác dụng · phân tích theo nhiều phân khúc mà không hiệu chỉnh so sánh bội. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Decision Framework

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L067: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành Gọi đúng tên lỗi của cả ba báo cáo có lỗi thiết kế, và nhận đúng trường hợp không kết luận được.. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Worked Case: Running and interpreting - common failure modes

Bài thực hành dùng nhiệm vụ thật của roadmap: Phân tích năm kết quả thí nghiệm. Ba trong số đó có lỗi thiết kế, và một không kết luận được. Gọi tên lỗi của từng trường hợp.

Trước khi thao tác ở `Running and interpreting - common failure modes`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L067 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Limits and Common Errors

**Hiểu lầm:** Output của `Running and interpreting - common failure modes` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Bỏ kiểm tra bất cân xứng tỉ lệ mẫu · diễn giải kết quả không đạt ngưỡng thành không có tác dụng · phân tích theo nhiều phân khúc mà không hiệu chỉnh so sánh bội. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L067 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1: `population`.** Nhìn lén và dừng sớm: cơ chế khiến việc kiểm tra hằng ngày rồi dừng khi đạt ngưỡng ý nghĩa làm tăng tỉ lệ dương tính giả, minh hoạ bằng mô phỏng. Vấn đề so sánh bội khi phân tích theo nhiều phân khúc. Bất cân xứng tỉ lệ mẫu là phép kiểm bắt buộc trước khi đọc kết quả. Hiệu ứng mới lạ và hiệu ứng nguyên sơ. Phân biệt kết quả không đạt ngưỡng ý nghĩa với kết luận không có tác dụng.

**Thiết kế.** Probe 1 của L067 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L067.1.** Đối soát `population` bằng đường tính khác implementation chính của `running-and-interpreting-common-failure-modes`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2: `grain`.** Đọc một báo cáo thí nghiệm và định vị lỗi thiết kế hoặc lỗi phân tích trong đó trước khi chấp nhận kết luận.

**Thiết kế.** Probe 2 của L067 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L067.2.** Đối soát `grain` bằng đường tính khác implementation chính của `running-and-interpreting-common-failure-modes`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3: `identity`.** Bỏ kiểm tra bất cân xứng tỉ lệ mẫu · diễn giải kết quả không đạt ngưỡng thành không có tác dụng · phân tích theo nhiều phân khúc mà không hiệu chỉnh so sánh bội.

**Thiết kế.** Probe 3 của L067 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L067.3.** Đối soát `identity` bằng đường tính khác implementation chính của `running-and-interpreting-common-failure-modes`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4: `time cutoff`.** Gọi đúng tên lỗi của cả ba báo cáo có lỗi thiết kế, và nhận đúng trường hợp không kết luận được.

**Thiết kế.** Probe 4 của L067 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L067.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `running-and-interpreting-common-failure-modes`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5: `missing versus zero`.** Nhìn lén và dừng sớm: cơ chế khiến việc kiểm tra hằng ngày rồi dừng khi đạt ngưỡng ý nghĩa làm tăng tỉ lệ dương tính giả, minh hoạ bằng mô phỏng. Vấn đề so sánh bội khi phân tích theo nhiều phân khúc. Bất cân xứng tỉ lệ mẫu là phép kiểm bắt buộc trước khi đọc kết quả. Hiệu ứng mới lạ và hiệu ứng nguyên sơ. Phân biệt kết quả không đạt ngưỡng ý nghĩa với kết luận không có tác dụng.

**Thiết kế.** Probe 5 của L067 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L067.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `running-and-interpreting-common-failure-modes`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6: `duplicate`.** Đọc một báo cáo thí nghiệm và định vị lỗi thiết kế hoặc lỗi phân tích trong đó trước khi chấp nhận kết luận.

**Thiết kế.** Probe 6 của L067 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L067.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `running-and-interpreting-common-failure-modes`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7: `join fan-out`.** Bỏ kiểm tra bất cân xứng tỉ lệ mẫu · diễn giải kết quả không đạt ngưỡng thành không có tác dụng · phân tích theo nhiều phân khúc mà không hiệu chỉnh so sánh bội.

**Thiết kế.** Probe 7 của L067 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L067.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `running-and-interpreting-common-failure-modes`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8: `changed definition`.** Gọi đúng tên lỗi của cả ba báo cáo có lỗi thiết kế, và nhận đúng trường hợp không kết luận được.

**Thiết kế.** Probe 8 của L067 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L067.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `running-and-interpreting-common-failure-modes`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9: `independent oracle`.** Nhìn lén và dừng sớm: cơ chế khiến việc kiểm tra hằng ngày rồi dừng khi đạt ngưỡng ý nghĩa làm tăng tỉ lệ dương tính giả, minh hoạ bằng mô phỏng. Vấn đề so sánh bội khi phân tích theo nhiều phân khúc. Bất cân xứng tỉ lệ mẫu là phép kiểm bắt buộc trước khi đọc kết quả. Hiệu ứng mới lạ và hiệu ứng nguyên sơ. Phân biệt kết quả không đạt ngưỡng ý nghĩa với kết luận không có tác dụng.

**Thiết kế.** Probe 9 của L067 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L067.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `running-and-interpreting-common-failure-modes`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10: `replay`.** Đọc một báo cáo thí nghiệm và định vị lỗi thiết kế hoặc lỗi phân tích trong đó trước khi chấp nhận kết luận.

**Thiết kế.** Probe 10 của L067 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L067.10.** Đối soát `replay` bằng đường tính khác implementation chính của `running-and-interpreting-common-failure-modes`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11: `fresh snapshot`.** Bỏ kiểm tra bất cân xứng tỉ lệ mẫu · diễn giải kết quả không đạt ngưỡng thành không có tác dụng · phân tích theo nhiều phân khúc mà không hiệu chỉnh so sánh bội.

**Thiết kế.** Probe 11 của L067 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L067.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `running-and-interpreting-common-failure-modes`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12: `novel scenario`.** Gọi đúng tên lỗi của cả ba báo cáo có lỗi thiết kế, và nhận đúng trường hợp không kết luận được.

**Thiết kế.** Probe 12 của L067 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L067.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `running-and-interpreting-common-failure-modes`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L067?

<details><summary>Đáp án</summary>

Đọc một báo cáo thí nghiệm và định vị lỗi thiết kế hoặc lỗi phân tích trong đó trước khi chấp nhận kết luận.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Bỏ kiểm tra bất cân xứng tỉ lệ mẫu · diễn giải kết quả không đạt ngưỡng thành không có tác dụng · phân tích theo nhiều phân khúc mà không hiệu chỉnh so sánh bội.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Gọi đúng tên lỗi của cả ba báo cáo có lỗi thiết kế, và nhận đúng trường hợp không kết luận được.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.running-and-interpreting-common-failure-modes` đã được owner phê duyệt `canonical`; note thuộc canonical registry coverage. Trạng thái này không tự chứng minh learner mastery.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-TRUSTWORTHY-ONLINE-CONTROLLED-EXPERIMENTS]]: `src.book.kohavi-tang-xu-trustworthy-experiments.1e`
2. [[SRC-OPENINTRO-STATISTICS-4E]]: `src.book.openintro-statistics.4e`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-TRUSTWORTHY-ONLINE-CONTROLLED-EXPERIMENTS]]: `src.book.kohavi-tang-xu-trustworthy-experiments.1e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Running and interpreting - common failure modes | các mục cơ chế, case và probe | Đã phủ | ngoài objective L067 |
| [[SRC-OPENINTRO-STATISTICS-4E]]: `src.book.openintro-statistics.4e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Running and interpreting - common failure modes | các mục cơ chế, case và probe | Đã phủ | ngoài objective L067 |

## Key takeaways
- Đọc một báo cáo thí nghiệm và định vị lỗi thiết kế hoặc lỗi phân tích trong đó trước khi chấp nhận kết luận.
- Gọi đúng tên lỗi của cả ba báo cáo có lỗi thiết kế, và nhận đúng trường hợp không kết luận được.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule: kiểm chứng `wiki.da.running-and-interpreting-common-failure-modes`

> [!important] Phân loại mệnh đề
> Với `wiki.da.running-and-interpreting-common-failure-modes`, sơ đồ, ví dụ và artifact về **Running and interpreting - common failure modes** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.book.kohavi-tang-xu-trustworthy-experiments.1e"] --> B["Khóa boundary"]
    B --> M["Cơ chế: Running and interpreting - common failure modes"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.da.running-and-interpreting-common-failure-modes` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **Running and interpreting - common failure modes**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```yaml
concept_id: "wiki.da.running-and-interpreting-common-failure-modes"
concept: "Running and interpreting - common failure modes"
primary_question: "Làm sao áp dụng Running and interpreting - common failure modes và chứng minh kết quả không xanh giả?"
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

Artifact của `wiki.da.running-and-interpreting-common-failure-modes` buộc người dùng ghi boundary, oracle và reversal trigger cho **Running and interpreting - common failure modes**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

<!-- ATOMIC-EXECUTION-CAPSULE:END -->
