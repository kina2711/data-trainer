---
loai: authentic-homework
lesson_id: DE-L001
trang_thai: ready-for-owner-review
nguong_dat: 75
---

# Homework: Contract before code

## Bối cảnh cố định

Một API đối tác nhận order qua POST, trả 202 khi request được accepted và xử lý bất đồng bộ. Client có timeout 5 giây. Cùng order có thể được gửi lại; update cũ có thể đến muộn; hai đối tác có thể dùng cùng order_id.

Yêu cầu ban đầu:

> Đồng bộ order nhanh, không trùng, có lỗi thì retry.

Không được chọn framework trước khi khóa contract. Assumption phải nằm trong assumption ledger cùng impact-if-wrong và owner xác nhận.

## Artifact phải nộp

Một thư mục gồm:

- contract.md
- examples.feature
- fixture.json
- oracle.sql
- traceability.md
- operations-note.md

### Phần A: Testable contract, 30 điểm

Contract phải khóa:

1. consumer và decision
2. in-scope và out-of-scope boundary
3. identity, event time, processing time và state model
4. invariants cho current state và history
5. behavior cho invalid input, out-of-order event, timeout và partial failure
6. evidence location, retention và owner

### Phần B: Example Mapping và executable specification, 25 điểm

Viết ít nhất:

- bốn rules
- tám examples
- năm open questions
- sáu Given/When/Then scenarios

Scenario bắt buộc gồm happy path, duplicate retry, same key with conflicting payload, late older update, invalid record và timeout after commit.

### Phần C: Oracle và traceability, 25 điểm

Tạo fixture tối thiểu 12 records và các check cho:

- uniqueness của current state
- source-to-curated completeness
- monotonic state hoặc source version
- quarantine isolation
- idempotency ledger
- freshness distribution

Mỗi check nối tới requirement ID, expected result, observed evidence và owner. Ít nhất một oracle phải độc lập với phép biến đổi đang kiểm.

### Phần D: Changed constraint, 20 điểm

**Changed constraint:** freshness SLO đổi từ 10 phút xuống 30 giây, trong khi source contract chỉ cho poll mỗi 2 phút.

Nộp decision record:

- hard constraint
- ít nhất ba option
- chosen và rejected option
- cost, consumer harm và blast radius
- rollback hoặc recovery
- approval owner
- condition làm quyết định đảo

## Rubric chấm điểm

| Tiêu chí | Điểm | Full-credit evidence |
|---|---:|---|
| Boundary và semantics | 20 | Identity, time, state, population và exclusions tạo expected result duy nhất |
| Invariants và failure behavior | 20 | Happy path cùng timeout, conflict, late và invalid path rõ |
| Fixture và oracle | 20 | Expected result viết trước; có independent control và discrepancy handling |
| Idempotency và recovery | 15 | Key scope, conflict, status lookup, retry và replay an toàn |
| SLI, SLO và change control | 15 | Formula, threshold, window, hard constraint và owner rõ |
| Traceability và handoff | 10 | Requirement, test, evidence, owner nối được end to end |

**Ngưỡng đạt:** từ 75/100 và không có critical failure.

## Critical-failure rules

- Timeout được coi là bằng chứng server chưa commit.
- Retry bằng key mới mà không phân tích side effect.
- Duplicate được định nghĩa khi chưa khóa identity và state.
- Oracle dùng cùng logic lỗi với implementation mà không có independent control.
- Expected result bị sửa sau khi xem output mà không ghi discrepancy.
- Bỏ hard source constraint để hứa đạt SLO 30 giây.
- Khẳng định production readiness chỉ từ fixture của bài.

## Remediation và retest

Reviewer gắn lỗi với requirement ID và rubric row. Người học sửa đúng phần lỗi rồi retest trên scenario khác: file ingestion có checksum, partial upload và replay sau crash. Bản gốc, feedback, patch và retest phải được giữ tách biệt.

## References

- [[wiki.engineering-foundation.testable-contract|From a vague request to a testable contract]]
- [[wiki.data-product.requirements-traceability|Requirements traceability]]
- [[wiki.data-quality.sli-slo-design|Data SLI and SLO design]]
