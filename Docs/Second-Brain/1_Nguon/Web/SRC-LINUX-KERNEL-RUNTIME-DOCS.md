---
source_id: src.docs.linux-kernel-runtime
source_type: official-documentation
title: Linux Kernel Documentation — runtime, pressure and asynchronous I/O
owner: Linux kernel documentation project
canonical_url: https://docs.kernel.org/
captured: 2026-10-02
status: active-public-source
rights: public-official-documentation
sensitivity: public
authority: authoritative-primary-source
extraction_method: bounded-web-review
tags: [source/web, linux, kernel, psi, io-uring]
---

# Linux Kernel runtime documentation — hồ sơ nguồn

## Phạm vi đã đọc

- Pressure Stall Information: `https://docs.kernel.org/accounting/psi.html`, gồm `cpu`, `memory`, `io`, trường `some`/`full`, cửa sổ trung bình và trigger.
- Userspace API và tài liệu `io_uring` được liên kết từ `docs.kernel.org`; dùng để phân biệt submission/completion model với readiness model.
- Tài liệu trace/scheduler chỉ dùng cho mental model; câu lệnh và event có sẵn phải kiểm trên kernel target.

## Giới hạn

Tài liệu kernel thay đổi theo nhánh và cấu hình build. Note không suy ra feature availability chỉ từ phiên bản kernel; cần kiểm config, permission, filesystem, driver và tool trên máy đích. Phần `io_uring` trong curriculum là awareness, không phải cam kết mọi opcode có cùng semantics hoặc support.
