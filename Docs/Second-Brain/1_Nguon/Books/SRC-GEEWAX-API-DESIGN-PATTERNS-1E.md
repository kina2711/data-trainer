---
source_id: src.book.geewax-api-design-patterns.1e
source_type: book
title: API Design Patterns
authors:
  - JJ Geewax
publisher: Manning Publications
edition: first-edition
published: 2021
captured: 2026-09-28
status: active-private-source
rights: copyrighted-private-owner-provided
sensitivity: private
authority: practitioner-secondary-source
sha256: d3e249946160d18fc59e822edd3b0f68d7ce13921c6f196ae1774a8ac00e7952
canonical_path: /home/kina2711/PROJECT/data-trainer/Material/Reference_temp/API_Design_Patterns_-_JJ_Geewax.pdf
extraction_method: pdftotext-layout-bounded-page-range
tags:
  - source/book
  - api-design
  - compatibility
  - versioning
  - idempotency
aliases:
  - API Design Patterns
---

# API Design Patterns — hồ sơ nguồn

## Phạm vi sử dụng

Nguồn được dùng cho định nghĩa compatibility theo quan sát của client, chính sách backward compatibility, các trường hợp thêm field hoặc resource, thay đổi semantics, versioning và deprecation.

## Provenance

- Bản PDF do chủ dự án cung cấp trong `Material/Reference_temp`.
- SHA-256 được tính trực tiếp; PDF gồm 846 trang và có text layer.
- Nội dung trang bản quyền ghi JJ Geewax, Manning Publications, 2021.
- Metadata cho thấy tệp được tạo lại bằng Calibre năm 2026; byte identity với bản Manning chưa được xác minh.
- Không sao chép PDF vào vault và không tái phân phối công khai.

## Phạm vi đã đọc

- Chapter 24, versioning, compatibility, backward-compatibility policy, semantic changes, versioning strategies và trade-offs; PDF 642–680.
- Pagination và continuation token cho list methods; PDF 556–566.
- Chapter 26, request deduplication, request identifier, response replay, fingerprint/collision và expiration; PDF 712–733.
- 72/72 trang duy nhất trong toàn bộ các phạm vi đã đọc có text trích xuất được.

## Giới hạn

- “Thêm field là tương thích” không phải luật tuyệt đối; client strict, giới hạn bộ nhớ, parser đóng và semantic expectation có thể làm thay đổi đó phá vỡ.
- SemVer chỉ mang nghĩa khi compatibility policy đã được công bố và tuân thủ.
- Nguồn tập trung vào web API; áp dụng cho event/schema dữ liệu cần ghi thêm delivery và replay rules.

## Note dẫn xuất

- [[Consumer-Provider Contract Testing|Kiểm thử hợp đồng giữa producer và consumer]]
- [[API Contracts - Resources Errors and Versioning|Hợp đồng API: resource, lỗi và versioning]]
- [[Idempotency Keys and Deduplication State|Idempotency key và trạng thái chống trùng]]
- [[Metric Lifecycle - Propose, Certify, Version, Deprecate]]
- [[Interface Design for an Analytical Product]]
- [[Contract Compatibility for Consumers]]

## Liên kết về source note của dự án

- `Material/DE/Reference/Library/Source-Notes/PACK-SOFTWARE-DESIGN-BOOK-01.md`
