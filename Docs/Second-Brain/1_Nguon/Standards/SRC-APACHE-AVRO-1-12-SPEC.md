---
source_id: src.standard.apache-avro-1.12
source_type: specification
title: Apache Avro 1.12.0 Specification
publisher: Apache Software Foundation
canonical_url: https://avro.apache.org/docs/1.12.0/specification/
captured: 2026-10-01
status: active-public-source
rights: Apache-project-documentation
authority: normative-project-specification
tags: [source/standard, avro, schema-resolution, container-file]
---

# Apache Avro 1.12 — hồ sơ nguồn

## Phạm vi đã đọc

- Schema declaration, defaults, aliases, primitive promotion, union resolution và record field matching.
- Writer schema/reader schema resolution rules và error conditions.
- Object Container File header, embedded schema, blocks, codecs và sync markers cho splitting.
- Logical types được đối chiếu với underlying primitive và application semantics.

## Giới hạn

Spec cho phép implementation optionally use aliases; hành vi thư viện cụ thể phải kiểm. Decode success chỉ chứng minh structural resolution, không chứng minh semantic compatibility.

## Note dẫn xuất

- [[Avro Writer Reader Schema Resolution]]
- [[Four Cell Schema Compatibility Gate]]
