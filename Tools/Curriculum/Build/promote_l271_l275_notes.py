#!/usr/bin/env python3
from promote_l271_l300_common import make_lesson, run_batch

AF="src.web.apache-airflow-dag-runs"; AT="src.web.apache-airflow-tasks"; AR="src.web.aws-timeouts-retries-backoff"; GX="src.web.gx-data-quality-use-cases"
AFL="1_Nguon/Web/SRC-APACHE-AIRFLOW-DAG-RUNS"; ATL="1_Nguon/Web/SRC-APACHE-AIRFLOW-TASKS"; ARL="1_Nguon/Web/SRC-AWS-TIMEOUTS-RETRIES-BACKOFF"; GXL="1_Nguon/Web/SRC-GX-DATA-QUALITY-USE-CASES"

def a(*items): return tuple((x.split("|",1)[0],x.split("|",1)[1]) for x in items)

LESSONS=(
make_lesson(271,"Lesson_271-mastering-one-orchestrator-airflow-or-dagster","Mastering one orchestrator - Airflow or Dagster","wiki.orchestration.master-one-orchestrator","Làm chủ một orchestrator được chứng minh bằng những năng lực vận hành nào thay vì số lượng DAG đã viết?",(AF,AT),(AFL,ATL),a(
"Mastery surface|Làm chủ gồm authoring, scheduling, deployment, observation, recovery và upgrade; biết API happy path mới chỉ là exposure.",
"Execution identity|DAG run, task instance, logical interval, code version và external artifact phải nối thành một run identity có thể truy vết.",
"Local-to-production gap|Local executor không đại diện queue, worker loss, secret backend, remote logging hay scheduler contention của deployment thật.",
"Failure laboratory|Bộ lab phải tiêm parse error, worker death, stuck task, duplicate trigger, missed schedule và partial publish.",
"Operational dossier|Dossier giữ topology, configuration diff, runbook, metrics, logs, recovery transcript và giới hạn đã biết.",
"Choice boundary|Chọn Airflow hay Dagster là quyết định theo workload và operating model; bài này yêu cầu chiều sâu trên một tool, không so brochure.")),
make_lesson(272,"Lesson_272-retry-concurrency-pools-and-the-side-effect-boundary","Retry, concurrency, pools and the side-effect boundary","wiki.orchestration.retry-concurrency-pools-side-effects","Retry, concurrency và pools phải được đặt quanh side-effect boundary thế nào để replay không nhân tác động?",(AT,AR),(ATL,ARL),a(
"Failure classification|Transient, permanent, throttling, invalid input và unknown failure cần action khác nhau; retry mọi exception tạo retry storm.",
"Side-effect boundary|Commit ở API, database, object store hay message broker có thể hoàn tất trước khi task ghi success vào scheduler.",
"Idempotency identity|Replay an toàn cần business operation key, conflict policy và durable ledger chứ không chỉ task instance ID.",
"Concurrency contract|Parallelism phải tôn trọng source quota, destination locks, partition ownership và shared dependency capacity.",
"Pools and fairness|Pool bảo vệ tài nguyên hữu hạn nhưng slot count sai có thể gây starvation, head-of-line blocking hoặc throughput giả.",
"Kill-point proof|Dừng worker trước/sau commit và chạy lại để chứng minh state hội tụ, side effect không nhân và operator nhìn thấy ambiguity.")),
make_lesson(273,"Lesson_273-control-plane-diagnosis-the-required-incident-list","Control-plane diagnosis - the required incident list","wiki.orchestration.control-plane-diagnosis","Danh sách incident tối thiểu nào chứng minh người vận hành chẩn đoán được control plane thay vì chỉ đọc task log?",(AF,AT),(AFL,ATL),a(
"Control versus data plane|Scheduler, parser, metadata DB, queue và workers là control plane; warehouse/API side effects thuộc data plane và có failure độc lập.",
"Required incidents|Phải tái hiện DAG không parse, schedule không tạo run, queued không được nhận, zombie, log mất và state lệch external reality.",
"Boundary evidence|Mỗi incident cần expected transition, component owner, metric/log/query và điểm handoff sang data plane.",
"Diagnosis order|Đi từ run existence tới task state, queue dispatch, worker heartbeat, external execution và publication để tránh đoán mò.",
"False recovery|Clear task hay mark success có thể làm UI xanh nhưng không khôi phục artifact, checkpoint hoặc downstream completeness.",
"Runbook usability|Người trực không viết DAG phải dùng runbook tìm cause class, containment, recovery và escalation trong thời gian hữu hạn.")),
make_lesson(274,"Lesson_274-pipeline-capstone-daily-backfill-and-full-rebuild","Pipeline capstone - daily, backfill and full rebuild","wiki.orchestration.capstone-daily-backfill-rebuild","Một pipeline capstone phải chứng minh daily, backfill và full rebuild cùng hội tụ về một semantic state ra sao?",(AF,AT),(AFL,ATL),a(
"One semantic contract|Daily, backfill và rebuild có execution plan khác nhau nhưng phải chia sẻ grain, identity, transformations và publication invariant.",
"Interval planning|Daily xử lý interval mới; backfill liệt kê intervals lịch sử; rebuild dựng candidate toàn phần với code/source version đã ghi.",
"Isolation and promotion|Backfill/rebuild chạy trong namespace hoặc candidate table riêng, đối soát xong mới promote atomically hay theo staged contract.",
"Resource governance|Historical work phải có pool, concurrency, warehouse budget và pause rule để không làm trễ daily critical path.",
"Reconciliation|So key set, typed hashes, totals và freshness giữa incremental accumulation với independent full computation.",
"Recovery demonstration|Capstone chỉ đạt khi chịu duplicate trigger, late data, task death, partial publish và rollback mà không mất audit trail.")),
make_lesson(275,"Lesson_275-quality-dimensions-defined-operationally","Quality dimensions defined operationally","wiki.data-quality.dimensions-operational","Bảy chiều chất lượng được biến thành phép quan sát có grain, population và nguồn thẩm quyền như thế nào?",(GX,),(GXL,),a(
"Completeness|Đầy đủ phải nói expected population, required fields và denominator; null rate không phát hiện record chưa từng đến.",
"Validity|Hợp lệ kiểm type, format, domain và range đã công bố nhưng một giá trị hợp lệ vẫn có thể sai ngoài đời.",
"Uniqueness|Duy nhất phụ thuộc entity/event identity và scope thời gian; DISTINCT trên một cột không thay business key.",
"Consistency and integrity|Nhất quán so representations; toàn vẹn kiểm quan hệ và state transition, cả hai cần authority và timing rõ.",
"Timeliness|Kịp thời gắn consumer deadline, event/arrival/publish time và late policy thay vì age chung chung.",
"Accuracy boundary|Chính xác cần ground truth hoặc nguồn có thẩm quyền; nếu chỉ có proxy phải ghi proxy và giới hạn nhận thức.")),
)
QUERIES={n:[f"L{n} khái niệm cốt lõi là gì?",f"L{n} failure probe nào bắt buộc?",f"L{n} evidence package cần gì?"] for n in range(271,276)}
VERIFY={n:"Dựng fixture có run/data identity rõ, tiêm một failure tại boundary quan trọng và đối soát state bằng oracle độc lập." for n in range(271,276)}
TAKEAWAYS={271:"Mastery là năng lực vận hành và phục hồi có bằng chứng, không phải số DAG.",272:"Retry chỉ an toàn khi side-effect identity và replay policy bền vững.",273:"Control-plane diagnosis cần chuỗi bằng chứng xuyên scheduler, queue, worker và external state.",274:"Ba execution modes phải hội tụ về cùng semantic state và có promotion boundary.",275:"Quality dimension chỉ hữu ích khi biến thành phép đo có grain, denominator và authority."}
SOURCES=((AT,"1_Nguon/Web/SRC-APACHE-AIRFLOW-TASKS.md","https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html","Apache Airflow Tasks","Task instances, states, timeouts, heartbeat failures and retry behavior."),(GX,"1_Nguon/Web/SRC-GX-DATA-QUALITY-USE-CASES.md","https://docs.greatexpectations.io/docs/reference/learn/data_quality_use_cases/dq_use_cases_lp/","Great Expectations data quality use cases","Official quality-use-case taxonomy including freshness, integrity, missingness, schema, uniqueness and volume."))
if __name__=="__main__": raise SystemExit(run_batch(lessons=LESSONS,queries=QUERIES,verification=VERIFY,takeaways=TAKEAWAYS,sources=SOURCES,version="1.0.54",timestamp="2026-10-02T23:59:54+07:00"))
