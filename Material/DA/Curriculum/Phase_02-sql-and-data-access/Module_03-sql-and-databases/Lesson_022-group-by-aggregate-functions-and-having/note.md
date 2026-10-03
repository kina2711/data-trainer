# Phase 2: Data Analyst
# Module 3: SQL and Databases
# Lesson 22: GROUP BY, aggregate functions and HAVING

## Mục tiêu bài học

**Năng lực cần chứng minh.** Phát biểu hạt trước và sau mỗi phép `GROUP BY`, và chọn đúng biến thể `COUNT` theo câu hỏi nghiệp vụ.

**Điều kiện hoàn thành.** ≥ 18/20 truy vấn đúng cả kết quả lẫn phát biểu hạt trước và sau.

# GROUP BY, aggregate functions and HAVING

**Tóm tắt bản chất:** `GROUP BY` là một phép biến đổi hạt; cách trình bày này suy ra được mọi quy tắc còn lại của mệnh đề. Hệ quả: mọi cột trong `SELECT` phải nằm trong `GROUP BY` hoặc trong một hàm tổng hợp. Ba biến thể đếm `COUNT(*)`, `COUNT(cot)`, `COUNT(DISTINCT cot)` và tập bản ghi mỗi biến thể tính. `SUM`, `AVG`, `MIN`, `MAX` và cách chúng bỏ qua `NULL`. `WHERE` lọc dòng trước gộp, `HAVING` lọc nhóm sau gộp. Gộp nhóm trên biểu thức. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Nỗi Đau & Động Lực

L022 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **GROUP BY, aggregate functions and HAVING**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Phát biểu hạt trước và sau mỗi phép `GROUP BY`, và chọn đúng biến thể `COUNT` theo câu hỏi nghiệp vụ. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Cơ Chế Tác Động

`GROUP BY` là một phép biến đổi hạt; cách trình bày này suy ra được mọi quy tắc còn lại của mệnh đề. Hệ quả: mọi cột trong `SELECT` phải nằm trong `GROUP BY` hoặc trong một hàm tổng hợp. Ba biến thể đếm `COUNT(*)`, `COUNT(cot)`, `COUNT(DISTINCT cot)` và tập bản ghi mỗi biến thể tính. `SUM`, `AVG`, `MIN`, `MAX` và cách chúng bỏ qua `NULL`. `WHERE` lọc dòng trước gộp, `HAVING` lọc nhóm sau gộp. Gộp nhóm trên biểu thức.

Cơ chế của `group-by-aggregate-functions-and-having` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Đặt điều kiện trên giá trị tổng hợp vào `WHERE` · dùng `COUNT(*)` khi câu hỏi cần `COUNT(DISTINCT)` · lấy trung bình của trung bình. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Bản Đồ Quyết Định

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L022: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành “≥ 18/20 truy vấn đúng cả kết quả lẫn phát biểu hạt trước và sau.”. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Case Study Thực Chiến: GROUP BY, aggregate functions and HAVING

Bài thực hành dùng nhiệm vụ thật của roadmap: 20 truy vấn gộp nhóm trên `DS1`, mỗi truy vấn nộp kèm phát biểu hạt trước và sau khi gộp.

Trước khi thao tác ở `GROUP BY, aggregate functions and HAVING`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L022 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Output của `GROUP BY, aggregate functions and HAVING` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Đặt điều kiện trên giá trị tổng hợp vào `WHERE` · dùng `COUNT(*)` khi câu hỏi cần `COUNT(DISTINCT)` · lấy trung bình của trung bình. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L022 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1 — `population`.** `GROUP BY` là một phép biến đổi hạt; cách trình bày này suy ra được mọi quy tắc còn lại của mệnh đề. Hệ quả: mọi cột trong `SELECT` phải nằm trong `GROUP BY` hoặc trong một hàm tổng hợp. Ba biến thể đếm `COUNT(*)`, `COUNT(cot)`, `COUNT(DISTINCT cot)` và tập bản ghi mỗi biến thể tính. `SUM`, `AVG`, `MIN`, `MAX` và cách chúng bỏ qua `NULL`. `WHERE` lọc dòng trước gộp, `HAVING` lọc nhóm sau gộp. Gộp nhóm trên biểu thức.

**Thiết kế.** Probe 1 của L022 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L022.1.** Đối soát `population` bằng đường tính khác implementation chính của `group-by-aggregate-functions-and-having`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2 — `grain`.** Phát biểu hạt trước và sau mỗi phép `GROUP BY`, và chọn đúng biến thể `COUNT` theo câu hỏi nghiệp vụ.

**Thiết kế.** Probe 2 của L022 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L022.2.** Đối soát `grain` bằng đường tính khác implementation chính của `group-by-aggregate-functions-and-having`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3 — `identity`.** Đặt điều kiện trên giá trị tổng hợp vào `WHERE` · dùng `COUNT(*)` khi câu hỏi cần `COUNT(DISTINCT)` · lấy trung bình của trung bình.

**Thiết kế.** Probe 3 của L022 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L022.3.** Đối soát `identity` bằng đường tính khác implementation chính của `group-by-aggregate-functions-and-having`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4 — `time cutoff`.** ≥ 18/20 truy vấn đúng cả kết quả lẫn phát biểu hạt trước và sau.

