# Phase 2: Machine, Operating System and Network
# Module 4: Computer Architecture and the Performance Model
# Lesson 52: Storage - sequential against random, and the device model

## Mục tiêu bài học

**Năng lực cần chứng minh.** Đo được ba đại lượng của thiết bị lưu trữ và chỉ ra chênh lệch giữa đọc tuần tự với đọc ngẫu nhiên trên chính máy mình.

**Điều kiện hoàn thành.** Bảng bốn cấu hình đủ ba đại lượng, chênh lệch tuần tự so với ngẫu nhiên đúng chiều, và đồ thị ghi liên tục cho thấy mức tụt.

**Kiến thức và cơ chế.** Đĩa quay và đĩa thể rắn khác nhau về cơ chế nên khác nhau về hình dạng chi phí, và biết khác biệt đó quyết định nhiều thiết kế. Đĩa quay phải quay và dịch đầu đọc nên đọc ngẫu nhiên đắt hơn tuần tự nhiều bậc độ lớn; tỉ số cụ thể do tốc độ quay và thời gian dịch đầu đọc của từng thiết bị quyết định, và lab bài này đo trên thiết bị đang có. Đĩa thể rắn không có bộ phận cơ nên đọc ngẫu nhiên rẻ hơn nhiều, nhưng vẫn có ba đặc tính phải biết: đơn vị đọc là trang còn đơn vị xoá là khối lớn hơn nhiều, nên ghi đè sinh ra khuếch đại ghi; hiệu năng phụ thuộc độ sâu hàng đợi nên một luồng không khai thác hết; và ghi liên tục lâu dài làm tốc độ tụt khi bộ gom rác bên trong phải chạy. Ba đại lượng đo khác nhau và hay bị gộp: số thao tác mỗi giây, thông lượng byte, và độ trễ; một thiết bị có thể tốt ở đại lượng này và tệ ở đại lượng kia. Nối tới M15: đây là lý do tệp nhỏ đắt và tệp lớn rẻ trên kho đối tượng.


# Storage - sequential against random, and the device model

**Tóm tắt bản chất:** Đo được ba đại lượng của thiết bị lưu trữ và chỉ ra chênh lệch giữa đọc tuần tự với đọc ngẫu nhiên trên chính máy mình. Cơ chế chỉ có giá trị khi workload, version, state owner và failure boundary đã được khóa; một con số đẹp ngoài bốn điều kiện đó không đủ để ra quyết định.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, đo và ra quyết định đúng về Storage - sequential against random, and the device model?

## Nỗi Đau & Động Lực

Đo với tệp nhỏ hơn bộ đệm trang nên chỉ đo RAM · đo ở một độ sâu hàng đợi rồi kết luận · gộp ba đại lượng làm một · tin thông số nhà sản xuất mà không đo. Đây không phải danh sách lỗi cú pháp. Mỗi lỗi làm người vận hành chọn nhầm owner hoặc chữa symptom ở layer sau, khiến thời gian phục hồi tăng dù command vừa chạy trả về thành công.

Năng lực cần giữ sau bài là: Đo được ba đại lượng của thiết bị lưu trữ và chỉ ra chênh lệch giữa đọc tuần tự với đọc ngẫu nhiên trên chính máy mình. Nếu learner chỉ nhắc lại định nghĩa nhưng không phân biệt được hai state gần nhau trên số đo, bài chưa đạt.

## Cơ Chế Tác Động

Đĩa quay và đĩa thể rắn khác nhau về cơ chế nên khác nhau về hình dạng chi phí, và biết khác biệt đó quyết định nhiều thiết kế. Đĩa quay phải quay và dịch đầu đọc nên đọc ngẫu nhiên đắt hơn tuần tự nhiều bậc độ lớn; tỉ số cụ thể do tốc độ quay và thời gian dịch đầu đọc của từng thiết bị quyết định, và lab bài này đo trên thiết bị đang có. Đĩa thể rắn không có bộ phận cơ nên đọc ngẫu nhiên rẻ hơn nhiều, nhưng vẫn có ba đặc tính phải biết: đơn vị đọc là trang còn đơn vị xoá là khối lớn hơn nhiều, nên ghi đè sinh ra khuếch đại ghi; hiệu năng phụ thuộc độ sâu hàng đợi nên một luồng không khai thác hết; và ghi liên tục lâu dài làm tốc độ tụt khi bộ gom rác bên trong phải chạy. Ba đại lượng đo khác nhau và hay bị gộp: số thao tác mỗi giây, thông lượng byte, và độ trễ; một thiết bị có thể tốt ở đại lượng này và tệ ở đại lượng kia. Nối tới M15: đây là lý do tệp nhỏ đắt và tệp lớn rẻ trên kho đối tượng.

