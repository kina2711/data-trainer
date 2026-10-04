# Phase 1: Engineering Foundation
# Module 1: Engineering Thinking, Git and Debugging
# Lesson 5: Branching, merge, rebase and commit identity

## Mục tiêu bài học

**Năng lực cần chứng minh.** Chọn đúng giữa hợp nhất, rebase và đảo ngược cho một tình huống cho trước, và giải thích bằng định danh commit cùng phạm vi ảnh hưởng.

**Điều kiện hoàn thành.** Chọn đúng ≥ 3/4 tình huống kèm phạm vi ảnh hưởng, và giải thích đúng vị trí xung đột bằng tổ tiên chung.


# Branching, merge, rebase and commit identity

> [!abstract] Câu hỏi trung tâm
> Khi nào nên merge, rebase, squash hoặc revert, và lựa chọn đó thay đổi graph cùng người dùng khác ra sao?

## 1. Branch là con trỏ, divergence nằm ở graph

Tạo branch chỉ tạo ref tới commit hiện có. Khi hai branch nhận commit riêng, graph phân kỳ từ common ancestor. Work không được sao chép thành thư mục thứ hai; working tree được materialize theo commit mà `HEAD` chọn.

Trước integration, vẽ tips, parents và merge base. Nếu một tip reachable từ tip kia, merge có thể fast-forward bằng cách di chuyển ref. Nếu histories đã diverge, Git cần kết hợp snapshots và thường tạo merge commit hai parent.

## 2. Three-way merge và conflict

Three-way merge so hai tips với merge base. Thay đổi chỉ ở một phía thường được lấy tự động; thay đổi tương thích ở hai phía có thể kết hợp; thay đổi cạnh tranh trên cùng vùng khiến Git dừng. Conflict là bằng chứng thiếu quyết định nội dung, không phải lỗi engine.

Giải conflict cần đọc base, ours và theirs rồi xây kết quả thỏa invariant hiện tại. Chọn nguyên một phía có thể xóa thay đổi hợp lệ của phía kia. Sau resolution, test phải kiểm behavior chứ không chỉ kiểm marker conflict đã biến mất.

> [!synthesis]
> Phần này ghép contract của roadmap DE-L005 với các lát nguồn đã khai báo. Mọi threshold và tình huống cụ thể là thiết kế giáo trình, không phải lời trích nguyên văn của tác giả.

## 3. Rebase phát lại thay đổi lên base mới

Rebase tìm commits thuộc nhánh hiện tại nhưng không thuộc upstream, tính patch tương ứng rồi tạo commit mới trên base mới. Parent thay đổi nên commit identity thay đổi; author có thể được giữ nhưng committer metadata và graph không còn giống lịch sử cũ.

Lịch sử thẳng giúp đọc tuyến tính nhưng đổi lấy việc viết lại identity. Nó phù hợp cho branch riêng trước khi chia sẻ. Khi commit cũ đã được người khác dùng, force update bắt họ reconcile hai histories tương đương về nội dung nhưng khác identity.

## 4. Merge, squash và thông tin bị giữ hoặc mất

Merge commit giữ topology và parent của hai nhánh. Rebase giữ các bước logic theo tuyến nhưng thay identity. Squash tạo một commit tổng hợp và bỏ các boundary trung gian khỏi history đích. Không có lựa chọn luôn tốt; cần hỏi history được dùng để audit, bisect, revert hay chỉ để review kết quả.

Nếu chuỗi commit biểu diễn migration theo bước có deploy checkpoint, squash có thể xóa thông tin vận hành cần thiết. Nếu branch chứa nhiều fixup noise không có giá trị độc lập, squash có thể giảm chi phí đọc. Quyết định phải dựa vào consumer của history.

## 5. Revert và reset giải hai bài toán khác

Revert tạo commit mới có patch đảo tác dụng của commit đích; lịch sử công khai vẫn tiến về trước và collaborators không phải thay refs đã biết. Reset di chuyển ref và có thể cập nhật index/working tree; nó phù hợp cho lịch sử riêng hoặc phục hồi có kiểm soát.

Revert merge cần chọn mainline parent và không đồng nghĩa Git quên merge cũ. Một revert sau đó có thể ảnh hưởng merge lại. Vì vậy incident trên shared branch cần rehearsal trong clone và graph review, không chạy lệnh theo tên gọi.

