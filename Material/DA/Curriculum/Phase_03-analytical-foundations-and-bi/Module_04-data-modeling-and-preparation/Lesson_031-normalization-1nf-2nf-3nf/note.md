# Phase 3: Data Analyst
# Module 4: Data Modeling and Preparation
# Lesson 31: Normalization - 1NF, 2NF, 3NF

## Mục tiêu bài học

**Năng lực cần chứng minh.** Chuẩn hoá một bảng phẳng tới 3NF và chỉ ra dị thường nào được loại bỏ ở bước nào.

**Điều kiện hoàn thành.** Ba bước tách được ánh xạ đúng sang ba dạng chuẩn, và mỗi bước nêu được dị thường cụ thể đã loại bỏ.

# Normalization - 1NF, 2NF, 3NF

**Tóm tắt bản chất:** Ba dị thường thao tác: dị thường thêm, dị thường sửa, dị thường xoá. Trình tự dạy đi từ dị thường quan sát được tới quy tắc, không theo chiều ngược lại. Phụ thuộc hàm. 1NF và giá trị nguyên tử: cơ chế khiến một cột chứa danh sách ngăn bởi dấu phẩy làm mọi phép lọc và gộp theo phần tử trở nên không tin được. 2NF, 3NF và phụ thuộc bắc cầu. Phi chuẩn hoá có chủ đích: điều kiện áp dụng và chi phí đi kèm. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Nỗi Đau & Động Lực

L031 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **Normalization - 1NF, 2NF, 3NF**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Chuẩn hoá một bảng phẳng tới 3NF và chỉ ra dị thường nào được loại bỏ ở bước nào. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Cơ Chế Tác Động

Ba dị thường thao tác: dị thường thêm, dị thường sửa, dị thường xoá. Trình tự dạy đi từ dị thường quan sát được tới quy tắc, không theo chiều ngược lại. Phụ thuộc hàm. 1NF và giá trị nguyên tử: cơ chế khiến một cột chứa danh sách ngăn bởi dấu phẩy làm mọi phép lọc và gộp theo phần tử trở nên không tin được. 2NF, 3NF và phụ thuộc bắc cầu. Phi chuẩn hoá có chủ đích: điều kiện áp dụng và chi phí đi kèm.

Cơ chế của `normalization-1nf-2nf-3nf` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Học quy tắc dạng chuẩn trước khi gặp dị thường nên không giải thích được vì sao tách · chuẩn hoá tới mức làm mọi truy vấn phân tích cần bảy phép ghép · nhầm phụ thuộc hàm với tương quan thống kê. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Bản Đồ Quyết Định

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L031: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành “Ba bước tách được ánh xạ đúng sang ba dạng chuẩn, và mỗi bước nêu được dị thường cụ thể đã loại bỏ.”. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Case Study Thực Chiến: Normalization - 1NF, 2NF, 3NF

Bài thực hành dùng nhiệm vụ thật của roadmap: Từ một bảng phẳng chứa mọi thuộc tính, tự tạo ba dị thường, rồi tách bảng để loại bỏ từng dị thường. Ánh xạ mỗi bước tách sang 1NF, 2NF hoặc 3NF.

Trước khi thao tác ở `Normalization - 1NF, 2NF, 3NF`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L031 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Output của `Normalization - 1NF, 2NF, 3NF` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Học quy tắc dạng chuẩn trước khi gặp dị thường nên không giải thích được vì sao tách · chuẩn hoá tới mức làm mọi truy vấn phân tích cần bảy phép ghép · nhầm phụ thuộc hàm với tương quan thống kê. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L031 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1 — `population`.** Ba dị thường thao tác: dị thường thêm, dị thường sửa, dị thường xoá. Trình tự dạy đi từ dị thường quan sát được tới quy tắc, không theo chiều ngược lại. Phụ thuộc hàm. 1NF và giá trị nguyên tử: cơ chế khiến một cột chứa danh sách ngăn bởi dấu phẩy làm mọi phép lọc và gộp theo phần tử trở nên không tin được. 2NF, 3NF và phụ thuộc bắc cầu. Phi chuẩn hoá có chủ đích: điều kiện áp dụng và chi phí đi kèm.

**Thiết kế.** Probe 1 của L031 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L031.1.** Đối soát `population` bằng đường tính khác implementation chính của `normalization-1nf-2nf-3nf`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2 — `grain`.** Chuẩn hoá một bảng phẳng tới 3NF và chỉ ra dị thường nào được loại bỏ ở bước nào.

**Thiết kế.** Probe 2 của L031 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L031.2.** Đối soát `grain` bằng đường tính khác implementation chính của `normalization-1nf-2nf-3nf`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3 — `identity`.** Học quy tắc dạng chuẩn trước khi gặp dị thường nên không giải thích được vì sao tách · chuẩn hoá tới mức làm mọi truy vấn phân tích cần bảy phép ghép · nhầm phụ thuộc hàm với tương quan thống kê.

**Thiết kế.** Probe 3 của L031 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L031.3.** Đối soát `identity` bằng đường tính khác implementation chính của `normalization-1nf-2nf-3nf`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4 — `time cutoff`.** Ba bước tách được ánh xạ đúng sang ba dạng chuẩn, và mỗi bước nêu được dị thường cụ thể đã loại bỏ.

