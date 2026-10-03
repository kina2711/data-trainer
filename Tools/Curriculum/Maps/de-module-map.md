# DE v5.0 — bản đồ module đề xuất (bản 3: ba công cụ điều phối ngang độ sâu)

Nguồn: `/home/kina2711/PROJECT/roadmap-de/ROADMAP_DATA_ENGINEER_0_TO_ARCHITECT.md`
(9 chặng) cộng `List học.md` (22 level, ~150 chủ đề).
Quy đổi: 1 bài = 2 giờ trên lớp + 2,2 giờ tự học = 4,2 giờ.

Nguyên tắc bản 2: **một công cụ lớn là một module**, và mỗi nhóm công cụ có
một module nền không phụ thuộc công cụ đứng trước, cùng một module so sánh đứng sau.
Module nền dạy khái niệm để module so sánh có tiêu chí chấm; không có nó thì
so sánh biến thành liệt kê tính năng.

| Chặng | Module | Tên | Mức | Bài |
|---|---|---|---|---:|
| 0 | M1 | Introduction to the Data Engineer Role and the Learning System | | 5 |
| 1 | M2 | Computers - CPU, memory, storage and the cost of a computation | | 12 |
| 1 | M3 | Operating systems and Linux | | 12 |
| 1 | M4 | Networking for data engineers | | 10 |
| 1 | M5 | Algorithms and data structures for data work | | 10 |
| 1 | M6 | Concurrency, parallelism and correctness under contention | | 12 |
| 2 | M7 | Python for data engineering | | 16 |
| 2 | M8 | Software engineering - Git, testing, packaging, APIs | | 14 |
| 3 | M9 | SQL from zero to advanced | | 16 |
| 3 | M10 | The life of a query - database internals | | 14 |
| 3 | M11 | PostgreSQL | `A` | 14 |
| 3 | M12 | MySQL | `B` | 8 |
| 3 | M13 | MongoDB | `B` | 8 |
| 3 | M14 | Redis | `B` | 7 |
| 3 | M15 | BigQuery | `B` | 8 |
| 3 | M16 | ClickHouse | `B` | 8 |
| 3 | M17 | Elasticsearch | `B` | 8 |
| 3 | M18 | Choosing a database - polyglot design and defence | | 6 |
| 4 | M19 | Data modeling and warehousing | | 14 |
| 4 | M20 | Batch ingestion, accuracy and data quality | | 16 |
| 5 | M21 | Orchestration foundations - DAG, state, schedule, backfill | | 6 |
| 5 | M22 | Apache Airflow | `A` | 12 |
| 5 | M23 | Dagster | `A` | 12 |
| 5 | M24 | Prefect | `A` | 12 |
| 5 | M25 | Choosing an orchestrator - the evidence matrix (Kestra `C` ở đây) | | 6 |
| 5 | M26 | Data contracts and dataset handover | | 10 |
| 6 | M27 | Messaging foundations - delivery semantics, ordering, DLQ, replay | | 6 |
| 6 | M28 | RabbitMQ | `B` | 8 |
| 6 | M29 | Apache Kafka | `A` | 14 |
| 6 | M30 | Choosing a message system - queue against log | | 4 |
| 6 | M31 | Change data capture with Debezium | `B` | 8 |
| 6 | M32 | Stream processing - Spark Structured Streaming and Flink | `A`/`B` | 12 |
| 7 | M33 | Storage, file formats and the lakehouse | | 14 |
| 7 | M34 | Spark and distributed processing | `A` | 14 |
| 7 | M35 | Docker | `A` | 8 |
| 7 | M36 | Kubernetes | `B` | 10 |
| 7 | M37 | Cloud and infrastructure as code | `A`+`B` | 12 |
| 7 | M38 | Operations, observability, security and cost | | 14 |
| 8 | M39 | System design and distributed systems | | 16 |
| 9 | M40 | Capstone - build and defend a data platform | | 6 |
| | | **Tổng** | | **422** |

**422 bài · 40 module · 844 giờ lớp + 1.013 giờ tự học = ~1.857 giờ.**
Ở 15 giờ/tuần là ~27 tháng; ở 12 giờ/tuần là ~34 tháng.

## Cảnh báo về con số

Bản nguồn ước lượng 18–30 tháng. 422 bài ở nhịp 12 giờ/tuần vượt lên ~35 tháng,
tức ra ngoài khoảng đó. Hai cách kéo về trong khoảng:

- Hạ mức các CSDL `B` từ 8 bài xuống 5 bài mỗi hệ (M12–M17): bớt 18 bài.
- Hạ Kestra từ 5 bài xuống 3, Prefect và Dagster từ 8 xuống 6: bớt 6 bài.
- Bỏ M25 Kestra thành một bài trong M26: bớt 4 bài.

Ba cách trên cộng lại còn ~390 bài, ~31 tháng ở 12 giờ/tuần.

## Ba nhóm có cấu trúc nền → công cụ → so sánh

| Nhóm | Module nền | Module công cụ | Module so sánh |
|---|---|---|---|
| Cơ sở dữ liệu | M9 · M10 | M11–M17 (7 hệ) | M18 |
| Điều phối | M21 | M22–M24 (3 công cụ, cùng độ sâu) | M25 |
| Message queue | M27 | M28 · M29 | M30 |

