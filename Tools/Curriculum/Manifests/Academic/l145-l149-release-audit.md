# L145–L149 release audit

## Phạm vi

- Bài 145–148: Phase 4, Module 10; bài 149: Phase 5, Module 11.
- Atomic tasks: `book-fold-into-existing-system`, `brain-build-atomic-knowledge-note`.
- Primary deliverable: năm knowledge note tiếng Việt, năm Wiki notes byte-identical, năm cặp `note.md`/`after-note.md`.

## Nguồn và thay đổi học thuật

Phạm vi trang nằm trong `l145-l149-source-reading.json`. Batch dùng PostgreSQL 17.10 manual, *Mastering PostgreSQL 17*, Rogov, Silberschatz, DDIA và thêm hồ sơ nguồn *The Data Warehouse Toolkit* 3e. L149 ghi rõ quy trình bốn bước của Kimball–Ross và đánh dấu quy trình bảy bước là synthesis của giáo trình.

- Backup được mô tả thành chuỗi capture–retain–restore–reconcile, không phải một file hoặc trạng thái job xanh.
- PITR yêu cầu base backup, WAL chain không đứt, target/timeline và validation.
- Restore drill đo RPO bằng operation ledger và RTO theo các pha, không ước lượng sau sự kiện.
- Database operations tách symptom metrics khỏi cause metrics; threshold phải dẫn từ baseline/SLO/capacity.
- Gate 4 không thêm kiến thức; critical failure ở isolation/recovery/safety không được tổng điểm che lấp.
- Modeling method nằm cuối sau process, grain, identity, time/change và workload.

## Kiểm chứng

- Generator check: `checked=20 stale=0`.
- Batch validator: `PASS lessons=5 files=10 knowledge_notes=5 min_words=1800 wiki_parity=5/5`.
- Formatter: `checked=201 failed=0`.
- Whole-vault coverage: `checked=72 failed=0`.
- Manifest: version `1.0.29`, 55 sources, 72 notes, 263 retrieval tests.
- Content fingerprint trước sync: `6e19ef3f1f6b5686a8b86cf8f0d5a8ad80897e2b0cf289aa9267d4cd3d59734e`.

## Scope audit

Generator chỉ ghi Reference/Wiki note, `note.md`, `after-note.md` và manifest trong allowed roots. Source records và audit artifacts thuộc scope đã khai báo. Không có code path ghi `quiz.md`, `homework.md`, `slides.md`, `lesson.yaml` hoặc `Material/DA`.

## Chưa kiểm

- Chưa chạy restore drill, PITR, database workload, benchmark hoặc fault injection.
- Chưa có owner semantic approval; note giữ trạng thái `review`.
- Coursera không được truy cập trong batch này theo thỏa thuận.
- Canonical Obsidian đã đồng bộ bằng `rsync -a`; manifest, năm Wiki notes và sáu source records khớp SHA-256 `12/12`.
