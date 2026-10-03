---
source_id: src.spec.apache-parquet-file-format
source_type: specification
title: Apache Parquet File Format
publisher: Apache Software Foundation
canonical_url: https://parquet.apache.org/docs/file-format/
captured: 2026-10-02
status: active-public-source
rights: Apache-2.0-public-documentation
authority: official-format-specification
tags: [source/standard, parquet, row-group, column-chunk, page, footer]
---

# Apache Parquet File Format — hồ sơ nguồn

## Phạm vi đã đọc

- File layout: magic bytes, column chunks, footer metadata, footer length và magic bytes cuối tệp.
- Quan hệ giữa file, row group, column chunk và page; footer giữ vị trí các column chunk.
- Configuration guidance cho row-group size và data-page size, gồm trade-off giữa sequential I/O, buffering, metadata overhead và độ chi tiết khi đọc.
- Logical types và nested encoding chỉ được dùng như ranh giới định dạng; hành vi engine phải kiểm riêng.

## Ranh giới diễn giải

Các kích thước được trang tài liệu đề xuất gắn với bối cảnh HDFS và không phải ngưỡng phổ quát cho object store hoặc mọi engine. Metadata cho phép reader lập kế hoạch; nó không chứng minh engine cụ thể đã thực sự pruning hay giảm physical bytes. Mọi kết luận hiệu năng trong giáo trình phải đo trên writer, reader, version và storage backend được pin.

## Note dẫn xuất

- [[Parquet File Row Group Column Chunk and Page]]
- [[Parquet Statistics and Pushdown Evidence]]
- [[Nested Timestamp and Decimal Interoperability]]
