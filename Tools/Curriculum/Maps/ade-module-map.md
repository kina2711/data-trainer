# ADE v1.0 — bản đồ module chương trình gộp Analytics Engineer và Data Engineer

Nguồn: `/home/kina2711/PROJECT/roadmap-de/about me/06_LO_TRINH_CHI_TIET_THEO_MODULE/`
(29 hợp đồng học tập: 24 core cộng 5 bridge) và `05_LO_TRINH_HOC_TAP_30_THANG.md` (8 phase).
Căn cứ gộp: [AE_DE_COVERAGE_AUDIT.md](../../../roadmap-de/about%20me/06_LO_TRINH_CHI_TIET_THEO_MODULE/AE_DE_COVERAGE_AUDIT.md),
kết luận rằng sau khi thêm 11B, 11C, 14B, 14C, 14D thì **một core chung phủ đủ cả hai vai**.

Quy đổi: bài thường 2 giờ trên lớp + 2,4 giờ tự học = 4,4 giờ. Mười bài cổng dài 120–180 phút và không có bài tự học.

---

## 1. Vì sao khung 30 tháng của bản nguồn không dùng lại được nguyên vẹn

Bản nguồn xếp 9 module vào Phase 5 và ghi rằng 5 bridge "không tạo thêm một phase thời gian độc lập".
Đo theo độ dày hợp đồng thì khẳng định đó không đứng vững:

| | Số dòng hợp đồng | Tỉ lệ nội dung | Tỉ lệ thời gian được cấp |
|---|---:|---:|---:|
| Phase 5 gốc (M11 → M14D, 9 module) | 2.017 | **49%** | 4/30 tháng = **13%** |
| 5 bridge module (phần bù AE) | 1.331 | 33% | không được cấp riêng |
| Toàn chương trình | 4.076 | 100% | 30 tháng |

Nên bản gộp **tách Phase 5 gốc thành ba phase** (P5, P6, P7 dưới đây) và giữ nguyên thứ tự phụ thuộc.
Không module nào bị bỏ, không module nào đổi vị trí trong đồ thị phụ thuộc.

---

## 2. Bản đồ 29 module

Cột **Vai** ghi module phục vụ vai nào theo audit: `AE` phần bù Analytics Engineer,
`DE` phần riêng Data Engineer, `chung` là nền bắt buộc cho cả hai.

| Phase | Module | Tên | Vai | Mức | Bài |
|---|---|---|---|---|---:|
| 1 | M1 | Engineering thinking, Git and debugging | chung | | 12 |
| 1 | M2 | Python for production | chung | `A` | 20 |
| 1 | M3 | Data structures and algorithms for systems | chung | | 12 |
| 2 | M4 | Computer architecture and the performance model | chung | | 16 |
| 2 | M5 | Operating systems, concurrency and Linux | chung | `A` | 16 |
| 2 | M6 | Networking from packet to API | chung | | 12 |
| 3 | M7 | Software design and delivery | chung | | 12 |
| 3 | M8 | Backend and API engineering | DE | | 12 |
| 4 | M9 | Relational theory and SQL execution | chung | `A` | 20 |
| 4 | M10 | Storage engine and database operations | chung | `A` | 16 |
| 5 | M11 | Data modeling - operational, analytical, domain | chung | `A` | 16 |
| 5 | M11B | Semantic layer and metrics engineering | **AE** | `A` | 20 |
| 5 | M11C | Analytical data product and self-service | **AE** | | 18 |
| 6 | M12 | OLAP internals | chung | | 14 |
| 6 | M13 | File, serialization and table formats | chung | `A` | 14 |
| 7 | M14B | Data ingestion and integration | chung | `A` | 16 |
| 7 | M14 | ELT, dbt and orchestration | chung | `A` | 28 |
| 7 | M14C | Data quality and reliability | **AE** | `A` | 18 |
| 7 | M14D | Metadata, catalog, lineage and governance | **AE** | `B` | 16 |
| 8 | M15 | Distributed systems fundamentals | DE | | 12 |
| 8 | M16 | Kafka and event streaming | DE | `A` | 14 |
| 8 | M17 | Change data capture internals | DE | `B` | 10 |
| 8 | M18 | Spark, Flink and compute engines | DE | `A` | 16 |
| 9 | M19 | Cloud abstractions before service names | chung | `A` | 12 |
| 9 | M20 | Docker, infrastructure as code and Kubernetes | DE | `A`/`B` | 16 |
| 9 | M21 | Observability, reliability and security | chung | `A` | 16 |
| 10 | M22 | System design progression | chung | | 16 |
| 10 | M23 | Modern AI engineering, bounded | chung | `C` | 10 |
| 10 | M24 | Staff and principal trajectory | chung | | 10 |
| | | **Tổng** | | | **440** |

