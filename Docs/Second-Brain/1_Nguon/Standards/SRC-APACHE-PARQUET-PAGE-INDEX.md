---
source_id: src.spec.apache-parquet-page-index
source_type: specification
title: Apache Parquet Page Index
publisher: Apache Software Foundation
canonical_url: https://parquet.apache.org/docs/file-format/pageindex/
captured: 2026-10-02
status: active-public-source
rights: Apache-2.0-public-documentation
authority: official-format-specification
tags: [source/standard, parquet, page-index, column-index, offset-index, pruning]
---

# Apache Parquet Page Index — hồ sơ nguồn

## Phạm vi đã đọc

- Page index là metadata tùy chọn của column chunk; `ColumnIndex` định vị page theo value bounds và `OffsetIndex` định vị page/row ranges.
- Mục tiêu là page skipping cho point/range/selective scans mà không buộc full scan trả thêm chi phí đọc index.
- Ordered columns có thể dùng binary search trên bounds; unordered columns cần duyệt bounds tuần tự.
- Page index không phải secondary index và không bảo đảm mọi reader triển khai hoặc sử dụng nó.

## Ranh giới diễn giải

Metadata hiện diện, metadata được reader đọc và physical I/O thực sự giảm là ba mệnh đề riêng. Bounds có thể được truncation; nulls, NaN, ordering, cache, prefetch và reader implementation ảnh hưởng kết quả. Note chỉ coi bytes/counters từ một run đã khóa cấu hình là observation.

## Note dẫn xuất

- [[Parquet Statistics and Pushdown Evidence]]
