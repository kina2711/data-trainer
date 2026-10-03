# Phase 8: Distributed Systems, Streaming and Compute
# Module 22: Change Data Capture Internals
# Lesson 336: Inside the transaction log - WAL, logical decoding and the replication slot

## Mục tiêu bài học

**Năng lực cần chứng minh.** Đọc được vị trí và trạng thái khe trên nguồn thật, và định lượng tốc độ tích luỹ nhật ký khi bên đọc dừng.

**Điều kiện hoàn thành.** Tốc độ tích luỹ được đo theo dung lượng trên giờ, thời gian tới khi đầy đĩa tính được, và nhật ký được giải phóng sau khi bên đọc chạy lại.

> [!abstract] Câu hỏi trung tâm
> WAL, logical decoding, output plugin và replication slot phối hợp để CDC đọc committed changes thế nào?

## 1. WAL purpose

WAL trước hết phục vụ durability/recovery; physical records không mặc nhiên là business change events. Đừng bắt đầu bằng tên công cụ. Hãy bắt đầu bằng đối tượng được bảo vệ, boundary quan sát được và hậu quả nếu kết luận sai. Trong bài `Inside the transaction log - WAL, logical decoding and the replication slot`, câu hỏi thực dụng là: WAL, logical decoding, output plugin và replication slot phối hợp để CDC đọc committed changes thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 2. Logical decoding

Decoder reconstructs logical changes từ WAL với transaction boundaries và plugin format dưới source/version rules. Điểm khó không nằm ở cú pháp mà ở identity và scope. Hai phép đo cùng tên vẫn có thể nói về hai population hoặc hai thời điểm khác nhau. Trong bài `Inside the transaction log - WAL, logical decoding and the replication slot`, câu hỏi thực dụng là: WAL, logical decoding, output plugin và replication slot phối hợp để CDC đọc committed changes thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 3. Replication slot

Slot giữ restart position và ngăn WAL cần thiết bị recycle, đổi reliability lấy source disk liability. Một dashboard xanh chỉ là tín hiệu. Muốn biến nó thành bằng chứng phải giữ input, phiên bản, rule, trạng thái trước–sau và cách tính độc lập. Trong bài `Inside the transaction log - WAL, logical decoding and the replication slot`, câu hỏi thực dụng là: WAL, logical decoding, output plugin và replication slot phối hợp để CDC đọc committed changes thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 4. Publication and identity

Publication/table filters, replica identity và primary keys quyết định before image/key/delete fidelity. Thiết kế tốt phải chịu được counterexample. Hãy chủ động tạo case sát boundary, case thiếu dữ liệu và case replay thay vì chỉ chạy happy path. Trong bài `Inside the transaction log - WAL, logical decoding and the replication slot`, câu hỏi thực dụng là: WAL, logical decoding, output plugin và replication slot phối hợp để CDC đọc committed changes thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 5. Commit visibility

Connector chỉ emit committed changes theo protocol; long/open transactions và rollback ảnh hưởng lag/visibility. Chi phí vận hành thuộc contract. Một rule đúng nhưng quá đắt, quá ồn hoặc không có owner sẽ nhanh chóng bị tắt và mất tác dụng. Trong bài `Inside the transaction log - WAL, logical decoding and the replication slot`, câu hỏi thực dụng là: WAL, logical decoding, output plugin và replication slot phối hợp để CDC đọc committed changes thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 6. Inspection lab

Create slot/publication, mutate/rollback rows, consume changes and compare LSN, transaction, keys and source WAL retention. Kết luận cần có điều kiện đảo chiều. Khi volume, latency, nguồn thẩm quyền hoặc topology đổi, quyết định cũ phải được xem xét lại bằng cùng một oracle. Trong bài `Inside the transaction log - WAL, logical decoding and the replication slot`, câu hỏi thực dụng là: WAL, logical decoding, output plugin và replication slot phối hợp để CDC đọc committed changes thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 7. Ma trận kiểm chứng từng mệnh đề

Với `wiki.cdc.wal-logical-decoding-slot`, command thành công không tự chứng minh dữ liệu đúng. Protocol riêng của bài là: Run PostgreSQL/Debezium-compatible fixture, inject writes/crash/interleaving and reconcile source keys, log positions, transport offsets and sink state. Mỗi probe dưới đây phải nối input boundary với failure signal và oracle có thể phản bác kết luận.

### 7.1. Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `WAL purpose` bằng case 1, cụ thể wal trước hết phục vụ durability/recovery; physical records không mặc nhiên là business change events

