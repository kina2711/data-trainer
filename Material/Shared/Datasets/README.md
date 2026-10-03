# Bộ dữ liệu chương trình Full-stack Data

Bốn bộ dữ liệu đi theo học viên suốt 72 buổi. Mỗi bộ được dùng lại nhiều lần ở mức độ khó
tăng dần — nhờ đó học viên không mất thời gian làm quen dữ liệu mới mà tập trung vào kỹ thuật mới.

| Bộ | Quy mô | Dung lượng | Dùng ở buổi | Vai trò sư phạm |
|---|---|---|---|---|
| **DS1 · SalesDB** | 41.861 dòng | 1,6 MB | 2–10, 15–21 | Nhỏ đủ để **tính tay biết đáp án đúng** |
| **DS2 · RetailBig** | 2.241.006 dòng | 84 MB | 12–14, 20, 26–33, 37–43 | Có sẵn dữ liệu bẩn — **vấp trong lớp thay vì vấp ở công ty** |
| **DS3 · AppEvents** | 2.000.000 event | 223 MB | 42–43, 51–57, 62–67 | Bán cấu trúc, scale được tới 50 triệu |
| **DS4 · Dữ liệu của bạn** | tuỳ | — | BTVN mọi buổi, Capstone | Yếu tố dự báo tốt nhất cho việc hoàn thành khoá |

---

## DS1 · SalesDB — bộ sạch, dùng để học đúng

Chuỗi cà phê 5 chi nhánh, dữ liệu năm 2024. **Không cài lỗi** — mọi kết quả đối soát tay đều khớp.

```
ds1-salesdb/
  csv/  ChiNhanh · KhachHang · NhanVien · SanPham · HoaDon · ChiTietHoaDon
  ddl/  create_sqlserver.sql · create_postgres.sql
```

Đặc điểm đã cài có chủ đích:
- **Mùa vụ thật:** tháng 1 và 12 cao hơn ~45%, cuối tuần cao hơn ~35% → dùng cho buổi 32 (chuỗi thời gian)
- **22% hoá đơn không có `MaKH`** (khách vãng lai) → dạy `LEFT JOIN` và xử lý `NULL` ở buổi 4
- **`ChiTietHoaDon.DonGia` lưu giá tại thời điểm bán**, không tham chiếu `SanPham.GiaBan` → đúng bài học Slowly Changing Dimension của buổi 1 và 7
- Khoá chính phức hợp `(MaHD, MaSP)` → dạy composite key

Cách nạp: chạy `ddl/create_*.sql` rồi import từ `csv/` bằng DBeaver.

---

## DS2 · RetailBig — bộ bẩn, dùng để học nhanh và học sạch

Bán lẻ đa kênh 2023–2024. **Cố ý cài dữ liệu bẩn** để học viên gặp trong lớp.

```
ds2-retailbig/
  csv/  KhachHang · SanPham · HoaDon · ChiTietHoaDon
  raw/  orders.csv · orders_dirty.csv · orders_dirty_ANSWERS.txt
```

### Dữ liệu bẩn đã cài trong `csv/`

| Vấn đề | Quy mô | Dạy ở buổi |
|---|---|---|
| 900 dòng khách hàng **trùng lặp** | 0,7% | 2 (chiều Duy nhất), 26 (Pandas dedup) |
| Cột `Tinh` viết **5 kiểu khác nhau** cho Hà Nội | ~32% dòng Hà Nội | 2 (chiều Nhất quán), 16 (Power Query) |
| 6% dòng **thiếu** cột `Tinh` | 6% | 2 (chiều Đầy đủ) |
| 22% đơn có trạng thái `cancelled` / `returned` | 22% | 8, 20 — quên lọc là thổi phồng doanh thu |
| 0,4% đơn `LaDonTest = 1` | 0,4% | 1 (mục 14 — bước tìm cột trạng thái) |

### `raw/orders.csv` — tệp thực hành import của **buổi 2**

50.000 dòng, chứa đúng **4 cạm bẫy** mà giáo án buổi 2 mô tả:

