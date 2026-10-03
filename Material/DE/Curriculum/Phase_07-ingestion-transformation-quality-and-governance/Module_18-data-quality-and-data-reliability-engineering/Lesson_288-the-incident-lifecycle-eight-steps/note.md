# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 18: Data Quality and Data Reliability Engineering
# Lesson 288: The incident lifecycle - eight steps

## Mục tiêu bài học

**Năng lực cần chứng minh.** Chạy đúng thứ tự tám bước trên một sự cố mô phỏng và nêu quyết định của từng bước.

**Điều kiện hoàn thành.** Tám bước có quyết định ghi lại theo đúng thứ tự, bằng chứng được giữ nguyên, và danh sách bên tiêu thụ lập trước khi sửa.

> [!abstract] Câu hỏi trung tâm
> Tám bước incident lifecycle giữ containment, communication, evidence và learning liền mạch như thế nào?

## 1. Detect and declare

Xác nhận user impact, severity và scope ban đầu; declare sớm với uncertainty tốt hơn xử lý ngầm. Đừng bắt đầu bằng tên công cụ. Hãy bắt đầu bằng đối tượng được bảo vệ, boundary quan sát được và hậu quả nếu kết luận sai. Trong bài `The incident lifecycle - eight steps`, câu hỏi thực dụng là: Tám bước incident lifecycle giữ containment, communication, evidence và learning liền mạch như thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 2. Assign roles

Incident commander, operations, communication và scribe có trách nhiệm tách biệt và handoff rõ. Điểm khó không nằm ở cú pháp mà ở identity và scope. Hai phép đo cùng tên vẫn có thể nói về hai population hoặc hai thời điểm khác nhau. Trong bài `The incident lifecycle - eight steps`, câu hỏi thực dụng là: Tám bước incident lifecycle giữ containment, communication, evidence và learning liền mạch như thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 3. Contain

Dừng bleeding bằng pause publication, rollback, quarantine hoặc serve-last-known-good nhưng bảo toàn evidence. Một dashboard xanh chỉ là tín hiệu. Muốn biến nó thành bằng chứng phải giữ input, phiên bản, rule, trạng thái trước–sau và cách tính độc lập. Trong bài `The incident lifecycle - eight steps`, câu hỏi thực dụng là: Tám bước incident lifecycle giữ containment, communication, evidence và learning liền mạch như thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 4. Diagnose

Dựng timeline và hypotheses từ facts; phân biệt trigger, contributing conditions và latent controls. Thiết kế tốt phải chịu được counterexample. Hãy chủ động tạo case sát boundary, case thiếu dữ liệu và case replay thay vì chỉ chạy happy path. Trong bài `The incident lifecycle - eight steps`, câu hỏi thực dụng là: Tám bước incident lifecycle giữ containment, communication, evidence và learning liền mạch như thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 5. Recover and validate

Khôi phục service/data rồi đối soát completeness, correctness và downstream restatement trước close. Chi phí vận hành thuộc contract. Một rule đúng nhưng quá đắt, quá ồn hoặc không có owner sẽ nhanh chóng bị tắt và mất tác dụng. Trong bài `The incident lifecycle - eight steps`, câu hỏi thực dụng là: Tám bước incident lifecycle giữ containment, communication, evidence và learning liền mạch như thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 6. Communicate learn follow-up

Cập nhật stakeholders, viết blameless postmortem, giao action owner/deadline và kiểm hiệu quả sau triển khai. Kết luận cần có điều kiện đảo chiều. Khi volume, latency, nguồn thẩm quyền hoặc topology đổi, quyết định cũ phải được xem xét lại bằng cùng một oracle. Trong bài `The incident lifecycle - eight steps`, câu hỏi thực dụng là: Tám bước incident lifecycle giữ containment, communication, evidence và learning liền mạch như thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 7. Ma trận kiểm chứng từng mệnh đề

Với `wiki.data-quality.incident-lifecycle`, command thành công không tự chứng minh dữ liệu đúng. Protocol riêng của bài là: Replay một cửa sổ có good/bad events hoặc incident state, tính lại metric độc lập và kiểm action/routing đúng policy. Mỗi probe dưới đây phải nối input boundary với failure signal và oracle có thể phản bác kết luận.

### 7.1. The incident lifecycle - eight steps: kiểm `Detect and declare` bằng case 1, cụ thể xác nhận user impact, severity và scope ban đầu; declare sớm với uncertainty tốt hơn xử lý ngầm

**Mệnh đề cần kiểm.** The incident lifecycle - eight steps: kiểm `Detect and declare` bằng case 1, cụ thể xác nhận user impact, severity và scope ban đầu; declare sớm với uncertainty tốt hơn xử lý ngầm.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.data-quality.incident-lifecycle`, tạo positive control và negative control chỉ khác đúng một điều kiện. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The incident lifecycle - eight steps` công bố.

