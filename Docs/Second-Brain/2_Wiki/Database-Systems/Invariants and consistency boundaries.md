---
note_id: wiki.system-design.invariants-consistency
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
primary_question: Làm thế nào mô hình, kiểm chứng và vận hành business invariants, atomicity scope và client-visible consistency boundaries mà không khẳng định vượt quá evidence?
source_ids:
  - src.book.kleppmann-ddia.1e
  - src.paper.raft-extended
aliases: [Invariants and consistency boundaries]
tags: [wiki/system-design, system-design, capacity, consistency, replication, reliability]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/295-invariants-and-consistency-boundaries.md
relationships:
  builds_on: [wiki.system-design.ten-step-process]
  prerequisite_of: [wiki.system-design.single-stateful-service]
  related_to: []

---
# Invariants and consistency boundaries

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, kiểm chứng và vận hành business invariants, atomicity scope và client-visible consistency boundaries mà không khẳng định vượt quá evidence?

## 1. Mechanism

Mô hình business invariants, atomicity scope và client-visible consistency boundaries phải nêu actors, identities, state transitions và authority thay vì chỉ liệt kê components. Đừng bắt đầu bằng tên công cụ. Hãy bắt đầu bằng đối tượng được bảo vệ, boundary quan sát được và hậu quả nếu kết luận sai. Trong bài `Invariants and consistency boundaries`, câu hỏi thực dụng là: Làm thế nào mô hình, kiểm chứng và vận hành business invariants, atomicity scope và client-visible consistency boundaries mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 2. Boundary

Guarantee của business invariants, atomicity scope và client-visible consistency boundaries chỉ đúng trong workload, failure model, time window, trust boundary và version đã khóa. Điểm khó không nằm ở cú pháp mà ở identity và scope. Hai phép đo cùng tên vẫn có thể nói về hai population hoặc hai thời điểm khác nhau. Trong bài `Invariants and consistency boundaries`, câu hỏi thực dụng là: Làm thế nào mô hình, kiểm chứng và vận hành business invariants, atomicity scope và client-visible consistency boundaries mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 3. Failure mode

Phân tích business invariants, atomicity scope và client-visible consistency boundaries cần tìm earliest controllable failure, propagation path, blast radius và durable state còn tin cậy. Một dashboard xanh chỉ là tín hiệu. Muốn biến nó thành bằng chứng phải giữ input, phiên bản, rule, trạng thái trước-sau và cách tính độc lập. Trong bài `Invariants and consistency boundaries`, câu hỏi thực dụng là: Làm thế nào mô hình, kiểm chứng và vận hành business invariants, atomicity scope và client-visible consistency boundaries mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 4. Decision rule

Quyết định về business invariants, atomicity scope và client-visible consistency boundaries phải nối quantified requirements với alternatives, cost, complexity và reversal trigger. Thiết kế tốt phải chịu được counterexample. Hãy chủ động tạo case sát boundary, case thiếu dữ liệu và case replay thay vì chỉ chạy happy path. Trong bài `Invariants and consistency boundaries`, câu hỏi thực dụng là: Làm thế nào mô hình, kiểm chứng và vận hành business invariants, atomicity scope và client-visible consistency boundaries mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 5. Evidence

Bằng chứng cho business invariants, atomicity scope và client-visible consistency boundaries gồm input assumptions, stable identity, resolved design/config, raw observations và independent oracle. Chi phí vận hành thuộc contract. Một rule đúng nhưng quá đắt, quá ồn hoặc không có owner sẽ nhanh chóng bị tắt và mất tác dụng. Trong bài `Invariants and consistency boundaries`, câu hỏi thực dụng là: Làm thế nào mô hình, kiểm chứng và vận hành business invariants, atomicity scope và client-visible consistency boundaries mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 6. Recovery lab

Lab business invariants, atomicity scope và client-visible consistency boundaries phải inject failure hoặc đổi một assumption, phục hồi theo runbook rồi reconcile outcome với invariants. Kết luận cần có điều kiện đảo chiều. Khi volume, latency, nguồn thẩm quyền hoặc topology đổi, quyết định cũ phải được xem xét lại bằng cùng một oracle. Trong bài `Invariants and consistency boundaries`, câu hỏi thực dụng là: Làm thế nào mô hình, kiểm chứng và vận hành business invariants, atomicity scope và client-visible consistency boundaries mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 7. Ma trận kiểm chứng từng mệnh đề

