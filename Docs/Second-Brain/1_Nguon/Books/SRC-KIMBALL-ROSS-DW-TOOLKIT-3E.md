---
source_id: src.book.kimball-ross-data-warehouse-toolkit.3e
source_type: book
title: The Data Warehouse Toolkit
subtitle: The Definitive Guide to Dimensional Modeling
authors: [Ralph Kimball, Margy Ross]
publisher: Wiley
edition: third
published: 2013
captured: 2026-10-01
status: active-private-source
rights: copyrighted-private-owner-provided
sensitivity: private
authority: canonical-practitioner-source
sha256: 422e1a6070547f4dd62f29e1b1b635a158a0b5b30bee965de834ac3961ce9d9b
canonical_path: /home/kina2711/PROJECT/data-trainer/Material/Reference_temp/The_Data_Warehouse_Toolkit_The_Definitive_Guide_to_Dimensional_Modeling_-_Ralph_Kimball.pdf
extraction_method: pdftotext-layout-bounded-page-range
tags: [source/book, dimensional-modeling, grain, facts, dimensions, late-arriving-data]
---

# The Data Warehouse Toolkit 3e — hồ sơ nguồn

## Phạm vi đã đọc

- Chapters 1–2, mục tiêu của dimensional model, common pitfalls và quy trình bốn bước: PDF 48–66.
- Chapter 3, surrogate keys, date dimensions và tính cộng được của facts: PDF 78–90.
- Chapter 4, enterprise data warehouse bus architecture, bus matrix và conformed dimensions: PDF 96–112.
- Chapter 5, transaction fact, periodic snapshot và accumulating snapshot: PDF 145–161.
- Chapters 4–6, SCD Types 0–6, degenerate/junk dimensions và bridge tables: PDF 115–139, 178–188.
- Chapter 11, role-playing dimensions và superdimension trade-off: PDF 245–255.
- Chapter 14, late-arriving facts/dimensions và historical corrections: PDF 280–291.
- Các phạm vi trên có text layer; locator dùng số trang PDF.

## Provenance và giới hạn

PDF do chủ dự án cung cấp để sử dụng nội bộ. Sách là nguồn chính cho quy trình dimensional modeling; quy trình bảy bước của giáo trình mở rộng quy trình bốn bước bằng identity, time/correction semantics và workload trước khi chọn phương pháp. Phần mở rộng phải được ghi là synthesis của giáo trình, không gán nguyên văn cho Kimball và Ross.

## Note dẫn xuất

- [[From requirement to model - the seven-step protocol]]
- [[Declaring the grain before the columns]]
- [[Keys - natural, surrogate and identity over time]]
- [[Dimensional modelling - facts, dimensions and the bus matrix]]
- [[Fact types - transaction, periodic and accumulating snapshot]]
- [[Additivity - additive, semi-additive and non-additive measures]]
- [[Dimension patterns - role-playing, junk, degenerate and bridge]]
- [[Slowly changing dimensions, type 0 to type 6]]
- [[Valid time, system time, corrections and restatement]]
- [[Star, snowflake and the one-big-table trade-off]]
- [[Data Vault at a level sufficient to recognise it]]
- [[Capstone - A Governed Revenue Semantic Product]]
- [[Gate 5 - Defend a Metric Definition and Prove Self-Service]]
