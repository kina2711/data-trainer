---
loai: diagnostic-quiz
lesson_id: DE-L001
so_cau: 10
nguong_dat: 8
trang_thai: ready-for-owner-review
---

# Quiz: DE-L001

Chọn đáp án tốt nhất và đọc phần chẩn đoán. Mục tiêu là phát hiện mental model sai trước khi viết code.

### Câu 1

Vì sao pipeline không được trùng order chưa test được?

A. Chưa chọn ngôn ngữ lập trình<br>
B. Chưa khóa identity, state, boundary, time và phép đếm<br>
C. Chưa có dashboard<br>
D. Duplicate luôn được định nghĩa giống nhau

<details><summary>Đáp án và phản hồi</summary>

**Đáp án: B.** Không có semantics thì nhiều expected output đều có thể hợp lý.

</details>

### Câu 2

Hai source cùng có order_id O-42. Identity hợp lý nhất theo contract bài học là:

A. order_id<br>
B. hash toàn payload<br>
C. source_system cộng order_id<br>
D. ingested_at

<details><summary>Đáp án và phản hồi</summary>

**Đáp án: C.** A collision giữa nguồn; B đổi khi payload cập nhật; D là thời gian xử lý.

</details>

### Câu 3

Client timeout sau khi gửi request. Kết luận an toàn nhất là:

A. Server chắc chắn chưa nhận<br>
B. Server chắc chắn đã fail<br>
C. Outcome chưa biết, cần status lookup hoặc retry có idempotency semantics<br>
D. Gửi request mới với key mới

<details><summary>Đáp án và phản hồi</summary>

**Đáp án: C.** Timeout là trạng thái quan sát của client, không phải bằng chứng commit state.

</details>

### Câu 4

Cùng idempotency key nhưng payload khác nên xử lý thế nào?

A. Chấp nhận payload mới<br>
B. Im lặng bỏ qua<br>
C. Reject conflict và giữ trace<br>
D. Tạo hai operation

<details><summary>Đáp án và phản hồi</summary>

**Đáp án: C.** Cùng key phải đại diện cùng ý định logic; payload khác là vi phạm contract.

</details>

### Câu 5

Given/When/Then nào tốt nhất?

A. Given Kafka, When MERGE, Then success<br>
B. Given order fixture và current state, When request cụ thể, Then outcome quan sát được<br>
C. Given nhanh, When ổn định, Then không lỗi<br>
D. Given code chạy, When test chạy, Then pass

<details><summary>Đáp án và phản hồi</summary>

**Đáp án: B.** Scenario mô tả behavior; A khóa implementation mà chưa nêu outcome.

</details>

### Câu 6

Job chạy xanh nhưng 3% order hợp lệ chưa vào curated sau 10 phút. Nhận định nào đúng?

A. Availability signal có thể xanh nhưng freshness SLO trượt<br>
B. Job xanh chứng minh mọi SLO đạt<br>
C. Đây chỉ là lỗi dashboard<br>
D. Correctness và freshness luôn giống nhau

<details><summary>Đáp án và phản hồi</summary>

**Đáp án: A.** Tín hiệu tiến trình, correctness và freshness là các trục khác nhau.

</details>

### Câu 7

Version paid lúc 11:55 đến trước version accepted lúc 11:50. Current state nên là gì theo contract?

A. Accepted vì đến sau<br>
B. Paid vì source_updated_at mới hơn<br>
C. Hai current rows<br>
D. Xóa cả hai

<details><summary>Đáp án và phản hồi</summary>

**Đáp án: B.** Ingestion order không được thay thế source ordering nếu contract dùng source_updated_at.

</details>

### Câu 8

Uniqueness query trả zero rows. Điều gì vẫn chưa được chứng minh?

A. Query chạy được<br>
B. Không có duplicate trong row đã quan sát<br>
C. End-to-end completeness so với population nguồn<br>
D. Schema có cột identity

<details><summary>Đáp án và phản hồi</summary>

**Đáp án: C.** Nếu record bị mất trước curated, uniqueness vẫn có thể hoàn hảo.

</details>

### Câu 9

Source chỉ cho poll mỗi 2 phút nhưng SLO đổi xuống 30 giây. Phản ứng tốt nhất là:

A. Hứa rồi tối ưu code<br>
B. Bỏ source constraint khỏi contract<br>
C. Nêu hard constraint và chọn renegotiate SLO, đổi integration hoặc architecture<br>
D. Đổi dashboard sang màu đỏ

<details><summary>Đáp án và phản hồi</summary>

**Đáp án: C.** Đây là change control, không phải tuning thông thường.

</details>

### Câu 10

Contract khác implementation plan ở đâu?

A. Contract chọn framework; plan chọn requirement<br>
B. Contract khóa behavior và evidence; plan chọn cơ chế thực hiện<br>
C. Hai thứ giống nhau<br>
D. Contract thay thế test và runbook

<details><summary>Đáp án và phản hồi</summary>

**Đáp án: B.** Contract không thay thiết kế, test, telemetry hay vận hành.

</details>

## Chẩn đoán và remediation

| Câu sai | Lỗ hổng | Quay lại |
|---|---|---|
| 1, 2, 7 | identity, time, state | S02, S03 |
| 3, 4 | timeout và idempotency | S05 |
| 5 | behavioral specification | S04 |
| 6, 9 | SLO và change control | S06 |
| 8 | oracle và completeness | S07 |
| 10 | contract boundary | S08, S09 |

Retest phải dùng fixture mới và expected result được ghi trước khi chạy.

## References

- [[wiki.engineering-foundation.testable-contract|From a vague request to a testable contract]]
- [[wiki.data-product.requirements-traceability|Requirements traceability]]
- [[wiki.data-quality.sli-slo-design|Data SLI and SLO design]]
