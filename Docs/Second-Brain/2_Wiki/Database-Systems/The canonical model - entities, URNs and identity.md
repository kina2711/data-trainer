---
note_id: wiki.metadata.canonical-entities-urns
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
primary_question: Canonical metadata model giữ identity ổn định xuyên connectors, environments và rename bằng cách nào?
source_ids:
  - src.web.datahub-metadata-model
aliases: [The canonical model - entities, URNs and identity]
tags: [wiki/metadata, metadata, catalog, lineage, governance]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/182-the-canonical-model-entities-urns-and-identity.md
relationships:
  builds_on: [wiki.metadata.taxonomy-authority]
  prerequisite_of: [wiki.metadata.relationships-versioning-lifecycle]
  related_to: []

---
# The canonical model - entities, URNs and identity

> [!abstract] Câu hỏi trung tâm
> Canonical metadata model giữ identity ổn định xuyên connectors, environments và rename bằng cách nào?

## 1. Entity boundary

Dataset, field, job, run, dashboard, glossary term và owner là entity types có lifecycle khác nhau. Đừng bắt đầu bằng tên công cụ. Hãy bắt đầu bằng đối tượng được bảo vệ, boundary quan sát được và hậu quả nếu kết luận sai. Trong bài `The canonical model - entities, URNs and identity`, câu hỏi thực dụng là: Canonical metadata model giữ identity ổn định xuyên connectors, environments và rename bằng cách nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 2. Key aspect

Identity dùng platform/instance/environment/native key ổn định; display name và path không mặc nhiên là key. Điểm khó không nằm ở cú pháp mà ở identity và scope. Hai phép đo cùng tên vẫn có thể nói về hai population hoặc hai thời điểm khác nhau. Trong bài `The canonical model - entities, URNs and identity`, câu hỏi thực dụng là: Canonical metadata model giữ identity ổn định xuyên connectors, environments và rename bằng cách nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 3. URN construction

URN cần canonical encoding, namespace rules, case policy và validation để connectors không tạo twins. Một dashboard xanh chỉ là tín hiệu. Muốn biến nó thành bằng chứng phải giữ input, phiên bản, rule, trạng thái trước–sau và cách tính độc lập. Trong bài `The canonical model - entities, URNs and identity`, câu hỏi thực dụng là: Canonical metadata model giữ identity ổn định xuyên connectors, environments và rename bằng cách nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 4. Aspect separation

Schema, ownership, tags, status và usage là aspects có authority/update cadence riêng quanh cùng entity. Thiết kế tốt phải chịu được counterexample. Hãy chủ động tạo case sát boundary, case thiếu dữ liệu và case replay thay vì chỉ chạy happy path. Trong bài `The canonical model - entities, URNs and identity`, câu hỏi thực dụng là: Canonical metadata model giữ identity ổn định xuyên connectors, environments và rename bằng cách nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 5. Alias and mapping

Cross-system equivalence cần explicit mapping với evidence/confidence; fuzzy name match không merge tự động. Chi phí vận hành thuộc contract. Một rule đúng nhưng quá đắt, quá ồn hoặc không có owner sẽ nhanh chóng bị tắt và mất tác dụng. Trong bài `The canonical model - entities, URNs and identity`, câu hỏi thực dụng là: Canonical metadata model giữ identity ổn định xuyên connectors, environments và rename bằng cách nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 6. Identity tests

Round-trip serialization, collision, rename, environment split và deleted/recreated object phải có expected identity. Kết luận cần có điều kiện đảo chiều. Khi volume, latency, nguồn thẩm quyền hoặc topology đổi, quyết định cũ phải được xem xét lại bằng cùng một oracle. Trong bài `The canonical model - entities, URNs and identity`, câu hỏi thực dụng là: Canonical metadata model giữ identity ổn định xuyên connectors, environments và rename bằng cách nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 7. Ma trận kiểm chứng từng mệnh đề

Với `wiki.metadata.canonical-entities-urns`, command thành công không tự chứng minh dữ liệu đúng. Protocol riêng của bài là: Dựng fixture có identity và version rõ, inject defect/lifecycle event rồi so canonical graph hoặc recovery state với expected manifest. Mỗi probe dưới đây phải nối input boundary với failure signal và oracle có thể phản bác kết luận.

### 7.1. The canonical model - entities, URNs and identity: kiểm `Entity boundary` bằng case 1, cụ thể dataset, field, job, run, dashboard, glossary term và owner là entity types có lifecycle khác nhau

