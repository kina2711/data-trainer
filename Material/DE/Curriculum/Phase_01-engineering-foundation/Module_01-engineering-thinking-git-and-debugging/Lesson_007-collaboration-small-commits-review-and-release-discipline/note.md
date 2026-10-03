# Phase 1: Engineering Foundation
# Module 1: Engineering Thinking, Git and Debugging
# Lesson 7: Collaboration - small commits, review and release discipline

## Mục tiêu bài học

**Năng lực cần chứng minh.** Nộp một yêu cầu hợp nhất đủ bốn phần, rà soát yêu cầu của người khác bằng ba câu hỏi bắt buộc, và chỉ ra được một thay đổi mà lùi mã không đủ để lùi.

**Điều kiện hoàn thành.** Bốn commit đều một mục đích và có lý do, yêu cầu hợp nhất đủ bốn phần, bản rà soát nêu được ít nhất một rủi ro thật, và phép thử lùi chỉ ra đúng chỗ lùi mã không đủ với kế hoạch tương thích làm lần lùi thứ hai thành công.


# Collaboration - small commits, review and release discipline

**Tóm tắt bản chất:** commit nhỏ giữ một intention có test; review so contract và risk; release trỏ artifact/version đã kiểm Sai boundary ở `small commits, review boundary và release discipline trong cộng tác Git` làm kết quả có vẻ đúng trong happy path nhưng không chịu được failure hoặc changed constraint.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, kiểm chứng và áp dụng small commits, review boundary và release discipline trong cộng tác Git?

## Nỗi Đau & Động Lực

commit nhỏ giữ một intention có test; review so contract và risk; release trỏ artifact/version đã kiểm Với `wiki.de-foundation.collaboration-small-commits-review-release-discipline`, điểm phải khóa là state transition và invariant; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Không có mô hình này, lỗi thường lộ ở consumer sau cùng: output sai, latency vọt, resource không được giải phóng hoặc lịch sử không còn tái hiện được. Chi phí thật của `Collaboration - small commits, review and release discipline` vì thế nằm ở thời gian chẩn đoán và phạm vi phục hồi, không nằm ở số dòng syntax.

## Cơ Chế Tác Động

nhỏ không có nghĩa chia cơ học; commit phải build được hoặc nói rõ dependency; shared history giới hạn rewrite Với `wiki.de-foundation.collaboration-small-commits-review-release-discipline`, điểm phải khóa là identity, ownership và boundary; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hãy tách declared state, executed state và published state của `small commits, review boundary và release discipline trong cộng tác Git`. Một command thành công chỉ là executed signal; muốn kết luận cần đối soát consumer-visible invariant và trạng thái còn lại sau restart hoặc replay.

## Bản Đồ Quyết Định

commit trộn refactor với behavior che review; approval trên SHA cũ mất hiệu lực sau force-push Với `wiki.de-foundation.collaboration-small-commits-review-release-discipline`, điểm phải khóa là failure path và recovery; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Quy tắc mặc định cho `Collaboration - small commits, review and release discipline` là chọn phương án đơn giản nhất qua được hard constraints, rồi ghi rõ điều kiện đảo. Bảng quyết định tối thiểu gồm workload, identity, state owner, time/memory budget, failure domain và khả năng rollback.

## Case Study Thực Chiến: Collaboration - small commits, review and release discipline

tách theo independently reviewable outcome, squash fixup noise khi policy cho phép, release từ immutable revision Với `wiki.de-foundation.collaboration-small-commits-review-release-discipline`, điểm phải khóa là decision trade-off và reversal trigger; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Case dùng fixture nhỏ nhưng phải giữ cơ chế chi phối. Trước khi chạy, learner viết expected transition; sau khi chạy, họ đối chiếu raw artifact với oracle và giải thích mọi khác biệt thay vì sửa expected cho khớp output.

## Góc Khuất & Ngộ Nhận

giữ diff, tests, review findings, approved SHA và artifact digest Với `wiki.de-foundation.collaboration-small-commits-review-release-discipline`, điểm phải khóa là evidence package và oracle; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

**Hiểu lầm:** Happy path chạy nhanh nghĩa là thiết kế đúng. **Thực tế:** commit trộn refactor với behavior che review; approval trên SHA cũ mất hiệu lực sau force-push **Vì sao nghe hợp lý:** case nhỏ thường không chạm capacity, concurrency, failure hoặc version boundary.

**Hiểu lầm:** Tool hoặc API tự bảo đảm semantics. **Thực tế:** guarantee chỉ tồn tại trong scope và state đã công bố. **Vì sao nghe hợp lý:** syntax che mất protocol phía dưới.

## Nếu Bạn Dạy Lại Điều Này...

đổi một requirement giữa review và release để kiểm approval invalidation Với `wiki.de-foundation.collaboration-small-commits-review-release-discipline`, điểm phải khóa là changed-constraint transfer; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hook dạy lại bắt đầu bằng một dự đoán dễ sai về `small commits, review boundary và release discipline trong cộng tác Git`. Bài tập seed đổi đúng một constraint, yêu cầu learner giữ hoặc đảo quyết định và chỉ ra evidence nào đủ mạnh để thuyết phục một reviewer không tham dự buổi học.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `Collaboration - small commits, review and release discipline` là: giữ diff, tests, review findings, approved SHA và artifact digest Mỗi probe nối input boundary với failure signal và oracle có thể bác bỏ kết luận.

### Probe 1: state transition và invariant

