---
marp: true
theme: default
paginate: true
title: "DE-L001: From a vague request to a testable contract"
---

# From a vague request to a testable contract

DE-L001

**Câu hỏi trung tâm:** Làm sao biết hệ thống đã làm đúng?

<!-- scene: S01 | source: note.md heading 'Yêu cầu mơ hồ không có oracle' -->

---

## Mục tiêu kiểm chứng được

- tạo expected result duy nhất từ fixture
- khóa identity, time và state
- mô tả failure behavior
- thiết kế retry an toàn sau timeout
- viết SLI và SLO có threshold

---

## Yêu cầu nghe có vẻ đủ

> Đồng bộ orders nhanh, không trùng, có lỗi thì retry.

- order nào?
- nhanh bao nhiêu?
- trùng theo identity nào?
- timeout có phải failure?
- evidence ở đâu?

---

## Không có oracle, không có test

Hai reviewer nhận cùng input.

Nếu họ tạo hai expected output khác nhau:

**Requirement chưa đủ để mutation.**

---

## Sáu lớp của contract

| Lớp | Khóa |
|---|---|
| Decision | ai dùng outcome |
| Boundary | trách nhiệm từ đâu tới đâu |
| Semantics | identity, time, state |
| Invariants | điều luôn phải đúng |
| Failure | behavior khi bất thường |
| Evidence | oracle và trace |

<!-- scene: S02 | source: note.md heading 'Contract kiểm thử được khóa sáu lớp nghĩa' -->

---

## Identity trước deduplication

 order_identity = source_system + order_id

partner_a O-42 khác partner_b O-42.

Hash toàn payload không ổn định khi order được update hợp lệ.

---

## State quyết định duplicate hay history

 Accepted -> Paid -> Fulfilled
 |
 +----> Cancelled

Event cũ đến muộn không được rollback state nếu contract cấm.

<!-- scene: S03 | source: note.md heading 'Identity, time và state quyết định thế nào là đúng' -->

---

## Given When Then

**Given:** known state

**When:** observable event

**Then:** observable outcome

Không khóa MERGE, queue hay transaction nếu đó chưa phải constraint.

---

## Guided practice

Đổi sáu câu mơ hồ thành:

1. Rule
2. Fixture
3. Expected result
4. Failure path
5. Oracle
6. Requirement ID

<!-- scene: S04 | source: UNSOURCED guided practice -->

---

## Luồng kiểm soát

 Send -> Response?
 | yes: known outcome
 | timeout: unknown outcome
 |
 +-> query status -> safe retry

Timeout không chứng minh server chưa commit.

---

## Idempotency key bảo vệ ý định logic

| Cùng key | Hành vi |
|---|---|
| cùng payload, committed | trả outcome cũ |
| cùng payload, running | trả pending |
| payload khác | reject conflict |

Key mới sau timeout có thể tạo side effect thứ hai.

<!-- scene: S05 | source: note.md heading 'Timeout tạo trạng thái unknown, retry tạo side effect' -->

---

## Correctness khác freshness

 SLI = orders hợp lệ có ở curated trong 10 phút
 / tổng orders hợp lệ thuộc cutoff

SLO: ít nhất 99,0% trong rolling 28 days.

Job xanh không chứng minh output đúng.

---

## Changed constraint

SLO đổi từ 10 phút xuống 30 giây.

Source chỉ cho poll mỗi 2 phút.

- renegotiate SLO
- đổi integration contract
- đổi architecture

<!-- scene: S06 | source: UNSOURCED changed-constraint scenario -->

---

## Fixture phải chứa phản ví dụ

- cùng identity và cùng version
- version cũ đến sau
- cùng order_id từ source khác
- thiếu order_id
- timeout sau commit

Happy path đơn lẻ không kiểm contract.

---

## Nhiều oracle, nhiều failure được thấy

- uniqueness query
- source control total
- run manifest
- quarantine count
- idempotency ledger
- latency distribution

<!-- scene: S07 | source: note.md heading 'Case xuyên chương: đồng bộ orders từ API vào warehouse' -->

---

## Transfer challenge

API trả 202 rồi client timeout.

- status model
- idempotency scope
- evidence cho accepted, running, completed
- recovery path
- reversal trigger

<!-- scene: S08 | source: UNSOURCED curriculum transfer scenario -->

---

## Exit check

Contract khác implementation plan ở đâu?

Contract khóa behavior và evidence.

Implementation chọn cơ chế đạt behavior đó.

<!-- scene: S09 -->

---

## Mang theo sau buổi học

> Hai reviewer có tạo cùng expected result từ cùng fixture không?

Nếu không, hãy tiếp tục làm rõ contract.

---

## References

- [[wiki.engineering-foundation.testable-contract|From a vague request to a testable contract]]
- [[wiki.data-product.requirements-traceability|Requirements traceability]]
- [[wiki.data-quality.sli-slo-design|Data SLI and SLO design]]
