---
source_id: src.web.owasp-authorization-cheat-sheet
source_type: security-guidance
title: Authorization Cheat Sheet
publisher: OWASP Foundation
url: https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html
captured: 2026-10-02
status: active-web-source
rights: public-web-documentation
authority: security-community-primary-guidance
tags: [source/web, owasp, authorization, least-privilege, deny-by-default]
---

# OWASP Authorization Cheat Sheet — hồ sơ nguồn

## Phạm vi sử dụng

Nguồn dùng cho phân biệt authentication/authorization, least privilege, deny by default, kiểm permission trên mọi request và enforcement server-side.

## Locator đã dùng

- Dòng 194–203: phân biệt authentication và authorization, cùng các dạng privilege elevation.
- Dòng 206–224: least privilege, deny by default và kiểm quyền trên mọi request.
- Dòng 230–240: không phó mặc authorization cho framework; cần defense in depth và hiểu giới hạn công cụ.
- Truy cập lại ngày 2026-10-02.
- Checklist được dùng như security guidance; policy model và HTTP response cụ thể vẫn phụ thuộc threat model của hệ thống.

## Note dẫn xuất

- [[Authentication Authorization and Ownership Checks|Xác thực, ủy quyền và kiểm quyền sở hữu]]
- [[Access Control at the Semantic Layer]]
- [[Serving, Access and Security for Consumers]]
- [[Capstone - A Governed Customer Health Data Product]]
