# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 19: Metadata Engineering, Catalog, Lineage and Governance
# Lesson 298: Lineage levels and what each answers

## Mục tiêu bài học

**Năng lực cần chứng minh.** Chọn mức dòng dõi cho năm câu hỏi thực tế và phân biệt dòng dõi tĩnh với dòng dõi thời gian chạy.

**Điều kiện hoàn thành.** Chọn đúng mức cho ≥ 4/5 câu hỏi kèm chi phí, và hai loại cạnh tĩnh với thời gian chạy được phân biệt bằng ví dụ thật.

> [!abstract] Câu hỏi trung tâm
> Entity, dataset, job, run và field lineage trả lời những câu hỏi khác nhau nào và không được suy vượt cấp ra sao?

## 1. System/entity level

Cho biết platform hoặc asset lớn liên quan, hữu ích discovery nhưng quá thô cho impact kỹ thuật. Đừng bắt đầu bằng tên công cụ. Hãy bắt đầu bằng đối tượng được bảo vệ, boundary quan sát được và hậu quả nếu kết luận sai. Trong bài `Lineage levels and what each answers`, câu hỏi thực dụng là: Entity, dataset, job, run và field lineage trả lời những câu hỏi khác nhau nào và không được suy vượt cấp ra sao? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 2. Dataset level

Nối input/output datasets, trả lời upstream/downstream và blast radius sơ bộ; chưa nói cột hay row nào ảnh hưởng. Điểm khó không nằm ở cú pháp mà ở identity và scope. Hai phép đo cùng tên vẫn có thể nói về hai population hoặc hai thời điểm khác nhau. Trong bài `Lineage levels and what each answers`, câu hỏi thực dụng là: Entity, dataset, job, run và field lineage trả lời những câu hỏi khác nhau nào và không được suy vượt cấp ra sao? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 3. Job level

Đặt transformation/process giữa datasets, hỗ trợ ownership và operational diagnosis. Một dashboard xanh chỉ là tín hiệu. Muốn biến nó thành bằng chứng phải giữ input, phiên bản, rule, trạng thái trước–sau và cách tính độc lập. Trong bài `Lineage levels and what each answers`, câu hỏi thực dụng là: Entity, dataset, job, run và field lineage trả lời những câu hỏi khác nhau nào và không được suy vượt cấp ra sao? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 4. Run level

Gắn dependency với execution, code/version, nominal time và actual inputs; cần cho incident/reproducibility. Thiết kế tốt phải chịu được counterexample. Hãy chủ động tạo case sát boundary, case thiếu dữ liệu và case replay thay vì chỉ chạy happy path. Trong bài `Lineage levels and what each answers`, câu hỏi thực dụng là: Entity, dataset, job, run và field lineage trả lời những câu hỏi khác nhau nào và không được suy vượt cấp ra sao? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 5. Field level

Direct/indirect transformation của columns tăng precision nhưng parser, dynamic SQL và UDF tạo unknowns. Chi phí vận hành thuộc contract. Một rule đúng nhưng quá đắt, quá ồn hoặc không có owner sẽ nhanh chóng bị tắt và mất tác dụng. Trong bài `Lineage levels and what each answers`, câu hỏi thực dụng là: Entity, dataset, job, run và field lineage trả lời những câu hỏi khác nhau nào và không được suy vượt cấp ra sao? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 6. Question-fit rule

Chọn mức nhỏ nhất đủ trả lời câu hỏi; graph sâu hơn không tự chính xác hơn nếu provenance/confidence yếu. Kết luận cần có điều kiện đảo chiều. Khi volume, latency, nguồn thẩm quyền hoặc topology đổi, quyết định cũ phải được xem xét lại bằng cùng một oracle. Trong bài `Lineage levels and what each answers`, câu hỏi thực dụng là: Entity, dataset, job, run và field lineage trả lời những câu hỏi khác nhau nào và không được suy vượt cấp ra sao? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 7. Ma trận kiểm chứng từng mệnh đề

