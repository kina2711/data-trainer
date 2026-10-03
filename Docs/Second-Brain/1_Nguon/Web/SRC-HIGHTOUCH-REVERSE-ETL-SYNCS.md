---
source_id: src.web.hightouch-reverse-etl-syncs
source_type: vendor-documentation
title: Hightouch Reverse ETL Sync Types, Modes and CDC
publisher: Hightouch
canonical_url: https://hightouch.com/docs/syncs/types-and-modes
captured: 2026-10-01
status: active
authority: vendor-primary-documentation
rights: public-web-documentation
tags: [source/web, reverse-etl, sync, cdc, idempotency, destination]
---

# Hightouch — Reverse ETL Sync Types, Modes and CDC

## Phạm vi đã đọc

Nguồn dùng như ví dụ product về objects/events/audiences, insert/update/upsert/archive/all/snapshot/diff modes, matching keys, delete behavior và difference-based CDC. Documentation nhấn mạnh behavior thay đổi theo destination và sync family.

## Locator đã dùng

- “Sync types” và “Sync modes”: object/event/list cùng insert, update, upsert, archive, all, snapshot và diff.
- “Sync modes and change data capture”: mode quyết định operation nào được gửi.
- CDC documentation, “CDC depends on a unique primary key”: identity và hậu quả khi key đổi hoặc trùng.
- Sync overview, “Full resync prerequisites”: resync có thể tạo duplicate với insert/event/webhook modes.

## Giới hạn

Vendor docs mô tả mechanics của sản phẩm, không đặt architecture ownership, privacy purpose hoặc feedback-loop policy cho tổ chức. Idempotency còn phụ thuộc destination API, matching key, retry và side-effect semantics.

## Note dẫn xuất

- [[Reverse ETL and the Shadow Operational System]]
