# Phase 1: Engineering Foundation
# Module 1: Engineering Thinking, Git and Debugging
# Lesson 10: Technical artifacts - README, runbook and postmortem

## Mục tiêu bài học

**Năng lực cần chứng minh.** Viết bộ bốn tài liệu cho một thành phần nhỏ, và người khác dùng được mà không phải hỏi.

**Điều kiện hoàn thành.** Người nhận cài và chạy được, xử lý được tình huống theo sổ tay, và số câu hỏi phải hỏi dưới ngưỡng.


# Technical artifacts - README, runbook and postmortem

**Tóm tắt bản chất:** README giúp bắt đầu và hiểu boundary; runbook hướng dẫn vận hành dưới áp lực; postmortem lưu timeline, causes và prevention Sai boundary ở `README, runbook và postmortem như ba artifact phục vụ ba quyết định khác nhau` làm kết quả có vẻ đúng trong happy path nhưng không chịu được failure hoặc changed constraint.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào mô hình, kiểm chứng và áp dụng README, runbook và postmortem như ba artifact phục vụ ba quyết định khác nhau?

## Nỗi Đau & Động Lực

README giúp bắt đầu và hiểu boundary; runbook hướng dẫn vận hành dưới áp lực; postmortem lưu timeline, causes và prevention Với `wiki.de-foundation.technical-artifacts-readme-runbook-postmortem`, điểm phải khóa là state transition và invariant; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Không có mô hình này, lỗi thường lộ ở consumer sau cùng: output sai, latency vọt, resource không được giải phóng hoặc lịch sử không còn tái hiện được. Chi phí thật của `Technical artifacts - README, runbook and postmortem` vì thế nằm ở thời gian chẩn đoán và phạm vi phục hồi, không nằm ở số dòng syntax.

## Cơ Chế Tác Động

không trộn tutorial với emergency procedure; postmortem không phải nơi quy trách cá nhân; mọi command nguy hiểm cần precondition Với `wiki.de-foundation.technical-artifacts-readme-runbook-postmortem`, điểm phải khóa là identity, ownership và boundary; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hãy tách declared state, executed state và published state của `README, runbook và postmortem như ba artifact phục vụ ba quyết định khác nhau`. Một command thành công chỉ là executed signal; muốn kết luận cần đối soát consumer-visible invariant và trạng thái còn lại sau restart hoặc replay.

## Bản Đồ Quyết Định

README stale làm setup sai; runbook thiếu stop condition tăng blast radius; postmortem chỉ kể chuyện không tạo control Với `wiki.de-foundation.technical-artifacts-readme-runbook-postmortem`, điểm phải khóa là failure path và recovery; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Quy tắc mặc định cho `Technical artifacts - README, runbook and postmortem` là chọn phương án đơn giản nhất qua được hard constraints, rồi ghi rõ điều kiện đảo. Bảng quyết định tối thiểu gồm workload, identity, state owner, time/memory budget, failure domain và khả năng rollback.

## Case Study Thực Chiến: Technical artifacts - README, runbook and postmortem

chọn artifact theo consumer và thời điểm; version cùng hệ thống; test bằng người không dự buổi viết Với `wiki.de-foundation.technical-artifacts-readme-runbook-postmortem`, điểm phải khóa là decision trade-off và reversal trigger; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Case dùng fixture nhỏ nhưng phải giữ cơ chế chi phối. Trước khi chạy, learner viết expected transition; sau khi chạy, họ đối chiếu raw artifact với oracle và giải thích mọi khác biệt thay vì sửa expected cho khớp output.

## Góc Khuất & Ngộ Nhận

fresh-environment setup, runbook drill, postmortem action owner và review date Với `wiki.de-foundation.technical-artifacts-readme-runbook-postmortem`, điểm phải khóa là evidence package và oracle; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

**Hiểu lầm:** Happy path chạy nhanh nghĩa là thiết kế đúng. **Thực tế:** README stale làm setup sai; runbook thiếu stop condition tăng blast radius; postmortem chỉ kể chuyện không tạo control **Vì sao nghe hợp lý:** case nhỏ thường không chạm capacity, concurrency, failure hoặc version boundary.

