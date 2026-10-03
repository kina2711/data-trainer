# Phase 6: Analytical Storage and Query Engines
# Module 14: OLAP Internals and Analytical Engines
# Lesson 215: Analytical Engine Cost Model

## Mục tiêu bài học

**Năng lực cần chứng minh.** Tính chi phí cho một khối lượng công việc trên hai mô hình tính tiền và chỉ ra thứ hạng có thể đảo ngược.

**Điều kiện hoàn thành.** Năm thành phần được tính cho cả hai mô hình, điểm đảo ngược thứ hạng được chỉ ra, và ba đòn bẩy có mức giảm riêng.

> [!abstract] Câu hỏi trung tâm
> Xây cost model workload-weighted cho hai pricing models như thế nào để tìm reversal point, allocation boundary và đòn bẩy giảm chi phí thật?

## 1. Cost model bắt đầu từ workload

Inventory query/job families với frequency, bytes processed, slot/credit/compute time, concurrency window, cache state, storage footprint/retention, output/egress và SLO. Ba query đại diện chỉ hợp lệ khi có weight từ trace hoặc scenario được ghi rõ. Tính theo period: daily/monthly workload volume, không so một query lẻ. Correctness và latency SLO là constraints; phương án rẻ nhưng không đạt output/SLO không nằm trên feasible frontier.

## 2. Năm thành phần cần unit

Scan/analysis cost: billed bytes hoặc service-specific processed units. Compute time: runtime × metered rate khi serverless/job model. Provisioned/capacity: allocated units × billed duration dù idle, có minimum/granularity/commitment. Storage: logical/physical/active/long-term bytes × retention. Transfer/egress: source-destination-region path × bytes. Operator TCO thêm engineering/on-call/governance/support; không trộn vào invoice subtotal nhưng phải hiện trong decision total. Mọi term ghi currency, region, date, tax/discount scope.

## 3. Hai pricing archetypes

On-demand scan model gần `sum(query_frequency × billed_bytes × rate)` với minimum/free-tier/cache exceptions. Capacity model gần `allocated_units × billable_time × rate`, có utilization và commitments. Credit/warehouse model cũng capacity-time nhưng unit conversion, auto-suspend minimum và multi-cluster khác. Một engine có thể kết hợp storage, compute, serverless features và transfer. Model là piecewise function, không phải đơn giá nhân một metric duy nhất.

## 4. Reversal point

Gọi workload volume `x`. Nếu A có fixed baseline `F_A` và marginal `v_A`, B có `F_B`, `v_B`, equality ở `(F_B-F_A)/(v_A-v_B)` khi denominator khác zero và trong valid pricing segment. Thực tế rates tiered, commitments và concurrency làm nhiều breakpoints; solve từng interval hoặc scenario grid. Sensitivity thay frequency, bytes/query, concurrency, utilization, cache hit và egress. Reversal point là decision boundary, không dự báo nếu inputs không có uncertainty ranges.

## 5. Allocation và shared capacity

Invoice capacity dùng chung không có natural per-query cost. Allocation có thể theo slot-ms/credit, execution time weighted by size, bytes, reservation/project labels hoặc policy; mỗi cách tạo incentive khác. Idle and shared service cost cần rule: direct, proportional, even, committed owner hoặc unallocated platform. Tách measured usage khỏi allocated cost. Sum allocated phải reconcile invoice within tolerance; nếu không, unit economics không đáng tin.

## 6. Ba đòn bẩy nhưng không có thứ tự phổ quát

Giảm scanned bytes bằng projection, pruning, clustering/materialization thường giảm on-demand scan cost; trong fixed capacity nó chỉ tạo headroom trừ khi capacity/commitment giảm hoặc workload tăng. Query rewrite giảm compute/service time nhưng có engineering/maintenance cost. Right-size/schedule/auto-suspend giảm allocated idle time nhưng cold-start/cache effects có thể tăng latency/remote bytes. Roadmap nêu thứ tự scan→compute→cluster là heuristic lab, không định luật. Chọn theo marginal cost driver đã đo.

