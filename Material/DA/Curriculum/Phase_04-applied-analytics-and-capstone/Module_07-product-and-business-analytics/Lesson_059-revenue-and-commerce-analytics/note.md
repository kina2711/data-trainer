# Phase 4: Data Analyst
# Module 7: Product and Business Analytics
# Lesson 59: Revenue and commerce analytics

## Mục tiêu bài học

**Năng lực cần chứng minh.** Phân rã doanh thu theo bốn thành phần và kết luận một chương trình khuyến mại tạo thêm doanh thu hay chỉ dịch chuyển thời điểm mua, kèm định lượng phần ăn mòn.

**Điều kiện hoàn thành.** Bốn thành phần nhân lại bằng đúng tổng doanh thu, và kết luận về khuyến mại có kèm con số ăn mòn định lượng được.

# Revenue and commerce analytics

**Tóm tắt bản chất:** Phân rã doanh thu thành bốn thành phần nhân được: số khách × tần suất × giá trị đơn × biên lợi nhuận. Phân tích giá và độ co giãn ở mức mô tả. Phân tích giỏ hàng và bán kèm. Phân tích khuyến mại: tách doanh thu tăng thêm khỏi doanh thu bị ăn mòn, và cơ chế khiến phần ăn mòn thường không được tính. Giá trị vòng đời khách hàng ở mức mô tả. Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.

## Nỗi Đau & Động Lực

L059 bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **Revenue and commerce analytics**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.

Roadmap đặt chuẩn đầu ra như sau: Phân rã doanh thu theo bốn thành phần và kết luận một chương trình khuyến mại tạo thêm doanh thu hay chỉ dịch chuyển thời điểm mua, kèm định lượng phần ăn mòn. Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.

## Cơ Chế Tác Động

Phân rã doanh thu thành bốn thành phần nhân được: số khách × tần suất × giá trị đơn × biên lợi nhuận. Phân tích giá và độ co giãn ở mức mô tả. Phân tích giỏ hàng và bán kèm. Phân tích khuyến mại: tách doanh thu tăng thêm khỏi doanh thu bị ăn mòn, và cơ chế khiến phần ăn mòn thường không được tính. Giá trị vòng đời khách hàng ở mức mô tả.

Cơ chế của `revenue-and-commerce-analytics` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.

Lỗi cần loại trừ trong bài này là: Báo cáo doanh thu tăng thêm mà không trừ ăn mòn · phân rã thành các thành phần không nhân được với nhau · so sánh kỳ khuyến mại với kỳ liền trước mà không xét mùa vụ. Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.

## Bản Đồ Quyết Định

| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |
|---|---|---|
| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |
| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |
| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |
| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |
| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |

Quy tắc của L059: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành “Bốn thành phần nhân lại bằng đúng tổng doanh thu, và kết luận về khuyến mại có kèm con số ăn mòn định lượng được.”. Không dùng độ phức tạp để che một câu hỏi chưa rõ.

## Case Study Thực Chiến: Revenue and commerce analytics

Bài thực hành dùng nhiệm vụ thật của roadmap: Phân rã doanh thu `DS2` theo bốn thành phần. Đánh giá một đợt khuyến mại, có tính và trừ phần doanh thu bị ăn mòn.

Trước khi thao tác ở `Revenue and commerce analytics`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.

Biến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L059 chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Output của `Revenue and commerce analytics` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.

**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.

**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** Báo cáo doanh thu tăng thêm mà không trừ ăn mòn · phân rã thành các thành phần không nhân được với nhau · so sánh kỳ khuyến mại với kỳ liền trước mà không xét mùa vụ. **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.

## Nếu Bạn Dạy Lại Điều Này...

Mở đầu L059 bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.

## Ma trận kiểm chứng

### Probe 1: population

**Mệnh đề của probe 1 — `population`.** Phân rã doanh thu thành bốn thành phần nhân được: số khách × tần suất × giá trị đơn × biên lợi nhuận. Phân tích giá và độ co giãn ở mức mô tả. Phân tích giỏ hàng và bán kèm. Phân tích khuyến mại: tách doanh thu tăng thêm khỏi doanh thu bị ăn mòn, và cơ chế khiến phần ăn mòn thường không được tính. Giá trị vòng đời khách hàng ở mức mô tả.

