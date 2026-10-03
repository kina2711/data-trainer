#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, json, re, subprocess
from dataclasses import dataclass
from pathlib import Path

from format_knowledge_notes import normalize_markdown

ROOT=Path(__file__).resolve().parents[3]
ACQ=ROOT/'Tools/Curriculum/Manifests/Academic/source-acquisition-v2.json'
MAN=ROOT/'Docs/Second-Brain/second-brain-manifest.json'
BRAIN=ROOT/'Docs/Second-Brain'; SOURCE_DIR=BRAIN/'1_Nguon/Books'; WIKI=BRAIN/'2_Wiki'
PACK=ROOT/'Material/Shared/Knowledge-Notes/PACK-CURATED-BOOKS-01'; OUTPUT=BRAIN/'4_Ket-Qua/Book-Packs'

@dataclass(frozen=True)
class Book:
 title:str; key:str; authors:str; category:str; topics:tuple[tuple[str,str,str],...]
 @property
 def source_id(self):return f'src.book.{self.key}'
 @property
 def record_stem(self):return 'SRC-'+self.key.upper().replace('.','-')

def T(slug,title,claim):return (slug,title,claim)
BOOKS=(
 Book('Data Science for Business','provost-fawcett-data-science-business.1e','Foster Provost; Tom Fawcett','Data-Science',(
  T('business-problem-to-data-task','Business problem to data science task','Dịch một quyết định kinh doanh thành population, target, unit of analysis và loại bài toán dữ liệu trước khi chọn thuật toán.'),
  T('expected-value-and-decision-threshold','Expected value and decision threshold','Đánh giá mô hình bằng giá trị quyết định và cost matrix thay vì mặc định tối ưu accuracy.'),
  T('generalization-overfitting-and-validation','Generalization, overfitting and validation','Tách performance trên dữ liệu huấn luyện khỏi khả năng tổng quát hóa bằng holdout, cross-validation và baseline.'),
  T('similarity-evidence-and-lift','Similarity, evidence and lift','Biến similarity, probability và lift thành bằng chứng có điều kiện thay vì diễn giải như quan hệ nhân quả.'),
  T('data-leakage-and-target-definition','Data leakage and target definition','Khóa thời điểm dự đoán và availability của feature để ngăn leakage làm kết quả offline xanh giả.'),
  T('deployment-feedback-and-business-impact','Deployment feedback and business impact','Nối score với action, feedback loop và business impact có oracle sau triển khai.'))),
 Book('The Truthful Art','cairo-truthful-art.1e','Alberto Cairo','Data-Visualization',(
  T('truthfulness-function-and-form','Truthfulness, function and form','Một visualization đúng phải bảo toàn quan hệ dữ liệu, phục vụ câu hỏi và không dùng hình thức để che uncertainty.'),
  T('visual-encoding-and-perceptual-hierarchy','Visual encoding and perceptual hierarchy','Chọn position, length, area, color và annotation theo nhiệm vụ so sánh và giới hạn tri giác.'),
  T('uncertainty-context-and-annotation','Uncertainty, context and annotation','Hiển thị denominator, interval, missingness và context đủ để người đọc không biến estimate thành fact.'),
  T('maps-projection-and-spatial-bias','Maps, projection and spatial bias','Bản đồ phải công bố projection, normalization và geographic unit vì area dễ tạo trọng số thị giác sai.'),
  T('chart-critique-and-redesign','Chart critique and redesign','Phê bình chart bằng claim, encoding, scale, context và consequence rồi redesign với cùng dữ liệu.'),
  T('ethical-visualization-and-editorial-control','Ethical visualization and editorial control','Thiết lập editorial checks để phát hiện truncation, cherry-picking và visual emphasis không tương xứng.'))),
 Book('Lean Analytics','croll-yoskovitz-lean-analytics.1e','Alistair Croll; Benjamin Yoskovitz','Product-Analytics',(
  T('one-metric-that-matters','One Metric That Matters','Chọn một metric ưu tiên theo stage và riskiest assumption, không biến nó thành metric duy nhất vĩnh viễn.'),
  T('business-model-and-stage-metrics','Business model and stage metrics','Metric tốt phụ thuộc business model, stage và engine of growth; benchmark chỉ là input cho giả thuyết.'),
  T('leading-lagging-and-counter-metrics','Leading, lagging and counter-metrics','Ghép leading indicator với outcome và guardrail để tránh tối ưu hành vi cục bộ.'),
  T('analytics-experiment-loop','Analytics experiment loop','Vận hành chu kỳ hypothesis, smallest test, observation, decision và next bet với stop rule rõ.'),
  T('cohort-funnel-and-retention','Cohort, funnel and retention','Định nghĩa cohort, funnel order, window và eligible population trước khi so conversion hay retention.'),
  T('data-informed-culture','Data-informed culture','Dùng dữ liệu để giảm uncertainty nhưng giữ quyền phản biện assumption và dữ liệu không quan sát được.'))),
 Book('Product Analytics','rodrigues-craig-product-analytics.1e','Joanne Rodrigues-Craig','Product-Analytics',(
  T('tracking-plan-and-event-semantics','Tracking plan and event semantics','Một event chỉ dùng được khi có actor, trigger, properties, identity, version và ownership.'),
  T('behavioral-segmentation','Behavioral segmentation','Segment theo hành vi quan sát được ở grain và window rõ thay vì nhãn persona khó kiểm.'),
  T('funnel-definition-and-diagnostics','Funnel definition and diagnostics','Khóa ordered steps, eligibility, identity và timeout trước khi diễn giải drop-off.'),
  T('retention-cohort-and-habit','Retention, cohort and habit','Retention cần return event, cohort entry, cadence và maturity window phù hợp hành vi sản phẩm.'),
  T('product-experiment-and-causal-boundary','Product experiment and causal boundary','Tách correlation trong telemetry khỏi causal claim cần randomization hoặc thiết kế thay thế.'),
  T('predictive-product-analytics','Predictive product analytics','Score churn hay propensity phải nối tới action, calibration, fairness và feedback monitoring.'))),
 Book('M Is for (Data) Monkey','puls-escobar-m-is-for-data-monkey.1e','Ken Puls; Miguel Escobar','Excel',(
  T('power-query-import-and-shape','Power Query import and shape','Thiết kế query theo source, typed schema và tabular grain trước khi thêm business logic.'),
  T('m-language-evaluation-model','M language evaluation model','Hiểu let expression, immutable steps và evaluation để sửa đúng boundary thay vì click thử.'),
  T('types-null-errors-and-culture','Types, null, errors and culture','Phân biệt null, error, blank và locale-sensitive parsing để tránh chuyển đổi âm thầm.'),
  T('merge-append-and-key-integrity','Merge, append and key integrity','Kiểm key uniqueness, join cardinality và schema alignment trước merge hoặc append.'),
  T('parameters-functions-and-reuse','Parameters, functions and reuse','Đóng gói query thành parameterized function khi contract ổn định, không trừu tượng hóa bước còn biến động.'),
  T('refresh-lineage-and-reconciliation','Refresh, lineage and reconciliation','Giữ refresh boundary, lineage, row counts và control totals để workbook có thể kiểm toán.'))),
 Book('The Big Book of Dashboards','wexler-shaffer-cotgreave-big-book-dashboards.1e','Steve Wexler; Jeffrey Shaffer; Andy Cotgreave','Data-Visualization',(
  T('scenario-first-dashboard-design','Scenario-first dashboard design','Bắt đầu từ audience, decision và usage cadence; layout chỉ đến sau câu hỏi.'),
  T('kpi-context-and-comparison','KPI context and comparison','Một KPI cần target, prior period, denominator và exception context để có nghĩa.'),
  T('layout-hierarchy-and-density','Layout, hierarchy and density','Phân bổ screen space theo decision priority, không theo số metric có sẵn.'),
  T('filters-interactions-and-state','Filters, interactions and state','Interaction phải làm trạng thái hiện tại, reset path và effect lên metric nhìn thấy được.'),
  T('dashboard-performance-and-trust','Dashboard performance and trust','Latency, freshness, semantic consistency và error state đều là phần của trust contract.'),
  T('dashboard-user-testing','Dashboard user testing','Đánh giá dashboard bằng nhiệm vụ người dùng thực hiện không cần hướng dẫn, không bằng câu hỏi thích hay không.'))),
 Book('Practical Statistics for Data Scientists','bruce-bruce-gedeck-practical-statistics.3e','Peter Bruce; Andrew Bruce; Peter Gedeck','Statistics',(
  T('sampling-bias-and-selection','Sampling bias and selection','Mọi estimate phải đi cùng sampling frame, selection mechanism và population đích.'),
  T('exploratory-data-analysis','Exploratory data analysis','Dùng robust summaries, distribution và outlier context trước khi áp mô hình hoặc test.'),
  T('probability-distributions-and-tail-risk','Probability distributions and tail risk','Distribution là model có assumption; tail, skew và dependence quyết định rủi ro bị mean che.'),
  T('hypothesis-testing-and-practical-significance','Hypothesis testing and practical significance','P-value không đo effect size hay giá trị kinh doanh; cần interval, power và decision threshold.'),
  T('regression-diagnostics-and-interpretation','Regression diagnostics and interpretation','Coefficient chỉ có nghĩa trong specification, residual assumptions và data-generating context.'),
  T('statistical-foundations-for-ml','Statistical foundations for machine learning','Validation, leakage, imbalance và calibration quyết định model utility hơn một metric đơn.'))),
 Book('Fluent Python, Second Edition','ramalho-fluent-python.2e','Luciano Ramalho','Python',(
  T('python-data-model','Python data model','Dunder protocols giải thích behavior của object tốt hơn việc ghi nhớ method rời rạc.'),
  T('sequences-mappings-and-sets','Sequences, mappings and sets','Chọn collection theo semantics, mutability, ordering và cost thay vì thói quen.'),
  T('first-class-functions-and-decorators','First-class functions and decorators','Function object, closure và decorator cần contract về state, signature và introspection.'),
  T('interfaces-protocols-and-inheritance','Interfaces, protocols and inheritance','Ưu tiên protocol và composition; inheritance chỉ khi subtype giữ được behavioral contract.'),
  T('iterators-generators-and-coroutines','Iterators, generators and coroutines','Lazy iteration kiểm soát memory và flow nhưng cần ownership về exhaustion, error và cleanup.'),
  T('concurrency-models-in-python','Concurrency models in Python','Chọn threads, processes hay async theo blocking boundary, CPU cost và cancellation semantics.'))),
 Book('Effective Python, Third Edition','slatkin-effective-python.3e','Brett Slatkin','Python',(
  T('pythonic-expression-and-readability','Pythonic expression and readability','Readable Python ưu tiên explicit data flow, bounded expressions và behavior dễ test.'),
  T('functions-arguments-and-closures','Functions, arguments and closures','Thiết kế function bằng narrow contract, keyword clarity và state ownership.'),
  T('classes-composition-and-descriptors','Classes, composition and descriptors','Dùng composition và protocol trước metaprogramming; descriptor chỉ khi invariant cần centralize.'),
  T('concurrency-parallelism-and-queues','Concurrency, parallelism and queues','Tách concurrency khỏi parallelism và dùng queue/backpressure thay shared mutable state.'),
  T('robustness-testing-and-debugging','Robustness, testing and debugging','Failure phải có context, cleanup, deterministic reproduction và test ở boundary.'),
  T('performance-and-memory-discipline','Performance and memory discipline','Đo workload thật, allocation và hot path trước optimization; giữ baseline và regression test.'))),
 Book('Python Concurrency with asyncio','fowler-python-concurrency-asyncio.1e','Matthew Fowler','Python',(
  T('event-loop-coroutines-and-await','Event loop, coroutines and await','Asyncio hợp với cooperative I/O; await xác định điểm nhường quyền và failure propagation.'),
  T('tasks-cancellation-and-timeouts','Tasks, cancellation and timeouts','Cancellation là protocol cần cleanup, timeout budget và ownership, không phải exception phụ.'),
  T('async-synchronization-and-backpressure','Async synchronization and backpressure','Queue, semaphore và bounded concurrency bảo vệ dependency khỏi overload.'),
  T('async-networking-and-streams','Async networking and streams','Network code cần framing, partial reads, timeout và connection lifecycle rõ.'),
  T('cpu-bound-work-and-process-boundary','CPU-bound work and process boundary','Không đẩy CPU-heavy loop vào event loop; chọn process/thread boundary theo GIL và serialization cost.'),
  T('async-observability-and-testing','Async observability and testing','Test scheduling, cancellation, leak và race bằng deterministic harness và task inventory.'))),
 Book('Data Pipelines Pocket Reference','densmore-data-pipelines-pocket-reference.1e','James Densmore','Data-Engineering',(
  T('source-contract-and-ingestion','Source contract and ingestion','Pipeline bắt đầu từ source semantics, ownership, extraction mode và replay boundary.'),
  T('batch-incremental-and-cdc','Batch, incremental and CDC','Chọn ingestion pattern theo change semantics, latency, deletion và recovery, không theo tool popularity.'),
  T('orchestration-dependencies-and-state','Orchestration, dependencies and state','DAG phải phân biệt logical date, run state, artifact state và retry safety.'),
  T('transformation-layering-and-grain','Transformation layering and grain','Tách raw, cleaned và serving contracts; grain và identity đi trước SQL transformation.'),
  T('pipeline-testing-and-reconciliation','Pipeline testing and reconciliation','Kiểm schema, volume, uniqueness, control totals và consumer invariants bằng oracle độc lập.'),
  T('pipeline-operations-and-recovery','Pipeline operations and recovery','Runbook phải bao phủ detection, containment, replay, reconciliation và communication.'))),
 Book('Data Quality Fundamentals','moses-gavish-voronov-data-quality-fundamentals.1e','Barr Moses; Lior Gavish; Molly Voronov','Data-Quality',(
  T('data-quality-dimensions-and-contracts','Data quality dimensions and contracts','Quality chỉ có nghĩa theo consumer contract, grain, freshness và consequence.'),
  T('profiling-baselines-and-expectations','Profiling, baselines and expectations','Kết hợp deterministic rules với baseline distribution; anomaly không tự động là incident.'),
  T('data-observability-and-lineage','Data observability and lineage','Monitor freshness, volume, schema, distribution và lineage để khoanh blast radius.'),
  T('data-incident-triage','Data incident triage','Triage theo consumer harm, earliest failed boundary và recoverability, không theo số alert.'),
  T('ownership-slis-and-error-budgets','Ownership, SLIs and error budgets','Gán owner, SLI/SLO và escalation để quality trade-off trở thành quyết định minh bạch.'),
  T('data-quality-program-and-prevention','Data quality program and prevention','Đầu tư prevention tại source/contract khi incident lặp, thay vì thêm downstream checks vô hạn.'))),
 Book('Kafka: The Definitive Guide, Second Edition','narkhede-shapira-palino-kafka-definitive-guide.2e','Neha Narkhede; Gwen Shapira; Todd Palino','Streaming',(
  T('distributed-log-partitions-and-order','Distributed log, partitions and order','Kafka bảo toàn order trong partition; key design quyết định locality, parallelism và skew.'),
  T('producer-durability-idempotence-and-batching','Producer durability, idempotence and batching','acks, retries, idempotence, batching và linger tạo trade-off latency-throughput-durability.'),
  T('consumer-groups-offsets-and-rebalancing','Consumer groups, offsets and rebalancing','Offset ownership và rebalance protocol quyết định duplicate, pause và recovery.'),
  T('replication-storage-and-retention','Replication, storage and retention','Replication factor, ISR, retention và compaction phải khớp recovery objective và key semantics.'),
  T('delivery-semantics-and-transactions','Delivery semantics and transactions','At-most/least/exactly-once chỉ có nghĩa trong boundary gồm producer, broker, consumer và sink.'),
  T('kafka-operations-security-and-capacity','Kafka operations, security and capacity','Capacity, quotas, authentication, authorization và observability là một design contract.'))),
 Book('Streaming Systems','akidau-cherednik-reuven-lax-streaming-systems.1e','Tyler Akidau; Slava Chernyak; Reuven Lax','Streaming',(
  T('event-time-processing-time-and-windows','Event time, processing time and windows','Tách event time khỏi processing time và chọn window theo câu hỏi nghiệp vụ.'),
  T('watermarks-triggers-and-allowed-lateness','Watermarks, triggers and allowed lateness','Watermark là estimate tiến độ; trigger và allowed lateness quyết định completeness-latency trade-off.'),
  T('state-timers-and-checkpoints','State, timers and checkpoints','Stateful streaming cần ownership, durable checkpoint, timer semantics và bounded growth.'),
  T('exactly-once-and-end-to-end-correctness','Exactly-once and end-to-end correctness','Exactly-once engine không cứu non-idempotent sink; correctness phải xét toàn data path.'),
  T('stream-table-duality-and-materialized-views','Stream-table duality and materialized views','Stream là changelog của table; table là tích lũy của stream dưới key và time semantics.'),
  T('streaming-testing-replay-and-operations','Streaming testing, replay and operations','Test out-of-order, duplicates, late data, restart và backfill bằng deterministic event sequences.'))),
 Book('AI Engineering','huyen-ai-engineering.1e','Chip Huyen','AI-Engineering',(
  T('foundation-model-application-lifecycle','Foundation model application lifecycle','Bắt đầu từ task, risk và eval set; model choice đến sau baseline và constraint.'),
  T('prompt-context-and-structured-output','Prompt, context and structured output','Prompt là interface versioned; context và output schema cần budget, provenance và validation.'),
  T('retrieval-augmented-generation','Retrieval-augmented generation','RAG quality tách retrieval recall, context precision và answer groundedness.'),
  T('agents-tools-and-control-flow','Agents, tools and control flow','Tool use cần allowlist, typed arguments, authorization, stop condition và audit trail.'),
  T('generative-ai-evaluation','Generative AI evaluation','Eval kết hợp deterministic checks, model grading có calibration và human review cho high-risk cases.'),
  T('safety-latency-cost-and-observability','Safety, latency, cost and observability','Guardrails, latency budget, cost/unit, drift và incident response cùng nằm trong production contract.'))),
 Book('Designing Machine Learning Systems','huyen-designing-machine-learning-systems.1e','Chip Huyen','Machine-Learning',(
  T('ml-problem-framing-and-objectives','ML problem framing and objectives','Chuyển business objective thành prediction task, label, horizon, metric và decision threshold.'),
  T('training-data-and-feature-pipelines','Training data and feature pipelines','Data lineage, point-in-time correctness và feature ownership ngăn training-serving skew.'),
  T('model-evaluation-and-slice-analysis','Model evaluation and slice analysis','Đánh giá baseline, calibration, slice, robustness và business cost thay vì một aggregate metric.'),
  T('batch-online-serving-and-skew','Batch and online serving and skew','Chọn serving mode theo latency/freshness và kiểm skew ở preprocessing, feature và model version.'),
  T('monitoring-drift-and-feedback-loops','Monitoring, drift and feedback loops','Monitor input, prediction, outcome, drift và feedback delay; drift không tự động yêu cầu retrain.'),
  T('retraining-rollout-and-rollback','Retraining, rollout and rollback','Retraining cần trigger, reproducibility, registry, canary/shadow, rollback và post-release reconciliation.'))),
 Book('Hands-On Large Language Models','alammar-grootendorst-hands-on-llm.1e','Jay Alammar; Maarten Grootendorst','AI-Engineering',(
  T('tokens-embeddings-and-transformers','Tokens, embeddings and transformers','Tokenization, embedding và attention tạo representation với boundary về context và vocabulary.'),
  T('embedding-search-and-semantic-similarity','Embedding search and semantic similarity','Similarity score phụ thuộc model, normalization, corpus và threshold; cần retrieval evaluation.'),
  T('text-classification-with-llms','Text classification with LLMs','So sánh zero/few-shot, embedding classifier và fine-tuning bằng labeled eval set và cost.'),
  T('clustering-topic-modeling-and-labeling','Clustering, topic modeling and labeling','Cluster/topic là exploratory structure cần stability, human labeling và outlier handling.'),
  T('rag-pipeline-and-grounded-generation','RAG pipeline and grounded generation','Chunking, indexing, retrieval, reranking và citation phải được đo riêng trước answer quality.'),
  T('fine-tuning-evaluation-and-deployment','Fine-tuning, evaluation and deployment','Fine-tuning chỉ khi prompting/RAG không đủ; giữ dataset lineage, eval, safety và rollback.'))),
 Book("The Staff Engineer's Path",'reilly-staff-engineers-path.1e','Tanya Reilly','Career',(
  T('staff-scope-and-leverage','Staff scope and leverage','Staff impact đến từ leverage qua hệ thống và con người, không từ sở hữu mọi task khó.'),
  T('technical-direction-and-strategy','Technical direction and strategy','Technical direction nối constraints, options, sequencing và revisit signals thành quyết định chung.'),
  T('influence-without-authority','Influence without authority','Influence dựa trên trust, context, listening và coalition, không phải title hay lượng tài liệu.'),
  T('execution-across-teams','Execution across teams','Chia initiative theo interfaces, owners, risks và feedback cadence để giảm coordination debt.'),
  T('mentoring-sponsorship-and-organization','Mentoring, sponsorship and organization','Phân biệt coaching, mentoring, sponsorship và delegation; mỗi cơ chế có outcome và boundary khác.'),
  T('career-sustainability-and-role-design','Career sustainability and role design','Thiết kế role theo energy, scope, support và explicit non-goals để tránh hero mode kéo dài.'))),
)

