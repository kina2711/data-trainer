# Phase 2: Machine, Operating System and Network
# Module 4: Computer Architecture and the Performance Model
# Lesson 57: Linking the model to databases

## Mục tiêu bài học

**Năng lực cần chứng minh.** Giải thích bằng mô hình chi phí vì sao một truy vấn cụ thể chọn quét toàn bảng thay vì dùng chỉ mục.

**Điều kiện hoàn thành.** Giải thích đúng ≥ 3/4 tình huống bằng ước lượng số lần đọc, và tính đúng chiều cao cây chỉ mục.

**Kiến thức và cơ chế.** Bài nối, và nó biến mọi thứ đã đo thành công cụ đọc hành vi cơ sở dữ liệu ở M9 và M10. Bốn liên hệ bắt buộc. Trang và hồ đệm: cơ sở dữ liệu đọc ghi theo trang chứ theo dòng, và hồ đệm chính là bộ đệm trang của riêng nó, nên tỉ lệ trúng hồ đệm là chỉ số hiệu năng hàng đầu. Tra chỉ mục so với quét toàn bảng: tra chỉ mục là đọc ngẫu nhiên còn quét là đọc tuần tự, nên **khi số dòng cần lấy đủ lớn thì quét thắng dù chỉ mục tồn tại**, và đây là lý do bộ tối ưu đôi khi cố ý bỏ qua chỉ mục. Độ rẽ nhánh của cây B và chi phí đọc khối, nối lại lesson 36. Nhật ký ghi trước và `fsync`: mọi cam kết bền vững của giao dịch quy về một lần đẩy xuống đĩa, theo lesson 53. Ba câu hỏi để đọc một kế hoạch thực thi chậm trước khi biết cú pháp của công cụ nào.


# Linking the model to databases

**Tóm tắt bản chất:** Giải thích bằng mô hình chi phí vì sao một truy vấn cụ thể chọn quét toàn bảng thay vì dùng chỉ mục. Cơ chế chỉ có giá trị khi workload, version, state owner và failure boundary đã được khóa; một con số đẹp ngoài bốn điều kiện đó không đủ để ra quyết định.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, đo và ra quyết định đúng về Linking the model to databases?

## Nỗi Đau & Động Lực

Cho rằng có chỉ mục thì luôn nên dùng chỉ mục · bỏ qua tỉ lệ dòng lấy ra · quên rằng tra chỉ mục còn phải đọc thêm dòng dữ liệu · học quy tắc thay vì tính chi phí. Đây không phải danh sách lỗi cú pháp. Mỗi lỗi làm người vận hành chọn nhầm owner hoặc chữa symptom ở layer sau, khiến thời gian phục hồi tăng dù command vừa chạy trả về thành công.

Năng lực cần giữ sau bài là: Giải thích bằng mô hình chi phí vì sao một truy vấn cụ thể chọn quét toàn bảng thay vì dùng chỉ mục. Nếu learner chỉ nhắc lại định nghĩa nhưng không phân biệt được hai state gần nhau trên số đo, bài chưa đạt.

## Cơ Chế Tác Động

Bài nối, và nó biến mọi thứ đã đo thành công cụ đọc hành vi cơ sở dữ liệu ở M9 và M10. Bốn liên hệ bắt buộc. Trang và hồ đệm: cơ sở dữ liệu đọc ghi theo trang chứ theo dòng, và hồ đệm chính là bộ đệm trang của riêng nó, nên tỉ lệ trúng hồ đệm là chỉ số hiệu năng hàng đầu. Tra chỉ mục so với quét toàn bảng: tra chỉ mục là đọc ngẫu nhiên còn quét là đọc tuần tự, nên **khi số dòng cần lấy đủ lớn thì quét thắng dù chỉ mục tồn tại**, và đây là lý do bộ tối ưu đôi khi cố ý bỏ qua chỉ mục. Độ rẽ nhánh của cây B và chi phí đọc khối, nối lại lesson 36. Nhật ký ghi trước và `fsync`: mọi cam kết bền vững của giao dịch quy về một lần đẩy xuống đĩa, theo lesson 53. Ba câu hỏi để đọc một kế hoạch thực thi chậm trước khi biết cú pháp của công cụ nào.

