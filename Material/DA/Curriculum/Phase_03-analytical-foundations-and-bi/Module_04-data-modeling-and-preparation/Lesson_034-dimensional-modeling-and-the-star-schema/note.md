# Phase 3: Data Analyst
# Module 4: Data Modeling and Preparation
# Lesson 34: Dimensional modeling and the star schema

## Mục tiêu bài học

**Năng lực cần chứng minh.** Thiết kế một lược đồ sao từ một lược đồ chuẩn hoá cho trước, và bảo vệ lựa chọn hạt của bảng sự kiện trước năm câu hỏi phân tích mà lược đồ phải trả lời được.

**Điều kiện hoàn thành.** Lược đồ sao trả lời được cả 5 câu hỏi phân tích ở đúng hạt, và hạt bảng sự kiện được phát biểu bằng một câu kiểm chứng được bằng phép đếm.

# Dimensional modeling and the star schema

**Tóm tắt bản chất:** Bốn bước thiết kế theo Kimball: chọn quy trình nghiệp vụ, khai báo hạt, xác định chiều, xác định độ đo. Bảng sự kiện và bảng chiều. Ba loại độ đo theo tính cộng được: cộng được, bán cộng được, không cộng được, cùng hệ quả lên phép tổng hợp. Khoá thay thế so với khoá nghiệp vụ. Lược đồ sao so với lược đồ bông tuyết và điều kiện chọn giữa hai loại. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Nỗi Đau & Động Lực

L034 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **Dimensional modeling and the star schema**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Thiết kế một lược đồ sao từ một lược đồ chuẩn hoá cho trước, và bảo vệ lựa chọn hạt của bảng sự kiện trước năm câu hỏi phân tích mà lược đồ phải trả lời được. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Cơ Chế Tác Động

Bốn bước thiết kế theo Kimball: chọn quy trình nghiệp vụ, khai báo hạt, xác định chiều, xác định độ đo. Bảng sự kiện và bảng chiều. Ba loại độ đo theo tính cộng được: cộng được, bán cộng được, không cộng được, cùng hệ quả lên phép tổng hợp. Khoá thay thế so với khoá nghiệp vụ. Lược đồ sao so với lược đồ bông tuyết và điều kiện chọn giữa hai loại.

Cơ chế của `dimensional-modeling-and-the-star-schema` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Khai báo hạt sau khi đã chọn chiều · đưa độ đo không cộng được vào bảng sự kiện mà không đánh dấu · dùng khoá nghiệp vụ làm khoá của bảng chiều rồi mất khả năng theo dõi thay đổi. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Bản Đồ Quyết Định

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L034: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành “Lược đồ sao trả lời được cả 5 câu hỏi phân tích ở đúng hạt, và hạt bảng sự kiện được phát biểu bằng một câu kiểm chứng được bằng phép đếm.”. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Case Study Thực Chiến: Dimensional modeling and the star schema

Bài thực hành dùng nhiệm vụ thật của roadmap: Chuyển `DS1` từ 6 bảng chuẩn hoá thành một lược đồ sao. Bảo vệ thiết kế trước 5 câu hỏi phân tích cho trước.

Trước khi thao tác ở `Dimensional modeling and the star schema`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L034 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Output của `Dimensional modeling and the star schema` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Khai báo hạt sau khi đã chọn chiều · đưa độ đo không cộng được vào bảng sự kiện mà không đánh dấu · dùng khoá nghiệp vụ làm khoá của bảng chiều rồi mất khả năng theo dõi thay đổi. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L034 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1 — `population`.** Bốn bước thiết kế theo Kimball: chọn quy trình nghiệp vụ, khai báo hạt, xác định chiều, xác định độ đo. Bảng sự kiện và bảng chiều. Ba loại độ đo theo tính cộng được: cộng được, bán cộng được, không cộng được, cùng hệ quả lên phép tổng hợp. Khoá thay thế so với khoá nghiệp vụ. Lược đồ sao so với lược đồ bông tuyết và điều kiện chọn giữa hai loại.

**Thiết kế.** Probe 1 của L034 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L034.1.** Đối soát `population` bằng đường tính khác implementation chính của `dimensional-modeling-and-the-star-schema`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2 — `grain`.** Thiết kế một lược đồ sao từ một lược đồ chuẩn hoá cho trước, và bảo vệ lựa chọn hạt của bảng sự kiện trước năm câu hỏi phân tích mà lược đồ phải trả lời được.

**Thiết kế.** Probe 2 của L034 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L034.2.** Đối soát `grain` bằng đường tính khác implementation chính của `dimensional-modeling-and-the-star-schema`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3 — `identity`.** Khai báo hạt sau khi đã chọn chiều · đưa độ đo không cộng được vào bảng sự kiện mà không đánh dấu · dùng khoá nghiệp vụ làm khoá của bảng chiều rồi mất khả năng theo dõi thay đổi.

**Thiết kế.** Probe 3 của L034 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L034.3.** Đối soát `identity` bằng đường tính khác implementation chính của `dimensional-modeling-and-the-star-schema`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4 — `time cutoff`.** Lược đồ sao trả lời được cả 5 câu hỏi phân tích ở đúng hạt, và hạt bảng sự kiện được phát biểu bằng một câu kiểm chứng được bằng phép đếm.