Với `wiki.system-design.invariants-consistency`, command thành công không tự chứng minh dữ liệu đúng. Protocol riêng của bài là: Run a version-pinned model, sandbox or replayable fixture, change one assumption or inject one failure, retain raw state and event evidence, then reconcile the result against an independent invariant oracle. Mỗi probe dưới đây phải nối input boundary với failure signal và oracle có thể phản bác kết luận.

### 7.1. Invariants and consistency boundaries: kiểm `Mechanism` bằng case 1, cụ thể mô hình business invariants, atomicity scope và client-visible consistency boundaries phải nêu actors, identities, state transitions và authority thay vì chỉ liệt kê components

**Mệnh đề cần kiểm.** Invariants and consistency boundaries: kiểm `Mechanism` bằng case 1, cụ thể mô hình business invariants, atomicity scope và client-visible consistency boundaries phải nêu actors, identities, state transitions và authority thay vì chỉ liệt kê components.

**Thiết kế phép thử cho `wiki.system-design.invariants-consistency`.** Trong ngữ cảnh `wiki.system-design.invariants-consistency`, tạo positive control và negative control chỉ khác đúng một điều kiện. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Invariants and consistency boundaries` công bố.

**Bằng chứng cần giữ.** Đối với probe 1 của `Invariants and consistency boundaries`, giữ fixture, raw failing rows và lệnh tái hiện. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.2. Invariants and consistency boundaries: kiểm `Boundary` bằng case 2, cụ thể guarantee của business invariants, atomicity scope và client-visible consistency boundaries chỉ đúng trong workload, failure model, time window, trust boundary và version đã khóa

**Mệnh đề cần kiểm.** Invariants and consistency boundaries: kiểm `Boundary` bằng case 2, cụ thể guarantee của business invariants, atomicity scope và client-visible consistency boundaries chỉ đúng trong workload, failure model, time window, trust boundary và version đã khóa.

**Thiết kế phép thử cho `wiki.system-design.invariants-consistency`.** Trong ngữ cảnh `wiki.system-design.invariants-consistency`, đổi grain nhưng giữ tổng số dòng để lộ phép đo sai cấp. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Invariants and consistency boundaries` công bố.

**Bằng chứng cần giữ.** Đối với probe 2 của `Invariants and consistency boundaries`, báo numerator, denominator và key set ở cả hai grain. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.3. Invariants and consistency boundaries: kiểm `Failure mode` bằng case 3, cụ thể phân tích business invariants, atomicity scope và client-visible consistency boundaries cần tìm earliest controllable failure, propagation path, blast radius và durable state còn tin cậy

**Mệnh đề cần kiểm.** Invariants and consistency boundaries: kiểm `Failure mode` bằng case 3, cụ thể phân tích business invariants, atomicity scope và client-visible consistency boundaries cần tìm earliest controllable failure, propagation path, blast radius và durable state còn tin cậy.

**Thiết kế phép thử cho `wiki.system-design.invariants-consistency`.** Trong ngữ cảnh `wiki.system-design.invariants-consistency`, đưa một giá trị tới đúng boundary và một giá trị vượt boundary. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Invariants and consistency boundaries` công bố.

**Bằng chứng cần giữ.** Đối với probe 3 của `Invariants and consistency boundaries`, lưu hai observed values cùng rule đã resolve. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.4. Invariants and consistency boundaries: kiểm `Decision rule` bằng case 4, cụ thể quyết định về business invariants, atomicity scope và client-visible consistency boundaries phải nối quantified requirements với alternatives, cost, complexity và reversal trigger

**Mệnh đề cần kiểm.** Invariants and consistency boundaries: kiểm `Decision rule` bằng case 4, cụ thể quyết định về business invariants, atomicity scope và client-visible consistency boundaries phải nối quantified requirements với alternatives, cost, complexity và reversal trigger.

**Thiết kế phép thử cho `wiki.system-design.invariants-consistency`.** Trong ngữ cảnh `wiki.system-design.invariants-consistency`, kill tiến trình ngay trước rồi ngay sau durable side effect. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Invariants and consistency boundaries` công bố.

