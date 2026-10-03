#!/usr/bin/env python3
"""Build source-grounded L196-L200 data-product operations notes."""
from __future__ import annotations

import argparse
import json
import re

import promote_l191_l195_notes as previous
from format_knowledge_notes import normalize_markdown
from promote_l140_l144_notes import Lesson

ROOT = previous.ROOT
BASE = previous.BASE
PACK = previous.PACK
WIKI = previous.WIKI

OW = "src.web.owasp-authorization-cheat-sheet"
NI = "src.web.nist-sp-800-188-deidentification"
K6 = "src.web.grafana-k6-performance-testing"
HE = "src.paper.google-heart-ux-metrics"
AM = "src.web.amplitude-north-star-framework"
UB = "src.web.govuk-usability-benchmarking"
FA = "src.web.finops-allocation"
FU = "src.web.finops-unit-economics"
FD = "src.book.reis-housley-fundamentals-data-engineering"
HI = "src.web.hightouch-reverse-etl-syncs"
IC = "src.web.ico-purpose-limitation"
ST = "src.web.stripe-idempotent-requests"
BA = "src.web.backstage-software-catalog"
SO = "src.book.sommerville-software-engineering.10e"
SR = "src.web.google-sre-postmortem-culture"

OWL = "SRC-OWASP-AUTHORIZATION-CHEAT-SHEET"
NIL = "SRC-NIST-SP-800-188-DEIDENTIFICATION"
K6L = "SRC-GRAFANA-K6-PERFORMANCE-TESTING"
HEL = "SRC-GOOGLE-HEART-UX-METRICS"
AML = "SRC-AMPLITUDE-NORTH-STAR-FRAMEWORK"
UBL = "SRC-GOVUK-USABILITY-BENCHMARKING"
FAL = "SRC-FINOPS-ALLOCATION"
FUL = "SRC-FINOPS-UNIT-ECONOMICS"
FDL = "SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING"
HIL = "SRC-HIGHTOUCH-REVERSE-ETL-SYNCS"
ICL = "SRC-ICO-PURPOSE-LIMITATION"
STL = "SRC-STRIPE-IDEMPOTENT-REQUESTS"
BAL = "SRC-BACKSTAGE-SOFTWARE-CATALOG"
SOL = "SRC-SOMMERVILLE-SOFTWARE-ENGINEERING-10E"
SRL = "SRC-GOOGLE-SRE-POSTMORTEM-CULTURE"

