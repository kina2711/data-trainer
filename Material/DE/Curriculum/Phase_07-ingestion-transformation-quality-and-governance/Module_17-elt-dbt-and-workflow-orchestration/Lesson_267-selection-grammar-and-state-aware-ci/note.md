# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 267: Selection Grammar and State Aware CI

## Mục tiêu bài học

**Năng lực cần chứng minh.** Dựng tích hợp liên tục chỉ dựng phần đổi cộng hạ lưu, và chứng minh nó không bỏ sót nhờ một lần kiểm đầy đủ theo lịch.

**Điều kiện hoàn thành.** Tập nút được chọn khớp tập đúng ở cả ba thay đổi, và lần kiểm đầy đủ theo lịch bắt được lỗi do dữ liệu.

> [!abstract] Câu hỏi trung tâm
> Selection grammar, graph operators và state comparison phải kết hợp thế nào để CI nhanh nhưng không bỏ sót downstream impact hoặc trộn môi trường?

## 1. Selection là set trên graph

Methods chọn name/path/tag/config/resource/source/exposure/state; graph operators mở parents/children; set operators union/intersection/exclusion theo syntax/tool rules. Shell quoting cũng ảnh hưởng expression. Trước CI, materialize selected unique_ids bằng `ls`/artifact query và lưu list; đừng suy scope từ string nhìn có vẻ đúng. Một selector chạy được nhưng chọn zero nodes cần fail guard nếu không expected.

## 2. State cần baseline hợp lệ

`state:modified` so current project với prior manifest. Baseline phải là exact approved environment/commit/artifact schema, immutable và không nằm cùng target path mà current command sẽ overwrite. Modified semantics có subselectors and config/body/dependency nuances theo version. State nói logical change, không nói source data changed hay database drift. Record baseline SHA and generation provenance.

## 3. Graph expansion cho blast radius

Changed node thường cần tests and downstream children, nhưng `+` distance phải match risk. Macro/package/config change có fanout wider than direct model diff. Exposure ancestors giúp critical consumer path. Source freshness/data changes không hiện như code modification. Build policy maps change class to selection: docs-only, model SQL, macro, contract, seed/snapshot, project config. Không một selector phù hợp mọi PR.

## 4. Defer và mixed-environment risk

Deferral resolves unselected upstream refs to state environment when local relation absent or policy favors state. CI nhanh hơn nhưng query có thể trộn dev and production datasets, row filters, schemas or sensitive data. Multi-parent tests may cross environments. Mark every relation origin, use isolated target and approved prod-read permissions, and avoid interpreting cross-env mismatch as model bug. Ephemeral behavior requires special attention.

## 5. False negative controls

Inject changed macro used widely, rename, indirect config, disabled node, uncommitted baseline, missing upstream in dev and downstream contract break. For each, predict selection list and execute `ls` before build. Add sentinel model/test that must be selected for a known change; CI fails if not. Periodically compare slim CI with wider/full build on representative changes and track escaped failures.

## 6. CI dossier

Persist current/baseline manifests, selector expression, resolved unique_ids, deferred relation map, command args, run_results and coverage gaps. Pass requires all critical changed/affected nodes tested, no unexpected zero selection, and environment mixing documented. Runtime saving is measured but secondary to escaped-defect rate. Reversal trigger expands scope when state/baseline uncertainty or macro/global change exceeds policy.

## 7. Ma trận kiểm chứng từng mệnh đề

Trong `Selection Grammar and State Aware CI`, mỗi claim phải nối được tới input boundary, compiled hoặc executed artifact, trạng thái trước–sau, failure signal và independent oracle. Một command kết thúc với exit code 0 không tự chứng minh dữ liệu đúng, đầy đủ hoặc phù hợp với consumer contract. Protocol nền của bài này: Dựng artifact/workflow fixture có exact versions và intervals; inject one failure or changed assumption; capture resolved graph/state/query IDs or scheduler context and compare with independent coverage oracle.

### 7.1. State-CI probe 1: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ

**Mệnh đề cần kiểm.** State-CI probe 1: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ.

