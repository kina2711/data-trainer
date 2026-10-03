# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 266: dbt Artifacts Manifest Run Results and Catalog

## Mục tiêu bài học

**Năng lực cần chứng minh.** Đọc ba hiện vật để trả lời năm câu hỏi vận hành, gồm câu phân biệt chạy xong với dữ liệu đúng.

**Điều kiện hoàn thành.** Trả lời đúng ≥ 4/5 câu hỏi chỉ bằng ba hiện vật, và nơi lưu hiện vật sản xuất được thiết lập kèm chính sách giữ.

> [!abstract] Câu hỏi trung tâm
> Manifest, run results và catalog mô tả ba loại state nào, và phải join/chốt version ra sao trước khi dùng chúng làm evidence?

## 1. Artifacts không cùng một sự thật

Manifest mô tả logical project graph/config/resources tại một invocation. Run results chứa executed-node status/timing cho command cụ thể, không chứa mọi node. Catalog/metadata mô tả warehouse relations/columns/stats tại thời điểm introspection. Một model có trong manifest nhưng không executed; một relation có trong catalog nhưng code đã đổi; run success không bảo đảm catalog hiện tại. Analysis phải ghép đúng invocation/environment thay vì trộn latest files.

## 2. Manifest và unique_id

Manifest keys nodes, sources, tests, macros, exposures, parent maps và configs theo artifact schema version. `unique_id` là join key logical, nhưng relation name/database/schema còn phụ thuộc target/config. Disabled nodes và package versions ảnh hưởng graph. State comparison dùng prior manifest; file path rename có thể thay properties. Lưu dbt version, manifest schema, invocation/project IDs, git commit và target identity.

## 3. Run results chỉ phủ scope đã chạy

Mỗi result nối manifest bằng unique_id và có status, timing, adapter response/message tùy node. Nodes ngoài selection không xuất hiện; skipped/warn/error phải tách. `execution_time` không tự bằng warehouse compute time hay cost. Nhiều commands tạo nhiều run_results, và target directory có thể bị overwrite. Archive immutable artifact bundle per invocation trước bước kế tiếp.

## 4. Catalog là observed warehouse metadata

Catalog nối resources với database/schema/name, columns/types và adapter-specific stats. Nó đến từ introspection và có thể có errors/partial coverage. Catalog không nói row-level correctness hoặc lineage hoàn chỉnh. Relation may drift after generation. Compare manifest declared columns/contracts with catalog observed columns at same environment/time, nhưng không gọi mismatch là code bug trước khi loại stale artifact, grants và external changes.

## 5. Artifact join protocol

Bundle manifest, run_results, catalog/freshness, compiled SQL, invocation args, git SHA, target and generated timestamps. Validate schema versions before parsing; do not hard-code fields across versions without compatibility. Join run results to manifest by unique_id; join catalog by unique_id plus relation identity. Detect missing/extra nodes explicitly. Hash bundle and store retention/access because compiled SQL/messages may expose sensitive literals or identifiers.

## 6. Evidence lab

Create project with selected, unselected, failed, skipped and disabled nodes; generate artifacts from parse/build/docs at two commits and targets. Ask which node ran, which relation exists, what changed and what cannot be concluded. Deliberately mix bundles to make wrong answer, then enforce provenance guard. Đạt khi query/report refuses incompatible schema/invocation instead of silently joining.

## 7. Ma trận kiểm chứng từng mệnh đề

Trong `dbt Artifacts Manifest Run Results and Catalog`, mỗi claim phải nối được tới input boundary, compiled hoặc executed artifact, trạng thái trước–sau, failure signal và independent oracle. Một command kết thúc với exit code 0 không tự chứng minh dữ liệu đúng, đầy đủ hoặc phù hợp với consumer contract. Protocol nền của bài này: Dựng artifact/workflow fixture có exact versions và intervals; inject one failure or changed assumption; capture resolved graph/state/query IDs or scheduler context and compare with independent coverage oracle.