LESSONS = (
    Lesson(
        196,
        "Lesson_196-serving-access-and-security-for-consumers",
        "Serving, Access and Security for Consumers",
        "84-serving-access-security-consumers.md",
        "wiki.data-product.serving-access-security",
        "Làm sao chứng minh BI, SQL và API cùng thi hành một access policy, đáp ứng workload contract và không biến dữ liệu thử nghiệm thành một bản sao nhạy cảm không kiểm soát?",
        (OW, NI, K6),
        (OWL, NIL, K6L),
        (
            ("Ba bề mặt, một policy intent", "BI, direct SQL và API có identity propagation, query semantics, caching và export behavior khác nhau. Cấu hình có thể khác nhưng policy intent phải thống nhất: persona nào được xem product, rows, columns, metrics và operations nào trong context nào. Tạo policy matrix với subject class, resource, action, condition và expected decision; mỗi surface có adapter mapping về cùng stable rule ID. Nếu BI dùng extract, SQL dùng live warehouse còn API dùng cache, phép thử phải chạm cả ba execution path thay vì chỉ kiểm source table."),
            ("Deny by default và quyền theo vai", "OWASP khuyến nghị least privilege, deny by default và kiểm authorization ở mọi request. Role/group entitlement nên có owner, business purpose, approver, review cadence và expiry cho quyền tạm. Cấp trực tiếp theo cá nhân tạo ngoại lệ khó rà nhưng RBAC quá rộng cũng không an toàn; attributes như region, purpose hoặc sensitivity có thể cần ABAC. Service accounts được quản trị như principals riêng, không mượn user role. Break-glass access cần timebox, audit và post-use review; việc đăng nhập thành công không chứng minh authorization đúng."),
            ("Negative tests và policy parity", "Fixture có ít nhất hai tenants, public/sensitive columns, certified/restricted metrics và principals: allowed, denied, expired, service, privileged. Với mỗi rule chạy positive control và negative attempt ở BI, SQL, API; so decision code, visible row/field set, aggregation/inference behavior và audit event. Kết quả không nhất thiết giống error text, nhưng không surface nào được trả dữ liệu rộng hơn contract. Test owner/admin path riêng vì database owner, superuser hoặc bypass capability có thể không chịu row policy như ordinary principal."),
            ("Performance contract phải có workload", "p95 không có nghĩa nếu thiếu query/task mix, arrival/concurrency model, dataset/cardinality, cache state, timeout, warm-up và observation window. k6 scenarios, metrics và thresholds minh họa cách mã hóa load shape cùng pass/fail criteria; BI interaction và warehouse SQL có thể cần harness khác nhưng vẫn dùng cùng principle. Đo latency, throughput/concurrency, error/timeout, queue/saturation, cost và result correctness. Cache làm p95 đẹp nhưng có thể trả stale hoặc cross-principal data; mỗi test cần semantic/security assertions, không chỉ response time."),
            ("Overload là một phần của interface", "Hệ thống phải nêu behavior khi vượt capacity: queue có bound, reject/throttle với signal rõ, degrade feature có kiểm soát hoặc shed low-priority workload. Unlimited queue thường biến overload thành timeout dài và retry amplification. Fairness giữa BI refresh, analyst query và API caller cần quota/priorities; một tenant không được chiếm toàn concurrency. Thử ramp, steady và spike; ghi recovery sau khi load giảm. Success là giữ invariants và bounded failure, không phải ép mọi request thành công. Load test chỉ chạy trong environment có capacity và stop conditions được phép."),
            ("Masking không đồng nghĩa de-identification", "Xóa tên/email nhưng giữ ZIP, timestamp, rare behavior hoặc stable pseudonym vẫn cho phép linkage. NIST SP 800-188 phân biệt nhiều sharing models và nhấn mạnh disclosure-risk governance; synthetic data hoặc controlled query/enclave có thể phù hợp hơn một masked copy. Non-production data policy phải lập inventory direct/quasi-identifiers, threat model, utility need, transformation, re-identification test, retention và egress restriction. Tokenization/pseudonymization hữu ích nhưng reversible mapping/key trở thành sensitive asset."),
            ("Audit, export và bằng chứng hoàn thành", "Access log cần actor/service principal, purpose/context nếu có, resource/version, decision, query/API action, rows/bytes/export và timestamp; không ghi secrets hoặc raw sensitive predicates vô hạn. Log phải phân biệt denied attempt, empty authorized result và system error. Export từ BI hoặc SQL tạo bản sao ngoài policy boundary nên cần watermark/retention/DLP hoặc restricted path theo risk. Lab đạt khi negative matrix parity đúng ở ba surfaces, workload thresholds và overload behavior có raw evidence, non-production fixture qua de-identification review; chưa chạy thì chỉ là protocol."),
        ),
        (
            "policy intent dùng chung nhưng adapters theo từng surface",
            "BI extract có thể lệch live warehouse policy",
            "deny by default cần explicit grants",
            "RBAC quá rộng vẫn vi phạm least privilege",
            "temporary access cần expiry và review",
            "service account là principal riêng",
            "negative tests chạy trên BI SQL và API",
            "admin path không đại diện ordinary principal",
            "p95 cần workload và observation window",
            "cache test cần security context và freshness",
            "overload cần bounded failure behavior",
            "unlimited queue có thể khuếch đại timeout",
            "mask direct identifier chưa đủ de-identification",
            "quasi-identifiers tạo re-identification risk",
            "export tạo policy boundary mới",
        ),
    ),
    Lesson(
        197,
        "Lesson_197-adoption-metrics-that-are-not-vanity",
        "Adoption Metrics That Are Not Vanity",
        "85-adoption-metrics-not-vanity.md",
        "wiki.data-product.adoption-metrics",
        "Bộ đo adoption nào nối product goals với hành vi và decision outcomes, tránh activity counts, denominator sai, trust proxy mơ hồ và incentive gaming?",
        (HE, AM, UB),
        (HEL, AML, UBL),
        (
            ("Đi từ goal tới signal rồi metric", "HEART cung cấp năm góc nhìn Happiness, Engagement, Adoption, Retention và Task Success; Goals–Signals–Metrics buộc nêu mục tiêu trước tín hiệu và phép tính. Với data product, goal có thể là một cohort ra quyết định định kỳ bằng metric certified mà không cần handoff thủ công. Signal gồm use đúng persona/cadence, task hoàn tất đúng và decision record có evidence. Metric chỉ hợp lệ khi có population, event, grain, time window, owner, quality và action threshold; log dễ lấy không phải lý do đủ để chọn."),
            ("Adoption và active use theo nhịp quyết định", "Activated user phải hoàn tất activation event có ý nghĩa, chẳng hạn tìm đúng product, chạy use case đầu và giải thích đúng grain; được cấp quyền không phải activation. Active cadence theo natural decision cycle: daily cho operations, monthly cho close, quarterly cho planning. Dùng DAU cho quarterly product sẽ gọi người dùng tốt là inactive; dùng MAU có thể che failed daily workflows. Loại bots, service accounts, scheduled refresh hoặc tách thành automation cohort. Báo cohort eligible, activated, active và dormant để denominator minh bạch."),
            ("Retention và breadth không thay correctness", "Retention đo cohort quay lại thực hiện value event sau lần đầu, không phải page view. Breadth cho biết bao nhiêu teams/personas/decisions có use; depth cho biết frequency hoặc workflows per active. Cả hai có thể tăng khi user dùng product sai. Kết hợp task success, semantic correctness, stale/incident exposure và high-stakes review. Amplitude North Star phân biệt outcome và input metrics; bài sử dụng distinction này nhưng không coi một North Star duy nhất đủ cho data product governance."),
            ("Support-free answer rate cần guardrails", "Tử số là eligible analytical tasks hoàn tất đúng trong product scope mà không cần human intervention ngoài published enablement; mẫu số là toàn bộ eligible attempts, gồm abandon và escalations. Ticket count riêng không đủ vì user có thể bỏ cuộc hoặc tạo shadow spreadsheet. Audit một sample kết quả và confident-wrong rate; giảm support nhưng tăng sai số là regression. Phân loại intervention thành access, docs, product defect, skill hoặc novel analysis để không phạt đúng escalation của câu hỏi level 3."),
            ("Decision evidence không chứng minh impact", "Một decision record trích product/version, metric và cutoff cho thấy adoption vào process, nhưng không chứng minh quyết định tốt hoặc product gây business outcome. Đo coverage: số eligible decisions có traceable evidence / toàn eligible decisions; bổ sung reviewer quality, freshness và alternative sources. Tránh khuyến khích chèn link hình thức bằng sampling. Outcome metric ở business level cần counterfactual/causal design riêng; adoption metrics chỉ chứng minh use pattern và process integration."),
            ("Trust cần đo nhiều tín hiệu", "Roadmap gọi tỷ lệ tự kiểm chứng bằng nguồn khác là nghịch đảo của trust; quan hệ này không xác định. Cross-check có thể do low trust, high stakes, policy bắt buộc hoặc practice tốt. Đo trust bằng calibrated survey, explain-back, willingness-to-use, repeat use sau incident, discrepancy reports, freshness/quality awareness và verification reason. Trust cao mù quáng cũng nguy hiểm; target là calibrated reliance: user biết khi nào dùng, kiểm hoặc dừng. Luôn phân tách attitude, behavior và observed correctness."),
            ("Vanity, gaming và audit", "Số tables hoặc dashboards là output/activity count; chưa có bằng chứng để khẳng định dashboard count tương quan nghịch với quality. Access grants đo entitlement, không đo use. Các số này hữu ích cho inventory/capacity nhưng không đại diện adoption/value. Với mỗi KPI viết gaming hypothesis: spam dashboards, auto-refresh để tăng actives, đóng tickets không giải quyết, bắt buộc link evidence. Thêm guardrail, segmentation, raw-event quality và metric review cadence. Lab phải tính metric hợp lệ lẫn activity counts trên cùng data rồi nêu quyết định sai mà từng proxy có thể gây ra."),
        ),
        (
            "goal signal metric đi trước event instrumentation",
            "HEART categories không bắt buộc dùng đủ năm",
            "access grant khác activation",
            "active cadence khớp decision cycle",
            "bots và scheduled refresh tách cohort",
            "retention dùng value event không dùng page view",
            "breadth và depth không chứng minh correctness",
            "support-free denominator gồm abandon và escalation",
            "sample audit chặn confident-wrong self-service",
            "level-three escalation không bị tính là failure",
            "decision evidence coverage không chứng minh causal impact",
            "cross-check rate không phải trust inverse trực tiếp",
            "trust cần calibrated reliance",
            "dashboard count là activity không mặc nhiên inverse quality",
            "mỗi KPI cần gaming hypothesis và guardrail",
        ),
    ),
    Lesson(
        198,
        "Lesson_198-cost-to-serve",
        "Cost to Serve",
        "86-cost-to-serve.md",
        "wiki.data-product.cost-to-serve",
        "Làm sao dựng cost-to-serve có boundary, allocation policy, unit denominator và uncertainty đủ để so sánh hoặc đề xuất retirement mà không cắt nhầm giá trị?",
        (FA, FU, FD),
        (FAL, FUL, FDL),
        (
            ("Chốt boundary và kỳ đo", "Cost model phải ghi product ID/version, environments, services/jobs/tables, support responsibilities, currency, effective rates, discounts/amortization, period và excluded items. Một pipeline dùng chung cho năm products không thể gán toàn bộ cho product đầu tiên được xem. Phân biệt actual billed cost, allocated cost, estimate và opportunity cost. Reconcile tổng direct + shared + unallocated với bill/ledger trong tolerance; nếu phần unallocated lớn, ranking product là provisional. Không trộn monthly run rate của product này với one-time migration cost của product khác."),
            ("Bốn nhóm chi phí có cấu trúc", "Build/refresh compute gồm orchestration, warehouse/cluster jobs, network/egress và retries/backfills. Storage gồm tables, replicas, indexes, snapshots/backups và retention tiers. Serving gồm BI extracts, interactive SQL/API compute, cache, network và concurrency headroom. Labor/operations gồm build amortization nếu scope yêu cầu, on-call, incidents, support, governance, access reviews và vendor administration. Shared platform/license/observability phải direct, allocate hoặc báo unallocated; không làm nó biến mất. Roadmap nói labor thường lớn nhất nhưng đây chỉ là giả thuyết cần time evidence."),
            ("Allocation là policy có sensitivity", "FinOps Allocation dùng accounts/tags/labels/derived metadata và chiến lược shared cost. Direct attribution ưu tiên resource/job/query tags có product ID. Shared cost có thể chia fixed, proportional theo usage/spend/queries/users hoặc proxy khác; mỗi method mang incentive và bias. Platform base cost có thể central fund nếu đó là quyết định minh bạch. Chạy sensitivity với ít nhất hai plausible policies; nếu retirement candidate đổi theo method, không kết luận từ một ranking. Báo allocation coverage và phần chưa phân bổ."),
            ("Labor estimate có evidence", "Nguồn gồm ticket system, incident timeline, on-call events, deployment/change records và sampled time study; không hồi tưởng một con số đẹp. Gắn activity taxonomy: operate, support, governance, improvement, toil và product development. Tránh double-count một incident vào on-call và support hoặc phân toàn meeting time cho một product. Fully loaded rate là policy finance gồm salary/benefit/overhead hoặc internal standard; báo hours và rate tách riêng. Uncertainty range, confidence và missing logs quan trọng hơn giả chính xác tới đồng."),
            ("Unit economics nối cost với purpose", "FinOps Unit Economics phân resource-efficiency unit và business unit. Product có thể theo cost per refresh/query/GB cho engineering và cost per active decision, case resolved hoặc eligible user served cho business. Denominator phải là value-bearing event đã định nghĩa, không dùng access grants. So trend trong cùng scope thường đáng tin hơn xếp hạng products phục vụ mục tiêu khác. Unit cost giảm vì denominator bị spam hoặc quality/freshness giảm là false economy; kèm SLO, correctness, adoption và risk guardrails."),
            ("Retirement là decision nhiều chiều", "Candidate signals gồm không trace tới active decision, no confirmed consumer qua đủ cadence, duplicate contract, cost/risk cao so với replacement hoặc owner withdrawn. High cost–low use chưa đủ nếu product phục vụ rare regulatory/high-stakes event. Lập consumer inventory gồm offline exports, scheduled accounts và dormant cycles; so keep, optimize, merge, archive và retire. Phương án thay thế có compatibility/migration, retention/audit, notice, parallel window, removal proof và restore boundary. Stakeholder approval không sửa cost data sai."),
            ("Tối ưu có guardrails và test thay đổi", "Mỗi action nêu mechanism: reduce refresh frequency, incrementalize, tier storage, right-size, cache, prune fields/retention hoặc giảm manual support bằng product fix. Dự báo savings với assumptions rồi đo realized savings và regression. Cắt freshness chỉ hợp lệ khi decision latency cho phép; cache không được phá security/semantic version; xóa history không vi phạm audit. Lab ba products lưu raw bills/usage/tickets, allocation table, unit metrics, sensitivity, alternative analysis và migration plan; chưa có evidence thì đề xuất retirement chỉ là hypothesis."),
        ),
        (
            "cost model có product boundary và period",
            "actual allocated estimate opportunity cost tách nhau",
            "direct shared và unallocated phải reconcile",
            "build compute gồm retry và backfill",
            "storage gồm backup snapshot và retention",
            "serving cost gồm BI SQL API cache và egress",
            "labor largest là hypothesis không phải fact",
            "time evidence cần taxonomy và tránh double count",
            "shared allocation method tạo bias",
            "sensitivity test hai allocation policies",
            "unit denominator là value-bearing event",
            "trend within scope an toàn hơn cross-product ranking",
            "rare high-stakes product không bị xóa chỉ vì low use",
            "retirement inventory gồm offline and dormant consumers",
            "cost optimization cần freshness quality security guardrails",
        ),
    ),
    Lesson(
        199,
        "Lesson_199-reverse-etl-and-the-shadow-operational-system",
        "Reverse ETL and the Shadow Operational System",
        "87-reverse-etl-shadow-operational-system.md",
        "wiki.data-product.reverse-etl-shadow-system",
        "Reverse ETL được thiết kế thế nào để giữ system-of-record boundary, identity và retry safety, purpose limitation và vòng phản hồi có thể truy vết?",
        (HI, IC, ST),
        (HIL, ICL, STL),
        (
            ("Activation khác system of record", "Reverse ETL chuyển warehouse-derived rows, scores hoặc audiences sang CRM, support, marketing hoặc operational tools để hành động. Warehouse có thể là authoritative computation cho derived attribute nhưng không mặc nhiên là owner của customer consent, order state hoặc workflow truth. Với mỗi field ghi system of record, calculation owner, destination use, write authority và conflict rule. Destination edits có được phép không; nếu có, chúng quay về đâu. Shadow operational system xuất hiện khi daily workflow phụ thuộc sync nhưng ownership, SLO, incident response và state authority vẫn được đối xử như analytics batch."),
            ("Identity, matching và delete semantics", "Stable destination key phải unique, immutable trong horizon và map được với consent/tenant context. `user_id` không đủ cho event nếu nhiều events cùng user; composite/event ID cần uniqueness. Hightouch docs cho thấy CDC dựa primary key và key change có thể tạo add/remove ngoài dự kiến. Chốt insert/update/upsert/archive/all, field mapping, null semantics, record leaving segment và hard/soft delete. Một removed warehouse row không mặc nhiên có nghĩa xóa customer ở CRM. Trước full resync cần biết destination side effects và duplicate risk."),
            ("Idempotency và retry boundary", "Network timeout không cho biết destination đã áp write hay chưa. Operation có deterministic idempotency key theo business action/version, request fingerprint và durable outcome record; retry cùng intent không tạo side effect mới. Stripe documentation minh họa idempotency key cho request retry, nhưng mỗi destination có semantics/retention khác. Upsert record có thể idempotent về final fields nhưng trigger email, campaign enrollment hoặc webhook không idempotent. Tách state synchronization khỏi commands/events; action side effect cần command ID, dedupe và replay policy."),
            ("Purpose limitation và field minimization", "Dữ liệu được thu cho analytics không tự được phép dùng để target, deny service hoặc trigger outreach. ICO guidance yêu cầu specified purposes và review further processing; legal basis, notice và jurisdiction do owner pháp lý xác định. Mỗi sync có purpose ID, approved fields, sensitive/protected attributes, recipient, retention và allowed action. Không sync field chỉ vì có sẵn. Derived score có thể tiết lộ sensitive inference dù input đã aggregate. Test denied mapping và purpose mismatch, đồng thời kiểm destination admins/exports."),
            ("Feedback loop làm đổi dữ liệu", "Ví dụ warehouse tính churn score, sync sang CRM; agent gọi ưu đãi, outcome quay vào source rồi model học rằng nhóm score cao có retention tốt. Intervention làm thay distribution và outcome, nên score-performance drift không chỉ do model. Gắn exposure/intervention ID, policy/version, assignment/time và suppress re-entry khi cần. Phân biệt organic outcome với treated outcome; causal evaluation cần design phù hợp. Lineage graph phải có vòng destination action → operational event → ingestion → model, không dừng ở một chiều warehouse → CRM."),
            ("SLO và dấu hiệu shadow system", "Theo dõi source cutoff, model run, CDC baseline, queued operations, destination accepted/rejected, retry age, duplicate/conflict, privacy block và end-to-end action latency. Ba dấu hiệu mạnh: workflow không chạy nếu analytics sync trễ; team hứa operational SLO nhưng không có on-call/recovery; không rõ state nào thắng khi warehouse và destination khác nhau. Bổ sung manual override, backfill/resync runbook, destination rate-limit/partial failure handling và reconciliation. Completed sync với rejected rows không phải success toàn phần."),
            ("Architecture review ba trường hợp", "Case A sync descriptive account tier vào CRM với SoR rõ và idempotent upsert. Case B sync audience membership rồi auto-send message, cần purpose/consent, command dedupe và intervention logging. Case C sync operational status từ warehouse rồi agents sửa destination và ingest ngược, tạo bi-directional conflict/feedback. Với mỗi case vẽ nodes/edges, state authority, identity, retry/delete, privacy purpose, feedback và SLO owner. Chỉ ra violated constraint và smallest control; nếu operational criticality vượt platform capability, chuyển state computation/write vào operational service."),
        ),
        (
            "warehouse-derived field không mặc nhiên là operational source of truth",
            "mỗi field có authority và conflict rule",
            "primary key change làm CDC identity đổi",
            "record leaving segment không mặc nhiên hard delete",
            "full resync có thể duplicate side effects",
            "retry timeout cần idempotency key and outcome record",
            "upsert state khác action command",
            "purpose limitation áp cho further processing",
            "derived score có thể là sensitive inference",
            "sync cần approved-field allowlist",
            "intervention làm thay outcome distribution",
            "feedback lineage phải quay từ destination về source",
            "completed with rejected rows không phải full success",
            "operational SLO cần on-call and recovery",
            "bidirectional edits cần explicit conflict resolution",
        ),
    ),
    Lesson(
        200,
        "Lesson_200-lifecycle-and-the-operating-model",
        "Lifecycle and the Operating Model",
        "88-lifecycle-operating-model.md",
        "wiki.data-product.lifecycle-operating-model",
        "Sáu trạng thái data-product lifecycle được điều khiển bằng evidence gates, operating ownership, deprecation safeguards và support feedback như thế nào?",
        (BA, SO, SR),
        (BAL, SOL, SRL),
        (
            ("State machine có quyền và bằng chứng", "Proposed, build, certified, operate, deprecated và removed cần entry criteria, allowed actions, exit evidence, accountable owner và audit event. State không phải label tự sửa trong catalog. Proposed chưa được dùng cho decision; build chỉ ở controlled context; certified đúng version/scope/evidence; operate có SLO/on-call; deprecated vẫn phục vụ trong window có migration; removed không còn resolve nhưng audit/retention artifact có thể còn. Transition failure giữ product ở state cũ; emergency exception có owner, expiry và compensating control."),
            ("Certification bundle và invalidation", "Gate tổng hợp product boundary/owner/consumers, eight-attribute evidence của L188, contract/version, access/security negative tests, documentation hierarchy, findability/usability evidence, correctness/quality/freshness SLO, cost/adoption baselines và runbooks. Mỗi artifact có locator/hash, environment, evidence date và reviewer. Certification không vĩnh viễn: semantic/security/source change, evidence expiry, incident hoặc owner departure kích re-review/suspend. Catalog có thể hiển thị state nhưng không tự chứng nhận correctness; Backstage docs cũng phân biệt catalog hub với authoritative external systems."),
            ("Operating model", "Mỗi product có business owner, technical owner, steward và on-call/escalation theo criticality; đội nhỏ có thể một người giữ nhiều role nhưng decision rights vẫn rõ. Severity matrix dựa impact, scope, security/privacy, decision deadline và workaround. Ghi response target khác resolution target, communication cadence, status channel, handoff và post-incident review. SLO budget liên kết operating capacity; không hứa operational response cho reverse-ETL workflow nếu analytics platform không có trực, replay và reconciliation."),
            ("Feedback phải được phân loại", "Support event lưu persona, task, product/version, channel, category, severity, resolution, recurrence và linked artifact. Categories gồm product defect, data incident, docs/findability gap, access, skill, unsupported request và novel analysis. Roadmap nói câu hỏi lặp lại luôn là lỗi thiết kế thay vì training need; đây là tuyệt đối hóa. Repetition là signal điều tra: có thể do interface/docs, onboarding, role change, policy hoặc task ngoài scope. Chọn intervention bằng root-cause evidence; test lại recurrence và task outcome sau thay đổi."),
            ("Deprecation và removal an toàn", "Trigger gồm replacement, no active decision, cost/risk, owner withdrawal hoặc compliance change. Inventory query logs, lineage, subscriptions, service accounts, offline exports và long-cadence users; zero recent queries không chứng minh zero consumer. Deprecation record có replacement/mapping, notices, window, telemetry, exceptions, retention, archive và rollback/restore. Block removal nếu critical consumer chưa migrate, legal/audit retention chưa giải quyết hoặc destination sync còn dependency. Removed catalog entry có thể giữ tombstone để ngăn asset cũ bị tái dùng."),
            ("Metrics điều khiển lifecycle", "Certified/operated product theo correctness/SLO/security cùng adoption, support dependence, decision evidence, cost-to-serve và consumer satisfaction. Không dùng một composite score che automatic-fail gate. Trend và segment quan trọng hơn snapshot; metric definition/version đi cùng product. Low adoption mở discovery, không auto-retire; high adoption tăng change/incident rigor. Cost spike mở investigation; cutting quality không được coi là optimization. Feedback, incidents và failed tasks tạo backlog có owner và verification, không chỉ thêm training."),
            ("Lab ba products và fault cases", "Dựng state-transition table và certification checklist. Product A đủ bundle đi certify→operate; B thiếu usability evidence bị chặn; C đang deprecated nhưng có hidden quarterly export nên removal fail. Tiêm owner departure, freshness breach, repeated question và security change để kiểm invalidation/escalation. Với ba repeated questions, phân loại root cause rồi đề xuất design/docs/training/policy change phù hợp; không ép tất cả thành design. Done khi transitions có evidence, blocked states giữ nguyên, consumer migration/retention đầy đủ và feedback change có retest plan."),
        ),
        (
            "lifecycle state có entry exit evidence và owner",
            "catalog label không tự tạo certification",
            "certification gắn product version and scope",
            "evidence expiry kích recertification",
            "response target khác resolution target",
            "on-call requirement theo product criticality",
            "support event cần task version and category",
            "repeated question là investigation signal không mặc nhiên design defect",
            "training vẫn đúng khi root cause là skill or role change",
            "zero recent queries không chứng minh zero consumer",
            "deprecation record có replacement telemetry and exceptions",
            "removal bị chặn bởi retention or hidden consumer",
            "composite score không che automatic fail gate",
            "high adoption làm tăng change rigor",
            "feedback action cần retest evidence",
        ),
    ),
)

