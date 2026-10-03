---
source_id: src.web.microservices-io-polling-publisher
source_type: web-documentation
title: Polling publisher pattern
author: Chris Richardson
canonical_url: https://microservices.io/patterns/data/polling-publisher.html
captured: 2026-09-28
status: active
authority: practitioner-primary-pattern-catalog
rights: public-web-documentation
---

# Polling publisher pattern — hồ sơ nguồn

## Phạm vi đã đọc

Đã đọc toàn bộ pattern. Polling publisher truy vấn outbox định kỳ, phát message rồi ghi trạng thái. Cách này phù hợp SQL nhưng khó đảm bảo thứ tự khi nhiều publisher chạy đồng thời. Transaction-log tailing là phương án liên quan khi hệ quản trị và hạ tầng cho phép.

## Giới hạn

Nguồn không quy định một SQL claim algorithm duy nhất. Mọi lựa chọn `FOR UPDATE SKIP LOCKED`, lease hoặc partition trong note phải được kiểm theo database và semantics của hệ thống cụ thể.

## Note dẫn xuất

- [[Transactional Outbox - One Atomic Write|Transactional outbox — một lần ghi nguyên tử]]