**Mệnh đề cần kiểm.** Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `WAL purpose` bằng case 1, cụ thể wal trước hết phục vụ durability/recovery; physical records không mặc nhiên là business change events.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.wal-logical-decoding-slot`, tạo positive control và negative control chỉ khác đúng một điều kiện. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Inside the transaction log - WAL, logical decoding and the replication slot` công bố.

**Bằng chứng cần giữ.** Đối với probe 1 của `Inside the transaction log - WAL, logical decoding and the replication slot`, giữ fixture, raw failing rows và lệnh tái hiện. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.2. Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `Logical decoding` bằng case 2, cụ thể decoder reconstructs logical changes từ wal với transaction boundaries và plugin format dưới source/version rules

**Mệnh đề cần kiểm.** Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `Logical decoding` bằng case 2, cụ thể decoder reconstructs logical changes từ wal với transaction boundaries và plugin format dưới source/version rules.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.wal-logical-decoding-slot`, đổi grain nhưng giữ tổng số dòng để lộ phép đo sai cấp. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Inside the transaction log - WAL, logical decoding and the replication slot` công bố.

**Bằng chứng cần giữ.** Đối với probe 2 của `Inside the transaction log - WAL, logical decoding and the replication slot`, báo numerator, denominator và key set ở cả hai grain. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.3. Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `Replication slot` bằng case 3, cụ thể slot giữ restart position và ngăn wal cần thiết bị recycle, đổi reliability lấy source disk liability

**Mệnh đề cần kiểm.** Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `Replication slot` bằng case 3, cụ thể slot giữ restart position và ngăn wal cần thiết bị recycle, đổi reliability lấy source disk liability.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.wal-logical-decoding-slot`, đưa một giá trị tới đúng boundary và một giá trị vượt boundary. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Inside the transaction log - WAL, logical decoding and the replication slot` công bố.

**Bằng chứng cần giữ.** Đối với probe 3 của `Inside the transaction log - WAL, logical decoding and the replication slot`, lưu hai observed values cùng rule đã resolve. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.4. Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `Publication and identity` bằng case 4, cụ thể publication/table filters, replica identity và primary keys quyết định before image/key/delete fidelity

**Mệnh đề cần kiểm.** Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `Publication and identity` bằng case 4, cụ thể publication/table filters, replica identity và primary keys quyết định before image/key/delete fidelity.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.wal-logical-decoding-slot`, kill tiến trình ngay trước rồi ngay sau durable side effect. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Inside the transaction log - WAL, logical decoding and the replication slot` công bố.

**Bằng chứng cần giữ.** Đối với probe 4 của `Inside the transaction log - WAL, logical decoding and the replication slot`, lưu checkpoint, external ledger và trạng thái sau restart. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.5. Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `Commit visibility` bằng case 5, cụ thể connector chỉ emit committed changes theo protocol; long/open transactions và rollback ảnh hưởng lag/visibility

**Mệnh đề cần kiểm.** Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `Commit visibility` bằng case 5, cụ thể connector chỉ emit committed changes theo protocol; long/open transactions và rollback ảnh hưởng lag/visibility.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.wal-logical-decoding-slot`, đảo thứ tự input và concurrency nhưng giữ logical population. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Inside the transaction log - WAL, logical decoding and the replication slot` công bố.

**Bằng chứng cần giữ.** Đối với probe 5 của `Inside the transaction log - WAL, logical decoding and the replication slot`, so canonical hash và business totals giữa các thứ tự. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.6. Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `Inspection lab` bằng case 6, cụ thể create slot/publication, mutate/rollback rows, consume changes and compare lsn, transaction, keys and source wal retention

**Mệnh đề cần kiểm.** Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `Inspection lab` bằng case 6, cụ thể create slot/publication, mutate/rollback rows, consume changes and compare lsn, transaction, keys and source wal retention.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.wal-logical-decoding-slot`, replay cùng identity với payload giống rồi payload xung đột. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Inside the transaction log - WAL, logical decoding and the replication slot` công bố.

**Bằng chứng cần giữ.** Đối với probe 6 của `Inside the transaction log - WAL, logical decoding and the replication slot`, tách duplicate replay khỏi identity collision bằng reason code. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.7. Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `WAL purpose` bằng case 7, cụ thể wal trước hết phục vụ durability/recovery; physical records không mặc nhiên là business change events

**Mệnh đề cần kiểm.** Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `WAL purpose` bằng case 7, cụ thể wal trước hết phục vụ durability/recovery; physical records không mặc nhiên là business change events.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.wal-logical-decoding-slot`, thêm record tới trễ trong horizon và ngoài horizon. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Inside the transaction log - WAL, logical decoding and the replication slot` công bố.

