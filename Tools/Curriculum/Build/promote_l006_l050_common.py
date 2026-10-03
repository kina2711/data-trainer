#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, json, re
from dataclasses import dataclass
from pathlib import Path
from format_knowledge_notes import normalize_markdown
from promote_l006_l050_specs import *

ROOT=Path(__file__).resolve().parents[3]
CURRICULUM=ROOT/"Material/DE/Curriculum"
PACK=ROOT/"Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01"
MANIFEST=ROOT/"Docs/Second-Brain/second-brain-manifest.json"
MODULES={1:"Engineering Thinking, Git and Debugging",2:"Python for Production",3:"Data Structures and Algorithms for Systems",4:"Computer Architecture and the Performance Model"}
WIKI_DIR={1:"Software-Engineering",2:"Python",3:"Algorithms",4:"Computer-Architecture"}
LABEL={
PG:"SRC-CHACON-STRAUB-PRO-GIT-2E",PP:"SRC-HUNT-THOMAS-PRAGMATIC-PROGRAMMER-20AE",SOM:"SRC-SOMMERVILLE-SOFTWARE-ENGINEERING-10E",
SRE_POST:"SRC-GOOGLE-SRE-POSTMORTEM-CULTURE",SRE_INC:"SRC-GOOGLE-SRE-INCIDENT-MANAGEMENT",SRE_MON:"SRC-GOOGLE-SRE-MONITORING",
PY_LANG:"SRC-PYTHON-314-LANGUAGE-REFERENCE",PY_LIB:"SRC-PYTHON-314-STDLIB-RUNTIME",PYPA:"SRC-PYPA-PACKAGING-PROJECTS",GH:"SRC-GITHUB-STATUS-CHECKS",TLPI:"SRC-TLPI-2010",
ALG:"SRC-SEDGEWICK-WAYNE-ALGORITHMS-4E",PET:"SRC-PETROV-DATABASE-INTERNALS-1E",DB:"SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E",
COD:"SRC-PATTERSON-HENNESSY-COD-5E",INTEL:"SRC-INTEL-INTRINSICS-GUIDE",LLVM:"SRC-LLVM-AUTO-VECTORIZATION"}
SOURCE_NEW={
PY_LANG:{"source_id":PY_LANG,"record_path":"1_Nguon/Web/SRC-PYTHON-314-LANGUAGE-REFERENCE.md","canonical_url":"https://docs.python.org/3/reference/","captured":"2026-10-02","rights":"public-official-documentation"},
PY_LIB:{"source_id":PY_LIB,"record_path":"1_Nguon/Web/SRC-PYTHON-314-STDLIB-RUNTIME.md","canonical_url":"https://docs.python.org/3/library/","captured":"2026-10-02","rights":"public-official-documentation"},
PYPA:{"source_id":PYPA,"record_path":"1_Nguon/Web/SRC-PYPA-PACKAGING-PROJECTS.md","canonical_url":"https://packaging.python.org/en/latest/tutorials/packaging-projects/","captured":"2026-10-02","rights":"public-official-documentation"},
ALG:{"source_id":ALG,"record_path":"1_Nguon/Books/SRC-SEDGEWICK-WAYNE-ALGORITHMS-4E.md","canonical_path":str(ROOT/"Material/Reference_temp/Algorithms_Fourth_Edition.pdf"),"sha256":"960d9490a2b977a8f77871d154c8ddb1d4ad7b666341abcd7cb157922af28c5d","captured":"2026-10-02","rights":"copyrighted-private-owner-provided"},
COD:{"source_id":COD,"record_path":"1_Nguon/Books/SRC-PATTERSON-HENNESSY-COD-5E.md","canonical_path":str(ROOT/"Material/DE/Reference/Library/Computer Science/Kiến trúc máy tính - CO2007/Slide bài giảng/CS422-Computer-Architecture-ComputerOrganizationAndDesign5thEdition2014.pdf"),"sha256":"ecef083800324810f2c9fe06b5a8b52f8d4bd4e718583edb7ef5127532e7967d","captured":"2026-10-02","rights":"copyrighted-private-owner-provided"},
}
LOCATOR={
PG:"Chapter 3 PDF 129–174; Chapter 7 PDF 422–434; Chapter 10 PDF 762–790",PP:"Topic 10 PDF 76–83; Topics 23–25 PDF 148–166; Topic 40 PDF 276–280",SOM:"Chapters 4, 7, 8 và 25; PDF 103–132, 169–212, 228–242, 732–756",
SRE_POST:"Postmortem culture; accessed 2026-10-01",SRE_INC:"Incident management; accessed 2026-10-01",SRE_MON:"Monitoring distributed systems; accessed 2026-10-01",
PY_LANG:"Python 3.14.8 Language Reference; accessed 2026-10-02",PY_LIB:"Python 3.14.8 Library Reference; accessed 2026-10-02",PYPA:"PyPA Packaging Projects; accessed 2026-10-02",GH:"GitHub status checks; accessed 2026-10-01",TLPI:"process, thread, IPC và lifecycle scopes trong source record",
ALG:"Sections 1.4, 2.2, 2.4, 3.2–3.4, 4.1–4.2; PDF 185–604",PET:"Chapter 7 PDF 167–210",DB:"Chapter 15 PDF 1902–1955",COD:"Chapter 5 PDF 397–459; Section 6.3 PDF 523–538",INTEL:"Intel Intrinsics Guide; accessed 2026-10-01",LLVM:"LLVM Auto-Vectorization documentation; accessed 2026-10-01"}