**Thiết kế phép thử.** Với `State-CI probe 1: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ`, Bắt đầu bằng ca nhỏ nhất có thể làm mệnh đề sai; chỉ thêm dữ liệu sau khi failure signal đã xuất hiện đúng chỗ. Cách này phân biệt một assertion có lực với một bài demo chỉ đi qua happy path. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `State-CI probe 1: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ` phải cho thấy: Giữ fixture tối thiểu, raw failure rows và câu lệnh tái hiện; ảnh chụp màn hình một trạng thái xanh không đủ. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.2. State-CI probe 2: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ

**Mệnh đề cần kiểm.** State-CI probe 2: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ.

**Thiết kế phép thử.** Với `State-CI probe 2: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ`, Giữ nguyên input rồi đổi đúng một tham số cấu hình liên quan. Nếu output đổi theo nhiều hướng cùng lúc, phép thử chưa cô lập được nguyên nhân và phải thu hẹp lại. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `State-CI probe 2: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ` phải cho thấy: Báo cả giá trị trước–sau của tham số, compiled artifact và diff đầu ra để reviewer thấy biến nào thực sự đổi. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.3. State-CI probe 3: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ

**Mệnh đề cần kiểm.** State-CI probe 3: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ.

**Thiết kế phép thử.** Với `State-CI probe 3: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ`, Chạy cặp đối chứng: một input phải được chấp nhận và một input chỉ lệch tại boundary phải bị chặn hoặc được phân loại. Hai ca dùng chung code path để tránh so hai hệ thống khác nhau. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `State-CI probe 3: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ` phải cho thấy: Pass khi positive control đi qua, negative control dừng đúng lớp và không có side effect ngoài scope. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.4. State-CI probe 4: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ

**Mệnh đề cần kiểm.** State-CI probe 4: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ.

**Thiết kế phép thử.** Với `State-CI probe 4: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ`, Đặt kill point ngay trước và ngay sau durable boundary. So trạng thái sau restart để biết hệ thống tạo replay có kiểm soát, silent gap hay một trạng thái nửa vời mà dashboard không báo. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `State-CI probe 4: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ` phải cho thấy: Run ledger phải cho biết commit/checkpoint nào bền vững; sau rerun, key set và side-effect ledger cùng hội tụ. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.5. State-CI probe 5: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ

**Mệnh đề cần kiểm.** State-CI probe 5: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ.

**Thiết kế phép thử.** Với `State-CI probe 5: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ`, Đảo thứ tự input và thay concurrency nhưng giữ logical population. Kết quả khác nhau cho thấy thiết kế đang phụ thuộc physical order hoặc race thay vì contract đã công bố. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `State-CI probe 5: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ` phải cho thấy: Hash chuẩn hóa và business totals phải giống nhau giữa các thứ tự; chênh lệch được giữ như finding, không làm tròn mất. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.6. State-CI probe 6: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ

**Mệnh đề cần kiểm.** State-CI probe 6: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ.

**Thiết kế phép thử.** Với `State-CI probe 6: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ`, Cho cùng logical identity xuất hiện hai lần: trước hết cùng payload, sau đó payload khác. Trường hợp đầu phải hội tụ; trường hợp sau phải lộ collision thay vì âm thầm chọn một bản. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `State-CI probe 6: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ` phải cho thấy: Same-content replay được đếm nhưng không nhân state; different-content collision có reason code và đường xử lý riêng. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.7. State-CI probe 7: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ

**Mệnh đề cần kiểm.** State-CI probe 7: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ.

**Thiết kế phép thử.** Với `State-CI probe 7: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ`, Mở rộng fixture bằng một record tới trễ ngay trong horizon và một record nằm ngoài horizon. Ghi rõ record nào được sửa, record nào bị loại và metric nào khiến operator biết có mất coverage. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `State-CI probe 7: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ` phải cho thấy: Evidence ghi accepted-late, rejected-late và oldest outstanding timestamp; thiếu một nhóm được báo là coverage gap. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.8. State-CI probe 8: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ

**Mệnh đề cần kiểm.** State-CI probe 8: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ.

