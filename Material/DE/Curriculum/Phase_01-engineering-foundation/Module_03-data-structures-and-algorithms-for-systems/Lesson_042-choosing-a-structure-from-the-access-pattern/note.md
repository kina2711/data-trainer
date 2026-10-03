# Phase 1: Engineering Foundation
# Module 3: Data Structures and Algorithms for Systems
# Lesson 42: Choosing a structure from the access pattern

## Mục tiêu bài học

**Năng lực cần chứng minh.** Chọn cấu trúc cho năm mẫu truy cập cho trước, mỗi lần dẫn về một số đo đã tự đo.

**Điều kiện hoàn thành.** Chọn đúng ≥ 4/5 mẫu truy cập với số đo dẫn chứng, và nhận ra đúng trường hợp nên dùng cấu trúc đơn giản nhất.


# Choosing a structure from the access pattern

**Tóm tắt bản chất:** map required operations/frequency to candidate invariants and cost model, then include memory/locality/update/recovery Sai boundary ở `chọn data structure từ operations distribution và constraints` làm kết quả có vẻ đúng trong happy path nhưng không chịu được failure hoặc changed constraint.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, kiểm chứng và áp dụng chọn data structure từ operations distribution và constraints?

## Nỗi Đau & Động Lực

map required operations/frequency to candidate invariants and cost model, then include memory/locality/update/recovery Với `wiki.de-foundation.choosing-structure-access-pattern`, điểm phải khóa là state transition và invariant; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Không có mô hình này, lỗi thường lộ ở consumer sau cùng: output sai, latency vọt, resource không được giải phóng hoặc lịch sử không còn tái hiện được. Chi phí thật của `Choosing a structure from the access pattern` vì thế nằm ở thời gian chẩn đoán và phạm vi phục hồi, không nằm ở số dòng syntax.

## Cơ Chế Tác Động

average complexity alone ignores tail, scale range and representation; library implementation may alter constants Với `wiki.de-foundation.choosing-structure-access-pattern`, điểm phải khóa là identity, ownership và boundary; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hãy tách declared state, executed state và published state của `chọn data structure từ operations distribution và constraints`. Một command thành công chỉ là executed signal; muốn kết luận cần đối soát consumer-visible invariant và trạng thái còn lại sau restart hoặc replay.

## Bản Đồ Quyết Định

choose fashionable structure, benchmark wrong operation mix, or omit adversarial input Với `wiki.de-foundation.choosing-structure-access-pattern`, điểm phải khóa là failure path và recovery; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Quy tắc mặc định cho `Choosing a structure from the access pattern` là chọn phương án đơn giản nhất qua được hard constraints, rồi ghi rõ điều kiện đảo. Bảng quyết định tối thiểu gồm workload, identity, state owner, time/memory budget, failure domain và khả năng rollback.

## Case Study Thực Chiến: Choosing a structure from the access pattern

start access-pattern table; eliminate violated hard constraints; measure remaining candidates on representative trace Với `wiki.de-foundation.choosing-structure-access-pattern`, điểm phải khóa là decision trade-off và reversal trigger; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Case dùng fixture nhỏ nhưng phải giữ cơ chế chi phối. Trước khi chạy, learner viết expected transition; sau khi chạy, họ đối chiếu raw artifact với oracle và giải thích mọi khác biệt thay vì sửa expected cho khớp output.

## Góc Khuất & Ngộ Nhận

operation histogram, size distribution, memory, latency percentiles, invariant checks và maintenance cost Với `wiki.de-foundation.choosing-structure-access-pattern`, điểm phải khóa là evidence package và oracle; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

**Hiểu lầm:** Happy path chạy nhanh nghĩa là thiết kế đúng. **Thực tế:** choose fashionable structure, benchmark wrong operation mix, or omit adversarial input **Vì sao nghe hợp lý:** case nhỏ thường không chạm capacity, concurrency, failure hoặc version boundary.

**Hiểu lầm:** Tool hoặc API tự bảo đảm semantics. **Thực tế:** guarantee chỉ tồn tại trong scope và state đã công bố. **Vì sao nghe hợp lý:** syntax che mất protocol phía dưới.

## Nếu Bạn Dạy Lại Điều Này...

shift workload from point lookup to range/top-k and require decision reversal Với `wiki.de-foundation.choosing-structure-access-pattern`, điểm phải khóa là changed-constraint transfer; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hook dạy lại bắt đầu bằng một dự đoán dễ sai về `chọn data structure từ operations distribution và constraints`. Bài tập seed đổi đúng một constraint, yêu cầu learner giữ hoặc đảo quyết định và chỉ ra evidence nào đủ mạnh để thuyết phục một reviewer không tham dự buổi học.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `Choosing a structure from the access pattern` là: operation histogram, size distribution, memory, latency percentiles, invariant checks và maintenance cost Mỗi probe nối input boundary với failure signal và oracle có thể bác bỏ kết luận.

### Probe 1: state transition và invariant

