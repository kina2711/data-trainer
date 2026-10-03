# Phase 3: Software and Backend Engineering
# Module 7: Software Design and Delivery
# Lesson 89: From use case to contract and domain vocabulary

## Mục tiêu bài học

**Năng lực cần chứng minh.** Viết hợp đồng bốn phần cho các điểm vào của một mô đun, với từ vựng khớp từ vựng nghiệp vụ.

**Điều kiện hoàn thành.** Năm điểm vào đều có đủ bốn phần, và người đóng vai nghiệp vụ không tìm được khái niệm nào mang hai tên.

**Kiến thức và cơ chế.** Bài nối lesson 1 với thiết kế mã: sau khi có phát biểu bài toán thì bước tiếp là đặt tên cho các khái niệm và cố định hợp đồng. Từ vựng miền: dùng đúng từ mà người nghiệp vụ dùng, một khái niệm một tên, và không dịch qua lại giữa hai bộ từ vựng trong cùng một kho mã; mỗi lần dịch là một chỗ có thể sai. Ca sử dụng và tiêu chí chấp nhận theo lesson 1, nay gắn với một tên hàm hoặc một điểm vào cụ thể. Hợp đồng gồm bốn phần: kiểu dữ liệu vào ra, điều kiện trước, điều kiện sau, và hợp đồng lỗi tức hàm này có thể thất bại theo những cách nào. Phần cuối hay bị bỏ và là phần gây nhiều sự cố nhất, vì người gọi không biết phải xử lý gì. Hợp đồng dữ liệu ở đây là hợp đồng trong mã; hợp đồng giữa hai đội ở tầng cao hơn sẽ học ở M18 và M19.


# From use case to contract and domain vocabulary

**Tóm tắt bản chất:** Viết hợp đồng bốn phần cho các điểm vào của một mô đun, với từ vựng khớp từ vựng nghiệp vụ. Cơ chế chỉ có giá trị khi workload, version, state owner và failure boundary đã được khóa; một con số đẹp ngoài bốn điều kiện đó không đủ để ra quyết định.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, đo và ra quyết định đúng về From use case to contract and domain vocabulary?

## Nỗi Đau & Động Lực

Bỏ hợp đồng lỗi · đặt tên kỹ thuật cho khái niệm nghiệp vụ · một khái niệm mang hai tên ở hai chỗ · viết điều kiện trước mà không kiểm ở đâu cả. Đây không phải danh sách lỗi cú pháp. Mỗi lỗi làm người vận hành chọn nhầm owner hoặc chữa symptom ở layer sau, khiến thời gian phục hồi tăng dù command vừa chạy trả về thành công.

Năng lực cần giữ sau bài là: Viết hợp đồng bốn phần cho các điểm vào của một mô đun, với từ vựng khớp từ vựng nghiệp vụ. Nếu learner chỉ nhắc lại định nghĩa nhưng không phân biệt được hai state gần nhau trên số đo, bài chưa đạt.

## Cơ Chế Tác Động

Bài nối lesson 1 với thiết kế mã: sau khi có phát biểu bài toán thì bước tiếp là đặt tên cho các khái niệm và cố định hợp đồng. Từ vựng miền: dùng đúng từ mà người nghiệp vụ dùng, một khái niệm một tên, và không dịch qua lại giữa hai bộ từ vựng trong cùng một kho mã; mỗi lần dịch là một chỗ có thể sai. Ca sử dụng và tiêu chí chấp nhận theo lesson 1, nay gắn với một tên hàm hoặc một điểm vào cụ thể. Hợp đồng gồm bốn phần: kiểu dữ liệu vào ra, điều kiện trước, điều kiện sau, và hợp đồng lỗi tức hàm này có thể thất bại theo những cách nào. Phần cuối hay bị bỏ và là phần gây nhiều sự cố nhất, vì người gọi không biết phải xử lý gì. Hợp đồng dữ liệu ở đây là hợp đồng trong mã; hợp đồng giữa hai đội ở tầng cao hơn sẽ học ở M18 và M19.