**Bằng chứng cần giữ.** Đối với probe 1 của `The incident lifecycle - eight steps`, giữ fixture, raw failing rows và lệnh tái hiện. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.2. The incident lifecycle - eight steps: kiểm `Assign roles` bằng case 2, cụ thể incident commander, operations, communication và scribe có trách nhiệm tách biệt và handoff rõ

**Mệnh đề cần kiểm.** The incident lifecycle - eight steps: kiểm `Assign roles` bằng case 2, cụ thể incident commander, operations, communication và scribe có trách nhiệm tách biệt và handoff rõ.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.data-quality.incident-lifecycle`, đổi grain nhưng giữ tổng số dòng để lộ phép đo sai cấp. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The incident lifecycle - eight steps` công bố.

**Bằng chứng cần giữ.** Đối với probe 2 của `The incident lifecycle - eight steps`, báo numerator, denominator và key set ở cả hai grain. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.3. The incident lifecycle - eight steps: kiểm `Contain` bằng case 3, cụ thể dừng bleeding bằng pause publication, rollback, quarantine hoặc serve-last-known-good nhưng bảo toàn evidence

**Mệnh đề cần kiểm.** The incident lifecycle - eight steps: kiểm `Contain` bằng case 3, cụ thể dừng bleeding bằng pause publication, rollback, quarantine hoặc serve-last-known-good nhưng bảo toàn evidence.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.data-quality.incident-lifecycle`, đưa một giá trị tới đúng boundary và một giá trị vượt boundary. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The incident lifecycle - eight steps` công bố.

**Bằng chứng cần giữ.** Đối với probe 3 của `The incident lifecycle - eight steps`, lưu hai observed values cùng rule đã resolve. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.4. The incident lifecycle - eight steps: kiểm `Diagnose` bằng case 4, cụ thể dựng timeline và hypotheses từ facts; phân biệt trigger, contributing conditions và latent controls

**Mệnh đề cần kiểm.** The incident lifecycle - eight steps: kiểm `Diagnose` bằng case 4, cụ thể dựng timeline và hypotheses từ facts; phân biệt trigger, contributing conditions và latent controls.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.data-quality.incident-lifecycle`, kill tiến trình ngay trước rồi ngay sau durable side effect. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The incident lifecycle - eight steps` công bố.

**Bằng chứng cần giữ.** Đối với probe 4 của `The incident lifecycle - eight steps`, lưu checkpoint, external ledger và trạng thái sau restart. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.5. The incident lifecycle - eight steps: kiểm `Recover and validate` bằng case 5, cụ thể khôi phục service/data rồi đối soát completeness, correctness và downstream restatement trước close

**Mệnh đề cần kiểm.** The incident lifecycle - eight steps: kiểm `Recover and validate` bằng case 5, cụ thể khôi phục service/data rồi đối soát completeness, correctness và downstream restatement trước close.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.data-quality.incident-lifecycle`, đảo thứ tự input và concurrency nhưng giữ logical population. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The incident lifecycle - eight steps` công bố.

**Bằng chứng cần giữ.** Đối với probe 5 của `The incident lifecycle - eight steps`, so canonical hash và business totals giữa các thứ tự. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.6. The incident lifecycle - eight steps: kiểm `Communicate learn follow-up` bằng case 6, cụ thể cập nhật stakeholders, viết blameless postmortem, giao action owner/deadline và kiểm hiệu quả sau triển khai

**Mệnh đề cần kiểm.** The incident lifecycle - eight steps: kiểm `Communicate learn follow-up` bằng case 6, cụ thể cập nhật stakeholders, viết blameless postmortem, giao action owner/deadline và kiểm hiệu quả sau triển khai.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.data-quality.incident-lifecycle`, replay cùng identity với payload giống rồi payload xung đột. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The incident lifecycle - eight steps` công bố.

**Bằng chứng cần giữ.** Đối với probe 6 của `The incident lifecycle - eight steps`, tách duplicate replay khỏi identity collision bằng reason code. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.7. The incident lifecycle - eight steps: kiểm `Detect and declare` bằng case 7, cụ thể xác nhận user impact, severity và scope ban đầu; declare sớm với uncertainty tốt hơn xử lý ngầm

**Mệnh đề cần kiểm.** The incident lifecycle - eight steps: kiểm `Detect and declare` bằng case 7, cụ thể xác nhận user impact, severity và scope ban đầu; declare sớm với uncertainty tốt hơn xử lý ngầm.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.data-quality.incident-lifecycle`, thêm record tới trễ trong horizon và ngoài horizon. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The incident lifecycle - eight steps` công bố.

