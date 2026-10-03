---
loai: formative-quiz
lesson: 2
lesson_id: DE-L002
tieu_de: "Decomposition: responsibility, interface, state and failure domain"
so_cau: 10
thoi_gian_phut: 18
trang_thai: ready-for-owner-review
nguong_dat: 8
---

# Quiz — DE Lesson 2: Decomposition: responsibility, interface, state and failure domain

**Mục đích:** kiểm mental model và khả năng áp dụng, không dùng điểm danh làm bằng chứng.  
**Đạt:** ≥ 8/10. Câu 7-10 là critical transfer set; sai câu nào phải remediation và retest câu tương đương.

### Câu 1

Responsibility nên được tìm bằng gì?

- [ ] A. Operation, input/output semantics, error contract và invariant caller được dựa vào.
- [ ] B. Trace fault qua dependency/state tới consumer harm và recovery.
- [ ] C. Ownership/abstraction chưa rõ và thay đổi có thể lan hai chiều.
- [ ] D. Invariant và lý do thay đổi nghiệp vụ/vận hành, không chỉ technical layer.

<details><summary>Đáp án và phản hồi</summary>

**D. Invariant và lý do thay đổi nghiệp vụ/vận hành, không chỉ technical layer.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 2

Interface tối thiểu phải nêu gì?

- [ ] A. Caller vẫn phải biết chi tiết mà boundary tuyên bố đã che.
- [ ] B. Liệt kê invariants và các thay đổi độc lập, rồi hỏi phần nào phải đổi cùng nhau.
- [ ] C. Operation, input/output semantics, error contract và invariant caller được dựa vào.
- [ ] D. Ngăn nhiều component cập nhật cùng state machine mà không có protocol.

<details><summary>Đáp án và phản hồi</summary>

**C. Operation, input/output semantics, error contract và invariant caller được dựa vào.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 3

Authoritative writer có tác dụng gì?

- [ ] A. Context/component diagram, interface contract, state ownership table, dependency DAG và ba fault traces.
- [ ] B. Ngăn nhiều component cập nhật cùng state machine mà không có protocol.
- [ ] C. Trace fault qua dependency/state tới consumer harm và recovery.
- [ ] D. Ownership/abstraction chưa rõ và thay đổi có thể lan hai chiều.

<details><summary>Đáp án và phản hồi</summary>

**B. Ngăn nhiều component cập nhật cùng state machine mà không có protocol.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 4

Failure domain được xác định thế nào?

- [ ] A. Trace fault qua dependency/state tới consumer harm và recovery.
- [ ] B. Caller vẫn phải biết chi tiết mà boundary tuyên bố đã che.
- [ ] C. Liệt kê invariants và các thay đổi độc lập, rồi hỏi phần nào phải đổi cùng nhau.
- [ ] D. Đổi database không được buộc domain import driver type; nếu có, dependency direction đang sai.

<details><summary>Đáp án và phản hồi</summary>

**A. Trace fault qua dependency/state tới consumer harm và recovery.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 5

Abstraction leak là gì?

- [ ] A. Ownership/abstraction chưa rõ và thay đổi có thể lan hai chiều.
- [ ] B. Context/component diagram, interface contract, state ownership table, dependency DAG và ba fault traces.
- [ ] C. Chia theo folder/service aesthetic, để nhiều writer cho cùng state hoặc public interface lộ storage detail.
- [ ] D. Caller vẫn phải biết chi tiết mà boundary tuyên bố đã che.

<details><summary>Đáp án và phản hồi</summary>

**D. Caller vẫn phải biết chi tiết mà boundary tuyên bố đã che.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 6

Dependency cycle báo hiệu gì?

- [ ] A. Đổi database không được buộc domain import driver type; nếu có, dependency direction đang sai.
- [ ] B. Invariant và lý do thay đổi nghiệp vụ/vận hành, không chỉ technical layer.
- [ ] C. Ownership/abstraction chưa rõ và thay đổi có thể lan hai chiều.
- [ ] D. Liệt kê invariants và các thay đổi độc lập, rồi hỏi phần nào phải đổi cùng nhau.

<details><summary>Đáp án và phản hồi</summary>

**C. Ownership/abstraction chưa rõ và thay đổi có thể lan hai chiều.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 7

Trong tình huống mở bài, hành động đầu tiên tốt nhất là gì?

- [ ] A. Operation, input/output semantics, error contract và invariant caller được dựa vào.
- [ ] B. Liệt kê invariants và các thay đổi độc lập, rồi hỏi phần nào phải đổi cùng nhau.
- [ ] C. Context/component diagram, interface contract, state ownership table, dependency DAG và ba fault traces.
- [ ] D. Chia theo folder/service aesthetic, để nhiều writer cho cùng state hoặc public interface lộ storage detail.

<details><summary>Đáp án và phản hồi</summary>

**B. Liệt kê invariants và các thay đổi độc lập, rồi hỏi phần nào phải đổi cùng nhau.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 8

Bằng chứng nào trực tiếp nhất để xác nhận năng lực của bài này?

- [ ] A. Context/component diagram, interface contract, state ownership table, dependency DAG và ba fault traces.
- [ ] B. Đổi database không được buộc domain import driver type; nếu có, dependency direction đang sai.
- [ ] C. Invariant và lý do thay đổi nghiệp vụ/vận hành, không chỉ technical layer.
- [ ] D. Ngăn nhiều component cập nhật cùng state machine mà không có protocol.

<details><summary>Đáp án và phản hồi</summary>

**A. Context/component diagram, interface contract, state ownership table, dependency DAG và ba fault traces.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 9

Khi constraint thay đổi, nguyên tắc xử lý đúng là gì?

- [ ] A. Chia theo folder/service aesthetic, để nhiều writer cho cùng state hoặc public interface lộ storage detail.
- [ ] B. Operation, input/output semantics, error contract và invariant caller được dựa vào.
- [ ] C. Trace fault qua dependency/state tới consumer harm và recovery.
- [ ] D. Đổi database không được buộc domain import driver type; nếu có, dependency direction đang sai.

<details><summary>Đáp án và phản hồi</summary>

**D. Đổi database không được buộc domain import driver type; nếu có, dependency direction đang sai.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 10

Phát biểu nào mô tả critical failure của bài?

- [ ] A. Ngăn nhiều component cập nhật cùng state machine mà không có protocol.
- [ ] B. Caller vẫn phải biết chi tiết mà boundary tuyên bố đã che.
- [ ] C. Chia theo folder/service aesthetic, để nhiều writer cho cùng state hoặc public interface lộ storage detail.
- [ ] D. Invariant và lý do thay đổi nghiệp vụ/vận hành, không chỉ technical layer.

<details><summary>Đáp án và phản hồi</summary>

**C. Chia theo folder/service aesthetic, để nhiều writer cho cùng state hoặc public interface lộ storage detail.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>
