# Phase 2: Machine, Operating System and Network
# Module 6: Networking from Packet to API
# Lesson 81: HTTP semantics - methods, status, idempotency and caching

## Mục tiêu bài học

**Năng lực cần chứng minh.** Quyết định một yêu cầu thất bại có được thử lại hay không dựa trên phương thức và mã trạng thái.

**Điều kiện hoàn thành.** Quyết định đúng ≥ 8/10 tổ hợp kèm giải thích bằng tính bất biến, và đọc đúng tiêu đề chờ từ giao diện thật.

**Kiến thức và cơ chế.** Giao thức ứng dụng phổ biến nhất, và phần quan trọng với người làm dữ liệu là ngữ nghĩa chứ cú pháp. Phương thức và hai tính chất tách bạch: an toàn nghĩa là không đổi trạng thái, bất biến nghĩa là gọi lại cho cùng kết quả; **bất biến là tính chất quyết định có được thử lại hay không**, và đây là cầu nối trực tiếp tới lesson 30. Mã trạng thái theo nhóm và cách xử lý từng nhóm khi nạp dữ liệu: nhóm lỗi máy khách thường không nên thử lại, nhóm lỗi máy chủ thì nên, và mã báo quá nhiều yêu cầu cần chờ theo tiêu đề máy chủ trả về. Tiêu đề quan trọng với việc nạp dữ liệu: nén, kiểu nội dung, phân trang, và giới hạn tốc độ. Bộ đệm và các tiêu đề điều khiển. Giữ kết nối sống và ghép nhiều yêu cầu trên một kết nối, nối lại chi phí bắt tay ở lesson 79 và 80.


# HTTP semantics - methods, status, idempotency and caching

**Tóm tắt bản chất:** Quyết định một yêu cầu thất bại có được thử lại hay không dựa trên phương thức và mã trạng thái. Cơ chế chỉ có giá trị khi workload, version, state owner và failure boundary đã được khóa; một con số đẹp ngoài bốn điều kiện đó không đủ để ra quyết định.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, đo và ra quyết định đúng về HTTP semantics - methods, status, idempotency and caching?

## Nỗi Đau & Động Lực

Thử lại mọi lỗi · thử lại một yêu cầu tạo tài nguyên mà không có khoá bất biến · bỏ qua tiêu đề chờ của giới hạn tốc độ · nhầm an toàn với bất biến. Đây không phải danh sách lỗi cú pháp. Mỗi lỗi làm người vận hành chọn nhầm owner hoặc chữa symptom ở layer sau, khiến thời gian phục hồi tăng dù command vừa chạy trả về thành công.

Năng lực cần giữ sau bài là: Quyết định một yêu cầu thất bại có được thử lại hay không dựa trên phương thức và mã trạng thái. Nếu learner chỉ nhắc lại định nghĩa nhưng không phân biệt được hai state gần nhau trên số đo, bài chưa đạt.

## Cơ Chế Tác Động

Giao thức ứng dụng phổ biến nhất, và phần quan trọng với người làm dữ liệu là ngữ nghĩa chứ cú pháp. Phương thức và hai tính chất tách bạch: an toàn nghĩa là không đổi trạng thái, bất biến nghĩa là gọi lại cho cùng kết quả; **bất biến là tính chất quyết định có được thử lại hay không**, và đây là cầu nối trực tiếp tới lesson 30. Mã trạng thái theo nhóm và cách xử lý từng nhóm khi nạp dữ liệu: nhóm lỗi máy khách thường không nên thử lại, nhóm lỗi máy chủ thì nên, và mã báo quá nhiều yêu cầu cần chờ theo tiêu đề máy chủ trả về. Tiêu đề quan trọng với việc nạp dữ liệu: nén, kiểu nội dung, phân trang, và giới hạn tốc độ. Bộ đệm và các tiêu đề điều khiển. Giữ kết nối sống và ghép nhiều yêu cầu trên một kết nối, nối lại chi phí bắt tay ở lesson 79 và 80.

