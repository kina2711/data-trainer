# Phase 1: Engineering Foundation
# Module 1: Engineering Thinking, Git and Debugging
# Lesson 6: Recovering lost work - reflog, detached HEAD and bisect

## Mục tiêu bài học

**Năng lực cần chứng minh.** Phục hồi được việc đã mất trong ba tình huống, và định vị commit gây hồi quy bằng tìm kiếm chia đôi tự động.

**Điều kiện hoàn thành.** Phục hồi thành công cả ba tình huống có ghi chú, và chia đôi tự động chỉ đúng commit 4.


# Recovering lost work - reflog, detached HEAD and bisect

**Tóm tắt bản chất:** reflog ghi lịch sử cập nhật ref cục bộ; detached HEAD vẫn cho phép tạo commit; bisect thu hẹp khoảng good/bad theo graph Sai boundary ở `recovery của commit và khoanh vùng regression bằng graph Git` làm kết quả có vẻ đúng trong happy path nhưng không chịu được failure hoặc changed constraint.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, kiểm chứng và áp dụng recovery của commit và khoanh vùng regression bằng graph Git?

## Nỗi Đau & Động Lực

reflog ghi lịch sử cập nhật ref cục bộ; detached HEAD vẫn cho phép tạo commit; bisect thu hẹp khoảng good/bad theo graph Với `wiki.de-foundation.recovering-lost-work-reflog-detached-head-bisect`, điểm phải khóa là state transition và invariant; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Không có mô hình này, lỗi thường lộ ở consumer sau cùng: output sai, latency vọt, resource không được giải phóng hoặc lịch sử không còn tái hiện được. Chi phí thật của `Recovering lost work - reflog, detached HEAD and bisect` vì thế nằm ở thời gian chẩn đoán và phạm vi phục hồi, không nằm ở số dòng syntax.

## Cơ Chế Tác Động

khả năng phục hồi phụ thuộc reachability, reflog retention, garbage collection và việc có backup ref trước mutation Với `wiki.de-foundation.recovering-lost-work-reflog-detached-head-bisect`, điểm phải khóa là identity, ownership và boundary; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hãy tách declared state, executed state và published state của `recovery của commit và khoanh vùng regression bằng graph Git`. Một command thành công chỉ là executed signal; muốn kết luận cần đối soát consumer-visible invariant và trạng thái còn lại sau restart hoặc replay.

## Bản Đồ Quyết Định

checkout/reset vội có thể làm commit mới không còn tên; test nondeterministic làm bisect kết luận sai Với `wiki.de-foundation.recovering-lost-work-reflog-detached-head-bisect`, điểm phải khóa là failure path và recovery; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Quy tắc mặc định cho `Recovering lost work - reflog, detached HEAD and bisect` là chọn phương án đơn giản nhất qua được hard constraints, rồi ghi rõ điều kiện đảo. Bảng quyết định tối thiểu gồm workload, identity, state owner, time/memory budget, failure domain và khả năng rollback.

## Case Study Thực Chiến: Recovering lost work - reflog, detached HEAD and bisect

tạo rescue branch trước, xác nhận object còn tồn tại, rồi chọn reflog, fsck hoặc bisect theo failure Với `wiki.de-foundation.recovering-lost-work-reflog-detached-head-bisect`, điểm phải khóa là decision trade-off và reversal trigger; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Case dùng fixture nhỏ nhưng phải giữ cơ chế chi phối. Trước khi chạy, learner viết expected transition; sau khi chạy, họ đối chiếu raw artifact với oracle và giải thích mọi khác biệt thay vì sửa expected cho khớp output.

## Góc Khuất & Ngộ Nhận

giữ graph, ref log, good/bad oracle, commit IDs và lệnh phục hồi Với `wiki.de-foundation.recovering-lost-work-reflog-detached-head-bisect`, điểm phải khóa là evidence package và oracle; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

**Hiểu lầm:** Happy path chạy nhanh nghĩa là thiết kế đúng. **Thực tế:** checkout/reset vội có thể làm commit mới không còn tên; test nondeterministic làm bisect kết luận sai **Vì sao nghe hợp lý:** case nhỏ thường không chạm capacity, concurrency, failure hoặc version boundary.

**Hiểu lầm:** Tool hoặc API tự bảo đảm semantics. **Thực tế:** guarantee chỉ tồn tại trong scope và state đã công bố. **Vì sao nghe hợp lý:** syntax che mất protocol phía dưới.

## Nếu Bạn Dạy Lại Điều Này...

xóa branch, tạo detached commit và inject một regression rồi phục hồi trên clone sandbox Với `wiki.de-foundation.recovering-lost-work-reflog-detached-head-bisect`, điểm phải khóa là changed-constraint transfer; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hook dạy lại bắt đầu bằng một dự đoán dễ sai về `recovery của commit và khoanh vùng regression bằng graph Git`. Bài tập seed đổi đúng một constraint, yêu cầu learner giữ hoặc đảo quyết định và chỉ ra evidence nào đủ mạnh để thuyết phục một reviewer không tham dự buổi học.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `Recovering lost work - reflog, detached HEAD and bisect` là: giữ graph, ref log, good/bad oracle, commit IDs và lệnh phục hồi Mỗi probe nối input boundary với failure signal và oracle có thể bác bỏ kết luận.

### Probe 1: state transition và invariant

