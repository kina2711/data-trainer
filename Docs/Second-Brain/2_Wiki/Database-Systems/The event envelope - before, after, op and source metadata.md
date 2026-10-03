---
note_id: wiki.cdc.event-envelope
note_type: concept-deep-dive
status: canonical
approved_by: second-brain-owner
approved_at: 2026-10-03
approval_scope: all-registered-notes
canonical_since: 2026-10-03
language: vi
created: 2026-10-02
last_verified: 2026-10-02
editorial_pass: humanized-v3
primary_question: CDC envelope fields before, after, op và source metadata phải được đọc như typed evidence thay vì JSON shape cố định ra sao?
source_ids:
  - src.web.debezium-postgresql
aliases: [The event envelope - before, after, op and source metadata]
tags: [wiki/change-data-capture, cdc, transaction-log, replication, reliability]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/226-the-event-envelope-before-after-op-and-source-metadata.md
relationships:
  builds_on: [wiki.cdc.consistent-bootstrap-snapshot-log]
  prerequisite_of: [wiki.cdc.ordering-transaction-scope]
  related_to: []

---
# The event envelope - before, after, op and source metadata

> [!abstract] Câu hỏi trung tâm
> CDC envelope fields before, after, op và source metadata phải được đọc như typed evidence thay vì JSON shape cố định ra sao?

## 1. Key

Event key normally derives from primary/unique key or configured columns; keyless rows weaken identity/dedup/delete handling. Đừng bắt đầu bằng tên công cụ. Hãy bắt đầu bằng đối tượng được bảo vệ, boundary quan sát được và hậu quả nếu kết luận sai. Trong bài `The event envelope - before, after, op and source metadata`, câu hỏi thực dụng là: CDC envelope fields before, after, op và source metadata phải được đọc như typed evidence thay vì JSON shape cố định ra sao? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 2. Before and after

Images depend on operation and replica identity/source configuration; null may mean unavailable, not necessarily empty row. Điểm khó không nằm ở cú pháp mà ở identity và scope. Hai phép đo cùng tên vẫn có thể nói về hai population hoặc hai thời điểm khác nhau. Trong bài `The event envelope - before, after, op and source metadata`, câu hỏi thực dụng là: CDC envelope fields before, after, op và source metadata phải được đọc như typed evidence thay vì JSON shape cố định ra sao? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 3. Operation code

Create, update, delete, read snapshot, truncate and message events carry different state transitions. Một dashboard xanh chỉ là tín hiệu. Muốn biến nó thành bằng chứng phải giữ input, phiên bản, rule, trạng thái trước–sau và cách tính độc lập. Trong bài `The event envelope - before, after, op and source metadata`, câu hỏi thực dụng là: CDC envelope fields before, after, op và source metadata phải được đọc như typed evidence thay vì JSON shape cố định ra sao? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 4. Source metadata

Connector/source/table, transaction, log position, snapshot flag and source timestamp support ordering/lineage diagnosis. Thiết kế tốt phải chịu được counterexample. Hãy chủ động tạo case sát boundary, case thiếu dữ liệu và case replay thay vì chỉ chạy happy path. Trong bài `The event envelope - before, after, op and source metadata`, câu hỏi thực dụng là: CDC envelope fields before, after, op và source metadata phải được đọc như typed evidence thay vì JSON shape cố định ra sao? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 5. Processing time

Connector processing timestamp differs source commit/event time; their difference is a lag signal with clock caveats. Chi phí vận hành thuộc contract. Một rule đúng nhưng quá đắt, quá ồn hoặc không có owner sẽ nhanh chóng bị tắt và mất tác dụng. Trong bài `The event envelope - before, after, op and source metadata`, câu hỏi thực dụng là: CDC envelope fields before, after, op và source metadata phải được đọc như typed evidence thay vì JSON shape cố định ra sao? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 6. Consumer contract

Schema ID/version, envelope version and unsupported types must be pinned; quarantine unknown op/schema instead of coercing. Kết luận cần có điều kiện đảo chiều. Khi volume, latency, nguồn thẩm quyền hoặc topology đổi, quyết định cũ phải được xem xét lại bằng cùng một oracle. Trong bài `The event envelope - before, after, op and source metadata`, câu hỏi thực dụng là: CDC envelope fields before, after, op và source metadata phải được đọc như typed evidence thay vì JSON shape cố định ra sao? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 7. Ma trận kiểm chứng từng mệnh đề

