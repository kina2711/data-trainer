---
source_id: src.web.sqlalchemy-session-basics
source_type: official-documentation
title: Session Basics
publisher: SQLAlchemy Documentation
url: https://docs.sqlalchemy.org/en/20/orm/session_basics.html
captured: 2026-09-28
status: active-web-source
rights: public-web-documentation
authority: primary-product-documentation
tags: [source/web, sqlalchemy, session, unit-of-work, connection-pool]
---

# SQLAlchemy Session Basics — hồ sơ nguồn

## Phạm vi sử dụng

Tài liệu được dùng để mô tả một implementation cụ thể của Unit of Work: Session giữ identity map, ghi nhận thay đổi, flush trước query hoặc commit, giữ transaction trên connection, rồi trả connection về pool khi commit hoặc rollback. Note không đồng nhất Session của SQLAlchemy với mọi cách cài Unit of Work.

## Kiểm chứng

- Truy cập ngày 2026-09-28; tài liệu thuộc nhánh SQLAlchemy 2.0.
- Session là object mutable, stateful và không được chia sẻ đồng thời giữa thread hoặc asyncio task nếu không có cơ chế đồng bộ phù hợp.
- API có thể đổi giữa major version; ví dụ lab phải ghim dependency.

## Note dẫn xuất

- [[Transaction Boundaries and the Unit of Work|Ranh giới giao dịch và Unit of Work]]
