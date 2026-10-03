# Phase 8: Distributed Systems, Streaming and Compute
# Module 21: Kafka and Event Streaming
# Lesson 333: Security, quota and multi-tenancy

## Mục tiêu bài học

**Năng lực cần chứng minh.** Cài xác thực, phân quyền và hạn mức, rồi chứng minh một bên đọc lại không làm vỡ cam kết của bên khác.

**Điều kiện hoàn thành.** Phép thử phủ định bị chặn hết, độ trễ của đội không liên quan giữ trong cam kết suốt lần đọc lại, và xoay thông tin xác thực không gây gián đoạn.

> [!abstract] Câu hỏi trung tâm
> Authentication, authorization, encryption, quotas và namespace isolation tạo multi-tenant boundary thế nào?

## 1. Identity and transport

Broker/client identity, TLS endpoint verification và credential lifecycle phải rõ ở mọi listener. Đừng bắt đầu bằng tên công cụ. Hãy bắt đầu bằng đối tượng được bảo vệ, boundary quan sát được và hậu quả nếu kết luận sai. Trong bài `Security, quota and multi-tenancy`, câu hỏi thực dụng là: Authentication, authorization, encryption, quotas và namespace isolation tạo multi-tenant boundary thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 2. Authorization

ACL/policy theo cluster, topic, group, transactional ID và admin operation; deny test quan trọng như allow test. Điểm khó không nằm ở cú pháp mà ở identity và scope. Hai phép đo cùng tên vẫn có thể nói về hai population hoặc hai thời điểm khác nhau. Trong bài `Security, quota and multi-tenancy`, câu hỏi thực dụng là: Authentication, authorization, encryption, quotas và namespace isolation tạo multi-tenant boundary thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 3. Quotas

Producer/consumer bandwidth, request rate và controller/admin protections giới hạn noisy neighbor nhưng throttling metrics phải visible. Một dashboard xanh chỉ là tín hiệu. Muốn biến nó thành bằng chứng phải giữ input, phiên bản, rule, trạng thái trước–sau và cách tính độc lập. Trong bài `Security, quota and multi-tenancy`, câu hỏi thực dụng là: Authentication, authorization, encryption, quotas và namespace isolation tạo multi-tenant boundary thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 4. Namespace isolation

Topic/group/transactional IDs, schema subjects và service accounts cần ownership/naming để tenant không collision. Thiết kế tốt phải chịu được counterexample. Hãy chủ động tạo case sát boundary, case thiếu dữ liệu và case replay thay vì chỉ chạy happy path. Trong bài `Security, quota and multi-tenancy`, câu hỏi thực dụng là: Authentication, authorization, encryption, quotas và namespace isolation tạo multi-tenant boundary thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 5. Data protection

Encryption in transit/at rest, secret handling và sensitive payload policy không được giao mặc định cho broker. Chi phí vận hành thuộc contract. Một rule đúng nhưng quá đắt, quá ồn hoặc không có owner sẽ nhanh chóng bị tắt và mất tác dụng. Trong bài `Security, quota and multi-tenancy`, câu hỏi thực dụng là: Authentication, authorization, encryption, quotas và namespace isolation tạo multi-tenant boundary thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 6. Abuse test

Tenant vượt quota, đo throttling/latency của neighbor, thử unauthorized consume/alter và verify audit without leaking payload. Kết luận cần có điều kiện đảo chiều. Khi volume, latency, nguồn thẩm quyền hoặc topology đổi, quyết định cũ phải được xem xét lại bằng cùng một oracle. Trong bài `Security, quota and multi-tenancy`, câu hỏi thực dụng là: Authentication, authorization, encryption, quotas và namespace isolation tạo multi-tenant boundary thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 7. Ma trận kiểm chứng từng mệnh đề

Với `wiki.streaming.kafka-security-quota-tenancy`, command thành công không tự chứng minh dữ liệu đúng. Protocol riêng của bài là: Dựng version-pinned fixture, inject compatibility/capacity/failure/change case và đối soát emitted/visible state bằng oracle độc lập. Mỗi probe dưới đây phải nối input boundary với failure signal và oracle có thể phản bác kết luận.

### 7.1. Security, quota and multi-tenancy: kiểm `Identity and transport` bằng case 1, cụ thể broker/client identity, tls endpoint verification và credential lifecycle phải rõ ở mọi listener

**Mệnh đề cần kiểm.** Security, quota and multi-tenancy: kiểm `Identity and transport` bằng case 1, cụ thể broker/client identity, tls endpoint verification và credential lifecycle phải rõ ở mọi listener.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-security-quota-tenancy`, tạo positive control và negative control chỉ khác đúng một điều kiện. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Security, quota and multi-tenancy` công bố.

