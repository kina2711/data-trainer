---
source_id: src.web.postgresql-17-window-functions
source_type: web-documentation
title: PostgreSQL 17 — Window Functions
publisher: PostgreSQL Global Development Group
canonical_url: https://www.postgresql.org/docs/17/tutorial-window.html
secondary_url: https://www.postgresql.org/docs/17/functions-window.html
captured: 2026-09-29
status: active
authority: official-primary-documentation
rights: public-web-documentation
---

# PostgreSQL 17 — window functions

## Phạm vi đã đọc

Đã đọc partition, ordering, peer rows, default frame, ranking functions, `lag`/`lead`, aggregate dùng như window function và giới hạn vị trí đặt window expression. Đối chiếu thêm cú pháp frame trong SQL expressions của PostgreSQL 17.

## Giới hạn

Default frame phụ thuộc việc có `ORDER BY` và quan hệ peer. `lag` đọc row trước trong tập đầu vào đã sắp xếp, không tự hiểu kỳ lịch bị thiếu. PostgreSQL 17 không triển khai tùy chọn SQL-standard `IGNORE NULLS` cho các hàm liên quan.

## Note dẫn xuất

- [[Window Functions - Partition Order and Frame]]
- [[Window Frames Running Totals and Period Comparison]]
