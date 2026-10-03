#!/usr/bin/env python3
"""Build source-grounded L191-L195 documentation and usability notes."""
from __future__ import annotations

import argparse
import json
import re

import promote_l186_l190_notes as previous
from format_knowledge_notes import normalize_markdown
from promote_l140_l144_notes import Lesson

ROOT = previous.ROOT
BASE = previous.BASE
PACK = previous.PACK
WIKI = previous.WIKI

DI = "src.web.diataxis-framework"
DH = "src.web.datahub-search"
DB = "src.web.dbt-documentation"
GH = "src.web.github-status-checks"
GS = "src.web.govuk-simple-to-use"
GM = "src.web.govuk-moderated-usability-testing"
GB = "src.web.govuk-usability-benchmarking"
NN = "src.web.nngroup-usability-sample-size"
SM = "src.book.sommerville-software-engineering.10e"
DM = "src.web.dehghani-data-mesh-principles"
GU = "src.web.govuk-understand-user-needs"

DIL = "SRC-DIATAXIS-FRAMEWORK"
DHL = "SRC-DATAHUB-SEARCH"
DBL = "SRC-DBT-DOCUMENTATION"
GHL = "SRC-GITHUB-STATUS-CHECKS"
GSL = "SRC-GOVUK-SIMPLE-TO-USE"
GML = "SRC-GOVUK-MODERATED-USABILITY-TESTING"
GBL = "SRC-GOVUK-USABILITY-BENCHMARKING"
NNL = "SRC-NNGROUP-USABILITY-SAMPLE-SIZE"
SML = "SRC-SOMMERVILLE-SOFTWARE-ENGINEERING-10E"
DML = "SRC-DEHGHANI-DATA-MESH-PRINCIPLES"
GUL = "SRC-GOVUK-UNDERSTAND-USER-NEEDS"

