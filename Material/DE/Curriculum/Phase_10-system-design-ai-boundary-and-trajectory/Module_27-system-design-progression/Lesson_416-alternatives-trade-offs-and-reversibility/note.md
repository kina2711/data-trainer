# Phase 10: System Design, AI Boundary and Trajectory
# Module 27: System Design Progression
# Lesson 416: Alternatives, trade-offs and reversibility

## Mục tiêu bài học

**Năng lực cần chứng minh.** Trình ba phương án thật có lượng hoá và nêu điều kiện làm lựa chọn không còn phù hợp.

**Điều kiện hoàn thành.** Mỗi phương án có một bối cảnh mà nó thắng, hệ quả lượng hoá theo cùng bộ tiêu chí, và hai điều kiện đảo ngược được nêu kèm chi phí.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào thiết kế, kiểm chứng và bảo vệ alternatives, explicit trade-offs, reversibility và option value mà không khẳng định vượt quá evidence?

## 1. Mechanism

Mô hình alternatives, explicit trade-offs, reversibility và option value phải nêu actors, identities, state transitions và decision authority thay vì liệt kê công cụ. Đừng bắt đầu bằng tên công cụ. Hãy bắt đầu bằng đối tượng được bảo vệ, boundary quan sát được và hậu quả nếu kết luận sai. Trong bài `Alternatives, trade-offs and reversibility`, câu hỏi thực dụng là: Làm thế nào thiết kế, kiểm chứng và bảo vệ alternatives, explicit trade-offs, reversibility và option value mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 2. Boundary

Kết luận về alternatives, explicit trade-offs, reversibility và option value chỉ đúng trong audience, workload, trust boundary, time window và version đã khóa. Điểm khó không nằm ở cú pháp mà ở identity và scope. Hai phép đo cùng tên vẫn có thể nói về hai population hoặc hai thời điểm khác nhau. Trong bài `Alternatives, trade-offs and reversibility`, câu hỏi thực dụng là: Làm thế nào thiết kế, kiểm chứng và bảo vệ alternatives, explicit trade-offs, reversibility và option value mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 3. Failure mode

Phân tích alternatives, explicit trade-offs, reversibility và option value cần tìm earliest failure, propagation path, blast radius và state hoặc claim còn đáng tin. Một dashboard xanh chỉ là tín hiệu. Muốn biến nó thành bằng chứng phải giữ input, phiên bản, rule, trạng thái trước–sau và cách tính độc lập. Trong bài `Alternatives, trade-offs and reversibility`, câu hỏi thực dụng là: Làm thế nào thiết kế, kiểm chứng và bảo vệ alternatives, explicit trade-offs, reversibility và option value mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 4. Decision rule

Quyết định về alternatives, explicit trade-offs, reversibility và option value phải nối quantified constraints với alternatives, trade-offs và reversal trigger. Thiết kế tốt phải chịu được counterexample. Hãy chủ động tạo case sát boundary, case thiếu dữ liệu và case replay thay vì chỉ chạy happy path. Trong bài `Alternatives, trade-offs and reversibility`, câu hỏi thực dụng là: Làm thế nào thiết kế, kiểm chứng và bảo vệ alternatives, explicit trade-offs, reversibility và option value mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 5. Evidence

Bằng chứng cho alternatives, explicit trade-offs, reversibility và option value gồm inputs có version, stable identity, raw observations, reviewer-visible limitations và independent oracle. Chi phí vận hành thuộc contract. Một rule đúng nhưng quá đắt, quá ồn hoặc không có owner sẽ nhanh chóng bị tắt và mất tác dụng. Trong bài `Alternatives, trade-offs and reversibility`, câu hỏi thực dụng là: Làm thế nào thiết kế, kiểm chứng và bảo vệ alternatives, explicit trade-offs, reversibility và option value mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 6. Transfer test

Bài thực hành alternatives, explicit trade-offs, reversibility và option value phải đổi một constraint hoặc inject counterexample rồi bảo vệ hoặc đảo quyết định bằng evidence. Kết luận cần có điều kiện đảo chiều. Khi volume, latency, nguồn thẩm quyền hoặc topology đổi, quyết định cũ phải được xem xét lại bằng cùng một oracle. Trong bài `Alternatives, trade-offs and reversibility`, câu hỏi thực dụng là: Làm thế nào thiết kế, kiểm chứng và bảo vệ alternatives, explicit trade-offs, reversibility và option value mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 7. Ma trận kiểm chứng từng mệnh đề

