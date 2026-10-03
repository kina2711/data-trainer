# Phase 10: System Design, AI Boundary and Trajectory
# Module 27: System Design Progression
# Lesson 420: Capstone design dossier - RFC, spike and ADRs

## Mục tiêu bài học

**Năng lực cần chứng minh.** Nộp hồ sơ thiết kế đủ sáu phần, có thử nghiệm nhỏ chạy được và mọi thành phần truy được về một yêu cầu.

**Điều kiện hoàn thành.** Sáu phần đầy đủ, mọi thành phần truy được về một yêu cầu hoặc bảo đảm, thử nghiệm nhỏ chạy thật có kết quả báo cáo trung thực, và bốn ràng buộc đổi được trả lời.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào thiết kế, kiểm chứng và bảo vệ capstone dossier nối RFC, spike evidence và ADRs mà không khẳng định vượt quá evidence?

## 1. Mechanism

Mô hình capstone dossier nối RFC, spike evidence và ADRs phải nêu actors, identities, state transitions và decision authority thay vì liệt kê công cụ. Đừng bắt đầu bằng tên công cụ. Hãy bắt đầu bằng đối tượng được bảo vệ, boundary quan sát được và hậu quả nếu kết luận sai. Trong bài `Capstone design dossier - RFC, spike and ADRs`, câu hỏi thực dụng là: Làm thế nào thiết kế, kiểm chứng và bảo vệ capstone dossier nối RFC, spike evidence và ADRs mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 2. Boundary

Kết luận về capstone dossier nối RFC, spike evidence và ADRs chỉ đúng trong audience, workload, trust boundary, time window và version đã khóa. Điểm khó không nằm ở cú pháp mà ở identity và scope. Hai phép đo cùng tên vẫn có thể nói về hai population hoặc hai thời điểm khác nhau. Trong bài `Capstone design dossier - RFC, spike and ADRs`, câu hỏi thực dụng là: Làm thế nào thiết kế, kiểm chứng và bảo vệ capstone dossier nối RFC, spike evidence và ADRs mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 3. Failure mode

Phân tích capstone dossier nối RFC, spike evidence và ADRs cần tìm earliest failure, propagation path, blast radius và state hoặc claim còn đáng tin. Một dashboard xanh chỉ là tín hiệu. Muốn biến nó thành bằng chứng phải giữ input, phiên bản, rule, trạng thái trước–sau và cách tính độc lập. Trong bài `Capstone design dossier - RFC, spike and ADRs`, câu hỏi thực dụng là: Làm thế nào thiết kế, kiểm chứng và bảo vệ capstone dossier nối RFC, spike evidence và ADRs mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 4. Decision rule

Quyết định về capstone dossier nối RFC, spike evidence và ADRs phải nối quantified constraints với alternatives, trade-offs và reversal trigger. Thiết kế tốt phải chịu được counterexample. Hãy chủ động tạo case sát boundary, case thiếu dữ liệu và case replay thay vì chỉ chạy happy path. Trong bài `Capstone design dossier - RFC, spike and ADRs`, câu hỏi thực dụng là: Làm thế nào thiết kế, kiểm chứng và bảo vệ capstone dossier nối RFC, spike evidence và ADRs mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 5. Evidence

Bằng chứng cho capstone dossier nối RFC, spike evidence và ADRs gồm inputs có version, stable identity, raw observations, reviewer-visible limitations và independent oracle. Chi phí vận hành thuộc contract. Một rule đúng nhưng quá đắt, quá ồn hoặc không có owner sẽ nhanh chóng bị tắt và mất tác dụng. Trong bài `Capstone design dossier - RFC, spike and ADRs`, câu hỏi thực dụng là: Làm thế nào thiết kế, kiểm chứng và bảo vệ capstone dossier nối RFC, spike evidence và ADRs mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 6. Transfer test

Bài thực hành capstone dossier nối RFC, spike evidence và ADRs phải đổi một constraint hoặc inject counterexample rồi bảo vệ hoặc đảo quyết định bằng evidence. Kết luận cần có điều kiện đảo chiều. Khi volume, latency, nguồn thẩm quyền hoặc topology đổi, quyết định cũ phải được xem xét lại bằng cùng một oracle. Trong bài `Capstone design dossier - RFC, spike and ADRs`, câu hỏi thực dụng là: Làm thế nào thiết kế, kiểm chứng và bảo vệ capstone dossier nối RFC, spike evidence và ADRs mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 7. Ma trận kiểm chứng từng mệnh đề

