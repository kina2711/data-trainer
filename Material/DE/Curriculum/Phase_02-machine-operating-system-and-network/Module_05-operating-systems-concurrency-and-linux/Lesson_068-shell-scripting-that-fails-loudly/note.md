# Phase 2: Machine, Operating System and Network
# Module 5: Operating Systems, Concurrency and Linux
# Lesson 68: Shell scripting that fails loudly

## Mục tiêu bài học

**Năng lực cần chứng minh.** Viết script vận hành dừng đúng lúc lỗi, dọn dẹp khi thoát, và trả mã thoát đúng trong mọi nhánh.

**Điều kiện hoàn thành.** Năm lỗi đều làm script dừng với mã thoát khác không, và thư mục tạm được dọn trong cả năm trường hợp.

**Kiến thức và cơ chế.** Shell là keo dán của mọi hệ vận hành, và script shell viết ẩu là nguồn sự cố âm thầm vì mặc định của shell là chạy tiếp khi có lỗi. Ba tuỳ chọn nghiêm ngặt và tác dụng từng cái: dừng khi một lệnh lỗi, coi biến chưa đặt là lỗi, và cho lỗi trong đường ống lan ra. Kèm theo là cảnh báo về các trường hợp tuỳ chọn dừng khi lỗi **không** kích hoạt, vì tin tưởng mù vào nó cũng nguy hiểm. Trích dẫn và khai triển: quên ngoặc kép quanh biến là nguồn lỗi số một khi tên tệp có dấu cách. Bẫy để dọn dẹp khi thoát, tương đương trình quản lý ngữ cảnh ở lesson 15. Mã thoát và cách kiểm tra từng bước theo lesson 67. Khi nào nên dừng viết shell và chuyển sang Python: ba dấu hiệu cụ thể, thường là khi cần cấu trúc dữ liệu, cần xử lý lỗi phân tầng, hoặc script vượt khoảng một trăm dòng.


# Shell scripting that fails loudly

**Tóm tắt bản chất:** Viết script vận hành dừng đúng lúc lỗi, dọn dẹp khi thoát, và trả mã thoát đúng trong mọi nhánh. Cơ chế chỉ có giá trị khi workload, version, state owner và failure boundary đã được khóa; một con số đẹp ngoài bốn điều kiện đó không đủ để ra quyết định.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, đo và ra quyết định đúng về Shell scripting that fails loudly?

## Nỗi Đau & Động Lực

Quên ngoặc kép quanh biến · tin tuỳ chọn dừng khi lỗi bắt được mọi trường hợp · không dọn khi bị dừng giữa chừng · viết 500 dòng shell cho việc cần Python. Đây không phải danh sách lỗi cú pháp. Mỗi lỗi làm người vận hành chọn nhầm owner hoặc chữa symptom ở layer sau, khiến thời gian phục hồi tăng dù command vừa chạy trả về thành công.

Năng lực cần giữ sau bài là: Viết script vận hành dừng đúng lúc lỗi, dọn dẹp khi thoát, và trả mã thoát đúng trong mọi nhánh. Nếu learner chỉ nhắc lại định nghĩa nhưng không phân biệt được hai state gần nhau trên số đo, bài chưa đạt.

## Cơ Chế Tác Động

Shell là keo dán của mọi hệ vận hành, và script shell viết ẩu là nguồn sự cố âm thầm vì mặc định của shell là chạy tiếp khi có lỗi. Ba tuỳ chọn nghiêm ngặt và tác dụng từng cái: dừng khi một lệnh lỗi, coi biến chưa đặt là lỗi, và cho lỗi trong đường ống lan ra. Kèm theo là cảnh báo về các trường hợp tuỳ chọn dừng khi lỗi **không** kích hoạt, vì tin tưởng mù vào nó cũng nguy hiểm. Trích dẫn và khai triển: quên ngoặc kép quanh biến là nguồn lỗi số một khi tên tệp có dấu cách. Bẫy để dọn dẹp khi thoát, tương đương trình quản lý ngữ cảnh ở lesson 15. Mã thoát và cách kiểm tra từng bước theo lesson 67. Khi nào nên dừng viết shell và chuyển sang Python: ba dấu hiệu cụ thể, thường là khi cần cấu trúc dữ liệu, cần xử lý lỗi phân tầng, hoặc script vượt khoảng một trăm dòng.