### 7.1. Artifact probe 1: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ

**Mệnh đề cần kiểm.** Artifact probe 1: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ.

**Thiết kế phép thử.** Với `Artifact probe 1: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ`, Bắt đầu bằng ca nhỏ nhất có thể làm mệnh đề sai; chỉ thêm dữ liệu sau khi failure signal đã xuất hiện đúng chỗ. Cách này phân biệt một assertion có lực với một bài demo chỉ đi qua happy path. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Artifact probe 1: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ` phải cho thấy: Giữ fixture tối thiểu, raw failure rows và câu lệnh tái hiện; ảnh chụp màn hình một trạng thái xanh không đủ. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.2. Artifact probe 2: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ

**Mệnh đề cần kiểm.** Artifact probe 2: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ.

**Thiết kế phép thử.** Với `Artifact probe 2: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ`, Giữ nguyên input rồi đổi đúng một tham số cấu hình liên quan. Nếu output đổi theo nhiều hướng cùng lúc, phép thử chưa cô lập được nguyên nhân và phải thu hẹp lại. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Artifact probe 2: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ` phải cho thấy: Báo cả giá trị trước–sau của tham số, compiled artifact và diff đầu ra để reviewer thấy biến nào thực sự đổi. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.3. Artifact probe 3: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ

**Mệnh đề cần kiểm.** Artifact probe 3: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ.

**Thiết kế phép thử.** Với `Artifact probe 3: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ`, Chạy cặp đối chứng: một input phải được chấp nhận và một input chỉ lệch tại boundary phải bị chặn hoặc được phân loại. Hai ca dùng chung code path để tránh so hai hệ thống khác nhau. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Artifact probe 3: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ` phải cho thấy: Pass khi positive control đi qua, negative control dừng đúng lớp và không có side effect ngoài scope. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.4. Artifact probe 4: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ

**Mệnh đề cần kiểm.** Artifact probe 4: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ.

**Thiết kế phép thử.** Với `Artifact probe 4: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ`, Đặt kill point ngay trước và ngay sau durable boundary. So trạng thái sau restart để biết hệ thống tạo replay có kiểm soát, silent gap hay một trạng thái nửa vời mà dashboard không báo. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Artifact probe 4: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ` phải cho thấy: Run ledger phải cho biết commit/checkpoint nào bền vững; sau rerun, key set và side-effect ledger cùng hội tụ. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.5. Artifact probe 5: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ

**Mệnh đề cần kiểm.** Artifact probe 5: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ.

**Thiết kế phép thử.** Với `Artifact probe 5: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ`, Đảo thứ tự input và thay concurrency nhưng giữ logical population. Kết quả khác nhau cho thấy thiết kế đang phụ thuộc physical order hoặc race thay vì contract đã công bố. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Artifact probe 5: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ` phải cho thấy: Hash chuẩn hóa và business totals phải giống nhau giữa các thứ tự; chênh lệch được giữ như finding, không làm tròn mất. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.6. Artifact probe 6: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ

**Mệnh đề cần kiểm.** Artifact probe 6: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ.

**Thiết kế phép thử.** Với `Artifact probe 6: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ`, Cho cùng logical identity xuất hiện hai lần: trước hết cùng payload, sau đó payload khác. Trường hợp đầu phải hội tụ; trường hợp sau phải lộ collision thay vì âm thầm chọn một bản. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Artifact probe 6: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ` phải cho thấy: Same-content replay được đếm nhưng không nhân state; different-content collision có reason code và đường xử lý riêng. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.7. Artifact probe 7: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ

**Mệnh đề cần kiểm.** Artifact probe 7: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ.

