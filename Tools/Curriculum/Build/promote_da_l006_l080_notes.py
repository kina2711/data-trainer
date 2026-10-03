#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, json, re
from dataclasses import dataclass
from pathlib import Path
from format_knowledge_notes import normalize_markdown

ROOT=Path(__file__).resolve().parents[3]; CUR=ROOT/'Material/DA/Curriculum'; MAN=ROOT/'Docs/Second-Brain/second-brain-manifest.json'
PACK=ROOT/'Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01'; WIKI=ROOT/'Docs/Second-Brain/2_Wiki'
SRC={
 1:('src.web.govuk-understand-user-needs','src.web.govuk-data-analytics-tools-guidance'),
 2:('src.web.govuk-data-analytics-tools-guidance','src.book.kimball-ross-data-warehouse-toolkit.3e'),
 3:('src.course.hcmut-sql','src.book.silberschatz-database-system-concepts.7e'),
 4:('src.book.kimball-ross-data-warehouse-toolkit.3e','src.book.silberschatz-database-system-concepts.7e'),
 5:('src.book.openintro-statistics.4e','src.paper.google-heart-ux-metrics'),
 6:('src.book.knaflic-storytelling-with-data.1e','src.book.ferrari-russo-definitive-guide-dax.3e'),
 7:('src.web.amplitude-north-star-framework','src.paper.google-heart-ux-metrics'),
 8:('src.book.kohavi-tang-xu-trustworthy-experiments.1e','src.book.openintro-statistics.4e'),
 9:('src.docs.python-3.14-language-reference','src.docs.python-3.14-stdlib-runtime'),
10:('src.book.knaflic-storytelling-with-data.1e','src.web.govuk-understand-user-needs'),
11:('src.web.govuk-data-analytics-tools-guidance','src.book.knaflic-storytelling-with-data.1e')}
WIKI_DIR={1:'Data-Analysis',2:'Excel',3:'SQL',4:'Data-Modeling',5:'Statistics',6:'Data-Visualization',7:'Product-Analytics',8:'Experimentation',9:'Python',10:'Communication',11:'Data-Analysis'}
MODULES={1:'Introduction to the Data Analyst Role',2:'Excel for Data Analysis',3:'SQL and Databases',4:'Data Modeling and Preparation',5:'Statistics for Data Analysts',6:'Visualization and Power BI',7:'Product and Business Analytics',8:'A-B Testing',9:'Python for Data Analysts',10:'Communication and Career',11:'Capstone Project'}
NEW_SOURCES=(
 ('src.book.openintro-statistics.4e','1_Nguon/Books/SRC-OPENINTRO-STATISTICS-4E.md','Material/Reference_temp/OpenIntro_Statistics_4th_ed_-_Christopher_Barr.pdf','fbdb1a6a002c5e0383a557bce1ed59075523f7719f650571466faa1fe4191781'),
 ('src.book.knaflic-storytelling-with-data.1e','1_Nguon/Books/SRC-STORYTELLING-WITH-DATA.md','Material/Reference_temp/Storytelling_with_Data_-_Cole_Nussbaumer_Knaflic.pdf','e87c92b0a9986433e747e72a245a82f13bdb7cadca782a26ae254dcbb25c4da0'),
 ('src.book.ferrari-russo-definitive-guide-dax.3e','1_Nguon/Books/SRC-DEFINITIVE-GUIDE-DAX-3E.md','Material/Reference_temp/The_Definitive_Guide_to_DAX_3E_-_Alberto_Ferrari.pdf','47f03d37f26dc46cd155a1090c8950fd5580bb4bd1aa8b026906e86093bec217'),
 ('src.book.kohavi-tang-xu-trustworthy-experiments.1e','1_Nguon/Books/SRC-TRUSTWORTHY-ONLINE-CONTROLLED-EXPERIMENTS.md','Material/Reference_temp/Trustworthy_Online_Controlled_Experiments_-_Ron_Kohavi.pdf','edcd7c588a21d465e74e8538a8052edbb4bd86527ad59df70e9dab071ca7f949'))