Với `wiki.cdc.event-envelope`, command thành công không tự chứng minh dữ liệu đúng. Protocol riêng của bài là: Run PostgreSQL/Debezium-compatible fixture, inject writes/crash/interleaving and reconcile source keys, log positions, transport offsets and sink state. Mỗi probe dưới đây phải nối input boundary với failure signal và oracle có thể phản bác kết luận.

### 7.1. The event envelope - before, after, op and source metadata: kiểm `Key` bằng case 1, cụ thể event key normally derives from primary/unique key or configured columns; keyless rows weaken identity/dedup/delete handling

**Mệnh đề cần kiểm.** The event envelope - before, after, op and source metadata: kiểm `Key` bằng case 1, cụ thể event key normally derives from primary/unique key or configured columns; keyless rows weaken identity/dedup/delete handling.

**Thiết kế phép thử cho `wiki.cdc.event-envelope`.** Trong ngữ cảnh `wiki.cdc.event-envelope`, tạo positive control và negative control chỉ khác đúng một điều kiện. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The event envelope - before, after, op and source metadata` công bố.

**Bằng chứng cần giữ.** Đối với probe 1 của `The event envelope - before, after, op and source metadata`, giữ fixture, raw failing rows và lệnh tái hiện. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.2. The event envelope - before, after, op and source metadata: kiểm `Before and after` bằng case 2, cụ thể images depend on operation and replica identity/source configuration; null may mean unavailable, not necessarily empty row

**Mệnh đề cần kiểm.** The event envelope - before, after, op and source metadata: kiểm `Before and after` bằng case 2, cụ thể images depend on operation and replica identity/source configuration; null may mean unavailable, not necessarily empty row.

**Thiết kế phép thử cho `wiki.cdc.event-envelope`.** Trong ngữ cảnh `wiki.cdc.event-envelope`, đổi grain nhưng giữ tổng số dòng để lộ phép đo sai cấp. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The event envelope - before, after, op and source metadata` công bố.

**Bằng chứng cần giữ.** Đối với probe 2 của `The event envelope - before, after, op and source metadata`, báo numerator, denominator và key set ở cả hai grain. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.3. The event envelope - before, after, op and source metadata: kiểm `Operation code` bằng case 3, cụ thể create, update, delete, read snapshot, truncate and message events carry different state transitions

**Mệnh đề cần kiểm.** The event envelope - before, after, op and source metadata: kiểm `Operation code` bằng case 3, cụ thể create, update, delete, read snapshot, truncate and message events carry different state transitions.

**Thiết kế phép thử cho `wiki.cdc.event-envelope`.** Trong ngữ cảnh `wiki.cdc.event-envelope`, đưa một giá trị tới đúng boundary và một giá trị vượt boundary. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The event envelope - before, after, op and source metadata` công bố.

**Bằng chứng cần giữ.** Đối với probe 3 của `The event envelope - before, after, op and source metadata`, lưu hai observed values cùng rule đã resolve. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.4. The event envelope - before, after, op and source metadata: kiểm `Source metadata` bằng case 4, cụ thể connector/source/table, transaction, log position, snapshot flag and source timestamp support ordering/lineage diagnosis

**Mệnh đề cần kiểm.** The event envelope - before, after, op and source metadata: kiểm `Source metadata` bằng case 4, cụ thể connector/source/table, transaction, log position, snapshot flag and source timestamp support ordering/lineage diagnosis.

**Thiết kế phép thử cho `wiki.cdc.event-envelope`.** Trong ngữ cảnh `wiki.cdc.event-envelope`, kill tiến trình ngay trước rồi ngay sau durable side effect. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The event envelope - before, after, op and source metadata` công bố.

**Bằng chứng cần giữ.** Đối với probe 4 của `The event envelope - before, after, op and source metadata`, lưu checkpoint, external ledger và trạng thái sau restart. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.5. The event envelope - before, after, op and source metadata: kiểm `Processing time` bằng case 5, cụ thể connector processing timestamp differs source commit/event time; their difference is a lag signal with clock caveats

**Mệnh đề cần kiểm.** The event envelope - before, after, op and source metadata: kiểm `Processing time` bằng case 5, cụ thể connector processing timestamp differs source commit/event time; their difference is a lag signal with clock caveats.

