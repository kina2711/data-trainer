---
source_id: src.web.trino-join-distribution
source_type: web-documentation
title: Trino Join Distribution and Cost-Based Optimizations
publisher: Trino Software Foundation
canonical_url: https://trino.io/docs/current/optimizer/cost-based-optimizations.html
captured: 2026-10-01
status: active-public-source
rights: public-project-documentation
authority: official-product-documentation
tags: [source/web, trino, broadcast-join, partitioned-join, statistics]
---

# Trino join distribution — hồ sơ nguồn

## Phạm vi đã đọc

- Broadcast và partitioned hash join, build/probe side, memory consequence trên từng worker.
- Automatic strategy, connector-provided statistics, join enumeration và broadcast-size cap.
- Hành vi fallback khi cost hoặc statistics không khả dụng.

## Giới hạn

Ngưỡng mặc định và behavior có thể đổi theo phiên bản. Broadcast nhanh hơn chỉ dưới data shape, memory, concurrency và network phù hợp; plan label chưa chứng minh actual bytes, memory hoặc absence of spill.

## Note dẫn xuất

- [[Broadcast Repartition Skew and Spill]]
