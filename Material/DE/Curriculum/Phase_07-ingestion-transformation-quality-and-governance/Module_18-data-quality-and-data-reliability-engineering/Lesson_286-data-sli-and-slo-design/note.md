# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 18: Data Quality and Data Reliability Engineering
# Lesson 286: Data SLI and SLO design

## Mục tiêu bài học

**Năng lực cần chứng minh.** Định nghĩa ba cam kết theo hành trình người dùng với tử số, mẫu số, cửa sổ và loại trừ tường minh.

**Điều kiện hoàn thành.** Ba cam kết cho cùng con số khi hai người tính độc lập, mỗi cam kết dẫn về một hành trình người dùng, và tình huống công việc xanh mà cam kết vỡ được tái hiện.

> [!abstract] Câu hỏi trung tâm
> Thiết kế data SLI/SLO thế nào để phản ánh trải nghiệm consumer thay vì sức khỏe job nội bộ?

## 1. Consumer journey

Bắt đầu từ decision/report/model mà dữ liệu phục vụ, critical assets và thời điểm consumer thực sự cần. Đừng bắt đầu bằng tên công cụ. Hãy bắt đầu bằng đối tượng được bảo vệ, boundary quan sát được và hậu quả nếu kết luận sai. Trong bài `Data SLI and SLO design`, câu hỏi thực dụng là: Thiết kế data SLI/SLO thế nào để phản ánh trải nghiệm consumer thay vì sức khỏe job nội bộ? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 2. SLI ratio

Định nghĩa good events trên eligible events hoặc good intervals trên valid intervals; numerator/denominator phải query lại được. Điểm khó không nằm ở cú pháp mà ở identity và scope. Hai phép đo cùng tên vẫn có thể nói về hai population hoặc hai thời điểm khác nhau. Trong bài `Data SLI and SLO design`, câu hỏi thực dụng là: Thiết kế data SLI/SLO thế nào để phản ánh trải nghiệm consumer thay vì sức khỏe job nội bộ? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 3. Data signals

Freshness, completeness, correctness proxy, schema usability và availability có thể là SLIs riêng, không trộn thành điểm bí ẩn. Một dashboard xanh chỉ là tín hiệu. Muốn biến nó thành bằng chứng phải giữ input, phiên bản, rule, trạng thái trước–sau và cách tính độc lập. Trong bài `Data SLI and SLO design`, câu hỏi thực dụng là: Thiết kế data SLI/SLO thế nào để phản ánh trải nghiệm consumer thay vì sức khỏe job nội bộ? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 4. SLO window

Target, rolling/calendar window, exclusions và low-traffic handling phải ghi cùng policy. Thiết kế tốt phải chịu được counterexample. Hãy chủ động tạo case sát boundary, case thiếu dữ liệu và case replay thay vì chỉ chạy happy path. Trong bài `Data SLI and SLO design`, câu hỏi thực dụng là: Thiết kế data SLI/SLO thế nào để phản ánh trải nghiệm consumer thay vì sức khỏe job nội bộ? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 5. Measurement architecture

Probe ở publication/consumer boundary, lưu late corrections và đo cả monitoring gaps. Chi phí vận hành thuộc contract. Một rule đúng nhưng quá đắt, quá ồn hoặc không có owner sẽ nhanh chóng bị tắt và mất tác dụng. Trong bài `Data SLI and SLO design`, câu hỏi thực dụng là: Thiết kế data SLI/SLO thế nào để phản ánh trải nghiệm consumer thay vì sức khỏe job nội bộ? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 6. Review and ownership

SLO có owner, stakeholder agreement, review cadence và trigger đổi khi use case hoặc source authority thay. Kết luận cần có điều kiện đảo chiều. Khi volume, latency, nguồn thẩm quyền hoặc topology đổi, quyết định cũ phải được xem xét lại bằng cùng một oracle. Trong bài `Data SLI and SLO design`, câu hỏi thực dụng là: Thiết kế data SLI/SLO thế nào để phản ánh trải nghiệm consumer thay vì sức khỏe job nội bộ? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 7. Ma trận kiểm chứng từng mệnh đề

Với `wiki.data-quality.sli-slo-design`, command thành công không tự chứng minh dữ liệu đúng. Protocol riêng của bài là: Replay một cửa sổ có good/bad events hoặc incident state, tính lại metric độc lập và kiểm action/routing đúng policy. Mỗi probe dưới đây phải nối input boundary với failure signal và oracle có thể phản bác kết luận.

### 7.1. Data SLI and SLO design: kiểm `Consumer journey` bằng case 1, cụ thể bắt đầu từ decision/report/model mà dữ liệu phục vụ, critical assets và thời điểm consumer thực sự cần

