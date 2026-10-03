# Phase 1: Engineering Foundation
# Module 2: Python for Production
# Lesson 13: Names, objects and mutability

## Mục tiêu bài học

**Năng lực cần chứng minh.** Dự đoán đúng kết quả của các đoạn mã có chia sẻ đối tượng thay đổi được, và giải thích bằng quan hệ tên với đối tượng.

**Điều kiện hoàn thành.** Dự đoán đúng ≥ 8/10 đoạn, và mỗi đoạn sai được giải thích lại bằng quan hệ tên với đối tượng.


# Names, objects and mutability

**Tóm tắt bản chất:** assignment bind name tới object; alias chia sẻ identity; mutation đổi object còn rebinding đổi liên kết tên Sai boundary ở `names, object identity, value và mutability trong Python` làm kết quả có vẻ đúng trong happy path nhưng không chịu được failure hoặc changed constraint.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, kiểm chứng và áp dụng names, object identity, value và mutability trong Python?

## Nỗi Đau & Động Lực

assignment bind name tới object; alias chia sẻ identity; mutation đổi object còn rebinding đổi liên kết tên Với `wiki.de-foundation.names-objects-mutability`, điểm phải khóa là state transition và invariant; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Không có mô hình này, lỗi thường lộ ở consumer sau cùng: output sai, latency vọt, resource không được giải phóng hoặc lịch sử không còn tái hiện được. Chi phí thật của `Names, objects and mutability` vì thế nằm ở thời gian chẩn đoán và phạm vi phục hồi, không nằm ở số dòng syntax.

## Cơ Chế Tác Động

identity không đồng nghĩa value; immutable container vẫn có thể chứa mutable object; implementation reuse không phải guarantee Với `wiki.de-foundation.names-objects-mutability`, điểm phải khóa là identity, ownership và boundary; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hãy tách declared state, executed state và published state của `names, object identity, value và mutability trong Python`. Một command thành công chỉ là executed signal; muốn kết luận cần đối soát consumer-visible invariant và trạng thái còn lại sau restart hoặc replay.

## Bản Đồ Quyết Định

mutable default và shallow copy tạo state dùng chung ngoài ý muốn; dùng is cho value gây bug phụ thuộc implementation Với `wiki.de-foundation.names-objects-mutability`, điểm phải khóa là failure path và recovery; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Quy tắc mặc định cho `Names, objects and mutability` là chọn phương án đơn giản nhất qua được hard constraints, rồi ghi rõ điều kiện đảo. Bảng quyết định tối thiểu gồm workload, identity, state owner, time/memory budget, failure domain và khả năng rollback.

## Case Study Thực Chiến: Names, objects and mutability

chọn immutable value hoặc copy tại ownership boundary; dùng equality cho value và identity cho singleton/owner semantics Với `wiki.de-foundation.names-objects-mutability`, điểm phải khóa là decision trade-off và reversal trigger; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Case dùng fixture nhỏ nhưng phải giữ cơ chế chi phối. Trước khi chạy, learner viết expected transition; sau khi chạy, họ đối chiếu raw artifact với oracle và giải thích mọi khác biệt thay vì sửa expected cho khớp output.

## Góc Khuất & Ngộ Nhận

object IDs chỉ là probe cục bộ; giữ mutation trace, alias graph và tests cho boundary Với `wiki.de-foundation.names-objects-mutability`, điểm phải khóa là evidence package và oracle; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

**Hiểu lầm:** Happy path chạy nhanh nghĩa là thiết kế đúng. **Thực tế:** mutable default và shallow copy tạo state dùng chung ngoài ý muốn; dùng is cho value gây bug phụ thuộc implementation **Vì sao nghe hợp lý:** case nhỏ thường không chạm capacity, concurrency, failure hoặc version boundary.

**Hiểu lầm:** Tool hoặc API tự bảo đảm semantics. **Thực tế:** guarantee chỉ tồn tại trong scope và state đã công bố. **Vì sao nghe hợp lý:** syntax che mất protocol phía dưới.

## Nếu Bạn Dạy Lại Điều Này...

đổi nested mutable input sau khi truyền qua API để quan sát ownership contract Với `wiki.de-foundation.names-objects-mutability`, điểm phải khóa là changed-constraint transfer; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hook dạy lại bắt đầu bằng một dự đoán dễ sai về `names, object identity, value và mutability trong Python`. Bài tập seed đổi đúng một constraint, yêu cầu learner giữ hoặc đảo quyết định và chỉ ra evidence nào đủ mạnh để thuyết phục một reviewer không tham dự buổi học.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `Names, objects and mutability` là: object IDs chỉ là probe cục bộ; giữ mutation trace, alias graph và tests cho boundary Mỗi probe nối input boundary với failure signal và oracle có thể bác bỏ kết luận.

### Probe 1: state transition và invariant

