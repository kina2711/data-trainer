---
source_id: src.web.postgresql-17-generate-series
source_type: web-documentation
title: PostgreSQL 17 — Series Generating Functions
publisher: PostgreSQL Global Development Group
canonical_url: https://www.postgresql.org/docs/17/functions-srf.html
captured: 2026-09-29
status: active
authority: official-primary-documentation
rights: public-web-documentation
---

# PostgreSQL 17 — series generating functions

## Phạm vi đã đọc

Đã đọc các overload của `generate_series`, quy tắc start/stop/step, trường hợp trả zero row, step bằng zero và biến thể timestamp có timezone. Nguồn được dùng để dựng calendar scaffold trước khi tính chỉ số theo kỳ.

## Giới hạn

`generate_series` là tiện ích PostgreSQL, không phải cú pháp portable giữa mọi DBMS. Calendar nghiệp vụ còn cần holiday, fiscal period và timezone policy riêng.

## Note dẫn xuất

- [[Window Frames Running Totals and Period Comparison]]
