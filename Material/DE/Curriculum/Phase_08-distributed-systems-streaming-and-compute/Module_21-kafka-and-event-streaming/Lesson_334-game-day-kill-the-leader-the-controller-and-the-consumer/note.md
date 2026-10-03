# Phase 8: Distributed Systems, Streaming and Compute
# Module 21: Kafka and Event Streaming
# Lesson 334: Game day - kill the leader, the controller and the consumer

## Mục tiêu bài học

**Năng lực cần chứng minh.** Chạy tám tình huống với hành vi kỳ vọng viết trước và nộp sổ tay vận hành có bằng chứng đối soát.

**Điều kiện hoàn thành.** ≥ 7/8 tình huống phục hồi với đối soát khớp, ba số đo đầy đủ cho mỗi tình huống, và sổ tay có đủ năm mục bắt buộc.

> [!abstract] Câu hỏi trung tâm
> Game day giết partition leader, controller và consumer chứng minh recovery boundaries nào mà không biến chaos thành phá hoại?

## 1. Hypothesis

Mỗi experiment nêu expected unavailability, data guarantee, alarms, recovery time và stop condition trước injection. Đừng bắt đầu bằng tên công cụ. Hãy bắt đầu bằng đối tượng được bảo vệ, boundary quan sát được và hậu quả nếu kết luận sai. Trong bài `Game day - kill the leader, the controller and the consumer`, câu hỏi thực dụng là: Game day giết partition leader, controller và consumer chứng minh recovery boundaries nào mà không biến chaos thành phá hoại? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 2. Leader loss

Kill partition leader dưới controlled ISR, observe election, producer errors/retries, HW/epochs và acknowledged-record visibility. Điểm khó không nằm ở cú pháp mà ở identity và scope. Hai phép đo cùng tên vẫn có thể nói về hai population hoặc hai thời điểm khác nhau. Trong bài `Game day - kill the leader, the controller and the consumer`, câu hỏi thực dụng là: Game day giết partition leader, controller và consumer chứng minh recovery boundaries nào mà không biến chaos thành phá hoại? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 3. Controller loss

Mất active/minority controller kiểm metadata quorum leadership; không reformat hay tạo cluster identity mới để chữa nhanh. Một dashboard xanh chỉ là tín hiệu. Muốn biến nó thành bằng chứng phải giữ input, phiên bản, rule, trạng thái trước–sau và cách tính độc lập. Trong bài `Game day - kill the leader, the controller and the consumer`, câu hỏi thực dụng là: Game day giết partition leader, controller và consumer chứng minh recovery boundaries nào mà không biến chaos thành phá hoại? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 4. Consumer loss

Kill during processing/commit/rebalance để đo duplicate/loss behavior theo sink idempotency và offset protocol. Thiết kế tốt phải chịu được counterexample. Hãy chủ động tạo case sát boundary, case thiếu dữ liệu và case replay thay vì chỉ chạy happy path. Trong bài `Game day - kill the leader, the controller and the consumer`, câu hỏi thực dụng là: Game day giết partition leader, controller và consumer chứng minh recovery boundaries nào mà không biến chaos thành phá hoại? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 5. Safety controls

Sandbox, backups, bounded blast radius, abort authority và source/destination reconciliation bắt buộc. Chi phí vận hành thuộc contract. Một rule đúng nhưng quá đắt, quá ồn hoặc không có owner sẽ nhanh chóng bị tắt và mất tác dụng. Trong bài `Game day - kill the leader, the controller and the consumer`, câu hỏi thực dụng là: Game day giết partition leader, controller và consumer chứng minh recovery boundaries nào mà không biến chaos thành phá hoại? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 6. Evidence review

Timeline nối injection, metrics, logs, state transitions, consumer outcomes và runbook gaps; green dashboard không thay reconciliation. Kết luận cần có điều kiện đảo chiều. Khi volume, latency, nguồn thẩm quyền hoặc topology đổi, quyết định cũ phải được xem xét lại bằng cùng một oracle. Trong bài `Game day - kill the leader, the controller and the consumer`, câu hỏi thực dụng là: Game day giết partition leader, controller và consumer chứng minh recovery boundaries nào mà không biến chaos thành phá hoại? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 7. Ma trận kiểm chứng từng mệnh đề

