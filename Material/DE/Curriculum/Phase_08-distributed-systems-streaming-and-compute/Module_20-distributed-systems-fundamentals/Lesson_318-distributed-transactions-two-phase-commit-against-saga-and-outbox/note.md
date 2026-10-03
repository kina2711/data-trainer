# Phase 8: Distributed Systems, Streaming and Compute
# Module 20: Distributed Systems Fundamentals
# Lesson 318: Distributed transactions - two-phase commit against saga and outbox

## Mục tiêu bài học

**Năng lực cần chứng minh.** So ba cách trên cùng bài toán và lập ma trận hỏng tại mọi ranh giới cho từng cách.

**Điều kiện hoàn thành.** Ma trận hỏng đầy đủ cho cả ba cách tại mọi ranh giới, ca điều phối viên chết được tái hiện kèm thời gian khoá đo được.

> [!abstract] Câu hỏi trung tâm
> Chọn 2PC, saga hay transactional outbox theo atomicity boundary, blocking, compensation và delivery semantics ra sao?

## 1. Two-phase commit

Prepare rồi commit/abort phối hợp participants, nhưng coordinator/participant recovery và locks tạo blocking/availability costs. Đừng bắt đầu bằng tên công cụ. Hãy bắt đầu bằng đối tượng được bảo vệ, boundary quan sát được và hậu quả nếu kết luận sai. Trong bài `Distributed transactions - two-phase commit against saga and outbox`, câu hỏi thực dụng là: Chọn 2PC, saga hay transactional outbox theo atomicity boundary, blocking, compensation và delivery semantics ra sao? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 2. Saga

Chuỗi local transactions với compensations chấp nhận intermediate visibility; compensation là business action, không phải undo hoàn hảo. Điểm khó không nằm ở cú pháp mà ở identity và scope. Hai phép đo cùng tên vẫn có thể nói về hai population hoặc hai thời điểm khác nhau. Trong bài `Distributed transactions - two-phase commit against saga and outbox`, câu hỏi thực dụng là: Chọn 2PC, saga hay transactional outbox theo atomicity boundary, blocking, compensation và delivery semantics ra sao? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 3. Transactional outbox

Domain state và outbox row cùng local transaction; relay at-least-once nên consumer vẫn cần dedup/idempotency. Một dashboard xanh chỉ là tín hiệu. Muốn biến nó thành bằng chứng phải giữ input, phiên bản, rule, trạng thái trước–sau và cách tính độc lập. Trong bài `Distributed transactions - two-phase commit against saga and outbox`, câu hỏi thực dụng là: Chọn 2PC, saga hay transactional outbox theo atomicity boundary, blocking, compensation và delivery semantics ra sao? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 4. Decision matrix

Cross-resource invariant, isolation need, participant support, latency, failure recovery và business reversibility quyết định pattern. Thiết kế tốt phải chịu được counterexample. Hãy chủ động tạo case sát boundary, case thiếu dữ liệu và case replay thay vì chỉ chạy happy path. Trong bài `Distributed transactions - two-phase commit against saga and outbox`, câu hỏi thực dụng là: Chọn 2PC, saga hay transactional outbox theo atomicity boundary, blocking, compensation và delivery semantics ra sao? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 5. Failure windows

Kill coordinator, relay và consumer trước/sau durable commits để thấy prepared, duplicate, partial compensation và poison message states. Chi phí vận hành thuộc contract. Một rule đúng nhưng quá đắt, quá ồn hoặc không có owner sẽ nhanh chóng bị tắt và mất tác dụng. Trong bài `Distributed transactions - two-phase commit against saga and outbox`, câu hỏi thực dụng là: Chọn 2PC, saga hay transactional outbox theo atomicity boundary, blocking, compensation và delivery semantics ra sao? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 6. Evidence

Lưu operation ID, participant/outbox states, delivery ledger, compensation result và reconciliation tới final business invariant. Kết luận cần có điều kiện đảo chiều. Khi volume, latency, nguồn thẩm quyền hoặc topology đổi, quyết định cũ phải được xem xét lại bằng cùng một oracle. Trong bài `Distributed transactions - two-phase commit against saga and outbox`, câu hỏi thực dụng là: Chọn 2PC, saga hay transactional outbox theo atomicity boundary, blocking, compensation và delivery semantics ra sao? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 7. Ma trận kiểm chứng từng mệnh đề

