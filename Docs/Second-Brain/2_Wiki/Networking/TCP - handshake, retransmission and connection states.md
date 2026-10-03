---
note_id: wiki.de-foundation.tcp-handshake-retransmission-and-connection-states
concept_key: ck.de.tcp-handshake-retransmission-and-connection-states
concept_key_status: canonical
note_type: concept-deep-dive
status: canonical
approved_by: second-brain-owner
approved_at: 2026-10-03
approval_scope: all-registered-notes
canonical_since: 2026-10-03
language: vi
created: 2026-10-02
last_verified: 2026-10-02
review_after: 2027-04-02
editorial_pass: humanized-v3
primary_question: Làm thế nào mô hình, đo và ra quyết định đúng về TCP - handshake, retransmission and connection states?
source_ids:
  - src.book.kurose-ross-networking.8e
  - src.standard.rfc9293-tcp
relationships:
  builds_on: [wiki.de-foundation.dns-resolution-caching-and-stale-records]
  prerequisite_of: [wiki.de-foundation.tls-certificates-verification-and-the-handshake-cost]
  related_to: []
aliases: [TCP - handshake, retransmission and connection states]
tags: [wiki/networking, de-foundation, module-6]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/079-tcp-handshake-retransmission-and-connection-states.md
---

# TCP - handshake, retransmission and connection states

**Tóm tắt bản chất:** Từ một bản bắt gói, phân biệt được truyền lại, đặt lại kết nối và lỗi ở tầng ứng dụng. Cơ chế chỉ có giá trị khi workload, version, state owner và failure boundary đã được khóa; một con số đẹp ngoài bốn điều kiện đó không đủ để ra quyết định.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, đo và ra quyết định đúng về TCP - handshake, retransmission and connection states?

## Nỗi Đau & Động Lực

Nhầm đặt lại kết nối với hết giờ · mở kết nối mới cho mỗi yêu cầu · bỏ qua trạng thái chờ đóng tới khi cạn cổng · kết luận từ nhật ký ứng dụng mà không bắt gói. Đây không phải danh sách lỗi cú pháp. Mỗi lỗi làm người vận hành chọn nhầm owner hoặc chữa symptom ở layer sau, khiến thời gian phục hồi tăng dù command vừa chạy trả về thành công.

Năng lực cần giữ sau bài là: Từ một bản bắt gói, phân biệt được truyền lại, đặt lại kết nối và lỗi ở tầng ứng dụng. Nếu learner chỉ nhắc lại định nghĩa nhưng không phân biệt được hai state gần nhau trên số đo, bài chưa đạt.

## Cơ Chế Tác Động

Giao thức bảo đảm thứ tự và không mất dữ liệu, và mọi bảo đảm đó đều có cái giá quan sát được. Bắt tay ba bước và vì sao kết nối tốn ít nhất một vòng khứ hồi trước khi gửi được byte dữ liệu đầu tiên; từ đó suy ra vì sao mở lại kết nối cho mỗi yêu cầu là lãng phí và vì sao cần hồ kết nối. Số thứ tự và xác nhận, truyền lại khi mất gói, và vì sao truyền lại làm độ trễ tăng đột biến chứ tăng dần. Cửa sổ và kiểm soát luồng: bên nhận báo mình còn chứa được bao nhiêu, đây là áp lực ngược ở tầng mạng và cùng ý tưởng với hàng đợi có giới hạn ở lesson 30. Đóng kết nối và trạng thái chờ đóng: vì sao nó tồn tại và vì sao tích tụ nhiều gây cạn cổng tạm. Đặt lại kết nối khác hết giờ: một cái là bên kia chủ động từ chối, một cái là im lặng.

Tách ba lớp khi đọc cơ chế `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`: declared state là điều cấu hình hoặc API yêu cầu; executed state là việc runtime thực sự làm; consumer-visible state là điều client hay operator quan sát. Ba lớp có thể lệch nhau vì cache, buffering, retry, scheduling, queue hoặc failure giữa hai transition. Evidence phải chỉ ra lớp nào đang được đo.

## Bản Đồ Quyết Định

