---
note_id: wiki.data-quality.reconciliation-ladder
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
primary_question: Bảy mức reconciliation tăng độ mạnh từ presence tới record semantics như thế nào?
source_ids:
  - src.web.gx-data-quality-use-cases
  - src.web.gx-expectations
aliases: [The reconciliation ladder - seven levels]
tags: [wiki/data-quality, data-quality, reliability, testing, incidents]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/172-the-reconciliation-ladder-seven-levels.md
relationships:
  builds_on: [wiki.data-quality.backtesting-known-incidents]
  prerequisite_of: [wiki.data-quality.normalization-before-comparison]
  related_to: []

---
# The reconciliation ladder - seven levels

> [!abstract] Câu hỏi trung tâm
> Bảy mức reconciliation tăng độ mạnh từ presence tới record semantics như thế nào?

## 1. Presence and manifest

Mức đầu xác nhận object/partition/file expected có mặt, size/checksum envelope hợp lệ; chưa nói nội dung đúng. Đừng bắt đầu bằng tên công cụ. Hãy bắt đầu bằng đối tượng được bảo vệ, boundary quan sát được và hậu quả nếu kết luận sai. Trong bài `The reconciliation ladder - seven levels`, câu hỏi thực dụng là: Bảy mức reconciliation tăng độ mạnh từ presence tới record semantics như thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 2. Counts

Row/event counts theo partition và status phát hiện loss/gain nhưng không thấy bù trừ. Điểm khó không nằm ở cú pháp mà ở identity và scope. Hai phép đo cùng tên vẫn có thể nói về hai population hoặc hai thời điểm khác nhau. Trong bài `The reconciliation ladder - seven levels`, câu hỏi thực dụng là: Bảy mức reconciliation tăng độ mạnh từ presence tới record semantics như thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 3. Control totals

Sum/min/max/distinct theo dimensions tăng sensitivity nhưng type, currency và null policy phải đồng nhất. Một dashboard xanh chỉ là tín hiệu. Muốn biến nó thành bằng chứng phải giữ input, phiên bản, rule, trạng thái trước-sau và cách tính độc lập. Trong bài `The reconciliation ladder - seven levels`, câu hỏi thực dụng là: Bảy mức reconciliation tăng độ mạnh từ presence tới record semantics như thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 4. Key sets

Anti-join và multiset comparison lộ missing, extra và multiplicity; cần normalize identity trước. Thiết kế tốt phải chịu được counterexample. Hãy chủ động tạo case sát boundary, case thiếu dữ liệu và case replay thay vì chỉ chạy happy path. Trong bài `The reconciliation ladder - seven levels`, câu hỏi thực dụng là: Bảy mức reconciliation tăng độ mạnh từ presence tới record semantics như thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 5. Record hashes

Typed canonical row hash phát hiện value drift, nhưng ordering, null và floating normalization phải cố định. Chi phí vận hành thuộc contract. Một rule đúng nhưng quá đắt, quá ồn hoặc không có owner sẽ nhanh chóng bị tắt và mất tác dụng. Trong bài `The reconciliation ladder - seven levels`, câu hỏi thực dụng là: Bảy mức reconciliation tăng độ mạnh từ presence tới record semantics như thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 6. Business invariants and sampling

Cấp cao nhất nối ledger/domain invariant với drill-down; sampling chỉ bổ sung, không thay population proof. Kết luận cần có điều kiện đảo chiều. Khi volume, latency, nguồn thẩm quyền hoặc topology đổi, quyết định cũ phải được xem xét lại bằng cùng một oracle. Trong bài `The reconciliation ladder - seven levels`, câu hỏi thực dụng là: Bảy mức reconciliation tăng độ mạnh từ presence tới record semantics như thế nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 7. Ma trận kiểm chứng từng mệnh đề

