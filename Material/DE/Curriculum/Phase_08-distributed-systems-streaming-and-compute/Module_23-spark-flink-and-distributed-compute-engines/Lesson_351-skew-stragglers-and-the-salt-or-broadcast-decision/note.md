# Phase 8: Distributed Systems, Streaming and Compute
# Module 23: Spark, Flink and Distributed Compute Engines
# Lesson 351: Skew, stragglers and the salt-or-broadcast decision

## Mục tiêu bài học

**Năng lực cần chứng minh.** Chẩn đoán lệch tải từ phân bố thời gian tác vụ và sửa bằng một trong ba cách, có đối soát kết quả.

**Điều kiện hoàn thành.** Chẩn đoán đúng cả ba tình huống bằng số đo, và bản sửa lệch tải khớp kết quả gốc với thời gian giảm có số đo.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, kiểm chứng và vận hành partition skew, straggler diagnosis và quyết định salt-or-broadcast mà không khẳng định vượt quá evidence?

## 1. Mechanism

Mô hình partition skew, straggler diagnosis và quyết định salt-or-broadcast phải nêu actor, state, transition và resource thực sự tham gia thay vì chỉ gọi tên tính năng. Đừng bắt đầu bằng tên công cụ. Hãy bắt đầu bằng đối tượng được bảo vệ, boundary quan sát được và hậu quả nếu kết luận sai. Trong bài `Skew, stragglers and the salt-or-broadcast decision`, câu hỏi thực dụng là: Làm thế nào mô hình, kiểm chứng và vận hành partition skew, straggler diagnosis và quyết định salt-or-broadcast mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 2. Boundary

Guarantee của partition skew, straggler diagnosis và quyết định salt-or-broadcast chỉ có nghĩa khi khóa scope, identity, time window, failure domain và version. Điểm khó không nằm ở cú pháp mà ở identity và scope. Hai phép đo cùng tên vẫn có thể nói về hai population hoặc hai thời điểm khác nhau. Trong bài `Skew, stragglers and the salt-or-broadcast decision`, câu hỏi thực dụng là: Làm thế nào mô hình, kiểm chứng và vận hành partition skew, straggler diagnosis và quyết định salt-or-broadcast mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 3. Failure mode

Phân tích partition skew, straggler diagnosis và quyết định salt-or-broadcast cần chỉ ra earliest controllable failure, blast radius và trạng thái còn quan sát được sau lỗi. Một dashboard xanh chỉ là tín hiệu. Muốn biến nó thành bằng chứng phải giữ input, phiên bản, rule, trạng thái trước–sau và cách tính độc lập. Trong bài `Skew, stragglers and the salt-or-broadcast decision`, câu hỏi thực dụng là: Làm thế nào mô hình, kiểm chứng và vận hành partition skew, straggler diagnosis và quyết định salt-or-broadcast mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 4. Decision rule

Quyết định về partition skew, straggler diagnosis và quyết định salt-or-broadcast phải nối workload constraints với alternatives, trade-offs và điều kiện đảo chiều. Thiết kế tốt phải chịu được counterexample. Hãy chủ động tạo case sát boundary, case thiếu dữ liệu và case replay thay vì chỉ chạy happy path. Trong bài `Skew, stragglers and the salt-or-broadcast decision`, câu hỏi thực dụng là: Làm thế nào mô hình, kiểm chứng và vận hành partition skew, straggler diagnosis và quyết định salt-or-broadcast mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 5. Evidence

Bằng chứng cho partition skew, straggler diagnosis và quyết định salt-or-broadcast gồm resolved configuration, runtime identity, metrics/logs, state trước–sau và independent oracle. Chi phí vận hành thuộc contract. Một rule đúng nhưng quá đắt, quá ồn hoặc không có owner sẽ nhanh chóng bị tắt và mất tác dụng. Trong bài `Skew, stragglers and the salt-or-broadcast decision`, câu hỏi thực dụng là: Làm thế nào mô hình, kiểm chứng và vận hành partition skew, straggler diagnosis và quyết định salt-or-broadcast mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 6. Recovery lab

