---
marp: true
theme: volt
paginate: true
size: 16:9
header: 'DE · Lesson 2'
footer: 'Foundation · runnable scene package'
---

<!-- _class: lead -->

# Decomposition: responsibility, interface, state and failure domain

**DE-L002**

> Làm sao chia hệ thành boundary thay đổi và hỏng theo cách có thể kiểm chứng?

---

## Chuẩn đầu ra

Phân rã hệ theo responsibility, interface, state, dependency direction và failure domain. kiểm bằng change/fault scenarios.

**Evidence:** Context/component diagram, interface contract, state ownership table, dependency DAG và ba fault traces.

**Không suy ra mastery từ việc có mặt hoặc xem hết slide.**

---

<!-- scene: S01 · source: note.md: heading 1. Ranh giới bắt đầu từ responsibility -->
## Tình huống mở

Tách monolith thành ba service nhưng cả ba dùng chung database và credential: network tăng, blast radius không giảm.

**Independent analysis followed by peer review**

1. Bạn sẽ làm gì đầu tiên?
2. Quyết định nào có thể bị ảnh hưởng?
3. Bằng chứng nào đang thiếu?

---

<!-- scene: S02 · source: note.md: heading 2. Interface là lời hứa tối thiểu -->
## Mental model trung tâm

> Boundary tốt gom invariant và lý do thay đổi, thu hẹp interface, có owner state rõ và làm failure propagation quan sát/kiểm soát được.

- Dùng change scenario để tìm responsibility và cohesion thay vì chỉ chia theo technical layer.
- Thiết kế interface bằng operation, semantics, errors và invariants tối thiểu.
- Gắn state với authoritative writer/lifecycle. trace fault tới consumer harm và recovery.

---

## Luồng kiểm soát

| 1. Câu hỏi hoặc thay đổi | 2. Boundary | 3. Evidence | 4. Decision gate | 5. Theo dõi |
|---|---|---|---|---|
| Nêu outcome cần quyết định | Khóa scope và semantics | Dùng phép kiểm độc lập | Áp dụng có giới hạn hoặc dừng | Quan sát reversal trigger |

---

## Bước đầu tiên có tính quyết định

**Liệt kê invariants và các thay đổi độc lập, rồi hỏi phần nào phải đổi cùng nhau.**

Không làm bước này, output sau đó có thể đúng cú pháp nhưng sai đối tượng, sai thời gian hoặc sai quyết định.

---

<!-- scene: S03 · source: note.md: heading 2. Interface là lời hứa tối thiểu -->
## Check 1 · trả lời không nhìn tài liệu

**Responsibility nên được tìm bằng gì?**

<details>
<summary>Đáp án và tín hiệu chẩn đoán</summary>

Invariant và lý do thay đổi nghiệp vụ/vận hành, không chỉ technical layer.

Nếu câu trả lời chỉ nêu tên công cụ, hãy quay lại mental model và nói rõ boundary + evidence + action.
</details>

---

<!-- scene: S04 · source: UNSOURCED guided practice synthesis -->
## Guided practice

Phân rã order-payment-fulfillment trên bốn trục. inject timeout payment và database outage rồi trace impact.

**Definition of done:** Mỗi component có một responsibility, interface tối thiểu, state owner, dependencies không vòng và failure trace tới recovery.

Người dạy không chữa bằng đáp án ngay. yêu cầu mỗi nhóm nêu assumption và phép kiểm trước.

---

<!-- scene: S05 · source: note.md: heading 3. State quyết định độ khó thay thế -->
## Quy tắc quyết định

Tách boundary khi change cadence, invariant/state ownership hoặc fault containment khác nhau và cost network/operation được biện minh.

**Boundary:** Deployment unit không tự tạo failure isolation. shared database, queue hoặc credential vẫn có thể nối blast radius.

---

## Changed constraint

<!-- scene: S06 · source: UNSOURCED changed-constraint synthesis -->

Đổi database không được buộc domain import driver type. nếu có, dependency direction đang sai.

**Thảo luận:** lựa chọn nào còn defensible? Bằng chứng nào làm bạn đảo quyết định?

---

## Worked example · đi từng bước

<!-- scene: S07 · source: note.md: heading 4. Failure domain không đồng nghĩa deployment unit -->

1. Tách order intent, payment adapter và fulfillment theo invariant/lifecycle.
2. Order là authoritative owner của state machine. payment trả outcome contract thay vì ORM object.
3. Timeout payment không làm mất order intent. retry dựa trên idempotency key.
4. Dependency đi từ domain policy ra ports. adapter phụ thuộc contract, không ngược lại.

---

## Evidence phải giữ lại

Context/component diagram, interface contract, state ownership table, dependency DAG và ba fault traces.

Một output không có boundary, oracle hoặc limitation chỉ là kết quả chưa review.

---

## Failure modes

- **Critical:** Chia theo folder/service aesthetic, để nhiều writer cho cùng state hoặc public interface lộ storage detail.
- Chỉ kiểm happy path và sửa expected sau khi nhìn output.
- Gộp author claim, curriculum synthesis và learner conclusion thành một giọng.
- Dùng số lượng biểu đồ/test để thay thế oracle độc lập.

---

## Independent practice · không có đáp án mẫu

Thiết kế decomposition cho ingestion service gồm fetch, normalize, dedup, publish và checkpoint. bảo vệ quyết định trước hai fault.

**Nộp:** artifact + evidence + limitation + reversal trigger.

---

<!-- scene: S08 · source: UNSOURCED curriculum transfer scenario -->
## Transfer challenge

Hai team cần đổi schema với cadence khác nhưng dùng chung dedup ledger. Chọn tách ở đâu và ai sở hữu migration/recovery.

Được phép có nhiều lựa chọn. Điểm nằm ở boundary, trade-off, evidence và blast radius: không nằm ở việc đoán ý người dạy.

---

<!-- scene: S09 · source: note.md: heading 8. Failure modes và ngộ nhận -->
## Exit check

**Vì sao tách process chưa chắc giảm failure domain?**

<details><summary>Đáp án tối thiểu</summary>

Các process có thể vẫn chung dependency/state/credential. fault ở shared resource tiếp tục ảnh hưởng tất cả.
</details>

---

## Post-Lesson

1. Làm `quiz.md`. đạt **8/10**.
2. Nếu trượt một concept, đọc remediation trong `after-note.md` rồi retest đúng concept đó.
3. Hoàn thành `homework.md`. đạt **≥ 75/100** và không có critical failure.

**Bắc cầu:** DE-L003: ghi trade-off và reversal trigger bằng ADR.

---

## References

- [[wiki.engineering-foundation.decomposition-four-axes|Decomposition across four axes]]
- [[wiki.data-product.requirements-traceability|Requirements traceability]]
- [[wiki.backend.idempotency-keys-deduplication-state|Idempotency keys and deduplication state]]
