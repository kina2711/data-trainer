# Phase 2: Data Analyst
# Module 3: SQL and Databases
# Lesson 28: Set operations and data quality in SQL

## Mục tiêu bài học

**Năng lực cần chứng minh.** Lập báo cáo chất lượng dữ liệu định lượng trên sáu chiều cho một bảng chưa từng thấy, và định vị đúng loại lỗi có trong dữ liệu.

**Điều kiện hoàn thành.** Phát hiện ≥ 5/7 loại lỗi cài sẵn trong `DS2` và định lượng đúng số bản ghi của mỗi loại đã phát hiện.

# Set operations and data quality in SQL

**Tóm tắt bản chất:** `UNION` so với `UNION ALL` và chi phí khử trùng. `INTERSECT` và `EXCEPT` dùng để đối chiếu hai nguồn. Ba loại trùng lặp: trùng toàn bộ cột, trùng khoá nghiệp vụ, trùng mờ. Khử trùng bằng `ROW_NUMBER` và tiêu chí quyết định giữ dòng nào. Bản ghi mồ côi và toàn vẹn tham chiếu. Bộ truy vấn kiểm tra chất lượng dùng lại được trên bảng bất kỳ. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Nỗi Đau & Động Lực

L028 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **Set operations and data quality in SQL**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Lập báo cáo chất lượng dữ liệu định lượng trên sáu chiều cho một bảng chưa từng thấy, và định vị đúng loại lỗi có trong dữ liệu. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Cơ Chế Tác Động

`UNION` so với `UNION ALL` và chi phí khử trùng. `INTERSECT` và `EXCEPT` dùng để đối chiếu hai nguồn. Ba loại trùng lặp: trùng toàn bộ cột, trùng khoá nghiệp vụ, trùng mờ. Khử trùng bằng `ROW_NUMBER` và tiêu chí quyết định giữ dòng nào. Bản ghi mồ côi và toàn vẹn tham chiếu. Bộ truy vấn kiểm tra chất lượng dùng lại được trên bảng bất kỳ.

Cơ chế của `set-operations-and-data-quality-in-sql` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Dùng `UNION` thay `UNION ALL` rồi mất dòng trùng hợp lệ · khử trùng không xác định được thứ tự nên kết quả đổi giữa các lần chạy · báo cáo tỉ lệ lỗi mà không nêu mẫu số. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Bản Đồ Quyết Định

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L028: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành “Phát hiện ≥ 5/7 loại lỗi cài sẵn trong `DS2` và định lượng đúng số bản ghi của mỗi loại đã phát hiện.”. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Case Study Thực Chiến: Set operations and data quality in SQL

Bài thực hành dùng nhiệm vụ thật của roadmap: Trên `DS2`, có 7 loại lỗi cài sẵn và không cho biết trước là lỗi gì. Tìm và định lượng.

Trước khi thao tác ở `Set operations and data quality in SQL`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L028 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Output của `Set operations and data quality in SQL` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Dùng `UNION` thay `UNION ALL` rồi mất dòng trùng hợp lệ · khử trùng không xác định được thứ tự nên kết quả đổi giữa các lần chạy · báo cáo tỉ lệ lỗi mà không nêu mẫu số. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L028 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1 — `population`.** `UNION` so với `UNION ALL` và chi phí khử trùng. `INTERSECT` và `EXCEPT` dùng để đối chiếu hai nguồn. Ba loại trùng lặp: trùng toàn bộ cột, trùng khoá nghiệp vụ, trùng mờ. Khử trùng bằng `ROW_NUMBER` và tiêu chí quyết định giữ dòng nào. Bản ghi mồ côi và toàn vẹn tham chiếu. Bộ truy vấn kiểm tra chất lượng dùng lại được trên bảng bất kỳ.

**Thiết kế.** Probe 1 của L028 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L028.1.** Đối soát `population` bằng đường tính khác implementation chính của `set-operations-and-data-quality-in-sql`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2 — `grain`.** Lập báo cáo chất lượng dữ liệu định lượng trên sáu chiều cho một bảng chưa từng thấy, và định vị đúng loại lỗi có trong dữ liệu.

**Thiết kế.** Probe 2 của L028 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L028.2.** Đối soát `grain` bằng đường tính khác implementation chính của `set-operations-and-data-quality-in-sql`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3 — `identity`.** Dùng `UNION` thay `UNION ALL` rồi mất dòng trùng hợp lệ · khử trùng không xác định được thứ tự nên kết quả đổi giữa các lần chạy · báo cáo tỉ lệ lỗi mà không nêu mẫu số.

**Thiết kế.** Probe 3 của L028 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L028.3.** Đối soát `identity` bằng đường tính khác implementation chính của `set-operations-and-data-quality-in-sql`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4 — `time cutoff`.** Phát hiện ≥ 5/7 loại lỗi cài sẵn trong `DS2` và định lượng đúng số bản ghi của mỗi loại đã phát hiện.

