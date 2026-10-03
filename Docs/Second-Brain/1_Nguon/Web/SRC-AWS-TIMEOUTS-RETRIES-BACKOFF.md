---
source_id: src.web.aws-timeouts-retries-backoff
source_type: practitioner-guidance
title: Timeouts, retries, and backoff with jitter
publisher: Amazon Web Services
url: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
captured: 2026-09-28
status: active-web-source
rights: public-web-documentation
authority: primary-vendor-practitioner-guidance
tags: [source/web, resilience, timeout, retry, backoff, jitter]
---

# AWS timeouts, retries and backoff with jitter — hồ sơ nguồn

## Phạm vi sử dụng

Nguồn dùng cho cách chọn timeout từ false-timeout budget và latency percentile, retry amplification, capped exponential backoff, jitter và token-bucket retry budget. Các con số AWS không được dùng làm default cho workload khác.

## Kiểm chứng

- Truy cập ngày 2026-09-28.
- Nguồn phân tích retry như load tăng thêm khi dependency đã gặp vấn đề và cảnh báo retry ở nhiều tầng.
- Timeout cần bao phủ connection setup phù hợp; deployment/cold connection có thể tạo false timeout nếu boundary không rõ.

## Note dẫn xuất

- [[Timeouts Circuit Breakers and Bulkheads|Deadline, timeout, circuit breaker và bulkhead]]