Tách ba lớp khi đọc cơ chế `wiki.de-foundation.linking-the-model-to-databases`: declared state là điều cấu hình hoặc API yêu cầu; executed state là việc runtime thực sự làm; consumer-visible state là điều client hay operator quan sát. Ba lớp có thể lệch nhau vì cache, buffering, retry, scheduling, queue hoặc failure giữa hai transition. Evidence phải chỉ ra lớp nào đang được đo.

## Bản Đồ Quyết Định

| Bước | Câu hỏi phải khóa | Điều kiện đạt |
|---|---|---|
| Model | Giải thích chi phí bằng hierarchy, parallel fraction hoặc data movement | Model dự đoán đúng khi đổi scale |
| Measure | Dùng counter và benchmark khóa workload | Observation khớp oracle và có raw sample |
| Explain | Nối delta với mechanism | Reviewer tái hiện được reasoning |
| Reverse | Đổi workload, layout hoặc resource | Quyết định đổi khi bottleneck đổi |

Quy tắc mặc định là chọn phép giải thích đơn giản nhất qua được hard constraints, rồi viết trước reversal trigger. Với `Linking the model to databases`, absence of error không phải pass; pass cần observation đúng grain, một oracle độc lập và changed-constraint case đủ làm model có cơ hội thất bại.

## Case Study Thực Chiến: Linking the model to databases

Cho bốn tình huống truy vấn với tỉ lệ dòng lấy ra khác nhau, từ 0,01% tới 40% bảng. Với mỗi tình huống, ước lượng số lần đọc ngẫu nhiên nếu dùng chỉ mục và số lần đọc tuần tự nếu quét, rồi dự đoán bộ tối ưu chọn cách nào. Ước lượng độ rẽ nhánh và chiều cao cây chỉ mục cho một bảng một triệu dòng.

Trong case `wiki.de-foundation.linking-the-model-to-databases`, learner ghi expected transition, input snapshot, version và giới hạn an toàn trước khi chạy. Sau execution, họ giữ raw counter, timestamp, exit status, state trước–sau và giải thích delta bằng mechanism ở trên. Đánh giá không cho phép sửa expected result sau khi nhìn output mà không ghi change record.

Biến thể khó hơn đổi một constraint có khả năng đảo kết luận: workload shape, memory pressure, connection reuse, retry budget, permission hoặc dependency direction. Tầng *hiểu*. Bài nối, chuẩn bị trực tiếp cho M9 và M10; chưa đòi vận hành cơ sở dữ liệu. Kiểm bằng bài lập luận trên bốn tình huống; đạt khi giải thích đúng ít nhất ba bằng chi phí đọc chứ bằng quy tắc thuộc lòng.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Cho rằng có chỉ mục thì luôn nên dùng chỉ mục. **Thực tế:** tín hiệu chỉ chứng minh điều nó đo trong đúng scope; state ở layer khác vẫn có thể trái ngược. **Vì sao nghe hợp lý:** happy path nhỏ thường không chạm queue, cache, partial progress hoặc restart.

**Hiểu lầm:** bỏ qua tỉ lệ dòng lấy ra. **Thực tế:** tool và API cung cấp primitive, không tự cấp ownership, deadline, idempotency hay recovery policy. **Vì sao nghe hợp lý:** syntax gọn che mất protocol và lifecycle phía dưới.

Với `wiki.de-foundation.linking-the-model-to-databases`, một edge case đáng giữ là observation đúng nhưng diagnosis sai: counter tăng thật, song nguyên nhân điều khiển nằm ở layer trước. Muốn tránh, timeline phải nối trigger tới consumer harm và ghi rõ negative control nào đã loại giả thuyết cạnh tranh.

## Nếu Bạn Dạy Lại Điều Này...

Mở bài bằng một dự đoán dễ sai về `Linking the model to databases`, không mở bằng định nghĩa. Cho hai trace gần giống nhau nhưng khác đúng một state boundary; learner phải chọn probe tiếp theo trước khi được xem đáp án.

