---
source_id: src.web.postgresql-concurrency-control
source_type: official-documentation
title: Concurrency Control, Transaction Isolation and Explicit Locking
publisher: PostgreSQL Global Development Group
url: https://www.postgresql.org/docs/current/mvcc.html
captured: 2026-09-28
status: active-web-source
rights: public-web-documentation
authority: primary-project-documentation
tags: [source/web, postgresql, concurrency, isolation, locking, deadlock]
---

# PostgreSQL concurrency control — hồ sơ nguồn

## Phạm vi sử dụng

Nguồn dùng cho isolation semantics, row-level locks, `SELECT FOR UPDATE`, `NOWAIT`, `SKIP LOCKED`, lock lifetime, deadlock và serialization failure. Ví dụ PostgreSQL không được nâng thành quy tắc cho mọi database.

## Kiểm chứng

- Đã đọc các mục Concurrency Control, Transaction Isolation, Explicit Locking và `SELECT` locking clause ngày 2026-09-28.
- URL `current` trỏ tài liệu PostgreSQL hiện hành; implementation lab PostgreSQL 17 phải ghim lại URL version khi chạy.
- Tài liệu nêu `SKIP LOCKED` tạo góc nhìn không nhất quán và phù hợp cho queue-like access, không phải truy vấn dữ liệu tổng quát.

## Note dẫn xuất

- [[Concurrency Control - Optimistic and Pessimistic|Kiểm soát đồng thời lạc quan và bi quan]]