**Thiết kế.** Probe 4 của L022 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L022.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `group-by-aggregate-functions-and-having`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5 — `missing versus zero`.** `GROUP BY` là một phép biến đổi hạt; cách trình bày này suy ra được mọi quy tắc còn lại của mệnh đề. Hệ quả: mọi cột trong `SELECT` phải nằm trong `GROUP BY` hoặc trong một hàm tổng hợp. Ba biến thể đếm `COUNT(*)`, `COUNT(cot)`, `COUNT(DISTINCT cot)` và tập bản ghi mỗi biến thể tính. `SUM`, `AVG`, `MIN`, `MAX` và cách chúng bỏ qua `NULL`. `WHERE` lọc dòng trước gộp, `HAVING` lọc nhóm sau gộp. Gộp nhóm trên biểu thức.

**Thiết kế.** Probe 5 của L022 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L022.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `group-by-aggregate-functions-and-having`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6 — `duplicate`.** Phát biểu hạt trước và sau mỗi phép `GROUP BY`, và chọn đúng biến thể `COUNT` theo câu hỏi nghiệp vụ.

**Thiết kế.** Probe 6 của L022 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L022.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `group-by-aggregate-functions-and-having`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7 — `join fan-out`.** Đặt điều kiện trên giá trị tổng hợp vào `WHERE` · dùng `COUNT(*)` khi câu hỏi cần `COUNT(DISTINCT)` · lấy trung bình của trung bình.

**Thiết kế.** Probe 7 của L022 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L022.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `group-by-aggregate-functions-and-having`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8 — `changed definition`.** ≥ 18/20 truy vấn đúng cả kết quả lẫn phát biểu hạt trước và sau.

**Thiết kế.** Probe 8 của L022 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L022.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `group-by-aggregate-functions-and-having`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9 — `independent oracle`.** `GROUP BY` là một phép biến đổi hạt; cách trình bày này suy ra được mọi quy tắc còn lại của mệnh đề. Hệ quả: mọi cột trong `SELECT` phải nằm trong `GROUP BY` hoặc trong một hàm tổng hợp. Ba biến thể đếm `COUNT(*)`, `COUNT(cot)`, `COUNT(DISTINCT cot)` và tập bản ghi mỗi biến thể tính. `SUM`, `AVG`, `MIN`, `MAX` và cách chúng bỏ qua `NULL`. `WHERE` lọc dòng trước gộp, `HAVING` lọc nhóm sau gộp. Gộp nhóm trên biểu thức.

**Thiết kế.** Probe 9 của L022 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L022.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `group-by-aggregate-functions-and-having`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10 — `replay`.** Phát biểu hạt trước và sau mỗi phép `GROUP BY`, và chọn đúng biến thể `COUNT` theo câu hỏi nghiệp vụ.

**Thiết kế.** Probe 10 của L022 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L022.10.** Đối soát `replay` bằng đường tính khác implementation chính của `group-by-aggregate-functions-and-having`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11 — `fresh snapshot`.** Đặt điều kiện trên giá trị tổng hợp vào `WHERE` · dùng `COUNT(*)` khi câu hỏi cần `COUNT(DISTINCT)` · lấy trung bình của trung bình.

**Thiết kế.** Probe 11 của L022 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L022.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `group-by-aggregate-functions-and-having`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12 — `novel scenario`.** ≥ 18/20 truy vấn đúng cả kết quả lẫn phát biểu hạt trước và sau.

**Thiết kế.** Probe 12 của L022 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L022.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `group-by-aggregate-functions-and-having`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L022?

<details><summary>Đáp án</summary>

Phát biểu hạt trước và sau mỗi phép `GROUP BY`, và chọn đúng biến thể `COUNT` theo câu hỏi nghiệp vụ.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Đặt điều kiện trên giá trị tổng hợp vào `WHERE` · dùng `COUNT(*)` khi câu hỏi cần `COUNT(DISTINCT)` · lấy trung bình của trung bình.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

≥ 18/20 truy vấn đúng cả kết quả lẫn phát biểu hạt trước và sau.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.group-by-aggregate-functions-and-having` đang `proposed`, chưa tính canonical coverage.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-HCMUT-SQL]] — `src.course.hcmut-sql`
2. [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]] — `src.book.silberschatz-database-system-concepts.7e`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-HCMUT-SQL]] — `src.course.hcmut-sql` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới GROUP BY, aggregate functions and HAVING | các mục cơ chế, case và probe | Đã phủ | ngoài objective L022 |
| [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]] — `src.book.silberschatz-database-system-concepts.7e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới GROUP BY, aggregate functions and HAVING | các mục cơ chế, case và probe | Đã phủ | ngoài objective L022 |

## Key takeaways
- Phát biểu hạt trước và sau mỗi phép `GROUP BY`, và chọn đúng biến thể `COUNT` theo câu hỏi nghiệp vụ.
- ≥ 18/20 truy vấn đúng cả kết quả lẫn phát biểu hạt trước và sau.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.
