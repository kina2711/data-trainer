# Phase 3: Data Analyst
# Module 6: Visualization and Power BI
# Lesson 48: Color, labels and accessibility

## Mục tiêu bài học

**Năng lực cần chứng minh.** Lập một bộ nguyên tắc màu và nhãn kiểm chứng được bằng công cụ, và áp nó để sửa ba dashboard không đạt.

**Điều kiện hoàn thành.** Cả ba dashboard sau khi sửa qua được bộ lọc mù màu và đạt ngưỡng độ tương phản, kiểm bằng công cụ.

# Color, labels and accessibility

**Tóm tắt bản chất:** Ba loại thang màu: định tính, tuần tự, phân kỳ, và hậu quả cụ thể khi dùng sai loại. Khả năng tiếp cận cho người mù màu và cách kiểm tra bằng bộ lọc mô phỏng. Ngưỡng độ tương phản. Nhãn trực tiếp thay cho chú giải và lý do kỹ thuật của lựa chọn đó. Chú thích mang nội dung diễn giải: tiêu đề nêu điều đáng chú ý thay vì nêu biểu đồ đang hiển thị dữ liệu gì. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Nỗi Đau & Động Lực

L048 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **Color, labels and accessibility**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Lập một bộ nguyên tắc màu và nhãn kiểm chứng được bằng công cụ, và áp nó để sửa ba dashboard không đạt. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Cơ Chế Tác Động

Ba loại thang màu: định tính, tuần tự, phân kỳ, và hậu quả cụ thể khi dùng sai loại. Khả năng tiếp cận cho người mù màu và cách kiểm tra bằng bộ lọc mô phỏng. Ngưỡng độ tương phản. Nhãn trực tiếp thay cho chú giải và lý do kỹ thuật của lựa chọn đó. Chú thích mang nội dung diễn giải: tiêu đề nêu điều đáng chú ý thay vì nêu biểu đồ đang hiển thị dữ liệu gì.

Cơ chế của `color-labels-and-accessibility` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Dùng thang tuần tự cho dữ liệu định tính · phân biệt hạng mục chỉ bằng màu đỏ và xanh lá · tiêu đề chỉ mô tả dữ liệu thay vì nêu kết luận. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Bản Đồ Quyết Định

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L048: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành “Cả ba dashboard sau khi sửa qua được bộ lọc mù màu và đạt ngưỡng độ tương phản, kiểm bằng công cụ.”. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Case Study Thực Chiến: Color, labels and accessibility

Bài thực hành dùng nhiệm vụ thật của roadmap: Kiểm tra ba dashboard cho sẵn qua bộ lọc mù màu và phép đo độ tương phản. Sửa phần không đạt và kiểm lại.

Trước khi thao tác ở `Color, labels and accessibility`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L048 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Output của `Color, labels and accessibility` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Dùng thang tuần tự cho dữ liệu định tính · phân biệt hạng mục chỉ bằng màu đỏ và xanh lá · tiêu đề chỉ mô tả dữ liệu thay vì nêu kết luận. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L048 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1 — `population`.** Ba loại thang màu: định tính, tuần tự, phân kỳ, và hậu quả cụ thể khi dùng sai loại. Khả năng tiếp cận cho người mù màu và cách kiểm tra bằng bộ lọc mô phỏng. Ngưỡng độ tương phản. Nhãn trực tiếp thay cho chú giải và lý do kỹ thuật của lựa chọn đó. Chú thích mang nội dung diễn giải: tiêu đề nêu điều đáng chú ý thay vì nêu biểu đồ đang hiển thị dữ liệu gì.

**Thiết kế.** Probe 1 của L048 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L048.1.** Đối soát `population` bằng đường tính khác implementation chính của `color-labels-and-accessibility`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2 — `grain`.** Lập một bộ nguyên tắc màu và nhãn kiểm chứng được bằng công cụ, và áp nó để sửa ba dashboard không đạt.

**Thiết kế.** Probe 2 của L048 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L048.2.** Đối soát `grain` bằng đường tính khác implementation chính của `color-labels-and-accessibility`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3 — `identity`.** Dùng thang tuần tự cho dữ liệu định tính · phân biệt hạng mục chỉ bằng màu đỏ và xanh lá · tiêu đề chỉ mô tả dữ liệu thay vì nêu kết luận.

**Thiết kế.** Probe 3 của L048 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L048.3.** Đối soát `identity` bằng đường tính khác implementation chính của `color-labels-and-accessibility`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4 — `time cutoff`.** Cả ba dashboard sau khi sửa qua được bộ lọc mù màu và đạt ngưỡng độ tương phản, kiểm bằng công cụ.

