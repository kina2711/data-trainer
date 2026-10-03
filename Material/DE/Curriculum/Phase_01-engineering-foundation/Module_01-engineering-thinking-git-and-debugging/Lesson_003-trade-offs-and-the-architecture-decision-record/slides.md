---
marp: true
theme: volt
paginate: true
size: 16:9
header: 'DE · Lesson 3'
footer: 'Foundation · runnable scene package'
---

<!-- _class: lead -->

# Trade-offs and the architecture decision record

**DE-L003 · 120 phút (ước tính)**

> Làm sao lưu reasoning để quyết định kỹ thuật có thể được tái tạo và xét lại?

---

## Chuẩn đầu ra

Viết ADR ngắn nhưng đủ context, drivers, options, evidence, consequences, decision và revisit signal.

**Evidence:** Reviewer tái tạo recommendation từ drivers/evidence và changed constraint làm recommendation đảo đúng rule.

**Không suy ra mastery từ việc có mặt hoặc xem hết slide.**

---

<!-- scene: S01 · source: note.md: heading '1. ADR lưu reasoning, không chỉ lưu kết luận' -->
## Tình huống mở

ADR chỉ ghi 'chọn Parquet' khiến đội sau không biết workload nào, option nào bị loại hay constraint nào đã đổi.

**Think–pair–share · 4 phút**

1. Bạn sẽ làm gì đầu tiên?
2. Quyết định nào có thể bị ảnh hưởng?
3. Bằng chứng nào đang thiếu?

---

<!-- scene: S02 · source: note.md: heading '2. Khóa tiêu chí trước khi so phương án' -->
## Mental model trung tâm

> ADR lưu context và reasoning tại thời điểm quyết định. chất lượng nằm ở option thật, hard constraints, evidence phân biệt và điều kiện đảo quyết định.

- Khóa decision drivers và hard constraints trước khi chấm option.
- Mô tả ít nhất hai option trong điều kiện tốt nhất, gồm failure mode và evidence có thể đảo đánh giá.
- Ghi consequences, owner, reversibility, confirmation và measurable revisit signal.

---

## Luồng kiểm soát

| 1. Câu hỏi hoặc thay đổi | 2. Boundary | 3. Evidence | 4. Decision gate | 5. Theo dõi |
|---|---|---|---|---|
| Nêu outcome cần quyết định | Khóa scope và semantics | Dùng phép kiểm độc lập | Áp dụng có giới hạn hoặc dừng | Quan sát reversal trigger |

---

## Bước đầu tiên có tính quyết định

**Viết context, decision scope và hard constraints trước khi nêu phương án yêu thích.**

Không làm bước này, output sau đó có thể đúng cú pháp nhưng sai đối tượng, sai thời gian hoặc sai quyết định.

---

<!-- scene: S03 · source: note.md: heading '2. Khóa tiêu chí trước khi so phương án' -->
## Check 1 · trả lời không nhìn tài liệu

**ADR lưu gì quan trọng nhất?**

<details>
<summary>Đáp án và tín hiệu chẩn đoán</summary>

Context và reasoning đủ để tái tạo quyết định khi constraint thay đổi.

Nếu câu trả lời chỉ nêu tên công cụ, hãy quay lại mental model và nói rõ boundary + evidence + action.
</details>

---

<!-- scene: S04 · source: UNSOURCED guided practice synthesis -->
## Guided practice · 12 phút làm + 6 phút chữa

Điền ADR one-page cho format trao đổi dữ liệu từ evidence packet. mỗi nhóm đóng vai reviewer tấn công một assumption.

**Definition of done:** ADR dưới hai trang, có ≥2 option thật, hard constraints, evidence, consequence owner và measurable revisit signal.

Người dạy không chữa bằng đáp án ngay. yêu cầu mỗi nhóm nêu assumption và phép kiểm trước.

---

<!-- scene: S05 · source: note.md: heading '3. Phương án bị loại là tài sản' -->
## Quy tắc quyết định

Loại option vi phạm hard constraint trước. trong số option còn lại ưu tiên evidence, reversibility và total cost, không dùng weighted score để bù vi phạm cấm.

**Boundary:** ADR không thay thế benchmark, spike hay approval. nó liên kết evidence đó với quyết định phiên bản cụ thể.

---

## Changed constraint

<!-- scene: S06 · source: UNSOURCED changed-constraint synthesis -->

Nếu consumer chính chuyển sang spreadsheet không hỗ trợ Parquet, compatibility gate có thể đảo quyết định dù benchmark không đổi.

**Thảo luận:** lựa chọn nào còn defensible? Bằng chứng nào làm bạn đảo quyết định?

---

## Worked example · đi từng bước

<!-- scene: S07 · source: note.md: heading '4. Consequence gồm cả khoản nợ được chấp nhận' -->

1. So CSV, JSONL và Parquet cho batch analytical exchange.
2. Hard gate: schema/type fidelity và reader compatibility. optimize scan cost sau gate.
3. Spike đo file size, scan latency, schema evolution và operability trên fixture thật.
4. Chọn Parquet, nhận debt inspection tooling. revisit nếu consumer không đọc được hoặc volume giảm dưới threshold.

---

## Evidence phải giữ lại

Reviewer tái tạo recommendation từ drivers/evidence và changed constraint làm recommendation đảo đúng rule.

Một output không có boundary, oracle hoặc limitation chỉ là kết quả chưa review.

---

## Failure modes

- **Critical:** Viết ADR sau khi đã chọn để hợp thức hóa, dùng strawman hoặc không ghi consequence/revisit signal.
- Chỉ kiểm happy path và sửa expected sau khi nhìn output.
- Gộp author claim, curriculum synthesis và learner conclusion thành một giọng.
- Dùng số lượng biểu đồ/test để thay thế oracle độc lập.

---

## Independent practice · không có đáp án mẫu

Viết ADR chọn scheduler cho ba workload. thiết kế spike phân biệt option và cập nhật ADR khi SLO đổi.

**Nộp:** artifact + evidence + limitation + reversal trigger.

---

<!-- scene: S08 · source: UNSOURCED curriculum transfer scenario -->
## Transfer challenge

Option rẻ nhất vi phạm RPO nhưng có tổng điểm cao nhất. Giải thích vì sao scoring sai và sửa decision rule.

Được phép có nhiều lựa chọn. Điểm nằm ở boundary, trade-off, evidence và blast radius: không nằm ở việc đoán ý người dạy.

---

<!-- scene: S09 · source: note.md: heading '6. Revisit signal phải kiểm được' -->
## Exit ticket · 3 phút

**Tại sao phương án bị loại vẫn là tài sản?**

<details><summary>Đáp án tối thiểu</summary>

Nó lưu constraint/evidence đã xét, tránh lặp tranh luận và cho biết khi nào option có thể hợp lệ trở lại.
</details>

---

## Sau buổi học

1. Làm `quiz.md`. đạt **8/10**.
2. Nếu trượt một concept, đọc remediation trong `after-note.md` rồi retest đúng concept đó.
3. Hoàn thành `homework.md`. đạt **≥ 75/100** và không có critical failure.

**Bắc cầu:** DE-L004: hiểu Git object graph để reasoning về thay đổi và phục hồi.
