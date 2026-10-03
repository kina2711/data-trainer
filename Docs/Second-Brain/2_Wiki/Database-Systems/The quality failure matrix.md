---
note_id: wiki.data-quality.failure-matrix
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
primary_question: Quality failure matrix nối defect class, detection layer, containment và owner như thế nào?
source_ids:
  - src.web.gx-expectations
  - src.web.google-sre-incident-management
aliases: [The quality failure matrix]
tags: [wiki/data-quality, data-quality, reliability, testing, incidents]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/179-the-quality-failure-matrix.md
relationships:
  builds_on: []
  prerequisite_of: [wiki.data-quality.capstone-seeded-defects]
  related_to: []

---
# The quality failure matrix

> [!abstract] Câu hỏi trung tâm
> Quality failure matrix nối defect class, detection layer, containment và owner như thế nào?

## 1. Matrix axes

Hàng là defect classes; cột gồm detection point, signal, impact, containment, recovery, owner và evidence. Đừng bắt đầu bằng tên công cụ. Hãy bắt đầu bằng đối tượng được bảo vệ, boundary quan sát được và hậu quả nếu kết luận sai. Trong bài `The quality failure matrix`, câu hỏi thực dụng là: Quality failure matrix nối defect class, detection layer, containment và owner như thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 2. Defect classes

Thiếu, extra, duplicate, invalid, inconsistent, stale, inaccurate và broken relationship cần tách vì recovery khác. Điểm khó không nằm ở cú pháp mà ở identity và scope. Hai phép đo cùng tên vẫn có thể nói về hai population hoặc hai thời điểm khác nhau. Trong bài `The quality failure matrix`, câu hỏi thực dụng là: Quality failure matrix nối defect class, detection layer, containment và owner như thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 3. Detection mapping

Mỗi defect có earliest viable control và consumer-visible monitor; không giả định một test bắt mọi biến thể. Một dashboard xanh chỉ là tín hiệu. Muốn biến nó thành bằng chứng phải giữ input, phiên bản, rule, trạng thái trước–sau và cách tính độc lập. Trong bài `The quality failure matrix`, câu hỏi thực dụng là: Quality failure matrix nối defect class, detection layer, containment và owner như thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 4. Containment mapping

Quarantine, block publish, serve stale, rollback hay notify phụ thuộc harm và recoverability. Thiết kế tốt phải chịu được counterexample. Hãy chủ động tạo case sát boundary, case thiếu dữ liệu và case replay thay vì chỉ chạy happy path. Trong bài `The quality failure matrix`, câu hỏi thực dụng là: Quality failure matrix nối defect class, detection layer, containment và owner như thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 5. Ownership

Producer, platform, domain steward và consumer có responsibilities khác; one owner cho decision nhưng contributors rõ. Chi phí vận hành thuộc contract. Một rule đúng nhưng quá đắt, quá ồn hoặc không có owner sẽ nhanh chóng bị tắt và mất tác dụng. Trong bài `The quality failure matrix`, câu hỏi thực dụng là: Quality failure matrix nối defect class, detection layer, containment và owner như thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 6. Gap analysis

Ô trống, unknown coverage và untested recovery trở thành backlog có risk score, không tô xanh bằng assumption. Kết luận cần có điều kiện đảo chiều. Khi volume, latency, nguồn thẩm quyền hoặc topology đổi, quyết định cũ phải được xem xét lại bằng cùng một oracle. Trong bài `The quality failure matrix`, câu hỏi thực dụng là: Quality failure matrix nối defect class, detection layer, containment và owner như thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 7. Ma trận kiểm chứng từng mệnh đề

Với `wiki.data-quality.failure-matrix`, command thành công không tự chứng minh dữ liệu đúng. Protocol riêng của bài là: Dựng fixture có identity và version rõ, inject defect/lifecycle event rồi so canonical graph hoặc recovery state với expected manifest. Mỗi probe dưới đây phải nối input boundary với failure signal và oracle có thể phản bác kết luận.

### 7.1. The quality failure matrix: kiểm `Matrix axes` bằng case 1, cụ thể hàng là defect classes; cột gồm detection point, signal, impact, containment, recovery, owner và evidence

**Mệnh đề cần kiểm.** The quality failure matrix: kiểm `Matrix axes` bằng case 1, cụ thể hàng là defect classes; cột gồm detection point, signal, impact, containment, recovery, owner và evidence.

