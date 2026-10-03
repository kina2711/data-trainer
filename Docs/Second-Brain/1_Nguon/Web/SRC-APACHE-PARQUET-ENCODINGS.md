---
source_id: src.web.apache-parquet-encodings
source_type: specification
title: Parquet Encoding Definitions
publisher: Apache Parquet
canonical_url: https://parquet.apache.org/docs/file-format/data-pages/encodings/
captured: 2026-10-01
status: active-public-source
rights: Apache-project-public-documentation
authority: official-format-specification
tags: [source/web, parquet, encoding, dictionary, rle, bit-packing, delta]
---

# Apache Parquet encodings — hồ sơ nguồn

## Phạm vi đã đọc

- Bảng supported encodings và physical types.
- Plain và dictionary encoding.
- RLE/bit-packing hybrid; bit-packed encoding cũ đã deprecated.
- Delta binary packed, delta length byte array và delta byte array.
- Header, block/miniblock, bit width, frame-of-reference và padding rules trong delta encoding.

## Ranh giới diễn giải

Đây là đặc tả biểu diễn dữ liệu, không phải benchmark. Việc một encoding được format hỗ trợ không chứng minh writer sẽ chọn nó, reader sẽ thực thi trực tiếp trên mã, hoặc nó nhanh hơn trên dataset cụ thể. Codec nén khối là lớp riêng với encoding và cần đo độc lập.

## Note dẫn xuất

- [[Encoding and Compression - Choosing from Data Shape]]
- [[Parquet File Row Group Column Chunk and Page]]
- [[Parquet Statistics and Pushdown Evidence]]
