---
source_id: src.web.postgresql-17-with-queries
source_type: web-documentation
title: PostgreSQL 17 — WITH Queries
publisher: PostgreSQL Global Development Group
canonical_url: https://www.postgresql.org/docs/17/queries-with.html
captured: 2026-09-29
status: active
authority: official-primary-documentation
rights: public-web-documentation
---

# PostgreSQL 17 — WITH queries

## Phạm vi đã đọc

Đã đọc CTE thường, CTE đệ quy, mô hình working table, termination, search order, cycle detection, data-modifying CTE và quy tắc fold/materialize. Giữ riêng semantics PostgreSQL 17 của `MATERIALIZED` và `NOT MATERIALIZED`.

## Giới hạn

Hành vi tối ưu hóa CTE phụ thuộc DBMS và phiên bản. `SEARCH` tạo khóa sắp xếp đầu ra, không điều khiển thứ tự engine thăm node. Thử nghiệm recursion không kết thúc phải dùng timeout và dữ liệu cô lập.

## Note dẫn xuất

- [[Subqueries CTEs and Materialization]]
- [[Recursive CTEs for Hierarchies and Graphs]]