Tách ba lớp khi đọc cơ chế `wiki.de-foundation.from-use-case-to-contract-and-domain-vocabulary`: declared state là điều cấu hình hoặc API yêu cầu; executed state là việc runtime thực sự làm; consumer-visible state là điều client hay operator quan sát. Ba lớp có thể lệch nhau vì cache, buffering, retry, scheduling, queue hoặc failure giữa hai transition. Evidence phải chỉ ra lớp nào đang được đo.

## Bản Đồ Quyết Định

| Bước | Câu hỏi phải khóa | Điều kiện đạt |
|---|---|---|
| Vocabulary | Một concept miền có một tên trong scope | Business reviewer hiểu cùng nghĩa |
| Contract | Input, output, pre/postcondition và error | Caller biết mọi outcome |
| Boundary | Policy phụ thuộc vào port, mechanism cài adapter | Đổi adapter không đổi policy |
| Review | Changed-use-case test | Quyết định giữ hoặc đảo có bằng chứng |

Quy tắc mặc định là chọn phép giải thích đơn giản nhất qua được hard constraints, rồi viết trước reversal trigger. Với `From use case to contract and domain vocabulary`, absence of error không phải pass; pass cần observation đúng grain, một oracle độc lập và changed-constraint case đủ làm model có cơ hội thất bại.

## Case Study Thực Chiến: From use case to contract and domain vocabulary

Cho mô tả nghiệp vụ một hệ đặt hàng. Rút từ vựng miền thành danh sách thuật ngữ có định nghĩa. Viết hợp đồng bốn phần cho năm điểm vào chính. Đổi bài: một học viên đóng vai người nghiệp vụ đọc và chỉ ra chỗ nào tên trong mã không khớp tên họ dùng.

Trong case `wiki.de-foundation.from-use-case-to-contract-and-domain-vocabulary`, learner ghi expected transition, input snapshot, version và giới hạn an toàn trước khi chạy. Sau execution, họ giữ raw counter, timestamp, exit status, state trước–sau và giải thích delta bằng mechanism ở trên. Đánh giá không cho phép sửa expected result sau khi nhìn output mà không ghi change record.

Biến thể khó hơn đổi một constraint có khả năng đảo kết luận: workload shape, memory pressure, connection reuse, retry budget, permission hoặc dependency direction. Tầng *áp dụng*. Bài mở module, nối kỹ năng phát biểu bài toán ở M1 với cấu trúc mã. Kiểm bằng rà soát chéo với người đóng vai nghiệp vụ; đạt khi mọi điểm vào có đủ bốn phần và không có khái niệm nào mang hai tên.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Bỏ hợp đồng lỗi. **Thực tế:** tín hiệu chỉ chứng minh điều nó đo trong đúng scope; state ở layer khác vẫn có thể trái ngược. **Vì sao nghe hợp lý:** happy path nhỏ thường không chạm queue, cache, partial progress hoặc restart.

**Hiểu lầm:** đặt tên kỹ thuật cho khái niệm nghiệp vụ. **Thực tế:** tool và API cung cấp primitive, không tự cấp ownership, deadline, idempotency hay recovery policy. **Vì sao nghe hợp lý:** syntax gọn che mất protocol và lifecycle phía dưới.

Với `wiki.de-foundation.from-use-case-to-contract-and-domain-vocabulary`, một edge case đáng giữ là observation đúng nhưng diagnosis sai: counter tăng thật, song nguyên nhân điều khiển nằm ở layer trước. Muốn tránh, timeline phải nối trigger tới consumer harm và ghi rõ negative control nào đã loại giả thuyết cạnh tranh.

## Nếu Bạn Dạy Lại Điều Này...

Mở bài bằng một dự đoán dễ sai về `From use case to contract and domain vocabulary`, không mở bằng định nghĩa. Cho hai trace gần giống nhau nhưng khác đúng một state boundary; learner phải chọn probe tiếp theo trước khi được xem đáp án.

