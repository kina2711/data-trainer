---
source_id: src.web.apache-iceberg-maintenance
source_type: web-documentation
title: Apache Iceberg Maintenance
publisher: Apache Software Foundation
canonical_url: https://iceberg.apache.org/docs/latest/maintenance/
captured: 2026-10-02
status: active-public-source
rights: Apache-2.0-public-documentation
authority: official-project-documentation
tags: [source/web, iceberg, compaction, snapshot-expiration, orphan-cleanup]
---

# Apache Iceberg Maintenance — hồ sơ nguồn

## Phạm vi đã đọc

- Snapshot expiration and its effect on time travel and unreferenced file deletion.
- Old metadata tracking and the distinction between tracked metadata and orphaned metadata.
- Orphan-file deletion warning: retention shorter than maximum write duration can corrupt a table.
- Data-file compaction, manifest rewrite, position-delete rewrite and dangling-delete cleanup.

## Giới hạn

Examples and defaults are version-specific. Retention must derive from real write/recovery/audit requirements. Maintenance success output does not prove no row loss; reconciliation and rollback/time-travel tests remain required.

## Note dẫn xuất

- [[Iceberg Maintenance Compaction Retention and Cleanup]]
- [[Gate 6 Metadata Concurrency Compatibility and Engine Evidence]]
