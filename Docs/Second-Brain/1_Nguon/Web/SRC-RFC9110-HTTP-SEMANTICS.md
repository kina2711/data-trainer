---
source_id: src.web.rfc9110-http-semantics
source_type: standard
title: HTTP Semantics
publisher: IETF
url: https://datatracker.ietf.org/doc/html/rfc9110
captured: 2026-09-28
status: active-web-source
rights: public-standard
authority: primary-standard
tags: [source/web, http, idempotence, retry, semantics]
---

# RFC 9110 HTTP Semantics — hồ sơ nguồn

## Phạm vi sử dụng

RFC được dùng cho định nghĩa method idempotence và điều kiện client có thể tự động retry. Nguồn không định nghĩa một idempotency-key protocol chung.

## Kiểm chứng

- Đọc §9.2.2 “Idempotent Methods” ngày 2026-09-28.
- `PUT`, `DELETE` và safe methods được định nghĩa idempotent theo intended effect; side effect nội bộ như log vẫn có thể lặp.
- Client không nên tự retry non-idempotent method nếu không biết semantics thực sự idempotent hoặc có cách phát hiện request gốc chưa được áp dụng.

## Note dẫn xuất

- [[Idempotency Keys and Deduplication State|Idempotency key và trạng thái chống trùng]]