**Mệnh đề cần kiểm.** The canonical model - entities, URNs and identity: kiểm `Entity boundary` bằng case 1, cụ thể dataset, field, job, run, dashboard, glossary term và owner là entity types có lifecycle khác nhau.

**Thiết kế phép thử cho `wiki.metadata.canonical-entities-urns`.** Trong ngữ cảnh `wiki.metadata.canonical-entities-urns`, tạo positive control và negative control chỉ khác đúng một điều kiện. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The canonical model - entities, URNs and identity` công bố.

**Bằng chứng cần giữ.** Đối với probe 1 của `The canonical model - entities, URNs and identity`, giữ fixture, raw failing rows và lệnh tái hiện. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.2. The canonical model - entities, URNs and identity: kiểm `Key aspect` bằng case 2, cụ thể identity dùng platform/instance/environment/native key ổn định; display name và path không mặc nhiên là key

**Mệnh đề cần kiểm.** The canonical model - entities, URNs and identity: kiểm `Key aspect` bằng case 2, cụ thể identity dùng platform/instance/environment/native key ổn định; display name và path không mặc nhiên là key.

**Thiết kế phép thử cho `wiki.metadata.canonical-entities-urns`.** Trong ngữ cảnh `wiki.metadata.canonical-entities-urns`, đổi grain nhưng giữ tổng số dòng để lộ phép đo sai cấp. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The canonical model - entities, URNs and identity` công bố.

**Bằng chứng cần giữ.** Đối với probe 2 của `The canonical model - entities, URNs and identity`, báo numerator, denominator và key set ở cả hai grain. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.3. The canonical model - entities, URNs and identity: kiểm `URN construction` bằng case 3, cụ thể urn cần canonical encoding, namespace rules, case policy và validation để connectors không tạo twins

**Mệnh đề cần kiểm.** The canonical model - entities, URNs and identity: kiểm `URN construction` bằng case 3, cụ thể urn cần canonical encoding, namespace rules, case policy và validation để connectors không tạo twins.

**Thiết kế phép thử cho `wiki.metadata.canonical-entities-urns`.** Trong ngữ cảnh `wiki.metadata.canonical-entities-urns`, đưa một giá trị tới đúng boundary và một giá trị vượt boundary. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The canonical model - entities, URNs and identity` công bố.

**Bằng chứng cần giữ.** Đối với probe 3 của `The canonical model - entities, URNs and identity`, lưu hai observed values cùng rule đã resolve. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.4. The canonical model - entities, URNs and identity: kiểm `Aspect separation` bằng case 4, cụ thể schema, ownership, tags, status và usage là aspects có authority/update cadence riêng quanh cùng entity

**Mệnh đề cần kiểm.** The canonical model - entities, URNs and identity: kiểm `Aspect separation` bằng case 4, cụ thể schema, ownership, tags, status và usage là aspects có authority/update cadence riêng quanh cùng entity.

**Thiết kế phép thử cho `wiki.metadata.canonical-entities-urns`.** Trong ngữ cảnh `wiki.metadata.canonical-entities-urns`, kill tiến trình ngay trước rồi ngay sau durable side effect. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The canonical model - entities, URNs and identity` công bố.

**Bằng chứng cần giữ.** Đối với probe 4 của `The canonical model - entities, URNs and identity`, lưu checkpoint, external ledger và trạng thái sau restart. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.5. The canonical model - entities, URNs and identity: kiểm `Alias and mapping` bằng case 5, cụ thể cross-system equivalence cần explicit mapping với evidence/confidence; fuzzy name match không merge tự động

**Mệnh đề cần kiểm.** The canonical model - entities, URNs and identity: kiểm `Alias and mapping` bằng case 5, cụ thể cross-system equivalence cần explicit mapping với evidence/confidence; fuzzy name match không merge tự động.

**Thiết kế phép thử cho `wiki.metadata.canonical-entities-urns`.** Trong ngữ cảnh `wiki.metadata.canonical-entities-urns`, đảo thứ tự input và concurrency nhưng giữ logical population. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The canonical model - entities, URNs and identity` công bố.

**Bằng chứng cần giữ.** Đối với probe 5 của `The canonical model - entities, URNs and identity`, so canonical hash và business totals giữa các thứ tự. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.6. The canonical model - entities, URNs and identity: kiểm `Identity tests` bằng case 6, cụ thể round-trip serialization, collision, rename, environment split và deleted/recreated object phải có expected identity

**Mệnh đề cần kiểm.** The canonical model - entities, URNs and identity: kiểm `Identity tests` bằng case 6, cụ thể round-trip serialization, collision, rename, environment split và deleted/recreated object phải có expected identity.

**Thiết kế phép thử cho `wiki.metadata.canonical-entities-urns`.** Trong ngữ cảnh `wiki.metadata.canonical-entities-urns`, replay cùng identity với payload giống rồi payload xung đột. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The canonical model - entities, URNs and identity` công bố.

