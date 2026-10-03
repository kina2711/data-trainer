---
source_id: src.web.postgresql-hot-standby
source_type: web-documentation
title: PostgreSQL Hot Standby
publisher: PostgreSQL Global Development Group
canonical_url: https://www.postgresql.org/docs/current/hot-standby.html
captured: 2026-10-02
status: active-public-source
rights: PostgreSQL-public-documentation
authority: official-product-documentation
tags: [source/web, postgresql, replica, lag, snapshot, extraction]
---

# PostgreSQL Hot Standby — hồ sơ nguồn

## Phạm vi đã đọc

- Read-only snapshots on standby and visibility after commit record replay.
- Measurable delay and possibly different results between primary and standby.
- WAL replay conflicts, query cancellation and lag/resource trade-offs.
- Snapshot/isolation and monitoring implications.

## Giới hạn

PostgreSQL semantics do not generalize to every replica system. Extraction must define a boundary available on the replica, measure replay position/lag and reconcile to that boundary. Reading a replica does not automatically offload all source impact or ensure freshness.

## Note dẫn xuất

- [[Database Snapshot Chunking and Replica Boundary]]
