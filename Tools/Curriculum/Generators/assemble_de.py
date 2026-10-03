# -*- coding: utf-8 -*-
"""Ghép các file đặc tả DE thành bản nháp roadmap."""
import importlib.util, re, sys, os
B = os.path.dirname(os.path.abspath(__file__)) + '/'
sys.dont_write_bytecode = True

def load(n):
    sp = importlib.util.spec_from_file_location('m'+n, B+f'de_specs_{n}.py')
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m

FILES = sorted(re.findall(r'de_specs_(\d+)\.py', ' '.join(os.listdir(B))))
MODS = []
for fn in FILES:
    m = load(fn)
    for k in sorted([x for x in dir(m) if re.fullmatch(r'M\d+', x)], key=lambda s: int(s[1:])):
        MODS.append((int(k[1:]), getattr(m, k), getattr(m, 'L'+k[1:])))
MODS.sort(key=lambda t: t[0])

INC={'LT':"25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết",
     'TH':"20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung",
     'DA':"15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo",
     'KT':"75 phút làm bài độc lập · 45 phút chữa bài và phân tích lỗi theo nhóm"}
SELF={'LT':"**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi",
      'TH':"**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi",
      'DA':"**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp",
      'KT':"**Self-study (2,4 giờ).** Không có bài tự học. Nếu không đạt, theo phụ lục khắc phục khi không đạt cổng"}

def lesson(t):
    n,ti,ty,pre,learn,out,dg,lab,pit,done = t
    return (f"### Lesson {n} · {ti} `{ty}`\n**Prerequisites.** {pre}\n\n"
            f"**In-class (120 phút).** {INC[ty]}\n\n**Learn.** {learn}\n\n**Outcome.** {out}\n\n"
            f"**Đánh giá.** {dg}\n\n**Lab.** {lab}\n\n**Pitfalls.** {pit}\n\n{SELF[ty]}\n\n**Done when.** {done}\n")

def module(num, meta, ls):
    name,a1,z1,tbl,intro = meta
    return (f"# MODULE {num} · {name.upper()}\n\n**Lessons {a1}–{z1} · {(z1-a1+1)*2} giờ**\n\n"
            f"{tbl}\n\n{intro}\n\n" + "\n".join(lesson(x) for x in ls) + "\n")

mp = open(B+'de-module-map.md', encoding='utf-8').read()
rows = re.findall(r'^\|\s*([0-9])\s*\|\s*(M\d+)\s*\|\s*(.+?)\s*\|\s*(.*?)\s*\|\s*(\d+)\s*\|$', mp, re.M)
assert len(rows) == 40, len(rows)
tot = sum(int(r[4]) for r in rows)
tblmap = "| Chặng | Module | Tên | Mức | Bài |\n|---|---|---|---|---:|\n" + "\n".join(
    f"| {r[0]} | **{r[1]}** | {r[2]} | {r[3]} | {r[4]} |" for r in rows)

done = sum(len(ls) for _, _, ls in MODS)
lastmod = MODS[-1][0]
gates = [t[0] for _,_,ls in MODS for t in ls if t[2]=='KT']

