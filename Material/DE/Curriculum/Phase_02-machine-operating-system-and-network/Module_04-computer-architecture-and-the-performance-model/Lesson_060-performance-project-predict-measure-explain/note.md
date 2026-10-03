# Phase 2: Machine, Operating System and Network
# Module 4: Computer Architecture and the Performance Model
# Lesson 60: Performance project - predict, measure, explain

## Mục tiêu bài học

**Năng lực cần chứng minh.** Tăng tốc một chương trình ít nhất một mức bậc, mỗi lần sửa dẫn được về một số đo, và kết quả tính ra không đổi.

**Điều kiện hoàn thành.** Cải thiện ≥ 1 mức bậc, kết quả tính ra khớp tuyệt đối với bản gốc, và mọi lần sửa dẫn được về một số đo trong nhật ký.

**Kiến thức và cơ chế.** Bài dự án khép module, và điểm chấm nằm ở chất lượng lập luận chứ ở con số đẹp. Nhận một chương trình xử lý dữ liệu chạy chậm. Quy trình bắt buộc theo đúng thứ tự: đọc mã và **viết dự đoán nút thắt trước khi đo**, đo để xác nhận hoặc bác bỏ dự đoán, sửa đúng một thứ, đo lại, rồi lặp. Ghi lại mọi dự đoán sai và lý do sai, vì đó là phần có giá trị học tập cao nhất và cũng là phần hay bị giấu đi. Yêu cầu đạt: cải thiện ít nhất một mức bậc, kết quả tính ra không đổi, và mỗi lần sửa dẫn được về một số đo. Nộp kèm báo cáo hiệu năng sáu phần theo lesson 59 và sơ đồ đường đi của dữ liệu từ ứng dụng tới thiết bị theo yêu cầu của module. Cấm một điều: sửa nhiều chỗ cùng lúc, vì khi đó không biết chỗ nào có tác dụng.


# Performance project - predict, measure, explain

**Tóm tắt bản chất:** Tăng tốc một chương trình ít nhất một mức bậc, mỗi lần sửa dẫn được về một số đo, và kết quả tính ra không đổi. Cơ chế chỉ có giá trị khi workload, version, state owner và failure boundary đã được khóa; một con số đẹp ngoài bốn điều kiện đó không đủ để ra quyết định.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, đo và ra quyết định đúng về Performance project - predict, measure, explain?

## Nỗi Đau & Động Lực

Sửa nhiều chỗ cùng lúc · tối ưu trước khi đo · giấu dự đoán sai · cải thiện tốc độ mà đổi kết quả tính ra. Đây không phải danh sách lỗi cú pháp. Mỗi lỗi làm người vận hành chọn nhầm owner hoặc chữa symptom ở layer sau, khiến thời gian phục hồi tăng dù command vừa chạy trả về thành công.

Năng lực cần giữ sau bài là: Tăng tốc một chương trình ít nhất một mức bậc, mỗi lần sửa dẫn được về một số đo, và kết quả tính ra không đổi. Nếu learner chỉ nhắc lại định nghĩa nhưng không phân biệt được hai state gần nhau trên số đo, bài chưa đạt.

## Cơ Chế Tác Động

Bài dự án khép module, và điểm chấm nằm ở chất lượng lập luận chứ ở con số đẹp. Nhận một chương trình xử lý dữ liệu chạy chậm. Quy trình bắt buộc theo đúng thứ tự: đọc mã và **viết dự đoán nút thắt trước khi đo**, đo để xác nhận hoặc bác bỏ dự đoán, sửa đúng một thứ, đo lại, rồi lặp. Ghi lại mọi dự đoán sai và lý do sai, vì đó là phần có giá trị học tập cao nhất và cũng là phần hay bị giấu đi. Yêu cầu đạt: cải thiện ít nhất một mức bậc, kết quả tính ra không đổi, và mỗi lần sửa dẫn được về một số đo. Nộp kèm báo cáo hiệu năng sáu phần theo lesson 59 và sơ đồ đường đi của dữ liệu từ ứng dụng tới thiết bị theo yêu cầu của module. Cấm một điều: sửa nhiều chỗ cùng lúc, vì khi đó không biết chỗ nào có tác dụng.

