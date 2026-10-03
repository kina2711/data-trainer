---
source_id: src.paper.snowflake-elastic-data-warehouse
source_type: research-paper
title: The Snowflake Elastic Data Warehouse
authors: [Benoit Dageville, Thierry Cruanes, Marcin Zukowski, Vadim Antonov, Artin Avanes, Jon Bock, Jonathan Claybaugh, Daniel Engovatov, Martin Hentschel, Jiansheng Huang, Allison W. Lee, Ashish Motivala, Abdul Q. Munir, Steven Pelley, Peter Povinec, Greg Rahn, Spyridon Triantafyllis, Philipp Unterbrunner]
venue: SIGMOD 2016
canonical_url: https://www.cs.cmu.edu/~15721-f24/papers/Snowflake.pdf
captured: 2026-10-01
status: active-public-source
rights: author-public-paper-classroom-use
authority: primary-system-paper
tags: [source/paper, data-warehouse, shared-data, storage-compute-separation, cache]
---

# Snowflake Elastic Data Warehouse — hồ sơ nguồn

## Phạm vi đã đọc

- Sections 2–3: hạn chế của pure shared-nothing, separation of storage and compute, multi-cluster shared-data architecture.
- Section 3.2: virtual warehouses, elasticity, isolation, local data cache, consistent hashing và file stealing.
- Các trang 2–4: object-store latency, column-range reads, cache lifetime, resize behavior, spill và execution engine.
- Phần cloud services: metadata/catalog/optimizer là lớp dùng chung và có profile vận hành khác compute warehouse.

## Giới hạn

Paper mô tả Snowflake năm 2016, không phải hợp đồng cho mọi dịch vụ tách storage/compute hiện nay. Các tuyên bố hiệu năng trong paper không được dùng làm tỷ lệ phổ quát; lab phải đo đúng engine, phiên bản, region và cache state.

## Note dẫn xuất

- [[Shared Nothing and Separated Storage Compute]]
- [[Workload Management Concurrency and Cache]]
- [[Analytical Engine Selection ADR]]
