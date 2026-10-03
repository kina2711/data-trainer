# DE L130–L134 release audit

## Deliverable

- 5 knowledge note tiếng Việt, tên file tiếng Anh, 1.812–1.887 từ mỗi note.
- 10 Curriculum artifacts: `note.md` và `after-note.md` cho L130–L134.
- 5 Wiki note đồng nhất byte với Reference.
- 2 source record được mở rộng phạm vi đọc và backlinks.
- Manifest Second Brain 1.0.26: 51 nguồn, 57 Wiki note, 218 retrieval tests.

## Phạm vi nguồn đã đọc

- *PostgreSQL 17.10 Manual*: PDF 559–580, 2018–2030, 2623–2630, 2888–2910; 66/66 trang có text.
- *Mastering PostgreSQL 17, 6th Edition*: PDF 87–112, 198–202, 223–270; 79/79 trang có text.
- *PostgreSQL 14 Internals*: PDF 60–82, 156–176, 330–458; 173/173 trang có text.
- Coursera không được dùng trong batch này theo policy của owner.

## Semantic controls

- `EXPLAIN ANALYZE` thực thi statement; plan là bằng chứng trung tâm nhưng không bao phủ pool wait, network, client fetch hoặc mọi lock wait.
- Actual rows và time được đọc cùng `loops`; không cộng time inclusive của cha và con.
- `shared read` không được đồng nhất với physical disk read vì còn OS page cache.
- PostgreSQL prepared statement được mô tả theo custom/generic plan và heuristic năm executions; không dùng mô hình “plan của giá trị đầu bị đóng băng”.
- Parameterization vẫn là kiểm soát injection khi cần plan specialization.
- Project tuning yêu cầu multiset/schema parity, evidence dossier và one-variable discipline.
- Trang PostgreSQL thông thường mặc định 8 KiB; FSM/VM là các fork riêng, không phải metadata nằm trong heap page.
- Buffer hit ratio cần ngữ cảnh workload, latency và I/O; không được gọi là chỉ số hiệu năng tối thượng.
- Insert khóa tăng dần tập trung rightmost path nhưng không mặc định chậm hơn khóa ngẫu nhiên nếu chưa đo.
- B-tree level/height, free space, fragmentation và bloat được tách thành các khái niệm khác nhau.

## Validation

```text
format_knowledge_notes.py --check: checked=167 failed=0
promote_l130_l134_notes.py --check: checked=10 stale=0
validate_l130_l134_notes.py: PASS lessons=5 files=10 knowledge_notes=5
validate_knowledge_note_coverage.py: checked=57 failed=0
manifest: JSON valid; version=1.0.26 sources=51 notes=57 retrieval_tests=218
Obsidian sync: 8/8 checksum byte-identical giữa repo và /media/kina2711/DATA/2026/Second_Brain
```

## Scope audit

Trong năm lesson, generator chỉ ghi `note.md` và `after-note.md`. Không sửa `quiz.md`, `homework.md`, `slides.md`, `lesson.yaml` hoặc cây Data Analyst. Các thay đổi còn lại nằm trong Reference, Second Brain, build/validation scripts và academic manifests đã khai trong scope contract. Những thay đổi khác có sẵn trong worktree không thuộc batch này.

## Giới hạn

- Chưa thực thi năm plan-diagnosis case, sáu sargability fixtures, tuning project, page/cache experiment hoặc B-tree load experiment trên PostgreSQL thật.
- Chưa có số đo latency, buffers, estimate error, temp I/O, B-tree height, insert throughput hoặc bloat; yêu cầu đo nằm trong `after-note.md`.
- Nội dung engine-specific được chứng nhận theo các nguồn PostgreSQL 17.10 và PostgreSQL 14 Internals; không chứng nhận portability sang DBMS khác.
- Nội dung ở trạng thái `review`, chờ owner duyệt ngữ nghĩa.
