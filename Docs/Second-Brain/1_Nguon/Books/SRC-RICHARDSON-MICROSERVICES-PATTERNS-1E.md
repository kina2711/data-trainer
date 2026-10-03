---
source_id: src.book.richardson-microservices-patterns.1e
source_type: book
title: Microservices Patterns
subtitle: With examples in Java
authors:
  - Chris Richardson
publisher: Manning Publications
edition: first-edition
published: 2018
captured: 2026-09-28
status: active-private-source
rights: copyrighted-private-owner-provided
sensitivity: private
authority: practitioner-secondary-source
sha256: 474a64084f202c57f361e72a1140f231c3ed8e884bcaa9ef274d5fe8551ebe5d
canonical_path: /home/kina2711/PROJECT/data-trainer/Material/DE/Reference/Library/knowledge/microservices/1. Chris Richardson - Microservices Patterns_ With examples in Java (2018, Manning Publications) - libgen.li.pdf
extraction_method: pdftotext-layout-bounded-page-range
tags:
  - source/book
  - software-architecture
  - microservices
  - testing
aliases:
  - Microservices Patterns 1e
---

# Microservices Patterns — hồ sơ nguồn

## Phạm vi sử dụng

Nguồn được dùng cho hexagonal architecture, inbound/outbound port và adapter, chiến lược kiểm thử theo tầng, test double, consumer-driven contract test và cách đưa contract vào pipeline của producer. Các ví dụ Spring/Java minh họa cơ chế; note không coi framework cụ thể là yêu cầu kiến trúc.

## Provenance

- Bản PDF do chủ dự án cung cấp trong thư viện Reference của Data Engineer.
- SHA-256 được tính trực tiếp; PDF gồm 522 trang và có text layer.
- Nội dung trang bản quyền ghi Chris Richardson, Manning Publications, 2018.
- Metadata PDF không có title/author và producer ghi `Foxebook.net`; byte identity với bản Manning chính thức chưa được xác minh.
- Không sao chép PDF vào vault và không tái phân phối công khai.

## Phạm vi đã đọc

- Hexagonal architecture, ports, inbound/outbound adapters và testability: PDF 68–73.
- Testing strategy, test double, test pyramid và consumer-driven contract testing: PDF 321–348.
- Consumer/provider integration tests cho REST và messaging: PDF 353–360.
- Monolithic architecture, microservice trade-offs, decomposition và database ownership: PDF 32–55, 81–95.
- Local ACID transaction, giới hạn của transaction qua nhiều service, saga và compensating transaction: PDF 140–149, trang in 110–119.
- Transactional outbox, polling publisher, transaction-log tailing, at-least-once delivery và yêu cầu consumer idempotent: PDF 120–139, trang in 90–109.
- 111/111 trang duy nhất trong các phạm vi trên có text trích xuất được.

## Giới hạn

- Sách đặt ví dụ trong kiến trúc microservice; nhiều nguyên tắc vẫn dùng được trong modular monolith nhưng phần ánh xạ đó là tổng hợp của chương trình.
- Spring Cloud Contract và Java là implementation examples, không phải lựa chọn bắt buộc.
- Contract example không thay thế semantic validation hoặc kiểm thử business logic của provider.

## Note dẫn xuất

- [[Ports and Adapters in a Data Pipeline|Ports và adapters trong một pipeline dữ liệu]]
- [[Test Strategy and Test Double Placement|Chiến lược kiểm thử và vị trí đặt test double]]
- [[Consumer-Provider Contract Testing|Kiểm thử hợp đồng giữa producer và consumer]]
- [[Monolith Modular Monolith and the Cost of Splitting|Monolith, modular monolith và chi phí tách dịch vụ]]
- [[Transaction Boundaries and the Unit of Work|Ranh giới giao dịch và Unit of Work]]
- [[Transactional Outbox - One Atomic Write|Transactional outbox — một lần ghi nguyên tử]]

## Liên kết về source note của dự án

- `Material/DE/Reference/Library/Source-Notes/PACK-SOFTWARE-DESIGN-BOOK-01.md`