VERIFY = {
    196: "Dựng policy matrix và synthetic principals; chạy positive/negative cases ở BI, SQL và API. Chạy workload scenarios có p95/concurrency/overload thresholds, result/security assertions và de-identification risk review trên fixture non-production.",
    197: "Từ versioned access/task/decision/support events, tính goals–signals–metrics theo cohort và natural cadence. Inject bots, scheduled refresh, abandon, confident-wrong và mandatory cross-check; kiểm denominator, segmentation, gaming và guardrails.",
    198: "Reconcile direct, shared và unallocated amounts với billing/usage/support artifacts. Chạy ít nhất hai allocation policies, hai unit denominators và one changed freshness constraint; lưu sensitivity, uncertainty và consumer migration analysis.",
    199: "Vẽ source–model–sync–destination–action–event loop; inject timeout-after-commit, duplicate key, key change, removed row, purpose mismatch và rejected destination rows. Kiểm idempotency, authority, privacy, reconciliation và intervention lineage.",
    200: "Đưa ba products qua transition table; inject missing usability evidence, owner departure, hidden long-cadence consumer, retention hold và repeated support questions. Mỗi state/gate/finding cần exact artifact, owner, decision và retest plan.",
}

QUERIES = {
    196: ["Làm sao kiểm policy parity giữa BI SQL và API?", "p95 load test cần những điều kiện workload nào?", "Masking khác de-identification ở điểm nào?"],
    197: ["Active user cadence phải theo nhịp quyết định ra sao?", "Tại sao cross-check rate không phải nghịch đảo trực tiếp của trust?", "Support-free answer rate cần guardrail nào?"],
    198: ["Bốn nhóm cost-to-serve gồm gì?", "Shared cost allocation làm thay đổi ranking sản phẩm thế nào?", "Khi nào low-use product không nên bị khai tử?"],
    199: ["Reverse ETL khi nào tạo shadow operational system?", "Upsert state khác side-effect command như thế nào?", "Feedback loop từ activation làm sai phân tích ra sao?"],
    200: ["Sáu trạng thái data-product lifecycle có gate gì?", "Câu hỏi lặp lại có luôn là design defect không?", "Removal gate phải tìm hidden consumers bằng cách nào?"],
}