| Bước | Câu hỏi phải khóa | Điều kiện đạt |
|---|---|---|
| Layer | Xác định hop và protocol state | Không gọi mọi lỗi là network |
| Budget | Chia deadline và capacity theo hop | Không reset budget sau retry |
| Identity | Khóa connection, request và operation identity | Không gộp duplicate với retry |
| Evidence | Ghép client, DNS, transport, TLS, HTTP và server timeline | Clock và correlation được công bố |

Quy tắc mặc định là chọn phép giải thích đơn giản nhất qua được hard constraints, rồi viết trước reversal trigger. Với `TCP - handshake, retransmission and connection states`, absence of error không phải pass; pass cần observation đúng grain, một oracle độc lập và changed-constraint case đủ làm model có cơ hội thất bại.

## Case Study Thực Chiến: TCP - handshake, retransmission and connection states

Bắt gói cho ba tình huống: mạng mất gói mô phỏng, dịch vụ từ chối kết nối, và dịch vụ trả về lỗi ứng dụng. Với mỗi bản, chỉ ra gói nào là bằng chứng và phân loại. Đếm số socket ở trạng thái chờ đóng sau khi chạy 10.000 kết nối ngắn, rồi chạy lại với hồ kết nối và đếm lại.

Trong case `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`, learner ghi expected transition, input snapshot, version và giới hạn an toàn trước khi chạy. Sau execution, họ giữ raw counter, timestamp, exit status, state trước–sau và giải thích delta bằng mechanism ở trên. Đánh giá không cho phép sửa expected result sau khi nhìn output mà không ghi change record.

Biến thể khó hơn đổi một constraint có khả năng đảo kết luận: workload shape, memory pressure, connection reuse, retry budget, permission hoặc dependency direction. Tầng *phân tích*. Objective là đọc bằng chứng thô, kỹ năng mà không đọc được thì mọi chẩn đoán mạng đều là phỏng đoán. Kiểm bằng ba bản bắt gói; đạt khi phân loại đúng ít nhất hai và chỉ ra được gói cụ thể làm bằng chứng.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Nhầm đặt lại kết nối với hết giờ. **Thực tế:** tín hiệu chỉ chứng minh điều nó đo trong đúng scope; state ở layer khác vẫn có thể trái ngược. **Vì sao nghe hợp lý:** happy path nhỏ thường không chạm queue, cache, partial progress hoặc restart.

**Hiểu lầm:** mở kết nối mới cho mỗi yêu cầu. **Thực tế:** tool và API cung cấp primitive, không tự cấp ownership, deadline, idempotency hay recovery policy. **Vì sao nghe hợp lý:** syntax gọn che mất protocol và lifecycle phía dưới.

Với `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`, một edge case đáng giữ là observation đúng nhưng diagnosis sai: counter tăng thật, song nguyên nhân điều khiển nằm ở layer trước. Muốn tránh, timeline phải nối trigger tới consumer harm và ghi rõ negative control nào đã loại giả thuyết cạnh tranh.

## Nếu Bạn Dạy Lại Điều Này...

Mở bài bằng một dự đoán dễ sai về `TCP - handshake, retransmission and connection states`, không mở bằng định nghĩa. Cho hai trace gần giống nhau nhưng khác đúng một state boundary; learner phải chọn probe tiếp theo trước khi được xem đáp án.

Bài tập seed dùng chính lab của DE-L079, sau đó đổi constraint đủ mạnh để buộc giữ hoặc đảo quyết định. Người dạy chấm reasoning chain và evidence, không chấm việc learner đoán đúng tên công cụ.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `TCP - handshake, retransmission and connection states` dùng điều kiện hoàn thành sau: Phân loại đúng ≥ 2/3 bản bắt gói kèm gói làm bằng chứng, và số socket chờ đóng giảm rõ rệt khi dùng hồ kết nối. Mỗi probe phải có prediction, failure signal và independent oracle.

### Probe 1: state transition và invariant

**Mệnh đề P1 cần kiểm.** Giao thức bảo đảm thứ tự và không mất dữ liệu, và mọi bảo đảm đó đều có cái giá quan sát được.