Với `wiki.system-design.capstone-dossier`, command thành công không tự chứng minh dữ liệu đúng. Protocol riêng của bài là: Run a version-pinned model, evaluation corpus or review simulation, change one material constraint, retain raw evidence and reconcile the recommendation against an independent rubric or invariant oracle. Mỗi probe dưới đây phải nối input boundary với failure signal và oracle có thể phản bác kết luận.

### 7.1. Capstone design dossier - RFC, spike and ADRs: kiểm `Mechanism` bằng case 1, cụ thể mô hình capstone dossier nối rfc, spike evidence và adrs phải nêu actors, identities, state transitions và decision authority thay vì liệt kê công cụ

**Mệnh đề cần kiểm.** Capstone design dossier - RFC, spike and ADRs: kiểm `Mechanism` bằng case 1, cụ thể mô hình capstone dossier nối rfc, spike evidence và adrs phải nêu actors, identities, state transitions và decision authority thay vì liệt kê công cụ.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.capstone-dossier`, tạo positive control và negative control chỉ khác đúng một điều kiện. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Capstone design dossier - RFC, spike and ADRs` công bố.

**Bằng chứng cần giữ.** Đối với probe 1 của `Capstone design dossier - RFC, spike and ADRs`, giữ fixture, raw failing rows và lệnh tái hiện. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.2. Capstone design dossier - RFC, spike and ADRs: kiểm `Boundary` bằng case 2, cụ thể kết luận về capstone dossier nối rfc, spike evidence và adrs chỉ đúng trong audience, workload, trust boundary, time window và version đã khóa

**Mệnh đề cần kiểm.** Capstone design dossier - RFC, spike and ADRs: kiểm `Boundary` bằng case 2, cụ thể kết luận về capstone dossier nối rfc, spike evidence và adrs chỉ đúng trong audience, workload, trust boundary, time window và version đã khóa.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.capstone-dossier`, đổi grain nhưng giữ tổng số dòng để lộ phép đo sai cấp. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Capstone design dossier - RFC, spike and ADRs` công bố.

**Bằng chứng cần giữ.** Đối với probe 2 của `Capstone design dossier - RFC, spike and ADRs`, báo numerator, denominator và key set ở cả hai grain. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.3. Capstone design dossier - RFC, spike and ADRs: kiểm `Failure mode` bằng case 3, cụ thể phân tích capstone dossier nối rfc, spike evidence và adrs cần tìm earliest failure, propagation path, blast radius và state hoặc claim còn đáng tin

**Mệnh đề cần kiểm.** Capstone design dossier - RFC, spike and ADRs: kiểm `Failure mode` bằng case 3, cụ thể phân tích capstone dossier nối rfc, spike evidence và adrs cần tìm earliest failure, propagation path, blast radius và state hoặc claim còn đáng tin.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.capstone-dossier`, đưa một giá trị tới đúng boundary và một giá trị vượt boundary. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Capstone design dossier - RFC, spike and ADRs` công bố.

**Bằng chứng cần giữ.** Đối với probe 3 của `Capstone design dossier - RFC, spike and ADRs`, lưu hai observed values cùng rule đã resolve. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.4. Capstone design dossier - RFC, spike and ADRs: kiểm `Decision rule` bằng case 4, cụ thể quyết định về capstone dossier nối rfc, spike evidence và adrs phải nối quantified constraints với alternatives, trade-offs và reversal trigger

**Mệnh đề cần kiểm.** Capstone design dossier - RFC, spike and ADRs: kiểm `Decision rule` bằng case 4, cụ thể quyết định về capstone dossier nối rfc, spike evidence và adrs phải nối quantified constraints với alternatives, trade-offs và reversal trigger.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.capstone-dossier`, kill tiến trình ngay trước rồi ngay sau durable side effect. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Capstone design dossier - RFC, spike and ADRs` công bố.

**Bằng chứng cần giữ.** Đối với probe 4 của `Capstone design dossier - RFC, spike and ADRs`, lưu checkpoint, external ledger và trạng thái sau restart. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.5. Capstone design dossier - RFC, spike and ADRs: kiểm `Evidence` bằng case 5, cụ thể bằng chứng cho capstone dossier nối rfc, spike evidence và adrs gồm inputs có version, stable identity, raw observations, reviewer-visible limitations và independent oracle

**Mệnh đề cần kiểm.** Capstone design dossier - RFC, spike and ADRs: kiểm `Evidence` bằng case 5, cụ thể bằng chứng cho capstone dossier nối rfc, spike evidence và adrs gồm inputs có version, stable identity, raw observations, reviewer-visible limitations và independent oracle.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.capstone-dossier`, đảo thứ tự input và concurrency nhưng giữ logical population. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Capstone design dossier - RFC, spike and ADRs` công bố.

