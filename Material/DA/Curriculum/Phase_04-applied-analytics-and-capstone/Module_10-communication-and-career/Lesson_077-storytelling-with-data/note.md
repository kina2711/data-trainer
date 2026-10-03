# Phase 4: Data Analyst
# Module 10: Communication and Career
# Lesson 77: Storytelling with data

## Mục tiêu bài học

**Năng lực cần chứng minh.** Sắp xếp lại một báo cáo viết theo trình tự thời gian thành cấu trúc kim tự tháp và rút xuống một trang, giữ nguyên kết luận và bằng chứng.

**Điều kiện hoàn thành.** Ba bản viết lại đều trong một trang, và người đọc trong 2 phút nêu lại đúng kết luận của cả ba.

# Storytelling with data

**Tóm tắt bản chất:** Cấu trúc kim tự tháp: kết luận trước, lý do sau, chi tiết cuối. Lý do cấu trúc này ngược với trình tự thực hiện công việc, và vì sao vẫn dùng nó khi trình bày. Ba thành phần của một trình bày dựa trên dữ liệu: bối cảnh, mâu thuẫn, giải pháp. Nguyên tắc một thông điệp chính cho mỗi báo cáo. Xác định điều gì làm người nhận thay đổi quyết định. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Nỗi Đau & Động Lực

L077 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **Storytelling with data**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Sắp xếp lại một báo cáo viết theo trình tự thời gian thành cấu trúc kim tự tháp và rút xuống một trang, giữ nguyên kết luận và bằng chứng. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Cơ Chế Tác Động

Cấu trúc kim tự tháp: kết luận trước, lý do sau, chi tiết cuối. Lý do cấu trúc này ngược với trình tự thực hiện công việc, và vì sao vẫn dùng nó khi trình bày. Ba thành phần của một trình bày dựa trên dữ liệu: bối cảnh, mâu thuẫn, giải pháp. Nguyên tắc một thông điệp chính cho mỗi báo cáo. Xác định điều gì làm người nhận thay đổi quyết định.

Cơ chế của `storytelling-with-data` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Đặt kết luận ở cuối theo thói quen viết báo cáo học thuật · rút gọn bằng cách bỏ bằng chứng thay vì bỏ chi tiết quy trình · đưa nhiều thông điệp chính vào một báo cáo. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Bản Đồ Quyết Định

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L077: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành “Ba bản viết lại đều trong một trang, và người đọc trong 2 phút nêu lại đúng kết luận của cả ba.”. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Case Study Thực Chiến: Storytelling with data

Bài thực hành dùng nhiệm vụ thật của roadmap: Nhận ba báo cáo viết theo trình tự thời gian làm việc. Viết lại theo cấu trúc kim tự tháp, rút mỗi bản xuống một trang. Thử với bạn học đọc trong 2 phút.

Trước khi thao tác ở `Storytelling with data`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L077 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Output của `Storytelling with data` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Đặt kết luận ở cuối theo thói quen viết báo cáo học thuật · rút gọn bằng cách bỏ bằng chứng thay vì bỏ chi tiết quy trình · đưa nhiều thông điệp chính vào một báo cáo. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L077 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1 — `population`.** Cấu trúc kim tự tháp: kết luận trước, lý do sau, chi tiết cuối. Lý do cấu trúc này ngược với trình tự thực hiện công việc, và vì sao vẫn dùng nó khi trình bày. Ba thành phần của một trình bày dựa trên dữ liệu: bối cảnh, mâu thuẫn, giải pháp. Nguyên tắc một thông điệp chính cho mỗi báo cáo. Xác định điều gì làm người nhận thay đổi quyết định.

**Thiết kế.** Probe 1 của L077 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L077.1.** Đối soát `population` bằng đường tính khác implementation chính của `storytelling-with-data`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2 — `grain`.** Sắp xếp lại một báo cáo viết theo trình tự thời gian thành cấu trúc kim tự tháp và rút xuống một trang, giữ nguyên kết luận và bằng chứng.

**Thiết kế.** Probe 2 của L077 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L077.2.** Đối soát `grain` bằng đường tính khác implementation chính của `storytelling-with-data`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3 — `identity`.** Đặt kết luận ở cuối theo thói quen viết báo cáo học thuật · rút gọn bằng cách bỏ bằng chứng thay vì bỏ chi tiết quy trình · đưa nhiều thông điệp chính vào một báo cáo.

**Thiết kế.** Probe 3 của L077 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L077.3.** Đối soát `identity` bằng đường tính khác implementation chính của `storytelling-with-data`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4 — `time cutoff`.** Ba bản viết lại đều trong một trang, và người đọc trong 2 phút nêu lại đúng kết luận của cả ba.

