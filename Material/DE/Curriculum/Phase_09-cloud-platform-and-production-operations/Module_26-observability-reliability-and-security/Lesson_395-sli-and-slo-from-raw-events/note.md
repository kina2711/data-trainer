# Phase 9: Cloud Platform and Production Operations
# Module 26: Observability, Reliability and Security
# Lesson 395: SLI and SLO from raw events

## Mục tiêu bài học

**Năng lực cần chứng minh.** Định nghĩa ba chỉ số phục vụ từ dữ liệu sự kiện thô với bốn phần tường minh và ngưỡng dẫn từ dữ liệu.

**Điều kiện hoàn thành.** Ba chỉ số cho cùng con số khi hai người tính độc lập, ngưỡng dẫn từ dữ liệu hành vi, và tình huống khả dụng cao mà tính đúng thấp được tái hiện.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, kiểm chứng và vận hành SLI numerator, denominator và SLO window từ raw events mà không khẳng định vượt quá evidence?

## 1. Mechanism

Mô hình SLI numerator, denominator và SLO window từ raw events phải chỉ rõ actors, identities, state transitions và control loop thay vì dừng ở tên object hay tool. Đừng bắt đầu bằng tên công cụ. Hãy bắt đầu bằng đối tượng được bảo vệ, boundary quan sát được và hậu quả nếu kết luận sai. Trong bài `SLI and SLO from raw events`, câu hỏi thực dụng là: Làm thế nào mô hình, kiểm chứng và vận hành SLI numerator, denominator và SLO window từ raw events mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 2. Boundary

Guarantee của SLI numerator, denominator và SLO window từ raw events chỉ đúng trong scope, time window, failure domain, permissions và version đã khóa. Điểm khó không nằm ở cú pháp mà ở identity và scope. Hai phép đo cùng tên vẫn có thể nói về hai population hoặc hai thời điểm khác nhau. Trong bài `SLI and SLO from raw events`, câu hỏi thực dụng là: Làm thế nào mô hình, kiểm chứng và vận hành SLI numerator, denominator và SLO window từ raw events mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 3. Failure mode

Phân tích SLI numerator, denominator và SLO window từ raw events cần tìm earliest observable failure, propagation path, blast radius và state còn đáng tin. Một dashboard xanh chỉ là tín hiệu. Muốn biến nó thành bằng chứng phải giữ input, phiên bản, rule, trạng thái trước–sau và cách tính độc lập. Trong bài `SLI and SLO from raw events`, câu hỏi thực dụng là: Làm thế nào mô hình, kiểm chứng và vận hành SLI numerator, denominator và SLO window từ raw events mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 4. Decision rule

Quyết định về SLI numerator, denominator và SLO window từ raw events phải nối user impact và constraints với alternatives, trade-offs và reversal trigger. Thiết kế tốt phải chịu được counterexample. Hãy chủ động tạo case sát boundary, case thiếu dữ liệu và case replay thay vì chỉ chạy happy path. Trong bài `SLI and SLO from raw events`, câu hỏi thực dụng là: Làm thế nào mô hình, kiểm chứng và vận hành SLI numerator, denominator và SLO window từ raw events mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 5. Evidence

Bằng chứng cho SLI numerator, denominator và SLO window từ raw events gồm stable identity, resolved configuration, telemetry thô, state trước–sau và independent oracle. Chi phí vận hành thuộc contract. Một rule đúng nhưng quá đắt, quá ồn hoặc không có owner sẽ nhanh chóng bị tắt và mất tác dụng. Trong bài `SLI and SLO from raw events`, câu hỏi thực dụng là: Làm thế nào mô hình, kiểm chứng và vận hành SLI numerator, denominator và SLO window từ raw events mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 6. Recovery lab

Lab SLI numerator, denominator và SLO window từ raw events phải inject failure hoặc changed assumption, phục hồi theo runbook rồi reconcile outcome với invariant. Kết luận cần có điều kiện đảo chiều. Khi volume, latency, nguồn thẩm quyền hoặc topology đổi, quyết định cũ phải được xem xét lại bằng cùng một oracle. Trong bài `SLI and SLO from raw events`, câu hỏi thực dụng là: Làm thế nào mô hình, kiểm chứng và vận hành SLI numerator, denominator và SLO window từ raw events mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 7. Ma trận kiểm chứng từng mệnh đề

