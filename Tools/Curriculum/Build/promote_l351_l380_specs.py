#!/usr/bin/env python3
from __future__ import annotations
import re
from promote_l271_l300_common import PHASE8, PHASE9, make_lesson

SP="src.web.apache-spark-rdd-guide"; SQ="src.web.apache-spark-sql-performance"; ST="src.web.apache-spark-tuning"
SS="src.web.apache-spark-structured-streaming"; AR="src.web.aws-well-architected-reliability"; AI="src.web.aws-iam-best-practices"; AV="src.web.aws-vpc-route-tables"; AC="src.web.aws-budgets"
DO="src.web.docker-overview"; DI="src.web.docker-image-layers"; DM="src.web.docker-multi-stage"; DV="src.web.docker-volumes"; DS="src.web.docker-build-secrets"
TF="src.web.terraform-state"; TM="src.web.terraform-modules"
LABEL={x:x.replace("src.web.","SRC-").upper().replace("-","-") for x in (SP,SQ,ST,SS,AR,AI,AV,AC,DO,DI,DM,DV,DS,TF,TM)}

SOURCES={
SS:("1_Nguon/Web/SRC-APACHE-SPARK-STRUCTURED-STREAMING.md","https://spark.apache.org/docs/latest/streaming/getting-started.html","Apache Spark Structured Streaming programming guide","Official programming model, offsets, checkpoints, state, watermarks and fault-tolerance semantics."),
AR:("1_Nguon/Web/SRC-AWS-WELL-ARCHITECTED-RELIABILITY.md","https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/shared-responsibility-model-for-resiliency.html","AWS Well-Architected Reliability Pillar","Official failure-domain, shared-responsibility, multi-zone and recovery guidance."),
AI:("1_Nguon/Web/SRC-AWS-IAM-BEST-PRACTICES.md","https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html","AWS IAM security best practices","Official guidance for principals, roles, temporary credentials, least privilege and access review."),
AV:("1_Nguon/Web/SRC-AWS-VPC-ROUTE-TABLES.md","https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html","Amazon VPC route tables","Official route-table and traffic-path behavior for VPC networks."),
AC:("1_Nguon/Web/SRC-AWS-BUDGETS.md","https://docs.aws.amazon.com/cost-management/latest/userguide/bcm-lite-use-budget.html","AWS Budgets guidance","Official budget types, actual and forecast alerts, notification limits and reporting latency."),
DO:("1_Nguon/Web/SRC-DOCKER-OVERVIEW.md","https://docs.docker.com/get-started/docker-overview","Docker overview","Official container, image, runtime and writable-layer concepts."),
DI:("1_Nguon/Web/SRC-DOCKER-IMAGE-LAYERS.md","https://docs.docker.com/get-started/docker-concepts/building-images/understanding-image-layers/","Docker image layers","Official immutable-layer, content-addressing and union-filesystem concepts."),
DM:("1_Nguon/Web/SRC-DOCKER-MULTI-STAGE.md","https://docs.docker.com/build/building/multi-stage/","Docker multi-stage builds","Official build-stage, artifact-copy and final-image minimization behavior."),
DV:("1_Nguon/Web/SRC-DOCKER-VOLUMES.md","https://docs.docker.com/engine/storage/volumes/","Docker volumes","Official volume lifecycle, mounts and persistence semantics."),
DS:("1_Nguon/Web/SRC-DOCKER-BUILD-SECRETS.md","https://docs.docker.com/build/building/secrets/","Docker build secrets","Official secret and SSH mount mechanisms for builds without baking credentials into images."),
TF:("1_Nguon/Web/SRC-TERRAFORM-STATE.md","https://developer.hashicorp.com/terraform/language/state","Terraform state","Official state mapping, storage, inspection, locking and collaboration guidance."),
TM:("1_Nguon/Web/SRC-TERRAFORM-MODULES.md","https://developer.hashicorp.com/terraform/language/modules","Terraform modules","Official root/child module hierarchy and reusable configuration concepts."),
}