**Thiết kế phép thử cho `wiki.data-quality.failure-matrix`.** Trong ngữ cảnh `wiki.data-quality.failure-matrix`, tạo positive control và negative control chỉ khác đúng một điều kiện. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The quality failure matrix` công bố.

**Bằng chứng cần giữ.** Đối với probe 1 của `The quality failure matrix`, giữ fixture, raw failing rows và lệnh tái hiện. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.2. The quality failure matrix: kiểm `Defect classes` bằng case 2, cụ thể thiếu, extra, duplicate, invalid, inconsistent, stale, inaccurate và broken relationship cần tách vì recovery khác

**Mệnh đề cần kiểm.** The quality failure matrix: kiểm `Defect classes` bằng case 2, cụ thể thiếu, extra, duplicate, invalid, inconsistent, stale, inaccurate và broken relationship cần tách vì recovery khác.

**Thiết kế phép thử cho `wiki.data-quality.failure-matrix`.** Trong ngữ cảnh `wiki.data-quality.failure-matrix`, đổi grain nhưng giữ tổng số dòng để lộ phép đo sai cấp. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The quality failure matrix` công bố.

**Bằng chứng cần giữ.** Đối với probe 2 của `The quality failure matrix`, báo numerator, denominator và key set ở cả hai grain. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.3. The quality failure matrix: kiểm `Detection mapping` bằng case 3, cụ thể mỗi defect có earliest viable control và consumer-visible monitor; không giả định một test bắt mọi biến thể

**Mệnh đề cần kiểm.** The quality failure matrix: kiểm `Detection mapping` bằng case 3, cụ thể mỗi defect có earliest viable control và consumer-visible monitor; không giả định một test bắt mọi biến thể.

**Thiết kế phép thử cho `wiki.data-quality.failure-matrix`.** Trong ngữ cảnh `wiki.data-quality.failure-matrix`, đưa một giá trị tới đúng boundary và một giá trị vượt boundary. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The quality failure matrix` công bố.

**Bằng chứng cần giữ.** Đối với probe 3 của `The quality failure matrix`, lưu hai observed values cùng rule đã resolve. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.4. The quality failure matrix: kiểm `Containment mapping` bằng case 4, cụ thể quarantine, block publish, serve stale, rollback hay notify phụ thuộc harm và recoverability

**Mệnh đề cần kiểm.** The quality failure matrix: kiểm `Containment mapping` bằng case 4, cụ thể quarantine, block publish, serve stale, rollback hay notify phụ thuộc harm và recoverability.

**Thiết kế phép thử cho `wiki.data-quality.failure-matrix`.** Trong ngữ cảnh `wiki.data-quality.failure-matrix`, kill tiến trình ngay trước rồi ngay sau durable side effect. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The quality failure matrix` công bố.

**Bằng chứng cần giữ.** Đối với probe 4 của `The quality failure matrix`, lưu checkpoint, external ledger và trạng thái sau restart. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.5. The quality failure matrix: kiểm `Ownership` bằng case 5, cụ thể producer, platform, domain steward và consumer có responsibilities khác; one owner cho decision nhưng contributors rõ

**Mệnh đề cần kiểm.** The quality failure matrix: kiểm `Ownership` bằng case 5, cụ thể producer, platform, domain steward và consumer có responsibilities khác; one owner cho decision nhưng contributors rõ.

**Thiết kế phép thử cho `wiki.data-quality.failure-matrix`.** Trong ngữ cảnh `wiki.data-quality.failure-matrix`, đảo thứ tự input và concurrency nhưng giữ logical population. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The quality failure matrix` công bố.

**Bằng chứng cần giữ.** Đối với probe 5 của `The quality failure matrix`, so canonical hash và business totals giữa các thứ tự. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.6. The quality failure matrix: kiểm `Gap analysis` bằng case 6, cụ thể ô trống, unknown coverage và untested recovery trở thành backlog có risk score, không tô xanh bằng assumption

**Mệnh đề cần kiểm.** The quality failure matrix: kiểm `Gap analysis` bằng case 6, cụ thể ô trống, unknown coverage và untested recovery trở thành backlog có risk score, không tô xanh bằng assumption.

**Thiết kế phép thử cho `wiki.data-quality.failure-matrix`.** Trong ngữ cảnh `wiki.data-quality.failure-matrix`, replay cùng identity với payload giống rồi payload xung đột. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The quality failure matrix` công bố.

