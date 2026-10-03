#!/usr/bin/env python3
"""Build source-grounded L161-L165 knowledge and curriculum notes."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path
from format_knowledge_notes import normalize_markdown
from promote_l140_l144_notes import Lesson

ROOT=Path(__file__).resolve().parents[3]
BASE11=ROOT/'Material/DE/Curriculum/Phase_05-modeling-semantics-and-analytical-product/Module_11-data-modeling-operational-analytical-and-domain'
BASE12=ROOT/'Material/DE/Curriculum/Phase_05-modeling-semantics-and-analytical-product/Module_12-semantic-layer-and-metrics-engineering'
PACK=ROOT/'Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01'
WIKI=ROOT/'Docs/Second-Brain/2_Wiki/Database-Systems'

BO='src.book.boyle-ddd-golang.1e'; ST='src.book.stopford-designing-event-driven-systems'; FW='src.web.fowler-bounded-context'
KI='src.book.kimball-ross-data-warehouse-toolkit.3e'; AD='src.book.adamson-star-schema-complete-reference'; SI='src.book.silberschatz-database-system-concepts.7e'
FD='src.book.reis-housley-fundamentals-data-engineering'; DB='src.web.dbt-semantic-models'; DV='src.web.data-vault-alliance-foundations'
BOL='SRC-BOYLE-DDD-GOLANG-1E'; STL='SRC-STOPFORD-DESIGNING-EVENT-DRIVEN-SYSTEMS'; FWL='SRC-FOWLER-BOUNDED-CONTEXT'
KIL='SRC-KIMBALL-ROSS-DW-TOOLKIT-3E'; ADL='SRC-ADAMSON-STAR-SCHEMA-COMPLETE-REFERENCE'; SIL='SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E'
FDL='SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING'; DBL='SRC-DBT-SEMANTIC-MODELS'; DVL='SRC-DATA-VAULT-ALLIANCE-FOUNDATIONS'

LESSONS=(
Lesson(161,'Lesson_161-domain-modelling-bounded-context-and-the-canonical-model-trap','Domain Modelling, Bounded Context and the Canonical Model Trap','49-domain-modelling-bounded-context-canonical-model-trap.md','wiki.data-modeling.bounded-context-contract-integration','Khi nhiều đội dùng cùng một từ với nghĩa khác nhau, làm thế nào giữ mô hình riêng của từng context nhưng vẫn tích hợp được mà không dựng một canonical model khổng lồ?',(BO,ST,FW),(BOL,STL,FWL),(
('Mô hình chỉ đúng trong một ngữ cảnh','Một domain model là tập khái niệm, quy tắc và quan hệ được dùng để giải quyết một nhóm vấn đề. Từ `customer` có thể là pháp nhân ký hợp đồng trong sales, người đang dùng sản phẩm trong product, người mở ticket trong support và đối tượng chịu kiểm soát trong risk. Các định nghĩa không nhất thiết cạnh tranh; chúng trả lời câu hỏi khác nhau. Bounded context đặt ranh giới nơi một vocabulary và model có thể nhất quán. Bên trong ranh giới, tên phải ổn định; đi qua ranh giới, nghĩa phải được dịch có chủ ý.'),
('Phát hiện xung đột ngữ nghĩa','Xung đột không chỉ là hai cột cùng tên. Cần so identity, lifecycle, cardinality, time và authority. Sales có thể nhận dạng customer bằng contract account; support bằng contact; billing bằng payer. Một context coi merge account là correction, context khác coi là event. Cùng `revenue` nhưng thời điểm ghi nhận, currency, refund và tax khác nhau sẽ tạo số khác dù schema giống hệt. Bảng so sánh phải ghi term, context, definition, identifier, valid time, owner và permitted uses.'),
('Canonical-model trap','Canonical enterprise model thường bắt đầu với mục tiêu giảm trùng lặp nhưng dễ trở thành phép hợp của mọi thuộc tính, mọi trạng thái và mọi ngoại lệ. Một thay đổi cục bộ kéo theo review toàn công ty; trường optional tăng; ownership mờ; release của một đội bị chặn bởi đội khác. Vấn đề không phải mọi canonical artifact đều sai. Một chuẩn trao đổi hẹp hoặc reference data chung có thể hữu ích. Cái bẫy là coi một model toàn cục, giàu chi tiết và thay đổi đồng bộ là điều kiện bắt buộc trước khi các miền được vận hành.'),
('Tích hợp bằng hợp đồng và mapping','Mỗi context giữ model nội bộ, rồi công bố contract nhỏ cho nhu cầu trao đổi. Contract phải nêu producer, consumer, event/entity grain, identity, schema, semantics, time, compatibility, quality, ownership và version. Mapping đứng ở boundary: `sales_contract_account_id` có thể ánh xạ sang một hay nhiều `support_contact_id`, kèm effective period và confidence nếu cần. Anti-corruption layer hoặc translation view ngăn vocabulary ngoại lai lan vào model nội bộ. Không dùng rename như biện pháp chữa xung đột; đổi tên chỉ có giá trị khi đi kèm định nghĩa và phép ánh xạ.'),
('Context map và ownership','Context map ghi quan hệ upstream/downstream, published language, conformist, customer-supplier hoặc translation boundary. Nó làm rõ đội nào có quyền thay contract, đội nào chịu migration và thời hạn deprecation. Ownership dữ liệu theo miền không có nghĩa producer tự quyết mọi thứ: consumer requirements, privacy, interoperability và governance vẫn tạo ràng buộc. Một contract không có owner, changelog, compatibility test và kênh thông báo chỉ là tài liệu tĩnh.'),
),('customer có identity khác nhau giữa sales và support','cùng tên cột không chứng minh cùng nghĩa','khác tên không chứng minh khác nghĩa','lifecycle và valid time là một phần của definition','canonical model dạng union tạo nhiều optional fields','một model toàn cục làm tăng change blast radius','published contract phải nhỏ hơn internal model','mapping phải có cardinality và effective period','anti-corruption layer bảo vệ vocabulary nội bộ','rename không thay semantic mapping','shared kernel chỉ phù hợp phạm vi nhỏ và ổn định','context boundary không bắt buộc trùng org chart','owner phải chịu compatibility và deprecation','glossary phải giữ nhiều định nghĩa theo context','integration test phải kiểm meaning chứ không chỉ schema')),
Lesson(162,'Lesson_162-late-arriving-data-early-arriving-facts-and-the-unknown-member','Late Arriving Data, Early Arriving Facts and the Unknown Member','50-late-arriving-data-early-facts-unknown-member.md','wiki.data-modeling.late-arriving-unknown-members','Làm thế nào nạp sự kiện khi dimensional context chưa có, phân biệt các loại unknown và sửa lịch sử sau đó mà không mất dòng hoặc làm sai tổng?',(KI,AD,SI),(KIL,ADL,SIL),(
('Ba ca biên khác nhau','Late-arriving fact là fact đến sau business event; nó phải lookup dimension version có hiệu lực tại event time, không phải current row lúc load. Early-arriving fact là fact đến trước dimension detail; pipeline chưa có surrogate key đúng. Late-arriving dimension change là thuộc tính/version đáng lẽ có hiệu lực trong quá khứ nhưng chỉ biết sau này. Ba trường hợp dùng cùng chữ “muộn” nhưng khác thao tác: insert fact vào lịch sử, dùng placeholder/inferred member, hoặc tách interval và relink/restatement.'),
('Không loại bỏ fact vì lookup thất bại','Inner join lookup rồi bỏ unmatched row làm control total thấp hơn source mà pipeline vẫn báo thành công. Thiết kế an toàn giữ fact bằng special member hoặc quarantine có ledger, tùy contract; mọi row phải có disposition. Reconciliation tối thiểu gồm source count, accepted count, quarantined count, rejected count, duplicate count và phương trình tổng. Với amount còn phải đối soát theo currency, business date và batch, không chỉ grand total.'),
('Unknown không phải một nghĩa','`Unknown` nên được tách ít nhất ba trạng thái: `not-yet-known` khi dimension dự kiến sẽ tới; `not-applicable` khi quan hệ không tồn tại theo nghiệp vụ; `invalid/error` khi source key vi phạm contract hoặc không map được. Ba rows có surrogate keys ổn định và labels rõ. Gộp chúng làm mất khả năng đo backlog enrichment, data-quality defect và optional relationship. NULL foreign key cũng làm fact biến mất trong inner join và buộc consumer tự hiểu three-valued logic.'),
('Inferred member và sửa liên kết','Nếu business key đáng tin, pipeline có thể tạo inferred dimension row tối thiểu, giữ surrogate key, rồi bổ sung attributes khi dimension đến. Nếu chưa xác định được identity, dùng shared not-yet-known member và lưu source key/event identity để relink. Khi late SCD Type 2 change đến, chèn version đúng effective interval, sửa boundaries không overlap và cập nhật fact foreign keys thuộc interval theo restatement policy. Rerun phải idempotent; không tạo thêm inferred member hoặc lặp correction.'),
('Hai thời gian và chính sách công bố lại','Event/effective time quyết định dimension version nào đúng về nghiệp vụ; load/system time ghi lúc warehouse biết. Báo cáo lịch sử có thể restate theo sự thật mới, đóng băng theo số đã công bố, hoặc cung cấp hai view original/revised. Không có lựa chọn mặc định đúng cho mọi miền. Policy phải nêu cutoff, accounting period, materiality, approver, consumer notification và lineage từ correction tới outputs bị ảnh hưởng.'),
),('late fact lookup dùng event time','early fact không được bị inner join làm mất','mọi source row phải có disposition','not-yet-known khác not-applicable','invalid khác optional relationship','NULL foreign key làm join semantics khó kiểm soát','inferred member cần stable business key','shared unknown member cần giữ source identity để relink','late SCD2 change có thể tách interval','SCD intervals không được overlap','fact relink phải theo effective interval','rerun không sinh placeholder trùng','row và amount reconciliation đều cần thiết','original và revised reports cần version','quarantine không được trở thành nơi bỏ quên dữ liệu')),
Lesson(163,'Lesson_163-modelling-for-handover-what-the-consumer-needs','Modelling for Handover - What the Consumer Needs','51-modelling-for-handover-consumer-needs.md','wiki.data-modeling.consumer-handover','Một người chưa tham gia thiết kế cần những bằng chứng nào để dùng mô hình đúng, tự phát hiện giới hạn và vận hành mà không phụ thuộc trí nhớ của tác giả?',(FD,DB,ST),(FDL,DBL,STL),(
('Bàn giao là phép thử khả dụng','Mô hình không hoàn thành khi tác giả chạy được query; nó hoàn thành khi consumer độc lập có thể tìm đúng bảng, hiểu một row, chọn đúng field, tính đúng measure và biết khi nào không được kết luận. Handover test vì thế đo hành vi thật: giao dataset, tài liệu và ba câu hỏi cho người chưa xem model; không coaching trong lúc làm. Câu hỏi họ phải hỏi, query sai và interpretation sai đều là defects có thể sửa.'),
('Phần một và hai: grain, keys, measures','Phần một ghi purpose, scope, grain, business keys, time/cutoff và quan hệ chính. Một câu grain phải đủ để người nhận dự đoán row count và join cardinality. Phần hai là metric dictionary: tên, business question, formula, numerator/denominator, filters, grouping, unit/currency, additivity, null/zero policy, owner và version. SQL minh họa không thay definition; definition không có executable test cũng khó giữ đúng khi model đổi.'),
('Phần ba và bốn: dimensions, freshness, quality','Phần ba mô tả dimensions/attributes bằng ngôn ngữ nghiệp vụ, values, hierarchy, role, slowly-changing behavior và unknown categories. Không chép tên cột source thành “định nghĩa”. Phần bốn ghi source lineage, refresh cadence, watermark, expected freshness, completeness, reconciliation, known incidents và support owner. “Cập nhật hằng ngày” chưa đủ nếu không có timezone, cutoff và cách xử lý late data.'),
('Phần năm và sáu: examples, limits','Phần năm có ít nhất ba query mẫu gắn business questions, expected grain/output và anti-example thường sai. Phần sáu ghi interpretation limits: coverage population, excluded events, survivorship bias, attribution boundary, non-causal nature, restatement policy và những câu hỏi dataset không trả lời. Đây không phải disclaimer trang trí; nó chặn người dùng biến sự tương quan thành nguyên nhân hoặc dùng snapshot để suy event không được capture.'),
('Từ tài liệu tĩnh tới hợp đồng vận hành','Bộ sáu phần phải version cùng model, có owner, changelog, deprecation notice và machine-checkable elements nơi phù hợp. Catalog/semantic tooling giúp discovery nhưng không tự sinh đúng business meaning. Handover log phải ghi task, time, câu hỏi, lỗi, sửa đổi và retest. Đạt 2/3 chỉ là ngưỡng bài học; production handover còn cần access, runbook, incident path, privacy và consumer sign-off.'),
),('grain phải giúp dự đoán row cardinality','metric formula phải nêu filters và time boundary','attribute definition không được chép tên cột','unknown categories phải được giải thích','freshness cần timezone và cutoff','quality cần control totals và owner','sample query phải ghi expected output grain','anti-example giúp nhận diện query sai','interpretation limits phải nêu population coverage','correlation không được viết thành causality','lineage phải đi tới source và transform','documentation version phải đi cùng model version','handover test không coaching người nhận','mọi câu hỏi phát sinh trở thành defect log','catalog tool không thay semantic ownership')),
Lesson(164,'Lesson_164-modelling-project-four-models-one-decision-matrix','Modelling Project - Four Models, One Decision Matrix','52-modelling-project-four-models-decision-matrix.md','wiki.data-modeling.four-model-decision-matrix','Làm thế nào so bốn mô hình trên cùng domain bằng bằng chứng tương đương, thay vì chọn theo sở thích hoặc một benchmark không cùng điều kiện?',(KI,AD,FD),(KIL,ADL,FDL),(
('Khóa bài toán trước khi dựng mô hình','Cả bốn phương án phải dùng cùng source snapshot, business question, cutoff, currency, privacy rule và expected answer. Ghi domain, workload, volume, concurrency, change frequency, latency/freshness target và team capability. Nếu mỗi mô hình trả lời một câu khác nhau thì ma trận không có giá trị. Ground truth cần được tính từ atomic source bằng một oracle query độc lập với bốn implementation.'),
('Bốn mô hình và grain','Operational normalized model ưu tiên transaction integrity, dependencies và write behavior. Dimensional model tuyên bố fact grain, conformed dimensions, SCD2 và aggregation semantics. Data Vault sketch xác định stable business keys, relationship grain, Satellites và delivery mart; bài không tuyên bố triển khai DV2 đầy đủ. Wide table chọn consumption grain, xử lý one-to-many/nested fields và duplicate measures. Mọi event table đều phải có một câu grain và test key/cardinality.'),
('Bảo toàn nghĩa trước khi đo hiệu năng','Chạy cùng query suite trên bốn models và đối chiếu result set sau khi normalize ordering/types/precision. Chênh lệch phải được giải thích bằng semantics đã công bố, không được bỏ qua. Bắt buộc có SCD2 case, early fact, ba special-member meanings và late correction. Một model nhanh nhưng bỏ unmatched facts hoặc dùng current dimension cho history là không hợp lệ, không được đưa vào ranking performance.'),
('Ma trận bốn nhân bốn có số','Bốn trục là correctness/traceability, usability, performance/cost và change/operations. Mỗi ô cần số đo hoặc ước lượng có công thức: mismatched rows/control-total delta; task success/time/error rate; p50/p95 latency, bytes scanned, storage, refresh; artifacts touched, migration hours, failed-change recovery. “Nhanh”, “dễ”, “linh hoạt” không phải evidence. Với ước lượng, ghi range, assumptions và confidence thay vì số giả chính xác.'),
('Khuyến nghị và điều kiện đảo ngược','Khuyến nghị phải có bối cảnh, lựa chọn, evidence, trade-off chấp nhận, rejected alternatives và ba trigger làm quyết định đổi: workload/concurrency vượt ngưỡng, source/domain volatility tăng, hoặc team/tool/governance thay đổi. Không nhất thiết một model thắng toàn bộ. Kiến trúc thực tế có thể dùng normalized source, Raw Vault, dimensional mart và semantic layer nối tiếp; ma trận phải chỉ rõ layer đang so, tránh biến patterns bổ sung thành đối thủ tuyệt đối.'),
),('bốn models phải dùng cùng source snapshot','business question và cutoff phải giống nhau','oracle query phải độc lập implementation','mỗi event table có declared grain','SCD2 behavior phải được kiểm','early fact không được làm mất row','ba unknown meanings phải còn queryable','result sets phải semantic-diff trước benchmark','p50 p95 cần cùng workload và warm-up','storage phải tính cả refresh artifacts','usability phải đo bằng consumer task','changeability phải đếm blast radius','ước lượng cần assumptions và confidence','recommendation phải có ba reversal triggers','patterns ở các layers khác nhau có thể cùng tồn tại')),
Lesson(165,'Lesson_165-the-layers-that-must-be-distinguished','The Layers That Must Be Distinguished','53-layers-physical-mart-semantic-metric-consumption.md','wiki.semantic-layer.five-layer-boundary','Bảng vật lý, mart, semantic model, metric contract và công cụ tiêu thụ khác nhau ở artifact, trách nhiệm và failure mode nào?',(FD,DB,SI),(FDL,DBL,SIL),(
('Tại sao phải tách năm tầng','Một dashboard hiển thị revenue không cho biết logic nằm trong SQL view, mart, BI calculated field hay semantic service. Khi cùng tên được định nghĩa ở nhiều nơi, sửa filter/refund/currency ở một chỗ không cập nhật các chỗ còn lại. Tách tầng không nhằm tăng số công cụ; nó tạo ranh giới để biết dữ liệu nằm đâu, structure được chuẩn bị ở đâu, nghĩa được khai báo ở đâu, metric được quản trị ở đâu và người dùng đặt câu hỏi ở đâu.'),
('Tầng một: bảng vật lý','Physical table/file/view là nơi rows và columns tồn tại trên engine cụ thể. Nó có schema, types, keys, partition, clustering, retention, permissions và storage format. Một bảng có cột `revenue` không tự biến thành metric contract; cột có thể là atomic amount, allocated amount hay pre-aggregated number. Physical optimization có thể đổi mà business meaning không đổi, miễn lineage và contract được bảo toàn.'),
('Tầng hai: mô hình mart','Mart tổ chức physical artifacts cho một domain/use case: facts, dimensions, wide product tables hoặc aggregate tables. Nó quyết định grain, joins, conformance, history và exposure boundary. Mart có dữ liệu, khác semantic model là metadata/declarations về cách consumer hiểu và kết nối model. Một mart tốt vẫn có thể bị dùng sai nếu metric filter, time grain và additivity không được quản trị.'),
('Tầng ba và bốn: semantic model, metric contract','Semantic model khai báo entities, dimensions, measures, relationships, time dimensions và join behavior trên marts. Metric contract đặt tên cho phép tính: expression, source measure, entity/grain, filters, time window, aggregation, unit, null/late-data policy, owner và version. Tùy sản phẩm, metric có thể nằm trong cùng YAML/repository với semantic model, nhưng hai trách nhiệm vẫn phân biệt được. “Một nơi” nghĩa một governed source of truth có version và API/build path, không phải một file bất biến.'),
('Tầng năm: công cụ tiêu thụ','BI, notebook, spreadsheet, reverse-ETL app hoặc API là nơi người dùng hỏi và trình bày. Tool có thể giữ layout, chart calculation chỉ dành cho hiển thị và parameters, nhưng shared business metric không nên được chép lại ở từng workbook/query. Ba triệu chứng phân tán là cùng tên cho nhiều số, sửa định nghĩa phải tìm nhiều assets, và không truy ra owner/version. Migration bắt đầu bằng inventory definitions, semantic diff, chọn canonical contract, redirect consumers rồi deprecate duplicates.'),
),('physical table có rows và engine-specific schema','mart quyết định grain và prepared joins','semantic model là declaration không phải bản sao dữ liệu','entity khác dimension và measure','metric contract phải có formula và filters','time grain và timezone thuộc metric semantics','semantic model và metric có thể cùng repository nhưng khác trách nhiệm','consumption tool không nên sở hữu shared metric','calculation chỉ cho visual phải được phân loại riêng','cùng metric name nhiều numbers là drift symptom','definition inventory phải tìm SQL BI và notebook','canonical source cần owner và version','redirect consumers phải có equivalence test','tool installation không tạo semantic governance','năm tầng là logical responsibilities không bắt buộc năm products')),
)

MODULE={161:(11,'Data Modeling - Operational, Analytical and Domain',BASE11),162:(11,'Data Modeling - Operational, Analytical and Domain',BASE11),163:(11,'Data Modeling - Operational, Analytical and Domain',BASE11),164:(11,'Data Modeling - Operational, Analytical and Domain',BASE11),165:(12,'Semantic Layer and Metrics Engineering',BASE12)}

VERIFY={
161:'Dùng ba context sales, support và billing. Lập bảng term–identity–lifecycle–time–owner; viết contract trao đổi và mapping cardinality/effective period. Thử một schema change cục bộ để đo số artifacts và teams bị ảnh hưởng.',
162:'Dựng fixture gồm normal fact, late fact, early fact, optional relationship, invalid key và late SCD2 change. Lưu ledger disposition; kiểm count/amount equation, no-overlap, relink theo effective time và rerun idempotency.',
163:'Giao model, bộ tài liệu và ba câu hỏi cho người chưa tham gia. Không coaching. Thu query, câu trả lời, thời gian, câu hỏi và lỗi; sửa đúng phần tài liệu rồi retest với cùng rubric.',
164:'Khóa một source snapshot và oracle result; dựng bốn models rồi chạy cùng correctness suite trước benchmark. Lưu semantic diff, query plans, latency, bytes/storage, refresh, consumer-task results và change-impact counts.',
165:'Lấy ba kiến trúc, inventory mọi physical object, mart, semantic declaration, metric definition và consumer. Chọn một metric, đếm definitions, semantic-diff chúng và chứng minh canonical contract có owner/version cùng consumers được redirect.',
}

def fm(x):
    sources='\n'.join(f'  - {s}' for s in x.sources)
    tags='semantic-layer, module-12' if x.number==165 else 'data-modeling, module-11'
    return f'''---
note_id: {x.note_id}
note_type: concept-deep-dive
status: review
language: vi
created: 2026-10-01
last_verified: 2026-10-01
editorial_pass: humanized-v1
primary_question: {x.question}
source_ids:
{sources}
aliases: [{x.title}]
tags: [wiki/database-systems, {tags}]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/{x.filename}
---
'''

def deep_note(x):
    parts=[fm(x),f'# {x.title}\n\n> [!abstract] Câu hỏi trung tâm\n> {x.question}\n']
    for i,(heading,body) in enumerate(x.core,1):
        parts.append(f'\n## {i}. {heading}\n\n{body}\n')
    parts.append('\n## 6. Ma trận kiểm chứng từng mệnh đề\n\nMỗi mệnh đề dưới đây cần một dữ liệu phản ví dụ, một invariant và một bằng chứng chạy lại được. Tên pattern, sơ đồ hoặc một query chạy thành công không đủ để xác nhận đúng ngữ nghĩa.\n')
    for i,probe in enumerate(x.probes,1):
        parts.append(f'''\n### 6.{i}. {probe}\n\n**Mệnh đề cần kiểm.** {probe}.\n\n**Cách kiểm.** {VERIFY[x.number]} Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.\n\n**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.\n''')
    parts.append('''\n## 7. Quy trình làm bài và phản biện\n\n1. Viết business question, phạm vi, vocabulary, grain, identity và time semantics trước khi chọn bảng hoặc công cụ.\n2. Gắn từng định nghĩa với context, owner, version và canonical artifact; không dùng tên cột thay nghĩa.\n3. Tách nội dung lấy trực tiếp từ nguồn, quyết định thiết kế và phần tổng hợp của giáo trình.\n4. Dựng normal case cùng các ca biên có thể tạo kết quả hợp lệ cú pháp nhưng sai nghĩa.\n5. Đo row count, distinct keys, unmatched/disposition counts, control totals và semantic diff trước–sau transform.\n6. Thử replay, late correction hoặc schema/contract change phù hợp với bài; ghi change blast radius.\n7. Giữ failed run, assumptions và limitation trong hồ sơ. Chúng cho người khác khả năng bác bỏ kết luận.\n\n## 8. Câu hỏi tự kiểm tra\n\n1. Artifact nào giữ dữ liệu, artifact nào giữ nghĩa và ai có quyền thay đổi?\n2. Một row/term/metric đại diện điều gì trong context và khoảng thời gian nào?\n3. Ca biên nào làm con số sai nhưng pipeline hoặc dashboard vẫn xanh?\n4. Phép kiểm nào xác nhận cấu trúc; phần nào vẫn cần owner xác nhận?\n5. Khi contract thay đổi, consumer nào bị ảnh hưởng và migration được kiểm ra sao?\n6. Phần nào của note là source fact, phần nào là synthesis có điều kiện?\n\n## 9. Giới hạn và điều chưa cho phép kết luận\n\n- Chưa chạy các lab, handover test hoặc benchmark mô tả trong note; chúng là giao thức kiểm chứng, không phải số đo đã thu.\n- Nguồn sách cung cấp khái niệm và patterns; lựa chọn cho một doanh nghiệp còn phụ thuộc domain, engine, workload, policy và owner.\n- Tài liệu web được kiểm ngày 2026-10-01 và có thể thay đổi theo phiên bản sản phẩm.\n- Không suy một tool, model hay kiến trúc là chuẩn duy nhất từ ví dụ của nguồn.\n- Không có owner review thì trạng thái vẫn là `review`, chưa phải policy được phê duyệt.\n''')
    refs='\n'.join(f'{i}. [[{s}]]' for i,s in enumerate(x.source_links,1))
    coverage='\n'.join(f'| [[{s}]] | Khái niệm, cơ chế và giới hạn liên quan trực tiếp | Đã đọc phạm vi có locator; không suy ngoài phạm vi |' for s in x.source_links)
    parts.append(f'''\n## Reference\n\n{refs}\n\n## Source coverage\n\n| Source slice | Nội dung sử dụng | Trạng thái |\n|---|---|---|\n{coverage}\n\n## Key takeaways\n\n- Bắt đầu từ nghĩa, context, grain, identity, time và ownership; schema và công cụ là phần triển khai.\n- Mọi trường hợp unmatched, unknown hoặc duplicated definition phải có trạng thái quan sát được, không được mất trong im lặng.\n- Tài liệu chỉ đạt khi một người khác dùng đúng mà không dựa vào trí nhớ của tác giả.\n- So sánh mô hình chỉ hợp lệ sau khi kết quả ngữ nghĩa đã được đối chiếu trên cùng dữ liệu và cutoff.\n- Chưa chạy phép kiểm thì note là tài liệu học thuật có truy nguồn, không phải chứng nhận production.\n''')
    return ''.join(parts)

def folder(x): return MODULE[x.number][2]/x.directory
def field(text,name):
    match=re.search(rf'(?m)^\*\*{re.escape(name)}\.\*\*\s*(.+)$',text)
    if not match: raise ValueError(name)
    return match.group(1).strip()
def section(text,heading):
    match=re.search(rf'(?ms)^## {re.escape(heading)}\n\n(.*?)(?=^## |\Z)',text)
    if not match: raise ValueError(heading)
    return match.group(1).strip()
def contract(x):
    note=(folder(x)/'note.md').read_text()
    after=(folder(x)/'after-note.md').read_text()
    if '**Outcome.**' in note:
        return tuple(field(note,k) for k in ('Outcome','Đánh giá','Lab','Pitfalls','Self-study (2,4 giờ)','Done when'))
    return (
        field(section(note,'Mục tiêu bài học'),'Năng lực cần chứng minh'),
        field(section(after,'Tiêu chí hoàn thành'),'Cách đánh giá'),
        field(section(after,'Thực hành'),'Nhiệm vụ'),
        field(section(after,'Bài làm sau buổi học'),'Lỗi cần chủ động loại trừ'),
        field(section(after,'Bài làm sau buổi học'),'Nhiệm vụ'),
        field(section(note,'Mục tiêu bài học'),'Điều kiện hoàn thành'),
    )
def curriculum(x,knowledge):
    outcome,assessment,lab,pitfalls,homework,done=contract(x)
    module_no,module_title,_=MODULE[x.number]
    header=f'# Phase 5: Modeling, Semantics and Analytical Product\n# Module {module_no}: {module_title}\n# Lesson {x.number}: {x.title}'
    body=re.sub(r'^---\n.*?\n---\n','',knowledge,flags=re.S)
    body=re.sub(r'^# .+\n+','',body,count=1)
    note=f'{header}\n\n## Mục tiêu bài học\n\n**Năng lực cần chứng minh.** {outcome}\n\n**Điều kiện hoàn thành.** {done}\n\n{body}'
    safety='Chỉ chạy fixture, profiling, reconciliation, semantic diff hoặc benchmark trên dataset thử nghiệm/versioned snapshot. Không sửa production model, metric, identity mapping hay history để minh họa. Lưu input, assumptions, query/test, raw output và diff trước–sau.'
    questions='\n'.join(f'{i}. {q}' for i,q in enumerate(('Phát biểu context/grain và invariant chính.','Nêu phản ví dụ cho kết quả hợp lệ cú pháp nhưng sai nghĩa.','Chỉ ra source fact, quyết định thiết kế và curriculum synthesis.','Đề xuất phép kiểm tái chạy được cùng bằng chứng cần lưu.'),1))
    after=f'{header}\n\n## Thực hành\n\n**Nhiệm vụ.** {lab}\n\n{safety}\n\n## Kiểm tra cuối bài\n\n{questions}\n\n## Tiêu chí hoàn thành\n\n**Cách đánh giá.** {assessment}\n\n**Điều kiện đạt.** {done}\n\n## Bài làm sau buổi học\n\n**Nhiệm vụ.** {homework}\n\n**Lỗi cần chủ động loại trừ.** {pitfalls}\n\n## Reference\n\n- Knowledge note: `{(PACK/x.filename).relative_to(ROOT)}`\n- Nội dung học thuật: `note.md` cùng thư mục.\n'
    return note,after

NEW_SOURCES=(
 {'source_id':ST,'record_path':'1_Nguon/Books/SRC-STOPFORD-DESIGNING-EVENT-DRIVEN-SYSTEMS.md','canonical_path':'/home/kina2711/PROJECT/data-trainer/Material/DE/Reference/Library/knowledge/System-Design/20220311-EB-Designing_Event_Driven_Systems.pdf','sha256':'c9bb3e324d93529a25563fd25447a11549dcca8e61d36b9665fff0c8de2cdd41','rights':'copyrighted-private-owner-provided'},
 {'source_id':FD,'record_path':'1_Nguon/Books/SRC-REIS-HOUSLEY-FUNDAMENTALS-DATA-ENGINEERING.md','canonical_path':'/home/kina2711/PROJECT/data-trainer/Material/Reference_temp/Fundamentals_of_Data_Engineering_-_Joe_Reis.pdf','sha256':'0189abd30d24db8faf9be5d195f7a9da60973a5f38f95497fbede80562c96eaf','rights':'copyrighted-private-owner-provided'},
 {'source_id':FW,'record_path':'1_Nguon/Web/SRC-FOWLER-BOUNDED-CONTEXT.md','canonical_url':'https://www.martinfowler.com/bliki/BoundedContext.html','captured':'2026-10-01','rights':'public-web-content'},
 {'source_id':DB,'record_path':'1_Nguon/Web/SRC-DBT-SEMANTIC-MODELS.md','canonical_url':'https://docs.getdbt.com/docs/build/semantic-models','captured':'2026-10-01','rights':'public-web-documentation'},
)
QUERIES={
161:['Bounded context giải quyết xung đột từ vựng thế nào?','Canonical model trap tạo change blast radius ra sao?','Contract integration cần mapping nào?'],
162:['Early-arriving fact khác late-arriving fact thế nào?','Ba loại unknown member là gì?','Late SCD2 change phải relink fact ra sao?'],
163:['Bộ tài liệu bàn giao sáu phần gồm gì?','Handover usability test chạy thế nào?','Interpretation limits ngăn sai lầm nào?'],
164:['Bốn mô hình được so công bằng bằng cách nào?','Ma trận quyết định bốn nhân bốn đo gì?','Điều kiện đảo ngược khuyến nghị là gì?'],
165:['Năm tầng physical mart semantic metric consumption khác nhau thế nào?','Metric definition nên nằm ở đâu?','Dấu hiệu metric definitions bị phân tán là gì?'],
}
def update_manifest(check=False):
    path=ROOT/'Docs/Second-Brain/second-brain-manifest.json'; data=json.loads(path.read_text())
    existing={s['source_id'] for s in data['source_registry']}; data['source_registry'].extend(s for s in NEW_SOURCES if s['source_id'] not in existing)
    ids={x.note_id for x in LESSONS}; data['note_registry']=[n for n in data['note_registry'] if n.get('note_id') not in ids]; data['retrieval_test_set']=[q for q in data['retrieval_test_set'] if q.get('expected_note_id') not in ids]
    for x in LESSONS:
        data['note_registry'].append({'note_id':x.note_id,'path':f'2_Wiki/Database-Systems/{x.title}.md','status':'review','source_ids':list(x.sources),'last_verified':'2026-10-01'})
        data['retrieval_test_set'].extend({'query':q,'expected_note_id':x.note_id} for q in QUERIES[x.number])
    data['version']='1.0.32'; data['updated_at']='2026-10-01T23:40:00+07:00'; data['layers']['1_Nguon']['source_count']=len(data['source_registry']); data['layers']['2_Wiki']['note_count']=len(data['note_registry'])
    expected=json.dumps(data,ensure_ascii=False,indent=2)+'\n'
    if check: return [] if path.read_text()==expected else [str(path.relative_to(ROOT))]
    path.write_text(expected); return []
def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--check',action='store_true'); args=parser.parse_args(); stale=[]
    for x in LESSONS:
        knowledge=normalize_markdown(deep_note(x)); note,after=curriculum(x,knowledge)
        for path,content in ((PACK/x.filename,knowledge),(WIKI/(x.title+'.md'),knowledge),(folder(x)/'note.md',note),(folder(x)/'after-note.md',after)):
            if args.check:
                if not path.exists() or path.read_text()!=content: stale.append(str(path.relative_to(ROOT)))
            else: path.write_text(content)
    stale.extend(update_manifest(args.check))
    if stale: print('STALE\n'+'\n'.join(stale)); return 1
    print(('checked' if args.check else 'written')+f'={len(LESSONS)*4} stale=0'); return 0
if __name__=='__main__': raise SystemExit(main())