Tách ba lớp khi đọc cơ chế `wiki.de-foundation.shell-scripting-that-fails-loudly`: declared state là điều cấu hình hoặc API yêu cầu; executed state là việc runtime thực sự làm; consumer-visible state là điều client hay operator quan sát. Ba lớp có thể lệch nhau vì cache, buffering, retry, scheduling, queue hoặc failure giữa hai transition. Evidence phải chỉ ra lớp nào đang được đo.

## Bản Đồ Quyết Định

| Bước | Câu hỏi phải khóa | Điều kiện đạt |
|---|---|---|
| Observe | Khóa process, resource, file descriptor và time window | Không trộn symptom giữa hai owner |
| Probe | Dùng phép đo read-only hẹp nhất | Probe phân biệt được hai giả thuyết |
| Contain | Giảm harm trước mutation | Có rollback và state snapshot |
| Escalate | Chuyển owner khi boundary đã chứng minh | Evidence đủ tái hiện |

Quy tắc mặc định là chọn phép giải thích đơn giản nhất qua được hard constraints, rồi viết trước reversal trigger. Với `Shell scripting that fails loudly`, absence of error không phải pass; pass cần observation đúng grain, một oracle độc lập và changed-constraint case đủ làm model có cơ hội thất bại.

## Case Study Thực Chiến: Shell scripting that fails loudly

Viết script nạp dữ liệu có tạo thư mục tạm, tải tệp, xử lý, rồi dọn. Tiêm năm lỗi: lệnh thất bại giữa chừng, biến chưa đặt, lỗi trong đường ống, tên tệp có dấu cách, và bị dừng giữa chừng. Chứng minh cả năm được xử lý đúng và thư mục tạm luôn được dọn.

Trong case `wiki.de-foundation.shell-scripting-that-fails-loudly`, learner ghi expected transition, input snapshot, version và giới hạn an toàn trước khi chạy. Sau execution, họ giữ raw counter, timestamp, exit status, state trước–sau và giải thích delta bằng mechanism ở trên. Đánh giá không cho phép sửa expected result sau khi nhìn output mà không ghi change record.

Biến thể khó hơn đổi một constraint có khả năng đảo kết luận: workload shape, memory pressure, connection reuse, retry budget, permission hoặc dependency direction. Tầng *áp dụng*. Objective là một tập quy tắc kiểm được bằng thí nghiệm tiêm lỗi. Kiểm bằng năm lỗi tiêm; đạt khi cả năm đều làm script dừng với mã thoát khác không và tài nguyên tạm được dọn.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Quên ngoặc kép quanh biến. **Thực tế:** tín hiệu chỉ chứng minh điều nó đo trong đúng scope; state ở layer khác vẫn có thể trái ngược. **Vì sao nghe hợp lý:** happy path nhỏ thường không chạm queue, cache, partial progress hoặc restart.

**Hiểu lầm:** tin tuỳ chọn dừng khi lỗi bắt được mọi trường hợp. **Thực tế:** tool và API cung cấp primitive, không tự cấp ownership, deadline, idempotency hay recovery policy. **Vì sao nghe hợp lý:** syntax gọn che mất protocol và lifecycle phía dưới.

Với `wiki.de-foundation.shell-scripting-that-fails-loudly`, một edge case đáng giữ là observation đúng nhưng diagnosis sai: counter tăng thật, song nguyên nhân điều khiển nằm ở layer trước. Muốn tránh, timeline phải nối trigger tới consumer harm và ghi rõ negative control nào đã loại giả thuyết cạnh tranh.

## Nếu Bạn Dạy Lại Điều Này...