**Bằng chứng cần giữ.** Đối với probe 6 của `The quality failure matrix`, tách duplicate replay khỏi identity collision bằng reason code. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.7. The quality failure matrix: kiểm `Matrix axes` bằng case 7, cụ thể hàng là defect classes; cột gồm detection point, signal, impact, containment, recovery, owner và evidence

**Mệnh đề cần kiểm.** The quality failure matrix: kiểm `Matrix axes` bằng case 7, cụ thể hàng là defect classes; cột gồm detection point, signal, impact, containment, recovery, owner và evidence.

**Thiết kế phép thử cho `wiki.data-quality.failure-matrix`.** Trong ngữ cảnh `wiki.data-quality.failure-matrix`, thêm record tới trễ trong horizon và ngoài horizon. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The quality failure matrix` công bố.

**Bằng chứng cần giữ.** Đối với probe 7 của `The quality failure matrix`, báo accepted-late, rejected-late và oldest outstanding timestamp. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.8. The quality failure matrix: kiểm `Defect classes` bằng case 8, cụ thể thiếu, extra, duplicate, invalid, inconsistent, stale, inaccurate và broken relationship cần tách vì recovery khác

**Mệnh đề cần kiểm.** The quality failure matrix: kiểm `Defect classes` bằng case 8, cụ thể thiếu, extra, duplicate, invalid, inconsistent, stale, inaccurate và broken relationship cần tách vì recovery khác.

**Thiết kế phép thử cho `wiki.data-quality.failure-matrix`.** Trong ngữ cảnh `wiki.data-quality.failure-matrix`, đổi schema theo một cách tương thích rồi một cách phá vỡ semantics. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The quality failure matrix` công bố.

**Bằng chứng cần giữ.** Đối với probe 8 của `The quality failure matrix`, giữ schema diff, classification và consumer-visible result. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.9. The quality failure matrix: kiểm `Detection mapping` bằng case 9, cụ thể mỗi defect có earliest viable control và consumer-visible monitor; không giả định một test bắt mọi biến thể

**Mệnh đề cần kiểm.** The quality failure matrix: kiểm `Detection mapping` bằng case 9, cụ thể mỗi defect có earliest viable control và consumer-visible monitor; không giả định một test bắt mọi biến thể.

**Thiết kế phép thử cho `wiki.data-quality.failure-matrix`.** Trong ngữ cảnh `wiki.data-quality.failure-matrix`, tạo missing và duplicate bù nhau để count tổng không đổi. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The quality failure matrix` công bố.

**Bằng chứng cần giữ.** Đối với probe 9 của `The quality failure matrix`, so key multiset và typed hashes thay vì chỉ row count. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.10. The quality failure matrix: kiểm `Containment mapping` bằng case 10, cụ thể quarantine, block publish, serve stale, rollback hay notify phụ thuộc harm và recoverability

**Mệnh đề cần kiểm.** The quality failure matrix: kiểm `Containment mapping` bằng case 10, cụ thể quarantine, block publish, serve stale, rollback hay notify phụ thuộc harm và recoverability.

**Thiết kế phép thử cho `wiki.data-quality.failure-matrix`.** Trong ngữ cảnh `wiki.data-quality.failure-matrix`, cho reviewer tái hiện chỉ từ evidence package. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The quality failure matrix` công bố.

**Bằng chứng cần giữ.** Đối với probe 10 của `The quality failure matrix`, package phải đủ để người khác dựng lại decision và limitation. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.11. The quality failure matrix: kiểm `Ownership` bằng case 11, cụ thể producer, platform, domain steward và consumer có responsibilities khác; one owner cho decision nhưng contributors rõ

**Mệnh đề cần kiểm.** The quality failure matrix: kiểm `Ownership` bằng case 11, cụ thể producer, platform, domain steward và consumer có responsibilities khác; one owner cho decision nhưng contributors rõ.

