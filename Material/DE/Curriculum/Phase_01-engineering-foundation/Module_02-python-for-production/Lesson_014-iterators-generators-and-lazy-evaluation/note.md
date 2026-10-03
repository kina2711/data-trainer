# Phase 1: Engineering Foundation
# Module 2: Python for Production
# Lesson 14: Iterators, generators and lazy evaluation

## Mục tiêu bài học

**Năng lực cần chứng minh.** Viết lại một đoạn xử lý nạp toàn bộ thành dạng dòng chảy, và chứng minh bằng số đo rằng bộ nhớ không tăng theo kích thước đầu vào.

**Điều kiện hoàn thành.** Bản dòng chảy giữ bộ nhớ đỉnh gần như không đổi qua cả ba kích thước, trong khi bản nạp toàn bộ tăng tuyến tính.


# Iterators, generators and lazy evaluation

**Tóm tắt bản chất:** iterable tạo iterator; next tiến state tới value hoặc StopIteration; generator giữ frame và resume tại yield Sai boundary ở `iterator protocol, generator suspension và lazy evaluation` làm kết quả có vẻ đúng trong happy path nhưng không chịu được failure hoặc changed constraint.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, kiểm chứng và áp dụng iterator protocol, generator suspension và lazy evaluation?

## Nỗi Đau & Động Lực

iterable tạo iterator; next tiến state tới value hoặc StopIteration; generator giữ frame và resume tại yield Với `wiki.de-foundation.iterators-generators-lazy-evaluation`, điểm phải khóa là state transition và invariant; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Không có mô hình này, lỗi thường lộ ở consumer sau cùng: output sai, latency vọt, resource không được giải phóng hoặc lịch sử không còn tái hiện được. Chi phí thật của `Iterators, generators and lazy evaluation` vì thế nằm ở thời gian chẩn đoán và phạm vi phục hồi, không nằm ở số dòng syntax.

## Cơ Chế Tác Động

lazy đổi thời điểm lỗi, resource lifetime và side effect; iterator thường one-shot chứ không phải collection tái dùng Với `wiki.de-foundation.iterators-generators-lazy-evaluation`, điểm phải khóa là identity, ownership và boundary; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hãy tách declared state, executed state và published state của `iterator protocol, generator suspension và lazy evaluation`. Một command thành công chỉ là executed signal; muốn kết luận cần đối soát consumer-visible invariant và trạng thái còn lại sau restart hoặc replay.

## Bản Đồ Quyết Định

iterate lần hai được zero rows; giữ file mở quá lâu; exception xuất hiện xa call site Với `wiki.de-foundation.iterators-generators-lazy-evaluation`, điểm phải khóa là failure path và recovery; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Quy tắc mặc định cho `Iterators, generators and lazy evaluation` là chọn phương án đơn giản nhất qua được hard constraints, rồi ghi rõ điều kiện đảo. Bảng quyết định tối thiểu gồm workload, identity, state owner, time/memory budget, failure domain và khả năng rollback.

## Case Study Thực Chiến: Iterators, generators and lazy evaluation

dùng lazy khi bounded memory/streaming có lợi và ownership/lifetime rõ; materialize khi cần replay hoặc snapshot Với `wiki.de-foundation.iterators-generators-lazy-evaluation`, điểm phải khóa là decision trade-off và reversal trigger; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Case dùng fixture nhỏ nhưng phải giữ cơ chế chi phối. Trước khi chạy, learner viết expected transition; sau khi chạy, họ đối chiếu raw artifact với oracle và giải thích mọi khác biệt thay vì sửa expected cho khớp output.

## Góc Khuất & Ngộ Nhận

đếm pulls, peak memory, close/finalization và output order trên fixture Với `wiki.de-foundation.iterators-generators-lazy-evaluation`, điểm phải khóa là evidence package và oracle; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

**Hiểu lầm:** Happy path chạy nhanh nghĩa là thiết kế đúng. **Thực tế:** iterate lần hai được zero rows; giữ file mở quá lâu; exception xuất hiện xa call site **Vì sao nghe hợp lý:** case nhỏ thường không chạm capacity, concurrency, failure hoặc version boundary.

**Hiểu lầm:** Tool hoặc API tự bảo đảm semantics. **Thực tế:** guarantee chỉ tồn tại trong scope và state đã công bố. **Vì sao nghe hợp lý:** syntax che mất protocol phía dưới.

## Nếu Bạn Dạy Lại Điều Này...

consume partial, break sớm rồi kiểm cleanup và khả năng replay Với `wiki.de-foundation.iterators-generators-lazy-evaluation`, điểm phải khóa là changed-constraint transfer; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hook dạy lại bắt đầu bằng một dự đoán dễ sai về `iterator protocol, generator suspension và lazy evaluation`. Bài tập seed đổi đúng một constraint, yêu cầu learner giữ hoặc đảo quyết định và chỉ ra evidence nào đủ mạnh để thuyết phục một reviewer không tham dự buổi học.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `Iterators, generators and lazy evaluation` là: đếm pulls, peak memory, close/finalization và output order trên fixture Mỗi probe nối input boundary với failure signal và oracle có thể bác bỏ kết luận.

### Probe 1: state transition và invariant

**Mệnh đề cần kiểm.** iterable tạo iterator; next tiến state tới value hoặc StopIteration; generator giữ frame và resume tại yield