Với `wiki.distributed.2pc-saga-outbox`, command thành công không tự chứng minh dữ liệu đúng. Protocol riêng của bài là: Chạy bounded state/history fixture với deterministic fault schedule và kiểm counterexample bằng independent state-machine oracle. Mỗi probe dưới đây phải nối input boundary với failure signal và oracle có thể phản bác kết luận.

### 7.1. Distributed transactions - two-phase commit against saga and outbox: kiểm `Two-phase commit` bằng case 1, cụ thể prepare rồi commit/abort phối hợp participants, nhưng coordinator/participant recovery và locks tạo blocking/availability costs

**Mệnh đề cần kiểm.** Distributed transactions - two-phase commit against saga and outbox: kiểm `Two-phase commit` bằng case 1, cụ thể prepare rồi commit/abort phối hợp participants, nhưng coordinator/participant recovery và locks tạo blocking/availability costs.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.distributed.2pc-saga-outbox`, tạo positive control và negative control chỉ khác đúng một điều kiện. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Distributed transactions - two-phase commit against saga and outbox` công bố.

**Bằng chứng cần giữ.** Đối với probe 1 của `Distributed transactions - two-phase commit against saga and outbox`, giữ fixture, raw failing rows và lệnh tái hiện. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.2. Distributed transactions - two-phase commit against saga and outbox: kiểm `Saga` bằng case 2, cụ thể chuỗi local transactions với compensations chấp nhận intermediate visibility; compensation là business action, không phải undo hoàn hảo

**Mệnh đề cần kiểm.** Distributed transactions - two-phase commit against saga and outbox: kiểm `Saga` bằng case 2, cụ thể chuỗi local transactions với compensations chấp nhận intermediate visibility; compensation là business action, không phải undo hoàn hảo.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.distributed.2pc-saga-outbox`, đổi grain nhưng giữ tổng số dòng để lộ phép đo sai cấp. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Distributed transactions - two-phase commit against saga and outbox` công bố.

**Bằng chứng cần giữ.** Đối với probe 2 của `Distributed transactions - two-phase commit against saga and outbox`, báo numerator, denominator và key set ở cả hai grain. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.3. Distributed transactions - two-phase commit against saga and outbox: kiểm `Transactional outbox` bằng case 3, cụ thể domain state và outbox row cùng local transaction; relay at-least-once nên consumer vẫn cần dedup/idempotency

**Mệnh đề cần kiểm.** Distributed transactions - two-phase commit against saga and outbox: kiểm `Transactional outbox` bằng case 3, cụ thể domain state và outbox row cùng local transaction; relay at-least-once nên consumer vẫn cần dedup/idempotency.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.distributed.2pc-saga-outbox`, đưa một giá trị tới đúng boundary và một giá trị vượt boundary. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Distributed transactions - two-phase commit against saga and outbox` công bố.

**Bằng chứng cần giữ.** Đối với probe 3 của `Distributed transactions - two-phase commit against saga and outbox`, lưu hai observed values cùng rule đã resolve. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.4. Distributed transactions - two-phase commit against saga and outbox: kiểm `Decision matrix` bằng case 4, cụ thể cross-resource invariant, isolation need, participant support, latency, failure recovery và business reversibility quyết định pattern

**Mệnh đề cần kiểm.** Distributed transactions - two-phase commit against saga and outbox: kiểm `Decision matrix` bằng case 4, cụ thể cross-resource invariant, isolation need, participant support, latency, failure recovery và business reversibility quyết định pattern.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.distributed.2pc-saga-outbox`, kill tiến trình ngay trước rồi ngay sau durable side effect. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Distributed transactions - two-phase commit against saga and outbox` công bố.

**Bằng chứng cần giữ.** Đối với probe 4 của `Distributed transactions - two-phase commit against saga and outbox`, lưu checkpoint, external ledger và trạng thái sau restart. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.5. Distributed transactions - two-phase commit against saga and outbox: kiểm `Failure windows` bằng case 5, cụ thể kill coordinator, relay và consumer trước/sau durable commits để thấy prepared, duplicate, partial compensation và poison message states

**Mệnh đề cần kiểm.** Distributed transactions - two-phase commit against saga and outbox: kiểm `Failure windows` bằng case 5, cụ thể kill coordinator, relay và consumer trước/sau durable commits để thấy prepared, duplicate, partial compensation và poison message states.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.distributed.2pc-saga-outbox`, đảo thứ tự input và concurrency nhưng giữ logical population. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Distributed transactions - two-phase commit against saga and outbox` công bố.

