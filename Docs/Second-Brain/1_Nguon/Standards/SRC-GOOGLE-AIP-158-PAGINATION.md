---
source_id: src.standard.google-aip-158-pagination
source_type: design-standard
title: Google AIP-158 Pagination
publisher: Google
canonical_url: https://google.aip.dev/158
captured: 2026-10-02
status: active-public-source
rights: public-design-guidance
authority: official-api-design-standard
tags: [source/standard, api, pagination, page-token, cursor]
---

# Google AIP-158 Pagination — hồ sơ nguồn

## Phạm vi đã đọc

- `page_size`, opaque `page_token`, `next_page_token` và end-of-collection contract.
- Các tham số khác phải giữ nguyên khi dùng page token; token không mang quyền truy cập.
- Token có thể hết hạn; adding pagination later is behaviorally incompatible.
- `skip` semantics và degraded responses.

## Giới hạn

AIP thiết kế interface; nó không bảo đảm snapshot consistency khi collection thay đổi, không quy định keyset SQL và không thay source-specific error/body semantics. Extractor phải kiểm duplication, omission, expiry và authorization trên API thật.

## Note dẫn xuất

- [[API Offset Keyset and Cursor Pagination]]
