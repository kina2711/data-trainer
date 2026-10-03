# Phase 3: Data Analyst
# Module 4: Data Modeling and Preparation
# Lesson 37: Reconciliation and the discipline of verification

## Mục tiêu bài học

**Năng lực cần chứng minh.** Chứng minh một kết quả bằng hai đường tính toán độc lập, và truy nguyên nguồn gốc của mọi khoản chênh lệch giữa các báo cáo mâu thuẫn.

**Điều kiện hoàn thành.** Nộp bản ghi điều tra truy được nguồn gốc cả ba khoản chênh lệch, hai đường chứng minh không dùng chung nguồn trung gian, và bản ghi qua được phản biện chéo. Đây là exit criterion của Module 4.

# Reconciliation and the discipline of verification

**Tóm tắt bản chất:** Bốn kỹ thuật đối soát: tổng kiểm tra, đối chiếu chéo giữa hai nguồn độc lập, kiểm tra biên, kiểm tra thứ nguyên. Ba phép kiểm tính hợp lý: bậc độ lớn, chiều xu hướng, tỉ lệ nội bộ giữa các thành phần. Cấu trúc bốn đoạn của phần giả định và giới hạn. Cách phát biểu mức độ không chắc chắn mà vẫn giữ được giá trị sử dụng của kết quả. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Nỗi Đau & Động Lực

L037 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **Reconciliation and the discipline of verification**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Chứng minh một kết quả bằng hai đường tính toán độc lập, và truy nguyên nguồn gốc của mọi khoản chênh lệch giữa các báo cáo mâu thuẫn. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Cơ Chế Tác Động

Bốn kỹ thuật đối soát: tổng kiểm tra, đối chiếu chéo giữa hai nguồn độc lập, kiểm tra biên, kiểm tra thứ nguyên. Ba phép kiểm tính hợp lý: bậc độ lớn, chiều xu hướng, tỉ lệ nội bộ giữa các thành phần. Cấu trúc bốn đoạn của phần giả định và giới hạn. Cách phát biểu mức độ không chắc chắn mà vẫn giữ được giá trị sử dụng của kết quả.

Cơ chế của `reconciliation-and-the-discipline-of-verification` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Chứng minh bằng hai đường không thực sự độc lập vì cùng dùng một nguồn trung gian · bỏ kiểm tra thứ nguyên · viết phần giới hạn mà không gắn với dữ liệu cụ thể. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Bản Đồ Quyết Định

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L037: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành “Nộp bản ghi điều tra truy được nguồn gốc cả ba khoản chênh lệch, hai đường chứng minh không dùng chung nguồn trung gian, và bản ghi qua được phản biện chéo. Đây là exit criterion của Module 4.”. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Case Study Thực Chiến: Reconciliation and the discipline of verification

Bài thực hành dùng nhiệm vụ thật của roadmap: Nhận bốn báo cáo mâu thuẫn về cùng một tháng. Truy nguyên nguồn gốc từng khoản chênh lệch, kết luận con số nào đúng, viết bản ghi điều tra. Phản biện chéo giữa các nhóm.

Trước khi thao tác ở `Reconciliation and the discipline of verification`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L037 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Output của `Reconciliation and the discipline of verification` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Chứng minh bằng hai đường không thực sự độc lập vì cùng dùng một nguồn trung gian · bỏ kiểm tra thứ nguyên · viết phần giới hạn mà không gắn với dữ liệu cụ thể. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L037 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1 — `population`.** Bốn kỹ thuật đối soát: tổng kiểm tra, đối chiếu chéo giữa hai nguồn độc lập, kiểm tra biên, kiểm tra thứ nguyên. Ba phép kiểm tính hợp lý: bậc độ lớn, chiều xu hướng, tỉ lệ nội bộ giữa các thành phần. Cấu trúc bốn đoạn của phần giả định và giới hạn. Cách phát biểu mức độ không chắc chắn mà vẫn giữ được giá trị sử dụng của kết quả.

**Thiết kế.** Probe 1 của L037 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L037.1.** Đối soát `population` bằng đường tính khác implementation chính của `reconciliation-and-the-discipline-of-verification`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2 — `grain`.** Chứng minh một kết quả bằng hai đường tính toán độc lập, và truy nguyên nguồn gốc của mọi khoản chênh lệch giữa các báo cáo mâu thuẫn.

**Thiết kế.** Probe 2 của L037 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L037.2.** Đối soát `grain` bằng đường tính khác implementation chính của `reconciliation-and-the-discipline-of-verification`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3 — `identity`.** Chứng minh bằng hai đường không thực sự độc lập vì cùng dùng một nguồn trung gian · bỏ kiểm tra thứ nguyên · viết phần giới hạn mà không gắn với dữ liệu cụ thể.

**Thiết kế.** Probe 3 của L037 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L037.3.** Đối soát `identity` bằng đường tính khác implementation chính của `reconciliation-and-the-discipline-of-verification`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4 — `time cutoff`.** Nộp bản ghi điều tra truy được nguồn gốc cả ba khoản chênh lệch, hai đường chứng minh không dùng chung nguồn trung gian, và bản ghi qua được phản biện chéo. Đây là exit criterion của Module 4.