**Bằng chứng cần giữ.** Đối với probe 6 của `The canonical model - entities, URNs and identity`, tách duplicate replay khỏi identity collision bằng reason code. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.7. The canonical model - entities, URNs and identity: kiểm `Entity boundary` bằng case 7, cụ thể dataset, field, job, run, dashboard, glossary term và owner là entity types có lifecycle khác nhau

**Mệnh đề cần kiểm.** The canonical model - entities, URNs and identity: kiểm `Entity boundary` bằng case 7, cụ thể dataset, field, job, run, dashboard, glossary term và owner là entity types có lifecycle khác nhau.

**Thiết kế phép thử cho `wiki.metadata.canonical-entities-urns`.** Trong ngữ cảnh `wiki.metadata.canonical-entities-urns`, thêm record tới trễ trong horizon và ngoài horizon. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The canonical model - entities, URNs and identity` công bố.

**Bằng chứng cần giữ.** Đối với probe 7 của `The canonical model - entities, URNs and identity`, báo accepted-late, rejected-late và oldest outstanding timestamp. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.8. The canonical model - entities, URNs and identity: kiểm `Key aspect` bằng case 8, cụ thể identity dùng platform/instance/environment/native key ổn định; display name và path không mặc nhiên là key

**Mệnh đề cần kiểm.** The canonical model - entities, URNs and identity: kiểm `Key aspect` bằng case 8, cụ thể identity dùng platform/instance/environment/native key ổn định; display name và path không mặc nhiên là key.

**Thiết kế phép thử cho `wiki.metadata.canonical-entities-urns`.** Trong ngữ cảnh `wiki.metadata.canonical-entities-urns`, đổi schema theo một cách tương thích rồi một cách phá vỡ semantics. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The canonical model - entities, URNs and identity` công bố.

**Bằng chứng cần giữ.** Đối với probe 8 của `The canonical model - entities, URNs and identity`, giữ schema diff, classification và consumer-visible result. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.9. The canonical model - entities, URNs and identity: kiểm `URN construction` bằng case 9, cụ thể urn cần canonical encoding, namespace rules, case policy và validation để connectors không tạo twins

**Mệnh đề cần kiểm.** The canonical model - entities, URNs and identity: kiểm `URN construction` bằng case 9, cụ thể urn cần canonical encoding, namespace rules, case policy và validation để connectors không tạo twins.

**Thiết kế phép thử cho `wiki.metadata.canonical-entities-urns`.** Trong ngữ cảnh `wiki.metadata.canonical-entities-urns`, tạo missing và duplicate bù nhau để count tổng không đổi. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The canonical model - entities, URNs and identity` công bố.

**Bằng chứng cần giữ.** Đối với probe 9 của `The canonical model - entities, URNs and identity`, so key multiset và typed hashes thay vì chỉ row count. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.10. The canonical model - entities, URNs and identity: kiểm `Aspect separation` bằng case 10, cụ thể schema, ownership, tags, status và usage là aspects có authority/update cadence riêng quanh cùng entity

**Mệnh đề cần kiểm.** The canonical model - entities, URNs and identity: kiểm `Aspect separation` bằng case 10, cụ thể schema, ownership, tags, status và usage là aspects có authority/update cadence riêng quanh cùng entity.

**Thiết kế phép thử cho `wiki.metadata.canonical-entities-urns`.** Trong ngữ cảnh `wiki.metadata.canonical-entities-urns`, cho reviewer tái hiện chỉ từ evidence package. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The canonical model - entities, URNs and identity` công bố.

**Bằng chứng cần giữ.** Đối với probe 10 của `The canonical model - entities, URNs and identity`, package phải đủ để người khác dựng lại decision và limitation. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.11. The canonical model - entities, URNs and identity: kiểm `Alias and mapping` bằng case 11, cụ thể cross-system equivalence cần explicit mapping với evidence/confidence; fuzzy name match không merge tự động

**Mệnh đề cần kiểm.** The canonical model - entities, URNs and identity: kiểm `Alias and mapping` bằng case 11, cụ thể cross-system equivalence cần explicit mapping với evidence/confidence; fuzzy name match không merge tự động.

