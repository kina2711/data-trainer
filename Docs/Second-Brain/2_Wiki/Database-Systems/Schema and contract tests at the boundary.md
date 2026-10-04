---
note_id: wiki.data-quality.schema-contract-boundary
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
primary_question: Schema test và semantic contract test khác nhau thế nào tại producer-consumer boundary?
source_ids:
  - src.web.gx-data-quality-use-cases
  - src.web.gx-expectations
aliases: [Schema and contract tests at the boundary]
tags: [wiki/data-quality, data-quality, reliability, testing, incidents]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/166-schema-and-contract-tests-at-the-boundary.md
relationships:
  builds_on: [wiki.data-quality.layered-controls]
  prerequisite_of: [wiki.data-quality.row-aggregate-relationship-tests]
  related_to: []

---
# Schema and contract tests at the boundary

> [!abstract] Câu hỏi trung tâm
> Schema test và semantic contract test khác nhau thế nào tại producer-consumer boundary?

## 1. Structural schema

Columns, nested fields, types, nullability và order chỉ là cấu trúc; parse được chưa chứng minh meaning đúng. Đừng bắt đầu bằng tên công cụ. Hãy bắt đầu bằng đối tượng được bảo vệ, boundary quan sát được và hậu quả nếu kết luận sai. Trong bài `Schema and contract tests at the boundary`, câu hỏi thực dụng là: Schema test và semantic contract test khác nhau thế nào tại producer-consumer boundary? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 2. Semantic contract

Grain, key, units, timezone, enum meaning, update/deletion policy và compatibility tạo consumer contract. Điểm khó không nằm ở cú pháp mà ở identity và scope. Hai phép đo cùng tên vẫn có thể nói về hai population hoặc hai thời điểm khác nhau. Trong bài `Schema and contract tests at the boundary`, câu hỏi thực dụng là: Schema test và semantic contract test khác nhau thế nào tại producer-consumer boundary? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 3. Compatibility direction

Backward và forward compatibility phụ thuộc ai đọc phiên bản nào; additive field không luôn an toàn với strict consumers. Một dashboard xanh chỉ là tín hiệu. Muốn biến nó thành bằng chứng phải giữ input, phiên bản, rule, trạng thái trước-sau và cách tính độc lập. Trong bài `Schema and contract tests at the boundary`, câu hỏi thực dụng là: Schema test và semantic contract test khác nhau thế nào tại producer-consumer boundary? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 4. Boundary fixtures

Giữ golden valid payload, missing/extra field, widened/narrowed type, null transition và changed-meaning case. Thiết kế tốt phải chịu được counterexample. Hãy chủ động tạo case sát boundary, case thiếu dữ liệu và case replay thay vì chỉ chạy happy path. Trong bài `Schema and contract tests at the boundary`, câu hỏi thực dụng là: Schema test và semantic contract test khác nhau thế nào tại producer-consumer boundary? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 5. Enforcement modes

Observe, warn, quarantine và block cần rollout policy; block đột ngột có thể gây outage lớn hơn defect. Chi phí vận hành thuộc contract. Một rule đúng nhưng quá đắt, quá ồn hoặc không có owner sẽ nhanh chóng bị tắt và mất tác dụng. Trong bài `Schema and contract tests at the boundary`, câu hỏi thực dụng là: Schema test và semantic contract test khác nhau thế nào tại producer-consumer boundary? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 6. Contract evidence

Consumer inventory, schema diff, compatibility decision, owner approval và migration window phải cùng version. Kết luận cần có điều kiện đảo chiều. Khi volume, latency, nguồn thẩm quyền hoặc topology đổi, quyết định cũ phải được xem xét lại bằng cùng một oracle. Trong bài `Schema and contract tests at the boundary`, câu hỏi thực dụng là: Schema test và semantic contract test khác nhau thế nào tại producer-consumer boundary? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 7. Ma trận kiểm chứng từng mệnh đề