**Bằng chứng cần giữ.** Đối với probe 7 của `The incident lifecycle - eight steps`, báo accepted-late, rejected-late và oldest outstanding timestamp. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.8. The incident lifecycle - eight steps: kiểm `Assign roles` bằng case 8, cụ thể incident commander, operations, communication và scribe có trách nhiệm tách biệt và handoff rõ

**Mệnh đề cần kiểm.** The incident lifecycle - eight steps: kiểm `Assign roles` bằng case 8, cụ thể incident commander, operations, communication và scribe có trách nhiệm tách biệt và handoff rõ.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.data-quality.incident-lifecycle`, đổi schema theo một cách tương thích rồi một cách phá vỡ semantics. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The incident lifecycle - eight steps` công bố.

**Bằng chứng cần giữ.** Đối với probe 8 của `The incident lifecycle - eight steps`, giữ schema diff, classification và consumer-visible result. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.9. The incident lifecycle - eight steps: kiểm `Contain` bằng case 9, cụ thể dừng bleeding bằng pause publication, rollback, quarantine hoặc serve-last-known-good nhưng bảo toàn evidence

**Mệnh đề cần kiểm.** The incident lifecycle - eight steps: kiểm `Contain` bằng case 9, cụ thể dừng bleeding bằng pause publication, rollback, quarantine hoặc serve-last-known-good nhưng bảo toàn evidence.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.data-quality.incident-lifecycle`, tạo missing và duplicate bù nhau để count tổng không đổi. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The incident lifecycle - eight steps` công bố.

**Bằng chứng cần giữ.** Đối với probe 9 của `The incident lifecycle - eight steps`, so key multiset và typed hashes thay vì chỉ row count. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.10. The incident lifecycle - eight steps: kiểm `Diagnose` bằng case 10, cụ thể dựng timeline và hypotheses từ facts; phân biệt trigger, contributing conditions và latent controls

**Mệnh đề cần kiểm.** The incident lifecycle - eight steps: kiểm `Diagnose` bằng case 10, cụ thể dựng timeline và hypotheses từ facts; phân biệt trigger, contributing conditions và latent controls.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.data-quality.incident-lifecycle`, cho reviewer tái hiện chỉ từ evidence package. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The incident lifecycle - eight steps` công bố.

**Bằng chứng cần giữ.** Đối với probe 10 của `The incident lifecycle - eight steps`, package phải đủ để người khác dựng lại decision và limitation. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.11. The incident lifecycle - eight steps: kiểm `Recover and validate` bằng case 11, cụ thể khôi phục service/data rồi đối soát completeness, correctness và downstream restatement trước close

**Mệnh đề cần kiểm.** The incident lifecycle - eight steps: kiểm `Recover and validate` bằng case 11, cụ thể khôi phục service/data rồi đối soát completeness, correctness và downstream restatement trước close.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.data-quality.incident-lifecycle`, so với oracle độc lập không dùng chung query hoặc parser. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The incident lifecycle - eight steps` công bố.

**Bằng chứng cần giữ.** Đối với probe 11 của `The incident lifecycle - eight steps`, independent result phải khớp ở grain đã công bố. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.12. The incident lifecycle - eight steps: kiểm `Communicate learn follow-up` bằng case 12, cụ thể cập nhật stakeholders, viết blameless postmortem, giao action owner/deadline và kiểm hiệu quả sau triển khai

**Mệnh đề cần kiểm.** The incident lifecycle - eight steps: kiểm `Communicate learn follow-up` bằng case 12, cụ thể cập nhật stakeholders, viết blameless postmortem, giao action owner/deadline và kiểm hiệu quả sau triển khai.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.data-quality.incident-lifecycle`, chạy scope hẹp và population đầy đủ rồi công bố phần bị loại. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The incident lifecycle - eight steps` công bố.

**Bằng chứng cần giữ.** Đối với probe 12 của `The incident lifecycle - eight steps`, coverage phải nêu rõ excluded nodes, partitions hoặc incidents. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.13. The incident lifecycle - eight steps: kiểm `Detect and declare` bằng case 13, cụ thể xác nhận user impact, severity và scope ban đầu; declare sớm với uncertainty tốt hơn xử lý ngầm

**Mệnh đề cần kiểm.** The incident lifecycle - eight steps: kiểm `Detect and declare` bằng case 13, cụ thể xác nhận user impact, severity và scope ban đầu; declare sớm với uncertainty tốt hơn xử lý ngầm.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.data-quality.incident-lifecycle`, thử timezone, precision hoặc partition ở hai phía của ranh giới. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The incident lifecycle - eight steps` công bố.

**Bằng chứng cần giữ.** Đối với probe 13 của `The incident lifecycle - eight steps`, UTC/local interval và rounding policy phải hiện trong output. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.14. The incident lifecycle - eight steps: kiểm `Assign roles` bằng case 14, cụ thể incident commander, operations, communication và scribe có trách nhiệm tách biệt và handoff rõ