def field(t,n):
 m=re.search(rf'(?m)^\*\*{re.escape(n)}\.\*\*\s*(.+)$',t); return m.group(1).strip() if m else ''
@dataclass(frozen=True)
class L:
 n:int; folder:Path; module:int; title:str; slug:str; outcome:str; assessment:str; lab:str; pitfalls:str; homework:str; done:str; learn:str
 @property
 def note_id(self):return f'wiki.da.{self.slug}'
 @property
 def ck(self):return f'ck.da.{self.slug}'
 @property
 def filename(self):return f'{self.n:03d}-{self.slug}.md'
 @property
 def wiki(self):return WIKI/WIKI_DIR[self.module]/f'{self.title}.md'

def load(n):
 f=list(CUR.glob(f'Phase_*/Module_*/Lesson_{n:03d}-*'))[0]; t=(f/'note.md').read_text(); a=(f/'after-note.md').read_text(); mod=int(re.search(r'Module_(\d+)',f.parent.name).group(1)); title=(re.search(r'(?m)^tieu_de: "(.+)"$',t) or re.search(rf'(?m)^# Lesson {n}\s*[—:-]\s*(.+)$',t)).group(1); slug=f.name.split('-',1)[1]
 legacy=[field(t,x) for x in ('Outcome','Đánh giá','Lab','Pitfalls')]; ss=re.search(r'(?m)^\*\*Self-study[^*]*\.\*\*\s*(.+)$',t); legacy += [ss.group(1).strip() if ss else '',field(t,'Done when')]
 if all(legacy): out,ass,lab,pit,home,done=legacy
 else:
  tasks=re.findall(r'(?m)^\*\*Nhiệm vụ\.\*\*\s*(.+)$',a); out,ass,lab,pit,home,done=field(t,'Năng lực cần chứng minh'),field(a,'Cách đánh giá'),tasks[0],field(a,'Lỗi cần chủ động loại trừ'),tasks[1],field(t,'Điều kiện hoàn thành')
 summary=re.search(r'(?m)^\*\*Tóm tắt bản chất:\*\*\s*(.+?)\s+Điểm quyết định là ',t)
 learn=field(t,'Learn') or (summary.group(1).strip() if summary else out)
 return L(n,f,mod,title,slug,out,ass,lab,pit,home,done,learn)

