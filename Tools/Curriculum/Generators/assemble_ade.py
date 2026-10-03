# -*- coding: utf-8 -*-
"""Ghép các file đặc tả ADE thành bản nháp roadmap Data Engineer (gộp AE + DE)."""
import importlib.util, re, sys, os
B = os.path.dirname(os.path.abspath(__file__)) + '/'
sys.dont_write_bytecode = True


def load(n):
    sp = importlib.util.spec_from_file_location('a' + n, B + f'ade_specs_{n}.py')
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m


# Thu tu module lay tu bang o muc 2 cua ban do, khong suy tu ten bien,
# vi M11B va M14B khong sap xep duoc bang so.
mp = open(B + 'ade-module-map.md', encoding='utf-8').read()
ROWS = re.findall(
    r'^\|\s*(\d+)\s*\|\s*(M\d+[A-D]?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.*?)\s*\|\s*(\d+)\s*\|$',
    mp, re.M)
assert len(ROWS) == 29, len(ROWS)
ORDER = [r[1] for r in ROWS]
PHASE = {r[1]: int(r[0]) for r in ROWS}
PLAN = {r[1]: int(r[5]) for r in ROWS}
TOT = sum(PLAN.values())

FILES = sorted(re.findall(r'ade_specs_(\d+)\.py', ' '.join(os.listdir(B))))
FOUND = {}
for fn in FILES:
    m = load(fn)
    for k in [x for x in dir(m) if re.fullmatch(r'M\d+[A-D]?', x)]:
        FOUND[k] = (getattr(m, k), getattr(m, 'L' + k[1:]))
MODS = [(k, FOUND[k][0], FOUND[k][1]) for k in ORDER if k in FOUND]

INC = {'LT': "25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết",
       'TH': "20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung",
       'DA': "15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo",
       'KT': "75 phút làm bài độc lập · 45 phút chữa bài và phân tích lỗi theo nhóm"}
SELF = {'LT': "**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi",
        'TH': "**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi",
        'DA': "**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp",
        'KT': "**Self-study (2,4 giờ).** Không có bài tự học. Nếu không đạt, theo phụ lục khắc phục khi không đạt cổng"}


def lesson(t):
    n, ti, ty, pre, learn, out, dg, lab, pit, done = t
    # Bai kiem tra dai hon mot buoi thuong; lay thoi luong tu chinh de bai
    # de bang cong, dac ta bai va frontmatter khong lech nhau.
    m = re.search(r"Buổi (\d+) phút", lab)
    phut = int(m.group(1)) if m else 120
    inc = INC[ty] if ty != 'KT' else ("%d phút làm bài độc lập · %d phút chữa bài và phân tích lỗi theo nhóm"
                                      % (phut - 45, 45))
    return (f"### Lesson {n} · {ti} `{ty}`\n**Prerequisites.** {pre}\n\n"
            f"**In-class ({phut} phút).** {inc}\n\n**Learn.** {learn}\n\n**Outcome.** {out}\n\n"
            f"**Đánh giá.** {dg}\n\n**Lab.** {lab}\n\n**Pitfalls.** {pit}\n\n{SELF[ty]}\n\n**Done when.** {done}\n")


def phut_bai(x):
    """Bai thuong 120 phut; bai cong lay thoi luong ghi trong de bai."""
    m = re.search(r"Buổi (\d+) phút", x[7])
    return int(m.group(1)) if m else 120


def module(mid, meta, ls):
    name, a1, z1, tbl, intro = meta
    gio = sum(phut_bai(x) for x in ls) / 60
    gio = int(gio) if gio == int(gio) else round(gio, 1)
    return (f"# MODULE {mid} · {name.upper()}\n\n"
            f"**Phase {PHASE[mid]} · Lessons {a1}–{z1} · {gio} giờ**\n\n"
            f"{tbl}\n\n{intro}\n\n" + "\n".join(lesson(x) for x in ls) + "\n")


done = sum(len(ls) for _, _, ls in MODS)
_all = [x for _, _, ls in MODS for x in ls]
N_KT = sum(1 for x in _all if x[2] == 'KT')
_g = sum(phut_bai(x) for x in _all) / 60
GIO_LOP = int(_g) if _g == int(_g) else round(_g, 1)
_s = (len(_all) - N_KT) * 2.4
GIO_TU_HOC = int(_s) if _s == int(_s) else round(_s, 1)
_t = GIO_LOP + GIO_TU_HOC
GIO_TONG = int(_t) if _t == int(_t) else round(_t, 1)
lastmod = MODS[-1][0] if MODS else "chưa có"
gates = [t[0] for _, _, ls in MODS for t in ls if t[2] == 'KT']

