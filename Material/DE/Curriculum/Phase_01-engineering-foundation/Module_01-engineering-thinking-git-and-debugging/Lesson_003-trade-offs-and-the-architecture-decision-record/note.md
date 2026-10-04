# Phase 1: Engineering Foundation
# Module 1: Engineering Thinking, Git and Debugging
# Lesson 3: Trade-offs and the architecture decision record

## Mục tiêu bài học

**Năng lực cần chứng minh.** Viết một tài liệu quyết định đủ năm phần cho một lựa chọn thật, và người không dự buổi quyết định đọc hiểu được lý do.

**Điều kiện hoàn thành.** Tài liệu đủ năm phần và dưới hai trang, người rà soát không còn câu hỏi về lý do, và điều kiện xem lại nêu được mốc kiểm được.


# Trade-offs and the architecture decision record

> [!abstract] Câu hỏi trung tâm
> Làm sao ghi một quyết định kỹ thuật để người đến sau hiểu constraint, phương án bị loại và thời điểm cần xét lại?

## 1. ADR lưu reasoning, không chỉ lưu kết luận

Dòng chọn Parquet không giải thích workload, consumers hay constraint. ADR phải giữ context tại thời điểm quyết định để người đọc phân biệt quyết định sai với constraint đã đổi. Nếu chỉ còn kết luận, đội sau thường lặp lại tranh luận cũ hoặc áp lựa chọn vào bối cảnh khác.

Một ADR ngắn vẫn cần status, context, decision drivers, options, outcome, consequences và confirmation. Độ dài dưới hai trang buộc người viết chọn evidence quyết định thay vì chép toàn bộ cuộc họp.

## 2. Khóa tiêu chí trước khi so phương án

Nếu tiêu chí xuất hiện sau lựa chọn, bảng so sánh dễ trở thành biện minh. Hãy nêu trước population, volume, latency, compatibility, operability, cost và reversibility. Mỗi tiêu chí cần unit hoặc ordinal rule đủ rõ để reviewer phản bác.

Không phải mọi tiêu chí có trọng số bằng nhau. Correctness và compliance có thể là hard constraint; cost là biến tối ưu sau khi qua gate. Gộp chúng thành một điểm tổng duy nhất có thể che việc phương án thắng nhờ bù một vi phạm không được phép.

> [!synthesis]
> Phần này ghép contract của roadmap DE-L003 với các lát nguồn đã khai báo. Mọi threshold và tình huống cụ thể là thiết kế giáo trình, không phải lời trích nguyên văn của tác giả.

## 3. Phương án bị loại là tài sản

Ít nhất hai phương án thực phải được mô tả trong điều kiện tốt nhất của chúng. Strawman làm ADR trông chắc chắn nhưng không giúp quyết định. Với mỗi option, ghi lợi ích, chi phí, failure mode và evidence nào có thể đảo đánh giá.

Phương án không làm gì hoặc trì hoãn cũng là option nếu nó hợp lệ. Nó làm lộ cost of change và urgency. Tuy nhiên, không dùng nó để né quyết định khi risk đang tích lũy; consequence phải ghi cả chi phí của việc chờ.

## 4. Consequence gồm cả khoản nợ được chấp nhận

Mỗi quyết định tạo thuận lợi và giới hạn. Chọn CSV tăng interoperability nhưng làm schema và type ambiguity khó kiểm soát; chọn Parquet giảm scan cost nhưng tăng yêu cầu reader compatibility và inspection tooling. ADR phải ghi phần xấu bằng ngôn ngữ vận hành.

Consequence cần owner và hành động khi có thể: ai giữ compatibility suite, ai theo dõi file size, ai chịu migration. Nếu không có owner, consequence chỉ là lời cảnh báo không tạo thay đổi hành vi.

## 5. Reversibility và option value

Quyết định dễ rollback nên được timebox để học nhanh. Quyết định thay identifier, public schema hoặc storage layout khó đảo cần evidence và migration path mạnh hơn. Reversibility không phải nhãn yes/no; nó gồm thời gian, dữ liệu phải chuyển, số consumer và khả năng dual-run.

Một spike có giá trị khi giảm uncertainty quyết định. Nó phải nêu hypothesis, fixture, expected discriminating observation và stop condition. Demo thành công nhưng không phân biệt hai options thì không tạo evidence cho ADR.

