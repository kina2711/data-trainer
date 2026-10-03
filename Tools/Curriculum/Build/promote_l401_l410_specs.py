#!/usr/bin/env python3
from __future__ import annotations
import re
from promote_l271_l300_common import PHASE9,PHASE10,make_lesson
AI="src.web.aws-iam-best-practices";DS="src.web.docker-build-secrets";OD="src.web.owasp-dependency-check";GS="src.web.github-secret-scanning";GA="src.web.github-artifact-attestations";AT="src.web.aws-timeouts-retries-backoff";GC="src.web.google-sre-capacity-load-testing";GI="src.web.google-sre-incident-management";TF="src.web.terraform-state";KW="src.web.kubernetes-workload-management";AR="src.web.aws-well-architected-reliability";DD="src.book.kleppmann-ddia.1e";RA="src.paper.raft-extended";AC="src.web.aws-budgets"
LABEL={s:("SRC-"+s.removeprefix("src.web.").upper() if s.startswith("src.web.") else "SRC-KLEPPMANN-DDIA-1E" if s==DD else "SRC-RAFT-EXTENDED") for s in (AI,DS,OD,GS,GA,AT,GC,GI,TF,KW,AR,DD,RA,AC)}
SOURCES={GA:("1_Nguon/Web/SRC-GITHUB-ARTIFACT-ATTESTATIONS.md","https://docs.github.com/en/actions/concepts/security/artifact-attestations","GitHub artifact attestations","Official build-provenance, signed-claim, verification and policy-boundary guidance.")}
SPEC={
401:("security.identity-secret-key-lifecycle","principal identity, temporary credential, secret rotation và encryption-key lifecycle",(AI,DS)),
402:("security.secure-delivery-supply-chain","dependency inventory, pinned inputs, isolated build, provenance, attestation và deployment policy",(OD,GS,GA)),
403:("reliability.two-game-days","overload cascade và credential-incident game days với containment và recovery",(AT,GC,GI,AI)),
404:("reliability.gate9-redeploy-recover","Gate 9 redeploy from code, restore state và recover injected incident",(TF,KW,AR,GI)),
405:("system-design.ten-step-process","ten-step design process từ question, requirements và invariants tới failure proof",(DD,AR)),
406:("system-design.quantified-requirements","traffic, data volume, latency, availability, RPO, RTO và cost requirements",(AR,AC,GC)),
407:("system-design.invariants-consistency","business invariants, atomicity scope và client-visible consistency boundaries",(DD,RA)),
408:("system-design.capacity-sheet","capacity assumptions, units, bottlenecks, headroom và sensitivity analysis",(GC,AC)),
409:("system-design.single-stateful-service","single stateful service sequence, durability boundary và recovery path",(DD,AR)),
410:("system-design.replicated-partitioned","replication, partitioning, routing, failover và consistency trade-offs",(DD,RA)),
}
def _directory_and_title(n):
 roots=(PHASE9,PHASE10);ms=[p for r in roots for p in r.glob(f"Module_*/Lesson_{n}-*") if p.is_dir()]
 if len(ms)!=1:raise ValueError(f"L{n}: expected one lesson directory, got {ms}")
 text=(ms[0]/"note.md").read_text();m=(re.search(r'(?m)^tieu_de: "(.+)"$',text) or re.search(rf'(?m)^# Lesson {n}: (.+)$',text) or re.search(rf'(?m)^# Lesson {n} — (.+)$',text))
 if not m:raise ValueError(f"L{n}: cannot recover title")
 return ms[0].name,m.group(1)
def _angles(focus):
 return tuple((h,t) for h,t in (
  ("Mechanism",f"Mô hình {focus} phải nêu actors, identities, state transitions và authority thay vì chỉ liệt kê components."),
  ("Boundary",f"Guarantee của {focus} chỉ đúng trong workload, failure model, time window, trust boundary và version đã khóa."),
  ("Failure mode",f"Phân tích {focus} cần tìm earliest controllable failure, propagation path, blast radius và durable state còn tin cậy."),
  ("Decision rule",f"Quyết định về {focus} phải nối quantified requirements với alternatives, cost, complexity và reversal trigger."),
  ("Evidence",f"Bằng chứng cho {focus} gồm input assumptions, stable identity, resolved design/config, raw observations và independent oracle."),
  ("Recovery lab",f"Lab {focus} phải inject failure hoặc đổi một assumption, phục hồi theo runbook rồi reconcile outcome với invariants."),
 ))
def lessons(start,end):
 out=[]
 for n in range(start,end+1):
  nid,focus,srcs=SPEC[n];directory,title=_directory_and_title(n);out.append(make_lesson(n,directory,title,f"wiki.{nid}",f"Làm thế nào mô hình, kiểm chứng và vận hành {focus} mà không khẳng định vượt quá evidence?",srcs,tuple(LABEL[s] for s in srcs),_angles(focus)))
 return tuple(out)
def queries(start,end):return {n:[f"L{n} boundary nào?",f"L{n} failure probe nào?",f"L{n} evidence nào quyết định?"] for n in range(start,end+1)}
def verification(start,end):return {n:"Run a version-pinned model, sandbox or replayable fixture, change one assumption or inject one failure, retain raw state and event evidence, then reconcile the result against an independent invariant oracle." for n in range(start,end+1)}
def takeaways(start,end):return {n:f"{SPEC[n][1].capitalize()} phải được bảo vệ bằng quantified boundary, counterexample và evidence có thể phản bác." for n in range(start,end+1)}
def source_rows(*ids):return tuple((sid,*SOURCES[sid]) for sid in ids)