**Bằng chứng cần giữ.** Đối với probe 4 của `Invariants and consistency boundaries`, lưu checkpoint, external ledger và trạng thái sau restart. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.5. Invariants and consistency boundaries: kiểm `Evidence` bằng case 5, cụ thể bằng chứng cho business invariants, atomicity scope và client-visible consistency boundaries gồm input assumptions, stable identity, resolved design/config, raw observations và independent oracle

**Mệnh đề cần kiểm.** Invariants and consistency boundaries: kiểm `Evidence` bằng case 5, cụ thể bằng chứng cho business invariants, atomicity scope và client-visible consistency boundaries gồm input assumptions, stable identity, resolved design/config, raw observations và independent oracle.

**Thiết kế phép thử cho `wiki.system-design.invariants-consistency`.** Trong ngữ cảnh `wiki.system-design.invariants-consistency`, đảo thứ tự input và concurrency nhưng giữ logical population. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Invariants and consistency boundaries` công bố.

**Bằng chứng cần giữ.** Đối với probe 5 của `Invariants and consistency boundaries`, so canonical hash và business totals giữa các thứ tự. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.6. Invariants and consistency boundaries: kiểm `Recovery lab` bằng case 6, cụ thể lab business invariants, atomicity scope và client-visible consistency boundaries phải inject failure hoặc đổi một assumption, phục hồi theo runbook rồi reconcile outcome với invariants

**Mệnh đề cần kiểm.** Invariants and consistency boundaries: kiểm `Recovery lab` bằng case 6, cụ thể lab business invariants, atomicity scope và client-visible consistency boundaries phải inject failure hoặc đổi một assumption, phục hồi theo runbook rồi reconcile outcome với invariants.

**Thiết kế phép thử cho `wiki.system-design.invariants-consistency`.** Trong ngữ cảnh `wiki.system-design.invariants-consistency`, replay cùng identity với payload giống rồi payload xung đột. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Invariants and consistency boundaries` công bố.

**Bằng chứng cần giữ.** Đối với probe 6 của `Invariants and consistency boundaries`, tách duplicate replay khỏi identity collision bằng reason code. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.7. Invariants and consistency boundaries: kiểm `Mechanism` bằng case 7, cụ thể mô hình business invariants, atomicity scope và client-visible consistency boundaries phải nêu actors, identities, state transitions và authority thay vì chỉ liệt kê components

**Mệnh đề cần kiểm.** Invariants and consistency boundaries: kiểm `Mechanism` bằng case 7, cụ thể mô hình business invariants, atomicity scope và client-visible consistency boundaries phải nêu actors, identities, state transitions và authority thay vì chỉ liệt kê components.

**Thiết kế phép thử cho `wiki.system-design.invariants-consistency`.** Trong ngữ cảnh `wiki.system-design.invariants-consistency`, thêm record tới trễ trong horizon và ngoài horizon. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Invariants and consistency boundaries` công bố.

**Bằng chứng cần giữ.** Đối với probe 7 của `Invariants and consistency boundaries`, báo accepted-late, rejected-late và oldest outstanding timestamp. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.8. Invariants and consistency boundaries: kiểm `Boundary` bằng case 8, cụ thể guarantee của business invariants, atomicity scope và client-visible consistency boundaries chỉ đúng trong workload, failure model, time window, trust boundary và version đã khóa

**Mệnh đề cần kiểm.** Invariants and consistency boundaries: kiểm `Boundary` bằng case 8, cụ thể guarantee của business invariants, atomicity scope và client-visible consistency boundaries chỉ đúng trong workload, failure model, time window, trust boundary và version đã khóa.

**Thiết kế phép thử cho `wiki.system-design.invariants-consistency`.** Trong ngữ cảnh `wiki.system-design.invariants-consistency`, đổi schema theo một cách tương thích rồi một cách phá vỡ semantics. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Invariants and consistency boundaries` công bố.

**Bằng chứng cần giữ.** Đối với probe 8 của `Invariants and consistency boundaries`, giữ schema diff, classification và consumer-visible result. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.9. Invariants and consistency boundaries: kiểm `Failure mode` bằng case 9, cụ thể phân tích business invariants, atomicity scope và client-visible consistency boundaries cần tìm earliest controllable failure, propagation path, blast radius và durable state còn tin cậy

