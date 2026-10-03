# Phase 4: SQL and Database Internals
# Module 9: Relational Theory and SQL Execution
# Lesson 117: Normalization to BCNF, and deliberate denormalization

## Mục tiêu bài học

**Năng lực cần chứng minh.** Chuẩn hoá một bảng phẳng tới Boyce-Codd, chỉ ra dị thường nào được chữa ở bước nào, rồi phi chuẩn hoá một đường đọc có đo.

**Điều kiện hoàn thành.** Ba dị thường được tái hiện và gắn đúng bước chữa, và phần phi chuẩn hoá có số đo cả đọc, ghi lẫn dung lượng.

> [!abstract] Câu hỏi trung tâm
> Một bảng phẳng chứa phụ thuộc dư thừa tạo dị thường nào, decomposition nào bảo toàn thông tin và phụ thuộc, và khi nào lợi ích đọc đo được đủ trả chi phí đồng bộ của denormalization?

## 1. Bắt đầu từ dị thường

Chuẩn hóa không phải nghi thức tách table. Nó xử lý redundancy làm một fact được ghi nhiều nơi. Ba failure:

- insert anomaly: không ghi được fact A nếu chưa có fact B không liên quan;
- update anomaly: cùng fact xuất hiện nhiều row và cập nhật thiếu;
- delete anomaly: xóa fact B vô tình xóa fact A duy nhất.

Ví dụ `Enrollment(student_id,student_name,course_id,course_name,instructor)` lặp student/course facts theo mỗi enrollment. Đổi course_name phải sửa nhiều row; xóa enrollment cuối làm mất course. Tạo dữ liệu thật để tái hiện trước khi decomposition.

## 2. Functional dependency là đầu vào

FD $X\to Y$ là rule trên mọi valid state, không phải pattern của sample. Candidate key và attribute closure được xác định trước. Nếu FDs sai/thiếu, normalization “đúng thuật toán” vẫn sai domain.

Ghi nguồn mỗi FD: business contract, authoritative system, legal rule hay assumption. Sample chỉ tìm phản ví dụ. Time-varying dependency như postal code → province cần effective period hoặc relation lịch sử.

## 3. 1NF

1NF yêu cầu attribute values atomic theo relational domain và không có repeating groups. “Atomic” phụ thuộc operations: address string có thể atomic nếu chỉ hiển thị, nhưng không nếu cần validate/search components. JSON không tự vi phạm 1NF; vấn đề là domain và constraints/query needs, không kiểu syntax.

Tách repeating phone columns hoặc comma-separated product IDs thành relation. Tuy nhiên 1NF không loại partial/transitive dependency.

## 4. 2NF

2NF liên quan partial dependency của non-prime attribute vào proper subset của candidate key. Nó đáng chú ý khi composite keys. Trong Enrollment key `(student_id,course_id)`, `student_id -> student_name` và `course_id -> course_name`; đưa student/course facts ra relations riêng.

Nếu key chỉ một attribute, partial dependency trên key không tồn tại theo định nghĩa. Đừng tách table tùy tiện rồi gọi là 2NF.

## 5. 3NF

3NF loại transitive dependency không phù hợp từ key qua non-key determinant. Dạng formal: với mỗi nontrivial FD $X\to A$, X là superkey hoặc A là prime attribute. Rule mnemonic “non-key phụ thuộc key, whole key, nothing but key” hữu ích nhưng không thay formal check khi nhiều candidate keys.

Ví dụ employee_id → department_id và department_id → department_name. Department name thuộc Department relation. Nếu không, rename department tạo update anomaly.

## 6. BCNF

BCNF yêu cầu với mọi nontrivial FD $X\to Y$, X là superkey. BCNF mạnh hơn 3NF; relation có overlapping candidate keys có thể 3NF nhưng không BCNF. Decomposition theo violating FD thành `(X∪Y)` và `(R-Y)` theo algorithm, nhưng phải kiểm lossless và dependency preservation.

BCNF decomposition có thể mất khả năng enforce một FD bằng constraint trong một table. Vì vậy “BCNF luôn tốt hơn” sai nếu dependency preservation quan trọng. Quyết định ghi trade-off và enforcement plan.

## 7. Lossless join

Decomposition lossless nếu natural join các projections luôn tái tạo relation hợp lệ, không sinh spurious tuples. Với binary decomposition R→R1,R2, intersection cần functionally determine R1 hoặc R2 dưới F. Đây là property theo dependencies, không chứng minh bằng một sample join đúng.

