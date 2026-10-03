---
source_id: src.spec.apache-iceberg-current
source_type: specification
title: Apache Iceberg Table Specification
publisher: Apache Software Foundation
canonical_url: https://iceberg.apache.org/spec/
captured: 2026-10-02
status: active-public-source
rights: Apache-2.0-public-specification
authority: official-table-format-specification
tags: [source/standard, iceberg, snapshot, manifest-list, manifest, optimistic-concurrency]
---

# Apache Iceberg Table Specification — hồ sơ nguồn

## Phạm vi đã đọc

- Serializable isolation goal, committed snapshots và atomic metadata-pointer swap.
- Metadata JSON, snapshots, manifest lists, manifests, data/delete files và statistics dùng cho scan planning.
- Writers tạo immutable files trước rồi công bố bằng commit; readers giữ snapshot đã load tới khi refresh.
- Optimistic concurrency, retry/validation conditions, field IDs, hidden partitioning, schema/partition evolution và object-store compatibility.

## Ranh giới diễn giải

Đặc tả mô tả contract của table format, không chứng minh catalog/engine cụ thể cấu hình đúng, không thay thế permission, cleanup, compaction hay operational recovery. Từ “ACID” không được dùng thay cho việc nêu rõ snapshot isolation, atomic visibility, conflict validation và recovery boundary.

## Note dẫn xuất

- [[Object Store File Format and Table Format Boundaries]]
- [[Iceberg Metadata Tree and Snapshot Lineage]]
