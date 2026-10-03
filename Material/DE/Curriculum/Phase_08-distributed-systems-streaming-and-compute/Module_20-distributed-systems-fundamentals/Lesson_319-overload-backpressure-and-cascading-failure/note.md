# Phase 8: Distributed Systems, Streaming and Compute
# Module 20: Distributed Systems Fundamentals
# Lesson 319: Overload, backpressure and cascading failure

## Mục tiêu bài học

**Năng lực cần chứng minh.** Tái hiện một lần sập dây chuyền và chặn nó bằng bốn cơ chế, có số đo trước sau.

**Điều kiện hoàn thành.** Bản chưa phòng thủ sập hoàn toàn còn bản có phòng thủ giữ tỉ lệ phục vụ trên ngưỡng, và đóng góp của từng cơ chế có số đo.

> [!abstract] Câu hỏi trung tâm
> Backpressure và admission control chặn overload biến thành cascading failure bằng cách nào?

## 1. Capacity envelope

Service có finite CPU, memory, I/O, connections và downstream quota; latency tăng phi tuyến khi utilization sát saturation. Đừng bắt đầu bằng tên công cụ. Hãy bắt đầu bằng đối tượng được bảo vệ, boundary quan sát được và hậu quả nếu kết luận sai. Trong bài `Overload, backpressure and cascading failure`, câu hỏi thực dụng là: Backpressure và admission control chặn overload biến thành cascading failure bằng cách nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 2. Queueing

Unbounded queue đổi immediate rejection thành memory growth và stale work; queue length cần bound và deadline-aware discard. Điểm khó không nằm ở cú pháp mà ở identity và scope. Hai phép đo cùng tên vẫn có thể nói về hai population hoặc hai thời điểm khác nhau. Trong bài `Overload, backpressure and cascading failure`, câu hỏi thực dụng là: Backpressure và admission control chặn overload biến thành cascading failure bằng cách nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 3. Backpressure

Consumer/downstream truyền capacity signal upstream qua demand, credits, lag hoặc blocking; signal chậm vẫn gây overshoot. Một dashboard xanh chỉ là tín hiệu. Muốn biến nó thành bằng chứng phải giữ input, phiên bản, rule, trạng thái trước–sau và cách tính độc lập. Trong bài `Overload, backpressure and cascading failure`, câu hỏi thực dụng là: Backpressure và admission control chặn overload biến thành cascading failure bằng cách nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 4. Load shedding

Reject early theo priority/cost và preserve critical path; retries phải có backoff, jitter, budgets và retryability classification. Thiết kế tốt phải chịu được counterexample. Hãy chủ động tạo case sát boundary, case thiếu dữ liệu và case replay thay vì chỉ chạy happy path. Trong bài `Overload, backpressure and cascading failure`, câu hỏi thực dụng là: Backpressure và admission control chặn overload biến thành cascading failure bằng cách nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 5. Cascade

Timeouts dài, synchronized retries, shared pools và health-check work khuếch đại failure qua dependencies. Chi phí vận hành thuộc contract. Một rule đúng nhưng quá đắt, quá ồn hoặc không có owner sẽ nhanh chóng bị tắt và mất tác dụng. Trong bài `Overload, backpressure and cascading failure`, câu hỏi thực dụng là: Backpressure và admission control chặn overload biến thành cascading failure bằng cách nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 6. Game day

Ramp load, slow dependency và kill capacity; đo throughput, tail latency, queues, rejected work, recovery time và correctness. Kết luận cần có điều kiện đảo chiều. Khi volume, latency, nguồn thẩm quyền hoặc topology đổi, quyết định cũ phải được xem xét lại bằng cùng một oracle. Trong bài `Overload, backpressure and cascading failure`, câu hỏi thực dụng là: Backpressure và admission control chặn overload biến thành cascading failure bằng cách nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 7. Ma trận kiểm chứng từng mệnh đề

