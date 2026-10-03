# Phase 8: Distributed Systems, Streaming and Compute
# Module 22: Change Data Capture Internals
# Lesson 343: Slot retention, lag and the source disk risk

## Mục tiêu bài học

**Năng lực cần chứng minh.** Dựng cảnh báo theo thời gian còn lại và chạy đúng quy trình xử lý khi khe phình, không dùng thao tác phá huỷ.

**Điều kiện hoàn thành.** Cảnh báo nổ trước ngưỡng thời gian thoả thuận, phục hồi hoàn tất không cần bỏ khe, và lần chụp lại ở môi trường cách ly có đối soát trước khi hoán đổi.

> [!abstract] Câu hỏi trung tâm
> Replication slot biến consumer lag thành rủi ro source disk như thế nào và guardrail nào ngăn sự cố?

## 1. Retention mechanism

Slot giữ WAL còn cần cho confirmed consumer position; reliability downstream tạo storage liability upstream. Đừng bắt đầu bằng tên công cụ. Hãy bắt đầu bằng đối tượng được bảo vệ, boundary quan sát được và hậu quả nếu kết luận sai. Trong bài `Slot retention, lag and the source disk risk`, câu hỏi thực dụng là: Replication slot biến consumer lag thành rủi ro source disk như thế nào và guardrail nào ngăn sự cố? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 2. Lag meanings

Time lag, byte lag, restart LSN và confirmed-flush LSN trả lời các câu hỏi khác nhau nên không gom thành một số. Điểm khó không nằm ở cú pháp mà ở identity và scope. Hai phép đo cùng tên vẫn có thể nói về hai population hoặc hai thời điểm khác nhau. Trong bài `Slot retention, lag and the source disk risk`, câu hỏi thực dụng là: Replication slot biến consumer lag thành rủi ro source disk như thế nào và guardrail nào ngăn sự cố? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 3. Failure growth

Connector dừng, network lỗi hoặc transaction dài có thể làm retained WAL tăng dù database vẫn phục vụ query. Một dashboard xanh chỉ là tín hiệu. Muốn biến nó thành bằng chứng phải giữ input, phiên bản, rule, trạng thái trước–sau và cách tính độc lập. Trong bài `Slot retention, lag and the source disk risk`, câu hỏi thực dụng là: Replication slot biến consumer lag thành rủi ro source disk như thế nào và guardrail nào ngăn sự cố? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 4. Guardrails

Alert cần rate, absolute bytes, free disk, oldest position và time-to-exhaustion với owner/escalation rõ. Thiết kế tốt phải chịu được counterexample. Hãy chủ động tạo case sát boundary, case thiếu dữ liệu và case replay thay vì chỉ chạy happy path. Trong bài `Slot retention, lag and the source disk risk`, câu hỏi thực dụng là: Replication slot biến consumer lag thành rủi ro source disk như thế nào và guardrail nào ngăn sự cố? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 5. Recovery choices

Khôi phục connector, advance hoặc drop slot có trade-off mất change; mọi lựa chọn cần declared reconciliation boundary. Chi phí vận hành thuộc contract. Một rule đúng nhưng quá đắt, quá ồn hoặc không có owner sẽ nhanh chóng bị tắt và mất tác dụng. Trong bài `Slot retention, lag and the source disk risk`, câu hỏi thực dụng là: Replication slot biến consumer lag thành rủi ro source disk như thế nào và guardrail nào ngăn sự cố? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 6. Capacity drill

Dừng consumer có kiểm soát, đo WAL growth, chạm warning threshold rồi resume và chứng minh backlog drain. Kết luận cần có điều kiện đảo chiều. Khi volume, latency, nguồn thẩm quyền hoặc topology đổi, quyết định cũ phải được xem xét lại bằng cùng một oracle. Trong bài `Slot retention, lag and the source disk risk`, câu hỏi thực dụng là: Replication slot biến consumer lag thành rủi ro source disk như thế nào và guardrail nào ngăn sự cố? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 7. Ma trận kiểm chứng từng mệnh đề