**Thiết kế phép thử.** Với `State-CI probe 8: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ`, Dùng một schema change tương thích và một thay đổi phá vỡ key, type hoặc meaning. Kết quả phải chỉ ra khác biệt giữa parse được, chạy được và vẫn giữ đúng semantics. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `State-CI probe 8: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ` phải cho thấy: Lưu schema trước–sau, classification, compiled SQL và target state; một migration chạy xong nhưng đổi meaning vẫn fail. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.9. State-CI probe 9: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ

**Mệnh đề cần kiểm.** State-CI probe 9: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ.

**Thiết kế phép thử.** Với `State-CI probe 9: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ`, Tạo bảng rỗng, bảng một row và bảng có duplicate bù cho missing row. Đây là ba ca dễ làm count hoặc aggregate xanh dù invariant thực tế đã hỏng. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `State-CI probe 9: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ` phải cho thấy: Oracle so count, key multiset và typed hashes. Ca missing-plus-duplicate phải bị phát hiện dù tổng row count không đổi. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.10. State-CI probe 10: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ

**Mệnh đề cần kiểm.** State-CI probe 10: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ.

**Thiết kế phép thử.** Với `State-CI probe 10: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ`, Cho reviewer chỉ artifacts, không cho xem lời giải thích của tác giả. Nếu họ không dựng lại được input, decision và diff thì evidence package chưa đủ để bàn giao. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `State-CI probe 10: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ` phải cho thấy: Artifact package đạt khi reviewer tái hiện đúng diff và chỉ ra được limitation mà không cần hỏi tác giả về state ẩn. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.11. State-CI probe 11: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ

**Mệnh đề cần kiểm.** State-CI probe 11: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ.

**Thiết kế phép thử.** Với `State-CI probe 11: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ`, So output với một cách tính độc lập không tái sử dụng macro, filter hoặc intermediate relation đang được kiểm. Hai phép tính dùng chung lỗi chỉ tạo sự đồng thuận giả. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `State-CI probe 11: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ` phải cho thấy: Independent result phải khớp ở key/grain đã định; nếu chỉ khớp aggregate cao hơn thì drill-down chưa hoàn tất. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.12. State-CI probe 12: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ

**Mệnh đề cần kiểm.** State-CI probe 12: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ.

**Thiết kế phép thử.** Với `State-CI probe 12: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ`, Thử trên hai scope: selection hẹp dùng trong CI và population đầy đủ dùng khi phát hành. Ghi phần coverage bị bỏ qua; tốc độ của CI không được biến thành tuyên bố kiểm toàn bộ dữ liệu. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `State-CI probe 12: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ` phải cho thấy: Kết quả nêu numerator, denominator và excluded nodes/partitions; không dùng từ `all` khi selection không phủ toàn graph. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.13. State-CI probe 13: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ

**Mệnh đề cần kiểm.** State-CI probe 13: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ.

**Thiết kế phép thử.** Với `State-CI probe 13: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ`, Đẩy một giá trị tới sát giới hạn precision, timezone, partition hoặc threshold. Boundary phải được viết half-open hay inclusive rõ ràng, không suy từ một ví dụ ở giữa khoảng. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `State-CI probe 13: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ` phải cho thấy: Hai phía của boundary đều có expected result và raw observation. Sai đúng một đơn vị phải làm test fail có chẩn đoán. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.14. State-CI probe 14: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ

**Mệnh đề cần kiểm.** State-CI probe 14: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ.

**Thiết kế phép thử.** Với `State-CI probe 14: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ`, Thay constraint quan trọng nhất bằng giá trị đủ để decision phải đảo. Nếu thiết kế vẫn đưa cùng lựa chọn mà không giải thích, decision rule đang là khẩu hiệu chứ chưa phải rule. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `State-CI probe 14: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ` phải cho thấy: ADR hoặc rule chỉ pass khi changed constraint tạo lựa chọn mới đúng như đã dự báo và reversal threshold được lưu. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

### 7.15. State-CI probe 15: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ

**Mệnh đề cần kiểm.** State-CI probe 15: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ.

