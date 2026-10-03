# Phase 8: Distributed Systems, Streaming and Compute
# Module 21: Kafka and Event Streaming
# Lesson 328: Offset commit - the two failure windows

## Mục tiêu bài học

**Năng lực cần chứng minh.** Tái hiện cả hai cửa sổ hỏng bằng thực nghiệm và chọn một cửa sổ rồi bù bằng đích luỹ đẳng.

**Điều kiện hoàn thành.** Hai cửa sổ hỏng có số đo mất và trùng qua 100 lần giết, và bản có đích luỹ đẳng đưa số trùng quan sát được về không.

> [!abstract] Câu hỏi trung tâm
> Hai thứ tự process–commit offset tạo duplicate hoặc loss window ra sao, và state coupling sửa được gì?

## 1. Commit meaning

Committed offset là next position group sẽ resume, không phải bằng chứng external side effect completed. Đừng bắt đầu bằng tên công cụ. Hãy bắt đầu bằng đối tượng được bảo vệ, boundary quan sát được và hậu quả nếu kết luận sai. Trong bài `Offset commit - the two failure windows`, câu hỏi thực dụng là: Hai thứ tự process–commit offset tạo duplicate hoặc loss window ra sao, và state coupling sửa được gì? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 2. Process then commit

Crash sau side effect trước commit gây replay/duplicate; idempotent sink hoặc dedup ledger hấp thụ. Điểm khó không nằm ở cú pháp mà ở identity và scope. Hai phép đo cùng tên vẫn có thể nói về hai population hoặc hai thời điểm khác nhau. Trong bài `Offset commit - the two failure windows`, câu hỏi thực dụng là: Hai thứ tự process–commit offset tạo duplicate hoặc loss window ra sao, và state coupling sửa được gì? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 3. Commit then process

Crash sau commit trước side effect gây skipped/lost outcome; thường không chấp nhận cho at-least-once processing. Một dashboard xanh chỉ là tín hiệu. Muốn biến nó thành bằng chứng phải giữ input, phiên bản, rule, trạng thái trước–sau và cách tính độc lập. Trong bài `Offset commit - the two failure windows`, câu hỏi thực dụng là: Hai thứ tự process–commit offset tạo duplicate hoặc loss window ra sao, và state coupling sửa được gì? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 4. Batch granularity

Commit highest safely completed contiguous offset; parallel processing có holes nên max-seen commit nguy hiểm. Thiết kế tốt phải chịu được counterexample. Hãy chủ động tạo case sát boundary, case thiếu dữ liệu và case replay thay vì chỉ chạy happy path. Trong bài `Offset commit - the two failure windows`, câu hỏi thực dụng là: Hai thứ tự process–commit offset tạo duplicate hoặc loss window ra sao, và state coupling sửa được gì? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 5. Atomic coupling

Kafka transaction couple output+offset trong Kafka; external sink cần local transaction/outbox/checkpoint protocol riêng. Chi phí vận hành thuộc contract. Một rule đúng nhưng quá đắt, quá ồn hoặc không có owner sẽ nhanh chóng bị tắt và mất tác dụng. Trong bài `Offset commit - the two failure windows`, câu hỏi thực dụng là: Hai thứ tự process–commit offset tạo duplicate hoặc loss window ra sao, và state coupling sửa được gì? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 6. Kill-point proof

Crash tại từng boundary, restart with rebalance and compare source offsets, sink keys, duplicates and missing outcomes. Kết luận cần có điều kiện đảo chiều. Khi volume, latency, nguồn thẩm quyền hoặc topology đổi, quyết định cũ phải được xem xét lại bằng cùng một oracle. Trong bài `Offset commit - the two failure windows`, câu hỏi thực dụng là: Hai thứ tự process–commit offset tạo duplicate hoặc loss window ra sao, và state coupling sửa được gì? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 7. Ma trận kiểm chứng từng mệnh đề

Với `wiki.streaming.kafka-offset-commit-failure-windows`, command thành công không tự chứng minh dữ liệu đúng. Protocol riêng của bài là: Chạy Kafka 4.2-compatible sandbox hoặc protocol fixture, inject precise kill/failover point and compare visible records, offsets or metadata state. Mỗi probe dưới đây phải nối input boundary với failure signal và oracle có thể phản bác kết luận.

### 7.1. Offset commit - the two failure windows: kiểm `Commit meaning` bằng case 1, cụ thể committed offset là next position group sẽ resume, không phải bằng chứng external side effect completed

**Mệnh đề cần kiểm.** Offset commit - the two failure windows: kiểm `Commit meaning` bằng case 1, cụ thể committed offset là next position group sẽ resume, không phải bằng chứng external side effect completed.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-offset-commit-failure-windows`, tạo positive control và negative control chỉ khác đúng một điều kiện. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Offset commit - the two failure windows` công bố.

