# Phase 10: System Design, AI Boundary and Trajectory
# Module 27: System Design Progression
# Lesson 408: The capacity sheet - assumptions and sensitivity

## Mục tiêu bài học

**Năng lực cần chứng minh.** Lập bảng năng lực có công thức cho một thiết kế và chỉ ra nút thắt đầu tiên cùng ngưỡng đổi kiến trúc.

**Điều kiện hoàn thành.** Mọi ô có công thức, nút thắt đầu tiên được chỉ ra kèm giả định, và ≥ 2 ngưỡng đổi kiến trúc được nêu kèm mô tả.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, kiểm chứng và vận hành capacity assumptions, units, bottlenecks, headroom và sensitivity analysis mà không khẳng định vượt quá evidence?

## 1. Mechanism

Mô hình capacity assumptions, units, bottlenecks, headroom và sensitivity analysis phải nêu actors, identities, state transitions và authority thay vì chỉ liệt kê components. Đừng bắt đầu bằng tên công cụ. Hãy bắt đầu bằng đối tượng được bảo vệ, boundary quan sát được và hậu quả nếu kết luận sai. Trong bài `The capacity sheet - assumptions and sensitivity`, câu hỏi thực dụng là: Làm thế nào mô hình, kiểm chứng và vận hành capacity assumptions, units, bottlenecks, headroom và sensitivity analysis mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 2. Boundary

Guarantee của capacity assumptions, units, bottlenecks, headroom và sensitivity analysis chỉ đúng trong workload, failure model, time window, trust boundary và version đã khóa. Điểm khó không nằm ở cú pháp mà ở identity và scope. Hai phép đo cùng tên vẫn có thể nói về hai population hoặc hai thời điểm khác nhau. Trong bài `The capacity sheet - assumptions and sensitivity`, câu hỏi thực dụng là: Làm thế nào mô hình, kiểm chứng và vận hành capacity assumptions, units, bottlenecks, headroom và sensitivity analysis mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 3. Failure mode

Phân tích capacity assumptions, units, bottlenecks, headroom và sensitivity analysis cần tìm earliest controllable failure, propagation path, blast radius và durable state còn tin cậy. Một dashboard xanh chỉ là tín hiệu. Muốn biến nó thành bằng chứng phải giữ input, phiên bản, rule, trạng thái trước–sau và cách tính độc lập. Trong bài `The capacity sheet - assumptions and sensitivity`, câu hỏi thực dụng là: Làm thế nào mô hình, kiểm chứng và vận hành capacity assumptions, units, bottlenecks, headroom và sensitivity analysis mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 4. Decision rule

Quyết định về capacity assumptions, units, bottlenecks, headroom và sensitivity analysis phải nối quantified requirements với alternatives, cost, complexity và reversal trigger. Thiết kế tốt phải chịu được counterexample. Hãy chủ động tạo case sát boundary, case thiếu dữ liệu và case replay thay vì chỉ chạy happy path. Trong bài `The capacity sheet - assumptions and sensitivity`, câu hỏi thực dụng là: Làm thế nào mô hình, kiểm chứng và vận hành capacity assumptions, units, bottlenecks, headroom và sensitivity analysis mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 5. Evidence

Bằng chứng cho capacity assumptions, units, bottlenecks, headroom và sensitivity analysis gồm input assumptions, stable identity, resolved design/config, raw observations và independent oracle. Chi phí vận hành thuộc contract. Một rule đúng nhưng quá đắt, quá ồn hoặc không có owner sẽ nhanh chóng bị tắt và mất tác dụng. Trong bài `The capacity sheet - assumptions and sensitivity`, câu hỏi thực dụng là: Làm thế nào mô hình, kiểm chứng và vận hành capacity assumptions, units, bottlenecks, headroom và sensitivity analysis mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 6. Recovery lab

