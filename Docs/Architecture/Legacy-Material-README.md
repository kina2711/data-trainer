# DANH MỤC CHƯƠNG TRÌNH ĐÀO TẠO DATA

**2 chương trình · 525 bài · Data Analyst 85 bài và Data Engineer 440 bài**

| | |
|---|---|
| **Phiên bản** | 5.0 · `DRAFT` |
| **Cập nhật** | 24/09/2026 |
| **Thay thế** | Danh mục 9 chương trình v3.0 — xem [`archive/`](../archive/) |
| **Thay đổi mới nhất** | Data Engineer bản gộp 440 bài thay bản cũ 102 bài; Analytics Engineer đã gộp vào Data Engineer và ngừng làm chương trình riêng |

---

## 1. Chương trình

| Chương trình | Bài | Module | Giờ lớp | Thời gian | Đầu ra |
|---|---|---|---|---|---|
| [**Data Analyst**](data-analyst/roadmap/roadmap.md) | 85 | 11 | 170 | 7–10 tháng | DA · BI Analyst · Product Analyst |
| [**Data Engineer**](data-engineer/roadmap/roadmap.md) | 440 | 29 | 880 | 29–36 tháng | DE · Analytics Engineer · Platform Engineer |

**Bắt đầu từ con số 0.** Không yêu cầu kiến thức đầu vào ở cả hai chương trình.

**Vì sao Analytics Engineer không còn là chương trình riêng.** Bốn nhóm năng lực đặc trưng của vai
trò đó — tầng ngữ nghĩa và kỹ thuật chỉ số, sản phẩm dữ liệu và tự phục vụ, chất lượng và độ tin
cậy dữ liệu, siêu dữ liệu và quản trị — nay là bốn module bắt buộc trong Data Engineer, tổng 70 bài
ở Phase 5 và Phase 7. Bản đồ và lý do ở [`.data-2026/build/ade-module-map.md`](../.data-2026/build/ade-module-map.md).

---

## 2. Chọn chương trình nào

| Bạn thích | Chọn |
|---|---|
| Trả lời câu hỏi kinh doanh, làm dashboard, thuyết trình | **Data Analyst** |
| Xây mô hình dữ liệu, đặt chuẩn, để người khác dùng lại | **Data Engineer**, dừng sau Phase 5 hoặc Phase 7 |
| Xây hệ thống, đường ống, hạ tầng, vận hành sản xuất | **Data Engineer**, đi hết mười phase |

**Ba câu hỏi phân loại nhanh:**

1. *Bạn muốn người khác dùng kết quả của bạn, hay dùng hệ thống của bạn?* Kết quả → DA. Hệ thống → DE.
2. *Bạn ngại viết code không?* Ngại → DA. Không ngại → DE.
3. *Bạn chấp nhận bị gọi dậy lúc 3 giờ sáng khi hệ thống hỏng không?* Không → DA, hoặc DE dừng ở Phase 7. Có → DE đầy đủ.

**Data Engineer có điểm dừng có ý nghĩa.** Hết Phase 5 (bài 202) là năng lực mô hình hoá và tầng
ngữ nghĩa; hết Phase 7 (bài 308) là năng lực Analytics Engineer đầy đủ cộng kỹ thuật dữ liệu theo
lô; từ Phase 8 trở đi là hệ phân tán, hạ tầng và vận hành.

---

## 3. Phần chung giữa hai chương trình

Hai chương trình độc lập nhưng chồng lấn ở nền tảng dữ liệu. Bảng dưới cho biết mỗi chủ đề được
dạy sâu tới đâu ở từng chương trình:

