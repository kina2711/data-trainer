# Phase 4: Data Analyst
# Module 8: A-B Testing
# Lesson 65: Experiment design - hypothesis, metrics, unit

## Mục tiêu bài học

**Năng lực cần chứng minh.** Viết phần thiết kế của một tài liệu thí nghiệm: giả thuyết, cấu trúc chỉ số, đơn vị ngẫu nhiên hoá, và đánh giá nguy cơ nhiễm chéo.

**Điều kiện hoàn thành.** Ba tài liệu thiết kế đủ bốn thành phần, và tình huống có nguy cơ nhiễm chéo được xác định đúng kèm cách xử lý.

# Experiment design - hypothesis, metrics, unit

**Tóm tắt bản chất:** Giả thuyết phát biểu trước khi chạy và ở mức cụ thể kiểm được. Cấu trúc chỉ số: một chỉ số chính duy nhất, cộng chỉ số phụ, cộng chỉ số bảo vệ; cơ chế khiến nhiều chỉ số chính làm tăng tỉ lệ dương tính giả. Đơn vị ngẫu nhiên hoá: người dùng, phiên, thiết bị, cùng hậu quả của chọn sai. Nhiễm chéo giữa hai nhóm và điều kiện phát sinh. A/A test để kiểm tra cơ chế ngẫu nhiên hoá. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Nỗi Đau & Động Lực

L065 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **Experiment design - hypothesis, metrics, unit**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Viết phần thiết kế của một tài liệu thí nghiệm: giả thuyết, cấu trúc chỉ số, đơn vị ngẫu nhiên hoá, và đánh giá nguy cơ nhiễm chéo. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Cơ Chế Tác Động

Giả thuyết phát biểu trước khi chạy và ở mức cụ thể kiểm được. Cấu trúc chỉ số: một chỉ số chính duy nhất, cộng chỉ số phụ, cộng chỉ số bảo vệ; cơ chế khiến nhiều chỉ số chính làm tăng tỉ lệ dương tính giả. Đơn vị ngẫu nhiên hoá: người dùng, phiên, thiết bị, cùng hậu quả của chọn sai. Nhiễm chéo giữa hai nhóm và điều kiện phát sinh. A/A test để kiểm tra cơ chế ngẫu nhiên hoá.

Cơ chế của `experiment-design-hypothesis-metrics-unit` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Khai báo nhiều chỉ số chính · chọn phiên làm đơn vị khi tác động kéo dài qua nhiều phiên · bỏ chỉ số bảo vệ nên không phát hiện tác hại ngoài chỉ số chính. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Bản Đồ Quyết Định

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L065: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành “Ba tài liệu thiết kế đủ bốn thành phần, và tình huống có nguy cơ nhiễm chéo được xác định đúng kèm cách xử lý.”. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Case Study Thực Chiến: Experiment design - hypothesis, metrics, unit

Bài thực hành dùng nhiệm vụ thật của roadmap: Viết ba thiết kế cho ba tình huống sản phẩm khác nhau. Xác định tình huống nào có nguy cơ nhiễm chéo và nêu cách xử lý.

Trước khi thao tác ở `Experiment design - hypothesis, metrics, unit`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L065 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Output của `Experiment design - hypothesis, metrics, unit` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Khai báo nhiều chỉ số chính · chọn phiên làm đơn vị khi tác động kéo dài qua nhiều phiên · bỏ chỉ số bảo vệ nên không phát hiện tác hại ngoài chỉ số chính. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L065 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1 — `population`.** Giả thuyết phát biểu trước khi chạy và ở mức cụ thể kiểm được. Cấu trúc chỉ số: một chỉ số chính duy nhất, cộng chỉ số phụ, cộng chỉ số bảo vệ; cơ chế khiến nhiều chỉ số chính làm tăng tỉ lệ dương tính giả. Đơn vị ngẫu nhiên hoá: người dùng, phiên, thiết bị, cùng hậu quả của chọn sai. Nhiễm chéo giữa hai nhóm và điều kiện phát sinh. A/A test để kiểm tra cơ chế ngẫu nhiên hoá.

**Thiết kế.** Probe 1 của L065 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L065.1.** Đối soát `population` bằng đường tính khác implementation chính của `experiment-design-hypothesis-metrics-unit`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2 — `grain`.** Viết phần thiết kế của một tài liệu thí nghiệm: giả thuyết, cấu trúc chỉ số, đơn vị ngẫu nhiên hoá, và đánh giá nguy cơ nhiễm chéo.

**Thiết kế.** Probe 2 của L065 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L065.2.** Đối soát `grain` bằng đường tính khác implementation chính của `experiment-design-hypothesis-metrics-unit`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3 — `identity`.** Khai báo nhiều chỉ số chính · chọn phiên làm đơn vị khi tác động kéo dài qua nhiều phiên · bỏ chỉ số bảo vệ nên không phát hiện tác hại ngoài chỉ số chính.

**Thiết kế.** Probe 3 của L065 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L065.3.** Đối soát `identity` bằng đường tính khác implementation chính của `experiment-design-hypothesis-metrics-unit`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4 — `time cutoff`.** Ba tài liệu thiết kế đủ bốn thành phần, và tình huống có nguy cơ nhiễm chéo được xác định đúng kèm cách xử lý.