Với `wiki.data-quality.schema-contract-boundary`, command thành công không tự chứng minh dữ liệu đúng. Protocol riêng của bài là: Tạo positive/negative fixture ở đúng grain, chạy rule đã version hóa và so failing keys/metrics với một oracle độc lập. Mỗi probe dưới đây phải nối input boundary với failure signal và oracle có thể phản bác kết luận.

### 7.1. Schema and contract tests at the boundary: kiểm `Structural schema` bằng case 1, cụ thể columns, nested fields, types, nullability và order chỉ là cấu trúc; parse được chưa chứng minh meaning đúng

**Mệnh đề cần kiểm.** Schema and contract tests at the boundary: kiểm `Structural schema` bằng case 1, cụ thể columns, nested fields, types, nullability và order chỉ là cấu trúc; parse được chưa chứng minh meaning đúng.

**Thiết kế phép thử cho `wiki.data-quality.schema-contract-boundary`.** Trong ngữ cảnh `wiki.data-quality.schema-contract-boundary`, tạo positive control và negative control chỉ khác đúng một điều kiện. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Schema and contract tests at the boundary` công bố.

**Bằng chứng cần giữ.** Đối với probe 1 của `Schema and contract tests at the boundary`, giữ fixture, raw failing rows và lệnh tái hiện. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.2. Schema and contract tests at the boundary: kiểm `Semantic contract` bằng case 2, cụ thể grain, key, units, timezone, enum meaning, update/deletion policy và compatibility tạo consumer contract

**Mệnh đề cần kiểm.** Schema and contract tests at the boundary: kiểm `Semantic contract` bằng case 2, cụ thể grain, key, units, timezone, enum meaning, update/deletion policy và compatibility tạo consumer contract.

**Thiết kế phép thử cho `wiki.data-quality.schema-contract-boundary`.** Trong ngữ cảnh `wiki.data-quality.schema-contract-boundary`, đổi grain nhưng giữ tổng số dòng để lộ phép đo sai cấp. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Schema and contract tests at the boundary` công bố.

**Bằng chứng cần giữ.** Đối với probe 2 của `Schema and contract tests at the boundary`, báo numerator, denominator và key set ở cả hai grain. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.3. Schema and contract tests at the boundary: kiểm `Compatibility direction` bằng case 3, cụ thể backward và forward compatibility phụ thuộc ai đọc phiên bản nào; additive field không luôn an toàn với strict consumers

**Mệnh đề cần kiểm.** Schema and contract tests at the boundary: kiểm `Compatibility direction` bằng case 3, cụ thể backward và forward compatibility phụ thuộc ai đọc phiên bản nào; additive field không luôn an toàn với strict consumers.

**Thiết kế phép thử cho `wiki.data-quality.schema-contract-boundary`.** Trong ngữ cảnh `wiki.data-quality.schema-contract-boundary`, đưa một giá trị tới đúng boundary và một giá trị vượt boundary. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Schema and contract tests at the boundary` công bố.

**Bằng chứng cần giữ.** Đối với probe 3 của `Schema and contract tests at the boundary`, lưu hai observed values cùng rule đã resolve. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.4. Schema and contract tests at the boundary: kiểm `Boundary fixtures` bằng case 4, cụ thể giữ golden valid payload, missing/extra field, widened/narrowed type, null transition và changed-meaning case

**Mệnh đề cần kiểm.** Schema and contract tests at the boundary: kiểm `Boundary fixtures` bằng case 4, cụ thể giữ golden valid payload, missing/extra field, widened/narrowed type, null transition và changed-meaning case.

**Thiết kế phép thử cho `wiki.data-quality.schema-contract-boundary`.** Trong ngữ cảnh `wiki.data-quality.schema-contract-boundary`, kill tiến trình ngay trước rồi ngay sau durable side effect. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Schema and contract tests at the boundary` công bố.