| # | Cạm bẫy | Cách nó xuất hiện trong tệp |
|---|---|---|
| 1 | Dấu phẩy nội gián | Địa chỉ dạng `"Số 173 Điện Biên Phủ, Cầu Giấy, Hà Nội"` |
| 2 | Bảng mã | Tên tiếng Việt có dấu, tệp lưu UTF-8 |
| 3 | Mất số 0 đầu | Số điện thoại `0787243484` |
| 4 | Xung đột chuẩn ngày | Định dạng `dd/MM/yyyy` |

### `raw/orders_dirty.csv` — bài Staging Table

Cùng dữ liệu, thêm dòng hỏng. Số liệu **đếm trực tiếp trên tệp**:

```
Tổng số dòng                      : 50.005
OrderID không ép được sang INT    :      4
OrderDate sai định dạng           :      7
Sales không ép được sang DECIMAL  :      9
→ Orders_Rejected                 :     20
→ Qua được ép kiểu                : 49.985
OrderID trùng (trong nhóm đã qua) :  5 mã
Thiếu tên khách (vi phạm NOT NULL):      3
```

Phép kiểm tra bắt buộc ở Bước 6 của giáo án: `49.985 + 20 = 50.005`.
Nếu học viên áp thêm `PRIMARY KEY` và `NOT NULL`, bảng chính chỉ nhận **49.980** dòng —
chênh lệch 5 dòng chính là bài học của **Câu 7** trong phần tự kiểm tra buổi 2.

Đáp án đầy đủ cho giảng viên: `raw/orders_dirty_ANSWERS.txt`

---

## DS3 · AppEvents — bộ lớn, dùng để học quy mô

Log hành vi người dùng, phễu 8 bước, quý 4/2024. Dữ liệu bán cấu trúc (có cột `props_json`).

```
ds3-appevents/
  sample/events.csv   2.000.000 event · 787.903 phiên · 223 MB
```

### Tình huống cài sẵn — nối thẳng với case study buổi 1

App phiên bản **4.2.1 trên Android** rớt mạnh ở bước `checkout` kể từ **03/10**.
Số liệu kiểm chứng trên chính tệp đã sinh:

| Nền tảng | Phiên bản | add_to_cart | checkout | Tỉ lệ đi tiếp |
|---|---|---|---|---|
| android | 4.2.0 | 17.429 | 932 | 5,3% |
| **android** | **4.2.1** | **17.427** | **332** | **1,9%** |
| android | 4.3.0 | 17.369 | 866 | 5,0% |
| ios | 4.2.1 | 11.005 | 590 | 5,4% |
| web | 4.2.1 | 5.042 | 253 | 5,0% |

Bất thường **chỉ xuất hiện ở giao điểm Android × 4.2.1**, không ở nền tảng khác, không ở
phiên bản khác. Học viên phải phân rã theo hai chiều mới tìm ra — đúng những gì Lan làm ở
tuần 8 trong case study, và đúng bài phân tích phễu của buổi 42.

### Sinh bản lớn hơn cho buổi Spark / BigQuery

```bash
python3 generate_ds3.py --rows 50000000 --out /duong/dan/lon
```

50 triệu event chiếm khoảng 5,5 GB. Chỉ sinh khi cần cho buổi 62–67.

---

## Sinh lại toàn bộ

```bash
python3 generate_ds1.py          # DS1 · ~5 giây
python3 generate_orders_csv.py   # orders.csv + orders_dirty.csv · ~10 giây
python3 verify_orders_dirty.py   # đếm lại và sinh đáp án từ số liệu thật
python3 generate_ds2.py          # DS2 · ~60 giây
python3 generate_ds3.py          # DS3 2 triệu event · ~90 giây
```

Mọi script dùng seed cố định — chạy lại cho ra **đúng cùng một bộ dữ liệu**, nên đáp án
của giảng viên luôn khớp với dữ liệu học viên có.

---

## Giới hạn cần biết

- Đây là **dữ liệu tổng hợp**, không phải dữ liệu doanh nghiệp thật. Phân phối được thiết kế
  để bộc lộ đúng các bài học, không phản ánh một thị trường cụ thể nào.
- Tên người và số điện thoại được sinh ngẫu nhiên từ bảng âm tiết, **không tương ứng với
  người thật**. Vẫn nên đối xử với chúng như dữ liệu cá nhân khi thực hành mục 17 của buổi 1.
- DS3 mặc định 2 triệu event là bản **mẫu**. Các buổi Big Data cần sinh bản lớn hơn.
