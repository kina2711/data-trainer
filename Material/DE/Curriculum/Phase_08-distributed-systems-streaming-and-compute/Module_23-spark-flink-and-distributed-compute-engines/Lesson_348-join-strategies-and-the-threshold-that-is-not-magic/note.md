# Phase 8: Distributed Systems, Streaming and Compute
# Module 23: Spark, Flink and Distributed Compute Engines
# Lesson 348: Join strategies and the threshold that is not magic

## Mục tiêu bài học

**Năng lực cần chứng minh.** Ép cả ba chiến lược trên cùng phép kết, đo chi phí từng cái, và tái hiện ca phát tán gây tràn bộ nhớ.

**Điều kiện hoàn thành.** Ba chiến lược có số đo thời gian và lượng xáo trộn, và ca tràn bộ nhớ do ước lượng sai được tái hiện cùng giải thích.

> [!abstract] Câu hỏi trung tâm
> Spark chọn broadcast, sort-merge, shuffle-hash hoặc storage-partition join dựa trên evidence nào, và vì sao threshold không phải phép màu?

## 1. Strategy space

Join type, equi keys, side sizes, partitioning, ordering và engine support giới hạn tập strategies hợp lệ. Đừng bắt đầu bằng tên công cụ. Hãy bắt đầu bằng đối tượng được bảo vệ, boundary quan sát được và hậu quả nếu kết luận sai. Trong bài `Join strategies and the threshold that is not magic`, câu hỏi thực dụng là: Spark chọn broadcast, sort-merge, shuffle-hash hoặc storage-partition join dựa trên evidence nào, và vì sao threshold không phải phép màu? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 2. Broadcast

Broadcast hash join tránh shuffle phía lớn nhưng cần estimate nhỏ đáng tin và memory/network headroom trên executors. Điểm khó không nằm ở cú pháp mà ở identity và scope. Hai phép đo cùng tên vẫn có thể nói về hai population hoặc hai thời điểm khác nhau. Trong bài `Join strategies and the threshold that is not magic`, câu hỏi thực dụng là: Spark chọn broadcast, sort-merge, shuffle-hash hoặc storage-partition join dựa trên evidence nào, và vì sao threshold không phải phép màu? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 3. Sort merge

Sort-merge scales cho equi-join lớn nhưng trả chi phí exchange, sort và spill nếu inputs chưa đáp ứng distribution/order. Một dashboard xanh chỉ là tín hiệu. Muốn biến nó thành bằng chứng phải giữ input, phiên bản, rule, trạng thái trước–sau và cách tính độc lập. Trong bài `Join strategies and the threshold that is not magic`, câu hỏi thực dụng là: Spark chọn broadcast, sort-merge, shuffle-hash hoặc storage-partition join dựa trên evidence nào, và vì sao threshold không phải phép màu? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 4. Threshold

Auto-broadcast threshold là configuration applied to estimates, không bảo đảm runtime size hay performance tốt. Thiết kế tốt phải chịu được counterexample. Hãy chủ động tạo case sát boundary, case thiếu dữ liệu và case replay thay vì chỉ chạy happy path. Trong bài `Join strategies and the threshold that is not magic`, câu hỏi thực dụng là: Spark chọn broadcast, sort-merge, shuffle-hash hoặc storage-partition join dựa trên evidence nào, và vì sao threshold không phải phép màu? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 5. Statistics and AQE

Missing/stale stats gây plan xấu; runtime statistics có thể coalesce partitions, switch join hoặc handle skew theo AQE rules. Chi phí vận hành thuộc contract. Một rule đúng nhưng quá đắt, quá ồn hoặc không có owner sẽ nhanh chóng bị tắt và mất tác dụng. Trong bài `Join strategies and the threshold that is not magic`, câu hỏi thực dụng là: Spark chọn broadcast, sort-merge, shuffle-hash hoặc storage-partition join dựa trên evidence nào, và vì sao threshold không phải phép màu? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 6. Decision evidence