Mở bài bằng một dự đoán dễ sai về `Shell scripting that fails loudly`, không mở bằng định nghĩa. Cho hai trace gần giống nhau nhưng khác đúng một state boundary; learner phải chọn probe tiếp theo trước khi được xem đáp án.

Bài tập seed dùng chính lab của DE-L068, sau đó đổi constraint đủ mạnh để buộc giữ hoặc đảo quyết định. Người dạy chấm reasoning chain và evidence, không chấm việc learner đoán đúng tên công cụ.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `Shell scripting that fails loudly` dùng điều kiện hoàn thành sau: Năm lỗi đều làm script dừng với mã thoát khác không, và thư mục tạm được dọn trong cả năm trường hợp. Mỗi probe phải có prediction, failure signal và independent oracle.

### Probe 1: state transition và invariant

**Mệnh đề P1 cần kiểm.** Shell là keo dán của mọi hệ vận hành, và script shell viết ẩu là nguồn sự cố âm thầm vì mặc định của shell là chạy tiếp khi có lỗi.

**Thiết kế phép thử.** Với `wiki.de-foundation.shell-scripting-that-fails-loudly`, tạo positive và negative control chỉ khác một điều kiện; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P1 cần giữ.** Với `wiki.de-foundation.shell-scripting-that-fails-loudly`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề P2 cần kiểm.** Viết script vận hành dừng đúng lúc lỗi, dọn dẹp khi thoát, và trả mã thoát đúng trong mọi nhánh.

**Thiết kế phép thử.** Với `wiki.de-foundation.shell-scripting-that-fails-loudly`, tạo boundary case ngay trước và sau ngưỡng; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P2 cần giữ.** Với `wiki.de-foundation.shell-scripting-that-fails-loudly`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề P3 cần kiểm.** Tầng *áp dụng*.

**Thiết kế phép thử.** Với `wiki.de-foundation.shell-scripting-that-fails-loudly`, tạo replay cùng identity nhưng đổi state; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P3 cần giữ.** Với `wiki.de-foundation.shell-scripting-that-fails-loudly`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề P4 cần kiểm.** Viết script nạp dữ liệu có tạo thư mục tạm, tải tệp, xử lý, rồi dọn.

**Thiết kế phép thử.** Với `wiki.de-foundation.shell-scripting-that-fails-loudly`, tạo failure inject trước và sau transition bền vững; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P4 cần giữ.** Với `wiki.de-foundation.shell-scripting-that-fails-loudly`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề P5 cần kiểm.** Quên ngoặc kép quanh biến · tin tuỳ chọn dừng khi lỗi bắt được mọi trường hợp · không dọn khi bị dừng giữa chừng · viết 500 dòng shell cho việc cần Python.

**Thiết kế phép thử.** Với `wiki.de-foundation.shell-scripting-that-fails-loudly`, tạo changed scale làm cost model đổi; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P5 cần giữ.** Với `wiki.de-foundation.shell-scripting-that-fails-loudly`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề P6 cần kiểm.** Năm lỗi đều làm script dừng với mã thoát khác không, và thư mục tạm được dọn trong cả năm trường hợp.

**Thiết kế phép thử.** Với `wiki.de-foundation.shell-scripting-that-fails-loudly`, tạo adversarial order, skew hoặc packet timing; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P6 cần giữ.** Với `wiki.de-foundation.shell-scripting-that-fails-loudly`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề P7 cần kiểm.** Shell là keo dán của mọi hệ vận hành, và script shell viết ẩu là nguồn sự cố âm thầm vì mặc định của shell là chạy tiếp khi có lỗi.

**Thiết kế phép thử.** Với `wiki.de-foundation.shell-scripting-that-fails-loudly`, tạo fresh environment không cache; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P7 cần giữ.** Với `wiki.de-foundation.shell-scripting-that-fails-loudly`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề P8 cần kiểm.** Viết script vận hành dừng đúng lúc lỗi, dọn dẹp khi thoát, và trả mã thoát đúng trong mọi nhánh.