Bài tập seed dùng chính lab của DE-L089, sau đó đổi constraint đủ mạnh để buộc giữ hoặc đảo quyết định. Người dạy chấm reasoning chain và evidence, không chấm việc learner đoán đúng tên công cụ.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `From use case to contract and domain vocabulary` dùng điều kiện hoàn thành sau: Năm điểm vào đều có đủ bốn phần, và người đóng vai nghiệp vụ không tìm được khái niệm nào mang hai tên. Mỗi probe phải có prediction, failure signal và independent oracle.

### Probe 1: state transition và invariant

**Mệnh đề P1 cần kiểm.** Bài nối lesson 1 với thiết kế mã: sau khi có phát biểu bài toán thì bước tiếp là đặt tên cho các khái niệm và cố định hợp đồng.

**Thiết kế phép thử.** Với `wiki.de-foundation.from-use-case-to-contract-and-domain-vocabulary`, tạo positive và negative control chỉ khác một điều kiện; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P1 cần giữ.** Với `wiki.de-foundation.from-use-case-to-contract-and-domain-vocabulary`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề P2 cần kiểm.** Viết hợp đồng bốn phần cho các điểm vào của một mô đun, với từ vựng khớp từ vựng nghiệp vụ.

**Thiết kế phép thử.** Với `wiki.de-foundation.from-use-case-to-contract-and-domain-vocabulary`, tạo boundary case ngay trước và sau ngưỡng; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P2 cần giữ.** Với `wiki.de-foundation.from-use-case-to-contract-and-domain-vocabulary`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề P3 cần kiểm.** Tầng *áp dụng*.

**Thiết kế phép thử.** Với `wiki.de-foundation.from-use-case-to-contract-and-domain-vocabulary`, tạo replay cùng identity nhưng đổi state; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P3 cần giữ.** Với `wiki.de-foundation.from-use-case-to-contract-and-domain-vocabulary`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề P4 cần kiểm.** Cho mô tả nghiệp vụ một hệ đặt hàng.

**Thiết kế phép thử.** Với `wiki.de-foundation.from-use-case-to-contract-and-domain-vocabulary`, tạo failure inject trước và sau transition bền vững; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P4 cần giữ.** Với `wiki.de-foundation.from-use-case-to-contract-and-domain-vocabulary`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề P5 cần kiểm.** Bỏ hợp đồng lỗi · đặt tên kỹ thuật cho khái niệm nghiệp vụ · một khái niệm mang hai tên ở hai chỗ · viết điều kiện trước mà không kiểm ở đâu cả.

**Thiết kế phép thử.** Với `wiki.de-foundation.from-use-case-to-contract-and-domain-vocabulary`, tạo changed scale làm cost model đổi; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P5 cần giữ.** Với `wiki.de-foundation.from-use-case-to-contract-and-domain-vocabulary`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề P6 cần kiểm.** Năm điểm vào đều có đủ bốn phần, và người đóng vai nghiệp vụ không tìm được khái niệm nào mang hai tên.

**Thiết kế phép thử.** Với `wiki.de-foundation.from-use-case-to-contract-and-domain-vocabulary`, tạo adversarial order, skew hoặc packet timing; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P6 cần giữ.** Với `wiki.de-foundation.from-use-case-to-contract-and-domain-vocabulary`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề P7 cần kiểm.** Bài nối lesson 1 với thiết kế mã: sau khi có phát biểu bài toán thì bước tiếp là đặt tên cho các khái niệm và cố định hợp đồng.

**Thiết kế phép thử.** Với `wiki.de-foundation.from-use-case-to-contract-and-domain-vocabulary`, tạo fresh environment không cache; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P7 cần giữ.** Với `wiki.de-foundation.from-use-case-to-contract-and-domain-vocabulary`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề P8 cần kiểm.** Viết hợp đồng bốn phần cho các điểm vào của một mô đun, với từ vựng khớp từ vựng nghiệp vụ.

**Thiết kế phép thử.** Với `wiki.de-foundation.from-use-case-to-contract-and-domain-vocabulary`, tạo independent oracle không dùng chung implementation; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P8 cần giữ.** Với `wiki.de-foundation.from-use-case-to-contract-and-domain-vocabulary`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề P9 cần kiểm.** Tầng *áp dụng*.

