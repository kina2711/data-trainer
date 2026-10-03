# Phase 2: Machine, Operating System and Network
# Module 5: Operating Systems, Concurrency and Linux
# Lesson 61: User mode, kernel mode and the process lifecycle

## Mục tiêu bài học

**Năng lực cần chứng minh.** Đọc trạng thái của một tiến trình và suy ra nó đang chờ cái gì, phân biệt được chờ vào ra với chờ CPU.

**Điều kiện hoàn thành.** Phân loại đúng ≥ 4/5 trạng thái, và nhận ra đúng tiến trình đang chờ vào ra không ngắt được.

**Kiến thức và cơ chế.** Hai chế độ thực thi và ranh giới giữa chúng là thứ đã gặp ở lesson 54 dưới góc chi phí; bài này nhìn từ góc cơ chế. Chương trình chạy ở chế độ người dùng và không đụng trực tiếp vào phần cứng; mọi yêu cầu đều qua lời gọi hệ thống. Ngắt và bẫy là hai đường vào nhân khác nhau. Vòng đời tiến trình: tạo bằng nhân bản rồi thay thế ảnh chương trình, và vì sao hai bước đó tách rời lại hữu dụng. Các trạng thái của tiến trình và ý nghĩa vận hành của từng trạng thái, đặc biệt trạng thái chờ vào ra không ngắt được vì nó là dấu hiệu đĩa hoặc mạng có vấn đề. Tiến trình xác sống và tiến trình mồ côi, cùng cách chúng phát sinh; nối lại vấn đề tiến trình con mồ côi đã gặp ở lesson 23. Tiến trình so với luồng ở mức nhân: khác nhau ở chỗ chia sẻ không gian địa chỉ hay không, và mọi hệ quả suy ra từ đó.


# User mode, kernel mode and the process lifecycle

**Tóm tắt bản chất:** Đọc trạng thái của một tiến trình và suy ra nó đang chờ cái gì, phân biệt được chờ vào ra với chờ CPU. Cơ chế chỉ có giá trị khi workload, version, state owner và failure boundary đã được khóa; một con số đẹp ngoài bốn điều kiện đó không đủ để ra quyết định.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, đo và ra quyết định đúng về User mode, kernel mode and the process lifecycle?

## Nỗi Đau & Động Lực

Nhầm chờ vào ra với chờ CPU nên chẩn đoán sai · không biết trạng thái xác sống nghĩa là gì · dùng lệnh liệt kê tiến trình mà không đọc cột trạng thái. Đây không phải danh sách lỗi cú pháp. Mỗi lỗi làm người vận hành chọn nhầm owner hoặc chữa symptom ở layer sau, khiến thời gian phục hồi tăng dù command vừa chạy trả về thành công.

Năng lực cần giữ sau bài là: Đọc trạng thái của một tiến trình và suy ra nó đang chờ cái gì, phân biệt được chờ vào ra với chờ CPU. Nếu learner chỉ nhắc lại định nghĩa nhưng không phân biệt được hai state gần nhau trên số đo, bài chưa đạt.

## Cơ Chế Tác Động

Hai chế độ thực thi và ranh giới giữa chúng là thứ đã gặp ở lesson 54 dưới góc chi phí; bài này nhìn từ góc cơ chế. Chương trình chạy ở chế độ người dùng và không đụng trực tiếp vào phần cứng; mọi yêu cầu đều qua lời gọi hệ thống. Ngắt và bẫy là hai đường vào nhân khác nhau. Vòng đời tiến trình: tạo bằng nhân bản rồi thay thế ảnh chương trình, và vì sao hai bước đó tách rời lại hữu dụng. Các trạng thái của tiến trình và ý nghĩa vận hành của từng trạng thái, đặc biệt trạng thái chờ vào ra không ngắt được vì nó là dấu hiệu đĩa hoặc mạng có vấn đề. Tiến trình xác sống và tiến trình mồ côi, cùng cách chúng phát sinh; nối lại vấn đề tiến trình con mồ côi đã gặp ở lesson 23. Tiến trình so với luồng ở mức nhân: khác nhau ở chỗ chia sẻ không gian địa chỉ hay không, và mọi hệ quả suy ra từ đó.

