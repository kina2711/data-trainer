# L171–L175 release audit

## Phạm vi

- Bài 171–175: Phase 5, Module 12.
- Atomic tasks: `book-fold-into-existing-system`, `brain-build-atomic-knowledge-note`.
- Primary deliverable: năm knowledge note tiếng Việt, năm Wiki notes byte-identical, năm cặp `note.md`/`after-note.md`.

## Nguồn và thay đổi học thuật

Phạm vi nguồn nằm trong `l171-l175-source-reading.json`.

- L171 mô tả chasm bằng multiplicity theo key, phân biệt fanout với lost population và kiểm ba cách sửa.
- L172 biến “không double count” thành hồ sơ grain/multiplicity/oracle/three-grain reconciliation có invalidation trigger.
- L173 xây compatibility matrix valid/invalid/conditional, stable reason codes và valid siblings để bắt overblocking.
- L174 dùng current MetricFlow concepts, tách current/legacy spec và tách parse, semantic validation, compile với reconciliation.
- L175 đọc generated SQL theo population, path/grain, aggregation và time/filter; tách dataflow plan khỏi warehouse execution plan.

## Kiểm chứng

- Generator check: `checked=20 stale=0`.
- Batch validator: `PASS lessons=5 curriculum_files=10 knowledge_notes=5 min_words=2200 wiki_parity=5/5 metricflow-version-boundary=checked`.
- Formatter: `checked=263 failed=0`.
- Whole-vault coverage: `checked=98 failed=0`.
- Manifest: version `1.0.34`, 65 sources, 98 notes, 341 retrieval tests.
- Năm knowledge note có 2.385–2.670 từ, tổng 12.417 từ.
- Content fingerprint trước sync: `1f1a3e1a00fcbbfc1450daa767cb7d4db62fba89a0f2110cb26b1e26ba9b6b8c`.

## Scope audit

Generator chỉ ghi năm Reference/Wiki note, `note.md`, `after-note.md` và manifest trong allowed roots. Source record dbt được bổ sung command/join locators trong scope. Không có code path ghi `quiz.md`, `homework.md`, `slides.md`, `lesson.yaml` hoặc `Material/DA`. Các thay đổi khác tồn tại trong working tree không được quy cho batch này.

## Chưa kiểm

- Chưa chạy MetricFlow, fanout fixtures, compatibility enforcement, compiled SQL hay warehouse execution plans.
- Chưa có owner semantic approval; note giữ trạng thái `review`.
- Coursera không được truy cập trong batch này theo thỏa thuận.
- Canonical Obsidian đã đồng bộ bằng `rsync -a` không xóa dữ liệu đích; checksum dry-run của toàn bộ cây nguồn không còn sai khác.