**Thiết kế phép thử cho `wiki.cdc.event-envelope`.** Trong ngữ cảnh `wiki.cdc.event-envelope`, đảo thứ tự input và concurrency nhưng giữ logical population. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The event envelope - before, after, op and source metadata` công bố.

**Bằng chứng cần giữ.** Đối với probe 5 của `The event envelope - before, after, op and source metadata`, so canonical hash và business totals giữa các thứ tự. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.6. The event envelope - before, after, op and source metadata: kiểm `Consumer contract` bằng case 6, cụ thể schema id/version, envelope version and unsupported types must be pinned; quarantine unknown op/schema instead of coercing

**Mệnh đề cần kiểm.** The event envelope - before, after, op and source metadata: kiểm `Consumer contract` bằng case 6, cụ thể schema id/version, envelope version and unsupported types must be pinned; quarantine unknown op/schema instead of coercing.

**Thiết kế phép thử cho `wiki.cdc.event-envelope`.** Trong ngữ cảnh `wiki.cdc.event-envelope`, replay cùng identity với payload giống rồi payload xung đột. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The event envelope - before, after, op and source metadata` công bố.

**Bằng chứng cần giữ.** Đối với probe 6 của `The event envelope - before, after, op and source metadata`, tách duplicate replay khỏi identity collision bằng reason code. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.7. The event envelope - before, after, op and source metadata: kiểm `Key` bằng case 7, cụ thể event key normally derives from primary/unique key or configured columns; keyless rows weaken identity/dedup/delete handling

**Mệnh đề cần kiểm.** The event envelope - before, after, op and source metadata: kiểm `Key` bằng case 7, cụ thể event key normally derives from primary/unique key or configured columns; keyless rows weaken identity/dedup/delete handling.

**Thiết kế phép thử cho `wiki.cdc.event-envelope`.** Trong ngữ cảnh `wiki.cdc.event-envelope`, thêm record tới trễ trong horizon và ngoài horizon. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The event envelope - before, after, op and source metadata` công bố.

**Bằng chứng cần giữ.** Đối với probe 7 của `The event envelope - before, after, op and source metadata`, báo accepted-late, rejected-late và oldest outstanding timestamp. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.8. The event envelope - before, after, op and source metadata: kiểm `Before and after` bằng case 8, cụ thể images depend on operation and replica identity/source configuration; null may mean unavailable, not necessarily empty row

**Mệnh đề cần kiểm.** The event envelope - before, after, op and source metadata: kiểm `Before and after` bằng case 8, cụ thể images depend on operation and replica identity/source configuration; null may mean unavailable, not necessarily empty row.

**Thiết kế phép thử cho `wiki.cdc.event-envelope`.** Trong ngữ cảnh `wiki.cdc.event-envelope`, đổi schema theo một cách tương thích rồi một cách phá vỡ semantics. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The event envelope - before, after, op and source metadata` công bố.

**Bằng chứng cần giữ.** Đối với probe 8 của `The event envelope - before, after, op and source metadata`, giữ schema diff, classification và consumer-visible result. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.9. The event envelope - before, after, op and source metadata: kiểm `Operation code` bằng case 9, cụ thể create, update, delete, read snapshot, truncate and message events carry different state transitions

**Mệnh đề cần kiểm.** The event envelope - before, after, op and source metadata: kiểm `Operation code` bằng case 9, cụ thể create, update, delete, read snapshot, truncate and message events carry different state transitions.

**Thiết kế phép thử cho `wiki.cdc.event-envelope`.** Trong ngữ cảnh `wiki.cdc.event-envelope`, tạo missing và duplicate bù nhau để count tổng không đổi. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The event envelope - before, after, op and source metadata` công bố.

**Bằng chứng cần giữ.** Đối với probe 9 của `The event envelope - before, after, op and source metadata`, so key multiset và typed hashes thay vì chỉ row count. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.10. The event envelope - before, after, op and source metadata: kiểm `Source metadata` bằng case 10, cụ thể connector/source/table, transaction, log position, snapshot flag and source timestamp support ordering/lineage diagnosis

**Mệnh đề cần kiểm.** The event envelope - before, after, op and source metadata: kiểm `Source metadata` bằng case 10, cụ thể connector/source/table, transaction, log position, snapshot flag and source timestamp support ordering/lineage diagnosis.

**Thiết kế phép thử cho `wiki.cdc.event-envelope`.** Trong ngữ cảnh `wiki.cdc.event-envelope`, cho reviewer tái hiện chỉ từ evidence package. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The event envelope - before, after, op and source metadata` công bố.

**Bằng chứng cần giữ.** Đối với probe 10 của `The event envelope - before, after, op and source metadata`, package phải đủ để người khác dựng lại decision và limitation. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.11. The event envelope - before, after, op and source metadata: kiểm `Processing time` bằng case 11, cụ thể connector processing timestamp differs source commit/event time; their difference is a lag signal with clock caveats