**Bằng chứng cần giữ.** Đối với probe 5 của `Distributed transactions - two-phase commit against saga and outbox`, so canonical hash và business totals giữa các thứ tự. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.6. Distributed transactions - two-phase commit against saga and outbox: kiểm `Evidence` bằng case 6, cụ thể lưu operation id, participant/outbox states, delivery ledger, compensation result và reconciliation tới final business invariant

**Mệnh đề cần kiểm.** Distributed transactions - two-phase commit against saga and outbox: kiểm `Evidence` bằng case 6, cụ thể lưu operation id, participant/outbox states, delivery ledger, compensation result và reconciliation tới final business invariant.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.distributed.2pc-saga-outbox`, replay cùng identity với payload giống rồi payload xung đột. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Distributed transactions - two-phase commit against saga and outbox` công bố.

**Bằng chứng cần giữ.** Đối với probe 6 của `Distributed transactions - two-phase commit against saga and outbox`, tách duplicate replay khỏi identity collision bằng reason code. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.7. Distributed transactions - two-phase commit against saga and outbox: kiểm `Two-phase commit` bằng case 7, cụ thể prepare rồi commit/abort phối hợp participants, nhưng coordinator/participant recovery và locks tạo blocking/availability costs

**Mệnh đề cần kiểm.** Distributed transactions - two-phase commit against saga and outbox: kiểm `Two-phase commit` bằng case 7, cụ thể prepare rồi commit/abort phối hợp participants, nhưng coordinator/participant recovery và locks tạo blocking/availability costs.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.distributed.2pc-saga-outbox`, thêm record tới trễ trong horizon và ngoài horizon. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Distributed transactions - two-phase commit against saga and outbox` công bố.

**Bằng chứng cần giữ.** Đối với probe 7 của `Distributed transactions - two-phase commit against saga and outbox`, báo accepted-late, rejected-late và oldest outstanding timestamp. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.8. Distributed transactions - two-phase commit against saga and outbox: kiểm `Saga` bằng case 8, cụ thể chuỗi local transactions với compensations chấp nhận intermediate visibility; compensation là business action, không phải undo hoàn hảo

**Mệnh đề cần kiểm.** Distributed transactions - two-phase commit against saga and outbox: kiểm `Saga` bằng case 8, cụ thể chuỗi local transactions với compensations chấp nhận intermediate visibility; compensation là business action, không phải undo hoàn hảo.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.distributed.2pc-saga-outbox`, đổi schema theo một cách tương thích rồi một cách phá vỡ semantics. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Distributed transactions - two-phase commit against saga and outbox` công bố.

**Bằng chứng cần giữ.** Đối với probe 8 của `Distributed transactions - two-phase commit against saga and outbox`, giữ schema diff, classification và consumer-visible result. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.9. Distributed transactions - two-phase commit against saga and outbox: kiểm `Transactional outbox` bằng case 9, cụ thể domain state và outbox row cùng local transaction; relay at-least-once nên consumer vẫn cần dedup/idempotency

**Mệnh đề cần kiểm.** Distributed transactions - two-phase commit against saga and outbox: kiểm `Transactional outbox` bằng case 9, cụ thể domain state và outbox row cùng local transaction; relay at-least-once nên consumer vẫn cần dedup/idempotency.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.distributed.2pc-saga-outbox`, tạo missing và duplicate bù nhau để count tổng không đổi. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Distributed transactions - two-phase commit against saga and outbox` công bố.

**Bằng chứng cần giữ.** Đối với probe 9 của `Distributed transactions - two-phase commit against saga and outbox`, so key multiset và typed hashes thay vì chỉ row count. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.10. Distributed transactions - two-phase commit against saga and outbox: kiểm `Decision matrix` bằng case 10, cụ thể cross-resource invariant, isolation need, participant support, latency, failure recovery và business reversibility quyết định pattern

**Mệnh đề cần kiểm.** Distributed transactions - two-phase commit against saga and outbox: kiểm `Decision matrix` bằng case 10, cụ thể cross-resource invariant, isolation need, participant support, latency, failure recovery và business reversibility quyết định pattern.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.distributed.2pc-saga-outbox`, cho reviewer tái hiện chỉ từ evidence package. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Distributed transactions - two-phase commit against saga and outbox` công bố.

