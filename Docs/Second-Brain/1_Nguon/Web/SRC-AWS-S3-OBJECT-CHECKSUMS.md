---
source_id: src.web.aws-s3-object-checksums
source_type: web-documentation
title: Amazon S3 Object Integrity Checksums
publisher: Amazon Web Services
canonical_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity-upload.html
captured: 2026-10-02
status: active-public-source
rights: public-vendor-documentation
authority: official-product-documentation
tags: [source/web, s3, checksum, integrity, multipart]
---

# Amazon S3 Object Integrity Checksums — hồ sơ nguồn

## Phạm vi đã đọc

- Client/server checksum validation on upload and stored checksum metadata.
- Full-object and composite checksum distinction for multipart objects.
- ETag limitations, including multipart ETag not being full-object MD5.
- Retrieval of checksum metadata for later integrity validation.

## Giới hạn

Transport/object integrity does not prove file-format validity, row-level correctness or batch completeness. Algorithm, checksum type, SDK behavior and encryption/versioning must be recorded.

## Note dẫn xuất

- [[File Drop Delivery and Arrival Completeness Protocol]]
- [[Landing Zone Fidelity Envelope and Metadata]]