Với `wiki.distributed.overload-backpressure-cascade`, command thành công không tự chứng minh dữ liệu đúng. Protocol riêng của bài là: Chạy bounded state/history fixture với deterministic fault schedule và kiểm counterexample bằng independent state-machine oracle. Mỗi probe dưới đây phải nối input boundary với failure signal và oracle có thể phản bác kết luận.

### 7.1. Overload, backpressure and cascading failure: kiểm `Capacity envelope` bằng case 1, cụ thể service có finite cpu, memory, i/o, connections và downstream quota; latency tăng phi tuyến khi utilization sát saturation

**Mệnh đề cần kiểm.** Overload, backpressure and cascading failure: kiểm `Capacity envelope` bằng case 1, cụ thể service có finite cpu, memory, i/o, connections và downstream quota; latency tăng phi tuyến khi utilization sát saturation.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.distributed.overload-backpressure-cascade`, tạo positive control và negative control chỉ khác đúng một điều kiện. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Overload, backpressure and cascading failure` công bố.

**Bằng chứng cần giữ.** Đối với probe 1 của `Overload, backpressure and cascading failure`, giữ fixture, raw failing rows và lệnh tái hiện. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.2. Overload, backpressure and cascading failure: kiểm `Queueing` bằng case 2, cụ thể unbounded queue đổi immediate rejection thành memory growth và stale work; queue length cần bound và deadline-aware discard

**Mệnh đề cần kiểm.** Overload, backpressure and cascading failure: kiểm `Queueing` bằng case 2, cụ thể unbounded queue đổi immediate rejection thành memory growth và stale work; queue length cần bound và deadline-aware discard.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.distributed.overload-backpressure-cascade`, đổi grain nhưng giữ tổng số dòng để lộ phép đo sai cấp. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Overload, backpressure and cascading failure` công bố.

**Bằng chứng cần giữ.** Đối với probe 2 của `Overload, backpressure and cascading failure`, báo numerator, denominator và key set ở cả hai grain. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.3. Overload, backpressure and cascading failure: kiểm `Backpressure` bằng case 3, cụ thể consumer/downstream truyền capacity signal upstream qua demand, credits, lag hoặc blocking; signal chậm vẫn gây overshoot

**Mệnh đề cần kiểm.** Overload, backpressure and cascading failure: kiểm `Backpressure` bằng case 3, cụ thể consumer/downstream truyền capacity signal upstream qua demand, credits, lag hoặc blocking; signal chậm vẫn gây overshoot.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.distributed.overload-backpressure-cascade`, đưa một giá trị tới đúng boundary và một giá trị vượt boundary. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Overload, backpressure and cascading failure` công bố.

**Bằng chứng cần giữ.** Đối với probe 3 của `Overload, backpressure and cascading failure`, lưu hai observed values cùng rule đã resolve. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.4. Overload, backpressure and cascading failure: kiểm `Load shedding` bằng case 4, cụ thể reject early theo priority/cost và preserve critical path; retries phải có backoff, jitter, budgets và retryability classification

**Mệnh đề cần kiểm.** Overload, backpressure and cascading failure: kiểm `Load shedding` bằng case 4, cụ thể reject early theo priority/cost và preserve critical path; retries phải có backoff, jitter, budgets và retryability classification.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.distributed.overload-backpressure-cascade`, kill tiến trình ngay trước rồi ngay sau durable side effect. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Overload, backpressure and cascading failure` công bố.

**Bằng chứng cần giữ.** Đối với probe 4 của `Overload, backpressure and cascading failure`, lưu checkpoint, external ledger và trạng thái sau restart. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.5. Overload, backpressure and cascading failure: kiểm `Cascade` bằng case 5, cụ thể timeouts dài, synchronized retries, shared pools và health-check work khuếch đại failure qua dependencies

**Mệnh đề cần kiểm.** Overload, backpressure and cascading failure: kiểm `Cascade` bằng case 5, cụ thể timeouts dài, synchronized retries, shared pools và health-check work khuếch đại failure qua dependencies.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.distributed.overload-backpressure-cascade`, đảo thứ tự input và concurrency nhưng giữ logical population. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Overload, backpressure and cascading failure` công bố.