Với `wiki.system-design.alternatives-reversibility`, command thành công không tự chứng minh dữ liệu đúng. Protocol riêng của bài là: Run a version-pinned model, evaluation corpus or review simulation, change one material constraint, retain raw evidence and reconcile the recommendation against an independent rubric or invariant oracle. Mỗi probe dưới đây phải nối input boundary với failure signal và oracle có thể phản bác kết luận.

### 7.1. Alternatives, trade-offs and reversibility: kiểm `Mechanism` bằng case 1, cụ thể mô hình alternatives, explicit trade-offs, reversibility và option value phải nêu actors, identities, state transitions và decision authority thay vì liệt kê công cụ

**Mệnh đề cần kiểm.** Alternatives, trade-offs and reversibility: kiểm `Mechanism` bằng case 1, cụ thể mô hình alternatives, explicit trade-offs, reversibility và option value phải nêu actors, identities, state transitions và decision authority thay vì liệt kê công cụ.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.alternatives-reversibility`, tạo positive control và negative control chỉ khác đúng một điều kiện. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Alternatives, trade-offs and reversibility` công bố.

**Bằng chứng cần giữ.** Đối với probe 1 của `Alternatives, trade-offs and reversibility`, giữ fixture, raw failing rows và lệnh tái hiện. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.2. Alternatives, trade-offs and reversibility: kiểm `Boundary` bằng case 2, cụ thể kết luận về alternatives, explicit trade-offs, reversibility và option value chỉ đúng trong audience, workload, trust boundary, time window và version đã khóa

**Mệnh đề cần kiểm.** Alternatives, trade-offs and reversibility: kiểm `Boundary` bằng case 2, cụ thể kết luận về alternatives, explicit trade-offs, reversibility và option value chỉ đúng trong audience, workload, trust boundary, time window và version đã khóa.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.alternatives-reversibility`, đổi grain nhưng giữ tổng số dòng để lộ phép đo sai cấp. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Alternatives, trade-offs and reversibility` công bố.

**Bằng chứng cần giữ.** Đối với probe 2 của `Alternatives, trade-offs and reversibility`, báo numerator, denominator và key set ở cả hai grain. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.3. Alternatives, trade-offs and reversibility: kiểm `Failure mode` bằng case 3, cụ thể phân tích alternatives, explicit trade-offs, reversibility và option value cần tìm earliest failure, propagation path, blast radius và state hoặc claim còn đáng tin

**Mệnh đề cần kiểm.** Alternatives, trade-offs and reversibility: kiểm `Failure mode` bằng case 3, cụ thể phân tích alternatives, explicit trade-offs, reversibility và option value cần tìm earliest failure, propagation path, blast radius và state hoặc claim còn đáng tin.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.alternatives-reversibility`, đưa một giá trị tới đúng boundary và một giá trị vượt boundary. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Alternatives, trade-offs and reversibility` công bố.

**Bằng chứng cần giữ.** Đối với probe 3 của `Alternatives, trade-offs and reversibility`, lưu hai observed values cùng rule đã resolve. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.4. Alternatives, trade-offs and reversibility: kiểm `Decision rule` bằng case 4, cụ thể quyết định về alternatives, explicit trade-offs, reversibility và option value phải nối quantified constraints với alternatives, trade-offs và reversal trigger

**Mệnh đề cần kiểm.** Alternatives, trade-offs and reversibility: kiểm `Decision rule` bằng case 4, cụ thể quyết định về alternatives, explicit trade-offs, reversibility và option value phải nối quantified constraints với alternatives, trade-offs và reversal trigger.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.alternatives-reversibility`, kill tiến trình ngay trước rồi ngay sau durable side effect. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Alternatives, trade-offs and reversibility` công bố.

**Bằng chứng cần giữ.** Đối với probe 4 của `Alternatives, trade-offs and reversibility`, lưu checkpoint, external ledger và trạng thái sau restart. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.5. Alternatives, trade-offs and reversibility: kiểm `Evidence` bằng case 5, cụ thể bằng chứng cho alternatives, explicit trade-offs, reversibility và option value gồm inputs có version, stable identity, raw observations, reviewer-visible limitations và independent oracle

**Mệnh đề cần kiểm.** Alternatives, trade-offs and reversibility: kiểm `Evidence` bằng case 5, cụ thể bằng chứng cho alternatives, explicit trade-offs, reversibility và option value gồm inputs có version, stable identity, raw observations, reviewer-visible limitations và independent oracle.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.alternatives-reversibility`, đảo thứ tự input và concurrency nhưng giữ logical population. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Alternatives, trade-offs and reversibility` công bố.