Tách ba lớp khi đọc cơ chế `wiki.de-foundation.http-semantics-methods-status-idempotency-and-caching`: declared state là điều cấu hình hoặc API yêu cầu; executed state là việc runtime thực sự làm; consumer-visible state là điều client hay operator quan sát. Ba lớp có thể lệch nhau vì cache, buffering, retry, scheduling, queue hoặc failure giữa hai transition. Evidence phải chỉ ra lớp nào đang được đo.

## Bản Đồ Quyết Định

| Bước | Câu hỏi phải khóa | Điều kiện đạt |
|---|---|---|
| Layer | Xác định hop và protocol state | Không gọi mọi lỗi là network |
| Budget | Chia deadline và capacity theo hop | Không reset budget sau retry |
| Identity | Khóa connection, request và operation identity | Không gộp duplicate với retry |
| Evidence | Ghép client, DNS, transport, TLS, HTTP và server timeline | Clock và correlation được công bố |

Quy tắc mặc định là chọn phép giải thích đơn giản nhất qua được hard constraints, rồi viết trước reversal trigger. Với `HTTP semantics - methods, status, idempotency and caching`, absence of error không phải pass; pass cần observation đúng grain, một oracle độc lập và changed-constraint case đủ làm model có cơ hội thất bại.

## Case Study Thực Chiến: HTTP semantics - methods, status, idempotency and caching

Cho mười tổ hợp phương thức và mã trạng thái. Với mỗi tổ hợp, quyết định có thử lại không và giải thích bằng tính bất biến cùng ngữ nghĩa mã trạng thái. Gọi một giao diện thật có giới hạn tốc độ và đọc tiêu đề cho biết phải chờ bao lâu.

Trong case `wiki.de-foundation.http-semantics-methods-status-idempotency-and-caching`, learner ghi expected transition, input snapshot, version và giới hạn an toàn trước khi chạy. Sau execution, họ giữ raw counter, timestamp, exit status, state trước–sau và giải thích delta bằng mechanism ở trên. Đánh giá không cho phép sửa expected result sau khi nhìn output mà không ghi change record.

Biến thể khó hơn đổi một constraint có khả năng đảo kết luận: workload shape, memory pressure, connection reuse, retry budget, permission hoặc dependency direction. Tầng *hiểu*. Bài lý thuyết chuẩn bị cho lesson 83 và cho M16; chưa đòi cài đặt. Kiểm bằng bảng quyết định trên mười tổ hợp; đạt khi đúng ít nhất tám và giải thích được bằng tính bất biến chứ bằng thói quen.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Thử lại mọi lỗi. **Thực tế:** tín hiệu chỉ chứng minh điều nó đo trong đúng scope; state ở layer khác vẫn có thể trái ngược. **Vì sao nghe hợp lý:** happy path nhỏ thường không chạm queue, cache, partial progress hoặc restart.

**Hiểu lầm:** thử lại một yêu cầu tạo tài nguyên mà không có khoá bất biến. **Thực tế:** tool và API cung cấp primitive, không tự cấp ownership, deadline, idempotency hay recovery policy. **Vì sao nghe hợp lý:** syntax gọn che mất protocol và lifecycle phía dưới.

Với `wiki.de-foundation.http-semantics-methods-status-idempotency-and-caching`, một edge case đáng giữ là observation đúng nhưng diagnosis sai: counter tăng thật, song nguyên nhân điều khiển nằm ở layer trước. Muốn tránh, timeline phải nối trigger tới consumer harm và ghi rõ negative control nào đã loại giả thuyết cạnh tranh.

## Nếu Bạn Dạy Lại Điều Này...

Mở bài bằng một dự đoán dễ sai về `HTTP semantics - methods, status, idempotency and caching`, không mở bằng định nghĩa. Cho hai trace gần giống nhau nhưng khác đúng một state boundary; learner phải chọn probe tiếp theo trước khi được xem đáp án.

Bài tập seed dùng chính lab của DE-L081, sau đó đổi constraint đủ mạnh để buộc giữ hoặc đảo quyết định. Người dạy chấm reasoning chain và evidence, không chấm việc learner đoán đúng tên công cụ.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `HTTP semantics - methods, status, idempotency and caching` dùng điều kiện hoàn thành sau: Quyết định đúng ≥ 8/10 tổ hợp kèm giải thích bằng tính bất biến, và đọc đúng tiêu đề chờ từ giao diện thật. Mỗi probe phải có prediction, failure signal và independent oracle.

