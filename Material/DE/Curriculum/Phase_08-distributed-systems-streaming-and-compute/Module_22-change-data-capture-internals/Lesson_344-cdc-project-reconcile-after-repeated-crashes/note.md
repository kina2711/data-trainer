# Phase 8: Distributed Systems, Streaming and Compute
# Module 22: Change Data Capture Internals
# Lesson 344: CDC project - reconcile after repeated crashes

## Mục tiêu bài học

**Năng lực cần chứng minh.** Nộp đường bắt thay đổi hoàn chỉnh, đối soát khớp nguồn sau ít nhất 30 lần giết ngẫu nhiên.

**Điều kiện hoàn thành.** Đích khớp nguồn tuyệt đối về tập khoá và giá trị sau ≥ 30 lần giết, bốn vị trí tiến độ có số đo độ trễ, và lần chụp lại có đối soát trước khi hoán đổi.

> [!abstract] Câu hỏi trung tâm
> Một CDC pipeline phải chứng minh convergence ra sao sau nhiều lần crash tại các durability boundaries?

## 1. Invariant

Capstone chốt source key set, typed row hash, delete semantics, accepted schema versions và maximum declared lag. Đừng bắt đầu bằng tên công cụ. Hãy bắt đầu bằng đối tượng được bảo vệ, boundary quan sát được và hậu quả nếu kết luận sai. Trong bài `CDC project - reconcile after repeated crashes`, câu hỏi thực dụng là: Một CDC pipeline phải chứng minh convergence ra sao sau nhiều lần crash tại các durability boundaries? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 2. Crash matrix

Kill trước/sau source-offset flush, transport publish, sink side effect và sink checkpoint để tạo replay windows có chủ đích. Điểm khó không nằm ở cú pháp mà ở identity và scope. Hai phép đo cùng tên vẫn có thể nói về hai population hoặc hai thời điểm khác nhau. Trong bài `CDC project - reconcile after repeated crashes`, câu hỏi thực dụng là: Một CDC pipeline phải chứng minh convergence ra sao sau nhiều lần crash tại các durability boundaries? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 3. Idempotent sink

Sink dùng stable event identity hoặc compare-and-set/version rule; dedup không được dựa duy nhất vào wall clock. Một dashboard xanh chỉ là tín hiệu. Muốn biến nó thành bằng chứng phải giữ input, phiên bản, rule, trạng thái trước–sau và cách tính độc lập. Trong bài `CDC project - reconcile after repeated crashes`, câu hỏi thực dụng là: Một CDC pipeline phải chứng minh convergence ra sao sau nhiều lần crash tại các durability boundaries? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 4. Reconciliation

So key multiset, per-key version/hash, aggregates và quarantine inventory tại cùng declared cut. Thiết kế tốt phải chịu được counterexample. Hãy chủ động tạo case sát boundary, case thiếu dữ liệu và case replay thay vì chỉ chạy happy path. Trong bài `CDC project - reconcile after repeated crashes`, câu hỏi thực dụng là: Một CDC pipeline phải chứng minh convergence ra sao sau nhiều lần crash tại các durability boundaries? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 5. Repair

Backfill hoặc replay phải có bounded scope, checkpoint riêng, conflict policy và proof không ghi đè state mới hơn. Chi phí vận hành thuộc contract. Một rule đúng nhưng quá đắt, quá ồn hoặc không có owner sẽ nhanh chóng bị tắt và mất tác dụng. Trong bài `CDC project - reconcile after repeated crashes`, câu hỏi thực dụng là: Một CDC pipeline phải chứng minh convergence ra sao sau nhiều lần crash tại các durability boundaries? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 6. Dossier

Bàn giao gồm configs, versions, mutation log, crash schedule, offsets, reconciliation output, residual gaps và owner sign-off. Kết luận cần có điều kiện đảo chiều. Khi volume, latency, nguồn thẩm quyền hoặc topology đổi, quyết định cũ phải được xem xét lại bằng cùng một oracle. Trong bài `CDC project - reconcile after repeated crashes`, câu hỏi thực dụng là: Một CDC pipeline phải chứng minh convergence ra sao sau nhiều lần crash tại các durability boundaries? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 7. Ma trận kiểm chứng từng mệnh đề

