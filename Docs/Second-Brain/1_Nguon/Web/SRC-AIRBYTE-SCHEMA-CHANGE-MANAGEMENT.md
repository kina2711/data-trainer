---
source_id: src.web.airbyte-schema-change-management
source_type: web-documentation
title: Airbyte Schema Change Management
publisher: Airbyte
canonical_url: https://docs.airbyte.com/platform/using-airbyte/schema-change-management
captured: 2026-10-02
status: active-public-source
rights: public-vendor-documentation
authority: official-product-documentation
tags: [source/web, ingestion, schema-drift, backfill]
---

# Airbyte Schema Change Management — hồ sơ nguồn

## Phạm vi đã đọc

- Chu kỳ phát hiện schema và các lựa chọn propagate, approve hoặc stop.
- Hành vi với thêm, xóa, đổi kiểu field; thêm, xóa stream.
- Cursor hoặc primary key bị xóa được xem là breaking change và làm connection dừng.
- Backfill cho cột mới/đổi tên, giới hạn và tác động chi phí.
- Major connector version change có thể đổi schema, sync mode, key, state hoặc destination format.

## Giới hạn

Đây là hành vi của Airbyte theo phiên bản và cấu hình được nêu. Nó không tạo một phân loại schema change phổ quát, không chứng minh downstream compatibility và không thay impact analysis hay reconciliation độc lập.

## Note dẫn xuất

- [[Schema Drift Detection Classification and Quarantine]]
- [[Ingestion SLO and Backfill Isolation Rule]]
- [[Connector Landscape Build Adopt or Buy]]