Lab partition skew, straggler diagnosis và quyết định salt-or-broadcast phải inject một failure hoặc changed constraint, phục hồi từ checkpoint hợp lệ rồi reconcile kết quả. Kết luận cần có điều kiện đảo chiều. Khi volume, latency, nguồn thẩm quyền hoặc topology đổi, quyết định cũ phải được xem xét lại bằng cùng một oracle. Trong bài `Skew, stragglers and the salt-or-broadcast decision`, câu hỏi thực dụng là: Làm thế nào mô hình, kiểm chứng và vận hành partition skew, straggler diagnosis và quyết định salt-or-broadcast mà không khẳng định vượt quá evidence? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 7. Ma trận kiểm chứng từng mệnh đề

Với `wiki.spark.skew-straggler-decision`, command thành công không tự chứng minh dữ liệu đúng. Protocol riêng của bài là: Run a version-pinned sandbox fixture, change one declared constraint or inject one failure, retain raw runtime evidence and reconcile the final identities and state against an independent oracle. Mỗi probe dưới đây phải nối input boundary với failure signal và oracle có thể phản bác kết luận.

### 7.1. Skew, stragglers and the salt-or-broadcast decision: kiểm `Mechanism` bằng case 1, cụ thể mô hình partition skew, straggler diagnosis và quyết định salt-or-broadcast phải nêu actor, state, transition và resource thực sự tham gia thay vì chỉ gọi tên tính năng

**Mệnh đề cần kiểm.** Skew, stragglers and the salt-or-broadcast decision: kiểm `Mechanism` bằng case 1, cụ thể mô hình partition skew, straggler diagnosis và quyết định salt-or-broadcast phải nêu actor, state, transition và resource thực sự tham gia thay vì chỉ gọi tên tính năng.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.skew-straggler-decision`, tạo positive control và negative control chỉ khác đúng một điều kiện. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Skew, stragglers and the salt-or-broadcast decision` công bố.

**Bằng chứng cần giữ.** Đối với probe 1 của `Skew, stragglers and the salt-or-broadcast decision`, giữ fixture, raw failing rows và lệnh tái hiện. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.2. Skew, stragglers and the salt-or-broadcast decision: kiểm `Boundary` bằng case 2, cụ thể guarantee của partition skew, straggler diagnosis và quyết định salt-or-broadcast chỉ có nghĩa khi khóa scope, identity, time window, failure domain và version

**Mệnh đề cần kiểm.** Skew, stragglers and the salt-or-broadcast decision: kiểm `Boundary` bằng case 2, cụ thể guarantee của partition skew, straggler diagnosis và quyết định salt-or-broadcast chỉ có nghĩa khi khóa scope, identity, time window, failure domain và version.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.skew-straggler-decision`, đổi grain nhưng giữ tổng số dòng để lộ phép đo sai cấp. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Skew, stragglers and the salt-or-broadcast decision` công bố.

**Bằng chứng cần giữ.** Đối với probe 2 của `Skew, stragglers and the salt-or-broadcast decision`, báo numerator, denominator và key set ở cả hai grain. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.3. Skew, stragglers and the salt-or-broadcast decision: kiểm `Failure mode` bằng case 3, cụ thể phân tích partition skew, straggler diagnosis và quyết định salt-or-broadcast cần chỉ ra earliest controllable failure, blast radius và trạng thái còn quan sát được sau lỗi

**Mệnh đề cần kiểm.** Skew, stragglers and the salt-or-broadcast decision: kiểm `Failure mode` bằng case 3, cụ thể phân tích partition skew, straggler diagnosis và quyết định salt-or-broadcast cần chỉ ra earliest controllable failure, blast radius và trạng thái còn quan sát được sau lỗi.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.skew-straggler-decision`, đưa một giá trị tới đúng boundary và một giá trị vượt boundary. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Skew, stragglers and the salt-or-broadcast decision` công bố.

