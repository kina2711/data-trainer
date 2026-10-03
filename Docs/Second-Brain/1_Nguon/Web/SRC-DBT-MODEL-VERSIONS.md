---
source_id: src.web.dbt-model-versions
source_type: web-documentation
title: dbt Model Versions and Breaking Contract Changes
publisher: dbt Labs
canonical_url: https://docs.getdbt.com/reference/resource-properties/versions?version=2
captured: 2026-10-02
status: active
authority: official-product-documentation
rights: public-web-documentation
tags: [source/web, dbt, model-contracts, versioning, compatibility]
---

# dbt — Model Versions and Breaking Contract Changes

## Phạm vi đã đọc

Nguồn dùng như ví dụ công cụ về versioned model contract và phát hiện schema-breaking changes trong CI. Tài liệu hiện hành cho biết dbt có thể phát hiện remove column, đổi data type, bỏ/sửa constraints và thay contracted unversioned model; additive column/constraint changes không bị công cụ phân loại là breaking.

## Locator đã dùng

- Dòng 219–232: version-specific columns, naming recommendation và latest-version pointer.
- Dòng 233–270: Slim CI detection, các loại breaking change và hướng dẫn tạo model version mới.
- Dòng 274–277: additive changes theo contract checker của dbt.

## Giới hạn

“Additive” theo schema checker không đồng nghĩa an toàn với mọi consumer. `SELECT *`, positional readers, closed deserializers, schema snapshots, cost và semantic assumptions vẫn có thể vỡ. Đổi nghĩa nhưng giữ type/name thường không được schema diff phát hiện; cần semantic regression và consumer notification.

## Note dẫn xuất

- [[Contract Compatibility for Consumers]]
