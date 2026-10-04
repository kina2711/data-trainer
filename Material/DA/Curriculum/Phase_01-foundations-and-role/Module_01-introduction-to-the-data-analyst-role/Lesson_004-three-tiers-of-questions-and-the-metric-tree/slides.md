---
marp: true
theme: volt
paginate: true
size: 16:9
header: 'DA · Lesson 4'
footer: 'Foundation · runnable scene package'
---

<!-- _class: lead -->

# Three tiers of questions and the metric tree

**DA-L004**

> Làm sao đi từ outcome biến động tới driver có owner và hành động?

---

## Chuẩn đầu ra

Dựng metric tree cân bằng số học, nối descriptive-diagnostic-prescriptive questions và bảo vệ driver bằng owner cùng lever.

**Evidence:** Metric tree cân bằng trên fixture, mỗi lá có definition, grain, owner, lever và test cộng/nhân lại outcome.

**Không suy ra mastery từ việc có mặt hoặc xem hết slide.**

---

<!-- scene: S01 · source: note.md: heading Problem Definition and Operational Relevance -->
## Tình huống mở

Revenue giảm 8%. Chia theo mọi dimension tạo 40 biểu đồ nhưng không cho biết driver nào có thể can thiệp.

**Independent analysis followed by peer review**

1. Bạn sẽ làm gì đầu tiên?
2. Quyết định nào có thể bị ảnh hưởng?
3. Bằng chứng nào đang thiếu?

---

<!-- scene: S02 · source: note.md: heading Mechanism -->
## Mental model trung tâm

> Metric tree là mô hình giả thuyết định lượng: outcome được phân rã thành driver có thể đo, có owner và lever. ba tầng câu hỏi dẫn từ quan sát tới quyết định.

- Bắt đầu từ decision/outcome và viết identity toán học hoặc quan hệ nhân quả có điều kiện.
- Phân rã driver đến mức đo được và can thiệp được, tránh trộn stock, flow và rate.
- Đi từ descriptive sang diagnostic rồi prescriptive. mỗi nhánh có owner, evidence và reversal trigger.

---

## Luồng kiểm soát

| 1. Câu hỏi hoặc thay đổi | 2. Boundary | 3. Evidence | 4. Decision gate | 5. Theo dõi |
|---|---|---|---|---|
| Nêu outcome cần quyết định | Khóa scope và semantics | Dùng phép kiểm độc lập | Áp dụng có giới hạn hoặc dừng | Quan sát reversal trigger |

---

## Bước đầu tiên có tính quyết định

**Xác định quyết định và công thức outcome trước khi chọn dimension để cắt lát.**

Không làm bước này, output sau đó có thể đúng cú pháp nhưng sai đối tượng, sai thời gian hoặc sai quyết định.

---

<!-- scene: S03 · source: note.md: heading Mechanism -->
## Check 1 · trả lời không nhìn tài liệu

**Ba tầng câu hỏi là gì?**

<details>
<summary>Đáp án và tín hiệu chẩn đoán</summary>

Descriptive: chuyện gì. diagnostic: vì sao. prescriptive: nên làm gì.

Nếu câu trả lời chỉ nêu tên công cụ, hãy quay lại mental model và nói rõ boundary + evidence + action.
</details>

---

<!-- scene: S04 · source: UNSOURCED guided practice synthesis -->
## Guided practice

Dựng cây revenue cho marketplace từ GMV tới traffic, conversion, orders, AOV, take rate và refunds. đánh dấu stock/flow/rate.

**Definition of done:** Cây cân bằng trên số mẫu, không double count, mọi lá có owner và ít nhất một lever kiểm được.

Người dạy không chữa bằng đáp án ngay. yêu cầu mỗi nhóm nêu assumption và phép kiểm trước.

---

<!-- scene: S05 · source: note.md: heading Decision Framework -->
## Quy tắc quyết định

Chỉ đưa driver vào nhánh hành động khi definition và grain ổn định, có owner/lever, và contribution đủ lớn so với uncertainty và cost can thiệp.

**Boundary:** Metric tree biểu diễn giả thuyết và identity. nó không chứng minh quan hệ nhân quả chỉ vì các nhánh cộng đúng.

---

## Changed constraint

<!-- scene: S06 · source: UNSOURCED changed-constraint synthesis -->

Nếu margin thay revenue làm outcome, discount có thể đổi từ lever tích cực thành driver phá giá trị. cây phải được dựng lại theo decision.

**Thảo luận:** lựa chọn nào còn defensible? Bằng chứng nào làm bạn đảo quyết định?

---

## Worked example · đi từng bước

<!-- scene: S07 · source: note.md: heading Worked Case: một chỉ số bán hàng đổi nghĩa giữa đường -->

1. Revenue = Orders × Average Order Value.
2. Orders = Traffic × Conversion Rate. AOV = Items/Order × Price/Item.
3. Đối chiếu đóng góp driver với mức giảm 8% và giữ interaction/residual.
4. Chọn lever checkout conversion vì có owner, đủ volume và cost thử nghiệm thấp hơn giảm giá toàn site.

---

## Evidence phải giữ lại

Metric tree cân bằng trên fixture, mỗi lá có definition, grain, owner, lever và test cộng/nhân lại outcome.

Một output không có boundary, oracle hoặc limitation chỉ là kết quả chưa review.

---

## Failure modes

- **Critical:** Cây chỉ là taxonomy đẹp, lá không có owner, hoặc diễn giải tương quan như nguyên nhân.
- Chỉ kiểm happy path và sửa expected sau khi nhìn output.
- Gộp author claim, curriculum synthesis và learner conclusion thành một giọng.
- Dùng số lượng biểu đồ/test để thay thế oracle độc lập.

---

## Independent practice · không có đáp án mẫu

Dựng ba cây cho subscription, marketplace và vận hành giao hàng. viết một câu hỏi ở mỗi tầng cho từng cây.

**Nộp:** artifact + evidence + limitation + reversal trigger.

---

<!-- scene: S08 · source: UNSOURCED curriculum transfer scenario -->
## Transfer challenge

Conversion giảm nhưng revenue tăng do AOV. Quyết định ưu tiên driver nào khi mục tiêu đổi từ tăng trưởng sang contribution margin?

Được phép có nhiều lựa chọn. Điểm nằm ở boundary, trade-off, evidence và blast radius: không nằm ở việc đoán ý người dạy.

---

<!-- scene: S09 · source: note.md: heading Limits and Common Errors -->
## Exit check

**Một metric tree cộng đúng đã đủ để kết luận nguyên nhân chưa?**

<details><summary>Đáp án tối thiểu</summary>

Chưa. Identity mô tả đóng góp số học. causal claim cần thiết kế bằng chứng riêng và loại trừ confounder.
</details>

---

## Post-Lesson

1. Làm `quiz.md`. đạt **8/10**.
2. Nếu trượt một concept, đọc remediation trong `after-note.md` rồi retest đúng concept đó.
3. Hoàn thành `homework.md`. đạt **≥ 75/100** và không có critical failure.

**Bắc cầu:** L005: biến yêu cầu mơ hồ thành analytical contract trả lời được.

---

## References

- [[wiki.da-foundation.three-question-tiers-and-metric-tree|Three question tiers and the metric tree]]
- [[wiki.data-product.metric-tree|Question decomposition and the metric tree]]
- [[wiki.data-product.decision-first-discovery|Decision-First Discovery]]