**440 bài · 29 module · 884,5 giờ trên lớp + 1.032 giờ tự học = ~1.916,5 giờ.**
Ở 15 giờ/tuần là ~29 tháng; ở 12 giờ/tuần là ~36 tháng.

Bản nguồn ước lượng 30 tháng cho phần DE. Bản gộp cộng thêm 72 bài thuộc phần bù AE
(M11B, M11C, M14C, M14D), nên mốc thực tế là **33–36 tháng ở nhịp 12 giờ/tuần**.

---

## 3. Mười phase và cổng kiểm tra

| Phase | Tên | Module | Bài | Cổng |
|---|---|---|---:|---|
| 1 | Engineering foundation | M1 · M2 · M3 | 44 | Gate 1 |
| 2 | Machine, operating system and network | M4 · M5 · M6 | 44 | Gate 2 |
| 3 | Software and backend engineering | M7 · M8 | 24 | Gate 3 |
| 4 | SQL and database internals | M9 · M10 | 36 | Gate 4 |
| 5 | Modeling, semantics and analytical product | M11 · M11B · M11C | 54 | Gate 5 |
| 6 | Analytical storage and query engines | M12 · M13 | 28 | Gate 6 |
| 7 | Ingestion, transformation, quality and governance | M14B · M14 · M14C · M14D | 78 | Gate 7 |
| 8 | Distributed systems, streaming and compute | M15 · M16 · M17 · M18 | 52 | Gate 8 |
| 9 | Cloud, platform and production operations | M19 · M20 · M21 | 44 | Gate 9 |
| 10 | System design, AI boundary and trajectory | M22 · M23 · M24 | 36 | Bảo vệ tốt nghiệp |

Phase 5 và Phase 7 là hai phase nặng nhất và cũng là hai phase chứa toàn bộ phần bù AE.
Đó là hệ quả trực tiếp của việc gộp, không phải lỗi phân bổ.

### 3.1 Chi tiết từng phase

Mỗi phase có một câu hỏi trung tâm; cổng cuối phase kiểm đúng câu hỏi đó chứ kiểm lại toàn bộ nội dung.
Cột *chế độ hỏng* ghi cách hỏng đặc trưng của phase, tức cách một người học qua phase mà không đạt năng lực.

**Phase 1 · Engineering foundation** — bài 1–44 · M1 (1–12) · M2 (13–32) · M3 (33–44) · Gate 1

- *Câu hỏi trung tâm:* viết được phần mềm người khác chạy lại được, và chọn cấu trúc dữ liệu bằng số đo.
- *Năng lực mới:* phát biểu bài toán sáu phần; Git và gỡ lỗi có phương pháp; Python đóng gói được, kiểm thử được, quan sát được; bốn mô hình đồng thời; độ phức tạp kiểm bằng thực nghiệm.
- *Cổng 1 kiểm:* giải thích một lựa chọn cấu trúc dữ liệu và chứng minh bằng phép đo.
- *Chế độ hỏng:* viết script chạy được trên máy mình rồi gọi là xong.

**Phase 2 · Machine, operating system and network** — bài 45–88 · M4 (45–60) · M5 (61–76) · M6 (77–88) · Gate 2

- *Câu hỏi trung tâm:* một thao tác chậm thì chậm ở đâu, và biết bằng cách nào.
- *Năng lực mới:* thứ bậc chi phí bộ nhớ; phân loại Flynn cùng SIMD, MIMD và SPMD; hệ điều hành ở mức chẩn đoán; vào ra bất đồng bộ từ nhân tới môi trường chạy; mạng từ gói tin tới giao diện lập trình.
- *Cổng 2 kiểm:* dự đoán thứ bậc chi phí trước khi đo, rồi giải thích chênh lệch bằng cơ chế.
- *Chế độ hỏng:* đổi phần cứng hoặc cấu hình trước khi có giả thuyết.

**Phase 3 · Software and backend engineering** — bài 89–112 · M7 (89–100) · M8 (101–112) · Gate 3

