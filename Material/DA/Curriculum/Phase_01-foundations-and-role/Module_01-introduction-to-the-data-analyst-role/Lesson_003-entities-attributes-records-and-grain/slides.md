---
marp: true
theme: volt
paginate: true
size: 16:9
header: 'DA · Lesson 3'
footer: 'Foundation · runnable scene package'
---

<!-- _class: lead -->

# Entities, attributes, records and grain

**DA-L003**

> Mỗi dòng đại diện cho điều gì và phép tính nào hợp lệ ở grain đó?

---

## Chuẩn đầu ra

Phát biểu và kiểm chứng grain, khóa ứng viên, rồi định lượng fan-out khi ghép hai bảng khác grain.

**Evidence:** Bảng kiểm grain gồm candidate key, uniqueness, row count, distinct key, join multiplicity và reconciliation total.

**Không suy ra mastery từ việc có mặt hoặc xem hết slide.**

---

<!-- scene: S01 · source: note.md: heading Problem Definition and Operational Relevance -->
## Tình huống mở

Một đơn có ba dòng sản phẩm. Join orders với order_items rồi SUM(order_total) làm doanh thu tăng gấp ba dù query chạy hoàn hảo.

**Independent analysis followed by peer review**

1. Bạn sẽ làm gì đầu tiên?
2. Quyết định nào có thể bị ảnh hưởng?
3. Bằng chứng nào đang thiếu?

---

<!-- scene: S02 · source: note.md: heading Mechanism -->
## Mental model trung tâm

> Grain là lời cam kết mỗi dòng đại diện cho điều gì. mọi phép đếm, join và aggregate phải được chứng minh tương thích với lời cam kết đó.

- Xác định entity và một câu grain đầy đủ có thời gian/trạng thái khi cần.
- Kiểm uniqueness của khóa ứng viên và phân phối số dòng trên mỗi key.
- Dự đoán cardinality trước join, đo fan-out sau join và aggregate về grain chung trước khi kết hợp.

---

## Luồng kiểm soát

| 1. Câu hỏi hoặc thay đổi | 2. Boundary | 3. Evidence | 4. Decision gate | 5. Theo dõi |
|---|---|---|---|---|
| Nêu outcome cần quyết định | Khóa scope và semantics | Dùng phép kiểm độc lập | Áp dụng có giới hạn hoặc dừng | Quan sát reversal trigger |

---

## Bước đầu tiên có tính quyết định

**Viết câu 'mỗi dòng đại diện cho…' và khóa ứng viên trước bất kỳ SUM hoặc JOIN nào.**

Không làm bước này, output sau đó có thể đúng cú pháp nhưng sai đối tượng, sai thời gian hoặc sai quyết định.

---

<!-- scene: S03 · source: note.md: heading Mechanism -->
## Check 1 · trả lời không nhìn tài liệu

**Grain là gì?**

<details>
<summary>Đáp án và tín hiệu chẩn đoán</summary>

Lời cam kết một dòng đại diện cho đối tượng/sự kiện nào trong boundary đã nêu.

Nếu câu trả lời chỉ nêu tên công cụ, hãy quay lại mental model và nói rõ boundary + evidence + action.
</details>

---

<!-- scene: S04 · source: UNSOURCED guided practice synthesis -->
## Guided practice

Cho năm schema nhỏ. viết grain, candidate key, cardinality dự kiến và một query/profile chứng minh cho từng bảng.

**Definition of done:** 5/5 câu grain có entity + thời gian/trạng thái phù hợp và mỗi câu có phép kiểm uniqueness/fan-out tương ứng.

Người dạy không chữa bằng đáp án ngay. yêu cầu mỗi nhóm nêu assumption và phép kiểm trước.

---

<!-- scene: S05 · source: note.md: heading Decision Framework -->
## Quy tắc quyết định

Nếu hai bảng khác grain, hoặc aggregate bảng nhiều về grain một trước join, hoặc giữ measure ở bảng sở hữu. không SUM measure phía một sau join many.

**Boundary:** Khóa duy nhất về kỹ thuật chưa đủ nếu một dòng vẫn trộn nhiều trạng thái nghiệp vụ hoặc snapshot time khác nhau.

---

## Changed constraint

<!-- scene: S06 · source: UNSOURCED changed-constraint synthesis -->

Nếu yêu cầu chuyển từ đơn sang khách-tháng, phải công bố grain mới và rule phân bổ trước khi tổng hợp.

**Thảo luận:** lựa chọn nào còn defensible? Bằng chứng nào làm bạn đảo quyết định?

---

## Worked example · đi từng bước

<!-- scene: S07 · source: note.md: heading Worked Case: một chỉ số bán hàng đổi nghĩa giữa đường -->

1. Orders ở grain một dòng/đơn. items ở grain một dòng/sản phẩm trong đơn.
2. Dự đoán join one-to-many và đánh dấu order_total không additive sau join.
3. Aggregate items về order_id hoặc chỉ lấy order_total một lần trên orders.
4. Đối soát doanh thu và số đơn trước/sau join bằng oracle riêng.

---

## Evidence phải giữ lại

Bảng kiểm grain gồm candidate key, uniqueness, row count, distinct key, join multiplicity và reconciliation total.

Một output không có boundary, oracle hoặc limitation chỉ là kết quả chưa review.

---

## Failure modes

- **Critical:** Suy grain từ tên bảng, dùng DISTINCT để che fan-out hoặc coi primary key kỹ thuật là nghĩa nghiệp vụ.
- Chỉ kiểm happy path và sửa expected sau khi nhìn output.
- Gộp author claim, curriculum synthesis và learner conclusion thành một giọng.
- Dùng số lượng biểu đồ/test để thay thế oracle độc lập.

---

## Independent practice · không có đáp án mẫu

Chẩn đoán workbook doanh thu bị thổi phồng 18%. tái cấu trúc phép join và lập reconciliation trước/sau.

**Nộp:** artifact + evidence + limitation + reversal trigger.

---

<!-- scene: S08 · source: UNSOURCED curriculum transfer scenario -->
## Transfer challenge

Một bảng customer_address lưu lịch sử hiệu lực. Chọn grain và join rule để gán đúng địa chỉ tại thời điểm order.

Được phép có nhiều lựa chọn. Điểm nằm ở boundary, trade-off, evidence và blast radius: không nằm ở việc đoán ý người dạy.

---

<!-- scene: S09 · source: note.md: heading Limits and Common Errors -->
## Exit check

**Tại sao DISTINCT không phải cách sửa mặc định cho fan-out?**

<details><summary>Đáp án tối thiểu</summary>

DISTINCT có thể xóa record hợp lệ và che mismatch grain. phải sửa cardinality hoặc aggregate về grain đúng.
</details>

---

## Post-Lesson

1. Làm `quiz.md`. đạt **8/10**.
2. Nếu trượt một concept, đọc remediation trong `after-note.md` rồi retest đúng concept đó.
3. Hoàn thành `homework.md`. đạt **≥ 75/100** và không có critical failure.

**Bắc cầu:** L004: phân rã outcome thành metric tree có driver hành động được.

---

## References

- [[wiki.da-foundation.entity-attribute-record-and-grain|Entities, attributes, records and grain]]
- [[wiki.data-modeling.fact-table-types|Fact table types]]
- [[wiki.database.joins-duplicate-multiplication-null|Join multiplication and NULL behavior]]
