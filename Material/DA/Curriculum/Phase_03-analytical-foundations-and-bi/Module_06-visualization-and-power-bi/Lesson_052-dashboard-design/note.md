# Phase 3: Data Analyst
# Module 6: Visualization and Power BI
# Lesson 52: Dashboard design

## Mục tiêu bài học

**Năng lực cần chứng minh.** Phác thảo một dashboard trên giấy trước khi mở công cụ, và biện minh từng thành phần bằng một quyết định cụ thể của người dùng.

**Điều kiện hoàn thành.** Nộp ba bản phác thảo, mỗi thành phần nối được với một quyết định cụ thể từ bản ghi phỏng vấn, và không có thành phần thừa.

# Dashboard design

**Tóm tắt bản chất:** Ba loại dashboard phân theo tần suất xem và loại quyết định: chiến lược xem theo tháng, vận hành xem theo giờ, phân tích xem theo nhu cầu. Cơ chế khiến việc trộn ba loại trong một trang làm dashboard không phục vụ được loại người dùng nào. Quy trình thiết kế đi ngược: từ quyết định người dùng cần ra, tới câu hỏi, tới chỉ số, tới biểu đồ. Bố cục: thứ tự đọc, phân cấp thị giác, mật độ thông tin. Tiêu chí thêm bộ lọc và tương tác. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Nỗi Đau & Động Lực

L052 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **Dashboard design**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Phác thảo một dashboard trên giấy trước khi mở công cụ, và biện minh từng thành phần bằng một quyết định cụ thể của người dùng. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Cơ Chế Tác Động

Ba loại dashboard phân theo tần suất xem và loại quyết định: chiến lược xem theo tháng, vận hành xem theo giờ, phân tích xem theo nhu cầu. Cơ chế khiến việc trộn ba loại trong một trang làm dashboard không phục vụ được loại người dùng nào. Quy trình thiết kế đi ngược: từ quyết định người dùng cần ra, tới câu hỏi, tới chỉ số, tới biểu đồ. Bố cục: thứ tự đọc, phân cấp thị giác, mật độ thông tin. Tiêu chí thêm bộ lọc và tương tác.

Cơ chế của `dashboard-design` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Bắt đầu từ dữ liệu có sẵn thay vì từ quyết định · trộn ba loại dashboard trong một trang · thêm bộ lọc không ai yêu cầu. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Bản Đồ Quyết Định

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L052: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành “Nộp ba bản phác thảo, mỗi thành phần nối được với một quyết định cụ thể từ bản ghi phỏng vấn, và không có thành phần thừa.”. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Case Study Thực Chiến: Dashboard design

Bài thực hành dùng nhiệm vụ thật của roadmap: Phỏng vấn ba người dùng do bạn học đóng vai, mỗi người thuộc một loại dashboard khác nhau. Phác thảo ba dashboard trên giấy, mỗi thành phần ghi rõ phục vụ quyết định nào.

Trước khi thao tác ở `Dashboard design`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L052 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Output của `Dashboard design` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Bắt đầu từ dữ liệu có sẵn thay vì từ quyết định · trộn ba loại dashboard trong một trang · thêm bộ lọc không ai yêu cầu. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L052 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1 — `population`.** Ba loại dashboard phân theo tần suất xem và loại quyết định: chiến lược xem theo tháng, vận hành xem theo giờ, phân tích xem theo nhu cầu. Cơ chế khiến việc trộn ba loại trong một trang làm dashboard không phục vụ được loại người dùng nào. Quy trình thiết kế đi ngược: từ quyết định người dùng cần ra, tới câu hỏi, tới chỉ số, tới biểu đồ. Bố cục: thứ tự đọc, phân cấp thị giác, mật độ thông tin. Tiêu chí thêm bộ lọc và tương tác.

**Thiết kế.** Probe 1 của L052 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L052.1.** Đối soát `population` bằng đường tính khác implementation chính của `dashboard-design`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2 — `grain`.** Phác thảo một dashboard trên giấy trước khi mở công cụ, và biện minh từng thành phần bằng một quyết định cụ thể của người dùng.

**Thiết kế.** Probe 2 của L052 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L052.2.** Đối soát `grain` bằng đường tính khác implementation chính của `dashboard-design`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3 — `identity`.** Bắt đầu từ dữ liệu có sẵn thay vì từ quyết định · trộn ba loại dashboard trong một trang · thêm bộ lọc không ai yêu cầu.

**Thiết kế.** Probe 3 của L052 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L052.3.** Đối soát `identity` bằng đường tính khác implementation chính của `dashboard-design`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4 — `time cutoff`.** Nộp ba bản phác thảo, mỗi thành phần nối được với một quyết định cụ thể từ bản ghi phỏng vấn, và không có thành phần thừa.

