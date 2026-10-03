#!/usr/bin/env python3
"""Build source-grounded L156-L160 knowledge and curriculum notes."""
from __future__ import annotations
import argparse, json, re
from promote_l150_l155_notes import Lesson, ROOT, BASE, PACK, WIKI, curriculum
from format_knowledge_notes import normalize_markdown

K='src.book.kimball-ross-data-warehouse-toolkit.3e'
A='src.book.adamson-star-schema-complete-reference'
S='src.book.silberschatz-database-system-concepts.7e'
M='src.web.microsoft-sql-server-temporal-tables'
G='src.web.google-bigquery-denormalization'
V='src.web.data-vault-alliance-foundations'
B='src.web.datavault-builder-main-documentation'
KL='SRC-KIMBALL-ROSS-DW-TOOLKIT-3E'; AL='SRC-ADAMSON-STAR-SCHEMA-COMPLETE-REFERENCE'; SL='SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E'
ML='SRC-MICROSOFT-SQL-SERVER-TEMPORAL-TABLES'; GL='SRC-GOOGLE-BIGQUERY-DENORMALIZATION'; VL='SRC-DATA-VAULT-ALLIANCE-FOUNDATIONS'; BL='SRC-DATAVAULT-BUILDER-MAIN-DOCUMENTATION'

