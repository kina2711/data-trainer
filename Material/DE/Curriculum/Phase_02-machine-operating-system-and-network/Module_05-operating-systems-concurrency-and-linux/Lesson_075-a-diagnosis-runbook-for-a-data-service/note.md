# Phase 2: Machine, Operating System and Network
# Module 5: Operating Systems, Concurrency and Linux
# Lesson 75: A diagnosis runbook for a data service

## Mục tiêu bài học

**Năng lực cần chứng minh.** Viết sổ tay năm mục mà một người khác dùng được để chẩn đoán và khắc phục, không cần hỏi.

**Điều kiện hoàn thành.** Người ngoài xử lý được ≥ 3/5 tình huống chỉ bằng sổ tay, và bản sửa sau đó giảm được số câu phải hỏi.

**Kiến thức và cơ chế.** Bài ghép: biến mọi kỹ năng chẩn đoán trong module thành một sổ tay dùng được lúc ba giờ sáng. Cấu trúc sổ tay theo đúng trình tự người trực cần, đã đặt ở lesson 10: triệu chứng nào, ảnh hưởng ra sao, chẩn đoán theo bước nào, giảm nhẹ thế nào, leo thang cho ai, và xác nhận đã hồi phục bằng gì. Năm mục bắt buộc cho một dịch vụ dữ liệu, mỗi mục tương ứng một bài đã học: dịch vụ không khởi động, dịch vụ chậm bất thường, đĩa đầy, rò rỉ mô tả tệp, và không kết nối được tới nguồn. Nguyên tắc viết: mỗi bước là một lệnh chạy được kèm cái cần nhìn trong kết quả, chứ một lời khuyên chung. Ngưỡng phải là số chứ tính từ. Phép thử của một sổ tay tốt là người chưa từng chạm vào hệ làm theo được, và đó chính là cách bài này chấm điểm.


# A diagnosis runbook for a data service

**Tóm tắt bản chất:** Viết sổ tay năm mục mà một người khác dùng được để chẩn đoán và khắc phục, không cần hỏi. Cơ chế chỉ có giá trị khi workload, version, state owner và failure boundary đã được khóa; một con số đẹp ngoài bốn điều kiện đó không đủ để ra quyết định.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, đo và ra quyết định đúng về A diagnosis runbook for a data service?

## Nỗi Đau & Động Lực

Viết bước dạng kiểm tra nhật ký mà không nói tìm gì · đặt ngưỡng bằng tính từ · bỏ bước xác nhận đã hồi phục · viết cho người đã biết hệ. Đây không phải danh sách lỗi cú pháp. Mỗi lỗi làm người vận hành chọn nhầm owner hoặc chữa symptom ở layer sau, khiến thời gian phục hồi tăng dù command vừa chạy trả về thành công.

Năng lực cần giữ sau bài là: Viết sổ tay năm mục mà một người khác dùng được để chẩn đoán và khắc phục, không cần hỏi. Nếu learner chỉ nhắc lại định nghĩa nhưng không phân biệt được hai state gần nhau trên số đo, bài chưa đạt.

## Cơ Chế Tác Động

Bài ghép: biến mọi kỹ năng chẩn đoán trong module thành một sổ tay dùng được lúc ba giờ sáng. Cấu trúc sổ tay theo đúng trình tự người trực cần, đã đặt ở lesson 10: triệu chứng nào, ảnh hưởng ra sao, chẩn đoán theo bước nào, giảm nhẹ thế nào, leo thang cho ai, và xác nhận đã hồi phục bằng gì. Năm mục bắt buộc cho một dịch vụ dữ liệu, mỗi mục tương ứng một bài đã học: dịch vụ không khởi động, dịch vụ chậm bất thường, đĩa đầy, rò rỉ mô tả tệp, và không kết nối được tới nguồn. Nguyên tắc viết: mỗi bước là một lệnh chạy được kèm cái cần nhìn trong kết quả, chứ một lời khuyên chung. Ngưỡng phải là số chứ tính từ. Phép thử của một sổ tay tốt là người chưa từng chạm vào hệ làm theo được, và đó chính là cách bài này chấm điểm.

