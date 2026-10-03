# Phase 2: Data Analyst
# Module 3: SQL and Databases
# Lesson 26: Window functions (1) - ranking and positioning

## Mục tiêu bài học

**Năng lực cần chứng minh.** Giải bài toán lấy N dòng đầu theo nhóm, và chọn giữa bốn hàm xếp hạng theo yêu cầu nghiệp vụ về cách xử lý giá trị trùng.

**Điều kiện hoàn thành.** Cả ba bài cho số dòng đúng trên dữ liệu có giá trị trùng, và mỗi bài kèm lý do chọn hàm xếp hạng.

# Window functions (1) - ranking and positioning

**Tóm tắt bản chất:** Khác biệt nền tảng: `GROUP BY` thu gọn số dòng, `OVER` giữ nguyên số dòng. Cấu trúc `OVER (PARTITION BY ... ORDER BY ...)`. `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `NTILE`, với khác biệt chỉ biểu hiện khi tồn tại giá trị trùng. Mẫu lấy N dòng đầu mỗi nhóm. Nguyên nhân không dùng được hàm cửa sổ trong `WHERE` và cách vòng qua bằng truy vấn con hoặc CTE. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Nỗi Đau & Động Lực

L026 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **Window functions (1) - ranking and positioning**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Giải bài toán lấy N dòng đầu theo nhóm, và chọn giữa bốn hàm xếp hạng theo yêu cầu nghiệp vụ về cách xử lý giá trị trùng. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Cơ Chế Tác Động

Khác biệt nền tảng: `GROUP BY` thu gọn số dòng, `OVER` giữ nguyên số dòng. Cấu trúc `OVER (PARTITION BY ... ORDER BY ...)`. `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `NTILE`, với khác biệt chỉ biểu hiện khi tồn tại giá trị trùng. Mẫu lấy N dòng đầu mỗi nhóm. Nguyên nhân không dùng được hàm cửa sổ trong `WHERE` và cách vòng qua bằng truy vấn con hoặc CTE.

Cơ chế của `window-functions-1-ranking-and-positioning` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Dùng `RANK` khi nghiệp vụ cần đúng N dòng · đặt hàm cửa sổ trong `WHERE` · thiếu `PARTITION BY` nên xếp hạng trên toàn bảng. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Bản Đồ Quyết Định

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L026: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành “Cả ba bài cho số dòng đúng trên dữ liệu có giá trị trùng, và mỗi bài kèm lý do chọn hàm xếp hạng.”. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Case Study Thực Chiến: Window functions (1) - ranking and positioning

Bài thực hành dùng nhiệm vụ thật của roadmap: Ba sản phẩm bán chạy nhất mỗi chi nhánh. Đơn hàng gần nhất của mỗi khách. Chia khách thành 5 nhóm ngũ phân vị theo chi tiêu. Dữ liệu có chứa giá trị trùng ở cả ba bài.

Trước khi thao tác ở `Window functions (1) - ranking and positioning`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L026 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Output của `Window functions (1) - ranking and positioning` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Dùng `RANK` khi nghiệp vụ cần đúng N dòng · đặt hàm cửa sổ trong `WHERE` · thiếu `PARTITION BY` nên xếp hạng trên toàn bảng. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L026 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1 — `population`.** Khác biệt nền tảng: `GROUP BY` thu gọn số dòng, `OVER` giữ nguyên số dòng. Cấu trúc `OVER (PARTITION BY ... ORDER BY ...)`. `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `NTILE`, với khác biệt chỉ biểu hiện khi tồn tại giá trị trùng. Mẫu lấy N dòng đầu mỗi nhóm. Nguyên nhân không dùng được hàm cửa sổ trong `WHERE` và cách vòng qua bằng truy vấn con hoặc CTE.

**Thiết kế.** Probe 1 của L026 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L026.1.** Đối soát `population` bằng đường tính khác implementation chính của `window-functions-1-ranking-and-positioning`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2 — `grain`.** Giải bài toán lấy N dòng đầu theo nhóm, và chọn giữa bốn hàm xếp hạng theo yêu cầu nghiệp vụ về cách xử lý giá trị trùng.

**Thiết kế.** Probe 2 của L026 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L026.2.** Đối soát `grain` bằng đường tính khác implementation chính của `window-functions-1-ranking-and-positioning`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3 — `identity`.** Dùng `RANK` khi nghiệp vụ cần đúng N dòng · đặt hàm cửa sổ trong `WHERE` · thiếu `PARTITION BY` nên xếp hạng trên toàn bảng.

**Thiết kế.** Probe 3 của L026 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L026.3.** Đối soát `identity` bằng đường tính khác implementation chính của `window-functions-1-ranking-and-positioning`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4 — `time cutoff`.** Cả ba bài cho số dòng đúng trên dữ liệu có giá trị trùng, và mỗi bài kèm lý do chọn hàm xếp hạng.

**Thiết kế.** Probe 4 của L026 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L026.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `window-functions-1-ranking-and-positioning`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5 — `missing versus zero`.** Khác biệt nền tảng: `GROUP BY` thu gọn số dòng, `OVER` giữ nguyên số dòng. Cấu trúc `OVER (PARTITION BY ... ORDER BY ...)`. `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `NTILE`, với khác biệt chỉ biểu hiện khi tồn tại giá trị trùng. Mẫu lấy N dòng đầu mỗi nhóm. Nguyên nhân không dùng được hàm cửa sổ trong `WHERE` và cách vòng qua bằng truy vấn con hoặc CTE.