## 7. Guardrails và anomaly control

Dry-run/estimates, maximum bytes billed, resource monitors, quotas, budgets, alerts và approval gates giảm blast radius; chúng không thay correctness/performance tests. Alert theo absolute spend, rate-of-change và unit cost; failed/retried work phải tính. Hard stop có thể phá pipeline/SLO, nên có exception owner và recovery. Rate card snapshot/versioned, FX/tax/discount/contract sensitivity visible. Không nhúng giá hiện tại vào knowledge invariant.

## 8. Lab cost ledger

Tạo ledger rows cho three query families × frequency × two pricing models. Pull actual billed bytes, slot/credit/compute time, storage and transfer from telemetry/billing export; operator time là scenario có owner. Reconcile model subtotal với provider export trên sample window. Sweep volume/concurrency/storage/egress để tìm ranking reversal. Apply three interventions one at a time; keep result hash and SLO, calculate absolute and unit-cost delta plus confidence/assumptions. Done khi five terms present, allocation reconciles, reversal is reproducible and no saving is double-counted.

## 9. Ma trận kiểm chứng từng mệnh đề

Mỗi mệnh đề về latency, scaling, cache, concurrency hoặc cost cần counterfactual, correctness oracle và counter ở đúng boundary. Tên kiến trúc, plan label, elapsed time hoặc rate card riêng lẻ chưa đủ để quy nguyên nhân.

### 9.1. workload weights cần trace hoặc explicit scenario

**Mệnh đề cần kiểm.** workload weights cần trace hoặc explicit scenario.

**Cách kiểm.** Dựng versioned rate-card plus workload ledger; reconcile telemetry/billing, sweep scenario variables, solve breakpoints và kiểm result/SLO không đổi sau mỗi optimization. Ghi engine/version, workload shape, controlled variables, expected counter, failure signal và reversal condition.

**Bằng chứng đạt.** Lưu source/query/config hashes, plans/profiles, raw counters, result oracle, repetitions, units và reviewer. Khi lab chưa chạy, chỉ giữ protocol và expected observations; không viết chúng như kết quả thực nghiệm.

### 9.2. cheap option must still satisfy correctness and SLO

**Mệnh đề cần kiểm.** cheap option must still satisfy correctness and SLO.

**Cách kiểm.** Dựng versioned rate-card plus workload ledger; reconcile telemetry/billing, sweep scenario variables, solve breakpoints và kiểm result/SLO không đổi sau mỗi optimization. Ghi engine/version, workload shape, controlled variables, expected counter, failure signal và reversal condition.

**Bằng chứng đạt.** Lưu source/query/config hashes, plans/profiles, raw counters, result oracle, repetitions, units và reviewer. Khi lab chưa chạy, chỉ giữ protocol và expected observations; không viết chúng như kết quả thực nghiệm.

### 9.3. scan compute capacity storage transfer phải có unit riêng

**Mệnh đề cần kiểm.** scan compute capacity storage transfer phải có unit riêng.

**Cách kiểm.** Dựng versioned rate-card plus workload ledger; reconcile telemetry/billing, sweep scenario variables, solve breakpoints và kiểm result/SLO không đổi sau mỗi optimization. Ghi engine/version, workload shape, controlled variables, expected counter, failure signal và reversal condition.

**Bằng chứng đạt.** Lưu source/query/config hashes, plans/profiles, raw counters, result oracle, repetitions, units và reviewer. Khi lab chưa chạy, chỉ giữ protocol và expected observations; không viết chúng như kết quả thực nghiệm.

### 9.4. invoice subtotal khác fully loaded TCO

**Mệnh đề cần kiểm.** invoice subtotal khác fully loaded TCO.