Với `wiki.metadata.lineage-levels`, command thành công không tự chứng minh dữ liệu đúng. Protocol riêng của bài là: Chạy connector/parser/event fixture có expected entity-edge manifest, tiêm partial failure hoặc ambiguity và đo missing/extra/unknown theo producer. Mỗi probe dưới đây phải nối input boundary với failure signal và oracle có thể phản bác kết luận.

### 7.1. Lineage levels and what each answers: kiểm `System/entity level` bằng case 1, cụ thể cho biết platform hoặc asset lớn liên quan, hữu ích discovery nhưng quá thô cho impact kỹ thuật

**Mệnh đề cần kiểm.** Lineage levels and what each answers: kiểm `System/entity level` bằng case 1, cụ thể cho biết platform hoặc asset lớn liên quan, hữu ích discovery nhưng quá thô cho impact kỹ thuật.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.lineage-levels`, tạo positive control và negative control chỉ khác đúng một điều kiện. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Lineage levels and what each answers` công bố.

**Bằng chứng cần giữ.** Đối với probe 1 của `Lineage levels and what each answers`, giữ fixture, raw failing rows và lệnh tái hiện. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.2. Lineage levels and what each answers: kiểm `Dataset level` bằng case 2, cụ thể nối input/output datasets, trả lời upstream/downstream và blast radius sơ bộ; chưa nói cột hay row nào ảnh hưởng

**Mệnh đề cần kiểm.** Lineage levels and what each answers: kiểm `Dataset level` bằng case 2, cụ thể nối input/output datasets, trả lời upstream/downstream và blast radius sơ bộ; chưa nói cột hay row nào ảnh hưởng.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.lineage-levels`, đổi grain nhưng giữ tổng số dòng để lộ phép đo sai cấp. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Lineage levels and what each answers` công bố.

**Bằng chứng cần giữ.** Đối với probe 2 của `Lineage levels and what each answers`, báo numerator, denominator và key set ở cả hai grain. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.3. Lineage levels and what each answers: kiểm `Job level` bằng case 3, cụ thể đặt transformation/process giữa datasets, hỗ trợ ownership và operational diagnosis

**Mệnh đề cần kiểm.** Lineage levels and what each answers: kiểm `Job level` bằng case 3, cụ thể đặt transformation/process giữa datasets, hỗ trợ ownership và operational diagnosis.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.lineage-levels`, đưa một giá trị tới đúng boundary và một giá trị vượt boundary. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Lineage levels and what each answers` công bố.

**Bằng chứng cần giữ.** Đối với probe 3 của `Lineage levels and what each answers`, lưu hai observed values cùng rule đã resolve. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.4. Lineage levels and what each answers: kiểm `Run level` bằng case 4, cụ thể gắn dependency với execution, code/version, nominal time và actual inputs; cần cho incident/reproducibility

**Mệnh đề cần kiểm.** Lineage levels and what each answers: kiểm `Run level` bằng case 4, cụ thể gắn dependency với execution, code/version, nominal time và actual inputs; cần cho incident/reproducibility.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.lineage-levels`, kill tiến trình ngay trước rồi ngay sau durable side effect. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Lineage levels and what each answers` công bố.

**Bằng chứng cần giữ.** Đối với probe 4 của `Lineage levels and what each answers`, lưu checkpoint, external ledger và trạng thái sau restart. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.5. Lineage levels and what each answers: kiểm `Field level` bằng case 5, cụ thể direct/indirect transformation của columns tăng precision nhưng parser, dynamic sql và udf tạo unknowns

**Mệnh đề cần kiểm.** Lineage levels and what each answers: kiểm `Field level` bằng case 5, cụ thể direct/indirect transformation của columns tăng precision nhưng parser, dynamic sql và udf tạo unknowns.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.lineage-levels`, đảo thứ tự input và concurrency nhưng giữ logical population. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Lineage levels and what each answers` công bố.

