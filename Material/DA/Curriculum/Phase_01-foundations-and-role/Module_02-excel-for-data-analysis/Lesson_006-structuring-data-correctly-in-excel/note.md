# Phase 1: Data Analyst
# Module 2: Excel for Data Analysis
# Lesson 6: Structuring data correctly in Excel

## Mục tiêu bài học

**Năng lực cần chứng minh.** Chuyển một tệp Excel có ô gộp, tiêu đề nhiều tầng và số lưu dạng văn bản thành một Table ở dạng dữ liệu dài, và chứng minh kết quả bằng một PivotTable chạy được.

**Điều kiện hoàn thành.** Tệp kết quả tạo được PivotTable không lỗi, và tổng doanh thu khớp tuyệt đối với tổng tính từ tệp gốc.

# Structuring data correctly in Excel

**Tóm tắt bản chất:** Phân biệt bảng dữ liệu và bảng báo cáo. Bốn quy tắc của dạng dữ liệu dài: một dòng một bản ghi, một cột một thuộc tính, không ô gộp, không dòng trống ngắt khối. Định dạng Table và ba hệ quả kỹ thuật của nó: vùng tự mở rộng, tham chiếu theo tên cột, nguồn hợp lệ cho PivotTable. Kiểu dữ liệu trong ô và cơ chế suy đoán kiểu tự động của Excel, gồm các trường hợp suy đoán sai không phát tín hiệu. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Nỗi Đau & Động Lực

L006 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **Structuring data correctly in Excel**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Chuyển một tệp Excel có ô gộp, tiêu đề nhiều tầng và số lưu dạng văn bản thành một Table ở dạng dữ liệu dài, và chứng minh kết quả bằng một PivotTable chạy được. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Cơ Chế Tác Động

Phân biệt bảng dữ liệu và bảng báo cáo. Bốn quy tắc của dạng dữ liệu dài: một dòng một bản ghi, một cột một thuộc tính, không ô gộp, không dòng trống ngắt khối. Định dạng Table và ba hệ quả kỹ thuật của nó: vùng tự mở rộng, tham chiếu theo tên cột, nguồn hợp lệ cho PivotTable. Kiểu dữ liệu trong ô và cơ chế suy đoán kiểu tự động của Excel, gồm các trường hợp suy đoán sai không phát tín hiệu.

Cơ chế của `structuring-data-correctly-in-excel` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Gộp ô để trình bày rồi mất khả năng dùng hàm · để số điện thoại ở kiểu số và mất chữ số 0 đầu · trộn dữ liệu với ghi chú trong cùng một cột. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Bản Đồ Quyết Định

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L006: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành “Tệp kết quả tạo được PivotTable không lỗi, và tổng doanh thu khớp tuyệt đối với tổng tính từ tệp gốc.”. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Case Study Thực Chiến: Structuring data correctly in Excel

Bài thực hành dùng nhiệm vụ thật của roadmap: Cho một tệp báo cáo bán hàng có ô gộp, tiêu đề hai tầng và cột số lưu dạng văn bản. Chuyển thành một Table sạch. Kiểm chứng bằng một PivotTable chạy được và bằng phép đối chiếu tổng với tệp gốc.

Trước khi thao tác ở `Structuring data correctly in Excel`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L006 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Output của `Structuring data correctly in Excel` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Gộp ô để trình bày rồi mất khả năng dùng hàm · để số điện thoại ở kiểu số và mất chữ số 0 đầu · trộn dữ liệu với ghi chú trong cùng một cột. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L006 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1 — `population`.** Phân biệt bảng dữ liệu và bảng báo cáo. Bốn quy tắc của dạng dữ liệu dài: một dòng một bản ghi, một cột một thuộc tính, không ô gộp, không dòng trống ngắt khối. Định dạng Table và ba hệ quả kỹ thuật của nó: vùng tự mở rộng, tham chiếu theo tên cột, nguồn hợp lệ cho PivotTable. Kiểu dữ liệu trong ô và cơ chế suy đoán kiểu tự động của Excel, gồm các trường hợp suy đoán sai không phát tín hiệu.

**Thiết kế.** Probe 1 của L006 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L006.1.** Đối soát `population` bằng đường tính khác implementation chính của `structuring-data-correctly-in-excel`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2 — `grain`.** Chuyển một tệp Excel có ô gộp, tiêu đề nhiều tầng và số lưu dạng văn bản thành một Table ở dạng dữ liệu dài, và chứng minh kết quả bằng một PivotTable chạy được.

**Thiết kế.** Probe 2 của L006 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L006.2.** Đối soát `grain` bằng đường tính khác implementation chính của `structuring-data-correctly-in-excel`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3 — `identity`.** Gộp ô để trình bày rồi mất khả năng dùng hàm · để số điện thoại ở kiểu số và mất chữ số 0 đầu · trộn dữ liệu với ghi chú trong cùng một cột.

**Thiết kế.** Probe 3 của L006 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L006.3.** Đối soát `identity` bằng đường tính khác implementation chính của `structuring-data-correctly-in-excel`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4 — `time cutoff`.** Tệp kết quả tạo được PivotTable không lỗi, và tổng doanh thu khớp tuyệt đối với tổng tính từ tệp gốc.

