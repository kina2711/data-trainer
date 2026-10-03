# Phase 4: Data Analyst
# Module 10: Communication and Career
# Lesson 78: Writing an analytical report

## Mục tiêu bài học

**Năng lực cần chứng minh.** Viết một báo cáo mà người quản lý đọc trong 2 phút ra được quyết định, và ba phiên bản của cùng kết quả cho ba nhóm người đọc khác nhau.

**Điều kiện hoàn thành.** Người đọc đóng vai quản lý nêu được quyết định cụ thể sau 2 phút đọc bản một trang, và ba phiên bản nhất quán về kết luận và số liệu.

# Writing an analytical report

**Tóm tắt bản chất:** Cấu trúc báo cáo phân tích: tóm tắt điều hành, câu hỏi, phương pháp, kết quả, khuyến nghị, giả định và giới hạn, phụ lục. Viết tóm tắt điều hành trong năm gạch đầu dòng. Quy ước trình bày số: mức làm tròn theo độ chính xác thực của phép đo, luôn kèm mốc so sánh, tránh phần trăm của phần trăm. Viết phần giới hạn sao cho nó định rõ phạm vi áp dụng thay vì làm mất giá trị kết quả. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Nỗi Đau & Động Lực

L078 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **Writing an analytical report**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Viết một báo cáo mà người quản lý đọc trong 2 phút ra được quyết định, và ba phiên bản của cùng kết quả cho ba nhóm người đọc khác nhau. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Cơ Chế Tác Động

Cấu trúc báo cáo phân tích: tóm tắt điều hành, câu hỏi, phương pháp, kết quả, khuyến nghị, giả định và giới hạn, phụ lục. Viết tóm tắt điều hành trong năm gạch đầu dòng. Quy ước trình bày số: mức làm tròn theo độ chính xác thực của phép đo, luôn kèm mốc so sánh, tránh phần trăm của phần trăm. Viết phần giới hạn sao cho nó định rõ phạm vi áp dụng thay vì làm mất giá trị kết quả.

Cơ chế của `writing-an-analytical-report` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Làm tròn khác nhau giữa ba phiên bản nên số không khớp · viết phần giới hạn chung chung nên người đọc bỏ qua kết luận · đưa phương pháp lên trước kết quả. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Bản Đồ Quyết Định

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L078: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành “Người đọc đóng vai quản lý nêu được quyết định cụ thể sau 2 phút đọc bản một trang, và ba phiên bản nhất quán về kết luận và số liệu.”. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Case Study Thực Chiến: Writing an analytical report

Bài thực hành dùng nhiệm vụ thật của roadmap: Viết báo cáo hoàn chỉnh cho kết quả điều tra ở lesson 61, ba phiên bản: một trang cho giám đốc, năm trang cho đồng nghiệp kỹ thuật, và bản lưu trữ đầy đủ.

Trước khi thao tác ở `Writing an analytical report`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L078 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Output của `Writing an analytical report` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Làm tròn khác nhau giữa ba phiên bản nên số không khớp · viết phần giới hạn chung chung nên người đọc bỏ qua kết luận · đưa phương pháp lên trước kết quả. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L078 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1 — `population`.** Cấu trúc báo cáo phân tích: tóm tắt điều hành, câu hỏi, phương pháp, kết quả, khuyến nghị, giả định và giới hạn, phụ lục. Viết tóm tắt điều hành trong năm gạch đầu dòng. Quy ước trình bày số: mức làm tròn theo độ chính xác thực của phép đo, luôn kèm mốc so sánh, tránh phần trăm của phần trăm. Viết phần giới hạn sao cho nó định rõ phạm vi áp dụng thay vì làm mất giá trị kết quả.

**Thiết kế.** Probe 1 của L078 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L078.1.** Đối soát `population` bằng đường tính khác implementation chính của `writing-an-analytical-report`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2 — `grain`.** Viết một báo cáo mà người quản lý đọc trong 2 phút ra được quyết định, và ba phiên bản của cùng kết quả cho ba nhóm người đọc khác nhau.

**Thiết kế.** Probe 2 của L078 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L078.2.** Đối soát `grain` bằng đường tính khác implementation chính của `writing-an-analytical-report`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3 — `identity`.** Làm tròn khác nhau giữa ba phiên bản nên số không khớp · viết phần giới hạn chung chung nên người đọc bỏ qua kết luận · đưa phương pháp lên trước kết quả.

**Thiết kế.** Probe 3 của L078 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L078.3.** Đối soát `identity` bằng đường tính khác implementation chính của `writing-an-analytical-report`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4 — `time cutoff`.** Người đọc đóng vai quản lý nêu được quyết định cụ thể sau 2 phút đọc bản một trang, và ba phiên bản nhất quán về kết luận và số liệu.