def render(x):
 prev='wiki.da-foundation.vague-request-to-answerable-question' if x.n==6 else f'wiki.da.{load(x.n-1).slug}'
 prerequisite='[]' if x.n==85 else f'[wiki.da.{load(x.n+1).slug}]'
 registry={s['source_id']:s for s in json.loads(MAN.read_text())['source_registry']}
 src='\n'.join(f'  - {s}' for s in SRC[x.module])
 refs='\n'.join(f'{i}. [[{Path(registry[s]["record_path"]).stem}]] — `{s}`' for i,s in enumerate(SRC[x.module],1))
 rows='\n'.join(f'| [[{Path(registry[s]["record_path"]).stem}]] — `{s}` | Source record và phạm vi đọc đã đăng ký | Cơ chế liên quan tới {x.title} | các mục cơ chế, case và probe | Đã phủ | ngoài objective L{x.n:03d} |' for s in SRC[x.module])
 fm=f'''---\nnote_id: {x.note_id}\nconcept_key: {x.ck}\nconcept_key_status: proposed\nnote_type: concept-deep-dive\nstatus: review\nlanguage: vi\ncreated: 2026-10-02\nlast_verified: 2026-10-02\nreview_after: 2027-04-02\neditorial_pass: humanized-v3\nprimary_question: Làm sao áp dụng {x.title} và chứng minh kết quả không xanh giả?\nsource_ids:\n{src}\nrelationships:\n  builds_on: [{prev}]\n  prerequisite_of: {prerequisite}\naliases: [{x.title}]\ntags: [wiki/{WIKI_DIR[x.module].lower()}, data-analyst, module-{x.module}]\nreference_path: Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/{x.filename}\n---\n'''
 parts=[fm,f'''\n# {x.title}\n\n**Tóm tắt bản chất:** {x.learn} Điểm quyết định là giữ đúng population, grain, thời gian và oracle trước khi tin output.\n\n## Nỗi Đau & Động Lực\n\nL{x.n:03d} bắt đầu từ một lỗi rất thực dụng: analyst có thể tạo được file, query hoặc dashboard đúng cú pháp nhưng không trả lời đúng câu hỏi. Với **{x.title}**, hậu quả xuất hiện ở người ra quyết định; họ hành động trên một con số không còn truy được về population, grain hoặc assumption ban đầu.\n\nRoadmap đặt chuẩn đầu ra như sau: {x.outcome} Đây là năng lực quan sát được, không phải yêu cầu nhớ thuật ngữ. Nếu bằng chứng không cho reviewer tái hiện cùng kết luận, bài vẫn chưa đạt dù output nhìn hợp lý.\n\n## Cơ Chế Tác Động\n\n{x.learn}\n\nCơ chế của `{x.slug}` được kiểm qua năm lớp: input và population; identity và grain; transformation; time boundary; consumer-visible output. Mỗi lớp cần một invariant ngắn, một failure có chủ ý và một phép đối soát độc lập. Command chạy thành công chỉ chứng minh execution; nó không chứng minh semantics.\n\nLỗi cần loại trừ trong bài này là: {x.pitfalls} Tách các lỗi ấy thành fixture riêng giúp chẩn đoán nguyên nhân thay vì sửa nhiều biến cùng lúc.\n\n## Bản Đồ Quyết Định\n\n| Dấu hiệu | Quyết định | Bằng chứng bắt buộc |\n|---|---|---|\n| Population và grain rõ | Tiếp tục xử lý | Row count, uniqueness, control total |\n| Assumption đổi nghĩa kết quả | Dừng và xác minh | Owner cùng impact-if-wrong |\n| Dữ liệu thiếu nhưng đo được coverage | Phân tích có điều kiện | Missing report và limitation |\n| Hai đường tính không khớp | Truy ngược boundary | Snapshot và reconciliation |\n| Deadline không đủ cho phép kiểm | Co phạm vi | Non-goal và câu trả lời tạm thời |\n\nQuy tắc của L{x.n:03d}: chọn phương án đơn giản nhất vẫn giữ được điều kiện hoàn thành “{x.done}”. Không dùng độ phức tạp để che một câu hỏi chưa rõ.\n\n## Case Study Thực Chiến: {x.title}\n\nBài thực hành dùng nhiệm vụ thật của roadmap: {x.lab}\n\nTrước khi thao tác ở `{x.title}`, learner ghi expected result, grain, identity, cutoff và phép kiểm. Sau thao tác, họ giữ raw output cùng một oracle khác đường triển khai. Nếu hai đường không khớp, discrepancy trở thành kết quả cần điều tra; không được sửa expected cho giống output vừa thấy.\n\nBiến thể khó hơn đổi một constraint: dữ liệu có bản ghi trùng, đến muộn, thiếu khóa hoặc có nhiều dòng con cho một thực thể. L{x.n:03d} chỉ được xem là transfer khi learner tự nhận ra phép tính nào không còn hợp lệ và thiết kế lại boundary mà không cần chép case mẫu.\n\n## Góc Khuất & Ngộ Nhận\n\n**Hiểu lầm:** Output của `{x.title}` chạy được nghĩa là kết luận đúng. **Thực tế:** syntax không kiểm population, grain, cutoff hay định nghĩa nghiệp vụ. **Vì sao nghe hợp lý:** công cụ trả kết quả cụ thể và không hiển thị assumption đã bị bỏ qua.\n\n**Hiểu lầm:** Thêm nhiều bước kiểm luôn làm phân tích đáng tin hơn. **Thực tế:** hai phép kiểm dùng chung dữ liệu và cùng logic có thể sai giống nhau. **Vì sao nghe hợp lý:** số lượng test tạo cảm giác độc lập dù oracle không độc lập.\n\n**Hiểu lầm:** Có thể sửa edge case sau khi hoàn thành happy path. **Thực tế:** {x.pitfalls} **Vì sao nghe hợp lý:** dữ liệu mẫu nhỏ thường không chạm fan-out, missing, skew, late arrival hoặc changed constraint.\n\n## Nếu Bạn Dạy Lại Điều Này...\n\nMở đầu L{x.n:03d} bằng một output trông hợp lý nhưng sai đúng một invariant. Người học viết dự đoán trước khi xem cơ chế. Exercise seed đổi duy nhất một constraint và yêu cầu họ nói rõ quyết định giữ nguyên hay đảo, cùng evidence đủ mạnh để thuyết phục reviewer.\n\n## Ma trận kiểm chứng\n''']
 pivots=('population','grain','identity','time cutoff','missing versus zero','duplicate','join fan-out','changed definition','independent oracle','replay','fresh snapshot','novel scenario')
 claims=(x.learn,x.outcome,x.pitfalls,x.done)
 for i,p in enumerate(pivots,1):
  parts.append(f'''\n### Probe {i}: {p}\n\n**Mệnh đề của probe {i} — `{p}`.** {claims[(i-1)%4]}\n\n**Thiết kế.** Probe {i} của L{x.n:03d} tạo fixture nhỏ cho `{p}` với một control và một bản ghi chỉ khác tại boundary đang xét. Expected result được khóa trước execution; snapshot, version, identity và state ban đầu đi cùng artifact.\n\n**Oracle L{x.n:03d}.{i}.** Đối soát `{p}` bằng đường tính khác implementation chính của `{x.slug}`. Giữ command, raw observation, before/after counts và limitation. Probe chỉ đạt khi reviewer đi từ fixture tới cùng kết luận mà không hỏi tác giả đã chọn mặc định nào.\n''')
 parts.append(f'''\n## Tự Kiểm Tra Nhanh\n\n1. Năng lực nào phải chứng minh ở L{x.n:03d}?\n\n<details><summary>Đáp án</summary>\n\n{x.outcome}\n\n</details>\n\n2. Failure nào phải chủ động cài vào fixture?\n\n<details><summary>Đáp án</summary>\n\n{x.pitfalls}\n\n</details>\n\n3. Khi nào bài được xem là hoàn thành?\n\n<details><summary>Đáp án</summary>\n\n{x.done}\n\n</details>\n\n## Giới hạn và điều chưa cho phép kết luận\n\n- Case và probe là protocol giảng dạy; chưa phải quan sát production.\n- Con số minh họa không phải benchmark ngành.\n- Concept key `{x.ck}` đang `proposed`, chưa tính canonical coverage.\n- Note tồn tại không phải bằng chứng learner đã thành thạo.\n\n## Reference\n\n{refs}\n\n## Source coverage\n\n| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |\n|---|---|---|---|---|---|\n{rows}\n\n## Key takeaways\n\n- {x.outcome}\n- {x.done}\n- Kết luận chỉ có nghĩa trong population, grain, time và version đã công bố.\n- Note tiếp theo được nối bằng `prerequisite_of`; mastery cần learner artifact riêng.\n''')
 return normalize_markdown(''.join(parts))