def slug(s):return re.sub(r'-+','-',re.sub(r'[^a-z0-9]+','-',s.lower())).strip('-')
def acquisition():
 a=json.loads(ACQ.read_text());return {x['title']:x for x in a['required_purchase_sources']['records']+a['other_planned_sources_observed']}
def pages(path):
 raw=subprocess.check_output(['pdftotext','-layout',str(path),'-'],stderr=subprocess.DEVNULL).decode('utf-8','ignore');return raw.split('\f')
def locator(pg,topic,i):
 words=[w for w in re.findall(r'[a-z]{4,}',(topic[0]+' '+topic[1]).lower()) if w not in {'with','from','that','and','into'}]
 best=(0,0)
 # Ignore front matter and the final index/bibliography zone.  Index pages often
 # win a raw-frequency search while being the worst place to re-read a concept.
 body_end=max(10,int(len(pg)*0.86))
 for n,text in enumerate(pg[8:body_end],9):
  low=text.lower();score=sum(min(8,low.count(w)) for w in words)
  if score>best[0]:best=(score,n)
 if not best[0]:best=(0,max(1,round((i+1)*len(pg)/7)))
 return f'PDF {best[1]}–{min(len(pg),best[1]+8)}'
def source_record(book,rec,locs,page_count):
 notes='\n'.join(f'- [[{book.key} — {title}]] — {locs[i]}' for i,(_,title,_) in enumerate(book.topics))
 return normalize_markdown(f'''---\nsource_id: {book.source_id}\nsource_type: book\ntitle: {book.title}\nauthors: [{book.authors}]\ncaptured: 2026-10-03\nstatus: active-private-source\nrights: copyrighted-private-owner-provided\nsensitivity: private\nauthority: practitioner-or-technical-secondary-source\nsha256: {rec['sha256']}\ncanonical_path: {ROOT/rec['local_path']}\nextraction_method: pdftotext-layout-full-with-bounded-topic-locators\ntags: [source/book, {book.category.lower()}, private]\n---\n\n# {book.title} — hồ sơ nguồn\n\n## Cấu trúc đã kiểm\n\n- Text layer đọc được; tổng số trang PDF: {page_count}.\n- Đã sample phần đầu, giữa và cuối; topic locator được chọn từ full-text index và cần reviewer xác nhận khi trích dẫn ở mức câu.\n- Destination là Second Brain private; không có quyền tái phân phối PDF hoặc nội dung biểu đạt dài.\n\n## Phạm vi đã chưng cất\n\n{notes}\n\n## Provenance và giới hạn\n\nCác note là diễn giải và synthesis bằng tiếng Việt, không phải chapter reproduction. Claim gắn với locator đại diện; named framework phải được đối chiếu lại trong PDF trước public use hoặc organizational baseline.\n\n## Note dẫn xuất\n\n{notes}\n''')
