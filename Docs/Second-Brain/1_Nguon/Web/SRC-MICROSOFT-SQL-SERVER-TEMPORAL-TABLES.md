---
source_id: src.web.microsoft-sql-server-temporal-tables
source_type: official-documentation
title: SQL Server system-versioned temporal tables
publisher: Microsoft Learn
canonical_url: https://learn.microsoft.com/en-us/sql/relational-databases/tables/temporal-tables
captured: 2026-10-01
status: active-web-source
rights: public-web-documentation
authority: vendor-primary-documentation
tags: [source/web, sql-server, temporal, system-time, history]
---

# SQL Server — system-versioned temporal tables

## Phạm vi đã đọc

Đã đọc overview, current/history table, hai period columns, insert/update/delete semantics, `FOR SYSTEM_TIME AS OF`, zero-duration row caveat, UTC transaction-begin timestamp và các use case audit/point-in-time/SCD.

## Locator

- https://learn.microsoft.com/en-us/sql/relational-databases/tables/temporal-tables
- https://learn.microsoft.com/en-us/sql/relational-databases/tables/temporal/overview
- https://learn.microsoft.com/en-us/sql/relational-databases/tables/temporal-table-usage-scenarios

## Giới hạn

`ValidFrom`/`ValidTo` trong tính năng này do engine quản lý cho **system time**; tên cột không biến chúng thành business-valid time. Bài học tách hai trục và không khái quát cú pháp SQL Server sang DBMS khác.

## Note dẫn xuất

- [[Valid time, system time, corrections and restatement]]
