---
loai: formative-quiz
lesson: 5
lesson_id: DE-L005
tieu_de: "Branching, merge, rebase and commit identity"
so_cau: 10
trang_thai: ready-for-owner-review
nguong_dat: 8
---

# Quiz: DE Lesson 5: Branching, merge, rebase and commit identity

**Mục đích:** kiểm mental model và khả năng áp dụng, không dùng điểm danh làm bằng chứng.
**Đạt:** ≥ 8/10. Câu 7-10 là critical transfer set; sai câu nào phải remediation và retest câu tương đương.

### Câu 1

Fast-forward xảy ra khi nào?

- [ ] A. Hai tips và merge base chung.
- [ ] B. Các commit boundary và topology trung gian trên history đích.
- [ ] C. Khi bad change đã nằm trong lịch sử shared/công khai cần giữ audit và identity hiện có.
- [ ] D. Tip hiện tại là ancestor của tip được hợp nhất nên ref chỉ cần di chuyển.

<details><summary>Đáp án và phản hồi</summary>

**D. Tip hiện tại là ancestor của tip được hợp nhất nên ref chỉ cần di chuyển.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi: lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 2

Three-way merge dùng ba trạng thái nào?

- [ ] A. Kết quả thỏa invariant và test, không chỉ khi marker biến mất.
- [ ] B. Vẽ tips, parents, merge base và những người/automation đang dùng các commit trước khi chọn thao tác.
- [ ] C. Hai tips và merge base chung.
- [ ] D. Commit được tạo lại trên parent mới nên object content và OID đổi.

<details><summary>Đáp án và phản hồi</summary>

**C. Hai tips và merge base chung.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi: lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 3

Vì sao rebase đổi commit identity?

- [ ] A. Graph trước/sau, OID mapping, clone mô phỏng consumer, invariant tests và recovery command được chạy trong sandbox.
- [ ] B. Commit được tạo lại trên parent mới nên object content và OID đổi.
- [ ] C. Các commit boundary và topology trung gian trên history đích.
- [ ] D. Khi bad change đã nằm trong lịch sử shared/công khai cần giữ audit và identity hiện có.

<details><summary>Đáp án và phản hồi</summary>

**B. Commit được tạo lại trên parent mới nên object content và OID đổi.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi: lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 4

Squash mất thông tin gì?

- [ ] A. Các commit boundary và topology trung gian trên history đích.
- [ ] B. Kết quả thỏa invariant và test, không chỉ khi marker biến mất.
- [ ] C. Vẽ tips, parents, merge base và những người/automation đang dùng các commit trước khi chọn thao tác.
- [ ] D. Nếu commit boundaries là deployment checkpoints, squash làm mất khả năng bisect/revert theo bước và có thể không chấp nhận được.

<details><summary>Đáp án và phản hồi</summary>

**A. Các commit boundary và topology trung gian trên history đích.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi: lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 5

Conflict resolution hoàn thành khi nào?

- [ ] A. Khi bad change đã nằm trong lịch sử shared/công khai cần giữ audit và identity hiện có.
- [ ] B. Graph trước/sau, OID mapping, clone mô phỏng consumer, invariant tests và recovery command được chạy trong sandbox.
- [ ] C. Force-push chỉ để có graph đẹp, hoặc coi hết conflict marker là bằng chứng behavior đúng.
- [ ] D. Kết quả thỏa invariant và test, không chỉ khi marker biến mất.

<details><summary>Đáp án và phản hồi</summary>

**D. Kết quả thỏa invariant và test, không chỉ khi marker biến mất.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi: lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 6

Khi nào ưu tiên revert?

- [ ] A. Nếu commit boundaries là deployment checkpoints, squash làm mất khả năng bisect/revert theo bước và có thể không chấp nhận được.
- [ ] B. Tip hiện tại là ancestor của tip được hợp nhất nên ref chỉ cần di chuyển.
- [ ] C. Khi bad change đã nằm trong lịch sử shared/công khai cần giữ audit và identity hiện có.
- [ ] D. Vẽ tips, parents, merge base và những người/automation đang dùng các commit trước khi chọn thao tác.

<details><summary>Đáp án và phản hồi</summary>

**C. Khi bad change đã nằm trong lịch sử shared/công khai cần giữ audit và identity hiện có.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi: lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 7

Trong tình huống mở bài, hành động đầu tiên tốt nhất là gì?

- [ ] A. Hai tips và merge base chung.
- [ ] B. Vẽ tips, parents, merge base và những người/automation đang dùng các commit trước khi chọn thao tác.
- [ ] C. Graph trước/sau, OID mapping, clone mô phỏng consumer, invariant tests và recovery command được chạy trong sandbox.
- [ ] D. Force-push chỉ để có graph đẹp, hoặc coi hết conflict marker là bằng chứng behavior đúng.

<details><summary>Đáp án và phản hồi</summary>

**B. Vẽ tips, parents, merge base và những người/automation đang dùng các commit trước khi chọn thao tác.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi: lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 8

Bằng chứng nào trực tiếp nhất để xác nhận năng lực của bài này?

- [ ] A. Graph trước/sau, OID mapping, clone mô phỏng consumer, invariant tests và recovery command được chạy trong sandbox.
- [ ] B. Nếu commit boundaries là deployment checkpoints, squash làm mất khả năng bisect/revert theo bước và có thể không chấp nhận được.
- [ ] C. Tip hiện tại là ancestor của tip được hợp nhất nên ref chỉ cần di chuyển.
- [ ] D. Commit được tạo lại trên parent mới nên object content và OID đổi.

<details><summary>Đáp án và phản hồi</summary>

**A. Graph trước/sau, OID mapping, clone mô phỏng consumer, invariant tests và recovery command được chạy trong sandbox.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi: lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 9

Khi constraint thay đổi, nguyên tắc xử lý đúng là gì?

- [ ] A. Force-push chỉ để có graph đẹp, hoặc coi hết conflict marker là bằng chứng behavior đúng.
- [ ] B. Hai tips và merge base chung.
- [ ] C. Các commit boundary và topology trung gian trên history đích.
- [ ] D. Nếu commit boundaries là deployment checkpoints, squash làm mất khả năng bisect/revert theo bước và có thể không chấp nhận được.

<details><summary>Đáp án và phản hồi</summary>

**D. Nếu commit boundaries là deployment checkpoints, squash làm mất khả năng bisect/revert theo bước và có thể không chấp nhận được.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi: lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 10

Phát biểu nào mô tả critical failure của bài?

- [ ] A. Commit được tạo lại trên parent mới nên object content và OID đổi.
- [ ] B. Kết quả thỏa invariant và test, không chỉ khi marker biến mất.
- [ ] C. Force-push chỉ để có graph đẹp, hoặc coi hết conflict marker là bằng chứng behavior đúng.
- [ ] D. Tip hiện tại là ancestor của tip được hợp nhất nên ref chỉ cần di chuyển.

<details><summary>Đáp án và phản hồi</summary>

**C. Force-push chỉ để có graph đẹp, hoặc coi hết conflict marker là bằng chứng behavior đúng.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi: lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

## References

- [[wiki.engineering-foundation.git-history-integration|Branching, merge, rebase and commit identity]]
- [[wiki.engineering-foundation.git-object-database|Git as a content-addressed object database]]
- [[wiki.engineering-foundation.adr-trade-offs|Trade-offs and architecture decision records]]