| Chủ đề | Data Analyst | Data Engineer |
|---|---|---|
| Excel | 11 bài | — |
| SQL | 14 bài | 20 bài |
| Nội bộ cơ sở dữ liệu, giao dịch, phục hồi | — | 16 bài |
| Mô hình hoá dữ liệu | 7 bài | 16 bài |
| Tầng ngữ nghĩa và kỹ thuật chỉ số | — | 20 bài |
| Sản phẩm dữ liệu và tự phục vụ | — | 18 bài |
| Thống kê | 8 bài | — |
| Trực quan hoá · BI | 9 bài | — |
| Phân tích sản phẩm · thí nghiệm A/B | 14 bài | — |
| Python | 8 bài | 20 bài |
| Nền tảng máy tính, hệ điều hành, mạng | trong 1 bài | 44 bài |
| Nạp dữ liệu và tích hợp | trong 2 bài | 16 bài |
| Biến đổi, dbt, điều phối | — | 28 bài |
| Chất lượng và độ tin cậy dữ liệu | trong 2 bài | 18 bài |
| Siêu dữ liệu, dòng dõi, quản trị | — | 16 bài |
| Định dạng tệp, định dạng bảng mở | — | 14 bài |
| Hệ phân tán, Kafka, CDC, Spark | — | 52 bài |
| Đám mây, vùng chứa, hạ tầng khai báo | — | 28 bài |
| Quan sát được, tin cậy, bảo mật | — | 16 bài |
| Thiết kế hệ thống | — | 16 bài |
| Kỹ thuật AI, mức `C` | — | 10 bài |
| Giao tiếp, nghề nghiệp | 6 bài | 10 bài |

**Chủ ý của việc lặp:** cùng một chủ đề được cắt gọt khác nhau theo vai trò. SQL cho DA nhấn vào
trả lời câu hỏi kinh doanh; SQL cho DE nhấn thêm vào cơ chế bên dưới, kế hoạch thực thi, chỉ mục,
giao dịch và tác động lên hệ nguồn.

---

## 4. Khung chung của cả hai

**Cấu trúc.** Chương trình → Module → Bài. Bài đánh số liên tục trong mỗi chương trình.

**Một bài** = 2 giờ trên lớp + 2–2,4 giờ tự làm. Bốn dạng: `LT` lý thuyết · `TH` thực hành · `DA` dự án · `KT` kiểm tra.

**Mỗi bài khai báo chín mục:** Prerequisites · In-class · Learn · Outcome · Đánh giá · Lab · Pitfalls · Self-study · Done when.

**Cổng kiểm tra** là điều kiện cứng, không phải mốc tham khảo: Data Analyst có 4 cổng, Data Engineer
có 10. Không qua cổng thì học lại phần tương ứng.

**Bảo vệ tốt nghiệp** trước hội đồng ba người, không phải bài trắc nghiệm.

**Bộ dữ liệu dùng chung** cho cả ba chương trình:

| Mã | Tên | Quy mô | Vai trò |
|---|---|---|---|
| `DS1` | SalesDB — 8 bảng chuẩn hoá | 42.000 dòng | Sạch, nhỏ đủ để đối soát tay |
| `DS2` | RetailBig — bán lẻ | 2,2 triệu dòng | Bẩn có chủ đích, 7 loại lỗi cài sẵn |
| `DS3` | AppEvents — sự kiện ứng dụng | 5 triệu dòng | Có bất thường ẩn ở giao hai chiều |
| `DS4` | orders.csv | 50.000 dòng | Bốn bẫy nhập liệu |

Sinh bằng script có hạt giống cố định — chạy lại luôn ra đúng cùng dữ liệu.

---

## 5. Trạng thái xây dựng

| | Data Analyst | Data Engineer |
|---|---|---|
| Cấu trúc module | đã xong | đã xong |
| Đặc tả từng bài | 85/85 | 440/440 |
| Cổng có rubric | 4/4 | 10/10 · thang điểm nằm trong đặc tả bài |
| Giáo án chi tiết | 0/85 | 0/440 |
| Slide · PDF | 0/85 | 0/440 |
| Đề thi cổng | chưa soạn | chưa soạn |
| Môi trường lab | không cần thêm | chưa chuẩn bị |

**Đọc bảng này thẳng thắn.** Cả 525 bài đã có đặc tả chín mục: học gì, làm được gì, đánh giá thế
nào, thực hành gì, lỗi nào hay gặp, và đạt khi nào. Cả 14 cổng đã có cấu trúc đề cùng thang điểm.
Đó là **bản thiết kế chương trình**.

Cái còn thiếu là **vật liệu giảng dạy**: chưa bài nào có giáo án chi tiết, chưa có slide, chưa có
PDF, chưa có ngân hàng đề và ngân hàng bài tập. Môi trường lab cho Data Engineer chưa được chuẩn bị
và chưa có ngân sách; nó chặn phần lớn Phase 8 tới Phase 10.

Nói ngắn gọn: **có thể lên kế hoạch đào tạo từ tài liệu này, chưa thể mở lớp từ nó.**