**Mệnh đề cần kiểm.** Data SLI and SLO design: kiểm `Consumer journey` bằng case 1, cụ thể bắt đầu từ decision/report/model mà dữ liệu phục vụ, critical assets và thời điểm consumer thực sự cần.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.data-quality.sli-slo-design`, tạo positive control và negative control chỉ khác đúng một điều kiện. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Data SLI and SLO design` công bố.

**Bằng chứng cần giữ.** Đối với probe 1 của `Data SLI and SLO design`, giữ fixture, raw failing rows và lệnh tái hiện. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.2. Data SLI and SLO design: kiểm `SLI ratio` bằng case 2, cụ thể định nghĩa good events trên eligible events hoặc good intervals trên valid intervals; numerator/denominator phải query lại được

**Mệnh đề cần kiểm.** Data SLI and SLO design: kiểm `SLI ratio` bằng case 2, cụ thể định nghĩa good events trên eligible events hoặc good intervals trên valid intervals; numerator/denominator phải query lại được.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.data-quality.sli-slo-design`, đổi grain nhưng giữ tổng số dòng để lộ phép đo sai cấp. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Data SLI and SLO design` công bố.

**Bằng chứng cần giữ.** Đối với probe 2 của `Data SLI and SLO design`, báo numerator, denominator và key set ở cả hai grain. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.3. Data SLI and SLO design: kiểm `Data signals` bằng case 3, cụ thể freshness, completeness, correctness proxy, schema usability và availability có thể là slis riêng, không trộn thành điểm bí ẩn

**Mệnh đề cần kiểm.** Data SLI and SLO design: kiểm `Data signals` bằng case 3, cụ thể freshness, completeness, correctness proxy, schema usability và availability có thể là slis riêng, không trộn thành điểm bí ẩn.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.data-quality.sli-slo-design`, đưa một giá trị tới đúng boundary và một giá trị vượt boundary. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Data SLI and SLO design` công bố.

**Bằng chứng cần giữ.** Đối với probe 3 của `Data SLI and SLO design`, lưu hai observed values cùng rule đã resolve. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.4. Data SLI and SLO design: kiểm `SLO window` bằng case 4, cụ thể target, rolling/calendar window, exclusions và low-traffic handling phải ghi cùng policy

**Mệnh đề cần kiểm.** Data SLI and SLO design: kiểm `SLO window` bằng case 4, cụ thể target, rolling/calendar window, exclusions và low-traffic handling phải ghi cùng policy.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.data-quality.sli-slo-design`, kill tiến trình ngay trước rồi ngay sau durable side effect. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Data SLI and SLO design` công bố.

**Bằng chứng cần giữ.** Đối với probe 4 của `Data SLI and SLO design`, lưu checkpoint, external ledger và trạng thái sau restart. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.5. Data SLI and SLO design: kiểm `Measurement architecture` bằng case 5, cụ thể probe ở publication/consumer boundary, lưu late corrections và đo cả monitoring gaps

**Mệnh đề cần kiểm.** Data SLI and SLO design: kiểm `Measurement architecture` bằng case 5, cụ thể probe ở publication/consumer boundary, lưu late corrections và đo cả monitoring gaps.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.data-quality.sli-slo-design`, đảo thứ tự input và concurrency nhưng giữ logical population. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Data SLI and SLO design` công bố.

**Bằng chứng cần giữ.** Đối với probe 5 của `Data SLI and SLO design`, so canonical hash và business totals giữa các thứ tự. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.6. Data SLI and SLO design: kiểm `Review and ownership` bằng case 6, cụ thể slo có owner, stakeholder agreement, review cadence và trigger đổi khi use case hoặc source authority thay

**Mệnh đề cần kiểm.** Data SLI and SLO design: kiểm `Review and ownership` bằng case 6, cụ thể slo có owner, stakeholder agreement, review cadence và trigger đổi khi use case hoặc source authority thay.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.data-quality.sli-slo-design`, replay cùng identity với payload giống rồi payload xung đột. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Data SLI and SLO design` công bố.

**Bằng chứng cần giữ.** Đối với probe 6 của `Data SLI and SLO design`, tách duplicate replay khỏi identity collision bằng reason code. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.7. Data SLI and SLO design: kiểm `Consumer journey` bằng case 7, cụ thể bắt đầu từ decision/report/model mà dữ liệu phục vụ, critical assets và thời điểm consumer thực sự cần

**Mệnh đề cần kiểm.** Data SLI and SLO design: kiểm `Consumer journey` bằng case 7, cụ thể bắt đầu từ decision/report/model mà dữ liệu phục vụ, critical assets và thời điểm consumer thực sự cần.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.data-quality.sli-slo-design`, thêm record tới trễ trong horizon và ngoài horizon. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Data SLI and SLO design` công bố.

