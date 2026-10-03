# Phase 6: Analytical Storage and Query Engines
# Module 15: File, Serialization and Open Table Formats
# Lesson 219: Protobuf Field Numbers and Wire Compatibility

## Mục tiêu bài học

**Năng lực cần chứng minh.** Xây ma trận tương thích cho bốn thay đổi và chứng minh hậu quả của việc dùng lại số hiệu trường.

**Điều kiện hoàn thành.** Dự đoán đúng cả bốn thay đổi, và ca dùng lại số hiệu cho thấy giá trị bị diễn giải sai mà không có lỗi.

> [!abstract] Câu hỏi trung tâm
> Field numbers và wire types quyết định Protobuf compatibility thế nào, kể cả khi parse không báo lỗi?

## 1. Tag là identity trên wire

Binary key combines field number and wire type; field name absent. Rename in `.proto` preserves binary wire identity when number/type unchanged, nhưng generated API, JSON/TextFormat names và reflection users có thể break. Renumber equals delete plus add. Numbers 1–15 encode compactly; optimization không bao giờ biện minh renumber deployed fields.

## 2. Wire types không phải semantic types

VARINT, I32, I64 và LEN describe encoding families. Nhiều declared types share wire type, nên reused number có thể parse bytes under wrong semantic definition without error. Same wire type is not proof of safe change. Even documented wire-compatible numeric conversions may truncate or reinterpret values. Test boundary values and application invariants, not only parser return code.

## 3. Add delete reserve

Adding a new field number is binary wire-safe under guide rules, while application exhaustive switches/defaults may still break. Deleting requires reserving number; reserve name as protection for JSON/TextFormat paths. Never unreserve/reuse. Old reader treats new field unknown; new reader sees default presence semantics for missing old data. Proto2/proto3/editions presence behavior and generated language APIs must be pinned.

## 4. Unknown fields

Modern proto3 binary messages preserve unknown fields through parse and binary reserialization, but conversion to JSON, field-by-field copy, reflection filters or older/specific runtime paths may discard them. A relay compatibility test must execute the exact parse–transform–serialize path. Unknown preservation does not mean application understands or validates the field.

## 5. oneof enum map boundaries

Moving fields into existing oneof can alter presence and clear behavior. Adding enum values may be wire-safe yet break exhaustive source code or application policy. Maps encode entry messages; changing key/value semantics needs separate analysis. Required-like application validation is outside wire format. Compatibility report separates binary wire, generated source, JSON/TextFormat and semantic layers.

## 6. Reuse failure lab

v1 encodes retired field N using old definition; v2 reuses N under another compatible wire type. Decode through v2 and show wrong value, parse error or corruption depending pair. Include old→new, new→old and relay round-trip. Reserve N then prove compiler blocks reuse. Preserve raw bytes/Protoscope, schema hashes and runtime versions. Done when silent reinterpretation is traced to tag and semantic oracle catches it.

## 7. Ma trận kiểm chứng từng mệnh đề

Mỗi claim cần fixture, versioned contract, counterexample và oracle ở đúng tầng. Parse/decode success, registry acceptance hoặc feature name không tự chứng minh semantic correctness.

### 7.1. Protobuf change 1 phải kiểm binary wire, generated API, JSON/TextFormat, relay và semantic layers

**Mệnh đề cần kiểm.** Protobuf change 1 phải kiểm binary wire, generated API, JSON/TextFormat, relay và semantic layers.

**Protocol.** Khóa source/schema versions, producer-consumer path, configuration và canonical meaning. Chạy positive, boundary và negative fixtures; lưu raw bytes/files, hashes, logs, typed output và exact failing cell. Đổi một assumption rồi ghi reversal condition.

**Bằng chứng đạt.** Kết quả structural và semantic được báo riêng, có independent oracle, repetitions khi đo performance, reviewer và limitation. Lab chưa chạy chỉ được ghi protocol, không ghi expected behavior như observation.

### 7.2. Protobuf change 2 phải kiểm binary wire, generated API, JSON/TextFormat, relay và semantic layers

**Mệnh đề cần kiểm.** Protobuf change 2 phải kiểm binary wire, generated API, JSON/TextFormat, relay và semantic layers.