**Mệnh đề cần kiểm.** Invariants and consistency boundaries: kiểm `Failure mode` bằng case 9, cụ thể phân tích business invariants, atomicity scope và client-visible consistency boundaries cần tìm earliest controllable failure, propagation path, blast radius và durable state còn tin cậy.

**Thiết kế phép thử cho `wiki.system-design.invariants-consistency`.** Trong ngữ cảnh `wiki.system-design.invariants-consistency`, tạo missing và duplicate bù nhau để count tổng không đổi. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Invariants and consistency boundaries` công bố.

**Bằng chứng cần giữ.** Đối với probe 9 của `Invariants and consistency boundaries`, so key multiset và typed hashes thay vì chỉ row count. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.10. Invariants and consistency boundaries: kiểm `Decision rule` bằng case 10, cụ thể quyết định về business invariants, atomicity scope và client-visible consistency boundaries phải nối quantified requirements với alternatives, cost, complexity và reversal trigger

**Mệnh đề cần kiểm.** Invariants and consistency boundaries: kiểm `Decision rule` bằng case 10, cụ thể quyết định về business invariants, atomicity scope và client-visible consistency boundaries phải nối quantified requirements với alternatives, cost, complexity và reversal trigger.

**Thiết kế phép thử cho `wiki.system-design.invariants-consistency`.** Trong ngữ cảnh `wiki.system-design.invariants-consistency`, cho reviewer tái hiện chỉ từ evidence package. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Invariants and consistency boundaries` công bố.

**Bằng chứng cần giữ.** Đối với probe 10 của `Invariants and consistency boundaries`, package phải đủ để người khác dựng lại decision và limitation. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.11. Invariants and consistency boundaries: kiểm `Evidence` bằng case 11, cụ thể bằng chứng cho business invariants, atomicity scope và client-visible consistency boundaries gồm input assumptions, stable identity, resolved design/config, raw observations và independent oracle

**Mệnh đề cần kiểm.** Invariants and consistency boundaries: kiểm `Evidence` bằng case 11, cụ thể bằng chứng cho business invariants, atomicity scope và client-visible consistency boundaries gồm input assumptions, stable identity, resolved design/config, raw observations và independent oracle.

**Thiết kế phép thử cho `wiki.system-design.invariants-consistency`.** Trong ngữ cảnh `wiki.system-design.invariants-consistency`, so với oracle độc lập không dùng chung query hoặc parser. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Invariants and consistency boundaries` công bố.

**Bằng chứng cần giữ.** Đối với probe 11 của `Invariants and consistency boundaries`, independent result phải khớp ở grain đã công bố. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.12. Invariants and consistency boundaries: kiểm `Recovery lab` bằng case 12, cụ thể lab business invariants, atomicity scope và client-visible consistency boundaries phải inject failure hoặc đổi một assumption, phục hồi theo runbook rồi reconcile outcome với invariants

**Mệnh đề cần kiểm.** Invariants and consistency boundaries: kiểm `Recovery lab` bằng case 12, cụ thể lab business invariants, atomicity scope và client-visible consistency boundaries phải inject failure hoặc đổi một assumption, phục hồi theo runbook rồi reconcile outcome với invariants.

**Thiết kế phép thử cho `wiki.system-design.invariants-consistency`.** Trong ngữ cảnh `wiki.system-design.invariants-consistency`, chạy scope hẹp và population đầy đủ rồi công bố phần bị loại. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Invariants and consistency boundaries` công bố.

**Bằng chứng cần giữ.** Đối với probe 12 của `Invariants and consistency boundaries`, coverage phải nêu rõ excluded nodes, partitions hoặc incidents. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.13. Invariants and consistency boundaries: kiểm `Mechanism` bằng case 13, cụ thể mô hình business invariants, atomicity scope và client-visible consistency boundaries phải nêu actors, identities, state transitions và authority thay vì chỉ liệt kê components

**Mệnh đề cần kiểm.** Invariants and consistency boundaries: kiểm `Mechanism` bằng case 13, cụ thể mô hình business invariants, atomicity scope và client-visible consistency boundaries phải nêu actors, identities, state transitions và authority thay vì chỉ liệt kê components.