HEAD = f"""---
chuong_trinh: Data Engineer
ma: DE
phien_ban: "5.0-draft"
trang_thai: draft
cap_do_dau_ra: Junior — Senior
so_bai: {tot}
cap_nhat: 2026-09-21
---

# CHƯƠNG TRÌNH DATA ENGINEER — BẢN NHÁP

> **Bản nháp để rà soát, không phải roadmap chính thức.**
> Roadmap chính thức vẫn là `material/data-engineer/roadmap/roadmap.md` (bản cũ, 102 bài).
> Bản này chứa **{done}/{tot} bài**, tức module M1 tới M{lastmod}{": đặc tả đã đủ 40 module." if lastmod == 40 and done == tot else ". %d module còn lại chưa viết đặc tả." % (40 - lastmod)}

**{tot} bài · 40 module · {tot*2} giờ trên lớp · không yêu cầu kiến thức đầu vào**

| | |
|---|---|
| **Vị trí đầu ra** | Data Engineer · Platform Engineer · Data Architect (đích mở rộng) |
| **Cấp độ đạt được** | Junior vững tới Senior; Staff và Principal cần kinh nghiệm thực tế ngoài chương trình |
| **Điều kiện đầu vào** | Không. Giả định chưa biết lập trình |
| **Thời lượng** | {tot} bài × 2 giờ trên lớp = {tot*2} giờ · cộng tự học 2,4 giờ mỗi bài = {int(tot*2.4)} giờ · tổng ~{int(tot*4.4)} giờ |
| **Nhịp học** | 12 giờ/tuần → ~34 tháng · 15 giờ/tuần → ~27 tháng |
| **Nguồn thiết kế** | `ROADMAP_DATA_ENGINEER_0_TO_ARCHITECT.md` (9 chặng) và `List học.md` (22 level) |
| **Ánh xạ khung năng lực** | SFIA 9 (2024): `DTAN`, `PROG`, `SYSP`, `NTAS`, `HPCC`, `DATM`, `TEST`, `CFMG`, `DBAD`, `ARCH` |

---

## 1. Bản đồ 40 module

{tblmap}

Cổng kiểm tra đã đặc tả: {' · '.join('lesson %d'%g for g in gates)}.

---

## 2. Quy ước đọc đặc tả bài

Mỗi bài trình bày theo cùng một khuôn, chín trường theo thứ tự cố định:

| Trường | Nội dung |
|---|---|
| **Prerequisites** | Bài hoặc module phải đạt trước |
| **In-class** | Phân bổ 120 phút trên lớp |
| **Learn** | Nội dung khái niệm và cơ chế |
| **Outcome** | Objective phát biểu bằng động từ quan sát được |
| **Đánh giá** | Tầng Bloom của objective, lý do tầng đó khớp vị trí bài, và hình thức kiểm tương ứng |
| **Lab** | Bài thực hành trên lớp |
| **Pitfalls** | Lỗi thường gặp |
| **Self-study** | Phân bổ 2,4 giờ ngoài lớp |
| **Done when** | Tiêu chí ra: đạt hoặc không đạt, có ngưỡng |

**Dạng bài.** `LT` lý thuyết · `TH` thực hành · `DA` dự án · `KT` kiểm tra.

**Ba mức thành thạo công cụ.** `A` xây và vận hành được · `B` làm lab và so sánh có căn cứ · `C` biết dùng đúng tình huống.

**Thang Bloom.** Sáu tầng dùng trong trường `Đánh giá`: *nhớ*, *hiểu*, *áp dụng*, *phân tích*, *đánh giá*, *sáng tạo*. Tầng quyết định hình thức kiểm hợp lệ; một objective tầng *áp dụng* không kiểm được bằng câu hỏi nhiều lựa chọn.

---

"""
TAIL = f"""
---

# PHỤ LỤC — TRẠNG THÁI BẢN NHÁP

| Hạng mục | Trạng thái |
|---|---|
| Bản đồ 40 module | Xong |
| Đặc tả bài M1–M{lastmod} | Xong {done}/{tot} |{"" if done == tot else "\n| Đặc tả bài M%d–M40 | **Chưa · 0/%d** |" % (lastmod + 1, tot - done)}
| Đồ thị phụ thuộc trong module | Chưa |
| Bộ dữ liệu và môi trường lab | Chưa |
| Đề các cổng có rubric | Thang điểm đã có trong đặc tả bài; chưa soạn đề |
"""

body = "".join(module(n, meta, ls) for n, meta, ls in MODS)
p = B + 'de-roadmap-draft.md'
open(p, 'w', encoding='utf-8').write(HEAD + body + TAIL)
print(f"{len(MODS)} module · {done}/{tot} bài · ghi {os.path.basename(p)}")