**Bằng chứng cần giữ.** Đối với probe 5 của `Capstone design dossier - RFC, spike and ADRs`, so canonical hash và business totals giữa các thứ tự. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.6. Capstone design dossier - RFC, spike and ADRs: kiểm `Transfer test` bằng case 6, cụ thể bài thực hành capstone dossier nối rfc, spike evidence và adrs phải đổi một constraint hoặc inject counterexample rồi bảo vệ hoặc đảo quyết định bằng evidence

**Mệnh đề cần kiểm.** Capstone design dossier - RFC, spike and ADRs: kiểm `Transfer test` bằng case 6, cụ thể bài thực hành capstone dossier nối rfc, spike evidence và adrs phải đổi một constraint hoặc inject counterexample rồi bảo vệ hoặc đảo quyết định bằng evidence.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.capstone-dossier`, replay cùng identity với payload giống rồi payload xung đột. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Capstone design dossier - RFC, spike and ADRs` công bố.

**Bằng chứng cần giữ.** Đối với probe 6 của `Capstone design dossier - RFC, spike and ADRs`, tách duplicate replay khỏi identity collision bằng reason code. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.7. Capstone design dossier - RFC, spike and ADRs: kiểm `Mechanism` bằng case 7, cụ thể mô hình capstone dossier nối rfc, spike evidence và adrs phải nêu actors, identities, state transitions và decision authority thay vì liệt kê công cụ

**Mệnh đề cần kiểm.** Capstone design dossier - RFC, spike and ADRs: kiểm `Mechanism` bằng case 7, cụ thể mô hình capstone dossier nối rfc, spike evidence và adrs phải nêu actors, identities, state transitions và decision authority thay vì liệt kê công cụ.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.capstone-dossier`, thêm record tới trễ trong horizon và ngoài horizon. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Capstone design dossier - RFC, spike and ADRs` công bố.

**Bằng chứng cần giữ.** Đối với probe 7 của `Capstone design dossier - RFC, spike and ADRs`, báo accepted-late, rejected-late và oldest outstanding timestamp. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.8. Capstone design dossier - RFC, spike and ADRs: kiểm `Boundary` bằng case 8, cụ thể kết luận về capstone dossier nối rfc, spike evidence và adrs chỉ đúng trong audience, workload, trust boundary, time window và version đã khóa

**Mệnh đề cần kiểm.** Capstone design dossier - RFC, spike and ADRs: kiểm `Boundary` bằng case 8, cụ thể kết luận về capstone dossier nối rfc, spike evidence và adrs chỉ đúng trong audience, workload, trust boundary, time window và version đã khóa.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.capstone-dossier`, đổi schema theo một cách tương thích rồi một cách phá vỡ semantics. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Capstone design dossier - RFC, spike and ADRs` công bố.

**Bằng chứng cần giữ.** Đối với probe 8 của `Capstone design dossier - RFC, spike and ADRs`, giữ schema diff, classification và consumer-visible result. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.9. Capstone design dossier - RFC, spike and ADRs: kiểm `Failure mode` bằng case 9, cụ thể phân tích capstone dossier nối rfc, spike evidence và adrs cần tìm earliest failure, propagation path, blast radius và state hoặc claim còn đáng tin

**Mệnh đề cần kiểm.** Capstone design dossier - RFC, spike and ADRs: kiểm `Failure mode` bằng case 9, cụ thể phân tích capstone dossier nối rfc, spike evidence và adrs cần tìm earliest failure, propagation path, blast radius và state hoặc claim còn đáng tin.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.capstone-dossier`, tạo missing và duplicate bù nhau để count tổng không đổi. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Capstone design dossier - RFC, spike and ADRs` công bố.

**Bằng chứng cần giữ.** Đối với probe 9 của `Capstone design dossier - RFC, spike and ADRs`, so key multiset và typed hashes thay vì chỉ row count. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.10. Capstone design dossier - RFC, spike and ADRs: kiểm `Decision rule` bằng case 10, cụ thể quyết định về capstone dossier nối rfc, spike evidence và adrs phải nối quantified constraints với alternatives, trade-offs và reversal trigger

**Mệnh đề cần kiểm.** Capstone design dossier - RFC, spike and ADRs: kiểm `Decision rule` bằng case 10, cụ thể quyết định về capstone dossier nối rfc, spike evidence và adrs phải nối quantified constraints với alternatives, trade-offs và reversal trigger.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.capstone-dossier`, cho reviewer tái hiện chỉ từ evidence package. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Capstone design dossier - RFC, spike and ADRs` công bố.

