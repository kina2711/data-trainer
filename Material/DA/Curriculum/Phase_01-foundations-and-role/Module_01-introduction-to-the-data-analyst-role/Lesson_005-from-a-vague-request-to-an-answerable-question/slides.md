---
marp: true
theme: volt
paginate: true
size: 16:9
header: 'DA · Lesson 5'
footer: 'Foundation · runnable scene package'
---

<!-- _class: lead -->

# From a vague request to an answerable question

**DA-L005**

> Làm sao chuyển yêu cầu mơ hồ thành analytical contract có thể bác bỏ?

---

## Chuẩn đầu ra

Viết contract khóa decision, population, metric, comparison, time, slices, constraints và acceptance trước khi phân tích.

**Evidence:** Một analytical contract một trang và test bằng hai reviewer độc lập tạo cùng expected output từ cùng fixture.

**Không suy ra mastery từ việc có mặt hoặc xem hết slide.**

---

<!-- scene: S01 · source: note.md: heading Problem Definition and Operational Relevance -->
## Tình huống mở

Câu 'phân tích giúp vì sao khách giảm' có ít nhất năm nghĩa của khách, ba cửa sổ thời gian và nhiều quyết định khác nhau.

**Independent analysis followed by peer review**

1. Bạn sẽ làm gì đầu tiên?
2. Quyết định nào có thể bị ảnh hưởng?
3. Bằng chứng nào đang thiếu?

---

<!-- scene: S02 · source: note.md: heading Mechanism -->
## Mental model trung tâm

> Một câu hỏi trả lời được phải nêu ai sẽ quyết định gì, trên population nào, bằng metric/comparison nào, trong time boundary nào và bằng chứng nào đủ để dừng.

- Bắt đầu bằng decision và action threshold, không bắt đầu bằng danh sách biểu đồ.
- Khóa population, identity/grain, metric, comparison, time, segments và exclusions.
- Ghi assumptions, unknowns, non-goals, deliverable, deadline và acceptance check có thể bác bỏ.

---

## Luồng kiểm soát

| 1. Câu hỏi hoặc thay đổi | 2. Boundary | 3. Evidence | 4. Decision gate | 5. Theo dõi |
|---|---|---|---|---|
| Nêu outcome cần quyết định | Khóa scope và semantics | Dùng phép kiểm độc lập | Áp dụng có giới hạn hoặc dừng | Quan sát reversal trigger |

---

## Bước đầu tiên có tính quyết định

**Hỏi 'ai sẽ làm gì khác đi nếu kết quả cao, thấp hoặc chưa đủ chắc chắn?'.**

Không làm bước này, output sau đó có thể đúng cú pháp nhưng sai đối tượng, sai thời gian hoặc sai quyết định.

---

<!-- scene: S03 · source: note.md: heading Mechanism -->
## Check 1 · trả lời không nhìn tài liệu

**Trường đầu tiên của analytical contract là gì?**

<details>
<summary>Đáp án và tín hiệu chẩn đoán</summary>

Decision và hành động mà kết quả sẽ hỗ trợ.

Nếu câu trả lời chỉ nêu tên công cụ, hãy quay lại mental model và nói rõ boundary + evidence + action.
</details>

---

<!-- scene: S04 · source: UNSOURCED guided practice synthesis -->
## Guided practice

Phỏng vấn role-play: stakeholder chỉ nói 'campaign vừa rồi có hiệu quả không?'. nhóm có 12 phút để tạo contract và read-back.

**Definition of done:** Contract đủ tám trường semantic, có non-goal, acceptance và ít nhất một unknown với owner.

Người dạy không chữa bằng đáp án ngay. yêu cầu mỗi nhóm nêu assumption và phép kiểm trước.

---

<!-- scene: S05 · source: note.md: heading Decision Framework -->
## Quy tắc quyết định

Unknown làm đổi semantics, blast radius hoặc acceptance phải chặn execution. unknown định lượng được có thể đi tiếp với coverage và limitation công khai.

**Boundary:** Contract khóa nghĩa và tiêu chí. nó không bảo đảm source có đủ dữ liệu hay kết luận sẽ có causal strength mong muốn.

---

## Changed constraint

<!-- scene: S06 · source: UNSOURCED changed-constraint synthesis -->

Nếu deadline từ ba ngày xuống hai giờ, co scope và strength of claim. không âm thầm hạ correctness gate.

**Thảo luận:** lựa chọn nào còn defensible? Bằng chứng nào làm bạn đảo quyết định?

---

## Worked example · đi từng bước

<!-- scene: S07 · source: note.md: heading Worked Case: một chỉ số bán hàng đổi nghĩa giữa đường -->

1. Đổi 'khách giảm' thành paid customers tháng 9 so tháng 8 theo event time ICT, chốt D+3.
2. Định nghĩa paid customer là distinct customer_id có payment_success, loại test/refund toàn phần.
3. Slice theo acquisition channel và device vì owner có lever tương ứng.
4. Acceptance: reconcile với finance ±0,5%. nếu coverage <98% thì trả lời có điều kiện.

---

## Evidence phải giữ lại

Một analytical contract một trang và test bằng hai reviewer độc lập tạo cùng expected output từ cùng fixture.

Một output không có boundary, oracle hoặc limitation chỉ là kết quả chưa review.

---

## Failure modes

- **Critical:** Tự điền định nghĩa để kịp deadline, hoặc nhận deliverable 'dashboard' trước khi biết decision.
- Chỉ kiểm happy path và sửa expected sau khi nhìn output.
- Gộp author claim, curriculum synthesis và learner conclusion thành một giọng.
- Dùng số lượng biểu đồ/test để thay thế oracle độc lập.

---

## Independent practice · không có đáp án mẫu

Viết contract một trang cho yêu cầu retention giảm. đổi một constraint rồi cập nhật scope, test và deliverable.

**Nộp:** artifact + evidence + limitation + reversal trigger.

---

<!-- scene: S08 · source: UNSOURCED curriculum transfer scenario -->
## Transfer challenge

CEO muốn câu trả lời trong hai giờ nhưng identity khách đa thiết bị chưa được giải quyết. Chọn dừng, co claim hay dùng proxy và nêu điều kiện.

Được phép có nhiều lựa chọn. Điểm nằm ở boundary, trade-off, evidence và blast radius: không nằm ở việc đoán ý người dạy.

---

<!-- scene: S09 · source: note.md: heading Limits and Common Errors -->
## Exit check

**Unknown nào bắt buộc phải chặn phân tích?**

<details><summary>Đáp án tối thiểu</summary>

Unknown có thể đổi nghĩa population/metric, blast radius hoặc tiêu chí đạt. identity chưa rõ là ví dụ điển hình.
</details>

---

## Post-Lesson

1. Làm `quiz.md`. đạt **8/10**.
2. Nếu trượt một concept, đọc remediation trong `after-note.md` rồi retest đúng concept đó.
3. Hoàn thành `homework.md`. đạt **≥ 75/100** và không có critical failure.

**Bắc cầu:** DA-L006: cấu trúc dữ liệu đúng trong Excel theo contract đã khóa.

---

## References

- [[wiki.da-foundation.vague-request-to-answerable-question|From a vague request to an answerable question]]
- [[wiki.semantic-layer.metric-contract|From a business question to a metric contract]]
- [[wiki.data-product.requirements-traceability|Requirements traceability]]
