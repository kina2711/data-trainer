---
loai: formative-quiz
lesson: 3
lesson_id: DE-L003
tieu_de: "Trade-offs and the architecture decision record"
so_cau: 10
thoi_gian_phut: 18
trang_thai: ready-for-owner-review
nguong_dat: 8
---

# Quiz — DE Lesson 3: Trade-offs and the architecture decision record

**Mục đích:** kiểm mental model và khả năng áp dụng, không dùng điểm danh làm bằng chứng.  
**Đạt:** ≥ 8/10. Câu 7-10 là critical transfer set; sai câu nào phải remediation và retest câu tương đương.

### Câu 1

ADR lưu gì quan trọng nhất?

- [ ] A. Vi phạm hard constraint loại option; không được bù bằng điểm ở tiêu chí khác.
- [ ] B. Đo được, có owner và gắn với assumption/constraint cụ thể.
- [ ] C. Tạo quyết định mới thay thế nhưng giữ lịch sử và liên kết bản cũ.
- [ ] D. Context và reasoning đủ để tái tạo quyết định khi constraint thay đổi.

<details><summary>Đáp án và phản hồi</summary>

**D. Context và reasoning đủ để tái tạo quyết định khi constraint thay đổi.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 2

Hard constraint khác weighted criterion thế nào?

- [ ] A. Khi kết quả có thể phân biệt option và làm recommendation thay đổi.
- [ ] B. Viết context, decision scope và hard constraints trước khi nêu phương án yêu thích.
- [ ] C. Vi phạm hard constraint loại option; không được bù bằng điểm ở tiêu chí khác.
- [ ] D. Lợi ích, cost, failure mode và evidence có thể đảo đánh giá.

<details><summary>Đáp án và phản hồi</summary>

**C. Vi phạm hard constraint loại option; không được bù bằng điểm ở tiêu chí khác.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 3

Một option tốt cần mô tả gì?

- [ ] A. Reviewer tái tạo recommendation từ drivers/evidence và changed constraint làm recommendation đảo đúng rule.
- [ ] B. Lợi ích, cost, failure mode và evidence có thể đảo đánh giá.
- [ ] C. Đo được, có owner và gắn với assumption/constraint cụ thể.
- [ ] D. Tạo quyết định mới thay thế nhưng giữ lịch sử và liên kết bản cũ.

<details><summary>Đáp án và phản hồi</summary>

**B. Lợi ích, cost, failure mode và evidence có thể đảo đánh giá.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 4

Revisit signal tốt có tính chất gì?

- [ ] A. Đo được, có owner và gắn với assumption/constraint cụ thể.
- [ ] B. Khi kết quả có thể phân biệt option và làm recommendation thay đổi.
- [ ] C. Viết context, decision scope và hard constraints trước khi nêu phương án yêu thích.
- [ ] D. Nếu consumer chính chuyển sang spreadsheet không hỗ trợ Parquet, compatibility gate có thể đảo quyết định dù benchmark không đổi.

<details><summary>Đáp án và phản hồi</summary>

**A. Đo được, có owner và gắn với assumption/constraint cụ thể.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 5

Spike có giá trị khi nào?

- [ ] A. Tạo quyết định mới thay thế nhưng giữ lịch sử và liên kết bản cũ.
- [ ] B. Reviewer tái tạo recommendation từ drivers/evidence và changed constraint làm recommendation đảo đúng rule.
- [ ] C. Viết ADR sau khi đã chọn để hợp thức hóa, dùng strawman hoặc không ghi consequence/revisit signal.
- [ ] D. Khi kết quả có thể phân biệt option và làm recommendation thay đổi.

<details><summary>Đáp án và phản hồi</summary>

**D. Khi kết quả có thể phân biệt option và làm recommendation thay đổi.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 6

Supersede ADR nghĩa là gì?

- [ ] A. Nếu consumer chính chuyển sang spreadsheet không hỗ trợ Parquet, compatibility gate có thể đảo quyết định dù benchmark không đổi.
- [ ] B. Context và reasoning đủ để tái tạo quyết định khi constraint thay đổi.
- [ ] C. Tạo quyết định mới thay thế nhưng giữ lịch sử và liên kết bản cũ.
- [ ] D. Viết context, decision scope và hard constraints trước khi nêu phương án yêu thích.

<details><summary>Đáp án và phản hồi</summary>

**C. Tạo quyết định mới thay thế nhưng giữ lịch sử và liên kết bản cũ.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 7

Trong tình huống mở bài, hành động đầu tiên tốt nhất là gì?

- [ ] A. Vi phạm hard constraint loại option; không được bù bằng điểm ở tiêu chí khác.
- [ ] B. Viết context, decision scope và hard constraints trước khi nêu phương án yêu thích.
- [ ] C. Reviewer tái tạo recommendation từ drivers/evidence và changed constraint làm recommendation đảo đúng rule.
- [ ] D. Viết ADR sau khi đã chọn để hợp thức hóa, dùng strawman hoặc không ghi consequence/revisit signal.

<details><summary>Đáp án và phản hồi</summary>

**B. Viết context, decision scope và hard constraints trước khi nêu phương án yêu thích.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 8

Bằng chứng nào trực tiếp nhất để xác nhận năng lực của bài này?

- [ ] A. Reviewer tái tạo recommendation từ drivers/evidence và changed constraint làm recommendation đảo đúng rule.
- [ ] B. Nếu consumer chính chuyển sang spreadsheet không hỗ trợ Parquet, compatibility gate có thể đảo quyết định dù benchmark không đổi.
- [ ] C. Context và reasoning đủ để tái tạo quyết định khi constraint thay đổi.
- [ ] D. Lợi ích, cost, failure mode và evidence có thể đảo đánh giá.

<details><summary>Đáp án và phản hồi</summary>

**A. Reviewer tái tạo recommendation từ drivers/evidence và changed constraint làm recommendation đảo đúng rule.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 9

Khi constraint thay đổi, nguyên tắc xử lý đúng là gì?

- [ ] A. Viết ADR sau khi đã chọn để hợp thức hóa, dùng strawman hoặc không ghi consequence/revisit signal.
- [ ] B. Vi phạm hard constraint loại option; không được bù bằng điểm ở tiêu chí khác.
- [ ] C. Đo được, có owner và gắn với assumption/constraint cụ thể.
- [ ] D. Nếu consumer chính chuyển sang spreadsheet không hỗ trợ Parquet, compatibility gate có thể đảo quyết định dù benchmark không đổi.

<details><summary>Đáp án và phản hồi</summary>

**D. Nếu consumer chính chuyển sang spreadsheet không hỗ trợ Parquet, compatibility gate có thể đảo quyết định dù benchmark không đổi.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>

---

### Câu 10

Phát biểu nào mô tả critical failure của bài?

- [ ] A. Lợi ích, cost, failure mode và evidence có thể đảo đánh giá.
- [ ] B. Khi kết quả có thể phân biệt option và làm recommendation thay đổi.
- [ ] C. Viết ADR sau khi đã chọn để hợp thức hóa, dùng strawman hoặc không ghi consequence/revisit signal.
- [ ] D. Context và reasoning đủ để tái tạo quyết định khi constraint thay đổi.

<details><summary>Đáp án và phản hồi</summary>

**C. Viết ADR sau khi đã chọn để hợp thức hóa, dùng strawman hoặc không ghi consequence/revisit signal.**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>