**Mệnh đề cần kiểm.** The incident lifecycle - eight steps: kiểm `Assign roles` bằng case 14, cụ thể incident commander, operations, communication và scribe có trách nhiệm tách biệt và handoff rõ.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.data-quality.incident-lifecycle`, đổi constraint đủ lớn để quyết định phải đảo. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The incident lifecycle - eight steps` công bố.

**Bằng chứng cần giữ.** Đối với probe 14 của `The incident lifecycle - eight steps`, ADR phải lưu changed constraint và reversal threshold. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.15. The incident lifecycle - eight steps: kiểm `Contain` bằng case 15, cụ thể dừng bleeding bằng pause publication, rollback, quarantine hoặc serve-last-known-good nhưng bảo toàn evidence

**Mệnh đề cần kiểm.** The incident lifecycle - eight steps: kiểm `Contain` bằng case 15, cụ thể dừng bleeding bằng pause publication, rollback, quarantine hoặc serve-last-known-good nhưng bảo toàn evidence.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.data-quality.incident-lifecycle`, chạy lại từ môi trường sạch với versions và seed đã khóa. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The incident lifecycle - eight steps` công bố.

**Bằng chứng cần giữ.** Đối với probe 15 của `The incident lifecycle - eight steps`, canonical result phải ổn định hoặc mọi nondeterminism phải được giải thích. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

## 8. Quy trình phản biện

1. Viết consumer-visible invariant cho `The incident lifecycle - eight steps` trước khi chọn query hoặc tool.
2. Khóa grain, identity, population, time window và authoritative source.
3. Phân biệt declared configuration, executed state và published state.
4. Chạy negative control, replay hoặc changed-assumption case phù hợp.
5. Đối soát bằng oracle độc lập; công bố coverage và phần không quan sát được.
6. Gắn owner, hành động, reversal trigger và hạn review cho kết luận.

## 9. Câu hỏi tự kiểm tra

1. `The incident lifecycle - eight steps: kiểm `Detect and declare` bằng case 1, cụ thể xác nhận user impact, severity và scope ban đầu; declare sớm với uncertainty tốt hơn xử lý ngầm` thất bại đầu tiên ở boundary nào?
2. Artifact nào mạnh nhất để trả lời `The incident lifecycle - eight steps: kiểm `Contain` bằng case 3, cụ thể dừng bleeding bằng pause publication, rollback, quarantine hoặc serve-last-known-good nhưng bảo toàn evidence`?
3. Counterexample nhỏ nhất cho `The incident lifecycle - eight steps: kiểm `Communicate learn follow-up` bằng case 6, cụ thể cập nhật stakeholders, viết blameless postmortem, giao action owner/deadline và kiểm hiệu quả sau triển khai` gồm những state nào?
4. `The incident lifecycle - eight steps: kiểm `Contain` bằng case 9, cụ thể dừng bleeding bằng pause publication, rollback, quarantine hoặc serve-last-known-good nhưng bảo toàn evidence` có thể xanh giả ra sao?
5. Constraint nào khiến quyết định ở `The incident lifecycle - eight steps: kiểm `Assign roles` bằng case 14, cụ thể incident commander, operations, communication và scribe có trách nhiệm tách biệt và handoff rõ` phải đảo?
6. Phần nào của `The incident lifecycle - eight steps: kiểm `Contain` bằng case 15, cụ thể dừng bleeding bằng pause publication, rollback, quarantine hoặc serve-last-known-good nhưng bảo toàn evidence` mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `The incident lifecycle - eight steps` chưa chạy trên hệ thống production; nội dung là giáo trình và expected evidence.
- Hành vi phụ thuộc phiên bản, connector, scheduler, warehouse và catalog configuration phải được kiểm lại.
- Các ma trận, ladder và threshold do giáo trình tổng hợp không được gán nguyên văn cho vendor.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-GOOGLE-SRE-INCIDENT-MANAGEMENT]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-GOOGLE-SRE-INCIDENT-MANAGEMENT]] | Contract hoặc cơ chế liên quan trực tiếp tới `The incident lifecycle - eight steps` | Đã đọc locator; cần pin version khi chạy lab |

## Key takeaways
- Incident lifecycle cần roles, live state, containment, validated recovery và follow-up.
- Với `wiki.data-quality.incident-lifecycle`, quality của kết luận phụ thuộc identity, coverage và oracle chứ không phụ thuộc màu dashboard.
- Câu hỏi `Tám bước incident lifecycle giữ containment, communication, evidence và learning liền mạch như thế nào?` chỉ được trả lời trong scope và version đã ghi.
- Các source IDs `src.web.google-sre-incident-management` đặt ranh giới cho source fact; phần còn lại là synthesis có nhãn.
- Trước khi lab chạy, đây là note đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.
