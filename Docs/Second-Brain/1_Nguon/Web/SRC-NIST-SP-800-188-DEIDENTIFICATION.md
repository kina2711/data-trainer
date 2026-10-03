---
source_id: src.web.nist-sp-800-188-deidentification
source_type: government-standard
title: NIST SP 800-188 - De-Identifying Government Datasets
authors: [Simson Garfinkel, Barbara Guttman, Joseph Near, Aref Dajani, Phyllis Singer]
publisher: National Institute of Standards and Technology
edition: final-2023
canonical_url: https://csrc.nist.gov/pubs/sp/800/188/final
captured: 2026-10-01
status: active
authority: government-primary-standard
rights: public-government-document
tags: [source/web, privacy, de-identification, masking, non-production-data]
---

# NIST SP 800-188 — De-Identifying Government Datasets

## Phạm vi đã đọc

Nguồn dùng để phân biệt che vài trường định danh với de-identification có đánh giá disclosure risk. NIST mô tả nhiều data-sharing models: dữ liệu đã de-identify, synthetic data, query interface có kiểm soát hoặc protected enclave; lựa chọn phụ thuộc utility và risk thay vì một phép thay chuỗi cố định.

## Locator đã dùng

- Abstract và publication metadata: mục tiêu giảm disclosure risk trong khi vẫn hỗ trợ phân tích có ý nghĩa.
- Executive guidance về data-sharing models: de-identified release, synthetic data, controlled query interface và protected enclave.
- Phần governance/risk assessment: direct identifiers, quasi-identifiers, re-identification và review trước release.

## Giới hạn

Masking direct identifiers không tự chứng minh dữ liệu non-production an toàn. Bài L196 chỉ dùng nguồn để đặt risk boundary; kỹ thuật phù hợp còn phụ thuộc threat model, population, linkage data và jurisdiction.

## Note dẫn xuất

- [[Serving, Access and Security for Consumers]]