**Cách kiểm.** Dựng versioned rate-card plus workload ledger; reconcile telemetry/billing, sweep scenario variables, solve breakpoints và kiểm result/SLO không đổi sau mỗi optimization. Ghi engine/version, workload shape, controlled variables, expected counter, failure signal và reversal condition.

**Bằng chứng đạt.** Lưu source/query/config hashes, plans/profiles, raw counters, result oracle, repetitions, units và reviewer. Khi lab chưa chạy, chỉ giữ protocol và expected observations; không viết chúng như kết quả thực nghiệm.

### 9.5. operator time cần explicit scope và owner

**Mệnh đề cần kiểm.** operator time cần explicit scope và owner.

**Cách kiểm.** Dựng versioned rate-card plus workload ledger; reconcile telemetry/billing, sweep scenario variables, solve breakpoints và kiểm result/SLO không đổi sau mỗi optimization. Ghi engine/version, workload shape, controlled variables, expected counter, failure signal và reversal condition.

**Bằng chứng đạt.** Lưu source/query/config hashes, plans/profiles, raw counters, result oracle, repetitions, units và reviewer. Khi lab chưa chạy, chỉ giữ protocol và expected observations; không viết chúng như kết quả thực nghiệm.

### 9.6. pricing function thường piecewise không tuyến tính toàn miền

**Mệnh đề cần kiểm.** pricing function thường piecewise không tuyến tính toàn miền.

**Cách kiểm.** Dựng versioned rate-card plus workload ledger; reconcile telemetry/billing, sweep scenario variables, solve breakpoints và kiểm result/SLO không đổi sau mỗi optimization. Ghi engine/version, workload shape, controlled variables, expected counter, failure signal và reversal condition.

**Bằng chứng đạt.** Lưu source/query/config hashes, plans/profiles, raw counters, result oracle, repetitions, units và reviewer. Khi lab chưa chạy, chỉ giữ protocol và expected observations; không viết chúng như kết quả thực nghiệm.

### 9.7. on demand bytes và capacity time có fixed marginal structure khác

**Mệnh đề cần kiểm.** on demand bytes và capacity time có fixed marginal structure khác.

**Cách kiểm.** Dựng versioned rate-card plus workload ledger; reconcile telemetry/billing, sweep scenario variables, solve breakpoints và kiểm result/SLO không đổi sau mỗi optimization. Ghi engine/version, workload shape, controlled variables, expected counter, failure signal và reversal condition.

**Bằng chứng đạt.** Lưu source/query/config hashes, plans/profiles, raw counters, result oracle, repetitions, units và reviewer. Khi lab chưa chạy, chỉ giữ protocol và expected observations; không viết chúng như kết quả thực nghiệm.

### 9.8. reversal point cần valid interval và sensitivity ranges

**Mệnh đề cần kiểm.** reversal point cần valid interval và sensitivity ranges.

**Cách kiểm.** Dựng versioned rate-card plus workload ledger; reconcile telemetry/billing, sweep scenario variables, solve breakpoints và kiểm result/SLO không đổi sau mỗi optimization. Ghi engine/version, workload shape, controlled variables, expected counter, failure signal và reversal condition.

**Bằng chứng đạt.** Lưu source/query/config hashes, plans/profiles, raw counters, result oracle, repetitions, units và reviewer. Khi lab chưa chạy, chỉ giữ protocol và expected observations; không viết chúng như kết quả thực nghiệm.

### 9.9. shared capacity allocation là policy không phải source fact

**Mệnh đề cần kiểm.** shared capacity allocation là policy không phải source fact.

**Cách kiểm.** Dựng versioned rate-card plus workload ledger; reconcile telemetry/billing, sweep scenario variables, solve breakpoints và kiểm result/SLO không đổi sau mỗi optimization. Ghi engine/version, workload shape, controlled variables, expected counter, failure signal và reversal condition.