**Bằng chứng cần giữ.** Đối với probe 1 của `Security, quota and multi-tenancy`, giữ fixture, raw failing rows và lệnh tái hiện. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.2. Security, quota and multi-tenancy: kiểm `Authorization` bằng case 2, cụ thể acl/policy theo cluster, topic, group, transactional id và admin operation; deny test quan trọng như allow test

**Mệnh đề cần kiểm.** Security, quota and multi-tenancy: kiểm `Authorization` bằng case 2, cụ thể acl/policy theo cluster, topic, group, transactional id và admin operation; deny test quan trọng như allow test.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-security-quota-tenancy`, đổi grain nhưng giữ tổng số dòng để lộ phép đo sai cấp. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Security, quota and multi-tenancy` công bố.

**Bằng chứng cần giữ.** Đối với probe 2 của `Security, quota and multi-tenancy`, báo numerator, denominator và key set ở cả hai grain. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.3. Security, quota and multi-tenancy: kiểm `Quotas` bằng case 3, cụ thể producer/consumer bandwidth, request rate và controller/admin protections giới hạn noisy neighbor nhưng throttling metrics phải visible

**Mệnh đề cần kiểm.** Security, quota and multi-tenancy: kiểm `Quotas` bằng case 3, cụ thể producer/consumer bandwidth, request rate và controller/admin protections giới hạn noisy neighbor nhưng throttling metrics phải visible.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-security-quota-tenancy`, đưa một giá trị tới đúng boundary và một giá trị vượt boundary. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Security, quota and multi-tenancy` công bố.

**Bằng chứng cần giữ.** Đối với probe 3 của `Security, quota and multi-tenancy`, lưu hai observed values cùng rule đã resolve. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.4. Security, quota and multi-tenancy: kiểm `Namespace isolation` bằng case 4, cụ thể topic/group/transactional ids, schema subjects và service accounts cần ownership/naming để tenant không collision

**Mệnh đề cần kiểm.** Security, quota and multi-tenancy: kiểm `Namespace isolation` bằng case 4, cụ thể topic/group/transactional ids, schema subjects và service accounts cần ownership/naming để tenant không collision.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-security-quota-tenancy`, kill tiến trình ngay trước rồi ngay sau durable side effect. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Security, quota and multi-tenancy` công bố.

**Bằng chứng cần giữ.** Đối với probe 4 của `Security, quota and multi-tenancy`, lưu checkpoint, external ledger và trạng thái sau restart. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.5. Security, quota and multi-tenancy: kiểm `Data protection` bằng case 5, cụ thể encryption in transit/at rest, secret handling và sensitive payload policy không được giao mặc định cho broker

**Mệnh đề cần kiểm.** Security, quota and multi-tenancy: kiểm `Data protection` bằng case 5, cụ thể encryption in transit/at rest, secret handling và sensitive payload policy không được giao mặc định cho broker.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-security-quota-tenancy`, đảo thứ tự input và concurrency nhưng giữ logical population. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Security, quota and multi-tenancy` công bố.

**Bằng chứng cần giữ.** Đối với probe 5 của `Security, quota and multi-tenancy`, so canonical hash và business totals giữa các thứ tự. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.6. Security, quota and multi-tenancy: kiểm `Abuse test` bằng case 6, cụ thể tenant vượt quota, đo throttling/latency của neighbor, thử unauthorized consume/alter và verify audit without leaking payload

**Mệnh đề cần kiểm.** Security, quota and multi-tenancy: kiểm `Abuse test` bằng case 6, cụ thể tenant vượt quota, đo throttling/latency của neighbor, thử unauthorized consume/alter và verify audit without leaking payload.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-security-quota-tenancy`, replay cùng identity với payload giống rồi payload xung đột. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Security, quota and multi-tenancy` công bố.

**Bằng chứng cần giữ.** Đối với probe 6 của `Security, quota and multi-tenancy`, tách duplicate replay khỏi identity collision bằng reason code. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.7. Security, quota and multi-tenancy: kiểm `Identity and transport` bằng case 7, cụ thể broker/client identity, tls endpoint verification và credential lifecycle phải rõ ở mọi listener

**Mệnh đề cần kiểm.** Security, quota and multi-tenancy: kiểm `Identity and transport` bằng case 7, cụ thể broker/client identity, tls endpoint verification và credential lifecycle phải rõ ở mọi listener.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-security-quota-tenancy`, thêm record tới trễ trong horizon và ngoài horizon. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Security, quota and multi-tenancy` công bố.

**Bằng chứng cần giữ.** Đối với probe 7 của `Security, quota and multi-tenancy`, báo accepted-late, rejected-late và oldest outstanding timestamp. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.8. Security, quota and multi-tenancy: kiểm `Authorization` bằng case 8, cụ thể acl/policy theo cluster, topic, group, transactional id và admin operation; deny test quan trọng như allow test

