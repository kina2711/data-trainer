---
source_id: src.book.silberschatz-database-system-concepts.7e
source_type: textbook
title: Database System Concepts
authors: [Abraham Silberschatz, Henry F. Korth, S. Sudarshan]
publisher: McGraw-Hill Education
edition: seventh
published: 2020
captured: 2026-10-01
status: active-private-source
rights: copyrighted-private-owner-provided
sensitivity: private
authority: academic-secondary-source
sha256: 6757498cd254296fcdf24ef559b682308e7cb27bb332b8f8b6361b8c5baf6e46
canonical_path: /home/kina2711/PROJECT/data-trainer/Material/Reference_temp/Database_System_Concepts_-_Abraham_Silberschatz.pdf
extraction_method: pdftotext-layout-bounded-page-range
tags: [source/textbook, database-systems, lsm-tree, transactions, recovery]
---

# Database System Concepts 7e — hồ sơ nguồn

## Phạm vi đã đọc

- Chapter 17, transaction concept, ACID, transaction state và isolation: PDF 2144–2192.
- Chapter 19, recovery, WAL rule, checkpoint, redo/undo và group commit: PDF 2418–2462.
- Chapter 24, LSM tree variants, lookup/write costs và write amplification: PDF 2982–3002.
- Chapters 18 và 21, two-phase locking, deadlock detection/recovery, multiversion/snapshot isolation và data partitioning: PDF 2240–2292, 2338–2365, 2600–2635.
- Chapter 6, database design, conceptual/logical/physical design, entity, relationship, cardinality và identifier: PDF 871–920.
- Chapter 7, valid-time intervals, temporal keys/foreign keys và temporal joins: PDF 1144–1157.
- Chapter 11, warehouse schemas, fact/dimension, star/snowflake và columnar workload: PDF 1464–1478, 1565–1572.
- Chapter 15, external sort-merge, merge join, hash join, partitioning, memory boundary và I/O cost: PDF 1902–1955.
- Các phạm vi trên có text layer; locator dùng số trang PDF.

## Provenance và giới hạn

PDF do chủ dự án cung cấp, dùng nội bộ. Locator dùng số trang PDF vì số trang in và page object lệch lớn. Mô hình recovery trong giáo trình là mô hình tổng quát; không được gán nguyên xi cho PostgreSQL nếu manual và internals của PostgreSQL mô tả khác.

## Note dẫn xuất

- [[LSM Trees - Memtable SSTable and Compaction]]
- [[Read Write and Space Amplification]]
- [[Write-Ahead Log and Group Commit]]
- [[Crash Recovery Redo Undo and Checkpoints]]
- [[ACID and Transaction State Machine]]
- [[Locking, two-phase locking and deadlock detection]]
- [[MVCC, snapshots and vacuum]]
- [[Isolation levels chosen by anomaly, not by name]]
- [[Replication, lag, failover and split brain]]
- [[Partitioning against sharding]]
- [[Backup, PITR and what a backup is not]]
- [[The restore drill]]
- [[Operating a database day to day]]
- [[Gate 4 - trace a write and defend an isolation choice]]
- [[From requirement to model - the seven-step protocol]]
- [[Declaring the grain before the columns]]
- [[Conceptual, logical and physical models]]
- [[Keys - natural, surrogate and identity over time]]
- [[Dimensional modelling - facts, dimensions and the bus matrix]]
- [[Fact types - transaction, periodic and accumulating snapshot]]
- [[Additivity - additive, semi-additive and non-additive measures]]
- [[Dimension patterns - role-playing, junk, degenerate and bridge]]
- [[Slowly changing dimensions, type 0 to type 6]]
- [[Valid time, system time, corrections and restatement]]
- [[OLTP and OLAP - Workload Before Product Name]]
- [[Row and Column Layout - Isolating Physical Layout]]
