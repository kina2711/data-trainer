# Phase 4: SQL and Database Internals
# Module 9: Relational Theory and SQL Execution
# Lesson 131: Sargability, parameters and plan stability

## Mục tiêu bài học

**Năng lực cần chứng minh.** Nhận ra ba cách phá chỉ mục trong truy vấn cho trước và tái hiện được hiện tượng kế hoạch bị đóng băng theo tham số.

**Điều kiện hoàn thành.** Tìm đúng ≥ 5/6 chỗ phá chỉ mục và sửa được, và tái hiện được hiện tượng kế hoạch xấu theo tham số với số đo chênh lệch.

> [!abstract] Câu hỏi trung tâm
> Predicate có thể biến thành index condition không, tham số giữ được an toàn và type semantics không, và generic/custom plan được chọn thế nào trên distribution lệch?

## 1. Sargability là khả năng tạo search condition

Sargable predicate cho phép optimizer biến điều kiện thành boundary/lookup trên access path thay vì đọc rows rồi áp filter. Đây không phải thuộc tính nhị phân của SQL text tách khỏi index/opclass/type/collation; cùng predicate có thể sargable với một index nhưng không với index khác.

Trong plan, tìm `Index Cond` thay vì chỉ `Filter`. Query dùng index nhưng predicate chính ở Filter vẫn có thể fetch nhiều rows. Seq scan không tự chứng minh non-sargable; planner có thể chọn seq scan vì selectivity/cost.

Sửa sargability phải giữ semantics, đặc biệt timezone, collation, NULL và boundary.

## 2. Hàm bọc quanh cột

`lower(email)=lower($1)` không dùng plain B-tree trên `email` như equality key; lựa chọn gồm expression index trên `lower(email)`, normalized stored column hoặc domain-specific type/collation. Rewrite chỉ bỏ lower nếu case-sensitive semantics chấp nhận.

`date(created_at)=DATE '2026-10-01'` nên chuyển thành half-open range trên timestamp theo timezone nghiệp vụ. `created_at >= start AND created_at < next_start` dùng range index và tránh end-of-day precision bugs.

Không tạo expression index cho mọi function. Đo query frequency/write cost và volatility rules.

## 3. Arithmetic và transforms

`price * 1.1 > 100` có thể biến algebraically thành `price > 100/1.1` nếu numeric semantics, rounding, overflow và NULL giữ nguyên. Function monotonic/invertible quyết định rewrite an toàn.

`coalesce(column, sentinel)=...` đổi NULL semantics và cản plain index. Viết explicit branches hoặc expression index nếu business rule thật sự dùng sentinel.

Không tối ưu bằng biến đổi làm khác kiểu dữ liệu/precision.

## 4. Ép kiểu ngầm

Parameter/column types ảnh hưởng operator resolution và index opclass. Cast cột sang text để so parameter làm engine transform mọi row; cast parameter sang column type thường tốt hơn, nhưng invalid input/error semantics khác.

Driver gửi unknown/text/numeric types có thể tạo plan/operator khác. Ghi prepared parameter types và EXPLAIN EXECUTE. Cross-type operators đôi khi vẫn dùng index; không dùng khẩu quyết tuyệt đối.

Schema types phải khớp domain giữa join keys. Cast trong join trên cả bảng là smell và có thể làm estimate sai.

## 5. Pattern matching

`LIKE 'prefix%'` có thể dùng B-tree với collation/opclass phù hợp; `LIKE '%term'` không có fixed leading prefix nên plain B-tree thường không giới hạn scan. Trigram/GIN, full-text hoặc reverse-expression index tùy requirement.

Case-insensitive search có `lower` expression/trigram/citext trade-offs. Leading wildcard không “sửa” bằng bỏ wildcard nếu semantics cần substring.

Test selectivity, locale/collation và pattern classes. Một index tốt prefix không tốt contains.

## 6. OR, NOT và NULL

`OR` có thể dùng bitmap OR/multiple indexes, nhưng complex branches/low selectivity có thể seq scan. Rewrite UNION ALL phải xử lý overlap/duplicates đúng. `NOT` thường chọn phần lớn rows, nên index ít lợi.

`IS NULL` có thể dùng index; partial index cho rare NULL/status subset có thể phù hợp. `NOT IN` có NULL semantics riêng, không phải sargability đơn thuần.

Không đánh đổi correctness để có Index Cond.

## 7. Parameterization và injection

Parameters tách values khỏi SQL structure, tránh parser coi input là code và hỗ trợ plan reuse. Đây là kiểm soát bảo mật bắt buộc cho values. Identifier/order direction không parameterize như values; dùng allowlist/composition API.