Với `wiki.cdc.slot-retention-source-disk-risk`, command thành công không tự chứng minh dữ liệu đúng. Protocol riêng của bài là: Run a version-pinned CDC or Spark fixture, inject the declared mutation/failure and reconcile identities, positions, attempts and final state against an independent oracle. Mỗi probe dưới đây phải nối input boundary với failure signal và oracle có thể phản bác kết luận.

### 7.1. Slot retention, lag and the source disk risk: kiểm `Retention mechanism` bằng case 1, cụ thể slot giữ wal còn cần cho confirmed consumer position; reliability downstream tạo storage liability upstream

**Mệnh đề cần kiểm.** Slot retention, lag and the source disk risk: kiểm `Retention mechanism` bằng case 1, cụ thể slot giữ wal còn cần cho confirmed consumer position; reliability downstream tạo storage liability upstream.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.slot-retention-source-disk-risk`, tạo positive control và negative control chỉ khác đúng một điều kiện. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Slot retention, lag and the source disk risk` công bố.

**Bằng chứng cần giữ.** Đối với probe 1 của `Slot retention, lag and the source disk risk`, giữ fixture, raw failing rows và lệnh tái hiện. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.2. Slot retention, lag and the source disk risk: kiểm `Lag meanings` bằng case 2, cụ thể time lag, byte lag, restart lsn và confirmed-flush lsn trả lời các câu hỏi khác nhau nên không gom thành một số

**Mệnh đề cần kiểm.** Slot retention, lag and the source disk risk: kiểm `Lag meanings` bằng case 2, cụ thể time lag, byte lag, restart lsn và confirmed-flush lsn trả lời các câu hỏi khác nhau nên không gom thành một số.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.slot-retention-source-disk-risk`, đổi grain nhưng giữ tổng số dòng để lộ phép đo sai cấp. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Slot retention, lag and the source disk risk` công bố.

**Bằng chứng cần giữ.** Đối với probe 2 của `Slot retention, lag and the source disk risk`, báo numerator, denominator và key set ở cả hai grain. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.3. Slot retention, lag and the source disk risk: kiểm `Failure growth` bằng case 3, cụ thể connector dừng, network lỗi hoặc transaction dài có thể làm retained wal tăng dù database vẫn phục vụ query

**Mệnh đề cần kiểm.** Slot retention, lag and the source disk risk: kiểm `Failure growth` bằng case 3, cụ thể connector dừng, network lỗi hoặc transaction dài có thể làm retained wal tăng dù database vẫn phục vụ query.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.slot-retention-source-disk-risk`, đưa một giá trị tới đúng boundary và một giá trị vượt boundary. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Slot retention, lag and the source disk risk` công bố.

**Bằng chứng cần giữ.** Đối với probe 3 của `Slot retention, lag and the source disk risk`, lưu hai observed values cùng rule đã resolve. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.4. Slot retention, lag and the source disk risk: kiểm `Guardrails` bằng case 4, cụ thể alert cần rate, absolute bytes, free disk, oldest position và time-to-exhaustion với owner/escalation rõ

**Mệnh đề cần kiểm.** Slot retention, lag and the source disk risk: kiểm `Guardrails` bằng case 4, cụ thể alert cần rate, absolute bytes, free disk, oldest position và time-to-exhaustion với owner/escalation rõ.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.slot-retention-source-disk-risk`, kill tiến trình ngay trước rồi ngay sau durable side effect. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Slot retention, lag and the source disk risk` công bố.

**Bằng chứng cần giữ.** Đối với probe 4 của `Slot retention, lag and the source disk risk`, lưu checkpoint, external ledger và trạng thái sau restart. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.5. Slot retention, lag and the source disk risk: kiểm `Recovery choices` bằng case 5, cụ thể khôi phục connector, advance hoặc drop slot có trade-off mất change; mọi lựa chọn cần declared reconciliation boundary

**Mệnh đề cần kiểm.** Slot retention, lag and the source disk risk: kiểm `Recovery choices` bằng case 5, cụ thể khôi phục connector, advance hoặc drop slot có trade-off mất change; mọi lựa chọn cần declared reconciliation boundary.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.slot-retention-source-disk-risk`, đảo thứ tự input và concurrency nhưng giữ logical population. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Slot retention, lag and the source disk risk` công bố.

