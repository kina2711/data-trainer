# DE L109–L113 release audit

## Phạm vi

- Năm knowledge note tiếng Việt, tên file tiếng Anh.
- Mười file Curriculum: `note.md` và `after-note.md`.
- Năm bản Wiki đồng nhất byte với Reference.
- Bảy source record mới; một source record sách được mở rộng locator.

## Kiểm soát học thuật

- L109 chỉ hứa atomic business-write/outbox-intent và at-least-once relay; không hứa exactly-once tuyệt đối.
- L110 định nghĩa capacity theo workload + SLO + environment; soak 30 phút chỉ kết luận trong cửa sổ đo.
- L111 yêu cầu fencing cho stale worker và downstream idempotency/reconciliation cho crash-after-effect.
- L112 là assessment blueprint, không đưa nội dung mới vào bài cổng.
- L113 tách formal relation khỏi SQL bag semantics; sample chỉ bác bỏ, không chứng minh key/FD.

## Lệnh kiểm

```bash
python3 Tools/Curriculum/Build/promote_l109_l113_notes.py --check
python3 Tools/Curriculum/Build/validate_l109_l113_notes.py
python3 Tools/Curriculum/Build/format_knowledge_notes.py --check
python3 Tools/Curriculum/Build/validate_knowledge_note_coverage.py
```

## Giới hạn

- Chưa chạy lab, fault injection, load test 30 phút hoặc bài Gate trên implementation thật.
- Chưa dùng Coursera theo quy ước chỉ mở khi xây module.
- Trạng thái nội dung là `review`, chờ owner duyệt nghĩa học thuật.
