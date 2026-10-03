---
source_id: src.paper.monetdb-x100-hyper-pipelining
source_type: research-paper
title: "MonetDB/X100: Hyper-Pipelining Query Execution"
authors: [Peter Boncz, Marcin Zukowski, Niels Nes]
venue: CIDR 2005
canonical_url: https://cs.brown.edu/courses/cs227/archives/2008/Papers/ColumnStores/MonetDB.pdf
captured: 2026-10-01
status: active-public-source
rights: public-research-paper
authority: primary-research-source
tags: [source/paper, vectorized-execution, query-engine, cpu-cache]
---

# MonetDB/X100 — hồ sơ nguồn

## Phạm vi đã đọc

- Abstract, introduction và execution-model comparison: iterator/Volcano, full-column materialization và vectorized processing.
- Phần vector size, function-call overhead, tight loops, cache locality và type-specialized primitives.
- Phần experiment được dùng để hiểu phương pháp tách cơ chế trong hệ nghiên cứu, không dùng tỷ lệ tăng tốc làm cam kết cho engine khác.

## Giới hạn

Đây là paper năm 2005 trên hardware và prototype cụ thể. Vectorized execution trong bài là quyết định tầng engine; paper không đồng nhất vector batches với SIMD instructions. Số liệu của paper không được ngoại suy sang DuckDB, Trino hoặc workload hiện đại nếu chưa đo.

## Note dẫn xuất

- [[Vectorized Execution and Late Materialization]]
- [[Vectorized Execution Is Not SIMD]]