**Bằng chứng cần giữ.** Đối với probe 7 của `Inside the transaction log - WAL, logical decoding and the replication slot`, báo accepted-late, rejected-late và oldest outstanding timestamp. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.8. Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `Logical decoding` bằng case 8, cụ thể decoder reconstructs logical changes từ wal với transaction boundaries và plugin format dưới source/version rules

**Mệnh đề cần kiểm.** Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `Logical decoding` bằng case 8, cụ thể decoder reconstructs logical changes từ wal với transaction boundaries và plugin format dưới source/version rules.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.wal-logical-decoding-slot`, đổi schema theo một cách tương thích rồi một cách phá vỡ semantics. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Inside the transaction log - WAL, logical decoding and the replication slot` công bố.

**Bằng chứng cần giữ.** Đối với probe 8 của `Inside the transaction log - WAL, logical decoding and the replication slot`, giữ schema diff, classification và consumer-visible result. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.9. Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `Replication slot` bằng case 9, cụ thể slot giữ restart position và ngăn wal cần thiết bị recycle, đổi reliability lấy source disk liability

**Mệnh đề cần kiểm.** Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `Replication slot` bằng case 9, cụ thể slot giữ restart position và ngăn wal cần thiết bị recycle, đổi reliability lấy source disk liability.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.wal-logical-decoding-slot`, tạo missing và duplicate bù nhau để count tổng không đổi. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Inside the transaction log - WAL, logical decoding and the replication slot` công bố.

**Bằng chứng cần giữ.** Đối với probe 9 của `Inside the transaction log - WAL, logical decoding and the replication slot`, so key multiset và typed hashes thay vì chỉ row count. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.10. Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `Publication and identity` bằng case 10, cụ thể publication/table filters, replica identity và primary keys quyết định before image/key/delete fidelity

**Mệnh đề cần kiểm.** Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `Publication and identity` bằng case 10, cụ thể publication/table filters, replica identity và primary keys quyết định before image/key/delete fidelity.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.wal-logical-decoding-slot`, cho reviewer tái hiện chỉ từ evidence package. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Inside the transaction log - WAL, logical decoding and the replication slot` công bố.

**Bằng chứng cần giữ.** Đối với probe 10 của `Inside the transaction log - WAL, logical decoding and the replication slot`, package phải đủ để người khác dựng lại decision và limitation. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.11. Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `Commit visibility` bằng case 11, cụ thể connector chỉ emit committed changes theo protocol; long/open transactions và rollback ảnh hưởng lag/visibility

**Mệnh đề cần kiểm.** Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `Commit visibility` bằng case 11, cụ thể connector chỉ emit committed changes theo protocol; long/open transactions và rollback ảnh hưởng lag/visibility.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.wal-logical-decoding-slot`, so với oracle độc lập không dùng chung query hoặc parser. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Inside the transaction log - WAL, logical decoding and the replication slot` công bố.

**Bằng chứng cần giữ.** Đối với probe 11 của `Inside the transaction log - WAL, logical decoding and the replication slot`, independent result phải khớp ở grain đã công bố. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.12. Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `Inspection lab` bằng case 12, cụ thể create slot/publication, mutate/rollback rows, consume changes and compare lsn, transaction, keys and source wal retention

**Mệnh đề cần kiểm.** Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `Inspection lab` bằng case 12, cụ thể create slot/publication, mutate/rollback rows, consume changes and compare lsn, transaction, keys and source wal retention.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.wal-logical-decoding-slot`, chạy scope hẹp và population đầy đủ rồi công bố phần bị loại. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Inside the transaction log - WAL, logical decoding and the replication slot` công bố.

**Bằng chứng cần giữ.** Đối với probe 12 của `Inside the transaction log - WAL, logical decoding and the replication slot`, coverage phải nêu rõ excluded nodes, partitions hoặc incidents. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.13. Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `WAL purpose` bằng case 13, cụ thể wal trước hết phục vụ durability/recovery; physical records không mặc nhiên là business change events

**Mệnh đề cần kiểm.** Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `WAL purpose` bằng case 13, cụ thể wal trước hết phục vụ durability/recovery; physical records không mặc nhiên là business change events.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.wal-logical-decoding-slot`, thử timezone, precision hoặc partition ở hai phía của ranh giới. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Inside the transaction log - WAL, logical decoding and the replication slot` công bố.

**Bằng chứng cần giữ.** Đối với probe 13 của `Inside the transaction log - WAL, logical decoding and the replication slot`, UTC/local interval và rounding policy phải hiện trong output. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.14. Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `Logical decoding` bằng case 14, cụ thể decoder reconstructs logical changes từ wal với transaction boundaries và plugin format dưới source/version rules

**Mệnh đề cần kiểm.** Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `Logical decoding` bằng case 14, cụ thể decoder reconstructs logical changes từ wal với transaction boundaries và plugin format dưới source/version rules.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.wal-logical-decoding-slot`, đổi constraint đủ lớn để quyết định phải đảo. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Inside the transaction log - WAL, logical decoding and the replication slot` công bố.