**Thiết kế.** Probe 1 của L059 tạo fixture nhỏ cho `population` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L059.1.** Đối soát `population` bằng đường tính khác implementation chính của `revenue-and-commerce-analytics`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 2: grain

**Mệnh đề của probe 2 — `grain`.** Phân rã doanh thu theo bốn thành phần và kết luận một chương trình khuyến mại tạo thêm doanh thu hay chỉ dịch chuyển thời điểm mua, kèm định lượng phần ăn mòn.

**Thiết kế.** Probe 2 của L059 tạo fixture nhỏ cho `grain` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L059.2.** Đối soát `grain` bằng đường tính khác implementation chính của `revenue-and-commerce-analytics`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 3: identity

**Mệnh đề của probe 3 — `identity`.** Báo cáo doanh thu tăng thêm mà không trừ ăn mòn · phân rã thành các thành phần không nhân được với nhau · so sánh kỳ khuyến mại với kỳ liền trước mà không xét mùa vụ.

**Thiết kế.** Probe 3 của L059 tạo fixture nhỏ cho `identity` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L059.3.** Đối soát `identity` bằng đường tính khác implementation chính của `revenue-and-commerce-analytics`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 4: time cutoff

**Mệnh đề của probe 4 — `time cutoff`.** Bốn thành phần nhân lại bằng đúng tổng doanh thu, và kết luận về khuyến mại có kèm con số ăn mòn định lượng được.

**Thiết kế.** Probe 4 của L059 tạo fixture nhỏ cho `time cutoff` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L059.4.** Đối soát `time cutoff` bằng đường tính khác implementation chính của `revenue-and-commerce-analytics`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 5: missing versus zero

**Mệnh đề của probe 5 — `missing versus zero`.** Phân rã doanh thu thành bốn thành phần nhân được: số khách × tần suất × giá trị đơn × biên lợi nhuận. Phân tích giá và độ co giãn ở mức mô tả. Phân tích giỏ hàng và bán kèm. Phân tích khuyến mại: tách doanh thu tăng thêm khỏi doanh thu bị ăn mòn, và cơ chế khiến phần ăn mòn thường không được tính. Giá trị vòng đời khách hàng ở mức mô tả.

**Thiết kế.** Probe 5 của L059 tạo fixture nhỏ cho `missing versus zero` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L059.5.** Đối soát `missing versus zero` bằng đường tính khác implementation chính của `revenue-and-commerce-analytics`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 6: duplicate

**Mệnh đề của probe 6 — `duplicate`.** Phân rã doanh thu theo bốn thành phần và kết luận một chương trình khuyến mại tạo thêm doanh thu hay chỉ dịch chuyển thời điểm mua, kèm định lượng phần ăn mòn.

**Thiết kế.** Probe 6 của L059 tạo fixture nhỏ cho `duplicate` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L059.6.** Đối soát `duplicate` bằng đường tính khác implementation chính của `revenue-and-commerce-analytics`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 7: join fan-out

**Mệnh đề của probe 7 — `join fan-out`.** Báo cáo doanh thu tăng thêm mà không trừ ăn mòn · phân rã thành các thành phần không nhân được với nhau · so sánh kỳ khuyến mại với kỳ liền trước mà không xét mùa vụ.

**Thiết kế.** Probe 7 của L059 tạo fixture nhỏ cho `join fan-out` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L059.7.** Đối soát `join fan-out` bằng đường tính khác implementation chính của `revenue-and-commerce-analytics`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 8: changed definition

**Mệnh đề của probe 8 — `changed definition`.** Bốn thành phần nhân lại bằng đúng tổng doanh thu, và kết luận về khuyến mại có kèm con số ăn mòn định lượng được.

**Thiết kế.** Probe 8 của L059 tạo fixture nhỏ cho `changed definition` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L059.8.** Đối soát `changed definition` bằng đường tính khác implementation chính của `revenue-and-commerce-analytics`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 9: independent oracle

**Mệnh đề của probe 9 — `independent oracle`.** Phân rã doanh thu thành bốn thành phần nhân được: số khách × tần suất × giá trị đơn × biên lợi nhuận. Phân tích giá và độ co giãn ở mức mô tả. Phân tích giỏ hàng và bán kèm. Phân tích khuyến mại: tách doanh thu tăng thêm khỏi doanh thu bị ăn mòn, và cơ chế khiến phần ăn mòn thường không được tính. Giá trị vòng đời khách hàng ở mức mô tả.

