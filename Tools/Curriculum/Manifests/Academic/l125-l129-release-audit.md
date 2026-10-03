# DE L125–L129 release audit

## Deliverable

- 5 knowledge note tiếng Việt, tên file tiếng Anh, 1.891–2.081 từ mỗi note.
- 10 Curriculum artifacts: `note.md` và `after-note.md` cho L125–L129.
- 5 Wiki note đồng nhất byte với Reference.
- 2 source record mới; 1 source record *Mastering PostgreSQL 17* được bổ sung phạm vi đọc.
- Manifest Second Brain 1.0.25: 51 nguồn, 52 Wiki note, 203 retrieval tests.

## Semantic controls

- MERGE/UPSERT không được gọi là idempotent nếu chưa có business key, source uniqueness và side-effect contract.
- `NOT VALID`/`VALIDATE CONSTRAINT` được mô tả là cách tách validation, không phải zero-lock migration.
- Planner cost là đơn vị tương đối, không phải milliseconds.
- Không quy mọi truy vấn chậm cho optimizer/cardinality nếu chưa có evidence tại plan node.
- Ba join algorithms được trình bày theo full path, không có thuật toán thắng tuyệt đối.
- `work_mem` được ghi là budget theo operation và có thể nhân dưới concurrency.
- Extended statistics được tách thành dependencies, MCV và ndistinct cùng giới hạn áp dụng.
- Quy tắc leftmost B-tree giữ nuance skip scan của PostgreSQL 17; không dùng mệnh đề tuyệt đối “cột thứ hai không thể dùng”.
- Index-only scan cần cả coverage và heap-page visibility.
- `idx_scan = 0` chỉ tạo candidate review, không đủ để drop index.

## Validation

```text
format_knowledge_notes.py --check: checked=157 failed=0
promote_l125_l129_notes.py --check: checked=10 stale=0
validate_l125_l129_notes.py: PASS lessons=5 files=10 knowledge_notes=5
validate_knowledge_note_coverage.py: checked=52 failed=0
manifest: JSON valid; version=1.0.25 sources=51 notes=52 retrieval_tests=203
Obsidian sync: 9/9 kiểm tra checksum byte-identical giữa repo và `/media/kina2711/DATA/2026/Second_Brain`
```

## Scope audit

Trong năm lesson, chỉ `note.md` và `after-note.md` được thay đổi. Không sửa `quiz.md`, `homework.md`, `slides.md`, `lesson.yaml` hoặc cây Data Analyst. Các thay đổi còn lại nằm trong Reference, Second Brain, build/validation scripts và academic manifests đã khai trong scope contract. Những thay đổi khác đã có sẵn trong worktree không thuộc batch này.

## Giới hạn

- Chưa chạy replay/DDL lock lab, six-phenomenon engine lab, join/spill lab, three-statistics lab hoặc 50-query index benchmark trên PostgreSQL thật.
- Chưa có số liệu lock, plan, temp I/O, estimate-error hoặc read/write throughput; các yêu cầu đo nằm trong `after-note.md`.
- Nội dung engine-specific được chứng nhận cho PostgreSQL 17.10; không chứng nhận portability sang DBMS khác.
- Coursera chưa được dùng theo policy của owner.
- Nội dung ở trạng thái `review`, chờ owner duyệt ngữ nghĩa.
