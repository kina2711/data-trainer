# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 19: Metadata Engineering, Catalog, Lineage and Governance
# Lesson 296: Ingestion architecture - the six-step harvest

## Mục tiêu bài học

**Năng lực cần chứng minh.** Cài đường thu thập sáu bước luỹ đẳng từ hai nguồn và chứng minh chạy lại không tạo bản ghi trùng.

**Điều kiện hoàn thành.** Đồ thị sau năm lần chạy chồng chéo khớp đồ thị của một lần chạy sạch, và bước kiểm bắt được cả hai lỗi tiêm.

> [!abstract] Câu hỏi trung tâm
> Sáu bước metadata harvest tách discovery, extraction, normalization, enrichment, emission và reconciliation ra sao?

## 1. Discover

Probe scope, permissions, versions, object counts và allow/deny rules trước crawl để biết expected population. Đừng bắt đầu bằng tên công cụ. Hãy bắt đầu bằng đối tượng được bảo vệ, boundary quan sát được và hậu quả nếu kết luận sai. Trong bài `Ingestion architecture - the six-step harvest`, câu hỏi thực dụng là: Sáu bước metadata harvest tách discovery, extraction, normalization, enrichment, emission và reconciliation ra sao? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 2. Extract

Đọc native APIs/logs/config/artifacts với cursors và rate limits; giữ raw work units hoặc snapshot để debug. Điểm khó không nằm ở cú pháp mà ở identity và scope. Hai phép đo cùng tên vẫn có thể nói về hai population hoặc hai thời điểm khác nhau. Trong bài `Ingestion architecture - the six-step harvest`, câu hỏi thực dụng là: Sáu bước metadata harvest tách discovery, extraction, normalization, enrichment, emission và reconciliation ra sao? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 3. Normalize

Map native objects vào canonical identity/types mà không xóa source-specific fields hay uncertainty. Một dashboard xanh chỉ là tín hiệu. Muốn biến nó thành bằng chứng phải giữ input, phiên bản, rule, trạng thái trước–sau và cách tính độc lập. Trong bài `Ingestion architecture - the six-step harvest`, câu hỏi thực dụng là: Sáu bước metadata harvest tách discovery, extraction, normalization, enrichment, emission và reconciliation ra sao? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 4. Enrich

Thêm ownership, domains, tags hoặc inferred relations bằng transformer có provenance riêng. Thiết kế tốt phải chịu được counterexample. Hãy chủ động tạo case sát boundary, case thiếu dữ liệu và case replay thay vì chỉ chạy happy path. Trong bài `Ingestion architecture - the six-step harvest`, câu hỏi thực dụng là: Sáu bước metadata harvest tách discovery, extraction, normalization, enrichment, emission và reconciliation ra sao? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 5. Emit

Validate schema, batch/idempotency identity và write result tới sink; partial success không được báo toàn run thành công. Chi phí vận hành thuộc contract. Một rule đúng nhưng quá đắt, quá ồn hoặc không có owner sẽ nhanh chóng bị tắt và mất tác dụng. Trong bài `Ingestion architecture - the six-step harvest`, câu hỏi thực dụng là: Sáu bước metadata harvest tách discovery, extraction, normalization, enrichment, emission và reconciliation ra sao? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 6. Reconcile

So expected/seen/emitted/rejected/deleted counts, quarantine errors và chỉ advance checkpoint khi policy cho phép. Kết luận cần có điều kiện đảo chiều. Khi volume, latency, nguồn thẩm quyền hoặc topology đổi, quyết định cũ phải được xem xét lại bằng cùng một oracle. Trong bài `Ingestion architecture - the six-step harvest`, câu hỏi thực dụng là: Sáu bước metadata harvest tách discovery, extraction, normalization, enrichment, emission và reconciliation ra sao? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 7. Ma trận kiểm chứng từng mệnh đề

