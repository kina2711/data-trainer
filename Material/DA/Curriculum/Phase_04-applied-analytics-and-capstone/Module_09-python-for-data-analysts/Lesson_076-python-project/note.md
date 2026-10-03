# Phase 4: Data Analyst
# Module 9: Python for Data Analysts
# Lesson 76: Python project

## Mục tiêu bài học

**Năng lực cần chứng minh.** Đóng gói một quy trình phân tích thành kho mã mà một người chưa từng thấy nó chạy lại được bằng một lệnh và cho ra kết quả giống hệt.

**Điều kiện hoàn thành.** Một học viên khác chạy lại kho mã thành công bằng một lệnh, cho ra kết quả giống hệt, và không đặt câu hỏi nào. Đây là exit criterion của Module 9.

# Python project

**Tóm tắt bản chất:** Không có nội dung mới. Dự án gộp toàn bộ M9 vào một kho mã duy nhất. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Nỗi Đau & Động Lực

L076 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **Python project**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Đóng gói một quy trình phân tích thành kho mã mà một người chưa từng thấy nó chạy lại được bằng một lệnh và cho ra kết quả giống hệt. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Cơ Chế Tác Động

Không có nội dung mới. Dự án gộp toàn bộ M9 vào một kho mã duy nhất.

Cơ chế của `python-project` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: README ghi thư viện đã dùng thay vì ghi cách chạy · phụ thuộc đường dẫn tuyệt đối trên máy người viết · không ghim phiên bản thư viện nên môi trường người khác cho kết quả khác. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Bản Đồ Quyết Định

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L076: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành “Một học viên khác chạy lại kho mã thành công bằng một lệnh, cho ra kết quả giống hệt, và không đặt câu hỏi nào. Đây là exit criterion của Module 9.”. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Case Study Thực Chiến: Python project

Bài thực hành dùng nhiệm vụ thật của roadmap: Nhận một bài toán phân tích kèm yêu cầu tự động hoá. Nộp kho mã gồm: README đủ để người lạ chạy lại, script chạy bằng một lệnh, kiểm thử, nhật ký, và kết quả xuất ra. Hoán đổi kho mã với một học viên khác.

Trước khi thao tác ở `Python project`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L076 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Output của `Python project` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** README ghi thư viện đã dùng thay vì ghi cách chạy · phụ thuộc đường dẫn tuyệt đối trên máy người viết · không ghim phiên bản thư viện nên môi trường người khác cho kết quả khác. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L076 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1 — `population`.** Không có nội dung mới. Dự án gộp toàn bộ M9 vào một kho mã duy nhất.

**Thiết kế.** Probe 1 của L076 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L076.1.** Đối soát `population` bằng đường tính khác implementation chính của `python-project`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2 — `grain`.** Đóng gói một quy trình phân tích thành kho mã mà một người chưa từng thấy nó chạy lại được bằng một lệnh và cho ra kết quả giống hệt.

**Thiết kế.** Probe 2 của L076 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L076.2.** Đối soát `grain` bằng đường tính khác implementation chính của `python-project`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3 — `identity`.** README ghi thư viện đã dùng thay vì ghi cách chạy · phụ thuộc đường dẫn tuyệt đối trên máy người viết · không ghim phiên bản thư viện nên môi trường người khác cho kết quả khác.

**Thiết kế.** Probe 3 của L076 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L076.3.** Đối soát `identity` bằng đường tính khác implementation chính của `python-project`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4 — `time cutoff`.** Một học viên khác chạy lại kho mã thành công bằng một lệnh, cho ra kết quả giống hệt, và không đặt câu hỏi nào. Đây là exit criterion của Module 9.

**Thiết kế.** Probe 4 của L076 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L076.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `python-project`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5 — `missing versus zero`.** Không có nội dung mới. Dự án gộp toàn bộ M9 vào một kho mã duy nhất.

**Thiết kế.** Probe 5 của L076 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L076.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `python-project`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6 — `duplicate`.** Đóng gói một quy trình phân tích thành kho mã mà một người chưa từng thấy nó chạy lại được bằng một lệnh và cho ra kết quả giống hệt.

**Thiết kế.** Probe 6 của L076 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L076.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `python-project`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7 — `join fan-out`.** README ghi thư viện đã dùng thay vì ghi cách chạy · phụ thuộc đường dẫn tuyệt đối trên máy người viết · không ghim phiên bản thư viện nên môi trường người khác cho kết quả khác.

**Thiết kế.** Probe 7 của L076 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L076.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `python-project`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8 — `changed definition`.** Một học viên khác chạy lại kho mã thành công bằng một lệnh, cho ra kết quả giống hệt, và không đặt câu hỏi nào. Đây là exit criterion của Module 9.

**Thiết kế.** Probe 8 của L076 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L076.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `python-project`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9 — `independent oracle`.** Không có nội dung mới. Dự án gộp toàn bộ M9 vào một kho mã duy nhất.

**Thiết kế.** Probe 9 của L076 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L076.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `python-project`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10 — `replay`.** Đóng gói một quy trình phân tích thành kho mã mà một người chưa từng thấy nó chạy lại được bằng một lệnh và cho ra kết quả giống hệt.

**Thiết kế.** Probe 10 của L076 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L076.10.** Đối soát `replay` bằng đường tính khác implementation chính của `python-project`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11 — `fresh snapshot`.** README ghi thư viện đã dùng thay vì ghi cách chạy · phụ thuộc đường dẫn tuyệt đối trên máy người viết · không ghim phiên bản thư viện nên môi trường người khác cho kết quả khác.

**Thiết kế.** Probe 11 của L076 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L076.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `python-project`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12 — `novel scenario`.** Một học viên khác chạy lại kho mã thành công bằng một lệnh, cho ra kết quả giống hệt, và không đặt câu hỏi nào. Đây là exit criterion của Module 9.

**Thiết kế.** Probe 12 của L076 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L076.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `python-project`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L076?

<details><summary>Đáp án</summary>

Đóng gói một quy trình phân tích thành kho mã mà một người chưa từng thấy nó chạy lại được bằng một lệnh và cho ra kết quả giống hệt.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

README ghi thư viện đã dùng thay vì ghi cách chạy · phụ thuộc đường dẫn tuyệt đối trên máy người viết · không ghim phiên bản thư viện nên môi trường người khác cho kết quả khác.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Một học viên khác chạy lại kho mã thành công bằng một lệnh, cho ra kết quả giống hệt, và không đặt câu hỏi nào. Đây là exit criterion của Module 9.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.python-project` đang `proposed`, chưa tính canonical coverage.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-PYTHON-314-LANGUAGE-REFERENCE]] — `src.docs.python-3.14-language-reference`
2. [[SRC-PYTHON-314-STDLIB-RUNTIME]] — `src.docs.python-3.14-stdlib-runtime`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-PYTHON-314-LANGUAGE-REFERENCE]] — `src.docs.python-3.14-language-reference` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Python project | các mục cơ chế, case và probe | Đã phủ | ngoài objective L076 |
| [[SRC-PYTHON-314-STDLIB-RUNTIME]] — `src.docs.python-3.14-stdlib-runtime` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Python project | các mục cơ chế, case và probe | Đã phủ | ngoài objective L076 |

## Key takeaways
- Đóng gói một quy trình phân tích thành kho mã mà một người chưa từng thấy nó chạy lại được bằng một lệnh và cho ra kết quả giống hệt.
- Một học viên khác chạy lại kho mã thành công bằng một lệnh, cho ra kết quả giống hệt, và không đặt câu hỏi nào. Đây là exit criterion của Module 9.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.