**Mệnh đề cần kiểm.** map required operations/frequency to candidate invariants and cost model, then include memory/locality/update/recovery

**Thiết kế phép thử.** Với `wiki.de-foundation.choosing-structure-access-pattern`, tạo positive và negative control chỉ khác một điều kiện; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề cần kiểm.** average complexity alone ignores tail, scale range and representation; library implementation may alter constants

**Thiết kế phép thử.** Với `wiki.de-foundation.choosing-structure-access-pattern`, tạo boundary case ngay trước và sau ngưỡng; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề cần kiểm.** choose fashionable structure, benchmark wrong operation mix, or omit adversarial input

**Thiết kế phép thử.** Với `wiki.de-foundation.choosing-structure-access-pattern`, tạo replay cùng identity với state khác; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** start access-pattern table; eliminate violated hard constraints; measure remaining candidates on representative trace

**Thiết kế phép thử.** Với `wiki.de-foundation.choosing-structure-access-pattern`, tạo failure inject trước và sau durable transition; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề cần kiểm.** operation histogram, size distribution, memory, latency percentiles, invariant checks và maintenance cost

**Thiết kế phép thử.** Với `wiki.de-foundation.choosing-structure-access-pattern`, tạo changed scale làm cost model đổi; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề cần kiểm.** shift workload from point lookup to range/top-k and require decision reversal

**Thiết kế phép thử.** Với `wiki.de-foundation.choosing-structure-access-pattern`, tạo adversarial order hoặc skew; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề cần kiểm.** map required operations/frequency to candidate invariants and cost model, then include memory/locality/update/recovery

**Thiết kế phép thử.** Với `wiki.de-foundation.choosing-structure-access-pattern`, tạo fresh environment không cache; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề cần kiểm.** average complexity alone ignores tail, scale range and representation; library implementation may alter constants

**Thiết kế phép thử.** Với `wiki.de-foundation.choosing-structure-access-pattern`, tạo independent oracle không dùng chung implementation; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề cần kiểm.** choose fashionable structure, benchmark wrong operation mix, or omit adversarial input

**Thiết kế phép thử.** Với `wiki.de-foundation.choosing-structure-access-pattern`, tạo partial progress rồi restart; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** start access-pattern table; eliminate violated hard constraints; measure remaining candidates on representative trace

**Thiết kế phép thử.** Với `wiki.de-foundation.choosing-structure-access-pattern`, tạo missing evidence phải abstain; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề cần kiểm.** operation histogram, size distribution, memory, latency percentiles, invariant checks và maintenance cost

**Thiết kế phép thử.** Với `wiki.de-foundation.choosing-structure-access-pattern`, tạo reviewer tái hiện từ package; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề cần kiểm.** shift workload from point lookup to range/top-k and require decision reversal

**Thiết kế phép thử.** Với `wiki.de-foundation.choosing-structure-access-pattern`, tạo constraint đổi đủ để quyết định đảo; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên của `chọn data structure từ operations distribution và constraints` nằm ở đâu?

<details><summary>Đáp án</summary>average complexity alone ignores tail, scale range and representation; library implementation may alter constants</details>

2. Failure nào dễ tạo kết quả xanh giả nhất?

<details><summary>Đáp án</summary>choose fashionable structure, benchmark wrong operation mix, or omit adversarial input</details>

3. Constraint nào khiến quyết định phải đảo?

<details><summary>Đáp án</summary>shift workload from point lookup to range/top-k and require decision reversal</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `Choosing a structure from the access pattern` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Mọi kết luận phụ thuộc version, workload, operating system, interpreter/compiler hoặc hardware phải được kiểm lại trên target.
- Concept key `ck.de.choosing-structure-access-pattern` đang ở trạng thái `proposed`; note không được tính là canonical registry coverage trước khi owner đăng ký key.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-SEDGEWICK-WAYNE-ALGORITHMS-4E]]
2. [[SRC-PETROV-DATABASE-INTERNALS-1E]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-SEDGEWICK-WAYNE-ALGORITHMS-4E]] — `src.book.sedgewick-wayne-algorithms.4e` | Sections 1.4, 2.2, 2.4, 3.2–3.4, 4.1–4.2; PDF 185–604 | cơ chế và boundary liên quan trực tiếp tới `chọn data structure từ operations distribution và constraints` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L042 |
| [[SRC-PETROV-DATABASE-INTERNALS-1E]] — `src.book.petrov-database-internals.1e` | Chapter 7 PDF 167–210 | cơ chế và boundary liên quan trực tiếp tới `chọn data structure từ operations distribution và constraints` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L042 |

## Key takeaways
- start access-pattern table; eliminate violated hard constraints; measure remaining candidates on representative trace
- operation histogram, size distribution, memory, latency percentiles, invariant checks và maintenance cost
- `chọn data structure từ operations distribution và constraints` chỉ có nghĩa trong scope, identity, state và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.
