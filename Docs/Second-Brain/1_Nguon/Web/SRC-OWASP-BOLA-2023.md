---
source_id: src.web.owasp-bola-2023
source_type: security-guidance
title: API1:2023 Broken Object Level Authorization
publisher: OWASP Foundation
url: https://api-security.owasp.org/editions/2023/en/0xa1-broken-object-level-authorization/
captured: 2026-09-28
status: active-web-source
rights: public-web-documentation
authority: security-community-primary-guidance
tags: [source/web, owasp, api-security, authorization, bola]
---

# OWASP API1:2023 BOLA — hồ sơ nguồn

## Phạm vi sử dụng

Nguồn dùng cho yêu cầu object-level authorization tại mọi endpoint nhận object ID và giới hạn của ID khó đoán. Không dùng OWASP Top 10 làm bằng chứng về tỷ lệ khai thác của một hệ cụ thể.

## Kiểm chứng

- Truy cập ngày 2026-09-28.
- Guidance yêu cầu kiểm quyền trên object cho mọi function dùng input ID để truy cập object.
- GUID/UUID chỉ làm ID khó đoán hơn, không thay authorization check.

## Note dẫn xuất

- [[Authentication Authorization and Ownership Checks|Xác thực, ủy quyền và kiểm quyền sở hữu]]
