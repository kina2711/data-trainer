---
source_id: src.paper.amdahl-1967
source_type: research-paper
title: Validity of the Single Processor Approach to Achieving Large Scale Computing Capabilities
authors: [Gene M. Amdahl]
venue: AFIPS Spring Joint Computer Conference 1967
canonical_url: https://doi.org/10.1145/1465482.1465560
captured: 2026-10-01
status: active-public-source
rights: ACM-paper-classroom-use
authority: primary-research-source
tags: [source/paper, parallel-computing, strong-scaling, serial-fraction]
---

# Amdahl 1967 — hồ sơ nguồn

## Phạm vi đã đọc

- Bibliographic record, abstract và lập luận trung tâm của paper AFIPS 1967.
- Giới hạn do phần công việc không hưởng lợi từ parallel resources khi giải cùng một bài toán.
- Phân biệt giới hạn lý thuyết của mô hình với overhead truyền thông, lệch tải và scheduling quan sát trong hệ thật.

## Giới hạn

Paper không cung cấp mô hình đầy đủ cho một MPP query engine hiện đại. Công thức strong-scaling trong note là phép diễn giải có điều kiện; serial fraction suy ra từ số đo còn gộp coordinator, exchange, skew, startup và external bottlenecks.

## Note dẫn xuất

- [[MPP Strong Scaling - MIMD SPMD Batch and SIMD]]