# number -> (note-id suffix, focus, source ids)
SPEC={
351:("spark.skew-straggler-decision","partition skew, straggler diagnosis và quyết định salt-or-broadcast",(SQ,ST)),
352:("spark.mimd-spmd","MIMD, SPMD và cách distributed engine map program lên tasks",(SP,ST)),
353:("spark.nested-parallelism","nested parallelism, executor cores và oversubscription",(SP,ST)),
354:("spark.strong-scaling","strong-scaling curve và điểm scale-out chuyển thành âm",(SP,ST)),
355:("spark.tuning-decision-tree","decision tree chẩn đoán ba workload chưa biết",(SQ,ST)),
356:("spark.streaming-checkpoint-state","micro-batch offsets, checkpoint và state recovery",(SS,)),
357:("spark.event-time-watermark","event time, watermark, late data và state eviction",(SS,)),
358:("compute.engine-class-selection","lựa chọn distributed, embedded, vectorized và in-process engine",(SP,SQ)),
359:("streaming.end-to-end-guarantee","end-to-end guarantee qua replayable source, restored state và sink",(SS,)),
360:("streaming.gate8-recovery-defense","Gate 8 defense cho delivery semantic và stateful recovery",(SS,)),
361:("cloud.failure-domains-shared-responsibility","region, zone, failure domain và shared responsibility",(AR,)),
362:("cloud.identity-least-privilege","principal, role, temporary credential và least privilege",(AI,)),
363:("cloud.network-boundaries","CIDR, route, trust boundary, egress và DNS",(AV,)),
364:("cloud.compute-replacement","compute state, startup, scale unit và replacement",(AR,)),
365:("cloud.storage-data-contract","storage và managed database được chọn từ data contract",(AR,)),
366:("cloud.messaging-semantics","messaging primitives được map bằng delivery và ordering semantics",(AR,)),
367:("cloud.rpo-rto-restore","failure domains, RPO, RTO và tested restore",(AR,)),
368:("cloud.cost-unit-economics","unit economics, egress, allocation và budget alarm",(AC,)),
369:("cloud.secrets-keys-audit","secrets, encryption keys, rotation và audit trail",(AI,)),
370:("cloud.primitive-portability","primitive table ánh xạ compute, network, identity, storage và messaging giữa clouds",(AR,AI,AV)),
371:("cloud.landing-zone-project","landing zone nhỏ cho một cloud và một data service",(AR,AI,AV,AC)),
372:("cloud.failure-drill","failure drill loại một zone, service và credential",(AR,AI)),
373:("container.isolated-process","container như isolated process dùng chung host kernel",(DO,)),
374:("container.images-layers-digests","image layers, immutable digest và multi-stage build",(DI,DM)),
375:("container.pid1-signals","PID 1, signal propagation và graceful shutdown",(DO,)),
376:("container.network-volume-uid","container networking, volume lifecycle và UID mismatch",(DO,DV)),
377:("container.supply-chain","minimal base, pinned digest và secret-free image layers",(DI,DM,DS)),
378:("iac.desired-state-graph","IaC desired state, resource identity và dependency graph",(TF,TM)),
379:("iac.state-lock-drift-recovery","state locking, drift và evidence-led recovery",(TF,)),
380:("iac.modules-environments-plan","module boundaries, environments và saved-plan review",(TM,TF)),
}

def _directory_and_title(number:int):
    roots=(PHASE8,PHASE9)
    matches=[p for root in roots for p in root.glob(f"Module_*/Lesson_{number}-*") if p.is_dir()]
    if len(matches)!=1: raise ValueError(f"L{number}: expected one lesson directory, got {matches}")
    text=(matches[0]/"note.md").read_text()
    match=(re.search(r'(?m)^tieu_de: "(.+)"$',text)
           or re.search(rf'(?m)^# Lesson {number}: (.+)$',text)
           or re.search(rf'(?m)^# Lesson {number} — (.+)$',text))
    if not match: raise ValueError(f"L{number}: cannot recover title")
    title=match.group(1)
    return matches[0].name,title

def _angles(focus:str):
    return tuple((h,t) for h,t in (
        ("Mechanism",f"Mô hình {focus} phải nêu actor, state, transition và resource thực sự tham gia thay vì chỉ gọi tên tính năng."),
        ("Boundary",f"Guarantee của {focus} chỉ có nghĩa khi khóa scope, identity, time window, failure domain và version."),
        ("Failure mode",f"Phân tích {focus} cần chỉ ra earliest controllable failure, blast radius và trạng thái còn quan sát được sau lỗi."),
        ("Decision rule",f"Quyết định về {focus} phải nối workload constraints với alternatives, trade-offs và điều kiện đảo chiều."),
        ("Evidence",f"Bằng chứng cho {focus} gồm resolved configuration, runtime identity, metrics/logs, state trước–sau và independent oracle."),
        ("Recovery lab",f"Lab {focus} phải inject một failure hoặc changed constraint, phục hồi từ checkpoint hợp lệ rồi reconcile kết quả."),
    ))

def lessons(start:int,end:int):
    out=[]
    for n in range(start,end+1):
        note_id,focus,srcs=SPEC[n]; directory,title=_directory_and_title(n)
        out.append(make_lesson(n,directory,title,f"wiki.{note_id}",f"Làm thế nào mô hình, kiểm chứng và vận hành {focus} mà không khẳng định vượt quá evidence?",srcs,tuple(LABEL[s] for s in srcs),_angles(focus)))
    return tuple(out)

def queries(start:int,end:int): return {n:[f"L{n} boundary nào?",f"L{n} failure probe nào?",f"L{n} evidence nào quyết định?"] for n in range(start,end+1)}
def verification(start:int,end:int): return {n:"Run a version-pinned sandbox fixture, change one declared constraint or inject one failure, retain raw runtime evidence and reconcile the final identities and state against an independent oracle." for n in range(start,end+1)}
def takeaways(start:int,end:int): return {n:f"{SPEC[n][1].capitalize()} phải được bảo vệ bằng boundary, failure probe và evidence có thể phản bác." for n in range(start,end+1)}
def source_rows(*ids): return tuple((sid,*SOURCES[sid]) for sid in ids)