**Bằng chứng cần giữ.** Đối với probe 5 của `Slot retention, lag and the source disk risk`, so canonical hash và business totals giữa các thứ tự. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.6. Slot retention, lag and the source disk risk: kiểm `Capacity drill` bằng case 6, cụ thể dừng consumer có kiểm soát, đo wal growth, chạm warning threshold rồi resume và chứng minh backlog drain

**Mệnh đề cần kiểm.** Slot retention, lag and the source disk risk: kiểm `Capacity drill` bằng case 6, cụ thể dừng consumer có kiểm soát, đo wal growth, chạm warning threshold rồi resume và chứng minh backlog drain.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.slot-retention-source-disk-risk`, replay cùng identity với payload giống rồi payload xung đột. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Slot retention, lag and the source disk risk` công bố.

**Bằng chứng cần giữ.** Đối với probe 6 của `Slot retention, lag and the source disk risk`, tách duplicate replay khỏi identity collision bằng reason code. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.7. Slot retention, lag and the source disk risk: kiểm `Retention mechanism` bằng case 7, cụ thể slot giữ wal còn cần cho confirmed consumer position; reliability downstream tạo storage liability upstream

**Mệnh đề cần kiểm.** Slot retention, lag and the source disk risk: kiểm `Retention mechanism` bằng case 7, cụ thể slot giữ wal còn cần cho confirmed consumer position; reliability downstream tạo storage liability upstream.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.slot-retention-source-disk-risk`, thêm record tới trễ trong horizon và ngoài horizon. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Slot retention, lag and the source disk risk` công bố.

**Bằng chứng cần giữ.** Đối với probe 7 của `Slot retention, lag and the source disk risk`, báo accepted-late, rejected-late và oldest outstanding timestamp. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.8. Slot retention, lag and the source disk risk: kiểm `Lag meanings` bằng case 8, cụ thể time lag, byte lag, restart lsn và confirmed-flush lsn trả lời các câu hỏi khác nhau nên không gom thành một số

**Mệnh đề cần kiểm.** Slot retention, lag and the source disk risk: kiểm `Lag meanings` bằng case 8, cụ thể time lag, byte lag, restart lsn và confirmed-flush lsn trả lời các câu hỏi khác nhau nên không gom thành một số.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.slot-retention-source-disk-risk`, đổi schema theo một cách tương thích rồi một cách phá vỡ semantics. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Slot retention, lag and the source disk risk` công bố.

**Bằng chứng cần giữ.** Đối với probe 8 của `Slot retention, lag and the source disk risk`, giữ schema diff, classification và consumer-visible result. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.9. Slot retention, lag and the source disk risk: kiểm `Failure growth` bằng case 9, cụ thể connector dừng, network lỗi hoặc transaction dài có thể làm retained wal tăng dù database vẫn phục vụ query

**Mệnh đề cần kiểm.** Slot retention, lag and the source disk risk: kiểm `Failure growth` bằng case 9, cụ thể connector dừng, network lỗi hoặc transaction dài có thể làm retained wal tăng dù database vẫn phục vụ query.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.slot-retention-source-disk-risk`, tạo missing và duplicate bù nhau để count tổng không đổi. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Slot retention, lag and the source disk risk` công bố.

**Bằng chứng cần giữ.** Đối với probe 9 của `Slot retention, lag and the source disk risk`, so key multiset và typed hashes thay vì chỉ row count. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.10. Slot retention, lag and the source disk risk: kiểm `Guardrails` bằng case 10, cụ thể alert cần rate, absolute bytes, free disk, oldest position và time-to-exhaustion với owner/escalation rõ

**Mệnh đề cần kiểm.** Slot retention, lag and the source disk risk: kiểm `Guardrails` bằng case 10, cụ thể alert cần rate, absolute bytes, free disk, oldest position và time-to-exhaustion với owner/escalation rõ.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.slot-retention-source-disk-risk`, cho reviewer tái hiện chỉ từ evidence package. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Slot retention, lag and the source disk risk` công bố.

