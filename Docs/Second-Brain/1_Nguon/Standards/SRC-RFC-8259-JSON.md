---
source_id: src.standard.rfc8259-json
source_type: standard
title: The JavaScript Object Notation Data Interchange Format
publisher: IETF
canonical_url: https://datatracker.ietf.org/doc/html/rfc8259
captured: 2026-10-01
status: active-public-source
rights: public-standards-document
authority: internet-standard
tags: [source/standard, json, number, unicode, interoperability]
---

# RFC 8259 JSON — hồ sơ nguồn

## Phạm vi đã đọc

- JSON values, objects, arrays, strings, number grammar và duplicate-name interoperability warning.
- Number range/precision phụ thuộc implementation; binary64 exact-integer interoperability range được nêu làm mốc.
- UTF-8 requirement cho trao đổi ngoài closed ecosystem và parser behavior boundaries.

## Giới hạn

JSON không có built-in timestamp, decimal, identifier hay timezone type. Precision loss xuất hiện ở reader representation/conversion, không phải định luật cho mọi parser.

## Note dẫn xuất

- [[CSV and JSON Ambiguity Contracts]]
