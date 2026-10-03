---
source_id: src.web.apache-druid-architecture
source_type: web-documentation
title: Apache Druid Architecture
publisher: Apache Software Foundation
canonical_url: https://druid.apache.org/docs/latest/design/architecture/
captured: 2026-10-01
status: active-public-source
rights: Apache-project-documentation
authority: official-project-documentation
tags: [source/web, druid, real-time-analytics, ingestion, segments]
---

# Apache Druid architecture — hồ sơ nguồn

## Phạm vi đã đọc

- Coordinator, Overlord, Broker, Router, Historical and ingestion services.
- Deep storage, local segment caches, metadata store and streaming ingestion/query flow.
- Segment/time pruning and broker merge path.

## Giới hạn

Druid is one real-time analytics design, not the definition of the archetype. Supported joins, updates, consistency and operations must be evaluated against the target version and workload.

## Note dẫn xuất

- [[Analytical Engine Selection ADR]]