@dataclass(frozen=True)
class Lesson:
 number:int;slug:str;focus:str;mechanism:str;boundary:str;failure:str;decision:str;evidence:str;transfer:str;sources:tuple[str,...];directory:str;title:str
 @property
 def module(self):return 1 if self.number<=12 else 2 if self.number<=32 else 3 if self.number<=44 else 4
 @property
 def note_id(self):return f"wiki.de-foundation.{self.slug}"
 @property
 def concept_key(self):return f"ck.de.{self.slug}"
 @property
 def filename(self):return f"{self.number:03d}-{self.slug}.md"
 @property
 def folder(self):
  matches=list(CURRICULUM.glob(f"Phase_*/Module_*/{self.directory}"))
  if len(matches)!=1:raise ValueError(f"L{self.number}: directory mismatch {matches}")
  return matches[0]
 @property
 def wiki(self):return ROOT/"Docs/Second-Brain/2_Wiki"/WIKI_DIR[self.module]/f"{self.title}.md"

def load_lesson(n:int)->Lesson:
 spec=SPECS[n];matches=list(CURRICULUM.glob(f"Phase_*/Module_*/Lesson_{n:03d}-*"))
 if len(matches)!=1:raise ValueError(f"L{n}: expected one folder")
 text=(matches[0]/"note.md").read_text();m=re.search(r'(?m)^tieu_de: "(.+)"$',text) or re.search(rf'(?m)^# Lesson {n}: (.+)$',text)
 if not m:raise ValueError(f"L{n}: title missing")
 return Lesson(n,*spec,matches[0].name,m.group(1))

def contract(l:Lesson):
 text=(l.folder/"note.md").read_text();after=(l.folder/"after-note.md").read_text()
 def f(body,name):
  m=re.search(rf"(?m)^\*\*{re.escape(name)}\.\*\*\s*(.+)$",body);return m.group(1).strip() if m else ""
 legacy=tuple(f(text,x) for x in ("Outcome","Đánh giá","Lab","Pitfalls","Self-study (2,4 giờ)","Done when"))
 if all(legacy):return legacy
 tasks=re.findall(r"(?m)^\*\*Nhiệm vụ\.\*\*\s*(.+)$",after)
 restored=(f(text,"Năng lực cần chứng minh"),f(after,"Cách đánh giá"),tasks[0] if tasks else "",f(after,"Lỗi cần chủ động loại trừ"),tasks[1] if len(tasks)>1 else "",f(text,"Điều kiện hoàn thành"))
 if not all(restored):raise ValueError(f"L{l.number}: contract missing")
 return restored