**Bằng chứng cần giữ.** Đối với probe 3 của `Skew, stragglers and the salt-or-broadcast decision`, lưu hai observed values cùng rule đã resolve. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.4. Skew, stragglers and the salt-or-broadcast decision: kiểm `Decision rule` bằng case 4, cụ thể quyết định về partition skew, straggler diagnosis và quyết định salt-or-broadcast phải nối workload constraints với alternatives, trade-offs và điều kiện đảo chiều

**Mệnh đề cần kiểm.** Skew, stragglers and the salt-or-broadcast decision: kiểm `Decision rule` bằng case 4, cụ thể quyết định về partition skew, straggler diagnosis và quyết định salt-or-broadcast phải nối workload constraints với alternatives, trade-offs và điều kiện đảo chiều.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.skew-straggler-decision`, kill tiến trình ngay trước rồi ngay sau durable side effect. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Skew, stragglers and the salt-or-broadcast decision` công bố.

**Bằng chứng cần giữ.** Đối với probe 4 của `Skew, stragglers and the salt-or-broadcast decision`, lưu checkpoint, external ledger và trạng thái sau restart. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.5. Skew, stragglers and the salt-or-broadcast decision: kiểm `Evidence` bằng case 5, cụ thể bằng chứng cho partition skew, straggler diagnosis và quyết định salt-or-broadcast gồm resolved configuration, runtime identity, metrics/logs, state trước–sau và independent oracle

**Mệnh đề cần kiểm.** Skew, stragglers and the salt-or-broadcast decision: kiểm `Evidence` bằng case 5, cụ thể bằng chứng cho partition skew, straggler diagnosis và quyết định salt-or-broadcast gồm resolved configuration, runtime identity, metrics/logs, state trước–sau và independent oracle.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.skew-straggler-decision`, đảo thứ tự input và concurrency nhưng giữ logical population. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Skew, stragglers and the salt-or-broadcast decision` công bố.

**Bằng chứng cần giữ.** Đối với probe 5 của `Skew, stragglers and the salt-or-broadcast decision`, so canonical hash và business totals giữa các thứ tự. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.6. Skew, stragglers and the salt-or-broadcast decision: kiểm `Recovery lab` bằng case 6, cụ thể lab partition skew, straggler diagnosis và quyết định salt-or-broadcast phải inject một failure hoặc changed constraint, phục hồi từ checkpoint hợp lệ rồi reconcile kết quả

**Mệnh đề cần kiểm.** Skew, stragglers and the salt-or-broadcast decision: kiểm `Recovery lab` bằng case 6, cụ thể lab partition skew, straggler diagnosis và quyết định salt-or-broadcast phải inject một failure hoặc changed constraint, phục hồi từ checkpoint hợp lệ rồi reconcile kết quả.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.skew-straggler-decision`, replay cùng identity với payload giống rồi payload xung đột. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Skew, stragglers and the salt-or-broadcast decision` công bố.

**Bằng chứng cần giữ.** Đối với probe 6 của `Skew, stragglers and the salt-or-broadcast decision`, tách duplicate replay khỏi identity collision bằng reason code. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.7. Skew, stragglers and the salt-or-broadcast decision: kiểm `Mechanism` bằng case 7, cụ thể mô hình partition skew, straggler diagnosis và quyết định salt-or-broadcast phải nêu actor, state, transition và resource thực sự tham gia thay vì chỉ gọi tên tính năng

**Mệnh đề cần kiểm.** Skew, stragglers and the salt-or-broadcast decision: kiểm `Mechanism` bằng case 7, cụ thể mô hình partition skew, straggler diagnosis và quyết định salt-or-broadcast phải nêu actor, state, transition và resource thực sự tham gia thay vì chỉ gọi tên tính năng.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.skew-straggler-decision`, thêm record tới trễ trong horizon và ngoài horizon. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Skew, stragglers and the salt-or-broadcast decision` công bố.

**Bằng chứng cần giữ.** Đối với probe 7 của `Skew, stragglers and the salt-or-broadcast decision`, báo accepted-late, rejected-late và oldest outstanding timestamp. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.8. Skew, stragglers and the salt-or-broadcast decision: kiểm `Boundary` bằng case 8, cụ thể guarantee của partition skew, straggler diagnosis và quyết định salt-or-broadcast chỉ có nghĩa khi khóa scope, identity, time window, failure domain và version