**Mệnh đề cần kiểm.** commit nhỏ giữ một intention có test; review so contract và risk; release trỏ artifact/version đã kiểm

**Thiết kế phép thử.** Với `wiki.de-foundation.collaboration-small-commits-review-release-discipline`, tạo positive và negative control chỉ khác một điều kiện; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề cần kiểm.** nhỏ không có nghĩa chia cơ học; commit phải build được hoặc nói rõ dependency; shared history giới hạn rewrite

**Thiết kế phép thử.** Với `wiki.de-foundation.collaboration-small-commits-review-release-discipline`, tạo boundary case ngay trước và sau ngưỡng; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề cần kiểm.** commit trộn refactor với behavior che review; approval trên SHA cũ mất hiệu lực sau force-push

**Thiết kế phép thử.** Với `wiki.de-foundation.collaboration-small-commits-review-release-discipline`, tạo replay cùng identity với state khác; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** tách theo independently reviewable outcome, squash fixup noise khi policy cho phép, release từ immutable revision

**Thiết kế phép thử.** Với `wiki.de-foundation.collaboration-small-commits-review-release-discipline`, tạo failure inject trước và sau durable transition; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề cần kiểm.** giữ diff, tests, review findings, approved SHA và artifact digest

**Thiết kế phép thử.** Với `wiki.de-foundation.collaboration-small-commits-review-release-discipline`, tạo changed scale làm cost model đổi; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề cần kiểm.** đổi một requirement giữa review và release để kiểm approval invalidation

**Thiết kế phép thử.** Với `wiki.de-foundation.collaboration-small-commits-review-release-discipline`, tạo adversarial order hoặc skew; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề cần kiểm.** commit nhỏ giữ một intention có test; review so contract và risk; release trỏ artifact/version đã kiểm

**Thiết kế phép thử.** Với `wiki.de-foundation.collaboration-small-commits-review-release-discipline`, tạo fresh environment không cache; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề cần kiểm.** nhỏ không có nghĩa chia cơ học; commit phải build được hoặc nói rõ dependency; shared history giới hạn rewrite

**Thiết kế phép thử.** Với `wiki.de-foundation.collaboration-small-commits-review-release-discipline`, tạo independent oracle không dùng chung implementation; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề cần kiểm.** commit trộn refactor với behavior che review; approval trên SHA cũ mất hiệu lực sau force-push

**Thiết kế phép thử.** Với `wiki.de-foundation.collaboration-small-commits-review-release-discipline`, tạo partial progress rồi restart; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** tách theo independently reviewable outcome, squash fixup noise khi policy cho phép, release từ immutable revision

**Thiết kế phép thử.** Với `wiki.de-foundation.collaboration-small-commits-review-release-discipline`, tạo missing evidence phải abstain; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề cần kiểm.** giữ diff, tests, review findings, approved SHA và artifact digest

**Thiết kế phép thử.** Với `wiki.de-foundation.collaboration-small-commits-review-release-discipline`, tạo reviewer tái hiện từ package; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề cần kiểm.** đổi một requirement giữa review và release để kiểm approval invalidation

**Thiết kế phép thử.** Với `wiki.de-foundation.collaboration-small-commits-review-release-discipline`, tạo constraint đổi đủ để quyết định đảo; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên của `small commits, review boundary và release discipline trong cộng tác Git` nằm ở đâu?

<details><summary>Đáp án</summary>nhỏ không có nghĩa chia cơ học; commit phải build được hoặc nói rõ dependency; shared history giới hạn rewrite</details>

2. Failure nào dễ tạo kết quả xanh giả nhất?

<details><summary>Đáp án</summary>commit trộn refactor với behavior che review; approval trên SHA cũ mất hiệu lực sau force-push</details>

3. Constraint nào khiến quyết định phải đảo?

<details><summary>Đáp án</summary>đổi một requirement giữa review và release để kiểm approval invalidation</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `Collaboration - small commits, review and release discipline` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Mọi kết luận phụ thuộc version, workload, operating system, interpreter/compiler hoặc hardware phải được kiểm lại trên target.
- Concept key `ck.de.collaboration-small-commits-review-release-discipline` đang ở trạng thái `proposed`; note không được tính là canonical registry coverage trước khi owner đăng ký key.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-CHACON-STRAUB-PRO-GIT-2E]]
2. [[SRC-SOMMERVILLE-SOFTWARE-ENGINEERING-10E]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-CHACON-STRAUB-PRO-GIT-2E]] — `src.book.chacon-straub-pro-git.2e` | Chapter 3 PDF 129–174; Chapter 7 PDF 422–434; Chapter 10 PDF 762–790 | cơ chế và boundary liên quan trực tiếp tới `small commits, review boundary và release discipline trong cộng tác Git` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L007 |
| [[SRC-SOMMERVILLE-SOFTWARE-ENGINEERING-10E]] — `src.book.sommerville-software-engineering.10e` | Chapters 4, 7, 8 và 25; PDF 103–132, 169–212, 228–242, 732–756 | cơ chế và boundary liên quan trực tiếp tới `small commits, review boundary và release discipline trong cộng tác Git` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L007 |

## Key takeaways
- tách theo independently reviewable outcome, squash fixup noise khi policy cho phép, release từ immutable revision
- giữ diff, tests, review findings, approved SHA và artifact digest
- `small commits, review boundary và release discipline trong cộng tác Git` chỉ có nghĩa trong scope, identity, state và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.