Bài tập seed dùng chính lab của DE-L057, sau đó đổi constraint đủ mạnh để buộc giữ hoặc đảo quyết định. Người dạy chấm reasoning chain và evidence, không chấm việc learner đoán đúng tên công cụ.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `Linking the model to databases` dùng điều kiện hoàn thành sau: Giải thích đúng ≥ 3/4 tình huống bằng ước lượng số lần đọc, và tính đúng chiều cao cây chỉ mục. Mỗi probe phải có prediction, failure signal và independent oracle.

### Probe 1: state transition và invariant

**Mệnh đề P1 cần kiểm.** Bài nối, và nó biến mọi thứ đã đo thành công cụ đọc hành vi cơ sở dữ liệu ở M9 và M10.

**Thiết kế phép thử.** Với `wiki.de-foundation.linking-the-model-to-databases`, tạo positive và negative control chỉ khác một điều kiện; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P1 cần giữ.** Với `wiki.de-foundation.linking-the-model-to-databases`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề P2 cần kiểm.** Giải thích bằng mô hình chi phí vì sao một truy vấn cụ thể chọn quét toàn bảng thay vì dùng chỉ mục.

**Thiết kế phép thử.** Với `wiki.de-foundation.linking-the-model-to-databases`, tạo boundary case ngay trước và sau ngưỡng; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P2 cần giữ.** Với `wiki.de-foundation.linking-the-model-to-databases`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề P3 cần kiểm.** Tầng *hiểu*.

**Thiết kế phép thử.** Với `wiki.de-foundation.linking-the-model-to-databases`, tạo replay cùng identity nhưng đổi state; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P3 cần giữ.** Với `wiki.de-foundation.linking-the-model-to-databases`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề P4 cần kiểm.** Cho bốn tình huống truy vấn với tỉ lệ dòng lấy ra khác nhau, từ 0,01% tới 40% bảng.

**Thiết kế phép thử.** Với `wiki.de-foundation.linking-the-model-to-databases`, tạo failure inject trước và sau transition bền vững; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P4 cần giữ.** Với `wiki.de-foundation.linking-the-model-to-databases`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề P5 cần kiểm.** Cho rằng có chỉ mục thì luôn nên dùng chỉ mục · bỏ qua tỉ lệ dòng lấy ra · quên rằng tra chỉ mục còn phải đọc thêm dòng dữ liệu · học quy tắc thay vì tính chi phí.

**Thiết kế phép thử.** Với `wiki.de-foundation.linking-the-model-to-databases`, tạo changed scale làm cost model đổi; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P5 cần giữ.** Với `wiki.de-foundation.linking-the-model-to-databases`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề P6 cần kiểm.** Giải thích đúng ≥ 3/4 tình huống bằng ước lượng số lần đọc, và tính đúng chiều cao cây chỉ mục.

**Thiết kế phép thử.** Với `wiki.de-foundation.linking-the-model-to-databases`, tạo adversarial order, skew hoặc packet timing; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P6 cần giữ.** Với `wiki.de-foundation.linking-the-model-to-databases`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề P7 cần kiểm.** Bài nối, và nó biến mọi thứ đã đo thành công cụ đọc hành vi cơ sở dữ liệu ở M9 và M10.

**Thiết kế phép thử.** Với `wiki.de-foundation.linking-the-model-to-databases`, tạo fresh environment không cache; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P7 cần giữ.** Với `wiki.de-foundation.linking-the-model-to-databases`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề P8 cần kiểm.** Giải thích bằng mô hình chi phí vì sao một truy vấn cụ thể chọn quét toàn bảng thay vì dùng chỉ mục.

**Thiết kế phép thử.** Với `wiki.de-foundation.linking-the-model-to-databases`, tạo independent oracle không dùng chung implementation; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P8 cần giữ.** Với `wiki.de-foundation.linking-the-model-to-databases`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề P9 cần kiểm.** Tầng *hiểu*.

**Thiết kế phép thử.** Với `wiki.de-foundation.linking-the-model-to-databases`, tạo partial progress rồi restart; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P9 cần giữ.** Với `wiki.de-foundation.linking-the-model-to-databases`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề P10 cần kiểm.** Cho bốn tình huống truy vấn với tỉ lệ dòng lấy ra khác nhau, từ 0,01% tới 40% bảng.