Lossy decomposition làm join sinh combinations chưa từng tồn tại. Test sample có adversarial rows nhưng vẫn cần reasoning.

## 8. Dependency preservation

Nếu mọi FD ban đầu có thể kiểm bằng constraints trên từng decomposed relation mà không join, decomposition preserve dependencies. Nếu không, write validation có thể cần cross-table transaction/trigger và khó enforce.

Lossless và dependency-preserving là hai tiêu chí khác. 3NF synthesis thường ưu tiên bảo toàn dependency; BCNF có thể hy sinh. Designer phải nêu ưu tiên domain.

## 9. Constraints sau decomposition

Mỗi relation mới cần PK/candidate keys/FK/NOT NULL/CHECK. Tách table nhưng bỏ unique/FK không tự bảo vệ fact. Migration cần deduplicate theo business rule, không chọn row tùy ý. Orphan và conflicting repeated values phải được resolve có audit.

DDL phải phản ánh FD: determinant là UNIQUE/key khi phù hợp; dependent columns nằm đúng owner relation. Không phải mọi FD biểu diễn bằng một unique constraint.

## 10. Over-normalization là chẩn đoán workload, không phải số table

Nhiều joins không tự chứng minh schema “quá chuẩn hóa”. Cần đo latency, CPU, I/O, plan, caching, write volume và correctness cost. Có thể vấn đề do thiếu index, statistics, query grain hoặc API chứ không do normalization.

Đừng gộp table chỉ để giảm join nếu làm lặp fact có tần suất cập nhật cao. Complexity của view/query có thể giải bằng view/materialized view mà vẫn giữ write model chuẩn hóa.

## 11. Denormalization có chủ đích

Denormalization lưu lặp/derived data để tối ưu path đã đo: snapshot, precomputed aggregate, duplicated label, wide serving table. Nó tạo invariant mới: nhiều bản sao phải đồng bộ hoặc có freshness contract.

Trước khi làm, ghi:

1. query/workload bottleneck và baseline;
2. target SLO;
3. duplicated fact và authoritative owner;
4. writer/refresh path;
5. atomicity hoặc eventual consistency window;
6. reconciliation/repair;
7. read, write, storage measurement;
8. rollback/removal path.

Không có writer owner thì denormalized field là defect chờ xảy ra.

## 12. Các chiến lược đồng bộ

- cùng transaction khi cùng database và boundary;
- generated column cho expression local nếu DB hỗ trợ;
- trigger với cost/visibility/test rõ;
- outbox/CDC cập nhật read model eventual;
- scheduled rebuild/materialized view refresh;
- application dual write chỉ khi có protocol/reconciliation, không dựa may mắn.

Mỗi cách có failure window. Read model phải có watermark/freshness và backfill idempotent. Consumer duplicate/out-of-order cần xử lý.

## 13. Đo ba chiều

Read: p50/p95/p99, buffers, rows, CPU. Write: latency, locks, WAL, amplification và failure rate. Storage: table/index bytes, growth, backup/vacuum/refresh. Giữ cùng data/workload/config và lặp run.

Nếu read nhanh 30% nhưng write chậm gấp ba và correctness risk tăng, quyết định phụ thuộc workload ratio/SLO. Không tối ưu bằng một benchmark chỉ có SELECT.

## 14. Transactional và analytical models

OLTP thường ưu tiên normalized ownership và write correctness. Analytical star schema cố ý lặp dimension attributes/snapshot facts để query dễ và scan hiệu quả. Đây không phải “warehouse bỏ lý thuyết”; grain, keys, slowly changing dimensions và ETL quality thay vai trò enforcement.

Không copy OLTP schema nguyên xi vào serving analytics rồi kết luận mọi join chậm. Cũng không dùng star schema làm write model transactional nếu updates cần strong consistency.

## 15. Lab từ anomaly tới đo

Tạo bảng phẳng và dữ liệu gây đủ ba anomaly. Liệt kê FDs/candidate keys. Decompose 1NF→2NF→3NF→BCNF, ở mỗi bước chỉ anomaly/FD được xử lý, kiểm lossless và preservation. Tạo constraints và rerun invalid writes.

Sau đó chọn một read path, baseline, denormalize, thiết kế writer và fault test, đo read/write/storage. Kết luận có giữ thay đổi hay rollback. Artifact gồm DDL, seed, queries, plans, raw results và decision record.