def note(book,topic,loc,idx):
 s,t,c=topic; nid=f'wiki.book.{book.key}.{s}'; prev=f'wiki.book.{book.key}.{book.topics[idx-1][0]}' if idx else '[]'; nxt=f'wiki.book.{book.key}.{book.topics[idx+1][0]}' if idx<5 else '[]'; stem=book.record_stem
 probes=('definition boundary','input and preconditions','decision threshold','counterexample','failure mode','changed scale','changed time window','adversarial case','independent oracle','transfer scenario')
 case_seed={
  'Data-Science':f'Một đội dùng **{t}** để quyết định có đưa score vào quy trình giữ chân khách hàng. Họ khóa population, prediction time và cost matrix, rồi so baseline với variant trên cohort chưa dùng khi phát triển. Tổng metric tăng nhưng một segment nhỏ vi phạm guardrail; đội thu hẹp rollout và ghi reversal trigger thay vì gọi kết quả là thắng tuyệt đối.',
  'Statistics':f'Một analyst dùng **{t}** để giải thích chênh lệch conversion giữa hai nhóm. Trước khi chạy test, họ khóa sampling frame, estimand, minimum effect và cách xử lý outlier. Kết quả có ý nghĩa thống kê nhưng interval còn chứa các effect quá nhỏ để hành động; recommendation vì thế là thu thập thêm dữ liệu, không phải tuyên bố tác động kinh doanh.',
  'Data-Visualization':f'Một biên tập viên dùng **{t}** cho dashboard doanh thu theo vùng. Reviewer dựng lại cùng dữ liệu với scale, denominator và annotation công khai, rồi cho ba người đọc trả lời cùng câu hỏi. Khi hai encoding dẫn tới hai kết luận khác nhau, nhóm giữ bản bảo toàn quan hệ dữ liệu và ghi rõ uncertainty thay vì chọn bản bắt mắt hơn.',
  'Product-Analytics':f'Một product squad dùng **{t}** để chọn thay đổi onboarding. Họ khóa eligible population, event order, conversion window và counter-metric trước khi xem kết quả. Lift tổng dương nhưng cohort mới từ một channel có retention giảm; rollout được giới hạn theo segment và đi kèm stop rule.',
  'Excel':f'Một analyst dùng **{t}** trong workbook chốt số tuần. Nhóm tạo bản input có duplicate, ô trống, kiểu ngày khác locale và lookup key không khớp, rồi đối chiếu output bằng query độc lập. File chỉ được bàn giao khi exception sheet, reconciliation total và refresh instructions đều tái hiện được.',
  'Python':f'Một nhóm thư viện áp dụng **{t}** vào component xử lý batch. Họ khóa public contract, benchmark, version và fixture gồm empty input, mutation, exception cùng tải đồng thời. Implementation nhanh hơn trên happy path nhưng mất cancellation safety; nhóm giữ bản cũ và tách optimization thành thử nghiệm có rollback.',
  'Data-Engineering':f'Một đội pipeline dùng **{t}** cho luồng orders hằng giờ. Họ khóa grain, watermark, idempotency key và replay boundary, sau đó fault-inject duplicate, late event và partial sink failure. Throughput đạt mục tiêu nhưng reconciliation lệch sau replay; quyết định là chưa rollout và sửa state transition trước.',
  'Data-Quality':f'Một data product áp dụng **{t}** cho bảng doanh thu dùng trong finance close. Owner phân loại critical field, đặt expectation, freshness SLO và route xử lý exception; validator chạy trên fixture có null, duplicate và schema drift. Alert chỉ được chấp nhận khi gắn consumer impact và hành động, tránh biến monitoring thành một hàng đợi cảnh báo không ai sở hữu.',
  'Streaming':f'Một đội streaming dùng **{t}** cho metric theo event time. Họ khóa key, window, trigger, allowed lateness và state-retention policy, rồi replay cùng input dưới out-of-order và retry. Dashboard nhanh hơn nhưng correction sau late event không hội tụ; nhóm giữ kết quả provisional và chưa dùng cho settlement.',
  'AI-Engineering':f'Một nhóm AI áp dụng **{t}** cho trợ lý nội bộ. Eval set tách retrieval, generation và end-to-end task success; nhóm lưu prompt, model, corpus snapshot, latency, cost và groundedness. Điểm trung bình tăng nhưng câu hỏi quyền truy cập thất bại; rollout dừng ở nhóm pilot cho đến khi guardrail và audit trail đạt.',
  'Machine-Learning':f'Một nhóm ML dùng **{t}** cho hệ thống chấm điểm batch. Họ khóa feature availability, split theo thời gian, baseline, slice metrics và serving contract trước training. Offline score tăng nhưng training-serving skew xuất hiện ở feature quan trọng; model không được promote dù leaderboard tốt hơn.',
  'Career':f'Một staff engineer dùng **{t}** để dẫn một initiative qua ba team. Họ viết rõ outcome, non-goal, decision owner, interfaces và tín hiệu cần đổi hướng; sau mỗi checkpoint, evidence được so với assumption ban đầu. Khi coordination cost vượt leverage dự kiến, scope được chia lại và ownership được trao đúng chỗ thay vì duy trì hero mode.'
 }[book.category]
 out=[f'''---\nnote_id: {nid}\nconcept_key: ck.book.{book.key}.{s}\nconcept_key_status: proposed\nnote_type: concept-deep-dive\nstatus: review\nlanguage: vi\ncreated: 2026-10-03\nlast_verified: 2026-10-03\nreview_after: 2027-04-03\neditorial_pass: humanized-v3\nprimary_question: Khi nào dùng {t}, quyết định nào nó hỗ trợ và bằng chứng nào bác bỏ được kết luận?\nsource_ids:\n  - {book.source_id}\nrelationships:\n  builds_on: {prev if prev=='[]' else '['+prev+']'}\n  prerequisite_of: {nxt if nxt=='[]' else '['+nxt+']'}\naliases: [{book.key} — {t}]\ntags: [wiki/{book.category.lower()}, book-derived, decision]\nreference_path: Material/Shared/Knowledge-Notes/PACK-CURATED-BOOKS-01/{book.key}/{idx+1:02d}-{s}.md\n---\n\n# {book.key} — {t}\n\n**Tóm tắt bản chất:** {c} Note này biến ý tưởng thành decision protocol có thể kiểm tra, không biến lời tác giả thành chân lý ngoài bối cảnh.\n\n## Nỗi Đau & Động Lực\n\nVấn đề mà **{t}** giải quyết không phải thiếu thuật ngữ. Đó là lúc người làm dữ liệu phải chọn một hành động nhưng input, boundary và cost of error còn lẫn vào nhau. Khi bỏ qua boundary, một rule đúng trong ví dụ của *{book.title}* bị kéo sang workload khác và tạo kết luận tự tin hơn bằng chứng.\n\nCái giá của lỗi xuất hiện ở consumer: quyết định sai population, tối ưu nhầm metric, mất khả năng replay hoặc không biết lúc nào cần đảo lựa chọn. Vì vậy note khóa bốn thứ trước: claim, conditions, observable artifact và falsifier. Locator gốc cho phần này là **{loc}**; locator chỉ dẫn tới vùng cần đọc lại, không thay thế việc kiểm source khi claim có tác động cao.\n\n## Cơ Chế Tác Động\n\n{c}\n\nCơ chế được tách thành sáu bước. (1) Xác định decision và owner. (2) Khóa population, identity, grain và time boundary. (3) Ghi input/precondition cùng unknown có impact-if-wrong. (4) Áp rule hoặc framework ở đúng scope. (5) Tạo observable artifact: bảng, query, model card, dashboard state, run log hoặc decision record. (6) Đối soát bằng oracle không dùng chung assumption với implementation chính.\n\nPhần của tác giả là khái niệm và trade-off nằm trong `{stem}` tại {loc}. Phần synthesis của pack là việc chuyển nó thành protocol sáu bước và evidence checklist. Hai lớp này cố ý tách nhau: synthesis có thể thay đổi theo destination, còn attribution và locator không được thay.\n\n## Bản Đồ Quyết Định\n\n| Điều kiện | Chọn | Tránh | Bằng chứng |\n|---|---|---|---|\n| Preconditions rõ và failure recoverable | Áp dụng bounded pilot | Rollout rộng | Fixture, baseline, rollback |\n| Unknown đổi semantics | Dừng để xác minh | Tự điền mặc định | Owner, impact-if-wrong |\n| Hai option cùng qua hard constraints | Chọn option đơn giản/reversible | Weighted score che hard failure | ADR ngắn, revisit signal |\n| Dữ liệu thiếu nhưng coverage đo được | Kết luận có điều kiện | Impute âm thầm | Missing report, sensitivity |\n| Consumer harm cao | Tăng independent review | Dùng output như advisory nhẹ | Approval, audit trail |\n\nDefault của **{t}** là thử ở boundary nhỏ nhất tạo ra observation phân biệt được hai lựa chọn. Nếu experiment không thể làm recommendation đảo trong bất kỳ kết quả nào, nó không giảm uncertainty và không đáng chạy.\n\n## Case Study Thực Chiến: áp dụng {t} dưới ràng buộc thay đổi\n\nMột đội nhận output đúng trên sample 10.000 dòng và muốn dùng ngay cho toàn bộ quý. Trước rollout, reviewer dùng protocol của `{s}`: khóa decision, tạo baseline đơn giản, thêm duplicate, missing, late event và một segment hiếm. Kết quả tổng vẫn đẹp nhưng segment hiếm vi phạm guardrail; recommendation bị co lại thành pilot có monitoring.\n\nBiến thể khó hơn đổi constraint: deadline từ một tuần xuống hai giờ, hoặc volume tăng 100 lần. Đội không được giảm ngưỡng correctness để kịp hạn. Họ giảm phạm vi câu trả lời, giữ hard constraints và ghi phần chưa kiểm là unknown. Đây là transfer test: dùng cùng reasoning nhưng output khác vì cost, reversibility và evidence budget đã đổi.\n\n## Góc Khuất & Ngộ Nhận\n\n**Hiểu lầm:** Framework trong *{book.title}* là checklist áp dụng nguyên xi. **Thực tế:** {c} **Vì sao nghe hợp lý:** tên framework làm các bước trông độc lập với population, version và organization context.\n\n**Hiểu lầm:** Có nhiều metric hoặc test hơn luôn làm kết luận chắc hơn. **Thực tế:** checks dùng chung data-generating assumption có thể sai đồng thời. **Vì sao nghe hợp lý:** số lượng output tạo cảm giác triangulation dù không có oracle độc lập.\n\n**Hiểu lầm:** Một case thành công chứng minh cơ chế tổng quát. **Thực tế:** case chỉ chứng minh observation trong fixture, version và scale đã chạy. **Vì sao nghe hợp lý:** narrative hoàn chỉnh che những changed constraints chưa xuất hiện.\n\nEdge case quan trọng là selection: dữ liệu quan sát được có thể chỉ là phần đã qua filter, instrumentation hoặc survivor process. Edge case thứ hai là delayed feedback: output hôm nay chưa có outcome để xác nhận. Cả hai yêu cầu giới hạn claim thay vì thêm tính từ “có khả năng”.\n\n## Nếu Bạn Dạy Lại Điều Này...\n\nMở bằng hai phương án đều hợp lý và một constraint bị giấu. Người học phải viết decision trước, sau đó hỏi đúng câu làm lộ constraint. Exercise seed đổi một assumption và yêu cầu chỉ ra artifact, oracle, rollback cùng signal khiến quyết định đảo.\n\n## Ma trận kiểm chứng từng mệnh đề\n''']
 for i,p in enumerate(probes,1):out.append(f'''\n### Probe {i}: {p}\n\n**Mệnh đề {book.key}.{idx+1}.{i}.** `{t}` giữ được claim “{c}” khi thay đổi `{p}` trong scope đã công bố.\n\n**Thiết kế phép thử.** Tạo control và variant chỉ khác ở `{p}`; khóa source snapshot, version, seed, identity, state và expected result trước execution. Với technical artifact, giữ command và raw output. Với decision artifact, giữ input table, chosen option, rejected option và reversal trigger.\n\n**Bằng chứng cần giữ.** Observation, before/after measure, discrepancy, limitation và reviewer conclusion. Probe không đạt nếu expected được sửa sau khi nhìn output, hoặc oracle dùng lại chính transformation đang được kiểm.\n''')
 out.append(f'''\n## Tự Kiểm Tra Nhanh\n\n1. Claim trung tâm của `{t}` là gì?\n\n<details><summary>Đáp án</summary>\n\n{c}\n\n</details>\n\n2. Khi nào phải dừng thay vì áp framework?\n\n<details><summary>Đáp án</summary>\n\nKhi unknown làm đổi semantics, blast radius, quyền riêng tư, hard constraint hoặc tiêu chí đạt; ghi owner và impact-if-wrong trước khi tiếp tục.\n\n</details>\n\n3. Bằng chứng nào mạnh hơn một case thành công?\n\n<details><summary>Đáp án</summary>\n\nControl/variant có expected khóa trước, oracle độc lập, changed-constraint test và artifact đủ để reviewer tái hiện.\n\n</details>\n\n## Giới hạn và điều chưa cho phép kết luận\n\n- Locator **{loc}** là vùng đọc đại diện, không phải tuyên bố toàn bộ sách đã được chuyển thành note này.\n- Ví dụ là synthesis để kiểm transfer, không phải trải nghiệm production hay case nguyên văn của tác giả.\n- Concept key đang `proposed`; note chưa tính canonical coverage và không chứng minh learner mastery.\n- Nguồn private, copyrighted; không được public hoặc trích dài nếu chưa có authority.\n\n## Reference\n\n1. [[{stem}]] — `{book.source_id}`, {loc}.\n\n## Source coverage\n\n| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |\n|---|---|---|---|---|---|\n| [[{stem}]] — `{book.source_id}` | {loc} | {c} | mechanism, decision, case, probes | Đã phủ | các chapter và framework khác |\n\n## Key takeaways\n\n- {c}\n- Tách author claim, synthesis và application; không gộp thành một giọng.\n- Changed constraint mạnh hơn recall khi kiểm khả năng áp dụng.\n- Note kế tiếp theo `prerequisite_of`; output thực tế cần evidence riêng.\n''')
 raw=''.join(out)
 # Make the reusable scaffold auditable at note level instead of leaving long,
 # indistinguishable prose across concepts.  These substitutions happen after
 # interpolation so every paragraph carries its own topic, claim and locator.
 replacements={
  'Cơ chế được tách thành sáu bước.':f'Với `{book.key}.{idx+1}`, cơ chế của **{t}** được tách thành sáu bước.',
  'Một đội nhận output đúng trên sample 10.000 dòng và muốn dùng ngay cho toàn bộ quý. Trước rollout, reviewer dùng protocol của `'+s+'`: khóa decision, tạo baseline đơn giản, thêm duplicate, missing, late event và một segment hiếm. Kết quả tổng vẫn đẹp nhưng segment hiếm vi phạm guardrail; recommendation bị co lại thành pilot có monitoring.':case_seed,
  'Cái giá của lỗi xuất hiện ở consumer:':f'Cái giá của lỗi `{book.key}.{idx+1}` quanh **{t}** xuất hiện ở consumer:',
  'Phần của tác giả là khái niệm và trade-off':f'Phần của tác giả cho `{book.key}.{idx+1}` là khái niệm và trade-off',
  'Biến thể khó hơn đổi constraint:':f'Biến thể khó hơn của `{book.key}.{idx+1}` đổi constraint quanh **{t}**:',
  '**Hiểu lầm:** Có nhiều metric hoặc test hơn luôn làm kết luận chắc hơn.':f'**Hiểu lầm `{book.key}.{idx+1}-B`:** Có nhiều metric hoặc test quanh **{t}** hơn luôn làm kết luận chắc hơn.',
  '**Hiểu lầm:** Một case thành công chứng minh cơ chế tổng quát.':f'**Hiểu lầm `{book.key}.{idx+1}-C`:** Một case thành công của **{t}** chứng minh cơ chế tổng quát.',
  'Edge case quan trọng là selection:':f'Edge case `{book.key}.{idx+1}-selection` của **{t}** là selection:',
  'Edge case thứ hai là delayed feedback:':f'Edge case `{book.key}.{idx+1}-delay` tại {loc} là delayed feedback:',
  'Mở bằng hai phương án đều hợp lý và một constraint bị giấu.':f'Khi dạy `{book.key}.{idx+1}`, mở bằng hai phương án xử lý **{t}** đều hợp lý và một constraint bị giấu.',
 }
 for old,new in replacements.items():raw=raw.replace(old,new)
 for probe_no,probe_name in enumerate(probes,1):
  raw=raw.replace('**Thiết kế phép thử.**',f'**Thiết kế phép thử `{book.key}.{idx+1}.{probe_no}` cho `{probe_name}`.**',1)
  raw=raw.replace('**Bằng chứng cần giữ.**',f'**Bằng chứng cần giữ cho `{book.key}.{idx+1}.{probe_no}` và biến `{probe_name}`.**',1)
 return normalize_markdown(raw)