**Bằng chứng cần giữ.** Đối với probe 4 của `Schema and contract tests at the boundary`, lưu checkpoint, external ledger và trạng thái sau restart. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.5. Schema and contract tests at the boundary: kiểm `Enforcement modes` bằng case 5, cụ thể observe, warn, quarantine và block cần rollout policy; block đột ngột có thể gây outage lớn hơn defect

**Mệnh đề cần kiểm.** Schema and contract tests at the boundary: kiểm `Enforcement modes` bằng case 5, cụ thể observe, warn, quarantine và block cần rollout policy; block đột ngột có thể gây outage lớn hơn defect.

**Thiết kế phép thử cho `wiki.data-quality.schema-contract-boundary`.** Trong ngữ cảnh `wiki.data-quality.schema-contract-boundary`, đảo thứ tự input và concurrency nhưng giữ logical population. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Schema and contract tests at the boundary` công bố.

**Bằng chứng cần giữ.** Đối với probe 5 của `Schema and contract tests at the boundary`, so canonical hash và business totals giữa các thứ tự. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.6. Schema and contract tests at the boundary: kiểm `Contract evidence` bằng case 6, cụ thể consumer inventory, schema diff, compatibility decision, owner approval và migration window phải cùng version

**Mệnh đề cần kiểm.** Schema and contract tests at the boundary: kiểm `Contract evidence` bằng case 6, cụ thể consumer inventory, schema diff, compatibility decision, owner approval và migration window phải cùng version.

**Thiết kế phép thử cho `wiki.data-quality.schema-contract-boundary`.** Trong ngữ cảnh `wiki.data-quality.schema-contract-boundary`, replay cùng identity với payload giống rồi payload xung đột. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Schema and contract tests at the boundary` công bố.

**Bằng chứng cần giữ.** Đối với probe 6 của `Schema and contract tests at the boundary`, tách duplicate replay khỏi identity collision bằng reason code. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.7. Schema and contract tests at the boundary: kiểm `Structural schema` bằng case 7, cụ thể columns, nested fields, types, nullability và order chỉ là cấu trúc; parse được chưa chứng minh meaning đúng

**Mệnh đề cần kiểm.** Schema and contract tests at the boundary: kiểm `Structural schema` bằng case 7, cụ thể columns, nested fields, types, nullability và order chỉ là cấu trúc; parse được chưa chứng minh meaning đúng.

**Thiết kế phép thử cho `wiki.data-quality.schema-contract-boundary`.** Trong ngữ cảnh `wiki.data-quality.schema-contract-boundary`, thêm record tới trễ trong horizon và ngoài horizon. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Schema and contract tests at the boundary` công bố.

**Bằng chứng cần giữ.** Đối với probe 7 của `Schema and contract tests at the boundary`, báo accepted-late, rejected-late và oldest outstanding timestamp. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.8. Schema and contract tests at the boundary: kiểm `Semantic contract` bằng case 8, cụ thể grain, key, units, timezone, enum meaning, update/deletion policy và compatibility tạo consumer contract

**Mệnh đề cần kiểm.** Schema and contract tests at the boundary: kiểm `Semantic contract` bằng case 8, cụ thể grain, key, units, timezone, enum meaning, update/deletion policy và compatibility tạo consumer contract.

**Thiết kế phép thử cho `wiki.data-quality.schema-contract-boundary`.** Trong ngữ cảnh `wiki.data-quality.schema-contract-boundary`, đổi schema theo một cách tương thích rồi một cách phá vỡ semantics. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Schema and contract tests at the boundary` công bố.

**Bằng chứng cần giữ.** Đối với probe 8 của `Schema and contract tests at the boundary`, giữ schema diff, classification và consumer-visible result. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.9. Schema and contract tests at the boundary: kiểm `Compatibility direction` bằng case 9, cụ thể backward và forward compatibility phụ thuộc ai đọc phiên bản nào; additive field không luôn an toàn với strict consumers