**Mệnh đề cần kiểm.** The event envelope - before, after, op and source metadata: kiểm `Processing time` bằng case 11, cụ thể connector processing timestamp differs source commit/event time; their difference is a lag signal with clock caveats.

**Thiết kế phép thử cho `wiki.cdc.event-envelope`.** Trong ngữ cảnh `wiki.cdc.event-envelope`, so với oracle độc lập không dùng chung query hoặc parser. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The event envelope - before, after, op and source metadata` công bố.

**Bằng chứng cần giữ.** Đối với probe 11 của `The event envelope - before, after, op and source metadata`, independent result phải khớp ở grain đã công bố. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.12. The event envelope - before, after, op and source metadata: kiểm `Consumer contract` bằng case 12, cụ thể schema id/version, envelope version and unsupported types must be pinned; quarantine unknown op/schema instead of coercing

**Mệnh đề cần kiểm.** The event envelope - before, after, op and source metadata: kiểm `Consumer contract` bằng case 12, cụ thể schema id/version, envelope version and unsupported types must be pinned; quarantine unknown op/schema instead of coercing.

**Thiết kế phép thử cho `wiki.cdc.event-envelope`.** Trong ngữ cảnh `wiki.cdc.event-envelope`, chạy scope hẹp và population đầy đủ rồi công bố phần bị loại. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The event envelope - before, after, op and source metadata` công bố.

**Bằng chứng cần giữ.** Đối với probe 12 của `The event envelope - before, after, op and source metadata`, coverage phải nêu rõ excluded nodes, partitions hoặc incidents. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.13. The event envelope - before, after, op and source metadata: kiểm `Key` bằng case 13, cụ thể event key normally derives from primary/unique key or configured columns; keyless rows weaken identity/dedup/delete handling

**Mệnh đề cần kiểm.** The event envelope - before, after, op and source metadata: kiểm `Key` bằng case 13, cụ thể event key normally derives from primary/unique key or configured columns; keyless rows weaken identity/dedup/delete handling.

**Thiết kế phép thử cho `wiki.cdc.event-envelope`.** Trong ngữ cảnh `wiki.cdc.event-envelope`, thử timezone, precision hoặc partition ở hai phía của ranh giới. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The event envelope - before, after, op and source metadata` công bố.

**Bằng chứng cần giữ.** Đối với probe 13 của `The event envelope - before, after, op and source metadata`, UTC/local interval và rounding policy phải hiện trong output. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.14. The event envelope - before, after, op and source metadata: kiểm `Before and after` bằng case 14, cụ thể images depend on operation and replica identity/source configuration; null may mean unavailable, not necessarily empty row

**Mệnh đề cần kiểm.** The event envelope - before, after, op and source metadata: kiểm `Before and after` bằng case 14, cụ thể images depend on operation and replica identity/source configuration; null may mean unavailable, not necessarily empty row.

**Thiết kế phép thử cho `wiki.cdc.event-envelope`.** Trong ngữ cảnh `wiki.cdc.event-envelope`, đổi constraint đủ lớn để quyết định phải đảo. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The event envelope - before, after, op and source metadata` công bố.

**Bằng chứng cần giữ.** Đối với probe 14 của `The event envelope - before, after, op and source metadata`, ADR phải lưu changed constraint và reversal threshold. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.15. The event envelope - before, after, op and source metadata: kiểm `Operation code` bằng case 15, cụ thể create, update, delete, read snapshot, truncate and message events carry different state transitions

**Mệnh đề cần kiểm.** The event envelope - before, after, op and source metadata: kiểm `Operation code` bằng case 15, cụ thể create, update, delete, read snapshot, truncate and message events carry different state transitions.