Với `wiki.metadata.ingestion-six-step-harvest`, command thành công không tự chứng minh dữ liệu đúng. Protocol riêng của bài là: Chạy connector/parser/event fixture có expected entity-edge manifest, tiêm partial failure hoặc ambiguity và đo missing/extra/unknown theo producer. Mỗi probe dưới đây phải nối input boundary với failure signal và oracle có thể phản bác kết luận.

### 7.1. Ingestion architecture - the six-step harvest: kiểm `Discover` bằng case 1, cụ thể probe scope, permissions, versions, object counts và allow/deny rules trước crawl để biết expected population

**Mệnh đề cần kiểm.** Ingestion architecture - the six-step harvest: kiểm `Discover` bằng case 1, cụ thể probe scope, permissions, versions, object counts và allow/deny rules trước crawl để biết expected population.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.ingestion-six-step-harvest`, tạo positive control và negative control chỉ khác đúng một điều kiện. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Ingestion architecture - the six-step harvest` công bố.

**Bằng chứng cần giữ.** Đối với probe 1 của `Ingestion architecture - the six-step harvest`, giữ fixture, raw failing rows và lệnh tái hiện. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.2. Ingestion architecture - the six-step harvest: kiểm `Extract` bằng case 2, cụ thể đọc native apis/logs/config/artifacts với cursors và rate limits; giữ raw work units hoặc snapshot để debug

**Mệnh đề cần kiểm.** Ingestion architecture - the six-step harvest: kiểm `Extract` bằng case 2, cụ thể đọc native apis/logs/config/artifacts với cursors và rate limits; giữ raw work units hoặc snapshot để debug.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.ingestion-six-step-harvest`, đổi grain nhưng giữ tổng số dòng để lộ phép đo sai cấp. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Ingestion architecture - the six-step harvest` công bố.

**Bằng chứng cần giữ.** Đối với probe 2 của `Ingestion architecture - the six-step harvest`, báo numerator, denominator và key set ở cả hai grain. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.3. Ingestion architecture - the six-step harvest: kiểm `Normalize` bằng case 3, cụ thể map native objects vào canonical identity/types mà không xóa source-specific fields hay uncertainty

**Mệnh đề cần kiểm.** Ingestion architecture - the six-step harvest: kiểm `Normalize` bằng case 3, cụ thể map native objects vào canonical identity/types mà không xóa source-specific fields hay uncertainty.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.ingestion-six-step-harvest`, đưa một giá trị tới đúng boundary và một giá trị vượt boundary. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Ingestion architecture - the six-step harvest` công bố.

**Bằng chứng cần giữ.** Đối với probe 3 của `Ingestion architecture - the six-step harvest`, lưu hai observed values cùng rule đã resolve. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.4. Ingestion architecture - the six-step harvest: kiểm `Enrich` bằng case 4, cụ thể thêm ownership, domains, tags hoặc inferred relations bằng transformer có provenance riêng

**Mệnh đề cần kiểm.** Ingestion architecture - the six-step harvest: kiểm `Enrich` bằng case 4, cụ thể thêm ownership, domains, tags hoặc inferred relations bằng transformer có provenance riêng.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.ingestion-six-step-harvest`, kill tiến trình ngay trước rồi ngay sau durable side effect. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Ingestion architecture - the six-step harvest` công bố.

**Bằng chứng cần giữ.** Đối với probe 4 của `Ingestion architecture - the six-step harvest`, lưu checkpoint, external ledger và trạng thái sau restart. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.5. Ingestion architecture - the six-step harvest: kiểm `Emit` bằng case 5, cụ thể validate schema, batch/idempotency identity và write result tới sink; partial success không được báo toàn run thành công

**Mệnh đề cần kiểm.** Ingestion architecture - the six-step harvest: kiểm `Emit` bằng case 5, cụ thể validate schema, batch/idempotency identity và write result tới sink; partial success không được báo toàn run thành công.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.ingestion-six-step-harvest`, đảo thứ tự input và concurrency nhưng giữ logical population. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Ingestion architecture - the six-step harvest` công bố.