**Bằng chứng cần giữ.** Đối với probe 1 của `Offset commit - the two failure windows`, giữ fixture, raw failing rows và lệnh tái hiện. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.2. Offset commit - the two failure windows: kiểm `Process then commit` bằng case 2, cụ thể crash sau side effect trước commit gây replay/duplicate; idempotent sink hoặc dedup ledger hấp thụ

**Mệnh đề cần kiểm.** Offset commit - the two failure windows: kiểm `Process then commit` bằng case 2, cụ thể crash sau side effect trước commit gây replay/duplicate; idempotent sink hoặc dedup ledger hấp thụ.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-offset-commit-failure-windows`, đổi grain nhưng giữ tổng số dòng để lộ phép đo sai cấp. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Offset commit - the two failure windows` công bố.

**Bằng chứng cần giữ.** Đối với probe 2 của `Offset commit - the two failure windows`, báo numerator, denominator và key set ở cả hai grain. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.3. Offset commit - the two failure windows: kiểm `Commit then process` bằng case 3, cụ thể crash sau commit trước side effect gây skipped/lost outcome; thường không chấp nhận cho at-least-once processing

**Mệnh đề cần kiểm.** Offset commit - the two failure windows: kiểm `Commit then process` bằng case 3, cụ thể crash sau commit trước side effect gây skipped/lost outcome; thường không chấp nhận cho at-least-once processing.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-offset-commit-failure-windows`, đưa một giá trị tới đúng boundary và một giá trị vượt boundary. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Offset commit - the two failure windows` công bố.

**Bằng chứng cần giữ.** Đối với probe 3 của `Offset commit - the two failure windows`, lưu hai observed values cùng rule đã resolve. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.4. Offset commit - the two failure windows: kiểm `Batch granularity` bằng case 4, cụ thể commit highest safely completed contiguous offset; parallel processing có holes nên max-seen commit nguy hiểm

**Mệnh đề cần kiểm.** Offset commit - the two failure windows: kiểm `Batch granularity` bằng case 4, cụ thể commit highest safely completed contiguous offset; parallel processing có holes nên max-seen commit nguy hiểm.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-offset-commit-failure-windows`, kill tiến trình ngay trước rồi ngay sau durable side effect. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Offset commit - the two failure windows` công bố.

**Bằng chứng cần giữ.** Đối với probe 4 của `Offset commit - the two failure windows`, lưu checkpoint, external ledger và trạng thái sau restart. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.5. Offset commit - the two failure windows: kiểm `Atomic coupling` bằng case 5, cụ thể kafka transaction couple output+offset trong kafka; external sink cần local transaction/outbox/checkpoint protocol riêng

**Mệnh đề cần kiểm.** Offset commit - the two failure windows: kiểm `Atomic coupling` bằng case 5, cụ thể kafka transaction couple output+offset trong kafka; external sink cần local transaction/outbox/checkpoint protocol riêng.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-offset-commit-failure-windows`, đảo thứ tự input và concurrency nhưng giữ logical population. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Offset commit - the two failure windows` công bố.

**Bằng chứng cần giữ.** Đối với probe 5 của `Offset commit - the two failure windows`, so canonical hash và business totals giữa các thứ tự. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.6. Offset commit - the two failure windows: kiểm `Kill-point proof` bằng case 6, cụ thể crash tại từng boundary, restart with rebalance and compare source offsets, sink keys, duplicates and missing outcomes

**Mệnh đề cần kiểm.** Offset commit - the two failure windows: kiểm `Kill-point proof` bằng case 6, cụ thể crash tại từng boundary, restart with rebalance and compare source offsets, sink keys, duplicates and missing outcomes.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-offset-commit-failure-windows`, replay cùng identity với payload giống rồi payload xung đột. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Offset commit - the two failure windows` công bố.

**Bằng chứng cần giữ.** Đối với probe 6 của `Offset commit - the two failure windows`, tách duplicate replay khỏi identity collision bằng reason code. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.7. Offset commit - the two failure windows: kiểm `Commit meaning` bằng case 7, cụ thể committed offset là next position group sẽ resume, không phải bằng chứng external side effect completed

**Mệnh đề cần kiểm.** Offset commit - the two failure windows: kiểm `Commit meaning` bằng case 7, cụ thể committed offset là next position group sẽ resume, không phải bằng chứng external side effect completed.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-offset-commit-failure-windows`, thêm record tới trễ trong horizon và ngoài horizon. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Offset commit - the two failure windows` công bố.

**Bằng chứng cần giữ.** Đối với probe 7 của `Offset commit - the two failure windows`, báo accepted-late, rejected-late và oldest outstanding timestamp. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.8. Offset commit - the two failure windows: kiểm `Process then commit` bằng case 8, cụ thể crash sau side effect trước commit gây replay/duplicate; idempotent sink hoặc dedup ledger hấp thụ