**Thiết kế phép thử cho `wiki.system-design.invariants-consistency`.** Trong ngữ cảnh `wiki.system-design.invariants-consistency`, thử timezone, precision hoặc partition ở hai phía của ranh giới. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Invariants and consistency boundaries` công bố.

**Bằng chứng cần giữ.** Đối với probe 13 của `Invariants and consistency boundaries`, UTC/local interval và rounding policy phải hiện trong output. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.14. Invariants and consistency boundaries: kiểm `Boundary` bằng case 14, cụ thể guarantee của business invariants, atomicity scope và client-visible consistency boundaries chỉ đúng trong workload, failure model, time window, trust boundary và version đã khóa

**Mệnh đề cần kiểm.** Invariants and consistency boundaries: kiểm `Boundary` bằng case 14, cụ thể guarantee của business invariants, atomicity scope và client-visible consistency boundaries chỉ đúng trong workload, failure model, time window, trust boundary và version đã khóa.

**Thiết kế phép thử cho `wiki.system-design.invariants-consistency`.** Trong ngữ cảnh `wiki.system-design.invariants-consistency`, đổi constraint đủ lớn để quyết định phải đảo. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Invariants and consistency boundaries` công bố.

**Bằng chứng cần giữ.** Đối với probe 14 của `Invariants and consistency boundaries`, ADR phải lưu changed constraint và reversal threshold. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.15. Invariants and consistency boundaries: kiểm `Failure mode` bằng case 15, cụ thể phân tích business invariants, atomicity scope và client-visible consistency boundaries cần tìm earliest controllable failure, propagation path, blast radius và durable state còn tin cậy

**Mệnh đề cần kiểm.** Invariants and consistency boundaries: kiểm `Failure mode` bằng case 15, cụ thể phân tích business invariants, atomicity scope và client-visible consistency boundaries cần tìm earliest controllable failure, propagation path, blast radius và durable state còn tin cậy.