**Mệnh đề cần kiểm.** Security, quota and multi-tenancy: kiểm `Authorization` bằng case 8, cụ thể acl/policy theo cluster, topic, group, transactional id và admin operation; deny test quan trọng như allow test.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-security-quota-tenancy`, đổi schema theo một cách tương thích rồi một cách phá vỡ semantics. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Security, quota and multi-tenancy` công bố.

**Bằng chứng cần giữ.** Đối với probe 8 của `Security, quota and multi-tenancy`, giữ schema diff, classification và consumer-visible result. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.9. Security, quota and multi-tenancy: kiểm `Quotas` bằng case 9, cụ thể producer/consumer bandwidth, request rate và controller/admin protections giới hạn noisy neighbor nhưng throttling metrics phải visible

**Mệnh đề cần kiểm.** Security, quota and multi-tenancy: kiểm `Quotas` bằng case 9, cụ thể producer/consumer bandwidth, request rate và controller/admin protections giới hạn noisy neighbor nhưng throttling metrics phải visible.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-security-quota-tenancy`, tạo missing và duplicate bù nhau để count tổng không đổi. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Security, quota and multi-tenancy` công bố.

**Bằng chứng cần giữ.** Đối với probe 9 của `Security, quota and multi-tenancy`, so key multiset và typed hashes thay vì chỉ row count. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.10. Security, quota and multi-tenancy: kiểm `Namespace isolation` bằng case 10, cụ thể topic/group/transactional ids, schema subjects và service accounts cần ownership/naming để tenant không collision

**Mệnh đề cần kiểm.** Security, quota and multi-tenancy: kiểm `Namespace isolation` bằng case 10, cụ thể topic/group/transactional ids, schema subjects và service accounts cần ownership/naming để tenant không collision.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-security-quota-tenancy`, cho reviewer tái hiện chỉ từ evidence package. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Security, quota and multi-tenancy` công bố.

**Bằng chứng cần giữ.** Đối với probe 10 của `Security, quota and multi-tenancy`, package phải đủ để người khác dựng lại decision và limitation. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.11. Security, quota and multi-tenancy: kiểm `Data protection` bằng case 11, cụ thể encryption in transit/at rest, secret handling và sensitive payload policy không được giao mặc định cho broker

**Mệnh đề cần kiểm.** Security, quota and multi-tenancy: kiểm `Data protection` bằng case 11, cụ thể encryption in transit/at rest, secret handling và sensitive payload policy không được giao mặc định cho broker.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-security-quota-tenancy`, so với oracle độc lập không dùng chung query hoặc parser. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Security, quota and multi-tenancy` công bố.

**Bằng chứng cần giữ.** Đối với probe 11 của `Security, quota and multi-tenancy`, independent result phải khớp ở grain đã công bố. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.12. Security, quota and multi-tenancy: kiểm `Abuse test` bằng case 12, cụ thể tenant vượt quota, đo throttling/latency của neighbor, thử unauthorized consume/alter và verify audit without leaking payload

**Mệnh đề cần kiểm.** Security, quota and multi-tenancy: kiểm `Abuse test` bằng case 12, cụ thể tenant vượt quota, đo throttling/latency của neighbor, thử unauthorized consume/alter và verify audit without leaking payload.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-security-quota-tenancy`, chạy scope hẹp và population đầy đủ rồi công bố phần bị loại. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Security, quota and multi-tenancy` công bố.

**Bằng chứng cần giữ.** Đối với probe 12 của `Security, quota and multi-tenancy`, coverage phải nêu rõ excluded nodes, partitions hoặc incidents. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.13. Security, quota and multi-tenancy: kiểm `Identity and transport` bằng case 13, cụ thể broker/client identity, tls endpoint verification và credential lifecycle phải rõ ở mọi listener

**Mệnh đề cần kiểm.** Security, quota and multi-tenancy: kiểm `Identity and transport` bằng case 13, cụ thể broker/client identity, tls endpoint verification và credential lifecycle phải rõ ở mọi listener.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-security-quota-tenancy`, thử timezone, precision hoặc partition ở hai phía của ranh giới. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Security, quota and multi-tenancy` công bố.

**Bằng chứng cần giữ.** Đối với probe 13 của `Security, quota and multi-tenancy`, UTC/local interval và rounding policy phải hiện trong output. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.14. Security, quota and multi-tenancy: kiểm `Authorization` bằng case 14, cụ thể acl/policy theo cluster, topic, group, transactional id và admin operation; deny test quan trọng như allow test

**Mệnh đề cần kiểm.** Security, quota and multi-tenancy: kiểm `Authorization` bằng case 14, cụ thể acl/policy theo cluster, topic, group, transactional id và admin operation; deny test quan trọng như allow test.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-security-quota-tenancy`, đổi constraint đủ lớn để quyết định phải đảo. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Security, quota and multi-tenancy` công bố.