**Thiết kế phép thử.** Với `State-CI probe 15: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ`, Lặp lại phép thử từ môi trường sạch bằng seed và versions đã lưu. Một kết quả chỉ tái hiện được trên workspace của tác giả không đủ làm release evidence. Khóa versions, target và input boundary có liên quan; lưu command, compiled SQL hoặc scheduler context cùng query IDs và timestamps.

**Bằng chứng cần giữ.** Hồ sơ của `State-CI probe 15: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ` phải cho thấy: Lần chạy sạch phải tạo cùng canonical state; khác biệt do timestamp, file order hoặc generated IDs phải được loại hoặc giải thích. Nếu sandbox chưa chạy, mục này vẫn là protocol; không đổi expected result thành observation.

## 8. Quy trình phản biện

Áp dụng sáu bước sau cho `Selection Grammar and State Aware CI`; nếu một bước không phù hợp, ghi lý do thay vì bỏ qua im lặng.

1. Với `wiki.transformation.dbt-selection-state-ci`, chốt grain, identity, time boundary và consumer-visible invariant trước câu lệnh.
2. Tách parse/compile state, warehouse execution và publication state.
3. Pin dbt core, adapter, warehouse hoặc orchestrator version cùng configuration có ảnh hưởng.
4. Kiểm correctness bằng key set, typed hash và business invariant trước performance.
5. Chạy negative case, kill point hoặc changed assumption; green path đơn lẻ không đủ.
6. Phân loại source fact, project convention, curriculum synthesis và untested hypothesis.

## 9. Câu hỏi tự kiểm tra

1. `State-CI probe 1: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ` sẽ thất bại trước tiên ở boundary nào?
2. Với `State-CI probe 2: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ`, artifact nào là nguồn bằng chứng mạnh nhất?
3. Counterexample nhỏ nhất cho `State-CI probe 3: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ` gồm những row hoặc state nào?
4. `State-CI probe 4: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ` có thể xanh giả trong tình huống nào?
5. Version, adapter, timezone hoặc state nào làm `State-CI probe 5: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ` đổi nghĩa?
6. Phần nào của `State-CI probe 6: baseline provenance, selector resolution, graph impact, deferred origin và escape oracle phải rõ` hiện mới là protocol, chưa phải observation?

## 10. Giới hạn và điều chưa cho phép kết luận

- Lab của `Selection Grammar and State Aware CI` chưa chạy trên warehouse, dbt project hoặc orchestrator production; các mục kiểm chứng vẫn là protocol và expected evidence.
- Các claim gắn `wiki.transformation.dbt-selection-state-ci` phải kiểm lại theo dbt core, adapter, warehouse và scheduler version được chọn.
- Decision matrix, failure campaign và ngưỡng review là curriculum synthesis, không phải cam kết của vendor.
- Note giữ trạng thái `review` cho tới khi chủ dự án duyệt semantic meaning và learner artifact.

## Reference
1. [[SRC-DBT-STATE-SELECTION]]
2. [[SRC-DBT-ARTIFACTS]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-DBT-STATE-SELECTION]] | Cơ chế, contract hoặc giới hạn liên quan | Đã đọc locator; claim theo version/configuration |
| [[SRC-DBT-ARTIFACTS]] | Cơ chế, contract hoặc giới hạn liên quan | Đã đọc locator; claim theo version/configuration |

## Key takeaways
- State-aware CI chỉ an toàn khi baseline immutable, selection được resolve thành node list và deferred relation origins được công bố; nhanh không bù escaped impact.
- Với `Selection Grammar and State Aware CI`, compiled intent và observed state phải được lưu tách biệt; trộn hai lớp sẽ che failure window.
- Oracle của bài phải bám câu hỏi trung tâm: Selection grammar, graph operators và state comparison phải kết hợp thế nào để CI nhanh nhưng không bỏ sót downstream impact hoặc trộn môi trường?
- Các source IDs `src.web.dbt-state-selection, src.web.dbt-artifacts` đặt ranh giới cho claim; phần synthesis không được gán nguyên văn cho vendor.
- Trước khi lab chạy, note này là giáo trình đã kiểm cấu trúc và provenance, chưa phải chứng nhận production.
