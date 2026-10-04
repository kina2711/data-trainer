---
marp: true
theme: volt
paginate: true
size: 16:9
header: 'DE · Lesson 4'
footer: 'Foundation · runnable scene package'
---

<!-- _class: lead -->

# Git as a content-addressed object database

**DE-L004**

> Object graph, index và refs giải thích Git như thế nào?

---

## Chuẩn đầu ra

Dựng object graph và dự đoán thay đổi ở working tree, index, repository, HEAD và branch ref sau thao tác Git.

**Evidence:** Dự đoán rồi đối chiếu bằng git status, diff, diff --cached, ls-files --stage, cat-file và log --graph.

**Không suy ra mastery từ việc có mặt hoặc xem hết slide.**

---

<!-- scene: S01 · source: note.md: heading 1. Git lưu snapshot qua object graph -->
## Tình huống mở

Bạn git add file, sửa tiếp rồi git commit. Vì sao commit không chứa bản đang nhìn thấy trong editor?

**Independent analysis followed by peer review**

1. Bạn sẽ làm gì đầu tiên?
2. Quyết định nào có thể bị ảnh hưởng?
3. Bằng chứng nào đang thiếu?

---

<!-- scene: S02 · source: note.md: heading 2. Content-addressed identity -->
## Mental model trung tâm

> Git lưu immutable content-addressed objects. working tree, index và repository là ba trạng thái khác nhau, còn refs đặt tên lên commit graph.

- Blob giữ content. tree giữ name/mode sang object. commit giữ tree, parents và metadata.
- git add chụp content vào index. diff phải luôn nêu hai trạng thái đang so.
- Branch là ref di chuyển. HEAD thường trỏ symbolic tới branch. reachability/reflog giải thích phục hồi.

---

## Luồng kiểm soát

| 1. Câu hỏi hoặc thay đổi | 2. Boundary | 3. Evidence | 4. Decision gate | 5. Theo dõi |
|---|---|---|---|---|
| Nêu outcome cần quyết định | Khóa scope và semantics | Dùng phép kiểm độc lập | Áp dụng có giới hạn hoặc dừng | Quan sát reversal trigger |

---

## Bước đầu tiên có tính quyết định

**Vẽ working tree-index-HEAD và object graph trước khi chạy lệnh thay đổi trạng thái.**

Không làm bước này, output sau đó có thể đúng cú pháp nhưng sai đối tượng, sai thời gian hoặc sai quyết định.

---

<!-- scene: S03 · source: note.md: heading 2. Content-addressed identity -->
## Check 1 · trả lời không nhìn tài liệu

**Blob lưu gì?**

<details>
<summary>Đáp án và tín hiệu chẩn đoán</summary>

Nội dung file. tên và mode nằm trong tree.

Nếu câu trả lời chỉ nêu tên công cụ, hãy quay lại mental model và nói rõ boundary + evidence + action.
</details>

---

<!-- scene: S04 · source: UNSOURCED guided practice synthesis -->
## Guided practice

Trong repo sandbox, học viên dự đoán sáu trạng thái rồi chạy command để kiểm bằng object plumbing.

**Definition of done:** Đúng ≥5/6 dự đoán, vẽ được blob-tree-commit graph và giải thích staged/unstaged bằng cặp trạng thái.

Người dạy không chữa bằng đáp án ngay. yêu cầu mỗi nhóm nêu assumption và phép kiểm trước.

---

<!-- scene: S05 · source: note.md: heading 3. Working tree, index và repository -->
## Quy tắc quyết định

Trước reset/restore, gọi tên ref và ba trạng thái sẽ đổi. dùng mode nhỏ nhất đạt mục tiêu và bảo toàn evidence cần giữ.

**Boundary:** Content-addressing hỗ trợ integrity và dedup. nó không tự xác minh tác giả hay ý nghĩa nghiệp vụ của thay đổi.

---

## Changed constraint

<!-- scene: S06 · source: UNSOURCED changed-constraint synthesis -->

Đổi commit message hoặc parent tạo commit ID mới dù tree giống, vì commit object content đã đổi.

**Thảo luận:** lựa chọn nào còn defensible? Bằng chứng nào làm bạn đảo quyết định?

---

## Worked example · đi từng bước

<!-- scene: S07 · source: note.md: heading 4. References làm graph có tên -->

1. Tạo file, hash-object để thấy blob identity, add và đọc index entry.
2. Commit để tạo tree/commit. cat-file -p lần theo parent và tree.
3. Sửa file sau add để quan sát index khác working tree.
4. Xóa branch rồi dùng reflog tìm commit còn reachable và tạo rescue ref.

---

## Evidence phải giữ lại

Dự đoán rồi đối chiếu bằng git status, diff, diff --cached, ls-files --stage, cat-file và log --graph.

Một output không có boundary, oracle hoặc limitation chỉ là kết quả chưa review.

---

## Failure modes

- **Critical:** Học thuộc lệnh reset mà không dự đoán ba cây, hoặc tin xóa branch đồng nghĩa object biến mất ngay.
- Chỉ kiểm happy path và sửa expected sau khi nhìn output.
- Gộp author claim, curriculum synthesis và learner conclusion thành một giọng.
- Dùng số lượng biểu đồ/test để thay thế oracle độc lập.

---

## Independent practice · không có đáp án mẫu

Tạo repo ba commit, partial staging, detached HEAD và deleted branch. thu evidence và phục hồi không mất work.

**Nộp:** artifact + evidence + limitation + reversal trigger.

---

<!-- scene: S08 · source: UNSOURCED curriculum transfer scenario -->
## Transfer challenge

Một commit 'mất' sau reset nhưng còn trong reflog. Giải thích reachability, retention và cách tạo ref cứu hộ trước thao tác khác.

Được phép có nhiều lựa chọn. Điểm nằm ở boundary, trade-off, evidence và blast radius: không nằm ở việc đoán ý người dạy.

---

<!-- scene: S09 · source: note.md: heading 5. Reset được suy từ ba cây -->
## Exit check

**git diff và git diff --cached so những trạng thái nào?**

<details><summary>Đáp án tối thiểu</summary>

git diff: working tree với index. git diff --cached: index với HEAD.
</details>

---

## Post-Lesson

1. Làm `quiz.md`. đạt **8/10**.
2. Nếu trượt một concept, đọc remediation trong `after-note.md` rồi retest đúng concept đó.
3. Hoàn thành `homework.md`. đạt **≥ 75/100** và không có critical failure.

**Bắc cầu:** DE-L005: merge, rebase, revert và commit identity.

---

## References

- [[wiki.engineering-foundation.git-object-database|Git as a content-addressed object database]]
- [[wiki.engineering-foundation.adr-trade-offs|Trade-offs and architecture decision records]]
- [[wiki.data-product.requirements-traceability|Requirements traceability]]
