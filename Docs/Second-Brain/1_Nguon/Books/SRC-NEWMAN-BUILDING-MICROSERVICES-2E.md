---
source_id: src.book.newman-building-microservices.2e
source_type: book
title: Building Microservices
authors:
  - Sam Newman
publisher: O'Reilly Media
edition: second-edition
published: 2021
captured: 2026-09-28
status: active-private-source
rights: copyrighted-private-owner-provided
sensitivity: private
authority: practitioner-secondary-source
sha256: ae5bfe31baa680e78f54032151ed3772bd097db2d445f462e1a512447c9f7c21
canonical_path: /home/kina2711/PROJECT/data-trainer/Material/DE/Reference/Library/knowledge/microservices/2. Building Microservices Designing Fine-Grained Systems 2nd By Sam Newman.pdf
extraction_method: pdftotext-layout-bounded-page-range
tags:
  - source/book
  - software-design
  - microservices
  - modularity
aliases:
  - Building Microservices 2e
---

# Building Microservices 2e — hồ sơ nguồn

## Phạm vi sử dụng

Nguồn được dùng cho information hiding, cohesion, coupling, quan hệ giữa cohesion và coupling, cùng các dạng domain, temporal, pass-through, common và content coupling. Chương trình dùng các khái niệm này ở cấp mô-đun trong một kho mã; nguồn còn hỗ trợ test scope, service test và consumer-driven contract. Không mặc nhiên khuyến nghị tách microservice.

## Provenance

- Bản PDF do chủ dự án cung cấp trong thư viện Reference của Data Engineer.
- SHA-256 được tính trực tiếp; PDF gồm 754 trang và có text layer.
- Trang bản quyền ghi Sam Newman, O'Reilly Media, Second Edition, tháng 8/2021.
- Tệp được tạo bằng Calibre năm 2023; tính toàn vẹn byte với ấn bản O'Reilly chưa được xác minh.
- Không sao chép PDF vào vault và không tái phân phối công khai.

## Phạm vi đã đọc

- Chapter 2: ranh giới mô-đun, information hiding, cohesion, coupling, quan hệ giữa hai đại lượng và các dạng coupling từ domain tới content coupling; PDF 56–77.
- Chapter 9: test scope, service test, end-to-end test và consumer-driven contract; PDF 353–372.
- Modular monolith, information hiding, decomposition và coupling; PDF 32–37, 56–77, 98–112.
- Compatibility, version coexistence và expand/contract; PDF 191–197.
- Build pipeline, artifact và progressive delivery; PDF 257–261, 342–347.
- 91/91 trang duy nhất trong các phạm vi khai báo có text trích xuất được.

## Giới hạn

- Taxonomy coupling được tác giả tổng hợp cho microservice từ prior art của structured design; không phải mọi dạng ánh xạ nguyên vẹn xuống import graph trong monolith.
- Một số coupling là không tránh được. Mục tiêu là giảm assumptions và change propagation, không phải đạt số cạnh bằng không.
- Ví dụ microservice chỉ được dùng như trường hợp biên rõ; `DE-L090` chưa yêu cầu phân tách dịch vụ.

## Note dẫn xuất

- [[Cohesion Coupling and Dependency Direction|Độ gắn kết độ phụ thuộc và chiều phụ thuộc]]
- [[Ports and Adapters in a Data Pipeline|Ports và adapters trong một pipeline dữ liệu]]
- [[Test Strategy and Test Double Placement|Chiến lược kiểm thử và vị trí đặt test double]]
- [[Consumer-Provider Contract Testing|Kiểm thử hợp đồng giữa producer và consumer]]
- [[Monolith Modular Monolith and the Cost of Splitting|Monolith, modular monolith và chi phí tách dịch vụ]]
- [[Delivery Project - Modular Package with a Release Path|Dự án delivery: modular package có đường phát hành]]
- [[The Request Lifecycle End to End|Vòng đời request từ đầu đến cuối]]
- [[API Contracts - Resources Errors and Versioning|Hợp đồng API: resource, lỗi và versioning]]

## Liên kết về source note của dự án

- `Material/DE/Reference/Library/Source-Notes/PACK-SOFTWARE-DESIGN-BOOK-01.md`
