---
note_id: wiki.distributed.partitioning-rebalancing
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
primary_question: Partitioning và rebalancing phân bố keys/load thế nào mà vẫn kiểm soát movement, hotspots và availability?
source_ids:
  - src.book.kleppmann-ddia.1e
aliases: [Partitioning, consistent hashing and rebalancing]
tags: [wiki/distributed-systems, distributed-systems, replication, consensus, reliability]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/201-partitioning-consistent-hashing-and-rebalancing.md
relationships:
  builds_on: [wiki.distributed.replication-topologies]
  prerequisite_of: [wiki.distributed.consistency-client-observations]
  related_to: []

---
# Partitioning, consistent hashing and rebalancing

> [!abstract] Câu hỏi trung tâm
> Partitioning và rebalancing phân bố keys/load thế nào mà vẫn kiểm soát movement, hotspots và availability?

## 1. Partition objective

Chia data/traffic để scale storage/compute nhưng mỗi key cần deterministic owner và replication placement. Đừng bắt đầu bằng tên công cụ. Hãy bắt đầu bằng đối tượng được bảo vệ, boundary quan sát được và hậu quả nếu kết luận sai. Trong bài `Partitioning, consistent hashing and rebalancing`, câu hỏi thực dụng là: Partitioning và rebalancing phân bố keys/load thế nào mà vẫn kiểm soát movement, hotspots và availability? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 2. Range and hash

Range hỗ trợ scans nhưng hotspot theo key/time; hash cân key count hơn nhưng phá locality và không cân workload tự động. Điểm khó không nằm ở cú pháp mà ở identity và scope. Hai phép đo cùng tên vẫn có thể nói về hai population hoặc hai thời điểm khác nhau. Trong bài `Partitioning, consistent hashing and rebalancing`, câu hỏi thực dụng là: Partitioning và rebalancing phân bố keys/load thế nào mà vẫn kiểm soát movement, hotspots và availability? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 3. Consistent hashing

Ring/vnodes giảm movement khi membership đổi nhưng distribution, heterogeneous capacity và replicas cần thiết kế thêm. Một dashboard xanh chỉ là tín hiệu. Muốn biến nó thành bằng chứng phải giữ input, phiên bản, rule, trạng thái trước–sau và cách tính độc lập. Trong bài `Partitioning, consistent hashing and rebalancing`, câu hỏi thực dụng là: Partitioning và rebalancing phân bố keys/load thế nào mà vẫn kiểm soát movement, hotspots và availability? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 4. Hot keys

Một key/popular tenant vượt capacity dù hash đều; split key, salting, cache hay dedicated shard có trade-offs semantics. Thiết kế tốt phải chịu được counterexample. Hãy chủ động tạo case sát boundary, case thiếu dữ liệu và case replay thay vì chỉ chạy happy path. Trong bài `Partitioning, consistent hashing and rebalancing`, câu hỏi thực dụng là: Partitioning và rebalancing phân bố keys/load thế nào mà vẫn kiểm soát movement, hotspots và availability? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 5. Rebalance protocol

Copy, catch up, ownership cutover và cleanup phải versioned; dual ownership cần fencing để tránh writes divergent. Chi phí vận hành thuộc contract. Một rule đúng nhưng quá đắt, quá ồn hoặc không có owner sẽ nhanh chóng bị tắt và mất tác dụng. Trong bài `Partitioning, consistent hashing and rebalancing`, câu hỏi thực dụng là: Partitioning và rebalancing phân bố keys/load thế nào mà vẫn kiểm soát movement, hotspots và availability? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 6. Evidence

Đo key/load skew, bytes moved, convergence time, error rate và correctness trong add/remove/failure scenarios. Kết luận cần có điều kiện đảo chiều. Khi volume, latency, nguồn thẩm quyền hoặc topology đổi, quyết định cũ phải được xem xét lại bằng cùng một oracle. Trong bài `Partitioning, consistent hashing and rebalancing`, câu hỏi thực dụng là: Partitioning và rebalancing phân bố keys/load thế nào mà vẫn kiểm soát movement, hotspots và availability? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 7. Ma trận kiểm chứng từng mệnh đề