tblmap = "| Phase | Module | Tên | Vai | Mức | Bài |\n|---|---|---|---|---|---:|\n" + "\n".join(
    f"| {r[0]} | **{r[1]}** | {r[2]} | {r[3]} | {r[4]} | {r[5]} |" for r in ROWS)

HEAD = f"""---
chuong_trinh: Data Engineer
ma: DE
phien_ban: "6.0-draft"
trang_thai: draft
cap_do_dau_ra: Junior — Senior
so_bai: {TOT}
cap_nhat: 2026-09-23
---

# CHƯƠNG TRÌNH DATA ENGINEER — BẢN NHÁP GỘP

> **Bản nháp để rà soát, không phải roadmap chính thức.**
> Roadmap chính thức vẫn là `material/data-engineer/roadmap/roadmap.md` (bản cũ, 102 bài).
> Bản này gộp Analytics Engineer vào Data Engineer theo bản đồ `ade-module-map.md`.
> Đã đặc tả **{done}/{TOT} bài**{"" if done == TOT else f", tức {len(MODS)}/29 module. {29 - len(MODS)} module còn lại chưa viết đặc tả."}

**{TOT} bài · 29 module · {GIO_LOP} giờ trên lớp · không yêu cầu kiến thức đầu vào**

| | |
|---|---|
| **Vị trí đầu ra** | Data Engineer · Analytics Engineer · Platform Engineer · Data Architect (đích mở rộng) |
| **Cấp độ đạt được** | Junior vững tới Senior; Staff và Principal cần kinh nghiệm thực tế ngoài chương trình |
| **Điều kiện đầu vào** | Không. Giả định chưa biết lập trình |
| **Thời lượng** | {GIO_LOP} giờ trên lớp · {GIO_TU_HOC} giờ tự học · tổng ~{GIO_TONG} giờ. Bài thường 2 giờ lớp cộng 2,4 giờ tự học; {N_KT} bài cổng dài hơn và không có bài tự học |
| **Nhịp học** | 12 giờ/tuần → ~36 tháng · 15 giờ/tuần → ~29 tháng |
| **Nguồn thiết kế** | 29 hợp đồng học tập trong `06_LO_TRINH_CHI_TIET_THEO_MODULE` và `AE_DE_COVERAGE_AUDIT.md` |
| **Ánh xạ khung năng lực** | SFIA 9 (2024): `DTAN`, `PROG`, `SYSP`, `NTAS`, `HPCC`, `DATM`, `TEST`, `CFMG`, `DBAD`, `ARCH` |

---

## 1. Bản đồ 29 module

Cột **Vai** ghi module phục vụ vai nào: `AE` phần bù Analytics Engineer, `DE` phần riêng
Data Engineer, `chung` là nền bắt buộc cho cả hai. Bốn module `AE` là phần mà bản Data
Engineer cũ không phủ và là lý do của việc gộp.

{tblmap}

Cổng kiểm tra đã đặc tả: {' · '.join('lesson %d' % g for g in gates) if gates else 'chưa có'}.

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

**Tám cổng xuyên suốt.** Correctness · Failure · Performance · Operability · Security · Change · Consumer value · Evidence. Mọi bài dự án và mọi cổng phase chấm theo tám cổng này.

---

"""

TAIL = f"""
---

# PHỤ LỤC — TRẠNG THÁI BẢN NHÁP

| Hạng mục | Trạng thái |
|---|---|
| Bản đồ 29 module | Xong |
| Đặc tả bài | {"Xong %d/%d" % (done, TOT) if done == TOT else "**Đang viết · %d/%d**" % (done, TOT)} |
| Đồ thị phụ thuộc trong module | Chưa |
| Bộ dữ liệu và môi trường lab | Chưa |
| Đề các cổng có rubric | Thang điểm đã có trong đặc tả bài; chưa soạn đề |
| Gỡ chương trình Analytics Engineer khỏi `material/` | Chưa · cần bản chốt mới |
"""

body = "".join(module(mid, meta, ls) for mid, meta, ls in MODS)
p = B + 'ade-roadmap-draft.md'
open(p, 'w', encoding='utf-8').write(HEAD + body + TAIL)

# doi chieu so bai thuc te voi ke hoach trong ban do
lech = [(mid, len(ls), PLAN[mid]) for mid, _, ls in MODS if len(ls) != PLAN[mid]]
print(f"{len(MODS)}/29 module · {done}/{TOT} bài · ghi {os.path.basename(p)}")
for mid, thuc, kh in lech:
    print(f"  LỆCH {mid}: đặc tả {thuc} bài, bản đồ ghi {kh}")
