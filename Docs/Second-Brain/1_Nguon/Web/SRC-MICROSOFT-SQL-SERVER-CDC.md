---
source_id: src.web.microsoft-sql-server-cdc
source_type: web-documentation
title: SQL Server Change Data Capture
publisher: Microsoft
canonical_url: https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/about-change-data-capture-sql-server
captured: 2026-10-02
status: active-public-source
rights: public-vendor-documentation
authority: official-product-documentation
tags: [source/web, sql-server, cdc, lsn, insert, update, delete]
---

# SQL Server Change Data Capture — hồ sơ nguồn

## Phạm vi đã đọc

- Transaction-log capture of inserts, updates and deletes into change tables.
- Before/after update rows, operation codes, commit LSN and sequence ordering.
- Validity interval, retention cleanup, low/high endpoints and capture latency.
- Source DDL effects and capture-instance schema boundaries.

## Giới hạn

Đây là semantics của SQL Server CDC, không phải mọi CDC product. Hard delete visibility, ordering, retention, snapshot handoff và DDL behavior phải xác minh per source/version/configuration. Log availability does not prove downstream exactly-once application.

## Note dẫn xuất

- [[Source Change Semantics and Delete Visibility]]
- [[Extraction Pattern Decision Framework]]
- [[High Watermark Assumptions and Overlap Deduplication]]
