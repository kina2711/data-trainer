# Phase 2: Machine, Operating System and Network
# Module 6: Networking from Packet to API
# Lesson 84: Designing an API client for data ingestion

## Mục tiêu bài học

**Năng lực cần chứng minh.** Viết trình gọi đạt sáu yêu cầu và chứng minh nó nạp đủ, không trùng, dưới điều kiện nguồn lỗi và giới hạn tốc độ.

**Điều kiện hoàn thành.** Đối soát khớp tuyệt đối dưới cả ba điều kiện lỗi, và sau khi giết tiến trình thì lần chạy sau tiếp tục đúng chỗ.

**Kiến thức và cơ chế.** Bài ghép, và kết quả của nó được dùng lại nguyên vẹn ở M16. Sáu yêu cầu của một trình gọi giao diện lập trình web dùng để nạp dữ liệu. Ba hạn chờ theo lesson 83. Thử lại có lùi và nhiễu, chỉ cho lỗi đáng thử lại theo lesson 81. Tôn trọng giới hạn tốc độ bằng cách đọc tiêu đề máy chủ trả về chứ đoán. Phân trang: ba kiểu phân trang và **vì sao phân trang theo số trang không an toàn khi dữ liệu đang thay đổi**, một chi tiết sẽ quay lại ở M16. Khoá bất biến khi ghi để thử lại không sinh trùng. Và ghi nhật ký có mã theo dõi theo lesson 20 để truy ngược được. Kèm theo là một phần thường bị bỏ: lưu trạng thái đã nạp tới đâu để lần chạy sau tiếp tục được thay vì bắt đầu lại.


# Designing an API client for data ingestion

**Tóm tắt bản chất:** Viết trình gọi đạt sáu yêu cầu và chứng minh nó nạp đủ, không trùng, dưới điều kiện nguồn lỗi và giới hạn tốc độ. Cơ chế chỉ có giá trị khi workload, version, state owner và failure boundary đã được khóa; một con số đẹp ngoài bốn điều kiện đó không đủ để ra quyết định.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, đo và ra quyết định đúng về Designing an API client for data ingestion?

## Nỗi Đau & Động Lực

Phân trang theo số trang trên dữ liệu đang đổi · thử lại mà không có khoá bất biến · đoán thời gian chờ thay vì đọc tiêu đề · không lưu trạng thái nên chạy lại từ đầu. Đây không phải danh sách lỗi cú pháp. Mỗi lỗi làm người vận hành chọn nhầm owner hoặc chữa symptom ở layer sau, khiến thời gian phục hồi tăng dù command vừa chạy trả về thành công.

Năng lực cần giữ sau bài là: Viết trình gọi đạt sáu yêu cầu và chứng minh nó nạp đủ, không trùng, dưới điều kiện nguồn lỗi và giới hạn tốc độ. Nếu learner chỉ nhắc lại định nghĩa nhưng không phân biệt được hai state gần nhau trên số đo, bài chưa đạt.

## Cơ Chế Tác Động

Bài ghép, và kết quả của nó được dùng lại nguyên vẹn ở M16. Sáu yêu cầu của một trình gọi giao diện lập trình web dùng để nạp dữ liệu. Ba hạn chờ theo lesson 83. Thử lại có lùi và nhiễu, chỉ cho lỗi đáng thử lại theo lesson 81. Tôn trọng giới hạn tốc độ bằng cách đọc tiêu đề máy chủ trả về chứ đoán. Phân trang: ba kiểu phân trang và **vì sao phân trang theo số trang không an toàn khi dữ liệu đang thay đổi**, một chi tiết sẽ quay lại ở M16. Khoá bất biến khi ghi để thử lại không sinh trùng. Và ghi nhật ký có mã theo dõi theo lesson 20 để truy ngược được. Kèm theo là một phần thường bị bỏ: lưu trạng thái đã nạp tới đâu để lần chạy sau tiếp tục được thay vì bắt đầu lại.

Tách ba lớp khi đọc cơ chế `wiki.de-foundation.designing-an-api-client-for-data-ingestion`: declared state là điều cấu hình hoặc API yêu cầu; executed state là việc runtime thực sự làm; consumer-visible state là điều client hay operator quan sát. Ba lớp có thể lệch nhau vì cache, buffering, retry, scheduling, queue hoặc failure giữa hai transition. Evidence phải chỉ ra lớp nào đang được đo.

