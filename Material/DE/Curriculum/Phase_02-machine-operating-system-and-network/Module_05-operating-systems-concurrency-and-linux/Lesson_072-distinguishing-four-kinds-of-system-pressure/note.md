# Phase 2: Machine, Operating System and Network
# Module 5: Operating Systems, Concurrency and Linux
# Lesson 72: Distinguishing four kinds of system pressure

## Mục tiêu bài học

**Năng lực cần chứng minh.** Chẩn đoán đúng loại tải trong bốn loại chỉ bằng chỉ số hệ thống, trong giới hạn thời gian.

**Điều kiện hoàn thành.** Chẩn đoán đúng ≥ 3/4 tình huống trong giới hạn thời gian, mỗi lần dẫn được hai chỉ số nhất quán.

**Kiến thức và cơ chế.** Bài tổng hợp phần chẩn đoán, và nó là thứ dùng nhiều nhất khi trực. Bốn loại tải và bộ chỉ số phân biệt từng loại. Bão hoà CPU: mức dùng cao ở phần người dùng hoặc phần nhân, hàng đợi chạy dài, chờ vào ra thấp. Nghẽn vào ra: chờ vào ra cao, độ sâu hàng đợi thiết bị cao, thời gian phục vụ cao, trong khi CPU rảnh. Áp lực bộ nhớ: lỗi trang nặng tăng, hoạt động hoán đổi, bộ nhớ khả dụng thấp; phân biệt với bộ nhớ trống thấp theo lesson 63. Đĩa đầy: khác ba loại trên vì nó làm thao tác ghi thất bại chứ chỉ chậm, và có thể do tệp đã xoá còn mở theo lesson 64. Quy trình chẩn đoán bốn bước theo thứ tự cố định để không bỏ sót. Nguyên tắc: **kết luận phải dẫn được về ít nhất hai chỉ số nhất quán với nhau**, vì một chỉ số đơn lẻ dễ dẫn tới kết luận sai.


# Distinguishing four kinds of system pressure

**Tóm tắt bản chất:** Chẩn đoán đúng loại tải trong bốn loại chỉ bằng chỉ số hệ thống, trong giới hạn thời gian. Cơ chế chỉ có giá trị khi workload, version, state owner và failure boundary đã được khóa; một con số đẹp ngoài bốn điều kiện đó không đủ để ra quyết định.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, đo và ra quyết định đúng về Distinguishing four kinds of system pressure?

## Nỗi Đau & Động Lực

Kết luận từ một chỉ số · chạy mọi lệnh rồi vẫn không kết luận · nhầm bộ nhớ trống thấp với áp lực bộ nhớ · bỏ qua bước xác định nguyên nhân sâu hơn. Đây không phải danh sách lỗi cú pháp. Mỗi lỗi làm người vận hành chọn nhầm owner hoặc chữa symptom ở layer sau, khiến thời gian phục hồi tăng dù command vừa chạy trả về thành công.

Năng lực cần giữ sau bài là: Chẩn đoán đúng loại tải trong bốn loại chỉ bằng chỉ số hệ thống, trong giới hạn thời gian. Nếu learner chỉ nhắc lại định nghĩa nhưng không phân biệt được hai state gần nhau trên số đo, bài chưa đạt.

## Cơ Chế Tác Động

Bài tổng hợp phần chẩn đoán, và nó là thứ dùng nhiều nhất khi trực. Bốn loại tải và bộ chỉ số phân biệt từng loại. Bão hoà CPU: mức dùng cao ở phần người dùng hoặc phần nhân, hàng đợi chạy dài, chờ vào ra thấp. Nghẽn vào ra: chờ vào ra cao, độ sâu hàng đợi thiết bị cao, thời gian phục vụ cao, trong khi CPU rảnh. Áp lực bộ nhớ: lỗi trang nặng tăng, hoạt động hoán đổi, bộ nhớ khả dụng thấp; phân biệt với bộ nhớ trống thấp theo lesson 63. Đĩa đầy: khác ba loại trên vì nó làm thao tác ghi thất bại chứ chỉ chậm, và có thể do tệp đã xoá còn mở theo lesson 64. Quy trình chẩn đoán bốn bước theo thứ tự cố định để không bỏ sót. Nguyên tắc: **kết luận phải dẫn được về ít nhất hai chỉ số nhất quán với nhau**, vì một chỉ số đơn lẻ dễ dẫn tới kết luận sai.