Với `wiki.cdc.repeated-crash-reconciliation`, command thành công không tự chứng minh dữ liệu đúng. Protocol riêng của bài là: Run a version-pinned CDC or Spark fixture, inject the declared mutation/failure and reconcile identities, positions, attempts and final state against an independent oracle. Mỗi probe dưới đây phải nối input boundary với failure signal và oracle có thể phản bác kết luận.

### 7.1. CDC project - reconcile after repeated crashes: kiểm `Invariant` bằng case 1, cụ thể capstone chốt source key set, typed row hash, delete semantics, accepted schema versions và maximum declared lag

**Mệnh đề cần kiểm.** CDC project - reconcile after repeated crashes: kiểm `Invariant` bằng case 1, cụ thể capstone chốt source key set, typed row hash, delete semantics, accepted schema versions và maximum declared lag.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.repeated-crash-reconciliation`, tạo positive control và negative control chỉ khác đúng một điều kiện. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `CDC project - reconcile after repeated crashes` công bố.

**Bằng chứng cần giữ.** Đối với probe 1 của `CDC project - reconcile after repeated crashes`, giữ fixture, raw failing rows và lệnh tái hiện. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.2. CDC project - reconcile after repeated crashes: kiểm `Crash matrix` bằng case 2, cụ thể kill trước/sau source-offset flush, transport publish, sink side effect và sink checkpoint để tạo replay windows có chủ đích

**Mệnh đề cần kiểm.** CDC project - reconcile after repeated crashes: kiểm `Crash matrix` bằng case 2, cụ thể kill trước/sau source-offset flush, transport publish, sink side effect và sink checkpoint để tạo replay windows có chủ đích.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.repeated-crash-reconciliation`, đổi grain nhưng giữ tổng số dòng để lộ phép đo sai cấp. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `CDC project - reconcile after repeated crashes` công bố.

**Bằng chứng cần giữ.** Đối với probe 2 của `CDC project - reconcile after repeated crashes`, báo numerator, denominator và key set ở cả hai grain. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.3. CDC project - reconcile after repeated crashes: kiểm `Idempotent sink` bằng case 3, cụ thể sink dùng stable event identity hoặc compare-and-set/version rule; dedup không được dựa duy nhất vào wall clock

**Mệnh đề cần kiểm.** CDC project - reconcile after repeated crashes: kiểm `Idempotent sink` bằng case 3, cụ thể sink dùng stable event identity hoặc compare-and-set/version rule; dedup không được dựa duy nhất vào wall clock.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.repeated-crash-reconciliation`, đưa một giá trị tới đúng boundary và một giá trị vượt boundary. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `CDC project - reconcile after repeated crashes` công bố.

**Bằng chứng cần giữ.** Đối với probe 3 của `CDC project - reconcile after repeated crashes`, lưu hai observed values cùng rule đã resolve. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.4. CDC project - reconcile after repeated crashes: kiểm `Reconciliation` bằng case 4, cụ thể so key multiset, per-key version/hash, aggregates và quarantine inventory tại cùng declared cut

**Mệnh đề cần kiểm.** CDC project - reconcile after repeated crashes: kiểm `Reconciliation` bằng case 4, cụ thể so key multiset, per-key version/hash, aggregates và quarantine inventory tại cùng declared cut.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.repeated-crash-reconciliation`, kill tiến trình ngay trước rồi ngay sau durable side effect. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `CDC project - reconcile after repeated crashes` công bố.

**Bằng chứng cần giữ.** Đối với probe 4 của `CDC project - reconcile after repeated crashes`, lưu checkpoint, external ledger và trạng thái sau restart. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.5. CDC project - reconcile after repeated crashes: kiểm `Repair` bằng case 5, cụ thể backfill hoặc replay phải có bounded scope, checkpoint riêng, conflict policy và proof không ghi đè state mới hơn

