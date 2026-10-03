# Phase 4: Data Analyst
# Module 9: Python for Data Analysts
# Lesson 71: pandas (2) - grouping, joining, pivoting

## Mục tiêu bài học

**Năng lực cần chứng minh.** Thực hiện bằng pandas mọi phép biến đổi đã làm được bằng SQL, và nêu tiêu chí quyết định phép nào nên chạy ở cơ sở dữ liệu.

**Điều kiện hoàn thành.** Cả 10 kết quả khớp từng dòng với truy vấn SQL, và bảng so thời gian chạy được nộp kèm kết luận về nơi nên chạy phép gộp.

# pandas (2) - grouping, joining, pivoting

**Tóm tắt bản chất:** `groupby` và các phép tổng hợp; `agg` với nhiều hàm cùng lúc. `merge` với bốn kiểu tương ứng bốn kiểu `JOIN`, và tham số `validate` để phát hiện nhân bản dòng. `concat`. `pivot_table` và `melt`. `sort_values` và `nlargest`. Mỗi thao tác được giới thiệu kèm truy vấn SQL tương đương từ lesson 22 tới 24. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Nỗi Đau & Động Lực

L071 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **pandas (2) - grouping, joining, pivoting**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Thực hiện bằng pandas mọi phép biến đổi đã làm được bằng SQL, và nêu tiêu chí quyết định phép nào nên chạy ở cơ sở dữ liệu. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Cơ Chế Tác Động

`groupby` và các phép tổng hợp; `agg` với nhiều hàm cùng lúc. `merge` với bốn kiểu tương ứng bốn kiểu `JOIN`, và tham số `validate` để phát hiện nhân bản dòng. `concat`. `pivot_table` và `melt`. `sort_values` và `nlargest`. Mỗi thao tác được giới thiệu kèm truy vấn SQL tương đương từ lesson 22 tới 24.

Cơ chế của `pandas-2-grouping-joining-pivoting` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Bỏ tham số `validate` nên không phát hiện nhân bản dòng khi `merge` · kéo toàn bộ bảng về rồi gộp trong pandas · dùng `apply` theo dòng ở nơi có phép vector hoá. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Bản Đồ Quyết Định

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L071: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành “Cả 10 kết quả khớp từng dòng với truy vấn SQL, và bảng so thời gian chạy được nộp kèm kết luận về nơi nên chạy phép gộp.”. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Case Study Thực Chiến: pandas (2) - grouping, joining, pivoting

Bài thực hành dùng nhiệm vụ thật của roadmap: Làm lại 10 truy vấn SQL từ lesson 22–24 bằng pandas. So kết quả từng dòng. Đo và so thời gian chạy của hai cách.

Trước khi thao tác ở `pandas (2) - grouping, joining, pivoting`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L071 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Output của `pandas (2) - grouping, joining, pivoting` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Bỏ tham số `validate` nên không phát hiện nhân bản dòng khi `merge` · kéo toàn bộ bảng về rồi gộp trong pandas · dùng `apply` theo dòng ở nơi có phép vector hoá. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L071 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1 — `population`.** `groupby` và các phép tổng hợp; `agg` với nhiều hàm cùng lúc. `merge` với bốn kiểu tương ứng bốn kiểu `JOIN`, và tham số `validate` để phát hiện nhân bản dòng. `concat`. `pivot_table` và `melt`. `sort_values` và `nlargest`. Mỗi thao tác được giới thiệu kèm truy vấn SQL tương đương từ lesson 22 tới 24.

**Thiết kế.** Probe 1 của L071 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L071.1.** Đối soát `population` bằng đường tính khác implementation chính của `pandas-2-grouping-joining-pivoting`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2 — `grain`.** Thực hiện bằng pandas mọi phép biến đổi đã làm được bằng SQL, và nêu tiêu chí quyết định phép nào nên chạy ở cơ sở dữ liệu.

**Thiết kế.** Probe 2 của L071 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L071.2.** Đối soát `grain` bằng đường tính khác implementation chính của `pandas-2-grouping-joining-pivoting`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3 — `identity`.** Bỏ tham số `validate` nên không phát hiện nhân bản dòng khi `merge` · kéo toàn bộ bảng về rồi gộp trong pandas · dùng `apply` theo dòng ở nơi có phép vector hoá.

**Thiết kế.** Probe 3 của L071 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L071.3.** Đối soát `identity` bằng đường tính khác implementation chính của `pandas-2-grouping-joining-pivoting`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4 — `time cutoff`.** Cả 10 kết quả khớp từng dòng với truy vấn SQL, và bảng so thời gian chạy được nộp kèm kết luận về nơi nên chạy phép gộp.