**Thiết kế phép thử cho `wiki.data-quality.failure-matrix`.** Trong ngữ cảnh `wiki.data-quality.failure-matrix`, so với oracle độc lập không dùng chung query hoặc parser. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The quality failure matrix` công bố.

**Bằng chứng cần giữ.** Đối với probe 11 của `The quality failure matrix`, independent result phải khớp ở grain đã công bố. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.12. The quality failure matrix: kiểm `Gap analysis` bằng case 12, cụ thể ô trống, unknown coverage và untested recovery trở thành backlog có risk score, không tô xanh bằng assumption

**Mệnh đề cần kiểm.** The quality failure matrix: kiểm `Gap analysis` bằng case 12, cụ thể ô trống, unknown coverage và untested recovery trở thành backlog có risk score, không tô xanh bằng assumption.

**Thiết kế phép thử cho `wiki.data-quality.failure-matrix`.** Trong ngữ cảnh `wiki.data-quality.failure-matrix`, chạy scope hẹp và population đầy đủ rồi công bố phần bị loại. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The quality failure matrix` công bố.

**Bằng chứng cần giữ.** Đối với probe 12 của `The quality failure matrix`, coverage phải nêu rõ excluded nodes, partitions hoặc incidents. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.13. The quality failure matrix: kiểm `Matrix axes` bằng case 13, cụ thể hàng là defect classes; cột gồm detection point, signal, impact, containment, recovery, owner và evidence

**Mệnh đề cần kiểm.** The quality failure matrix: kiểm `Matrix axes` bằng case 13, cụ thể hàng là defect classes; cột gồm detection point, signal, impact, containment, recovery, owner và evidence.

**Thiết kế phép thử cho `wiki.data-quality.failure-matrix`.** Trong ngữ cảnh `wiki.data-quality.failure-matrix`, thử timezone, precision hoặc partition ở hai phía của ranh giới. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The quality failure matrix` công bố.

**Bằng chứng cần giữ.** Đối với probe 13 của `The quality failure matrix`, UTC/local interval và rounding policy phải hiện trong output. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.14. The quality failure matrix: kiểm `Defect classes` bằng case 14, cụ thể thiếu, extra, duplicate, invalid, inconsistent, stale, inaccurate và broken relationship cần tách vì recovery khác

**Mệnh đề cần kiểm.** The quality failure matrix: kiểm `Defect classes` bằng case 14, cụ thể thiếu, extra, duplicate, invalid, inconsistent, stale, inaccurate và broken relationship cần tách vì recovery khác.

**Thiết kế phép thử cho `wiki.data-quality.failure-matrix`.** Trong ngữ cảnh `wiki.data-quality.failure-matrix`, đổi constraint đủ lớn để quyết định phải đảo. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The quality failure matrix` công bố.

**Bằng chứng cần giữ.** Đối với probe 14 của `The quality failure matrix`, ADR phải lưu changed constraint và reversal threshold. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.15. The quality failure matrix: kiểm `Detection mapping` bằng case 15, cụ thể mỗi defect có earliest viable control và consumer-visible monitor; không giả định một test bắt mọi biến thể

**Mệnh đề cần kiểm.** The quality failure matrix: kiểm `Detection mapping` bằng case 15, cụ thể mỗi defect có earliest viable control và consumer-visible monitor; không giả định một test bắt mọi biến thể.