**Bằng chứng cần giữ.** Đối với probe 14 của `Security, quota and multi-tenancy`, ADR phải lưu changed constraint và reversal threshold. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.15. Security, quota and multi-tenancy: kiểm `Quotas` bằng case 15, cụ thể producer/consumer bandwidth, request rate và controller/admin protections giới hạn noisy neighbor nhưng throttling metrics phải visible

**Mệnh đề cần kiểm.** Security, quota and multi-tenancy: kiểm `Quotas` bằng case 15, cụ thể producer/consumer bandwidth, request rate và controller/admin protections giới hạn noisy neighbor nhưng throttling metrics phải visible.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.streaming.kafka-security-quota-tenancy`, chạy lại từ môi trường sạch với versions và seed đã khóa. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Security, quota and multi-tenancy` công bố.

**Bằng chứng cần giữ.** Đối với probe 15 của `Security, quota and multi-tenancy`, canonical result phải ổn định hoặc mọi nondeterminism phải được giải thích. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

## 8. Quy trình phản biện

1. Viết consumer-visible invariant cho `Security, quota and multi-tenancy` trước khi chọn query hoặc tool.
2. Khóa grain, identity, population, time window và authoritative source.
3. Phân biệt declared configuration, executed state và published state.
4. Chạy negative control, replay hoặc changed-assumption case phù hợp.
5. Đối soát bằng oracle độc lập; công bố coverage và phần không quan sát được.
6. Gắn owner, hành động, reversal trigger và hạn review cho kết luận.

## 9. Câu hỏi tự kiểm tra

1. `Security, quota and multi-tenancy: kiểm `Identity and transport` bằng case 1, cụ thể broker/client identity, tls endpoint verification và credential lifecycle phải rõ ở mọi listener` thất bại đầu tiên ở boundary nào?
2. Artifact nào mạnh nhất để trả lời `Security, quota and multi-tenancy: kiểm `Quotas` bằng case 3, cụ thể producer/consumer bandwidth, request rate và controller/admin protections giới hạn noisy neighbor nhưng throttling metrics phải visible`?
3. Counterexample nhỏ nhất cho `Security, quota and multi-tenancy: kiểm `Abuse test` bằng case 6, cụ thể tenant vượt quota, đo throttling/latency của neighbor, thử unauthorized consume/alter và verify audit without leaking payload` gồm những state nào?
4. `Security, quota and multi-tenancy: kiểm `Quotas` bằng case 9, cụ thể producer/consumer bandwidth, request rate và controller/admin protections giới hạn noisy neighbor nhưng throttling metrics phải visible` có thể xanh giả ra sao?
5. Constraint nào khiến quyết định ở `Security, quota and multi-tenancy: kiểm `Authorization` bằng case 14, cụ thể acl/policy theo cluster, topic, group, transactional id và admin operation; deny test quan trọng như allow test` phải đảo?
6. Phần nào của `Security, quota and multi-tenancy: kiểm `Quotas` bằng case 15, cụ thể producer/consumer bandwidth, request rate và controller/admin protections giới hạn noisy neighbor nhưng throttling metrics phải visible` mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `Security, quota and multi-tenancy` chưa chạy trên hệ thống production; nội dung là giáo trình và expected evidence.
- Hành vi phụ thuộc phiên bản, connector, scheduler, warehouse và catalog configuration phải được kiểm lại.
- Các ma trận, ladder và threshold do giáo trình tổng hợp không được gán nguyên văn cho vendor.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-APACHE-KAFKA-BROKER-CONFIG]]
2. [[SRC-APACHE-KAFKA-DESIGN]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-APACHE-KAFKA-BROKER-CONFIG]] | Contract hoặc cơ chế liên quan trực tiếp tới `Security, quota and multi-tenancy` | Đã đọc locator; cần pin version khi chạy lab |
| [[SRC-APACHE-KAFKA-DESIGN]] | Contract hoặc cơ chế liên quan trực tiếp tới `Security, quota and multi-tenancy` | Đã đọc locator; cần pin version khi chạy lab |

## Key takeaways
- Multi-tenancy cần identity, authorization, quota và namespace boundaries cùng nhau.
- Với `wiki.streaming.kafka-security-quota-tenancy`, quality của kết luận phụ thuộc identity, coverage và oracle chứ không phụ thuộc màu dashboard.
- Câu hỏi `Authentication, authorization, encryption, quotas và namespace isolation tạo multi-tenant boundary thế nào?` chỉ được trả lời trong scope và version đã ghi.
- Các source IDs `src.web.apache-kafka-broker-config, src.web.apache-kafka-design` đặt ranh giới cho source fact; phần còn lại là synthesis có nhãn.
- Trước khi lab chạy, đây là note đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.
