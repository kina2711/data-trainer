---
note_id: wiki.distributed.formal-model-safety-liveness
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
primary_question: Trước khi nói hệ phân tán đúng, cần phát biểu safety, liveness và network/failure assumptions nào?
source_ids:
  - src.book.kleppmann-ddia.1e
aliases: [The formal model - safety, liveness and what the network may do]
tags: [wiki/distributed-systems, distributed-systems, replication, consensus, reliability]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/197-the-formal-model-safety-liveness-and-what-the-network-may-do.md
relationships:
  builds_on: [wiki.ingestion.atomic-landing-checkpoint-ordering]
  prerequisite_of: [wiki.distributed.timeout-ambiguity-failure-modes]
  related_to: []

---
# The formal model - safety, liveness and what the network may do

> [!abstract] Câu hỏi trung tâm
> Trước khi nói hệ phân tán đúng, cần phát biểu safety, liveness và network/failure assumptions nào?

## 1. State machine model

Processes, local state, messages, transitions và external observations phải được định nghĩa trước trace. Đừng bắt đầu bằng tên công cụ. Hãy bắt đầu bằng đối tượng được bảo vệ, boundary quan sát được và hậu quả nếu kết luận sai. Trong bài `The formal model - safety, liveness and what the network may do`, câu hỏi thực dụng là: Trước khi nói hệ phân tán đúng, cần phát biểu safety, liveness và network/failure assumptions nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 2. Safety

Safety nói điều xấu không bao giờ xảy ra, như hai committed values xung đột; một counterexample đủ bác bỏ. Điểm khó không nằm ở cú pháp mà ở identity và scope. Hai phép đo cùng tên vẫn có thể nói về hai population hoặc hai thời điểm khác nhau. Trong bài `The formal model - safety, liveness and what the network may do`, câu hỏi thực dụng là: Trước khi nói hệ phân tán đúng, cần phát biểu safety, liveness và network/failure assumptions nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 3. Liveness

Liveness nói điều tốt cuối cùng xảy ra dưới fairness/timing assumptions; delay hữu hạn nhưng không biết giới hạn làm proof khó. Một dashboard xanh chỉ là tín hiệu. Muốn biến nó thành bằng chứng phải giữ input, phiên bản, rule, trạng thái trước–sau và cách tính độc lập. Trong bài `The formal model - safety, liveness and what the network may do`, câu hỏi thực dụng là: Trước khi nói hệ phân tán đúng, cần phát biểu safety, liveness và network/failure assumptions nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 4. Network model

Message có thể delay, drop, duplicate, reorder; partition là mất kết nối kéo dài, không phải exception có timing chắc chắn. Thiết kế tốt phải chịu được counterexample. Hãy chủ động tạo case sát boundary, case thiếu dữ liệu và case replay thay vì chỉ chạy happy path. Trong bài `The formal model - safety, liveness and what the network may do`, câu hỏi thực dụng là: Trước khi nói hệ phân tán đúng, cần phát biểu safety, liveness và network/failure assumptions nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 5. Failure model

Crash-stop, crash-recovery, omission và Byzantine khác nhau; thuật toán đúng cho loại này không tự đúng cho loại kia. Chi phí vận hành thuộc contract. Một rule đúng nhưng quá đắt, quá ồn hoặc không có owner sẽ nhanh chóng bị tắt và mất tác dụng. Trong bài `The formal model - safety, liveness and what the network may do`, câu hỏi thực dụng là: Trước khi nói hệ phân tán đúng, cần phát biểu safety, liveness và network/failure assumptions nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 6. Trace experiment

Viết invariant và progress condition rồi enumerate schedules có delay, retry, restart và partition để tìm counterexample. Kết luận cần có điều kiện đảo chiều. Khi volume, latency, nguồn thẩm quyền hoặc topology đổi, quyết định cũ phải được xem xét lại bằng cùng một oracle. Trong bài `The formal model - safety, liveness and what the network may do`, câu hỏi thực dụng là: Trước khi nói hệ phân tán đúng, cần phát biểu safety, liveness và network/failure assumptions nào? Ta ghi rõ grain, population, time window, owner và hành động sau failure; nếu một trường chưa biết thì đánh dấu unknown thay vì lấp bằng mặc định. Bằng chứng tối thiểu gồm fixture có version, cấu hình hoặc rule đã resolve, raw observation, expected result và limitation. Phần này là curriculum synthesis dựa trên các nguồn đã định danh, không phải lời hứa rằng mọi adapter hay deployment đều có cùng hành vi.