- *Câu hỏi trung tâm:* một dịch vụ đúng dưới đồng thời và dưới lỗi trông như thế nào.
- *Năng lực mới:* ranh giới module và hợp đồng; kiểm thử theo tầng; vòng đời một yêu cầu; ranh giới giao dịch; luỹ đẳng; chịu lỗi; quan sát được.
- *Cổng 3 kiểm:* một dịch vụ giữ đúng bất biến khi có đồng thời và khi có lỗi.
- *Chế độ hỏng:* coi mã chạy đúng trên đường thuận lợi là mã đúng.

**Phase 4 · SQL and database internals** — bài 113–148 · M9 (113–132) · M10 (133–148) · Gate 4

- *Câu hỏi trung tâm:* câu lệnh chạy ra sao bên trong, và hệ giữ dữ liệu bền vững bằng cách nào.
- *Năng lực mới:* đại số quan hệ và ba giá trị chân lý; hàm cửa sổ; đọc kế hoạch thực thi; cây B và cây hợp nhất; nhật ký ghi trước; điều khiển đồng thời và mức cô lập; sao lưu cùng phục hồi.
- *Cổng 4 kiểm:* truy một phép ghi từ đầu tới cuối và bảo vệ một lựa chọn mức cô lập.
- *Chế độ hỏng:* chọn mức cô lập theo tên chứ theo hiện tượng bất thường cần chặn.

**Phase 5 · Modeling, semantics and analytical product** — bài 149–202 · M11 (149–164) · M11B (165–184) · M11C (185–202) · Gate 5

- *Câu hỏi trung tâm:* một con số có nghĩa duy nhất, và người khác dùng được nó mà không hỏi ai.
- *Năng lực mới:* **phần bù AE bắt đầu ở đây.** Hạt như công cụ thiết kế; chiều biến đổi chậm; hợp đồng chỉ số sáu phần; đồ thị ngữ nghĩa; chứng minh không đếm trùng; ma trận tương thích; sản phẩm dữ liệu và phép thử khả dụng theo tác vụ.
- *Cổng 5 kiểm:* bảo vệ một định nghĩa chỉ số trước chất vấn và trình bằng chứng người khác dùng được.
- *Chế độ hỏng:* cài công cụ tầng ngữ nghĩa rồi khai báo chỉ số theo cột có sẵn, không có hợp đồng và không đối soát.

**Phase 6 · Analytical storage and query engines** — bài 203–230 · M12 (203–216) · M13 (217–230) · Gate 6

- *Câu hỏi trung tâm:* vì sao engine phân tích nhanh, và tệp nào thuộc bảng tại thời điểm nào.
- *Năng lực mới:* bốn phần đóng góp làm hệ cột nhanh, đo riêng từng phần; ba tầng song song lồng nhau; định dạng tuần tự hoá và ma trận tương thích; giao thức chốt giao dịch của định dạng bảng mở; bảo trì an toàn.
- *Cổng 6 kiểm:* giải thích một chuỗi siêu dữ liệu thật và sống sót qua ghi đồng thời.
- *Chế độ hỏng:* dùng chữ ACID thay cho mô tả cơ chế, và so lần chạy đệm nóng với lần chạy đệm lạnh.

**Phase 7 · Ingestion, transformation, quality and governance** — bài 231–308 · M14B (231–246) · M14 (247–274) · M14C (275–292) · M14D (293–308) · Gate 7

- *Câu hỏi trung tâm:* dữ liệu đi từ nguồn tới người dùng mà không mất, không trùng, và chứng minh được điều đó.
- *Năng lực mới:* hợp đồng trích xuất; hạ cánh nguyên tử và thứ tự mốc tiến độ; mô hình tăng dần cùng chứng minh bảy phần; **phần bù AE thứ hai** gồm kỹ thuật chất lượng, thang đối soát, cam kết dịch vụ dữ liệu, vòng đời sự cố, siêu dữ liệu, dòng dõi và quản trị.
- *Cổng 7 kiểm:* bảo vệ một khẳng định về dòng dõi và chứng minh tính đầy đủ bằng đối soát.
- *Chế độ hỏng:* coi mọi việc xanh là bằng chứng dữ liệu đầy đủ.

**Phase 8 · Distributed systems, streaming and compute** — bài 309–360 · M15 (309–320) · M16 (321–334) · M17 (335–344) · M18 (345–360) · Gate 8

