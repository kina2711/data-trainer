# Phase 1: Engineering Foundation
# Module 2: Python for Production
# Lesson 27: End-to-end deadlines and backpressure

## Mục tiêu bài học

**Năng lực cần chứng minh.** Cài truyền hạn chót đầu cuối và áp lực ngược, chứng minh yêu cầu không vượt ngân sách và bể không bị cạn.

**Điều kiện hoàn thành.** Phân vị 99 của thời gian yêu cầu nằm trong ngân sách hạn chót, và không lần nào bể kết nối cạn dưới tải.


# End-to-end deadlines and backpressure

**Tóm tắt bản chất:** deadline là absolute budget truyền xuống; backpressure giới hạn admission/queue; timeout từng hop phải nằm trong remaining budget Sai boundary ở `end-to-end deadline và backpressure qua nhiều queue/call` làm kết quả có vẻ đúng trong happy path nhưng không chịu được failure hoặc changed constraint.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, kiểm chứng và áp dụng end-to-end deadline và backpressure qua nhiều queue/call?

## Nỗi Đau & Động Lực

deadline là absolute budget truyền xuống; backpressure giới hạn admission/queue; timeout từng hop phải nằm trong remaining budget Với `wiki.de-foundation.end-to-end-deadlines-backpressure`, điểm phải khóa là state transition và invariant; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Không có mô hình này, lỗi thường lộ ở consumer sau cùng: output sai, latency vọt, resource không được giải phóng hoặc lịch sử không còn tái hiện được. Chi phí thật của `End-to-end deadlines and backpressure` vì thế nằm ở thời gian chẩn đoán và phạm vi phục hồi, không nằm ở số dòng syntax.

## Cơ Chế Tác Động

retry tiêu budget; queue wait tính vào latency; semaphore chỉ giới hạn concurrency chứ không giới hạn backlog Với `wiki.de-foundation.end-to-end-deadlines-backpressure`, điểm phải khóa là identity, ownership và boundary; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hãy tách declared state, executed state và published state của `end-to-end deadline và backpressure qua nhiều queue/call`. Một command thành công chỉ là executed signal; muốn kết luận cần đối soát consumer-visible invariant và trạng thái còn lại sau restart hoặc replay.

## Bản Đồ Quyết Định

unbounded queue biến overload thành memory/latency; timeout reset mỗi hop vượt user deadline Với `wiki.de-foundation.end-to-end-deadlines-backpressure`, điểm phải khóa là failure path và recovery; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Quy tắc mặc định cho `End-to-end deadlines and backpressure` là chọn phương án đơn giản nhất qua được hard constraints, rồi ghi rõ điều kiện đảo. Bảng quyết định tối thiểu gồm workload, identity, state owner, time/memory budget, failure domain và khả năng rollback.

## Case Study Thực Chiến: End-to-end deadlines and backpressure

set capacity từ service time/arrival và harm; reject/degrade sớm khi không còn budget Với `wiki.de-foundation.end-to-end-deadlines-backpressure`, điểm phải khóa là decision trade-off và reversal trigger; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Case dùng fixture nhỏ nhưng phải giữ cơ chế chi phối. Trước khi chạy, learner viết expected transition; sau khi chạy, họ đối chiếu raw artifact với oracle và giải thích mọi khác biệt thay vì sửa expected cho khớp output.

## Góc Khuất & Ngộ Nhận

queue depth/age, admission, remaining deadline, completions và drops by reason Với `wiki.de-foundation.end-to-end-deadlines-backpressure`, điểm phải khóa là evidence package và oracle; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

**Hiểu lầm:** Happy path chạy nhanh nghĩa là thiết kế đúng. **Thực tế:** unbounded queue biến overload thành memory/latency; timeout reset mỗi hop vượt user deadline **Vì sao nghe hợp lý:** case nhỏ thường không chạm capacity, concurrency, failure hoặc version boundary.

**Hiểu lầm:** Tool hoặc API tự bảo đảm semantics. **Thực tế:** guarantee chỉ tồn tại trong scope và state đã công bố. **Vì sao nghe hợp lý:** syntax che mất protocol phía dưới.

## Nếu Bạn Dạy Lại Điều Này...

tăng arrival vượt capacity rồi kiểm bounded memory và predictable rejection Với `wiki.de-foundation.end-to-end-deadlines-backpressure`, điểm phải khóa là changed-constraint transfer; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hook dạy lại bắt đầu bằng một dự đoán dễ sai về `end-to-end deadline và backpressure qua nhiều queue/call`. Bài tập seed đổi đúng một constraint, yêu cầu learner giữ hoặc đảo quyết định và chỉ ra evidence nào đủ mạnh để thuyết phục một reviewer không tham dự buổi học.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `End-to-end deadlines and backpressure` là: queue depth/age, admission, remaining deadline, completions và drops by reason Mỗi probe nối input boundary với failure signal và oracle có thể bác bỏ kết luận.

### Probe 1: state transition và invariant

**Mệnh đề cần kiểm.** deadline là absolute budget truyền xuống; backpressure giới hạn admission/queue; timeout từng hop phải nằm trong remaining budget

