# Phase 5: Modeling, Semantics and Analytical Product
# Module 13: Analytical Data Product and Self-service
# Lesson 201: Capstone - A Governed Customer Health Data Product

## Mục tiêu bài học

**Năng lực cần chứng minh.** Nộp sản phẩm đủ tám hạng mục, không vi phạm bốn điều kiện tự động không đạt.

**Điều kiện hoàn thành.** Tám hạng mục đầy đủ, hai vòng thử khả dụng có bốn số đo với vòng hai cải thiện ≥ 3 số, và không vi phạm bốn điều kiện tự động không đạt.

> [!abstract] Câu hỏi trung tâm
> Một customer-health data product cần những artifact, phép thử và failure gates nào để chứng minh decision traceability, semantic correctness, self-service, access control và lifecycle readiness?

## 1. Bài toán và ranh giới của sản phẩm

Capstone bắt đầu từ một quyết định có thật trong tình huống giả lập: đội Customer Success chọn tài khoản cần can thiệp trong tuần, không phải từ mong muốn tạo dashboard sức khỏe khách hàng. Product boundary ghi population là tài khoản B2B đang hoạt động, observation cutoff, excluded segments, data latency và action branches. `customer_health_score` chỉ là một tín hiệu tổng hợp; người làm phải công bố components, trọng số, missing-data behavior và nơi human review có quyền đảo kết quả. Không dùng score cho từ chối dịch vụ, định giá hoặc quyết định pháp lý nếu chưa có approval và fairness analysis tương ứng.

## 2. Tám hạng mục là một chuỗi bằng chứng

Hạng mục 1 là decision statement bốn phần và metric tree có owner ở từng lá. Hạng mục 2 là traceability matrix năm mắt từ decision đến question, concept, field/metric và test/evidence. Hạng mục 3 là contract năm phần cho product và contract sáu phần cho metric trọng yếu. Hạng mục 4 là public interface tối thiểu, gồm grain, keys, fields, time/freshness, examples và compatibility. Hạng mục 5 là documentation hierarchy với interpretation limits. Hạng mục 6 là access policy parity trên BI, SQL, API. Hạng mục 7 là hai vòng task-based usability. Hạng mục 8 là cost-to-serve cùng keep/optimize/merge/retire analysis. Thiếu một mắt xích làm bằng chứng downstream mất căn cứ.

## 3. Mô hình và ngữ nghĩa customer health

Chốt grain trước columns: một row cho account tại một snapshot cutoff hay một account-day. Events như ticket, usage và invoice phải aggregate về grain đó bằng window công bố; joins cần multiplicity proof để không nhân đôi. Metric contract nêu population, expression, time basis, exclusions, null/late-data behavior và owner. Health score version là public semantic version, không sửa đè trọng số. Ground truth không được giả định: churn/renewal là lagging outcome và chịu can thiệp; capstone đánh giá correctness của computation và use boundary, không tuyên bố predictive validity khi chưa có study.

## 4. Kiểm soát truy cập và dữ liệu thử

Policy matrix ghi persona, resource, action, condition và expected decision. Customer Success xem account trong region được giao; analyst có aggregate access; service principal chỉ chạy approved export. Chạy positive và negative cases ở BI, SQL, API, gồm expired role, cross-region row, restricted field và cached response. Fixture dùng synthetic identifiers và giả lập distribution; masked production copy không tự trở thành an toàn. Export tạo bản sao mới nên cần retention, owner và egress rule. Access log phải phân biệt denied, empty authorized result và system error.

## 5. Hai vòng usability có protocol cố định

Tác vụ đại diện gồm tìm đúng product, xác định account cần review, giải thích score components, nhận ra stale cutoff và từ chối một kết luận ngoài phạm vi. Ghi completion correctness, time, abandonment, assistance và confident-wrong outcome. Vòng hai sửa information architecture hoặc interface từ findings vòng một rồi chạy protocol tương đương. Điều kiện roadmap 'cải thiện ít nhất ba số' là gate học tập; với mẫu nhỏ, chênh lệch không chứng minh cải thiện population hay causal effect. Correctness và safety là guardrail: thời gian giảm nhưng hiểu sai tăng là regression.

## 6. Chi phí và vòng đời

