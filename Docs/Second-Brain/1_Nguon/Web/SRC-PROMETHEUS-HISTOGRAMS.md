---
source_id: src.web.prometheus-histograms
source_type: official-documentation
title: Histograms and summaries
publisher: Prometheus Authors
url: https://prometheus.io/docs/practices/histograms/
captured: 2026-09-28
status: active-web-source
rights: public-web-documentation
authority: primary-project-documentation
tags: [source/web, prometheus, histogram, summary, quantile, metrics]
---

# Prometheus histograms and summaries — hồ sơ nguồn

## Phạm vi sử dụng

Nguồn dùng cho classic histogram bucket, summary quantile, aggregation trade-off, `histogram_quantile` và cảnh báo không lấy trung bình quantile từ summary. Query phải đối chiếu metric/version thực tế.

## Kiểm chứng

- Truy cập ngày 2026-09-28.
- Trang có ghi chú tài liệu cũ hơn một số tính năng hiện hành và dẫn sang native histograms; note không trộn hai model.
- Bucket/quantile examples là minh họa, không phải SLO mặc định.

## Note dẫn xuất

- [[API Observability - RED Metrics and Tracing|Quan sát API bằng RED metrics và distributed tracing]]