**Bằng chứng cần giữ.** Đối với probe 5 của `Overload, backpressure and cascading failure`, so canonical hash và business totals giữa các thứ tự. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.6. Overload, backpressure and cascading failure: kiểm `Game day` bằng case 6, cụ thể ramp load, slow dependency và kill capacity; đo throughput, tail latency, queues, rejected work, recovery time và correctness

**Mệnh đề cần kiểm.** Overload, backpressure and cascading failure: kiểm `Game day` bằng case 6, cụ thể ramp load, slow dependency và kill capacity; đo throughput, tail latency, queues, rejected work, recovery time và correctness.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.distributed.overload-backpressure-cascade`, replay cùng identity với payload giống rồi payload xung đột. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Overload, backpressure and cascading failure` công bố.

**Bằng chứng cần giữ.** Đối với probe 6 của `Overload, backpressure and cascading failure`, tách duplicate replay khỏi identity collision bằng reason code. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.7. Overload, backpressure and cascading failure: kiểm `Capacity envelope` bằng case 7, cụ thể service có finite cpu, memory, i/o, connections và downstream quota; latency tăng phi tuyến khi utilization sát saturation

**Mệnh đề cần kiểm.** Overload, backpressure and cascading failure: kiểm `Capacity envelope` bằng case 7, cụ thể service có finite cpu, memory, i/o, connections và downstream quota; latency tăng phi tuyến khi utilization sát saturation.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.distributed.overload-backpressure-cascade`, thêm record tới trễ trong horizon và ngoài horizon. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Overload, backpressure and cascading failure` công bố.

**Bằng chứng cần giữ.** Đối với probe 7 của `Overload, backpressure and cascading failure`, báo accepted-late, rejected-late và oldest outstanding timestamp. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.8. Overload, backpressure and cascading failure: kiểm `Queueing` bằng case 8, cụ thể unbounded queue đổi immediate rejection thành memory growth và stale work; queue length cần bound và deadline-aware discard

**Mệnh đề cần kiểm.** Overload, backpressure and cascading failure: kiểm `Queueing` bằng case 8, cụ thể unbounded queue đổi immediate rejection thành memory growth và stale work; queue length cần bound và deadline-aware discard.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.distributed.overload-backpressure-cascade`, đổi schema theo một cách tương thích rồi một cách phá vỡ semantics. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Overload, backpressure and cascading failure` công bố.

**Bằng chứng cần giữ.** Đối với probe 8 của `Overload, backpressure and cascading failure`, giữ schema diff, classification và consumer-visible result. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.9. Overload, backpressure and cascading failure: kiểm `Backpressure` bằng case 9, cụ thể consumer/downstream truyền capacity signal upstream qua demand, credits, lag hoặc blocking; signal chậm vẫn gây overshoot

**Mệnh đề cần kiểm.** Overload, backpressure and cascading failure: kiểm `Backpressure` bằng case 9, cụ thể consumer/downstream truyền capacity signal upstream qua demand, credits, lag hoặc blocking; signal chậm vẫn gây overshoot.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.distributed.overload-backpressure-cascade`, tạo missing và duplicate bù nhau để count tổng không đổi. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Overload, backpressure and cascading failure` công bố.

**Bằng chứng cần giữ.** Đối với probe 9 của `Overload, backpressure and cascading failure`, so key multiset và typed hashes thay vì chỉ row count. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.10. Overload, backpressure and cascading failure: kiểm `Load shedding` bằng case 10, cụ thể reject early theo priority/cost và preserve critical path; retries phải có backoff, jitter, budgets và retryability classification

**Mệnh đề cần kiểm.** Overload, backpressure and cascading failure: kiểm `Load shedding` bằng case 10, cụ thể reject early theo priority/cost và preserve critical path; retries phải có backoff, jitter, budgets và retryability classification.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.distributed.overload-backpressure-cascade`, cho reviewer tái hiện chỉ từ evidence package. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Overload, backpressure and cascading failure` công bố.