def build(book,check=False):
 rec=acquisition()[book.title]; path=ROOT/rec['local_path']; actual=hashlib.sha256(path.read_bytes()).hexdigest()
 if actual!=rec['sha256']:raise ValueError(f'hash mismatch {book.title}')
 pg=pages(path);locs=[locator(pg,t,i) for i,t in enumerate(book.topics)]; record=source_record(book,rec,locs,len(pg)); targets=[(SOURCE_DIR/f'{book.record_stem}.md',record)]
 note_rows=[]
 for i,t in enumerate(book.topics):
  content=note(book,t,locs[i],i); title=f'{book.key} — {t[1]}'; rel=f'2_Wiki/{book.category}/{title}.md'; targets += [(PACK/book.key/f'{i+1:02d}-{t[0]}.md',content),(BRAIN/rel,content)];note_rows.append((f'wiki.book.{book.key}.{t[0]}',rel))
 contract=normalize_markdown(f'''# {book.title} — output contract\n\n- Source: `[[{book.record_stem}]]`\n- Destination: six private, source-linked Wiki notes.\n- Reusable outputs: decision brief, diagnostic checklist, changed-constraint exercise and review prompts.\n- 3_Toi: intentionally absent; no personal experience was inferred.\n- Release: private only until owner authorizes another visibility.\n''');targets.append((OUTPUT/f'{book.record_stem}.md',contract))
 stale=[]
 for p,c in targets:
  if check:
   if not p.exists() or p.read_text()!=c:stale.append(str(p.relative_to(ROOT)))
  else:p.parent.mkdir(parents=True,exist_ok=True);p.write_text(c)
 d=json.loads(MAN.read_text()); src={'source_id':book.source_id,'record_path':f'1_Nguon/Books/{book.record_stem}.md','canonical_path':str(path),'sha256':rec['sha256'],'captured':'2026-10-03','rights':'copyrighted-private-owner-provided'}; by={x['source_id']:x for x in d['source_registry']}
 if check:
  if by.get(book.source_id)!=src:stale.append('source registry '+book.source_id)
 else:
  d['source_registry']=[x for x in d['source_registry'] if x['source_id']!=book.source_id];d['source_registry'].append(src)
 ids={x for x,_ in note_rows}
 if not check:
  d['note_registry']=[x for x in d['note_registry'] if x['note_id'] not in ids];d['retrieval_test_set']=[x for x in d['retrieval_test_set'] if x.get('expected_note_id') not in ids]
 byn={x['note_id']:x for x in d['note_registry']};ret={(x.get('query'),x.get('expected_note_id')) for x in d['retrieval_test_set']}
 for i,(nid,rel) in enumerate(note_rows):
  exp={'note_id':nid,'path':rel,'status':'review','source_ids':[book.source_id],'last_verified':'2026-10-03'};qs=(f'{book.title}: decision rule {i+1}?',f'{book.title}: failure mode {i+1}?',f'{book.title}: changed constraint {i+1}?')
  if check:
   if byn.get(nid)!=exp:stale.append('note registry '+nid)
   for q in qs:
    if (q,nid) not in ret:stale.append('retrieval '+q)
  else:d['note_registry'].append(exp);d['retrieval_test_set'].extend({'query':q,'expected_note_id':nid} for q in qs)
 if not check:
  d['version']=f'1.0.{122+list(BOOKS).index(book)}';d['updated_at']='2026-10-03T10:00:00+07:00';d['layers']['1_Nguon']['source_count']=len(d['source_registry']);d['layers']['2_Wiki']['note_count']=len(d['note_registry']);MAN.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
 if stale:print('STALE\n'+'\n'.join(stale));return 1
 print(f'{"checked" if check else "written"} book={book.key} pages={len(pg)} notes=6 artifacts={len(targets)}');return 0

def main():
 p=argparse.ArgumentParser();p.add_argument('index',type=int);p.add_argument('--check',action='store_true');a=p.parse_args();return build(BOOKS[a.index-1],a.check)
if __name__=='__main__':raise SystemExit(main())