def frontmatter(l:Lesson):
 src="\n".join(f"  - {s}" for s in l.sources);prev=f"wiki.de-foundation.{SPECS[l.number-1][0]}" if l.number>6 else "wiki.engineering-foundation.git-history-integration";nxt=f"[wiki.de-foundation.{SPECS[l.number+1][0]}]" if l.number<50 else "[]"
 return f'''---
note_id: {l.note_id}
concept_key: {l.concept_key}
concept_key_status: proposed
note_type: concept-deep-dive
status: review
language: vi
created: 2026-10-02
last_verified: 2026-10-02
review_after: 2027-04-02
editorial_pass: humanized-v3
primary_question: Làm thế nào mô hình, kiểm chứng và áp dụng {l.focus}?
source_ids:
{src}
relationships:
  builds_on: [{prev}]
  prerequisite_of: {nxt}
aliases: [{l.title}]
tags: [wiki/{WIKI_DIR[l.module].lower()}, de-foundation, module-{l.module}]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/{l.filename}
---
'''

PIVOTS=("state transition và invariant","identity, ownership và boundary","failure path và recovery","decision trade-off và reversal trigger","evidence package và oracle","changed-constraint transfer")
TESTS=("positive và negative control chỉ khác một điều kiện","boundary case ngay trước và sau ngưỡng","replay cùng identity với state khác","failure inject trước và sau durable transition","changed scale làm cost model đổi","adversarial order hoặc skew","fresh environment không cache","independent oracle không dùng chung implementation","partial progress rồi restart","missing evidence phải abstain","reviewer tái hiện từ package","constraint đổi đủ để quyết định đảo")