**Bằng chứng cần giữ.** Đối với probe 5 của `Alternatives, trade-offs and reversibility`, so canonical hash và business totals giữa các thứ tự. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.6. Alternatives, trade-offs and reversibility: kiểm `Transfer test` bằng case 6, cụ thể bài thực hành alternatives, explicit trade-offs, reversibility và option value phải đổi một constraint hoặc inject counterexample rồi bảo vệ hoặc đảo quyết định bằng evidence

**Mệnh đề cần kiểm.** Alternatives, trade-offs and reversibility: kiểm `Transfer test` bằng case 6, cụ thể bài thực hành alternatives, explicit trade-offs, reversibility và option value phải đổi một constraint hoặc inject counterexample rồi bảo vệ hoặc đảo quyết định bằng evidence.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.alternatives-reversibility`, replay cùng identity với payload giống rồi payload xung đột. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Alternatives, trade-offs and reversibility` công bố.

**Bằng chứng cần giữ.** Đối với probe 6 của `Alternatives, trade-offs and reversibility`, tách duplicate replay khỏi identity collision bằng reason code. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.7. Alternatives, trade-offs and reversibility: kiểm `Mechanism` bằng case 7, cụ thể mô hình alternatives, explicit trade-offs, reversibility và option value phải nêu actors, identities, state transitions và decision authority thay vì liệt kê công cụ

**Mệnh đề cần kiểm.** Alternatives, trade-offs and reversibility: kiểm `Mechanism` bằng case 7, cụ thể mô hình alternatives, explicit trade-offs, reversibility và option value phải nêu actors, identities, state transitions và decision authority thay vì liệt kê công cụ.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.alternatives-reversibility`, thêm record tới trễ trong horizon và ngoài horizon. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Alternatives, trade-offs and reversibility` công bố.

**Bằng chứng cần giữ.** Đối với probe 7 của `Alternatives, trade-offs and reversibility`, báo accepted-late, rejected-late và oldest outstanding timestamp. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.8. Alternatives, trade-offs and reversibility: kiểm `Boundary` bằng case 8, cụ thể kết luận về alternatives, explicit trade-offs, reversibility và option value chỉ đúng trong audience, workload, trust boundary, time window và version đã khóa

**Mệnh đề cần kiểm.** Alternatives, trade-offs and reversibility: kiểm `Boundary` bằng case 8, cụ thể kết luận về alternatives, explicit trade-offs, reversibility và option value chỉ đúng trong audience, workload, trust boundary, time window và version đã khóa.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.alternatives-reversibility`, đổi schema theo một cách tương thích rồi một cách phá vỡ semantics. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Alternatives, trade-offs and reversibility` công bố.

**Bằng chứng cần giữ.** Đối với probe 8 của `Alternatives, trade-offs and reversibility`, giữ schema diff, classification và consumer-visible result. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.9. Alternatives, trade-offs and reversibility: kiểm `Failure mode` bằng case 9, cụ thể phân tích alternatives, explicit trade-offs, reversibility và option value cần tìm earliest failure, propagation path, blast radius và state hoặc claim còn đáng tin

**Mệnh đề cần kiểm.** Alternatives, trade-offs and reversibility: kiểm `Failure mode` bằng case 9, cụ thể phân tích alternatives, explicit trade-offs, reversibility và option value cần tìm earliest failure, propagation path, blast radius và state hoặc claim còn đáng tin.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.alternatives-reversibility`, tạo missing và duplicate bù nhau để count tổng không đổi. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Alternatives, trade-offs and reversibility` công bố.

**Bằng chứng cần giữ.** Đối với probe 9 của `Alternatives, trade-offs and reversibility`, so key multiset và typed hashes thay vì chỉ row count. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.10. Alternatives, trade-offs and reversibility: kiểm `Decision rule` bằng case 10, cụ thể quyết định về alternatives, explicit trade-offs, reversibility và option value phải nối quantified constraints với alternatives, trade-offs và reversal trigger

**Mệnh đề cần kiểm.** Alternatives, trade-offs and reversibility: kiểm `Decision rule` bằng case 10, cụ thể quyết định về alternatives, explicit trade-offs, reversibility và option value phải nối quantified constraints với alternatives, trade-offs và reversal trigger.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.alternatives-reversibility`, cho reviewer tái hiện chỉ từ evidence package. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Alternatives, trade-offs and reversibility` công bố.