Với `wiki.data-quality.reconciliation-ladder`, command thành công không tự chứng minh dữ liệu đúng. Protocol riêng của bài là: Chạy fixture gốc và biến đổi/đối chiếu độc lập, giữ seed hoặc canonicalization version và chứng minh ít nhất một negative case bị bắt. Mỗi probe dưới đây phải nối input boundary với failure signal và oracle có thể phản bác kết luận.

### 7.1. The reconciliation ladder - seven levels: kiểm `Presence and manifest` bằng case 1, cụ thể mức đầu xác nhận object/partition/file expected có mặt, size/checksum envelope hợp lệ; chưa nói nội dung đúng

**Mệnh đề cần kiểm.** The reconciliation ladder - seven levels: kiểm `Presence and manifest` bằng case 1, cụ thể mức đầu xác nhận object/partition/file expected có mặt, size/checksum envelope hợp lệ; chưa nói nội dung đúng.

**Thiết kế phép thử cho `wiki.data-quality.reconciliation-ladder`.** Trong ngữ cảnh `wiki.data-quality.reconciliation-ladder`, tạo positive control và negative control chỉ khác đúng một điều kiện. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The reconciliation ladder - seven levels` công bố.

**Bằng chứng cần giữ.** Đối với probe 1 của `The reconciliation ladder - seven levels`, giữ fixture, raw failing rows và lệnh tái hiện. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.2. The reconciliation ladder - seven levels: kiểm `Counts` bằng case 2, cụ thể row/event counts theo partition và status phát hiện loss/gain nhưng không thấy bù trừ

**Mệnh đề cần kiểm.** The reconciliation ladder - seven levels: kiểm `Counts` bằng case 2, cụ thể row/event counts theo partition và status phát hiện loss/gain nhưng không thấy bù trừ.

**Thiết kế phép thử cho `wiki.data-quality.reconciliation-ladder`.** Trong ngữ cảnh `wiki.data-quality.reconciliation-ladder`, đổi grain nhưng giữ tổng số dòng để lộ phép đo sai cấp. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The reconciliation ladder - seven levels` công bố.

**Bằng chứng cần giữ.** Đối với probe 2 của `The reconciliation ladder - seven levels`, báo numerator, denominator và key set ở cả hai grain. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.3. The reconciliation ladder - seven levels: kiểm `Control totals` bằng case 3, cụ thể sum/min/max/distinct theo dimensions tăng sensitivity nhưng type, currency và null policy phải đồng nhất

**Mệnh đề cần kiểm.** The reconciliation ladder - seven levels: kiểm `Control totals` bằng case 3, cụ thể sum/min/max/distinct theo dimensions tăng sensitivity nhưng type, currency và null policy phải đồng nhất.

**Thiết kế phép thử cho `wiki.data-quality.reconciliation-ladder`.** Trong ngữ cảnh `wiki.data-quality.reconciliation-ladder`, đưa một giá trị tới đúng boundary và một giá trị vượt boundary. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The reconciliation ladder - seven levels` công bố.

**Bằng chứng cần giữ.** Đối với probe 3 của `The reconciliation ladder - seven levels`, lưu hai observed values cùng rule đã resolve. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.4. The reconciliation ladder - seven levels: kiểm `Key sets` bằng case 4, cụ thể anti-join và multiset comparison lộ missing, extra và multiplicity; cần normalize identity trước

**Mệnh đề cần kiểm.** The reconciliation ladder - seven levels: kiểm `Key sets` bằng case 4, cụ thể anti-join và multiset comparison lộ missing, extra và multiplicity; cần normalize identity trước.

**Thiết kế phép thử cho `wiki.data-quality.reconciliation-ladder`.** Trong ngữ cảnh `wiki.data-quality.reconciliation-ladder`, kill tiến trình ngay trước rồi ngay sau durable side effect. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The reconciliation ladder - seven levels` công bố.

