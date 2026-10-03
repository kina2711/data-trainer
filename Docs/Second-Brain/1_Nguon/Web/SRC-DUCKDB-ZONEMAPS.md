---
source_id: src.web.duckdb-zonemaps
source_type: web-documentation
title: DuckDB Zonemaps and Ordering
publisher: DuckDB Foundation
canonical_url: https://duckdb.org/docs/stable/guides/performance/indexing
captured: 2026-10-01
status: active-public-source
rights: public-web-documentation
authority: official-product-documentation
tags: [source/web, duckdb, zonemap, min-max, pruning]
---

# DuckDB zonemaps — hồ sơ nguồn

## Phạm vi đã đọc

- Min-max index/zonemap theo row group và ví dụ bỏ qua range không thể chứa filter value.
- Tác động của ordering/correlation lên độ chọn lọc của zonemap.
- Quan hệ với predicate pushdown và row-group scan.

## Giới hạn

DuckDB tự tạo zonemap nhưng exact plan/profile counters và supported predicates thay đổi theo version/type. Min/max có thể tạo false positives và đọc block không chứa match; nó không được phép tạo false negative nếu metadata và comparison semantics hợp lệ.

## Note dẫn xuất

- [[Zone Maps Statistics and Pruning]]
- [[Parquet Statistics and Pushdown Evidence]]