**Mệnh đề cần kiểm.** Offset commit - the two failure windows: kiểm `Process then commit` bằng case 8, cụ thể crash sau side effect trước commit gây replay/duplicate; idempotent sink hoặc dedup ledger hấp thụ.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-offset-commit-failure-windows`, đổi schema theo một cách tương thích rồi một cách phá vỡ semantics. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Offset commit - the two failure windows` công bố.

**Bằng chứng cần giữ.** Đối với probe 8 của `Offset commit - the two failure windows`, giữ schema diff, classification và consumer-visible result. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.9. Offset commit - the two failure windows: kiểm `Commit then process` bằng case 9, cụ thể crash sau commit trước side effect gây skipped/lost outcome; thường không chấp nhận cho at-least-once processing

**Mệnh đề cần kiểm.** Offset commit - the two failure windows: kiểm `Commit then process` bằng case 9, cụ thể crash sau commit trước side effect gây skipped/lost outcome; thường không chấp nhận cho at-least-once processing.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-offset-commit-failure-windows`, tạo missing và duplicate bù nhau để count tổng không đổi. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Offset commit - the two failure windows` công bố.

**Bằng chứng cần giữ.** Đối với probe 9 của `Offset commit - the two failure windows`, so key multiset và typed hashes thay vì chỉ row count. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.10. Offset commit - the two failure windows: kiểm `Batch granularity` bằng case 10, cụ thể commit highest safely completed contiguous offset; parallel processing có holes nên max-seen commit nguy hiểm

**Mệnh đề cần kiểm.** Offset commit - the two failure windows: kiểm `Batch granularity` bằng case 10, cụ thể commit highest safely completed contiguous offset; parallel processing có holes nên max-seen commit nguy hiểm.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-offset-commit-failure-windows`, cho reviewer tái hiện chỉ từ evidence package. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Offset commit - the two failure windows` công bố.

**Bằng chứng cần giữ.** Đối với probe 10 của `Offset commit - the two failure windows`, package phải đủ để người khác dựng lại decision và limitation. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.11. Offset commit - the two failure windows: kiểm `Atomic coupling` bằng case 11, cụ thể kafka transaction couple output+offset trong kafka; external sink cần local transaction/outbox/checkpoint protocol riêng

**Mệnh đề cần kiểm.** Offset commit - the two failure windows: kiểm `Atomic coupling` bằng case 11, cụ thể kafka transaction couple output+offset trong kafka; external sink cần local transaction/outbox/checkpoint protocol riêng.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-offset-commit-failure-windows`, so với oracle độc lập không dùng chung query hoặc parser. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Offset commit - the two failure windows` công bố.

**Bằng chứng cần giữ.** Đối với probe 11 của `Offset commit - the two failure windows`, independent result phải khớp ở grain đã công bố. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.12. Offset commit - the two failure windows: kiểm `Kill-point proof` bằng case 12, cụ thể crash tại từng boundary, restart with rebalance and compare source offsets, sink keys, duplicates and missing outcomes

**Mệnh đề cần kiểm.** Offset commit - the two failure windows: kiểm `Kill-point proof` bằng case 12, cụ thể crash tại từng boundary, restart with rebalance and compare source offsets, sink keys, duplicates and missing outcomes.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-offset-commit-failure-windows`, chạy scope hẹp và population đầy đủ rồi công bố phần bị loại. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Offset commit - the two failure windows` công bố.

**Bằng chứng cần giữ.** Đối với probe 12 của `Offset commit - the two failure windows`, coverage phải nêu rõ excluded nodes, partitions hoặc incidents. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.13. Offset commit - the two failure windows: kiểm `Commit meaning` bằng case 13, cụ thể committed offset là next position group sẽ resume, không phải bằng chứng external side effect completed

**Mệnh đề cần kiểm.** Offset commit - the two failure windows: kiểm `Commit meaning` bằng case 13, cụ thể committed offset là next position group sẽ resume, không phải bằng chứng external side effect completed.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-offset-commit-failure-windows`, thử timezone, precision hoặc partition ở hai phía của ranh giới. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Offset commit - the two failure windows` công bố.

**Bằng chứng cần giữ.** Đối với probe 13 của `Offset commit - the two failure windows`, UTC/local interval và rounding policy phải hiện trong output. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.14. Offset commit - the two failure windows: kiểm `Process then commit` bằng case 14, cụ thể crash sau side effect trước commit gây replay/duplicate; idempotent sink hoặc dedup ledger hấp thụ

**Mệnh đề cần kiểm.** Offset commit - the two failure windows: kiểm `Process then commit` bằng case 14, cụ thể crash sau side effect trước commit gây replay/duplicate; idempotent sink hoặc dedup ledger hấp thụ.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-offset-commit-failure-windows`, đổi constraint đủ lớn để quyết định phải đảo. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Offset commit - the two failure windows` công bố.