**Bằng chứng cần giữ.** Đối với probe 5 của `Lineage levels and what each answers`, so canonical hash và business totals giữa các thứ tự. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.6. Lineage levels and what each answers: kiểm `Question-fit rule` bằng case 6, cụ thể chọn mức nhỏ nhất đủ trả lời câu hỏi; graph sâu hơn không tự chính xác hơn nếu provenance/confidence yếu

**Mệnh đề cần kiểm.** Lineage levels and what each answers: kiểm `Question-fit rule` bằng case 6, cụ thể chọn mức nhỏ nhất đủ trả lời câu hỏi; graph sâu hơn không tự chính xác hơn nếu provenance/confidence yếu.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.lineage-levels`, replay cùng identity với payload giống rồi payload xung đột. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Lineage levels and what each answers` công bố.

**Bằng chứng cần giữ.** Đối với probe 6 của `Lineage levels and what each answers`, tách duplicate replay khỏi identity collision bằng reason code. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.7. Lineage levels and what each answers: kiểm `System/entity level` bằng case 7, cụ thể cho biết platform hoặc asset lớn liên quan, hữu ích discovery nhưng quá thô cho impact kỹ thuật

**Mệnh đề cần kiểm.** Lineage levels and what each answers: kiểm `System/entity level` bằng case 7, cụ thể cho biết platform hoặc asset lớn liên quan, hữu ích discovery nhưng quá thô cho impact kỹ thuật.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.lineage-levels`, thêm record tới trễ trong horizon và ngoài horizon. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Lineage levels and what each answers` công bố.

**Bằng chứng cần giữ.** Đối với probe 7 của `Lineage levels and what each answers`, báo accepted-late, rejected-late và oldest outstanding timestamp. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.8. Lineage levels and what each answers: kiểm `Dataset level` bằng case 8, cụ thể nối input/output datasets, trả lời upstream/downstream và blast radius sơ bộ; chưa nói cột hay row nào ảnh hưởng

**Mệnh đề cần kiểm.** Lineage levels and what each answers: kiểm `Dataset level` bằng case 8, cụ thể nối input/output datasets, trả lời upstream/downstream và blast radius sơ bộ; chưa nói cột hay row nào ảnh hưởng.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.lineage-levels`, đổi schema theo một cách tương thích rồi một cách phá vỡ semantics. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Lineage levels and what each answers` công bố.

**Bằng chứng cần giữ.** Đối với probe 8 của `Lineage levels and what each answers`, giữ schema diff, classification và consumer-visible result. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.9. Lineage levels and what each answers: kiểm `Job level` bằng case 9, cụ thể đặt transformation/process giữa datasets, hỗ trợ ownership và operational diagnosis

**Mệnh đề cần kiểm.** Lineage levels and what each answers: kiểm `Job level` bằng case 9, cụ thể đặt transformation/process giữa datasets, hỗ trợ ownership và operational diagnosis.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.lineage-levels`, tạo missing và duplicate bù nhau để count tổng không đổi. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Lineage levels and what each answers` công bố.

**Bằng chứng cần giữ.** Đối với probe 9 của `Lineage levels and what each answers`, so key multiset và typed hashes thay vì chỉ row count. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.10. Lineage levels and what each answers: kiểm `Run level` bằng case 10, cụ thể gắn dependency với execution, code/version, nominal time và actual inputs; cần cho incident/reproducibility

**Mệnh đề cần kiểm.** Lineage levels and what each answers: kiểm `Run level` bằng case 10, cụ thể gắn dependency với execution, code/version, nominal time và actual inputs; cần cho incident/reproducibility.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.lineage-levels`, cho reviewer tái hiện chỉ từ evidence package. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Lineage levels and what each answers` công bố.

