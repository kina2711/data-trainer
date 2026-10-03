# L191–L195 release audit

## Phạm vi

- L191: documentation hierarchy theo reader job và consumer task.
- L192: search, discovery và findability measurement.
- L193: documentation tests, mutation tests và required merge gate.
- L194: self-service evidence và enablement boundary.
- L195: task-based usability testing, formative study và benchmark boundary.

## Kiểm tra đã chạy

- Generator: `checked=20 stale=0`.
- Batch validator: `PASS lessons=5 curriculum_files=10 knowledge_notes=5 min_words=2200 wiki_parity=5/5`.
- Formatter: `checked=320 failed=0`.
- Whole-vault coverage: `checked=118 failed=0`.
- Word counts: 3204, 3130, 3083, 3087, 3017.
- Manifest: version `1.0.38`, 82 sources, 118 notes, 401 retrieval tests.

## Ranh giới học thuật đã giữ

- Bốn tầng trong L191 là curriculum synthesis; không gán nguyên văn cho Diátaxis.
- Catalog coverage, search capability, click và findability outcome được tách riêng.
- Documentation build xanh không chứng minh nội dung đúng; bốn mutations cần fail đúng rule code.
- Cấp quyền không đồng nghĩa self-service; bốn điều kiện là AND gate trong persona/task scope.
- Heuristic năm người chỉ được dùng cho formative qualitative rounds; không dùng làm population estimate hoặc chứng minh statistical improvement.
- Correct completion gồm kết quả và cách hiểu đúng; confident-wrong outcome được giữ thành failure riêng.

## Chưa kiểm bằng thực thi

- Chưa chạy timed documentation test với người lạ.
- Chưa chạy hai vòng findability test trên catalog thật.
- Chưa cấu hình documentation CI/mutation gate trong repository sản phẩm.
- Chưa diễn tập support boundary với một đội sử dụng thật.
- Chưa tuyển người, thu consent hoặc chạy hai vòng usability study.
- Chưa có owner approval; artifacts giữ trạng thái `review`.