LESSONS=(
Lesson(156,'Lesson_156-dimension-patterns-role-playing-junk-degenerate-and-bridge','Dimension patterns - role-playing, junk, degenerate and bridge','44-dimension-patterns-role-playing-junk-degenerate-bridge.md','wiki.data-modeling.dimension-patterns','Role-playing, junk, degenerate dimension và bridge giải bốn vấn đề khác nhau; làm sao nhận đúng mẫu và không nhân measures khi join?',(K,A,S),(KL,AL,SL),(
('Role-playing dimension','Một physical dimension được dùng qua nhiều quan hệ ngữ nghĩa, chẳng hạn order date, requested date và ship date. Mỗi role cần alias/view và tên cột rõ nghĩa; cùng date key không có nghĩa cùng business event. Không nhân bản dimension chỉ để đổi tên, vì như vậy làm tách governance và fiscal-calendar logic.'),
('Degenerate dimension','Mã giao dịch như order number có thể nằm ngay trong fact khi không còn descriptive attributes tạo thành một dimension riêng. Nó vẫn hữu ích cho grouping, drill-through và đối chiếu với source. Degenerate không phải giấy phép nhét status code khó hiểu vào fact; code có nhãn, nhóm hoặc policy cần dimension.'),
('Junk dimension','Các flag/indicator low-cardinality, tương đối độc lập, có thể gom thành một dimension nhỏ thay vì tăng độ rộng fact hoặc tạo hàng chục dimensions. Phải ước lượng Cartesian combinations và chỉ materialize combinations thực tế nếu không gian lớn. Không gom các thuộc tính có ownership, rate-of-change hay semantics khác nhau chỉ vì chúng ít giá trị.'),
('Bridge','Bridge biểu diễn quan hệ many-to-many, multivalued dimension hoặc hierarchy path. Một fact có thể nối nhiều members, vì vậy SUM sau join sẽ nhân measure nếu không có allocation weight hoặc impact-only contract. Weight phải có hiệu lực theo thời gian và tổng bằng 1 trong phạm vi allocation; DISTINCT không sửa được sai semantics.'),
('Chọn mẫu bằng failure mode','Role-playing giải bài toán nhiều vai của cùng domain; junk giải low-cardinality flags; degenerate giữ transaction identifier không có attributes; bridge giải multiplicity. Bốn mẫu không thay thế nhau. Review phải viết input/output grain, cardinality và control total trước khi chạy truy vấn.'),
),('order date và ship date phải có role names riêng','một physical date dimension có thể phục vụ nhiều role','order number không có attributes là degenerate dimension','status code có nhãn không nên bị coi là degenerate','junk dimension phù hợp low-cardinality flags','Cartesian combinations phải được ước lượng','bridge làm tăng row count sau join','allocation weights phải có policy và hiệu lực','impact-only query không được giả vờ là allocation','DISTINCT không sửa double counting','hierarchy bridge cần zero-length path khi contract yêu cầu','bridge history cần valid interval','nhiều parent cần weighting hoặc non-additive interpretation','mỗi role cần semantic label','control total phải khớp trước và sau bridge')),
Lesson(157,'Lesson_157-slowly-changing-dimensions-type-0-to-type-6','Slowly changing dimensions, type 0 to type 6','45-slowly-changing-dimensions-type-0-to-type-6.md','wiki.data-modeling.scd-types','Chọn và cài SCD response theo câu hỏi lịch sử như thế nào, đặc biệt khi late-arriving change, correction và hai cách nhìn cùng tồn tại?',(K,A,S),(KL,AL,SL),(
('Type 0, 1 và ranh giới correction','Type 0 giữ nguyên giá trị ban đầu; Type 1 overwrite và không giữ prior value. Type 1 hợp với sửa lỗi hoặc thuộc tính không cần lịch sử, nhưng sẽ restate toàn bộ facts cũ theo giá trị mới khi join. Quyết định correction hay business change thuộc data contract, không thể suy chỉ từ việc source gửi UPDATE.'),
('Type 2 và hai bất biến','Type 2 thêm version row với surrogate key mới; fact mới trỏ version có hiệu lực, fact cũ không rewrite. Hai bất biến tối thiểu là không overlap valid interval cho cùng business key và tối đa một current row. Half-open interval [from,to) giúp hai version kề nhau không overlap. Cần transaction/merge semantics để close old và insert new một cách atomic.'),
('Type 3 và alternate reality','Type 3 thêm cột prior/alternate value trên cùng row, cho phép xem facts theo cả cấu trúc cũ và mới trong một số change hữu hạn. Nó không lưu chuỗi vô hạn và phải đặt tên cột rõ current/prior/as-was/as-is. Dùng cho reorganization cần hai cách roll-up, không phải thay Type 2 cho mọi change.'),
('Type 4–6 và cảnh báo taxonomy','Sau ba type cơ bản, cách đánh số không hoàn toàn thống nhất giữa tài liệu. Trong hệ Kimball hiện đại, Type 4 thường là mini-dimension cho rapidly changing attributes; Type 5 ghép mini-dimension với current profile; Type 6 ghép Type 1+2+3 để hỗ trợ as-was và as-is. Thiết kế phải mô tả behavior thay vì chỉ ghi con số type.'),
('Late arriving, idempotency và fact lookup','Change đến muộn có thể phải chèn version giữa hai interval, tách interval cũ và xác định facts cần restate theo policy. Hash-diff chỉ phát hiện row khác; nó không quyết định attribute nào Type 1/2. Rerun cùng batch phải không sinh thêm version; lookup surrogate key phải dùng business key cùng effective time/cutoff.'),
),('Type 0 giữ original value','Type 1 overwrite làm lịch sử facts mang current label','Type 2 tạo surrogate key mới','Type 2 không được overlap intervals','mỗi business key có tối đa một current row','Type 3 chỉ giữ số alternate values hữu hạn','Type 4–6 phải mô tả behavior vì taxonomy có thể khác','mini-dimension tách rapidly changing profile','Type 6 hỗ trợ as-was và as-is với chi phí cao hơn','late change có thể tách interval','correction khác business change','hash-diff không thay attribute policy','rerun không được sinh version trùng','fact lookup cần effective time','report Type 1 và Type 2 phải định lượng chênh lệch')),
Lesson(158,'Lesson_158-valid-time-system-time-corrections-and-restatement','Valid time, system time, corrections and restatement','46-valid-time-system-time-corrections-restatement.md','wiki.data-modeling.bitemporal-corrections','Valid time và system time trả lời hai câu hỏi nào, và correction/restatement phải được quản trị ra sao để không viết lại lịch sử đã công bố một cách vô hình?',(S,M,K),(SL,ML,KL),(
('Hai trục, hai câu hỏi','Valid/effective time nói fact đúng trong thế giới nghiệp vụ khi nào. System/transaction time nói database biết hoặc lưu phiên bản khi nào. Bitemporal data kết hợp hai trục để trả lời both what was true then và what did we believe/report then. Tên `ValidFrom` do engine sinh trong SQL Server temporal table thực ra biểu diễn system period; tên cột không thay semantics.'),
('Khoảng thời gian và bất biến','Dùng half-open interval [start,end) để hai version kề nhau không overlap. Cùng business key không được có hai valid intervals chồng nếu domain yêu cầu single state. Primary key thêm start/end vẫn không bắt overlap; cần exclusion/temporal constraint hoặc validation. Temporal join lấy phần giao interval và loại cặp không giao.'),
('Biết muộn và sửa sai','Late-known fact có valid time cũ nhưng system time mới: hệ thống vừa mới biết một điều đã đúng trước đó. Correction thay mệnh đề do prior record sai; business change tạo state mới. Cả hai có thể cùng valid interval pattern nhưng khác reason, approval và cách đối xử số đã công bố.'),
('Restatement policy','Restatement là quyết định governance: số lịch sử được tái tính, đóng băng hay công bố song song original/revised. Policy phải chỉ ra materiality, accounting/report period, consumer notification, owner phê duyệt, version label và reconciliation. UPDATE đúng kỹ thuật không đủ thẩm quyền đổi dashboard hoặc regulatory report đã phát hành.'),
('Truy vấn và provenance','As-of-valid truy state nghiệp vụ tại thời điểm V theo knowledge hiện nay; as-of-system truy database view tại thời điểm S. Bitemporal query cố định cả V và S. Mỗi correction cần reason code, source record, load/batch ID, approver và links tới output versions bị ảnh hưởng. Retention của history table có thể giới hạn khả năng trả lời.'),
),('valid time mô tả khi fact đúng trong domain','system time mô tả khi database ghi nhận','late-known fact có valid time cũ và system time mới','correction khác business change','half-open interval cho phép hai version kề nhau','primary key gồm endpoints không tự chặn overlap','temporal join dùng intersection','SQL Server system-versioned period không tự là business-valid time','as-of-valid khác as-of-system','bitemporal query cố định hai trục','restatement cần decision owner','original và revised outputs cần version','consumer notification là một phần policy','history retention giới hạn answerability','correction cần provenance và reason code')),
Lesson(159,'Lesson_159-star-snowflake-and-the-one-big-table-trade-off','Star, snowflake and the one-big-table trade-off','47-star-snowflake-one-big-table-trade-off.md','wiki.data-modeling.star-snowflake-obt','So sánh star, snowflake và one-big-table theo workload, storage, khả năng thay đổi và mức dễ hiểu như thế nào mà không biến một engine-specific optimization thành quy tắc chung?',(K,A,G),(KL,AL,GL),(
('Star','Star giữ fact ở declared grain và dimensions rộng, descriptive, thường denormalized. Ít join hơn và vocabulary gần nghiệp vụ giúp truy vấn/BI dễ dùng; conformed dimensions hỗ trợ nhiều processes. Chi phí là repeated dimension attributes, SCD processing và cần kiểm grain/additivity. Star không có nghĩa nhét mọi measure vào một fact.'),
('Snowflake','Snowflake chuẩn hoá một phần hierarchy/attributes của dimension thành nhiều bảng. Nó có thể giảm lặp hoặc phù hợp tool/DBMS cụ thể, nhưng thêm join, alias và ripple effect cho SCD. Tiết kiệm dung lượng dimension thường phải được so với tổng footprint fact; không được chọn snowflake chỉ vì nó trông normalized.'),
('One big table','OBT/flat table đưa context tới cùng grain tiêu thụ để giảm join và đơn giản hoá truy cập. Trên BigQuery, nested/repeated fields có thể giữ hierarchy mà không flatten many-side thành duplicate rows. OBT phải có grain rõ; flatten order và lines sai grain làm lặp header measures. Redundancy, rebuild cost, schema width và definition drift là chi phí thật.'),
('Bốn trục so sánh','Performance đo bytes scanned, shuffle, joins, latency p50/p95 và concurrency; storage đo compressed bytes cùng refresh cost; changeability đo artifacts/jobs/consumers bị ảnh hưởng; usability đo thời gian và error rate của người chưa biết schema. Chỉ so trên cùng data snapshot, semantic results, partition/clustering và workload. Một query nhanh không chứng minh model tốt hơn.'),
('Lựa chọn có thể đảo ngược','Star phù hợp shared analytics và governed dimensions; snowflake có thể hợp khi engine/tool khai thác hierarchy hoặc attribute reuse; OBT hợp bounded data product/read pattern có refresh contract. Lựa chọn đảo khi workload, engine, change frequency, team skill hay governance thay đổi. Semantic layer và lineage phải giữ một định nghĩa metric qua các physical layouts.'),
),('star có fact và denormalized dimensions','snowflake chuẩn hoá dimension hierarchy','OBT vẫn phải có declared grain','flatten one-to-many có thể lặp header measure','nested repeated khác flat duplication','join count không phải chi phí duy nhất','bytes scanned và shuffle phải đo','compressed storage phải gồm refresh cost','change blast radius phải được đếm','usability cần task test với người dùng','star có thể đã đủ nhanh trên BigQuery','snowflake SCD có ripple effect','OBT cần definition ownership','semantic result phải giống nhau khi benchmark','lựa chọn cần điều kiện đảo ngược')),
Lesson(160,'Lesson_160-data-vault-at-a-level-sufficient-to-recognise-it','Data Vault at a level sufficient to recognise it','48-data-vault-at-recognition-level.md','wiki.data-modeling.data-vault-recognition','Nhận diện Hub–Link–Satellite, phân biệt Raw Vault với delivery model và đánh giá chi phí/phù hợp mà không tuyên bố năng lực triển khai Data Vault?',(V,B,K),(VL,BL,KL),(
('Hub','Hub đại diện business concept identity qua business key ổn định và metadata load/source; descriptive attributes không nằm trong Hub. Nhận diện bằng grain một business key duy nhất, không bằng tên bảng có tiền tố `HUB_`. Việc chọn sai business key bị automation nhân rộng rất nhanh.'),
('Link','Link ghi association/unit of work giữa Hubs, thường là insert-only và mang các hub keys cùng load/source metadata. Relationship grain phải được phát biểu; Link không phải generic join table được tạo cho mọi FK. Dependent child, driving key và effectivity là các chủ đề nâng cao nằm ngoài năng lực triển khai của bài.'),
('Satellite','Satellite chứa descriptive context và history gắn với Hub/Link, tách theo source, rate of change hoặc meaning khi cần. Load timestamp/hashdiff/record source hỗ trợ historization và provenance; chúng không tự sửa data quality hoặc identity semantics. Một parent có thể có nhiều Satellites và cần point-in-time logic để ghép state hiện hành.'),
('Raw, Business và delivery','Raw Vault bảo toàn loaded source-aligned evidence; Business Vault thêm derived rules/structures có lineage; Information Mart/dimensional/semantic layer phục vụ consumption. Raw Vault không phải giao diện tối ưu cho analyst. Truy vấn customer current state có thể cần nhiều joins, latest-row logic và PIT/bridge acceleration.'),
('Khi nào phù hợp','Data Vault có lý khi nhiều sources thay đổi, cần lineage/audit/history cao và tổ chức có automation, modeling discipline cùng delivery layer. Nó có thể quá nặng cho một source ổn định, team nhỏ, nhu cầu delivery nhanh hoặc không có metadata/automation. Chi phí gồm table/join proliferation, orchestration, testing, skill và nuôi thêm mart layer.'),
),('Hub giữ stable business keys không giữ descriptors','Link giữ relationship grain','Satellite giữ context/history và source metadata','tên prefix không chứng minh object đúng pattern','Raw Vault không phải BI presentation layer','Business Vault phải giữ lineage của derived rules','Information Mart phục vụ consumption','insert-only không tự bảo đảm data quality','hash key không sửa sai business identity','current-state query có latest-row logic','PIT/bridge là access structures không đổi Raw Vault meaning','nhiều source thay đổi tăng giá trị auditability','team nhỏ có thể không gánh được hai delivery layers','Data Vault không thay dimensional model cho BI','bài này chỉ chứng minh recognition không implementation competence')),
)

