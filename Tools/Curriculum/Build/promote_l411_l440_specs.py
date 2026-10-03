#!/usr/bin/env python3
from __future__ import annotations
import re
from promote_l271_l300_common import PHASE10,make_lesson
DD="src.book.kleppmann-ddia.1e";RA="src.paper.raft-extended";AR="src.web.aws-well-architected-reliability";AC="src.web.aws-budgets";GM="src.web.google-sre-monitoring";GC="src.web.google-sre-capacity-load-testing";MA="src.web.madr-templates";PP="src.book.hunt-thomas-pragmatic-programmer.20ae"
OF="src.web.openai-function-calling";OR="src.web.openai-retrieval";OE="src.web.openai-evals";OP="src.web.openai-prompt-injection";NG="src.web.nist-generative-ai-profile"
LABEL={s:("SRC-"+s.removeprefix("src.web.").upper() if s.startswith("src.web.") else "SRC-KLEPPMANN-DDIA-1E" if s==DD else "SRC-RAFT-EXTENDED" if s==RA else "SRC-HUNT-THOMAS-PRAGMATIC-PROGRAMMER-20AE") for s in (DD,RA,AR,AC,GM,GC,MA,PP,OF,OR,OE,OP,NG)}
SOURCES={
OF:("1_Nguon/Web/SRC-OPENAI-FUNCTION-CALLING.md","https://developers.openai.com/api/docs/guides/function-calling","OpenAI function calling guide","Official tool definitions, structured arguments, strict schemas and application execution boundaries."),
OR:("1_Nguon/Web/SRC-OPENAI-RETRIEVAL.md","https://developers.openai.com/api/docs/guides/retrieval","OpenAI retrieval guide","Official vector-store, search, filtering and retrieval integration guidance."),
OE:("1_Nguon/Web/SRC-OPENAI-EVALS.md","https://platform.openai.com/docs/guides/evals","OpenAI evaluation guide","Official dataset, grader, run and iterative evaluation workflow guidance."),
OP:("1_Nguon/Web/SRC-OPENAI-PROMPT-INJECTION.md","https://openai.com/index/designing-agents-to-resist-prompt-injection/","OpenAI prompt-injection resistance","Official source-sink framing, constrained impact and layered agent-security guidance."),
NG:("1_Nguon/Papers/SRC-NIST-GENERATIVE-AI-PROFILE.md","https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf","NIST Generative AI Profile","Official cross-sector GenAI risk profile and govern-map-measure-manage actions."),
}
SPEC={
411:("system-design.async-workflow","asynchronous workflow, durable command, retry, dedup và compensation",(DD,AR)),
412:("system-design.analytics-platform","analytical platform từ ingest, storage, transform tới serving và governance",(DD,GC)),
413:("system-design.multi-tenant","multi-tenant identity, isolation, quota, noisy-neighbor và cost allocation",(DD,AC)),
414:("system-design.failure-table","failure table và remove-component test trên dependencies",(AR,GC)),
415:("system-design.cost-model","cost model, unit economics, demand curve và sensitivity",(AC,GC)),
416:("system-design.alternatives-reversibility","alternatives, explicit trade-offs, reversibility và option value",(MA,PP)),
417:("system-design.migration-cutover","dual run, shadow comparison, cutover, rollback và convergence",(DD,AR)),
418:("system-design.review-three-pass","design review qua scope, correctness và operability passes",(MA,PP)),
419:("system-design.changed-constraint","changed-constraint defence và reversal triggers",(MA,GC)),
420:("system-design.capstone-dossier","capstone dossier nối RFC, spike evidence và ADRs",(MA,PP)),
421:("ai.boundary","bounded AI-engineering scope, excluded claims và human authority",(NG,)),
422:("ai.assisted-engineering","AI-assisted engineering với tests, review, provenance và abstention",(NG,OE)),
423:("ai.api-contract","LLM API contract gồm structured output, tools, budgets, retries và version lineage",(OF,NG)),
424:("ai.retrieval-pipeline","chunking, embedding, metadata filters, retrieval và rerank",(OR,NG)),
425:("ai.grounding-citation-abstention","grounding, claim citation, coverage và abstention",(OR,NG)),
426:("ai.evaluation-five-layers","evaluation blueprint qua retrieval, generation, grounding, safety và operations",(OE,NG)),
427:("ai.baseline-first","baseline-first comparison giữa simple search và retrieval augmentation",(OR,OE)),
428:("ai.prompt-injection-isolation","prompt injection, tool permission, source-sink path và tenant isolation",(OP,NG)),
429:("ai.serving-lineage","serving latency, token cost, fallback, caching và model-version lineage",(OF,OE)),
430:("ai.grounded-assistant-red-team","grounded assistant project với eval corpus và red-team suite",(OR,OE,OP,NG)),
431:("staff.competency-evidence","competency ladder và evidence boundary cho Staff/Principal progression",(PP,)),
432:("staff.problem-framing","one-page problem framing từ decision, users, constraints và success measures",(PP,MA)),
433:("staff.rfc-options","RFC với ba options thực, disconfirming evidence và recommendation",(MA,PP)),
434:("staff.adr-irreversible","ADR cho lựa chọn khó đảo, consequences và revisit signals",(MA,)),
435:("staff.migration-playbook","migration playbook với consumer inventory, waves, rollback và closure",(DD,MA)),
436:("staff.platform-product","platform as product qua paved road, guardrails, adoption và escape hatch",(PP,GM)),
437:("staff.strategy-memo","strategy memo gồm diagnosis, bets, sequence và revisit signals",(PP,MA)),
438:("staff.influence-bottleneck","influence, review quality và bottleneck anti-pattern",(PP,)),
439:("staff.evidence-dossier","evidence dossier nối baseline, decision, outcome, limitations và attribution",(PP,MA)),
440:("staff.graduation-defence","graduation defence cho một design trước executive, peer và operator audiences",(PP,MA)),
}
def _directory_and_title(n):
 ms=[p for p in PHASE10.glob(f"Module_*/Lesson_{n}-*") if p.is_dir()]
 if len(ms)!=1:raise ValueError(f"L{n}: expected one lesson directory, got {ms}")
 text=(ms[0]/"note.md").read_text();m=(re.search(r'(?m)^tieu_de: "(.+)"$',text) or re.search(rf'(?m)^# Lesson {n}: (.+)$',text) or re.search(rf'(?m)^# Lesson {n} — (.+)$',text))
 if not m:raise ValueError(f"L{n}: cannot recover title")
 return ms[0].name,m.group(1)
