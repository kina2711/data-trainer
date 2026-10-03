# Phase 1: Engineering Foundation
# Module 3: Data Structures and Algorithms for Systems
# Lesson 40: Hash join against sort-merge join

## Mục tiêu bài học

**Năng lực cần chứng minh.** Cài cả hai phép kết và tìm được điểm giao theo kích thước dữ liệu, bộ nhớ và độ lệch khoá.

**Điều kiện hoàn thành.** Tìm được điểm giao theo ≥ 2 yếu tố kèm số đo, và giải thích đúng vì sao phép kết băm suy giảm khi khoá lệch.


# Hash join against sort-merge join

**Tóm tắt bản chất:** hash join builds partitions/table then probes; merge join advances sorted inputs and handles duplicate groups Sai boundary ở `hash join và sort-merge join dưới memory/order constraints` làm kết quả có vẻ đúng trong happy path nhưng không chịu được failure hoặc changed constraint.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, kiểm chứng và áp dụng hash join và sort-merge join dưới memory/order constraints?

## Nỗi Đau & Động Lực

hash join builds partitions/table then probes; merge join advances sorted inputs and handles duplicate groups Với `wiki.de-foundation.hash-join-vs-sort-merge-join`, điểm phải khóa là state transition và invariant; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Không có mô hình này, lỗi thường lộ ở consumer sau cùng: output sai, latency vọt, resource không được giải phóng hoặc lịch sử không còn tái hiện được. Chi phí thật của `Hash join against sort-merge join` vì thế nằm ở thời gian chẩn đoán và phạm vi phục hồi, không nằm ở số dòng syntax.

## Cơ Chế Tác Động

hash join suits equi-join and needs build memory/partition; merge join benefits existing order and supports ordered stream Với `wiki.de-foundation.hash-join-vs-sort-merge-join`, điểm phải khóa là identity, ownership và boundary; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hãy tách declared state, executed state và published state của `hash join và sort-merge join dưới memory/order constraints`. Một command thành công chỉ là executed signal; muốn kết luận cần đối soát consumer-visible invariant và trạng thái còn lại sau restart hoặc replay.

## Bản Đồ Quyết Định

build spill, skew hot key, duplicate cross product và bad estimates explode cost Với `wiki.de-foundation.hash-join-vs-sort-merge-join`, điểm phải khóa là failure path và recovery; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Quy tắc mặc định cho `Hash join against sort-merge join` là chọn phương án đơn giản nhất qua được hard constraints, rồi ghi rõ điều kiện đảo. Bảng quyết định tối thiểu gồm workload, identity, state owner, time/memory budget, failure domain và khả năng rollback.

## Case Study Thực Chiến: Hash join against sort-merge join

choose from predicate, input order, sizes, skew, memory and downstream order; benchmark both at boundary Với `wiki.de-foundation.hash-join-vs-sort-merge-join`, điểm phải khóa là decision trade-off và reversal trigger; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Case dùng fixture nhỏ nhưng phải giữ cơ chế chi phối. Trước khi chạy, learner viết expected transition; sau khi chạy, họ đối chiếu raw artifact với oracle và giải thích mọi khác biệt thay vì sửa expected cho khớp output.

## Góc Khuất & Ngộ Nhận

build/probe rows/bytes, spill partitions, sort runs, output multiset và cost Với `wiki.de-foundation.hash-join-vs-sort-merge-join`, điểm phải khóa là evidence package và oracle; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

**Hiểu lầm:** Happy path chạy nhanh nghĩa là thiết kế đúng. **Thực tế:** build spill, skew hot key, duplicate cross product và bad estimates explode cost **Vì sao nghe hợp lý:** case nhỏ thường không chạm capacity, concurrency, failure hoặc version boundary.

**Hiểu lầm:** Tool hoặc API tự bảo đảm semantics. **Thực tế:** guarantee chỉ tồn tại trong scope và state đã công bố. **Vì sao nghe hợp lý:** syntax che mất protocol phía dưới.

## Nếu Bạn Dạy Lại Điều Này...

make build just exceed memory and pre-sort one input to force crossover Với `wiki.de-foundation.hash-join-vs-sort-merge-join`, điểm phải khóa là changed-constraint transfer; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hook dạy lại bắt đầu bằng một dự đoán dễ sai về `hash join và sort-merge join dưới memory/order constraints`. Bài tập seed đổi đúng một constraint, yêu cầu learner giữ hoặc đảo quyết định và chỉ ra evidence nào đủ mạnh để thuyết phục một reviewer không tham dự buổi học.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `Hash join against sort-merge join` là: build/probe rows/bytes, spill partitions, sort runs, output multiset và cost Mỗi probe nối input boundary với failure signal và oracle có thể bác bỏ kết luận.