Cost table tách build/refresh compute, storage, serving và labor/operations; direct, shared và unallocated phải reconcile trong tolerance. Unit cost dùng active decision hoặc reviewed account có định nghĩa, không dùng access grants. Retirement analysis kiểm long-cadence consumers, scheduled accounts, exports và compliance retention. Product đi qua proposed, build, certified, operate, deprecated, removed bằng evidence gates. Capstone chỉ tạo hồ sơ đủ để review trong môi trường học; không tự cấp chứng nhận production.

## 7. Bốn automatic-fail gates

Gate 1: metric không trace được về decision và action branch. Gate 2: không có executed usability evidence, chỉ có kế hoạch hoặc ảnh giao diện. Gate 3: thiếu interpretation limits cụ thể, làm consumer không biết kết luận bị cấm. Gate 4: dùng vanity signal như dashboard count, access count hoặc page views làm bằng chứng adoption/self-service. Mỗi gate ghi exact artifact, invariant bị vi phạm và remediation; presentation đẹp không bù được. Reviewer còn kiểm independent reconciliation, negative access test và raw evidence, vì tám hạng mục có thể đủ tên nhưng rỗng nội dung.

## 8. Ma trận kiểm chứng từng mệnh đề

Mỗi kết luận cần input, observation và failure signal có thể lưu. Tên sản phẩm, file nhỏ, query nhanh hoặc presentation thuyết phục không tự chứng minh cơ chế hay năng lực.

### 8.1. decision statement có decider cadence và action branches

**Mệnh đề cần kiểm.** decision statement có decider cadence và action branches.

**Cách kiểm.** Dựng synthetic customer/account fixture; kiểm tám artifacts, independent metric reconciliation, three-surface negative access, hai vòng task protocol và cost/lifecycle dossier. Gắn mỗi claim với exact artifact/version. Với mệnh đề này, ghi dataset/contract version, environment, controlled variables, expected observation, failure signal và boundary làm kết luận mất hiệu lực.

**Bằng chứng đạt.** Lưu fixture hoặc source slice, command/query/protocol, raw output, counters/diff, reviewer và artifact hash. Nếu lab chưa chạy trên môi trường được phép, chỉ ghi protocol và expected result; không viết như kết quả đã quan sát.

### 8.2. metric tree có owner ở mọi lá

**Mệnh đề cần kiểm.** metric tree có owner ở mọi lá.

**Cách kiểm.** Dựng synthetic customer/account fixture; kiểm tám artifacts, independent metric reconciliation, three-surface negative access, hai vòng task protocol và cost/lifecycle dossier. Gắn mỗi claim với exact artifact/version. Với mệnh đề này, ghi dataset/contract version, environment, controlled variables, expected observation, failure signal và boundary làm kết luận mất hiệu lực.

**Bằng chứng đạt.** Lưu fixture hoặc source slice, command/query/protocol, raw output, counters/diff, reviewer và artifact hash. Nếu lab chưa chạy trên môi trường được phép, chỉ ghi protocol và expected result; không viết như kết quả đã quan sát.

### 8.3. traceability matrix nối decision đến test evidence

**Mệnh đề cần kiểm.** traceability matrix nối decision đến test evidence.

**Cách kiểm.** Dựng synthetic customer/account fixture; kiểm tám artifacts, independent metric reconciliation, three-surface negative access, hai vòng task protocol và cost/lifecycle dossier. Gắn mỗi claim với exact artifact/version. Với mệnh đề này, ghi dataset/contract version, environment, controlled variables, expected observation, failure signal và boundary làm kết luận mất hiệu lực.

**Bằng chứng đạt.** Lưu fixture hoặc source slice, command/query/protocol, raw output, counters/diff, reviewer và artifact hash. Nếu lab chưa chạy trên môi trường được phép, chỉ ghi protocol và expected result; không viết như kết quả đã quan sát.

### 8.4. grain của customer health snapshot được khóa trước join

**Mệnh đề cần kiểm.** grain của customer health snapshot được khóa trước join.

**Cách kiểm.** Dựng synthetic customer/account fixture; kiểm tám artifacts, independent metric reconciliation, three-surface negative access, hai vòng task protocol và cost/lifecycle dossier. Gắn mỗi claim với exact artifact/version. Với mệnh đề này, ghi dataset/contract version, environment, controlled variables, expected observation, failure signal và boundary làm kết luận mất hiệu lực.

