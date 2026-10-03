# Phase 2: Machine, Operating System and Network
# Module 6: Networking from Packet to API
# Lesson 77: Layers, addresses and routing

## Mục tiêu bài học

**Năng lực cần chứng minh.** Tính được dải địa chỉ của một mạng con và dự đoán đường đi của một gói trước khi kiểm chứng bằng lệnh.

**Điều kiện hoàn thành.** Tính đúng ≥ 4/5 mạng con, và dự đoán đường đi khớp kết quả lệnh tra ở cả ba trường hợp.

**Kiến thức và cơ chế.** Mô hình phân tầng dùng để định vị vấn đề chứ để học thuộc: khi có sự cố, câu hỏi đầu tiên là nó nằm ở tầng nào. Địa chỉ và khối địa chỉ: cách đọc ký hiệu tiền tố và tính được dải địa chỉ của một mạng con, kỹ năng dùng trực tiếp khi thiết kế mạng riêng ở M24. Bảng định tuyến và cổng ra: máy quyết định gửi gói đi đâu bằng cách so địa chỉ đích với bảng định tuyến, và đọc được bảng đó là trả lời được câu gói này đi đường nào. Phân giải địa chỉ vật lý trong mạng cục bộ ở mức nhận biết. Đơn vị truyền tối đa và phân mảnh: gói vượt kích thước tối đa bị chia hoặc bị loại, và triệu chứng của nó rất dễ nhầm với lỗi ứng dụng vì kết nối thành công nhưng truyền dữ liệu lớn thì treo. Chuyển đổi địa chỉ và tường lửa: hai thứ đứng giữa và làm thay đổi những gì bên kia nhìn thấy.


# Layers, addresses and routing

**Tóm tắt bản chất:** Tính được dải địa chỉ của một mạng con và dự đoán đường đi của một gói trước khi kiểm chứng bằng lệnh. Cơ chế chỉ có giá trị khi workload, version, state owner và failure boundary đã được khóa; một con số đẹp ngoài bốn điều kiện đó không đủ để ra quyết định.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, đo và ra quyết định đúng về Layers, addresses and routing?

## Nỗi Đau & Động Lực

Học thuộc bảy tầng mà không dùng để định vị · tính nhầm số địa chỉ dùng được · bỏ qua đơn vị truyền tối đa nên không giải thích được lỗi treo khi truyền dữ liệu lớn. Đây không phải danh sách lỗi cú pháp. Mỗi lỗi làm người vận hành chọn nhầm owner hoặc chữa symptom ở layer sau, khiến thời gian phục hồi tăng dù command vừa chạy trả về thành công.

Năng lực cần giữ sau bài là: Tính được dải địa chỉ của một mạng con và dự đoán đường đi của một gói trước khi kiểm chứng bằng lệnh. Nếu learner chỉ nhắc lại định nghĩa nhưng không phân biệt được hai state gần nhau trên số đo, bài chưa đạt.

## Cơ Chế Tác Động

Mô hình phân tầng dùng để định vị vấn đề chứ để học thuộc: khi có sự cố, câu hỏi đầu tiên là nó nằm ở tầng nào. Địa chỉ và khối địa chỉ: cách đọc ký hiệu tiền tố và tính được dải địa chỉ của một mạng con, kỹ năng dùng trực tiếp khi thiết kế mạng riêng ở M24. Bảng định tuyến và cổng ra: máy quyết định gửi gói đi đâu bằng cách so địa chỉ đích với bảng định tuyến, và đọc được bảng đó là trả lời được câu gói này đi đường nào. Phân giải địa chỉ vật lý trong mạng cục bộ ở mức nhận biết. Đơn vị truyền tối đa và phân mảnh: gói vượt kích thước tối đa bị chia hoặc bị loại, và triệu chứng của nó rất dễ nhầm với lỗi ứng dụng vì kết nối thành công nhưng truyền dữ liệu lớn thì treo. Chuyển đổi địa chỉ và tường lửa: hai thứ đứng giữa và làm thay đổi những gì bên kia nhìn thấy.