Không ghép chuỗi literal để “có plan tốt hơn”. Nếu specialization cần, dùng supported plan controls/query variants với allowlist và tests, vẫn bind values.

Parameterization còn chuẩn hóa query logs/fingerprints, nhưng phải giữ parameter classes cho performance diagnosis.

## 8. PostgreSQL custom và generic plans

Prepared statement có thể dùng custom plan cho execution cụ thể hoặc generic plan dùng chung. Ở `plan_cache_mode=auto`, PostgreSQL 17 thực hiện năm executions đầu bằng custom plans, tính average estimated cost, rồi so generic estimated cost; subsequent có thể dùng generic nếu không cao đáng kể.

Đây không phải cơ chế “plan đóng băng theo giá trị đầu tiên” như cách mô tả parameter sniffing ở một số DBMS. Giá trị đầu ảnh hưởng custom execution đó; heuristic xem năm executions, không cache nguyên plan đầu tiên làm default.

Generic plan hiển thị `$n`; custom plan substitues values trong EXPLAIN EXECUTE. Session scope/driver behavior/pool preparation phải ghi.

## 9. Dữ liệu lệch và plan classes

Hot value trả hàng triệu rows có thể cần seq/hash; rare value có thể cần index/nested loop. Một generic plan tối ưu trung bình có thể xấu ở tail. Custom plan dùng parameter stats nhưng trả planning overhead mỗi execution.

Tạo parameter classes: hot, cold, absent, NULL/boundary. Đo latency/work/plans từng class. Không chỉ chạy rare trước rồi popular sau và gọi plan đầu bị đóng băng; phải xác nhận generic/custom bằng EXPLAIN EXECUTE/plan_cache_mode.

Nếu app/driver dùng unnamed statements hoặc client-side prepare, behavior khác. Inspect thực tế.

## 10. Ba cách xử lý generic-plan mismatch

Một: sửa statistics/extended statistics và indexes/query để generic plan đủ tốt. Hai: force/custom plan ở session/transaction/query path có kiểm soát khi execution benefit vượt planning cost. Ba: tách query variants theo parameter class/domain rule, vẫn parameterized và có routing tests.

`force_custom_plan`/`force_generic_plan` chủ yếu là diagnostic hoặc scoped control, không global reflex. Reprepare/deallocate có thể reset nhưng không sửa root cause.

Một phương án khác là avoid server prepare cho query nhạy, tùy driver; đánh đổi planning overhead.

## 11. Plan invalidation và replanning

Prepared statements được re-analyze/replanned khi referenced objects undergo DDL changes hoặc planner statistics update theo documented behavior. Search_path changes cũng có effects. Plan không phải immutable suốt session.

Statistics refresh, schema/index, config, PostgreSQL upgrade, extension/collation và data volume có thể đổi plan. Đây là tính năng cost optimizer thích nghi, đồng thời là change risk.

Không đặt mục tiêu plan shape không bao giờ đổi. Đặt SLO/result invariants và representative plan tests.

## 12. Plan stability

Ổn định nghĩa tail latency trong budget trên parameter classes và changes, không phải lock plan node names. Lưu baseline JSON plans, dataset stats, settings và timings; compare sau ANALYZE/deploy/upgrade.

Plan regression gate không nên fail mọi plan diff. Fail khi result đổi, SLO/work budgets vượt hoặc critical evidence xấu. Alternative plan có thể tốt hơn.

Rollback gồm revert stats target/index/query/config; có plan for reanalyze/reprepare.

## 13. Sáu non-sargable fixtures

Phủ function on column; timestamp date cast; implicit/cross type cast; leading wildcard; arithmetic transform; optional-filter pattern như `col = COALESCE($1,col)` hoặc OR parameter làm generic estimate khó. Mỗi fixture có old/new semantics tests, plan và buffers.

Một số fix dùng expression/partial/trigram index thay rewrite. Rubric yêu cầu giải thích access path, không chỉ “Index Scan xuất hiện”.

Test NULL, timezone boundary, collation và invalid inputs.

## 14. Prepared-plan experiment đúng

Tạo skewed table, ANALYZE và index. PREPARE typed statement. Chạy ít nhất năm+ executions với sequence được ghi, dùng `EXPLAIN (ANALYZE, BUFFERS) EXECUTE`, phân biệt custom/generic qua constants vs `$1`. So auto, force_custom và force_generic trong session-local settings.

Đo planning/execution distribution cho hot/cold. Result phải bằng. Không tuyên bố first-value freeze nếu actual plan history không chứng minh.