Benchmark giữ input stats, chosen/final plan, build size, shuffle/spill, skew distribution, configs và correctness hash. Kết luận cần có điều kiện đảo chiều. Khi volume, latency, nguồn thẩm quyền hoặc topology đổi, quyết định cũ phải được xem xét lại bằng cùng một oracle. Trong bài `Join strategies and the threshold that is not magic`, câu hỏi thực dụng là: Spark chọn broadcast, sort-merge, shuffle-hash hoặc storage-partition join dựa trên evidence nào, và vì sao threshold không phải phép màu? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 7. Ma trận kiểm chứng từng mệnh đề

Với `wiki.spark.join-strategies-thresholds`, command thành công không tự chứng minh dữ liệu đúng. Protocol riêng của bài là: Run a version-pinned Spark fixture with fixed inputs, capture explain/UI/event-log evidence, inject one changed constraint and reconcile output hashes plus operator/task metrics. Mỗi probe dưới đây phải nối input boundary với failure signal và oracle có thể phản bác kết luận.

### 7.1. Join strategies and the threshold that is not magic: kiểm `Strategy space` bằng case 1, cụ thể join type, equi keys, side sizes, partitioning, ordering và engine support giới hạn tập strategies hợp lệ

**Mệnh đề cần kiểm.** Join strategies and the threshold that is not magic: kiểm `Strategy space` bằng case 1, cụ thể join type, equi keys, side sizes, partitioning, ordering và engine support giới hạn tập strategies hợp lệ.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.join-strategies-thresholds`, tạo positive control và negative control chỉ khác đúng một điều kiện. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Join strategies and the threshold that is not magic` công bố.

**Bằng chứng cần giữ.** Đối với probe 1 của `Join strategies and the threshold that is not magic`, giữ fixture, raw failing rows và lệnh tái hiện. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.2. Join strategies and the threshold that is not magic: kiểm `Broadcast` bằng case 2, cụ thể broadcast hash join tránh shuffle phía lớn nhưng cần estimate nhỏ đáng tin và memory/network headroom trên executors

**Mệnh đề cần kiểm.** Join strategies and the threshold that is not magic: kiểm `Broadcast` bằng case 2, cụ thể broadcast hash join tránh shuffle phía lớn nhưng cần estimate nhỏ đáng tin và memory/network headroom trên executors.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.join-strategies-thresholds`, đổi grain nhưng giữ tổng số dòng để lộ phép đo sai cấp. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Join strategies and the threshold that is not magic` công bố.

**Bằng chứng cần giữ.** Đối với probe 2 của `Join strategies and the threshold that is not magic`, báo numerator, denominator và key set ở cả hai grain. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.3. Join strategies and the threshold that is not magic: kiểm `Sort merge` bằng case 3, cụ thể sort-merge scales cho equi-join lớn nhưng trả chi phí exchange, sort và spill nếu inputs chưa đáp ứng distribution/order

**Mệnh đề cần kiểm.** Join strategies and the threshold that is not magic: kiểm `Sort merge` bằng case 3, cụ thể sort-merge scales cho equi-join lớn nhưng trả chi phí exchange, sort và spill nếu inputs chưa đáp ứng distribution/order.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.join-strategies-thresholds`, đưa một giá trị tới đúng boundary và một giá trị vượt boundary. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Join strategies and the threshold that is not magic` công bố.

**Bằng chứng cần giữ.** Đối với probe 3 của `Join strategies and the threshold that is not magic`, lưu hai observed values cùng rule đã resolve. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.4. Join strategies and the threshold that is not magic: kiểm `Threshold` bằng case 4, cụ thể auto-broadcast threshold là configuration applied to estimates, không bảo đảm runtime size hay performance tốt

**Mệnh đề cần kiểm.** Join strategies and the threshold that is not magic: kiểm `Threshold` bằng case 4, cụ thể auto-broadcast threshold là configuration applied to estimates, không bảo đảm runtime size hay performance tốt.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.join-strategies-thresholds`, kill tiến trình ngay trước rồi ngay sau durable side effect. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Join strategies and the threshold that is not magic` công bố.

**Bằng chứng cần giữ.** Đối với probe 4 của `Join strategies and the threshold that is not magic`, lưu checkpoint, external ledger và trạng thái sau restart. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.5. Join strategies and the threshold that is not magic: kiểm `Statistics and AQE` bằng case 5, cụ thể missing/stale stats gây plan xấu; runtime statistics có thể coalesce partitions, switch join hoặc handle skew theo aqe rules

