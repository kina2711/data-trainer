---
source_id: src.web.microservices-io-transactional-outbox
source_type: web-documentation
title: Transactional outbox pattern
author: Chris Richardson
canonical_url: https://microservices.io/patterns/data/transactional-outbox.html
captured: 2026-09-28
status: active
authority: practitioner-primary-pattern-catalog
rights: public-web-documentation
---

# Transactional outbox pattern — hồ sơ nguồn

## Phạm vi đã đọc

Đã đọc toàn bộ mô tả problem, forces, solution, result và related patterns. Nguồn xác nhận service ghi business entity và message vào cùng transaction của database; relay riêng đọc outbox và phát message. Cách này tránh 2PC nhưng relay có thể phát lặp nếu chết sau publish trước khi đánh dấu, vì vậy consumer phải idempotent. Thứ tự message cũng là một phần của forces, không tự nhiên đúng chỉ vì có bảng outbox.

## Giới hạn

Trang là pattern catalog, không phải đặc tả triển khai hoàn chỉnh. Schema, claim protocol, retention, partitioning và phép thử kill-point trong note là phần tổng hợp kỹ thuật, được gắn nhãn tương ứng.

## Note dẫn xuất

- [[Transactional Outbox - One Atomic Write|Transactional outbox — một lần ghi nguyên tử]]
