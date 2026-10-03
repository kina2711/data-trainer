# Phase 2: Data Analyst
# Module 3: SQL and Databases
# Lesson 29: Exploring an unfamiliar database

## Mục tiêu bài học

**Năng lực cần chứng minh.** Tái dựng sơ đồ quan hệ của một cơ sở dữ liệu không có tài liệu, chỉ bằng truy vấn, và phát biểu hạt của từng bảng.

**Điều kiện hoàn thành.** Xác định đúng ≥ 4/5 quan hệ khoá ngoại và phát biểu đúng hạt của cả 6 bảng, chỉ dùng truy vấn.

# Exploring an unfamiliar database

**Tóm tắt bản chất:** Đọc siêu dữ liệu hệ thống qua `INFORMATION_SCHEMA`. Bảy truy vấn khảo sát chuẩn: đếm dòng, đếm giá trị phân biệt, tỉ lệ `NULL`, khoảng min–max, các giá trị xuất hiện nhiều nhất, phân bố độ dài chuỗi, phân bố theo ngày. Suy ra khoá chính và khoá ngoại từ dữ liệu khi không có ràng buộc khai báo. Kiểm chứng hạt bằng phép đếm. Đọc tên cột như một giả thuyết cần kiểm chứng chứ không như một định nghĩa. Nguyên nhân truy vấn chậm và vai trò của chỉ mục, ở mức nhận biết. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Nỗi Đau & Động Lực

L029 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **Exploring an unfamiliar database**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Tái dựng sơ đồ quan hệ của một cơ sở dữ liệu không có tài liệu, chỉ bằng truy vấn, và phát biểu hạt của từng bảng. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Cơ Chế Tác Động

Đọc siêu dữ liệu hệ thống qua `INFORMATION_SCHEMA`. Bảy truy vấn khảo sát chuẩn: đếm dòng, đếm giá trị phân biệt, tỉ lệ `NULL`, khoảng min–max, các giá trị xuất hiện nhiều nhất, phân bố độ dài chuỗi, phân bố theo ngày. Suy ra khoá chính và khoá ngoại từ dữ liệu khi không có ràng buộc khai báo. Kiểm chứng hạt bằng phép đếm. Đọc tên cột như một giả thuyết cần kiểm chứng chứ không như một định nghĩa. Nguyên nhân truy vấn chậm và vai trò của chỉ mục, ở mức nhận biết.

Cơ chế của `exploring-an-unfamiliar-database` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Suy khoá ngoại từ tên cột mà không kiểm chứng bằng dữ liệu · giả định cột tên giống nhau thì nghĩa giống nhau · bỏ qua bảng trung gian của quan hệ nhiều–nhiều. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Bản Đồ Quyết Định

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L029: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành “Xác định đúng ≥ 4/5 quan hệ khoá ngoại và phát biểu đúng hạt của cả 6 bảng, chỉ dùng truy vấn.”. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Case Study Thực Chiến: Exploring an unfamiliar database

Bài thực hành dùng nhiệm vụ thật của roadmap: Nhận `DS1` không kèm sơ đồ. Tái dựng sơ đồ quan hệ và phát biểu hạt của cả 6 bảng. Đối chiếu với đáp án sau khi nộp.

Trước khi thao tác ở `Exploring an unfamiliar database`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L029 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Output của `Exploring an unfamiliar database` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Suy khoá ngoại từ tên cột mà không kiểm chứng bằng dữ liệu · giả định cột tên giống nhau thì nghĩa giống nhau · bỏ qua bảng trung gian của quan hệ nhiều–nhiều. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L029 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1 — `population`.** Đọc siêu dữ liệu hệ thống qua `INFORMATION_SCHEMA`. Bảy truy vấn khảo sát chuẩn: đếm dòng, đếm giá trị phân biệt, tỉ lệ `NULL`, khoảng min–max, các giá trị xuất hiện nhiều nhất, phân bố độ dài chuỗi, phân bố theo ngày. Suy ra khoá chính và khoá ngoại từ dữ liệu khi không có ràng buộc khai báo. Kiểm chứng hạt bằng phép đếm. Đọc tên cột như một giả thuyết cần kiểm chứng chứ không như một định nghĩa. Nguyên nhân truy vấn chậm và vai trò của chỉ mục, ở mức nhận biết.

**Thiết kế.** Probe 1 của L029 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L029.1.** Đối soát `population` bằng đường tính khác implementation chính của `exploring-an-unfamiliar-database`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2 — `grain`.** Tái dựng sơ đồ quan hệ của một cơ sở dữ liệu không có tài liệu, chỉ bằng truy vấn, và phát biểu hạt của từng bảng.

**Thiết kế.** Probe 2 của L029 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L029.2.** Đối soát `grain` bằng đường tính khác implementation chính của `exploring-an-unfamiliar-database`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3 — `identity`.** Suy khoá ngoại từ tên cột mà không kiểm chứng bằng dữ liệu · giả định cột tên giống nhau thì nghĩa giống nhau · bỏ qua bảng trung gian của quan hệ nhiều–nhiều.

**Thiết kế.** Probe 3 của L029 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L029.3.** Đối soát `identity` bằng đường tính khác implementation chính của `exploring-an-unfamiliar-database`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4 — `time cutoff`.** Xác định đúng ≥ 4/5 quan hệ khoá ngoại và phát biểu đúng hạt của cả 6 bảng, chỉ dùng truy vấn.

