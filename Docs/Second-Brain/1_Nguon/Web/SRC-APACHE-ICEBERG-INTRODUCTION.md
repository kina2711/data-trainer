---
source_id: src.web.apache-iceberg-introduction
source_type: web-documentation
title: Apache Iceberg Introduction
publisher: Apache Software Foundation
canonical_url: https://iceberg.apache.org/docs/latest/
captured: 2026-10-01
status: active-public-source
rights: Apache-project-documentation
authority: official-project-documentation
tags: [source/web, iceberg, open-table-format, lakehouse, evolution]
---

# Apache Iceberg introduction — hồ sơ nguồn

## Phạm vi đã đọc

- Open table format shared by multiple compute engines.
- Snapshot/time travel, schema evolution, hidden partitioning and partition evolution.
- Metadata/table-format boundary distinct from execution engine and platform operation.

## Giới hạn

Iceberg is a table format, not a complete lakehouse engine or managed platform. Selecting it does not resolve catalog, compute, compaction, security or operations by itself.

## Note dẫn xuất

- [[Analytical Engine Selection ADR]]
- [[Object Store File Format and Table Format Boundaries]]
- [[Iceberg Metadata Tree and Snapshot Lineage]]