LESSONS = (
    Lesson(
        191,
        "Lesson_191-the-documentation-hierarchy",
        "The Documentation Hierarchy",
        "79-documentation-hierarchy.md",
        "wiki.data-product.documentation-hierarchy",
        "Bộ tài liệu cho data product phải tách theo nhu cầu đọc nào, đồng bộ với product ra sao và được kiểm bằng hành vi nào thay vì số trang?",
        (DI, DB, SM),
        (DIL, DBL, SML),
        (
            ("Tài liệu là một hệ giao diện", "Tài liệu không phải phần giải thích thêm sau khi product đã hoàn tất. Consumer dựa vào tên, mô tả, ví dụ, grain, cutoff và limitation để quyết định có dùng product hay không; do đó các thành phần này thuộc public interface. Hệ tài liệu phải có owner, version, effective date, product/contract ID và đường báo lỗi. Một trang dài chứa đủ mọi thứ vẫn có thể thất bại nếu người mới không biết bắt đầu ở đâu. Đơn vị đánh giá không phải số chữ mà là tác vụ: chọn đúng product, chạy được use case đầu, tra được một field và biết kết luận nào bị cấm."),
            ("Bốn tầng theo bốn câu hỏi", "Tầng discovery trả lời product là gì, dành cho quyết định nào, owner và trust state nào. Tầng getting-started đưa prerequisite, access path, ba ví dụ chạy được và expected result. Tầng reference mô tả grain, keys, fields, metric contracts, freshness, quality, security và version. Tầng context giải thích design decisions, assumptions, trade-offs, known gaps và interpretation limits. Diátaxis phân loại tutorial, how-to, reference và explanation theo nhu cầu người đọc; hierarchy của bài là synthesis cho data product, không phải tên bốn quadrant nguyên văn của Diátaxis."),
            ("Discovery phải hỗ trợ quyết định nhanh", "Một discovery card tốt cho phép người đọc loại product không phù hợp mà không mở schema. Nó nêu business capability, population, time coverage, supported questions, prohibited questions, owner, certification state, freshness và link truy cập. Ngưỡng 30 giây là acceptance target nội bộ cần đo, không phải quy luật nhận thức. Nếu card dùng tên bảng kỹ thuật, liệt kê hàng trăm cột hoặc che giấu limitation, người đọc có thể chọn sai nhanh hơn. Negative fit statement, chẳng hạn không dùng cho causal attribution hoặc real-time operations, có giá trị ngang danh sách use cases."),
            ("Getting-started phải thực thi được", "Ba example queries đại diện happy path, boundary case và common filter/join. Mỗi ví dụ pin product/version, environment, role, parameters, expected columns, row-shape và cutoff. Test chỉ parse SQL là chưa đủ; query phải chạy trên fixture hoặc safe environment và assertion phải phát hiện empty result, wrong grain hoặc semantic drift. Credentials, secrets và production identifiers không được hard-code. Ví dụ cần copy-run được nhưng cũng phải giải thích điều kiện đúng, nếu không người dùng sẽ sao chép query ngoài population hoặc time window hợp lệ."),
            ("Reference sinh từ source of truth", "Reference mô tả chính xác, ít diễn giải và dễ tra cứu. Phần có thể sinh từ contract/schema/semantic config nên generate thay vì chép tay: columns, types, keys, metric IDs, dimensions, version và lineage. dbt có thể kết hợp descriptions với metadata introspect và lineage, nhưng cột xuất hiện trên docs không có nghĩa cột đã được mô tả. Generated reference cần build timestamp và artifact fingerprint; phần curated như business definition, exception, sensitive-use rule vẫn cần owner review. Wiki được phép làm entry point, nhưng source-of-truth link phải quay về version cạnh code."),
            ("Context giữ lý do và ranh giới diễn giải", "ADR hoặc explanation record lưu vì sao chọn grain, population, time, source, aggregation và privacy control; alternatives nào bị loại; điều kiện nào buộc xem lại. Interpretation limits phải viết thành câu kiểm được: dữ liệu quan sát không chứng minh causal effect; snapshot không dùng cho event sequence; missing segment làm comparison lệch. Ba nội dung nhanh lạc hậu nếu viết tay là dynamic schema inventory, current usage leaderboard và operational status; chúng nên được generate hoặc link live system. Context không được trộn vào reference đến mức người tra type phải đọc một bài luận."),
            ("Kiểm hierarchy bằng người lạ và drift", "Test có hai lớp. Lớp consumer: người chưa biết product quyết định fit/no-fit, xin quyền hoặc dùng fixture, chạy query đầu, giải thích grain/freshness/limitation; ghi thời gian, lỗi và câu hỏi hỗ trợ. Lớp consistency: contract version, public fields, metric IDs, sample queries và schedule promises khớp artifacts hiện hành. Một người hoàn tất nhanh nhưng hiểu sai là failure; một bộ docs đúng kỹ thuật nhưng không ai tìm được cũng là failure. Khi người dùng hỏi, không trả lời trực tiếp trước khi ghi lại điểm thiếu trong information architecture."),
        ),
        (
            "bốn tầng phục vụ bốn reader jobs khác nhau",
            "discovery card cho phép cả fit và no-fit decision",
            "30 giây là target cần đo chứ không là định luật",
            "getting-started examples phải chạy và có expected result",
            "example query cần pin version và cutoff",
            "reference ưu tiên generated metadata",
            "generated docs vẫn có thể thiếu descriptions",
            "context lưu alternatives và reversal triggers",
            "interpretation limit phải quan sát được",
            "dynamic inventory không nên chép tay",
            "wiki entry point không thay source of truth",
            "consumer test cần explain-back",
            "hoàn tất nhanh nhưng hiểu sai vẫn là failure",
            "documentation version gắn product version",
            "mỗi câu hỏi hỗ trợ tạo một finding có owner",
        ),
    ),
    Lesson(
        192,
        "Lesson_192-search-discovery-and-the-findability-test",
        "Search, Discovery and the Findability Test",
        "80-search-discovery-findability-test.md",
        "wiki.data-product.findability-test",
        "Findability của data product được đo bằng tác vụ tìm kiếm, query logs và failed vocabulary như thế nào mà không đánh đồng catalog coverage với kết quả người dùng?",
        (DH, DM, GU),
        (DHL, DML, GUL),
        (
            ("Findability là outcome của một nhu cầu", "Một asset chỉ được xem là tìm thấy khi người dùng có nhu cầu xác định, truy cập từ điểm bắt đầu thực tế, chọn đúng product trong giới hạn thời gian và giải thích được vì sao nó phù hợp. Số assets đã ingest, số trường metadata hay việc search endpoint trả 200 chỉ là input/capability. Denominator phải là search tasks hợp lệ; numerator là tasks tìm đúng product mà không có trợ giúp ngoài protocol. Nếu product không tồn tại hoặc user không có quyền thấy nó, task phải được phân loại riêng thay vì tính như lỗi ranking."),
            ("Bốn bề mặt metadata", "Name dùng business vocabulary và tránh mã pipeline làm primary label. One-line description nêu population, outcome/use case và time scope. Domain/tags/glossary terms hỗ trợ synonyms và filter nhưng cần governance để không thành tag soup. Trust state nêu certified, experimental, deprecated hoặc restricted cùng owner và evidence date. DataHub search cho thấy engine có thể match names, descriptions, tags, terms, owners và columns; kết quả tốt hơn khi metadata liên quan được ingest. Đây là mechanism, không phải bằng chứng findability."),
            ("Thiết kế task và tập người dùng", "Task viết theo intent, không đưa tên product hoặc keyword mà metadata đang dùng; ví dụ “tìm nguồn trả lời tỷ lệ khách hàng quay lại theo cohort” thay vì “tìm mart customer_retention”. Bao phủ distinct roles, vocabulary và access contexts. Mỗi participant bắt đầu từ catalog/search entry point họ thực sự dùng. Với formative vòng nhỏ, báo observed rate cùng n và từng case; không biến 3/5 thành ước lượng population chính xác. Nếu so hai vòng bằng hai nhóm khác nhau, giữ task difficulty và recruitment criteria tương đương."),
            ("Failed-query vocabulary là evidence", "Ghi raw query, reformulations, clicked results, rank của target, filters, time, abandon, wrong selection và câu hỏi hỗ trợ. Phân loại failure: vocabulary mismatch, missing metadata, ranking, trust ambiguity, permission visibility, duplicate product, stale/deprecated result hoặc product gap. Sửa đúng nguyên nhân: thêm synonym khi mismatch, không nhồi mọi keyword vào title; hide/de-rank deprecated assets thay vì chỉ thêm badge; hợp nhất duplicates hoặc chỉ canonical product. Query logs không có intent đầy đủ nên cần session observation."),
            ("Ranking, access và trust tương tác", "Text relevance cao không đủ nếu top result stale, inaccessible hoặc không certified. Usage signal có thể củng cố popularity bias: product cũ tiếp tục đứng cao vì đã phổ biến, product tốt hơn không được khám phá. Certification boost có thể che product phù hợp ngách. Search evaluation cần relevance judgments theo task, permission-aware expected set và trust-state policy. Một product bị loại vì không có quyền nhưng hiện kết quả không thể hành động tạo frustration; ẩn hoàn toàn lại che path xin quyền. Thiết kế phải nói rõ trạng thái và next action."),
            ("Hai vòng sửa có kiểm soát", "Baseline đóng băng catalog snapshot, tasks, expected products, participant criteria và timebox. Sau vòng một, tạo change log nối failure class với name/description/tag/ranking/trust fix. Vòng hai dùng participants mới để giảm learning effect; giữ task semantics tương đương. So task-level completion, median/time distribution, wrong-product rate và assistance count; với mẫu nhỏ, mô tả quan sát và case evidence thay vì tuyên bố significance. Nếu tỷ lệ tăng vì task dễ hơn hoặc target được gợi ý, không được ghi là product cải thiện."),
            ("Findability không kết thúc ở click", "Người dùng có thể click đúng asset nhưng không xác nhận grain, freshness hoặc limitation, nên discovery success cần một explain-back ngắn. Success funnel gồm search attempt → target visible → target selected → fit verified → access/use next step. L192 tập trung đoạn đầu nhưng phải ghi rơi rụng ở đoạn sau để chuyển cho L191, L194 và L195. Duplicate self-built assets là signal cần điều tra: đôi khi do không tìm thấy, đôi khi do trust, performance, access hoặc contract không phù hợp; không gán mọi bản sao cho search failure."),
        ),
        (
            "catalog coverage khác findability outcome",
            "denominator là valid user-needs tasks",
            "product gap không được tính như ranking failure",
            "business names không dùng technical table code làm primary label",
            "description phải nêu population use case và time scope",
            "tags cần controlled vocabulary",
            "trust state có owner và evidence date",
            "task không được lộ tên product",
            "small sample rate phải kèm numerator denominator",
            "failed terms cần raw query và reformulation",
            "usage ranking có popularity bias",
            "permission state ảnh hưởng discovery actionability",
            "round comparison giữ task difficulty tương đương",
            "click đúng nhưng hiểu sai chưa phải success",
            "duplicate asset không luôn là findability failure",
        ),
    ),
    Lesson(
        193,
        "Lesson_193-documentation-tests",
        "Documentation Tests",
        "81-documentation-tests.md",
        "wiki.data-product.documentation-tests",
        "Làm sao biến tài liệu data product thành artifact có bốn nhóm kiểm tự động, mutation tests và merge gate nhưng vẫn giữ phần review cần phán đoán của con người?",
        (DB, GH, SM),
        (DBL, GHL, SML),
        (
            ("Test contract thay vì test file tồn tại", "Một README tồn tại hoặc site docs build thành công chỉ chứng minh pipeline tạo được artifact. Documentation test phải nối public contract với nội dung được công bố và hành vi người dùng. Bốn nhóm tối thiểu của bài là public-field coverage, executable examples, semantic-reference integrity và freshness-promise consistency. Mỗi rule có stable code, severity, owner, input artifacts, failure message và remediation link. Rule phải chỉ ra field/query/metric/schedule cụ thể; thông báo “docs invalid” không đủ để sửa."),
            ("Public-field coverage", "Lấy public surface từ contract hoặc versioned schema, không từ toàn warehouse relation. So stable field IDs/names với description records; reject missing, placeholder, copy-paste trùng hoặc description không có business meaning theo policy. dbt introspection có thể hiện undocumented columns, vì vậy generated page vẫn cần completeness assertion. Khi field được remove/rename, docs entry cũ phải deprecate hoặc xóa theo version; orphan descriptions cũng là drift. Sensitive/internal fields không được ép document công khai chỉ để đạt coverage."),
            ("Executable examples", "Extract code blocks được đánh dấu runnable, dựng environment/fixture và chạy bằng read-only principal. Assert parse/compile, execution, non-empty khi contract hứa có data, expected columns/types, grain/uniqueness và một semantic control total. Ví dụ parameterized phải có safe defaults; time-relative query cần fixed clock hoặc bounded assertion để tránh flaky. Test không chạy unrestricted query trên production. Snapshot output quá rộng dễ che drift; assertion chọn property liên quan mục đích ví dụ."),
            ("Semantic reference integrity", "Mọi metric, dimension, enum, glossary term, owner và product version được nhắc phải resolve stable ID trong registry hiện hành. Text matching tên hiển thị không đủ vì rename/alias. Deprecated reference có thể cho warning trong cửa sổ nhưng fail sau deadline. Kiểm dependency graph phát hiện broken anchor, missing target và circular navigation; semantic meaning vẫn cần human review. Một metric tồn tại nhưng docs mô tả sai population không bị existence test phát hiện, nên semantic regression hoặc owner attestation vẫn cần."),
            ("Freshness promise consistency", "Machine-readable docs promise gồm schedule/timezone, expected cutoff, SLO window, holiday/backfill semantics và incident behavior. So với orchestrator/config/service-level artifact, không so với một run gần nhất. Schedule match không chứng minh data thật sự fresh; operational monitor kiểm observed freshness là lớp khác. Nếu pipeline đổi từ hourly sang daily mà docs vẫn hourly, gate phải fail trong cùng change. Nếu emergency override có expiry, docs hiển thị trạng thái tạm và quay lại tự động."),
            ("Mutation testing và cửa chặn", "Tiêm bốn mutations độc lập: public column không description; example query hỏng hoặc sai grain; metric ID đã retire; schedule thay không cập nhật promise. Mỗi mutation phải fail đúng rule code, còn baseline sạch phải pass. False positive/negative được lưu để cải tiến rules. GitHub required status check có thể chặn merge khi CI fail, nhưng chỉ sau khi branch protection cấu hình đúng; một job optional xanh/đỏ không tạo gate. Kiểm cả bypass authority và audit trail để tránh rule chỉ áp với contributor thường."),
            ("Ba phần bắt buộc review người", "Thứ nhất, liệu discovery/context có trả đúng user need và tránh ngôn ngữ mơ hồ. Thứ hai, interpretation limits, causal caveat, trade-off và design rationale có đầy đủ hay không. Thứ ba, ví dụ có đại diện use case, dễ dùng và không khuyến khích practice nguy hiểm. Automated lint hỗ trợ nhưng không chứng minh clarity hoặc truth. Review có checklist, named reviewer, exact artifact hash và expiry; “đã đọc” không phải evidence. Escaped documentation defect phải tạo regression rule nếu có thể tự động hóa mà không làm rule quá nhiễu."),
        ),
        (
            "file existence không chứng minh documentation correctness",
            "public surface là oracle cho field coverage",
            "generated docs có thể chứa undocumented columns",
            "orphan description cũng là drift",
            "runnable example cần read-only fixture",
            "example assertion kiểm grain và semantics",
            "time-relative example cần fixed clock",
            "metric references resolve stable IDs",
            "existence test không phát hiện wrong population",
            "freshness promise khác observed freshness",
            "schedule change phải cập nhật docs trong same change",
            "mỗi mutation fail đúng rule code",
            "status check chỉ là gate khi required",
            "human review giữ interpretation and clarity",
            "review gắn exact artifact hash",
        ),
    ),
    Lesson(
        194,
        "Lesson_194-self-service-ux-and-the-enablement-boundary",
        "Self-Service UX and the Enablement Boundary",
        "82-self-service-ux-enablement-boundary.md",
        "wiki.data-product.self-service-enablement-boundary",
        "Một data product chỉ được gọi là self-service khi bốn điều kiện nào có bằng chứng, và ranh giới hỗ trợ được thiết kế ra sao để vừa giảm phụ thuộc vừa không đẩy rủi ro sang người dùng?",
        (DM, GS, GU),
        (DML, GSL, GUL),
        (
            ("Self-service là khả năng hoàn tất việc", "Cấp quyền chỉ mở một cánh cửa. Self-service đạt khi người dùng thuộc persona đã định có thể tìm đúng product, hiểu nghĩa, thao tác bằng interface phù hợp và tin kết quả trong một class câu hỏi, với mức trợ giúp đã công bố. Scope phải nêu role, task, stakes, environment và excluded decisions. Một analyst tự viết SQL phức tạp không chứng minh business user tự phục vụ; một dashboard dễ dùng cũng không chứng minh metric đúng. GOV.UK nhấn mạnh thành công lần đầu với trợ giúp tối thiểu và kiểm với actual/likely users; giáo trình chuyển nguyên tắc đó sang analytical product."),
            ("Bốn điều kiện và evidence", "Findable: task test có success/time/failed terms. Understandable: explain-back về grain, population, time, dimensions và limits. Usable: hoàn tất representative task qua public interface mà không cần workaround hay SQL vượt năng lực persona. Trustworthy: result reconciled, freshness/quality/security visible và người dùng phản ứng đúng khi status degraded. Chấm pass/partial/fail với locator và observation, không chấm cảm nhận. Bốn điều kiện là AND gate trong scope; access count, page views hoặc training attendance không thay được."),
            ("Ba mức câu hỏi", "Mức 1 repeatable lookup: câu hỏi chuẩn, metric certified, dimensions hợp lệ, thao tác có path rõ. Mức 2 bounded exploration: slice/comparison mới nhưng vẫn trong semantic contract; cần skill về filters, uncertainty và data quality. Mức 3 analytical investigation: ambiguity, causal inference, forecast, policy trade-off hoặc novel modeling; cần analyst/data scientist và review. Classification dựa reasoning risk, reversibility, cost of error và contract coverage, không dựa chức danh người hỏi. Một câu hỏi có thể đổi mức khi product, evidence hoặc stakes đổi."),
            ("Ranh giới hỗ trợ hai phía", "Data team chịu product correctness, contract, access policy, reliability, documentation, supported paths, incident communication và enablement material. Consumer chịu đặt câu hỏi trong scope, chọn đúng cohort/time, tuân thủ interpretation limits, bảo vệ exports và báo lỗi kèm context. Shared duties gồm validation cho high-stakes use, change acceptance và vocabulary. Boundary ghi service channels, response class, escalation, office hours, unsupported requests và handoff criteria. Không dùng boundary để từ chối mọi help; cũng không nhận bespoke query vô hạn."),
            ("Enablement thay cho ticket treadmill", "Mỗi ticket được phân loại product defect, documentation gap, discoverability gap, access issue, skill gap hoặc novel analysis. Lỗi lặp chuyển thành product/docs/training change có owner; novel analysis đi intake riêng. Theo dõi assistance rate theo natural decision cadence, repeat-contact rate, time-to-independence và wrong-confident outcomes. Giảm ticket bằng cách từ chối hỗ trợ có thể làm metric đẹp nhưng đẩy shadow copies và sai số sang consumer. Guardrails gồm sampled outcome audit, user interviews và escalation accessibility."),
            ("Không phải mọi thứ nên tự phục vụ", "Causal claim, legal/regulatory interpretation, sparse subgroup, privacy-sensitive join, novel forecast và irreversible high-stakes decision thường cần chuyên gia. Một interface có thể cho phép query nhưng policy vẫn yêu cầu review. Honest stop message phải nêu vì sao, evidence còn thiếu, ai hỗ trợ và artifact cần chuẩn bị. Đây là feature an toàn, không phải failure của UX. Mục tiêu là self-service tối đa trong bounded safe space, không phải loại bỏ chuyên gia hoặc biến mọi consumer thành data engineer."),
            ("Chấm mười câu hỏi và kiểm ranh giới", "Lấy mười câu hỏi thật đủ ba mức, ẩn đáp án mẫu khỏi người chấm, ghi reasoning, contract coverage, required evidence, risk và route. Reviewer độc lập so classification; disagreements tạo decision rule mới. Với product hiện tại, chấm bốn điều kiện bằng artifact và observed task. Boundary one-pager được thử bằng tình huống: metric không reconcile, user cần causal answer, access expired, stale data, unsupported export. Done khi cả hai phía biết next action; wording “liên hệ data team” mà không owner/SLA/context yêu cầu là chưa đủ."),
        ),
        (
            "access entitlement không đồng nghĩa self-service",
            "self-service luôn có persona task và risk scope",
            "findable cần task evidence",
            "understandable cần explain-back",
            "usable phụ thuộc public interface và persona skill",
            "trustworthy cần degraded-state behavior",
            "bốn điều kiện là AND gate trong scope",
            "câu hỏi mức một là repeatable lookup",
            "bounded exploration khác causal investigation",
            "classification dựa reasoning risk không dựa title",
            "support boundary nêu trách nhiệm hai phía",
            "repeated ticket trở thành product finding",
            "ticket reduction cần wrong-outcome guardrail",
            "high-stakes causal question cần expert review",
            "stop message phải có rationale và next action",
        ),
    ),
    Lesson(
        195,
        "Lesson_195-task-based-usability-testing",
        "Task-Based Usability Testing",
        "83-task-based-usability-testing.md",
        "wiki.data-product.task-based-usability-testing",
        "Thiết kế hai vòng usability test cho analytical product như thế nào để quan sát task success, time, assistance và confident-wrong outcomes mà không biến năm người thành bằng chứng thống kê giả?",
        (GM, GB, NN),
        (GML, GBL, NNL),
        (
            ("Tách formative study và benchmark", "Formative qualitative test nhằm phát hiện cơ chế lỗi: vocabulary, navigation, interpretation, query construction, trust signal hoặc recovery. Benchmark quantitative nhằm ước lượng/so sánh metrics của population hoặc cohort với độ chính xác xác định. Một session có thể thu số, nhưng n=5 không biến tỷ lệ thành estimate đáng tin. NN/g đặt năm người trong qualitative iterative testing và nêu ngoại lệ; GOV.UK benchmark guidance đề xuất 30–60 actual/likely users trong bối cảnh benchmark. Roadmap dùng năm người mỗi vòng nên kết quả phải gọi là observed round evidence, không là chứng minh thống kê toàn population."),
            ("Research question, participant và consent", "Mỗi vòng bắt đầu bằng câu hỏi nghiên cứu và target persona. Recruit actual/likely users theo role, domain knowledge, data literacy, access context và assistive needs; distinct cohorts không được trộn rồi gọi đồng nhất. Ghi inclusion/exclusion, recruitment channel, incentive và no-show. Có informed consent cho recording, screen/data capture và retention; dùng synthetic hoặc properly governed data nếu task có thông tin nhạy cảm. Nhắc rõ kiểm product chứ không chấm người. Moderator không phải owner duy nhất chấm success nếu owner biết đáp án và muốn bảo vệ thiết kế."),
            ("Tác vụ trung tính và có oracle", "Task nêu goal nghiệp vụ, context và constraints, không nêu tên menu, product, metric hoặc sequence thao tác. Nó phải thực tế, đủ thách thức và có expected answer/acceptance range từ oracle độc lập. Ba task nên phủ discovery/no-fit, correct analysis và response to degraded/ambiguous state. Pilot với người ngoài mẫu phát hiện wording gợi ý, missing data và timing lỗi. Giữ task semantics giữa hai vòng; nếu product change buộc đổi task, đánh dấu non-comparable thay vì ép so."),
            ("Protocol không cứu người dùng", "Dùng introduction script và điều kiện bắt đầu nhất quán. Moderator yêu cầu think aloud cho mục tiêu định tính nhưng không chỉ đường; prompt trung tính như “bạn đang nghĩ gì?” được log riêng. Với time benchmark, think-aloud có thể làm thời gian chậm và moderator prompts tạo nhiễu, nên protocol metric phải chuẩn hóa hoặc tách. Assistance event có taxonomy: clarification về scenario, technical failure, hint, direct instruction. Stop criteria bảo vệ participant và hệ thống; downtime không được chấm thành UX failure."),
            ("Bốn số đo và denominator", "Task completion rate = correct completions / valid attempts, với success definition trước session. Time-to-correct-result tính từ task start tới verified correct output; censor abandon/time limit thay vì gán tùy ý. Assistance count chỉ so khi prompt policy thống nhất. Confident-wrong count yêu cầu participant tuyên bố hoàn tất/độ tin cậy rồi oracle cho biết result sai; wrong but uncertain là category khác. Ghi partial, abandon, technical invalid và no-opportunity. Median/distribution và task-level table có ích hơn một average che outlier."),
            ("Severity và vòng sửa", "Finding có observed behavior, task/step, frequency trong sample, consequence, recovery, affected cohort và evidence clip/note. Severity kết hợp impact và persistence/recovery; frequency nhỏ trong mẫu không đồng nghĩa hiếm trong population. Prioritize wrong-confident/high-stakes trước cosmetic delay. Mỗi fix nối tới mechanism hypothesis và expected metric/failure change. Vòng hai dùng người mới phù hợp cùng cohort để giảm memory; giữ environment, task oracle, moderator script và scoring. Regression task bảo đảm fix một điểm không làm hỏng path khác."),
            ("Diễn giải cải thiện trung thực", "Báo từng vòng bằng numerator/denominator, task distribution, participant composition và protocol deviations. “Ít nhất ba số cải thiện” là acceptance nội bộ; không cho phép cherry-pick direction hoặc che confidence-wrong tăng. Với mẫu nhỏ, kết luận “đã quan sát cải thiện ở vòng hai trong sample/protocol này”, kèm cases không cải thiện và alternative explanations. Muốn tuyên bố population improvement phải thiết kế benchmark/power/precision phù hợp. Không lấy satisfaction thay behavior; nhưng perception-confidence gap hữu ích để phát hiện kết quả sai mà tự tin."),
        ),
        (
            "qualitative issue discovery khác quantitative benchmark",
            "năm người không tạo population estimate đáng tin",
            "distinct user cohorts cần sampling riêng",
            "consent bao phủ recording và retention",
            "task wording không lộ interface path",
            "task success cần independent oracle",
            "pilot không tính vào final sample",
            "moderator prompt được log và phân loại",
            "think-aloud có thể làm nhiễu time metric",
            "completion denominator loại technical-invalid theo rule trước",
            "time-to-correct khác time-to-any-result",
            "confident-wrong cần self-assessed completion hoặc confidence",
            "severity không đồng nhất frequency trong sample",
            "round two giữ protocol và dùng participants mới",
            "small-sample improvement phải giới hạn phạm vi kết luận",
        ),
    ),
)

