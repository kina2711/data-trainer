---
loai: formative-quiz
lesson: 3
lesson_id: DA-L003
tieu_de: "Entities, attributes, records and grain"
so_cau: 10
trang_thai: ready-for-owner-review
nguong_dat: 8
---

# Quiz: DA Lesson 3: Entities, attributes, records and grain

**Mục đích:** kiểm mental model và khả năng áp dụng, không dùng điểm danh làm bằng chứng.
**Đạt:** ≥ 8/10. Câu 7-10 là critical transfer set; sai câu nào phải remediation và retest câu tương đương.

### Câu 1

Grain là gì?

- [ ] A. Row count hoặc multiplicity trên base key tăng sau join.
- [ ] B. Count so với count distinct cùng kiểm NULL và duplicate distribution.
- [ ] C. Khi population, identity, thời gian và status của customer đã được khóa.
- [ ] D. Lời cam kết một dòng đại diện cho đối tượng/sự kiện nào trong boundary đã nêu.

<details><summary>Đáp án và phản hồi</summary>

**D. Lời cam kết một dòng đại diện cho đối tượng/sự kiện nào trong boundary đã nêu.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi: lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 2

Dấu hiệu trực tiếp của fan-out là gì?

- [ ] A. Chỉ chứng minh định danh row, không tự chứng minh nghĩa nghiệp vụ của grain.
- [ ] B. Viết câu 'mỗi dòng đại diện cho…' và khóa ứng viên trước bất kỳ SUM hoặc JOIN nào.
- [ ] C. Row count hoặc multiplicity trên base key tăng sau join.
- [ ] D. Giữ ở bảng sở hữu hoặc aggregate phía many về cùng grain trước khi ghép.

<details><summary>Đáp án và phản hồi</summary>

**C. Row count hoặc multiplicity trên base key tăng sau join.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi: lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 3

Measure phía one nên xử lý thế nào trước one-to-many join?

- [ ] A. Bảng kiểm grain gồm candidate key, uniqueness, row count, distinct key, join multiplicity và reconciliation total.
- [ ] B. Giữ ở bảng sở hữu hoặc aggregate phía many về cùng grain trước khi ghép.
- [ ] C. Count so với count distinct cùng kiểm NULL và duplicate distribution.
- [ ] D. Khi population, identity, thời gian và status của customer đã được khóa.

<details><summary>Đáp án và phản hồi</summary>

**B. Giữ ở bảng sở hữu hoặc aggregate phía many về cùng grain trước khi ghép.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi: lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 4

Candidate key cần được kiểm bằng gì?

- [ ] A. Count so với count distinct cùng kiểm NULL và duplicate distribution.
- [ ] B. Chỉ chứng minh định danh row, không tự chứng minh nghĩa nghiệp vụ của grain.
- [ ] C. Viết câu 'mỗi dòng đại diện cho…' và khóa ứng viên trước bất kỳ SUM hoặc JOIN nào.
- [ ] D. Nếu yêu cầu chuyển từ đơn sang khách-tháng, phải công bố grain mới và rule phân bổ trước khi tổng hợp.

<details><summary>Đáp án và phản hồi</summary>

**A. Count so với count distinct cùng kiểm NULL và duplicate distribution.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi: lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 5

Primary key kỹ thuật chứng minh điều gì?

- [ ] A. Khi population, identity, thời gian và status của customer đã được khóa.
- [ ] B. Bảng kiểm grain gồm candidate key, uniqueness, row count, distinct key, join multiplicity và reconciliation total.
- [ ] C. Suy grain từ tên bảng, dùng DISTINCT để che fan-out hoặc coi primary key kỹ thuật là nghĩa nghiệp vụ.
- [ ] D. Chỉ chứng minh định danh row, không tự chứng minh nghĩa nghiệp vụ của grain.

<details><summary>Đáp án và phản hồi</summary>

**D. Chỉ chứng minh định danh row, không tự chứng minh nghĩa nghiệp vụ của grain.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi: lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 6

Khi nào COUNT(DISTINCT customer_id) hợp lệ?