### Probe 1: state transition và invariant

**Mệnh đề P1 cần kiểm.** Giao thức ứng dụng phổ biến nhất, và phần quan trọng với người làm dữ liệu là ngữ nghĩa chứ cú pháp.

**Thiết kế phép thử.** Với `wiki.de-foundation.http-semantics-methods-status-idempotency-and-caching`, tạo positive và negative control chỉ khác một điều kiện; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P1 cần giữ.** Với `wiki.de-foundation.http-semantics-methods-status-idempotency-and-caching`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề P2 cần kiểm.** Quyết định một yêu cầu thất bại có được thử lại hay không dựa trên phương thức và mã trạng thái.

**Thiết kế phép thử.** Với `wiki.de-foundation.http-semantics-methods-status-idempotency-and-caching`, tạo boundary case ngay trước và sau ngưỡng; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P2 cần giữ.** Với `wiki.de-foundation.http-semantics-methods-status-idempotency-and-caching`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề P3 cần kiểm.** Tầng *hiểu*.

**Thiết kế phép thử.** Với `wiki.de-foundation.http-semantics-methods-status-idempotency-and-caching`, tạo replay cùng identity nhưng đổi state; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P3 cần giữ.** Với `wiki.de-foundation.http-semantics-methods-status-idempotency-and-caching`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề P4 cần kiểm.** Cho mười tổ hợp phương thức và mã trạng thái.

**Thiết kế phép thử.** Với `wiki.de-foundation.http-semantics-methods-status-idempotency-and-caching`, tạo failure inject trước và sau transition bền vững; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P4 cần giữ.** Với `wiki.de-foundation.http-semantics-methods-status-idempotency-and-caching`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề P5 cần kiểm.** Thử lại mọi lỗi · thử lại một yêu cầu tạo tài nguyên mà không có khoá bất biến · bỏ qua tiêu đề chờ của giới hạn tốc độ · nhầm an toàn với bất biến.

**Thiết kế phép thử.** Với `wiki.de-foundation.http-semantics-methods-status-idempotency-and-caching`, tạo changed scale làm cost model đổi; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P5 cần giữ.** Với `wiki.de-foundation.http-semantics-methods-status-idempotency-and-caching`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề P6 cần kiểm.** Quyết định đúng ≥ 8/10 tổ hợp kèm giải thích bằng tính bất biến, và đọc đúng tiêu đề chờ từ giao diện thật.

**Thiết kế phép thử.** Với `wiki.de-foundation.http-semantics-methods-status-idempotency-and-caching`, tạo adversarial order, skew hoặc packet timing; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P6 cần giữ.** Với `wiki.de-foundation.http-semantics-methods-status-idempotency-and-caching`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề P7 cần kiểm.** Giao thức ứng dụng phổ biến nhất, và phần quan trọng với người làm dữ liệu là ngữ nghĩa chứ cú pháp.

**Thiết kế phép thử.** Với `wiki.de-foundation.http-semantics-methods-status-idempotency-and-caching`, tạo fresh environment không cache; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P7 cần giữ.** Với `wiki.de-foundation.http-semantics-methods-status-idempotency-and-caching`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề P8 cần kiểm.** Quyết định một yêu cầu thất bại có được thử lại hay không dựa trên phương thức và mã trạng thái.

**Thiết kế phép thử.** Với `wiki.de-foundation.http-semantics-methods-status-idempotency-and-caching`, tạo independent oracle không dùng chung implementation; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P8 cần giữ.** Với `wiki.de-foundation.http-semantics-methods-status-idempotency-and-caching`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề P9 cần kiểm.** Tầng *hiểu*.

**Thiết kế phép thử.** Với `wiki.de-foundation.http-semantics-methods-status-idempotency-and-caching`, tạo partial progress rồi restart; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P9 cần giữ.** Với `wiki.de-foundation.http-semantics-methods-status-idempotency-and-caching`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề P10 cần kiểm.** Cho mười tổ hợp phương thức và mã trạng thái.

