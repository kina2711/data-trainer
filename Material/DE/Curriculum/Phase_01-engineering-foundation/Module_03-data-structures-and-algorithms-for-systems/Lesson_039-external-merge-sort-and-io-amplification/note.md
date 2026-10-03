# Phase 1: Engineering Foundation
# Module 3: Data Structures and Algorithms for Systems
# Lesson 39: External merge sort and IO amplification

## Mục tiêu bài học

**Năng lực cần chứng minh.** Cài sắp xếp ngoài với ngân sách bộ nhớ nhỏ hơn dữ liệu, và đo được quan hệ giữa bộ nhớ cấp và hệ số khuếch đại vào ra.

**Điều kiện hoàn thành.** Kết quả sắp xếp đúng ở cả ba mức bộ nhớ, và hệ số khuếch đại vào ra giảm khi tăng bộ nhớ có số chứng minh.


# External merge sort and IO amplification

**Tóm tắt bản chất:** generate sorted runs fitting memory, spill, then multiway merge; fan-in/buffers determine passes and I/O Sai boundary ở `external merge sort under bounded memory` làm kết quả có vẻ đúng trong happy path nhưng không chịu được failure hoặc changed constraint.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, kiểm chứng và áp dụng external merge sort under bounded memory?

## Nỗi Đau & Động Lực

generate sorted runs fitting memory, spill, then multiway merge; fan-in/buffers determine passes and I/O Với `wiki.de-foundation.external-merge-sort-io-amplification`, điểm phải khóa là state transition và invariant; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Không có mô hình này, lỗi thường lộ ở consumer sau cùng: output sai, latency vọt, resource không được giải phóng hoặc lịch sử không còn tái hiện được. Chi phí thật của `External merge sort and IO amplification` vì thế nằm ở thời gian chẩn đoán và phạm vi phục hồi, không nằm ở số dòng syntax.

## Cơ Chế Tác Động

cost counts bytes/blocks and passes, not comparisons alone; temp storage and file count are operational limits Với `wiki.de-foundation.external-merge-sort-io-amplification`, điểm phải khóa là identity, ownership và boundary; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hãy tách declared state, executed state và published state của `external merge sort under bounded memory`. Một command thành công chỉ là executed signal; muốn kết luận cần đối soát consumer-visible invariant và trạng thái còn lại sau restart hoặc replay.

## Bản Đồ Quyết Định

too many tiny runs, insufficient disk, skewed records and retry leave orphan spills Với `wiki.de-foundation.external-merge-sort-io-amplification`, điểm phải khóa là failure path và recovery; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Quy tắc mặc định cho `External merge sort and IO amplification` là chọn phương án đơn giản nhất qua được hard constraints, rồi ghi rõ điều kiện đảo. Bảng quyết định tối thiểu gồm workload, identity, state owner, time/memory budget, failure domain và khả năng rollback.

## Case Study Thực Chiến: External merge sort and IO amplification

use external sort when full order exceeds memory; exploit pre-order/partition if it removes passes Với `wiki.de-foundation.external-merge-sort-io-amplification`, điểm phải khóa là decision trade-off và reversal trigger; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Case dùng fixture nhỏ nhưng phải giữ cơ chế chi phối. Trước khi chạy, learner viết expected transition; sau khi chạy, họ đối chiếu raw artifact với oracle và giải thích mọi khác biệt thay vì sửa expected cho khớp output.

## Góc Khuất & Ngộ Nhận

run sizes/count, bytes read/written, passes, temp peak, throughput and output-order oracle Với `wiki.de-foundation.external-merge-sort-io-amplification`, điểm phải khóa là evidence package và oracle; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

**Hiểu lầm:** Happy path chạy nhanh nghĩa là thiết kế đúng. **Thực tế:** too many tiny runs, insufficient disk, skewed records and retry leave orphan spills **Vì sao nghe hợp lý:** case nhỏ thường không chạm capacity, concurrency, failure hoặc version boundary.

**Hiểu lầm:** Tool hoặc API tự bảo đảm semantics. **Thực tế:** guarantee chỉ tồn tại trong scope và state đã công bố. **Vì sao nghe hợp lý:** syntax che mất protocol phía dưới.

## Nếu Bạn Dạy Lại Điều Này...

halve memory and vary fan-in to predict extra pass before run Với `wiki.de-foundation.external-merge-sort-io-amplification`, điểm phải khóa là changed-constraint transfer; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hook dạy lại bắt đầu bằng một dự đoán dễ sai về `external merge sort under bounded memory`. Bài tập seed đổi đúng một constraint, yêu cầu learner giữ hoặc đảo quyết định và chỉ ra evidence nào đủ mạnh để thuyết phục một reviewer không tham dự buổi học.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `External merge sort and IO amplification` là: run sizes/count, bytes read/written, passes, temp peak, throughput and output-order oracle Mỗi probe nối input boundary với failure signal và oracle có thể bác bỏ kết luận.