**Bằng chứng cần giữ.** Đối với probe 10 của `Alternatives, trade-offs and reversibility`, package phải đủ để người khác dựng lại decision và limitation. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.11. Alternatives, trade-offs and reversibility: kiểm `Evidence` bằng case 11, cụ thể bằng chứng cho alternatives, explicit trade-offs, reversibility và option value gồm inputs có version, stable identity, raw observations, reviewer-visible limitations và independent oracle

**Mệnh đề cần kiểm.** Alternatives, trade-offs and reversibility: kiểm `Evidence` bằng case 11, cụ thể bằng chứng cho alternatives, explicit trade-offs, reversibility và option value gồm inputs có version, stable identity, raw observations, reviewer-visible limitations và independent oracle.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.alternatives-reversibility`, so với oracle độc lập không dùng chung query hoặc parser. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Alternatives, trade-offs and reversibility` công bố.

**Bằng chứng cần giữ.** Đối với probe 11 của `Alternatives, trade-offs and reversibility`, independent result phải khớp ở grain đã công bố. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.12. Alternatives, trade-offs and reversibility: kiểm `Transfer test` bằng case 12, cụ thể bài thực hành alternatives, explicit trade-offs, reversibility và option value phải đổi một constraint hoặc inject counterexample rồi bảo vệ hoặc đảo quyết định bằng evidence

**Mệnh đề cần kiểm.** Alternatives, trade-offs and reversibility: kiểm `Transfer test` bằng case 12, cụ thể bài thực hành alternatives, explicit trade-offs, reversibility và option value phải đổi một constraint hoặc inject counterexample rồi bảo vệ hoặc đảo quyết định bằng evidence.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.alternatives-reversibility`, chạy scope hẹp và population đầy đủ rồi công bố phần bị loại. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Alternatives, trade-offs and reversibility` công bố.

**Bằng chứng cần giữ.** Đối với probe 12 của `Alternatives, trade-offs and reversibility`, coverage phải nêu rõ excluded nodes, partitions hoặc incidents. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.13. Alternatives, trade-offs and reversibility: kiểm `Mechanism` bằng case 13, cụ thể mô hình alternatives, explicit trade-offs, reversibility và option value phải nêu actors, identities, state transitions và decision authority thay vì liệt kê công cụ

**Mệnh đề cần kiểm.** Alternatives, trade-offs and reversibility: kiểm `Mechanism` bằng case 13, cụ thể mô hình alternatives, explicit trade-offs, reversibility và option value phải nêu actors, identities, state transitions và decision authority thay vì liệt kê công cụ.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.alternatives-reversibility`, thử timezone, precision hoặc partition ở hai phía của ranh giới. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Alternatives, trade-offs and reversibility` công bố.

**Bằng chứng cần giữ.** Đối với probe 13 của `Alternatives, trade-offs and reversibility`, UTC/local interval và rounding policy phải hiện trong output. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.14. Alternatives, trade-offs and reversibility: kiểm `Boundary` bằng case 14, cụ thể kết luận về alternatives, explicit trade-offs, reversibility và option value chỉ đúng trong audience, workload, trust boundary, time window và version đã khóa

**Mệnh đề cần kiểm.** Alternatives, trade-offs and reversibility: kiểm `Boundary` bằng case 14, cụ thể kết luận về alternatives, explicit trade-offs, reversibility và option value chỉ đúng trong audience, workload, trust boundary, time window và version đã khóa.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.alternatives-reversibility`, đổi constraint đủ lớn để quyết định phải đảo. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Alternatives, trade-offs and reversibility` công bố.

**Bằng chứng cần giữ.** Đối với probe 14 của `Alternatives, trade-offs and reversibility`, ADR phải lưu changed constraint và reversal threshold. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.15. Alternatives, trade-offs and reversibility: kiểm `Failure mode` bằng case 15, cụ thể phân tích alternatives, explicit trade-offs, reversibility và option value cần tìm earliest failure, propagation path, blast radius và state hoặc claim còn đáng tin

**Mệnh đề cần kiểm.** Alternatives, trade-offs and reversibility: kiểm `Failure mode` bằng case 15, cụ thể phân tích alternatives, explicit trade-offs, reversibility và option value cần tìm earliest failure, propagation path, blast radius và state hoặc claim còn đáng tin.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.alternatives-reversibility`, chạy lại từ môi trường sạch với versions và seed đã khóa. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Alternatives, trade-offs and reversibility` công bố.