- *Câu hỏi trung tâm:* hệ nhiều nút hỏng một phần thì dữ liệu còn đúng không.
- *Năng lực mới:* nhất quán và định lý đánh đổi; đồng thuận ở mức dùng được; nhật ký sự kiện phân tán; bắt thay đổi từ nhật ký giao dịch; engine tính toán phân tán với MIMD phân tán, tác vụ theo khuôn mẫu SPMD và song song lồng nhau.
- *Cổng 8 kiểm:* thiết kế một đường dòng chảy có ngữ nghĩa giao nhận nêu rõ ranh giới, và phục hồi sau hỏng một phần.
- *Chế độ hỏng:* tuyên bố đúng một lần mà không nêu ranh giới nguồn, đích và giả định lỗi.

**Phase 9 · Cloud, platform and production operations** — bài 361–404 · M19 (361–372) · M20 (373–388) · M21 (389–404) · Gate 9

- *Câu hỏi trung tâm:* đưa hệ lên môi trường thật và giữ nó chạy, có bằng chứng.
- *Năng lực mới:* trừu tượng đám mây trước tên dịch vụ; đóng gói và hạ tầng khai báo; điều phối vùng chứa; quan sát được, tin cậy và bảo mật ở mức vận hành.
- *Cổng 9 kiểm:* triển khai lại từ đầu bằng mã, rồi phục hồi sau một sự cố có tiêm lỗi.
- *Chế độ hỏng:* chọn dịch vụ theo tên nhà cung cấp trước khi gọi tên trừu tượng cần dùng.

**Phase 10 · System design, AI boundary and trajectory** — bài 405–440 · M22 (405–420) · M23 (421–430) · M24 (431–440) · Bảo vệ tốt nghiệp

- *Câu hỏi trung tâm:* ra quyết định kiến trúc có đánh đổi, và bảo vệ nó trước phản biện.
- *Năng lực mới:* thiết kế hệ thống theo bậc; ranh giới của kỹ thuật trí tuệ nhân tạo trong công việc dữ liệu, ở mức `C`; năng lực dẫn dắt kỹ thuật.
- *Bảo vệ tốt nghiệp kiểm:* một thiết kế đầu cuối có ngân sách chi phí, chế độ hỏng và điều kiện đảo ngược.
- *Chế độ hỏng:* trình bày kiến trúc bằng sơ đồ hộp mà không có số và không có điều kiện đảo ngược.

---

## 4. Tám cổng xuyên suốt

Lấy nguyên từ mục *Các gate xuyên suốt bắt buộc* của audit. Mỗi bài dự án và mỗi cổng phase
phải chấm theo những cổng này chứ theo cảm nhận về độ hoàn thiện:

1. **Correctness** — golden case, đối soát, bất biến, kiểm trùng, tới muộn, xoá, đổi lược đồ.
2. **Failure** — giết tiến trình, thử lại, phát lại, chạy bù, phân mảnh, thiếu quyền, khôi phục.
3. **Performance** — kế hoạch thực thi, đo, benchmark, ước lượng quy mô, chi phí trước và sau.
4. **Operability** — nhật ký, số đo, dấu vết, mục tiêu mức dịch vụ, cảnh báo, sổ tay, phân tích sau sự cố.
5. **Security** — đặc quyền tối thiểu, phân loại, bí mật, phép thử truy cập trái phép.
6. **Change** — hợp đồng, tương thích, di trú, quay lui, khai tử.
7. **Consumer value** — truy được quyết định, khả năng tìm thấy, khả năng dùng, mức áp dụng.
8. **Evidence** — mã, kiểm thử, số đo, lập luận viết ra, và phản biện của người rà soát.

Cổng 7 là cổng mà bản DE cũ không có. Nó đến từ phần AE và là lý do M11C tồn tại.

---

## 5. Chênh so với hai chương trình hiện tại

