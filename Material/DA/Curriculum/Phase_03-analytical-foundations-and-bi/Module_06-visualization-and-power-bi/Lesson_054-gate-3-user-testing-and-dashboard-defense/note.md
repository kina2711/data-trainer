# Phase 3: Data Analyst
# Module 6: Visualization and Power BI
# Lesson 54: Gate 3 - User testing and dashboard defense

## Mục tiêu bài học

**Năng lực cần chứng minh.** Chứng minh bằng quan sát rằng ba người chưa từng thấy dashboard trả lời được năm câu hỏi nghiệp vụ trên đó mà không cần hướng dẫn.

**Điều kiện hoàn thành.** ≥ 70/100 và phần A ≥ 60%. Không đạt thì làm lại với đề khác, theo phụ lục J. Đạt ≥ 70/100 và phần kiểm thử người dùng ≥ 60%. Đây là exit criterion của Module 6.

# Gate 3 - User testing and dashboard defense

**Tóm tắt bản chất:** Quy trình kiểm thử với người dùng thật: đưa dashboard cho ba người chưa từng thấy, giao năm câu hỏi nghiệp vụ, quan sát và ghi lại điểm vướng thay vì hỏi ý kiến. Tài liệu bắt buộc trong dashboard: định nghĩa chỉ số, ngày cập nhật, nguồn dữ liệu, giới hạn đã biết. Đo mức sử dụng và quy trình dừng một dashboard không còn ai mở. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Nỗi Đau & Động Lực

L054 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **Gate 3 - User testing and dashboard defense**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Chứng minh bằng quan sát rằng ba người chưa từng thấy dashboard trả lời được năm câu hỏi nghiệp vụ trên đó mà không cần hướng dẫn. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Cơ Chế Tác Động

Quy trình kiểm thử với người dùng thật: đưa dashboard cho ba người chưa từng thấy, giao năm câu hỏi nghiệp vụ, quan sát và ghi lại điểm vướng thay vì hỏi ý kiến. Tài liệu bắt buộc trong dashboard: định nghĩa chỉ số, ngày cập nhật, nguồn dữ liệu, giới hạn đã biết. Đo mức sử dụng và quy trình dừng một dashboard không còn ai mở.

Cơ chế của `gate-3-user-testing-and-dashboard-defense` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Hướng dẫn người dùng trong lúc kiểm thử nên kết quả không dùng được · hỏi ý kiến thay vì quan sát thao tác · bỏ phần tài liệu chỉ số. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Bản Đồ Quyết Định

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L054: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành “≥ 70/100 và phần A ≥ 60%. Không đạt thì làm lại với đề khác, theo phụ lục J. Đạt ≥ 70/100 và phần kiểm thử người dùng ≥ 60%. Đây là exit criterion của Module 6.”. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Case Study Thực Chiến: Gate 3 - User testing and dashboard defense

Bài thực hành dùng nhiệm vụ thật của roadmap: Phần A (30đ) kết quả kiểm thử với ba người dùng · Phần B (20đ) tài liệu chỉ số trong dashboard · Phần C (20đ) chất lượng thiết kế theo nguyên tắc lesson 46–48 · Phần D (15đ) hiệu năng đo được · Phần E (15đ) bảo vệ lựa chọn thiết kế dưới chất vấn.

Trước khi thao tác ở `Gate 3 - User testing and dashboard defense`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L054 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Output của `Gate 3 - User testing and dashboard defense` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Hướng dẫn người dùng trong lúc kiểm thử nên kết quả không dùng được · hỏi ý kiến thay vì quan sát thao tác · bỏ phần tài liệu chỉ số. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L054 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1 — `population`.** Quy trình kiểm thử với người dùng thật: đưa dashboard cho ba người chưa từng thấy, giao năm câu hỏi nghiệp vụ, quan sát và ghi lại điểm vướng thay vì hỏi ý kiến. Tài liệu bắt buộc trong dashboard: định nghĩa chỉ số, ngày cập nhật, nguồn dữ liệu, giới hạn đã biết. Đo mức sử dụng và quy trình dừng một dashboard không còn ai mở.

**Thiết kế.** Probe 1 của L054 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L054.1.** Đối soát `population` bằng đường tính khác implementation chính của `gate-3-user-testing-and-dashboard-defense`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2 — `grain`.** Chứng minh bằng quan sát rằng ba người chưa từng thấy dashboard trả lời được năm câu hỏi nghiệp vụ trên đó mà không cần hướng dẫn.

**Thiết kế.** Probe 2 của L054 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L054.2.** Đối soát `grain` bằng đường tính khác implementation chính của `gate-3-user-testing-and-dashboard-defense`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3 — `identity`.** Hướng dẫn người dùng trong lúc kiểm thử nên kết quả không dùng được · hỏi ý kiến thay vì quan sát thao tác · bỏ phần tài liệu chỉ số.

**Thiết kế.** Probe 3 của L054 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L054.3.** Đối soát `identity` bằng đường tính khác implementation chính của `gate-3-user-testing-and-dashboard-defense`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4 — `time cutoff`.** ≥ 70/100 và phần A ≥ 60%. Không đạt thì làm lại với đề khác, theo phụ lục J. Đạt ≥ 70/100 và phần kiểm thử người dùng ≥ 60%. Đây là exit criterion của Module 6.

