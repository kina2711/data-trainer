---
source_id: src.web.aws-dms-data-validation
source_type: web-documentation
title: AWS DMS Data Validation
publisher: Amazon Web Services
canonical_url: https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Validating.html
captured: 2026-10-02
status: active-public-source
rights: public-vendor-documentation
authority: official-product-documentation
tags: [source/web, ingestion, reconciliation, validation]
---

# AWS DMS Data Validation — hồ sơ nguồn

## Phạm vi đã đọc

- So sánh từng hàng source–target, trạng thái pending, mismatched, suspended, failed và validated.
- Validation cho full load, CDC và validation-only task.
- Failure records phân biệt record diff, missing source, missing target và table warning.
- Yêu cầu key, giới hạn kiểu dữ liệu, ảnh hưởng tài nguyên và các tình huống concurrent change tạo false mismatch.
- Thread count, partitioning và revalidation có tác động đến tải nguồn/đích.

## Giới hạn

AWS DMS là một hiện thực cụ thể. Row-level equality của nó không thay thế control totals theo business grain, semantic reconciliation, boundary contract hoặc việc xác nhận những cột bị masking/không hỗ trợ.

## Note dẫn xuất

- [[Source to Landing Reconciliation]]
- [[Three Source Ingestion Capstone]]