## 7. Ma trận kiểm chứng từng mệnh đề

Với `wiki.distributed.formal-model-safety-liveness`, command thành công không tự chứng minh dữ liệu đúng. Protocol riêng của bài là: Mô hình hóa boundary/state, tiêm một event gây ambiguity hoặc policy conflict và so trace với invariant cùng oracle độc lập. Mỗi probe dưới đây phải nối input boundary với failure signal và oracle có thể phản bác kết luận.

### 7.1. The formal model - safety, liveness and what the network may do: kiểm `State machine model` bằng case 1, cụ thể processes, local state, messages, transitions và external observations phải được định nghĩa trước trace

**Mệnh đề cần kiểm.** The formal model - safety, liveness and what the network may do: kiểm `State machine model` bằng case 1, cụ thể processes, local state, messages, transitions và external observations phải được định nghĩa trước trace.

**Thiết kế phép thử cho `wiki.distributed.formal-model-safety-liveness`.** Trong ngữ cảnh `wiki.distributed.formal-model-safety-liveness`, tạo positive control và negative control chỉ khác đúng một điều kiện. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The formal model - safety, liveness and what the network may do` công bố.

**Bằng chứng cần giữ.** Đối với probe 1 của `The formal model - safety, liveness and what the network may do`, giữ fixture, raw failing rows và lệnh tái hiện. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.2. The formal model - safety, liveness and what the network may do: kiểm `Safety` bằng case 2, cụ thể safety nói điều xấu không bao giờ xảy ra, như hai committed values xung đột; một counterexample đủ bác bỏ

**Mệnh đề cần kiểm.** The formal model - safety, liveness and what the network may do: kiểm `Safety` bằng case 2, cụ thể safety nói điều xấu không bao giờ xảy ra, như hai committed values xung đột; một counterexample đủ bác bỏ.

**Thiết kế phép thử cho `wiki.distributed.formal-model-safety-liveness`.** Trong ngữ cảnh `wiki.distributed.formal-model-safety-liveness`, đổi grain nhưng giữ tổng số dòng để lộ phép đo sai cấp. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The formal model - safety, liveness and what the network may do` công bố.

**Bằng chứng cần giữ.** Đối với probe 2 của `The formal model - safety, liveness and what the network may do`, báo numerator, denominator và key set ở cả hai grain. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.3. The formal model - safety, liveness and what the network may do: kiểm `Liveness` bằng case 3, cụ thể liveness nói điều tốt cuối cùng xảy ra dưới fairness/timing assumptions; delay hữu hạn nhưng không biết giới hạn làm proof khó

**Mệnh đề cần kiểm.** The formal model - safety, liveness and what the network may do: kiểm `Liveness` bằng case 3, cụ thể liveness nói điều tốt cuối cùng xảy ra dưới fairness/timing assumptions; delay hữu hạn nhưng không biết giới hạn làm proof khó.

**Thiết kế phép thử cho `wiki.distributed.formal-model-safety-liveness`.** Trong ngữ cảnh `wiki.distributed.formal-model-safety-liveness`, đưa một giá trị tới đúng boundary và một giá trị vượt boundary. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The formal model - safety, liveness and what the network may do` công bố.

**Bằng chứng cần giữ.** Đối với probe 3 của `The formal model - safety, liveness and what the network may do`, lưu hai observed values cùng rule đã resolve. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.4. The formal model - safety, liveness and what the network may do: kiểm `Network model` bằng case 4, cụ thể message có thể delay, drop, duplicate, reorder; partition là mất kết nối kéo dài, không phải exception có timing chắc chắn

**Mệnh đề cần kiểm.** The formal model - safety, liveness and what the network may do: kiểm `Network model` bằng case 4, cụ thể message có thể delay, drop, duplicate, reorder; partition là mất kết nối kéo dài, không phải exception có timing chắc chắn.

**Thiết kế phép thử cho `wiki.distributed.formal-model-safety-liveness`.** Trong ngữ cảnh `wiki.distributed.formal-model-safety-liveness`, kill tiến trình ngay trước rồi ngay sau durable side effect. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The formal model - safety, liveness and what the network may do` công bố.

