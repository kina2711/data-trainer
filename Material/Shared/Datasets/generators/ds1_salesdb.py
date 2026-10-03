# -*- coding: utf-8 -*-
"""DS1 · SalesDB — bo du lieu SACH, nho, dung de hoc dung (buoi 2-10, 15-21).
Du nho de doi soat tay, du lon de Excel bat dau cham."""
import csv, random, os, datetime as dt
random.seed(20260101)
ROOT=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT=os.path.join(ROOT, "_data","ds1-salesdb","csv")
os.makedirs(OUT, exist_ok=True)

HO = "Nguyễn Trần Lê Phạm Hoàng Huỳnh Phan Vũ Võ Đặng Bùi Đỗ Hồ Ngô Dương Lý".split()
DEM = "Văn Thị Hữu Đức Minh Ngọc Thanh Quang Xuân Hải Anh Tuấn".split()
TEN = "An Bình Cường Dũng Giang Hà Hùng Khanh Lan Mai Nam Oanh Phúc Quân Sơn Thảo Tuấn Vy Yến Đạt Linh Trang Hạnh Nhung Tú".split()
def ten_nguoi(): return f"{random.choice(HO)} {random.choice(DEM)} {random.choice(TEN)}"

TINH = ["Hà Nội","TP. Hồ Chí Minh","Đà Nẵng","Hải Phòng","Cần Thơ","Bình Dương","Đồng Nai","Khánh Hòa","Nghệ An","Thừa Thiên Huế"]
CN = [("CN01","Chi nhánh Quận 1","TP. Hồ Chí Minh"),("CN02","Chi nhánh Quận 7","TP. Hồ Chí Minh"),
      ("CN03","Chi nhánh Cầu Giấy","Hà Nội"),("CN04","Chi nhánh Hải Châu","Đà Nẵng"),
      ("CN05","Chi nhánh Ninh Kiều","Cần Thơ")]
DM = [("Đồ uống",18000,65000),("Đồ ăn nhẹ",15000,55000),("Bánh ngọt",25000,90000),
      ("Cà phê hạt",120000,450000),("Quà tặng",80000,350000)]

def w(name, header, rows):
    p=os.path.join(OUT,name)
    with open(p,"w",newline="",encoding="utf-8") as f:
        wr=csv.writer(f); wr.writerow(header); wr.writerows(rows)
    print(f"  {name:<24} {len(rows):>8,} dòng")

# --- ChiNhanh ---
chinhanh=[[c,n,t,f"{random.randint(10,300)} {random.choice(['Lê Lợi','Nguyễn Huệ','Trần Phú','Hai Bà Trưng'])}"] for c,n,t in CN]
w("ChiNhanh.csv",["MaChiNhanh","TenChiNhanh","Tinh","DiaChi"],chinhanh)

# --- NhanVien ---
VITRI=["Nhân viên bán hàng","Thu ngân","Pha chế","Quản lý ca","Quản lý chi nhánh"]
nv=[]
for i in range(1,41):
    cn=random.choice(CN)[0]
    ngay=dt.date(2021,1,1)+dt.timedelta(days=random.randint(0,1400))
    nv.append([f"NV{i:03d}",ten_nguoi(),cn,random.choice(VITRI),ngay.isoformat()])
w("NhanVien.csv",["MaNV","HoTen","MaChiNhanh","ViTri","NgayVaoLam"],nv)

# --- SanPham ---
sp=[]
for i in range(1,121):
    dm,lo,hi=random.choice(DM)
    gia=round(random.randint(lo,hi)/1000)*1000
    sp.append([f"SP{i:03d}",f"{dm} {i:03d}",dm,gia,1 if random.random()>.08 else 0])
w("SanPham.csv",["MaSP","TenSP","DanhMuc","GiaBan","DangKinhDoanh"],sp)

# --- KhachHang ---
kh=[]
for i in range(1,3001):
    ngay=dt.date(2022,1,1)+dt.timedelta(days=random.randint(0,1000))
    kh.append([f"KH{i:05d}",ten_nguoi(),f"0{random.choice('35789')}{random.randint(10**7,10**8-1)}",
               random.choice(TINH),ngay.isoformat(),0])
w("KhachHang.csv",["MaKH","HoTen","SoDienThoai","Tinh","NgayDangKy","DiemTichLuy"],kh)

# --- HoaDon + ChiTietHoaDon ---
PTTT=["Tiền mặt","Chuyển khoản","Thẻ","Ví điện tử"]
gia={r[0]:r[3] for r in sp}
hd=[];ct=[];diem={r[0]:0 for r in kh}
d0,d1=dt.date(2024,1,1),dt.date(2024,12,31)
span=(d1-d0).days
for i in range(1,12001):
    ma=f"HD{i:06d}"
    # mua vu: thang 12 va thang 1 cao hon; cuoi tuan cao hon
    while True:
        d=d0+dt.timedelta(days=random.randint(0,span))
        p=1.0
        if d.month in (1,12): p=1.45
        elif d.month in (6,7): p=1.15
        if d.weekday()>=5: p*=1.35
        if random.random()<p/1.96: break
    gio=random.choices([7,8,9,10,11,12,13,14,15,16,17,18,19,20],
                       weights=[6,11,9,7,9,12,8,6,6,7,9,10,7,4])[0]
    tg=dt.datetime.combine(d,dt.time(gio,random.randint(0,59),random.randint(0,59)))
    makh=random.choice(kh)[0] if random.random()>.22 else ""   # 22% khach vang lai
    manv=random.choice(nv)[0]
    n=random.choices([1,2,3,4,5],weights=[34,30,20,11,5])[0]
    chon=random.sample(sp,n); tong=0
    for s in chon:
        sl=random.choices([1,2,3],weights=[70,22,8])[0]
        dg=gia[s[0]]
        ct.append([ma,s[0],sl,dg]); tong+=sl*dg
    hd.append([ma,makh,manv,tg.strftime("%Y-%m-%d %H:%M:%S"),tong,random.choice(PTTT)])
    if makh: diem[makh]+=int(tong/10000)
w("HoaDon.csv",["MaHD","MaKH","MaNV","ThoiGian","TongTien","PhuongThucTT"],hd)
w("ChiTietHoaDon.csv",["MaHD","MaSP","SoLuong","DonGia"],ct)
for r in kh: r[5]=diem[r[0]]
w("KhachHang.csv",["MaKH","HoTen","SoDienThoai","Tinh","NgayDangKy","DiemTichLuy"],kh)
print(f"  TỔNG: {len(chinhanh)+len(nv)+len(sp)+len(kh)+len(hd)+len(ct):,} dòng")
