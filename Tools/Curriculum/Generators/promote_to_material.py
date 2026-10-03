# -*- coding: utf-8 -*-
"""Dua ban nhap ADE thanh material/data-engineer/roadmap/roadmap.md.

    python3 .data-2026/build/promote_to_material.py

Nguon:  .data-2026/build/ade-roadmap-draft.md  (sinh boi assemble_ade.py)
        .data-2026/build/ade-module-map.md     (thu tu va so bai cua 29 module)
Ra:     material/data-engineer/roadmap/roadmap.md

Viec chinh la doi ma module: ban nhap dung ma cua hop dong nguon (M11B, M14B,
M14C, M14D) de truy nguoc; trong material/ module phai danh so lien tuc 1..29.
Anh xa chay MOT LUOT tren toan van ban, khong thay the tuan tu, vi thay the
tuan tu se dich chong len nhau (M16 -> M21 roi M21 -> M26).
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
B = os.path.join(ROOT, ".data-2026", "build") + os.sep
sys.path.insert(0, os.path.join(ROOT, "material", "_shared", "tools"))
from scaffold_material import title_case

mp = open(B + "ade-module-map.md", encoding="utf-8").read()
ROWS = re.findall(
    r"^\|\s*(\d+)\s*\|\s*(M\d+[A-D]?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.*?)\s*\|\s*(\d+)\s*\|$",
    mp, re.M)
assert len(ROWS) == 29, len(ROWS)
ORDER = [r[1] for r in ROWS]
OLD2NEW = {mid: str(i + 1) for i, mid in enumerate(ORDER)}

t = open(B + "ade-roadmap-draft.md", encoding="utf-8").read()

# 1. frontmatter va tieu de
t = re.sub(r"^---\n.*?\n---\n", """---
chuong_trinh: Data Engineer
ma: DE
phien_ban: "6.0"
trang_thai: draft
cap_do_dau_ra: Junior — Senior
so_bai: 440
cap_nhat: 2026-09-24
---
""", t, count=1, flags=re.S)
t = t.replace("# CHƯƠNG TRÌNH DATA ENGINEER — BẢN NHÁP GỘP", "# CHƯƠNG TRÌNH DATA ENGINEER")
t = re.sub(r"\n> \*\*Bản nháp để rà soát.*?\n\n", "\n\n", t, count=1, flags=re.S)

# 2. doi ma module. Ba dang phai xu ly, lam theo dung thu tu nay:
#    a) tieu de  "# MODULE M14B ·"
#    b) tien de  "**Prerequisites.** Module 14B: ..."   <- khong co tien to M
#    c) tham chieu trong van xuoi "M14B"
t = re.sub(r"^# MODULE (M\d+[A-D]?) · ",
           lambda m: "# MODULE %s · " % OLD2NEW[m.group(1)], t, flags=re.M)
t = re.sub(r"^(\*\*Prerequisites\.\*\* Module )(\d+[A-D]?):",
           lambda m: "%s%s:" % (m.group(1), OLD2NEW["M" + m.group(2)]), t, flags=re.M)
t = re.sub(r"\b(M\d+[A-D]?)\b",
           lambda m: "M" + OLD2NEW[m.group(1)] if m.group(1) in OLD2NEW else m.group(0), t)

# 3. dong phu cap module: scaffold_material doc dong bat dau bang "**Lesson"
t = re.sub(r"^\*\*Phase (\d+) · (Lessons [^\n]*?)\*\*$", r"**\2 · Phase \1**", t, flags=re.M)

# 4. bang cong kiem tra, dung cho moi so bai KT chu gan cung bon cong
kt = re.findall(r"^### Lesson (\d+) · ([^\n]+?) `KT`\n(.*?)(?=\n### Lesson |\n# |\Z)",
                t, re.M | re.S)
grows = []
for i, (n, _title, body) in enumerate(kt, 1):
    out = re.search(r"\*\*Outcome\.\*\* ([^\n]+)", body).group(1).rstrip(".")
    done = re.search(r"\*\*Done when\.\*\* ([^\n]+)", body).group(1).split(".")[0]
    phut = re.search(r"\*\*In-class \((\d+) phút\)", body).group(1)
    grows.append("| %s | %s | %s | %s phút | %s |" % (
        "Tốt nghiệp" if i == len(kt) else str(i), n, out, phut, done))
GATES = ("\n## %s cổng kiểm tra\n\n"
         "Cổng là điều kiện cứng, không phải mốc tham khảo. Không đạt thì học lại phần tương ứng\n"
         "và thi lại một lần; chi phí của việc cho qua phát sinh ở module sau và cao hơn chi phí học lại.\n\n"
         "| Cổng | Sau bài | Đo cái gì | Thời lượng | Ngưỡng đạt |\n|---|---|---|---|---|\n"
         % {10: "Mười"}.get(len(kt), str(len(kt))) + "\n".join(grows) + """