## 6. Quy tắc quyết định dựa trên phạm vi ảnh hưởng

Hỏi ba câu: commit đã public chưa, topology có giá trị không, và cần giữ từng bước hay chỉ kết quả? Public history ưu tiên merge hoặc revert. Private history có thể rebase để sắp xếp. Squash phù hợp khi intermediate commits không phải đơn vị audit hoặc rollback.

Mọi rewrite cần backup ref, kiểm remote state và dùng lease khi force push được policy cho phép. `--force-with-lease` giảm nguy cơ ghi đè cập nhật chưa thấy nhưng không thay thế phối hợp con người; lease đúng vẫn có thể phá consumer dùng commit cũ.

## 7. Tình huống xuyên suốt

Ba bản sao của cùng repository tích hợp một feature và hotfix. Bản A merge giữ topology, bản B rebase feature lên hotfix, bản C squash feature. Nhóm so `git log --graph`, commit IDs, khả năng revert từng bước và hành vi của một clone đã fetch lịch sử cũ. Sau đó họ xử lý một conflict bằng cách kiểm invariant thay vì chọn ours/theirs nguyên khối.

Tình huống của `wiki.engineering-foundation.git-history-integration` phải được chạy trong sandbox hoặc fixture có version. Nếu chưa chạy, các kết quả mong đợi chỉ là protocol đánh giá; không được ghi thành observation. Người học giữ input, command, state trước-sau, raw output và một oracle độc lập đủ để reviewer tái hiện câu hỏi riêng của bài `Branching, merge, rebase and commit identity`.

## 8. Failure modes và ngộ nhận

- **Failure mode.** Rebase branch đã chia sẻ mà không phối hợp. Cần đưa một counterexample nhỏ nhất để chứng minh hậu quả, sau đó ghi owner và cách phục hồi thay vì chỉ sửa câu chữ.

- **Failure mode.** Dùng `reset --hard` để sửa shared branch. Cần đưa một counterexample nhỏ nhất để chứng minh hậu quả, sau đó ghi owner và cách phục hồi thay vì chỉ sửa câu chữ.

- **Failure mode.** Giải conflict bằng giữ một phía mà không đọc base. Cần đưa một counterexample nhỏ nhất để chứng minh hậu quả, sau đó ghi owner và cách phục hồi thay vì chỉ sửa câu chữ.

- **Failure mode.** Squash chuỗi migration cần rollback theo từng bước. Cần đưa một counterexample nhỏ nhất để chứng minh hậu quả, sau đó ghi owner và cách phục hồi thay vì chỉ sửa câu chữ.

## 9. Ma trận kiểm chứng

Mỗi probe dưới đây bắt đầu bằng dự đoán viết trước. Kết quả đạt chỉ được ghi khi artifact thực tế khớp oracle; exit code thành công không thay thế kiểm tra semantics.

### 9.1. Dự đoán merge base và loại merge trước khi chạy.

**Mệnh đề.** Dự đoán merge base và loại merge trước khi chạy.

**Thiết kế phép thử.** Tạo positive control và một boundary hoặc changed-constraint case chỉ khác đúng biến cần kiểm. Khóa fixture, phiên bản, identity và state ban đầu; ghi expected result trước khi chạy.

**Bằng chứng.** Giữ command, raw output, state transition và reconciliation với oracle không dùng chung assumption. Nếu evidence không phân biệt được mệnh đề đúng và sai, probe chưa có giá trị quyết định.

### 9.2. Chứng minh rebase tạo identity mới cho commits được replay.

**Mệnh đề.** Chứng minh rebase tạo identity mới cho commits được replay.

**Thiết kế phép thử.** Tạo positive control và một boundary hoặc changed-constraint case chỉ khác đúng biến cần kiểm. Khóa fixture, phiên bản, identity và state ban đầu; ghi expected result trước khi chạy.

**Bằng chứng.** Giữ command, raw output, state transition và reconciliation với oracle không dùng chung assumption. Nếu evidence không phân biệt được mệnh đề đúng và sai, probe chưa có giá trị quyết định.

### 9.3. Một clone cũ minh họa blast radius của force update.

**Mệnh đề.** Một clone cũ minh họa blast radius của force update.

