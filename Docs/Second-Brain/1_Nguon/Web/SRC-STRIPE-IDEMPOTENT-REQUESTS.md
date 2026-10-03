---
source_id: src.web.stripe-idempotent-requests
source_type: vendor-documentation
title: Idempotent requests
publisher: Stripe
url: https://docs.stripe.com/api/idempotent_requests
captured: 2026-09-28
status: active-web-source
rights: public-web-documentation
authority: primary-vendor-documentation
tags: [source/web, api, idempotency, retry, stripe]
---

# Stripe idempotent requests — hồ sơ nguồn

## Phạm vi sử dụng

Nguồn là case study production về key do client tạo, replay status/body đầu tiên, parameter comparison, concurrent conflict và key retention. Các lựa chọn của Stripe không phải chuẩn chung.

## Kiểm chứng

- Truy cập ngày 2026-09-28.
- Tài liệu mô tả lưu status code/body của execution đầu tiên, kể cả `500`, và so tham số khi dùng lại key.
- Tài liệu cho phép loại key sau ít nhất 24 giờ; note ghi rõ đây là policy Stripe.
- Request xung đột đồng thời trước khi execution bắt đầu có thể không được lưu result và có thể retry theo contract Stripe.

## Note dẫn xuất

- [[Idempotency Keys and Deduplication State|Idempotency key và trạng thái chống trùng]]
- [[Reverse ETL and the Shadow Operational System]]