**Mệnh đề cần kiểm.** Skew, stragglers and the salt-or-broadcast decision: kiểm `Boundary` bằng case 8, cụ thể guarantee của partition skew, straggler diagnosis và quyết định salt-or-broadcast chỉ có nghĩa khi khóa scope, identity, time window, failure domain và version.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.skew-straggler-decision`, đổi schema theo một cách tương thích rồi một cách phá vỡ semantics. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Skew, stragglers and the salt-or-broadcast decision` công bố.

**Bằng chứng cần giữ.** Đối với probe 8 của `Skew, stragglers and the salt-or-broadcast decision`, giữ schema diff, classification và consumer-visible result. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.9. Skew, stragglers and the salt-or-broadcast decision: kiểm `Failure mode` bằng case 9, cụ thể phân tích partition skew, straggler diagnosis và quyết định salt-or-broadcast cần chỉ ra earliest controllable failure, blast radius và trạng thái còn quan sát được sau lỗi

**Mệnh đề cần kiểm.** Skew, stragglers and the salt-or-broadcast decision: kiểm `Failure mode` bằng case 9, cụ thể phân tích partition skew, straggler diagnosis và quyết định salt-or-broadcast cần chỉ ra earliest controllable failure, blast radius và trạng thái còn quan sát được sau lỗi.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.skew-straggler-decision`, tạo missing và duplicate bù nhau để count tổng không đổi. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Skew, stragglers and the salt-or-broadcast decision` công bố.

**Bằng chứng cần giữ.** Đối với probe 9 của `Skew, stragglers and the salt-or-broadcast decision`, so key multiset và typed hashes thay vì chỉ row count. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.10. Skew, stragglers and the salt-or-broadcast decision: kiểm `Decision rule` bằng case 10, cụ thể quyết định về partition skew, straggler diagnosis và quyết định salt-or-broadcast phải nối workload constraints với alternatives, trade-offs và điều kiện đảo chiều

**Mệnh đề cần kiểm.** Skew, stragglers and the salt-or-broadcast decision: kiểm `Decision rule` bằng case 10, cụ thể quyết định về partition skew, straggler diagnosis và quyết định salt-or-broadcast phải nối workload constraints với alternatives, trade-offs và điều kiện đảo chiều.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.skew-straggler-decision`, cho reviewer tái hiện chỉ từ evidence package. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Skew, stragglers and the salt-or-broadcast decision` công bố.

**Bằng chứng cần giữ.** Đối với probe 10 của `Skew, stragglers and the salt-or-broadcast decision`, package phải đủ để người khác dựng lại decision và limitation. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.11. Skew, stragglers and the salt-or-broadcast decision: kiểm `Evidence` bằng case 11, cụ thể bằng chứng cho partition skew, straggler diagnosis và quyết định salt-or-broadcast gồm resolved configuration, runtime identity, metrics/logs, state trước–sau và independent oracle

**Mệnh đề cần kiểm.** Skew, stragglers and the salt-or-broadcast decision: kiểm `Evidence` bằng case 11, cụ thể bằng chứng cho partition skew, straggler diagnosis và quyết định salt-or-broadcast gồm resolved configuration, runtime identity, metrics/logs, state trước–sau và independent oracle.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.skew-straggler-decision`, so với oracle độc lập không dùng chung query hoặc parser. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Skew, stragglers and the salt-or-broadcast decision` công bố.

**Bằng chứng cần giữ.** Đối với probe 11 của `Skew, stragglers and the salt-or-broadcast decision`, independent result phải khớp ở grain đã công bố. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.12. Skew, stragglers and the salt-or-broadcast decision: kiểm `Recovery lab` bằng case 12, cụ thể lab partition skew, straggler diagnosis và quyết định salt-or-broadcast phải inject một failure hoặc changed constraint, phục hồi từ checkpoint hợp lệ rồi reconcile kết quả