**Thiết kế.** Probe 4 của L034 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L034.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `dimensional-modeling-and-the-star-schema`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5 — `missing versus zero`.** Bốn bước thiết kế theo Kimball: chọn quy trình nghiệp vụ, khai báo hạt, xác định chiều, xác định độ đo. Bảng sự kiện và bảng chiều. Ba loại độ đo theo tính cộng được: cộng được, bán cộng được, không cộng được, cùng hệ quả lên phép tổng hợp. Khoá thay thế so với khoá nghiệp vụ. Lược đồ sao so với lược đồ bông tuyết và điều kiện chọn giữa hai loại.

**Thiết kế.** Probe 5 của L034 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L034.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `dimensional-modeling-and-the-star-schema`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6 — `duplicate`.** Thiết kế một lược đồ sao từ một lược đồ chuẩn hoá cho trước, và bảo vệ lựa chọn hạt của bảng sự kiện trước năm câu hỏi phân tích mà lược đồ phải trả lời được.

**Thiết kế.** Probe 6 của L034 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L034.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `dimensional-modeling-and-the-star-schema`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7 — `join fan-out`.** Khai báo hạt sau khi đã chọn chiều · đưa độ đo không cộng được vào bảng sự kiện mà không đánh dấu · dùng khoá nghiệp vụ làm khoá của bảng chiều rồi mất khả năng theo dõi thay đổi.

**Thiết kế.** Probe 7 của L034 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L034.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `dimensional-modeling-and-the-star-schema`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8 — `changed definition`.** Lược đồ sao trả lời được cả 5 câu hỏi phân tích ở đúng hạt, và hạt bảng sự kiện được phát biểu bằng một câu kiểm chứng được bằng phép đếm.

**Thiết kế.** Probe 8 của L034 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L034.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `dimensional-modeling-and-the-star-schema`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9 — `independent oracle`.** Bốn bước thiết kế theo Kimball: chọn quy trình nghiệp vụ, khai báo hạt, xác định chiều, xác định độ đo. Bảng sự kiện và bảng chiều. Ba loại độ đo theo tính cộng được: cộng được, bán cộng được, không cộng được, cùng hệ quả lên phép tổng hợp. Khoá thay thế so với khoá nghiệp vụ. Lược đồ sao so với lược đồ bông tuyết và điều kiện chọn giữa hai loại.

**Thiết kế.** Probe 9 của L034 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L034.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `dimensional-modeling-and-the-star-schema`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10 — `replay`.** Thiết kế một lược đồ sao từ một lược đồ chuẩn hoá cho trước, và bảo vệ lựa chọn hạt của bảng sự kiện trước năm câu hỏi phân tích mà lược đồ phải trả lời được.

**Thiết kế.** Probe 10 của L034 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L034.10.** Đối soát `replay` bằng đường tính khác implementation chính của `dimensional-modeling-and-the-star-schema`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11 — `fresh snapshot`.** Khai báo hạt sau khi đã chọn chiều · đưa độ đo không cộng được vào bảng sự kiện mà không đánh dấu · dùng khoá nghiệp vụ làm khoá của bảng chiều rồi mất khả năng theo dõi thay đổi.

**Thiết kế.** Probe 11 của L034 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L034.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `dimensional-modeling-and-the-star-schema`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12 — `novel scenario`.** Lược đồ sao trả lời được cả 5 câu hỏi phân tích ở đúng hạt, và hạt bảng sự kiện được phát biểu bằng một câu kiểm chứng được bằng phép đếm.

**Thiết kế.** Probe 12 của L034 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L034.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `dimensional-modeling-and-the-star-schema`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L034?

<details><summary>Đáp án</summary>

Thiết kế một lược đồ sao từ một lược đồ chuẩn hoá cho trước, và bảo vệ lựa chọn hạt của bảng sự kiện trước năm câu hỏi phân tích mà lược đồ phải trả lời được.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Khai báo hạt sau khi đã chọn chiều · đưa độ đo không cộng được vào bảng sự kiện mà không đánh dấu · dùng khoá nghiệp vụ làm khoá của bảng chiều rồi mất khả năng theo dõi thay đổi.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Lược đồ sao trả lời được cả 5 câu hỏi phân tích ở đúng hạt, và hạt bảng sự kiện được phát biểu bằng một câu kiểm chứng được bằng phép đếm.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.dimensional-modeling-and-the-star-schema` đang `proposed`, chưa tính canonical coverage.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-KIMBALL-ROSS-DW-TOOLKIT-3E]] — `src.book.kimball-ross-data-warehouse-toolkit.3e`
2. [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]] — `src.book.silberschatz-database-system-concepts.7e`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-KIMBALL-ROSS-DW-TOOLKIT-3E]] — `src.book.kimball-ross-data-warehouse-toolkit.3e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Dimensional modeling and the star schema | các mục cơ chế, case và probe | Đã phủ | ngoài objective L034 |
| [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]] — `src.book.silberschatz-database-system-concepts.7e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Dimensional modeling and the star schema | các mục cơ chế, case và probe | Đã phủ | ngoài objective L034 |

## Key takeaways
- Thiết kế một lược đồ sao từ một lược đồ chuẩn hoá cho trước, và bảo vệ lựa chọn hạt của bảng sự kiện trước năm câu hỏi phân tích mà lược đồ phải trả lời được.
- Lược đồ sao trả lời được cả 5 câu hỏi phân tích ở đúng hạt, và hạt bảng sự kiện được phát biểu bằng một câu kiểm chứng được bằng phép đếm.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.
