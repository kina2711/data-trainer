---
source_id: src.book.rogov-postgresql-14-internals
source_type: book
title: PostgreSQL 14 Internals
authors: [Egor Rogov]
published: 2023
captured: 2026-09-29
status: active-private-source
rights: copyrighted-private-owner-provided
sensitivity: private
authority: technical-secondary-source
sha256: 0868e53b6fdca5352e725e453e3f58ce2114246a19239931de1615f60f418f51
canonical_path: /home/kina2711/PROJECT/data-trainer/Material/DE/Reference/Library/knowledge/postgresql/postgresql_internals-14_en.pdf
extraction_method: pdftotext-layout-bounded-page-range
tags: [source/book, postgresql, internals, statistics, index-scans, joins]
---

# PostgreSQL 14 Internals — hồ sơ nguồn

## Phạm vi đã đọc

- Chapter 17, basic/expression/multivariate statistics: PDF 271–303.
- Chapters 3–4, page layout, heap tuples và visibility: PDF 60–82.
- Chapter 9, shared/local buffer cache, clock sweep và dirty buffers: PDF 156–176.
- Chapter 20, regular/index-only/bitmap/parallel index scans và cost: PDF 330–349.
- Chapters 21–23, nested-loop, hash và merge join; so sánh join methods: PDF 350–407.
- Chapter 25, B-tree search, splits, metapage, deduplication và access properties: PDF 419–458.
- Chapters 10–11, WAL structure, checkpoint, crash recovery, background writing, synchronous/asynchronous commit và fault tolerance: PDF 164–196.
- Chapters 2–8, isolation/MVCC, row visibility, vacuum/autovacuum, freezing và bloat: PDF 37–141.
- Chapters 12–14, relation/row/predicate/advisory locks và lock waits: PDF 197–239.
- 228/228 trang trong các phạm vi có text layer.

## Provenance và giới hạn

PDF do chủ dự án cung cấp. Nội dung mô tả PostgreSQL 14, nên chi tiết có khả năng đổi được đối chiếu với manual PostgreSQL 17.10. Sách được dùng để giải thích cơ chế và cost reasoning; không biến ví dụ cost thành ngưỡng phổ quát.

## Note dẫn xuất

- [[Physical Operators and Join Algorithms]]
- [[Statistics Selectivity and Cardinality Estimation]]
- [[Index Structure Composite Order and Cost]]
- [[Reading EXPLAIN ANALYZE with Buffers]]
- [[Pages Heap Files and Buffer Pool]]
- [[B-tree Internals - Fanout Splits and Clustering]]
- [[Write-Ahead Log and Group Commit]]
- [[Crash Recovery Redo Undo and Checkpoints]]
- [[ACID and Transaction State Machine]]
- [[Locking, two-phase locking and deadlock detection]]
- [[MVCC, snapshots and vacuum]]
- [[Isolation levels chosen by anomaly, not by name]]
- [[Replication, lag, failover and split brain]]
- [[Backup, PITR and what a backup is not]]
- [[The restore drill]]
- [[Operating a database day to day]]
- [[Gate 4 - trace a write and defend an isolation choice]]
