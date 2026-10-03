---
source_id: src.standard.rfc9293-tcp
source_type: internet-standard
title: RFC 9293 — Transmission Control Protocol
authors: [Wesley M. Eddy]
publisher: RFC Editor
published: 2022-08
canonical_url: https://www.rfc-editor.org/rfc/rfc9293.html
captured: 2026-10-02
status: active-public-source
rights: IETF-Trust
sensitivity: public
authority: authoritative-primary-source
extraction_method: bounded-web-review
tags: [source/standard, tcp, transport]
---

# RFC 9293 — hồ sơ nguồn

## Phạm vi đã đọc

- TCP service model, state machine, connection establishment/termination, sequence space và reliable ordered byte stream.
- Không dùng RFC này để suy ra congestion-control algorithm hoặc kernel default cụ thể; các phần đó cần implementation evidence.

## Giới hạn

RFC mô tả protocol requirements, không mô tả đầy đủ middlebox, TLS, application framing hoặc timeout policy của một client cụ thể.