**Bằng chứng cần giữ.** Đối với probe 10 của `Capstone design dossier - RFC, spike and ADRs`, package phải đủ để người khác dựng lại decision và limitation. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.11. Capstone design dossier - RFC, spike and ADRs: kiểm `Evidence` bằng case 11, cụ thể bằng chứng cho capstone dossier nối rfc, spike evidence và adrs gồm inputs có version, stable identity, raw observations, reviewer-visible limitations và independent oracle

**Mệnh đề cần kiểm.** Capstone design dossier - RFC, spike and ADRs: kiểm `Evidence` bằng case 11, cụ thể bằng chứng cho capstone dossier nối rfc, spike evidence và adrs gồm inputs có version, stable identity, raw observations, reviewer-visible limitations và independent oracle.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.capstone-dossier`, so với oracle độc lập không dùng chung query hoặc parser. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Capstone design dossier - RFC, spike and ADRs` công bố.

**Bằng chứng cần giữ.** Đối với probe 11 của `Capstone design dossier - RFC, spike and ADRs`, independent result phải khớp ở grain đã công bố. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.12. Capstone design dossier - RFC, spike and ADRs: kiểm `Transfer test` bằng case 12, cụ thể bài thực hành capstone dossier nối rfc, spike evidence và adrs phải đổi một constraint hoặc inject counterexample rồi bảo vệ hoặc đảo quyết định bằng evidence

**Mệnh đề cần kiểm.** Capstone design dossier - RFC, spike and ADRs: kiểm `Transfer test` bằng case 12, cụ thể bài thực hành capstone dossier nối rfc, spike evidence và adrs phải đổi một constraint hoặc inject counterexample rồi bảo vệ hoặc đảo quyết định bằng evidence.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.capstone-dossier`, chạy scope hẹp và population đầy đủ rồi công bố phần bị loại. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Capstone design dossier - RFC, spike and ADRs` công bố.

**Bằng chứng cần giữ.** Đối với probe 12 của `Capstone design dossier - RFC, spike and ADRs`, coverage phải nêu rõ excluded nodes, partitions hoặc incidents. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.13. Capstone design dossier - RFC, spike and ADRs: kiểm `Mechanism` bằng case 13, cụ thể mô hình capstone dossier nối rfc, spike evidence và adrs phải nêu actors, identities, state transitions và decision authority thay vì liệt kê công cụ

**Mệnh đề cần kiểm.** Capstone design dossier - RFC, spike and ADRs: kiểm `Mechanism` bằng case 13, cụ thể mô hình capstone dossier nối rfc, spike evidence và adrs phải nêu actors, identities, state transitions và decision authority thay vì liệt kê công cụ.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.capstone-dossier`, thử timezone, precision hoặc partition ở hai phía của ranh giới. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Capstone design dossier - RFC, spike and ADRs` công bố.

**Bằng chứng cần giữ.** Đối với probe 13 của `Capstone design dossier - RFC, spike and ADRs`, UTC/local interval và rounding policy phải hiện trong output. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.14. Capstone design dossier - RFC, spike and ADRs: kiểm `Boundary` bằng case 14, cụ thể kết luận về capstone dossier nối rfc, spike evidence và adrs chỉ đúng trong audience, workload, trust boundary, time window và version đã khóa

**Mệnh đề cần kiểm.** Capstone design dossier - RFC, spike and ADRs: kiểm `Boundary` bằng case 14, cụ thể kết luận về capstone dossier nối rfc, spike evidence và adrs chỉ đúng trong audience, workload, trust boundary, time window và version đã khóa.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.capstone-dossier`, đổi constraint đủ lớn để quyết định phải đảo. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Capstone design dossier - RFC, spike and ADRs` công bố.

**Bằng chứng cần giữ.** Đối với probe 14 của `Capstone design dossier - RFC, spike and ADRs`, ADR phải lưu changed constraint và reversal threshold. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.15. Capstone design dossier - RFC, spike and ADRs: kiểm `Failure mode` bằng case 15, cụ thể phân tích capstone dossier nối rfc, spike evidence và adrs cần tìm earliest failure, propagation path, blast radius và state hoặc claim còn đáng tin

**Mệnh đề cần kiểm.** Capstone design dossier - RFC, spike and ADRs: kiểm `Failure mode` bằng case 15, cụ thể phân tích capstone dossier nối rfc, spike evidence và adrs cần tìm earliest failure, propagation path, blast radius và state hoặc claim còn đáng tin.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.system-design.capstone-dossier`, chạy lại từ môi trường sạch với versions và seed đã khóa. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Capstone design dossier - RFC, spike and ADRs` công bố.

