---
loai: formative-quiz
lesson: 2
lesson_id: DA-L002
tieu_de: "Where data comes from and the stages it passes through"
so_cau: 10
thoi_gian_phut: 18
trang_thai: ready-for-owner-review
nguong_dat: 8
---

# Quiz — DA Lesson 2: Where data comes from and the stages it passes through

**Mục đích:** kiểm mental model và khả năng áp dụng, không dùng điểm danh làm bằng chứng.  
**Đạt:** ≥ 8/10. Câu 7-10 là critical transfer set; sai câu nào phải remediation và retest câu tương đương.

### Câu 1

Ba lớp nào dễ bị đánh đồng?

- [ ] A. Boundary gần nguồn nhất còn giữ được bằng chứng độc lập.
- [ ] B. Oracle hoặc tổng kiểm không dùng cùng logic biến đổi đang được kiểm.
- [ ] C. Nó che cơ chế upstream và khiến consumer khác tiếp tục dùng dữ liệu sai.
- [ ] D. Sự kiện nghiệp vụ, bản ghi nguồn và bảng phục vụ phân tích.

<details><summary>Đáp án và phản hồi</summary>

**D. Sự kiện nghiệp vụ, bản ghi nguồn và bảng phục vụ phân tích.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 2

Khi hai nguồn lệch, nên bắt đầu ở đâu?

- [ ] A. Presentation/serving, sau khi metric có thể đã đúng ở mart.
- [ ] B. Viết event nghiệp vụ, population, grain và cutoff mà con số tuyên bố đại diện.
- [ ] C. Boundary gần nguồn nhất còn giữ được bằng chứng độc lập.
- [ ] D. Event time là lúc nghiệp vụ xảy ra; processing time là lúc hệ thống xử lý bản ghi.

<details><summary>Đáp án và phản hồi</summary>

**C. Boundary gần nguồn nhất còn giữ được bằng chứng độc lập.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 3

Event time khác processing time thế nào?

- [ ] A. Bảng lineage bảy chặng với input, output, owner, failure mode và reconciliation check cho cùng một giao dịch.
- [ ] B. Event time là lúc nghiệp vụ xảy ra; processing time là lúc hệ thống xử lý bản ghi.
- [ ] C. Oracle hoặc tổng kiểm không dùng cùng logic biến đổi đang được kiểm.
- [ ] D. Nó che cơ chế upstream và khiến consumer khác tiếp tục dùng dữ liệu sai.

<details><summary>Đáp án và phản hồi</summary>

**B. Event time là lúc nghiệp vụ xảy ra; processing time là lúc hệ thống xử lý bản ghi.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 4

Một phép reconciliation tốt cần gì?

- [ ] A. Oracle hoặc tổng kiểm không dùng cùng logic biến đổi đang được kiểm.
- [ ] B. Presentation/serving, sau khi metric có thể đã đúng ở mart.
- [ ] C. Viết event nghiệp vụ, population, grain và cutoff mà con số tuyên bố đại diện.
- [ ] D. Khi dữ liệu đến muộn, phải tách event time, processing time và cutoff; con số hôm nay có thể đúng theo snapshot nhưng chưa final.

<details><summary>Đáp án và phản hồi</summary>

**A. Oracle hoặc tổng kiểm không dùng cùng logic biến đổi đang được kiểm.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 5

Stale dashboard cache thuộc chặng nào?

- [ ] A. Nó che cơ chế upstream và khiến consumer khác tiếp tục dùng dữ liệu sai.
- [ ] B. Bảng lineage bảy chặng với input, output, owner, failure mode và reconciliation check cho cùng một giao dịch.
- [ ] C. Dùng tên bảng như bằng chứng về nghĩa dữ liệu, hoặc sửa dashboard cho khớp một tổng không độc lập.
- [ ] D. Presentation/serving, sau khi metric có thể đã đúng ở mart.

<details><summary>Đáp án và phản hồi</summary>

