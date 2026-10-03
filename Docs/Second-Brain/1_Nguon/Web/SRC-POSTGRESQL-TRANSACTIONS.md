---
source_id: src.web.postgresql-transactions
source_type: official-documentation
title: Transactions
publisher: PostgreSQL Global Development Group
url: https://www.postgresql.org/docs/current/tutorial-transactions.html
captured: 2026-09-28
status: active-web-source
rights: public-web-documentation
authority: primary-project-documentation
tags: [source/web, postgresql, transaction, commit, rollback, savepoint]
---

# PostgreSQL Transactions — hồ sơ nguồn

## Phạm vi sử dụng

Tài liệu được dùng để chốt semantics hiện hành của transaction block: các lệnh giữa `BEGIN` và `COMMIT` trở nên nhìn thấy như một đơn vị; `ROLLBACK` hủy thay đổi; mỗi statement ngoài block vẫn chạy trong một transaction ngầm; savepoint chỉ quay lại một phần trong transaction hiện tại.

## Kiểm chứng

- Truy cập ngày 2026-09-28; URL `current` tại thời điểm kiểm chứng trỏ tới PostgreSQL 18.
- Đây là tài liệu chính thức của dự án PostgreSQL.
- Khi chạy lab bằng PostgreSQL 17 phải đối chiếu bản tài liệu đã ghim trong PDF 17.10; note chỉ sử dụng semantics chung có mặt ở cả hai phiên bản.

## Note dẫn xuất

- [[Transaction Boundaries and the Unit of Work|Ranh giới giao dịch và Unit of Work]]
