# L181–L185 release audit

## Phạm vi

- L181: architecture alternatives.
- L182: metric lifecycle and breaking migration.
- L183: ownership, failure matrix and postmortem.
- L184: governed revenue semantic product capstone.
- L185: decision-first discovery, mở Module 13.

## Kiểm tra đã chạy

- Generator check: `checked=20 stale=0`.
- Batch validator: `PASS lessons=5 modules=2 curriculum_files=10 knowledge_notes=5 min_words=2200 wiki_parity=5/5`.
- Formatter: `checked=288 failed=0`.
- Whole-vault coverage: `checked=108 failed=0`.
- Word counts: 2686, 2482, 2473, 2467, 2577.
- Module hierarchy: L181–L184 ở Module 12; L185 ở Module 13.

## Ranh giới học thuật đã giữ

- Không coi headless semantic layer là mặc định tốt hơn BI-native hoặc curated marts.
- Không gọi lock-in nếu chưa có dependency inventory và migration-cost evidence.
- Semantic-result change có thể nguy hiểm dù interface vẫn tương thích.
- Consumer approval không thay independent reconciliation.
- Blameless postmortem không loại accountability và verification của corrective actions.
- Capstone nêu rõ 270 metric-cell assertions khi 15 metrics đều áp đủ 3 grains × 6 cases.
- Decision-first discovery cho phép từ chối analytics product hoặc chuyển yêu cầu sang operational workflow.

## Chưa kiểm bằng thực thi

- Chưa chạy architecture migration rehearsal hoặc benchmark tổng chi phí.
- Chưa thực hiện parallel run/cutover/deprecation trên metric thật.
- Chưa tiêm bảy failure modes vào semantic platform.
- Chưa chạy 270 assertions, security/cache tests hoặc changed-constraint capstone defense.
- Chưa phỏng vấn người dùng thật; five-request lab vẫn là protocol.
- Chưa có owner approval; artifacts giữ trạng thái `review`.