**Thiết kế.** Probe 4 của L029 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L029.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `exploring-an-unfamiliar-database`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5 — `missing versus zero`.** Đọc siêu dữ liệu hệ thống qua `INFORMATION_SCHEMA`. Bảy truy vấn khảo sát chuẩn: đếm dòng, đếm giá trị phân biệt, tỉ lệ `NULL`, khoảng min–max, các giá trị xuất hiện nhiều nhất, phân bố độ dài chuỗi, phân bố theo ngày. Suy ra khoá chính và khoá ngoại từ dữ liệu khi không có ràng buộc khai báo. Kiểm chứng hạt bằng phép đếm. Đọc tên cột như một giả thuyết cần kiểm chứng chứ không như một định nghĩa. Nguyên nhân truy vấn chậm và vai trò của chỉ mục, ở mức nhận biết.

**Thiết kế.** Probe 5 của L029 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L029.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `exploring-an-unfamiliar-database`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6 — `duplicate`.** Tái dựng sơ đồ quan hệ của một cơ sở dữ liệu không có tài liệu, chỉ bằng truy vấn, và phát biểu hạt của từng bảng.

**Thiết kế.** Probe 6 của L029 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L029.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `exploring-an-unfamiliar-database`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7 — `join fan-out`.** Suy khoá ngoại từ tên cột mà không kiểm chứng bằng dữ liệu · giả định cột tên giống nhau thì nghĩa giống nhau · bỏ qua bảng trung gian của quan hệ nhiều–nhiều.

**Thiết kế.** Probe 7 của L029 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L029.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `exploring-an-unfamiliar-database`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8 — `changed definition`.** Xác định đúng ≥ 4/5 quan hệ khoá ngoại và phát biểu đúng hạt của cả 6 bảng, chỉ dùng truy vấn.

**Thiết kế.** Probe 8 của L029 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L029.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `exploring-an-unfamiliar-database`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9 — `independent oracle`.** Đọc siêu dữ liệu hệ thống qua `INFORMATION_SCHEMA`. Bảy truy vấn khảo sát chuẩn: đếm dòng, đếm giá trị phân biệt, tỉ lệ `NULL`, khoảng min–max, các giá trị xuất hiện nhiều nhất, phân bố độ dài chuỗi, phân bố theo ngày. Suy ra khoá chính và khoá ngoại từ dữ liệu khi không có ràng buộc khai báo. Kiểm chứng hạt bằng phép đếm. Đọc tên cột như một giả thuyết cần kiểm chứng chứ không như một định nghĩa. Nguyên nhân truy vấn chậm và vai trò của chỉ mục, ở mức nhận biết.

**Thiết kế.** Probe 9 của L029 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L029.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `exploring-an-unfamiliar-database`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10 — `replay`.** Tái dựng sơ đồ quan hệ của một cơ sở dữ liệu không có tài liệu, chỉ bằng truy vấn, và phát biểu hạt của từng bảng.

**Thiết kế.** Probe 10 của L029 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L029.10.** Đối soát `replay` bằng đường tính khác implementation chính của `exploring-an-unfamiliar-database`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11 — `fresh snapshot`.** Suy khoá ngoại từ tên cột mà không kiểm chứng bằng dữ liệu · giả định cột tên giống nhau thì nghĩa giống nhau · bỏ qua bảng trung gian của quan hệ nhiều–nhiều.

**Thiết kế.** Probe 11 của L029 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L029.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `exploring-an-unfamiliar-database`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12 — `novel scenario`.** Xác định đúng ≥ 4/5 quan hệ khoá ngoại và phát biểu đúng hạt của cả 6 bảng, chỉ dùng truy vấn.

**Thiết kế.** Probe 12 của L029 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L029.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `exploring-an-unfamiliar-database`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L029?

<details><summary>Đáp án</summary>

Tái dựng sơ đồ quan hệ của một cơ sở dữ liệu không có tài liệu, chỉ bằng truy vấn, và phát biểu hạt của từng bảng.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Suy khoá ngoại từ tên cột mà không kiểm chứng bằng dữ liệu · giả định cột tên giống nhau thì nghĩa giống nhau · bỏ qua bảng trung gian của quan hệ nhiều–nhiều.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Xác định đúng ≥ 4/5 quan hệ khoá ngoại và phát biểu đúng hạt của cả 6 bảng, chỉ dùng truy vấn.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.exploring-an-unfamiliar-database` đang `proposed`, chưa tính canonical coverage.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-HCMUT-SQL]] — `src.course.hcmut-sql`
2. [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]] — `src.book.silberschatz-database-system-concepts.7e`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-HCMUT-SQL]] — `src.course.hcmut-sql` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Exploring an unfamiliar database | các mục cơ chế, case và probe | Đã phủ | ngoài objective L029 |
| [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]] — `src.book.silberschatz-database-system-concepts.7e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Exploring an unfamiliar database | các mục cơ chế, case và probe | Đã phủ | ngoài objective L029 |

## Key takeaways
- Tái dựng sơ đồ quan hệ của một cơ sở dữ liệu không có tài liệu, chỉ bằng truy vấn, và phát biểu hạt của từng bảng.
- Xác định đúng ≥ 4/5 quan hệ khoá ngoại và phát biểu đúng hạt của cả 6 bảng, chỉ dùng truy vấn.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.