Với `wiki.distributed.partitioning-rebalancing`, command thành công không tự chứng minh dữ liệu đúng. Protocol riêng của bài là: Sinh bounded histories có invocation/response, network schedule và node state; kiểm invariant bằng model/oracle tách khỏi implementation. Mỗi probe dưới đây phải nối input boundary với failure signal và oracle có thể phản bác kết luận.

### 7.1. Partitioning, consistent hashing and rebalancing: kiểm `Partition objective` bằng case 1, cụ thể chia data/traffic để scale storage/compute nhưng mỗi key cần deterministic owner và replication placement

**Mệnh đề cần kiểm.** Partitioning, consistent hashing and rebalancing: kiểm `Partition objective` bằng case 1, cụ thể chia data/traffic để scale storage/compute nhưng mỗi key cần deterministic owner và replication placement.

**Thiết kế phép thử cho `wiki.distributed.partitioning-rebalancing`.** Trong ngữ cảnh `wiki.distributed.partitioning-rebalancing`, tạo positive control và negative control chỉ khác đúng một điều kiện. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Partitioning, consistent hashing and rebalancing` công bố.

**Bằng chứng cần giữ.** Đối với probe 1 của `Partitioning, consistent hashing and rebalancing`, giữ fixture, raw failing rows và lệnh tái hiện. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.2. Partitioning, consistent hashing and rebalancing: kiểm `Range and hash` bằng case 2, cụ thể range hỗ trợ scans nhưng hotspot theo key/time; hash cân key count hơn nhưng phá locality và không cân workload tự động

**Mệnh đề cần kiểm.** Partitioning, consistent hashing and rebalancing: kiểm `Range and hash` bằng case 2, cụ thể range hỗ trợ scans nhưng hotspot theo key/time; hash cân key count hơn nhưng phá locality và không cân workload tự động.

**Thiết kế phép thử cho `wiki.distributed.partitioning-rebalancing`.** Trong ngữ cảnh `wiki.distributed.partitioning-rebalancing`, đổi grain nhưng giữ tổng số dòng để lộ phép đo sai cấp. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Partitioning, consistent hashing and rebalancing` công bố.

**Bằng chứng cần giữ.** Đối với probe 2 của `Partitioning, consistent hashing and rebalancing`, báo numerator, denominator và key set ở cả hai grain. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.3. Partitioning, consistent hashing and rebalancing: kiểm `Consistent hashing` bằng case 3, cụ thể ring/vnodes giảm movement khi membership đổi nhưng distribution, heterogeneous capacity và replicas cần thiết kế thêm

**Mệnh đề cần kiểm.** Partitioning, consistent hashing and rebalancing: kiểm `Consistent hashing` bằng case 3, cụ thể ring/vnodes giảm movement khi membership đổi nhưng distribution, heterogeneous capacity và replicas cần thiết kế thêm.

**Thiết kế phép thử cho `wiki.distributed.partitioning-rebalancing`.** Trong ngữ cảnh `wiki.distributed.partitioning-rebalancing`, đưa một giá trị tới đúng boundary và một giá trị vượt boundary. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Partitioning, consistent hashing and rebalancing` công bố.

**Bằng chứng cần giữ.** Đối với probe 3 của `Partitioning, consistent hashing and rebalancing`, lưu hai observed values cùng rule đã resolve. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.4. Partitioning, consistent hashing and rebalancing: kiểm `Hot keys` bằng case 4, cụ thể một key/popular tenant vượt capacity dù hash đều; split key, salting, cache hay dedicated shard có trade-offs semantics

**Mệnh đề cần kiểm.** Partitioning, consistent hashing and rebalancing: kiểm `Hot keys` bằng case 4, cụ thể một key/popular tenant vượt capacity dù hash đều; split key, salting, cache hay dedicated shard có trade-offs semantics.

**Thiết kế phép thử cho `wiki.distributed.partitioning-rebalancing`.** Trong ngữ cảnh `wiki.distributed.partitioning-rebalancing`, kill tiến trình ngay trước rồi ngay sau durable side effect. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Partitioning, consistent hashing and rebalancing` công bố.

