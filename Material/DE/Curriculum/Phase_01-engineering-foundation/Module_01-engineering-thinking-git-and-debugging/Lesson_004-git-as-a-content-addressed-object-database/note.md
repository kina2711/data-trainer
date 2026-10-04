# Phase 1: Engineering Foundation
# Module 1: Engineering Thinking, Git and Debugging
# Lesson 4: Git as a content-addressed object database

## Mục tiêu bài học

**Năng lực cần chứng minh.** Vẽ đúng đồ thị đối tượng của một kho nhỏ và dự đoán con trỏ nào thay đổi sau mỗi thao tác.

**Điều kiện hoàn thành.** Đồ thị đối tượng vẽ đúng, và dự đoán khớp thực tế ở ≥ 5/6 thao tác.


# Git as a content-addressed object database

> [!abstract] Câu hỏi trung tâm
> Mô hình object, snapshot, index và references giải thích các thao tác Git như thế nào?

## 1. Git lưu snapshot qua object graph

Blob giữ nội dung file, tree ánh xạ tên và mode tới blob hoặc tree con, commit trỏ tới top-level tree cùng parent và metadata. Commit vì thế là node trong graph của snapshot, không phải một patch được lưu như đơn vị gốc. Diff là phép so sánh Git tính ra giữa hai trạng thái.

Hai file có cùng content có thể dùng cùng blob dù tên khác, vì tên nằm trong tree. Hai commit có tree giống nhau vẫn có identity khác nếu parent, author, timestamp hoặc message khác. Điều này giải thích vì sao cherry-pick hoặc rebase tạo commit mới dù patch trông giống.

## 2. Content-addressed identity

Object ID được suy từ type, size và content theo object format của repository. Thay một byte trong blob tạo identity khác; tree trỏ blob mới nên tree đổi; commit trỏ tree mới nên commit đổi. Chuỗi ảnh hưởng này tạo integrity có thể kiểm tra bằng traversal.

Không nên dạy SHA-1 như bản chất duy nhất của Git. Bản chất là object được gọi bằng digest của nội dung đã canonicalize; repository có thể dùng object format khác. Lab phải hỏi Git bằng `git hash-object` và `git cat-file`, không hard-code độ dài hash.

> [!synthesis]
> Phần này ghép contract của roadmap DE-L004 với các lát nguồn đã khai báo. Mọi threshold và tình huống cụ thể là thiết kế giáo trình, không phải lời trích nguyên văn của tác giả.

## 3. Working tree, index và repository

Working tree là bản checkout có thể sửa; index là snapshot dự kiến cho commit kế tiếp; repository giữ object và refs. `git add` cập nhật index bằng content hiện tại, không đơn giản đặt cờ đã theo dõi. Sửa file lần nữa sau add tạo hai phiên bản: index giữ bản đã stage, working tree giữ bản mới hơn.

`git status` và `git diff` chỉ có nghĩa khi biết hai trạng thái đang được so. `git diff` mặc định so working tree với index; `git diff --cached` so index với `HEAD`. Học thuộc output mà không nêu cặp trạng thái dẫn tới dự đoán sai khi partial staging.

## 4. References làm graph có tên

Branch là ref có thể di chuyển tới commit. `HEAD` thường là symbolic ref trỏ tới branch hiện tại; branch lại trỏ tới commit. Commit mới dùng commit hiện tại làm parent rồi cập nhật branch. Detached HEAD bỏ lớp branch nhưng không phá object graph.

Xóa branch chỉ xóa một ref, không xóa object ngay lập tức. Commit còn reachable từ ref khác hoặc reflog vẫn có thể tìm và phục hồi. Sau khi không còn reachable và hết retention, garbage collection mới có thể loại object; vì vậy xóa nhánh luôn an toàn cũng là kết luận quá rộng.

## 5. Reset được suy từ ba cây