Lab capacity assumptions, units, bottlenecks, headroom và sensitivity analysis phải inject failure hoặc đổi một assumption, phục hồi theo runbook rồi reconcile outcome với invariants. Kết luận cần có điều kiện đảo chiều. Khi volume, latency, nguồn thẩm quyền hoặc topology đổi, quyết định cũ phải được xem xét lại bằng cùng một oracle. Trong bài `The capacity sheet - assumptions and sensitivity`, câu hỏi thực dụng là: Làm thế nào mô hình, kiểm chứng và vận hành capacity assumptions, units, bottlenecks, headroom và sensitivity analysis mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 7. Ma trận kiểm chứng từng mệnh đề

Với `wiki.system-design.capacity-sheet`, command thành công không tự chứng minh dữ liệu đúng. Protocol riêng của bài là: Run a version-pinned model, sandbox or replayable fixture, change one assumption or inject one failure, retain raw state and event evidence, then reconcile the result against an independent invariant oracle. Mỗi probe dưới đây phải nối input boundary với failure signal và oracle có thể phản bác kết luận.

### 7.1. The capacity sheet - assumptions and sensitivity: kiểm `Mechanism` bằng case 1, cụ thể mô hình capacity assumptions, units, bottlenecks, headroom và sensitivity analysis phải nêu actors, identities, state transitions và authority thay vì chỉ liệt kê components

**Mệnh đề cần kiểm.** The capacity sheet - assumptions and sensitivity: kiểm `Mechanism` bằng case 1, cụ thể mô hình capacity assumptions, units, bottlenecks, headroom và sensitivity analysis phải nêu actors, identities, state transitions và authority thay vì chỉ liệt kê components.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.capacity-sheet`, tạo positive control và negative control chỉ khác đúng một điều kiện. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The capacity sheet - assumptions and sensitivity` công bố.

**Bằng chứng cần giữ.** Đối với probe 1 của `The capacity sheet - assumptions and sensitivity`, giữ fixture, raw failing rows và lệnh tái hiện. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.2. The capacity sheet - assumptions and sensitivity: kiểm `Boundary` bằng case 2, cụ thể guarantee của capacity assumptions, units, bottlenecks, headroom và sensitivity analysis chỉ đúng trong workload, failure model, time window, trust boundary và version đã khóa

**Mệnh đề cần kiểm.** The capacity sheet - assumptions and sensitivity: kiểm `Boundary` bằng case 2, cụ thể guarantee của capacity assumptions, units, bottlenecks, headroom và sensitivity analysis chỉ đúng trong workload, failure model, time window, trust boundary và version đã khóa.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.capacity-sheet`, đổi grain nhưng giữ tổng số dòng để lộ phép đo sai cấp. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The capacity sheet - assumptions and sensitivity` công bố.

**Bằng chứng cần giữ.** Đối với probe 2 của `The capacity sheet - assumptions and sensitivity`, báo numerator, denominator và key set ở cả hai grain. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.3. The capacity sheet - assumptions and sensitivity: kiểm `Failure mode` bằng case 3, cụ thể phân tích capacity assumptions, units, bottlenecks, headroom và sensitivity analysis cần tìm earliest controllable failure, propagation path, blast radius và durable state còn tin cậy

**Mệnh đề cần kiểm.** The capacity sheet - assumptions and sensitivity: kiểm `Failure mode` bằng case 3, cụ thể phân tích capacity assumptions, units, bottlenecks, headroom và sensitivity analysis cần tìm earliest controllable failure, propagation path, blast radius và durable state còn tin cậy.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.capacity-sheet`, đưa một giá trị tới đúng boundary và một giá trị vượt boundary. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The capacity sheet - assumptions and sensitivity` công bố.

**Bằng chứng cần giữ.** Đối với probe 3 của `The capacity sheet - assumptions and sensitivity`, lưu hai observed values cùng rule đã resolve. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.4. The capacity sheet - assumptions and sensitivity: kiểm `Decision rule` bằng case 4, cụ thể quyết định về capacity assumptions, units, bottlenecks, headroom và sensitivity analysis phải nối quantified requirements với alternatives, cost, complexity và reversal trigger