**Mệnh đề cần kiểm.** CDC project - reconcile after repeated crashes: kiểm `Repair` bằng case 5, cụ thể backfill hoặc replay phải có bounded scope, checkpoint riêng, conflict policy và proof không ghi đè state mới hơn.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.repeated-crash-reconciliation`, đảo thứ tự input và concurrency nhưng giữ logical population. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `CDC project - reconcile after repeated crashes` công bố.

**Bằng chứng cần giữ.** Đối với probe 5 của `CDC project - reconcile after repeated crashes`, so canonical hash và business totals giữa các thứ tự. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.6. CDC project - reconcile after repeated crashes: kiểm `Dossier` bằng case 6, cụ thể bàn giao gồm configs, versions, mutation log, crash schedule, offsets, reconciliation output, residual gaps và owner sign-off

**Mệnh đề cần kiểm.** CDC project - reconcile after repeated crashes: kiểm `Dossier` bằng case 6, cụ thể bàn giao gồm configs, versions, mutation log, crash schedule, offsets, reconciliation output, residual gaps và owner sign-off.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.repeated-crash-reconciliation`, replay cùng identity với payload giống rồi payload xung đột. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `CDC project - reconcile after repeated crashes` công bố.

**Bằng chứng cần giữ.** Đối với probe 6 của `CDC project - reconcile after repeated crashes`, tách duplicate replay khỏi identity collision bằng reason code. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.7. CDC project - reconcile after repeated crashes: kiểm `Invariant` bằng case 7, cụ thể capstone chốt source key set, typed row hash, delete semantics, accepted schema versions và maximum declared lag

**Mệnh đề cần kiểm.** CDC project - reconcile after repeated crashes: kiểm `Invariant` bằng case 7, cụ thể capstone chốt source key set, typed row hash, delete semantics, accepted schema versions và maximum declared lag.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.repeated-crash-reconciliation`, thêm record tới trễ trong horizon và ngoài horizon. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `CDC project - reconcile after repeated crashes` công bố.

**Bằng chứng cần giữ.** Đối với probe 7 của `CDC project - reconcile after repeated crashes`, báo accepted-late, rejected-late và oldest outstanding timestamp. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.8. CDC project - reconcile after repeated crashes: kiểm `Crash matrix` bằng case 8, cụ thể kill trước/sau source-offset flush, transport publish, sink side effect và sink checkpoint để tạo replay windows có chủ đích

**Mệnh đề cần kiểm.** CDC project - reconcile after repeated crashes: kiểm `Crash matrix` bằng case 8, cụ thể kill trước/sau source-offset flush, transport publish, sink side effect và sink checkpoint để tạo replay windows có chủ đích.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.repeated-crash-reconciliation`, đổi schema theo một cách tương thích rồi một cách phá vỡ semantics. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `CDC project - reconcile after repeated crashes` công bố.

**Bằng chứng cần giữ.** Đối với probe 8 của `CDC project - reconcile after repeated crashes`, giữ schema diff, classification và consumer-visible result. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.9. CDC project - reconcile after repeated crashes: kiểm `Idempotent sink` bằng case 9, cụ thể sink dùng stable event identity hoặc compare-and-set/version rule; dedup không được dựa duy nhất vào wall clock

**Mệnh đề cần kiểm.** CDC project - reconcile after repeated crashes: kiểm `Idempotent sink` bằng case 9, cụ thể sink dùng stable event identity hoặc compare-and-set/version rule; dedup không được dựa duy nhất vào wall clock.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.repeated-crash-reconciliation`, tạo missing và duplicate bù nhau để count tổng không đổi. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `CDC project - reconcile after repeated crashes` công bố.

**Bằng chứng cần giữ.** Đối với probe 9 của `CDC project - reconcile after repeated crashes`, so key multiset và typed hashes thay vì chỉ row count. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.10. CDC project - reconcile after repeated crashes: kiểm `Reconciliation` bằng case 10, cụ thể so key multiset, per-key version/hash, aggregates và quarantine inventory tại cùng declared cut

**Mệnh đề cần kiểm.** CDC project - reconcile after repeated crashes: kiểm `Reconciliation` bằng case 10, cụ thể so key multiset, per-key version/hash, aggregates và quarantine inventory tại cùng declared cut.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.repeated-crash-reconciliation`, cho reviewer tái hiện chỉ từ evidence package. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `CDC project - reconcile after repeated crashes` công bố.