**Mệnh đề cần kiểm.** Skew, stragglers and the salt-or-broadcast decision: kiểm `Recovery lab` bằng case 12, cụ thể lab partition skew, straggler diagnosis và quyết định salt-or-broadcast phải inject một failure hoặc changed constraint, phục hồi từ checkpoint hợp lệ rồi reconcile kết quả.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.skew-straggler-decision`, chạy scope hẹp và population đầy đủ rồi công bố phần bị loại. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Skew, stragglers and the salt-or-broadcast decision` công bố.

**Bằng chứng cần giữ.** Đối với probe 12 của `Skew, stragglers and the salt-or-broadcast decision`, coverage phải nêu rõ excluded nodes, partitions hoặc incidents. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.13. Skew, stragglers and the salt-or-broadcast decision: kiểm `Mechanism` bằng case 13, cụ thể mô hình partition skew, straggler diagnosis và quyết định salt-or-broadcast phải nêu actor, state, transition và resource thực sự tham gia thay vì chỉ gọi tên tính năng

**Mệnh đề cần kiểm.** Skew, stragglers and the salt-or-broadcast decision: kiểm `Mechanism` bằng case 13, cụ thể mô hình partition skew, straggler diagnosis và quyết định salt-or-broadcast phải nêu actor, state, transition và resource thực sự tham gia thay vì chỉ gọi tên tính năng.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.skew-straggler-decision`, thử timezone, precision hoặc partition ở hai phía của ranh giới. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Skew, stragglers and the salt-or-broadcast decision` công bố.

**Bằng chứng cần giữ.** Đối với probe 13 của `Skew, stragglers and the salt-or-broadcast decision`, UTC/local interval và rounding policy phải hiện trong output. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.14. Skew, stragglers and the salt-or-broadcast decision: kiểm `Boundary` bằng case 14, cụ thể guarantee của partition skew, straggler diagnosis và quyết định salt-or-broadcast chỉ có nghĩa khi khóa scope, identity, time window, failure domain và version

**Mệnh đề cần kiểm.** Skew, stragglers and the salt-or-broadcast decision: kiểm `Boundary` bằng case 14, cụ thể guarantee của partition skew, straggler diagnosis và quyết định salt-or-broadcast chỉ có nghĩa khi khóa scope, identity, time window, failure domain và version.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.skew-straggler-decision`, đổi constraint đủ lớn để quyết định phải đảo. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Skew, stragglers and the salt-or-broadcast decision` công bố.

**Bằng chứng cần giữ.** Đối với probe 14 của `Skew, stragglers and the salt-or-broadcast decision`, ADR phải lưu changed constraint và reversal threshold. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.15. Skew, stragglers and the salt-or-broadcast decision: kiểm `Failure mode` bằng case 15, cụ thể phân tích partition skew, straggler diagnosis và quyết định salt-or-broadcast cần chỉ ra earliest controllable failure, blast radius và trạng thái còn quan sát được sau lỗi

**Mệnh đề cần kiểm.** Skew, stragglers and the salt-or-broadcast decision: kiểm `Failure mode` bằng case 15, cụ thể phân tích partition skew, straggler diagnosis và quyết định salt-or-broadcast cần chỉ ra earliest controllable failure, blast radius và trạng thái còn quan sát được sau lỗi.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.skew-straggler-decision`, chạy lại từ môi trường sạch với versions và seed đã khóa. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Skew, stragglers and the salt-or-broadcast decision` công bố.

**Bằng chứng cần giữ.** Đối với probe 15 của `Skew, stragglers and the salt-or-broadcast decision`, canonical result phải ổn định hoặc mọi nondeterminism phải được giải thích. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

## 8. Quy trình phản biện

1. Viết consumer-visible invariant cho `Skew, stragglers and the salt-or-broadcast decision` trước khi chọn query hoặc tool.
2. Khóa grain, identity, population, time window và authoritative source.
3. Phân biệt declared configuration, executed state và published state.
4. Chạy negative control, replay hoặc changed-assumption case phù hợp.
5. Đối soát bằng oracle độc lập; công bố coverage và phần không quan sát được.
6. Gắn owner, hành động, reversal trigger và hạn review cho kết luận.