**Bằng chứng cần giữ.** Đối với probe 10 của `Slot retention, lag and the source disk risk`, package phải đủ để người khác dựng lại decision và limitation. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.11. Slot retention, lag and the source disk risk: kiểm `Recovery choices` bằng case 11, cụ thể khôi phục connector, advance hoặc drop slot có trade-off mất change; mọi lựa chọn cần declared reconciliation boundary

**Mệnh đề cần kiểm.** Slot retention, lag and the source disk risk: kiểm `Recovery choices` bằng case 11, cụ thể khôi phục connector, advance hoặc drop slot có trade-off mất change; mọi lựa chọn cần declared reconciliation boundary.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.slot-retention-source-disk-risk`, so với oracle độc lập không dùng chung query hoặc parser. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Slot retention, lag and the source disk risk` công bố.

**Bằng chứng cần giữ.** Đối với probe 11 của `Slot retention, lag and the source disk risk`, independent result phải khớp ở grain đã công bố. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.12. Slot retention, lag and the source disk risk: kiểm `Capacity drill` bằng case 12, cụ thể dừng consumer có kiểm soát, đo wal growth, chạm warning threshold rồi resume và chứng minh backlog drain

**Mệnh đề cần kiểm.** Slot retention, lag and the source disk risk: kiểm `Capacity drill` bằng case 12, cụ thể dừng consumer có kiểm soát, đo wal growth, chạm warning threshold rồi resume và chứng minh backlog drain.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.slot-retention-source-disk-risk`, chạy scope hẹp và population đầy đủ rồi công bố phần bị loại. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Slot retention, lag and the source disk risk` công bố.

**Bằng chứng cần giữ.** Đối với probe 12 của `Slot retention, lag and the source disk risk`, coverage phải nêu rõ excluded nodes, partitions hoặc incidents. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.13. Slot retention, lag and the source disk risk: kiểm `Retention mechanism` bằng case 13, cụ thể slot giữ wal còn cần cho confirmed consumer position; reliability downstream tạo storage liability upstream

**Mệnh đề cần kiểm.** Slot retention, lag and the source disk risk: kiểm `Retention mechanism` bằng case 13, cụ thể slot giữ wal còn cần cho confirmed consumer position; reliability downstream tạo storage liability upstream.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.slot-retention-source-disk-risk`, thử timezone, precision hoặc partition ở hai phía của ranh giới. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Slot retention, lag and the source disk risk` công bố.

**Bằng chứng cần giữ.** Đối với probe 13 của `Slot retention, lag and the source disk risk`, UTC/local interval và rounding policy phải hiện trong output. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.14. Slot retention, lag and the source disk risk: kiểm `Lag meanings` bằng case 14, cụ thể time lag, byte lag, restart lsn và confirmed-flush lsn trả lời các câu hỏi khác nhau nên không gom thành một số

**Mệnh đề cần kiểm.** Slot retention, lag and the source disk risk: kiểm `Lag meanings` bằng case 14, cụ thể time lag, byte lag, restart lsn và confirmed-flush lsn trả lời các câu hỏi khác nhau nên không gom thành một số.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.slot-retention-source-disk-risk`, đổi constraint đủ lớn để quyết định phải đảo. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Slot retention, lag and the source disk risk` công bố.

**Bằng chứng cần giữ.** Đối với probe 14 của `Slot retention, lag and the source disk risk`, ADR phải lưu changed constraint và reversal threshold. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.15. Slot retention, lag and the source disk risk: kiểm `Failure growth` bằng case 15, cụ thể connector dừng, network lỗi hoặc transaction dài có thể làm retained wal tăng dù database vẫn phục vụ query

**Mệnh đề cần kiểm.** Slot retention, lag and the source disk risk: kiểm `Failure growth` bằng case 15, cụ thể connector dừng, network lỗi hoặc transaction dài có thể làm retained wal tăng dù database vẫn phục vụ query.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.slot-retention-source-disk-risk`, chạy lại từ môi trường sạch với versions và seed đã khóa. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Slot retention, lag and the source disk risk` công bố.