**Bằng chứng cần giữ.** Đối với probe 4 của `The reconciliation ladder - seven levels`, lưu checkpoint, external ledger và trạng thái sau restart. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.5. The reconciliation ladder - seven levels: kiểm `Record hashes` bằng case 5, cụ thể typed canonical row hash phát hiện value drift, nhưng ordering, null và floating normalization phải cố định

**Mệnh đề cần kiểm.** The reconciliation ladder - seven levels: kiểm `Record hashes` bằng case 5, cụ thể typed canonical row hash phát hiện value drift, nhưng ordering, null và floating normalization phải cố định.

**Thiết kế phép thử cho `wiki.data-quality.reconciliation-ladder`.** Trong ngữ cảnh `wiki.data-quality.reconciliation-ladder`, đảo thứ tự input và concurrency nhưng giữ logical population. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The reconciliation ladder - seven levels` công bố.

**Bằng chứng cần giữ.** Đối với probe 5 của `The reconciliation ladder - seven levels`, so canonical hash và business totals giữa các thứ tự. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.6. The reconciliation ladder - seven levels: kiểm `Business invariants and sampling` bằng case 6, cụ thể cấp cao nhất nối ledger/domain invariant với drill-down; sampling chỉ bổ sung, không thay population proof

**Mệnh đề cần kiểm.** The reconciliation ladder - seven levels: kiểm `Business invariants and sampling` bằng case 6, cụ thể cấp cao nhất nối ledger/domain invariant với drill-down; sampling chỉ bổ sung, không thay population proof.

**Thiết kế phép thử cho `wiki.data-quality.reconciliation-ladder`.** Trong ngữ cảnh `wiki.data-quality.reconciliation-ladder`, replay cùng identity với payload giống rồi payload xung đột. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The reconciliation ladder - seven levels` công bố.

**Bằng chứng cần giữ.** Đối với probe 6 của `The reconciliation ladder - seven levels`, tách duplicate replay khỏi identity collision bằng reason code. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.7. The reconciliation ladder - seven levels: kiểm `Presence and manifest` bằng case 7, cụ thể mức đầu xác nhận object/partition/file expected có mặt, size/checksum envelope hợp lệ; chưa nói nội dung đúng

**Mệnh đề cần kiểm.** The reconciliation ladder - seven levels: kiểm `Presence and manifest` bằng case 7, cụ thể mức đầu xác nhận object/partition/file expected có mặt, size/checksum envelope hợp lệ; chưa nói nội dung đúng.

**Thiết kế phép thử cho `wiki.data-quality.reconciliation-ladder`.** Trong ngữ cảnh `wiki.data-quality.reconciliation-ladder`, thêm record tới trễ trong horizon và ngoài horizon. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The reconciliation ladder - seven levels` công bố.

**Bằng chứng cần giữ.** Đối với probe 7 của `The reconciliation ladder - seven levels`, báo accepted-late, rejected-late và oldest outstanding timestamp. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.8. The reconciliation ladder - seven levels: kiểm `Counts` bằng case 8, cụ thể row/event counts theo partition và status phát hiện loss/gain nhưng không thấy bù trừ

**Mệnh đề cần kiểm.** The reconciliation ladder - seven levels: kiểm `Counts` bằng case 8, cụ thể row/event counts theo partition và status phát hiện loss/gain nhưng không thấy bù trừ.

**Thiết kế phép thử cho `wiki.data-quality.reconciliation-ladder`.** Trong ngữ cảnh `wiki.data-quality.reconciliation-ladder`, đổi schema theo một cách tương thích rồi một cách phá vỡ semantics. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The reconciliation ladder - seven levels` công bố.

**Bằng chứng cần giữ.** Đối với probe 8 của `The reconciliation ladder - seven levels`, giữ schema diff, classification và consumer-visible result. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.9. The reconciliation ladder - seven levels: kiểm `Control totals` bằng case 9, cụ thể sum/min/max/distinct theo dimensions tăng sensitivity nhưng type, currency và null policy phải đồng nhất