**Mệnh đề cần kiểm.** assignment bind name tới object; alias chia sẻ identity; mutation đổi object còn rebinding đổi liên kết tên

**Thiết kế phép thử.** Với `wiki.de-foundation.names-objects-mutability`, tạo positive và negative control chỉ khác một điều kiện; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề cần kiểm.** identity không đồng nghĩa value; immutable container vẫn có thể chứa mutable object; implementation reuse không phải guarantee

**Thiết kế phép thử.** Với `wiki.de-foundation.names-objects-mutability`, tạo boundary case ngay trước và sau ngưỡng; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề cần kiểm.** mutable default và shallow copy tạo state dùng chung ngoài ý muốn; dùng is cho value gây bug phụ thuộc implementation

**Thiết kế phép thử.** Với `wiki.de-foundation.names-objects-mutability`, tạo replay cùng identity với state khác; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** chọn immutable value hoặc copy tại ownership boundary; dùng equality cho value và identity cho singleton/owner semantics

**Thiết kế phép thử.** Với `wiki.de-foundation.names-objects-mutability`, tạo failure inject trước và sau durable transition; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề cần kiểm.** object IDs chỉ là probe cục bộ; giữ mutation trace, alias graph và tests cho boundary

**Thiết kế phép thử.** Với `wiki.de-foundation.names-objects-mutability`, tạo changed scale làm cost model đổi; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề cần kiểm.** đổi nested mutable input sau khi truyền qua API để quan sát ownership contract

**Thiết kế phép thử.** Với `wiki.de-foundation.names-objects-mutability`, tạo adversarial order hoặc skew; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề cần kiểm.** assignment bind name tới object; alias chia sẻ identity; mutation đổi object còn rebinding đổi liên kết tên

**Thiết kế phép thử.** Với `wiki.de-foundation.names-objects-mutability`, tạo fresh environment không cache; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề cần kiểm.** identity không đồng nghĩa value; immutable container vẫn có thể chứa mutable object; implementation reuse không phải guarantee

**Thiết kế phép thử.** Với `wiki.de-foundation.names-objects-mutability`, tạo independent oracle không dùng chung implementation; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề cần kiểm.** mutable default và shallow copy tạo state dùng chung ngoài ý muốn; dùng is cho value gây bug phụ thuộc implementation

**Thiết kế phép thử.** Với `wiki.de-foundation.names-objects-mutability`, tạo partial progress rồi restart; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** chọn immutable value hoặc copy tại ownership boundary; dùng equality cho value và identity cho singleton/owner semantics

**Thiết kế phép thử.** Với `wiki.de-foundation.names-objects-mutability`, tạo missing evidence phải abstain; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề cần kiểm.** object IDs chỉ là probe cục bộ; giữ mutation trace, alias graph và tests cho boundary

**Thiết kế phép thử.** Với `wiki.de-foundation.names-objects-mutability`, tạo reviewer tái hiện từ package; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề cần kiểm.** đổi nested mutable input sau khi truyền qua API để quan sát ownership contract

**Thiết kế phép thử.** Với `wiki.de-foundation.names-objects-mutability`, tạo constraint đổi đủ để quyết định đảo; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên của `names, object identity, value và mutability trong Python` nằm ở đâu?

<details><summary>Đáp án</summary>identity không đồng nghĩa value; immutable container vẫn có thể chứa mutable object; implementation reuse không phải guarantee</details>

2. Failure nào dễ tạo kết quả xanh giả nhất?

<details><summary>Đáp án</summary>mutable default và shallow copy tạo state dùng chung ngoài ý muốn; dùng is cho value gây bug phụ thuộc implementation</details>

3. Constraint nào khiến quyết định phải đảo?

<details><summary>Đáp án</summary>đổi nested mutable input sau khi truyền qua API để quan sát ownership contract</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `Names, objects and mutability` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Mọi kết luận phụ thuộc version, workload, operating system, interpreter/compiler hoặc hardware phải được kiểm lại trên target.
- Concept key `ck.de.names-objects-mutability` đang ở trạng thái `proposed`; note không được tính là canonical registry coverage trước khi owner đăng ký key.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-PYTHON-314-LANGUAGE-REFERENCE]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-PYTHON-314-LANGUAGE-REFERENCE]] — `src.docs.python-3.14-language-reference` | Python 3.14.8 Language Reference; accessed 2026-10-02 | cơ chế và boundary liên quan trực tiếp tới `names, object identity, value và mutability trong Python` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L013 |

## Key takeaways
- chọn immutable value hoặc copy tại ownership boundary; dùng equality cho value và identity cho singleton/owner semantics
- object IDs chỉ là probe cục bộ; giữ mutation trace, alias graph và tests cho boundary
- `names, object identity, value và mutability trong Python` chỉ có nghĩa trong scope, identity, state và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.
