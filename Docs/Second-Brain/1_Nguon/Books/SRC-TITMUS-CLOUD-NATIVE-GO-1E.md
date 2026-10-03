---
source_id: src.book.titmus-cloud-native-go.1e
source_type: book
title: Cloud Native Go
subtitle: Building Reliable Services in Unreliable Environments
authors:
  - Matthew A. Titmus
publisher: O'Reilly Media
edition: first-edition
published: 2021
captured: 2026-09-27
status: active-private-source
rights: copyrighted-private-owner-provided
sensitivity: private
authority: authoritative-secondary-source
sha256: bba89fa1fa9092b9043634bef78f968d02723658ff4437d2da4a60c037dba777
canonical_path: /home/kina2711/PROJECT/data-trainer/Material/DE/Reference/Library/knowledge/Go/Matthew_A_Titmus_-_Cloud_Native_Go_Building_Reliable_Services_in_Unreliable_Environments-OReilly_Media_2021/Matthew A. Titmus - Cloud Native Go_ Building Reliable Services in Unreliable Environments-O'Reilly Media (2021).pdf
extraction_method: pdftotext-layout-bounded-page-range
tags:
  - source/book
  - distributed-systems
  - resilience
  - golang
aliases:
  - Cloud Native Go
---

# Cloud Native Go — hồ sơ nguồn

## Phạm vi sử dụng

Nguồn được dùng cho stability patterns và service resilience: circuit breaker, throttle, timeout, retry/backoff/jitter, overload, load shedding và graceful degradation. Code Go trong sách là ví dụ giải thích cơ chế, không mặc nhiên là implementation dùng được ở production.

## Provenance

- Bản PDF do chủ dự án cung cấp trong thư viện Reference của Data Engineer.
- SHA-256 đã tính trực tiếp từ tệp; PDF gồm 436 trang và có text layer.
- Trang nhan đề ghi First Edition, O'Reilly Media, tháng 4 năm 2021, ISBN 978-1-492-07633-9.
- Không sao chép PDF vào vault; source record giữ locator và checksum.

## Phạm vi đã đọc

- Chapter 4, *Circuit Breaker*, trang in 77–78, PDF 99–100.
- Chapter 4, *Retry* và transient faults, trang in 83–86, PDF 105–108.
- Chapter 9, *Building for Resilience* đến *Timeouts*, trang in 268–281, PDF 290–303.
- HTTP/gRPC service, middleware, health và service lifecycle; PDF 293–323.
- Chapter 11, observability và tracing concepts, trang in 343–351, PDF 365–373; metrics, trang in 369–371, PDF 391–393; logging, trang in 387–390, PDF 409–412.
- 56/56 trang duy nhất trong các phạm vi đã dùng có text trích xuất được.

## Giới hạn

- Token-bucket và load-shedding code được tác giả ghi rõ là minh họa, có thiếu sót về concurrency, record eviction và distributed state.
- Threshold, timeout, HTTP behavior và recovery policy phải được thiết kế theo workload thực tế.
- Sách không thay tài liệu của circuit-breaker/rate-limiter library hoặc platform đang triển khai.
- Không tái phân phối PDF, hình, bảng hoặc code listing dài.

## Note dẫn xuất

- [[Rate Limiting Backpressure and Circuit Breakers Between Services|Rate limiting backpressure và circuit breaker giữa các dịch vụ]]
- [[End-to-End Request Tracing and Evidence-Based Diagnosis|Truy vết request end-to-end và chẩn đoán bằng bằng chứng]]
- [[Error Design for Data Pipelines|Thiết kế lỗi cho pipeline dữ liệu]]
- [[The Request Lifecycle End to End|Vòng đời request từ đầu đến cuối]]

## Liên kết về source note của dự án

- `Material/DE/Reference/Library/Source-Notes/PACK-SERVICE-RESILIENCE-BOOK-01.md`