**Bằng chứng cần giữ.** Đối với probe 14 của `Offset commit - the two failure windows`, ADR phải lưu changed constraint và reversal threshold. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.15. Offset commit - the two failure windows: kiểm `Commit then process` bằng case 15, cụ thể crash sau commit trước side effect gây skipped/lost outcome; thường không chấp nhận cho at-least-once processing

**Mệnh đề cần kiểm.** Offset commit - the two failure windows: kiểm `Commit then process` bằng case 15, cụ thể crash sau commit trước side effect gây skipped/lost outcome; thường không chấp nhận cho at-least-once processing.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-offset-commit-failure-windows`, chạy lại từ môi trường sạch với versions và seed đã khóa. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Offset commit - the two failure windows` công bố.

**Bằng chứng cần giữ.** Đối với probe 15 của `Offset commit - the two failure windows`, canonical result phải ổn định hoặc mọi nondeterminism phải được giải thích. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

## 8. Quy trình phản biện

1. Viết consumer-visible invariant cho `Offset commit - the two failure windows` trước khi chọn query hoặc tool.
2. Khóa grain, identity, population, time window và authoritative source.
3. Phân biệt declared configuration, executed state và published state.
4. Chạy negative control, replay hoặc changed-assumption case phù hợp.
5. Đối soát bằng oracle độc lập; công bố coverage và phần không quan sát được.
6. Gắn owner, hành động, reversal trigger và hạn review cho kết luận.

## 9. Câu hỏi tự kiểm tra

1. `Offset commit - the two failure windows: kiểm `Commit meaning` bằng case 1, cụ thể committed offset là next position group sẽ resume, không phải bằng chứng external side effect completed` thất bại đầu tiên ở boundary nào?
2. Artifact nào mạnh nhất để trả lời `Offset commit - the two failure windows: kiểm `Commit then process` bằng case 3, cụ thể crash sau commit trước side effect gây skipped/lost outcome; thường không chấp nhận cho at-least-once processing`?
3. Counterexample nhỏ nhất cho `Offset commit - the two failure windows: kiểm `Kill-point proof` bằng case 6, cụ thể crash tại từng boundary, restart with rebalance and compare source offsets, sink keys, duplicates and missing outcomes` gồm những state nào?
4. `Offset commit - the two failure windows: kiểm `Commit then process` bằng case 9, cụ thể crash sau commit trước side effect gây skipped/lost outcome; thường không chấp nhận cho at-least-once processing` có thể xanh giả ra sao?
5. Constraint nào khiến quyết định ở `Offset commit - the two failure windows: kiểm `Process then commit` bằng case 14, cụ thể crash sau side effect trước commit gây replay/duplicate; idempotent sink hoặc dedup ledger hấp thụ` phải đảo?
6. Phần nào của `Offset commit - the two failure windows: kiểm `Commit then process` bằng case 15, cụ thể crash sau commit trước side effect gây skipped/lost outcome; thường không chấp nhận cho at-least-once processing` mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `Offset commit - the two failure windows` chưa chạy trên hệ thống production; nội dung là giáo trình và expected evidence.
- Hành vi phụ thuộc phiên bản, connector, scheduler, warehouse và catalog configuration phải được kiểm lại.
- Các ma trận, ladder và threshold do giáo trình tổng hợp không được gán nguyên văn cho vendor.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-APACHE-KAFKA-CONSUMER-CONFIG]]
2. [[SRC-APACHE-KAFKA-DESIGN]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-APACHE-KAFKA-CONSUMER-CONFIG]] | Contract hoặc cơ chế liên quan trực tiếp tới `Offset commit - the two failure windows` | Đã đọc locator; cần pin version khi chạy lab |
| [[SRC-APACHE-KAFKA-DESIGN]] | Contract hoặc cơ chế liên quan trực tiếp tới `Offset commit - the two failure windows` | Đã đọc locator; cần pin version khi chạy lab |

## Key takeaways
- Process-before-commit duplicates; commit-before-process loses outcomes unless state is atomically coupled.
- Với `wiki.streaming.kafka-offset-commit-failure-windows`, quality của kết luận phụ thuộc identity, coverage và oracle chứ không phụ thuộc màu dashboard.
- Câu hỏi `Hai thứ tự process–commit offset tạo duplicate hoặc loss window ra sao, và state coupling sửa được gì?` chỉ được trả lời trong scope và version đã ghi.
- Các source IDs `src.web.apache-kafka-consumer-config, src.web.apache-kafka-design` đặt ranh giới cho source fact; phần còn lại là synthesis có nhãn.
- Trước khi lab chạy, đây là note đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.
