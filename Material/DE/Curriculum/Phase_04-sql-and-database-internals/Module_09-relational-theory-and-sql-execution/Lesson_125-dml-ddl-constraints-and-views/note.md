# Phase 4: SQL and Database Internals
# Module 9: Relational Theory and SQL Execution
# Lesson 125: DML, DDL, constraints and views

## Mục tiêu bài học

**Năng lực cần chứng minh.** Viết lệnh ghi bất biến theo khoá nghiệp vụ và đổi cấu trúc bảng lớn mà không khoá bảng quá ngưỡng.

**Điều kiện hoàn thành.** Ghi lặp năm lần không sinh trùng, và thời gian khoá khi thêm ràng buộc dưới ngưỡng ở cách làm hai bước.

> [!abstract] Câu hỏi trung tâm
> Một thao tác ghi bảo vệ bất biến nào, giữ lock gì, có thể chạy lại ra sao, và schema/view thay đổi được phát hành thế nào mà không vượt lock budget?

## 1. Bắt đầu từ bất biến

DML và DDL không phải hai danh sách cú pháp độc lập. DML làm thay đổi trạng thái; DDL định nghĩa cấu trúc và các bất biến mà mọi writer phải tuân theo. Thiết kế bắt đầu bằng phát biểu có thể kiểm: “mỗi event chỉ có một row cho business key”, “amount không âm”, “order phải trỏ tới customer tồn tại”, “mỗi email chuẩn hóa là duy nhất trong tenant”.

Ứng dụng có thể kiểm sớm để trả lỗi đẹp, nhưng database constraint là ranh giới cuối cho nhiều writer và concurrency. Query kiểm `SELECT` rồi mới `INSERT` không nguyên tử: hai transaction có thể cùng thấy chưa tồn tại. Unique constraint/index biến race thành một quyết định tuần tự có thể bắt lỗi hoặc dùng conflict clause.

Không phải mọi business rule đặt được trong row constraint. Rule xuyên row/table, temporal overlap hoặc external state cần exclusion constraint, trigger, transaction protocol hay data-quality job. Ghi rõ nơi sở hữu invariant.

## 2. INSERT, UPDATE và DELETE

`INSERT` tạo rows; column list phải explicit để schema evolution không đổi mapping ngầm. Multi-row insert là một statement nhưng error behavior còn phụ thuộc constraint/transaction. `UPDATE` chọn target bằng predicate rồi tạo row versions theo MVCC; một predicate rộng có thể giữ nhiều row locks, sinh WAL và bloat. `DELETE` cũng là write có lock, WAL, FK effect và vacuum hậu xử lý.

Mọi write production cần bounded predicate, expected affected-row count và guard. Nếu kỳ vọng một row, `UPDATE ... WHERE business_key = ...` phải kiểm command count bằng một; zero và nhiều hơn một là hai failure modes khác nhau.

Batch lớn nên chia theo stable key/range, commit có chủ đích và theo dõi replication lag, WAL, lock waits. Chia batch đổi atomicity; recovery/checkpoint phải được thiết kế.

## 3. RETURNING và audit trong cùng statement

PostgreSQL hỗ trợ `RETURNING` cho `INSERT`, `UPDATE`, `DELETE` và `MERGE`, trả các cột của rows đã thay đổi mà không cần query lại. Nó hữu ích lấy generated ID, old/new values phù hợp, timestamp/default/trigger effects và đưa vào CTE/audit flow.

`RETURNING` không tự tạo audit log bền vững. Nếu application nhận kết quả rồi ghi audit ở hệ khác, vẫn có failure window. Muốn audit atomic trong database, audit insert phải thuộc cùng transaction và có schema/provenance rõ. Trigger hoặc data-modifying CTE là lựa chọn cần cân trade-off.

Không log payload nhạy cảm chỉ vì RETURNING tiện. Chọn fields, redaction, retention và access policy.

## 4. UPSERT và business key

PostgreSQL `INSERT ... ON CONFLICT` dựa trên unique/exclusion arbiter. Nó chỉ đúng khi conflict target đại diện business identity. Surrogate primary key không giúp deduplicate cùng event nếu mỗi retry sinh UUID mới.

Idempotent write cần request/business key ổn định, unique constraint và semantics khi payload khác cho cùng key. Có thể reject mismatch, giữ first result hoặc version theo rule; không im lặng overwrite.

`DO UPDATE` vẫn là update: có lock, triggers, index maintenance và possibly bloat. Năm lần chạy cùng source không sinh thêm row chưa đủ; phải kiểm field outcome và side effects không lặp.

## 5. MERGE và source uniqueness

`MERGE` mô tả nhiều nhánh matched/not matched trên source–target join. Nó không biến source duplicate thành deterministic. Nếu nhiều source rows cùng match một target, cardinality violation hoặc outcome phụ thuộc điều kiện/engine; pipeline phải canonicalize source về một row/business key trước.