VERIFY = {
    191: "Dựng đủ bốn tầng cho một product/version; nhờ người chưa biết product thực hiện fit/no-fit, chạy query đầu, tra một field và explain-back grain/freshness/limit. Đồng thời tạo một schema drift và một example drift để kiểm consistency.",
    192: "Đóng băng catalog snapshot và năm intent tasks; ghi raw queries, clicks, rank, time, wrong selection, trust/access state và assistance. Sửa theo failure taxonomy rồi chạy lại với participants mới, giữ task difficulty và recruitment criteria.",
    193: "Chạy baseline sạch rồi tiêm riêng bốn mutations: public field thiếu mô tả, example sai, retired metric và freshness promise lệch schedule. Mỗi mutation phải fail đúng stable rule code trong required merge gate; human-review findings được tách riêng.",
    194: "Chấm bốn điều kiện bằng artifacts và observed tasks; phân loại mười câu hỏi theo repeatable lookup, bounded exploration hoặc expert investigation. Diễn tập năm support scenarios để kiểm owner, escalation, context và stop boundary.",
    195: "Chạy protocol trên synthetic/governed data với task oracle, script và scoring khóa trước. Ghi numerator/denominator, time-to-correct, assistance taxonomy, confident-wrong và deviations cho hai vòng; không suy population significance từ mẫu nhỏ.",
}