**Bằng chứng cần giữ.** Đối với probe 10 của `CDC project - reconcile after repeated crashes`, package phải đủ để người khác dựng lại decision và limitation. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.11. CDC project - reconcile after repeated crashes: kiểm `Repair` bằng case 11, cụ thể backfill hoặc replay phải có bounded scope, checkpoint riêng, conflict policy và proof không ghi đè state mới hơn

**Mệnh đề cần kiểm.** CDC project - reconcile after repeated crashes: kiểm `Repair` bằng case 11, cụ thể backfill hoặc replay phải có bounded scope, checkpoint riêng, conflict policy và proof không ghi đè state mới hơn.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.repeated-crash-reconciliation`, so với oracle độc lập không dùng chung query hoặc parser. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `CDC project - reconcile after repeated crashes` công bố.

**Bằng chứng cần giữ.** Đối với probe 11 của `CDC project - reconcile after repeated crashes`, independent result phải khớp ở grain đã công bố. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.12. CDC project - reconcile after repeated crashes: kiểm `Dossier` bằng case 12, cụ thể bàn giao gồm configs, versions, mutation log, crash schedule, offsets, reconciliation output, residual gaps và owner sign-off

**Mệnh đề cần kiểm.** CDC project - reconcile after repeated crashes: kiểm `Dossier` bằng case 12, cụ thể bàn giao gồm configs, versions, mutation log, crash schedule, offsets, reconciliation output, residual gaps và owner sign-off.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.repeated-crash-reconciliation`, chạy scope hẹp và population đầy đủ rồi công bố phần bị loại. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `CDC project - reconcile after repeated crashes` công bố.

**Bằng chứng cần giữ.** Đối với probe 12 của `CDC project - reconcile after repeated crashes`, coverage phải nêu rõ excluded nodes, partitions hoặc incidents. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.13. CDC project - reconcile after repeated crashes: kiểm `Invariant` bằng case 13, cụ thể capstone chốt source key set, typed row hash, delete semantics, accepted schema versions và maximum declared lag

**Mệnh đề cần kiểm.** CDC project - reconcile after repeated crashes: kiểm `Invariant` bằng case 13, cụ thể capstone chốt source key set, typed row hash, delete semantics, accepted schema versions và maximum declared lag.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.repeated-crash-reconciliation`, thử timezone, precision hoặc partition ở hai phía của ranh giới. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `CDC project - reconcile after repeated crashes` công bố.

**Bằng chứng cần giữ.** Đối với probe 13 của `CDC project - reconcile after repeated crashes`, UTC/local interval và rounding policy phải hiện trong output. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.14. CDC project - reconcile after repeated crashes: kiểm `Crash matrix` bằng case 14, cụ thể kill trước/sau source-offset flush, transport publish, sink side effect và sink checkpoint để tạo replay windows có chủ đích

**Mệnh đề cần kiểm.** CDC project - reconcile after repeated crashes: kiểm `Crash matrix` bằng case 14, cụ thể kill trước/sau source-offset flush, transport publish, sink side effect và sink checkpoint để tạo replay windows có chủ đích.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.repeated-crash-reconciliation`, đổi constraint đủ lớn để quyết định phải đảo. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `CDC project - reconcile after repeated crashes` công bố.

**Bằng chứng cần giữ.** Đối với probe 14 của `CDC project - reconcile after repeated crashes`, ADR phải lưu changed constraint và reversal threshold. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.15. CDC project - reconcile after repeated crashes: kiểm `Idempotent sink` bằng case 15, cụ thể sink dùng stable event identity hoặc compare-and-set/version rule; dedup không được dựa duy nhất vào wall clock

