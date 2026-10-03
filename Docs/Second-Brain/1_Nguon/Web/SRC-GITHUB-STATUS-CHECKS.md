---
source_id: src.web.github-status-checks
source_type: product-documentation
title: GitHub Status Checks
publisher: GitHub
canonical_url: https://docs.github.com/en/pull-requests/reference/status-checks
captured: 2026-10-01
status: active
authority: official-product-documentation
rights: public-web-documentation
tags: [source/web, github, ci, merge-gate, status-checks]
---

# GitHub Status Checks

## Phạm vi đã đọc

Nguồn dùng để phân biệt “đã chạy một kiểm tra” với “kiểm tra đó là cửa chặn hợp nhất”. Status checks thể hiện điều kiện của commit; khi check được đặt bắt buộc trên protected branch, pull request phải đạt trước khi merge.

## Locator đã dùng

- Phần mở đầu “Status checks”: nguồn tạo check, trạng thái và kết luận.
- Mục về required status checks: check bắt buộc phải đạt trước merge trên branch được bảo vệ.
- Phần Checks tab: quan sát check nào đã chạy và lý do pass/fail.

## Giới hạn

GitHub chỉ thực thi trạng thái gate đã cấu hình; nó không đánh giá chất lượng rule. Một check chỉ xác nhận file tồn tại vẫn có thể xanh trong khi mô tả sai, ví dụ hỏng hoặc freshness promise lệch thực tế.

## Note dẫn xuất

- [[Documentation Tests]]