### Probe 1: state transition và invariant

**Mệnh đề cần kiểm.** generate sorted runs fitting memory, spill, then multiway merge; fan-in/buffers determine passes and I/O

**Thiết kế phép thử.** Với `wiki.de-foundation.external-merge-sort-io-amplification`, tạo positive và negative control chỉ khác một điều kiện; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề cần kiểm.** cost counts bytes/blocks and passes, not comparisons alone; temp storage and file count are operational limits

**Thiết kế phép thử.** Với `wiki.de-foundation.external-merge-sort-io-amplification`, tạo boundary case ngay trước và sau ngưỡng; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề cần kiểm.** too many tiny runs, insufficient disk, skewed records and retry leave orphan spills

**Thiết kế phép thử.** Với `wiki.de-foundation.external-merge-sort-io-amplification`, tạo replay cùng identity với state khác; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** use external sort when full order exceeds memory; exploit pre-order/partition if it removes passes

**Thiết kế phép thử.** Với `wiki.de-foundation.external-merge-sort-io-amplification`, tạo failure inject trước và sau durable transition; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề cần kiểm.** run sizes/count, bytes read/written, passes, temp peak, throughput and output-order oracle

**Thiết kế phép thử.** Với `wiki.de-foundation.external-merge-sort-io-amplification`, tạo changed scale làm cost model đổi; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề cần kiểm.** halve memory and vary fan-in to predict extra pass before run

**Thiết kế phép thử.** Với `wiki.de-foundation.external-merge-sort-io-amplification`, tạo adversarial order hoặc skew; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề cần kiểm.** generate sorted runs fitting memory, spill, then multiway merge; fan-in/buffers determine passes and I/O

**Thiết kế phép thử.** Với `wiki.de-foundation.external-merge-sort-io-amplification`, tạo fresh environment không cache; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề cần kiểm.** cost counts bytes/blocks and passes, not comparisons alone; temp storage and file count are operational limits

**Thiết kế phép thử.** Với `wiki.de-foundation.external-merge-sort-io-amplification`, tạo independent oracle không dùng chung implementation; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề cần kiểm.** too many tiny runs, insufficient disk, skewed records and retry leave orphan spills

**Thiết kế phép thử.** Với `wiki.de-foundation.external-merge-sort-io-amplification`, tạo partial progress rồi restart; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** use external sort when full order exceeds memory; exploit pre-order/partition if it removes passes

**Thiết kế phép thử.** Với `wiki.de-foundation.external-merge-sort-io-amplification`, tạo missing evidence phải abstain; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề cần kiểm.** run sizes/count, bytes read/written, passes, temp peak, throughput and output-order oracle

**Thiết kế phép thử.** Với `wiki.de-foundation.external-merge-sort-io-amplification`, tạo reviewer tái hiện từ package; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề cần kiểm.** halve memory and vary fan-in to predict extra pass before run

**Thiết kế phép thử.** Với `wiki.de-foundation.external-merge-sort-io-amplification`, tạo constraint đổi đủ để quyết định đảo; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên của `external merge sort under bounded memory` nằm ở đâu?

<details><summary>Đáp án</summary>cost counts bytes/blocks and passes, not comparisons alone; temp storage and file count are operational limits</details>

2. Failure nào dễ tạo kết quả xanh giả nhất?

<details><summary>Đáp án</summary>too many tiny runs, insufficient disk, skewed records and retry leave orphan spills</details>

3. Constraint nào khiến quyết định phải đảo?

<details><summary>Đáp án</summary>halve memory and vary fan-in to predict extra pass before run</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `External merge sort and IO amplification` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Mọi kết luận phụ thuộc version, workload, operating system, interpreter/compiler hoặc hardware phải được kiểm lại trên target.
- Concept key `ck.de.external-merge-sort-io-amplification` đang ở trạng thái `proposed`; note không được tính là canonical registry coverage trước khi owner đăng ký key.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-SEDGEWICK-WAYNE-ALGORITHMS-4E]]
2. [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-SEDGEWICK-WAYNE-ALGORITHMS-4E]] — `src.book.sedgewick-wayne-algorithms.4e` | Sections 1.4, 2.2, 2.4, 3.2–3.4, 4.1–4.2; PDF 185–604 | cơ chế và boundary liên quan trực tiếp tới `external merge sort under bounded memory` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L039 |
| [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]] — `src.book.silberschatz-database-system-concepts.7e` | Chapter 15 PDF 1902–1955 | cơ chế và boundary liên quan trực tiếp tới `external merge sort under bounded memory` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L039 |

## Key takeaways
- use external sort when full order exceeds memory; exploit pre-order/partition if it removes passes
- run sizes/count, bytes read/written, passes, temp peak, throughput and output-order oracle
- `external merge sort under bounded memory` chỉ có nghĩa trong scope, identity, state và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.
