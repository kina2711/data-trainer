# Phase 4: Data Analyst
# Module 10: Communication and Career
# Lesson 79: Presenting and handling challenge

## Mục tiêu bài học

**Năng lực cần chứng minh.** Bảo vệ một kết luận bất lợi trước hội đồng, giữ được phần có bằng chứng và nhượng bộ đúng phần chưa đủ bằng chứng.

**Điều kiện hoàn thành.** Giữ được phần kết luận có bằng chứng qua cả năm câu phản biện, và nhượng bộ đúng câu nêu giới hạn có thật.

# Presenting and handling challenge

**Tóm tắt bản chất:** Thiết kế slide cho buổi họp 15 phút. Nói rõ chuỗi suy luận thay vì chỉ nêu kết quả. Ba loại câu hỏi và cách xử lý từng loại: câu hỏi tìm thông tin, câu hỏi thử thách phương pháp, câu hỏi bảo vệ một lập trường có sẵn. Trình bày kết quả đi ngược kỳ vọng của người nghe. Cách phát biểu rằng dữ liệu hiện có không trả lời được câu hỏi được đặt ra. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Nỗi Đau & Động Lực

L079 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **Presenting and handling challenge**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Bảo vệ một kết luận bất lợi trước hội đồng, giữ được phần có bằng chứng và nhượng bộ đúng phần chưa đủ bằng chứng. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Cơ Chế Tác Động

Thiết kế slide cho buổi họp 15 phút. Nói rõ chuỗi suy luận thay vì chỉ nêu kết quả. Ba loại câu hỏi và cách xử lý từng loại: câu hỏi tìm thông tin, câu hỏi thử thách phương pháp, câu hỏi bảo vệ một lập trường có sẵn. Trình bày kết quả đi ngược kỳ vọng của người nghe. Cách phát biểu rằng dữ liệu hiện có không trả lời được câu hỏi được đặt ra.

Cơ chế của `presenting-and-handling-challenge` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Nhượng bộ mọi câu phản biện để tránh xung đột · bảo vệ cả phần không có bằng chứng · trả lời câu hỏi thử thách phương pháp bằng cách nhắc lại kết quả. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Bản Đồ Quyết Định

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L079: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành “Giữ được phần kết luận có bằng chứng qua cả năm câu phản biện, và nhượng bộ đúng câu nêu giới hạn có thật.”. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Case Study Thực Chiến: Presenting and handling challenge

Bài thực hành dùng nhiệm vụ thật của roadmap: Trình bày 10 phút kết quả lesson 61 trước hội đồng đóng vai. Hội đồng chuẩn bị trước năm câu phản biện, trong đó có ít nhất một câu nêu giới hạn có thật.

Trước khi thao tác ở `Presenting and handling challenge`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L079 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Output của `Presenting and handling challenge` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Nhượng bộ mọi câu phản biện để tránh xung đột · bảo vệ cả phần không có bằng chứng · trả lời câu hỏi thử thách phương pháp bằng cách nhắc lại kết quả. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L079 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1 — `population`.** Thiết kế slide cho buổi họp 15 phút. Nói rõ chuỗi suy luận thay vì chỉ nêu kết quả. Ba loại câu hỏi và cách xử lý từng loại: câu hỏi tìm thông tin, câu hỏi thử thách phương pháp, câu hỏi bảo vệ một lập trường có sẵn. Trình bày kết quả đi ngược kỳ vọng của người nghe. Cách phát biểu rằng dữ liệu hiện có không trả lời được câu hỏi được đặt ra.

**Thiết kế.** Probe 1 của L079 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L079.1.** Đối soát `population` bằng đường tính khác implementation chính của `presenting-and-handling-challenge`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2 — `grain`.** Bảo vệ một kết luận bất lợi trước hội đồng, giữ được phần có bằng chứng và nhượng bộ đúng phần chưa đủ bằng chứng.

**Thiết kế.** Probe 2 của L079 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L079.2.** Đối soát `grain` bằng đường tính khác implementation chính của `presenting-and-handling-challenge`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3 — `identity`.** Nhượng bộ mọi câu phản biện để tránh xung đột · bảo vệ cả phần không có bằng chứng · trả lời câu hỏi thử thách phương pháp bằng cách nhắc lại kết quả.

**Thiết kế.** Probe 3 của L079 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L079.3.** Đối soát `identity` bằng đường tính khác implementation chính của `presenting-and-handling-challenge`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4 — `time cutoff`.** Giữ được phần kết luận có bằng chứng qua cả năm câu phản biện, và nhượng bộ đúng câu nêu giới hạn có thật.

