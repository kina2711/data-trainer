---
source_id: src.web.airbyte-incremental-append-deduped
source_type: web-documentation
title: Airbyte Incremental Append and Deduped
publisher: Airbyte
canonical_url: https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes/incremental-append-deduped
captured: 2026-10-02
status: active-public-source
rights: public-vendor-documentation
authority: official-product-documentation
tags: [source/web, ingestion, cursor, primary-key, deduplication]
---

# Airbyte Incremental Append and Deduped — hồ sơ nguồn

## Phạm vi đã đọc

- Cursor and primary-key roles in incremental append/deduped.
- History table versus final deduplicated table.
- Inclusive cursor and at-least-once preference at ambiguous boundaries.
- Known limitation when records change without cursor update.

## Giới hạn

Vendor sync mode is one implementation example. It does not make an arbitrary timestamp reliable, expose hard deletes unless the source emits them, or prove completeness. Cursor, key, delete semantics and reconciliation remain source contracts.

## Note dẫn xuất

- [[Extraction Pattern Decision Framework]]
- [[High Watermark Assumptions and Overlap Deduplication]]