**Thiết kế phép thử.** Với `wiki.de-foundation.shell-scripting-that-fails-loudly`, tạo independent oracle không dùng chung implementation; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P8 cần giữ.** Với `wiki.de-foundation.shell-scripting-that-fails-loudly`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề P9 cần kiểm.** Tầng *áp dụng*.

**Thiết kế phép thử.** Với `wiki.de-foundation.shell-scripting-that-fails-loudly`, tạo partial progress rồi restart; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P9 cần giữ.** Với `wiki.de-foundation.shell-scripting-that-fails-loudly`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề P10 cần kiểm.** Viết script nạp dữ liệu có tạo thư mục tạm, tải tệp, xử lý, rồi dọn.

**Thiết kế phép thử.** Với `wiki.de-foundation.shell-scripting-that-fails-loudly`, tạo missing evidence phải abstain; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P10 cần giữ.** Với `wiki.de-foundation.shell-scripting-that-fails-loudly`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề P11 cần kiểm.** Quên ngoặc kép quanh biến · tin tuỳ chọn dừng khi lỗi bắt được mọi trường hợp · không dọn khi bị dừng giữa chừng · viết 500 dòng shell cho việc cần Python.

**Thiết kế phép thử.** Với `wiki.de-foundation.shell-scripting-that-fails-loudly`, tạo reviewer tái hiện từ evidence package; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P11 cần giữ.** Với `wiki.de-foundation.shell-scripting-that-fails-loudly`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề P12 cần kiểm.** Năm lỗi đều làm script dừng với mã thoát khác không, và thư mục tạm được dọn trong cả năm trường hợp.

**Thiết kế phép thử.** Với `wiki.de-foundation.shell-scripting-that-fails-loudly`, tạo constraint đổi đủ để quyết định đảo; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P12 cần giữ.** Với `wiki.de-foundation.shell-scripting-that-fails-loudly`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên khiến mô hình `Shell scripting that fails loudly` không còn đúng là gì?

<details><summary>Đáp án</summary>Quên ngoặc kép quanh biến · tin tuỳ chọn dừng khi lỗi bắt được mọi trường hợp · không dọn khi bị dừng giữa chừng · viết 500 dòng shell cho việc cần Python.</details>

2. Evidence nào phân biệt được hai state dễ nhầm?

<details><summary>Đáp án</summary>Tầng *áp dụng*. Objective là một tập quy tắc kiểm được bằng thí nghiệm tiêm lỗi. Kiểm bằng năm lỗi tiêm; đạt khi cả năm đều làm script dừng với mã thoát khác không và tài nguyên tạm được dọn.</details>

3. Khi constraint đổi, điều gì quyết định giữ hay đảo lựa chọn?

<details><summary>Đáp án</summary>Năm lỗi đều làm script dừng với mã thoát khác không, và thư mục tạm được dọn trong cả năm trường hợp.</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `Shell scripting that fails loudly` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Hành vi phụ thuộc kernel, distribution, library, network path hoặc hardware phải được kiểm lại trên target đã ghi version.
- Concept key `ck.de.shell-scripting-that-fails-loudly` đang ở trạng thái `proposed`; note chưa được tính là canonical registry coverage.
- Một trace đơn lẻ không chứng minh capacity, reliability hoặc security cho population khác.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-GNU-BASH-REFERENCE]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-GNU-BASH-REFERENCE]] — `src.docs.gnu-bash-reference` | Bash Reference Manual 5.3, shell operation, pipelines, redirection và set builtin; accessed 2026-10-02 | mechanism và boundary liên quan trực tiếp tới `Shell scripting that fails loudly` | cơ chế, quyết định, case và probe | Đã phủ | phần ngoài objective DE-L068 |

## Key takeaways
- Viết script vận hành dừng đúng lúc lỗi, dọn dẹp khi thoát, và trả mã thoát đúng trong mọi nhánh.
- Năm lỗi đều làm script dừng với mã thoát khác không, và thư mục tạm được dọn trong cả năm trường hợp.
- `Shell scripting that fails loudly` chỉ có nghĩa trong scope, state, identity và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.