## Bản Đồ Quyết Định

| Bước | Câu hỏi phải khóa | Điều kiện đạt |
|---|---|---|
| Layer | Xác định hop và protocol state | Không gọi mọi lỗi là network |
| Budget | Chia deadline và capacity theo hop | Không reset budget sau retry |
| Identity | Khóa connection, request và operation identity | Không gộp duplicate với retry |
| Evidence | Ghép client, DNS, transport, TLS, HTTP và server timeline | Clock và correlation được công bố |

Quy tắc mặc định là chọn phép giải thích đơn giản nhất qua được hard constraints, rồi viết trước reversal trigger. Với `Designing an API client for data ingestion`, absence of error không phải pass; pass cần observation đúng grain, một oracle độc lập và changed-constraint case đủ làm model có cơ hội thất bại.

## Case Study Thực Chiến: Designing an API client for data ingestion

Dựng một máy chủ giả có phân trang, giới hạn tốc độ, lỗi ngẫu nhiên 10%, và chèn thêm bản ghi giữa lúc đang phân trang. Viết trình gọi đạt sáu yêu cầu. Nạp toàn bộ và đối soát số bản ghi với nguồn. Giết tiến trình giữa chừng và chứng minh lần chạy sau tiếp tục đúng chỗ.

Trong case `wiki.de-foundation.designing-an-api-client-for-data-ingestion`, learner ghi expected transition, input snapshot, version và giới hạn an toàn trước khi chạy. Sau execution, họ giữ raw counter, timestamp, exit status, state trước–sau và giải thích delta bằng mechanism ở trên. Đánh giá không cho phép sửa expected result sau khi nhìn output mà không ghi change record.

Biến thể khó hơn đổi một constraint có khả năng đảo kết luận: workload shape, memory pressure, connection reuse, retry budget, permission hoặc dependency direction. Tầng *sáng tạo*. Objective đòi ghép sáu cơ chế thành một thành phần chịu lỗi. Kiểm bằng thí nghiệm nguồn xấu; đạt khi đối soát khớp tuyệt đối dưới cả ba điều kiện lỗi.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Phân trang theo số trang trên dữ liệu đang đổi. **Thực tế:** tín hiệu chỉ chứng minh điều nó đo trong đúng scope; state ở layer khác vẫn có thể trái ngược. **Vì sao nghe hợp lý:** happy path nhỏ thường không chạm queue, cache, partial progress hoặc restart.

**Hiểu lầm:** thử lại mà không có khoá bất biến. **Thực tế:** tool và API cung cấp primitive, không tự cấp ownership, deadline, idempotency hay recovery policy. **Vì sao nghe hợp lý:** syntax gọn che mất protocol và lifecycle phía dưới.

Với `wiki.de-foundation.designing-an-api-client-for-data-ingestion`, một edge case đáng giữ là observation đúng nhưng diagnosis sai: counter tăng thật, song nguyên nhân điều khiển nằm ở layer trước. Muốn tránh, timeline phải nối trigger tới consumer harm và ghi rõ negative control nào đã loại giả thuyết cạnh tranh.

## Nếu Bạn Dạy Lại Điều Này...

Mở bài bằng một dự đoán dễ sai về `Designing an API client for data ingestion`, không mở bằng định nghĩa. Cho hai trace gần giống nhau nhưng khác đúng một state boundary; learner phải chọn probe tiếp theo trước khi được xem đáp án.

Bài tập seed dùng chính lab của DE-L084, sau đó đổi constraint đủ mạnh để buộc giữ hoặc đảo quyết định. Người dạy chấm reasoning chain và evidence, không chấm việc learner đoán đúng tên công cụ.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `Designing an API client for data ingestion` dùng điều kiện hoàn thành sau: Đối soát khớp tuyệt đối dưới cả ba điều kiện lỗi, và sau khi giết tiến trình thì lần chạy sau tiếp tục đúng chỗ. Mỗi probe phải có prediction, failure signal và independent oracle.

### Probe 1: state transition và invariant

**Mệnh đề P1 cần kiểm.** Bài ghép, và kết quả của nó được dùng lại nguyên vẹn ở M16.