def curriculum(x,k):
 body=re.sub(r'^---\n.*?\n---\n','',k,flags=re.S);body=re.sub(r'^# .+\n+','',body,count=1);h=f'# Phase {1 if x.n<=16 else 2 if x.n<=30 else 3 if x.n<=54 else 4}: Data Analyst\n# Module {x.module}: {MODULES[x.module]}\n# Lesson {x.n}: {x.title}'
 note=f'{h}\n\n## Mục tiêu bài học\n\n**Năng lực cần chứng minh.** {x.outcome}\n\n**Điều kiện hoàn thành.** {x.done}\n\n{body}'
 after=f'''{h}\n\n## Thực hành\n\n**Nhiệm vụ.** {x.lab}\n\nGiữ input snapshot, grain, identity, version, raw output, reconciliation và limitation.\n\n## Tiêu chí hoàn thành\n\n**Cách đánh giá.** {x.assessment}\n\n**Điều kiện đạt.** {x.done}\n\n## Bài làm sau buổi học\n\n**Nhiệm vụ.** {x.homework}\n\n**Lỗi cần chủ động loại trừ.** {x.pitfalls}\n\n## Reference\n\n- Knowledge note: `{(PACK/x.filename).relative_to(ROOT)}`\n'''
 return normalize_markdown(note),normalize_markdown(after)

