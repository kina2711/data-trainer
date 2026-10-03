# Phase 2: Machine, Operating System and Network
# Module 5: Operating Systems, Concurrency and Linux
# Lesson 65: Non-blocking descriptors, select, poll and epoll

## Mục tiêu bài học

**Năng lực cần chứng minh.** Viết một máy chủ một luồng theo dõi nhiều kết nối và đo chi phí của hai cơ chế theo dõi khi số kết nối tăng.

**Điều kiện hoàn thành.** Hai đường chi phí tách nhau rõ ở 10.000 kết nối, và ca treo do báo theo sườn được tái hiện rồi sửa.

**Kiến thức và cơ chế.** Bài giải thích cơ chế dưới mọi vòng lặp sự kiện, nên nó là nền của phần bất đồng bộ đã học ở M2. Bộ mô tả chặn làm luồng gọi ngủ tới khi thao tác xong; bộ mô tả không chặn trả về ngay một trạng thái chưa sẵn sàng thay vì chờ, nên một luồng theo dõi được nhiều kết nối. Ba thế hệ cơ chế theo dõi và khác biệt về chi phí: hai cơ chế cũ quét toàn bộ tập bộ mô tả mỗi lần gọi nên chi phí tăng theo số kết nối; cơ chế mới giữ sẵn tập quan tâm và chỉ trả về phần đã sẵn sàng, nên chi phí không tăng theo số kết nối đang mở. Hai chế độ báo: báo theo mức lặp lại trạng thái tới khi được xử lý, báo theo sườn chỉ báo một lần khi trạng thái đổi; **chế độ báo theo sườn bắt buộc đọc tới khi hết dữ liệu**, và bỏ quy tắc đó làm treo kết nối mà không có lỗi nào. Tệp thường không có ngữ nghĩa sẵn sàng hữu ích như ổ cắm.


# Non-blocking descriptors, select, poll and epoll

**Tóm tắt bản chất:** Viết một máy chủ một luồng theo dõi nhiều kết nối và đo chi phí của hai cơ chế theo dõi khi số kết nối tăng. Cơ chế chỉ có giá trị khi workload, version, state owner và failure boundary đã được khóa; một con số đẹp ngoài bốn điều kiện đó không đủ để ra quyết định.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, đo và ra quyết định đúng về Non-blocking descriptors, select, poll and epoll?

## Nỗi Đau & Động Lực

Dùng bộ mô tả chặn trong vòng lặp sự kiện · dùng chế độ báo theo sườn mà không đọc cạn · đo chi phí chỉ ở số kết nối nhỏ · giả định tệp thường có ngữ nghĩa sẵn sàng như ổ cắm. Đây không phải danh sách lỗi cú pháp. Mỗi lỗi làm người vận hành chọn nhầm owner hoặc chữa symptom ở layer sau, khiến thời gian phục hồi tăng dù command vừa chạy trả về thành công.

Năng lực cần giữ sau bài là: Viết một máy chủ một luồng theo dõi nhiều kết nối và đo chi phí của hai cơ chế theo dõi khi số kết nối tăng. Nếu learner chỉ nhắc lại định nghĩa nhưng không phân biệt được hai state gần nhau trên số đo, bài chưa đạt.

## Cơ Chế Tác Động

Bài giải thích cơ chế dưới mọi vòng lặp sự kiện, nên nó là nền của phần bất đồng bộ đã học ở M2. Bộ mô tả chặn làm luồng gọi ngủ tới khi thao tác xong; bộ mô tả không chặn trả về ngay một trạng thái chưa sẵn sàng thay vì chờ, nên một luồng theo dõi được nhiều kết nối. Ba thế hệ cơ chế theo dõi và khác biệt về chi phí: hai cơ chế cũ quét toàn bộ tập bộ mô tả mỗi lần gọi nên chi phí tăng theo số kết nối; cơ chế mới giữ sẵn tập quan tâm và chỉ trả về phần đã sẵn sàng, nên chi phí không tăng theo số kết nối đang mở. Hai chế độ báo: báo theo mức lặp lại trạng thái tới khi được xử lý, báo theo sườn chỉ báo một lần khi trạng thái đổi; **chế độ báo theo sườn bắt buộc đọc tới khi hết dữ liệu**, và bỏ quy tắc đó làm treo kết nối mà không có lỗi nào. Tệp thường không có ngữ nghĩa sẵn sàng hữu ích như ổ cắm.