**Thiết kế phép thử.** Với `wiki.de-foundation.from-use-case-to-contract-and-domain-vocabulary`, tạo partial progress rồi restart; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P9 cần giữ.** Với `wiki.de-foundation.from-use-case-to-contract-and-domain-vocabulary`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề P10 cần kiểm.** Cho mô tả nghiệp vụ một hệ đặt hàng.

**Thiết kế phép thử.** Với `wiki.de-foundation.from-use-case-to-contract-and-domain-vocabulary`, tạo missing evidence phải abstain; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P10 cần giữ.** Với `wiki.de-foundation.from-use-case-to-contract-and-domain-vocabulary`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề P11 cần kiểm.** Bỏ hợp đồng lỗi · đặt tên kỹ thuật cho khái niệm nghiệp vụ · một khái niệm mang hai tên ở hai chỗ · viết điều kiện trước mà không kiểm ở đâu cả.

**Thiết kế phép thử.** Với `wiki.de-foundation.from-use-case-to-contract-and-domain-vocabulary`, tạo reviewer tái hiện từ evidence package; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P11 cần giữ.** Với `wiki.de-foundation.from-use-case-to-contract-and-domain-vocabulary`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề P12 cần kiểm.** Năm điểm vào đều có đủ bốn phần, và người đóng vai nghiệp vụ không tìm được khái niệm nào mang hai tên.

**Thiết kế phép thử.** Với `wiki.de-foundation.from-use-case-to-contract-and-domain-vocabulary`, tạo constraint đổi đủ để quyết định đảo; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P12 cần giữ.** Với `wiki.de-foundation.from-use-case-to-contract-and-domain-vocabulary`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên khiến mô hình `From use case to contract and domain vocabulary` không còn đúng là gì?

<details><summary>Đáp án</summary>Bỏ hợp đồng lỗi · đặt tên kỹ thuật cho khái niệm nghiệp vụ · một khái niệm mang hai tên ở hai chỗ · viết điều kiện trước mà không kiểm ở đâu cả.</details>

2. Evidence nào phân biệt được hai state dễ nhầm?

<details><summary>Đáp án</summary>Tầng *áp dụng*. Bài mở module, nối kỹ năng phát biểu bài toán ở M1 với cấu trúc mã. Kiểm bằng rà soát chéo với người đóng vai nghiệp vụ; đạt khi mọi điểm vào có đủ bốn phần và không có khái niệm nào mang hai tên.</details>

3. Khi constraint đổi, điều gì quyết định giữ hay đảo lựa chọn?

<details><summary>Đáp án</summary>Năm điểm vào đều có đủ bốn phần, và người đóng vai nghiệp vụ không tìm được khái niệm nào mang hai tên.</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `From use case to contract and domain vocabulary` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Hành vi phụ thuộc kernel, distribution, library, network path hoặc hardware phải được kiểm lại trên target đã ghi version.
- Concept key `ck.de.from-use-case-to-contract-and-domain-vocabulary` đang ở trạng thái `proposed`; note chưa được tính là canonical registry coverage.
- Một trace đơn lẻ không chứng minh capacity, reliability hoặc security cho population khác.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-SOMMERVILLE-SOFTWARE-ENGINEERING-10E]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-SOMMERVILLE-SOFTWARE-ENGINEERING-10E]] — `src.book.sommerville-software-engineering.10e` | Chapters 4, 6–8 và 25; PDF 103–756 | mechanism và boundary liên quan trực tiếp tới `From use case to contract and domain vocabulary` | cơ chế, quyết định, case và probe | Đã phủ | phần ngoài objective DE-L089 |

## Key takeaways
- Viết hợp đồng bốn phần cho các điểm vào của một mô đun, với từ vựng khớp từ vựng nghiệp vụ.
- Năm điểm vào đều có đủ bốn phần, và người đóng vai nghiệp vụ không tìm được khái niệm nào mang hai tên.
- `From use case to contract and domain vocabulary` chỉ có nghĩa trong scope, state, identity và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.