**Bằng chứng cần giữ.** Đối với probe 4 của `The formal model - safety, liveness and what the network may do`, lưu checkpoint, external ledger và trạng thái sau restart. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.5. The formal model - safety, liveness and what the network may do: kiểm `Failure model` bằng case 5, cụ thể crash-stop, crash-recovery, omission và byzantine khác nhau; thuật toán đúng cho loại này không tự đúng cho loại kia

**Mệnh đề cần kiểm.** The formal model - safety, liveness and what the network may do: kiểm `Failure model` bằng case 5, cụ thể crash-stop, crash-recovery, omission và byzantine khác nhau; thuật toán đúng cho loại này không tự đúng cho loại kia.

**Thiết kế phép thử cho `wiki.distributed.formal-model-safety-liveness`.** Trong ngữ cảnh `wiki.distributed.formal-model-safety-liveness`, đảo thứ tự input và concurrency nhưng giữ logical population. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The formal model - safety, liveness and what the network may do` công bố.

**Bằng chứng cần giữ.** Đối với probe 5 của `The formal model - safety, liveness and what the network may do`, so canonical hash và business totals giữa các thứ tự. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.6. The formal model - safety, liveness and what the network may do: kiểm `Trace experiment` bằng case 6, cụ thể viết invariant và progress condition rồi enumerate schedules có delay, retry, restart và partition để tìm counterexample

**Mệnh đề cần kiểm.** The formal model - safety, liveness and what the network may do: kiểm `Trace experiment` bằng case 6, cụ thể viết invariant và progress condition rồi enumerate schedules có delay, retry, restart và partition để tìm counterexample.

**Thiết kế phép thử cho `wiki.distributed.formal-model-safety-liveness`.** Trong ngữ cảnh `wiki.distributed.formal-model-safety-liveness`, replay cùng identity với payload giống rồi payload xung đột. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The formal model - safety, liveness and what the network may do` công bố.

**Bằng chứng cần giữ.** Đối với probe 6 của `The formal model - safety, liveness and what the network may do`, tách duplicate replay khỏi identity collision bằng reason code. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.7. The formal model - safety, liveness and what the network may do: kiểm `State machine model` bằng case 7, cụ thể processes, local state, messages, transitions và external observations phải được định nghĩa trước trace

**Mệnh đề cần kiểm.** The formal model - safety, liveness and what the network may do: kiểm `State machine model` bằng case 7, cụ thể processes, local state, messages, transitions và external observations phải được định nghĩa trước trace.

**Thiết kế phép thử cho `wiki.distributed.formal-model-safety-liveness`.** Trong ngữ cảnh `wiki.distributed.formal-model-safety-liveness`, thêm record tới trễ trong horizon và ngoài horizon. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The formal model - safety, liveness and what the network may do` công bố.

**Bằng chứng cần giữ.** Đối với probe 7 của `The formal model - safety, liveness and what the network may do`, báo accepted-late, rejected-late và oldest outstanding timestamp. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.8. The formal model - safety, liveness and what the network may do: kiểm `Safety` bằng case 8, cụ thể safety nói điều xấu không bao giờ xảy ra, như hai committed values xung đột; một counterexample đủ bác bỏ

**Mệnh đề cần kiểm.** The formal model - safety, liveness and what the network may do: kiểm `Safety` bằng case 8, cụ thể safety nói điều xấu không bao giờ xảy ra, như hai committed values xung đột; một counterexample đủ bác bỏ.

**Thiết kế phép thử cho `wiki.distributed.formal-model-safety-liveness`.** Trong ngữ cảnh `wiki.distributed.formal-model-safety-liveness`, đổi schema theo một cách tương thích rồi một cách phá vỡ semantics. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The formal model - safety, liveness and what the network may do` công bố.