**Protocol.** Khóa source/schema versions, producer-consumer path, configuration và canonical meaning. Chạy positive, boundary và negative fixtures; lưu raw bytes/files, hashes, logs, typed output và exact failing cell. Đổi một assumption rồi ghi reversal condition.

**Bằng chứng đạt.** Kết quả structural và semantic được báo riêng, có independent oracle, repetitions khi đo performance, reviewer và limitation. Lab chưa chạy chỉ được ghi protocol, không ghi expected behavior như observation.

### 7.3. Protobuf change 3 phải kiểm binary wire, generated API, JSON/TextFormat, relay và semantic layers

**Mệnh đề cần kiểm.** Protobuf change 3 phải kiểm binary wire, generated API, JSON/TextFormat, relay và semantic layers.

**Protocol.** Khóa source/schema versions, producer-consumer path, configuration và canonical meaning. Chạy positive, boundary và negative fixtures; lưu raw bytes/files, hashes, logs, typed output và exact failing cell. Đổi một assumption rồi ghi reversal condition.

**Bằng chứng đạt.** Kết quả structural và semantic được báo riêng, có independent oracle, repetitions khi đo performance, reviewer và limitation. Lab chưa chạy chỉ được ghi protocol, không ghi expected behavior như observation.

### 7.4. Protobuf change 4 phải kiểm binary wire, generated API, JSON/TextFormat, relay và semantic layers

**Mệnh đề cần kiểm.** Protobuf change 4 phải kiểm binary wire, generated API, JSON/TextFormat, relay và semantic layers.

**Protocol.** Khóa source/schema versions, producer-consumer path, configuration và canonical meaning. Chạy positive, boundary và negative fixtures; lưu raw bytes/files, hashes, logs, typed output và exact failing cell. Đổi một assumption rồi ghi reversal condition.

**Bằng chứng đạt.** Kết quả structural và semantic được báo riêng, có independent oracle, repetitions khi đo performance, reviewer và limitation. Lab chưa chạy chỉ được ghi protocol, không ghi expected behavior như observation.

### 7.5. Protobuf change 5 phải kiểm binary wire, generated API, JSON/TextFormat, relay và semantic layers

**Mệnh đề cần kiểm.** Protobuf change 5 phải kiểm binary wire, generated API, JSON/TextFormat, relay và semantic layers.

**Protocol.** Khóa source/schema versions, producer-consumer path, configuration và canonical meaning. Chạy positive, boundary và negative fixtures; lưu raw bytes/files, hashes, logs, typed output và exact failing cell. Đổi một assumption rồi ghi reversal condition.

**Bằng chứng đạt.** Kết quả structural và semantic được báo riêng, có independent oracle, repetitions khi đo performance, reviewer và limitation. Lab chưa chạy chỉ được ghi protocol, không ghi expected behavior như observation.

### 7.6. Protobuf change 6 phải kiểm binary wire, generated API, JSON/TextFormat, relay và semantic layers

**Mệnh đề cần kiểm.** Protobuf change 6 phải kiểm binary wire, generated API, JSON/TextFormat, relay và semantic layers.

**Protocol.** Khóa source/schema versions, producer-consumer path, configuration và canonical meaning. Chạy positive, boundary và negative fixtures; lưu raw bytes/files, hashes, logs, typed output và exact failing cell. Đổi một assumption rồi ghi reversal condition.

**Bằng chứng đạt.** Kết quả structural và semantic được báo riêng, có independent oracle, repetitions khi đo performance, reviewer và limitation. Lab chưa chạy chỉ được ghi protocol, không ghi expected behavior như observation.

### 7.7. Protobuf change 7 phải kiểm binary wire, generated API, JSON/TextFormat, relay và semantic layers

**Mệnh đề cần kiểm.** Protobuf change 7 phải kiểm binary wire, generated API, JSON/TextFormat, relay và semantic layers.

**Protocol.** Khóa source/schema versions, producer-consumer path, configuration và canonical meaning. Chạy positive, boundary và negative fixtures; lưu raw bytes/files, hashes, logs, typed output và exact failing cell. Đổi một assumption rồi ghi reversal condition.