**Thiết kế.** Probe 4 của L078 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L078.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `writing-an-analytical-report`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5 — `missing versus zero`.** Cấu trúc báo cáo phân tích: tóm tắt điều hành, câu hỏi, phương pháp, kết quả, khuyến nghị, giả định và giới hạn, phụ lục. Viết tóm tắt điều hành trong năm gạch đầu dòng. Quy ước trình bày số: mức làm tròn theo độ chính xác thực của phép đo, luôn kèm mốc so sánh, tránh phần trăm của phần trăm. Viết phần giới hạn sao cho nó định rõ phạm vi áp dụng thay vì làm mất giá trị kết quả.

**Thiết kế.** Probe 5 của L078 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L078.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `writing-an-analytical-report`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6 — `duplicate`.** Viết một báo cáo mà người quản lý đọc trong 2 phút ra được quyết định, và ba phiên bản của cùng kết quả cho ba nhóm người đọc khác nhau.

**Thiết kế.** Probe 6 của L078 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L078.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `writing-an-analytical-report`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7 — `join fan-out`.** Làm tròn khác nhau giữa ba phiên bản nên số không khớp · viết phần giới hạn chung chung nên người đọc bỏ qua kết luận · đưa phương pháp lên trước kết quả.

**Thiết kế.** Probe 7 của L078 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L078.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `writing-an-analytical-report`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8 — `changed definition`.** Người đọc đóng vai quản lý nêu được quyết định cụ thể sau 2 phút đọc bản một trang, và ba phiên bản nhất quán về kết luận và số liệu.

**Thiết kế.** Probe 8 của L078 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L078.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `writing-an-analytical-report`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9 — `independent oracle`.** Cấu trúc báo cáo phân tích: tóm tắt điều hành, câu hỏi, phương pháp, kết quả, khuyến nghị, giả định và giới hạn, phụ lục. Viết tóm tắt điều hành trong năm gạch đầu dòng. Quy ước trình bày số: mức làm tròn theo độ chính xác thực của phép đo, luôn kèm mốc so sánh, tránh phần trăm của phần trăm. Viết phần giới hạn sao cho nó định rõ phạm vi áp dụng thay vì làm mất giá trị kết quả.

**Thiết kế.** Probe 9 của L078 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L078.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `writing-an-analytical-report`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10 — `replay`.** Viết một báo cáo mà người quản lý đọc trong 2 phút ra được quyết định, và ba phiên bản của cùng kết quả cho ba nhóm người đọc khác nhau.

**Thiết kế.** Probe 10 của L078 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L078.10.** Đối soát `replay` bằng đường tính khác implementation chính của `writing-an-analytical-report`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11 — `fresh snapshot`.** Làm tròn khác nhau giữa ba phiên bản nên số không khớp · viết phần giới hạn chung chung nên người đọc bỏ qua kết luận · đưa phương pháp lên trước kết quả.

**Thiết kế.** Probe 11 của L078 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L078.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `writing-an-analytical-report`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12 — `novel scenario`.** Người đọc đóng vai quản lý nêu được quyết định cụ thể sau 2 phút đọc bản một trang, và ba phiên bản nhất quán về kết luận và số liệu.

**Thiết kế.** Probe 12 của L078 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L078.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `writing-an-analytical-report`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L078?

<details><summary>Đáp án</summary>

Viết một báo cáo mà người quản lý đọc trong 2 phút ra được quyết định, và ba phiên bản của cùng kết quả cho ba nhóm người đọc khác nhau.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Làm tròn khác nhau giữa ba phiên bản nên số không khớp · viết phần giới hạn chung chung nên người đọc bỏ qua kết luận · đưa phương pháp lên trước kết quả.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Người đọc đóng vai quản lý nêu được quyết định cụ thể sau 2 phút đọc bản một trang, và ba phiên bản nhất quán về kết luận và số liệu.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.writing-an-analytical-report` đang `proposed`, chưa tính canonical coverage.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-STORYTELLING-WITH-DATA]] — `src.book.knaflic-storytelling-with-data.1e`
2. [[SRC-GOVUK-UNDERSTAND-USER-NEEDS]] — `src.web.govuk-understand-user-needs`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-STORYTELLING-WITH-DATA]] — `src.book.knaflic-storytelling-with-data.1e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Writing an analytical report | các mục cơ chế, case và probe | Đã phủ | ngoài objective L078 |
| [[SRC-GOVUK-UNDERSTAND-USER-NEEDS]] — `src.web.govuk-understand-user-needs` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Writing an analytical report | các mục cơ chế, case và probe | Đã phủ | ngoài objective L078 |

## Key takeaways
- Viết một báo cáo mà người quản lý đọc trong 2 phút ra được quyết định, và ba phiên bản của cùng kết quả cho ba nhóm người đọc khác nhau.
- Người đọc đóng vai quản lý nêu được quyết định cụ thể sau 2 phút đọc bản một trang, và ba phiên bản nhất quán về kết luận và số liệu.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.