**Mệnh đề cần kiểm.** The reconciliation ladder - seven levels: kiểm `Control totals` bằng case 9, cụ thể sum/min/max/distinct theo dimensions tăng sensitivity nhưng type, currency và null policy phải đồng nhất.

**Thiết kế phép thử cho `wiki.data-quality.reconciliation-ladder`.** Trong ngữ cảnh `wiki.data-quality.reconciliation-ladder`, tạo missing và duplicate bù nhau để count tổng không đổi. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The reconciliation ladder - seven levels` công bố.

**Bằng chứng cần giữ.** Đối với probe 9 của `The reconciliation ladder - seven levels`, so key multiset và typed hashes thay vì chỉ row count. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.10. The reconciliation ladder - seven levels: kiểm `Key sets` bằng case 10, cụ thể anti-join và multiset comparison lộ missing, extra và multiplicity; cần normalize identity trước

**Mệnh đề cần kiểm.** The reconciliation ladder - seven levels: kiểm `Key sets` bằng case 10, cụ thể anti-join và multiset comparison lộ missing, extra và multiplicity; cần normalize identity trước.

**Thiết kế phép thử cho `wiki.data-quality.reconciliation-ladder`.** Trong ngữ cảnh `wiki.data-quality.reconciliation-ladder`, cho reviewer tái hiện chỉ từ evidence package. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The reconciliation ladder - seven levels` công bố.

**Bằng chứng cần giữ.** Đối với probe 10 của `The reconciliation ladder - seven levels`, package phải đủ để người khác dựng lại decision và limitation. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.11. The reconciliation ladder - seven levels: kiểm `Record hashes` bằng case 11, cụ thể typed canonical row hash phát hiện value drift, nhưng ordering, null và floating normalization phải cố định

**Mệnh đề cần kiểm.** The reconciliation ladder - seven levels: kiểm `Record hashes` bằng case 11, cụ thể typed canonical row hash phát hiện value drift, nhưng ordering, null và floating normalization phải cố định.

**Thiết kế phép thử cho `wiki.data-quality.reconciliation-ladder`.** Trong ngữ cảnh `wiki.data-quality.reconciliation-ladder`, so với oracle độc lập không dùng chung query hoặc parser. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The reconciliation ladder - seven levels` công bố.

**Bằng chứng cần giữ.** Đối với probe 11 của `The reconciliation ladder - seven levels`, independent result phải khớp ở grain đã công bố. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.12. The reconciliation ladder - seven levels: kiểm `Business invariants and sampling` bằng case 12, cụ thể cấp cao nhất nối ledger/domain invariant với drill-down; sampling chỉ bổ sung, không thay population proof

**Mệnh đề cần kiểm.** The reconciliation ladder - seven levels: kiểm `Business invariants and sampling` bằng case 12, cụ thể cấp cao nhất nối ledger/domain invariant với drill-down; sampling chỉ bổ sung, không thay population proof.

**Thiết kế phép thử cho `wiki.data-quality.reconciliation-ladder`.** Trong ngữ cảnh `wiki.data-quality.reconciliation-ladder`, chạy scope hẹp và population đầy đủ rồi công bố phần bị loại. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The reconciliation ladder - seven levels` công bố.

**Bằng chứng cần giữ.** Đối với probe 12 của `The reconciliation ladder - seven levels`, coverage phải nêu rõ excluded nodes, partitions hoặc incidents. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.13. The reconciliation ladder - seven levels: kiểm `Presence and manifest` bằng case 13, cụ thể mức đầu xác nhận object/partition/file expected có mặt, size/checksum envelope hợp lệ; chưa nói nội dung đúng

**Mệnh đề cần kiểm.** The reconciliation ladder - seven levels: kiểm `Presence and manifest` bằng case 13, cụ thể mức đầu xác nhận object/partition/file expected có mặt, size/checksum envelope hợp lệ; chưa nói nội dung đúng.