Để hiểu reset, theo dõi `HEAD`, index và working tree riêng. `--soft` di chuyển ref/HEAD nhưng giữ index và working tree; mixed reset còn cập nhật index; hard reset cập nhật cả working tree và có thể làm mất thay đổi chưa lưu. Cú pháp nguy hiểm vì phạm vi mutation khác nhau, không phải vì tên lệnh khó nhớ.

Trước reset, ghi bảng trạng thái của ba vùng và dự đoán từng cột sau lệnh. Nếu mục tiêu chỉ bỏ stage hoặc khôi phục file, dùng command hẹp hơn giúp giảm blast radius. Không chạy hard reset dựa trên trực giác quay lại commit.

## 6. Đọc object thô để kiểm mô hình

Một repository ba commit đủ để kiểm mọi mệnh đề nền. Dùng `git rev-parse`, `git cat-file -t/-p`, `git ls-tree`, `git show-ref` và `git symbolic-ref HEAD` để dựng graph từ evidence. Dự đoán trước mỗi command rồi so output, tránh biến lab thành chép lệnh.

Bằng chứng cần ghi Git version, object format, commit IDs trước-sau và trạng thái ba vùng. Nếu command hiện đại thay output so với sách 2014, giữ cơ chế ổn định và ghi khác biệt phiên bản thay vì ép output cũ.

## 7. Tình huống xuyên suốt

Một file `orders.csv` được commit ba lần, lần hai thêm dòng và lần ba đổi tên. Học viên chứng minh blob của content không đổi được tái dùng, tree đổi khi tên đổi, commit đổi theo tree/parent, rồi tạo và xóa một branch để thấy ref biến mất trong khi commit còn trong reflog.

Tình huống của `wiki.engineering-foundation.git-object-database` phải được chạy trong sandbox hoặc fixture có version. Nếu chưa chạy, các kết quả mong đợi chỉ là protocol đánh giá; không được ghi thành observation. Người học giữ input, command, state trước-sau, raw output và một oracle độc lập đủ để reviewer tái hiện câu hỏi riêng của bài `Git as a content-addressed object database`.

## 8. Failure modes và ngộ nhận

- **Failure mode.** Nghĩ commit lưu patch thay vì snapshot graph. Cần đưa một counterexample nhỏ nhất để chứng minh hậu quả, sau đó ghi owner và cách phục hồi thay vì chỉ sửa câu chữ.

- **Failure mode.** Nghĩ staging area chỉ là danh sách tên file. Cần đưa một counterexample nhỏ nhất để chứng minh hậu quả, sau đó ghi owner và cách phục hồi thay vì chỉ sửa câu chữ.

- **Failure mode.** Đồng nhất `HEAD` với commit thay vì symbolic ref trong trường hợp thường. Cần đưa một counterexample nhỏ nhất để chứng minh hậu quả, sau đó ghi owner và cách phục hồi thay vì chỉ sửa câu chữ.

- **Failure mode.** Tin rằng xóa branch lập tức xóa commit hoặc hard reset luôn phục hồi được. Cần đưa một counterexample nhỏ nhất để chứng minh hậu quả, sau đó ghi owner và cách phục hồi thay vì chỉ sửa câu chữ.

## 9. Ma trận kiểm chứng

Mỗi probe dưới đây bắt đầu bằng dự đoán viết trước. Kết quả đạt chỉ được ghi khi artifact thực tế khớp oracle; exit code thành công không thay thế kiểm tra semantics.

### 9.1. Dựng đúng blob-tree-commit graph từ `cat-file`.

**Mệnh đề.** Dựng đúng blob-tree-commit graph từ `cat-file`.

**Thiết kế phép thử.** Tạo positive control và một boundary hoặc changed-constraint case chỉ khác đúng biến cần kiểm. Khóa fixture, phiên bản, identity và state ban đầu; ghi expected result trước khi chạy.