Quy trình: profile duplicates; chọn winner bằng version/event time + deterministic tie-break; quarantine conflicts; assert uniqueness; mới MERGE. Target cần unique constraint phù hợp để bảo vệ concurrent writers.

Không gọi MERGE là idempotent chỉ từ cú pháp. Chạy lại phải được chứng minh bằng row counts, checksum, audit events và business state.

## 6. DDL là thay đổi vận hành

`ALTER TABLE` có nhiều subcommands với lock level, scan/rewrite và duration khác nhau. Cùng từ khóa nhưng blast radius khác: thêm nullable column không default volatile có thể metadata-only; đổi type có thể rewrite; add/validate constraint có scan và locks; set not null có thể scan nếu chưa có bằng chứng constraint.

Trước migration, tra manual đúng PostgreSQL version, đo table/index size, write rate, long transactions, replicas, free disk và dependency. Đặt `lock_timeout` để fail nhanh thay vì chờ rồi bất ngờ chặn traffic; đặt `statement_timeout` theo maintenance budget.

DDL transactional của PostgreSQL giúp rollback nhiều thay đổi, nhưng lock vẫn được giữ đến transaction end. Không mở transaction migration rồi chờ thao tác thủ công.

## 7. Thêm constraint hai bước

PostgreSQL cho phép thêm foreign key hoặc check constraint ở trạng thái `NOT VALID`: constraint áp cho rows mới/thay đổi nhưng chưa chứng nhận dữ liệu cũ. Sau remediation, `VALIDATE CONSTRAINT` quét dữ liệu hiện có với lock nhẹ hơn so với đường add-and-validate trực tiếp trong nhiều trường hợp.

Đây không phải “không khóa”. Add phase vẫn cần lock để sửa catalog; validation lấy lock và tiêu thụ I/O/CPU. Long transaction có thể làm lock acquisition chờ. Lab phải đo wait/hold time và traffic impact, không chỉ elapsed command.

Quy trình: precheck violations; add `NOT VALID` với lock timeout; theo dõi; backfill/quarantine; validate trong cửa sổ; xác nhận `convalidated`; giữ rollback/abort path. Với NOT NULL, có thể dùng validated check làm bằng chứng trước khi set not null theo behavior phiên bản.

## 8. UNIQUE, CHECK và FOREIGN KEY

UNIQUE xử lý concurrency tốt hơn precheck, nhưng PostgreSQL mặc định cho nhiều NULL vì NULL không bằng nhau; `NULLS NOT DISTINCT` nếu domain coi NULL là cùng một giá trị. Composite unique phải gồm tenant nếu identity scoped per tenant.

CHECK đánh giá TRUE hoặc NULL là pass; nếu NULL không hợp lệ, thêm NOT NULL hoặc điều kiện rõ. CHECK chỉ nên dựa row hiện tại và immutable logic; lookup bảng khác không được bảo đảm ổn định.

Foreign key bảo vệ referential integrity và có action delete/update. Child FK columns thường cần index để parent update/delete không scan child lớn; FK không tự tạo index phía referencing trong PostgreSQL.

## 9. View là truy vấn đặt tên

Regular view lưu định nghĩa, không lưu result. Khi query view, rule/rewrite system mở rộng view thành query tree rồi planner tối ưu tổng thể trong phạm vi cho phép. View không phải cache và không bảo đảm plan đơn giản.

View cung cấp abstraction, quyền truy cập và contract columns. Nhưng đổi type/meaning vẫn là contract change. `SELECT *` trong view làm ownership mờ; dùng column list và tests.

Updatable view có điều kiện và `WITH CHECK OPTION`; không suy rằng mọi view ghi được. Security-barrier/invoker semantics cần review riêng khi dùng làm boundary bảo mật.

## 10. Materialized view

Materialized view lưu result như relation và đọc nhanh hơn cho computation đắt, nhưng dữ liệu stale đến khi refresh. Nó là cache có source, refresh policy, freshness SLO, failure state, ownership và storage cost.

`REFRESH MATERIALIZED VIEW` thay nội dung; `CONCURRENTLY` giảm chặn readers nhưng có yêu cầu unique index thích hợp và trade-off. Không gọi concurrent refresh là miễn lock/tài nguyên. Refresh có thể tạo I/O, WAL và ảnh hưởng replicas.

Expose `last_successful_refresh`, source watermark và completeness. Consumer phải biết đang đọc snapshot nào.

## 11. View chồng nhiều tầng

Một tầng view hợp lý có thể chuẩn hóa contract. Nhiều tầng không owner tạo dependency graph khó truy, cột đổi nghĩa, predicate khó push, plan rất lớn và error khó quy source. Vấn đề không phải số ba kỳ diệu mà là không thấy lineage và grain.

Mỗi view cần owner, purpose, grain, source dependencies, freshness và consumers. Nếu logic trở thành model dùng chung, quản trị như code: version, tests, documentation, deprecation.

Không materialize chỉ để che query view rối. Sửa grain/logic trước, rồi benchmark materialization.

## 12. Expand–migrate–contract

