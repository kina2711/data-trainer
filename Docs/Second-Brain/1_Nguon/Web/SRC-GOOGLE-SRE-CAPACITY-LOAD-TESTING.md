---
source_id: src.web.google-sre-capacity-load-testing
source_type: web-book
title: Capacity planning and load testing in Site Reliability Engineering
publisher: Google
canonical_url: https://sre.google/sre-book/addressing-cascading-failures/
captured: 2026-09-28
status: active
authority: practitioner-primary-source
rights: public-web-book
---

# Google SRE — capacity và load testing

## Phạm vi đã đọc

Đã đọc các phần liên quan trong *Introduction*, *Addressing Cascading Failures* và *Reliable Product Launches*. Các phần này nối capacity planning với forecast nhu cầu, raw-resource capacity với service capacity, và yêu cầu load test cả giới hạn lẫn failure mode khi overload. Nguồn nhấn mạnh overload thực tế khó dự đoán chỉ bằng tính toán tĩnh.

## Locator

- https://sre.google/sre-book/introduction/
- https://sre.google/sre-book/addressing-cascading-failures/
- https://sre.google/sre-book/reliable-product-launches/

## Giới hạn

Nguồn không đặt ra một ngưỡng p99 hay CPU chung cho mọi service. Capacity trong note luôn được định nghĩa theo workload mix, SLO và resource boundary cụ thể.

## Note dẫn xuất

- [[Load Testing and Capacity Notes|Load testing và capacity note]]