**Bằng chứng đạt.** Kết quả structural và semantic được báo riêng, có independent oracle, repetitions khi đo performance, reviewer và limitation. Lab chưa chạy chỉ được ghi protocol, không ghi expected behavior như observation.

### 7.8. Protobuf change 8 phải kiểm binary wire, generated API, JSON/TextFormat, relay và semantic layers

**Mệnh đề cần kiểm.** Protobuf change 8 phải kiểm binary wire, generated API, JSON/TextFormat, relay và semantic layers.

**Protocol.** Khóa source/schema versions, producer-consumer path, configuration và canonical meaning. Chạy positive, boundary và negative fixtures; lưu raw bytes/files, hashes, logs, typed output và exact failing cell. Đổi một assumption rồi ghi reversal condition.

**Bằng chứng đạt.** Kết quả structural và semantic được báo riêng, có independent oracle, repetitions khi đo performance, reviewer và limitation. Lab chưa chạy chỉ được ghi protocol, không ghi expected behavior như observation.

### 7.9. Protobuf change 9 phải kiểm binary wire, generated API, JSON/TextFormat, relay và semantic layers

**Mệnh đề cần kiểm.** Protobuf change 9 phải kiểm binary wire, generated API, JSON/TextFormat, relay và semantic layers.

**Protocol.** Khóa source/schema versions, producer-consumer path, configuration và canonical meaning. Chạy positive, boundary và negative fixtures; lưu raw bytes/files, hashes, logs, typed output và exact failing cell. Đổi một assumption rồi ghi reversal condition.

**Bằng chứng đạt.** Kết quả structural và semantic được báo riêng, có independent oracle, repetitions khi đo performance, reviewer và limitation. Lab chưa chạy chỉ được ghi protocol, không ghi expected behavior như observation.

### 7.10. Protobuf change 10 phải kiểm binary wire, generated API, JSON/TextFormat, relay và semantic layers

**Mệnh đề cần kiểm.** Protobuf change 10 phải kiểm binary wire, generated API, JSON/TextFormat, relay và semantic layers.

**Protocol.** Khóa source/schema versions, producer-consumer path, configuration và canonical meaning. Chạy positive, boundary và negative fixtures; lưu raw bytes/files, hashes, logs, typed output và exact failing cell. Đổi một assumption rồi ghi reversal condition.

**Bằng chứng đạt.** Kết quả structural và semantic được báo riêng, có independent oracle, repetitions khi đo performance, reviewer và limitation. Lab chưa chạy chỉ được ghi protocol, không ghi expected behavior như observation.

### 7.11. Protobuf change 11 phải kiểm binary wire, generated API, JSON/TextFormat, relay và semantic layers

**Mệnh đề cần kiểm.** Protobuf change 11 phải kiểm binary wire, generated API, JSON/TextFormat, relay và semantic layers.

**Protocol.** Khóa source/schema versions, producer-consumer path, configuration và canonical meaning. Chạy positive, boundary và negative fixtures; lưu raw bytes/files, hashes, logs, typed output và exact failing cell. Đổi một assumption rồi ghi reversal condition.

**Bằng chứng đạt.** Kết quả structural và semantic được báo riêng, có independent oracle, repetitions khi đo performance, reviewer và limitation. Lab chưa chạy chỉ được ghi protocol, không ghi expected behavior như observation.

### 7.12. Protobuf change 12 phải kiểm binary wire, generated API, JSON/TextFormat, relay và semantic layers

**Mệnh đề cần kiểm.** Protobuf change 12 phải kiểm binary wire, generated API, JSON/TextFormat, relay và semantic layers.

**Protocol.** Khóa source/schema versions, producer-consumer path, configuration và canonical meaning. Chạy positive, boundary và negative fixtures; lưu raw bytes/files, hashes, logs, typed output và exact failing cell. Đổi một assumption rồi ghi reversal condition.

**Bằng chứng đạt.** Kết quả structural và semantic được báo riêng, có independent oracle, repetitions khi đo performance, reviewer và limitation. Lab chưa chạy chỉ được ghi protocol, không ghi expected behavior như observation.

### 7.13. Protobuf change 13 phải kiểm binary wire, generated API, JSON/TextFormat, relay và semantic layers

**Mệnh đề cần kiểm.** Protobuf change 13 phải kiểm binary wire, generated API, JSON/TextFormat, relay và semantic layers.