Tách ba lớp khi đọc cơ chế `wiki.de-foundation.user-mode-kernel-mode-and-the-process-lifecycle`: declared state là điều cấu hình hoặc API yêu cầu; executed state là việc runtime thực sự làm; consumer-visible state là điều client hay operator quan sát. Ba lớp có thể lệch nhau vì cache, buffering, retry, scheduling, queue hoặc failure giữa hai transition. Evidence phải chỉ ra lớp nào đang được đo.

## Bản Đồ Quyết Định

| Bước | Câu hỏi phải khóa | Điều kiện đạt |
|---|---|---|
| Observe | Khóa process, resource, file descriptor và time window | Không trộn symptom giữa hai owner |
| Probe | Dùng phép đo read-only hẹp nhất | Probe phân biệt được hai giả thuyết |
| Contain | Giảm harm trước mutation | Có rollback và state snapshot |
| Escalate | Chuyển owner khi boundary đã chứng minh | Evidence đủ tái hiện |

Quy tắc mặc định là chọn phép giải thích đơn giản nhất qua được hard constraints, rồi viết trước reversal trigger. Với `User mode, kernel mode and the process lifecycle`, absence of error không phải pass; pass cần observation đúng grain, một oracle độc lập và changed-constraint case đủ làm model có cơ hội thất bại.

## Case Study Thực Chiến: User mode, kernel mode and the process lifecycle

Tạo năm tiến trình ở năm trạng thái khác nhau gồm đang chạy, chờ được cấp CPU, chờ vào ra, dừng, và xác sống. Quan sát trạng thái qua công cụ hệ thống và qua hệ tệp ảo của nhân. Phân loại từng cái. Tạo một tiến trình mồ côi và quan sát nó được nhận nuôi.

Trong case `wiki.de-foundation.user-mode-kernel-mode-and-the-process-lifecycle`, learner ghi expected transition, input snapshot, version và giới hạn an toàn trước khi chạy. Sau execution, họ giữ raw counter, timestamp, exit status, state trước–sau và giải thích delta bằng mechanism ở trên. Đánh giá không cho phép sửa expected result sau khi nhìn output mà không ghi change record.

Biến thể khó hơn đổi một constraint có khả năng đảo kết luận: workload shape, memory pressure, connection reuse, retry budget, permission hoặc dependency direction. Tầng *hiểu*. Bài mở module, đặt từ vựng cho phần chẩn đoán sau. Kiểm bằng bài đọc trạng thái trên năm tiến trình thật; đạt khi phân loại đúng ít nhất bốn và nhận ra đúng tiến trình đang ở trạng thái chờ vào ra không ngắt được.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Nhầm chờ vào ra với chờ CPU nên chẩn đoán sai. **Thực tế:** tín hiệu chỉ chứng minh điều nó đo trong đúng scope; state ở layer khác vẫn có thể trái ngược. **Vì sao nghe hợp lý:** happy path nhỏ thường không chạm queue, cache, partial progress hoặc restart.

**Hiểu lầm:** không biết trạng thái xác sống nghĩa là gì. **Thực tế:** tool và API cung cấp primitive, không tự cấp ownership, deadline, idempotency hay recovery policy. **Vì sao nghe hợp lý:** syntax gọn che mất protocol và lifecycle phía dưới.

Với `wiki.de-foundation.user-mode-kernel-mode-and-the-process-lifecycle`, một edge case đáng giữ là observation đúng nhưng diagnosis sai: counter tăng thật, song nguyên nhân điều khiển nằm ở layer trước. Muốn tránh, timeline phải nối trigger tới consumer harm và ghi rõ negative control nào đã loại giả thuyết cạnh tranh.

## Nếu Bạn Dạy Lại Điều Này...

Mở bài bằng một dự đoán dễ sai về `User mode, kernel mode and the process lifecycle`, không mở bằng định nghĩa. Cho hai trace gần giống nhau nhưng khác đúng một state boundary; learner phải chọn probe tiếp theo trước khi được xem đáp án.

