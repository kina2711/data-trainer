# -*- coding: utf-8 -*-
"""orders.csv — tep thuc hanh cho BUOI 2 (ky thuat import).
Chua dung 4 cam bay ma giao an mo ta:
  1. dau phay noi gian trong dia chi  -> bat buoc dung text qualifier
  2. tieng Viet co dau                -> bat buoc UTF-8 + NVARCHAR
  3. so dien thoai bat dau bang 0     -> bat buoc VARCHAR
  4. ngay dinh dang dd/mm/yyyy        -> xung dot voi chuan My
Ban _dirty them cac dong hong de lam bai Staging Table."""
import csv, random, os, datetime as dt
random.seed(777)
ROOT=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT=os.path.join(ROOT, "_data","ds2-retailbig","raw")
os.makedirs(OUT, exist_ok=True)

HO="Nguyễn Trần Lê Phạm Hoàng Huỳnh Phan Vũ Võ Đặng Bùi Đỗ".split()
DEM="Văn Thị Hữu Đức Minh Ngọc Thanh Quang".split()
TEN="An Bình Cường Dũng Hà Hùng Lan Mai Nam Oanh Phúc Quân Sơn Thảo Tuấn Vy Yến Đạt Linh Trang".split()
DUONG=["Lê Lợi","Nguyễn Huệ","Hai Bà Trưng","Trần Hưng Đạo","Điện Biên Phủ","Cách Mạng Tháng 8","Nguyễn Trãi"]
# dia chi CO dau phay ben trong -> cam bay so 1
TINH=[("Quận 1","TP. Hồ Chí Minh"),("Quận 7","TP. Hồ Chí Minh"),("Cầu Giấy","Hà Nội"),
      ("Ba Đình","Hà Nội"),("Hải Châu","Đà Nẵng"),("Ninh Kiều","Cần Thơ")]

def row(i):
    ten=f"{random.choice(HO)} {random.choice(DEM)} {random.choice(TEN)}"
    sdt=f"0{random.choice('35789')}{random.randint(10**7,10**8-1)}"      # cam bay 3
    q,t=random.choice(TINH)
    dc=f"Số {random.randint(1,320)} {random.choice(DUONG)}, {q}, {t}"     # cam bay 1
    d=dt.date(2024,1,1)+dt.timedelta(days=random.randint(0,365))
    ngay=d.strftime("%d/%m/%Y")                                          # cam bay 4
    sales=round(random.randint(45,5200)*1000 + random.choice([0,.5]),2)
    return [1000+i,ten,sdt,dc,ngay,f"{sales:.2f}"]

H=["OrderID","CustomerName","Phone","Address","OrderDate","Sales"]
N=50000
rows=[row(i) for i in range(N)]

p=os.path.join(OUT,"orders.csv")
with open(p,"w",newline="",encoding="utf-8") as f:
    w=csv.writer(f,quoting=csv.QUOTE_MINIMAL); w.writerow(H); w.writerows(rows)
print(f"  orders.csv        {N:,} dòng  ({os.path.getsize(p)/1048576:.1f} MB)")

# --- ban ban: them dong hong cho bai Staging Table ---
dirty=[r[:] for r in rows]
bad=[]
for idx in random.sample(range(N),9):
    dirty[idx][5]="N/A"; bad.append(("Sales = N/A",dirty[idx][0]))
for idx in random.sample(range(N),7):
    dirty[idx][4]="chưa rõ"; bad.append(("OrderDate = chưa rõ",dirty[idx][0]))
for idx in random.sample(range(N),4):
    dirty[idx][0]=f"ORD-{dirty[idx][0]}"; bad.append(("OrderID không phải số",dirty[idx][0]))
for idx in random.sample(range(N),5):
    d=dirty[idx][:]; dirty.append(d); bad.append(("OrderID trùng",d[0]))
for idx in random.sample(range(N),3):
    dirty[idx][1]=""; bad.append(("Thiếu tên khách",dirty[idx][0]))
random.shuffle(dirty)
p2=os.path.join(OUT,"orders_dirty.csv")
with open(p2,"w",newline="",encoding="utf-8") as f:
    w=csv.writer(f,quoting=csv.QUOTE_MINIMAL); w.writerow(H); w.writerows(dirty)
print(f"  orders_dirty.csv  {len(dirty):,} dòng  ({os.path.getsize(p2)/1048576:.1f} MB)  · {len(bad)} vấn đề cài sẵn")

with open(os.path.join(OUT,"orders_dirty_ANSWERS.txt"),"w",encoding="utf-8") as f:
    f.write("ĐÁP ÁN — các vấn đề cài sẵn trong orders_dirty.csv (dành cho giảng viên)\n")
    f.write("="*68+"\n")
    f.write(f"Tổng số dòng: {len(dirty):,} (gốc {N:,} + 5 dòng trùng)\n\n")
    from collections import Counter
    for k,v in Counter(b[0] for b in bad).items(): f.write(f"  {v:>2} dòng — {k}\n")
    f.write(f"\nSau khi làm sạch đúng, bảng chính phải có {N-9-7-4-3:,} dòng hợp lệ\n")
    f.write("và bảng Orders_Rejected phải có 23 dòng.\n")
print("  orders_dirty_ANSWERS.txt (đáp án cho giảng viên)")