QUERIES = {
    191: ["Bốn tầng tài liệu data product trả lời bốn nhu cầu nào?", "Generated reference khác contextual explanation ra sao?", "Làm sao kiểm một bộ tài liệu bằng hành vi người lạ?"],
    192: ["Catalog coverage khác findability rate thế nào?", "Failed search terms phải được phân loại ra sao?", "Vì sao click đúng asset chưa chắc là discovery success?"],
    193: ["Bốn loại documentation tests là gì?", "Tại sao docs build xanh vẫn có thể sai?", "Những phần nào bắt buộc human review?"],
    194: ["Bốn điều kiện self-service là gì?", "Ba mức câu hỏi tự phục vụ khác nhau thế nào?", "Support boundary phải nêu trách nhiệm hai phía ra sao?"],
    195: ["Năm người phù hợp loại usability study nào?", "Bốn số đo task-based usability được định nghĩa thế nào?", "Confident-wrong outcome được ghi nhận ra sao?"],
}

NEW_SOURCES = (
    {"source_id": DI, "record_path": "1_Nguon/Web/SRC-DIATAXIS-FRAMEWORK.md", "canonical_url": "https://diataxis.fr/", "captured": "2026-10-01", "rights": "public-web-content"},
    {"source_id": DH, "record_path": "1_Nguon/Web/SRC-DATAHUB-SEARCH.md", "canonical_url": "https://docs.datahub.com/docs/how/search", "captured": "2026-10-01", "rights": "public-web-documentation"},
    {"source_id": DB, "record_path": "1_Nguon/Web/SRC-DBT-DOCUMENTATION.md", "canonical_url": "https://docs.getdbt.com/docs/build/documentation", "captured": "2026-10-01", "rights": "public-web-documentation"},
    {"source_id": GH, "record_path": "1_Nguon/Web/SRC-GITHUB-STATUS-CHECKS.md", "canonical_url": "https://docs.github.com/en/pull-requests/reference/status-checks", "captured": "2026-10-01", "rights": "public-web-documentation"},
    {"source_id": GS, "record_path": "1_Nguon/Web/SRC-GOVUK-SIMPLE-TO-USE.md", "canonical_url": "https://www.gov.uk/service-manual/service-standard/point-4-make-the-service-simple-to-use", "captured": "2026-10-01", "rights": "Open Government Licence v3.0"},
    {"source_id": GM, "record_path": "1_Nguon/Web/SRC-GOVUK-MODERATED-USABILITY-TESTING.md", "canonical_url": "https://www.gov.uk/service-manual/user-research/using-moderated-usability-testing", "captured": "2026-10-01", "rights": "Open Government Licence v3.0"},
    {"source_id": GB, "record_path": "1_Nguon/Web/SRC-GOVUK-USABILITY-BENCHMARKING.md", "canonical_url": "https://www.gov.uk/service-manual/measuring-success/usability-benchmarking-a-website-or-whole-service", "captured": "2026-10-01", "rights": "Open Government Licence v3.0"},
    {"source_id": NN, "record_path": "1_Nguon/Web/SRC-NNGROUP-USABILITY-SAMPLE-SIZE.md", "canonical_url": "https://www.nngroup.com/articles/how-many-test-users/", "captured": "2026-10-01", "rights": "public-web-content"},
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
tags: [wiki/database-systems, data-product, documentation, usability]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/{lesson.filename}
---
"""


def deep_note(lesson: Lesson) -> str:
    parts = [frontmatter(lesson), f"# {lesson.title}\n\n> [!abstract] Câu hỏi trung tâm\n> {lesson.question}\n"]
    for index, (heading, body) in enumerate(lesson.core, 1):
        parts.append(f"\n## {index}. {heading}\n\n{body}\n")
    parts.append("\n## 8. Ma trận kiểm chứng từng mệnh đề\n\nMỗi mệnh đề dưới đây cần artifact hoặc observation lưu được. Một trang tài liệu tồn tại, catalog có search box hoặc người dùng nói ‘dễ’ không tự là bằng chứng.\n")
    for index, probe in enumerate(lesson.probes, 1):
        parts.append(
            f"\n### 8.{index}. {probe}\n\n"
            f"**Mệnh đề cần kiểm.** {probe}.\n\n"
            f"**Cách kiểm.** {VERIFY[lesson.number]} Với mệnh đề này, ghi participant/task hoặc artifact version, điều kiện đầu vào, expected observation, failure signal và yếu tố làm kết luận không còn đúng.\n\n"
            "**Bằng chứng đạt.** Lưu protocol hoặc command, raw observations, numerator/denominator nếu có, exact product/docs version, reviewer và artifact hash. Nếu chưa chạy study/lab, chỉ ghi đây là protocol; không biến expected result thành kết quả quan sát.\n"
        )
    parts.append(
        """
## 9. Quy trình phản biện

1. Viết user need, task, persona, stakes và scope trước khi chọn catalog, tài liệu hoặc metric.
2. Tách source fact, curriculum synthesis, organizational policy và observation từ study.
3. Khóa task/protocol/oracle trước khi đo; mọi deviation phải được ghi.
4. Kiểm correct outcome và interpretation, không chỉ completion hoặc cảm nhận.
5. Phân loại lỗi theo cơ chế để sửa đúng lớp: metadata, docs, interface, trust, access hay skill.
6. Kiểm changed user group, changed task và degraded state trước khi khái quát.
7. Chưa có execution evidence thì giữ trạng thái `review`.

## 10. Câu hỏi tự kiểm tra

1. User task nào đang được hỗ trợ, và điều gì nằm ngoài scope?
2. Oracle nào xác định product hoặc kết quả đúng?
3. Số đo dùng denominator nào và loại invalid attempt theo rule nào?
4. Điểm nào cần automation, điểm nào bắt buộc human judgment?
5. Một kết quả nhanh nhưng sai nghĩa được phát hiện ở đâu?
6. Điều kiện nào làm kết luận từ sample hoặc catalog hiện tại không còn áp dụng?

## 11. Giới hạn và điều chưa cho phép kết luận

- Chưa chạy user study, catalog experiment, documentation CI hoặc support-boundary exercise; note mô tả protocol và expected evidence.
- Tài liệu web được kiểm ngày 2026-10-01; tính năng, giao diện, license và guidance có thể đổi.
- Bốn tầng documentation, bốn điều kiện self-service và bốn số đo của module là curriculum synthesis; không gán nguyên văn cho một nguồn.
- Cỡ mẫu nhỏ cho formative discovery không cho phép kết luận tỷ lệ toàn population hoặc statistical significance.
- Dữ liệu người tham gia, recording và screen capture cần consent, minimization, retention và access controls riêng.
- Note giữ trạng thái `review` cho tới khi chủ dự án duyệt semantic meaning.
"""
    )
    references = "\n".join(f"{index}. [[{link}]]" for index, link in enumerate(lesson.source_links, 1))
    coverage = "\n".join(
        f"| [[{link}]] | Khái niệm, mechanism hoặc study boundary liên quan | Đã đọc locator trong source record; không suy ngoài phạm vi |"
        for link in lesson.source_links
    )
    takeaways = {
        191: "Tách reader jobs, sinh reference từ source of truth và kiểm bằng fit/query/explain-back tasks.",
        192: "Đo khả năng tìm đúng product cho intent; inventory, search endpoint và click không tự là success.",
        193: "Test contract/docs behavior bằng mutations và required gate; clarity cùng interpretation vẫn cần người review.",
        194: "Self-service là bounded capability gồm find, understand, use và trust; không phải số tài khoản được cấp quyền.",
        195: "Tách formative discovery khỏi benchmark; mẫu nhỏ mô tả observations, không chứng minh population improvement.",
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

- {takeaways[lesson.number]}
- Chỉ số phải gắn task, persona, product version, protocol và denominator.
- Correct completion gồm cả kết quả và cách diễn giải đúng; confident-wrong là failure nghiêm trọng.
- Công cụ catalog, docs generator và CI cung cấp mechanism, không tự chứng minh outcome.
- Chưa chạy study hoặc lab thì artifact là tài liệu học thuật đã kiểm cấu trúc, không phải chứng nhận thực tế.
"""
    )
    return "".join(parts)