**Thiết kế.** Probe 4 của L071 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L071.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `pandas-2-grouping-joining-pivoting`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5 — `missing versus zero`.** `groupby` và các phép tổng hợp; `agg` với nhiều hàm cùng lúc. `merge` với bốn kiểu tương ứng bốn kiểu `JOIN`, và tham số `validate` để phát hiện nhân bản dòng. `concat`. `pivot_table` và `melt`. `sort_values` và `nlargest`. Mỗi thao tác được giới thiệu kèm truy vấn SQL tương đương từ lesson 22 tới 24.

**Thiết kế.** Probe 5 của L071 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L071.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `pandas-2-grouping-joining-pivoting`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6 — `duplicate`.** Thực hiện bằng pandas mọi phép biến đổi đã làm được bằng SQL, và nêu tiêu chí quyết định phép nào nên chạy ở cơ sở dữ liệu.

**Thiết kế.** Probe 6 của L071 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L071.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `pandas-2-grouping-joining-pivoting`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7 — `join fan-out`.** Bỏ tham số `validate` nên không phát hiện nhân bản dòng khi `merge` · kéo toàn bộ bảng về rồi gộp trong pandas · dùng `apply` theo dòng ở nơi có phép vector hoá.

**Thiết kế.** Probe 7 của L071 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L071.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `pandas-2-grouping-joining-pivoting`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8 — `changed definition`.** Cả 10 kết quả khớp từng dòng với truy vấn SQL, và bảng so thời gian chạy được nộp kèm kết luận về nơi nên chạy phép gộp.

**Thiết kế.** Probe 8 của L071 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L071.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `pandas-2-grouping-joining-pivoting`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9 — `independent oracle`.** `groupby` và các phép tổng hợp; `agg` với nhiều hàm cùng lúc. `merge` với bốn kiểu tương ứng bốn kiểu `JOIN`, và tham số `validate` để phát hiện nhân bản dòng. `concat`. `pivot_table` và `melt`. `sort_values` và `nlargest`. Mỗi thao tác được giới thiệu kèm truy vấn SQL tương đương từ lesson 22 tới 24.

**Thiết kế.** Probe 9 của L071 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L071.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `pandas-2-grouping-joining-pivoting`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10 — `replay`.** Thực hiện bằng pandas mọi phép biến đổi đã làm được bằng SQL, và nêu tiêu chí quyết định phép nào nên chạy ở cơ sở dữ liệu.

**Thiết kế.** Probe 10 của L071 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L071.10.** Đối soát `replay` bằng đường tính khác implementation chính của `pandas-2-grouping-joining-pivoting`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11 — `fresh snapshot`.** Bỏ tham số `validate` nên không phát hiện nhân bản dòng khi `merge` · kéo toàn bộ bảng về rồi gộp trong pandas · dùng `apply` theo dòng ở nơi có phép vector hoá.

**Thiết kế.** Probe 11 của L071 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L071.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `pandas-2-grouping-joining-pivoting`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12 — `novel scenario`.** Cả 10 kết quả khớp từng dòng với truy vấn SQL, và bảng so thời gian chạy được nộp kèm kết luận về nơi nên chạy phép gộp.

**Thiết kế.** Probe 12 của L071 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L071.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `pandas-2-grouping-joining-pivoting`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L071?

<details><summary>Đáp án</summary>

Thực hiện bằng pandas mọi phép biến đổi đã làm được bằng SQL, và nêu tiêu chí quyết định phép nào nên chạy ở cơ sở dữ liệu.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Bỏ tham số `validate` nên không phát hiện nhân bản dòng khi `merge` · kéo toàn bộ bảng về rồi gộp trong pandas · dùng `apply` theo dòng ở nơi có phép vector hoá.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Cả 10 kết quả khớp từng dòng với truy vấn SQL, và bảng so thời gian chạy được nộp kèm kết luận về nơi nên chạy phép gộp.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.pandas-2-grouping-joining-pivoting` đang `proposed`, chưa tính canonical coverage.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-PYTHON-314-LANGUAGE-REFERENCE]] — `src.docs.python-3.14-language-reference`
2. [[SRC-PYTHON-314-STDLIB-RUNTIME]] — `src.docs.python-3.14-stdlib-runtime`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-PYTHON-314-LANGUAGE-REFERENCE]] — `src.docs.python-3.14-language-reference` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới pandas (2) - grouping, joining, pivoting | các mục cơ chế, case và probe | Đã phủ | ngoài objective L071 |
| [[SRC-PYTHON-314-STDLIB-RUNTIME]] — `src.docs.python-3.14-stdlib-runtime` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới pandas (2) - grouping, joining, pivoting | các mục cơ chế, case và probe | Đã phủ | ngoài objective L071 |

## Key takeaways
- Thực hiện bằng pandas mọi phép biến đổi đã làm được bằng SQL, và nêu tiêu chí quyết định phép nào nên chạy ở cơ sở dữ liệu.
- Cả 10 kết quả khớp từng dòng với truy vấn SQL, và bảng so thời gian chạy được nộp kèm kết luận về nơi nên chạy phép gộp.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.
