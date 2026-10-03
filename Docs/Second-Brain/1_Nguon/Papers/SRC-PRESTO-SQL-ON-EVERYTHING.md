---
source_id: src.paper.presto-sql-on-everything
source_type: research-paper
title: Presto - SQL on Everything
authors: [Raghav Sethi, Martin Traverso, Dain Sundstrom, David Phillips, Wenlei Xie, Yutian Sun, Nezih Yigitbasi, Haozhun Jin, Eric Hwang, Nileema Shingte, Christopher Berner]
canonical_url: https://trino.io/Presto_SQL_on_Everything.pdf
captured: 2026-10-01
status: active-public-source
rights: public-research-paper
authority: primary-system-paper
tags: [source/paper, presto, distributed-query, exchange, small-files]
---

# Presto: SQL on Everything — hồ sơ nguồn

## Phạm vi đã đọc

- Query execution: stages, tasks, drivers, buffered exchanges và distributed planning.
- Connector/split model và physical layout properties.
- Co-located joins, shuffle avoidance và partition skew trade-off.
- File enumeration/small-file overhead trong object-storage workloads.

## Giới hạn

Paper mô tả hệ tại thời điểm công bố và không thay documentation hiện hành của Trino. Thuật ngữ, optimizer và fault-tolerant execution đã phát triển. Các claims hiệu năng được giữ trong bối cảnh hệ và workload của paper.

## Note dẫn xuất

- [[MPP Strong Scaling - MIMD SPMD Batch and SIMD]]
- [[Shared Nothing and Separated Storage Compute]]
- [[Partitioning Clustering and Sort Order]]
- [[MPP - Coordinator Fragments and Exchange]]
- [[Analytical Engine Selection ADR]]