### Probe 1: state transition và invariant

**Mệnh đề cần kiểm.** hash join builds partitions/table then probes; merge join advances sorted inputs and handles duplicate groups

**Thiết kế phép thử.** Với `wiki.de-foundation.hash-join-vs-sort-merge-join`, tạo positive và negative control chỉ khác một điều kiện; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề cần kiểm.** hash join suits equi-join and needs build memory/partition; merge join benefits existing order and supports ordered stream

**Thiết kế phép thử.** Với `wiki.de-foundation.hash-join-vs-sort-merge-join`, tạo boundary case ngay trước và sau ngưỡng; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề cần kiểm.** build spill, skew hot key, duplicate cross product và bad estimates explode cost

**Thiết kế phép thử.** Với `wiki.de-foundation.hash-join-vs-sort-merge-join`, tạo replay cùng identity với state khác; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** choose from predicate, input order, sizes, skew, memory and downstream order; benchmark both at boundary

**Thiết kế phép thử.** Với `wiki.de-foundation.hash-join-vs-sort-merge-join`, tạo failure inject trước và sau durable transition; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề cần kiểm.** build/probe rows/bytes, spill partitions, sort runs, output multiset và cost

**Thiết kế phép thử.** Với `wiki.de-foundation.hash-join-vs-sort-merge-join`, tạo changed scale làm cost model đổi; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề cần kiểm.** make build just exceed memory and pre-sort one input to force crossover

**Thiết kế phép thử.** Với `wiki.de-foundation.hash-join-vs-sort-merge-join`, tạo adversarial order hoặc skew; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề cần kiểm.** hash join builds partitions/table then probes; merge join advances sorted inputs and handles duplicate groups

**Thiết kế phép thử.** Với `wiki.de-foundation.hash-join-vs-sort-merge-join`, tạo fresh environment không cache; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề cần kiểm.** hash join suits equi-join and needs build memory/partition; merge join benefits existing order and supports ordered stream

**Thiết kế phép thử.** Với `wiki.de-foundation.hash-join-vs-sort-merge-join`, tạo independent oracle không dùng chung implementation; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề cần kiểm.** build spill, skew hot key, duplicate cross product và bad estimates explode cost

**Thiết kế phép thử.** Với `wiki.de-foundation.hash-join-vs-sort-merge-join`, tạo partial progress rồi restart; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** choose from predicate, input order, sizes, skew, memory and downstream order; benchmark both at boundary

**Thiết kế phép thử.** Với `wiki.de-foundation.hash-join-vs-sort-merge-join`, tạo missing evidence phải abstain; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề cần kiểm.** build/probe rows/bytes, spill partitions, sort runs, output multiset và cost

**Thiết kế phép thử.** Với `wiki.de-foundation.hash-join-vs-sort-merge-join`, tạo reviewer tái hiện từ package; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề cần kiểm.** make build just exceed memory and pre-sort one input to force crossover

**Thiết kế phép thử.** Với `wiki.de-foundation.hash-join-vs-sort-merge-join`, tạo constraint đổi đủ để quyết định đảo; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên của `hash join và sort-merge join dưới memory/order constraints` nằm ở đâu?

<details><summary>Đáp án</summary>hash join suits equi-join and needs build memory/partition; merge join benefits existing order and supports ordered stream</details>

2. Failure nào dễ tạo kết quả xanh giả nhất?

<details><summary>Đáp án</summary>build spill, skew hot key, duplicate cross product và bad estimates explode cost</details>

3. Constraint nào khiến quyết định phải đảo?

<details><summary>Đáp án</summary>make build just exceed memory and pre-sort one input to force crossover</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `Hash join against sort-merge join` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Mọi kết luận phụ thuộc version, workload, operating system, interpreter/compiler hoặc hardware phải được kiểm lại trên target.
- Concept key `ck.de.hash-join-vs-sort-merge-join` đang ở trạng thái `proposed`; note không được tính là canonical registry coverage trước khi owner đăng ký key.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]] — `src.book.silberschatz-database-system-concepts.7e` | Chapter 15 PDF 1902–1955 | cơ chế và boundary liên quan trực tiếp tới `hash join và sort-merge join dưới memory/order constraints` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L040 |

## Key takeaways
- choose from predicate, input order, sizes, skew, memory and downstream order; benchmark both at boundary
- build/probe rows/bytes, spill partitions, sort runs, output multiset và cost
- `hash join và sort-merge join dưới memory/order constraints` chỉ có nghĩa trong scope, identity, state và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.