**Bằng chứng cần giữ.** Đối với probe 10 của `Overload, backpressure and cascading failure`, package phải đủ để người khác dựng lại decision và limitation. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.11. Overload, backpressure and cascading failure: kiểm `Cascade` bằng case 11, cụ thể timeouts dài, synchronized retries, shared pools và health-check work khuếch đại failure qua dependencies

**Mệnh đề cần kiểm.** Overload, backpressure and cascading failure: kiểm `Cascade` bằng case 11, cụ thể timeouts dài, synchronized retries, shared pools và health-check work khuếch đại failure qua dependencies.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.distributed.overload-backpressure-cascade`, so với oracle độc lập không dùng chung query hoặc parser. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Overload, backpressure and cascading failure` công bố.

**Bằng chứng cần giữ.** Đối với probe 11 của `Overload, backpressure and cascading failure`, independent result phải khớp ở grain đã công bố. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.12. Overload, backpressure and cascading failure: kiểm `Game day` bằng case 12, cụ thể ramp load, slow dependency và kill capacity; đo throughput, tail latency, queues, rejected work, recovery time và correctness

**Mệnh đề cần kiểm.** Overload, backpressure and cascading failure: kiểm `Game day` bằng case 12, cụ thể ramp load, slow dependency và kill capacity; đo throughput, tail latency, queues, rejected work, recovery time và correctness.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.distributed.overload-backpressure-cascade`, chạy scope hẹp và population đầy đủ rồi công bố phần bị loại. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Overload, backpressure and cascading failure` công bố.

**Bằng chứng cần giữ.** Đối với probe 12 của `Overload, backpressure and cascading failure`, coverage phải nêu rõ excluded nodes, partitions hoặc incidents. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.13. Overload, backpressure and cascading failure: kiểm `Capacity envelope` bằng case 13, cụ thể service có finite cpu, memory, i/o, connections và downstream quota; latency tăng phi tuyến khi utilization sát saturation

**Mệnh đề cần kiểm.** Overload, backpressure and cascading failure: kiểm `Capacity envelope` bằng case 13, cụ thể service có finite cpu, memory, i/o, connections và downstream quota; latency tăng phi tuyến khi utilization sát saturation.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.distributed.overload-backpressure-cascade`, thử timezone, precision hoặc partition ở hai phía của ranh giới. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Overload, backpressure and cascading failure` công bố.

**Bằng chứng cần giữ.** Đối với probe 13 của `Overload, backpressure and cascading failure`, UTC/local interval và rounding policy phải hiện trong output. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.14. Overload, backpressure and cascading failure: kiểm `Queueing` bằng case 14, cụ thể unbounded queue đổi immediate rejection thành memory growth và stale work; queue length cần bound và deadline-aware discard

**Mệnh đề cần kiểm.** Overload, backpressure and cascading failure: kiểm `Queueing` bằng case 14, cụ thể unbounded queue đổi immediate rejection thành memory growth và stale work; queue length cần bound và deadline-aware discard.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.distributed.overload-backpressure-cascade`, đổi constraint đủ lớn để quyết định phải đảo. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Overload, backpressure and cascading failure` công bố.

**Bằng chứng cần giữ.** Đối với probe 14 của `Overload, backpressure and cascading failure`, ADR phải lưu changed constraint và reversal threshold. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.15. Overload, backpressure and cascading failure: kiểm `Backpressure` bằng case 15, cụ thể consumer/downstream truyền capacity signal upstream qua demand, credits, lag hoặc blocking; signal chậm vẫn gây overshoot

**Mệnh đề cần kiểm.** Overload, backpressure and cascading failure: kiểm `Backpressure` bằng case 15, cụ thể consumer/downstream truyền capacity signal upstream qua demand, credits, lag hoặc blocking; signal chậm vẫn gây overshoot.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.distributed.overload-backpressure-cascade`, chạy lại từ môi trường sạch với versions và seed đã khóa. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Overload, backpressure and cascading failure` công bố.