**Bằng chứng cần giữ.** Đối với probe 4 của `Partitioning, consistent hashing and rebalancing`, lưu checkpoint, external ledger và trạng thái sau restart. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.5. Partitioning, consistent hashing and rebalancing: kiểm `Rebalance protocol` bằng case 5, cụ thể copy, catch up, ownership cutover và cleanup phải versioned; dual ownership cần fencing để tránh writes divergent

**Mệnh đề cần kiểm.** Partitioning, consistent hashing and rebalancing: kiểm `Rebalance protocol` bằng case 5, cụ thể copy, catch up, ownership cutover và cleanup phải versioned; dual ownership cần fencing để tránh writes divergent.

**Thiết kế phép thử cho `wiki.distributed.partitioning-rebalancing`.** Trong ngữ cảnh `wiki.distributed.partitioning-rebalancing`, đảo thứ tự input và concurrency nhưng giữ logical population. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Partitioning, consistent hashing and rebalancing` công bố.

**Bằng chứng cần giữ.** Đối với probe 5 của `Partitioning, consistent hashing and rebalancing`, so canonical hash và business totals giữa các thứ tự. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.6. Partitioning, consistent hashing and rebalancing: kiểm `Evidence` bằng case 6, cụ thể đo key/load skew, bytes moved, convergence time, error rate và correctness trong add/remove/failure scenarios

**Mệnh đề cần kiểm.** Partitioning, consistent hashing and rebalancing: kiểm `Evidence` bằng case 6, cụ thể đo key/load skew, bytes moved, convergence time, error rate và correctness trong add/remove/failure scenarios.

**Thiết kế phép thử cho `wiki.distributed.partitioning-rebalancing`.** Trong ngữ cảnh `wiki.distributed.partitioning-rebalancing`, replay cùng identity với payload giống rồi payload xung đột. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Partitioning, consistent hashing and rebalancing` công bố.

**Bằng chứng cần giữ.** Đối với probe 6 của `Partitioning, consistent hashing and rebalancing`, tách duplicate replay khỏi identity collision bằng reason code. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.7. Partitioning, consistent hashing and rebalancing: kiểm `Partition objective` bằng case 7, cụ thể chia data/traffic để scale storage/compute nhưng mỗi key cần deterministic owner và replication placement

**Mệnh đề cần kiểm.** Partitioning, consistent hashing and rebalancing: kiểm `Partition objective` bằng case 7, cụ thể chia data/traffic để scale storage/compute nhưng mỗi key cần deterministic owner và replication placement.

**Thiết kế phép thử cho `wiki.distributed.partitioning-rebalancing`.** Trong ngữ cảnh `wiki.distributed.partitioning-rebalancing`, thêm record tới trễ trong horizon và ngoài horizon. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Partitioning, consistent hashing and rebalancing` công bố.

**Bằng chứng cần giữ.** Đối với probe 7 của `Partitioning, consistent hashing and rebalancing`, báo accepted-late, rejected-late và oldest outstanding timestamp. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.8. Partitioning, consistent hashing and rebalancing: kiểm `Range and hash` bằng case 8, cụ thể range hỗ trợ scans nhưng hotspot theo key/time; hash cân key count hơn nhưng phá locality và không cân workload tự động

**Mệnh đề cần kiểm.** Partitioning, consistent hashing and rebalancing: kiểm `Range and hash` bằng case 8, cụ thể range hỗ trợ scans nhưng hotspot theo key/time; hash cân key count hơn nhưng phá locality và không cân workload tự động.

**Thiết kế phép thử cho `wiki.distributed.partitioning-rebalancing`.** Trong ngữ cảnh `wiki.distributed.partitioning-rebalancing`, đổi schema theo một cách tương thích rồi một cách phá vỡ semantics. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Partitioning, consistent hashing and rebalancing` công bố.

**Bằng chứng cần giữ.** Đối với probe 8 của `Partitioning, consistent hashing and rebalancing`, giữ schema diff, classification và consumer-visible result. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.9. Partitioning, consistent hashing and rebalancing: kiểm `Consistent hashing` bằng case 9, cụ thể ring/vnodes giảm movement khi membership đổi nhưng distribution, heterogeneous capacity và replicas cần thiết kế thêm