| Mảng | AE hiện tại (112 bài) | DE hiện tại (102 bài) | ADE gộp |
|---|---|---|---|
| Nền kỹ thuật máy tính, OS, mạng | không có | 56 bài (M2–M6 bản 422) | 38 bài, P2 |
| Backend và API | không có | rải trong M3 | 12 bài, M8 |
| SQL và nội bộ cơ sở dữ liệu | 30 bài | 30 bài | 36 bài, P4 |
| Mô hình hoá dữ liệu | 18 bài | 14 bài | 16 bài, M11 |
| **Semantic layer và chỉ số** | 12 bài | không có | **20 bài, M11B** |
| **Sản phẩm dữ liệu và tự phục vụ** | rải rác | không có | **18 bài, M11C** |
| dbt và điều phối | 34 bài | 8 bài | 28 bài, M14 |
| **Chất lượng và độ tin cậy dữ liệu** | 14 bài | rải rác | **18 bài, M14C** |
| **Siêu dữ liệu, lineage, quản trị** | 10 bài | không có | **16 bài, M14D** |
| Nạp dữ liệu và tích hợp nguồn | nhận từ DE | 16 bài | 16 bài, M14B |
| Hệ phân tán, Kafka, CDC, Spark | không có | 44 bài | 52 bài, P8 |
| Cloud, container, hạ tầng bằng mã | không có | 36 bài | 44 bài, P9 |
| Thiết kế hệ thống | không có | 16 bài | 16 bài, M22 |
| AI engineering có giới hạn | không có | không có | 10 bài, M23 |
| Lộ trình Staff và Principal | không có | không có | 10 bài, M24 |

Bốn module in đậm là phần mà **gộp mới có**: chúng là năng lực AE mà bản DE 422 bài không phủ,
và là năng lực hạ tầng mà bản AE 112 bài không phủ.

---

## 6. Những gì cố ý để ngoài core

Lấy nguyên từ audit, giữ nguyên quyết định của bản nguồn:

| Năng lực | Quyết định |
|---|---|
| Quản trị dữ liệu chủ, phân giải thực thể | chuyên sâu theo doanh nghiệp |
| Không gian địa lý, chuỗi thời gian, đồ thị | chuyên sâu theo khối lượng công việc |
| Tích hợp hệ thống doanh nghiệp cũ | module theo công việc đích |
| Trực quan hoá và trải nghiệm người dùng BI | chuyên sâu BI Engineer |
| Thống kê nâng cao và thiết kế thí nghiệm | thuộc Data Analyst và Data Science |
| Nền tảng đặc trưng và vận hành mô hình học máy | M23 mở cửa, đào sâu khi chọn hướng |
| Thành thạo nhiều nhà cung cấp đám mây | phản mục tiêu; thạo một, ánh xạ sang hai |

---

## 7. Trạng thái

| Hạng mục | Trạng thái |
|---|---|
| Bản đồ 29 module và 10 phase | Xong |
| Đặc tả 440 bài | **Xong · 440/440 · 29/29 module · 10/10 cổng** |
| Đối chiếu từng module với hợp đồng nguồn | Xong ở mức tên và số bài; chưa ở mức nội dung bài |
| Quyết định số phận AE và DE hiện tại | **Chưa · cần bạn chốt** |

Bản nguồn tự ghi trạng thái là `drafted`, chưa `reviewed`. Bản đồ này kế thừa trạng thái đó.

## Bản cập nhật 2026-09-24 — SIMD, MIMD và lập trình bất đồng bộ

Nguồn `roadmap-de/about me` bổ sung ba track và chương trình bên này thêm **12 bài**, đưa tổng từ 428 lên 440.

| Module | Bài thêm | Nội dung |
|---|---|---|
| M2 | 25 · 26 · 27 · 28 | Mô hình trạng thái hiệp trình; đồng thời có cấu trúc và an toàn khi huỷ; hạn chót đầu cuối và áp lực ngược; tiêm sáu chế độ hỏng bất đồng bộ |
| M4 | 48 · 49 · 50 · 56 | Phân loại Flynn và vị trí của SPMD; SIMD từ làn tới toán tử; véctơ hoá tự động; MIMD bộ nhớ chung, bộ nhớ phân tán và SPMD |
| M5 | 65 · 66 | Bộ mô tả không chặn và ba cơ chế theo dõi; mô hình sẵn sàng so với mô hình hoàn tất |
| M12 | 208 · 211 | Xử lý theo lô véctơ không đồng nghĩa với SIMD; cụm MPP nhìn như MIMD phân tán và SPMD |

Hai bài có sẵn được viết lại để mang nội dung mới: **lesson 55** thêm định luật Gustafson cùng yêu cầu báo hiệu suất song song kèm tăng tốc, và **lesson 58** thêm ba tầng song song lồng nhau.

**M18 đã viết đặc tả** (bài 345–360) và mang đủ phần được yêu cầu: MIMD phân tán cùng khuôn mẫu SPMD ở lesson 352, song song lồng nhau cùng cấp phát quá mức ở lesson 353, và lab tăng quy mô cố định khối lượng ở lesson 354.