Bài tập seed dùng chính lab của DE-L061, sau đó đổi constraint đủ mạnh để buộc giữ hoặc đảo quyết định. Người dạy chấm reasoning chain và evidence, không chấm việc learner đoán đúng tên công cụ.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `User mode, kernel mode and the process lifecycle` dùng điều kiện hoàn thành sau: Phân loại đúng ≥ 4/5 trạng thái, và nhận ra đúng tiến trình đang chờ vào ra không ngắt được. Mỗi probe phải có prediction, failure signal và independent oracle.

### Probe 1: state transition và invariant

**Mệnh đề P1 cần kiểm.** Hai chế độ thực thi và ranh giới giữa chúng là thứ đã gặp ở lesson 54 dưới góc chi phí; bài này nhìn từ góc cơ chế.

**Thiết kế phép thử.** Với `wiki.de-foundation.user-mode-kernel-mode-and-the-process-lifecycle`, tạo positive và negative control chỉ khác một điều kiện; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P1 cần giữ.** Với `wiki.de-foundation.user-mode-kernel-mode-and-the-process-lifecycle`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề P2 cần kiểm.** Đọc trạng thái của một tiến trình và suy ra nó đang chờ cái gì, phân biệt được chờ vào ra với chờ CPU.

**Thiết kế phép thử.** Với `wiki.de-foundation.user-mode-kernel-mode-and-the-process-lifecycle`, tạo boundary case ngay trước và sau ngưỡng; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P2 cần giữ.** Với `wiki.de-foundation.user-mode-kernel-mode-and-the-process-lifecycle`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề P3 cần kiểm.** Tầng *hiểu*.

**Thiết kế phép thử.** Với `wiki.de-foundation.user-mode-kernel-mode-and-the-process-lifecycle`, tạo replay cùng identity nhưng đổi state; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P3 cần giữ.** Với `wiki.de-foundation.user-mode-kernel-mode-and-the-process-lifecycle`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề P4 cần kiểm.** Tạo năm tiến trình ở năm trạng thái khác nhau gồm đang chạy, chờ được cấp CPU, chờ vào ra, dừng, và xác sống.

**Thiết kế phép thử.** Với `wiki.de-foundation.user-mode-kernel-mode-and-the-process-lifecycle`, tạo failure inject trước và sau transition bền vững; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P4 cần giữ.** Với `wiki.de-foundation.user-mode-kernel-mode-and-the-process-lifecycle`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề P5 cần kiểm.** Nhầm chờ vào ra với chờ CPU nên chẩn đoán sai · không biết trạng thái xác sống nghĩa là gì · dùng lệnh liệt kê tiến trình mà không đọc cột trạng thái.

**Thiết kế phép thử.** Với `wiki.de-foundation.user-mode-kernel-mode-and-the-process-lifecycle`, tạo changed scale làm cost model đổi; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P5 cần giữ.** Với `wiki.de-foundation.user-mode-kernel-mode-and-the-process-lifecycle`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề P6 cần kiểm.** Phân loại đúng ≥ 4/5 trạng thái, và nhận ra đúng tiến trình đang chờ vào ra không ngắt được.

**Thiết kế phép thử.** Với `wiki.de-foundation.user-mode-kernel-mode-and-the-process-lifecycle`, tạo adversarial order, skew hoặc packet timing; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P6 cần giữ.** Với `wiki.de-foundation.user-mode-kernel-mode-and-the-process-lifecycle`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề P7 cần kiểm.** Hai chế độ thực thi và ranh giới giữa chúng là thứ đã gặp ở lesson 54 dưới góc chi phí; bài này nhìn từ góc cơ chế.

**Thiết kế phép thử.** Với `wiki.de-foundation.user-mode-kernel-mode-and-the-process-lifecycle`, tạo fresh environment không cache; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P7 cần giữ.** Với `wiki.de-foundation.user-mode-kernel-mode-and-the-process-lifecycle`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề P8 cần kiểm.** Đọc trạng thái của một tiến trình và suy ra nó đang chờ cái gì, phân biệt được chờ vào ra với chờ CPU.

**Thiết kế phép thử.** Với `wiki.de-foundation.user-mode-kernel-mode-and-the-process-lifecycle`, tạo independent oracle không dùng chung implementation; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P8 cần giữ.** Với `wiki.de-foundation.user-mode-kernel-mode-and-the-process-lifecycle`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề P9 cần kiểm.** Tầng *hiểu*.

