---
loai: formative-quiz
lesson: 4
lesson_id: DE-L004
tieu_de: "Git as a content-addressed object database"
so_cau: 10
thoi_gian_phut: 18
trang_thai: ready-for-owner-review
nguong_dat: 8
---

# Quiz — DE Lesson 4: Git as a content-addressed object database

**Mục đích:** kiểm mental model và khả năng áp dụng, không dùng điểm danh làm bằng chứng.  
**Đạt:** ≥ 8/10. Câu 7-10 là critical transfer set; sai câu nào phải remediation và retest câu tương đương.

### Câu 1

Blob lưu gì?

- [ ] A. Top-level tree, parent(s) và metadata nằm trong commit object.
- [ ] B. Một ref có thể di chuyển trỏ tới commit.
- [ ] C. Parent, author/time hoặc message khác làm content commit object khác.
- [ ] D. Nội dung file; tên và mode nằm trong tree.

<details><summary>Đáp án và phản hồi</summary>

**D. Nội dung file; tên và mode nằm trong tree.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 2

Commit trỏ trực tiếp tới gì?

- [ ] A. HEAD trỏ trực tiếp commit thay vì symbolic ref tới branch.
- [ ] B. Vẽ working tree-index-HEAD và object graph trước khi chạy lệnh thay đổi trạng thái.
- [ ] C. Top-level tree, parent(s) và metadata nằm trong commit object.
- [ ] D. Ghi content hiện tại của path vào index cho snapshot kế tiếp.

<details><summary>Đáp án và phản hồi</summary>

**C. Top-level tree, parent(s) và metadata nằm trong commit object.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 3

git add thực sự làm gì?

- [ ] A. Dự đoán rồi đối chiếu bằng git status, diff, diff --cached, ls-files --stage, cat-file và log --graph.
- [ ] B. Ghi content hiện tại của path vào index cho snapshot kế tiếp.
- [ ] C. Một ref có thể di chuyển trỏ tới commit.
- [ ] D. Parent, author/time hoặc message khác làm content commit object khác.

<details><summary>Đáp án và phản hồi</summary>

**B. Ghi content hiện tại của path vào index cho snapshot kế tiếp.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 4

Branch là gì?

- [ ] A. Một ref có thể di chuyển trỏ tới commit.
- [ ] B. HEAD trỏ trực tiếp commit thay vì symbolic ref tới branch.
- [ ] C. Vẽ working tree-index-HEAD và object graph trước khi chạy lệnh thay đổi trạng thái.
- [ ] D. Đổi commit message hoặc parent tạo commit ID mới dù tree giống, vì commit object content đã đổi.

<details><summary>Đáp án và phản hồi</summary>

**A. Một ref có thể di chuyển trỏ tới commit.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 5

Detached HEAD nghĩa là gì?

- [ ] A. Parent, author/time hoặc message khác làm content commit object khác.
- [ ] B. Dự đoán rồi đối chiếu bằng git status, diff, diff --cached, ls-files --stage, cat-file và log --graph.
- [ ] C. Học thuộc lệnh reset mà không dự đoán ba cây, hoặc tin xóa branch đồng nghĩa object biến mất ngay.
- [ ] D. HEAD trỏ trực tiếp commit thay vì symbolic ref tới branch.

<details><summary>Đáp án và phản hồi</summary>

**D. HEAD trỏ trực tiếp commit thay vì symbolic ref tới branch.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 6

Vì sao cùng tree vẫn có commit ID khác?

- [ ] A. Đổi commit message hoặc parent tạo commit ID mới dù tree giống, vì commit object content đã đổi.
- [ ] B. Nội dung file; tên và mode nằm trong tree.
- [ ] C. Parent, author/time hoặc message khác làm content commit object khác.
- [ ] D. Vẽ working tree-index-HEAD và object graph trước khi chạy lệnh thay đổi trạng thái.

<details><summary>Đáp án và phản hồi</summary>

**C. Parent, author/time hoặc message khác làm content commit object khác.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 7

Trong tình huống mở bài, hành động đầu tiên tốt nhất là gì?

- [ ] A. Top-level tree, parent(s) và metadata nằm trong commit object.
- [ ] B. Vẽ working tree-index-HEAD và object graph trước khi chạy lệnh thay đổi trạng thái.
- [ ] C. Dự đoán rồi đối chiếu bằng git status, diff, diff --cached, ls-files --stage, cat-file và log --graph.
- [ ] D. Học thuộc lệnh reset mà không dự đoán ba cây, hoặc tin xóa branch đồng nghĩa object biến mất ngay.

<details><summary>Đáp án và phản hồi</summary>

**B. Vẽ working tree-index-HEAD và object graph trước khi chạy lệnh thay đổi trạng thái.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 8

Bằng chứng nào trực tiếp nhất để xác nhận năng lực của bài này?

- [ ] A. Dự đoán rồi đối chiếu bằng git status, diff, diff --cached, ls-files --stage, cat-file và log --graph.
- [ ] B. Đổi commit message hoặc parent tạo commit ID mới dù tree giống, vì commit object content đã đổi.
- [ ] C. Nội dung file; tên và mode nằm trong tree.
- [ ] D. Ghi content hiện tại của path vào index cho snapshot kế tiếp.

<details><summary>Đáp án và phản hồi</summary>

**A. Dự đoán rồi đối chiếu bằng git status, diff, diff --cached, ls-files --stage, cat-file và log --graph.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 9

Khi constraint thay đổi, nguyên tắc xử lý đúng là gì?

- [ ] A. Học thuộc lệnh reset mà không dự đoán ba cây, hoặc tin xóa branch đồng nghĩa object biến mất ngay.
- [ ] B. Top-level tree, parent(s) và metadata nằm trong commit object.
- [ ] C. Một ref có thể di chuyển trỏ tới commit.
- [ ] D. Đổi commit message hoặc parent tạo commit ID mới dù tree giống, vì commit object content đã đổi.

<details><summary>Đáp án và phản hồi</summary>

**D. Đổi commit message hoặc parent tạo commit ID mới dù tree giống, vì commit object content đã đổi.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 10

Phát biểu nào mô tả critical failure của bài?

- [ ] A. Ghi content hiện tại của path vào index cho snapshot kế tiếp.
- [ ] B. HEAD trỏ trực tiếp commit thay vì symbolic ref tới branch.
- [ ] C. Học thuộc lệnh reset mà không dự đoán ba cây, hoặc tin xóa branch đồng nghĩa object biến mất ngay.
- [ ] D. Nội dung file; tên và mode nằm trong tree.

<details><summary>Đáp án và phản hồi</summary>

**C. Học thuộc lệnh reset mà không dự đoán ba cây, hoặc tin xóa branch đồng nghĩa object biến mất ngay.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>
