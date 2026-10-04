---
loai: diagnostic-quiz
lesson_id: DA-L001
so_cau: 10
nguong_dat: 8
trang_thai: ready-for-owner-review
---

# Quiz: DA-L001

Chọn đáp án tốt nhất. Mỗi câu kiểm một failure mode khác nhau. Sau khi làm, đối chiếu không chỉ đáp án mà cả lý do.

### Câu 1

Stakeholder nói: Làm dashboard doanh thu giúp tôi. Câu hỏi đầu tiên tốt nhất là gì?

A. Anh/chị thích màu nào?<br>
B. Anh/chị sẽ thay đổi quyết định gì nếu kết quả cao, thấp hoặc chưa chắc chắn?<br>
C. Dùng Power BI hay Tableau?<br>
D. Cần bao nhiêu biểu đồ?

<details><summary>Đáp án và phản hồi</summary>

**Đáp án: B.** Output chỉ có nghĩa khi nối với consumer và decision. Chọn C cho thấy đang khóa công cụ trước vấn đề.

</details>

### Câu 2

Dashboard báo revenue giảm 12%, nhưng một chi nhánh thiếu 11 ngày dữ liệu. Claim mạnh nhất hiện có là gì?

A. Marketing làm revenue giảm 12%<br>
B. Revenue chắc chắn không giảm<br>
C. Dashboard quan sát giảm 12%, nhưng business change chưa đủ bằng chứng trước reconciliation<br>
D. Chi nhánh đó gây toàn bộ mức giảm

<details><summary>Đáp án và phản hồi</summary>

**Đáp án: C.** A và D vượt quá evidence; B cũng là khẳng định chưa kiểm chứng.

</details>

### Câu 3

Ai nên là owner chính khi pipeline không ingest file của một chi nhánh?

A. Data Engineer, với DA cung cấp evidence về ảnh hưởng tới phân tích<br>
B. Data Analyst vì người này phát hiện lỗi<br>
C. BI Developer vì lỗi xuất hiện trên dashboard<br>
D. Stakeholder vì họ xem báo cáo

<details><summary>Đáp án và phản hồi</summary>

**Đáp án: A.** Vai phát hiện không nhất thiết là vai sở hữu cơ chế hỏng.

</details>

### Câu 4

Sau reconciliation, revenue giảm 4%; khách mới giảm 140 triệu còn khách cũ tăng 20 triệu. Kết luận nào hợp lệ?

A. Campaign acquisition chắc chắn gây ra giảm<br>
B. Mức giảm tập trung ở khách mới; campaign là một giả thuyết cần kiểm thêm<br>
C. Khách cũ bù hoàn toàn mức giảm<br>
D. Không cần kiểm tracking vì tổng đã reconcile

<details><summary>Đáp án và phản hồi</summary>

**Đáp án: B.** Decomposition xác định nơi chênh lệch tập trung, không tự chứng minh nguyên nhân.

</details>

### Câu 5

Tại sao query coverage không tự chứng minh completeness?

A. SQL không dùng được cho data quality<br>
B. Query chỉ thấy record đã vào bảng và có thể cùng mất dữ liệu với hệ thống đang kiểm<br>
C. Coverage chỉ dành cho Data Engineer<br>
D. Completeness không thể đo

<details><summary>Đáp án và phản hồi</summary>

**Đáp án: B.** Cần oracle độc lập như settlement control total.

</details>

### Câu 6

Một startup có một người làm ingestion, model, dashboard và analysis. Phát biểu đúng nhất là:

A. Người đó chỉ có một vai vì chức danh chỉ có một<br>
B. Không cần phân ranh giới vì đội nhỏ<br>
C. Một người có thể đội nhiều mũ, nhưng invariant và artifact của từng mũ vẫn phải rõ<br>
D. Mọi lỗi đều thuộc Data Analyst

<details><summary>Đáp án và phản hồi</summary>

**Đáp án: C.** Phạm vi người làm thay đổi, trách nhiệm của từng loại artifact không biến mất.

</details>

### Câu 7

Decision memo nào có reversal trigger tốt nhất?

A. Theo dõi thêm khi cần.<br>
B. Nếu reconciliation lệch trên 0,5% hoặc coverage dưới 98%, dừng quyết định ngân sách.<br>
C. Nếu dashboard xấu, kiểm tra lại.<br>
D. Chúng tôi khá chắc chắn.

<details><summary>Đáp án và phản hồi</summary>

**Đáp án: B.** Trigger có observable condition và action.

</details>

### Câu 8

Vì sao Act nối ngược về Ask?

A. Vì phân tích luôn sai<br>
B. Vì hành động tạo kết quả và bằng chứng mới, có thể thay đổi câu hỏi hoặc giả thuyết<br>
C. Vì dashboard cần refresh<br>
D. Vì stakeholder luôn đổi ý

<details><summary>Đáp án và phản hồi</summary>

**Đáp án: B.** Vòng phản hồi là cơ chế học, không phải dấu hiệu thất bại.

</details>

### Câu 9

Trường hợp nào gần nhất với BI ownership?

A. Dự báo xác suất churn<br>
B. Vận hành dashboard chỉ số đã thống nhất, có refresh và trạng thái tương tác rõ<br>
C. Sửa retry semantics của API<br>
D. Đặc tả quy trình duyệt hoàn tiền

<details><summary>Đáp án và phản hồi</summary>

**Đáp án: B.** A gần DS, C gần DE, D gần BA.

</details>

### Câu 10

DA đã reconcile revenue giảm 4% và xác định phần giảm tập trung ở khách mới. Claim nào vượt quá bằng chứng?

A. Revenue trong boundary đã nêu giảm 4%<br>
B. Chênh lệch tập trung ở khách mới<br>
C. Marketing là nguyên nhân gây ra toàn bộ mức giảm<br>
D. Cần kiểm thêm campaign, stock và tracking

<details><summary>Đáp án và phản hồi</summary>

**Đáp án: C.** Decomposition chưa tạo causal evidence. Chọn C cho thấy người học đã nâng diagnostic claim thành causal claim.

</details>

## Chẩn đoán và remediation

| Câu sai | Lỗ hổng | Quay lại |
|---|---|---|
| 1, 8 | decision loop | S01, S02 |
| 2, 4, 5 | claim và evidence | S03, S07 |
| 3, 6, 9 | role boundary | S04, S05, S06 |
| 7 | decision memo | S08 |
| 10 | claim ladder | phần Claim ladder |

Retest dùng scenario mới, không đổi thứ tự đáp án rồi làm lại cùng câu.

## References

- [[wiki.da.operating-as-a-data-analyst|Operating as a Data Analyst]]
- [[wiki.data-product.decision-first-discovery|Decision-First Discovery]]
- [[wiki.da.revenue-and-commerce-analytics|Revenue and commerce analytics]]
