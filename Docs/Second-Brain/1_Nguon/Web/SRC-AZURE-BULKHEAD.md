---
source_id: src.web.azure-bulkhead
source_type: vendor-documentation
title: Bulkhead Pattern
publisher: Microsoft Azure Architecture Center
url: https://learn.microsoft.com/azure/architecture/patterns/bulkhead
captured: 2026-09-28
status: active-web-source
rights: public-web-documentation
authority: primary-vendor-architecture-guidance
tags: [source/web, resilience, bulkhead, failure-isolation, connection-pool]
---

# Azure Bulkhead Pattern — hồ sơ nguồn

## Phạm vi sử dụng

Nguồn dùng cho failure isolation bằng pool/partition riêng, ví dụ connection pool theo dependency và trade-off chi phí, utilization, performance, manageability.

## Kiểm chứng

- Truy cập ngày 2026-09-28.
- Tài liệu mô tả việc một dependency không phản hồi có thể cạn resource chung và làm hỏng call tới dependency khác.
- Bulkhead không mặc nhiên phù hợp khi overhead/cost isolation lớn hơn rủi ro; boundary phải theo yêu cầu kỹ thuật và nghiệp vụ.

## Note dẫn xuất

- [[Timeouts Circuit Breakers and Bulkheads|Deadline, timeout, circuit breaker và bulkhead]]