Tách ba lớp khi đọc cơ chế `wiki.de-foundation.layers-addresses-and-routing`: declared state là điều cấu hình hoặc API yêu cầu; executed state là việc runtime thực sự làm; consumer-visible state là điều client hay operator quan sát. Ba lớp có thể lệch nhau vì cache, buffering, retry, scheduling, queue hoặc failure giữa hai transition. Evidence phải chỉ ra lớp nào đang được đo.

## Bản Đồ Quyết Định

| Bước | Câu hỏi phải khóa | Điều kiện đạt |
|---|---|---|
| Layer | Xác định hop và protocol state | Không gọi mọi lỗi là network |
| Budget | Chia deadline và capacity theo hop | Không reset budget sau retry |
| Identity | Khóa connection, request và operation identity | Không gộp duplicate với retry |
| Evidence | Ghép client, DNS, transport, TLS, HTTP và server timeline | Clock và correlation được công bố |

Quy tắc mặc định là chọn phép giải thích đơn giản nhất qua được hard constraints, rồi viết trước reversal trigger. Với `Layers, addresses and routing`, absence of error không phải pass; pass cần observation đúng grain, một oracle độc lập và changed-constraint case đủ làm model có cơ hội thất bại.

## Case Study Thực Chiến: Layers, addresses and routing

Cho năm khối địa chỉ, tính dải địa chỉ dùng được và địa chỉ quảng bá cho từng cái. Đọc bảng định tuyến của máy mình. Với ba địa chỉ đích khác nhau, viết dự đoán gói đi qua cổng nào **trước khi** chạy lệnh tra đường, rồi đối chiếu.

Trong case `wiki.de-foundation.layers-addresses-and-routing`, learner ghi expected transition, input snapshot, version và giới hạn an toàn trước khi chạy. Sau execution, họ giữ raw counter, timestamp, exit status, state trước–sau và giải thích delta bằng mechanism ở trên. Đánh giá không cho phép sửa expected result sau khi nhìn output mà không ghi change record.

Biến thể khó hơn đổi một constraint có khả năng đảo kết luận: workload shape, memory pressure, connection reuse, retry budget, permission hoặc dependency direction. Tầng *áp dụng*. Bài mở module, kỹ năng tính toán cụ thể chuẩn bị cho M24. Kiểm bằng bài tính cộng dự đoán; đạt khi tính đúng ít nhất bốn trong năm mạng con và dự đoán đúng đường đi ở cả ba trường hợp.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Học thuộc bảy tầng mà không dùng để định vị. **Thực tế:** tín hiệu chỉ chứng minh điều nó đo trong đúng scope; state ở layer khác vẫn có thể trái ngược. **Vì sao nghe hợp lý:** happy path nhỏ thường không chạm queue, cache, partial progress hoặc restart.

**Hiểu lầm:** tính nhầm số địa chỉ dùng được. **Thực tế:** tool và API cung cấp primitive, không tự cấp ownership, deadline, idempotency hay recovery policy. **Vì sao nghe hợp lý:** syntax gọn che mất protocol và lifecycle phía dưới.

Với `wiki.de-foundation.layers-addresses-and-routing`, một edge case đáng giữ là observation đúng nhưng diagnosis sai: counter tăng thật, song nguyên nhân điều khiển nằm ở layer trước. Muốn tránh, timeline phải nối trigger tới consumer harm và ghi rõ negative control nào đã loại giả thuyết cạnh tranh.

## Nếu Bạn Dạy Lại Điều Này...

Mở bài bằng một dự đoán dễ sai về `Layers, addresses and routing`, không mở bằng định nghĩa. Cho hai trace gần giống nhau nhưng khác đúng một state boundary; learner phải chọn probe tiếp theo trước khi được xem đáp án.

