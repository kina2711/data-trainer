---
source_id: src.web.apache-iceberg-evolution
source_type: web-documentation
title: Apache Iceberg Evolution
publisher: Apache Software Foundation
canonical_url: https://iceberg.apache.org/docs/latest/evolution/
captured: 2026-10-02
status: active-public-source
rights: Apache-2.0-public-documentation
authority: official-project-documentation
tags: [source/web, iceberg, schema-evolution, partition-evolution, field-id]
---

# Apache Iceberg Evolution — hồ sơ nguồn

## Phạm vi đã đọc

- Schema add, drop, rename, widen và reorder as metadata changes.
- Correctness through field identity rather than name/position reuse.
- Partition evolution: old and new specs coexist; split planning applies the relevant transform per file/spec.
- Hidden partitioning and sort-order evolution.

## Giới hạn

Format-level evolution does not prove every engine/connector implements the same feature/version. Rename preserves field identity only when writers/readers and catalog maintain IDs. Business-semantic changes are outside schema evolution.

## Note dẫn xuất

- [[Iceberg Hidden Partition Schema and Field ID Evolution]]
