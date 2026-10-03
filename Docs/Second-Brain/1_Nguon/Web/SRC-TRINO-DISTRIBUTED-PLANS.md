---
source_id: src.web.trino-distributed-plans
source_type: web-documentation
title: Trino Concepts, Distributed EXPLAIN and Join Distribution
publisher: Trino Software Foundation
canonical_url: https://trino.io/docs/current/sql/explain.html
captured: 2026-10-01
status: active-public-source
rights: public-project-documentation
authority: official-product-documentation
tags: [source/web, trino, mpp, fragments, exchange, join-distribution]
---

# Trino distributed plans — hồ sơ nguồn

## Phạm vi đã đọc

- Concepts: coordinator, worker, stage, task, driver, operator, split và exchange.
- Distributed EXPLAIN: fragment boundaries và SINGLE, HASH, ROUND_ROBIN, BROADCAST, SOURCE distributions.
- Cost in EXPLAIN: estimated rows/bytes, CPU, memory, network và unknown estimates.
- Cost-based join distribution: partitioned và broadcast joins, build/probe sides và memory boundary.
- Web UI: task/stage statistics, blocked causes, skew và lack of parallelism.

## Giới hạn

Planner estimates không phải runtime measurements. Trino terms are implementation-specific; other MPP engines may call fragments stages, exchanges shuffles, and splits partitions. Lesson uses the concepts comparatively and requires actual counters before a scaling conclusion.

## Note dẫn xuất

- [[MPP Strong Scaling - MIMD SPMD Batch and SIMD]]
- [[Broadcast Repartition Skew and Spill]]
- [[Shared Nothing and Separated Storage Compute]]

- [[MPP - Coordinator Fragments and Exchange]]
