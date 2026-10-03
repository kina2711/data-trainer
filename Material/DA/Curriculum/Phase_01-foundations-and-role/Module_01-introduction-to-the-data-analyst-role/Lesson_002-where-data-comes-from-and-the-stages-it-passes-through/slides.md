---
marp: true
theme: volt
paginate: true
size: 16:9
header: 'DA · Lesson 2'
footer: 'Foundation · runnable scene package'
---

<!-- _class: lead -->

# Where data comes from and the stages it passes through

**DA-L002 · 120 phút (ước tính)**

> Một con số đã bị biến đổi ở đâu từ sự kiện nghiệp vụ đến quyết định?

---

## Chuẩn đầu ra

Tái dựng vòng đời bảy chặng và định vị cơ chế sai lệch cùng bằng chứng kiểm tra tại từng boundary.

**Evidence:** Bảng lineage bảy chặng với input, output, owner, failure mode và reconciliation check cho cùng một giao dịch.

**Không suy ra mastery từ việc có mặt hoặc xem hết slide.**

---

<!-- scene: S01 · source: note.md: heading 'Nỗi Đau & Động Lực' -->
## Tình huống mở

Dashboard báo khách hoạt động giảm, nhưng source ghi đơn tạo, vận hành đếm đơn thanh toán còn CRM đếm phiên truy cập. Ba số đúng theo code nhưng không cùng khái niệm.

**Think–pair–share · 4 phút**

1. Bạn sẽ làm gì đầu tiên?
2. Quyết định nào có thể bị ảnh hưởng?
3. Bằng chứng nào đang thiếu?

---

<!-- scene: S02 · source: note.md: heading 'Cơ Chế Tác Động' -->
## Mental model trung tâm

> Con số phân tích là một chuỗi biến đổi có lineage. muốn tin kết luận phải nối event, record, storage, transform, metric, presentation và decision bằng các phép đối soát.

- Tách sự kiện thật khỏi bản ghi nguồn và bảng phân tích.
- Khóa population, grain, event time/cutoff và định nghĩa metric ở mỗi boundary.
- Đối soát gần nguồn nhất còn giữ bằng chứng thay vì vá công thức cuối.

---

## Luồng kiểm soát

| 1. Câu hỏi hoặc thay đổi | 2. Boundary | 3. Evidence | 4. Decision gate | 5. Theo dõi |
|---|---|---|---|---|
| Nêu outcome cần quyết định | Khóa scope và semantics | Dùng phép kiểm độc lập | Áp dụng có giới hạn hoặc dừng | Quan sát reversal trigger |

---

## Bước đầu tiên có tính quyết định

**Viết event nghiệp vụ, population, grain và cutoff mà con số tuyên bố đại diện.**

Không làm bước này, output sau đó có thể đúng cú pháp nhưng sai đối tượng, sai thời gian hoặc sai quyết định.

---

<!-- scene: S03 · source: note.md: heading 'Cơ Chế Tác Động' -->
## Check 1 · trả lời không nhìn tài liệu

**Ba lớp nào dễ bị đánh đồng?**

<details>
<summary>Đáp án và tín hiệu chẩn đoán</summary>

Sự kiện nghiệp vụ, bản ghi nguồn và bảng phục vụ phân tích.

Nếu câu trả lời chỉ nêu tên công cụ, hãy quay lại mental model và nói rõ boundary + evidence + action.
</details>

---

<!-- scene: S04 · source: UNSOURCED guided practice synthesis -->
## Guided practice · 12 phút làm + 6 phút chữa

Xếp 14 thẻ artifact vào bảy chặng và nối mỗi chặng với một failure mode: missing event, duplicate, timezone, filter, join fan-out, stale cache, wrong action.

**Definition of done:** Đúng ≥ 12/14 thẻ và nêu được một phép kiểm độc lập tại ít nhất năm boundary.

Người dạy không chữa bằng đáp án ngay. yêu cầu mỗi nhóm nêu assumption và phép kiểm trước.

---

<!-- scene: S05 · source: note.md: heading 'Bản Đồ Quyết Định' -->
## Quy tắc quyết định

Khi hai số lệch, đi ngược lineage và kiểm boundary đầu tiên chúng bắt đầu khác. chỉ sửa downstream sau khi cơ chế upstream đã được xác nhận.

**Boundary:** Lineage mô tả đường đi và biến đổi. nó không tự chứng minh completeness nếu không có count, checksum hoặc oracle độc lập.

---

## Changed constraint

<!-- scene: S06 · source: UNSOURCED changed-constraint synthesis -->

Khi dữ liệu đến muộn, phải tách event time, processing time và cutoff. con số hôm nay có thể đúng theo snapshot nhưng chưa final.

**Thảo luận:** lựa chọn nào còn defensible? Bằng chứng nào làm bạn đảo quyết định?

---

## Worked example · đi từng bước

<!-- scene: S07 · source: note.md: heading 'Case Study Thực Chiến: một chỉ số bán hàng đổi nghĩa giữa đường' -->

1. Đặt ba định nghĩa 'active customer' cạnh nhau trên cùng snapshot.
2. Theo một khách từ click, order_created, payment_success tới mart và dashboard.
3. So count và distinct identity sau mỗi join/filter để tìm chặng làm mất tín hiệu.
4. Đổi câu hỏi từ 'khách giảm' thành 'conversion tạo đơn sang thanh toán giảm ở thiết bị nào'.

---

## Evidence phải giữ lại

Bảng lineage bảy chặng với input, output, owner, failure mode và reconciliation check cho cùng một giao dịch.

Một output không có boundary, oracle hoặc limitation chỉ là kết quả chưa review.

---

## Failure modes

- **Critical:** Dùng tên bảng như bằng chứng về nghĩa dữ liệu, hoặc sửa dashboard cho khớp một tổng không độc lập.
- Chỉ kiểm happy path và sửa expected sau khi nhìn output.
- Gộp author claim, curriculum synthesis và learner conclusion thành một giọng.
- Dùng số lượng biểu đồ/test để thay thế oracle độc lập.

---

## Independent practice · không có đáp án mẫu

Lập trace table cho một giao dịch từ checkout tới weekly revenue dashboard. ghi row count, distinct key, timestamp và owner ở mỗi chặng.

**Nộp:** artifact + evidence + limitation + reversal trigger.

---

<!-- scene: S08 · source: UNSOURCED curriculum transfer scenario -->
## Transfer challenge

Dashboard retention giảm đúng ngày đổi SDK. Thiết kế thứ tự kiểm chứng để phân biệt hành vi thật, mất event và đổi identity.

Được phép có nhiều lựa chọn. Điểm nằm ở boundary, trade-off, evidence và blast radius: không nằm ở việc đoán ý người dạy.

---

<!-- scene: S09 · source: note.md: heading 'Góc Khuất & Ngộ Nhận' -->
## Exit ticket · 3 phút

**Vì sao lineage không đồng nghĩa dữ liệu đúng?**

<details><summary>Đáp án tối thiểu</summary>

Lineage chỉ nói đường đi. correctness cần invariant và reconciliation độc lập tại boundary.
</details>

---

## Sau buổi học

1. Làm `quiz.md`. đạt **8/10**.
2. Nếu trượt một concept, đọc remediation trong `after-note.md` rồi retest đúng concept đó.
3. Hoàn thành `homework.md`. đạt **≥ 75/100** và không có critical failure.

**Bắc cầu:** L003: khóa entity, record và grain trước khi đếm hoặc join.