**Bằng chứng cần giữ.** Đối với probe 10 của `Distributed transactions - two-phase commit against saga and outbox`, package phải đủ để người khác dựng lại decision và limitation. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.11. Distributed transactions - two-phase commit against saga and outbox: kiểm `Failure windows` bằng case 11, cụ thể kill coordinator, relay và consumer trước/sau durable commits để thấy prepared, duplicate, partial compensation và poison message states

**Mệnh đề cần kiểm.** Distributed transactions - two-phase commit against saga and outbox: kiểm `Failure windows` bằng case 11, cụ thể kill coordinator, relay và consumer trước/sau durable commits để thấy prepared, duplicate, partial compensation và poison message states.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.distributed.2pc-saga-outbox`, so với oracle độc lập không dùng chung query hoặc parser. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Distributed transactions - two-phase commit against saga and outbox` công bố.

**Bằng chứng cần giữ.** Đối với probe 11 của `Distributed transactions - two-phase commit against saga and outbox`, independent result phải khớp ở grain đã công bố. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.12. Distributed transactions - two-phase commit against saga and outbox: kiểm `Evidence` bằng case 12, cụ thể lưu operation id, participant/outbox states, delivery ledger, compensation result và reconciliation tới final business invariant

**Mệnh đề cần kiểm.** Distributed transactions - two-phase commit against saga and outbox: kiểm `Evidence` bằng case 12, cụ thể lưu operation id, participant/outbox states, delivery ledger, compensation result và reconciliation tới final business invariant.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.distributed.2pc-saga-outbox`, chạy scope hẹp và population đầy đủ rồi công bố phần bị loại. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Distributed transactions - two-phase commit against saga and outbox` công bố.

**Bằng chứng cần giữ.** Đối với probe 12 của `Distributed transactions - two-phase commit against saga and outbox`, coverage phải nêu rõ excluded nodes, partitions hoặc incidents. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.13. Distributed transactions - two-phase commit against saga and outbox: kiểm `Two-phase commit` bằng case 13, cụ thể prepare rồi commit/abort phối hợp participants, nhưng coordinator/participant recovery và locks tạo blocking/availability costs

**Mệnh đề cần kiểm.** Distributed transactions - two-phase commit against saga and outbox: kiểm `Two-phase commit` bằng case 13, cụ thể prepare rồi commit/abort phối hợp participants, nhưng coordinator/participant recovery và locks tạo blocking/availability costs.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.distributed.2pc-saga-outbox`, thử timezone, precision hoặc partition ở hai phía của ranh giới. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Distributed transactions - two-phase commit against saga and outbox` công bố.

**Bằng chứng cần giữ.** Đối với probe 13 của `Distributed transactions - two-phase commit against saga and outbox`, UTC/local interval và rounding policy phải hiện trong output. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.14. Distributed transactions - two-phase commit against saga and outbox: kiểm `Saga` bằng case 14, cụ thể chuỗi local transactions với compensations chấp nhận intermediate visibility; compensation là business action, không phải undo hoàn hảo

**Mệnh đề cần kiểm.** Distributed transactions - two-phase commit against saga and outbox: kiểm `Saga` bằng case 14, cụ thể chuỗi local transactions với compensations chấp nhận intermediate visibility; compensation là business action, không phải undo hoàn hảo.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.distributed.2pc-saga-outbox`, đổi constraint đủ lớn để quyết định phải đảo. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Distributed transactions - two-phase commit against saga and outbox` công bố.

**Bằng chứng cần giữ.** Đối với probe 14 của `Distributed transactions - two-phase commit against saga and outbox`, ADR phải lưu changed constraint và reversal threshold. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.15. Distributed transactions - two-phase commit against saga and outbox: kiểm `Transactional outbox` bằng case 15, cụ thể domain state và outbox row cùng local transaction; relay at-least-once nên consumer vẫn cần dedup/idempotency

**Mệnh đề cần kiểm.** Distributed transactions - two-phase commit against saga and outbox: kiểm `Transactional outbox` bằng case 15, cụ thể domain state và outbox row cùng local transaction; relay at-least-once nên consumer vẫn cần dedup/idempotency.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.distributed.2pc-saga-outbox`, chạy lại từ môi trường sạch với versions và seed đã khóa. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Distributed transactions - two-phase commit against saga and outbox` công bố.