Tách ba lớp khi đọc cơ chế `wiki.de-foundation.performance-project-predict-measure-explain`: declared state là điều cấu hình hoặc API yêu cầu; executed state là việc runtime thực sự làm; consumer-visible state là điều client hay operator quan sát. Ba lớp có thể lệch nhau vì cache, buffering, retry, scheduling, queue hoặc failure giữa hai transition. Evidence phải chỉ ra lớp nào đang được đo.

## Bản Đồ Quyết Định

| Bước | Câu hỏi phải khóa | Điều kiện đạt |
|---|---|---|
| Model | Giải thích chi phí bằng hierarchy, parallel fraction hoặc data movement | Model dự đoán đúng khi đổi scale |
| Measure | Dùng counter và benchmark khóa workload | Observation khớp oracle và có raw sample |
| Explain | Nối delta với mechanism | Reviewer tái hiện được reasoning |
| Reverse | Đổi workload, layout hoặc resource | Quyết định đổi khi bottleneck đổi |

Quy tắc mặc định là chọn phép giải thích đơn giản nhất qua được hard constraints, rồi viết trước reversal trigger. Với `Performance project - predict, measure, explain`, absence of error không phải pass; pass cần observation đúng grain, một oracle độc lập và changed-constraint case đủ làm model có cơ hội thất bại.

## Case Study Thực Chiến: Performance project - predict, measure, explain

Nhận chương trình chậm. Viết dự đoán trước. Đo, sửa từng thứ một, đo lại sau mỗi lần. Ghi nhật ký gồm cả dự đoán sai. Nộp báo cáo sáu phần và sơ đồ đường đi dữ liệu. Đối soát kết quả tính ra với bản gốc.

Trong case `wiki.de-foundation.performance-project-predict-measure-explain`, learner ghi expected transition, input snapshot, version và giới hạn an toàn trước khi chạy. Sau execution, họ giữ raw counter, timestamp, exit status, state trước–sau và giải thích delta bằng mechanism ở trên. Đánh giá không cho phép sửa expected result sau khi nhìn output mà không ghi change record.

Biến thể khó hơn đổi một constraint có khả năng đảo kết luận: workload shape, memory pressure, connection reuse, retry budget, permission hoặc dependency direction. Tầng *sáng tạo*. Bài tổng hợp toàn module thành một quy trình tối ưu có bằng chứng. Kiểm bằng cặp số đo trước sau cộng rà soát nhật ký; đạt khi cải thiện đạt ngưỡng, kết quả không đổi, và mọi lần sửa có số đo dẫn chứng.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Sửa nhiều chỗ cùng lúc. **Thực tế:** tín hiệu chỉ chứng minh điều nó đo trong đúng scope; state ở layer khác vẫn có thể trái ngược. **Vì sao nghe hợp lý:** happy path nhỏ thường không chạm queue, cache, partial progress hoặc restart.

**Hiểu lầm:** tối ưu trước khi đo. **Thực tế:** tool và API cung cấp primitive, không tự cấp ownership, deadline, idempotency hay recovery policy. **Vì sao nghe hợp lý:** syntax gọn che mất protocol và lifecycle phía dưới.

Với `wiki.de-foundation.performance-project-predict-measure-explain`, một edge case đáng giữ là observation đúng nhưng diagnosis sai: counter tăng thật, song nguyên nhân điều khiển nằm ở layer trước. Muốn tránh, timeline phải nối trigger tới consumer harm và ghi rõ negative control nào đã loại giả thuyết cạnh tranh.

## Nếu Bạn Dạy Lại Điều Này...

Mở bài bằng một dự đoán dễ sai về `Performance project - predict, measure, explain`, không mở bằng định nghĩa. Cho hai trace gần giống nhau nhưng khác đúng một state boundary; learner phải chọn probe tiếp theo trước khi được xem đáp án.