**Mệnh đề cần kiểm.** CDC project - reconcile after repeated crashes: kiểm `Idempotent sink` bằng case 15, cụ thể sink dùng stable event identity hoặc compare-and-set/version rule; dedup không được dựa duy nhất vào wall clock.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.repeated-crash-reconciliation`, chạy lại từ môi trường sạch với versions và seed đã khóa. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `CDC project - reconcile after repeated crashes` công bố.

**Bằng chứng cần giữ.** Đối với probe 15 của `CDC project - reconcile after repeated crashes`, canonical result phải ổn định hoặc mọi nondeterminism phải được giải thích. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

## 8. Quy trình phản biện

1. Viết consumer-visible invariant cho `CDC project - reconcile after repeated crashes` trước khi chọn query hoặc tool.
2. Khóa grain, identity, population, time window và authoritative source.
3. Phân biệt declared configuration, executed state và published state.
4. Chạy negative control, replay hoặc changed-assumption case phù hợp.
5. Đối soát bằng oracle độc lập; công bố coverage và phần không quan sát được.
6. Gắn owner, hành động, reversal trigger và hạn review cho kết luận.

## 9. Câu hỏi tự kiểm tra

1. `CDC project - reconcile after repeated crashes: kiểm `Invariant` bằng case 1, cụ thể capstone chốt source key set, typed row hash, delete semantics, accepted schema versions và maximum declared lag` thất bại đầu tiên ở boundary nào?
2. Artifact nào mạnh nhất để trả lời `CDC project - reconcile after repeated crashes: kiểm `Idempotent sink` bằng case 3, cụ thể sink dùng stable event identity hoặc compare-and-set/version rule; dedup không được dựa duy nhất vào wall clock`?
3. Counterexample nhỏ nhất cho `CDC project - reconcile after repeated crashes: kiểm `Dossier` bằng case 6, cụ thể bàn giao gồm configs, versions, mutation log, crash schedule, offsets, reconciliation output, residual gaps và owner sign-off` gồm những state nào?
4. `CDC project - reconcile after repeated crashes: kiểm `Idempotent sink` bằng case 9, cụ thể sink dùng stable event identity hoặc compare-and-set/version rule; dedup không được dựa duy nhất vào wall clock` có thể xanh giả ra sao?
5. Constraint nào khiến quyết định ở `CDC project - reconcile after repeated crashes: kiểm `Crash matrix` bằng case 14, cụ thể kill trước/sau source-offset flush, transport publish, sink side effect và sink checkpoint để tạo replay windows có chủ đích` phải đảo?
6. Phần nào của `CDC project - reconcile after repeated crashes: kiểm `Idempotent sink` bằng case 15, cụ thể sink dùng stable event identity hoặc compare-and-set/version rule; dedup không được dựa duy nhất vào wall clock` mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `CDC project - reconcile after repeated crashes` chưa chạy trên hệ thống production; nội dung là giáo trình và expected evidence.
- Hành vi phụ thuộc phiên bản, connector, scheduler, warehouse và catalog configuration phải được kiểm lại.
- Các ma trận, ladder và threshold do giáo trình tổng hợp không được gán nguyên văn cho vendor.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-DEBEZIUM-POSTGRESQL]]
2. [[SRC-POSTGRESQL-LOGICAL-DECODING]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-DEBEZIUM-POSTGRESQL]] | Contract hoặc cơ chế liên quan trực tiếp tới `CDC project - reconcile after repeated crashes` | Đã đọc locator; cần pin version khi chạy lab |
| [[SRC-POSTGRESQL-LOGICAL-DECODING]] | Contract hoặc cơ chế liên quan trực tiếp tới `CDC project - reconcile after repeated crashes` | Đã đọc locator; cần pin version khi chạy lab |

## Key takeaways
- CDC correctness is convergence after crashes, proved by reconciliation rather than a green connector.
- Với `wiki.cdc.repeated-crash-reconciliation`, quality của kết luận phụ thuộc identity, coverage và oracle chứ không phụ thuộc màu dashboard.
- Câu hỏi `Một CDC pipeline phải chứng minh convergence ra sao sau nhiều lần crash tại các durability boundaries?` chỉ được trả lời trong scope và version đã ghi.
- Các source IDs `src.web.debezium-postgresql, src.web.postgresql-logical-decoding` đặt ranh giới cho source fact; phần còn lại là synthesis có nhãn.
- Trước khi lab chạy, đây là note đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.