Với `wiki.sre.sli-slo-raw-events`, command thành công không tự chứng minh dữ liệu đúng. Protocol riêng của bài là: Run a version-pinned sandbox or replayable fixture, inject one declared failure or changed constraint, retain raw object and telemetry evidence, then reconcile final state against an independent oracle. Mỗi probe dưới đây phải nối input boundary với failure signal và oracle có thể phản bác kết luận.

### 7.1. SLI and SLO from raw events: kiểm `Mechanism` bằng case 1, cụ thể mô hình sli numerator, denominator và slo window từ raw events phải chỉ rõ actors, identities, state transitions và control loop thay vì dừng ở tên object hay tool

**Mệnh đề cần kiểm.** SLI and SLO from raw events: kiểm `Mechanism` bằng case 1, cụ thể mô hình sli numerator, denominator và slo window từ raw events phải chỉ rõ actors, identities, state transitions và control loop thay vì dừng ở tên object hay tool.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.sre.sli-slo-raw-events`, tạo positive control và negative control chỉ khác đúng một điều kiện. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `SLI and SLO from raw events` công bố.

**Bằng chứng cần giữ.** Đối với probe 1 của `SLI and SLO from raw events`, giữ fixture, raw failing rows và lệnh tái hiện. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.2. SLI and SLO from raw events: kiểm `Boundary` bằng case 2, cụ thể guarantee của sli numerator, denominator và slo window từ raw events chỉ đúng trong scope, time window, failure domain, permissions và version đã khóa

**Mệnh đề cần kiểm.** SLI and SLO from raw events: kiểm `Boundary` bằng case 2, cụ thể guarantee của sli numerator, denominator và slo window từ raw events chỉ đúng trong scope, time window, failure domain, permissions và version đã khóa.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.sre.sli-slo-raw-events`, đổi grain nhưng giữ tổng số dòng để lộ phép đo sai cấp. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `SLI and SLO from raw events` công bố.

**Bằng chứng cần giữ.** Đối với probe 2 của `SLI and SLO from raw events`, báo numerator, denominator và key set ở cả hai grain. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.3. SLI and SLO from raw events: kiểm `Failure mode` bằng case 3, cụ thể phân tích sli numerator, denominator và slo window từ raw events cần tìm earliest observable failure, propagation path, blast radius và state còn đáng tin

**Mệnh đề cần kiểm.** SLI and SLO from raw events: kiểm `Failure mode` bằng case 3, cụ thể phân tích sli numerator, denominator và slo window từ raw events cần tìm earliest observable failure, propagation path, blast radius và state còn đáng tin.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.sre.sli-slo-raw-events`, đưa một giá trị tới đúng boundary và một giá trị vượt boundary. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `SLI and SLO from raw events` công bố.

**Bằng chứng cần giữ.** Đối với probe 3 của `SLI and SLO from raw events`, lưu hai observed values cùng rule đã resolve. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.4. SLI and SLO from raw events: kiểm `Decision rule` bằng case 4, cụ thể quyết định về sli numerator, denominator và slo window từ raw events phải nối user impact và constraints với alternatives, trade-offs và reversal trigger

**Mệnh đề cần kiểm.** SLI and SLO from raw events: kiểm `Decision rule` bằng case 4, cụ thể quyết định về sli numerator, denominator và slo window từ raw events phải nối user impact và constraints với alternatives, trade-offs và reversal trigger.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.sre.sli-slo-raw-events`, kill tiến trình ngay trước rồi ngay sau durable side effect. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `SLI and SLO from raw events` công bố.

**Bằng chứng cần giữ.** Đối với probe 4 của `SLI and SLO from raw events`, lưu checkpoint, external ledger và trạng thái sau restart. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.5. SLI and SLO from raw events: kiểm `Evidence` bằng case 5, cụ thể bằng chứng cho sli numerator, denominator và slo window từ raw events gồm stable identity, resolved configuration, telemetry thô, state trước–sau và independent oracle