Bài tập seed dùng chính lab của DE-L060, sau đó đổi constraint đủ mạnh để buộc giữ hoặc đảo quyết định. Người dạy chấm reasoning chain và evidence, không chấm việc learner đoán đúng tên công cụ.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `Performance project - predict, measure, explain` dùng điều kiện hoàn thành sau: Cải thiện ≥ 1 mức bậc, kết quả tính ra khớp tuyệt đối với bản gốc, và mọi lần sửa dẫn được về một số đo trong nhật ký. Mỗi probe phải có prediction, failure signal và independent oracle.

### Probe 1: state transition và invariant

**Mệnh đề P1 cần kiểm.** Bài dự án khép module, và điểm chấm nằm ở chất lượng lập luận chứ ở con số đẹp.

**Thiết kế phép thử.** Với `wiki.de-foundation.performance-project-predict-measure-explain`, tạo positive và negative control chỉ khác một điều kiện; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P1 cần giữ.** Với `wiki.de-foundation.performance-project-predict-measure-explain`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề P2 cần kiểm.** Tăng tốc một chương trình ít nhất một mức bậc, mỗi lần sửa dẫn được về một số đo, và kết quả tính ra không đổi.

**Thiết kế phép thử.** Với `wiki.de-foundation.performance-project-predict-measure-explain`, tạo boundary case ngay trước và sau ngưỡng; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P2 cần giữ.** Với `wiki.de-foundation.performance-project-predict-measure-explain`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề P3 cần kiểm.** Tầng *sáng tạo*.

**Thiết kế phép thử.** Với `wiki.de-foundation.performance-project-predict-measure-explain`, tạo replay cùng identity nhưng đổi state; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P3 cần giữ.** Với `wiki.de-foundation.performance-project-predict-measure-explain`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề P4 cần kiểm.** Nhận chương trình chậm.

**Thiết kế phép thử.** Với `wiki.de-foundation.performance-project-predict-measure-explain`, tạo failure inject trước và sau transition bền vững; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P4 cần giữ.** Với `wiki.de-foundation.performance-project-predict-measure-explain`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề P5 cần kiểm.** Sửa nhiều chỗ cùng lúc · tối ưu trước khi đo · giấu dự đoán sai · cải thiện tốc độ mà đổi kết quả tính ra.

**Thiết kế phép thử.** Với `wiki.de-foundation.performance-project-predict-measure-explain`, tạo changed scale làm cost model đổi; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P5 cần giữ.** Với `wiki.de-foundation.performance-project-predict-measure-explain`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề P6 cần kiểm.** Cải thiện ≥ 1 mức bậc, kết quả tính ra khớp tuyệt đối với bản gốc, và mọi lần sửa dẫn được về một số đo trong nhật ký.

**Thiết kế phép thử.** Với `wiki.de-foundation.performance-project-predict-measure-explain`, tạo adversarial order, skew hoặc packet timing; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P6 cần giữ.** Với `wiki.de-foundation.performance-project-predict-measure-explain`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề P7 cần kiểm.** Bài dự án khép module, và điểm chấm nằm ở chất lượng lập luận chứ ở con số đẹp.

**Thiết kế phép thử.** Với `wiki.de-foundation.performance-project-predict-measure-explain`, tạo fresh environment không cache; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P7 cần giữ.** Với `wiki.de-foundation.performance-project-predict-measure-explain`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề P8 cần kiểm.** Tăng tốc một chương trình ít nhất một mức bậc, mỗi lần sửa dẫn được về một số đo, và kết quả tính ra không đổi.

**Thiết kế phép thử.** Với `wiki.de-foundation.performance-project-predict-measure-explain`, tạo independent oracle không dùng chung implementation; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P8 cần giữ.** Với `wiki.de-foundation.performance-project-predict-measure-explain`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề P9 cần kiểm.** Tầng *sáng tạo*.

**Thiết kế phép thử.** Với `wiki.de-foundation.performance-project-predict-measure-explain`, tạo partial progress rồi restart; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P9 cần giữ.** Với `wiki.de-foundation.performance-project-predict-measure-explain`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề P10 cần kiểm.** Nhận chương trình chậm.

