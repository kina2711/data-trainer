---
source_id: src.book.petrov-database-internals.1e
source_type: book
title: Database Internals
subtitle: A Deep Dive into How Distributed Data Systems Work
authors: [Alex Petrov]
publisher: O'Reilly Media
edition: first
published: 2019
captured: 2026-10-01
status: active-private-source
rights: copyrighted-private-owner-provided
sensitivity: private
authority: technical-secondary-source
sha256: 0f23c5ecaffde9fdbc6e69f315c48f943429b0aa7e3ec2e92955f18ad353829f
canonical_path: /home/kina2711/PROJECT/data-trainer/Material/Reference_temp/Database_Internals_-_Alex_Petrov.pdf
extraction_method: pdftotext-layout-bounded-page-range
tags: [source/book, database-internals, storage-engine, lsm-tree, wal, recovery]
---

# Database Internals — hồ sơ nguồn

## Phạm vi đã đọc

- Chapter 5, recovery, WAL semantics, checkpoints, steal/force, ARIES và transaction isolation: PDF 117–130.
- Chapter 5, concurrency control, serializability, anomalies, snapshot isolation, MVCC và deadlock: PDF 124–145.
- Chapter 7, LSM tree, memtable, immutable disk tables, tombstone, lookup, compaction, amplification, Bloom filter và log stacking: PDF 167–210.
- 58/58 trang trong các phạm vi có text layer.

## Provenance và giới hạn

PDF do chủ dự án cung cấp, dùng nội bộ. Sách giải thích các mô hình storage/recovery tổng quát; chi tiết PostgreSQL được đối chiếu với manual PostgreSQL 17.10 và *PostgreSQL 14 Internals*. Không sao chép đoạn dài hoặc tái phân phối PDF.

## Note dẫn xuất

- [[LSM Trees - Memtable SSTable and Compaction]]
- [[Read Write and Space Amplification]]
- [[Write-Ahead Log and Group Commit]]
- [[Crash Recovery Redo Undo and Checkpoints]]
- [[ACID and Transaction State Machine]]
- [[Locking, two-phase locking and deadlock detection]]
- [[MVCC, snapshots and vacuum]]
- [[Isolation levels chosen by anomaly, not by name]]
- [[Partitioning against sharding]]