**Thiết kế phép thử cho `wiki.metadata.canonical-entities-urns`.** Trong ngữ cảnh `wiki.metadata.canonical-entities-urns`, so với oracle độc lập không dùng chung query hoặc parser. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The canonical model - entities, URNs and identity` công bố.

**Bằng chứng cần giữ.** Đối với probe 11 của `The canonical model - entities, URNs and identity`, independent result phải khớp ở grain đã công bố. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.12. The canonical model - entities, URNs and identity: kiểm `Identity tests` bằng case 12, cụ thể round-trip serialization, collision, rename, environment split và deleted/recreated object phải có expected identity

**Mệnh đề cần kiểm.** The canonical model - entities, URNs and identity: kiểm `Identity tests` bằng case 12, cụ thể round-trip serialization, collision, rename, environment split và deleted/recreated object phải có expected identity.

**Thiết kế phép thử cho `wiki.metadata.canonical-entities-urns`.** Trong ngữ cảnh `wiki.metadata.canonical-entities-urns`, chạy scope hẹp và population đầy đủ rồi công bố phần bị loại. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The canonical model - entities, URNs and identity` công bố.

**Bằng chứng cần giữ.** Đối với probe 12 của `The canonical model - entities, URNs and identity`, coverage phải nêu rõ excluded nodes, partitions hoặc incidents. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.13. The canonical model - entities, URNs and identity: kiểm `Entity boundary` bằng case 13, cụ thể dataset, field, job, run, dashboard, glossary term và owner là entity types có lifecycle khác nhau

**Mệnh đề cần kiểm.** The canonical model - entities, URNs and identity: kiểm `Entity boundary` bằng case 13, cụ thể dataset, field, job, run, dashboard, glossary term và owner là entity types có lifecycle khác nhau.

**Thiết kế phép thử cho `wiki.metadata.canonical-entities-urns`.** Trong ngữ cảnh `wiki.metadata.canonical-entities-urns`, thử timezone, precision hoặc partition ở hai phía của ranh giới. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The canonical model - entities, URNs and identity` công bố.

**Bằng chứng cần giữ.** Đối với probe 13 của `The canonical model - entities, URNs and identity`, UTC/local interval và rounding policy phải hiện trong output. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.14. The canonical model - entities, URNs and identity: kiểm `Key aspect` bằng case 14, cụ thể identity dùng platform/instance/environment/native key ổn định; display name và path không mặc nhiên là key

**Mệnh đề cần kiểm.** The canonical model - entities, URNs and identity: kiểm `Key aspect` bằng case 14, cụ thể identity dùng platform/instance/environment/native key ổn định; display name và path không mặc nhiên là key.

**Thiết kế phép thử cho `wiki.metadata.canonical-entities-urns`.** Trong ngữ cảnh `wiki.metadata.canonical-entities-urns`, đổi constraint đủ lớn để quyết định phải đảo. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The canonical model - entities, URNs and identity` công bố.

**Bằng chứng cần giữ.** Đối với probe 14 của `The canonical model - entities, URNs and identity`, ADR phải lưu changed constraint và reversal threshold. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.15. The canonical model - entities, URNs and identity: kiểm `URN construction` bằng case 15, cụ thể urn cần canonical encoding, namespace rules, case policy và validation để connectors không tạo twins

**Mệnh đề cần kiểm.** The canonical model - entities, URNs and identity: kiểm `URN construction` bằng case 15, cụ thể urn cần canonical encoding, namespace rules, case policy và validation để connectors không tạo twins.