**Mệnh đề cần kiểm.** Schema and contract tests at the boundary: kiểm `Compatibility direction` bằng case 9, cụ thể backward và forward compatibility phụ thuộc ai đọc phiên bản nào; additive field không luôn an toàn với strict consumers.

**Thiết kế phép thử cho `wiki.data-quality.schema-contract-boundary`.** Trong ngữ cảnh `wiki.data-quality.schema-contract-boundary`, tạo missing và duplicate bù nhau để count tổng không đổi. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Schema and contract tests at the boundary` công bố.

**Bằng chứng cần giữ.** Đối với probe 9 của `Schema and contract tests at the boundary`, so key multiset và typed hashes thay vì chỉ row count. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.10. Schema and contract tests at the boundary: kiểm `Boundary fixtures` bằng case 10, cụ thể giữ golden valid payload, missing/extra field, widened/narrowed type, null transition và changed-meaning case

**Mệnh đề cần kiểm.** Schema and contract tests at the boundary: kiểm `Boundary fixtures` bằng case 10, cụ thể giữ golden valid payload, missing/extra field, widened/narrowed type, null transition và changed-meaning case.

**Thiết kế phép thử cho `wiki.data-quality.schema-contract-boundary`.** Trong ngữ cảnh `wiki.data-quality.schema-contract-boundary`, cho reviewer tái hiện chỉ từ evidence package. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Schema and contract tests at the boundary` công bố.

**Bằng chứng cần giữ.** Đối với probe 10 của `Schema and contract tests at the boundary`, package phải đủ để người khác dựng lại decision và limitation. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.11. Schema and contract tests at the boundary: kiểm `Enforcement modes` bằng case 11, cụ thể observe, warn, quarantine và block cần rollout policy; block đột ngột có thể gây outage lớn hơn defect

**Mệnh đề cần kiểm.** Schema and contract tests at the boundary: kiểm `Enforcement modes` bằng case 11, cụ thể observe, warn, quarantine và block cần rollout policy; block đột ngột có thể gây outage lớn hơn defect.

**Thiết kế phép thử cho `wiki.data-quality.schema-contract-boundary`.** Trong ngữ cảnh `wiki.data-quality.schema-contract-boundary`, so với oracle độc lập không dùng chung query hoặc parser. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Schema and contract tests at the boundary` công bố.

**Bằng chứng cần giữ.** Đối với probe 11 của `Schema and contract tests at the boundary`, independent result phải khớp ở grain đã công bố. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.12. Schema and contract tests at the boundary: kiểm `Contract evidence` bằng case 12, cụ thể consumer inventory, schema diff, compatibility decision, owner approval và migration window phải cùng version

**Mệnh đề cần kiểm.** Schema and contract tests at the boundary: kiểm `Contract evidence` bằng case 12, cụ thể consumer inventory, schema diff, compatibility decision, owner approval và migration window phải cùng version.

**Thiết kế phép thử cho `wiki.data-quality.schema-contract-boundary`.** Trong ngữ cảnh `wiki.data-quality.schema-contract-boundary`, chạy scope hẹp và population đầy đủ rồi công bố phần bị loại. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Schema and contract tests at the boundary` công bố.

**Bằng chứng cần giữ.** Đối với probe 12 của `Schema and contract tests at the boundary`, coverage phải nêu rõ excluded nodes, partitions hoặc incidents. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.13. Schema and contract tests at the boundary: kiểm `Structural schema` bằng case 13, cụ thể columns, nested fields, types, nullability và order chỉ là cấu trúc; parse được chưa chứng minh meaning đúng

**Mệnh đề cần kiểm.** Schema and contract tests at the boundary: kiểm `Structural schema` bằng case 13, cụ thể columns, nested fields, types, nullability và order chỉ là cấu trúc; parse được chưa chứng minh meaning đúng.

