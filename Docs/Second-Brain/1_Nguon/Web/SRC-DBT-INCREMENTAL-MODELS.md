---
source_id: src.web.dbt-incremental-models
source_type: web-documentation
title: Configure Incremental Models
publisher: dbt Labs
canonical_url: https://docs.getdbt.com/docs/build/incremental-models
captured: 2026-10-02
status: active-public-source
rights: public-vendor-documentation
authority: official-product-documentation
tags: [source/web, dbt, incremental, merge, unique-key]
---

# Configure Incremental Models — hồ sơ nguồn

## Phạm vi đã đọc

- `is_incremental()` và điều kiện để incremental branch chạy.
- `unique_key` cho cập nhật thay vì append-only, cùng giới hạn khi key không duy nhất.
- Các chiến lược append, delete+insert, merge, insert_overwrite và microbatch phụ thuộc adapter.
- Giới hạn scan bằng incremental predicates và yêu cầu lọc sớm để giảm compute.
- Full refresh là đường tái dựng khi logic hoặc lịch sử không còn tương thích.

## Giới hạn

dbt cấu hình cách dựng model; nó không tự chứng minh source completeness, uniqueness, late-data coverage, atomic visibility hay idempotency end-to-end. Các bảo đảm phụ thuộc adapter, warehouse transaction và model contract.

## Note dẫn xuất

- [[Load Semantics Append Upsert Merge Replace and Swap]]
- [[Batch Idempotency Deterministic Keys and Overwrite]]