Với `wiki.streaming.kafka-game-day`, command thành công không tự chứng minh dữ liệu đúng. Protocol riêng của bài là: Dựng version-pinned fixture, inject compatibility/capacity/failure/change case và đối soát emitted/visible state bằng oracle độc lập. Mỗi probe dưới đây phải nối input boundary với failure signal và oracle có thể phản bác kết luận.

### 7.1. Game day - kill the leader, the controller and the consumer: kiểm `Hypothesis` bằng case 1, cụ thể mỗi experiment nêu expected unavailability, data guarantee, alarms, recovery time và stop condition trước injection

**Mệnh đề cần kiểm.** Game day - kill the leader, the controller and the consumer: kiểm `Hypothesis` bằng case 1, cụ thể mỗi experiment nêu expected unavailability, data guarantee, alarms, recovery time và stop condition trước injection.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-game-day`, tạo positive control và negative control chỉ khác đúng một điều kiện. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Game day - kill the leader, the controller and the consumer` công bố.

**Bằng chứng cần giữ.** Đối với probe 1 của `Game day - kill the leader, the controller and the consumer`, giữ fixture, raw failing rows và lệnh tái hiện. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.2. Game day - kill the leader, the controller and the consumer: kiểm `Leader loss` bằng case 2, cụ thể kill partition leader dưới controlled isr, observe election, producer errors/retries, hw/epochs và acknowledged-record visibility

**Mệnh đề cần kiểm.** Game day - kill the leader, the controller and the consumer: kiểm `Leader loss` bằng case 2, cụ thể kill partition leader dưới controlled isr, observe election, producer errors/retries, hw/epochs và acknowledged-record visibility.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-game-day`, đổi grain nhưng giữ tổng số dòng để lộ phép đo sai cấp. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Game day - kill the leader, the controller and the consumer` công bố.

**Bằng chứng cần giữ.** Đối với probe 2 của `Game day - kill the leader, the controller and the consumer`, báo numerator, denominator và key set ở cả hai grain. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.3. Game day - kill the leader, the controller and the consumer: kiểm `Controller loss` bằng case 3, cụ thể mất active/minority controller kiểm metadata quorum leadership; không reformat hay tạo cluster identity mới để chữa nhanh

**Mệnh đề cần kiểm.** Game day - kill the leader, the controller and the consumer: kiểm `Controller loss` bằng case 3, cụ thể mất active/minority controller kiểm metadata quorum leadership; không reformat hay tạo cluster identity mới để chữa nhanh.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-game-day`, đưa một giá trị tới đúng boundary và một giá trị vượt boundary. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Game day - kill the leader, the controller and the consumer` công bố.

**Bằng chứng cần giữ.** Đối với probe 3 của `Game day - kill the leader, the controller and the consumer`, lưu hai observed values cùng rule đã resolve. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.4. Game day - kill the leader, the controller and the consumer: kiểm `Consumer loss` bằng case 4, cụ thể kill during processing/commit/rebalance để đo duplicate/loss behavior theo sink idempotency và offset protocol

**Mệnh đề cần kiểm.** Game day - kill the leader, the controller and the consumer: kiểm `Consumer loss` bằng case 4, cụ thể kill during processing/commit/rebalance để đo duplicate/loss behavior theo sink idempotency và offset protocol.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-game-day`, kill tiến trình ngay trước rồi ngay sau durable side effect. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Game day - kill the leader, the controller and the consumer` công bố.

**Bằng chứng cần giữ.** Đối với probe 4 của `Game day - kill the leader, the controller and the consumer`, lưu checkpoint, external ledger và trạng thái sau restart. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.5. Game day - kill the leader, the controller and the consumer: kiểm `Safety controls` bằng case 5, cụ thể sandbox, backups, bounded blast radius, abort authority và source/destination reconciliation bắt buộc

**Mệnh đề cần kiểm.** Game day - kill the leader, the controller and the consumer: kiểm `Safety controls` bằng case 5, cụ thể sandbox, backups, bounded blast radius, abort authority và source/destination reconciliation bắt buộc.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-game-day`, đảo thứ tự input và concurrency nhưng giữ logical population. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Game day - kill the leader, the controller and the consumer` công bố.