**Bằng chứng cần giữ.** Đối với probe 8 của `The formal model - safety, liveness and what the network may do`, giữ schema diff, classification và consumer-visible result. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.9. The formal model - safety, liveness and what the network may do: kiểm `Liveness` bằng case 9, cụ thể liveness nói điều tốt cuối cùng xảy ra dưới fairness/timing assumptions; delay hữu hạn nhưng không biết giới hạn làm proof khó

**Mệnh đề cần kiểm.** The formal model - safety, liveness and what the network may do: kiểm `Liveness` bằng case 9, cụ thể liveness nói điều tốt cuối cùng xảy ra dưới fairness/timing assumptions; delay hữu hạn nhưng không biết giới hạn làm proof khó.

**Thiết kế phép thử cho `wiki.distributed.formal-model-safety-liveness`.** Trong ngữ cảnh `wiki.distributed.formal-model-safety-liveness`, tạo missing và duplicate bù nhau để count tổng không đổi. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The formal model - safety, liveness and what the network may do` công bố.

**Bằng chứng cần giữ.** Đối với probe 9 của `The formal model - safety, liveness and what the network may do`, so key multiset và typed hashes thay vì chỉ row count. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.10. The formal model - safety, liveness and what the network may do: kiểm `Network model` bằng case 10, cụ thể message có thể delay, drop, duplicate, reorder; partition là mất kết nối kéo dài, không phải exception có timing chắc chắn

**Mệnh đề cần kiểm.** The formal model - safety, liveness and what the network may do: kiểm `Network model` bằng case 10, cụ thể message có thể delay, drop, duplicate, reorder; partition là mất kết nối kéo dài, không phải exception có timing chắc chắn.

**Thiết kế phép thử cho `wiki.distributed.formal-model-safety-liveness`.** Trong ngữ cảnh `wiki.distributed.formal-model-safety-liveness`, cho reviewer tái hiện chỉ từ evidence package. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The formal model - safety, liveness and what the network may do` công bố.

**Bằng chứng cần giữ.** Đối với probe 10 của `The formal model - safety, liveness and what the network may do`, package phải đủ để người khác dựng lại decision và limitation. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.11. The formal model - safety, liveness and what the network may do: kiểm `Failure model` bằng case 11, cụ thể crash-stop, crash-recovery, omission và byzantine khác nhau; thuật toán đúng cho loại này không tự đúng cho loại kia

**Mệnh đề cần kiểm.** The formal model - safety, liveness and what the network may do: kiểm `Failure model` bằng case 11, cụ thể crash-stop, crash-recovery, omission và byzantine khác nhau; thuật toán đúng cho loại này không tự đúng cho loại kia.

**Thiết kế phép thử cho `wiki.distributed.formal-model-safety-liveness`.** Trong ngữ cảnh `wiki.distributed.formal-model-safety-liveness`, so với oracle độc lập không dùng chung query hoặc parser. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The formal model - safety, liveness and what the network may do` công bố.

**Bằng chứng cần giữ.** Đối với probe 11 của `The formal model - safety, liveness and what the network may do`, independent result phải khớp ở grain đã công bố. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.12. The formal model - safety, liveness and what the network may do: kiểm `Trace experiment` bằng case 12, cụ thể viết invariant và progress condition rồi enumerate schedules có delay, retry, restart và partition để tìm counterexample

**Mệnh đề cần kiểm.** The formal model - safety, liveness and what the network may do: kiểm `Trace experiment` bằng case 12, cụ thể viết invariant và progress condition rồi enumerate schedules có delay, retry, restart và partition để tìm counterexample.

**Thiết kế phép thử cho `wiki.distributed.formal-model-safety-liveness`.** Trong ngữ cảnh `wiki.distributed.formal-model-safety-liveness`, chạy scope hẹp và population đầy đủ rồi công bố phần bị loại. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The formal model - safety, liveness and what the network may do` công bố.

**Bằng chứng cần giữ.** Đối với probe 12 của `The formal model - safety, liveness and what the network may do`, coverage phải nêu rõ excluded nodes, partitions hoặc incidents. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.13. The formal model - safety, liveness and what the network may do: kiểm `State machine model` bằng case 13, cụ thể processes, local state, messages, transitions và external observations phải được định nghĩa trước trace