**Bằng chứng đạt.** Lưu source/query/config hashes, plans/profiles, raw counters, result oracle, repetitions, units và reviewer. Khi lab chưa chạy, chỉ giữ protocol và expected observations; không viết chúng như kết quả thực nghiệm.

### 9.10. allocated costs phải reconcile provider invoice

**Mệnh đề cần kiểm.** allocated costs phải reconcile provider invoice.

**Cách kiểm.** Dựng versioned rate-card plus workload ledger; reconcile telemetry/billing, sweep scenario variables, solve breakpoints và kiểm result/SLO không đổi sau mỗi optimization. Ghi engine/version, workload shape, controlled variables, expected counter, failure signal và reversal condition.

**Bằng chứng đạt.** Lưu source/query/config hashes, plans/profiles, raw counters, result oracle, repetitions, units và reviewer. Khi lab chưa chạy, chỉ giữ protocol và expected observations; không viết chúng như kết quả thực nghiệm.

### 9.11. bytes saved không luôn tạo invoice saving dưới fixed commitment

**Mệnh đề cần kiểm.** bytes saved không luôn tạo invoice saving dưới fixed commitment.

**Cách kiểm.** Dựng versioned rate-card plus workload ledger; reconcile telemetry/billing, sweep scenario variables, solve breakpoints và kiểm result/SLO không đổi sau mỗi optimization. Ghi engine/version, workload shape, controlled variables, expected counter, failure signal và reversal condition.

**Bằng chứng đạt.** Lưu source/query/config hashes, plans/profiles, raw counters, result oracle, repetitions, units và reviewer. Khi lab chưa chạy, chỉ giữ protocol và expected observations; không viết chúng như kết quả thực nghiệm.

### 9.12. right sizing có thể đổi cold start và cache behavior

**Mệnh đề cần kiểm.** right sizing có thể đổi cold start và cache behavior.

**Cách kiểm.** Dựng versioned rate-card plus workload ledger; reconcile telemetry/billing, sweep scenario variables, solve breakpoints và kiểm result/SLO không đổi sau mỗi optimization. Ghi engine/version, workload shape, controlled variables, expected counter, failure signal và reversal condition.

**Bằng chứng đạt.** Lưu source/query/config hashes, plans/profiles, raw counters, result oracle, repetitions, units và reviewer. Khi lab chưa chạy, chỉ giữ protocol và expected observations; không viết chúng như kết quả thực nghiệm.

### 9.13. guardrail không thay performance correctness test

**Mệnh đề cần kiểm.** guardrail không thay performance correctness test.

**Cách kiểm.** Dựng versioned rate-card plus workload ledger; reconcile telemetry/billing, sweep scenario variables, solve breakpoints và kiểm result/SLO không đổi sau mỗi optimization. Ghi engine/version, workload shape, controlled variables, expected counter, failure signal và reversal condition.

**Bằng chứng đạt.** Lưu source/query/config hashes, plans/profiles, raw counters, result oracle, repetitions, units và reviewer. Khi lab chưa chạy, chỉ giữ protocol và expected observations; không viết chúng như kết quả thực nghiệm.

### 9.14. failed retries và idle capacity vẫn là cost

**Mệnh đề cần kiểm.** failed retries và idle capacity vẫn là cost.

**Cách kiểm.** Dựng versioned rate-card plus workload ledger; reconcile telemetry/billing, sweep scenario variables, solve breakpoints và kiểm result/SLO không đổi sau mỗi optimization. Ghi engine/version, workload shape, controlled variables, expected counter, failure signal và reversal condition.

**Bằng chứng đạt.** Lưu source/query/config hashes, plans/profiles, raw counters, result oracle, repetitions, units và reviewer. Khi lab chưa chạy, chỉ giữ protocol và expected observations; không viết chúng như kết quả thực nghiệm.

### 9.15. rate card phải versioned theo date region contract currency

**Mệnh đề cần kiểm.** rate card phải versioned theo date region contract currency.