**Mệnh đề cần kiểm.** Join strategies and the threshold that is not magic: kiểm `Statistics and AQE` bằng case 5, cụ thể missing/stale stats gây plan xấu; runtime statistics có thể coalesce partitions, switch join hoặc handle skew theo aqe rules.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.join-strategies-thresholds`, đảo thứ tự input và concurrency nhưng giữ logical population. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Join strategies and the threshold that is not magic` công bố.

**Bằng chứng cần giữ.** Đối với probe 5 của `Join strategies and the threshold that is not magic`, so canonical hash và business totals giữa các thứ tự. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.6. Join strategies and the threshold that is not magic: kiểm `Decision evidence` bằng case 6, cụ thể benchmark giữ input stats, chosen/final plan, build size, shuffle/spill, skew distribution, configs và correctness hash

**Mệnh đề cần kiểm.** Join strategies and the threshold that is not magic: kiểm `Decision evidence` bằng case 6, cụ thể benchmark giữ input stats, chosen/final plan, build size, shuffle/spill, skew distribution, configs và correctness hash.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.join-strategies-thresholds`, replay cùng identity với payload giống rồi payload xung đột. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Join strategies and the threshold that is not magic` công bố.

**Bằng chứng cần giữ.** Đối với probe 6 của `Join strategies and the threshold that is not magic`, tách duplicate replay khỏi identity collision bằng reason code. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.7. Join strategies and the threshold that is not magic: kiểm `Strategy space` bằng case 7, cụ thể join type, equi keys, side sizes, partitioning, ordering và engine support giới hạn tập strategies hợp lệ

**Mệnh đề cần kiểm.** Join strategies and the threshold that is not magic: kiểm `Strategy space` bằng case 7, cụ thể join type, equi keys, side sizes, partitioning, ordering và engine support giới hạn tập strategies hợp lệ.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.join-strategies-thresholds`, thêm record tới trễ trong horizon và ngoài horizon. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Join strategies and the threshold that is not magic` công bố.

**Bằng chứng cần giữ.** Đối với probe 7 của `Join strategies and the threshold that is not magic`, báo accepted-late, rejected-late và oldest outstanding timestamp. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.8. Join strategies and the threshold that is not magic: kiểm `Broadcast` bằng case 8, cụ thể broadcast hash join tránh shuffle phía lớn nhưng cần estimate nhỏ đáng tin và memory/network headroom trên executors

**Mệnh đề cần kiểm.** Join strategies and the threshold that is not magic: kiểm `Broadcast` bằng case 8, cụ thể broadcast hash join tránh shuffle phía lớn nhưng cần estimate nhỏ đáng tin và memory/network headroom trên executors.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.join-strategies-thresholds`, đổi schema theo một cách tương thích rồi một cách phá vỡ semantics. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Join strategies and the threshold that is not magic` công bố.

**Bằng chứng cần giữ.** Đối với probe 8 của `Join strategies and the threshold that is not magic`, giữ schema diff, classification và consumer-visible result. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.9. Join strategies and the threshold that is not magic: kiểm `Sort merge` bằng case 9, cụ thể sort-merge scales cho equi-join lớn nhưng trả chi phí exchange, sort và spill nếu inputs chưa đáp ứng distribution/order

**Mệnh đề cần kiểm.** Join strategies and the threshold that is not magic: kiểm `Sort merge` bằng case 9, cụ thể sort-merge scales cho equi-join lớn nhưng trả chi phí exchange, sort và spill nếu inputs chưa đáp ứng distribution/order.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.join-strategies-thresholds`, tạo missing và duplicate bù nhau để count tổng không đổi. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Join strategies and the threshold that is not magic` công bố.

**Bằng chứng cần giữ.** Đối với probe 9 của `Join strategies and the threshold that is not magic`, so key multiset và typed hashes thay vì chỉ row count. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.10. Join strategies and the threshold that is not magic: kiểm `Threshold` bằng case 10, cụ thể auto-broadcast threshold là configuration applied to estimates, không bảo đảm runtime size hay performance tốt