## 15.1. Case study: enrollment và instructor assignment

Relation phẳng gồm student, course, section, instructor, room và grade dễ trộn nhiều facts. Student ID xác định student name; course ID xác định title; section ID xác định course, term, room và instructor; `(student_id,section_id)` xác định grade. Insert course mới bị chặn nếu chưa có enrollment; đổi room/instructor phải sửa mọi enrollment; xóa enrollment cuối có thể làm mất section. Đây là ba anomaly tái hiện được.

Decompose Student, Course, Section và Enrollment. Kiểm mỗi table có key/FD owner. Join lại theo keys phải lossless dưới constraints. Nếu domain cho một instructor dạy một course duy nhất nhưng instructor có thể đổi theo term, FD phải bao gồm effective context; viết `instructor→course` tuyệt đối sẽ normalize sai.

Giả sử dashboard đọc enrollment cùng course_title rất nhiều. Duplicating course_title vào serving table chỉ hợp lệ nếu nó là snapshot mong muốn hoặc CDC cập nhật có freshness SLO. Nếu cần historical label-at-enrollment, duplicate không phải cache mà là fact snapshot, và update course title không nên rewrite history. Cùng cột vật lý nhưng semantics khác dẫn tới writer khác; decision record phải nói rõ.

## 15.2. Fault tests cho denormalization

Kill producer sau authoritative commit trước outbox, delay consumer, deliver duplicate/out-of-order và rebuild từ source. Đo maximum staleness, mismatch count và repair duration. Nếu cùng transaction, inject constraint/trigger failure và kiểm rollback cả hai copies. Nếu materialized view, kiểm concurrent refresh behavior và reader visibility.

Reconciliation so authoritative key/version/checksum với serving copy; không chỉ count rows. Alert có threshold/owner, repair idempotent và lưu watermark. Rollback phải cho phép reader quay về normalized query hoặc rebuild copy. Nếu không có fallback, optimization đã trở thành single point of failure.

## 16. Câu hỏi tự kiểm tra

1. Ba anomaly khác nhau ở thao tác nào?
2. 2NF có ý nghĩa gì khi key đơn?
3. 3NF và BCNF khác determinant condition nào?
4. Lossless join khác dependency preservation ra sao?
5. BCNF decomposition khi nào làm enforcement khó hơn?
6. Denormalization cần writer và reconciliation nào?

## 17. Giới hạn và điều chưa cho phép kết luận

- Normal forms dựa trên FDs đã xác nhận; source semantics sai làm kết quả sai.
- Note chưa bao phủ đầy đủ multivalued/join dependencies và 4NF/5NF.
- Benchmark local không tự ngoại suy production.
- Denormalization không được biện minh chỉ bằng số join hoặc cảm giác query dài.

## Reference
1. [[SRC-HCMUT-FUNCTIONAL-DEPENDENCIES]] — PDF 6–65.
2. [[SRC-HCMUT-RELATIONAL-DATA-MODEL]] — keys và integrity.
3. [[SRC-POSTGRESQL-17-CONSTRAINTS]] — enforcement primitives.

## Source coverage

| Source slice | Nội dung phải giữ | Vị trí trong note | Trạng thái |
|---|---|---|---|
| [[SRC-HCMUT-FUNCTIONAL-DEPENDENCIES]], PDF 6–65 | anomalies, 1NF–BCNF, decomposition | §§1–8 | Đã giữ formal distinctions |
| [[SRC-HCMUT-RELATIONAL-DATA-MODEL]] | keys và constraints | §§2, 9 | Đã nối decomposition với DDL |
| [[SRC-POSTGRESQL-17-CONSTRAINTS]] | PK/UNIQUE/FK/CHECK | §9 | Đã giới hạn theo PostgreSQL 17 |
| Tổng hợp DE-L117 | deliberate denormalization và measurement | §§10–15 | Đã ghi writer/failure/rollback controls |

## Key takeaways
- Chuẩn hóa chữa redundancy anomalies dựa trên FDs, không phải tách table theo cảm giác.
- Lossless và dependency preservation là hai phép kiểm khác nhau.
- BCNF mạnh hơn 3NF nhưng có thể làm mất dependency preservation.
- Denormalization tạo consistency obligation mới và cần authoritative writer.
- Quyết định chỉ hợp lệ khi đo cả read, write và storage.
