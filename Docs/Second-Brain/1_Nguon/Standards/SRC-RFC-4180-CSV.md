---
source_id: src.standard.rfc4180-csv
source_type: standard
title: Common Format and MIME Type for Comma-Separated Values Files
publisher: IETF
canonical_url: https://datatracker.ietf.org/doc/html/rfc4180
captured: 2026-10-01
status: active-public-source
rights: public-standards-document
authority: informational-rfc
tags: [source/standard, csv, text, interoperability]
---

# RFC 4180 CSV — hồ sơ nguồn

## Phạm vi đã đọc

- Section 2: records, CRLF, optional header, comma, double quotes, embedded comma/quote/line break và escaping.
- Section 3: `text/csv`, optional `charset` và `header` parameters.
- RFC tự ghi nhận implementations có nhiều cách diễn giải; đây là common format, không phải type/schema contract.

## Giới hạn

RFC 4180 không định nghĩa null, data types, locale, date/time semantics hay schema evolution. Nhiều dialect thực tế khác RFC; ingestion phải lưu dialect contract riêng.

## Note dẫn xuất

- [[CSV and JSON Ambiguity Contracts]]