**Bằng chứng cần giữ.** Đối với probe 5 của `Ingestion architecture - the six-step harvest`, so canonical hash và business totals giữa các thứ tự. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.6. Ingestion architecture - the six-step harvest: kiểm `Reconcile` bằng case 6, cụ thể so expected/seen/emitted/rejected/deleted counts, quarantine errors và chỉ advance checkpoint khi policy cho phép

**Mệnh đề cần kiểm.** Ingestion architecture - the six-step harvest: kiểm `Reconcile` bằng case 6, cụ thể so expected/seen/emitted/rejected/deleted counts, quarantine errors và chỉ advance checkpoint khi policy cho phép.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.ingestion-six-step-harvest`, replay cùng identity với payload giống rồi payload xung đột. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Ingestion architecture - the six-step harvest` công bố.

**Bằng chứng cần giữ.** Đối với probe 6 của `Ingestion architecture - the six-step harvest`, tách duplicate replay khỏi identity collision bằng reason code. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.7. Ingestion architecture - the six-step harvest: kiểm `Discover` bằng case 7, cụ thể probe scope, permissions, versions, object counts và allow/deny rules trước crawl để biết expected population

**Mệnh đề cần kiểm.** Ingestion architecture - the six-step harvest: kiểm `Discover` bằng case 7, cụ thể probe scope, permissions, versions, object counts và allow/deny rules trước crawl để biết expected population.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.ingestion-six-step-harvest`, thêm record tới trễ trong horizon và ngoài horizon. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Ingestion architecture - the six-step harvest` công bố.

**Bằng chứng cần giữ.** Đối với probe 7 của `Ingestion architecture - the six-step harvest`, báo accepted-late, rejected-late và oldest outstanding timestamp. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.8. Ingestion architecture - the six-step harvest: kiểm `Extract` bằng case 8, cụ thể đọc native apis/logs/config/artifacts với cursors và rate limits; giữ raw work units hoặc snapshot để debug

**Mệnh đề cần kiểm.** Ingestion architecture - the six-step harvest: kiểm `Extract` bằng case 8, cụ thể đọc native apis/logs/config/artifacts với cursors và rate limits; giữ raw work units hoặc snapshot để debug.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.ingestion-six-step-harvest`, đổi schema theo một cách tương thích rồi một cách phá vỡ semantics. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Ingestion architecture - the six-step harvest` công bố.

**Bằng chứng cần giữ.** Đối với probe 8 của `Ingestion architecture - the six-step harvest`, giữ schema diff, classification và consumer-visible result. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.9. Ingestion architecture - the six-step harvest: kiểm `Normalize` bằng case 9, cụ thể map native objects vào canonical identity/types mà không xóa source-specific fields hay uncertainty

**Mệnh đề cần kiểm.** Ingestion architecture - the six-step harvest: kiểm `Normalize` bằng case 9, cụ thể map native objects vào canonical identity/types mà không xóa source-specific fields hay uncertainty.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.ingestion-six-step-harvest`, tạo missing và duplicate bù nhau để count tổng không đổi. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Ingestion architecture - the six-step harvest` công bố.

**Bằng chứng cần giữ.** Đối với probe 9 của `Ingestion architecture - the six-step harvest`, so key multiset và typed hashes thay vì chỉ row count. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.10. Ingestion architecture - the six-step harvest: kiểm `Enrich` bằng case 10, cụ thể thêm ownership, domains, tags hoặc inferred relations bằng transformer có provenance riêng

**Mệnh đề cần kiểm.** Ingestion architecture - the six-step harvest: kiểm `Enrich` bằng case 10, cụ thể thêm ownership, domains, tags hoặc inferred relations bằng transformer có provenance riêng.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.ingestion-six-step-harvest`, cho reviewer tái hiện chỉ từ evidence package. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Ingestion architecture - the six-step harvest` công bố.