**Mệnh đề cần kiểm.** The capacity sheet - assumptions and sensitivity: kiểm `Decision rule` bằng case 4, cụ thể quyết định về capacity assumptions, units, bottlenecks, headroom và sensitivity analysis phải nối quantified requirements với alternatives, cost, complexity và reversal trigger.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.capacity-sheet`, kill tiến trình ngay trước rồi ngay sau durable side effect. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The capacity sheet - assumptions and sensitivity` công bố.

**Bằng chứng cần giữ.** Đối với probe 4 của `The capacity sheet - assumptions and sensitivity`, lưu checkpoint, external ledger và trạng thái sau restart. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.5. The capacity sheet - assumptions and sensitivity: kiểm `Evidence` bằng case 5, cụ thể bằng chứng cho capacity assumptions, units, bottlenecks, headroom và sensitivity analysis gồm input assumptions, stable identity, resolved design/config, raw observations và independent oracle

**Mệnh đề cần kiểm.** The capacity sheet - assumptions and sensitivity: kiểm `Evidence` bằng case 5, cụ thể bằng chứng cho capacity assumptions, units, bottlenecks, headroom và sensitivity analysis gồm input assumptions, stable identity, resolved design/config, raw observations và independent oracle.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.capacity-sheet`, đảo thứ tự input và concurrency nhưng giữ logical population. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The capacity sheet - assumptions and sensitivity` công bố.

**Bằng chứng cần giữ.** Đối với probe 5 của `The capacity sheet - assumptions and sensitivity`, so canonical hash và business totals giữa các thứ tự. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.6. The capacity sheet - assumptions and sensitivity: kiểm `Recovery lab` bằng case 6, cụ thể lab capacity assumptions, units, bottlenecks, headroom và sensitivity analysis phải inject failure hoặc đổi một assumption, phục hồi theo runbook rồi reconcile outcome với invariants

**Mệnh đề cần kiểm.** The capacity sheet - assumptions and sensitivity: kiểm `Recovery lab` bằng case 6, cụ thể lab capacity assumptions, units, bottlenecks, headroom và sensitivity analysis phải inject failure hoặc đổi một assumption, phục hồi theo runbook rồi reconcile outcome với invariants.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.capacity-sheet`, replay cùng identity với payload giống rồi payload xung đột. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The capacity sheet - assumptions and sensitivity` công bố.

**Bằng chứng cần giữ.** Đối với probe 6 của `The capacity sheet - assumptions and sensitivity`, tách duplicate replay khỏi identity collision bằng reason code. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.7. The capacity sheet - assumptions and sensitivity: kiểm `Mechanism` bằng case 7, cụ thể mô hình capacity assumptions, units, bottlenecks, headroom và sensitivity analysis phải nêu actors, identities, state transitions và authority thay vì chỉ liệt kê components

**Mệnh đề cần kiểm.** The capacity sheet - assumptions and sensitivity: kiểm `Mechanism` bằng case 7, cụ thể mô hình capacity assumptions, units, bottlenecks, headroom và sensitivity analysis phải nêu actors, identities, state transitions và authority thay vì chỉ liệt kê components.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.capacity-sheet`, thêm record tới trễ trong horizon và ngoài horizon. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The capacity sheet - assumptions and sensitivity` công bố.

**Bằng chứng cần giữ.** Đối với probe 7 của `The capacity sheet - assumptions and sensitivity`, báo accepted-late, rejected-late và oldest outstanding timestamp. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.8. The capacity sheet - assumptions and sensitivity: kiểm `Boundary` bằng case 8, cụ thể guarantee của capacity assumptions, units, bottlenecks, headroom và sensitivity analysis chỉ đúng trong workload, failure model, time window, trust boundary và version đã khóa