**Bằng chứng cần giữ.** Đối với probe 5 của `Game day - kill the leader, the controller and the consumer`, so canonical hash và business totals giữa các thứ tự. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.6. Game day - kill the leader, the controller and the consumer: kiểm `Evidence review` bằng case 6, cụ thể timeline nối injection, metrics, logs, state transitions, consumer outcomes và runbook gaps; green dashboard không thay reconciliation

**Mệnh đề cần kiểm.** Game day - kill the leader, the controller and the consumer: kiểm `Evidence review` bằng case 6, cụ thể timeline nối injection, metrics, logs, state transitions, consumer outcomes và runbook gaps; green dashboard không thay reconciliation.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-game-day`, replay cùng identity với payload giống rồi payload xung đột. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Game day - kill the leader, the controller and the consumer` công bố.

**Bằng chứng cần giữ.** Đối với probe 6 của `Game day - kill the leader, the controller and the consumer`, tách duplicate replay khỏi identity collision bằng reason code. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.7. Game day - kill the leader, the controller and the consumer: kiểm `Hypothesis` bằng case 7, cụ thể mỗi experiment nêu expected unavailability, data guarantee, alarms, recovery time và stop condition trước injection

**Mệnh đề cần kiểm.** Game day - kill the leader, the controller and the consumer: kiểm `Hypothesis` bằng case 7, cụ thể mỗi experiment nêu expected unavailability, data guarantee, alarms, recovery time và stop condition trước injection.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-game-day`, thêm record tới trễ trong horizon và ngoài horizon. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Game day - kill the leader, the controller and the consumer` công bố.

**Bằng chứng cần giữ.** Đối với probe 7 của `Game day - kill the leader, the controller and the consumer`, báo accepted-late, rejected-late và oldest outstanding timestamp. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.8. Game day - kill the leader, the controller and the consumer: kiểm `Leader loss` bằng case 8, cụ thể kill partition leader dưới controlled isr, observe election, producer errors/retries, hw/epochs và acknowledged-record visibility

**Mệnh đề cần kiểm.** Game day - kill the leader, the controller and the consumer: kiểm `Leader loss` bằng case 8, cụ thể kill partition leader dưới controlled isr, observe election, producer errors/retries, hw/epochs và acknowledged-record visibility.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-game-day`, đổi schema theo một cách tương thích rồi một cách phá vỡ semantics. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Game day - kill the leader, the controller and the consumer` công bố.

**Bằng chứng cần giữ.** Đối với probe 8 của `Game day - kill the leader, the controller and the consumer`, giữ schema diff, classification và consumer-visible result. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.9. Game day - kill the leader, the controller and the consumer: kiểm `Controller loss` bằng case 9, cụ thể mất active/minority controller kiểm metadata quorum leadership; không reformat hay tạo cluster identity mới để chữa nhanh

**Mệnh đề cần kiểm.** Game day - kill the leader, the controller and the consumer: kiểm `Controller loss` bằng case 9, cụ thể mất active/minority controller kiểm metadata quorum leadership; không reformat hay tạo cluster identity mới để chữa nhanh.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-game-day`, tạo missing và duplicate bù nhau để count tổng không đổi. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Game day - kill the leader, the controller and the consumer` công bố.

**Bằng chứng cần giữ.** Đối với probe 9 của `Game day - kill the leader, the controller and the consumer`, so key multiset và typed hashes thay vì chỉ row count. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.10. Game day - kill the leader, the controller and the consumer: kiểm `Consumer loss` bằng case 10, cụ thể kill during processing/commit/rebalance để đo duplicate/loss behavior theo sink idempotency và offset protocol

**Mệnh đề cần kiểm.** Game day - kill the leader, the controller and the consumer: kiểm `Consumer loss` bằng case 10, cụ thể kill during processing/commit/rebalance để đo duplicate/loss behavior theo sink idempotency và offset protocol.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-game-day`, cho reviewer tái hiện chỉ từ evidence package. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Game day - kill the leader, the controller and the consumer` công bố.

