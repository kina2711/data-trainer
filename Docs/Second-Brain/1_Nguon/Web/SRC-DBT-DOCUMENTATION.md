---
source_id: src.web.dbt-documentation
source_type: product-documentation
title: dbt Documentation
publisher: dbt Labs
canonical_url: https://docs.getdbt.com/docs/build/documentation
captured: 2026-10-01
status: active
authority: official-product-documentation
rights: public-web-documentation
tags: [source/web, dbt, documentation, metadata, docs-as-code]
---

# dbt Documentation

## Phạm vi đã đọc

Nguồn dùng cho generated documentation, resource descriptions, model/column metadata, lineage và docs blocks. dbt đặt descriptions cạnh resource declarations và tạo site bằng lệnh tài liệu; việc introspect warehouse khiến cột chưa có mô tả vẫn có thể xuất hiện, vì vậy “có trang docs” không đồng nghĩa “mọi public field đã được mô tả”.

## Locator đã dùng

- “Overview”: project information, DAG, tests, warehouse metadata và descriptions.
- “Adding descriptions”: `description` cho model, column, source và resource khác; cột chưa document vẫn có thể hiện ra sau introspection.
- “Generating documentation”: build/export documentation site.
- “Using docs blocks”: long-form Markdown gắn với resources.

## Giới hạn

Nguồn mô tả khả năng của dbt, không quy định hierarchy bốn tầng hoặc bốn documentation gates của giáo trình. Executable examples, freshness consistency và semantic-reference checks cần pipeline riêng.

## Note dẫn xuất

- [[The Documentation Hierarchy]]
- [[Documentation Tests]]
