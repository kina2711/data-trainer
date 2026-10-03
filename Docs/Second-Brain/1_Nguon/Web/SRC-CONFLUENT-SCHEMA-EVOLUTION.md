---
source_id: src.web.confluent-schema-evolution
source_type: web-documentation
title: Schema Evolution and Compatibility for Schema Registry
publisher: Confluent
canonical_url: https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html
captured: 2026-10-01
status: active-public-source
rights: public-vendor-documentation
authority: official-product-documentation
tags: [source/web, schema-registry, backward, forward, full, transitive]
---

# Confluent schema evolution — hồ sơ nguồn

## Phạm vi đã đọc

- BACKWARD, FORWARD, FULL và transitive variants.
- Compatibility check direction và registry enforcement at registration time.
- Avro/Protobuf rules delegate to format-specific resolution semantics.

## Giới hạn

Registry acceptance is a structural gate over configured history, not proof of business semantics, generated-code compatibility, deployment readiness or golden-record behavior.

## Note dẫn xuất

- [[Four Cell Schema Compatibility Gate]]