**Thiết kế.** Probe 4 của L077 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L077.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `storytelling-with-data`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5 — `missing versus zero`.** Cấu trúc kim tự tháp: kết luận trước, lý do sau, chi tiết cuối. Lý do cấu trúc này ngược với trình tự thực hiện công việc, và vì sao vẫn dùng nó khi trình bày. Ba thành phần của một trình bày dựa trên dữ liệu: bối cảnh, mâu thuẫn, giải pháp. Nguyên tắc một thông điệp chính cho mỗi báo cáo. Xác định điều gì làm người nhận thay đổi quyết định.

**Thiết kế.** Probe 5 của L077 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L077.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `storytelling-with-data`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6 — `duplicate`.** Sắp xếp lại một báo cáo viết theo trình tự thời gian thành cấu trúc kim tự tháp và rút xuống một trang, giữ nguyên kết luận và bằng chứng.

**Thiết kế.** Probe 6 của L077 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L077.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `storytelling-with-data`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7 — `join fan-out`.** Đặt kết luận ở cuối theo thói quen viết báo cáo học thuật · rút gọn bằng cách bỏ bằng chứng thay vì bỏ chi tiết quy trình · đưa nhiều thông điệp chính vào một báo cáo.

**Thiết kế.** Probe 7 của L077 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L077.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `storytelling-with-data`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8 — `changed definition`.** Ba bản viết lại đều trong một trang, và người đọc trong 2 phút nêu lại đúng kết luận của cả ba.

**Thiết kế.** Probe 8 của L077 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L077.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `storytelling-with-data`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9 — `independent oracle`.** Cấu trúc kim tự tháp: kết luận trước, lý do sau, chi tiết cuối. Lý do cấu trúc này ngược với trình tự thực hiện công việc, và vì sao vẫn dùng nó khi trình bày. Ba thành phần của một trình bày dựa trên dữ liệu: bối cảnh, mâu thuẫn, giải pháp. Nguyên tắc một thông điệp chính cho mỗi báo cáo. Xác định điều gì làm người nhận thay đổi quyết định.

**Thiết kế.** Probe 9 của L077 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L077.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `storytelling-with-data`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10 — `replay`.** Sắp xếp lại một báo cáo viết theo trình tự thời gian thành cấu trúc kim tự tháp và rút xuống một trang, giữ nguyên kết luận và bằng chứng.

**Thiết kế.** Probe 10 của L077 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L077.10.** Đối soát `replay` bằng đường tính khác implementation chính của `storytelling-with-data`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11 — `fresh snapshot`.** Đặt kết luận ở cuối theo thói quen viết báo cáo học thuật · rút gọn bằng cách bỏ bằng chứng thay vì bỏ chi tiết quy trình · đưa nhiều thông điệp chính vào một báo cáo.

**Thiết kế.** Probe 11 của L077 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L077.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `storytelling-with-data`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12 — `novel scenario`.** Ba bản viết lại đều trong một trang, và người đọc trong 2 phút nêu lại đúng kết luận của cả ba.

**Thiết kế.** Probe 12 của L077 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L077.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `storytelling-with-data`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L077?

<details><summary>Đáp án</summary>

Sắp xếp lại một báo cáo viết theo trình tự thời gian thành cấu trúc kim tự tháp và rút xuống một trang, giữ nguyên kết luận và bằng chứng.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Đặt kết luận ở cuối theo thói quen viết báo cáo học thuật · rút gọn bằng cách bỏ bằng chứng thay vì bỏ chi tiết quy trình · đưa nhiều thông điệp chính vào một báo cáo.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Ba bản viết lại đều trong một trang, và người đọc trong 2 phút nêu lại đúng kết luận của cả ba.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.storytelling-with-data` đang `proposed`, chưa tính canonical coverage.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-STORYTELLING-WITH-DATA]] — `src.book.knaflic-storytelling-with-data.1e`
2. [[SRC-GOVUK-UNDERSTAND-USER-NEEDS]] — `src.web.govuk-understand-user-needs`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-STORYTELLING-WITH-DATA]] — `src.book.knaflic-storytelling-with-data.1e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Storytelling with data | các mục cơ chế, case và probe | Đã phủ | ngoài objective L077 |
| [[SRC-GOVUK-UNDERSTAND-USER-NEEDS]] — `src.web.govuk-understand-user-needs` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Storytelling with data | các mục cơ chế, case và probe | Đã phủ | ngoài objective L077 |

## Key takeaways
- Sắp xếp lại một báo cáo viết theo trình tự thời gian thành cấu trúc kim tự tháp và rút xuống một trang, giữ nguyên kết luận và bằng chứng.
- Ba bản viết lại đều trong một trang, và người đọc trong 2 phút nêu lại đúng kết luận của cả ba.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.