**Mệnh đề cần kiểm.** Partitioning, consistent hashing and rebalancing: kiểm `Consistent hashing` bằng case 9, cụ thể ring/vnodes giảm movement khi membership đổi nhưng distribution, heterogeneous capacity và replicas cần thiết kế thêm.

**Thiết kế phép thử cho `wiki.distributed.partitioning-rebalancing`.** Trong ngữ cảnh `wiki.distributed.partitioning-rebalancing`, tạo missing và duplicate bù nhau để count tổng không đổi. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Partitioning, consistent hashing and rebalancing` công bố.

**Bằng chứng cần giữ.** Đối với probe 9 của `Partitioning, consistent hashing and rebalancing`, so key multiset và typed hashes thay vì chỉ row count. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.10. Partitioning, consistent hashing and rebalancing: kiểm `Hot keys` bằng case 10, cụ thể một key/popular tenant vượt capacity dù hash đều; split key, salting, cache hay dedicated shard có trade-offs semantics

**Mệnh đề cần kiểm.** Partitioning, consistent hashing and rebalancing: kiểm `Hot keys` bằng case 10, cụ thể một key/popular tenant vượt capacity dù hash đều; split key, salting, cache hay dedicated shard có trade-offs semantics.

**Thiết kế phép thử cho `wiki.distributed.partitioning-rebalancing`.** Trong ngữ cảnh `wiki.distributed.partitioning-rebalancing`, cho reviewer tái hiện chỉ từ evidence package. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Partitioning, consistent hashing and rebalancing` công bố.

**Bằng chứng cần giữ.** Đối với probe 10 của `Partitioning, consistent hashing and rebalancing`, package phải đủ để người khác dựng lại decision và limitation. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.11. Partitioning, consistent hashing and rebalancing: kiểm `Rebalance protocol` bằng case 11, cụ thể copy, catch up, ownership cutover và cleanup phải versioned; dual ownership cần fencing để tránh writes divergent

**Mệnh đề cần kiểm.** Partitioning, consistent hashing and rebalancing: kiểm `Rebalance protocol` bằng case 11, cụ thể copy, catch up, ownership cutover và cleanup phải versioned; dual ownership cần fencing để tránh writes divergent.

**Thiết kế phép thử cho `wiki.distributed.partitioning-rebalancing`.** Trong ngữ cảnh `wiki.distributed.partitioning-rebalancing`, so với oracle độc lập không dùng chung query hoặc parser. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Partitioning, consistent hashing and rebalancing` công bố.

**Bằng chứng cần giữ.** Đối với probe 11 của `Partitioning, consistent hashing and rebalancing`, independent result phải khớp ở grain đã công bố. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.12. Partitioning, consistent hashing and rebalancing: kiểm `Evidence` bằng case 12, cụ thể đo key/load skew, bytes moved, convergence time, error rate và correctness trong add/remove/failure scenarios

**Mệnh đề cần kiểm.** Partitioning, consistent hashing and rebalancing: kiểm `Evidence` bằng case 12, cụ thể đo key/load skew, bytes moved, convergence time, error rate và correctness trong add/remove/failure scenarios.

**Thiết kế phép thử cho `wiki.distributed.partitioning-rebalancing`.** Trong ngữ cảnh `wiki.distributed.partitioning-rebalancing`, chạy scope hẹp và population đầy đủ rồi công bố phần bị loại. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Partitioning, consistent hashing and rebalancing` công bố.

**Bằng chứng cần giữ.** Đối với probe 12 của `Partitioning, consistent hashing and rebalancing`, coverage phải nêu rõ excluded nodes, partitions hoặc incidents. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.13. Partitioning, consistent hashing and rebalancing: kiểm `Partition objective` bằng case 13, cụ thể chia data/traffic để scale storage/compute nhưng mỗi key cần deterministic owner và replication placement

