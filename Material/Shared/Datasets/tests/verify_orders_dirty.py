# -*- coding: utf-8 -*-
"""Quet orders_dirty.csv va sinh dap an tu SO LIEU THAT, khong uoc luong."""
import csv, os, collections, datetime as dt
ROOT=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P=os.path.join(ROOT, "_data","ds2-retailbig","raw")
if not os.path.exists(os.path.join(P,"orders_dirty.csv")):
    print("  BO QUA kiem chung du lieu — chua sinh. Chay `make data` truoc.")
    raise SystemExit(0)
rows=list(csv.DictReader(open(os.path.join(P,"orders_dirty.csv"),encoding="utf-8")))
def is_int(s):
    try: int(s); return True
    except: return False
def is_date(s):
    try: dt.datetime.strptime(s,"%d/%m/%Y"); return True
    except: return False
def is_dec(s):
    try: float(s); return True
    except: return False

bad_id  = [r for r in rows if not is_int(r["OrderID"])]
bad_day = [r for r in rows if not is_date(r["OrderDate"])]
bad_num = [r for r in rows if not is_dec(r["Sales"])]
no_name = [r for r in rows if not r["CustomerName"].strip()]
fail_cast = {id(r) for r in bad_id+bad_day+bad_num}
ok = [r for r in rows if id(r) not in fail_cast]
dup = {k:v for k,v in collections.Counter(r["OrderID"] for r in ok).items() if v>1}
dup_rows = sum(v-1 for v in dup.values())

txt=[]
txt.append("ĐÁP ÁN — orders_dirty.csv (dành cho giảng viên)")
txt.append("="*62)
txt.append("Số liệu dưới đây được đếm trực tiếp trên file, không phải ước lượng.\n")
txt.append(f"Tổng số dòng trong file          : {len(rows):,}")
txt.append(f"OrderID không ép được sang INT   : {len(bad_id)}")
txt.append(f"OrderDate không đúng dd/MM/yyyy  : {len(bad_day)}")
txt.append(f"Sales không ép được sang DECIMAL : {len(bad_num)}")
txt.append(f"→ Tổng dòng TRY_CONVERT thất bại : {len(fail_cast)}  (Orders_Rejected)")
txt.append(f"→ Dòng qua được ép kiểu          : {len(ok):,}")
txt.append(f"OrderID trùng trong nhóm qua ép  : {len(dup)} mã, thừa {dup_rows} dòng")
txt.append(f"Thiếu tên khách (vi phạm NOT NULL): {len(no_name)}")
txt.append("")
txt.append(f"Phép kiểm tra bắt buộc ở Bước 6:")
txt.append(f"  {len(ok):,} (sạch) + {len(fail_cast)} (bị loại) = {len(ok)+len(fail_cast):,} = tổng số dòng nguồn")
txt.append("")
txt.append("Nếu học viên áp thêm ràng buộc PRIMARY KEY và NOT NULL thì bảng chính")
txt.append(f"chỉ nhận {len(ok)-dup_rows:,} dòng — chênh lệch này chính là bài học của Câu 7 trong giáo án.")
txt.append("")
txt.append("Mã OrderID bị trùng: "+", ".join(sorted(dup)[:10])+(" ..." if len(dup)>10 else ""))
open(os.path.join(P,"orders_dirty_ANSWERS.txt"),"w",encoding="utf-8").write("\n".join(txt)+"\n")
print("\n".join(txt))