**Thiết kế phép thử.** Với `wiki.de-foundation.user-mode-kernel-mode-and-the-process-lifecycle`, tạo partial progress rồi restart; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P9 cần giữ.** Với `wiki.de-foundation.user-mode-kernel-mode-and-the-process-lifecycle`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề P10 cần kiểm.** Tạo năm tiến trình ở năm trạng thái khác nhau gồm đang chạy, chờ được cấp CPU, chờ vào ra, dừng, và xác sống.

**Thiết kế phép thử.** Với `wiki.de-foundation.user-mode-kernel-mode-and-the-process-lifecycle`, tạo missing evidence phải abstain; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P10 cần giữ.** Với `wiki.de-foundation.user-mode-kernel-mode-and-the-process-lifecycle`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề P11 cần kiểm.** Nhầm chờ vào ra với chờ CPU nên chẩn đoán sai · không biết trạng thái xác sống nghĩa là gì · dùng lệnh liệt kê tiến trình mà không đọc cột trạng thái.

**Thiết kế phép thử.** Với `wiki.de-foundation.user-mode-kernel-mode-and-the-process-lifecycle`, tạo reviewer tái hiện từ evidence package; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P11 cần giữ.** Với `wiki.de-foundation.user-mode-kernel-mode-and-the-process-lifecycle`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề P12 cần kiểm.** Phân loại đúng ≥ 4/5 trạng thái, và nhận ra đúng tiến trình đang chờ vào ra không ngắt được.

**Thiết kế phép thử.** Với `wiki.de-foundation.user-mode-kernel-mode-and-the-process-lifecycle`, tạo constraint đổi đủ để quyết định đảo; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P12 cần giữ.** Với `wiki.de-foundation.user-mode-kernel-mode-and-the-process-lifecycle`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên khiến mô hình `User mode, kernel mode and the process lifecycle` không còn đúng là gì?

<details><summary>Đáp án</summary>Nhầm chờ vào ra với chờ CPU nên chẩn đoán sai · không biết trạng thái xác sống nghĩa là gì · dùng lệnh liệt kê tiến trình mà không đọc cột trạng thái.</details>

2. Evidence nào phân biệt được hai state dễ nhầm?

<details><summary>Đáp án</summary>Tầng *hiểu*. Bài mở module, đặt từ vựng cho phần chẩn đoán sau. Kiểm bằng bài đọc trạng thái trên năm tiến trình thật; đạt khi phân loại đúng ít nhất bốn và nhận ra đúng tiến trình đang ở trạng thái chờ vào ra không ngắt được.</details>

3. Khi constraint đổi, điều gì quyết định giữ hay đảo lựa chọn?

<details><summary>Đáp án</summary>Phân loại đúng ≥ 4/5 trạng thái, và nhận ra đúng tiến trình đang chờ vào ra không ngắt được.</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `User mode, kernel mode and the process lifecycle` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Hành vi phụ thuộc kernel, distribution, library, network path hoặc hardware phải được kiểm lại trên target đã ghi version.
- Concept key `ck.de.user-mode-kernel-mode-and-the-process-lifecycle` đang ở trạng thái `proposed`; note chưa được tính là canonical registry coverage.
- Một trace đơn lẻ không chứng minh capacity, reliability hoặc security cho population khác.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-TLPI-2010]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-TLPI-2010]] — `src.book.tlpi.2010` | Chapters 4–39, 49–50, 61 và 63 theo scope record; PDF 113–1418 | mechanism và boundary liên quan trực tiếp tới `User mode, kernel mode and the process lifecycle` | cơ chế, quyết định, case và probe | Đã phủ | phần ngoài objective DE-L061 |

## Key takeaways
- Đọc trạng thái của một tiến trình và suy ra nó đang chờ cái gì, phân biệt được chờ vào ra với chờ CPU.
- Phân loại đúng ≥ 4/5 trạng thái, và nhận ra đúng tiến trình đang chờ vào ra không ngắt được.
- `User mode, kernel mode and the process lifecycle` chỉ có nghĩa trong scope, state, identity và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.