**Thiết kế.** Probe 4 của L028 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L028.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `set-operations-and-data-quality-in-sql`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5 — `missing versus zero`.** `UNION` so với `UNION ALL` và chi phí khử trùng. `INTERSECT` và `EXCEPT` dùng để đối chiếu hai nguồn. Ba loại trùng lặp: trùng toàn bộ cột, trùng khoá nghiệp vụ, trùng mờ. Khử trùng bằng `ROW_NUMBER` và tiêu chí quyết định giữ dòng nào. Bản ghi mồ côi và toàn vẹn tham chiếu. Bộ truy vấn kiểm tra chất lượng dùng lại được trên bảng bất kỳ.

**Thiết kế.** Probe 5 của L028 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L028.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `set-operations-and-data-quality-in-sql`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6 — `duplicate`.** Lập báo cáo chất lượng dữ liệu định lượng trên sáu chiều cho một bảng chưa từng thấy, và định vị đúng loại lỗi có trong dữ liệu.

**Thiết kế.** Probe 6 của L028 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L028.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `set-operations-and-data-quality-in-sql`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7 — `join fan-out`.** Dùng `UNION` thay `UNION ALL` rồi mất dòng trùng hợp lệ · khử trùng không xác định được thứ tự nên kết quả đổi giữa các lần chạy · báo cáo tỉ lệ lỗi mà không nêu mẫu số.

**Thiết kế.** Probe 7 của L028 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L028.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `set-operations-and-data-quality-in-sql`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8 — `changed definition`.** Phát hiện ≥ 5/7 loại lỗi cài sẵn trong `DS2` và định lượng đúng số bản ghi của mỗi loại đã phát hiện.

**Thiết kế.** Probe 8 của L028 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L028.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `set-operations-and-data-quality-in-sql`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9 — `independent oracle`.** `UNION` so với `UNION ALL` và chi phí khử trùng. `INTERSECT` và `EXCEPT` dùng để đối chiếu hai nguồn. Ba loại trùng lặp: trùng toàn bộ cột, trùng khoá nghiệp vụ, trùng mờ. Khử trùng bằng `ROW_NUMBER` và tiêu chí quyết định giữ dòng nào. Bản ghi mồ côi và toàn vẹn tham chiếu. Bộ truy vấn kiểm tra chất lượng dùng lại được trên bảng bất kỳ.

**Thiết kế.** Probe 9 của L028 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L028.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `set-operations-and-data-quality-in-sql`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10 — `replay`.** Lập báo cáo chất lượng dữ liệu định lượng trên sáu chiều cho một bảng chưa từng thấy, và định vị đúng loại lỗi có trong dữ liệu.

**Thiết kế.** Probe 10 của L028 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L028.10.** Đối soát `replay` bằng đường tính khác implementation chính của `set-operations-and-data-quality-in-sql`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11 — `fresh snapshot`.** Dùng `UNION` thay `UNION ALL` rồi mất dòng trùng hợp lệ · khử trùng không xác định được thứ tự nên kết quả đổi giữa các lần chạy · báo cáo tỉ lệ lỗi mà không nêu mẫu số.

**Thiết kế.** Probe 11 của L028 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L028.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `set-operations-and-data-quality-in-sql`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12 — `novel scenario`.** Phát hiện ≥ 5/7 loại lỗi cài sẵn trong `DS2` và định lượng đúng số bản ghi của mỗi loại đã phát hiện.

**Thiết kế.** Probe 12 của L028 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L028.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `set-operations-and-data-quality-in-sql`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L028?

<details><summary>Đáp án</summary>

Lập báo cáo chất lượng dữ liệu định lượng trên sáu chiều cho một bảng chưa từng thấy, và định vị đúng loại lỗi có trong dữ liệu.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Dùng `UNION` thay `UNION ALL` rồi mất dòng trùng hợp lệ · khử trùng không xác định được thứ tự nên kết quả đổi giữa các lần chạy · báo cáo tỉ lệ lỗi mà không nêu mẫu số.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Phát hiện ≥ 5/7 loại lỗi cài sẵn trong `DS2` và định lượng đúng số bản ghi của mỗi loại đã phát hiện.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.set-operations-and-data-quality-in-sql` đang `proposed`, chưa tính canonical coverage.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-HCMUT-SQL]] — `src.course.hcmut-sql`
2. [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]] — `src.book.silberschatz-database-system-concepts.7e`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-HCMUT-SQL]] — `src.course.hcmut-sql` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Set operations and data quality in SQL | các mục cơ chế, case và probe | Đã phủ | ngoài objective L028 |
| [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]] — `src.book.silberschatz-database-system-concepts.7e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Set operations and data quality in SQL | các mục cơ chế, case và probe | Đã phủ | ngoài objective L028 |

## Key takeaways
- Lập báo cáo chất lượng dữ liệu định lượng trên sáu chiều cho một bảng chưa từng thấy, và định vị đúng loại lỗi có trong dữ liệu.
- Phát hiện ≥ 5/7 loại lỗi cài sẵn trong `DS2` và định lượng đúng số bản ghi của mỗi loại đã phát hiện.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.
