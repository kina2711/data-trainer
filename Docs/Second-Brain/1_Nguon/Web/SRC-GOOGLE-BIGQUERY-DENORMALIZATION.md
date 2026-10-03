---
source_id: src.web.google-bigquery-denormalization
source_type: official-documentation
title: BigQuery denormalization with nested and repeated fields
publisher: Google Cloud
canonical_url: https://cloud.google.com/bigquery/docs/best-practices-performance-nested
captured: 2026-10-01
status: active-web-source
rights: public-web-documentation
authority: vendor-primary-documentation
tags: [source/web, bigquery, denormalization, nested, repeated, one-big-table]
---

# BigQuery — denormalization, nested và repeated fields

## Phạm vi đã đọc

Đã đọc phần denormalization, `STRUCT`, `ARRAY`, one-to-many inline, shuffle/join trade-off, cảnh báo flatten hoàn toàn và nhận xét rằng star schema vốn đã tối ưu cho analytics nên denormalize thêm không phải lúc nào cũng nhanh hơn.

## Locator

- https://cloud.google.com/bigquery/docs/best-practices-performance-nested
- https://cloud.google.com/bigquery/docs/migration/schema-data-overview#denormalization

## Giới hạn

Đây là khuyến nghị theo kiến trúc BigQuery. Không suy thành quy tắc chung rằng bảng rộng luôn nhanh hơn, rẻ hơn hoặc dễ bảo trì hơn.

## Note dẫn xuất

- [[Star, snowflake and the one-big-table trade-off]]
