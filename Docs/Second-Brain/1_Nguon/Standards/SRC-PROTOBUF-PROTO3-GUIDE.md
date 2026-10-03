---
source_id: src.standard.protobuf-proto3-guide
source_type: specification-guide
title: Protocol Buffers Proto3 Language Guide
publisher: Google
canonical_url: https://protobuf.dev/programming-guides/proto3/
captured: 2026-10-01
status: active-public-source
rights: public-project-documentation
authority: official-project-guide
tags: [source/standard, protobuf, field-number, compatibility, unknown-fields]
---

# Protobuf proto3 guide — hồ sơ nguồn

## Phạm vi đã đọc

- Field-number identity, reserved numbers/names, deletion and consequences of reuse.
- Binary wire-safe, wire-compatible và application/source-code compatibility distinctions.
- Unknown-field preservation in proto3 binary messages và caveats across transformations.

## Giới hạn

Generated APIs, JSON/TextFormat, language runtimes và parse–modify–serialize paths có thể có additional behavior. Wire-safe không bảo đảm application semantics hoặc source compatibility.

## Note dẫn xuất

- [[Protobuf Field Numbers and Wire Compatibility]]
- [[Four Cell Schema Compatibility Gate]]
