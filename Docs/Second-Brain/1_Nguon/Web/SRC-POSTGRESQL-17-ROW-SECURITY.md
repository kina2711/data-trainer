---
source_id: src.web.postgresql-17-row-security
source_type: web-documentation
title: PostgreSQL 17 — Row Security Policies
publisher: PostgreSQL Global Development Group
canonical_url: https://www.postgresql.org/docs/17/ddl-rowsecurity.html
captured: 2026-10-02
status: active
authority: official-primary-documentation
rights: public-web-documentation
tags: [source/web, postgresql, row-level-security, authorization]
---

# PostgreSQL 17 — Row Security Policies

## Phạm vi đã đọc

Đã đọc cơ chế bật row-level security, chính sách mặc định từ chối khi không có policy phù hợp, biểu thức `USING` và `WITH CHECK`, policy permissive/restrictive, vai trò có thể bypass RLS, `FORCE ROW LEVEL SECURITY`, cùng cảnh báo về covert channel và race condition khi policy tham chiếu bảng khác.

Tài liệu xác nhận một điểm quan trọng cho giáo trình: với truy vấn đọc, dòng không thỏa `USING` thường bị loại khỏi kết quả thay vì gây lỗi. Vì vậy “không nhìn thấy dòng ngoài phạm vi” và “request bị từ chối rõ ràng” là hai hành vi khác nhau, phải được đặc tả và kiểm thử riêng.

## Locator đã dùng

- Dòng 20–27: phạm vi RLS, default deny, thứ tự đánh giá, chủ sở hữu và `BYPASSRLS`.
- Dòng 33–57: cách ghép permissive/restrictive policies và ví dụ `USING`/`WITH CHECK`.
- Dòng 156–185: policy kết hợp, covert channel, chế độ báo lỗi khi kết quả bị lọc và race condition của policy lookup.

## Giới hạn

PostgreSQL là ví dụ cơ sở dữ liệu cụ thể, không đại diện cho hành vi của mọi semantic-layer product. Chính sách metric-level, cache isolation và ngăn suy luận từ aggregate là thiết kế ở tầng ứng dụng/ngữ nghĩa, không được suy trực tiếp từ tài liệu RLS này.

## Note dẫn xuất

- [[Access Control at the Semantic Layer]]
