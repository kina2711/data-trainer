---
source_id: src.web.fowler-unit-of-work
source_type: pattern-catalog
title: Unit of Work
authors: [Martin Fowler]
publisher: martinfowler.com
url: https://martinfowler.com/eaaCatalog/unitOfWork.html
captured: 2026-09-28
status: active-web-source
rights: public-web-documentation
authority: original-pattern-catalog
tags: [source/web, unit-of-work, transaction, persistence]
---

# Fowler Unit of Work — hồ sơ nguồn

## Phạm vi sử dụng

Nguồn được dùng cho định nghĩa pattern: theo dõi các object bị tác động bởi một business transaction, rồi điều phối việc ghi thay đổi và xử lý concurrency. Trang catalog không quy định rằng mọi HTTP request phải là một transaction hay mọi repository cần một class Unit of Work riêng.

## Kiểm chứng

- Truy cập ngày 2026-09-28.
- Trang do Martin Fowler xuất bản ngày 2003-03-05 và liên kết pattern với *Patterns of Enterprise Application Architecture*.
- Chỉ dùng định nghĩa và ranh giới pattern; phần triển khai cụ thể được đối chiếu bằng PostgreSQL và SQLAlchemy.

## Note dẫn xuất

- [[Transaction Boundaries and the Unit of Work|Ranh giới giao dịch và Unit of Work]]