VERIFY={
156:'Dựng một star có hai date roles, transaction number, sáu flags và multivalued sales reps. Ghi input/output grain, cardinality và control total; chạy query không allocation, có allocation và impact-only để chứng minh điểm khác.',
157:'Tạo timeline gồm normal change, correction, late-arriving change và rerun. Kiểm no-overlap, exactly-one-current, stable business key, surrogate lookup theo effective time và report as-was/as-is. Chạy lại cùng batch để bắt version trùng.',
158:'Dựng bitemporal fixture có một fact được biết muộn và một correction. Viết bốn query cố định valid/system cutoffs; kiểm interval overlap, temporal join và diff original/revised report cùng provenance.',
159:'Materialize cùng snapshot và metric contract thành star, snowflake và OBT/nested layout. Chạy cùng năm query sau warm-up; lưu plan, bytes, shuffle, latency, storage, refresh time, semantic diff và change-blast-radius.',
160:'Cho một lược đồ không dán nhãn, xác định business keys, relationship grain, descriptive history và source metadata để nhận Hub–Link–Satellite. Viết current-state query, đếm joins và so ba bối cảnh theo audit/change/team/automation/delivery cost.',
}

def fm(x):
    src='\n'.join(f'  - {s}' for s in x.sources)
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
{src}
aliases: [{x.title}]
tags: [wiki/database-systems, data-modeling, module-11]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/{x.filename}
---
'''

def deep_note(x):
    parts=[fm(x),f'# {x.title}\n\n> [!abstract] Câu hỏi trung tâm\n> {x.question}\n']
    for i,(heading,body) in enumerate(x.core,1): parts.append(f'\n## {i}. {heading}\n\n{body}\n')
    parts.append('\n## 6. Ma trận kiểm chứng từng mệnh đề\n\nMỗi mệnh đề phải chuyển thành fixture, invariant và phép đối chiếu tái chạy được. Tên pattern, sơ đồ hoặc một query chạy không lỗi không tự chứng minh đúng grain và semantics.\n')
    for i,probe in enumerate(x.probes,1):
        parts.append(f'\n### 6.{i}. {probe}\n\n**Mệnh đề cần kiểm.** {probe}. **Thiết kế phép kiểm.** {VERIFY[x.number]} **Bằng chứng đạt.** Lưu model/metric contract, seed data, SQL/notebook, raw output, row counts, distinct keys, unmatched rate và control totals. Nếu kết quả phụ thuộc engine, cutoff hoặc business policy, phải ghi điều kiện đó cùng phản ví dụ.\n')
    parts.append('\n## 7. Quy trình phản biện\n\n1. Viết business question, grain, identity, time semantics và aggregation contract.\n2. Tách source fact, quyết định thiết kế và synthesis của giáo trình.\n3. Dựng ca biên nhỏ nhất có thể làm query đúng cú pháp nhưng sai số.\n4. Kiểm key, interval, cardinality và control total trước–sau transform/join.\n5. Chạy replay, late data hoặc schema change phù hợp với bài; lưu failed run.\n6. Phân biệt correctness, usability, performance và governance; một trục đạt không che lấp trục khác.\n7. Ghi owner, version, policy và điều kiện làm lựa chọn hiện tại không còn đúng.\n')
    parts.append('\n## 8. Câu hỏi tự kiểm tra\n\n1. Pattern trong bài giải failure mode nào và không giải failure mode nào?\n2. Row đại diện điều gì, có hiệu lực khi nào và được nhận dạng bằng gì?\n3. Ca biên nào làm SUM, current-state lookup hoặc history query sai âm thầm?\n4. Constraint/test nào bắt lỗi cấu trúc; phần ngữ nghĩa nào cần owner xác nhận?\n5. Late data, correction, replay hoặc model change ảnh hưởng output đã công bố ra sao?\n6. Nguồn nào hỗ trợ trực tiếp và phần nào là synthesis của bài?\n')
    parts.append('\n## 9. Giới hạn và điều chưa cho phép kết luận\n\n- Chưa chạy modeling lab, benchmark, late-data replay hay reconciliation; phép kiểm là protocol, không phải kết quả đã đo.\n- Type number sau SCD Type 3 không hoàn toàn thống nhất giữa mọi tài liệu; implementation phải mô tả behavior.\n- BigQuery guidance là engine-specific; không suy OBT luôn nhanh hoặc rẻ hơn.\n- SQL Server system-versioned temporal table quản system time; business-valid time là trục khác.\n- Bài Data Vault chỉ xác nhận khả năng nhận diện và đánh giá bối cảnh, không xác nhận năng lực triển khai DV2.\n')
    refs='\n'.join(f'{i}. [[{link}]]' for i,link in enumerate(x.source_links,1))
    coverage='\n'.join(f'| [[{link}]] | Khái niệm, ranh giới và phản ví dụ liên quan đến bài | Đã đọc phạm vi có locator; không suy ngoài phạm vi |' for link in x.source_links)
    parts.append(f'\n## Reference\n\n{refs}\n\n## Source coverage\n\n| Source slice | Nội dung sử dụng | Trạng thái |\n|---|---|---|\n{coverage}\n\n## Key takeaways\n\n- Chọn pattern theo failure mode, grain, time và workload; không chọn theo tên gọi.\n- Key/interval/cardinality đúng về cấu trúc vẫn cần business semantics và owner.\n- History và restatement là data contract có tác động tới người dùng, không chỉ là ETL technique.\n- Layout physical phải được so trên cùng workload và semantic output.\n- Chưa chạy lab thì note là tài liệu học thuật đã truy nguồn, không phải chứng nhận production.\n')
    return ''.join(parts)

def folder(x): return BASE/x.directory

NEW_SOURCES=(
 {'source_id':A,'record_path':'1_Nguon/Books/SRC-ADAMSON-STAR-SCHEMA-COMPLETE-REFERENCE.md','canonical_path':'/home/kina2711/PROJECT/data-trainer/Material/DE/Reference/Library/book/Ôn DE/Star Schema.pdf','sha256':'bae9c4569463cf0da3311c9e945587da48d6bf35eed3dad9cc5dd90fca181766','rights':'copyrighted-private-owner-provided'},
 {'source_id':M,'record_path':'1_Nguon/Web/SRC-MICROSOFT-SQL-SERVER-TEMPORAL-TABLES.md','canonical_url':'https://learn.microsoft.com/en-us/sql/relational-databases/tables/temporal-tables','captured':'2026-10-01','rights':'public-web-documentation'},
 {'source_id':G,'record_path':'1_Nguon/Web/SRC-GOOGLE-BIGQUERY-DENORMALIZATION.md','canonical_url':'https://cloud.google.com/bigquery/docs/best-practices-performance-nested','captured':'2026-10-01','rights':'public-web-documentation'},
 {'source_id':V,'record_path':'1_Nguon/Web/SRC-DATA-VAULT-ALLIANCE-FOUNDATIONS.md','canonical_url':'https://datavaultalliance.com/engineering/agile-methodology/','captured':'2026-10-01','rights':'public-web-content'},
 {'source_id':B,'record_path':'1_Nguon/Web/SRC-DATAVAULT-BUILDER-MAIN-DOCUMENTATION.md','canonical_url':'https://docs.datavault-builder.com/documentation/latest/_modules/dataVault','captured':'2026-10-01','rights':'public-web-documentation'},
)

def update_manifest(check=False):
    path=ROOT/'Docs/Second-Brain/second-brain-manifest.json'; data=json.loads(path.read_text())
    existing={s['source_id'] for s in data['source_registry']}
    data['source_registry'].extend(s for s in NEW_SOURCES if s['source_id'] not in existing)
    ids={x.note_id for x in LESSONS}
    data['note_registry']=[n for n in data['note_registry'] if n.get('note_id') not in ids]
    data['retrieval_test_set']=[q for q in data['retrieval_test_set'] if q.get('expected_note_id') not in ids]
    queries={
      156:['Bridge làm double count như thế nào?','Junk dimension khác degenerate dimension ra sao?','Role-playing date dimension cần alias gì?'],
      157:['Hai bất biến của SCD Type 2 là gì?','Type 1 làm sai lịch sử báo cáo ra sao?','Late-arriving SCD change tách interval thế nào?'],
      158:['Valid time khác system time thế nào?','Correction khác business change ra sao?','Restatement policy phải có owner nào?'],
      159:['Star snowflake và OBT nên so theo tiêu chí nào?','Vì sao flatten one-to-many làm lặp measure?','BigQuery nested data khác OBT phẳng ra sao?'],
      160:['Hub Link Satellite giữ loại dữ liệu nào?','Raw Vault có phải presentation layer không?','Khi nào Data Vault không phù hợp?'],
    }
    for x in LESSONS:
        data['note_registry'].append({'note_id':x.note_id,'path':f'2_Wiki/Database-Systems/{x.title}.md','status':'review','source_ids':list(x.sources),'last_verified':'2026-10-01'})
        data['retrieval_test_set'].extend({'query':q,'expected_note_id':x.note_id} for q in queries[x.number])
    data['version']='1.0.31'; data['updated_at']='2026-10-01T23:00:00+07:00'
    data['layers']['1_Nguon']['source_count']=len(data['source_registry']); data['layers']['2_Wiki']['note_count']=len(data['note_registry'])
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
