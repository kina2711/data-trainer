-- DS1 · SalesDB — PostgreSQL
-- Chay theo thu tu duoi day. Sau khi tao xong, nap du lieu tu thu muc csv/
-- bang DBeaver Import Data hoac lenh \copy (vi du o cuoi file).

DROP TABLE IF EXISTS ChiTietHoaDon CASCADE;
DROP TABLE IF EXISTS HoaDon        CASCADE;
DROP TABLE IF EXISTS SanPham       CASCADE;
DROP TABLE IF EXISTS NhanVien      CASCADE;
DROP TABLE IF EXISTS KhachHang     CASCADE;
DROP TABLE IF EXISTS ChiNhanh      CASCADE;

CREATE TABLE ChiNhanh (
    MaChiNhanh   VARCHAR(10)  PRIMARY KEY,
    TenChiNhanh  VARCHAR(100) NOT NULL,
    Tinh         VARCHAR(60)  NOT NULL,
    DiaChi       VARCHAR(200)
);

CREATE TABLE KhachHang (
    MaKH         VARCHAR(10)  PRIMARY KEY,
    HoTen        VARCHAR(100) NOT NULL,       -- PostgreSQL luu UTF-8 san, khong can NVARCHAR
    SoDienThoai  VARCHAR(15),                 -- VARCHAR de giu so 0 dau
    Tinh         VARCHAR(60),
    NgayDangKy   DATE         NOT NULL,
    DiemTichLuy  INT          NOT NULL DEFAULT 0
);

CREATE TABLE NhanVien (
    MaNV         VARCHAR(10)  PRIMARY KEY,
    HoTen        VARCHAR(100) NOT NULL,
    MaChiNhanh   VARCHAR(10)  NOT NULL REFERENCES ChiNhanh(MaChiNhanh),
    ViTri        VARCHAR(60),
    NgayVaoLam   DATE         NOT NULL
);

CREATE TABLE SanPham (
    MaSP           VARCHAR(10)   PRIMARY KEY,
    TenSP          VARCHAR(120)  NOT NULL,
    DanhMuc        VARCHAR(60)   NOT NULL,
    GiaBan         NUMERIC(18,2) NOT NULL CHECK (GiaBan > 0),   -- NUMERIC: tien phai chinh xac
    DangKinhDoanh  BOOLEAN       NOT NULL DEFAULT TRUE
);

CREATE TABLE HoaDon (
    MaHD         VARCHAR(12)   PRIMARY KEY,
    MaKH         VARCHAR(10)   REFERENCES KhachHang(MaKH),  -- cho phep NULL: khach vang lai
    MaNV         VARCHAR(10)   NOT NULL REFERENCES NhanVien(MaNV),
    ThoiGian     TIMESTAMP     NOT NULL,
    TongTien     NUMERIC(18,2) NOT NULL CHECK (TongTien >= 0),
    PhuongThucTT VARCHAR(30)   NOT NULL
);

CREATE TABLE ChiTietHoaDon (
    MaHD     VARCHAR(12)   NOT NULL REFERENCES HoaDon(MaHD),
    MaSP     VARCHAR(10)   NOT NULL REFERENCES SanPham(MaSP),
    SoLuong  INT           NOT NULL CHECK (SoLuong > 0),
    DonGia   NUMERIC(18,2) NOT NULL,   -- gia TAI THOI DIEM BAN, khong tham chieu SanPham.GiaBan
    PRIMARY KEY (MaHD, MaSP)
);

CREATE INDEX IX_HoaDon_ThoiGian ON HoaDon(ThoiGian);
CREATE INDEX IX_HoaDon_MaKH     ON HoaDon(MaKH);

-- Nap du lieu (chay trong psql, sua duong dan cho dung may ban):
-- \copy ChiNhanh      FROM 'csv/ChiNhanh.csv'      CSV HEADER
-- \copy KhachHang     FROM 'csv/KhachHang.csv'     CSV HEADER
-- \copy NhanVien      FROM 'csv/NhanVien.csv'      CSV HEADER
-- \copy SanPham       FROM 'csv/SanPham.csv'       CSV HEADER
-- \copy HoaDon        FROM 'csv/HoaDon.csv'        CSV HEADER
-- \copy ChiTietHoaDon FROM 'csv/ChiTietHoaDon.csv' CSV HEADER
