# Phase 1: Nền tảng kỹ thuật
# Module 1: Tư duy kỹ thuật, Git và gỡ lỗi
# Lesson 1: Practice, assessment and transfer

## Thực hành

### Worked trace: từ vague request tới contract

Yêu cầu gốc:

> Đồng bộ order nhanh, không trùng, có lỗi thì retry.

Trace mẫu:

1. **Decision:** Fulfillment chỉ xử lý order complete.
2. **Boundary:** API response hợp lệ tới curated current-state table.
3. **Identity:** source_system cộng order_id.
4. **Time:** source_updated_at cho ordering; curated_at cho freshness.
5. **Invariant:** đúng một current row trên mỗi identity.
6. **Failure:** invalid vào quarantine; timeout tạo unknown outcome.
7. **Evidence:** source total, run manifest, uniqueness, idempotency ledger.
8. **Trigger:** đổi SLO hoặc source contract phải qua change control.

### Guided task

Dùng Example Mapping cho sáu cụm từ:

- nhanh
- không trùng
- không mất
- retry an toàn
- latest state
- job thành công

Mỗi cụm phải có một rule, hai examples, một counterexample và một open question.

**Điều kiện đạt:** expected result duy nhất, observable outcome và không khóa implementation khi chưa cần.

### Independent task

Viết Given/When/Then cho:

1. duplicate request sau timeout
2. same key với payload khác
3. event cũ đến muộn
4. invalid row giữa batch
5. API 202 nhưng processing fail
6. source count lệch curated count

### Changed constraint

Freshness SLO đổi từ 10 phút xuống 30 giây, source chỉ cho poll mỗi 2 phút. Tạo decision record với ba option, hard constraint, chosen/rejected option, owner và reversal trigger.

### Feedback protocol

1. Người học công bố fixture và expected result trước test output.
2. Reviewer hỏi identity, boundary, failure path và independent oracle.
3. Mọi feedback gắn requirement ID và observable evidence.
4. Sửa expected result phải ghi discrepancy và được owner phê duyệt.
5. Retest dùng fixture mới, giữ nguyên failed attempt.

## Kiểm tra cuối bài

### Recall cần thiết

- Sáu lớp của testable contract là gì?
- Timeout khác failure ra sao?
- Correctness, freshness và availability khác nhau thế nào?

### Apply hoặc diagnose

Client gửi POST, server commit, response bị mất, client retry bằng key mới và tạo side effect thứ hai. Hãy chỉ ra:

1. failure nằm ở contract nào
2. evidence cần giữ
3. behavior đúng cho retry
4. consumer harm
5. recovery và prevention

### Transfer

Thiết kế contract cho file ingestion: file có checksum, upload có thể partial, rename đánh dấu complete và process có thể crash sau commit.

### Cách chấm rubric

- 0: chỉ nêu tool hoặc implementation
- 1: có happy path nhưng thiếu semantics/failure
- 2: có contract và fixture nhưng oracle phụ thuộc
- 3: có independent evidence, recovery và change trigger

## Novel-scenario retest

API trả 202 Accepted và operation ID. Client timeout trước khi đọc body. Thiết kế status lookup, idempotency scope và evidence phân biệt accepted, running, completed, failed.

**Pass condition:** không đồng nhất 202 với completed, không tạo key mới tùy tiện, có conflict behavior và recovery.

## Bài làm sau buổi học

### Bài làm

Hoàn thành quiz.md và homework.md. Ngưỡng quiz là 8/10. Ngưỡng homework là 75/100 cùng zero critical failure.

### Kiểm lại trước khi nộp

- Identity, time, state và population đã khóa.
- Mọi từ định tính có metric và threshold.
- Failure paths có expected observation.
- Ít nhất một oracle độc lập.
- Retry semantics và conflict behavior rõ.
- Requirement, test, evidence và owner trace được.

### Cách nộp

Giữ original, test output, feedback, patch và retest thành artifact riêng. Không ghi đè evidence cũ.

## Remediation map

| Lỗi quan sát | Quay lại | Micro-task | Retest |
|---|---|---|---|
| không tạo được oracle | S01, S02 | viết fixture và expected table | file ingestion |
| nhầm duplicate với update | S03 | lập identity/state matrix | CDC event |
| Given/Then khóa tool | S04 | viết lại bằng behavior | batch loader |
| timeout được coi là fail | S05 | vẽ unknown-state flow | API 202 |
| hứa SLO bất khả thi | S06 | tách hard constraint | polling source |
| uniqueness thay completeness | S07 | thêm source control | partial batch |

## Giới hạn

Fixture bài học không mô phỏng concurrency, distributed transaction hay mọi kiểu retry storm. Điểm đạt chỉ là evidence trong scope DE-L001, không chứng nhận hệ thống production-ready.

## References

- [[wiki.engineering-foundation.testable-contract|From a vague request to a testable contract]]
- [[wiki.data-product.requirements-traceability|Requirements traceability]]
- [[wiki.data-quality.sli-slo-design|Data SLI and SLO design]]
