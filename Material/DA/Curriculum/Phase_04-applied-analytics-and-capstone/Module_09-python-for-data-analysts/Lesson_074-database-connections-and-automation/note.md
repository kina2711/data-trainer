# Phase 4: Data Analyst
# Module 9: Python for Data Analysts
# Lesson 74: Database connections and automation

## Mục tiêu bài học

**Năng lực cần chứng minh.** Viết script kéo dữ liệu, biến đổi và xuất báo cáo, chạy được bằng một lệnh trên máy chưa cấu hình sẵn.

**Điều kiện hoàn thành.** Script chạy bằng một lệnh và xuất đúng tệp Excel 4 sheet, và quét mã không tìm thấy thông tin xác thực nào.

# Database connections and automation

**Tóm tắt bản chất:** Kết nối cơ sở dữ liệu từ Python: chuỗi kết nối, con trỏ, đóng tài nguyên đúng cách. Truy vấn tham số hoá và cơ chế tấn công chèn SQL khi ghép chuỗi. Quản lý bí mật: biến môi trường, tệp `.env`, và nguyên tắc không ghi thông tin xác thực trong mã nguồn. Quy tắc phân công tính toán: đẩy phép lọc và phép gộp xuống cơ sở dữ liệu, kéo về lượng dữ liệu nhỏ nhất đủ dùng. Xuất kết quả ra tệp Excel nhiều sheet. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Nỗi Đau & Động Lực

L074 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **Database connections and automation**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Viết script kéo dữ liệu, biến đổi và xuất báo cáo, chạy được bằng một lệnh trên máy chưa cấu hình sẵn. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Cơ Chế Tác Động

Kết nối cơ sở dữ liệu từ Python: chuỗi kết nối, con trỏ, đóng tài nguyên đúng cách. Truy vấn tham số hoá và cơ chế tấn công chèn SQL khi ghép chuỗi. Quản lý bí mật: biến môi trường, tệp `.env`, và nguyên tắc không ghi thông tin xác thực trong mã nguồn. Quy tắc phân công tính toán: đẩy phép lọc và phép gộp xuống cơ sở dữ liệu, kéo về lượng dữ liệu nhỏ nhất đủ dùng. Xuất kết quả ra tệp Excel nhiều sheet.

Cơ chế của `database-connections-and-automation` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Ghép tham số vào chuỗi truy vấn · để chuỗi kết nối trong mã rồi đưa lên kho mã · kéo toàn bộ bảng về rồi lọc trong Python. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Bản Đồ Quyết Định

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L074: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành “Script chạy bằng một lệnh và xuất đúng tệp Excel 4 sheet, và quét mã không tìm thấy thông tin xác thực nào.”. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Case Study Thực Chiến: Database connections and automation

Bài thực hành dùng nhiệm vụ thật của roadmap: Viết script tự động: kết nối `DS2`, tính bộ chỉ số tháng, xuất tệp Excel có 4 sheet kèm biểu đồ. Chạy bằng một lệnh.

Trước khi thao tác ở `Database connections and automation`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L074 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Output của `Database connections and automation` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Ghép tham số vào chuỗi truy vấn · để chuỗi kết nối trong mã rồi đưa lên kho mã · kéo toàn bộ bảng về rồi lọc trong Python. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L074 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1 — `population`.** Kết nối cơ sở dữ liệu từ Python: chuỗi kết nối, con trỏ, đóng tài nguyên đúng cách. Truy vấn tham số hoá và cơ chế tấn công chèn SQL khi ghép chuỗi. Quản lý bí mật: biến môi trường, tệp `.env`, và nguyên tắc không ghi thông tin xác thực trong mã nguồn. Quy tắc phân công tính toán: đẩy phép lọc và phép gộp xuống cơ sở dữ liệu, kéo về lượng dữ liệu nhỏ nhất đủ dùng. Xuất kết quả ra tệp Excel nhiều sheet.

**Thiết kế.** Probe 1 của L074 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L074.1.** Đối soát `population` bằng đường tính khác implementation chính của `database-connections-and-automation`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2 — `grain`.** Viết script kéo dữ liệu, biến đổi và xuất báo cáo, chạy được bằng một lệnh trên máy chưa cấu hình sẵn.

**Thiết kế.** Probe 2 của L074 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L074.2.** Đối soát `grain` bằng đường tính khác implementation chính của `database-connections-and-automation`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3 — `identity`.** Ghép tham số vào chuỗi truy vấn · để chuỗi kết nối trong mã rồi đưa lên kho mã · kéo toàn bộ bảng về rồi lọc trong Python.

**Thiết kế.** Probe 3 của L074 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L074.3.** Đối soát `identity` bằng đường tính khác implementation chính của `database-connections-and-automation`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4 — `time cutoff`.** Script chạy bằng một lệnh và xuất đúng tệp Excel 4 sheet, và quét mã không tìm thấy thông tin xác thực nào.