**Bằng chứng cần giữ.** Đối với probe 15 của `Alternatives, trade-offs and reversibility`, canonical result phải ổn định hoặc mọi nondeterminism phải được giải thích. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

## 8. Quy trình phản biện

1. Viết consumer-visible invariant cho `Alternatives, trade-offs and reversibility` trước khi chọn query hoặc tool.
2. Khóa grain, identity, population, time window và authoritative source.
3. Phân biệt declared configuration, executed state và published state.
4. Chạy negative control, replay hoặc changed-assumption case phù hợp.
5. Đối soát bằng oracle độc lập; công bố coverage và phần không quan sát được.
6. Gắn owner, hành động, reversal trigger và hạn review cho kết luận.

## 9. Câu hỏi tự kiểm tra

1. `Alternatives, trade-offs and reversibility: kiểm `Mechanism` bằng case 1, cụ thể mô hình alternatives, explicit trade-offs, reversibility và option value phải nêu actors, identities, state transitions và decision authority thay vì liệt kê công cụ` thất bại đầu tiên ở boundary nào?
2. Artifact nào mạnh nhất để trả lời `Alternatives, trade-offs and reversibility: kiểm `Failure mode` bằng case 3, cụ thể phân tích alternatives, explicit trade-offs, reversibility và option value cần tìm earliest failure, propagation path, blast radius và state hoặc claim còn đáng tin`?
3. Counterexample nhỏ nhất cho `Alternatives, trade-offs and reversibility: kiểm `Transfer test` bằng case 6, cụ thể bài thực hành alternatives, explicit trade-offs, reversibility và option value phải đổi một constraint hoặc inject counterexample rồi bảo vệ hoặc đảo quyết định bằng evidence` gồm những state nào?
4. `Alternatives, trade-offs and reversibility: kiểm `Failure mode` bằng case 9, cụ thể phân tích alternatives, explicit trade-offs, reversibility và option value cần tìm earliest failure, propagation path, blast radius và state hoặc claim còn đáng tin` có thể xanh giả ra sao?
5. Constraint nào khiến quyết định ở `Alternatives, trade-offs and reversibility: kiểm `Boundary` bằng case 14, cụ thể kết luận về alternatives, explicit trade-offs, reversibility và option value chỉ đúng trong audience, workload, trust boundary, time window và version đã khóa` phải đảo?
6. Phần nào của `Alternatives, trade-offs and reversibility: kiểm `Failure mode` bằng case 15, cụ thể phân tích alternatives, explicit trade-offs, reversibility và option value cần tìm earliest failure, propagation path, blast radius và state hoặc claim còn đáng tin` mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `Alternatives, trade-offs and reversibility` chưa chạy trên hệ thống production; nội dung là giáo trình và expected evidence.
- Hành vi phụ thuộc phiên bản, connector, scheduler, warehouse và catalog configuration phải được kiểm lại.
- Các ma trận, ladder và threshold do giáo trình tổng hợp không được gán nguyên văn cho vendor.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-MADR-TEMPLATES]]
2. [[SRC-HUNT-THOMAS-PRAGMATIC-PROGRAMMER-20AE]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-MADR-TEMPLATES]] | Contract hoặc cơ chế liên quan trực tiếp tới `Alternatives, trade-offs and reversibility` | Đã đọc locator; cần pin version khi chạy lab |
| [[SRC-HUNT-THOMAS-PRAGMATIC-PROGRAMMER-20AE]] | Contract hoặc cơ chế liên quan trực tiếp tới `Alternatives, trade-offs and reversibility` | Đã đọc locator; cần pin version khi chạy lab |

## Key takeaways
- Alternatives, explicit trade-offs, reversibility và option value phải được bảo vệ bằng explicit boundary, changed-constraint test và evidence có thể phản bác.
- Với `wiki.system-design.alternatives-reversibility`, quality của kết luận phụ thuộc identity, coverage và oracle chứ không phụ thuộc màu dashboard.
- Câu hỏi `Làm thế nào thiết kế, kiểm chứng và bảo vệ alternatives, explicit trade-offs, reversibility và option value mà không khẳng định vượt quá evidence?` chỉ được trả lời trong scope và version đã ghi.
- Các source IDs `src.web.madr-templates, src.book.hunt-thomas-pragmatic-programmer.20ae` đặt ranh giới cho source fact; phần còn lại là synthesis có nhãn.
- Trước khi lab chạy, đây là note đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.