**D. Presentation/serving, sau khi metric có thể đã đúng ở mart.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 6

Vì sao không vá công thức cuối?

- [ ] A. Khi dữ liệu đến muộn, phải tách event time, processing time và cutoff; con số hôm nay có thể đúng theo snapshot nhưng chưa final.
- [ ] B. Sự kiện nghiệp vụ, bản ghi nguồn và bảng phục vụ phân tích.
- [ ] C. Nó che cơ chế upstream và khiến consumer khác tiếp tục dùng dữ liệu sai.
- [ ] D. Viết event nghiệp vụ, population, grain và cutoff mà con số tuyên bố đại diện.

<details><summary>Đáp án và phản hồi</summary>

**C. Nó che cơ chế upstream và khiến consumer khác tiếp tục dùng dữ liệu sai.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 7

Trong tình huống mở bài, hành động đầu tiên tốt nhất là gì?

- [ ] A. Boundary gần nguồn nhất còn giữ được bằng chứng độc lập.
- [ ] B. Viết event nghiệp vụ, population, grain và cutoff mà con số tuyên bố đại diện.
- [ ] C. Bảng lineage bảy chặng với input, output, owner, failure mode và reconciliation check cho cùng một giao dịch.
- [ ] D. Dùng tên bảng như bằng chứng về nghĩa dữ liệu, hoặc sửa dashboard cho khớp một tổng không độc lập.

<details><summary>Đáp án và phản hồi</summary>

**B. Viết event nghiệp vụ, population, grain và cutoff mà con số tuyên bố đại diện.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 8

Bằng chứng nào trực tiếp nhất để xác nhận năng lực của bài này?

- [ ] A. Bảng lineage bảy chặng với input, output, owner, failure mode và reconciliation check cho cùng một giao dịch.
- [ ] B. Khi dữ liệu đến muộn, phải tách event time, processing time và cutoff; con số hôm nay có thể đúng theo snapshot nhưng chưa final.
- [ ] C. Sự kiện nghiệp vụ, bản ghi nguồn và bảng phục vụ phân tích.
- [ ] D. Event time là lúc nghiệp vụ xảy ra; processing time là lúc hệ thống xử lý bản ghi.

<details><summary>Đáp án và phản hồi</summary>

**A. Bảng lineage bảy chặng với input, output, owner, failure mode và reconciliation check cho cùng một giao dịch.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 9

Khi constraint thay đổi, nguyên tắc xử lý đúng là gì?

- [ ] A. Dùng tên bảng như bằng chứng về nghĩa dữ liệu, hoặc sửa dashboard cho khớp một tổng không độc lập.
- [ ] B. Boundary gần nguồn nhất còn giữ được bằng chứng độc lập.
- [ ] C. Oracle hoặc tổng kiểm không dùng cùng logic biến đổi đang được kiểm.
- [ ] D. Khi dữ liệu đến muộn, phải tách event time, processing time và cutoff; con số hôm nay có thể đúng theo snapshot nhưng chưa final.

<details><summary>Đáp án và phản hồi</summary>

**D. Khi dữ liệu đến muộn, phải tách event time, processing time và cutoff; con số hôm nay có thể đúng theo snapshot nhưng chưa final.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 10

Phát biểu nào mô tả critical failure của bài?

- [ ] A. Event time là lúc nghiệp vụ xảy ra; processing time là lúc hệ thống xử lý bản ghi.
- [ ] B. Presentation/serving, sau khi metric có thể đã đúng ở mart.
- [ ] C. Dùng tên bảng như bằng chứng về nghĩa dữ liệu, hoặc sửa dashboard cho khớp một tổng không độc lập.
- [ ] D. Sự kiện nghiệp vụ, bản ghi nguồn và bảng phục vụ phân tích.

<details><summary>Đáp án và phản hồi</summary>

**C. Dùng tên bảng như bằng chứng về nghĩa dữ liệu, hoặc sửa dashboard cho khớp một tổng không độc lập.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>
