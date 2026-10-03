# DE L114–L119 release audit

## Deliverable

- 6 knowledge notes tiếng Việt, tên file tiếng Anh.
- 12 Curriculum artifacts: `note.md` và `after-note.md`.
- 6 Wiki notes đồng nhất byte với Reference.
- 5 source records mới; 1 source record normalization được tái sử dụng.
- Manifest Second Brain 1.0.23: 45 nguồn, 42 Wiki notes, 173 retrieval tests.

## Semantic controls

- NULL được xử lý bằng three-valued logic; không đồng nhất với zero/empty/false.
- Set relational algebra không bị đồng nhất với SQL bag/NULL semantics.
- Logical query processing không bị gọi là physical execution order.
- ER cardinality được tách khỏi participation và lifecycle policy.
- BCNF không bị mô tả là luôn tốt hơn 3NF; lossless và dependency preservation được tách.
- DISTINCT/SUM(DISTINCT) không được dùng để che join grain/fanout sai.

## Validation

```text
format_knowledge_notes.py --check: checked=131 failed=0
promote_l114_l119_notes.py --check: checked=12 stale=0
validate_l114_l119_notes.py: PASS lessons=6 files=12 knowledge_notes=6
validate_knowledge_note_coverage.py: checked=42 failed=0
manifest: JSON valid; sources=45 notes=42 retrieval_tests=173
```

## Scope audit

Trong sáu lesson, chỉ `note.md` và `after-note.md` thuộc phạm vi thay đổi. Không sửa `quiz.md`, `homework.md`, `slides.md`, `lesson.yaml` hoặc cây Data Analyst. Các thay đổi còn lại nằm trong Reference, Second Brain, build/validation scripts và academic manifests đã khai trong scope contract.

## Giới hạn

- Chưa thực thi 15-expression lab, tám negative constraints, normalization benchmark hoặc join reconciliation trên database thật.
- Chưa đo physical plan/performance; mọi yêu cầu đo nằm trong `after-note.md` để thực thi sau.
- Coursera chưa được dùng theo policy của owner.
- Nội dung ở trạng thái `review`, chờ owner semantic approval.
