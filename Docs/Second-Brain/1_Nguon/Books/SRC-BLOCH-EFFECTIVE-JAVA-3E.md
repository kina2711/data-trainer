---
source_id: src.book.bloch-effective-java.3e
source_type: book
title: Effective Java
subtitle: Best Practices for the Java Platform
authors:
  - Joshua Bloch
publisher: Addison-Wesley Professional
edition: third-edition
published: 2018
captured: 2026-09-28
status: active-private-source
rights: copyrighted-private-owner-provided
sensitivity: private
authority: practitioner-secondary-source
sha256: f55a60e65c553a34f2f2dd8451988b3886d849bfb258fdd13ee9a1a03e3b4b00
canonical_path: /home/kina2711/PROJECT/data-trainer/Material/DE/Reference/Library/knowledge/java/Effective Java_ Best practices for the Java Platform Updated for Java 9 3rd Edition{Joshua Bloch}(2017){106240065} libgen.li.pdf
extraction_method: pdftotext-layout-bounded-page-range
tags:
  - source/book
  - java
  - error-design
  - exceptions
aliases:
  - Effective Java 3e
---

# Effective Java 3e — hồ sơ nguồn

## Phạm vi sử dụng

Nguồn được dùng cho ranh giới giữa điều kiện có thể phục hồi và lỗi lập trình, exception translation, exception chaining, failure-capture information, tài liệu hóa error contract và failure atomicity. Chương trình dùng các decision rule này ở mức khái niệm, không biến checked exception của Java thành quy tắc bắt buộc cho ngôn ngữ khác.

## Provenance

- Bản PDF do chủ dự án cung cấp trong thư viện Reference của Data Engineer.
- SHA-256 được tính trực tiếp; PDF gồm 413 trang và có text layer.
- Nội dung trang bản quyền ghi Joshua Bloch, Third Edition, Addison-Wesley, 2018.
- Metadata PDF không có title/author; provenance phân phối và byte identity với bản nhà xuất bản chưa được xác minh.
- Không sao chép PDF vào vault và không tái phân phối công khai.

## Phạm vi đã đọc

- Chapter 10, Items 70–76: recoverable condition so với programming error, abstraction-appropriate exceptions, context, documentation và failure atomicity; PDF 317–329.
- 13/13 trang trong phạm vi có text trích xuất được.

## Giới hạn

- Checked/unchecked là cơ chế riêng của Java; note giữ decision rule về khả năng phục hồi và contract, rồi ánh xạ sang typed result hoặc exception theo ngôn ngữ đích.
- “Recoverable” phụ thuộc caller, idempotency, deadline và side effect; không thể suy chỉ từ tên lỗi.

## Note dẫn xuất

- [[Error Design for Data Pipelines|Thiết kế lỗi cho pipeline dữ liệu]]

## Liên kết về source note của dự án

- `Material/DE/Reference/Library/Source-Notes/PACK-SOFTWARE-DESIGN-BOOK-01.md`