- [ ] A. Nếu yêu cầu chuyển từ đơn sang khách-tháng, phải công bố grain mới và rule phân bổ trước khi tổng hợp.
- [ ] B. Lời cam kết một dòng đại diện cho đối tượng/sự kiện nào trong boundary đã nêu.
- [ ] C. Khi population, identity, thời gian và status của customer đã được khóa.
- [ ] D. Viết câu 'mỗi dòng đại diện cho…' và khóa ứng viên trước bất kỳ SUM hoặc JOIN nào.

<details><summary>Đáp án và phản hồi</summary>

**C. Khi population, identity, thời gian và status của customer đã được khóa.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi: lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 7

Trong tình huống mở bài, hành động đầu tiên tốt nhất là gì?

- [ ] A. Row count hoặc multiplicity trên base key tăng sau join.
- [ ] B. Viết câu 'mỗi dòng đại diện cho…' và khóa ứng viên trước bất kỳ SUM hoặc JOIN nào.
- [ ] C. Bảng kiểm grain gồm candidate key, uniqueness, row count, distinct key, join multiplicity và reconciliation total.
- [ ] D. Suy grain từ tên bảng, dùng DISTINCT để che fan-out hoặc coi primary key kỹ thuật là nghĩa nghiệp vụ.

<details><summary>Đáp án và phản hồi</summary>

**B. Viết câu 'mỗi dòng đại diện cho…' và khóa ứng viên trước bất kỳ SUM hoặc JOIN nào.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi: lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 8

Bằng chứng nào trực tiếp nhất để xác nhận năng lực của bài này?

- [ ] A. Bảng kiểm grain gồm candidate key, uniqueness, row count, distinct key, join multiplicity và reconciliation total.
- [ ] B. Nếu yêu cầu chuyển từ đơn sang khách-tháng, phải công bố grain mới và rule phân bổ trước khi tổng hợp.
- [ ] C. Lời cam kết một dòng đại diện cho đối tượng/sự kiện nào trong boundary đã nêu.
- [ ] D. Giữ ở bảng sở hữu hoặc aggregate phía many về cùng grain trước khi ghép.

<details><summary>Đáp án và phản hồi</summary>

**A. Bảng kiểm grain gồm candidate key, uniqueness, row count, distinct key, join multiplicity và reconciliation total.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi: lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 9

Khi constraint thay đổi, nguyên tắc xử lý đúng là gì?

- [ ] A. Suy grain từ tên bảng, dùng DISTINCT để che fan-out hoặc coi primary key kỹ thuật là nghĩa nghiệp vụ.
- [ ] B. Row count hoặc multiplicity trên base key tăng sau join.
- [ ] C. Count so với count distinct cùng kiểm NULL và duplicate distribution.
- [ ] D. Nếu yêu cầu chuyển từ đơn sang khách-tháng, phải công bố grain mới và rule phân bổ trước khi tổng hợp.

<details><summary>Đáp án và phản hồi</summary>

**D. Nếu yêu cầu chuyển từ đơn sang khách-tháng, phải công bố grain mới và rule phân bổ trước khi tổng hợp.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi: lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 10

Phát biểu nào mô tả critical failure của bài?

- [ ] A. Giữ ở bảng sở hữu hoặc aggregate phía many về cùng grain trước khi ghép.
- [ ] B. Chỉ chứng minh định danh row, không tự chứng minh nghĩa nghiệp vụ của grain.
- [ ] C. Suy grain từ tên bảng, dùng DISTINCT để che fan-out hoặc coi primary key kỹ thuật là nghĩa nghiệp vụ.
- [ ] D. Lời cam kết một dòng đại diện cho đối tượng/sự kiện nào trong boundary đã nêu.

<details><summary>Đáp án và phản hồi</summary>

**C. Suy grain từ tên bảng, dùng DISTINCT để che fan-out hoặc coi primary key kỹ thuật là nghĩa nghiệp vụ.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi: lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

## References

- [[wiki.da-foundation.entity-attribute-record-and-grain|Entities, attributes, records and grain]]
- [[wiki.data-modeling.fact-table-types|Fact table types]]
- [[wiki.database.joins-duplicate-multiplication-null|Join multiplication and NULL behavior]]
