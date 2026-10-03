---
marp: true
theme: volt
paginate: true
size: 16:9
header: 'DE · Lesson 1'
footer: 'Foundation · runnable scene package'
---

<!-- _class: lead -->

# From a vague request to a testable contract

**DE-L001 · 120 phút (ước tính)**

> Làm sao biến yêu cầu kỹ thuật mơ hồ thành behavior và acceptance check có thể tái hiện?

---

## Chuẩn đầu ra

Viết testable contract khóa decision, boundary, input/output, invariants, failure behavior và evidence trước mutation.

**Evidence:** Hai reviewer độc lập tạo cùng expected output từ fixture và trace mỗi failed check về requirement/owner.

**Không suy ra mastery từ việc có mặt hoặc xem hết slide.**

---

<!-- scene: S01 · source: note.md: heading '1. Bắt đầu từ quyết định, không bắt đầu từ giải pháp' -->
## Tình huống mở

Yêu cầu 'đồng bộ orders nhanh và không trùng' không nói nhanh bao nhiêu, order nào, identity nào hay retry sau timeout phải quan sát gì.

**Think–pair–share · 4 phút**

1. Bạn sẽ làm gì đầu tiên?
2. Quyết định nào có thể bị ảnh hưởng?
3. Bằng chứng nào đang thiếu?

---

<!-- scene: S02 · source: note.md: heading '2. Sáu phần của một phát biểu kiểm thử được' -->
## Mental model trung tâm

> Contract kiểm thử được mô tả behavior quan sát được trong boundary rõ, gồm precondition, input, transformation, expected output, failure semantics và acceptance evidence.

- Bắt đầu từ quyết định và consumer harm, rồi khóa scope/non-goal.
- Viết identity, state, time, input/output và invariant đủ để reviewer dựng expected result.
- Gắn mỗi requirement với acceptance check và owner. unknown làm đổi semantics phải chặn mutation.

---

## Luồng kiểm soát

| 1. Câu hỏi hoặc thay đổi | 2. Boundary | 3. Evidence | 4. Decision gate | 5. Theo dõi |
|---|---|---|---|---|
| Nêu outcome cần quyết định | Khóa scope và semantics | Dùng phép kiểm độc lập | Áp dụng có giới hạn hoặc dừng | Quan sát reversal trigger |

---

## Bước đầu tiên có tính quyết định

**Hỏi consumer cần behavior nào và failure nào không được phép xảy ra.**

Không làm bước này, output sau đó có thể đúng cú pháp nhưng sai đối tượng, sai thời gian hoặc sai quyết định.

---

<!-- scene: S03 · source: note.md: heading '2. Sáu phần của một phát biểu kiểm thử được' -->
## Check 1 · trả lời không nhìn tài liệu

**Một expected output tốt phải có tính chất gì?**

<details>
<summary>Đáp án và tín hiệu chẩn đoán</summary>

Hai reviewer độc lập suy ra cùng kết quả từ cùng fixture.

Nếu câu trả lời chỉ nêu tên công cụ, hãy quay lại mental model và nói rõ boundary + evidence + action.
</details>

---

<!-- scene: S04 · source: UNSOURCED guided practice synthesis -->
## Guided practice · 12 phút làm + 6 phút chữa

Biến sáu câu requirement mơ hồ thành Given/When/Then có fixture, invariant và failure path.

**Definition of done:** Mỗi check có input cụ thể, expected result duy nhất, oracle và requirement ID. không dùng từ định tính chưa có threshold.

Người dạy không chữa bằng đáp án ngay. yêu cầu mỗi nhóm nêu assumption và phép kiểm trước.

---

<!-- scene: S05 · source: note.md: heading '3. Từ requirement tới acceptance check' -->
## Quy tắc quyết định

Nếu thiếu identity, state transition hoặc failure semantics thì dừng. nếu chỉ thiếu threshold tối ưu có thể pilot trong bounded range và giữ reversal trigger.

**Boundary:** Contract tốt không thay thế thiết kế hay test runtime. nó định nghĩa điều các bước đó phải chứng minh.

---

## Changed constraint

<!-- scene: S06 · source: UNSOURCED changed-constraint synthesis -->

Khi SLO từ 10 phút xuống 30 giây, contract buộc lộ thay đổi kiến trúc thay vì coi đây là tuning nhỏ.

**Thảo luận:** lựa chọn nào còn defensible? Bằng chứng nào làm bạn đảo quyết định?

---

## Worked example · đi từng bước

<!-- scene: S07 · source: note.md: heading '6. Definition of Ready và điểm dừng' -->

1. Định nghĩa order identity = source + order_id. event time và D+1 cutoff.
2. Success: mỗi identity xuất hiện đúng một lần ở curated table trong 10 phút.
3. Timeout có outcome unknown. retry phải idempotent và đối soát bằng run_id.
4. Non-goal: không backfill trước ngày X. change request nếu stakeholder mở rộng.

---

## Evidence phải giữ lại

Hai reviewer độc lập tạo cùng expected output từ fixture và trace mỗi failed check về requirement/owner.

Một output không có boundary, oracle hoặc limitation chỉ là kết quả chưa review.

---

## Failure modes

- **Critical:** Viết acceptance bằng từ mơ hồ như nhanh/ổn định, hoặc để implementation tự quyết semantics.
- Chỉ kiểm happy path và sửa expected sau khi nhìn output.
- Gộp author claim, curriculum synthesis và learner conclusion thành một giọng.
- Dùng số lượng biểu đồ/test để thay thế oracle độc lập.

---

## Independent practice · không có đáp án mẫu

Viết contract cho job ingest orders có retry, late data và delete. thêm traceability matrix hai chiều.

**Nộp:** artifact + evidence + limitation + reversal trigger.

---

<!-- scene: S08 · source: UNSOURCED curriculum transfer scenario -->
## Transfer challenge

API trả 202 nhưng commit outcome unknown. Định nghĩa behavior client, idempotency key và evidence phân biệt accepted với completed.

Được phép có nhiều lựa chọn. Điểm nằm ở boundary, trade-off, evidence và blast radius: không nằm ở việc đoán ý người dạy.

---

<!-- scene: S09 · source: note.md: heading '8. Failure modes và ngộ nhận' -->
## Exit ticket · 3 phút

**Vì sao 'pipeline không được trùng dữ liệu' chưa phải acceptance criterion?**

<details><summary>Đáp án tối thiểu</summary>

Chưa có identity, boundary, time, trạng thái và phép đếm/oracle nên không thể tạo expected output duy nhất.
</details>

---

## Sau buổi học

1. Làm `quiz.md`. đạt **8/10**.
2. Nếu trượt một concept, đọc remediation trong `after-note.md` rồi retest đúng concept đó.
3. Hoàn thành `homework.md`. đạt **≥ 75/100** và không có critical failure.

**Bắc cầu:** DE-L002: phân rã responsibility, interface, state và failure domain.
