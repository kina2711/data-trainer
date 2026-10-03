# L140–L144 release audit

## Phạm vi

- Bài: 140–144, Phase 4, Module 10.
- Atomic tasks: `book-fold-into-existing-system` và `brain-build-atomic-knowledge-note`.
- Profile: `build-change`; risk: `R2-standard`.
- Primary deliverable: năm knowledge note tiếng Việt, bản Wiki byte-identical, `note.md` và `after-note.md` tương ứng.

## Nguồn đã đọc

Chi tiết page ranges nằm tại `l140-l144-source-reading.json`. Nguồn gồm Petrov, Silberschatz/Korth/Sudarshan, PostgreSQL 17.10 manual, Rogov PostgreSQL 14 Internals và DDIA 1e. Tất cả là nguồn đã có trong source registry; không thêm nguồn không rõ quyền sử dụng.

## Sửa sai học thuật quan trọng

- Không đồng nhất lock wait với deadlock; deadlock cần cycle trong wait-for graph.
- Không mô tả PostgreSQL như strict-2PL thuần; MVCC xử lý ordinary reads còn locks điều phối conflicts khác.
- Không đồng nhất dead tuples với bloat hoặc kỳ vọng routine `VACUUM` làm file nhỏ ngay.
- Tách SQL-standard isolation labels khỏi hành vi PostgreSQL: Read Uncommitted map thành Read Committed; Repeatable Read chặn phantom theo implementation nhưng vẫn có serialization anomaly.
- Không hứa synchronous replication “không mất dữ liệu” tuyệt đối; note ghi rõ acknowledgment boundary, quorum/candidate, fencing và failure model.
- Tách partitioning trong một cluster khỏi sharding qua nhiều failure/administrative domains.

## Bằng chứng kiểm

- `python3 Tools/Curriculum/Build/promote_l140_l144_notes.py --check` → `checked=20 stale=0`.
- `python3 Tools/Curriculum/Build/validate_l140_l144_notes.py` → `PASS lessons=5 files=10 knowledge_notes=5 min_words=1800 wiki_parity=5/5`.
- `python3 Tools/Curriculum/Build/format_knowledge_notes.py --check` → `checked=190 failed=0`.
- `python3 Tools/Curriculum/Build/validate_knowledge_note_coverage.py` → `checked=67 failed=0`.
- Manifest sau cập nhật: version `1.0.28`, 54 sources, 67 notes, 248 retrieval tests.
- Content fingerprint trước sync: `1a16ad3287a68429a7b74ed4337e0df779615569c5c71288065c72904d3f900e`.

## Scope audit

Generator chỉ ghi bốn nhóm đích đã khai báo: năm Reference notes, năm Wiki notes, năm `note.md`, năm `after-note.md`, và manifest Second Brain. Các source records, generator, validator và audit artifacts nằm trong allowed roots. Không có code path ghi `quiz.md`, `homework.md`, `slides.md`, `lesson.yaml` hoặc `Material/DA`.

## Điều chưa kiểm

- Chưa chạy database lab, benchmark, fault injection, failover, vacuum hay rebalance.
- Chưa có owner semantic approval; trạng thái note là `review`.
- Chưa truy cập Coursera trong batch này, đúng thỏa thuận chỉ dùng Coursera khi dựng module cụ thể.
- Canonical Obsidian đã đồng bộ bằng `rsync -a`; manifest, năm Wiki notes và năm source records khớp SHA-256 `11/11`.
