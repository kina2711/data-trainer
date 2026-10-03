---
loai: formative-quiz
lesson: 1
lesson_id: DE-L001
tieu_de: "From a vague request to a testable contract"
so_cau: 10
thoi_gian_phut: 18
trang_thai: ready-for-owner-review
nguong_dat: 8
---

# Quiz — DE Lesson 1: From a vague request to a testable contract

**Mục đích:** kiểm mental model và khả năng áp dụng, không dùng điểm danh làm bằng chứng.  
**Đạt:** ≥ 8/10. Câu 7-10 là critical transfer set; sai câu nào phải remediation và retest câu tương đương.

### Câu 1

Một expected output tốt phải có tính chất gì?

- [ ] A. Dedup và replay có thể xanh giả vì không biết hai record có cùng thực thể hay không.
- [ ] B. Boundary và change control khỏi mở rộng scope âm thầm.
- [ ] C. Khi input bắt buộc làm đổi semantics, risk hoặc acceptance chưa được giải quyết.
- [ ] D. Hai reviewer độc lập suy ra cùng kết quả từ cùng fixture.

<details><summary>Đáp án và phản hồi</summary>

**D. Hai reviewer độc lập suy ra cùng kết quả từ cùng fixture.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 2

Identity thiếu gây rủi ro gì?

- [ ] A. Dùng idempotency/reconciliation để xác định trạng thái trước retry mù.
- [ ] B. Hỏi consumer cần behavior nào và failure nào không được phép xảy ra.
- [ ] C. Dedup và replay có thể xanh giả vì không biết hai record có cùng thực thể hay không.
- [ ] D. Requirement tới test/artifact và failed evidence quay về đúng requirement/owner.

<details><summary>Đáp án và phản hồi</summary>

**C. Dedup và replay có thể xanh giả vì không biết hai record có cùng thực thể hay không.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 3

Traceability hai chiều là gì?

- [ ] A. Hai reviewer độc lập tạo cùng expected output từ fixture và trace mỗi failed check về requirement/owner.
- [ ] B. Requirement tới test/artifact và failed evidence quay về đúng requirement/owner.
- [ ] C. Boundary và change control khỏi mở rộng scope âm thầm.
- [ ] D. Khi input bắt buộc làm đổi semantics, risk hoặc acceptance chưa được giải quyết.

<details><summary>Đáp án và phản hồi</summary>

**B. Requirement tới test/artifact và failed evidence quay về đúng requirement/owner.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 4

Non-goal bảo vệ điều gì?

- [ ] A. Boundary và change control khỏi mở rộng scope âm thầm.
- [ ] B. Dùng idempotency/reconciliation để xác định trạng thái trước retry mù.
- [ ] C. Hỏi consumer cần behavior nào và failure nào không được phép xảy ra.
- [ ] D. Khi SLO từ 10 phút xuống 30 giây, contract buộc lộ thay đổi kiến trúc thay vì coi đây là tuning nhỏ.

<details><summary>Đáp án và phản hồi</summary>

**A. Boundary và change control khỏi mở rộng scope âm thầm.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 5

Outcome unknown cần xử lý thế nào?

- [ ] A. Khi input bắt buộc làm đổi semantics, risk hoặc acceptance chưa được giải quyết.
- [ ] B. Hai reviewer độc lập tạo cùng expected output từ fixture và trace mỗi failed check về requirement/owner.
- [ ] C. Viết acceptance bằng từ mơ hồ như nhanh/ổn định, hoặc để implementation tự quyết semantics.
- [ ] D. Dùng idempotency/reconciliation để xác định trạng thái trước retry mù.

<details><summary>Đáp án và phản hồi</summary>

**D. Dùng idempotency/reconciliation để xác định trạng thái trước retry mù.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 6

Definition of Ready chặn khi nào?

- [ ] A. Khi SLO từ 10 phút xuống 30 giây, contract buộc lộ thay đổi kiến trúc thay vì coi đây là tuning nhỏ.
- [ ] B. Hai reviewer độc lập suy ra cùng kết quả từ cùng fixture.
- [ ] C. Khi input bắt buộc làm đổi semantics, risk hoặc acceptance chưa được giải quyết.
- [ ] D. Hỏi consumer cần behavior nào và failure nào không được phép xảy ra.

<details><summary>Đáp án và phản hồi</summary>

**C. Khi input bắt buộc làm đổi semantics, risk hoặc acceptance chưa được giải quyết.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 7

Trong tình huống mở bài, hành động đầu tiên tốt nhất là gì?

- [ ] A. Dedup và replay có thể xanh giả vì không biết hai record có cùng thực thể hay không.
- [ ] B. Hỏi consumer cần behavior nào và failure nào không được phép xảy ra.
- [ ] C. Hai reviewer độc lập tạo cùng expected output từ fixture và trace mỗi failed check về requirement/owner.
- [ ] D. Viết acceptance bằng từ mơ hồ như nhanh/ổn định, hoặc để implementation tự quyết semantics.

<details><summary>Đáp án và phản hồi</summary>

**B. Hỏi consumer cần behavior nào và failure nào không được phép xảy ra.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 8

Bằng chứng nào trực tiếp nhất để xác nhận năng lực của bài này?

- [ ] A. Hai reviewer độc lập tạo cùng expected output từ fixture và trace mỗi failed check về requirement/owner.
- [ ] B. Khi SLO từ 10 phút xuống 30 giây, contract buộc lộ thay đổi kiến trúc thay vì coi đây là tuning nhỏ.
- [ ] C. Hai reviewer độc lập suy ra cùng kết quả từ cùng fixture.
- [ ] D. Requirement tới test/artifact và failed evidence quay về đúng requirement/owner.

<details><summary>Đáp án và phản hồi</summary>

**A. Hai reviewer độc lập tạo cùng expected output từ fixture và trace mỗi failed check về requirement/owner.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 9

Khi constraint thay đổi, nguyên tắc xử lý đúng là gì?

- [ ] A. Viết acceptance bằng từ mơ hồ như nhanh/ổn định, hoặc để implementation tự quyết semantics.
- [ ] B. Dedup và replay có thể xanh giả vì không biết hai record có cùng thực thể hay không.
- [ ] C. Boundary và change control khỏi mở rộng scope âm thầm.
- [ ] D. Khi SLO từ 10 phút xuống 30 giây, contract buộc lộ thay đổi kiến trúc thay vì coi đây là tuning nhỏ.

<details><summary>Đáp án và phản hồi</summary>

**D. Khi SLO từ 10 phút xuống 30 giây, contract buộc lộ thay đổi kiến trúc thay vì coi đây là tuning nhỏ.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 10

Phát biểu nào mô tả critical failure của bài?

- [ ] A. Requirement tới test/artifact và failed evidence quay về đúng requirement/owner.
- [ ] B. Dùng idempotency/reconciliation để xác định trạng thái trước retry mù.
- [ ] C. Viết acceptance bằng từ mơ hồ như nhanh/ổn định, hoặc để implementation tự quyết semantics.
- [ ] D. Hai reviewer độc lập suy ra cùng kết quả từ cùng fixture.

<details><summary>Đáp án và phản hồi</summary>

**C. Viết acceptance bằng từ mơ hồ như nhanh/ổn định, hoặc để implementation tự quyết semantics.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>