**Bằng chứng cần giữ.** Đối với probe 10 của `Game day - kill the leader, the controller and the consumer`, package phải đủ để người khác dựng lại decision và limitation. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.11. Game day - kill the leader, the controller and the consumer: kiểm `Safety controls` bằng case 11, cụ thể sandbox, backups, bounded blast radius, abort authority và source/destination reconciliation bắt buộc

**Mệnh đề cần kiểm.** Game day - kill the leader, the controller and the consumer: kiểm `Safety controls` bằng case 11, cụ thể sandbox, backups, bounded blast radius, abort authority và source/destination reconciliation bắt buộc.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-game-day`, so với oracle độc lập không dùng chung query hoặc parser. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Game day - kill the leader, the controller and the consumer` công bố.

**Bằng chứng cần giữ.** Đối với probe 11 của `Game day - kill the leader, the controller and the consumer`, independent result phải khớp ở grain đã công bố. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.12. Game day - kill the leader, the controller and the consumer: kiểm `Evidence review` bằng case 12, cụ thể timeline nối injection, metrics, logs, state transitions, consumer outcomes và runbook gaps; green dashboard không thay reconciliation

**Mệnh đề cần kiểm.** Game day - kill the leader, the controller and the consumer: kiểm `Evidence review` bằng case 12, cụ thể timeline nối injection, metrics, logs, state transitions, consumer outcomes và runbook gaps; green dashboard không thay reconciliation.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-game-day`, chạy scope hẹp và population đầy đủ rồi công bố phần bị loại. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Game day - kill the leader, the controller and the consumer` công bố.

**Bằng chứng cần giữ.** Đối với probe 12 của `Game day - kill the leader, the controller and the consumer`, coverage phải nêu rõ excluded nodes, partitions hoặc incidents. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.13. Game day - kill the leader, the controller and the consumer: kiểm `Hypothesis` bằng case 13, cụ thể mỗi experiment nêu expected unavailability, data guarantee, alarms, recovery time và stop condition trước injection

**Mệnh đề cần kiểm.** Game day - kill the leader, the controller and the consumer: kiểm `Hypothesis` bằng case 13, cụ thể mỗi experiment nêu expected unavailability, data guarantee, alarms, recovery time và stop condition trước injection.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-game-day`, thử timezone, precision hoặc partition ở hai phía của ranh giới. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Game day - kill the leader, the controller and the consumer` công bố.

**Bằng chứng cần giữ.** Đối với probe 13 của `Game day - kill the leader, the controller and the consumer`, UTC/local interval và rounding policy phải hiện trong output. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.14. Game day - kill the leader, the controller and the consumer: kiểm `Leader loss` bằng case 14, cụ thể kill partition leader dưới controlled isr, observe election, producer errors/retries, hw/epochs và acknowledged-record visibility

**Mệnh đề cần kiểm.** Game day - kill the leader, the controller and the consumer: kiểm `Leader loss` bằng case 14, cụ thể kill partition leader dưới controlled isr, observe election, producer errors/retries, hw/epochs và acknowledged-record visibility.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-game-day`, đổi constraint đủ lớn để quyết định phải đảo. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Game day - kill the leader, the controller and the consumer` công bố.

**Bằng chứng cần giữ.** Đối với probe 14 của `Game day - kill the leader, the controller and the consumer`, ADR phải lưu changed constraint và reversal threshold. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.15. Game day - kill the leader, the controller and the consumer: kiểm `Controller loss` bằng case 15, cụ thể mất active/minority controller kiểm metadata quorum leadership; không reformat hay tạo cluster identity mới để chữa nhanh

**Mệnh đề cần kiểm.** Game day - kill the leader, the controller and the consumer: kiểm `Controller loss` bằng case 15, cụ thể mất active/minority controller kiểm metadata quorum leadership; không reformat hay tạo cluster identity mới để chữa nhanh.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-game-day`, chạy lại từ môi trường sạch với versions và seed đã khóa. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Game day - kill the leader, the controller and the consumer` công bố.

**Bằng chứng cần giữ.** Đối với probe 15 của `Game day - kill the leader, the controller and the consumer`, canonical result phải ổn định hoặc mọi nondeterminism phải được giải thích. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

## 8. Quy trình phản biện

