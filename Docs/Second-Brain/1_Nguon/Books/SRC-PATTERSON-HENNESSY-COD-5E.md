---
source_id: src.book.patterson-hennessy-cod.5e
source_type: textbook
title: Computer Organization and Design
subtitle: The Hardware Software Interface
authors: [David A. Patterson, John L. Hennessy]
publisher: Morgan Kaufmann
edition: fifth
published: 2014
captured: 2026-10-02
status: active-private-source
rights: copyrighted-private-owner-provided
sensitivity: private
authority: academic-secondary-source
sha256: ecef083800324810f2c9fe06b5a8b52f8d4bd4e718583edb7ef5127532e7967d
canonical_path: /home/kina2711/PROJECT/data-trainer/Material/DE/Reference/Library/Computer Science/Kiến trúc máy tính - CO2007/Slide bài giảng/CS422-Computer-Architecture-ComputerOrganizationAndDesign5thEdition2014.pdf
extraction_method: pdftotext-layout-bounded-page-range
tags: [source/book, computer-architecture, memory-hierarchy, cache, simd]
---

# Computer Organization and Design 5e — hồ sơ nguồn

## Phạm vi đã đọc

- Chapter 5, locality, memory hierarchy, cache blocks, hit/miss, miss penalty và quantitative cost model; PDF 397–459.
- Section 6.3, Flynn taxonomy, SISD/MIMD/SIMD, SPMD, vector lanes, data-level parallelism và divergence; PDF 523–538.
- Phần data layout và matrix traversal được dùng để phân tích row-major/column-major cùng cache locality; PDF 240 và các ví dụ liên quan trong Chapter 5.

## Provenance và giới hạn

- PDF nằm trong thư viện học liệu do chủ dự án cung cấp; 793 trang và có text layer.
- Metadata ghi Fifth Edition, 2014; tệp từng được chỉnh bằng iTextSharp nên chưa xác minh integrity với bản phát hành gốc.
- Con số cache, lane và ISA trong ví dụ sách đã cũ; note chỉ giữ mô hình và yêu cầu đo trên target hiện tại.

## Note dẫn xuất

- [[The memory hierarchy and the cost model]]
- [[Cache lines locality and the cache cliff]]
- [[Row-major against column-major layout]]
- [[Flynn taxonomy SISD SIMD MIMD and where SPMD fits]]
- [[SIMD from lane to operator width mask tail and gather]]