**Bằng chứng.** Giữ command, raw output, state transition và reconciliation với oracle không dùng chung assumption. Nếu evidence không phân biệt được mệnh đề đúng và sai, probe chưa có giá trị quyết định.

### 9.2. Stage rồi sửa tiếp phải quan sát được hai phiên bản file.

**Mệnh đề.** Stage rồi sửa tiếp phải quan sát được hai phiên bản file.

**Thiết kế phép thử.** Tạo positive control và một boundary hoặc changed-constraint case chỉ khác đúng biến cần kiểm. Khóa fixture, phiên bản, identity và state ban đầu; ghi expected result trước khi chạy.

**Bằng chứng.** Giữ command, raw output, state transition và reconciliation với oracle không dùng chung assumption. Nếu evidence không phân biệt được mệnh đề đúng và sai, probe chưa có giá trị quyết định.

### 9.3. Xóa branch nhưng tìm lại commit qua reflog.

**Mệnh đề.** Xóa branch nhưng tìm lại commit qua reflog.

**Thiết kế phép thử.** Tạo positive control và một boundary hoặc changed-constraint case chỉ khác đúng biến cần kiểm. Khóa fixture, phiên bản, identity và state ban đầu; ghi expected result trước khi chạy.

**Bằng chứng.** Giữ command, raw output, state transition và reconciliation với oracle không dùng chung assumption. Nếu evidence không phân biệt được mệnh đề đúng và sai, probe chưa có giá trị quyết định.

### 9.4. Soft, mixed và hard reset tạo đúng ba trạng thái đã dự đoán.

**Mệnh đề.** Soft, mixed và hard reset tạo đúng ba trạng thái đã dự đoán.

**Thiết kế phép thử.** Tạo positive control và một boundary hoặc changed-constraint case chỉ khác đúng biến cần kiểm. Khóa fixture, phiên bản, identity và state ban đầu; ghi expected result trước khi chạy.

**Bằng chứng.** Giữ command, raw output, state transition và reconciliation với oracle không dùng chung assumption. Nếu evidence không phân biệt được mệnh đề đúng và sai, probe chưa có giá trị quyết định.

### 9.5. Đổi message nhưng giữ tree vẫn tạo commit identity mới.

**Mệnh đề.** Đổi message nhưng giữ tree vẫn tạo commit identity mới.

**Thiết kế phép thử.** Tạo positive control và một boundary hoặc changed-constraint case chỉ khác đúng biến cần kiểm. Khóa fixture, phiên bản, identity và state ban đầu; ghi expected result trước khi chạy.

**Bằng chứng.** Giữ command, raw output, state transition và reconciliation với oracle không dùng chung assumption. Nếu evidence không phân biệt được mệnh đề đúng và sai, probe chưa có giá trị quyết định.

### 9.6. Clone sandbox và tái dựng graph trên Git version đã ghi.

**Mệnh đề.** Clone sandbox và tái dựng graph trên Git version đã ghi.

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
| [[SRC-CHACON-STRAUB-PRO-GIT-2E]]: `src.book.chacon-straub-pro-git.2e` | Chapter 1 PDF 42-43; Chapter 3 PDF 129-174; Chapter 7 PDF 422-434; Chapter 10 PDF 762-790 | object graph, refs, merge, rebase, reset và identity | §§1-9 | Đã phủ | Nội dung ngoài objective DE-L004 |

## Key takeaways
- Khi coi Git là object graph cộng refs và ba vùng, command trở thành hệ quả có thể dự đoán thay vì danh sách phải học thuộc.
- Một kết luận chỉ có giá trị trong scope, version và state đã ghi.
- Counterexample và changed-constraint test mạnh hơn việc lặp lại định nghĩa.
- Trước khi lab chạy, note này đã có provenance và protocol nhưng chưa phải chứng nhận production.

## References

- [[wiki.engineering-foundation.git-object-database|Git as a content-addressed object database]]