**Thiết kế.** Probe 5 của L026 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L026.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `window-functions-1-ranking-and-positioning`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6 — `duplicate`.** Giải bài toán lấy N dòng đầu theo nhóm, và chọn giữa bốn hàm xếp hạng theo yêu cầu nghiệp vụ về cách xử lý giá trị trùng.

**Thiết kế.** Probe 6 của L026 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L026.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `window-functions-1-ranking-and-positioning`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7 — `join fan-out`.** Dùng `RANK` khi nghiệp vụ cần đúng N dòng · đặt hàm cửa sổ trong `WHERE` · thiếu `PARTITION BY` nên xếp hạng trên toàn bảng.

**Thiết kế.** Probe 7 của L026 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L026.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `window-functions-1-ranking-and-positioning`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8 — `changed definition`.** Cả ba bài cho số dòng đúng trên dữ liệu có giá trị trùng, và mỗi bài kèm lý do chọn hàm xếp hạng.

**Thiết kế.** Probe 8 của L026 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L026.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `window-functions-1-ranking-and-positioning`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9 — `independent oracle`.** Khác biệt nền tảng: `GROUP BY` thu gọn số dòng, `OVER` giữ nguyên số dòng. Cấu trúc `OVER (PARTITION BY ... ORDER BY ...)`. `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `NTILE`, với khác biệt chỉ biểu hiện khi tồn tại giá trị trùng. Mẫu lấy N dòng đầu mỗi nhóm. Nguyên nhân không dùng được hàm cửa sổ trong `WHERE` và cách vòng qua bằng truy vấn con hoặc CTE.

**Thiết kế.** Probe 9 của L026 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L026.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `window-functions-1-ranking-and-positioning`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10 — `replay`.** Giải bài toán lấy N dòng đầu theo nhóm, và chọn giữa bốn hàm xếp hạng theo yêu cầu nghiệp vụ về cách xử lý giá trị trùng.

**Thiết kế.** Probe 10 của L026 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L026.10.** Đối soát `replay` bằng đường tính khác implementation chính của `window-functions-1-ranking-and-positioning`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11 — `fresh snapshot`.** Dùng `RANK` khi nghiệp vụ cần đúng N dòng · đặt hàm cửa sổ trong `WHERE` · thiếu `PARTITION BY` nên xếp hạng trên toàn bảng.

**Thiết kế.** Probe 11 của L026 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L026.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `window-functions-1-ranking-and-positioning`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12 — `novel scenario`.** Cả ba bài cho số dòng đúng trên dữ liệu có giá trị trùng, và mỗi bài kèm lý do chọn hàm xếp hạng.

**Thiết kế.** Probe 12 của L026 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L026.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `window-functions-1-ranking-and-positioning`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L026?

<details><summary>Đáp án</summary>

Giải bài toán lấy N dòng đầu theo nhóm, và chọn giữa bốn hàm xếp hạng theo yêu cầu nghiệp vụ về cách xử lý giá trị trùng.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Dùng `RANK` khi nghiệp vụ cần đúng N dòng · đặt hàm cửa sổ trong `WHERE` · thiếu `PARTITION BY` nên xếp hạng trên toàn bảng.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Cả ba bài cho số dòng đúng trên dữ liệu có giá trị trùng, và mỗi bài kèm lý do chọn hàm xếp hạng.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.window-functions-1-ranking-and-positioning` đang `proposed`, chưa tính canonical coverage.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-HCMUT-SQL]] — `src.course.hcmut-sql`
2. [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]] — `src.book.silberschatz-database-system-concepts.7e`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-HCMUT-SQL]] — `src.course.hcmut-sql` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Window functions (1) - ranking and positioning | các mục cơ chế, case và probe | Đã phủ | ngoài objective L026 |
| [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]] — `src.book.silberschatz-database-system-concepts.7e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Window functions (1) - ranking and positioning | các mục cơ chế, case và probe | Đã phủ | ngoài objective L026 |

## Key takeaways
- Giải bài toán lấy N dòng đầu theo nhóm, và chọn giữa bốn hàm xếp hạng theo yêu cầu nghiệp vụ về cách xử lý giá trị trùng.
- Cả ba bài cho số dòng đúng trên dữ liệu có giá trị trùng, và mỗi bài kèm lý do chọn hàm xếp hạng.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.