**Thiết kế.** Probe 9 của L059 tạo fixture nhỏ cho `independent oracle` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L059.9.** Đối soát `independent oracle` bằng đường tính khác implementation chính của `revenue-and-commerce-analytics`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 10: replay

**Mệnh đề của probe 10 — `replay`.** Phân rã doanh thu theo bốn thành phần và kết luận một chương trình khuyến mại tạo thêm doanh thu hay chỉ dịch chuyển thời điểm mua, kèm định lượng phần ăn mòn.

**Thiết kế.** Probe 10 của L059 tạo fixture nhỏ cho `replay` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L059.10.** Đối soát `replay` bằng đường tính khác implementation chính của `revenue-and-commerce-analytics`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 11: fresh snapshot

**Mệnh đề của probe 11 — `fresh snapshot`.** Báo cáo doanh thu tăng thêm mà không trừ ăn mòn · phân rã thành các thành phần không nhân được với nhau · so sánh kỳ khuyến mại với kỳ liền trước mà không xét mùa vụ.

**Thiết kế.** Probe 11 của L059 tạo fixture nhỏ cho `fresh snapshot` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L059.11.** Đối soát `fresh snapshot` bằng đường tính khác implementation chính của `revenue-and-commerce-analytics`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

### Probe 12: novel scenario

**Mệnh đề của probe 12 — `novel scenario`.** Bốn thành phần nhân lại bằng đúng tổng doanh thu, và kết luận về khuyến mại có kèm con số ăn mòn định lượng được.

**Thiết kế.** Probe 12 của L059 tạo fixture nhỏ cho `novel scenario` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.

**Oracle L059.12.** Đối soát `novel scenario` bằng đường tính khác implementation chính của `revenue-and-commerce-analytics`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Năng lực nào phải chứng minh ở L059?

<details><summary>Đáp án</summary>

Phân rã doanh thu theo bốn thành phần và kết luận một chương trình khuyến mại tạo thêm doanh thu hay chỉ dịch chuyển thời điểm mua, kèm định lượng phần ăn mòn.

</details>

2. Failure nào phải chủ động cài vào fixture?

<details><summary>Đáp án</summary>

Báo cáo doanh thu tăng thêm mà không trừ ăn mòn · phân rã thành các thành phần không nhân được với nhau · so sánh kỳ khuyến mại với kỳ liền trước mà không xét mùa vụ.

</details>

3. Khi nào bài được xem là hoàn thành?

<details><summary>Đáp án</summary>

Bốn thành phần nhân lại bằng đúng tổng doanh thu, và kết luận về khuyến mại có kèm con số ăn mòn định lượng được.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case và probe là protocol giảng dạy; chưa phải quan sát production.
- Con số minh họa không phải benchmark ngành.
- Concept key `ck.da.revenue-and-commerce-analytics` đang `proposed`, chưa tính canonical coverage.
- Note tồn tại không phải bằng chứng learner đã thành thạo.

## Reference
1. [[SRC-AMPLITUDE-NORTH-STAR-FRAMEWORK]] — `src.web.amplitude-north-star-framework`
2. [[SRC-GOOGLE-HEART-UX-METRICS]] — `src.paper.google-heart-ux-metrics`

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-AMPLITUDE-NORTH-STAR-FRAMEWORK]] — `src.web.amplitude-north-star-framework` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Revenue and commerce analytics | các mục cơ chế, case và probe | Đã phủ | ngoài objective L059 |
| [[SRC-GOOGLE-HEART-UX-METRICS]] — `src.paper.google-heart-ux-metrics` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới Revenue and commerce analytics | các mục cơ chế, case và probe | Đã phủ | ngoài objective L059 |

## Key takeaways
- Phân rã doanh thu theo bốn thành phần và kết luận một chương trình khuyến mại tạo thêm doanh thu hay chỉ dịch chuyển thời điểm mua, kèm định lượng phần ăn mòn.
- Bốn thành phần nhân lại bằng đúng tổng doanh thu, và kết luận về khuyến mại có kèm con số ăn mòn định lượng được.
- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.
- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.