Tách ba lớp khi đọc cơ chế `wiki.de-foundation.storage-sequential-against-random-and-the-device-model`: declared state là điều cấu hình hoặc API yêu cầu; executed state là việc runtime thực sự làm; consumer-visible state là điều client hay operator quan sát. Ba lớp có thể lệch nhau vì cache, buffering, retry, scheduling, queue hoặc failure giữa hai transition. Evidence phải chỉ ra lớp nào đang được đo.

## Bản Đồ Quyết Định

| Bước | Câu hỏi phải khóa | Điều kiện đạt |
|---|---|---|
| Model | Giải thích chi phí bằng hierarchy, parallel fraction hoặc data movement | Model dự đoán đúng khi đổi scale |
| Measure | Dùng counter và benchmark khóa workload | Observation khớp oracle và có raw sample |
| Explain | Nối delta với mechanism | Reviewer tái hiện được reasoning |
| Reverse | Đổi workload, layout hoặc resource | Quyết định đổi khi bottleneck đổi |

Quy tắc mặc định là chọn phép giải thích đơn giản nhất qua được hard constraints, rồi viết trước reversal trigger. Với `Storage - sequential against random, and the device model`, absence of error không phải pass; pass cần observation đúng grain, một oracle độc lập và changed-constraint case đủ làm model có cơ hội thất bại.

## Case Study Thực Chiến: Storage - sequential against random, and the device model

Đo đọc tuần tự và đọc ngẫu nhiên ở hai độ sâu hàng đợi, ghi cả ba đại lượng cho mỗi cấu hình. Tính tỉ lệ chênh lệch. Chạy ghi liên tục 10 phút và vẽ tốc độ theo thời gian để quan sát mức tụt. So kết quả với thông số nhà sản xuất công bố.

Trong case `wiki.de-foundation.storage-sequential-against-random-and-the-device-model`, learner ghi expected transition, input snapshot, version và giới hạn an toàn trước khi chạy. Sau execution, họ giữ raw counter, timestamp, exit status, state trước–sau và giải thích delta bằng mechanism ở trên. Đánh giá không cho phép sửa expected result sau khi nhìn output mà không ghi change record.

Biến thể khó hơn đổi một constraint có khả năng đảo kết luận: workload shape, memory pressure, connection reuse, retry budget, permission hoặc dependency direction. Tầng *áp dụng*. Objective là một phép đo theo quy trình cộng đọc kết quả đúng. Kiểm bằng bảng đo bốn cấu hình; đạt khi cả ba đại lượng có số và chênh lệch tuần tự so với ngẫu nhiên đúng chiều.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Đo với tệp nhỏ hơn bộ đệm trang nên chỉ đo RAM. **Thực tế:** tín hiệu chỉ chứng minh điều nó đo trong đúng scope; state ở layer khác vẫn có thể trái ngược. **Vì sao nghe hợp lý:** happy path nhỏ thường không chạm queue, cache, partial progress hoặc restart.

**Hiểu lầm:** đo ở một độ sâu hàng đợi rồi kết luận. **Thực tế:** tool và API cung cấp primitive, không tự cấp ownership, deadline, idempotency hay recovery policy. **Vì sao nghe hợp lý:** syntax gọn che mất protocol và lifecycle phía dưới.

Với `wiki.de-foundation.storage-sequential-against-random-and-the-device-model`, một edge case đáng giữ là observation đúng nhưng diagnosis sai: counter tăng thật, song nguyên nhân điều khiển nằm ở layer trước. Muốn tránh, timeline phải nối trigger tới consumer harm và ghi rõ negative control nào đã loại giả thuyết cạnh tranh.

## Nếu Bạn Dạy Lại Điều Này...

Mở bài bằng một dự đoán dễ sai về `Storage - sequential against random, and the device model`, không mở bằng định nghĩa. Cho hai trace gần giống nhau nhưng khác đúng một state boundary; learner phải chọn probe tiếp theo trước khi được xem đáp án.