## 6. Revisit signal phải kiểm được

Xem lại khi cần không phải signal. Signal tốt có metric hoặc sự kiện: median file vượt 1 GB, có consumer cần random row update, scan cost vượt ngưỡng hoặc library mất support. Khi signal xảy ra, ADR chuyển sang review chứ không tự động đảo quyết định.

ADR mới supersede ADR cũ thay vì sửa lịch sử như chưa từng có lựa chọn trước. Chuỗi quyết định giúp thấy constraint tiến hóa và tránh gán logic mới cho evidence cũ.

## 7. Tình huống xuyên suốt

Hai đội trao đổi 200 GB sự kiện mỗi ngày. Nhóm so CSV, JSON và Parquet theo schema enforcement, interoperability, scan pattern, compression và debugging. Parquet thắng cho batch analytics; CSV giữ làm export nhỏ cho đối tác. ADR ghi reader compatibility suite, ngưỡng file nhỏ cần compaction và signal xét lại nếu workload chuyển sang point update.

Tình huống của `wiki.engineering-foundation.adr-trade-offs` phải được chạy trong sandbox hoặc fixture có version. Nếu chưa chạy, các kết quả mong đợi chỉ là protocol đánh giá; không được ghi thành observation. Người học giữ input, command, state trước-sau, raw output và một oracle độc lập đủ để reviewer tái hiện câu hỏi riêng của bài `Trade-offs and the architecture decision record`.

## 8. Failure modes và ngộ nhận

- **Failure mode.** Chọn phương án trước rồi mới tạo tiêu chí. Cần đưa một counterexample nhỏ nhất để chứng minh hậu quả, sau đó ghi owner và cách phục hồi thay vì chỉ sửa câu chữ.

- **Failure mode.** Chỉ ghi mặt tốt của lựa chọn thắng. Cần đưa một counterexample nhỏ nhất để chứng minh hậu quả, sau đó ghi owner và cách phục hồi thay vì chỉ sửa câu chữ.

- **Failure mode.** Dùng option giả yếu để tránh phản biện. Cần đưa một counterexample nhỏ nhất để chứng minh hậu quả, sau đó ghi owner và cách phục hồi thay vì chỉ sửa câu chữ.

- **Failure mode.** Không có revisit signal hoặc confirmation test. Cần đưa một counterexample nhỏ nhất để chứng minh hậu quả, sau đó ghi owner và cách phục hồi thay vì chỉ sửa câu chữ.

## 9. Ma trận kiểm chứng

Mỗi probe dưới đây bắt đầu bằng dự đoán viết trước. Kết quả đạt chỉ được ghi khi artifact thực tế khớp oracle; exit code thành công không thay thế kiểm tra semantics.

### 9.1. Reviewer tái tạo được recommendation từ drivers và evidence.

**Mệnh đề.** Reviewer tái tạo được recommendation từ drivers và evidence.

**Thiết kế phép thử.** Tạo positive control và một boundary hoặc changed-constraint case chỉ khác đúng biến cần kiểm. Khóa fixture, phiên bản, identity và state ban đầu; ghi expected result trước khi chạy.

**Bằng chứng.** Giữ command, raw output, state transition và reconciliation với oracle không dùng chung assumption. Nếu evidence không phân biệt được mệnh đề đúng và sai, probe chưa có giá trị quyết định.

### 9.2. Changed constraint đủ lớn làm recommendation đảo theo rule đã ghi.

**Mệnh đề.** Changed constraint đủ lớn làm recommendation đảo theo rule đã ghi.

**Thiết kế phép thử.** Tạo positive control và một boundary hoặc changed-constraint case chỉ khác đúng biến cần kiểm. Khóa fixture, phiên bản, identity và state ban đầu; ghi expected result trước khi chạy.

**Bằng chứng.** Giữ command, raw output, state transition và reconciliation với oracle không dùng chung assumption. Nếu evidence không phân biệt được mệnh đề đúng và sai, probe chưa có giá trị quyết định.

### 9.3. Mỗi option có ít nhất một failure mode thật.

**Mệnh đề.** Mỗi option có ít nhất một failure mode thật.

**Thiết kế phép thử.** Tạo positive control và một boundary hoặc changed-constraint case chỉ khác đúng biến cần kiểm. Khóa fixture, phiên bản, identity và state ban đầu; ghi expected result trước khi chạy.

