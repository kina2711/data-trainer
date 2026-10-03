# AE — tách khối điều phối thành module riêng

Hiện tại: 12 module · 90 bài. M10 gộp 12 bài, trong đó 6 bài điều phối (L71–76)
và 6 bài CI/vận hành (L77–82).

Sau khi tách: **17 module · 112 bài**. Khối điều phối từ 6 lên 28 bài.

| Module | Tên | Mức | Bài | Ghi chú |
|---|---|---|---:|---|
| M1–M9 | giữ nguyên | | 70 | lesson 1–70 |
| M10 | Orchestration foundations | | 4 | mới |
| M11 | Apache Airflow for a transformation layer | `A` | 8 | mới |
| M12 | Dagster for a transformation layer | `A` | 6 | mới |
| M13 | Prefect for a transformation layer | `A` | 6 | mới |
| M14 | Choosing an orchestrator | | 4 | mới |
| M15 | CI/CD, release and operations | | 6 | tách ra từ M10 cũ |
| M16 | Lineage, Governance and Cost | | 5 | M11 cũ |
| M17 | Capstone Project | | 3 | M12 cũ |
| | **Tổng** | | **112** | |

112 bài × 2 giờ lớp = 224 giờ · cộng 246 giờ tự học = **~470 giờ**.
Ở 3 bài/tuần là ~9 tháng; ở 2 bài/tuần là ~13 tháng.

## Góc nhìn khác DE, không chép lại

DE dạy ba công cụ ở góc vận hành nền tảng: chẩn đoán scheduler đứng, chọn executor,
worker chết. AE dạy cùng ba công cụ ở góc **điều phối một dự án dbt cho tin được**.
Cùng tên công cụ, khác bài. Không có bài nào trùng tiêu đề giữa hai chương trình.

## M10 · Orchestration foundations — 4 bài
| # | Bài | Dạng |
|---|---|---|
| 1 | Why `dbt build` on cron stops working - failures cron cannot express | `LT` |
| 2 | DAG, task dependency and the state machine of a run | `LT` |
| 3 | Logical date, schedule against event trigger, and what dbt needs from each | `LT` |
| 4 | Idempotency, retries and safe re-runs for a transformation layer | `TH` |

## M11 · Apache Airflow `A` — 8 bài
| # | Bài | Dạng |
|---|---|---|
| 1 | Architecture - scheduler, metadata database, executor, worker | `LT` |
| 2 | A first DAG that runs dbt, and the top-level code trap | `TH` |
| 3 | Task lifecycle, logs, and tracing a failed model back to its task | `TH` |
| 4 | Connections and hooks - keeping warehouse credentials out of the DAG | `TH` |
| 5 | One task per model against one task for the whole project | `TH` |
| 6 | Retries, timeouts, SLA and alerting for a transformation run | `TH` |
| 7 | Backfill and catchup over a 30-day window | `TH` |
| 8 | Pools and concurrency - not melting the warehouse | `TH` |

## M12 · Dagster `A` — 6 bài
| # | Bài | Dạng |
|---|---|---|
| 1 | The asset as the unit of modelling, and why it matches `ref()` | `LT` |
| 2 | Loading a dbt project as an asset graph | `TH` |
| 3 | Partitions - materializing one day without rebuilding the graph | `TH` |
| 4 | Asset checks against dbt tests - overlap and division of work | `TH` |
| 5 | Schedules, sensors and freshness policies | `TH` |
| 6 | Lineage and the asset catalog as a self-service surface | `TH` |

## M13 · Prefect `A` — 6 bài
| # | Bài | Dạng |
|---|---|---|
| 1 | Flows and tasks as plain Python; state as a return value | `LT` |
| 2 | Wrapping a dbt run in a flow with typed failure handling | `TH` |
| 3 | Deployments and work pools - separating the flow from where it runs | `TH` |
| 4 | Schedules, event triggers and automations | `TH` |
| 5 | Blocks, variables and secrets for warehouse credentials | `TH` |
| 6 | Artifacts, logging and run observability | `TH` |

## M14 · Choosing an orchestrator — 4 bài
| # | Bài | Dạng |
|---|---|---|
| 1 | Nine dimensions, scored from lab evidence only | `LT` |
| 2 | The same dbt project in three tools - what each one made cheap | `TH` |
| 3 | Kestra `C` and the case for YAML-declared flows | `LT` |
| 4 | The decision - defend one choice for a team with given constraints | `KT` |

**Dự án tham chiếu chung.** M11, M12, M13 điều phối cùng một dự án dbt: cùng số mô hình,
cùng nguồn, cùng lỗi cài sẵn ở một mô hình giữa đồ thị, cùng yêu cầu chạy bù 30 ngày.
Không cùng dự án thì M14 không đo được gì.