**Thiết kế phép thử cho `wiki.data-quality.schema-contract-boundary`.** Trong ngữ cảnh `wiki.data-quality.schema-contract-boundary`, thử timezone, precision hoặc partition ở hai phía của ranh giới. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Schema and contract tests at the boundary` công bố.

**Bằng chứng cần giữ.** Đối với probe 13 của `Schema and contract tests at the boundary`, UTC/local interval và rounding policy phải hiện trong output. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.14. Schema and contract tests at the boundary: kiểm `Semantic contract` bằng case 14, cụ thể grain, key, units, timezone, enum meaning, update/deletion policy và compatibility tạo consumer contract

**Mệnh đề cần kiểm.** Schema and contract tests at the boundary: kiểm `Semantic contract` bằng case 14, cụ thể grain, key, units, timezone, enum meaning, update/deletion policy và compatibility tạo consumer contract.

**Thiết kế phép thử cho `wiki.data-quality.schema-contract-boundary`.** Trong ngữ cảnh `wiki.data-quality.schema-contract-boundary`, đổi constraint đủ lớn để quyết định phải đảo. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Schema and contract tests at the boundary` công bố.

**Bằng chứng cần giữ.** Đối với probe 14 của `Schema and contract tests at the boundary`, ADR phải lưu changed constraint và reversal threshold. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.15. Schema and contract tests at the boundary: kiểm `Compatibility direction` bằng case 15, cụ thể backward và forward compatibility phụ thuộc ai đọc phiên bản nào; additive field không luôn an toàn với strict consumers

**Mệnh đề cần kiểm.** Schema and contract tests at the boundary: kiểm `Compatibility direction` bằng case 15, cụ thể backward và forward compatibility phụ thuộc ai đọc phiên bản nào; additive field không luôn an toàn với strict consumers.