Tách ba lớp khi đọc cơ chế `wiki.de-foundation.non-blocking-descriptors-select-poll-and-epoll`: declared state là điều cấu hình hoặc API yêu cầu; executed state là việc runtime thực sự làm; consumer-visible state là điều client hay operator quan sát. Ba lớp có thể lệch nhau vì cache, buffering, retry, scheduling, queue hoặc failure giữa hai transition. Evidence phải chỉ ra lớp nào đang được đo.

## Bản Đồ Quyết Định

| Bước | Câu hỏi phải khóa | Điều kiện đạt |
|---|---|---|
| Observe | Khóa process, resource, file descriptor và time window | Không trộn symptom giữa hai owner |
| Probe | Dùng phép đo read-only hẹp nhất | Probe phân biệt được hai giả thuyết |
| Contain | Giảm harm trước mutation | Có rollback và state snapshot |
| Escalate | Chuyển owner khi boundary đã chứng minh | Evidence đủ tái hiện |

Quy tắc mặc định là chọn phép giải thích đơn giản nhất qua được hard constraints, rồi viết trước reversal trigger. Với `Non-blocking descriptors, select, poll and epoll`, absence of error không phải pass; pass cần observation đúng grain, một oracle độc lập và changed-constraint case đủ làm model có cơ hội thất bại.

## Case Study Thực Chiến: Non-blocking descriptors, select, poll and epoll

Viết máy chủ một luồng dùng bộ mô tả không chặn. Cài cả hai cơ chế theo dõi. Đo thời gian mỗi vòng lặp ở 100, 1.000 và 10.000 kết nối nhàn rỗi, vẽ hai đường. Chuyển sang chế độ báo theo sườn mà không đọc tới khi hết dữ liệu, tái hiện kết nối treo, rồi sửa theo quy tắc đọc cạn.

Trong case `wiki.de-foundation.non-blocking-descriptors-select-poll-and-epoll`, learner ghi expected transition, input snapshot, version và giới hạn an toàn trước khi chạy. Sau execution, họ giữ raw counter, timestamp, exit status, state trước–sau và giải thích delta bằng mechanism ở trên. Đánh giá không cho phép sửa expected result sau khi nhìn output mà không ghi change record.

Biến thể khó hơn đổi một constraint có khả năng đảo kết luận: workload shape, memory pressure, connection reuse, retry budget, permission hoặc dependency direction. Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là đường chi phí theo số kết nối. Kiểm bằng phép đo thay đổi quy mô; đạt khi hai đường chi phí tách nhau rõ ở 10.000 kết nối và ca báo theo sườn bị treo được tái hiện rồi sửa.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Dùng bộ mô tả chặn trong vòng lặp sự kiện. **Thực tế:** tín hiệu chỉ chứng minh điều nó đo trong đúng scope; state ở layer khác vẫn có thể trái ngược. **Vì sao nghe hợp lý:** happy path nhỏ thường không chạm queue, cache, partial progress hoặc restart.

**Hiểu lầm:** dùng chế độ báo theo sườn mà không đọc cạn. **Thực tế:** tool và API cung cấp primitive, không tự cấp ownership, deadline, idempotency hay recovery policy. **Vì sao nghe hợp lý:** syntax gọn che mất protocol và lifecycle phía dưới.

Với `wiki.de-foundation.non-blocking-descriptors-select-poll-and-epoll`, một edge case đáng giữ là observation đúng nhưng diagnosis sai: counter tăng thật, song nguyên nhân điều khiển nằm ở layer trước. Muốn tránh, timeline phải nối trigger tới consumer harm và ghi rõ negative control nào đã loại giả thuyết cạnh tranh.

## Nếu Bạn Dạy Lại Điều Này...

Mở bài bằng một dự đoán dễ sai về `Non-blocking descriptors, select, poll and epoll`, không mở bằng định nghĩa. Cho hai trace gần giống nhau nhưng khác đúng một state boundary; learner phải chọn probe tiếp theo trước khi được xem đáp án.

