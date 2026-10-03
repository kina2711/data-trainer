# Phase 1: Engineering Foundation
# Module 2: Python for Production
# Lesson 15: Exceptions, resource lifetime and context managers

## Mục tiêu bài học

**Năng lực cần chứng minh.** Viết mã xử lý lỗi không nuốt ngoại lệ và không rò rỉ tài nguyên, chứng minh bằng thí nghiệm gây lỗi giữa chừng.

**Điều kiện hoàn thành.** Sau 100 lần gây lỗi không còn kết nối nào mở, và mọi lỗi ở ranh giới đều giữ được nguyên nhân gốc trong dấu vết.


# Exceptions, resource lifetime and context managers

**Tóm tắt bản chất:** try/finally bảo đảm cleanup; context manager đóng gói acquire/release; __exit__ quyết định suppression Sai boundary ở `exception propagation và deterministic resource lifetime` làm kết quả có vẻ đúng trong happy path nhưng không chịu được failure hoặc changed constraint.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, kiểm chứng và áp dụng exception propagation và deterministic resource lifetime?

## Nỗi Đau & Động Lực

try/finally bảo đảm cleanup; context manager đóng gói acquire/release; __exit__ quyết định suppression Với `wiki.de-foundation.exceptions-resource-lifetime-context-managers`, điểm phải khóa là state transition và invariant; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Không có mô hình này, lỗi thường lộ ở consumer sau cùng: output sai, latency vọt, resource không được giải phóng hoặc lịch sử không còn tái hiện được. Chi phí thật của `Exceptions, resource lifetime and context managers` vì thế nằm ở thời gian chẩn đoán và phạm vi phục hồi, không nằm ở số dòng syntax.

## Cơ Chế Tác Động

exception là failure contract; không bắt BaseException rộng; cleanup phải đúng cả khi acquire nửa chừng Với `wiki.de-foundation.exceptions-resource-lifetime-context-managers`, điểm phải khóa là identity, ownership và boundary; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hãy tách declared state, executed state và published state của `exception propagation và deterministic resource lifetime`. Một command thành công chỉ là executed signal; muốn kết luận cần đối soát consumer-visible invariant và trạng thái còn lại sau restart hoặc replay.

## Bản Đồ Quyết Định

swallow exception tạo success giả; cleanup lỗi che primary failure; GC-based close không deterministic Với `wiki.de-foundation.exceptions-resource-lifetime-context-managers`, điểm phải khóa là failure path và recovery; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Quy tắc mặc định cho `Exceptions, resource lifetime and context managers` là chọn phương án đơn giản nhất qua được hard constraints, rồi ghi rõ điều kiện đảo. Bảng quyết định tối thiểu gồm workload, identity, state owner, time/memory budget, failure domain và khả năng rollback.

## Case Study Thực Chiến: Exceptions, resource lifetime and context managers

bắt ở boundary có đủ context để recover hoặc translate; dùng ExitStack cho tài nguyên động Với `wiki.de-foundation.exceptions-resource-lifetime-context-managers`, điểm phải khóa là decision trade-off và reversal trigger; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Case dùng fixture nhỏ nhưng phải giữ cơ chế chi phối. Trước khi chạy, learner viết expected transition; sau khi chạy, họ đối chiếu raw artifact với oracle và giải thích mọi khác biệt thay vì sửa expected cho khớp output.

## Góc Khuất & Ngộ Nhận

giữ primary/secondary exception, open-handle count, cleanup order và exit status Với `wiki.de-foundation.exceptions-resource-lifetime-context-managers`, điểm phải khóa là evidence package và oracle; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

**Hiểu lầm:** Happy path chạy nhanh nghĩa là thiết kế đúng. **Thực tế:** swallow exception tạo success giả; cleanup lỗi che primary failure; GC-based close không deterministic **Vì sao nghe hợp lý:** case nhỏ thường không chạm capacity, concurrency, failure hoặc version boundary.

**Hiểu lầm:** Tool hoặc API tự bảo đảm semantics. **Thực tế:** guarantee chỉ tồn tại trong scope và state đã công bố. **Vì sao nghe hợp lý:** syntax che mất protocol phía dưới.

## Nếu Bạn Dạy Lại Điều Này...

inject failure sau mỗi bước acquire để chứng minh unwind theo thứ tự ngược Với `wiki.de-foundation.exceptions-resource-lifetime-context-managers`, điểm phải khóa là changed-constraint transfer; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hook dạy lại bắt đầu bằng một dự đoán dễ sai về `exception propagation và deterministic resource lifetime`. Bài tập seed đổi đúng một constraint, yêu cầu learner giữ hoặc đảo quyết định và chỉ ra evidence nào đủ mạnh để thuyết phục một reviewer không tham dự buổi học.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `Exceptions, resource lifetime and context managers` là: giữ primary/secondary exception, open-handle count, cleanup order và exit status Mỗi probe nối input boundary với failure signal và oracle có thể bác bỏ kết luận.

### Probe 1: state transition và invariant

**Mệnh đề cần kiểm.** try/finally bảo đảm cleanup; context manager đóng gói acquire/release; __exit__ quyết định suppression