**Thiết kế phép thử.** Tạo positive control và một boundary hoặc changed-constraint case chỉ khác đúng biến cần kiểm. Khóa fixture, phiên bản, identity và state ban đầu; ghi expected result trước khi chạy.

**Bằng chứng.** Giữ command, raw output, state transition và reconciliation với oracle không dùng chung assumption. Nếu evidence không phân biệt được mệnh đề đúng và sai, probe chưa có giá trị quyết định.

### 9.4. Revert giữ lịch sử tiến tới và tạo commit mới.

**Mệnh đề.** Revert giữ lịch sử tiến tới và tạo commit mới.

**Thiết kế phép thử.** Tạo positive control và một boundary hoặc changed-constraint case chỉ khác đúng biến cần kiểm. Khóa fixture, phiên bản, identity và state ban đầu; ghi expected result trước khi chạy.

**Bằng chứng.** Giữ command, raw output, state transition và reconciliation với oracle không dùng chung assumption. Nếu evidence không phân biệt được mệnh đề đúng và sai, probe chưa có giá trị quyết định.

### 9.5. Conflict resolution qua test invariant chứ không qua absence of markers.

**Mệnh đề.** Conflict resolution qua test invariant chứ không qua absence of markers.

**Thiết kế phép thử.** Tạo positive control và một boundary hoặc changed-constraint case chỉ khác đúng biến cần kiểm. Khóa fixture, phiên bản, identity và state ban đầu; ghi expected result trước khi chạy.

**Bằng chứng.** Giữ command, raw output, state transition và reconciliation với oracle không dùng chung assumption. Nếu evidence không phân biệt được mệnh đề đúng và sai, probe chưa có giá trị quyết định.

### 9.6. Bốn scenario đạt ít nhất ba lựa chọn đúng kèm affected users.

**Mệnh đề.** Bốn scenario đạt ít nhất ba lựa chọn đúng kèm affected users.

**Thiết kế phép thử.** Tạo positive control và một boundary hoặc changed-constraint case chỉ khác đúng biến cần kiểm. Khóa fixture, phiên bản, identity và state ban đầu; ghi expected result trước khi chạy.

**Bằng chứng.** Giữ command, raw output, state transition và reconciliation với oracle không dùng chung assumption. Nếu evidence không phân biệt được mệnh đề đúng và sai, probe chưa có giá trị quyết định.

## 10. Câu hỏi tự kiểm tra

1. Boundary nào làm mệnh đề trung tâm không còn đúng?
2. Artifact nào là nguồn thẩm quyền và artifact nào chỉ là tín hiệu?
3. Counterexample nhỏ nhất cần những state nào?
4. Một kiểm tra xanh giả có thể xuất hiện theo đường nào?
5. Constraint nào khiến quyết định phải đảo?
6. Phần nào hiện mới là protocol, chưa phải observation?

## 11. Giới hạn và điều chưa cho phép kết luận

- Nội dung là giáo trình và expected evidence; không tuyên bố đã kiểm chứng trên production.
- Hành vi phụ thuộc phiên bản phải được chạy lại với version ghi trong evidence package.
- Threshold, case study và decision rule tổng hợp cho curriculum không được gán nguyên văn cho nguồn.
- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.

## Reference
1. [[SRC-CHACON-STRAUB-PRO-GIT-2E]]

## Source coverage

| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |
|---|---|---|---|---|---|
| [[SRC-CHACON-STRAUB-PRO-GIT-2E]]: `src.book.chacon-straub-pro-git.2e` | Chapter 1 PDF 42-43; Chapter 3 PDF 129-174; Chapter 7 PDF 422-434; Chapter 10 PDF 762-790 | object graph, refs, merge, rebase, reset và identity | §§1-9 | Đã phủ | Nội dung ngoài objective DE-L005 |

## Key takeaways
- Lựa chọn integration là quyết định về graph, identity và collaborators; lịch sử đẹp không được đánh đổi bằng blast radius không được công bố.
- Một kết luận chỉ có giá trị trong scope, version và state đã ghi.
- Counterexample và changed-constraint test mạnh hơn việc lặp lại định nghĩa.
- Trước khi lab chạy, note này đã có provenance và protocol nhưng chưa phải chứng nhận production.

## References

- [[wiki.engineering-foundation.git-history-integration|Branching, merge, rebase and commit identity]]