**Thiết kế phép thử.** Với `Artifact probe 7: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ`, Mở rộng fixture bằng một record tới trễ ngay trong horizon và một record nằm ngoài horizon. Ghi rõ record nào được sửa, record nào bị loại và metric nào khiến operator biết có mất coverage. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Artifact probe 7: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ` phải cho thấy: Evidence ghi accepted-late, rejected-late và oldest outstanding timestamp; thiếu một nhóm được báo là coverage gap. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.8. Artifact probe 8: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ

**Mệnh đề cần kiểm.** Artifact probe 8: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ.

**Thiết kế phép thử.** Với `Artifact probe 8: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ`, Dùng một schema change tương thích và một thay đổi phá vỡ key, type hoặc meaning. Kết quả phải chỉ ra khác biệt giữa parse được, chạy được và vẫn giữ đúng semantics. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Artifact probe 8: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ` phải cho thấy: Lưu schema trước–sau, classification, compiled SQL và target state; một migration chạy xong nhưng đổi meaning vẫn fail. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.9. Artifact probe 9: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ

**Mệnh đề cần kiểm.** Artifact probe 9: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ.

**Thiết kế phép thử.** Với `Artifact probe 9: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ`, Tạo bảng rỗng, bảng một row và bảng có duplicate bù cho missing row. Đây là ba ca dễ làm count hoặc aggregate xanh dù invariant thực tế đã hỏng. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Artifact probe 9: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ` phải cho thấy: Oracle so count, key multiset và typed hashes. Ca missing-plus-duplicate phải bị phát hiện dù tổng row count không đổi. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.10. Artifact probe 10: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ

**Mệnh đề cần kiểm.** Artifact probe 10: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ.

**Thiết kế phép thử.** Với `Artifact probe 10: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ`, Cho reviewer chỉ artifacts, không cho xem lời giải thích của tác giả. Nếu họ không dựng lại được input, decision và diff thì evidence package chưa đủ để bàn giao. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Artifact probe 10: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ` phải cho thấy: Artifact package đạt khi reviewer tái hiện đúng diff và chỉ ra được limitation mà không cần hỏi tác giả về state ẩn. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.11. Artifact probe 11: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ

**Mệnh đề cần kiểm.** Artifact probe 11: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ.

**Thiết kế phép thử.** Với `Artifact probe 11: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ`, So output với một cách tính độc lập không tái sử dụng macro, filter hoặc intermediate relation đang được kiểm. Hai phép tính dùng chung lỗi chỉ tạo sự đồng thuận giả. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Artifact probe 11: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ` phải cho thấy: Independent result phải khớp ở key/grain đã định; nếu chỉ khớp aggregate cao hơn thì drill-down chưa hoàn tất. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.12. Artifact probe 12: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ

**Mệnh đề cần kiểm.** Artifact probe 12: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ.

**Thiết kế phép thử.** Với `Artifact probe 12: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ`, Thử trên hai scope: selection hẹp dùng trong CI và population đầy đủ dùng khi phát hành. Ghi phần coverage bị bỏ qua; tốc độ của CI không được biến thành tuyên bố kiểm toàn bộ dữ liệu. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Artifact probe 12: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ` phải cho thấy: Kết quả nêu numerator, denominator và excluded nodes/partitions; không dùng từ `all` khi selection không phủ toàn graph. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.13. Artifact probe 13: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ

**Mệnh đề cần kiểm.** Artifact probe 13: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ.

**Thiết kế phép thử.** Với `Artifact probe 13: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ`, Đẩy một giá trị tới sát giới hạn precision, timezone, partition hoặc threshold. Boundary phải được viết half-open hay inclusive rõ ràng, không suy từ một ví dụ ở giữa khoảng. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Artifact probe 13: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ` phải cho thấy: Hai phía của boundary đều có expected result và raw observation. Sai đúng một đơn vị phải làm test fail có chẩn đoán. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.14. Artifact probe 14: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ

**Mệnh đề cần kiểm.** Artifact probe 14: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ.

**Thiết kế phép thử.** Với `Artifact probe 14: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ`, Thay constraint quan trọng nhất bằng giá trị đủ để decision phải đảo. Nếu thiết kế vẫn đưa cùng lựa chọn mà không giải thích, decision rule đang là khẩu hiệu chứ chưa phải rule. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Artifact probe 14: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ` phải cho thấy: ADR hoặc rule chỉ pass khi changed constraint tạo lựa chọn mới đúng như đã dự báo và reversal threshold được lưu. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.15. Artifact probe 15: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ

**Mệnh đề cần kiểm.** Artifact probe 15: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ.

**Thiết kế phép thử.** Với `Artifact probe 15: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ`, Lặp lại phép thử từ môi trường sạch bằng seed và versions đã lưu. Một kết quả chỉ tái hiện được trên workspace của tác giả không đủ làm release evidence. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `Artifact probe 15: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ` phải cho thấy: Lần chạy sạch phải tạo cùng canonical state; khác biệt do timestamp, file order hoặc generated IDs phải được loại hoặc giải thích. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

## 8. Quy trình phản biện

Áp dụng sáu bước sau cho `dbt Artifacts Manifest Run Results and Catalog`; nếu một bước không phù hợp, ghi lý do thay vì bỏ qua im lặng.

1. Với `wiki.transformation.dbt-artifacts-manifest-results-catalog`, chốt grain, identity, time boundary và consumer-visible invariant trước câu lệnh.
2. Tách parse/compile state, warehouse execution và publication state.
3. Pin dbt core, adapter, warehouse hoặc orchestrator version cùng configuration có ảnh hưởng.
4. Kiểm correctness bằng key set, typed hash và business invariant trước performance.
5. Chạy negative case, kill point hoặc changed assumption; green path đơn lẻ không đủ.
6. Phân loại source fact, project convention, curriculum synthesis và untested hypothesis.

## 9. Câu hỏi tự kiểm tra

1. `Artifact probe 1: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ` sẽ thất bại trước tiên ở boundary nào?
2. Với `Artifact probe 2: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ`, artifact nào là nguồn bằng chứng mạnh nhất?
3. Counterexample nhỏ nhất cho `Artifact probe 3: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ` gồm những row hoặc state nào?
4. `Artifact probe 4: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ` có thể xanh giả trong tình huống nào?
5. Version, adapter, timezone hoặc state nào làm `Artifact probe 5: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ` đổi nghĩa?
6. Phần nào của `Artifact probe 6: artifact type, schema/version, invocation join, missing coverage và valid conclusion phải rõ` hiện mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `dbt Artifacts Manifest Run Results and Catalog` chưa chạy trên warehouse, dbt project hoặc orchestrator production; các mục kiểm chứng vẫn là protocol và expected evidence.
- Các claim gắn `wiki.transformation.dbt-artifacts-manifest-results-catalog` phải kiểm lại theo dbt core, adapter, warehouse và scheduler version được chọn.
- Decision matrix, failure campaign và ngưỡng review là curriculum synthesis, không phải cam kết của vendor.
- Note giữ trạng thái `review` cho tới khi chủ dự án duyệt semantic meaning và learner artifact.

## Reference
1. [[SRC-DBT-ARTIFACTS]]
2. [[SRC-DBT-DOCUMENTATION]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-DBT-ARTIFACTS]] | Cơ chế, contract hoặc giới hạn liên quan | Đã đọc locator; claim theo version/configuration |
| [[SRC-DBT-DOCUMENTATION]] | Cơ chế, contract hoặc giới hạn liên quan | Đã đọc locator; claim theo version/configuration |

## Key takeaways
- Manifest là logical graph, run_results là executed invocation và catalog là observed warehouse metadata; ghép sai provenance tạo kết luận tự tin nhưng sai thời điểm.
- Với `dbt Artifacts Manifest Run Results and Catalog`, compiled intent và observed state phải được lưu tách biệt; trộn hai lớp sẽ che failure window.
- Oracle của bài phải bám câu hỏi trung tâm: Manifest, run results và catalog mô tả ba loại state nào, và phải join/chốt version ra sao trước khi dùng chúng làm evidence?
- Các source IDs `src.web.dbt-artifacts, src.web.dbt-documentation` đặt ranh giới cho claim; phần synthesis không được gán nguyên văn cho vendor.
- Trước khi lab chạy, note này là giáo trình đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.
