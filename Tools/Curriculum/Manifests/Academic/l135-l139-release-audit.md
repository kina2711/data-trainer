# DE L135–L139 release audit

## Deliverable

- 5 knowledge note tiếng Việt, tên file tiếng Anh, 1.862–2.429 từ mỗi note.
- 10 Curriculum artifacts: `note.md` và `after-note.md` cho L135–L139.
- 5 Wiki note đồng nhất byte với Reference.
- 3 source record mới và 2 source record PostgreSQL được mở rộng.
- Manifest Second Brain 1.0.27: 54 nguồn, 62 Wiki note, 233 retrieval tests.

## Phạm vi nguồn đã đọc

- *Database Internals*: PDF 117–130 và 167–210; 58/58 trang có text.
- *Designing Data-Intensive Applications*, 1e: PDF 94–106; 13/13 trang có text.
- *Database System Concepts*, 7e: PDF 2144–2192, 2418–2462, 2982–3002; 115/115 trang có text.
- *PostgreSQL 17.10 Manual*: PDF 543–550 và 918–926; 17/17 trang có text.
- *PostgreSQL 14 Internals*: PDF 164–196; 33/33 trang có text.

## Semantic controls

- Không biến “sequential writes” thành cam kết latency phổ quát; có xét filesystem, SSD FTL và multiple write streams.
- Memtable durability gắn WAL; flush publication và WAL retirement được mô tả như protocol có thứ tự.
- Tombstone chỉ được bỏ khi không còn khả năng làm phiên bản cũ hồi sinh.
- Read/write/space amplification có numerator, denominator, layer và measurement window rõ.
- Benchmark hai engine yêu cầu durability parity, cache regime và maintenance-debt drain.
- Group commit khấu hao sync cost nhưng không mặc định giảm latency từng transaction.
- Asynchronous commit được tách khỏi `fsync=off`: mất recent suffix khác corruption risk.
- Mô hình ARIES analysis/redo/undo được tách khỏi PostgreSQL: PostgreSQL crash recovery dùng REDO và MVCC status, không có pha physical UNDO cổ điển.
- Checkpoint PostgreSQL được mô tả là interval có pacing, không phải một global flush tức thời.
- ACID consistency được chia trách nhiệm giữa constraint/engine, application invariant và isolation.

## Validation

```text
format_knowledge_notes.py --check: checked=180 failed=0
promote_l135_l139_notes.py --check: checked=10 stale=0
validate_l135_l139_notes.py: PASS lessons=5 files=10 knowledge_notes=5
validate_knowledge_note_coverage.py: checked=62 failed=0
manifest: JSON valid; version=1.0.27 sources=54 notes=62 retrieval_tests=233
Obsidian sync: 11/11 checksum byte-identical giữa repo và /media/kina2711/DATA/2026/Second_Brain
```

## Scope audit

Generator chỉ ghi `note.md` và `after-note.md` của L135–L139. Không sửa `quiz.md`, `homework.md`, `slides.md`, `lesson.yaml` hoặc cây Data Analyst. Các thay đổi còn lại nằm trong Reference, Second Brain, build/validation scripts và academic manifests đã khai trong scope contract.

## Giới hạn

- Chưa chạy engine file/compaction inspection, benchmark amplification, group-commit benchmark, crash injection hoặc ACID state-machine lab.
- Chưa có số RA/WA/SA, TPS/p95, WAL sync, recovery time hoặc survived transaction count.
- So sánh engine vẫn cần chọn LSM engine/version cụ thể và khóa semantic/durability parity.
- Coursera không được dùng trong batch này theo policy của owner.
- Nội dung ở trạng thái `review`, chờ owner duyệt ngữ nghĩa.