Bài tập seed dùng chính lab của DE-L077, sau đó đổi constraint đủ mạnh để buộc giữ hoặc đảo quyết định. Người dạy chấm reasoning chain và evidence, không chấm việc learner đoán đúng tên công cụ.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `Layers, addresses and routing` dùng điều kiện hoàn thành sau: Tính đúng ≥ 4/5 mạng con, và dự đoán đường đi khớp kết quả lệnh tra ở cả ba trường hợp. Mỗi probe phải có prediction, failure signal và independent oracle.

### Probe 1: state transition và invariant

**Mệnh đề P1 cần kiểm.** Mô hình phân tầng dùng để định vị vấn đề chứ để học thuộc: khi có sự cố, câu hỏi đầu tiên là nó nằm ở tầng nào.

**Thiết kế phép thử.** Với `wiki.de-foundation.layers-addresses-and-routing`, tạo positive và negative control chỉ khác một điều kiện; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P1 cần giữ.** Với `wiki.de-foundation.layers-addresses-and-routing`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề P2 cần kiểm.** Tính được dải địa chỉ của một mạng con và dự đoán đường đi của một gói trước khi kiểm chứng bằng lệnh.

**Thiết kế phép thử.** Với `wiki.de-foundation.layers-addresses-and-routing`, tạo boundary case ngay trước và sau ngưỡng; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P2 cần giữ.** Với `wiki.de-foundation.layers-addresses-and-routing`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề P3 cần kiểm.** Tầng *áp dụng*.

**Thiết kế phép thử.** Với `wiki.de-foundation.layers-addresses-and-routing`, tạo replay cùng identity nhưng đổi state; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P3 cần giữ.** Với `wiki.de-foundation.layers-addresses-and-routing`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề P4 cần kiểm.** Cho năm khối địa chỉ, tính dải địa chỉ dùng được và địa chỉ quảng bá cho từng cái.

**Thiết kế phép thử.** Với `wiki.de-foundation.layers-addresses-and-routing`, tạo failure inject trước và sau transition bền vững; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P4 cần giữ.** Với `wiki.de-foundation.layers-addresses-and-routing`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề P5 cần kiểm.** Học thuộc bảy tầng mà không dùng để định vị · tính nhầm số địa chỉ dùng được · bỏ qua đơn vị truyền tối đa nên không giải thích được lỗi treo khi truyền dữ liệu lớn.

**Thiết kế phép thử.** Với `wiki.de-foundation.layers-addresses-and-routing`, tạo changed scale làm cost model đổi; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P5 cần giữ.** Với `wiki.de-foundation.layers-addresses-and-routing`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề P6 cần kiểm.** Tính đúng ≥ 4/5 mạng con, và dự đoán đường đi khớp kết quả lệnh tra ở cả ba trường hợp.

**Thiết kế phép thử.** Với `wiki.de-foundation.layers-addresses-and-routing`, tạo adversarial order, skew hoặc packet timing; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P6 cần giữ.** Với `wiki.de-foundation.layers-addresses-and-routing`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề P7 cần kiểm.** Mô hình phân tầng dùng để định vị vấn đề chứ để học thuộc: khi có sự cố, câu hỏi đầu tiên là nó nằm ở tầng nào.

**Thiết kế phép thử.** Với `wiki.de-foundation.layers-addresses-and-routing`, tạo fresh environment không cache; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P7 cần giữ.** Với `wiki.de-foundation.layers-addresses-and-routing`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề P8 cần kiểm.** Tính được dải địa chỉ của một mạng con và dự đoán đường đi của một gói trước khi kiểm chứng bằng lệnh.

**Thiết kế phép thử.** Với `wiki.de-foundation.layers-addresses-and-routing`, tạo independent oracle không dùng chung implementation; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P8 cần giữ.** Với `wiki.de-foundation.layers-addresses-and-routing`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề P9 cần kiểm.** Tầng *áp dụng*.