**Mệnh đề cần kiểm.** SLI and SLO from raw events: kiểm `Evidence` bằng case 5, cụ thể bằng chứng cho sli numerator, denominator và slo window từ raw events gồm stable identity, resolved configuration, telemetry thô, state trước–sau và independent oracle.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.sre.sli-slo-raw-events`, đảo thứ tự input và concurrency nhưng giữ logical population. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `SLI and SLO from raw events` công bố.

**Bằng chứng cần giữ.** Đối với probe 5 của `SLI and SLO from raw events`, so canonical hash và business totals giữa các thứ tự. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.6. SLI and SLO from raw events: kiểm `Recovery lab` bằng case 6, cụ thể lab sli numerator, denominator và slo window từ raw events phải inject failure hoặc changed assumption, phục hồi theo runbook rồi reconcile outcome với invariant

**Mệnh đề cần kiểm.** SLI and SLO from raw events: kiểm `Recovery lab` bằng case 6, cụ thể lab sli numerator, denominator và slo window từ raw events phải inject failure hoặc changed assumption, phục hồi theo runbook rồi reconcile outcome với invariant.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.sre.sli-slo-raw-events`, replay cùng identity với payload giống rồi payload xung đột. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `SLI and SLO from raw events` công bố.

**Bằng chứng cần giữ.** Đối với probe 6 của `SLI and SLO from raw events`, tách duplicate replay khỏi identity collision bằng reason code. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.7. SLI and SLO from raw events: kiểm `Mechanism` bằng case 7, cụ thể mô hình sli numerator, denominator và slo window từ raw events phải chỉ rõ actors, identities, state transitions và control loop thay vì dừng ở tên object hay tool

**Mệnh đề cần kiểm.** SLI and SLO from raw events: kiểm `Mechanism` bằng case 7, cụ thể mô hình sli numerator, denominator và slo window từ raw events phải chỉ rõ actors, identities, state transitions và control loop thay vì dừng ở tên object hay tool.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.sre.sli-slo-raw-events`, thêm record tới trễ trong horizon và ngoài horizon. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `SLI and SLO from raw events` công bố.

**Bằng chứng cần giữ.** Đối với probe 7 của `SLI and SLO from raw events`, báo accepted-late, rejected-late và oldest outstanding timestamp. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.8. SLI and SLO from raw events: kiểm `Boundary` bằng case 8, cụ thể guarantee của sli numerator, denominator và slo window từ raw events chỉ đúng trong scope, time window, failure domain, permissions và version đã khóa

**Mệnh đề cần kiểm.** SLI and SLO from raw events: kiểm `Boundary` bằng case 8, cụ thể guarantee của sli numerator, denominator và slo window từ raw events chỉ đúng trong scope, time window, failure domain, permissions và version đã khóa.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.sre.sli-slo-raw-events`, đổi schema theo một cách tương thích rồi một cách phá vỡ semantics. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `SLI and SLO from raw events` công bố.

**Bằng chứng cần giữ.** Đối với probe 8 của `SLI and SLO from raw events`, giữ schema diff, classification và consumer-visible result. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.9. SLI and SLO from raw events: kiểm `Failure mode` bằng case 9, cụ thể phân tích sli numerator, denominator và slo window từ raw events cần tìm earliest observable failure, propagation path, blast radius và state còn đáng tin

**Mệnh đề cần kiểm.** SLI and SLO from raw events: kiểm `Failure mode` bằng case 9, cụ thể phân tích sli numerator, denominator và slo window từ raw events cần tìm earliest observable failure, propagation path, blast radius và state còn đáng tin.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.sre.sli-slo-raw-events`, tạo missing và duplicate bù nhau để count tổng không đổi. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `SLI and SLO from raw events` công bố.

**Bằng chứng cần giữ.** Đối với probe 9 của `SLI and SLO from raw events`, so key multiset và typed hashes thay vì chỉ row count. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.10. SLI and SLO from raw events: kiểm `Decision rule` bằng case 10, cụ thể quyết định về sli numerator, denominator và slo window từ raw events phải nối user impact và constraints với alternatives, trade-offs và reversal trigger

**Mệnh đề cần kiểm.** SLI and SLO from raw events: kiểm `Decision rule` bằng case 10, cụ thể quyết định về sli numerator, denominator và slo window từ raw events phải nối user impact và constraints với alternatives, trade-offs và reversal trigger.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.sre.sli-slo-raw-events`, cho reviewer tái hiện chỉ từ evidence package. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `SLI and SLO from raw events` công bố.