**Thiết kế phép thử cho `wiki.data-quality.schema-contract-boundary`.** Trong ngữ cảnh `wiki.data-quality.schema-contract-boundary`, chạy lại từ môi trường sạch với versions và seed đã khóa. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Schema and contract tests at the boundary` công bố.

**Bằng chứng cần giữ.** Đối với probe 15 của `Schema and contract tests at the boundary`, canonical result phải ổn định hoặc mọi nondeterminism phải được giải thích. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

## 8. Quy trình phản biện

1. Viết consumer-visible invariant cho `Schema and contract tests at the boundary` trước khi chọn query hoặc tool.
2. Khóa grain, identity, population, time window và authoritative source.
3. Phân biệt declared configuration, executed state và published state.
4. Chạy negative control, replay hoặc changed-assumption case phù hợp.
5. Đối soát bằng oracle độc lập; công bố coverage và phần không quan sát được.
6. Gắn owner, hành động, reversal trigger và hạn review cho kết luận.

## 9. Câu hỏi tự kiểm tra

1. `Schema and contract tests at the boundary: kiểm `Structural schema` bằng case 1, cụ thể columns, nested fields, types, nullability và order chỉ là cấu trúc; parse được chưa chứng minh meaning đúng` thất bại đầu tiên ở boundary nào?
2. Artifact nào mạnh nhất để trả lời `Schema and contract tests at the boundary: kiểm `Compatibility direction` bằng case 3, cụ thể backward và forward compatibility phụ thuộc ai đọc phiên bản nào; additive field không luôn an toàn với strict consumers`?
3. Counterexample nhỏ nhất cho `Schema and contract tests at the boundary: kiểm `Contract evidence` bằng case 6, cụ thể consumer inventory, schema diff, compatibility decision, owner approval và migration window phải cùng version` gồm những state nào?
4. `Schema and contract tests at the boundary: kiểm `Compatibility direction` bằng case 9, cụ thể backward và forward compatibility phụ thuộc ai đọc phiên bản nào; additive field không luôn an toàn với strict consumers` có thể xanh giả ra sao?
5. Constraint nào khiến quyết định ở `Schema and contract tests at the boundary: kiểm `Semantic contract` bằng case 14, cụ thể grain, key, units, timezone, enum meaning, update/deletion policy và compatibility tạo consumer contract` phải đảo?
6. Phần nào của `Schema and contract tests at the boundary: kiểm `Compatibility direction` bằng case 15, cụ thể backward và forward compatibility phụ thuộc ai đọc phiên bản nào; additive field không luôn an toàn với strict consumers` mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `Schema and contract tests at the boundary` chưa chạy trên hệ thống production; nội dung là giáo trình và expected evidence.
- Hành vi phụ thuộc phiên bản, connector, scheduler, warehouse và catalog configuration phải được kiểm lại.
- Các ma trận, ladder và threshold do giáo trình tổng hợp không được gán nguyên văn cho vendor.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-GX-DATA-QUALITY-USE-CASES]]
2. [[SRC-GX-EXPECTATIONS]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-GX-DATA-QUALITY-USE-CASES]] | Contract hoặc cơ chế liên quan trực tiếp tới `Schema and contract tests at the boundary` | Đã đọc locator; cần pin version khi chạy lab |
| [[SRC-GX-EXPECTATIONS]] | Contract hoặc cơ chế liên quan trực tiếp tới `Schema and contract tests at the boundary` | Đã đọc locator; cần pin version khi chạy lab |

## Key takeaways
- Schema là cấu trúc; contract còn sở hữu semantics và compatibility.
- Với `wiki.data-quality.schema-contract-boundary`, quality của kết luận phụ thuộc identity, coverage và oracle chứ không phụ thuộc màu dashboard.
- Câu hỏi `Schema test và semantic contract test khác nhau thế nào tại producer-consumer boundary?` chỉ được trả lời trong scope và version đã ghi.
- Các source IDs `src.web.gx-data-quality-use-cases, src.web.gx-expectations` đặt ranh giới cho source fact; phần còn lại là synthesis có nhãn.
- Trước khi lab chạy, đây là note đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule: kiểm chứng `wiki.data-quality.schema-contract-boundary`

> [!important] Phân loại mệnh đề
> Với `wiki.data-quality.schema-contract-boundary`, sơ đồ, ví dụ và artifact về **Schema and contract tests at the boundary** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.web.gx-data-quality-use-cases"] --> B["Khóa boundary"]
    B --> M["Cơ chế: Schema and contract tests at the boundary"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.data-quality.schema-contract-boundary` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **Schema and contract tests at the boundary**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```sql
-- Verification harness for: Schema and contract tests at the boundary
WITH evidence AS (
    SELECT 'wiki.data-quality.schema-contract-boundary' AS concept_id,
           'boundary_declared' AS check_name, 1 AS passed
    UNION ALL
    SELECT 'wiki.data-quality.schema-contract-boundary', 'independent_oracle', 1
    UNION ALL
    SELECT 'wiki.data-quality.schema-contract-boundary', 'reversal_trigger_recorded', 1
)
SELECT concept_id,
       MIN(passed) AS all_hard_checks_pass,
       COUNT(*) AS evidence_items
FROM evidence
GROUP BY concept_id
HAVING MIN(passed) = 1;
```

Artifact của `wiki.data-quality.schema-contract-boundary` buộc người dùng ghi boundary, oracle và reversal trigger cho **Schema and contract tests at the boundary**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

### Tự kiểm tra trước khi tái sử dụng

1. Bạn có thể trả lời `Schema test và semantic contract test khác nhau thế nào tại producer-consumer boundary?` bằng một câu mà không kéo thêm concept thứ hai không?
2. Source locator nào đỡ cho claim, và phần nào chỉ là synthesis trong note?
3. Observation nào khiến bạn dừng, thu hẹp hoặc đảo quyết định?
4. Artifact nào cho phép một reviewer độc lập tái hiện kết quả?

<!-- ATOMIC-EXECUTION-CAPSULE:END -->