**Thiết kế phép thử cho `wiki.cdc.event-envelope`.** Trong ngữ cảnh `wiki.cdc.event-envelope`, chạy lại từ môi trường sạch với versions và seed đã khóa. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The event envelope - before, after, op and source metadata` công bố.

**Bằng chứng cần giữ.** Đối với probe 15 của `The event envelope - before, after, op and source metadata`, canonical result phải ổn định hoặc mọi nondeterminism phải được giải thích. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

## 8. Quy trình phản biện

1. Viết consumer-visible invariant cho `The event envelope - before, after, op and source metadata` trước khi chọn query hoặc tool.
2. Khóa grain, identity, population, time window và authoritative source.
3. Phân biệt declared configuration, executed state và published state.
4. Chạy negative control, replay hoặc changed-assumption case phù hợp.
5. Đối soát bằng oracle độc lập; công bố coverage và phần không quan sát được.
6. Gắn owner, hành động, reversal trigger và hạn review cho kết luận.

## 9. Câu hỏi tự kiểm tra

1. `The event envelope - before, after, op and source metadata: kiểm `Key` bằng case 1, cụ thể event key normally derives from primary/unique key or configured columns; keyless rows weaken identity/dedup/delete handling` thất bại đầu tiên ở boundary nào?
2. Artifact nào mạnh nhất để trả lời `The event envelope - before, after, op and source metadata: kiểm `Operation code` bằng case 3, cụ thể create, update, delete, read snapshot, truncate and message events carry different state transitions`?
3. Counterexample nhỏ nhất cho `The event envelope - before, after, op and source metadata: kiểm `Consumer contract` bằng case 6, cụ thể schema id/version, envelope version and unsupported types must be pinned; quarantine unknown op/schema instead of coercing` gồm những state nào?
4. `The event envelope - before, after, op and source metadata: kiểm `Operation code` bằng case 9, cụ thể create, update, delete, read snapshot, truncate and message events carry different state transitions` có thể xanh giả ra sao?
5. Constraint nào khiến quyết định ở `The event envelope - before, after, op and source metadata: kiểm `Before and after` bằng case 14, cụ thể images depend on operation and replica identity/source configuration; null may mean unavailable, not necessarily empty row` phải đảo?
6. Phần nào của `The event envelope - before, after, op and source metadata: kiểm `Operation code` bằng case 15, cụ thể create, update, delete, read snapshot, truncate and message events carry different state transitions` mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `The event envelope - before, after, op and source metadata` chưa chạy trên hệ thống production; nội dung là giáo trình và expected evidence.
- Hành vi phụ thuộc phiên bản, connector, scheduler, warehouse và catalog configuration phải được kiểm lại.
- Các ma trận, ladder và threshold do giáo trình tổng hợp không được gán nguyên văn cho vendor.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-DEBEZIUM-POSTGRESQL]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-DEBEZIUM-POSTGRESQL]] | Contract hoặc cơ chế liên quan trực tiếp tới `The event envelope - before, after, op and source metadata` | Đã đọc locator; cần pin version khi chạy lab |

## Key takeaways
- Envelope fields are conditional evidence under source configuration.
- Với `wiki.cdc.event-envelope`, quality của kết luận phụ thuộc identity, coverage và oracle chứ không phụ thuộc màu dashboard.
- Câu hỏi `CDC envelope fields before, after, op và source metadata phải được đọc như typed evidence thay vì JSON shape cố định ra sao?` chỉ được trả lời trong scope và version đã ghi.
- Các source IDs `src.web.debezium-postgresql` đặt ranh giới cho source fact; phần còn lại là synthesis có nhãn.
- Trước khi lab chạy, đây là note đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule — kiểm chứng `wiki.cdc.event-envelope`

> [!important] Phân loại mệnh đề
> Với `wiki.cdc.event-envelope`, sơ đồ, ví dụ và artifact về **The event envelope - before, after, op and source metadata** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.web.debezium-postgresql"] --> B["Khóa boundary"]
    B --> M["Cơ chế: The event envelope - before, after, op and source metadata"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.cdc.event-envelope` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **The event envelope - before, after, op and source metadata**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```sql
-- Verification harness for: The event envelope - before, after, op and source metadata
WITH evidence AS (
    SELECT 'wiki.cdc.event-envelope' AS concept_id,
           'boundary_declared' AS check_name, 1 AS passed
    UNION ALL
    SELECT 'wiki.cdc.event-envelope', 'independent_oracle', 1
    UNION ALL
    SELECT 'wiki.cdc.event-envelope', 'reversal_trigger_recorded', 1
)
SELECT concept_id,
       MIN(passed) AS all_hard_checks_pass,
       COUNT(*) AS evidence_items
FROM evidence
GROUP BY concept_id
HAVING MIN(passed) = 1;
```

Artifact của `wiki.cdc.event-envelope` buộc người dùng ghi boundary, oracle và reversal trigger cho **The event envelope - before, after, op and source metadata**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

### Tự kiểm tra trước khi tái sử dụng

1. Bạn có thể trả lời `CDC envelope fields before, after, op và source metadata phải được đọc như typed evidence thay vì JSON shape cố định ra sao?` bằng một câu mà không kéo thêm concept thứ hai không?
2. Source locator nào đỡ cho claim, và phần nào chỉ là synthesis trong note?
3. Observation nào khiến bạn dừng, thu hẹp hoặc đảo quyết định?
4. Artifact nào cho phép một reviewer độc lập tái hiện kết quả?

<!-- ATOMIC-EXECUTION-CAPSULE:END -->
