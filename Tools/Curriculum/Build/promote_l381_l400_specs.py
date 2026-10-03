#!/usr/bin/env python3
from __future__ import annotations
import re
from promote_l271_l300_common import PHASE9, make_lesson

KD="src.web.kubernetes-deployments"; KP="src.web.kubernetes-container-probes"; KS="src.web.kubernetes-services"; KW="src.web.kubernetes-workload-management"; KX="src.web.kubernetes-disruptions"
OT="src.web.opentelemetry-signals"; OC="src.web.opentelemetry-collector"; PH="src.web.prometheus-histograms"; GM="src.web.google-sre-monitoring"; GE="src.web.google-sre-error-budget-policy"; GC="src.web.google-sre-capacity-load-testing"; AT="src.web.aws-timeouts-retries-backoff"; GI="src.web.google-sre-incident-management"; OW="src.web.owasp-threat-modeling"
LABEL={s:"SRC-"+s.removeprefix("src.web.").upper() for s in (KD,KP,KS,KW,KX,OT,OC,PH,GM,GE,GC,AT,GI,OW)}
SOURCES={
KS:("1_Nguon/Web/SRC-KUBERNETES-SERVICES.md","https://kubernetes.io/docs/concepts/services-networking/service/","Kubernetes Services","Official Service, selector, EndpointSlice and service-discovery behavior."),
KW:("1_Nguon/Web/SRC-KUBERNETES-WORKLOAD-MANAGEMENT.md","https://kubernetes.io/docs/concepts/workloads/controllers/","Kubernetes workload management","Official declarative workload objects, controllers, Deployments and StatefulSet behavior."),
KX:("1_Nguon/Web/SRC-KUBERNETES-DISRUPTIONS.md","https://kubernetes.io/docs/concepts/workloads/pods/disruptions/","Kubernetes disruptions","Official voluntary/involuntary disruption, eviction, drain and PodDisruptionBudget behavior."),
OC:("1_Nguon/Web/SRC-OPENTELEMETRY-COLLECTOR.md","https://opentelemetry.io/docs/collector/","OpenTelemetry Collector","Official receiver, processor, exporter and deployment concepts for telemetry pipelines."),
OW:("1_Nguon/Web/SRC-OWASP-THREAT-MODELING.md","https://owasp.org/www-community/Threat_Modeling","OWASP threat modeling","OWASP guidance for system models, assets, trust boundaries, threats and mitigations."),
}
SPEC={
381:("kubernetes.orchestration-fit","orchestration value và trường hợp simple deployment tốt hơn",(KW,KD)),
382:("kubernetes.object-controller-trace","object, API server, desired state, controller reconciliation và Pod result",(KW,KD)),
383:("kubernetes.pods-probes-resources","Pod lifecycle, probes, resource requests và limits",(KP,KW)),
384:("kubernetes.service-endpoint-policy","Service, EndpointSlice, DNS và network-policy boundary",(KS,)),
385:("kubernetes.config-stateful","ConfigMap, Secret, volume identity và stateful workload",(KW,)),
386:("kubernetes.rollout-disruption","rollout, rollback, node drain và disruption budget",(KD,KX)),
387:("kubernetes.broken-workload-diagnosis","evidence-led diagnosis cho mười broken workloads",(KD,KP,KS,KX)),
388:("kubernetes.rebuild-from-code-backup","cluster và service rebuild từ code, state inventory và backup",(KW,KX)),
389:("observability.question-first","observability khác monitoring và instrumentation bắt đầu từ decision question",(OT,GM)),
390:("observability.structured-logs","structured logs, correlation, retention, access và redaction",(OT,GM)),
391:("observability.metrics-cardinality","counter, gauge, histogram, cardinality và percentile trap",(OT,PH)),
392:("observability.traces-context","span identity, context propagation, sampling và queue boundary",(OT,)),
393:("observability.telemetry-pipeline","SDK, resource attributes, collector pipeline và exporter",(OT,OC)),
394:("observability.user-journey-dashboard","dashboard được dẫn từ user journey, failure signals và drill-down",(GM,OT)),
395:("sre.sli-slo-raw-events","SLI numerator, denominator và SLO window từ raw events",(GM,GE)),
396:("sre.error-budget-burn-rate","error budget, multi-window burn rate và release decision",(GE,GM)),
397:("sre.failure-blast-radius","failure-mode analysis, dependency map và blast radius",(GC,GI)),
398:("sre.overload-control","timeout budget, retry jitter, circuit breaker và load shedding",(AT,GC)),
399:("sre.disaster-recovery","RPO, RTO, dependency ordering và clean-environment restore",(GI,GC)),
400:("security.threat-model","asset, actor, entry point, trust boundary, abuse case và mitigation",(OW,)),
}
def _directory_and_title(n):
    ms=[p for p in PHASE9.glob(f"Module_*/Lesson_{n}-*") if p.is_dir()]
    if len(ms)!=1: raise ValueError(f"L{n}: expected one lesson directory, got {ms}")
    text=(ms[0]/"note.md").read_text(); m=(re.search(r'(?m)^tieu_de: "(.+)"$',text) or re.search(rf'(?m)^# Lesson {n}: (.+)$',text) or re.search(rf'(?m)^# Lesson {n} — (.+)$',text))
    if not m: raise ValueError(f"L{n}: cannot recover title")
    return ms[0].name,m.group(1)
def _angles(focus):
    return tuple((h,t) for h,t in (
      ("Mechanism",f"Mô hình {focus} phải chỉ rõ actors, identities, state transitions và control loop thay vì dừng ở tên object hay tool."),
      ("Boundary",f"Guarantee của {focus} chỉ đúng trong scope, time window, failure domain, permissions và version đã khóa."),
      ("Failure mode",f"Phân tích {focus} cần tìm earliest observable failure, propagation path, blast radius và state còn đáng tin."),
      ("Decision rule",f"Quyết định về {focus} phải nối user impact và constraints với alternatives, trade-offs và reversal trigger."),
      ("Evidence",f"Bằng chứng cho {focus} gồm stable identity, resolved configuration, telemetry thô, state trước–sau và independent oracle."),
      ("Recovery lab",f"Lab {focus} phải inject failure hoặc changed assumption, phục hồi theo runbook rồi reconcile outcome với invariant."),
    ))
def lessons(start,end):
    out=[]
    for n in range(start,end+1):
        nid,focus,srcs=SPEC[n]; directory,title=_directory_and_title(n)
        out.append(make_lesson(n,directory,title,f"wiki.{nid}",f"Làm thế nào mô hình, kiểm chứng và vận hành {focus} mà không khẳng định vượt quá evidence?",srcs,tuple(LABEL[s] for s in srcs),_angles(focus)))
    return tuple(out)
def queries(start,end): return {n:[f"L{n} boundary nào?",f"L{n} failure probe nào?",f"L{n} evidence nào quyết định?"] for n in range(start,end+1)}
def verification(start,end): return {n:"Run a version-pinned sandbox or replayable fixture, inject one declared failure or changed constraint, retain raw object and telemetry evidence, then reconcile final state against an independent oracle." for n in range(start,end+1)}
def takeaways(start,end): return {n:f"{SPEC[n][1].capitalize()} phải được bảo vệ bằng boundary, counterexample và evidence có thể phản bác." for n in range(start,end+1)}
def source_rows(*ids): return tuple((sid,*SOURCES[sid]) for sid in ids)