Bài tập seed dùng chính lab của DE-L065, sau đó đổi constraint đủ mạnh để buộc giữ hoặc đảo quyết định. Người dạy chấm reasoning chain và evidence, không chấm việc learner đoán đúng tên công cụ.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `Non-blocking descriptors, select, poll and epoll` dùng điều kiện hoàn thành sau: Hai đường chi phí tách nhau rõ ở 10.000 kết nối, và ca treo do báo theo sườn được tái hiện rồi sửa. Mỗi probe phải có prediction, failure signal và independent oracle.

### Probe 1: state transition và invariant

**Mệnh đề P1 cần kiểm.** Bài giải thích cơ chế dưới mọi vòng lặp sự kiện, nên nó là nền của phần bất đồng bộ đã học ở M2.

**Thiết kế phép thử.** Với `wiki.de-foundation.non-blocking-descriptors-select-poll-and-epoll`, tạo positive và negative control chỉ khác một điều kiện; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P1 cần giữ.** Với `wiki.de-foundation.non-blocking-descriptors-select-poll-and-epoll`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề P2 cần kiểm.** Viết một máy chủ một luồng theo dõi nhiều kết nối và đo chi phí của hai cơ chế theo dõi khi số kết nối tăng.

**Thiết kế phép thử.** Với `wiki.de-foundation.non-blocking-descriptors-select-poll-and-epoll`, tạo boundary case ngay trước và sau ngưỡng; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P2 cần giữ.** Với `wiki.de-foundation.non-blocking-descriptors-select-poll-and-epoll`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề P3 cần kiểm.** Tầng *áp dụng*.

**Thiết kế phép thử.** Với `wiki.de-foundation.non-blocking-descriptors-select-poll-and-epoll`, tạo replay cùng identity nhưng đổi state; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P3 cần giữ.** Với `wiki.de-foundation.non-blocking-descriptors-select-poll-and-epoll`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề P4 cần kiểm.** Viết máy chủ một luồng dùng bộ mô tả không chặn.

**Thiết kế phép thử.** Với `wiki.de-foundation.non-blocking-descriptors-select-poll-and-epoll`, tạo failure inject trước và sau transition bền vững; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P4 cần giữ.** Với `wiki.de-foundation.non-blocking-descriptors-select-poll-and-epoll`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề P5 cần kiểm.** Dùng bộ mô tả chặn trong vòng lặp sự kiện · dùng chế độ báo theo sườn mà không đọc cạn · đo chi phí chỉ ở số kết nối nhỏ · giả định tệp thường có ngữ nghĩa sẵn sàng như ổ cắm.

**Thiết kế phép thử.** Với `wiki.de-foundation.non-blocking-descriptors-select-poll-and-epoll`, tạo changed scale làm cost model đổi; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P5 cần giữ.** Với `wiki.de-foundation.non-blocking-descriptors-select-poll-and-epoll`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề P6 cần kiểm.** Hai đường chi phí tách nhau rõ ở 10.000 kết nối, và ca treo do báo theo sườn được tái hiện rồi sửa.

**Thiết kế phép thử.** Với `wiki.de-foundation.non-blocking-descriptors-select-poll-and-epoll`, tạo adversarial order, skew hoặc packet timing; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P6 cần giữ.** Với `wiki.de-foundation.non-blocking-descriptors-select-poll-and-epoll`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề P7 cần kiểm.** Bài giải thích cơ chế dưới mọi vòng lặp sự kiện, nên nó là nền của phần bất đồng bộ đã học ở M2.

**Thiết kế phép thử.** Với `wiki.de-foundation.non-blocking-descriptors-select-poll-and-epoll`, tạo fresh environment không cache; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P7 cần giữ.** Với `wiki.de-foundation.non-blocking-descriptors-select-poll-and-epoll`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề P8 cần kiểm.** Viết một máy chủ một luồng theo dõi nhiều kết nối và đo chi phí của hai cơ chế theo dõi khi số kết nối tăng.

**Thiết kế phép thử.** Với `wiki.de-foundation.non-blocking-descriptors-select-poll-and-epoll`, tạo independent oracle không dùng chung implementation; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P8 cần giữ.** Với `wiki.de-foundation.non-blocking-descriptors-select-poll-and-epoll`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề P9 cần kiểm.** Tầng *áp dụng*.

