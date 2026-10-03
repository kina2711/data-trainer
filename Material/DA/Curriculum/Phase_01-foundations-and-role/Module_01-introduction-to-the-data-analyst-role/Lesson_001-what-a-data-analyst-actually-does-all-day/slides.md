---
marp: true
theme: volt
paginate: true
size: 16:9
header: 'DA · Lesson 1'
footer: 'Foundation · runnable scene package'
---

<!-- _class: lead -->

# What a Data Analyst actually does all day

**DA-L001 · 120 phút (ước tính)**

> Data Analyst tạo giá trị ở đâu trong vòng đời từ yêu cầu đến quyết định?

---

## Chuẩn đầu ra

Phân loại nhiệm vụ theo sáu vai trò dữ liệu và bảo vệ ranh giới trách nhiệm bằng outcome, artifact và consumer.

**Evidence:** Bảng phân vai 15 nhiệm vụ kèm lý do dựa trên outcome và artifact, không dựa trên tên công cụ.

**Không suy ra mastery từ việc có mặt hoặc xem hết slide.**

---

<!-- scene: S01 · source: note.md: heading 'II. Bối cảnh và vấn đề đặt ra' -->
## Tình huống mở

Giám đốc nói doanh thu tháng 10 giảm 12% và hỏi vì sao. Một dashboard đẹp có thể vẫn hoàn toàn vô dụng nếu mốc so sánh, dữ liệu thiếu và quyết định cần hỗ trợ chưa rõ.

**Think–pair–share · 4 phút**

1. Bạn sẽ làm gì đầu tiên?
2. Quyết định nào có thể bị ảnh hưởng?
3. Bằng chứng nào đang thiếu?

---

<!-- scene: S02 · source: note.md: heading 'III. Cơ sở lý thuyết và cơ chế vận hành' -->
## Mental model trung tâm

> DA không được định nghĩa bởi công cụ. DA biến một câu hỏi mơ hồ thành kết luận có kiểm chứng và hành động có chủ sở hữu.

- Làm rõ quyết định, population, mốc so sánh và deadline trước khi chạm dữ liệu.
- Kiểm chứng con số và định nghĩa trước khi giải thích biến động.
- Tách nhiệm vụ theo artifact: pipeline, semantic model, dashboard, phân tích, dự báo hay đặc tả quy trình.

---

## Luồng kiểm soát

| 1. Câu hỏi hoặc thay đổi | 2. Boundary | 3. Evidence | 4. Decision gate | 5. Theo dõi |
|---|---|---|---|---|
| Nêu outcome cần quyết định | Khóa scope và semantics | Dùng phép kiểm độc lập | Áp dụng có giới hạn hoặc dừng | Quan sát reversal trigger |

---

## Bước đầu tiên có tính quyết định

**Hỏi người nhận sẽ dùng câu trả lời để quyết định điều gì và 12% được so với mốc nào.**

Không làm bước này, output sau đó có thể đúng cú pháp nhưng sai đối tượng, sai thời gian hoặc sai quyết định.

---

<!-- scene: S03 · source: note.md: heading 'III. Cơ sở lý thuyết và cơ chế vận hành' -->
## Check 1 · trả lời không nhìn tài liệu

**Phần giá trị cao nhất của DA là gì?**

<details>
<summary>Đáp án và tín hiệu chẩn đoán</summary>

Biến câu hỏi thành kết luận kiểm chứng được và hành động cụ thể.

Nếu câu trả lời chỉ nêu tên công cụ, hãy quay lại mental model và nói rõ boundary + evidence + action.
</details>

---

<!-- scene: S04 · source: UNSOURCED guided practice synthesis -->
## Guided practice · 12 phút làm + 6 phút chữa

Phân loại tám thẻ việc: sửa pipeline mất dữ liệu, định nghĩa revenue, dashboard ngày, phân tích churn, dự báo churn, đặc tả hoàn tiền, đối soát hai báo cáo, trình bày khuyến nghị.

**Definition of done:** Ít nhất 6/8 thẻ đúng và mỗi lý do gọi tên outcome hoặc artifact bàn giao.