**Mệnh đề cần kiểm.** The formal model - safety, liveness and what the network may do: kiểm `State machine model` bằng case 13, cụ thể processes, local state, messages, transitions và external observations phải được định nghĩa trước trace.

**Thiết kế phép thử cho `wiki.distributed.formal-model-safety-liveness`.** Trong ngữ cảnh `wiki.distributed.formal-model-safety-liveness`, thử timezone, precision hoặc partition ở hai phía của ranh giới. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The formal model - safety, liveness and what the network may do` công bố.

**Bằng chứng cần giữ.** Đối với probe 13 của `The formal model - safety, liveness and what the network may do`, UTC/local interval và rounding policy phải hiện trong output. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.14. The formal model - safety, liveness and what the network may do: kiểm `Safety` bằng case 14, cụ thể safety nói điều xấu không bao giờ xảy ra, như hai committed values xung đột; một counterexample đủ bác bỏ

**Mệnh đề cần kiểm.** The formal model - safety, liveness and what the network may do: kiểm `Safety` bằng case 14, cụ thể safety nói điều xấu không bao giờ xảy ra, như hai committed values xung đột; một counterexample đủ bác bỏ.

**Thiết kế phép thử cho `wiki.distributed.formal-model-safety-liveness`.** Trong ngữ cảnh `wiki.distributed.formal-model-safety-liveness`, đổi constraint đủ lớn để quyết định phải đảo. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The formal model - safety, liveness and what the network may do` công bố.

**Bằng chứng cần giữ.** Đối với probe 14 của `The formal model - safety, liveness and what the network may do`, ADR phải lưu changed constraint và reversal threshold. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

### 7.15. The formal model - safety, liveness and what the network may do: kiểm `Liveness` bằng case 15, cụ thể liveness nói điều tốt cuối cùng xảy ra dưới fairness/timing assumptions; delay hữu hạn nhưng không biết giới hạn làm proof khó

**Mệnh đề cần kiểm.** The formal model - safety, liveness and what the network may do: kiểm `Liveness` bằng case 15, cụ thể liveness nói điều tốt cuối cùng xảy ra dưới fairness/timing assumptions; delay hữu hạn nhưng không biết giới hạn làm proof khó.

**Thiết kế phép thử cho `wiki.distributed.formal-model-safety-liveness`.** Trong ngữ cảnh `wiki.distributed.formal-model-safety-liveness`, chạy lại từ môi trường sạch với versions và seed đã khóa. Khóa input snapshot, phiên bản và owner của rule; chạy đúng population được bài `The formal model - safety, liveness and what the network may do` công bố.

**Bằng chứng cần giữ.** Đối với probe 15 của `The formal model - safety, liveness and what the network may do`, canonical result phải ổn định hoặc mọi nondeterminism phải được giải thích. Nếu chưa chạy lab, ghi expected evidence và giữ trạng thái review; không biến protocol thành observation.

## 8. Quy trình phản biện

1. Viết consumer-visible invariant cho `The formal model - safety, liveness and what the network may do` trước khi chọn query hoặc tool.
2. Khóa grain, identity, population, time window và authoritative source.
3. Phân biệt declared configuration, executed state và published state.
4. Chạy negative control, replay hoặc changed-assumption case phù hợp.
5. Đối soát bằng oracle độc lập; công bố coverage và phần không quan sát được.
6. Gắn owner, hành động, reversal trigger và hạn review cho kết luận.

## 9. Câu hỏi tự kiểm tra