**Hiểu lầm:** Tool hoặc API tự bảo đảm semantics. **Thực tế:** guarantee chỉ tồn tại trong scope và state đã công bố. **Vì sao nghe hợp lý:** syntax che mất protocol phía dưới.

## Nếu Bạn Dạy Lại Điều Này...

đổi dependency và inject incident để kiểm ba artifact cập nhật đúng phần Với `wiki.de-foundation.technical-artifacts-readme-runbook-postmortem`, điểm phải khóa là changed-constraint transfer; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.

Hook dạy lại bắt đầu bằng một dự đoán dễ sai về `README, runbook và postmortem như ba artifact phục vụ ba quyết định khác nhau`. Bài tập seed đổi đúng một constraint, yêu cầu learner giữ hoặc đảo quyết định và chỉ ra evidence nào đủ mạnh để thuyết phục một reviewer không tham dự buổi học.

## Ma trận kiểm chứng từng mệnh đề

Protocol riêng của `Technical artifacts - README, runbook and postmortem` là: fresh-environment setup, runbook drill, postmortem action owner và review date Mỗi probe nối input boundary với failure signal và oracle có thể bác bỏ kết luận.

### Probe 1: state transition và invariant

**Mệnh đề cần kiểm.** README giúp bắt đầu và hiểu boundary; runbook hướng dẫn vận hành dưới áp lực; postmortem lưu timeline, causes và prevention

**Thiết kế phép thử.** Với `wiki.de-foundation.technical-artifacts-readme-runbook-postmortem`, tạo positive và negative control chỉ khác một điều kiện; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 2: identity, ownership và boundary

**Mệnh đề cần kiểm.** không trộn tutorial với emergency procedure; postmortem không phải nơi quy trách cá nhân; mọi command nguy hiểm cần precondition

**Thiết kế phép thử.** Với `wiki.de-foundation.technical-artifacts-readme-runbook-postmortem`, tạo boundary case ngay trước và sau ngưỡng; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 3: failure path và recovery

**Mệnh đề cần kiểm.** README stale làm setup sai; runbook thiếu stop condition tăng blast radius; postmortem chỉ kể chuyện không tạo control

**Thiết kế phép thử.** Với `wiki.de-foundation.technical-artifacts-readme-runbook-postmortem`, tạo replay cùng identity với state khác; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 4: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** chọn artifact theo consumer và thời điểm; version cùng hệ thống; test bằng người không dự buổi viết

**Thiết kế phép thử.** Với `wiki.de-foundation.technical-artifacts-readme-runbook-postmortem`, tạo failure inject trước và sau durable transition; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 5: evidence package và oracle

**Mệnh đề cần kiểm.** fresh-environment setup, runbook drill, postmortem action owner và review date

**Thiết kế phép thử.** Với `wiki.de-foundation.technical-artifacts-readme-runbook-postmortem`, tạo changed scale làm cost model đổi; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 6: changed-constraint transfer

**Mệnh đề cần kiểm.** đổi dependency và inject incident để kiểm ba artifact cập nhật đúng phần

**Thiết kế phép thử.** Với `wiki.de-foundation.technical-artifacts-readme-runbook-postmortem`, tạo adversarial order hoặc skew; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 7: state transition và invariant

**Mệnh đề cần kiểm.** README giúp bắt đầu và hiểu boundary; runbook hướng dẫn vận hành dưới áp lực; postmortem lưu timeline, causes và prevention

**Thiết kế phép thử.** Với `wiki.de-foundation.technical-artifacts-readme-runbook-postmortem`, tạo fresh environment không cache; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 8: identity, ownership và boundary

**Mệnh đề cần kiểm.** không trộn tutorial với emergency procedure; postmortem không phải nơi quy trách cá nhân; mọi command nguy hiểm cần precondition

**Thiết kế phép thử.** Với `wiki.de-foundation.technical-artifacts-readme-runbook-postmortem`, tạo independent oracle không dùng chung implementation; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 9: failure path và recovery

**Mệnh đề cần kiểm.** README stale làm setup sai; runbook thiếu stop condition tăng blast radius; postmortem chỉ kể chuyện không tạo control