**Bằng chứng cần giữ.** Đối với probe 7 của `Data SLI and SLO design`, báo accepted-late, rejected-late và oldest outstanding timestamp. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.8. Data SLI and SLO design: kiểm `SLI ratio` bằng case 8, cụ thể định nghĩa good events trên eligible events hoặc good intervals trên valid intervals; numerator/denominator phải query lại được

**Mệnh đề cần kiểm.** Data SLI and SLO design: kiểm `SLI ratio` bằng case 8, cụ thể định nghĩa good events trên eligible events hoặc good intervals trên valid intervals; numerator/denominator phải query lại được.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.data-quality.sli-slo-design`, đổi schema theo một cách tương thích rồi một cách phá vỡ semantics. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Data SLI and SLO design` công bố.

**Bằng chứng cần giữ.** Đối với probe 8 của `Data SLI and SLO design`, giữ schema diff, classification và consumer-visible result. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.9. Data SLI and SLO design: kiểm `Data signals` bằng case 9, cụ thể freshness, completeness, correctness proxy, schema usability và availability có thể là slis riêng, không trộn thành điểm bí ẩn

**Mệnh đề cần kiểm.** Data SLI and SLO design: kiểm `Data signals` bằng case 9, cụ thể freshness, completeness, correctness proxy, schema usability và availability có thể là slis riêng, không trộn thành điểm bí ẩn.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.data-quality.sli-slo-design`, tạo missing và duplicate bù nhau để count tổng không đổi. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Data SLI and SLO design` công bố.

**Bằng chứng cần giữ.** Đối với probe 9 của `Data SLI and SLO design`, so key multiset và typed hashes thay vì chỉ row count. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.10. Data SLI and SLO design: kiểm `SLO window` bằng case 10, cụ thể target, rolling/calendar window, exclusions và low-traffic handling phải ghi cùng policy

**Mệnh đề cần kiểm.** Data SLI and SLO design: kiểm `SLO window` bằng case 10, cụ thể target, rolling/calendar window, exclusions và low-traffic handling phải ghi cùng policy.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.data-quality.sli-slo-design`, cho reviewer tái hiện chỉ từ evidence package. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Data SLI and SLO design` công bố.

**Bằng chứng cần giữ.** Đối với probe 10 của `Data SLI and SLO design`, package phải đủ để người khác dựng lại decision và limitation. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.11. Data SLI and SLO design: kiểm `Measurement architecture` bằng case 11, cụ thể probe ở publication/consumer boundary, lưu late corrections và đo cả monitoring gaps

**Mệnh đề cần kiểm.** Data SLI and SLO design: kiểm `Measurement architecture` bằng case 11, cụ thể probe ở publication/consumer boundary, lưu late corrections và đo cả monitoring gaps.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.data-quality.sli-slo-design`, so với oracle độc lập không dùng chung query hoặc parser. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Data SLI and SLO design` công bố.

**Bằng chứng cần giữ.** Đối với probe 11 của `Data SLI and SLO design`, independent result phải khớp ở grain đã công bố. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.12. Data SLI and SLO design: kiểm `Review and ownership` bằng case 12, cụ thể slo có owner, stakeholder agreement, review cadence và trigger đổi khi use case hoặc source authority thay

**Mệnh đề cần kiểm.** Data SLI and SLO design: kiểm `Review and ownership` bằng case 12, cụ thể slo có owner, stakeholder agreement, review cadence và trigger đổi khi use case hoặc source authority thay.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.data-quality.sli-slo-design`, chạy scope hẹp và population đầy đủ rồi công bố phần bị loại. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Data SLI and SLO design` công bố.

**Bằng chứng cần giữ.** Đối với probe 12 của `Data SLI and SLO design`, coverage phải nêu rõ excluded nodes, partitions hoặc incidents. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.13. Data SLI and SLO design: kiểm `Consumer journey` bằng case 13, cụ thể bắt đầu từ decision/report/model mà dữ liệu phục vụ, critical assets và thời điểm consumer thực sự cần

**Mệnh đề cần kiểm.** Data SLI and SLO design: kiểm `Consumer journey` bằng case 13, cụ thể bắt đầu từ decision/report/model mà dữ liệu phục vụ, critical assets và thời điểm consumer thực sự cần.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.data-quality.sli-slo-design`, thử timezone, precision hoặc partition ở hai phía của ranh giới. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Data SLI and SLO design` công bố.

**Bằng chứng cần giữ.** Đối với probe 13 của `Data SLI and SLO design`, UTC/local interval và rounding policy phải hiện trong output. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.14. Data SLI and SLO design: kiểm `SLI ratio` bằng case 14, cụ thể định nghĩa good events trên eligible events hoặc good intervals trên valid intervals; numerator/denominator phải query lại được

