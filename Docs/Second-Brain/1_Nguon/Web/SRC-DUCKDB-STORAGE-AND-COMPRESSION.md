---
source_id: src.web.duckdb-storage-compression
source_type: web-documentation
title: DuckDB Storage Format and Lightweight Compression
publisher: DuckDB Foundation
canonical_url: https://duckdb.org/docs/stable/internals/storage
captured: 2026-10-01
status: active-public-source
rights: public-web-documentation
authority: official-product-documentation
tags: [source/web, duckdb, storage, row-groups, compression]
---

# DuckDB storage and compression — hồ sơ nguồn

## Phạm vi đã đọc

- Storage-format documentation: row groups, persistence boundary, storage-version compatibility và danh sách compression algorithms.
- `PRAGMA storage_info`: column segment, compression, statistics, update và persistence fields dùng để quan sát lựa chọn vật lý.
- Lightweight Compression article ngày 2022-10-28: algorithm selection theo pattern dữ liệu, row group/column segment và quan hệ giữa giảm byte với CPU.

## Giới hạn

Danh sách thuật toán và storage version thay đổi theo phiên bản. DuckDB được dùng làm engine quan sát trong lab, không đại diện cho mọi column store. Con số compression trong bài viết của dự án là ví dụ theo workload, không phải cam kết tỷ lệ cho dữ liệu khác.

## Note dẫn xuất

- [[Row and Column Layout - Isolating Physical Layout]]
- [[Encoding and Compression - Choosing from Data Shape]]
- [[Analytical Engine Selection ADR]]
