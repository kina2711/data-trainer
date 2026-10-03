---
source_id: src.web.redshift-wlm-query-metrics
source_type: web-documentation
title: Amazon Redshift WLM Query Monitoring Metrics
publisher: Amazon Web Services
canonical_url: https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html
captured: 2026-10-01
status: active-public-source
rights: public-vendor-documentation
authority: official-product-documentation
tags: [source/web, redshift, workload-management, queue-time, execution-time, skew]
---

# Redshift WLM query metrics — hồ sơ nguồn

## Phạm vi đã đọc

- Tách query queue time, execution time và CPU time trong metric contract.
- Temporary blocks to disk, CPU skew, I/O skew, scan rows/blocks và query monitoring rules.
- Sai số lấy mẫu ở segment ngắn và khác biệt giữa provisioned/serverless metrics.

## Giới hạn

Tên field, unit và availability thuộc Redshift, không phải taxonomy chung cho mọi engine. Note map sang lifecycle chung nhưng yêu cầu ghi lại definition của engine đang đo.

## Note dẫn xuất

- [[Workload Management Concurrency and Cache]]