**Bằng chứng đạt.** Lưu fixture hoặc source slice, command/query/protocol, raw output, counters/diff, reviewer và artifact hash. Nếu lab chưa chạy trên môi trường được phép, chỉ ghi protocol và expected result; không viết như kết quả đã quan sát.

### 8.5. score version không bị sửa đè

**Mệnh đề cần kiểm.** score version không bị sửa đè.

**Cách kiểm.** Dựng synthetic customer/account fixture; kiểm tám artifacts, independent metric reconciliation, three-surface negative access, hai vòng task protocol và cost/lifecycle dossier. Gắn mỗi claim với exact artifact/version. Với mệnh đề này, ghi dataset/contract version, environment, controlled variables, expected observation, failure signal và boundary làm kết luận mất hiệu lực.

**Bằng chứng đạt.** Lưu fixture hoặc source slice, command/query/protocol, raw output, counters/diff, reviewer và artifact hash. Nếu lab chưa chạy trên môi trường được phép, chỉ ghi protocol và expected result; không viết như kết quả đã quan sát.

### 8.6. predictive validity không được suy từ computation correctness

**Mệnh đề cần kiểm.** predictive validity không được suy từ computation correctness.

**Cách kiểm.** Dựng synthetic customer/account fixture; kiểm tám artifacts, independent metric reconciliation, three-surface negative access, hai vòng task protocol và cost/lifecycle dossier. Gắn mỗi claim với exact artifact/version. Với mệnh đề này, ghi dataset/contract version, environment, controlled variables, expected observation, failure signal và boundary làm kết luận mất hiệu lực.

**Bằng chứng đạt.** Lưu fixture hoặc source slice, command/query/protocol, raw output, counters/diff, reviewer và artifact hash. Nếu lab chưa chạy trên môi trường được phép, chỉ ghi protocol và expected result; không viết như kết quả đã quan sát.

### 8.7. public interface nêu interpretation limits

**Mệnh đề cần kiểm.** public interface nêu interpretation limits.

**Cách kiểm.** Dựng synthetic customer/account fixture; kiểm tám artifacts, independent metric reconciliation, three-surface negative access, hai vòng task protocol và cost/lifecycle dossier. Gắn mỗi claim với exact artifact/version. Với mệnh đề này, ghi dataset/contract version, environment, controlled variables, expected observation, failure signal và boundary làm kết luận mất hiệu lực.

**Bằng chứng đạt.** Lưu fixture hoặc source slice, command/query/protocol, raw output, counters/diff, reviewer và artifact hash. Nếu lab chưa chạy trên môi trường được phép, chỉ ghi protocol và expected result; không viết như kết quả đã quan sát.

### 8.8. BI SQL API cùng policy intent qua negative tests

**Mệnh đề cần kiểm.** BI SQL API cùng policy intent qua negative tests.

**Cách kiểm.** Dựng synthetic customer/account fixture; kiểm tám artifacts, independent metric reconciliation, three-surface negative access, hai vòng task protocol và cost/lifecycle dossier. Gắn mỗi claim với exact artifact/version. Với mệnh đề này, ghi dataset/contract version, environment, controlled variables, expected observation, failure signal và boundary làm kết luận mất hiệu lực.

**Bằng chứng đạt.** Lưu fixture hoặc source slice, command/query/protocol, raw output, counters/diff, reviewer và artifact hash. Nếu lab chưa chạy trên môi trường được phép, chỉ ghi protocol và expected result; không viết như kết quả đã quan sát.

### 8.9. synthetic fixture không chứa production identifier

**Mệnh đề cần kiểm.** synthetic fixture không chứa production identifier.

**Cách kiểm.** Dựng synthetic customer/account fixture; kiểm tám artifacts, independent metric reconciliation, three-surface negative access, hai vòng task protocol và cost/lifecycle dossier. Gắn mỗi claim với exact artifact/version. Với mệnh đề này, ghi dataset/contract version, environment, controlled variables, expected observation, failure signal và boundary làm kết luận mất hiệu lực.

**Bằng chứng đạt.** Lưu fixture hoặc source slice, command/query/protocol, raw output, counters/diff, reviewer và artifact hash. Nếu lab chưa chạy trên môi trường được phép, chỉ ghi protocol và expected result; không viết như kết quả đã quan sát.

### 8.10. usability task có correct answer và confident-wrong outcome