**Thiết kế phép thử.** Với `wiki.de-foundation.non-blocking-descriptors-select-poll-and-epoll`, tạo partial progress rồi restart; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P9 cần giữ.** Với `wiki.de-foundation.non-blocking-descriptors-select-poll-and-epoll`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề P10 cần kiểm.** Viết máy chủ một luồng dùng bộ mô tả không chặn.

**Thiết kế phép thử.** Với `wiki.de-foundation.non-blocking-descriptors-select-poll-and-epoll`, tạo missing evidence phải abstain; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P10 cần giữ.** Với `wiki.de-foundation.non-blocking-descriptors-select-poll-and-epoll`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề P11 cần kiểm.** Dùng bộ mô tả chặn trong vòng lặp sự kiện · dùng chế độ báo theo sườn mà không đọc cạn · đo chi phí chỉ ở số kết nối nhỏ · giả định tệp thường có ngữ nghĩa sẵn sàng như ổ cắm.

**Thiết kế phép thử.** Với `wiki.de-foundation.non-blocking-descriptors-select-poll-and-epoll`, tạo reviewer tái hiện từ evidence package; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P11 cần giữ.** Với `wiki.de-foundation.non-blocking-descriptors-select-poll-and-epoll`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề P12 cần kiểm.** Hai đường chi phí tách nhau rõ ở 10.000 kết nối, và ca treo do báo theo sườn được tái hiện rồi sửa.

**Thiết kế phép thử.** Với `wiki.de-foundation.non-blocking-descriptors-select-poll-and-epoll`, tạo constraint đổi đủ để quyết định đảo; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P12 cần giữ.** Với `wiki.de-foundation.non-blocking-descriptors-select-poll-and-epoll`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên khiến mô hình `Non-blocking descriptors, select, poll and epoll` không còn đúng là gì?

<details><summary>Đáp án</summary>Dùng bộ mô tả chặn trong vòng lặp sự kiện · dùng chế độ báo theo sườn mà không đọc cạn · đo chi phí chỉ ở số kết nối nhỏ · giả định tệp thường có ngữ nghĩa sẵn sàng như ổ cắm.</details>

2. Evidence nào phân biệt được hai state dễ nhầm?

<details><summary>Đáp án</summary>Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là đường chi phí theo số kết nối. Kiểm bằng phép đo thay đổi quy mô; đạt khi hai đường chi phí tách nhau rõ ở 10.000 kết nối và ca báo theo sườn bị treo được tái hiện rồi sửa.</details>

3. Khi constraint đổi, điều gì quyết định giữ hay đảo lựa chọn?

<details><summary>Đáp án</summary>Hai đường chi phí tách nhau rõ ở 10.000 kết nối, và ca treo do báo theo sườn được tái hiện rồi sửa.</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `Non-blocking descriptors, select, poll and epoll` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Hành vi phụ thuộc kernel, distribution, library, network path hoặc hardware phải được kiểm lại trên target đã ghi version.
- Concept key `ck.de.non-blocking-descriptors-select-poll-and-epoll` đang ở trạng thái `proposed`; note chưa được tính là canonical registry coverage.
- Một trace đơn lẻ không chứng minh capacity, reliability hoặc security cho population khác.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-TLPI-2010]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-TLPI-2010]] — `src.book.tlpi.2010` | Chapters 4–39, 49–50, 61 và 63 theo scope record; PDF 113–1418 | mechanism và boundary liên quan trực tiếp tới `Non-blocking descriptors, select, poll and epoll` | cơ chế, quyết định, case và probe | Đã phủ | phần ngoài objective DE-L065 |

## Key takeaways
- Viết một máy chủ một luồng theo dõi nhiều kết nối và đo chi phí của hai cơ chế theo dõi khi số kết nối tăng.
- Hai đường chi phí tách nhau rõ ở 10.000 kết nối, và ca treo do báo theo sườn được tái hiện rồi sửa.
- `Non-blocking descriptors, select, poll and epoll` chỉ có nghĩa trong scope, state, identity và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.