Bài tập seed dùng chính lab của DE-L052, sau đó đổi constraint đủ mạnh để buộc giữ hoặc đảo quyết định. Người dạy chấm reasoning chain và evidence, không chấm việc learner đoán đúng tên công cụ.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `Storage - sequential against random, and the device model` dùng điều kiện hoàn thành sau: Bảng bốn cấu hình đủ ba đại lượng, chênh lệch tuần tự so với ngẫu nhiên đúng chiều, và đồ thị ghi liên tục cho thấy mức tụt. Mỗi probe phải có prediction, failure signal và independent oracle.

### Probe 1: state transition và invariant

**Mệnh đề P1 cần kiểm.** Đĩa quay và đĩa thể rắn khác nhau về cơ chế nên khác nhau về hình dạng chi phí, và biết khác biệt đó quyết định nhiều thiết kế.

**Thiết kế phép thử.** Với `wiki.de-foundation.storage-sequential-against-random-and-the-device-model`, tạo positive và negative control chỉ khác một điều kiện; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P1 cần giữ.** Với `wiki.de-foundation.storage-sequential-against-random-and-the-device-model`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề P2 cần kiểm.** Đo được ba đại lượng của thiết bị lưu trữ và chỉ ra chênh lệch giữa đọc tuần tự với đọc ngẫu nhiên trên chính máy mình.

**Thiết kế phép thử.** Với `wiki.de-foundation.storage-sequential-against-random-and-the-device-model`, tạo boundary case ngay trước và sau ngưỡng; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P2 cần giữ.** Với `wiki.de-foundation.storage-sequential-against-random-and-the-device-model`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề P3 cần kiểm.** Tầng *áp dụng*.

**Thiết kế phép thử.** Với `wiki.de-foundation.storage-sequential-against-random-and-the-device-model`, tạo replay cùng identity nhưng đổi state; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P3 cần giữ.** Với `wiki.de-foundation.storage-sequential-against-random-and-the-device-model`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề P4 cần kiểm.** Đo đọc tuần tự và đọc ngẫu nhiên ở hai độ sâu hàng đợi, ghi cả ba đại lượng cho mỗi cấu hình.

**Thiết kế phép thử.** Với `wiki.de-foundation.storage-sequential-against-random-and-the-device-model`, tạo failure inject trước và sau transition bền vững; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P4 cần giữ.** Với `wiki.de-foundation.storage-sequential-against-random-and-the-device-model`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề P5 cần kiểm.** Đo với tệp nhỏ hơn bộ đệm trang nên chỉ đo RAM · đo ở một độ sâu hàng đợi rồi kết luận · gộp ba đại lượng làm một · tin thông số nhà sản xuất mà không đo.

**Thiết kế phép thử.** Với `wiki.de-foundation.storage-sequential-against-random-and-the-device-model`, tạo changed scale làm cost model đổi; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P5 cần giữ.** Với `wiki.de-foundation.storage-sequential-against-random-and-the-device-model`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề P6 cần kiểm.** Bảng bốn cấu hình đủ ba đại lượng, chênh lệch tuần tự so với ngẫu nhiên đúng chiều, và đồ thị ghi liên tục cho thấy mức tụt.

**Thiết kế phép thử.** Với `wiki.de-foundation.storage-sequential-against-random-and-the-device-model`, tạo adversarial order, skew hoặc packet timing; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P6 cần giữ.** Với `wiki.de-foundation.storage-sequential-against-random-and-the-device-model`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề P7 cần kiểm.** Đĩa quay và đĩa thể rắn khác nhau về cơ chế nên khác nhau về hình dạng chi phí, và biết khác biệt đó quyết định nhiều thiết kế.

**Thiết kế phép thử.** Với `wiki.de-foundation.storage-sequential-against-random-and-the-device-model`, tạo fresh environment không cache; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P7 cần giữ.** Với `wiki.de-foundation.storage-sequential-against-random-and-the-device-model`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề P8 cần kiểm.** Đo được ba đại lượng của thiết bị lưu trữ và chỉ ra chênh lệch giữa đọc tuần tự với đọc ngẫu nhiên trên chính máy mình.

**Thiết kế phép thử.** Với `wiki.de-foundation.storage-sequential-against-random-and-the-device-model`, tạo independent oracle không dùng chung implementation; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P8 cần giữ.** Với `wiki.de-foundation.storage-sequential-against-random-and-the-device-model`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề P9 cần kiểm.** Tầng *áp dụng*.