**Mệnh đề cần kiểm.** usability task có correct answer và confident-wrong outcome.

**Cách kiểm.** Dựng synthetic customer/account fixture; kiểm tám artifacts, independent metric reconciliation, three-surface negative access, hai vòng task protocol và cost/lifecycle dossier. Gắn mỗi claim với exact artifact/version. Với mệnh đề này, ghi dataset/contract version, environment, controlled variables, expected observation, failure signal và boundary làm kết luận mất hiệu lực.

**Bằng chứng đạt.** Lưu fixture hoặc source slice, command/query/protocol, raw output, counters/diff, reviewer và artifact hash. Nếu lab chưa chạy trên môi trường được phép, chỉ ghi protocol và expected result; không viết như kết quả đã quan sát.

### 8.11. ba số cải thiện trong mẫu nhỏ không chứng minh causal effect

**Mệnh đề cần kiểm.** ba số cải thiện trong mẫu nhỏ không chứng minh causal effect.

**Cách kiểm.** Dựng synthetic customer/account fixture; kiểm tám artifacts, independent metric reconciliation, three-surface negative access, hai vòng task protocol và cost/lifecycle dossier. Gắn mỗi claim với exact artifact/version. Với mệnh đề này, ghi dataset/contract version, environment, controlled variables, expected observation, failure signal và boundary làm kết luận mất hiệu lực.

**Bằng chứng đạt.** Lưu fixture hoặc source slice, command/query/protocol, raw output, counters/diff, reviewer và artifact hash. Nếu lab chưa chạy trên môi trường được phép, chỉ ghi protocol và expected result; không viết như kết quả đã quan sát.

### 8.12. cost table reconcile direct shared unallocated

**Mệnh đề cần kiểm.** cost table reconcile direct shared unallocated.

**Cách kiểm.** Dựng synthetic customer/account fixture; kiểm tám artifacts, independent metric reconciliation, three-surface negative access, hai vòng task protocol và cost/lifecycle dossier. Gắn mỗi claim với exact artifact/version. Với mệnh đề này, ghi dataset/contract version, environment, controlled variables, expected observation, failure signal và boundary làm kết luận mất hiệu lực.

**Bằng chứng đạt.** Lưu fixture hoặc source slice, command/query/protocol, raw output, counters/diff, reviewer và artifact hash. Nếu lab chưa chạy trên môi trường được phép, chỉ ghi protocol và expected result; không viết như kết quả đã quan sát.

### 8.13. retirement inventory tìm long-cadence consumers

**Mệnh đề cần kiểm.** retirement inventory tìm long-cadence consumers.

**Cách kiểm.** Dựng synthetic customer/account fixture; kiểm tám artifacts, independent metric reconciliation, three-surface negative access, hai vòng task protocol và cost/lifecycle dossier. Gắn mỗi claim với exact artifact/version. Với mệnh đề này, ghi dataset/contract version, environment, controlled variables, expected observation, failure signal và boundary làm kết luận mất hiệu lực.

**Bằng chứng đạt.** Lưu fixture hoặc source slice, command/query/protocol, raw output, counters/diff, reviewer và artifact hash. Nếu lab chưa chạy trên môi trường được phép, chỉ ghi protocol và expected result; không viết như kết quả đã quan sát.

### 8.14. automatic-fail gate không được presentation miễn trừ

**Mệnh đề cần kiểm.** automatic-fail gate không được presentation miễn trừ.

**Cách kiểm.** Dựng synthetic customer/account fixture; kiểm tám artifacts, independent metric reconciliation, three-surface negative access, hai vòng task protocol và cost/lifecycle dossier. Gắn mỗi claim với exact artifact/version. Với mệnh đề này, ghi dataset/contract version, environment, controlled variables, expected observation, failure signal và boundary làm kết luận mất hiệu lực.

**Bằng chứng đạt.** Lưu fixture hoặc source slice, command/query/protocol, raw output, counters/diff, reviewer và artifact hash. Nếu lab chưa chạy trên môi trường được phép, chỉ ghi protocol và expected result; không viết như kết quả đã quan sát.

### 8.15. capstone review không phải production certification

**Mệnh đề cần kiểm.** capstone review không phải production certification.