NEW_SOURCES = (
    {"source_id": NI, "record_path": "1_Nguon/Web/SRC-NIST-SP-800-188-DEIDENTIFICATION.md", "canonical_url": "https://csrc.nist.gov/pubs/sp/800/188/final", "captured": "2026-10-01", "rights": "public-government-document"},
    {"source_id": HE, "record_path": "1_Nguon/Web/SRC-GOOGLE-HEART-UX-METRICS.md", "canonical_url": "https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/", "captured": "2026-10-01", "rights": "public-research-page"},
    {"source_id": FA, "record_path": "1_Nguon/Web/SRC-FINOPS-ALLOCATION.md", "canonical_url": "https://framework.finops.org/framework/capabilities/allocation/", "captured": "2026-10-01", "rights": "public-web-content"},
    {"source_id": FU, "record_path": "1_Nguon/Web/SRC-FINOPS-UNIT-ECONOMICS.md", "canonical_url": "https://www.finops.org/framework/capabilities/unit-economics/", "captured": "2026-10-01", "rights": "public-web-content"},
    {"source_id": HI, "record_path": "1_Nguon/Web/SRC-HIGHTOUCH-REVERSE-ETL-SYNCS.md", "canonical_url": "https://hightouch.com/docs/syncs/types-and-modes", "captured": "2026-10-01", "rights": "public-web-documentation"},
    {"source_id": IC, "record_path": "1_Nguon/Web/SRC-ICO-PURPOSE-LIMITATION.md", "canonical_url": "https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-protection-principles/a-guide-to-the-data-protection-principles/the-principles/purpose-limitation/", "captured": "2026-10-01", "rights": "public-regulator-guidance"},
    {"source_id": BA, "record_path": "1_Nguon/Web/SRC-BACKSTAGE-SOFTWARE-CATALOG.md", "canonical_url": "https://backstage.io/docs/features/software-catalog/", "captured": "2026-10-01", "rights": "public-web-documentation"},
)


