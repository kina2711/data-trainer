---
source_id: src.book.kleppmann-ddia.1e
source_type: book
title: Designing Data-Intensive Applications
subtitle: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems
authors: [Martin Kleppmann]
publisher: O'Reilly Media
edition: first
published: 2017
captured: 2026-10-01
status: active-private-source
rights: copyrighted-private-owner-provided
sensitivity: private
authority: technical-secondary-source
sha256: 3480da3ae9a353067c574924e296bee55b63adfb4af43cbb852a98fdd91e0394
canonical_path: /home/kina2711/PROJECT/data-trainer/Material/DE/Reference/Library/book/Ôn DE/Designing Data-Intensive Applications.pdf
extraction_method: pdftotext-layout-bounded-page-range
tags: [source/book, data-systems, storage-engine, lsm-tree, sstable]
---

# Designing Data-Intensive Applications 1e — hồ sơ nguồn

## Phạm vi đã đọc

- Chapter 2, data models, query languages và ranh giới workload/representation: PDF 49–66.
- Chapter 3, append-only segments, compaction, SSTables, memtables, LSM trees, Bloom filters và so sánh B-tree/LSM-tree: PDF 94–106.
- Chapter 3, transaction processing so với analytics, data warehouse, column-oriented storage, compression, sort order và write path: PDF 113–123.
- Chapters 5–7, leader replication, replication lag, failover, partitioning/rebalancing và write skew: PDF 154–194, 220–239, 233–270.
- Các phạm vi trên có text layer; locator dùng số trang PDF.

## Provenance và giới hạn

PDF do chủ dự án cung cấp, dùng nội bộ. Đây là bản First Edition phát hành tháng 03-2017. Các mô tả engine cụ thể có thể đã thay đổi; note chỉ dùng cơ chế nền và luôn yêu cầu đo trên engine/phiên bản mục tiêu. Không tái phân phối PDF hoặc trích đoạn dài.

## Note dẫn xuất

- [[LSM Trees - Memtable SSTable and Compaction]]
- [[Read Write and Space Amplification]]
- [[Isolation levels chosen by anomaly, not by name]]
- [[Replication, lag, failover and split brain]]
- [[Partitioning against sharding]]
- [[Backup, PITR and what a backup is not]]
- [[The restore drill]]
- [[From requirement to model - the seven-step protocol]]
- [[Dimensional modelling - facts, dimensions and the bus matrix]]
- [[Fact types - transaction, periodic and accumulating snapshot]]
- [[Additivity - additive, semi-additive and non-additive measures]]
- [[OLTP and OLAP - Workload Before Product Name]]
- [[Row and Column Layout - Isolating Physical Layout]]
- [[Encoding and Compression - Choosing from Data Shape]]
- [[Vectorized Execution and Late Materialization]]