---

## 6. Cách tổ chức thư mục

```
material/
├── README.md                          danh mục này
├── data-analyst/                      Data Analyst
│   ├── roadmap/roadmap.md             ← NGUỒN DUY NHẤT của chương trình
│   ├── ref/                           tài liệu tham khảo (bổ sung sau)
│   └── curriculum/
│       ├── module_1-.../
│       │   ├── roadmap/roadmap.md     sinh ra từ roadmap gốc
│       │   ├── ref/
│       │   └── curriculum/
│       │       └── lesson_001_.../
│       │           ├── note.md        ghi chú chi tiết    ← soạn tay
│       │           ├── quiz.md        câu hỏi trắc nghiệm ← soạn tay
│       │           ├── homework.md    bài tập về nhà      ← soạn tay
│       │           ├── slides.md      slide Marp          ← soạn tay
│       │           ├── *.drawio       sơ đồ khung
│       │           └── material/      code, dữ liệu mẫu   ← soạn tay
│       └── module_2-.../
└── data-engineer/                     Data Engineer
```

**Nguồn duy nhất** là `material/<chương-trình>/roadmap/roadmap.md`. Sửa số bài hay tên bài ở đó,
rồi chạy `make scaffold` để cập nhật roadmap cấp module và tạo khung cho bài mới.
Lệnh này **không ghi đè** file đã có nội dung.

---

## 7. Bước tiếp theo

Thứ tự ưu tiên đề xuất:

1. **Viết giáo án cho 5 bài đầu của một chương trình** — đủ để chạy thử một lớp nhỏ và kiểm chứng thiết kế trước khi viết tiếp.
2. **Soạn đề cổng 1** của chương trình đó.
3. **Giải ràng buộc môi trường lab** cho Data Engineer — đây là việc tổ chức, không phải việc soạn nội dung, và nó chặn từ Phase 8 trở đi.

Kho lưu trữ [`archive/v3-danh-muc-9-chuong-trinh/`](../archive/v3-danh-muc-9-chuong-trinh/) chứa ba
giáo án chi tiết và ba bộ slide viết theo cấu trúc cũ — khai thác lại được khi viết giáo án mới.

---

## PHỤ LỤC Z — Nguồn đối chiếu

Ba roadmap được đối chiếu với các nguồn công khai để phần nghề nghiệp không dựa vào phỏng đoán:

| Nguồn | Dùng cho |
|---|---|
| [data-road-map-by-roles](https://github.com/tunguyenn99/data-road-map-by-roles) | Cấu trúc ma trận năm cấp độ · mức lương tham chiếu VN · danh sách công ty tuyển · kênh tìm việc · tài nguyên học |
| [ITViec — Thị trường IT Việt Nam Q2/2025](https://itviec.com/blog/vietnam-it-job-market-q2-2025-python-ai-see-strong-growth/) | Số liệu nhu cầu tuyển dụng, dẫn lại qua nguồn trên |
| [State of Analytics Engineering — dbt Labs](https://www.getdbt.com/resources/state-of-analytics-engineering-2025) | Ba trách nhiệm đang mở rộng của Analytics Engineer |
| `ROADMAP_DATA_ENGINEER_0_TO_ARCHITECT.md` (tài liệu người dùng cung cấp) | Mức thành thạo A/B/C · thang đánh giá 1–5 · chuẩn ghi chú 9 phần · bảng 7 hệ CSDL · so sánh 4 orchestrator · RabbitMQ so Kafka · hợp đồng 11 trường · trọng số chấm |
| `ROADMAP_ANALYTICS_ENGINEER_0_TO_ARCHITECT.md` (tài liệu người dùng cung cấp) | Đặc tả chỉ số 13 trường · phân loại cộng được/bán cộng được/không cộng được · 3 loại fact · 7 loại dimension · 40 bài SQL · bảng ranh giới vai trò |

**Giới hạn cần nói rõ.** Số liệu lương và thị trường được **trích lại, chưa kiểm chứng độc lập**.
Dùng làm mốc tham khảo, không dùng làm căn cứ đàm phán tuyệt đối. Repo nguồn không có roadmap
riêng cho Data Engineer — phần lương của chương trình DE lấy từ bảng BI Engineer và có ghi chú rõ.