**Thiết kế phép thử cho `wiki.data-quality.reconciliation-ladder`.** Trong ngữ cảnh `wiki.data-quality.reconciliation-ladder`, thử timezone, precision hoặc partition ở hai phía của ranh giới. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The reconciliation ladder - seven levels` công bố.

**Bằng chứng cần giữ.** Đối với probe 13 của `The reconciliation ladder - seven levels`, UTC/local interval và rounding policy phải hiện trong output. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.14. The reconciliation ladder - seven levels: kiểm `Counts` bằng case 14, cụ thể row/event counts theo partition và status phát hiện loss/gain nhưng không thấy bù trừ

**Mệnh đề cần kiểm.** The reconciliation ladder - seven levels: kiểm `Counts` bằng case 14, cụ thể row/event counts theo partition và status phát hiện loss/gain nhưng không thấy bù trừ.

**Thiết kế phép thử cho `wiki.data-quality.reconciliation-ladder`.** Trong ngữ cảnh `wiki.data-quality.reconciliation-ladder`, đổi constraint đủ lớn để quyết định phải đảo. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The reconciliation ladder - seven levels` công bố.

**Bằng chứng cần giữ.** Đối với probe 14 của `The reconciliation ladder - seven levels`, ADR phải lưu changed constraint và reversal threshold. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.15. The reconciliation ladder - seven levels: kiểm `Control totals` bằng case 15, cụ thể sum/min/max/distinct theo dimensions tăng sensitivity nhưng type, currency và null policy phải đồng nhất

**Mệnh đề cần kiểm.** The reconciliation ladder - seven levels: kiểm `Control totals` bằng case 15, cụ thể sum/min/max/distinct theo dimensions tăng sensitivity nhưng type, currency và null policy phải đồng nhất.