**Bằng chứng cần giữ.** Đối với probe 15 của `Slot retention, lag and the source disk risk`, canonical result phải ổn định hoặc mọi nondeterminism phải được giải thích. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

## 8. Quy trình phản biện

1. Viết consumer-visible invariant cho `Slot retention, lag and the source disk risk` trước khi chọn query hoặc tool.
2. Khóa grain, identity, population, time window và authoritative source.
3. Phân biệt declared configuration, executed state và published state.
4. Chạy negative control, replay hoặc changed-assumption case phù hợp.
5. Đối soát bằng oracle độc lập; công bố coverage và phần không quan sát được.
6. Gắn owner, hành động, reversal trigger và hạn review cho kết luận.

## 9. Câu hỏi tự kiểm tra

1. `Slot retention, lag and the source disk risk: kiểm `Retention mechanism` bằng case 1, cụ thể slot giữ wal còn cần cho confirmed consumer position; reliability downstream tạo storage liability upstream` thất bại đầu tiên ở boundary nào?
2. Artifact nào mạnh nhất để trả lời `Slot retention, lag and the source disk risk: kiểm `Failure growth` bằng case 3, cụ thể connector dừng, network lỗi hoặc transaction dài có thể làm retained wal tăng dù database vẫn phục vụ query`?
3. Counterexample nhỏ nhất cho `Slot retention, lag and the source disk risk: kiểm `Capacity drill` bằng case 6, cụ thể dừng consumer có kiểm soát, đo wal growth, chạm warning threshold rồi resume và chứng minh backlog drain` gồm những state nào?
4. `Slot retention, lag and the source disk risk: kiểm `Failure growth` bằng case 9, cụ thể connector dừng, network lỗi hoặc transaction dài có thể làm retained wal tăng dù database vẫn phục vụ query` có thể xanh giả ra sao?
5. Constraint nào khiến quyết định ở `Slot retention, lag and the source disk risk: kiểm `Lag meanings` bằng case 14, cụ thể time lag, byte lag, restart lsn và confirmed-flush lsn trả lời các câu hỏi khác nhau nên không gom thành một số` phải đảo?
6. Phần nào của `Slot retention, lag and the source disk risk: kiểm `Failure growth` bằng case 15, cụ thể connector dừng, network lỗi hoặc transaction dài có thể làm retained wal tăng dù database vẫn phục vụ query` mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `Slot retention, lag and the source disk risk` chưa chạy trên hệ thống production; nội dung là giáo trình và expected evidence.
- Hành vi phụ thuộc phiên bản, connector, scheduler, warehouse và catalog configuration phải được kiểm lại.
- Các ma trận, ladder và threshold do giáo trình tổng hợp không được gán nguyên văn cho vendor.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-POSTGRESQL-LOGICAL-DECODING]]
2. [[SRC-DEBEZIUM-POSTGRESQL]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-POSTGRESQL-LOGICAL-DECODING]] | Contract hoặc cơ chế liên quan trực tiếp tới `Slot retention, lag and the source disk risk` | Đã đọc locator; cần pin version khi chạy lab |
| [[SRC-DEBEZIUM-POSTGRESQL]] | Contract hoặc cơ chế liên quan trực tiếp tới `Slot retention, lag and the source disk risk` | Đã đọc locator; cần pin version khi chạy lab |

## Key takeaways
- A stalled replication slot can turn downstream lag into source disk exhaustion.
- Với `wiki.cdc.slot-retention-source-disk-risk`, quality của kết luận phụ thuộc identity, coverage và oracle chứ không phụ thuộc màu dashboard.
- Câu hỏi `Replication slot biến consumer lag thành rủi ro source disk như thế nào và guardrail nào ngăn sự cố?` chỉ được trả lời trong scope và version đã ghi.
- Các source IDs `src.web.postgresql-logical-decoding, src.web.debezium-postgresql` đặt ranh giới cho source fact; phần còn lại là synthesis có nhãn.
- Trước khi lab chạy, đây là note đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.