**Thiết kế.** Probe 4 của L048 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L048.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `color-labels-and-accessibility`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5 — `missing versus zero`.** Ba loại thang màu: định tính, tuần tự, phân kỳ, và hậu quả cụ thể khi dùng sai loại. Khả năng tiếp cận cho người mù màu và cách kiểm tra bằng bộ lọc mô phỏng. Ngưỡng độ tương phản. Nhãn trực tiếp thay cho chú giải và lý do kỹ thuật của lựa chọn đó. Chú thích mang nội dung diễn giải: tiêu đề nêu điều đáng chú ý thay vì nêu biểu đồ đang hiển thị dữ liệu gì.

**Thiết kế.** Probe 5 của L048 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L048.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `color-labels-and-accessibility`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6 — `duplicate`.** Lập một bộ nguyên tắc màu và nhãn kiểm chứng được bằng công cụ, và áp nó để sửa ba dashboard không đạt.

**Thiết kế.** Probe 6 của L048 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L048.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `color-labels-and-accessibility`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7 — `join fan-out`.** Dùng thang tuần tự cho dữ liệu định tính · phân biệt hạng mục chỉ bằng màu đỏ và xanh lá · tiêu đề chỉ mô tả dữ liệu thay vì nêu kết luận.

**Thiết kế.** Probe 7 của L048 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L048.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `color-labels-and-accessibility`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8 — `changed definition`.** Cả ba dashboard sau khi sửa qua được bộ lọc mù màu và đạt ngưỡng độ tương phản, kiểm bằng công cụ.

**Thiết kế.** Probe 8 của L048 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L048.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `color-labels-and-accessibility`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9 — `independent oracle`.** Ba loại thang màu: định tính, tuần tự, phân kỳ, và hậu quả cụ thể khi dùng sai loại. Khả năng tiếp cận cho người mù màu và cách kiểm tra bằng bộ lọc mô phỏng. Ngưỡng độ tương phản. Nhãn trực tiếp thay cho chú giải và lý do kỹ thuật của lựa chọn đó. Chú thích mang nội dung diễn giải: tiêu đề nêu điều đáng chú ý thay vì nêu biểu đồ đang hiển thị dữ liệu gì.

**Thiết kế.** Probe 9 của L048 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L048.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `color-labels-and-accessibility`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10 — `replay`.** Lập một bộ nguyên tắc màu và nhãn kiểm chứng được bằng công cụ, và áp nó để sửa ba dashboard không đạt.

**Thiết kế.** Probe 10 của L048 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L048.10.** Đối soát `replay` bằng đường tính khác implementation chính của `color-labels-and-accessibility`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11 — `fresh snapshot`.** Dùng thang tuần tự cho dữ liệu định tính · phân biệt hạng mục chỉ bằng màu đỏ và xanh lá · tiêu đề chỉ mô tả dữ liệu thay vì nêu kết luận.

**Thiết kế.** Probe 11 của L048 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L048.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `color-labels-and-accessibility`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12 — `novel scenario`.** Cả ba dashboard sau khi sửa qua được bộ lọc mù màu và đạt ngưỡng độ tương phản, kiểm bằng công cụ.

**Thiết kế.** Probe 12 của L048 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L048.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `color-labels-and-accessibility`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L048?

<details><summary>Đáp án</summary>

Lập một bộ nguyên tắc màu và nhãn kiểm chứng được bằng công cụ, và áp nó để sửa ba dashboard không đạt.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Dùng thang tuần tự cho dữ liệu định tính · phân biệt hạng mục chỉ bằng màu đỏ và xanh lá · tiêu đề chỉ mô tả dữ liệu thay vì nêu kết luận.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Cả ba dashboard sau khi sửa qua được bộ lọc mù màu và đạt ngưỡng độ tương phản, kiểm bằng công cụ.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.color-labels-and-accessibility` đang `proposed`, chưa tính canonical coverage.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-STORYTELLING-WITH-DATA]] — `src.book.knaflic-storytelling-with-data.1e`
2. [[SRC-DEFINITIVE-GUIDE-DAX-3E]] — `src.book.ferrari-russo-definitive-guide-dax.3e`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-STORYTELLING-WITH-DATA]] — `src.book.knaflic-storytelling-with-data.1e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Color, labels and accessibility | các mục cơ chế, case và probe | Đã phủ | ngoài objective L048 |
| [[SRC-DEFINITIVE-GUIDE-DAX-3E]] — `src.book.ferrari-russo-definitive-guide-dax.3e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Color, labels and accessibility | các mục cơ chế, case và probe | Đã phủ | ngoài objective L048 |

## Key takeaways
- Lập một bộ nguyên tắc màu và nhãn kiểm chứng được bằng công cụ, và áp nó để sửa ba dashboard không đạt.
- Cả ba dashboard sau khi sửa qua được bộ lọc mù màu và đạt ngưỡng độ tương phản, kiểm bằng công cụ.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.
