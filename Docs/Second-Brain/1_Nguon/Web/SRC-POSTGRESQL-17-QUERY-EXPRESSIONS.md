---
source_id: src.web.postgresql-17-query-expressions
source_type: web-documentation
title: PostgreSQL 17 — Table Expressions and SELECT
publisher: PostgreSQL Global Development Group
canonical_url: https://www.postgresql.org/docs/17/queries-table-expressions.html
secondary_url: https://www.postgresql.org/docs/17/sql-select.html
captured: 2026-09-29
status: active
authority: official-primary-documentation
rights: public-web-documentation
---

# PostgreSQL 17 — query expressions

## Phạm vi đã đọc

Đã đọc table-expression pipeline, FROM/WHERE/GROUP BY/HAVING/window processing, joined tables, ON/USING/NATURAL, inner/left/right/full join, alias scope; đồng thời đọc processing steps của SELECT. Đặc biệt giữ ví dụ cho thấy điều kiện bảng phải trong `ON` và trong `WHERE` cho kết quả khác nhau với LEFT JOIN.

## Giới hạn

Logical processing không phải physical execution order. Optimizer có thể biến đổi kế hoạch miễn giữ semantics theo PostgreSQL 17.

## Note dẫn xuất

- [[Relational Algebra and Logical Equivalence]]
- [[Logical Query Processing Order]]
- [[Joins Duplicate Multiplication and NULL Behaviour]]