**Thiết kế phép thử.** Với `wiki.de-foundation.http-semantics-methods-status-idempotency-and-caching`, tạo missing evidence phải abstain; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P10 cần giữ.** Với `wiki.de-foundation.http-semantics-methods-status-idempotency-and-caching`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề P11 cần kiểm.** Thử lại mọi lỗi · thử lại một yêu cầu tạo tài nguyên mà không có khoá bất biến · bỏ qua tiêu đề chờ của giới hạn tốc độ · nhầm an toàn với bất biến.

**Thiết kế phép thử.** Với `wiki.de-foundation.http-semantics-methods-status-idempotency-and-caching`, tạo reviewer tái hiện từ evidence package; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P11 cần giữ.** Với `wiki.de-foundation.http-semantics-methods-status-idempotency-and-caching`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề P12 cần kiểm.** Quyết định đúng ≥ 8/10 tổ hợp kèm giải thích bằng tính bất biến, và đọc đúng tiêu đề chờ từ giao diện thật.

**Thiết kế phép thử.** Với `wiki.de-foundation.http-semantics-methods-status-idempotency-and-caching`, tạo constraint đổi đủ để quyết định đảo; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P12 cần giữ.** Với `wiki.de-foundation.http-semantics-methods-status-idempotency-and-caching`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên khiến mô hình `HTTP semantics - methods, status, idempotency and caching` không còn đúng là gì?

<details><summary>Đáp án</summary>Thử lại mọi lỗi · thử lại một yêu cầu tạo tài nguyên mà không có khoá bất biến · bỏ qua tiêu đề chờ của giới hạn tốc độ · nhầm an toàn với bất biến.</details>

2. Evidence nào phân biệt được hai state dễ nhầm?

<details><summary>Đáp án</summary>Tầng *hiểu*. Bài lý thuyết chuẩn bị cho lesson 83 và cho M16; chưa đòi cài đặt. Kiểm bằng bảng quyết định trên mười tổ hợp; đạt khi đúng ít nhất tám và giải thích được bằng tính bất biến chứ bằng thói quen.</details>

3. Khi constraint đổi, điều gì quyết định giữ hay đảo lựa chọn?

<details><summary>Đáp án</summary>Quyết định đúng ≥ 8/10 tổ hợp kèm giải thích bằng tính bất biến, và đọc đúng tiêu đề chờ từ giao diện thật.</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `HTTP semantics - methods, status, idempotency and caching` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Hành vi phụ thuộc kernel, distribution, library, network path hoặc hardware phải được kiểm lại trên target đã ghi version.
- Concept key `ck.de.http-semantics-methods-status-idempotency-and-caching` đang ở trạng thái `proposed`; note chưa được tính là canonical registry coverage.
- Một trace đơn lẻ không chứng minh capacity, reliability hoặc security cho population khác.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-KUROSE-ROSS-NETWORKING-8E]]
2. [[SRC-RFC9110-HTTP-SEMANTICS]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-KUROSE-ROSS-NETWORKING-8E]] — `src.book.kurose-ross-networking.8e` | §§1.4, 2.2, 2.4, 2.7, 3.5–3.7, 4.5, 6.6.1 và Chapter 8; PDF 67–682 | mechanism và boundary liên quan trực tiếp tới `HTTP semantics - methods, status, idempotency and caching` | cơ chế, quyết định, case và probe | Đã phủ | phần ngoài objective DE-L081 |
| [[SRC-RFC9110-HTTP-SEMANTICS]] — `src.web.rfc9110-http-semantics` | RFC 9110 method, status, representation, cache và idempotent semantics | mechanism và boundary liên quan trực tiếp tới `HTTP semantics - methods, status, idempotency and caching` | cơ chế, quyết định, case và probe | Đã phủ | phần ngoài objective DE-L081 |

## Key takeaways
- Quyết định một yêu cầu thất bại có được thử lại hay không dựa trên phương thức và mã trạng thái.
- Quyết định đúng ≥ 8/10 tổ hợp kèm giải thích bằng tính bất biến, và đọc đúng tiêu đề chờ từ giao diện thật.
- `HTTP semantics - methods, status, idempotency and caching` chỉ có nghĩa trong scope, state, identity và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.