**Mệnh đề cần kiểm.** Join strategies and the threshold that is not magic: kiểm `Threshold` bằng case 10, cụ thể auto-broadcast threshold là configuration applied to estimates, không bảo đảm runtime size hay performance tốt.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.join-strategies-thresholds`, cho reviewer tái hiện chỉ từ evidence package. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Join strategies and the threshold that is not magic` công bố.

**Bằng chứng cần giữ.** Đối với probe 10 của `Join strategies and the threshold that is not magic`, package phải đủ để người khác dựng lại decision và limitation. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.11. Join strategies and the threshold that is not magic: kiểm `Statistics and AQE` bằng case 11, cụ thể missing/stale stats gây plan xấu; runtime statistics có thể coalesce partitions, switch join hoặc handle skew theo aqe rules

**Mệnh đề cần kiểm.** Join strategies and the threshold that is not magic: kiểm `Statistics and AQE` bằng case 11, cụ thể missing/stale stats gây plan xấu; runtime statistics có thể coalesce partitions, switch join hoặc handle skew theo aqe rules.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.join-strategies-thresholds`, so với oracle độc lập không dùng chung query hoặc parser. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Join strategies and the threshold that is not magic` công bố.

**Bằng chứng cần giữ.** Đối với probe 11 của `Join strategies and the threshold that is not magic`, independent result phải khớp ở grain đã công bố. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.12. Join strategies and the threshold that is not magic: kiểm `Decision evidence` bằng case 12, cụ thể benchmark giữ input stats, chosen/final plan, build size, shuffle/spill, skew distribution, configs và correctness hash

**Mệnh đề cần kiểm.** Join strategies and the threshold that is not magic: kiểm `Decision evidence` bằng case 12, cụ thể benchmark giữ input stats, chosen/final plan, build size, shuffle/spill, skew distribution, configs và correctness hash.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.join-strategies-thresholds`, chạy scope hẹp và population đầy đủ rồi công bố phần bị loại. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Join strategies and the threshold that is not magic` công bố.

**Bằng chứng cần giữ.** Đối với probe 12 của `Join strategies and the threshold that is not magic`, coverage phải nêu rõ excluded nodes, partitions hoặc incidents. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.13. Join strategies and the threshold that is not magic: kiểm `Strategy space` bằng case 13, cụ thể join type, equi keys, side sizes, partitioning, ordering và engine support giới hạn tập strategies hợp lệ

**Mệnh đề cần kiểm.** Join strategies and the threshold that is not magic: kiểm `Strategy space` bằng case 13, cụ thể join type, equi keys, side sizes, partitioning, ordering và engine support giới hạn tập strategies hợp lệ.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.join-strategies-thresholds`, thử timezone, precision hoặc partition ở hai phía của ranh giới. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Join strategies and the threshold that is not magic` công bố.

**Bằng chứng cần giữ.** Đối với probe 13 của `Join strategies and the threshold that is not magic`, UTC/local interval và rounding policy phải hiện trong output. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.14. Join strategies and the threshold that is not magic: kiểm `Broadcast` bằng case 14, cụ thể broadcast hash join tránh shuffle phía lớn nhưng cần estimate nhỏ đáng tin và memory/network headroom trên executors

**Mệnh đề cần kiểm.** Join strategies and the threshold that is not magic: kiểm `Broadcast` bằng case 14, cụ thể broadcast hash join tránh shuffle phía lớn nhưng cần estimate nhỏ đáng tin và memory/network headroom trên executors.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.join-strategies-thresholds`, đổi constraint đủ lớn để quyết định phải đảo. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Join strategies and the threshold that is not magic` công bố.

**Bằng chứng cần giữ.** Đối với probe 14 của `Join strategies and the threshold that is not magic`, ADR phải lưu changed constraint và reversal threshold. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.15. Join strategies and the threshold that is not magic: kiểm `Sort merge` bằng case 15, cụ thể sort-merge scales cho equi-join lớn nhưng trả chi phí exchange, sort và spill nếu inputs chưa đáp ứng distribution/order