**Bằng chứng cần giữ.** Đối với probe 10 của `Lineage levels and what each answers`, package phải đủ để người khác dựng lại decision và limitation. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.11. Lineage levels and what each answers: kiểm `Field level` bằng case 11, cụ thể direct/indirect transformation của columns tăng precision nhưng parser, dynamic sql và udf tạo unknowns

**Mệnh đề cần kiểm.** Lineage levels and what each answers: kiểm `Field level` bằng case 11, cụ thể direct/indirect transformation của columns tăng precision nhưng parser, dynamic sql và udf tạo unknowns.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.lineage-levels`, so với oracle độc lập không dùng chung query hoặc parser. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Lineage levels and what each answers` công bố.

**Bằng chứng cần giữ.** Đối với probe 11 của `Lineage levels and what each answers`, independent result phải khớp ở grain đã công bố. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.12. Lineage levels and what each answers: kiểm `Question-fit rule` bằng case 12, cụ thể chọn mức nhỏ nhất đủ trả lời câu hỏi; graph sâu hơn không tự chính xác hơn nếu provenance/confidence yếu

**Mệnh đề cần kiểm.** Lineage levels and what each answers: kiểm `Question-fit rule` bằng case 12, cụ thể chọn mức nhỏ nhất đủ trả lời câu hỏi; graph sâu hơn không tự chính xác hơn nếu provenance/confidence yếu.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.lineage-levels`, chạy scope hẹp và population đầy đủ rồi công bố phần bị loại. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Lineage levels and what each answers` công bố.

**Bằng chứng cần giữ.** Đối với probe 12 của `Lineage levels and what each answers`, coverage phải nêu rõ excluded nodes, partitions hoặc incidents. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.13. Lineage levels and what each answers: kiểm `System/entity level` bằng case 13, cụ thể cho biết platform hoặc asset lớn liên quan, hữu ích discovery nhưng quá thô cho impact kỹ thuật

**Mệnh đề cần kiểm.** Lineage levels and what each answers: kiểm `System/entity level` bằng case 13, cụ thể cho biết platform hoặc asset lớn liên quan, hữu ích discovery nhưng quá thô cho impact kỹ thuật.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.lineage-levels`, thử timezone, precision hoặc partition ở hai phía của ranh giới. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Lineage levels and what each answers` công bố.

**Bằng chứng cần giữ.** Đối với probe 13 của `Lineage levels and what each answers`, UTC/local interval và rounding policy phải hiện trong output. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.14. Lineage levels and what each answers: kiểm `Dataset level` bằng case 14, cụ thể nối input/output datasets, trả lời upstream/downstream và blast radius sơ bộ; chưa nói cột hay row nào ảnh hưởng

**Mệnh đề cần kiểm.** Lineage levels and what each answers: kiểm `Dataset level` bằng case 14, cụ thể nối input/output datasets, trả lời upstream/downstream và blast radius sơ bộ; chưa nói cột hay row nào ảnh hưởng.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.lineage-levels`, đổi constraint đủ lớn để quyết định phải đảo. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Lineage levels and what each answers` công bố.

**Bằng chứng cần giữ.** Đối với probe 14 của `Lineage levels and what each answers`, ADR phải lưu changed constraint và reversal threshold. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.15. Lineage levels and what each answers: kiểm `Job level` bằng case 15, cụ thể đặt transformation/process giữa datasets, hỗ trợ ownership và operational diagnosis

**Mệnh đề cần kiểm.** Lineage levels and what each answers: kiểm `Job level` bằng case 15, cụ thể đặt transformation/process giữa datasets, hỗ trợ ownership và operational diagnosis.

**Thiết kế phép thử.** Trong ngữ cảnh `wiki.metadata.lineage-levels`, chạy lại từ môi trường sạch với versions và seed đã khóa. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `Lineage levels and what each answers` công bố.

**Bằng chứng cần giữ.** Đối với probe 15 của `Lineage levels and what each answers`, canonical result phải ổn định hoặc mọi nondeterminism phải được giải thích. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

## 8. Quy trình phản biện

