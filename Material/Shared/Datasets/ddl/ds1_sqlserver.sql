/* DS1 · SalesDB — SQL Server
   Chay theo thu tu: bang khong co khoa ngoai truoc.
   Sau khi tao xong, dung DBeaver Import Data hoac BULK INSERT tu thu muc csv/. */
IF DB_ID('SalesDB') IS NULL CREATE DATABASE SalesDB;
GO
USE SalesDB;
GO
IF OBJECT_ID('ChiTietHoaDon') IS NOT NULL DROP TABLE ChiTietHoaDon;
IF OBJECT_ID('HoaDon')        IS NOT NULL DROP TABLE HoaDon;
IF OBJECT_ID('SanPham')       IS NOT NULL DROP TABLE SanPham;
IF OBJECT_ID('NhanVien')      IS NOT NULL DROP TABLE NhanVien;
IF OBJECT_ID('KhachHang')     IS NOT NULL DROP TABLE KhachHang;
IF OBJECT_ID('ChiNhanh')      IS NOT NULL DROP TABLE ChiNhanh;
GO
CREATE TABLE ChiNhanh (
    MaChiNhanh   VARCHAR(10)   NOT NULL PRIMARY KEY,
    TenChiNhanh  NVARCHAR(100) NOT NULL,
    Tinh         NVARCHAR(60)  NOT NULL,
    DiaChi       NVARCHAR(200) NULL
);
CREATE TABLE KhachHang (
    MaKH         VARCHAR(10)   NOT NULL PRIMARY KEY,
    HoTen        NVARCHAR(100) NOT NULL,     -- NVARCHAR: giu dau tieng Viet
    SoDienThoai  VARCHAR(15)   NULL,         -- VARCHAR: giu so 0 dau
    Tinh         NVARCHAR(60)  NULL,
    NgayDangKy   DATE          NOT NULL,
    DiemTichLuy  INT           NOT NULL DEFAULT 0
);
CREATE TABLE NhanVien (
    MaNV         VARCHAR(10)   NOT NULL PRIMARY KEY,
    HoTen        NVARCHAR(100) NOT NULL,
    MaChiNhanh   VARCHAR(10)   NOT NULL REFERENCES ChiNhanh(MaChiNhanh),
    ViTri        NVARCHAR(60)  NULL,
    NgayVaoLam   DATE          NOT NULL
);
CREATE TABLE SanPham (
    MaSP           VARCHAR(10)   NOT NULL PRIMARY KEY,
    TenSP          NVARCHAR(120) NOT NULL,
    DanhMuc        NVARCHAR(60)  NOT NULL,
    GiaBan         DECIMAL(18,2) NOT NULL CHECK (GiaBan > 0),   -- DECIMAL: tien phai chinh xac
    DangKinhDoanh  BIT           NOT NULL DEFAULT 1
);
CREATE TABLE HoaDon (
    MaHD           VARCHAR(12)   NOT NULL PRIMARY KEY,
    MaKH           VARCHAR(10)   NULL REFERENCES KhachHang(MaKH),  -- NULL: khach vang lai
    MaNV           VARCHAR(10)   NOT NULL REFERENCES NhanVien(MaNV),
    ThoiGian       DATETIME2(0)  NOT NULL,
    TongTien       DECIMAL(18,2) NOT NULL CHECK (TongTien >= 0),
    PhuongThucTT   NVARCHAR(30)  NOT NULL
);
CREATE TABLE ChiTietHoaDon (
    MaHD      VARCHAR(12)   NOT NULL REFERENCES HoaDon(MaHD),
    MaSP      VARCHAR(10)   NOT NULL REFERENCES SanPham(MaSP),
    SoLuong   INT           NOT NULL CHECK (SoLuong > 0),
    DonGia    DECIMAL(18,2) NOT NULL,   -- gia TAI THOI DIEM BAN, khong tham chieu SanPham.GiaBan
    CONSTRAINT PK_ChiTietHoaDon PRIMARY KEY (MaHD, MaSP)
);
GO
CREATE INDEX IX_HoaDon_ThoiGian ON HoaDon(ThoiGian);
CREATE INDEX IX_HoaDon_MaKH     ON HoaDon(MaKH);
GO