**Mệnh đề cần kiểm.** Join strategies and the threshold that is not magic: kiểm `Sort merge` bằng case 15, cụ thể sort-merge scales cho equi-join lớn nhưng trả chi phí exchange, sort và spill nếu inputs chưa đáp ứng distribution/order.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.spark.join-strategies-thresholds`, chạy lại từ môi trường sạch với versions và seed đã khóa. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Join strategies and the threshold that is not magic` công bố.

**Bằng chứng cần giữ.** Đối với probe 15 của `Join strategies and the threshold that is not magic`, canonical result phải ổn định hoặc mọi nondeterminism phải được giải thích. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

## 8. Quy trình phản biện

1. Viết consumer-visible invariant cho `Join strategies and the threshold that is not magic` trước khi chọn query hoặc tool.
2. Khóa grain, identity, population, time window và authoritative source.
3. Phân biệt declared configuration, executed state và published state.
4. Chạy negative control, replay hoặc changed-assumption case phù hợp.
5. Đối soát bằng oracle độc lập; công bố coverage và phần không quan sát được.
6. Gắn owner, hành động, reversal trigger và hạn review cho kết luận.

## 9. Câu hỏi tự kiểm tra

1. `Join strategies and the threshold that is not magic: kiểm `Strategy space` bằng case 1, cụ thể join type, equi keys, side sizes, partitioning, ordering và engine support giới hạn tập strategies hợp lệ` thất bại đầu tiên ở boundary nào?
2. Artifact nào mạnh nhất để trả lời `Join strategies and the threshold that is not magic: kiểm `Sort merge` bằng case 3, cụ thể sort-merge scales cho equi-join lớn nhưng trả chi phí exchange, sort và spill nếu inputs chưa đáp ứng distribution/order`?
3. Counterexample nhỏ nhất cho `Join strategies and the threshold that is not magic: kiểm `Decision evidence` bằng case 6, cụ thể benchmark giữ input stats, chosen/final plan, build size, shuffle/spill, skew distribution, configs và correctness hash` gồm những state nào?
4. `Join strategies and the threshold that is not magic: kiểm `Sort merge` bằng case 9, cụ thể sort-merge scales cho equi-join lớn nhưng trả chi phí exchange, sort và spill nếu inputs chưa đáp ứng distribution/order` có thể xanh giả ra sao?
5. Constraint nào khiến quyết định ở `Join strategies and the threshold that is not magic: kiểm `Broadcast` bằng case 14, cụ thể broadcast hash join tránh shuffle phía lớn nhưng cần estimate nhỏ đáng tin và memory/network headroom trên executors` phải đảo?
6. Phần nào của `Join strategies and the threshold that is not magic: kiểm `Sort merge` bằng case 15, cụ thể sort-merge scales cho equi-join lớn nhưng trả chi phí exchange, sort và spill nếu inputs chưa đáp ứng distribution/order` mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `Join strategies and the threshold that is not magic` chưa chạy trên hệ thống production; nội dung là giáo trình và expected evidence.
- Hành vi phụ thuộc phiên bản, connector, scheduler, warehouse và catalog configuration phải được kiểm lại.
- Các ma trận, ladder và threshold do giáo trình tổng hợp không được gán nguyên văn cho vendor.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-APACHE-SPARK-SQL-PERFORMANCE]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-APACHE-SPARK-SQL-PERFORMANCE]] | Contract hoặc cơ chế liên quan trực tiếp tới `Join strategies and the threshold that is not magic` | Đã đọc locator; cần pin version khi chạy lab |

## Key takeaways
- Join thresholds act on estimates and must be checked against final plans and runtime headroom.
- Với `wiki.spark.join-strategies-thresholds`, quality của kết luận phụ thuộc identity, coverage và oracle chứ không phụ thuộc màu dashboard.
- Câu hỏi `Spark chọn broadcast, sort-merge, shuffle-hash hoặc storage-partition join dựa trên evidence nào, và vì sao threshold không phải phép màu?` chỉ được trả lời trong scope và version đã ghi.
- Các source IDs `src.web.apache-spark-sql-performance` đặt ranh giới cho source fact; phần còn lại là synthesis có nhãn.
- Trước khi lab chạy, đây là note đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.