**Bằng chứng.** Giữ command, raw output, state transition và reconciliation với oracle không dùng chung assumption. Nếu evidence không phân biệt được mệnh đề đúng và sai, probe chưa có giá trị quyết định.

### 9.4. Consequence có owner hoặc được đánh dấu risk được chấp nhận.

**Mệnh đề.** Consequence có owner hoặc được đánh dấu risk được chấp nhận.

**Thiết kế phép thử.** Tạo positive control và một boundary hoặc changed-constraint case chỉ khác đúng biến cần kiểm. Khóa fixture, phiên bản, identity và state ban đầu; ghi expected result trước khi chạy.

**Bằng chứng.** Giữ command, raw output, state transition và reconciliation với oracle không dùng chung assumption. Nếu evidence không phân biệt được mệnh đề đúng và sai, probe chưa có giá trị quyết định.

### 9.5. Spike phân biệt hai option thay vì chỉ chứng minh một demo chạy.

**Mệnh đề.** Spike phân biệt hai option thay vì chỉ chứng minh một demo chạy.

**Thiết kế phép thử.** Tạo positive control và một boundary hoặc changed-constraint case chỉ khác đúng biến cần kiểm. Khóa fixture, phiên bản, identity và state ban đầu; ghi expected result trước khi chạy.

**Bằng chứng.** Giữ command, raw output, state transition và reconciliation với oracle không dùng chung assumption. Nếu evidence không phân biệt được mệnh đề đúng và sai, probe chưa có giá trị quyết định.

### 9.6. ADR mới supersede bản cũ mà giữ nguyên lịch sử.

**Mệnh đề.** ADR mới supersede bản cũ mà giữ nguyên lịch sử.

**Thiết kế phép thử.** Tạo positive control và một boundary hoặc changed-constraint case chỉ khác đúng biến cần kiểm. Khóa fixture, phiên bản, identity và state ban đầu; ghi expected result trước khi chạy.

**Bằng chứng.** Giữ command, raw output, state transition và reconciliation với oracle không dùng chung assumption. Nếu evidence không phân biệt được mệnh đề đúng và sai, probe chưa có giá trị quyết định.

## 10. Câu hỏi tự kiểm tra

1. Boundary nào làm mệnh đề trung tâm không còn đúng?
2. Artifact nào là nguồn thẩm quyền và artifact nào chỉ là tín hiệu?
3. Counterexample nhỏ nhất cần những state nào?
4. Một kiểm tra xanh giả có thể xuất hiện theo đường nào?
5. Constraint nào khiến quyết định phải đảo?
6. Phần nào hiện mới là protocol, chưa phải observation?

## 11. Giới hạn và điều chưa cho phép kết luận

- Nội dung là giáo trình và expected evidence; không tuyên bố đã kiểm chứng trên production.
- Hành vi phụ thuộc phiên bản phải được chạy lại với version ghi trong evidence package.
- Threshold, case study và decision rule tổng hợp cho curriculum không được gán nguyên văn cho nguồn.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-MADR-TEMPLATES]]
2. [[SRC-HUNT-THOMAS-PRAGMATIC-PROGRAMMER-20AE]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-MADR-TEMPLATES]]: `src.web.madr-templates` | ADR core và MADR additions; accessed 2026-10-01 | context, drivers, options, decision, consequences và confirmation | §§1-9 | Đã phủ | Nội dung ngoài objective DE-L003 |
| [[SRC-HUNT-THOMAS-PRAGMATIC-PROGRAMMER-20AE]]: `src.book.hunt-thomas-pragmatic-programmer.20ae` | Topic 10 PDF 76-83 | orthogonality, change isolation và decision discipline | §§1-9 | Đã phủ | Nội dung ngoài objective DE-L003 |

## Key takeaways
- ADR tốt làm reasoning có thể kiểm tra lại; nó không biến lựa chọn phụ thuộc bối cảnh thành chân lý lâu dài.
- Một kết luận chỉ có giá trị trong scope, version và state đã ghi.
- Counterexample và changed-constraint test mạnh hơn việc lặp lại định nghĩa.
- Trước khi lab chạy, note này đã có provenance và protocol nhưng chưa phải chứng nhận production.

## References

- [[wiki.engineering-foundation.adr-trade-offs|Trade-offs and the architecture decision record]]