**Bằng chứng cần giữ.** Đối với probe 15 của `Overload, backpressure and cascading failure`, canonical result phải ổn định hoặc mọi nondeterminism phải được giải thích. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

## 8. Quy trình phản biện

1. Viết consumer-visible invariant cho `Overload, backpressure and cascading failure` trước khi chọn query hoặc tool.
2. Khóa grain, identity, population, time window và authoritative source.
3. Phân biệt declared configuration, executed state và published state.
4. Chạy negative control, replay hoặc changed-assumption case phù hợp.
5. Đối soát bằng oracle độc lập; công bố coverage và phần không quan sát được.
6. Gắn owner, hành động, reversal trigger và hạn review cho kết luận.

## 9. Câu hỏi tự kiểm tra

1. `Overload, backpressure and cascading failure: kiểm `Capacity envelope` bằng case 1, cụ thể service có finite cpu, memory, i/o, connections và downstream quota; latency tăng phi tuyến khi utilization sát saturation` thất bại đầu tiên ở boundary nào?
2. Artifact nào mạnh nhất để trả lời `Overload, backpressure and cascading failure: kiểm `Backpressure` bằng case 3, cụ thể consumer/downstream truyền capacity signal upstream qua demand, credits, lag hoặc blocking; signal chậm vẫn gây overshoot`?
3. Counterexample nhỏ nhất cho `Overload, backpressure and cascading failure: kiểm `Game day` bằng case 6, cụ thể ramp load, slow dependency và kill capacity; đo throughput, tail latency, queues, rejected work, recovery time và correctness` gồm những state nào?
4. `Overload, backpressure and cascading failure: kiểm `Backpressure` bằng case 9, cụ thể consumer/downstream truyền capacity signal upstream qua demand, credits, lag hoặc blocking; signal chậm vẫn gây overshoot` có thể xanh giả ra sao?
5. Constraint nào khiến quyết định ở `Overload, backpressure and cascading failure: kiểm `Queueing` bằng case 14, cụ thể unbounded queue đổi immediate rejection thành memory growth và stale work; queue length cần bound và deadline-aware discard` phải đảo?
6. Phần nào của `Overload, backpressure and cascading failure: kiểm `Backpressure` bằng case 15, cụ thể consumer/downstream truyền capacity signal upstream qua demand, credits, lag hoặc blocking; signal chậm vẫn gây overshoot` mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `Overload, backpressure and cascading failure` chưa chạy trên hệ thống production; nội dung là giáo trình và expected evidence.
- Hành vi phụ thuộc phiên bản, connector, scheduler, warehouse và catalog configuration phải được kiểm lại.
- Các ma trận, ladder và threshold do giáo trình tổng hợp không được gán nguyên văn cho vendor.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-KLEPPMANN-DDIA-1E]]
2. [[SRC-AWS-TIMEOUTS-RETRIES-BACKOFF]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-KLEPPMANN-DDIA-1E]] | Contract hoặc cơ chế liên quan trực tiếp tới `Overload, backpressure and cascading failure` | Đã đọc locator; cần pin version khi chạy lab |
| [[SRC-AWS-TIMEOUTS-RETRIES-BACKOFF]] | Contract hoặc cơ chế liên quan trực tiếp tới `Overload, backpressure and cascading failure` | Đã đọc locator; cần pin version khi chạy lab |

## Key takeaways
- Bounded queues, backpressure, shedding và retry budgets ngăn cascade.
- Với `wiki.distributed.overload-backpressure-cascade`, quality của kết luận phụ thuộc identity, coverage và oracle chứ không phụ thuộc màu dashboard.
- Câu hỏi `Backpressure và admission control chặn overload biến thành cascading failure bằng cách nào?` chỉ được trả lời trong scope và version đã ghi.
- Các source IDs `src.book.kleppmann-ddia.1e, src.web.aws-timeouts-retries-backoff` đặt ranh giới cho source fact; phần còn lại là synthesis có nhãn.
- Trước khi lab chạy, đây là note đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.