**Thiết kế.** Probe 4 của L031 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L031.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `normalization-1nf-2nf-3nf`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5 — `missing versus zero`.** Ba dị thường thao tác: dị thường thêm, dị thường sửa, dị thường xoá. Trình tự dạy đi từ dị thường quan sát được tới quy tắc, không theo chiều ngược lại. Phụ thuộc hàm. 1NF và giá trị nguyên tử: cơ chế khiến một cột chứa danh sách ngăn bởi dấu phẩy làm mọi phép lọc và gộp theo phần tử trở nên không tin được. 2NF, 3NF và phụ thuộc bắc cầu. Phi chuẩn hoá có chủ đích: điều kiện áp dụng và chi phí đi kèm.

**Thiết kế.** Probe 5 của L031 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L031.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `normalization-1nf-2nf-3nf`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6 — `duplicate`.** Chuẩn hoá một bảng phẳng tới 3NF và chỉ ra dị thường nào được loại bỏ ở bước nào.

**Thiết kế.** Probe 6 của L031 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L031.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `normalization-1nf-2nf-3nf`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7 — `join fan-out`.** Học quy tắc dạng chuẩn trước khi gặp dị thường nên không giải thích được vì sao tách · chuẩn hoá tới mức làm mọi truy vấn phân tích cần bảy phép ghép · nhầm phụ thuộc hàm với tương quan thống kê.

**Thiết kế.** Probe 7 của L031 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L031.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `normalization-1nf-2nf-3nf`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8 — `changed definition`.** Ba bước tách được ánh xạ đúng sang ba dạng chuẩn, và mỗi bước nêu được dị thường cụ thể đã loại bỏ.

**Thiết kế.** Probe 8 của L031 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L031.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `normalization-1nf-2nf-3nf`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9 — `independent oracle`.** Ba dị thường thao tác: dị thường thêm, dị thường sửa, dị thường xoá. Trình tự dạy đi từ dị thường quan sát được tới quy tắc, không theo chiều ngược lại. Phụ thuộc hàm. 1NF và giá trị nguyên tử: cơ chế khiến một cột chứa danh sách ngăn bởi dấu phẩy làm mọi phép lọc và gộp theo phần tử trở nên không tin được. 2NF, 3NF và phụ thuộc bắc cầu. Phi chuẩn hoá có chủ đích: điều kiện áp dụng và chi phí đi kèm.

**Thiết kế.** Probe 9 của L031 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L031.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `normalization-1nf-2nf-3nf`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10 — `replay`.** Chuẩn hoá một bảng phẳng tới 3NF và chỉ ra dị thường nào được loại bỏ ở bước nào.

**Thiết kế.** Probe 10 của L031 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L031.10.** Đối soát `replay` bằng đường tính khác implementation chính của `normalization-1nf-2nf-3nf`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11 — `fresh snapshot`.** Học quy tắc dạng chuẩn trước khi gặp dị thường nên không giải thích được vì sao tách · chuẩn hoá tới mức làm mọi truy vấn phân tích cần bảy phép ghép · nhầm phụ thuộc hàm với tương quan thống kê.

**Thiết kế.** Probe 11 của L031 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L031.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `normalization-1nf-2nf-3nf`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12 — `novel scenario`.** Ba bước tách được ánh xạ đúng sang ba dạng chuẩn, và mỗi bước nêu được dị thường cụ thể đã loại bỏ.

**Thiết kế.** Probe 12 của L031 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L031.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `normalization-1nf-2nf-3nf`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L031?

<details><summary>Đáp án</summary>

Chuẩn hoá một bảng phẳng tới 3NF và chỉ ra dị thường nào được loại bỏ ở bước nào.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Học quy tắc dạng chuẩn trước khi gặp dị thường nên không giải thích được vì sao tách · chuẩn hoá tới mức làm mọi truy vấn phân tích cần bảy phép ghép · nhầm phụ thuộc hàm với tương quan thống kê.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Ba bước tách được ánh xạ đúng sang ba dạng chuẩn, và mỗi bước nêu được dị thường cụ thể đã loại bỏ.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.normalization-1nf-2nf-3nf` đang `proposed`, chưa tính canonical coverage.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-KIMBALL-ROSS-DW-TOOLKIT-3E]] — `src.book.kimball-ross-data-warehouse-toolkit.3e`
2. [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]] — `src.book.silberschatz-database-system-concepts.7e`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-KIMBALL-ROSS-DW-TOOLKIT-3E]] — `src.book.kimball-ross-data-warehouse-toolkit.3e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Normalization - 1NF, 2NF, 3NF | các mục cơ chế, case và probe | Đã phủ | ngoài objective L031 |
| [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]] — `src.book.silberschatz-database-system-concepts.7e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Normalization - 1NF, 2NF, 3NF | các mục cơ chế, case và probe | Đã phủ | ngoài objective L031 |

## Key takeaways
- Chuẩn hoá một bảng phẳng tới 3NF và chỉ ra dị thường nào được loại bỏ ở bước nào.
- Ba bước tách được ánh xạ đúng sang ba dạng chuẩn, và mỗi bước nêu được dị thường cụ thể đã loại bỏ.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.