**Thiết kế.** Probe 4 của L079 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L079.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `presenting-and-handling-challenge`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5 — `missing versus zero`.** Thiết kế slide cho buổi họp 15 phút. Nói rõ chuỗi suy luận thay vì chỉ nêu kết quả. Ba loại câu hỏi và cách xử lý từng loại: câu hỏi tìm thông tin, câu hỏi thử thách phương pháp, câu hỏi bảo vệ một lập trường có sẵn. Trình bày kết quả đi ngược kỳ vọng của người nghe. Cách phát biểu rằng dữ liệu hiện có không trả lời được câu hỏi được đặt ra.

**Thiết kế.** Probe 5 của L079 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L079.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `presenting-and-handling-challenge`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6 — `duplicate`.** Bảo vệ một kết luận bất lợi trước hội đồng, giữ được phần có bằng chứng và nhượng bộ đúng phần chưa đủ bằng chứng.

**Thiết kế.** Probe 6 của L079 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L079.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `presenting-and-handling-challenge`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7 — `join fan-out`.** Nhượng bộ mọi câu phản biện để tránh xung đột · bảo vệ cả phần không có bằng chứng · trả lời câu hỏi thử thách phương pháp bằng cách nhắc lại kết quả.

**Thiết kế.** Probe 7 của L079 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L079.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `presenting-and-handling-challenge`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8 — `changed definition`.** Giữ được phần kết luận có bằng chứng qua cả năm câu phản biện, và nhượng bộ đúng câu nêu giới hạn có thật.

**Thiết kế.** Probe 8 của L079 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L079.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `presenting-and-handling-challenge`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9 — `independent oracle`.** Thiết kế slide cho buổi họp 15 phút. Nói rõ chuỗi suy luận thay vì chỉ nêu kết quả. Ba loại câu hỏi và cách xử lý từng loại: câu hỏi tìm thông tin, câu hỏi thử thách phương pháp, câu hỏi bảo vệ một lập trường có sẵn. Trình bày kết quả đi ngược kỳ vọng của người nghe. Cách phát biểu rằng dữ liệu hiện có không trả lời được câu hỏi được đặt ra.

**Thiết kế.** Probe 9 của L079 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L079.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `presenting-and-handling-challenge`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10 — `replay`.** Bảo vệ một kết luận bất lợi trước hội đồng, giữ được phần có bằng chứng và nhượng bộ đúng phần chưa đủ bằng chứng.

**Thiết kế.** Probe 10 của L079 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L079.10.** Đối soát `replay` bằng đường tính khác implementation chính của `presenting-and-handling-challenge`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11 — `fresh snapshot`.** Nhượng bộ mọi câu phản biện để tránh xung đột · bảo vệ cả phần không có bằng chứng · trả lời câu hỏi thử thách phương pháp bằng cách nhắc lại kết quả.

**Thiết kế.** Probe 11 của L079 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L079.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `presenting-and-handling-challenge`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12 — `novel scenario`.** Giữ được phần kết luận có bằng chứng qua cả năm câu phản biện, và nhượng bộ đúng câu nêu giới hạn có thật.

**Thiết kế.** Probe 12 của L079 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L079.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `presenting-and-handling-challenge`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L079?

<details><summary>Đáp án</summary>

Bảo vệ một kết luận bất lợi trước hội đồng, giữ được phần có bằng chứng và nhượng bộ đúng phần chưa đủ bằng chứng.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Nhượng bộ mọi câu phản biện để tránh xung đột · bảo vệ cả phần không có bằng chứng · trả lời câu hỏi thử thách phương pháp bằng cách nhắc lại kết quả.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Giữ được phần kết luận có bằng chứng qua cả năm câu phản biện, và nhượng bộ đúng câu nêu giới hạn có thật.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.presenting-and-handling-challenge` đang `proposed`, chưa tính canonical coverage.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-STORYTELLING-WITH-DATA]] — `src.book.knaflic-storytelling-with-data.1e`
2. [[SRC-GOVUK-UNDERSTAND-USER-NEEDS]] — `src.web.govuk-understand-user-needs`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-STORYTELLING-WITH-DATA]] — `src.book.knaflic-storytelling-with-data.1e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Presenting and handling challenge | các mục cơ chế, case và probe | Đã phủ | ngoài objective L079 |
| [[SRC-GOVUK-UNDERSTAND-USER-NEEDS]] — `src.web.govuk-understand-user-needs` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Presenting and handling challenge | các mục cơ chế, case và probe | Đã phủ | ngoài objective L079 |

## Key takeaways
- Bảo vệ một kết luận bất lợi trước hội đồng, giữ được phần có bằng chứng và nhượng bộ đúng phần chưa đủ bằng chứng.
- Giữ được phần kết luận có bằng chứng qua cả năm câu phản biện, và nhượng bộ đúng câu nêu giới hạn có thật.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.
