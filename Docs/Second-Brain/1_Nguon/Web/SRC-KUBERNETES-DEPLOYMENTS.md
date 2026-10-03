---
source_id: src.web.kubernetes-deployments
source_type: official-documentation
title: Deployments
publisher: Kubernetes Documentation
url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
captured: 2026-09-28
status: active-web-source
rights: public-web-documentation
authority: primary-project-documentation
tags: [source/web, kubernetes, deployment, rolling-update, rollback]
---

# Kubernetes Deployments — hồ sơ nguồn

## Phạm vi sử dụng

Tài liệu được dùng để đối chiếu cơ chế Deployment hiện hành: `RollingUpdate`, `maxUnavailable`, `maxSurge`, trạng thái rollout, revision và rollback. Rollback Deployment chỉ đưa phần Pod template về revision trước; nó không đảo ngược dữ liệu, side effect ngoài cluster hoặc thay đổi cấu hình không thuộc Pod template.

## Kiểm chứng

- Truy cập ngày 2026-09-28.
- URL thuộc tài liệu chính thức của dự án Kubernetes.
- Lab phải ghim phiên bản Kubernetes và kiểm lại tài liệu tương ứng vì API, feature state và hành vi controller có thể đổi.

## Note dẫn xuất

- [[Deployment Strategies and Rollback|Chiến lược triển khai và rollback]]
