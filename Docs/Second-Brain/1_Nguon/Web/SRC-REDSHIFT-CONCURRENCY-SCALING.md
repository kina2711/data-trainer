---
source_id: src.web.redshift-concurrency-scaling
source_type: web-documentation
title: Amazon Redshift Concurrency Scaling
publisher: Amazon Web Services
canonical_url: https://docs.aws.amazon.com/redshift/latest/dg/concurrency-scaling.html
captured: 2026-10-01
status: active-public-source
rights: public-vendor-documentation
authority: official-product-documentation
tags: [source/web, redshift, concurrency, queue, workload-isolation, autoscaling]
---

# Redshift concurrency scaling — hồ sơ nguồn

## Phạm vi đã đọc

- Routing eligible work từ WLM queue sang concurrency-scaling cluster.
- Monitoring main/secondary execution, queue time, execution time và usage.
- Eligibility, queue configuration, cluster limits và cost boundary.

## Giới hạn

Concurrency scaling không đồng nghĩa mọi query đều được chuyển hoặc mọi latency đều giảm. Eligibility, configured limits, startup, workload shape và billing phải được quan sát; tài liệu sản phẩm không thay benchmark có controlled load.

## Note dẫn xuất

- [[Workload Management Concurrency and Cache]]