**Thiết kế phép thử.** Với `wiki.de-foundation.designing-an-api-client-for-data-ingestion`, tạo positive và negative control chỉ khác một điều kiện; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P1 cần giữ.** Với `wiki.de-foundation.designing-an-api-client-for-data-ingestion`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề P2 cần kiểm.** Viết trình gọi đạt sáu yêu cầu và chứng minh nó nạp đủ, không trùng, dưới điều kiện nguồn lỗi và giới hạn tốc độ.

**Thiết kế phép thử.** Với `wiki.de-foundation.designing-an-api-client-for-data-ingestion`, tạo boundary case ngay trước và sau ngưỡng; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P2 cần giữ.** Với `wiki.de-foundation.designing-an-api-client-for-data-ingestion`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề P3 cần kiểm.** Tầng *sáng tạo*.

**Thiết kế phép thử.** Với `wiki.de-foundation.designing-an-api-client-for-data-ingestion`, tạo replay cùng identity nhưng đổi state; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P3 cần giữ.** Với `wiki.de-foundation.designing-an-api-client-for-data-ingestion`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề P4 cần kiểm.** Dựng một máy chủ giả có phân trang, giới hạn tốc độ, lỗi ngẫu nhiên 10%, và chèn thêm bản ghi giữa lúc đang phân trang.

**Thiết kế phép thử.** Với `wiki.de-foundation.designing-an-api-client-for-data-ingestion`, tạo failure inject trước và sau transition bền vững; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P4 cần giữ.** Với `wiki.de-foundation.designing-an-api-client-for-data-ingestion`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề P5 cần kiểm.** Phân trang theo số trang trên dữ liệu đang đổi · thử lại mà không có khoá bất biến · đoán thời gian chờ thay vì đọc tiêu đề · không lưu trạng thái nên chạy lại từ đầu.

**Thiết kế phép thử.** Với `wiki.de-foundation.designing-an-api-client-for-data-ingestion`, tạo changed scale làm cost model đổi; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P5 cần giữ.** Với `wiki.de-foundation.designing-an-api-client-for-data-ingestion`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề P6 cần kiểm.** Đối soát khớp tuyệt đối dưới cả ba điều kiện lỗi, và sau khi giết tiến trình thì lần chạy sau tiếp tục đúng chỗ.

**Thiết kế phép thử.** Với `wiki.de-foundation.designing-an-api-client-for-data-ingestion`, tạo adversarial order, skew hoặc packet timing; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P6 cần giữ.** Với `wiki.de-foundation.designing-an-api-client-for-data-ingestion`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề P7 cần kiểm.** Bài ghép, và kết quả của nó được dùng lại nguyên vẹn ở M16.

**Thiết kế phép thử.** Với `wiki.de-foundation.designing-an-api-client-for-data-ingestion`, tạo fresh environment không cache; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P7 cần giữ.** Với `wiki.de-foundation.designing-an-api-client-for-data-ingestion`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề P8 cần kiểm.** Viết trình gọi đạt sáu yêu cầu và chứng minh nó nạp đủ, không trùng, dưới điều kiện nguồn lỗi và giới hạn tốc độ.

**Thiết kế phép thử.** Với `wiki.de-foundation.designing-an-api-client-for-data-ingestion`, tạo independent oracle không dùng chung implementation; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P8 cần giữ.** Với `wiki.de-foundation.designing-an-api-client-for-data-ingestion`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề P9 cần kiểm.** Tầng *sáng tạo*.

**Thiết kế phép thử.** Với `wiki.de-foundation.designing-an-api-client-for-data-ingestion`, tạo partial progress rồi restart; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P9 cần giữ.** Với `wiki.de-foundation.designing-an-api-client-for-data-ingestion`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề P10 cần kiểm.** Dựng một máy chủ giả có phân trang, giới hạn tốc độ, lỗi ngẫu nhiên 10%, và chèn thêm bản ghi giữa lúc đang phân trang.

**Thiết kế phép thử.** Với `wiki.de-foundation.designing-an-api-client-for-data-ingestion`, tạo missing evidence phải abstain; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P10 cần giữ.** Với `wiki.de-foundation.designing-an-api-client-for-data-ingestion`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề P11 cần kiểm.** Phân trang theo số trang trên dữ liệu đang đổi · thử lại mà không có khoá bất biến · đoán thời gian chờ thay vì đọc tiêu đề · không lưu trạng thái nên chạy lại từ đầu.

