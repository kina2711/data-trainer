---
source_id: src.docs.gnu-bash-reference
source_type: official-documentation
title: GNU Bash Reference Manual
owner: Free Software Foundation
canonical_url: https://www.gnu.org/software/bash/manual/
captured: 2026-10-02
status: active-public-source
rights: public-official-documentation
sensitivity: public
authority: authoritative-primary-source
extraction_method: bounded-web-review
tags: [source/web, bash, shell, scripting]
---

# GNU Bash Reference Manual — hồ sơ nguồn

## Phạm vi đã đọc

- Shell operation, quoting, expansion, pipelines, redirection và exit status.
- `set -e`, `set -u`, `pipefail`, `trap` và các exception khiến fail-fast không vận hành như một blanket guarantee.
- POSIX mode chỉ được dùng để nêu compatibility boundary, không đồng nhất Bash script với portable POSIX shell.

## Giới hạn

Source mô tả Bash hiện hành tại thời điểm capture. Script phải khai báo interpreter và được test bằng chính shell/version đích; note không dùng `set -e` như bằng chứng thay thế explicit error handling hoặc idempotency.
