---
source_id: src.web.trino-dynamic-filtering
source_type: web-documentation
title: Trino Dynamic Filtering
publisher: Trino Software Foundation
canonical_url: https://trino.io/docs/current/admin/dynamic-filtering.html
captured: 2026-10-01
status: active-public-source
rights: public-project-documentation
authority: official-product-documentation
tags: [source/web, trino, dynamic-filtering, pruning, joins]
---

# Trino dynamic filtering — hồ sơ nguồn

## Phạm vi đã đọc

- Planner, connector và storage-reader conditions để dynamic filter được đẩy xuống scan.
- Distinct-values và min/max representations cùng collection thresholds.
- EXPLAIN/EXPLAIN ANALYZE và QueryInfo statistics dùng để quan sát filter.
- CPU overhead và build-side size boundary.

## Giới hạn

Dynamic filtering là runtime join-derived pruning, khác static partition/row-group statistics. Planner annotation không chứng minh connector đã bỏ splits hoặc reader đã bỏ row groups; cần runtime counters và connector support.

## Note dẫn xuất

- [[Zone Maps Statistics and Pruning]]