1. `The formal model - safety, liveness and what the network may do: kiểm `State machine model` bằng case 1, cụ thể processes, local state, messages, transitions và external observations phải được định nghĩa trước trace` thất bại đầu tiên ở boundary nào?
2. Artifact nào mạnh nhất để trả lời `The formal model - safety, liveness and what the network may do: kiểm `Liveness` bằng case 3, cụ thể liveness nói điều tốt cuối cùng xảy ra dưới fairness/timing assumptions; delay hữu hạn nhưng không biết giới hạn làm proof khó`?
3. Counterexample nhỏ nhất cho `The formal model - safety, liveness and what the network may do: kiểm `Trace experiment` bằng case 6, cụ thể viết invariant và progress condition rồi enumerate schedules có delay, retry, restart và partition để tìm counterexample` gồm những state nào?
4. `The formal model - safety, liveness and what the network may do: kiểm `Liveness` bằng case 9, cụ thể liveness nói điều tốt cuối cùng xảy ra dưới fairness/timing assumptions; delay hữu hạn nhưng không biết giới hạn làm proof khó` có thể xanh giả ra sao?
5. Constraint nào khiến quyết định ở `The formal model - safety, liveness and what the network may do: kiểm `Safety` bằng case 14, cụ thể safety nói điều xấu không bao giờ xảy ra, như hai committed values xung đột; một counterexample đủ bác bỏ` phải đảo?
6. Phần nào của `The formal model - safety, liveness and what the network may do: kiểm `Liveness` bằng case 15, cụ thể liveness nói điều tốt cuối cùng xảy ra dưới fairness/timing assumptions; delay hữu hạn nhưng không biết giới hạn làm proof khó` mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `The formal model - safety, liveness and what the network may do` chưa chạy trên hệ thống production; nội dung là giáo trình và expected evidence.
- Hành vi phụ thuộc phiên bản, connector, scheduler, warehouse và catalog configuration phải được kiểm lại.
- Các ma trận, ladder và threshold do giáo trình tổng hợp không được gán nguyên văn cho vendor.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-KLEPPMANN-DDIA-1E]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-KLEPPMANN-DDIA-1E]] | Contract hoặc cơ chế liên quan trực tiếp tới `The formal model - safety, liveness and what the network may do` | Đã đọc locator; cần pin version khi chạy lab |

## Key takeaways
- Correctness chỉ có nghĩa dưới safety/liveness và failure assumptions đã phát biểu.
- Với `wiki.distributed.formal-model-safety-liveness`, quality của kết luận phụ thuộc identity, coverage và oracle chứ không phụ thuộc màu dashboard.
- Câu hỏi `Trước khi nói hệ phân tán đúng, cần phát biểu safety, liveness và network/failure assumptions nào?` chỉ được trả lời trong scope và version đã ghi.
- Các source IDs `src.book.kleppmann-ddia.1e` đặt ranh giới cho source fact; phần còn lại là synthesis có nhãn.
- Trước khi lab chạy, đây là note đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule — kiểm chứng `wiki.distributed.formal-model-safety-liveness`

> [!important] Phân loại mệnh đề
> Với `wiki.distributed.formal-model-safety-liveness`, sơ đồ, ví dụ và artifact về **The formal model - safety, liveness and what the network may do** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.book.kleppmann-ddia.1e"] --> B["Khóa boundary"]
    B --> M["Cơ chế: The formal model - safety, liveness and what the network may d"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.distributed.formal-model-safety-liveness` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **The formal model - safety, liveness and what the network may do**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```sql
-- Verification harness for: The formal model - safety, liveness and what the network may do
WITH evidence AS (
    SELECT 'wiki.distributed.formal-model-safety-liveness' AS concept_id,
           'boundary_declared' AS check_name, 1 AS passed
    UNION ALL
    SELECT 'wiki.distributed.formal-model-safety-liveness', 'independent_oracle', 1
    UNION ALL
    SELECT 'wiki.distributed.formal-model-safety-liveness', 'reversal_trigger_recorded', 1
)
SELECT concept_id,
       MIN(passed) AS all_hard_checks_pass,
       COUNT(*) AS evidence_items
FROM evidence
GROUP BY concept_id
HAVING MIN(passed) = 1;
```

Artifact của `wiki.distributed.formal-model-safety-liveness` buộc người dùng ghi boundary, oracle và reversal trigger cho **The formal model - safety, liveness and what the network may do**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

### Tự kiểm tra trước khi tái sử dụng

1. Bạn có thể trả lời `Trước khi nói hệ phân tán đúng, cần phát biểu safety, liveness và network/failure assumptions nào?` bằng một câu mà không kéo thêm concept thứ hai không?
2. Source locator nào đỡ cho claim, và phần nào chỉ là synthesis trong note?
3. Observation nào khiến bạn dừng, thu hẹp hoặc đảo quyết định?
4. Artifact nào cho phép một reviewer độc lập tái hiện kết quả?

<!-- ATOMIC-EXECUTION-CAPSULE:END -->
