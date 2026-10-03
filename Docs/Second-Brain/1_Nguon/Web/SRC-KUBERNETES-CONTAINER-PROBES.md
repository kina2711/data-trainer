---
source_id: src.web.kubernetes-container-probes
source_type: official-documentation
title: Liveness, Readiness, and Startup Probes
publisher: Kubernetes Documentation
url: https://kubernetes.io/docs/concepts/workloads/pods/probes/
captured: 2026-09-28
status: active-web-source
rights: public-web-documentation
authority: primary-project-documentation
tags: [source/web, kubernetes, startup-probe, readiness-probe, liveness-probe]
---

# Kubernetes container probes — hồ sơ nguồn

## Phạm vi sử dụng

Tài liệu được dùng để phân biệt ba tín hiệu: startup cho biết ứng dụng đã khởi động xong, readiness quyết định Pod có nên nhận traffic qua Service, còn liveness cho biết container có cần restart. Startup probe, nếu được cấu hình, trì hoãn liveness và readiness cho tới khi startup thành công.

## Kiểm chứng

- Truy cập ngày 2026-09-28.
- URL thuộc tài liệu chính thức của dự án Kubernetes.
- Cấu hình probe sai có thể gây restart cascade hoặc loại capacity khỏi Service; endpoint và threshold phải được kiểm bằng failure drill của workload thật.

## Note dẫn xuất

- [[Deployment Strategies and Rollback|Chiến lược triển khai và rollback]]
