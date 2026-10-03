# Trạng thái nguồn bổ sung offline

Ngày lập: 2026-09-27  
Phạm vi: 11 thư mục dưới `/media/kina2711/DATA/` do owner cung cấp  
Trạng thái: source manifest đã tạo; chưa coi nguồn nào là đã đọc sâu

## Kết quả chuẩn hóa

| Chỉ số | Giá trị |
|---|---:|
| Tệp đã kiểm kê | 2.991 |
| Source identity theo SHA-256 | 2.662 |
| Alias trùng nội dung | 329 |
| Nguồn vào hàng đợi đọc | 676 |
| Companion code/lab/artifact | 68 |
| Cần phân loại thủ công | 48 |
| Runtime/binary bị loại | 1.864 |
| File hỏng, rỗng hoặc tải dở bị từ chối | 6 |
| Nguồn có rủi ro provenance, chỉ dùng private | 10 |
| Candidate chưa ánh xạ được module | 28 |

`Source identity` là một nội dung duy nhất theo SHA-256. Các đường dẫn chứa cùng nội dung được giữ
trong `aliases`; không có file nguồn nào bị xóa.

## Hàng đợi xử lý

| Batch | Phạm vi | Đọc | Companion | Loại | Triage/Từ chối |
|---|---|---:|---:|---:|---:|
| `B01-DE-FOUNDATION` | Nền tảng DE | 7 | 0 | 0 | 0 |
| `B02-DE-DSA` | DSA | 140 | 4 | 0 | 1 |
| `B03-DE-DWH-DATALAKE` | Database, DWH, Data Lake | 24 | 0 | 0 | 0 |
| `B04-DE-ETL-SPARK` | ETL, Spark và lab | 56 | 51 | 1.862 | 1 |
| `B05-DE-KAFKA` | Kafka course | 365 | 0 | 0 | 47 |
| `B06-DA-STATISTICS` | Thống kê | 1 | 0 | 0 | 0 |
| `B07-CROSS-DOMAIN` | Banking, Marketing, Game | 9 | 0 | 0 | 0 |
| `B08-MIXED-BOOKS` | Kho sách hỗn hợp | 39 | 1 | 0 | 0 |
| `B09-MIXED-LIBRARY` | Library tổng hợp | 19 | 12 | 2 | 5 |
| `B10-DE-BOOKS-2025` | Sách DE 2025 | 15 | 0 | 0 | 0 |
| `B11-DE-BOOKS-ARCHIVE` | Sách DE lưu trữ | 1 | 0 | 0 | 0 |

## Phương thức trích xuất

| Phương thức | Số source identity |
|---|---:|
| Đọc PDF trực tiếp | 178 |
| PDF cần hybrid extraction | 35 |
| PDF cần OCR | 29 |
| Text/note trực tiếp | 75 |
| Transcript trực tiếp | 223 |
| Video kiểm chứng theo transcript | 112 |
| Media cần transcription | 21 |
| Document ngoài PDF | 3 |
| Code/lab review | 47 |
| Companion artifact review | 21 |

## Quy tắc ánh xạ hiện tại

Candidate module được suy ra từ thư mục, tên file hoặc metadata nhúng trong PDF. Candidate chỉ dùng
để xếp hàng đọc; nó **không phải bằng chứng nội dung**. Mỗi mapping chỉ được chuyển thành
`supports`, `qualifies`, `contradicts` hoặc `example` sau khi nguồn được đọc và có locator.

Các module chưa có candidate từ **kho bổ sung** gồm `DA-M01`, `DA-M11`, `DE-M12`, `DE-M13`,
`DE-M18`, `DE-M19`, `DE-M22` và `DE-M29`. Điều này không đồng nghĩa các module thiếu nguồn, vì
source plan chính đã có nguồn khác; nó chỉ mô tả phần bổ sung offline này.

## Ràng buộc quyền sử dụng

- Toàn bộ nguồn bổ sung mặc định là private.
- Sở hữu file không đồng nghĩa có quyền phân phối.
- File có dấu hiệu `Z-Library`, `libgen` hoặc `OceanofPDF` chỉ được dùng để nghiên cứu nội bộ;
  Reference công khai không sao chép nội dung biểu đạt dài và phải dẫn tác phẩm/nhà xuất bản gốc.
- Web và Artifact không được phục vụ file nguồn thương mại.

## Trình tự tiếp theo

1. Đọc `B01-DE-FOUNDATION`, xác minh title/author/edition và tạo source note có page locator.
2. Đọc `B02-DE-DSA` theo bounded retrieval, không tải toàn bộ 140 PDF vào một lần.
3. Đọc `B03-DE-DWH-DATALAKE`, ưu tiên transcript/note rồi kiểm chứng lại video/PDF.
4. Đọc `B04-DE-ETL-SPARK`; giữ 51 lab làm companion và bỏ qua 1.862 file runtime.
5. Đọc `B05-DE-KAFKA` theo transcript; chỉ mở video tại timestamp cần xác minh.
6. Xử lý các batch DA và kho sách hỗn hợp theo module objective tương ứng.