**Thiết kế phép thử.** Với `wiki.de-foundation.linking-the-model-to-databases`, tạo missing evidence phải abstain; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P10 cần giữ.** Với `wiki.de-foundation.linking-the-model-to-databases`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề P11 cần kiểm.** Cho rằng có chỉ mục thì luôn nên dùng chỉ mục · bỏ qua tỉ lệ dòng lấy ra · quên rằng tra chỉ mục còn phải đọc thêm dòng dữ liệu · học quy tắc thay vì tính chi phí.

**Thiết kế phép thử.** Với `wiki.de-foundation.linking-the-model-to-databases`, tạo reviewer tái hiện từ evidence package; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P11 cần giữ.** Với `wiki.de-foundation.linking-the-model-to-databases`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề P12 cần kiểm.** Giải thích đúng ≥ 3/4 tình huống bằng ước lượng số lần đọc, và tính đúng chiều cao cây chỉ mục.

**Thiết kế phép thử.** Với `wiki.de-foundation.linking-the-model-to-databases`, tạo constraint đổi đủ để quyết định đảo; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P12 cần giữ.** Với `wiki.de-foundation.linking-the-model-to-databases`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên khiến mô hình `Linking the model to databases` không còn đúng là gì?

<details><summary>Đáp án</summary>Cho rằng có chỉ mục thì luôn nên dùng chỉ mục · bỏ qua tỉ lệ dòng lấy ra · quên rằng tra chỉ mục còn phải đọc thêm dòng dữ liệu · học quy tắc thay vì tính chi phí.</details>

2. Evidence nào phân biệt được hai state dễ nhầm?

<details><summary>Đáp án</summary>Tầng *hiểu*. Bài nối, chuẩn bị trực tiếp cho M9 và M10; chưa đòi vận hành cơ sở dữ liệu. Kiểm bằng bài lập luận trên bốn tình huống; đạt khi giải thích đúng ít nhất ba bằng chi phí đọc chứ bằng quy tắc thuộc lòng.</details>

3. Khi constraint đổi, điều gì quyết định giữ hay đảo lựa chọn?

<details><summary>Đáp án</summary>Giải thích đúng ≥ 3/4 tình huống bằng ước lượng số lần đọc, và tính đúng chiều cao cây chỉ mục.</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `Linking the model to databases` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Hành vi phụ thuộc kernel, distribution, library, network path hoặc hardware phải được kiểm lại trên target đã ghi version.
- Concept key `ck.de.linking-the-model-to-databases` đang ở trạng thái `proposed`; note chưa được tính là canonical registry coverage.
- Một trace đơn lẻ không chứng minh capacity, reliability hoặc security cho population khác.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-PATTERSON-HENNESSY-COD-5E]]
2. [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]]
3. [[SRC-PETROV-DATABASE-INTERNALS-1E]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-PATTERSON-HENNESSY-COD-5E]] — `src.book.patterson-hennessy-cod.5e` | Chapter 5 và §6.3; PDF 397–538 | mechanism và boundary liên quan trực tiếp tới `Linking the model to databases` | cơ chế, quyết định, case và probe | Đã phủ | phần ngoài objective DE-L057 |
| [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]] — `src.book.silberschatz-database-system-concepts.7e` | Chapters 15–18 theo source record | mechanism và boundary liên quan trực tiếp tới `Linking the model to databases` | cơ chế, quyết định, case và probe | Đã phủ | phần ngoài objective DE-L057 |
| [[SRC-PETROV-DATABASE-INTERNALS-1E]] — `src.book.petrov-database-internals.1e` | Chapters 3–7 theo source record | mechanism và boundary liên quan trực tiếp tới `Linking the model to databases` | cơ chế, quyết định, case và probe | Đã phủ | phần ngoài objective DE-L057 |

## Key takeaways
- Giải thích bằng mô hình chi phí vì sao một truy vấn cụ thể chọn quét toàn bảng thay vì dùng chỉ mục.
- Giải thích đúng ≥ 3/4 tình huống bằng ước lượng số lần đọc, và tính đúng chiều cao cây chỉ mục.
- `Linking the model to databases` chỉ có nghĩa trong scope, state, identity và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.