**Thiết kế phép thử.** Với `wiki.de-foundation.layers-addresses-and-routing`, tạo partial progress rồi restart; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P9 cần giữ.** Với `wiki.de-foundation.layers-addresses-and-routing`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề P10 cần kiểm.** Cho năm khối địa chỉ, tính dải địa chỉ dùng được và địa chỉ quảng bá cho từng cái.

**Thiết kế phép thử.** Với `wiki.de-foundation.layers-addresses-and-routing`, tạo missing evidence phải abstain; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P10 cần giữ.** Với `wiki.de-foundation.layers-addresses-and-routing`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề P11 cần kiểm.** Học thuộc bảy tầng mà không dùng để định vị · tính nhầm số địa chỉ dùng được · bỏ qua đơn vị truyền tối đa nên không giải thích được lỗi treo khi truyền dữ liệu lớn.

**Thiết kế phép thử.** Với `wiki.de-foundation.layers-addresses-and-routing`, tạo reviewer tái hiện từ evidence package; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P11 cần giữ.** Với `wiki.de-foundation.layers-addresses-and-routing`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề P12 cần kiểm.** Tính đúng ≥ 4/5 mạng con, và dự đoán đường đi khớp kết quả lệnh tra ở cả ba trường hợp.

**Thiết kế phép thử.** Với `wiki.de-foundation.layers-addresses-and-routing`, tạo constraint đổi đủ để quyết định đảo; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P12 cần giữ.** Với `wiki.de-foundation.layers-addresses-and-routing`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên khiến mô hình `Layers, addresses and routing` không còn đúng là gì?

<details><summary>Đáp án</summary>Học thuộc bảy tầng mà không dùng để định vị · tính nhầm số địa chỉ dùng được · bỏ qua đơn vị truyền tối đa nên không giải thích được lỗi treo khi truyền dữ liệu lớn.</details>

2. Evidence nào phân biệt được hai state dễ nhầm?

<details><summary>Đáp án</summary>Tầng *áp dụng*. Bài mở module, kỹ năng tính toán cụ thể chuẩn bị cho M24. Kiểm bằng bài tính cộng dự đoán; đạt khi tính đúng ít nhất bốn trong năm mạng con và dự đoán đúng đường đi ở cả ba trường hợp.</details>

3. Khi constraint đổi, điều gì quyết định giữ hay đảo lựa chọn?

<details><summary>Đáp án</summary>Tính đúng ≥ 4/5 mạng con, và dự đoán đường đi khớp kết quả lệnh tra ở cả ba trường hợp.</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `Layers, addresses and routing` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Hành vi phụ thuộc kernel, distribution, library, network path hoặc hardware phải được kiểm lại trên target đã ghi version.
- Concept key `ck.de.layers-addresses-and-routing` đang ở trạng thái `proposed`; note chưa được tính là canonical registry coverage.
- Một trace đơn lẻ không chứng minh capacity, reliability hoặc security cho population khác.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-KUROSE-ROSS-NETWORKING-8E]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-KUROSE-ROSS-NETWORKING-8E]] — `src.book.kurose-ross-networking.8e` | §§1.4, 2.2, 2.4, 2.7, 3.5–3.7, 4.5, 6.6.1 và Chapter 8; PDF 67–682 | mechanism và boundary liên quan trực tiếp tới `Layers, addresses and routing` | cơ chế, quyết định, case và probe | Đã phủ | phần ngoài objective DE-L077 |

## Key takeaways
- Tính được dải địa chỉ của một mạng con và dự đoán đường đi của một gói trước khi kiểm chứng bằng lệnh.
- Tính đúng ≥ 4/5 mạng con, và dự đoán đường đi khớp kết quả lệnh tra ở cả ba trường hợp.
- `Layers, addresses and routing` chỉ có nghĩa trong scope, state, identity và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.