**Bằng chứng cần giữ.** Đối với probe 10 của `Ingestion architecture - the six-step harvest`, package phải đủ để người khác dựng lại decision và limitation. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.11. Ingestion architecture - the six-step harvest: kiểm `Emit` bằng case 11, cụ thể validate schema, batch/idempotency identity và write result tới sink; partial success không được báo toàn run thành công

**Mệnh đề cần kiểm.** Ingestion architecture - the six-step harvest: kiểm `Emit` bằng case 11, cụ thể validate schema, batch/idempotency identity và write result tới sink; partial success không được báo toàn run thành công.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.ingestion-six-step-harvest`, so với oracle độc lập không dùng chung query hoặc parser. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Ingestion architecture - the six-step harvest` công bố.

**Bằng chứng cần giữ.** Đối với probe 11 của `Ingestion architecture - the six-step harvest`, independent result phải khớp ở grain đã công bố. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.12. Ingestion architecture - the six-step harvest: kiểm `Reconcile` bằng case 12, cụ thể so expected/seen/emitted/rejected/deleted counts, quarantine errors và chỉ advance checkpoint khi policy cho phép

**Mệnh đề cần kiểm.** Ingestion architecture - the six-step harvest: kiểm `Reconcile` bằng case 12, cụ thể so expected/seen/emitted/rejected/deleted counts, quarantine errors và chỉ advance checkpoint khi policy cho phép.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.ingestion-six-step-harvest`, chạy scope hẹp và population đầy đủ rồi công bố phần bị loại. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Ingestion architecture - the six-step harvest` công bố.

**Bằng chứng cần giữ.** Đối với probe 12 của `Ingestion architecture - the six-step harvest`, coverage phải nêu rõ excluded nodes, partitions hoặc incidents. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.13. Ingestion architecture - the six-step harvest: kiểm `Discover` bằng case 13, cụ thể probe scope, permissions, versions, object counts và allow/deny rules trước crawl để biết expected population

**Mệnh đề cần kiểm.** Ingestion architecture - the six-step harvest: kiểm `Discover` bằng case 13, cụ thể probe scope, permissions, versions, object counts và allow/deny rules trước crawl để biết expected population.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.ingestion-six-step-harvest`, thử timezone, precision hoặc partition ở hai phía của ranh giới. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Ingestion architecture - the six-step harvest` công bố.

**Bằng chứng cần giữ.** Đối với probe 13 của `Ingestion architecture - the six-step harvest`, UTC/local interval và rounding policy phải hiện trong output. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.14. Ingestion architecture - the six-step harvest: kiểm `Extract` bằng case 14, cụ thể đọc native apis/logs/config/artifacts với cursors và rate limits; giữ raw work units hoặc snapshot để debug

**Mệnh đề cần kiểm.** Ingestion architecture - the six-step harvest: kiểm `Extract` bằng case 14, cụ thể đọc native apis/logs/config/artifacts với cursors và rate limits; giữ raw work units hoặc snapshot để debug.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.ingestion-six-step-harvest`, đổi constraint đủ lớn để quyết định phải đảo. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Ingestion architecture - the six-step harvest` công bố.

**Bằng chứng cần giữ.** Đối với probe 14 của `Ingestion architecture - the six-step harvest`, ADR phải lưu changed constraint và reversal threshold. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.15. Ingestion architecture - the six-step harvest: kiểm `Normalize` bằng case 15, cụ thể map native objects vào canonical identity/types mà không xóa source-specific fields hay uncertainty

**Mệnh đề cần kiểm.** Ingestion architecture - the six-step harvest: kiểm `Normalize` bằng case 15, cụ thể map native objects vào canonical identity/types mà không xóa source-specific fields hay uncertainty.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.ingestion-six-step-harvest`, chạy lại từ môi trường sạch với versions và seed đã khóa. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Ingestion architecture - the six-step harvest` công bố.