**Bằng chứng cần giữ.** Đối với probe 14 của `Inside the transaction log - WAL, logical decoding and the replication slot`, ADR phải lưu changed constraint và reversal threshold. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.15. Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `Replication slot` bằng case 15, cụ thể slot giữ restart position và ngăn wal cần thiết bị recycle, đổi reliability lấy source disk liability

**Mệnh đề cần kiểm.** Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `Replication slot` bằng case 15, cụ thể slot giữ restart position và ngăn wal cần thiết bị recycle, đổi reliability lấy source disk liability.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.cdc.wal-logical-decoding-slot`, chạy lại từ môi trường sạch với versions và seed đã khóa. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Inside the transaction log - WAL, logical decoding and the replication slot` công bố.

**Bằng chứng cần giữ.** Đối với probe 15 của `Inside the transaction log - WAL, logical decoding and the replication slot`, canonical result phải ổn định hoặc mọi nondeterminism phải được giải thích. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

## 8. Quy trình phản biện

1. Viết consumer-visible invariant cho `Inside the transaction log - WAL, logical decoding and the replication slot` trước khi chọn query hoặc tool.
2. Khóa grain, identity, population, time window và authoritative source.
3. Phân biệt declared configuration, executed state và published state.
4. Chạy negative control, replay hoặc changed-assumption case phù hợp.
5. Đối soát bằng oracle độc lập; công bố coverage và phần không quan sát được.
6. Gắn owner, hành động, reversal trigger và hạn review cho kết luận.

## 9. Câu hỏi tự kiểm tra

1. `Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `WAL purpose` bằng case 1, cụ thể wal trước hết phục vụ durability/recovery; physical records không mặc nhiên là business change events` thất bại đầu tiên ở boundary nào?
2. Artifact nào mạnh nhất để trả lời `Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `Replication slot` bằng case 3, cụ thể slot giữ restart position và ngăn wal cần thiết bị recycle, đổi reliability lấy source disk liability`?
3. Counterexample nhỏ nhất cho `Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `Inspection lab` bằng case 6, cụ thể create slot/publication, mutate/rollback rows, consume changes and compare lsn, transaction, keys and source wal retention` gồm những state nào?
4. `Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `Replication slot` bằng case 9, cụ thể slot giữ restart position và ngăn wal cần thiết bị recycle, đổi reliability lấy source disk liability` có thể xanh giả ra sao?
5. Constraint nào khiến quyết định ở `Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `Logical decoding` bằng case 14, cụ thể decoder reconstructs logical changes từ wal với transaction boundaries và plugin format dưới source/version rules` phải đảo?
6. Phần nào của `Inside the transaction log - WAL, logical decoding and the replication slot: kiểm `Replication slot` bằng case 15, cụ thể slot giữ restart position và ngăn wal cần thiết bị recycle, đổi reliability lấy source disk liability` mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `Inside the transaction log - WAL, logical decoding and the replication slot` chưa chạy trên hệ thống production; nội dung là giáo trình và expected evidence.
- Hành vi phụ thuộc phiên bản, connector, scheduler, warehouse và catalog configuration phải được kiểm lại.
- Các ma trận, ladder và threshold do giáo trình tổng hợp không được gán nguyên văn cho vendor.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-POSTGRESQL-LOGICAL-DECODING]]
2. [[SRC-DEBEZIUM-POSTGRESQL]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-POSTGRESQL-LOGICAL-DECODING]] | Contract hoặc cơ chế liên quan trực tiếp tới `Inside the transaction log - WAL, logical decoding and the replication slot` | Đã đọc locator; cần pin version khi chạy lab |
| [[SRC-DEBEZIUM-POSTGRESQL]] | Contract hoặc cơ chế liên quan trực tiếp tới `Inside the transaction log - WAL, logical decoding and the replication slot` | Đã đọc locator; cần pin version khi chạy lab |

## Key takeaways
- Slot makes logical decoding resumable but can retain WAL and threaten source disk.
- Với `wiki.cdc.wal-logical-decoding-slot`, quality của kết luận phụ thuộc identity, coverage và oracle chứ không phụ thuộc màu dashboard.
- Câu hỏi `WAL, logical decoding, output plugin và replication slot phối hợp để CDC đọc committed changes thế nào?` chỉ được trả lời trong scope và version đã ghi.
- Các source IDs `src.web.postgresql-logical-decoding, src.web.debezium-postgresql` đặt ranh giới cho source fact; phần còn lại là synthesis có nhãn.
- Trước khi lab chạy, đây là note đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.