**Thiết kế phép thử.** Với `wiki.de-foundation.storage-sequential-against-random-and-the-device-model`, tạo partial progress rồi restart; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P9 cần giữ.** Với `wiki.de-foundation.storage-sequential-against-random-and-the-device-model`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề P10 cần kiểm.** Đo đọc tuần tự và đọc ngẫu nhiên ở hai độ sâu hàng đợi, ghi cả ba đại lượng cho mỗi cấu hình.

**Thiết kế phép thử.** Với `wiki.de-foundation.storage-sequential-against-random-and-the-device-model`, tạo missing evidence phải abstain; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P10 cần giữ.** Với `wiki.de-foundation.storage-sequential-against-random-and-the-device-model`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề P11 cần kiểm.** Đo với tệp nhỏ hơn bộ đệm trang nên chỉ đo RAM · đo ở một độ sâu hàng đợi rồi kết luận · gộp ba đại lượng làm một · tin thông số nhà sản xuất mà không đo.

**Thiết kế phép thử.** Với `wiki.de-foundation.storage-sequential-against-random-and-the-device-model`, tạo reviewer tái hiện từ evidence package; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P11 cần giữ.** Với `wiki.de-foundation.storage-sequential-against-random-and-the-device-model`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề P12 cần kiểm.** Bảng bốn cấu hình đủ ba đại lượng, chênh lệch tuần tự so với ngẫu nhiên đúng chiều, và đồ thị ghi liên tục cho thấy mức tụt.

**Thiết kế phép thử.** Với `wiki.de-foundation.storage-sequential-against-random-and-the-device-model`, tạo constraint đổi đủ để quyết định đảo; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P12 cần giữ.** Với `wiki.de-foundation.storage-sequential-against-random-and-the-device-model`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên khiến mô hình `Storage - sequential against random, and the device model` không còn đúng là gì?

<details><summary>Đáp án</summary>Đo với tệp nhỏ hơn bộ đệm trang nên chỉ đo RAM · đo ở một độ sâu hàng đợi rồi kết luận · gộp ba đại lượng làm một · tin thông số nhà sản xuất mà không đo.</details>

2. Evidence nào phân biệt được hai state dễ nhầm?

<details><summary>Đáp án</summary>Tầng *áp dụng*. Objective là một phép đo theo quy trình cộng đọc kết quả đúng. Kiểm bằng bảng đo bốn cấu hình; đạt khi cả ba đại lượng có số và chênh lệch tuần tự so với ngẫu nhiên đúng chiều.</details>

3. Khi constraint đổi, điều gì quyết định giữ hay đảo lựa chọn?

<details><summary>Đáp án</summary>Bảng bốn cấu hình đủ ba đại lượng, chênh lệch tuần tự so với ngẫu nhiên đúng chiều, và đồ thị ghi liên tục cho thấy mức tụt.</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `Storage - sequential against random, and the device model` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Hành vi phụ thuộc kernel, distribution, library, network path hoặc hardware phải được kiểm lại trên target đã ghi version.
- Concept key `ck.de.storage-sequential-against-random-and-the-device-model` đang ở trạng thái `proposed`; note chưa được tính là canonical registry coverage.
- Một trace đơn lẻ không chứng minh capacity, reliability hoặc security cho population khác.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-TLPI-2010]]
2. [[SRC-PATTERSON-HENNESSY-COD-5E]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-TLPI-2010]] — `src.book.tlpi.2010` | Chapters 4–39, 49–50, 61 và 63 theo scope record; PDF 113–1418 | mechanism và boundary liên quan trực tiếp tới `Storage - sequential against random, and the device model` | cơ chế, quyết định, case và probe | Đã phủ | phần ngoài objective DE-L052 |
| [[SRC-PATTERSON-HENNESSY-COD-5E]] — `src.book.patterson-hennessy-cod.5e` | Chapter 5 và §6.3; PDF 397–538 | mechanism và boundary liên quan trực tiếp tới `Storage - sequential against random, and the device model` | cơ chế, quyết định, case và probe | Đã phủ | phần ngoài objective DE-L052 |

## Key takeaways
- Đo được ba đại lượng của thiết bị lưu trữ và chỉ ra chênh lệch giữa đọc tuần tự với đọc ngẫu nhiên trên chính máy mình.
- Bảng bốn cấu hình đủ ba đại lượng, chênh lệch tuần tự so với ngẫu nhiên đúng chiều, và đồ thị ghi liên tục cho thấy mức tụt.
- `Storage - sequential against random, and the device model` chỉ có nghĩa trong scope, state, identity và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.