**Thiết kế phép thử cho `wiki.metadata.canonical-entities-urns`.** Trong ngữ cảnh `wiki.metadata.canonical-entities-urns`, chạy lại từ môi trường sạch với versions và seed đã khóa. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The canonical model - entities, URNs and identity` công bố.

**Bằng chứng cần giữ.** Đối với probe 15 của `The canonical model - entities, URNs and identity`, canonical result phải ổn định hoặc mọi nondeterminism phải được giải thích. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

## 8. Quy trình phản biện

1. Viết consumer-visible invariant cho `The canonical model - entities, URNs and identity` trước khi chọn query hoặc tool.
2. Khóa grain, identity, population, time window và authoritative source.
3. Phân biệt declared configuration, executed state và published state.
4. Chạy negative control, replay hoặc changed-assumption case phù hợp.
5. Đối soát bằng oracle độc lập; công bố coverage và phần không quan sát được.
6. Gắn owner, hành động, reversal trigger và hạn review cho kết luận.

## 9. Câu hỏi tự kiểm tra

1. `The canonical model - entities, URNs and identity: kiểm `Entity boundary` bằng case 1, cụ thể dataset, field, job, run, dashboard, glossary term và owner là entity types có lifecycle khác nhau` thất bại đầu tiên ở boundary nào?
2. Artifact nào mạnh nhất để trả lời `The canonical model - entities, URNs and identity: kiểm `URN construction` bằng case 3, cụ thể urn cần canonical encoding, namespace rules, case policy và validation để connectors không tạo twins`?
3. Counterexample nhỏ nhất cho `The canonical model - entities, URNs and identity: kiểm `Identity tests` bằng case 6, cụ thể round-trip serialization, collision, rename, environment split và deleted/recreated object phải có expected identity` gồm những state nào?
4. `The canonical model - entities, URNs and identity: kiểm `URN construction` bằng case 9, cụ thể urn cần canonical encoding, namespace rules, case policy và validation để connectors không tạo twins` có thể xanh giả ra sao?
5. Constraint nào khiến quyết định ở `The canonical model - entities, URNs and identity: kiểm `Key aspect` bằng case 14, cụ thể identity dùng platform/instance/environment/native key ổn định; display name và path không mặc nhiên là key` phải đảo?
6. Phần nào của `The canonical model - entities, URNs and identity: kiểm `URN construction` bằng case 15, cụ thể urn cần canonical encoding, namespace rules, case policy và validation để connectors không tạo twins` mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `The canonical model - entities, URNs and identity` chưa chạy trên hệ thống production; nội dung là giáo trình và expected evidence.
- Hành vi phụ thuộc phiên bản, connector, scheduler, warehouse và catalog configuration phải được kiểm lại.
- Các ma trận, ladder và threshold do giáo trình tổng hợp không được gán nguyên văn cho vendor.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-DATAHUB-METADATA-MODEL]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-DATAHUB-METADATA-MODEL]] | Contract hoặc cơ chế liên quan trực tiếp tới `The canonical model - entities, URNs and identity` | Đã đọc locator; cần pin version khi chạy lab |

## Key takeaways
- Stable identity nằm ở canonical key, không ở display path.
- Với `wiki.metadata.canonical-entities-urns`, quality của kết luận phụ thuộc identity, coverage và oracle chứ không phụ thuộc màu dashboard.
- Câu hỏi `Canonical metadata model giữ identity ổn định xuyên connectors, environments và rename bằng cách nào?` chỉ được trả lời trong scope và version đã ghi.
- Các source IDs `src.web.datahub-metadata-model` đặt ranh giới cho source fact; phần còn lại là synthesis có nhãn.
- Trước khi lab chạy, đây là note đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule — kiểm chứng `wiki.metadata.canonical-entities-urns`

> [!important] Phân loại mệnh đề
> Với `wiki.metadata.canonical-entities-urns`, sơ đồ, ví dụ và artifact về **The canonical model - entities, URNs and identity** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.web.datahub-metadata-model"] --> B["Khóa boundary"]
    B --> M["Cơ chế: The canonical model - entities, URNs and identity"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.metadata.canonical-entities-urns` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **The canonical model - entities, URNs and identity**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```sql
-- Verification harness for: The canonical model - entities, URNs and identity
WITH evidence AS (
    SELECT 'wiki.metadata.canonical-entities-urns' AS concept_id,
           'boundary_declared' AS check_name, 1 AS passed
    UNION ALL
    SELECT 'wiki.metadata.canonical-entities-urns', 'independent_oracle', 1
    UNION ALL
    SELECT 'wiki.metadata.canonical-entities-urns', 'reversal_trigger_recorded', 1
)
SELECT concept_id,
       MIN(passed) AS all_hard_checks_pass,
       COUNT(*) AS evidence_items
FROM evidence
GROUP BY concept_id
HAVING MIN(passed) = 1;
```

Artifact của `wiki.metadata.canonical-entities-urns` buộc người dùng ghi boundary, oracle và reversal trigger cho **The canonical model - entities, URNs and identity**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

### Tự kiểm tra trước khi tái sử dụng

1. Bạn có thể trả lời `Canonical metadata model giữ identity ổn định xuyên connectors, environments và rename bằng cách nào?` bằng một câu mà không kéo thêm concept thứ hai không?
2. Source locator nào đỡ cho claim, và phần nào chỉ là synthesis trong note?
3. Observation nào khiến bạn dừng, thu hẹp hoặc đảo quyết định?
4. Artifact nào cho phép một reviewer độc lập tái hiện kết quả?

<!-- ATOMIC-EXECUTION-CAPSULE:END -->