**Protocol.** Khóa source/schema versions, producer-consumer path, configuration và canonical meaning. Chạy positive, boundary và negative fixtures; lưu raw bytes/files, hashes, logs, typed output và exact failing cell. Đổi một assumption rồi ghi reversal condition.

**Bằng chứng đạt.** Kết quả structural và semantic được báo riêng, có independent oracle, repetitions khi đo performance, reviewer và limitation. Lab chưa chạy chỉ được ghi protocol, không ghi expected behavior như observation.

### 7.14. Protobuf change 14 phải kiểm binary wire, generated API, JSON/TextFormat, relay và semantic layers

**Mệnh đề cần kiểm.** Protobuf change 14 phải kiểm binary wire, generated API, JSON/TextFormat, relay và semantic layers.

**Protocol.** Khóa source/schema versions, producer-consumer path, configuration và canonical meaning. Chạy positive, boundary và negative fixtures; lưu raw bytes/files, hashes, logs, typed output và exact failing cell. Đổi một assumption rồi ghi reversal condition.

**Bằng chứng đạt.** Kết quả structural và semantic được báo riêng, có independent oracle, repetitions khi đo performance, reviewer và limitation. Lab chưa chạy chỉ được ghi protocol, không ghi expected behavior như observation.

### 7.15. Protobuf change 15 phải kiểm binary wire, generated API, JSON/TextFormat, relay và semantic layers

**Mệnh đề cần kiểm.** Protobuf change 15 phải kiểm binary wire, generated API, JSON/TextFormat, relay và semantic layers.

**Protocol.** Khóa source/schema versions, producer-consumer path, configuration và canonical meaning. Chạy positive, boundary và negative fixtures; lưu raw bytes/files, hashes, logs, typed output và exact failing cell. Đổi một assumption rồi ghi reversal condition.

**Bằng chứng đạt.** Kết quả structural và semantic được báo riêng, có independent oracle, repetitions khi đo performance, reviewer và limitation. Lab chưa chạy chỉ được ghi protocol, không ghi expected behavior như observation.

## 8. Quy trình phản biện

1. Tách syntax/wire, structural compatibility, generated API và business semantics.
2. Ghi direction bằng writer–reader versions, không chỉ dùng nhãn backward/forward.
3. Khóa canonical meaning và negative fixtures trước implementation.
4. Giữ source bytes/schema fingerprints để tái hiện.
5. Mọi default, cache, inference hoặc registry policy đều là explicit configuration.
6. Viết rollout, rollback và reversal condition trước merge.

## 9. Câu hỏi tự kiểm tra

1. Identity nằm ở name, position, field number hay stable ID?
2. Parser biết điều gì và application phải biết điều gì?
3. Cell/version nào chưa được test?
4. Decode sạch có thể sai nghĩa ở đâu?
5. Intermediate system có làm mất thông tin không?
6. Evidence nào mới là protocol?

## 10. Giới hạn và điều chưa cho phép kết luận

- Chưa chạy benchmark engine hoặc compatibility matrix bằng libraries/registry thật.
- Specifications được kiểm ngày 2026-10-01; library, generated API và registry behavior cần pin version.
- Curriculum matrices là synthesis; không gán nguyên văn cho một source.
- Note giữ trạng thái `review` tới khi chủ dự án duyệt.

## Reference
1. [[SRC-PROTOBUF-PROTO3-GUIDE]]
2. [[SRC-PROTOBUF-WIRE-ENCODING]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-PROTOBUF-PROTO3-GUIDE]] | Normative rule, architecture boundary hoặc decision evidence | Đã đọc locator; không suy ngoài phạm vi |
| [[SRC-PROTOBUF-WIRE-ENCODING]] | Normative rule, architecture boundary hoặc decision evidence | Đã đọc locator; không suy ngoài phạm vi |

## Key takeaways
- Structural success và semantic correctness là hai gates riêng.
- Writer–reader direction, version history và exact fixtures phải hiện trong evidence.
- Defaults, aliases, unknown fields và registry modes có scope cụ thể; không dùng như bảo đảm chung.
- Chưa chạy lab thì note là giáo trình/protocol, chưa phải production certification.