**Thiết kế phép thử.** Với `wiki.de-foundation.end-to-end-deadlines-backpressure`, tạo positive và negative control chỉ khác một điều kiện; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề cần kiểm.** retry tiêu budget; queue wait tính vào latency; semaphore chỉ giới hạn concurrency chứ không giới hạn backlog

**Thiết kế phép thử.** Với `wiki.de-foundation.end-to-end-deadlines-backpressure`, tạo boundary case ngay trước và sau ngưỡng; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề cần kiểm.** unbounded queue biến overload thành memory/latency; timeout reset mỗi hop vượt user deadline

**Thiết kế phép thử.** Với `wiki.de-foundation.end-to-end-deadlines-backpressure`, tạo replay cùng identity với state khác; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** set capacity từ service time/arrival và harm; reject/degrade sớm khi không còn budget

**Thiết kế phép thử.** Với `wiki.de-foundation.end-to-end-deadlines-backpressure`, tạo failure inject trước và sau durable transition; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề cần kiểm.** queue depth/age, admission, remaining deadline, completions và drops by reason

**Thiết kế phép thử.** Với `wiki.de-foundation.end-to-end-deadlines-backpressure`, tạo changed scale làm cost model đổi; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề cần kiểm.** tăng arrival vượt capacity rồi kiểm bounded memory và predictable rejection

**Thiết kế phép thử.** Với `wiki.de-foundation.end-to-end-deadlines-backpressure`, tạo adversarial order hoặc skew; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề cần kiểm.** deadline là absolute budget truyền xuống; backpressure giới hạn admission/queue; timeout từng hop phải nằm trong remaining budget

**Thiết kế phép thử.** Với `wiki.de-foundation.end-to-end-deadlines-backpressure`, tạo fresh environment không cache; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề cần kiểm.** retry tiêu budget; queue wait tính vào latency; semaphore chỉ giới hạn concurrency chứ không giới hạn backlog

**Thiết kế phép thử.** Với `wiki.de-foundation.end-to-end-deadlines-backpressure`, tạo independent oracle không dùng chung implementation; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề cần kiểm.** unbounded queue biến overload thành memory/latency; timeout reset mỗi hop vượt user deadline

**Thiết kế phép thử.** Với `wiki.de-foundation.end-to-end-deadlines-backpressure`, tạo partial progress rồi restart; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** set capacity từ service time/arrival và harm; reject/degrade sớm khi không còn budget

**Thiết kế phép thử.** Với `wiki.de-foundation.end-to-end-deadlines-backpressure`, tạo missing evidence phải abstain; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề cần kiểm.** queue depth/age, admission, remaining deadline, completions và drops by reason

**Thiết kế phép thử.** Với `wiki.de-foundation.end-to-end-deadlines-backpressure`, tạo reviewer tái hiện từ package; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề cần kiểm.** tăng arrival vượt capacity rồi kiểm bounded memory và predictable rejection

**Thiết kế phép thử.** Với `wiki.de-foundation.end-to-end-deadlines-backpressure`, tạo constraint đổi đủ để quyết định đảo; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên của `end-to-end deadline và backpressure qua nhiều queue/call` nằm ở đâu?

<details><summary>Đáp án</summary>retry tiêu budget; queue wait tính vào latency; semaphore chỉ giới hạn concurrency chứ không giới hạn backlog</details>

2. Failure nào dễ tạo kết quả xanh giả nhất?

<details><summary>Đáp án</summary>unbounded queue biến overload thành memory/latency; timeout reset mỗi hop vượt user deadline</details>

3. Constraint nào khiến quyết định phải đảo?

<details><summary>Đáp án</summary>tăng arrival vượt capacity rồi kiểm bounded memory và predictable rejection</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `End-to-end deadlines and backpressure` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Mọi kết luận phụ thuộc version, workload, operating system, interpreter/compiler hoặc hardware phải được kiểm lại trên target.
- Concept key `ck.de.end-to-end-deadlines-backpressure` đang ở trạng thái `proposed`; note không được tính là canonical registry coverage trước khi owner đăng ký key.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-PYTHON-314-STDLIB-RUNTIME]]
2. [[SRC-GOOGLE-SRE-MONITORING]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-PYTHON-314-STDLIB-RUNTIME]] — `src.docs.python-3.14-stdlib-runtime` | Python 3.14.8 Library Reference; accessed 2026-10-02 | cơ chế và boundary liên quan trực tiếp tới `end-to-end deadline và backpressure qua nhiều queue/call` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L027 |
| [[SRC-GOOGLE-SRE-MONITORING]] — `src.web.google-sre-monitoring` | Monitoring distributed systems; accessed 2026-10-01 | cơ chế và boundary liên quan trực tiếp tới `end-to-end deadline và backpressure qua nhiều queue/call` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L027 |

## Key takeaways
- set capacity từ service time/arrival và harm; reject/degrade sớm khi không còn budget
- queue depth/age, admission, remaining deadline, completions và drops by reason
- `end-to-end deadline và backpressure qua nhiều queue/call` chỉ có nghĩa trong scope, identity, state và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.
