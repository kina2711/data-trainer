---
source_id: src.web.backstage-software-catalog
source_type: project-documentation
title: Backstage Software Catalog and Entity Lifecycle
publisher: Backstage / CNCF
canonical_url: https://backstage.io/docs/features/software-catalog/
captured: 2026-10-01
status: active
authority: official-project-documentation
rights: public-web-documentation
tags: [source/web, catalog, ownership, lifecycle, metadata]
---

# Backstage — Software Catalog and Entity Lifecycle

## Phạm vi đã đọc

Nguồn dùng như ví dụ về metadata cạnh code, ownership, discoverability, entity processing và orphan state. Catalog là hub/cache của authoritative descriptors và linked tools; nó không tự trở thành source of truth cho runtime health hoặc business meaning.

## Locator đã dùng

- Software Catalog overview: ownership/metadata, YAML cạnh code, owner cập nhật qua Git workflow.
- Technical overview: components, APIs, resources, systems, domains, permissions và notifications.
- “The Life of an Entity”: ingestion, policy/processor validation, stitching và removal behavior.
- “Creating the Catalog Graph”: ownership, lifecycle tracking và catalog không phải ultimate source of truth.

## Giới hạn

Sáu state của L200 và certification gates là curriculum synthesis. Backstage entity lifecycle mô tả catalog mechanics, không chứng nhận data product correctness, usability hay business approval.

## Note dẫn xuất

- [[Lifecycle and the Operating Model]]