Cổng cuối là **Bảo vệ tốt nghiệp** của toàn chương trình. Mỗi cổng có ít nhất một điều kiện điểm
không: một sai lầm về phương pháp làm phần đó bằng không dù các phần khác đạt. Chi tiết nằm trong
đặc tả của từng bài cổng.

---
""")

# 5. bang ban do module. Ten module lay qua title_case de khop ten thu muc
#    va khop frontmatter ma scaffold_material sinh ra.
mods = re.findall(
    r"^# MODULE (\d+) · ([^\n]+)\n\n\*\*Lessons ([^\n]+?) · ([\d.]+) giờ · Phase (\d+)\*\*",
    t, re.M)
assert len(mods) == 29, len(mods)
mrows = ["| **M%s** | %s | %s | %s | Phase %s | `%s` |"
         % (num, title_case(name), rng, gio, ph, ORDER[int(num) - 1])
         for num, name, rng, gio, ph in mods]
MAP = ("\n## Bản đồ module\n\n"
       "Cột *hợp đồng nguồn* giữ mã module trong `06_LO_TRINH_CHI_TIET_THEO_MODULE` để truy ngược.\n\n"
       "| Module | Tên | Bài | Giờ | Phase | Hợp đồng nguồn |\n|---|---|---|---|---|---|\n"
       + "\n".join(mrows) + "\n\n---\n")

i = t.index("\n# MODULE 1 · ")
t = t[:i] + GATES + MAP + t[i:]

# 6. phu luc trang thai
t = re.sub(r"# PHỤ LỤC — TRẠNG THÁI BẢN NHÁP\n.*$", """# PHỤ LỤC — TRẠNG THÁI XÂY DỰNG

| Hạng mục | Trạng thái |
|---|---|
| Bản đồ 29 module | Xong |
| Đặc tả 440 bài | Xong · 440/440 |
| Mười cổng kiểm tra | Xong · thang điểm nằm trong đặc tả bài |
| Đồ thị phụ thuộc trong từng module | Chưa |
| Bộ dữ liệu và môi trường lab | Chưa · sẽ do người dạy cung cấp |
| Đề chi tiết cho từng cổng | Chưa · mới có cấu trúc và thang điểm |
| Nội dung chi tiết từng bài trong `curriculum/` | Chưa · khung đã sinh |

## Quy ước về ngưỡng chấm

Một số tiêu chí `Done when` viết là *dưới ngưỡng thoả thuận* hoặc *trong giới hạn thời gian* thay
vì một con số. Đó là chủ ý: ngưỡng phụ thuộc phần cứng của lớp, bộ dữ liệu và bối cảnh, nên gán
cứng một con số sẽ sai ở phần lớn lớp học. Điều kiện bắt buộc đi kèm: **người dạy chốt ngưỡng và
ghi vào đề trước buổi học, không chốt sau khi đã thấy kết quả của học viên.**
""", t, flags=re.S)

out = os.path.join(ROOT, "material", "data-engineer", "roadmap", "roadmap.md")
os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, "w", encoding="utf-8").write(t)
print("module %d · bai %d · hang ban do %d · cong %d"
      % (len(re.findall(r"^# MODULE \d+ ·", t, re.M)),
         len(re.findall(r"^### Lesson \d+ ·", t, re.M)), len(mrows), len(kt)))
bad = re.findall(r"^\*\*Prerequisites\.\*\* Module (\d+[A-D]):", t, re.M)
print("tien de con mang ma cu:", bad or "khong co")