**Thiết kế phép thử.** Với `wiki.de-foundation.exceptions-resource-lifetime-context-managers`, tạo positive và negative control chỉ khác một điều kiện; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề cần kiểm.** exception là failure contract; không bắt BaseException rộng; cleanup phải đúng cả khi acquire nửa chừng

**Thiết kế phép thử.** Với `wiki.de-foundation.exceptions-resource-lifetime-context-managers`, tạo boundary case ngay trước và sau ngưỡng; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề cần kiểm.** swallow exception tạo success giả; cleanup lỗi che primary failure; GC-based close không deterministic

**Thiết kế phép thử.** Với `wiki.de-foundation.exceptions-resource-lifetime-context-managers`, tạo replay cùng identity với state khác; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** bắt ở boundary có đủ context để recover hoặc translate; dùng ExitStack cho tài nguyên động

**Thiết kế phép thử.** Với `wiki.de-foundation.exceptions-resource-lifetime-context-managers`, tạo failure inject trước và sau durable transition; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề cần kiểm.** giữ primary/secondary exception, open-handle count, cleanup order và exit status

**Thiết kế phép thử.** Với `wiki.de-foundation.exceptions-resource-lifetime-context-managers`, tạo changed scale làm cost model đổi; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề cần kiểm.** inject failure sau mỗi bước acquire để chứng minh unwind theo thứ tự ngược

**Thiết kế phép thử.** Với `wiki.de-foundation.exceptions-resource-lifetime-context-managers`, tạo adversarial order hoặc skew; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề cần kiểm.** try/finally bảo đảm cleanup; context manager đóng gói acquire/release; __exit__ quyết định suppression

**Thiết kế phép thử.** Với `wiki.de-foundation.exceptions-resource-lifetime-context-managers`, tạo fresh environment không cache; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề cần kiểm.** exception là failure contract; không bắt BaseException rộng; cleanup phải đúng cả khi acquire nửa chừng

**Thiết kế phép thử.** Với `wiki.de-foundation.exceptions-resource-lifetime-context-managers`, tạo independent oracle không dùng chung implementation; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề cần kiểm.** swallow exception tạo success giả; cleanup lỗi che primary failure; GC-based close không deterministic

**Thiết kế phép thử.** Với `wiki.de-foundation.exceptions-resource-lifetime-context-managers`, tạo partial progress rồi restart; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** bắt ở boundary có đủ context để recover hoặc translate; dùng ExitStack cho tài nguyên động

**Thiết kế phép thử.** Với `wiki.de-foundation.exceptions-resource-lifetime-context-managers`, tạo missing evidence phải abstain; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề cần kiểm.** giữ primary/secondary exception, open-handle count, cleanup order và exit status

**Thiết kế phép thử.** Với `wiki.de-foundation.exceptions-resource-lifetime-context-managers`, tạo reviewer tái hiện từ package; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề cần kiểm.** inject failure sau mỗi bước acquire để chứng minh unwind theo thứ tự ngược

**Thiết kế phép thử.** Với `wiki.de-foundation.exceptions-resource-lifetime-context-managers`, tạo constraint đổi đủ để quyết định đảo; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên của `exception propagation và deterministic resource lifetime` nằm ở đâu?

<details><summary>Đáp án</summary>exception là failure contract; không bắt BaseException rộng; cleanup phải đúng cả khi acquire nửa chừng</details>

2. Failure nào dễ tạo kết quả xanh giả nhất?

<details><summary>Đáp án</summary>swallow exception tạo success giả; cleanup lỗi che primary failure; GC-based close không deterministic</details>

3. Constraint nào khiến quyết định phải đảo?

<details><summary>Đáp án</summary>inject failure sau mỗi bước acquire để chứng minh unwind theo thứ tự ngược</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `Exceptions, resource lifetime and context managers` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Mọi kết luận phụ thuộc version, workload, operating system, interpreter/compiler hoặc hardware phải được kiểm lại trên target.
- Concept key `ck.de.exceptions-resource-lifetime-context-managers` đang ở trạng thái `proposed`; note không được tính là canonical registry coverage trước khi owner đăng ký key.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-PYTHON-314-LANGUAGE-REFERENCE]]
2. [[SRC-PYTHON-314-STDLIB-RUNTIME]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-PYTHON-314-LANGUAGE-REFERENCE]] — `src.docs.python-3.14-language-reference` | Python 3.14.8 Language Reference; accessed 2026-10-02 | cơ chế và boundary liên quan trực tiếp tới `exception propagation và deterministic resource lifetime` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L015 |
| [[SRC-PYTHON-314-STDLIB-RUNTIME]] — `src.docs.python-3.14-stdlib-runtime` | Python 3.14.8 Library Reference; accessed 2026-10-02 | cơ chế và boundary liên quan trực tiếp tới `exception propagation và deterministic resource lifetime` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L015 |

## Key takeaways
- bắt ở boundary có đủ context để recover hoặc translate; dùng ExitStack cho tài nguyên động
- giữ primary/secondary exception, open-handle count, cleanup order và exit status
- `exception propagation và deterministic resource lifetime` chỉ có nghĩa trong scope, identity, state và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.