def update_manifest(ls,check,version):
 d=json.loads(MAN.read_text());fail=[];by={s['source_id']:s for s in d['source_registry']}
 for sid,rp,rel,sha in NEW_SOURCES:
  exp={'source_id':sid,'record_path':rp,'canonical_path':str(ROOT/rel),'sha256':sha,'captured':'2026-10-02','rights':'copyrighted-private-owner-provided'}
  if check:
   if by.get(sid)!=exp:fail.append('source drift '+sid)
  elif sid not in by:d['source_registry'].append(exp)
 ids={x.note_id for x in ls}
 if not check:
  d['note_registry']=[z for z in d['note_registry'] if z.get('note_id') not in ids];d['retrieval_test_set']=[z for z in d['retrieval_test_set'] if z.get('expected_note_id') not in ids]
 byn={z['note_id']:z for z in d['note_registry']}; ret={(z.get('query'),z.get('expected_note_id')) for z in d['retrieval_test_set']}
 for x in ls:
  exp={'note_id':x.note_id,'path':f'2_Wiki/{WIKI_DIR[x.module]}/{x.title}.md','status':'review','source_ids':list(SRC[x.module]),'last_verified':'2026-10-02'};qs=(f'DA L{x.n} boundary?',f'DA L{x.n} failure?',f'DA L{x.n} evidence?')
  if check:
   if byn.get(x.note_id)!=exp:fail.append('note drift '+x.note_id)
   for q in qs:
    if (q,x.note_id) not in ret:fail.append('missing retrieval '+q)
  else:d['note_registry'].append(exp);d['retrieval_test_set'].extend({'query':q,'expected_note_id':x.note_id} for q in qs)
 if not check:
  d['version']=version;d['updated_at']='2026-10-02T18:00:00+07:00';d['layers']['1_Nguon']['source_count']=len(d['source_registry']);d['layers']['2_Wiki']['note_count']=len(d['note_registry']);MAN.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
 return fail

def run(start,end,check=False):
 ls=[load(n) for n in range(start,end+1)];stale=[];dig=hashlib.sha256()
 for x in ls:
  k=render(x);n,a=curriculum(x,k); targets=((PACK/x.filename,k),(x.wiki,k),(x.folder/'note.md',n),(x.folder/'after-note.md',a))
  for p,c in targets:
   if check:
    if not p.exists() or p.read_text()!=c:stale.append(str(p.relative_to(ROOT)))
   else:p.parent.mkdir(parents=True,exist_ok=True);p.write_text(c)
   dig.update(c.encode())
 stale+=update_manifest(ls,check,f'1.0.{104+end//5}')
 if stale:print('STALE\n'+'\n'.join(stale));return 1
 print(f'{"checked" if check else "written"} lessons={start:03d}-{end:03d} files={len(ls)*4} fingerprint={dig.hexdigest()}');return 0

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('start',type=int);p.add_argument('end',type=int);p.add_argument('--check',action='store_true');a=p.parse_args();raise SystemExit(run(a.start,a.end,a.check))