## Chênh so với DE hiện tại (102 bài / 13 module)

| Mảng | Hiện tại | Bản 2 |
|---|---|---|
| Bảy hệ CSDL | 14 bài gộp, không tách hệ | 61 bài, mỗi hệ một module |
| Máy tính / OS / network / concurrency | 6 bài chung module với Git | 56 bài, M2–M6 |
| Vòng đời query và vận hành DB | không có | 14 bài, M10 |
| Orchestration | 8 bài, chỉ Airflow | 44 bài, 4 công cụ + nền + so sánh |
| Message queue | 8 bài, chỉ Kafka | 40 bài, RabbitMQ + Kafka + CDC + stream |
| System design, distributed systems | không có | 16 bài, M39 |

---

# Khối điều phối — danh sách bài (M21–M25, 48 bài)

Ba công cụ cùng mức `A`, cùng 12 bài, cùng dựng một pipeline tham chiếu để
module so sánh có cùng một bài toán mà đối chiếu.

## M21 · Orchestration foundations — 6 bài
| # | Bài | Dạng |
|---|---|---|
| 1 | Why an orchestrator exists - cron and the failures it cannot handle | `LT` |
| 2 | DAG, task dependency and the state machine of a run | `LT` |
| 3 | Logical date against wall-clock date; schedule against event trigger | `LT` |
| 4 | Idempotency, retries, timeouts and what may be retried safely | `LT` |
| 5 | Backfill, catchup and concurrency limits | `TH` |
| 6 | What an orchestrator is not - processing engine and message broker | `LT` |

## M22 · Apache Airflow `A` — 12 bài
| # | Bài | Dạng |
|---|---|---|
| 1 | Architecture - scheduler, metadata database, executor, worker | `LT` |
| 2 | DAG parsing, the top-level code trap and import time | `TH` |
| 3 | Task lifecycle and state transitions in the metadata database | `TH` |
| 4 | Operators, hooks and connections | `TH` |
| 5 | XCom, its size limit, and why data does not travel through it | `TH` |
| 6 | Sensors - poke against reschedule - and deferrable tasks | `TH` |
| 7 | Dynamic task mapping | `TH` |
| 8 | Retries, timeouts, SLA and alerting | `TH` |
| 9 | Backfill and catchup at scale | `TH` |
| 10 | Pools, priority weight and concurrency at three levels | `TH` |
| 11 | Executors - Local, Celery, Kubernetes - and choosing between them | `TH` |
| 12 | Operating Airflow - deployment, upgrade, diagnosing a stuck scheduler | `TH` |

## M23 · Dagster `A` — 12 bài
| # | Bài | Dạng |
|---|---|---|
| 1 | The asset as the unit of modelling, against the task | `LT` |
| 2 | Software-defined assets and the asset graph | `TH` |
| 3 | Ops, jobs and graphs - when you still need them | `TH` |
| 4 | Partitions - time, static and multi-dimensional | `TH` |
| 5 | Schedules and sensors | `TH` |
| 6 | Resources, configuration and separating IO from logic | `TH` |
| 7 | IO managers and where the data actually lands | `TH` |
| 8 | Asset checks - data quality inside the graph | `TH` |
| 9 | Backfilling partitions and selective materialization | `TH` |
| 10 | Lineage, the asset catalog and observability | `TH` |
| 11 | dbt integration - one graph instead of two | `TH` |
| 12 | Operating Dagster - daemon, code locations, deployment | `TH` |

## M24 · Prefect `A` — 12 bài
| # | Bài | Dạng |
|---|---|---|
| 1 | Flows and tasks as plain Python functions | `LT` |
| 2 | State as a first-class object, and handling it | `TH` |
| 3 | Deployments - separating the flow from where it runs | `TH` |
| 4 | Work pools, workers and infrastructure configuration | `TH` |
| 5 | Schedules, event triggers and automations | `TH` |
| 6 | Retries, caching and result persistence | `TH` |
| 7 | Subflows, task runners and concurrency | `TH` |
| 8 | Blocks, variables and secret management | `TH` |
| 9 | Artifacts, logging and observability | `TH` |
| 10 | Failure handling, notifications and crash hooks | `TH` |
| 11 | Dynamic workflows and mapping | `TH` |
| 12 | Operating Prefect - self-hosted server against Cloud | `TH` |

## M25 · Choosing an orchestrator — 6 bài
| # | Bài | Dạng |
|---|---|---|
| 1 | Nine dimensions, and how to score each from lab evidence | `LT` |
| 2 | Modelling power - task graph against asset graph on one pipeline | `TH` |
| 3 | Backfill, replay and recovery compared under the same induced failure | `TH` |
| 4 | Operational cost - infrastructure, upgrade path and on-call load | `TH` |
| 5 | Kestra `C` - YAML-declared flows, and when a team wants no Python | `LT` |
| 6 | The decision - defend one choice for a team with given constraints | `KT` |

**Pipeline tham chiếu chung.** Ba module công cụ dựng lại cùng một pipeline:
nạp từ PostgreSQL và một API có phân trang, ghi vào object store, biến đổi, nạp mart,
có kiểm tra chất lượng. Cùng dữ liệu, cùng lỗi cài sẵn, cùng kịch bản giết tiến trình.
Không cùng bài toán thì M25 không so sánh được, chỉ liệt kê được.
