---
source_id: src.book.mastering-postgresql-17.6e
source_type: book
title: Mastering PostgreSQL 17
authors: [Hans-Jürgen Schönig]
publisher: Packt Publishing
edition: sixth-edition
published: 2024
captured: 2026-09-28
status: active-private-source
rights: copyrighted-private-owner-provided
sensitivity: private
authority: practitioner-secondary-source
sha256: ee15cedfea766f282e6cf8aaeab4213d357f6b6dece287cb4e6077816f743be1
canonical_path: /home/kina2711/PROJECT/data-trainer/Material/DE/Reference/Library/knowledge/postgresql/Mastering PostgreSQL 17, 6th Edition{Hans-Jürgen Schönig}(2024).pdf
extraction_method: pdftotext-layout-bounded-page-range
tags: [source/book, postgresql, transaction, locking, planner, indexes, statistics]
---

# Mastering PostgreSQL 17 — hồ sơ nguồn

## Phạm vi sử dụng

Nguồn được dùng cho cơ chế transaction block của PostgreSQL, `BEGIN`/`COMMIT`/`ROLLBACK`, trạng thái aborted sau lỗi, savepoint, transactional DDL, locking và hậu quả của transaction kéo dài. Note không nâng ví dụ PostgreSQL thành quy tắc bất biến cho mọi hệ quản trị.

## Provenance

- PDF do chủ dự án cung cấp trong thư viện Reference của Data Engineer.
- SHA-256 được tính trực tiếp; PDF gồm 474 trang và có text layer.
- Metadata ghi tiêu đề *Mastering PostgreSQL 17*; tên tác giả trong metadata bị lỗi mã hóa nhưng trang sách ghi Hans-Jürgen Schönig.
- Không sao chép PDF vào vault và không tái phân phối công khai.

## Phạm vi đã đọc

- Chapter 1, `transaction_timeout` và tác động của transaction kéo dài: PDF 30–34, trang in 1–5.
- Chapter 2, transaction, error state, savepoint, transactional DDL, locking và isolation: PDF 49–62, trang in 19–32.
- Chapter 3, cost model, EXPLAIN, simple/combined/functional/partial/index-only indexes: PDF 87–112, trang in 49–74.
- Chapter 6, runtime statistics và phát hiện index ít dùng: PDF 198–202, trang in 161–164.
- Chapter 7, optimizer, statistics, plans, join ordering và planner settings: PDF 223–270, trang in 185–232.
- Chapters 9–10, logical dumps, restore, globals, base backup, replication, PITR và upgrade/monitoring concerns: PDF 345–365, 385–398.
- 97/97 trang trong các phạm vi trên có text trích xuất được.

## Giới hạn

- Sách giải thích PostgreSQL 17; hành vi ORM, pool và framework phải đối chiếu tài liệu của chính thư viện đang dùng.
- Các ngưỡng timeout, pool size và query budget trong note là quyết định theo workload, không lấy nguyên từ sách.

## Note dẫn xuất

- [[Transaction Boundaries and the Unit of Work|Ranh giới giao dịch và Unit of Work]]
- [[Inside the Engine - Parser to Executor]]
- [[Physical Operators and Join Algorithms]]
- [[Statistics Selectivity and Cardinality Estimation]]
- [[Index Structure Composite Order and Cost]]
- [[Backup, PITR and what a backup is not]]
- [[The restore drill]]
- [[Operating a database day to day]]
- [[Gate 4 - trace a write and defend an isolation choice]]
