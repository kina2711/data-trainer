---
marp: true
theme: volt
paginate: true
size: 16:9
header: 'DE · Lesson 5'
footer: 'Foundation · runnable scene package'
---

<!-- _class: lead -->

# Branching, merge, rebase and commit identity

**DE-L005**

> Chọn merge, rebase, squash, revert hay reset dựa trên graph và blast radius thế nào?

---

## Chuẩn đầu ra

Dự đoán graph/identity sau integration và chọn thao tác dựa trên history consumers, shared scope và recovery.

**Evidence:** Graph trước/sau, OID mapping, clone mô phỏng consumer, invariant tests và recovery command được chạy trong sandbox.

**Không suy ra mastery từ việc có mặt hoặc xem hết slide.**

---

<!-- scene: S01 · source: note.md: heading 1. Branch là con trỏ, divergence nằm ở graph -->
## Tình huống mở

Rebase một branch đã chia sẻ làm nội dung nhìn giống nhưng commit identity đổi. clone cũ và remote giờ kể hai lịch sử khác nhau.

**Independent analysis followed by peer review**

1. Bạn sẽ làm gì đầu tiên?
2. Quyết định nào có thể bị ảnh hưởng?
3. Bằng chứng nào đang thiếu?

---

<!-- scene: S02 · source: note.md: heading 2. Three-way merge và conflict -->
## Mental model trung tâm

> Integration là biến đổi commit graph. Merge giữ topology, rebase replay tạo identity mới, squash nén boundary. revert tiến lịch sử còn reset di chuyển ref.

- Tìm merge base và reachability để dự đoán fast-forward hay three-way merge.
- Rebase replay commits lên parent mới nên tạo OID mới và có blast radius với consumer đã dùng OID cũ.
- Chọn history shape theo audit, bisect, revert và collaboration. kiểm conflict bằng invariant/test.

---

## Luồng kiểm soát

| 1. Câu hỏi hoặc thay đổi | 2. Boundary | 3. Evidence | 4. Decision gate | 5. Theo dõi |
|---|---|---|---|---|
| Nêu outcome cần quyết định | Khóa scope và semantics | Dùng phép kiểm độc lập | Áp dụng có giới hạn hoặc dừng | Quan sát reversal trigger |

---

## Bước đầu tiên có tính quyết định

**Vẽ tips, parents, merge base và những người/automation đang dùng các commit trước khi chọn thao tác.**

Không làm bước này, output sau đó có thể đúng cú pháp nhưng sai đối tượng, sai thời gian hoặc sai quyết định.

---

<!-- scene: S03 · source: note.md: heading 2. Three-way merge và conflict -->
## Check 1 · trả lời không nhìn tài liệu

**Fast-forward xảy ra khi nào?**

<details>
<summary>Đáp án và tín hiệu chẩn đoán</summary>

Tip hiện tại là ancestor của tip được hợp nhất nên ref chỉ cần di chuyển.

Nếu câu trả lời chỉ nêu tên công cụ, hãy quay lại mental model và nói rõ boundary + evidence + action.
</details>

---

<!-- scene: S04 · source: UNSOURCED guided practice synthesis -->
## Guided practice

Bốn scenario card: branch riêng, shared branch, bad release, noisy fixups. Chọn operation, vẽ graph và nêu affected users.

**Definition of done:** Đúng ≥3/4 lựa chọn. mỗi lựa chọn có merge base/OID reasoning, blast radius và recovery.

Người dạy không chữa bằng đáp án ngay. yêu cầu mỗi nhóm nêu assumption và phép kiểm trước.

---

<!-- scene: S05 · source: note.md: heading 3. Rebase phát lại thay đổi lên base mới -->
## Quy tắc quyết định

Không rewrite identity đã chia sẻ nếu chưa có coordinated migration. dùng revert cho lịch sử công khai, reset cho ref cục bộ/recovery có containment.

**Boundary:** Lịch sử thẳng không đồng nghĩa lịch sử đúng. topology bị xóa có thể làm mất thông tin vận hành.

---

## Changed constraint

<!-- scene: S06 · source: UNSOURCED changed-constraint synthesis -->

Nếu commit boundaries là deployment checkpoints, squash làm mất khả năng bisect/revert theo bước và có thể không chấp nhận được.

**Thảo luận:** lựa chọn nào còn defensible? Bằng chứng nào làm bạn đảo quyết định?

---

## Worked example · đi từng bước

<!-- scene: S07 · source: note.md: heading 4. Merge, squash và thông tin bị giữ hoặc mất -->

1. Nhánh riêng chưa chia sẻ: rebase lên main để cập nhật base và giữ commits logic sạch.
2. Nhánh shared: merge để không đổi identity mà consumer đã dùng.
3. Bad commit đã phát hành: revert tạo inverse commit, giữ audit và tương thích clone.
4. Conflict: đọc base/ours/theirs, dựng output theo invariant rồi chạy test. không chọn nguyên một phía theo thói quen.

---

## Evidence phải giữ lại

Graph trước/sau, OID mapping, clone mô phỏng consumer, invariant tests và recovery command được chạy trong sandbox.

Một output không có boundary, oracle hoặc limitation chỉ là kết quả chưa review.

---

## Failure modes

- **Critical:** Force-push chỉ để có graph đẹp, hoặc coi hết conflict marker là bằng chứng behavior đúng.
- Chỉ kiểm happy path và sửa expected sau khi nhìn output.
- Gộp author claim, curriculum synthesis và learner conclusion thành một giọng.
- Dùng số lượng biểu đồ/test để thay thế oracle độc lập.

---

## Independent practice · không có đáp án mẫu

Dựng hai clone và remote local, tạo divergence, merge, rebase và revert. chứng minh identity/blast radius bằng log graph.

**Nộp:** artifact + evidence + limitation + reversal trigger.

---

<!-- scene: S08 · source: UNSOURCED curriculum transfer scenario -->
## Transfer challenge

Pipeline pin commit SHA cũ trong khi team muốn rebase branch. Thiết kế migration hoặc chọn operation không phá consumer.

Được phép có nhiều lựa chọn. Điểm nằm ở boundary, trade-off, evidence và blast radius: không nằm ở việc đoán ý người dạy.

---

<!-- scene: S09 · source: note.md: heading 5. Revert và reset giải hai bài toán khác -->
## Exit check

**Revert khác reset ở outcome lịch sử và phạm vi ảnh hưởng thế nào?**

<details><summary>Đáp án tối thiểu</summary>

Revert thêm commit đảo thay đổi và an toàn hơn cho lịch sử shared. reset di chuyển ref và có thể làm commit biến khỏi history hiện tại.
</details>

---

## Post-Lesson

1. Làm `quiz.md`. đạt **8/10**.
2. Nếu trượt một concept, đọc remediation trong `after-note.md` rồi retest đúng concept đó.
3. Hoàn thành `homework.md`. đạt **≥ 75/100** và không có critical failure.

**Bắc cầu:** DE-L006: phục hồi lost work bằng reflog, detached HEAD và bisect.

---

## References

- [[wiki.engineering-foundation.git-history-integration|Branching, merge, rebase and commit identity]]
- [[wiki.engineering-foundation.git-object-database|Git as a content-addressed object database]]
- [[wiki.engineering-foundation.adr-trade-offs|Trade-offs and architecture decision records]]