**Thiết kế phép thử.** Với `wiki.de-foundation.iterators-generators-lazy-evaluation`, tạo positive và negative control chỉ khác một điều kiện; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề cần kiểm.** lazy đổi thời điểm lỗi, resource lifetime và side effect; iterator thường one-shot chứ không phải collection tái dùng

**Thiết kế phép thử.** Với `wiki.de-foundation.iterators-generators-lazy-evaluation`, tạo boundary case ngay trước và sau ngưỡng; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề cần kiểm.** iterate lần hai được zero rows; giữ file mở quá lâu; exception xuất hiện xa call site

**Thiết kế phép thử.** Với `wiki.de-foundation.iterators-generators-lazy-evaluation`, tạo replay cùng identity với state khác; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** dùng lazy khi bounded memory/streaming có lợi và ownership/lifetime rõ; materialize khi cần replay hoặc snapshot

**Thiết kế phép thử.** Với `wiki.de-foundation.iterators-generators-lazy-evaluation`, tạo failure inject trước và sau durable transition; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề cần kiểm.** đếm pulls, peak memory, close/finalization và output order trên fixture

**Thiết kế phép thử.** Với `wiki.de-foundation.iterators-generators-lazy-evaluation`, tạo changed scale làm cost model đổi; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề cần kiểm.** consume partial, break sớm rồi kiểm cleanup và khả năng replay

**Thiết kế phép thử.** Với `wiki.de-foundation.iterators-generators-lazy-evaluation`, tạo adversarial order hoặc skew; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề cần kiểm.** iterable tạo iterator; next tiến state tới value hoặc StopIteration; generator giữ frame và resume tại yield

**Thiết kế phép thử.** Với `wiki.de-foundation.iterators-generators-lazy-evaluation`, tạo fresh environment không cache; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề cần kiểm.** lazy đổi thời điểm lỗi, resource lifetime và side effect; iterator thường one-shot chứ không phải collection tái dùng

**Thiết kế phép thử.** Với `wiki.de-foundation.iterators-generators-lazy-evaluation`, tạo independent oracle không dùng chung implementation; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề cần kiểm.** iterate lần hai được zero rows; giữ file mở quá lâu; exception xuất hiện xa call site

**Thiết kế phép thử.** Với `wiki.de-foundation.iterators-generators-lazy-evaluation`, tạo partial progress rồi restart; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** dùng lazy khi bounded memory/streaming có lợi và ownership/lifetime rõ; materialize khi cần replay hoặc snapshot

**Thiết kế phép thử.** Với `wiki.de-foundation.iterators-generators-lazy-evaluation`, tạo missing evidence phải abstain; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề cần kiểm.** đếm pulls, peak memory, close/finalization và output order trên fixture

**Thiết kế phép thử.** Với `wiki.de-foundation.iterators-generators-lazy-evaluation`, tạo reviewer tái hiện từ package; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề cần kiểm.** consume partial, break sớm rồi kiểm cleanup và khả năng replay

**Thiết kế phép thử.** Với `wiki.de-foundation.iterators-generators-lazy-evaluation`, tạo constraint đổi đủ để quyết định đảo; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên của `iterator protocol, generator suspension và lazy evaluation` nằm ở đâu?

<details><summary>Đáp án</summary>lazy đổi thời điểm lỗi, resource lifetime và side effect; iterator thường one-shot chứ không phải collection tái dùng</details>

2. Failure nào dễ tạo kết quả xanh giả nhất?

<details><summary>Đáp án</summary>iterate lần hai được zero rows; giữ file mở quá lâu; exception xuất hiện xa call site</details>

3. Constraint nào khiến quyết định phải đảo?

<details><summary>Đáp án</summary>consume partial, break sớm rồi kiểm cleanup và khả năng replay</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `Iterators, generators and lazy evaluation` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Mọi kết luận phụ thuộc version, workload, operating system, interpreter/compiler hoặc hardware phải được kiểm lại trên target.
- Concept key `ck.de.iterators-generators-lazy-evaluation` đang ở trạng thái `proposed`; note không được tính là canonical registry coverage trước khi owner đăng ký key.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-PYTHON-314-LANGUAGE-REFERENCE]]
2. [[SRC-PYTHON-314-STDLIB-RUNTIME]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-PYTHON-314-LANGUAGE-REFERENCE]] — `src.docs.python-3.14-language-reference` | Python 3.14.8 Language Reference; accessed 2026-10-02 | cơ chế và boundary liên quan trực tiếp tới `iterator protocol, generator suspension và lazy evaluation` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L014 |
| [[SRC-PYTHON-314-STDLIB-RUNTIME]] — `src.docs.python-3.14-stdlib-runtime` | Python 3.14.8 Library Reference; accessed 2026-10-02 | cơ chế và boundary liên quan trực tiếp tới `iterator protocol, generator suspension và lazy evaluation` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L014 |

## Key takeaways
- dùng lazy khi bounded memory/streaming có lợi và ownership/lifetime rõ; materialize khi cần replay hoặc snapshot
- đếm pulls, peak memory, close/finalization và output order trên fixture
- `iterator protocol, generator suspension và lazy evaluation` chỉ có nghĩa trong scope, identity, state và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.
