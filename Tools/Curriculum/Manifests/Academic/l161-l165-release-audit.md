# L161–L165 release audit

## Phạm vi

- Bài 161–165: Phase 5, cuối Module 11 và đầu Module 12.
- Atomic tasks: `book-fold-into-existing-system`, `brain-build-atomic-knowledge-note`.
- Primary deliverable: năm knowledge note tiếng Việt, năm Wiki notes byte-identical, năm cặp `note.md`/`after-note.md`.

## Nguồn và thay đổi học thuật

Phạm vi trang và web locator nằm trong `l161-l165-source-reading.json`.

- L161 tách vocabulary theo bounded context, phân tích canonical-model trap và yêu cầu contract/mapping có owner, version, compatibility.
- L162 tách late fact, early fact và late dimension change; ba meanings `not-yet-known`, `not-applicable`, `invalid/error` không bị gộp.
- L163 định nghĩa bộ bàn giao sáu phần và handover usability test dựa trên hành vi của consumer độc lập.
- L164 khóa semantic equivalence trước benchmark, dùng ma trận 4 × 4 có số đo và ba reversal triggers.
- L165 tách physical table, mart, semantic model, metric contract và consumption tool; ranh giới Module 11 → 12 được kiểm riêng.

## Kiểm chứng

- Generator check: `checked=20 stale=0`.
- Batch validator: `PASS lessons=5 curriculum_files=10 knowledge_notes=5 min_words=2200 wiki_parity=5/5 module_boundary=11-to-12`.
- Formatter: `checked=243 failed=0`.
- Whole-vault coverage: `checked=88 failed=0`.
- Manifest: version `1.0.32`, 65 sources, 88 notes, 311 retrieval tests.
- Năm knowledge note có 2.957–3.162 từ, tổng 15.285 từ.
- Content fingerprint trước sync: `cb050d9d62295372142faa8bec081039cbe3ae6efd0489ad2cfc346588cff978`.

## Scope audit

Generator chỉ ghi năm Reference/Wiki note, `note.md`, `after-note.md` và manifest trong allowed roots. Source records và audit artifacts thuộc scope đã khai báo. Không có code path ghi `quiz.md`, `homework.md`, `slides.md`, `lesson.yaml` hoặc `Material/DA`. Working tree có nhiều thay đổi tồn tại từ các đợt trước; audit này không quy chúng cho batch L161–L165.

## Chưa kiểm

- Chưa chạy lab late-data/relink, handover test với người thật, benchmark bốn models hoặc semantic-definition migration.
- Chưa có owner semantic approval; note giữ trạng thái `review`.
- Coursera không được truy cập trong batch này theo thỏa thuận.
- Canonical Obsidian đã đồng bộ bằng `rsync -a` không xóa dữ liệu đích; checksum dry-run của toàn bộ cây nguồn không còn sai khác. Mười artifact mới/chính của batch gồm manifest, năm Wiki notes và bốn source records đã nằm trong lần kiểm này.