**Bằng chứng cần giữ.** Đối với probe 10 của `SLI and SLO from raw events`, package phải đủ để người khác dựng lại decision và limitation. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.11. SLI and SLO from raw events: kiểm `Evidence` bằng case 11, cụ thể bằng chứng cho sli numerator, denominator và slo window từ raw events gồm stable identity, resolved configuration, telemetry thô, state trước–sau và independent oracle

**Mệnh đề cần kiểm.** SLI and SLO from raw events: kiểm `Evidence` bằng case 11, cụ thể bằng chứng cho sli numerator, denominator và slo window từ raw events gồm stable identity, resolved configuration, telemetry thô, state trước–sau và independent oracle.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.sre.sli-slo-raw-events`, so với oracle độc lập không dùng chung query hoặc parser. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `SLI and SLO from raw events` công bố.

**Bằng chứng cần giữ.** Đối với probe 11 của `SLI and SLO from raw events`, independent result phải khớp ở grain đã công bố. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.12. SLI and SLO from raw events: kiểm `Recovery lab` bằng case 12, cụ thể lab sli numerator, denominator và slo window từ raw events phải inject failure hoặc changed assumption, phục hồi theo runbook rồi reconcile outcome với invariant

**Mệnh đề cần kiểm.** SLI and SLO from raw events: kiểm `Recovery lab` bằng case 12, cụ thể lab sli numerator, denominator và slo window từ raw events phải inject failure hoặc changed assumption, phục hồi theo runbook rồi reconcile outcome với invariant.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.sre.sli-slo-raw-events`, chạy scope hẹp và population đầy đủ rồi công bố phần bị loại. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `SLI and SLO from raw events` công bố.

**Bằng chứng cần giữ.** Đối với probe 12 của `SLI and SLO from raw events`, coverage phải nêu rõ excluded nodes, partitions hoặc incidents. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.13. SLI and SLO from raw events: kiểm `Mechanism` bằng case 13, cụ thể mô hình sli numerator, denominator và slo window từ raw events phải chỉ rõ actors, identities, state transitions và control loop thay vì dừng ở tên object hay tool

**Mệnh đề cần kiểm.** SLI and SLO from raw events: kiểm `Mechanism` bằng case 13, cụ thể mô hình sli numerator, denominator và slo window từ raw events phải chỉ rõ actors, identities, state transitions và control loop thay vì dừng ở tên object hay tool.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.sre.sli-slo-raw-events`, thử timezone, precision hoặc partition ở hai phía của ranh giới. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `SLI and SLO from raw events` công bố.

**Bằng chứng cần giữ.** Đối với probe 13 của `SLI and SLO from raw events`, UTC/local interval và rounding policy phải hiện trong output. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.14. SLI and SLO from raw events: kiểm `Boundary` bằng case 14, cụ thể guarantee của sli numerator, denominator và slo window từ raw events chỉ đúng trong scope, time window, failure domain, permissions và version đã khóa

**Mệnh đề cần kiểm.** SLI and SLO from raw events: kiểm `Boundary` bằng case 14, cụ thể guarantee của sli numerator, denominator và slo window từ raw events chỉ đúng trong scope, time window, failure domain, permissions và version đã khóa.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.sre.sli-slo-raw-events`, đổi constraint đủ lớn để quyết định phải đảo. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `SLI and SLO from raw events` công bố.

**Bằng chứng cần giữ.** Đối với probe 14 của `SLI and SLO from raw events`, ADR phải lưu changed constraint và reversal threshold. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.15. SLI and SLO from raw events: kiểm `Failure mode` bằng case 15, cụ thể phân tích sli numerator, denominator và slo window từ raw events cần tìm earliest observable failure, propagation path, blast radius và state còn đáng tin