**Thiết kế phép thử cho `wiki.data-quality.failure-matrix`.** Trong ngữ cảnh `wiki.data-quality.failure-matrix`, chạy lại từ môi trường sạch với versions và seed đã khóa. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The quality failure matrix` công bố.

**Bằng chứng cần giữ.** Đối với probe 15 của `The quality failure matrix`, canonical result phải ổn định hoặc mọi nondeterminism phải được giải thích. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

## 8. Quy trình phản biện

1. Viết consumer-visible invariant cho `The quality failure matrix` trước khi chọn query hoặc tool.
2. Khóa grain, identity, population, time window và authoritative source.
3. Phân biệt declared configuration, executed state và published state.
4. Chạy negative control, replay hoặc changed-assumption case phù hợp.
5. Đối soát bằng oracle độc lập; công bố coverage và phần không quan sát được.
6. Gắn owner, hành động, reversal trigger và hạn review cho kết luận.

## 9. Câu hỏi tự kiểm tra

1. `The quality failure matrix: kiểm `Matrix axes` bằng case 1, cụ thể hàng là defect classes; cột gồm detection point, signal, impact, containment, recovery, owner và evidence` thất bại đầu tiên ở boundary nào?
2. Artifact nào mạnh nhất để trả lời `The quality failure matrix: kiểm `Detection mapping` bằng case 3, cụ thể mỗi defect có earliest viable control và consumer-visible monitor; không giả định một test bắt mọi biến thể`?
3. Counterexample nhỏ nhất cho `The quality failure matrix: kiểm `Gap analysis` bằng case 6, cụ thể ô trống, unknown coverage và untested recovery trở thành backlog có risk score, không tô xanh bằng assumption` gồm những state nào?
4. `The quality failure matrix: kiểm `Detection mapping` bằng case 9, cụ thể mỗi defect có earliest viable control và consumer-visible monitor; không giả định một test bắt mọi biến thể` có thể xanh giả ra sao?
5. Constraint nào khiến quyết định ở `The quality failure matrix: kiểm `Defect classes` bằng case 14, cụ thể thiếu, extra, duplicate, invalid, inconsistent, stale, inaccurate và broken relationship cần tách vì recovery khác` phải đảo?
6. Phần nào của `The quality failure matrix: kiểm `Detection mapping` bằng case 15, cụ thể mỗi defect có earliest viable control và consumer-visible monitor; không giả định một test bắt mọi biến thể` mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `The quality failure matrix` chưa chạy trên hệ thống production; nội dung là giáo trình và expected evidence.
- Hành vi phụ thuộc phiên bản, connector, scheduler, warehouse và catalog configuration phải được kiểm lại.
- Các ma trận, ladder và threshold do giáo trình tổng hợp không được gán nguyên văn cho vendor.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-GX-EXPECTATIONS]]
2. [[SRC-GOOGLE-SRE-INCIDENT-MANAGEMENT]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-GX-EXPECTATIONS]] | Contract hoặc cơ chế liên quan trực tiếp tới `The quality failure matrix` | Đã đọc locator; cần pin version khi chạy lab |
| [[SRC-GOOGLE-SRE-INCIDENT-MANAGEMENT]] | Contract hoặc cơ chế liên quan trực tiếp tới `The quality failure matrix` | Đã đọc locator; cần pin version khi chạy lab |

## Key takeaways
- Failure matrix biến điểm mù thành backlog có owner và containment.
- Với `wiki.data-quality.failure-matrix`, quality của kết luận phụ thuộc identity, coverage và oracle chứ không phụ thuộc màu dashboard.
- Câu hỏi `Quality failure matrix nối defect class, detection layer, containment và owner như thế nào?` chỉ được trả lời trong scope và version đã ghi.
- Các source IDs `src.web.gx-expectations, src.web.google-sre-incident-management` đặt ranh giới cho source fact; phần còn lại là synthesis có nhãn.
- Trước khi lab chạy, đây là note đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule — kiểm chứng `wiki.data-quality.failure-matrix`

> [!important] Phân loại mệnh đề
> Với `wiki.data-quality.failure-matrix`, sơ đồ, ví dụ và artifact về **The quality failure matrix** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.web.gx-expectations"] --> B["Khóa boundary"]
    B --> M["Cơ chế: The quality failure matrix"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.data-quality.failure-matrix` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **The quality failure matrix**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```sql
-- Verification harness for: The quality failure matrix
WITH evidence AS (
    SELECT 'wiki.data-quality.failure-matrix' AS concept_id,
           'boundary_declared' AS check_name, 1 AS passed
    UNION ALL
    SELECT 'wiki.data-quality.failure-matrix', 'independent_oracle', 1
    UNION ALL
    SELECT 'wiki.data-quality.failure-matrix', 'reversal_trigger_recorded', 1
)
SELECT concept_id,
       MIN(passed) AS all_hard_checks_pass,
       COUNT(*) AS evidence_items
FROM evidence
GROUP BY concept_id
HAVING MIN(passed) = 1;
```

Artifact của `wiki.data-quality.failure-matrix` buộc người dùng ghi boundary, oracle và reversal trigger cho **The quality failure matrix**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

### Tự kiểm tra trước khi tái sử dụng

1. Bạn có thể trả lời `Quality failure matrix nối defect class, detection layer, containment và owner như thế nào?` bằng một câu mà không kéo thêm concept thứ hai không?
2. Source locator nào đỡ cho claim, và phần nào chỉ là synthesis trong note?
3. Observation nào khiến bạn dừng, thu hẹp hoặc đảo quyết định?
4. Artifact nào cho phép một reviewer độc lập tái hiện kết quả?

<!-- ATOMIC-EXECUTION-CAPSULE:END -->