**Thiết kế phép thử.** Với `wiki.de-foundation.technical-artifacts-readme-runbook-postmortem`, tạo partial progress rồi restart; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 10: decision trade-off và reversal trigger

**Mệnh đề cần kiểm.** chọn artifact theo consumer và thời điểm; version cùng hệ thống; test bằng người không dự buổi viết

**Thiết kế phép thử.** Với `wiki.de-foundation.technical-artifacts-readme-runbook-postmortem`, tạo missing evidence phải abstain; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 11: evidence package và oracle

**Mệnh đề cần kiểm.** fresh-environment setup, runbook drill, postmortem action owner và review date

**Thiết kế phép thử.** Với `wiki.de-foundation.technical-artifacts-readme-runbook-postmortem`, tạo reviewer tái hiện từ package; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

### Probe 12: changed-constraint transfer

**Mệnh đề cần kiểm.** đổi dependency và inject incident để kiểm ba artifact cập nhật đúng phần

**Thiết kế phép thử.** Với `wiki.de-foundation.technical-artifacts-readme-runbook-postmortem`, tạo constraint đổi đủ để quyết định đảo; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.

**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.

## Tự Kiểm Tra Nhanh

1. Boundary đầu tiên của `README, runbook và postmortem như ba artifact phục vụ ba quyết định khác nhau` nằm ở đâu?

<details><summary>Đáp án</summary>không trộn tutorial với emergency procedure; postmortem không phải nơi quy trách cá nhân; mọi command nguy hiểm cần precondition</details>

2. Failure nào dễ tạo kết quả xanh giả nhất?

<details><summary>Đáp án</summary>README stale làm setup sai; runbook thiếu stop condition tăng blast radius; postmortem chỉ kể chuyện không tạo control</details>

3. Constraint nào khiến quyết định phải đảo?

<details><summary>Đáp án</summary>đổi dependency và inject incident để kiểm ba artifact cập nhật đúng phần</details>

## Giới hạn và điều chưa cho phép kết luận

- Lab của `Technical artifacts - README, runbook and postmortem` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.
- Mọi kết luận phụ thuộc version, workload, operating system, interpreter/compiler hoặc hardware phải được kiểm lại trên target.
- Concept key `ck.de.technical-artifacts-readme-runbook-postmortem` đang ở trạng thái `proposed`; note không được tính là canonical registry coverage trước khi owner đăng ký key.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-SOMMERVILLE-SOFTWARE-ENGINEERING-10E]]
2. [[SRC-GOOGLE-SRE-POSTMORTEM-CULTURE]]
3. [[SRC-GOOGLE-SRE-INCIDENT-MANAGEMENT]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-SOMMERVILLE-SOFTWARE-ENGINEERING-10E]] — `src.book.sommerville-software-engineering.10e` | Chapters 4, 7, 8 và 25; PDF 103–132, 169–212, 228–242, 732–756 | cơ chế và boundary liên quan trực tiếp tới `README, runbook và postmortem như ba artifact phục vụ ba quyết định khác nhau` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L010 |
| [[SRC-GOOGLE-SRE-POSTMORTEM-CULTURE]] — `src.web.google-sre-postmortem-culture` | Postmortem culture; accessed 2026-10-01 | cơ chế và boundary liên quan trực tiếp tới `README, runbook và postmortem như ba artifact phục vụ ba quyết định khác nhau` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L010 |
| [[SRC-GOOGLE-SRE-INCIDENT-MANAGEMENT]] — `src.web.google-sre-incident-management` | Incident management; accessed 2026-10-01 | cơ chế và boundary liên quan trực tiếp tới `README, runbook và postmortem như ba artifact phục vụ ba quyết định khác nhau` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L010 |

## Key takeaways
- chọn artifact theo consumer và thời điểm; version cùng hệ thống; test bằng người không dự buổi viết
- fresh-environment setup, runbook drill, postmortem action owner và review date
- `README, runbook và postmortem như ba artifact phục vụ ba quyết định khác nhau` chỉ có nghĩa trong scope, identity, state và version đã ghi.
- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.