**Mệnh đề cần kiểm.** Data SLI and SLO design: kiểm `SLI ratio` bằng case 14, cụ thể định nghĩa good events trên eligible events hoặc good intervals trên valid intervals; numerator/denominator phải query lại được.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.data-quality.sli-slo-design`, đổi constraint đủ lớn để quyết định phải đảo. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Data SLI and SLO design` công bố.

**Bằng chứng cần giữ.** Đối với probe 14 của `Data SLI and SLO design`, ADR phải lưu changed constraint và reversal threshold. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.15. Data SLI and SLO design: kiểm `Data signals` bằng case 15, cụ thể freshness, completeness, correctness proxy, schema usability và availability có thể là slis riêng, không trộn thành điểm bí ẩn

**Mệnh đề cần kiểm.** Data SLI and SLO design: kiểm `Data signals` bằng case 15, cụ thể freshness, completeness, correctness proxy, schema usability và availability có thể là slis riêng, không trộn thành điểm bí ẩn.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.data-quality.sli-slo-design`, chạy lại từ môi trường sạch với versions và seed đã khóa. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Data SLI and SLO design` công bố.

**Bằng chứng cần giữ.** Đối với probe 15 của `Data SLI and SLO design`, canonical result phải ổn định hoặc mọi nondeterminism phải được giải thích. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

## 8. Quy trình phản biện

1. Viết consumer-visible invariant cho `Data SLI and SLO design` trước khi chọn query hoặc tool.
2. Khóa grain, identity, population, time window và authoritative source.
3. Phân biệt declared configuration, executed state và published state.
4. Chạy negative control, replay hoặc changed-assumption case phù hợp.
5. Đối soát bằng oracle độc lập; công bố coverage và phần không quan sát được.
6. Gắn owner, hành động, reversal trigger và hạn review cho kết luận.

## 9. Câu hỏi tự kiểm tra

1. `Data SLI and SLO design: kiểm `Consumer journey` bằng case 1, cụ thể bắt đầu từ decision/report/model mà dữ liệu phục vụ, critical assets và thời điểm consumer thực sự cần` thất bại đầu tiên ở boundary nào?
2. Artifact nào mạnh nhất để trả lời `Data SLI and SLO design: kiểm `Data signals` bằng case 3, cụ thể freshness, completeness, correctness proxy, schema usability và availability có thể là slis riêng, không trộn thành điểm bí ẩn`?
3. Counterexample nhỏ nhất cho `Data SLI and SLO design: kiểm `Review and ownership` bằng case 6, cụ thể slo có owner, stakeholder agreement, review cadence và trigger đổi khi use case hoặc source authority thay` gồm những state nào?
4. `Data SLI and SLO design: kiểm `Data signals` bằng case 9, cụ thể freshness, completeness, correctness proxy, schema usability và availability có thể là slis riêng, không trộn thành điểm bí ẩn` có thể xanh giả ra sao?
5. Constraint nào khiến quyết định ở `Data SLI and SLO design: kiểm `SLI ratio` bằng case 14, cụ thể định nghĩa good events trên eligible events hoặc good intervals trên valid intervals; numerator/denominator phải query lại được` phải đảo?
6. Phần nào của `Data SLI and SLO design: kiểm `Data signals` bằng case 15, cụ thể freshness, completeness, correctness proxy, schema usability và availability có thể là slis riêng, không trộn thành điểm bí ẩn` mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `Data SLI and SLO design` chưa chạy trên hệ thống production; nội dung là giáo trình và expected evidence.
- Hành vi phụ thuộc phiên bản, connector, scheduler, warehouse và catalog configuration phải được kiểm lại.
- Các ma trận, ladder và threshold do giáo trình tổng hợp không được gán nguyên văn cho vendor.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-GOOGLE-SRE-MONITORING]]
2. [[SRC-GX-DATA-QUALITY-USE-CASES]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-GOOGLE-SRE-MONITORING]] | Contract hoặc cơ chế liên quan trực tiếp tới `Data SLI and SLO design` | Đã đọc locator; cần pin version khi chạy lab |
| [[SRC-GX-DATA-QUALITY-USE-CASES]] | Contract hoặc cơ chế liên quan trực tiếp tới `Data SLI and SLO design` | Đã đọc locator; cần pin version khi chạy lab |

## Key takeaways
- Data SLI đo trải nghiệm consumer trên population có thể kiểm lại.
- Với `wiki.data-quality.sli-slo-design`, quality của kết luận phụ thuộc identity, coverage và oracle chứ không phụ thuộc màu dashboard.
- Câu hỏi `Thiết kế data SLI/SLO thế nào để phản ánh trải nghiệm consumer thay vì sức khỏe job nội bộ?` chỉ được trả lời trong scope và version đã ghi.
- Các source IDs `src.web.google-sre-monitoring, src.web.gx-data-quality-use-cases` đặt ranh giới cho source fact; phần còn lại là synthesis có nhãn.
- Trước khi lab chạy, đây là note đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.
