# L176–L180 release audit

## Phạm vi

- L176: query compilation internals.
- L177: definition and static tests.
- L178: independent reconciliation and regression.
- L179: serving, caching and performance.
- L180: semantic-layer access control.

## Kiểm tra đã chạy

- Generator check: `checked=20 stale=0`.
- Batch validator: `PASS lessons=5 curriculum_files=10 knowledge_notes=5 min_words=2200 wiki_parity=5/5`.
- Formatter: `checked=274 failed=0`.
- Whole-vault coverage: `checked=103 failed=0`.
- Word counts của năm knowledge notes: 2750, 2604, 2607, 2438, 2581.

## Ranh giới học thuật đã giữ

- Metric dependency graph phải acyclic; entity relationship graph có cycle không tự động sai, nhưng ambiguous path phải được qualification hoặc reject.
- 18 reconciliation cells của L178 chứa năm metric assertions mỗi cell, tức 90 comparisons.
- Pre-aggregation ngây thơ chỉ an toàn cho fully additive roll-up; non-additive metric cần mergeable state/operator contract.
- PostgreSQL RLS thường lọc dòng không thỏa policy; explicit request rejection là contract khác ở semantic/API boundary.
- Minimum group size không đủ chặn differencing và repeated-query inference.
- dbt declarative cache hiện hành không tự áp security context lên cached table ở query time; cache isolation phải được thiết kế và test riêng.

## Chưa kiểm bằng thực thi

- Chưa chạy MetricFlow/dbt trong môi trường đã pin version.
- Chưa chạy 18-cell × 5-metric reconciliation fixture.
- Chưa benchmark 20-query workload hoặc đo p95/cost/freshness.
- Chưa chạy sáu access-control negative tests hay penetration test.
- Chưa có owner approval cho semantic meaning; artifacts giữ trạng thái `review`.