Người dạy không chữa bằng đáp án ngay. yêu cầu mỗi nhóm nêu assumption và phép kiểm trước.

---

<!-- scene: S05 · source: note.md: heading 'IV. Khung quyết định và tiêu chí lựa chọn' -->
## Quy tắc quyết định

Nếu yêu cầu hỏi chuyện gì xảy ra, vì sao và nên làm gì thì DA sở hữu phân tích. nếu lỗi nằm ở ingestion, định nghĩa dùng chung, theo dõi định kỳ, dự báo hoặc quy trình thì phải có vai tương ứng đồng sở hữu.

**Boundary:** Ở công ty nhỏ một người có thể đội nhiều mũ. vẫn phải gọi đúng vai đang thực hiện để biết invariant và bàn giao nào thuộc trách nhiệm đó.

---

## Changed constraint

<!-- scene: S06 · source: UNSOURCED changed-constraint synthesis -->

Nếu công ty chỉ có một người dữ liệu, phạm vi thực thi rộng lên nhưng tiêu chí bàn giao của từng vai không biến mất.

**Thảo luận:** lựa chọn nào còn defensible? Bằng chứng nào làm bạn đảo quyết định?

---

## Worked example · đi từng bước

<!-- scene: S07 · source: note.md: heading 'V. Nghiên cứu tình huống: quay lại câu "doanh thu giảm 12%"' -->

1. Chuẩn hóa doanh thu theo số ngày và phát hiện chi nhánh Đà Nẵng thiếu 11 ngày dữ liệu.
2. Tách mức giảm báo cáo 12% khỏi mức giảm thật 4% sau kiểm chứng.
3. Xác định phần giảm tập trung ở khách mới, không phải khách cũ.
4. Khuyến nghị ngân sách có mục tiêu và mở incident dữ liệu riêng cho chi nhánh.

---

## Evidence phải giữ lại

Bảng phân vai 15 nhiệm vụ kèm lý do dựa trên outcome và artifact, không dựa trên tên công cụ.

Một output không có boundary, oracle hoặc limitation chỉ là kết quả chưa review.

---

## Failure modes

- **Critical:** Gán vai theo công cụ, hoặc gửi output không nói quyết định nào sẽ thay đổi.
- Chỉ kiểm happy path và sửa expected sau khi nhìn output.
- Gộp author claim, curriculum synthesis và learner conclusion thành một giọng.
- Dùng số lượng biểu đồ/test để thay thế oracle độc lập.

---

## Independent practice · không có đáp án mẫu

Phân loại 15 nhiệm vụ của một đội thương mại điện tử. đánh dấu ba vùng cần đồng sở hữu và viết RACI tối thiểu.

**Nộp:** artifact + evidence + limitation + reversal trigger.

---

<!-- scene: S08 · source: UNSOURCED curriculum transfer scenario -->
## Transfer challenge

Một startup 20 người tuyển 'Data Analyst' nhưng JD gồm Airflow, dbt, Power BI và churn model. Hãy tách bốn vai, rủi ro và thứ tự tuyển/bàn giao.

Được phép có nhiều lựa chọn. Điểm nằm ở boundary, trade-off, evidence và blast radius: không nằm ở việc đoán ý người dạy.

---

<!-- scene: S09 · source: note.md: heading 'VI. Giới hạn và ngộ nhận phổ biến' -->
## Exit ticket · 3 phút

**Data Analyst khác Data Engineer ở đâu, và vì sao ranh giới vẫn có thể chồng lấn?**

<details><summary>Đáp án tối thiểu</summary>

DA sở hữu câu trả lời và khuyến nghị. DE sở hữu dòng dữ liệu tin cậy. Chồng lấn xuất hiện ở kiểm chứng và lỗi dữ liệu, nên cần phân biệt lỗi hệ thống với logic nghiệp vụ.
</details>

---

## Sau buổi học

1. Làm `quiz.md`. đạt **8/10**.
2. Nếu trượt một concept, đọc remediation trong `after-note.md` rồi retest đúng concept đó.
3. Hoàn thành `homework.md`. đạt **≥ 75/100** và không có critical failure.

**Bắc cầu:** L002: theo dấu một con số qua vòng đời dữ liệu.