**Thiết kế.** Probe 4 của L065 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L065.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `experiment-design-hypothesis-metrics-unit`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5 — `missing versus zero`.** Giả thuyết phát biểu trước khi chạy và ở mức cụ thể kiểm được. Cấu trúc chỉ số: một chỉ số chính duy nhất, cộng chỉ số phụ, cộng chỉ số bảo vệ; cơ chế khiến nhiều chỉ số chính làm tăng tỉ lệ dương tính giả. Đơn vị ngẫu nhiên hoá: người dùng, phiên, thiết bị, cùng hậu quả của chọn sai. Nhiễm chéo giữa hai nhóm và điều kiện phát sinh. A/A test để kiểm tra cơ chế ngẫu nhiên hoá.

**Thiết kế.** Probe 5 của L065 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L065.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `experiment-design-hypothesis-metrics-unit`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6 — `duplicate`.** Viết phần thiết kế của một tài liệu thí nghiệm: giả thuyết, cấu trúc chỉ số, đơn vị ngẫu nhiên hoá, và đánh giá nguy cơ nhiễm chéo.

**Thiết kế.** Probe 6 của L065 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L065.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `experiment-design-hypothesis-metrics-unit`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7 — `join fan-out`.** Khai báo nhiều chỉ số chính · chọn phiên làm đơn vị khi tác động kéo dài qua nhiều phiên · bỏ chỉ số bảo vệ nên không phát hiện tác hại ngoài chỉ số chính.

**Thiết kế.** Probe 7 của L065 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L065.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `experiment-design-hypothesis-metrics-unit`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8 — `changed definition`.** Ba tài liệu thiết kế đủ bốn thành phần, và tình huống có nguy cơ nhiễm chéo được xác định đúng kèm cách xử lý.

**Thiết kế.** Probe 8 của L065 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L065.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `experiment-design-hypothesis-metrics-unit`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9 — `independent oracle`.** Giả thuyết phát biểu trước khi chạy và ở mức cụ thể kiểm được. Cấu trúc chỉ số: một chỉ số chính duy nhất, cộng chỉ số phụ, cộng chỉ số bảo vệ; cơ chế khiến nhiều chỉ số chính làm tăng tỉ lệ dương tính giả. Đơn vị ngẫu nhiên hoá: người dùng, phiên, thiết bị, cùng hậu quả của chọn sai. Nhiễm chéo giữa hai nhóm và điều kiện phát sinh. A/A test để kiểm tra cơ chế ngẫu nhiên hoá.

**Thiết kế.** Probe 9 của L065 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L065.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `experiment-design-hypothesis-metrics-unit`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10 — `replay`.** Viết phần thiết kế của một tài liệu thí nghiệm: giả thuyết, cấu trúc chỉ số, đơn vị ngẫu nhiên hoá, và đánh giá nguy cơ nhiễm chéo.

**Thiết kế.** Probe 10 của L065 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L065.10.** Đối soát `replay` bằng đường tính khác implementation chính của `experiment-design-hypothesis-metrics-unit`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11 — `fresh snapshot`.** Khai báo nhiều chỉ số chính · chọn phiên làm đơn vị khi tác động kéo dài qua nhiều phiên · bỏ chỉ số bảo vệ nên không phát hiện tác hại ngoài chỉ số chính.

**Thiết kế.** Probe 11 của L065 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L065.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `experiment-design-hypothesis-metrics-unit`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12 — `novel scenario`.** Ba tài liệu thiết kế đủ bốn thành phần, và tình huống có nguy cơ nhiễm chéo được xác định đúng kèm cách xử lý.

**Thiết kế.** Probe 12 của L065 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L065.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `experiment-design-hypothesis-metrics-unit`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L065?

<details><summary>Đáp án</summary>

Viết phần thiết kế của một tài liệu thí nghiệm: giả thuyết, cấu trúc chỉ số, đơn vị ngẫu nhiên hoá, và đánh giá nguy cơ nhiễm chéo.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Khai báo nhiều chỉ số chính · chọn phiên làm đơn vị khi tác động kéo dài qua nhiều phiên · bỏ chỉ số bảo vệ nên không phát hiện tác hại ngoài chỉ số chính.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Ba tài liệu thiết kế đủ bốn thành phần, và tình huống có nguy cơ nhiễm chéo được xác định đúng kèm cách xử lý.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.experiment-design-hypothesis-metrics-unit` đang `proposed`, chưa tính canonical coverage.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-TRUSTWORTHY-ONLINE-CONTROLLED-EXPERIMENTS]] — `src.book.kohavi-tang-xu-trustworthy-experiments.1e`
2. [[SRC-OPENINTRO-STATISTICS-4E]] — `src.book.openintro-statistics.4e`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-TRUSTWORTHY-ONLINE-CONTROLLED-EXPERIMENTS]] — `src.book.kohavi-tang-xu-trustworthy-experiments.1e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Experiment design - hypothesis, metrics, unit | các mục cơ chế, case và probe | Đã phủ | ngoài objective L065 |
| [[SRC-OPENINTRO-STATISTICS-4E]] — `src.book.openintro-statistics.4e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Experiment design - hypothesis, metrics, unit | các mục cơ chế, case và probe | Đã phủ | ngoài objective L065 |

## Key takeaways
- Viết phần thiết kế của một tài liệu thí nghiệm: giả thuyết, cấu trúc chỉ số, đơn vị ngẫu nhiên hoá, và đánh giá nguy cơ nhiễm chéo.
- Ba tài liệu thiết kế đủ bốn thành phần, và tình huống có nguy cơ nhiễm chéo được xác định đúng kèm cách xử lý.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.
