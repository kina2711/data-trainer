# Phase 3: Data Analyst
# Module 4: Data Modeling and Preparation
# Lesson 36: Data cleaning in practice

## Mục tiêu bài học

**Năng lực cần chứng minh.** Nạp một tệp CSV có lỗi vào cơ sở dữ liệu và chứng minh bằng phép cộng rằng tổng số bản ghi đầu vào bằng số bản ghi sạch cộng số bản ghi lỗi.

**Điều kiện hoàn thành.** Đẳng thức 50.000 = 49.985 + 15 kiểm được bằng truy vấn, và cả 15 bản ghi lỗi có lý do ghi rõ.

# Data cleaning in practice

**Tóm tắt bản chất:** Quy trình năm bước: khảo sát tệp, định nghĩa lược đồ tạm, nạp thô, chuyển đổi có bắt lỗi, đối soát. Bốn bẫy nhập liệu: dấu phẩy trong trường địa chỉ, mã hoá tiếng Việt UTF-8, số điện thoại có chữ số 0 đầu, ngày ở định dạng `dd/MM/yyyy`. Nguyên tắc không loại bản ghi lỗi trong im lặng: tách bảng lỗi riêng, mỗi bản ghi kèm lý do bị loại. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Nỗi Đau & Động Lực

L036 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **Data cleaning in practice**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Nạp một tệp CSV có lỗi vào cơ sở dữ liệu và chứng minh bằng phép cộng rằng tổng số bản ghi đầu vào bằng số bản ghi sạch cộng số bản ghi lỗi. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Cơ Chế Tác Động

Quy trình năm bước: khảo sát tệp, định nghĩa lược đồ tạm, nạp thô, chuyển đổi có bắt lỗi, đối soát. Bốn bẫy nhập liệu: dấu phẩy trong trường địa chỉ, mã hoá tiếng Việt UTF-8, số điện thoại có chữ số 0 đầu, ngày ở định dạng `dd/MM/yyyy`. Nguyên tắc không loại bản ghi lỗi trong im lặng: tách bảng lỗi riêng, mỗi bản ghi kèm lý do bị loại.

Cơ chế của `data-cleaning-in-practice` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Bỏ qua dòng lỗi trong im lặng nên mất dấu vết · đặt bước lọc trước bước ép kiểu · để công cụ tự suy đoán mã hoá ký tự. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Bản Đồ Quyết Định

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L036: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành “Đẳng thức 50.000 = 49.985 + 15 kiểm được bằng truy vấn, và cả 15 bản ghi lỗi có lý do ghi rõ.”. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Case Study Thực Chiến: Data cleaning in practice

Bài thực hành dùng nhiệm vụ thật của roadmap: Nạp `orders.csv` gồm 50.000 dòng và xử lý đủ bốn bẫy định dạng. Rồi nạp `orders_dirty.csv` gồm 50.005 dòng vào bảng trung chuyển; kết quả phải chứng minh 50.005 = 49.985 bản ghi qua được ép kiểu + 20 bản ghi bị loại, mỗi bản ghi bị loại có lý do ghi rõ. Nếu áp thêm khoá chính và ràng buộc không rỗng thì bảng chính chỉ nhận 49.980 dòng; giải thích chênh lệch 5 dòng.

Trước khi thao tác ở `Data cleaning in practice`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L036 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Output của `Data cleaning in practice` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Bỏ qua dòng lỗi trong im lặng nên mất dấu vết · đặt bước lọc trước bước ép kiểu · để công cụ tự suy đoán mã hoá ký tự. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L036 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1 — `population`.** Quy trình năm bước: khảo sát tệp, định nghĩa lược đồ tạm, nạp thô, chuyển đổi có bắt lỗi, đối soát. Bốn bẫy nhập liệu: dấu phẩy trong trường địa chỉ, mã hoá tiếng Việt UTF-8, số điện thoại có chữ số 0 đầu, ngày ở định dạng `dd/MM/yyyy`. Nguyên tắc không loại bản ghi lỗi trong im lặng: tách bảng lỗi riêng, mỗi bản ghi kèm lý do bị loại.

**Thiết kế.** Probe 1 của L036 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L036.1.** Đối soát `population` bằng đường tính khác implementation chính của `data-cleaning-in-practice`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2 — `grain`.** Nạp một tệp CSV có lỗi vào cơ sở dữ liệu và chứng minh bằng phép cộng rằng tổng số bản ghi đầu vào bằng số bản ghi sạch cộng số bản ghi lỗi.

**Thiết kế.** Probe 2 của L036 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L036.2.** Đối soát `grain` bằng đường tính khác implementation chính của `data-cleaning-in-practice`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3 — `identity`.** Bỏ qua dòng lỗi trong im lặng nên mất dấu vết · đặt bước lọc trước bước ép kiểu · để công cụ tự suy đoán mã hoá ký tự.

**Thiết kế.** Probe 3 của L036 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L036.3.** Đối soát `identity` bằng đường tính khác implementation chính của `data-cleaning-in-practice`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4 — `time cutoff`.** Đẳng thức 50.000 = 49.985 + 15 kiểm được bằng truy vấn, và cả 15 bản ghi lỗi có lý do ghi rõ.