Lặp với driver/app mode nếu mục tiêu production, vì SQL PREPARE experiment không đại diện mọi driver.

## 15. Sửa một biến

Baseline query/index/stats. Viết hypothesis: “function prevents index condition”; predicted observation: rewrite/expression index chuyển filter thành Index Cond và giảm buffers. Thay một thứ, rerun parity/plan/work/latency.

Với generic mismatch, không đồng thời tăng stats, thêm index và force custom. Nếu sửa nhiều, không biết causal.

Giữ failed hypotheses trong ledger để tránh lặp.

## 15.1. Trường hợp optional filters

API search thường viết một statement kiểu `($1 IS NULL OR tenant_id = $1) AND ($2 IS NULL OR status = $2)`. Nó tiện tái sử dụng nhưng generic plan phải phục vụ nhiều hình dạng: không filter, một filter, hai filters, hot status và cold status. Estimates/access paths có thể kém dù từng branch riêng sargable. Việc ghép literal động không phải câu trả lời vì mở injection/plan churn.

Thiết kế có thể dùng một tập query variants hữu hạn theo filter presence, mỗi variant vẫn bind values; hoặc custom plans cho endpoint có execution đủ đắt; hoặc indexes/statistics giúp generic plan. Router variants phải allowlist structure và test mọi combination. Đo planning overhead, query frequency và tail latency. Result parity phải gồm NULL parameter semantics; `col = COALESCE($1,col)` làm rows có `col IS NULL` hành xử khác khi `$1` NULL, nên không được coi là rewrite tương đương mặc định. Đây là ví dụ sargability, NULL logic, security và plan caching phải được giải cùng nhau.

Một bộ kiểm thử tối thiểu phải có bốn lớp bằng chứng: truth table cho từng tổ hợp tham số; `EXPLAIN (ANALYZE, BUFFERS)` cho hot, cold và không lọc; phân phối latency gồm planning time; và số lượng statement variants thực sự tồn tại trong pool. Nếu tách quá nhiều variants, chi phí vận hành chuyển thành plan-cache churn và khó quan sát. Nếu giữ một statement duy nhất, chi phí có thể chuyển thành generic-plan compromise. Quyết định phải dựa trên tần suất từng lớp tham số và ngân sách tail latency, không dựa trên sở thích cú pháp.

## 16. Câu hỏi tự kiểm tra

1. Index Cond khác Filter thế nào?
2. Vì sao date(timestamp)=date rewrite cần timezone/half-open range?
3. PostgreSQL auto generic/custom heuristic dùng năm executions ra sao?
4. Vì sao gọi “plan theo giá trị đầu tiên” là sai mô hình PostgreSQL 17?
5. Parameterization và plan specialization có thể cùng tồn tại thế nào?
6. Plan stability nên đo SLO hay node names?

## 17. Giới hạn và điều chưa cho phép kết luận

- Sargability phụ thuộc access method, opclass, type/collation và workload.
- Driver/pool preparation behavior có thể khác SQL PREPARE trực tiếp.
- Generic/custom heuristic là PostgreSQL 17-specific và có thể đổi phiên bản.
- Plan shape change không tự là regression.
- Sáu query và skew experiment chưa chạy; evidence thuộc `after-note.md`.

## Reference
1. [[SRC-POSTGRESQL-17-10-MANUAL]] — PREPARE, generic/custom plans, EXPLAIN và indexes.
2. [[SRC-MASTERING-POSTGRESQL-17-6E]] — functional indexes, cost và plan behavior.

## Source coverage

| Source slice | Nội dung phải giữ | Vị trí trong note | Trạng thái |
|---|---|---|---|
| [[SRC-POSTGRESQL-17-10-MANUAL]], PDF 488–498, 559–580, 2018–2030 | expression indexes, plans, PREPARE heuristic | §§1–14 | Đã sửa first-value misconception |
| [[SRC-MASTERING-POSTGRESQL-17-6E]], PDF 87–112, 223–270 | functions/indexes/cost/plans | §§2–15 | Đã gắn workload evidence |
| Tổng hợp DE-L131 | six fixtures và hot/cold experiment | §§13–15 | Đã thành protocol tái hiện |

## Key takeaways
- Sargability được xác nhận qua access condition và reduced work, không chỉ node name.
- Parameterization là kiểm soát injection; không bỏ để đổi plan.
- PostgreSQL 17 chọn custom/generic theo heuristic, không đơn giản cache plan của giá trị đầu.
- Dữ liệu lệch cần parameter classes và tail measurement.
- Plan stability là ổn định correctness/SLO, không phải bất biến plan shape.
