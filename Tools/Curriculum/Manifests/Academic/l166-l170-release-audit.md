# L166–L170 release audit

## Phạm vi

- Bài 166–170: Phase 5, Module 12.
- Atomic tasks: `book-fold-into-existing-system`, `brain-build-atomic-knowledge-note`.
- Primary deliverable: năm knowledge note tiếng Việt, năm Wiki notes byte-identical, năm cặp `note.md`/`after-note.md`.

## Nguồn và thay đổi học thuật

Phạm vi nguồn nằm trong `l166-l170-source-reading.json`.

- L166 chuyển câu hỏi nghiệp vụ thành contract sáu phần; phép thử so cả eligible rows và intermediate components, không chỉ final value.
- L167 mô hình hóa semantic graph, identity, cardinality và multi-path semantics; phân biệt taxonomy khái niệm với current dbt authoring spec.
- L168 tách simple, ratio, derived và cumulative metrics; ratio-of-sums và continuous time spine là invariant bắt buộc.
- L169 mã hóa additivity theo dimension, negative/valid controls, aggregate-aware routing và exact/approximate distinct boundary.
- L170 chốt timestamp role, grain, timezone, fiscal calendar, dense time spine, leap-day và partial-period policy.

## Kiểm chứng

- Generator check: `checked=20 stale=0`.
- Batch validator: `PASS lessons=5 curriculum_files=10 knowledge_notes=5 min_words=2200 wiki_parity=5/5 dbt-version-boundary=checked`.
- Formatter: `checked=253 failed=0`.
- Whole-vault coverage: `checked=93 failed=0`.
- Manifest: version `1.0.33`, 65 sources, 93 notes, 326 retrieval tests.
- Năm knowledge note có 2.871–3.116 từ, tổng 14.869 từ.
- Content fingerprint trước sync: `5a4821e794f61a3960055d5e5a86d2cbc1b04f65c1aeb6a7cbc2cc4e114b05da`.

## Scope audit

Generator chỉ ghi năm Reference/Wiki note, `note.md`, `after-note.md` và manifest trong allowed roots. Source record dbt được cập nhật phạm vi/version trong scope. Không có code path ghi `quiz.md`, `homework.md`, `slides.md`, `lesson.yaml` hoặc `Material/DA`. Working tree có các thay đổi từ những đợt khác; audit này không quy chúng cho batch L166–L170.

## Chưa kiểm

- Chưa chạy lab hai người, graph path planner, ratio/cumulative fixture, aggregation rejection hay calendar edge cases.
- Chưa có owner semantic approval; note giữ trạng thái `review`.
- Coursera không được truy cập trong batch này theo thỏa thuận.
- Canonical Obsidian đã đồng bộ bằng `rsync -a` không xóa dữ liệu đích; checksum dry-run của toàn bộ cây nguồn không còn sai khác.