**Thiết kế.** Probe 4 của L052 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L052.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `dashboard-design`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5 — `missing versus zero`.** Ba loại dashboard phân theo tần suất xem và loại quyết định: chiến lược xem theo tháng, vận hành xem theo giờ, phân tích xem theo nhu cầu. Cơ chế khiến việc trộn ba loại trong một trang làm dashboard không phục vụ được loại người dùng nào. Quy trình thiết kế đi ngược: từ quyết định người dùng cần ra, tới câu hỏi, tới chỉ số, tới biểu đồ. Bố cục: thứ tự đọc, phân cấp thị giác, mật độ thông tin. Tiêu chí thêm bộ lọc và tương tác.

**Thiết kế.** Probe 5 của L052 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L052.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `dashboard-design`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6 — `duplicate`.** Phác thảo một dashboard trên giấy trước khi mở công cụ, và biện minh từng thành phần bằng một quyết định cụ thể của người dùng.

**Thiết kế.** Probe 6 của L052 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L052.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `dashboard-design`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7 — `join fan-out`.** Bắt đầu từ dữ liệu có sẵn thay vì từ quyết định · trộn ba loại dashboard trong một trang · thêm bộ lọc không ai yêu cầu.

**Thiết kế.** Probe 7 của L052 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L052.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `dashboard-design`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8 — `changed definition`.** Nộp ba bản phác thảo, mỗi thành phần nối được với một quyết định cụ thể từ bản ghi phỏng vấn, và không có thành phần thừa.

**Thiết kế.** Probe 8 của L052 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L052.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `dashboard-design`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9 — `independent oracle`.** Ba loại dashboard phân theo tần suất xem và loại quyết định: chiến lược xem theo tháng, vận hành xem theo giờ, phân tích xem theo nhu cầu. Cơ chế khiến việc trộn ba loại trong một trang làm dashboard không phục vụ được loại người dùng nào. Quy trình thiết kế đi ngược: từ quyết định người dùng cần ra, tới câu hỏi, tới chỉ số, tới biểu đồ. Bố cục: thứ tự đọc, phân cấp thị giác, mật độ thông tin. Tiêu chí thêm bộ lọc và tương tác.

**Thiết kế.** Probe 9 của L052 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L052.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `dashboard-design`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10 — `replay`.** Phác thảo một dashboard trên giấy trước khi mở công cụ, và biện minh từng thành phần bằng một quyết định cụ thể của người dùng.

**Thiết kế.** Probe 10 của L052 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L052.10.** Đối soát `replay` bằng đường tính khác implementation chính của `dashboard-design`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11 — `fresh snapshot`.** Bắt đầu từ dữ liệu có sẵn thay vì từ quyết định · trộn ba loại dashboard trong một trang · thêm bộ lọc không ai yêu cầu.

**Thiết kế.** Probe 11 của L052 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L052.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `dashboard-design`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12 — `novel scenario`.** Nộp ba bản phác thảo, mỗi thành phần nối được với một quyết định cụ thể từ bản ghi phỏng vấn, và không có thành phần thừa.

**Thiết kế.** Probe 12 của L052 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L052.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `dashboard-design`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L052?

<details><summary>Đáp án</summary>

Phác thảo một dashboard trên giấy trước khi mở công cụ, và biện minh từng thành phần bằng một quyết định cụ thể của người dùng.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Bắt đầu từ dữ liệu có sẵn thay vì từ quyết định · trộn ba loại dashboard trong một trang · thêm bộ lọc không ai yêu cầu.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Nộp ba bản phác thảo, mỗi thành phần nối được với một quyết định cụ thể từ bản ghi phỏng vấn, và không có thành phần thừa.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.dashboard-design` đang `proposed`, chưa tính canonical coverage.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-STORYTELLING-WITH-DATA]] — `src.book.knaflic-storytelling-with-data.1e`
2. [[SRC-DEFINITIVE-GUIDE-DAX-3E]] — `src.book.ferrari-russo-definitive-guide-dax.3e`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-STORYTELLING-WITH-DATA]] — `src.book.knaflic-storytelling-with-data.1e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Dashboard design | các mục cơ chế, case và probe | Đã phủ | ngoài objective L052 |
| [[SRC-DEFINITIVE-GUIDE-DAX-3E]] — `src.book.ferrari-russo-definitive-guide-dax.3e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Dashboard design | các mục cơ chế, case và probe | Đã phủ | ngoài objective L052 |

## Key takeaways
- Phác thảo một dashboard trên giấy trước khi mở công cụ, và biện minh từng thành phần bằng một quyết định cụ thể của người dùng.
- Nộp ba bản phác thảo, mỗi thành phần nối được với một quyết định cụ thể từ bản ghi phỏng vấn, và không có thành phần thừa.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.