def folder(lesson: Lesson):
    return BASE / lesson.directory


def frontmatter(lesson: Lesson) -> str:
    sources = "\n".join(f"  - {source}" for source in lesson.sources)
    return f"""---
note_id: {lesson.note_id}
note_type: concept-deep-dive
status: review
language: vi
created: 2026-10-01
last_verified: 2026-10-01
editorial_pass: humanized-v1
primary_question: {lesson.question}
source_ids:
{sources}
aliases: [{lesson.title}]
tags: [wiki/database-systems, data-product, operations, governance]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/{lesson.filename}
---
"""


def deep_note(lesson: Lesson) -> str:
    parts = [frontmatter(lesson), f"# {lesson.title}\n\n> [!abstract] Câu hỏi trung tâm\n> {lesson.question}\n"]
    for index, (heading, body) in enumerate(lesson.core, 1):
        parts.append(f"\n## {index}. {heading}\n\n{body}\n")
    parts.append("\n## 8. Ma trận kiểm chứng từng mệnh đề\n\nMọi kết luận cần raw artifact, version và failure signal. Một dashboard xanh, sync completed, catalog label hoặc bảng cost có số không tự chứng minh correctness, security, value hay readiness.\n")
    for index, probe in enumerate(lesson.probes, 1):
        parts.append(
            f"\n### 8.{index}. {probe}\n\n"
            f"**Mệnh đề cần kiểm.** {probe}.\n\n"
            f"**Cách kiểm.** {VERIFY[lesson.number]} Với mệnh đề này, ghi environment/product/policy version, input shape, expected observation, failure signal và boundary làm kết luận không còn đúng.\n\n"
            "**Bằng chứng đạt.** Lưu contract/policy, fixture hoặc event extract, command/query, raw output, numerator–denominator hoặc cost reconciliation, reviewer và artifact hash. Nếu chưa chạy lab trên hệ được phép, chỉ ghi protocol; không biến expected result thành evidence.\n"
        )
    parts.append(
        """
## 9. Quy trình phản biện

1. Chốt product, consumer, decision, environment và criticality trước khi chọn metric hoặc control.
2. Tách tool capability, configured policy, observed behavior và business outcome.
3. Ghi stable IDs, versions, time window, denominator, allocation hoặc identity rules.
4. Kiểm negative/failure path, overload, retry, stale state, hidden consumer và changed constraint.
5. Phân loại source fact, curriculum synthesis, organizational policy và untested hypothesis.
6. Lưu uncertainty, unallocated/unknown set và stop condition; không ép bảng phải cho kết luận.
7. Chưa có execution evidence thì giữ trạng thái `review`.

## 10. Câu hỏi tự kiểm tra

1. Invariant hoặc decision nào đang được bảo vệ?
2. Chủ thể, resource, event hay cost unit được định danh bằng gì?
3. Denominator, time window và unknown/unallocated set là gì?
4. Failure nào vẫn cho tín hiệu xanh hoặc “completed”?
5. Thay đổi nào làm policy, metric, allocation hoặc state transition phải xem lại?
6. Ai có quyền duyệt, ai vận hành và bằng chứng nào còn chưa chạy?

## 11. Giới hạn và điều chưa cho phép kết luận

- Chưa chạy security/load test, adoption analysis, cost allocation, reverse-ETL fault injection hoặc lifecycle exercise; note mô tả protocol và expected evidence.
- Tài liệu web được kiểm ngày 2026-10-01; feature, pricing, law/guidance và vendor behavior có thể đổi.
- Metrics, cost categories, shadow-system constraints và six-state lifecycle là curriculum synthesis; không gán nguyên văn cho một nguồn.
- Guidance privacy không thay legal review; performance/security examples không thay threat model và production authorization.
- Note giữ trạng thái `review` cho tới khi chủ dự án duyệt semantic meaning.
"""
    )
    references = "\n".join(f"{index}. [[{link}]]" for index, link in enumerate(lesson.source_links, 1))
    coverage = "\n".join(
        f"| [[{link}]] | Khái niệm, mechanism hoặc governance boundary liên quan | Đã đọc locator trong source record; không suy ngoài phạm vi |"
        for link in lesson.source_links
    )
    takeaway = {
        196: "Policy parity cần negative evidence ở từng serving surface; performance và de-identification là hai gates riêng.",
        197: "Adoption metric bắt đầu từ goal và value event; activity, entitlement và trust proxy mơ hồ không thay outcome.",
        198: "Cost-to-serve phải reconcile direct/shared/unallocated, kiểm sensitivity và ghép unit cost với value guardrails.",
        199: "Reverse ETL an toàn cần authority, identity, idempotency, purpose và feedback lineage rõ trước operational use.",
        200: "Lifecycle là state machine dựa evidence; catalog state, repeated ticket hay zero usage không tự quyết transition.",
    }
    parts.append(
        f"""
## Reference

{references}

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
{coverage}

## Key takeaways

- {takeaway[lesson.number]}
- Mọi phép đo hoặc gate cần stable version, owner, denominator/scope và failure evidence.
- Signal dễ lấy không được dùng thay decision outcome, correctness hoặc user safety.
- Unknown consumers, unallocated costs, rejected rows và expired evidence phải hiển thị, không mặc định bằng zero.
- Chưa chạy lab thì artifact là tài liệu học thuật đã kiểm cấu trúc, không phải chứng nhận production.
"""
    )
    return "".join(parts)


