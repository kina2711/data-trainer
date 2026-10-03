---
source_id: src.web.duckdb-parquet-pushdown
source_type: web-documentation
title: DuckDB Reading and Writing Parquet Files
publisher: DuckDB Foundation
canonical_url: https://duckdb.org/docs/stable/data/parquet/overview
captured: 2026-10-01
status: active-public-source
rights: public-web-documentation
authority: official-product-documentation
tags: [source/web, duckdb, parquet, projection-pushdown, filter-pushdown]
---

# DuckDB Parquet pushdown — hồ sơ nguồn

## Phạm vi đã đọc

- Partial reading: projection pushdown chỉ đọc các cột cần cho truy vấn.
- Filter pushdown và khả năng bỏ qua phần tệp qua statistics/zonemaps khi metadata cho phép.
- Parquet tips: row group gồm column chunks, ảnh hưởng của row-group size tới compression, parallelism, metadata overhead và pruning.

## Giới hạn

Projection pushdown và filter pruning là hai cơ chế khác nhau. Bytes engine báo, bytes storage backend truyền và kích thước logic của cột có thể khác nhau vì metadata, page boundaries, cache, prefetch và instrumentation. Lab phải khóa version, cache state và metric definition.

## Note dẫn xuất

- [[Row and Column Layout - Isolating Physical Layout]]
- [[Zone Maps Statistics and Pruning]]
- [[Partitioning Clustering and Sort Order]]
- [[Parquet File Row Group Column Chunk and Page]]
- [[Parquet Statistics and Pushdown Evidence]]