**Bằng chứng cần giữ.** Đối với probe 15 của `Ingestion architecture - the six-step harvest`, canonical result phải ổn định hoặc mọi nondeterminism phải được giải thích. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

## 8. Quy trình phản biện

1. Viết consumer-visible invariant cho `Ingestion architecture - the six-step harvest` trước khi chọn query hoặc tool.
2. Khóa grain, identity, population, time window và authoritative source.
3. Phân biệt declared configuration, executed state và published state.
4. Chạy negative control, replay hoặc changed-assumption case phù hợp.
5. Đối soát bằng oracle độc lập; công bố coverage và phần không quan sát được.
6. Gắn owner, hành động, reversal trigger và hạn review cho kết luận.

## 9. Câu hỏi tự kiểm tra

1. `Ingestion architecture - the six-step harvest: kiểm `Discover` bằng case 1, cụ thể probe scope, permissions, versions, object counts và allow/deny rules trước crawl để biết expected population` thất bại đầu tiên ở boundary nào?
2. Artifact nào mạnh nhất để trả lời `Ingestion architecture - the six-step harvest: kiểm `Normalize` bằng case 3, cụ thể map native objects vào canonical identity/types mà không xóa source-specific fields hay uncertainty`?
3. Counterexample nhỏ nhất cho `Ingestion architecture - the six-step harvest: kiểm `Reconcile` bằng case 6, cụ thể so expected/seen/emitted/rejected/deleted counts, quarantine errors và chỉ advance checkpoint khi policy cho phép` gồm những state nào?
4. `Ingestion architecture - the six-step harvest: kiểm `Normalize` bằng case 9, cụ thể map native objects vào canonical identity/types mà không xóa source-specific fields hay uncertainty` có thể xanh giả ra sao?
5. Constraint nào khiến quyết định ở `Ingestion architecture - the six-step harvest: kiểm `Extract` bằng case 14, cụ thể đọc native apis/logs/config/artifacts với cursors và rate limits; giữ raw work units hoặc snapshot để debug` phải đảo?
6. Phần nào của `Ingestion architecture - the six-step harvest: kiểm `Normalize` bằng case 15, cụ thể map native objects vào canonical identity/types mà không xóa source-specific fields hay uncertainty` mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `Ingestion architecture - the six-step harvest` chưa chạy trên hệ thống production; nội dung là giáo trình và expected evidence.
- Hành vi phụ thuộc phiên bản, connector, scheduler, warehouse và catalog configuration phải được kiểm lại.
- Các ma trận, ladder và threshold do giáo trình tổng hợp không được gán nguyên văn cho vendor.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-DATAHUB-METADATA-MODEL]]
2. [[SRC-OPENLINEAGE-OVERVIEW]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-DATAHUB-METADATA-MODEL]] | Contract hoặc cơ chế liên quan trực tiếp tới `Ingestion architecture - the six-step harvest` | Đã đọc locator; cần pin version khi chạy lab |
| [[SRC-OPENLINEAGE-OVERVIEW]] | Contract hoặc cơ chế liên quan trực tiếp tới `Ingestion architecture - the six-step harvest` | Đã đọc locator; cần pin version khi chạy lab |

## Key takeaways
- Harvest an toàn tách sáu bước và reconcile từng boundary trước checkpoint.
- Với `wiki.metadata.ingestion-six-step-harvest`, quality của kết luận phụ thuộc identity, coverage và oracle chứ không phụ thuộc màu dashboard.
- Câu hỏi `Sáu bước metadata harvest tách discovery, extraction, normalization, enrichment, emission và reconciliation ra sao?` chỉ được trả lời trong scope và version đã ghi.
- Các source IDs `src.web.datahub-metadata-model, src.web.openlineage-overview` đặt ranh giới cho source fact; phần còn lại là synthesis có nhãn.
- Trước khi lab chạy, đây là note đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.
