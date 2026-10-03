# DE L120–L124 release audit

## Deliverable

- 5 knowledge note tiếng Việt, tên file tiếng Anh, 2.100–2.499 từ mỗi note.
- 10 Curriculum artifacts: `note.md` và `after-note.md` cho L120–L124.
- 5 Wiki note đồng nhất byte với Reference.
- 4 source record PostgreSQL 17 mới; tái sử dụng HCMUT SQL và các record PostgreSQL đã có.
- Manifest Second Brain 1.0.24: 49 nguồn, 47 Wiki note, 188 retrieval tests.

## Semantic controls

- Grain statement được ghi là quy tắc kiểm soát của chương trình, không phải cú pháp SQL bắt buộc.
- `COUNT(*)`, `COUNT(expression)` và `COUNT(DISTINCT expression)` được tách theo semantics NULL/duplicate.
- CTE folding/materialization chỉ được khẳng định cho PostgreSQL 17; không dùng mệnh đề “CTE luôn là optimization fence”.
- Recursive CTE tách output order khỏi evaluation order; cycle, depth và row budget được kiểm riêng.
- Truy vấn recursion cố ý không kết thúc chỉ được chạy cô lập dưới `statement_timeout`.
- Ranking functions có tie semantics và deterministic tie-break rõ.
- `lag` trên dữ liệu thưa không được gọi là kỳ lịch trước nếu chưa dựng calendar scaffold.
- `ROWS`, `RANGE`, `GROUPS`, default frame, missing, zero và not-applicable được phân biệt.

## Validation

```text
format_knowledge_notes.py --check: checked=145 failed=0
promote_l120_l124_notes.py --check: checked=10 stale=0
validate_l120_l124_notes.py: PASS lessons=5 files=10 knowledge_notes=5
validate_knowledge_note_coverage.py: checked=47 failed=0
manifest: JSON valid; version=1.0.24 sources=49 notes=47 retrieval_tests=188
Obsidian sync: 10/10 kiểm tra checksum byte-identical giữa repo và `/media/kina2711/DATA/2026/Second_Brain`
```

## Scope audit

Trong năm lesson, chỉ `note.md` và `after-note.md` được thay đổi. Không sửa `quiz.md`, `homework.md`, `slides.md`, `lesson.yaml` hoặc cây Data Analyst. Các thay đổi còn lại nằm trong Reference, Second Brain, build/validation scripts và academic manifests đã khai trong scope contract. Những thay đổi/deletion khác đã có sẵn trong worktree không thuộc batch này.

## Giới hạn

- Chưa chạy 20 aggregate queries, refactor query 80 dòng, recursion lab, ranking lab hoặc báo cáo 24 tháng trên PostgreSQL thật.
- Chưa đo execution plan/performance; mọi yêu cầu đo được đưa vào `after-note.md`.
- Chưa chứng nhận portability ngoài PostgreSQL 17.
- Coursera chưa được dùng theo policy của owner.
- Nội dung ở trạng thái `review`, chờ owner duyệt ngữ nghĩa.