**Cách kiểm.** Dựng synthetic customer/account fixture; kiểm tám artifacts, independent metric reconciliation, three-surface negative access, hai vòng task protocol và cost/lifecycle dossier. Gắn mỗi claim với exact artifact/version. Với mệnh đề này, ghi dataset/contract version, environment, controlled variables, expected observation, failure signal và boundary làm kết luận mất hiệu lực.

**Bằng chứng đạt.** Lưu fixture hoặc source slice, command/query/protocol, raw output, counters/diff, reviewer và artifact hash. Nếu lab chưa chạy trên môi trường được phép, chỉ ghi protocol và expected result; không viết như kết quả đã quan sát.

## 9. Quy trình phản biện

1. Chốt decision hoặc workload, grain, version và constraints trước khi chọn implementation.
2. Tách logical semantics, physical mechanism, observed metric và business conclusion.
3. Khóa controlled variables; ghi rõ confounders còn lại và instrumentation boundary.
4. Kiểm correctness trước performance, đồng thời giữ negative và changed-constraint cases.
5. Phân loại source fact, curriculum synthesis, engine-specific behavior và untested hypothesis.
6. Dùng raw artifacts và independent oracle khi kết quả do chính implementation sinh ra.
7. Chưa có execution evidence thì giữ trạng thái `review`.

## 10. Câu hỏi tự kiểm tra

1. Invariant, decision hoặc workload characteristic trung tâm là gì?
2. Biến nào được giữ cố định và biến nào được thay đổi?
3. Counter nào đo đúng mechanism thay vì chỉ đo wall-clock?
4. Một kết quả xanh nhưng sai semantics có thể xuất hiện bằng cách nào?
5. Điều kiện nào làm lựa chọn hiện tại phải đảo?
6. Kết luận nào mới là protocol, chưa phải evidence quan sát được?

## 11. Giới hạn và điều chưa cho phép kết luận

- Chưa chạy capstone với người dùng thật, Gate 5 với hội đồng, benchmark engines hoặc compression matrix; note mô tả protocol và expected evidence.
- Tài liệu web được kiểm ngày 2026-10-01; format, encoding support, storage version và engine behavior có thể đổi.
- Rubric, tám hạng mục capstone và ma trận kiểm chứng là curriculum synthesis; không gán nguyên văn cho một nguồn.
- Kết quả microbenchmark chỉ áp cho dataset, version, configuration, cache và workload đã ghi; không chứng minh ưu thế phổ quát.
- Note giữ trạng thái `review` cho tới khi chủ dự án duyệt semantic meaning.

## Reference
1. [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]]
2. [[SRC-DBT-SEMANTIC-MODELS]]
3. [[SRC-GOVUK-USABILITY-BENCHMARKING]]
4. [[SRC-OWASP-AUTHORIZATION-CHEAT-SHEET]]
5. [[SRC-FINOPS-ALLOCATION]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING]] | Khái niệm, mechanism hoặc evidence boundary liên quan | Đã đọc locator được ghi trong source record; không suy ngoài phạm vi |
| [[SRC-DBT-SEMANTIC-MODELS]] | Khái niệm, mechanism hoặc evidence boundary liên quan | Đã đọc locator được ghi trong source record; không suy ngoài phạm vi |
| [[SRC-GOVUK-USABILITY-BENCHMARKING]] | Khái niệm, mechanism hoặc evidence boundary liên quan | Đã đọc locator được ghi trong source record; không suy ngoài phạm vi |
| [[SRC-OWASP-AUTHORIZATION-CHEAT-SHEET]] | Khái niệm, mechanism hoặc evidence boundary liên quan | Đã đọc locator được ghi trong source record; không suy ngoài phạm vi |
| [[SRC-FINOPS-ALLOCATION]] | Khái niệm, mechanism hoặc evidence boundary liên quan | Đã đọc locator được ghi trong source record; không suy ngoài phạm vi |

## Key takeaways
- Capstone là chuỗi bằng chứng tám hạng mục; đủ file nhưng thiếu traceability, usability, limitation hoặc valid adoption evidence vẫn không đạt.
- Correctness, scope và exact version đi trước performance hoặc approval.
- Một proxy dễ lấy không được dùng thay consumer outcome, physical counter hoặc independent reconciliation.
- Counterexample và changed constraint phải làm kết luận đảo khi assumptions không còn đúng.
- Chưa chạy lab thì artifact là giáo trình đã kiểm cấu trúc, không phải chứng nhận production hay benchmark result.