def knowledge(l:Lesson):
 angles=(l.mechanism,l.boundary,l.failure,l.decision,l.evidence,l.transfer);parts=[frontmatter(l),f"\n# {l.title}\n\n**Tóm tắt bản chất:** {l.mechanism} Sai boundary ở `{l.focus}` làm kết quả có vẻ đúng trong happy path nhưng không chịu được failure hoặc changed constraint.\n\n> [!abstract] Câu hỏi trung tâm\n> Làm thế nào mô hình, kiểm chứng và áp dụng {l.focus}?\n"]
 heads=("Nỗi Đau & Động Lực","Cơ Chế Tác Động","Bản Đồ Quyết Định",f"Case Study Thực Chiến: {l.title}","Góc Khuất & Ngộ Nhận","Nếu Bạn Dạy Lại Điều Này...")
 for i,(h,a) in enumerate(zip(heads,angles),1):
  parts.append(f"\n## {h}\n\n{a} Với `{l.note_id}`, điểm phải khóa là {PIVOTS[i-1]}; nếu trường nào chưa biết thì ghi unknown và nêu impact-if-wrong thay vì tự điền mặc định.\n\n")
  if i==1:parts.append(f"Không có mô hình này, lỗi thường lộ ở consumer sau cùng: output sai, latency vọt, resource không được giải phóng hoặc lịch sử không còn tái hiện được. Chi phí thật của `{l.title}` vì thế nằm ở thời gian chẩn đoán và phạm vi phục hồi, không nằm ở số dòng syntax.\n")
  elif i==2:parts.append(f"Hãy tách declared state, executed state và published state của `{l.focus}`. Một command thành công chỉ là executed signal; muốn kết luận cần đối soát consumer-visible invariant và trạng thái còn lại sau restart hoặc replay.\n")
  elif i==3:parts.append(f"Quy tắc mặc định cho `{l.title}` là chọn phương án đơn giản nhất qua được hard constraints, rồi ghi rõ điều kiện đảo. Bảng quyết định tối thiểu gồm workload, identity, state owner, time/memory budget, failure domain và khả năng rollback.\n")
  elif i==4:parts.append(f"Case dùng fixture nhỏ nhưng phải giữ cơ chế chi phối. Trước khi chạy, learner viết expected transition; sau khi chạy, họ đối chiếu raw artifact với oracle và giải thích mọi khác biệt thay vì sửa expected cho khớp output.\n")
  elif i==5:parts.append(f"**Hiểu lầm:** Happy path chạy nhanh nghĩa là thiết kế đúng. **Thực tế:** {l.failure} **Vì sao nghe hợp lý:** case nhỏ thường không chạm capacity, concurrency, failure hoặc version boundary.\n\n**Hiểu lầm:** Tool hoặc API tự bảo đảm semantics. **Thực tế:** guarantee chỉ tồn tại trong scope và state đã công bố. **Vì sao nghe hợp lý:** syntax che mất protocol phía dưới.\n")
  else:parts.append(f"Hook dạy lại bắt đầu bằng một dự đoán dễ sai về `{l.focus}`. Bài tập seed đổi đúng một constraint, yêu cầu learner giữ hoặc đảo quyết định và chỉ ra evidence nào đủ mạnh để thuyết phục một reviewer không tham dự buổi học.\n")
 parts.append(f"\n## Ma trận kiểm chứng từng mệnh đề\n\nProtocol riêng của `{l.title}` là: {l.evidence} Mỗi probe nối input boundary với failure signal và oracle có thể bác bỏ kết luận.\n")
 for i,t in enumerate(TESTS,1):
  angle=angles[(i-1)%6]
  parts.append(f"\n### Probe {i}: {PIVOTS[(i-1)%6]}\n\n**Mệnh đề cần kiểm.** {angle}\n\n**Thiết kế phép thử.** Với `{l.note_id}`, tạo {t}; khóa input snapshot, phiên bản, seed, identity và state ban đầu. Viết expected result trước execution để tránh đổi tiêu chí sau khi nhìn output.\n\n**Bằng chứng cần giữ.** Lưu command hoặc harness, raw observation, transition trước–sau, coverage và limitation. Kết luận chỉ đạt khi oracle độc lập khớp ở đúng grain; nếu chưa chạy, phần này vẫn là protocol chứ không phải observation.\n")
 parts.append(f"\n## Tự Kiểm Tra Nhanh\n\n1. Boundary đầu tiên của `{l.focus}` nằm ở đâu?\n\n<details><summary>Đáp án</summary>{l.boundary}</details>\n\n2. Failure nào dễ tạo kết quả xanh giả nhất?\n\n<details><summary>Đáp án</summary>{l.failure}</details>\n\n3. Constraint nào khiến quyết định phải đảo?\n\n<details><summary>Đáp án</summary>{l.transfer}</details>\n")
 parts.append(f"\n## Giới hạn và điều chưa cho phép kết luận\n\n- Lab của `{l.title}` chưa được tuyên bố đã chạy trên production; note mô tả curriculum và expected evidence.\n- Mọi kết luận phụ thuộc version, workload, operating system, interpreter/compiler hoặc hardware phải được kiểm lại trên target.\n- Concept key `{l.concept_key}` đang ở trạng thái `proposed`; note không được tính là canonical registry coverage trước khi owner đăng ký key.\n- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.\n")
 refs="\n".join(f"{i}. [[{LABEL[s]}]]" for i,s in enumerate(l.sources,1));rows="\n".join(f"| [[{LABEL[s]}]] — `{s}` | {LOCATOR[s]} | cơ chế và boundary liên quan trực tiếp tới `{l.focus}` | các mục cơ chế, quyết định và probe | Đã phủ | phần ngoài objective DE-L{l.number:03d} |" for s in l.sources)
 parts.append(f"\n## Reference\n\n{refs}\n\n## Source coverage\n\n| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |\n|---|---|---|---|---|---|\n{rows}\n\n## Key takeaways\n\n- {l.decision}\n- {l.evidence}\n- `{l.focus}` chỉ có nghĩa trong scope, identity, state và version đã ghi.\n- Trước khi lab chạy, đây là note có provenance và protocol, chưa phải production evidence hay bằng chứng mastery.\n")
 return normalize_markdown("".join(parts))

