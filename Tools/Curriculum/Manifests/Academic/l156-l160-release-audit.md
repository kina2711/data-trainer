# L156–L160 release audit

## Phạm vi

- Bài 156–160: Phase 5, Module 11.
- Atomic tasks: `book-fold-into-existing-system`, `brain-build-atomic-knowledge-note`.
- Primary deliverable: năm knowledge note tiếng Việt, năm Wiki notes byte-identical, năm cặp `note.md`/`after-note.md`.

## Nguồn và thay đổi học thuật

Phạm vi trang và web locator nằm trong `l156-l160-source-reading.json`. Batch dùng Kimball–Ross, Adamson và Silberschatz; temporal semantics được đối chiếu Microsoft, OBT được giới hạn bởi tài liệu BigQuery, Data Vault được đối chiếu Data Vault Alliance và Datavault Builder.

- Role-playing, junk, degenerate và bridge được tách theo bốn failure mode; bridge có allocation/impact-only contract và control-total check.
- SCD Type 2 có no-overlap và exactly-one-current invariants; numbering sau Type 3 được ghi là không hoàn toàn thống nhất.
- Valid time và system time được tách; correction, late-known fact và restatement policy có provenance/decision owner.
- Star, snowflake và OBT được so trên performance, storage, changeability và usability; BigQuery guidance không bị khái quát thành quy tắc chung.
- Data Vault chỉ đến mức nhận diện Hub–Link–Satellite, Raw/Business/Information Mart và chi phí phù hợp; không tuyên bố năng lực triển khai.

## Kiểm chứng

- Generator check: `checked=20 stale=0`.
- Batch validator: `PASS lessons=5 curriculum_files=10 knowledge_notes=5 min_words=2200 wiki_parity=5/5`.
- Formatter: `checked=229 failed=0`.
- Whole-vault coverage: `checked=83 failed=0`.
- Manifest: version `1.0.31`, 61 sources, 83 notes, 296 retrieval tests.
- Năm knowledge note có 2.317–2.405 từ, tổng 11.844 từ.
- Content fingerprint trước sync: `028d297d3c97b1cb03916515f899d0c5c53859c9726ee08e942cf0734d4eec5b`.

## Scope audit

Generator chỉ ghi Reference/Wiki note, `note.md`, `after-note.md` và manifest trong allowed roots. Source records và audit artifacts thuộc scope đã khai báo. Không có code path ghi `quiz.md`, `homework.md`, `slides.md`, `lesson.yaml` hoặc `Material/DA`.

## Chưa kiểm

- Chưa chạy modeling lab, bridge allocation, SCD late-data replay, bitemporal restatement, benchmark ba layout hoặc Data Vault query lab.
- Chưa có owner semantic approval; note giữ trạng thái `review`.
- Coursera không được truy cập trong batch này theo thỏa thuận.
- Canonical Obsidian đã đồng bộ bằng `rsync -a`; manifest, năm Wiki notes và bảy source records khớp SHA-256 `13/13`.