**Thiết kế phép thử cho `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`.** Với `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`, tạo positive và negative control chỉ khác một điều kiện; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P1 cần giữ.** Với `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề P2 cần kiểm.** Từ một bản bắt gói, phân biệt được truyền lại, đặt lại kết nối và lỗi ở tầng ứng dụng.

**Thiết kế phép thử cho `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`.** Với `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`, tạo boundary case ngay trước và sau ngưỡng; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P2 cần giữ.** Với `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề P3 cần kiểm.** Tầng *phân tích*.

**Thiết kế phép thử cho `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`.** Với `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`, tạo replay cùng identity nhưng đổi state; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P3 cần giữ.** Với `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề P4 cần kiểm.** Bắt gói cho ba tình huống: mạng mất gói mô phỏng, dịch vụ từ chối kết nối, và dịch vụ trả về lỗi ứng dụng.

**Thiết kế phép thử cho `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`.** Với `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`, tạo failure inject trước và sau transition bền vững; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P4 cần giữ.** Với `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề P5 cần kiểm.** Nhầm đặt lại kết nối với hết giờ · mở kết nối mới cho mỗi yêu cầu · bỏ qua trạng thái chờ đóng tới khi cạn cổng · kết luận từ nhật ký ứng dụng mà không bắt gói.

**Thiết kế phép thử cho `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`.** Với `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`, tạo changed scale làm cost model đổi; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P5 cần giữ.** Với `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề P6 cần kiểm.** Phân loại đúng ≥ 2/3 bản bắt gói kèm gói làm bằng chứng, và số socket chờ đóng giảm rõ rệt khi dùng hồ kết nối.

**Thiết kế phép thử cho `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`.** Với `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`, tạo adversarial order, skew hoặc packet timing; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P6 cần giữ.** Với `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề P7 cần kiểm.** Giao thức bảo đảm thứ tự và không mất dữ liệu, và mọi bảo đảm đó đều có cái giá quan sát được.

**Thiết kế phép thử cho `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`.** Với `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`, tạo fresh environment không cache; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P7 cần giữ.** Với `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề P8 cần kiểm.** Từ một bản bắt gói, phân biệt được truyền lại, đặt lại kết nối và lỗi ở tầng ứng dụng.

**Thiết kế phép thử cho `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`.** Với `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`, tạo independent oracle không dùng chung implementation; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P8 cần giữ.** Với `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề P9 cần kiểm.** Tầng *phân tích*.

**Thiết kế phép thử cho `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`.** Với `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`, tạo partial progress rồi restart; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P9 cần giữ.** Với `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề P10 cần kiểm.** Bắt gói cho ba tình huống: mạng mất gói mô phỏng, dịch vụ từ chối kết nối, và dịch vụ trả về lỗi ứng dụng.

**Thiết kế phép thử cho `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`.** Với `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`, tạo missing evidence phải abstain; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P10 cần giữ.** Với `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề P11 cần kiểm.** Nhầm đặt lại kết nối với hết giờ · mở kết nối mới cho mỗi yêu cầu · bỏ qua trạng thái chờ đóng tới khi cạn cổng · kết luận từ nhật ký ứng dụng mà không bắt gói.

**Thiết kế phép thử cho `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`.** Với `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`, tạo reviewer tái hiện từ evidence package; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P11 cần giữ.** Với `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề P12 cần kiểm.** Phân loại đúng ≥ 2/3 bản bắt gói kèm gói làm bằng chứng, và số socket chờ đóng giảm rõ rệt khi dùng hồ kết nối.

**Thiết kế phép thử cho `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`.** Với `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`, tạo constraint đổi đủ để quyết định đảo; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P12 cần giữ.** Với `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên khiến mô hình `TCP - handshake, retransmission and connection states` không còn đúng là gì?

<details><summary>Đáp án</summary>Nhầm đặt lại kết nối với hết giờ · mở kết nối mới cho mỗi yêu cầu · bỏ qua trạng thái chờ đóng tới khi cạn cổng · kết luận từ nhật ký ứng dụng mà không bắt gói.</details>