Tách ba lớp khi đọc cơ chế `wiki.de-foundation.a-diagnosis-runbook-for-a-data-service`: declared state là điều cấu hình hoặc API yêu cầu; executed state là việc runtime thực sự làm; consumer-visible state là điều client hay operator quan sát. Ba lớp có thể lệch nhau vì cache, buffering, retry, scheduling, queue hoặc failure giữa hai transition. Evidence phải chỉ ra lớp nào đang được đo.

## Bản Đồ Quyết Định

| Bước | Câu hỏi phải khóa | Điều kiện đạt |
|---|---|---|
| Observe | Khóa process, resource, file descriptor và time window | Không trộn symptom giữa hai owner |
| Probe | Dùng phép đo read-only hẹp nhất | Probe phân biệt được hai giả thuyết |
| Contain | Giảm harm trước mutation | Có rollback và state snapshot |
| Escalate | Chuyển owner khi boundary đã chứng minh | Evidence đủ tái hiện |

Quy tắc mặc định là chọn phép giải thích đơn giản nhất qua được hard constraints, rồi viết trước reversal trigger. Với `A diagnosis runbook for a data service`, absence of error không phải pass; pass cần observation đúng grain, một oracle độc lập và changed-constraint case đủ làm model có cơ hội thất bại.

## Case Study Thực Chiến: A diagnosis runbook for a data service

Viết sổ tay năm mục cho dịch vụ ở lesson 69. Đưa cho một học viên chưa từng chạm vào dịch vụ đó. Giảng viên tạo lần lượt năm tình huống; người kia chỉ được dùng sổ tay. Ghi lại tình huống nào họ xử lý được và mọi câu họ phải hỏi. Sửa sổ tay theo danh sách đó.

Trong case `wiki.de-foundation.a-diagnosis-runbook-for-a-data-service`, learner ghi expected transition, input snapshot, version và giới hạn an toàn trước khi chạy. Sau execution, họ giữ raw counter, timestamp, exit status, state trước–sau và giải thích delta bằng mechanism ở trên. Đánh giá không cho phép sửa expected result sau khi nhìn output mà không ghi change record.

Biến thể khó hơn đổi một constraint có khả năng đảo kết luận: workload shape, memory pressure, connection reuse, retry budget, permission hoặc dependency direction. Tầng *đánh giá*. Objective đo chất lượng sổ tay bằng kết quả của người dùng nó chứ bằng độ dày. Kiểm bằng phép thử với người ngoài; đạt khi họ xử lý được ít nhất ba trong năm tình huống mà không phải hỏi.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Viết bước dạng kiểm tra nhật ký mà không nói tìm gì. **Thực tế:** tín hiệu chỉ chứng minh điều nó đo trong đúng scope; state ở layer khác vẫn có thể trái ngược. **Vì sao nghe hợp lý:** happy path nhỏ thường không chạm queue, cache, partial progress hoặc restart.

**Hiểu lầm:** đặt ngưỡng bằng tính từ. **Thực tế:** tool và API cung cấp primitive, không tự cấp ownership, deadline, idempotency hay recovery policy. **Vì sao nghe hợp lý:** syntax gọn che mất protocol và lifecycle phía dưới.

Với `wiki.de-foundation.a-diagnosis-runbook-for-a-data-service`, một edge case đáng giữ là observation đúng nhưng diagnosis sai: counter tăng thật, song nguyên nhân điều khiển nằm ở layer trước. Muốn tránh, timeline phải nối trigger tới consumer harm và ghi rõ negative control nào đã loại giả thuyết cạnh tranh.

## Nếu Bạn Dạy Lại Điều Này...

Mở bài bằng một dự đoán dễ sai về `A diagnosis runbook for a data service`, không mở bằng định nghĩa. Cho hai trace gần giống nhau nhưng khác đúng một state boundary; learner phải chọn probe tiếp theo trước khi được xem đáp án.

