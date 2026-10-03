# L216–L220 release audit

## Phạm vi

- L216: chọn analytical engine bằng workload contract, năm archetype, evidence matrix, ADR và reversal conditions.
- L217: CSV/JSON syntax, phần schema bị bỏ ngỏ, record boundary, numeric representation và silent reinterpretation.
- L218: Avro writer/reader schema resolution, defaults, aliases, logical types và object container splitting.
- L219: Protobuf field number, wire type, reserved fields, unknown fields và các lớp compatibility.
- L220: ma trận writer–reader bốn ô, transitive history, rollout, golden records, registry gate và semantic oracle.

## Kiểm tra đã chạy

- Generator: `checked=20 stale=0`.
- Batch validator: `PASS lessons=5 curriculum_files=10 knowledge_notes=5 min_words=2200 wiki_parity=5/5`.
- Formatter toàn kho: `checked=407 failed=0`.
- Whole-vault coverage: `checked=143 failed=0`.
- Word counts: 2366, 2314, 2369, 2316, 2366.
- Manifest: version `1.0.43`, 119 sources, 143 notes, 476 retrieval tests.

## Ranh giới học thuật đã giữ

- Engine được chọn từ workload contract và hard constraints; feature list không phải bằng chứng quyết định.
- CSV có convention trong RFC 4180 nhưng không mang application schema, types hay null semantics hoàn chỉnh.
- JSON number grammar không tự gây mất precision; mất mát phụ thuộc representation và conversion của reader.
- Avro default được áp dụng khi reader thiếu field; alias có hướng và mức hỗ trợ phải kiểm trên implementation.
- Avro decode thành công vẫn có thể sai nghĩa ở unit, scale, timezone hoặc định nghĩa nghiệp vụ.
- Protobuf field number là identity trên binary wire; cùng wire type không làm field-number reuse an toàn.
- Unknown fields có thể được giữ trên binary relay nhưng mất qua JSON, field-by-field copy hoặc runtime path khác.
- Registry pass chỉ là structural gate; generated-code behavior, rollout và semantic invariants cần test riêng.
- Compatibility luôn ghi rõ writer version → reader version và history window.

## Chưa kiểm bằng thực thi

- Chưa benchmark năm engine archetype trên ba workload thật.
- Chưa chạy CSV/JSON split, inference và round-trip fixtures bằng parser cụ thể.
- Chưa chạy Avro/Protobuf matrix bằng library và generated code đã pin version.
- Chưa gọi Schema Registry thật hoặc diễn tập rolling rollout/rollback.
- Chưa có owner approval; artifacts giữ trạng thái `review`.
