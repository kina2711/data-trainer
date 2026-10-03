---
source_id: src.web.oauth-security-bcp
source_type: standard
title: Best Current Practice for OAuth 2.0 Security
publisher: IETF
url: https://datatracker.ietf.org/doc/html/rfc9700
published: 2025-01
captured: 2026-09-28
status: active-web-source
rights: public-standard
authority: primary-standard
tags: [source/web, oauth, access-token, refresh-token, rotation, security]
---

# RFC 9700 OAuth 2.0 Security BCP — hồ sơ nguồn

## Phạm vi sử dụng

RFC dùng cho access-token privilege restriction, replay prevention, sender-constrained token và refresh-token protection/rotation. Không được diễn giải thành một JWT implementation bắt buộc.

## Kiểm chứng

- Đọc §§2.2–2.3 và 4.14 ngày 2026-09-28.
- RFC yêu cầu public-client refresh token phải sender-constrained hoặc dùng rotation để phát hiện replay.
- Refresh token phải ràng buộc với scope/resource đã được consent; expiry khi không hoạt động là policy do authorization server quyết định.

## Note dẫn xuất

- [[Authentication Authorization and Ownership Checks|Xác thực, ủy quyền và kiểm quyền sở hữu]]