Bài tập seed dùng chính lab của DE-L075, sau đó đổi constraint đủ mạnh để buộc giữ hoặc đảo quyết định. Người dạy chấm reasoning chain và evidence, không chấm việc learner đoán đúng tên công cụ.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `A diagnosis runbook for a data service` dùng điều kiện hoàn thành sau: Người ngoài xử lý được ≥ 3/5 tình huống chỉ bằng sổ tay, và bản sửa sau đó giảm được số câu phải hỏi. Mỗi probe phải có prediction, failure signal và independent oracle.

### Probe 1: state transition và invariant

**Mệnh đề P1 cần kiểm.** Bài ghép: biến mọi kỹ năng chẩn đoán trong module thành một sổ tay dùng được lúc ba giờ sáng.

**Thiết kế phép thử.** Với `wiki.de-foundation.a-diagnosis-runbook-for-a-data-service`, tạo positive và negative control chỉ khác một điều kiện; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P1 cần giữ.** Với `wiki.de-foundation.a-diagnosis-runbook-for-a-data-service`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề P2 cần kiểm.** Viết sổ tay năm mục mà một người khác dùng được để chẩn đoán và khắc phục, không cần hỏi.

**Thiết kế phép thử.** Với `wiki.de-foundation.a-diagnosis-runbook-for-a-data-service`, tạo boundary case ngay trước và sau ngưỡng; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P2 cần giữ.** Với `wiki.de-foundation.a-diagnosis-runbook-for-a-data-service`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề P3 cần kiểm.** Tầng *đánh giá*.

**Thiết kế phép thử.** Với `wiki.de-foundation.a-diagnosis-runbook-for-a-data-service`, tạo replay cùng identity nhưng đổi state; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P3 cần giữ.** Với `wiki.de-foundation.a-diagnosis-runbook-for-a-data-service`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề P4 cần kiểm.** Viết sổ tay năm mục cho dịch vụ ở lesson 69.

**Thiết kế phép thử.** Với `wiki.de-foundation.a-diagnosis-runbook-for-a-data-service`, tạo failure inject trước và sau transition bền vững; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P4 cần giữ.** Với `wiki.de-foundation.a-diagnosis-runbook-for-a-data-service`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề P5 cần kiểm.** Viết bước dạng kiểm tra nhật ký mà không nói tìm gì · đặt ngưỡng bằng tính từ · bỏ bước xác nhận đã hồi phục · viết cho người đã biết hệ.

**Thiết kế phép thử.** Với `wiki.de-foundation.a-diagnosis-runbook-for-a-data-service`, tạo changed scale làm cost model đổi; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P5 cần giữ.** Với `wiki.de-foundation.a-diagnosis-runbook-for-a-data-service`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề P6 cần kiểm.** Người ngoài xử lý được ≥ 3/5 tình huống chỉ bằng sổ tay, và bản sửa sau đó giảm được số câu phải hỏi.

**Thiết kế phép thử.** Với `wiki.de-foundation.a-diagnosis-runbook-for-a-data-service`, tạo adversarial order, skew hoặc packet timing; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P6 cần giữ.** Với `wiki.de-foundation.a-diagnosis-runbook-for-a-data-service`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề P7 cần kiểm.** Bài ghép: biến mọi kỹ năng chẩn đoán trong module thành một sổ tay dùng được lúc ba giờ sáng.

**Thiết kế phép thử.** Với `wiki.de-foundation.a-diagnosis-runbook-for-a-data-service`, tạo fresh environment không cache; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P7 cần giữ.** Với `wiki.de-foundation.a-diagnosis-runbook-for-a-data-service`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề P8 cần kiểm.** Viết sổ tay năm mục mà một người khác dùng được để chẩn đoán và khắc phục, không cần hỏi.

**Thiết kế phép thử.** Với `wiki.de-foundation.a-diagnosis-runbook-for-a-data-service`, tạo independent oracle không dùng chung implementation; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P8 cần giữ.** Với `wiki.de-foundation.a-diagnosis-runbook-for-a-data-service`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề P9 cần kiểm.** Tầng *đánh giá*.