**Thiết kế.** Probe 4 của L036 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L036.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `data-cleaning-in-practice`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5 — `missing versus zero`.** Quy trình năm bước: khảo sát tệp, định nghĩa lược đồ tạm, nạp thô, chuyển đổi có bắt lỗi, đối soát. Bốn bẫy nhập liệu: dấu phẩy trong trường địa chỉ, mã hoá tiếng Việt UTF-8, số điện thoại có chữ số 0 đầu, ngày ở định dạng `dd/MM/yyyy`. Nguyên tắc không loại bản ghi lỗi trong im lặng: tách bảng lỗi riêng, mỗi bản ghi kèm lý do bị loại.

**Thiết kế.** Probe 5 của L036 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L036.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `data-cleaning-in-practice`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6 — `duplicate`.** Nạp một tệp CSV có lỗi vào cơ sở dữ liệu và chứng minh bằng phép cộng rằng tổng số bản ghi đầu vào bằng số bản ghi sạch cộng số bản ghi lỗi.

**Thiết kế.** Probe 6 của L036 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L036.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `data-cleaning-in-practice`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7 — `join fan-out`.** Bỏ qua dòng lỗi trong im lặng nên mất dấu vết · đặt bước lọc trước bước ép kiểu · để công cụ tự suy đoán mã hoá ký tự.

**Thiết kế.** Probe 7 của L036 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L036.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `data-cleaning-in-practice`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8 — `changed definition`.** Đẳng thức 50.000 = 49.985 + 15 kiểm được bằng truy vấn, và cả 15 bản ghi lỗi có lý do ghi rõ.

**Thiết kế.** Probe 8 của L036 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L036.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `data-cleaning-in-practice`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9 — `independent oracle`.** Quy trình năm bước: khảo sát tệp, định nghĩa lược đồ tạm, nạp thô, chuyển đổi có bắt lỗi, đối soát. Bốn bẫy nhập liệu: dấu phẩy trong trường địa chỉ, mã hoá tiếng Việt UTF-8, số điện thoại có chữ số 0 đầu, ngày ở định dạng `dd/MM/yyyy`. Nguyên tắc không loại bản ghi lỗi trong im lặng: tách bảng lỗi riêng, mỗi bản ghi kèm lý do bị loại.

**Thiết kế.** Probe 9 của L036 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L036.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `data-cleaning-in-practice`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10 — `replay`.** Nạp một tệp CSV có lỗi vào cơ sở dữ liệu và chứng minh bằng phép cộng rằng tổng số bản ghi đầu vào bằng số bản ghi sạch cộng số bản ghi lỗi.

**Thiết kế.** Probe 10 của L036 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L036.10.** Đối soát `replay` bằng đường tính khác implementation chính của `data-cleaning-in-practice`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11 — `fresh snapshot`.** Bỏ qua dòng lỗi trong im lặng nên mất dấu vết · đặt bước lọc trước bước ép kiểu · để công cụ tự suy đoán mã hoá ký tự.

**Thiết kế.** Probe 11 của L036 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L036.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `data-cleaning-in-practice`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12 — `novel scenario`.** Đẳng thức 50.000 = 49.985 + 15 kiểm được bằng truy vấn, và cả 15 bản ghi lỗi có lý do ghi rõ.

**Thiết kế.** Probe 12 của L036 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L036.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `data-cleaning-in-practice`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L036?

<details><summary>Đáp án</summary>

Nạp một tệp CSV có lỗi vào cơ sở dữ liệu và chứng minh bằng phép cộng rằng tổng số bản ghi đầu vào bằng số bản ghi sạch cộng số bản ghi lỗi.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Bỏ qua dòng lỗi trong im lặng nên mất dấu vết · đặt bước lọc trước bước ép kiểu · để công cụ tự suy đoán mã hoá ký tự.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Đẳng thức 50.000 = 49.985 + 15 kiểm được bằng truy vấn, và cả 15 bản ghi lỗi có lý do ghi rõ.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.data-cleaning-in-practice` đang `proposed`, chưa tính canonical coverage.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-KIMBALL-ROSS-DW-TOOLKIT-3E]] — `src.book.kimball-ross-data-warehouse-toolkit.3e`
2. [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]] — `src.book.silberschatz-database-system-concepts.7e`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-KIMBALL-ROSS-DW-TOOLKIT-3E]] — `src.book.kimball-ross-data-warehouse-toolkit.3e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Data cleaning in practice | các mục cơ chế, case và probe | Đã phủ | ngoài objective L036 |
| [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]] — `src.book.silberschatz-database-system-concepts.7e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Data cleaning in practice | các mục cơ chế, case và probe | Đã phủ | ngoài objective L036 |

## Key takeaways
- Nạp một tệp CSV có lỗi vào cơ sở dữ liệu và chứng minh bằng phép cộng rằng tổng số bản ghi đầu vào bằng số bản ghi sạch cộng số bản ghi lỗi.
- Đẳng thức 50.000 = 49.985 + 15 kiểm được bằng truy vấn, và cả 15 bản ghi lỗi có lý do ghi rõ.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.