**Mệnh đề cần kiểm.** Partitioning, consistent hashing and rebalancing: kiểm `Partition objective` bằng case 13, cụ thể chia data/traffic để scale storage/compute nhưng mỗi key cần deterministic owner và replication placement.

**Thiết kế phép thử cho `wiki.distributed.partitioning-rebalancing`.** Trong ngữ cảnh `wiki.distributed.partitioning-rebalancing`, thử timezone, precision hoặc partition ở hai phía của ranh giới. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Partitioning, consistent hashing and rebalancing` công bố.

**Bằng chứng cần giữ.** Đối với probe 13 của `Partitioning, consistent hashing and rebalancing`, UTC/local interval và rounding policy phải hiện trong output. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.14. Partitioning, consistent hashing and rebalancing: kiểm `Range and hash` bằng case 14, cụ thể range hỗ trợ scans nhưng hotspot theo key/time; hash cân key count hơn nhưng phá locality và không cân workload tự động

**Mệnh đề cần kiểm.** Partitioning, consistent hashing and rebalancing: kiểm `Range and hash` bằng case 14, cụ thể range hỗ trợ scans nhưng hotspot theo key/time; hash cân key count hơn nhưng phá locality và không cân workload tự động.

**Thiết kế phép thử cho `wiki.distributed.partitioning-rebalancing`.** Trong ngữ cảnh `wiki.distributed.partitioning-rebalancing`, đổi constraint đủ lớn để quyết định phải đảo. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Partitioning, consistent hashing and rebalancing` công bố.

**Bằng chứng cần giữ.** Đối với probe 14 của `Partitioning, consistent hashing and rebalancing`, ADR phải lưu changed constraint và reversal threshold. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.15. Partitioning, consistent hashing and rebalancing: kiểm `Consistent hashing` bằng case 15, cụ thể ring/vnodes giảm movement khi membership đổi nhưng distribution, heterogeneous capacity và replicas cần thiết kế thêm

**Mệnh đề cần kiểm.** Partitioning, consistent hashing and rebalancing: kiểm `Consistent hashing` bằng case 15, cụ thể ring/vnodes giảm movement khi membership đổi nhưng distribution, heterogeneous capacity và replicas cần thiết kế thêm.