def curriculum(lesson: Lesson, knowledge: str):
    outcome, assessment, lab, pitfalls, homework, done = previous.previous.shared.contract(lesson)
    header = f"# Phase 5: Modeling, Semantics and Analytical Product\n# Module 13: Analytical Data Product and Self-service\n# Lesson {lesson.number}: {lesson.title}"
    body = re.sub(r"^---\n.*?\n---\n", "", knowledge, flags=re.S)
    body = re.sub(r"^# .+\n+", "", body, count=1)
    note = f"{header}\n\n## Mục tiêu bài học\n\n**Năng lực cần chứng minh.** {outcome}\n\n**Điều kiện hoàn thành.** {done}\n\n{body}"
    safety = "Chỉ dùng fixture, synthetic principals, isolated load environment và cost/event extracts đã loại dữ liệu nhạy cảm. Không mở quyền production, load-test hệ dùng chung, gửi reverse-ETL action thật, xóa product hoặc thu personal data. Lưu versions, commands, raw outputs, unknown sets, approvals mô phỏng và limitations."
    questions = "\n".join(
        f"{index}. {question}"
        for index, question in enumerate(
            (
                "Nêu invariant, product scope và owner trung tâm.",
                "Đưa một failure vẫn có thể tạo tín hiệu xanh hoặc completed.",
                "Nêu denominator, identity hoặc allocation rule cần khóa trước khi đo.",
                "Phân biệt protocol đã viết với evidence đã quan sát.",
            ),
            1,
        )
    )
    after = f"{header}\n\n## Thực hành\n\n**Nhiệm vụ.** {lab}\n\n{safety}\n\n## Kiểm tra cuối bài\n\n{questions}\n\n## Tiêu chí hoàn thành\n\n**Cách đánh giá.** {assessment}\n\n**Điều kiện đạt.** {done}\n\n## Bài làm sau buổi học\n\n**Nhiệm vụ.** {homework}\n\n**Lỗi cần chủ động loại trừ.** {pitfalls}\n\n## Reference\n\n- Knowledge note: `{(PACK / lesson.filename).relative_to(ROOT)}`\n- Nội dung học thuật: `note.md` cùng thư mục.\n"
    return note, after


