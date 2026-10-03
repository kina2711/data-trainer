---
source_id: src.standard.rfc8446-tls13
source_type: internet-standard
title: RFC 8446 — The Transport Layer Security Protocol Version 1.3
authors: [Eric Rescorla]
publisher: RFC Editor
published: 2018-08
canonical_url: https://www.rfc-editor.org/rfc/rfc8446.html
captured: 2026-10-02
status: active-public-source
rights: IETF-Trust
sensitivity: public
authority: authoritative-primary-source
extraction_method: bounded-web-review
tags: [source/standard, tls, certificate, security]
---

# RFC 8446 — hồ sơ nguồn

## Phạm vi đã đọc

- TLS 1.3 handshake phases, parameter negotiation, server authentication, shared-key establishment và record protection.
- 0-RTT được giữ như một boundary có replay trade-off, không được mô tả như giảm latency miễn phí.

## Giới hạn

RFC không thay thế certificate-policy, trust-store, hostname-verification hoặc library-specific documentation. Note chỉ tuyên bố handshake mechanics trong scope TLS 1.3 và yêu cầu capture negotiated protocol trên target.