**Mệnh đề cần kiểm.** The capacity sheet - assumptions and sensitivity: kiểm `Boundary` bằng case 8, cụ thể guarantee của capacity assumptions, units, bottlenecks, headroom và sensitivity analysis chỉ đúng trong workload, failure model, time window, trust boundary và version đã khóa.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.capacity-sheet`, đổi schema theo một cách tương thích rồi một cách phá vỡ semantics. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The capacity sheet - assumptions and sensitivity` công bố.

**Bằng chứng cần giữ.** Đối với probe 8 của `The capacity sheet - assumptions and sensitivity`, giữ schema diff, classification và consumer-visible result. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.9. The capacity sheet - assumptions and sensitivity: kiểm `Failure mode` bằng case 9, cụ thể phân tích capacity assumptions, units, bottlenecks, headroom và sensitivity analysis cần tìm earliest controllable failure, propagation path, blast radius và durable state còn tin cậy

**Mệnh đề cần kiểm.** The capacity sheet - assumptions and sensitivity: kiểm `Failure mode` bằng case 9, cụ thể phân tích capacity assumptions, units, bottlenecks, headroom và sensitivity analysis cần tìm earliest controllable failure, propagation path, blast radius và durable state còn tin cậy.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.capacity-sheet`, tạo missing và duplicate bù nhau để count tổng không đổi. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The capacity sheet - assumptions and sensitivity` công bố.

**Bằng chứng cần giữ.** Đối với probe 9 của `The capacity sheet - assumptions and sensitivity`, so key multiset và typed hashes thay vì chỉ row count. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.10. The capacity sheet - assumptions and sensitivity: kiểm `Decision rule` bằng case 10, cụ thể quyết định về capacity assumptions, units, bottlenecks, headroom và sensitivity analysis phải nối quantified requirements với alternatives, cost, complexity và reversal trigger

**Mệnh đề cần kiểm.** The capacity sheet - assumptions and sensitivity: kiểm `Decision rule` bằng case 10, cụ thể quyết định về capacity assumptions, units, bottlenecks, headroom và sensitivity analysis phải nối quantified requirements với alternatives, cost, complexity và reversal trigger.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.capacity-sheet`, cho reviewer tái hiện chỉ từ evidence package. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The capacity sheet - assumptions and sensitivity` công bố.

**Bằng chứng cần giữ.** Đối với probe 10 của `The capacity sheet - assumptions and sensitivity`, package phải đủ để người khác dựng lại decision và limitation. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.11. The capacity sheet - assumptions and sensitivity: kiểm `Evidence` bằng case 11, cụ thể bằng chứng cho capacity assumptions, units, bottlenecks, headroom và sensitivity analysis gồm input assumptions, stable identity, resolved design/config, raw observations và independent oracle

**Mệnh đề cần kiểm.** The capacity sheet - assumptions and sensitivity: kiểm `Evidence` bằng case 11, cụ thể bằng chứng cho capacity assumptions, units, bottlenecks, headroom và sensitivity analysis gồm input assumptions, stable identity, resolved design/config, raw observations và independent oracle.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.capacity-sheet`, so với oracle độc lập không dùng chung query hoặc parser. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The capacity sheet - assumptions and sensitivity` công bố.

**Bằng chứng cần giữ.** Đối với probe 11 của `The capacity sheet - assumptions and sensitivity`, independent result phải khớp ở grain đã công bố. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.12. The capacity sheet - assumptions and sensitivity: kiểm `Recovery lab` bằng case 12, cụ thể lab capacity assumptions, units, bottlenecks, headroom và sensitivity analysis phải inject failure hoặc đổi một assumption, phục hồi theo runbook rồi reconcile outcome với invariants