**Thiết kế phép thử.** Với `wiki.de-foundation.a-diagnosis-runbook-for-a-data-service`, tạo partial progress rồi restart; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P9 cần giữ.** Với `wiki.de-foundation.a-diagnosis-runbook-for-a-data-service`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề P10 cần kiểm.** Viết sổ tay năm mục cho dịch vụ ở lesson 69.

**Thiết kế phép thử.** Với `wiki.de-foundation.a-diagnosis-runbook-for-a-data-service`, tạo missing evidence phải abstain; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P10 cần giữ.** Với `wiki.de-foundation.a-diagnosis-runbook-for-a-data-service`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề P11 cần kiểm.** Viết bước dạng kiểm tra nhật ký mà không nói tìm gì · đặt ngưỡng bằng tính từ · bỏ bước xác nhận đã hồi phục · viết cho người đã biết hệ.

**Thiết kế phép thử.** Với `wiki.de-foundation.a-diagnosis-runbook-for-a-data-service`, tạo reviewer tái hiện từ evidence package; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P11 cần giữ.** Với `wiki.de-foundation.a-diagnosis-runbook-for-a-data-service`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề P12 cần kiểm.** Người ngoài xử lý được ≥ 3/5 tình huống chỉ bằng sổ tay, và bản sửa sau đó giảm được số câu phải hỏi.

**Thiết kế phép thử.** Với `wiki.de-foundation.a-diagnosis-runbook-for-a-data-service`, tạo constraint đổi đủ để quyết định đảo; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P12 cần giữ.** Với `wiki.de-foundation.a-diagnosis-runbook-for-a-data-service`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên khiến mô hình `A diagnosis runbook for a data service` không còn đúng là gì?

<details><summary>Đáp án</summary>Viết bước dạng kiểm tra nhật ký mà không nói tìm gì · đặt ngưỡng bằng tính từ · bỏ bước xác nhận đã hồi phục · viết cho người đã biết hệ.</details>

2. Evidence nào phân biệt được hai state dễ nhầm?

<details><summary>Đáp án</summary>Tầng *đánh giá*. Objective đo chất lượng sổ tay bằng kết quả của người dùng nó chứ bằng độ dày. Kiểm bằng phép thử với người ngoài; đạt khi họ xử lý được ít nhất ba trong năm tình huống mà không phải hỏi.</details>

3. Khi constraint đổi, điều gì quyết định giữ hay đảo lựa chọn?

<details><summary>Đáp án</summary>Người ngoài xử lý được ≥ 3/5 tình huống chỉ bằng sổ tay, và bản sửa sau đó giảm được số câu phải hỏi.</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `A diagnosis runbook for a data service` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Hành vi phụ thuộc kernel, distribution, library, network path hoặc hardware phải được kiểm lại trên target đã ghi version.
- Concept key `ck.de.a-diagnosis-runbook-for-a-data-service` đang ở trạng thái `proposed`; note chưa được tính là canonical registry coverage.
- Một trace đơn lẻ không chứng minh capacity, reliability hoặc security cho population khác.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-TLPI-2010]]
2. [[SRC-GOOGLE-SRE-MONITORING]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-TLPI-2010]] — `src.book.tlpi.2010` | Chapters 4–39, 49–50, 61 và 63 theo scope record; PDF 113–1418 | mechanism và boundary liên quan trực tiếp tới `A diagnosis runbook for a data service` | cơ chế, quyết định, case và probe | Đã phủ | phần ngoài objective DE-L075 |
| [[SRC-GOOGLE-SRE-MONITORING]] — `src.web.google-sre-monitoring` | Monitoring distributed systems; accessed 2026-10-01 | mechanism và boundary liên quan trực tiếp tới `A diagnosis runbook for a data service` | cơ chế, quyết định, case và probe | Đã phủ | phần ngoài objective DE-L075 |

## Key takeaways
- Viết sổ tay năm mục mà một người khác dùng được để chẩn đoán và khắc phục, không cần hỏi.
- Người ngoài xử lý được ≥ 3/5 tình huống chỉ bằng sổ tay, và bản sửa sau đó giảm được số câu phải hỏi.
- `A diagnosis runbook for a data service` chỉ có nghĩa trong scope, state, identity và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.
