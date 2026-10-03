# L201–L205 release audit

## Phạm vi

- L201: capstone customer-health data product với tám artifacts và bốn automatic-fail gates.
- L202: Gate 5 gồm grain, independent oracle, fanout, compatibility, self-service và traceability.
- L203: phân loại OLTP/OLAP/HTAP bằng workload shape có unit.
- L204: cô lập row/column layout khỏi compression, pruning, cache và engine differences.
- L205: dictionary, RLE, bit packing, delta, null representation và block codec.

## Kiểm tra đã chạy

- Generator: `checked=20 stale=0`.
- Batch validator: `PASS lessons=5 curriculum_files=10 knowledge_notes=5 min_words=2200 wiki_parity=5/5`.
- Formatter: `checked=351 failed=0`.
- Whole-vault coverage: `checked=128 failed=0`.
- Word counts: 3053, 2884, 2913, 2932, 3014.
- Manifest: version `1.0.40`, 93 sources, 128 notes, 431 retrieval tests.

## Ranh giới học thuật đã giữ

- Hai vòng usability có ba số cải thiện chỉ là gate học tập; không chứng minh causal effect hoặc population improvement.
- Gate 5 dùng oracle do examiner viết độc lập; generated SQL hoặc compiler pass không tự chứng minh metric đúng.
- OLTP và OLAP được trình bày như workload profiles, không phải thuộc tính cố định của tên sản phẩm.
- Read replica chỉ tách một phần resource contention; lag, WAL retention và failover vẫn cần đo.
- Ba trên một trăm columns không đồng nghĩa đọc ba phần trăm bytes.
- Column store không mặc nhiên rewrite mọi column file khi update một row; delta/update/merge path phụ thuộc engine.
- Encoding và block compression được tách thành hai lớp.
- Dictionary, RLE, bit packing và delta đều có reversal cases; không có một encoding tốt nhất cho mọi cột.
- Kết quả C-Store và ví dụ DuckDB không được ngoại suy thành benchmark phổ quát.

## Chưa kiểm bằng thực thi

- Chưa chạy capstone với consumer đại diện hoặc hội đồng Gate 5.
- Chưa chạy independent reconciliation trên một implementation thật.
- Chưa benchmark row/column layouts với controlled engine, cache và storage counters.
- Chưa force/inspect encoding matrix và đo decode/query CPU trên fixture thật.
- Chưa có owner approval; artifacts giữ trạng thái `review`.
