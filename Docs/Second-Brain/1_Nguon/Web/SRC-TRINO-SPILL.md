---
source_id: src.web.trino-spill
source_type: web-documentation
title: Trino Spill to Disk
publisher: Trino Software Foundation
canonical_url: https://trino.io/docs/current/admin/spill.html
captured: 2026-10-01
status: active-public-source
rights: public-project-documentation
authority: official-product-documentation
tags: [source/web, trino, memory, spill, join, aggregation]
---

# Trino spill — hồ sơ nguồn

## Phạm vi đã đọc

- Revocable memory, memory limits và spill lifecycle cho join, aggregation, sort và window operators.
- Peak-memory reduction, partitioned build side, spill write/read, disk saturation, compression và encryption trade-off.
- Tài liệu hiện đánh dấu spill implementation là legacy và nêu fault-tolerant execution như hướng thay thế trong một số deployment.

## Giới hạn

Spill là cơ chế sống sót có phạm vi operator cụ thể, không bảo đảm mọi query vượt memory sẽ hoàn tất. Mức chậm phụ thuộc bytes, device, compression, encryption, reuse và concurrency; note không dùng một hệ số cố định.

## Note dẫn xuất

- [[Broadcast Repartition Skew and Spill]]