**Bằng chứng cần giữ.** Đối với probe 15 của `Capstone design dossier - RFC, spike and ADRs`, canonical result phải ổn định hoặc mọi nondeterminism phải được giải thích. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

## 8. Quy trình phản biện

1. Viết consumer-visible invariant cho `Capstone design dossier - RFC, spike and ADRs` trước khi chọn query hoặc tool.
2. Khóa grain, identity, population, time window và authoritative source.
3. Phân biệt declared configuration, executed state và published state.
4. Chạy negative control, replay hoặc changed-assumption case phù hợp.
5. Đối soát bằng oracle độc lập; công bố coverage và phần không quan sát được.
6. Gắn owner, hành động, reversal trigger và hạn review cho kết luận.

## 9. Câu hỏi tự kiểm tra

1. `Capstone design dossier - RFC, spike and ADRs: kiểm `Mechanism` bằng case 1, cụ thể mô hình capstone dossier nối rfc, spike evidence và adrs phải nêu actors, identities, state transitions và decision authority thay vì liệt kê công cụ` thất bại đầu tiên ở boundary nào?
2. Artifact nào mạnh nhất để trả lời `Capstone design dossier - RFC, spike and ADRs: kiểm `Failure mode` bằng case 3, cụ thể phân tích capstone dossier nối rfc, spike evidence và adrs cần tìm earliest failure, propagation path, blast radius và state hoặc claim còn đáng tin`?
3. Counterexample nhỏ nhất cho `Capstone design dossier - RFC, spike and ADRs: kiểm `Transfer test` bằng case 6, cụ thể bài thực hành capstone dossier nối rfc, spike evidence và adrs phải đổi một constraint hoặc inject counterexample rồi bảo vệ hoặc đảo quyết định bằng evidence` gồm những state nào?
4. `Capstone design dossier - RFC, spike and ADRs: kiểm `Failure mode` bằng case 9, cụ thể phân tích capstone dossier nối rfc, spike evidence và adrs cần tìm earliest failure, propagation path, blast radius và state hoặc claim còn đáng tin` có thể xanh giả ra sao?
5. Constraint nào khiến quyết định ở `Capstone design dossier - RFC, spike and ADRs: kiểm `Boundary` bằng case 14, cụ thể kết luận về capstone dossier nối rfc, spike evidence và adrs chỉ đúng trong audience, workload, trust boundary, time window và version đã khóa` phải đảo?
6. Phần nào của `Capstone design dossier - RFC, spike and ADRs: kiểm `Failure mode` bằng case 15, cụ thể phân tích capstone dossier nối rfc, spike evidence và adrs cần tìm earliest failure, propagation path, blast radius và state hoặc claim còn đáng tin` mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `Capstone design dossier - RFC, spike and ADRs` chưa chạy trên hệ thống production; nội dung là giáo trình và expected evidence.
- Hành vi phụ thuộc phiên bản, connector, scheduler, warehouse và catalog configuration phải được kiểm lại.
- Các ma trận, ladder và threshold do giáo trình tổng hợp không được gán nguyên văn cho vendor.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-MADR-TEMPLATES]]
2. [[SRC-HUNT-THOMAS-PRAGMATIC-PROGRAMMER-20AE]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-MADR-TEMPLATES]] | Contract hoặc cơ chế liên quan trực tiếp tới `Capstone design dossier - RFC, spike and ADRs` | Đã đọc locator; cần pin version khi chạy lab |
| [[SRC-HUNT-THOMAS-PRAGMATIC-PROGRAMMER-20AE]] | Contract hoặc cơ chế liên quan trực tiếp tới `Capstone design dossier - RFC, spike and ADRs` | Đã đọc locator; cần pin version khi chạy lab |

## Key takeaways
- Capstone dossier nối rfc, spike evidence và adrs phải được bảo vệ bằng explicit boundary, changed-constraint test và evidence có thể phản bác.
- Với `wiki.system-design.capstone-dossier`, quality của kết luận phụ thuộc identity, coverage và oracle chứ không phụ thuộc màu dashboard.
- Câu hỏi `Làm thế nào thiết kế, kiểm chứng và bảo vệ capstone dossier nối RFC, spike evidence và ADRs mà không khẳng định vượt quá evidence?` chỉ được trả lời trong scope và version đã ghi.
- Các source IDs `src.web.madr-templates, src.book.hunt-thomas-pragmatic-programmer.20ae` đặt ranh giới cho source fact; phần còn lại là synthesis có nhãn.
- Trước khi lab chạy, đây là note đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.