**Mệnh đề cần kiểm.** reflog ghi lịch sử cập nhật ref cục bộ; detached HEAD vẫn cho phép tạo commit; bisect thu hẹp khoảng good/bad theo graph

**Thiết kế phép thử.** Với `wiki.de-foundation.recovering-lost-work-reflog-detached-head-bisect`, tạo positive và negative control chỉ khác một điều kiện; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề cần kiểm.** khả năng phục hồi phụ thuộc reachability, reflog retention, garbage collection và việc có backup ref trước mutation

**Thiết kế phép thử.** Với `wiki.de-foundation.recovering-lost-work-reflog-detached-head-bisect`, tạo boundary case ngay trước và sau ngưỡng; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề cần kiểm.** checkout/reset vội có thể làm commit mới không còn tên; test nondeterministic làm bisect kết luận sai

**Thiết kế phép thử.** Với `wiki.de-foundation.recovering-lost-work-reflog-detached-head-bisect`, tạo replay cùng identity với state khác; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** tạo rescue branch trước, xác nhận object còn tồn tại, rồi chọn reflog, fsck hoặc bisect theo failure

**Thiết kế phép thử.** Với `wiki.de-foundation.recovering-lost-work-reflog-detached-head-bisect`, tạo failure inject trước và sau durable transition; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề cần kiểm.** giữ graph, ref log, good/bad oracle, commit IDs và lệnh phục hồi

**Thiết kế phép thử.** Với `wiki.de-foundation.recovering-lost-work-reflog-detached-head-bisect`, tạo changed scale làm cost model đổi; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề cần kiểm.** xóa branch, tạo detached commit và inject một regression rồi phục hồi trên clone sandbox

**Thiết kế phép thử.** Với `wiki.de-foundation.recovering-lost-work-reflog-detached-head-bisect`, tạo adversarial order hoặc skew; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề cần kiểm.** reflog ghi lịch sử cập nhật ref cục bộ; detached HEAD vẫn cho phép tạo commit; bisect thu hẹp khoảng good/bad theo graph

**Thiết kế phép thử.** Với `wiki.de-foundation.recovering-lost-work-reflog-detached-head-bisect`, tạo fresh environment không cache; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề cần kiểm.** khả năng phục hồi phụ thuộc reachability, reflog retention, garbage collection và việc có backup ref trước mutation

**Thiết kế phép thử.** Với `wiki.de-foundation.recovering-lost-work-reflog-detached-head-bisect`, tạo independent oracle không dùng chung implementation; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề cần kiểm.** checkout/reset vội có thể làm commit mới không còn tên; test nondeterministic làm bisect kết luận sai

**Thiết kế phép thử.** Với `wiki.de-foundation.recovering-lost-work-reflog-detached-head-bisect`, tạo partial progress rồi restart; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** tạo rescue branch trước, xác nhận object còn tồn tại, rồi chọn reflog, fsck hoặc bisect theo failure

**Thiết kế phép thử.** Với `wiki.de-foundation.recovering-lost-work-reflog-detached-head-bisect`, tạo missing evidence phải abstain; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề cần kiểm.** giữ graph, ref log, good/bad oracle, commit IDs và lệnh phục hồi

**Thiết kế phép thử.** Với `wiki.de-foundation.recovering-lost-work-reflog-detached-head-bisect`, tạo reviewer tái hiện từ package; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề cần kiểm.** xóa branch, tạo detached commit và inject một regression rồi phục hồi trên clone sandbox

**Thiết kế phép thử.** Với `wiki.de-foundation.recovering-lost-work-reflog-detached-head-bisect`, tạo constraint đổi đủ để quyết định đảo; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên của `recovery của commit và khoanh vùng regression bằng graph Git` nằm ở đâu?

<details><summary>Đáp án</summary>khả năng phục hồi phụ thuộc reachability, reflog retention, garbage collection và việc có backup ref trước mutation</details>

2. Failure nào dễ tạo kết quả xanh giả nhất?

<details><summary>Đáp án</summary>checkout/reset vội có thể làm commit mới không còn tên; test nondeterministic làm bisect kết luận sai</details>

3. Constraint nào khiến quyết định phải đảo?

<details><summary>Đáp án</summary>xóa branch, tạo detached commit và inject một regression rồi phục hồi trên clone sandbox</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `Recovering lost work - reflog, detached HEAD and bisect` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Mọi kết luận phụ thuộc version, workload, operating system, interpreter/compiler hoặc hardware phải được kiểm lại trên target.
- Concept key `ck.de.recovering-lost-work-reflog-detached-head-bisect` đang ở trạng thái `proposed`; note không được tính là canonical registry coverage trước khi owner đăng ký key.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-CHACON-STRAUB-PRO-GIT-2E]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-CHACON-STRAUB-PRO-GIT-2E]] — `src.book.chacon-straub-pro-git.2e` | Chapter 3 PDF 129–174; Chapter 7 PDF 422–434; Chapter 10 PDF 762–790 | cơ chế và boundary liên quan trực tiếp tới `recovery của commit và khoanh vùng regression bằng graph Git` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L006 |

## Key takeaways
- tạo rescue branch trước, xác nhận object còn tồn tại, rồi chọn reflog, fsck hoặc bisect theo failure
- giữ graph, ref log, good/bad oracle, commit IDs và lệnh phục hồi
- `recovery của commit và khoanh vùng regression bằng graph Git` chỉ có nghĩa trong scope, identity, state và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.