1. Viết consumer-visible invariant cho `Game day - kill the leader, the controller and the consumer` trước khi chọn query hoặc tool.
2. Khóa grain, identity, population, time window và authoritative source.
3. Phân biệt declared configuration, executed state và published state.
4. Chạy negative control, replay hoặc changed-assumption case phù hợp.
5. Đối soát bằng oracle độc lập; công bố coverage và phần không quan sát được.
6. Gắn owner, hành động, reversal trigger và hạn review cho kết luận.

## 9. Câu hỏi tự kiểm tra

1. `Game day - kill the leader, the controller and the consumer: kiểm `Hypothesis` bằng case 1, cụ thể mỗi experiment nêu expected unavailability, data guarantee, alarms, recovery time và stop condition trước injection` thất bại đầu tiên ở boundary nào?
2. Artifact nào mạnh nhất để trả lời `Game day - kill the leader, the controller and the consumer: kiểm `Controller loss` bằng case 3, cụ thể mất active/minority controller kiểm metadata quorum leadership; không reformat hay tạo cluster identity mới để chữa nhanh`?
3. Counterexample nhỏ nhất cho `Game day - kill the leader, the controller and the consumer: kiểm `Evidence review` bằng case 6, cụ thể timeline nối injection, metrics, logs, state transitions, consumer outcomes và runbook gaps; green dashboard không thay reconciliation` gồm những state nào?
4. `Game day - kill the leader, the controller and the consumer: kiểm `Controller loss` bằng case 9, cụ thể mất active/minority controller kiểm metadata quorum leadership; không reformat hay tạo cluster identity mới để chữa nhanh` có thể xanh giả ra sao?
5. Constraint nào khiến quyết định ở `Game day - kill the leader, the controller and the consumer: kiểm `Leader loss` bằng case 14, cụ thể kill partition leader dưới controlled isr, observe election, producer errors/retries, hw/epochs và acknowledged-record visibility` phải đảo?
6. Phần nào của `Game day - kill the leader, the controller and the consumer: kiểm `Controller loss` bằng case 15, cụ thể mất active/minority controller kiểm metadata quorum leadership; không reformat hay tạo cluster identity mới để chữa nhanh` mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `Game day - kill the leader, the controller and the consumer` chưa chạy trên hệ thống production; nội dung là giáo trình và expected evidence.
- Hành vi phụ thuộc phiên bản, connector, scheduler, warehouse và catalog configuration phải được kiểm lại.
- Các ma trận, ladder và threshold do giáo trình tổng hợp không được gán nguyên văn cho vendor.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-APACHE-KAFKA-DESIGN]]
2. [[SRC-APACHE-KAFKA-KRAFT]]
3. [[SRC-APACHE-KAFKA-CONSUMER-CONFIG]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-APACHE-KAFKA-DESIGN]] | Contract hoặc cơ chế liên quan trực tiếp tới `Game day - kill the leader, the controller and the consumer` | Đã đọc locator; cần pin version khi chạy lab |
| [[SRC-APACHE-KAFKA-KRAFT]] | Contract hoặc cơ chế liên quan trực tiếp tới `Game day - kill the leader, the controller and the consumer` | Đã đọc locator; cần pin version khi chạy lab |
| [[SRC-APACHE-KAFKA-CONSUMER-CONFIG]] | Contract hoặc cơ chế liên quan trực tiếp tới `Game day - kill the leader, the controller and the consumer` | Đã đọc locator; cần pin version khi chạy lab |

## Key takeaways
- Game day bắt đầu từ hypothesis/stop condition và kết thúc bằng reconciliation.
- Với `wiki.streaming.kafka-game-day`, quality của kết luận phụ thuộc identity, coverage và oracle chứ không phụ thuộc màu dashboard.
- Câu hỏi `Game day giết partition leader, controller và consumer chứng minh recovery boundaries nào mà không biến chaos thành phá hoại?` chỉ được trả lời trong scope và version đã ghi.
- Các source IDs `src.web.apache-kafka-design, src.web.apache-kafka-kraft, src.web.apache-kafka-consumer-config` đặt ranh giới cho source fact; phần còn lại là synthesis có nhãn.
- Trước khi lab chạy, đây là note đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.