**Thiết kế.** Probe 4 của L006 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L006.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `structuring-data-correctly-in-excel`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5 — `missing versus zero`.** Phân biệt bảng dữ liệu và bảng báo cáo. Bốn quy tắc của dạng dữ liệu dài: một dòng một bản ghi, một cột một thuộc tính, không ô gộp, không dòng trống ngắt khối. Định dạng Table và ba hệ quả kỹ thuật của nó: vùng tự mở rộng, tham chiếu theo tên cột, nguồn hợp lệ cho PivotTable. Kiểu dữ liệu trong ô và cơ chế suy đoán kiểu tự động của Excel, gồm các trường hợp suy đoán sai không phát tín hiệu.

**Thiết kế.** Probe 5 của L006 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L006.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `structuring-data-correctly-in-excel`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6 — `duplicate`.** Chuyển một tệp Excel có ô gộp, tiêu đề nhiều tầng và số lưu dạng văn bản thành một Table ở dạng dữ liệu dài, và chứng minh kết quả bằng một PivotTable chạy được.

**Thiết kế.** Probe 6 của L006 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L006.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `structuring-data-correctly-in-excel`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7 — `join fan-out`.** Gộp ô để trình bày rồi mất khả năng dùng hàm · để số điện thoại ở kiểu số và mất chữ số 0 đầu · trộn dữ liệu với ghi chú trong cùng một cột.

**Thiết kế.** Probe 7 của L006 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L006.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `structuring-data-correctly-in-excel`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8 — `changed definition`.** Tệp kết quả tạo được PivotTable không lỗi, và tổng doanh thu khớp tuyệt đối với tổng tính từ tệp gốc.

**Thiết kế.** Probe 8 của L006 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L006.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `structuring-data-correctly-in-excel`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9 — `independent oracle`.** Phân biệt bảng dữ liệu và bảng báo cáo. Bốn quy tắc của dạng dữ liệu dài: một dòng một bản ghi, một cột một thuộc tính, không ô gộp, không dòng trống ngắt khối. Định dạng Table và ba hệ quả kỹ thuật của nó: vùng tự mở rộng, tham chiếu theo tên cột, nguồn hợp lệ cho PivotTable. Kiểu dữ liệu trong ô và cơ chế suy đoán kiểu tự động của Excel, gồm các trường hợp suy đoán sai không phát tín hiệu.

**Thiết kế.** Probe 9 của L006 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L006.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `structuring-data-correctly-in-excel`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10 — `replay`.** Chuyển một tệp Excel có ô gộp, tiêu đề nhiều tầng và số lưu dạng văn bản thành một Table ở dạng dữ liệu dài, và chứng minh kết quả bằng một PivotTable chạy được.

**Thiết kế.** Probe 10 của L006 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L006.10.** Đối soát `replay` bằng đường tính khác implementation chính của `structuring-data-correctly-in-excel`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11 — `fresh snapshot`.** Gộp ô để trình bày rồi mất khả năng dùng hàm · để số điện thoại ở kiểu số và mất chữ số 0 đầu · trộn dữ liệu với ghi chú trong cùng một cột.

**Thiết kế.** Probe 11 của L006 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L006.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `structuring-data-correctly-in-excel`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12 — `novel scenario`.** Tệp kết quả tạo được PivotTable không lỗi, và tổng doanh thu khớp tuyệt đối với tổng tính từ tệp gốc.

**Thiết kế.** Probe 12 của L006 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L006.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `structuring-data-correctly-in-excel`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L006?

<details><summary>Đáp án</summary>

Chuyển một tệp Excel có ô gộp, tiêu đề nhiều tầng và số lưu dạng văn bản thành một Table ở dạng dữ liệu dài, và chứng minh kết quả bằng một PivotTable chạy được.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Gộp ô để trình bày rồi mất khả năng dùng hàm · để số điện thoại ở kiểu số và mất chữ số 0 đầu · trộn dữ liệu với ghi chú trong cùng một cột.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Tệp kết quả tạo được PivotTable không lỗi, và tổng doanh thu khớp tuyệt đối với tổng tính từ tệp gốc.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.structuring-data-correctly-in-excel` đang `proposed`, chưa tính canonical coverage.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-GOVUK-DATA-ANALYTICS-TOOLS-GUIDANCE]] — `src.web.govuk-data-analytics-tools-guidance`
2. [[SRC-KIMBALL-ROSS-DW-TOOLKIT-3E]] — `src.book.kimball-ross-data-warehouse-toolkit.3e`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-GOVUK-DATA-ANALYTICS-TOOLS-GUIDANCE]] — `src.web.govuk-data-analytics-tools-guidance` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Structuring data correctly in Excel | các mục cơ chế, case và probe | Đã phủ | ngoài objective L006 |
| [[SRC-KIMBALL-ROSS-DW-TOOLKIT-3E]] — `src.book.kimball-ross-data-warehouse-toolkit.3e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Structuring data correctly in Excel | các mục cơ chế, case và probe | Đã phủ | ngoài objective L006 |

## Key takeaways
- Chuyển một tệp Excel có ô gộp, tiêu đề nhiều tầng và số lưu dạng văn bản thành một Table ở dạng dữ liệu dài, và chứng minh kết quả bằng một PivotTable chạy được.
- Tệp kết quả tạo được PivotTable không lỗi, và tổng doanh thu khớp tuyệt đối với tổng tính từ tệp gốc.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.