**Thiết kế phép thử cho `wiki.distributed.partitioning-rebalancing`.** Trong ngữ cảnh `wiki.distributed.partitioning-rebalancing`, chạy lại từ môi trường sạch với versions và seed đã khóa. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Partitioning, consistent hashing and rebalancing` công bố.

**Bằng chứng cần giữ.** Đối với probe 15 của `Partitioning, consistent hashing and rebalancing`, canonical result phải ổn định hoặc mọi nondeterminism phải được giải thích. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

## 8. Quy trình phản biện

1. Viết consumer-visible invariant cho `Partitioning, consistent hashing and rebalancing` trước khi chọn query hoặc tool.
2. Khóa grain, identity, population, time window và authoritative source.
3. Phân biệt declared configuration, executed state và published state.
4. Chạy negative control, replay hoặc changed-assumption case phù hợp.
5. Đối soát bằng oracle độc lập; công bố coverage và phần không quan sát được.
6. Gắn owner, hành động, reversal trigger và hạn review cho kết luận.

## 9. Câu hỏi tự kiểm tra

1. `Partitioning, consistent hashing and rebalancing: kiểm `Partition objective` bằng case 1, cụ thể chia data/traffic để scale storage/compute nhưng mỗi key cần deterministic owner và replication placement` thất bại đầu tiên ở boundary nào?
2. Artifact nào mạnh nhất để trả lời `Partitioning, consistent hashing and rebalancing: kiểm `Consistent hashing` bằng case 3, cụ thể ring/vnodes giảm movement khi membership đổi nhưng distribution, heterogeneous capacity và replicas cần thiết kế thêm`?
3. Counterexample nhỏ nhất cho `Partitioning, consistent hashing and rebalancing: kiểm `Evidence` bằng case 6, cụ thể đo key/load skew, bytes moved, convergence time, error rate và correctness trong add/remove/failure scenarios` gồm những state nào?
4. `Partitioning, consistent hashing and rebalancing: kiểm `Consistent hashing` bằng case 9, cụ thể ring/vnodes giảm movement khi membership đổi nhưng distribution, heterogeneous capacity và replicas cần thiết kế thêm` có thể xanh giả ra sao?
5. Constraint nào khiến quyết định ở `Partitioning, consistent hashing and rebalancing: kiểm `Range and hash` bằng case 14, cụ thể range hỗ trợ scans nhưng hotspot theo key/time; hash cân key count hơn nhưng phá locality và không cân workload tự động` phải đảo?
6. Phần nào của `Partitioning, consistent hashing and rebalancing: kiểm `Consistent hashing` bằng case 15, cụ thể ring/vnodes giảm movement khi membership đổi nhưng distribution, heterogeneous capacity và replicas cần thiết kế thêm` mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `Partitioning, consistent hashing and rebalancing` chưa chạy trên hệ thống production; nội dung là giáo trình và expected evidence.
- Hành vi phụ thuộc phiên bản, connector, scheduler, warehouse và catalog configuration phải được kiểm lại.
- Các ma trận, ladder và threshold do giáo trình tổng hợp không được gán nguyên văn cho vendor.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-KLEPPMANN-DDIA-1E]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-KLEPPMANN-DDIA-1E]] | Contract hoặc cơ chế liên quan trực tiếp tới `Partitioning, consistent hashing and rebalancing` | Đã đọc locator; cần pin version khi chạy lab |

## Key takeaways
- Even key distribution không đảm bảo even load; rebalance cần ownership protocol.
- Với `wiki.distributed.partitioning-rebalancing`, quality của kết luận phụ thuộc identity, coverage và oracle chứ không phụ thuộc màu dashboard.
- Câu hỏi `Partitioning và rebalancing phân bố keys/load thế nào mà vẫn kiểm soát movement, hotspots và availability?` chỉ được trả lời trong scope và version đã ghi.
- Các source IDs `src.book.kleppmann-ddia.1e` đặt ranh giới cho source fact; phần còn lại là synthesis có nhãn.
- Trước khi lab chạy, đây là note đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule — kiểm chứng `wiki.distributed.partitioning-rebalancing`

> [!important] Phân loại mệnh đề
> Với `wiki.distributed.partitioning-rebalancing`, sơ đồ, ví dụ và artifact về **Partitioning, consistent hashing and rebalancing** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.book.kleppmann-ddia.1e"] --> B["Khóa boundary"]
    B --> M["Cơ chế: Partitioning, consistent hashing and rebalancing"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.distributed.partitioning-rebalancing` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **Partitioning, consistent hashing and rebalancing**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```sql
-- Verification harness for: Partitioning, consistent hashing and rebalancing
WITH evidence AS (
    SELECT 'wiki.distributed.partitioning-rebalancing' AS concept_id,
           'boundary_declared' AS check_name, 1 AS passed
    UNION ALL
    SELECT 'wiki.distributed.partitioning-rebalancing', 'independent_oracle', 1
    UNION ALL
    SELECT 'wiki.distributed.partitioning-rebalancing', 'reversal_trigger_recorded', 1
)
SELECT concept_id,
       MIN(passed) AS all_hard_checks_pass,
       COUNT(*) AS evidence_items
FROM evidence
GROUP BY concept_id
HAVING MIN(passed) = 1;
```

Artifact của `wiki.distributed.partitioning-rebalancing` buộc người dùng ghi boundary, oracle và reversal trigger cho **Partitioning, consistent hashing and rebalancing**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

### Tự kiểm tra trước khi tái sử dụng

1. Bạn có thể trả lời `Partitioning và rebalancing phân bố keys/load thế nào mà vẫn kiểm soát movement, hotspots và availability?` bằng một câu mà không kéo thêm concept thứ hai không?
2. Source locator nào đỡ cho claim, và phần nào chỉ là synthesis trong note?
3. Observation nào khiến bạn dừng, thu hẹp hoặc đảo quyết định?
4. Artifact nào cho phép một reviewer độc lập tái hiện kết quả?

<!-- ATOMIC-EXECUTION-CAPSULE:END -->