**Thiết kế.** Probe 4 của L074 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L074.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `database-connections-and-automation`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5 — `missing versus zero`.** Kết nối cơ sở dữ liệu từ Python: chuỗi kết nối, con trỏ, đóng tài nguyên đúng cách. Truy vấn tham số hoá và cơ chế tấn công chèn SQL khi ghép chuỗi. Quản lý bí mật: biến môi trường, tệp `.env`, và nguyên tắc không ghi thông tin xác thực trong mã nguồn. Quy tắc phân công tính toán: đẩy phép lọc và phép gộp xuống cơ sở dữ liệu, kéo về lượng dữ liệu nhỏ nhất đủ dùng. Xuất kết quả ra tệp Excel nhiều sheet.

**Thiết kế.** Probe 5 của L074 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L074.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `database-connections-and-automation`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6 — `duplicate`.** Viết script kéo dữ liệu, biến đổi và xuất báo cáo, chạy được bằng một lệnh trên máy chưa cấu hình sẵn.

**Thiết kế.** Probe 6 của L074 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L074.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `database-connections-and-automation`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7 — `join fan-out`.** Ghép tham số vào chuỗi truy vấn · để chuỗi kết nối trong mã rồi đưa lên kho mã · kéo toàn bộ bảng về rồi lọc trong Python.

**Thiết kế.** Probe 7 của L074 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L074.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `database-connections-and-automation`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8 — `changed definition`.** Script chạy bằng một lệnh và xuất đúng tệp Excel 4 sheet, và quét mã không tìm thấy thông tin xác thực nào.

**Thiết kế.** Probe 8 của L074 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L074.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `database-connections-and-automation`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9 — `independent oracle`.** Kết nối cơ sở dữ liệu từ Python: chuỗi kết nối, con trỏ, đóng tài nguyên đúng cách. Truy vấn tham số hoá và cơ chế tấn công chèn SQL khi ghép chuỗi. Quản lý bí mật: biến môi trường, tệp `.env`, và nguyên tắc không ghi thông tin xác thực trong mã nguồn. Quy tắc phân công tính toán: đẩy phép lọc và phép gộp xuống cơ sở dữ liệu, kéo về lượng dữ liệu nhỏ nhất đủ dùng. Xuất kết quả ra tệp Excel nhiều sheet.

**Thiết kế.** Probe 9 của L074 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L074.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `database-connections-and-automation`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10 — `replay`.** Viết script kéo dữ liệu, biến đổi và xuất báo cáo, chạy được bằng một lệnh trên máy chưa cấu hình sẵn.

**Thiết kế.** Probe 10 của L074 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L074.10.** Đối soát `replay` bằng đường tính khác implementation chính của `database-connections-and-automation`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11 — `fresh snapshot`.** Ghép tham số vào chuỗi truy vấn · để chuỗi kết nối trong mã rồi đưa lên kho mã · kéo toàn bộ bảng về rồi lọc trong Python.

**Thiết kế.** Probe 11 của L074 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L074.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `database-connections-and-automation`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12 — `novel scenario`.** Script chạy bằng một lệnh và xuất đúng tệp Excel 4 sheet, và quét mã không tìm thấy thông tin xác thực nào.

**Thiết kế.** Probe 12 của L074 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L074.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `database-connections-and-automation`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L074?

<details><summary>Đáp án</summary>

Viết script kéo dữ liệu, biến đổi và xuất báo cáo, chạy được bằng một lệnh trên máy chưa cấu hình sẵn.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Ghép tham số vào chuỗi truy vấn · để chuỗi kết nối trong mã rồi đưa lên kho mã · kéo toàn bộ bảng về rồi lọc trong Python.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Script chạy bằng một lệnh và xuất đúng tệp Excel 4 sheet, và quét mã không tìm thấy thông tin xác thực nào.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.database-connections-and-automation` đang `proposed`, chưa tính canonical coverage.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-PYTHON-314-LANGUAGE-REFERENCE]] — `src.docs.python-3.14-language-reference`
2. [[SRC-PYTHON-314-STDLIB-RUNTIME]] — `src.docs.python-3.14-stdlib-runtime`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-PYTHON-314-LANGUAGE-REFERENCE]] — `src.docs.python-3.14-language-reference` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Database connections and automation | các mục cơ chế, case và probe | Đã phủ | ngoài objective L074 |
| [[SRC-PYTHON-314-STDLIB-RUNTIME]] — `src.docs.python-3.14-stdlib-runtime` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Database connections and automation | các mục cơ chế, case và probe | Đã phủ | ngoài objective L074 |

## Key takeaways
- Viết script kéo dữ liệu, biến đổi và xuất báo cáo, chạy được bằng một lệnh trên máy chưa cấu hình sẵn.
- Script chạy bằng một lệnh và xuất đúng tệp Excel 4 sheet, và quét mã không tìm thấy thông tin xác thực nào.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.