## 9. Câu hỏi tự kiểm tra

1. `Skew, stragglers and the salt-or-broadcast decision: kiểm `Mechanism` bằng case 1, cụ thể mô hình partition skew, straggler diagnosis và quyết định salt-or-broadcast phải nêu actor, state, transition và resource thực sự tham gia thay vì chỉ gọi tên tính năng` thất bại đầu tiên ở boundary nào?
2. Artifact nào mạnh nhất để trả lời `Skew, stragglers and the salt-or-broadcast decision: kiểm `Failure mode` bằng case 3, cụ thể phân tích partition skew, straggler diagnosis và quyết định salt-or-broadcast cần chỉ ra earliest controllable failure, blast radius và trạng thái còn quan sát được sau lỗi`?
3. Counterexample nhỏ nhất cho `Skew, stragglers and the salt-or-broadcast decision: kiểm `Recovery lab` bằng case 6, cụ thể lab partition skew, straggler diagnosis và quyết định salt-or-broadcast phải inject một failure hoặc changed constraint, phục hồi từ checkpoint hợp lệ rồi reconcile kết quả` gồm những state nào?
4. `Skew, stragglers and the salt-or-broadcast decision: kiểm `Failure mode` bằng case 9, cụ thể phân tích partition skew, straggler diagnosis và quyết định salt-or-broadcast cần chỉ ra earliest controllable failure, blast radius và trạng thái còn quan sát được sau lỗi` có thể xanh giả ra sao?
5. Constraint nào khiến quyết định ở `Skew, stragglers and the salt-or-broadcast decision: kiểm `Boundary` bằng case 14, cụ thể guarantee của partition skew, straggler diagnosis và quyết định salt-or-broadcast chỉ có nghĩa khi khóa scope, identity, time window, failure domain và version` phải đảo?
6. Phần nào của `Skew, stragglers and the salt-or-broadcast decision: kiểm `Failure mode` bằng case 15, cụ thể phân tích partition skew, straggler diagnosis và quyết định salt-or-broadcast cần chỉ ra earliest controllable failure, blast radius và trạng thái còn quan sát được sau lỗi` mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `Skew, stragglers and the salt-or-broadcast decision` chưa chạy trên hệ thống production; nội dung là giáo trình và expected evidence.
- Hành vi phụ thuộc phiên bản, connector, scheduler, warehouse và catalog configuration phải được kiểm lại.
- Các ma trận, ladder và threshold do giáo trình tổng hợp không được gán nguyên văn cho vendor.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-APACHE-SPARK-SQL-PERFORMANCE]]
2. [[SRC-APACHE-SPARK-TUNING]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-APACHE-SPARK-SQL-PERFORMANCE]] | Contract hoặc cơ chế liên quan trực tiếp tới `Skew, stragglers and the salt-or-broadcast decision` | Đã đọc locator; cần pin version khi chạy lab |
| [[SRC-APACHE-SPARK-TUNING]] | Contract hoặc cơ chế liên quan trực tiếp tới `Skew, stragglers and the salt-or-broadcast decision` | Đã đọc locator; cần pin version khi chạy lab |

## Key takeaways
- Partition skew, straggler diagnosis và quyết định salt-or-broadcast phải được bảo vệ bằng boundary, failure probe và evidence có thể phản bác.
- Với `wiki.spark.skew-straggler-decision`, quality của kết luận phụ thuộc identity, coverage và oracle chứ không phụ thuộc màu dashboard.
- Câu hỏi `Làm thế nào mô hình, kiểm chứng và vận hành partition skew, straggler diagnosis và quyết định salt-or-broadcast mà không khẳng định vượt quá evidence?` chỉ được trả lời trong scope và version đã ghi.
- Các source IDs `src.web.apache-spark-sql-performance, src.web.apache-spark-tuning` đặt ranh giới cho source fact; phần còn lại là synthesis có nhãn.
- Trước khi lab chạy, đây là note đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.