**Thiết kế.** Probe 4 của L054 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L054.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `gate-3-user-testing-and-dashboard-defense`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5 — `missing versus zero`.** Quy trình kiểm thử với người dùng thật: đưa dashboard cho ba người chưa từng thấy, giao năm câu hỏi nghiệp vụ, quan sát và ghi lại điểm vướng thay vì hỏi ý kiến. Tài liệu bắt buộc trong dashboard: định nghĩa chỉ số, ngày cập nhật, nguồn dữ liệu, giới hạn đã biết. Đo mức sử dụng và quy trình dừng một dashboard không còn ai mở.

**Thiết kế.** Probe 5 của L054 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L054.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `gate-3-user-testing-and-dashboard-defense`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6 — `duplicate`.** Chứng minh bằng quan sát rằng ba người chưa từng thấy dashboard trả lời được năm câu hỏi nghiệp vụ trên đó mà không cần hướng dẫn.

**Thiết kế.** Probe 6 của L054 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L054.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `gate-3-user-testing-and-dashboard-defense`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7 — `join fan-out`.** Hướng dẫn người dùng trong lúc kiểm thử nên kết quả không dùng được · hỏi ý kiến thay vì quan sát thao tác · bỏ phần tài liệu chỉ số.

**Thiết kế.** Probe 7 của L054 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L054.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `gate-3-user-testing-and-dashboard-defense`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8 — `changed definition`.** ≥ 70/100 và phần A ≥ 60%. Không đạt thì làm lại với đề khác, theo phụ lục J. Đạt ≥ 70/100 và phần kiểm thử người dùng ≥ 60%. Đây là exit criterion của Module 6.

**Thiết kế.** Probe 8 của L054 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L054.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `gate-3-user-testing-and-dashboard-defense`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9 — `independent oracle`.** Quy trình kiểm thử với người dùng thật: đưa dashboard cho ba người chưa từng thấy, giao năm câu hỏi nghiệp vụ, quan sát và ghi lại điểm vướng thay vì hỏi ý kiến. Tài liệu bắt buộc trong dashboard: định nghĩa chỉ số, ngày cập nhật, nguồn dữ liệu, giới hạn đã biết. Đo mức sử dụng và quy trình dừng một dashboard không còn ai mở.

**Thiết kế.** Probe 9 của L054 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L054.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `gate-3-user-testing-and-dashboard-defense`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10 — `replay`.** Chứng minh bằng quan sát rằng ba người chưa từng thấy dashboard trả lời được năm câu hỏi nghiệp vụ trên đó mà không cần hướng dẫn.

**Thiết kế.** Probe 10 của L054 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L054.10.** Đối soát `replay` bằng đường tính khác implementation chính của `gate-3-user-testing-and-dashboard-defense`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11 — `fresh snapshot`.** Hướng dẫn người dùng trong lúc kiểm thử nên kết quả không dùng được · hỏi ý kiến thay vì quan sát thao tác · bỏ phần tài liệu chỉ số.

**Thiết kế.** Probe 11 của L054 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L054.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `gate-3-user-testing-and-dashboard-defense`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12 — `novel scenario`.** ≥ 70/100 và phần A ≥ 60%. Không đạt thì làm lại với đề khác, theo phụ lục J. Đạt ≥ 70/100 và phần kiểm thử người dùng ≥ 60%. Đây là exit criterion của Module 6.

**Thiết kế.** Probe 12 của L054 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L054.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `gate-3-user-testing-and-dashboard-defense`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L054?

<details><summary>Đáp án</summary>

Chứng minh bằng quan sát rằng ba người chưa từng thấy dashboard trả lời được năm câu hỏi nghiệp vụ trên đó mà không cần hướng dẫn.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Hướng dẫn người dùng trong lúc kiểm thử nên kết quả không dùng được · hỏi ý kiến thay vì quan sát thao tác · bỏ phần tài liệu chỉ số.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

≥ 70/100 và phần A ≥ 60%. Không đạt thì làm lại với đề khác, theo phụ lục J. Đạt ≥ 70/100 và phần kiểm thử người dùng ≥ 60%. Đây là exit criterion của Module 6.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.gate-3-user-testing-and-dashboard-defense` đang `proposed`, chưa tính canonical coverage.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-STORYTELLING-WITH-DATA]] — `src.book.knaflic-storytelling-with-data.1e`
2. [[SRC-DEFINITIVE-GUIDE-DAX-3E]] — `src.book.ferrari-russo-definitive-guide-dax.3e`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-STORYTELLING-WITH-DATA]] — `src.book.knaflic-storytelling-with-data.1e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Gate 3 - User testing and dashboard defense | các mục cơ chế, case và probe | Đã phủ | ngoài objective L054 |
| [[SRC-DEFINITIVE-GUIDE-DAX-3E]] — `src.book.ferrari-russo-definitive-guide-dax.3e` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Gate 3 - User testing and dashboard defense | các mục cơ chế, case và probe | Đã phủ | ngoài objective L054 |

## Key takeaways
- Chứng minh bằng quan sát rằng ba người chưa từng thấy dashboard trả lời được năm câu hỏi nghiệp vụ trên đó mà không cần hướng dẫn.
- ≥ 70/100 và phần A ≥ 60%. Không đạt thì làm lại với đề khác, theo phụ lục J. Đạt ≥ 70/100 và phần kiểm thử người dùng ≥ 60%. Đây là exit criterion của Module 6.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.