Thay schema an toàn khi old/new application cùng chạy: expand bằng additive compatible structure; deploy writer dual/write hoặc backfill có kiểm soát; migrate/read switch; observe; contract xóa cũ sau khi không còn consumer.

Mỗi bước có rollback riêng. Backfill phải idempotent, batchable, resumable và có reconciliation. Dual-write có nguy cơ divergence nên cần owner và deadline; không để thành vĩnh viễn.

Destructive rename/drop trong một deployment thường phá rolling release. Dependency query và telemetry quyết định khi contract.

## 13. Lock budget và thí nghiệm năm triệu dòng

“Không khóa quá ngưỡng” cần số: lock acquisition < X ms, blocking sessions ≤ Y, p95 write latency tăng ≤ Z%, replication lag ≤ budget. Chọn ngưỡng theo SLO, không chép từ nguồn.

Lab tạo bảng năm triệu rows và concurrent workload kiểm soát. So add constraint trực tiếp với add NOT VALID + validate. Ghi PostgreSQL version, machine, table size, active workload, lock modes/waits, elapsed, CPU/I/O, errors và plan remediation.

Không suy kết quả lab thành production nếu scale/hardware/concurrency khác. Lab là bằng chứng cơ chế và phương pháp đo.

## 14. Five-run replay test

Seed source có duplicate business key và conflicting payload. Canonicalize hoặc cố ý bỏ để quan sát failure. Chạy write năm lần; sau mỗi lần ghi row count, unique business keys, payload checksum, audit rows và affected-row counts.

Pass khi state sau lần một đến năm giống theo contract, không duplicate và không side effect lặp ngoài policy. Nếu update timestamp mỗi retry, state không hoàn toàn idempotent; phải quyết định có chấp nhận.

Chạy thêm hai sessions đồng thời. Sequential replay không chứng minh concurrency safety.

## 15. Review checklist

Reviewer hỏi: invariant là gì; constraint nào enforce; NULL semantics; business key; source duplicate; affected-row guard; transaction boundary; lock mode/budget; rewrite/scan; replica/WAL; compatibility window; backfill/reconciliation; view grain; materialized freshness; rollback và observability.

Một migration “chạy xong” nhưng vượt latency SLO không đạt. Một MERGE không duplicate trên fixture sạch chưa đạt. Evidence phải chứa negative/concurrent cases.

## 16. Câu hỏi tự kiểm tra

1. Vì sao precheck rồi insert không thay unique constraint?
2. MERGE cần source uniqueness và target invariant nào?
3. `NOT VALID` và `VALIDATE` tách rủi ro ra sao?
4. CHECK gặp NULL có thể pass như thế nào?
5. View và materialized view khác storage/freshness ra sao?
6. Lock acquisition time khác lock hold time thế nào?

## 17. Giới hạn và điều chưa cho phép kết luận

- Lock behavior/cú pháp nêu theo PostgreSQL 17.10; DBMS khác phải tra manual.
- Không có ngưỡng lock phổ quát; SLO của hệ quyết định.
- `NOT VALID` không bảo đảm zero blocking hay zero scan.
- Replay tuần tự không chứng minh an toàn dưới concurrency.
- Lab năm triệu dòng chưa chạy; kết quả benchmark phải nằm trong `after-note.md`.

## Reference
1. [[SRC-POSTGRESQL-17-10-MANUAL]] — DDL/DML, constraints, views và materialized views.
2. [[SRC-MASTERING-POSTGRESQL-17-6E]] — transactional DDL, locks và runtime statistics.
3. [[SRC-POSTGRESQL-17-CONSTRAINTS]] — constraint semantics PostgreSQL 17.

## Source coverage

| Source slice | Nội dung phải giữ | Vị trí trong note | Trạng thái |
|---|---|---|---|
| [[SRC-POSTGRESQL-17-10-MANUAL]], PDF 97–117, 147–153, 1356–1368 | modifying tables, RETURNING, view/materialized view | §§2–12 | Đã giữ và giới hạn theo phiên bản |
| [[SRC-MASTERING-POSTGRESQL-17-6E]], PDF 49–62 | transactional DDL, lock modes | §§6–7, 13 | Đã nối với lock budget |
| [[SRC-POSTGRESQL-17-CONSTRAINTS]] | UNIQUE/CHECK/FK | §§1, 8 | Đã giữ NULL/concurrency caveat |
| Tổng hợp DE-L125 | replay, source duplicate, online migration evidence | §§13–15 | Đã thành lab kiểm được |

## Key takeaways
- Idempotency đến từ business key, constraint và side-effect contract; không đến từ tên lệnh.
- MERGE cần source unique/canonical và target invariant.
- Mọi DDL phải được đánh giá theo lock, scan/rewrite, compatibility và rollback.
- `NOT VALID`/`VALIDATE` giảm blast radius trong trường hợp phù hợp nhưng không phải zero-lock.
- Materialized view là cache có freshness SLO, không phải view “nhanh hơn” miễn phí.