**Mệnh đề cần kiểm.** SLI and SLO from raw events: kiểm `Failure mode` bằng case 15, cụ thể phân tích sli numerator, denominator và slo window từ raw events cần tìm earliest observable failure, propagation path, blast radius và state còn đáng tin.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.sre.sli-slo-raw-events`, chạy lại từ môi trường sạch với versions và seed đã khóa. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `SLI and SLO from raw events` công bố.

**Bằng chứng cần giữ.** Đối với probe 15 của `SLI and SLO from raw events`, canonical result phải ổn định hoặc mọi nondeterminism phải được giải thích. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

## 8. Quy trình phản biện

1. Viết consumer-visible invariant cho `SLI and SLO from raw events` trước khi chọn query hoặc tool.
2. Khóa grain, identity, population, time window và authoritative source.
3. Phân biệt declared configuration, executed state và published state.
4. Chạy negative control, replay hoặc changed-assumption case phù hợp.
5. Đối soát bằng oracle độc lập; công bố coverage và phần không quan sát được.
6. Gắn owner, hành động, reversal trigger và hạn review cho kết luận.

## 9. Câu hỏi tự kiểm tra

1. `SLI and SLO from raw events: kiểm `Mechanism` bằng case 1, cụ thể mô hình sli numerator, denominator và slo window từ raw events phải chỉ rõ actors, identities, state transitions và control loop thay vì dừng ở tên object hay tool` thất bại đầu tiên ở boundary nào?
2. Artifact nào mạnh nhất để trả lời `SLI and SLO from raw events: kiểm `Failure mode` bằng case 3, cụ thể phân tích sli numerator, denominator và slo window từ raw events cần tìm earliest observable failure, propagation path, blast radius và state còn đáng tin`?
3. Counterexample nhỏ nhất cho `SLI and SLO from raw events: kiểm `Recovery lab` bằng case 6, cụ thể lab sli numerator, denominator và slo window từ raw events phải inject failure hoặc changed assumption, phục hồi theo runbook rồi reconcile outcome với invariant` gồm những state nào?
4. `SLI and SLO from raw events: kiểm `Failure mode` bằng case 9, cụ thể phân tích sli numerator, denominator và slo window từ raw events cần tìm earliest observable failure, propagation path, blast radius và state còn đáng tin` có thể xanh giả ra sao?
5. Constraint nào khiến quyết định ở `SLI and SLO from raw events: kiểm `Boundary` bằng case 14, cụ thể guarantee của sli numerator, denominator và slo window từ raw events chỉ đúng trong scope, time window, failure domain, permissions và version đã khóa` phải đảo?
6. Phần nào của `SLI and SLO from raw events: kiểm `Failure mode` bằng case 15, cụ thể phân tích sli numerator, denominator và slo window từ raw events cần tìm earliest observable failure, propagation path, blast radius và state còn đáng tin` mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `SLI and SLO from raw events` chưa chạy trên hệ thống production; nội dung là giáo trình và expected evidence.
- Hành vi phụ thuộc phiên bản, connector, scheduler, warehouse và catalog configuration phải được kiểm lại.
- Các ma trận, ladder và threshold do giáo trình tổng hợp không được gán nguyên văn cho vendor.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-GOOGLE-SRE-MONITORING]]
2. [[SRC-GOOGLE-SRE-ERROR-BUDGET-POLICY]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-GOOGLE-SRE-MONITORING]] | Contract hoặc cơ chế liên quan trực tiếp tới `SLI and SLO from raw events` | Đã đọc locator; cần pin version khi chạy lab |
| [[SRC-GOOGLE-SRE-ERROR-BUDGET-POLICY]] | Contract hoặc cơ chế liên quan trực tiếp tới `SLI and SLO from raw events` | Đã đọc locator; cần pin version khi chạy lab |

## Key takeaways
- Sli numerator, denominator và slo window từ raw events phải được bảo vệ bằng boundary, counterexample và evidence có thể phản bác.
- Với `wiki.sre.sli-slo-raw-events`, quality của kết luận phụ thuộc identity, coverage và oracle chứ không phụ thuộc màu dashboard.
- Câu hỏi `Làm thế nào mô hình, kiểm chứng và vận hành SLI numerator, denominator và SLO window từ raw events mà không khẳng định vượt quá evidence?` chỉ được trả lời trong scope và version đã ghi.
- Các source IDs `src.web.google-sre-monitoring, src.web.google-sre-error-budget-policy` đặt ranh giới cho source fact; phần còn lại là synthesis có nhãn.
- Trước khi lab chạy, đây là note đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.