**Thiết kế phép thử cho `wiki.data-quality.reconciliation-ladder`.** Trong ngữ cảnh `wiki.data-quality.reconciliation-ladder`, chạy lại từ môi trường sạch với versions và seed đã khóa. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The reconciliation ladder - seven levels` công bố.

**Bằng chứng cần giữ.** Đối với probe 15 của `The reconciliation ladder - seven levels`, canonical result phải ổn định hoặc mọi nondeterminism phải được giải thích. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

## 8. Quy trình phản biện

1. Viết consumer-visible invariant cho `The reconciliation ladder - seven levels` trước khi chọn query hoặc tool.
2. Khóa grain, identity, population, time window và authoritative source.
3. Phân biệt declared configuration, executed state và published state.
4. Chạy negative control, replay hoặc changed-assumption case phù hợp.
5. Đối soát bằng oracle độc lập; công bố coverage và phần không quan sát được.
6. Gắn owner, hành động, reversal trigger và hạn review cho kết luận.

## 9. Câu hỏi tự kiểm tra

1. `The reconciliation ladder - seven levels: kiểm `Presence and manifest` bằng case 1, cụ thể mức đầu xác nhận object/partition/file expected có mặt, size/checksum envelope hợp lệ; chưa nói nội dung đúng` thất bại đầu tiên ở boundary nào?
2. Artifact nào mạnh nhất để trả lời `The reconciliation ladder - seven levels: kiểm `Control totals` bằng case 3, cụ thể sum/min/max/distinct theo dimensions tăng sensitivity nhưng type, currency và null policy phải đồng nhất`?
3. Counterexample nhỏ nhất cho `The reconciliation ladder - seven levels: kiểm `Business invariants and sampling` bằng case 6, cụ thể cấp cao nhất nối ledger/domain invariant với drill-down; sampling chỉ bổ sung, không thay population proof` gồm những state nào?
4. `The reconciliation ladder - seven levels: kiểm `Control totals` bằng case 9, cụ thể sum/min/max/distinct theo dimensions tăng sensitivity nhưng type, currency và null policy phải đồng nhất` có thể xanh giả ra sao?
5. Constraint nào khiến quyết định ở `The reconciliation ladder - seven levels: kiểm `Counts` bằng case 14, cụ thể row/event counts theo partition và status phát hiện loss/gain nhưng không thấy bù trừ` phải đảo?
6. Phần nào của `The reconciliation ladder - seven levels: kiểm `Control totals` bằng case 15, cụ thể sum/min/max/distinct theo dimensions tăng sensitivity nhưng type, currency và null policy phải đồng nhất` mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `The reconciliation ladder - seven levels` chưa chạy trên hệ thống production; nội dung là giáo trình và expected evidence.
- Hành vi phụ thuộc phiên bản, connector, scheduler, warehouse và catalog configuration phải được kiểm lại.
- Các ma trận, ladder và threshold do giáo trình tổng hợp không được gán nguyên văn cho vendor.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-GX-DATA-QUALITY-USE-CASES]]
2. [[SRC-GX-EXPECTATIONS]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-GX-DATA-QUALITY-USE-CASES]] | Contract hoặc cơ chế liên quan trực tiếp tới `The reconciliation ladder - seven levels` | Đã đọc locator; cần pin version khi chạy lab |
| [[SRC-GX-EXPECTATIONS]] | Contract hoặc cơ chế liên quan trực tiếp tới `The reconciliation ladder - seven levels` | Đã đọc locator; cần pin version khi chạy lab |

## Key takeaways
- Reconciliation mạnh dần từ presence tới key, record và business invariants.
- Với `wiki.data-quality.reconciliation-ladder`, quality của kết luận phụ thuộc identity, coverage và oracle chứ không phụ thuộc màu dashboard.
- Câu hỏi `Bảy mức reconciliation tăng độ mạnh từ presence tới record semantics như thế nào?` chỉ được trả lời trong scope và version đã ghi.
- Các source IDs `src.web.gx-data-quality-use-cases, src.web.gx-expectations` đặt ranh giới cho source fact; phần còn lại là synthesis có nhãn.
- Trước khi lab chạy, đây là note đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule: kiểm chứng `wiki.data-quality.reconciliation-ladder`

> [!important] Phân loại mệnh đề
> Với `wiki.data-quality.reconciliation-ladder`, sơ đồ, ví dụ và artifact về **The reconciliation ladder - seven levels** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.web.gx-data-quality-use-cases"] --> B["Khóa boundary"]
    B --> M["Cơ chế: The reconciliation ladder - seven levels"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.data-quality.reconciliation-ladder` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **The reconciliation ladder - seven levels**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```sql
-- Verification harness for: The reconciliation ladder - seven levels
WITH evidence AS (
    SELECT 'wiki.data-quality.reconciliation-ladder' AS concept_id,
           'boundary_declared' AS check_name, 1 AS passed
    UNION ALL
    SELECT 'wiki.data-quality.reconciliation-ladder', 'independent_oracle', 1
    UNION ALL
    SELECT 'wiki.data-quality.reconciliation-ladder', 'reversal_trigger_recorded', 1
)
SELECT concept_id,
       MIN(passed) AS all_hard_checks_pass,
       COUNT(*) AS evidence_items
FROM evidence
GROUP BY concept_id
HAVING MIN(passed) = 1;
```

Artifact của `wiki.data-quality.reconciliation-ladder` buộc người dùng ghi boundary, oracle và reversal trigger cho **The reconciliation ladder - seven levels**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

### Tự kiểm tra trước khi tái sử dụng

1. Bạn có thể trả lời `Bảy mức reconciliation tăng độ mạnh từ presence tới record semantics như thế nào?` bằng một câu mà không kéo thêm concept thứ hai không?
2. Source locator nào đỡ cho claim, và phần nào chỉ là synthesis trong note?
3. Observation nào khiến bạn dừng, thu hẹp hoặc đảo quyết định?
4. Artifact nào cho phép một reviewer độc lập tái hiện kết quả?

<!-- ATOMIC-EXECUTION-CAPSULE:END -->
