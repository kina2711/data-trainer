---
source_id: src.paper.gustafson-1988
source_type: research-paper
title: Reevaluating Amdahl's Law
authors: [John L. Gustafson]
venue: Communications of the ACM 31(5), 1988
canonical_url: https://doi.org/10.1145/42411.42415
captured: 2026-10-01
status: active-public-source
rights: ACM-research-paper
authority: primary-research-source
tags: [source/paper, parallel-computing, scaled-speedup, weak-scaling]
---

# Gustafson 1988 — hồ sơ nguồn

## Phạm vi đã đọc

- Bibliographic record và lập luận về scaled problem: tăng workload cùng số processor thay vì giữ workload cố định.
- Ranh giới giữa scaled speedup và strong scaling của một query/data cố định.
- Cách dùng kết quả weak-scaling để mô tả capacity, không thay thế phép đo latency fixed-work.

## Giới hạn

Scaled speedup không phủ định Amdahl; hai mô hình trả lời hai câu hỏi khác nhau. Note không gán weak-scaling gần hằng số cho engine khi chưa đo storage bandwidth, exchange, metadata và workload shape.

## Note dẫn xuất

- [[MPP Strong Scaling - MIMD SPMD Batch and SIMD]]
