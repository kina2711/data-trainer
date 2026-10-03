---
source_id: src.web.postgresql-17-constraints
source_type: web-documentation
title: PostgreSQL 17 — Constraints
publisher: PostgreSQL Global Development Group
canonical_url: https://www.postgresql.org/docs/17/ddl-constraints.html
captured: 2026-09-28
status: active
authority: official-primary-documentation
rights: public-web-documentation
---

# PostgreSQL 17 — constraints

## Phạm vi đã đọc

Đã đọc CHECK, NOT NULL, UNIQUE, PRIMARY KEY và FOREIGN KEY. Primary key kết hợp uniqueness với not-null và mỗi bảng chỉ có một primary key được chỉ định, nhưng có thể có nhiều UNIQUE constraint. Foreign key duy trì referential integrity. CHECK không phải cơ chế để kiểm ràng buộc tùy ý qua các dòng khác.

## Giới hạn

Đây là semantics PostgreSQL 17. DDL và hành vi NULL/deferrable/index ở DBMS khác phải kiểm tài liệu tương ứng.

## Note dẫn xuất

- [[Relations Keys and Functional Dependencies|Quan hệ, khoá và phụ thuộc hàm]]