1. Viết consumer-visible invariant cho `Lineage levels and what each answers` trước khi chọn query hoặc tool.
2. Khóa grain, identity, population, time window và authoritative source.
3. Phân biệt declared configuration, executed state và published state.
4. Chạy negative control, replay hoặc changed-assumption case phù hợp.
5. Đối soát bằng oracle độc lập; công bố coverage và phần không quan sát được.
6. Gắn owner, hành động, reversal trigger và hạn review cho kết luận.

## 9. Câu hỏi tự kiểm tra

1. `Lineage levels and what each answers: kiểm `System/entity level` bằng case 1, cụ thể cho biết platform hoặc asset lớn liên quan, hữu ích discovery nhưng quá thô cho impact kỹ thuật` thất bại đầu tiên ở boundary nào?
2. Artifact nào mạnh nhất để trả lời `Lineage levels and what each answers: kiểm `Job level` bằng case 3, cụ thể đặt transformation/process giữa datasets, hỗ trợ ownership và operational diagnosis`?
3. Counterexample nhỏ nhất cho `Lineage levels and what each answers: kiểm `Question-fit rule` bằng case 6, cụ thể chọn mức nhỏ nhất đủ trả lời câu hỏi; graph sâu hơn không tự chính xác hơn nếu provenance/confidence yếu` gồm những state nào?
4. `Lineage levels and what each answers: kiểm `Job level` bằng case 9, cụ thể đặt transformation/process giữa datasets, hỗ trợ ownership và operational diagnosis` có thể xanh giả ra sao?
5. Constraint nào khiến quyết định ở `Lineage levels and what each answers: kiểm `Dataset level` bằng case 14, cụ thể nối input/output datasets, trả lời upstream/downstream và blast radius sơ bộ; chưa nói cột hay row nào ảnh hưởng` phải đảo?
6. Phần nào của `Lineage levels and what each answers: kiểm `Job level` bằng case 15, cụ thể đặt transformation/process giữa datasets, hỗ trợ ownership và operational diagnosis` mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `Lineage levels and what each answers` chưa chạy trên hệ thống production; nội dung là giáo trình và expected evidence.
- Hành vi phụ thuộc phiên bản, connector, scheduler, warehouse và catalog configuration phải được kiểm lại.
- Các ma trận, ladder và threshold do giáo trình tổng hợp không được gán nguyên văn cho vendor.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-OPENLINEAGE-OVERVIEW]]
2. [[SRC-OPENLINEAGE-FACETS]]
3. [[SRC-DATAHUB-LINEAGE]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-OPENLINEAGE-OVERVIEW]] | Contract hoặc cơ chế liên quan trực tiếp tới `Lineage levels and what each answers` | Đã đọc locator; cần pin version khi chạy lab |
| [[SRC-OPENLINEAGE-FACETS]] | Contract hoặc cơ chế liên quan trực tiếp tới `Lineage levels and what each answers` | Đã đọc locator; cần pin version khi chạy lab |
| [[SRC-DATAHUB-LINEAGE]] | Contract hoặc cơ chế liên quan trực tiếp tới `Lineage levels and what each answers` | Đã đọc locator; cần pin version khi chạy lab |

## Key takeaways
- Mỗi lineage level trả lời một lớp câu hỏi; không suy field impact từ dataset edge.
- Với `wiki.metadata.lineage-levels`, quality của kết luận phụ thuộc identity, coverage và oracle chứ không phụ thuộc màu dashboard.
- Câu hỏi `Entity, dataset, job, run và field lineage trả lời những câu hỏi khác nhau nào và không được suy vượt cấp ra sao?` chỉ được trả lời trong scope và version đã ghi.
- Các source IDs `src.web.openlineage-overview, src.web.openlineage-facets, src.web.datahub-lineage` đặt ranh giới cho source fact; phần còn lại là synthesis có nhãn.
- Trước khi lab chạy, đây là note đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.