**Thiết kế.** Probe 4 của L037 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L037.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `reconciliation-and-the-discipline-of-verification`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5 — `missing versus zero`.** Bốn kỹ thuật đối soát: tổng kiểm tra, đối chiếu chéo giữa hai nguồn độc lập, kiểm tra biên, kiểm tra thứ nguyên. Ba phép kiểm tính hợp lý: bậc độ lớn, chiều xu hướng, tỉ lệ nội bộ giữa các thành phần. Cấu trúc bốn đoạn của phần giả định và giới hạn. Cách phát biểu mức độ không chắc chắn mà vẫn giữ được giá trị sử dụng của kết quả.

**Thiết kế.** Probe 5 của L037 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L037.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `reconciliation-and-the-discipline-of-verification`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6 — `duplicate`.** Chứng minh một kết quả bằng hai đường tính toán độc lập, và truy nguyên nguồn gốc của mọi khoản chênh lệch giữa các báo cáo mâu thuẫn.

**Thiết kế.** Probe 6 của L037 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L037.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `reconciliation-and-the-discipline-of-verification`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7 — `join fan-out`.** Chứng minh bằng hai đường không thực sự độc lập vì cùng dùng một nguồn trung gian · bỏ kiểm tra thứ nguyên · viết phần giới hạn mà không gắn với dữ liệu cụ thể.

**Thiết kế.** Probe 7 của L037 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L037.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `reconciliation-and-the-discipline-of-verification`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8 — `changed definition`.** Nộp bản ghi điều tra truy được nguồn gốc cả ba khoản chênh lệch, hai đường chứng minh không dùng chung nguồn trung gian, và bản ghi qua được phản biện chéo. Đây là exit criterion của Module 4.

**Thiết kế.** Probe 8 của L037 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L037.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `reconciliation-and-the-discipline-of-verification`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9 — `independent oracle`.** Bốn kỹ thuật đối soát: tổng kiểm tra, đối chiếu chéo giữa hai nguồn độc lập, kiểm tra biên, kiểm tra thứ nguyên. Ba phép kiểm tính hợp lý: bậc độ lớn, chiều xu hướng, tỉ lệ nội bộ giữa các thành phần. Cấu trúc bốn đoạn của phần giả định và giới hạn. Cách phát biểu mức độ không chắc chắn mà vẫn giữ được giá trị sử dụng của kết quả.

**Thiết kế.** Probe 9 của L037 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L037.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `reconciliation-and-the-discipline-of-verification`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10 — `replay`.** Chứng minh một kết quả bằng hai đường tính toán độc lập, và truy nguyên nguồn gốc của mọi khoản chênh lệch giữa các báo cáo mâu thuẫn.

**Thiết kế.** Probe 10 của L037 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L037.10.** Đối soát `replay` bằng đường tính khác implementation chính của `reconciliation-and-the-discipline-of-verification`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11 — `fresh snapshot`.** Chứng minh bằng hai đường không thực sự độc lập vì cùng dùng một nguồn trung gian · bỏ kiểm tra thứ nguyên · viết phần giới hạn mà không gắn với dữ liệu cụ thể.

**Thiết kế.** Probe 11 của L037 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L037.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `reconciliation-and-the-discipline-of-verification`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12 — `novel scenario`.** Nộp bản ghi điều tra truy được nguồn gốc cả ba khoản chênh lệch, hai đường chứng minh không dùng chung nguồn trung gian, và bản ghi qua được phản biện chéo. Đây là exit criterion của Module 4.

**Thiết kế.** Probe 12 của L037 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L037.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `reconciliation-and-the-discipline-of-verification`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L037?

<details><summary>Đáp án</summary>

Chứng minh một kết quả bằng hai đường tính toán độc lập, và truy nguyên nguồn gốc của mọi khoản chênh lệch giữa các báo cáo mâu thuẫn.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Chứng minh bằng hai đường không thực sự độc lập vì cùng dùng một nguồn trung gian · bỏ kiểm tra thứ nguyên · viết phần giới hạn mà không gắn với dữ liệu cụ thể.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Nộp bản ghi điều tra truy được nguồn gốc cả ba khoản chênh lệch, hai đường chứng minh không dùng chung nguồn trung gian, và bản ghi qua được phản biện chéo. Đây là exit criterion của Module 4.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.reconciliation-and-the-discipline-of-verification` đang `proposed`, chưa tính canonical coverage.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-KIMBALL-ROSS-DW-TOOLKIT-3E]] — `src.book.kimball-ross-data-warehouse-toolkit.3e`
2. [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]] — `src.book.silberschatz-database-system-concepts.7e`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-KIMBALL-ROSS-DW-TOOLKIT-3E]] — `src.book.kimball-ross-data-warehouse-toolkit.3e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Reconciliation and the discipline of verification | các mục cơ chế, case và probe | Đã phủ | ngoài objective L037 |
| [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]] — `src.book.silberschatz-database-system-concepts.7e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Reconciliation and the discipline of verification | các mục cơ chế, case và probe | Đã phủ | ngoài objective L037 |

## Key takeaways
- Chứng minh một kết quả bằng hai đường tính toán độc lập, và truy nguyên nguồn gốc của mọi khoản chênh lệch giữa các báo cáo mâu thuẫn.
- Nộp bản ghi điều tra truy được nguồn gốc cả ba khoản chênh lệch, hai đường chứng minh không dùng chung nguồn trung gian, và bản ghi qua được phản biện chéo. Đây là exit criterion của Module 4.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.