Tách ba lớp khi đọc cơ chế `wiki.de-foundation.distinguishing-four-kinds-of-system-pressure`: declared state là điều cấu hình hoặc API yêu cầu; executed state là việc runtime thực sự làm; consumer-visible state là điều client hay operator quan sát. Ba lớp có thể lệch nhau vì cache, buffering, retry, scheduling, queue hoặc failure giữa hai transition. Evidence phải chỉ ra lớp nào đang được đo.

## Bản Đồ Quyết Định

| Bước | Câu hỏi phải khóa | Điều kiện đạt |
|---|---|---|
| Observe | Khóa process, resource, file descriptor và time window | Không trộn symptom giữa hai owner |
| Probe | Dùng phép đo read-only hẹp nhất | Probe phân biệt được hai giả thuyết |
| Contain | Giảm harm trước mutation | Có rollback và state snapshot |
| Escalate | Chuyển owner khi boundary đã chứng minh | Evidence đủ tái hiện |

Quy tắc mặc định là chọn phép giải thích đơn giản nhất qua được hard constraints, rồi viết trước reversal trigger. Với `Distinguishing four kinds of system pressure`, absence of error không phải pass; pass cần observation đúng grain, một oracle độc lập và changed-constraint case đủ làm model có cơ hội thất bại.

## Case Study Thực Chiến: Distinguishing four kinds of system pressure

Giảng viên tạo lần lượt bốn loại tải trên một máy, mỗi lần 8 phút. Với mỗi lần, chạy quy trình bốn bước, ghi bộ chỉ số, và kết luận. Với tình huống đĩa đầy, xác định thêm nguyên nhân là tệp thật hay tệp đã xoá còn mở.

Trong case `wiki.de-foundation.distinguishing-four-kinds-of-system-pressure`, learner ghi expected transition, input snapshot, version và giới hạn an toàn trước khi chạy. Sau execution, họ giữ raw counter, timestamp, exit status, state trước–sau và giải thích delta bằng mechanism ở trên. Đánh giá không cho phép sửa expected result sau khi nhìn output mà không ghi change record.

Biến thể khó hơn đổi một constraint có khả năng đảo kết luận: workload shape, memory pressure, connection reuse, retry budget, permission hoặc dependency direction. Tầng *phân tích*. Objective là chẩn đoán dưới áp lực thời gian, đúng điều kiện khi trực. Kiểm bằng bốn tình huống tiêm sẵn, mỗi tình huống 8 phút; đạt khi chẩn đoán đúng ít nhất ba và mỗi lần dẫn được hai chỉ số nhất quán.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Kết luận từ một chỉ số. **Thực tế:** tín hiệu chỉ chứng minh điều nó đo trong đúng scope; state ở layer khác vẫn có thể trái ngược. **Vì sao nghe hợp lý:** happy path nhỏ thường không chạm queue, cache, partial progress hoặc restart.

**Hiểu lầm:** chạy mọi lệnh rồi vẫn không kết luận. **Thực tế:** tool và API cung cấp primitive, không tự cấp ownership, deadline, idempotency hay recovery policy. **Vì sao nghe hợp lý:** syntax gọn che mất protocol và lifecycle phía dưới.

Với `wiki.de-foundation.distinguishing-four-kinds-of-system-pressure`, một edge case đáng giữ là observation đúng nhưng diagnosis sai: counter tăng thật, song nguyên nhân điều khiển nằm ở layer trước. Muốn tránh, timeline phải nối trigger tới consumer harm và ghi rõ negative control nào đã loại giả thuyết cạnh tranh.

## Nếu Bạn Dạy Lại Điều Này...

Mở bài bằng một dự đoán dễ sai về `Distinguishing four kinds of system pressure`, không mở bằng định nghĩa. Cho hai trace gần giống nhau nhưng khác đúng một state boundary; learner phải chọn probe tiếp theo trước khi được xem đáp án.