2. Evidence nào phân biệt được hai state dễ nhầm?

<details><summary>Đáp án</summary>Tầng *phân tích*. Objective là đọc bằng chứng thô, kỹ năng mà không đọc được thì mọi chẩn đoán mạng đều là phỏng đoán. Kiểm bằng ba bản bắt gói; đạt khi phân loại đúng ít nhất hai và chỉ ra được gói cụ thể làm bằng chứng.</details>

3. Khi constraint đổi, điều gì quyết định giữ hay đảo lựa chọn?

<details><summary>Đáp án</summary>Phân loại đúng ≥ 2/3 bản bắt gói kèm gói làm bằng chứng, và số socket chờ đóng giảm rõ rệt khi dùng hồ kết nối.</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `TCP - handshake, retransmission and connection states` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Hành vi phụ thuộc kernel, distribution, library, network path hoặc hardware phải được kiểm lại trên target đã ghi version.
- Concept key `ck.de.tcp-handshake-retransmission-and-connection-states` đã được owner phê duyệt `canonical`; note thuộc canonical registry coverage. Trạng thái này không tự chứng minh learner mastery.
- Một trace đơn lẻ không chứng minh capacity, reliability hoặc security cho population khác.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-KUROSE-ROSS-NETWORKING-8E]]
2. [[SRC-RFC-9293-TCP]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-KUROSE-ROSS-NETWORKING-8E]] — `src.book.kurose-ross-networking.8e` | §§1.4, 2.2, 2.4, 2.7, 3.5–3.7, 4.5, 6.6.1 và Chapter 8; PDF 67–682 | mechanism và boundary liên quan trực tiếp tới `TCP - handshake, retransmission and connection states` | cơ chế, quyết định, case và probe | Đã phủ | phần ngoài objective DE-L079 |
| [[SRC-RFC-9293-TCP]] — `src.standard.rfc9293-tcp` | RFC 9293 service model, state machine và connection lifecycle | mechanism và boundary liên quan trực tiếp tới `TCP - handshake, retransmission and connection states` | cơ chế, quyết định, case và probe | Đã phủ | phần ngoài objective DE-L079 |

## Key takeaways
- Từ một bản bắt gói, phân biệt được truyền lại, đặt lại kết nối và lỗi ở tầng ứng dụng.
- Phân loại đúng ≥ 2/3 bản bắt gói kèm gói làm bằng chứng, và số socket chờ đóng giảm rõ rệt khi dùng hồ kết nối.
- `TCP - handshake, retransmission and connection states` chỉ có nghĩa trong scope, state, identity và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule — kiểm chứng `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`

> [!important] Phân loại mệnh đề
> Với `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states`, sơ đồ, ví dụ và artifact về **TCP - handshake, retransmission and connection states** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.book.kurose-ross-networking.8e"] --> B["Khóa boundary"]
    B --> M["Cơ chế: TCP - handshake, retransmission and connection states"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **TCP - handshake, retransmission and connection states**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```yaml
concept_id: "wiki.de-foundation.tcp-handshake-retransmission-and-connection-states"
concept: "TCP - handshake, retransmission and connection states"
primary_question: "Làm thế nào mô hình, đo và ra quyết định đúng về TCP - handshake, retransmission and connection states?"
decision_contract:
  input_boundary: "Ghi population, thời điểm, owner và điều chưa biết"
  hard_constraints:
    - "Không vượt quyền hoặc privacy boundary"
    - "Không dùng cùng một assumption làm cả implementation và oracle"
  accept_when: "Có observation phân biệt được các lựa chọn"
  reversal_trigger: "Một hard constraint sai hoặc evidence mới đổi recommendation"
evidence_to_keep:
  - "input snapshot"
  - "chosen and rejected options"
  - "independent review result"
```

Artifact của `wiki.de-foundation.tcp-handshake-retransmission-and-connection-states` buộc người dùng ghi boundary, oracle và reversal trigger cho **TCP - handshake, retransmission and connection states**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

<!-- ATOMIC-EXECUTION-CAPSULE:END -->