**Mệnh đề cần kiểm.** The capacity sheet - assumptions and sensitivity: kiểm `Recovery lab` bằng case 12, cụ thể lab capacity assumptions, units, bottlenecks, headroom và sensitivity analysis phải inject failure hoặc đổi một assumption, phục hồi theo runbook rồi reconcile outcome với invariants.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.capacity-sheet`, chạy scope hẹp và population đầy đủ rồi công bố phần bị loại. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The capacity sheet - assumptions and sensitivity` công bố.

**Bằng chứng cần giữ.** Đối với probe 12 của `The capacity sheet - assumptions and sensitivity`, coverage phải nêu rõ excluded nodes, partitions hoặc incidents. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.13. The capacity sheet - assumptions and sensitivity: kiểm `Mechanism` bằng case 13, cụ thể mô hình capacity assumptions, units, bottlenecks, headroom và sensitivity analysis phải nêu actors, identities, state transitions và authority thay vì chỉ liệt kê components

**Mệnh đề cần kiểm.** The capacity sheet - assumptions and sensitivity: kiểm `Mechanism` bằng case 13, cụ thể mô hình capacity assumptions, units, bottlenecks, headroom và sensitivity analysis phải nêu actors, identities, state transitions và authority thay vì chỉ liệt kê components.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.capacity-sheet`, thử timezone, precision hoặc partition ở hai phía của ranh giới. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The capacity sheet - assumptions and sensitivity` công bố.

**Bằng chứng cần giữ.** Đối với probe 13 của `The capacity sheet - assumptions and sensitivity`, UTC/local interval và rounding policy phải hiện trong output. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.14. The capacity sheet - assumptions and sensitivity: kiểm `Boundary` bằng case 14, cụ thể guarantee của capacity assumptions, units, bottlenecks, headroom và sensitivity analysis chỉ đúng trong workload, failure model, time window, trust boundary và version đã khóa

**Mệnh đề cần kiểm.** The capacity sheet - assumptions and sensitivity: kiểm `Boundary` bằng case 14, cụ thể guarantee của capacity assumptions, units, bottlenecks, headroom và sensitivity analysis chỉ đúng trong workload, failure model, time window, trust boundary và version đã khóa.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.capacity-sheet`, đổi constraint đủ lớn để quyết định phải đảo. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The capacity sheet - assumptions and sensitivity` công bố.

**Bằng chứng cần giữ.** Đối với probe 14 của `The capacity sheet - assumptions and sensitivity`, ADR phải lưu changed constraint và reversal threshold. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.15. The capacity sheet - assumptions and sensitivity: kiểm `Failure mode` bằng case 15, cụ thể phân tích capacity assumptions, units, bottlenecks, headroom và sensitivity analysis cần tìm earliest controllable failure, propagation path, blast radius và durable state còn tin cậy

**Mệnh đề cần kiểm.** The capacity sheet - assumptions and sensitivity: kiểm `Failure mode` bằng case 15, cụ thể phân tích capacity assumptions, units, bottlenecks, headroom và sensitivity analysis cần tìm earliest controllable failure, propagation path, blast radius và durable state còn tin cậy.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.capacity-sheet`, chạy lại từ môi trường sạch với versions và seed đã khóa. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The capacity sheet - assumptions and sensitivity` công bố.

**Bằng chứng cần giữ.** Đối với probe 15 của `The capacity sheet - assumptions and sensitivity`, canonical result phải ổn định hoặc mọi nondeterminism phải được giải thích. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

## 8. Quy trình phản biện

1. Viết consumer-visible invariant cho `The capacity sheet - assumptions and sensitivity` trước khi chọn query hoặc tool.
2. Khóa grain, identity, population, time window và authoritative source.
3. Phân biệt declared configuration, executed state và published state.
4. Chạy negative control, replay hoặc changed-assumption case phù hợp.
5. Đối soát bằng oracle độc lập; công bố coverage và phần không quan sát được.
6. Gắn owner, hành động, reversal trigger và hạn review cho kết luận.