Bài tập seed dùng chính lab của DE-L072, sau đó đổi constraint đủ mạnh để buộc giữ hoặc đảo quyết định. Người dạy chấm reasoning chain và evidence, không chấm việc learner đoán đúng tên công cụ.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `Distinguishing four kinds of system pressure` dùng điều kiện hoàn thành sau: Chẩn đoán đúng ≥ 3/4 tình huống trong giới hạn thời gian, mỗi lần dẫn được hai chỉ số nhất quán. Mỗi probe phải có prediction, failure signal và independent oracle.

### Probe 1: state transition và invariant

**Mệnh đề P1 cần kiểm.** Bài tổng hợp phần chẩn đoán, và nó là thứ dùng nhiều nhất khi trực.

**Thiết kế phép thử.** Với `wiki.de-foundation.distinguishing-four-kinds-of-system-pressure`, tạo positive và negative control chỉ khác một điều kiện; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P1 cần giữ.** Với `wiki.de-foundation.distinguishing-four-kinds-of-system-pressure`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề P2 cần kiểm.** Chẩn đoán đúng loại tải trong bốn loại chỉ bằng chỉ số hệ thống, trong giới hạn thời gian.

**Thiết kế phép thử.** Với `wiki.de-foundation.distinguishing-four-kinds-of-system-pressure`, tạo boundary case ngay trước và sau ngưỡng; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P2 cần giữ.** Với `wiki.de-foundation.distinguishing-four-kinds-of-system-pressure`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề P3 cần kiểm.** Tầng *phân tích*.

**Thiết kế phép thử.** Với `wiki.de-foundation.distinguishing-four-kinds-of-system-pressure`, tạo replay cùng identity nhưng đổi state; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P3 cần giữ.** Với `wiki.de-foundation.distinguishing-four-kinds-of-system-pressure`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề P4 cần kiểm.** Giảng viên tạo lần lượt bốn loại tải trên một máy, mỗi lần 8 phút.

**Thiết kế phép thử.** Với `wiki.de-foundation.distinguishing-four-kinds-of-system-pressure`, tạo failure inject trước và sau transition bền vững; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P4 cần giữ.** Với `wiki.de-foundation.distinguishing-four-kinds-of-system-pressure`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề P5 cần kiểm.** Kết luận từ một chỉ số · chạy mọi lệnh rồi vẫn không kết luận · nhầm bộ nhớ trống thấp với áp lực bộ nhớ · bỏ qua bước xác định nguyên nhân sâu hơn.

**Thiết kế phép thử.** Với `wiki.de-foundation.distinguishing-four-kinds-of-system-pressure`, tạo changed scale làm cost model đổi; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P5 cần giữ.** Với `wiki.de-foundation.distinguishing-four-kinds-of-system-pressure`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề P6 cần kiểm.** Chẩn đoán đúng ≥ 3/4 tình huống trong giới hạn thời gian, mỗi lần dẫn được hai chỉ số nhất quán.

**Thiết kế phép thử.** Với `wiki.de-foundation.distinguishing-four-kinds-of-system-pressure`, tạo adversarial order, skew hoặc packet timing; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P6 cần giữ.** Với `wiki.de-foundation.distinguishing-four-kinds-of-system-pressure`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề P7 cần kiểm.** Bài tổng hợp phần chẩn đoán, và nó là thứ dùng nhiều nhất khi trực.

**Thiết kế phép thử.** Với `wiki.de-foundation.distinguishing-four-kinds-of-system-pressure`, tạo fresh environment không cache; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P7 cần giữ.** Với `wiki.de-foundation.distinguishing-four-kinds-of-system-pressure`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề P8 cần kiểm.** Chẩn đoán đúng loại tải trong bốn loại chỉ bằng chỉ số hệ thống, trong giới hạn thời gian.

**Thiết kế phép thử.** Với `wiki.de-foundation.distinguishing-four-kinds-of-system-pressure`, tạo independent oracle không dùng chung implementation; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P8 cần giữ.** Với `wiki.de-foundation.distinguishing-four-kinds-of-system-pressure`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề P9 cần kiểm.** Tầng *phân tích*.

**Thiết kế phép thử.** Với `wiki.de-foundation.distinguishing-four-kinds-of-system-pressure`, tạo partial progress rồi restart; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P9 cần giữ.** Với `wiki.de-foundation.distinguishing-four-kinds-of-system-pressure`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề P10 cần kiểm.** Giảng viên tạo lần lượt bốn loại tải trên một máy, mỗi lần 8 phút.

