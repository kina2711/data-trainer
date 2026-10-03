# -*- coding: utf-8 -*-
"""DS2 · RetailBig — ~2 trieu dong, CO SAN DU LIEU BAN.
Dung cho buoi 12-14 (window functions), 20 (chan doan), 26-33 (Pandas/ML), 37-43 (cohort/RFM/funnel).
Du lieu ban duoc cai co y de hoc vien vap trong lop thay vi vap lan dau o cong ty."""
import csv, random, os, datetime as dt
random.seed(31415)
ROOT=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT=os.path.join(ROOT, "_data","ds2-retailbig","csv")
os.makedirs(OUT, exist_ok=True)

HO="Nguyễn Trần Lê Phạm Hoàng Huỳnh Phan Vũ Võ Đặng Bùi Đỗ Hồ Ngô Dương".split()
DEM="Văn Thị Hữu Đức Minh Ngọc Thanh Quang Xuân Hải".split()
TEN="An Bình Cường Dũng Hà Hùng Lan Mai Nam Oanh Phúc Quân Sơn Thảo Tuấn Vy Yến Đạt Linh Trang Nhung Tú Khoa Duy".split()
# CO Y viet khong thong nhat -> bai hoc ve chieu "Nhat quan"
TINH_BAN=[("Hà Nội",.55),("HN",.15),("Ha Noi",.12),("hà nội",.10),("TP Hà Nội",.08)]
TINH_SACH=["TP. Hồ Chí Minh","Đà Nẵng","Hải Phòng","Cần Thơ","Bình Dương","Đồng Nai","Khánh Hòa","Nghệ An"]
KENH=["app","web","san_tmdt","cua_hang"]
TT=[("delivered",.78),("cancelled",.11),("returned",.05),("pending",.06)]
def pick(ws):
    r=random.random(); c=0
    for v,w in ws:
        c+=w
        if r<=c: return v
    return ws[-1][0]

def w(name,header,rows,note=""):
    p=os.path.join(OUT,name)
    with open(p,"w",newline="",encoding="utf-8") as f:
        wr=csv.writer(f); wr.writerow(header); wr.writerows(rows)
    print(f"  {name:<22} {len(rows):>9,} dòng  {os.path.getsize(p)/1048576:>6.1f} MB  {note}")

# --- KhachHang: 120k, co dong trung + thieu tinh ---
kh=[]
for i in range(1,120001):
    tinh = pick(TINH_BAN) if random.random()<.32 else random.choice(TINH_SACH)
    if random.random()<.06: tinh=""                                   # thieu gia tri
    d=dt.date(2022,1,1)+dt.timedelta(days=random.randint(0,1090))
    kh.append([f"C{i:06d}",f"{random.choice(HO)} {random.choice(DEM)} {random.choice(TEN)}",
               f"0{random.choice('35789')}{random.randint(10**7,10**8-1)}",tinh,
               d.isoformat(),random.choice(KENH)])
for r in random.sample(kh,900): kh.append(r[:])                        # 900 dong trung
random.shuffle(kh)
w("KhachHang.csv",["MaKH","HoTen","SoDienThoai","Tinh","NgayDangKy","KenhDangKy"],kh,
  "· 900 dòng trùng · 6% thiếu tỉnh · tên tỉnh 5 cách viết")

# --- SanPham: 2000 ---
DM=["Thời trang","Điện tử","Gia dụng","Mỹ phẩm","Thực phẩm","Sách","Thể thao","Mẹ & Bé"]
sp=[]
for i in range(1,2001):
    dm=random.choice(DM); gia=round(random.randint(29,4900)*1000/1000)*1000
    sp.append([f"P{i:05d}",f"{dm} {i:05d}",dm,gia,round(gia*random.uniform(.45,.78))])
w("SanPham.csv",["MaSP","TenSP","DanhMuc","GiaBan","GiaVon"],sp)

# --- HoaDon 600k + ChiTiet ~1.5M ---
gia={r[0]:r[3] for r in sp}
makhs=[r[0] for r in kh]
hd=[];ct=[]
d0=dt.date(2023,1,1); span=(dt.date(2024,12,31)-d0).days
for i in range(1,600001):
    ma=f"O{i:07d}"
    while True:
        d=d0+dt.timedelta(days=random.randint(0,span))
        p=1.0
        if d.month in (11,12): p=1.6
        elif d.month in (6,7): p=1.2
        if d.weekday()>=5: p*=1.25
        if random.random()<p/1.99: break
    tg=dt.datetime.combine(d,dt.time(random.randint(0,23),random.randint(0,59)))
    tt=pick(TT); kenh=random.choice(KENH)
    is_test = 1 if random.random()<.004 else 0                          # 0.4% don test
    n=random.choices([1,2,3,4,5,6],weights=[30,27,19,12,8,4])[0]
    tong=0
    for s in random.sample(sp,n):
        sl=random.choices([1,2,3,4],weights=[66,22,9,3])[0]
        ct.append([ma,s[0],sl,gia[s[0]]]); tong+=sl*gia[s[0]]
    hd.append([ma,random.choice(makhs),tg.strftime("%Y-%m-%d %H:%M:%S"),tong,tt,kenh,is_test])
w("HoaDon.csv",["MaHD","MaKH","ThoiGian","TongTien","TrangThai","Kenh","LaDonTest"],hd,
  "· 22% huỷ/hoàn · 0.4% đơn test")
w("ChiTietHoaDon.csv",["MaHD","MaSP","SoLuong","DonGia"],ct)
tot=len(kh)+len(sp)+len(hd)+len(ct)
print(f"  TỔNG: {tot:,} dòng")