**Cách kiểm.** Dựng versioned rate-card plus workload ledger; reconcile telemetry/billing, sweep scenario variables, solve breakpoints và kiểm result/SLO không đổi sau mỗi optimization. Ghi engine/version, workload shape, controlled variables, expected counter, failure signal và reversal condition.

**Bằng chứng đạt.** Lưu source/query/config hashes, plans/profiles, raw counters, result oracle, repetitions, units và reviewer. Khi lab chưa chạy, chỉ giữ protocol và expected observations; không viết chúng như kết quả thực nghiệm.

## 10. Quy trình phản biện

1. Viết câu hỏi đo lường và decision cần hỗ trợ trước khi chọn metric.
2. Khóa query semantics, snapshot, output oracle và unit của mọi số.
3. Vẽ boundaries: client, queue, planner, source, worker, exchange, cache, spill và billing.
4. Thay một cơ chế; ghi mọi thay đổi algorithm/config do engine tự thực hiện.
5. Dùng distribution và critical path; không để average che tails hoặc skew.
6. Viết counterexample, reversal condition và stop threshold trước khi chạy.
7. Tách estimate, configured intent, runtime observation và invoice fact.
8. Nếu không kiểm soát được cache, resource hoặc rate contract, ghi giới hạn thay vì kết luận nhân quả.

## 11. Câu hỏi tự kiểm tra

1. Mệnh đề đang nằm ở tầng kiến trúc, scheduler, operator, hardware hay billing?
2. Counter nào quan sát trực tiếp cơ chế đó và proxy nào dễ gây nhầm?
3. Correctness/SLO nào phải giữ trước khi gọi một phương án tốt hơn?
4. Cache, concurrency, statistics, data shape hay rate card nào có thể đảo kết luận?
5. Intervention nào bác bỏ diagnosis hiện tại?
6. Kết luận nào mới là protocol, chưa phải observation?

## 12. Giới hạn và điều chưa cho phép kết luận

- Chưa chạy cluster scaling, join/spill, cache, concurrency hoặc billing reconciliation lab; note mô tả protocol và evidence contract.
- Tài liệu sản phẩm được kiểm ngày 2026-10-01; field, feature, pricing và behavior có thể đổi theo version, region và contract.
- Amdahl, Gustafson, workload matrices và cost equations là mô hình; chúng không thay runtime counters hay invoice export.
- Không suy vendor superiority từ paper hoặc một benchmark; workload, correctness, SLO, operation và price contract phải cùng phạm vi.
- Note giữ trạng thái `review` cho tới khi chủ dự án duyệt semantic meaning.

## Reference
1. [[SRC-FINOPS-DATA-CLOUD-PLATFORMS]]
2. [[SRC-FINOPS-UNIT-ECONOMICS]]
3. [[SRC-BIGQUERY-PRICING-SLOTS]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-FINOPS-DATA-CLOUD-PLATFORMS]] | Khái niệm, mechanism hoặc evidence boundary liên quan | Đã đọc locator trong source record; không suy ngoài phạm vi |
| [[SRC-FINOPS-UNIT-ECONOMICS]] | Khái niệm, mechanism hoặc evidence boundary liên quan | Đã đọc locator trong source record; không suy ngoài phạm vi |
| [[SRC-BIGQUERY-PRICING-SLOTS]] | Khái niệm, mechanism hoặc evidence boundary liên quan | Đã đọc locator trong source record; không suy ngoài phạm vi |

## Key takeaways
- Cost comparison là workload-weighted piecewise model có allocation, reconciliation và reversal point, không phải so đơn giá.
- Estimate và configured intent phải được tách khỏi runtime observation và invoice fact.
- Correctness oracle, units, cache state, workload shape và controlled variables đi trước performance/cost claim.
- Average phải đi cùng distributions, tails, critical path và per-class hoặc per-task counters.
- Chưa chạy lab thì artifact là giáo trình đã kiểm cấu trúc, chưa phải benchmark hay production certification.
