# L150–L155 release audit

## Phạm vi

- Bài 150–155: Phase 5, Module 11.
- Atomic tasks: `book-fold-into-existing-system`, `brain-build-atomic-knowledge-note`.
- Primary deliverable: sáu knowledge note tiếng Việt, sáu Wiki notes byte-identical, sáu cặp `note.md`/`after-note.md`.

## Nguồn và thay đổi học thuật

Phạm vi trang nằm trong `l150-l155-source-reading.json`. Batch dùng *The Data Warehouse Toolkit* 3e làm nguồn chính cho dimensional modeling; HCMUT ER, HCMUT System Modeling, Silberschatz và DDIA làm nguồn đối chiếu cho identity, abstraction, database design và workload boundary.

- Grain được tách khỏi key; zero duplicate không được dùng để chứng minh semantics.
- Conceptual, logical và physical model được tách theo câu hỏi, audience và artifact; phép ánh xạ từ HCMUT System Modeling được ghi là synthesis.
- Surrogate key không thay business key; merge/split identity phải giữ lineage và effective time.
- Bus matrix có row là business process, không phải phòng ban; conformed dimension đòi hỏi semantic conformance.
- Accumulating snapshot được nhận diện bằng việc revisit một pipeline row, không chỉ bằng nhiều cột ngày.
- Additivity là contract theo dimension, unit, grain và cutoff; note có phản ví dụ average-of-averages và distinct-count cộng dồn.

## Kiểm chứng

- Generator check: `checked=24 stale=0`.
- Batch validator: `PASS lessons=6 curriculum_files=12 knowledge_notes=6 min_words=2200 wiki_parity=6/6`.
- Formatter: `checked=214 failed=0`.
- Whole-vault coverage: `checked=78 failed=0`.
- Manifest: version `1.0.30`, 56 sources, 78 notes, 281 retrieval tests.
- Sáu knowledge note có 2.727–3.026 từ, tổng 16.914 từ.
- Content fingerprint trước sync: `947afb32131960b3e438349a545dad078092016aa9dc7c708e9c19393e3afbc2`.

## Scope audit

Generator chỉ ghi Reference/Wiki note, `note.md`, `after-note.md` và manifest trong allowed roots. Source records và audit artifacts thuộc scope đã khai báo. Không có code path ghi `quiz.md`, `homework.md`, `slides.md`, `lesson.yaml` hoặc `Material/DA`.

## Chưa kiểm

- Chưa chạy profiling, identity merge/split, backfill, reconciliation hoặc dimensional-query lab.
- Chưa có owner semantic approval; note giữ trạng thái `review`.
- Coursera không được truy cập trong batch này theo thỏa thuận.
- Canonical Obsidian đã đồng bộ bằng `rsync -a`; manifest, sáu Wiki notes và năm source records khớp SHA-256 `12/12`.