**Thiết kế phép thử cho `wiki.system-design.invariants-consistency`.** Trong ngữ cảnh `wiki.system-design.invariants-consistency`, chạy lại từ môi trường sạch với versions và seed đã khóa. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Invariants and consistency boundaries` công bố.

**Bằng chứng cần giữ.** Đối với probe 15 của `Invariants and consistency boundaries`, canonical result phải ổn định hoặc mọi nondeterminism phải được giải thích. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

## 8. Quy trình phản biện

1. Viết consumer-visible invariant cho `Invariants and consistency boundaries` trước khi chọn query hoặc tool.
2. Khóa grain, identity, population, time window và authoritative source.
3. Phân biệt declared configuration, executed state và published state.
4. Chạy negative control, replay hoặc changed-assumption case phù hợp.
5. Đối soát bằng oracle độc lập; công bố coverage và phần không quan sát được.
6. Gắn owner, hành động, reversal trigger và hạn review cho kết luận.

## 9. Câu hỏi tự kiểm tra

1. `Invariants and consistency boundaries: kiểm `Mechanism` bằng case 1, cụ thể mô hình business invariants, atomicity scope và client-visible consistency boundaries phải nêu actors, identities, state transitions và authority thay vì chỉ liệt kê components` thất bại đầu tiên ở boundary nào?
2. Artifact nào mạnh nhất để trả lời `Invariants and consistency boundaries: kiểm `Failure mode` bằng case 3, cụ thể phân tích business invariants, atomicity scope và client-visible consistency boundaries cần tìm earliest controllable failure, propagation path, blast radius và durable state còn tin cậy`?
3. Counterexample nhỏ nhất cho `Invariants and consistency boundaries: kiểm `Recovery lab` bằng case 6, cụ thể lab business invariants, atomicity scope và client-visible consistency boundaries phải inject failure hoặc đổi một assumption, phục hồi theo runbook rồi reconcile outcome với invariants` gồm những state nào?
4. `Invariants and consistency boundaries: kiểm `Failure mode` bằng case 9, cụ thể phân tích business invariants, atomicity scope và client-visible consistency boundaries cần tìm earliest controllable failure, propagation path, blast radius và durable state còn tin cậy` có thể xanh giả ra sao?
5. Constraint nào khiến quyết định ở `Invariants and consistency boundaries: kiểm `Boundary` bằng case 14, cụ thể guarantee của business invariants, atomicity scope và client-visible consistency boundaries chỉ đúng trong workload, failure model, time window, trust boundary và version đã khóa` phải đảo?
6. Phần nào của `Invariants and consistency boundaries: kiểm `Failure mode` bằng case 15, cụ thể phân tích business invariants, atomicity scope và client-visible consistency boundaries cần tìm earliest controllable failure, propagation path, blast radius và durable state còn tin cậy` mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `Invariants and consistency boundaries` chưa chạy trên hệ thống production; nội dung là giáo trình và expected evidence.
- Hành vi phụ thuộc phiên bản, connector, scheduler, warehouse và catalog configuration phải được kiểm lại.
- Các ma trận, ladder và threshold do giáo trình tổng hợp không được gán nguyên văn cho vendor.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-KLEPPMANN-DDIA-1E]]
2. [[SRC-RAFT-EXTENDED]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-KLEPPMANN-DDIA-1E]] | Contract hoặc cơ chế liên quan trực tiếp tới `Invariants and consistency boundaries` | Đã đọc locator; cần pin version khi chạy lab |
| [[SRC-RAFT-EXTENDED]] | Contract hoặc cơ chế liên quan trực tiếp tới `Invariants and consistency boundaries` | Đã đọc locator; cần pin version khi chạy lab |

## Key takeaways
- Business invariants, atomicity scope và client-visible consistency boundaries phải được bảo vệ bằng quantified boundary, counterexample và evidence có thể phản bác.
- Với `wiki.system-design.invariants-consistency`, quality của kết luận phụ thuộc identity, coverage và oracle chứ không phụ thuộc màu dashboard.
- Câu hỏi `Làm thế nào mô hình, kiểm chứng và vận hành business invariants, atomicity scope và client-visible consistency boundaries mà không khẳng định vượt quá evidence?` chỉ được trả lời trong scope và version đã ghi.
- Các source IDs `src.book.kleppmann-ddia.1e, src.paper.raft-extended` đặt ranh giới cho source fact; phần còn lại là synthesis có nhãn.
- Trước khi lab chạy, đây là note đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule: kiểm chứng `wiki.system-design.invariants-consistency`

> [!important] Phân loại mệnh đề
> Với `wiki.system-design.invariants-consistency`, sơ đồ, ví dụ và artifact về **Invariants and consistency boundaries** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.book.kleppmann-ddia.1e"] --> B["Khóa boundary"]
    B --> M["Cơ chế: Invariants and consistency boundaries"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.system-design.invariants-consistency` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **Invariants and consistency boundaries**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```sql
-- Verification harness for: Invariants and consistency boundaries
WITH evidence AS (
    SELECT 'wiki.system-design.invariants-consistency' AS concept_id,
           'boundary_declared' AS check_name, 1 AS passed
    UNION ALL
    SELECT 'wiki.system-design.invariants-consistency', 'independent_oracle', 1
    UNION ALL
    SELECT 'wiki.system-design.invariants-consistency', 'reversal_trigger_recorded', 1
)
SELECT concept_id,
       MIN(passed) AS all_hard_checks_pass,
       COUNT(*) AS evidence_items
FROM evidence
GROUP BY concept_id
HAVING MIN(passed) = 1;
```

Artifact của `wiki.system-design.invariants-consistency` buộc người dùng ghi boundary, oracle và reversal trigger cho **Invariants and consistency boundaries**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

### Tự kiểm tra trước khi tái sử dụng

1. Bạn có thể trả lời `Làm thế nào mô hình, kiểm chứng và vận hành business invariants, atomicity scope và client-visible consistency boundaries mà không khẳng định vượt quá evidence?` bằng một câu mà không kéo thêm concept thứ hai không?
2. Source locator nào đỡ cho claim, và phần nào chỉ là synthesis trong note?
3. Observation nào khiến bạn dừng, thu hẹp hoặc đảo quyết định?
4. Artifact nào cho phép một reviewer độc lập tái hiện kết quả?

<!-- ATOMIC-EXECUTION-CAPSULE:END -->