**Bằng chứng cần giữ.** Đối với probe 15 của `Distributed transactions - two-phase commit against saga and outbox`, canonical result phải ổn định hoặc mọi nondeterminism phải được giải thích. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

## 8. Quy trình phản biện

1. Viết consumer-visible invariant cho `Distributed transactions - two-phase commit against saga and outbox` trước khi chọn query hoặc tool.
2. Khóa grain, identity, population, time window và authoritative source.
3. Phân biệt declared configuration, executed state và published state.
4. Chạy negative control, replay hoặc changed-assumption case phù hợp.
5. Đối soát bằng oracle độc lập; công bố coverage và phần không quan sát được.
6. Gắn owner, hành động, reversal trigger và hạn review cho kết luận.

## 9. Câu hỏi tự kiểm tra

1. `Distributed transactions - two-phase commit against saga and outbox: kiểm `Two-phase commit` bằng case 1, cụ thể prepare rồi commit/abort phối hợp participants, nhưng coordinator/participant recovery và locks tạo blocking/availability costs` thất bại đầu tiên ở boundary nào?
2. Artifact nào mạnh nhất để trả lời `Distributed transactions - two-phase commit against saga and outbox: kiểm `Transactional outbox` bằng case 3, cụ thể domain state và outbox row cùng local transaction; relay at-least-once nên consumer vẫn cần dedup/idempotency`?
3. Counterexample nhỏ nhất cho `Distributed transactions - two-phase commit against saga and outbox: kiểm `Evidence` bằng case 6, cụ thể lưu operation id, participant/outbox states, delivery ledger, compensation result và reconciliation tới final business invariant` gồm những state nào?
4. `Distributed transactions - two-phase commit against saga and outbox: kiểm `Transactional outbox` bằng case 9, cụ thể domain state và outbox row cùng local transaction; relay at-least-once nên consumer vẫn cần dedup/idempotency` có thể xanh giả ra sao?
5. Constraint nào khiến quyết định ở `Distributed transactions - two-phase commit against saga and outbox: kiểm `Saga` bằng case 14, cụ thể chuỗi local transactions với compensations chấp nhận intermediate visibility; compensation là business action, không phải undo hoàn hảo` phải đảo?
6. Phần nào của `Distributed transactions - two-phase commit against saga and outbox: kiểm `Transactional outbox` bằng case 15, cụ thể domain state và outbox row cùng local transaction; relay at-least-once nên consumer vẫn cần dedup/idempotency` mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `Distributed transactions - two-phase commit against saga and outbox` chưa chạy trên hệ thống production; nội dung là giáo trình và expected evidence.
- Hành vi phụ thuộc phiên bản, connector, scheduler, warehouse và catalog configuration phải được kiểm lại.
- Các ma trận, ladder và threshold do giáo trình tổng hợp không được gán nguyên văn cho vendor.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-KLEPPMANN-DDIA-1E]]
2. [[SRC-MICROSERVICES-IO-TRANSACTIONAL-OUTBOX]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-KLEPPMANN-DDIA-1E]] | Contract hoặc cơ chế liên quan trực tiếp tới `Distributed transactions - two-phase commit against saga and outbox` | Đã đọc locator; cần pin version khi chạy lab |
| [[SRC-MICROSERVICES-IO-TRANSACTIONAL-OUTBOX]] | Contract hoặc cơ chế liên quan trực tiếp tới `Distributed transactions - two-phase commit against saga and outbox` | Đã đọc locator; cần pin version khi chạy lab |

## Key takeaways
- 2PC, saga và outbox bảo vệ boundaries khác nhau; không pattern nào tạo atomicity miễn phí.
- Với `wiki.distributed.2pc-saga-outbox`, quality của kết luận phụ thuộc identity, coverage và oracle chứ không phụ thuộc màu dashboard.
- Câu hỏi `Chọn 2PC, saga hay transactional outbox theo atomicity boundary, blocking, compensation và delivery semantics ra sao?` chỉ được trả lời trong scope và version đã ghi.
- Các source IDs `src.book.kleppmann-ddia.1e, src.web.microservices-io-transactional-outbox` đặt ranh giới cho source fact; phần còn lại là synthesis có nhãn.
- Trước khi lab chạy, đây là note đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.