def _angles(focus):
 return tuple((h,t) for h,t in (
  ("Mechanism",f"Mô hình {focus} phải nêu actors, identities, state transitions và decision authority thay vì liệt kê công cụ."),
  ("Boundary",f"Kết luận về {focus} chỉ đúng trong audience, workload, trust boundary, time window và version đã khóa."),
  ("Failure mode",f"Phân tích {focus} cần tìm earliest failure, propagation path, blast radius và state hoặc claim còn đáng tin."),
  ("Decision rule",f"Quyết định về {focus} phải nối quantified constraints với alternatives, trade-offs và reversal trigger."),
  ("Evidence",f"Bằng chứng cho {focus} gồm inputs có version, stable identity, raw observations, reviewer-visible limitations và independent oracle."),
  ("Transfer test",f"Bài thực hành {focus} phải đổi một constraint hoặc inject counterexample rồi bảo vệ hoặc đảo quyết định bằng evidence."),
 ))
def lessons(start,end):
 out=[]
 for n in range(start,end+1):
  nid,focus,srcs=SPEC[n];directory,title=_directory_and_title(n);out.append(make_lesson(n,directory,title,f"wiki.{nid}",f"Làm thế nào thiết kế, kiểm chứng và bảo vệ {focus} mà không khẳng định vượt quá evidence?",srcs,tuple(LABEL[s] for s in srcs),_angles(focus)))
 return tuple(out)
def queries(start,end):return {n:[f"L{n} decision boundary nào?",f"L{n} counterexample nào?",f"L{n} evidence nào quyết định?"] for n in range(start,end+1)}
def verification(start,end):return {n:"Run a version-pinned model, evaluation corpus or review simulation, change one material constraint, retain raw evidence and reconcile the recommendation against an independent rubric or invariant oracle." for n in range(start,end+1)}
def takeaways(start,end):return {n:f"{SPEC[n][1].capitalize()} phải được bảo vệ bằng explicit boundary, changed-constraint test và evidence có thể phản bác." for n in range(start,end+1)}
def source_rows(*ids):return tuple((sid,*SOURCES[sid]) for sid in ids)