def curriculum(l:Lesson,k:str):
 outcome,assessment,lab,pitfalls,homework,done=contract(l);header=f"# Phase 1: Engineering Foundation\n# Module {l.module}: {MODULES[l.module]}\n# Lesson {l.number}: {l.title}";body=re.sub(r"^---\n.*?\n---\n","",k,flags=re.S);body=re.sub(r"^# .+\n+","",body,count=1)
 note=f"{header}\n\n## Mục tiêu bài học\n\n**Năng lực cần chứng minh.** {outcome}\n\n**Điều kiện hoàn thành.** {done}\n\n{body}"
 after=f'''{header}

## Thực hành

**Nhiệm vụ.** {lab}

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** {assessment}

**Điều kiện đạt.** {done}

## Bài làm sau buổi học

**Nhiệm vụ.** {homework}

**Lỗi cần chủ động loại trừ.** {pitfalls}

## Reference

- Knowledge note: `{(PACK/l.filename).relative_to(ROOT)}`
- Nội dung học thuật: `note.md` cùng thư mục.
'''
 return note,after

def update_manifest(lessons,version,timestamp,check):
 data=json.loads(MANIFEST.read_text());fail=[];used={s for l in lessons for s in l.sources};by={x.get("source_id"):x for x in data["source_registry"]}
 for sid in used & SOURCE_NEW.keys():
  if check:
   if by.get(sid)!=SOURCE_NEW[sid]:fail.append(f"source drift {sid}")
  else:
   data["source_registry"]=[x for x in data["source_registry"] if x.get("source_id")!=sid];data["source_registry"].append(SOURCE_NEW[sid])
 ids={l.note_id for l in lessons}
 if not check:
  data["note_registry"]=[x for x in data["note_registry"] if x.get("note_id") not in ids];data["retrieval_test_set"]=[x for x in data["retrieval_test_set"] if x.get("expected_note_id") not in ids]
 byn={x.get("note_id"):x for x in data["note_registry"]};ret={(x.get("query"),x.get("expected_note_id")) for x in data["retrieval_test_set"]}
 for l in lessons:
  exp={"note_id":l.note_id,"path":f"2_Wiki/{WIKI_DIR[l.module]}/{l.title}.md","status":"review","source_ids":list(l.sources),"last_verified":"2026-10-02"};qs=(f"L{l.number} decision boundary nào?",f"L{l.number} counterexample nào?",f"L{l.number} evidence nào quyết định?")
  if check:
   if byn.get(l.note_id)!=exp:fail.append(f"note drift {l.note_id}")
   for q in qs:
    if (q,l.note_id) not in ret:fail.append(f"missing retrieval {q}")
  else:data["note_registry"].append(exp);data["retrieval_test_set"].extend({"query":q,"expected_note_id":l.note_id} for q in qs)
 if not check:
  data.update({"version":version,"updated_at":timestamp});data["layers"]["1_Nguon"]["source_count"]=len(data["source_registry"]);data["layers"]["2_Wiki"]["note_count"]=len(data["note_registry"]);MANIFEST.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
 return fail

def run(start,end,version,timestamp):
 parser=argparse.ArgumentParser();parser.add_argument("--check",action="store_true");a=parser.parse_args();lessons=tuple(load_lesson(n) for n in range(start,end+1));stale=[];digest=hashlib.sha256()
 for l in lessons:
  k=knowledge(l);note,after=curriculum(l,k);targets=((PACK/l.filename,k),(l.wiki,k),(l.folder/"note.md",note),(l.folder/"after-note.md",after))
  for p,c in targets:
   if a.check:
    if not p.exists() or p.read_text()!=c:stale.append(str(p.relative_to(ROOT)))
   else:p.parent.mkdir(parents=True,exist_ok=True);p.write_text(c)
  digest.update(note.encode());digest.update(after.encode())
 stale.extend(update_manifest(lessons,version,timestamp,a.check))
 if stale:print("STALE\n"+"\n".join(stale));return 1
 print(("checked" if a.check else "written")+f"={len(lessons)*4} stale=0 fingerprint={digest.hexdigest()}");return 0
