---
source_id: src.manual.postgresql-17.10
source_type: official-manual
title: PostgreSQL 17.10 Documentation
authors: [PostgreSQL Global Development Group]
published: 2026-05-12
captured: 2026-09-29
status: active-local-source
rights: public-documentation
sensitivity: public
authority: official-primary-documentation
sha256: 373847948d91630e85dfd80d54a9929920e666575a4a2a276e081480fd0b4ff1
canonical_path: /home/kina2711/PROJECT/data-trainer/Material/DE/Reference/Library/knowledge/postgresql/postgresql-17-docs.pdf
extraction_method: pdftotext-layout-bounded-page-range
tags: [source/manual, postgresql-17, ddl, planner, statistics, indexes]
---

# PostgreSQL 17.10 Documentation — hồ sơ nguồn

## Phạm vi đã đọc

- DDL constraints và modifying tables: PDF 97–117.
- DML `RETURNING` và related statements: PDF 147–153; `MERGE` command được đối chiếu tại phần SQL Commands.
- Multicolumn, expression, partial và index-only indexes: PDF 488–498.
- `EXPLAIN`, planner statistics và planner control: PDF 559–580.
- Prepared statements, generic/custom plans và `plan_cache_mode`: PDF 2018–2030.
- Views/materialized views: PDF 1356–1368.
- Query path và overview internals: PDF 2341–2347.
- Database page layout và HOT: PDF 2623–2630.
- Multivariate statistics examples: PDF 2643–2650.
- `pageinspect` và `pg_buffercache`: PDF 2888–2910.
- MVCC và transaction isolation: PDF 543–550.
- Table partitioning và pruning: PDF 134–147.
- Transaction isolation, explicit locks, deadlocks và consistency checks: PDF 543–555.
- Routine vacuuming, autovacuum và wraparound prevention: PDF 808–823.
- WAL shipping, streaming và synchronous replication: PDF 830–850.
- Backup/restore, continuous archiving, PITR và backup manifest: PDF 820–857.
- Monitoring database activity, progress, statistics, locks và disk usage: PDF 858–920.
- Reliability, WAL, asynchronous commit, checkpoint configuration, group commit và recovery internals: PDF 918–926.

## Giới hạn

Đây là manual PostgreSQL 17.10. Các khái niệm SQL chung vẫn cần kiểm dialect khi chuyển DBMS. Cost constants và `work_mem` là tham số mô hình/vận hành, không phải benchmark mặc định cho mọi máy.

## Note dẫn xuất

- [[DML DDL Constraints and Views]]
- [[Inside the Engine - Parser to Executor]]
- [[Physical Operators and Join Algorithms]]
- [[Statistics Selectivity and Cardinality Estimation]]
- [[Index Structure Composite Order and Cost]]
- [[Reading EXPLAIN ANALYZE with Buffers]]
- [[Sargability Parameters and Plan Stability]]
- [[SQL Tuning Project - Five Slow Queries]]
- [[Pages Heap Files and Buffer Pool]]
- [[B-tree Internals - Fanout Splits and Clustering]]
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