**Thiết kế phép thử.** Với `wiki.de-foundation.designing-an-api-client-for-data-ingestion`, tạo reviewer tái hiện từ evidence package; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P11 cần giữ.** Với `wiki.de-foundation.designing-an-api-client-for-data-ingestion`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề P12 cần kiểm.** Đối soát khớp tuyệt đối dưới cả ba điều kiện lỗi, và sau khi giết tiến trình thì lần chạy sau tiếp tục đúng chỗ.

**Thiết kế phép thử.** Với `wiki.de-foundation.designing-an-api-client-for-data-ingestion`, tạo constraint đổi đủ để quyết định đảo; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P12 cần giữ.** Với `wiki.de-foundation.designing-an-api-client-for-data-ingestion`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên khiến mô hình `Designing an API client for data ingestion` không còn đúng là gì?

<details><summary>Đáp án</summary>Phân trang theo số trang trên dữ liệu đang đổi · thử lại mà không có khoá bất biến · đoán thời gian chờ thay vì đọc tiêu đề · không lưu trạng thái nên chạy lại từ đầu.</details>

2. Evidence nào phân biệt được hai state dễ nhầm?

<details><summary>Đáp án</summary>Tầng *sáng tạo*. Objective đòi ghép sáu cơ chế thành một thành phần chịu lỗi. Kiểm bằng thí nghiệm nguồn xấu; đạt khi đối soát khớp tuyệt đối dưới cả ba điều kiện lỗi.</details>

3. Khi constraint đổi, điều gì quyết định giữ hay đảo lựa chọn?

<details><summary>Đáp án</summary>Đối soát khớp tuyệt đối dưới cả ba điều kiện lỗi, và sau khi giết tiến trình thì lần chạy sau tiếp tục đúng chỗ.</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `Designing an API client for data ingestion` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Hành vi phụ thuộc kernel, distribution, library, network path hoặc hardware phải được kiểm lại trên target đã ghi version.
- Concept key `ck.de.designing-an-api-client-for-data-ingestion` đang ở trạng thái `proposed`; note chưa được tính là canonical registry coverage.
- Một trace đơn lẻ không chứng minh capacity, reliability hoặc security cho population khác.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-KUROSE-ROSS-NETWORKING-8E]]
2. [[SRC-RFC9110-HTTP-SEMANTICS]]
3. [[SRC-AWS-TIMEOUTS-RETRIES-BACKOFF]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-KUROSE-ROSS-NETWORKING-8E]] — `src.book.kurose-ross-networking.8e` | §§1.4, 2.2, 2.4, 2.7, 3.5–3.7, 4.5, 6.6.1 và Chapter 8; PDF 67–682 | mechanism và boundary liên quan trực tiếp tới `Designing an API client for data ingestion` | cơ chế, quyết định, case và probe | Đã phủ | phần ngoài objective DE-L084 |
| [[SRC-RFC9110-HTTP-SEMANTICS]] — `src.web.rfc9110-http-semantics` | RFC 9110 method, status, representation, cache và idempotent semantics | mechanism và boundary liên quan trực tiếp tới `Designing an API client for data ingestion` | cơ chế, quyết định, case và probe | Đã phủ | phần ngoài objective DE-L084 |
| [[SRC-AWS-TIMEOUTS-RETRIES-BACKOFF]] — `src.web.aws-timeouts-retries-backoff` | Timeouts, retries, backoff with jitter; accessed 2026-10-01 | mechanism và boundary liên quan trực tiếp tới `Designing an API client for data ingestion` | cơ chế, quyết định, case và probe | Đã phủ | phần ngoài objective DE-L084 |

## Key takeaways
- Viết trình gọi đạt sáu yêu cầu và chứng minh nó nạp đủ, không trùng, dưới điều kiện nguồn lỗi và giới hạn tốc độ.
- Đối soát khớp tuyệt đối dưới cả ba điều kiện lỗi, và sau khi giết tiến trình thì lần chạy sau tiếp tục đúng chỗ.
- `Designing an API client for data ingestion` chỉ có nghĩa trong scope, state, identity và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.