**Thiết kế phép thử.** Với `wiki.de-foundation.performance-project-predict-measure-explain`, tạo missing evidence phải abstain; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P10 cần giữ.** Với `wiki.de-foundation.performance-project-predict-measure-explain`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề P11 cần kiểm.** Sửa nhiều chỗ cùng lúc · tối ưu trước khi đo · giấu dự đoán sai · cải thiện tốc độ mà đổi kết quả tính ra.

**Thiết kế phép thử.** Với `wiki.de-foundation.performance-project-predict-measure-explain`, tạo reviewer tái hiện từ evidence package; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P11 cần giữ.** Với `wiki.de-foundation.performance-project-predict-measure-explain`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề P12 cần kiểm.** Cải thiện ≥ 1 mức bậc, kết quả tính ra khớp tuyệt đối với bản gốc, và mọi lần sửa dẫn được về một số đo trong nhật ký.

**Thiết kế phép thử.** Với `wiki.de-foundation.performance-project-predict-measure-explain`, tạo constraint đổi đủ để quyết định đảo; khóa workload, version, identity, permission, clock và state ban đầu. Expected result được viết trước execution để tiêu chí không trôi theo output.

**Bằng chứng P12 cần giữ.** Với `wiki.de-foundation.performance-project-predict-measure-explain`, lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp đúng grain; nếu chưa chạy thì đây vẫn là protocol, không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên khiến mô hình `Performance project - predict, measure, explain` không còn đúng là gì?

<details><summary>Đáp án</summary>Sửa nhiều chỗ cùng lúc · tối ưu trước khi đo · giấu dự đoán sai · cải thiện tốc độ mà đổi kết quả tính ra.</details>

2. Evidence nào phân biệt được hai state dễ nhầm?

<details><summary>Đáp án</summary>Tầng *sáng tạo*. Bài tổng hợp toàn module thành một quy trình tối ưu có bằng chứng. Kiểm bằng cặp số đo trước sau cộng rà soát nhật ký; đạt khi cải thiện đạt ngưỡng, kết quả không đổi, và mọi lần sửa có số đo dẫn chứng.</details>

3. Khi constraint đổi, điều gì quyết định giữ hay đảo lựa chọn?

<details><summary>Đáp án</summary>Cải thiện ≥ 1 mức bậc, kết quả tính ra khớp tuyệt đối với bản gốc, và mọi lần sửa dẫn được về một số đo trong nhật ký.</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `Performance project - predict, measure, explain` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Hành vi phụ thuộc kernel, distribution, library, network path hoặc hardware phải được kiểm lại trên target đã ghi version.
- Concept key `ck.de.performance-project-predict-measure-explain` đang ở trạng thái `proposed`; note chưa được tính là canonical registry coverage.
- Một trace đơn lẻ không chứng minh capacity, reliability hoặc security cho population khác.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-PATTERSON-HENNESSY-COD-5E]]
2. [[SRC-HUNT-THOMAS-PRAGMATIC-PROGRAMMER-20AE]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-PATTERSON-HENNESSY-COD-5E]] — `src.book.patterson-hennessy-cod.5e` | Chapter 5 và §6.3; PDF 397–538 | mechanism và boundary liên quan trực tiếp tới `Performance project - predict, measure, explain` | cơ chế, quyết định, case và probe | Đã phủ | phần ngoài objective DE-L060 |
| [[SRC-HUNT-THOMAS-PRAGMATIC-PROGRAMMER-20AE]] — `src.book.hunt-thomas-pragmatic-programmer.20ae` | Topics 10, 23–25 và 40; PDF 76–280 | mechanism và boundary liên quan trực tiếp tới `Performance project - predict, measure, explain` | cơ chế, quyết định, case và probe | Đã phủ | phần ngoài objective DE-L060 |

## Key takeaways
- Tăng tốc một chương trình ít nhất một mức bậc, mỗi lần sửa dẫn được về một số đo, và kết quả tính ra không đổi.
- Cải thiện ≥ 1 mức bậc, kết quả tính ra khớp tuyệt đối với bản gốc, và mọi lần sửa dẫn được về một số đo trong nhật ký.
- `Performance project - predict, measure, explain` chỉ có nghĩa trong scope, state, identity và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.