**Thiết kế phép thử.** Với `wiki.de-foundation.distinguishing-four-kinds-of-system-pressure`, tạo missing evidence phải abstain; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P10 cần giữ.** Với `wiki.de-foundation.distinguishing-four-kinds-of-system-pressure`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề P11 cần kiểm.** Kết luận từ một chỉ số · chạy mọi lệnh rồi vẫn không kết luận · nhầm bộ nhớ trống thấp với áp lực bộ nhớ · bỏ qua bước xác định nguyên nhân sâu hơn.

**Thiết kế phép thử.** Với `wiki.de-foundation.distinguishing-four-kinds-of-system-pressure`, tạo reviewer tái hiện từ evidence package; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P11 cần giữ.** Với `wiki.de-foundation.distinguishing-four-kinds-of-system-pressure`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề P12 cần kiểm.** Chẩn đoán đúng ≥ 3/4 tình huống trong giới hạn thời gian, mỗi lần dẫn được hai chỉ số nhất quán.

**Thiết kế phép thử.** Với `wiki.de-foundation.distinguishing-four-kinds-of-system-pressure`, tạo constraint đổi đủ để quyết định đảo; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P12 cần giữ.** Với `wiki.de-foundation.distinguishing-four-kinds-of-system-pressure`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên khiến mô hình `Distinguishing four kinds of system pressure` không còn đúng là gì?

<details><summary>Đáp án</summary>Kết luận từ một chỉ số · chạy mọi lệnh rồi vẫn không kết luận · nhầm bộ nhớ trống thấp với áp lực bộ nhớ · bỏ qua bước xác định nguyên nhân sâu hơn.</details>

2. Evidence nào phân biệt được hai state dễ nhầm?

<details><summary>Đáp án</summary>Tầng *phân tích*. Objective là chẩn đoán dưới áp lực thời gian, đúng điều kiện khi trực. Kiểm bằng bốn tình huống tiêm sẵn, mỗi tình huống 8 phút; đạt khi chẩn đoán đúng ít nhất ba và mỗi lần dẫn được hai chỉ số nhất quán.</details>

3. Khi constraint đổi, điều gì quyết định giữ hay đảo lựa chọn?

<details><summary>Đáp án</summary>Chẩn đoán đúng ≥ 3/4 tình huống trong giới hạn thời gian, mỗi lần dẫn được hai chỉ số nhất quán.</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `Distinguishing four kinds of system pressure` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Hành vi phụ thuộc kernel, distribution, library, network path hoặc hardware phải được kiểm lại trên target đã ghi version.
- Concept key `ck.de.distinguishing-four-kinds-of-system-pressure` đang ở trạng thái `proposed`; note chưa được tính là canonical registry coverage.
- Một trace đơn lẻ không chứng minh capacity, reliability hoặc security cho population khác.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-LINUX-KERNEL-RUNTIME-DOCS]]
2. [[SRC-GOOGLE-SRE-MONITORING]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-LINUX-KERNEL-RUNTIME-DOCS]] — `src.docs.linux-kernel-runtime` | PSI, userspace API, io_uring và trace documentation; accessed 2026-10-02 | mechanism và boundary liên quan trực tiếp tới `Distinguishing four kinds of system pressure` | cơ chế, quyết định, case và probe | Đã phủ | phần ngoài objective DE-L072 |
| [[SRC-GOOGLE-SRE-MONITORING]] — `src.web.google-sre-monitoring` | Monitoring distributed systems; accessed 2026-10-01 | mechanism và boundary liên quan trực tiếp tới `Distinguishing four kinds of system pressure` | cơ chế, quyết định, case và probe | Đã phủ | phần ngoài objective DE-L072 |

## Key takeaways
- Chẩn đoán đúng loại tải trong bốn loại chỉ bằng chỉ số hệ thống, trong giới hạn thời gian.
- Chẩn đoán đúng ≥ 3/4 tình huống trong giới hạn thời gian, mỗi lần dẫn được hai chỉ số nhất quán.
- `Distinguishing four kinds of system pressure` chỉ có nghĩa trong scope, state, identity và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.
