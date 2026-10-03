---
source_id: src.book.tlpi.2010
source_type: book
title: The Linux Programming Interface
subtitle: A Linux and UNIX System Programming Handbook
authors:
  - Michael Kerrisk
publisher: No Starch Press
edition: first-edition
published: 2010
captured: 2026-09-27
status: active-private-source
rights: copyrighted-private-owner-provided
sensitivity: private
authority: authoritative-secondary-source
sha256: 99df6ce877588872fa15b63a490b9857b00d2c7a2d5ae3ceb75b9a05ff324848
canonical_path: Material/Reference_temp/The_Linux_Programming_Interface_-_Michael_Kerrisk.pdf
extraction_method: pdftotext-layout-plus-page-boundary-sampling
tags:
  - source/book
  - linux
  - operating-system
aliases:
  - TLPI
---

# The Linux Programming Interface — hồ sơ nguồn

## Phạm vi sử dụng

Nguồn dùng để xây mental model và kỹ năng lập trình hệ thống Linux/UNIX: file I/O, process, signal, thread, virtual memory, socket và event-driven I/O.

Không dùng riêng nguồn này để khẳng định hành vi hiện tại của kernel, systemd, cgroup v2, PSI, eBPF hoặc `io_uring`. Những phần phụ thuộc phiên bản phải được đối chiếu tài liệu chính thức mới.

## Provenance

- Bản PDF do chủ dự án cung cấp trong `Material/Reference_temp`.
- SHA-256 đã đối chiếu với `source-acquisition-v2.json` và tệp thực tế.
- PDF có 1.556 trang và text layer sử dụng được.
- Không sao chép PDF vào vault; `canonical_path` là đường dẫn tương đối từ gốc repository.

## Phạm vi đã đọc cho các note hiện tại

- Chapters 6–9, process address space, virtual memory, heap, users, groups và process credentials; printed pp. 113–184, PDF 157–228.
- Chapter 4, universal file I/O; printed pp. 69–87, PDF 113–131.
- Chapter 5, file I/O nâng cao, open file description, sharing và descriptor flags; printed pp. 89–110, PDF 133–154.
- Chapter 12 §12.1, `/proc/PID`; printed pp. 223–228, PDF 267–272.
- Chapter 13 §§13.2–13.3, buffering và synchronized I/O; printed pp. 237–245, PDF 281–289.
- Chapter 14, filesystem structure, inode và mount; printed pp. 251–278, PDF 295–322.
- Chapters 15 và 17, file permission, ownership, ACL và permission-checking; printed pp. 279–337, PDF 323–381.
- Chapters 20–28, signal lifecycle, process creation/termination, child monitoring, `execve()` và process-creation cost; printed pp. 395–616, PDF 439–660.
- Chapters 29–39, thread lifecycle, synchronization, scheduling, resource limit, daemon, least privilege và capability; printed pp. 617–816, PDF 661–860.
- Chapters 49–50, memory mapping và virtual-memory operations; printed pp. 1001–1041, PDF 1045–1085.
- Chapter 61 §§61.1–61.2, partial socket I/O; printed pp. 1254–1257, PDF 1298–1301.
- Chapter 63, `select`, `poll` và `epoll`; printed pp. 1325–1374, PDF 1369–1418.
- Kiểm tra lại ngày 2026-09-28: 138/138 trang PDF duy nhất trong các phạm vi trên có text; không phát hiện ký tự thay thế do lỗi giải mã.

## Quyền và giới hạn

- Đây là sách có bản quyền; quyền đọc nội bộ không đồng nghĩa quyền phát hành lại.
- Không đưa PDF, hình, bảng hoặc code listing dài lên web.
- Wiki note chỉ dùng diễn giải, mô hình tự vẽ, ví dụ tự viết và trích dẫn ngắn khi thật cần thiết.
- Các benchmark ext2 và Linux 2.6 trong sách có giá trị lịch sử, không đại diện hệ thống hiện hành.

## Note dẫn xuất

- [[File Descriptors and the Universal I-O Model in Linux|File descriptor và mô hình I-O phổ quát trong Linux]]
- [[Socket Byte Streams Framing and Partial I-O|Socket byte stream, framing và partial I/O]]

## Liên kết về source note của dự án

- `Material/DE/Reference/Library/Source-Notes/PACK-OS_NETWORK-BOOK-02.md`