def curriculum(lesson: Lesson, knowledge: str):
    outcome, assessment, lab, pitfalls, homework, done = previous.shared.contract(lesson)
    header = f"# Phase 5: Modeling, Semantics and Analytical Product\n# Module 13: Analytical Data Product and Self-service\n# Lesson {lesson.number}: {lesson.title}"
    body = re.sub(r"^---\n.*?\n---\n", "", knowledge, flags=re.S)
    body = re.sub(r"^# .+\n+", "", body, count=1)
    note = f"{header}\n\n## Mục tiêu bài học\n\n**Năng lực cần chứng minh.** {outcome}\n\n**Điều kiện hoàn thành.** {done}\n\n{body}"
    safety = "Chỉ dùng product, fixture và accounts thử nghiệm; không thu recording hoặc dữ liệu cá nhân khi chưa có consent và retention rule. Khóa task, oracle, protocol và version trước khi đo. Lưu raw observations, invalid-attempt rules, deviations và artifact hashes; không suy population result từ sample nhỏ."
    questions = "\n".join(
        f"{index}. {question}"
        for index, question in enumerate(
            (
                "Nêu user task và oracle xác định kết quả đúng.",
                "Phân biệt tool capability với user outcome.",
                "Nêu một failure nhanh nhưng sai nghĩa và cách phát hiện.",
                "Nêu bằng chứng, giới hạn mẫu và owner cần để hoàn thành.",
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
    data["version"] = "1.0.38"
    data["updated_at"] = "2026-10-01T21:30:00+07:00"
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
