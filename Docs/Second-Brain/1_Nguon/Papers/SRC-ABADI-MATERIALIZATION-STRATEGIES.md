---
source_id: src.paper.abadi-materialization-strategies
source_type: research-paper
title: Materialization Strategies in a Column-Oriented DBMS
authors: [Daniel J. Abadi, Daniel S. Myers, David J. DeWitt, Samuel R. Madden]
venue: ICDE 2007
canonical_url: https://www.cs.umd.edu/~abadi/papers/abadiicde2007.pdf
captured: 2026-10-01
status: active-public-source
rights: IEEE-paper-public-author-copy
authority: primary-research-source
tags: [source/paper, column-store, late-materialization, positions]
---

# Materialization Strategies in a Column-Oriented DBMS — hồ sơ nguồn

## Phạm vi đã đọc

- Abstract và taxonomy về early/late materialization.
- Intermediate representations dựa trên positions và thời điểm ghép columns thành tuples.
- Trade-off theo selectivity, query shape, tuple construction, random access và compressed execution.

## Giới hạn

Late materialization không phải quy tắc luôn thắng. Kết quả phụ thuộc selectivity, số cột, joins, ordering, cache, representation và engine implementation. Paper được dùng cho mechanism và reversal cases; benchmark cụ thể không được tái sử dụng như dự báo.

## Note dẫn xuất

- [[Vectorized Execution and Late Materialization]]
