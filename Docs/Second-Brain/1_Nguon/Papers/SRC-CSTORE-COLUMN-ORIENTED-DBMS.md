---
source_id: src.paper.cstore-column-oriented-dbms
source_type: research-paper
title: "C-Store: A Column-oriented DBMS"
authors: [Mike Stonebraker, Daniel J. Abadi, Adam Batkin, Xuedong Chen, Mitch Cherniack, Miguel Ferreira, Edmond Lau, Amerson Lin, Sam Madden, Elizabeth O'Neil, Pat O'Neil, Alex Rasin, Nga Tran, Stan Zdonik]
venue: VLDB 2005
canonical_url: https://web.eecs.umich.edu/~mozafari/fall2015/eecs584/papers/c-store.pdf
captured: 2026-10-01
status: active-public-source
rights: public-research-paper
authority: primary-research-source
tags: [source/paper, column-store, olap, compression, projections]
---

# C-Store — hồ sơ nguồn

## Phạm vi đã đọc

- Abstract và Section 1: workload đọc nhiều, bố cục cột, projection, coding/packing và khác biệt với hệ tối ưu ghi.
- Sections 2–3: projection, sort order, storage representation và read/write store.
- Phần compression: lựa chọn encoding theo sort order, cardinality và đặc trưng cột.
- Phần đánh giá chỉ được dùng như kết quả của prototype và cấu hình trong paper; không ngoại suy thành ưu thế phổ quát của mọi column store.

## Giới hạn

C-Store là kiến trúc nghiên cứu năm 2005. Các chi tiết về projection, transaction và write path không đại diện cho mọi engine hiện đại. Paper hỗ trợ cơ chế và trade-off; benchmark của paper không được dùng để hứa một hệ bất kỳ sẽ nhanh hơn theo cùng tỷ lệ.

## Note dẫn xuất

- [[OLTP and OLAP - Workload Before Product Name]]
- [[Row and Column Layout - Isolating Physical Layout]]
- [[Encoding and Compression - Choosing from Data Shape]]
- [[Partitioning Clustering and Sort Order]]
- [[MPP - Coordinator Fragments and Exchange]]