def update_manifest(check: bool = False):
    path = ROOT / "Docs/Second-Brain/second-brain-manifest.json"
    data = json.loads(path.read_text())
    new_source_ids = {source["source_id"] for source in NEW_SOURCES}
    data["source_registry"] = [source for source in data["source_registry"] if source.get("source_id") not in new_source_ids] + list(NEW_SOURCES)
    note_ids = {lesson.note_id for lesson in LESSONS}
    data["note_registry"] = [note for note in data["note_registry"] if note.get("note_id") not in note_ids]
    data["retrieval_test_set"] = [test for test in data["retrieval_test_set"] if test.get("expected_note_id") not in note_ids]
    for lesson in LESSONS:
        data["note_registry"].append({
            "note_id": lesson.note_id,
            "path": f"2_Wiki/Database-Systems/{lesson.title}.md",
            "status": "review",
            "source_ids": list(lesson.sources),
            "last_verified": "2026-10-01",
        })
        data["retrieval_test_set"].extend({"query": query, "expected_note_id": lesson.note_id} for query in QUERIES[lesson.number])
    data["version"] = "1.0.39"
    data["updated_at"] = "2026-10-01T23:10:00+07:00"
    data["layers"]["1_Nguon"]["source_count"] = len(data["source_registry"])
    data["layers"]["2_Wiki"]["note_count"] = len(data["note_registry"])
    expected = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    if check:
        return [] if path.read_text() == expected else [str(path.relative_to(ROOT))]
    path.write_text(expected)
    return []


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    stale = []
    for lesson in LESSONS:
        knowledge = normalize_markdown(deep_note(lesson))
        note, after = curriculum(lesson, knowledge)
        targets = (
            (PACK / lesson.filename, knowledge),
            (WIKI / f"{lesson.title}.md", knowledge),
            (folder(lesson) / "note.md", note),
            (folder(lesson) / "after-note.md", after),
        )
        for path, content in targets:
            if args.check:
                if not path.exists() or path.read_text() != content:
                    stale.append(str(path.relative_to(ROOT)))
            else:
                path.write_text(content)
    stale.extend(update_manifest(args.check))
    if stale:
        print("STALE\n" + "\n".join(stale))
        return 1
    print(("checked" if args.check else "written") + f"={len(LESSONS) * 4} stale=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