## 9. Câu hỏi tự kiểm tra

1. `The capacity sheet - assumptions and sensitivity: kiểm `Mechanism` bằng case 1, cụ thể mô hình capacity assumptions, units, bottlenecks, headroom và sensitivity analysis phải nêu actors, identities, state transitions và authority thay vì chỉ liệt kê components` thất bại đầu tiên ở boundary nào?
2. Artifact nào mạnh nhất để trả lời `The capacity sheet - assumptions and sensitivity: kiểm `Failure mode` bằng case 3, cụ thể phân tích capacity assumptions, units, bottlenecks, headroom và sensitivity analysis cần tìm earliest controllable failure, propagation path, blast radius và durable state còn tin cậy`?
3. Counterexample nhỏ nhất cho `The capacity sheet - assumptions and sensitivity: kiểm `Recovery lab` bằng case 6, cụ thể lab capacity assumptions, units, bottlenecks, headroom và sensitivity analysis phải inject failure hoặc đổi một assumption, phục hồi theo runbook rồi reconcile outcome với invariants` gồm những state nào?
4. `The capacity sheet - assumptions and sensitivity: kiểm `Failure mode` bằng case 9, cụ thể phân tích capacity assumptions, units, bottlenecks, headroom và sensitivity analysis cần tìm earliest controllable failure, propagation path, blast radius và durable state còn tin cậy` có thể xanh giả ra sao?
5. Constraint nào khiến quyết định ở `The capacity sheet - assumptions and sensitivity: kiểm `Boundary` bằng case 14, cụ thể guarantee của capacity assumptions, units, bottlenecks, headroom và sensitivity analysis chỉ đúng trong workload, failure model, time window, trust boundary và version đã khóa` phải đảo?
6. Phần nào của `The capacity sheet - assumptions and sensitivity: kiểm `Failure mode` bằng case 15, cụ thể phân tích capacity assumptions, units, bottlenecks, headroom và sensitivity analysis cần tìm earliest controllable failure, propagation path, blast radius và durable state còn tin cậy` mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `The capacity sheet - assumptions and sensitivity` chưa chạy trên hệ thống production; nội dung là giáo trình và expected evidence.
- Hành vi phụ thuộc phiên bản, connector, scheduler, warehouse và catalog configuration phải được kiểm lại.
- Các ma trận, ladder và threshold do giáo trình tổng hợp không được gán nguyên văn cho vendor.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-GOOGLE-SRE-CAPACITY-LOAD-TESTING]]
2. [[SRC-AWS-BUDGETS]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-GOOGLE-SRE-CAPACITY-LOAD-TESTING]] | Contract hoặc cơ chế liên quan trực tiếp tới `The capacity sheet - assumptions and sensitivity` | Đã đọc locator; cần pin version khi chạy lab |
| [[SRC-AWS-BUDGETS]] | Contract hoặc cơ chế liên quan trực tiếp tới `The capacity sheet - assumptions and sensitivity` | Đã đọc locator; cần pin version khi chạy lab |

## Key takeaways
- Capacity assumptions, units, bottlenecks, headroom và sensitivity analysis phải được bảo vệ bằng quantified boundary, counterexample và evidence có thể phản bác.
- Với `wiki.system-design.capacity-sheet`, quality của kết luận phụ thuộc identity, coverage và oracle chứ không phụ thuộc màu dashboard.
- Câu hỏi `Làm thế nào mô hình, kiểm chứng và vận hành capacity assumptions, units, bottlenecks, headroom và sensitivity analysis mà không khẳng định vượt quá evidence?` chỉ được trả lời trong scope và version đã ghi.
- Các source IDs `src.web.google-sre-capacity-load-testing, src.web.aws-budgets` đặt ranh giới cho source fact; phần còn lại là synthesis có nhãn.
- Trước khi lab chạy, đây là note đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.
