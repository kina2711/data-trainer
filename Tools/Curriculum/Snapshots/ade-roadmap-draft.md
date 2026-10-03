---
chuong_trinh: Data Engineer
ma: DE
phien_ban: "6.0-draft"
trang_thai: draft
cap_do_dau_ra: Junior — Senior
so_bai: 440
cap_nhat: 2026-09-23
---

# CHƯƠNG TRÌNH DATA ENGINEER — BẢN NHÁP GỘP

> **Bản nháp để rà soát, không phải roadmap chính thức.**
> Roadmap chính thức vẫn là `material/data-engineer/roadmap/roadmap.md` (bản cũ, 102 bài).
> Bản này gộp Analytics Engineer vào Data Engineer theo bản đồ `ade-module-map.md`.
> Đã đặc tả **440/440 bài**

**440 bài · 29 module · 885.5 giờ trên lớp · không yêu cầu kiến thức đầu vào**

| | |
|---|---|
| **Vị trí đầu ra** | Data Engineer · Analytics Engineer · Platform Engineer · Data Architect (đích mở rộng) |
| **Cấp độ đạt được** | Junior vững tới Senior; Staff và Principal cần kinh nghiệm thực tế ngoài chương trình |
| **Điều kiện đầu vào** | Không. Giả định chưa biết lập trình |
| **Thời lượng** | 885.5 giờ trên lớp · 1032 giờ tự học · tổng ~1917.5 giờ. Bài thường 2 giờ lớp cộng 2,4 giờ tự học; 10 bài cổng dài hơn và không có bài tự học |
| **Nhịp học** | 12 giờ/tuần → ~36 tháng · 15 giờ/tuần → ~29 tháng |
| **Nguồn thiết kế** | 29 hợp đồng học tập trong `06_LO_TRINH_CHI_TIET_THEO_MODULE` và `AE_DE_COVERAGE_AUDIT.md` |
| **Ánh xạ khung năng lực** | SFIA 9 (2024): `DTAN`, `PROG`, `SYSP`, `NTAS`, `HPCC`, `DATM`, `TEST`, `CFMG`, `DBAD`, `ARCH` |

---

## 1. Bản đồ 29 module

Cột **Vai** ghi module phục vụ vai nào: `AE` phần bù Analytics Engineer, `DE` phần riêng
Data Engineer, `chung` là nền bắt buộc cho cả hai. Bốn module `AE` là phần mà bản Data
Engineer cũ không phủ và là lý do của việc gộp.

| Phase | Module | Tên | Vai | Mức | Bài |
|---|---|---|---|---|---:|
| 1 | **M1** | Engineering thinking, Git and debugging | chung |  | 12 |
| 1 | **M2** | Python for production | chung | `A` | 20 |
| 1 | **M3** | Data structures and algorithms for systems | chung |  | 12 |
| 2 | **M4** | Computer architecture and the performance model | chung |  | 16 |
| 2 | **M5** | Operating systems, concurrency and Linux | chung | `A` | 16 |
| 2 | **M6** | Networking from packet to API | chung |  | 12 |
| 3 | **M7** | Software design and delivery | chung |  | 12 |
| 3 | **M8** | Backend and API engineering | DE |  | 12 |
| 4 | **M9** | Relational theory and SQL execution | chung | `A` | 20 |
| 4 | **M10** | Storage engine and database operations | chung | `A` | 16 |
| 5 | **M11** | Data modeling - operational, analytical, domain | chung | `A` | 16 |
| 5 | **M11B** | Semantic layer and metrics engineering | **AE** | `A` | 20 |
| 5 | **M11C** | Analytical data product and self-service | **AE** |  | 18 |
| 6 | **M12** | OLAP internals | chung |  | 14 |
| 6 | **M13** | File, serialization and table formats | chung | `A` | 14 |
| 7 | **M14B** | Data ingestion and integration | chung | `A` | 16 |
| 7 | **M14** | ELT, dbt and orchestration | chung | `A` | 28 |
| 7 | **M14C** | Data quality and reliability | **AE** | `A` | 18 |
| 7 | **M14D** | Metadata, catalog, lineage and governance | **AE** | `B` | 16 |
| 8 | **M15** | Distributed systems fundamentals | DE |  | 12 |
| 8 | **M16** | Kafka and event streaming | DE | `A` | 14 |
| 8 | **M17** | Change data capture internals | DE | `B` | 10 |
| 8 | **M18** | Spark, Flink and compute engines | DE | `A` | 16 |
| 9 | **M19** | Cloud abstractions before service names | chung | `A` | 12 |
| 9 | **M20** | Docker, infrastructure as code and Kubernetes | DE | `A`/`B` | 16 |
| 9 | **M21** | Observability, reliability and security | chung | `A` | 16 |
| 10 | **M22** | System design progression | chung |  | 16 |
| 10 | **M23** | Modern AI engineering, bounded | chung | `C` | 10 |
| 10 | **M24** | Staff and principal trajectory | chung |  | 10 |

Cổng kiểm tra đã đặc tả: lesson 44 · lesson 88 · lesson 112 · lesson 148 · lesson 202 · lesson 230 · lesson 308 · lesson 360 · lesson 404 · lesson 440.

---

## 2. Quy ước đọc đặc tả bài

Mỗi bài trình bày theo cùng một khuôn, chín trường theo thứ tự cố định:

| Trường | Nội dung |
|---|---|
| **Prerequisites** | Bài hoặc module phải đạt trước |
| **In-class** | Phân bổ 120 phút trên lớp |
| **Learn** | Nội dung khái niệm và cơ chế |
| **Outcome** | Objective phát biểu bằng động từ quan sát được |
| **Đánh giá** | Tầng Bloom của objective, lý do tầng đó khớp vị trí bài, và hình thức kiểm tương ứng |
| **Lab** | Bài thực hành trên lớp |
| **Pitfalls** | Lỗi thường gặp |
| **Self-study** | Phân bổ 2,4 giờ ngoài lớp |
| **Done when** | Tiêu chí ra: đạt hoặc không đạt, có ngưỡng |

**Dạng bài.** `LT` lý thuyết · `TH` thực hành · `DA` dự án · `KT` kiểm tra.

**Ba mức thành thạo công cụ.** `A` xây và vận hành được · `B` làm lab và so sánh có căn cứ · `C` biết dùng đúng tình huống.

**Tám cổng xuyên suốt.** Correctness · Failure · Performance · Operability · Security · Change · Consumer value · Evidence. Mọi bài dự án và mọi cổng phase chấm theo tám cổng này.

---

# MODULE M1 · ENGINEERING THINKING, GIT AND DEBUGGING

**Phase 1 · Lessons 1–12 · 24 giờ**

| | |
|---|---|
| **Objective cấp module** | Biến một yêu cầu mơ hồ thành hợp đồng kiểm thử được, quản lý thay đổi an toàn, và chẩn đoán lỗi bằng bằng chứng chứ bằng thử sai |
| **Tiền đề** | Không. Dùng được terminal và sửa được tệp văn bản |
| **Exit criterion** | Vẽ đúng đồ thị đối tượng của một kho Git và dự đoán đúng `HEAD` sau merge, rebase, reset; nhật ký gỡ lỗi có ít nhất ba giả thuyết bị bác bỏ bằng bằng chứng |
| **Kỹ năng SFIA** | `PROG` mức 3 · `TEST` mức 3 |
| **Chế độ hỏng** | Học thuộc lệnh Git rời rạc mà không có mô hình đối tượng, nên mất commit là mất luôn, và sửa lỗi bằng cách đổi thử tới khi hết báo lỗi |

Module mở đầu và là module đặt kỷ luật cho cả 428 bài còn lại. Ba năng lực ở đây được dùng lại ở mọi module sau: phát biểu hợp đồng trước khi viết mã, quản lý thay đổi có thể lùi, và chẩn đoán có bằng chứng.

Không dạy công cụ dữ liệu nào. Đây là chủ ý: người học vào thẳng công cụ dữ liệu mà thiếu ba năng lực này sẽ dựng được pipeline chạy nhưng không sửa được khi nó hỏng.

### Lesson 1 · From a vague request to a testable contract `LT`
**Prerequisites.** Module 1: Không

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Yêu cầu nghiệp vụ tới dưới dạng một câu mơ hồ, và khoảng cách giữa câu đó với một thứ kiểm thử được là nơi phần lớn công sức bị lãng phí. Sáu phần của một phát biểu bài toán dùng được: ai là người dùng, sự kiện nào kích hoạt, đầu vào gì, đầu ra gì, ràng buộc nào, và **cái gì cố ý không làm**. Phần cuối là phần hay thiếu nhất và cũng là phần cứu dự án khỏi phình. Chuyển mỗi yêu cầu thành hành vi quan sát được rồi thành một phép kiểm chấp nhận: nếu không viết được phép kiểm thì yêu cầu chưa đủ rõ để bắt đầu. Ba loại ràng buộc phải tách bạch vì chúng dẫn tới ba thiết kế khác nhau: ràng buộc về đúng đắn, về hiệu năng, và về vận hành. Phi mục tiêu viết ra thành câu chứ để ngầm hiểu.

**Outcome.** Viết lại một yêu cầu mơ hồ thành phát biểu sáu phần, và cho mỗi yêu cầu một phép kiểm chấp nhận kiểm được.

**Đánh giá.** Tầng *áp dụng*. Bài mở chương trình, người học chưa có nền kỹ thuật nào nên objective dừng ở việc áp một khuôn có sẵn vào tình huống mới. Kiểm bằng bài viết lại ba yêu cầu; đạt khi cả ba có đủ sáu phần và mọi phép kiểm chấp nhận đều nêu được đầu vào cùng kết quả mong đợi.

**Lab.** Nhận ba yêu cầu viết theo cách người nghiệp vụ thật hay nhắn. Viết lại từng cái thành phát biểu sáu phần. Với mỗi yêu cầu, viết ít nhất hai phép kiểm chấp nhận có đầu vào và kết quả mong đợi cụ thể. Đổi bài với một học viên khác: họ chỉ ra chỗ nào còn mơ hồ tới mức hai người có thể hiểu khác nhau.

**Pitfalls.** Bỏ phần phi mục tiêu · viết phép kiểm dạng chạy không lỗi · trộn ràng buộc đúng đắn với ràng buộc hiệu năng · bắt đầu viết mã khi chưa viết được phép kiểm nào.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba yêu cầu đều có đủ sáu phần, mỗi yêu cầu có ≥ 2 phép kiểm chấp nhận cụ thể, và người đổi bài không tìm được chỗ hiểu hai nghĩa.

### Lesson 2 · Decomposition - responsibility, interface, state and failure domain `LT`
**Prerequisites.** Lesson 1

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Chia một hệ thành phần là quyết định thiết kế đầu tiên và khó sửa nhất. Bốn trục để chia và mỗi trục trả lời một câu hỏi khác nhau: trách nhiệm tức phần này chịu trách nhiệm về cái gì, giao diện tức nó hứa gì với bên ngoài, trạng thái tức nó nhớ gì, và phạm vi hỏng tức nó chết thì kéo theo những gì. Độ gắn kết và độ phụ thuộc: gắn kết cao trong một phần, phụ thuộc thấp giữa các phần, và chiều phụ thuộc phải một chiều chứ vòng. Trừu tượng hoá che cái gì và bắt buộc lộ cái gì; trừu tượng rò rỉ là trừu tượng che một thứ mà người dùng vẫn phải biết, và nhận ra nó sớm tiết kiệm rất nhiều thời gian về sau. Bất biến là điều luôn đúng qua mọi lần chuyển trạng thái; bài này chỉ đặt khái niệm, còn chỗ đặt bất biến vào cơ sở dữ liệu sẽ quay lại ở M10.

**Outcome.** Phân rã một hệ cho trước theo bốn trục và chỉ ra chiều phụ thuộc cùng phạm vi hỏng của từng phần.

**Đánh giá.** Tầng *phân tích*. Objective đòi tách một chỉnh thể thành các phần có ranh giới lý giải được, chứ vẽ lại sơ đồ có sẵn. Kiểm bằng bài phân rã cộng phản biện; đạt khi bốn trục đều được trả lời và không có phụ thuộc vòng.

**Lab.** Cho mô tả một hệ bán hàng nhỏ. Phân rã thành các phần, với mỗi phần ghi bốn trục. Vẽ chiều phụ thuộc và chỉ ra phụ thuộc vòng nếu có. Với mỗi phần, trả lời: phần này chết thì cái gì còn chạy được. Hai bạn cùng lớp phản biện ranh giới bạn chọn.

**Pitfalls.** Chia theo tầng kỹ thuật thay vì theo trách nhiệm · để phụ thuộc vòng · bỏ qua trạng thái nên không thấy phần nào khó thay thế · vẽ sơ đồ mà không nêu phạm vi hỏng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn trục được trả lời cho mọi phần, đồ thị phụ thuộc không có vòng, và chỉ đúng phạm vi hỏng của ít nhất ba phần.

### Lesson 3 · Trade-offs and the architecture decision record `TH`
**Prerequisites.** Lesson 2

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phần lớn quyết định kỹ thuật không có phương án đúng tuyệt đối, chỉ có phương án phù hợp ràng buộc, nên thứ cần lưu lại là **lý do** chứ kết luận. Tài liệu quyết định kiến trúc có năm phần: bối cảnh và ràng buộc, các phương án đã cân nhắc, quyết định, hệ quả gồm cả mặt xấu, và điều kiện xem lại. Phần các phương án bị loại là phần giá trị nhất: người đọc sau cần biết phương án kia đã được xét và loại vì gì, nếu không họ đề xuất lại đúng phương án đó. Điều kiện xem lại làm tài liệu này khác một biên bản: ghi mốc nào thì quyết định nên được xét lại. Tiêu chí so sánh phải nêu trước khi so, nếu không thì việc so biến thành biện minh cho lựa chọn đã có sẵn trong đầu. Khả năng đảo ngược là một tiêu chí thường bị bỏ: quyết định dễ lùi thì quyết nhanh, quyết định khó lùi thì cần bằng chứng.

**Outcome.** Viết một tài liệu quyết định đủ năm phần cho một lựa chọn thật, và người không dự buổi quyết định đọc hiểu được lý do.

**Đánh giá.** Tầng *áp dụng*. Objective là một sản phẩm viết theo chuẩn, kiểm được bằng phản ứng của người đọc chứ bằng độ dài. Kiểm bằng rà soát chéo; đạt khi người rà soát không còn câu hỏi nào về lý do và điều kiện xem lại là kiểm được.

**Lab.** Chọn định dạng tệp cho một bài toán trao đổi dữ liệu giữa hai đội: so CSV, JSON và Parquet theo lược đồ, kích thước, khả năng liên thông và mẫu quét. Nêu tiêu chí trước, rồi mới so. Viết tài liệu quyết định đủ năm phần, dưới hai trang. Đưa cho một học viên khác đọc và ghi lại mọi câu họ phải hỏi.

**Pitfalls.** Bỏ phần phương án bị loại · viết hệ quả chỉ có mặt tốt · đặt điều kiện xem lại chung chung · chọn trước rồi mới nghĩ tiêu chí.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tài liệu đủ năm phần và dưới hai trang, người rà soát không còn câu hỏi về lý do, và điều kiện xem lại nêu được mốc kiểm được.

### Lesson 4 · Git as a content-addressed object database `LT`
**Prerequisites.** Lesson 3

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Học Git bằng cách nhớ lệnh thì mỗi tình huống lạ là một lần bế tắc; học bằng mô hình đối tượng thì suy ra được lệnh. Bốn loại đối tượng: blob giữ nội dung tệp, cây giữ danh sách tên trỏ tới blob và cây con, commit giữ một cây cộng danh sách cha cộng siêu dữ liệu, và thẻ có chú thích. Điểm quyết định: **commit là ảnh chụp toàn bộ cây cộng con trỏ cha, không phải một bản khác biệt**; phần khác biệt chỉ là thứ Git tính ra khi cần hiển thị. Ba vùng và ba con trỏ: cây làm việc, vùng chờ, kho; `HEAD` trỏ tới nhánh, nhánh trỏ tới commit. Từ mô hình này suy ra ngay: xoá nhánh không xoá commit, nên commit vẫn còn và phục hồi được; hai nhánh chia sẻ phần lịch sử chung vì cùng trỏ ngược về một tổ tiên. Cách tự kiểm chứng mọi khẳng định trên bằng lệnh đọc đối tượng thô, thay vì tin lời giảng.

**Outcome.** Vẽ đúng đồ thị đối tượng của một kho nhỏ và dự đoán con trỏ nào thay đổi sau mỗi thao tác.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết nền, chưa đòi xử lý sự cố. Kiểm bằng bài vẽ cộng dự đoán viết trước khi chạy; đạt khi đồ thị đúng và dự đoán khớp thực tế ở ít nhất năm trong sáu thao tác.

**Lab.** Tạo một kho mới, tạo ba commit. Dùng lệnh đọc đối tượng thô để liệt kê blob, cây và commit, rồi vẽ đồ thị. Với sáu thao tác gồm `add`, `commit`, `checkout`, `branch`, `reset --soft` và `reset --hard`, viết dự đoán con trỏ nào đổi **trước khi chạy**, rồi chạy và đối chiếu.

**Pitfalls.** Nghĩ commit lưu phần khác biệt · nhầm nhánh với thư mục · tin rằng xoá nhánh là mất commit · học lệnh mà không đọc đối tượng lần nào.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đồ thị đối tượng vẽ đúng, và dự đoán khớp thực tế ở ≥ 5/6 thao tác.

### Lesson 5 · Branching, merge, rebase and commit identity `TH`
**Prerequisites.** Lesson 4

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hợp nhất ba chiều dùng tổ tiên chung làm gốc so sánh, nên hiểu tổ tiên chung là hiểu vì sao xung đột xảy ra ở đúng chỗ đó. Xung đột không phải lỗi mà là chỗ Git không tự quyết được; giải xung đột là một quyết định nội dung chứ thao tác cơ khí. Rebase phát lại các commit lên một gốc mới, và điều quan trọng là **commit mới có mã định danh mới dù nội dung giống hệt**; từ đó suy ra quy tắc không rebase nhánh người khác đang dùng. Ba cách hợp nhất và hệ quả lên lịch sử: hợp nhất thường giữ đồ thị thật, rebase cho lịch sử thẳng nhưng viết lại định danh, và gộp thành một commit làm mất bước trung gian. Phân biệt viết lại lịch sử với commit đảo ngược: `revert` tạo một commit mới huỷ hiệu lực commit cũ và an toàn trên nhánh chung, còn `reset` viết lại và chỉ an toàn trên nhánh riêng.

**Outcome.** Chọn đúng giữa hợp nhất, rebase và đảo ngược cho một tình huống cho trước, và giải thích bằng định danh commit cùng phạm vi ảnh hưởng.

**Đánh giá.** Tầng *đánh giá*. Objective đòi cân giữa lịch sử sạch và an toàn cho người khác, chứ nhớ cú pháp. Kiểm bằng bốn tình huống; đạt khi chọn đúng ít nhất ba và mỗi lần nêu đúng ai bị ảnh hưởng.

**Lab.** Dựng hai nhánh có xung đột nội dung. Giải xung đột và giải thích vì sao Git dừng ở đúng đoạn đó, dẫn bằng tổ tiên chung. Thực hiện cả ba cách hợp nhất trên ba bản sao của cùng kho, so đồ thị kết quả. Cho bốn tình huống và chọn cách xử lý, nêu ai bị ảnh hưởng nếu chọn sai.

**Pitfalls.** Rebase nhánh đã đẩy lên kho chung · dùng `reset --hard` trên nhánh chung · gộp commit cho một chuỗi cần giữ bước trung gian · giải xung đột bằng cách giữ một bên mà không đọc.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chọn đúng ≥ 3/4 tình huống kèm phạm vi ảnh hưởng, và giải thích đúng vị trí xung đột bằng tổ tiên chung.

### Lesson 6 · Recovering lost work - reflog, detached HEAD and bisect `TH`
**Prerequisites.** Lesson 5

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hai kỹ năng cứu nguy mà phần lớn người dùng Git chỉ học sau khi đã mất việc một lần. Nhật ký tham chiếu ghi lại mọi vị trí `HEAD` từng đứng, kể cả những vị trí không còn nhánh nào trỏ tới, nên gần như mọi commit đã tạo đều tìm lại được trong thời gian giữ mặc định. Ba tình huống mất việc hay gặp và cách phục hồi từng cái: `reset --hard` nhầm, xoá nhánh chưa hợp nhất, và rebase hỏng giữa chừng. `HEAD` tách rời là trạng thái bình thường chứ lỗi, nhưng commit tạo ra trong đó không có nhánh giữ nên dễ mất. Tìm lỗi bằng chia đôi biến việc truy hồi quy thành bài toán tìm kiếm nhị phân: với một phép kiểm tự động trả đúng mã thoát thì toàn bộ quá trình tự chạy. Điều kiện để dùng được: có phép kiểm tái hiện lỗi, và lịch sử có commit nhỏ chứ commit khổng lồ.

**Outcome.** Phục hồi được việc đã mất trong ba tình huống, và định vị commit gây hồi quy bằng tìm kiếm chia đôi tự động.

**Đánh giá.** Tầng *áp dụng*. Objective là hai thao tác cứu nguy kiểm được bằng kết quả. Kiểm bằng ba tình huống mất việc cộng một lần chia đôi; đạt khi phục hồi cả ba và chia đôi chỉ đúng commit gây lỗi.

**Lab.** Tự gây cả ba tình huống mất việc rồi phục hồi từng cái bằng nhật ký tham chiếu, ghi lại ghi chú phục hồi. Tạo 8 commit, cài một hồi quy ở commit thứ tư, viết một phép kiểm trả mã thoát đúng, rồi chạy chia đôi tự động và xác nhận nó chỉ ra commit 4.

**Pitfalls.** Không biết nhật ký tham chiếu tồn tại · chia đôi thủ công thay vì dùng phép kiểm tự động · commit quá to nên chia đôi chỉ tới một commit đổi 40 tệp · hoảng rồi clone lại kho.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phục hồi thành công cả ba tình huống có ghi chú, và chia đôi tự động chỉ đúng commit 4.

### Lesson 7 · Collaboration - small commits, review and release discipline `TH`
**Prerequisites.** Lesson 6

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Làm việc nhóm đặt ra ràng buộc mà làm một mình không có, và ba ràng buộc quan trọng nhất đều nằm ở kích thước và ranh giới thay đổi. Commit nhỏ và một mục đích: dễ rà soát, dễ lùi, và làm chia đôi ở lesson 6 thật sự dùng được. Thông điệp commit nói **vì sao** chứ cái gì, vì cái gì đã nằm trong phần khác biệt. Yêu cầu hợp nhất là đơn vị rà soát: kèm mô tả, phạm vi ảnh hưởng, cách kiểm chứng, và ghi chú lùi. Rà soát mã là việc tìm hiểu lầm và rủi ro chứ bắt lỗi chính tả; ba câu hỏi người rà soát phải trả lời được. Chính sách nhánh và nhánh được bảo vệ. Đánh số phiên bản theo ngữ nghĩa và ý nghĩa thật của từng số với người dùng thư viện. Ghi chú lùi phải nói được **lùi bằng cách nào**, chứ chỉ nói có lùi được hay không; và đây là chỗ một loại thay đổi phá vỡ giả định: **thay đổi có kèm sửa cấu trúc dữ liệu thì lùi mã không đủ**, vì mã cũ không đọc được dữ liệu đã đổi. Lời giải là kế hoạch tương thích: đổi cấu trúc theo hướng cộng thêm trước, để mã cũ và mã mới cùng chạy được trong một cửa sổ, rồi mới bỏ phần cũ. Quy tắc suy ra: khả năng lùi là một thuộc tính phải thiết kế, không phải một nút bấm có sẵn. Vì sao phần này nằm ở module đầu chứ module cuối: mọi lab từ đây trở đi đều nộp qua yêu cầu hợp nhất, nên kỷ luật phải có trước.

**Outcome.** Nộp một yêu cầu hợp nhất đủ bốn phần, rà soát yêu cầu của người khác bằng ba câu hỏi bắt buộc, và chỉ ra được một thay đổi mà lùi mã không đủ để lùi.

**Đánh giá.** Tầng *áp dụng*. Objective là hai vai trong cùng một quy trình, kiểm được bằng sản phẩm của cả hai phía. Kiểm bằng một vòng nộp và rà soát chéo cộng một phép thử lùi; đạt khi yêu cầu đủ bốn phần, bản rà soát nêu được ít nhất một rủi ro thật, và phép thử lùi cho thấy đúng chỗ lùi mã không đủ.

**Lab.** Chia nhỏ một thay đổi lớn thành bốn commit một mục đích, mỗi commit có thông điệp nói vì sao. Nộp yêu cầu hợp nhất đủ mô tả, phạm vi ảnh hưởng, cách kiểm chứng và ghi chú lùi. Rà soát yêu cầu của một học viên khác theo ba câu hỏi bắt buộc và ghi ít nhất một rủi ro. Tạo một thay đổi có kèm sửa cấu trúc dữ liệu, lùi mã về bản trước, và ghi lại chuyện gì xảy ra với dữ liệu đã đổi. Viết kế hoạch tương thích cho phép mã cũ và mã mới cùng chạy, rồi lùi lại lần nữa và chứng minh lần này lùi được.

**Pitfalls.** Một commit khổng lồ cho cả tính năng · thông điệp commit chép lại tên tệp đã sửa · rà soát chỉ soi phong cách · bỏ ghi chú lùi · coi lùi mã là lùi được toàn bộ khi thay đổi có kèm sửa cấu trúc dữ liệu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn commit đều một mục đích và có lý do, yêu cầu hợp nhất đủ bốn phần, bản rà soát nêu được ít nhất một rủi ro thật, và phép thử lùi chỉ ra đúng chỗ lùi mã không đủ với kế hoạch tương thích làm lần lùi thứ hai thành công.

### Lesson 8 · Scientific debugging - from symptom to proven cause `LT`
**Prerequisites.** Lesson 7

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Sửa lỗi bằng cách đổi thử tới khi hết báo lỗi là cách tạo ra lỗi tiếp theo, vì nguyên nhân chưa từng được chứng minh. Quy trình sáu bước: ghi lại triệu chứng gồm mong đợi, thực tế, thời điểm, phiên bản, đầu vào và môi trường; tái hiện một cách xác định; thu nhỏ về trường hợp hỏng nhỏ nhất; thêm khả năng quan sát ở ranh giới; lập bảng giả thuyết; và sửa đúng nguyên nhân nhỏ nhất rồi thêm phép kiểm hồi quy. Bảng giả thuyết là công cụ trung tâm và có ba cột: dự đoán, phép thử có thể bác bỏ nó, và kết quả. **Giả thuyết không kèm phép thử bác bỏ được thì không phải giả thuyết.** Phân biệt tương quan với nguyên nhân: hai thứ cùng xảy ra không chứng minh cái này gây cái kia. Định vị theo tầng từ trên xuống: dữ liệu đầu vào, ứng dụng, phụ thuộc, hệ điều hành và mạng, nền tảng.

**Outcome.** Lập bảng giả thuyết cho một lỗi cho trước, với mỗi giả thuyết nêu một phép thử bác bỏ được.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết đặt quy trình, phần thực hành nằm ở lesson 9. Kiểm bằng bảng giả thuyết cho ba lỗi mẫu; đạt khi mọi giả thuyết đều có phép thử bác bỏ được và không có giả thuyết nào không kiểm được.

**Lab.** Cho ba mô tả lỗi. Với mỗi lỗi, viết hồ sơ triệu chứng sáu phần và lập bảng giả thuyết ít nhất ba dòng. Đổi bài: học viên khác chỉ ra giả thuyết nào không bác bỏ được bằng phép thử bạn đề ra.

**Pitfalls.** Đoán nguyên nhân rồi tìm bằng chứng ủng hộ nó · đặt giả thuyết dạng chắc do môi trường · sửa trước khi tái hiện · bỏ bước thu nhỏ nên gỡ trên hệ đầy đủ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba hồ sơ triệu chứng đủ sáu phần, mọi giả thuyết có phép thử bác bỏ được, và người đổi bài không tìm được giả thuyết không kiểm được.

### Lesson 9 · Reproduce, reduce and instrument at the boundary `TH`
**Prerequisites.** Lesson 8

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba kỹ năng làm cho quy trình ở lesson 8 chạy được trong thực tế. Tái hiện xác định: cố định đầu vào, cố định thời gian và ngẫu nhiên, cố định phiên bản; lỗi chỉ xuất hiện thỉnh thoảng thì phải tìm ra biến còn thay đổi chứ kết luận là lỗi ngẫu nhiên. Thu nhỏ: cắt dần đầu vào và cắt dần mã cho tới khi bỏ thêm một thứ nữa thì lỗi biến mất; trường hợp nhỏ nhất thường tự nó chỉ ra nguyên nhân. Thêm khả năng quan sát ở **ranh giới** chứ rải khắp nơi: ghi lại đầu vào và đầu ra tại mỗi ranh giới giữa hai thành phần, vì lỗi nằm ở chỗ hai bên hiểu khác nhau về hợp đồng. Nhật ký có cấu trúc và mã theo dõi để nối các dòng thuộc cùng một lần chạy. Ba loại lỗi hay gặp với dữ liệu và cách nhận ra từng loại: dữ liệu không đúng hình dạng, tài nguyên cạn, và thiếu quyền.

**Outcome.** Tái hiện xác định một lỗi, thu nhỏ về trường hợp nhỏ nhất, và chứng minh nguyên nhân bằng quan sát ở ranh giới.

**Đánh giá.** Tầng *phân tích*. Objective là truy từ triệu chứng về nguyên nhân bằng bằng chứng, kỹ năng nền cho mọi module sau. Kiểm bằng ba lỗi tiêm sẵn; đạt khi chứng minh đúng nguyên nhân ít nhất hai và trường hợp nhỏ nhất thật sự nhỏ.

**Lab.** Nhận một chương trình xử lý CSV có ba lỗi tiêm sẵn: một dòng sai định dạng, một tình huống hết chỗ trống trên đĩa mô phỏng, và một lỗi thiếu quyền. Với mỗi lỗi, tái hiện xác định, thu nhỏ đầu vào, thêm ghi nhật ký ở ranh giới, và nộp bảng giả thuyết có ít nhất ba dòng bị bác bỏ.

**Pitfalls.** Rải lệnh in khắp mã thay vì đặt ở ranh giới · kết luận lỗi ngẫu nhiên khi chưa cố định biến · thu nhỏ bằng cách xoá mã tới khi không chạy nữa · sửa khi chưa tái hiện được.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chứng minh đúng nguyên nhân ≥ 2/3 lỗi, mỗi lần có ≥ 3 giả thuyết bị bác bỏ bằng bằng chứng, và trường hợp nhỏ nhất dưới 20 dòng.

### Lesson 10 · Technical artifacts - README, runbook and postmortem `TH`
**Prerequisites.** Lesson 9

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bốn tài liệu mà mọi thành phần chạy trong sản xuất phải có, và mỗi tài liệu phục vụ một người đọc ở một thời điểm khác nhau. README phục vụ người mới: mục đích, kiến trúc một đoạn, cách cài, cách chạy và kiểm, và giới hạn đã biết. Tài liệu quyết định ở lesson 3 phục vụ người sửa kiến trúc về sau. Sổ tay vận hành phục vụ người trực lúc ba giờ sáng, nên cấu trúc phải theo đúng trình tự họ cần: cảnh báo nào, ảnh hưởng gì, chẩn đoán ra sao, giảm nhẹ thế nào, leo thang cho ai, và xác nhận đã hồi phục bằng cách nào. Phân tích sau sự cố phục vụ cả đội về sau: dòng thời gian, điều kiện góp phần, khoảng trống trong phát hiện, và hành động khắc phục có chủ. Nguyên tắc chung: viết cho người chưa có bối cảnh, và mọi từ viết tắt được định nghĩa ở chỗ người đọc gặp nó lần đầu.

**Outcome.** Viết bộ bốn tài liệu cho một thành phần nhỏ, và người khác dùng được mà không phải hỏi.

**Đánh giá.** Tầng *áp dụng*. Objective là sản phẩm viết theo chuẩn, đo bằng kết quả của người đọc. Kiểm bằng phép thử bàn giao; đạt khi người nhận chạy được và xử lý được tình huống trong sổ tay với số câu hỏi dưới ngưỡng.

**Lab.** Viết bốn tài liệu cho công cụ CSV ở lesson 9. Đưa cho một học viên chưa xem mã: họ cài, chạy, và xử lý một tình huống lỗi chỉ dựa vào sổ tay. Ghi lại mọi câu họ phải hỏi rồi sửa tài liệu theo danh sách đó.

**Pitfalls.** Viết README cho chính mình đọc · sổ tay không có bước xác nhận đã hồi phục · phân tích sau sự cố quy về lỗi cá nhân · dùng từ viết tắt chưa định nghĩa.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Người nhận cài và chạy được, xử lý được tình huống theo sổ tay, và số câu hỏi phải hỏi dưới ngưỡng.

### Lesson 11 · Putting it together - a small CLI with contract, tests and logs `DA`
**Prerequisites.** Lesson 10

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Bài dự án gộp toàn module: một công cụ dòng lệnh nạp tệp CSV, kiểm tra lược đồ, và ghi ra kết quả. Yêu cầu bắt buộc và mỗi yêu cầu đến từ một bài trước: phát biểu bài toán sáu phần theo lesson 1; ranh giới thành phần rõ theo lesson 2; một tài liệu quyết định theo lesson 3; lịch sử Git gồm commit nhỏ một mục đích theo lesson 7; **mã thoát đúng** để hệ gọi biết thành công hay thất bại; nhật ký có cấu trúc ở ranh giới theo lesson 9; phép kiểm đơn vị và phép kiểm tích hợp; và bộ bốn tài liệu theo lesson 10. Phép thử nghiệm thu là phép thử tiêm lỗi: giảng viên đưa năm tệp đầu vào hỏng theo năm cách, và công cụ phải phân loại đúng, thoát đúng mã, và ghi đủ để chẩn đoán mà không cần chạy lại.

**Outcome.** Nộp một công cụ đạt tám yêu cầu, xử lý đúng năm loại đầu vào hỏng, và có bộ tài liệu dùng được.

**Đánh giá.** Tầng *sáng tạo*. Bài dự án tổng hợp, đòi ghép tám yêu cầu rời thành một sản phẩm chạy được. Kiểm bằng phép thử tiêm lỗi cộng rà soát tám yêu cầu; đạt khi cả năm đầu vào hỏng được xử lý đúng và tám yêu cầu đều có bằng chứng.

**Lab.** Xây công cụ. Nộp qua yêu cầu hợp nhất. Giảng viên đưa năm tệp hỏng: thiếu cột, sai kiểu, bảng mã sai, dòng có dấu phân cách trong trường, và tệp rỗng. Với mỗi tệp, công cụ phải phân loại, thoát đúng mã, và nhật ký đủ để một người khác chẩn đoán.

**Pitfalls.** Nuốt ngoại lệ rồi vẫn thoát mã không · ghi nhật ký dạng chuỗi tự do · nộp một commit duy nhất · bỏ tài liệu vì thấy công cụ nhỏ.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Năm đầu vào hỏng đều được phân loại đúng với mã thoát đúng, tám yêu cầu đều có bằng chứng, và một học viên khác chẩn đoán được cả năm chỉ bằng nhật ký.

### Lesson 12 · Delayed recall and the evidence habit `LT`
**Prerequisites.** Lesson 11

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài chốt module, và nó đặt một thói quen dùng cho cả 416 bài còn lại. Ôn lại có khoảng cách: kiểm tra lại sau 1 ngày, 7 ngày và 30 ngày, vì nhớ ngay sau buổi học không dự đoán được việc nhớ sau một tháng. Phân biệt nhận ra với nhớ lại: đọc lại tài liệu thấy quen thuộc là nhận ra, và nó tạo cảm giác đã học xong mà không tương ứng với năng lực; phép kiểm thật là viết lại hoặc làm lại mà không nhìn. Ghi chú chín phần dùng suốt chương trình và lý do từng phần. Nhật ký lỗi cá nhân: mỗi lỗi ghi triệu chứng, nguyên nhân thật, và dấu hiệu nhận ra sớm lần sau; đây là tài liệu người học dùng lại nhiều nhất về sau. Thói quen bằng chứng: mọi khẳng định về hệ thống của mình phải dẫn được về một số đo, một nhật ký hoặc một phép kiểm, chứ dừng ở cảm nhận. Đây chính là cổng thứ tám trong tám cổng xuyên suốt.

**Outcome.** Thiết lập được hệ ôn tập có khoảng cách và nhật ký lỗi, và đạt ngưỡng nhớ lại trên nội dung của module.

**Đánh giá.** Tầng *hiểu*. Bài chốt, đo mức giữ lại chứ mở nội dung mới. Kiểm bằng bài nhớ lại có khoảng cách sau 14 ngày; đạt khi đúng ≥ 80% và lặp lại được thao tác chia đôi mà không nhìn hướng dẫn.

**Lab.** Dựng ghi chú chín phần cho cả 11 bài trước và nhật ký lỗi từ những lỗi đã gặp trong module. Đặt lịch ôn 1, 7 và 30 ngày. Sau 14 ngày, làm bài nhớ lại gồm 20 câu và thực hiện lại quy trình chia đôi ở lesson 6 mà không nhìn hướng dẫn.

**Pitfalls.** Đọc lại tài liệu rồi tưởng đã nhớ · bỏ nhật ký lỗi vì thấy mất thời gian · ôn dồn một lần thay vì có khoảng cách · ghi chú chép lại slide.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đạt ≥ 80% bài nhớ lại sau 14 ngày, và lặp lại được quy trình chia đôi không nhìn hướng dẫn.

# MODULE M2 · PYTHON FOR PRODUCTION

**Phase 1 · Lessons 13–32 · 40 giờ**

| | |
|---|---|
| **Objective cấp module** | Viết Python có hợp đồng, có kiểm thử, đóng gói được, quan sát được, và chọn đúng mô hình đồng thời theo khối lượng công việc |
| **Tiền đề** | M1 |
| **Exit criterion** | Gói cài được, có chú thích kiểu, có CI xanh, môi trường tái tạo được trên máy khác; một dịch vụ bất đồng bộ không có tác vụ mồ côi, không phát tán không giới hạn, không rò bể kết nối, và phân biệt được hết giờ cục bộ với hạn chót đầu cuối |
| **Kỹ năng SFIA** | `PROG` mức 4 · `TEST` mức 3 |
| **Chế độ hỏng** | Viết script chạy được trên máy mình rồi gọi đó là xong: không đóng gói, không kiểm thử, không đo, và chọn mô hình đồng thời theo lời khuyên trên mạng |

Python là công cụ mức `A` của cả chương trình: mọi module sau đều dùng nó để nạp dữ liệu, biến đổi, kiểm thử và vận hành. Nên module này dạy Python như ngôn ngữ xây sản phẩm chứ ngôn ngữ viết script.

Ba phần có thứ tự bắt buộc: hiểu mô hình đối tượng và vòng đời tài nguyên trước, đóng gói và kiểm thử sau, rồi mới tới đồng thời. Học đồng thời trước khi hiểu vòng đời tài nguyên là cách tạo ra lỗi không tái hiện được.

### Lesson 13 · Names, objects and mutability `LT`
**Prerequisites.** Module 2: M1

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Phần lớn lỗi khó hiểu của người mới học Python bắt nguồn từ việc nhầm tên với đối tượng. Gán không sao chép giá trị mà gắn một tên vào một đối tượng, nên hai tên có thể trỏ cùng một đối tượng và sửa qua tên này thì tên kia thấy. Phân biệt đồng nhất với bằng nhau, và vì sao hai thứ này khác nhau với đối tượng thay đổi được. Đối tượng thay đổi được và không thay đổi được: hệ quả trực tiếp là **giá trị mặc định của tham số hàm được tạo một lần khi định nghĩa hàm**, nên dùng danh sách rỗng làm mặc định là một trong những bẫy kinh điển. Sao chép nông và sao chép sâu, cùng chi phí của từng loại. Phạm vi tên và bao đóng: hàm lồng nhau bắt giữ tên chứ giá trị, nên vòng lặp tạo hàm cho kết quả bất ngờ nếu không hiểu điều này. Cách tự kiểm chứng mọi khẳng định trên bằng lệnh xem đồng nhất, thay vì tin lời giảng.

**Outcome.** Dự đoán đúng kết quả của các đoạn mã có chia sẻ đối tượng thay đổi được, và giải thích bằng quan hệ tên với đối tượng.

**Đánh giá.** Tầng *hiểu*. Bài mở module, nền cho mọi bài sau; chưa đòi viết sản phẩm. Kiểm bằng bài dự đoán viết trước khi chạy; đạt khi đúng ≥ 8/10 đoạn và giải thích được bằng tên và đối tượng chứ bằng mô tả hiện tượng.

**Lab.** Cho 10 đoạn mã ngắn về chia sẻ đối tượng, mặc định thay đổi được, sao chép nông và bao đóng trong vòng lặp. Viết dự đoán trước, chạy, đối chiếu. Với mỗi đoạn sai dự đoán, vẽ lại quan hệ tên và đối tượng bằng lệnh xem đồng nhất.

**Pitfalls.** Dùng danh sách rỗng làm giá trị mặc định · nghĩ gán là sao chép · dùng so sánh bằng cho kiểm tra đồng nhất · sao chép nông rồi tưởng đã tách hẳn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Dự đoán đúng ≥ 8/10 đoạn, và mỗi đoạn sai được giải thích lại bằng quan hệ tên với đối tượng.

### Lesson 14 · Iterators, generators and lazy evaluation `TH`
**Prerequisites.** Lesson 13

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Đọc cả tệp vào bộ nhớ là cách viết chạy tốt trên tệp mẫu và chết trên tệp thật, nên đánh giá lười là kỹ thuật nền của mọi module xử lý dữ liệu về sau. Phân biệt đối tượng lặp được với bộ lặp: một cái tạo ra bộ lặp, một cái giữ trạng thái đang ở đâu; từ đó suy ra vì sao duyệt một bộ lặp hai lần thì lần hai rỗng. Hàm sinh là một máy trạng thái: mỗi lần gặp lệnh nhường thì dừng lại và giữ nguyên trạng thái cục bộ, lần gọi sau chạy tiếp từ đó. Hệ quả cho dữ liệu: xử lý theo dòng chảy dùng bộ nhớ không đổi bất kể kích thước đầu vào. Áp lực ngược tự nhiên: bên tiêu thụ quyết định nhịp, nên không có chuyện bên sản xuất dồn quá nhanh. Chuỗi hàm sinh nối nhau tạo thành một đường ống trong bộ nhớ, và đây là mô hình sẽ gặp lại ở tầng lớn hơn tại M18.

**Outcome.** Viết lại một đoạn xử lý nạp toàn bộ thành dạng dòng chảy, và chứng minh bằng số đo rằng bộ nhớ không tăng theo kích thước đầu vào.

**Đánh giá.** Tầng *áp dụng*. Objective là một phép biến đổi mã có kết quả đo được bằng bộ nhớ. Kiểm bằng cặp số đo trên ba kích thước đầu vào; đạt khi bản dòng chảy giữ bộ nhớ gần như không đổi.

**Lab.** Viết bản nạp toàn bộ xử lý một tệp CSV và đo bộ nhớ đỉnh trên tệp 10 MB, 200 MB và 2 GB. Viết lại bằng hàm sinh và đo lại. Vẽ hai đường. Nối ba hàm sinh thành một chuỗi và chứng minh bộ nhớ vẫn không đổi.

**Pitfalls.** Gọi hàm chuyển thành danh sách ngay trong chuỗi nên mất tính lười · duyệt bộ lặp hai lần · đo bộ nhớ trung bình thay vì đỉnh · kết luận từ tệp mẫu quá nhỏ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bản dòng chảy giữ bộ nhớ đỉnh gần như không đổi qua cả ba kích thước, trong khi bản nạp toàn bộ tăng tuyến tính.

### Lesson 15 · Exceptions, resource lifetime and context managers `TH`
**Prerequisites.** Lesson 14

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hai lỗi vận hành phổ biến nhất trong mã xử lý dữ liệu đều nằm ở đây: nuốt ngoại lệ, và rò rỉ tài nguyên. Phân loại ngoại lệ và nguyên tắc bắt cụ thể chứ bắt chung: bắt mọi thứ rồi bỏ qua là cách biến một lỗi rõ ràng thành dữ liệu sai âm thầm. Nối chuỗi ngoại lệ để giữ nguyên nhân gốc khi dịch lỗi sang ngôn ngữ của tầng trên. Dịch lỗi ở ranh giới: bên trong dùng ngoại lệ chi tiết, ra tới ranh giới thì dịch sang lỗi có nghĩa với người gọi. Trình quản lý ngữ cảnh bảo đảm dọn dẹp chạy kể cả khi có ngoại lệ, và đây là cách duy nhất đúng để quản lý tệp, kết nối cơ sở dữ liệu và khoá. Tự viết trình quản lý ngữ cảnh cho một tài nguyên của mình. Nguyên tắc thông báo lỗi dùng được: nêu cái gì hỏng, ở đâu, với dữ liệu nào, và người đọc nên làm gì tiếp.

**Outcome.** Viết mã xử lý lỗi không nuốt ngoại lệ và không rò rỉ tài nguyên, chứng minh bằng thí nghiệm gây lỗi giữa chừng.

**Đánh giá.** Tầng *áp dụng*. Objective là hai tính chất kiểm được bằng thực nghiệm chứ bằng đọc mã. Kiểm bằng thí nghiệm gây lỗi; đạt khi không kết nối nào còn mở sau 100 lần lỗi và mọi lỗi đều lộ ra kèm nguyên nhân gốc.

**Lab.** Viết một hàm mở kết nối, xử lý, rồi đóng. Gây lỗi giữa chừng 100 lần và đếm số kết nối còn mở. Viết lại bằng trình quản lý ngữ cảnh và đếm lại. Dịch một ngoại lệ thấp tầng sang lỗi có nghĩa ở ranh giới, giữ nguyên nhân gốc, và kiểm bằng cách đọc dấu vết.

**Pitfalls.** Bắt mọi ngoại lệ rồi bỏ qua · đóng tài nguyên trong nhánh thành công mà quên nhánh lỗi · dịch lỗi mà mất nguyên nhân gốc · thông báo lỗi chỉ ghi thất bại.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Sau 100 lần gây lỗi không còn kết nối nào mở, và mọi lỗi ở ranh giới đều giữ được nguyên nhân gốc trong dấu vết.

### Lesson 16 · CPython internals that change your decisions `LT`
**Prerequisites.** Lesson 15

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bốn chi tiết bên trong máy thực thi có ảnh hưởng thật tới quyết định thiết kế, phần còn lại thì không nên bận tâm ở mức này. Đếm tham chiếu cộng bộ dọn rác chu trình: đối tượng được giải phóng ngay khi không còn tham chiếu, nên vòng tham chiếu là chỗ duy nhất cần bộ dọn chu trình; hệ quả thực tế là giữ một tham chiếu quên xoá thì bộ nhớ không về. Cấp phát bộ nhớ theo khối nhỏ và vì sao bộ nhớ trả về hệ điều hành chậm hơn người ta tưởng. Khoá thông dịch toàn cục: chỉ một luồng chạy mã Python tại một thời điểm, **nhưng phát biểu thường gặp rằng luồng vô dụng là sai**, vì khoá được nhả trong lúc chờ vào ra và trong nhiều thư viện tính toán. Từ đó rút ra quy tắc chọn ở lesson 29 chứ chọn theo cảm tính. Mã byte ở mức khái niệm, đủ để biết vì sao một số phép viết nhanh hơn phép khác.

**Outcome.** Giải thích bằng cơ chế vì sao luồng vẫn hữu ích cho khối lượng công việc thiên vào ra, và đo được để chứng minh.

**Đánh giá.** Tầng *hiểu*. Objective là bác bỏ một hiểu lầm phổ biến bằng cơ chế cộng số đo. Kiểm bằng thí nghiệm hai loại khối lượng công việc; đạt khi số đo cho thấy đúng chiều và giải thích đúng vai trò của khoá.

**Lab.** Chạy cùng một tác vụ ở ba cấu hình một luồng, nhiều luồng và nhiều tiến trình, trên hai loại khối lượng công việc: một thiên CPU và một thiên vào ra. Lập bảng sáu ô. Giải thích từng ô bằng cơ chế khoá. Tạo một vòng tham chiếu và quan sát bộ nhớ không về cho tới khi bộ dọn chu trình chạy.

**Pitfalls.** Kết luận luồng vô dụng trong Python · dùng nhiều tiến trình cho tác vụ thiên vào ra · bỏ qua chi phí khởi động tiến trình khi so · đo một lần rồi kết luận.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng sáu ô có số đo thật, và giải thích đúng vì sao luồng thắng ở khối lượng công việc thiên vào ra.

### Lesson 17 · Packaging - project layout, build and reproducible environments `TH`
**Prerequisites.** Lesson 16

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Script chạy được trên máy mình không phải phần mềm, và ranh giới giữa hai thứ nằm ở chỗ người khác chạy lại được. Bố cục dự án và cách Python tìm mô đun: đường dẫn tìm kiếm, nhập tuyệt đối so với nhập tương đối, và nhập vòng cùng cách phá vòng. Tệp cấu hình dự án và hậu trường dựng gói: khác biệt giữa gói nguồn và gói dựng sẵn. Môi trường ảo giải bài toán xung đột phụ thuộc, còn tệp khoá phiên bản giải bài toán tái tạo: **không khoá phiên bản thì bản dựng hôm nay khác bản dựng hôm qua**, đúng vấn đề ghim phiên bản sẽ gặp lại ở M20. Đánh số phiên bản theo ngữ nghĩa và ý nghĩa với người dùng gói. Cấu hình theo thứ tự ưu tiên và ranh giới biến môi trường; bí mật không bao giờ vào kho mã hay vào nhật ký, quy tắc này lặp lại ở M19 và M21.

**Outcome.** Đóng gói một công cụ thành gói cài được với môi trường khoá phiên bản, và người khác tái tạo được trên máy trống.

**Đánh giá.** Tầng *áp dụng*. Objective là tiêu chí *clone, một lệnh, cùng kết quả* ở mức gói. Kiểm bằng phép thử tái tạo do người khác chạy; đạt khi họ cài và chạy được mà không phải sửa gì.

**Lab.** Chuyển công cụ CSV ở lesson 11 thành gói có tệp cấu hình dự án. Tạo môi trường ảo và khoá phiên bản. Dựng gói nguồn và gói dựng sẵn. Đưa cho một học viên khác cài trên máy trống từ gói dựng sẵn, chạy, và ghi lại mọi chỗ họ phải hỏi.

**Pitfalls.** Không khoá phiên bản · để cấu hình đường dẫn tuyệt đối của máy mình · đặt bí mật trong tệp cấu hình rồi nộp vào kho · nhập tương đối lung tung gây nhập vòng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Người khác cài từ gói dựng sẵn và chạy được trên máy trống mà không phải sửa gì, và môi trường tái tạo cho cùng danh sách phiên bản.

### Lesson 18 · Type hints and validation at the boundary `TH`
**Prerequisites.** Lesson 17

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Chú thích kiểu không làm chương trình chạy nhanh hơn, nó làm lỗi lộ ra sớm hơn và làm mã đọc được mà không phải đoán. Cú pháp đủ dùng: kiểu hợp, kiểu tuỳ chọn, kiểu tổng quát cho vùng chứa, và giao thức cho kiểu vịt có kiểm tra. Bộ kiểm kiểu tĩnh chạy trong tích hợp liên tục và ngưỡng chặn. Ranh giới quan trọng và hay bị nhầm: **chú thích kiểu là kiểm ở thời điểm dịch, không kiểm dữ liệu lúc chạy**; dữ liệu từ tệp, từ mạng hay từ cơ sở dữ liệu phải xác thực lúc chạy tại ranh giới nhận. Xác thực ở ranh giới chứ rải khắp nơi: vào tới trong thì dữ liệu đã đúng hình dạng và mã bên trong không phải kiểm lại. Lớp dữ liệu để mô tả bản ghi có cấu trúc thay vì dùng từ điển, và vì sao điều đó quan trọng với mã xử lý dữ liệu: từ điển sai khoá chỉ lộ ra lúc chạy, còn lớp dữ liệu lộ ra lúc kiểm.

**Outcome.** Thêm chú thích kiểu cho một gói tới mức bộ kiểm tĩnh sạch, và xác thực dữ liệu lúc chạy ở đúng ranh giới.

**Đánh giá.** Tầng *áp dụng*. Objective gồm hai cơ chế khác nhau mà người học hay gộp làm một. Kiểm bằng bộ kiểm tĩnh cộng thí nghiệm dữ liệu bẩn; đạt khi bộ kiểm sạch và dữ liệu sai hình dạng bị chặn ngay tại ranh giới.

**Lab.** Thêm chú thích kiểu cho gói ở lesson 17 tới khi bộ kiểm tĩnh sạch. Thêm xác thực lúc chạy tại ranh giới đọc tệp. Đưa vào 10 bản ghi sai hình dạng và chứng minh cả 10 bị chặn ở ranh giới với thông báo nêu rõ trường nào sai. Chứng minh mã bên trong không còn kiểm lại kiểu.

**Pitfalls.** Tưởng chú thích kiểu kiểm được dữ liệu lúc chạy · xác thực rải khắp mã · dùng từ điển cho bản ghi có cấu trúc · tắt bộ kiểm tĩnh vì nhiều cảnh báo.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bộ kiểm tĩnh sạch, 10 bản ghi sai đều bị chặn tại ranh giới với thông báo nêu đúng trường, và mã bên trong không kiểm lại kiểu.

### Lesson 19 · Testing - unit, integration, property and contract `TH`
**Prerequisites.** Lesson 18

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bốn loại phép kiểm trả lời bốn câu hỏi khác nhau, và dùng một loại cho mọi việc là cách vừa chậm vừa không bắt được lỗi. Phép kiểm đơn vị kiểm một đơn vị logic, nhanh, chạy mọi lúc. Phép kiểm tích hợp kiểm hai thành phần nói chuyện đúng với nhau, và đây là nơi bắt phần lớn lỗi thật trong mã dữ liệu. Phép kiểm tính chất sinh đầu vào ngẫu nhiên và kiểm một bất biến luôn đúng, rất hợp với mã biến đổi dữ liệu vì nó tìm ra ca biên mà con người không nghĩ ra. Phép kiểm hợp đồng kiểm hai bên vẫn hiểu giống nhau về giao diện. Bộ thay thế và ranh giới đặt chúng: chỉ thay thế ở ranh giới hệ ngoài, thay thế bên trong là tự kiểm mã giả của mình. Tính xác định: cố định thời gian và ngẫu nhiên, dùng thư mục tạm; phép kiểm chạy lúc được lúc không thì tệ hơn không có. Độ phủ không đồng nghĩa chất lượng.

**Outcome.** Viết đủ bốn loại phép kiểm cho một gói, và chứng minh phép kiểm tính chất bắt được ca biên mà phép kiểm đơn vị bỏ sót.

**Đánh giá.** Tầng *áp dụng*. Objective đòi chọn đúng loại phép kiểm cho từng mục tiêu, chứ tăng độ phủ. Kiểm bằng bài tiêm lỗi; đạt khi bộ kiểm bắt được ít nhất bốn trong năm lỗi và phép kiểm tính chất bắt ít nhất một ca mà phép kiểm đơn vị bỏ sót.

**Lab.** Viết cả bốn loại phép kiểm cho gói ở lesson 18. Giảng viên tiêm năm lỗi vào mã. Chạy bộ kiểm và ghi lỗi nào bị bắt bởi loại nào. Cố định thời gian và ngẫu nhiên, chạy bộ kiểm 20 lần liên tiếp và chứng minh kết quả không đổi.

**Pitfalls.** Thay thế cả thành phần bên trong · viết phép kiểm phụ thuộc thời gian thật · chạy theo độ phủ · bỏ phép kiểm tích hợp vì chậm.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bộ kiểm bắt ≥ 4/5 lỗi tiêm, phép kiểm tính chất bắt ≥ 1 ca mà phép kiểm đơn vị bỏ sót, và 20 lần chạy cho kết quả giống nhau.

### Lesson 20 · Structured logging, correlation and actionable errors `TH`
**Prerequisites.** Lesson 19

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Nhật ký là thứ duy nhất còn lại khi sự cố đã qua, nên thiết kế nhật ký là thiết kế khả năng chẩn đoán về sau. Nhật ký có cấu trúc thay vì chuỗi tự do: có cấu trúc thì truy vấn và tổng hợp được, còn chuỗi tự do thì chỉ đọc mắt được. Bốn mức và quy tắc dùng từng mức, cùng lý do để mức gỡ lỗi chạy trong sản xuất là cách làm hoá đơn tăng mà không ai đọc. Mã theo dõi nối mọi dòng thuộc cùng một lần chạy hoặc cùng một bản ghi; đây là cơ chế sẽ dùng lại xuyên suốt tới M21 để truy ngược một bản ghi sai về lô nạp sinh ra nó. Ghi cái gì ở ranh giới: đầu vào tóm tắt, quyết định đã lấy, và kết quả. Không ghi bí mật và không ghi dữ liệu cá nhân, quy tắc nối tới M21. Thông báo lỗi dùng được nêu bốn thứ: cái gì hỏng, ở đâu, với dữ liệu nào, và nên làm gì.

**Outcome.** Dựng nhật ký có cấu trúc kèm mã theo dõi, và truy được toàn bộ đường đi của một bản ghi chỉ bằng mã đó.

**Đánh giá.** Tầng *áp dụng*. Objective là một thiết kế kiểm được bằng phép truy ngược thật. Kiểm bằng bài truy ngược; đạt khi truy được đủ đường đi của bản ghi bằng một truy vấn theo mã theo dõi.

**Lab.** Thêm nhật ký có cấu trúc và mã theo dõi vào gói. Chạy trên 10.000 bản ghi trong đó có 3 bản lỗi. Với mỗi bản lỗi, truy toàn bộ đường đi chỉ bằng mã theo dõi và dựng lại chuyện đã xảy ra. Kiểm nhật ký không chứa bí mật bằng một phép quét.

**Pitfalls.** Ghi nhật ký dạng chuỗi tự do · không có mã theo dõi · để mức gỡ lỗi trong sản xuất · ghi cả bản ghi đầy đủ vào nhật ký gồm cả dữ liệu cá nhân.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Truy được đủ đường đi của cả 3 bản lỗi bằng một truy vấn theo mã theo dõi, và phép quét không tìm thấy bí mật trong nhật ký.

### Lesson 21 · Profiling before optimising `TH`
**Prerequisites.** Lesson 20

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Tối ưu dựa trên phỏng đoán là cách tốn thời gian vào chỗ không quan trọng, nên quy tắc không thoả hiệp là **đo trước khi sửa**. Ba loại đo cho ba loại nút thắt: đo CPU theo hàm để biết thời gian tiêu ở đâu, đo bộ nhớ theo dòng để tìm chỗ giữ dữ liệu, và đo vào ra để biết đang chờ đĩa hay chờ mạng. Đo lấy mẫu so với đo có dụng cụ: cái đầu nhẹ và dùng được trong sản xuất, cái sau chi tiết hơn nhưng làm chương trình chậm nên số đo lệch. Cách chạy so sánh đúng: có giai đoạn khởi động, lặp nhiều lần, có mốc so sánh, và cố định dữ liệu; ba cách làm số đo vô nghĩa gồm đầu vào quá nhỏ, bộ nhớ đệm đã ấm, và không lặp. Nguyên tắc rút ra và dùng lại ở M18: sửa nút thắt lớn nhất, đo lại, rồi mới sang nút thắt kế tiếp; sửa nhiều chỗ cùng lúc thì không biết chỗ nào có tác dụng.

**Outcome.** Định vị nút thắt của một chương trình bằng số đo, sửa đúng nó, và định lượng phần cải thiện.

**Đánh giá.** Tầng *phân tích*. Objective là truy từ tổng thời gian về một hàm cụ thể bằng dữ liệu đo. Kiểm bằng cặp số đo trước sau; đạt khi định vị đúng nút thắt và cải thiện đo được mà kết quả không đổi.

**Lab.** Nhận một chương trình xử lý dữ liệu chạy chậm. Đo CPU, bộ nhớ và vào ra. Viết dự đoán nút thắt trước khi đo, rồi đối chiếu. Sửa đúng một chỗ, đo lại, ghi mức cải thiện. Chạy lại bộ kiểm để chứng minh kết quả không đổi. Cố ý chạy một phép so sánh sai cách và chỉ ra nó sai ở đâu.

**Pitfalls.** Tối ưu theo cảm giác · sửa nhiều chỗ cùng lúc · so sánh không có giai đoạn khởi động · tối ưu một hàm chiếm 2% tổng thời gian.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Định vị đúng nút thắt bằng số đo, cải thiện có số, bộ kiểm vẫn xanh, và chỉ ra được chỗ sai của phép so sánh sai cách.

### Lesson 22 · Threads - shared memory, races and locks `TH`
**Prerequisites.** Lesson 21

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Luồng dùng chung bộ nhớ, nên nhanh khi chia sẻ dữ liệu và nguy hiểm vì hai luồng có thể sửa cùng một chỗ. Điều kiện tranh đoạt: kết quả phụ thuộc vào thứ tự thực thi, nên chương trình chạy đúng 99 lần và sai lần thứ 100, và đây là loại lỗi khó tái hiện nhất. Vùng tranh chấp và khoá; khoá chết khi hai luồng giữ chéo nhau và chờ nhau, cùng bốn điều kiện cần để nó xảy ra. Thao tác nguyên tử và vì sao một phép tăng biến đơn giản không nguyên tử. Hàng đợi có giới hạn là cách chia việc giữa các luồng an toàn hơn chia sẻ biến, vì nó gói việc đồng bộ vào một chỗ. Khi nào luồng là lựa chọn đúng: khối lượng công việc thiên vào ra, theo đúng kết luận đã đo ở lesson 16. Tắt có kiểm soát: luồng phải nhận được tín hiệu dừng và kết thúc công việc đang dở chứ bị cắt ngang.

**Outcome.** Tái hiện được một điều kiện tranh đoạt một cách xác định và sửa bằng cơ chế đồng bộ đúng.

**Đánh giá.** Tầng *phân tích*. Objective đòi biến một lỗi ngẫu nhiên thành lỗi tái hiện được, kỹ năng khó và dùng lại ở M5. Kiểm bằng bài tái hiện cộng sửa; đạt khi tái hiện được 10/10 lần trước khi sửa và 0/1000 lần sau khi sửa.

**Lab.** Viết một bộ đếm dùng chung cho 8 luồng và chứng minh kết quả sai. Tăng khả năng tái hiện bằng cách chèn điểm dừng, đạt 10/10 lần sai. Sửa bằng khoá, chạy 1000 lần và xác nhận không sai lần nào. Tạo một khoá chết có chủ ý, chẩn đoán và sửa bằng cách sắp thứ tự lấy khoá.

**Pitfalls.** Kết luận lỗi ngẫu nhiên nên bỏ qua · thêm khoá khắp nơi rồi mất hết tác dụng của nhiều luồng · dùng luồng cho tác vụ thiên CPU · cắt ngang luồng thay vì báo dừng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tái hiện sai 10/10 lần trước khi sửa, 0/1000 lần sau khi sửa, và chẩn đoán được khoá chết bằng bốn điều kiện.

### Lesson 23 · Processes - isolation, serialization and cost `TH`
**Prerequisites.** Lesson 22

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Tiến trình có bộ nhớ riêng, nên không có điều kiện tranh đoạt trên biến dùng chung, đổi lại mọi thứ truyền qua lại phải tuần tự hoá. Ba chi phí phải tính trước khi chọn: thời gian khởi động một tiến trình, bộ nhớ nhân lên theo số tiến trình, và chi phí tuần tự hoá dữ liệu qua lại. Hệ quả thực tế hay bị bất ngờ: chia một việc nhỏ cho nhiều tiến trình có thể **chậm hơn** làm tuần tự, vì chi phí truyền lớn hơn phần tiết kiệm. Khi nào tiến trình là lựa chọn đúng: khối lượng công việc thiên CPU, theo bảng đo ở lesson 16. Hồ tiến trình và cách chia việc theo khối thay vì theo từng phần tử để giảm số lần truyền. Điều gì không truyền được qua ranh giới tiến trình và cách xử lý. Tắt có kiểm soát với hồ tiến trình: tiến trình con phải được dừng sạch, nếu không thì chúng thành tiến trình mồ côi.

**Outcome.** Chọn giữa tiến trình và tuần tự cho một khối lượng công việc cho trước, dẫn bằng số đo gồm cả chi phí truyền.

**Đánh giá.** Tầng *đánh giá*. Objective đòi cân chi phí song song với phần tiết kiệm, chứ mặc định song song là nhanh. Kiểm bằng bảng ba kích thước công việc; đạt khi chỉ ra đúng điểm giao mà dưới đó tuần tự thắng.

**Lab.** Chạy cùng phép tính thiên CPU ở ba kích thước dữ liệu, mỗi kích thước ở hai chế độ tuần tự và nhiều tiến trình. Đo thời gian và bộ nhớ. Tìm điểm giao. Đổi cách chia từ từng phần tử sang theo khối và đo lại phần cải thiện. Giết tiến trình chính và kiểm tiến trình con có mồ côi không.

**Pitfalls.** Song song hoá mọi thứ · chia theo từng phần tử · bỏ qua bộ nhớ khi tăng số tiến trình · để tiến trình con mồ côi khi tiến trình chính chết.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng ba kích thước nhân hai chế độ đủ thời gian và bộ nhớ, chỉ ra đúng điểm giao, và không còn tiến trình mồ côi sau khi giết tiến trình chính.

### Lesson 24 · Asyncio - the event loop, cancellation and timeouts `TH`
**Prerequisites.** Lesson 23

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Mô hình thứ ba, hợp nhất với khối lượng công việc có rất nhiều thao tác chờ mạng cùng lúc. Vòng lặp sự kiện chạy trên một luồng và chuyển qua lại giữa các tác vụ ở những điểm chờ; nên hàng nghìn kết nối đồng thời không tốn hàng nghìn luồng. Chi tiết quyết định thành bại: **một lời gọi chặn nằm trong hàm bất đồng bộ sẽ khoá cả vòng lặp**, nên mọi thứ khác đứng im, và đây là lỗi phổ biến nhất khi mới dùng. Cách phát hiện lời gọi chặn và cách đẩy nó sang luồng riêng. Huỷ bỏ là công dân hạng nhất: tác vụ phải xử lý được việc bị huỷ giữa chừng và dọn dẹp tài nguyên. Hết giờ đặt ở mọi lời gọi ra ngoài, không có ngoại lệ, vì không đặt là chờ vô hạn. Giới hạn đồng thời bằng cờ hiệu có giới hạn để không mở 10.000 kết nối cùng lúc và làm sập bên kia.

**Outcome.** Viết một trình thu thập bất đồng bộ có giới hạn đồng thời, hết giờ và huỷ bỏ đúng, không có lời gọi chặn nào trong vòng lặp.

**Đánh giá.** Tầng *áp dụng*. Objective gồm ba cơ chế bắt buộc kiểm được bằng thực nghiệm. Kiểm bằng ba phép thử; đạt khi không lời gọi chặn nào lọt, hết giờ kích hoạt đúng, và huỷ bỏ dọn sạch tài nguyên.

**Lab.** Viết trình thu thập gọi 500 địa chỉ với giới hạn 20 kết nối đồng thời. Cố ý chèn một lời gọi chặn và đo tác động lên toàn vòng lặp, rồi sửa bằng cách đẩy sang luồng riêng. Đặt hết giờ và kiểm nó kích hoạt. Huỷ toàn bộ giữa chừng và chứng minh mọi kết nối được đóng.

**Pitfalls.** Gọi hàm chặn trong hàm bất đồng bộ · không đặt hết giờ · mở không giới hạn kết nối · bỏ qua việc dọn dẹp khi bị huỷ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Không lời gọi chặn nào trong vòng lặp, hết giờ kích hoạt đúng ngưỡng, và sau khi huỷ thì mọi kết nối đã đóng.

### Lesson 25 · Coroutine, task and future - the state model `TH`
**Prerequisites.** Lesson 24

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài mở phần bất đồng bộ sâu bằng việc tách bốn thứ hay bị gọi chung là tác vụ. Hàm hiệp trình là hàm được khai báo bất đồng bộ; gọi nó **không chạy gì cả**, chỉ tạo ra một đối tượng hiệp trình, và quên chờ nó là nguồn của lỗi im lặng đầu tiên mà người mới gặp. Đối tượng chờ được là bất cứ thứ gì đặt sau từ khoá chờ. Tác vụ là một hiệp trình đã được giao cho vòng lặp sự kiện chạy, nên nó có vòng đời độc lập. Tương lai là chỗ giữ kết quả chưa có. Năm trạng thái phải truy được: vừa tạo, đang chạy, đang tạm dừng, đã xong, và đã bị huỷ; phân biệt đã xong vì trả kết quả, vì ném ngoại lệ, và vì bị huỷ. Ngoại lệ trong một tác vụ không ai chờ thì bị nuốt tới lúc chương trình kết thúc mới in ra. Liệt kê tác vụ đang sống là công cụ chẩn đoán chính.

**Outcome.** Truy được trạng thái của một tác vụ qua đủ năm giai đoạn và chỉ ra hai cách một lỗi bị nuốt.

**Đánh giá.** Tầng *phân tích*. Objective đòi quan sát trạng thái thời gian chạy chứ đọc tài liệu. Kiểm bằng bài truy trạng thái; đạt khi năm trạng thái được quan sát bằng công cụ và hai ca lỗi bị nuốt được tái hiện.

**Lab.** Viết chương trình tạo bốn tác vụ: một chạy xong, một ném ngoại lệ, một bị huỷ, một treo. Sau mỗi bước, liệt kê tác vụ đang sống và ghi trạng thái từng cái. Tái hiện hai ca lỗi bị nuốt: gọi hàm hiệp trình mà không chờ, và tạo tác vụ rồi không ai lấy kết quả. Bật chế độ gỡ lỗi của thư viện bất đồng bộ và ghi lại cảnh báo nó đưa ra.

**Pitfalls.** Gọi hàm hiệp trình mà quên chờ · tạo tác vụ rồi không giữ tham chiếu · nhầm đối tượng hiệp trình với tác vụ đang chạy · không bao giờ liệt kê tác vụ đang sống.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Năm trạng thái được quan sát bằng công cụ, và hai ca lỗi bị nuốt được tái hiện cùng chỉ ra cách phát hiện.

### Lesson 26 · Structured concurrency - TaskGroup, ownership and cancellation safety `TH`
**Prerequisites.** Lesson 25

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Tác vụ tạo ra rồi bỏ mặc là nguồn của rò rỉ và của lỗi biến mất, nên bài này đặt ra một kỷ luật sở hữu. Đồng thời có cấu trúc buộc mọi tác vụ con thuộc một phạm vi cha, và **phạm vi cha không được rời khỏi khi còn tác vụ con đang chạy**. Bốn bảo đảm kéo theo: một tác vụ con hỏng thì các anh em bị huỷ; ngoại lệ được gom lại chứ mất; phạm vi chờ dọn dẹp xong mới thoát; và không còn tác vụ mồ côi khi tắt. Huỷ bỏ an toàn là phần khó: tín hiệu huỷ tới ở một điểm chờ bất kỳ, nên mọi tài nguyên phải nằm trong khối dọn dẹp hoặc trình quản lý ngữ cảnh bất đồng bộ; **nuốt tín hiệu huỷ để chạy nốt là lỗi nghiêm trọng** vì nó làm việc tắt treo. Dọn dẹp trong lúc bị huỷ cần được che chắn để bản thân nó không bị huỷ giữa chừng.

**Outcome.** Dựng phạm vi đồng thời có cấu trúc đạt bốn bảo đảm và chứng minh không còn tác vụ mồ côi khi tắt.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu đếm được là số tác vụ còn sống và số tài nguyên chưa đóng. Kiểm bằng ba kịch bản tắt; đạt khi số tác vụ còn sống bằng không và số kết nối rò bằng không ở cả ba.

**Lab.** Viết một dịch vụ mở 50 tác vụ con trong một phạm vi có cấu trúc. Chạy ba kịch bản: một tác vụ con ném ngoại lệ, phạm vi bị huỷ từ ngoài, và nhận tín hiệu tắt. Sau mỗi kịch bản, đếm tác vụ còn sống và bộ mô tả tệp còn mở. Viết một bản không có cấu trúc để so và định lượng số tác vụ mồ côi.

**Pitfalls.** Tạo tác vụ rời rồi quên · nuốt tín hiệu huỷ để chạy nốt · dọn dẹp mà không che chắn nên bị huỷ giữa chừng · rời phạm vi khi tác vụ con còn chạy.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Số tác vụ còn sống và số kết nối rò đều bằng không ở cả ba kịch bản, và bản không có cấu trúc được định lượng số tác vụ mồ côi.

### Lesson 27 · End-to-end deadlines and backpressure `TH`
**Prerequisites.** Lesson 26

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hai cơ chế giữ một dịch vụ bất đồng bộ không sụp dưới tải, và cả hai đều bị hiểu nhầm là hết giờ. Hết giờ cục bộ đặt cho từng lời gọi; hạn chót đầu cuối là tổng ngân sách cho cả yêu cầu. Khác biệt có hậu quả cụ thể: ba chặng mỗi chặng hết giờ 10 giây cho phép một yêu cầu chạy 30 giây, và nếu mỗi chặng còn thử lại thì con số nhân lên nữa; **hết giờ cục bộ cộng thử lại tạo ra khuếch đại thời gian chờ**. Cách đúng là truyền ngân sách còn lại xuống từng chặng, và chặng nào thấy ngân sách cạn thì bỏ sớm thay vì thử. Áp lực ngược giới hạn phía sản xuất bằng hàng đợi có giới hạn, cờ hiệu và bể kết nối có giới hạn; khi đầy thì phải chọn tường minh một trong bốn hành vi là từ chối, chờ, loại bớt, hoặc giảm chất lượng. Giữ một kết nối qua một điểm chờ dài làm cạn bể, là chế độ hỏng đặc trưng.

**Outcome.** Cài truyền hạn chót đầu cuối và áp lực ngược, chứng minh yêu cầu không vượt ngân sách và bể không bị cạn.

**Đánh giá.** Tầng *áp dụng*. Objective có hai tiêu chí nghiệm thu đo được dưới tải. Kiểm bằng phép thử tải có chặng chậm; đạt khi phân vị 99 của thời gian yêu cầu nằm trong ngân sách và không lần nào bể kết nối cạn.

**Lab.** Dựng dịch vụ ba chặng, mỗi chặng gọi một phụ thuộc có thể chậm. Cài bản chỉ có hết giờ cục bộ cộng thử lại, chạy tải với một chặng chậm, và đo phân vị 99. Cài bản truyền hạn chót và đo lại. Thêm hàng đợi có giới hạn cùng bể kết nối có giới hạn, chọn tường minh hành vi khi đầy. Tạo một đoạn giữ kết nối qua điểm chờ dài và quan sát bể cạn.

**Pitfalls.** Chỉ đặt hết giờ cục bộ rồi tin yêu cầu có giới hạn · thử lại ở mọi chặng mà không có ngân sách chung · để hàng đợi không giới hạn · giữ kết nối qua một điểm chờ dài.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân vị 99 của thời gian yêu cầu nằm trong ngân sách hạn chót, và không lần nào bể kết nối cạn dưới tải.

### Lesson 28 · Async failure injection - six failure modes `TH`
**Prerequisites.** Lesson 27

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài khép phần bất đồng bộ bằng cách tiêm lỗi có chủ ý, vì sáu chế độ hỏng dưới đây đều không lộ ra khi chạy thuận lợi. Vòng lặp trễ vì một lời gọi chặn hoặc một vòng tính toán dài: bằng chứng là số đo độ trễ của vòng lặp, phòng thủ là đẩy sang luồng hoặc tiến trình riêng. Tác vụ mồ côi vì tạo rồi bỏ: bằng chứng là danh sách tác vụ còn sống lúc tắt. Rò rỉ khi huỷ vì dọn dẹp không chạy: bằng chứng là số bộ mô tả tệp tăng dần. Khuếch đại thời gian chờ theo lesson 27. Cạn bể kết nối. Bão thử lại khi nhiều tác vụ cùng thử lại một lúc: bằng chứng là đỉnh tải đồng bộ, phòng thủ là ngân sách thử lại cùng nhiễu ngẫu nhiên. **Mỗi chế độ hỏng phải có một phép thử tự động tái hiện được**, nếu không nó sẽ quay lại. Sáu tình huống tiêm gồm lời gọi chặn, ổ cắm treo, ngoại lệ trong tác vụ, huỷ giữa một giao dịch, hàng đợi đầy, và tín hiệu tắt.

**Outcome.** Tái hiện sáu chế độ hỏng bằng phép thử tự động và chứng minh phòng thủ tương ứng có hiệu lực.

**Đánh giá.** Tầng *đánh giá*. Objective tổng hợp bốn bài trước thành một hệ phòng vệ có bằng chứng. Kiểm bằng sáu phép thử tiêm; đạt khi cả sáu tái hiện được tự động và ít nhất năm có phòng thủ chứng minh bằng số đo trước sau.

**Lab.** Viết sáu phép thử tiêm lỗi chạy tự động. Với mỗi cái, ghi lại bằng chứng quan sát được trước khi phòng thủ, áp phòng thủ, rồi đo lại. Chạy phép thử tắt có kiểm soát nhận tín hiệu kết thúc và chứng minh mọi giao dịch đang dở hoặc hoàn tất hoặc quay lui. Lập bảng sáu hàng gồm cơ chế, bằng chứng và phòng thủ.

**Pitfalls.** Thử bằng tay một lần rồi coi là xong · huỷ giữa một giao dịch mà không định nghĩa ranh giới công bố · đo phòng thủ mà không đo trước · bỏ tình huống tín hiệu tắt vì khó tái hiện.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Sáu phép thử tiêm chạy tự động, ≥ 5 phòng thủ có số đo trước sau, và tắt có kiểm soát không để giao dịch dở dang.

### Lesson 29 · Choosing a concurrency model from the workload `LT`
**Prerequisites.** Lesson 28

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài chốt phần đồng thời, và nó biến ba bài trước thành một quy tắc quyết định. Ba câu hỏi theo thứ tự: công việc này chờ hay tính, có cần chia sẻ trạng thái không, và quy mô đồng thời là bao nhiêu. Bảng quyết định: thiên CPU thì nhiều tiến trình; thiên vào ra với vài chục đồng thời thì luồng đủ và đơn giản hơn; thiên vào ra với hàng nghìn đồng thời thì bất đồng bộ. Lựa chọn thứ tư hay bị bỏ qua và thường đúng nhất: **không đồng thời**, vì mã tuần tự dễ đọc và dễ gỡ hơn nhiều, và phần lớn công việc dữ liệu theo lô không cần đồng thời trong tiến trình mà cần chia việc ở tầng trên, đúng cách M14 và M18 làm. Ba dấu hiệu cho thấy đã chọn sai. Mọi kết luận ở bài này phải dẫn về bảng số đo của chính mình ở lesson 16, 22, 23 và 24 chứ về lời khuyên chung.

**Outcome.** Chọn mô hình đồng thời cho bốn khối lượng công việc cho trước, mỗi lần dẫn về một số đo đã tự đo.

**Đánh giá.** Tầng *đánh giá*. Objective đòi áp một quy tắc quyết định có bằng chứng, chuẩn bị cho mọi module vận hành sau. Kiểm bằng bốn khối lượng công việc trong đó ít nhất một không nên đồng thời; đạt khi chọn đúng ít nhất ba và nhận ra trường hợp không nên đồng thời.

**Lab.** Cho bốn khối lượng công việc. Với mỗi cái, chọn mô hình và dẫn một số đo từ lesson 16, 22, 23 hoặc 24 làm căn cứ. Với khối lượng công việc không nên đồng thời, ước lượng phần phức tạp thêm vào so với phần thời gian tiết kiệm được.

**Pitfalls.** Chọn theo mô hình đang thịnh hành · dùng bất đồng bộ cho việc thiên CPU · bỏ qua phương án không đồng thời · dẫn lời khuyên thay vì dẫn số đo.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chọn đúng ≥ 3/4 khối lượng công việc với số đo dẫn chứng, và nhận ra đúng trường hợp không nên đồng thời.

### Lesson 30 · A resilient worker - retry, backoff, idempotency and shutdown `TH`
**Prerequisites.** Lesson 29

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài ghép mọi thứ của module thành mẫu sẽ dùng lại ở M14B, M16 và M21. Bốn tính chất của một tiến trình xử lý đáng tin. Thử lại có lùi theo hàm mũ và nhiễu ngẫu nhiên: thử lại ngay lập tức làm sự cố nặng thêm vì mọi tiến trình cùng thử lại một lúc; nhiễu ngẫu nhiên phá sự đồng pha đó. Chỉ thử lại lỗi tạm thời, còn lỗi dữ liệu thì thử lại vô ích và phải tách ra. Khoá bất biến: vì thử lại nghĩa là cùng một việc chạy hai lần, nên ghi phải cho cùng kết quả khi lặp; đây là nguyên tắc nền của cả chương trình và sẽ quay lại ở M14 và M16. Hàng đợi có giới hạn giữa các giai đoạn để tạo áp lực ngược thay vì dồn vô hạn. Tắt có kiểm soát: nhận tín hiệu, ngừng nhận việc mới, hoàn tất việc đang dở trong hạn, rồi thoát với mã đúng.

**Outcome.** Viết một tiến trình xử lý đạt bốn tính chất và chứng minh bằng thí nghiệm giết tiến trình rằng không mất và không trùng việc.

**Đánh giá.** Tầng *sáng tạo*. Objective đòi ghép bốn cơ chế rời thành một mẫu chạy được dưới sự cố. Kiểm bằng thí nghiệm giết tiến trình 20 lần; đạt khi đối soát khớp tuyệt đối và tắt có kiểm soát hoàn tất trong hạn.

**Lab.** Viết tiến trình xử lý đọc từ hàng đợi có giới hạn và ghi vào tệp kết quả có khoá bất biến. Tiêm lỗi tạm thời và lỗi dữ liệu, chứng minh chỉ loại đầu được thử lại. Giết tiến trình 20 lần ở các thời điểm ngẫu nhiên, khởi động lại, và đối soát kết quả với đầu vào. Gửi tín hiệu dừng và đo thời gian tắt.

**Pitfalls.** Thử lại mọi loại lỗi · thử lại ngay không lùi và không nhiễu · ghi không bất biến rồi sinh trùng khi thử lại · bỏ qua tín hiệu dừng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Sau 20 lần giết và khởi động lại, đối soát khớp tuyệt đối; lỗi dữ liệu không bị thử lại; và tắt có kiểm soát xong trong hạn.

### Lesson 31 · Continuous integration for a Python package `TH`
**Prerequisites.** Lesson 30

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Tích hợp liên tục biến kỷ luật cá nhân thành ràng buộc của cả kho, và bài này dựng bộ khung dùng cho mọi module sau. Các bước tối thiểu theo thứ tự chạy nhanh trước: định dạng và soát lỗi tĩnh, kiểm kiểu, phép kiểm đơn vị, phép kiểm tích hợp, dựng gói, và quét bí mật. Cửa chặn hợp nhất: nhánh chính chỉ nhận thay đổi khi mọi bước xanh, nếu không thì quy trình chỉ là trang trí. Chạy trên nhiều phiên bản Python nếu gói tuyên bố hỗ trợ nhiều phiên bản. Bộ nhớ đệm phụ thuộc để vòng lặp phản hồi đủ nhanh, vì quy trình chạy 20 phút là quy trình người ta tìm cách vòng qua. Quét bí mật cả lịch sử kho chứ chỉ mã hiện tại, vì xoá ở lần nộp sau không xoá được ở lần nộp trước. Mã thoát và thông báo hỏng phải nói được hỏng ở bước nào, nối lại nguyên tắc thông báo lỗi ở lesson 15.

**Outcome.** Dựng quy trình tích hợp liên tục sáu bước có cửa chặn hợp nhất, với thời gian phản hồi dưới ngưỡng.

**Đánh giá.** Tầng *áp dụng*. Objective là một cấu hình có hai ràng buộc đo được là tính chặn và thời gian. Kiểm bằng phép thử nộp mã hỏng; đạt khi mọi loại hỏng đều bị chặn và thời gian chạy dưới ngưỡng.

**Lab.** Dựng quy trình sáu bước cho gói. Bật cửa chặn hợp nhất. Nộp năm yêu cầu hợp nhất hỏng theo năm cách khác nhau, mỗi cách ứng với một bước, và xác nhận cả năm bị chặn ở đúng bước. Bật bộ nhớ đệm phụ thuộc và đo thời gian trước sau.

**Pitfalls.** Cho phép hợp nhất khi quy trình đỏ · đặt bước chậm lên đầu · không quét lịch sử kho · thông báo hỏng không nói hỏng ở bước nào.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Năm yêu cầu hỏng đều bị chặn ở đúng bước, thời gian chạy dưới ngưỡng sau khi bật bộ nhớ đệm, và cửa chặn hợp nhất hoạt động.

### Lesson 32 · Python project - a packaged, tested, observable tool `DA`
**Prerequisites.** Lesson 31

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Bài dự án khép module. Nâng công cụ CSV ở lesson 11 thành một gói đạt chuẩn sản xuất. Danh mục kiểm tám điểm, mỗi điểm đến từ một bài: đóng gói cài được và môi trường khoá phiên bản; chú thích kiểu sạch với bộ kiểm tĩnh; xác thực dữ liệu tại ranh giới; đủ bốn loại phép kiểm; nhật ký có cấu trúc và mã theo dõi; hồ sơ đo hiệu năng có trước và sau; mô hình đồng thời chọn có số đo; và quy trình tích hợp liên tục xanh có cửa chặn. Phép thử nghiệm thu gồm hai phần: một học viên khác cài từ gói dựng sẵn trên máy trống và chạy được; và công cụ chịu được 20 lần giết tiến trình giữa chừng mà đối soát vẫn khớp. Bằng chứng nộp kèm: bảng danh mục kiểm tám điểm, mỗi điểm dẫn tới một tệp hoặc một số đo cụ thể.

**Outcome.** Nộp một gói đạt cả tám điểm danh mục kiểm, qua được phép thử cài trên máy trống và phép thử giết tiến trình.

**Đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module thành một sản phẩm đạt chuẩn. Kiểm bằng hai phép thử nghiệm thu cộng rà soát danh mục; đạt khi cả tám điểm có bằng chứng và cả hai phép thử qua.

**Lab.** Nâng công cụ thành gói đạt tám điểm. Nộp bảng danh mục kiểm, mỗi điểm dẫn tới tệp hoặc số đo. Đưa cho một học viên khác cài trên máy trống. Chạy phép thử giết tiến trình 20 lần và đối soát.

**Pitfalls.** Bỏ phần đo hiệu năng vì thấy công cụ đủ nhanh · chọn mô hình đồng thời mà không dẫn số đo · nộp khi quy trình còn đỏ · dẫn bằng chứng chung chung.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Tám điểm đều dẫn được tới tệp hoặc số đo, người khác cài và chạy được trên máy trống, và 20 lần giết tiến trình vẫn đối soát khớp.

# MODULE M3 · DATA STRUCTURES AND ALGORITHMS FOR SYSTEMS

**Phase 1 · Lessons 33–44 · 24.4 giờ**

| | |
|---|---|
| **Objective cấp module** | Chọn cấu trúc dữ liệu theo mẫu truy cập, tính cục bộ và tỉ lệ đọc ghi, rồi bảo vệ lựa chọn bằng số đo chứ bằng ký hiệu độ phức tạp |
| **Tiền đề** | M2 |
| **Exit criterion** | Với mỗi cấu trúc đã học, nêu được độ phức tạp thao tác, cách xếp trong bộ nhớ, khối lượng công việc phù hợp, và ca biên làm nó sụp |
| **Kỹ năng SFIA** | `PROG` mức 4 · `HPCC` mức 3 |
| **Chế độ hỏng** | Học độ phức tạp như công thức để đọc, rồi không giải thích được vì sao một phép quét tuyến tính thắng một cấu trúc có độ phức tạp tốt hơn |

Module này không phải luyện phỏng vấn thuật toán. Mục tiêu là nối cấu trúc dữ liệu với những thứ sẽ gặp ở tầng hệ thống: bảng băm nối với phép kết băm ở M9 và M18, cây B nối với chỉ mục ở M10, đồ thị nối với đồ thị phụ thuộc ở M14 và lineage ở M14D, bộ lọc Bloom nối với cấu trúc gộp theo nhật ký ở M10.

Nguyên tắc xuyên suốt: mọi kết luận về hiệu năng phải dẫn về một phép đo, vì hằng số nhân và tính cục bộ của bộ nhớ đệm thường lấn át bậc độ phức tạp ở quy mô thật.

### Lesson 33 · Complexity, constant factors and benchmark bias `LT`
**Prerequisites.** Module 3: M2

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Ký hiệu độ phức tạp mô tả xu hướng khi dữ liệu lớn dần, nó không nói gì về tốc độ ở quy mô cụ thể, và nhầm hai thứ này là nguồn của rất nhiều quyết định sai. Ba loại phân tích và khi nào dùng loại nào: xấu nhất cho cam kết, trung bình cho kỳ vọng, và khấu hao cho cấu trúc có thao tác đắt thỉnh thoảng như mảng động. Hằng số nhân và vì sao nó quan trọng: một thuật toán bậc tuyến tính với hằng số nhỏ thường thắng một thuật toán bậc lôgarit với hằng số lớn trong khoảng dữ liệu thực tế của phần lớn hệ. Chi phí theo bộ nhớ đệm: đọc một ô nhớ liền kề rẻ hơn nhiều so với nhảy lung tung, nên cách xếp dữ liệu trong bộ nhớ ảnh hưởng tới tốc độ không kém gì thuật toán, và điều này sẽ quay lại ở M4. Bốn cách làm phép so sánh vô nghĩa và cách tránh từng cái, nối lại kỷ luật đo ở lesson 21.

**Outcome.** Dự đoán và kiểm chứng điểm giao giữa hai cách cài đặt có bậc độ phức tạp khác nhau trên dữ liệu thật.

**Đánh giá.** Tầng *phân tích*. Objective đòi nối lý thuyết với số đo và giải thích chênh lệch, chứ tính bậc. Kiểm bằng bài đo có điểm giao; đạt khi tìm ra điểm giao và giải thích đúng bằng hằng số nhân hoặc tính cục bộ.

**Lab.** Cài hai cách tìm kiếm trên dữ liệu đã sắp xếp: quét tuyến tính và tìm nhị phân. Đo trên tám kích thước từ 8 tới 1 triệu phần tử. Vẽ đồ thị và tìm điểm giao. Giải thích vì sao quét tuyến tính thắng ở dưới điểm đó. Cố ý chạy một phép so sánh có bộ nhớ đệm đã ấm và chỉ ra nó lệch bao nhiêu.

**Pitfalls.** Chọn cấu trúc chỉ theo bậc độ phức tạp · đo với dữ liệu quá nhỏ · không lặp lại phép đo · bỏ qua giai đoạn khởi động.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tìm được điểm giao bằng số đo, và giải thích đúng nguyên nhân bằng hằng số nhân hoặc tính cục bộ.

### Lesson 34 · Arrays, dynamic arrays and memory layout `TH`
**Prerequisites.** Lesson 33

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Mảng liên tục là cấu trúc nền của gần như mọi thứ nhanh, vì nó cho truy cập ngẫu nhiên theo chỉ số và cho phép đọc tuần tự với tính cục bộ tốt nhất. Mảng động thêm khả năng lớn lên: khi đầy thì cấp vùng lớn hơn và sao chép sang, và nhân đôi kích thước cho chi phí khấu hao hằng số cho mỗi lần thêm. Từ đó suy ra hai hệ quả thực tế: thêm vào cuối rẻ còn chèn vào giữa đắt vì phải dịch chuyển; và biết trước kích thước rồi cấp sẵn thì tránh được nhiều lần sao chép. Danh sách liên kết đối lập: thêm và xoá ở giữa rẻ về mặt thao tác con trỏ, nhưng mỗi nút nằm rải rác nên duyệt tốn nhiều lần nhảy bộ nhớ và chậm hơn mảng nhiều lần trong thực tế. Đây là ví dụ rõ nhất cho bài học ở lesson 33: bậc độ phức tạp giống nhau mà tốc độ thật khác nhau nhiều lần.

**Outcome.** Đo được chênh lệch tốc độ duyệt giữa mảng và danh sách liên kết, và giải thích bằng cách xếp trong bộ nhớ.

**Đánh giá.** Tầng *áp dụng*. Objective là một phép đo có giải thích cơ chế. Kiểm bằng bảng số đo; đạt khi chênh lệch đo được đúng chiều và giải thích đúng bằng tính cục bộ chứ bằng bậc độ phức tạp.

**Lab.** Cài mảng động của riêng mình có chiến lược nhân đôi, đo chi phí khấu hao cho mỗi lần thêm qua một triệu lần. So thời gian duyệt giữa mảng và danh sách liên kết cùng số phần tử. Thử cấp sẵn kích thước và đo phần tiết kiệm.

**Pitfalls.** Giải thích chênh lệch bằng bậc độ phức tạp · dùng danh sách liên kết vì thấy thêm xoá rẻ · tăng kích thước theo hằng số thay vì nhân đôi · không cấp sẵn khi đã biết kích thước.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng số đo cho thấy mảng duyệt nhanh hơn nhiều lần, và giải thích đúng bằng tính cục bộ bộ nhớ.

### Lesson 35 · Hash tables - collisions, load factor and resize `TH`
**Prerequisites.** Lesson 34

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bảng băm là cấu trúc được dùng nhiều nhất trong hệ dữ liệu và cũng là cấu trúc bị coi là hộp đen nhiều nhất. Cơ chế: hàm băm ánh xạ khoá sang vị trí, nhiều khoá có thể rơi cùng vị trí, nên phải có cách xử lý va chạm. Hai cách và đánh đổi: móc xích giữ danh sách tại mỗi vị trí, đơn giản và chịu được hệ số tải cao; địa chỉ mở tìm vị trí kế tiếp, tính cục bộ tốt hơn nhưng xuống cấp nhanh khi gần đầy và cần bia mộ khi xoá. Hệ số tải quyết định tốc độ: vượt ngưỡng thì phải cấp lại và băm lại toàn bộ, một thao tác đắt xảy ra thỉnh thoảng. Chất lượng hàm băm quyết định tất cả: hàm băm kém cho phân bố lệch và bảng băm suy biến về danh sách, và **kẻ tấn công cố tình tạo va chạm là một dạng tấn công có thật**. Nối tới hệ thống: phép kết băm ở M9 và M18, và phân vùng theo băm ở M16.

**Outcome.** Đo được quan hệ giữa hệ số tải và tốc độ tra cứu, và chứng minh bằng thực nghiệm tác động của hàm băm kém.

**Đánh giá.** Tầng *phân tích*. Objective đòi nối tham số cấu hình với hành vi quan sát được. Kiểm bằng bảng đo nhiều hệ số tải cộng thí nghiệm va chạm; đạt khi đường cong đúng dạng và thí nghiệm va chạm cho thấy suy biến.

**Lab.** Cài cả hai cách xử lý va chạm. Đo thời gian tra cứu ở năm mức hệ số tải. Đo chi phí của một lần cấp lại. Thay hàm băm tốt bằng một hàm băm kém có chủ ý và đo lại. Tạo một tập khoá cố tình va chạm và đo mức suy biến.

**Pitfalls.** Coi bảng băm là hộp đen · để hệ số tải rất cao · dùng địa chỉ mở mà không xử lý bia mộ khi xoá · giả định hàm băm mặc định luôn an toàn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng đo năm mức hệ số tải cho đường cong đúng dạng, và tập khoá va chạm làm tra cứu suy biến có số chứng minh.

### Lesson 36 · Trees - BST, balancing and the B-tree idea `LT`
**Prerequisites.** Lesson 35

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bảng băm cho tra cứu theo khoá chính xác rất nhanh nhưng không giữ thứ tự, nên không trả lời được truy vấn theo khoảng, và đó là lý do cây tồn tại. Cây tìm kiếm nhị phân giữ thứ tự nên tra theo khoảng được, nhưng suy biến thành danh sách nếu chèn dữ liệu đã sắp xếp; cây tự cân bằng giải vấn đề đó bằng cách xoay để giữ chiều cao. Cây B là biến thể cho lưu trữ ngoài và là cấu trúc của gần như mọi chỉ mục cơ sở dữ liệu: mỗi nút chứa nhiều khoá và có nhiều con, nên cây rất thấp và số lần đọc đĩa để tìm một khoá rất nhỏ. **Lý do thiết kế đó nằm ở chỗ đọc đĩa theo khối**: đọc một khối 8 KB tốn gần bằng đọc 100 byte, nên nhồi nhiều khoá vào một nút là tối ưu đúng. Đây là bài đặt nền trực tiếp cho chỉ mục ở M10 và cho việc đọc kế hoạch thực thi ở M9.

**Outcome.** Giải thích vì sao chỉ mục cơ sở dữ liệu dùng cây B thay vì cây nhị phân hay bảng băm, dẫn bằng chi phí đọc khối.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết chuẩn bị cho M9 và M10; chưa đòi cài đặt cây B. Kiểm bằng bài giải thích cộng tính toán; đạt khi tính đúng chiều cao cây ở hai cấu hình và nêu đúng lý do liên quan tới đọc khối.

**Lab.** Cài cây tìm kiếm nhị phân, chèn dữ liệu đã sắp xếp và đo chiều cao để thấy suy biến. Tính chiều cao cây B cho một triệu khoá ở hai kích thước nút khác nhau. Viết ba câu giải thích vì sao cấu trúc này phù hợp với lưu trữ ngoài, và một câu nêu khi nào bảng băm vẫn tốt hơn.

**Pitfalls.** Nghĩ cây B là cây nhị phân cân bằng · bỏ qua lý do đọc khối · dùng cây cho tra cứu chỉ theo khoá chính xác · chèn dữ liệu đã sắp xếp vào cây không cân bằng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chiều cao cây B tính đúng ở cả hai cấu hình, và giải thích nêu đúng vai trò của chi phí đọc khối.

### Lesson 37 · Heaps, priority queues and top-k `TH`
**Prerequisites.** Lesson 36

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Đống là cấu trúc trả lời một câu hỏi rất hẹp nhưng rất hay gặp: phần tử nhỏ nhất hoặc lớn nhất hiện tại là gì. Cơ chế cây gần đầy đủ lưu trong mảng, nên không cần con trỏ và tính cục bộ tốt. Ba ứng dụng trong hệ dữ liệu: lấy N phần tử đầu mà không phải sắp xếp toàn bộ, trộn nhiều dòng đã sắp xếp trong sắp xếp ngoài ở lesson 39, và lập lịch theo độ ưu tiên. Lấy N đầu bằng đống giữ kích thước N: duyệt một lần, bộ nhớ chỉ N, so với sắp xếp toàn bộ tốn bộ nhớ theo toàn bộ dữ liệu; đây là ví dụ rõ về chọn cấu trúc theo câu hỏi thay vì theo thói quen. Dựng đống một lần rẻ hơn chèn lần lượt, và đo được chênh lệch đó. Nối tới hệ thống: bài toán lấy N đầu mỗi nhóm sẽ gặp lại ở M9 dưới dạng hàm cửa sổ.

**Outcome.** Giải bài toán lấy N phần tử đầu trên dữ liệu vượt bộ nhớ bằng đống giữ kích thước N, và so bộ nhớ với cách sắp xếp toàn bộ.

**Đánh giá.** Tầng *áp dụng*. Objective là chọn cấu trúc theo ràng buộc bộ nhớ và chứng minh bằng số đo. Kiểm bằng cặp số đo bộ nhớ; đạt khi bản dùng đống giữ bộ nhớ theo N chứ theo kích thước dữ liệu.

**Lab.** Trên tệp 5 GB, lấy 100 bản ghi lớn nhất bằng hai cách: sắp xếp toàn bộ rồi cắt, và đống giữ kích thước 100. Đo thời gian và bộ nhớ đỉnh của cả hai. So dựng đống một lần với chèn lần lượt trên một triệu phần tử.

**Pitfalls.** Sắp xếp toàn bộ để lấy vài phần tử · dùng đống khi cần thứ tự đầy đủ · chèn lần lượt thay vì dựng một lần · bỏ qua bộ nhớ khi so.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bản dùng đống giữ bộ nhớ đỉnh theo N và cho cùng kết quả, kèm số đo so với cách sắp xếp toàn bộ.

### Lesson 38 · Graphs, topological order and dependency scheduling `TH`
**Prerequisites.** Lesson 37

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Đồ thị là mô hình của mọi thứ có quan hệ phụ thuộc, và trong chương trình này nó xuất hiện ba lần: đồ thị phụ thuộc của bộ điều phối ở M14, đồ thị lineage ở M14D, và đồ thị thực thi của engine phân tán ở M18. Hai cách biểu diễn và khi nào dùng cái nào: danh sách kề tiết kiệm cho đồ thị thưa, ma trận kề nhanh cho kiểm tra cạnh trên đồ thị dày. Duyệt theo chiều rộng và theo chiều sâu, cùng bài toán tương ứng. Sắp thứ tự tô pô cho đồ thị có hướng không chu trình là thuật toán trung tâm: nó trả lời câu hỏi chạy các bước theo thứ tự nào, và **thuật toán tự phát hiện chu trình** vì đồ thị có chu trình thì không sắp được. Từ đó suy ra cách bộ điều phối báo lỗi phụ thuộc vòng. Chạy song song có giới hạn trên đồ thị: các nút không phụ thuộc nhau chạy đồng thời được, và đó là cách một đồ thị phụ thuộc được thực thi nhanh.

**Outcome.** Cài bộ thực thi đồ thị phụ thuộc có phát hiện chu trình và chạy song song có giới hạn, và chứng minh thứ tự chạy đúng.

**Đánh giá.** Tầng *sáng tạo*. Objective đòi ghép sắp thứ tự tô pô với giới hạn đồng thời ở lesson 29 thành một bộ thực thi. Kiểm bằng ba đồ thị thử trong đó một có chu trình; đạt khi thứ tự chạy hợp lệ, chu trình bị phát hiện, và giới hạn đồng thời được tôn trọng.

**Lab.** Cài bộ thực thi nhận một đồ thị nhiệm vụ. Chạy trên ba đồ thị: một chuỗi thẳng, một đồ thị có nhánh song song, và một đồ thị có chu trình. Chứng minh thứ tự chạy hợp lệ bằng nhật ký, chu trình bị báo lỗi rõ ràng, và số nhiệm vụ chạy đồng thời không vượt giới hạn. Thêm trạng thái thử lại cho nhiệm vụ hỏng.

**Pitfalls.** Không phát hiện chu trình nên chạy vô hạn · chạy song song không giới hạn · bắt đầu một nhiệm vụ khi phụ thuộc chưa xong · không giữ trạng thái nên chạy lại từ đầu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Thứ tự chạy hợp lệ trên cả ba đồ thị, chu trình bị báo lỗi rõ, và số nhiệm vụ đồng thời không vượt giới hạn.

### Lesson 39 · External merge sort and IO amplification `TH`
**Prerequisites.** Lesson 38

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài toán nền của mọi xử lý dữ liệu vượt bộ nhớ, và cũng là thứ engine phân tán ở M18 làm bên trong khi sắp xếp và khi xáo trộn. Cơ chế hai pha: pha một chia dữ liệu thành các đoạn vừa bộ nhớ, sắp xếp từng đoạn và ghi ra đĩa; pha hai trộn các đoạn đã sắp xếp bằng một đống theo lesson 37. Số đoạn trộn cùng lúc bị giới hạn bởi bộ nhớ, nên dữ liệu rất lớn cần nhiều vòng trộn, và **số vòng trộn nhân lên lượng đọc ghi đĩa**; đại lượng này gọi là hệ số khuếch đại vào ra và là thứ quyết định thời gian chạy thật. Đánh đổi bộ nhớ và số vòng: cho nhiều bộ nhớ hơn thì ít vòng hơn và ít đọc ghi hơn. Đây là lý do một công việc sắp xếp được cấp thêm bộ nhớ có thể nhanh lên nhiều lần chứ tuyến tính, và là bài học sẽ dùng lại khi chỉnh bộ nhớ ở M18.

**Outcome.** Cài sắp xếp ngoài với ngân sách bộ nhớ nhỏ hơn dữ liệu, và đo được quan hệ giữa bộ nhớ cấp và hệ số khuếch đại vào ra.

**Đánh giá.** Tầng *áp dụng*. Objective là một cài đặt có số đo giải thích được bằng cơ chế hai pha. Kiểm bằng bảng ba mức bộ nhớ; đạt khi sắp xếp đúng ở mọi mức và hệ số khuếch đại đo được giảm khi tăng bộ nhớ.

**Lab.** Cài sắp xếp ngoài cho tệp 2 GB với ngân sách bộ nhớ 100 MB. Kiểm kết quả đã sắp xếp đúng. Chạy lại ở ba mức bộ nhớ và đo tổng byte đọc cùng ghi. Tính hệ số khuếch đại vào ra cho từng mức và vẽ quan hệ.

**Pitfalls.** Đọc cả tệp vào bộ nhớ · dùng số đoạn trộn quá lớn so với bộ nhớ · chỉ đo thời gian mà không đo byte đọc ghi · không kiểm kết quả đã sắp xếp đúng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Kết quả sắp xếp đúng ở cả ba mức bộ nhớ, và hệ số khuếch đại vào ra giảm khi tăng bộ nhớ có số chứng minh.

### Lesson 40 · Hash join against sort-merge join `TH`
**Prerequisites.** Lesson 39

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hai cách ghép hai tập dữ liệu theo khoá, và đây là bài nối trực tiếp tới M9 và M18 vì mọi engine đều chọn giữa hai cách này. Phép kết băm dựng bảng băm từ bên nhỏ rồi quét bên lớn để dò; nhanh khi bên nhỏ vừa bộ nhớ, và suy giảm khi không vừa vì phải chia thành phân vùng rồi làm từng phần. Phép kết sắp xếp trộn sắp cả hai bên theo khoá rồi trộn; tốn hơn khi dữ liệu chưa sắp xếp, nhưng **miễn phí nếu dữ liệu đã sắp xếp sẵn**, và đây là lý do bố trí dữ liệu ở M13 ảnh hưởng tới tốc độ kết. Điểm giao phụ thuộc ba yếu tố: kích thước hai bên, bộ nhớ có sẵn, và dữ liệu đã sắp xếp chưa. Khoá lệch làm phép kết băm suy giảm vì một phân vùng quá lớn, đúng hiện tượng sẽ gặp lại ở M18. Cách đo để tìm điểm giao trên dữ liệu của chính mình thay vì tin quy tắc chung.

**Outcome.** Cài cả hai phép kết và tìm được điểm giao theo kích thước dữ liệu, bộ nhớ và độ lệch khoá.

**Đánh giá.** Tầng *đánh giá*. Objective đòi xác định điều kiện áp dụng của hai thuật toán bằng thực nghiệm, chuẩn bị trực tiếp cho M9. Kiểm bằng bảng ba yếu tố; đạt khi tìm ra điểm giao theo ít nhất hai yếu tố và giải thích đúng cơ chế suy giảm.

**Lab.** Cài phép kết băm và phép kết sắp xếp trộn. Đo thời gian trên lưới gồm ba kích thước dữ liệu nhân hai mức bộ nhớ. Thêm một khoá chiếm 60% dữ liệu và đo lại cả hai. Chạy lại phép kết sắp xếp trộn trên dữ liệu đã sắp xếp sẵn và ghi phần chênh.

**Pitfalls.** Kết luận một cách luôn nhanh hơn · bỏ qua bộ nhớ khi so · không thử dữ liệu lệch khoá · quên rằng dữ liệu đã sắp xếp đổi hẳn kết luận.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tìm được điểm giao theo ≥ 2 yếu tố kèm số đo, và giải thích đúng vì sao phép kết băm suy giảm khi khoá lệch.

### Lesson 41 · Bloom filters and probabilistic membership `TH`
**Prerequisites.** Lesson 40

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Cấu trúc trả lời câu hỏi khoá này có thể có trong tập không, với một đánh đổi rất cụ thể: nó có thể trả lời nhầm là có, nhưng **không bao giờ trả lời nhầm là không**. Tính chất một chiều đó là thứ làm nó hữu dụng: dùng làm bộ lọc trước để tránh một phép tìm đắt, và trả lời nhầm là có chỉ tốn thêm một lần tìm chứ cho kết quả sai. Cơ chế: một dãy bit và k hàm băm; thêm phần tử thì bật k bit, hỏi thì kiểm k bit. Tỉ lệ trả lời nhầm phụ thuộc số bit trên mỗi phần tử và số hàm băm, và có công thức để chọn hai tham số theo tỉ lệ mong muốn. Không xoá được phần tử, và đó là giới hạn phải biết trước khi dùng. Nối tới hệ thống: cấu trúc gộp theo nhật ký ở M10 dùng nó để tránh đọc các tệp không chứa khoá, và engine truy vấn dùng nó để bỏ qua tệp ở M13.

**Outcome.** Chọn số bit trên mỗi phần tử và số hàm băm cho một tỉ lệ nhầm mục tiêu, và kiểm chứng tỉ lệ thật bằng thực nghiệm.

**Đánh giá.** Tầng *áp dụng*. Objective là chọn tham số có công thức rồi xác nhận bằng đo. Kiểm bằng bảng quét tham số; đạt khi tỉ lệ nhầm đo được bám sát lý thuyết và không có lần nào trả lời nhầm là không.

**Lab.** Cài bộ lọc Bloom. Quét số bit trên mỗi phần tử từ 4 tới 16 và số hàm băm từ 1 tới 8. Với mỗi tổ hợp, đo tỉ lệ trả lời nhầm thật trên một triệu phép hỏi và so với giá trị lý thuyết. Chứng minh bằng thực nghiệm không có trường hợp nào trả lời nhầm là không. Đo phần tiết kiệm khi dùng nó làm bộ lọc trước một phép tìm trên đĩa.

**Pitfalls.** Dùng bộ lọc Bloom khi cần câu trả lời chắc chắn · chọn tham số theo cảm tính · quên rằng không xoá được · bỏ qua chi phí tính k hàm băm.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tỉ lệ nhầm đo được bám sát lý thuyết trên lưới tham số, không có lần nào trả lời nhầm là không, và có số đo phần tiết kiệm.

### Lesson 42 · Choosing a structure from the access pattern `LT`
**Prerequisites.** Lesson 41

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài chốt phần cấu trúc, biến bảy bài trước thành một quy tắc quyết định. Bốn câu hỏi theo thứ tự: truy cập theo khoá chính xác hay theo khoảng, tỉ lệ đọc so với ghi ra sao, dữ liệu có vừa bộ nhớ không, và có cần giữ thứ tự không. Bảng quyết định nối bốn câu đó với các cấu trúc đã học. Ba cặp đối lập cần thuộc: bảng băm cho tra chính xác còn cây cho tra khoảng; mảng cho duyệt tuần tự còn danh sách liên kết gần như không bao giờ đúng trong mã dữ liệu; đống cho câu hỏi cực trị còn sắp xếp cho thứ tự đầy đủ. Nguyên tắc cuối và quan trọng nhất: **ở quy mô thật, đo quyết định chứ bậc độ phức tạp quyết định**, và mọi lựa chọn trong bài này phải dẫn về một số đo đã tự đo ở lesson 33 tới 41. Ba tình huống mà cấu trúc đơn giản nhất là lựa chọn đúng dù có cấu trúc tốt hơn về lý thuyết.

**Outcome.** Chọn cấu trúc cho năm mẫu truy cập cho trước, mỗi lần dẫn về một số đo đã tự đo.

**Đánh giá.** Tầng *đánh giá*. Objective đòi áp một quy tắc quyết định có bằng chứng. Kiểm bằng năm mẫu truy cập trong đó ít nhất một nên dùng cấu trúc đơn giản nhất; đạt khi chọn đúng ít nhất bốn và nhận ra trường hợp đó.

**Lab.** Cho năm mẫu truy cập mô tả bằng ngôn ngữ nghiệp vụ. Với mỗi mẫu, trả lời bốn câu hỏi, chọn cấu trúc, và dẫn một số đo từ các bài trước. Với mẫu mà cấu trúc đơn giản là đúng, ước lượng phần phức tạp thêm nếu chọn cấu trúc tinh vi hơn.

**Pitfalls.** Chọn cấu trúc tinh vi vì nghe hay hơn · bỏ qua tỉ lệ đọc ghi · quên hỏi dữ liệu có vừa bộ nhớ không · dẫn lý thuyết thay vì dẫn số đo.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chọn đúng ≥ 4/5 mẫu truy cập với số đo dẫn chứng, và nhận ra đúng trường hợp nên dùng cấu trúc đơn giản nhất.

### Lesson 43 · Failure drills - adversarial input and measurement traps `TH`
**Prerequisites.** Lesson 42

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài diễn tập hỏng, và nó kiểm tra xem người học có thật sự hiểu cơ chế hay chỉ chạy được lab. Năm tình huống hỏng, mỗi tình huống nhắm vào một hiểu lầm cụ thể. Một là tập khoá cố tình va chạm làm bảng băm suy biến, theo lesson 35. Hai là đồ thị có chu trình làm bộ thực thi chạy vô hạn, theo lesson 38. Ba là đệ quy quá sâu làm tràn ngăn xếp, và cách chuyển sang vòng lặp có ngăn xếp tường minh. Bốn là tràn số khi cộng dồn kích thước, một lỗi ít gặp trong Python nhưng phải hiểu vì sẽ gặp ở M4. Năm là phép so sánh cho kết quả ngược vì đầu vào quá nhỏ hoặc bộ nhớ đệm đã ấm, theo lesson 33. Với mỗi tình huống, yêu cầu không phải chỉ sửa mà là **dựng một phép kiểm hồi quy bắt được nó lần sau**, đúng kỷ luật đã đặt ở lesson 9.

**Outcome.** Chẩn đoán năm tình huống hỏng về đúng cơ chế và viết phép kiểm hồi quy bắt được từng cái.

**Đánh giá.** Tầng *phân tích*. Objective đòi truy từ triệu chứng về cơ chế đã học và biến nó thành một phép kiểm lâu dài. Kiểm bằng năm tình huống tính giờ; đạt khi chẩn đoán đúng ít nhất bốn và mỗi cái có phép kiểm hồi quy chạy được.

**Lab.** Giảng viên đưa năm chương trình hỏng theo năm cách trên, mỗi cái 10 phút. Với mỗi cái, chẩn đoán cơ chế, sửa, và viết một phép kiểm hồi quy. Chạy toàn bộ phép kiểm trên bản chưa sửa để chứng minh chúng thật sự bắt được lỗi.

**Pitfalls.** Sửa mà không viết phép kiểm hồi quy · tăng giới hạn đệ quy thay vì đổi cách · kết luận từ một lần đo · viết phép kiểm không chạy trên bản chưa sửa.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chẩn đoán đúng ≥ 4/5 tình huống, và mọi phép kiểm hồi quy đều báo đỏ trên bản chưa sửa và xanh trên bản đã sửa.

### Lesson 44 · Gate 1 - explain a structure choice and prove it by measurement `KT`
**Prerequisites.** Lesson 43

**In-class (145 phút).** 100 phút làm bài độc lập · 45 phút chữa bài và phân tích lỗi theo nhóm

**Learn.** Cổng của Phase 1. Bài kiểm ba năng lực nền của cả chương trình: kỷ luật kỹ thuật ở M1, Python có chất lượng sản phẩm ở M2, và chọn cấu trúc có bằng chứng ở M3. Không có nội dung mới.

**Outcome.** Nộp lời giải cho một bài toán dữ liệu cho trước, bảo vệ lựa chọn cấu trúc bằng số đo của chính mình, và chẩn đoán được một lỗi tiêm sẵn.

**Đánh giá.** Tầng *đánh giá*. Cổng đo năng lực tổng hợp dưới chất vấn, nên hình thức là bài làm cộng bảo vệ chứ trắc nghiệm.

**Lab.** Buổi 145 phút: 100 phút làm bài độc lập, 45 phút chữa bài. Nhận một bài toán xử lý tệp 3 GB với ngân sách bộ nhớ 200 MB. Bài chấm sáu phần: A (15đ) phát biểu bài toán sáu phần và phép kiểm chấp nhận · B (20đ) chương trình chạy đúng trong ngân sách bộ nhớ · C (20đ) lựa chọn cấu trúc dẫn bằng số đo của chính mình, không dẫn lý thuyết suông · D (15đ) bộ kiểm đủ bốn loại và quy trình tích hợp xanh · E (20đ) chẩn đoán một lỗi tiêm sẵn bằng bảng giả thuyết có ít nhất ba dòng bị bác bỏ · F (10đ) nhật ký có cấu trúc đủ để người khác chẩn đoán lại.

**Pitfalls.** Nạp cả tệp vào bộ nhớ · chọn cấu trúc rồi mới tìm lý do · bỏ phần chẩn đoán vì hết giờ · dẫn bậc độ phức tạp thay vì số đo.

**Self-study (2,4 giờ).** Không có bài tự học. Nếu không đạt, theo phụ lục khắc phục khi không đạt cổng

**Done when.** Đạt ≥ 70/100, phần B và C đều ≥ 60%. Lựa chọn cấu trúc không dẫn được về số đo của chính mình thì phần C bằng không.

# MODULE M4 · COMPUTER ARCHITECTURE AND THE PERFORMANCE MODEL

**Phase 2 · Lessons 45–60 · 32 giờ**

| | |
|---|---|
| **Objective cấp module** | Dự đoán rồi đo được chi phí từ tầng lệnh, bộ nhớ đệm, RAM và thiết bị lưu trữ, và dùng mô hình đó giải thích hành vi của cơ sở dữ liệu, engine phân tán và dịch vụ |
| **Tiền đề** | M3 |
| **Exit criterion** | Vẽ được đường đi của một phép đọc và một phép ghi từ ứng dụng tới CPU, bộ nhớ đệm, RAM, bộ đệm trang và thiết bị; phân loại đúng SISD, SIMD và MIMD và giải thích SPMD chạy trên nền MIMD; dùng số đo tìm trần tính toán, bộ nhớ đệm, băng thông, đồng bộ hay mạng trước khi thêm làn, lõi hoặc nút |
| **Kỹ năng SFIA** | `HPCC` mức 3 · `SYSP` mức 3 |
| **Chế độ hỏng** | Học thông số phần cứng như kiến thức rời, rồi không nối được với việc vì sao một truy vấn chậm hay vì sao thêm luồng không tăng thông lượng |

Module này là nền của mọi lập luận hiệu năng trong chương trình. Bốn kết luận ở đây được dùng lại liên tục: tuần tự rẻ hơn ngẫu nhiên nhiều bậc, bố trí theo cột thắng vì tính cục bộ, bền vững tốn tiền vì `fsync`, và thêm luồng chỉ giúp khi nút thắt là chờ chứ tính.

Mọi khẳng định trong module phải kèm số đo của chính người học, theo đúng kỷ luật đã đặt ở lesson 21 và 33.

### Lesson 45 · The memory hierarchy and the cost model `LT`
**Prerequisites.** Module 4: M3

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Một phép truy cập dữ liệu có thể tốn một nhịp đồng hồ hoặc tốn rất nhiều nhịp, tuỳ dữ liệu đang nằm ở đâu; khoảng cách giữa các bậc là nhiều bậc độ lớn chứ vài phần trăm, và con số của từng bậc do phần cứng quyết định nên bài này đo chứ tra bảng, và khoảng cách đó là thứ giải thích gần như mọi hiện tượng hiệu năng. Thứ bậc từ nhanh tới chậm: thanh ghi, ba mức bộ nhớ đệm, RAM, đĩa thể rắn, đĩa quay, mạng. Mỗi bậc chậm hơn bậc trên khoảng một tới ba bậc độ lớn, và dung lượng thì ngược lại. Bộ số mốc cần thuộc để ước lượng mà không tra: truy cập bộ nhớ đệm mức một, truy cập RAM, đọc ngẫu nhiên trên đĩa thể rắn, đọc tuần tự một megabyte, và một vòng mạng trong trung tâm dữ liệu. Ba loại nút thắt và cách phân biệt bằng số đo chứ bằng cảm nhận: nghẽn CPU, nghẽn băng thông bộ nhớ, và nghẽn vào ra. **Xác định sai loại nút thắt thì mọi tối ưu sau đó đều đi sai hướng**, và đây là lỗi tốn kém nhất trong cả chương trình.

**Outcome.** Phân loại nút thắt của một chương trình cho trước vào đúng một trong ba loại, dẫn bằng số đo chứ bằng phỏng đoán.

**Đánh giá.** Tầng *phân tích*. Bài mở module, người học đã biết đo từ lesson 21 nên đủ nền để phân loại. Kiểm bằng ba chương trình có ba loại nút thắt khác nhau; đạt khi phân loại đúng cả ba và mỗi lần dẫn được một số đo cụ thể.

**Lab.** Cho ba chương trình, mỗi cái nghẽn ở một tầng khác nhau. Với mỗi cái, đo mức dùng CPU, băng thông bộ nhớ và thời gian chờ vào ra, rồi phân loại nút thắt. Viết bộ số mốc từ chính máy của mình bằng cách đo, không chép từ tài liệu.

**Pitfalls.** Kết luận nghẽn CPU vì thấy CPU cao trong khi thực ra là chờ bộ nhớ · tối ưu thuật toán khi nút thắt là đĩa · dùng số mốc của máy khác.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân loại đúng cả ba nút thắt kèm số đo, và có bộ số mốc đo trên chính máy mình.

### Lesson 46 · Cache lines, locality and the cache cliff `TH`
**Prerequisites.** Lesson 45

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bộ nhớ đệm không nạp từng byte mà nạp cả một dòng, thường 64 byte, nên đọc một byte thì 63 byte lân cận được nạp theo miễn phí. Từ một sự thật đó suy ra toàn bộ khái niệm tính cục bộ: cục bộ theo không gian là dùng dữ liệu nằm gần nhau, cục bộ theo thời gian là dùng lại dữ liệu vừa dùng. Hệ quả đo được và gây bất ngờ: duyệt một mảng theo thứ tự nhanh hơn duyệt ngẫu nhiên nhiều lần dù cùng số phép đọc. **Con số cụ thể phụ thuộc phần cứng nên nó là giả thuyết phải tự đo ở lab bài này, không phải một hằng số nhớ được**; phần phải giải thích là vì sao có chênh lệch, không phải chênh lệch bằng mấy. Vách bộ nhớ đệm là hiện tượng tốc độ tụt đột ngột khi dữ liệu vượt dung lượng một mức đệm, và đo được thành một đồ thị có bậc rõ ràng. Chia sẻ giả: hai luồng ghi hai biến khác nhau nhưng nằm cùng một dòng đệm thì chúng tranh nhau và chậm hơn chạy tuần tự; đây là lỗi hiệu năng khó đoán nhất trong lập trình đa luồng. Nối tới M12: engine cột nhanh vì khai thác đúng tính cục bộ này.

**Outcome.** Đo được vách bộ nhớ đệm trên máy của mình và suy ra dung lượng các mức đệm từ đồ thị.

**Đánh giá.** Tầng *phân tích*. Objective đòi suy đặc tính phần cứng từ dữ liệu đo, chứ đọc thông số. Kiểm bằng đồ thị quét kích thước; đạt khi đồ thị có bậc rõ và dung lượng suy ra gần đúng với thông số thật.

**Lab.** Viết phép đo duyệt mảng với bước nhảy thay đổi, quét kích thước dữ liệu từ 4 KB tới 256 MB. Vẽ đồ thị thời gian trên mỗi phần tử và chỉ ra các bậc. So thông số suy ra với thông số thật của máy. Tái hiện chia sẻ giả với hai luồng và đo mức chậm đi, rồi sửa bằng cách chèn đệm.

**Pitfalls.** Đo với dữ liệu nhỏ hơn bộ nhớ đệm nên không thấy bậc nào · quên hâm nóng trước khi đo · kết luận chia sẻ giả mà không đo bản đã chèn đệm.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đồ thị có bậc rõ ràng, dung lượng suy ra cùng bậc với thông số thật, và bản sửa chia sẻ giả nhanh hơn có số chứng minh.

### Lesson 47 · Row-major against column-major layout `TH`
**Prerequisites.** Lesson 46

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Cùng một bảng dữ liệu, hai cách xếp trong bộ nhớ, và chênh lệch tốc độ cho phép gộp thường lớn tới mức đổi cả quyết định thiết kế. Mức chênh cụ thể phụ thuộc số cột, kiểu dữ liệu và kích thước bộ nhớ đệm, nên nó được đo ở lab chứ nêu sẵn. Xếp theo dòng gom mọi trường của một bản ghi cạnh nhau; xếp theo cột gom mọi giá trị của một trường cạnh nhau. Khi tính tổng một cột trên bảng 40 cột: bố trí theo dòng phải nạp cả 40 cột vào đệm dù chỉ dùng một, nên 39 phần bốn mươi băng thông bị lãng phí; bố trí theo cột chỉ nạp phần cần. **Đây là lý do vật lý của mọi engine phân tích cột** và là bài học sẽ dùng lại nguyên vẹn ở M12 và M13. Chiều ngược lại cũng đúng và phải nói rõ: đọc nguyên một bản ghi thì bố trí theo dòng thắng, nên hệ giao dịch dùng dòng. Thực thi theo lô và theo véc tơ: xử lý một khối giá trị cùng kiểu một lần cho phép dùng lệnh song song của CPU, và đó là tầng tăng tốc thứ hai sau tính cục bộ.

**Outcome.** Đo chênh lệch giữa hai bố trí trên cùng phép gộp và giải thích bằng tỉ lệ băng thông bị lãng phí.

**Đánh giá.** Tầng *phân tích*. Objective đòi quy chênh lệch đo được về cơ chế nạp dòng đệm. Kiểm bằng bảng đo hai bố trí nhân hai loại truy vấn; đạt khi cả bốn ô có số và giải thích đúng chiều đảo ngược ở truy vấn đọc cả bản ghi.

**Lab.** Dựng cùng dữ liệu 40 cột ở hai bố trí. Chạy hai truy vấn: tính tổng một cột, và đọc nguyên 100 bản ghi. Đo cả bốn ô. Tính tỉ lệ băng thông lãng phí của bố trí theo dòng ở truy vấn thứ nhất và so với chênh lệch thời gian đo được.

**Pitfalls.** Kết luận bố trí cột luôn nhanh hơn · so hai bố trí ở hai kích thước dữ liệu khác nhau · bỏ qua truy vấn đọc cả bản ghi nên không thấy chiều ngược.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng bốn ô đủ số đo, tỉ lệ băng thông lãng phí giải thích được chênh lệch, và chiều đảo ngược ở truy vấn thứ hai được chỉ ra.

### Lesson 48 · Flynn taxonomy - SISD, SIMD, MIMD and where SPMD fits `LT`
**Prerequisites.** Lesson 47

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài đặt từ vựng chính xác cho toàn bộ phần song song, vì bốn từ dưới đây bị dùng lẫn thường xuyên và dùng lẫn thì không bàn được thiết kế. Phân loại theo hai trục là số dòng lệnh và số dòng dữ liệu: một lệnh một dữ liệu là mô hình tuần tự cổ điển; một lệnh nhiều dữ liệu áp cùng phép toán lên nhiều phần tử trong một dòng lệnh; nhiều lệnh nhiều dữ liệu cho mỗi lõi hoặc mỗi nút một bộ đếm chương trình riêng nên chúng chạy mã khác nhau được; nhiều lệnh một dữ liệu chỉ cần biết là có. Bốn khái niệm phải tách và đây là điểm ra của bài: **một lệnh nhiều dữ liệu, nhiều lệnh nhiều dữ liệu, đồng thời, và song song không phải bốn tên của một thứ**; đồng thời là nhiều việc chồng lấn theo thời gian, song song là nhiều việc chạy thật sự cùng lúc. Một chương trình nhiều dữ liệu là khuôn mẫu lập trình: cùng một chương trình chạy trên nhiều tiến trình với phân vùng dữ liệu khác nhau, và nó thường được triển khai trên nền nhiều lệnh nhiều dữ liệu.

**Outcome.** Phân loại đúng bốn khái niệm cho một tập hệ thống thật và giải thích quan hệ giữa một chương trình nhiều dữ liệu với nền nhiều lệnh nhiều dữ liệu.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết đặt từ vựng cho năm bài sau; chưa đo gì. Kiểm bằng bài phân loại tám hệ thống; đạt khi phân đúng ít nhất sáu và giải thích được hai ca nằm ở nhiều tầng cùng lúc.

**Lab.** Cho tám hệ thống hoặc đoạn mã thật, gồm một vòng lặp véctơ hoá, một bể luồng, một cụm xử lý phân tán, và một engine phân tích. Phân loại từng cái theo bốn khái niệm. Với hai ca có nhiều tầng song song lồng nhau, mô tả từng tầng. Viết một đoạn phân biệt đồng thời với song song bằng một ví dụ của chính mình.

**Pitfalls.** Gọi mọi thứ chạy nhanh là một lệnh nhiều dữ liệu · dùng đồng thời và song song thay nhau · nghĩ một chương trình nhiều dữ liệu là một kiến trúc phần cứng · bỏ qua việc một hệ có thể thuộc nhiều tầng cùng lúc.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân đúng ≥ 6/8 hệ thống, và hai ca song song lồng nhau được mô tả đủ từng tầng.

### Lesson 49 · SIMD from lane to operator - width, mask, tail and gather `TH`
**Prerequisites.** Lesson 48

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài đi vào cơ chế của một lệnh nhiều dữ liệu ở mức đủ để giải thích hiệu năng, chứ mức viết mã máy. Lệnh vô hướng xử lý một giá trị, lệnh véctơ áp cùng phép toán lên nhiều làn; số làn bằng độ rộng thanh ghi véctơ chia độ rộng phần tử, nên cùng một thanh ghi cho tám làn số thực 32 bit hoặc bốn làn 64 bit. Phần đuôi khi số phần tử không chia hết cho số làn phải xử lý bằng vòng lặp vô hướng hoặc bằng mặt nạ. Dữ liệu liền kề và căn chỉnh làm việc nạp rẻ; **thu thập rải rác và đuổi theo con trỏ thường đắt hơn nhiều và là lý do chính làm tăng tốc thấp hơn kỳ vọng**. Rẽ nhánh trong vòng lặp được chuyển thành mặt nạ hoặc véctơ chọn lọc khi có lợi, nhưng bỏ rẽ nhánh không mặc định nhanh hơn vì nó tính cả hai nhánh. Sáu chế độ hỏng: phụ thuộc vòng lặp, lô quá nhỏ, rẽ nhánh phân kỳ, đường thu thập nhiều giá trị rỗng, bão hoà băng thông bộ nhớ, và cấp phát quá mức.

**Outcome.** Đo phần tăng tốc thật của một vòng lặp véctơ hoá và quy mức tăng tốc thấp về đúng một trong sáu chế độ hỏng.

**Đánh giá.** Tầng *phân tích*. Objective đòi giải thích một con số chứ chỉ tạo ra nó. Kiểm bằng ba vòng lặp có đặc trưng khác nhau; đạt khi mỗi vòng lặp có số đo kèm bộ đếm phần cứng và mức tăng tốc thấp được quy đúng nguyên nhân ở ít nhất hai.

**Lab.** Viết cùng một phép tính ở ba dạng: vô hướng, để trình biên dịch tự véctơ hoá, và dùng thư viện đã véctơ hoá. Đo thời gian cùng bộ đếm gồm số chu kỳ, số lệnh, lỗi bộ nhớ đệm và băng thông; tính số chu kỳ trên mỗi dòng. Chạy lại với ba biến thể dữ liệu: liền kề, rải rác cần thu thập, và nhiều giá trị rỗng. Quy mỗi lần tăng tốc thấp về một trong sáu chế độ hỏng.

**Pitfalls.** Kết luận từ một số đo thời gian duy nhất · dùng lô quá nhỏ rồi kết luận véctơ hoá vô dụng · so hai bản mà không kiểm kết quả giống nhau · viết mã đặc thù tập lệnh trước khi đo.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba dạng đều có số đo kèm bộ đếm phần cứng và số chu kỳ trên mỗi dòng, và ≥ 2 lần tăng tốc thấp được quy đúng chế độ hỏng.

### Lesson 50 · Auto-vectorization - when the compiler gives up `TH`
**Prerequisites.** Lesson 49

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Trình biên dịch véctơ hoá giúp được nhiều, nhưng nó bỏ cuộc trong im lặng, nên biết nó có làm hay không là kỹ năng đo lường. Điều kiện để nó làm được: không có phụ thuộc mang qua vòng lặp, không có khả năng hai con trỏ trỏ chồng nhau, số vòng lặp biết được hoặc xử lý được phần đuôi, và thân vòng lặp không gọi hàm không nội tuyến được. Báo cáo tối ưu hoá của trình biên dịch nói rõ nó véctơ hoá chỗ nào và từ chối chỗ nào kèm lý do; đọc báo cáo rẻ hơn nhiều so với đoán. Đọc mã máy ở mức nhận ra lệnh véctơ là đủ, không cần viết được. **Mã dùng lệnh đặc thù tập lệnh chỉ viết sau khi đã đo và đã thử cách đơn giản**, vì nó kéo theo chi phí về khả năng mang đi, về hạ xung nhịp, và về bảo trì; với phần lớn công việc dữ liệu, dùng thư viện hoặc engine đã véctơ hoá là lựa chọn đúng. Ba cách viết lại vòng lặp để trình biên dịch làm được.

**Outcome.** Làm cho ba vòng lặp bị từ chối véctơ hoá trở nên véctơ hoá được, chứng minh bằng báo cáo và bằng số đo.

**Đánh giá.** Tầng *áp dụng*. Objective có bằng chứng hai lớp là báo cáo trình biên dịch và số đo thời gian. Kiểm bằng ba vòng lặp; đạt khi cả ba chuyển từ bị từ chối sang được véctơ hoá với kết quả tính không đổi.

**Lab.** Viết ba vòng lặp bị từ chối vì ba lý do khác nhau. Bật báo cáo tối ưu hoá và ghi lại lý do từ chối của từng cái. Viết lại từng vòng lặp để gỡ nguyên nhân. Xác nhận trong báo cáo và trong mã máy sinh ra rằng nó đã dùng lệnh véctơ. Đo thời gian trước sau và đối chiếu kết quả tính để chứng minh không đổi.

**Pitfalls.** Đoán trình biên dịch có véctơ hoá hay không · viết lệnh đặc thù tập lệnh trước khi đọc báo cáo · sửa vòng lặp mà không kiểm kết quả giữ nguyên · dùng cờ tối ưu hoá làm đổi ngữ nghĩa số thực mà không nói rõ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba vòng lặp chuyển từ bị từ chối sang được véctơ hoá theo báo cáo, có số đo trước sau, và kết quả tính không đổi.

### Lesson 51 · Virtual memory, page faults and mmap `LT`
**Prerequisites.** Lesson 50

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Chương trình nhìn thấy không gian địa chỉ liên tục của riêng nó, còn bộ nhớ vật lý thì không; ánh xạ giữa hai thứ là bộ nhớ ảo, và nó giải thích nhiều hiện tượng vận hành. Trang là đơn vị ánh xạ, bảng trang giữ ánh xạ, và bộ đệm ánh xạ giữ những mục gần đây để tra nhanh. Lỗi trang nhẹ là trang đã trong RAM nhưng chưa ánh xạ, rẻ; lỗi trang nặng là phải đọc từ đĩa, đắt gấp nhiều bậc, và **tỉ lệ lỗi trang nặng là chỉ số chẩn đoán quan trọng mà nhiều người bỏ qua**. Vùng hoán đổi và vì sao một máy bắt đầu hoán đổi thì mọi thứ chậm thảm hại chứ chậm dần. Sao chép khi ghi làm việc tạo tiến trình con rẻ, và đây là cơ chế đứng sau chi phí khởi động tiến trình đã đo ở lesson 23. Ánh xạ tệp vào bộ nhớ cho phép đọc tệp như đọc mảng, tiện nhưng giấu mất chi phí vào ra nên khó đo.

**Outcome.** Phân biệt lỗi trang nhẹ với lỗi trang nặng bằng số đo, và nhận ra dấu hiệu một tiến trình đang hoán đổi.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết chuẩn bị cho phần chẩn đoán ở M5; chưa đòi xử lý sự cố. Kiểm bằng bài đo cộng nhận dạng; đạt khi phân biệt đúng hai loại lỗi trang và nhận ra đúng trạng thái hoán đổi qua số đo.

**Lab.** Viết chương trình cấp phát dần bộ nhớ vượt RAM khả dụng. Đo số lỗi trang nhẹ và nặng theo thời gian. Ghi lại thời điểm máy bắt đầu hoán đổi và mức chậm đi. Chạy một chương trình tạo tiến trình con và đo chi phí, giải thích bằng sao chép khi ghi.

**Pitfalls.** Nhầm lỗi trang nhẹ với nặng nên hoảng nhầm · tăng bộ nhớ khi nguyên nhân là ánh xạ tệp · bỏ qua tỉ lệ lỗi trang nặng khi chẩn đoán chậm.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân biệt đúng hai loại lỗi trang bằng số đo, và chỉ ra đúng thời điểm bắt đầu hoán đổi kèm mức chậm đi.

### Lesson 52 · Storage - sequential against random, and the device model `TH`
**Prerequisites.** Lesson 51

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Đĩa quay và đĩa thể rắn khác nhau về cơ chế nên khác nhau về hình dạng chi phí, và biết khác biệt đó quyết định nhiều thiết kế. Đĩa quay phải quay và dịch đầu đọc nên đọc ngẫu nhiên đắt hơn tuần tự nhiều bậc độ lớn; tỉ số cụ thể do tốc độ quay và thời gian dịch đầu đọc của từng thiết bị quyết định, và lab bài này đo trên thiết bị đang có. Đĩa thể rắn không có bộ phận cơ nên đọc ngẫu nhiên rẻ hơn nhiều, nhưng vẫn có ba đặc tính phải biết: đơn vị đọc là trang còn đơn vị xoá là khối lớn hơn nhiều, nên ghi đè sinh ra khuếch đại ghi; hiệu năng phụ thuộc độ sâu hàng đợi nên một luồng không khai thác hết; và ghi liên tục lâu dài làm tốc độ tụt khi bộ gom rác bên trong phải chạy. Ba đại lượng đo khác nhau và hay bị gộp: số thao tác mỗi giây, thông lượng byte, và độ trễ; một thiết bị có thể tốt ở đại lượng này và tệ ở đại lượng kia. Nối tới M13: đây là lý do tệp nhỏ đắt và tệp lớn rẻ trên kho đối tượng.

**Outcome.** Đo được ba đại lượng của thiết bị lưu trữ và chỉ ra chênh lệch giữa đọc tuần tự với đọc ngẫu nhiên trên chính máy mình.

**Đánh giá.** Tầng *áp dụng*. Objective là một phép đo theo quy trình cộng đọc kết quả đúng. Kiểm bằng bảng đo bốn cấu hình; đạt khi cả ba đại lượng có số và chênh lệch tuần tự so với ngẫu nhiên đúng chiều.

**Lab.** Đo đọc tuần tự và đọc ngẫu nhiên ở hai độ sâu hàng đợi, ghi cả ba đại lượng cho mỗi cấu hình. Tính tỉ lệ chênh lệch. Chạy ghi liên tục 10 phút và vẽ tốc độ theo thời gian để quan sát mức tụt. So kết quả với thông số nhà sản xuất công bố.

**Pitfalls.** Đo với tệp nhỏ hơn bộ đệm trang nên chỉ đo RAM · đo ở một độ sâu hàng đợi rồi kết luận · gộp ba đại lượng làm một · tin thông số nhà sản xuất mà không đo.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng bốn cấu hình đủ ba đại lượng, chênh lệch tuần tự so với ngẫu nhiên đúng chiều, và đồ thị ghi liên tục cho thấy mức tụt.

### Lesson 53 · Buffering, page cache and fsync `TH`
**Prerequisites.** Lesson 52

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Giữa lệnh ghi của chương trình và byte nằm trên đĩa có ít nhất ba tầng đệm, và không biết tầng nào đã qua thì không biết dữ liệu có sống sót khi mất điện hay không. Đệm của thư viện, bộ đệm trang của nhân, và bộ đệm của chính thiết bị. Lệnh ghi thường chỉ chép vào bộ đệm trang rồi trả về ngay, nên **ghi xong không có nghĩa là dữ liệu đã bền**. `fsync` buộc nhân đẩy xuống thiết bị và chờ xác nhận, và đó là lý do nó chậm hơn ghi thường nhiều bậc. Ba mức cam kết bền vững và giá của từng mức, đo được thành số. Đây chính là cơ chế đứng sau nhật ký ghi trước ở M10 và sau tham số xác nhận của hệ truyền thông điệp: mọi hệ hứa không mất dữ liệu đều phải trả giá `fsync` ở đâu đó. Bộ đệm trang cũng giải thích vì sao lần đo thứ hai luôn nhanh hơn lần đầu, một cái bẫy đã nêu ở lesson 33.

**Outcome.** Đo được cái giá của `fsync` và phát biểu chính xác mức cam kết bền vững của ba cấu hình ghi.

**Đánh giá.** Tầng *phân tích*. Objective đòi nối một tham số cấu hình với một cam kết ngữ nghĩa và một con số. Kiểm bằng bảng ba cấu hình cộng thí nghiệm mất điện mô phỏng; đạt khi ba mức cam kết được phát biểu đúng và số đo đúng chiều.

**Lab.** Ghi 100.000 bản ghi ở ba cấu hình: ghi đệm, ghi đệm rồi đẩy một lần cuối, và gọi `fsync` sau mỗi bản ghi. Đo thông lượng từng cấu hình. Mô phỏng mất điện bằng cách giết tiến trình cứng và đếm số bản ghi còn lại ở mỗi cấu hình. Lập bảng ba cột.

**Pitfalls.** Tin rằng ghi xong là dữ liệu đã bền · gọi `fsync` sau mỗi bản ghi rồi thắc mắc vì sao chậm · đo lần hai mà quên bộ đệm trang đã ấm.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng ba cấu hình có cả thông lượng lẫn số bản ghi sống sót, và ba mức cam kết bền vững được phát biểu đúng.

### Lesson 54 · The kernel boundary - syscalls and context switches `TH`
**Prerequisites.** Lesson 53

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Mỗi lần chương trình cần nhân làm gì đó thì phải vượt ranh giới người dùng và nhân, và mỗi lần vượt tốn chi phí cố định. Hệ quả thực tế lớn hơn người ta tưởng: đọc một tệp bằng một triệu lời gọi mỗi lần một byte chậm hơn nhiều bậc độ lớn so với đọc theo khối lớn, dù cùng tổng số byte. Kích thước khối tốt nhất và mức chênh đều phụ thuộc hệ điều hành cùng thiết bị, nên lab đo bốn kích thước khối rồi tự tìm điểm bão hoà. Đây là lý do mọi thư viện vào ra đều có đệm, và là lý do xử lý theo lô luôn thắng xử lý từng phần tử khi có ranh giới nhân ở giữa. Chuyển ngữ cảnh khi nhân đổi tiến trình đang chạy: tốn vì phải lưu và khôi phục trạng thái, và tốn thêm vì bộ nhớ đệm bị làm nguội. Từ đó suy ra vì sao chạy quá nhiều luồng so với số lõi làm thông lượng giảm chứ tăng. Cách đo số lời gọi hệ thống và số lần chuyển ngữ cảnh của một chương trình thật, và dùng hai số đó làm bằng chứng thay vì suy đoán.

**Outcome.** Đo số lời gọi hệ thống của một chương trình và giảm nó bằng cách gộp lô, chứng minh bằng số đo thời gian.

**Đánh giá.** Tầng *áp dụng*. Objective là một tối ưu có cơ chế rõ và kết quả đo được hai chiều. Kiểm bằng cặp số đo lời gọi và thời gian; đạt khi số lời gọi giảm ít nhất một bậc và thời gian giảm tương ứng.

**Lab.** Viết chương trình đọc tệp 500 MB theo từng byte, đếm số lời gọi hệ thống và đo thời gian. Viết lại theo khối 64 KB và đo lại cả hai. Chạy một tác vụ tính với số luồng bằng 1, bằng số lõi và gấp 8 lần số lõi; đo thông lượng và số lần chuyển ngữ cảnh.

**Pitfalls.** Tối ưu thuật toán khi nút thắt là số lời gọi hệ thống · tăng số luồng cho tới khi máy chậm lại · đo thời gian mà không đếm lời gọi nên không biết nguyên nhân.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Số lời gọi hệ thống giảm ≥ 1 bậc sau khi gộp lô với thời gian giảm tương ứng, và bảng ba mức luồng cho thấy điểm quá tải.

### Lesson 55 · Amdahl, Gustafson and why adding threads stops helping `LT`
**Prerequisites.** Lesson 54

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài này trả lời một câu hỏi vận hành gặp liên tục: đã tăng số luồng mà thông lượng không tăng, vì sao. Bốn nguyên nhân và cách phân biệt bằng số đo. Một là nút thắt vốn không phải CPU: nếu đang chờ đĩa hoặc mạng thì thêm luồng tính không giúp gì, theo phân loại ở lesson 45. Hai là đã bão hoà lõi: vượt số lõi thì chỉ thêm chuyển ngữ cảnh, theo lesson 54. Ba là tranh khoá: các luồng chờ nhau ở vùng tranh chấp nên phần chạy song song thật nhỏ hơn nhiều so với số luồng. Bốn là bão hoà băng thông bộ nhớ: mọi luồng cùng kéo dữ liệu từ RAM và kênh bộ nhớ đầy, một nguyên nhân hay bị bỏ sót vì CPU vẫn hiện là bận. Định luật Amdahl ở mức dùng được: **phần không song song hoá được đặt trần cho toàn bộ nỗ lực thêm lõi**, và ước lượng được phần đó từ số đo. Góc nhìn đối lập cũng phải biết: khi bài toán lớn lên theo số lõi thì phần tuần tự chiếm tỉ lệ nhỏ dần, nên trần của định luật Amdahl áp cho bài toán cố định kích thước chứ mọi bài toán. Hai chỉ số phải báo cùng nhau là tăng tốc và hiệu suất song song, vì tăng tốc 4 lần trên 16 lõi là một kết quả kém mà con số tăng tốc không nói ra.

**Outcome.** Chẩn đoán một chương trình không tăng tốc khi thêm luồng về đúng một trong bốn nguyên nhân, dẫn bằng số đo.

**Đánh giá.** Tầng *phân tích*. Objective đòi phân biệt bốn nguyên nhân có biểu hiện bề ngoài giống nhau. Kiểm bằng bốn chương trình tiêm sẵn; đạt khi chẩn đoán đúng ít nhất ba và mỗi lần dẫn được số đo phân biệt.

**Lab.** Cho bốn chương trình không tăng tốc khi thêm luồng, mỗi cái một nguyên nhân. Với mỗi cái, đo mức dùng lõi, thời gian chờ vào ra, thời gian chờ khoá và băng thông bộ nhớ, rồi chẩn đoán. Với chương trình bị giới hạn bởi phần tuần tự, ước lượng tỉ lệ phần đó từ đồ thị tăng tốc.

**Pitfalls.** Kết luận thiếu CPU vì thấy CPU cao · bỏ qua băng thông bộ nhớ · thêm luồng cho tác vụ chờ đĩa · không đo thời gian chờ khoá.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chẩn đoán đúng ≥ 3/4 chương trình kèm số đo phân biệt, ước lượng được tỉ lệ phần tuần tự từ đồ thị, và mọi kết luận về tăng tốc đều kèm hiệu suất song song.

### Lesson 56 · MIMD - shared memory, distributed memory and SPMD `TH`
**Prerequisites.** Lesson 55

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài đi vào tầng song song thứ hai, nơi mỗi đơn vị thực thi có dòng lệnh riêng. Hai dạng và hai mô hình chi phí khác hẳn nhau. Bộ nhớ dùng chung: nhiều lõi cùng nhìn một không gian địa chỉ, nên cần giao thức nhất quán bộ nhớ đệm và cần đồng bộ; chia sẻ giả xảy ra khi hai lõi ghi hai biến khác nhau nằm cùng một dòng đệm, và nó làm chậm mà không có tranh chấp logic nào; truy cập bộ nhớ không đồng nhất biến vị trí bộ nhớ thành một quyết định đặt chỗ. Bộ nhớ phân tán: trao đổi bằng thông điệp qua mạng, nên độ trễ, chi phí tuần tự hoá, cách phân vùng và hỏng một phần trở thành mô hình chi phí và mô hình hỏng. Một chương trình nhiều dữ liệu là khuôn mẫu phổ biến trên cả hai. **Tăng tốc bị chặn bởi phần tuần tự, mất cân bằng, đồng bộ, truyền thông và băng thông bộ nhớ**, nên phải báo cáo cả tăng tốc lẫn hiệu suất song song chứ chỉ con số tăng tốc.

**Outcome.** Đo tăng tốc và hiệu suất song song khi tăng số đơn vị thực thi, và quy trần hiệu năng về đúng nguyên nhân.

**Đánh giá.** Tầng *phân tích*. Objective đòi giải thích vì sao đường tăng tốc bão hoà chứ chỉ vẽ nó. Kiểm bằng thí nghiệm thay đổi quy mô; đạt khi đường hiệu suất song song được vẽ tới ít nhất tám đơn vị và trần được quy về nguyên nhân bằng số đo.

**Lab.** Chạy cùng khối lượng công việc với 1, 2, 4 và 8 đơn vị thực thi; tính tăng tốc và hiệu suất song song ở mỗi mức. Ước lượng phần tuần tự từ đường cong và đối chiếu với dự đoán của định luật tăng tốc. Tái hiện chia sẻ giả và đo chi phí của nó. Chạy một bản đặt bộ nhớ ở nút xa và đo chênh lệch. Với bản phân tán, đo thời gian truyền thông tách khỏi thời gian tính.

**Pitfalls.** Báo cáo tăng tốc mà không báo hiệu suất song song · thêm đơn vị thực thi khi trần là băng thông bộ nhớ · bỏ qua chia sẻ giả vì không thấy tranh chấp trong mã · so bản phân tán mà không tách thời gian truyền thông.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đường hiệu suất song song có số đo tới ≥ 8 đơn vị, phần tuần tự được ước lượng từ dữ liệu, và trần hiệu năng được quy về nguyên nhân cụ thể.

### Lesson 57 · Linking the model to databases `LT`
**Prerequisites.** Lesson 56

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài nối, và nó biến mọi thứ đã đo thành công cụ đọc hành vi cơ sở dữ liệu ở M9 và M10. Bốn liên hệ bắt buộc. Trang và hồ đệm: cơ sở dữ liệu đọc ghi theo trang chứ theo dòng, và hồ đệm chính là bộ đệm trang của riêng nó, nên tỉ lệ trúng hồ đệm là chỉ số hiệu năng hàng đầu. Tra chỉ mục so với quét toàn bảng: tra chỉ mục là đọc ngẫu nhiên còn quét là đọc tuần tự, nên **khi số dòng cần lấy đủ lớn thì quét thắng dù chỉ mục tồn tại**, và đây là lý do bộ tối ưu đôi khi cố ý bỏ qua chỉ mục. Độ rẽ nhánh của cây B và chi phí đọc khối, nối lại lesson 36. Nhật ký ghi trước và `fsync`: mọi cam kết bền vững của giao dịch quy về một lần đẩy xuống đĩa, theo lesson 53. Ba câu hỏi để đọc một kế hoạch thực thi chậm trước khi biết cú pháp của công cụ nào.

**Outcome.** Giải thích bằng mô hình chi phí vì sao một truy vấn cụ thể chọn quét toàn bảng thay vì dùng chỉ mục.

**Đánh giá.** Tầng *hiểu*. Bài nối, chuẩn bị trực tiếp cho M9 và M10; chưa đòi vận hành cơ sở dữ liệu. Kiểm bằng bài lập luận trên bốn tình huống; đạt khi giải thích đúng ít nhất ba bằng chi phí đọc chứ bằng quy tắc thuộc lòng.

**Lab.** Cho bốn tình huống truy vấn với tỉ lệ dòng lấy ra khác nhau, từ 0,01% tới 40% bảng. Với mỗi tình huống, ước lượng số lần đọc ngẫu nhiên nếu dùng chỉ mục và số lần đọc tuần tự nếu quét, rồi dự đoán bộ tối ưu chọn cách nào. Ước lượng độ rẽ nhánh và chiều cao cây chỉ mục cho một bảng một triệu dòng.

**Pitfalls.** Cho rằng có chỉ mục thì luôn nên dùng chỉ mục · bỏ qua tỉ lệ dòng lấy ra · quên rằng tra chỉ mục còn phải đọc thêm dòng dữ liệu · học quy tắc thay vì tính chi phí.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Giải thích đúng ≥ 3/4 tình huống bằng ước lượng số lần đọc, và tính đúng chiều cao cây chỉ mục.

### Lesson 58 · Linking the model to distributed engines `LT`
**Prerequisites.** Lesson 57

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài nối thứ hai, chuẩn bị cho M18 và M12. Bốn liên hệ. Tuần tự hoá: dữ liệu đi qua mạng hoặc qua ranh giới tiến trình phải chuyển thành byte rồi chuyển lại, và chi phí đó thường lớn hơn phép tính; đây là lý do hàm do người dùng định nghĩa chậm hơn hàm dựng sẵn ở engine phân tán. Xáo trộn: gom dữ liệu cùng khoá về một chỗ nghĩa là ghi đĩa cục bộ, truyền mạng, đọc lại, tức là đi qua ba bậc chậm nhất của thứ bậc bộ nhớ cùng lúc, nên nó là thao tác đắt nhất. Tràn ra đĩa khi dữ liệu không vừa bộ nhớ, và vì sao đó là cơ chế tự bảo vệ chứ lỗi. Áp lực bộ nhớ và bộ dọn rác: giữ quá nhiều dữ liệu sống làm bộ dọn chạy liên tục và ăn CPU mà không làm việc hữu ích. Thực thi theo véc tơ ở engine cột khai thác đúng tính cục bộ ở lesson 47, nên hiểu lesson 47 là hiểu vì sao engine cột nhanh. Ba tầng song song lồng nhau đặt ra ở lesson 48 và lesson 56 gặp lại đầy đủ ở đây: tiến trình trên nhiều nút, toán tử xử lý theo lô trong mỗi tiến trình, và làn véctơ trong mỗi toán tử; M12 và M18 sẽ đo từng tầng riêng.

**Outcome.** Ước lượng thứ tự chi phí của bốn thao tác trong một công việc phân tán và chỉ ra thao tác đắt nhất.

**Đánh giá.** Tầng *hiểu*. Bài nối chuẩn bị cho M18; kiểm bằng lập luận chứ bằng vận hành engine. Kiểm bằng bài xếp hạng có lý do; đạt khi xếp đúng thứ tự và giải thích xáo trộn bằng ba bậc thứ bậc bộ nhớ.

**Lab.** Cho mô tả một công việc phân tán gồm đọc tệp, lọc, gộp nhóm theo khoá, và ghi kết quả. Xếp hạng chi phí bốn bước và giải thích từng bước bằng thứ bậc bộ nhớ ở lesson 45. Đo chi phí tuần tự hoá bằng cách so truyền một triệu bản ghi qua ranh giới tiến trình ở hai định dạng khác nhau.

**Pitfalls.** Nghĩ phép tính là phần đắt nhất · bỏ qua chi phí tuần tự hoá · coi tràn ra đĩa là lỗi cấu hình · xếp hạng theo cảm tính mà không đo.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Xếp đúng thứ tự chi phí bốn bước, giải thích xáo trộn bằng ba bậc thứ bậc bộ nhớ, và có số đo chi phí tuần tự hoá.

### Lesson 59 · Writing a performance report that survives review `TH`
**Prerequisites.** Lesson 58

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Số đo không có ngữ cảnh thì không thuyết phục được ai và cũng không dùng lại được sau ba tháng. Sáu phần của một báo cáo hiệu năng dùng được: khối lượng công việc mô tả đủ để lặp lại, môi trường gồm phần cứng và phiên bản, giả thuyết đặt trước khi đo, phương pháp đo gồm số lần lặp và cách xử lý giai đoạn khởi động, kết quả kèm mức phân tán chứ chỉ giá trị trung bình, và **giới hạn của kết luận**. Phần cuối là phần phân biệt báo cáo kỹ thuật với quảng cáo: nêu rõ kết luận này đúng trong khoảng nào và ngoài khoảng đó thì không biết. Vì sao báo cáo trung vị và phân vị cao thay vì trung bình: trung bình che mất đuôi phân bố, và đuôi mới là thứ người dùng cảm nhận. Ba cách trình bày số làm người đọc hiểu sai và cách tránh. Mẫu báo cáo này dùng lại ở mọi module có đo, tới tận M18 và M21.

**Outcome.** Viết một báo cáo hiệu năng đủ sáu phần cho một phép đo đã làm, và qua được rà soát chéo về phần giới hạn.

**Đánh giá.** Tầng *áp dụng*. Objective là sản phẩm viết theo chuẩn, đo bằng khả năng người khác lặp lại. Kiểm bằng rà soát chéo cộng phép thử lặp lại; đạt khi người khác lặp lại được phép đo và ra kết quả cùng bậc.

**Lab.** Chọn một phép đo đã làm trong module. Viết báo cáo đủ sáu phần, báo trung vị và phân vị 95 thay vì trung bình. Đưa cho một học viên khác: họ phải lặp lại được phép đo chỉ bằng báo cáo, trên máy của họ. So hai kết quả và giải thích chênh lệch bằng khác biệt môi trường.

**Pitfalls.** Báo giá trị trung bình · bỏ phần giới hạn · không ghi phiên bản và phần cứng · đo một lần rồi báo cáo.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Người khác lặp lại được phép đo chỉ bằng báo cáo và ra kết quả cùng bậc, và phần giới hạn nêu rõ khoảng áp dụng.

### Lesson 60 · Performance project - predict, measure, explain `DA`
**Prerequisites.** Lesson 59

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Bài dự án khép module, và điểm chấm nằm ở chất lượng lập luận chứ ở con số đẹp. Nhận một chương trình xử lý dữ liệu chạy chậm. Quy trình bắt buộc theo đúng thứ tự: đọc mã và **viết dự đoán nút thắt trước khi đo**, đo để xác nhận hoặc bác bỏ dự đoán, sửa đúng một thứ, đo lại, rồi lặp. Ghi lại mọi dự đoán sai và lý do sai, vì đó là phần có giá trị học tập cao nhất và cũng là phần hay bị giấu đi. Yêu cầu đạt: cải thiện ít nhất một mức bậc, kết quả tính ra không đổi, và mỗi lần sửa dẫn được về một số đo. Nộp kèm báo cáo hiệu năng sáu phần theo lesson 59 và sơ đồ đường đi của dữ liệu từ ứng dụng tới thiết bị theo yêu cầu của module. Cấm một điều: sửa nhiều chỗ cùng lúc, vì khi đó không biết chỗ nào có tác dụng.

**Outcome.** Tăng tốc một chương trình ít nhất một mức bậc, mỗi lần sửa dẫn được về một số đo, và kết quả tính ra không đổi.

**Đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module thành một quy trình tối ưu có bằng chứng. Kiểm bằng cặp số đo trước sau cộng rà soát nhật ký; đạt khi cải thiện đạt ngưỡng, kết quả không đổi, và mọi lần sửa có số đo dẫn chứng.

**Lab.** Nhận chương trình chậm. Viết dự đoán trước. Đo, sửa từng thứ một, đo lại sau mỗi lần. Ghi nhật ký gồm cả dự đoán sai. Nộp báo cáo sáu phần và sơ đồ đường đi dữ liệu. Đối soát kết quả tính ra với bản gốc.

**Pitfalls.** Sửa nhiều chỗ cùng lúc · tối ưu trước khi đo · giấu dự đoán sai · cải thiện tốc độ mà đổi kết quả tính ra.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Cải thiện ≥ 1 mức bậc, kết quả tính ra khớp tuyệt đối với bản gốc, và mọi lần sửa dẫn được về một số đo trong nhật ký.

# MODULE M5 · OPERATING SYSTEMS, CONCURRENCY AND LINUX

**Phase 2 · Lessons 61–76 · 32 giờ**

| | |
|---|---|
| **Objective cấp module** | Dùng bằng chứng từ Linux để chẩn đoán tiến trình, bộ nhớ, hệ tệp, socket và tranh chấp, thay vì đoán từ triệu chứng |
| **Tiền đề** | M2 · M4 |
| **Exit criterion** | Chẩn đoán đúng bốn tình huống tải khác nhau chỉ bằng số đo hệ thống, sửa được một rò rỉ mô tả tệp cùng một khoá chết, và truy được đường từ hiệp trình tới tác vụ tới vòng lặp sự kiện tới bộ theo dõi tới mô tả tệp không chặn |
| **Kỹ năng SFIA** | `SYSP` mức 4 · `PROG` mức 3 |
| **Chế độ hỏng** | Học thuộc danh sách lệnh mà không biết mỗi lệnh đo cái gì, nên khi hệ chậm thì chạy lần lượt mọi lệnh và vẫn không kết luận được |

Đây là module công cụ chẩn đoán của cả chương trình. Mọi module vận hành sau, từ M10 tới M21, đều giả định người học đọc được số đo hệ thống và phân biệt được bốn loại tải.

Phần đồng thời ở đây là phần hệ điều hành của chủ đề đã học ở mức ngôn ngữ tại lesson 22 tới 29; hai phần bổ sung nhau chứ lặp lại.

### Lesson 61 · User mode, kernel mode and the process lifecycle `LT`
**Prerequisites.** Module 5: M2 · M4

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Hai chế độ thực thi và ranh giới giữa chúng là thứ đã gặp ở lesson 54 dưới góc chi phí; bài này nhìn từ góc cơ chế. Chương trình chạy ở chế độ người dùng và không đụng trực tiếp vào phần cứng; mọi yêu cầu đều qua lời gọi hệ thống. Ngắt và bẫy là hai đường vào nhân khác nhau. Vòng đời tiến trình: tạo bằng nhân bản rồi thay thế ảnh chương trình, và vì sao hai bước đó tách rời lại hữu dụng. Các trạng thái của tiến trình và ý nghĩa vận hành của từng trạng thái, đặc biệt trạng thái chờ vào ra không ngắt được vì nó là dấu hiệu đĩa hoặc mạng có vấn đề. Tiến trình xác sống và tiến trình mồ côi, cùng cách chúng phát sinh; nối lại vấn đề tiến trình con mồ côi đã gặp ở lesson 23. Tiến trình so với luồng ở mức nhân: khác nhau ở chỗ chia sẻ không gian địa chỉ hay không, và mọi hệ quả suy ra từ đó.

**Outcome.** Đọc trạng thái của một tiến trình và suy ra nó đang chờ cái gì, phân biệt được chờ vào ra với chờ CPU.

**Đánh giá.** Tầng *hiểu*. Bài mở module, đặt từ vựng cho phần chẩn đoán sau. Kiểm bằng bài đọc trạng thái trên năm tiến trình thật; đạt khi phân loại đúng ít nhất bốn và nhận ra đúng tiến trình đang ở trạng thái chờ vào ra không ngắt được.

**Lab.** Tạo năm tiến trình ở năm trạng thái khác nhau gồm đang chạy, chờ được cấp CPU, chờ vào ra, dừng, và xác sống. Quan sát trạng thái qua công cụ hệ thống và qua hệ tệp ảo của nhân. Phân loại từng cái. Tạo một tiến trình mồ côi và quan sát nó được nhận nuôi.

**Pitfalls.** Nhầm chờ vào ra với chờ CPU nên chẩn đoán sai · không biết trạng thái xác sống nghĩa là gì · dùng lệnh liệt kê tiến trình mà không đọc cột trạng thái.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân loại đúng ≥ 4/5 trạng thái, và nhận ra đúng tiến trình đang chờ vào ra không ngắt được.

### Lesson 62 · Scheduling, priority and load average `TH`
**Prerequisites.** Lesson 61

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bộ lập lịch quyết định tiến trình nào chạy khi nào, và hiểu nó giải thích vài chỉ số hay bị đọc sai. Lát thời gian và tính công bằng; độ ưu tiên và giá trị nhường. Chỉ số tải trung bình là chỉ số bị hiểu sai nhiều nhất trên Linux: nó đếm cả tiến trình đang chạy lẫn tiến trình đang chờ vào ra không ngắt được, nên **tải trung bình cao không đồng nghĩa CPU bận**; một máy đĩa hỏng có tải trung bình rất cao trong khi CPU rảnh. Cách đọc đúng: so tải trung bình với số lõi, rồi đối chiếu với tỉ lệ CPU chờ vào ra để biết đang nghẽn ở đâu. Mức dùng CPU chia theo loại và ý nghĩa của từng loại, đặc biệt phần chờ vào ra và phần bị đánh cắp trên máy ảo. Độ dài hàng đợi chạy. Ba tình huống mà thêm tiến trình làm mọi thứ chậm đi thay vì nhanh lên.

**Outcome.** Phân biệt máy nghẽn CPU với máy nghẽn vào ra chỉ bằng chỉ số hệ thống, không cần đọc mã.

**Đánh giá.** Tầng *phân tích*. Objective là đọc và diễn giải chỉ số đúng, kỹ năng dùng trực tiếp khi trực. Kiểm bằng bốn máy mô phỏng; đạt khi phân loại đúng ít nhất ba và mỗi lần dẫn được chỉ số phân biệt chứ chỉ tải trung bình.

**Lab.** Tạo bốn tình huống tải: bão hoà CPU, chờ vào ra nặng, áp lực bộ nhớ, và nhiều tiến trình chờ được cấp CPU. Với mỗi tình huống, ghi tải trung bình, mức dùng CPU chia theo loại, và độ dài hàng đợi chạy. Phân loại từng tình huống. Chỉ ra tình huống nào có tải trung bình cao mà CPU rảnh.

**Pitfalls.** Kết luận CPU bận vì tải trung bình cao · so tải trung bình mà quên số lõi · bỏ qua phần chờ vào ra trong mức dùng CPU.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân loại đúng ≥ 3/4 tình huống, và chỉ ra đúng tình huống tải trung bình cao trong khi CPU rảnh.

### Lesson 63 · Memory - virtual, resident, shared and OOM `TH`
**Prerequisites.** Lesson 62

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Câu hỏi tiến trình này dùng bao nhiêu bộ nhớ không có một câu trả lời duy nhất, và chọn sai chỉ số dẫn tới kết luận sai. Bốn chỉ số và ý nghĩa: bộ nhớ ảo là không gian địa chỉ đã đăng ký và thường lớn vô lý nên gần như vô dụng để đánh giá; bộ nhớ thường trú là phần thật đang trong RAM; bộ nhớ chia sẻ bị đếm nhiều lần khi cộng các tiến trình; và kích thước tập làm việc là phần thật sự đang được dùng. Bộ nhớ khả dụng khác bộ nhớ trống: phần bộ đệm trang tính là dùng nhưng giải phóng được ngay, nên **bộ nhớ trống thấp không phải vấn đề**, và đây là báo động giả phổ biến nhất. Bộ giết khi cạn bộ nhớ: khi nào kích hoạt, chọn nạn nhân theo điểm số nào, và cách đọc bản ghi của nó trong nhật ký nhân; nối lại tình huống tác vụ bị giết ở tầng container sẽ gặp ở M20.

**Outcome.** Chọn đúng chỉ số để trả lời câu hỏi một tiến trình dùng bao nhiêu bộ nhớ, và đọc được bản ghi của bộ giết khi cạn bộ nhớ.

**Đánh giá.** Tầng *phân tích*. Objective đòi chọn đúng công cụ đo cho câu hỏi, chỗ rất dễ kết luận sai. Kiểm bằng bài đo cộng thí nghiệm cạn bộ nhớ; đạt khi chọn đúng chỉ số và đọc đúng nguyên nhân từ nhật ký nhân.

**Lab.** Chạy ba tiến trình có hồ sơ bộ nhớ khác nhau gồm ánh xạ tệp lớn, cấp phát thật lớn, và dùng chung thư viện. Với mỗi cái, ghi cả bốn chỉ số và giải thích chênh lệch. Đẩy máy tới cạn bộ nhớ, tìm bản ghi của bộ giết trong nhật ký nhân và xác định nạn nhân cùng lý do.

**Pitfalls.** Dùng bộ nhớ ảo để đánh giá mức dùng · cộng bộ nhớ thường trú của nhiều tiến trình dùng chung thư viện · hoảng vì bộ nhớ trống thấp · không biết tìm bản ghi bộ giết ở đâu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chọn đúng chỉ số cho cả ba tiến trình kèm giải thích chênh lệch, và đọc đúng nạn nhân cùng lý do từ nhật ký nhân.

### Lesson 64 · Filesystems, inodes, file descriptors and leaks `TH`
**Prerequisites.** Lesson 63

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hệ tệp tách tên khỏi nội dung: nút chỉ mục giữ siêu dữ liệu và con trỏ tới khối, còn thư mục chỉ là ánh xạ tên sang nút chỉ mục. Từ đó suy ra ba điều hay gây ngạc nhiên: liên kết cứng là hai tên trỏ cùng nút chỉ mục nên xoá một tên không xoá dữ liệu; **xoá một tệp đang được tiến trình mở thì dung lượng không được giải phóng cho tới khi tiến trình đóng**, và đây là nguyên nhân kinh điển của việc đĩa đầy mà tìm không ra tệp nào; và đổi tên trong cùng hệ tệp là thao tác rẻ vì chỉ đổi mục thư mục. Mô tả tệp là chỉ số trỏ vào bảng của tiến trình, và giới hạn số mô tả tệp là giới hạn hay chạm trong dịch vụ dữ liệu. Rò rỉ mô tả tệp: triệu chứng, cách tìm bằng hệ tệp ảo của nhân, và cách sửa bằng trình quản lý ngữ cảnh ở lesson 15. Hai lệnh đo dung lượng cho kết quả khác nhau và lý do.

**Outcome.** Tìm được nguyên nhân đĩa đầy mà không thấy tệp, và định vị một rò rỉ mô tả tệp về đúng đoạn mã.

**Đánh giá.** Tầng *phân tích*. Objective là hai chẩn đoán cụ thể mà người mới gần như luôn bế tắc. Kiểm bằng hai tình huống tiêm sẵn tính giờ; đạt khi tìm ra nguyên nhân cả hai và sửa được rò rỉ có bằng chứng số mô tả tệp không tăng.

**Lab.** Tạo tình huống đĩa đầy do tệp đã xoá nhưng còn mở; dùng công cụ hệ thống tìm ra tiến trình giữ nó. Chạy một dịch vụ rò rỉ mô tả tệp, quan sát số mô tả tăng theo thời gian, định vị đoạn mã, sửa bằng trình quản lý ngữ cảnh, và chứng minh số mô tả ổn định sau 10.000 yêu cầu.

**Pitfalls.** Xoá tệp rồi tưởng đã giải phóng dung lượng · so hai lệnh đo dung lượng mà không biết vì sao khác nhau · tăng giới hạn mô tả tệp thay vì sửa rò rỉ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tìm đúng tiến trình giữ tệp đã xoá, và sau khi sửa thì số mô tả tệp ổn định qua 10.000 yêu cầu.

### Lesson 65 · Non-blocking descriptors, select, poll and epoll `TH`
**Prerequisites.** Lesson 64

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài giải thích cơ chế dưới mọi vòng lặp sự kiện, nên nó là nền của phần bất đồng bộ đã học ở M2. Bộ mô tả chặn làm luồng gọi ngủ tới khi thao tác xong; bộ mô tả không chặn trả về ngay một trạng thái chưa sẵn sàng thay vì chờ, nên một luồng theo dõi được nhiều kết nối. Ba thế hệ cơ chế theo dõi và khác biệt về chi phí: hai cơ chế cũ quét toàn bộ tập bộ mô tả mỗi lần gọi nên chi phí tăng theo số kết nối; cơ chế mới giữ sẵn tập quan tâm và chỉ trả về phần đã sẵn sàng, nên chi phí không tăng theo số kết nối đang mở. Hai chế độ báo: báo theo mức lặp lại trạng thái tới khi được xử lý, báo theo sườn chỉ báo một lần khi trạng thái đổi; **chế độ báo theo sườn bắt buộc đọc tới khi hết dữ liệu**, và bỏ quy tắc đó làm treo kết nối mà không có lỗi nào. Tệp thường không có ngữ nghĩa sẵn sàng hữu ích như ổ cắm.

**Outcome.** Viết một máy chủ một luồng theo dõi nhiều kết nối và đo chi phí của hai cơ chế theo dõi khi số kết nối tăng.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là đường chi phí theo số kết nối. Kiểm bằng phép đo thay đổi quy mô; đạt khi hai đường chi phí tách nhau rõ ở 10.000 kết nối và ca báo theo sườn bị treo được tái hiện rồi sửa.

**Lab.** Viết máy chủ một luồng dùng bộ mô tả không chặn. Cài cả hai cơ chế theo dõi. Đo thời gian mỗi vòng lặp ở 100, 1.000 và 10.000 kết nối nhàn rỗi, vẽ hai đường. Chuyển sang chế độ báo theo sườn mà không đọc tới khi hết dữ liệu, tái hiện kết nối treo, rồi sửa theo quy tắc đọc cạn.

**Pitfalls.** Dùng bộ mô tả chặn trong vòng lặp sự kiện · dùng chế độ báo theo sườn mà không đọc cạn · đo chi phí chỉ ở số kết nối nhỏ · giả định tệp thường có ngữ nghĩa sẵn sàng như ổ cắm.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Hai đường chi phí tách nhau rõ ở 10.000 kết nối, và ca treo do báo theo sườn được tái hiện rồi sửa.

### Lesson 66 · Readiness against completion - partial I/O, cancellation and io_uring awareness `TH`
**Prerequisites.** Lesson 65

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hai mô hình vào ra khác nhau ở chỗ hệ điều hành báo gì cho ứng dụng. Mô hình sẵn sàng báo rằng thao tác có thể tiến triển, còn ứng dụng tự gọi đọc hoặc ghi; mô hình hoàn tất nhận yêu cầu rồi báo khi đã xong. Hệ quả quan trọng nhất của mô hình sẵn sàng và là lỗi hay gặp: **sẵn sàng không bảo đảm đọc hoặc ghi được trọn vẹn thông điệp**, nên mọi lời gọi phải xử lý đọc thiếu và ghi thiếu, và ứng dụng phải tự đóng khung thông điệp. Huỷ bỏ ở tầng ứng dụng không tự hoàn tác một lời gọi hệ thống đã phát ra hay một tác dụng phụ đã xảy ra ở bên kia, nên ranh giới sở hữu, dọn dẹp và công bố phải do mã định nghĩa, đúng nguyên tắc ở lesson 27. Giao diện gửi và nhận theo hàng đợi ở mức nhận biết: nó giảm số lời gọi hệ thống và chi phí chuyển ngữ cảnh, và **không dùng chỉ vì nó mới** khi khối lượng công việc và môi trường chạy chưa hưởng lợi.

**Outcome.** Xử lý đúng đọc thiếu và ghi thiếu dưới tải, và nêu ranh giới mà huỷ bỏ không hoàn tác được.

**Đánh giá.** Tầng *áp dụng*. Objective có một ca hỏng đặc trưng chỉ lộ ra dưới tải. Kiểm bằng phép thử thông điệp lớn; đạt khi không thông điệp nào bị cắt hay ghép sai qua 10.000 lượt và ca huỷ giữa chừng được mô tả đúng hậu quả.

**Lab.** Viết bên gửi và bên nhận trao đổi thông điệp lớn hơn bộ đệm ổ cắm. Chạy 10.000 lượt dưới tải và đếm số thông điệp bị cắt hoặc ghép sai khi chưa xử lý đọc thiếu, rồi sửa bằng cách đóng khung và lặp tới đủ. Huỷ một thao tác giữa chừng sau khi đã ghi một phần và mô tả trạng thái bên kia nhìn thấy. Viết một đoạn nêu điều kiện mà giao diện theo hàng đợi đáng cân nhắc.

**Pitfalls.** Giả định một lần gọi đọc trả về trọn thông điệp · không đóng khung thông điệp · tin rằng huỷ bỏ hoàn tác được tác dụng phụ đã gửi đi · chọn giao diện mới vì nghe hiện đại.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Không thông điệp nào bị cắt hay ghép sai qua 10.000 lượt, và hậu quả của huỷ giữa chừng được mô tả đúng ở phía bên kia.

### Lesson 67 · Signals, exit codes and graceful shutdown `TH`
**Prerequisites.** Lesson 66

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Tín hiệu là cách nhân và các tiến trình báo cho nhau, và xử lý sai tín hiệu là nguyên nhân mất dữ liệu khi triển khai. Phân biệt hai tín hiệu dừng: một cái bắt được và cho phép dọn dẹp, một cái không bắt được và giết ngay. Quy trình tắt đúng của một tiến trình xử lý dữ liệu: nhận tín hiệu, ngừng nhận việc mới, hoàn tất việc đang dở trong hạn, đẩy dữ liệu xuống đĩa, rồi thoát với mã đúng. Thời gian chờ trước khi bị giết cứng là hữu hạn nên phần dọn dẹp phải nằm trong hạn đó, và đây là ràng buộc sẽ gặp lại ở M20. Mã thoát và quy ước: không là thành công, khác không là thất bại, và bị tín hiệu giết thì mã thoát mã hoá số hiệu tín hiệu. Vì sao mã thoát đúng quan trọng: hệ điều phối ở M14 và hệ chạy container ở M20 đều dựa vào nó để biết việc thành công hay thất bại.

**Outcome.** Cài đặt tắt có kiểm soát cho một tiến trình xử lý và chứng minh không mất việc đang dở khi nhận tín hiệu dừng.

**Đánh giá.** Tầng *áp dụng*. Objective là một cơ chế kiểm được bằng thí nghiệm dừng. Kiểm bằng 20 lần gửi tín hiệu ở thời điểm ngẫu nhiên; đạt khi không lần nào mất việc và mã thoát đúng ở mọi trường hợp.

**Lab.** Viết tiến trình xử lý hàng đợi. Cài bắt tín hiệu dừng, hoàn tất việc đang dở, đẩy dữ liệu xuống đĩa rồi thoát. Gửi tín hiệu dừng 20 lần ở thời điểm ngẫu nhiên và đối soát kết quả. Gửi tín hiệu giết cứng và ghi lại khác biệt. Kiểm mã thoát ở ba trường hợp thành công, thất bại và bị giết.

**Pitfalls.** Không bắt tín hiệu nên bị giết giữa lúc ghi · dọn dẹp quá lâu rồi bị giết cứng · trả mã thoát không khi thực ra thất bại · dùng shell làm tiến trình chính nên tín hiệu không tới được chương trình.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** 20 lần gửi tín hiệu dừng đều không mất việc đang dở, và mã thoát đúng ở cả ba trường hợp.

### Lesson 68 · Shell scripting that fails loudly `TH`
**Prerequisites.** Lesson 67

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Shell là keo dán của mọi hệ vận hành, và script shell viết ẩu là nguồn sự cố âm thầm vì mặc định của shell là chạy tiếp khi có lỗi. Ba tuỳ chọn nghiêm ngặt và tác dụng từng cái: dừng khi một lệnh lỗi, coi biến chưa đặt là lỗi, và cho lỗi trong đường ống lan ra. Kèm theo là cảnh báo về các trường hợp tuỳ chọn dừng khi lỗi **không** kích hoạt, vì tin tưởng mù vào nó cũng nguy hiểm. Trích dẫn và khai triển: quên ngoặc kép quanh biến là nguồn lỗi số một khi tên tệp có dấu cách. Bẫy để dọn dẹp khi thoát, tương đương trình quản lý ngữ cảnh ở lesson 15. Mã thoát và cách kiểm tra từng bước theo lesson 67. Khi nào nên dừng viết shell và chuyển sang Python: ba dấu hiệu cụ thể, thường là khi cần cấu trúc dữ liệu, cần xử lý lỗi phân tầng, hoặc script vượt khoảng một trăm dòng.

**Outcome.** Viết script vận hành dừng đúng lúc lỗi, dọn dẹp khi thoát, và trả mã thoát đúng trong mọi nhánh.

**Đánh giá.** Tầng *áp dụng*. Objective là một tập quy tắc kiểm được bằng thí nghiệm tiêm lỗi. Kiểm bằng năm lỗi tiêm; đạt khi cả năm đều làm script dừng với mã thoát khác không và tài nguyên tạm được dọn.

**Lab.** Viết script nạp dữ liệu có tạo thư mục tạm, tải tệp, xử lý, rồi dọn. Tiêm năm lỗi: lệnh thất bại giữa chừng, biến chưa đặt, lỗi trong đường ống, tên tệp có dấu cách, và bị dừng giữa chừng. Chứng minh cả năm được xử lý đúng và thư mục tạm luôn được dọn.

**Pitfalls.** Quên ngoặc kép quanh biến · tin tuỳ chọn dừng khi lỗi bắt được mọi trường hợp · không dọn khi bị dừng giữa chừng · viết 500 dòng shell cho việc cần Python.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Năm lỗi đều làm script dừng với mã thoát khác không, và thư mục tạm được dọn trong cả năm trường hợp.

### Lesson 69 · Services with systemd and the journal `TH`
**Prerequisites.** Lesson 68

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Chạy một tiến trình lâu dài bằng cách mở terminal rồi để đó không phải cách vận hành, và trình quản lý dịch vụ giải bốn việc: khởi động cùng máy, khởi động lại khi chết, thu thập nhật ký, và quản lý phụ thuộc giữa các dịch vụ. Tệp định nghĩa dịch vụ và các trường quan trọng: lệnh chạy, người dùng chạy, chính sách khởi động lại, biến môi trường, và giới hạn tài nguyên. Chính sách khởi động lại và bẫy vòng lặp: dịch vụ chết ngay khi khởi động cộng với chính sách luôn khởi động lại cho ra vòng lặp khởi động liên tục, nên phải đặt giới hạn số lần trong một khoảng. Nhật ký tập trung: đọc theo dịch vụ, theo thời gian, theo mức, và vì sao ghi ra luồng chuẩn tiện hơn tự ghi tệp, nối lại nguyên tắc ở lesson 20. Ranh giới bí mật: biến môi trường trong tệp định nghĩa đọc được bởi ai, và cách đưa bí mật vào đúng cách.

**Outcome.** Chạy một dịch vụ dữ liệu dưới trình quản lý dịch vụ với chính sách khởi động lại đúng và nhật ký đọc được tập trung.

**Đánh giá.** Tầng *áp dụng*. Objective là một cấu hình vận hành kiểm được bằng thí nghiệm giết tiến trình. Kiểm bằng ba phép thử; đạt khi dịch vụ tự khởi động lại, vòng lặp khởi động bị chặn, và nhật ký truy được theo mã theo dõi.

**Lab.** Đóng gói tiến trình xử lý ở lesson 67 thành một dịch vụ. Giết nó và xác nhận tự khởi động lại. Làm nó chết ngay khi khởi động và xác nhận giới hạn số lần chặn được vòng lặp. Đọc nhật ký theo dịch vụ và lọc theo mã theo dõi. Đưa một bí mật vào đúng cách và kiểm tài khoản thường không đọc được.

**Pitfalls.** Đặt chính sách luôn khởi động lại mà không giới hạn số lần · chạy dịch vụ bằng quyền quản trị · ghi nhật ký vào tệp riêng thay vì luồng chuẩn · đặt bí mật thẳng trong tệp định nghĩa dịch vụ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Dịch vụ tự khởi động lại sau khi bị giết, vòng lặp khởi động bị chặn theo giới hạn, và nhật ký lọc được theo mã theo dõi.

### Lesson 70 · Races, locks and deadlock at the OS level `TH`
**Prerequisites.** Lesson 69

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phần này lặp lại chủ đề của lesson 22 nhưng ở tầng hệ điều hành và với công cụ chẩn đoán thật. Ba tính chất phải phân biệt vì chúng hỏng theo ba cách khác nhau: tính nguyên tử, tính nhìn thấy được, và thứ tự. Ba nguyên hàm đồng bộ và khi nào dùng cái nào: khoá loại trừ, cờ hiệu đếm, và biến điều kiện. Bốn điều kiện cần cùng lúc để có khoá chết, và phá bất kỳ điều kiện nào là chặn được; cách phá thực dụng nhất là quy định thứ tự lấy khoá. Đói tài nguyên và khoá sống là hai chế độ hỏng khác khoá chết và cần cách chữa khác. Đo tranh chấp: thời gian tiến trình nằm chờ ở nguyên hàm đồng bộ quan sát được bằng công cụ theo dõi lời gọi hệ thống, nên tranh chấp là thứ đo được chứ đoán. Từ số đo đó suy ra phần song song thật, nối lại định luật ở lesson 55.

**Outcome.** Chẩn đoán một khoá chết thật bằng công cụ hệ thống và sửa bằng cách phá đúng một trong bốn điều kiện.

**Đánh giá.** Tầng *phân tích*. Objective đòi truy từ hiện tượng treo về cấu trúc lấy khoá, dùng bằng chứng hệ thống. Kiểm bằng tình huống khoá chết tiêm sẵn tính giờ; đạt khi định vị đúng cặp khoá và nêu đúng điều kiện đã phá.

**Lab.** Viết chương trình có hai khoá lấy theo thứ tự chéo nhau và làm nó treo. Dùng công cụ theo dõi lời gọi hệ thống để thấy cả hai luồng đang chờ ở đâu. Sửa bằng cách quy định thứ tự lấy khoá. Đo thời gian chờ ở nguyên hàm đồng bộ trước và sau khi giảm vùng tranh chấp.

**Pitfalls.** Thêm khoá bao quanh mọi thứ · tăng thời gian chờ khoá thay vì sửa thứ tự · kết luận treo do mạng mà chưa xem tiến trình đang chờ gì · không đo tranh chấp.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Định vị đúng cặp khoá gây treo bằng bằng chứng hệ thống, sửa xong chương trình không treo qua 1000 lần chạy, và có số đo tranh chấp trước sau.

### Lesson 71 · Tracing a program with strace and perf `TH`
**Prerequisites.** Lesson 70

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hai công cụ trả lời hai câu hỏi khác nhau, và biết dùng cái nào cho câu nào tiết kiệm rất nhiều thời gian. Theo dõi lời gọi hệ thống trả lời chương trình đang nói gì với nhân: mở tệp nào, kết nối tới đâu, chờ ở đâu; rất hữu dụng khi chương trình treo hoặc khi không rõ nó đọc tệp cấu hình nào. Nhược điểm là làm chương trình chậm đáng kể nên không dùng trong sản xuất khi tải cao. Lấy mẫu hiệu năng trả lời thời gian CPU tiêu ở hàm nào, nhẹ nên dùng được trong sản xuất, nhưng không thấy phần chờ. Từ đó rút ra quy tắc chọn: chương trình bận CPU thì lấy mẫu hiệu năng, chương trình treo hoặc chờ thì theo dõi lời gọi hệ thống. Cách đọc kết quả: đếm theo lời gọi để thấy cái nào nhiều, và xem thời gian nằm trong lời gọi nào để thấy chờ ở đâu. Nối tới M21: đây là hai công cụ của bước chẩn đoán trong quy trình xử lý sự cố.

**Outcome.** Chọn đúng công cụ cho một triệu chứng cho trước và định vị nguyên nhân từ kết quả của nó.

**Đánh giá.** Tầng *phân tích*. Objective là chọn công cụ theo câu hỏi rồi đọc kết quả, kỹ năng dùng lại suốt phần vận hành. Kiểm bằng ba chương trình có ba triệu chứng; đạt khi chọn đúng công cụ ít nhất hai và định vị đúng nguyên nhân.

**Lab.** Cho ba chương trình: một treo khi khởi động, một bận CPU bất thường, một chậm vì gọi hệ thống quá nhiều. Với mỗi cái, chọn công cụ, chạy, và định vị nguyên nhân. Với chương trình treo, chỉ ra chính xác lời gọi hệ thống nó đang chờ.

**Pitfalls.** Dùng theo dõi lời gọi hệ thống cho chương trình bận CPU · chạy công cụ theo dõi trên sản xuất lúc tải cao · đọc kết quả mà không đếm theo lời gọi · bỏ qua thời gian nằm trong lời gọi.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chọn đúng công cụ ≥ 2/3 trường hợp và định vị đúng nguyên nhân, kể cả chỉ ra lời gọi mà chương trình treo đang chờ.

### Lesson 72 · Distinguishing four kinds of system pressure `TH`
**Prerequisites.** Lesson 71

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài tổng hợp phần chẩn đoán, và nó là thứ dùng nhiều nhất khi trực. Bốn loại tải và bộ chỉ số phân biệt từng loại. Bão hoà CPU: mức dùng cao ở phần người dùng hoặc phần nhân, hàng đợi chạy dài, chờ vào ra thấp. Nghẽn vào ra: chờ vào ra cao, độ sâu hàng đợi thiết bị cao, thời gian phục vụ cao, trong khi CPU rảnh. Áp lực bộ nhớ: lỗi trang nặng tăng, hoạt động hoán đổi, bộ nhớ khả dụng thấp; phân biệt với bộ nhớ trống thấp theo lesson 63. Đĩa đầy: khác ba loại trên vì nó làm thao tác ghi thất bại chứ chỉ chậm, và có thể do tệp đã xoá còn mở theo lesson 64. Quy trình chẩn đoán bốn bước theo thứ tự cố định để không bỏ sót. Nguyên tắc: **kết luận phải dẫn được về ít nhất hai chỉ số nhất quán với nhau**, vì một chỉ số đơn lẻ dễ dẫn tới kết luận sai.

**Outcome.** Chẩn đoán đúng loại tải trong bốn loại chỉ bằng chỉ số hệ thống, trong giới hạn thời gian.

**Đánh giá.** Tầng *phân tích*. Objective là chẩn đoán dưới áp lực thời gian, đúng điều kiện khi trực. Kiểm bằng bốn tình huống tiêm sẵn, mỗi tình huống 8 phút; đạt khi chẩn đoán đúng ít nhất ba và mỗi lần dẫn được hai chỉ số nhất quán.

**Lab.** Giảng viên tạo lần lượt bốn loại tải trên một máy, mỗi lần 8 phút. Với mỗi lần, chạy quy trình bốn bước, ghi bộ chỉ số, và kết luận. Với tình huống đĩa đầy, xác định thêm nguyên nhân là tệp thật hay tệp đã xoá còn mở.

**Pitfalls.** Kết luận từ một chỉ số · chạy mọi lệnh rồi vẫn không kết luận · nhầm bộ nhớ trống thấp với áp lực bộ nhớ · bỏ qua bước xác định nguyên nhân sâu hơn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chẩn đoán đúng ≥ 3/4 tình huống trong giới hạn thời gian, mỗi lần dẫn được hai chỉ số nhất quán.

### Lesson 73 · Permissions, users and the least-privilege habit `TH`
**Prerequisites.** Lesson 72

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Quyền trên Linux là tầng phòng vệ đầu tiên và cũng là tầng hay bị vô hiệu hoá vì tiện. Ba nhóm quyền và ba loại quyền, cùng cách đọc và đặt. Mặt nạ tạo tệp quyết định quyền mặc định của tệp mới và là nguồn lỗi hay gặp khi một dịch vụ ghi tệp mà dịch vụ khác không đọc được. Quyền trên thư mục có nghĩa khác quyền trên tệp và đây là chỗ hay nhầm: quyền thực thi trên thư mục nghĩa là đi vào được. Chạy dịch vụ bằng người dùng riêng có quyền tối thiểu thay vì quyền quản trị: lý do không phải hình thức mà là phạm vi thiệt hại khi dịch vụ bị lợi dụng. Chủ sở hữu tệp giữa tiến trình trong container và tiến trình trên máy chủ, một vấn đề sẽ gặp lại ở M20. Ba phép thử truy cập trái phép phải chạy sau khi đặt quyền, vì đặt quyền mà không thử là không biết nó có tác dụng không.

**Outcome.** Đặt quyền tối thiểu cho một dịch vụ và chứng minh bằng phép thử rằng tài khoản khác không đọc hay ghi được.

**Đánh giá.** Tầng *áp dụng*. Objective là một cấu hình bảo mật kiểm được bằng phép thử phủ định. Kiểm bằng ba phép thử truy cập trái phép; đạt khi cả ba bị từ chối và dịch vụ vẫn chạy đúng.

**Lab.** Chạy dịch vụ ở lesson 69 bằng người dùng riêng. Đặt quyền tối thiểu cho thư mục dữ liệu và tệp cấu hình. Thử đọc, ghi và thực thi bằng một tài khoản khác và ghi lại kết quả cả ba. Đặt mặt nạ tạo tệp và kiểm tệp mới sinh ra có quyền đúng.

**Pitfalls.** Chạy dịch vụ bằng quyền quản trị cho tiện · đặt quyền mở cho mọi người để hết lỗi · quên mặt nạ tạo tệp nên tệp mới sai quyền · đặt quyền mà không thử truy cập trái phép.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba phép thử truy cập trái phép đều bị từ chối, dịch vụ vẫn chạy đúng, và tệp mới sinh ra có quyền đúng theo mặt nạ.

### Lesson 74 · Networking from the command line `TH`
**Prerequisites.** Lesson 73

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bộ công cụ tối thiểu để trả lời câu hỏi vì sao không kết nối được, và bài này chuẩn bị trực tiếp cho M6. Năm câu hỏi theo thứ tự chẩn đoán và công cụ tương ứng cho từng câu: tên miền phân giải ra địa chỉ nào, máy có đường đi tới địa chỉ đó không, cổng có mở và có ai đang nghe không, bắt tay có thành công không, và ứng dụng trả lời gì. Đi theo thứ tự này tránh được việc đoán lung tung. Phân biệt ba loại thất bại có triệu chứng giống nhau nhưng nguyên nhân khác hẳn: không phân giải được tên, kết nối bị từ chối, và kết nối hết giờ; loại thứ ba thường là tường lửa chặn im lặng. Xem socket đang mở và trạng thái của chúng, đặc biệt trạng thái chờ đóng tích tụ nhiều là dấu hiệu cạn cổng tạm. Bắt gói ở mức đủ để xác nhận gói có đi ra không, chưa cần phân tích sâu vì phần đó ở M6.

**Outcome.** Chẩn đoán một lỗi kết nối về đúng một trong ba loại thất bại, theo đúng thứ tự năm bước.

**Đánh giá.** Tầng *phân tích*. Objective là một quy trình chẩn đoán có thứ tự, chuẩn bị cho M6. Kiểm bằng ba lỗi kết nối tiêm sẵn; đạt khi phân loại đúng ít nhất hai và chỉ ra bước nào trong năm bước phát hiện ra.

**Lab.** Giảng viên tạo ba lỗi kết nối: tên miền trỏ sai, dịch vụ không nghe cổng, và tường lửa chặn im lặng. Với mỗi lỗi, chạy đủ năm bước theo thứ tự và ghi bước nào phát hiện ra. Liệt kê socket đang mở và chỉ ra trạng thái chờ đóng nếu có.

**Pitfalls.** Bắt gói ngay từ đầu thay vì kiểm phân giải tên trước · nhầm bị từ chối với hết giờ · bỏ qua bước kiểm ai đang nghe cổng · không biết trạng thái socket nghĩa là gì.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân loại đúng ≥ 2/3 lỗi và chỉ ra đúng bước phát hiện, kèm bảng socket đang mở có đọc trạng thái.

### Lesson 75 · A diagnosis runbook for a data service `TH`
**Prerequisites.** Lesson 74

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài ghép: biến mọi kỹ năng chẩn đoán trong module thành một sổ tay dùng được lúc ba giờ sáng. Cấu trúc sổ tay theo đúng trình tự người trực cần, đã đặt ở lesson 10: triệu chứng nào, ảnh hưởng ra sao, chẩn đoán theo bước nào, giảm nhẹ thế nào, leo thang cho ai, và xác nhận đã hồi phục bằng gì. Năm mục bắt buộc cho một dịch vụ dữ liệu, mỗi mục tương ứng một bài đã học: dịch vụ không khởi động, dịch vụ chậm bất thường, đĩa đầy, rò rỉ mô tả tệp, và không kết nối được tới nguồn. Nguyên tắc viết: mỗi bước là một lệnh chạy được kèm cái cần nhìn trong kết quả, chứ một lời khuyên chung. Ngưỡng phải là số chứ tính từ. Phép thử của một sổ tay tốt là người chưa từng chạm vào hệ làm theo được, và đó chính là cách bài này chấm điểm.

**Outcome.** Viết sổ tay năm mục mà một người khác dùng được để chẩn đoán và khắc phục, không cần hỏi.

**Đánh giá.** Tầng *đánh giá*. Objective đo chất lượng sổ tay bằng kết quả của người dùng nó chứ bằng độ dày. Kiểm bằng phép thử với người ngoài; đạt khi họ xử lý được ít nhất ba trong năm tình huống mà không phải hỏi.

**Lab.** Viết sổ tay năm mục cho dịch vụ ở lesson 69. Đưa cho một học viên chưa từng chạm vào dịch vụ đó. Giảng viên tạo lần lượt năm tình huống; người kia chỉ được dùng sổ tay. Ghi lại tình huống nào họ xử lý được và mọi câu họ phải hỏi. Sửa sổ tay theo danh sách đó.

**Pitfalls.** Viết bước dạng kiểm tra nhật ký mà không nói tìm gì · đặt ngưỡng bằng tính từ · bỏ bước xác nhận đã hồi phục · viết cho người đã biết hệ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Người ngoài xử lý được ≥ 3/5 tình huống chỉ bằng sổ tay, và bản sửa sau đó giảm được số câu phải hỏi.

### Lesson 76 · Linux diagnosis project `DA`
**Prerequisites.** Lesson 75

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Bài dự án khép module. Nhận một máy có dịch vụ dữ liệu đang chạy sai theo nhiều cách cùng lúc, và nhiệm vụ là đưa nó về trạng thái khoẻ mạnh với bằng chứng cho từng bước. Ba loại vấn đề cài sẵn, mỗi loại thuộc một nhóm đã học: một vấn đề tài nguyên, một vấn đề cấu hình dịch vụ, và một vấn đề quyền hoặc kết nối. Yêu cầu nộp: dòng thời gian chẩn đoán ghi theo thứ tự thật gồm cả nhánh sai đã thử, bằng chứng số đo cho từng kết luận, thay đổi đã thực hiện, và cách xác nhận đã hồi phục. Chấm nặng phần lập luận: một chẩn đoán đúng do đoán trúng được ít điểm hơn một chẩn đoán có ba giả thuyết bị bác bỏ bằng bằng chứng, theo đúng kỷ luật đặt ở lesson 8. Cấm khởi động lại máy như bước đầu tiên, vì nó xoá mất bằng chứng.

**Outcome.** Đưa một máy có ba vấn đề về trạng thái khoẻ mạnh, mỗi kết luận dẫn được về số đo, và xác nhận được đã hồi phục.

**Đánh giá.** Tầng *phân tích*. Bài tổng hợp toàn module thành một buổi chẩn đoán thật. Kiểm bằng trạng thái cuối cộng rà soát dòng thời gian; đạt khi cả ba vấn đề được sửa và mỗi kết luận có số đo dẫn chứng.

**Lab.** Nhận máy có ba vấn đề cài sẵn, 90 phút. Chẩn đoán và sửa từng cái. Nộp dòng thời gian gồm cả nhánh sai, bằng chứng số đo, thay đổi đã làm, và cách xác nhận. Không được khởi động lại máy trước khi thu thập bằng chứng.

**Pitfalls.** Khởi động lại máy rồi mất bằng chứng · sửa nhiều thứ cùng lúc nên không biết cái nào có tác dụng · giấu nhánh sai · kết luận không kèm số đo.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Cả ba vấn đề được sửa và xác nhận hồi phục, mỗi kết luận dẫn được về số đo, và dòng thời gian có ghi nhánh sai đã thử.

# MODULE M6 · NETWORKING FROM PACKET TO API

**Phase 2 · Lessons 77–88 · 24 giờ**

| | |
|---|---|
| **Objective cấp module** | Theo được một yêu cầu qua phân giải tên, bắt tay, mã hoá, giao thức ứng dụng, proxy và cân bằng tải, rồi chẩn đoán độ trễ cùng hết giờ bằng gói tin và nhật ký |
| **Tiền đề** | M5 |
| **Exit criterion** | Vẽ được trình tự từ phân giải tên tới phản hồi và chỉ ra trạng thái cùng hạn chờ ở từng bước; từ một bản bắt gói phân biệt được truyền lại, đặt lại kết nối và lỗi ứng dụng |
| **Kỹ năng SFIA** | `NTAS` mức 4 · `SYSP` mức 3 |
| **Chế độ hỏng** | Gọi giao diện lập trình web mà không đặt hạn chờ và không giới hạn thử lại, rồi một nguồn chậm kéo sập cả pipeline |

Module này phục vụ trực tiếp M14B khi nạp dữ liệu từ giao diện lập trình web, và M16 cùng M21 khi chẩn đoán hệ phân tán. Trọng tâm không phải lý thuyết mạng mà là **đọc được bằng chứng**: gói tin, trạng thái socket, và nhật ký.

Ba con số sẽ dùng lại suốt phần sau: hạn chờ kết nối, hạn chờ đọc, và hạn chờ tổng. Không đặt đủ ba là để hệ có thể treo vô hạn.

### Lesson 77 · Layers, addresses and routing `LT`
**Prerequisites.** Module 6: M5

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Mô hình phân tầng dùng để định vị vấn đề chứ để học thuộc: khi có sự cố, câu hỏi đầu tiên là nó nằm ở tầng nào. Địa chỉ và khối địa chỉ: cách đọc ký hiệu tiền tố và tính được dải địa chỉ của một mạng con, kỹ năng dùng trực tiếp khi thiết kế mạng riêng ở M19. Bảng định tuyến và cổng ra: máy quyết định gửi gói đi đâu bằng cách so địa chỉ đích với bảng định tuyến, và đọc được bảng đó là trả lời được câu gói này đi đường nào. Phân giải địa chỉ vật lý trong mạng cục bộ ở mức nhận biết. Đơn vị truyền tối đa và phân mảnh: gói vượt kích thước tối đa bị chia hoặc bị loại, và triệu chứng của nó rất dễ nhầm với lỗi ứng dụng vì kết nối thành công nhưng truyền dữ liệu lớn thì treo. Chuyển đổi địa chỉ và tường lửa: hai thứ đứng giữa và làm thay đổi những gì bên kia nhìn thấy.

**Outcome.** Tính được dải địa chỉ của một mạng con và dự đoán đường đi của một gói trước khi kiểm chứng bằng lệnh.

**Đánh giá.** Tầng *áp dụng*. Bài mở module, kỹ năng tính toán cụ thể chuẩn bị cho M19. Kiểm bằng bài tính cộng dự đoán; đạt khi tính đúng ít nhất bốn trong năm mạng con và dự đoán đúng đường đi ở cả ba trường hợp.

**Lab.** Cho năm khối địa chỉ, tính dải địa chỉ dùng được và địa chỉ quảng bá cho từng cái. Đọc bảng định tuyến của máy mình. Với ba địa chỉ đích khác nhau, viết dự đoán gói đi qua cổng nào **trước khi** chạy lệnh tra đường, rồi đối chiếu.

**Pitfalls.** Học thuộc bảy tầng mà không dùng để định vị · tính nhầm số địa chỉ dùng được · bỏ qua đơn vị truyền tối đa nên không giải thích được lỗi treo khi truyền dữ liệu lớn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tính đúng ≥ 4/5 mạng con, và dự đoán đường đi khớp kết quả lệnh tra ở cả ba trường hợp.

### Lesson 78 · DNS - resolution, caching and stale records `TH`
**Prerequisites.** Lesson 77

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phân giải tên là bước đầu tiên của mọi kết nối và cũng là nguồn sự cố hay bị bỏ qua nhất vì nó thường hoạt động. Quá trình phân giải đệ quy và vai trò của máy chủ có thẩm quyền. Các loại bản ghi hay dùng và ý nghĩa vận hành của từng loại. Thời gian sống quyết định bộ đệm giữ kết quả bao lâu, và từ đó suy ra hai hệ quả quan trọng: đổi bản ghi không có hiệu lực ngay với mọi nơi, nên **kế hoạch chuyển đổi hạ tầng phải hạ thời gian sống trước nhiều giờ**; và một bản ghi cũ nằm trong bộ đệm có thể trỏ tới máy đã ngừng hoạt động. Ba tầng đệm hay quên: đệm của thư viện trong tiến trình, đệm của hệ điều hành, và đệm của máy chủ phân giải. Triệu chứng của bản ghi cũ và cách phân biệt với lỗi mạng: một số máy gọi được và một số không, đó là dấu hiệu đặc trưng.

**Outcome.** Chẩn đoán một sự cố do bản ghi cũ trong bộ đệm và phân biệt nó với lỗi kết nối thật.

**Đánh giá.** Tầng *phân tích*. Objective là nhận ra một loại sự cố có triệu chứng gây hiểu nhầm. Kiểm bằng hai tình huống trong đó một là bản ghi cũ; đạt khi phân biệt đúng và chỉ ra tầng đệm nào đang giữ bản ghi.

**Lab.** Dựng một tên miền thử trỏ tới một máy, gọi thành công, rồi đổi sang máy khác. Quan sát thời gian bản ghi cũ còn hiệu lực ở từng tầng đệm. Tạo tình huống một số tiến trình gọi được và một số không, rồi chẩn đoán. So thời gian sống đặt trước và sau khi hạ xuống.

**Pitfalls.** Bỏ qua bước phân giải tên khi chẩn đoán · đổi bản ghi rồi mong có hiệu lực ngay · quên đệm trong tiến trình · kết luận lỗi mạng khi thực ra là bản ghi cũ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân biệt đúng hai tình huống, chỉ ra đúng tầng đệm giữ bản ghi cũ, và có số đo thời gian hiệu lực ở từng tầng.

### Lesson 79 · TCP - handshake, retransmission and connection states `TH`
**Prerequisites.** Lesson 78

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Giao thức bảo đảm thứ tự và không mất dữ liệu, và mọi bảo đảm đó đều có cái giá quan sát được. Bắt tay ba bước và vì sao kết nối tốn ít nhất một vòng khứ hồi trước khi gửi được byte dữ liệu đầu tiên; từ đó suy ra vì sao mở lại kết nối cho mỗi yêu cầu là lãng phí và vì sao cần hồ kết nối. Số thứ tự và xác nhận, truyền lại khi mất gói, và vì sao truyền lại làm độ trễ tăng đột biến chứ tăng dần. Cửa sổ và kiểm soát luồng: bên nhận báo mình còn chứa được bao nhiêu, đây là áp lực ngược ở tầng mạng và cùng ý tưởng với hàng đợi có giới hạn ở lesson 30. Đóng kết nối và trạng thái chờ đóng: vì sao nó tồn tại và vì sao tích tụ nhiều gây cạn cổng tạm. Đặt lại kết nối khác hết giờ: một cái là bên kia chủ động từ chối, một cái là im lặng.

**Outcome.** Từ một bản bắt gói, phân biệt được truyền lại, đặt lại kết nối và lỗi ở tầng ứng dụng.

**Đánh giá.** Tầng *phân tích*. Objective là đọc bằng chứng thô, kỹ năng mà không đọc được thì mọi chẩn đoán mạng đều là phỏng đoán. Kiểm bằng ba bản bắt gói; đạt khi phân loại đúng ít nhất hai và chỉ ra được gói cụ thể làm bằng chứng.

**Lab.** Bắt gói cho ba tình huống: mạng mất gói mô phỏng, dịch vụ từ chối kết nối, và dịch vụ trả về lỗi ứng dụng. Với mỗi bản, chỉ ra gói nào là bằng chứng và phân loại. Đếm số socket ở trạng thái chờ đóng sau khi chạy 10.000 kết nối ngắn, rồi chạy lại với hồ kết nối và đếm lại.

**Pitfalls.** Nhầm đặt lại kết nối với hết giờ · mở kết nối mới cho mỗi yêu cầu · bỏ qua trạng thái chờ đóng tới khi cạn cổng · kết luận từ nhật ký ứng dụng mà không bắt gói.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân loại đúng ≥ 2/3 bản bắt gói kèm gói làm bằng chứng, và số socket chờ đóng giảm rõ rệt khi dùng hồ kết nối.

### Lesson 80 · TLS - certificates, verification and the handshake cost `TH`
**Prerequisites.** Lesson 79

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Lớp mã hoá thêm hai thứ vào mọi kết nối: chi phí bắt tay và một tập lỗi mới. Chuỗi chứng chỉ và xác minh: máy khách kiểm chứng chỉ có do một gốc tin cậy ký không, còn hạn không, và **tên miền có khớp không**; bỏ qua bước cuối là lỗ hổng chứ tiện lợi. Bắt tay tốn thêm vòng khứ hồi, sau đó chuyển sang mã hoá đối xứng rẻ hơn nhiều; nên chi phí nằm ở lúc mở kết nối và đây là lý do nữa để dùng hồ kết nối. Ba lỗi hay gặp và cách phân biệt: chứng chỉ hết hạn, tên miền không khớp, và thiếu chứng chỉ trung gian; lỗi thứ ba đặc biệt khó vì trình duyệt thường tự vá được còn thư viện thì không, nên chạy được trên trình duyệt mà hỏng trong mã. Xác thực hai chiều ở mức nhận biết. Ba cách tắt xác minh và vì sao cả ba đều không được xuất hiện trong mã sản xuất.

**Outcome.** Chẩn đoán ba loại lỗi chứng chỉ bằng công cụ dòng lệnh và giải thích vì sao trình duyệt chạy được mà thư viện thì không.

**Đánh giá.** Tầng *phân tích*. Objective là phân biệt ba lỗi có cùng thông báo mơ hồ. Kiểm bằng ba tình huống; đạt khi phân loại đúng cả ba và giải thích đúng trường hợp thiếu chứng chỉ trung gian.

**Lab.** Dựng ba tình huống lỗi chứng chỉ. Với mỗi cái, dùng công cụ dòng lệnh xem chuỗi chứng chỉ và xác định nguyên nhân. Với trường hợp thiếu chứng chỉ trung gian, chứng minh trình duyệt gọi được còn thư viện thì lỗi. Đo chi phí bắt tay bằng cách so thời gian yêu cầu đầu với yêu cầu sau trên cùng kết nối.

**Pitfalls.** Tắt xác minh chứng chỉ để hết lỗi · kết luận từ thông báo lỗi của thư viện mà không xem chuỗi chứng chỉ · quên chứng chỉ trung gian · đo chi phí bắt tay trên kết nối đã mở sẵn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân loại đúng cả ba lỗi chứng chỉ, giải thích đúng trường hợp thiếu chứng chỉ trung gian, và có số đo chi phí bắt tay.

### Lesson 81 · HTTP semantics - methods, status, idempotency and caching `LT`
**Prerequisites.** Lesson 80

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Giao thức ứng dụng phổ biến nhất, và phần quan trọng với người làm dữ liệu là ngữ nghĩa chứ cú pháp. Phương thức và hai tính chất tách bạch: an toàn nghĩa là không đổi trạng thái, bất biến nghĩa là gọi lại cho cùng kết quả; **bất biến là tính chất quyết định có được thử lại hay không**, và đây là cầu nối trực tiếp tới lesson 30. Mã trạng thái theo nhóm và cách xử lý từng nhóm khi nạp dữ liệu: nhóm lỗi máy khách thường không nên thử lại, nhóm lỗi máy chủ thì nên, và mã báo quá nhiều yêu cầu cần chờ theo tiêu đề máy chủ trả về. Tiêu đề quan trọng với việc nạp dữ liệu: nén, kiểu nội dung, phân trang, và giới hạn tốc độ. Bộ đệm và các tiêu đề điều khiển. Giữ kết nối sống và ghép nhiều yêu cầu trên một kết nối, nối lại chi phí bắt tay ở lesson 79 và 80.

**Outcome.** Quyết định một yêu cầu thất bại có được thử lại hay không dựa trên phương thức và mã trạng thái.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết chuẩn bị cho lesson 83 và cho M14B; chưa đòi cài đặt. Kiểm bằng bảng quyết định trên mười tổ hợp; đạt khi đúng ít nhất tám và giải thích được bằng tính bất biến chứ bằng thói quen.

**Lab.** Cho mười tổ hợp phương thức và mã trạng thái. Với mỗi tổ hợp, quyết định có thử lại không và giải thích bằng tính bất biến cùng ngữ nghĩa mã trạng thái. Gọi một giao diện thật có giới hạn tốc độ và đọc tiêu đề cho biết phải chờ bao lâu.

**Pitfalls.** Thử lại mọi lỗi · thử lại một yêu cầu tạo tài nguyên mà không có khoá bất biến · bỏ qua tiêu đề chờ của giới hạn tốc độ · nhầm an toàn với bất biến.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Quyết định đúng ≥ 8/10 tổ hợp kèm giải thích bằng tính bất biến, và đọc đúng tiêu đề chờ từ giao diện thật.

### Lesson 82 · Proxies, load balancers and what they hide `LT`
**Prerequisites.** Lesson 81

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Giữa máy khách và máy chủ hiếm khi chỉ có một chặng, và mỗi thứ đứng giữa đều thêm trạng thái cùng hạn chờ riêng. Phân biệt proxy chuyển tiếp với proxy đảo: một cái đại diện cho máy khách, một cái đại diện cho máy chủ. Cân bằng tải ở tầng bốn và tầng bảy: tầng bốn chỉ nhìn địa chỉ và cổng nên nhanh và không hiểu giao thức; tầng bảy đọc được nội dung nên định tuyến theo đường dẫn được nhưng tốn hơn. Kiểm tra sức khoẻ và khác biệt giữa kiểm tiến trình còn sống với kiểm dịch vụ còn phục vụ được, một khác biệt sẽ gặp lại ở M20. Phiên dính và vì sao nó làm việc mở rộng khó. Ba thứ lớp trung gian che mất và gây chẩn đoán sai: địa chỉ thật của máy khách, lỗi thật của máy chủ gốc, và hạn chờ của chính nó thường ngắn hơn hạn chờ của ứng dụng nên cắt kết nối trước. Mạng phân phối nội dung ở mức nhận biết.

**Outcome.** Chỉ ra trong một kiến trúc có lớp trung gian chỗ nào có thể cắt kết nối trước ứng dụng, và nêu cách xác minh.

**Đánh giá.** Tầng *hiểu*. Objective là nhận ra nguồn gây nhầm lẫn khi chẩn đoán qua nhiều chặng. Kiểm bằng ba kiến trúc; đạt khi chỉ đúng ít nhất hai chặng có hạn chờ riêng và nêu đúng cách xác minh.

**Lab.** Dựng một proxy đảo đứng trước hai bản sao dịch vụ. Đặt hạn chờ của proxy ngắn hơn thời gian xử lý của dịch vụ và quan sát máy khách nhận lỗi gì. Tắt một bản sao và quan sát kiểm tra sức khoẻ loại nó ra. Thử kiểm tra sức khoẻ chỉ kiểm tiến trình còn sống trong khi dịch vụ đã mất kết nối cơ sở dữ liệu.

**Pitfalls.** Nghĩ lỗi đến từ ứng dụng trong khi proxy cắt trước · dùng kiểm tra sức khoẻ chỉ kiểm tiến trình · bật phiên dính mà không cần · quên rằng lớp trung gian che địa chỉ máy khách thật.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chỉ đúng ≥ 2/3 chặng có hạn chờ riêng, và chứng minh được kiểm tra sức khoẻ sai loại không phát hiện dịch vụ đã hỏng.

### Lesson 83 · Timeout budgets, retries and connection pools `TH`
**Prerequisites.** Lesson 82

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài quan trọng nhất của module với người làm dữ liệu, vì nó quyết định pipeline có chịu được nguồn chậm hay không. Ba hạn chờ phải đặt riêng và đặt đủ: hạn mở kết nối, hạn chờ dữ liệu, và hạn tổng cho cả yêu cầu; thiếu hạn tổng thì một nguồn trả từng byte rất chậm sẽ giữ kết nối vô hạn. Ngân sách hạn chờ theo tầng: hạn của tầng ngoài phải lớn hơn tổng hạn của các tầng trong cộng với thời gian thử lại, nếu không thì tầng ngoài cắt trước và mọi thử lại bên trong thành vô ích. Khuếch đại thử lại: ba tầng mỗi tầng thử ba lần cho ra 27 lần gọi thật, nên **thử lại phải có ngân sách toàn tuyến chứ đặt độc lập từng tầng**. Lùi theo hàm mũ có nhiễu ngẫu nhiên, theo lesson 30. Hồ kết nối: kích thước hồ là một giới hạn đồng thời, và hồ cạn biểu hiện giống mạng chậm nên hay bị chẩn đoán nhầm.

**Outcome.** Đặt ngân sách hạn chờ nhất quán cho một tuyến ba tầng và chứng minh không có khuếch đại thử lại.

**Đánh giá.** Tầng *áp dụng*. Objective là một cấu hình có ràng buộc số học kiểm được bằng đếm lời gọi thật. Kiểm bằng thí nghiệm nguồn chậm; đạt khi tổng số lời gọi thật nằm trong ngân sách và không yêu cầu nào treo quá hạn tổng.

**Lab.** Dựng tuyến ba tầng gọi nhau. Đặt hạn chờ độc lập mỗi tầng thử ba lần, đếm số lời gọi thật tới tầng cuối khi nó lỗi. Đặt lại theo ngân sách toàn tuyến và đếm lại. Mô phỏng nguồn trả byte rất chậm và chứng minh hạn tổng cắt đúng lúc. Làm cạn hồ kết nối và ghi triệu chứng.

**Pitfalls.** Chỉ đặt một hạn chờ chung · để thử lại độc lập từng tầng · không có hạn tổng · chẩn đoán hồ cạn thành mạng chậm.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tổng lời gọi thật nằm trong ngân sách đã đặt, hạn tổng cắt đúng với nguồn trả chậm, và mô tả đúng triệu chứng hồ cạn.

### Lesson 84 · Designing an API client for data ingestion `TH`
**Prerequisites.** Lesson 83

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài ghép, và kết quả của nó được dùng lại nguyên vẹn ở M14B. Sáu yêu cầu của một trình gọi giao diện lập trình web dùng để nạp dữ liệu. Ba hạn chờ theo lesson 83. Thử lại có lùi và nhiễu, chỉ cho lỗi đáng thử lại theo lesson 81. Tôn trọng giới hạn tốc độ bằng cách đọc tiêu đề máy chủ trả về chứ đoán. Phân trang: ba kiểu phân trang và **vì sao phân trang theo số trang không an toàn khi dữ liệu đang thay đổi**, một chi tiết sẽ quay lại ở M14B. Khoá bất biến khi ghi để thử lại không sinh trùng. Và ghi nhật ký có mã theo dõi theo lesson 20 để truy ngược được. Kèm theo là một phần thường bị bỏ: lưu trạng thái đã nạp tới đâu để lần chạy sau tiếp tục được thay vì bắt đầu lại.

**Outcome.** Viết trình gọi đạt sáu yêu cầu và chứng minh nó nạp đủ, không trùng, dưới điều kiện nguồn lỗi và giới hạn tốc độ.

**Đánh giá.** Tầng *sáng tạo*. Objective đòi ghép sáu cơ chế thành một thành phần chịu lỗi. Kiểm bằng thí nghiệm nguồn xấu; đạt khi đối soát khớp tuyệt đối dưới cả ba điều kiện lỗi.

**Lab.** Dựng một máy chủ giả có phân trang, giới hạn tốc độ, lỗi ngẫu nhiên 10%, và chèn thêm bản ghi giữa lúc đang phân trang. Viết trình gọi đạt sáu yêu cầu. Nạp toàn bộ và đối soát số bản ghi với nguồn. Giết tiến trình giữa chừng và chứng minh lần chạy sau tiếp tục đúng chỗ.

**Pitfalls.** Phân trang theo số trang trên dữ liệu đang đổi · thử lại mà không có khoá bất biến · đoán thời gian chờ thay vì đọc tiêu đề · không lưu trạng thái nên chạy lại từ đầu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đối soát khớp tuyệt đối dưới cả ba điều kiện lỗi, và sau khi giết tiến trình thì lần chạy sau tiếp tục đúng chỗ.

### Lesson 85 · Building a TCP protocol with framing `TH`
**Prerequisites.** Lesson 84

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài này dạy một thứ mà dùng thư viện sẵn sẽ không bao giờ thấy: dòng byte không có ranh giới thông điệp. Giao thức bảo đảm thứ tự byte nhưng **không bảo đảm một lần đọc trả về đúng một thông điệp**; một lần đọc có thể trả về nửa thông điệp hoặc hai thông điệp rưỡi. Từ đó suy ra mọi giao thức trên nó đều phải tự đóng khung: theo độ dài đặt trước, theo ký tự phân tách, hoặc theo độ dài cố định. Đọc thiếu là lỗi kinh điển của người tự viết giao thức và biểu hiện là dữ liệu hỏng ngẫu nhiên khi tải cao. Ba tình huống hỏng phải xử lý: máy khách ngắt giữa chừng, máy khách gửi rất chậm, và máy khách gửi thông điệp lớn bất thường. Vì sao bài này quan trọng dù ít khi phải tự viết giao thức: nó giải thích vì sao thư viện có tham số kích thước bộ đệm và vì sao dữ liệu hỏng ở biên thông điệp.

**Outcome.** Cài một giao thức có đóng khung xử lý đúng ba tình huống hỏng, và tái hiện được lỗi do đọc thiếu.

**Đánh giá.** Tầng *áp dụng*. Objective là một cài đặt có ba ca biên kiểm được. Kiểm bằng ba phép thử hỏng; đạt khi cả ba được xử lý đúng và tái hiện được lỗi đọc thiếu ở bản chưa sửa.

**Lab.** Viết máy chủ lặp lại có đóng khung theo độ dài. Cố ý cài bản đọc thiếu và tái hiện dữ liệu hỏng khi tải cao. Sửa. Tiêm ba tình huống: ngắt giữa chừng, gửi rất chậm, và thông điệp vượt giới hạn. Chứng minh máy chủ xử lý đúng cả ba mà không treo và không cạn bộ nhớ.

**Pitfalls.** Giả định một lần đọc trả về đúng một thông điệp · không giới hạn kích thước thông điệp · treo vô hạn với máy khách gửi chậm · không đóng khung mà dựa vào kích thước gói.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba tình huống hỏng đều được xử lý đúng, và tái hiện được dữ liệu hỏng ở bản đọc thiếu.

### Lesson 86 · Diagnosing latency across the whole path `TH`
**Prerequisites.** Lesson 85

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài tổng hợp phần chẩn đoán. Một yêu cầu chậm có thể chậm ở sáu chặng và mỗi chặng có cách đo riêng: phân giải tên, mở kết nối, bắt tay mã hoá, gửi yêu cầu, chờ máy chủ xử lý, và nhận phản hồi. Công cụ dòng lệnh tách được thời gian theo từng chặng, và đây là bước đầu tiên nên làm thay vì đoán. Nguyên tắc: **đo phân vị cao chứ trung bình**, vì độ trễ hầu như luôn có đuôi dài và người dùng cảm nhận đuôi đó. Ba nguyên nhân chậm có triệu chứng giống nhau và cách phân biệt: mạng mất gói gây truyền lại, máy chủ xử lý chậm, và hồ kết nối cạn ở phía máy khách. Đo từ nhiều phía: chỉ đo ở máy khách thì không biết phần nào là mạng và phần nào là máy chủ, nên phải đối chiếu với nhật ký phía máy chủ qua mã theo dõi ở lesson 20.

**Outcome.** Phân rã độ trễ của một yêu cầu thành sáu chặng và chỉ ra chặng chiếm phần lớn thời gian.

**Đánh giá.** Tầng *phân tích*. Objective là phân rã một số đo tổng thành thành phần, kỹ năng dùng lại ở M21. Kiểm bằng ba tình huống chậm; đạt khi chỉ đúng chặng nút thắt ở ít nhất hai và dẫn được số đo của chặng đó.

**Lab.** Giảng viên tạo ba tình huống chậm ở ba chặng khác nhau. Với mỗi cái, đo tách theo chặng, báo phân vị 95, và chỉ ra chặng nút thắt. Đối chiếu số đo phía máy khách với nhật ký phía máy chủ qua mã theo dõi để tách phần mạng khỏi phần xử lý.

**Pitfalls.** Báo độ trễ trung bình · chỉ đo ở một phía · kết luận mạng chậm mà chưa bắt gói · bỏ qua chặng phân giải tên.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chỉ đúng chặng nút thắt ở ≥ 2/3 tình huống kèm số đo, và tách được phần mạng khỏi phần xử lý bằng đối chiếu hai phía.

### Lesson 87 · Rate limiting and backpressure between services `TH`
**Prerequisites.** Lesson 86

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hai mặt của cùng một vấn đề: bên gọi phải tự kiềm chế, và bên bị gọi phải tự bảo vệ. Giới hạn tốc độ ở phía máy chủ: ba thuật toán thường dùng và khác biệt về hành vi khi có đợt dồn. Phía máy khách: đọc tiêu đề giới hạn và tự điều tiết thay vì cứ gọi tới khi bị chặn, theo lesson 81. Áp lực ngược giữa các dịch vụ không có cơ chế tự động như trong một tiến trình, nên phải dựng bằng tay: hàng đợi có giới hạn, từ chối khi đầy, và báo cho bên gọi biết. Giảm tải chủ động: khi quá tải thì từ chối một phần để phần còn lại được phục vụ đúng, và tiêu chí chọn từ chối cái gì phải theo mức ưu tiên nghiệp vụ chứ ngẫu nhiên. Bộ ngắt mạch: ngừng gọi khi bên kia đang hỏng, để không lãng phí tài nguyên vào những lời gọi chắc chắn thất bại và để bên kia có cơ hội hồi phục. Ba cơ chế này sẽ gặp lại ở M21.

**Outcome.** Dựng giới hạn tốc độ và bộ ngắt mạch cho một tuyến, và chứng minh hệ suy giảm có kiểm soát khi quá tải.

**Đánh giá.** Tầng *áp dụng*. Objective là hai cơ chế phòng vệ kiểm được bằng thí nghiệm quá tải. Kiểm bằng phép thử tải gấp năm lần công suất; đạt khi phần ưu tiên cao vẫn được phục vụ và không thành phần nào cạn tài nguyên.

**Lab.** Dựng giới hạn tốc độ ở máy chủ và bộ ngắt mạch ở máy khách. Đẩy tải gấp năm lần công suất và đo tỉ lệ phục vụ của phần ưu tiên cao, có và không có giảm tải. Làm máy chủ hỏng hoàn toàn và chứng minh bộ ngắt mạch ngừng gọi thay vì tiếp tục thử.

**Pitfalls.** Không có giới hạn nên máy chủ sập · thử lại ngay khi bị từ chối · giảm tải ngẫu nhiên thay vì theo ưu tiên · bộ ngắt mạch không bao giờ đóng lại.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phần ưu tiên cao vẫn được phục vụ ở mức chấp nhận được khi quá tải, và bộ ngắt mạch ngừng gọi khi máy chủ hỏng hoàn toàn.

### Lesson 88 · Gate 2 - trace a request and diagnose the system `KT`
**Prerequisites.** Lesson 87

**In-class (120 phút).** 75 phút làm bài độc lập · 45 phút chữa bài và phân tích lỗi theo nhóm

**Learn.** Cổng của Phase 2. Bài kiểm ba năng lực: mô hình chi phí phần cứng ở M4, chẩn đoán hệ điều hành ở M5, và theo vết mạng ở M6. Không có nội dung mới.

**Outcome.** Chẩn đoán đúng ba sự cố thuộc ba tầng khác nhau, mỗi kết luận dẫn được về số đo hoặc gói tin làm bằng chứng.

**Đánh giá.** Tầng *phân tích*. Cổng đo năng lực chẩn đoán dưới áp lực thời gian, nên hình thức là buổi thực hành tính giờ chứ bài viết.

**Lab.** Buổi 120 phút: 75 phút làm bài độc lập, 45 phút chữa bài. Làm trên một hệ có ba sự cố cài sẵn ở ba tầng. Bài chấm sáu phần: A (20đ) phân loại đúng loại tải bằng chỉ số hệ thống · B (20đ) chẩn đoán sự cố mạng bằng bản bắt gói, chỉ đúng gói làm bằng chứng · C (20đ) giải thích một hiện tượng hiệu năng bằng mô hình chi phí, dẫn số đo của chính mình · D (15đ) sửa cả ba và xác nhận đã hồi phục · E (15đ) dòng thời gian chẩn đoán có ghi nhánh sai đã thử · F (10đ) báo cáo hiệu năng sáu phần cho một phép đo trong buổi.

**Pitfalls.** Khởi động lại hệ rồi mất bằng chứng · kết luận từ một chỉ số · đoán trúng mà không có bằng chứng · bỏ phần dòng thời gian vì hết giờ.

**Self-study (2,4 giờ).** Không có bài tự học. Nếu không đạt, theo phụ lục khắc phục khi không đạt cổng

**Done when.** Đạt ≥ 70/100, phần A và B đều ≥ 60%. Kết luận nào không dẫn được về số đo hoặc gói tin thì phần đó bằng không.

# MODULE M7 · SOFTWARE DESIGN AND DELIVERY

**Phase 3 · Lessons 89–100 · 24 giờ**

| | |
|---|---|
| **Objective cấp module** | Xây một kho mã đổi được mà không phá hợp đồng, có chiến lược kiểm thử theo tầng, và có đường phát hành cùng đường lùi đáng tin |
| **Tiền đề** | M1 · M2, cộng M5 và M6 ở mức nền |
| **Exit criterion** | Đồ thị phụ thuộc không có tầng nghiệp vụ phụ thuộc khung hay cơ sở dữ liệu; đổi một bộ chuyển đổi mà phép kiểm lõi không sửa một dòng |
| **Kỹ năng SFIA** | `PROG` mức 4 · `TEST` mức 4 · `CFMG` mức 3 |
| **Chế độ hỏng** | Áp nguyên tắc thiết kế như luật tuyệt đối, chia lớp thật nhiều rồi mã khó đọc hơn; hoặc kiểm thử mô phỏng cả thành phần bên trong nên đổi cấu trúc là phép kiểm đỏ |

Module này quyết định mã của cả chương trình còn sửa được sau sáu tháng hay không. Nó cũng là nơi đặt ranh giới mà mọi module dữ liệu sau đều dựa vào: lõi nghiệp vụ không biết gì về nơi dữ liệu đến và đi.

Nguyên tắc xuyên suốt: mọi nguyên tắc thiết kế ở đây là **công cụ chẩn đoán**, dùng để phát hiện mã đang khó đổi ở chỗ nào, không phải luật áp lên mọi dòng.

### Lesson 89 · From use case to contract and domain vocabulary `LT`
**Prerequisites.** Module 7: M2

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài nối lesson 1 với thiết kế mã: sau khi có phát biểu bài toán thì bước tiếp là đặt tên cho các khái niệm và cố định hợp đồng. Từ vựng miền: dùng đúng từ mà người nghiệp vụ dùng, một khái niệm một tên, và không dịch qua lại giữa hai bộ từ vựng trong cùng một kho mã; mỗi lần dịch là một chỗ có thể sai. Ca sử dụng và tiêu chí chấp nhận theo lesson 1, nay gắn với một tên hàm hoặc một điểm vào cụ thể. Hợp đồng gồm bốn phần: kiểu dữ liệu vào ra, điều kiện trước, điều kiện sau, và hợp đồng lỗi tức hàm này có thể thất bại theo những cách nào. Phần cuối hay bị bỏ và là phần gây nhiều sự cố nhất, vì người gọi không biết phải xử lý gì. Hợp đồng dữ liệu ở đây là hợp đồng trong mã; hợp đồng giữa hai đội ở tầng cao hơn sẽ học ở M14C và M14D.

**Outcome.** Viết hợp đồng bốn phần cho các điểm vào của một mô đun, với từ vựng khớp từ vựng nghiệp vụ.

**Đánh giá.** Tầng *áp dụng*. Bài mở module, nối kỹ năng phát biểu bài toán ở M1 với cấu trúc mã. Kiểm bằng rà soát chéo với người đóng vai nghiệp vụ; đạt khi mọi điểm vào có đủ bốn phần và không có khái niệm nào mang hai tên.

**Lab.** Cho mô tả nghiệp vụ một hệ đặt hàng. Rút từ vựng miền thành danh sách thuật ngữ có định nghĩa. Viết hợp đồng bốn phần cho năm điểm vào chính. Đổi bài: một học viên đóng vai người nghiệp vụ đọc và chỉ ra chỗ nào tên trong mã không khớp tên họ dùng.

**Pitfalls.** Bỏ hợp đồng lỗi · đặt tên kỹ thuật cho khái niệm nghiệp vụ · một khái niệm mang hai tên ở hai chỗ · viết điều kiện trước mà không kiểm ở đâu cả.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Năm điểm vào đều có đủ bốn phần, và người đóng vai nghiệp vụ không tìm được khái niệm nào mang hai tên.

### Lesson 90 · Cohesion, coupling and the direction of dependency `LT`
**Prerequisites.** Lesson 89

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Hai đại lượng quyết định mã có sửa được không, và chúng đo được chứ chỉ cảm nhận. Độ gắn kết: các thứ trong một mô đun có cùng lý do thay đổi không. Độ phụ thuộc: đổi mô đun này buộc đổi bao nhiêu mô đun khác. Chiều phụ thuộc là thứ quan trọng nhất và hay bị làm sai: **lõi nghiệp vụ không được phụ thuộc vào khung, cơ sở dữ liệu hay định dạng tệp**, mà ngược lại. Lý do không phải thẩm mỹ mà là khả năng kiểm thử và khả năng thay thế: lõi không biết gì về cơ sở dữ liệu thì kiểm thử lõi không cần cơ sở dữ liệu, và đổi cơ sở dữ liệu không đụng lõi. Đảo ngược phụ thuộc là kỹ thuật đạt điều đó: lõi định nghĩa giao diện nó cần, tầng ngoài cài đặt giao diện đó. Che giấu thông tin: mô đun lộ ra ít nhất có thể, vì mọi thứ lộ ra đều thành hợp đồng mà người khác dựa vào.

**Outcome.** Vẽ đồ thị phụ thuộc của một kho mã và chỉ ra mọi cạnh đi sai chiều.

**Đánh giá.** Tầng *phân tích*. Objective đòi đọc cấu trúc thật và đánh giá nó theo tiêu chí, chứ nhớ định nghĩa. Kiểm bằng bài phân tích hai kho mã; đạt khi vẽ đúng đồ thị và chỉ ra đủ các cạnh sai chiều ở kho có vấn đề.

**Lab.** Cho hai kho mã, một có lõi phụ thuộc cơ sở dữ liệu và một đã đảo ngược. Vẽ đồ thị phụ thuộc cho cả hai bằng cách đọc phần nhập mô đun. Chỉ ra cạnh sai chiều. Với kho có vấn đề, đếm số tệp phải sửa nếu đổi cơ sở dữ liệu; làm tương tự với kho kia và so hai con số.

**Pitfalls.** Chia lớp theo loại kỹ thuật thay vì theo lý do thay đổi · để lõi nhập thư viện cơ sở dữ liệu · lộ mọi thứ ra ngoài mô đun · đánh giá độ phụ thuộc bằng cảm nhận.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đồ thị phụ thuộc vẽ đúng cho cả hai kho, chỉ đủ cạnh sai chiều, và hai con số tệp phải sửa chênh nhau rõ rệt.

### Lesson 91 · Ports and adapters in practice `TH`
**Prerequisites.** Lesson 90

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài biến nguyên tắc ở lesson 90 thành cấu trúc thư mục cụ thể. Ba tầng và trách nhiệm: miền chứa quy tắc nghiệp vụ và không nhập gì từ bên ngoài; ứng dụng điều phối các ca sử dụng và định nghĩa cổng tức giao diện nó cần; bộ chuyển đổi cài đặt cổng bằng công nghệ cụ thể. Gốc kết nối là chỗ duy nhất biết cả ba và ghép chúng lại lúc khởi động. Phép thử thật của kiến trúc này không phải sơ đồ đẹp mà là **đổi bộ chuyển đổi mà phép kiểm lõi không sửa một dòng**; nếu phải sửa thì ranh giới đã rò rỉ. Ba dấu hiệu ranh giới rò rỉ: kiểu dữ liệu của thư viện cơ sở dữ liệu xuất hiện trong chữ ký hàm miền, lỗi của thư viện lọt ra ngoài chưa dịch, và cấu trúc bảng lộ nguyên vào tên thuộc tính miền. Cảnh báo về mức độ: kiến trúc này tốn công, và với một script một lần thì nó là thừa.

**Outcome.** Tái cấu trúc một script thành ba tầng, rồi đổi bộ chuyển đổi lưu trữ mà không sửa phép kiểm lõi.

**Đánh giá.** Tầng *áp dụng*. Objective là một phép biến đổi cấu trúc có tiêu chí nghiệm thu khách quan. Kiểm bằng phép thử đổi bộ chuyển đổi; đạt khi phép kiểm lõi không sửa dòng nào và vẫn xanh.

**Lab.** Tái cấu trúc công cụ nạp CSV ở lesson 32 thành ba tầng. Viết phép kiểm cho tầng miền không dùng tệp và không dùng cơ sở dữ liệu. Thay bộ chuyển đổi từ tệp sang PostgreSQL. Chứng minh phép kiểm lõi không sửa dòng nào. Đếm số tệp phải sửa cho lần thay đó.

**Pitfalls.** Cho kiểu dữ liệu của thư viện lọt vào tầng miền · gọi thẳng cơ sở dữ liệu từ miền · dựng ba tầng cho một script dùng một lần · để lỗi thư viện lan ra ngoài chưa dịch.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phép kiểm lõi không sửa dòng nào và vẫn xanh sau khi đổi bộ chuyển đổi, và tầng miền không nhập thư viện ngoài nào.

### Lesson 92 · Error design - expected failure against defect `TH`
**Prerequisites.** Lesson 91

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phân biệt quan trọng nhất trong thiết kế lỗi và cũng là phân biệt hay bị bỏ: thất bại dự kiến là phần của hợp đồng và người gọi phải xử lý; khiếm khuyết là lỗi lập trình và không nên bắt để chạy tiếp. Ví dụ với dữ liệu: tệp nguồn thiếu cột là thất bại dự kiến, còn chỉ số mảng vượt biên là khiếm khuyết. Hệ quả: bắt hết mọi ngoại lệ rồi ghi nhật ký và chạy tiếp là biến khiếm khuyết thành dữ liệu sai âm thầm. Phân loại thứ hai độc lập với phân loại trên và quyết định hành vi vận hành: lỗi thử lại được và lỗi vĩnh viễn, theo đúng phân loại ở lesson 30. Truyền ngữ cảnh: lỗi đi lên phải mang theo đủ thông tin để chẩn đoán mà không cần chạy lại, tức là dòng nào, tệp nào, giá trị nào. Dịch lỗi ở ranh giới theo lesson 15, nay đặt vào đúng tầng của kiến trúc ba tầng.

**Outcome.** Phân loại lỗi theo hai trục và cài đặt cách xử lý đúng cho từng ô, chứng minh bằng thí nghiệm tiêm lỗi.

**Đánh giá.** Tầng *áp dụng*. Objective là một thiết kế có bốn trường hợp kiểm được riêng. Kiểm bằng bốn loại lỗi tiêm; đạt khi cả bốn đi đúng đường và khiếm khuyết không bị nuốt.

**Lab.** Lập bảng hai trục cho mười lỗi có thể xảy ra trong pipeline nạp dữ liệu. Cài đặt xử lý cho từng ô. Tiêm bốn lỗi đại diện bốn ô và chứng minh đường đi đúng: thất bại dự kiến thử lại được thì thử lại, vĩnh viễn thì vào vùng cách ly, còn khiếm khuyết thì dừng và lộ ra.

**Pitfalls.** Bắt mọi ngoại lệ rồi chạy tiếp · thử lại một lỗi dữ liệu vĩnh viễn · để lỗi lên tới tầng trên mà mất ngữ cảnh · coi mọi lỗi là thất bại dự kiến.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng mười lỗi phân loại đủ hai trục, và bốn lỗi tiêm đều đi đúng đường với khiếm khuyết không bị nuốt.

### Lesson 93 · The test pyramid and where to place a double `TH`
**Prerequisites.** Lesson 92

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài này chi tiết hoá lesson 19 bằng câu hỏi đặt phép kiểm ở tầng nào. Hình tháp hay hình thoi: nhiều phép kiểm nhanh ở dưới, ít phép kiểm chậm ở trên; với mã dữ liệu thì tầng tích hợp thường dày hơn hình tháp kinh điển vì phần lớn lỗi nằm ở chỗ ghép với cơ sở dữ liệu và định dạng tệp. Quy tắc đặt bộ thay thế và đây là quy tắc quan trọng nhất của bài: **chỉ thay thế ở ranh giới mình không sở hữu**, tức hệ ngoài; thay thế thành phần bên trong là tự kiểm mã giả của mình và làm mọi lần tái cấu trúc thành phép kiểm đỏ. Bộ dựng dữ liệu kiểm thử để phép kiểm đọc được và không lặp. Tính xác định theo lesson 19. Phép kiểm đặc tả dùng khi tái cấu trúc mã cũ chưa có phép kiểm: ghi lại hành vi hiện tại làm mốc trước khi sửa, kể cả hành vi đó có vẻ sai.

**Outcome.** Đặt đúng tầng cho mười phép kiểm và chứng minh bộ kiểm không đỏ khi tái cấu trúc mà hành vi không đổi.

**Đánh giá.** Tầng *đánh giá*. Objective đòi phán đoán về vị trí và phạm vi phép kiểm, chỗ hay làm sai theo hướng tốn kém. Kiểm bằng phép thử tái cấu trúc; đạt khi bộ kiểm vẫn xanh sau khi đổi cấu trúc nội bộ mà không sửa phép kiểm nào.

**Lab.** Cho mười tình huống cần kiểm. Đặt mỗi cái vào một tầng và nêu có dùng bộ thay thế không, ở ranh giới nào. Cài đặt chúng. Sau đó tái cấu trúc nội bộ một mô đun mà giữ nguyên hành vi, và chứng minh không phép kiểm nào phải sửa.

**Pitfalls.** Thay thế thành phần bên trong · viết phép kiểm đầu cuối cho mọi thứ vì thấy chắc chắn hơn · bỏ tầng tích hợp vì chậm · tái cấu trúc mã cũ mà không có phép kiểm đặc tả.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mười phép kiểm đặt đúng tầng, và sau khi tái cấu trúc nội bộ thì bộ kiểm xanh mà không sửa phép kiểm nào.

### Lesson 94 · Contract testing between a producer and a consumer `TH`
**Prerequisites.** Lesson 93

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Khi hai thành phần do hai người hoặc hai đội viết, phép kiểm của mỗi bên không phát hiện được việc hai bên hiểu khác nhau về giao diện. Phép kiểm hợp đồng giải đúng chỗ đó: bên tiêu thụ khai báo nó cần gì, bên cung cấp chạy phép kiểm chứng minh nó đáp ứng, và hợp đồng đó nằm trong quy trình tích hợp liên tục của cả hai. Khác với phép kiểm đầu cuối: hợp đồng chạy nhanh, không cần dựng cả hệ, và chỉ ra chính xác trường nào không khớp. Thay đổi phá vỡ và thay đổi tương thích: thêm trường tuỳ chọn thì an toàn, xoá trường bắt buộc hoặc đổi kiểu thì không; đây là cùng bộ quy tắc sẽ gặp ở M14D khi nói về sổ đăng ký lược đồ. Quy trình đổi hợp đồng an toàn theo hai giai đoạn. Vì sao bài này quan trọng với người làm dữ liệu: mọi nguồn dữ liệu là một bên cung cấp, và không có hợp đồng thì họ đổi lược đồ lúc nào ta hỏng lúc đó.

**Outcome.** Dựng phép kiểm hợp đồng giữa hai thành phần và chứng minh nó bắt được thay đổi phá vỡ trước khi triển khai.

**Đánh giá.** Tầng *áp dụng*. Objective là một cơ chế kiểm được bằng thí nghiệm đổi lược đồ. Kiểm bằng ba thay đổi; đạt khi phép kiểm hợp đồng chặn đúng thay đổi phá vỡ và cho qua thay đổi tương thích.

**Lab.** Dựng một bên cung cấp và một bên tiêu thụ. Viết hợp đồng từ phía tiêu thụ và đưa vào quy trình của bên cung cấp. Thực hiện ba thay đổi: thêm trường tuỳ chọn, xoá trường bắt buộc, và đổi kiểu. Ghi lại phép kiểm hợp đồng phản ứng thế nào với từng cái. Thực hiện thay đổi phá vỡ theo quy trình hai giai đoạn mà không làm bên tiêu thụ lỗi.

**Pitfalls.** Dùng phép kiểm đầu cuối thay cho hợp đồng · viết hợp đồng từ phía cung cấp nên nó chỉ mô tả cái đang có · đổi lược đồ rồi mới báo bên tiêu thụ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phép kiểm hợp đồng chặn đúng thay đổi phá vỡ, cho qua thay đổi tương thích, và quy trình hai giai đoạn hoàn tất không gây lỗi.

### Lesson 95 · Refactoring in small behaviour-preserving steps `TH`
**Prerequisites.** Lesson 94

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Tái cấu trúc là đổi cấu trúc mà giữ nguyên hành vi, và hai chữ cuối là phần khó. Quy trình an toàn: có phép kiểm phủ hành vi hiện tại trước, đổi một bước nhỏ, chạy phép kiểm, nộp; lặp lại. Bước nhỏ nghĩa là mỗi lần đổi vẫn chạy được, chứ đập ra rồi dựng lại trong ba ngày. Với mã cũ chưa có phép kiểm thì dùng phép kiểm đặc tả ở lesson 93 để chốt hành vi hiện tại trước, kể cả hành vi có vẻ sai; sửa cái sai là một thay đổi riêng và phải nộp riêng. Các mẫu tái cấu trúc phổ biến dùng như công cụ chứ mục tiêu: **đưa vào một mẫu khi nó giải một sức ép có thật trong mã**, chứ vì mẫu đó nổi tiếng. Ba dấu hiệu mã cần tái cấu trúc và ba dấu hiệu đang tái cấu trúc quá đà. Cách tách tái cấu trúc khỏi sửa lỗi trong lịch sử Git để rà soát được, nối lại kỷ luật commit ở lesson 7.

**Outcome.** Tái cấu trúc một mô đun rối bằng các bước nhỏ, mỗi bước chạy được và có phép kiểm xanh.

**Đánh giá.** Tầng *áp dụng*. Objective đòi kỷ luật quy trình chứ kiến thức mới. Kiểm bằng lịch sử Git cộng bộ kiểm; đạt khi mọi commit đều chạy được và bộ kiểm xanh, và hành vi cuối giống hành vi đầu.

**Lab.** Nhận một mô đun 300 dòng không có phép kiểm. Viết phép kiểm đặc tả chốt hành vi hiện tại. Tái cấu trúc thành ba tầng theo lesson 91 bằng ít nhất sáu bước nhỏ, mỗi bước một commit chạy được. Chứng minh hành vi đầu ra không đổi trên cùng bộ dữ liệu.

**Pitfalls.** Đập ra viết lại từ đầu · trộn sửa lỗi vào commit tái cấu trúc · tái cấu trúc khi chưa có phép kiểm nào · đưa mẫu thiết kế vào vì thấy hay.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mọi commit đều chạy được với bộ kiểm xanh, và đầu ra trên bộ dữ liệu chuẩn khớp tuyệt đối với bản gốc.

### Lesson 96 · Static analysis, dependency and security scanning `TH`
**Prerequisites.** Lesson 95

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bốn loại kiểm tự động chạy trước khi mã tới tay người rà soát, để người rà soát dành thời gian cho phần máy không làm được. Định dạng tự động: chấm dứt tranh luận phong cách bằng một công cụ, không bàn nữa. Soát lỗi tĩnh: bắt lỗi thật như biến chưa dùng, so sánh luôn đúng, hoặc tài nguyên chưa đóng. Kiểm kiểu theo lesson 18. Quét phụ thuộc: thư viện có lỗ hổng đã công bố, và đây là loại rủi ro mà đội tự viết mã tốt vẫn dính. Quét bí mật cả lịch sử kho theo lesson 31. Ngưỡng chặn phải quyết trước chứ tuỳ hứng: mức nào chặn hợp nhất, mức nào chỉ cảnh báo; không đặt ngưỡng thì hoặc chặn mọi thứ rồi bị tắt, hoặc không chặn gì. Danh mục thành phần phần mềm ở mức nhận biết: biết mình đang chạy những thư viện nào là điều kiện để phản ứng khi có lỗ hổng mới công bố.

**Outcome.** Dựng bộ kiểm tự động bốn loại với ngưỡng chặn rõ, và chứng minh nó bắt được lỗi ở cả bốn loại.

**Đánh giá.** Tầng *áp dụng*. Objective là một cấu hình có tiêu chí nghiệm thu bằng phép thử tiêm. Kiểm bằng bốn vi phạm tiêm; đạt khi cả bốn bị chặn ở đúng bước và ngưỡng chặn được ghi lại thành tài liệu.

**Lab.** Thêm bốn loại kiểm vào quy trình ở lesson 31. Đặt ngưỡng chặn và ghi thành tài liệu ngắn. Tiêm bốn vi phạm: sai định dạng, một lỗi soát tĩnh thật, một thư viện có lỗ hổng đã biết, và một bí mật trong lịch sử. Chứng minh cả bốn bị chặn. Sinh danh mục thành phần và đọc nó.

**Pitfalls.** Bật mọi luật rồi bị tắt vì quá ồn · chỉ quét mã hiện tại · không đặt ngưỡng chặn · coi quét phụ thuộc là việc làm một lần.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn vi phạm đều bị chặn ở đúng bước, và tài liệu ngưỡng chặn nêu rõ mức nào chặn mức nào cảnh báo.

### Lesson 97 · Release - artifacts, versions and migration compatibility `TH`
**Prerequisites.** Lesson 96

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phát hành là chỗ mã gặp người dùng, và ba nguyên tắc quyết định nó có an toàn không. Sản phẩm dựng bất biến: dựng một lần, cùng một sản phẩm đó đi qua mọi môi trường; dựng lại cho từng môi trường là cách để môi trường sản xuất chạy thứ chưa ai kiểm. Đánh số phiên bản theo ngữ nghĩa và ý nghĩa với người dùng theo lesson 17. Tương thích khi di trú là phần khó nhất với hệ có dữ liệu: **mã mới phải chạy được với lược đồ cũ, và mã cũ phải chạy được với lược đồ mới**, ít nhất trong một cửa sổ, vì lúc triển khai thì hai phiên bản cùng chạy. Từ đó suy ra quy tắc đổi lược đồ hai giai đoạn: thêm trước, chuyển dữ liệu, đổi mã, rồi mới xoá cái cũ; gộp lại một bước là gây gián đoạn. Nhật ký thay đổi viết cho người dùng chứ chép lại danh sách commit.

**Outcome.** Thực hiện một thay đổi lược đồ phá vỡ theo quy trình hai giai đoạn mà không gây gián đoạn.

**Đánh giá.** Tầng *áp dụng*. Objective là một quy trình có tiêu chí nghiệm thu bằng việc dịch vụ không lỗi trong suốt quá trình. Kiểm bằng thí nghiệm triển khai có tải; đạt khi không yêu cầu nào thất bại và cả hai phiên bản cùng chạy được.

**Lab.** Dựng dịch vụ đọc ghi một bảng. Cần đổi tên một cột. Thực hiện theo hai giai đoạn trong lúc có tải liên tục: thêm cột mới, ghi cả hai, chuyển dữ liệu, đổi mã đọc, rồi xoá cột cũ. Ở mỗi bước, chạy đồng thời cả phiên bản cũ lẫn mới và đếm số yêu cầu thất bại.

**Pitfalls.** Đổi tên cột trong một bước · dựng lại sản phẩm cho từng môi trường · xoá cột cũ ngay sau khi đổi mã · viết nhật ký thay đổi bằng danh sách commit.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Không yêu cầu nào thất bại qua toàn bộ quá trình, và cả hai phiên bản cùng chạy được ở mọi bước trung gian.

### Lesson 98 · Deployment strategies and rollback `TH`
**Prerequisites.** Lesson 97

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bốn cách đưa phiên bản mới ra và đánh đổi của từng cách. Thay thế tại chỗ: đơn giản, có gián đoạn, lùi lại chậm. Xanh và lam: chạy song song hai môi trường rồi chuyển lưu lượng, lùi lại tức thì nhưng tốn gấp đôi tài nguyên. Phát hành dần: đưa phiên bản mới cho một phần nhỏ người dùng, quan sát chỉ số, rồi mở rộng; đây là cách an toàn nhất và cũng đòi khả năng quan sát tốt nhất. Cờ tính năng: tách việc triển khai mã khỏi việc bật tính năng, nên lùi một tính năng không cần triển khai lại. Điều kiện để mọi cách trên hoạt động với hệ có dữ liệu: tương thích hai chiều theo lesson 97, vì lùi mã mà lược đồ đã đổi một chiều thì không lùi được. **Lùi lại phải được diễn tập chứ chỉ viết trong tài liệu**, và bài lab này chính là buổi diễn tập đó.

**Outcome.** Chọn chiến lược triển khai cho một ràng buộc cho trước và diễn tập được một lần lùi thành công.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn theo ràng buộc tài nguyên và rủi ro, rồi chứng minh bằng diễn tập. Kiểm bằng bài chọn cộng diễn tập lùi; đạt khi chọn đúng ba tình huống và lùi hoàn tất trong hạn đã đặt.

**Lab.** Cho ba tình huống có ràng buộc khác nhau về tài nguyên, rủi ro và khả năng quan sát. Chọn chiến lược cho từng cái kèm lý do. Triển khai một phiên bản có lỗi bằng cách phát hành dần, phát hiện qua chỉ số, và lùi lại. Đo thời gian từ lúc triển khai tới lúc lùi xong.

**Pitfalls.** Chọn phát hành dần mà không có chỉ số để quan sát · lùi mã khi lược đồ đã đổi một chiều · chưa bao giờ diễn tập lùi · dùng cờ tính năng rồi không bao giờ dọn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chọn đúng chiến lược cho cả ba tình huống, và diễn tập lùi hoàn tất trong hạn với số đo thời gian.

### Lesson 99 · Monolith, modular monolith and the cost of splitting `LT`
**Prerequisites.** Lesson 98

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài chống lại một xu hướng tốn kém: chia nhỏ dịch vụ khi chưa cần. Ba dạng và điều kiện phù hợp. Khối đơn: một kho mã một sản phẩm triển khai, đơn giản nhất, và đủ cho phần lớn hệ dữ liệu ở quy mô vừa. Khối đơn có mô đun: vẫn một sản phẩm triển khai nhưng ranh giới mô đun được cưỡng chế, nên giữ được tính đơn giản vận hành mà vẫn sửa được; đây là lựa chọn mặc định đúng cho phần lớn đội. Nhiều dịch vụ: mỗi phần triển khai riêng, chia được theo đội và theo tải, đổi lại **thuế vận hành rất lớn** gồm mạng giữa các dịch vụ, dữ liệu phân tán, theo vết xuyên dịch vụ, và triển khai phối hợp. Ba điều kiện cần trước khi tách và ba dấu hiệu tách quá sớm. Sở hữu dữ liệu là ranh giới thật: hai dịch vụ cùng ghi một bảng thì chúng chưa thật sự tách.

**Outcome.** Quyết định có nên tách dịch vụ hay không cho một tình huống cho trước và nêu điều kiện kích hoạt việc tách sau này.

**Đánh giá.** Tầng *đánh giá*. Objective đòi cân chi phí vận hành với lợi ích tổ chức, chứ theo xu hướng. Kiểm bằng ba tình huống trong đó ít nhất hai không nên tách; đạt khi quyết định đúng cả ba và nêu điều kiện kích hoạt kiểm được.

**Lab.** Cho ba tình huống khác nhau về quy mô đội, tải và ranh giới nghiệp vụ. Quyết định dạng kiến trúc cho từng cái. Viết một tài liệu quyết định theo lesson 3 chọn khối đơn có mô đun cho một trong ba, nêu rõ ba điều kiện kích hoạt việc tách về sau.

**Pitfalls.** Tách dịch vụ vì nghe hiện đại · để hai dịch vụ cùng ghi một bảng rồi gọi là đã tách · bỏ qua thuế vận hành khi so · viết điều kiện kích hoạt chung chung.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Quyết định đúng cả ba tình huống, và tài liệu quyết định nêu được ba điều kiện kích hoạt kiểm được.

### Lesson 100 · Delivery project - a modular package with a release path `DA`
**Prerequisites.** Lesson 99

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Bài dự án khép module. Nâng công cụ ở lesson 32 thành một sản phẩm có kiến trúc và có đường phát hành. Danh mục kiểm tám điểm: ba tầng với đồ thị phụ thuộc không có cạnh sai chiều; hợp đồng bốn phần cho mọi điểm vào công khai; thiết kế lỗi hai trục; bộ kiểm đủ bốn tầng không mô phỏng thành phần bên trong; phép kiểm hợp đồng với một bên tiêu thụ; quy trình tự động bốn loại kiểm có ngưỡng chặn; sản phẩm dựng bất biến có đánh số phiên bản; và một lần di trú lược đồ hai giai đoạn đã diễn tập. Phép thử nghiệm thu gồm hai phần: đổi bộ chuyển đổi lưu trữ mà phép kiểm lõi không sửa dòng nào; và triển khai một phiên bản có lỗi rồi lùi lại trong hạn đã đặt. Nộp kèm một tài liệu quyết định cho lựa chọn kiến trúc, theo lesson 99.

**Outcome.** Nộp một sản phẩm đạt tám điểm danh mục kiểm và qua được hai phép thử nghiệm thu.

**Đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module thành một sản phẩm có kiến trúc và quy trình phát hành. Kiểm bằng hai phép thử cộng rà soát danh mục; đạt khi cả tám điểm có bằng chứng và cả hai phép thử qua.

**Lab.** Nâng công cụ thành sản phẩm đạt tám điểm. Nộp bảng danh mục kiểm, mỗi điểm dẫn tới tệp hoặc số đo. Thực hiện phép thử đổi bộ chuyển đổi và phép thử lùi. Nộp tài liệu quyết định kiến trúc.

**Pitfalls.** Dựng ba tầng cho phần không cần · mô phỏng thành phần bên trong nên phép kiểm đỏ khi tái cấu trúc · bỏ phép thử lùi vì tốn thời gian · dẫn bằng chứng chung chung.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Tám điểm đều dẫn được tới tệp hoặc số đo, đổi bộ chuyển đổi không sửa phép kiểm lõi, và lùi hoàn tất trong hạn.

# MODULE M8 · BACKEND AND API ENGINEERING

**Phase 3 · Lessons 101–112 · 24.6 giờ**

| | |
|---|---|
| **Objective cấp module** | Vận hành đúng một giao diện lập trình web có trạng thái dưới ràng buộc đồng thời, sự cố và bảo mật |
| **Tiền đề** | M5 · M6 · M7 |
| **Exit criterion** | Không sinh tác động kép khi máy khách thử lại trong hợp đồng đã định; bất biến giao dịch được kiểm bằng phép chạy song song; có mô hình mối đe doạ và sổ tay chẩn đoán |
| **Kỹ năng SFIA** | `PROG` mức 4 · `SYSP` mức 4 · `TEST` mức 4 |
| **Chế độ hỏng** | Xây giao diện chạy đúng khi gọi lần lượt rồi hỏng khi có hai máy khách gọi cùng lúc, vì ranh giới giao dịch và khoá bất biến chưa được thiết kế |

Module này là module cuối trước khi vào tầng dữ liệu, và nó là nơi người học lần đầu chịu trách nhiệm về một hệ có trạng thái dưới tải thật.

**Ghi chú về phụ thuộc.** Hợp đồng nguồn nêu module này cần SQL cơ bản và cho phép học song song phần đầu của M9. Ở đây SQL chỉ dùng ở mức đọc ghi và giao dịch; phần kế hoạch thực thi, chỉ mục và tối ưu thuộc M9 và M10, nên bài 95 chỉ dùng giao dịch chứ chưa đòi đọc kế hoạch.

Dự án của module là một giao diện điều khiển công việc, và nó được dùng lại làm nguồn dữ liệu cho pipeline tham chiếu từ M14B trở đi.

### Lesson 101 · The request lifecycle end to end `LT`
**Prerequisites.** Module 8: M7

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài mở module bằng cách nối mọi thứ đã học ở M5 và M6 thành một đường đi duy nhất: socket nhận kết nối, máy chủ phân luồng, bộ định tuyến chọn hàm xử lý, các lớp trung gian chạy trước và sau, hàm xử lý gọi tầng ứng dụng, tầng ứng dụng gọi kho dữ liệu, rồi phản hồi đi ngược lại. Mỗi chặng có một hạn chờ và một chỗ có thể hỏng, và vẽ được đường này là điều kiện để chẩn đoán về sau. Ba mô hình xử lý đồng thời của máy chủ và hệ quả: một tiến trình nhiều luồng, nhiều tiến trình, và vòng lặp sự kiện; chọn theo đúng quy tắc ở lesson 29. Lớp trung gian làm gì và thứ tự chạy của chúng quan trọng ra sao, đặc biệt lớp ghi nhật ký và lớp xác thực. Điểm kiểm sức khoẻ và điểm kiểm sẵn sàng là hai thứ khác nhau, theo phân biệt đã nêu ở lesson 82.

**Outcome.** Vẽ đường đi của một yêu cầu qua bảy chặng và chỉ ra hạn chờ cùng chế độ hỏng của từng chặng.

**Đánh giá.** Tầng *hiểu*. Bài mở module, tổng hợp kiến thức đã có thành một bản đồ. Kiểm bằng bài vẽ có chú thích; đạt khi đủ bảy chặng, mỗi chặng có hạn chờ và ít nhất một chế độ hỏng.

**Lab.** Dựng một dịch vụ tối thiểu có lớp trung gian ghi nhật ký. Gửi một yêu cầu và ghi lại dấu thời gian ở từng chặng bằng nhật ký có mã theo dõi. Vẽ đường đi có chú thích hạn chờ và chế độ hỏng. Phân biệt điểm kiểm sức khoẻ với điểm kiểm sẵn sàng bằng cách ngắt kết nối cơ sở dữ liệu và xem cái nào đổi trạng thái.

**Pitfalls.** Vẽ sơ đồ mà bỏ qua lớp trung gian · dùng một điểm kiểm cho cả hai mục đích · không đặt hạn chờ ở chặng gọi cơ sở dữ liệu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Sơ đồ đủ bảy chặng với hạn chờ và chế độ hỏng, và hai điểm kiểm phản ứng khác nhau khi mất kết nối cơ sở dữ liệu.

### Lesson 102 · API contract - resources, errors and versioning `TH`
**Prerequisites.** Lesson 101

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hợp đồng của giao diện là thứ người khác dựa vào, nên đổi nó là đổi thứ ngoài tầm kiểm soát của mình. Tài nguyên và đường dẫn: đặt tên theo danh từ nghiệp vụ, theo từ vựng miền ở lesson 89. Ngữ nghĩa phương thức và tính bất biến theo lesson 81, nay là quyết định thiết kế chứ chỉ kiến thức. Xác thực đầu vào ở ranh giới theo lesson 18, và trả lỗi nêu rõ trường nào sai chứ một thông báo chung. Phong bì lỗi thống nhất: mã lỗi ổn định cho máy đọc, thông điệp cho người đọc, và mã theo dõi để đối chiếu nhật ký. Phân trang, lọc và sắp xếp: ba kiểu phân trang và vì sao phân trang theo con trỏ an toàn hơn theo số trang khi dữ liệu đang đổi, nối lại lesson 84. Đánh phiên bản: ba cách và đánh đổi; nguyên tắc chung là **thêm thì được, bớt và đổi kiểu thì cần phiên bản mới**, cùng bộ quy tắc với lesson 94.

**Outcome.** Thiết kế hợp đồng cho một tài nguyên có phân trang và phong bì lỗi thống nhất, và chứng minh hợp đồng ổn định khi thêm trường.

**Đánh giá.** Tầng *áp dụng*. Objective là một thiết kế có tiêu chí nghiệm thu bằng phép kiểm hợp đồng ở lesson 94. Kiểm bằng ba thay đổi hợp đồng; đạt khi thêm trường không làm bên tiêu thụ lỗi và hai thay đổi phá vỡ bị phép kiểm chặn.

**Lab.** Thiết kế và cài giao diện cho tài nguyên công việc: tạo, xem, liệt kê có phân trang theo con trỏ, và huỷ. Viết đặc tả giao diện. Dựng phép kiểm hợp đồng từ phía một máy khách. Thực hiện ba thay đổi và ghi phản ứng của phép kiểm. Chèn bản ghi mới giữa lúc phân trang và chứng minh không trùng không sót.

**Pitfalls.** Phân trang theo số trang · phong bì lỗi mỗi chỗ một kiểu · trả mã trạng thái chung cho mọi lỗi · đổi kiểu một trường mà giữ nguyên phiên bản.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân trang theo con trỏ không trùng không sót khi dữ liệu đổi, và ba thay đổi hợp đồng cho phản ứng đúng như thiết kế.

### Lesson 103 · Transaction boundaries and the unit of work `TH`
**Prerequisites.** Lesson 102

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ranh giới giao dịch là quyết định thiết kế chứ chi tiết cài đặt, và đặt sai là nguồn của dữ liệu không nhất quán. Nguyên tắc: **một ca sử dụng là một giao dịch**, mở ở tầng ứng dụng chứ ở tầng kho dữ liệu, vì tầng kho không biết ca sử dụng gồm mấy thao tác. Ba lỗi hay gặp: mỗi thao tác một giao dịch nên nửa chừng lỗi thì dữ liệu dở dang; giữ giao dịch mở trong lúc gọi hệ ngoài nên khoá bị giữ rất lâu; và gọi hệ ngoài bên trong giao dịch rồi giao dịch lùi mà tác động bên ngoài không lùi được. Lỗi thứ ba là bài toán hai hệ và lời giải của nó là mẫu hộp thư đi, đặt ở lesson 109. Hồ kết nối và quan hệ với ranh giới giao dịch: giao dịch giữ một kết nối, nên giao dịch dài làm cạn hồ, và triệu chứng là yêu cầu xếp hàng chờ kết nối chứ chờ cơ sở dữ liệu. Vấn đề truy vấn lặp và cách phát hiện bằng đếm số truy vấn cho mỗi yêu cầu.

**Outcome.** Đặt đúng ranh giới giao dịch cho ba ca sử dụng và chứng minh không còn trạng thái dở dang khi lỗi giữa chừng.

**Đánh giá.** Tầng *áp dụng*. Objective là một quyết định thiết kế kiểm được bằng thí nghiệm lỗi giữa chừng. Kiểm bằng ba ca sử dụng có tiêm lỗi; đạt khi không ca nào để lại trạng thái dở dang và số truy vấn cho mỗi yêu cầu nằm trong ngưỡng.

**Lab.** Cài ba ca sử dụng, mỗi cái ghi nhiều bảng. Tiêm lỗi ở giữa và đối soát để chứng minh không dở dang. Đếm số truy vấn cho mỗi yêu cầu và phát hiện truy vấn lặp, rồi sửa. Giữ một giao dịch mở trong lúc gọi hệ ngoài chậm và quan sát hồ kết nối cạn.

**Pitfalls.** Mở giao dịch ở tầng kho dữ liệu · gọi hệ ngoài trong giao dịch · giữ giao dịch qua nhiều bước chờ người dùng · không đếm số truy vấn mỗi yêu cầu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba ca sử dụng không để lại trạng thái dở dang khi lỗi, số truy vấn mỗi yêu cầu trong ngưỡng, và tái hiện được hồ kết nối cạn.

### Lesson 104 · Concurrency control - optimistic and pessimistic `TH`
**Prerequisites.** Lesson 103

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hai máy khách cùng sửa một bản ghi là tình huống bình thường, và không xử lý thì một bản cập nhật biến mất mà không ai biết. Cập nhật mất là chế độ hỏng cụ thể: cả hai đọc giá trị cũ, cả hai ghi, bản ghi sau đè bản trước. Hai cách chống và điều kiện dùng. Khoá lạc quan: mỗi bản ghi có số phiên bản, khi ghi thì kiểm phiên bản còn như lúc đọc không, khác thì từ chối và báo máy khách thử lại; hợp khi xung đột hiếm. Khoá bi quan: khoá bản ghi lúc đọc, giữ tới khi ghi xong; hợp khi xung đột nhiều, đổi lại giảm đồng thời và có nguy cơ khoá chết theo lesson 70. Mức cô lập giao dịch ở mức đủ dùng, phần chi tiết thuộc M10. Cách kiểm thử: phép kiểm tuần tự **không bao giờ** phát hiện được lỗi loại này, nên bắt buộc phải có phép kiểm chạy song song thật.

**Outcome.** Chống được cập nhật mất bằng một trong hai cơ chế và chứng minh bằng phép kiểm chạy song song.

**Đánh giá.** Tầng *áp dụng*. Objective là một cơ chế chỉ kiểm được bằng phép chạy song song, điểm mà phép kiểm thông thường bỏ sót. Kiểm bằng 1000 lần ghi đồng thời; đạt khi không có cập nhật nào bị mất và số lần từ chối khớp số xung đột thật.

**Lab.** Cài một điểm cập nhật không có kiểm soát đồng thời. Viết phép kiểm chạy 50 luồng cùng cập nhật và chứng minh có cập nhật bị mất. Cài khoá lạc quan và chạy lại. Cài khoá bi quan và chạy lại. So thông lượng hai cách ở hai mức tỉ lệ xung đột khác nhau.

**Pitfalls.** Chỉ kiểm tuần tự rồi kết luận đúng · dùng khoá bi quan cho mọi thứ · trả lỗi xung đột mà không nói máy khách phải làm gì · giữ khoá qua nhiều yêu cầu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bản chưa sửa mất cập nhật có số chứng minh, cả hai cơ chế đều cho 0 cập nhật mất qua 1000 lần, và có bảng so thông lượng.

### Lesson 105 · Idempotency keys and deduplication state `TH`
**Prerequisites.** Lesson 104

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Máy khách thử lại là chuyện chắc chắn xảy ra theo lesson 83, nên giao diện phải định nghĩa rõ thử lại nghĩa là gì. Khoá bất biến: máy khách sinh một khoá cho mỗi ý định, gửi kèm; máy chủ lưu khoá cùng kết quả, và lần gọi lại với cùng khoá thì trả lại kết quả cũ thay vì làm lại. Ba chi tiết quyết định đúng sai. Một là **lưu khoá và thực hiện tác động phải nằm trong cùng một giao dịch**, nếu không thì có khe hở giữa hai bước; đây là ứng dụng trực tiếp của lesson 103. Hai là thời gian giữ khoá và điều gì xảy ra sau khi hết hạn. Ba là hành vi khi hai yêu cầu cùng khoá tới đồng thời chứ nối tiếp: bản sau phải chờ hoặc bị từ chối, chứ tạo hai bản ghi. Hợp đồng phải ghi rõ trong tài liệu để máy khách biết mình được thử lại trong điều kiện nào và trong bao lâu.

**Outcome.** Cài khoá bất biến đúng cả ba chi tiết và chứng minh không sinh tác động kép kể cả khi hai yêu cầu cùng khoá tới đồng thời.

**Đánh giá.** Tầng *sáng tạo*. Objective đòi ghép giao dịch, lưu trạng thái và xử lý đồng thời thành một cơ chế mà thư viện không cho sẵn. Kiểm bằng ba thí nghiệm; đạt khi cả ba đều không sinh tác động kép.

**Lab.** Cài khoá bất biến cho điểm tạo công việc. Ba thí nghiệm: gọi lại cùng khoá sau khi thành công, gọi lại sau khi máy chủ chết giữa chừng, và gọi hai yêu cầu cùng khoá đồng thời. Với mỗi thí nghiệm, đếm số công việc thật được tạo. Viết phần hợp đồng mô tả điều kiện và thời hạn thử lại.

**Pitfalls.** Lưu khoá ngoài giao dịch · để hai yêu cầu cùng khoá cùng đi qua · không nêu thời hạn trong hợp đồng · dùng dấu thời gian làm khoá bất biến.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Cả ba thí nghiệm đều tạo đúng một công việc, và hợp đồng nêu rõ điều kiện cùng thời hạn thử lại.

### Lesson 106 · Authentication, authorization and ownership checks `TH`
**Prerequisites.** Lesson 105

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hai việc khác nhau hay bị gộp: xác thực trả lời bạn là ai, uỷ quyền trả lời bạn được làm gì. Ba cách xác thực và đánh đổi: phiên lưu phía máy chủ, thẻ mang theo, và chuẩn uỷ quyền mở ở mức khái niệm. Giới hạn của thẻ tự chứa: nó không thu hồi được trước khi hết hạn, nên thời hạn phải ngắn và phải có cơ chế làm mới; đây là chi tiết hay bị bỏ và gây rủi ro thật. Uỷ quyền theo vai và kiểm quyền sở hữu là hai tầng phải có cả hai: có vai đọc công việc không có nghĩa được đọc công việc **của người khác**; thiếu tầng thứ hai là lỗ hổng phổ biến nhất trong giao diện tự viết. Nguyên tắc kiểm ở đâu: kiểm ở tầng ứng dụng chứ ở hàm xử lý, để mọi đường vào đều đi qua. Phép thử phủ định bắt buộc: với mỗi điểm vào, viết một phép kiểm chứng minh người không có quyền bị từ chối.

**Outcome.** Cài hai tầng uỷ quyền và chứng minh bằng phép thử phủ định rằng người dùng không truy cập được tài nguyên của người khác.

**Đánh giá.** Tầng *áp dụng*. Objective là một cơ chế bảo mật kiểm được bằng phép thử phủ định, chứ bằng việc đường đi thuận chạy được. Kiểm bằng phép thử phủ định cho mọi điểm vào; đạt khi mọi truy cập trái phép bị từ chối và có ghi nhật ký.

**Lab.** Cài xác thực bằng thẻ có thời hạn ngắn và cơ chế làm mới. Cài kiểm vai và kiểm quyền sở hữu. Với mỗi điểm vào, viết phép thử phủ định. Thử truy cập tài nguyên của người khác bằng thẻ hợp lệ và chứng minh bị từ chối. Thu hồi quyền một người dùng và đo bao lâu thẻ cũ còn dùng được.

**Pitfalls.** Chỉ kiểm vai mà quên kiểm quyền sở hữu · đặt thời hạn thẻ rất dài cho tiện · kiểm quyền trong từng hàm xử lý nên sót đường vào · không viết phép thử phủ định.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mọi điểm vào có phép thử phủ định và đều từ chối đúng, và đo được khoảng thời gian thẻ cũ còn hiệu lực sau khi thu hồi.

### Lesson 107 · Resilience - timeouts, circuit breakers and bulkheads `TH`
**Prerequisites.** Lesson 106

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài áp các cơ chế đã học ở lesson 83 và 87 vào một dịch vụ có trạng thái. Hạn chờ ở mọi lời gọi ra ngoài, gồm cả lời gọi tới cơ sở dữ liệu, vì cơ sở dữ liệu chậm là nguyên nhân sập dịch vụ phổ biến hơn mạng chậm. Thử lại có giới hạn và chỉ cho thao tác bất biến theo lesson 105. Bộ ngắt mạch bảo vệ bản thân khỏi việc lãng phí tài nguyên vào lời gọi chắc chắn thất bại. Vách ngăn là cơ chế ít được dùng nhưng rất hiệu quả: chia hồ tài nguyên theo loại việc, để một loại việc chậm không chiếm hết hồ kết nối và làm chết mọi loại còn lại; với dịch vụ dữ liệu thì tách hồ cho truy vấn nhanh và truy vấn nặng là cách đơn giản nhất. Giảm tải và hàng đợi có giới hạn theo lesson 87. Thứ tự áp dụng: đặt hạn chờ trước, rồi mới tới các cơ chế còn lại, vì không có hạn chờ thì mọi cơ chế khác vô nghĩa.

**Outcome.** Dựng bốn cơ chế chịu lỗi và chứng minh dịch vụ suy giảm có kiểm soát khi phụ thuộc hạ nguồn hỏng.

**Đánh giá.** Tầng *áp dụng*. Objective là một tập cấu hình kiểm được bằng thí nghiệm hỏng hạ nguồn. Kiểm bằng ba kịch bản hỏng; đạt khi dịch vụ vẫn phục vụ phần không phụ thuộc và không cạn hồ kết nối.

**Lab.** Dựng bốn cơ chế. Ba kịch bản: cơ sở dữ liệu chậm gấp mười lần, một phụ thuộc ngoài chết hoàn toàn, và tải gấp năm lần công suất. Với mỗi kịch bản, đo tỉ lệ phục vụ của các điểm vào không phụ thuộc phần hỏng, và kiểm hồ kết nối có cạn không. Thêm vách ngăn tách hồ và đo lại.

**Pitfalls.** Không đặt hạn chờ cho lời gọi cơ sở dữ liệu · dùng chung một hồ cho mọi loại truy vấn · thử lại thao tác không bất biến · bộ ngắt mạch không bao giờ đóng lại.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba kịch bản hỏng đều giữ được tỉ lệ phục vụ của phần không phụ thuộc, và vách ngăn ngăn được hồ kết nối cạn có số chứng minh.

### Lesson 108 · Observability for an API - RED metrics and tracing `TH`
**Prerequisites.** Lesson 107

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba chỉ số tối thiểu cho mọi điểm vào: tốc độ yêu cầu, tỉ lệ lỗi, và phân bố thời gian xử lý. Báo phân vị chứ trung bình theo lesson 59 và 86. Chia theo điểm vào và theo mã trạng thái, vì tổng gộp che mất một điểm vào đang hỏng. Nhật ký có cấu trúc kèm mã yêu cầu theo lesson 20, và mã đó phải truyền sang cả lời gọi hạ nguồn để nối được toàn tuyến. Theo vết phân tán ở mức dùng được: một mã theo dõi đi qua nhiều thành phần cho biết thời gian tiêu ở đâu, và đây là thứ duy nhất trả lời được câu chậm ở chặng nào khi có nhiều chặng. Điểm kiểm sức khoẻ và sẵn sàng theo lesson 101, nay gắn với hành vi thật: sẵn sàng phải kiểm được kết nối cơ sở dữ liệu, nếu không thì bộ cân bằng tải gửi lưu lượng tới một bản sao đã hỏng. Ba câu hỏi chẩn đoán mà bộ chỉ số phải trả lời được.

**Outcome.** Dựng bộ chỉ số và theo vết đủ để trả lời ba câu hỏi chẩn đoán mà không cần đọc mã.

**Đánh giá.** Tầng *áp dụng*. Objective đo bằng khả năng trả lời câu hỏi chứ bằng số lượng biểu đồ. Kiểm bằng ba câu hỏi chẩn đoán trong lúc có sự cố tiêm sẵn; đạt khi trả lời được ít nhất hai chỉ bằng bảng điều khiển và theo vết.

**Lab.** Gắn ba chỉ số chia theo điểm vào và mã trạng thái. Truyền mã yêu cầu xuống hạ nguồn. Dựng theo vết cho tuyến gọi ba chặng. Giảng viên tiêm một sự cố ở một chặng và đặt ba câu hỏi chẩn đoán; trả lời chỉ bằng bảng điều khiển và theo vết. Kiểm điểm sẵn sàng phản ứng đúng khi mất kết nối cơ sở dữ liệu.

**Pitfalls.** Báo thời gian xử lý trung bình · gộp mọi điểm vào vào một chỉ số · không truyền mã yêu cầu xuống hạ nguồn · để điểm sẵn sàng luôn trả về khoẻ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Trả lời được ≥ 2/3 câu hỏi chẩn đoán chỉ bằng bảng điều khiển và theo vết, và điểm sẵn sàng đổi trạng thái khi mất cơ sở dữ liệu.

### Lesson 109 · The outbox pattern - one atomic write `TH`
**Prerequisites.** Lesson 108

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài giải bài toán đã nêu ở lesson 103: ghi cơ sở dữ liệu rồi phát một sự kiện là hai thao tác trên hai hệ, nên chết giữa chừng làm hai bên lệch nhau và không có giao dịch nào bao được cả hai. Mẫu hộp thư đi biến hai thao tác thành một: ghi dữ liệu và ghi bản ghi sự kiện vào một bảng trong **cùng một giao dịch**, rồi một tiến trình riêng đọc bảng đó và phát đi. Vì chỉ còn một thao tác nguyên tử nên không có khe hở. Ba chi tiết cài đặt: đánh dấu đã phát thế nào để không phát lại vô hạn, xử lý khi phát thành công nhưng đánh dấu thất bại, và dọn bảng hộp thư để nó không phình. Bên nhận vẫn phải chịu được nhận trùng, vì mẫu này cho ít nhất một lần chứ đúng một lần. Ở M17, tiến trình đọc bảng hộp thư sẽ được thay bằng đọc thẳng nhật ký giao dịch; ở đây làm bản đơn giản trước.

**Outcome.** Cài mẫu hộp thư đi và chứng minh bằng thí nghiệm giết tiến trình rằng cơ sở dữ liệu và luồng sự kiện không lệch nhau.

**Đánh giá.** Tầng *sáng tạo*. Objective đòi ghép giao dịch với một tiến trình phát riêng thành một mẫu giải bài toán hai hệ. Kiểm bằng 20 lần giết tiến trình; đạt khi số sự kiện phát ra khớp số bản ghi tạo ra, không thiếu.

**Lab.** Cài bản ngây thơ ghi cơ sở dữ liệu rồi phát sự kiện, giết tiến trình giữa hai thao tác 20 lần và đếm mức lệch. Cài lại bằng hộp thư đi và lặp thí nghiệm. Xử lý trường hợp phát thành công nhưng đánh dấu thất bại. Thêm việc dọn bảng hộp thư theo lịch.

**Pitfalls.** Ghi hai hệ trong hai thao tác rời · dùng giao dịch phân tán khi hộp thư đi đủ · quên dọn bảng hộp thư · giả định bên nhận không bao giờ nhận trùng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bản ngây thơ có mức lệch đo được, bản hộp thư đi không thiếu sự kiện nào qua 20 lần giết, và bảng hộp thư được dọn tự động.

### Lesson 110 · Load testing and capacity notes `TH`
**Prerequisites.** Lesson 109

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Đo dịch vụ dưới tải là cách duy nhất biết nó chịu được bao nhiêu, và làm sai cách thì số đo vô nghĩa. Bốn đại lượng phải đo cùng nhau: thông lượng, thời gian xử lý ở ba phân vị, tỉ lệ lỗi, và mức bão hoà của tài nguyên nút thắt, thường là hồ kết nối. Chỉ đo thông lượng mà không đo tỉ lệ lỗi là cách báo cáo một con số đẹp trong khi dịch vụ đang từ chối phần lớn yêu cầu. Quy trình: tăng tải theo bậc, ở mỗi bậc chờ ổn định rồi mới đo, và tìm điểm mà thời gian xử lý bắt đầu tăng phi tuyến; điểm đó là công suất thật chứ điểm dịch vụ sập. Phân biệt ba loại phép thử: tải thường, tải đỉnh, và tải kéo dài để phát hiện rò rỉ. Ghi chú công suất viết ra thành tài liệu gồm công suất đo được, nút thắt, và ước lượng khi nào cần mở rộng; đây là đầu vào cho M22.

**Outcome.** Đo được công suất thật của dịch vụ và xác định đúng tài nguyên nút thắt bằng số đo.

**Đánh giá.** Tầng *phân tích*. Objective đòi đọc đường cong và định vị nút thắt chứ chỉ chạy công cụ tải. Kiểm bằng đường cong bốn đại lượng; đạt khi xác định đúng điểm công suất và chỉ đúng tài nguyên nút thắt.

**Lab.** Chạy tải tăng theo sáu bậc trên giao diện. Ở mỗi bậc đo cả bốn đại lượng. Vẽ đường cong và xác định điểm công suất. Chỉ ra tài nguyên nút thắt bằng số đo. Chạy tải kéo dài 30 phút và kiểm bộ nhớ cùng số kết nối có tăng đơn điệu không. Viết ghi chú công suất một trang.

**Pitfalls.** Báo thông lượng đỉnh mà không báo tỉ lệ lỗi · đo ngay khi vừa tăng tải · không đo mức bão hoà hồ kết nối · bỏ phép thử kéo dài nên không phát hiện rò rỉ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đường cong bốn đại lượng đủ sáu bậc, xác định đúng điểm công suất và tài nguyên nút thắt, và phép thử kéo dài không cho thấy rò rỉ.

### Lesson 111 · The job-control API project `DA`
**Prerequisites.** Lesson 110

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Bài dự án khép module, và sản phẩm của nó được dùng lại làm nguồn dữ liệu cho pipeline tham chiếu từ M14B. Xây giao diện điều khiển công việc: nộp công việc có khoá bất biến, truy trạng thái, huỷ, và một tiến trình thợ nhận việc theo cơ chế thuê có thời hạn, có thử lại và có hàng đợi thư chết. PostgreSQL là nguồn sự thật; chỉ thêm kho đệm nếu phép đo chứng minh cần, chứ thêm vì mặc định. Năm phép thử hỏng bắt buộc: nộp trùng, thợ chết sau khi đã gây tác động, cơ sở dữ liệu hết giờ, thuê hết hạn trong khi thợ vẫn sống, và triển khai phiên bản mới trong lúc có công việc đang chạy. Phép thử cuối là phép thử khó nhất và nối thẳng tới lesson 97 và 98. Nộp kèm ghi chú công suất theo lesson 110, mô hình mối đe doạ ngắn, và sổ tay chẩn đoán ba mục.

**Outcome.** Nộp giao diện chạy đúng qua cả năm phép thử hỏng, có ghi chú công suất, mô hình mối đe doạ và sổ tay.

**Đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module thành một dịch vụ có trạng thái chịu được sự cố. Kiểm bằng năm phép thử hỏng cộng rà soát tài liệu; đạt khi không phép thử nào sinh tác động kép hoặc mất công việc.

**Lab.** Xây giao diện theo đặc tả. Chạy năm phép thử hỏng và ghi kết quả từng cái. Chạy tải và viết ghi chú công suất. Viết mô hình mối đe doạ ngắn nêu ba mối đe doạ chính và cách chặn. Viết sổ tay ba mục gồm bão hoà, cơ sở dữ liệu hỏng, và triển khai lỗi.

**Pitfalls.** Thêm kho đệm mà chưa đo · không có cơ chế thuê nên hai thợ cùng nhận một việc · bỏ phép thử triển khai khi đang chạy · sổ tay viết sau khi bảo vệ.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Năm phép thử hỏng đều không sinh tác động kép và không mất công việc, và ba tài liệu đều có nội dung kiểm được.

### Lesson 112 · Gate 3 - a correct service under concurrency and failure `KT`
**Prerequisites.** Lesson 111

**In-class (155 phút).** 110 phút làm bài độc lập · 45 phút chữa bài và phân tích lỗi theo nhóm

**Learn.** Cổng của Phase 3. Bài kiểm hai năng lực: thiết kế mã sửa được ở M7, và vận hành dịch vụ có trạng thái ở M8. Không có nội dung mới.

**Outcome.** Nộp một dịch vụ giữ đúng bất biến dưới truy cập đồng thời và dưới sự cố, với bằng chứng từ phép kiểm chạy song song.

**Đánh giá.** Tầng *đánh giá*. Cổng đo năng lực xây hệ đúng dưới điều kiện thật, nên hình thức là bài làm có tiêm lỗi và có chất vấn.

**Lab.** Buổi 155 phút: 110 phút làm bài độc lập, 45 phút chữa bài. Nhận một đặc tả dịch vụ nhỏ. Bài chấm sáu phần: A (15đ) đồ thị phụ thuộc không có cạnh sai chiều và phép kiểm lõi không cần cơ sở dữ liệu · B (25đ) không sinh tác động kép khi máy khách thử lại, chứng minh bằng ba thí nghiệm · C (20đ) bất biến giữ đúng dưới 50 luồng đồng thời, chứng minh bằng phép kiểm chạy song song · D (15đ) hạn chờ và giới hạn thử lại đặt đủ, không khuếch đại · E (15đ) chẩn đoán một sự cố tiêm sẵn bằng chỉ số và theo vết · F (10đ) phép thử phủ định cho mọi điểm vào đều từ chối đúng.

**Pitfalls.** Chỉ kiểm tuần tự rồi kết luận đúng · bỏ phần chẩn đoán vì hết giờ · thử lại mà không có khoá bất biến · để lõi phụ thuộc cơ sở dữ liệu.

**Self-study (2,4 giờ).** Không có bài tự học. Nếu không đạt, theo phụ lục khắc phục khi không đạt cổng

**Done when.** Đạt ≥ 70/100, phần B và C đều ≥ 60%. Bất biến nào chỉ được chứng minh bằng phép kiểm tuần tự thì không tính điểm ở phần C.

# MODULE M9 · RELATIONAL THEORY AND SQL EXECUTION

**Phase 4 · Lessons 113–132 · 40 giờ**

| | |
|---|---|
| **Objective cấp module** | Đi từ logic quan hệ tới kế hoạch thực thi vật lý: viết truy vấn đúng hạt và tối ưu bằng ước lượng số dòng, chi phí và bằng chứng |
| **Tiền đề** | M2 · M3 · M4 |
| **Exit criterion** | Với năm truy vấn chậm, nộp kế hoạch trước và sau, số khối đọc, số dòng ước lượng so với thực tế, và độ trễ; mọi tối ưu dẫn được về một quan sát trong kế hoạch |
| **Kỹ năng SFIA** | `DBAD` mức 4 · `DTAN` mức 4 |
| **Chế độ hỏng** | Học cú pháp rồi tối ưu bằng cách thêm chỉ mục cho mọi cột, không đọc kế hoạch lần nào, nên truy vấn vẫn chậm và ghi thì chậm thêm |

Đây là module công cụ chính của cả hai vai gộp trong chương trình: Analytics Engineer dùng SQL để mô hình hoá, Data Engineer dùng SQL để nạp và đối soát. Mức yêu cầu vì thế cao hơn mức viết được truy vấn chạy ra kết quả.

Ba phần có thứ tự bắt buộc: nền quan hệ trước để biết truy vấn *nên* trả về gì, ngôn ngữ sau để viết ra, rồi mới tới thực thi để biết vì sao nó chậm. Học phần ba trước là học mẹo tối ưu mà không biết truy vấn có đúng hay không.

Khái niệm **hạt** đặt ở lesson 120 là khái niệm được dùng lại nhiều nhất trong toàn chương trình, tới tận M11, M11B và M14.

### Lesson 113 · Relations, keys and functional dependencies `LT`
**Prerequisites.** Module 9: M4

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bảng trong cơ sở dữ liệu quan hệ không phải bảng tính: nó là một tập các bộ giá trị, nên về lý thuyết không có thứ tự và không có dòng trùng nhau. Hai tính chất đó giải thích nhiều hành vi gây ngạc nhiên, ví dụ vì sao không có thứ tự thì phải nêu rõ cách sắp khi cần. Khoá: khoá dự tuyển là tập thuộc tính xác định duy nhất một bộ, khoá chính là khoá được chọn, khoá ngoại nối hai quan hệ. Phụ thuộc hàm là công cụ để nói một thuộc tính được xác định bởi thuộc tính nào, và nó là nền của chuẩn hoá ở lesson 117. Ràng buộc là tri thức nghiệp vụ được phát biểu bằng máy kiểm được, và **ràng buộc đặt trong cơ sở dữ liệu vẫn đúng khi có đường ghi thứ hai mà ứng dụng không biết**; đây là lý do không nên dựa hoàn toàn vào kiểm tra ở tầng ứng dụng. Phân biệt khoá tự nhiên với khoá thay thế, chuẩn bị cho M11.

**Outcome.** Xác định khoá dự tuyển và phụ thuộc hàm của một quan hệ cho trước, và nêu ràng buộc nào nên đặt trong cơ sở dữ liệu.

**Đánh giá.** Tầng *hiểu*. Bài mở module, đặt từ vựng cho toàn phần nền. Kiểm bằng bài phân tích ba bảng; đạt khi tìm đúng khoá dự tuyển ở ít nhất hai và nêu đúng ràng buộc nên đặt ở tầng cơ sở dữ liệu.

**Lab.** Cho ba bảng có dữ liệu mẫu. Với mỗi bảng, tìm khoá dự tuyển bằng cách kiểm tính duy nhất trên dữ liệu thật, viết các phụ thuộc hàm quan sát được, và đề xuất ràng buộc. Thêm một đường ghi thứ hai bỏ qua ứng dụng và chứng minh ràng buộc ở cơ sở dữ liệu vẫn chặn được.

**Pitfalls.** Coi bảng như bảng tính có thứ tự · chọn khoá chính là một cột tăng tự động mà không xác định khoá tự nhiên · để mọi ràng buộc ở tầng ứng dụng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tìm đúng khoá dự tuyển ở ≥ 2/3 bảng, và chứng minh được ràng buộc ở cơ sở dữ liệu chặn đường ghi thứ hai.

### Lesson 114 · NULL and three-valued logic `TH`
**Prerequisites.** Lesson 113

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** `NULL` không phải một giá trị mà là sự vắng mặt của giá trị, và nhầm hai thứ này là nguồn của những con số sai mà không báo lỗi. Logic ba trạng thái: so sánh với `NULL` cho kết quả không xác định chứ đúng hay sai, nên `WHERE cot <> 'A'` loại luôn cả dòng `NULL`, một hành vi đúng theo lý thuyết và bất ngờ với người dùng. Hành vi của `NULL` trong sáu ngữ cảnh khác nhau: số học, so sánh, nối chuỗi, danh sách giá trị, hàm tổng hợp, và sắp xếp; **hàm tổng hợp bỏ qua `NULL` nên trung bình tính trên cột có `NULL` khác trung bình người dùng nghĩ**. Ba nghĩa khác nhau bị gộp vào một ký hiệu: chưa nhập, không áp dụng, và bằng không; gộp ba nghĩa là mất thông tin và không lấy lại được. Cách xử lý đúng theo ngữ nghĩa chứ theo thói quen thay bằng số không.

**Outcome.** Dự đoán đúng kết quả của biểu thức chứa `NULL` trong sáu ngữ cảnh và chọn cách xử lý theo đúng ngữ nghĩa nghiệp vụ.

**Đánh giá.** Tầng *áp dụng*. Objective là một kỹ năng dự đoán kiểm được ngay, và là nguồn lỗi âm thầm nên phải kiểm kỹ. Kiểm bằng bài dự đoán 15 biểu thức; đạt khi đúng ≥ 13 và giải thích được bằng logic ba trạng thái.

**Lab.** Cho 15 biểu thức chứa `NULL` trong sáu ngữ cảnh. Viết dự đoán trước, chạy, đối chiếu. Trên một bảng có cột thiếu dữ liệu, tính trung bình theo ba cách xử lý khác nhau và so ba kết quả. Viết một câu cho mỗi cách nêu nó phù hợp nghĩa nghiệp vụ nào.

**Pitfalls.** Dùng `= NULL` thay vì `IS NULL` · thay mọi `NULL` bằng số không · quên rằng điều kiện khác giá trị loại luôn dòng `NULL` · gộp ba nghĩa làm một.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Dự đoán đúng ≥ 13/15 biểu thức, và ba cách tính trung bình được gán đúng nghĩa nghiệp vụ.

### Lesson 115 · Relational algebra and logical equivalence `LT`
**Prerequisites.** Lesson 114

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Đại số quan hệ là ngôn ngữ mà bộ tối ưu thật sự làm việc trên đó, nên hiểu nó là hiểu vì sao hai truy vấn viết khác nhau lại cho cùng kế hoạch. Sáu phép cơ bản và ý nghĩa: chọn, chiếu, kết, hợp, hiệu, gộp nhóm. Tương đương logic: đẩy phép chọn xuống sát nguồn không đổi kết quả nhưng đổi hẳn chi phí, và đó chính là phép biến đổi mà bộ tối ưu làm đầu tiên; **viết truy vấn đúng nghĩa quan trọng hơn viết truy vấn theo thứ tự mình muốn nó chạy**, vì bộ tối ưu sẽ sắp lại. Ba phép biến đổi mà bộ tối ưu không tự làm được và người viết phải tự làm: đổi truy vấn con tương quan thành phép kết, bỏ phép chọn phân biệt không cần thiết, và tránh hàm bọc quanh cột lọc. Nối tới lesson 40: ba thuật toán kết đã cài tay nay xuất hiện lại dưới dạng toán tử vật lý mà bộ tối ưu chọn.

**Outcome.** Viết lại một truy vấn thành dạng tương đương có chi phí thấp hơn và giải thích bằng phép biến đổi đại số.

**Đánh giá.** Tầng *áp dụng*. Objective là một phép biến đổi có kết quả kiểm được bằng kế hoạch và số đo. Kiểm bằng ba truy vấn; đạt khi ít nhất hai bản viết lại cho cùng kết quả và chi phí thấp hơn đo được.

**Lab.** Cho ba truy vấn viết kém. Với mỗi cái, viết lại theo một phép biến đổi tương đương, đối soát kết quả khớp tuyệt đối, và so chi phí. Với một truy vấn, viết hai cách khác nhau về hình thức và chứng minh bộ tối ưu cho cùng kế hoạch.

**Pitfalls.** Tối ưu bằng cách đổi thứ tự mệnh đề trong truy vấn · bỏ phép chọn phân biệt mà đổi kết quả · tin rằng cách viết quyết định thứ tự thực thi.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** ≥ 2/3 bản viết lại cho kết quả khớp tuyệt đối với chi phí thấp hơn, và chứng minh được hai cách viết cho cùng kế hoạch.

### Lesson 116 · ER modelling and what the database should enforce `TH`
**Prerequisites.** Lesson 115

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Mô hình thực thể quan hệ là cầu giữa từ vựng nghiệp vụ ở lesson 89 và lược đồ vật lý. Thực thể, thuộc tính, quan hệ; bản số một một, một nhiều, nhiều nhiều và cách hiện thực từng loại. Quan hệ nhiều nhiều luôn cần bảng nối, và bảng nối thường mang thêm thuộc tính riêng mà người mới hay bỏ sót. Bốn loại ràng buộc và việc mỗi loại chặn được gì: khoá chính chặn trùng, khoá ngoại chặn tham chiếu mồ côi, duy nhất chặn trùng theo khoá nghiệp vụ, và kiểm tra chặn giá trị vô lý. Câu hỏi thiết kế đi kèm: **hành vi khi xoá bản ghi cha**, vì ba lựa chọn cho ba kết quả khác nhau và chọn sai gây mất dữ liệu hoặc chặn nghiệp vụ. Ba trường hợp nên cố ý không đặt khoá ngoại và lý do, thường gặp ở kho phân tích, chuẩn bị cho M11 và M12.

**Outcome.** Dựng lược đồ từ mô tả nghiệp vụ với ràng buộc đầy đủ, và chứng minh mỗi ràng buộc chặn được đúng loại dữ liệu sai.

**Đánh giá.** Tầng *áp dụng*. Objective là một thiết kế có tiêu chí nghiệm thu bằng phép thử chèn dữ liệu sai. Kiểm bằng tám phép thử phủ định; đạt khi cả tám bị chặn và thông báo lỗi nêu đúng ràng buộc.

**Lab.** Từ mô tả nghiệp vụ một hệ đặt hàng có quan hệ nhiều nhiều, dựng lược đồ đầy đủ ràng buộc. Chèn tám bản ghi sai theo tám cách và chứng minh cả tám bị chặn. Thử ba hành vi xoá bản ghi cha khác nhau và ghi kết quả từng cái.

**Pitfalls.** Quên bảng nối cho quan hệ nhiều nhiều · bỏ khoá ngoại vì thấy chậm mà chưa đo · đặt hành vi xoá lan toả cho bảng có dữ liệu lịch sử · không thử chèn dữ liệu sai.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tám phép thử phủ định đều bị chặn với thông báo nêu đúng ràng buộc, và ba hành vi xoá được ghi kết quả rõ ràng.

### Lesson 117 · Normalization to BCNF, and deliberate denormalization `TH`
**Prerequisites.** Lesson 116

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Chuẩn hoá không phải nghi thức mà là cách loại bỏ ba dị thường cụ thể, nên dạy bằng cách gặp dị thường trước rồi mới học quy tắc. Ba dị thường: thêm không được vì thiếu dữ liệu không liên quan, sửa một chỗ mà chỗ khác còn giá trị cũ, và xoá một bản ghi làm mất luôn thông tin khác. Các dạng chuẩn từ một tới Boyce-Codd, mỗi dạng chữa một loại phụ thuộc, dựa trên phụ thuộc hàm ở lesson 113. Phi chuẩn hoá có chủ đích: lặp dữ liệu để đọc nhanh hơn, đổi lại phải tự giữ đồng bộ và chấp nhận rủi ro lệch; **chỉ phi chuẩn hoá sau khi đo và sau khi biết đường ghi nào giữ đồng bộ**. Đây là chỗ hai vai trong chương trình tách nhau: hệ giao dịch nghiêng về chuẩn hoá, kho phân tích cố ý phi chuẩn hoá, và lý do sẽ rõ ở M11 và M12.

**Outcome.** Chuẩn hoá một bảng phẳng tới Boyce-Codd, chỉ ra dị thường nào được chữa ở bước nào, rồi phi chuẩn hoá một đường đọc có đo.

**Đánh giá.** Tầng *phân tích*. Objective đòi nối mỗi bước chuẩn hoá với một dị thường cụ thể, chứ áp quy tắc. Kiểm bằng bài chuẩn hoá cộng đo; đạt khi mỗi bước gắn đúng dị thường và phần phi chuẩn hoá có số đo ba chiều.

**Lab.** Từ một bảng phẳng, tự tạo ra cả ba dị thường bằng dữ liệu thật. Chuẩn hoá từng bước và chỉ ra bước nào chữa dị thường nào. Sau đó chọn một đường đọc và phi chuẩn hoá, đo tác động lên tốc độ đọc, tốc độ ghi và dung lượng. Nêu đường ghi nào chịu trách nhiệm giữ đồng bộ.

**Pitfalls.** Học thuộc định nghĩa dạng chuẩn mà không nhận ra dị thường trong bảng thật · chuẩn hoá tới mức mọi truy vấn phải kết mười bảng · phi chuẩn hoá mà không có cơ chế giữ đồng bộ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba dị thường được tái hiện và gắn đúng bước chữa, và phần phi chuẩn hoá có số đo cả đọc, ghi lẫn dung lượng.

### Lesson 118 · Logical query processing order `LT`
**Prerequisites.** Lesson 117

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Thứ tự viết một truy vấn khác thứ tự nó được xử lý về mặt logic, và biết thứ tự đó giải thích phần lớn lỗi cú pháp khó hiểu của người mới. Thứ tự logic: nguồn, lọc dòng, gộp nhóm, lọc nhóm, chọn cột, sắp xếp, giới hạn. Từ đó suy ra ngay ba hệ quả: bí danh đặt ở bước chọn cột nên không dùng được ở bước lọc dòng nhưng dùng được ở bước sắp xếp; lọc dòng chạy trước gộp nhóm còn lọc nhóm chạy sau, nên đặt điều kiện sai chỗ vừa sai nghĩa vừa chậm; và hàm cửa sổ chạy sau gộp nhóm nên không lồng trực tiếp vào điều kiện lọc được. Phân biệt thứ tự logic với thứ tự thực thi vật lý: bộ tối ưu được phép sắp lại miễn kết quả không đổi, theo lesson 115. Phạm vi tên và cách giải quyết khi hai bảng có cột cùng tên.

**Outcome.** Giải thích một lỗi cú pháp hoặc một kết quả sai bằng thứ tự xử lý logic, và sửa bằng cách đặt điều kiện đúng bước.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết nền cho toàn phần ngôn ngữ; chưa đòi tối ưu. Kiểm bằng tám truy vấn có lỗi; đạt khi giải thích đúng ít nhất sáu bằng thứ tự xử lý chứ bằng kinh nghiệm.

**Lab.** Cho tám truy vấn: bốn cái lỗi cú pháp, bốn cái chạy được nhưng sai nghĩa do đặt điều kiện sai bước. Với mỗi cái, chỉ ra bước nào gây ra và sửa. Với hai truy vấn, chứng minh đặt điều kiện ở bước lọc dòng và bước lọc nhóm cho hai kết quả khác nhau.

**Pitfalls.** Dùng bí danh trong mệnh đề lọc dòng · đặt điều kiện lọc dòng vào mệnh đề lọc nhóm · tin thứ tự viết là thứ tự chạy · lồng hàm cửa sổ vào điều kiện lọc.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Giải thích đúng ≥ 6/8 truy vấn bằng thứ tự xử lý, và chứng minh được hai kết quả khác nhau khi đặt điều kiện sai bước.

### Lesson 119 · Joins, duplicate multiplication and NULL behaviour `TH`
**Prerequisites.** Lesson 118

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phép kết giải thích bằng tích Descartes cộng điều kiện lọc: đó là định nghĩa cho phép suy ra mọi hành vi còn lại thay vì nhớ từng trường hợp. Bốn kiểu kết cơ bản cộng hai kiểu nửa và phản, cùng bài toán mỗi kiểu giải. Nhân bản dòng là chế độ hỏng nguy hiểm nhất: khi bên phải có nhiều dòng khớp, mỗi dòng bên trái nhân lên và **mọi phép tổng sau đó bị thổi phồng mà không có lỗi nào báo**. Cách phát hiện bắt buộc: đếm dòng trước và sau mỗi phép kết, và đối chiếu tổng với nguồn độc lập. Kết trái rồi đặt điều kiện bảng phải vào mệnh đề lọc dòng làm nó âm thầm thành kết trong, một lỗi kinh điển. `NULL` trong khoá kết không bao giờ khớp, theo lesson 114, nên dòng có khoá thiếu biến mất khỏi kết quả. Nối tới lesson 40: ba thuật toán kết là cách engine thực hiện, còn đây là nghĩa.

**Outcome.** Viết truy vấn nhiều bảng và chứng minh không mất dòng không nhân dòng bằng phép đếm và đối soát tổng.

**Đánh giá.** Tầng *áp dụng*. Objective là một quy trình kiểm chứng bắt buộc chứ chỉ viết đúng cú pháp. Kiểm bằng bài ghép năm bảng; đạt khi tổng khớp tuyệt đối với tổng tính trực tiếp từ bảng gốc.

**Lab.** Ghép năm bảng để ra báo cáo doanh thu theo khách và sản phẩm. Đếm dòng sau mỗi bước kết. Đối soát tổng với tổng tính thẳng từ bảng hoá đơn. Cố ý tạo nhân bản dòng và định lượng mức thổi phồng. Đặt điều kiện bảng phải vào mệnh đề lọc dòng và chứng minh kết trái thành kết trong.

**Pitfalls.** Không đếm dòng sau khi kết · dùng phép chọn phân biệt để chữa nhân bản thay vì sửa hạt · đặt điều kiện bảng phải sai mệnh đề · quên rằng khoá `NULL` không khớp.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tổng khớp tuyệt đối với bản tính trực tiếp, và định lượng được mức thổi phồng của trường hợp nhân bản cố ý.

### Lesson 120 · Aggregation, HAVING and the grain statement `TH`
**Prerequisites.** Lesson 119

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Gộp nhóm là **một phép biến đổi hạt**, và cách trình bày này giải thích mọi quy tắc còn lại thay vì phải nhớ chúng rời rạc. Hạt là câu trả lời cho một dòng trong kết quả đại diện cho cái gì, phát biểu bằng một câu không mơ hồ. Từ đó suy ra: mọi cột trong danh sách chọn phải nằm trong nhóm hoặc trong hàm tổng hợp, vì cột khác không xác định ở hạt mới. Ba biến thể đếm cho ba nghĩa khác nhau và nhầm chúng là nguồn số sai. Hàm tổng hợp bỏ qua `NULL` theo lesson 114. Lọc dòng trước gộp và lọc nhóm sau gộp theo lesson 118. Gộp nhóm trên biểu thức. **Quy tắc bắt buộc của chương trình: mỗi truy vấn gộp phải kèm phát biểu hạt trước và sau, và sai hạt là sai bài dù kết quả số trông hợp lý**; quy tắc này được dùng lại nguyên vẹn ở M11 và M11B.

**Outcome.** Phát biểu hạt trước và sau mỗi phép gộp và chọn đúng biến thể đếm theo nghĩa nghiệp vụ.

**Đánh giá.** Tầng *áp dụng*. Objective là một kỷ luật phát biểu kiểm được bằng rà soát, và là nền cho toàn phần mô hình hoá sau. Kiểm bằng 20 truy vấn gộp; đạt khi mọi truy vấn có phát biểu hạt đúng và ba biến thể đếm dùng đúng chỗ.

**Lab.** Viết 20 truy vấn gộp trên dữ liệu thật, mỗi truy vấn nộp kèm phát biểu hạt trước và sau. Với ba truy vấn, dùng cả ba biến thể đếm và giải thích ba con số khác nhau. Đổi bài: người khác đọc phát biểu hạt và kiểm truy vấn có khớp phát biểu không.

**Pitfalls.** Bỏ phát biểu hạt vì thấy hiển nhiên · dùng đếm mọi dòng khi cần đếm giá trị phân biệt · báo trung bình trên dữ liệu lệch mà không kèm phân bố · quên rằng gộp đổi hạt nên tổng không còn cộng được như trước.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Cả 20 truy vấn có phát biểu hạt đúng và khớp truy vấn, và ba biến thể đếm được giải thích đúng nghĩa.

### Lesson 121 · Subqueries, CTEs and the materialization caveat `TH`
**Prerequisites.** Lesson 120

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba vị trí đặt truy vấn con và chi phí khác nhau của từng vị trí. Truy vấn con tương quan chạy lại cho mỗi dòng bên ngoài nên chi phí nhân lên, và phần lớn trường hợp viết lại được thành phép kết; bộ tối ưu đôi khi tự làm việc đó nhưng không phải lúc nào cũng làm. So sánh ba cách kiểm tồn tại và khác biệt ngữ nghĩa khi có `NULL`: dùng danh sách giá trị với truy vấn con chứa `NULL` trả về rỗng một cách bất ngờ, theo lesson 114. Biểu thức bảng chung làm truy vấn dài đọc được bằng cách đặt tên cho từng bước; **quy tắc đặt tên là đặt theo hạt chứ theo thao tác**, vì tên theo hạt cho biết một dòng là gì. Cảnh báo về vật chất hoá: ở một số hệ, biểu thức bảng chung là hàng rào tối ưu nên bộ tối ưu không đẩy điều kiện lọc xuyên qua được, và khi đó nó làm truy vấn chậm hẳn.

**Outcome.** Tái cấu trúc một truy vấn lồng nhiều tầng thành chuỗi biểu thức bảng chung đặt tên theo hạt, và kiểm xem vật chất hoá có làm chậm không.

**Đánh giá.** Tầng *áp dụng*. Objective gồm cả một cảnh báo về hiệu năng kiểm được bằng kế hoạch. Kiểm bằng bài tái cấu trúc cộng so kế hoạch; đạt khi kết quả khớp tuyệt đối và nhận ra đúng trường hợp vật chất hoá gây chậm.

**Lab.** Nhận một truy vấn 80 dòng lồng bốn tầng. Tái cấu trúc thành năm biểu thức bảng chung đặt tên theo hạt. Đối soát kết quả. So kế hoạch và thời gian hai bản. Viết một truy vấn mà biểu thức bảng chung chặn việc đẩy điều kiện lọc và chứng minh bằng kế hoạch.

**Pitfalls.** Đặt tên biểu thức bảng chung là `t1` hay `tam2` · dùng danh sách giá trị với truy vấn con có `NULL` · giả định biểu thức bảng chung luôn miễn phí · để truy vấn con tương quan trong vòng lặp lớn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Kết quả tái cấu trúc khớp tuyệt đối, tên các bước đặt theo hạt, và chỉ ra được bằng kế hoạch trường hợp vật chất hoá chặn tối ưu.

### Lesson 122 · Recursive CTEs for hierarchies and graphs `TH`
**Prerequisites.** Lesson 121

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Cấu trúc phân cấp xuất hiện khắp nơi trong dữ liệu nghiệp vụ: cây tổ chức, danh mục sản phẩm, và đồ thị phụ thuộc theo lesson 38. Biểu thức bảng chung đệ quy gồm hai phần: phần neo cho mức đầu, và phần đệ quy nối tiếp cho tới khi không còn dòng mới. Ba điều kiện để nó dừng và chỉ cần thiếu một là vòng lặp vô hạn: có điều kiện dừng, dữ liệu không có chu trình, và có giới hạn độ sâu phòng khi hai điều kiện trên sai. Kỹ thuật chống chu trình bằng cách giữ đường đi đã qua, đúng ý tưởng phát hiện chu trình ở lesson 38. Ba bài toán thường giải bằng đệ quy: duyệt xuống toàn bộ con cháu, truy ngược lên tổ tiên, và tính tổng tích luỹ theo nhánh. Giới hạn hiệu năng: đệ quy trên đồ thị lớn tốn kém, nên với đồ thị rất lớn thì tính sẵn bảng đường đi là lựa chọn đúng hơn.

**Outcome.** Viết truy vấn đệ quy duyệt một cấu trúc phân cấp có chống chu trình và có giới hạn độ sâu.

**Đánh giá.** Tầng *áp dụng*. Objective là một kỹ thuật cụ thể có ba điều kiện an toàn kiểm được. Kiểm bằng ba bài toán cộng một tập dữ liệu có chu trình; đạt khi cả ba đúng và truy vấn không treo trên dữ liệu có chu trình.

**Lab.** Trên bảng cây tổ chức, viết ba truy vấn đệ quy: liệt kê toàn bộ cấp dưới, truy ngược chuỗi quản lý, và tính tổng ngân sách theo nhánh. Chèn một chu trình vào dữ liệu và chứng minh truy vấn có chống chu trình vẫn dừng còn bản không có thì treo.

**Pitfalls.** Quên điều kiện dừng · không chống chu trình · không đặt giới hạn độ sâu · dùng đệ quy cho đồ thị rất lớn mà chưa cân nhắc bảng đường đi tính sẵn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba truy vấn cho kết quả đúng, và bản có chống chu trình dừng được trên dữ liệu có chu trình trong khi bản không có thì treo.

### Lesson 123 · Window functions - partition, order and frame `TH`
**Prerequisites.** Lesson 122

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Khác biệt cơ bản với gộp nhóm phát biểu bằng một câu: gộp nhóm **thu gọn** dòng còn hàm cửa sổ **giữ nguyên** dòng và thêm một cột tính trên một nhóm dòng lân cận. Từ đó suy ra vì sao dùng được hàm cửa sổ để lấy đứng đầu mỗi nhóm mà vẫn giữ mọi cột. Giải phẫu ba phần: phân vùng chia dòng thành nhóm, sắp xếp định thứ tự trong nhóm, khung xác định dòng nào được tính. Bốn hàm xếp hạng và khác biệt chỉ lộ ra khi có giá trị trùng, nên phải thử trên dữ liệu có trùng chứ dữ liệu sạch. Mẫu lấy N dòng đầu mỗi nhóm, giải đúng bài toán đã gặp ở lesson 37 nhưng ở tầng SQL. Vì sao không dùng hàm cửa sổ trong mệnh đề lọc dòng được, theo thứ tự xử lý ở lesson 118, và cách vòng qua bằng một tầng bọc ngoài.

**Outcome.** Giải bài toán lấy N đầu mỗi nhóm và chọn đúng hàm xếp hạng theo yêu cầu xử lý giá trị trùng.

**Đánh giá.** Tầng *áp dụng*. Objective đòi chọn đúng biến thể theo ngữ nghĩa, chỗ khác biệt chỉ lộ ra ở ca biên. Kiểm bằng ba yêu cầu trên dữ liệu có trùng; đạt khi cả ba chọn đúng hàm và kết quả đúng ở ca có trùng.

**Lab.** Trên dữ liệu cố ý có giá trị trùng, viết ba truy vấn: top ba sản phẩm mỗi chi nhánh, đơn gần nhất của mỗi khách, và chia khách thành năm nhóm theo chi tiêu. Với mỗi cái, thử cả bốn hàm xếp hạng và giải thích vì sao chọn cái đã chọn.

**Pitfalls.** Dùng hàm xếp hạng có trùng khi cần đúng một dòng mỗi nhóm · quên phân vùng nên xếp hạng toàn bảng · đặt hàm cửa sổ vào mệnh đề lọc dòng · thử trên dữ liệu không có giá trị trùng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba truy vấn đúng trên dữ liệu có trùng, và giải thích được vì sao chọn hàm xếp hạng đó thay vì ba hàm kia.

### Lesson 124 · Frames, running totals and period comparison `TH`
**Prerequisites.** Lesson 123

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Mệnh đề khung quyết định hàm cửa sổ nhìn thấy những dòng nào, và hiểu nhầm nó là nguồn của các con số luỹ kế sai. Hai cách đếm khung: theo số dòng và theo giá trị; hai cách cho kết quả khác nhau khi có giá trị trùng, và ví dụ đối chiếu làm rõ khác biệt đó. Khung mặc định khi có mệnh đề sắp xếp không phải toàn bộ phân vùng, nên một số hàm cho kết quả bất ngờ nếu không nêu khung tường minh. So kỳ trước và cùng kỳ năm trước bằng hàm lấy giá trị dòng trước và dòng sau. **Vấn đề kỳ thiếu**: tháng không có giao dịch biến mất khỏi kết quả nên phép so kỳ trước lấy nhầm tháng, và lời giải là kết với bảng lịch đầy đủ; đây là bài học sẽ dùng lại ở M11 khi dựng bảng chiều thời gian. Chia cho không khi kỳ trước bằng không, và cách xử lý theo nghĩa nghiệp vụ.

**Outcome.** Dựng báo cáo có luỹ kế, trung bình trượt và tăng trưởng so kỳ, đúng cả ở kỳ không có dữ liệu.

**Đánh giá.** Tầng *áp dụng*. Objective có một ca biên cụ thể mà bản làm ẩu luôn sai. Kiểm bằng đối soát với bản tính độc lập; đạt khi khớp tuyệt đối kể cả ở các kỳ thiếu dữ liệu.

**Lab.** Dựng báo cáo 24 tháng có ba chỉ số trên dữ liệu cố ý thiếu ba tháng. Đối soát với bản tính độc lập. So kết quả giữa khung đếm theo dòng và khung đếm theo giá trị trên dữ liệu có trùng. Xử lý trường hợp kỳ trước bằng không và nêu nghĩa nghiệp vụ đã chọn.

**Pitfalls.** Không dựng bảng lịch nên kỳ rỗng biến mất · dựa vào khung mặc định · nhầm hai cách đếm khung · chia cho không mà không xử lý.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba chỉ số khớp tuyệt đối với bản tính độc lập kể cả ở ba tháng thiếu, và giải thích được khác biệt giữa hai cách đếm khung.

### Lesson 125 · DML, DDL, constraints and views `TH`
**Prerequisites.** Lesson 124

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phần ngôn ngữ còn lại, gắn với ranh giới giao dịch đã học ở lesson 103. Các lệnh sửa dữ liệu và mệnh đề trả về dòng đã sửa, hữu dụng để ghi nhật ký kiểm toán trong cùng một lượt. Lệnh hợp nhất và cạm bẫy khi nguồn có dòng trùng: nó không báo lỗi mà cho kết quả không xác định. Ghi bất biến theo khoá nghiệp vụ, đúng nguyên tắc ở lesson 30 và 105, nay bằng SQL. Lệnh định nghĩa cấu trúc và ràng buộc theo lesson 116; **thêm ràng buộc lên bảng lớn có thể khoá bảng rất lâu**, nên quy trình đổi cấu trúc an toàn là thêm ở trạng thái chưa kiểm rồi kiểm sau. Khung nhìn là truy vấn đặt tên, không lưu dữ liệu; khung nhìn vật chất hoá có lưu và phải làm mới, nên nó là một dạng bộ đệm và mang mọi vấn đề của bộ đệm, chủ đề sẽ quay lại ở M12 và M14. Ba lý do khung nhìn chồng khung nhìn thành khó gỡ, chuẩn bị cho bài toán ở M14.

**Outcome.** Viết lệnh ghi bất biến theo khoá nghiệp vụ và đổi cấu trúc bảng lớn mà không khoá bảng quá ngưỡng.

**Đánh giá.** Tầng *áp dụng*. Objective gồm hai thao tác có ràng buộc vận hành kiểm được. Kiểm bằng thí nghiệm ghi lặp và thí nghiệm đổi cấu trúc có tải; đạt khi ghi lặp không sinh trùng và thời gian khoá dưới ngưỡng.

**Lab.** Viết lệnh hợp nhất theo khoá nghiệp vụ và chạy lại năm lần trên cùng dữ liệu, chứng minh không sinh trùng. Tạo nguồn có dòng trùng và quan sát kết quả không xác định. Thêm một ràng buộc lên bảng 5 triệu dòng đang có tải, đo thời gian khoá ở hai cách làm.

**Pitfalls.** Dùng lệnh hợp nhất với nguồn chưa khử trùng · thêm ràng buộc trực tiếp lên bảng lớn đang có tải · chồng khung nhìn nhiều tầng · nhầm khung nhìn với khung nhìn vật chất hoá.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ghi lặp năm lần không sinh trùng, và thời gian khoá khi thêm ràng buộc dưới ngưỡng ở cách làm hai bước.

### Lesson 126 · Inside the engine - from parser to executor `LT`
**Prerequisites.** Lesson 125

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Truy vấn đi qua năm giai đoạn trước khi có kết quả, và biết giai đoạn nào làm gì là điều kiện để đọc kế hoạch ở lesson 130. Bộ phân tích cú pháp dựng cây; bộ ràng buộc tên phân giải bảng và cột, đây là nơi lỗi tên xuất hiện; bộ viết lại áp các phép biến đổi tương đương ở lesson 115; bộ lập kế hoạch liệt kê các cách thực hiện và chọn cái rẻ nhất theo mô hình chi phí; bộ thực thi chạy kế hoạch đã chọn. Điểm quan trọng: **bộ lập kế hoạch chọn dựa trên ước lượng, và ước lượng có thể sai**; phần lớn truy vấn chậm bất thường là hậu quả của ước lượng sai chứ của bộ tối ưu kém. Mô hình chi phí kết hợp chi phí đọc và chi phí tính, và nó được hiệu chỉnh theo giả định về phần cứng, nên máy có đĩa thể rắn mà cấu hình mặc định cho đĩa quay thì bộ tối ưu tránh tra chỉ mục một cách không cần thiết.

**Outcome.** Nêu đúng giai đoạn nào chịu trách nhiệm cho một hiện tượng cho trước, và giải thích vì sao ước lượng sai làm kế hoạch xấu.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết nền cho toàn phần thực thi. Kiểm bằng sáu hiện tượng cần quy về giai đoạn; đạt khi quy đúng ít nhất bốn và giải thích đúng vai trò của ước lượng.

**Lab.** Cho sáu hiện tượng gồm lỗi tên cột, truy vấn viết khác nhau ra cùng kế hoạch, kế hoạch đổi sau khi cập nhật thống kê, và ba cái khác. Quy mỗi hiện tượng về một giai đoạn. Đọc cấu hình chi phí của hệ và chỉ ra giả định nào về phần cứng đang được dùng.

**Pitfalls.** Nghĩ bộ tối ưu luôn chọn đúng · đổ lỗi cho engine khi nguyên nhân là ước lượng sai · bỏ qua cấu hình chi phí không khớp phần cứng thật.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Quy đúng ≥ 4/6 hiện tượng về giai đoạn, và chỉ ra được giả định phần cứng trong cấu hình chi phí.

### Lesson 127 · Physical operators and the three join algorithms `TH`
**Prerequisites.** Lesson 126

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Các toán tử vật lý là những viên gạch mà kế hoạch được ghép từ đó, và ba thuật toán kết ở đây chính là ba thứ đã tự cài ở lesson 40. Toán tử quét: quét tuần tự đọc cả bảng, quét chỉ mục đi qua cây rồi lấy dòng, quét chỉ mục có phủ không cần lấy dòng vì chỉ mục đã chứa đủ cột. Toán tử sắp xếp và toán tử gộp, cùng ngưỡng bộ nhớ: vượt ngưỡng thì tràn ra đĩa và đó chính là sắp xếp ngoài ở lesson 39, nên chi phí nhảy vọt. Ba thuật toán kết và điều kiện chọn: vòng lặp lồng nhau tốt khi bên ngoài nhỏ và bên trong có chỉ mục; kết băm tốt khi một bên vừa bộ nhớ; kết trộn tốt khi cả hai đã sắp xếp. Bộ nhớ làm việc là tham số quyết định ranh giới giữa chạy trong bộ nhớ và tràn đĩa, và đo được tác động của nó.

**Outcome.** Dự đoán thuật toán kết mà bộ tối ưu sẽ chọn cho một tình huống và kiểm chứng bằng kế hoạch.

**Đánh giá.** Tầng *phân tích*. Objective nối kiến thức tự cài ở lesson 40 với lựa chọn thật của engine. Kiểm bằng bốn tình huống; đạt khi dự đoán đúng ít nhất ba và giải thích đúng trường hợp tràn đĩa.

**Lab.** Tạo bốn tình huống khác nhau về kích thước hai bên và sự có mặt của chỉ mục. Với mỗi cái, viết dự đoán thuật toán kết trước khi chạy, rồi đọc kế hoạch để đối chiếu. Giảm bộ nhớ làm việc tới khi thấy tràn đĩa trong kế hoạch và đo mức chậm đi.

**Pitfalls.** Nghĩ một thuật toán kết luôn nhanh hơn · bỏ qua bộ nhớ làm việc · không phân biệt quét chỉ mục với quét chỉ mục có phủ · kết luận mà không đọc kế hoạch.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Dự đoán đúng ≥ 3/4 tình huống, và chỉ ra được dấu hiệu tràn đĩa trong kế hoạch kèm số đo mức chậm đi.

### Lesson 128 · Statistics, selectivity and cardinality estimation `TH`
**Prerequisites.** Lesson 127

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bộ lập kế hoạch chọn dựa trên ước lượng số dòng, và ước lượng dựa trên thống kê thu thập được từ dữ liệu. Ba loại thống kê: số giá trị phân biệt, biểu đồ phân bố, và danh sách giá trị phổ biến nhất. Độ chọn lọc là tỉ lệ dòng còn lại sau một điều kiện, và ước lượng số dòng là tích của các độ chọn lọc. Từ đó lộ ra **giả định độc lập**: engine giả định các điều kiện không liên quan nhau, nên khi hai cột tương quan thì ước lượng sai nhiều bậc. Ví dụ điển hình là lọc theo thành phố và theo mã vùng: hai điều kiện thực ra nói cùng một thứ. Ba nguyên nhân ước lượng sai: thống kê cũ, dữ liệu lệch, và tương quan giữa cột. Ba cách chữa theo thứ tự nên thử: cập nhật thống kê, khai báo thống kê mở rộng cho nhóm cột tương quan, và viết lại truy vấn. So sánh số dòng ước lượng với số dòng thật là bước chẩn đoán đầu tiên.

**Outcome.** Phát hiện ước lượng sai bằng cách so số dòng ước lượng với thực tế và chữa bằng đúng một trong ba cách.

**Đánh giá.** Tầng *phân tích*. Objective là chẩn đoán nguyên nhân gốc của phần lớn truy vấn chậm. Kiểm bằng ba tình huống ước lượng sai; đạt khi phát hiện cả ba và chữa được ít nhất hai với tỉ lệ sai giảm rõ rệt.

**Lab.** Tạo ba tình huống: thống kê cũ sau khi nạp lớn, dữ liệu lệch nặng, và hai cột tương quan. Với mỗi cái, chạy kế hoạch có phân tích và so số dòng ước lượng với thực tế. Chữa bằng cách phù hợp và đo lại tỉ lệ sai. Ghi bảng trước sau.

**Pitfalls.** Thêm chỉ mục để chữa ước lượng sai · không cập nhật thống kê sau khi nạp lớn · bỏ qua giả định độc lập · so thời gian mà không so số dòng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phát hiện đúng cả ba tình huống, và tỉ lệ sai ước lượng giảm rõ rệt ở ≥ 2/3 sau khi chữa.

### Lesson 129 · Indexes - structure, composite order and cost `TH`
**Prerequisites.** Lesson 128

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Chỉ mục là cây B theo lesson 36, và mọi quy tắc dùng chỉ mục suy ra từ cấu trúc đó. Chỉ mục tổ hợp và quy tắc tiền tố trái: chỉ mục trên ba cột dùng được cho điều kiện trên cột đầu, hai cột đầu, hoặc cả ba, nhưng **không dùng được nếu điều kiện chỉ có cột thứ hai**; nên thứ tự cột trong chỉ mục là quyết định thiết kế chứ chi tiết. Chỉ mục có cột phủ thêm để tránh phải lấy dòng. Chỉ mục một phần chỉ trên tập con dòng, rất hiệu quả khi truy vấn luôn lọc theo một điều kiện cố định. Chỉ mục trên biểu thức khi điều kiện lọc bọc hàm quanh cột. Cái giá của chỉ mục và phần hay bị bỏ qua: mỗi chỉ mục làm mọi lệnh ghi chậm thêm và chiếm dung lượng, nên **thêm chỉ mục cho mọi cột là cách làm hệ ghi chậm mà đọc không nhanh hơn**. Cách tìm chỉ mục không bao giờ được dùng và bỏ chúng đi.

**Outcome.** Thiết kế bộ chỉ mục cho một khối lượng truy vấn thật và định lượng cả phần đọc nhanh lên lẫn phần ghi chậm đi.

**Đánh giá.** Tầng *đánh giá*. Objective đòi cân hai chiều đối nghịch, chứ chỉ thêm chỉ mục. Kiểm bằng bảng đo hai chiều; đạt khi đọc nhanh lên có số, ghi chậm đi được định lượng, và không chỉ mục nào thừa.

**Lab.** Nhận nhật ký 50 truy vấn thật. Thiết kế bộ chỉ mục. Đo thời gian bộ truy vấn trước và sau, và đo thông lượng ghi trước và sau. Cố ý tạo một chỉ mục sai thứ tự cột và chứng minh nó không được dùng. Tìm và bỏ các chỉ mục không bao giờ được dùng.

**Pitfalls.** Thêm chỉ mục cho mọi cột trong điều kiện lọc · đặt sai thứ tự cột trong chỉ mục tổ hợp · bọc hàm quanh cột lọc làm chỉ mục vô hiệu · không đo tác động lên ghi.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bộ truy vấn nhanh lên có số, tác động lên thông lượng ghi được định lượng, và chứng minh được chỉ mục sai thứ tự không được dùng.

### Lesson 130 · Reading EXPLAIN ANALYZE with buffers `TH`
**Prerequisites.** Lesson 129

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Kế hoạch thực thi là nguồn sự thật duy nhất khi chẩn đoán truy vấn, và đọc được nó phân biệt người tối ưu có căn cứ với người thử từng cách. Đọc từ trong ra ngoài, vì nút con chạy trước nút cha. Bốn con số phải xem ở mỗi nút: số dòng ước lượng, số dòng thật, thời gian, và số khối đọc. **So ước lượng với thực tế là bước đầu tiên**, vì lệch nhiều bậc chỉ thẳng tới nguyên nhân ở lesson 128. Số khối đọc tách thành khối trong bộ đệm và khối đọc từ đĩa, và tỉ lệ đó cho biết truy vấn có được hưởng hồ đệm hay không, nối lại lesson 53. Cảnh báo về thời gian: bật đo thời gian từng nút làm truy vấn chậm đi, nên số thời gian trong kế hoạch không so trực tiếp với thời gian chạy thật được. Quy trình chẩn đoán bốn bước theo thứ tự cố định để không bỏ sót.

**Outcome.** Đọc một kế hoạch và định vị nút tốn nhất cùng nguyên nhân, dẫn bằng bốn con số chứ bằng cảm nhận.

**Đánh giá.** Tầng *phân tích*. Objective là kỹ năng đọc bằng chứng, điều kiện cho bài dự án ở lesson 132. Kiểm bằng năm kế hoạch; đạt khi định vị đúng nút tốn nhất ở ít nhất bốn và quy đúng nguyên nhân ở ít nhất ba.

**Lab.** Cho năm kế hoạch thực thi của năm truy vấn chậm vì năm nguyên nhân khác nhau. Với mỗi kế hoạch, chạy quy trình bốn bước, định vị nút tốn nhất, và quy nguyên nhân. Với một truy vấn, so thời gian trong kế hoạch với thời gian chạy thật và giải thích chênh lệch.

**Pitfalls.** Đọc kế hoạch từ ngoài vào · chỉ nhìn thời gian mà bỏ số dòng · bỏ qua số khối đọc · so thời gian trong kế hoạch với thời gian chạy thật.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Định vị đúng nút tốn nhất ở ≥ 4/5 kế hoạch và quy đúng nguyên nhân ở ≥ 3/5, kèm bốn con số dẫn chứng.

### Lesson 131 · Sargability, parameters and plan stability `TH`
**Prerequisites.** Lesson 130

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba chủ đề nhỏ nhưng gây nhiều sự cố trong hệ thật. Điều kiện dùng được chỉ mục: điều kiện phải so sánh trực tiếp với cột chứ với hàm bọc quanh cột; ba cách phá chỉ mục phổ biến là bọc hàm, ép kiểu ngầm, và khớp mẫu có ký tự đại diện ở đầu. Truy vấn tham số hoá: tách giá trị khỏi câu lệnh giúp tái dùng kế hoạch và chặn lỗ hổng chèn mã, theo nguyên tắc đã nêu ở lesson 102. Nhưng nó sinh vấn đề riêng: **kế hoạch lập cho giá trị đầu tiên có thể rất xấu cho giá trị sau**, đặc biệt khi dữ liệu lệch; đây là hiện tượng kế hoạch bị đóng băng theo tham số và là nguyên nhân của những sự cố kiểu truy vấn đột nhiên chậm mà mã không đổi. Ba cách xử lý. Ổn định kế hoạch: vì sao kế hoạch đổi sau khi cập nhật thống kê hoặc sau khi nâng cấp, và vì sao đó vừa là tính năng vừa là rủi ro.

**Outcome.** Nhận ra ba cách phá chỉ mục trong truy vấn cho trước và tái hiện được hiện tượng kế hoạch bị đóng băng theo tham số.

**Đánh giá.** Tầng *phân tích*. Objective gồm một hiện tượng khó tái hiện mà nhiều người chưa từng thấy. Kiểm bằng sáu truy vấn cộng một thí nghiệm; đạt khi tìm đúng ít nhất năm chỗ phá chỉ mục và tái hiện được hiện tượng kế hoạch xấu theo tham số.

**Lab.** Cho sáu truy vấn, mỗi cái phá chỉ mục theo một cách. Tìm và sửa từng cái, kiểm chứng bằng kế hoạch. Trên bảng có dữ liệu lệch, chạy truy vấn tham số hoá với giá trị hiếm trước rồi giá trị phổ biến sau, và chứng minh kế hoạch không đổi dù đáng lẽ phải đổi.

**Pitfalls.** Bọc hàm quanh cột lọc · ghép chuỗi giá trị vào câu lệnh · giả định kế hoạch luôn tối ưu cho mọi tham số · đổ lỗi cho engine khi kế hoạch đóng băng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tìm đúng ≥ 5/6 chỗ phá chỉ mục và sửa được, và tái hiện được hiện tượng kế hoạch xấu theo tham số với số đo chênh lệch.

### Lesson 132 · SQL tuning project - five slow queries `DA`
**Prerequisites.** Lesson 131

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Bài dự án khép module, và nó là bài chuẩn bị trực tiếp cho công việc thật của cả hai vai. Nhận năm truy vấn chậm trên một cơ sở dữ liệu có dữ liệu thật, mỗi truy vấn chậm vì một nguyên nhân khác nhau trong số đã học: ước lượng sai, thiếu chỉ mục, chỉ mục sai thứ tự, điều kiện phá chỉ mục, và tràn bộ nhớ làm việc. Quy trình bắt buộc theo đúng thứ tự: đọc kế hoạch trước, viết giả thuyết, sửa một thứ, đo lại, rồi lặp; cấm sửa nhiều thứ cùng lúc theo đúng kỷ luật ở lesson 60. Nộp cho mỗi truy vấn: kế hoạch trước và sau, số khối đọc, số dòng ước lượng so với thực tế, độ trễ, và một câu nêu tối ưu này dẫn về quan sát nào. Yêu cầu bổ sung quan trọng: **kết quả sau khi tối ưu phải khớp tuyệt đối với kết quả ban đầu**, vì tối ưu làm đổi kết quả là làm hỏng chứ tối ưu.

**Outcome.** Tăng tốc năm truy vấn đạt ngưỡng, mỗi tối ưu dẫn được về một quan sát trong kế hoạch, và kết quả không đổi.

**Đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module thành một quy trình tối ưu có bằng chứng. Kiểm bằng bảng trước sau cộng đối soát kết quả; đạt khi ít nhất bốn truy vấn đạt ngưỡng và mọi kết quả khớp tuyệt đối.

**Lab.** Nhận năm truy vấn chậm. Với mỗi cái, nộp kế hoạch trước và sau, bốn con số, và câu dẫn chứng. Đối soát kết quả từng truy vấn với bản gốc. Rà soát chéo: một học viên khác chọn một tối ưu bất kỳ và bạn phải chỉ ra quan sát dẫn tới nó.

**Pitfalls.** Thêm chỉ mục cho mọi truy vấn · sửa nhiều thứ cùng lúc · tối ưu làm đổi kết quả · nộp số mà không nộp kế hoạch.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** ≥ 4/5 truy vấn đạt ngưỡng, mọi kết quả khớp tuyệt đối với bản gốc, và mọi tối ưu dẫn được về một quan sát trong kế hoạch.

# MODULE M10 · STORAGE ENGINE AND DATABASE OPERATIONS

**Phase 4 · Lessons 133–148 · 32 giờ**

| | |
|---|---|
| **Objective cấp module** | Hiểu đường đi của một lệnh ghi và một lệnh đọc, chọn mức cô lập theo dị thường cần chặn, và vận hành được cơ sở dữ liệu gồm cả khôi phục đã kiểm chứng |
| **Tiền đề** | M4 · M5 · M9 |
| **Exit criterion** | Truy được một lệnh chèn từ câu lệnh tới nhật ký ghi trước, tới trang, tới điểm kiểm tra và tới khôi phục sau sự cố; thực hiện thành công một lần khôi phục thật |
| **Kỹ năng SFIA** | `DBAD` mức 4 · `SYSP` mức 4 |
| **Chế độ hỏng** | Chọn mức cô lập theo tên nghe có vẻ an toàn, và tin vào bản sao lưu chưa bao giờ khôi phục thử |

Module này đóng phần nền cơ sở dữ liệu. Nguyên tắc chấm nghiêm nhất của cả chương trình nằm ở đây: **bản sao lưu chưa khôi phục thử thì không tính là bản sao lưu**, và lesson 147 là buổi diễn tập đó.

Thạo sâu một hệ là PostgreSQL, rồi ánh xạ khác biệt sang các hệ khác; đây là quyết định của bản nguồn và được giữ nguyên, vì học nông nhiều hệ cho ra kiến thức không dùng được lúc sự cố.

### Lesson 133 · Pages, heap files and the buffer pool `LT`
**Prerequisites.** Module 10: M9

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Cơ sở dữ liệu không đọc ghi theo dòng mà theo trang, thường 8 KB, và mọi thứ còn lại suy ra từ đó. Bố cục một trang: phần đầu, mảng con trỏ dòng, và vùng dữ liệu lớn dần từ cuối lên; thiết kế này cho phép dòng đổi kích thước mà không phải dịch chuyển cả trang. Siêu dữ liệu về không gian trống và về khả năng nhìn thấy nằm ngay trong trang. Tệp đống là tập các trang không có thứ tự, nên tìm một dòng không có chỉ mục nghĩa là quét mọi trang. Hồ đệm là bộ đệm trang của riêng cơ sở dữ liệu, tách biệt với bộ đệm trang của hệ điều hành ở lesson 53, nên dữ liệu có thể nằm ở cả hai chỗ và điều đó gây nhầm khi đo. Chính sách loại bỏ trang, trang bẩn, và điểm kiểm tra là ba khái niệm nối trực tiếp sang lesson 137 và 138. **Tỉ lệ trúng hồ đệm là chỉ số hiệu năng hàng đầu**, đọc được từ kế hoạch ở lesson 130.

**Outcome.** Đọc được bố cục một trang thật và giải thích quan hệ giữa hồ đệm với bộ đệm trang của hệ điều hành.

**Đánh giá.** Tầng *hiểu*. Bài mở module, nối kiến thức lưu trữ ở M4 với cấu trúc bên trong cơ sở dữ liệu. Kiểm bằng bài khảo sát trang thật cộng bài giải thích; đạt khi đọc đúng ba thành phần của trang và giải thích đúng hai tầng đệm.

**Lab.** Dùng công cụ khảo sát trang của PostgreSQL để xem một trang thật: phần đầu, con trỏ dòng, và dữ liệu. Chèn thêm dòng và quan sát trang đổi. Đo tỉ lệ trúng hồ đệm cho một truy vấn ở hai trạng thái đệm nguội và đệm ấm. Giải thích vì sao đo lần hai luôn nhanh hơn.

**Pitfalls.** Nghĩ cơ sở dữ liệu đọc theo dòng · nhầm hồ đệm với bộ đệm trang hệ điều hành · đo hiệu năng trên đệm ấm rồi kết luận · bỏ qua tỉ lệ trúng hồ đệm.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đọc đúng ba thành phần của một trang thật, và giải thích đúng hai tầng đệm kèm số đo tỉ lệ trúng ở hai trạng thái.

### Lesson 134 · B-tree internals - fanout, splits and clustering `TH`
**Prerequisites.** Lesson 133

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Chỉ mục ở lesson 129 nay mở ra bên trong. Độ rẽ nhánh quyết định chiều cao cây: mỗi nút là một trang chứa nhiều khoá, nên cây một triệu khoá chỉ cao ba tới bốn mức và tìm một khoá tốn ba tới bốn lần đọc trang. Chèn làm nút đầy thì tách, và tách lan lên trên có thể làm cây cao thêm một mức. Từ đó suy ra hai hiện tượng thực tế: chèn theo khoá tăng dần làm mọi lần chèn dồn vào nút cuối nên nút đó thành điểm nóng, còn chèn ngẫu nhiên thì phân bố đều nhưng làm trang bị phân mảnh. Phình chỉ mục sau nhiều lần xoá và cập nhật, cùng cách dựng lại. Gom cụm vật lý: sắp xếp dữ liệu trên đĩa theo thứ tự một chỉ mục làm truy vấn theo khoảng đọc tuần tự thay vì ngẫu nhiên, và đó là chênh lệch đã đo ở lesson 52; đổi lại chỉ gom cụm được theo một thứ tự.

**Outcome.** Đo được chiều cao cây chỉ mục và chứng minh tác động của thứ tự chèn lên phân mảnh cùng điểm nóng.

**Đánh giá.** Tầng *phân tích*. Objective đòi nối cấu trúc bên trong với hiện tượng đo được. Kiểm bằng hai thí nghiệm chèn; đạt khi đo đúng chiều cao cây và chỉ ra khác biệt giữa hai thứ tự chèn bằng số.

**Lab.** Tạo chỉ mục trên bảng một triệu dòng và đo chiều cao cây cùng kích thước. Chèn 100.000 dòng theo khoá tăng dần rồi theo khoá ngẫu nhiên vào hai bảng riêng; so thông lượng chèn và độ phân mảnh. Xoá 50% dòng và đo phình chỉ mục, rồi dựng lại và đo lại.

**Pitfalls.** Nghĩ chỉ mục là danh sách sắp xếp · bỏ qua phình chỉ mục sau nhiều lần xoá · gom cụm theo nhiều thứ tự cùng lúc · chèn theo khoá tăng dần ở hệ ghi rất nhiều mà không lường điểm nóng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chiều cao cây đo đúng, và chênh lệch giữa hai thứ tự chèn cùng mức phình sau khi xoá đều có số chứng minh.

### Lesson 135 · LSM trees - memtable, SSTable and compaction `LT`
**Prerequisites.** Lesson 134

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Cấu trúc thứ hai, tối ưu cho ghi thay vì đọc, và là cấu trúc của nhiều kho khoá giá trị cùng một số engine phân tích. Cơ chế: ghi vào bảng trong bộ nhớ và vào nhật ký, khi đầy thì đẩy xuống đĩa thành một tệp đã sắp xếp bất biến; đọc phải tra nhiều tệp nên tốn hơn. Bộ lọc Bloom ở lesson 41 dùng đúng ở đây để bỏ qua tệp chắc chắn không chứa khoá. Gộp tệp chạy nền để giảm số tệp phải tra, và đây là nguồn tải vào ra nền mà người vận hành phải biết. So với cây B bằng ba đại lượng khuếch đại ở lesson 136. Nguyên tắc rút ra: **ghi tuần tự luôn rẻ hơn ghi ngẫu nhiên**, theo lesson 52, nên cấu trúc biến mọi lần ghi thành ghi tuần tự thì thắng ở khối lượng ghi nặng, và trả giá ở đọc. Xoá bằng cách ghi thêm dấu xoá chứ xoá tại chỗ, và hệ quả là dung lượng không giảm ngay.

**Outcome.** Giải thích bằng cơ chế vì sao cấu trúc này thắng ở khối lượng ghi nặng và thua ở đọc ngẫu nhiên.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết so sánh hai cấu trúc; phần đo nằm ở lesson 136. Kiểm bằng bài giải thích cộng dự đoán; đạt khi giải thích đúng cơ chế và dự đoán đúng chiều của ba đại lượng khuếch đại.

**Lab.** Đọc cấu trúc thư mục dữ liệu của một kho dùng cấu trúc này: quan sát tệp đã sắp xếp, bộ lọc Bloom, và các mức gộp. Kích hoạt một lần gộp và quan sát tải vào ra. Viết dự đoán về ba đại lượng khuếch đại so với cây B trước khi đo ở bài sau.

**Pitfalls.** Nghĩ cấu trúc này luôn nhanh hơn · quên rằng xoá không giải phóng dung lượng ngay · bỏ qua tải nền do gộp tệp · dùng cho khối lượng đọc ngẫu nhiên nặng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Giải thích đúng cơ chế biến ghi ngẫu nhiên thành ghi tuần tự, và dự đoán đúng chiều của cả ba đại lượng khuếch đại.

### Lesson 136 · Amplification - read, write and space `TH`
**Prerequisites.** Lesson 135

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba đại lượng để so hai cấu trúc lưu trữ một cách khách quan thay vì bằng danh tiếng. Khuếch đại đọc: một lần đọc logic tốn bao nhiêu lần đọc vật lý; cấu trúc gộp theo nhật ký cao hơn vì phải tra nhiều tệp. Khuếch đại ghi: một byte dữ liệu cuối cùng được ghi xuống đĩa bao nhiêu lần; cấu trúc gộp theo nhật ký ghi lại nhiều lần qua các mức gộp, cây B ghi lại khi tách trang và khi ghi nhật ký. Khuếch đại dung lượng: dữ liệu chiếm bao nhiêu lần kích thước logic; cả hai đều có phần dư, một bên do dấu xoá chưa gộp, một bên do trang chưa đầy. **Không có cấu trúc nào tốt cả ba**, nên chọn là chọn đại lượng nào chịu được cao. Cách đo ba đại lượng trên hệ thật, và cách dùng chúng để giải thích vì sao một hệ ghi nặng nên chọn cấu trúc nào.

**Outcome.** Đo được ba đại lượng khuếch đại trên hai engine và chọn engine theo khối lượng công việc cho trước.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn theo ba tiêu chí đối nghịch dựa trên số tự đo. Kiểm bằng bảng ba đại lượng nhân hai engine; đạt khi cả sáu ô có số và lựa chọn dẫn được từ bảng.

**Lab.** Chạy cùng một khối lượng công việc ghi nặng trên PostgreSQL và trên một kho dùng cấu trúc gộp theo nhật ký. Đo cả ba đại lượng khuếch đại cho mỗi bên. Lặp lại với khối lượng đọc ngẫu nhiên nặng. Lập bảng và chọn engine cho hai tình huống cho trước.

**Pitfalls.** So hai engine chỉ bằng thông lượng · bỏ qua khuếch đại dung lượng · đo trong lúc gộp tệp đang chạy nên số bị lệch · kết luận một engine tốt hơn mà không nêu khối lượng công việc.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng ba đại lượng nhân hai engine đủ sáu ô, và lựa chọn cho hai tình huống dẫn được từ số trong bảng.

### Lesson 137 · The write-ahead log and group commit `TH`
**Prerequisites.** Lesson 136

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Quy tắc nền của mọi cơ sở dữ liệu có cam kết bền vững: **ghi nhật ký trước khi ghi dữ liệu**, vì nhật ký là ghi tuần tự nên rẻ, còn ghi dữ liệu là ghi ngẫu nhiên nên đắt. Số thứ tự nhật ký định danh từng bản ghi và cho phép biết trang đã được ghi tới đâu. Một giao dịch được coi là chốt khi bản ghi chốt của nó đã nằm trên đĩa, và đó chính là một lần `fsync` theo lesson 53; đây là lý do vật lý khiến số giao dịch mỗi giây bị chặn bởi tốc độ `fsync`. Chốt theo nhóm là cách vượt giới hạn đó: gom nhiều giao dịch rồi đẩy một lần, nên thông lượng tăng mạnh trong khi độ trễ từng giao dịch tăng nhẹ; đây là đánh đổi cấu hình được. Ba mức cam kết bền vững và giá của từng mức, đo được. Nhật ký cũng là nguồn cho nhân bản ở lesson 143 và cho bắt dữ liệu thay đổi ở M17, nên hiểu nó là hiểu hai thứ sau.

**Outcome.** Đo được quan hệ giữa cấu hình chốt và cặp thông lượng, độ trễ, và phát biểu đúng cam kết bền vững của từng mức.

**Đánh giá.** Tầng *phân tích*. Objective nối một tham số cấu hình với một cam kết ngữ nghĩa và một con số. Kiểm bằng bảng ba mức cộng thí nghiệm mất điện; đạt khi ba cam kết phát biểu đúng và số đo đúng chiều.

**Lab.** Chạy tải ghi ở ba cấu hình bền vững khác nhau, đo thông lượng và độ trễ phân vị 95 cho từng cái. Giết tiến trình cơ sở dữ liệu cứng giữa lúc ghi và đếm số giao dịch đã chốt còn lại ở mỗi cấu hình. Quan sát tệp nhật ký lớn lên và điểm kiểm tra làm nó được tái sử dụng.

**Pitfalls.** Tắt cam kết bền vững trên hệ sản xuất để tăng tốc · nghĩ chốt theo nhóm làm giảm độ trễ · không thử giết tiến trình nên không biết cam kết thật · bỏ qua quan hệ giữa nhật ký và nhân bản.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng ba cấu hình có cả thông lượng lẫn độ trễ, số giao dịch sống sót đúng với cam kết đã phát biểu ở cả ba mức.

### Lesson 138 · Crash recovery - redo, undo and checkpoints `TH`
**Prerequisites.** Lesson 137

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Sau sự cố, cơ sở dữ liệu phải đưa dữ liệu về trạng thái nhất quán, và nó làm bằng đúng hai thao tác. Làm lại: áp lại các thay đổi đã chốt nhưng chưa kịp ghi xuống trang dữ liệu. Huỷ bỏ: gỡ các thay đổi của giao dịch chưa chốt mà đã kịp ghi xuống trang. Điểm kiểm tra giới hạn lượng nhật ký phải đọc lại khi khôi phục: nó đẩy mọi trang bẩn xuống đĩa và ghi một mốc, nên khôi phục chỉ cần đọc từ mốc đó trở đi. Từ đó suy ra đánh đổi cấu hình: điểm kiểm tra dày thì khôi phục nhanh nhưng tải vào ra nền cao; thưa thì ngược lại, và **thời gian khôi phục là một cam kết vận hành chứ một hằng số**. Ba tình huống hỏng và kết quả của từng tình huống: chưa chốt thì mất, đã chốt thì còn, đang chốt thì phụ thuộc bản ghi chốt đã xuống đĩa chưa. Cách đọc nhật ký khôi phục để biết đã làm lại bao nhiêu.

**Outcome.** Dự đoán đúng kết cục của ba tình huống hỏng và đo được quan hệ giữa chu kỳ điểm kiểm tra với thời gian khôi phục.

**Đánh giá.** Tầng *phân tích*. Objective đòi suy kết cục từ cơ chế, rồi kiểm bằng thí nghiệm hỏng. Kiểm bằng ba tình huống cộng bảng hai chu kỳ; đạt khi dự đoán đúng cả ba và bảng cho thấy đúng chiều đánh đổi.

**Lab.** Chạy ba tình huống: giết cơ sở dữ liệu khi có giao dịch chưa chốt, khi vừa chốt xong, và đúng lúc đang chốt. Viết dự đoán trước, rồi khởi động lại và đối chiếu. Đo thời gian khôi phục ở hai chu kỳ điểm kiểm tra khác nhau và ghi tải vào ra nền tương ứng.

**Pitfalls.** Nghĩ khôi phục chỉ có làm lại · đặt điểm kiểm tra rất thưa để giảm tải rồi thời gian khôi phục vượt cam kết · không đo thời gian khôi phục bao giờ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Dự đoán đúng kết cục cả ba tình huống, và bảng hai chu kỳ điểm kiểm tra cho thấy đúng chiều đánh đổi có số.

### Lesson 139 · ACID and the transaction state machine `LT`
**Prerequisites.** Lesson 138

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bốn chữ cái được nhắc nhiều và hiểu sai nhiều, nên bài này định nghĩa từng chữ bằng phản ví dụ chứ bằng định nghĩa trừu tượng. Nguyên tử: giao dịch chuyển tiền đứt giữa chừng thì không được trừ mà không cộng; cơ chế là huỷ bỏ ở lesson 138. Nhất quán: các ràng buộc ở lesson 116 vẫn đúng trước và sau; đây là chữ phụ thuộc vào người thiết kế chứ vào engine. Cô lập: giao dịch chạy song song cho kết quả như thể chạy lần lượt, và đây là chữ có nhiều mức nhất, nội dung của lesson 140 tới 142. Bền vững: đã chốt thì sống sót qua sự cố; cơ chế là nhật ký ghi trước ở lesson 137. Máy trạng thái của một giao dịch và các đường chuyển. Vì sao mức cô lập là thứ duy nhất trong bốn chữ được phép hạ xuống để đổi lấy hiệu năng, và hạ tới đâu là câu hỏi của lesson 142.

**Outcome.** Giải thích mỗi chữ trong bốn chữ bằng một phản ví dụ cụ thể và chỉ ra cơ chế nào bảo đảm nó.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết nối bốn bài trước thành một khung; chuẩn bị cho ba bài sau. Kiểm bằng bài viết phản ví dụ; đạt khi cả bốn có phản ví dụ cụ thể và gắn đúng cơ chế.

**Lab.** Với mỗi chữ trong bốn chữ, viết một phản ví dụ bằng dữ liệu cụ thể và chỉ ra cơ chế nào chặn nó. Với chữ nhất quán, nêu rõ phần nào do engine bảo đảm và phần nào do người thiết kế. Vẽ máy trạng thái của một giao dịch và chỉ ra các đường chuyển quan sát được trong hệ thật.

**Pitfalls.** Coi cả bốn chữ đều do engine bảo đảm tự động · nghĩ mức cô lập mặc định là mức cao nhất · giải thích bằng định nghĩa trừu tượng mà không có phản ví dụ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn phản ví dụ đều cụ thể và gắn đúng cơ chế, và phần nhất quán phân định rõ trách nhiệm engine với trách nhiệm người thiết kế.

### Lesson 140 · Locking, two-phase locking and deadlock detection `TH`
**Prerequisites.** Lesson 139

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Cách thứ nhất để đạt cô lập: chặn truy cập đồng thời bằng khoá. Hai loại khoá và ma trận tương thích; mức chi tiết của khoá từ dòng tới bảng, và đánh đổi giữa mức chi tiết với chi phí quản lý khoá. Khoá hai pha: giai đoạn lấy khoá và giai đoạn nhả khoá không đan xen, và đó là điều kiện để bảo đảm kết quả tương đương chạy lần lượt. Hệ quả vận hành: khoá giữ tới cuối giao dịch, nên **giao dịch dài giữ khoá lâu và chặn người khác**, đây là nguyên nhân số một của hiện tượng cơ sở dữ liệu đột nhiên treo. Khoá chết ở tầng cơ sở dữ liệu: engine phát hiện bằng đồ thị chờ và huỷ một giao dịch làm nạn nhân, nên ứng dụng phải xử lý lỗi bị huỷ và thử lại, theo đúng lesson 104. Cách đọc bảng khoá đang giữ và đang chờ để chẩn đoán một hệ đang bị chặn.

**Outcome.** Chẩn đoán một hệ bị chặn bằng cách đọc khoá đang giữ và đang chờ, và xử lý đúng khi giao dịch bị huỷ làm nạn nhân.

**Đánh giá.** Tầng *phân tích*. Objective là chẩn đoán một sự cố hay gặp và khó đoán từ bên ngoài. Kiểm bằng hai tình huống tiêm sẵn tính giờ; đạt khi định vị đúng giao dịch chặn ở cả hai và xử lý đúng lỗi bị huỷ.

**Lab.** Mở một giao dịch dài không chốt rồi chạy tải; quan sát hệ treo và dùng khung nhìn khoá để định vị giao dịch chặn. Tạo khoá chết giữa hai giao dịch, đọc thông báo và xác định nạn nhân. Cài xử lý thử lại cho lỗi bị huỷ và chạy 1000 lần chứng minh không mất giao dịch nào.

**Pitfalls.** Khởi động lại cơ sở dữ liệu để gỡ treo · không xử lý lỗi bị huỷ nên mất giao dịch · giữ giao dịch mở trong lúc chờ người dùng · đặt mức khoá bảng cho thao tác chỉ cần khoá dòng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Định vị đúng giao dịch chặn ở cả hai tình huống, và sau khi cài thử lại thì 1000 lần chạy không mất giao dịch nào.

### Lesson 141 · MVCC, snapshots and vacuum `TH`
**Prerequisites.** Lesson 140

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Cách thứ hai để đạt cô lập, và là cách PostgreSQL dùng: thay vì chặn, giữ nhiều phiên bản của một dòng để người đọc thấy ảnh chụp tại thời điểm giao dịch bắt đầu. Hệ quả lớn nhất và là lý do cách này thắng trong hệ phân tích: **người đọc không chặn người ghi và ngược lại**. Cái giá là phiên bản cũ tích tụ và phải dọn. Dọn rác cơ sở dữ liệu đánh dấu phiên bản không ai còn thấy là dùng lại được; không chạy hoặc chạy không kịp thì bảng phình và truy vấn chậm dần. Chi tiết quyết định vận hành: **một giao dịch mở rất lâu giữ ảnh chụp cũ, nên không phiên bản nào sau đó dọn được**, và đây là nguyên nhân kinh điển của bảng phình mà không ai hiểu vì sao. Quấn số giao dịch ở mức nhận biết và vì sao nó có thể buộc dừng cơ sở dữ liệu. Ba chỉ số phải theo dõi: tuổi giao dịch cũ nhất, mức phình, và tiến độ dọn.

**Outcome.** Tái hiện được hiện tượng giao dịch dài chặn việc dọn rác và đo mức phình bảng gây ra.

**Đánh giá.** Tầng *phân tích*. Objective đòi nối một hành vi ứng dụng với một hậu quả vận hành, chỗ rất khó đoán nếu không biết cơ chế. Kiểm bằng thí nghiệm có đo; đạt khi tái hiện được hiện tượng và ba chỉ số theo dõi cho thấy đúng nguyên nhân.

**Lab.** Mở một giao dịch và để nguyên không chốt. Chạy tải cập nhật liên tục trong 20 phút. Đo mức phình bảng và tuổi giao dịch cũ nhất theo thời gian. Chốt giao dịch kia rồi chạy dọn và đo lại. Dựng cảnh báo trên ba chỉ số.

**Pitfalls.** Tin rằng dọn tự động luôn đủ · để giao dịch mở lâu trong mã ứng dụng · dùng lệnh dọn toàn phần trên bảng lớn đang có tải · chỉ theo dõi dung lượng mà không theo dõi tuổi giao dịch.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tái hiện được mức phình tăng khi có giao dịch dài, và sau khi chốt thì dọn đưa mức phình về, cả hai có số đo theo thời gian.

### Lesson 142 · Isolation levels chosen by anomaly, not by name `TH`
**Prerequisites.** Lesson 141

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài quan trọng nhất của phần giao dịch, và nguyên tắc của nó nằm ngay trong tiêu đề: **chọn mức cô lập theo dị thường cần chặn, không theo tên mức nghe có vẻ an toàn**. Năm dị thường và định nghĩa bằng kịch bản cụ thể: đọc bẩn, đọc không lặp lại, dòng ma, cập nhật mất, và lệch ghi. Hai dị thường cuối là hai dị thường mà người mới gần như không biết tới. Cập nhật mất đã gặp ở lesson 104. Lệch ghi tinh vi hơn: hai giao dịch đọc cùng một điều kiện, mỗi cái ghi một dòng khác nhau, cả hai đều hợp lệ khi xét riêng nhưng kết quả chung vi phạm một bất biến; ví dụ kinh điển là hai bác sĩ cùng xin nghỉ ca trực khi quy định phải còn ít nhất một người. Bảng ánh xạ mức cô lập với dị thường còn lại, kèm cảnh báo rằng cùng một tên mức có hành vi khác nhau giữa các engine. Ba cách chặn lệch ghi.

**Outcome.** Tái hiện cập nhật mất và lệch ghi ở các mức cô lập, rồi chọn cơ chế chặn đúng theo bất biến cần giữ.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn theo dị thường chứ theo tên, và là chỗ nhiều hệ thật chọn sai. Kiểm bằng hai thí nghiệm tái hiện cộng bài chọn; đạt khi tái hiện được cả hai dị thường và chọn đúng cơ chế chặn cho ba bất biến cho trước.

**Lab.** Tái hiện cập nhật mất và lệch ghi bằng hai phiên chạy song song. Thử lại ở từng mức cô lập và lập bảng dị thường nào còn ở mức nào. Cho ba bất biến nghiệp vụ, chọn mức cô lập hoặc cơ chế khoá để chặn, và chứng minh bằng phép kiểm chạy song song.

**Pitfalls.** Chọn mức cô lập theo tên · nghĩ mức cao nhất luôn là lựa chọn đúng · cho rằng cùng tên mức thì cùng hành vi giữa các engine · kiểm bằng phép chạy tuần tự.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tái hiện được cả hai dị thường, bảng ánh xạ đúng, và ba bất biến đều được chặn có phép kiểm chạy song song chứng minh.

### Lesson 143 · Replication, lag, failover and split brain `TH`
**Prerequisites.** Lesson 142

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Nhân bản phục vụ ba mục đích khác nhau đã nêu ở góc nhìn hệ thống, nay nhìn từ cơ sở dữ liệu. Hai cách nhân bản: theo nhật ký vật lý sao chép byte của nhật ký ghi trước ở lesson 137 nên bản sao giống hệt bản chính; theo nhật ký logic giải mã thành sự kiện có nghĩa nên nhân bản chọn lọc được và đây chính là cơ chế bắt dữ liệu thay đổi. Đồng bộ và bất đồng bộ: đồng bộ không mất dữ liệu khi bản chính chết nhưng neo độ trễ ghi vào bản sao chậm nhất; bất đồng bộ nhanh nhưng có cửa sổ mất dữ liệu, và cửa sổ đó chính là mục tiêu điểm khôi phục. Độ trễ bản sao và hệ quả đọc không thấy thứ vừa ghi. Chuyển đổi khi hỏng và hai rủi ro: não phân đôi khi hai nút cùng tin mình là bản chính, và cần cơ chế rào chặn nút cũ. Kiểm tra bản sao có thật sự bắt kịp chứ chỉ còn kết nối.

**Outcome.** Đo được độ trễ bản sao dưới tải và thực hiện một lần chuyển đổi có đo lượng dữ liệu mất.

**Đánh giá.** Tầng *áp dụng*. Objective là một thao tác vận hành có hai số đo. Kiểm bằng lần chuyển đổi thật; đạt khi đo được độ trễ dưới tải và lượng dữ liệu mất khớp với cấu hình đã chọn.

**Lab.** Dựng một bản chính và một bản sao bất đồng bộ. Chạy tải ghi và đo độ trễ bản sao. Đọc ngay sau khi ghi trên bản sao và tái hiện hiện tượng không thấy. Giết bản chính, chuyển đổi, và đếm số giao dịch mất. Lặp lại với nhân bản đồng bộ và so hai con số.

**Pitfalls.** Đọc bản sao cho bước đối soát · nghĩ bản sao còn kết nối là còn bắt kịp · chuyển đổi mà không rào chặn nút cũ · không đo độ trễ bản sao dưới tải thật.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Có số đo độ trễ bản sao dưới tải, và lượng dữ liệu mất khi chuyển đổi khớp với cam kết của cấu hình ở cả hai chế độ.

### Lesson 144 · Partitioning against sharding `LT`
**Prerequisites.** Lesson 143

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Hai kỹ thuật chia dữ liệu hay bị gọi lẫn nhưng khác nhau ở một điểm quyết định: phân vùng chia trong một hệ, còn phân mảnh chia sang nhiều hệ, nên phân mảnh kéo theo mọi vấn đề của hệ phân tán. Phân vùng theo khoảng, theo danh sách và theo băm; lợi ích thật là cắt bớt phân vùng khi truy vấn có điều kiện trên khoá phân vùng, và bảo trì theo phân vùng như xoá cả một tháng bằng một thao tác. Chọn khoá phân vùng theo mẫu truy vấn chứ theo trực giác, cùng nguyên tắc sẽ gặp ở M13. Phân mảnh: định tuyến yêu cầu tới mảnh đúng, cân bằng lại khi thêm mảnh, khoá nóng, và **giao dịch bắc qua nhiều mảnh là thứ tốn kém nhất và nên tránh bằng thiết kế**. Ba dấu hiệu cho thấy thật sự cần phân mảnh, và cảnh báo rằng phần lớn hệ dữ liệu ở quy mô vừa không cần, cùng lập luận sẽ gặp lại ở M15.

**Outcome.** Chọn giữa phân vùng và phân mảnh cho ba tình huống và nêu khoá chia cùng hệ quả lên truy vấn.

**Đánh giá.** Tầng *đánh giá*. Objective đòi phân biệt hai kỹ thuật và chống việc phân mảnh quá sớm. Kiểm bằng ba tình huống trong đó ít nhất hai chỉ cần phân vùng; đạt khi chọn đúng cả ba và nêu đúng khoá chia.

**Lab.** Phân vùng một bảng 50 triệu dòng theo tháng. Đo chênh lệch byte quét giữa truy vấn có và không có điều kiện trên khoá phân vùng. Xoá một tháng bằng thao tác phân vùng và so thời gian với lệnh xoá thường. Cho ba tình huống và quyết định phân vùng hay phân mảnh.

**Pitfalls.** Phân mảnh khi phân vùng đủ · chọn khoá phân vùng không xuất hiện trong điều kiện lọc · thiết kế để mọi truy vấn phải hỏi mọi mảnh · bỏ qua chi phí cân bằng lại.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Có số đo chênh lệch byte quét khi cắt phân vùng, và ba tình huống được quyết định đúng kèm khoá chia.

### Lesson 145 · Backup, PITR and what a backup is not `LT`
**Prerequisites.** Lesson 144

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Hai loại sao lưu và điều kiện dùng: sao lưu logic xuất ra câu lệnh nên di chuyển được giữa phiên bản và hệ, nhưng chậm và khôi phục lâu; sao lưu vật lý sao chép tệp nên nhanh, đổi lại gắn với phiên bản và kiến trúc. Khôi phục tới một thời điểm: kết hợp một bản sao lưu vật lý với chuỗi nhật ký ghi trước ở lesson 137 để đưa cơ sở dữ liệu về đúng một mốc, và đây là thứ cứu được tình huống xoá nhầm bảng lúc mười giờ sáng. Hai mục tiêu quyết định thiết kế: chịu mất bao nhiêu dữ liệu và chịu ngừng bao lâu; cả hai do nghiệp vụ quyết chứ kỹ thuật tự đặt. Bốn thứ hay bị quên khỏi kế hoạch sao lưu và đều làm nó thất bại đúng lúc cần: cấu hình, bí mật, phần mở rộng, và chính người biết quy trình. **Quy tắc không thoả hiệp: bản sao lưu chưa khôi phục thử thì chưa phải bản sao lưu**, và lesson 146 là buổi diễn tập.

**Outcome.** Thiết kế kế hoạch sao lưu từ hai mục tiêu nghiệp vụ và nêu bốn thứ phải có ngoài dữ liệu.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết chuẩn bị cho buổi diễn tập ở lesson 146. Kiểm bằng bản kế hoạch; đạt khi hai mục tiêu được nối với tần suất sao lưu cụ thể và nêu đủ bốn thứ hay quên.

**Lab.** Phỏng vấn một người đóng vai nghiệp vụ để chốt hai mục tiêu. Từ đó suy ra tần suất sao lưu đầy đủ, tần suất lưu nhật ký, và thời gian giữ. Lập danh mục mọi thứ phải sao lưu ngoài dữ liệu. Ước lượng dung lượng và chi phí lưu trữ cho ba tháng.

**Pitfalls.** Kỹ thuật tự đặt hai mục tiêu · chỉ sao lưu dữ liệu mà quên cấu hình và bí mật · đặt thời gian giữ nhật ký ngắn hơn khoảng cách giữa hai lần sao lưu đầy đủ · chưa từng tính dung lượng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Hai mục tiêu được nối với tần suất cụ thể, danh mục nêu đủ bốn thứ ngoài dữ liệu, và có ước lượng dung lượng ba tháng.

### Lesson 146 · The restore drill `TH`
**Prerequisites.** Lesson 145

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Buổi diễn tập, và đây là bài mà bỏ qua thì cả module vô nghĩa. Kịch bản: mười giờ sáng có người chạy nhầm lệnh xoá một bảng quan trọng trên hệ sản xuất; nhiệm vụ là khôi phục về trạng thái ngay trước thời điểm đó, trên một máy mới, với cơ sở dữ liệu vẫn đang nhận ghi từ các bảng khác. Quy trình sáu bước và mỗi bước có điểm kiểm chứng riêng. Hai đại lượng phải đo trong lúc làm chứ ước lượng sau: thời gian từ lúc bắt đầu tới lúc phục vụ lại được, và lượng dữ liệu mất thật. So hai con số đo được với hai mục tiêu đã chốt ở lesson 145, và **nếu không đạt thì kế hoạch sai chứ buổi diễn tập sai**. Ba tình huống phát sinh hay gặp trong lúc khôi phục: thiếu phần mở rộng, sai phiên bản, và hết dung lượng đĩa. Viết lại quy trình thành sổ tay sau buổi diễn tập theo chuẩn ở lesson 10.

**Outcome.** Khôi phục thành công về một mốc thời gian trên máy mới, đo hai đại lượng, và so với hai mục tiêu đã chốt.

**Đánh giá.** Tầng *áp dụng*. Objective là một thao tác vận hành có hai số đo so với cam kết. Kiểm bằng buổi diễn tập tính giờ cộng đối soát dữ liệu; đạt khi dữ liệu khôi phục khớp trạng thái tại mốc và hai số đo được ghi lại.

**Lab.** Chạy buổi diễn tập theo kịch bản. Khôi phục về mốc ngay trước lệnh xoá nhầm, trên máy mới. Đối soát dữ liệu với bản chụp đã lưu trước đó. Đo cả hai đại lượng. So với hai mục tiêu và ghi rõ chỗ không đạt. Viết sổ tay khôi phục từ chính quy trình vừa làm.

**Pitfalls.** Khôi phục trên chính máy đang hỏng · bỏ qua bước đối soát sau khi khôi phục · ước lượng thời gian thay vì đo · không ghi lại quy trình nên lần sau làm lại từ đầu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Dữ liệu khôi phục khớp trạng thái tại mốc, hai đại lượng được đo và so với mục tiêu, và sổ tay viết ra từ quy trình thật.

### Lesson 147 · Operating a database day to day `TH`
**Prerequisites.** Lesson 146

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Sáu việc vận hành định kỳ và chỉ số đi kèm từng việc. Kết nối và hồ kết nối: số kết nối tối đa là tài nguyên hữu hạn, và mỗi kết nối tốn bộ nhớ, nên hồ đặt ở phía ứng dụng theo lesson 103 là bắt buộc chứ tuỳ chọn. Truy vấn chậm: bật ghi nhật ký truy vấn vượt ngưỡng và rà định kỳ, đây là nguồn đầu vào cho việc tối ưu ở lesson 132. Phình bảng và dọn rác theo lesson 141. Thống kê theo lesson 128, và lịch cập nhật sau các đợt nạp lớn. Dung lượng: theo dõi tốc độ tăng chứ mức hiện tại, để biết trước khi đầy chứ lúc đầy. Nâng cấp: nâng cấp nhỏ và nâng cấp lớn khác nhau ở chỗ có cần chuyển đổi định dạng dữ liệu không, và nâng cấp lớn cần kế hoạch cùng đường lùi theo lesson 98. Bốn cảnh báo tối thiểu một cơ sở dữ liệu sản xuất phải có.

**Outcome.** Dựng bộ theo dõi sáu việc vận hành với ngưỡng cảnh báo có căn cứ và rà được truy vấn chậm.

**Đánh giá.** Tầng *áp dụng*. Objective là một cấu hình vận hành kiểm được bằng việc phát hiện sự cố trước khi người dùng báo. Kiểm bằng bốn sự cố tiêm sẵn; đạt khi cảnh báo phát hiện ít nhất ba trước khi tác động tới truy vấn.

**Lab.** Dựng theo dõi cho sáu việc. Đặt bốn cảnh báo tối thiểu với ngưỡng dẫn từ phân bố đo được chứ số tròn. Giảng viên tiêm bốn sự cố: cạn kết nối, phình bảng, thống kê cũ, và dung lượng tăng nhanh bất thường. Ghi cảnh báo nào phát hiện được và phát hiện trước bao lâu.

**Pitfalls.** Đặt ngưỡng bằng số tròn · theo dõi dung lượng hiện tại mà không theo dõi tốc độ tăng · không giới hạn số kết nối ở phía ứng dụng · nâng cấp lớn mà không có đường lùi.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Cảnh báo phát hiện ≥ 3/4 sự cố trước khi tác động tới truy vấn, và mọi ngưỡng dẫn được từ phân bố đo được.

### Lesson 148 · Gate 4 - trace a write and defend an isolation choice `KT`
**Prerequisites.** Lesson 147

**In-class (120 phút).** 75 phút làm bài độc lập · 45 phút chữa bài và phân tích lỗi theo nhóm

**Learn.** Cổng của Phase 4. Bài kiểm hai năng lực: viết và tối ưu SQL có bằng chứng ở M9, và hiểu cùng vận hành cơ sở dữ liệu ở M10. Không có nội dung mới.

**Outcome.** Truy được đường đi của một lệnh ghi từ câu lệnh tới khôi phục, bảo vệ một lựa chọn mức cô lập theo dị thường, và khôi phục thành công.

**Đánh giá.** Tầng *đánh giá*. Cổng đo năng lực tổng hợp gồm cả một thao tác vận hành có rủi ro thật, nên hình thức là bài làm cộng diễn tập.

**Lab.** Buổi 120 phút: 75 phút làm bài độc lập, 45 phút chữa bài. Bài chấm sáu phần: A (20đ) truy đường đi của một lệnh chèn từ câu lệnh tới nhật ký ghi trước, tới trang, tới điểm kiểm tra và tới khôi phục · B (20đ) tối ưu hai truy vấn chậm, mỗi tối ưu dẫn về một quan sát trong kế hoạch và kết quả khớp tuyệt đối · C (20đ) chọn mức cô lập cho hai bất biến cho trước và chứng minh bằng phép kiểm chạy song song · D (20đ) khôi phục về một mốc thời gian và đối soát khớp · E (10đ) chẩn đoán một hệ đang bị chặn bằng khung nhìn khoá · F (10đ) nêu ba chỉ số vận hành phải theo dõi và ngưỡng dẫn từ phân bố.

**Pitfalls.** Chọn mức cô lập theo tên · tối ưu làm đổi kết quả · bỏ phần khôi phục vì tốn thời gian · chứng minh bất biến bằng phép chạy tuần tự.

**Self-study (2,4 giờ).** Không có bài tự học. Nếu không đạt, theo phụ lục khắc phục khi không đạt cổng

**Done when.** Đạt ≥ 70/100, phần C và D đều ≥ 60%. Bất biến chỉ chứng minh bằng phép chạy tuần tự thì phần C bằng không; khôi phục không đối soát thì phần D bằng không.

# MODULE M11 · DATA MODELING - OPERATIONAL, ANALYTICAL AND DOMAIN

**Phase 5 · Lessons 149–164 · 32 giờ**

| | |
|---|---|
| **Objective cấp module** | Chọn hạt, khoá, cách lưu lịch sử và phương pháp mô hình hoá dựa trên khối lượng công việc, yêu cầu quản trị và khả năng tiến hoá |
| **Tiền đề** | M9 · M10 |
| **Exit criterion** | Mọi bảng sự kiện phát biểu hạt bằng một câu không mơ hồ; phép kết không đổi hạt ngoài ý muốn; chọn phương pháp theo chi phí thay đổi, kiểm toán, truy vấn và đội |
| **Kỹ năng SFIA** | `DATM` mức 4 · `DTAN` mức 4 |
| **Chế độ hỏng** | Vẽ lược đồ sao theo mẫu có sẵn mà không phát biểu hạt, rồi phép kết nhân dòng và mọi chỉ số bị thổi phồng mà không ai phát hiện |

Module này là bản lề của cả chương trình gộp: mọi thứ phía trước phục vụ nó, và M11B cùng M11C xây thẳng trên nó.

Khái niệm **hạt** đặt ở lesson 120 nay trở thành công cụ thiết kế chứ chỉ là kỷ luật viết truy vấn. Quy tắc giữ nguyên: một dòng đại diện cho cái gì, phát biểu bằng một câu, và phát biểu trước khi nghĩ tới cột.

Bốn phương pháp được dạy để **chọn**, không để áp dụng cả bốn: chuẩn hoá cho hệ giao dịch, mô hình chiều cho phân tích, Data Vault ở mức nhận ra, và bảng rộng cho tốc độ tiêu thụ.

### Lesson 149 · From requirement to model - the seven-step protocol `LT`
**Prerequisites.** Module 11: M10

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài mở module bằng một quy trình có thứ tự cố định, vì bỏ bước hoặc đảo bước là nguồn của phần lớn mô hình sai. Bảy bước: gọi tên quy trình nghiệp vụ và sự kiện, **phát biểu hạt trước khi nghĩ tới cột**, xác định danh tính tự nhiên và nhu cầu khoá thay thế, định nghĩa độ đo cùng chiều và ngữ nghĩa thời gian, mô hình hoá hiệu chỉnh cùng dữ liệu tới muộn cùng xoá, ánh xạ mẫu truy cập và khối lượng ghi đọc, rồi mới chọn phương pháp. Bước cuối nằm cuối là chủ ý: chọn phương pháp trước rồi ép bài toán vào nó là cách làm ra lược đồ sao cho một bài toán không phải phân tích. Ba câu hỏi phải trả lời được trước khi rời bước hai, vì hạt sai thì sáu bước sau đều sai theo. Nối với lesson 89: từ vựng miền là đầu vào của bước một.

**Outcome.** Chạy đủ bảy bước trên một mô tả nghiệp vụ và dừng lại được ở bước hai với một phát biểu hạt không mơ hồ.

**Đánh giá.** Tầng *áp dụng*. Bài mở module, áp một quy trình có sẵn vào tình huống mới. Kiểm bằng rà soát chéo phát biểu hạt; đạt khi hai người đọc cùng một phát biểu hiểu giống nhau ở cả ba mô tả nghiệp vụ.

**Lab.** Cho ba mô tả nghiệp vụ. Với mỗi cái, chạy đủ bảy bước và nộp kết quả từng bước. Đổi bài: người khác đọc phát biểu hạt của bạn và viết lại bằng lời của họ; nếu hai bản khác nghĩa thì phát biểu còn mơ hồ và phải sửa.

**Pitfalls.** Nghĩ tới cột trước khi chốt hạt · chọn lược đồ sao rồi mới đọc yêu cầu · bỏ bước mô hình hoá hiệu chỉnh và dữ liệu tới muộn · viết hạt bằng một cụm danh từ thay vì một câu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba phát biểu hạt đều được người đọc thứ hai diễn đạt lại đúng nghĩa, và cả bảy bước có kết quả ghi ra.

### Lesson 150 · Declaring the grain before the columns `TH`
**Prerequisites.** Lesson 149

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài dành riêng cho bước hai vì nó là bước quyết định. Hạt là câu trả lời cho một dòng trong bảng này đại diện cho cái gì, và câu đó phải chặt tới mức không hai người hiểu khác nhau. Ba mức chặt và khác biệt hậu quả: một dòng là một đơn hàng, một dòng là một dòng hàng trong đơn, một dòng là một lần thay đổi trạng thái của dòng hàng; ba mức cho ba bảng khác nhau và trộn chúng là gốc của mọi lỗi nhân dòng. Kiểm chứng hạt bằng thực nghiệm chứ bằng niềm tin: đếm dòng theo tập khoá được tuyên bố là duy nhất, và nếu có nhóm nào nhiều hơn một dòng thì hạt đã phát biểu sai. Hạt và khoá liên quan nhưng khác nhau: khoá là cách nhận dạng một dòng, hạt là ý nghĩa của một dòng. Phép kết đổi hạt là hiện tượng đã gặp ở lesson 119, nay có tên gọi và có cách chặn.

**Outcome.** Phát biểu hạt cho năm bảng và kiểm chứng từng phát biểu bằng phép đếm trên dữ liệu thật.

**Đánh giá.** Tầng *áp dụng*. Objective có phép kiểm chứng khách quan bằng truy vấn, chứ dựa vào cảm nhận. Kiểm bằng phép đếm trùng; đạt khi cả năm phát biểu được dữ liệu xác nhận hoặc bị bác bỏ và sửa lại đúng.

**Lab.** Cho năm bảng có dữ liệu thật, không kèm tài liệu. Với mỗi bảng, suy ra hạt từ dữ liệu, viết phát biểu, rồi kiểm bằng cách đếm dòng theo tập khoá tuyên bố. Với bảng nào phát biểu sai, sửa lại và kiểm lần nữa. Ghi lại bảng nào có hạt khác với tên bảng gợi ý.

**Pitfalls.** Tin tên bảng nói đúng hạt · phát biểu hạt rồi không kiểm bằng dữ liệu · nhầm hạt với khoá chính · chấp nhận phát biểu có từ mơ hồ như thông tin hay dữ liệu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Cả năm phát biểu được kiểm bằng phép đếm, và mọi phát biểu sai đều được phát hiện rồi sửa đúng.

### Lesson 151 · Conceptual, logical and physical models `LT`
**Prerequisites.** Lesson 150

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Ba tầng mô hình phục vụ ba người đọc khác nhau, và trộn chúng làm cả ba không dùng được. Mô hình khái niệm nói về khái niệm nghiệp vụ và quan hệ giữa chúng, không có kiểu dữ liệu, dùng để thống nhất với người nghiệp vụ. Mô hình logic có thuộc tính, khoá và ràng buộc, chưa gắn với hệ cụ thể. Mô hình vật lý có kiểu dữ liệu, chỉ mục, phân vùng và quyết định lưu trữ, gắn chặt với engine. Từ đó suy ra một quy tắc thực dụng: đổi engine chỉ nên ảnh hưởng tầng vật lý; nếu phải sửa cả tầng logic thì mô hình đã lẫn tầng. Chuẩn hoá theo lesson 117 là quyết định ở tầng logic, còn phi chuẩn hoá thường là quyết định ở tầng vật lý cho một đường đọc cụ thể. Ba sai lầm khi vẽ sơ đồ quan hệ cho người nghiệp vụ xem.

**Outcome.** Tách một mô hình lẫn tầng thành ba tầng và chỉ ra quyết định nào thuộc tầng nào.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết đặt khung cho phần còn lại của module. Kiểm bằng bài phân tầng 15 quyết định; đạt khi phân đúng ít nhất 12 và giải thích được ba quyết định biên.

**Lab.** Cho một tài liệu thiết kế lẫn cả ba tầng. Tách thành ba mô hình riêng. Cho 15 quyết định thiết kế cụ thể và phân mỗi cái vào một tầng. Với ba quyết định nằm ở ranh giới, viết một câu giải thích vì sao đặt ở tầng đó.

**Pitfalls.** Đưa kiểu dữ liệu vào mô hình khái niệm · đưa quyết định chỉ mục vào mô hình logic · vẽ một sơ đồ duy nhất rồi dùng cho cả ba người đọc.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân đúng ≥ 12/15 quyết định vào tầng, và ba quyết định biên có giải thích hợp lý.

### Lesson 152 · Keys - natural, surrogate and identity over time `TH`
**Prerequisites.** Lesson 151

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Khoá tự nhiên đến từ nghiệp vụ, khoá thay thế do hệ sinh ra, và chọn sai gây hậu quả kéo dài. Ba lý do kho phân tích cần khoá thay thế: khoá tự nhiên có thể đổi, có thể trùng giữa các nguồn, và có thể rất dài nên tốn khi kết. Nhưng khoá thay thế không thay thế khoá tự nhiên mà đi kèm: **khoá nghiệp vụ vẫn phải lưu và vẫn phải có ràng buộc duy nhất**, vì đối soát với nguồn dựa trên nó chứ trên số do ta tự sinh. Phạm vi duy nhất theo thời gian là chỗ tinh vi: một mã khách duy nhất tại một thời điểm nhưng có thể được cấp lại sau khi khách cũ đóng tài khoản, nên duy nhất theo thời gian khác duy nhất tuyệt đối. Khoá băm và đánh đổi: tiện vì tính được ở nhiều nơi, rủi ro khi thành phần băm có giá trị thiếu vì kết quả không xác định. Danh tính tách và gộp: khi hai bản ghi hoá ra là một người, hoặc một bản ghi hoá ra là hai.

**Outcome.** Thiết kế bộ khoá cho một bảng chiều có danh tính đổi theo thời gian và xử lý được một lần gộp danh tính.

**Đánh giá.** Tầng *áp dụng*. Objective là một thiết kế có ca biên cụ thể kiểm được. Kiểm bằng ba ca biên; đạt khi cả ba được xử lý đúng và đối soát theo khoá nghiệp vụ vẫn khớp sau khi gộp.

**Lab.** Thiết kế khoá cho bảng chiều khách hàng. Xử lý ba ca: mã khách đổi, mã khách được cấp lại cho người khác, và hai bản ghi được xác định là cùng một người. Với mỗi ca, chứng minh dữ liệu lịch sử vẫn truy được và đối soát theo khoá nghiệp vụ vẫn khớp.

**Pitfalls.** Bỏ khoá nghiệp vụ vì đã có khoá thay thế · băm từ cột có thể thiếu giá trị · giả định mã nghiệp vụ không bao giờ được cấp lại · xử lý gộp danh tính bằng cách xoá một bản ghi.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba ca biên được xử lý đúng, dữ liệu lịch sử vẫn truy được, và đối soát theo khoá nghiệp vụ khớp sau khi gộp.

### Lesson 153 · Dimensional modelling - facts, dimensions and the bus matrix `LT`
**Prerequisites.** Lesson 152

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Mô hình chiều tối ưu cho việc đọc và cho việc người không chuyên hiểu được, nên nó là dạng chính của tầng phục vụ. Bảng sự kiện chứa khoá ngoại và độ đo, không chứa thuộc tính mô tả; bảng chiều rộng, phi chuẩn hoá, giàu thuộc tính, và **cố ý lặp dữ liệu** vì lặp ở chiều rẻ hơn nhiều so với phải kết thêm bảng. Đây là chỗ mâu thuẫn có chủ đích với chuẩn hoá ở lesson 117, và lý do là hai hệ tối ưu cho hai việc khác nhau. Ma trận xe buýt: bảng liệt kê quy trình nghiệp vụ theo hàng và chiều theo cột, đánh dấu chiều nào dùng ở quy trình nào; nó là công cụ lập kế hoạch cho cả kho chứ chỉ cho một mart. Chiều dùng chung là khái niệm quan trọng nhất của ma trận: cùng một bảng chiều dùng ở nhiều bảng sự kiện thì hai mart so sánh được với nhau; thiếu nó thì mỗi phòng một con số.

**Outcome.** Dựng ma trận xe buýt cho một miền nghiệp vụ và chỉ ra chiều nào phải dùng chung.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết đặt khung cho bốn bài thực hành sau. Kiểm bằng ma trận cộng bài lập luận; đạt khi ma trận phủ đủ quy trình và chỉ đúng ít nhất ba chiều phải dùng chung kèm hậu quả nếu không.

**Lab.** Từ mô tả một doanh nghiệp bán lẻ, liệt kê sáu quy trình nghiệp vụ và các chiều. Dựng ma trận xe buýt. Chỉ ra chiều nào dùng ở nhiều quy trình và phải dùng chung. Với một chiều, mô tả cụ thể chuyện gì xảy ra nếu hai mart tự dựng bản riêng.

**Pitfalls.** Đưa thuộc tính mô tả vào bảng sự kiện · chuẩn hoá bảng chiều vì thấy lặp dữ liệu · dựng mart rời nhau không có chiều dùng chung · vẽ ma trận mà không xác định quy trình nghiệp vụ trước.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ma trận phủ đủ sáu quy trình, chỉ đúng ≥ 3 chiều phải dùng chung, và mô tả được hậu quả cụ thể khi không dùng chung.

### Lesson 154 · Fact types - transaction, periodic and accumulating snapshot `TH`
**Prerequisites.** Lesson 153

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba loại bảng sự kiện trả lời ba loại câu hỏi, và chọn sai loại là không trả lời được câu hỏi chứ chỉ chậm. Bảng giao dịch: một dòng một sự kiện xảy ra, hạt mịn nhất, trả lời câu hỏi chuyện gì đã xảy ra. Bảng ảnh chụp định kỳ: một dòng một thực thể tại một kỳ, dùng cho số dư và tồn kho tức những đại lượng không cộng được theo thời gian. Bảng ảnh chụp tích luỹ: một dòng một quy trình có nhiều mốc, mỗi mốc một cột thời gian, và dòng được cập nhật khi quy trình tiến triển; dùng cho vòng đời đơn hàng và để tính thời gian giữa các mốc. Loại thứ ba là loại khác biệt nhất vì nó **cập nhật dòng đã tồn tại** thay vì chỉ thêm, nên kéo theo yêu cầu về ghi bất biến và về chạy bù. Bảng sự kiện không độ đo cho việc đếm sự kiện hoặc ghi nhận quan hệ.

**Outcome.** Chọn đúng loại bảng sự kiện cho bốn câu hỏi nghiệp vụ và dựng được một bảng ảnh chụp tích luỹ có chạy bù.

**Đánh giá.** Tầng *áp dụng*. Objective là chọn theo câu hỏi rồi cài đặt loại khó nhất. Kiểm bằng bốn câu hỏi cộng bài dựng; đạt khi chọn đúng cả bốn và bảng tích luỹ chạy bù cho kết quả khớp tuyệt đối.

**Lab.** Cho bốn câu hỏi nghiệp vụ. Chọn loại bảng sự kiện cho từng câu kèm lý do. Dựng bảng ảnh chụp tích luỹ cho vòng đời đơn hàng với năm mốc. Chạy bù 30 ngày và đối soát với bản chạy tuần tự. Tính thời gian trung bình giữa hai mốc bất kỳ.

**Pitfalls.** Dùng bảng giao dịch cho câu hỏi về số dư · dựng bảng tích luỹ mà không bất biến khi chạy lại · trộn hai loại vào một bảng · quên rằng số dư không cộng được theo thời gian.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chọn đúng cả bốn câu hỏi, và bảng tích luỹ chạy bù 30 ngày đối soát khớp tuyệt đối.

### Lesson 155 · Additivity - additive, semi-additive and non-additive measures `TH`
**Prerequisites.** Lesson 154

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phân loại quyết định độ đo được phép cộng theo chiều nào, và bỏ qua nó là nguồn của những con số sai mà trông hợp lý. Cộng được hoàn toàn: doanh thu cộng được theo mọi chiều gồm cả thời gian. Cộng được một phần: số dư và tồn kho cộng được theo chiều khác nhưng **không cộng được theo thời gian**, vì cộng số dư của mười hai tháng không ra số dư năm; cách xử lý đúng là lấy giá trị cuối kỳ hoặc trung bình. Không cộng được: tỉ lệ và phần trăm, vì trung bình của các tỉ lệ khác tỉ lệ của các tổng. Quy tắc vàng cho loại thứ ba và là quy tắc được dùng lại ở M11B: **lưu tử số và mẫu số riêng, tính tỉ lệ ở bước cuối**; lưu sẵn tỉ lệ rồi cộng lại là lỗi sai số liệu âm thầm phổ biến nhất trong kho dữ liệu. Đếm giá trị phân biệt cũng không cộng được, và đây là chỗ nhiều công cụ làm sai âm thầm.

**Outcome.** Phân loại độ đo theo ba nhóm và chứng minh bằng số rằng cộng sai nhóm cho ra kết quả sai.

**Đánh giá.** Tầng *phân tích*. Objective đòi nhận ra một lỗi không báo lỗi, nên phải chứng minh bằng đối chứng số. Kiểm bằng ba phép cộng sai; đạt khi định lượng được mức sai ở cả ba và đề xuất cách lưu đúng.

**Lab.** Cho mười độ đo, phân vào ba nhóm. Với ba độ đo không cộng được hoặc cộng được một phần, tính theo cách sai và cách đúng rồi so số. Thiết kế lại cách lưu cho một tỉ lệ theo quy tắc tử số mẫu số riêng và chứng minh nó gộp đúng ở mọi mức.

**Pitfalls.** Cộng số dư theo thời gian · lưu sẵn tỉ lệ trong bảng sự kiện · trung bình các tỉ lệ · giả định đếm giá trị phân biệt cộng được.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mười độ đo phân đúng nhóm, ba phép cộng sai được định lượng mức sai, và bản lưu tử số mẫu số gộp đúng ở mọi mức.

### Lesson 156 · Dimension patterns - role-playing, junk, degenerate and bridge `TH`
**Prerequisites.** Lesson 155

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bốn mẫu bảng chiều giải bốn vấn đề cụ thể, học để nhận ra chứ để nhồi vào mọi thiết kế. Chiều vai trò: cùng một bảng chiều dùng ở nhiều vai trong một bảng sự kiện, ví dụ ngày đặt và ngày giao cùng trỏ bảng lịch; cách hiện thực là tạo khung nhìn đặt tên theo vai để truy vấn đọc được. Chiều rác: gom nhiều cờ và mã nhỏ lẻ vào một bảng thay vì để mỗi cái một chiều, tránh bảng sự kiện có hai mươi khoá ngoại. Chiều suy biến: khoá nghiệp vụ như mã hoá đơn nằm thẳng trong bảng sự kiện vì nó không có thuộc tính nào khác. Bảng cầu cho quan hệ nhiều nhiều và cho phân cấp có độ sâu thay đổi; **đây là mẫu nguy hiểm nhất vì nó nhân dòng theo thiết kế**, nên mọi phép gộp qua bảng cầu phải có hệ số phân bổ, nếu không thì đếm trùng.

**Outcome.** Nhận ra bốn mẫu trong một lược đồ cho trước và xử lý đúng phép gộp qua bảng cầu để không đếm trùng.

**Đánh giá.** Tầng *áp dụng*. Objective gồm một ca dễ sai âm thầm là bảng cầu. Kiểm bằng bài nhận dạng cộng phép đối soát; đạt khi nhận đúng ít nhất ba mẫu và tổng qua bảng cầu khớp tổng thật.

**Lab.** Cho một lược đồ có cả bốn mẫu. Nhận dạng từng cái. Viết truy vấn gộp qua bảng cầu theo hai cách: không có hệ số phân bổ và có hệ số; so hai kết quả với tổng thật. Tạo khung nhìn chiều vai trò cho ngày đặt và ngày giao.

**Pitfalls.** Gộp qua bảng cầu mà không phân bổ · tạo một chiều riêng cho mỗi cờ nhị phân · tách mã hoá đơn thành một chiều không có thuộc tính · dùng cùng tên cột cho hai vai của một chiều.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Nhận đúng ≥ 3/4 mẫu, và tổng gộp qua bảng cầu có hệ số phân bổ khớp tổng thật.

### Lesson 157 · Slowly changing dimensions, type 0 to type 6 `TH`
**Prerequisites.** Lesson 156

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Thuộc tính chiều đổi theo thời gian, và cách xử lý quyết định báo cáo lịch sử đúng hay sai. Bài toán cụ thể: khách chuyển từ vùng bắc sang vùng nam; nếu ghi đè thì **toàn bộ doanh thu lịch sử của khách đó nhảy sang vùng mới** và báo cáo năm ngoái đổi số dù không ai sửa dữ liệu bán hàng. Các loại và hậu quả báo cáo của từng loại: loại không giữ nguyên giá trị đầu, loại một ghi đè nên mất lịch sử, loại hai thêm dòng mới nên giữ đủ lịch sử và là loại dùng nhiều nhất, loại ba giữ một giá trị trước, loại sáu kết hợp. Cài đặt loại hai: khoá thay thế, hai cột hiệu lực, cờ bản ghi hiện hành, và quy trình tải gồm phát hiện thay đổi, đóng dòng cũ, mở dòng mới. Hai phép kiểm bắt buộc: không có khoảng hiệu lực chồng nhau, và mỗi khoá nghiệp vụ có đúng một dòng hiện hành.

**Outcome.** Cài đặt chiều biến đổi chậm loại hai đạt hai bất biến, và định lượng sai lệch báo cáo nếu dùng loại một.

**Đánh giá.** Tầng *áp dụng*. Objective là một cài đặt có hai bất biến kiểm được bằng truy vấn. Kiểm bằng hai phép kiểm bất biến cộng đối chứng; đạt khi cả hai bất biến giữ được qua 1000 lần cập nhật và sai lệch của loại một được định lượng.

**Lab.** Cài chiều khách hàng loại hai. Chạy 1000 lần cập nhật thuộc tính, gồm cả cập nhật tới muộn và cập nhật hiệu chỉnh. Chạy hai phép kiểm bất biến. Dựng cùng báo cáo doanh thu theo vùng trên bản loại một và bản loại hai, so hai kết quả cho kỳ lịch sử.

**Pitfalls.** Ghi đè thuộc tính rồi mất lịch sử · để khoảng hiệu lực chồng nhau · có hai dòng cùng đánh dấu hiện hành · quên xử lý cập nhật tới muộn nên chèn sai thứ tự.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Hai bất biến giữ được qua 1000 lần cập nhật, và chênh lệch báo cáo giữa loại một và loại hai được định lượng.

### Lesson 158 · Valid time, system time, corrections and restatement `TH`
**Prerequisites.** Lesson 157

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hai trục thời gian trả lời hai câu hỏi khác nhau và trộn chúng làm không trả lời được câu nào. Thời gian hiệu lực là khoảng mà sự thật đúng trong thế giới; thời gian hệ thống là khoảng mà hệ của ta tin điều đó. Ví dụ phân biệt: khách đổi địa chỉ từ ngày mùng một nhưng hệ chỉ biết vào ngày mười; hai trục cho hai câu trả lời khác nhau cho câu hỏi ngày năm khách ở đâu. Từ đó suy ra hai loại câu hỏi mà một hệ trưởng thành phải trả lời được: tình trạng thật tại một thời điểm, và **báo cáo đã in ra hôm đó dựa trên dữ liệu nào**; câu thứ hai là yêu cầu kiểm toán và chỉ trả lời được nếu có trục thời gian hệ thống. Hiệu chỉnh và trình bày lại: khi dữ liệu cũ sai và được sửa, báo cáo đã công bố đổi theo hay giữ nguyên là quyết định nghiệp vụ chứ kỹ thuật, và phải thoả thuận trước.

**Outcome.** Trả lời được cả hai loại câu hỏi thời gian trên cùng một tập dữ liệu và nêu chính sách hiệu chỉnh.

**Đánh giá.** Tầng *đánh giá*. Objective đòi phân biệt hai trục và nhận ra đây là quyết định có bên liên quan. Kiểm bằng bốn câu hỏi hai loại; đạt khi trả lời đúng ít nhất ba và chính sách hiệu chỉnh nêu rõ ai quyết.

**Lab.** Dựng bảng có cả hai trục thời gian. Tạo một chuỗi sự kiện gồm một lần biết muộn và một lần hiệu chỉnh dữ liệu sai. Trả lời bốn câu hỏi: hai câu về tình trạng thật và hai câu về báo cáo đã công bố. Viết chính sách hiệu chỉnh nêu rõ số đã công bố có đổi không và ai quyết.

**Pitfalls.** Chỉ lưu một trục thời gian · sửa dữ liệu cũ mà không ghi lại đã sửa · đổi số đã công bố mà không báo bên dùng · coi chính sách hiệu chỉnh là quyết định kỹ thuật.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Trả lời đúng ≥ 3/4 câu hỏi hai loại, và chính sách hiệu chỉnh nêu rõ hành vi cùng người quyết.

### Lesson 159 · Star, snowflake and the one-big-table trade-off `TH`
**Prerequisites.** Lesson 158

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba cách bố trí tầng phục vụ, so bằng bốn tiêu chí chứ bằng sở thích. Lược đồ sao: bảng chiều phi chuẩn hoá, ít phép kết, dễ hiểu với người dùng cuối, tốn dung lượng do lặp. Bông tuyết: chiều được chuẩn hoá thành nhiều bảng, tiết kiệm dung lượng, thêm phép kết và khó hiểu hơn; hiếm khi đáng ở kho hiện đại vì dung lượng rẻ còn phép kết thì không. Bảng rộng gộp tất cả vào một bảng: nhanh nhất cho người tiêu thụ và không thể kết sai, đổi lại lặp dữ liệu nhiều, khó quản trị khi một định nghĩa đổi, và mất tính linh hoạt khi cần chiều mới. Bốn tiêu chí so: tốc độ truy vấn, dung lượng, chi phí thay đổi định nghĩa, và mức dễ hiểu với người dùng. Khi nào bảng rộng là lựa chọn đúng: đường tiêu thụ cố định, số người dùng lớn, và có tầng ngữ nghĩa ở trên giữ định nghĩa, tức chính bối cảnh của M11B.

**Outcome.** So ba bố trí trên cùng dữ liệu theo bốn tiêu chí và chọn một kèm điều kiện làm lựa chọn đó sai.

**Đánh giá.** Tầng *đánh giá*. Objective đòi so đa tiêu chí có số đo chứ theo quy tắc chung. Kiểm bằng bảng ba bố trí nhân bốn tiêu chí; đạt khi hai tiêu chí đầu có số đo thật và lựa chọn có hai điều kiện đảo ngược.

**Lab.** Dựng cùng dữ liệu ở cả ba bố trí. Chạy bộ năm truy vấn chuẩn và đo thời gian cùng dung lượng. Ước lượng chi phí thay đổi bằng cách đếm số chỗ phải sửa khi đổi một định nghĩa. Khảo sát mức dễ hiểu bằng cách nhờ một người chưa biết lược đồ viết một truy vấn và tính giờ.

**Pitfalls.** Chọn bông tuyết để tiết kiệm dung lượng mà không đo phép kết thêm · dựng bảng rộng mà không có tầng giữ định nghĩa · so ba bố trí chỉ bằng tốc độ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng ba bố trí nhân bốn tiêu chí có số ở hai tiêu chí đầu, và lựa chọn kèm hai điều kiện đảo ngược cụ thể.

### Lesson 160 · Data Vault at a level sufficient to recognise it `LT`
**Prerequisites.** Lesson 159

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Phương pháp thứ ba, dạy ở mức nhận ra và đánh giá chứ mức triển khai, vì phần lớn đội không cần nó. Ba thành phần: trung tâm giữ khoá nghiệp vụ, liên kết giữ quan hệ giữa các trung tâm, vệ tinh giữ thuộc tính có lịch sử. Bất biến khi tải và lý do thiết kế: mọi thứ chỉ thêm chứ sửa, nên tải song song được và giữ đủ dấu vết kiểm toán. Điểm mạnh thật: chịu được nguồn đổi lược đồ thường xuyên và yêu cầu kiểm toán chặt, vì không bao giờ mất dữ liệu gốc. Điểm yếu thật và lý do ít dùng: số bảng nhân lên nhiều lần, truy vấn phải kết rất nhiều, nên **luôn cần một tầng phục vụ dạng chiều ở trên** và đội phải nuôi hai tầng. Hai câu hỏi quyết định có nên dùng. Ba dấu hiệu một dự án đang dùng nó vì nghe chuyên nghiệp chứ vì ràng buộc thật.

**Outcome.** Nhận ra cấu trúc này trong một lược đồ và đánh giá nó có phù hợp một bối cảnh cho trước không.

**Đánh giá.** Tầng *đánh giá*. Objective là năng lực đánh giá chứ triển khai, đúng phạm vi bản nguồn đặt ra. Kiểm bằng ba bối cảnh; đạt khi quyết định đúng cả ba và nêu đúng chi phí kéo theo ở bối cảnh chọn dùng.

**Lab.** Cho một lược đồ đã dựng theo phương pháp này; nhận dạng ba thành phần và viết một truy vấn lấy thông tin khách hàng hiện hành, đếm số phép kết cần. Cho ba bối cảnh khác nhau về tần suất đổi lược đồ nguồn, yêu cầu kiểm toán và quy mô đội; quyết định có dùng không.

**Pitfalls.** Chọn vì nghe chuyên nghiệp · dùng mà không dựng tầng phục vụ ở trên · nghĩ nó thay thế mô hình chiều · bỏ qua chi phí nuôi hai tầng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Nhận đúng ba thành phần kèm số phép kết đo được, và quyết định đúng cả ba bối cảnh kèm chi phí kéo theo.

### Lesson 161 · Domain modelling, bounded context and the canonical-model trap `LT`
**Prerequisites.** Lesson 160

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Góc nhìn thứ tư, đến từ thiết kế phần mềm và quan trọng khi dữ liệu đến từ nhiều đội. Ngữ cảnh giới hạn: cùng một từ có nghĩa khác nhau ở hai đội, và ép chúng dùng chung một định nghĩa thường thất bại; ví dụ khách hàng với đội bán hàng là người ký hợp đồng, với đội hỗ trợ là người gọi lên. Cái bẫy mô hình chuẩn chung: cố xây một mô hình duy nhất đúng cho cả công ty; nó tốn nhiều năm, không bao giờ xong, và chặn mọi đội. Cách đúng theo bản nguồn: **tích hợp ở mức hợp đồng chứ ở mức mô hình chung**, tức mỗi miền giữ mô hình riêng và công bố một hợp đồng ổn định ra ngoài. Sở hữu dữ liệu đi theo miền: đội sinh ra dữ liệu chịu trách nhiệm về nó. Quan hệ với M14D: từ điển thuật ngữ ghi lại việc một từ có nhiều nghĩa theo ngữ cảnh thay vì ép một nghĩa.

**Outcome.** Nhận ra hai ngữ cảnh giới hạn xung đột nhau trong một mô tả và đề xuất cách tích hợp bằng hợp đồng.

**Đánh giá.** Tầng *phân tích*. Objective đòi nhận ra xung đột ngữ nghĩa trước khi nó thành xung đột kỹ thuật. Kiểm bằng bài phân tích; đạt khi chỉ ra đúng ít nhất hai từ mang hai nghĩa và đề xuất hợp đồng thay vì mô hình chung.

**Lab.** Cho mô tả ba đội cùng dùng ba từ chung nhưng nghĩa khác nhau. Chỉ ra xung đột. Với mỗi từ, viết định nghĩa theo từng ngữ cảnh và một hợp đồng để hai bên trao đổi. Viết hai câu giải thích vì sao ép một định nghĩa chung sẽ thất bại ở đây.

**Pitfalls.** Ép một định nghĩa chung cho cả công ty · đổi tên để né xung đột mà không giải quyết nghĩa · coi xung đột ngữ nghĩa là vấn đề kỹ thuật · bỏ qua ai sở hữu dữ liệu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chỉ đúng ≥ 2 từ mang hai nghĩa, và đề xuất tích hợp bằng hợp đồng kèm định nghĩa theo từng ngữ cảnh.

### Lesson 162 · Late arriving data, early arriving facts and the unknown member `TH`
**Prerequisites.** Lesson 161

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba ca biên mà mọi mô hình thật đều gặp và mọi mô hình sách giáo khoa đều bỏ qua. Sự kiện tới trước chiều: một đơn hàng tham chiếu khách hàng chưa có trong bảng chiều; ba cách xử lý và hậu quả từng cách, trong đó cách sai phổ biến là bỏ dòng sự kiện đi và làm tổng thiếu mà không ai biết. Thành viên chưa biết: một dòng chiều đặc biệt để sự kiện luôn kết được, kèm ba biến thể mang ba nghĩa khác nhau là chưa biết, không áp dụng, và lỗi; gộp ba nghĩa là mất thông tin theo đúng bài học ở lesson 114. Chiều tới muộn: thuộc tính đúng chỉ biết sau khi sự kiện đã tải, nên phải sửa lại liên kết lịch sử; đây là chỗ khó nhất và liên quan trực tiếp tới loại hai ở lesson 157. Nguyên tắc chung: **không bao giờ bỏ dòng trong im lặng**, quy tắc sẽ được cưỡng chế ở M14C.

**Outcome.** Xử lý đúng ba ca biên và chứng minh tổng không thiếu dòng nào so với nguồn.

**Đánh giá.** Tầng *áp dụng*. Objective là ba ca biên có tiêu chí nghiệm thu bằng đối soát. Kiểm bằng đối soát tổng; đạt khi không dòng nào bị bỏ và ba nghĩa của thành viên chưa biết phân biệt được.

**Lab.** Tạo dữ liệu có cả ba ca biên. Xử lý từng ca. Đối soát tổng số dòng và tổng tiền với nguồn để chứng minh không mất dòng. Truy vấn phân biệt được ba nghĩa của thành viên chưa biết. Với ca chiều tới muộn, sửa lại liên kết lịch sử và đối soát báo cáo trước sau.

**Pitfalls.** Bỏ dòng sự kiện không kết được · dùng một thành viên chưa biết cho cả ba nghĩa · để sự kiện tham chiếu khoá không tồn tại · sửa chiều tới muộn mà không sửa liên kết lịch sử.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đối soát tổng khớp tuyệt đối với nguồn, ba nghĩa phân biệt được bằng truy vấn, và liên kết lịch sử sau khi sửa cho báo cáo đúng.

### Lesson 163 · Modelling for handover - what the consumer needs `TH`
**Prerequisites.** Lesson 162

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Mô hình tốt về kỹ thuật vẫn vô dụng nếu người dùng không hiểu, nên bài này nhìn từ phía người tiêu thụ và là cầu nối sang M11C. Sáu thứ người tiêu thụ cần cùng với bảng: phát biểu hạt, định nghĩa từng độ đo gồm công thức và bộ lọc, ý nghĩa từng thuộc tính chiều, độ tươi và lịch làm mới, truy vấn mẫu cho ba câu hỏi thường gặp, và **hạn chế diễn giải** tức những kết luận mà dữ liệu này không cho phép rút ra. Phần cuối là phần hiếm ai viết và là phần chặn được nhiều kết luận sai nhất. Quy ước đặt tên nhất quán quan trọng hơn quy ước hoàn hảo, theo tinh thần đã nêu ở M7. Ba dấu hiệu mô hình chưa sẵn sàng bàn giao. Phép thử bàn giao ở đây là bản thu nhỏ của phép thử sẽ làm ở M11C: một người khác trả lời được ba câu hỏi nghiệp vụ chỉ bằng bảng và tài liệu.

**Outcome.** Nộp bộ tài liệu sáu phần cho một mô hình và chứng minh người khác trả lời được ba câu hỏi mà không hỏi.

**Đánh giá.** Tầng *đánh giá*. Objective đo chất lượng bàn giao bằng kết quả của người nhận. Kiểm bằng phép thử bàn giao; đạt khi người nhận trả lời đúng ít nhất hai trong ba câu hỏi mà không phải hỏi lại.

**Lab.** Viết bộ tài liệu sáu phần cho mô hình đã dựng. Đưa cho một học viên chưa xem mô hình cùng ba câu hỏi nghiệp vụ. Họ viết truy vấn và trả lời. Ghi lại mọi câu họ phải hỏi và mọi chỗ họ hiểu sai, rồi sửa tài liệu.

**Pitfalls.** Bỏ phần hạn chế diễn giải · viết tài liệu cho người đã biết mô hình · đặt tên cột theo tên cột nguồn · không kèm truy vấn mẫu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Người nhận trả lời đúng ≥ 2/3 câu hỏi mà không phải hỏi lại, và bộ tài liệu có đủ sáu phần gồm hạn chế diễn giải.

### Lesson 164 · Modelling project - four models, one decision matrix `DA`
**Prerequisites.** Lesson 163

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Bài dự án khép module. Trên cùng một miền nghiệp vụ, dựng bốn mô hình: chuẩn hoá cho hệ giao dịch, mô hình chiều cho phân tích, phác thảo Data Vault, và một bảng rộng. Với mỗi mô hình, nộp phát biểu hạt cho mọi bảng sự kiện và một truy vấn trả lời cùng một câu hỏi nghiệp vụ. Sau đó lập ma trận quyết định bốn phương án nhân bốn tiêu chí ở lesson 159, mỗi ô có số đo hoặc ước lượng có căn cứ chứ tính từ. Kết luận: chọn một phương án cho một bối cảnh cho trước và **nêu ba điều kiện làm lựa chọn đó sai**. Yêu cầu bắt buộc: mô hình chiều phải cài loại hai theo lesson 157, xử lý đủ ba ca biên ở lesson 162, và kèm bộ tài liệu sáu phần theo lesson 163.

**Outcome.** Nộp bốn mô hình có phát biểu hạt đầy đủ, một ma trận quyết định có số, và một khuyến nghị kèm điều kiện đảo ngược.

**Đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module thành một quyết định thiết kế có bằng chứng. Kiểm bằng rà soát chéo cộng đối soát; đạt khi mọi bảng sự kiện có hạt kiểm được và ma trận không có ô nào chỉ có tính từ.

**Lab.** Dựng bốn mô hình trên cùng miền. Kiểm hạt bằng phép đếm theo lesson 150. Chạy cùng một truy vấn nghiệp vụ trên cả bốn và đối soát bốn kết quả phải khớp. Lập ma trận bốn nhân bốn. Viết khuyến nghị kèm ba điều kiện đảo ngược.

**Pitfalls.** Bỏ phát biểu hạt ở một mô hình · để bốn mô hình cho bốn kết quả khác nhau mà không giải thích · điền ma trận bằng tính từ · khuyến nghị không có điều kiện đảo ngược.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Bốn mô hình cho cùng kết quả trên truy vấn đối chứng, mọi bảng sự kiện có hạt kiểm được, và ma trận không có ô nào thiếu số.

# MODULE M11B · SEMANTIC LAYER AND METRICS ENGINEERING

**Phase 5 · Lessons 165–184 · 40 giờ**

| | |
|---|---|
| **Objective cấp module** | Thiết kế hợp đồng chỉ số không mơ hồ, dựng đồ thị ngữ nghĩa an toàn trước nhân dòng, và quản trị vòng đời chỉ số |
| **Tiền đề** | M11 |
| **Exit criterion** | 15 chỉ số thuộc ≥ 5 loại, mỗi cái có hợp đồng sáu phần, chủ sở hữu và phép kiểm; ≥ 3 mô hình ngữ nghĩa với chứng minh không nhân dòng cho truy vấn nhiều bước kết; bộ đối chứng phủ sáu ca; phục vụ hai bên tiêu thụ có bảo mật và cách ly đệm; một lần di trú phá vỡ hoàn tất với chạy song song và đối soát |
| **Kỹ năng SFIA** | `DATM` mức 5 · `DTAN` mức 4 |
| **Chế độ hỏng** | Cài công cụ tầng ngữ nghĩa rồi khai báo chỉ số theo bảng hiện có, không có hợp đồng và không đối soát, nên tầng mới trở thành một nguồn số sai mới có thẩm quyền |

**Đây là module đầu tiên thuộc phần bù Analytics Engineer.** Bản Data Engineer cũ không có nội dung này, và nó là một trong bốn lý do của việc gộp.

Thứ tự bắt buộc lấy từ hợp đồng nguồn: **nền ngữ nghĩa trước công cụ**. Ba bài đầu không mở công cụ nào, vì khai báo chỉ số bằng công cụ khi chưa có hợp đồng là cách nhân bản sự mơ hồ với tốc độ cao hơn.

Quy tắc hạt ở lesson 120 và quy tắc tử số mẫu số riêng ở lesson 155 được dùng lại liên tục trong module này.

### Lesson 165 · The layers that must be distinguished `LT`
**Prerequisites.** Module 11B: M11

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài mở module bằng việc tách năm thứ hay bị gọi lẫn, vì gọi lẫn thì không bàn được thiết kế. Bảng vật lý là nơi dữ liệu nằm. Mô hình mart là cách bảng được tổ chức cho một miền, nội dung của M11. Mô hình ngữ nghĩa là khai báo thực thể, chiều và độ đo cùng cách chúng nối nhau, không chứa dữ liệu. Chỉ số là một phép tính có tên, có hợp đồng, dựng trên mô hình ngữ nghĩa. Công cụ tiêu thụ là nơi người dùng đặt câu hỏi. Điểm quan trọng nhất và là lý do tầng ngữ nghĩa tồn tại: **định nghĩa chỉ số phải nằm ở một chỗ duy nhất, không nằm rải trong công cụ BI và trong từng truy vấn**; nằm rải thì mỗi chỗ một số. Ba triệu chứng của việc định nghĩa nằm rải, đã gặp dưới dạng khác trong tình huống bốn báo cáo bốn con số. Ranh giới với M11C: module này lo định nghĩa đúng, module sau lo người dùng dùng được.

**Outcome.** Phân loại năm tầng cho một kiến trúc cho trước và chỉ ra định nghĩa chỉ số đang nằm ở đâu.

**Đánh giá.** Tầng *hiểu*. Bài mở module, đặt từ vựng; chưa mở công cụ. Kiểm bằng bài phân tích ba kiến trúc; đạt khi phân đúng năm tầng ở ít nhất hai và chỉ ra đúng chỗ định nghĩa đang nằm rải.

**Lab.** Cho ba kiến trúc thật về mặt cấu trúc. Với mỗi cái, phân loại thành phần vào năm tầng và chỉ ra định nghĩa chỉ số đang nằm ở đâu. Với kiến trúc có định nghĩa nằm rải, đếm số chỗ cùng một chỉ số được định nghĩa và liệt kê ba triệu chứng quan sát được.

**Pitfalls.** Gọi mọi thứ là tầng ngữ nghĩa · coi bảng mart là mô hình ngữ nghĩa · để công cụ BI giữ định nghĩa chỉ số · nghĩ cài công cụ là đã có tầng ngữ nghĩa.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân đúng năm tầng ở ≥ 2/3 kiến trúc, và đếm được số chỗ trùng định nghĩa ở kiến trúc có vấn đề.

### Lesson 166 · From a business question to a metric contract `TH`
**Prerequisites.** Lesson 165

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài trung tâm của module. Hợp đồng chỉ số gồm sáu phần bắt buộc, và thiếu bất kỳ phần nào là chỉ số còn mơ hồ: **tập hợp** tức tính trên những bản ghi nào và loại trừ những gì; **hạt** theo lesson 120; **thời gian** tức dùng mốc thời gian nào và thuộc kỳ nào; **bộ lọc** tức điều kiện nằm trong định nghĩa chứ do người dùng chọn; **phép gộp** tức cộng, đếm, trung bình hay tỉ lệ; và **chủ sở hữu** tức ai quyết khi cần đổi. Ví dụ đối chiếu: câu hỏi doanh thu tháng trước là bao nhiêu có thể cho tám con số đều hợp lệ tuỳ sáu phần trên được chốt thế nào, và liệt kê đủ tám là bài tập của lab. Cách phỏng vấn người nghiệp vụ để chốt sáu phần, theo tinh thần bốn câu hỏi làm rõ ở lesson 1. Phép thử của một hợp đồng tốt: hai người đọc cùng viết ra cùng một truy vấn.

**Outcome.** Viết hợp đồng sáu phần cho một chỉ số và chứng minh hai người đọc độc lập cho ra cùng một con số.

**Đánh giá.** Tầng *áp dụng*. Objective có phép kiểm chứng khách quan bằng hai bản cài độc lập. Kiểm bằng phép thử hai người; đạt khi ba chỉ số đều cho hai con số khớp tuyệt đối giữa hai người cài độc lập.

**Lab.** Nhận ba câu hỏi nghiệp vụ mơ hồ. Với câu thứ nhất, liệt kê tám cách hiểu đều hợp lệ và con số tương ứng. Viết hợp đồng sáu phần cho cả ba. Đưa hợp đồng cho một học viên khác; hai người cài độc lập và so ba cặp con số.

**Pitfalls.** Bỏ phần tập hợp nên không rõ loại trừ gì · không nêu mốc thời gian dùng để quy kỳ · để bộ lọc trong định nghĩa lẫn với bộ lọc người dùng chọn · không có chủ sở hữu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba cặp con số từ hai người cài độc lập đều khớp tuyệt đối, và tám cách hiểu của câu đầu được liệt kê đủ.

### Lesson 167 · The semantic graph - entities, dimensions, measures, metrics `LT`
**Prerequisites.** Lesson 166

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Mô hình ngữ nghĩa là một đồ thị chứ một danh sách khai báo, và nhìn nó như đồ thị giải thích mọi ràng buộc về sau. Bốn loại nút: thực thể là thứ có danh tính và là điểm nối, chiều là thuộc tính để cắt lát, độ đo là cột số có thể gộp, chỉ số là phép tính có hợp đồng dựng trên độ đo. Cạnh là quan hệ kết giữa các thực thể kèm bản số. Từ đồ thị suy ra ba câu hỏi mà tầng ngữ nghĩa phải trả lời được bằng máy: chỉ số này cắt được theo chiều nào, hai chỉ số này đặt cạnh nhau được không, và đường kết nào được dùng khi có nhiều đường. Câu cuối là nguồn của mọi phép kết mơ hồ ở lesson 171. Khác biệt với lược đồ vật lý: một thực thể ngữ nghĩa có thể ánh xạ tới nhiều bảng, và một bảng có thể chứa nhiều thực thể; nên đồ thị ngữ nghĩa không phải bản sao của sơ đồ bảng.

**Outcome.** Vẽ đồ thị ngữ nghĩa cho một miền và chỉ ra chỗ có nhiều hơn một đường kết giữa hai thực thể.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết chuẩn bị cho ba bài về tính đúng của phép kết. Kiểm bằng bài vẽ cộng nhận dạng; đạt khi đồ thị đủ bốn loại nút và chỉ ra đúng ít nhất một cặp thực thể có nhiều đường kết.

**Lab.** Từ lược đồ mart đã dựng ở M11, vẽ đồ thị ngữ nghĩa với bốn loại nút và cạnh có bản số. Chỉ ra mọi cặp thực thể có nhiều hơn một đường kết. Với mỗi cặp đó, viết hai câu hỏi nghiệp vụ mà hai đường cho hai câu trả lời khác nhau.

**Pitfalls.** Chép sơ đồ bảng thành đồ thị ngữ nghĩa · nhầm độ đo với chỉ số · bỏ bản số trên cạnh · giả định luôn chỉ có một đường kết.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đồ thị đủ bốn loại nút và cạnh có bản số, và chỉ ra được ít nhất một cặp có nhiều đường kèm hai câu hỏi cho hai kết quả.

### Lesson 168 · Metric types - simple, ratio, derived and cumulative `TH`
**Prerequisites.** Lesson 167

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bốn loại chỉ số, mỗi loại có ràng buộc gộp riêng, và xử lý sai loại là nguồn số sai phổ biến nhất ở tầng này. Chỉ số đơn giản là một phép gộp trên một độ đo. Chỉ số tỉ lệ có tử và mẫu, và ràng buộc bắt buộc theo lesson 155: **lưu tử và mẫu riêng, chia ở bước cuối**, vì gộp các tỉ lệ đã tính sẵn cho kết quả sai ở mọi mức trừ mức đã tính. Chỉ số phái sinh dựng từ chỉ số khác bằng phép toán, và phải kế thừa ràng buộc gộp của thành phần. Chỉ số tích luỹ cộng dồn theo một cửa sổ thời gian, nên phụ thuộc vào ngữ nghĩa thời gian ở lesson 170 và vào bảng lịch đầy đủ theo lesson 124. Với mỗi loại, một phép kiểm đặc trưng để phát hiện cài sai. Bảng phân loại mười chỉ số thật của một doanh nghiệp là bài tập nhận dạng.

**Outcome.** Phân loại chỉ số vào bốn nhóm và chứng minh bằng số rằng cài tỉ lệ sai cho kết quả sai ở mức gộp cao hơn.

**Đánh giá.** Tầng *phân tích*. Objective đòi nhận ra lỗi không báo lỗi, nên bắt buộc chứng minh bằng đối chứng. Kiểm bằng bài phân loại cộng đối chứng số; đạt khi phân đúng ít nhất tám trong mười và định lượng được sai lệch của cách cài sai.

**Lab.** Phân loại mười chỉ số thật vào bốn nhóm. Cài một chỉ số tỉ lệ theo hai cách: lưu sẵn tỉ lệ, và lưu tử mẫu riêng. Gộp lên ba mức khác nhau và so hai bộ kết quả với bản tính tay. Cài một chỉ số tích luỹ và kiểm ở kỳ không có dữ liệu.

**Pitfalls.** Lưu sẵn tỉ lệ trong bảng · chỉ số phái sinh không kế thừa ràng buộc gộp · chỉ số tích luỹ không dựng trên bảng lịch đầy đủ · kiểm chỉ ở mức đã tính sẵn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân đúng ≥ 8/10 chỉ số, và sai lệch của cách lưu sẵn tỉ lệ được định lượng ở cả ba mức gộp.

### Lesson 169 · Additivity and aggregation in the semantic layer `TH`
**Prerequisites.** Lesson 168

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài áp phân loại cộng được ở lesson 155 vào tầng ngữ nghĩa, nơi nó trở thành một khai báo mà máy cưỡng chế được. Mỗi độ đo khai báo phép gộp mặc định và những chiều nó cộng được; tầng ngữ nghĩa dựa vào đó để **từ chối một truy vấn cộng sai** thay vì im lặng trả về số sai, và đây là giá trị lớn nhất của việc có tầng này. Ba nhóm theo lesson 155 nay thành ba kiểu khai báo. Độ đo bán cộng: khai báo phép gộp khác nhau theo chiều, ví dụ cộng theo sản phẩm nhưng lấy giá trị cuối kỳ theo thời gian. Đếm giá trị phân biệt: không cộng được và cũng không cộng dồn được, nên tầng ngữ nghĩa phải tính lại ở mọi mức thay vì gộp từ mức thấp; đây là lý do chỉ số loại này tốn hơn nhiều. Bảng tổng hợp tính sẵn và điều kiện dùng được: chỉ dùng cho độ đo cộng được hoàn toàn.

**Outcome.** Khai báo phép gộp cho mười độ đo sao cho tầng ngữ nghĩa từ chối được các truy vấn cộng sai.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu bằng phép thử phủ định. Kiểm bằng năm truy vấn cộng sai; đạt khi cả năm bị từ chối hoặc trả về đúng, và không truy vấn hợp lệ nào bị chặn nhầm.

**Lab.** Khai báo mười độ đo gồm cả cộng được, bán cộng và không cộng được. Viết năm truy vấn cố ý cộng sai và chứng minh tầng ngữ nghĩa từ chối hoặc xử lý đúng. Viết năm truy vấn hợp lệ và chứng minh không cái nào bị chặn nhầm. Đo chi phí của một chỉ số đếm giá trị phân biệt ở ba mức.

**Pitfalls.** Khai báo phép gộp mặc định là cộng cho mọi độ đo · dùng bảng tổng hợp tính sẵn cho chỉ số không cộng được · chặn quá tay nên truy vấn hợp lệ cũng bị từ chối.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Năm truy vấn cộng sai đều bị chặn hoặc xử lý đúng, năm truy vấn hợp lệ đều chạy, và có số đo chi phí của chỉ số đếm phân biệt.

### Lesson 170 · Time semantics - grain, offsets and period comparison `TH`
**Prerequisites.** Lesson 169

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Thời gian là chiều phức tạp nhất và là nguồn tranh cãi nhiều nhất giữa các phòng ban. Bốn quyết định phải chốt trong hợp đồng: dùng mốc thời gian nào khi một bản ghi có nhiều mốc như ngày đặt, ngày giao, ngày ghi nhận doanh thu; hạt thời gian mặc định; múi giờ quy chiếu, vì một giao dịch lúc nửa đêm thuộc ngày nào phụ thuộc múi giờ; và định nghĩa kỳ tài chính nếu khác kỳ dương lịch. So kỳ trước và cùng kỳ năm trước: ba cách dịch chuyển kỳ và chúng cho kết quả khác nhau ở tháng có số ngày khác nhau và ở năm nhuận. **Vấn đề kỳ thiếu** theo lesson 124 nay là ràng buộc bắt buộc của tầng ngữ nghĩa: mọi chỉ số theo thời gian phải dựng trên bảng lịch đầy đủ, nếu không thì kỳ không có dữ liệu biến mất và phép so kỳ lấy nhầm kỳ. Cửa sổ trượt và kỳ tới hiện tại.

**Outcome.** Chốt bốn quyết định thời gian cho một bộ chỉ số và chứng minh phép so kỳ đúng ở tháng thiếu dữ liệu và ở năm nhuận.

**Đánh giá.** Tầng *áp dụng*. Objective có hai ca biên cụ thể mà bản làm ẩu luôn sai. Kiểm bằng đối soát ở ca biên; đạt khi kết quả khớp bản tính tay ở cả tháng thiếu dữ liệu lẫn ngày 29 tháng 2.

**Lab.** Với một bộ ba chỉ số, chốt bốn quyết định thời gian và ghi vào hợp đồng. Dựng bảng lịch đầy đủ có kỳ tài chính. Tính so kỳ trước và cùng kỳ năm trước bằng ba cách dịch chuyển, trên dữ liệu cố ý thiếu ba tháng và bắc qua năm nhuận. Đối soát với bản tính tay.

**Pitfalls.** Không chốt mốc thời gian dùng để quy kỳ · bỏ qua múi giờ · không dựng bảng lịch nên kỳ rỗng biến mất · dùng một cách dịch kỳ cho mọi chỉ số mà không hỏi nghiệp vụ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Kết quả khớp bản tính tay ở cả tháng thiếu dữ liệu lẫn năm nhuận, và bốn quyết định thời gian có trong hợp đồng.

### Lesson 171 · Ambiguous joins and the chasm trap `TH`
**Prerequisites.** Lesson 170

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hai chế độ hỏng đặc trưng của tầng ngữ nghĩa, và cả hai đều cho số sai mà không báo lỗi. Phép kết mơ hồ: khi có nhiều hơn một đường nối hai thực thể theo lesson 167, công cụ phải chọn một đường và chọn khác nhau thì số khác nhau; cách chặn là khai báo tường minh đường kết hợp lệ chứ để công cụ đoán. Bẫy vực: hai bảng sự kiện cùng nối vào một chiều chung nhưng không nối trực tiếp với nhau; kết cả ba trong một truy vấn làm **hai bảng sự kiện nhân dòng lẫn nhau qua chiều chung**, và tổng của cả hai đều bị thổi phồng. Ví dụ kinh điển: đơn hàng và phiếu hỗ trợ cùng nối vào khách hàng. Ba cách giải: gộp riêng từng bảng rồi mới nối kết quả, dùng truy vấn con tương quan, hoặc tách thành hai truy vấn. Bẫy hố: quan hệ một nhiều theo chiều ngược làm mất dòng thay vì nhân dòng.

**Outcome.** Tái hiện bẫy vực bằng số và chặn nó bằng một trong ba cách, chứng minh tổng trở lại đúng.

**Đánh giá.** Tầng *phân tích*. Objective đòi nhận ra một lỗi im lặng rồi sửa bằng cơ chế đúng. Kiểm bằng đối chứng với tổng thật; đạt khi định lượng được mức thổi phồng và bản sửa khớp tổng thật.

**Lab.** Dựng hai bảng sự kiện cùng nối vào chiều khách hàng. Viết truy vấn kết cả ba và so tổng của từng bảng với tổng thật; định lượng mức thổi phồng. Sửa bằng cả ba cách và so ba kết quả. Tạo một cặp thực thể có hai đường kết và chứng minh hai đường cho hai con số.

**Pitfalls.** Kết hai bảng sự kiện qua một chiều chung · để công cụ tự chọn đường kết · phát hiện bằng cách nhìn số rồi thấy hợp lý · dùng phép chọn phân biệt để chữa nhân dòng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mức thổi phồng được định lượng, cả ba cách sửa đều cho tổng khớp tổng thật, và hai đường kết cho hai con số khác nhau được chỉ ra.

### Lesson 172 · Fanout - proving a metric is not double counted `TH`
**Prerequisites.** Lesson 171

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài đặt ra một nghĩa vụ chứng minh chứ chỉ một lời khuyên cẩn thận. Nhân dòng xảy ra bất cứ khi nào phép kết đổi hạt theo lesson 150, và hậu quả là mọi phép cộng sau đó bị thổi phồng. Ba nguồn nhân dòng ở tầng ngữ nghĩa: kết với bảng có bản số nhiều, kết qua bảng cầu theo lesson 156, và bẫy vực ở lesson 171. Quy trình chứng minh không đếm trùng gồm bốn bước và đây là quy trình bắt buộc cho mọi chỉ số trước khi được chứng nhận: phát biểu hạt của mỗi bảng tham gia; đếm dòng trước và sau mỗi phép kết; đối soát tổng với một truy vấn viết tay trên bảng gốc; và kiểm ở ít nhất ba mức gộp khác nhau chứ chỉ mức chi tiết nhất. **Một chỉ số chưa qua bốn bước này thì chưa được đưa vào danh mục**, và quy tắc đó được cưỡng chế ở lesson 182.

**Outcome.** Chạy đủ bốn bước chứng minh cho ba chỉ số và phát hiện được chỉ số nào đang đếm trùng.

**Đánh giá.** Tầng *áp dụng*. Objective là một quy trình kiểm chứng bắt buộc có kết quả nhị phân. Kiểm bằng ba chỉ số trong đó ít nhất một đang đếm trùng; đạt khi phát hiện đúng và hai chỉ số còn lại được chứng minh sạch ở cả ba mức gộp.

**Lab.** Nhận ba chỉ số đã khai báo sẵn, trong đó một cái đếm trùng. Chạy đủ bốn bước cho từng cái. Với chỉ số có vấn đề, định lượng mức thổi phồng và sửa. Nộp bảng đối soát ba mức gộp cho cả ba.

**Pitfalls.** Chỉ đối soát ở mức chi tiết nhất · tin công cụ đã xử lý nhân dòng · bỏ bước đếm dòng trước và sau kết · đối soát với chính truy vấn do công cụ sinh ra thay vì truy vấn viết tay.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phát hiện đúng chỉ số đếm trùng và định lượng mức thổi phồng, và hai chỉ số còn lại khớp truy vấn viết tay ở cả ba mức gộp.

### Lesson 173 · The compatibility matrix - which dimension goes with which metric `TH`
**Prerequisites.** Lesson 172

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Không phải chỉ số nào cũng cắt được theo chiều nào, và để người dùng tự phát hiện điều đó bằng cách nhận số vô nghĩa là thiết kế tồi. Ma trận tương thích liệt kê chỉ số theo hàng và chiều theo cột, mỗi ô ghi hợp lệ, không hợp lệ, hoặc hợp lệ có điều kiện. Ba nguồn không tương thích: chiều không nối được tới bảng sự kiện của chỉ số; chiều nối được nhưng ở hạt thô hơn nên cắt lát làm mất nghĩa; và độ đo không cộng được theo chiều đó theo lesson 169. Ví dụ cụ thể: cắt số dư cuối kỳ theo chiều sản phẩm có nghĩa, cắt theo thời gian rồi cộng thì không. Tầng ngữ nghĩa nên **cưỡng chế ma trận bằng máy**: truy vấn ở ô không hợp lệ bị từ chối kèm thông báo giải thích, thay vì trả về số. Ma trận cũng là tài liệu cho người dùng, và nó là đầu vào của phần khả năng tìm thấy ở M11C.

**Outcome.** Dựng ma trận tương thích cho bộ chỉ số và cưỡng chế được nó bằng máy với thông báo giải thích.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu hai chiều: chặn đúng cái sai và không chặn nhầm cái đúng. Kiểm bằng mười truy vấn; đạt khi mọi ô không hợp lệ bị chặn có giải thích và không ô hợp lệ nào bị chặn nhầm.

**Lab.** Dựng ma trận cho tám chỉ số nhân sáu chiều, mỗi ô ghi một trong ba trạng thái kèm lý do cho ô không hợp lệ. Cưỡng chế bằng công cụ. Chạy mười truy vấn gồm năm hợp lệ và năm không, kiểm phản ứng từng cái. Xuất ma trận thành tài liệu cho người dùng.

**Pitfalls.** Để người dùng tự phát hiện chiều không dùng được · chặn mà không giải thích lý do · đánh dấu hợp lệ cho mọi ô để tránh phiền · không xuất ma trận thành tài liệu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Năm truy vấn không hợp lệ bị chặn kèm giải thích, năm truy vấn hợp lệ chạy được, và ma trận xuất ra dạng tài liệu đọc được.

### Lesson 174 · Semantic models in MetricFlow `TH`
**Prerequisites.** Lesson 173

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài đầu tiên mở công cụ, sau khi chín bài trước đã dựng nền. Mô hình ngữ nghĩa khai báo ba phần: thực thể với loại khoá chính hoặc khoá ngoại, chiều với loại phân loại hoặc thời gian, và độ đo với phép gộp. Chiều thời gian chính là khai báo quyết định hạt thời gian mặc định theo lesson 170. Ánh xạ từ mô hình ngữ nghĩa xuống bảng vật lý, và vì sao một mô hình ngữ nghĩa có thể trỏ tới một bảng hoặc một truy vấn. Quan hệ với tầng biến đổi ở M14: mô hình ngữ nghĩa đặt trên mart chứ trên bảng thô, nên chất lượng mart quyết định chất lượng tầng ngữ nghĩa. Ba lỗi khai báo hay gặp và thông báo lỗi tương ứng. Nguyên tắc giữ trong suốt module: **mọi khai báo phải truy được về một dòng trong hợp đồng chỉ số ở lesson 166**, chứ suy ra từ cột có sẵn trong bảng.

**Outcome.** Khai báo mô hình ngữ nghĩa cho ba bảng mart sao cho mọi khai báo truy được về hợp đồng.

**Đánh giá.** Tầng *áp dụng*. Objective là chuyển một thiết kế đã có sang khai báo công cụ, có tiêu chí truy ngược. Kiểm bằng rà soát truy ngược; đạt khi mọi độ đo và chiều dẫn được về một dòng trong hợp đồng và ba mô hình biên dịch sạch.

**Lab.** Khai báo mô hình ngữ nghĩa cho ba bảng mart đã dựng ở M11. Với mỗi độ đo và chiều, ghi rõ nó đến từ phần nào của hợp đồng. Biên dịch và sửa tới sạch. Cố ý khai báo sai loại thực thể và ghi lại thông báo lỗi.

**Pitfalls.** Khai báo theo cột có sẵn trong bảng · đặt mô hình ngữ nghĩa trên bảng thô · bỏ khai báo chiều thời gian chính · khai báo phép gộp mặc định là cộng cho mọi độ đo.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba mô hình biên dịch sạch, và mọi độ đo cùng chiều dẫn được về một dòng cụ thể trong hợp đồng.

### Lesson 175 · Defining metrics and reading the generated SQL `TH`
**Prerequisites.** Lesson 174

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Khai báo bốn loại chỉ số ở lesson 168 bằng công cụ, và bước quan trọng hơn là đọc câu lệnh SQL mà nó sinh ra. Lý do đọc: **công cụ sinh SQL không phải hộp đen được phép tin**, và cách duy nhất biết định nghĩa có đúng là đọc câu lệnh rồi đối chiếu với hợp đồng. Bốn thứ cần soi trong SQL sinh ra: phạm vi tập hợp có khớp phần tập hợp của hợp đồng không, bộ lọc trong định nghĩa có được áp không, đường kết nào được chọn theo lesson 171, và phép gộp có đúng loại theo lesson 169. Chỉ số tỉ lệ sinh ra SQL đặc trưng với tử và mẫu tính riêng rồi chia, và thấy đúng dạng đó là bằng chứng công cụ đang làm đúng. Chỉ số tích luỹ sinh ra phép kết với bảng lịch. Cách đọc kế hoạch thực thi của SQL sinh ra, dùng kỹ năng ở lesson 130.

**Outcome.** Khai báo bốn loại chỉ số và chứng minh bằng SQL sinh ra rằng mỗi cái khớp hợp đồng ở cả bốn điểm soi.

**Đánh giá.** Tầng *phân tích*. Objective đòi kiểm chứng đầu ra của công cụ thay vì tin nó. Kiểm bằng bài đọc SQL có danh mục bốn điểm; đạt khi cả bốn chỉ số qua đủ bốn điểm soi và phát hiện được một khai báo sai cài sẵn.

**Lab.** Khai báo bốn chỉ số theo bốn loại. Với mỗi cái, xuất SQL sinh ra và soi đủ bốn điểm, đối chiếu với hợp đồng. Giảng viên sửa một khai báo cho sai lệch hợp đồng; tìm ra nó chỉ bằng cách đọc SQL. Đọc kế hoạch thực thi của chỉ số tốn nhất.

**Pitfalls.** Tin SQL sinh ra là đúng vì công cụ nổi tiếng · chỉ kiểm bằng cách so con số · bỏ qua đường kết được chọn · không bao giờ đọc kế hoạch của SQL sinh ra.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn chỉ số qua đủ bốn điểm soi, và khai báo sai cài sẵn được tìm ra chỉ bằng đọc SQL.

### Lesson 176 · Query compilation internals `TH`
**Prerequisites.** Lesson 175

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hiểu công cụ biên dịch một câu hỏi thành SQL ra sao là điều kiện để chẩn đoán khi nó cho số lạ hoặc chạy chậm. Các bước: phân giải chỉ số và chiều được yêu cầu, xác định tập mô hình ngữ nghĩa cần tới, tìm đường kết giữa chúng, dựng truy vấn theo từng nguồn rồi nối, và áp phép gộp cuối. Bước tìm đường kết là bước quyết định và là nơi phát sinh phép kết mơ hồ ở lesson 171. Cơ chế tránh nhân dòng của công cụ: gộp riêng từng nguồn về hạt chung trước khi nối, và đây chính là cách giải thứ nhất ở lesson 171 được tự động hoá. Giới hạn phải biết: công cụ chỉ đúng khi khai báo đúng, nên **nó không cứu được một mô hình ngữ nghĩa sai**. Ba trường hợp công cụ sinh SQL kém hiệu quả và cách can thiệp, gồm cả việc dựng bảng tổng hợp tính sẵn.

**Outcome.** Giải thích một kết quả lạ bằng cách truy các bước biên dịch, và can thiệp được vào một truy vấn sinh ra kém hiệu quả.

**Đánh giá.** Tầng *phân tích*. Objective là chẩn đoán xuyên tầng từ câu hỏi tới SQL. Kiểm bằng ba tình huống; đạt khi truy đúng bước gây ra ở ít nhất hai và cải thiện được truy vấn chậm có số đo.

**Lab.** Giảng viên đưa ba tình huống: một kết quả lạ do đường kết, một do phép gộp, và một truy vấn chậm. Với mỗi cái, truy các bước biên dịch để tìm bước gây ra. Với truy vấn chậm, dựng bảng tổng hợp tính sẵn hoặc chỉnh khai báo, đo thời gian trước sau.

**Pitfalls.** Đổ lỗi cho công cụ khi nguyên nhân là khai báo · sửa bằng cách viết SQL tay ngoài tầng ngữ nghĩa · dựng bảng tổng hợp cho chỉ số không cộng được · không đo trước sau.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Truy đúng bước gây ra ở ≥ 2/3 tình huống, và truy vấn chậm cải thiện có số đo mà kết quả không đổi.

### Lesson 177 · Testing a semantic layer - definition and static tests `TH`
**Prerequisites.** Lesson 176

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Tháp kiểm thử cho tầng ngữ nghĩa có ba tầng, bài này lo tầng thứ nhất. Kiểm tra định nghĩa chạy nhanh và không cần dữ liệu: mọi chỉ số có đủ sáu phần hợp đồng, mọi độ đo khai báo phép gộp, mọi chiều thuộc ít nhất một thực thể, không có chỉ số mồ côi không ai dùng, và mọi khai báo có chủ sở hữu. Kiểm tra tĩnh về cấu trúc đồ thị: không có chu trình, không có thực thể cô lập, và mọi cặp thực thể dùng chung trong một chỉ số có đúng một đường kết được khai báo. Những kiểm tra này chạy trong tích hợp liên tục theo lesson 96 và chặn hợp nhất, nên một chỉ số thiếu hợp đồng không vào được nhánh chính. **Giá trị thật của tầng kiểm tra này là nó rẻ và chạy ở mọi lần nộp mã**, nên bắt lỗi trước khi ai đó nhìn thấy số sai.

**Outcome.** Dựng bộ kiểm tra định nghĩa và cấu trúc chạy trong tích hợp liên tục, chặn được năm loại vi phạm.

**Đánh giá.** Tầng *áp dụng*. Objective là một cửa chặn tự động có tiêu chí nghiệm thu bằng phép thử tiêm. Kiểm bằng năm vi phạm tiêm; đạt khi cả năm bị chặn và không khai báo hợp lệ nào bị chặn nhầm.

**Lab.** Viết bộ kiểm tra cho năm quy tắc định nghĩa và ba quy tắc cấu trúc đồ thị. Đưa vào quy trình tích hợp liên tục có cửa chặn hợp nhất. Nộp năm yêu cầu hợp nhất vi phạm năm quy tắc khác nhau và xác nhận cả năm bị chặn ở đúng quy tắc.

**Pitfalls.** Chỉ kiểm bằng cách chạy truy vấn · không chặn hợp nhất nên kiểm tra chỉ để tham khảo · viết kiểm tra cần dữ liệu nên chạy chậm và bị tắt · bỏ quy tắc bắt buộc có chủ sở hữu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Năm vi phạm đều bị chặn ở đúng quy tắc, và không khai báo hợp lệ nào bị chặn nhầm.

### Lesson 178 · Correctness tests and reconciliation against hand-written SQL `TH`
**Prerequisites.** Lesson 177

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Tầng thứ hai của tháp kiểm thử, và là tầng quyết định tầng ngữ nghĩa có đáng tin không. Bốn loại kiểm tra tính đúng. Đối soát với SQL viết tay: với mỗi chỉ số được chứng nhận, có một truy vấn viết tay độc lập trên bảng gốc và hai kết quả phải khớp ở ít nhất ba mức gộp, theo lesson 172; **truy vấn đối soát phải do người khác viết từ hợp đồng chứ chép từ SQL sinh ra**, nếu không thì nó chỉ lặp lại cùng một sai lầm. Kiểm bất biến: tổng con bằng tổng cha, tỉ lệ nằm trong khoảng hợp lệ, và chỉ số không âm khi không được phép âm. Kiểm ca biên: hợp đồng nguồn đòi bộ đối chứng phủ **sáu ca bắt buộc** chứ ba, vì mỗi ca làm sai một chỉ số theo một cách khác nhau: giá trị rỗng, bản ghi trùng, giao dịch hoàn tiền tức giá trị âm, dữ liệu tới muộn, thay đổi ở chiều biến đổi chậm, và ranh giới kỳ tài chính. Bộ đối chứng là tài sản cố định của module: nó không đổi giữa các lần chạy, nên mọi hồi quy đều quy được về thay đổi của mã chứ của dữ liệu. Kiểm hồi quy: khi định nghĩa đổi, so kết quả trước và sau trên cùng dữ liệu để biết chính xác cái gì đổi.

**Outcome.** Dựng bộ đối soát độc lập cho năm chỉ số và chứng minh khớp ở ba mức gộp cùng đủ sáu ca đối chứng bắt buộc.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu khắt khe là khớp tuyệt đối với nguồn độc lập. Kiểm bằng đối soát ba mức nhân sáu ca đối chứng; đạt khi năm chỉ số khớp ở mọi ô trong 18 ô và bộ kiểm chạy tự động.

**Lab.** Với năm chỉ số đã chứng nhận, nhờ một học viên khác viết truy vấn đối soát chỉ từ hợp đồng. Dựng bộ đối chứng cố định phủ đủ sáu ca: giá trị rỗng, trùng, hoàn tiền, tới muộn, chiều biến đổi chậm, và ranh giới kỳ tài chính. So kết quả ở ba mức gộp nhân sáu ca. Đưa bộ đối soát vào quy trình chạy hằng ngày. Đổi một định nghĩa và chạy kiểm hồi quy để liệt kê chính xác cái gì đổi.

**Pitfalls.** Viết truy vấn đối soát bằng cách chép SQL sinh ra · chỉ đối soát ở một mức gộp · bộ đối chứng thiếu ca hoàn tiền hoặc ca chiều biến đổi chậm · đổi bộ đối chứng giữa hai lần chạy nên không quy được hồi quy · không có kiểm hồi quy nên đổi định nghĩa mà không biết ảnh hưởng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Năm chỉ số khớp ở cả 18 ô ba mức nhân sáu ca đối chứng, và kiểm hồi quy liệt kê đúng phần thay đổi khi đổi định nghĩa.

### Lesson 179 · Serving, caching and performance `TH`
**Prerequisites.** Lesson 178

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Tầng ngữ nghĩa đứng trên đường truy vấn nên nó là một thành phần có hiệu năng, chứ chỉ một tệp khai báo. Ba đường phục vụ: truy vấn từ công cụ BI, từ SQL, và từ mã qua giao diện lập trình. Bảng tổng hợp tính sẵn là kỹ thuật tăng tốc chính: tính trước ở một hạt thô hơn rồi dùng lại; điều kiện dùng được là độ đo cộng được hoàn toàn theo lesson 169, và chọn hạt tính sẵn là đánh đổi giữa tốc độ với dung lượng cùng độ tươi. Bộ đệm kết quả và ba chiến lược làm mới, cùng vấn đề dữ liệu cũ. **Khoá đệm phải mang ngữ cảnh bảo mật và phiên bản ngữ nghĩa**: thiếu phần đầu thì một người thấy kết quả dựng từ dữ liệu ngoài quyền của họ, thiếu phần sau thì một định nghĩa đã đổi vẫn trả kết quả cũ; cả hai là điều kiện tự động không đạt của module. Phục vụ cho hai loại bên tiêu thụ cùng lúc là yêu cầu bắt buộc chứ tuỳ chọn, vì chỉ khi có hai bên mới lộ ra chỗ định nghĩa bị diễn giải khác nhau. Đồng thời và giới hạn: nhiều người cùng chạy truy vấn nặng làm kho quá tải, nên cần giới hạn tốc độ và hàng đợi theo lesson 87. Bốn chỉ số phải theo dõi: thời gian phản hồi phân vị 95, tỉ lệ trúng đệm, số truy vấn đồng thời, và chi phí trên mỗi truy vấn.

**Outcome.** Phục vụ hai loại bên tiêu thụ đạt ngưỡng thời gian phản hồi, với khoá đệm mang ngữ cảnh bảo mật và phiên bản ngữ nghĩa.

**Đánh giá.** Tầng *đánh giá*. Objective đòi tối ưu dưới hai ràng buộc đối nghịch là tốc độ và độ tươi. Kiểm bằng cặp số đo cộng phép thử cách ly đệm; đạt khi thời gian phân vị 95 dưới ngưỡng, độ tươi trong cam kết, và hai người dùng khác quyền không bao giờ nhận cùng một mục đệm.

**Lab.** Chạy bộ 20 truy vấn chuẩn và đo bốn chỉ số ở trạng thái chưa tối ưu. Dựng bảng tổng hợp tính sẵn cho các chỉ số cộng được. Bật đệm với chiến lược làm mới phù hợp. Đo lại. Phục vụ cùng bộ chỉ số cho hai bên tiêu thụ khác loại, ví dụ một công cụ báo cáo và một ứng dụng gọi qua giao diện lập trình, rồi đối soát hai bên cho cùng con số. Chạy phép thử cách ly đệm: hai người dùng khác quyền hỏi cùng câu, chứng minh không ai nhận mục đệm của người kia. Đổi một định nghĩa và chứng minh đệm cũ bị vô hiệu nhờ phiên bản ngữ nghĩa trong khoá.

**Pitfalls.** Dựng bảng tổng hợp cho chỉ số không cộng được · đặt thời gian sống của đệm dài hơn cam kết độ tươi · tối ưu mà đổi kết quả · **đặt khoá đệm bỏ ngữ cảnh bảo mật hoặc bỏ phiên bản ngữ nghĩa** · chỉ phục vụ một bên tiêu thụ rồi coi là đã kiểm · không đo chi phí trên mỗi truy vấn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Thời gian phân vị 95 dưới ngưỡng, độ tươi trong cam kết, hai bên tiêu thụ cho cùng con số, và phép thử cách ly đệm không có lần nào hai người khác quyền dùng chung một mục.

### Lesson 180 · Access control at the semantic layer `TH`
**Prerequisites.** Lesson 179

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Đặt kiểm soát truy cập ở tầng ngữ nghĩa có lợi thế lớn: một chỗ cưỡng chế cho mọi công cụ tiêu thụ, thay vì cấu hình lại ở từng công cụ BI. Ba mức kiểm soát: theo chỉ số tức ai được xem chỉ số nào, theo dòng tức mỗi người chỉ thấy dữ liệu thuộc phạm vi của mình, và theo cột tức che các trường nhạy cảm. Bảo mật mức dòng cài bằng cách gắn thuộc tính người dùng vào điều kiện lọc được áp tự động; ba cách lấy thuộc tính người dùng và đánh đổi. Cạm bẫy rò rỉ qua phép gộp: người không được xem dòng chi tiết nhưng được xem tổng có thể suy ra dòng chi tiết khi nhóm chỉ có một phần tử; cách chặn là đặt ngưỡng số phần tử tối thiểu cho mỗi nhóm. **Phép thử phủ định bắt buộc**: với mỗi chính sách, một phép kiểm chứng minh người không có quyền nhận được từ chối chứ nhận số đã lọc âm thầm.

**Outcome.** Cài ba mức kiểm soát và chứng minh bằng phép thử phủ định rằng không rò rỉ, kể cả qua phép gộp.

**Đánh giá.** Tầng *áp dụng*. Objective là một cơ chế bảo mật kiểm được bằng phép thử phủ định gồm cả đường rò gián tiếp. Kiểm bằng sáu phép thử; đạt khi cả sáu bị chặn đúng và đường rò qua phép gộp được chặn bằng ngưỡng nhóm.

**Lab.** Cài kiểm soát theo chỉ số, theo dòng và theo cột. Viết sáu phép thử phủ định gồm một phép thử suy ra dòng chi tiết từ nhóm một phần tử. Đặt ngưỡng số phần tử tối thiểu và chứng minh đường rò bị chặn. Kiểm rằng cùng chính sách có hiệu lực ở cả ba đường phục vụ.

**Pitfalls.** Cấu hình quyền ở từng công cụ BI thay vì ở tầng ngữ nghĩa · bỏ qua đường rò qua phép gộp · trả về số đã lọc âm thầm thay vì từ chối · không kiểm chính sách ở mọi đường phục vụ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Sáu phép thử phủ định đều bị chặn đúng, đường rò qua nhóm một phần tử bị chặn, và chính sách có hiệu lực ở cả ba đường phục vụ.

### Lesson 181 · Architecture alternatives - headless, BI-native or curated marts `LT`
**Prerequisites.** Lesson 180

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Ba kiến trúc cho cùng một mục tiêu, và chọn theo ràng buộc tổ chức chứ theo công nghệ. Tầng ngữ nghĩa độc lập: định nghĩa nằm ngoài mọi công cụ tiêu thụ, nên nhiều công cụ dùng chung một định nghĩa; đổi lại thêm một thành phần phải vận hành và không phải công cụ BI nào cũng tích hợp tốt. Tầng ngữ nghĩa trong công cụ BI: tiện, không thêm thành phần, nhưng định nghĩa bị khoá trong một công cụ nên đổi công cụ là làm lại từ đầu, và người dùng SQL không hưởng được. Mart đã chuẩn bị sẵn: không có tầng ngữ nghĩa, thay vào đó là bảng rộng theo lesson 159 với định nghĩa đã tính sẵn; đơn giản nhất và đủ cho nhiều đội, đổi lại thiếu linh hoạt và số tổ hợp bảng phình theo nhu cầu. Sáu chiều để chọn và ba tình huống mà mart chuẩn bị sẵn là lựa chọn đúng dù nghe kém hiện đại.

**Outcome.** Chọn kiến trúc cho ba bối cảnh tổ chức và nêu điều kiện làm lựa chọn đó sai.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn theo ràng buộc tổ chức, và chống việc mặc định chọn phương án phức tạp nhất. Kiểm bằng ba bối cảnh trong đó ít nhất một nên chọn mart chuẩn bị sẵn; đạt khi chọn đúng cả ba kèm điều kiện đảo ngược.

**Lab.** Cho ba bối cảnh khác nhau về số công cụ tiêu thụ, quy mô đội, và mức trưởng thành. Chấm ba kiến trúc trên sáu chiều cho từng bối cảnh, mỗi ô dẫn một quan sát từ lab của chính mình ở các bài trước. Chọn một và nêu hai điều kiện làm nó sai.

**Pitfalls.** Chọn tầng ngữ nghĩa độc lập cho đội hai người · giữ định nghĩa trong công cụ BI rồi khoá mình vào nó · chấm bằng tính từ · bỏ qua phương án mart chuẩn bị sẵn vì nghe đơn giản.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chọn đúng cả ba bối cảnh, mỗi ô trong bảng chấm dẫn một quan sát từ lab, và mỗi lựa chọn có hai điều kiện đảo ngược.

### Lesson 182 · Metric lifecycle - propose, certify, version, deprecate `TH`
**Prerequisites.** Lesson 181

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Chỉ số có vòng đời, và không quản vòng đời thì danh mục phình tới mức không ai tin được cái nào. Năm trạng thái và điều kiện chuyển: đề xuất, đang rà soát, đã chứng nhận, đã khai tử, và đã gỡ. Điều kiện để được chứng nhận là danh mục kiểm lấy từ các bài trước: hợp đồng sáu phần đủ, qua bốn bước chứng minh không đếm trùng ở lesson 172, có bộ đối soát độc lập ở lesson 178, có ma trận tương thích ở lesson 173, và có chủ sở hữu. Phân loại thay đổi thành ba mức và quy trình tương ứng: thay đổi không ảnh hưởng số, thay đổi làm số đổi, và thay đổi phá vỡ tương thích; **mức hai là mức nguy hiểm nhất vì nó im lặng**, nên bắt buộc phải thông báo và phải chạy kiểm hồi quy. Với mức ba, thông báo là chưa đủ: hợp đồng nguồn đòi **chạy song song hai phiên bản, đối soát chênh lệch giữa chúng, lấy chấp thuận của bên tiêu thụ, rồi mới gỡ bản cũ**, và toàn bộ được ghi thành một bản ghi khai tử. Lý do chạy song song: chênh lệch giữa hai phiên bản là con số duy nhất cho bên tiêu thụ biết báo cáo của họ sẽ đổi bao nhiêu; không có nó thì họ chỉ nhận được một lời hứa. **Sửa đè công thức tại chỗ mà không có phiên bản mới là điều kiện tự động không đạt**, vì nó làm mọi số lịch sử đổi nghĩa mà không ai truy được. Khai tử có cửa sổ chuyển tiếp và cảnh báo cho người đang dùng. **Quy trình khai tử là quy trình hay bị bỏ quên nhất** và là lý do danh mục phình mãi.

**Outcome.** Vận hành vòng đời năm trạng thái, và thực hiện một lần đổi công thức phá vỡ theo quy trình chạy song song cộng đối soát cộng bản ghi khai tử.

**Đánh giá.** Tầng *áp dụng*. Objective là một quy trình quản trị có tiêu chí nghiệm thu bằng việc chặn đúng và khai tử sạch. Kiểm bằng ba chỉ số đi qua vòng đời cộng một lần di trú phá vỡ; đạt khi chỉ số thiếu điều kiện bị chặn chứng nhận, lần di trú có số chênh lệch đo được giữa hai phiên bản, và chỉ số khai tử không còn người dùng khi gỡ.

**Lab.** Dựng vòng đời năm trạng thái với cửa chặn tự động cho danh mục chứng nhận. Đưa ba chỉ số qua vòng đời, trong đó một cái thiếu bộ đối soát và phải bị chặn. Thực hiện một lần đổi định nghĩa mức hai với thông báo và kiểm hồi quy. Thực hiện một lần đổi công thức mức ba theo đủ quy trình: tạo phiên bản thứ hai, chạy song song cả hai trên cùng dữ liệu ít nhất một chu kỳ, đối soát và báo cho bên tiêu thụ chênh lệch bằng số, lấy chấp thuận, rồi gỡ bản cũ và nộp bản ghi khai tử. Khai tử một chỉ số với cửa sổ chuyển tiếp và xác nhận không còn ai dùng trước khi gỡ.

**Pitfalls.** Chứng nhận chỉ số chưa có bộ đối soát · **sửa đè công thức tại chỗ thay vì tạo phiên bản mới** · gỡ bản cũ trước khi có chấp thuận của bên tiêu thụ · đổi định nghĩa làm số đổi mà không thông báo · gỡ chỉ số khi còn người dùng · không có quy trình khai tử nên danh mục chỉ phình.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chỉ số thiếu điều kiện bị chặn chứng nhận, đổi công thức mức ba có chạy song song kèm số chênh lệch và chấp thuận của bên tiêu thụ, bản ghi khai tử đầy đủ, và chỉ số khai tử không còn người dùng khi gỡ.

### Lesson 183 · Ownership, change classification and the failure matrix `TH`
**Prerequisites.** Lesson 182

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài chốt phần quản trị. Mô hình sở hữu ba vai và ranh giới: chủ sở hữu nghiệp vụ quyết định nghĩa, chủ sở hữu kỹ thuật chịu trách nhiệm cài đặt và vận hành, người quản trị danh mục giữ quy trình. Thiếu vai thứ nhất là nguyên nhân phổ biến nhất khiến định nghĩa không ai dám chốt. Ma trận chế độ hỏng của tầng ngữ nghĩa, mỗi dòng gồm hiện tượng, nguyên nhân gốc, cách phát hiện, và cách chặn; sáu chế độ hỏng chính đã gặp rải rác nay gom thành một bảng dùng được khi trực: đếm trùng, phép kết mơ hồ, gộp sai loại độ đo, ngữ nghĩa thời gian lệch, rò rỉ qua phép gộp, **đệm bỏ ngữ cảnh bảo mật hoặc bỏ phiên bản ngữ nghĩa** theo lesson 179, và **công thức bị sửa đè tại chỗ nên số lịch sử đổi nghĩa** theo lesson 182. Hai chế độ hỏng cuối nguy hiểm hơn phần còn lại vì chúng không sinh ra con số lạ: kết quả vẫn nằm trong khoảng hợp lý, chỉ là thuộc về người khác hoặc thuộc về một định nghĩa khác. **Với mỗi chế độ hỏng phải có một phép kiểm tự động phát hiện được**, nếu không thì nó sẽ tái diễn. Phân tích sau sự cố cho một lần số sai đã công bố ra ngoài.

**Outcome.** Lập ma trận chế độ hỏng có phép kiểm tự động cho từng dòng, và gán được ba vai sở hữu cho bộ chỉ số.

**Đánh giá.** Tầng *đánh giá*. Objective đòi tổng hợp các lỗi đã gặp thành một hệ phòng vệ. Kiểm bằng phép thử tiêm bảy lỗi; đạt khi ít nhất sáu bị phép kiểm tự động phát hiện và ba vai được gán rõ.

**Lab.** Lập ma trận bảy chế độ hỏng với đủ bốn cột. Với mỗi dòng, viết một phép kiểm tự động. Giảng viên tiêm bảy lỗi tương ứng, trong đó có một mục đệm dùng lại xuyên người dùng và một công thức bị sửa đè, rồi đếm bao nhiêu cái bị phát hiện. Gán ba vai cho bộ chỉ số đã dựng. Viết phân tích sau sự cố cho một lần số sai công bố ra ngoài.

**Pitfalls.** Gán chủ sở hữu nghiệp vụ cho một nhóm thay vì một người · viết cách chặn mà không có phép kiểm tự động · bỏ chế độ hỏng rò rỉ qua phép gộp · bỏ hai chế độ hỏng về đệm và về sửa đè công thức vì chúng không sinh số lạ · phân tích sau sự cố quy về lỗi cá nhân.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** ≥ 6/7 lỗi tiêm bị phép kiểm tự động phát hiện, ba vai được gán rõ, và phân tích sau sự cố không đổ lỗi cá nhân.

### Lesson 184 · Capstone - a governed revenue semantic product `DA`
**Prerequisites.** Lesson 183

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Bài dự án khép module, lấy đúng yêu cầu capstone của hợp đồng nguồn. Dựng một sản phẩm ngữ nghĩa cho miền doanh thu. Sản phẩm nộp gồm chín hạng mục, lấy đúng ngưỡng của hợp đồng nguồn: hợp đồng sáu phần cho **ít nhất 15 chỉ số thuộc ít nhất năm loại**, mỗi chỉ số có chủ sở hữu và có phép kiểm; **ít nhất ba mô hình ngữ nghĩa**, và một truy vấn đi qua nhiều bước kết kèm chứng minh bản số cùng chứng minh không nhân dòng; ma trận tương thích chỉ số nhân chiều; bộ kiểm ba tầng gồm định nghĩa, tính đúng và tích hợp; bộ đối chứng cố định phủ đủ sáu ca ở lesson 178; SQL sinh ra cùng kế hoạch thực thi được soi cho một ma trận truy vấn đại diện; **phục vụ hai loại bên tiêu thụ** có bảo mật theo dòng cùng theo khách hàng và có phép thử cách ly đệm theo lesson 179; một lần **di trú phá vỡ hoàn chỉnh** gồm chạy song song, đối soát, chấp thuận của bên tiêu thụ và bản ghi khai tử theo lesson 182; và tài liệu vòng đời gồm trạng thái từng chỉ số cùng ba vai sở hữu. Sáu điều kiện tự động không đạt, lấy đủ từ phần *Critical failures* của nguồn: chỉ số thiếu tập hợp, thời gian, hạt hoặc chủ sở hữu; đồ thị kết cho phép đếm trùng im lặng; lấy sự đồng thuận trên bảng điều khiển làm bằng chứng đúng duy nhất; **sửa đè công thức tại chỗ khi thay đổi phá vỡ, không có di trú**; **đệm bỏ ngữ cảnh bảo mật hoặc bỏ phiên bản ngữ nghĩa**; và công cụ biên dịch xanh nhưng không có đối soát độc lập.

**Outcome.** Nộp sản phẩm ngữ nghĩa đủ chín hạng mục với 15 chỉ số thuộc năm loại, không vi phạm sáu điều kiện tự động không đạt.

**Đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module thành một sản phẩm có quản trị. Kiểm bằng rà soát chín hạng mục cộng đối soát độc lập; đạt khi cả 15 chỉ số khớp đối soát ở ba mức gộp nhân sáu ca đối chứng và không vi phạm điều kiện nào.

**Lab.** Dựng sản phẩm theo chín hạng mục. Nhờ một học viên khác viết bộ đối soát chỉ từ hợp đồng. So ở ba mức gộp nhân sáu ca đối chứng. Chạy phép thử phủ định cho chính sách truy cập và phép thử cách ly đệm. Thực hiện trọn một lần di trú phá vỡ và nộp bản ghi khai tử. Người chấm đổi một hạt, một mốc thời gian hoặc một quy tắc nghiệp vụ; thiết kế phải xác định đúng phạm vi ảnh hưởng và đúng đường di trú. Trình bày 15 phút và trả lời chất vấn về một chỉ số bất kỳ: chỉ số đó tính trên tập nào, ở hạt nào, và vì sao không đếm trùng.

**Pitfalls.** Khai báo chỉ số theo cột có sẵn thay vì theo hợp đồng · tự viết bộ đối soát của chính mình · nộp đủ số lượng chỉ số nhưng dồn vào hai ba loại · bỏ phần di trú phá vỡ vì tốn một chu kỳ chạy song song · bỏ chính sách truy cập vì thấy môi trường thử không cần.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Chín hạng mục đầy đủ với ≥ 15 chỉ số thuộc ≥ 5 loại và ≥ 3 mô hình ngữ nghĩa, mọi chỉ số khớp đối soát độc lập ở ba mức gộp nhân sáu ca đối chứng, di trú phá vỡ hoàn tất có bản ghi khai tử, và không vi phạm sáu điều kiện tự động không đạt.

# MODULE M11C · ANALYTICAL DATA PRODUCT AND SELF-SERVICE

**Phase 5 · Lessons 185–202 · 36 giờ**

| | |
|---|---|
| **Objective cấp module** | Biến một yêu cầu mơ hồ thành quyết định, câu hỏi, cây chỉ số và tiêu chí nghiệm thu; rồi dựng một sản phẩm dữ liệu có chủ, có hợp đồng, có tài liệu và có bằng chứng người dùng dùng được |
| **Tiền đề** | M11B |
| **Exit criterion** | Chứng minh tự phục vụ bằng phép thử khả dụng theo tác vụ, không bằng số dashboard đã tạo; mọi chỉ số truy được về một quyết định nghiệp vụ |
| **Kỹ năng SFIA** | `DATM` mức 5 · `DTAN` mức 4 |
| **Chế độ hỏng** | Trở thành người viết dbt giỏi mà không hiểu người tiêu thụ, quyết định và vòng đời sản phẩm, nên dựng ra mart đúng kỹ thuật mà không ai dùng |

**Module thứ hai thuộc phần bù Analytics Engineer**, và là module ngăn việc người học thành người viết mã biến đổi thuần tuý.

Ranh giới lấy từ hợp đồng nguồn: đây không phải curriculum Business Analyst. Trọng tâm là **truy được từ chỉ số ngược về quyết định**, và chứng minh người khác dùng được sản phẩm của mình.

Nguyên tắc chấm nghiêm nhất: số dashboard đã tạo, số bảng đã dựng và số người có quyền truy cập đều **không** phải bằng chứng tự phục vụ.

### Lesson 185 · Decision-first discovery `LT`
**Prerequisites.** Module 11C: M11B

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài mở module bằng cách đảo ngược thứ tự quen thuộc: bắt đầu từ quyết định chứ từ dữ liệu có sẵn. Bốn câu hỏi phải trả lời trước khi dựng bất cứ thứ gì: quyết định nào sẽ được đưa ra, ai đưa ra, theo nhịp nào, và hành động thay đổi ra sao tuỳ kết quả. Câu cuối là câu lọc mạnh nhất: nếu mọi kết quả đều dẫn tới cùng một hành động thì phân tích đó không cần làm. Phân biệt ba loại yêu cầu và cách xử lý khác nhau: yêu cầu có quyết định rõ, yêu cầu tò mò không gắn hành động, và yêu cầu thực ra là một yêu cầu vận hành chứ phân tích. Nối với lesson 1: phát biểu bài toán sáu phần áp vào đây với phần phi mục tiêu đặc biệt quan trọng. Ba câu hỏi để phát hiện yêu cầu là dashboard theo thói quen chứ theo nhu cầu quyết định thật.

**Outcome.** Chuyển một yêu cầu mơ hồ thành phát biểu quyết định đủ bốn phần và nhận ra yêu cầu không dẫn tới hành động nào.

**Đánh giá.** Tầng *áp dụng*. Bài mở module, áp một khung phỏng vấn vào tình huống mới. Kiểm bằng năm yêu cầu trong đó ít nhất một không dẫn tới hành động; đạt khi bốn phần đầy đủ ở ít nhất bốn yêu cầu và nhận ra đúng yêu cầu nên từ chối.

**Lab.** Nhận năm yêu cầu viết theo cách người nghiệp vụ thật hay nhắn. Phỏng vấn giảng viên đóng vai người yêu cầu để chốt bốn phần cho từng cái. Nhận ra yêu cầu nào không dẫn tới hành động khác nhau và viết cách từ chối hoặc chuyển hướng nó.

**Pitfalls.** Nhận mọi yêu cầu rồi dựng dashboard · bỏ câu hỏi hành động thay đổi ra sao · nhầm yêu cầu vận hành với yêu cầu phân tích · phỏng vấn bằng câu hỏi đóng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn phần đầy đủ ở ≥ 4/5 yêu cầu, và nhận ra đúng yêu cầu không dẫn tới hành động kèm cách xử lý.

### Lesson 186 · Question decomposition and the metric tree `TH`
**Prerequisites.** Lesson 185

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Một quyết định phân rã thành câu hỏi, câu hỏi phân rã thành chỉ số, và chỉ số phân rã thành thành phần điều khiển được. Cây chỉ số là công cụ trung tâm: chỉ số đầu ra ở gốc, các thành phần nhân hoặc cộng ở dưới, cho tới khi tới các lá mà một đội cụ thể tác động được. Phép thử của một cây tốt: **mọi lá có người sở hữu và có đòn bẩy tác động được**, nếu không thì cây chỉ là phép chia số học không dẫn tới hành động. Ví dụ phân rã doanh thu thành số khách nhân tần suất nhân giá trị đơn nhân biên lợi nhuận, rồi mỗi thành phần lại phân rã tiếp. Phân biệt chỉ số dẫn dắt với chỉ số kết quả và vì sao dashboard chỉ có chỉ số kết quả thì luôn tới muộn. Mỗi chỉ số trong cây phải trỏ tới một hợp đồng sáu phần ở lesson 166 chứ chỉ một cái tên.

**Outcome.** Dựng cây chỉ số từ một quyết định sao cho mọi lá có chủ và có đòn bẩy, và mọi nút trỏ tới một hợp đồng.

**Đánh giá.** Tầng *áp dụng*. Objective có phép thử khách quan ở mọi lá. Kiểm bằng rà soát cây; đạt khi mọi lá có chủ và đòn bẩy, và mọi nút dẫn được tới một hợp đồng chỉ số.

**Lab.** Từ một quyết định đã chốt ở lesson 185, dựng cây chỉ số ba tầng. Với mỗi lá, ghi đội sở hữu và đòn bẩy cụ thể họ tác động được. Với mỗi nút, trỏ tới hợp đồng tương ứng. Đánh dấu chỉ số nào là dẫn dắt và chỉ số nào là kết quả.

**Pitfalls.** Phân rã tới mức không ai tác động được · để lá không có chủ · dựng cây chỉ toàn chỉ số kết quả · đặt tên chỉ số mà không có hợp đồng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mọi lá có chủ và đòn bẩy cụ thể, mọi nút dẫn tới một hợp đồng, và chỉ số dẫn dắt được đánh dấu tách khỏi chỉ số kết quả.

### Lesson 187 · Requirements traceability `TH`
**Prerequisites.** Lesson 186

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Khả năng truy ngược là thứ phân biệt một sản phẩm dữ liệu với một đống bảng. Chuỗi truy ngược đầy đủ có năm mắt: quyết định, câu hỏi, chỉ số, mô hình, và bảng nguồn. Từ bất kỳ mắt nào phải đi được cả hai chiều: từ một cột trong bảng nguồn trả lời được nó phục vụ quyết định nào, và từ một quyết định liệt kê được mọi thứ nó phụ thuộc. Công dụng thực tế và đo được: khi một nguồn đổi lược đồ thì biết ngay quyết định nào bị ảnh hưởng để báo đúng người; và khi cần cắt chi phí thì biết bảng nào không phục vụ quyết định nào để bỏ. Cách ghi lại chuỗi truy ngược: ma trận truy ngược trong kho mã chứ trong tài liệu rời, để nó được rà soát cùng mã. Quan hệ với lineage kỹ thuật ở M14D: lineage nối bảng với bảng, còn truy ngược nối bảng với quyết định, và cần cả hai.

**Outcome.** Dựng ma trận truy ngược năm mắt và trả lời được cả hai chiều cho ba truy vấn kiểm tra.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu bằng việc trả lời câu hỏi hai chiều. Kiểm bằng ba câu hỏi truy ngược; đạt khi trả lời đúng cả ba chỉ bằng ma trận và tìm được ít nhất một bảng không phục vụ quyết định nào.

**Lab.** Dựng ma trận truy ngược năm mắt cho sản phẩm đang làm, lưu trong kho mã. Trả lời ba câu hỏi: nguồn này đổi thì quyết định nào ảnh hưởng, quyết định này phụ thuộc những bảng nào, và bảng nào không phục vụ quyết định nào. Đề xuất bỏ những bảng ở câu cuối.

**Pitfalls.** Lưu ma trận truy ngược trong tài liệu rời nên nó lạc hậu ngay · chỉ truy được một chiều · nhầm lineage kỹ thuật với truy ngược tới quyết định · bỏ mắt câu hỏi nên nhảy thẳng từ quyết định sang chỉ số.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Trả lời đúng cả ba câu hỏi chỉ bằng ma trận, và tìm được ít nhất một bảng không phục vụ quyết định nào.

### Lesson 188 · Product anatomy - what makes a dataset a product `LT`
**Prerequisites.** Lesson 187

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài phân biệt sáu thứ hay bị gọi chung là sản phẩm dữ liệu: tập dữ liệu, mart, dashboard, mô hình ngữ nghĩa, giao diện chỉ số, và sản phẩm dữ liệu. Tám thuộc tính làm một tập dữ liệu thành sản phẩm: có chủ sở hữu tên cụ thể, có người tiêu thụ xác định, có giao diện ổn định, có hợp đồng, có cam kết mức dịch vụ, có tài liệu, có chính sách truy cập, và có kế hoạch khai tử. Thiếu thuộc tính cuối là dấu hiệu rõ nhất của một thứ chưa phải sản phẩm: **không ai nghĩ tới việc nó sẽ chết thì nó sẽ sống mãi mà không ai dùng**. So sánh với sản phẩm phần mềm: điểm giống là vòng đời và hợp đồng, điểm khác là người tiêu thụ thường không biết mình cần gì cho tới khi thấy số. Ba mức trưởng thành và cách nhận ra đội đang ở mức nào.

**Outcome.** Chấm một tập dữ liệu theo tám thuộc tính và chỉ ra nó ở mức trưởng thành nào.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết đặt tiêu chuẩn cho phần còn lại của module. Kiểm bằng bài chấm ba tập dữ liệu; đạt khi chấm đúng ít nhất hai theo tám thuộc tính và chỉ đúng thuộc tính thiếu quan trọng nhất.

**Lab.** Chấm ba tập dữ liệu thật trong dự án theo tám thuộc tính, mỗi thuộc tính có hoặc không kèm bằng chứng. Với tập yếu nhất, chỉ ra thuộc tính thiếu nào gây hậu quả lớn nhất và vì sao. Phân loại sáu khái niệm ở phần đầu bài bằng ví dụ từ dự án của mình.

**Pitfalls.** Gọi mọi bảng là sản phẩm dữ liệu · gán chủ sở hữu là một phòng ban thay vì một người · bỏ kế hoạch khai tử · nhầm dashboard với sản phẩm dữ liệu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chấm đúng ≥ 2/3 tập dữ liệu theo tám thuộc tính kèm bằng chứng, và sáu khái niệm được phân loại bằng ví dụ thật.

### Lesson 189 · Interface design for an analytical product `TH`
**Prerequisites.** Lesson 188

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Giao diện của một sản phẩm dữ liệu là thứ người tiêu thụ dựa vào, nên nó là phần phải ổn định nhất. Bốn dạng giao diện và điều kiện dùng: bảng trong kho, khung nhìn, giao diện chỉ số qua tầng ngữ nghĩa ở M11B, và tệp xuất ra. Nguyên tắc thiết kế: **lộ ra ít nhất có thể**, vì mọi cột lộ ra đều thành hợp đồng mà ai đó sẽ dựa vào, theo đúng nguyên tắc che giấu thông tin ở lesson 90. Ba quyết định phải chốt: hạt của giao diện, tập cột công khai so với cột nội bộ, và quy ước đặt tên. Quy ước đặt tên nhất quán quan trọng hơn quy ước đẹp; đặt tên theo từ vựng nghiệp vụ ở lesson 89 chứ theo tên cột nguồn. Ba cách người tiêu thụ sẽ dùng sai giao diện nếu không thiết kế trước, và cách chặn từng cái bằng thiết kế chứ bằng tài liệu.

**Outcome.** Thiết kế giao diện cho một sản phẩm với tập cột công khai tối thiểu và chứng minh nó đủ cho ba câu hỏi nghiệp vụ.

**Đánh giá.** Tầng *áp dụng*. Objective có hai ràng buộc đối nghịch là tối thiểu và đủ dùng. Kiểm bằng ba câu hỏi nghiệp vụ; đạt khi cả ba trả lời được bằng tập cột công khai và không cột nội bộ nào bị lộ.

**Lab.** Thiết kế giao diện cho sản phẩm đang làm: chốt hạt, chia cột công khai và nội bộ, đặt tên theo từ vựng nghiệp vụ. Kiểm bằng ba câu hỏi nghiệp vụ. Nhờ một học viên dùng thử và ghi lại mọi lần họ phải hỏi cột này nghĩa là gì.

**Pitfalls.** Lộ toàn bộ cột cho tiện · đặt tên cột theo tên ở hệ nguồn · đổi hạt của giao diện sau khi có người dùng · dựa vào tài liệu để chặn cách dùng sai thay vì thiết kế.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba câu hỏi nghiệp vụ trả lời được bằng tập cột công khai, không cột nội bộ nào lộ ra, và người dùng thử không phải hỏi nghĩa cột.

### Lesson 190 · Contract compatibility for consumers `TH`
**Prerequisites.** Lesson 189

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hợp đồng của sản phẩm dữ liệu gồm những gì và đổi nó thế nào cho an toàn. Năm phần: lược đồ, ngữ nghĩa từng trường, cam kết chất lượng, cam kết độ tươi, và quy trình thay đổi. Ba mức thay đổi theo đúng phân loại ở lesson 94 và 182: tương thích, làm đổi số, và phá vỡ. Quy tắc: **thêm cột thì an toàn, đổi nghĩa một cột mà giữ nguyên tên là mức nguy hiểm nhất vì không có gì báo hiệu**. Quy trình đổi hai giai đoạn cho thay đổi phá vỡ, theo lesson 97: thêm cái mới, chạy song song, thông báo, cho cửa sổ chuyển, rồi mới bỏ cái cũ. Cửa sổ chuyển đủ dài là bao lâu và ai quyết. Phát hiện ai đang dùng cái sắp bỏ: đây là chỗ nhật ký truy vấn và lineage ở M14D trả cổ tức, vì không biết ai dùng thì không dám bỏ gì cả.

**Outcome.** Thực hiện một thay đổi phá vỡ theo quy trình hai giai đoạn mà không làm bên tiêu thụ nào lỗi.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu bằng việc bên tiêu thụ không lỗi lần nào. Kiểm bằng thí nghiệm đổi có tải; đạt khi không bên tiêu thụ nào lỗi và danh sách người dùng cái cũ được xác định trước khi bỏ.

**Lab.** Viết hợp đồng năm phần cho sản phẩm. Thực hiện ba thay đổi ở ba mức. Với thay đổi phá vỡ, xác định ai đang dùng bằng nhật ký truy vấn, chạy quy trình hai giai đoạn với cửa sổ chuyển, và chứng minh không bên nào lỗi. Thực hiện một thay đổi mức hai và chứng minh có thông báo.

**Pitfalls.** Đổi nghĩa một cột mà giữ nguyên tên · bỏ cột cũ ngay sau khi thêm cột mới · không biết ai đang dùng · cửa sổ chuyển do kỹ thuật tự đặt.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Không bên tiêu thụ nào lỗi qua toàn bộ quá trình, danh sách người dùng được xác định trước khi bỏ, và thay đổi mức hai có thông báo.

### Lesson 191 · The documentation hierarchy `TH`
**Prerequisites.** Lesson 190

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Tài liệu cho sản phẩm dữ liệu có bốn tầng phục vụ bốn nhu cầu khác nhau, và viết gộp làm cả bốn không dùng được. Tầng khám phá trả lời sản phẩm này là gì và có phải thứ tôi cần không, đọc trong 30 giây. Tầng bắt đầu trả lời làm sao dùng ngay, gồm ba truy vấn mẫu chạy được. Tầng tham chiếu mô tả từng trường, từng chỉ số, hạt, và độ tươi. Tầng ngữ cảnh giải thích quyết định thiết kế và **hạn chế diễn giải** tức kết luận nào dữ liệu này không cho phép rút ra, phần đã nêu ở lesson 163 và là phần chặn nhiều kết luận sai nhất. Nguyên tắc chung: tài liệu nằm cạnh mã và được rà soát cùng mã, chứ trong một trang wiki rời sẽ lạc hậu sau ba tháng. Ba thứ không nên có trong tài liệu vì chúng chắc chắn lạc hậu.

**Outcome.** Viết bộ tài liệu bốn tầng và chứng minh người lạ tìm được sản phẩm rồi dùng được trong giới hạn thời gian.

**Đánh giá.** Tầng *áp dụng*. Objective đo bằng thời gian và kết quả của người đọc, chứ bằng độ dài tài liệu. Kiểm bằng phép thử tính giờ; đạt khi người lạ quyết định được sản phẩm có phù hợp trong 30 giây và chạy được truy vấn đầu trong 10 phút.

**Lab.** Viết bộ tài liệu bốn tầng cho sản phẩm. Nhờ một học viên chưa biết sản phẩm: tính giờ xem họ mất bao lâu để quyết định sản phẩm có phù hợp nhu cầu không, và bao lâu để chạy được truy vấn đầu tiên. Ghi lại mọi chỗ họ phải hỏi.

**Pitfalls.** Viết một trang dài cho mọi nhu cầu · bỏ hạn chế diễn giải · để tài liệu trong wiki rời khỏi mã · đưa ảnh chụp màn hình vào tài liệu tham chiếu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Người lạ quyết định được trong 30 giây và chạy được truy vấn đầu trong 10 phút, và bốn tầng tài liệu đều có nội dung.

### Lesson 192 · Search, discovery and the findability test `TH`
**Prerequisites.** Lesson 191

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Sản phẩm tốt mà không ai tìm thấy thì bằng không tồn tại, và khả năng tìm thấy là thứ đo được chứ giả định. Bốn yếu tố quyết định: tên đặt theo từ người dùng tìm chứ theo từ kỹ thuật, mô tả một dòng chứa từ khoá họ dùng, nhãn phân loại theo miền nghiệp vụ, và chỉ dấu mức độ tin cậy như đã chứng nhận hay còn thử nghiệm. Phép thử khả năng tìm thấy: cho năm người dùng thật một nhu cầu và tính tỉ lệ họ tìm ra đúng sản phẩm trong ba phút mà không hỏi ai; **tỉ lệ đó là chỉ số, không phải số sản phẩm đã đăng ký trong danh mục**. Ba lý do khiến người dùng dựng bản sao riêng thay vì dùng sản phẩm có sẵn, và cả ba đều là lỗi của khả năng tìm thấy chứ của người dùng. Quan hệ với danh mục dữ liệu ở M14D: danh mục là công cụ, còn khả năng tìm thấy là kết quả.

**Outcome.** Đo tỉ lệ tìm thấy bằng phép thử với người dùng thật và cải thiện được tỉ lệ đó sau một vòng sửa.

**Đánh giá.** Tầng *đánh giá*. Objective đo bằng hành vi người dùng chứ bằng cấu hình công cụ. Kiểm bằng phép thử hai vòng; đạt khi có số đo cả hai vòng và vòng sau cao hơn vòng trước.

**Lab.** Chạy phép thử khả năng tìm thấy với năm người, mỗi người một nhu cầu, tính giờ ba phút. Ghi tỉ lệ tìm ra và mọi từ khoá họ đã thử mà không ra kết quả. Sửa tên, mô tả và nhãn theo danh sách đó. Chạy lại với năm người khác và so hai tỉ lệ.

**Pitfalls.** Đo bằng số sản phẩm đã đăng ký · đặt tên theo tên bảng kỹ thuật · bỏ chỉ dấu mức tin cậy · kết luận người dùng lười tìm thay vì sửa khả năng tìm thấy.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Có tỉ lệ tìm thấy ở cả hai vòng với vòng sau cao hơn, và danh sách từ khoá thất bại được dùng để sửa.

### Lesson 193 · Documentation tests `TH`
**Prerequisites.** Lesson 192

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Tài liệu sai còn nguy hiểm hơn không có tài liệu, vì người đọc tin nó. Bốn loại kiểm tự động giữ tài liệu khớp thực tế: mọi cột công khai có mô tả, mọi truy vấn mẫu trong tài liệu chạy được và trả về dòng, mọi chỉ số nhắc trong tài liệu tồn tại trong tầng ngữ nghĩa, và cam kết độ tươi trong tài liệu khớp lịch làm mới thật. Loại thứ hai là loại có giá trị cao nhất và hay bị bỏ: truy vấn mẫu hỏng là thứ người mới gặp đầu tiên và mất niềm tin ngay. Những kiểm tra này chạy trong tích hợp liên tục và chặn hợp nhất theo lesson 96, nên tài liệu không thể lạc hậu quá một lần nộp mã. **Nguyên tắc: tài liệu là mã, nên nó được kiểm như mã.** Ba thứ không kiểm tự động được và cần rà soát người, gồm cả phần hạn chế diễn giải.

**Outcome.** Dựng bốn loại kiểm tài liệu chạy tự động và chặn được tài liệu lạc hậu ở mức nộp mã.

**Đánh giá.** Tầng *áp dụng*. Objective là một cửa chặn tự động có tiêu chí nghiệm thu bằng phép thử tiêm. Kiểm bằng bốn vi phạm tiêm; đạt khi cả bốn bị chặn ở đúng loại kiểm.

**Lab.** Viết bốn loại kiểm tài liệu và đưa vào quy trình có cửa chặn. Tiêm bốn vi phạm: thêm cột công khai không mô tả, làm hỏng một truy vấn mẫu, nhắc một chỉ số đã khai tử, và đổi lịch làm mới mà không sửa tài liệu. Xác nhận cả bốn bị chặn. Liệt kê ba thứ phải rà soát bằng người.

**Pitfalls.** Chỉ kiểm sự tồn tại của tài liệu chứ không kiểm nội dung · không chạy truy vấn mẫu · để tài liệu ngoài quy trình kiểm · tin rằng kiểm tự động thay được rà soát người.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn vi phạm đều bị chặn ở đúng loại kiểm, và ba thứ cần rà soát người được liệt kê rõ.

### Lesson 194 · Self-service UX and the enablement boundary `LT`
**Prerequisites.** Lesson 193

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Tự phục vụ là mục tiêu hay được tuyên bố và hiếm khi đạt, vì nó thường bị hiểu thành cấp quyền truy cập cho nhiều người hơn. Bốn điều kiện thật của tự phục vụ: người dùng tìm được sản phẩm theo lesson 192, hiểu được nghĩa mà không hỏi, dùng được mà không viết SQL phức tạp, và tin được số. Thiếu điều kiện nào thì họ quay lại hỏi đội dữ liệu, và khi đó tự phục vụ chỉ tồn tại trên giấy. Ranh giới hỗ trợ: đội dữ liệu chịu trách nhiệm tới đâu và người dùng tự lo từ đâu; ranh giới mơ hồ làm đội dữ liệu thành bộ phận trả lời câu hỏi lặt vặt. Ba mức tự phục vụ theo độ khó câu hỏi, và việc **không phải câu hỏi nào cũng nên tự phục vụ**: câu hỏi cần suy luận nhân quả thì vẫn cần người phân tích, và nói rõ điều đó là trung thực chứ thất bại.

**Outcome.** Chấm mức tự phục vụ hiện tại theo bốn điều kiện và xác định ranh giới hỗ trợ cho một đội cho trước.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết chuẩn bị cho phép thử khả dụng ở lesson 195. Kiểm bằng bài chấm cộng bài phân loại; đạt khi chấm bốn điều kiện có bằng chứng và phân đúng ít nhất bảy trong mười câu hỏi theo ba mức.

**Lab.** Chấm sản phẩm hiện tại theo bốn điều kiện, mỗi điều kiện kèm bằng chứng chứ cảm nhận. Phân mười câu hỏi nghiệp vụ thật vào ba mức tự phục vụ. Viết ranh giới hỗ trợ một trang nêu rõ đội dữ liệu lo gì và người dùng lo gì.

**Pitfalls.** Đo tự phục vụ bằng số người có quyền truy cập · hứa mọi câu hỏi đều tự phục vụ được · không có ranh giới hỗ trợ nên đội thành bộ phận hỏi đáp · chấm bằng cảm nhận.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn điều kiện được chấm có bằng chứng, phân đúng ≥ 7/10 câu hỏi vào ba mức, và ranh giới hỗ trợ nêu rõ hai phía.

### Lesson 195 · Task-based usability testing `TH`
**Prerequisites.** Lesson 194

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài đặt ra phương pháp đo duy nhất được chấp nhận trong module này. Phép thử khả dụng theo tác vụ: đưa người dùng thật một tác vụ nghiệp vụ, không hướng dẫn, tính giờ và ghi lại mọi chỗ họ vấp; **không hỏi họ thấy có dễ dùng không**, vì câu trả lời đó không dự đoán được hành vi. Bốn số đo: tỉ lệ hoàn thành, thời gian tới kết quả đúng, số lần phải hỏi người khác, và số lần ra kết quả sai mà họ tin là đúng; số đo thứ tư là số đo quan trọng nhất và hay bị bỏ, vì kết quả sai mà tự tin nguy hiểm hơn không ra kết quả. Cỡ mẫu đủ dùng: năm người phát hiện phần lớn vấn đề nghiêm trọng. Quy trình: chuẩn bị tác vụ, chạy, tổng hợp theo mức nghiêm trọng, sửa, rồi chạy lại vòng hai với người khác.

**Outcome.** Chạy được hai vòng thử khả dụng và chứng minh bốn số đo cải thiện ở vòng hai.

**Đánh giá.** Tầng *đánh giá*. Objective đo bằng hành vi người dùng thật, và đây là tiêu chí nghiệm thu chính của cả module. Kiểm bằng hai vòng thử; đạt khi có đủ bốn số đo ở cả hai vòng và ít nhất ba số cải thiện.

**Lab.** Chuẩn bị ba tác vụ nghiệp vụ. Chạy vòng một với năm người, ghi đủ bốn số đo và mọi chỗ vấp. Xếp vấn đề theo mức nghiêm trọng, sửa những cái nghiêm trọng nhất. Chạy vòng hai với năm người khác. So bốn số đo và giải thích chỗ không cải thiện.

**Pitfalls.** Hỏi cảm nhận thay vì giao tác vụ · hướng dẫn trong lúc thử · bỏ số đo kết quả sai mà tự tin · chỉ chạy một vòng nên không biết sửa có tác dụng không.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn số đo đủ ở cả hai vòng, ≥ 3 số cải thiện, và chỗ không cải thiện có giải thích.

### Lesson 196 · Serving, access and security for consumers `TH`
**Prerequisites.** Lesson 195

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Đưa sản phẩm tới người dùng an toàn và đủ nhanh. Ba đường phục vụ và người dùng tương ứng: công cụ BI cho người không viết mã, SQL trực tiếp cho người phân tích, và giao diện lập trình cho hệ khác. Chính sách truy cập kế thừa từ tầng ngữ nghĩa ở lesson 180, nhưng phải kiểm lại ở từng đường vì cấu hình có thể lệch. Ba yêu cầu phi chức năng phải đo: thời gian phản hồi ở phân vị 95, số người dùng đồng thời chịu được, và hành vi khi quá tải, theo lesson 179 và 87. Phân loại dữ liệu và che dữ liệu nhạy cảm cho môi trường không phải sản xuất. Ba lỗi hay gặp khi mở quyền: cấp theo cá nhân thay vì theo vai nên không quản được, cấp quyền tạm rồi quên thu hồi, và sao chép dữ liệu ra ngoài phạm vi kiểm soát. Nhật ký truy cập là đầu vào cho đo mức dùng ở lesson 197.

**Outcome.** Mở ba đường phục vụ với chính sách nhất quán và đạt ba yêu cầu phi chức năng.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu gồm cả bảo mật lẫn hiệu năng. Kiểm bằng phép thử phủ định ở cả ba đường cộng phép thử tải; đạt khi chính sách nhất quán ở ba đường và ba yêu cầu phi chức năng đạt.

**Lab.** Mở ba đường phục vụ. Chạy cùng bộ phép thử phủ định ở cả ba và chứng minh kết quả giống nhau. Chạy tải tới ngưỡng người dùng đồng thời mục tiêu và đo ba yêu cầu phi chức năng. Dựng quy trình che dữ liệu cho môi trường thử và kiểm không còn trường định danh.

**Pitfalls.** Cấu hình quyền khác nhau ở ba đường · cấp quyền theo cá nhân · chép dữ liệu sản xuất sang môi trường thử chưa che · không đo hành vi khi quá tải.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phép thử phủ định cho kết quả giống nhau ở cả ba đường, ba yêu cầu phi chức năng đạt, và dữ liệu môi trường thử đã che.

### Lesson 197 · Adoption metrics that are not vanity `TH`
**Prerequisites.** Lesson 196

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Đo mức dùng sai cách dẫn tới tối ưu sai thứ, nên bài này tách chỉ số hợp lệ khỏi chỉ số phù phiếm. Ba chỉ số phù phiếm và lý do vô nghĩa: số bảng đã dựng đo khối lượng chứ giá trị; số dashboard đã tạo thường tương quan nghịch với chất lượng; số người có quyền truy cập không nói gì về việc họ có dùng không. Bốn chỉ số hợp lệ: số người dùng hoạt động theo tần suất tự nhiên của quyết định, tỉ lệ câu hỏi được trả lời mà không cần đội dữ liệu can thiệp, số quyết định có dẫn chứng từ sản phẩm, và tỉ lệ người dùng quay lại sau lần đầu. Chỉ số thứ hai là chỉ số trung tâm vì nó đo đúng định nghĩa tự phục vụ ở lesson 194. Đo niềm tin: tỉ lệ người dùng tự kiểm chứng lại số bằng nguồn khác là chỉ số nghịch đảo của niềm tin. Ba cách đo làm hỏng hành vi nếu đội bị chấm theo chúng.

**Outcome.** Chọn bộ chỉ số mức dùng hợp lệ cho một sản phẩm và giải thích vì sao ba chỉ số phù phiếm bị loại.

**Đánh giá.** Tầng *đánh giá*. Objective đòi phán đoán về chất lượng của chính phép đo, chứ chỉ đo. Kiểm bằng bài chọn cộng dựng đo; đạt khi loại đúng ba chỉ số phù phiếm và bốn chỉ số hợp lệ đều đo được từ dữ liệu có sẵn.

**Lab.** Từ nhật ký truy cập, dựng bốn chỉ số hợp lệ cho sản phẩm. Tính cả ba chỉ số phù phiếm và chỉ ra cụ thể chúng dẫn tới kết luận sai thế nào trên dữ liệu thật của mình. Đo tỉ lệ người dùng tự kiểm chứng lại số. Viết một câu cho mỗi chỉ số nêu hành vi xấu nào sẽ xuất hiện nếu đội bị chấm theo nó.

**Pitfalls.** Báo cáo số dashboard như thành tích · đo người dùng hoạt động theo tần suất không khớp nhịp quyết định · bỏ chỉ số niềm tin · chọn chỉ số dễ đo thay vì chỉ số đúng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn chỉ số hợp lệ đo được từ dữ liệu thật, ba chỉ số phù phiếm được chỉ ra dẫn tới kết luận sai thế nào, và mỗi chỉ số có cảnh báo hành vi xấu.

### Lesson 198 · Cost to serve `TH`
**Prerequisites.** Lesson 197

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Một sản phẩm dữ liệu có chi phí và không đo thì không biết nó có đáng giữ không. Bốn thành phần chi phí: tính toán để dựng, lưu trữ, tính toán để phục vụ truy vấn, và thời gian người để vận hành cùng hỗ trợ. Thành phần thứ tư thường lớn nhất và hầu như không bao giờ được tính. Chi phí trên mỗi đơn vị giá trị: chia chi phí cho số quyết định được phục vụ hoặc số người dùng hoạt động, và con số đó là thứ so sánh được giữa các sản phẩm. Ba sản phẩm nên cân nhắc khai tử: chi phí cao mà ít người dùng, trùng lặp với sản phẩm khác, và không truy được về quyết định nào theo lesson 187. Quyết định khai tử là quyết định có bên liên quan nên cần quy trình ở lesson 200. Cảnh báo về tối ưu chi phí quá đà: cắt độ tươi để giảm chi phí làm sản phẩm mất giá trị cho quyết định cần dữ liệu mới.

**Outcome.** Tính chi phí bốn thành phần cho ba sản phẩm và đề xuất khai tử có căn cứ cho ít nhất một cái.

**Đánh giá.** Tầng *đánh giá*. Objective đòi nối chi phí với giá trị, chứ chỉ cắt chi phí. Kiểm bằng bảng chi phí ba sản phẩm; đạt khi cả bốn thành phần có số hoặc ước lượng có căn cứ và đề xuất khai tử dẫn được từ bảng.

**Lab.** Tính bốn thành phần chi phí cho ba sản phẩm, gồm cả ước lượng thời gian người từ nhật ký hỗ trợ. Tính chi phí trên mỗi đơn vị giá trị. Xếp hạng. Đề xuất khai tử một sản phẩm kèm lập luận và kèm phương án cho người đang dùng nó.

**Pitfalls.** Bỏ qua thời gian người · so tổng chi phí giữa các sản phẩm khác quy mô · cắt độ tươi để giảm chi phí mà không hỏi quyết định · đề xuất khai tử mà không có phương án cho người dùng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn thành phần có số hoặc ước lượng có căn cứ cho cả ba sản phẩm, và đề xuất khai tử dẫn được từ bảng kèm phương án thay thế.

### Lesson 199 · Reverse ETL and the shadow operational system `LT`
**Prerequisites.** Lesson 198

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Đẩy dữ liệu từ kho phân tích ngược về hệ vận hành là nhu cầu có thật, và cũng là chỗ dễ tạo ra một hệ vận hành ngầm nguy hiểm. Bốn ràng buộc phải tôn trọng khi làm: ranh giới trách nhiệm tức kho phân tích không được trở thành nguồn sự thật cho nghiệp vụ; tính bất biến khi đẩy lại theo lesson 105; quyền riêng tư vì dữ liệu tổng hợp đẩy ngược có thể chứa thông tin không được phép dùng cho mục đích vận hành; và vòng phản hồi tức dữ liệu đẩy về hệ vận hành rồi lại được nạp lên kho tạo vòng lặp làm hỏng phân tích. Vấn đề thứ tư tinh vi nhất và khó phát hiện nhất. Ba dấu hiệu một hệ vận hành ngầm đang hình thành: nghiệp vụ phụ thuộc kho phân tích để chạy quy trình hằng ngày, kho phân tích có cam kết mức dịch vụ của hệ vận hành mà không có năng lực vận hành tương ứng, và không ai biết dữ liệu gốc nằm ở đâu.

**Outcome.** Nhận ra một hệ vận hành ngầm đang hình thành và nêu bốn ràng buộc phải tôn trọng khi đẩy ngược.

**Đánh giá.** Tầng *phân tích*. Objective là nhận ra một rủi ro kiến trúc trước khi nó cố định. Kiểm bằng ba kiến trúc; đạt khi nhận ra đúng ít nhất hai trường hợp có rủi ro và chỉ ra ràng buộc bị vi phạm.

**Lab.** Cho ba kiến trúc có đẩy dữ liệu ngược. Với mỗi cái, kiểm bốn ràng buộc và chỉ ra cái nào bị vi phạm. Với kiến trúc có vòng phản hồi, vẽ đường đi của dữ liệu và chỉ ra chỗ vòng lặp hình thành. Đề xuất cách chặn cho từng vi phạm.

**Pitfalls.** Coi đẩy ngược là một pipeline bình thường · để kho phân tích thành nguồn sự thật cho nghiệp vụ · không chặn vòng phản hồi · hứa cam kết mức dịch vụ của hệ vận hành trên hạ tầng phân tích.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Nhận đúng ≥ 2/3 trường hợp có rủi ro kèm ràng buộc bị vi phạm, và vẽ đúng chỗ vòng phản hồi hình thành.

### Lesson 200 · Lifecycle and the operating model `TH`
**Prerequisites.** Lesson 199

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài chốt phần quản trị của module. Vòng đời sản phẩm dữ liệu sáu giai đoạn: đề xuất, dựng, chứng nhận, vận hành, khai tử, và gỡ. Điều kiện chuyển giai đoạn lấy từ các bài trước: được chứng nhận khi có đủ tám thuộc tính ở lesson 188, hợp đồng ở lesson 190, tài liệu bốn tầng ở lesson 191, và qua phép thử khả dụng ở lesson 195. Mô hình vận hành: ai trực khi sản phẩm hỏng, cam kết thời gian phản hồi theo mức nghiêm trọng, và kênh nhận phản hồi từ người dùng. Vòng phản hồi vận hành là thứ phân biệt sản phẩm sống với sản phẩm bị bỏ: thu thập câu hỏi người dùng hỏi, phân loại, và dùng chúng làm đầu vào cho việc sửa tài liệu và sửa thiết kế. **Câu hỏi lặp lại nhiều lần là lỗi thiết kế chứ nhu cầu đào tạo**, và đó là cách đọc đúng dữ liệu hỗ trợ.

**Outcome.** Vận hành vòng đời sáu giai đoạn với cửa chứng nhận và vòng phản hồi đọc được từ dữ liệu hỗ trợ.

**Đánh giá.** Tầng *áp dụng*. Objective là một quy trình có cửa chặn và một vòng cải tiến đo được. Kiểm bằng ba sản phẩm đi qua vòng đời; đạt khi sản phẩm thiếu điều kiện bị chặn chứng nhận và câu hỏi lặp lại được chuyển thành thay đổi thiết kế.

**Lab.** Dựng vòng đời sáu giai đoạn với danh mục chứng nhận. Đưa ba sản phẩm qua, trong đó một cái thiếu phép thử khả dụng và phải bị chặn. Thu thập câu hỏi người dùng trong hai tuần, phân loại, và chỉ ra ba câu hỏi lặp lại; chuyển chúng thành thay đổi thiết kế chứ tài liệu đào tạo.

**Pitfalls.** Chứng nhận sản phẩm chưa qua phép thử khả dụng · trả lời câu hỏi lặp lại bằng cách mở lớp hướng dẫn · không có kênh phản hồi · gỡ sản phẩm khi còn người dùng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Sản phẩm thiếu điều kiện bị chặn chứng nhận, và ba câu hỏi lặp lại được chuyển thành thay đổi thiết kế cụ thể.

### Lesson 201 · Capstone - a governed customer health data product `DA`
**Prerequisites.** Lesson 200

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Bài dự án khép module, lấy đúng yêu cầu capstone của hợp đồng nguồn. Dựng một sản phẩm dữ liệu về sức khoẻ khách hàng. Sản phẩm nộp gồm tám hạng mục: phát biểu quyết định bốn phần và cây chỉ số có chủ ở mọi lá; ma trận truy ngược năm mắt; hợp đồng năm phần; giao diện có tập cột công khai tối thiểu; bộ tài liệu bốn tầng có hạn chế diễn giải; chính sách truy cập ba đường có phép thử phủ định; kết quả hai vòng thử khả dụng với bốn số đo; và bảng chi phí bốn thành phần cùng kế hoạch khai tử. Bốn điều kiện tự động không đạt lấy từ phần *Critical failures* của nguồn: có chỉ số không truy được về quyết định, chưa chạy phép thử khả dụng, thiếu hạn chế diễn giải, hoặc dùng chỉ số phù phiếm làm bằng chứng mức dùng.

**Outcome.** Nộp sản phẩm đủ tám hạng mục, không vi phạm bốn điều kiện tự động không đạt.

**Đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module thành một sản phẩm có người dùng thật. Kiểm bằng rà soát tám hạng mục cộng kết quả thử khả dụng; đạt khi hai vòng thử có bốn số đo và vòng hai cải thiện ở ít nhất ba số.

**Lab.** Dựng sản phẩm theo tám hạng mục. Chạy hai vòng thử khả dụng với người dùng thật. Trình bày 15 phút và trả lời chất vấn: chỉ số này phục vụ quyết định nào, ai sở hữu lá nào trong cây, và bằng chứng nào cho thấy người khác dùng được.

**Pitfalls.** Dựng sản phẩm rồi mới tìm quyết định cho nó · dùng số người có quyền truy cập làm bằng chứng · bỏ phép thử khả dụng vì tốn thời gian · viết hạn chế diễn giải chung chung.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Tám hạng mục đầy đủ, hai vòng thử khả dụng có bốn số đo với vòng hai cải thiện ≥ 3 số, và không vi phạm bốn điều kiện tự động không đạt.

### Lesson 202 · Gate 5 - defend a metric definition and prove self-service `KT`
**Prerequisites.** Lesson 201

**In-class (120 phút).** 75 phút làm bài độc lập · 45 phút chữa bài và phân tích lỗi theo nhóm

**Learn.** Cổng của Phase 5, và là cổng đầu tiên kiểm phần năng lực Analytics Engineer. Bài kiểm ba module: mô hình hoá ở M11, ngữ nghĩa và chỉ số ở M11B, và sản phẩm cùng tự phục vụ ở M11C. Không có nội dung mới.

**Outcome.** Bảo vệ một định nghĩa chỉ số trước chất vấn, chứng minh nó không đếm trùng, và trình ra bằng chứng người khác dùng được sản phẩm.

**Đánh giá.** Tầng *đánh giá*. Cổng đo năng lực thiết kế và bảo vệ dưới chất vấn, nên hình thức là bảo vệ trực tiếp có đối soát tại chỗ.

**Lab.** Buổi 120 phút: 75 phút làm bài độc lập, 45 phút chữa bài. Bài chấm sáu phần: A (20đ) phát biểu hạt cho mọi bảng và chứng minh bằng phép đếm · B (25đ) hợp đồng sáu phần cho ba chỉ số, và đối soát với truy vấn do hội đồng viết từ hợp đồng, khớp ở ba mức gộp · C (20đ) chứng minh không đếm trùng bằng bốn bước, gồm một chỉ số có bẫy vực cài sẵn · D (15đ) ma trận tương thích chỉ số nhân chiều, cưỡng chế được bằng máy · E (15đ) bằng chứng thử khả dụng theo tác vụ với bốn số đo · F (5đ) truy ngược một chỉ số bất kỳ về quyết định nghiệp vụ.

**Pitfalls.** Dùng số dashboard làm bằng chứng tự phục vụ · đối soát bằng truy vấn do chính mình viết · bỏ phần truy ngược vì hết giờ · khai báo chỉ số theo cột có sẵn.

**Self-study (2,4 giờ).** Không có bài tự học. Nếu không đạt, theo phụ lục khắc phục khi không đạt cổng

**Done when.** Đạt ≥ 70/100, phần B và C đều ≥ 60%. Chỉ số nào không khớp đối soát của hội đồng thì phần B của chỉ số đó bằng không; bằng chứng tự phục vụ bằng chỉ số phù phiếm thì phần E bằng không.

# MODULE M12 · OLAP INTERNALS AND ANALYTICAL ENGINES

**Phase 6 · Lessons 203–216 · 28 giờ**

| | |
|---|---|
| **Objective cấp module** | Giải thích vì sao hệ cột, xử lý theo lô véctơ và kiến trúc phân tán nhanh, rồi chọn engine theo khối lượng công việc, vận hành và chi phí |
| **Tiền đề** | M4 · M9 · M10 · M11 |
| **Exit criterion** | Đọc được kế hoạch có quét, cắt tỉa, trao đổi dữ liệu, kết và tràn đĩa; truy được ba tầng song song lồng nhau gồm tác vụ MIMD, toán tử xử lý theo lô và làn véctơ; mọi khuyến nghị engine gắn với bằng chứng đo được chứ danh sách tính năng |
| **Kỹ năng SFIA** | `DBAD` mức 4 · `SYSP` mức 4 |
| **Chế độ hỏng** | Chọn engine bằng danh sách tính năng của nhà cung cấp, và so tốc độ giữa một lần chạy có đệm nóng với một lần chạy đệm lạnh |

Module này trả lời câu hỏi vì sao một truy vấn quét mười tỉ dòng xong trong vài giây, và nó trả lời bằng bốn cơ chế độc lập chứ bằng một lời giải thích chung.

Bốn cơ chế: bố cục theo cột giảm lượng byte phải đọc, mã hoá và nén giảm tiếp, thống kê theo khối cho phép bỏ qua phần lớn dữ liệu mà không đọc, và xử lý theo lô véctơ giảm chi phí trên mỗi dòng. **Tách riêng bốn phần đóng góp là yêu cầu bắt buộc của module**, vì gộp chúng lại thì không tối ưu được cái nào.

Mô hình chi phí bộ nhớ ở lesson 45 và bố cục theo hàng hay theo cột ở lesson 47 nay được áp vào quy mô kho dữ liệu.

### Lesson 203 · OLTP against OLAP - the workload is the difference `LT`
**Prerequisites.** Module 12: M11

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Hai hệ khác nhau ở khối lượng công việc chứ ở công nghệ, và hiểu đúng khác biệt đó giải thích mọi quyết định thiết kế còn lại. Năm chiều so sánh: một truy vấn chạm bao nhiêu dòng, bao nhiêu cột, tỉ lệ đọc trên ghi, yêu cầu độ trễ, và số người dùng đồng thời. Hệ giao dịch đọc ít dòng nhiều cột với độ trễ mili giây và đồng thời cao; hệ phân tích quét rất nhiều dòng ít cột với độ trễ giây và đồng thời thấp hơn nhiều. Từ năm chiều đó suy ra vì sao hệ phân tích chọn bố cục cột, chọn nén mạnh, và chấp nhận cập nhật từng dòng đắt. Hệ lai và giới hạn thật của nó. Ba dấu hiệu một khối lượng công việc bị đặt nhầm hệ, và chi phí của việc chạy báo cáo phân tích thẳng trên cơ sở dữ liệu giao dịch, vấn đề đã gặp ở M10.

**Outcome.** Phân loại khối lượng công việc theo năm chiều và suy ra hệ phù hợp kèm lý do cơ chế.

**Đánh giá.** Tầng *hiểu*. Bài mở module, đặt khung giải thích cho mười bài sau. Kiểm bằng bài phân loại sáu khối lượng công việc; đạt khi phân đúng ít nhất năm và lý do dẫn được về năm chiều chứ về tên sản phẩm.

**Lab.** Cho sáu mô tả khối lượng công việc, trong đó hai cái nằm ở ranh giới. Chấm từng cái theo năm chiều và suy ra hệ phù hợp. Với hai ca ranh giới, nêu hai điều kiện đẩy nó về mỗi phía. Đo một truy vấn phân tích chạy trên cơ sở dữ liệu giao dịch và trên hệ cột, ghi lại chênh lệch.

**Pitfalls.** Phân loại theo tên sản phẩm thay vì theo khối lượng công việc · giả định hệ phân tích luôn nhanh hơn · bỏ qua chiều đồng thời · chạy báo cáo nặng trên bản sao đọc rồi tưởng đã tách tải.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân đúng ≥ 5/6 khối lượng công việc, lý do dẫn về năm chiều, và có số đo chênh lệch giữa hai hệ.

### Lesson 204 · Row and column layout `TH`
**Prerequisites.** Lesson 203

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài đưa bố cục dữ liệu ở lesson 47 lên quy mô tệp và đo từng phần đóng góp. Bố cục theo hàng đặt mọi cột của một dòng cạnh nhau, nên đọc một dòng đủ cột thì rẻ; bố cục theo cột đặt mọi giá trị của một cột cạnh nhau, nên đọc ba cột trong bảng trăm cột chỉ chạm phần dữ liệu của ba cột đó. Tỉ lệ byte đọc **không bằng đúng tỉ lệ số cột**, vì mỗi cột có kích thước khác nhau, có mã hoá khác nhau, và tệp còn phần siêu dữ liệu đọc trong mọi trường hợp; lab bài này đo tỉ lệ thật rồi giải thích vì sao nó lệch khỏi tỉ lệ số cột. **Đây là phần đóng góp thứ nhất và phải đo riêng**, trước khi bật nén hay cắt tỉa. Hệ quả kéo theo: cập nhật một dòng trong hệ cột phải chạm mọi tệp cột, nên đắt hơn nhiều lần; đó là lý do hệ phân tích ưa thêm mới rồi hợp nhất hơn sửa tại chỗ, nối với cây hợp nhất có cấu trúc nhật ký ở lesson 135. Lợi ích phụ của bố cục cột và là lý do nén hiệu quả hơn: giá trị cùng cột cùng kiểu và thường giống nhau. Chọn cột dư thừa làm mất lợi ích và đây là lỗi hay gặp nhất.

**Outcome.** Đo riêng phần đóng góp của bố cục cột trên cùng dữ liệu, tách khỏi nén và cắt tỉa.

**Đánh giá.** Tầng *áp dụng*. Objective đòi cô lập một biến, nên thiết kế đo phải tắt các cơ chế còn lại. Kiểm bằng phép đo có đối chứng; đạt khi lượng byte đọc được giải thích bằng tỉ lệ số cột chọn và sai số dưới mức thoả thuận.

**Lab.** Ghi cùng một bảng trăm cột ở hai bố cục, tắt nén ở cả hai. Chạy bốn truy vấn chọn lần lượt 1, 3, 10 và 100 cột. Đo lượng byte đọc và thời gian. Vẽ quan hệ giữa số cột chọn và lượng byte đọc, kiểm nó tuyến tính ở bố cục cột và phẳng ở bố cục hàng. Đo chi phí cập nhật một dòng ở cả hai.

**Pitfalls.** Bật nén khi đo bố cục nên không tách được phần đóng góp · chọn toàn bộ cột rồi kết luận hệ cột không nhanh hơn · đo thời gian mà không đo byte đọc · so hai bố cục ở hai bộ dữ liệu khác nhau.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Quan hệ số cột chọn với byte đọc tuyến tính ở bố cục cột và phẳng ở bố cục hàng, và có số đo chi phí cập nhật một dòng.

### Lesson 205 · Encoding and compression `TH`
**Prerequisites.** Lesson 204

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phần đóng góp thứ hai, và nó phụ thuộc vào dữ liệu chứ vào thuật toán được chọn. Bốn cách mã hoá và điều kiện mỗi cách thắng: mã hoá từ điển thắng khi số giá trị phân biệt thấp; mã hoá độ dài chạy thắng khi giá trị lặp liên tiếp, nên **nó phụ thuộc thứ tự sắp xếp** và đây là liên hệ trực tiếp tới lesson 209; đóng gói bit thắng khi miền giá trị hẹp; mã hoá sai phân thắng với dãy tăng dần như dấu thời gian. Nén khối đặt trên mã hoá và đánh đổi giữa tỉ lệ nén với thời gian giải nén, nên nén mạnh nhất thường không phải lựa chọn nhanh nhất vì nút cổ chai chuyển từ đĩa sang bộ xử lý. Bitmap giá trị rỗng và cách nó tách rỗng khỏi giá trị. Lợi ích thứ hai của từ điển: engine tính trực tiếp trên mã từ điển mà không giải nén, nội dung của lesson 207.

**Outcome.** Chọn cách mã hoá theo đặc trưng dữ liệu và chứng minh lựa chọn bằng cặp số kích thước với thời gian giải nén.

**Đánh giá.** Tầng *áp dụng*. Objective là một quyết định có hai ràng buộc đối nghịch. Kiểm bằng ma trận cách mã hoá nhân đặc trưng dữ liệu; đạt khi mỗi ô có cặp số và lựa chọn cho mỗi cột dẫn được từ ma trận.

**Lab.** Tạo bốn cột có bốn đặc trưng khác nhau. Ghi mỗi cột bằng cả bốn cách mã hoá cộng ba mức nén khối. Đo kích thước và thời gian giải nén. Lập ma trận. Sắp lại bảng theo một cột và đo lại độ dài chạy để chứng minh nó phụ thuộc thứ tự. Chọn cấu hình cho từng cột và chứng minh tổng thời gian truy vấn giảm.

**Pitfalls.** Bật nén mạnh nhất cho mọi cột · dùng từ điển cho cột gần như duy nhất · đo kích thước mà không đo thời gian giải nén · quên rằng độ dài chạy phụ thuộc thứ tự sắp xếp.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ma trận có cặp số ở mọi ô, hiệu ứng thứ tự sắp xếp lên độ dài chạy được chứng minh, và cấu hình chọn làm giảm tổng thời gian truy vấn.

### Lesson 206 · Zone maps, statistics and pruning `TH`
**Prerequisites.** Lesson 205

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phần đóng góp thứ ba và thường là phần lớn nhất: không đọc còn rẻ hơn mọi cách đọc nhanh. Mỗi khối dữ liệu mang thống kê gồm giá trị nhỏ nhất, lớn nhất, số dòng và số giá trị rỗng; engine so điều kiện lọc với thống kê để bỏ qua cả khối mà không mở. Hiệu quả phụ thuộc hoàn toàn vào tương quan giữa cột lọc với thứ tự lưu: nếu dữ liệu sắp theo dấu thời gian thì lọc theo dấu thời gian cắt được gần hết, còn lọc theo một cột rải đều thì mỗi khối đều chứa cả miền giá trị nên không cắt được gì. **Cắt tỉa không xảy ra là chế độ hỏng im lặng phổ biến nhất**, và ba nguyên nhân là bọc cột trong hàm, lệch kiểu dữ liệu, và điều kiện không so trực tiếp; đây chính là tính bám chỉ mục ở lesson 131 dưới một dạng khác. Rủi ro cắt nhầm khi thống kê sai hoặc quy tắc so sánh chuỗi khác nhau giữa bên ghi và bên đọc.

**Outcome.** Đo tỉ lệ khối bị cắt tỉa cho từng truy vấn và sửa được ba trường hợp cắt tỉa không xảy ra.

**Đánh giá.** Tầng *phân tích*. Objective đòi nhận ra một cơ chế không hoạt động mà truy vấn vẫn trả đúng kết quả. Kiểm bằng số khối đọc trong kế hoạch; đạt khi ba trường hợp hỏng được sửa và tỉ lệ cắt tỉa tăng có số đo ở cả ba.

**Lab.** Ghi bảng có thống kê theo khối. Chạy sáu truy vấn và đọc số khối bị cắt từ kế hoạch. Ba truy vấn cố ý làm cắt tỉa thất bại theo ba nguyên nhân; sửa từng cái và đo lại. Ghi cùng dữ liệu theo hai thứ tự sắp xếp khác nhau và so tỉ lệ cắt tỉa cho cùng bộ truy vấn.

**Pitfalls.** Tin cắt tỉa đang xảy ra vì truy vấn nhanh · bọc cột lọc trong hàm · so cột kiểu chuỗi với giá trị kiểu số · đánh giá cắt tỉa mà không đọc số khối trong kế hoạch.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba trường hợp cắt tỉa thất bại được sửa với tỉ lệ cắt tỉa tăng có số đo, và hiệu ứng thứ tự sắp xếp lên cắt tỉa được định lượng.

### Lesson 207 · Vectorized execution and late materialization `LT`
**Prerequisites.** Lesson 206

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Phần đóng góp thứ tư, nằm ở tầng thực thi chứ tầng lưu trữ. Mô hình xử lý từng dòng trả một dòng mỗi lần gọi, nên chi phí gọi hàm và rẽ nhánh đè lên chi phí tính thật. Mô hình theo lô véctơ xử lý một nghìn giá trị mỗi lần gọi, nên chi phí trên mỗi dòng giảm mạnh và vòng lặp chặt tận dụng được dòng đệm cùng lệnh một chỉ thị nhiều dữ liệu theo lesson 46. Véctơ chọn lọc: thay vì sao chép dòng sau khi lọc, engine giữ một mảng chỉ số để tránh chép dữ liệu. Vật chất hoá muộn: chỉ đọc cột cần cho điều kiện lọc trước, lọc xong mới đọc các cột còn lại của những dòng sống sót; với bộ lọc chọn ít dòng thì lượng byte đọc giảm thêm nhiều lần. Thực thi trên mã từ điển: so sánh trên mã nguyên thay vì trên chuỗi, và giải nén đặt càng muộn càng tốt. Sinh mã tại thời điểm chạy ở mức nhận biết.

**Outcome.** Giải thích bốn cơ chế thực thi và suy ra điều kiện mỗi cơ chế mất tác dụng.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết khép phần cơ chế, chuẩn bị cho phần phân tán. Kiểm bằng bài lập luận bốn tình huống; đạt khi chỉ đúng cơ chế mất tác dụng ở ít nhất ba và lý do dẫn về cơ chế chứ về cấu hình.

**Lab.** Cho bốn tình huống: bộ lọc chọn gần hết số dòng, cột có kiểu phức hợp, hàm do người dùng viết chen giữa, và bảng rất hẹp. Với mỗi cái, chỉ ra cơ chế nào mất tác dụng và vì sao. Đo một truy vấn có hàm do người dùng viết so với bản viết bằng biểu thức có sẵn.

**Pitfalls.** Nghĩ xử lý theo lô là một cấu hình bật được · giả định vật chất hoá muộn luôn thắng · chen hàm tự viết vào vòng lặp nóng · bỏ qua chi phí chuyển đổi kiểu giữa các tầng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chỉ đúng cơ chế mất tác dụng ở ≥ 3/4 tình huống, và có số đo cho ảnh hưởng của hàm do người dùng viết.

### Lesson 208 · Vectorized execution is not SIMD `TH`
**Prerequisites.** Lesson 207

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài sửa một nhầm lẫn làm sai mọi lập luận hiệu năng về sau. Thực thi theo lô véctơ là một quyết định ở tầng engine: xử lý một lô giá trị mỗi lần gọi thay vì một dòng, nên chi phí gọi hàm và rẽ nhánh trên mỗi dòng giảm; lợi ích này có ngay cả khi không lệnh véctơ nào của bộ xử lý được dùng. Một lệnh nhiều dữ liệu là một cơ chế của phần cứng theo lesson 48. **Thực thi theo lô tạo điều kiện cho lệnh véctơ chứ đồng nghĩa với nó**, và trong nhiều engine phần lớn mức tăng đến từ việc giảm chi phí trên mỗi dòng chứ từ làn véctơ. Bốn thứ ở tầng engine quyết định làn véctơ có được dùng hiệu quả không: kích thước lô, mặt nạ chọn lọc và mặt nạ giá trị rỗng, phần đuôi, và biểu thức lọc nhiều rẽ nhánh. Ranh giới vật chất hoá và đường thu thập rải rác làm mất lợi ích, đúng như lesson 49.

**Outcome.** Tách phần đóng góp của xử lý theo lô khỏi phần đóng góp của lệnh véctơ trên cùng một phép toán.

**Đánh giá.** Tầng *phân tích*. Objective đòi tách hai cơ chế thường bị gộp thành một lời giải thích. Kiểm bằng ba cấu hình đo song song; đạt khi hai phần đóng góp được tách bằng số và mức tăng thấp ở lô nhỏ được giải thích.

**Lab.** Chạy cùng một phép tổng hợp ở ba cấu hình: xử lý từng dòng, xử lý theo lô nhưng tắt lệnh véctơ, và xử lý theo lô có lệnh véctơ. Đo thời gian cùng số chu kỳ trên mỗi dòng ở từng cấu hình. Lặp lại với bốn kích thước lô và với một biểu thức lọc nhiều rẽ nhánh. Giải thích vì sao lô nhỏ làm mức tăng sụt.

**Pitfalls.** Nói hệ cột nhanh vì dùng lệnh véctơ mà không tách hai cơ chế · đo ở một kích thước lô duy nhất · bỏ qua mặt nạ giá trị rỗng khi giải thích · kết luận từ thời gian tổng mà không có số chu kỳ trên mỗi dòng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Hai phần đóng góp được tách bằng số ở cả bốn kích thước lô, và mức sụt ở lô nhỏ được giải thích bằng cơ chế.

### Lesson 209 · Partitioning, clustering and sort order `TH`
**Prerequisites.** Lesson 208

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba cách bố trí dữ liệu quyết định cắt tỉa ở lesson 206 có hiệu quả hay không, và cả ba đều là quyết định có chi phí. Phân vùng chia dữ liệu theo giá trị một cột thành các nhóm tách biệt; nó cắt tỉa mạnh nhất nhưng **phân vùng theo cột có số giá trị phân biệt cao tạo ra hàng triệu tệp nhỏ**, và khi đó chi phí siêu dữ liệu cùng chi phí mở tệp vượt xa lợi ích, đây là lỗi nghiêm trọng nhất của module. Quy tắc thực dụng: chọn cột phân vùng sao cho mỗi phân vùng đủ lớn, và số phân vùng nằm trong khoảng quản được. Gom cụm và sắp xếp bố trí dữ liệu trong phân vùng, cho cắt tỉa mịn hơn mà không nhân số tệp. Sắp theo nhiều cột và vì sao thứ tự cột quan trọng, giống hệt lập luận về chỉ mục tổ hợp ở lesson 129. Hình phạt tệp nhỏ và cách đo nó tách khỏi chi phí quét.

**Outcome.** Chọn cách bố trí cho ba khối lượng công việc và chứng minh bằng số cả lợi ích cắt tỉa lẫn hình phạt tệp nhỏ.

**Đánh giá.** Tầng *đánh giá*. Objective đòi cân hai hiệu ứng ngược chiều, và chống lại quy tắc phân vùng theo cột hay lọc. Kiểm bằng ba phương án đo song song; đạt khi cả lợi ích lẫn hình phạt đều có số và lựa chọn dẫn được từ hai số đó.

**Lab.** Ghi cùng dữ liệu theo ba phương án: phân vùng theo cột ít giá trị, phân vùng theo cột nhiều giá trị, và phân vùng thô cộng sắp xếp trong phân vùng. Đo số tệp, kích thước tệp trung bình, thời gian liệt kê siêu dữ liệu, và thời gian bộ năm truy vấn. Chỉ ra phương án hai tạo bao nhiêu tệp và chi phí thêm bao nhiêu.

**Pitfalls.** Phân vùng theo cột chỉ vì hay lọc theo nó · không đo số tệp sinh ra · sắp theo nhiều cột mà không cân nhắc thứ tự · bỏ qua thời gian liệt kê siêu dữ liệu khi đo.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba phương án có đủ bốn số đo, hình phạt tệp nhỏ được định lượng, và lựa chọn dẫn được từ cặp lợi ích với chi phí.

### Lesson 210 · MPP - coordinator, fragments and exchange `LT`
**Prerequisites.** Lesson 209

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Từ một máy sang nhiều máy, và bài này giải thích một truy vấn được chia ra sao. Bộ điều phối phân tích câu lệnh, lập kế hoạch, rồi cắt kế hoạch thành các mảnh; mỗi mảnh chạy song song trên nhiều nút; giữa hai mảnh là một bước trao đổi dữ liệu qua mạng. **Bước trao đổi dữ liệu là chỗ tốn nhất**, vì nó là chỗ duy nhất dữ liệu đi qua mạng, nên đọc kế hoạch phân tán là tìm các bước trao đổi trước tiên. Ba cách phân bố dữ liệu giữa các nút và hệ quả: theo băm của một cột cho phép kết cục bộ nếu hai bảng cùng băm theo cột kết, theo khoảng, và ngẫu nhiên. Kết cục bộ là mục tiêu và nó chỉ đạt được khi thiết kế bố cục dữ liệu khớp với cách kết. Vì sao thêm nút không tự động làm nhanh hơn: nếu nút cổ chai là bước trao đổi hoặc là một nút lệch tải thì thêm nút làm tệ hơn.

**Outcome.** Đọc kế hoạch phân tán, chỉ ra các bước trao đổi dữ liệu, và suy ra thêm nút có giúp không.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết chuẩn bị cho bài thực hành về lệch tải. Kiểm bằng bài đọc ba kế hoạch; đạt khi chỉ đúng bước trao đổi ở cả ba và dự đoán đúng hiệu ứng thêm nút ở ít nhất hai.

**Lab.** Cho ba kế hoạch phân tán của cùng một truy vấn ở ba cách bố trí dữ liệu. Với mỗi cái, chỉ ra mảnh, bước trao đổi và lượng dữ liệu qua mạng. Dự đoán hiệu ứng khi gấp đôi số nút, rồi chạy thật và so với dự đoán.

**Pitfalls.** Cho rằng thêm nút luôn làm nhanh hơn · bỏ qua lượng dữ liệu qua mạng khi đọc kế hoạch · nhầm song song trong một nút với phân tán giữa các nút · thiết kế bố cục mà không xem cách kết.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chỉ đúng bước trao đổi ở cả ba kế hoạch, và dự đoán hiệu ứng thêm nút khớp thực tế ở ≥ 2/3.

### Lesson 211 · MPP as distributed MIMD and SPMD - the strong-scaling lab `TH`
**Prerequisites.** Lesson 210

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài đặt kiến trúc phân tán của engine phân tích vào đúng khung phân loại đã học ở lesson 48. Một cụm xử lý là bộ nhớ phân tán nhiều lệnh nhiều dữ liệu: mỗi nút có dòng lệnh, thời điểm và chế độ hỏng độc lập. Kế hoạch vật lý thường theo khuôn mẫu một chương trình nhiều dữ liệu: cùng một mảnh toán tử chạy trên nhiều phân vùng, nhưng mỗi bản chạy độc lập nên chênh lệch thời gian giữa chúng là chuyện bình thường chứ bất thường. Từ đó dựng được **hệ phân cấp ba tầng phải truy được**: tiến trình hoặc tác vụ ở tầng nhiều lệnh nhiều dữ liệu, toán tử xử lý theo lô ở tầng engine, và làn véctơ ở tầng phần cứng; mức tăng quan sát được phải quy được về đúng tầng. Rào đồng bộ và bước trao đổi dữ liệu là điểm mà một nút chậm kéo cả truy vấn theo. Thí nghiệm tăng quy mô cố định khối lượng và tăng số nút, rồi tìm trần.

**Outcome.** Truy được hệ phân cấp ba tầng trên một truy vấn thật và tìm trần khi tăng số nút bằng số đo.

**Đánh giá.** Tầng *phân tích*. Objective đòi quy mức tăng về đúng tầng thay vì gộp. Kiểm bằng thí nghiệm tăng quy mô; đạt khi hiệu suất song song được đo ở ít nhất bốn mức và trần được quy về một trong bốn nguyên nhân bằng bằng chứng.

**Lab.** Chạy cùng một truy vấn với 1, 2, 4 và 8 nút; tính tăng tốc và hiệu suất song song ở mỗi mức. Tách thời gian tính, thời gian trao đổi dữ liệu và thời gian chờ rào đồng bộ. Tìm mức mà thêm nút không còn giúp và quy trần về phần tuần tự, lệch tải, truyền thông hay nút cổ chai bên ngoài. Với một tác vụ, truy tiếp xuống tầng lô và tầng làn theo lesson 208.

**Pitfalls.** Báo cáo tăng tốc mà không báo hiệu suất song song · thêm nút khi trần là nguồn dữ liệu bên ngoài · coi chênh lệch thời gian giữa các tác vụ là lỗi · gộp ba tầng song song thành một lời giải thích.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Hiệu suất song song có số đo ở ≥ 4 mức nút, trần được quy về một nguyên nhân có bằng chứng, và hệ phân cấp ba tầng truy được trên một tác vụ.

### Lesson 212 · Broadcast, repartition, skew and spill `TH`
**Prerequisites.** Lesson 211

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bốn hiện tượng quyết định một truy vấn phân tán chạy được hay không. Kết phát tán gửi bảng nhỏ tới mọi nút rồi kết cục bộ; nhanh khi bảng nhỏ thật, và **tràn bộ nhớ khi engine ước lượng sai kích thước bảng nhỏ**, một hệ quả trực tiếp của sai số ước lượng lực lượng ở lesson 128. Kết phân bố lại băm cả hai bảng theo cột kết rồi kết từng phần; tốn mạng nhưng chịu được bảng lớn. Lệch tải xảy ra khi một giá trị khoá chiếm phần lớn số dòng, nên một nút nhận gần hết việc còn các nút khác chờ; triệu chứng là một tác vụ chạy lâu gấp nhiều lần phần còn lại. Ba cách xử lý lệch tải và đánh đổi của từng cách. Tràn đĩa khi bộ nhớ làm việc không đủ, và nhận ra tràn đĩa trong kế hoạch là kỹ năng chẩn đoán chính; tràn đĩa không phải lỗi mà là cơ chế sống sót, nhưng nó làm chậm nhiều lần.

**Outcome.** Tái hiện cả bốn hiện tượng và chẩn đoán được từng cái từ kế hoạch cùng số đo.

**Đánh giá.** Tầng *phân tích*. Objective đòi nối triệu chứng với nguyên nhân trong hệ phân tán. Kiểm bằng bốn tình huống tái hiện; đạt khi chẩn đoán đúng cả bốn từ bằng chứng và sửa được ít nhất ba với số đo trước sau.

**Lab.** Ép kết phát tán trên một bảng đủ lớn để tràn bộ nhớ. Ép kết phân bố lại và đo lượng dữ liệu qua mạng. Làm lệch một khoá tới mức chiếm phần lớn số dòng và quan sát tác vụ chạy lâu. Giảm bộ nhớ làm việc để gây tràn đĩa. Với mỗi hiện tượng, chỉ ra bằng chứng trong kế hoạch và số đo, rồi sửa.

**Pitfalls.** Ép kết phát tán mà không kiểm kích thước thật · kết luận truy vấn chậm mà không tách lệch tải khỏi tràn đĩa · tăng bộ nhớ để che lệch tải · sửa mà không đo lại.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn hiện tượng được tái hiện và chẩn đoán đúng từ bằng chứng, và ≥ 3 được sửa với số đo trước sau.

### Lesson 213 · Shared-nothing against separated storage and compute `LT`
**Prerequisites.** Lesson 212

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Hai kiến trúc và hệ quả vận hành khác nhau hoàn toàn. Kiến trúc không chia sẻ gắn dữ liệu với nút, nên đọc cục bộ nhanh nhưng thay đổi quy mô đòi phân bố lại dữ liệu, tức một thao tác nặng và có rủi ro. Kiến trúc tách lưu trữ khỏi tính toán đặt dữ liệu trên kho đối tượng và cho cụm tính toán co giãn độc lập; đổi lại mọi lần đọc đi qua mạng nên đệm trở thành thành phần quyết định hiệu năng. Ba hệ quả của việc tách: nhiều cụm tính toán đọc cùng dữ liệu nên cô lập được các khối lượng công việc; dừng cụm khi không dùng nên chi phí theo mức dùng; và đệm lạnh làm lần chạy đầu chậm hơn nhiều lần, điều làm mọi phép so tốc độ thành vô nghĩa nếu không kiểm soát trạng thái đệm. **So sánh đệm nóng với đệm lạnh là lỗi đo lường nghiêm trọng nhất của module.** Siêu dữ liệu và danh mục là thành phần dùng chung, nên nó cũng là điểm nghẽn và điểm hỏng.

**Outcome.** Chỉ ra hệ quả vận hành của mỗi kiến trúc và thiết kế được một phép đo công bằng về trạng thái đệm.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết chuẩn bị cho phần chi phí và phần chọn engine. Kiểm bằng bài thiết kế phép đo; đạt khi phép đo kiểm soát được trạng thái đệm và chênh lệch nóng lạnh được định lượng.

**Lab.** Chạy cùng bộ truy vấn ở đệm lạnh và đệm nóng, đo chênh lệch. Thiết kế một quy trình đo công bằng nêu rõ trạng thái đệm được đặt thế nào trước mỗi lần chạy. Cho hai tình huống thay đổi quy mô và suy ra thao tác cần làm ở mỗi kiến trúc.

**Pitfalls.** So một lần chạy nóng với một lần chạy lạnh · quên rằng siêu dữ liệu là thành phần dùng chung có thể nghẽn · giả định tách lưu trữ và tính toán luôn rẻ hơn · thay đổi quy mô cụm không chia sẻ mà không tính thời gian phân bố lại.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chênh lệch đệm nóng và đệm lạnh được định lượng, và quy trình đo nêu rõ cách đặt trạng thái đệm trước mỗi lần chạy.

### Lesson 214 · Workload management, concurrency and cache `TH`
**Prerequisites.** Lesson 213

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Một truy vấn chạy nhanh khi chạy một mình không nói gì về hành vi khi hai mươi người cùng chạy. Ba cơ chế quản lý: hàng đợi, đơn vị tính toán được cấp, và cô lập giữa các nhóm khối lượng công việc. Khi nhu cầu vượt năng lực thì hệ có hai hành vi khác nhau và phải chọn trước: xếp hàng làm độ trễ tăng, hoặc chia nhỏ tài nguyên làm mọi truy vấn chậm đều. Tách thời gian chờ khỏi thời gian chạy là kỹ năng chẩn đoán chính, vì hai nguyên nhân đó cần hai cách sửa hoàn toàn khác nhau và nhầm chúng dẫn tới mở rộng sai chỗ. Đệm kết quả và đệm dữ liệu là hai thứ khác nhau; đệm kết quả chỉ trúng khi truy vấn giống hệt, nên tỉ lệ trúng cao bất thường thường là dấu hiệu đang đo sai. Tự tạm dừng cụm và đánh đổi giữa chi phí với độ trễ lần chạy đầu. Bốn số phải theo dõi theo lesson 110 và 179.

**Outcome.** Tách được thời gian chờ khỏi thời gian chạy dưới tải và chọn đúng cách sửa cho hai tình huống.

**Đánh giá.** Tầng *phân tích*. Objective đòi phân giải một triệu chứng gộp thành hai nguyên nhân cần hai cách sửa khác nhau. Kiểm bằng hai tình huống; đạt khi tách đúng hai thành phần thời gian ở cả hai và cách sửa chọn đúng.

**Lab.** Chạy tải tăng dần tới khi hàng đợi hình thành. Đo và tách thời gian chờ khỏi thời gian chạy ở từng mức tải. Tạo hai tình huống: một cái nghẽn vì hàng đợi, một cái nghẽn vì truy vấn nặng. Chọn cách sửa cho từng cái và chứng minh cách sửa của tình huống này không giúp gì cho tình huống kia.

**Pitfalls.** Đo thời gian tổng mà không tách chờ · mở rộng cụm để chữa một truy vấn viết kém · để đệm kết quả làm sai phép đo · không cô lập nhóm khối lượng công việc nên báo cáo nặng chặn truy vấn tương tác.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Hai thành phần thời gian tách được ở mọi mức tải, và cách sửa của mỗi tình huống được chứng minh không áp dụng cho tình huống kia.

### Lesson 215 · The cost model of an analytical engine `TH`
**Prerequisites.** Lesson 214

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Chi phí là một ràng buộc thiết kế chứ một con số nhìn cuối tháng. Năm thành phần: lượng byte quét, thời gian tính toán, đơn vị tính toán được cấp nhân thời gian chạy, lưu trữ, và truyền dữ liệu ra ngoài. Các engine tính tiền theo mô hình khác nhau, nên **cùng một khối lượng công việc có thứ hạng chi phí đảo ngược giữa hai engine**, và đó là lý do không so được bằng đơn giá. Cách so đúng: dựng một khối lượng công việc đại diện rồi tính tổng chi phí sở hữu cho từng engine, gồm cả thời gian người vận hành. Ba đòn bẩy giảm chi phí theo thứ tự hiệu quả: giảm byte quét bằng cắt tỉa và chọn cột, giảm thời gian tính bằng viết lại truy vấn, rồi mới tới chỉnh kích thước cụm. Chi phí truyền ra ngoài hay bị quên và là nguồn hoá đơn bất ngờ. Đặt hạn mức và cảnh báo trước khi chạy khối lượng công việc mới.

**Outcome.** Tính chi phí cho một khối lượng công việc trên hai mô hình tính tiền và chỉ ra thứ hạng có thể đảo ngược.

**Đánh giá.** Tầng *áp dụng*. Objective đòi tính chi phí theo mô hình chứ tra bảng giá. Kiểm bằng bài tính hai mô hình; đạt khi tính đúng cả năm thành phần và chỉ ra được điều kiện làm thứ hạng đảo ngược.

**Lab.** Dựng một khối lượng công việc gồm ba loại truy vấn với tần suất khác nhau. Tính năm thành phần chi phí theo hai mô hình tính tiền. Tìm điểm mà thứ hạng đảo ngược khi đổi tần suất hoặc lượng dữ liệu. Áp ba đòn bẩy giảm chi phí theo thứ tự và đo mức giảm của từng đòn bẩy.

**Pitfalls.** So engine bằng đơn giá · bỏ thành phần truyền dữ liệu ra ngoài · bỏ thời gian người vận hành khỏi tổng chi phí · tăng kích thước cụm trước khi sửa truy vấn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Năm thành phần được tính cho cả hai mô hình, điểm đảo ngược thứ hạng được chỉ ra, và ba đòn bẩy có mức giảm riêng.

### Lesson 216 · Engine selection - five archetypes, one ADR `DA`
**Prerequisites.** Lesson 215

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Bài dự án khép module. Năm nguyên mẫu engine và điều kiện thắng của từng cái: kho dữ liệu đám mây được quản lý thắng khi cần quản trị cùng khả năng co giãn với chi phí là mô hình tính tiền và mức phụ thuộc nhà cung cấp; kho theo kiểu hồ dữ liệu thắng khi dùng chung với học máy và dòng dữ liệu với chi phí là độ phức tạp nền tảng; hệ phân tích thời gian thực thắng khi cần tổng hợp độ trễ thấp trên luồng nạp lớn với chi phí là hạn chế về cập nhật, phép kết và vận hành; truy vấn liên kết nhiều nguồn thắng khi cần hỏi xuyên nguồn với chi phí là khả năng đẩy điều kiện xuống nguồn; engine nhúng thắng cho phân tích cục bộ với chi phí là đồng thời và quy mô. Nộp một bản ghi quyết định kiến trúc cho ba khối lượng công việc, mỗi ô dẫn một số đo từ lab của chính mình.

**Outcome.** Nộp bản ghi quyết định chọn engine cho ba khối lượng công việc, mỗi luận điểm gắn một số đo của chính mình.

**Đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module thành một quyết định có bằng chứng. Kiểm bằng rà soát bản ghi quyết định; đạt khi không luận điểm nào chỉ có tính từ và mỗi khối lượng công việc có ngưỡng chi phí kèm hai điều kiện đảo ngược.

**Lab.** Dựng cùng khối lượng công việc trên ít nhất hai engine thuộc hai nguyên mẫu. Đo byte quét, thời gian, hành vi dưới đồng thời, và chi phí, với trạng thái đệm được kiểm soát theo lesson 213. So năm nguyên mẫu trên bốn tiêu chí cho ba khối lượng công việc. Viết bản ghi quyết định kèm ngưỡng chi phí và điều kiện đảo ngược.

**Pitfalls.** Chọn bằng danh sách tính năng của nhà cung cấp · so một lần chạy nóng với một lần chạy lạnh · bỏ chi phí vận hành khỏi so sánh · khuyến nghị không có điều kiện đảo ngược.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Mọi luận điểm gắn một số đo của chính mình, trạng thái đệm được kiểm soát trong mọi phép so, và mỗi khối lượng công việc có ngưỡng chi phí cùng hai điều kiện đảo ngược.

# MODULE M13 · FILE, SERIALIZATION AND OPEN TABLE FORMATS

**Phase 6 · Lessons 217–230 · 28.5 giờ**

| | |
|---|---|
| **Objective cấp module** | Chọn cách biểu diễn dữ liệu và giao thức chốt giao dịch, rồi vận hành tiến hoá lược đồ, tiến hoá phân vùng, gộp tệp và quay lại trạng thái cũ một cách an toàn |
| **Tiền đề** | M4 · M10 · M12 |
| **Exit criterion** | Nói được chính xác đơn vị nào được đọc và đơn vị nào bị cắt tỉa cho từng định dạng; mô tả được giao thức chốt nguyên tử và cách phát hiện xung đột mà không dùng chữ ACID thay cho lời giải thích |
| **Kỹ năng SFIA** | `DBAD` mức 4 · `DATM` mức 4 |
| **Chế độ hỏng** | Xoá tệp dữ liệu bằng tay, chạy dọn tệp mồ côi mà không kiểm thời hạn giữ và tham chiếu, hoặc tuyên bố đạt đúng một lần chỉ vì bảng chốt giao dịch nguyên tử |

Module tách ba khái niệm hay bị gọi lẫn: **định dạng tệp** quy định byte trên đĩa, **định dạng bảng** quy định tệp nào thuộc bảng tại thời điểm nào, và **danh mục** quy định tên bảng trỏ tới siêu dữ liệu nào.

Tách được ba khái niệm này là điều kiện để hiểu vì sao kho đối tượng không có thao tác đổi tên thư mục nguyên tử lại sinh ra cả một lớp phần mềm mới.

Chuẩn tương thích lấy từ M7 và M8 nay áp vào lược đồ dữ liệu, với một khác biệt: bên đọc và bên ghi ở đây thường là hai hệ khác nhau, chạy hai phiên bản thư viện khác nhau, và không ai điều phối được thời điểm chúng nâng cấp.

### Lesson 217 · CSV and JSON - the ambiguity you inherit `TH`
**Prerequisites.** Module 13: M12

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hai định dạng phổ biến nhất và cũng mơ hồ nhất, nên bài này liệt kê chính xác những gì chúng không quy định. Với định dạng phân tách bằng dấu: ký tự phân tách, cách trích dẫn, cách thoát, bảng mã ký tự, cách biểu diễn giá trị rỗng, và kiểu dữ liệu đều không có trong tệp; bên đọc phải đoán, và hai bên đoán khác nhau là nguồn của lỗi âm thầm. Khả năng chia tệp để đọc song song bị phá khi có ký tự xuống dòng nằm trong giá trị được trích dẫn. Với định dạng đối tượng lồng nhau: tự mô tả nên không cần lược đồ ngoài, đổi lại tốn dung lượng và tốn thời gian phân tích; **số lớn mất độ chính xác và dấu thời gian không có ngữ nghĩa múi giờ** là hai chỗ hỏng hay gặp. Dạng mỗi dòng một đối tượng chia tệp được nên dùng được cho đường dẫn dữ liệu lớn. Khi nào hai định dạng này vẫn là lựa chọn đúng: trao đổi với bên ngoài và dữ liệu thô khi nạp.

**Outcome.** Liệt kê những gì hai định dạng không quy định và tái hiện ba lỗi do khác giả định giữa bên ghi và bên đọc.

**Đánh giá.** Tầng *áp dụng*. Bài mở module, kiểm bằng phép thử vòng tròn. Kiểm bằng ba lỗi tái hiện; đạt khi cả ba được tái hiện, chẩn đoán đúng, và chặn bằng một khai báo tường minh.

**Lab.** Ghi cùng dữ liệu ra hai định dạng. Tái hiện ba lỗi: giá trị rỗng bị đọc thành chuỗi rỗng, số lớn mất độ chính xác, và dấu thời gian lệch múi giờ. Với mỗi lỗi, chỉ ra giả định nào khác nhau giữa hai bên và khai báo tường minh chặn nó. Tạo một tệp có xuống dòng trong giá trị trích dẫn và chứng minh không chia được.

**Pitfalls.** Giả định bên đọc hiểu giá trị rỗng giống bên ghi · để số định danh dài đi qua định dạng đối tượng lồng nhau · tin tệp phân tách bằng dấu luôn chia được · suy kiểu dữ liệu từ một mẫu nhỏ đầu tệp.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba lỗi được tái hiện và chặn bằng khai báo tường minh, và tệp không chia được được chứng minh.

### Lesson 218 · Avro and schema resolution `TH`
**Prerequisites.** Lesson 217

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Định dạng theo hàng có lược đồ đi kèm, và cơ chế đáng học nhất của nó là phép phân giải lược đồ. Lược đồ của bên ghi được lưu cùng dữ liệu; bên đọc có lược đồ riêng; thư viện đối chiếu hai lược đồ và quyết định đọc được hay không. Quy tắc đối chiếu theo tên trường, nên **đổi tên một trường là thay đổi phá vỡ dù kiểu dữ liệu không đổi**, và bí danh là cơ chế duy nhất cứu được. Giá trị mặc định cho phép bên đọc mới đọc dữ liệu cũ thiếu trường. Cấu trúc theo khối cho phép chia tệp để đọc song song. Vì sao định dạng theo hàng vẫn dùng ở tầng nạp dù tầng phân tích dùng định dạng cột: bên ghi thêm từng bản ghi, và tiến hoá lược đồ đơn giản hơn. Phân biệt giải mã được về cú pháp với tương thích về ngữ nghĩa: đọc không lỗi không có nghĩa là hiểu đúng.

**Outcome.** Cài phép phân giải lược đồ cho bốn loại thay đổi và phân biệt giải mã được với hiểu đúng.

**Đánh giá.** Tầng *áp dụng*. Objective đòi phân biệt hai mức tương thích mà một mức không có thông báo lỗi. Kiểm bằng bốn thay đổi; đạt khi dự đoán đúng kết quả cả bốn và chỉ ra được ca giải mã sạch nhưng sai nghĩa.

**Lab.** Định nghĩa lược đồ có đủ giá trị rỗng, mặc định, dấu thời gian và số thập phân. Thực hiện bốn thay đổi: thêm trường có mặc định, bỏ trường, đổi tên trường, và đổi kiểu. Với mỗi cái, dự đoán kết quả rồi kiểm. Tạo một thay đổi giải mã sạch nhưng đổi nghĩa và chỉ ra vì sao không có lỗi nào được báo.

**Pitfalls.** Đổi tên trường mà không đặt bí danh · thêm trường bắt buộc không có mặc định · coi giải mã không lỗi là tương thích · kiểm tương thích chỉ theo một chiều.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Dự đoán đúng kết quả cả bốn thay đổi, và ca giải mã sạch nhưng sai nghĩa được chỉ ra kèm giải thích.

### Lesson 219 · Protobuf - field numbers and wire compatibility `TH`
**Prerequisites.** Lesson 218

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Định dạng thứ hai, khác ở chỗ danh tính trường là một con số chứ một cái tên. Trên đường truyền chỉ có số hiệu trường và kiểu mã hoá, nên **đổi tên trường là an toàn còn dùng lại một số hiệu đã bỏ là thảm hoạ**, đúng ngược với định dạng ở bài trước. Quy tắc tương thích suy ra trực tiếp từ đó: thêm trường mới với số hiệu mới thì an toàn; bỏ trường thì phải giữ số hiệu đó ở trạng thái đã đặt chỗ để không ai dùng lại; đổi kiểu chỉ an toàn trong một số cặp kiểu tương thích trên đường truyền. Trường không nhận ra được giữ nguyên hay bị bỏ tuỳ phiên bản thư viện, và điều đó quyết định một bên trung gian có làm mất dữ liệu không. Vì sao định dạng này là lựa chọn cho hợp đồng sự kiện và cho giao thức gọi hàm từ xa ở lesson 101. So sánh với bài trước theo bốn tiêu chí.

**Outcome.** Xây ma trận tương thích cho bốn thay đổi và chứng minh hậu quả của việc dùng lại số hiệu trường.

**Đánh giá.** Tầng *áp dụng*. Objective có một ca hỏng đặc trưng cần tái hiện bằng dữ liệu thật. Kiểm bằng bốn thay đổi cộng ca dùng lại số hiệu; đạt khi dự đoán đúng cả bốn và ca dùng lại số hiệu cho thấy dữ liệu bị diễn giải sai.

**Lab.** Định nghĩa hợp đồng sự kiện. Thực hiện bốn thay đổi gồm đổi tên, thêm trường, bỏ trường có đặt chỗ, và bỏ trường không đặt chỗ rồi dùng lại số hiệu. Mã hoá bằng phiên bản cũ và giải mã bằng phiên bản mới cùng chiều ngược lại. Chỉ ra ca dùng lại số hiệu cho giá trị bị diễn giải sai mà không báo lỗi.

**Pitfalls.** Dùng lại số hiệu trường đã bỏ · giả định đổi tên là thay đổi phá vỡ như ở định dạng trước · bỏ qua hành vi của bên trung gian với trường không nhận ra · chỉ kiểm một chiều tương thích.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Dự đoán đúng cả bốn thay đổi, và ca dùng lại số hiệu cho thấy giá trị bị diễn giải sai mà không có lỗi.

### Lesson 220 · The compatibility matrix - writer old, reader new `TH`
**Prerequisites.** Lesson 219

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài gom hai bài trước thành một quy trình kiểm bắt buộc. Ma trận tương thích có bốn ô: bên ghi cũ với bên đọc cũ, bên ghi cũ với bên đọc mới, bên ghi mới với bên đọc cũ, và bên ghi mới với bên đọc mới. Ba mức tương thích và ý nghĩa vận hành: tương thích ngược cho phép nâng cấp bên đọc trước, tương thích xuôi cho phép nâng cấp bên ghi trước, và tương thích đầy đủ cho phép nâng cấp theo thứ tự bất kỳ. **Mức tương thích quyết định thứ tự triển khai**, nên chọn mức là quyết định vận hành chứ quyết định kỹ thuật thuần tuý. Bản ghi vàng: một tập bản ghi mẫu được giữ cố định, mã hoá bằng mọi phiên bản và giải mã bằng mọi phiên bản, chạy trong tích hợp liên tục theo lesson 96. Sổ đăng ký lược đồ cưỡng chế quy tắc tương thích tại thời điểm đăng ký, nên một thay đổi phá vỡ bị chặn trước khi tới môi trường chạy.

**Outcome.** Dựng ma trận bốn ô chạy tự động trên bản ghi vàng và chặn được một thay đổi phá vỡ trước khi hợp nhất.

**Đánh giá.** Tầng *áp dụng*. Objective là một cửa chặn tự động có tiêu chí nghiệm thu bằng phép thử tiêm. Kiểm bằng ba thay đổi phá vỡ tiêm; đạt khi cả ba bị chặn và mỗi ô của ma trận có kết quả rõ.

**Lab.** Dựng bộ bản ghi vàng cho một hợp đồng. Viết bộ kiểm chạy đủ bốn ô ma trận trên ba phiên bản lược đồ. Đưa vào tích hợp liên tục có cửa chặn. Tiêm ba thay đổi phá vỡ khác loại và xác nhận cả ba bị chặn kèm thông báo chỉ rõ ô nào hỏng. Chọn mức tương thích cho hợp đồng và nêu thứ tự triển khai kéo theo.

**Pitfalls.** Chỉ kiểm ô bên ghi mới với bên đọc mới · không có bản ghi vàng nên mỗi lần kiểm một bộ dữ liệu khác · chọn mức tương thích mà không suy ra thứ tự triển khai · để sổ đăng ký ở chế độ không cưỡng chế.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba thay đổi phá vỡ đều bị chặn kèm thông báo chỉ đúng ô hỏng, và mức tương thích chọn kèm thứ tự triển khai.

### Lesson 221 · Parquet internals - row group, column chunk, page `TH`
**Prerequisites.** Lesson 220

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Định dạng cột chính của hệ sinh thái phân tích, và hiểu cấu trúc của nó là điều kiện để giải thích mọi hành vi hiệu năng ở M12. Bốn mức lồng nhau: tệp chứa nhiều nhóm hàng, mỗi nhóm hàng chứa một khối cột cho mỗi cột, mỗi khối cột chứa nhiều trang, và chân tệp chứa siêu dữ liệu cùng thống kê. **Đơn vị cắt tỉa là nhóm hàng, đơn vị đọc là trang**, và trả lời được hai câu đó cho mỗi định dạng là tiêu chí ra module. Kích thước nhóm hàng là đánh đổi trung tâm: nhóm lớn cho nén tốt và ít siêu dữ liệu nhưng cắt tỉa thô và tốn bộ nhớ khi đọc; nhóm nhỏ cho cắt tỉa mịn nhưng sinh nhiều siêu dữ liệu. Chân tệp nằm ở cuối nên bên đọc phải đọc cuối tệp trước, điều có hệ quả trên kho đối tượng. Mức lặp và mức định nghĩa cho cấu trúc lồng nhau ở mức nhận biết.

**Outcome.** Đọc siêu dữ liệu thật của một tệp và giải thích đơn vị nào được cắt tỉa, đơn vị nào được đọc.

**Đánh giá.** Tầng *phân tích*. Objective đòi nối cấu trúc tệp với số đo hiệu năng. Kiểm bằng ba kích thước nhóm hàng đo song song; đạt khi ba đánh đổi đều có số và lựa chọn dẫn được từ số đó.

**Lab.** Ghi cùng dữ liệu với ba kích thước nhóm hàng. Đọc siêu dữ liệu chân tệp của cả ba và ghi lại số nhóm hàng, kích thước khối cột và thống kê. Chạy bộ truy vấn và đo byte đọc, số nhóm hàng bị cắt, bộ nhớ đỉnh. Chọn kích thước cho khối lượng công việc và dẫn từ ba số đo.

**Pitfalls.** Nhầm đơn vị cắt tỉa với đơn vị đọc · đặt kích thước nhóm hàng theo giá trị mặc định mà không đo · sinh nhóm hàng rất nhỏ rồi ngạc nhiên vì siêu dữ liệu phình · không bao giờ đọc chân tệp thật.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Siêu dữ liệu chân tệp của ba phương án được đọc và ghi lại, và lựa chọn kích thước nhóm hàng dẫn được từ ba số đo.

### Lesson 222 · Encoding choice, statistics and pushdown `TH`
**Prerequisites.** Lesson 221

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài nối cấu trúc tệp ở bài trước với hai cơ chế đã học ở M12, lần này ở phía bên ghi. Chọn cách mã hoá cho từng cột theo số giá trị phân biệt và phân bố, theo đúng ma trận ở lesson 205, nhưng nay quyết định nằm trong tham số ghi tệp. Thống kê tối thiểu lớn nhất và số giá trị rỗng ghi ở mức nhóm hàng và mức trang; chỉ mục trang cho cắt tỉa mịn hơn. Đẩy điều kiện lọc xuống tầng đọc và đẩy danh sách cột xuống tầng đọc là hai cơ chế khác nhau và phải kiểm riêng: một cái giảm số nhóm hàng đọc, cái kia giảm số cột đọc. Ba điều kiện làm đẩy điều kiện xuống thất bại, giống ba nguyên nhân ở lesson 206. Cột có phân bố rải đều làm thống kê vô dụng, nên sắp xếp trước khi ghi là bước quyết định, và đó là cùng một lập luận đã dùng ở lesson 209.

**Outcome.** Cấu hình bên ghi để đạt cả hai cơ chế đẩy xuống và chứng minh bằng số byte đọc tách theo từng cơ chế.

**Đánh giá.** Tầng *áp dụng*. Objective đòi tách hai cơ chế thường bị gộp. Kiểm bằng bốn cấu hình đo song song; đạt khi phần đóng góp của mỗi cơ chế được tách riêng và tổng khớp phép đo đầy đủ.

**Lab.** Ghi bảng với bốn cấu hình: không sắp xếp, sắp theo cột lọc, có chỉ mục trang, và cả hai. Chạy truy vấn chọn ít cột kèm điều kiện lọc hẹp. Với mỗi cấu hình, đo byte đọc khi chỉ bật đẩy cột, khi chỉ bật đẩy điều kiện, và khi bật cả hai. Chứng minh phần đóng góp cộng lại xấp xỉ phép đo đầy đủ.

**Pitfalls.** Gộp hai cơ chế đẩy xuống thành một số đo · sắp xếp theo cột không dùng để lọc · tin thống kê tồn tại là cắt tỉa hoạt động · ghi cột phân bố rải đều rồi mong cắt tỉa.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phần đóng góp của hai cơ chế được tách riêng ở cả bốn cấu hình, và tổng khớp phép đo đầy đủ trong sai số thoả thuận.

### Lesson 223 · Nested schemas, timestamps and decimal interoperability `TH`
**Prerequisites.** Lesson 222

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba chỗ mà hai hệ đọc cùng một tệp lại cho hai kết quả, và cả ba đều không báo lỗi. Cấu trúc lồng nhau: mảng và bản ghi con được biểu diễn bằng mức lặp và mức định nghĩa, và tiến hoá một trường bên trong cấu trúc lồng nhau có quy tắc khác với trường ở mức trên. Dấu thời gian: độ phân giải mili giây hay micro giây, có gắn múi giờ hay không, và hai hệ có thể hiểu cùng một cột theo hai cách; **đây là nguồn lệch số liệu theo ngày phổ biến nhất khi nhiều engine cùng đọc một bảng**. Số thập phân: độ chính xác và phần thập phân được biểu diễn khác nhau giữa các hệ, nên tiền tệ đi qua nhiều hệ có thể bị làm tròn khác nhau. Nguyên tắc chung: với mỗi kiểu dữ liệu nhạy cảm, một phép thử vòng tròn qua mọi engine sẽ đọc bảng, chạy tự động chứ làm một lần rồi tin.

**Outcome.** Chạy phép thử vòng tròn ba kiểu dữ liệu nhạy cảm qua nhiều engine và phát hiện ít nhất một chỗ lệch.

**Đánh giá.** Tầng *phân tích*. Objective đòi phát hiện một lệch không báo lỗi giữa hai hệ. Kiểm bằng phép thử vòng tròn; đạt khi phát hiện ít nhất một chỗ lệch, chẩn đoán đúng nguyên nhân, và chặn bằng một ràng buộc ở bên ghi.

**Lab.** Ghi một bảng có cấu trúc lồng nhau, dấu thời gian ở hai độ phân giải, và cột tiền tệ dạng số thập phân. Đọc bằng ít nhất hai engine và so từng giá trị chứ so tổng. Chỉ ra chỗ lệch, chẩn đoán, và chặn bằng cách cố định biểu diễn ở bên ghi. Đưa phép thử vòng tròn vào chạy tự động.

**Pitfalls.** So bằng tổng nên lệch làm tròn bị che · để độ phân giải dấu thời gian do giá trị mặc định quyết · dùng số dấu chấm động cho tiền tệ · kiểm vòng tròn một lần rồi coi như xong.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ít nhất một chỗ lệch được phát hiện và chẩn đoán đúng, và phép thử vòng tròn chạy tự động.

### Lesson 224 · Object store limits and why a table format exists `LT`
**Prerequisites.** Lesson 223

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài giải thích vì sao có cả một lớp phần mềm nằm giữa tệp và bảng. Kho đối tượng không phải hệ thống tệp: không có thao tác đổi tên thư mục nguyên tử, danh sách đối tượng có thể không phản ánh ngay trạng thái mới, và đối tượng là bất biến nên sửa nghĩa là ghi đối tượng mới. Hệ quả trực tiếp và là lý do tồn tại của định dạng bảng: cách làm cũ dùng một thư mục làm một phân vùng rồi ghi đè bằng đổi tên thư mục không còn nguyên tử, nên bên đọc có thể thấy trạng thái nửa vời. Ba khái niệm phải tách rõ: định dạng tệp quy định byte, định dạng bảng quy định tệp nào thuộc bảng tại thời điểm nào, và danh mục quy định tên bảng trỏ tới siêu dữ liệu nào. **Nói ACID mà không mô tả được cơ chế là dấu hiệu chưa hiểu**, và ranh giới đúng là nguyên tử cùng cô lập ở mức một bảng chứ xuyên bảng.

**Outcome.** Tách ba khái niệm và mô tả chính xác vấn đề mà định dạng bảng giải, không dùng chữ ACID thay lời giải thích.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết bản lề, chuyển từ định dạng tệp sang định dạng bảng. Kiểm bằng bài lập luận; đạt khi tách đúng ba khái niệm và mô tả được ranh giới bảo đảm mà không dùng từ viết tắt thay cơ chế.

**Lab.** Tái hiện vấn đề trên kho đối tượng: ghi một tập tệp mới rồi dừng giữa chừng, và chứng minh bên đọc thấy trạng thái nửa vời khi dùng cách theo thư mục. Phân loại mười thành phần vào ba khái niệm. Viết một đoạn mô tả chính xác bảo đảm mà định dạng bảng cho và không cho.

**Pitfalls.** Coi kho đối tượng như hệ thống tệp · dùng chữ ACID thay cho mô tả cơ chế · nhầm định dạng bảng với engine lưu trữ · giả định bảo đảm có hiệu lực xuyên nhiều bảng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mười thành phần phân đúng ba khái niệm, trạng thái nửa vời được tái hiện, và mô tả bảo đảm không dùng từ viết tắt thay cơ chế.

### Lesson 225 · The metadata tree - snapshot, manifest list, manifest `TH`
**Prerequisites.** Lesson 224

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Cấu trúc siêu dữ liệu của định dạng bảng mở, học bằng cách đọc tệp thật chứ đọc sơ đồ. Bốn tầng: tệp siêu dữ liệu của bảng giữ lược đồ, quy tắc phân vùng và danh sách ảnh chụp; mỗi ảnh chụp trỏ tới một danh sách kê khai; mỗi kê khai liệt kê các tệp dữ liệu kèm thống kê và giá trị phân vùng; tệp dữ liệu là bất biến. Vì sao cấu trúc này cho phép lập kế hoạch nhanh: engine đọc kê khai để loại bỏ tệp mà không chạm tệp dữ liệu, tức cắt tỉa xảy ra ở tầng siêu dữ liệu trước khi tới tầng tệp. Danh mục giữ một con trỏ tới tệp siêu dữ liệu hiện hành, và **con trỏ đó là thứ duy nhất phải đổi nguyên tử**. Đi ngược cây từ một dòng dữ liệu về tới ảnh chụp là bài tập cốt lõi. Siêu dữ liệu phình khi có quá nhiều ảnh chụp hoặc quá nhiều tệp nhỏ.

**Outcome.** Đọc chuỗi siêu dữ liệu thật của một bảng và giải thích một dòng dữ liệu thuộc ảnh chụp nào.

**Đánh giá.** Tầng *phân tích*. Objective đòi đọc cấu trúc thật thay vì mô tả nó. Kiểm bằng bài truy ngược; đạt khi truy đúng đường từ dòng dữ liệu về ảnh chụp và giải thích đúng nơi cắt tỉa siêu dữ liệu xảy ra.

**Lab.** Dựng một bảng và ghi ba lần. Mở tệp siêu dữ liệu, danh sách kê khai và kê khai của từng ảnh chụp, ghi lại nội dung. Chọn một dòng dữ liệu và truy ngược về tệp dữ liệu, kê khai, ảnh chụp. Chạy truy vấn có lọc theo phân vùng và chỉ ra bao nhiêu tệp bị loại ở tầng kê khai trước khi mở tệp nào.

**Pitfalls.** Học cấu trúc qua sơ đồ mà không mở tệp thật · nhầm ảnh chụp với phiên bản lược đồ · bỏ qua vai trò của danh mục · không đo số tệp bị loại ở tầng siêu dữ liệu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Truy đúng đường từ một dòng dữ liệu về ảnh chụp qua đủ bốn tầng, và số tệp bị loại ở tầng kê khai được đo.

### Lesson 226 · The commit protocol and atomic visibility `TH`
**Prerequisites.** Lesson 225

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Giao thức chốt giao dịch gồm năm bước, và hiểu năm bước này là hiểu toàn bộ bảo đảm của định dạng bảng. Bên ghi tạo các tệp dữ liệu bất biến; bên ghi tạo kê khai và tệp siêu dữ liệu mới trỏ tới các tệp đó cùng ảnh chụp cơ sở; danh mục đổi con trỏ bằng một thao tác so sánh rồi đặt, và **đây là bước duy nhất công bố thay đổi**; phát hiện xung đột quyết định thử lại hay báo lỗi; bảo trì ghi lại dữ liệu và siêu dữ liệu, hết hạn ảnh chụp cũ và xoá tệp mồ côi an toàn. Hệ quả quan trọng nhất và là điều phải chứng minh bằng thực nghiệm: nếu bên ghi chết trước bước ba thì các tệp đã ghi tồn tại trên kho đối tượng nhưng **không thuộc bảng**, nên bên đọc không bao giờ thấy chúng. Bên đọc ghim một ảnh chụp cho toàn bộ truy vấn nên nó thấy một trạng thái nhất quán. Du hành thời gian là hệ quả miễn phí của việc giữ các ảnh chụp cũ.

**Outcome.** Chứng minh bằng thực nghiệm rằng tệp chưa chốt không hiện ra với bên đọc, và lập được kế hoạch dọn chúng.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu bằng một thí nghiệm hỏng có chủ ý. Kiểm bằng thí nghiệm dừng giữa chừng; đạt khi bên đọc không thấy dòng nào của lần ghi hỏng và tệp mồ côi được xác định đúng.

**Lab.** Ghi một lô dữ liệu và dừng tiến trình sau bước hai nhưng trước bước ba. Đếm tệp trên kho đối tượng và đếm dòng bảng thấy được; chứng minh hai số không khớp và bảng vẫn đúng. Xác định đúng tập tệp mồ côi bằng cách đối chiếu với kê khai. Chạy du hành thời gian về ảnh chụp trước đó và đối soát.

**Pitfalls.** Xoá tệp lạ trên kho đối tượng bằng tay · cho rằng tệp đã ghi là đã thuộc bảng · dọn tệp mồ côi ngay mà không chờ hết thời hạn giữ · nhầm du hành thời gian với sao lưu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bên đọc không thấy dòng nào của lần ghi hỏng, tập tệp mồ côi được xác định đúng bằng đối chiếu kê khai, và du hành thời gian đối soát khớp.

### Lesson 227 · Optimistic concurrency and conflict detection `TH`
**Prerequisites.** Lesson 226

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Nhiều bên ghi cùng một bảng và cơ chế giải quyết là lạc quan chứ khoá, giống nguyên tắc đã gặp ở lesson 104. Mỗi bên ghi đọc ảnh chụp cơ sở, làm việc, rồi thử đổi con trỏ với điều kiện ảnh chụp cơ sở chưa đổi; nếu đã đổi thì thao tác so sánh rồi đặt thất bại và bên ghi phải quyết định thử lại hay báo lỗi. Ba loại xung đột và cách xử lý khác nhau: hai bên cùng thêm dữ liệu vào phân vùng khác nhau thường thử lại được; hai bên cùng sửa cùng tập tệp thì phải báo lỗi vì thử lại có thể mất thay đổi; và một bên chạy bảo trì trong khi bên kia ghi. **Thử lại vô điều kiện là lỗi nghiêm trọng** vì nó có thể làm mất thay đổi của bên kia. Chi phí khi tranh chấp cao: mọi bên ghi làm việc rồi hỏng ở bước cuối, nên thông lượng sụp; cách giảm là giảm số bên ghi hoặc tách phạm vi ghi.

**Outcome.** Tái hiện ba loại xung đột và chọn đúng hành vi thử lại hay báo lỗi cho từng loại.

**Đánh giá.** Tầng *phân tích*. Objective đòi phân biệt ca thử lại an toàn với ca thử lại làm mất dữ liệu. Kiểm bằng ba xung đột tái hiện; đạt khi cả ba được chẩn đoán đúng và không ca nào thử lại làm mất thay đổi.

**Lab.** Chạy hai bên ghi song song vào cùng bảng ở ba kịch bản. Với mỗi kịch bản, ghi lại thao tác nào thất bại và vì sao. Cài chính sách thử lại phân biệt ba loại. Chứng minh bằng đối soát rằng không thay đổi nào bị mất. Tăng số bên ghi và đo thông lượng sụp ở mức nào.

**Pitfalls.** Thử lại mọi xung đột · không đối soát sau khi thử lại · chạy bảo trì trong giờ ghi cao điểm · tăng bên ghi để tăng thông lượng khi tranh chấp đã cao.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba loại xung đột được chẩn đoán đúng, đối soát chứng minh không mất thay đổi nào, và ngưỡng sụp thông lượng được đo.

### Lesson 228 · Hidden partitioning, partition evolution and schema field IDs `TH`
**Prerequisites.** Lesson 227

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hai tính năng giải hai vấn đề vận hành mà cách làm theo thư mục không giải được. Phân vùng ẩn: người dùng lọc theo cột gốc, còn định dạng bảng tự suy ra giá trị phân vùng từ một phép biến đổi khai báo sẵn; nhờ vậy **không còn lỗi quên thêm điều kiện lọc theo cột phân vùng**, một lỗi tốn kém và im lặng trong cách làm cũ. Tiến hoá phân vùng: đổi quy tắc phân vùng cho dữ liệu mới mà không phải ghi lại dữ liệu cũ, vì mỗi tệp mang theo giá trị phân vùng của nó; đây là lý do siêu dữ liệu phải lưu phép biến đổi chứ chỉ lưu giá trị. Danh tính trường bằng số hiệu chứ bằng tên, cùng nguyên lý với lesson 219: nhờ đó đổi tên cột là thao tác an toàn, còn bên đọc dựa theo tên thì hỏng. Tiến hoá lược đồ gồm thêm, bỏ, đổi tên và mở rộng kiểu, mỗi loại có quy tắc riêng.

**Outcome.** Thực hiện tiến hoá phân vùng và tiến hoá lược đồ trên bảng có dữ liệu cũ, chứng minh truy vấn cũ vẫn đúng.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là dữ liệu cũ và mới cùng đọc đúng sau khi đổi quy tắc. Kiểm bằng đối soát bắc qua ranh giới tiến hoá; đạt khi truy vấn phủ cả hai vùng cho kết quả khớp bản tính tay.

**Lab.** Dựng bảng phân vùng ẩn theo tháng, nạp dữ liệu. Đổi quy tắc phân vùng sang theo ngày và nạp tiếp, không ghi lại dữ liệu cũ. Chạy truy vấn phủ cả hai vùng và đối soát với bản tính tay. Đổi tên một cột và chứng minh truy vấn cũ theo tên mới vẫn đọc đúng dữ liệu cũ. Kiểm cắt tỉa còn hoạt động ở cả hai vùng.

**Pitfalls.** Ghi lại toàn bộ dữ liệu cũ khi đổi quy tắc phân vùng · dùng bên đọc dựa theo tên cột · đổi quy tắc phân vùng mà không kiểm cắt tỉa ở vùng cũ · bỏ đối soát bắc qua ranh giới.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Truy vấn phủ cả hai vùng khớp bản tính tay, đổi tên cột không làm hỏng dữ liệu cũ, và cắt tỉa còn hoạt động ở cả hai vùng.

### Lesson 229 · Maintenance project - deletes, compaction and safe cleanup `DA`
**Prerequisites.** Lesson 228

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Bài dự án khép module, và là phần vận hành mà bỏ qua thì bảng tự hỏng theo thời gian. Hai mô hình xoá: xoá theo vị trí ghi lại dòng nào trong tệp nào bị xoá, xoá theo giá trị ghi điều kiện; mỗi mô hình có chi phí đọc khác nhau, và tệp xoá tích luỹ làm mọi truy vấn chậm dần cho tới khi được hợp nhất. Gộp tệp giải quyết cả tệp nhỏ lẫn tệp xoá tích luỹ, và nó phải chạy được song song với bên ghi theo lesson 227. Ba thao tác bảo trì có thứ tự bắt buộc và điều kiện an toàn: gộp tệp, hết hạn ảnh chụp cũ, rồi dọn tệp mồ côi. **Dọn tệp mồ côi là thao tác nguy hiểm nhất**: nó xoá tệp không được kê khai nào tham chiếu, nên nếu thời hạn giữ ngắn hơn thời gian một lần ghi đang chạy thì nó xoá mất tệp sống. Điều kiện an toàn bắt buộc: thời hạn giữ lớn hơn lần ghi dài nhất, và không bao giờ xoá tệp bằng tay.

**Outcome.** Vận hành đủ ba thao tác bảo trì an toàn trên bảng đang có bên ghi, không mất dòng nào và quay lại được trạng thái cũ.

**Đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module thành một quy trình vận hành có tiêu chí an toàn kiểm được. Kiểm bằng đối soát trước sau cộng phép thử quay lại; đạt khi số dòng khớp tuyệt đối qua mọi thao tác và quay lại được ảnh chụp trước bảo trì.

**Lab.** Tạo hàng nghìn tệp nhỏ và một lượng tệp xoá đáng kể; đo thời gian quét và kích thước siêu dữ liệu. Chạy gộp tệp trong khi một bên ghi vẫn đang thêm dữ liệu; đo lại và đối soát số dòng. Hết hạn ảnh chụp với thời hạn giữ có căn cứ. Chạy dọn tệp mồ côi và chứng minh thời hạn giữ lớn hơn lần ghi dài nhất. Quay lại một ảnh chụp trước đó và đối soát.

**Pitfalls.** Xoá tệp dữ liệu bằng tay · dọn tệp mồ côi với thời hạn giữ mặc định mà không đo lần ghi dài nhất · hết hạn ảnh chụp còn cần cho quay lại · gộp tệp mà không đối soát số dòng.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Số dòng khớp tuyệt đối qua cả ba thao tác, thời hạn giữ được chứng minh lớn hơn lần ghi dài nhất, và quay lại ảnh chụp trước bảo trì thành công.

### Lesson 230 · Gate 6 - explain a metadata chain and survive a concurrent write `KT`
**Prerequisites.** Lesson 229

**In-class (150 phút).** 105 phút làm bài độc lập · 45 phút chữa bài và phân tích lỗi theo nhóm

**Learn.** Cổng của Phase 6. Bài kiểm hai module: cơ chế engine phân tích ở M12 và định dạng tệp cùng định dạng bảng ở M13. Không có nội dung mới.

**Outcome.** Giải thích một chuỗi siêu dữ liệu thật, chứng minh tính hiển thị nguyên tử dưới ghi đồng thời, và chọn engine bằng số đo của chính mình.

**Đánh giá.** Tầng *đánh giá*. Cổng đo năng lực giải thích cơ chế và vận hành an toàn, nên hình thức là thực hành tại chỗ cộng bảo vệ.

**Lab.** Buổi 150 phút: 105 phút làm bài độc lập, 45 phút chữa bài. Bài chấm sáu phần: A (20đ) tách bốn phần đóng góp làm hệ cột nhanh, mỗi phần một số đo riêng · B (15đ) chẩn đoán một truy vấn phân tán chậm, phân biệt lệch tải với tràn đĩa với hàng đợi · C (20đ) đọc chuỗi siêu dữ liệu thật và truy một dòng dữ liệu về ảnh chụp · D (20đ) chạy hai bên ghi đồng thời, chỉ ra thao tác nào thất bại và vì sao, chứng minh không mất thay đổi · E (15đ) ma trận tương thích bốn ô cho một thay đổi lược đồ · F (10đ) khuyến nghị engine cho một khối lượng công việc, mọi luận điểm gắn số đo.

**Pitfalls.** Dùng chữ ACID thay cho mô tả giao thức chốt · so tốc độ giữa lần chạy nóng và lần chạy lạnh · thử lại mọi xung đột ghi · chọn engine bằng danh sách tính năng.

**Self-study (2,4 giờ).** Không có bài tự học. Nếu không đạt, theo phụ lục khắc phục khi không đạt cổng

**Done when.** Đạt ≥ 70/100, phần C và D đều ≥ 60%. Xoá tệp dữ liệu bằng tay trong phần D thì phần đó bằng không; khuyến nghị engine không có số đo thì phần F bằng không.

# MODULE M14B · DATA INGESTION AND INTEGRATION ENGINEERING

**Phase 7 · Lessons 231–246 · 32 giờ**

| | |
|---|---|
| **Objective cấp module** | Đưa dữ liệu từ cơ sở dữ liệu, giao diện lập trình, tệp, dịch vụ ngoài và nguồn sự kiện vào vùng thô với tính đầy đủ, khả năng chạy lại, tiến hoá lược đồ và bảo vệ nguồn |
| **Tiền đề** | M6 · M9 · M10 · M13 |
| **Exit criterion** | Ba loại nguồn chạy được cả khởi tạo, tăng dần, nạp bù và chạy lại; hỏng giữa chừng không mất dữ liệu im lặng; đối soát độc lập từ nguồn tới vùng thô đạt trong phạm vi đã ghi |
| **Kỹ năng SFIA** | `DTAN` mức 4 · `PROG` mức 4 |
| **Chế độ hỏng** | Đồng nhất việc trình kết nối chạy xong với việc đường dẫn dữ liệu đúng, và đẩy mốc tiến độ trước khi dữ liệu được công bố bền vững |

Module này sở hữu đoạn từ hệ nguồn tới vùng thô. Biến đổi dữ liệu thuộc M14, tầng phục vụ thuộc M11B, còn nội bộ dòng sự kiện thuộc M16 và M17.

Nguyên tắc xuyên suốt và cũng là chế độ hỏng nghiêm trọng nhất: **mốc tiến độ chỉ được đẩy sau khi dữ liệu đã nằm bền vững ở đích và đã được công bố nguyên tử**. Đảo thứ tự hai việc đó tạo ra mất dữ liệu im lặng, loại lỗi mà không cảnh báo nào bắt được và chỉ lộ ra khi đối soát.

Nguyên tắc thứ hai: một trình kết nối có sẵn chuyển giao trách nhiệm vận hành nhưng **không chuyển giao trách nhiệm về tính đúng**.

### Lesson 231 · Source discovery and the extraction contract `LT`
**Prerequisites.** Module 14B: M13

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Trước khi viết dòng mã nào, tám nhóm thông tin phải chốt với chủ hệ nguồn, và thiếu nhóm nào thì một chế độ hỏng cụ thể sẽ xuất hiện sau. Ai sở hữu hệ, ai sở hữu giao diện, ai sở hữu dữ liệu về mặt nghiệp vụ, và cửa sổ thời gian được phép trích xuất. Danh sách thực thể cùng khoá, quan hệ, hạt và khối lượng. Ngữ nghĩa thay đổi của từng thực thể. Ngữ nghĩa dấu thời gian gồm múi giờ nguồn, độ phân giải và tính đơn điệu. Lược đồ cùng kiểu, giá trị rỗng và **những giá trị canh chừng không có trong tài liệu** như ngày 1900-01-01 nghĩa là chưa biết. Thông lượng, hạn mức và thời hạn giữ dữ liệu ở nguồn. Phân loại dữ liệu cá nhân, nơi lưu trú và người được phép dùng. Số liệu cơ sở để đối soát về sau. Hợp đồng trích xuất là đầu ra của bài, và nó là tài liệu được hai bên ký chứ ghi chú riêng.

**Outcome.** Nộp hợp đồng trích xuất đủ tám nhóm cho một nguồn thật và chỉ ra rủi ro của từng nhóm còn trống.

**Đánh giá.** Tầng *áp dụng*. Bài mở module, áp một danh mục phỏng vấn vào nguồn thật. Kiểm bằng rà soát tám nhóm; đạt khi ít nhất sáu nhóm có câu trả lời cụ thể và mỗi nhóm trống kèm một chế độ hỏng dự đoán được.

**Lab.** Chọn một nguồn thật có tài liệu. Điền hợp đồng trích xuất tám nhóm, phần nào không có trong tài liệu thì ghi là chưa biết chứ đoán. Dò tìm giá trị canh chừng bằng cách thống kê phân bố từng cột. Với mỗi nhóm còn trống, viết một câu mô tả chế độ hỏng nó gây ra.

**Pitfalls.** Bắt đầu viết trình trích xuất trước khi chốt ngữ nghĩa thay đổi · tin tài liệu nguồn nói đúng về giá trị rỗng · bỏ qua múi giờ của dấu thời gian nguồn · không hỏi cửa sổ thời gian được phép chạy.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** ≥ 6/8 nhóm có câu trả lời cụ thể, giá trị canh chừng được dò bằng thống kê thật, và mọi nhóm trống kèm chế độ hỏng dự đoán.

### Lesson 232 · Change semantics - insert, update, delete and soft delete `TH`
**Prerequisites.** Lesson 231

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Cách nguồn thay đổi quyết định mọi lựa chọn còn lại, nên bài này đặt trước bài chọn mẫu trích xuất. Bốn câu hỏi phải trả lời cho từng thực thể: bản ghi có được sửa sau khi tạo không, có bị xoá cứng không, xoá mềm được đánh dấu bằng gì, và thứ tự thay đổi có quan sát được không. **Xoá cứng là chế độ hỏng nặng nhất của mọi phương pháp tăng dần**, vì một dòng biến mất khỏi nguồn không để lại dấu vết nào cho truy vấn theo dấu thời gian; ba cách phát hiện và chi phí từng cách. Lịch sử có thể thay đổi: khi nguồn sửa cả bản ghi cũ, mọi kỳ đã nạp đều có thể sai, nên cần đối soát định kỳ chứ chỉ nạp tiếp. Giao dịch và thứ tự: hai bản ghi cùng giao dịch phải cùng xuất hiện, nếu không thì đích có trạng thái không nhất quán tạm thời. Ánh xạ bốn câu trả lời sang yêu cầu kỹ thuật.

**Outcome.** Xác định ngữ nghĩa thay đổi của bốn thực thể bằng thực nghiệm và suy ra yêu cầu kỹ thuật kéo theo.

**Đánh giá.** Tầng *phân tích*. Objective đòi kiểm chứng bằng dữ liệu thay vì tin tài liệu. Kiểm bằng phép dò thực nghiệm; đạt khi bốn thực thể có kết luận dựa trên bằng chứng và phát hiện được ít nhất một chỗ tài liệu sai.

**Lab.** Với bốn thực thể, thiết kế phép dò: chụp hai lần cách nhau và so tập khoá để phát hiện xoá cứng; so nội dung để phát hiện sửa bản ghi cũ; kiểm tính đơn điệu của dấu thời gian. Đối chiếu kết quả với tài liệu nguồn và ghi lại mọi chỗ lệch. Với mỗi thực thể, suy ra yêu cầu kỹ thuật cho bước trích xuất.

**Pitfalls.** Tin tài liệu nói không có xoá cứng · bỏ qua khả năng lịch sử bị sửa · coi dấu thời gian luôn tăng · kết luận từ một lần chụp duy nhất.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn thực thể có kết luận dựa trên bằng chứng thực nghiệm, và ít nhất một chỗ tài liệu sai được phát hiện.

### Lesson 233 · Choosing an extraction pattern `TH`
**Prerequisites.** Lesson 232

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Tám mẫu trích xuất, mỗi mẫu có điều kiện thắng và rủi ro chính, và chọn theo ngữ nghĩa thay đổi ở bài trước chứ theo thói quen. Chụp toàn bộ đọc hết trạng thái: đơn giản và phục hồi dễ, nhưng tốn nguồn và không giữ thứ tự thay đổi. Mốc tiến độ theo dấu thời gian: rẻ, đòi một trường thay đổi đơn điệu tin cậy. Tăng dần theo khoá có thứ tự: phân trang được ở quy mô lớn, đòi khoá ổn định và có thứ tự toàn phần. Con trỏ do nhà cung cấp cấp: ổn định cho giao diện lập trình, rủi ro là con trỏ hết hạn tạo lỗ hổng. Thả tệp: hợp cho trao đổi khối lượng lớn, rủi ro là tải lên dở dang và trùng tên. Trích xuất bằng truy vấn giới hạn: kiểm soát được tập con, rủi ro là khoá và tải lên nguồn. Bắt thay đổi từ nhật ký giao dịch, học sâu ở M17. Nguồn tự phát sự kiện: bên sản xuất sở hữu ý định.

**Outcome.** Chọn mẫu trích xuất cho bốn nguồn và nêu rõ giả định phải đúng để mẫu đó cho kết quả đầy đủ.

**Đánh giá.** Tầng *đánh giá*. Objective đòi nêu giả định chứ chỉ chọn. Kiểm bằng bốn nguồn có ngữ nghĩa khác nhau; đạt khi chọn đúng ít nhất ba và mỗi lựa chọn kèm danh sách giả định kiểm được.

**Lab.** Cho bốn nguồn với ngữ nghĩa thay đổi khác nhau, trong đó một nguồn có xoá cứng và một nguồn có dấu thời gian không đơn điệu. Chọn mẫu cho từng cái. Với mỗi lựa chọn, liệt kê giả định phải đúng và thiết kế một phép kiểm cho từng giả định. Chỉ ra nguồn nào không dùng được mẫu theo dấu thời gian và vì sao.

**Pitfalls.** Mặc định dùng mốc theo dấu thời gian cho mọi nguồn · chọn chụp toàn bộ vì đơn giản mà không tính tải lên nguồn · dùng phân trang theo độ lệch trên tập đang thay đổi · chọn mẫu trước khi biết ngữ nghĩa xoá.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chọn đúng ≥ 3/4 nguồn, mỗi lựa chọn kèm danh sách giả định, và mỗi giả định có một phép kiểm cụ thể.

### Lesson 234 · High watermark - the five assumptions it needs `TH`
**Prerequisites.** Lesson 233

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Mẫu phổ biến nhất và cũng bị cài sai nhiều nhất, nên nó có một bài riêng. Điều kiện lọc theo mốc lớn hơn giá trị lớn nhất đã nạp chỉ đầy đủ khi năm giả định cùng đúng: đồng hồ nguồn không lùi; trường mốc được cập nhật ở mọi lần sửa; không có hai bản ghi cùng giá trị mốc nằm hai bên ranh giới; xoá được theo dõi bằng cơ chế khác; và đích rỗng được xử lý đúng. **Vi phạm giả định thứ ba là lỗi âm thầm phổ biến nhất**: dùng dấu lớn hơn thì mất bản ghi trùng giá trị, dùng lớn hơn hoặc bằng thì trùng lặp, nên lời giải đúng là cửa sổ chồng lấn cộng khử trùng có quy tắc chọn thắng xác định. Độ rộng cửa sổ chồng lấn tính từ độ trễ tối đa quan sát được chứ đoán. Cập nhật tới muộn và giao dịch mở lâu làm bản ghi xuất hiện với mốc cũ hơn thời điểm nhìn thấy.

**Outcome.** Cài trích xuất theo mốc tiến độ vượt qua cả năm giả định và chứng minh không mất cũng không trùng.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là đối soát khớp tuyệt đối qua các ca biên. Kiểm bằng năm ca biên tiêm; đạt khi số dòng và tổng khớp nguồn ở cả năm và quy tắc chọn thắng xác định.

**Lab.** Dựng nguồn có đủ năm ca biên: đồng hồ lùi, sửa không cập nhật mốc, nhiều bản ghi trùng giá trị mốc ở ranh giới, xoá cứng, và lần chạy đầu trên đích rỗng. Cài cửa sổ chồng lấn cộng khử trùng. Tính độ rộng cửa sổ từ độ trễ đo được. Đối soát số dòng, tổng và tập khoá với nguồn sau mỗi ca.

**Pitfalls.** Dùng điều kiện lớn hơn giá trị lớn nhất mà không có cửa sổ chồng lấn · đặt độ rộng cửa sổ bằng một con số tròn không có căn cứ · khử trùng không có quy tắc chọn thắng xác định · bỏ qua ca đích rỗng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Số dòng, tổng và tập khoá khớp nguồn ở cả năm ca biên, và độ rộng cửa sổ chồng lấn dẫn được từ độ trễ đo được.

### Lesson 235 · API pagination - offset, keyset and cursor `TH`
**Prerequisites.** Lesson 234

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba cách phân trang cho ba mức bảo đảm khác nhau, và chọn sai gây mất hoặc trùng bản ghi mà không báo lỗi. Phân trang theo độ lệch đơn giản nhưng **hỏng khi tập dữ liệu thay đổi giữa các trang**: thêm một bản ghi ở đầu làm mọi trang sau lệch một, nên vừa trùng vừa sót. Phân trang theo khoá dùng giá trị của bản ghi cuối làm điểm bắt đầu, nên ổn định trước việc thêm bản ghi, với điều kiện khoá sắp thứ tự toàn phần và không đổi. Con trỏ do nhà cung cấp cấp có thể ghim một ảnh chụp hoặc không, và tài liệu thường không nói rõ, nên phải kiểm bằng thực nghiệm. Ba chế độ hỏng bắt buộc xử lý: con trỏ hết hạn giữa chừng, phản hồi mã thành công nhưng thân chứa lỗi nghiệp vụ, và thứ tự trả về không ổn định. Điểm dừng phân trang phải tường minh chứ dựa vào trang rỗng.

**Outcome.** Cài trích xuất phân trang chịu được thay đổi giữa các trang và chứng minh không mất cũng không trùng bản ghi.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là đối soát tập khoá dưới nhiễu. Kiểm bằng phép thử chèn giữa chừng; đạt khi tập khoá thu được khớp tập khoá nguồn tại ranh giới đã chốt, ở cả ba cách phân trang được so.

**Lab.** Dựng một giao diện lập trình mô phỏng có thể chèn và xoá bản ghi giữa các trang. Cài cả ba cách phân trang. Chạy trích xuất trong khi chèn bản ghi ở đầu tập, và so tập khoá thu được với tập khoá đúng. Tái hiện con trỏ hết hạn và phản hồi mã thành công chứa lỗi nghiệp vụ. Chạy lại có điểm kiểm tra sau mỗi trang.

**Pitfalls.** Dùng phân trang theo độ lệch trên tập đang thay đổi · dừng khi gặp trang rỗng mà không kiểm dấu hiệu kết thúc tường minh · coi mã phản hồi thành công là dữ liệu hợp lệ · không kiểm con trỏ có ghim ảnh chụp hay không.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tập khoá khớp tập đúng khi có chèn giữa chừng ở cách phân trang được chọn, và hai chế độ hỏng con trỏ được tái hiện cùng xử lý.

### Lesson 236 · Rate limits, retry budget and source protection `TH`
**Prerequisites.** Lesson 235

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bên trích xuất là khách của hệ nguồn, nên bảo vệ nguồn là một yêu cầu chức năng chứ phép lịch sự. Đọc tín hiệu hạn mức từ tiêu đề phản hồi và tôn trọng chỉ dẫn chờ; ba cách hiểu sai đồng hồ đặt lại hạn mức, gồm cả lệch múi giờ. Phân loại lỗi tạm thời và lỗi vĩnh viễn theo lesson 107, vì thử lại một lỗi vĩnh viễn chỉ làm nguồn tệ hơn. Ngân sách thử lại có giới hạn cùng lùi dần theo cấp số nhân có nhiễu ngẫu nhiên, để tránh cả đoàn khách cùng quay lại một lúc. **Thử lại một yêu cầu ghi có thể nhân đôi tác dụng phụ** khi phản hồi thất lạc, nên cần khoá chống trùng theo lesson 105. Điều chỉnh mức đồng thời theo phản hồi của nguồn thay vì đặt cố định. Nạp bù là mối nguy lớn nhất với nguồn, nên nó phải có hạn mức riêng và cửa sổ riêng, quy tắc được cưỡng chế ở lesson 243.

**Outcome.** Cài lớp gọi có ngân sách thử lại và điều chỉnh đồng thời, chứng minh không vượt hạn mức nguồn dưới tải.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu đo được ở phía nguồn. Kiểm bằng phép thử tải; đạt khi không lần nào vượt hạn mức, số lần thử lại nằm trong ngân sách, và không có tác dụng phụ trùng lặp.

**Lab.** Dựng nguồn mô phỏng có hạn mức, có trả lỗi tạm thời ngẫu nhiên và có đồng hồ đặt lại ở múi giờ khác. Cài lớp gọi có phân loại lỗi, ngân sách thử lại, lùi dần có nhiễu, và điều chỉnh đồng thời. Chạy tải và đo số lần vượt hạn mức. Tái hiện phản hồi thất lạc sau một yêu cầu ghi và chứng minh không nhân đôi.

**Pitfalls.** Thử lại không giới hạn · thử lại lỗi vĩnh viễn · lùi dần không có nhiễu nên các tiến trình đồng loạt quay lại · chạy nạp bù chung hạn mức với lần chạy hằng ngày.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Không lần nào vượt hạn mức nguồn dưới tải, số lần thử lại trong ngân sách, và phản hồi thất lạc không tạo tác dụng phụ trùng.

### Lesson 237 · File drop - the delivery protocol and arrival completeness `TH`
**Prerequisites.** Lesson 236

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Trao đổi bằng tệp trông đơn giản và hỏng theo những cách rất đặc trưng. Giao thức giao nhận đúng có bốn bước: ghi bằng tên tạm, kiểm tổng kiểm tra, ghi tệp kê khai hoặc dấu hiệu hoàn tất, rồi mới đổi sang tên chính thức bất biến; **đọc tệp trước khi thấy dấu hiệu hoàn tất là nguyên nhân số một của dữ liệu cụt**. Danh tính tệp để khử trùng gồm nguồn, đường dẫn, băm nội dung, kích thước và siêu dữ liệu sửa đổi, vì tên tệp có thể bị dùng lại. Tính đầy đủ của lô là một khái niệm khác với sự kiện tệp tới: biết tệp nào đã tới không trả lời được câu đã tới đủ chưa, nên cần danh sách tệp kỳ vọng hoặc tổng kiểm soát trong kê khai. Tệp hỏng, cụt hoặc mã hoá đi vùng cách ly kèm chủ sở hữu, không bị bỏ im lặng. Sự kiện từ kho đối tượng thường là ít nhất một lần và có thể chạy đua với thao tác liệt kê.

**Outcome.** Cài giao thức bốn bước và chứng minh phát hiện được tệp thiếu, tệp trùng và tệp hỏng.

**Đánh giá.** Tầng *áp dụng*. Objective đòi phân biệt tệp đã tới với lô đã đủ. Kiểm bằng bốn ca hỏng tiêm; đạt khi cả bốn bị phát hiện, không ca nào bị bỏ im lặng, và lô thiếu tệp không được công bố.

**Lab.** Cài giao thức bốn bước cho bên gửi và bên nhận. Tiêm bốn ca: tải lên dở dang, tệp trùng tên khác nội dung, tệp hỏng, và lô thiếu một tệp so với kê khai. Chứng minh từng ca bị phát hiện và đi đúng đường xử lý. Chứng minh lô thiếu tệp không được đánh dấu hoàn tất. Đo hiệu ứng của việc gom tệp nhỏ trước khi ghi vùng thô.

**Pitfalls.** Đọc tệp ngay khi sự kiện báo tệp tới · khử trùng bằng tên tệp · coi có đủ sự kiện là có đủ tệp · bỏ tệp hỏng mà không cách ly và không báo chủ sở hữu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn ca hỏng đều bị phát hiện và đi đúng đường xử lý, và lô thiếu tệp không bao giờ được đánh dấu hoàn tất.

### Lesson 238 · Database extraction - snapshot, chunking and replica lag `TH`
**Prerequisites.** Lesson 237

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Trích xuất từ cơ sở dữ liệu giao dịch đụng thẳng vào nội dung M10, nên bài này dùng lại kiến thức đó ở vai người gọi. Ảnh chụp nhất quán: một truy vấn dài giữ một giao dịch mở, và giao dịch mở lâu cản việc thu dọn phiên bản cũ theo lesson 141, nên trích xuất nặng có thể làm phình cơ sở dữ liệu nguồn. Chia lô theo khoá có chỉ mục và ổn định, kích thước lô điều chỉnh theo thời gian phản hồi; chia theo độ lệch làm truy vấn chậm dần. Trích xuất từ bản sao đọc giảm tải cho bản chính nhưng đưa vào độ trễ sao chép, nên ranh giới trích xuất phải tính theo trạng thái bản sao chứ theo đồng hồ; chuyển đổi dự phòng làm điểm cuối đổi giữa chừng. Phát hiện thay đổi cấu trúc ở nguồn trước khi nó làm hỏng lần chạy. Theo dõi tác động lên nguồn bằng số đo của nguồn chứ bằng cảm nhận.

**Outcome.** Trích xuất bảng lớn theo lô mà không vượt ngưỡng tác động lên nguồn và không mất dòng vì độ trễ bản sao.

**Đánh giá.** Tầng *áp dụng*. Objective có hai ràng buộc: đúng dữ liệu và không hại nguồn. Kiểm bằng cặp số đo; đạt khi đối soát khớp nguồn tại ranh giới đã chốt và mọi số đo tác động nằm dưới ngưỡng thoả thuận.

**Lab.** Trích xuất một bảng lớn theo lô chia bằng khoá có chỉ mục, kích thước lô điều chỉnh động. Đo trên nguồn: thời gian truy vấn, số kết nối, độ dài giao dịch mở và mức phình phiên bản. So với một bản chia theo độ lệch. Chuyển sang trích xuất từ bản sao, tạo độ trễ nhân tạo và chứng minh ranh giới tính theo trạng thái bản sao cho kết quả đúng.

**Pitfalls.** Chia lô theo độ lệch · giữ một giao dịch mở suốt lần trích xuất · tính ranh giới theo đồng hồ khi đọc từ bản sao · không đo tác động lên nguồn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đối soát khớp nguồn tại ranh giới đã chốt, và mọi số đo tác động lên nguồn dưới ngưỡng thoả thuận.

### Lesson 239 · The landing zone - fidelity, envelope and required metadata `LT`
**Prerequisites.** Lesson 238

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Vùng thô có một nhiệm vụ: giữ đúng những gì nguồn đã nói, để mọi biến đổi sau này chạy lại được. Trung thực với nguồn nghĩa là lưu tải trọng gốc chưa diễn giải, kèm một phong bì siêu dữ liệu. Sáu trường siêu dữ liệu bắt buộc: định danh nguồn, định danh lần chạy trích xuất, vị trí của bản ghi trong nguồn, thời điểm nạp, phiên bản lược đồ, và tổng kiểm tra. Thiếu trường thứ ba thì không chạy lại từ một điểm được; thiếu trường thứ năm thì không giải thích được vì sao hai lô cùng nguồn có hình dạng khác nhau. **Trung thực với nguồn không có nghĩa lưu mọi dữ liệu nhạy cảm vô thời hạn**: phân loại, mã hoá, thời hạn giữ và đường lan truyền lệnh xoá vẫn áp dụng ở vùng thô, và đây là chỗ hay bị bỏ qua nhất. Vùng cách ly tách khỏi vùng thô đã nhận. Đăng ký danh mục và phát tín hiệu dòng dõi ngay khi công bố chứ suy lại sau nhiều tháng.

**Outcome.** Thiết kế phong bì vùng thô đủ sáu trường và nêu chính sách dữ liệu nhạy cảm đi kèm.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết đặt chuẩn cho hai bài thực hành sau. Kiểm bằng bài thiết kế cộng bài lập luận; đạt khi sáu trường có mặt và mỗi trường kèm một câu hỏi vận hành nó trả lời được.

**Lab.** Thiết kế phong bì cho ba loại nguồn khác nhau. Với mỗi trường siêu dữ liệu, viết một câu hỏi vận hành mà không có trường đó thì không trả lời được. Viết chính sách cho dữ liệu nhạy cảm ở vùng thô gồm phân loại, mã hoá, thời hạn giữ và cách lan truyền lệnh xoá. Chỉ ra ba thứ không nên nằm ở vùng thô.

**Pitfalls.** Diễn giải dữ liệu trước khi hạ cánh · bỏ vị trí bản ghi trong nguồn · trộn dữ liệu bị cách ly vào vùng thô đã nhận · coi trung thực với nguồn là miễn trừ khỏi quy định về dữ liệu cá nhân.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Sáu trường có mặt ở cả ba thiết kế, mỗi trường kèm câu hỏi vận hành nó trả lời, và chính sách dữ liệu nhạy cảm đủ bốn phần.

### Lesson 240 · Atomic landing and the checkpoint ordering rule `TH`
**Prerequisites.** Lesson 239

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài cưỡng chế nguyên tắc trung tâm của module bằng thực nghiệm. Thứ tự bắt buộc gồm bốn bước: ghi dữ liệu ra vị trí tạm, xác nhận đã bền vững, công bố nguyên tử, rồi mới đẩy mốc tiến độ. Đảo hai bước cuối tạo ra mất dữ liệu im lặng: tiến trình chết sau khi đẩy mốc nhưng trước khi công bố, và lần chạy sau bắt đầu từ mốc mới nên khoảng dữ liệu ở giữa không bao giờ được nạp, **không có lỗi nào được ghi lại và chỉ đối soát mới phát hiện ra**. Công bố nguyên tử trên kho đối tượng dùng giao thức chốt ở lesson 226. Trạng thái điểm kiểm tra gồm những gì, ai sở hữu nó, và nó phải bền vững cùng lúc hay sau dữ liệu. Thực thi ít nhất một lần cộng tác dụng phụ luỹ đẳng là mô hình thực tế; tuyên bố đúng một lần mà không nêu ranh giới là tuyên bố rỗng. Chạy lại vào đích cách ly để so trước khi hoán đổi.

**Outcome.** Chứng minh bằng thực nghiệm rằng hỏng ở mọi ranh giới đều không mất dữ liệu và không trùng ngoài giới hạn đã nêu.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu bằng thí nghiệm hỏng tại từng ranh giới. Kiểm bằng phép thử giết tiến trình; đạt khi mọi ranh giới cho kết quả đối soát khớp sau khi chạy lại, và ranh giới đảo thứ tự bị chứng minh là mất dữ liệu.

**Lab.** Cài đường nạp theo đúng bốn bước. Giết tiến trình ở từng ranh giới giữa các bước, chạy lại, và đối soát với nguồn. Cài thêm một bản cố ý đẩy mốc trước khi công bố, giết ở đúng ranh giới đó, và chứng minh dữ liệu mất mà không có lỗi nào. Định lượng số dòng mất.

**Pitfalls.** Đẩy mốc tiến độ trước khi công bố · lưu điểm kiểm tra ở nơi khác với dữ liệu mà không có thứ tự bền vững rõ · tuyên bố đúng một lần mà không nêu ranh giới · chạy lại thẳng vào đích đang phục vụ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mọi ranh giới hỏng đều phục hồi được với đối soát khớp, và bản đảo thứ tự được chứng minh mất dữ liệu kèm số dòng cụ thể.

### Lesson 241 · Schema drift - detect, classify, quarantine `TH`
**Prerequisites.** Lesson 240

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Lược đồ nguồn đổi mà không báo trước là chuyện thường, nên đường nạp phải coi đó là trạng thái bình thường chứ sự cố. Phát hiện bằng cách so lược đồ quan sát được của lô hiện tại với lược đồ đã đăng ký, chứ đợi bước biến đổi báo lỗi. Phân loại ba mức theo đúng ma trận ở lesson 220: thay đổi tương thích thì nạp tiếp và ghi nhận; thay đổi làm đổi nghĩa thì cảnh báo và chặn bước hạ nguồn; thay đổi phá vỡ thì đưa cả lô vào vùng cách ly kèm chủ sở hữu. **Cột mới xuất hiện không phải lý do dừng đường nạp**, còn cột đổi kiểu thu hẹp thì phải dừng. Phiên bản lược đồ ghi trong phong bì nên truy được lô nào theo lược đồ nào. Đường phục hồi sau khi sửa: nạp lại từ vùng cách ly chứ bỏ. Ba cách trình kết nối có sẵn xử lý việc này và vì sao phải kiểm chứ tin.

**Outcome.** Cài phát hiện và phân loại lệch lược đồ ba mức, chứng minh mỗi mức đi đúng đường xử lý.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu bằng phép thử tiêm ba mức. Kiểm bằng sáu thay đổi tiêm; đạt khi phân loại đúng ít nhất năm và không lô nào bị bỏ im lặng.

**Lab.** Đăng ký lược đồ cho ba nguồn. Tiêm sáu thay đổi thuộc ba mức, gồm thêm cột, bỏ cột, đổi kiểu mở rộng, đổi kiểu thu hẹp, đổi tên, và đổi nghĩa mà giữ kiểu. Chứng minh từng cái được phát hiện, phân đúng mức và đi đúng đường xử lý. Sửa một thay đổi phá vỡ rồi nạp lại từ vùng cách ly và đối soát.

**Pitfalls.** Dừng đường nạp khi chỉ có cột mới · để bước biến đổi phát hiện lệch thay vì bước nạp · bỏ lô hỏng thay vì cách ly · không ghi phiên bản lược đồ vào phong bì.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân loại đúng ≥ 5/6 thay đổi, không lô nào bị bỏ im lặng, và lô cách ly nạp lại được với đối soát khớp.

### Lesson 242 · Reconciliation from source to landing `TH`
**Prerequisites.** Lesson 241

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Đối soát là bằng chứng duy nhất cho tính đầy đủ, và mọi thứ khác chỉ là dấu hiệu. Thang đối soát bốn bậc theo chi phí tăng dần: tổng kiểm soát gồm số dòng, tổng, nhỏ nhất và lớn nhất theo phân vùng; so tập khoá để biết thiếu, thừa hay trùng cụ thể; băm dòng trên giá trị đã chuẩn hoá; và bất biến nghiệp vụ xuyên bảng. Chuẩn hoá trước khi băm là bước quyết định: thời gian, số thập phân, giá trị rỗng và thứ tự cột phải quy về một dạng, nếu không thì hai bên đúng vẫn cho hai băm khác nhau, đúng vấn đề đã gặp ở lesson 223. Ranh giới trích xuất phải bất biến khi đối soát, nếu không thì nguồn đã đổi giữa hai lần đếm và chênh lệch là giả. **Lấy mẫu không chứng minh được tính đầy đủ** và nhầm lẫn này là lỗi lập luận chính của bài. Ngân sách chênh lệch được chấp nhận phải có người duyệt chứ do kỹ thuật tự đặt.

**Outcome.** Chạy đủ bốn bậc đối soát cho ba nguồn và giải thích mọi chênh lệch còn lại bằng nguyên nhân cụ thể.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chứng minh tính đầy đủ chứ đưa dấu hiệu. Kiểm bằng bốn bậc cho ba nguồn; đạt khi bậc hai chỉ đúng khoá lệch, và mọi chênh lệch còn lại có nguyên nhân được nêu tên chứ bỏ qua.

**Lab.** Với ba nguồn, chạy cả bốn bậc đối soát tại một ranh giới bất biến. Tiêm ba lỗi: mất một lô, trùng một lô, và một cột bị làm tròn khác. Chứng minh bậc nào phát hiện được lỗi nào. Chuẩn hoá giá trị trước khi băm và chỉ ra chênh lệch giả biến mất. Viết ngân sách chênh lệch kèm người duyệt.

**Pitfalls.** Đối soát bằng lấy mẫu rồi kết luận đầy đủ · băm mà không chuẩn hoá · đếm hai bên ở hai thời điểm khác nhau · tự đặt ngân sách chênh lệch được chấp nhận.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn bậc chạy cho cả ba nguồn, ba lỗi tiêm được quy đúng bậc phát hiện, và mọi chênh lệch còn lại có nguyên nhân nêu tên.

### Lesson 243 · Ingestion SLO and the backfill isolation rule `TH`
**Prerequisites.** Lesson 242

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Đường nạp là dịch vụ, nên nó có chỉ số và cam kết. Bảy chỉ số phải đo: độ trễ trích xuất, độ tươi của vùng thô, tỉ lệ lần chạy thành công, số dòng và số byte, số lỗi lược đồ, tải đặt lên nguồn, và chênh lệch đối soát. Chỉ số cuối là chỉ số duy nhất nói về tính đúng, và sáu chỉ số kia đều xanh mà nó đỏ là tình huống phải nhận ra. Đặt cam kết theo nhu cầu của quyết định hạ nguồn theo lesson 185, chứ theo năng lực hiện có. Định tuyến cảnh báo theo chủ sở hữu và mức nghiêm trọng, tránh cảnh báo không hành động được. **Nạp bù phải cách ly khỏi lần chạy hằng ngày**: hạn mức riêng, hàng đợi riêng, cửa sổ riêng, và ngưỡng dừng; chạy chung là một trong những chế độ hỏng bị liệt vào danh sách tự động chưa đạt. Tiến độ từng phần và điểm kiểm tra cho nạp bù dài, để dừng giữa chừng không mất công đã làm.

**Outcome.** Dựng bộ bảy chỉ số cùng cam kết, và chứng minh nạp bù 90 phân vùng không phá cam kết của lần chạy hằng ngày.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là cam kết hằng ngày giữ được trong lúc nạp bù. Kiểm bằng thí nghiệm chạy song song; đạt khi độ tươi hằng ngày trong cam kết suốt thời gian nạp bù và nguồn không vượt hạn mức.

**Lab.** Dựng bộ bảy chỉ số và đặt cam kết cho ba chỉ số quan trọng nhất. Chạy nạp bù 90 phân vùng đồng thời với lần chạy hằng ngày, có hạn mức và hàng đợi riêng. Đo độ tươi hằng ngày và tải nguồn suốt quá trình. Dừng nạp bù giữa chừng và chứng minh chạy tiếp được từ điểm kiểm tra. Tạo một tình huống sáu chỉ số xanh mà chênh lệch đối soát đỏ.

**Pitfalls.** Chạy nạp bù chung hàng đợi với lần chạy hằng ngày · đặt cam kết theo năng lực hiện có · cảnh báo trên chỉ số không hành động được · nạp bù không có điểm kiểm tra nên dừng là mất hết.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Độ tươi hằng ngày trong cam kết suốt 90 phân vùng nạp bù, nguồn không vượt hạn mức, và nạp bù tiếp được từ điểm kiểm tra.

### Lesson 244 · Connector landscape - build, adopt or buy `LT`
**Prerequisites.** Lesson 243

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Năm nhóm công cụ và tiêu chí chọn, với một ranh giới trách nhiệm phải nói rõ. Dịch vụ nạp được quản lý: nhanh để có kết quả, chi phí theo lượng dữ liệu, và hành vi xử lý lệch lược đồ cùng thử lại phải kiểm chứ đọc trang giới thiệu. Trình kết nối mã nguồn mở: kiểm soát được, đổi lại phải tự vận hành. Bắt thay đổi từ nhật ký giao dịch, học sâu ở M17. Dịch vụ truyền dữ liệu của nhà cung cấp đám mây. Tự viết: bắt buộc cho nguồn không ai hỗ trợ hoặc nguồn trọng yếu. Mười tiêu chí chọn gồm ngữ nghĩa nguồn được hỗ trợ, xử lý xoá và lịch sử, lệch lược đồ, ai giữ trạng thái, hạn mức và nạp bù, bảo mật, khả năng quan sát, chi phí, khả năng mở rộng, và đường phục hồi. **Có trình kết nối không chứng minh ngữ nghĩa đúng**: công cụ chuyển giao trách nhiệm vận hành, không chuyển giao trách nhiệm về tính đúng, nên đối soát vẫn là của ta.

**Outcome.** Chọn nhóm công cụ cho ba nguồn theo mười tiêu chí và nêu trách nhiệm nào không được chuyển giao.

**Đánh giá.** Tầng *đánh giá*. Objective đòi phân biệt trách nhiệm vận hành với trách nhiệm về tính đúng. Kiểm bằng bản ghi quyết định ba nguồn; đạt khi mỗi lựa chọn có ít nhất năm tiêu chí được kiểm bằng thực nghiệm chứ bằng tài liệu.

**Lab.** Cho ba nguồn có ngữ nghĩa khác nhau, trong đó một nguồn có xoá cứng. Chấm ba nhóm công cụ theo mười tiêu chí. Với công cụ được chọn, kiểm bằng thực nghiệm ít nhất năm tiêu chí gồm hành vi khi lược đồ đổi và hành vi khi nguồn xoá bản ghi. Viết bản ghi quyết định nêu rõ trách nhiệm nào vẫn thuộc về đội.

**Pitfalls.** Chọn công cụ theo danh sách nguồn được hỗ trợ · tin tài liệu về hành vi lệch lược đồ · giả định công cụ xử lý xoá đúng · coi dùng dịch vụ quản lý là hết trách nhiệm đối soát.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mỗi lựa chọn có ≥ 5 tiêu chí kiểm bằng thực nghiệm, và bản ghi quyết định nêu rõ trách nhiệm về tính đúng vẫn thuộc đội.

### Lesson 245 · Ingestion capstone - three sources into one raw zone `DA`
**Prerequisites.** Lesson 244

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Bài dự án tổng hợp module, lấy đúng yêu cầu capstone của hợp đồng nguồn. Nạp ba loại nguồn vào một vùng thô trên kho đối tượng: một cơ sở dữ liệu quan hệ, một giao diện lập trình có phân trang, và tệp đối tác giao hằng ngày. Ba chế độ vận hành phải chạy được: khởi tạo ban đầu, tăng dần hằng ngày, và nạp bù 90 ngày. Yêu cầu bắt buộc: chạy lại luỹ đẳng, hạ cánh nguyên tử theo lesson 240, hợp đồng lược đồ có phiên bản và vùng cách ly, bảo vệ nguồn cùng quản lý thông tin xác thực, phát tín hiệu danh mục và dòng dõi khi công bố, và bộ chỉ số cùng bảng theo dõi cùng sổ tay vận hành. Đối soát độc lập từ nguồn tới vùng thô cho cả ba nguồn là tiêu chí nghiệm thu chính, chứ số lần chạy thành công.

**Outcome.** Nộp hệ nạp ba nguồn chạy được cả ba chế độ, với đối soát độc lập đạt cho cả ba.

**Đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module thành một hệ vận hành được. Kiểm bằng đối soát độc lập cộng rà soát sổ tay; đạt khi ba nguồn đối soát khớp trong ngân sách chênh lệch đã duyệt và mọi chế độ chạy lại được.

**Lab.** Dựng hệ nạp ba nguồn. Chạy khởi tạo, chạy tăng dần bảy ngày, rồi nạp bù 90 ngày có cách ly. Chạy đối soát bốn bậc cho cả ba nguồn. Giết tiến trình ngẫu nhiên trong mỗi chế độ và chứng minh chạy lại phục hồi đúng. Nộp sổ tay vận hành gồm đặt lại điểm kiểm tra, xoay thông tin xác thực, nguồn hỏng và quy trình chạy lại.

**Pitfalls.** Coi lần chạy thành công là bằng chứng đầy đủ · bỏ chế độ nạp bù vì tốn thời gian · để thông tin xác thực trong mã hoặc nhật ký · chạy lại bằng cách xoá đích rồi nạp lại mà không đối soát.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Ba nguồn đối soát khớp trong ngân sách đã duyệt, ba chế độ vận hành chạy được, và giết tiến trình ở mọi chế độ đều phục hồi đúng.

### Lesson 246 · Game day - provider throttling, cursor expiry and duplicate delivery `TH`
**Prerequisites.** Lesson 245

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài diễn tập sự cố khép module, chạy trên chính hệ đã dựng ở bài trước. Sáu tình huống bắt buộc, mỗi tình huống có một hành vi kỳ vọng ghi trước: nhà cung cấp trả mã từ chối vì vượt hạn mức trong lúc nạp bù; nhà cung cấp trả lỗi máy chủ ngẫu nhiên; con trỏ phân trang hết hạn giữa chừng; bản sao cơ sở dữ liệu trễ bất thường; tệp đối tác giao thiếu một phần; và cùng một lô được giao hai lần. Với mỗi tình huống, ba câu hỏi phải trả lời bằng bằng chứng: hệ có phát hiện không, ảnh hưởng có bị chặn trong phạm vi không, và phục hồi mất bao lâu. **Hành vi kỳ vọng phải viết trước khi chạy**, vì viết sau thì luôn khớp. Kết quả diễn tập là đầu vào sửa sổ tay vận hành chứ một buổi biểu diễn.

**Outcome.** Chạy sáu tình huống sự cố và chứng minh phát hiện, chặn phạm vi cùng phục hồi cho từng cái.

**Đánh giá.** Tầng *đánh giá*. Objective đo năng lực vận hành dưới sự cố có tiêu chí viết trước. Kiểm bằng sáu tình huống; đạt khi ít nhất năm được phát hiện tự động và mọi tình huống phục hồi với đối soát khớp.

**Lab.** Viết hành vi kỳ vọng cho sáu tình huống trước khi chạy. Chạy từng cái trên hệ đã dựng. Ghi lại thời điểm phát hiện, phạm vi ảnh hưởng và thời gian phục hồi. Đối soát sau mỗi lần phục hồi. So kết quả với hành vi kỳ vọng và sửa sổ tay vận hành theo chênh lệch.

**Pitfalls.** Viết hành vi kỳ vọng sau khi đã thấy kết quả · coi phục hồi bằng tay là đạt mà không ghi vào sổ tay · bỏ qua tình huống giao trùng lô vì nghĩ khử trùng đã lo · không đối soát sau khi phục hồi.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** ≥ 5/6 tình huống được phát hiện tự động, mọi tình huống phục hồi với đối soát khớp, và sổ tay được sửa theo chênh lệch quan sát.

# MODULE M14 · ELT, DBT AND WORKFLOW ORCHESTRATION

**Phase 7 · Lessons 247–274 · 56 giờ**

| | |
|---|---|
| **Objective cấp module** | Thiết kế đường dẫn theo lô có tính đúng qua chạy lại, nạp bù và đổi lược đồ; thành thạo dbt và thành thạo **một** bộ điều phối |
| **Tiền đề** | M1 · M2 · M9 · M10 · M11 · M12 · M13 · M14B |
| **Exit criterion** | Ít nhất ba mô hình tăng dần qua trọn ma trận chế độ hỏng kèm chứng minh bảy phần; một lần đổi lược đồ phá vỡ có phiên bản, kế hoạch chuyển đổi cho bên tiêu thụ và đường quay lại |
| **Kỹ năng SFIA** | `DTAN` mức 5 · `PROG` mức 4 · `SYSP` mức 4 |
| **Chế độ hỏng** | Tắt phép kiểm hoặc hạ mức nghiêm trọng để đường dẫn xanh, và dùng nạp lại toàn bộ như cách mặc định để chữa lỗi của mô hình tăng dần mà không truy nguyên nhân |

Module dài nhất chương trình, và nó có một quy tắc chọn công cụ tường minh: **thành thạo dbt, và thành thạo đúng một bộ điều phối**, chọn theo nơi làm việc. Bộ điều phối còn lại học tới mức hiểu kiến trúc và khác biệt. Học song song hai bộ tới mức sản xuất là cách chắc chắn không thành thạo cái nào.

Nguyên lý chung nằm ở phần đầu và không phụ thuộc công cụ: ngữ nghĩa nạp, công bố nguyên tử, luỹ đẳng, thời gian sự kiện so với thời gian xử lý, và nạp bù. Học phần đó một lần rồi mới mở công cụ.

Phần nặng nhất là mô hình tăng dần, và nó có một nghĩa vụ chứng minh bảy phần mà không mô hình nào được miễn.

### Lesson 247 · ETL against ELT - where the compute lives `LT`
**Prerequisites.** Module 14: M14B

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Hai kiến trúc khác nhau ở một điểm duy nhất là nơi phép biến đổi chạy, và mọi khác biệt còn lại suy ra từ đó. Biến đổi trước khi nạp thắng khi dữ liệu không được phép vào đích ở dạng thô, khi đích có ràng buộc về lược đồ, hoặc khi phép biến đổi cần môi trường chạy chuyên biệt mà đích không có; ví dụ rõ nhất là khử định danh dữ liệu cá nhân trước khi hạ cánh. Nạp thô rồi biến đổi thắng khi cần giữ lịch sử thô để chạy lại và khi đích có năng lực tính toán co giãn; đổi lại chi phí tính toán chuyển sang đích và dữ liệu thô phải được quản trị. **Không được kết luận nạp thô rồi biến đổi hiện đại hơn nên tốt hơn**; đó là một lựa chọn có điều kiện chứ một tiến bộ. Kiến trúc lai: kiểm tra và che dữ liệu nhạy cảm ở mức nhẹ trước, phần nặng sau. Năm chiều để chọn gồm nơi tính toán, độ nhạy dữ liệu, độ trễ, quản trị và mức phụ thuộc nhà cung cấp.

**Outcome.** Chọn kiến trúc cho ba khối lượng công việc theo năm chiều và giữ được tính đúng khi một ràng buộc đảo chiều.

**Đánh giá.** Tầng *đánh giá*. Bài mở module, đòi chọn theo ràng buộc chứ theo xu hướng. Kiểm bằng ba bối cảnh cộng một thay đổi ràng buộc do người chấm đưa ra; đạt khi thiết kế thích ứng mà không mất khả năng chạy lại.

**Lab.** Cho ba khối lượng công việc. Chấm hai kiến trúc theo năm chiều cho từng cái. Đo thời gian và chi phí của cùng một phép biến đổi chạy ở hai nơi. Người chấm đổi một ràng buộc, chẳng hạn cấm dữ liệu cá nhân thô vào đích hoặc nhân đôi giá tính toán; điều chỉnh thiết kế và chứng minh vẫn chạy lại được.

**Pitfalls.** Kết luận nạp thô rồi biến đổi luôn tốt hơn · đưa dữ liệu cá nhân thô vào đích vì tiện · bỏ khả năng chạy lại khi chuyển sang biến đổi trước · so hai kiến trúc mà không đo chi phí tính toán.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba bối cảnh có bảng chấm năm chiều kèm số đo, và thiết kế thích ứng được với ràng buộc đảo chiều mà vẫn chạy lại được.

### Lesson 248 · Load semantics - append, upsert, merge, replace and swap `TH`
**Prerequisites.** Lesson 247

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Năm ngữ nghĩa nạp, mỗi cái có điều kiện đúng riêng và hành vi khi chạy lại riêng. Thêm mới là rẻ nhất và trùng lặp khi chạy lại trừ khi có khử trùng. Ghi đè theo khoá đòi khoá duy nhất thật, và khoá không duy nhất làm kết quả phụ thuộc thứ tự. Trộn kết hợp thêm, sửa và xoá trong một thao tác, nên nó cần quy tắc chọn thắng xác định khi nguồn có nhiều bản ghi cùng khoá. Thay thế toàn bộ phân vùng là cách luỹ đẳng đơn giản nhất và thường bị bỏ qua: **ghi đè cả phân vùng làm chạy lại tự nhiên luỹ đẳng**, đổi lại tốn hơn khi phân vùng lớn. Hoán đổi ghi ra bảng tạm rồi đổi con trỏ, cho công bố nguyên tử theo lesson 226. Bảng đối chiếu năm ngữ nghĩa với hành vi chạy lại là đầu ra của bài, và nó được dùng lại ở lesson 261.

**Outcome.** Cài cả năm ngữ nghĩa nạp và lập bảng hành vi chạy lại có kiểm chứng bằng số cho từng cái.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là chạy lại hai lần cho cùng trạng thái. Kiểm bằng phép thử chạy lại; đạt khi bảng năm hàng có kết quả thực nghiệm và mọi ngữ nghĩa được tuyên bố luỹ đẳng đều qua phép thử chạy hai lần.

**Lab.** Cài năm ngữ nghĩa cho cùng một tập dữ liệu. Chạy mỗi cái hai lần liên tiếp và so trạng thái đích sau lần một với sau lần hai. Tạo nguồn có hai bản ghi cùng khoá và quan sát hành vi của ghi đè cùng trộn. Lập bảng năm hàng gồm điều kiện đúng, hành vi chạy lại và chi phí đo được.

**Pitfalls.** Dùng thêm mới rồi khử trùng ở bước sau mà không có quy tắc chọn thắng · ghi đè theo khoá không thật sự duy nhất · trộn mà không xác định bản ghi thắng · cho rằng nạp thành công là luỹ đẳng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng năm hàng có kết quả thực nghiệm, và mọi ngữ nghĩa tuyên bố luỹ đẳng đều cho trạng thái đích giống nhau sau hai lần chạy.

### Lesson 249 · Atomic publish and the partial-state reader `TH`
**Prerequisites.** Lesson 248

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bên đọc không được phép thấy trạng thái nửa vời, và bảo đảm đó phải chứng minh chứ giả định. Ba cách công bố nguyên tử: giao dịch trong cơ sở dữ liệu, hoán đổi tên bảng hoặc con trỏ, và chốt giao dịch của định dạng bảng mở theo lesson 226. Ranh giới nguyên tử nằm ở đâu là câu hỏi phải trả lời được cho từng cách. Ghi thẳng vào bảng đang phục vụ là cách chắc chắn tạo trạng thái nửa vời: bên đọc chạy giữa chừng thấy một nửa dữ liệu mới một nửa cũ, và **số ra sai mà không có lỗi nào**. Phát hiện bằng cách chạy truy vấn liên tục trong lúc nạp và ghi lại mọi kết quả bất thường. Nguyên tử ở mức một bảng không có nghĩa nguyên tử xuyên nhiều bảng; khi nhiều bảng phải đổi cùng lúc thì cần một cơ chế khác và phải nói rõ giới hạn. Dấu hiệu hoàn tất cho bên tiêu thụ.

**Outcome.** Chứng minh bằng thực nghiệm rằng bên đọc không bao giờ thấy trạng thái nửa vời với cách công bố đã chọn.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu bằng phép quan sát liên tục trong lúc ghi. Kiểm bằng phép thử đọc song song; đạt khi không lần đọc nào trong hàng nghìn lần thấy trạng thái nửa vời, và ca ghi thẳng bị chứng minh là thấy.

**Lab.** Cài ba cách công bố. Với mỗi cách, chạy một tiến trình đọc liên tục trong khi nạp một lô lớn, ghi lại tổng ở mỗi lần đọc. Cài thêm một bản ghi thẳng vào bảng phục vụ và chứng minh bên đọc thấy giá trị trung gian. Thử một thay đổi xuyên hai bảng và chỉ ra giới hạn của bảo đảm.

**Pitfalls.** Ghi thẳng vào bảng đang phục vụ · giả định nguyên tử một bảng suy ra nguyên tử nhiều bảng · kiểm bằng cách đọc một lần sau khi nạp xong · dùng dấu hiệu hoàn tất mà không nguyên tử ở bước ghi.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Không lần đọc nào thấy trạng thái nửa vời với cách đã chọn, ca ghi thẳng được chứng minh là thấy, và giới hạn xuyên bảng được nêu.

### Lesson 250 · Idempotency for batch - deterministic keys and overwrite `TH`
**Prerequisites.** Lesson 249

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Luỹ đẳng ở tầng theo lô có bốn cơ chế, và chọn theo hình dạng dữ liệu chứ theo thói quen. Khoá xác định sinh từ nội dung bản ghi cộng vị trí nguồn, nên cùng đầu vào cho cùng khoá; băm phải tính trên giá trị đã chuẩn hoá theo lesson 242. Ghi đè cả phân vùng là cơ chế mạnh nhất và đơn giản nhất khi phân vùng đủ nhỏ. Trộn theo khoá duy nhất. Khử trùng ở bước đọc bằng cách giữ bản ghi thắng theo quy tắc xác định. Dấu hiệu hoàn tất cho biết một phân vùng đã xong, nên lần chạy sau bỏ qua; nó phải ghi sau dữ liệu và trong cùng ranh giới nguyên tử. Bốn cơ chế này nối thẳng với khoá chống trùng ở lesson 105, khác biệt là ở đây đơn vị là phân vùng chứ yêu cầu. **Thực thi ít nhất một lần cộng tác dụng phụ luỹ đẳng là mô hình thực tế**, và nó mạnh hơn một tuyên bố đúng một lần không có ranh giới.

**Outcome.** Chọn và cài cơ chế luỹ đẳng cho bốn đường dẫn, chứng minh chạy lại nhiều lần cho cùng trạng thái.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là trạng thái hội tụ sau nhiều lần chạy ngẫu nhiên. Kiểm bằng phép thử chạy lại hỗn loạn; đạt khi trạng thái sau 20 lần chạy chồng chéo khớp trạng thái sau một lần chạy sạch.

**Lab.** Cài bốn cơ chế cho bốn đường dẫn có hình dạng dữ liệu khác nhau. Chạy mỗi đường dẫn 20 lần với thời điểm bắt đầu ngẫu nhiên và có lần bị giết giữa chừng. So trạng thái cuối với trạng thái của một lần chạy sạch. Đo chi phí của ghi đè phân vùng khi phân vùng lớn dần.

**Pitfalls.** Băm trên giá trị chưa chuẩn hoá · ghi dấu hiệu hoàn tất trước dữ liệu · dùng ghi đè phân vùng cho phân vùng quá lớn · tuyên bố đúng một lần mà không nêu ranh giới.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Trạng thái sau 20 lần chạy chồng chéo khớp trạng thái của một lần chạy sạch ở cả bốn đường dẫn.

### Lesson 251 · Event time, processing time and late data `TH`
**Prerequisites.** Lesson 250

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba trục thời gian trong một đường dẫn theo lô và trộn chúng là nguồn của báo cáo lệch. Thời gian sự kiện là lúc việc xảy ra; thời gian xử lý là lúc hệ ta chạy; thời gian nạp là lúc dữ liệu vào đích. Phân vùng theo trục nào là một quyết định có hậu quả: phân vùng theo thời gian sự kiện cho báo cáo đúng nhưng dữ liệu tới muộn làm phân vùng cũ phải cập nhật lại; phân vùng theo thời gian nạp thì phân vùng bất biến nhưng báo cáo theo ngày phải quét nhiều phân vùng. Dữ liệu tới muộn cần một cửa sổ cập nhật lại có độ rộng tính từ phân bố độ trễ quan sát được, và **phần đuôi vượt cửa sổ phải có chính sách rõ** chứ bỏ im lặng. Hiệu chỉnh và bản ghi đánh dấu xoá. Nối với hai trục thời gian ở lesson 158: ở đây trục thứ ba là thời gian xử lý của bộ điều phối.

**Outcome.** Chọn trục phân vùng cho hai đường dẫn và xử lý dữ liệu tới muộn với cửa sổ tính từ phân bố thật.

**Đánh giá.** Tầng *áp dụng*. Objective đòi rút tham số từ dữ liệu quan sát chứ đặt tuỳ ý. Kiểm bằng đối soát báo cáo sau khi dữ liệu muộn tới; đạt khi báo cáo phân vùng cũ tự đúng lại trong cửa sổ và phần vượt cửa sổ có chính sách áp dụng được.

**Lab.** Đo phân bố độ trễ giữa thời gian sự kiện và thời gian nạp trên dữ liệu thật; chọn độ rộng cửa sổ từ một phân vị có lý do. Cài cập nhật lại phân vùng trong cửa sổ. Tiêm dữ liệu muộn cả trong và ngoài cửa sổ. Đối soát báo cáo theo ngày trước và sau. Áp chính sách cho phần vượt cửa sổ và ghi lại số dòng bị ảnh hưởng.

**Pitfalls.** Phân vùng theo thời gian nạp rồi báo cáo theo ngày sự kiện mà không nói rõ · đặt cửa sổ cập nhật lại bằng một con số tròn · bỏ dữ liệu vượt cửa sổ im lặng · trộn ba trục thời gian trong một cột.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Độ rộng cửa sổ dẫn được từ phân bố độ trễ thật, báo cáo phân vùng cũ tự đúng lại trong cửa sổ, và phần vượt cửa sổ có chính sách cùng số dòng ghi lại.

### Lesson 252 · Backfill - plan, isolate, validate, promote `TH`
**Prerequisites.** Lesson 251

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Nạp bù là thao tác rủi ro nhất trong vận hành đường dẫn, nên nó có quy trình bốn bước bắt buộc. Lập kế hoạch: chia theo phân vùng, ước lượng chi phí bằng số phân vùng nhân chi phí trung bình và chi phí đỉnh, và xác định ngưỡng dừng cùng trần chi phí. Cách ly: hàng đợi riêng, hạn mức riêng, và đích riêng nếu có thể, để lần chạy hằng ngày và hệ nguồn không bị ảnh hưởng, nguyên tắc đã đặt ở lesson 243. Kiểm chứng: đối soát kết quả nạp bù ở đích cách ly trước khi cho ra bảng phục vụ. Thăng cấp: hoán đổi nguyên tử, và có đường quay lại. Tiến độ từng phần và điểm kiểm tra cho phép dừng giữa chừng mà không mất công. **Mã và cấu hình tại thời điểm chạy lại có thể khác lúc chạy gốc**, nên kết quả nạp bù có thể khác kết quả lịch sử, và phải nói rõ điều đó chứ coi là như nhau.

**Outcome.** Lập và thực hiện kế hoạch nạp bù 90 phân vùng có cách ly, kiểm chứng và đường quay lại.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là cam kết hằng ngày không vỡ và đối soát đạt trước khi thăng cấp. Kiểm bằng thí nghiệm nạp bù đầy đủ; đạt khi độ tươi hằng ngày trong cam kết, đối soát đạt ở đích cách ly, và quay lại được sau khi thăng cấp.

**Lab.** Lập kế hoạch nạp bù 90 phân vùng gồm ước lượng chi phí, ngưỡng dừng và trần chi phí. Chạy vào đích cách ly, đồng thời với lần chạy hằng ngày. Đối soát đích cách ly với nguồn. Thăng cấp bằng hoán đổi nguyên tử rồi thực hiện quay lại. So kết quả nạp bù với kết quả lịch sử và giải thích mọi chênh lệch do mã đổi.

**Pitfalls.** Nạp bù thẳng vào bảng phục vụ · không có trần chi phí nên hoá đơn vượt dự kiến · thăng cấp trước khi đối soát · coi kết quả nạp bù bằng kết quả lịch sử mà không kiểm.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Độ tươi hằng ngày trong cam kết suốt nạp bù, đối soát đạt ở đích cách ly trước khi thăng cấp, và quay lại thực hiện được.

### Lesson 253 · dbt mental model - parse, compile, run, build `LT`
**Prerequisites.** Lesson 252

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài mở phần dbt bằng việc nói rõ công cụ này là gì và không là gì. Nó là khung xây dựng phép biến đổi, **không phải công cụ nạp dữ liệu và không phải bộ điều phối đa hệ**; dùng nó ngoài phạm vi đó là nguồn của phần lớn thiết kế tồi. Bốn pha và khác biệt giữa chúng: phân tích dự án thành đồ thị, kết xuất mẫu thành câu lệnh SQL, chạy để thực thi, và lệnh xây dựng chạy cả mô hình lẫn phép kiểm theo thứ tự đồ thị. Trả lời được bốn lệnh khác nhau ở đồ thị nào, hành động gì và sinh hiện vật gì là một câu hỏi bắt buộc của module. Hàm tham chiếu mô hình và hàm tham chiếu nguồn dựng nên đồ thị, nên không bao giờ viết cứng tên bảng. Ranh giới bộ chuyển đổi: cái gì mang đi được giữa các kho dữ liệu và cái gì phụ thuộc kho cụ thể. Bố cục kho mã và vì sao nó phản ánh ba tầng mô hình.

**Outcome.** Phân biệt bốn pha theo đồ thị, hành động và hiện vật, và đọc được câu lệnh SQL đã kết xuất.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết mở phần công cụ sau sáu bài nguyên lý. Kiểm bằng bài đối chiếu bốn lệnh; đạt khi bảng bốn lệnh đúng ở cả ba cột và câu lệnh kết xuất được đối chiếu với mã nguồn.

**Lab.** Dựng một dự án tối thiểu trên cơ sở dữ liệu cục bộ với ba mô hình. Chạy cả bốn lệnh và ghi lại đồ thị được chọn, hành động thực hiện và hiện vật sinh ra. Mở câu lệnh SQL đã kết xuất của một mô hình và đối chiếu từng phần với mã nguồn. Vẽ đồ thị phụ thuộc và chỉ ra hàm tham chiếu nào tạo cạnh nào.

**Pitfalls.** Viết cứng tên bảng thay vì dùng hàm tham chiếu · dùng công cụ này để nạp dữ liệu · nhầm lệnh chạy với lệnh xây dựng · không bao giờ đọc câu lệnh đã kết xuất.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng bốn lệnh đúng ở cả ba cột, và câu lệnh kết xuất của một mô hình được đối chiếu đầy đủ với mã nguồn.

### Lesson 254 · Project layers - staging, intermediate and marts `TH`
**Prerequisites.** Lesson 253

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba tầng với ba nhiệm vụ tách bạch, và trộn chúng làm đồ thị không đọc được. Tầng chuẩn bị ánh xạ một đối một với nguồn: đổi tên, ép kiểu, dọn dẹp, và **không có phép gộp nghiệp vụ**; nó là chỗ duy nhất biết tên cột gốc của nguồn. Tầng trung gian chứa các đơn vị logic dùng lại được, phép kết và phép xoay; nó không được tiêu thụ trực tiếp. Tầng phục vụ có hạt rõ ràng theo lesson 150 và là hợp đồng với bên tiêu thụ. Quy ước đặt tên, cấu hình theo thư mục, nhãn và nhóm. Mô hình khổng lồ là dấu hiệu thiếu tầng trung gian. Tiêu chí ra của bài lấy thẳng từ hợp đồng nguồn và đo được: **một người rà soát chỉ đọc tệp và tài liệu mô hình phải xác định được hạt, chủ sở hữu, nguồn thượng lưu và bên tiêu thụ**. Độ tươi của nguồn và quyền sở hữu khai báo ở tầng chuẩn bị.

**Outcome.** Dựng dự án ba tầng sao cho người rà soát xác định được bốn thuộc tính của mọi mô hình chỉ từ tệp.

**Đánh giá.** Tầng *áp dụng*. Objective có phép thử khách quan là kết quả của người rà soát độc lập. Kiểm bằng phép thử rà soát chéo; đạt khi người rà soát xác định đúng bốn thuộc tính ở ít nhất tám trên mười mô hình.

**Lab.** Dựng dự án ít nhất mười mô hình đủ ba tầng. Đưa cho một học viên khác chỉ đọc tệp và tài liệu mô hình, yêu cầu họ ghi ra hạt, chủ sở hữu, nguồn thượng lưu và bên tiêu thụ của từng mô hình. Đếm số mô hình họ xác định đúng cả bốn. Sửa những mô hình họ không xác định được và kiểm lại.

**Pitfalls.** Đặt phép gộp nghiệp vụ ở tầng chuẩn bị · để bên tiêu thụ đọc thẳng tầng trung gian · viết mô hình khổng lồ thay vì tách tầng trung gian · dùng tên cột gốc của nguồn ở tầng phục vụ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Người rà soát độc lập xác định đúng bốn thuộc tính ở ≥ 8/10 mô hình chỉ từ tệp và tài liệu.

### Lesson 255 · Materializations - four choices, one ADR `TH`
**Prerequisites.** Lesson 254

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bốn cách hiện thực hoá một mô hình, khác nhau ở bốn chiều chi phí. Khung nhìn không tốn dung lượng và luôn tươi, nhưng chi phí dồn sang mỗi lần truy vấn. Bảng tốn chi phí dựng và dung lượng, đổi lại truy vấn rẻ. Dạng phù du được nhúng thẳng vào mô hình hạ nguồn, nên không tồn tại trong kho và **không gỡ lỗi được bằng cách truy vấn nó**, đây là đánh đổi chính của nó. Tăng dần chỉ xử lý phần mới, rẻ nhất khi chạy nhưng phức tạp nhất về tính đúng, nội dung của bốn bài sau. Bốn chiều so: chi phí dựng, chi phí truy vấn, dung lượng, và mức dễ gỡ lỗi cùng phụ thuộc. Quy tắc thực dụng: bắt đầu bằng khung nhìn hoặc bảng, chỉ chuyển sang tăng dần khi có bằng chứng chi phí dựng là vấn đề. Cách hiện thực hoá tự viết chỉ sau khi bốn cách mặc định không đủ và có người bảo trì.

**Outcome.** So bốn cách trên cùng mô hình theo bốn chiều và nộp bản ghi quyết định dựa trên số đo.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn theo số đo và chống việc mặc định dùng tăng dần. Kiểm bằng bảng bốn cách nhân bốn chiều; đạt khi ba chiều đầu có số đo thật và lựa chọn kèm ngưỡng chuyển đổi.

**Lab.** Chạy cùng một mô hình với cả bốn cách hiện thực hoá. Đo chi phí dựng, chi phí truy vấn và dung lượng cho từng cách. Đánh giá mức dễ gỡ lỗi bằng cách thử truy vấn kết quả trung gian. Lập bảng bốn nhân bốn. Viết bản ghi quyết định nêu ngưỡng khối lượng dữ liệu mà lựa chọn đổi.

**Pitfalls.** Mặc định dùng tăng dần từ đầu · dùng dạng phù du cho mô hình cần gỡ lỗi · chọn khung nhìn cho mô hình được truy vấn rất nhiều lần · so bốn cách mà không đo dung lượng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng bốn nhân bốn có số đo ở ba chiều đầu, và bản ghi quyết định nêu ngưỡng khối lượng làm lựa chọn đổi.

### Lesson 256 · Generic tests and their limits `TH`
**Prerequisites.** Lesson 255

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bốn phép kiểm có sẵn và giới hạn của từng cái, vì hiểu giới hạn quan trọng hơn biết cách bật. Kiểm không rỗng bắt cột thiếu giá trị nhưng không bắt giá trị canh chừng như chuỗi rỗng hay ngày 1900-01-01, đúng vấn đề ở lesson 231. Kiểm duy nhất bắt trùng khoá nhưng **chỉ trên một cột trừ khi khai báo trên biểu thức**, nên khoá tổ hợp hay bị kiểm sai. Kiểm quan hệ bắt khoá mồ côi nhưng không bắt chiều ngược lại là bản ghi cha không có con. Kiểm giá trị được chấp nhận bắt giá trị lạ nhưng danh sách giá trị lạc hậu khi nguồn thêm mã mới, nên nó vừa là phép kiểm vừa là cảnh báo lược đồ. Mức nghiêm trọng và ngưỡng: một phép kiểm luôn đỏ vì một ca ngoại lệ đã biết sẽ bị tắt, nên ngưỡng có căn cứ tốt hơn tắt. Lưu bản ghi hỏng để điều tra thay vì chỉ đếm.

**Outcome.** Cài bốn phép kiểm cho một mô hình và chỉ ra bằng dữ liệu những lỗi chúng không bắt được.

**Đánh giá.** Tầng *phân tích*. Objective đòi nhận ra giới hạn của công cụ kiểm. Kiểm bằng phép thử tiêm; đạt khi bốn lỗi trong tầm bị bắt và ít nhất ba lỗi ngoài tầm được chỉ ra kèm cách kiểm bổ sung.

**Lab.** Cài bốn phép kiểm cho một mô hình phục vụ. Tiêm bốn lỗi nằm trong tầm và bốn lỗi nằm ngoài tầm gồm giá trị canh chừng, khoá tổ hợp trùng, cha không có con, và mã mới hợp lệ. Ghi lại phép kiểm nào bắt được cái nào. Với mỗi lỗi không bắt được, viết một phép kiểm bổ sung. Bật lưu bản ghi hỏng và điều tra một ca.

**Pitfalls.** Kiểm duy nhất trên một cột khi khoá là tổ hợp · tắt phép kiểm luôn đỏ thay vì đặt ngưỡng · tin bốn phép kiểm là đủ · không lưu bản ghi hỏng nên không điều tra được.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn lỗi trong tầm bị bắt đúng, ≥ 3 lỗi ngoài tầm được chỉ ra và có phép kiểm bổ sung, và một ca hỏng được điều tra từ bản ghi lưu.

### Lesson 257 · Singular tests for business invariants `TH`
**Prerequisites.** Lesson 256

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phép kiểm viết riêng là nơi diễn đạt những quy tắc mà phép kiểm có sẵn không nói được, và chúng thường là phép kiểm có giá trị nhất. Bốn nhóm bất biến nghiệp vụ: bảo toàn tổng giữa hai tầng; bất biến về khoảng thời gian như không chồng lấn ở chiều biến đổi chậm theo lesson 157; bất biến về vòng đời như trạng thái chỉ đi theo một chiều; và bất biến đối soát giữa mô hình với nguồn. Viết phép kiểm theo nguyên tắc trả về dòng vi phạm chứ trả về đúng sai, để bản thân kết quả là đầu mối điều tra. **Phép kiểm tốt phải hỏng khi có lỗi và chỉ khi có lỗi**, nên phải thử cả hai chiều: tiêm lỗi để xem nó đỏ, và chạy trên dữ liệu sạch để xem nó không báo giả. Cân bằng số lượng: quá nhiều phép kiểm ồn làm người trực bỏ qua cảnh báo. Phân biệt phép kiểm chất lượng với phép kiểm đơn vị của logic biến đổi.

**Outcome.** Viết bốn phép kiểm bất biến nghiệp vụ và chứng minh chúng bắt đúng lỗi mà không báo giả.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu hai chiều. Kiểm bằng phép thử tiêm cộng phép thử trên dữ liệu sạch; đạt khi cả bốn bắt đúng lỗi tương ứng và không cái nào báo giả trên 30 ngày dữ liệu sạch.

**Lab.** Viết bốn phép kiểm thuộc bốn nhóm bất biến. Với mỗi cái, tiêm đúng loại lỗi nó nhắm tới và xác nhận nó đỏ. Chạy cả bốn trên 30 ngày dữ liệu sạch và đếm số lần báo giả. Sửa cho tới khi không còn báo giả. Viết một phép kiểm đối soát giữa mô hình phục vụ với vùng thô.

**Pitfalls.** Viết phép kiểm trả về đúng sai nên không điều tra được · không thử trên dữ liệu sạch nên không biết tỉ lệ báo giả · viết hàng trăm phép kiểm ồn · nhầm phép kiểm chất lượng với phép kiểm đơn vị.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn phép kiểm bắt đúng lỗi nhắm tới và không báo giả trên 30 ngày dữ liệu sạch.

### Lesson 258 · Jinja and macros - where abstraction stops paying `TH`
**Prerequisites.** Lesson 257

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hệ mẫu cho phép sinh câu lệnh SQL theo tham số, và nó vừa là công cụ mạnh vừa là nguồn của mã không đọc được. Ngữ cảnh kết xuất và khác biệt giữa thứ chạy lúc phân tích với thứ chạy lúc thực thi là chỗ hay nhầm nhất; gọi cơ sở dữ liệu lúc phân tích làm dự án chậm và khó đoán. Macro là hàm sinh chuỗi: nó cần giao diện rõ, kiểm tham số, tài liệu và đầu ra xác định. Điều phối theo bộ chuyển đổi cho phép cùng một macro sinh câu lệnh khác nhau cho từng kho dữ liệu. **Trừu tượng hoá quá sớm làm dòng dõi và việc gỡ lỗi khó hơn nhiều so với phần lặp lại mà nó tiết kiệm**, nên quy tắc là chỉ tách macro khi một khuôn mẫu đã lặp ổn định ở ba chỗ trở lên. Macro không được che giấu hạt hay quy tắc nghiệp vụ. Ghim phiên bản gói và rà soát khi nâng cấp.

**Outcome.** Viết macro có giao diện kiểm được và nhận ra khi nào không nên tách macro.

**Đánh giá.** Tầng *đánh giá*. Objective đòi phán đoán về mức trừu tượng chứ chỉ viết được macro. Kiểm bằng ba khuôn mẫu lặp; đạt khi tách đúng hai và giải thích được vì sao cái thứ ba không nên tách.

**Lab.** Cho ba khuôn mẫu lặp trong một dự án. Tách hai cái thành macro có kiểm tham số, tài liệu và phép kiểm kết xuất. Với cái thứ ba, lập luận vì sao tách làm mã khó đọc hơn. Đo thời gian phân tích dự án trước và sau. Viết một macro gọi cơ sở dữ liệu lúc phân tích và đo mức chậm nó gây ra.

**Pitfalls.** Tách macro cho mỗi đoạn lặp hai lần · gọi cơ sở dữ liệu trong ngữ cảnh phân tích · viết macro che giấu quy tắc nghiệp vụ · nâng cấp gói mà không rà soát thay đổi.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Hai macro có kiểm tham số và phép kiểm kết xuất, lý do không tách cái thứ ba được lập luận, và chi phí gọi cơ sở dữ liệu lúc phân tích được đo.

### Lesson 259 · Incremental models - the is_incremental contract `TH`
**Prerequisites.** Lesson 258

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài mở phần nặng nhất của module. Mô hình tăng dần chạy hai chế độ khác nhau, và điều kiện chuyển chế độ phải hiểu chính xác: lần đầu hoặc khi nạp lại toàn bộ thì chạy như bảng thường; các lần sau thì chỉ xử lý phần mới dựa trên một điều kiện lọc. Khối lọc chỉ có hiệu lực ở chế độ thứ hai, nên **một lỗi trong khối đó không lộ ra khi chạy trên đích rỗng**, và đó là lý do phải kiểm cả hai chế độ. Khoá duy nhất quyết định hành vi khi bản ghi đã tồn tại. Nguồn của mốc tiến độ có thể lấy từ đích hoặc từ một bảng trạng thái riêng, và hai cách có hành vi khác nhau khi đích bị cắt. Tối ưu quét đích so với lọc nguồn là hai việc khác nhau: lọc nguồn giảm dữ liệu đọc, giới hạn quét đích giảm chi phí trộn, và cần cả hai. Chính sách nạp lại toàn bộ phải viết ra.

**Outcome.** Cài mô hình tăng dần chạy đúng ở cả hai chế độ và giải thích điều kiện chuyển chế độ.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là hai chế độ cho kết quả nhất quán. Kiểm bằng đối chứng; đạt khi kết quả chạy tăng dần bảy ngày khớp kết quả nạp lại toàn bộ trên cùng dữ liệu.

**Lab.** Cài một mô hình tăng dần với khoá duy nhất và điều kiện lọc theo mốc. Chạy trên đích rỗng, rồi chạy tăng dần bảy ngày. Nạp lại toàn bộ trên cùng dữ liệu và so hai kết quả. Cố ý đưa lỗi vào khối lọc và chứng minh nó không lộ ra khi chạy trên đích rỗng. Đo chi phí có và không có giới hạn quét đích.

**Pitfalls.** Chỉ kiểm mô hình bằng cách chạy trên đích rỗng · lọc nguồn mà không giới hạn quét đích · lấy mốc từ đích rồi cắt đích · không có chính sách nạp lại toàn bộ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Kết quả chạy tăng dần bảy ngày khớp kết quả nạp lại toàn bộ, và lỗi trong khối lọc được chứng minh là ẩn ở chế độ đầu.

### Lesson 260 · Incremental strategies by adapter `TH`
**Prerequisites.** Lesson 259

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bốn chiến lược cập nhật và điều kiện dùng, cộng một khác biệt quan trọng là chúng không giống nhau giữa các kho dữ liệu. Thêm mới đơn thuần: nhanh nhất, chỉ đúng khi nguồn không bao giờ sửa. Trộn theo khoá: xử lý được cả thêm và sửa, đòi khoá duy nhất thật và có quy tắc chọn thắng. Xoá rồi chèn: xoá các khoá trùng rồi chèn lại, hành vi giống trộn nhưng chi phí và tính nguyên tử khác. Ghi đè phân vùng: thay cả phân vùng, luỹ đẳng tự nhiên theo lesson 250 và thường là lựa chọn đúng khi dữ liệu phân vùng theo thời gian. Chế độ xử lý theo lô nhỏ có ở một số phiên bản. **Chiến lược nào có sẵn và nó cài đặt ra sao phụ thuộc bộ chuyển đổi**, nên đọc câu lệnh sinh ra là bắt buộc chứ tin tên chiến lược. Quan hệ giữa chiến lược với cách phân vùng và gom cụm ở đích theo lesson 209.

**Outcome.** Chọn chiến lược cho ba mô hình theo hình dạng dữ liệu và xác minh bằng câu lệnh sinh ra.

**Đánh giá.** Tầng *phân tích*. Objective đòi kiểm chứng hành vi công cụ thay vì tin tên gọi. Kiểm bằng bài đọc câu lệnh sinh ra; đạt khi ba chiến lược được đối chiếu với câu lệnh thật và chi phí đo được cho từng cái.

**Lab.** Cài cùng một mô hình với ba chiến lược khác nhau. Với mỗi cái, xuất câu lệnh sinh ra và mô tả chính xác nó làm gì ở đích. Đo chi phí và thời gian. Tạo nguồn có hai bản ghi cùng khoá và quan sát bản nào thắng ở từng chiến lược. Kiểm tính nguyên tử của từng chiến lược bằng phép đọc song song theo lesson 249.

**Pitfalls.** Chọn chiến lược theo tên mà không đọc câu lệnh sinh ra · dùng thêm mới đơn thuần cho nguồn có sửa · trộn theo khoá không duy nhất · giả định mọi chiến lược đều nguyên tử.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba chiến lược được đối chiếu với câu lệnh sinh ra, có số đo chi phí, và bản ghi thắng ở mỗi chiến lược được xác định.

### Lesson 261 · The seven-part incremental proof `TH`
**Prerequisites.** Lesson 260

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài đặt ra nghĩa vụ chứng minh mà hợp đồng nguồn yêu cầu, và không mô hình tăng dần nào được miễn. Bảy phần, mỗi phần là một câu hỏi phải trả lời bằng văn bản kèm phép kiểm: **đầy đủ** tức cơ chế nào bảo đảm mọi thay đổi hợp lệ cuối cùng được xét; **duy nhất** tức bản trùng được nhận dạng và chọn thắng xác định ra sao; **luỹ đẳng** tức cùng đầu vào và điểm kiểm tra chạy lại cho trạng thái tương đương thế nào; **xoá** tức bản ghi bị xoá ở nguồn được phản ánh hay cố ý giữ, và trong bao lâu; **thứ tự** tức thời gian nào quyết định bản mới nhất và quy tắc phá hoà là gì; **nguyên tử** tức bên đọc có thể thấy kết quả nửa vời không và ranh giới ở đâu; **phục hồi** tức hỏng ở mỗi ranh giới dẫn tới thao tác nào. Quy tắc chốt của bài: điều kiện lọc theo mốc lớn nhất không được chấp nhận nếu chưa chứng minh xong đồng hồ, cập nhật muộn, giá trị mốc bằng nhau, xoá, và hành vi khi đích rỗng.

**Outcome.** Viết chứng minh bảy phần cho ba mô hình tăng dần, mỗi phần kèm một phép kiểm chạy được.

**Đánh giá.** Tầng *đánh giá*. Objective là một nghĩa vụ chứng minh, nên tiêu chí là tính đầy đủ và kiểm được của lập luận. Kiểm bằng rà soát chéo; đạt khi ba mô hình có đủ bảy phần và mỗi phần dẫn tới một phép kiểm tự động chứ dừng ở lời văn.

**Lab.** Với ba mô hình tăng dần đã cài, viết chứng minh bảy phần cho từng cái. Với mỗi phần, viết một phép kiểm tự động tương ứng và đưa vào bộ kiểm. Đổi bài chéo: người khác đọc chứng minh và tìm một giả định chưa được kiểm. Sửa theo phản hồi.

**Pitfalls.** Viết chứng minh bằng lời mà không có phép kiểm · bỏ phần xoá vì nguồn hiện chưa xoá · bỏ phần phục hồi vì chưa từng hỏng · chấp nhận điều kiện lọc theo mốc mà chưa chứng minh năm giả định.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba mô hình có đủ bảy phần, mỗi phần dẫn tới một phép kiểm tự động, và rà soát chéo không tìm thấy giả định chưa kiểm.

### Lesson 262 · The incremental failure matrix `TH`
**Prerequisites.** Lesson 261

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài kiểm chứng phần chứng minh ở bài trước bằng thực nghiệm, vì lập luận đúng trên giấy vẫn có thể sai khi chạy. Sáu chế độ hỏng bắt buộc cùng hành vi kỳ vọng của từng cái: tiến trình chết trước khi chốt thì đích không được ở trạng thái nửa vời hoặc chạy lại phải sửa được; chết sau khi chốt nhưng trước khi ghi điểm kiểm tra thì chạy lại không được trùng; bản ghi nguồn cập nhật muộn thì cửa sổ chồng lấn hoặc cơ chế bắt thay đổi phải bắt được; nguồn xoá bản ghi thì chính sách phải rõ chứ mặc định bỏ qua; hai bản ghi cùng khoá thì có bản thắng xác định hoặc đi cách ly; lược đồ thêm, bớt hoặc đổi kiểu thì hợp đồng và đường di trú phải phản ứng. **Hành vi kỳ vọng viết trước khi chạy thí nghiệm.** Mỗi ô của ma trận là một phép thử tự động, để hồi quy được phát hiện ở lần nộp mã sau.

**Outcome.** Chạy trọn sáu chế độ hỏng cho ba mô hình và chứng minh hành vi khớp kỳ vọng đã viết trước.

**Đánh giá.** Tầng *áp dụng*. Objective là tiêu chí ra của module, nên nghiệm thu là toàn bộ ma trận đạt. Kiểm bằng ma trận sáu nhân ba; đạt khi mọi ô có kết quả khớp hành vi kỳ vọng và cả sáu chế độ chạy được tự động.

**Lab.** Viết hành vi kỳ vọng cho sáu chế độ hỏng trước khi chạy. Với ba mô hình tăng dần, tái hiện từng chế độ hỏng và ghi lại kết quả thật. Đối soát đích với nguồn sau mỗi lần phục hồi. Chuyển sáu phép thử thành phép thử tự động chạy trong tích hợp liên tục. Sửa mọi ô không khớp kỳ vọng.

**Pitfalls.** Viết hành vi kỳ vọng sau khi thấy kết quả · nạp lại toàn bộ để chữa ô không khớp thay vì tìm nguyên nhân · bỏ chế độ xoá vì nguồn chưa xoá · chạy ma trận bằng tay một lần rồi thôi.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Toàn bộ 18 ô khớp hành vi kỳ vọng viết trước, và sáu phép thử chạy được tự động trong tích hợp liên tục.

### Lesson 263 · Snapshots and SCD2 invariants `TH`
**Prerequisites.** Lesson 262

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Cơ chế ghi lịch sử thay đổi của một bảng nguồn, và nó là cách cài chiều biến đổi chậm loại hai ở lesson 157 bằng công cụ. Hai chiến lược phát hiện thay đổi: theo dấu thời gian cập nhật, rẻ và đòi trường đó tin cậy; theo so sánh cột, đắt hơn và dùng khi nguồn không có dấu thời gian tin cậy. Hành vi khi bản ghi biến mất khỏi nguồn phải chọn tường minh chứ để mặc định. Ba bất biến bắt buộc kiểm, lấy thẳng từ lesson 157: mỗi khoá nghiệp vụ có đúng một dòng hiện hành; không có khoảng hiệu lực chồng nhau; và mọi khoảng có thời điểm bắt đầu trước thời điểm kết thúc. Hiệu chỉnh tới muộn là ca khó: một thay đổi được biết sau khi đã ghi thay đổi sau nó, nên phải chèn vào giữa chuỗi. **Cơ chế này không thay được mọi ca dùng bắt thay đổi từ nhật ký**: nó chỉ thấy trạng thái tại thời điểm chạy, nên thay đổi xảy ra giữa hai lần chạy bị bỏ sót.

**Outcome.** Cài ghi lịch sử đạt ba bất biến và chỉ ra ca dùng mà cơ chế này không đủ.

**Đánh giá.** Tầng *áp dụng*. Objective có ba bất biến kiểm được cộng một giới hạn phải nhận ra. Kiểm bằng ba phép kiểm bất biến cộng thí nghiệm bỏ sót; đạt khi ba bất biến giữ qua 500 lần cập nhật và ca bỏ sót được định lượng.

**Lab.** Cài ghi lịch sử cho một bảng nguồn bằng cả hai chiến lược phát hiện. Chạy 500 lần cập nhật gồm cả hiệu chỉnh tới muộn. Kiểm ba bất biến sau mỗi chu kỳ. Tạo một kịch bản có hai thay đổi giữa hai lần chạy và đếm số thay đổi bị bỏ sót. Chọn tường minh hành vi khi bản ghi biến mất khỏi nguồn.

**Pitfalls.** Để hành vi khi bản ghi biến mất theo giá trị mặc định · dùng chiến lược theo dấu thời gian khi trường đó không tin cậy · không kiểm bất biến chồng lấn · coi cơ chế này thay được bắt thay đổi từ nhật ký.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba bất biến giữ qua 500 lần cập nhật, và số thay đổi bị bỏ sót giữa hai lần chạy được định lượng.

### Lesson 264 · Model contracts, versions and consumer migration `TH`
**Prerequisites.** Lesson 263

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Mô hình ở tầng phục vụ là hợp đồng, nên đổi nó phải theo quy trình, giống hệt lesson 190 nhưng cưỡng chế bằng công cụ. Hợp đồng mô hình khai báo tên cột, kiểu và ràng buộc; khi mô hình sinh ra sai hợp đồng thì lần xây dựng hỏng ngay thay vì đẩy dữ liệu sai xuống hạ nguồn. Ba mức thay đổi theo lesson 220, và mức phá vỡ cần mô hình có phiên bản: hai phiên bản cùng tồn tại trong một cửa sổ chuyển đổi, bên tiêu thụ chuyển dần, rồi phiên bản cũ bị gỡ. Kiểm kê bên tiêu thụ trước khi đổi là bước bắt buộc và nó dựa vào khai báo bên tiêu thụ cùng nhật ký truy vấn. **Đổi lược đồ phá vỡ mà không có kiểm kê bên tiêu thụ, đường di trú và đường quay lại là một trong những chế độ hỏng tự động chưa đạt của module.** Đổi tên hoặc bỏ cột sao cho bên tiêu thụ cũ và mới cùng sống là bài tập trung tâm.

**Outcome.** Thực hiện một thay đổi phá vỡ có phiên bản, kiểm kê bên tiêu thụ và đường quay lại, không làm hỏng bên nào.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là không bên tiêu thụ nào hỏng suốt quá trình. Kiểm bằng thí nghiệm chuyển đổi có bên tiêu thụ chạy thật; đạt khi không bên nào lỗi và phiên bản cũ chỉ bị gỡ sau khi kiểm kê rỗng.

**Lab.** Khai báo hợp đồng cho ba mô hình phục vụ và chứng minh lần xây dựng hỏng khi mô hình sai hợp đồng. Kiểm kê bên tiêu thụ bằng khai báo cộng nhật ký truy vấn. Thực hiện một lần đổi tên cột theo quy trình có phiên bản với hai bên tiêu thụ chạy thật. Gỡ phiên bản cũ sau khi kiểm kê rỗng. Thực hiện một lần quay lại.

**Pitfalls.** Đổi cột rồi báo bên tiêu thụ sau · gỡ phiên bản cũ theo lịch thay vì theo kiểm kê · không khai báo hợp đồng nên dữ liệu sai chảy xuống hạ nguồn · không có đường quay lại.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Không bên tiêu thụ nào lỗi suốt quá trình, phiên bản cũ chỉ gỡ sau khi kiểm kê rỗng, và đường quay lại thực hiện được.

### Lesson 265 · Documentation, exposures and lineage artifacts `TH`
**Prerequisites.** Lesson 264

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Tài liệu nằm cạnh mã và được rà soát cùng mã, theo đúng nguyên tắc ở lesson 191. Bốn thứ phải khai báo cho mỗi mô hình phục vụ: hạt, chủ sở hữu, ngữ nghĩa từng cột, và cảnh báo diễn giải. Khai báo bên tiêu thụ nối mô hình với bảng điều khiển, báo cáo hoặc hệ hạ nguồn dùng nó; đây là thứ làm kiểm kê ở lesson 264 chạy được, và thiếu nó thì không ai dám đổi gì. Dòng dõi sinh ra từ đồ thị phụ thuộc là dòng dõi kỹ thuật, còn dòng dõi tới quyết định là nội dung lesson 187; cần cả hai và chúng không thay nhau. Kiểm tài liệu trong tích hợp liên tục theo lesson 193: **một mô hình công khai không có tài liệu là một lỗi chặn hợp nhất**, chứ một việc để sau. Ba thứ không nên đưa vào tài liệu vì chúng chắc chắn lạc hậu.

**Outcome.** Khai báo tài liệu và bên tiêu thụ đầy đủ, và chặn được mô hình công khai thiếu tài liệu ở cửa hợp nhất.

**Đánh giá.** Tầng *áp dụng*. Objective là một cửa chặn tự động có tiêu chí nghiệm thu bằng phép thử tiêm. Kiểm bằng ba vi phạm tiêm; đạt khi cả ba bị chặn và đồ thị dòng dõi phủ đủ bên tiêu thụ đã khai báo.

**Lab.** Khai báo bốn thứ cho mọi mô hình phục vụ và khai báo bên tiêu thụ cho từng cái. Sinh tài liệu và đồ thị dòng dõi. Viết phép kiểm chặn mô hình công khai thiếu tài liệu, thiếu chủ sở hữu, hoặc thiếu khai báo hạt. Tiêm ba vi phạm và xác nhận bị chặn. Dùng dòng dõi để trả lời câu một cột nguồn đổi thì bảng điều khiển nào ảnh hưởng.

**Pitfalls.** Viết tài liệu trong trang riêng ngoài kho mã · bỏ khai báo bên tiêu thụ nên không kiểm kê được · coi dòng dõi kỹ thuật là đủ · để mô hình công khai không tài liệu qua cửa hợp nhất.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba vi phạm bị chặn ở cửa hợp nhất, và dòng dõi trả lời được câu hỏi ảnh hưởng từ một cột nguồn tới bảng điều khiển.

### Lesson 266 · dbt artifacts - manifest, run results and catalog `TH`
**Prerequisites.** Lesson 265

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba tệp hiện vật là nơi công cụ ghi lại mọi thứ nó biết, và đọc được chúng là điều kiện để gỡ lỗi cùng để dựng tích hợp liên tục thông minh. Tệp kê khai chứa toàn bộ nút, phụ thuộc, cấu hình, tổng kiểm tra và siêu dữ liệu; nó là đầu vào cho việc so sánh trạng thái giữa hai lần chạy. Tệp kết quả chạy chứa trạng thái, thời gian và phản hồi của kho dữ liệu cho từng nút; nó là bằng chứng vận hành và cũng có giới hạn, chẳng hạn nó nói nút chạy xong chứ không nói dữ liệu đúng. Tệp danh mục chứa thông tin cột lấy từ kho dữ liệu. **Phân biệt việc điều phối báo thành công với việc dữ liệu đúng là một câu hỏi bắt buộc của module**, và ba hiện vật này giúp thấy rõ ranh giới đó. Giữ hiện vật của lần chạy sản xuất là điều kiện để so sánh trạng thái, nên nó cần nơi lưu và chính sách giữ.

**Outcome.** Đọc ba hiện vật để trả lời năm câu hỏi vận hành, gồm câu phân biệt chạy xong với dữ liệu đúng.

**Đánh giá.** Tầng *phân tích*. Objective đòi lấy bằng chứng từ hiện vật thay vì từ giao diện. Kiểm bằng năm câu hỏi; đạt khi trả lời đúng ít nhất bốn chỉ bằng ba tệp hiện vật.

**Lab.** Chạy dự án và thu ba hiện vật. Trả lời năm câu hỏi chỉ bằng chúng: mô hình nào chậm nhất, mô hình nào đổi so với lần chạy trước, mô hình nào không ai dùng, phép kiểm nào cảnh báo mà không chặn, và một nút báo thành công thì điều đó chứng minh gì về dữ liệu. Thiết lập nơi lưu hiện vật của lần chạy sản xuất.

**Pitfalls.** Đọc trạng thái từ giao diện thay vì hiện vật · coi mọi nút xanh là dữ liệu đúng · không lưu hiện vật sản xuất nên không so sánh trạng thái được · tin tệp danh mục luôn cập nhật.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Trả lời đúng ≥ 4/5 câu hỏi chỉ bằng ba hiện vật, và nơi lưu hiện vật sản xuất được thiết lập kèm chính sách giữ.

### Lesson 267 · Selection grammar and state-aware CI `TH`
**Prerequisites.** Lesson 266

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Cú pháp chọn nút quyết định lần chạy nào động tới cái gì, và hiểu sai nó làm tích hợp liên tục vừa chậm vừa bỏ sót. Toán tử đồ thị chọn nút cùng thượng lưu và hạ lưu; nhãn và nhóm chọn theo phân loại; chọn theo trạng thái so tệp kê khai hiện tại với tệp kê khai tham chiếu để tìm nút đã đổi. **Luôn xem danh sách nút được chọn trước khi chạy ở môi trường sản xuất**, vì một biểu thức chọn sai có thể dựng lại toàn bộ hoặc bỏ qua phần quan trọng. Tích hợp liên tục chỉ dựng phần đổi cộng hạ lưu là cách tiết kiệm chính, nhưng nó dựa vào tệp kê khai tham chiếu, nên quyền giữ và tính đúng của tệp đó là điểm yếu: tham chiếu sai môi trường làm phép so cho kết quả sai. Quy tắc bù: **vẫn phải có một lần kiểm đầy đủ theo lịch**, vì chỉ dựng phần đổi không phát hiện được lỗi do dữ liệu. Cách ly môi trường và quyền tối thiểu.

**Outcome.** Dựng tích hợp liên tục chỉ dựng phần đổi cộng hạ lưu, và chứng minh nó không bỏ sót nhờ một lần kiểm đầy đủ theo lịch.

**Đánh giá.** Tầng *áp dụng*. Objective có hai ràng buộc: nhanh và không bỏ sót. Kiểm bằng ba thay đổi tiêm; đạt khi tập nút được chọn khớp tập đúng ở cả ba và lần kiểm đầy đủ bắt được một lỗi do dữ liệu mà lần chạy phần đổi bỏ qua.

**Lab.** Dựng tích hợp liên tục dùng chọn theo trạng thái với tệp kê khai tham chiếu từ lần chạy sản xuất. Tiêm ba thay đổi ở ba vị trí trong đồ thị và so tập nút được chọn với tập đúng tính bằng tay. Tạo một lỗi chỉ lộ ra do dữ liệu mới chứ do mã đổi, và chứng minh lần kiểm đầy đủ theo lịch bắt được. Thử tham chiếu sai môi trường và ghi lại hậu quả.

**Pitfalls.** Chạy biểu thức chọn ở sản xuất mà không xem danh sách nút · bỏ lần kiểm đầy đủ vì đã có chọn theo trạng thái · lấy tệp kê khai tham chiếu từ môi trường phát triển · dùng thông tin xác thực sản xuất trong tích hợp liên tục.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tập nút được chọn khớp tập đúng ở cả ba thay đổi, và lần kiểm đầy đủ theo lịch bắt được lỗi do dữ liệu.

### Lesson 268 · dbt performance and cost per model `TH`
**Prerequisites.** Lesson 267

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hiệu năng của một dự án biến đổi có hai phần tách biệt: đường găng của đồ thị và chi phí của từng mô hình. Đường găng là chuỗi phụ thuộc dài nhất; rút ngắn nó là việc tái cấu trúc đồ thị chứ tối ưu truy vấn. **Tăng số luồng không tăng tốc quá mức đồng thời mà kho dữ liệu cho phép**, và vượt ngưỡng đó thì thời gian chờ hàng đợi cùng tràn đĩa tăng, nên nhiều luồng hơn có thể làm chậm hơn và đắt hơn, đúng hiện tượng ở lesson 214. Với từng mô hình, đo số dòng vào ra, số byte quét, mức tràn đĩa và chi phí; đọc kế hoạch theo lesson 130 và 206. Quét toàn bộ âm thầm trong một mô hình tăng dần là lỗi tốn kém hay gặp: mô hình chạy đúng nhưng quét cả bảng mỗi lần. Chi phí trên mỗi đơn vị gồm chi phí mỗi lần làm mới và chi phí mỗi dòng nguồn.

**Outcome.** Rút ngắn đường găng và giảm chi phí ba mô hình, giải thích bằng kế hoạch chứ bằng phỏng đoán.

**Đánh giá.** Tầng *đánh giá*. Objective đòi tách hai nguyên nhân chậm và chống việc tăng luồng theo phản xạ. Kiểm bằng cặp số đo trước sau; đạt khi đường găng ngắn lại và ba mô hình giảm chi phí với kế hoạch giải thích được, mà kết quả không đổi.

**Lab.** Vẽ đồ thị và xác định đường găng, đo thời gian của nó. Tăng số luồng qua bốn mức và vẽ quan hệ giữa số luồng với tổng thời gian cùng chi phí, chỉ ra điểm tăng luồng bắt đầu phản tác dụng. Chọn ba mô hình tốn nhất, đọc kế hoạch, tìm quét toàn bộ âm thầm và sửa. Đối soát kết quả trước sau.

**Pitfalls.** Tăng số luồng để chữa đồ thị có đường găng dài · tối ưu mô hình rẻ vì dễ · sửa mà không đối soát kết quả · không phát hiện quét toàn bộ trong mô hình tăng dần.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đường găng ngắn lại có số đo, ba mô hình giảm chi phí với kế hoạch giải thích, và kết quả đối soát không đổi.

### Lesson 269 · Orchestration primitives before the tool `LT`
**Prerequisites.** Lesson 268

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài mở phần điều phối bằng những khái niệm chung cho mọi công cụ, học một lần rồi mới chọn. Đồ thị phụ thuộc và phân biệt phụ thuộc dữ liệu với thứ tự chạy: hai việc chạy nối nhau không có nghĩa việc sau cần dữ liệu của việc trước, và nhầm hai thứ này tạo ra đồ thị cứng nhắc không song song được. Kỳ dữ liệu và phân vùng: một lần chạy xử lý một khoảng dữ liệu, và khoảng đó khác thời điểm chạy. Vòng đời một lần chạy từ lúc được lập lịch tới lúc kết thúc. Thử lại, hết giờ và huỷ; ranh giới tác dụng phụ. Đồng thời, hàng đợi và mức ưu tiên. Nạp bù và quan sát ở mức phân vùng. Vòng đời bí mật và tài nguyên. **Phụ thuộc vào thời gian thay vì vào tín hiệu dữ liệu sẵn sàng là lỗi thiết kế phổ biến nhất**: chạy lúc hai giờ sáng vì tin rằng nguồn xong lúc một giờ là một giả định không được kiểm.

**Outcome.** Phân biệt phụ thuộc dữ liệu với thứ tự chạy trong một đồ thị cho trước và thay giả định thời gian bằng tín hiệu.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết đặt từ vựng chung trước khi chọn công cụ. Kiểm bằng bài phân tích một đồ thị; đạt khi phân đúng ít nhất sáu trong tám cạnh và mọi giả định thời gian được thay bằng tín hiệu dữ liệu.

**Lab.** Cho một đồ thị tám cạnh trong đó vài cạnh chỉ là thứ tự chạy chứ phụ thuộc dữ liệu. Phân loại từng cạnh và vẽ lại đồ thị chỉ giữ phụ thuộc dữ liệu; đo mức song song tăng thêm. Tìm mọi chỗ đang giả định nguồn xong theo giờ và thay bằng một tín hiệu dữ liệu sẵn sàng.

**Pitfalls.** Nối các việc theo thứ tự thuận tiện rồi gọi đó là phụ thuộc · lập lịch theo giờ dựa trên niềm tin nguồn đã xong · nhầm kỳ dữ liệu với thời điểm chạy · để tác dụng phụ ngoài ranh giới việc.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân đúng ≥ 6/8 cạnh, mức song song tăng thêm được đo, và mọi giả định thời gian được thay bằng tín hiệu dữ liệu.

### Lesson 270 · Logical date, data interval and the timezone traps `TH`
**Prerequisites.** Lesson 269

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Khái niệm khó nhất của phần điều phối và là nguồn của lỗi nạp bù im lặng. Một lần chạy gắn với một khoảng dữ liệu, và khoảng đó thường kết thúc tại thời điểm lần chạy được kích hoạt chứ bắt đầu tại đó; hiểu ngược làm mọi phân vùng lệch một kỳ. Dùng thời điểm hiện tại trong mã xử lý là lỗi chí mạng: khi nạp bù, thời điểm hiện tại là hôm nay chứ ngày của phân vùng, nên **nạp bù ghi cùng một dữ liệu hôm nay vào mọi phân vùng lịch sử**, và kết quả trông có vẻ chạy xong. Múi giờ và giờ mùa hè: ở những múi giờ có áp dụng giờ mùa hè, mỗi lần chuyển làm một ngày có 23 hoặc 25 giờ, nên lịch chạy hằng giờ có kỳ lặp hoặc kỳ thiếu. Số lần chuyển trong năm và ngày chuyển do quy định của từng vùng đặt ra và có thể đổi, nên lịch phải tra từ cơ sở dữ liệu múi giờ chứ gán cứng; chọn múi giờ chuẩn cho lịch và quy đổi ở biên là cách tránh. Chạy bù tự động cho khoảng quá khứ và rủi ro tạo hàng nghìn lần chạy cùng lúc.

**Outcome.** Tái hiện lỗi dùng thời điểm hiện tại khi nạp bù và cài lịch chịu được chuyển giờ mùa hè.

**Đánh giá.** Tầng *phân tích*. Objective đòi nhận ra một lỗi làm mọi lần chạy đều báo thành công. Kiểm bằng nạp bù 30 phân vùng cộng thí nghiệm chuyển giờ; đạt khi lỗi được tái hiện và định lượng, bản sửa cho dữ liệu đúng theo từng phân vùng, và lịch không có kỳ lặp hay kỳ thiếu.

**Lab.** Viết một việc cố ý dùng thời điểm hiện tại. Nạp bù 30 phân vùng và chứng minh mọi phân vùng chứa cùng dữ liệu dù mọi lần chạy đều thành công. Sửa bằng cách dùng khoảng dữ liệu của lần chạy và đối soát lại. Cài một lịch hằng giờ và chạy qua hai lần chuyển giờ mùa hè, đếm số kỳ lặp và kỳ thiếu.

**Pitfalls.** Dùng thời điểm hiện tại trong mã xử lý · nhầm thời điểm kích hoạt với khoảng dữ liệu · bật chạy bù tự động cho khoảng quá khứ dài mà không giới hạn đồng thời · đặt lịch theo giờ địa phương có giờ mùa hè.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Lỗi dùng thời điểm hiện tại được tái hiện và định lượng, bản sửa cho dữ liệu đúng theo từng phân vùng, và lịch qua hai lần chuyển giờ không có kỳ lặp hay kỳ thiếu.

### Lesson 271 · Mastering one orchestrator - Airflow or Dagster `TH`
**Prerequisites.** Lesson 270

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài áp quy tắc chọn công cụ của module: thành thạo bộ điều phối mà nơi làm việc dùng, bộ còn lại chỉ tới mức hiểu kiến trúc. Với bộ điều phối theo việc: các thành phần gồm bộ xử lý tệp định nghĩa, bộ lập lịch, cơ sở dữ liệu siêu dữ liệu, giao diện, bộ thực thi và tiến trình chạy; vòng đời một thể hiện việc; cơ sở dữ liệu siêu dữ liệu là phụ thuộc vận hành thật; kênh truyền giá trị giữa các việc **chỉ dành cho siêu dữ liệu nhỏ, không phải nơi chuyển dữ liệu**. Với bộ điều phối theo tài sản: khoá tài sản, sự kiện hiện thực hoá, phân vùng như lát cắt độc lập, tài nguyên và bộ quản lý vào ra tách phần lưu trữ khỏi logic, phép kiểm tài sản. Điểm chung phải nắm ở cả hai: ranh giới giữa mặt điều khiển với mặt dữ liệu, và **không đặt xử lý dữ liệu nặng trong tiến trình lập lịch**. Tích hợp với dbt và nguyên tắc chỉ một nguồn sự thật về điều phối.

**Outcome.** Dựng một đồ thị chạy được trên bộ điều phối đã chọn, đúng ranh giới mặt điều khiển và mặt dữ liệu.

**Đánh giá.** Tầng *áp dụng*. Objective là năng lực dựng trên một công cụ tới mức vận hành. Kiểm bằng rà soát kiến trúc cộng phép thử tải; đạt khi không có xử lý dữ liệu nặng trong mặt điều khiển và đồ thị chạy đúng với dữ liệu thật.

**Lab.** Dựng đồ thị điều phối cho đường dẫn đã có ở M14B và dbt, trên bộ điều phối đã chọn. Chứng minh mọi xử lý nặng chạy ở hệ ngoài chứ trong tiến trình lập lịch. Đo mức tăng của cơ sở dữ liệu siêu dữ liệu hoặc nhật ký sự kiện sau 100 lần chạy. Cố ý truyền một tập dữ liệu lớn qua kênh siêu dữ liệu và ghi lại hậu quả.

**Pitfalls.** Học hai bộ điều phối cùng lúc tới mức sản xuất · chạy phép biến đổi nặng trong tiến trình lập lịch · truyền dữ liệu qua kênh siêu dữ liệu · để hai nguồn sự thật về điều phối giữa dbt và bộ điều phối.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đồ thị chạy đúng với dữ liệu thật, không có xử lý nặng trong mặt điều khiển, và mức tăng siêu dữ liệu sau 100 lần chạy được đo.

### Lesson 272 · Retry, concurrency, pools and the side-effect boundary `TH`
**Prerequisites.** Lesson 271

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Cơ chế tin cậy của bộ điều phối và giới hạn của chúng. Mỗi việc phải là một giao dịch: luỹ đẳng, công bố nguyên tử, đọc ghi đúng phân vùng của nó. Thử lại, hết giờ và cam kết thời hạn; việc mồ côi và nhịp tim. Bộ cảm biến chờ theo kiểu giữ tiến trình so với kiểu nhả tiến trình: kiểu giữ làm cạn tiến trình chạy khi có nhiều bộ cảm biến, và đây là chế độ hỏng đặc trưng. Hàng đợi, mức ưu tiên và số lần chạy đồng thời tối đa dùng để **cách ly nạp bù khỏi lần chạy hằng ngày**, quy tắc đã đặt ở lesson 252 và nay được cưỡng chế bằng cấu hình. Cơn bão thử lại và cách chặn. Điểm quan trọng nhất và là một câu hỏi bắt buộc của module: thử lại của bộ điều phối có thể nhân đôi tác dụng phụ dù trạng thái cuối của việc là thành công, nên **trạng thái việc không chứng minh được hiệu ứng ở đích**.

**Outcome.** Cấu hình hàng đợi và đồng thời để cách ly nạp bù, và chứng minh thử lại không nhân đôi tác dụng phụ.

**Đánh giá.** Tầng *áp dụng*. Objective có hai tiêu chí: cách ly đạt và tác dụng phụ không nhân đôi. Kiểm bằng thí nghiệm chạy chung; đạt khi nạp bù không làm vỡ cam kết hằng ngày và đối soát chứng minh không có tác dụng phụ trùng.

**Lab.** Cấu hình hàng đợi riêng cho nạp bù với giới hạn đồng thời. Chạy nạp bù 90 phân vùng song song với lịch hằng ngày và đo độ tươi hằng ngày. Tạo một việc có tác dụng phụ ra ngoài, làm phản hồi thất lạc để bộ điều phối thử lại, và đối soát xem tác dụng phụ có nhân đôi. Dựng 50 bộ cảm biến kiểu giữ tiến trình và quan sát cạn tiến trình, rồi chuyển sang kiểu nhả.

**Pitfalls.** Chạy nạp bù trong hàng đợi chung không giới hạn · dùng bộ cảm biến kiểu giữ tiến trình ở quy mô lớn · coi trạng thái việc thành công là bằng chứng hiệu ứng đúng · thử lại việc có tác dụng phụ không luỹ đẳng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Cam kết hằng ngày giữ được suốt nạp bù, đối soát chứng minh không có tác dụng phụ trùng, và chuyển kiểu bộ cảm biến làm hết cạn tiến trình.

### Lesson 273 · Control-plane diagnosis - the required incident list `TH`
**Prerequisites.** Lesson 272

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài chẩn đoán ở tầng mặt điều khiển, chạy theo đường truy vết chứ đoán. Đường truy vết chung ba chặng: từ tệp định nghĩa tới biểu diễn đã lưu trong siêu dữ liệu; từ bộ lập lịch tới việc được xếp hàng; và từ tiến trình chạy tới trạng thái cùng nhật ký cuối. Sáu sự cố bắt buộc diễn tập, và mỗi cái có một triệu chứng đặc trưng: thông lượng lập lịch sụp vì phân tích tệp định nghĩa quá nặng; cơ sở dữ liệu siêu dữ liệu hoặc nhật ký sự kiện bị nghẽn kết nối; việc kẹt ở trạng thái đã xếp hàng; việc mồ côi sau khi tiến trình chạy chết; bộ cảm biến làm cạn tiến trình; và nạp bù làm bão hoà nguồn. Với bộ điều phối theo tài sản, thêm ba ca: con trỏ của bộ cảm biến phát lại, tải lại định nghĩa thất bại, và ánh xạ phân vùng bỏ sót dữ liệu. **Truy vấn bảng siêu dữ liệu chỉ để chẩn đoán và chỉ đọc**; ứng dụng phải dùng giao diện ổn định.

**Outcome.** Chẩn đoán sáu sự cố mặt điều khiển bằng đường truy vết và sửa được ít nhất bốn với số đo.

**Đánh giá.** Tầng *phân tích*. Objective đòi chẩn đoán có phương pháp trong một hệ nhiều thành phần. Kiểm bằng sáu sự cố tái hiện; đạt khi truy đúng chặng gây ra ở ít nhất năm và sửa được ít nhất bốn với số đo trước sau.

**Lab.** Tái hiện sáu sự cố trên hệ đã dựng. Với mỗi cái, chạy đường truy vết ba chặng và ghi lại bằng chứng ở mỗi chặng. Sửa và đo lại. Với sự cố phân tích tệp định nghĩa, đo thời gian phân tích trước và sau khi giảm số tệp hoặc bỏ mã chạy lúc phân tích. Ghi mỗi sự cố thành một mục trong sổ tay vận hành.

**Pitfalls.** Đoán nguyên nhân từ triệu chứng mà không truy vết · sửa bằng cách khởi động lại rồi coi là xong · cho ứng dụng ghi thẳng vào bảng siêu dữ liệu · không ghi sự cố vào sổ tay.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Truy đúng chặng gây ra ở ≥ 5/6 sự cố, ≥ 4 sự cố được sửa với số đo trước sau, và mỗi sự cố có một mục trong sổ tay.

### Lesson 274 · Pipeline capstone - daily, backfill and full rebuild `DA`
**Prerequisites.** Lesson 273

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Bài dự án tổng hợp module, lấy đúng yêu cầu capstone của hợp đồng nguồn. Một đường dẫn hoàn chỉnh từ cơ sở dữ liệu quan hệ và giao diện lập trình, qua vùng thô bất biến, qua ba tầng mô hình, tới engine phân tích, có kiểm chất lượng và đối soát. Điều phối bằng bộ điều phối đã chọn. Ba chế độ phải chạy được: tăng dần hằng ngày, nạp bù theo yêu cầu, và dựng lại toàn bộ. Kiểm soát bắt buộc: hợp đồng lược đồ, dữ liệu tới muộn, xoá, khử trùng, và đối soát từ nguồn tới đích. Phần sản xuất gồm đóng gói, tích hợp liên tục, quản lý bí mật, nhật ký cùng số đo, cảnh báo, cam kết dịch vụ, sổ tay vận hành và ghi chú chi phí. Bài toán năng lực đi kèm: với 2.000 mô hình, 400 luồng công việc, cam kết 30 phút và 180 ngày nạp bù, xác định đường găng, vùng đồng thời an toàn, ngưỡng dừng và trần chi phí. **Mọi việc xanh không chứng minh dữ liệu đầy đủ**, nên nghiệm thu là đối soát.

**Outcome.** Nộp đường dẫn chạy được cả ba chế độ, với đối soát chứng minh tính đầy đủ và một kế hoạch năng lực có số.

**Đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module. Kiểm bằng đối soát cộng diễn tập sự cố; đạt khi đối soát đạt ở cả ba chế độ, sáu tình huống diễn tập phục hồi được, và kế hoạch năng lực có ngưỡng dừng cùng trần chi phí.

**Lab.** Dựng đường dẫn đầy đủ. Chạy ba chế độ và đối soát từng cái. Diễn tập sáu tình huống: giết tiến trình chạy, nguồn chậm, lược đồ đổi phá vỡ, đầu vào trùng, hiệu chỉnh tới muộn, và một lần triển khai hỏng. Giải bài toán năng lực với số cụ thể cho đường găng, vùng đồng thời, ngưỡng dừng và trần chi phí. Nộp sổ tay vận hành cùng ghi chú chi phí.

**Pitfalls.** Coi mọi việc xanh là bằng chứng đầy đủ · nạp lại toàn bộ để chữa lỗi tăng dần · tắt phép kiểm để đường dẫn xanh · bỏ bài toán năng lực vì chưa gặp quy mô đó.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Đối soát đạt ở cả ba chế độ, sáu tình huống diễn tập đều phục hồi với đối soát khớp, và kế hoạch năng lực có số cho cả bốn hạng mục.

# MODULE M14C · DATA QUALITY AND DATA RELIABILITY ENGINEERING

**Phase 7 · Lessons 275–292 · 36 giờ**

| | |
|---|---|
| **Objective cấp module** | Biến câu dữ liệu đúng thành hợp đồng, bất biến, cam kết dịch vụ, chốt kiểm soát và một vòng đời sự cố có phục hồi |
| **Tiền đề** | M9 · M10 · M11 · M14B · M14 |
| **Exit criterion** | Kế hoạch kiểm soát theo tầng có chủ sở hữu, mức nghiêm trọng, hành động và đường phục hồi cho mọi tài sản trọng yếu; hai sự cố được sửa, đối soát và ghi lại |
| **Kỹ năng SFIA** | `DTAN` mức 5 · `USUP` mức 4 |
| **Chế độ hỏng** | Dùng số lượng phép kiểm làm bằng chứng độ phủ mà không ánh xạ với rủi ro, và chọn ngưỡng sao cho bảng theo dõi luôn xanh |

**Module bù năng lực Analytics Engineer thứ ba.** Nó sở hữu tính đúng, tính đầy đủ và tính kịp thời của dữ liệu, cùng toàn bộ vòng đời sự cố dữ liệu.

Ranh giới lấy từ hợp đồng nguồn: sửa lỗi ở khâu nạp thuộc M14B, sửa lỗi mô hình thuộc M11 và M14, còn nền tảng quan sát và bảo mật đi tiếp ở M21.

Hai nhầm lẫn bị bác bỏ ngay từ bài đầu và được kiểm lại ở cổng: **nhiều phép kiểm không đồng nghĩa với dữ liệu đáng tin**, và **tính chính xác thường không chứng minh được chỉ từ dữ liệu ở đích**.

### Lesson 275 · Quality dimensions defined operationally `LT`
**Prerequisites.** Module 14C: M14

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài mở module bằng việc đổi bảy tính từ mơ hồ thành bảy định nghĩa quan sát được, vì không quan sát được thì không kiểm được. Đầy đủ: đủ bản ghi và đủ trường đã kỳ vọng cho một phân vùng. Hợp lệ: đúng miền giá trị, kiểu, khoảng và định dạng. Duy nhất: một thực thể hoặc sự kiện xuất hiện đúng số lần quy định. Nhất quán: các biểu diễn tuân thủ quy tắc xuyên hệ. Kịp thời: sẵn sàng trước một thời điểm nghiệp vụ. Toàn vẹn: quan hệ và chuyển trạng thái được giữ. Chính xác: giá trị khớp thực tế đáng tin cậy, và đây là chiều khác hẳn sáu chiều kia. **Tính chính xác thường không chứng minh được chỉ từ dữ liệu ở đích**, vì đích không biết thế giới thật; muốn chứng minh phải có một nguồn có thẩm quyền để đối chiếu, còn không thì phải nói rõ đang dùng một đại lượng thay thế. Phân biệt hợp lệ với chính xác bằng ví dụ: một số tiền đúng định dạng và đúng khoảng vẫn có thể sai.

**Outcome.** Chuyển bảy chiều thành định nghĩa quan sát được cho một tài sản thật và chỉ ra chiều nào không tự kiểm được.

**Đánh giá.** Tầng *hiểu*. Bài mở module, đặt từ vựng và đặt một giới hạn nhận thức. Kiểm bằng bài định nghĩa bảy chiều; đạt khi mỗi chiều có một phép quan sát cụ thể và chiều chính xác được nêu rõ cần nguồn đối chiếu nào.

**Lab.** Với một bảng phục vụ thật, viết định nghĩa quan sát được cho cả bảy chiều, mỗi cái kèm phép đo. Chỉ ra chiều nào cần nguồn có thẩm quyền bên ngoài. Tìm ba ví dụ dữ liệu hợp lệ nhưng không chính xác trong chính dữ liệu của mình. Nếu chưa có nguồn đối chiếu, viết rõ đang dùng đại lượng thay thế nào và giới hạn của nó.

**Pitfalls.** Gọi dữ liệu là chất lượng cao mà không nói theo chiều nào · tuyên bố chính xác dựa trên phép kiểm chạy ở đích · gộp hợp lệ với chính xác · định nghĩa chiều bằng tính từ thay vì bằng phép quan sát.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảy chiều đều có phép quan sát cụ thể, và chiều chính xác được nêu rõ nguồn đối chiếu hoặc nêu rõ đại lượng thay thế cùng giới hạn.

### Lesson 276 · Rule anatomy - seven parts `TH`
**Prerequisites.** Lesson 275

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Một quy tắc chất lượng thiếu phần nào thì hỏng theo một kiểu tương ứng, nên bài này đặt ra bảy phần bắt buộc. Tài sản, trường và phân vùng cùng bối cảnh nghiệp vụ. Bất biến hoặc truy vấn hoặc kỳ vọng thống kê. Ngưỡng, cửa sổ và đường cơ sở. Mức nghiêm trọng và hành động, chọn một trong bốn: cảnh báo, cách ly, chặn, hoặc quay lui. Chủ sở hữu và đường leo thang cùng ảnh hưởng tới bên tiêu thụ. Ngoại lệ có thời hạn và cách khắc phục. Bằng chứng được giữ lại cùng chi phí chạy. Phần thứ tư là phần hay bị bỏ nhất và bỏ nó gây hậu quả cụ thể: **một quy tắc không nói rõ hành động thì khi nó đỏ không ai biết phải chặn hay chỉ ghi nhận**, nên sau vài tuần nó bị tắt. Ngoại lệ phải có ngày hết hạn, nếu không thì danh sách miễn trừ chỉ dài thêm. Sổ đăng ký quy tắc nằm trong kho mã và được rà soát cùng mã.

**Outcome.** Viết sổ đăng ký quy tắc đủ bảy phần cho bốn tầng dữ liệu và chỉ ra hậu quả của từng phần bị thiếu.

**Đánh giá.** Tầng *áp dụng*. Objective là một chuẩn tài liệu có thể rà soát máy móc. Kiểm bằng rà soát sổ đăng ký; đạt khi mọi quy tắc đủ bảy phần và mỗi quy tắc có hành động nằm trong bốn lựa chọn cho phép.

**Lab.** Lập sổ đăng ký cho ít nhất 20 quy tắc phủ bốn tầng. Với mỗi quy tắc, điền đủ bảy phần. Viết một phép kiểm tự động chặn mọi quy tắc thiếu phần bắt buộc. Với ba quy tắc, cố ý bỏ một phần khác nhau và mô tả chế độ hỏng vận hành nó gây ra. Đặt hạn cho mọi ngoại lệ đang có.

**Pitfalls.** Viết quy tắc mà không nói hành động khi đỏ · gán chủ sở hữu là một phòng ban · miễn trừ không có ngày hết hạn · không ghi chi phí chạy nên quy tắc đắt bị tắt lặng lẽ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** 20 quy tắc đủ bảy phần, phép kiểm tự động chặn quy tắc thiếu phần, và mọi ngoại lệ đều có ngày hết hạn.

### Lesson 277 · Layered controls - where each check belongs `LT`
**Prerequisites.** Lesson 276

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Đặt phép kiểm sai tầng vừa tốn vừa bắt muộn, nên bài này ánh xạ từng loại kiểm vào từng tầng. Trước khi nạp: hợp đồng nguồn, lược đồ, khoá, ngữ nghĩa thay đổi, khối lượng và lịch kỳ vọng. Vùng thô: tổng kiểm tra tệp, giải mã được lược đồ, trùng lặp, dữ liệu hỏng hoặc cụt; **giữ lại tải trọng bị từ chối cùng xuất xứ, không bỏ im lặng**. Tầng chuẩn hoá: kiểu, miền giá trị, giá trị rỗng, khử trùng, toàn vẹn tham chiếu, quy tắc thời gian và thứ tự, kèm vùng cách ly có lý do và đường phát lại. Tầng phục vụ: tính duy nhất theo hạt, quan hệ, khoảng hiệu lực của chiều biến đổi chậm, đối soát tổng hợp, bất biến chỉ số và tương thích với tầng ngữ nghĩa. Tầng tiêu thụ: độ tươi, đầy đủ, bảo mật, đối soát giữa bảng điều khiển với chỉ số, và trạng thái suy giảm hiển thị cho người dùng. Nguyên tắc chọn tầng: bắt càng sớm càng rẻ, nhưng bất biến nghiệp vụ chỉ kiểm được ở tầng có đủ ngữ cảnh.

**Outcome.** Ánh xạ 20 phép kiểm vào đúng tầng và giải thích ba phép kiểm không thể đặt sớm hơn.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết đặt bản đồ cho tám bài thực hành sau. Kiểm bằng bài ánh xạ; đạt khi đặt đúng ít nhất 16 và ba ca không đặt sớm được có lý do dựa trên ngữ cảnh cần thiết.

**Lab.** Cho 20 phép kiểm và năm tầng. Ánh xạ từng cái vào tầng rẻ nhất mà nó vẫn bắt được lỗi. Với ba phép kiểm phải đặt muộn, giải thích ngữ cảnh nào chỉ có ở tầng đó. Rà đường dẫn hiện có và tìm mọi chỗ dữ liệu bị bỏ im lặng, rồi chuyển sang cách ly có lý do.

**Pitfalls.** Dồn mọi phép kiểm vào tầng phục vụ · bỏ bản ghi hỏng thay vì cách ly · kiểm bất biến nghiệp vụ ở vùng thô nơi chưa đủ ngữ cảnh · trộn dữ liệu cách ly với dữ liệu đã nhận.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ánh xạ đúng ≥ 16/20 phép kiểm, ba ca đặt muộn có lý do dựa trên ngữ cảnh, và không còn chỗ nào bỏ dữ liệu im lặng.

### Lesson 278 · Schema and contract tests at the boundary `TH`
**Prerequisites.** Lesson 277

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Tầng kiểm rẻ nhất và bắt sớm nhất, chạy ngay tại ranh giới giữa hai hệ. Bốn nhóm: tên và kiểu trường; trường bắt buộc và giá trị mặc định; tương thích giữa phiên bản bên ghi và bên đọc theo ma trận bốn ô ở lesson 220; và ngữ nghĩa khoá cùng cách thay đổi. Hợp đồng bên sản xuất khai báo lược đồ, khoá, ngữ nghĩa thay đổi và xoá, cam kết dịch vụ cùng chủ sở hữu; hợp đồng bên tiêu thụ khai báo hạt, ý nghĩa, độ tươi, mức tương thích cần và yêu cầu bảo mật. Hai hợp đồng gặp nhau ở một điểm và chênh lệch giữa chúng là thứ phải phát hiện trước khi chạy. Chạy phép kiểm hợp đồng ở cả hai phía khi thẩm quyền cho phép: bên sản xuất chạy để biết mình sắp phá vỡ ai, bên tiêu thụ chạy để biết mình đang dựa vào gì. **Miễn trừ phải có chủ sở hữu, lý do, hạn và một biện pháp bù**, nếu không thì nó là một cách tắt phép kiểm có giấy tờ.

**Outcome.** Cài phép kiểm hợp đồng ở cả hai phía và chặn được một thay đổi phá vỡ trước khi nó tới môi trường chạy.

**Đánh giá.** Tầng *áp dụng*. Objective là một cửa chặn hai phía có tiêu chí nghiệm thu bằng phép thử tiêm. Kiểm bằng ba thay đổi phá vỡ; đạt khi cả ba bị chặn ở phía sản xuất và mọi miễn trừ đang có đều đủ bốn phần.

**Lab.** Viết hợp đồng bên sản xuất và bên tiêu thụ cho hai tài sản. Cài phép kiểm hợp đồng chạy ở cả hai phía trong tích hợp liên tục. Tiêm ba thay đổi phá vỡ khác loại và xác nhận bị chặn kèm thông báo chỉ rõ bên tiêu thụ nào ảnh hưởng. Rà mọi miễn trừ đang có và bổ sung chủ sở hữu, lý do, hạn cùng biện pháp bù.

**Pitfalls.** Chỉ chạy phép kiểm hợp đồng ở phía tiêu thụ · miễn trừ không có hạn · không liệt kê bên tiêu thụ ảnh hưởng khi chặn · coi lược đồ khớp là hợp đồng được tôn trọng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba thay đổi phá vỡ bị chặn ở phía sản xuất kèm danh sách bên tiêu thụ ảnh hưởng, và mọi miễn trừ đủ bốn phần.

### Lesson 279 · Row, aggregate and relationship tests `TH`
**Prerequisites.** Lesson 278

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba nhóm phép kiểm phủ ba loại lỗi khác nhau, và dùng một nhóm thay cho nhóm khác là nguồn của lỗ hổng. Kiểm theo dòng xét từng bản ghi: miền giá trị, khoảng, mẫu, giá trị rỗng và ràng buộc có điều kiện; nó bắt được bản ghi xấu nhưng **không bắt được lỗi mà mọi dòng đều hợp lệ**. Kiểm tổng hợp xét phân bố theo phân vùng hoặc theo nhóm: số dòng, tổng, và hình dạng phân bố; đây là nhóm duy nhất bắt được lỗi nhân dòng do phép kết, vì từng dòng vẫn hợp lệ còn tổng thì gấp đôi. Kiểm quan hệ xét khoá mồ côi, bản số và phân bổ trong quan hệ nhiều nhiều theo lesson 156. Ví dụ đối chiếu bắt buộc chạy: một phép kết sai làm chỉ số gấp đôi thì kiểm theo dòng xanh hết, chỉ đối soát tổng mới thấy; và một phân vùng thiếu hoàn toàn thì kiểm theo dòng không chạy lần nào nên cũng xanh.

**Outcome.** Chứng minh bằng dữ liệu rằng kiểm theo dòng bỏ sót hai loại lỗi, và bịt chúng bằng hai nhóm còn lại.

**Đánh giá.** Tầng *phân tích*. Objective đòi nhận ra giới hạn của nhóm phép kiểm quen dùng nhất. Kiểm bằng hai lỗi tiêm; đạt khi cả hai lọt qua kiểm theo dòng, bị nhóm khác bắt, và độ phủ được ánh xạ theo loại lỗi chứ theo số lượng.

**Lab.** Cài đủ ba nhóm cho một mô hình phục vụ. Tiêm một phép kết nhân dòng và một phân vùng thiếu. Chứng minh kiểm theo dòng vẫn xanh ở cả hai. Thêm đối soát tổng và kiểm độ đầy đủ theo phân vùng kỳ vọng, rồi xác nhận bắt được. Lập bảng ánh xạ loại lỗi với nhóm phép kiểm bắt được nó.

**Pitfalls.** Coi số lượng phép kiểm là độ phủ · chỉ kiểm theo dòng rồi kết luận dữ liệu sạch · không kiểm phân vùng kỳ vọng nên phân vùng thiếu không ai biết · kiểm quan hệ mà bỏ chiều bản số.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Hai lỗi tiêm lọt qua kiểm theo dòng và bị hai nhóm còn lại bắt, và bảng ánh xạ loại lỗi với nhóm phép kiểm đầy đủ.

### Lesson 280 · Temporal tests - late, out of order and overlap `TH`
**Prerequisites.** Lesson 279

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Nhóm phép kiểm thứ tư, dành riêng cho lỗi về thời gian, vì chúng không lộ ra trong bất kỳ nhóm nào ở bài trước. Bốn loại kiểm: dữ liệu tới muộn vượt cửa sổ đã thoả thuận ở lesson 251; sự kiện tới sai thứ tự so với thời gian sự kiện; khoảng hiệu lực chồng nhau ở chiều biến đổi chậm theo lesson 157; và chuyển trạng thái đi ngược chiều trong một vòng đời. Loại thứ ba và thứ tư là bất biến chứ ngưỡng, nên chúng phải đỏ tuyệt đối chứ có dung sai. Một ca hỏng đặc trưng và bắt buộc tái hiện: **toàn bộ dữ liệu bị dịch múi giờ thì mọi kiểm kiểu và kiểm khoảng đều xanh**, vì giá trị vẫn hợp lệ, chỉ là thuộc sai ngày; cách bắt là một bộ dữ liệu đối chứng có mốc thời gian biết trước cùng một phép kiểm ranh giới ngày. Bộ đối chứng cố định là công cụ chính của nhóm này.

**Outcome.** Cài bốn phép kiểm thời gian và bắt được ca dịch múi giờ mà mọi phép kiểm khác bỏ qua.

**Đánh giá.** Tầng *phân tích*. Objective nhắm vào một lỗi đi qua được toàn bộ phép kiểm thông thường. Kiểm bằng bốn lỗi tiêm gồm ca dịch múi giờ; đạt khi cả bốn bị bắt và hai bất biến không có dung sai.

**Lab.** Cài bốn phép kiểm thời gian. Dựng một bộ đối chứng có mốc thời gian biết trước. Tiêm bốn lỗi: dữ liệu muộn vượt cửa sổ, sự kiện sai thứ tự, khoảng hiệu lực chồng nhau, và toàn bộ dữ liệu bị dịch một múi giờ. Chứng minh ba nhóm phép kiểm ở lesson 279 đều xanh với ca dịch múi giờ, còn phép kiểm ranh giới ngày thì đỏ.

**Pitfalls.** Đặt dung sai cho bất biến khoảng hiệu lực · kiểm thời gian mà không có bộ đối chứng · giả định mốc thời gian nguồn luôn cùng múi giờ · bỏ kiểm chuyển trạng thái ngược chiều vì hiếm.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn lỗi thời gian đều bị bắt, ca dịch múi giờ được chứng minh lọt qua ba nhóm kia, và hai bất biến chạy không dung sai.

### Lesson 281 · Metamorphic and property tests for pipelines `TH`
**Prerequisites.** Lesson 280

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Nhóm phép kiểm không cần biết kết quả đúng là gì, chỉ cần biết quan hệ giữa hai lần chạy phải đúng; nhờ vậy nó kiểm được cả những chỗ không có kết quả kỳ vọng. Bốn quan hệ biến hình dùng được cho đường dẫn dữ liệu: đảo thứ tự bản ghi đầu vào không được đổi kết quả; chia đầu vào thành nhiều phân vùng rồi gộp phải cho cùng kết quả với chạy một lần; chạy lại với cùng đầu vào phải cho trạng thái tương đương, tức chính tính luỹ đẳng ở lesson 250; và nhân đôi một bản ghi phải làm kết quả đổi theo đúng cách đã khai báo chứ tuỳ. Kiểm theo tính chất sinh dữ liệu ngẫu nhiên có ràng buộc rồi khẳng định bất biến, nên nó tìm ra ca biên mà con người không nghĩ tới. **Giá trị lớn nhất của nhóm này là nó bắt lỗi logic thầm lặng**, loại lỗi mà kết quả vẫn hợp lệ và vẫn trông hợp lý.

**Outcome.** Viết bốn phép kiểm biến hình cho một đường dẫn và bắt được một lỗi logic thầm lặng tiêm sẵn.

**Đánh giá.** Tầng *áp dụng*. Objective nhắm vào loại lỗi mà mọi phép kiểm giá trị đều bỏ qua. Kiểm bằng lỗi logic tiêm; đạt khi bốn quan hệ chạy tự động và lỗi tiêm bị ít nhất một quan hệ phát hiện.

**Lab.** Viết bốn phép kiểm biến hình cho một mô hình phục vụ. Viết thêm một phép kiểm theo tính chất sinh 1.000 trường hợp có ràng buộc. Giảng viên sửa một dòng logic biến đổi sao cho kết quả vẫn hợp lệ nhưng sai; chạy toàn bộ phép kiểm và xác định quan hệ nào bắt được. Đo thời gian chạy của nhóm này và đặt lịch phù hợp.

**Pitfalls.** Chỉ kiểm bằng giá trị kỳ vọng cố định · bỏ quan hệ chia rồi gộp vì nghĩ hiển nhiên đúng · sinh dữ liệu ngẫu nhiên không ràng buộc nên toàn ca vô nghĩa · chạy nhóm này ở mỗi lần nộp mã dù nó chậm.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn quan hệ chạy tự động, lỗi logic thầm lặng bị ít nhất một quan hệ phát hiện, và nhóm này có lịch chạy phù hợp thời gian đo được.

### Lesson 282 · Statistical anomaly detection and its cost `TH`
**Prerequisites.** Lesson 281

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phát hiện bất thường bằng thống kê phủ được phần mà quy tắc tất định không phủ, nhưng nó có bản chất khác và phải dùng khác. Bốn yếu tố cấu hình: đường cơ sở, cửa sổ, tính mùa vụ, và cách phân đoạn dữ liệu trước khi so. Thống kê bền vững trước giá trị ngoại lai tốt hơn trung bình và độ lệch chuẩn, vì chính giá trị ngoại lai là thứ ta đang tìm. Nhận biết điểm đổi để phân biệt một thay đổi thật với một bất thường. Đánh đổi trung tâm phải định lượng: ngưỡng chặt cho nhiều báo giả và người trực sẽ bỏ qua cảnh báo, ngưỡng lỏng cho lỗi lọt; nên phải tính độ chính xác và độ phủ chứ chọn ngưỡng theo cảm giác. **Bất thường là tín hiệu để phân loại, không phải bằng chứng dữ liệu sai**, và nhầm điều này biến mọi thay đổi nghiệp vụ hợp lệ thành sự cố. Quy tắc tất định luôn được ưu tiên khi biểu diễn được bằng bất biến.

**Outcome.** Cấu hình phát hiện bất thường cho ba chỉ số với độ chính xác và độ phủ được đo, không dùng nó thay bất biến.

**Đánh giá.** Tầng *đánh giá*. Objective đòi cân hai loại sai lầm và biết ranh giới dùng của phương pháp. Kiểm bằng cặp số độ chính xác với độ phủ; đạt khi cả ba chỉ số có cặp số đo trên dữ liệu lịch sử và không bất biến nào bị thay bằng phát hiện thống kê.

**Lab.** Chọn ba chỉ số có tính mùa vụ khác nhau. Dựng đường cơ sở bằng thống kê bền vững, phân đoạn theo nguồn hoặc theo phân khúc. Chạy trên sáu tháng dữ liệu lịch sử đã gắn nhãn sự cố và sự kiện nghiệp vụ hợp lệ. Tính độ chính xác và độ phủ ở ba mức ngưỡng. Chỉ ra ba chỗ đang định dùng phát hiện thống kê nhưng viết được thành bất biến.

**Pitfalls.** Dùng phát hiện thống kê cho thứ biểu diễn được bằng bất biến · dùng trung bình và độ lệch chuẩn trên dữ liệu có giá trị ngoại lai · bỏ tính mùa vụ nên mỗi thứ hai là một sự cố · coi bất thường là bằng chứng lỗi.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba chỉ số có cặp độ chính xác với độ phủ ở ba mức ngưỡng, và ba trường hợp viết lại được thành bất biến đã được chuyển.

### Lesson 283 · Backtesting rules against known incidents `TH`
**Prerequisites.** Lesson 282

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Một quy tắc chưa chạy lại trên quá khứ là một quy tắc chưa biết có dùng được không, nên bài này đặt ra nghĩa vụ kiểm ngược. Quy trình bốn bước: gắn nhãn một tập lịch sử gồm cả khoảng có sự cố đã biết và khoảng bình thường có thay đổi nghiệp vụ hợp lệ; chạy bộ quy tắc trên toàn bộ tập; đếm bốn ô gồm bắt đúng, bỏ sót, báo giả và im đúng; rồi điều chỉnh ngưỡng cùng phạm vi. Hai kết quả phải xử lý khác nhau: quy tắc bỏ sót một sự cố đã biết là quy tắc chưa phủ rủi ro đó, cần thêm hoặc sửa; quy tắc báo giả ở một thay đổi nghiệp vụ hợp lệ là quy tắc sẽ bị tắt, cần thu hẹp phạm vi hoặc đổi mức nghiêm trọng. **Độ phủ phải ánh xạ theo rủi ro chứ đếm theo số quy tắc**, nên đầu ra của bài là một bảng rủi ro với quy tắc phủ nó chứ một con số.

**Outcome.** Kiểm ngược bộ quy tắc trên sáu tháng dữ liệu có nhãn và nộp bảng ánh xạ rủi ro với quy tắc.

**Đánh giá.** Tầng *đánh giá*. Objective thay phép đếm quy tắc bằng phép đo độ phủ rủi ro. Kiểm bằng bảng bốn ô cộng bảng rủi ro; đạt khi mọi rủi ro trọng yếu có ít nhất một quy tắc phủ và tỉ lệ báo giả nằm dưới ngưỡng thoả thuận.

**Lab.** Gắn nhãn sáu tháng dữ liệu gồm ba sự cố đã biết và bốn thay đổi nghiệp vụ hợp lệ. Chạy bộ quy tắc và lập bảng bốn ô. Với mỗi sự cố bị bỏ sót, thêm hoặc sửa quy tắc rồi chạy lại. Với mỗi báo giả, thu hẹp phạm vi hoặc hạ mức nghiêm trọng. Nộp bảng ánh xạ rủi ro với quy tắc phủ nó.

**Pitfalls.** Báo cáo độ phủ bằng số lượng quy tắc · chỉ kiểm ngược trên khoảng có sự cố · giữ quy tắc báo giả nhiều vì nó đã từng bắt đúng một lần · không gắn nhãn thay đổi nghiệp vụ hợp lệ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mọi rủi ro trọng yếu có quy tắc phủ, ba sự cố lịch sử đều bị bắt sau khi sửa, và tỉ lệ báo giả dưới ngưỡng thoả thuận.

### Lesson 284 · The reconciliation ladder - seven levels `TH`
**Prerequisites.** Lesson 283

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài mở rộng thang đối soát bốn bậc ở lesson 242 thành bảy bậc phủ toàn tuyến. Bậc một là kê khai tệp cùng tổng kiểm tra byte. Bậc hai là số dòng theo một ranh giới bất biến. Bậc ba là so tập khoá để biết thiếu, thừa hay trùng cụ thể. Bậc bốn là tổng kiểm soát theo lát cắt có nghĩa nghiệp vụ. Bậc năm là băm dòng trên giá trị đã chuẩn hoá. Bậc sáu là bất biến của quy trình nghiệp vụ xuyên nhiều tài sản. Bậc bảy là đối soát chỉ số hoặc báo cáo mà người dùng nhìn thấy, và đây là bậc duy nhất trả lời được câu người dùng có thấy đúng không. Chốt kiểm soát đặt ở bốn điểm: nguồn, vùng thô, tầng chuẩn hoá, tầng phục vụ; chênh lệch ở mỗi chốt quy được về một đoạn cụ thể thay vì một chênh lệch tổng không biết ở đâu. **Lấy mẫu hỗ trợ chẩn đoán nhưng không chứng minh được không mất và không trùng**, nên mọi tuyên bố phải nêu tổng thể, cửa sổ, phép kiểm và dung sai.

**Outcome.** Chạy bảy bậc đối soát qua bốn chốt kiểm soát và quy được mọi chênh lệch về một đoạn cụ thể.

**Đánh giá.** Tầng *áp dụng*. Objective đòi định vị chênh lệch chứ chỉ phát hiện. Kiểm bằng ba lỗi tiêm ở ba đoạn khác nhau; đạt khi cả ba được quy đúng đoạn và mọi tuyên bố đối soát nêu đủ bốn yếu tố phạm vi.

**Lab.** Dựng bộ đối soát chạy bảy bậc tại bốn chốt. Tiêm ba lỗi ở ba đoạn: mất dữ liệu khi nạp, nhân dòng khi biến đổi, và lệch làm tròn ở tầng phục vụ. Với mỗi lỗi, chỉ ra bậc nào và chốt nào phát hiện, rồi quy về đoạn gây ra. Viết một tuyên bố đối soát nêu rõ tổng thể, cửa sổ, phép kiểm và dung sai.

**Pitfalls.** Chỉ đối soát hai đầu nên không biết chênh lệch sinh ở đâu · đối soát bằng lấy mẫu rồi tuyên bố đầy đủ · bỏ bậc bảy nên người dùng thấy sai mà hệ báo xanh · đối soát hai bên ở hai thời điểm khác nhau.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba lỗi tiêm được quy đúng đoạn gây ra, và tuyên bố đối soát nêu đủ tổng thể, cửa sổ, phép kiểm và dung sai.

### Lesson 285 · Normalization before comparison `TH`
**Prerequisites.** Lesson 284

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hai hệ cùng đúng vẫn cho hai kết quả đối soát khác nhau nếu chưa chuẩn hoá, nên chuẩn hoá là điều kiện để phép so có nghĩa. Bảy nhóm phải quy về một dạng trước khi so hoặc băm: giá trị rỗng so với thiếu so với chuỗi rỗng; khoảng trắng, chữ hoa chữ thường và dạng chuẩn ký tự; múi giờ và độ phân giải thời gian; số thập phân, cách làm tròn và đơn vị tiền tệ; thứ tự bản ghi và chính sách trùng lặp; thời điểm tham chiếu khi so với dữ liệu có lịch sử; và hiệu chỉnh từ nguồn cùng dung sai về độ trễ được chấp nhận. Nhóm thứ nhất và nhóm thứ tư gây nhiều chênh lệch giả nhất. **Chênh lệch giả nguy hiểm vì nó làm người vận hành quen với việc đối soát không khớp**, và khi có chênh lệch thật thì không ai để ý. Bộ quy tắc chuẩn hoá phải là mã dùng chung cho cả hai phía, chứ mỗi bên tự viết một bản.

**Outcome.** Loại hết chênh lệch giả trên một cặp đối soát và chứng minh chênh lệch còn lại đều có nguyên nhân thật.

**Đánh giá.** Tầng *phân tích*. Objective đòi tách chênh lệch giả khỏi chênh lệch thật. Kiểm bằng phép đối soát trước và sau chuẩn hoá; đạt khi số chênh lệch giả về không và mọi chênh lệch còn lại được nêu tên nguyên nhân.

**Lab.** Đối soát hai hệ khi chưa chuẩn hoá và đếm số chênh lệch. Phân loại từng chênh lệch vào bảy nhóm. Viết một thư viện chuẩn hoá dùng chung cho cả hai phía. Đối soát lại và chứng minh số chênh lệch giả về không. Với mỗi chênh lệch còn lại, nêu nguyên nhân thật. Đưa thư viện chuẩn hoá vào bộ kiểm để nó không lệch giữa hai phía.

**Pitfalls.** Mỗi bên tự viết quy tắc chuẩn hoá · băm trực tiếp trên giá trị thô · coi chênh lệch nhỏ là chấp nhận được mà không tìm nguyên nhân · bỏ nhóm thời điểm tham chiếu khi so dữ liệu có lịch sử.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Số chênh lệch giả về không sau khi chuẩn hoá, mọi chênh lệch còn lại có nguyên nhân nêu tên, và thư viện chuẩn hoá dùng chung cho hai phía.

### Lesson 286 · Data SLI and SLO design `TH`
**Prerequisites.** Lesson 285

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Cam kết chất lượng phải phát biểu được bằng số, nếu không thì nó là một lời hứa. Sáu chỉ số phục vụ: độ trễ tới khi sẵn sàng và thời điểm sẵn sàng cam kết; tỉ lệ phân vùng thành công và đầy đủ; tỉ lệ bản ghi hợp lệ và đã đối soát; tỉ lệ trùng, mồ côi và bị cách ly; thời gian phát hiện cùng thời gian phục hồi sự cố; và bằng chứng về tính đúng của truy vấn hoặc chỉ số đã chứng nhận. Thiết kế cam kết theo hành trình người dùng và mức trọng yếu nghiệp vụ trước, chứ theo công việc chạy; **cam kết đặt theo công việc không nói gì cho người dùng**, vì một công việc xanh vẫn có thể phục vụ dữ liệu cũ. Tử số, mẫu số, cửa sổ và phần loại trừ phải định nghĩa tường minh, nếu không hai người tính ra hai con số. Ngân sách sai sót nối cam kết với quyết định phát hành.

**Outcome.** Định nghĩa ba cam kết theo hành trình người dùng với tử số, mẫu số, cửa sổ và loại trừ tường minh.

**Đánh giá.** Tầng *áp dụng*. Objective đòi đặt cam kết theo người dùng chứ theo công việc. Kiểm bằng phép thử hai người tính độc lập; đạt khi ba cam kết cho cùng con số ở hai người và mỗi cam kết dẫn được về một hành trình người dùng.

**Lab.** Chọn ba hành trình người dùng khác mức trọng yếu. Với mỗi cái, định nghĩa chỉ số phục vụ và cam kết đủ bốn phần. Nhờ một học viên khác tính độc lập ba cam kết trên cùng dữ liệu và so con số. Tạo một tình huống công việc xanh mà cam kết vẫn vỡ, và giải thích vì sao. Đặt ngân sách sai sót và nêu quyết định nó chi phối.

**Pitfalls.** Đặt cam kết theo công việc chạy · không nêu phần loại trừ nên hai người tính khác nhau · đặt cam kết bằng năng lực hiện có · bỏ chỉ số về tính đúng vì khó đo.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba cam kết cho cùng con số khi hai người tính độc lập, mỗi cam kết dẫn về một hành trình người dùng, và tình huống công việc xanh mà cam kết vỡ được tái hiện.

### Lesson 287 · Low-noise alerting and the error budget `TH`
**Prerequisites.** Lesson 286

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Cảnh báo ồn tệ hơn không có cảnh báo, vì nó dạy người trực bỏ qua. Nguyên tắc chọn cái gì đáng cảnh báo: cảnh báo trên triệu chứng người dùng chịu chứ trên mọi quy tắc theo dòng; một quy tắc dòng đỏ là một sự kiện cần ghi nhận, còn một cam kết sắp vỡ mới là một cảnh báo. Cảnh báo theo tốc độ tiêu ngân sách sai sót cho hai mức: tiêu nhanh thì gọi ngay, tiêu chậm nhưng bền thì mở việc. Bốn thuộc tính bắt buộc của một cảnh báo: có chủ sở hữu, có sổ tay xử lý, có mô tả ảnh hưởng tới bên tiêu thụ, và có hành động cụ thể; **thiếu một trong bốn thì nó là thông báo chứ cảnh báo**. Chống ồn bằng gộp theo nguyên nhân gốc, im lặng có thời hạn khi đang xử lý, và phụ thuộc giữa các cảnh báo. Chọn ngưỡng sao cho bảng theo dõi luôn xanh là một chế độ hỏng tự động chưa đạt.

**Outcome.** Dựng bộ cảnh báo có bốn thuộc tính bắt buộc và giảm được số cảnh báo không hành động được sau một vòng rà.

**Đánh giá.** Tầng *đánh giá*. Objective đo chất lượng cảnh báo bằng tỉ lệ hành động được, chứ bằng độ phủ. Kiểm bằng phát lại sự cố cũ; đạt khi ba sự cố đều sinh cảnh báo đúng chủ sở hữu và tỉ lệ cảnh báo không hành động được giảm có số đo.

**Lab.** Rà toàn bộ cảnh báo đang có, đếm tỉ lệ không hành động được trong 30 ngày. Chuyển các quy tắc dòng từ cảnh báo sang ghi nhận. Dựng cảnh báo theo tốc độ tiêu ngân sách ở hai mức. Bổ sung đủ bốn thuộc tính. Phát lại ba sự cố lịch sử và kiểm cảnh báo có nổ đúng lúc, đúng người. Đo lại tỉ lệ không hành động được.

**Pitfalls.** Cảnh báo trên từng quy tắc dòng · cảnh báo không có sổ tay xử lý · đặt ngưỡng để bảng theo dõi xanh · im lặng vĩnh viễn thay vì im lặng có hạn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba sự cố phát lại đều sinh cảnh báo đúng người, mọi cảnh báo có đủ bốn thuộc tính, và tỉ lệ không hành động được giảm có số đo.

### Lesson 288 · The incident lifecycle - eight steps `LT`
**Prerequisites.** Lesson 287

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Sự cố dữ liệu khác sự cố hệ thống ở một điểm quyết định: dữ liệu sai đã công bố thì người ta đã ra quyết định dựa trên nó, nên dừng lan rộng quan trọng hơn khôi phục nhanh. Tám bước theo thứ tự: phát hiện và phân loại mức nghiêm trọng cùng phạm vi ảnh hưởng; **dừng công bố tiếp hoặc đánh dấu suy giảm, và giữ nguyên bằng chứng**; xác định phân vùng hỏng, bên tiêu thụ bị ảnh hưởng và trạng thái tốt gần nhất; giảm thiểu bằng quay lui, cách ly, chặn truy cập hoặc thông báo; truy nguyên nhân gốc xuyên nguồn, mã, cấu hình, nền tảng và vận hành; sửa, nạp bù hoặc trình bày lại trong luồng cách ly; đối soát và lấy chấp thuận trước khi công bố lại; rồi phân tích sau sự cố. Bước hai chứa một quy tắc hay bị vi phạm khi dọn dẹp vội: **ghi đè bằng chứng sự cố là mất khả năng truy nguyên nhân**.

**Outcome.** Chạy đúng thứ tự tám bước trên một sự cố mô phỏng và nêu quyết định của từng bước.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết đặt quy trình cho hai bài thực hành sau. Kiểm bằng bài chạy quy trình; đạt khi tám bước có quyết định ghi lại, bằng chứng được giữ nguyên, và bên tiêu thụ bị ảnh hưởng được liệt kê trước khi sửa.

**Lab.** Nhận một sự cố mô phỏng thuộc một trong chín lớp sự cố: phân vùng thiếu hoặc muộn, trùng lặp, phá vỡ lược đồ, hồi quy logic thầm lặng, hỏng lịch sử chiều, nạp bù dở dang, bảng điều khiển cũ, lộ dữ liệu xuyên khách hàng, và công cụ chất lượng hỏng gây tin nhầm. Chạy tám bước và ghi quyết định từng bước. Liệt kê bên tiêu thụ ảnh hưởng bằng dòng dõi trước khi sửa.

**Pitfalls.** Sửa dữ liệu trước khi giữ bằng chứng · công bố lại trước khi đối soát · bỏ bước liệt kê bên tiêu thụ · phân tích sau sự cố quy về lỗi cá nhân.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tám bước có quyết định ghi lại theo đúng thứ tự, bằng chứng được giữ nguyên, và danh sách bên tiêu thụ lập trước khi sửa.

### Lesson 289 · Repair, backfill and restatement `TH`
**Prerequisites.** Lesson 288

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Sửa dữ liệu hỏng là thao tác dễ tạo ra hỏng lần hai, nên nó có quy trình riêng. Bốn bước bắt buộc: chạy thử không ghi để biết phạm vi sẽ chạm; chạy vào đích cách ly theo lesson 252; đối soát đích cách ly với nguồn; rồi mới thăng cấp bằng hoán đổi nguyên tử và giữ đường quay lại. **Sửa mà không cách ly tạo hỏng lần hai**, và đó là ô nguy hiểm nhất trong ma trận chế độ hỏng của module. Trình bày lại là quyết định nghiệp vụ theo lesson 158: số đã công bố có đổi hay giữ nguyên, ai duyệt, và bên tiêu thụ được báo ra sao. Sửa dữ liệu lịch sử phải giữ dấu vết đã sửa gì, vào lúc nào, bởi ai. Ba tình huống không nên sửa mà nên đánh dấu suy giảm rồi sửa gốc trước, vì sửa hạ nguồn khi gốc còn sai chỉ tạo hai nguồn sự thật.

**Outcome.** Sửa hai sự cố qua đủ bốn bước, đối soát đạt trước khi công bố lại, và không tạo hỏng lần hai.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là đối soát đạt trước công bố và quay lại được sau đó. Kiểm bằng hai sự cố sửa đầy đủ; đạt khi cả hai đối soát đạt ở đích cách ly trước khi thăng cấp và quay lại thực hiện được.

**Lab.** Nhận hai sự cố: một phân vùng thiếu và một hồi quy logic thầm lặng. Với mỗi cái, chạy thử không ghi, sửa trong đích cách ly, đối soát, thăng cấp, rồi thực hiện quay lại. Ghi chính sách trình bày lại kèm người duyệt và cách báo bên tiêu thụ. Ghi lại dấu vết đã sửa gì và bởi ai.

**Pitfalls.** Sửa thẳng vào bảng phục vụ · công bố lại trước khi đối soát · nạp lại toàn bộ để chữa mà không truy nguyên nhân · sửa hạ nguồn khi nguồn vẫn còn sai.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Hai sự cố đều đối soát đạt ở đích cách ly trước khi thăng cấp, quay lại thực hiện được, và dấu vết sửa được ghi đầy đủ.

### Lesson 290 · False positives, coverage and quality debt `TH`
**Prerequisites.** Lesson 289

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bộ quy tắc là tài sản phải bảo trì, và không bảo trì thì nó tự mục theo ba cách. Báo giả tích luỹ làm người trực mất tin, và cách đo là tỉ lệ cảnh báo bị đóng với lý do không phải vấn đề. Độ phủ suy giảm khi hệ đổi mà quy tắc không đổi, và cách đo là ánh xạ rủi ro với quy tắc theo lesson 283 chạy lại định kỳ. Nợ chất lượng tích luỹ dưới dạng miễn trừ hết hạn, quy tắc bị tắt và chênh lệch được chấp nhận; nó phải có sổ, có chủ và có hạn giống nợ kỹ thuật. Một chế độ hỏng tinh vi phải nhận ra: **phép kiểm có bộ lọc thu hẹp sẽ che đúng phần dữ liệu hỏng**, vì người viết đã loại ca gây đỏ ra khỏi phạm vi; cách phát hiện là đối chiếu số dòng phép kiểm thực sự xét với số dòng của bảng. Rà soát định kỳ bộ quy tắc và điều kiện gỡ một quy tắc.

**Outcome.** Đo ba chỉ số sức khoẻ của bộ quy tắc và tìm được phép kiểm có phạm vi che dữ liệu hỏng.

**Đánh giá.** Tầng *đánh giá*. Objective đòi đánh giá chính hệ kiểm chứ dữ liệu. Kiểm bằng ba chỉ số cộng bài rà phạm vi; đạt khi ba chỉ số có số đo và mọi phép kiểm có bộ lọc thu hẹp đều được đối chiếu số dòng xét.

**Lab.** Đo tỉ lệ báo giả trong 30 ngày, chạy lại ánh xạ rủi ro với quy tắc, và lập sổ nợ chất lượng gồm miễn trừ hết hạn cùng quy tắc đang tắt. Với mọi phép kiểm có bộ lọc, đối chiếu số dòng nó xét với số dòng bảng và tìm ca che dữ liệu hỏng. Gỡ những quy tắc không còn phủ rủi ro nào.

**Pitfalls.** Coi phép kiểm xanh là dữ liệu sạch mà không xem phạm vi · để miễn trừ hết hạn nằm mãi · thêm quy tắc mà không bao giờ gỡ · đo độ phủ bằng số lượng quy tắc.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba chỉ số sức khoẻ có số đo, mọi phép kiểm có bộ lọc được đối chiếu số dòng xét, và sổ nợ chất lượng có chủ cùng hạn.

### Lesson 291 · The quality failure matrix `TH`
**Prerequisites.** Lesson 290

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài gom bảy chế độ hỏng mà hợp đồng nguồn liệt kê thành một bảng dùng được khi trực, mỗi dòng gồm hiện tượng, lý do phép kiểm thông thường bỏ sót, và chốt kiểm soát tốt hơn. Toàn bộ dữ liệu lệch múi giờ thì kiểu và khoảng đều hợp lệ, cần bộ đối chứng và kiểm ranh giới thời gian. Phép kết nhân dòng làm chỉ số sai thì kiểm theo dòng xanh, cần đối soát theo hạt và tổng kiểm soát. Phân vùng thiếu thì phép kiểm theo dòng không chạy lần nào, cần kiểm đầy đủ theo phân vùng kỳ vọng. Quy tắc tốt chặn nhầm dữ liệu tốt vì ngưỡng hoặc bối cảnh sai, cần kiểm ngược và cách ly thay vì chặn. Phép kiểm loại trừ chính phần hỏng, cần đối chiếu số dòng xét. Đường dẫn xanh trên nguồn cũ vì mọi việc chạy xong trên đầu vào cũ, cần chỉ số độ tươi của nguồn. Sửa tạo hỏng lần hai, cần chạy thử, cách ly và đối soát trước khi thăng cấp.

**Outcome.** Lập ma trận bảy chế độ hỏng có chốt kiểm soát tự động cho từng dòng và chứng minh bằng phép thử tiêm.

**Đánh giá.** Tầng *đánh giá*. Objective tổng hợp toàn module thành một hệ phòng vệ có bằng chứng. Kiểm bằng bảy lỗi tiêm; đạt khi ít nhất sáu bị chốt kiểm soát tương ứng phát hiện tự động.

**Lab.** Lập ma trận bảy dòng đủ ba cột. Với mỗi dòng, cài chốt kiểm soát tự động. Giảng viên tiêm bảy lỗi tương ứng vào hệ và đếm bao nhiêu cái bị phát hiện, mất bao lâu. Với lỗi không bị bắt, bổ sung chốt và tiêm lại. Đưa cả bảy vào bộ kiểm hồi quy.

**Pitfalls.** Viết cột chốt kiểm soát mà không cài tự động · bỏ dòng đường dẫn xanh trên nguồn cũ vì nghĩ hiếm · tin bộ kiểm hiện có đã phủ cả bảy · không đo thời gian phát hiện.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** ≥ 6/7 lỗi tiêm bị phát hiện tự động kèm thời gian phát hiện, và cả bảy chốt kiểm soát nằm trong bộ kiểm hồi quy.

### Lesson 292 · Reliability capstone - twenty seeded defects `DA`
**Prerequisites.** Lesson 291

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Bài dự án khép module, lấy đúng yêu cầu capstone của hợp đồng nguồn: bổ sung lớp kiểm soát tin cậy vào nền tảng đã dựng ở M14. Nộp gồm bảy hạng mục: hợp đồng dữ liệu và sổ đăng ký quy tắc đủ bảy phần; bộ kiểm cài trên một nền được chọn; đối soát bảy bậc từ nguồn tới tầng phục vụ; vùng cách ly cùng đường phát lại và một cửa chặn công bố có chứng nhận; cam kết dịch vụ, bảng theo dõi, cảnh báo, trạng thái và sổ tay vận hành; ma trận bảy chế độ hỏng có chốt tự động; và kết quả diễn tập ba tình huống gồm hồi quy logic thầm lặng, phân vùng thiếu, và một lần nạp bù hỏng. Nghiệm thu bằng 20 lỗi gieo sẵn: đo độ phủ phát hiện và tỉ lệ báo giả. Sáu điều kiện tự động chưa đạt lấy từ phần *Critical failures* của nguồn, gồm dùng số lượng phép kiểm làm bằng chứng độ phủ, tuyên bố chính xác không có nguồn đối chiếu, bỏ lỗi chất lượng im lặng, công bố bản sửa trước khi đối soát, cảnh báo không có chủ hoặc sổ tay, và ghi đè bằng chứng sự cố khi dọn dẹp.

**Outcome.** Nộp lớp kiểm soát tin cậy đủ bảy hạng mục, đạt ngưỡng phát hiện trên 20 lỗi gieo sẵn và không vi phạm sáu điều kiện.

**Đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module thành một hệ vận hành có bằng chứng định lượng. Kiểm bằng 20 lỗi gieo; đạt khi phát hiện ít nhất 16 với tỉ lệ báo giả dưới ngưỡng, và hai sự cố được sửa cùng đối soát cùng ghi lại.

**Lab.** Dựng lớp kiểm soát theo bảy hạng mục. Gieo 20 lỗi thuộc nhiều loại, trong đó ít nhất bốn lỗi thuộc loại phép kiểm theo dòng không bắt được. Đo độ phủ phát hiện, thời gian phát hiện và tỉ lệ báo giả. Người chấm tiêm thêm một lỗi thầm lặng chưa từng gặp; định vị phạm vi ảnh hưởng và chạy phục hồi an toàn.

**Pitfalls.** Thêm quy tắc để tăng độ phủ mà không ánh xạ rủi ro · tắt quy tắc ồn ngay trước khi chấm · công bố bản sửa trước khi đối soát · ghi đè bằng chứng sự cố khi dọn dẹp.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Phát hiện ≥ 16/20 lỗi gieo với tỉ lệ báo giả dưới ngưỡng, hai sự cố được sửa và đối soát và ghi lại, và không vi phạm sáu điều kiện tự động chưa đạt.

# MODULE M14D · METADATA ENGINEERING, CATALOG, LINEAGE AND GOVERNANCE

**Phase 7 · Lessons 293–308 · 33 giờ**

| | |
|---|---|
| **Objective cấp module** | Thiết kế mô hình siêu dữ liệu chuẩn, thu thập được dòng dõi có xuất xứ và độ tin cậy, rồi vận hành quyền sở hữu, từ điển, chứng nhận và khai tử |
| **Tiền đề** | M11 · M11C · M14 · M14C |
| **Exit criterion** | Định danh chuẩn phân giải cùng một tài sản xuyên hệ và xuyên môi trường mà không đụng độ; đường dòng dõi trọng yếu có xuất xứ cùng độ tin cậy; chú thích thủ công không bị thu thập tự động ghi đè |
| **Kỹ năng SFIA** | `DATM` mức 5 · `GOVN` mức 4 |
| **Chế độ hỏng** | Báo cáo dòng dõi do bộ phân tích suy ra như một sự thật, và tuyên bố danh mục cưỡng chế quyền truy cập trong khi nó chỉ lưu siêu dữ liệu |

**Module bù năng lực Analytics Engineer thứ tư và cuối cùng.** Nó sở hữu mô hình siêu dữ liệu, việc thu thập, dòng dõi, khả năng khám phá, từ điển, quyền sở hữu và các luồng phê duyệt.

Ranh giới lấy từ hợp đồng nguồn: nó **không thay** mô hình hoá dữ liệu, không thay việc chạy kiểm chất lượng, không phải hệ quản lý danh tính, và không phải thẩm quyền quản trị của tổ chức.

Nguyên tắc nhận thức xuyên module: **siêu dữ liệu thu thập tự động không tự nhiên trở thành ý nghĩa đáng tin**. Mỗi trường phải mang xuất xứ, thời điểm quan sát và thẩm quyền; cạnh dòng dõi không chắc chắn phải giữ nguyên trạng thái không chắc chắn thay vì vẽ thành một cạnh trông như sự thật.

### Lesson 293 · Metadata taxonomy - seven types and their authority `LT`
**Prerequisites.** Module 14D: M14C

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài mở module bằng việc tách bảy loại siêu dữ liệu, vì mỗi loại có một nguồn có thẩm quyền khác nhau và trộn chúng làm hỏng cả bảy. Kỹ thuật gồm lược đồ, kiểu, phân vùng, câu lệnh và vị trí, lấy từ nền tảng và hiện vật. Vận hành gồm lần chạy, độ tươi, khối lượng, lỗi và kế hoạch truy vấn, lấy từ bộ điều phối cùng engine. Nghiệp vụ gồm định nghĩa, hạt, chỉ số và thuật ngữ, lấy từ chủ sở hữu miền chứ từ bộ thu thập. Quyền sở hữu gồm đội, người quản lý và người trực. Quản trị gồm phân loại, chính sách, thời hạn giữ và chứng nhận. Sử dụng gồm truy vấn, bảng điều khiển, người dùng và mức phổ biến. Dòng dõi gồm các cạnh giữa tài sản, trường và công việc. **Mỗi trường cần xuất xứ, thời điểm quan sát và thẩm quyền**; một mô tả do bộ thu thập lấy từ chú thích cột không có cùng thẩm quyền với định nghĩa do chủ sở hữu miền viết.

**Outcome.** Phân bảy loại cho một tập trường siêu dữ liệu thật và chỉ đúng nguồn có thẩm quyền của từng loại.

**Đánh giá.** Tầng *hiểu*. Bài mở module, đặt từ vựng và đặt nguyên tắc xuất xứ. Kiểm bằng bài phân loại 20 trường; đạt khi phân đúng ít nhất 16 và mỗi trường có nguồn thẩm quyền nêu tên.

**Lab.** Cho 20 trường siêu dữ liệu thật lấy từ một danh mục đang chạy. Phân vào bảy loại và ghi nguồn có thẩm quyền của từng cái. Tìm ba trường đang lấy từ nguồn không có thẩm quyền và chỉ ra hậu quả. Bổ sung xuất xứ cùng thời điểm quan sát cho mọi trường chưa có.

**Pitfalls.** Coi mọi siêu dữ liệu thu thập được là đáng tin như nhau · lấy định nghĩa nghiệp vụ từ chú thích cột · không ghi thời điểm quan sát nên không biết dữ liệu cũ hay mới · gộp quyền sở hữu với quản trị.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân đúng ≥ 16/20 trường, mỗi trường có nguồn thẩm quyền nêu tên, và ba trường lấy sai thẩm quyền được chỉ ra.

### Lesson 294 · The canonical model - entities, URNs and identity `TH`
**Prerequisites.** Lesson 293

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Không có định danh ổn định thì mọi thứ còn lại sụp, nên bài này đặt nền định danh trước khi thu thập bất cứ gì. Danh sách thực thể cần mô hình hoá: cơ sở dữ liệu, lược đồ, bảng, khung nhìn, cột, tệp, chủ đề, công việc, tác vụ, mô hình, bảng điều khiển, biểu đồ, chỉ số, giao diện lập trình, sản phẩm dữ liệu, miền, đội, người dùng, nhãn, thuật ngữ và chính sách. Tên định danh chuẩn phải mang đủ nền tảng, thể hiện và môi trường, vì cùng một tên bảng tồn tại ở cả môi trường phát triển lẫn sản xuất. **Định danh trùng làm quyền sở hữu và dòng dõi bị chẻ đôi**, và đây là chế độ hỏng nền tảng nhất của module: hai bản ghi cho cùng một bảng nghĩa là nửa dòng dõi nằm ở bản này, nửa ở bản kia, nên phân tích ảnh hưởng thiếu. Cơ chế gộp danh tính trùng và cơ chế bí danh. Đánh đổi giữa kho đồ thị với kho quan hệ hoặc kho tài liệu.

**Outcome.** Thiết kế tên định danh chuẩn phân giải đúng cùng một tài sản xuyên bốn hệ và ba môi trường.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là không đụng độ và không chẻ danh tính. Kiểm bằng bài phân giải; đạt khi 40 tài sản từ bốn hệ phân giải đúng, không cặp nào đụng độ, và ca trùng danh tính được gộp đúng.

**Lab.** Định nghĩa lược đồ thực thể và quy tắc sinh tên định danh chuẩn. Lấy 40 tài sản thật từ bốn hệ và ba môi trường, sinh định danh cho từng cái. Kiểm không có hai tài sản khác nhau nhận cùng định danh và không có một tài sản nhận hai định danh. Tạo một ca trùng danh tính và gộp bằng cơ chế bí danh. So hai cách lưu trữ trên một truy vấn đồ thị điển hình.

**Pitfalls.** Dùng tên bảng làm định danh · bỏ môi trường khỏi định danh nên phát triển và sản xuất lẫn nhau · cho phép cặp khoá giá trị tuỳ ý thay vì mở rộng lược đồ có kiểm soát · không có cơ chế gộp danh tính trùng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** 40 tài sản phân giải đúng không đụng độ và không chẻ danh tính, và ca trùng được gộp bằng bí danh.

### Lesson 295 · Relationships, versioning, rename and soft deletion `TH`
**Prerequisites.** Lesson 294

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Cạnh quan hệ và vòng đời của chúng, nơi ba thao tác thường ngày phá hỏng đồ thị nếu xử lý sai. Bảy loại quan hệ: chứa, sinh ra, tiêu thụ, dẫn xuất, sở hữu, tài liệu hoá, và phân loại. Phiên bản cùng thời gian hiệu lực cho phép trả lời câu tài sản này hồi tháng trước có lược đồ gì. Xoá mềm bằng bia mộ giữ lại lịch sử thay vì xoá thật. **Đổi tên bị xử lý như xoá rồi tạo mới là chế độ hỏng làm mất toàn bộ lịch sử và mất cả danh sách bên tiêu thụ**; cách đúng là nhận diện đổi tên rồi ghi quan hệ kế thừa cùng bí danh, và cơ chế nhận diện dựa trên định danh ổn định hoặc trên so khớp lược đồ cùng dòng dõi. Bản số của quan hệ và những chỗ không được phép có chu trình. Mở rộng lược đồ có kiểm soát thay vì cho gắn cặp khoá giá trị tuỳ ý, vì cái sau biến danh mục thành bãi rác trong vài tháng.

**Outcome.** Xử lý đổi tên, xoá và phiên bản sao cho lịch sử cùng danh sách bên tiêu thụ không mất.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là truy được lịch sử sau ba thao tác phá hoại. Kiểm bằng ba thao tác; đạt khi sau cả ba vẫn truy được lược đồ cũ và danh sách bên tiêu thụ, và không có cạnh treo.

**Lab.** Dựng đồ thị có đủ bảy loại quan hệ cho 30 tài sản. Thực hiện ba thao tác: đổi tên một bảng, xoá một bảng còn bên tiêu thụ, và đổi lược đồ hai lần. Sau mỗi thao tác, truy lịch sử và danh sách bên tiêu thụ. Viết phép kiểm chặn cạnh treo và chặn chu trình ở nơi không cho phép.

**Pitfalls.** Xử lý đổi tên như xoá rồi tạo mới · xoá cứng bản ghi tài sản · cho phép gắn thuộc tính tuỳ ý · không kiểm cạnh treo sau mỗi lần thu thập.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Sau ba thao tác vẫn truy được lược đồ cũ và danh sách bên tiêu thụ, và phép kiểm không tìm thấy cạnh treo nào.

### Lesson 296 · Ingestion architecture - the six-step harvest `TH`
**Prerequisites.** Lesson 295

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Đường thu thập siêu dữ liệu là một đường dẫn dữ liệu, nên nó chịu mọi kỷ luật đã học ở M14B. Sáu bước: bộ nối đọc giao diện lập trình, hiện vật, nhật ký hoặc lịch sử truy vấn của nguồn; chuẩn hoá về thực thể và cạnh chuẩn kèm xuất xứ; so sánh rồi chèn hoặc cập nhật có phiên bản, xử lý xoá cùng đổi tên và nguồn đã cũ; phát sự kiện thay đổi và cập nhật đồ thị cùng chỉ mục tìm kiếm; kiểm tính đầy đủ, độ tươi, danh tính và quan hệ; rồi đưa thay đổi, ảnh hưởng và luồng phê duyệt ra cho người dùng. Bước năm là bước hay bị bỏ và bỏ nó thì danh mục trông đầy mà sai. Nguồn đầu vào giàu nhất là hiện vật của công cụ biến đổi theo lesson 266 và sự kiện thời gian chạy của bộ điều phối, vì chúng khai báo tường minh chứ phải suy đoán. Thu thập phải luỹ đẳng theo lesson 250.

**Outcome.** Cài đường thu thập sáu bước luỹ đẳng từ hai nguồn và chứng minh chạy lại không tạo bản ghi trùng.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là trạng thái đồ thị hội tụ sau nhiều lần chạy. Kiểm bằng phép thử chạy lại; đạt khi đồ thị sau năm lần chạy chồng chéo khớp đồ thị sau một lần chạy sạch và bước kiểm phát hiện được lỗi tiêm.

**Lab.** Cài bộ nối cho hiện vật của công cụ biến đổi và cho sự kiện của bộ điều phối. Chạy đủ sáu bước. Chạy lại năm lần với thời điểm bắt đầu chồng chéo và có lần bị giết giữa chừng; so đồ thị cuối với đồ thị của một lần chạy sạch. Tiêm một lỗi về danh tính và một cạnh treo, xác nhận bước kiểm bắt được.

**Pitfalls.** Bỏ bước kiểm nên danh mục đầy mà sai · thu thập không luỹ đẳng nên chạy lại sinh bản trùng · suy đoán quan hệ khi nguồn đã khai báo tường minh · không phát sự kiện thay đổi nên chỉ mục tìm kiếm lệch với đồ thị.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đồ thị sau năm lần chạy chồng chéo khớp đồ thị của một lần chạy sạch, và bước kiểm bắt được cả hai lỗi tiêm.

### Lesson 297 · Connector concerns - incremental crawl, partial failure, preserved annotations `TH`
**Prerequisites.** Lesson 296

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bộ nối gặp đúng những vấn đề của một trình trích xuất ở M14B, cộng thêm một vấn đề riêng. Quét toàn bộ so với thu thập tăng dần theo sự kiện, và đánh đổi giữa độ tươi với tải đặt lên nguồn. Hạn mức, phân trang, điểm kiểm tra và quyền hạn, theo lesson 237 và 238. Luỹ đẳng, trùng lặp, quét dở dang và nguồn đã xoá tài sản. Bí mật và nguyên tắc quyền tối thiểu chỉ đọc: **dùng quyền quản trị sản xuất để thu thập là một chế độ hỏng tự động chưa đạt**, vì một bộ nối chỉ cần đọc siêu dữ liệu. Tương thích phiên bản khi nâng cấp bộ nối. Vấn đề riêng của module và là ô nguy hiểm nhất: **chú thích thủ công do người viết bị lần thu thập sau ghi đè**, làm mất toàn bộ ngữ cảnh nghiệp vụ; lời giải là một chính sách ưu tiên nguồn tường minh, trong đó trường do người có thẩm quyền viết thắng trường do bộ thu thập lấy. Nạp lại và dựng lại chỉ mục mà không mất chú thích.

**Outcome.** Vận hành bộ nối qua bốn tình huống hỏng và chứng minh chú thích thủ công không bị mất.

**Đánh giá.** Tầng *áp dụng*. Objective có một tiêu chí nghiệm thu đặc trưng là bảo toàn chú thích. Kiểm bằng bốn tình huống; đạt khi cả bốn phục hồi đúng và không chú thích thủ công nào bị ghi đè sau khi dựng lại chỉ mục.

**Lab.** Thêm 20 chú thích thủ công vào các tài sản. Chạy bốn tình huống: quét dở dang, bộ nối trễ, nguồn xoá tài sản, và nâng cấp bộ nối lên phiên bản mới. Sau mỗi tình huống, đếm chú thích còn lại. Viết chính sách ưu tiên nguồn và chứng minh nó chặn ghi đè. Rà quyền của bộ nối và hạ xuống mức chỉ đọc siêu dữ liệu.

**Pitfalls.** Cho bộ nối quyền quản trị sản xuất · để lần thu thập ghi đè mọi trường · dựng lại danh mục từ đầu mà không di trú danh tính và chú thích · quét toàn bộ mỗi giờ làm nguồn quá tải.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** 20 chú thích thủ công còn nguyên sau cả bốn tình huống, chính sách ưu tiên nguồn chặn được ghi đè, và bộ nối chạy bằng quyền chỉ đọc.

### Lesson 298 · Lineage levels and what each answers `LT`
**Prerequisites.** Lesson 297

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Năm mức dòng dõi trả lời năm câu hỏi khác nhau, và đòi mức sai thì vừa tốn vừa không trả lời được câu mình cần. Dòng dõi mức tập dữ liệu nối nguồn với đích, đủ để trả lời câu bảng này lấy dữ liệu từ đâu. Dòng dõi mức trường nối biểu thức dẫn xuất từng cột, cần cho phân tích ảnh hưởng chính xác và đắt hơn nhiều. Dòng dõi mức công việc nối thành phần thực thi cùng phiên bản của nó. Dòng dõi mức bảng điều khiển và chỉ số nối tới nơi tiêu thụ, và đây là mức duy nhất trả lời được câu đổi cột này thì ai nhìn thấy số khác. Khác biệt cuối cùng và quan trọng: **dòng dõi tĩnh mô tả đồ thị có thể xảy ra, dòng dõi thời gian chạy mô tả đường đã thật sự chạy**; một cạnh có trong mã nhưng chưa bao giờ chạy và một cạnh đã chạy hôm qua là hai sự thật khác nhau, và câu hỏi vận hành thường cần cái thứ hai.

**Outcome.** Chọn mức dòng dõi cho năm câu hỏi thực tế và phân biệt dòng dõi tĩnh với dòng dõi thời gian chạy.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết đặt khung cho bốn bài thực hành sau. Kiểm bằng bài ánh xạ năm câu hỏi; đạt khi chọn đúng ít nhất bốn mức và nêu đúng một câu hỏi chỉ trả lời được bằng dòng dõi thời gian chạy.

**Lab.** Cho năm câu hỏi vận hành thật. Với mỗi câu, chỉ ra mức dòng dõi tối thiểu trả lời được và chi phí kéo theo. Trên hệ đang có, tìm một cạnh có trong mã nhưng chưa từng chạy và một cạnh đã chạy; giải thích hai loại bằng chứng khác nhau ra sao. Ước lượng chi phí nâng từ mức tập dữ liệu lên mức trường.

**Pitfalls.** Đòi dòng dõi mức trường cho mọi thứ · dùng dòng dõi tĩnh để trả lời câu hỏi về lần chạy hôm qua · bỏ mức tiêu thụ nên không biết ai bị ảnh hưởng · coi năm mức là một khái niệm.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chọn đúng mức cho ≥ 4/5 câu hỏi kèm chi phí, và hai loại cạnh tĩnh với thời gian chạy được phân biệt bằng ví dụ thật.

### Lesson 299 · Five extraction methods and their weaknesses `TH`
**Prerequisites.** Lesson 298

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Năm cách lấy dòng dõi, mỗi cách mạnh ở một chỗ và mù ở một chỗ, nên hệ thật dùng nhiều cách rồi hợp nhất. Khai báo tường minh từ hiện vật của khung biến đổi cho đồ thị chính xác nhưng chỉ trong phạm vi khung đó. Phân tích câu lệnh cho chi tiết tới mức cột ở quy mô lớn nhưng vấp phương ngữ, câu lệnh sinh động và hàm tự viết. Sự kiện thời gian chạy theo một chuẩn mở cho bối cảnh thật của lần chạy nhưng phụ thuộc mức tích hợp và thời hạn giữ. Lịch sử truy vấn cho thấy tiêu thụ thật nhưng chịu giới hạn về mẫu và về quyền, và bỏ sót truy vấn gián tiếp. Khai báo thủ công cho cạnh nghiệp vụ mà không cách nào tự lấy được, đổi lại nó cũ đi và tốn công quản trị. **Vùng mù của bốn cách đầu cộng lại vẫn còn khoảng trống**, nên phần còn thiếu phải hiện ra dưới dạng không rõ chứ bị lấp bằng suy đoán.

**Outcome.** Lấy dòng dõi bằng ít nhất ba cách, hợp nhất, và định lượng độ phủ cùng vùng mù của từng cách.

**Đánh giá.** Tầng *phân tích*. Objective đòi đo độ phủ chứ chỉ dựng được đồ thị. Kiểm bằng bảng độ phủ ba cách; đạt khi mỗi cách có tỉ lệ phủ đo được trên cùng tập tài sản và phần không cách nào phủ được đánh dấu rõ.

**Lab.** Trên cùng một nền tảng, lấy dòng dõi bằng khai báo tường minh, phân tích câu lệnh, và sự kiện thời gian chạy. Hợp nhất ba đồ thị. Với mỗi cách, tính tỉ lệ tài sản được phủ và liệt kê loại tài sản nó không thấy. Chỉ ra phần không cách nào phủ và đánh dấu trạng thái không rõ thay vì bỏ trống.

**Pitfalls.** Dùng một cách rồi coi đồ thị là đầy đủ · lấp khoảng trống bằng suy đoán · bỏ lịch sử truy vấn nên không biết ai đang tiêu thụ · không đo độ phủ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba cách đều có tỉ lệ phủ đo được trên cùng tập tài sản, và phần không cách nào phủ được đánh dấu trạng thái không rõ.

### Lesson 300 · Edge provenance - extracted, inferred, manual, unknown `TH`
**Prerequisites.** Lesson 299

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài đặt ra quy tắc nhận thức trung tâm của module: một cạnh dòng dõi phải mang theo bằng chứng của chính nó. Bốn trạng thái xuất xứ: trích xuất được, tức có khai báo tường minh hoặc bằng chứng thời gian chạy; suy ra, tức do bộ phân tích hoặc luật sinh, kèm tên luật, phiên bản và độ tin cậy; thủ công, tức một khẳng định của chủ sở hữu đã được duyệt; và không rõ hoặc nhập nhằng, tức giữ nguyên sự không chắc chắn. **Vẽ một cạnh suy ra như một cạnh sự thật làm phân tích ảnh hưởng sai**, và sai theo hướng nguy hiểm: người dùng tin rằng đã liệt kê hết bên bị ảnh hưởng trong khi thực tế còn thiếu. Hiển thị phải phân biệt được bốn trạng thái, và truy vấn ảnh hưởng phải trả về cả phần không chắc chắn kèm cảnh báo. Ngưỡng độ tin cậy để một cạnh được dùng trong quyết định tự động.

**Outcome.** Gắn xuất xứ cho mọi cạnh và chứng minh truy vấn ảnh hưởng phân biệt được cạnh chắc chắn với cạnh suy ra.

**Đánh giá.** Tầng *áp dụng*. Objective là một ràng buộc nhận thức kiểm được bằng truy vấn. Kiểm bằng phép kiểm xuất xứ cộng truy vấn ảnh hưởng; đạt khi không cạnh nào thiếu xuất xứ và truy vấn ảnh hưởng trả về phần không chắc chắn kèm cảnh báo.

**Lab.** Gắn một trong bốn trạng thái xuất xứ cho mọi cạnh trong đồ thị đã hợp nhất, cạnh suy ra kèm tên luật và độ tin cậy. Viết phép kiểm chặn cạnh không có xuất xứ. Chạy một truy vấn ảnh hưởng và chứng minh kết quả tách phần chắc chắn khỏi phần suy ra và phần không rõ. Đặt ngưỡng độ tin cậy cho quyết định tự động và nêu lý do.

**Pitfalls.** Vẽ cạnh suy ra như cạnh sự thật · bỏ cạnh không chắc chắn cho đồ thị sạch · không ghi phiên bản luật suy diễn · dùng cạnh độ tin cậy thấp cho quyết định tự động.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Không cạnh nào thiếu xuất xứ, và truy vấn ảnh hưởng tách rõ phần chắc chắn, phần suy ra và phần không rõ.

### Lesson 301 · Column lineage - why a parser cannot always prove it `TH`
**Prerequisites.** Lesson 300

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Dòng dõi mức cột là thứ đáng giá nhất và cũng là thứ không bao giờ đạt được hoàn toàn bằng máy, nên bài này liệt kê chính xác chỗ bộ phân tích chịu thua. Chọn toàn bộ cột làm tập cột đầu ra phụ thuộc lược đồ tại thời điểm chạy. Bí danh, trường lồng nhau, biểu thức bảng chung và truy vấn con làm chuỗi dẫn xuất dài và dễ đứt. Hàm tự viết cùng thủ tục lưu trữ là hộp đen với bộ phân tích. Câu lệnh sinh động và mã vĩ mô chỉ biết được nội dung sau khi kết xuất. Bảng tạm và mã ngoài viết bằng ngôn ngữ khác nằm ngoài tầm. Phép hợp, hàm cửa sổ và phép gộp tạo ra khác biệt giữa dẫn xuất theo biểu thức với ảnh hưởng theo ngữ nghĩa: một cột nằm trong điều kiện lọc ảnh hưởng tới kết quả mà không xuất hiện trong biểu thức đầu ra. **Khi bộ phân tích không chứng minh được, câu trả lời đúng là đánh dấu không rõ** chứ đoán một cạnh trông hợp lý.

**Outcome.** Chạy phân tích cột trên một tập câu lệnh đại diện và đánh dấu đúng mọi cạnh bộ phân tích không chứng minh được.

**Đánh giá.** Tầng *phân tích*. Objective đòi nhận ra giới hạn của công cụ và biểu diễn giới hạn đó. Kiểm bằng tập câu lệnh có ca khó; đạt khi mọi ca bộ phân tích chịu thua đều được đánh dấu không rõ và không ca nào bị vẽ thành cạnh sự thật.

**Lab.** Chuẩn bị 15 câu lệnh đại diện gồm chọn toàn bộ cột, biểu thức bảng chung lồng nhau, hàm tự viết, câu lệnh sinh động, phép hợp và hàm cửa sổ. Chạy bộ phân tích và đối chiếu kết quả với dòng dõi đúng do người xác định. Đếm số cạnh đúng, số cạnh sai và số cạnh bị bỏ sót. Đánh dấu không rõ cho mọi ca không chứng minh được. Tìm một cột ảnh hưởng qua điều kiện lọc mà không nằm trong biểu thức đầu ra.

**Pitfalls.** Tin kết quả bộ phân tích là đầy đủ · bỏ ca chọn toàn bộ cột vì khó · vẽ cạnh cho hàm tự viết theo phỏng đoán · bỏ qua ảnh hưởng qua điều kiện lọc.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mọi ca bộ phân tích chịu thua được đánh dấu không rõ, không cạnh suy đoán nào được vẽ thành sự thật, và ca ảnh hưởng qua điều kiện lọc được tìm ra.

### Lesson 302 · Impact analysis from a source column to a dashboard `TH`
**Prerequisites.** Lesson 301

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài chứng minh giá trị thật của đồ thị dòng dõi bằng câu hỏi mà nó sinh ra để trả lời. Truy vấn ảnh hưởng đi xuôi từ một cột nguồn qua các mô hình, qua chỉ số, tới bảng điều khiển và tới bên tiêu thụ; truy vấn nguyên nhân đi ngược từ một con số sai về tới nguồn. Kết quả phải kèm ba thứ để dùng được: danh sách bên tiêu thụ cùng chủ sở hữu của họ, mức tin cậy của từng đường, và phần không chắc chắn được nêu riêng. Ba tình huống dùng thật: trước khi đổi lược đồ thì biết phải báo ai theo lesson 264; khi có sự cố thì biết phạm vi ảnh hưởng theo lesson 288; và khi cắt chi phí thì biết tài sản nào không phục vụ ai. **Truy vấn ảnh hưởng thiếu vẫn trông như một câu trả lời đầy đủ**, nên nó phải luôn nói rõ độ phủ của đồ thị bên dưới, nếu không người dùng tưởng đã liệt kê hết.

**Outcome.** Chạy truy vấn ảnh hưởng hai chiều và trả về danh sách bên tiêu thụ kèm chủ sở hữu, mức tin cậy và phần không chắc chắn.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu bằng đối chiếu với danh sách đúng. Kiểm bằng ba truy vấn; đạt khi kết quả khớp danh sách đúng ở ít nhất hai và mọi kết quả đều kèm độ phủ của đồ thị.

**Lab.** Chạy ba truy vấn ảnh hưởng từ ba cột nguồn khác nhau tới bảng điều khiển. Đối chiếu kết quả với danh sách đúng xác định bằng tay. Chạy một truy vấn nguyên nhân ngược từ một con số sai. Với mỗi kết quả, kèm chủ sở hữu, mức tin cậy và độ phủ của đồ thị. Dùng kết quả để lập danh sách thông báo cho một lần đổi lược đồ.

**Pitfalls.** Trình bày kết quả truy vấn ảnh hưởng như danh sách đầy đủ · bỏ mức tin cậy · không kèm chủ sở hữu nên không báo được ai · bỏ phần không chắc chắn cho kết quả gọn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Kết quả khớp danh sách đúng ở ≥ 2/3 truy vấn, mọi kết quả kèm chủ sở hữu cùng mức tin cậy cùng độ phủ đồ thị.

### Lesson 303 · Catalog and discovery - search, relevance and the asset page `TH`
**Prerequisites.** Lesson 302

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Danh mục chỉ có giá trị khi người ta tìm thấy và tin được thứ tìm thấy, nên bài này nối thẳng với phép thử khả năng tìm thấy ở lesson 192. Tìm kiếm theo tên, mô tả, lược đồ, thuật ngữ, miền, chủ sở hữu, nhãn và mức sử dụng. Xếp hạng kết hợp khớp chính xác, khớp gần đúng, mức phổ biến, độ tươi, trạng thái chứng nhận, và **lọc theo quyền trước khi trả kết quả**, vì trả về siêu dữ liệu của tài sản mà người dùng không được xem cũng là rò rỉ. Trang tài sản phải có đủ mục đích, hạt, lược đồ, chủ sở hữu, cam kết dịch vụ, tình trạng chất lượng, dòng dõi, bên tiêu thụ, truy vấn mẫu và cách xin quyền. Duyệt theo miền và theo sản phẩm dữ liệu. Một cạm bẫy của xếp hạng theo mức phổ biến: **một tài sản bị dùng rộng rãi nhưng sai sẽ được đẩy lên đầu và trông như đã được chứng nhận**, nên mức phổ biến không được thay tín hiệu chứng nhận.

**Outcome.** Dựng tìm kiếm có lọc theo quyền và trang tài sản đủ mục, đạt ngưỡng trong phép thử khả năng tìm thấy.

**Đánh giá.** Tầng *đánh giá*. Objective đo bằng hành vi người dùng và bằng phép thử rò rỉ. Kiểm bằng phép thử với năm người cộng phép thử quyền; đạt khi tỉ lệ tìm thấy vượt ngưỡng và không kết quả nào lộ siêu dữ liệu ngoài quyền.

**Lab.** Dựng trang tài sản đủ mười mục cho 20 tài sản. Cài xếp hạng có lọc theo quyền. Chạy phép thử khả năng tìm thấy với năm người, mỗi người một nhu cầu, tính giờ ba phút. Chạy phép thử phủ định với một tài khoản hạn chế và kiểm không kết quả nào lộ tài sản ngoài quyền. Tạo một tài sản phổ biến nhưng chưa chứng nhận và chứng minh giao diện không làm nó trông như đã chứng nhận.

**Pitfalls.** Trả kết quả tìm kiếm trước khi lọc quyền · xếp hạng chỉ theo mức phổ biến · trang tài sản thiếu hạt và chủ sở hữu · đo danh mục bằng số tài sản đã đăng ký.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tỉ lệ tìm thấy trong ba phút vượt ngưỡng, không kết quả nào lộ siêu dữ liệu ngoài quyền, và tài sản phổ biến chưa chứng nhận không bị hiển thị như đã chứng nhận.

### Lesson 304 · Ownership, glossary and conflicting domain meanings `TH`
**Prerequisites.** Lesson 303

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Quyền sở hữu và từ vựng là hai thứ quyết định danh mục có được dùng hay không, và cả hai đều là vấn đề tổ chức được biểu diễn bằng dữ liệu. Năm vai: chủ sở hữu kỹ thuật, chủ sở hữu sản phẩm hoặc miền, người quản lý dữ liệu, người trực, và người phê duyệt. Ba phép đo về quyền sở hữu: độ phủ, phát hiện đội hoặc người đã rời, và đường leo thang. Một nguyên tắc dễ bị vi phạm: **chủ sở hữu phải có thẩm quyền và có năng lực**, nên gán tự động người tạo bảng chỉ là bước khởi tạo chứ không phải trạng thái quản trị cuối cùng. Thuật ngữ trong từ điển gồm định nghĩa, phạm vi, ví dụ cùng phản ví dụ, từ đồng nghĩa, chủ sở hữu và quan hệ; gắn thuật ngữ vào cột, tài sản và chỉ số, và phân biệt thuật ngữ nghiệp vụ với tên cột vật lý. Xung đột nghĩa giữa hai miền phải được giải bằng cách ghi nhận cả hai theo ngữ cảnh, theo đúng lesson 161, chứ ép một định nghĩa toàn công ty.

**Outcome.** Đạt độ phủ quyền sở hữu có thẩm quyền và ghi nhận được một xung đột nghĩa giữa hai miền mà không ép một định nghĩa.

**Đánh giá.** Tầng *áp dụng*. Objective đo chất lượng quyền sở hữu chứ chỉ sự tồn tại của một trường. Kiểm bằng phép thử xác nhận; đạt khi chủ sở hữu được chính họ xác nhận ở ít nhất 80 phần trăm tài sản trọng yếu và xung đột nghĩa được ghi theo ngữ cảnh.

**Lab.** Gán năm vai cho toàn bộ tài sản trọng yếu. Gửi xác nhận tới từng chủ sở hữu và đếm tỉ lệ xác nhận. Chạy phép kiểm phát hiện đội hoặc người đã rời. Xây từ điển cho 15 thuật ngữ và gắn vào cột cùng chỉ số. Tìm một từ mang hai nghĩa ở hai miền và ghi nhận cả hai theo ngữ cảnh kèm cách phân biệt cho người tìm kiếm.

**Pitfalls.** Gán tự động người tạo bảng rồi coi là xong · gán chủ sở hữu là một phòng ban · ép một định nghĩa toàn công ty cho từ có hai nghĩa · lập từ điển mà không gắn vào cột nào.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chủ sở hữu được chính họ xác nhận ở ≥ 80% tài sản trọng yếu, phép kiểm phát hiện người đã rời chạy tự động, và xung đột nghĩa được ghi theo cả hai ngữ cảnh.

### Lesson 305 · Certification, deprecation and the expiry rule `TH`
**Prerequisites.** Lesson 304

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Chứng nhận là tín hiệu tin cậy mạnh nhất trong danh mục, nên nó là thứ dễ bị lạm dụng nhất. Năm trạng thái: bản nháp, đã kiểm, đã chứng nhận, đã khai tử, đã gỡ. Phạm vi chứng nhận phải nói rõ nó bảo đảm gì: tính đúng về ngữ nghĩa, tình trạng chất lượng và cam kết dịch vụ, quyền sở hữu, mức hỗ trợ, và ngày rà soát lại. **Chứng nhận không bao giờ hết hạn tạo ra niềm tin sai**, vì một tài sản được chứng nhận hai năm trước có thể đã đổi hoàn toàn; nên mỗi chứng nhận có ngày rà soát và có cơ chế tự hạ cấp khi quá hạn hoặc khi cam kết dịch vụ vỡ. Điều kiện chứng nhận lấy từ các module trước và phải kiểm được bằng máy, chứ dựa trên việc tài liệu đã điền đủ: **tự động chứng nhận chỉ vì tài liệu đầy đủ là một chế độ hỏng tự động chưa đạt**. Khai tử cần danh sách bên tiêu thụ, phương án thay thế, thời hạn và theo dõi mức dùng còn lại.

**Outcome.** Vận hành năm trạng thái với điều kiện chứng nhận kiểm được bằng máy và cơ chế tự hạ cấp khi quá hạn.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là chặn đúng và tự hạ cấp đúng. Kiểm bằng ba tài sản đi qua vòng đời; đạt khi tài sản thiếu điều kiện bị chặn chứng nhận, tài sản quá hạn tự hạ cấp, và tài sản khai tử không còn người dùng khi gỡ.

**Lab.** Dựng vòng đời năm trạng thái với danh mục điều kiện chứng nhận kiểm tự động, gồm tình trạng chất lượng từ M14C và quyền sở hữu đã xác nhận. Đưa ba tài sản qua vòng đời, trong đó một cái chỉ có tài liệu đầy đủ mà chưa đạt chất lượng và phải bị chặn. Đẩy đồng hồ qua ngày rà soát và chứng minh tự hạ cấp. Khai tử một tài sản với thời hạn và theo dõi mức dùng tới khi về không.

**Pitfalls.** Chứng nhận dựa trên tài liệu đầy đủ · chứng nhận không có ngày rà soát · gỡ tài sản khi còn người dùng · không nói rõ chứng nhận bảo đảm điều gì.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tài sản thiếu điều kiện bị chặn chứng nhận, tài sản quá ngày rà soát tự hạ cấp, và tài sản khai tử về không người dùng trước khi gỡ.

### Lesson 306 · Classification, retention and the enforcement boundary `LT`
**Prerequisites.** Lesson 305

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài đặt ra ranh giới mà module này không được vượt, và vượt nó là chế độ hỏng nguy hiểm nhất về mặt pháp lý. Phân loại gồm mức nhạy cảm, dữ liệu cá nhân và phân loại nghiệp vụ; lan truyền phân loại theo dòng dõi là một tính năng mạnh và cũng dễ sai, nên nó cần cơ chế ghi đè có kiểm soát ở nơi phép lan truyền cho kết quả không đúng. Gắn chính sách vào tài sản. **Danh mục ghi lại bằng chứng và trạng thái; việc cưỡng chế quyền truy cập, che dữ liệu và xoá theo thời hạn do hệ có thẩm quyền thực hiện.** Tuyên bố danh mục cưỡng chế điều nó chỉ đang ghi lại là một tuyên bố sai và là một trong những chế độ hỏng tự động chưa đạt; hậu quả là tổ chức tin rằng một nghĩa vụ đã được thực hiện trong khi chưa. Một rủi ro riêng của danh mục: lưu giá trị mẫu hoặc thống kê phân bố có thể làm lộ dữ liệu nhạy cảm, nên phần đó cũng phải có phân loại và kiểm soát truy cập.

**Outcome.** Nêu chính xác ranh giới giữa ghi nhận với cưỡng chế và thiết kế lan truyền phân loại có cơ chế ghi đè.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết chốt phần quản trị. Kiểm bằng bài phân định; đạt khi phân đúng ít nhất tám trong mười nghĩa vụ vào ghi nhận hay cưỡng chế và thiết kế lan truyền có ghi đè cùng phép kiểm rò rỉ giá trị mẫu.

**Lab.** Cho mười nghĩa vụ quản trị cụ thể. Phân từng cái vào ghi nhận hay cưỡng chế và nêu hệ nào thực hiện. Thiết kế lan truyền phân loại theo dòng dõi cho một miền, kèm cơ chế ghi đè. Tìm ba chỗ phép lan truyền cho kết quả sai. Rà phần giá trị mẫu và thống kê trong danh mục, phân loại chúng và đặt kiểm soát truy cập.

**Pitfalls.** Nói danh mục đang cưỡng chế chính sách · lan truyền phân loại mà không có ghi đè · lưu giá trị mẫu không phân loại · coi phân loại là việc một lần chứ trạng thái phải rà lại.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân đúng ≥ 8/10 nghĩa vụ giữa ghi nhận và cưỡng chế, lan truyền phân loại có ghi đè cùng ba ca sai được tìm ra, và giá trị mẫu có phân loại cùng kiểm soát truy cập.

### Lesson 307 · Metadata control-plane capstone `DA`
**Prerequisites.** Lesson 306

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Bài dự án khép module và khép cả Phase 7, lấy đúng yêu cầu capstone của hợp đồng nguồn: bổ sung một mặt phẳng điều khiển siêu dữ liệu cho nền tảng đã dựng. Nộp gồm bảy hạng mục: một danh mục được chọn để cài đặt; thu thập từ khung biến đổi, bộ điều phối, kho dữ liệu, nền tảng dòng sự kiện và công cụ báo cáo; dòng dõi ở mức tập dữ liệu, cột, công việc, bảng điều khiển và chỉ số, mỗi cạnh có xuất xứ; miền cùng sản phẩm dữ liệu, từ điển, chủ sở hữu, phân loại và chứng nhận; nối với tình trạng chất lượng cùng cam kết dịch vụ ở M14C và phân tích ảnh hưởng khi có sự cố; luồng tìm kiếm, xin quyền và khai tử; và bảng theo dõi cùng sổ tay cho chính đường thu thập siêu dữ liệu. Chỉ số phục vụ của siêu dữ liệu phải đo được: độ phủ, độ tươi thu thập, tỉ lệ danh tính mồ côi hoặc trùng, độ phủ dòng dõi trên đường trọng yếu, tỉ lệ tìm kiếm không ra kết quả, và mức dùng tài sản đã chứng nhận.

**Outcome.** Nộp mặt phẳng điều khiển siêu dữ liệu đủ bảy hạng mục với chỉ số phục vụ đo được và không vi phạm sáu điều kiện tự động chưa đạt.

**Đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module thành một hệ vận hành. Kiểm bằng tiêm bốn tình huống cộng rà chỉ số; đạt khi bốn tình huống giữ được sự không chắc chắn hiện rõ và phục hồi an toàn, và sáu chỉ số phục vụ có số đo.

**Lab.** Dựng mặt phẳng điều khiển theo bảy hạng mục. Đo sáu chỉ số phục vụ. Người chấm tiêm bốn tình huống: đổi tên một tài sản, một câu lệnh sinh động mà bộ phân tích không đọc được, nguồn thu thập mất kết nối, và hai danh tính trùng. Với mỗi cái, chứng minh phần không chắc chắn vẫn hiện rõ và phục hồi không mất chú thích thủ công.

**Pitfalls.** Báo cáo dòng dõi suy ra như sự thật · tuyên bố danh mục cưỡng chế quyền truy cập · thu thập bằng quyền sản xuất quá rộng · dựng lại danh mục mà không sao lưu và không di trú danh tính.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Bảy hạng mục đầy đủ, sáu chỉ số phục vụ có số đo, bốn tình huống tiêm đều giữ sự không chắc chắn hiện rõ và phục hồi không mất chú thích.

### Lesson 308 · Gate 7 - defend a lineage claim and prove completeness `KT`
**Prerequisites.** Lesson 307

**In-class (180 phút).** 135 phút làm bài độc lập · 45 phút chữa bài và phân tích lỗi theo nhóm

**Learn.** Cổng của Phase 7, cổng lớn nhất chương trình vì nó phủ bốn module và 78 bài. Bài kiểm nạp dữ liệu ở M14B, biến đổi cùng điều phối ở M14, chất lượng cùng tin cậy ở M14C, và siêu dữ liệu cùng quản trị ở M14D. Không có nội dung mới.

**Outcome.** Chứng minh tính đầy đủ từ nguồn tới đích bằng đối soát, bảo vệ một khẳng định về dòng dõi trước chất vấn, và phục hồi một sự cố dữ liệu an toàn.

**Đánh giá.** Tầng *đánh giá*. Cổng đo năng lực chứng minh và vận hành dưới chất vấn, nên hình thức là thực hành tại chỗ cộng bảo vệ trực tiếp.

**Lab.** Buổi 180 phút: 135 phút làm bài độc lập, 45 phút chữa bài. Bài chấm sáu phần: A (20đ) chứng minh tính đầy đủ từ nguồn tới tầng phục vụ bằng thang đối soát, nêu rõ tổng thể, cửa sổ, phép kiểm và dung sai · B (20đ) trình chứng minh bảy phần cho một mô hình tăng dần và chạy hai ô của ma trận chế độ hỏng tại chỗ · C (15đ) một lỗi thầm lặng được tiêm; định vị phạm vi ảnh hưởng bằng dòng dõi và chạy phục hồi an toàn · D (20đ) bảo vệ một khẳng định về dòng dõi: cạnh này đến từ đâu, độ tin cậy bao nhiêu, phần nào chưa biết · E (15đ) giải thích ranh giới giữa danh mục ghi nhận và hệ cưỡng chế cho ba nghĩa vụ · F (10đ) rà một bộ quy tắc chất lượng và tìm phép kiểm có phạm vi che dữ liệu hỏng.

**Pitfalls.** Dùng mọi việc xanh làm bằng chứng đầy đủ · trình bày cạnh suy ra như sự thật · công bố bản sửa trước khi đối soát · tuyên bố danh mục cưỡng chế chính sách.

**Self-study (2,4 giờ).** Không có bài tự học. Nếu không đạt, theo phụ lục khắc phục khi không đạt cổng

**Done when.** Đạt ≥ 70/100, phần A và D đều ≥ 60%. Tuyên bố đầy đủ dựa trên lấy mẫu thì phần A bằng không; trình bày cạnh suy ra như sự thật mà không nêu xuất xứ thì phần D bằng không.

# MODULE M15 · DISTRIBUTED SYSTEMS FUNDAMENTALS

**Phase 8 · Lessons 309–320 · 24 giờ**

| | |
|---|---|
| **Objective cấp module** | Với mỗi bảo đảm được tuyên bố, nêu được giả định hệ thống nó dựa vào và chế độ hỏng nó không chịu được |
| **Tiền đề** | M5 · M6 · M9 · M10 · M14 |
| **Exit criterion** | Giải thích bầu chọn người dẫn, sao chép nhật ký, chốt theo số đông và cách chặn chia rẽ; mọi thiết kế có thử lại, luỹ đẳng, thẻ chặn và hết giờ, không dùng cụm từ đúng một lần theo nghĩa mơ hồ |
| **Kỹ năng SFIA** | `SYSP` mức 5 · `ARCH` mức 4 |
| **Chế độ hỏng** | Coi hết giờ là bằng chứng bên kia đã hỏng, và nói số đông thì suy ra tuần tự hoá được |

Module đặt nền cho ba module còn lại của phase, và nó có một câu bản lề chi phối mọi bài: **hết giờ không phải một lỗi, nó là một trạng thái không biết**. Bên kia có thể đã làm xong, có thể chưa làm, có thể đang làm; thiết kế phải đúng ở cả ba khả năng.

Hai nhầm lẫn bị bác bỏ ngay và được kiểm lại ở cổng: số đông không tự suy ra tuần tự hoá được, và đồng hồ treo tường không dùng để xác lập thứ tự.

Đồng thuận học sâu ở một thuật toán, thuật toán còn lại chỉ tới mức khái niệm.

### Lesson 309 · The formal model - safety, liveness and what the network may do `LT`
**Prerequisites.** Module 15: M14

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài mở module bằng một mô hình đủ chặt để lập luận, vì bàn về hệ phân tán bằng trực giác dẫn tới kết luận sai. Mô hình gồm nút, tiến trình, thông điệp và trạng thái; lịch sử thao tác gồm lời gọi và phản hồi, và khoảng giữa hai mốc đó là chỗ mọi sự không chắc chắn nằm. Hai loại tính chất phải tách: an toàn nghĩa là việc xấu không bao giờ xảy ra, sống động nghĩa là việc tốt cuối cùng sẽ xảy ra; **hy sinh an toàn để đổi lấy sống động là một quyết định, không phải một tối ưu hoá**, và nó phải được nói ra. Giả định về mạng và tiến trình: đồng bộ, bán đồng bộ, hay bất đồng bộ hoàn toàn; trong mô hình bất đồng bộ hoàn toàn có những việc không làm được, và trực giác về giới hạn đó giải thích vì sao mọi hệ thật đều thêm giả định về thời gian. Bảo đảm phải phát biểu theo thứ khách hàng quan sát được. Tách nhất quán của hệ sao chép khỏi mức cô lập của giao dịch ở lesson 142.

**Outcome.** Phát biểu một bảo đảm theo thứ khách hàng quan sát được và phân loại năm mệnh đề vào an toàn hay sống động.

**Đánh giá.** Tầng *hiểu*. Bài mở module, đặt từ vựng cho toàn phase. Kiểm bằng bài phân loại cộng bài phát biểu lại; đạt khi phân đúng ít nhất bốn trong năm và bảo đảm được phát biểu bằng quan sát của khách hàng chứ bằng cơ chế nội bộ.

**Lab.** Cho năm mệnh đề về một hệ lưu trữ; phân loại an toàn hay sống động và nêu giả định mỗi cái dựa vào. Lấy ba tuyên bố kiểu tiếp thị về một hệ thật và phát biểu lại bằng thứ khách hàng quan sát được. Chỉ ra chỗ nào tuyên bố gốc trộn nhất quán của hệ với mức cô lập giao dịch.

**Pitfalls.** Bàn về hệ phân tán bằng trực giác về trường hợp thuận lợi · phát biểu bảo đảm bằng cơ chế nội bộ · trộn nhất quán với mức cô lập · bỏ qua việc phải nêu giả định về mạng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân đúng ≥ 4/5 mệnh đề kèm giả định, và ba tuyên bố được phát biểu lại theo quan sát của khách hàng.

### Lesson 310 · Failure modes and why a timeout is not a failure `TH`
**Prerequisites.** Lesson 309

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài chốt câu bản lề của module bằng thực nghiệm. Các chế độ hỏng phải phân biệt: dừng hẳn, dừng rồi khởi động lại, bỏ sót thông điệp, phân vùng mạng, và trì hoãn cùng nhân bản cùng đảo thứ tự; hành vi tuỳ tiện chỉ cần biết là có. Từ đó suy ra điều quan trọng nhất: khi một lời gọi hết giờ, ta không biết bên kia đã thực hiện hay chưa, **nên mọi thao tác có thể bị gọi lại phải luỹ đẳng** theo lesson 105. Phản hồi chậm tới sau khi đã hết giờ là ca cụ thể: bên gọi đã coi như thất bại và đã thử lại, nên tác dụng phụ xảy ra hai lần. Phân vùng mạng khác nút chết ở một điểm quyết định: nút bên kia vẫn sống và vẫn đang phục vụ, nên có hai bên cùng tin mình đúng. Bộ phát hiện hỏng chỉ đoán, và mọi bộ phát hiện đều có thể đoán sai theo cả hai chiều.

**Outcome.** Tái hiện năm chế độ hỏng trên một dịch vụ nhỏ và chứng minh hành vi đúng ở cả ba khả năng sau khi hết giờ.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là trạng thái đúng bất kể kết cục thật của lời gọi. Kiểm bằng phép thử tiêm; đạt khi trạng thái cuối đúng ở cả ba khả năng và không tác dụng phụ nào xảy ra hai lần.

**Lab.** Dựng một dịch vụ có tác dụng phụ ghi được. Tiêm năm chế độ hỏng bằng lớp mạng giả lập: chậm, mất gói, nhân đôi, đảo thứ tự, và phân vùng. Với ca hết giờ, tạo cả ba kết cục thật và chứng minh trạng thái cuối đúng ở cả ba. Đo số lần tác dụng phụ lặp trước và sau khi thêm khoá chống trùng.

**Pitfalls.** Coi hết giờ là bên kia đã hỏng · thử lại thao tác không luỹ đẳng · giả định mất gói và chậm là một · tin bộ phát hiện hỏng nói đúng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Trạng thái cuối đúng ở cả ba kết cục sau hết giờ, và không tác dụng phụ nào xảy ra hai lần qua 1.000 lượt tiêm.

### Lesson 311 · Time and order - wall clock, monotonic clock and logical clocks `TH`
**Prerequisites.** Lesson 310

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Đồng hồ là công cụ đo thời gian, không phải công cụ xác lập thứ tự, và nhầm hai việc này gây mất dữ liệu im lặng. Đồng hồ treo tường có thể nhảy lùi khi đồng bộ, nên hai sự kiện có dấu thời gian nhỏ hơn chưa chắc xảy ra trước. Đồng hồ đơn điệu chỉ đo khoảng, dùng được cho hết giờ nhưng không so được giữa hai máy. Đồng hồ logic gán số đếm tăng theo quan hệ xảy ra trước; đồng hồ véctơ giữ một số đếm cho mỗi nút nên phân biệt được hai sự kiện đồng thời với hai sự kiện có quan hệ nhân quả, điều đồng hồ logic đơn không làm được. **Chiến lược bản ghi có dấu thời gian lớn nhất thắng làm mất cập nhật khi đồng hồ lệch**, và đây là ca phải tái hiện bằng số. Chính sách giải quyết xung đột phải chọn tường minh chứ để mặc định, và mọi chính sách đều mất thông tin theo một cách nào đó.

**Outcome.** Chứng minh bằng thực nghiệm rằng chiến lược theo dấu thời gian làm mất cập nhật, và thay bằng đồng hồ logic.

**Đánh giá.** Tầng *phân tích*. Objective đòi nhận ra một lỗi không báo lỗi và sửa bằng cơ chế đúng. Kiểm bằng thí nghiệm lệch đồng hồ; đạt khi số cập nhật bị mất được định lượng và bản dùng đồng hồ véctơ phát hiện đúng mọi cặp sự kiện đồng thời.

**Lab.** Dựng kho khoá giá trị hai bản sao. Đặt lệch đồng hồ giữa hai nút. Ghi song song và đếm số cập nhật bị mất với chiến lược dấu thời gian lớn nhất thắng. Cài đồng hồ logic rồi đồng hồ véctơ; chứng minh đồng hồ véctơ phân biệt được đồng thời với nhân quả. Chọn một chính sách giải quyết xung đột tường minh và nêu nó mất thông tin gì.

**Pitfalls.** Dùng đồng hồ treo tường để xác lập thứ tự · dùng đồng hồ đơn điệu để so giữa hai máy · để chính sách xung đột theo mặc định · nghĩ đồng hồ logic đơn phát hiện được đồng thời.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Số cập nhật bị mất được định lượng, đồng hồ véctơ phát hiện đúng mọi cặp đồng thời, và chính sách xung đột nêu rõ thông tin bị mất.

### Lesson 312 · Replication - single leader, multi leader, leaderless `LT`
**Prerequisites.** Lesson 311

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Ba kiểu sao chép cho ba mô hình xung đột khác nhau, và chọn kiểu là chọn loại vấn đề mình sẵn sàng xử lý. Một người dẫn: mọi phép ghi qua một nút nên không có xung đột ghi, đổi lại người dẫn là điểm nghẽn và là điểm hỏng; sao chép đồng bộ không mất dữ liệu khi chuyển đổi dự phòng nhưng chậm, sao chép bất đồng bộ nhanh nhưng **mất phần nhật ký chưa kịp truyền khi người dẫn chết**, và lượng mất đó bằng đúng độ trễ sao chép ở lesson 143. Nhiều người dẫn: ghi được ở nhiều nơi nên chịu được phân vùng tốt hơn, đổi lại phải giải quyết xung đột và phải chọn cách hội tụ. Không người dẫn: ghi vào nhiều bản sao và đọc từ nhiều bản sao, dùng số đông để bù; sửa khi đọc và chống lệch nền chỉ cần biết là có. Vị trí nhật ký, độ trễ và hành vi khi chuyển đổi dự phòng phải trả lời được cho cả ba kiểu.

**Outcome.** Chọn kiểu sao chép cho ba bối cảnh và định lượng lượng dữ liệu có thể mất khi chuyển đổi dự phòng.

**Đánh giá.** Tầng *đánh giá*. Objective đòi nối lựa chọn với một con số về rủi ro mất dữ liệu. Kiểm bằng ba bối cảnh cộng phép đo; đạt khi mỗi lựa chọn kèm lượng mất tối đa tính được từ độ trễ đo được.

**Lab.** Dựng bản sao một người dẫn ở cả chế độ đồng bộ và bất đồng bộ. Đo độ trễ sao chép dưới tải. Giết người dẫn và đếm số phép ghi đã báo thành công nhưng mất. Cho ba bối cảnh khác nhau về yêu cầu mất dữ liệu và độ trễ; chọn kiểu sao chép và tính lượng mất tối đa cho từng cái.

**Pitfalls.** Dùng sao chép bất đồng bộ rồi tuyên bố không mất dữ liệu · chọn nhiều người dẫn mà chưa có chính sách xung đột · bỏ qua độ trễ sao chép khi tính rủi ro · coi bản sao đọc là bản sao lưu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba bối cảnh có lựa chọn kèm lượng mất tối đa tính từ độ trễ đo được, và số phép ghi mất khi giết người dẫn được đếm thật.

### Lesson 313 · Partitioning, consistent hashing and rebalancing `TH`
**Prerequisites.** Lesson 312

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Chia dữ liệu ra nhiều nút để vượt giới hạn một máy, và ba quyết định đi kèm. Chia theo khoảng giá trị cho phép quét theo khoảng hiệu quả nhưng dễ tạo phân vùng nóng khi khoá phân bố lệch. Chia theo băm rải đều hơn nhưng mất khả năng quét theo khoảng. Băm nhất quán giảm lượng dữ liệu phải di chuyển khi thêm hoặc bớt nút, và nút ảo làm phân bố đều hơn. **Phân vùng nóng là chế độ hỏng chính**: một khoá chiếm phần lớn lưu lượng thì thêm nút không giúp gì, vì mọi yêu cầu của khoá đó vẫn về một nơi; ba cách xử lý và đánh đổi từng cách. Tái cân bằng là thao tác nặng và phải có giới hạn tốc độ, nếu không nó làm sập hệ đang phục vụ. Nối với phân vùng trong một cơ sở dữ liệu ở lesson 144: ở đây phân vùng nằm giữa các máy nên thêm chi phí mạng và chi phí di chuyển.

**Outcome.** Đo phân bố tải qua ba cách chia và xử lý được một phân vùng nóng có bằng chứng.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là độ lệch tải giảm có số đo. Kiểm bằng phép đo phân bố; đạt khi ba cách chia có số đo độ lệch, lượng dữ liệu di chuyển khi thêm nút được đo, và phân vùng nóng giảm lệch sau khi xử lý.

**Lab.** Cài ba cách chia trên cùng tập khoá thật có phân bố lệch. Đo độ lệch tải giữa các phân vùng. Thêm một nút và đo lượng dữ liệu phải di chuyển ở từng cách. Tạo một khoá nóng chiếm phần lớn lưu lượng, thử ba cách xử lý và đo lại. Chạy tái cân bằng có giới hạn tốc độ trong lúc hệ đang phục vụ và đo ảnh hưởng.

**Pitfalls.** Chia theo băm rồi vẫn cần quét theo khoảng · thêm nút để chữa phân vùng nóng · tái cân bằng không giới hạn tốc độ · đo phân bố bằng khoá sinh ngẫu nhiên đều thay vì khoá thật.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba cách chia có số đo độ lệch và lượng dữ liệu di chuyển, và phân vùng nóng giảm độ lệch sau khi xử lý.

### Lesson 314 · Consistency models named by what the client observes `LT`
**Prerequisites.** Lesson 313

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Năm mô hình nhất quán, đặt tên theo thứ khách hàng quan sát được chứ theo cơ chế bên trong. Tuần tự hoá được: mọi thao tác trông như xảy ra tức thời tại một thời điểm giữa lời gọi và phản hồi, đây là mô hình mạnh nhất và đắt nhất. Tuần tự: mọi nút thấy cùng một thứ tự nhưng thứ tự đó không nhất thiết khớp thời gian thật. Nhân quả: các thao tác có quan hệ nhân quả được thấy đúng thứ tự, thao tác đồng thời thì không ràng buộc. Đọc thấy phép ghi của chính mình: bảo đảm yếu nhưng là thứ người dùng thật hay kỳ vọng nhất. Cuối cùng nhất quán: chỉ hứa hội tụ khi ngừng ghi, nên **nó phải đi kèm một hợp đồng về mức cũ tối đa**, nếu không nó là một lời hứa rỗng. Định lý đánh đổi chỉ áp dụng khi có phân vùng; khi không có phân vùng thì đánh đổi thật là giữa độ trễ với nhất quán, và đó mới là trường hợp thường gặp hằng ngày.

**Outcome.** Xếp năm mô hình theo độ mạnh và chỉ ra bảo đảm nào một hệ cho trước thật sự cung cấp.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết chuẩn bị cho hai bài về số đông và đồng thuận. Kiểm bằng bài phân tích bốn lịch sử thao tác; đạt khi xác định đúng mô hình bị vi phạm ở ít nhất ba và nêu được đánh đổi khi không có phân vùng.

**Lab.** Cho bốn lịch sử thao tác của một thanh ghi; với mỗi cái, xác định mô hình nào bị vi phạm và giải thích bằng lời gọi cùng phản hồi cụ thể. Lấy tài liệu của hai hệ thật và phát biểu lại bảo đảm của chúng theo năm mô hình. Với một hệ hứa cuối cùng nhất quán, tìm hợp đồng về mức cũ tối đa; nếu không có thì ghi rõ là không có.

**Pitfalls.** Dùng định lý đánh đổi để biện minh cho mọi quyết định · nói cuối cùng nhất quán mà không kèm mức cũ tối đa · nhầm tuần tự với tuần tự hoá được · đặt tên mô hình theo cơ chế bên trong.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Xác định đúng mô hình bị vi phạm ở ≥ 3/4 lịch sử, và hai hệ thật được phát biểu lại bảo đảm theo năm mô hình.

### Lesson 315 · Quorum reasoning, and why a quorum is not linearizability `TH`
**Prerequisites.** Lesson 314

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Số đông là một kỹ thuật giao nhau giữa tập ghi và tập đọc, và hiểu đúng giới hạn của nó là mục tiêu chính của bài. Với tổng số bản sao, số bản sao phải ghi, và số bản sao phải đọc, điều kiện giao nhau bảo đảm phép đọc chạm ít nhất một bản sao có phiên bản mới nhất. Nhưng chạm được không bằng nhận ra: **phép đọc chỉ trả đúng nếu có cách so phiên bản và có cơ chế sửa**, nên số đông không tự suy ra tuần tự hoá được. Ba ca phá vỡ trực giác về số đông: phép ghi hỏng giữa chừng nên một số bản sao có giá trị mới còn số khác thì không, mà không có ai quay lui; số đông lỏng cùng trao tay gợi ý làm tập giao nhau không còn bảo đảm; và hai phép đọc liên tiếp có thể thấy giá trị mới rồi lại thấy giá trị cũ. Sửa khi đọc và chống lệch nền ở mức khái niệm.

**Outcome.** Tái hiện ca số đông giao nhau mà phép đọc vẫn trả giá trị cũ, và giải thích cần thêm gì.

**Đánh giá.** Tầng *phân tích*. Objective nhắm vào một kết luận sai rất phổ biến. Kiểm bằng ba ca tái hiện; đạt khi cả ba được tái hiện bằng dữ liệu và nêu đúng cơ chế còn thiếu cho từng ca.

**Lab.** Dựng kho khoá giá trị không người dẫn với tham số số đông cấu hình được. Tái hiện ba ca: phép ghi hỏng giữa chừng, hai phép đọc liên tiếp thấy mới rồi cũ, và số đông lỏng làm mất bảo đảm giao nhau. Với mỗi ca, nêu cơ chế còn thiếu. Bật sửa khi đọc và đo nó giảm ca nào, không giảm ca nào.

**Pitfalls.** Kết luận số đông suy ra tuần tự hoá được · bật số đông lỏng mà không nói rõ mất bảo đảm gì · không có cách so phiên bản giữa các bản sao · tin sửa khi đọc chữa được mọi ca.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba ca được tái hiện bằng dữ liệu, mỗi ca nêu đúng cơ chế còn thiếu, và hiệu lực của sửa khi đọc được đo theo từng ca.

### Lesson 316 · Consensus - the replicated log, term, election and commit `TH`
**Prerequisites.** Lesson 315

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Đồng thuận giải bài toán mà số đông không giải được: làm cho nhiều nút đồng ý về một chuỗi thao tác theo đúng một thứ tự. Học sâu một thuật toán, thuật toán còn lại chỉ tới mức khái niệm. Cấu trúc: một nhật ký được sao chép, mỗi mục có chỉ số và nhiệm kỳ; một người dẫn được bầu cho mỗi nhiệm kỳ; mục được chốt khi đã sao chép tới số đông; nút theo sau áp dụng theo đúng thứ tự đã chốt. Ba tính chất an toàn phải phát biểu được và phải kiểm được bằng thí nghiệm. Nhiệm kỳ là cơ chế chặn chia rẽ: một người dẫn cũ quay lại với nhiệm kỳ nhỏ hơn sẽ bị từ chối, nên **chia rẽ được chặn bằng nhiệm kỳ chứ bằng việc phát hiện nhanh**. Thay đổi thành viên cụm và vì sao nó khó. Khác biệt với chốt hai pha ở lesson 318: đồng thuận không chặn khi một nút chết vì số đông vẫn tiến được.

**Outcome.** Cài phần bầu chọn và sao chép nhật ký, rồi giữ được ba tính chất an toàn qua các lần giết nút.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là bất biến an toàn giữ được dưới lỗi ngẫu nhiên. Kiểm bằng phép thử hỗn loạn; đạt khi ba tính chất an toàn không bị vi phạm lần nào qua 200 chu kỳ giết và khôi phục nút.

**Lab.** Cài bầu chọn người dẫn và sao chép nhật ký cho cụm năm nút. Chạy 200 chu kỳ giết ngẫu nhiên một hoặc hai nút rồi cho khôi phục, kèm phân vùng mạng ngắn. Sau mỗi chu kỳ, kiểm ba tính chất an toàn. Tái hiện ca người dẫn cũ quay lại và chứng minh nó bị từ chối bằng nhiệm kỳ. Vẽ trình tự một lần chốt đi qua một lần người dẫn chết.

**Pitfalls.** Bầu người dẫn mà không so nhật ký nên mất mục đã chốt · dùng thời gian phát hiện nhanh thay cho nhiệm kỳ · chỉ kiểm ở trường hợp thuận lợi · nhầm đã sao chép với đã chốt.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba tính chất an toàn không bị vi phạm qua 200 chu kỳ, và ca người dẫn cũ quay lại bị từ chối bằng nhiệm kỳ.

### Lesson 317 · Leases, fencing tokens and the returning old leader `TH`
**Prerequisites.** Lesson 316

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Khoá phân tán là chỗ trực giác sai nhiều nhất, nên bài này tái hiện ca hỏng kinh điển. Hợp đồng thuê là một khoá có hạn, và nó dựa vào đồng hồ; nhưng tiến trình giữ hợp đồng thuê có thể bị tạm dừng lâu hơn hạn, chẳng hạn vì bộ dọn rác hoặc vì máy bị treo, nên nó tỉnh dậy và vẫn tưởng mình đang giữ khoá trong khi khoá đã cấp cho người khác. Hậu quả: hai tiến trình cùng ghi và dữ liệu hỏng. **Hợp đồng thuê một mình không đủ, phải có thẻ chặn**: mỗi lần cấp khoá kèm một số tăng dần, và tài nguyên ở đích từ chối mọi yêu cầu mang số nhỏ hơn số lớn nhất đã thấy. Điểm quan trọng là thẻ chặn phải được cưỡng chế ở phía tài nguyên chứ ở phía khách, vì khách đang là bên nhầm lẫn. Khoá chống trùng cùng bộ nhớ kết quả có thời hạn giữ. Thử lại khi không biết kết cục theo lesson 310.

**Outcome.** Tái hiện ca hai tiến trình cùng tưởng mình giữ khoá và chặn nó bằng thẻ chặn cưỡng chế ở đích.

**Đánh giá.** Tầng *áp dụng*. Objective có một ca hỏng cụ thể phải tái hiện được trước khi sửa. Kiểm bằng phép thử tạm dừng tiến trình; đạt khi ca hỏng được tái hiện kèm bằng chứng dữ liệu sai, và bản có thẻ chặn từ chối đúng mọi yêu cầu cũ.

**Lab.** Dựng dịch vụ cấp hợp đồng thuê và một tài nguyên dùng chung. Tạm dừng tiến trình giữ khoá lâu hơn hạn thuê rồi cho chạy tiếp; ghi lại dữ liệu hỏng. Thêm thẻ chặn tăng dần và cưỡng chế ở phía tài nguyên; chạy lại và chứng minh yêu cầu cũ bị từ chối. Thử cưỡng chế ở phía khách và chỉ ra vì sao không đủ.

**Pitfalls.** Dùng hợp đồng thuê mà không có thẻ chặn · cưỡng chế thẻ chặn ở phía khách · đặt hạn thuê ngắn hơn thời gian tạm dừng có thể xảy ra · giả định tiến trình không bao giờ bị tạm dừng lâu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ca hai tiến trình cùng ghi được tái hiện kèm bằng chứng dữ liệu sai, và bản có thẻ chặn từ chối đúng 100% yêu cầu mang số cũ.

### Lesson 318 · Distributed transactions - two-phase commit against saga and outbox `TH`
**Prerequisites.** Lesson 317

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba cách giữ tính nhất quán qua nhiều hệ, với ba mô hình hỏng khác nhau. Chốt hai pha: điều phối viên hỏi mọi bên sẵn sàng chưa rồi mới ra lệnh chốt; đúng về mặt nguyên tử nhưng **chặn khi điều phối viên chết sau pha chuẩn bị**, vì các bên đã khoá tài nguyên và không ai dám tự quyết. Chuỗi bù trừ: chia thành nhiều bước nhỏ, mỗi bước có một thao tác bù nghĩa; nó không nguyên tử nên có trạng thái trung gian nhìn thấy được, và phải chấp nhận điều đó tường minh. Hộp thư đi theo lesson 109: ghi dữ liệu và ghi ý định gửi trong cùng một giao dịch cục bộ, rồi một tiến trình riêng đọc hộp thư và gửi đi; nó biến bài toán hai hệ thành bài toán một giao dịch cộng một lần gửi có thể lặp. Kết luận thực dụng dùng lại ở M16 và M17: **giao nhận ít nhất một lần cộng tác dụng phụ luỹ đẳng thực tế hơn theo đuổi nguyên tử xuyên hệ**.

**Outcome.** So ba cách trên cùng bài toán và lập ma trận hỏng tại mọi ranh giới cho từng cách.

**Đánh giá.** Tầng *đánh giá*. Objective đòi so ba mô hình hỏng chứ ba cách cài đặt. Kiểm bằng ma trận hỏng; đạt khi mỗi cách có hành vi ghi rõ tại mọi ranh giới hỏng và ca điều phối viên chết được tái hiện thật.

**Lab.** Cài cùng một quy trình đặt hàng gồm thanh toán và trừ kho theo cả ba cách. Với mỗi cách, giết tiến trình tại từng ranh giới và ghi trạng thái cuối. Tái hiện ca điều phối viên chết sau pha chuẩn bị và đo thời gian tài nguyên bị khoá. Lập ma trận hỏng ba cách nhân các ranh giới. Chọn một cách cho một bối cảnh và nêu trạng thái trung gian mà nghiệp vụ phải chấp nhận.

**Pitfalls.** Dùng chốt hai pha mà không tính ca điều phối viên chết · viết thao tác bù bằng cách hoàn tác kỹ thuật thay vì bù nghĩa nghiệp vụ · gửi thông điệp ngoài giao dịch cục bộ · tuyên bố nguyên tử xuyên hệ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ma trận hỏng đầy đủ cho cả ba cách tại mọi ranh giới, ca điều phối viên chết được tái hiện kèm thời gian khoá đo được.

### Lesson 319 · Overload, backpressure and cascading failure `TH`
**Prerequisites.** Lesson 318

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hệ phân tán hỏng theo dây chuyền, và cơ chế lan truyền phải hiểu để chặn. Chuỗi điển hình: một phụ thuộc chậm lại, bên gọi giữ kết nối lâu hơn, bể kết nối cạn, hàng đợi dài ra, hết giờ kích hoạt, thử lại làm tải tăng thêm, rồi phụ thuộc sập hẳn; **thử lại là chất xúc tác của sập dây chuyền** chứ một biện pháp phòng thủ, nên nó cần ngân sách. Bốn cơ chế chặn: áp lực ngược theo lesson 27, ngắt mạch, vách ngăn để một phụ thuộc hỏng không ăn hết tài nguyên, và suy giảm có kiểm soát. Loại bỏ tải có chủ ý tốt hơn sập toàn bộ: từ chối sớm một phần yêu cầu giữ cho phần còn lại vẫn chạy. Cơn bão thử lại đồng bộ do nhiều khách cùng lùi theo cùng công thức, chặn bằng nhiễu ngẫu nhiên. Sấm sét khi cùng lúc hàng loạt yêu cầu tới một tài nguyên vừa hết đệm.

**Outcome.** Tái hiện một lần sập dây chuyền và chặn nó bằng bốn cơ chế, có số đo trước sau.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là hệ giữ được một phần năng lực thay vì sập toàn bộ. Kiểm bằng phép thử tải có phụ thuộc chậm; đạt khi bản chưa phòng thủ sập hoàn toàn và bản có phòng thủ giữ được tỉ lệ phục vụ trên ngưỡng.

**Lab.** Dựng ba dịch vụ nối nhau. Làm dịch vụ cuối chậm dần và đo chuỗi lan truyền: thời gian giữ kết nối, độ sâu hàng đợi, tỉ lệ hết giờ, tỉ lệ thử lại. Ghi lại thời điểm sập toàn bộ. Thêm lần lượt bốn cơ chế và đo đóng góp của từng cái. Tái hiện cơn bão thử lại đồng bộ rồi chặn bằng nhiễu ngẫu nhiên.

**Pitfalls.** Thử lại không có ngân sách · dùng một bể kết nối chung cho mọi phụ thuộc · lùi dần không có nhiễu · coi sập toàn bộ và suy giảm một phần là như nhau.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bản chưa phòng thủ sập hoàn toàn còn bản có phòng thủ giữ tỉ lệ phục vụ trên ngưỡng, và đóng góp của từng cơ chế có số đo.

### Lesson 320 · History analysis project - judge a guarantee from evidence `DA`
**Prerequisites.** Lesson 319

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Bài dự án khép module. Cho một tập lịch sử thao tác thu được từ nhiều khách hàng chạy song song trên một kho dữ liệu, mỗi bản ghi có lời gọi, phản hồi và dấu thời gian cục bộ. Nhiệm vụ: xác định lịch sử đó vi phạm mô hình nhất quán nào và chứng minh bằng một chuỗi thao tác cụ thể, chứ nói cảm nhận. Viết một bộ kiểm lịch sử cho một thanh ghi đơn giản và **nêu rõ giới hạn của chính bộ kiểm đó**: nó kiểm được gì, không kiểm được gì, và vì sao không được coi kết quả của nó là một chứng minh đầy đủ về hệ. Phần hai: chạy thử nghiệm của chính mình trên kho khoá giá trị đã dựng ở các bài trước, tiêm phân vùng và lệch đồng hồ, thu lịch sử rồi phân tích. Nộp kèm một bảng ghi với mỗi bảo đảm được tuyên bố thì giả định nào phải đúng và chế độ hỏng nào phá vỡ nó.

**Outcome.** Xác định đúng mô hình bị vi phạm trên bốn lịch sử và nêu giới hạn của bộ kiểm mình viết.

**Đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module thành một năng lực lập luận có bằng chứng. Kiểm bằng bốn lịch sử cộng rà soát bộ kiểm; đạt khi xác định đúng ít nhất ba kèm chuỗi thao tác chứng minh, và giới hạn của bộ kiểm được nêu rõ.

**Lab.** Nhận bốn lịch sử, trong đó một lịch sử hợp lệ. Viết bộ kiểm cho thanh ghi. Với mỗi lịch sử vi phạm, chỉ ra chuỗi thao tác cụ thể chứng minh. Chạy thử nghiệm riêng có tiêm phân vùng và lệch đồng hồ, thu lịch sử và phân tích. Nộp bảng bảo đảm với giả định và chế độ hỏng phá vỡ.

**Pitfalls.** Tuyên bố đã kiểm chứng toàn hệ từ một bộ kiểm nhỏ · kết luận vi phạm mà không chỉ ra chuỗi thao tác · dùng dấu thời gian cục bộ làm thứ tự toàn cục · bỏ lịch sử hợp lệ nên không kiểm được báo giả.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Xác định đúng ≥ 3/4 lịch sử kèm chuỗi thao tác chứng minh, lịch sử hợp lệ không bị báo nhầm, và giới hạn bộ kiểm được nêu rõ.

# MODULE M16 · KAFKA AND EVENT STREAMING

**Phase 8 · Lessons 321–334 · 28 giờ**

| | |
|---|---|
| **Objective cấp module** | Dự đoán được vị trí, thứ tự và quyền sở hữu của bất kỳ khoá nào; giải thích được khi nào một bản ghi hiển thị và khi nào nó bền vững |
| **Tiền đề** | M6 · M10 · M13 · M15 |
| **Exit criterion** | Sổ tay vận hành phủ được độ trễ tiêu thụ, thiếu bản sao đồng bộ, đầy đĩa, bản ghi độc và phá vỡ lược đồ; tính được số bản trùng và lượng mất tối đa cho một cấu hình cho trước |
| **Kỹ năng SFIA** | `SYSP` mức 4 · `ITOP` mức 4 |
| **Chế độ hỏng** | Tăng số phân vùng mà không xử lý khoá và thứ tự, đặt lại vị trí tiêu thụ mà không đối soát, và gọi giao nhận ít nhất một lần là đúng một lần |

Nhật ký phân tán khác hàng đợi ở một điểm quyết định: bản ghi **không bị xoá khi đã đọc**, nên nhiều nhóm tiêu thụ đọc độc lập và đọc lại được. Hiểu điều đó là hiểu vì sao nó thành xương sống của kiến trúc dữ liệu.

Ranh giới bảo đảm phải phát biểu chính xác: thứ tự chỉ có trong một phân vùng, giao dịch chỉ bao trong phạm vi hệ này, và mọi tuyên bố về đúng một lần phải nêu nguồn, đích và giả định lỗi, theo đúng kết luận ở lesson 318.

### Lesson 321 · Event, command and state - and three messaging shapes `LT`
**Prerequisites.** Module 16: M15

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài mở module bằng hai phép phân biệt quyết định thiết kế. Thứ nhất, ba loại thông điệp: sự kiện kể lại một việc đã xảy ra và không kỳ vọng ai làm gì; lệnh yêu cầu một việc được làm và có một người nhận xác định; trạng thái mô tả hiện trạng của một thực thể. Đặt tên sai loại dẫn tới ghép nối sai: gọi một lệnh là sự kiện làm bên sản xuất phụ thuộc ngầm vào việc bên nào đó phải xử lý. Thứ hai, ba hình thái hạ tầng: hàng đợi giao mỗi thông điệp cho một bên tiêu thụ rồi xoá; phát hành và đăng ký gửi cho mọi bên đăng ký tại thời điểm đó; nhật ký phân tán ghi bản ghi vào một chuỗi bền vững có thứ tự và **giữ lại theo thời hạn chứ theo việc đã đọc hay chưa**. Ba hệ quả của việc giữ lại: nhiều nhóm đọc độc lập, đọc lại được từ một vị trí cũ, và nhóm mới bắt đầu từ đầu được.

**Outcome.** Phân loại thông điệp và chọn hình thái hạ tầng cho bốn tình huống, nêu hệ quả của việc giữ lại bản ghi.

**Đánh giá.** Tầng *hiểu*. Bài mở module, đặt từ vựng. Kiểm bằng bài phân loại cộng bài chọn; đạt khi phân đúng ít nhất sáu trong tám thông điệp và chọn đúng hình thái ở ít nhất ba trong bốn tình huống.

**Lab.** Cho tám thông điệp thật trong một hệ; phân loại thành sự kiện, lệnh hay trạng thái và chỉ ra ba cái đang đặt tên sai kèm hệ quả ghép nối. Cho bốn tình huống; chọn hình thái hạ tầng và nêu lý do. Với tình huống chọn nhật ký phân tán, liệt kê ba việc làm được nhờ giữ lại bản ghi.

**Pitfalls.** Gọi lệnh là sự kiện · dùng hàng đợi rồi muốn đọc lại · giả định nhật ký phân tán thay được mọi hàng đợi · bỏ qua việc thời hạn giữ quyết định đọc lại được bao xa.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân đúng ≥ 6/8 thông điệp kèm hệ quả của ba cái đặt tên sai, và chọn đúng hình thái ở ≥ 3/4 tình huống.

### Lesson 322 · Topic, partition, key and the ordering boundary `TH`
**Prerequisites.** Lesson 321

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài dạy mô hình định vị, và nó là bài phải nắm chắc nhất vì mọi thứ sau đều dựa vào. Chủ đề chia thành phân vùng; mỗi bản ghi có vị trí tăng dần trong phân vùng của nó; khoá quyết định phân vùng qua một hàm băm, nên cùng khoá thì cùng phân vùng. Hệ quả trung tâm và là ranh giới bảo đảm: **thứ tự chỉ được giữ trong một phân vùng, không giữ giữa các phân vùng**; muốn hai bản ghi có thứ tự với nhau thì chúng phải cùng khoá. Bản ghi không khoá được rải theo cách khác và không có thứ tự với nhau. Vị trí không phải định danh của bản ghi: nó là vị trí trong một phân vùng cụ thể, nên cùng một con số ở hai phân vùng là hai bản ghi khác nhau. Tăng số phân vùng làm hàm băm cho kết quả khác, nên **khoá cũ có thể chuyển sang phân vùng khác và thứ tự lịch sử bị phá**.

**Outcome.** Dự đoán đúng phân vùng, thứ tự và nhóm sở hữu cho một tập tình huống khoá, và chứng minh hậu quả của việc tăng phân vùng.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là dự đoán khớp thực tế. Kiểm bằng mười tình huống; đạt khi dự đoán đúng ít nhất tám trước khi chạy, và ca phá thứ tự khi tăng phân vùng được tái hiện.

**Lab.** Dựng cụm ba máy chủ với một chủ đề sáu phân vùng. Với mười tình huống về khoá và nhóm tiêu thụ, dự đoán phân vùng, thứ tự và bên sở hữu trước khi chạy, rồi đối chiếu. Tăng số phân vùng và chứng minh một khoá cụ thể chuyển sang phân vùng khác, làm bản ghi mới của nó không còn thứ tự với bản ghi cũ.

**Pitfalls.** Giả định thứ tự toàn cục trong một chủ đề · dùng vị trí như định danh bản ghi · tăng phân vùng mà không xử lý khoá và thứ tự · gửi bản ghi không khoá rồi mong có thứ tự.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Dự đoán đúng ≥ 8/10 tình huống trước khi chạy, và ca khoá chuyển phân vùng sau khi tăng được tái hiện bằng dữ liệu.

### Lesson 323 · Broker internals - segment, index, page cache and retention `TH`
**Prerequisites.** Lesson 322

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bên trong một máy chủ, và hiểu nó giải thích cả hiệu năng lẫn các giới hạn vận hành. Đường đi của một bản ghi: lô bản ghi tới người dẫn phân vùng, ghi nối vào đoạn nhật ký hiện tại, cập nhật chỉ mục, nằm trong bộ đệm trang của hệ điều hành, rồi nút theo sau kéo về. **Ghi nối vào cuối tệp là lý do thông lượng cao**, và nó dùng lại đúng nguyên lý tuần tự nhanh hơn ngẫu nhiên ở lesson 52. Bộ đệm trang đóng vai trò chính nên bộ nhớ trống của máy quan trọng hơn kích thước bộ nhớ tiến trình. Đoạn nhật ký cuộn theo kích thước hoặc thời gian; thời hạn giữ theo thời gian hoặc dung lượng quyết định đọc lại được bao xa. Hai hệ quả vận hành: dung lượng đĩa là ràng buộc cứng, và đầy đĩa làm máy chủ ngừng nhận ghi; nên theo dõi dung lượng là việc bắt buộc chứ tuỳ chọn.

**Outcome.** Truy đường đi của một bản ghi trên hệ thật và tính được thời hạn đọc lại từ cấu hình cùng dung lượng.

**Đánh giá.** Tầng *phân tích*. Objective đòi đọc trạng thái thật thay vì mô tả kiến trúc. Kiểm bằng bài truy vết cộng bài tính; đạt khi truy đủ các chặng trên hệ thật và thời hạn đọc lại tính được khớp quan sát trong sai số thoả thuận.

**Lab.** Gửi một lô bản ghi và truy đường đi qua từng chặng: tìm tệp đoạn trên đĩa, xem chỉ mục, quan sát bộ đệm trang, và xác nhận nút theo sau đã kéo về. Tính thời hạn đọc lại từ tốc độ ghi, cấu hình giữ và dung lượng đĩa; đối chiếu với quan sát. Làm đầy đĩa có kiểm soát và ghi lại hành vi của máy chủ.

**Pitfalls.** Bỏ qua bộ đệm trang khi tính bộ nhớ cần · đặt thời hạn giữ mà không tính dung lượng · không theo dõi dung lượng đĩa · nghĩ thông lượng cao đến từ phần cứng chứ từ cách ghi nối.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đường đi của bản ghi được truy đủ chặng trên hệ thật, và thời hạn đọc lại tính từ cấu hình khớp quan sát.

### Lesson 324 · Log compaction and the tombstone lifecycle `TH`
**Prerequisites.** Lesson 323

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Cơ chế giữ lại bản ghi mới nhất cho mỗi khoá thay vì giữ theo thời gian, dùng khi chủ đề biểu diễn trạng thái chứ chuỗi sự kiện. Quá trình nén giữ lại bản ghi cuối cùng của mỗi khoá và xoá các bản cũ hơn, nên chủ đề trở thành một bản chụp trạng thái có thể đọc lại từ đầu để dựng lại toàn bộ. Bản ghi bia mộ có khoá và giá trị rỗng, báo rằng khoá đã bị xoá; nó phải nằm lại một khoảng đủ lâu để mọi bên tiêu thụ kịp thấy. **Bia mộ hết hạn trước khi một bên tiêu thụ chậm kịp đọc làm bên đó không bao giờ biết khoá đã bị xoá**, nên trạng thái dựng lại của nó thừa một bản ghi; đây là chế độ hỏng đặc trưng và phải tái hiện. Quan hệ với chủ đề theo thời gian: hai chế độ cho hai mục đích, và trộn chúng trên một chủ đề gây nhầm lẫn về nghĩa.

**Outcome.** Dựng lại trạng thái từ một chủ đề đã nén và tái hiện ca bia mộ hết hạn trước bên tiêu thụ chậm.

**Đánh giá.** Tầng *áp dụng*. Objective có một ca hỏng cụ thể cần tái hiện. Kiểm bằng đối soát trạng thái dựng lại; đạt khi trạng thái dựng lại khớp nguồn tuyệt đối, và ca bia mộ hết hạn được tái hiện kèm số khoá thừa.

**Lab.** Dựng một chủ đề chế độ nén biểu diễn trạng thái khách hàng. Ghi chuỗi tạo, cập nhật và xoá. Chạy nén rồi đọc lại từ đầu và đối soát trạng thái dựng lại với nguồn. Đặt thời hạn giữ bia mộ ngắn, dừng một bên tiêu thụ đủ lâu rồi cho chạy lại; đếm số khoá đã xoá mà nó vẫn giữ.

**Pitfalls.** Dùng chế độ nén cho chủ đề chuỗi sự kiện · đặt thời hạn giữ bia mộ ngắn hơn thời gian dừng tối đa của bên tiêu thụ · gửi bản ghi không khoá vào chủ đề nén · không đối soát trạng thái dựng lại.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Trạng thái dựng lại khớp nguồn tuyệt đối, và ca bia mộ hết hạn được tái hiện kèm số khoá thừa đếm được.

### Lesson 325 · Producer - acks, retry, idempotent producer and the sequence `TH`
**Prerequisites.** Lesson 324

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bên sản xuất quyết định một bản ghi bền vững tới mức nào, và ba tham số kiểm soát điều đó. Mức xác nhận: không chờ ai thì nhanh nhất và mất khi người dẫn chết; chờ người dẫn thì mất khi người dẫn chết trước khi nút theo sau kéo về; chờ toàn bộ bản sao đồng bộ thì bền nhất và chậm nhất. Thử lại và hết giờ giao hàng: **một lần thử lại sau khi máy chủ đã ghi thành công nhưng phản hồi thất lạc sẽ tạo bản trùng**, đúng ca không biết kết cục ở lesson 310. Bên sản xuất luỹ đẳng giải ca này bằng số thứ tự và nhiệm kỳ cho mỗi phân vùng, nên máy chủ nhận ra và bỏ bản trùng; giới hạn của nó là chỉ trong phạm vi một phiên và một phân vùng. Số yêu cầu đang bay ảnh hưởng thứ tự khi có thử lại. Gom lô, nén và thời gian chờ gom là ba nút điều chỉnh giữa thông lượng, độ trễ và bộ nhớ.

**Outcome.** Tính lượng mất và số bản trùng tối đa cho ba cấu hình, và chứng minh bằng thí nghiệm giết máy chủ.

**Đánh giá.** Tầng *phân tích*. Objective đòi nối cấu hình với một con số về rủi ro. Kiểm bằng ba cấu hình đo song song; đạt khi số đo khớp con số tính trước trong sai số thoả thuận ở cả ba.

**Lab.** Với ba cấu hình xác nhận khác nhau, tính trước lượng mất và số bản trùng tối đa. Chạy tải rồi giết người dẫn phân vùng; đếm bản ghi mất và bản ghi trùng thật, đối chiếu với tính toán. Bật bên sản xuất luỹ đẳng và đo lại số bản trùng. Đo ảnh hưởng của gom lô, nén và thời gian chờ lên thông lượng cùng độ trễ.

**Pitfalls.** Dùng mức xác nhận thấp rồi tuyên bố không mất · thử lại mà không bật chế độ luỹ đẳng · tăng số yêu cầu đang bay mà không xét thứ tự · chỉnh ba nút gom lô mà không đo.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Số đo mất và trùng khớp tính toán ở cả ba cấu hình, và bên sản xuất luỹ đẳng đưa số bản trùng về không trong phạm vi phiên.

### Lesson 326 · Producer transactions and the scope of the guarantee `TH`
**Prerequisites.** Lesson 325

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Giao dịch ở đây cho phép ghi nguyên tử qua nhiều phân vùng và ghi cả vị trí tiêu thụ trong cùng một giao dịch, nên nó giải được mẫu đọc rồi xử lý rồi ghi. Định danh giao dịch cùng cơ chế chặn ngăn một tiến trình cũ ghi tiếp sau khi đã có tiến trình mới, dùng lại đúng ý tưởng thẻ chặn ở lesson 317. Bên tiêu thụ phải đặt ở chế độ chỉ đọc bản đã chốt, nếu không nó vẫn thấy bản ghi của giao dịch chưa chốt. **Ranh giới bảo đảm phải phát biểu chính xác và đây là điểm ra của bài: giao dịch chỉ bao những gì nằm trong hệ này**; nó không bao một lần ghi vào cơ sở dữ liệu bên ngoài, không bao một lời gọi dịch vụ, không bao một lần gửi thư. Muốn đầu cuối thì phải cộng thêm đích luỹ đẳng hoặc hộp thư đi theo lesson 318. Chi phí của giao dịch về độ trễ và về thông lượng phải đo.

**Outcome.** Cài mẫu đọc rồi xử lý rồi ghi có giao dịch và phát biểu chính xác ranh giới bảo đảm.

**Đánh giá.** Tầng *đánh giá*. Objective đòi nêu đúng phạm vi bảo đảm chứ chỉ bật tính năng. Kiểm bằng phép thử giết tiến trình cộng bài phát biểu; đạt khi không bản trùng nào trong phạm vi hệ, và ca ghi ra hệ ngoài được chỉ ra là nằm ngoài bảo đảm kèm cách bù.

**Lab.** Cài luồng đọc từ một chủ đề, xử lý, rồi ghi sang chủ đề khác kèm ghi vị trí, tất cả trong một giao dịch. Giết tiến trình ở từng ranh giới và đếm bản trùng ở đích. Thêm một bước ghi vào cơ sở dữ liệu ngoài và chứng minh nó không được giao dịch bảo vệ; bổ sung cơ chế luỹ đẳng cho bước đó. Đo chi phí độ trễ và thông lượng của giao dịch.

**Pitfalls.** Tuyên bố đúng một lần đầu cuối nhờ giao dịch · để bên tiêu thụ đọc cả bản chưa chốt · đưa lời gọi dịch vụ ngoài vào trong giao dịch · bật giao dịch mà không đo chi phí.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Không bản trùng nào trong phạm vi hệ qua mọi ranh giới giết, và bước ghi ra hệ ngoài được chỉ rõ nằm ngoài bảo đảm kèm cơ chế bù.

### Lesson 327 · Consumer - the poll loop, group, assignment and rebalance `TH`
**Prerequisites.** Lesson 326

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bên tiêu thụ làm việc theo vòng lặp lấy dữ liệu, và mô hình nhóm quyết định ai đọc phân vùng nào. Một nhóm chia các phân vùng cho các thành viên, mỗi phân vùng thuộc đúng một thành viên tại một thời điểm, nên **mức song song tối đa bằng số phân vùng**; thêm thành viên vượt số phân vùng không tăng thông lượng. Điều phối viên nhóm quản lý thành viên qua nhịp tim và thời hạn phiên. Tái cân bằng xảy ra khi thành viên vào, ra, hoặc quá hạn; ca hay gặp và phải tái hiện: **xử lý một lô quá lâu làm thành viên quá hạn giữa chừng và bị coi là chết**, gây tái cân bằng, rồi lô đó bị giao cho người khác xử lý lại. Ba cách giảm: giảm số bản ghi mỗi lần lấy, tăng thời hạn, hoặc tách việc nặng ra khỏi vòng lặp. Kiểu gán hợp tác và thành viên tĩnh chỉ cần biết là có.

**Outcome.** Dự đoán quyền sở hữu phân vùng qua các lần thay đổi thành viên và tái hiện bão tái cân bằng do xử lý chậm.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là dự đoán khớp và ca hỏng được chặn có số đo. Kiểm bằng sáu tình huống cộng thí nghiệm xử lý chậm; đạt khi dự đoán đúng ít nhất năm và bão tái cân bằng được chặn với số lần tái cân bằng giảm có số đo.

**Lab.** Với chủ đề sáu phân vùng, chạy nhóm từ một tới tám thành viên; dự đoán phân bổ trước mỗi lần thay đổi rồi đối chiếu. Đo thông lượng khi số thành viên vượt số phân vùng. Làm xử lý một lô chậm hơn thời hạn và quan sát bão tái cân bằng; đếm số lần tái cân bằng và số bản ghi bị xử lý lại. Áp ba cách giảm và đo lại.

**Pitfalls.** Thêm thành viên vượt số phân vùng để tăng thông lượng · để việc nặng trong vòng lặp lấy dữ liệu · tăng thời hạn phiên mà không xét thời gian phát hiện chết · bỏ qua số bản ghi bị xử lý lại sau tái cân bằng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Dự đoán đúng ≥ 5/6 tình huống phân bổ, và số lần tái cân bằng giảm có số đo sau khi áp biện pháp.

### Lesson 328 · Offset commit - the two failure windows `TH`
**Prerequisites.** Lesson 327

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài chốt ngữ nghĩa giao nhận bằng hai cửa sổ hỏng, và đây là bài quyết định của module. Nếu ghi vị trí trước khi thực hiện tác dụng phụ rồi tiến trình chết ở giữa, bản ghi đó không bao giờ được xử lý: **mất dữ liệu**. Nếu thực hiện tác dụng phụ trước rồi ghi vị trí và chết ở giữa, bản ghi đó được xử lý lại: **trùng lặp**. Không có thứ tự nào tránh được cả hai, nên phải chọn một cửa sổ và bù bằng thiết kế: chọn trùng lặp rồi làm đích luỹ đẳng là lựa chọn đúng trong phần lớn trường hợp, theo kết luận ở lesson 318. Ghi vị trí tự động theo chu kỳ làm cửa sổ rộng và khó suy luận, nên ghi thủ công sau khi xử lý là mặc định nên chọn. Độ trễ tiêu thụ đọc được theo ba cách: theo số bản ghi, theo thời gian, và theo tốc độ xử lý; ba cách cho ba kết luận khác nhau. Chính sách bản ghi độc và hàng đợi bản ghi lỗi.

**Outcome.** Tái hiện cả hai cửa sổ hỏng bằng thực nghiệm và chọn một cửa sổ rồi bù bằng đích luỹ đẳng.

**Đánh giá.** Tầng *phân tích*. Objective đòi chứng minh đánh đổi thay vì phát biểu nó. Kiểm bằng hai thí nghiệm giết tiến trình; đạt khi số mất và số trùng được đếm ở hai thứ tự, và bản có đích luỹ đẳng đưa số trùng quan sát được về không.

**Lab.** Cài hai bản: ghi vị trí trước khi xử lý và sau khi xử lý. Giết tiến trình 100 lần ở từng bản và đếm số bản ghi mất cùng số bản ghi xử lý lại. Chọn bản gây trùng và thêm đích luỹ đẳng bằng khoá xác định; chạy lại và đối soát. Đọc độ trễ tiêu thụ theo ba cách trong lúc bên tiêu thụ chậm và giải thích ba kết luận khác nhau.

**Pitfalls.** Dùng ghi vị trí tự động rồi suy luận về cửa sổ hỏng · ghi vị trí trước khi xử lý · đọc độ trễ chỉ theo số bản ghi · đặt lại vị trí về cuối để làm sạch cảnh báo mà không đối soát.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Hai cửa sổ hỏng có số đo mất và trùng qua 100 lần giết, và bản có đích luỹ đẳng đưa số trùng quan sát được về không.

### Lesson 329 · Replication - in-sync replicas, high watermark and leader epoch `TH`
**Prerequisites.** Lesson 328

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Sao chép bên trong, và nó quyết định khi nào một bản ghi hiển thị với bên tiêu thụ. Tập bản sao đồng bộ là những nút theo sau đang bắt kịp người dẫn; một nút tụt quá ngưỡng bị loại khỏi tập. Mốc nước cao là vị trí mà mọi bản sao đồng bộ đã có; **bên tiêu thụ chỉ thấy bản ghi dưới mốc nước cao**, nên có độ trễ giữa lúc ghi xong và lúc đọc được. Ngưỡng số bản sao đồng bộ tối thiểu kết hợp với mức xác nhận toàn bộ mới cho bảo đảm bền vững thật: đặt ngưỡng bằng một thì mức xác nhận toàn bộ không còn nghĩa. Nhiệm kỳ người dẫn giải bài toán nút theo sau có phần nhật ký không thuộc nhiệm kỳ hiện tại, theo đúng cơ chế ở lesson 316. Bầu chọn người dẫn không sạch cho phép một nút không đồng bộ lên làm người dẫn để giữ khả dụng, và **nó đánh đổi bằng mất dữ liệu đã xác nhận**; bật hay tắt là một quyết định nghiệp vụ.

**Outcome.** Tính lượng dữ liệu có thể mất theo ba tổ hợp cấu hình và chứng minh bằng thí nghiệm giết máy chủ.

**Đánh giá.** Tầng *đánh giá*. Objective đòi nối ba tham số thành một con số rủi ro. Kiểm bằng ba tổ hợp; đạt khi lượng mất đo được khớp tính toán ở cả ba và ca bầu chọn không sạch được tái hiện kèm số bản ghi mất.

**Lab.** Dựng cụm ba máy chủ, hệ số sao chép ba. Với ba tổ hợp mức xác nhận và ngưỡng bản sao đồng bộ tối thiểu, tính trước lượng mất tối đa. Giết người dẫn rồi giết thêm một nút theo sau; đếm bản ghi đã xác nhận mà mất. Bật bầu chọn không sạch, tái hiện ca mất dữ liệu đã xác nhận. Đo độ trễ giữa lúc ghi và lúc đọc được.

**Pitfalls.** Đặt mức xác nhận toàn bộ với ngưỡng bản sao đồng bộ bằng một · bật bầu chọn không sạch mà không coi là quyết định nghiệp vụ · giả định bản ghi ghi xong là đọc được ngay · bỏ theo dõi số phân vùng thiếu bản sao.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Lượng mất đo được khớp tính toán ở cả ba tổ hợp, và ca bầu chọn không sạch được tái hiện kèm số bản ghi đã xác nhận bị mất.

### Lesson 330 · Controller quorum and metadata `LT`
**Prerequisites.** Lesson 329

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Mặt phẳng điều khiển quản lý siêu dữ liệu của cụm: danh sách máy chủ, phân vùng nào có người dẫn nào, và cấu hình. Nó dựa trên một nhật ký được sao chép cùng số đông, tức chính cơ chế đồng thuận ở lesson 316 áp dụng cho siêu dữ liệu chứ cho dữ liệu người dùng. Hệ quả vận hành: số đông điều khiển mất số đông thì cụm không bầu được người dẫn mới và không đổi được cấu hình, dù dữ liệu vẫn còn nguyên trên đĩa; **cụm vẫn phục vụ đọc ghi trên các phân vùng chưa đổi người dẫn nhưng không tự hồi phục được**, và phân biệt hai trạng thái này khi trực là quan trọng. Đăng ký máy chủ và nhiệm kỳ. Kiến trúc cũ dùng một hệ phối hợp riêng chỉ cần biết ở mức lịch sử. Ba chỉ số phải theo dõi cho mặt phẳng điều khiển và vì sao chúng khác chỉ số của mặt phẳng dữ liệu.

**Outcome.** Phân biệt sự cố mặt phẳng điều khiển với sự cố mặt phẳng dữ liệu từ triệu chứng và số đo.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết chuẩn bị cho bài diễn tập. Kiểm bằng bốn tình huống chẩn đoán; đạt khi phân đúng ít nhất ba và nêu đúng việc cụm còn làm được gì trong mỗi tình huống.

**Lab.** Cho bốn tình huống với triệu chứng và số đo. Với mỗi cái, xác định sự cố thuộc mặt phẳng nào và liệt kê việc cụm còn làm được. Trên cụm lab, dừng số đông điều khiển và quan sát: ghi và đọc trên phân vùng cũ còn chạy không, tạo chủ đề mới có được không, người dẫn mới có bầu được không.

**Pitfalls.** Nhầm sự cố điều khiển với sự cố dữ liệu · giả định mất số đông điều khiển là cụm ngừng hoàn toàn · theo dõi cụm chỉ bằng chỉ số của mặt phẳng dữ liệu · đổi cấu hình khi số đông điều khiển chưa lành.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân đúng ≥ 3/4 tình huống, và quan sát thật trên cụm xác nhận đúng việc cụm còn làm được khi mất số đông điều khiển.

### Lesson 331 · Schema registry, compatibility and consumer rollout order `TH`
**Prerequisites.** Lesson 330

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hợp đồng dữ liệu trên nhật ký phân tán có một khó khăn riêng: bản ghi cũ vẫn nằm trong nhật ký và vẫn được đọc lại, nên bên tiêu thụ mới phải đọc được cả bản ghi viết bằng lược đồ cũ. Sổ đăng ký lược đồ giữ phiên bản và cưỡng chế quy tắc tương thích tại thời điểm đăng ký, nên thay đổi phá vỡ bị chặn trước khi tới môi trường chạy. Mức tương thích quyết định thứ tự triển khai, theo đúng lesson 220: tương thích ngược thì nâng cấp bên tiêu thụ trước, tương thích xuôi thì nâng cấp bên sản xuất trước; **chọn sai thứ tự làm một phía không đọc được dữ liệu của phía kia**. Khác biệt so với hợp đồng theo yêu cầu phản hồi ở M8: ở đây không điều phối được thời điểm, vì dữ liệu cũ tồn tại suốt thời hạn giữ. Cách xử lý bản ghi không giải mã được: đưa vào hàng đợi bản ghi lỗi kèm nguyên nhân, không bỏ im lặng.

**Outcome.** Thực hiện một thay đổi lược đồ theo đúng thứ tự triển khai và chứng minh không bên nào ngừng đọc được.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là không gián đoạn ở cả hai phía. Kiểm bằng thí nghiệm triển khai có tải; đạt khi không bên tiêu thụ nào lỗi suốt quá trình và bản ghi cũ trong nhật ký vẫn đọc được sau khi nâng cấp.

**Lab.** Đăng ký lược đồ với mức tương thích chọn trước. Ghi 100.000 bản ghi bằng lược đồ cũ. Thực hiện một thay đổi tương thích và một thay đổi phá vỡ; xác nhận thay đổi phá vỡ bị sổ đăng ký chặn. Triển khai theo đúng thứ tự suy ra từ mức tương thích, với cả hai phía đang chạy tải. Đọc lại toàn bộ nhật ký từ đầu bằng bên tiêu thụ mới và đối soát.

**Pitfalls.** Nâng cấp bên sản xuất trước khi mức tương thích cho phép · đặt sổ đăng ký ở chế độ không cưỡng chế · bỏ bản ghi không giải mã được · quên rằng dữ liệu cũ vẫn nằm trong nhật ký.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Không bên tiêu thụ nào lỗi suốt quá trình triển khai, và bên tiêu thụ mới đọc lại toàn bộ nhật ký cũ với đối soát khớp.

### Lesson 332 · Capacity - partition count from throughput, not a rule `TH`
**Prerequisites.** Lesson 331

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Số phân vùng là quyết định khó đảo ngược nhất, nên nó phải tính chứ chọn theo quy tắc ngón tay. Bốn yếu tố đầu vào: thông lượng mục tiêu, mức song song tiêu thụ cần, thời gian phục hồi khi một máy chủ chết, và chi phí siêu dữ liệu trên mỗi phân vùng. Quá ít phân vùng thì không đủ song song và có phân vùng nóng; quá nhiều thì tăng chi phí siêu dữ liệu, kéo dài thời gian bầu chọn khi máy chủ chết, và tăng độ trễ đầu cuối vì lô nhỏ đi. **Tăng số phân vùng về sau phá thứ tự theo khoá** theo lesson 322, nên việc di trú phải có kế hoạch chứ làm tại chỗ. Khoá nóng là bài toán khác với thiếu phân vùng và cần cách khác: thêm phân vùng không chia nhỏ được một khoá. Kích thước bản ghi, thời hạn giữ và dung lượng cho ra ràng buộc lưu trữ. Đọc lại toàn bộ là một hợp đồng phải tính vào năng lực.

**Outcome.** Tính số phân vùng từ bốn yếu tố đầu vào và kiểm bằng phép thử tải ở ba mức.

**Đánh giá.** Tầng *đánh giá*. Objective đòi tính từ ràng buộc chứ chọn theo quy tắc. Kiểm bằng phép thử tải ba mức; đạt khi con số tính ra đạt thông lượng mục tiêu và đường cong cho thấy điểm tăng phân vùng bắt đầu phản tác dụng.

**Lab.** Tính số phân vùng cho một khối lượng công việc cho trước từ bốn yếu tố. Chạy tải với ba mức số phân vùng quanh con số tính được; đo thông lượng, độ trễ phân vị 95, thời gian phục hồi khi giết một máy chủ, và chi phí siêu dữ liệu. Tạo một khoá nóng và chứng minh thêm phân vùng không giúp. Lập kế hoạch di trú nếu phải tăng phân vùng.

**Pitfalls.** Chọn số phân vùng theo một quy tắc chung · tăng phân vùng để chữa khoá nóng · tăng phân vùng tại chỗ mà không có kế hoạch di trú khoá · bỏ thời gian phục hồi khỏi tính toán.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Con số tính ra đạt thông lượng mục tiêu trong phép thử, và đường cong ba mức cho thấy điểm tăng phân vùng phản tác dụng.

### Lesson 333 · Security, quota and multi-tenancy `TH`
**Prerequisites.** Lesson 332

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Cụm dùng chung nhiều đội đặt ra ba yêu cầu mà một cụm lab không có. Mã hoá đường truyền và xác thực cho cả máy khách lẫn giữa các máy chủ. Quyền truy cập ở mức chủ đề và mức nhóm, theo nguyên tắc quyền tối thiểu ở lesson 106: một bên tiêu thụ chỉ cần quyền đọc một chủ đề và quyền quản lý nhóm của nó. Hạn mức theo người dùng hoặc theo máy khách giới hạn băng thông và tốc độ yêu cầu, để **một đội chạy đọc lại toàn bộ không làm chậm mọi đội khác**; đây là ca cụ thể phải tái hiện vì đọc lại là thao tác hợp lệ nhưng nặng. Xoay thông tin xác thực mà không gián đoạn. Phân loại dữ liệu trên chủ đề và hệ quả về thời hạn giữ cùng quyền xem, nối với lesson 306. Ba chế độ hỏng của cụm dùng chung và cách cô lập.

**Outcome.** Cài xác thực, phân quyền và hạn mức, rồi chứng minh một bên đọc lại không làm vỡ cam kết của bên khác.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là cách ly đo được dưới tải. Kiểm bằng phép thử đọc lại; đạt khi bên bị ảnh hưởng giữ độ trễ trong cam kết, và phép thử phủ định về quyền bị chặn hết.

**Lab.** Bật mã hoá đường truyền và xác thực. Cấp quyền tối thiểu cho hai đội. Chạy phép thử phủ định: mỗi đội thử đọc và ghi chủ đề của đội kia. Đặt hạn mức. Cho một đội đọc lại toàn bộ chủ đề lớn trong khi đội kia đang chạy tải bình thường; đo độ trễ của đội kia trước và trong lúc đọc lại. Xoay thông tin xác thực không gián đoạn.

**Pitfalls.** Cấp quyền theo chủ đề mà quên quyền nhóm · không đặt hạn mức nên một đội chiếm hết băng thông · dùng chung một tài khoản cho nhiều đội · xoay thông tin xác thực bằng cách dừng dịch vụ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phép thử phủ định bị chặn hết, độ trễ của đội không liên quan giữ trong cam kết suốt lần đọc lại, và xoay thông tin xác thực không gây gián đoạn.

### Lesson 334 · Game day - kill the leader, the controller and the consumer `DA`
**Prerequisites.** Lesson 333

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Bài dự án khép module. Chạy diễn tập trên cụm đã dựng, với hành vi kỳ vọng viết trước theo đúng kỷ luật ở lesson 246. Tám tình huống bắt buộc: giết người dẫn của một phân vùng đang có tải; giết một máy chủ mang nhiều người dẫn; làm mất số đông điều khiển; giết bên tiêu thụ giữa lúc đã thực hiện tác dụng phụ nhưng chưa ghi vị trí; làm tập bản sao đồng bộ co lại; làm đầy đĩa một máy chủ; đưa một bản ghi độc vào chủ đề; và triển khai một thay đổi lược đồ phá vỡ. Với mỗi tình huống ghi ba số: thời gian phát hiện, thời gian phục hồi, và số bản ghi mất hoặc trùng đo bằng đối soát. **Phục hồi bằng cách đặt lại vị trí về cuối là lối tắt bị cấm**, vì nó bỏ qua dữ liệu chưa xử lý mà không ai biết; mọi lần đặt lại vị trí phải kèm đối soát. Nộp sổ tay vận hành gồm cả năm mục bắt buộc.

**Outcome.** Chạy tám tình huống với hành vi kỳ vọng viết trước và nộp sổ tay vận hành có bằng chứng đối soát.

**Đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module thành năng lực vận hành có số đo. Kiểm bằng tám tình huống; đạt khi ít nhất bảy phục hồi với đối soát khớp và không lần nào dùng lối tắt đặt lại vị trí về cuối.

**Lab.** Viết hành vi kỳ vọng cho tám tình huống. Chạy từng cái trên cụm có tải. Ghi ba số cho mỗi tình huống. Đối soát số bản ghi ở đích với nguồn sau mỗi lần phục hồi. Nộp sổ tay gồm độ trễ tiêu thụ, thiếu bản sao, đầy đĩa, bản ghi độc và phá vỡ lược đồ.

**Pitfalls.** Đặt lại vị trí về cuối để hết cảnh báo · viết hành vi kỳ vọng sau khi thấy kết quả · bỏ tình huống mất số đông điều khiển vì khó dựng · không đối soát sau phục hồi.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** ≥ 7/8 tình huống phục hồi với đối soát khớp, ba số đo đầy đủ cho mỗi tình huống, và sổ tay có đủ năm mục bắt buộc.

# MODULE M17 · CHANGE DATA CAPTURE INTERNALS

**Phase 8 · Lessons 335–344 · 20 giờ**

| | |
|---|---|
| **Objective cấp module** | Vẽ được đường từ vị trí nhật ký nguồn tới vị trí trình kết nối tới vị trí trên nhật ký phân tán tới điểm kiểm tra ở đích, và chứng minh tính đầy đủ bằng đối soát |
| **Tiền đề** | M10 · M13 · M15 · M16 |
| **Exit criterion** | Giải thích được tính nhất quán của bản chụp ban đầu cùng cửa sổ hỏng của nó và chứng minh bằng đối soát; sổ tay phủ rủi ro thời hạn giữ ở nguồn, độ trễ, bản ghi độc, chụp lại và phá vỡ lược đồ |
| **Kỹ năng SFIA** | `DTAN` mức 4 · `SYSP` mức 4 |
| **Chế độ hỏng** | Xoá khe sao chép để tắt cảnh báo mà không có kế hoạch phục hồi, và chụp lại đè lên trạng thái đang phục vụ |

Module học sâu cơ chế mà M14B chỉ nhắc tới. Nó nối trực tiếp ba module trước: nhật ký ghi trước ở M10 là nguồn, nhật ký phân tán ở M16 là đường truyền, và lập luận về hỏng ở M15 là khung phân tích.

Điểm khó nhất và cũng là đóng góp chính của module: **bản chụp ban đầu phải được đan xen với dòng thay đổi đang chạy**, vì nguồn vẫn đang ghi trong lúc ta chụp. Làm sai chỗ này tạo ra khoảng trống hoặc ghi đè ngược, và cả hai đều im lặng.

### Lesson 335 · Three ways to capture change and their cost `LT`
**Prerequisites.** Module 17: M16

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài mở module bằng việc so ba cách lấy thay đổi, để thấy vì sao cách thứ ba đáng học sâu. Hỏi theo dấu thời gian hoặc theo khoá: đơn giản, chạy được ở mọi nguồn, nhưng **bỏ sót thay đổi xảy ra giữa hai lần hỏi và không thấy bản ghi bị xoá**, đúng năm giả định ở lesson 234. Bẫy cơ sở dữ liệu ghi thay đổi vào một bảng phụ: bắt được đủ thao tác gồm cả xoá, nhưng thêm chi phí ghi lên mọi giao dịch của nguồn và phải bảo trì bẫy. Đọc nhật ký giao dịch: bắt đủ mọi thay đổi theo đúng thứ tự, độ trễ thấp, và gần như không thêm tải ghi cho nguồn; đổi lại phức tạp về vận hành và tạo một phụ thuộc mới lên thời hạn giữ nhật ký của nguồn. Ba tiêu chí so: tải đặt lên nguồn, độ trễ, và tính đầy đủ. Phân biệt với nguồn sự kiện: ở đó ứng dụng chủ động phát ý định nghiệp vụ, còn ở đây ta suy ra thay đổi từ trạng thái vật lý.

**Outcome.** So ba cách theo ba tiêu chí và chứng minh cách hỏi theo dấu thời gian bỏ sót thay đổi.

**Đánh giá.** Tầng *hiểu*. Bài mở module, kiểm bằng một thí nghiệm nhỏ chứ chỉ lập luận. Kiểm bằng phép đếm bỏ sót; đạt khi số thay đổi bị bỏ sót được đo thật và bảng ba cách nhân ba tiêu chí có số ở tiêu chí tải nguồn.

**Lab.** Dựng một bảng nguồn có ghi liên tục. Chạy cách hỏi theo dấu thời gian mỗi 10 giây trong khi ghi nhiều lần một bản ghi và xoá vài bản ghi; đếm số thay đổi bị bỏ sót và số bản xoá không thấy. Cài một bẫy và đo chi phí ghi thêm trên nguồn. Lập bảng ba cách nhân ba tiêu chí.

**Pitfalls.** Dùng cách hỏi theo dấu thời gian rồi tuyên bố bắt đủ thay đổi · cài bẫy mà không đo chi phí ghi thêm · nhầm bắt thay đổi với nguồn sự kiện · chọn đọc nhật ký mà chưa tính phụ thuộc thời hạn giữ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Số thay đổi bỏ sót và số bản xoá không thấy được đo thật, và bảng ba cách có số đo ở tiêu chí tải nguồn.

### Lesson 336 · Inside the transaction log - WAL, logical decoding and the replication slot `TH`
**Prerequisites.** Lesson 335

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài đi vào cơ chế của nguồn, dùng lại nhật ký ghi trước ở lesson 137 nhưng ở vai người đọc. Với hệ quan hệ phổ biến: nhật ký ghi trước ghi mọi thay đổi vật lý; bộ giải mã logic dịch chúng thành thay đổi mức hàng có nghĩa; khe sao chép giữ vị trí mà bên đọc đã xác nhận, và **nguồn không được xoá phần nhật ký chưa được khe nào xác nhận**. Từ đó suy ra rủi ro trung tâm của module: bên đọc dừng thì nhật ký tích luỹ và đĩa nguồn đầy dần, nên một trình kết nối chết có thể làm sập cơ sở dữ liệu sản xuất. Vị trí khởi động lại và vị trí đã xác nhận là hai con số khác nhau. Với hệ khác thì có nhật ký nhị phân cùng định dạng và vị trí hoặc định danh giao dịch toàn cục. Ranh giới giao dịch có trong nhật ký, và đây là thứ cách hỏi theo dấu thời gian không bao giờ có.

**Outcome.** Đọc được vị trí và trạng thái khe trên nguồn thật, và định lượng tốc độ tích luỹ nhật ký khi bên đọc dừng.

**Đánh giá.** Tầng *phân tích*. Objective đòi quan sát trạng thái thật của nguồn. Kiểm bằng thí nghiệm dừng bên đọc; đạt khi tốc độ tích luỹ được đo theo đơn vị dung lượng trên giờ và thời gian tới khi đầy đĩa tính được.

**Lab.** Bật giải mã logic trên một cơ sở dữ liệu lab và tạo một khe. Đọc vị trí khởi động lại và vị trí đã xác nhận, giải thích khác biệt. Chạy tải ghi, dừng bên đọc, và đo tốc độ tích luỹ nhật ký. Tính thời gian còn lại tới khi đầy đĩa. Cho bên đọc chạy lại và xác nhận nhật ký được giải phóng.

**Pitfalls.** Tạo khe rồi quên bên đọc · nhầm vị trí khởi động lại với vị trí đã xác nhận · không đo tốc độ tích luỹ nên không đặt được cảnh báo · giả định nguồn tự dọn nhật ký.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tốc độ tích luỹ được đo theo dung lượng trên giờ, thời gian tới khi đầy đĩa tính được, và nhật ký được giải phóng sau khi bên đọc chạy lại.

### Lesson 337 · The consistent bootstrap - snapshot interleaved with the live log `TH`
**Prerequisites.** Lesson 336

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài khó nhất của module và là đóng góp chính của nó. Bài toán: phải chụp toàn bộ dữ liệu hiện có, nhưng nguồn vẫn đang ghi trong lúc chụp, nên một bản ghi có thể được chụp ở trạng thái cũ rồi ngay sau đó một sự kiện thay đổi cũ hơn tới đích và ghi đè lên, tạo ra dữ liệu lùi về quá khứ. Thuật toán năm bước: xác lập vị trí nhật ký và ranh giới nhất quán trước khi chụp; đọc bảng theo từng khối trong khi vẫn thu sự kiện thay đổi; **đan xen sao cho một dòng của bản chụp không bao giờ ghi đè một sự kiện mới hơn**, dùng cơ chế mốc nước hoặc so phiên bản theo khoá; hoàn tất bản chụp rồi tiếp tục phát dòng từ đúng vị trí đã xác lập; và chỉ lưu vị trí của trình kết nối theo đúng giao thức giao nhận. Chia khối theo khoá có chỉ mục và ảnh hưởng lên nguồn theo lesson 238. Hai chế độ hỏng: khoảng trống, và ghi đè ngược.

**Outcome.** Chạy bản chụp ban đầu trong khi nguồn đang ghi và chứng minh không có khoảng trống cũng không có ghi đè ngược.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là đối soát khớp tuyệt đối dưới ghi đồng thời. Kiểm bằng đối soát tập khoá và giá trị; đạt khi đích khớp nguồn tại một ranh giới bất biến, và bản cài sai được chứng minh tạo ghi đè ngược.

**Lab.** Chạy tải ghi liên tục trên nguồn. Khởi tạo bản chụp trong lúc đó. Sau khi hoàn tất, dừng ghi và đối soát tập khoá cùng giá trị giữa nguồn và đích. Cài thêm một bản cố ý bỏ bước đan xen và chứng minh nó tạo ra dữ liệu lùi về quá khứ; đếm số bản ghi sai. Đo ảnh hưởng của việc chụp lên nguồn.

**Pitfalls.** Chụp xong rồi mới bắt đầu thu dòng thay đổi · để dòng bản chụp ghi đè sự kiện mới hơn · khoá bảng để chụp cho đơn giản · không đối soát sau khi hoàn tất.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đích khớp nguồn tuyệt đối tại ranh giới bất biến, và bản bỏ bước đan xen được chứng minh tạo ghi đè ngược kèm số bản ghi sai.

### Lesson 338 · The event envelope - before, after, op and source metadata `TH`
**Prerequisites.** Lesson 337

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Cấu trúc một sự kiện thay đổi, và mỗi trường tồn tại để trả lời một câu hỏi vận hành. Trạng thái trước và trạng thái sau cho phép bên tiêu thụ biết cái gì đã đổi chứ chỉ biết giá trị mới. Mã thao tác phân biệt thêm, sửa, xoá và đọc từ bản chụp; phân biệt cái cuối là quan trọng vì sự kiện từ bản chụp không có trạng thái trước. Siêu dữ liệu nguồn gồm tên bảng, vị trí trong nhật ký, định danh giao dịch và dấu thời gian ở nguồn; **vị trí trong nhật ký là thứ tạo nên thứ tự xác định cho mỗi khoá**, và nó là cơ sở để đích khử trùng và chọn bản thắng. Khoá của sự kiện lấy từ khoá chính, và nó quyết định phân vùng theo lesson 322 nên mọi thay đổi của một hàng đi cùng phân vùng và giữ đúng thứ tự. Sự kiện bia mộ cho thao tác xoá theo lesson 324. Đích áp dụng bằng ghi đè theo khoá cộng so phiên bản.

**Outcome.** Cài đích áp dụng sự kiện đúng cho cả bốn mã thao tác, dùng vị trí nhật ký để chọn bản thắng.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là trạng thái đích khớp nguồn sau một chuỗi thao tác hỗn hợp. Kiểm bằng đối soát sau 10.000 thao tác; đạt khi đích khớp nguồn tuyệt đối và sự kiện tới sai thứ tự không làm sai trạng thái.

**Lab.** Thu sự kiện cho một bảng và kiểm từng trường của phong bì. Cài đích áp dụng bằng ghi đè theo khoá với so phiên bản theo vị trí nhật ký. Chạy 10.000 thao tác hỗn hợp gồm thêm, sửa, xoá. Cố ý đảo thứ tự một số sự kiện khi giao và chứng minh so phiên bản giữ trạng thái đúng. Đối soát cuối cùng.

**Pitfalls.** Chỉ dùng trạng thái sau nên không biết cái gì đã đổi · áp dụng theo thứ tự tới thay vì theo vị trí nhật ký · xử lý sự kiện từ bản chụp như một lần sửa · bỏ qua sự kiện bia mộ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đích khớp nguồn tuyệt đối sau 10.000 thao tác, và sự kiện bị đảo thứ tự không làm sai trạng thái nhờ so phiên bản.

### Lesson 339 · Ordering scope and the multi-table transaction limit `TH`
**Prerequisites.** Lesson 338

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài phát biểu chính xác bảo đảm về thứ tự, vì đây là chỗ kỳ vọng thường vượt thực tế. Thứ tự được giữ cho mỗi khoá, vì mọi thay đổi của một hàng vào cùng phân vùng. Thứ tự giữa hai bảng khác nhau thì không, vì chúng thường ở hai chủ đề hoặc hai phân vùng khác nhau. **Hệ quả: một giao dịch nguồn chạm hai bảng sẽ tới đích thành hai sự kiện độc lập, và đích có thể thấy nửa giao dịch trong một khoảng thời gian**; nếu hạ nguồn có ràng buộc tham chiếu giữa hai bảng thì nó sẽ thấy trạng thái không nhất quán tạm thời. Ba cách xử lý và đánh đổi: chấp nhận trạng thái trung gian và nói rõ với bên tiêu thụ; gom theo định danh giao dịch rồi áp dụng cả cụm; hoặc đưa hai bảng về một chủ đề với khoá chung. Định danh giao dịch có trong phong bì nên gom được, nhưng ranh giới kết thúc giao dịch cần một tín hiệu riêng.

**Outcome.** Tái hiện ca đích thấy nửa giao dịch và chọn một cách xử lý kèm điều kiện áp dụng.

**Đánh giá.** Tầng *phân tích*. Objective đòi nhận ra một giới hạn thường bị bỏ qua khi thiết kế. Kiểm bằng ca tái hiện cộng bài chọn; đạt khi ca nửa giao dịch được quan sát và định lượng khoảng thời gian, và cách xử lý chọn kèm hai điều kiện.

**Lab.** Tạo một giao dịch nguồn chạm hai bảng có quan hệ tham chiếu. Ở đích, chạy một truy vấn liên tục kiểm ràng buộc tham chiếu và ghi lại mọi lần nó bị vi phạm cùng độ dài khoảng thời gian. Cài cách gom theo định danh giao dịch và đo lại. So độ trễ của hai cách. Viết một câu cho bên tiêu thụ nói rõ bảo đảm thứ tự mà họ nhận được.

**Pitfalls.** Giả định thứ tự toàn cục giữa các bảng · để hạ nguồn cưỡng chế ràng buộc tham chiếu mà không nói trước · gom theo giao dịch mà không có tín hiệu kết thúc · bỏ qua độ trễ tăng thêm khi gom.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ca nửa giao dịch được quan sát kèm độ dài khoảng thời gian, và cách xử lý chọn kèm hai điều kiện áp dụng.

### Lesson 340 · Position, offset and checkpoint - three different things `TH`
**Prerequisites.** Lesson 339

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba con số hay bị gọi chung là tiến độ, và trộn chúng làm không chẩn đoán được. Vị trí trong nhật ký nguồn là tiến độ của trình kết nối trên nguồn, và nó điều khiển việc nguồn giải phóng nhật ký theo lesson 336. Vị trí trên nhật ký phân tán là tiến độ của bản ghi đã được ghi sang đường truyền. Điểm kiểm tra ở đích là tiến độ của việc áp dụng vào kho cuối. Ba con số tiến theo ba nhịp và khoảng cách giữa chúng là ba loại độ trễ khác nhau, mỗi loại có nguyên nhân riêng và cách xử lý riêng. **Thứ tự lưu trạng thái phải theo đúng quy tắc ở lesson 240**: chỉ tiến một con số sau khi dữ liệu tương ứng đã bền vững ở bước sau. Ca hỏng bắt buộc tái hiện: trình kết nối chết sau khi đã phát sự kiện nhưng trước khi lưu vị trí, dẫn tới phát lại và trùng lặp ở đích; lời giải là đích luỹ đẳng chứ cố tránh phát lại.

**Outcome.** Đo riêng ba loại độ trễ và tái hiện ca phát lại sau khi chết, chứng minh đích luỹ đẳng xử lý đúng.

**Đánh giá.** Tầng *phân tích*. Objective đòi tách ba tiến độ thường bị gộp. Kiểm bằng ba số đo cộng thí nghiệm giết; đạt khi ba loại độ trễ được đo riêng và đích vẫn khớp nguồn sau 50 lần giết ngẫu nhiên.

**Lab.** Dựng đường đầy đủ từ nguồn qua nhật ký phân tán tới đích. Đo riêng ba loại độ trễ dưới tải và vẽ ba đường. Giết trình kết nối 50 lần ở các thời điểm ngẫu nhiên, trong đó có lần sau khi phát và trước khi lưu vị trí. Đếm số sự kiện trùng ở đích. Bật đích luỹ đẳng và đối soát lại.

**Pitfalls.** Gọi chung ba con số là độ trễ · lưu vị trí trình kết nối trước khi sự kiện bền vững ở đường truyền · cố tránh phát lại thay vì làm đích luỹ đẳng · theo dõi một loại độ trễ rồi kết luận cho cả tuyến.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba loại độ trễ được đo riêng, và đích khớp nguồn sau 50 lần giết nhờ luỹ đẳng.

### Lesson 341 · Deletes, truncates, primary key updates and tombstones `TH`
**Prerequisites.** Lesson 340

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bốn thao tác phá vỡ giả định thông thường của bên tiêu thụ, và cả bốn phải xử lý tường minh. Xoá tạo sự kiện có trạng thái trước và không có trạng thái sau, kèm bia mộ để chủ đề nén dọn được; đích phải xoá thật hoặc đánh dấu tuỳ hợp đồng, và **bỏ qua xoá làm đích phình dần và mọi phép đếm sai**. Cắt bảng ở nhiều hệ không sinh sự kiện mức hàng, nên đích không biết bảng đã rỗng; cần xử lý riêng hoặc cấm thao tác này ở nguồn. Cập nhật khoá chính là ca khó nhất: nguồn coi là một lần sửa, nhưng ở đích khoá cũ và khoá mới là hai hàng, nên nếu không xử lý thì hàng cũ ở lại thành bản mồ côi và số lượng bị đếm đôi; lời giải là phát cả sự kiện xoá khoá cũ lẫn sự kiện thêm khoá mới. Xoá theo tầng ở nguồn sinh hàng loạt sự kiện và có thể gây dồn ứ.

**Outcome.** Xử lý đúng cả bốn thao tác và chứng minh đích không còn bản mồ côi cũng không đếm đôi.

**Đánh giá.** Tầng *áp dụng*. Objective có bốn ca biên với tiêu chí nghiệm thu bằng đối soát. Kiểm bằng bốn thao tác tiêm; đạt khi đích khớp nguồn về tập khoá và số lượng sau cả bốn, và ca cắt bảng được xử lý tường minh.

**Lab.** Thực hiện bốn thao tác trên nguồn: xoá, cắt bảng, cập nhật khoá chính, và xoá theo tầng nhiều nghìn hàng. Sau mỗi thao tác, đối soát tập khoá và số lượng giữa nguồn và đích. Với cập nhật khoá chính, chứng minh không còn hàng mồ côi. Với cắt bảng, chỉ ra hệ có sinh sự kiện không và xử lý tường minh. Đo dồn ứ khi xoá theo tầng.

**Pitfalls.** Bỏ qua sự kiện xoá · coi cập nhật khoá chính là một lần sửa thường · giả định cắt bảng sinh sự kiện mức hàng · không đo dồn ứ khi có thao tác hàng loạt.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đích khớp nguồn về tập khoá và số lượng sau cả bốn thao tác, không còn hàng mồ côi, và ca cắt bảng có xử lý tường minh.

### Lesson 342 · Schema change, schema history and quarantine `TH`
**Prerequisites.** Lesson 341

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Lược đồ nguồn đổi trong lúc dòng đang chạy, và trình kết nối phải xử lý được vì nó không kiểm soát nguồn. Lịch sử lược đồ được lưu riêng để giải mã đúng sự kiện cũ: một sự kiện phát ra ba tháng trước phải được diễn giải bằng lược đồ của thời điểm đó chứ lược đồ hiện tại, nên **đọc lại dữ liệu cũ cần lịch sử lược đồ còn nguyên**; mất lịch sử lược đồ là mất khả năng đọc lại. Ba loại thay đổi và phản ứng, theo phân loại ở lesson 241: thêm cột thì bên tiêu thụ cũ vẫn chạy; đổi kiểu thu hẹp là phá vỡ; đổi tên là phá vỡ với bên đọc theo tên. Thứ tự triển khai giữa bên sản xuất và bên tiêu thụ lấy từ mức tương thích ở lesson 331. Sự kiện không giải mã được đi vào vùng cách ly kèm nguyên nhân và vị trí, để phát lại sau khi sửa chứ bỏ.

**Outcome.** Xử lý ba loại thay đổi lược đồ trong lúc dòng đang chạy và đọc lại được dữ liệu cũ sau đó.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là đọc lại dữ liệu cũ vẫn đúng sau khi lược đồ đã đổi. Kiểm bằng phép đọc lại; đạt khi dữ liệu trước thay đổi được giải mã đúng, không sự kiện nào bị bỏ im lặng, và sự kiện cách ly phát lại được.

**Lab.** Chạy dòng liên tục rồi thực hiện ba thay đổi lược đồ ở nguồn. Với mỗi cái, ghi lại phản ứng của trình kết nối và của bên tiêu thụ. Sau khi đổi xong, đọc lại toàn bộ chủ đề từ đầu và xác nhận dữ liệu cũ giải mã đúng nhờ lịch sử lược đồ. Tạo một sự kiện không giải mã được, xác nhận nó vào vùng cách ly, sửa rồi phát lại.

**Pitfalls.** Xoá lịch sử lược đồ để dọn dẹp · để sự kiện không giải mã được bị bỏ qua · đổi lược đồ nguồn mà không báo bên tiêu thụ · triển khai sai thứ tự so với mức tương thích.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Dữ liệu trước thay đổi giải mã đúng khi đọc lại, không sự kiện nào bị bỏ im lặng, và sự kiện cách ly được phát lại thành công.

### Lesson 343 · Slot retention, lag and the source disk risk `TH`
**Prerequisites.** Lesson 342

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài vận hành quan trọng nhất của module, vì đây là chỗ một lỗi ở hệ phụ làm sập hệ chính. Chuỗi nhân quả: bên tiêu thụ dừng hoặc chậm, trình kết nối không tiến vị trí đã xác nhận, nguồn không giải phóng nhật ký, đĩa nguồn đầy dần, rồi cơ sở dữ liệu sản xuất ngừng nhận ghi. Ba chỉ số phải theo dõi và đặt ngưỡng: độ trễ của khe tính bằng dung lượng, tốc độ tăng, và dung lượng đĩa còn lại quy ra thời gian. **Cảnh báo phải đặt theo thời gian còn lại chứ theo phần trăm đĩa**, vì phần trăm không nói được còn bao lâu để xử lý. Quy trình khi cảnh báo nổ, theo thứ tự: tìm nguyên nhân bên tiêu thụ dừng, khôi phục nó, chỉ khi hết cách mới cân nhắc bỏ khe. Bỏ khe là thao tác phá huỷ: nó giải phóng đĩa ngay nhưng **mất toàn bộ thay đổi chưa đọc, nên bắt buộc phải chụp lại**, và chụp lại phải vào không gian cách ly chứ đè lên trạng thái đang phục vụ.

**Outcome.** Dựng cảnh báo theo thời gian còn lại và chạy đúng quy trình xử lý khi khe phình, không dùng thao tác phá huỷ.

**Đánh giá.** Tầng *đánh giá*. Objective đo năng lực vận hành dưới một rủi ro có thể làm sập hệ chính. Kiểm bằng tình huống tái hiện; đạt khi cảnh báo nổ trước ngưỡng thời gian thoả thuận và quy trình phục hồi không cần bỏ khe.

**Lab.** Dựng ba chỉ số và đặt cảnh báo theo thời gian còn lại. Dừng bên tiêu thụ và để khe phình; xác nhận cảnh báo nổ đúng lúc. Chạy quy trình phục hồi theo thứ tự và đo thời gian tới khi nhật ký được giải phóng. Ở môi trường cách ly, thực hiện một lần bỏ khe rồi chụp lại vào không gian riêng, đối soát trước khi hoán đổi.

**Pitfalls.** Đặt cảnh báo theo phần trăm đĩa · bỏ khe để tắt cảnh báo · chụp lại đè lên trạng thái đang phục vụ · không đo thời gian còn lại nên không biết còn bao lâu để xử lý.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Cảnh báo nổ trước ngưỡng thời gian thoả thuận, phục hồi hoàn tất không cần bỏ khe, và lần chụp lại ở môi trường cách ly có đối soát trước khi hoán đổi.

### Lesson 344 · CDC project - reconcile after repeated crashes `DA`
**Prerequisites.** Lesson 343

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Bài dự án khép module. Dựng đường đầy đủ từ một cơ sở dữ liệu quan hệ qua nhật ký phân tán tới một đích phân tích, chạy được cả khởi tạo, dòng liên tục, và chụp lại. Nộp gồm: sơ đồ bốn vị trí tiến độ theo lesson 340 với số đo độ trễ thật cho từng chặng; bằng chứng bản chụp ban đầu nhất quán theo lesson 337; xử lý đủ bốn thao tác ở lesson 341; lịch sử lược đồ cùng vùng cách ly; ba chỉ số cùng cảnh báo theo lesson 343; và sổ tay vận hành. Nghiệm thu bằng đối soát sau khi giết lặp lại: chạy tải ghi liên tục trên nguồn, giết trình kết nối, máy chủ nhật ký và tiến trình ghi đích ở các thời điểm ngẫu nhiên ít nhất 30 lần, rồi đối soát tập khoá và giá trị giữa nguồn và đích tại một ranh giới bất biến. **Mọi việc chạy xong không phải bằng chứng; đối soát mới là.**

**Outcome.** Nộp đường bắt thay đổi hoàn chỉnh, đối soát khớp nguồn sau ít nhất 30 lần giết ngẫu nhiên.

**Đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module. Kiểm bằng đối soát sau giết lặp lại; đạt khi đích khớp nguồn tuyệt đối về tập khoá và giá trị, và bốn vị trí tiến độ đều có số đo độ trễ.

**Lab.** Dựng đường đầy đủ. Chạy tải ghi liên tục gồm thêm, sửa, xoá và một lần cập nhật khoá chính. Giết ba thành phần ngẫu nhiên ít nhất 30 lần. Dừng ghi và đối soát. Thực hiện một lần chụp lại vào không gian cách ly rồi hoán đổi. Nộp sổ tay đủ năm mục bắt buộc.

**Pitfalls.** Coi trình kết nối báo chạy là bằng chứng đầy đủ · chụp lại đè lên đích đang phục vụ · bỏ ca cập nhật khoá chính · đối soát bằng cách đếm tổng mà không so tập khoá.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Đích khớp nguồn tuyệt đối về tập khoá và giá trị sau ≥ 30 lần giết, bốn vị trí tiến độ có số đo độ trễ, và lần chụp lại có đối soát trước khi hoán đổi.

# MODULE M18 · SPARK, FLINK AND DISTRIBUTED COMPUTE ENGINES

**Phase 8 · Lessons 345–360 · 33 giờ**

| | |
|---|---|
| **Objective cấp module** | Ánh xạ mã nguồn thành kế hoạch logic, toán tử vật lý, giai đoạn và tác vụ; điều chỉnh bắt đầu từ số đo chứ từ việc đổi cấu hình |
| **Tiền đề** | M3 · M4 · M5 · M12 · M13 · M15 · M16 |
| **Exit criterion** | Giải thích được song song lồng nhau và tránh được cấp phát quá mức giữa lõi của tiến trình thực thi, mức đồng thời của tác vụ, luồng của thư viện gốc và số nút; chọn giữa **bốn lớp engine** gồm hai engine phân tán và hai engine một máy, theo khối lượng công việc, quy mô, độ trễ, nhu cầu giữ trạng thái và chi phí vận hành |
| **Kỹ năng SFIA** | `SYSP` mức 5 · `PROG` mức 4 |
| **Chế độ hỏng** | Đổi cấu hình bộ nhớ tiến trình thực thi một cách ngẫu nhiên, kéo toàn bộ dữ liệu về tiến trình điều khiển, và tuyên bố dòng chảy đúng một lần mà bỏ qua đích |

Module áp toàn bộ phần song song ở M4 vào một engine thật. Ba tầng đặt ra ở lesson 48 và lesson 56 gặp lại đầy đủ: **cụm tính toán là nhiều lệnh nhiều dữ liệu phân tán, một mảnh toán tử chạy theo khuôn mẫu một chương trình nhiều dữ liệu trên nhiều phân vùng, và bên trong mỗi tác vụ có đường xử lý theo lô cùng làn véctơ.**

Kỷ luật điều chỉnh lấy từ M4 và giữ nguyên ở đây: sửa dữ liệu, bố cục và thuật toán trước khi chạm tới cấu hình bộ nhớ.

Một engine học sâu là đủ; engine dòng chảy còn lại ở mức hiểu kiến trúc và khác biệt, trừ khi công việc yêu cầu.

### Lesson 345 · Cluster roles and the execution hierarchy `LT`
**Prerequisites.** Module 18: M16

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài mở module bằng từ vựng thực thi, vì năm từ dưới đây bị dùng lẫn thường xuyên. Tiến trình điều khiển giữ kế hoạch, lập lịch và gom kết quả; tiến trình thực thi chạy tác vụ và giữ dữ liệu trong bộ nhớ; bộ quản lý cụm cấp tài nguyên. Bậc thang thực thi có bốn mức lồng nhau: một ứng dụng gồm nhiều công việc, một công việc gồm nhiều giai đoạn, một giai đoạn gồm nhiều tác vụ, và **một tác vụ xử lý đúng một phân vùng**. Từ đó suy ra quan hệ nền tảng: số tác vụ trong một giai đoạn bằng số phân vùng, nên số phân vùng là nút điều chỉnh mức song song chứ số lõi. Tiến trình điều khiển là điểm nghẽn tiềm tàng và là điểm hỏng: kéo dữ liệu lớn về nó làm tràn bộ nhớ, và kế hoạch quá lớn cùng quá nhiều siêu dữ liệu cũng làm nó chậm. Ánh xạ sang ba tầng song song ở lesson 48 được làm rõ ở lesson 352.

**Outcome.** Ánh xạ năm từ vựng thực thi vào một ứng dụng thật và đếm đúng số tác vụ của từng giai đoạn.

**Đánh giá.** Tầng *hiểu*. Bài mở module, đặt từ vựng. Kiểm bằng bài đọc giao diện theo dõi; đạt khi đếm đúng số giai đoạn và số tác vụ cho ba công việc và giải thích được nguồn gốc của số tác vụ.

**Lab.** Chạy ba công việc có hình dạng khác nhau. Với mỗi cái, mở giao diện theo dõi và ghi số công việc, giai đoạn và tác vụ. Giải thích số tác vụ của mỗi giai đoạn đến từ đâu. Thay đổi số phân vùng đầu vào và xác nhận số tác vụ đổi theo. Kéo một tập dữ liệu lớn về tiến trình điều khiển và quan sát hậu quả.

**Pitfalls.** Nghĩ số tác vụ do số lõi quyết định · kéo dữ liệu lớn về tiến trình điều khiển · nhầm công việc với giai đoạn · bỏ qua tiến trình điều khiển khi tính năng lực.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đếm đúng số giai đoạn và tác vụ cho ba công việc, và giải thích được số tác vụ đến từ số phân vùng.

### Lesson 346 · From code to logical plan to physical operators `TH`
**Prerequisites.** Lesson 345

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài truy đường biên dịch, nối thẳng với nội dung engine truy vấn ở lesson 126 và lesson 130. Bốn bước: mã dựng kế hoạch logic chưa phân giải; bộ phân tích phân giải tên và kiểu theo danh mục; bộ tối ưu áp luật viết lại cùng thông tin chi phí; bộ lập kế hoạch chọn toán tử vật lý. Đọc kế hoạch là kỹ năng chính của module: phần quét cho biết có cắt tỉa và có đẩy điều kiện xuống không theo lesson 206 và 210; phần kết cho biết chiến lược được chọn; phần trao đổi cho biết ranh giới giai đoạn; phần gộp và sắp xếp cho biết chi phí bộ nhớ. **Kế hoạch đã tối ưu khác kế hoạch vật lý, và chỉ kế hoạch vật lý mới nói được công việc sẽ chạy ra sao.** Hai giới hạn của bộ tối ưu phải biết: nó dựa vào thống kê nên thống kê cũ cho kế hoạch tồi, và nó không nhìn thấy bên trong hàm do người dùng viết.

**Outcome.** Đọc kế hoạch vật lý của ba truy vấn và dự đoán đúng số giai đoạn trước khi chạy.

**Đánh giá.** Tầng *phân tích*. Objective đòi dự đoán từ kế hoạch rồi kiểm bằng thực tế. Kiểm bằng ba truy vấn; đạt khi dự đoán đúng số giai đoạn ở ít nhất hai và chỉ ra đúng vị trí mọi bước trao đổi dữ liệu.

**Lab.** Với ba truy vấn có hình dạng khác nhau, xuất cả kế hoạch logic, kế hoạch đã tối ưu và kế hoạch vật lý. Dự đoán số giai đoạn từ số bước trao đổi trước khi chạy, rồi đối chiếu. Làm thống kê lạc hậu và quan sát kế hoạch đổi thế nào. Chèn một hàm do người dùng viết và chỉ ra bộ tối ưu mất khả năng gì.

**Pitfalls.** Đọc kế hoạch logic rồi kết luận về cách chạy · bỏ qua bước trao đổi khi đếm giai đoạn · chạy với thống kê lạc hậu · chèn hàm tự viết vào chỗ cần đẩy điều kiện xuống.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Dự đoán đúng số giai đoạn ở ≥ 2/3 truy vấn, và mọi bước trao đổi dữ liệu được chỉ đúng vị trí trong kế hoạch.

### Lesson 347 · Narrow and wide dependencies, and why exchange creates a stage `TH`
**Prerequisites.** Lesson 346

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài giải thích ranh giới giai đoạn bằng cơ chế chứ bằng quy ước. Phụ thuộc hẹp: mỗi phân vùng đầu ra chỉ cần một phân vùng đầu vào, nên phép biến đổi chạy tại chỗ và nhiều phép nối tiếp nhau gộp vào một tác vụ. Phụ thuộc rộng: một phân vùng đầu ra cần dữ liệu từ nhiều phân vùng đầu vào, nên phải xáo trộn dữ liệu qua mạng; **bước trao đổi là ranh giới giai đoạn vì giai đoạn sau không bắt đầu được cho tới khi giai đoạn trước ghi xong toàn bộ dữ liệu xáo trộn**, tức nó là một rào đồng bộ. Từ đó suy ra ba hệ quả thực hành: giảm số bước xáo trộn là đòn bẩy tối ưu lớn nhất; một tác vụ chậm trong giai đoạn trước giữ chân cả giai đoạn sau; và dòng dõi cho phép tính lại một phân vùng mất mà không chạy lại toàn bộ. Điểm kiểm tra khác dòng dõi: dòng dõi tính lại, điểm kiểm tra cắt chuỗi tính lại.

**Outcome.** Phân loại phép biến đổi theo hai loại phụ thuộc và giảm được số bước xáo trộn của một công việc thật.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là số bước xáo trộn giảm mà kết quả không đổi. Kiểm bằng cặp số đo; đạt khi số bước trao đổi giảm ít nhất một, thời gian giảm có số đo, và kết quả đối soát khớp bản gốc.

**Lab.** Phân loại mười phép biến đổi vào hai loại. Lấy một công việc có bốn bước xáo trộn; viết lại để giảm ít nhất một bước, chẳng hạn bằng cách gộp phép gộp hoặc đổi thứ tự. Đo thời gian và lượng dữ liệu xáo trộn trước sau. Đối soát kết quả. Giết một tiến trình thực thi và quan sát việc tính lại theo dòng dõi; thêm điểm kiểm tra rồi đo lại.

**Pitfalls.** Coi ranh giới giai đoạn là quy ước · thêm phép sắp xếp không cần thiết · đặt điểm kiểm tra khắp nơi · sửa mà không đối soát kết quả.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Số bước trao đổi giảm ≥ 1 với thời gian giảm có số đo, và kết quả đối soát khớp bản gốc tuyệt đối.

### Lesson 348 · Join strategies and the threshold that is not magic `TH`
**Prerequisites.** Lesson 347

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba chiến lược kết trong engine phân tán, tương ứng ba thuật toán ở lesson 127 nhưng thêm chiều mạng. Kết phát tán băm gửi bảng nhỏ tới mọi tiến trình thực thi rồi kết cục bộ, nên không cần xáo trộn bảng lớn; điều kiện là bảng nhỏ vừa bộ nhớ, và **ngưỡng phát tán dựa trên ước lượng kích thước nên thống kê sai làm tràn bộ nhớ** theo đúng ca ở lesson 212. Kết băm sau xáo trộn băm cả hai bảng theo khoá kết. Kết trộn sau sắp xếp sắp cả hai rồi trộn, ổn định với dữ liệu lớn và tốn chi phí sắp xếp. Thực thi thích ứng có thể đổi chiến lược khi thấy kích thước thật tại thời gian chạy, nhưng nó chỉ sửa được sau khi đã có thống kê thật của giai đoạn trước, nên **nó không cứu được mọi trường hợp**. Ép chiến lược bằng gợi ý là công cụ chẩn đoán, không phải giải pháp lâu dài.

**Outcome.** Ép cả ba chiến lược trên cùng phép kết, đo chi phí từng cái, và tái hiện ca phát tán gây tràn bộ nhớ.

**Đánh giá.** Tầng *phân tích*. Objective đòi nối lựa chọn chiến lược với số đo và với một ca hỏng. Kiểm bằng ba chiến lược đo song song; đạt khi ba chiến lược có số đo thời gian cùng lượng xáo trộn và ca tràn bộ nhớ do ước lượng sai được tái hiện.

**Lab.** Với một phép kết giữa bảng lớn và bảng vừa, ép lần lượt ba chiến lược và xác nhận trong kế hoạch. Đo thời gian, lượng dữ liệu xáo trộn và bộ nhớ đỉnh. Làm thống kê sai để engine chọn phát tán cho một bảng quá lớn và ghi lại lỗi tràn bộ nhớ. Bật thực thi thích ứng và chỉ ra nó sửa được ca nào, không sửa được ca nào.

**Pitfalls.** Tin ngưỡng phát tán là con số an toàn · ép gợi ý rồi để đó thay vì sửa thống kê · bỏ qua lượng dữ liệu xáo trộn khi so · cho rằng thực thi thích ứng chữa được mọi kế hoạch tồi.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba chiến lược có số đo thời gian và lượng xáo trộn, và ca tràn bộ nhớ do ước lượng sai được tái hiện cùng giải thích.

### Lesson 349 · Shuffle - read, write, sort, spill and serialization `TH`
**Prerequisites.** Lesson 348

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bước xáo trộn là thao tác đắt nhất, nên nó có một bài riêng để mổ xẻ chi phí. Bốn thành phần chi phí phải tách: ghi dữ liệu xáo trộn ra đĩa cục bộ, truyền qua mạng, đọc lại, và chi phí tuần tự hoá cùng giải tuần tự hoá. **Xáo trộn đi qua ba bậc chậm nhất của thứ bậc bộ nhớ cùng lúc** theo lesson 58, nên nó thường chiếm phần lớn thời gian. Tràn đĩa xảy ra khi bộ nhớ làm việc không đủ cho phép sắp xếp hoặc phép gộp; nó là cơ chế sống sót chứ lỗi, nhưng làm chậm nhiều lần và phải đọc được trong số đo. Chi phí tuần tự hoá là phần hay bị bỏ qua và thường lớn hơn phép tính, nhất là với hàm do người dùng viết bằng ngôn ngữ cần chuyển đổi dữ liệu qua ranh giới. Số phân vùng sau xáo trộn quá nhỏ gây tràn, quá lớn gây nhiều tác vụ vụn và tăng chi phí lập lịch.

**Outcome.** Tách bốn thành phần chi phí của một bước xáo trộn và giảm tổng thời gian có số đo mà kết quả không đổi.

**Đánh giá.** Tầng *phân tích*. Objective đòi phân giải một số tổng thành bốn phần để biết sửa chỗ nào. Kiểm bằng phép đo phân tách; đạt khi bốn thành phần đều có số, và thành phần lớn nhất được giảm với tổng thời gian giảm theo.

**Lab.** Chạy một công việc có bước xáo trộn lớn dưới bộ nhớ hạn chế. Đo riêng bốn thành phần chi phí cùng mức tràn đĩa và thời gian thu dọn rác. Thử bốn mức số phân vùng sau xáo trộn và vẽ đường thời gian. Giảm chi phí tuần tự hoá bằng cách thay hàm tự viết bằng biểu thức có sẵn và đo lại. Đối soát kết quả.

**Pitfalls.** Tăng bộ nhớ tiến trình thực thi trước khi biết thành phần nào đắt · coi tràn đĩa là lỗi cấu hình · bỏ qua chi phí tuần tự hoá · chọn số phân vùng sau xáo trộn theo mặc định.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn thành phần chi phí đều có số đo, và thành phần lớn nhất giảm kéo tổng thời gian giảm theo với kết quả không đổi.

### Lesson 350 · Memory, caching and garbage collection `TH`
**Prerequisites.** Lesson 349

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bộ nhớ của tiến trình thực thi chia thành phần cho thực thi và phần cho lưu trữ, và hai phần cạnh tranh nhau. Lưu tạm một tập dữ liệu chỉ có lợi khi nó được đọc lại nhiều lần; **lưu tạm một tập dùng đúng một lần vừa không giúp vừa chiếm chỗ của phần thực thi**, làm tăng tràn đĩa. Các mức lưu tạm khác nhau về nơi giữ và về việc có tuần tự hoá không, nên chúng đánh đổi giữa bộ nhớ và chi phí giải tuần tự hoá. Thu dọn rác trở thành vấn đề khi giữ quá nhiều đối tượng sống: bộ thu dọn chạy liên tục và ăn thời gian bộ xử lý mà không làm việc hữu ích; biểu diễn dữ liệu ngoài vùng quản lý bộ nhớ giảm áp lực này. Ba dấu hiệu phân biệt thiếu bộ nhớ thật với dùng bộ nhớ sai cách. Giải phóng bộ nhớ lưu tạm khi không cần nữa là việc phải làm tường minh.

**Outcome.** Quyết định lưu tạm dựa trên số lần đọc lại và chứng minh bằng số đo rằng lưu tạm sai làm chậm hơn.

**Đánh giá.** Tầng *đánh giá*. Objective chống lại phản xạ lưu tạm mọi thứ. Kiểm bằng ba tình huống đo song song; đạt khi quyết định đúng ở cả ba và ca lưu tạm sai được định lượng mức chậm thêm.

**Lab.** Cho ba tình huống với số lần đọc lại khác nhau là một, ba và mười. Chạy có và không có lưu tạm ở từng tình huống; đo thời gian, mức tràn đĩa và thời gian thu dọn rác. Thử ba mức lưu tạm khác nhau cho tình huống đọc lại nhiều. Tạo một ca giữ quá nhiều đối tượng sống và quan sát thu dọn rác; giảm bằng biểu diễn ngoài vùng quản lý.

**Pitfalls.** Lưu tạm mọi tập dữ liệu trung gian · lưu tạm tập dùng một lần · không giải phóng bộ nhớ lưu tạm · tăng bộ nhớ khi nguyên nhân là thu dọn rác.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Quyết định lưu tạm đúng ở cả ba tình huống, và ca lưu tạm sai được định lượng mức chậm thêm.

### Lesson 351 · Skew, stragglers and the salt-or-broadcast decision `TH`
**Prerequisites.** Lesson 350

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Lệch tải là nguyên nhân số một khiến một công việc chạy lâu bất thường mà mọi cấu hình trông đều hợp lý. Triệu chứng đặc trưng: trong một giai đoạn, phần lớn tác vụ xong nhanh còn một hoặc vài tác vụ chạy lâu gấp nhiều lần; phân bố thời gian tác vụ là số đo chẩn đoán chính, và giá trị trung bình che mất hiện tượng này nên phải nhìn phân vị. Nguyên nhân: một khoá chiếm phần lớn số dòng, nên tác vụ nhận khoá đó làm nhiều việc hơn hẳn. Ba cách xử lý và điều kiện dùng: thêm phần ngẫu nhiên vào khoá rồi gộp hai bước, chuyển sang kết phát tán nếu một bên đủ nhỏ, hoặc tách riêng các khoá nóng và xử lý theo đường khác. **Mọi cách xử lý lệch tải đều đổi hình dạng phép tính, nên bắt buộc đối soát kết quả.** Phân biệt lệch tải với tác vụ chậm do máy yếu hoặc do thu dọn rác.

**Outcome.** Chẩn đoán lệch tải từ phân bố thời gian tác vụ và sửa bằng một trong ba cách, có đối soát kết quả.

**Đánh giá.** Tầng *phân tích*. Objective đòi phân biệt lệch tải với hai nguyên nhân giống triệu chứng. Kiểm bằng ba tình huống; đạt khi chẩn đoán đúng cả ba và bản sửa lệch tải cho kết quả khớp bản gốc với thời gian giảm có số đo.

**Lab.** Tạo lệch tải bằng một khoá chiếm phần lớn số dòng. Chạy và ghi phân bố thời gian tác vụ; chỉ ra trung bình che hiện tượng thế nào. Thử cả ba cách xử lý, đo thời gian và đối soát kết quả với bản gốc. Tạo thêm hai tình huống có triệu chứng giống nhưng nguyên nhân là máy yếu và thu dọn rác; phân biệt bằng số đo.

**Pitfalls.** Đánh giá bằng thời gian tác vụ trung bình · thêm phần ngẫu nhiên vào khoá mà không đối soát · tăng số phân vùng để chữa lệch tải · nhầm tác vụ chậm do máy yếu với lệch tải.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chẩn đoán đúng cả ba tình huống bằng số đo, và bản sửa lệch tải khớp kết quả gốc với thời gian giảm có số đo.

### Lesson 352 · Distributed MIMD and SPMD in a compute engine `LT`
**Prerequisites.** Lesson 351

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài đặt engine vào đúng khung phân loại ở lesson 48 và nối với lesson 56 cùng lesson 211. Mỗi lõi của mỗi tiến trình thực thi có dòng lệnh và trạng thái riêng, nên cụm là nhiều lệnh nhiều dữ liệu bộ nhớ phân tán. Bộ lập lịch gửi cùng một mã toán tử cho nhiều phân vùng, nên đây là khuôn mẫu một chương trình nhiều dữ liệu. Hệ quả quan trọng và hay bị hiểu sai: **tác vụ song song dữ liệu không chạy đồng bộ từng bước**; thời gian của chúng khác nhau do lệch tải, vị trí dữ liệu, thu dọn rác, vào ra, thử lại và phần cứng không đồng nhất, và chênh lệch đó là bình thường. Bước trao đổi dữ liệu là ranh giới truyền thông và đồng bộ; rào cùng phép gộp cuối làm lộ phần tuần tự và làm lộ tác vụ chậm. Bên trong một tác vụ, bộ giải mã tệp cột và toán tử truy vấn có thể dùng đường xử lý theo lô và làn véctơ, tức tầng thứ ba theo lesson 208.

**Outcome.** Truy được ba tầng song song trên một công việc thật và gán đúng mỗi mức tăng quan sát được về một tầng.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết nối M4 với engine thật, chuẩn bị cho hai bài đo. Kiểm bằng bài truy tầng; đạt khi ba tầng được chỉ ra bằng bằng chứng quan sát được và ba mức tăng được gán đúng tầng.

**Lab.** Trên một công việc thật, chỉ ra bằng chứng của từng tầng: số tiến trình thực thi và lõi cho tầng nhiều lệnh nhiều dữ liệu, cùng một mã toán tử chạy trên nhiều phân vùng cho khuôn mẫu một chương trình nhiều dữ liệu, và đường xử lý theo lô trong kế hoạch cho tầng làn véctơ. Ghi phân bố thời gian tác vụ và giải thích vì sao chênh lệch là bình thường. Gán ba mức tăng quan sát được về đúng tầng.

**Pitfalls.** Gộp ba tầng thành một lời giải thích · coi chênh lệch thời gian giữa các tác vụ là lỗi · nói engine nhanh vì dùng lệnh véctơ mà không tách các tầng · nhầm khuôn mẫu một chương trình nhiều dữ liệu với kiến trúc phần cứng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba tầng được chỉ ra bằng bằng chứng quan sát được, và ba mức tăng được gán đúng tầng kèm lý do.

### Lesson 353 · Nested parallelism and oversubscription `TH`
**Prerequisites.** Lesson 352

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài chỉ ra một chế độ hỏng mà chỉ hiểu song song lồng nhau mới nhận ra. Bốn nguồn song song cùng tồn tại: số nút trong cụm, số lõi cấp cho mỗi tiến trình thực thi, số tác vụ chạy đồng thời trong một tiến trình, và **luồng do thư viện gốc tự tạo bên trong một tác vụ**, chẳng hạn thư viện đại số tuyến tính hoặc thư viện xử lý cột. Nguồn thứ tư là nguồn ẩn: nó không xuất hiện trong bất kỳ cấu hình nào của engine, nhưng nó nhân lên với ba nguồn kia. Cấp phát quá mức xảy ra khi tổng số luồng vượt số lõi thật: hậu quả là tranh chấp bộ nhớ đệm, bão hoà băng thông bộ nhớ và chuyển ngữ cảnh liên tục, nên **thêm song song làm chậm hơn**, đúng hiện tượng ở lesson 55. Cách phát hiện: so tổng số luồng quan sát được với số lõi, và đo băng thông bộ nhớ. Cách chặn: đặt giới hạn luồng cho thư viện gốc một cách tường minh.

**Outcome.** Phát hiện cấp phát quá mức bằng số đo và chặn nó, chứng minh thông lượng tăng trở lại.

**Đánh giá.** Tầng *phân tích*. Objective nhắm vào một nguồn song song không xuất hiện trong cấu hình engine. Kiểm bằng cặp số đo; đạt khi tổng số luồng và số lõi được đo, và sau khi đặt giới hạn thì thông lượng tăng có số đo.

**Lab.** Chạy một công việc có dùng thư viện gốc đa luồng. Đếm tổng số luồng thật trên một máy và so với số lõi. Đo băng thông bộ nhớ và tỉ lệ chuyển ngữ cảnh. Đặt giới hạn luồng cho thư viện gốc và chạy lại; đo thông lượng cùng thời gian phân vị 95 của tác vụ. Lập bảng bốn nguồn song song với giá trị hiện tại của từng nguồn.

**Pitfalls.** Tăng số lõi mỗi tiến trình mà không biết thư viện gốc đang tạo bao nhiêu luồng · chỉ đếm song song ở tầng engine · kết luận thiếu tài nguyên khi nguyên nhân là tranh chấp · không đặt giới hạn luồng tường minh.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tổng số luồng và số lõi được đo, và sau khi đặt giới hạn thì thông lượng tăng với thời gian phân vị 95 của tác vụ giảm.

### Lesson 354 · Strong scaling lab - where scale-out turns negative `TH`
**Prerequisites.** Lesson 353

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài thí nghiệm khép phần song song: cố định khối lượng công việc và tăng tài nguyên, rồi tìm điểm mà thêm tài nguyên bắt đầu phản tác dụng. Chạy với 1, 2, 4 và nhiều hơn số lõi hoặc tiến trình thực thi; tính tăng tốc và hiệu suất song song ở từng mức theo lesson 56, và **báo cáo cả hai chứ chỉ tăng tốc**. Tách thời gian thành bốn phần: chờ lập lịch, tính, xáo trộn cùng truyền thông, và tuần tự hoá; bốn phần này tiến hoá khác nhau khi tăng quy mô, và phần nào tăng theo là phần chỉ ra trần. Năm nguyên nhân làm tăng quy mô phản tác dụng: phần tuần tự ở tiến trình điều khiển, chi phí xáo trộn tăng theo số phân vùng, lệch tải, cấp phát quá mức theo lesson 353, và nút cổ chai ở hệ bên ngoài như nguồn dữ liệu. Kết luận phải là một khuyến nghị về số tài nguyên kèm lý do, chứ một đồ thị.

**Outcome.** Vẽ đường hiệu suất song song tới ít nhất tám mức và quy trần về đúng một trong năm nguyên nhân.

**Đánh giá.** Tầng *đánh giá*. Objective đòi giải thích đường cong chứ chỉ vẽ nó. Kiểm bằng thí nghiệm tăng quy mô; đạt khi bốn thành phần thời gian được tách ở mọi mức, điểm phản tác dụng được xác định, và trần quy về một nguyên nhân có bằng chứng.

**Lab.** Cố định tập dữ liệu và chạy với ít nhất bốn mức tài nguyên tăng dần. Ở mỗi mức, tính tăng tốc và hiệu suất song song, và tách bốn thành phần thời gian. Xác định mức mà thêm tài nguyên không còn giúp hoặc làm chậm hơn. Quy trần về một trong năm nguyên nhân bằng bằng chứng. Viết khuyến nghị về số tài nguyên kèm ngưỡng chi phí.

**Pitfalls.** Báo cáo tăng tốc mà không báo hiệu suất song song · thêm tài nguyên khi trần là nguồn dữ liệu bên ngoài · không tách thời gian nên không biết phần nào tăng · kết luận bằng đồ thị mà không có khuyến nghị.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đường hiệu suất song song có số đo ở ≥ 4 mức, bốn thành phần thời gian tách được ở mọi mức, và trần quy về một nguyên nhân có bằng chứng.

### Lesson 355 · Tuning project - the decision tree on three unknown jobs `DA`
**Prerequisites.** Lesson 354

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Bài dự án về điều chỉnh hiệu năng, chạy theo một cây quyết định có thứ tự cố định để chống việc đổi cấu hình ngẫu nhiên. Thứ tự bắt buộc: kiểm tính đúng, lược đồ và số phân vùng trước; đọc kế hoạch theo trình tự quét rồi cắt tỉa rồi chiến lược kết rồi trao đổi rồi gộp và sắp xếp rồi ghi ra; thu số đo gồm số dòng và byte vào ra, phân bố thời gian tác vụ, lượng xáo trộn, mức tràn đĩa, thời gian thu dọn rác, bộ nhớ đỉnh và thời gian chờ lập lịch; chẩn đoán phân biệt lệch tải với thiếu song song với quá nhiều tác vụ vụn; rồi **sửa dữ liệu, bố cục và thuật toán trước khi chạm tới cấu hình bộ nhớ**. Nhận ba công việc chưa từng thấy, mỗi cái có một nguyên nhân khác nhau. Với mỗi công việc, đề xuất đúng một thay đổi có kiểm soát, đo trước sau, và đối soát kết quả.

**Outcome.** Chẩn đoán ba công việc lạ theo cây quyết định và cải thiện từng cái bằng đúng một thay đổi có kiểm soát.

**Đánh giá.** Tầng *sáng tạo*. Bài tổng hợp phần hiệu năng thành một quy trình chẩn đoán có kỷ luật. Kiểm bằng ba công việc; đạt khi chẩn đoán đúng nguyên nhân ở ít nhất hai, mỗi cải thiện chỉ dùng một thay đổi, và kết quả đối soát không đổi.

**Lab.** Nhận ba công việc chậm với ba nguyên nhân khác nhau. Với mỗi cái, chạy đủ cây quyết định và ghi số đo ở từng bước. Nêu giả thuyết trước khi sửa. Áp đúng một thay đổi, đo lại và đối soát kết quả. Nộp báo cáo hiệu năng theo chuẩn ở lesson 59, bắt đầu từ số đo chứ từ cấu hình.

**Pitfalls.** Đổi nhiều cấu hình cùng lúc · tăng bộ nhớ tiến trình thực thi trước khi đọc kế hoạch · sửa mà không đối soát kết quả · viết báo cáo bắt đầu bằng việc đã đổi gì thay vì đã đo gì.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Chẩn đoán đúng nguyên nhân ở ≥ 2/3 công việc, mỗi cải thiện dùng đúng một thay đổi có số đo trước sau, và kết quả đối soát không đổi.

### Lesson 356 · Structured streaming - micro-batch, offsets, checkpoint and state `TH`
**Prerequisites.** Lesson 355

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài chuyển sang xử lý dòng trên cùng engine, với mô hình xử lý theo lô nhỏ. Mỗi lần kích hoạt, engine đọc một khoảng vị trí từ nguồn, xử lý, ghi ra đích, rồi lưu tiến độ; nên nó là một chuỗi công việc theo lô liên tiếp chứ một dòng chảy từng bản ghi. Điểm kiểm tra giữ ba thứ: vị trí nguồn, trạng thái của các phép toán có trạng thái, và siêu dữ liệu của lần ghi; **mất điểm kiểm tra là mất khả năng tiếp tục đúng chỗ**, và nó không dựng lại được từ đích. Kho trạng thái giữ dữ liệu cho phép gộp theo cửa sổ và phép kết dòng; trạng thái phình vô hạn nếu không có cơ chế hết hạn, và đây là chế độ hỏng vận hành phổ biến nhất. Ba chế độ ghi ra và điều kiện dùng. Đổi lược đồ trạng thái giữa hai lần triển khai là thao tác không tương thích ngược ở nhiều trường hợp và phải có kế hoạch.

**Outcome.** Vận hành một công việc dòng có trạng thái, khôi phục từ điểm kiểm tra, và chặn được trạng thái phình vô hạn.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là tiếp tục đúng chỗ và trạng thái có trần. Kiểm bằng phép thử giết và đo trạng thái; đạt khi khôi phục không mất và không trùng ngoài giới hạn đã nêu, và kích thước trạng thái ổn định sau khi đặt hết hạn.

**Lab.** Dựng công việc dòng có phép gộp theo cửa sổ. Chạy vài giờ và đo kích thước trạng thái theo thời gian; chứng minh nó phình khi chưa có hết hạn. Đặt cơ chế hết hạn và đo lại. Giết công việc và khôi phục từ điểm kiểm tra; đối soát kết quả. Xoá điểm kiểm tra và chỉ ra hậu quả. Thử đổi lược đồ trạng thái và ghi lại phản ứng.

**Pitfalls.** Coi mô hình theo lô nhỏ là dòng chảy từng bản ghi · để trạng thái không có cơ chế hết hạn · xoá điểm kiểm tra để khởi động lại sạch · đổi lược đồ trạng thái mà không có kế hoạch.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Khôi phục từ điểm kiểm tra không mất và không trùng ngoài giới hạn đã nêu, và kích thước trạng thái ổn định sau khi đặt hết hạn.

### Lesson 357 · Event time, watermark and late data `TH`
**Prerequisites.** Lesson 356

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài áp ba trục thời gian ở lesson 251 vào xử lý dòng, nơi chúng trở thành cơ chế chạy được. Thời gian sự kiện là lúc việc xảy ra; xử lý theo thời gian sự kiện cho kết quả đúng và ổn định khi chạy lại, còn xử lý theo thời gian tới thì kết quả đổi mỗi lần chạy lại. Mốc nước là ước lượng của engine về thời điểm mà mọi sự kiện trước đó coi như đã tới; nó điều khiển thời điểm đóng cửa sổ và giải phóng trạng thái. Đánh đổi trung tâm phải đo: **mốc nước rộng cho kết quả đầy đủ hơn nhưng trễ hơn và giữ trạng thái lâu hơn**, mốc nước hẹp cho kết quả sớm nhưng bỏ nhiều sự kiện muộn. Độ trễ cho phép quyết định cửa sổ đã đóng còn nhận cập nhật không. Sự kiện tới sau ngưỡng phải có chính sách rõ: bỏ có ghi nhận, đưa vào luồng riêng, hoặc hiệu chỉnh về sau; **bỏ im lặng là chế độ hỏng**.

**Outcome.** Đo đánh đổi giữa độ trễ và tính đầy đủ theo ba mức mốc nước và áp chính sách rõ cho sự kiện quá muộn.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn tham số từ số đo chứ từ giá trị mặc định. Kiểm bằng ba mức mốc nước; đạt khi mỗi mức có cặp số độ trễ với tỉ lệ sự kiện bị bỏ, và sự kiện quá muộn không bị bỏ im lặng.

**Lab.** Sinh dòng sự kiện có phân bố độ trễ thực tế gồm một phần đuôi rất muộn. Chạy với ba mức mốc nước; với mỗi mức, đo độ trễ tới khi có kết quả, tỉ lệ sự kiện bị bỏ, và kích thước trạng thái. Chọn một mức và nêu lý do. Cài chính sách cho sự kiện quá muộn và chứng minh chúng được đếm và ghi nhận chứ bỏ.

**Pitfalls.** Xử lý theo thời gian tới rồi chạy lại ra kết quả khác · đặt mốc nước theo giá trị mặc định · bỏ sự kiện muộn im lặng · bỏ qua ảnh hưởng của mốc nước lên kích thước trạng thái.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba mức mốc nước có cặp số độ trễ với tỉ lệ bỏ cùng kích thước trạng thái, và sự kiện quá muộn được đếm và ghi nhận.

### Lesson 358 · Choosing among four engine classes - distributed, embedded and in-process `TH`
**Prerequisites.** Lesson 357

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài mở rộng phạm vi chọn engine ra bốn lớp, vì hai engine phân tán không phải lựa chọn duy nhất và thường không phải lựa chọn đúng. Engine dòng chảy thứ hai học tới mức hiểu kiến trúc và khác biệt, đi sâu chỉ khi công việc yêu cầu. Khác biệt nền tảng: nó xử lý từng bản ghi thay vì theo lô nhỏ, nên độ trễ thấp hơn đáng kể, đổi lại mô hình vận hành phức tạp hơn. Đồ thị toán tử, khe tác vụ và mức song song; nhóm khoá quyết định trạng thái được chia thế nào và quyết định mức song song đổi được tới đâu. Trạng thái theo khoá và trạng thái theo toán tử. Điểm kiểm tra dùng rào chắn chèn vào dòng: khi rào chắn đi qua mọi toán tử thì một ảnh chụp nhất quán được tạo mà không cần dừng dòng; chế độ căn chỉnh và không căn chỉnh khác nhau ở độ trễ dưới áp lực ngược. **Điểm lưu khác điểm kiểm tra ở mục đích: điểm kiểm tra do hệ tạo để phục hồi tự động, điểm lưu do người tạo để nâng cấp và di trú.** Áp lực ngược lan ngược về nguồn và làm điểm kiểm tra chậm hoặc hết giờ. Lớp thứ ba và thứ tư là engine chạy trên một máy, véctơ hoá theo lesson 208: một thư viện khung dữ liệu và một engine phân tích nhúng. **Với dữ liệu vừa bộ nhớ hoặc vừa đĩa của một máy, chúng thường nhanh hơn engine phân tán** vì không có chi phí xáo trộn, chi phí tuần tự hoá và chi phí lập lịch; ngưỡng chuyển sang phân tán phải đo chứ đoán. Mô hình lập trình theo đồ thị tính toán có nhiều bộ chạy chỉ cần biết là có. Quy tắc chọn: **engine đơn giản nhất còn đáp ứng được dữ liệu và độ trễ là engine đúng.**

**Outcome.** So bốn lớp engine theo năm tiêu chí và chọn đúng cho ba bối cảnh, phân biệt điểm kiểm tra với điểm lưu.

**Đánh giá.** Tầng *đánh giá*. Objective chống lại việc mặc định chọn engine phân tán. Kiểm bằng bảng bốn lớp nhân năm tiêu chí cộng một phép đo; đạt khi ba bối cảnh chọn đúng, ít nhất một bối cảnh chọn engine một máy, và ngưỡng chuyển sang phân tán có số đo.

**Lab.** So bốn lớp engine theo độ trễ, quy mô dữ liệu, mô hình trạng thái, chi phí vận hành và hệ sinh thái. Chạy một công việc đếm theo cửa sổ trên engine dòng chảy, giết một tiến trình quản lý tác vụ và khôi phục từ điểm kiểm tra; tạo một điểm lưu, đổi mức song song rồi khôi phục từ điểm lưu. Chạy **cùng một phép tổng hợp trên cả engine phân tán lẫn hai engine một máy** với ba kích thước dữ liệu tăng dần; tìm kích thước mà engine phân tán bắt đầu thắng. Cho ba bối cảnh khác nhau về quy mô và độ trễ, chọn engine cho từng cái.

**Pitfalls.** Chọn engine theo độ phổ biến · **dùng engine phân tán cho dữ liệu vừa một máy** · nhầm điểm lưu với điểm kiểm tra · học sâu cả hai engine phân tán cùng lúc · bỏ qua chi phí vận hành khi so.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng bốn lớp nhân năm tiêu chí có luận điểm kèm quan sát từ lab, ngưỡng chuyển sang engine phân tán có số đo từ ba kích thước dữ liệu, ba bối cảnh chọn đúng với ít nhất một chọn engine một máy, và khôi phục từ cả điểm kiểm tra lẫn điểm lưu thành công.

### Lesson 359 · End-to-end guarantee - source replay, state restore and sink `TH`
**Prerequisites.** Lesson 358

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài phát biểu chính xác bảo đảm đầu cuối của một đường dòng chảy, và nó là bài chống lại tuyên bố mơ hồ. Bảo đảm đầu cuối là tích của ba điều kiện chứ một tính năng bật được: nguồn phải phát lại được từ một vị trí; trạng thái phải khôi phục được nhất quán với vị trí đó; và đích phải luỹ đẳng hoặc có giao dịch. **Thiếu một trong ba thì không có bảo đảm, dù engine có cờ nào bật đi nữa**; và đích là mắt xích hay bị bỏ quên nhất. Ba loại đích và cách đạt: đích có giao dịch thì chốt cùng tiến độ; đích luỹ đẳng theo khoá thì ghi đè an toàn; đích chỉ thêm mới thì không đạt được và phải chấp nhận trùng. Ghi ra hệ ngoài như gửi thư hoặc gọi dịch vụ là tác dụng phụ không hoàn tác được, nên nó luôn là ít nhất một lần. Phát biểu bảo đảm phải nêu nguồn, đích và giả định lỗi, theo lesson 326.

**Outcome.** Phát biểu bảo đảm đầu cuối cho ba cấu hình và chứng minh bằng thí nghiệm giết có đối soát.

**Đánh giá.** Tầng *đánh giá*. Objective đòi phát biểu có điều kiện thay vì tuyên bố. Kiểm bằng ba cấu hình đích; đạt khi phát biểu khớp kết quả đo ở cả ba và cấu hình đích chỉ thêm mới được nêu rõ không đạt được đúng một lần.

**Lab.** Dựng cùng một đường dòng chảy với ba loại đích. Với mỗi cái, phát biểu bảo đảm đầu cuối trước khi thử. Giết tiến trình 50 lần ở các ranh giới khác nhau; đếm bản ghi mất và trùng ở đích rồi đối chiếu với phát biểu. Thêm một bước gọi dịch vụ ngoài và chỉ ra vì sao nó luôn là ít nhất một lần.

**Pitfalls.** Tuyên bố đúng một lần vì engine hỗ trợ · bỏ qua đích khi phát biểu bảo đảm · dùng đích chỉ thêm mới rồi mong không trùng · không nêu giả định lỗi.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phát biểu khớp kết quả đo ở cả ba cấu hình sau 50 lần giết, và cấu hình đích chỉ thêm mới được nêu rõ giới hạn.

### Lesson 360 · Gate 8 - defend a delivery semantic and recover a stateful job `KT`
**Prerequisites.** Lesson 359

**In-class (180 phút).** 135 phút làm bài độc lập · 45 phút chữa bài và phân tích lỗi theo nhóm

**Learn.** Cổng của Phase 8. Bài kiểm bốn module: nền tảng hệ phân tán ở M15, nhật ký phân tán ở M16, bắt thay đổi ở M17, và engine tính toán ở M18. Không có nội dung mới.

**Outcome.** Phát biểu và bảo vệ một bảo đảm giao nhận có nêu ranh giới, phục hồi một công việc có trạng thái, và giải thích song song lồng nhau bằng số đo.

**Đánh giá.** Tầng *đánh giá*. Cổng đo năng lực lập luận về bảo đảm và năng lực vận hành dưới hỏng, nên hình thức là thực hành tại chỗ cộng bảo vệ.

**Lab.** Buổi 180 phút: 135 phút làm bài độc lập, 45 phút chữa bài. Bài chấm sáu phần: A (20đ) cho một lịch sử thao tác, xác định mô hình nhất quán bị vi phạm kèm chuỗi chứng minh · B (20đ) phát biểu bảo đảm giao nhận đầu cuối của một đường cho trước, nêu nguồn, đích và giả định lỗi, rồi tính số bản trùng và lượng mất tối đa · C (15đ) tái hiện và sửa một ca người dẫn cũ quay lại bằng thẻ chặn · D (20đ) một công việc dòng có trạng thái bị giết; khôi phục từ điểm kiểm tra và đối soát · E (15đ) truy ba tầng song song trên một công việc và quy một mức tăng về đúng tầng · F (10đ) chẩn đoán một công việc chậm và đề xuất đúng một thay đổi có kiểm soát.

**Pitfalls.** Coi hết giờ là bên kia đã hỏng · nói đúng một lần mà không nêu ranh giới · đặt lại vị trí tiêu thụ về cuối để phục hồi · đổi cấu hình bộ nhớ trước khi đọc kế hoạch.

**Self-study (2,4 giờ).** Không có bài tự học. Nếu không đạt, theo phụ lục khắc phục khi không đạt cổng

**Done when.** Đạt ≥ 70/100, phần B và D đều ≥ 60%. Tuyên bố đúng một lần không nêu nguồn, đích và giả định lỗi thì phần B bằng không; phục hồi bằng cách đặt lại vị trí về cuối thì phần D bằng không.

# MODULE M19 · CLOUD ABSTRACTIONS BEFORE SERVICE NAMES

**Phase 9 · Lessons 361–372 · 24 giờ**

| | |
|---|---|
| **Objective cấp module** | Gọi tên trừu tượng cần dùng trước khi chọn dịch vụ, rồi triển khai một lát cắt nền tảng trên một đám mây có danh tính, mạng, đường dữ liệu, miền hỏng và ranh giới chi phí |
| **Tiền đề** | M5 · M6 · M10 · M15 |
| **Exit criterion** | Không có khoá tĩnh trong kho mã; quyền tối thiểu có lý do và có bằng chứng kiểm toán; phục hồi và chuyển dự phòng đã thử; chi phí hằng tháng cùng ba yếu tố nhạy cảm nhất được nêu ra |
| **Kỹ năng SFIA** | `ARCH` mức 4 · `ITMG` mức 4 · `SCTY` mức 4 |
| **Chế độ hỏng** | Dùng khoá tĩnh hoặc tài khoản cao nhất cho nhanh, mở công khai như một lối tắt, và trừu tượng hoá đa đám mây trước khi một đám mây chạy được |

Module có một quy tắc thứ tự tường minh: **gọi tên trừu tượng trước, chọn dịch vụ sau**. Với mỗi trừu tượng, có một câu hỏi phải trả lời và một bằng chứng phải đưa ra trước khi được phép nêu tên bất kỳ dịch vụ nào.

Chọn một đám mây để thành thạo theo tín hiệu thật từ nơi làm việc hoặc thị trường mục tiêu; hai đám mây còn lại chỉ tới mức ánh xạ trừu tượng. **Đa đám mây chỉ ở mức nhận biết cho tới khi một đám mây đã chạy được ở mức sản xuất.**

Ba thứ được kiểm ở mọi bài và ở cổng: danh tính, ranh giới tin cậy của mạng, và chi phí trên mỗi đơn vị công việc.

### Lesson 361 · Regions, zones, failure domains and shared responsibility `LT`
**Prerequisites.** Module 19: M15

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài mở module bằng ba khái niệm quyết định mọi quyết định kiến trúc về sau. Vùng và khu khả dụng là các miền hỏng: hai tài nguyên trong cùng một khu có thể hỏng cùng lúc, hai khu khác nhau thì độc lập hơn nhưng không độc lập hoàn toàn vì chúng vẫn dùng chung mặt phẳng điều khiển của vùng. Mặt phẳng điều khiển và mặt phẳng dữ liệu hỏng độc lập: **mặt phẳng điều khiển hỏng thì không tạo được tài nguyên mới và không chuyển dự phòng được, trong khi tài nguyên đang chạy vẫn phục vụ**, và phân biệt hai trạng thái này khi trực là quan trọng, đúng như ở lesson 330. Trách nhiệm chia sẻ: nhà cung cấp lo phần dưới một đường kẻ, khách hàng lo phần trên, và đường kẻ đó khác nhau giữa dịch vụ tự quản với dịch vụ được quản lý; hiểu sai đường kẻ tạo ra khoảng trống không ai lo, thường là sao lưu, vá lỗi và cấu hình truy cập.

**Outcome.** Vẽ miền hỏng cho một kiến trúc và chỉ đúng đường kẻ trách nhiệm cho bốn dịch vụ.

**Đánh giá.** Tầng *hiểu*. Bài mở module, đặt từ vựng. Kiểm bằng bài phân định; đạt khi vẽ đúng miền hỏng và chỉ đúng phần khách hàng phải lo ở ít nhất ba trong bốn dịch vụ.

**Lab.** Cho một kiến trúc bốn thành phần; vẽ sơ đồ miền hỏng và chỉ ra thành phần nào cùng chết khi mất một khu khả dụng. Với bốn dịch vụ thuộc bốn mức quản lý khác nhau, liệt kê phần nhà cung cấp lo và phần mình lo. Tìm ba khoảng trống không ai lo trong một kiến trúc thật.

**Pitfalls.** Giả định dịch vụ được quản lý thì không cần sao lưu · coi nhiều khu khả dụng là thay được sao lưu · nhầm sự cố mặt phẳng điều khiển với sự cố mặt phẳng dữ liệu · vẽ kiến trúc mà không đánh dấu miền hỏng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Sơ đồ miền hỏng đúng cho kiến trúc bốn thành phần, và phần trách nhiệm khách hàng đúng ở ≥ 3/4 dịch vụ kèm ba khoảng trống tìm được.

### Lesson 362 · Identity before services - principal, role, least privilege `TH`
**Prerequisites.** Lesson 361

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Danh tính là trừu tượng phải chốt trước mọi thứ khác, vì mọi lỗi bảo mật lớn đều bắt đầu ở đây. Bốn câu hỏi trước khi cấp quyền: ai đóng vai gì, từ đâu, trong bao lâu, và để làm gì. Chủ thể có thể là người hoặc là khối lượng công việc; danh tính cho khối lượng công việc là cách bỏ hẳn khoá tĩnh, vì tiến trình lấy thông tin xác thực ngắn hạn từ môi trường chạy thay vì đọc từ tệp. **Khoá tĩnh trong kho mã là chế độ hỏng tự động chưa đạt của module**, và nó được kiểm bằng máy chứ bằng lời hứa. Chính sách gắn vào danh tính khác chính sách gắn vào tài nguyên, và hai loại giao nhau theo cách phải hiểu để gỡ lỗi từ chối. Quyền tối thiểu đạt được bằng cách bắt đầu từ không có gì rồi thêm theo lỗi từ chối thật, chứ bắt đầu từ ký tự đại diện rồi thu hẹp. Bằng chứng bắt buộc: một phép thử cho thấy bị từ chối và một phép thử cho thấy được phép, cùng bản ghi kiểm toán tương ứng.

**Outcome.** Cấp quyền tối thiểu cho ba khối lượng công việc bằng danh tính cho khối lượng công việc, có bằng chứng kiểm toán hai chiều.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu bằng phép thử hai chiều chứ bằng rà soát chính sách. Kiểm bằng sáu phép thử; đạt khi ba phép thử được phép thành công, ba phép thử bị từ chối đúng, và không khoá tĩnh nào tồn tại trong kho mã.

**Lab.** Với ba khối lượng công việc, bắt đầu từ chính sách rỗng và thêm quyền theo từng lỗi từ chối thật; ghi lại lý do cho mỗi quyền. Chuyển toàn bộ sang danh tính cho khối lượng công việc và xoá mọi khoá tĩnh. Chạy sáu phép thử hai chiều và đối chiếu với bản ghi kiểm toán. Chạy một bộ quét chặn khoá tĩnh trong kho mã.

**Pitfalls.** Bắt đầu bằng ký tự đại diện rồi định thu hẹp sau · dùng tài khoản cao nhất cho việc thường ngày · để khoá tĩnh trong biến môi trường của kho mã · không chạy phép thử bị từ chối.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba phép thử được phép thành công và ba phép thử bị từ chối đúng, mỗi quyền có lý do ghi lại, và bộ quét không tìm thấy khoá tĩnh nào.

### Lesson 363 · Network - CIDR, route, trust boundary, egress and DNS `TH`
**Prerequisites.** Lesson 362

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Trừu tượng thứ hai: đường đi của gói tin và ranh giới tin cậy, dựng trên nền M6. Mạng riêng chia thành các dải địa chỉ; dải công khai có đường ra thẳng, dải riêng thì không và phải đi qua một cổng dịch địa chỉ hoặc một điểm cuối riêng để tới dịch vụ của nhà cung cấp. Bảng định tuyến quyết định gói đi đâu; quy tắc tường lửa quyết định gói nào được qua. Hai lựa chọn cho lưu lượng ra và đánh đổi phải tính bằng tiền: cổng dịch địa chỉ tính phí theo lượng dữ liệu nên nó là nguồn hoá đơn bất ngờ hay gặp, còn điểm cuối riêng giữ lưu lượng trong mạng nhà cung cấp và thường rẻ hơn cùng an toàn hơn. Phân giải tên và cân bằng tải. **Nhóm bảo mật mở cho toàn bộ internet là một lối tắt bị cấm**, kể cả trong môi trường thử. Bằng chứng bắt buộc của bài là một sơ đồ đường đi gói tin, không phải một sơ đồ hộp.

**Outcome.** Dựng mạng có dải riêng không đi ra internet trực tiếp và vẽ được sơ đồ đường đi gói tin có bằng chứng.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là đường đi thật quan sát được. Kiểm bằng phép thử kết nối; đạt khi tài nguyên ở dải riêng không ra được internet trực tiếp, vẫn gọi được dịch vụ qua điểm cuối riêng, và sơ đồ khớp kết quả truy vết thật.

**Lab.** Dựng mạng có dải công khai và dải riêng, cổng dịch địa chỉ và ít nhất một điểm cuối riêng. Từ một máy ở dải riêng, thử ra internet trực tiếp và xác nhận bị chặn; thử gọi dịch vụ nhà cung cấp qua điểm cuối riêng và xác nhận thành công. Truy vết đường đi và vẽ sơ đồ. So chi phí ước tính giữa đi qua cổng dịch địa chỉ và đi qua điểm cuối riêng cho một khối lượng cho trước.

**Pitfalls.** Mở quy tắc cho toàn bộ internet để gỡ lỗi nhanh · đặt mọi thứ ở dải công khai · bỏ qua chi phí lưu lượng qua cổng dịch địa chỉ · vẽ sơ đồ hộp thay vì sơ đồ đường đi gói tin.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tài nguyên ở dải riêng bị chặn ra internet nhưng gọi được dịch vụ qua điểm cuối riêng, và sơ đồ khớp kết quả truy vết thật.

### Lesson 364 · Compute - state, startup, scale unit and replacement `TH`
**Prerequisites.** Lesson 363

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Trừu tượng thứ ba, và bốn câu hỏi quyết định chọn dạng tính toán nào. Trạng thái nằm ở đâu: nếu nằm trong máy thì thay máy là mất dữ liệu. Thời gian khởi động bao lâu: quyết định phản ứng được với tải đột biến hay không. Đơn vị mở rộng là gì: một máy, một vùng chứa, hay một lời gọi hàm. Thay thế ra sao khi một đơn vị chết. Ba dạng và điều kiện dùng: máy ảo cho khối lượng công việc cần kiểm soát môi trường; vùng chứa được quản lý cho dịch vụ dài hạn không muốn nuôi cụm; hàm không máy chủ cho việc ngắn theo sự kiện, với ba giới hạn phải biết là thời gian chạy tối đa, khởi động nguội, và trạng thái không giữ được giữa hai lần gọi. **Ảnh máy bất biến cộng thay thế thay vì sửa tại chỗ** là nguyên tắc chung, và nó là điều kiện để dựng lại được từ mã ở lesson 371.

**Outcome.** Chọn dạng tính toán cho ba khối lượng công việc theo bốn câu hỏi và chứng minh mất một đơn vị không mất dữ liệu.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu bằng diễn tập mất máy. Kiểm bằng phép thử giết; đạt khi dịch vụ tự thay thế đơn vị đã mất và không dữ liệu nào nằm lại trên đơn vị đó.

**Lab.** Cho ba khối lượng công việc; trả lời bốn câu hỏi cho từng cái rồi chọn dạng tính toán. Triển khai một cái theo nhóm tự mở rộng dùng ảnh bất biến. Giết một đơn vị và đo thời gian tới khi đơn vị thay thế phục vụ được. Chứng minh không có trạng thái nằm lại trên đơn vị bị giết. Đo khởi động nguội của một hàm không máy chủ.

**Pitfalls.** Lưu trạng thái trên đĩa cục bộ của máy tự mở rộng · sửa cấu hình trên máy đang chạy thay vì dựng ảnh mới · chọn hàm không máy chủ cho việc chạy dài · bỏ qua khởi động nguội khi hứa độ trễ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đơn vị bị giết được thay thế tự động với thời gian đo được, và không dữ liệu nào nằm lại trên đơn vị đó.

### Lesson 365 · Storage and managed databases chosen by the data contract `TH`
**Prerequisites.** Lesson 364

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Trừu tượng thứ tư và thứ năm, chọn theo hợp đồng dữ liệu chứ theo tên dịch vụ. Ba dạng lưu trữ và ranh giới dùng: kho đối tượng cho dữ liệu bất biến quy mô lớn với ngữ nghĩa đã học ở lesson 224; khối cho đĩa gắn vào một máy; tệp chia sẻ cho nhiều máy cùng đọc ghi. Bốn thuộc tính phải hỏi trước: tính nhất quán, độ bền, độ khả dụng, và vòng đời cùng phiên bản cùng sao chép. **Độ bền và độ khả dụng là hai con số khác nhau**: dữ liệu bền tuyệt đối vẫn có thể không truy cập được trong một sự cố, nên hứa hẹn của nhà cung cấp phải đọc đúng cột. Cơ sở dữ liệu được quản lý chọn theo hợp đồng giao dịch, quy mô, cách chuyển dự phòng và đường kết nối; chuyển dự phòng nhiều khu không thay sao lưu, vì nó nhân bản cả một lệnh xoá nhầm. Đường mạng tới cơ sở dữ liệu và giới hạn số kết nối là hai chỗ hay bị bỏ qua tới khi có tải thật.

**Outcome.** Chọn lưu trữ và cơ sở dữ liệu cho ba hợp đồng dữ liệu và chứng minh khác biệt giữa độ bền với độ khả dụng.

**Đánh giá.** Tầng *đánh giá*. Objective đòi đọc đúng hợp đồng của nhà cung cấp chứ so tên dịch vụ. Kiểm bằng ba lựa chọn cộng một diễn tập; đạt khi mỗi lựa chọn dẫn từ bốn thuộc tính và diễn tập chuyển dự phòng cho số đo gián đoạn thật.

**Lab.** Cho ba hợp đồng dữ liệu khác nhau; chọn lưu trữ và cơ sở dữ liệu cho từng cái kèm lý do theo bốn thuộc tính. Bật phiên bản và vòng đời trên kho đối tượng, rồi xoá nhầm một đối tượng và khôi phục. Kích hoạt chuyển dự phòng của cơ sở dữ liệu nhiều khu và đo thời gian gián đoạn cùng số kết nối bị đứt.

**Pitfalls.** Coi nhiều khu là đã có sao lưu · đọc nhầm độ bền thành độ khả dụng · bỏ qua giới hạn số kết nối tới cơ sở dữ liệu · chọn dịch vụ theo tên rồi ép hợp đồng dữ liệu vào nó.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba lựa chọn dẫn từ bốn thuộc tính, khôi phục được đối tượng xoá nhầm, và chuyển dự phòng có số đo thời gian gián đoạn.

### Lesson 366 · Messaging services mapped by delivery semantics `TH`
**Prerequisites.** Lesson 365

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Trừu tượng thứ sáu, và bài này ánh xạ thẳng từ M16 sang các dịch vụ được quản lý. Bốn câu hỏi trước khi chọn: thứ tự được giữ ở phạm vi nào, ngữ nghĩa giao nhận là gì, thời hạn giữ bao lâu, và đọc lại được không. Bốn nhóm dịch vụ tương ứng bốn ngữ nghĩa: hàng đợi giao mỗi thông điệp cho một bên tiêu thụ rồi xoá; phát hành đăng ký gửi cho mọi bên đăng ký; bus sự kiện định tuyến theo quy tắc; nhật ký phân tán giữ lại và đọc lại được. **Chọn nhầm nhóm thì không sửa được bằng cấu hình**, vì thời hạn giữ và khả năng đọc lại là thuộc tính của nhóm chứ một tham số. Giới hạn của dịch vụ được quản lý phải đọc trước: kích thước thông điệp tối đa, số bên tiêu thụ, thời hạn giữ tối đa, và hạn mức tốc độ. Bằng chứng bắt buộc: một diễn tập tạo bản trùng hoặc mất thông điệp, giống lesson 328.

**Outcome.** Ánh xạ bốn ngữ nghĩa sang dịch vụ được quản lý và chứng minh bằng diễn tập trùng lặp hoặc mất.

**Đánh giá.** Tầng *áp dụng*. Objective đòi kiểm ngữ nghĩa bằng thực nghiệm chứ đọc tài liệu. Kiểm bằng diễn tập; đạt khi ngữ nghĩa quan sát được khớp ngữ nghĩa đã tuyên bố ở cả hai dịch vụ và giới hạn dịch vụ được ghi lại.

**Lab.** Chọn hai dịch vụ thuộc hai nhóm khác nhau. Với mỗi cái, trả lời bốn câu hỏi bằng tài liệu rồi kiểm bằng thực nghiệm: giết bên tiêu thụ giữa chừng và đếm bản trùng hoặc mất; thử đọc lại từ một thời điểm cũ. Ghi lại bốn giới hạn của dịch vụ. Chỉ ra một yêu cầu mà nhóm đã chọn không đáp ứng được.

**Pitfalls.** Chọn hàng đợi rồi cần đọc lại · tin ngữ nghĩa theo tài liệu mà không kiểm · bỏ qua giới hạn kích thước thông điệp · coi dịch vụ được quản lý là miễn trừ khỏi việc khử trùng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ngữ nghĩa quan sát được khớp tuyên bố ở cả hai dịch vụ, bốn giới hạn được ghi lại, và một yêu cầu không đáp ứng được chỉ ra.

### Lesson 367 · Reliability - failure domains, RPO and RTO with a tested restore `TH`
**Prerequisites.** Lesson 366

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Độ tin cậy phát biểu bằng hai con số và chúng phải đo được chứ tuyên bố. Mục tiêu điểm phục hồi là lượng dữ liệu chấp nhận mất tính theo thời gian; mục tiêu thời gian phục hồi là thời gian chấp nhận ngừng phục vụ. Hai con số này quyết định kiến trúc chứ ngược lại. Nhiều khu khả dụng chống mất một khu; nhiều vùng chống mất một vùng và đắt hơn nhiều; sao lưu chống lỗi logic mà hai cái kia không chống được. **Một bản sao lưu chưa được phục hồi thử thì không phải bản sao lưu**, và ba nguyên nhân làm phục hồi thất bại dù bản sao lưu tồn tại là thiếu quyền, thiếu khoá mã hoá, và bản sao lưu nằm trong cùng tài khoản đã bị xoá. Hạn mức và phụ thuộc bên ngoài là miền hỏng thứ tư hay bị quên: hết hạn mức thì không tạo được tài nguyên thay thế giữa lúc sự cố.

**Outcome.** Đo được cả hai con số phục hồi bằng một lần phục hồi thật vào môi trường sạch.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là số đo từ một lần phục hồi thật, không phải một kế hoạch. Kiểm bằng diễn tập phục hồi; đạt khi hai con số đo được, dữ liệu sau phục hồi đối soát khớp, và ba nguyên nhân thất bại được kiểm tường minh.

**Lab.** Đặt mục tiêu hai con số cho một dịch vụ. Tạo sao lưu và phục hồi vào một tài khoản hoặc dự án sạch; bấm giờ và đối soát dữ liệu. Kiểm ba nguyên nhân thất bại bằng cách thử phục hồi khi thiếu quyền và khi thiếu khoá. Mất một khu khả dụng có kiểm soát và đo lại. Kiểm hạn mức còn đủ để tạo tài nguyên thay thế.

**Pitfalls.** Coi có lịch sao lưu là có khả năng phục hồi · phục hồi vào chính môi trường cũ nên không kiểm được phụ thuộc · để sao lưu cùng tài khoản với dữ liệu gốc · bỏ qua hạn mức khi lập kế hoạch phục hồi.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Hai con số phục hồi đo được từ một lần phục hồi thật vào môi trường sạch, dữ liệu đối soát khớp, và ba nguyên nhân thất bại được kiểm.

### Lesson 368 · Cost - unit economics, egress and the budget alarm `TH`
**Prerequisites.** Lesson 367

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Chi phí là một ràng buộc thiết kế và phải đo theo đơn vị công việc chứ theo tổng hoá đơn. Sáu thành phần: số yêu cầu, thời gian tính toán, dung lượng lưu trữ, thao tác vào ra, lưu lượng ra ngoài, và năng lực nhàn rỗi. Hai thành phần hay gây bất ngờ nhất là lưu lượng ra ngoài theo lesson 363 và năng lực nhàn rỗi, vì cả hai không tỉ lệ với lượng công việc hữu ích. Chi phí trên mỗi đơn vị là con số so sánh được: chi phí trên mỗi nghìn yêu cầu, trên mỗi lần làm mới bảng, trên mỗi người dùng hoạt động, nối với lesson 198. Gắn thẻ tài nguyên là điều kiện để quy chi phí về đội và về sản phẩm; không gắn thẻ thì không quy được và không ai chịu trách nhiệm. **Cảnh báo ngân sách phải đặt trước khi chạy khối lượng công việc mới**, không phải sau khi nhận hoá đơn. Cam kết dài hạn chỉ hợp lý sau khi đã có dữ liệu sử dụng ổn định.

**Outcome.** Tính chi phí trên mỗi đơn vị cho ba khối lượng công việc và dựng cảnh báo ngân sách trước khi chạy.

**Đánh giá.** Tầng *áp dụng*. Objective đòi nối chi phí với đơn vị công việc chứ đọc tổng hoá đơn. Kiểm bằng đối chiếu ước tính với hoá đơn thật; đạt khi sai lệch dưới ngưỡng thoả thuận ở cả ba và cảnh báo ngân sách kích hoạt đúng ngưỡng.

**Lab.** Với ba khối lượng công việc, ước tính sáu thành phần chi phí trước khi chạy. Gắn thẻ mọi tài nguyên. Chạy một chu kỳ rồi đối chiếu ước tính với chi phí thật và giải thích chênh lệch. Tính chi phí trên mỗi đơn vị cho từng cái. Dựng cảnh báo ngân sách và kích hoạt nó bằng một khối lượng thử. Xác định ba yếu tố nhạy cảm nhất.

**Pitfalls.** Đọc tổng hoá đơn mà không quy về đơn vị công việc · bỏ lưu lượng ra ngoài khỏi ước tính · không gắn thẻ nên không quy được chi phí · cam kết dài hạn trước khi có dữ liệu sử dụng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Sai lệch giữa ước tính và chi phí thật dưới ngưỡng ở cả ba, chi phí trên mỗi đơn vị tính được, và cảnh báo ngân sách kích hoạt đúng.

### Lesson 369 · Secrets, keys and the audit trail `TH`
**Prerequisites.** Lesson 368

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài chốt phần bảo mật nền tảng bằng ba cơ chế. Kho bí mật giữ thông tin xác thực ngoài mã và ngoài ảnh máy, và cho phép xoay mà không sửa mã; xoay phải thử được chứ để trong tài liệu. Dịch vụ quản lý khoá giữ khoá mã hoá và ghi lại mọi lần dùng; điểm quan trọng và hay bị bỏ qua: **ai sở hữu khoá thì thực sự kiểm soát dữ liệu**, nên khoá nằm ở tài khoản khác với dữ liệu là một biện pháp phòng vệ thật. Mã hoá khi truyền và khi lưu là hai lớp khác nhau và cả hai đều cần. Nhật ký kiểm toán ghi ai làm gì lúc nào; nó chỉ có giá trị nếu được giữ ở nơi mà kẻ tấn công không xoá được, nên tách tài khoản lưu nhật ký là thực hành chuẩn. Ba phép kiểm tự động phải chạy trong tích hợp liên tục: không có khoá tĩnh, không có tài nguyên mở công khai ngoài ý muốn, và không có chính sách dùng ký tự đại diện.

**Outcome.** Dựng ba cơ chế và chứng minh xoay thông tin xác thực không gián đoạn cùng nhật ký kiểm toán đầy đủ.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là xoay thật và truy vết thật. Kiểm bằng phép thử xoay cộng truy vết; đạt khi xoay không gây gián đoạn, mọi thao tác nhạy cảm truy được trong nhật ký, và ba phép kiểm tự động chặn đúng vi phạm tiêm.

**Lab.** Chuyển toàn bộ thông tin xác thực sang kho bí mật. Thực hiện một lần xoay khi dịch vụ đang chạy và đo gián đoạn. Mã hoá một tập dữ liệu bằng khoá do mình quản lý; thu hồi quyền dùng khoá và chứng minh dữ liệu không đọc được. Tách tài khoản lưu nhật ký. Tiêm ba vi phạm và xác nhận ba phép kiểm tự động chặn được.

**Pitfalls.** Xoay bằng cách dừng dịch vụ · để khoá mã hoá cùng tài khoản với dữ liệu · lưu nhật ký kiểm toán trong chính tài khoản bị kiểm · coi mã hoá khi lưu là đủ khi thiếu kiểm soát khoá.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Xoay thông tin xác thực không gây gián đoạn, thao tác nhạy cảm truy được trong nhật ký, và ba vi phạm tiêm đều bị chặn.

### Lesson 370 · The primitive table - mapping one cloud to the others `LT`
**Prerequisites.** Lesson 369

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài cuối phần lý thuyết, và nó chỉ được học sau khi đã triển khai trên một đám mây. Bảng trừu tượng liệt kê bảy trừu tượng ở các bài trước theo hàng và ba nhà cung cấp theo cột, mỗi ô ghi tên dịch vụ tương ứng. Nhưng giá trị của bảng nằm ở cột thứ tư: **khác biệt về ngữ nghĩa, chứ khác biệt về tên**. Bốn chỗ khác biệt thật và phải ghi rõ: mô hình danh tính và cách chính sách giao nhau; mô hình mạng và cách lưu lượng ra được tính tiền; sự kiện của kho đối tượng có bảo đảm gì về thứ tự và về giao nhận; và cơ sở dữ liệu được quản lý khác nhau ở cách chuyển dự phòng cùng giới hạn kết nối. Cảnh báo về trừu tượng hoá sớm: xây một lớp trừu tượng chung cho nhiều đám mây trước khi một đám mây chạy được là cách chắc chắn có một lớp sai ở cả hai phía.

**Outcome.** Lập bảng ánh xạ bảy trừu tượng và ghi được khác biệt ngữ nghĩa chứ chỉ khác biệt tên.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết đặt sau khi đã triển khai, đúng thứ tự của hợp đồng nguồn. Kiểm bằng bảng ánh xạ; đạt khi mỗi hàng có ít nhất một khác biệt ngữ nghĩa cụ thể chứ chỉ tên dịch vụ.

**Lab.** Lập bảng bảy trừu tượng nhân ba nhà cung cấp. Với bốn hàng quan trọng nhất, tra tài liệu chính thức và ghi khác biệt ngữ nghĩa cụ thể kèm ngày tra. Chọn một kiến trúc đã dựng và mô tả nó phải đổi gì nếu chuyển sang đám mây khác. Viết hai câu nêu vì sao chưa nên xây lớp trừu tượng chung lúc này.

**Pitfalls.** Lập bảng chỉ ghi tên dịch vụ · kết luận hai dịch vụ tương đương vì cùng loại · học ba đám mây song song · xây lớp trừu tượng chung trước khi một đám mây chạy được.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mỗi hàng có ít nhất một khác biệt ngữ nghĩa cụ thể kèm nguồn và ngày tra, và bốn hàng quan trọng nhất có mô tả thay đổi khi chuyển đám mây.

### Lesson 371 · Landing zone project - one cloud, one data service `DA`
**Prerequisites.** Lesson 370

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Bài dự án khép module. Dựng một lát cắt nền tảng trên đám mây đã chọn, gồm: ranh giới tài khoản hoặc dự án theo môi trường; danh tính với quyền tối thiểu và danh tính cho khối lượng công việc; mạng có dải riêng, đường ra được kiểm soát và ít nhất một điểm cuối riêng; một dịch vụ dữ liệu gồm giao diện lập trình, cơ sở dữ liệu và một đường xử lý ghi ra kho đối tượng; bí mật và khoá theo lesson 369; nhật ký, số đo và nhật ký kiểm toán; sao lưu cùng một lần phục hồi đã thử; và gắn thẻ cùng cảnh báo ngân sách. Toàn bộ phải dựng bằng mã theo M20, để dựng lại được từ đầu. Nộp kèm sơ đồ kiến trúc có đủ năm thứ: danh tính, mạng, đường dữ liệu, miền hỏng và ranh giới chi phí; và một bảng chi phí hằng tháng kèm ba yếu tố nhạy cảm nhất.

**Outcome.** Nộp lát cắt nền tảng dựng lại được từ mã, không có khoá tĩnh, có phục hồi đã thử và chi phí đã đo.

**Đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module. Kiểm bằng dựng lại từ đầu cộng rà soát bằng chứng; đạt khi môi trường dựng lại được từ mã trong môi trường sạch, phục hồi thành công với đối soát, và không có khoá tĩnh hay tài nguyên mở công khai ngoài ý muốn.

**Lab.** Dựng lát cắt nền tảng đầy đủ bằng mã. Xoá sạch môi trường rồi dựng lại từ đầu chỉ bằng mã và sao lưu; bấm giờ. Chạy bộ quét bảo mật ba phép kiểm. Phục hồi dữ liệu và đối soát. Nộp sơ đồ năm thứ và bảng chi phí hằng tháng kèm ba yếu tố nhạy cảm.

**Pitfalls.** Tạo tài nguyên bằng tay rồi ghi lại vào mã sau · mở công khai một kho đối tượng cho tiện · bỏ bước dựng lại từ đầu vì tốn thời gian · nộp sơ đồ hộp không có miền hỏng và ranh giới chi phí.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Môi trường dựng lại được từ mã trong môi trường sạch, phục hồi có đối soát khớp, không khoá tĩnh và không tài nguyên mở ngoài ý muốn, và bảng chi phí có ba yếu tố nhạy cảm.

### Lesson 372 · Failure drill - remove a zone, a service and a credential `TH`
**Prerequisites.** Lesson 371

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài diễn tập khép module, chạy trên chính lát cắt nền tảng vừa dựng, với hành vi kỳ vọng viết trước. Sáu tình huống bắt buộc: mất một khu khả dụng; một dịch vụ được quản lý bị suy giảm trong vùng; mặt phẳng điều khiển không dùng được nên không tạo được tài nguyên mới; thông tin xác thực hết hạn giữa lúc chạy; chạm hạn mức của một dịch vụ; và một cú sốc chi phí do lượng quét hoặc lưu lượng ra tăng gấp mười. Với mỗi tình huống ghi ba số: thời gian phát hiện, mức suy giảm dịch vụ, và thời gian phục hồi. **Tình huống cú sốc chi phí phải trả lời bằng thiết kế lại có số đo trên mỗi đơn vị, chứ bằng việc tắt bớt tính năng**. Kết quả diễn tập là đầu vào sửa sổ tay vận hành và sửa kiến trúc, theo đúng kỷ luật ở lesson 246.

**Outcome.** Chạy sáu tình huống với hành vi kỳ vọng viết trước và đề xuất thiết kế lại cho cú sốc chi phí.

**Đánh giá.** Tầng *đánh giá*. Objective đo năng lực vận hành dưới sự cố cùng dưới ràng buộc chi phí. Kiểm bằng sáu tình huống; đạt khi ít nhất năm phục hồi trong mục tiêu thời gian đã đặt và cú sốc chi phí có phương án thiết kế lại kèm số đo trên mỗi đơn vị.

**Lab.** Viết hành vi kỳ vọng cho sáu tình huống trước khi chạy. Chạy từng cái trên lát cắt nền tảng. Ghi ba số cho mỗi tình huống. Với tình huống hạn mức, chứng minh cảnh báo nổ trước khi chạm trần. Với cú sốc chi phí, tính lại chi phí trên mỗi đơn vị và đề xuất thiết kế lại. Sửa sổ tay vận hành theo chênh lệch quan sát được.

**Pitfalls.** Viết hành vi kỳ vọng sau khi thấy kết quả · xử lý cú sốc chi phí bằng cách tắt tính năng · bỏ tình huống mặt phẳng điều khiển vì khó dựng · không đo mức suy giảm mà chỉ đo phục hồi.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** ≥ 5/6 tình huống phục hồi trong mục tiêu thời gian, cú sốc chi phí có phương án thiết kế lại kèm số đo trên mỗi đơn vị, và sổ tay được sửa.

# MODULE M20 · CONTAINERS, INFRASTRUCTURE AS CODE AND KUBERNETES

**Phase 9 · Lessons 373–388 · 32 giờ**

| | |
|---|---|
| **Objective cấp module** | Giải thích được mọi trường trong bản khai báo mình dùng thông qua hành vi của bộ điều khiển và của môi trường chạy; dựng lại được cụm cùng dịch vụ từ mã, kho ảnh và bản sao lưu |
| **Tiền đề** | M5 · M6 · M7 · M19 |
| **Exit criterion** | Ảnh bất biến và kế hoạch hạ tầng tái tạo được; quay lui đã thử; không rò rỉ bí mật; chẩn đoán được vòng lặp khởi động lại, trạng thái chờ, bị kết thúc vì hết bộ nhớ, thăm dò hỏng và sự cố triển khai |
| **Kỹ năng SFIA** | `SYSP` mức 4 · `ITOP` mức 4 · `PROG` mức 4 |
| **Chế độ hỏng** | Sửa trực tiếp trên cụm rồi coi là xong, chạy không đặt giới hạn tài nguyên và không có thăm dò, và dùng điều phối vùng chứa ở nơi một máy ảo hoặc một dịch vụ được quản lý an toàn hơn |

Module có một câu hỏi lọc đặt ngay ở bài về điều phối: **khi nào một cách triển khai đơn giản hơn lại thắng**. Điều phối vùng chứa là một khoản thuế vận hành, và trả khoản thuế đó chỉ hợp lý khi có đủ dịch vụ và đủ nhu cầu tự phục hồi.

Kỷ luật xuyên module: **mọi thay đổi đi qua mã, không đi qua thao tác tay trên cụm**. Sửa tay là cách chắc chắn làm môi trường trôi khỏi mã và làm mất khả năng dựng lại.

Ba tầng được học theo thứ tự cơ chế: tiến trình bị cô lập, trạng thái mong muốn, rồi vòng lặp hoà giải.

### Lesson 373 · A container is an isolated process `LT`
**Prerequisites.** Module 20: M19

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài mở module bằng việc bác bỏ một hình dung sai phổ biến: vùng chứa không phải máy ảo nhỏ. Nó là một tiến trình thường của hệ điều hành máy chủ, chỉ khác ở chỗ nó nhìn thấy một thế giới bị giới hạn. Ba cơ chế tạo ra giới hạn đó: không gian tên làm tiến trình chỉ thấy một tập tiến trình, một cây thư mục, một giao diện mạng và một tập người dùng riêng; nhóm điều khiển giới hạn lượng bộ xử lý và bộ nhớ nó dùng được; khả năng cùng bộ lọc lời gọi hệ thống giới hạn nó làm được gì với nhân. **Vì dùng chung nhân với máy chủ, mức cô lập yếu hơn máy ảo**, và đó là lý do khối lượng công việc không tin cậy cần thêm lớp cách ly. Hệ quả thực hành quan trọng: tiến trình trong vùng chứa vẫn chịu lịch biểu của nhân máy chủ, nên bị điều tiết vì vượt hạn mức bộ xử lý trông giống như chậm không rõ nguyên nhân.

**Outcome.** Quan sát ba cơ chế cô lập bằng công cụ và giải thích một lần bị điều tiết bằng nhóm điều khiển.

**Đánh giá.** Tầng *hiểu*. Bài mở module, kiểm bằng quan sát hệ thật chứ bằng lập luận. Kiểm bằng bài quan sát cộng thí nghiệm hạn mức; đạt khi ba không gian tên được chỉ ra bằng công cụ và hiện tượng điều tiết được tái hiện kèm số đo.

**Lab.** Chạy một vùng chứa và từ máy chủ tìm tiến trình tương ứng. Kiểm tra bốn không gian tên của nó và so với của máy chủ. Đặt hạn mức bộ xử lý thấp và chạy một tải tính toán; đo mức điều tiết. Đặt hạn mức bộ nhớ thấp và quan sát tiến trình bị kết thúc vì hết bộ nhớ. Ghi lại khác biệt so với chạy trên máy ảo.

**Pitfalls.** Coi vùng chứa là máy ảo nhỏ · chạy khối lượng công việc không tin cậy mà không thêm lớp cách ly · không đặt hạn mức nên một vùng chứa ăn hết máy · kết luận chậm mà không kiểm mức điều tiết.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn không gian tên được chỉ ra bằng công cụ, và hiện tượng điều tiết cùng bị kết thúc vì hết bộ nhớ được tái hiện kèm số đo.

### Lesson 374 · Images, layers, digests and the multi-stage build `TH`
**Prerequisites.** Lesson 373

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ảnh là một chồng lớp chỉ đọc cộng siêu dữ liệu, và hiểu cấu trúc đó giải thích cả tốc độ dựng lẫn kích thước. Mỗi chỉ thị dựng tạo một lớp; lớp được chia sẻ giữa các ảnh nhờ nội dung giống nhau, nên thứ tự chỉ thị quyết định bộ đệm dựng có dùng lại được không: **đặt bước cài phụ thuộc trước bước sao chép mã nguồn là mẹo quan trọng nhất**, vì mã đổi thường xuyên còn phụ thuộc thì không. Thẻ có thể bị đẩy lại trỏ sang ảnh khác, còn mã băm nội dung thì không; nên ghim theo mã băm là điều kiện để triển khai tái tạo được. Dựng nhiều giai đoạn tách môi trường biên dịch khỏi ảnh chạy, giảm kích thước và giảm bề mặt tấn công. Một điểm bắt buộc: **bí mật đưa vào trong một lớp thì vẫn nằm đó dù lớp sau có xoá**, vì lớp trước vẫn tồn tại trong ảnh.

**Outcome.** Dựng ảnh nhiều giai đoạn nhỏ hơn đáng kể, ghim theo mã băm, và chứng minh không bí mật nào nằm trong lớp.

**Đánh giá.** Tầng *áp dụng*. Objective có ba tiêu chí nghiệm thu đo được. Kiểm bằng cặp số đo cộng bộ quét; đạt khi kích thước giảm có số đo, thời gian dựng lại giảm nhờ bộ đệm, và bộ quét lớp không tìm thấy bí mật.

**Lab.** Dựng một ảnh theo cách thông thường rồi dựng lại theo nhiều giai đoạn; so kích thước và số lớp. Đảo thứ tự bước cài phụ thuộc và bước sao chép mã, đo thời gian dựng lại sau khi sửa một dòng mã ở cả hai cách. Ghim ảnh nền theo mã băm. Cố ý đưa một bí mật vào một lớp rồi xoá ở lớp sau; dùng công cụ tìm lại nó trong lịch sử lớp.

**Pitfalls.** Sao chép mã nguồn trước khi cài phụ thuộc · ghim ảnh nền theo thẻ · đưa bí mật vào thời điểm dựng · chạy bằng người dùng cao nhất trong vùng chứa.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Kích thước ảnh giảm có số đo, thời gian dựng lại giảm nhờ thứ tự lớp, và bí mật đã xoá vẫn tìm lại được ở bản sai rồi được loại bỏ hẳn ở bản đúng.

### Lesson 375 · PID 1, signals and graceful shutdown in a container `TH`
**Prerequisites.** Lesson 374

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Tiến trình đầu tiên trong vùng chứa mang số một, và nó có hành vi đặc biệt của nhân: nó không nhận tín hiệu mặc định như tiến trình thường. Hệ quả cụ thể và phải tái hiện: **nếu tiến trình chính không xử lý tín hiệu kết thúc thì nó bị buộc dừng sau thời gian chờ, nên công việc đang dở bị cắt ngang**; với một tiến trình ghi dữ liệu thì đó là mất dữ liệu hoặc ghi dở. Chạy tiến trình qua một lớp vỏ làm tín hiệu không tới được tiến trình thật, là lỗi hay gặp nhất. Tiến trình con mồ côi tích tụ khi tiến trình số một không thu hồi chúng. Tắt có kiểm soát trong vùng chứa gồm ba bước theo lesson 67: nhận tín hiệu, ngừng nhận việc mới, hoàn tất việc đang dở rồi thoát, tất cả trong khoảng thời gian chờ đã cấu hình. Chạy bằng người dùng không đặc quyền và hệ tệp chỉ đọc là hai biện pháp giảm rủi ro.

**Outcome.** Chứng minh tiến trình trong vùng chứa tắt có kiểm soát trong thời gian chờ và không mất công việc đang dở.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là không mất việc khi dừng. Kiểm bằng phép thử dừng; đạt khi 100 lần dừng đều hoàn tất việc đang dở, và bản chạy qua lớp vỏ được chứng minh là bị cắt ngang.

**Lab.** Viết một tiến trình xử lý có việc kéo dài vài giây. Đóng gói theo hai cách: chạy trực tiếp và chạy qua một lớp vỏ. Dừng vùng chứa 100 lần ở cả hai cách và đếm số việc bị cắt ngang. Thêm xử lý tín hiệu và tắt có kiểm soát. Kiểm tiến trình con mồ côi. Chuyển sang chạy bằng người dùng không đặc quyền với hệ tệp chỉ đọc.

**Pitfalls.** Chạy tiến trình qua một lớp vỏ nên tín hiệu không tới · không xử lý tín hiệu kết thúc · đặt thời gian chờ ngắn hơn việc dài nhất · chạy bằng người dùng cao nhất.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** 100 lần dừng đều hoàn tất việc đang dở ở bản đúng, và bản chạy qua lớp vỏ được chứng minh bị cắt ngang kèm số việc mất.

### Lesson 376 · Container networking, volumes and the UID mismatch `TH`
**Prerequisites.** Lesson 375

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hai phần hạ tầng của vùng chứa và ba lỗi đặc trưng của chúng. Mạng: vùng chứa có không gian tên mạng riêng, nối với máy chủ qua một cặp giao diện ảo và một cầu nối; ánh xạ cổng dịch địa chỉ từ máy chủ vào; phân giải tên giữa các vùng chứa dùng một máy chủ tên nội bộ. Truy vết đường đi của một gói từ ngoài vào ứng dụng là bài tập bắt buộc. Ổ đĩa: dữ liệu trong lớp ghi của vùng chứa biến mất khi vùng chứa bị xoá, nên **mọi dữ liệu cần giữ phải nằm trên ổ đĩa gắn ngoài**. Lỗi đặc trưng thứ ba và tốn thời gian nhất: định danh người dùng bên trong vùng chứa khác định danh sở hữu tệp trên máy chủ, nên tiến trình không ghi được vào thư mục gắn vào dù quyền trông có vẻ đúng; cách chẩn đoán là so định danh số chứ so tên người dùng.

**Outcome.** Truy vết đường gói tin vào ứng dụng và chẩn đoán đúng lỗi lệch định danh người dùng.

**Đánh giá.** Tầng *áp dụng*. Objective gồm một lỗi có triệu chứng gây hiểu nhầm. Kiểm bằng bài truy vết cộng ba lỗi tiêm; đạt khi sơ đồ đường gói khớp truy vết thật và ba lỗi được chẩn đoán đúng nguyên nhân.

**Lab.** Chạy nhiều dịch vụ nối nhau. Truy vết đường đi của một yêu cầu từ máy chủ vào ứng dụng qua ánh xạ cổng và cầu nối; vẽ sơ đồ. Tiêm ba lỗi: sai tên dịch vụ khi phân giải, dữ liệu mất vì không gắn ổ đĩa, và tiến trình không ghi được vì lệch định danh người dùng. Chẩn đoán từng cái bằng số đo chứ đoán.

**Pitfalls.** Ghi dữ liệu vào lớp ghi của vùng chứa · chẩn đoán quyền bằng tên người dùng thay vì định danh số · mở cổng ra máy chủ khi chỉ cần gọi nội bộ · giả định phân giải tên giữa vùng chứa giống trên máy chủ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Sơ đồ đường gói khớp truy vết thật, và ba lỗi tiêm được chẩn đoán đúng nguyên nhân kèm bằng chứng.

### Lesson 377 · Supply chain - minimal base, pinned digest, no secret in a layer `TH`
**Prerequisites.** Lesson 376

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ảnh là một hiện vật được phân phối, nên nó có chuỗi cung ứng và chuỗi đó là một bề mặt tấn công. Năm biện pháp theo thứ tự hiệu quả: chọn ảnh nền tối thiểu để giảm số gói và giảm số lỗ hổng phải theo; ghim theo mã băm để bản dựng tái tạo được; quét lỗ hổng trong tích hợp liên tục có cửa chặn; sinh bản kê thành phần để biết mình đang chạy những gì; và ký cùng kiểm nguồn gốc ở mức nhận biết. **Quét mà không chặn thì chỉ là một báo cáo không ai đọc**, nên ngưỡng chặn phải đặt tường minh kèm quy trình miễn trừ có hạn, theo đúng kỷ luật ở lesson 276. Bí mật trong tích hợp liên tục phải lấy từ kho bí mật và không bao giờ ghi ra nhật ký. Ba rủi ro riêng của chuỗi cung ứng ảnh: ảnh nền bị đẩy lại dưới cùng một thẻ, phụ thuộc bắc cầu không ai kiểm, và kho ảnh nội bộ không có kiểm soát truy cập.

**Outcome.** Dựng quy trình có cửa chặn lỗ hổng và bản kê thành phần, chặn được ba vi phạm tiêm.

**Đánh giá.** Tầng *áp dụng*. Objective là một cửa chặn tự động có phép thử tiêm. Kiểm bằng ba vi phạm; đạt khi cả ba bị chặn ở đúng bước, bản kê thành phần sinh được, và mọi miễn trừ có hạn.

**Lab.** Dựng quy trình gồm quét lỗ hổng có ngưỡng chặn, sinh bản kê thành phần, và kiểm ghim mã băm. Tiêm ba vi phạm: ảnh nền ghim theo thẻ, một phụ thuộc có lỗ hổng nghiêm trọng, và một bí mật lọt vào lớp. Xác nhận cả ba bị chặn. So số lỗ hổng giữa ảnh nền đầy đủ và ảnh nền tối thiểu. Đặt hạn cho mọi miễn trừ.

**Pitfalls.** Quét mà không chặn · ghim ảnh nền theo thẻ · miễn trừ lỗ hổng không có hạn · để nhật ký tích hợp liên tục in ra bí mật.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba vi phạm bị chặn ở đúng bước, bản kê thành phần sinh được, số lỗ hổng giảm có số đo khi đổi ảnh nền, và mọi miễn trừ có hạn.

### Lesson 378 · Infrastructure as code - desired state and the dependency graph `LT`
**Prerequisites.** Lesson 377

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài mở phần hạ tầng khai báo bằng mô hình tư duy của nó. Ta mô tả trạng thái mong muốn; công cụ so trạng thái mong muốn với trạng thái đã ghi và với thực tế, rồi tính ra tập thay đổi tối thiểu. Đồ thị phụ thuộc giữa các tài nguyên được suy ra từ tham chiếu, nên nó quyết định thứ tự tạo và thứ tự xoá; phụ thuộc ngầm không khai báo được là nguồn của lỗi thứ tự khó tái hiện. Bốn loại hành động trong một bản kế hoạch và ý nghĩa rủi ro rất khác nhau: tạo, cập nhật tại chỗ, **thay thế tức xoá rồi tạo lại**, và xoá; loại thứ ba là loại nguy hiểm nhất vì một thay đổi trông nhỏ có thể kéo theo thay thế một cơ sở dữ liệu sản xuất. Từ đó suy ra quy tắc bắt buộc: **đọc kế hoạch trước khi áp dụng, và mọi hành động thay thế hoặc xoá ở môi trường sản xuất phải được người thứ hai duyệt**.

**Outcome.** Đọc một bản kế hoạch và nhận ra mọi hành động thay thế cùng hệ quả của chúng.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết đặt khung cho hai bài thực hành. Kiểm bằng bài đọc kế hoạch; đạt khi nhận đúng mọi hành động thay thế trong ba kế hoạch và giải thích được nguyên nhân gây thay thế.

**Lab.** Cho ba bản kế hoạch thật, mỗi cái chứa ít nhất một hành động thay thế. Với mỗi cái, liệt kê bốn loại hành động và chỉ ra tài nguyên nào bị thay thế cùng thuộc tính nào gây ra. Vẽ đồ thị phụ thuộc của một tập tài nguyên và suy ra thứ tự xoá. Tạo một ca có phụ thuộc ngầm và chỉ ra lỗi thứ tự nó gây ra.

**Pitfalls.** Áp dụng mà không đọc kế hoạch · bỏ qua hành động thay thế vì thấy thay đổi nhỏ · dựa vào thứ tự viết trong tệp thay vì đồ thị phụ thuộc · không khai báo phụ thuộc ngầm.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Nhận đúng mọi hành động thay thế trong ba kế hoạch kèm thuộc tính gây ra, và thứ tự xoá suy đúng từ đồ thị phụ thuộc.

### Lesson 379 · State, locking, drift and the recovery you must not improvise `TH`
**Prerequisites.** Lesson 378

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Tệp trạng thái là bản ghi công cụ tin về thế giới, và nó là thành phần quan trọng nhất cần bảo vệ. Ba yêu cầu bắt buộc: lưu từ xa và mã hoá vì nó chứa thông tin nhạy cảm; khoá khi đang áp dụng để hai người không cùng sửa; và có phiên bản để quay lại được. Trôi cấu hình xảy ra khi ai đó sửa tay trên đám mây: thực tế khác trạng thái ghi, và lần áp dụng tiếp theo sẽ hoàn tác thay đổi tay đó mà không báo trước; **phát hiện trôi định kỳ là biện pháp phòng ngừa chứ một việc làm khi có sự cố**. Nhập tài nguyên có sẵn và di chuyển tài nguyên trong mã là hai thao tác hay cần. Quy tắc nghiêm nhất của bài: **không sửa tay tệp trạng thái khi chưa có bản sao lưu**, vì một thao tác sai làm công cụ quên mất tài nguyên đang chạy và lần áp dụng sau sẽ tạo trùng hoặc xoá nhầm.

**Outcome.** Vận hành trạng thái từ xa có khoá, phát hiện và xử lý trôi cấu hình, và phục hồi sau một sự cố trạng thái.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là phục hồi được mà không mất tài nguyên. Kiểm bằng ba tình huống; đạt khi trôi được phát hiện tự động, khoá chặn được áp dụng song song, và phục hồi trạng thái không làm mất hay tạo trùng tài nguyên nào.

**Lab.** Dựng trạng thái từ xa có mã hoá, khoá và phiên bản. Chạy hai lần áp dụng song song và xác nhận bị chặn. Sửa tay một tài nguyên trên đám mây rồi chạy phát hiện trôi; quyết định hoàn tác hay nhập vào mã. Mô phỏng mất tệp trạng thái và phục hồi từ phiên bản trước; đối soát danh sách tài nguyên thật với trạng thái sau phục hồi.

**Pitfalls.** Để tệp trạng thái trên máy cá nhân · sửa tay tệp trạng thái mà không sao lưu · bỏ qua trôi cấu hình tới khi lần áp dụng sau hoàn tác nó · để lộ giá trị nhạy cảm trong đầu ra.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Áp dụng song song bị khoá chặn, trôi cấu hình được phát hiện tự động, và phục hồi trạng thái không làm mất hay tạo trùng tài nguyên nào.

### Lesson 380 · Modules, environments and the plan review `TH`
**Prerequisites.** Lesson 379

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Tổ chức mã hạ tầng để nhiều môi trường dùng chung mà không sao chép. Hợp đồng của một mô đun gồm đầu vào có kiểm tra giá trị, đầu ra, phiên bản nhà cung cấp và cách nâng cấp; nó chịu cùng kỷ luật hợp đồng như một thư viện phần mềm ở M7. Chiến lược môi trường: tách tài khoản hoặc dự án theo môi trường là ranh giới mạnh nhất, tách bằng không gian tên trong cùng tài khoản là ranh giới yếu và dễ nhầm. Danh tính cho quy trình tự động phải riêng và có quyền tối thiểu, không dùng lại thông tin xác thực của người. Rà soát kế hoạch trong tích hợp liên tục: hiển thị kế hoạch trong yêu cầu hợp nhất, chạy kiểm chính sách để chặn cấu hình cấm, và ước tính chi phí của thay đổi. **Áp dụng ở môi trường sản xuất phải có phê duyệt của người thứ hai**, và hiện vật của lần áp dụng được giữ lại để truy vết.

**Outcome.** Dựng quy trình rà soát kế hoạch có kiểm chính sách và phê duyệt, chặn được ba cấu hình cấm.

**Đánh giá.** Tầng *áp dụng*. Objective là một cửa chặn tự động cộng một cửa chặn người. Kiểm bằng ba vi phạm tiêm; đạt khi cả ba bị kiểm chính sách chặn và mọi lần áp dụng ở môi trường sản xuất đều có dấu phê duyệt cùng hiện vật lưu lại.

**Lab.** Tách mã thành mô đun có kiểm tra đầu vào và ghim phiên bản nhà cung cấp. Dựng quy trình hiển thị kế hoạch trong yêu cầu hợp nhất, chạy kiểm chính sách và ước tính chi phí. Tiêm ba cấu hình cấm gồm mở công khai, chính sách dùng ký tự đại diện, và một hành động thay thế cơ sở dữ liệu. Xác nhận bị chặn. Áp dụng ở môi trường sản xuất có phê duyệt và lưu hiện vật.

**Pitfalls.** Sao chép mã giữa các môi trường thay vì dùng mô đun · dùng thông tin xác thực cá nhân cho quy trình tự động · áp dụng ở sản xuất không cần phê duyệt · không ghim phiên bản nhà cung cấp.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba cấu hình cấm bị chặn bởi kiểm chính sách, và mọi lần áp dụng ở sản xuất có dấu phê duyệt cùng hiện vật lưu lại.

### Lesson 381 · Why orchestration, and when a simpler deployment wins `LT`
**Prerequisites.** Lesson 380

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài đặt câu hỏi lọc trước khi học công cụ điều phối, vì đây là chỗ nhiều đội trả thuế vận hành mà không cần. Bốn thứ điều phối cho: hoà giải về trạng thái mong muốn, lập lịch lên các nút, khám phá dịch vụ, và triển khai dần cùng tự khởi động lại. Khoản thuế phải trả: một mặt phẳng điều khiển phải vận hành và nâng cấp, một mô hình mạng và bảo mật mới phải học, và một lớp chẩn đoán mới nằm giữa mã và máy. Ba tình huống mà cách đơn giản hơn thắng: ít dịch vụ và tải ổn định thì máy ảo cùng trình quản lý dịch vụ ở lesson 69 là đủ; công việc theo lô chạy định kỳ thì một dịch vụ chạy vùng chứa được quản lý đủ và rẻ hơn; và đội chưa có năng lực vận hành nền tảng thì **khoản thuế vận hành lớn hơn lợi ích và rủi ro cao hơn**. Ba dấu hiệu một đội đang dùng điều phối vì nó phổ biến chứ vì ràng buộc thật.

**Outcome.** So ba cách triển khai cho một dự án theo bốn tiêu chí và chọn một kèm điều kiện đảo ngược.

**Đánh giá.** Tầng *đánh giá*. Objective chống lại việc mặc định chọn phương án phức tạp nhất. Kiểm bằng bảng ba cách nhân bốn tiêu chí; đạt khi hai tiêu chí đầu có số đo và lựa chọn kèm hai điều kiện đảo ngược cụ thể.

**Lab.** Triển khai cùng một dịch vụ theo ba cách: máy ảo cùng trình quản lý dịch vụ, dịch vụ vùng chứa được quản lý, và cụm điều phối. Đo thời gian triển khai đầu, thời gian một lần cập nhật, thời gian phục hồi khi mất một máy, và ước lượng giờ công vận hành mỗi tháng. Chọn một cho dự án và nêu hai điều kiện làm lựa chọn đó sai.

**Pitfalls.** Chọn điều phối vì nó phổ biến · so ba cách mà không tính giờ công vận hành · bỏ qua yêu cầu nâng cấp mặt phẳng điều khiển · khuyến nghị không có điều kiện đảo ngược.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba cách có số đo ở hai tiêu chí đầu cùng ước lượng giờ công vận hành, và lựa chọn kèm hai điều kiện đảo ngược cụ thể.

### Lesson 382 · From object to controller - the five-step trace `TH`
**Prerequisites.** Lesson 381

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài dạy cơ chế trung tâm của điều phối: vòng lặp hoà giải. Năm bước khi ta gửi một đối tượng: máy chủ giao diện xác thực, phân quyền, chạy các bộ kiểm nạp rồi lưu vào kho khoá giá trị; bộ điều khiển thấy đối tượng mới và tạo các đối tượng phụ thuộc; bộ lập lịch gán một đơn vị chạy vào một nút; tiến trình trên nút tạo môi trường chạy, gắn ổ đĩa, nối mạng rồi chạy vùng chứa, và các phép thăm dò cập nhật trạng thái sẵn sàng; bộ điều khiển quan sát trạng thái và tiếp tục hoà giải cho tới khi khớp trạng thái mong muốn. Hai ý phải rút ra: **đặc tả là mong muốn còn trạng thái là thực tế, và khoảng cách giữa chúng là nơi mọi sự cố nằm**; và **hệ khởi động lại hoặc lập lịch lại chứ không tự khôi phục trạng thái ứng dụng**. Sự kiện của đối tượng là nguồn chẩn đoán đầu tiên, trước nhật ký.

**Outcome.** Truy đủ năm bước cho một lần triển khai thật và đọc được khoảng cách giữa đặc tả với trạng thái.

**Đánh giá.** Tầng *phân tích*. Objective đòi quan sát cơ chế thật thay vì mô tả nó. Kiểm bằng bài truy vết; đạt khi năm bước có bằng chứng quan sát được và ba lần triển khai hỏng được quy đúng bước.

**Lab.** Gửi một đối tượng triển khai và theo dõi từng bước bằng sự kiện cùng trạng thái của các đối tượng liên quan. Ghi lại thời gian ở mỗi bước. Tạo ba lần triển khai hỏng ở ba bước khác nhau: bị bộ kiểm nạp từ chối, không lập lịch được, và không kéo được ảnh; với mỗi cái, quy về đúng bước chỉ bằng sự kiện và trạng thái.

**Pitfalls.** Xem nhật ký ứng dụng trước khi xem sự kiện của đối tượng · giả định hệ khôi phục được trạng thái ứng dụng · sửa bằng cách xoá rồi tạo lại mà không tìm nguyên nhân · bỏ qua bước kiểm nạp khi chẩn đoán.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Năm bước có bằng chứng quan sát được kèm thời gian, và ba lần triển khai hỏng được quy đúng bước chỉ bằng sự kiện và trạng thái.

### Lesson 383 · Pods, probes, requests and limits `TH`
**Prerequisites.** Lesson 382

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bốn trường có ảnh hưởng lớn nhất tới hành vi thật, nên chúng có một bài riêng. Yêu cầu tài nguyên là thứ bộ lập lịch dùng để chọn nút; giới hạn tài nguyên là trần mà môi trường chạy cưỡng chế. **Đặt yêu cầu quá cao lãng phí năng lực, đặt quá thấp làm nút quá tải; đặt giới hạn bộ nhớ quá thấp làm tiến trình bị kết thúc vì hết bộ nhớ, còn giới hạn bộ xử lý gây điều tiết chứ kết thúc**, và phân biệt hai hiện tượng này là kỹ năng chẩn đoán chính. Ba loại thăm dò cho ba mục đích: thăm dò khởi động cho ứng dụng khởi động chậm, thăm dò sẵn sàng quyết định có nhận lưu lượng không, thăm dò sống quyết định có khởi động lại không. Chế độ hỏng đặc trưng: **thăm dò nông chỉ kiểm tiến trình còn sống làm một dịch vụ hỏng vẫn được đánh dấu sẵn sàng và vẫn nhận lưu lượng**; thăm dò sống quá nhạy gây vòng lặp khởi động lại dưới tải.

**Outcome.** Đặt bốn trường từ số đo thật và phân biệt được bị kết thúc vì hết bộ nhớ với bị điều tiết bộ xử lý.

**Đánh giá.** Tầng *áp dụng*. Objective đòi rút tham số từ đo lường và phân biệt hai triệu chứng gần giống. Kiểm bằng bốn tình huống tiêm; đạt khi bốn tình huống được chẩn đoán đúng và giá trị cuối dẫn được từ số đo chứ từ phỏng đoán.

**Lab.** Đo lượng bộ nhớ và bộ xử lý thật của một dịch vụ dưới tải; đặt yêu cầu và giới hạn từ số đo đó. Tiêm bốn tình huống: giới hạn bộ nhớ quá thấp, giới hạn bộ xử lý quá thấp, thăm dò sẵn sàng nông trên một dịch vụ hỏng, và thăm dò sống quá nhạy dưới tải. Chẩn đoán từng cái bằng sự kiện và số đo. Sửa và đo lại.

**Pitfalls.** Đặt yêu cầu và giới hạn bằng con số tròn · bỏ giới hạn cho khỏi bị kết thúc · viết thăm dò sẵn sàng chỉ kiểm tiến trình còn sống · đặt thăm dò sống nhạy hơn thăm dò sẵn sàng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn tình huống được chẩn đoán đúng, và giá trị bốn trường dẫn được từ số đo tải thật.

### Lesson 384 · Service, endpoint, DNS and network policy `TH`
**Prerequisites.** Lesson 383

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Cách lưu lượng tìm tới một đơn vị chạy, và bốn lỗi đặc trưng. Dịch vụ chọn các đơn vị chạy theo nhãn; danh sách điểm cuối được cập nhật khi trạng thái sẵn sàng đổi; tên dịch vụ phân giải qua máy chủ tên trong cụm. Từ đó suy ra chuỗi chẩn đoán có thứ tự: kiểm nhãn có khớp bộ chọn không, kiểm danh sách điểm cuối có rỗng không, kiểm phân giải tên, rồi mới kiểm ứng dụng. **Danh sách điểm cuối rỗng gần như luôn có nghĩa là nhãn sai hoặc không đơn vị nào sẵn sàng**, và đó là hai nguyên nhân chiếm phần lớn sự cố loại này. Cổng của dịch vụ khác cổng của vùng chứa và nhầm hai cái là lỗi phổ biến. Chính sách mạng mặc định cho phép mọi thứ nói chuyện với nhau; đặt chính sách từ chối mặc định rồi mở theo nhu cầu là thực hành đúng, theo nguyên tắc ở lesson 73.

**Outcome.** Chẩn đoán bốn sự cố kết nối theo đúng thứ tự chuỗi và dựng chính sách mạng từ chối mặc định.

**Đánh giá.** Tầng *áp dụng*. Objective có một chuỗi chẩn đoán có thứ tự và một cấu hình bảo mật kiểm được. Kiểm bằng bốn sự cố tiêm cộng phép thử phủ định; đạt khi cả bốn được chẩn đoán đúng nguyên nhân và chính sách từ chối mặc định chặn đúng mọi kết nối không được phép.

**Lab.** Tiêm bốn sự cố: nhãn không khớp bộ chọn, sai cổng, tên dịch vụ sai, và một đơn vị chạy chưa sẵn sàng. Với mỗi cái, chạy chuỗi chẩn đoán theo thứ tự và ghi bằng chứng ở mỗi bước. Đặt chính sách mạng từ chối mặc định rồi mở đúng các đường cần thiết; chạy phép thử phủ định cho mọi cặp dịch vụ.

**Pitfalls.** Xem nhật ký ứng dụng trước khi kiểm danh sách điểm cuối · nhầm cổng dịch vụ với cổng vùng chứa · để chính sách mạng mặc định cho phép mọi thứ · sửa bằng cách khởi động lại.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn sự cố được chẩn đoán đúng theo thứ tự chuỗi, và chính sách từ chối mặc định chặn đúng mọi kết nối không được phép trong phép thử phủ định.

### Lesson 385 · Config, secrets, volumes and stateful workloads `TH`
**Prerequisites.** Lesson 384

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Tách cấu hình khỏi ảnh và xử lý trạng thái. Cấu hình và bí mật được gắn vào dưới dạng biến môi trường hoặc tệp; gắn dưới dạng tệp có lợi hơn vì cập nhật được mà không dựng lại đơn vị chạy và không lộ trong danh sách tiến trình. **Bí mật ở dạng mặc định chỉ được mã hoá cơ bản chứ mã hoá thật, nên nó cần lớp bảo vệ bổ sung**, chẳng hạn mã hoá khi lưu ở kho khoá giá trị hoặc lấy từ kho bí mật bên ngoài theo lesson 369. Ổ đĩa bền vững gắn vào đơn vị chạy và tồn tại độc lập với nó. Khối lượng công việc có trạng thái cần danh tính ổn định và ổ đĩa riêng cho từng bản sao; nhưng phải nói rõ giới hạn: **hệ điều phối cấp danh tính và ổ đĩa, còn việc sao chép dữ liệu giữa các bản sao vẫn là việc của ứng dụng**, nên chạy một cơ sở dữ liệu ở đây không tự có tính sẵn sàng cao.

**Outcome.** Gắn cấu hình và bí mật an toàn, và chỉ ra chính xác điều mà khối lượng công việc có trạng thái không tự cho.

**Đánh giá.** Tầng *áp dụng*. Objective gồm một giới hạn phải phát biểu đúng. Kiểm bằng phép thử cập nhật cộng bài lập luận; đạt khi cấu hình cập nhật được không dựng lại đơn vị chạy, bí mật không lộ trong nhật ký hay danh sách tiến trình, và giới hạn về sao chép dữ liệu được nêu đúng.

**Lab.** Gắn cấu hình theo cả hai cách và so: cập nhật giá trị rồi xem cách nào cần dựng lại đơn vị chạy. Lấy bí mật từ kho bên ngoài. Kiểm bí mật không xuất hiện trong nhật ký, trong biến môi trường in ra, hay trong đặc tả đối tượng. Chạy một khối lượng công việc có trạng thái ba bản sao; giết một bản và quan sát danh tính cùng ổ đĩa được giữ. Viết một đoạn nêu rõ phần sao chép dữ liệu ai lo.

**Pitfalls.** Đưa bí mật vào biến môi trường rồi in ra nhật ký · tin bí mật ở dạng mặc định đã được mã hoá thật · nghĩ chạy cơ sở dữ liệu theo dạng có trạng thái là đã có sẵn sàng cao · gắn ổ đĩa chung cho nhiều bản sao cần ghi.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Cấu hình cập nhật được không dựng lại đơn vị chạy, bí mật không lộ ở cả ba nơi kiểm, và giới hạn về sao chép dữ liệu được nêu đúng.

### Lesson 386 · Rollout, rollback, drain and the disruption budget `TH`
**Prerequisites.** Lesson 385

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Triển khai phiên bản mới mà không gián đoạn, và bốn cơ chế kiểm soát. Triển khai dần thay thế từng phần với hai tham số là số đơn vị thừa được tạo thêm và số đơn vị được phép không sẵn sàng; hai con số này quyết định tốc độ và mức rủi ro. Quay lui là thao tác phải thử trước khi cần, theo lesson 97. Rút nút ra khỏi phục vụ khi bảo trì phải phối hợp với tắt có kiểm soát ở lesson 375, nếu không thì yêu cầu đang xử lý bị cắt. Ngân sách gián đoạn giới hạn số đơn vị được phép mất cùng lúc do thao tác chủ động; **đặt ngân sách quá chặt làm việc rút nút bị kẹt vô hạn**, một bế tắc hay gặp khi cụm không còn đủ năng lực để tạo đơn vị thay thế. Triển khai song song hai phiên bản và triển khai thử với một phần lưu lượng là hai chiến lược an toàn hơn, đổi lại tốn năng lực gấp đôi hoặc cần định tuyến theo tỉ lệ.

**Outcome.** Triển khai và quay lui không gián đoạn, và tái hiện được bế tắc do ngân sách gián đoạn quá chặt.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là không yêu cầu nào lỗi trong suốt quá trình. Kiểm bằng phép thử tải liên tục; đạt khi tỉ lệ lỗi bằng không suốt triển khai và quay lui, và bế tắc do ngân sách được tái hiện rồi gỡ.

**Lab.** Chạy tải liên tục trong lúc triển khai phiên bản mới; đo tỉ lệ lỗi và độ trễ. Thực hiện quay lui và đo lại. Rút một nút khi có tải và kiểm không yêu cầu nào bị cắt giữa chừng. Đặt ngân sách gián đoạn quá chặt rồi rút nút; quan sát bế tắc và gỡ bằng cách thêm năng lực hoặc nới ngân sách.

**Pitfalls.** Triển khai mà không chạy tải nên không thấy lỗi · chưa từng thử quay lui · rút nút mà không có tắt có kiểm soát · đặt ngân sách gián đoạn mà không xét năng lực dự phòng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tỉ lệ lỗi bằng không suốt triển khai và quay lui, không yêu cầu nào bị cắt khi rút nút, và bế tắc do ngân sách được tái hiện rồi gỡ.

### Lesson 387 · Diagnosing ten broken workloads `TH`
**Prerequisites.** Lesson 386

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài rèn chẩn đoán, dùng lại quy trình ở lesson 75 nhưng cho môi trường điều phối. Thứ tự cố định: đọc trạng thái của đối tượng, đọc sự kiện, đọc đặc tả, rồi mới đọc nhật ký ứng dụng và số đo của nút. Mười lỗi thuộc năm nhóm và mỗi nhóm có một dấu hiệu phân biệt: không kéo được ảnh do tên, thẻ hoặc quyền kho ảnh; vòng lặp khởi động lại do lỗi khi khởi động hoặc do thăm dò sống; trạng thái chờ do không đủ tài nguyên, do quy tắc chặn nút, hoặc do ổ đĩa chưa sẵn sàng; bị kết thúc vì hết bộ nhớ do giới hạn thấp hơn nhu cầu thật; và sẵn sàng nhưng hỏng do thăm dò nông. **Mỗi chẩn đoán phải dẫn ra bằng chứng cụ thể đã đọc ở bước nào**, và sửa bằng mã chứ bằng thao tác tay trên cụm. Ba lỗi trông giống nhau nhưng khác nguyên nhân được đặt cạnh nhau để rèn phân biệt.

**Outcome.** Chẩn đoán mười khối lượng công việc hỏng theo đúng thứ tự và sửa bằng mã.

**Đánh giá.** Tầng *phân tích*. Objective đo năng lực chẩn đoán có phương pháp. Kiểm bằng mười ca; đạt khi chẩn đoán đúng ít nhất tám kèm bằng chứng dẫn ra, và mọi bản sửa đi qua mã chứ thao tác tay.

**Lab.** Nhận mười khối lượng công việc hỏng thuộc năm nhóm. Với mỗi cái, chạy đúng thứ tự bốn bước và ghi bằng chứng ở bước phát hiện ra nguyên nhân. Sửa bằng cách đổi mã rồi triển khai lại. Bấm giờ từng ca. Lập bảng năm nhóm với dấu hiệu phân biệt để dùng khi trực.

**Pitfalls.** Sửa trực tiếp trên cụm · đọc nhật ký ứng dụng trước khi đọc sự kiện · khởi động lại để xem có hết không · chẩn đoán mà không dẫn bằng chứng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chẩn đoán đúng ≥ 8/10 ca kèm bằng chứng dẫn ra, mọi bản sửa đi qua mã, và bảng năm nhóm dấu hiệu phân biệt hoàn chỉnh.

### Lesson 388 · Rebuild project - cluster and service from code and backup `DA`
**Prerequisites.** Lesson 387

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Bài dự án khép module, và tiêu chí nghiệm thu của nó là một phép thử duy nhất: dựng lại được từ con số không. Trong một môi trường sạch, dựng lại toàn bộ chỉ từ ba thứ: mã hạ tầng, kho ảnh, và bản sao lưu dữ liệu. Không được dùng bất kỳ thao tác tay nào và không được chép cấu hình từ môi trường cũ. Nộp gồm: mã hạ tầng có mô đun, trạng thái từ xa và kiểm chính sách; ảnh nhiều giai đoạn ghim theo mã băm, chạy bằng người dùng không đặc quyền; bản khai báo đầy đủ có thăm dò, yêu cầu và giới hạn tài nguyên, phân quyền theo vai và chính sách mạng từ chối mặc định; quy trình triển khai có quay lui đã thử; và sổ tay chẩn đoán năm nhóm ở lesson 387. **Mọi trường trong bản khai báo phải giải thích được bằng hành vi của bộ điều khiển hoặc của môi trường chạy**; trường nào không giải thích được thì gỡ bỏ.

**Outcome.** Dựng lại toàn bộ trong môi trường sạch chỉ từ mã, kho ảnh và bản sao lưu, và giải thích được mọi trường đã dùng.

**Đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module thành một phép thử tái tạo. Kiểm bằng dựng lại từ đầu cộng bảo vệ bản khai báo; đạt khi môi trường sạch dựng lại thành công với dữ liệu đối soát khớp, và mọi trường được giải thích bằng cơ chế.

**Lab.** Dựng lại toàn bộ trong môi trường sạch, bấm giờ và ghi lại mọi chỗ phải can thiệp tay; mỗi lần can thiệp tay là một thiếu sót phải đưa vào mã rồi làm lại. Phục hồi dữ liệu và đối soát. Thực hiện một lần triển khai và một lần quay lui dưới tải. Bảo vệ bản khai báo: người chấm chỉ vào năm trường bất kỳ và hỏi cơ chế đằng sau.

**Pitfalls.** Chép cấu hình từ môi trường cũ · giữ lại trường trong bản khai báo mà không biết nó làm gì · bỏ bước phục hồi dữ liệu · can thiệp tay rồi không đưa vào mã.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Môi trường sạch dựng lại thành công không can thiệp tay, dữ liệu đối soát khớp, quay lui thử thành công dưới tải, và năm trường bất kỳ được giải thích bằng cơ chế.

# MODULE M21 · OBSERVABILITY, RELIABILITY AND SECURITY

**Phase 9 · Lessons 389–404 · 33 giờ**

| | |
|---|---|
| **Objective cấp module** | Một bảng theo dõi trả lời được chuỗi ảnh hưởng người dùng tới dịch vụ tới phụ thuộc tới tài nguyên; cam kết dịch vụ dẫn tới một quyết định phát hành cụ thể |
| **Tiền đề** | M7 · M8 · M14 · M19 · M20 |
| **Exit criterion** | Cảnh báo hành động được và có sổ tay đi kèm, không bùng nổ số chuỗi nhãn; phục hồi và xoay thông tin xác thực đã thử; mô hình mối đe doạ ánh xạ chốt kiểm soát với rủi ro |
| **Kỹ năng SFIA** | `USUP` mức 5 · `SCTY` mức 4 · `ITOP` mức 4 |
| **Chế độ hỏng** | Gọi người trực vì một số đo không hành động được, để số chuỗi nhãn không giới hạn, phân tích sau sự cố quy về lỗi cá nhân, và để dữ liệu nhạy cảm lọt vào tín hiệu đo lường |

Module khép Phase 9 bằng cách gộp ba mặt vốn bị tách rời: quan sát được, tin cậy và bảo mật. Chúng gộp vì một sự cố thật luôn chạm cả ba, và ma trận sự cố hợp nhất ở cuối module thể hiện đúng điều đó.

Nguyên tắc thiết kế tín hiệu chạy suốt module: **bắt đầu từ câu hỏi và từ hành trình người dùng, không bắt đầu từ những số đo sẵn có**. Đo cái đo được rồi mới nghĩ dùng làm gì là cách tạo ra bảng theo dõi đầy biểu đồ mà không trả lời được câu nào.

Phần cam kết dịch vụ nối thẳng với M14C: ở đó là cam kết về dữ liệu, ở đây là cam kết về dịch vụ, và hai loại dùng chung một bộ máy.

### Lesson 389 · Observability against monitoring - instrument from the question `LT`
**Prerequisites.** Module 21: M20

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài mở module bằng một phép phân biệt có hệ quả thực hành. Theo dõi trả lời những câu hỏi đã biết trước: dịch vụ còn sống không, mức dùng bộ nhớ bao nhiêu. Quan sát được là khả năng trả lời những câu hỏi chưa nghĩ tới, và nó đòi tín hiệu mang đủ ngữ cảnh để cắt lát theo nhiều chiều sau này. Ba loại tín hiệu cho ba nhiệm vụ khác nhau và không thay nhau được: nhật ký giải thích một sự kiện rời rạc; số đo định lượng một tập hợp; vết nối các bước của một đường nhân quả. Quy trình thiết kế tín hiệu có thứ tự bắt buộc: bắt đầu từ hành trình người dùng hoặc từ một bất biến, ánh xạ dịch vụ cùng phụ thuộc cùng tài nguyên, rồi mới quyết định đo gì ở đâu. **Đo những gì có sẵn rồi mới nghĩ dùng làm gì là cách tạo ra bảng theo dõi không trả lời được câu nào**, và ba dấu hiệu của tình trạng đó.

**Outcome.** Thiết kế bộ tín hiệu bắt đầu từ ba câu hỏi vận hành và chỉ ra loại tín hiệu nào trả lời câu nào.

**Đánh giá.** Tầng *hiểu*. Bài mở module, đặt phương pháp. Kiểm bằng bài thiết kế ngược; đạt khi ba câu hỏi đều có tín hiệu tương ứng và mỗi tín hiệu được chọn đúng loại kèm lý do.

**Lab.** Chọn ba câu hỏi vận hành thật, chẳng hạn người dùng nào bị ảnh hưởng, chậm ở chặng nào, và nguyên nhân thuộc dịch vụ nào. Với mỗi câu, xác định tín hiệu cần và chọn loại. Rà bảng theo dõi hiện có và đếm bao nhiêu biểu đồ trả lời được một câu hỏi cụ thể; bỏ những biểu đồ không trả lời câu nào.

**Pitfalls.** Đo mọi thứ đo được rồi vẽ hết lên bảng · dùng nhật ký để làm việc của số đo · vẽ bảng theo dõi theo thành phần hạ tầng thay vì theo hành trình người dùng · coi theo dõi là quan sát được.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba câu hỏi đều có tín hiệu tương ứng chọn đúng loại, và bảng theo dõi hiện có được rà với số biểu đồ không trả lời câu nào được đếm.

### Lesson 390 · Logs - structure, correlation, retention and redaction `TH`
**Prerequisites.** Lesson 389

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Nhật ký có cấu trúc dùng lại nội dung ở lesson 20 và thêm bốn yêu cầu của môi trường phân tán. Lược đồ thống nhất cho mọi dịch vụ để truy vấn được xuyên hệ. Định danh tương quan truyền qua mọi chặng, gồm cả qua hàng đợi, để nối các dòng nhật ký của cùng một yêu cầu; **qua ranh giới hàng đợi là chỗ định danh hay bị rơi mất nhất**, vì bên tiêu thụ là một tiến trình khác và phải đọc định danh từ thông điệp. Mức nhật ký phải có kỷ luật, nếu không thì mức lỗi mất ý nghĩa. Lấy mẫu và thời hạn giữ vì nhật ký là tín hiệu đắt nhất trên mỗi đơn vị thông tin. Che dữ liệu nhạy cảm ngay tại nơi sinh ra chứ ở nơi lưu: **dữ liệu cá nhân lọt vào nhật ký là một sự cố bảo mật**, và nó khó dọn vì nhật ký đã nhân bản sang nhiều nơi. Ba thứ không bao giờ được ghi.

**Outcome.** Nối được toàn bộ dòng nhật ký của một yêu cầu đi qua hàng đợi và chứng minh không dữ liệu nhạy cảm nào lọt.

**Đánh giá.** Tầng *áp dụng*. Objective có hai tiêu chí nghiệm thu kiểm được bằng truy vấn. Kiểm bằng phép thử tương quan cộng bộ quét; đạt khi 100 yêu cầu qua hàng đợi đều nối đủ chặng, và bộ quét không tìm thấy dữ liệu nhạy cảm trong nhật ký.

**Lab.** Thống nhất lược đồ nhật ký cho ba dịch vụ. Truyền định danh tương quan qua cả lời gọi trực tiếp lẫn hàng đợi. Chạy 100 yêu cầu và truy vấn nhật ký theo định danh; đếm số yêu cầu nối đủ chặng. Cài che dữ liệu tại nơi sinh và chạy bộ quét tìm dữ liệu nhạy cảm. Đặt lấy mẫu cùng thời hạn giữ và tính chi phí.

**Pitfalls.** Để định danh tương quan rơi mất ở ranh giới hàng đợi · che dữ liệu ở nơi lưu thay vì nơi sinh · ghi toàn bộ thân yêu cầu vào nhật ký · giữ mọi nhật ký vô thời hạn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** 100 yêu cầu qua hàng đợi đều nối đủ chặng, bộ quét không tìm thấy dữ liệu nhạy cảm, và chi phí nhật ký được tính.

### Lesson 391 · Metrics - the three types, cardinality and the percentile trap `TH`
**Prerequisites.** Lesson 390

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba kiểu số đo và ba cái bẫy đi kèm. Bộ đếm chỉ tăng và dùng để tính tốc độ; đồng hồ đo giá trị tức thời; biểu đồ phân bố ghi phân phối và cho phép tính phân vị. Bẫy thứ nhất là số chuỗi nhãn: mỗi tổ hợp giá trị nhãn tạo một chuỗi riêng, nên **thêm một nhãn có nhiều giá trị như định danh người dùng làm số chuỗi bùng nổ và làm sập hệ thu thập**; quy tắc là nhãn chỉ dùng cho giá trị có miền hữu hạn và nhỏ. Bẫy thứ hai là gộp phân vị: **không thể lấy trung bình của các phân vị**, vì phân vị 95 của tổng thể không bằng trung bình các phân vị 95 của từng phần; muốn gộp đúng thì phải gộp từ biểu đồ phân bố. Bẫy thứ ba là giá trị trung bình che mất đuôi phân phối. Bộ chỉ số theo yêu cầu và bộ chỉ số theo tài nguyên bị ràng buộc là hai khung chọn số đo.

**Outcome.** Chứng minh bằng số hai cái bẫy về nhãn và về phân vị, rồi sửa bộ số đo cho đúng.

**Đánh giá.** Tầng *phân tích*. Objective đòi chứng minh hai lỗi thường gặp bằng dữ liệu. Kiểm bằng hai thí nghiệm; đạt khi số chuỗi nhãn được đo trước sau và chênh lệch giữa phân vị gộp đúng với phân vị lấy trung bình được định lượng.

**Lab.** Thêm một nhãn có miền giá trị lớn và đo số chuỗi cùng mức dùng bộ nhớ của hệ thu thập; gỡ nhãn và đo lại. Tính phân vị 95 của một dịch vụ theo hai cách: lấy trung bình phân vị của từng bản sao, và gộp từ biểu đồ phân bố; so hai con số với giá trị đúng tính từ dữ liệu thô. Dựng bộ chỉ số theo yêu cầu cho một dịch vụ và theo tài nguyên cho một hàng đợi.

**Pitfalls.** Đặt định danh người dùng làm nhãn · lấy trung bình của các phân vị · theo dõi bằng giá trị trung bình · dùng đồng hồ đo cho thứ cần tính tốc độ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Số chuỗi nhãn đo được trước sau, và chênh lệch giữa phân vị gộp đúng với phân vị lấy trung bình được định lượng so với giá trị đúng.

### Lesson 392 · Traces - span, context propagation and the queue boundary `TH`
**Prerequisites.** Lesson 391

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Vết trả lời câu hỏi mà nhật ký và số đo không trả lời được: thời gian của một yêu cầu tiêu ở chặng nào. Một vết gồm nhiều đoạn lồng nhau, mỗi đoạn là một đơn vị công việc có thời điểm bắt đầu và kết thúc. Ngữ cảnh truyền qua tiêu đề khi gọi trực tiếp; **qua hàng đợi thì phải nhúng vào thông điệp, và đây là chỗ vết hay bị đứt**, làm phần xử lý bất đồng bộ trở thành một vết rời không nối được với yêu cầu gốc. Lấy mẫu là bắt buộc vì lưu mọi vết quá đắt; ba chiến lược và đánh đổi, trong đó lấy mẫu theo đuôi giữ được các vết chậm hoặc lỗi nhưng cần bộ đệm. Dữ liệu đính kèm truyền theo ngữ cảnh phải hạn chế vì nó đi qua mọi chặng. Đọc một vết để tìm chặng tốn nhất là kỹ năng chính, và nó phân biệt chậm do chờ với chậm do tính.

**Outcome.** Nối được vết đi qua hàng đợi và chỉ ra chặng tốn nhất của một yêu cầu chậm.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là vết liền mạch qua ranh giới bất đồng bộ. Kiểm bằng phép thử nối vết; đạt khi vết nối đủ chặng qua hàng đợi ở ít nhất 95 phần trăm mẫu, và chặng tốn nhất của ba yêu cầu chậm được chỉ đúng.

**Lab.** Gắn đo lường cho ba dịch vụ nối nhau qua một hàng đợi. Chạy tải và kiểm tỉ lệ vết nối đủ chặng. Cố ý bỏ truyền ngữ cảnh qua hàng đợi và quan sát vết đứt. Tạo ba yêu cầu chậm vì ba nguyên nhân khác nhau; đọc vết và chỉ ra chặng tốn nhất cùng phân biệt chờ với tính. Bật lấy mẫu theo đuôi và đo chi phí.

**Pitfalls.** Không truyền ngữ cảnh qua hàng đợi · lấy mẫu đầu với tỉ lệ thấp rồi mất hết vết lỗi · nhét dữ liệu lớn vào dữ liệu đính kèm · đọc vết mà không phân biệt chờ với tính.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Vết nối đủ chặng qua hàng đợi ở ≥ 95% mẫu, và chặng tốn nhất của ba yêu cầu chậm được chỉ đúng kèm phân biệt chờ với tính.

### Lesson 393 · One telemetry pipeline - SDK, collector, exporter `TH`
**Prerequisites.** Lesson 392

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Gom ba loại tín hiệu vào một đường thống nhất để không phụ thuộc vào một nhà cung cấp và để xử lý tín hiệu ở một chỗ. Ba thành phần: thư viện đo lường trong ứng dụng, bộ thu gom chạy riêng, và bộ xuất đẩy sang hệ lưu trữ. Bộ thu gom là nơi đặt các phép xử lý dùng chung: gộp, lấy mẫu, che dữ liệu nhạy cảm, và thêm siêu dữ liệu về môi trường; đặt chúng ở đây thay vì trong từng ứng dụng làm chính sách nhất quán và đổi được mà không triển khai lại ứng dụng. **Đường tín hiệu cũng có thể hỏng, và khi nó hỏng thì ta mù mà không biết mình mù**; nên phải có nhịp tim, phải theo dõi độ sâu hàng đợi của bộ thu gom, và cảnh báo phải hành xử thận trọng khi mất tín hiệu chứ coi im lặng là bình thường. Chi phí đo lường phải tính vào ngân sách theo lesson 368.

**Outcome.** Dựng đường tín hiệu thống nhất có che dữ liệu ở bộ thu gom và phát hiện được khi chính nó hỏng.

**Đánh giá.** Tầng *áp dụng*. Objective gồm một yêu cầu về chính hệ đo lường. Kiểm bằng phép thử mất tín hiệu; đạt khi mất tín hiệu được phát hiện trong ngưỡng thoả thuận và che dữ liệu ở bộ thu gom có hiệu lực cho cả ba dịch vụ.

**Lab.** Dựng đường tín hiệu cho ba dịch vụ với một bộ thu gom chung. Đặt che dữ liệu nhạy cảm và lấy mẫu ở bộ thu gom; xác nhận có hiệu lực cho cả ba mà không sửa ứng dụng. Dựng nhịp tim và cảnh báo mất tín hiệu. Dừng bộ thu gom và đo thời gian tới khi phát hiện. Làm đầy hàng đợi của bộ thu gom và quan sát hành vi. Tính chi phí đo lường.

**Pitfalls.** Đặt logic che dữ liệu trong từng ứng dụng · coi im lặng là hệ đang khoẻ · không theo dõi hàng đợi của bộ thu gom · bỏ chi phí đo lường khỏi ngân sách.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mất tín hiệu được phát hiện trong ngưỡng thoả thuận, che dữ liệu ở bộ thu gom có hiệu lực cho cả ba dịch vụ, và chi phí đo lường được tính.

### Lesson 394 · Dashboard from the user journey `TH`
**Prerequisites.** Lesson 393

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bảng theo dõi tốt có cấu trúc theo chuỗi suy luận chứ theo danh sách thành phần. Bốn tầng theo thứ tự đọc: ảnh hưởng người dùng, rồi dịch vụ nào gây ra, rồi phụ thuộc nào của dịch vụ đó, rồi tài nguyên nào bị ràng buộc. **Người trực đọc từ trên xuống và mỗi tầng phải thu hẹp phạm vi**, nên một bảng theo dõi chỉ có biểu đồ tài nguyên không giúp trả lời câu người dùng có bị ảnh hưởng không. Ba câu hỏi một bảng theo dõi phải trả lời trong vòng một phút: có đang có sự cố không, ai bị ảnh hưởng, và nên xem tiếp ở đâu. Phép thử của một bảng tốt là phép thử người: đưa cho một người chưa biết hệ cùng một sự cố đang diễn ra và bấm giờ xem họ mất bao lâu để thu hẹp tới đúng thành phần. Số biểu đồ không phải thước đo; biểu đồ không trả lời câu nào thì gỡ đi.

**Outcome.** Dựng bảng theo dõi bốn tầng và chứng minh người chưa biết hệ thu hẹp được tới đúng thành phần trong giới hạn thời gian.

**Đánh giá.** Tầng *đánh giá*. Objective đo bằng kết quả của người dùng bảng chứ bằng độ đầy đủ. Kiểm bằng phép thử người có tính giờ; đạt khi ít nhất hai trong ba người thu hẹp đúng thành phần trong năm phút.

**Lab.** Dựng bảng theo dõi bốn tầng cho một dịch vụ. Tiêm một sự cố. Đưa cho ba người chưa biết hệ và bấm giờ tới khi họ chỉ ra đúng thành phần gây ra. Ghi lại mọi chỗ họ vấp và mọi biểu đồ họ không dùng tới. Gỡ biểu đồ không trả lời câu nào và chạy lại với một sự cố khác.

**Pitfalls.** Xếp bảng theo dõi theo thành phần hạ tầng · thêm biểu đồ vì có số đo · đánh giá bảng bằng cảm nhận của chính người dựng · giữ biểu đồ không ai dùng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** ≥ 2/3 người chưa biết hệ thu hẹp đúng thành phần trong năm phút, và biểu đồ không trả lời câu nào đã được gỡ.

### Lesson 395 · SLI and SLO from raw events `TH`
**Prerequisites.** Lesson 394

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài dùng lại bộ máy ở lesson 286 nhưng cho cam kết về dịch vụ, và nhấn vào phần định nghĩa chính xác. Chỉ số phục vụ định nghĩa bằng tỉ lệ sự kiện tốt trên tổng sự kiện hợp lệ, nên bốn thứ phải nêu tường minh: tử số tức thế nào là tốt, mẫu số tức sự kiện nào được tính, cửa sổ đo, và phần loại trừ. **Thiếu phần loại trừ thì hai người tính ra hai con số**, chẳng hạn yêu cầu bị chặn vì vượt hạn mức có tính là hỏng không. Ngưỡng tốt phải chọn từ dữ liệu về hành vi người dùng chứ từ con số tròn. Bốn khía cạnh chất lượng dịch vụ cần cam kết riêng và không thay nhau: khả dụng, độ trễ, tính đúng, và độ tươi; một dịch vụ khả dụng 100 phần trăm mà trả số sai thì cam kết khả dụng không nói gì. Mục tiêu đặt theo giá trị nghiệp vụ và chi phí đạt được, chứ theo mong muốn.

**Outcome.** Định nghĩa ba chỉ số phục vụ từ dữ liệu sự kiện thô với bốn phần tường minh và ngưỡng dẫn từ dữ liệu.

**Đánh giá.** Tầng *áp dụng*. Objective có phép kiểm chứng khách quan bằng hai người tính độc lập. Kiểm bằng phép thử hai người; đạt khi ba chỉ số cho cùng con số ở hai người và mỗi ngưỡng dẫn được từ dữ liệu hành vi.

**Lab.** Từ nhật ký sự kiện thô, định nghĩa ba chỉ số phục vụ thuộc ba khía cạnh khác nhau, mỗi cái nêu đủ bốn phần. Chọn ngưỡng tốt từ phân bố độ trễ thật và từ dữ liệu hành vi người dùng. Nhờ một học viên khác tính độc lập ba chỉ số trên cùng dữ liệu và so con số. Tạo một tình huống khả dụng cao mà tính đúng thấp.

**Pitfalls.** Bỏ phần loại trừ · chọn ngưỡng bằng con số tròn · chỉ cam kết khả dụng rồi coi là đủ · tính chỉ số phục vụ từ số đo đã gộp thay vì từ sự kiện.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba chỉ số cho cùng con số khi hai người tính độc lập, ngưỡng dẫn từ dữ liệu hành vi, và tình huống khả dụng cao mà tính đúng thấp được tái hiện.

### Lesson 396 · Error budget, burn rate and the release decision `TH`
**Prerequisites.** Lesson 395

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ngân sách sai sót biến cam kết thành một công cụ ra quyết định thay vì một con số báo cáo. Ngân sách là phần được phép hỏng trong cửa sổ; tốc độ tiêu cho biết đang tiêu nhanh gấp bao nhiêu lần mức bền vững. Cảnh báo hai mức là thực hành chuẩn: tiêu rất nhanh trong cửa sổ ngắn thì gọi người ngay; tiêu vừa phải nhưng kéo dài trong cửa sổ dài thì mở một việc cần xử lý. **Cảnh báo theo tốc độ tiêu thay thế được phần lớn cảnh báo ngưỡng lặt vặt**, vì nó cảnh báo trên thứ người dùng chịu thay vì trên từng chỉ số thành phần. Mức giảm ồn thật phải đo trên chính hệ của mình bằng tỉ lệ cảnh báo hành động được ở lesson 287, chứ nhận theo lời. Chính sách ngân sách phải viết ra trước khi cần dùng: còn ngân sách thì được phát hành tính năng, cạn ngân sách thì dừng phát hành và chuyển sang việc về độ tin cậy; ngoại lệ cần ai duyệt. Viết chính sách trước là điều kiện để nó không bị tranh cãi ngay lúc đang căng thẳng.

**Outcome.** Dựng cảnh báo hai mức theo tốc độ tiêu và nối ngân sách với một quyết định phát hành cụ thể.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là cảnh báo nổ đúng và một quyết định thật được dẫn ra. Kiểm bằng phát lại sự cố; đạt khi cảnh báo nhanh nổ ở sự cố lớn, cảnh báo chậm nổ ở suy giảm kéo dài, và không cái nào nổ trong khoảng bình thường.

**Lab.** Tính ngân sách sai sót cho ba cam kết đã đặt. Dựng cảnh báo hai mức theo tốc độ tiêu. Phát lại ba đoạn dữ liệu lịch sử: một sự cố lớn ngắn, một suy giảm nhỏ kéo dài, và một khoảng bình thường; kiểm phản ứng của từng cảnh báo. Viết chính sách ngân sách và áp vào một quyết định phát hành thật.

**Pitfalls.** Cảnh báo trên từng ngưỡng riêng lẻ thay vì theo tốc độ tiêu · viết chính sách ngân sách sau khi đã cạn · không có ngoại lệ có người duyệt · coi ngân sách là chỉ số báo cáo.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Cảnh báo nhanh nổ ở sự cố lớn, cảnh báo chậm nổ ở suy giảm kéo dài, không cái nào nổ ở khoảng bình thường, và một quyết định phát hành được dẫn ra từ ngân sách.

### Lesson 397 · Failure-mode analysis, dependency map and blast radius `TH`
**Prerequisites.** Lesson 396

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phân tích trước khi hỏng thay vì sau khi hỏng. Bản đồ phụ thuộc liệt kê mọi thứ dịch vụ dựa vào, gồm cả phụ thuộc ngầm hay bị quên như phân giải tên, kho bí mật, sổ đăng ký ảnh và chính hệ đo lường. Với mỗi phụ thuộc, ba câu hỏi: nó hỏng thì dịch vụ còn chạy được phần nào, phạm vi ảnh hưởng tới đâu, và có cách suy giảm thay vì hỏng hẳn không. **Phụ thuộc cứng là phụ thuộc mà khi nó hỏng thì ta hỏng theo, và mục tiêu thiết kế là biến chúng thành phụ thuộc mềm** bằng bộ nhớ đệm, giá trị mặc định hoặc chế độ chỉ đọc. Phạm vi ảnh hưởng đo bằng tỉ lệ người dùng và tỉ lệ chức năng bị ảnh hưởng; thiết kế để thu hẹp phạm vi gồm phân vùng theo khách hàng và vách ngăn ở lesson 319. Năng lực dự phòng và dự báo tải, dùng lại lesson 110.

**Outcome.** Lập bản đồ phụ thuộc có phạm vi ảnh hưởng và biến được ít nhất hai phụ thuộc cứng thành mềm.

**Đánh giá.** Tầng *đánh giá*. Objective đòi phân tích trước rồi kiểm bằng thực nghiệm. Kiểm bằng tiêm lỗi phụ thuộc; đạt khi dự đoán khớp thực tế ở ít nhất ba phụ thuộc và hai phụ thuộc cứng được chuyển thành mềm có số đo.

**Lab.** Lập bản đồ phụ thuộc đầy đủ gồm cả phụ thuộc ngầm. Với mỗi cái, dự đoán hành vi khi nó hỏng và phạm vi ảnh hưởng. Tiêm lỗi cho năm phụ thuộc và so với dự đoán. Chọn hai phụ thuộc cứng và biến thành mềm bằng đệm hoặc chế độ suy giảm; đo lại phạm vi ảnh hưởng. Kiểm năng lực dự phòng bằng một lần chạy tải.

**Pitfalls.** Bỏ sót phụ thuộc ngầm như phân giải tên và kho bí mật · đo phạm vi ảnh hưởng bằng số máy thay vì tỉ lệ người dùng · dự đoán mà không tiêm lỗi kiểm chứng · coi mọi phụ thuộc là cứng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Dự đoán khớp thực tế ở ≥ 3/5 phụ thuộc tiêm lỗi, và hai phụ thuộc cứng chuyển thành mềm với phạm vi ảnh hưởng giảm có số đo.

### Lesson 398 · Overload control - timeout budget, jitter, circuit breaker, shedding `TH`
**Prerequisites.** Lesson 397

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài áp các cơ chế ở lesson 319 vào một hệ thật và đo hiệu lực từng cái. Ngân sách thời gian chờ đầu cuối theo lesson 27, phân bổ xuống từng chặng, và chặng nào thấy ngân sách cạn thì bỏ sớm thay vì thử. Thử lại có ngân sách cùng nhiễu ngẫu nhiên; **thử lại không giới hạn là chất xúc tác của sập dây chuyền**. Ngắt mạch mở ra khi tỉ lệ lỗi vượt ngưỡng và đóng dần lại qua trạng thái thăm dò; ba tham số phải đặt từ số đo. Vách ngăn tách bể tài nguyên theo phụ thuộc để một phụ thuộc hỏng không ăn hết. Loại bỏ tải có chủ ý khi quá tải: từ chối sớm một phần yêu cầu theo mức ưu tiên giữ cho phần còn lại vẫn đúng cam kết; **phục vụ một phần tốt hơn sập toàn bộ**, và quyết định ưu tiên là quyết định nghiệp vụ. Áp lực ngược từ hàng đợi ngược về nguồn.

**Outcome.** Áp năm cơ chế và đo đóng góp của từng cái vào việc giữ tỉ lệ phục vụ dưới quá tải.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là hệ giữ được cam kết cho phần lưu lượng ưu tiên. Kiểm bằng phép thử quá tải; đạt khi bản chưa có cơ chế sập, bản có cơ chế giữ tỉ lệ phục vụ trên ngưỡng, và đóng góp của từng cơ chế có số đo.

**Lab.** Chạy tải vượt năng lực hai lần cho một dịch vụ ba chặng. Đo điểm sập của bản chưa có cơ chế. Thêm lần lượt năm cơ chế và đo sau mỗi lần. Đặt ba tham số của ngắt mạch từ số đo chứ mặc định. Phân loại lưu lượng theo mức ưu tiên và chứng minh phần ưu tiên vẫn đúng cam kết khi đang loại bỏ tải.

**Pitfalls.** Thử lại không có ngân sách · đặt tham số ngắt mạch theo giá trị mặc định · dùng một bể tài nguyên chung cho mọi phụ thuộc · loại bỏ tải ngẫu nhiên thay vì theo mức ưu tiên.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bản chưa có cơ chế sập còn bản có cơ chế giữ tỉ lệ phục vụ trên ngưỡng, đóng góp từng cơ chế có số đo, và phần lưu lượng ưu tiên vẫn đúng cam kết.

### Lesson 399 · Disaster recovery - RPO, RTO and a restore into a clean environment `TH`
**Prerequisites.** Lesson 398

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài nâng phần phục hồi ở lesson 367 lên mức toàn hệ thống. Ba cấp thảm hoạ và cách chuẩn bị khác nhau: mất một thành phần, mất một vùng, và lỗi logic lan ra mọi bản sao. Cấp thứ ba là cấp mà sao chép không cứu được, vì nó nhân bản cả lệnh xoá nhầm hay bản ghi hỏng; chỉ có sao lưu theo thời điểm mới cứu được, theo lesson 145. Kế hoạch phục hồi phải nêu thứ tự khôi phục theo bản đồ phụ thuộc: khôi phục sai thứ tự làm dịch vụ khởi động rồi lỗi và phải làm lại. **Diễn tập phục hồi phải vào một môi trường sạch, vì phục hồi vào môi trường cũ không phát hiện được các phụ thuộc ngầm** đang tồn tại sẵn ở đó. Ba thứ hay thiếu khi phục hồi vào môi trường sạch: thông tin xác thực, cấu hình phân giải tên, và chứng chỉ. Kết quả diễn tập là hai con số đo được, và chúng thường tệ hơn nhiều so với con số trong kế hoạch.

**Outcome.** Chạy phục hồi toàn hệ vào môi trường sạch và đo được hai con số thật, kèm đối soát dữ liệu.

**Đánh giá.** Tầng *đánh giá*. Objective có tiêu chí nghiệm thu là một lần phục hồi thật chứ một kế hoạch. Kiểm bằng diễn tập; đạt khi hệ phục vụ lại được trong môi trường sạch, dữ liệu đối soát khớp, và chênh lệch giữa số đo với mục tiêu được giải thích.

**Lab.** Lập kế hoạch phục hồi có thứ tự theo bản đồ phụ thuộc. Phục hồi toàn hệ vào một môi trường sạch; bấm giờ và ghi lại mọi thứ thiếu. Đối soát dữ liệu sau phục hồi. So hai con số đo được với mục tiêu và giải thích chênh lệch. Diễn tập một lỗi logic lan ra mọi bản sao và phục hồi theo thời điểm.

**Pitfalls.** Coi sao chép là phương án chống thảm hoạ · phục hồi vào môi trường cũ · bỏ bước đối soát dữ liệu sau phục hồi · không thử ca lỗi logic lan ra mọi bản sao.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Hệ phục vụ lại được trong môi trường sạch với hai con số đo thật, dữ liệu đối soát khớp, và chênh lệch so với mục tiêu được giải thích.

### Lesson 400 · Threat modelling - asset, actor, trust boundary, abuse case `LT`
**Prerequisites.** Lesson 399

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài mở phần bảo mật bằng một quy trình có cấu trúc thay vì một danh sách kiểm. Bốn bước: liệt kê tài sản gồm dữ liệu cùng phân loại của nó theo lesson 306; xác định tác nhân cùng năng lực của họ, gồm cả người trong tổ chức; vẽ ranh giới tin cậy là nơi dữ liệu đi từ vùng tin cậy này sang vùng khác; và viết ca lạm dụng tức cách một tác nhân đạt mục tiêu của họ. Xếp hạng theo khả năng xảy ra và mức tác động, có nêu mức không chắc chắn chứ giả vờ chính xác. Với mỗi rủi ro, chọn chốt kiểm soát thuộc một trong bốn nhóm: ngăn chặn, phát hiện, ứng phó, và phục hồi; **một mô hình chỉ có chốt ngăn chặn là một mô hình giả định mình không bao giờ bị xuyên thủng**. Phòng thủ theo chiều sâu. Đầu ra là một bảng ánh xạ rủi ro với chốt kiểm soát, và nó là tài liệu sống được rà lại khi kiến trúc đổi.

**Outcome.** Lập mô hình mối đe doạ bốn bước cho một hệ thật và ánh xạ mỗi rủi ro với chốt kiểm soát đủ bốn nhóm.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết đặt khung cho hai bài thực hành. Kiểm bằng bảng ánh xạ; đạt khi mọi ranh giới tin cậy được vẽ, ít nhất sáu ca lạm dụng được viết, và mỗi rủi ro lớn có chốt ở ít nhất hai trong bốn nhóm.

**Lab.** Với hệ đã dựng ở M19 và M20, chạy bốn bước. Vẽ sơ đồ luồng dữ liệu có ranh giới tin cậy. Viết ít nhất sáu ca lạm dụng, trong đó có ít nhất một từ người trong tổ chức. Xếp hạng theo khả năng và tác động kèm mức không chắc chắn. Ánh xạ rủi ro với chốt kiểm soát theo bốn nhóm và chỉ ra chỗ chỉ có chốt ngăn chặn.

**Pitfalls.** Dùng danh sách kiểm thay cho mô hình mối đe doạ · bỏ qua tác nhân trong tổ chức · chỉ đặt chốt ngăn chặn · xếp hạng rủi ro bằng con số trông chính xác mà không có căn cứ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mọi ranh giới tin cậy được vẽ, ≥ 6 ca lạm dụng gồm ít nhất một từ người trong tổ chức, và mỗi rủi ro lớn có chốt ở ≥ 2 nhóm.

### Lesson 401 · Identity, secrets and key lifecycle in practice `TH`
**Prerequisites.** Lesson 400

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài thực hành phần bảo mật thứ nhất, dựng trên lesson 362 và lesson 369. Phân biệt xác thực với phân quyền và ba lỗi hay gặp ở ranh giới đó, gồm kiểm được đăng nhập mà quên kiểm quyền trên đúng tài nguyên. Giới hạn của mã thông báo dạng tự chứa: nó không thu hồi được trước khi hết hạn, nên thời hạn sống phải ngắn và phải có cơ chế thu hồi riêng cho ca khẩn. Vòng đời khoá và thông tin xác thực gồm tạo, phân phát, xoay, thu hồi, và huỷ; **xoay phải thử được khi dịch vụ đang chạy chứ nằm trong tài liệu**. Đường thoát khẩn cấp cần cho ca mất quyền truy cập, và nó phải được ghi lại cùng cảnh báo khi dùng. Cách ly giữa các khách hàng khi hệ phục vụ nhiều bên: kiểm quyền sở hữu ở mọi lối vào chứ chỉ ở giao diện chính, vì đường phụ là chỗ hay quên.

**Outcome.** Thực hiện xoay và thu hồi khi dịch vụ đang chạy, và chặn được ba lỗi phân quyền bằng phép thử phủ định.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu bằng phép thử phủ định và một thao tác vận hành thật. Kiểm bằng sáu phép thử phủ định cộng một lần xoay; đạt khi cả sáu bị chặn đúng và xoay không gây gián đoạn.

**Lab.** Viết sáu phép thử phủ định gồm truy cập tài nguyên của khách hàng khác qua cả giao diện chính lẫn một đường phụ. Chạy và xác nhận bị chặn. Thực hiện xoay thông tin xác thực khi dịch vụ đang chạy và đo gián đoạn. Thu hồi một mã thông báo trước hạn và chứng minh nó không dùng được nữa. Dùng đường thoát khẩn cấp và xác nhận có cảnh báo cùng bản ghi.

**Pitfalls.** Kiểm đăng nhập mà quên kiểm quyền sở hữu tài nguyên · đặt thời hạn mã thông báo dài vì tiện · chưa từng thử xoay · để đường thoát khẩn cấp không sinh cảnh báo.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Sáu phép thử phủ định bị chặn đúng gồm cả đường phụ, xoay không gây gián đoạn, và mã thông báo thu hồi trước hạn không dùng được.

### Lesson 402 · Supply chain and the secure delivery pipeline `TH`
**Prerequisites.** Lesson 401

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài thực hành bảo mật thứ hai, mở rộng lesson 377 ra toàn bộ đường giao hàng. Bốn chốt trong quy trình tích hợp và triển khai: khoá phiên bản phụ thuộc và quét lỗ hổng có cửa chặn; sinh bản kê thành phần cho mọi hiện vật phát hành; quét bí mật trên mã và trên nhật ký quy trình; và kiểm nguồn gốc hiện vật ở mức nhận biết. Bản thân quy trình tự động là một mục tiêu tấn công giá trị cao vì nó có quyền triển khai: **danh tính của quy trình phải có quyền tối thiểu và phải giới hạn phạm vi theo nhánh cùng môi trường**, nếu không thì một yêu cầu hợp nhất từ nguồn không tin cậy có thể chạy mã với quyền triển khai sản xuất. Ba lỗ hổng điển hình của quy trình tự động. Ứng phó khi có lỗ hổng mới công bố: biết mình đang chạy những gì ở đâu, và đó chính là lý do có bản kê thành phần.

**Outcome.** Dựng bốn chốt trong quy trình giao hàng và chứng minh quy trình không thể tự nâng quyền.

**Đánh giá.** Tầng *áp dụng*. Objective gồm cả bảo vệ chính quy trình tự động. Kiểm bằng bốn vi phạm tiêm cộng một phép thử nâng quyền; đạt khi bốn vi phạm bị chặn và yêu cầu hợp nhất từ nguồn không tin cậy không chạm được vào quyền triển khai.

**Lab.** Dựng bốn chốt trong quy trình. Tiêm bốn vi phạm và xác nhận bị chặn ở đúng chốt. Giới hạn danh tính của quy trình theo nhánh và môi trường; mở một yêu cầu hợp nhất từ một nhánh không tin cậy và chứng minh nó không lấy được quyền triển khai. Với một lỗ hổng giả định mới công bố, dùng bản kê thành phần trả lời trong bao lâu mình đang chạy nó ở đâu.

**Pitfalls.** Cho quy trình tự động quyền triển khai rộng · chạy mã của yêu cầu hợp nhất từ nguồn không tin cậy với bí mật · không quét bí mật trong nhật ký quy trình · không có bản kê thành phần nên không biết mình chạy gì.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn vi phạm bị chặn ở đúng chốt, yêu cầu hợp nhất từ nguồn không tin cậy không chạm được quyền triển khai, và câu hỏi về lỗ hổng mới trả lời được từ bản kê thành phần.

### Lesson 403 · Two game days - overload cascade and credential incident `DA`
**Prerequisites.** Lesson 402

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Bài dự án khép module, chạy hai buổi diễn tập trên hệ đã dựng, với ma trận sự cố hợp nhất làm khung: mỗi sự cố xem qua ba mặt là quan sát được, phản ứng về độ tin cậy, và khía cạnh bảo mật. Buổi thứ nhất là sập dây chuyền do quá tải: một phụ thuộc chậm lại, quan sát chuỗi lan truyền, áp các cơ chế ở lesson 398, và giữ cam kết cho phần lưu lượng ưu tiên. Buổi thứ hai là sự cố thông tin xác thực bị lộ: xác định phạm vi bằng nhật ký kiểm toán, xoay và thu hồi, cô lập, đánh giá dữ liệu nào có thể đã bị lấy, và phục hồi. Cả hai buổi chạy theo vòng đời sự cố ở lesson 288 với vai trò rõ, dòng thời gian, và truyền thông cho bên liên quan. **Phân tích sau sự cố không quy lỗi cá nhân**; mỗi hành động có chủ, có cách kiểm chứng hiệu lực, và có hạn.

**Outcome.** Chạy hai buổi diễn tập đủ vòng đời và nộp phân tích sau sự cố có hành động kiểm chứng được.

**Đánh giá.** Tầng *sáng tạo*. Bài tổng hợp ba mặt của module vào hai sự cố thật. Kiểm bằng hai buổi diễn tập; đạt khi cả hai có dòng thời gian đầy đủ, phạm vi ảnh hưởng xác định bằng bằng chứng, và mọi hành động sau sự cố có chủ cùng cách kiểm chứng cùng hạn.

**Lab.** Chuẩn bị vai trò và kênh truyền thông. Chạy buổi một: tiêm phụ thuộc chậm, ghi thời gian phát hiện, mức suy giảm và thời gian phục hồi. Chạy buổi hai: lộ một thông tin xác thực trong môi trường lab, xác định phạm vi bằng nhật ký kiểm toán, xoay và cô lập. Viết hai bản phân tích sau sự cố theo bốn nhóm hành động là phát hiện, ngăn chặn, kiềm chế và phục hồi.

**Pitfalls.** Chẩn đoán trước khi giảm thiểu khi người dùng đang chịu ảnh hưởng · quy lỗi cá nhân trong phân tích sau sự cố · hành động không có chủ và không có hạn · xoá bằng chứng khi dọn dẹp sự cố.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Hai buổi có dòng thời gian đầy đủ và phạm vi ảnh hưởng xác định bằng bằng chứng, và mọi hành động sau sự cố có chủ, cách kiểm chứng và hạn.

### Lesson 404 · Gate 9 - redeploy from code and recover from an injected incident `KT`
**Prerequisites.** Lesson 403

**In-class (180 phút).** 135 phút làm bài độc lập · 45 phút chữa bài và phân tích lỗi theo nhóm

**Learn.** Cổng của Phase 9. Bài kiểm ba module: trừu tượng đám mây ở M19, vùng chứa cùng hạ tầng khai báo cùng điều phối ở M20, và quan sát được cùng tin cậy cùng bảo mật ở M21. Không có nội dung mới.

**Outcome.** Dựng lại toàn hệ từ mã trong môi trường sạch, phục hồi sau một sự cố được tiêm, và bảo vệ các lựa chọn về danh tính, chi phí và độ tin cậy.

**Đánh giá.** Tầng *đánh giá*. Cổng đo năng lực vận hành đầu cuối, nên hình thức là thực hành tại chỗ cộng bảo vệ.

**Lab.** Buổi 180 phút: 135 phút làm bài độc lập, 45 phút chữa bài. Bài chấm sáu phần: A (20đ) dựng lại một lát cắt hệ trong môi trường sạch chỉ từ mã, kho ảnh và bản sao lưu, không thao tác tay · B (15đ) chẩn đoán ba khối lượng công việc hỏng theo đúng thứ tự bằng chứng · C (20đ) một sự cố được tiêm; chạy vòng đời sự cố, xác định phạm vi ảnh hưởng bằng bằng chứng và phục hồi · D (15đ) định nghĩa một chỉ số phục vụ từ sự kiện thô đủ bốn phần và dẫn ra một quyết định phát hành từ ngân sách sai sót · E (15đ) trình mô hình mối đe doạ và chỉ ra chốt kiểm soát cho ba rủi ro lớn nhất, đủ ít nhất hai nhóm · F (15đ) trình bảng chi phí trên mỗi đơn vị và một phương án cho cú sốc chi phí gấp mười.

**Pitfalls.** Sửa trực tiếp trên cụm thay vì qua mã · gọi người trực vì một số đo không hành động được · phục hồi mà không đối soát dữ liệu · trình mô hình mối đe doạ chỉ có chốt ngăn chặn.

**Self-study (2,4 giờ).** Không có bài tự học. Nếu không đạt, theo phụ lục khắc phục khi không đạt cổng

**Done when.** Đạt ≥ 70/100, phần A và C đều ≥ 60%. Dùng thao tác tay để hoàn thành phần A thì phần đó bằng không; phục hồi ở phần C mà không đối soát dữ liệu thì phần đó bằng không.

# MODULE M22 · SYSTEM DESIGN PROGRESSION

**Phase 10 · Lessons 405–420 · 32 giờ**

| | |
|---|---|
| **Objective cấp module** | Chạy một quy trình thiết kế mười bước cho năm loại hệ, và bảo vệ được quyết định rồi thay đổi nó khi một ràng buộc đổi |
| **Tiền đề** | M8 · M11 · M14 · M15 · M19 · M20 · M21 |
| **Exit criterion** | Người rà soát truy được mọi thành phần về một yêu cầu hoặc một bảo đảm; bảng năng lực có giả định và độ nhạy; bảng chế độ hỏng có phát hiện, ứng phó và hệ quả với dữ liệu |
| **Kỹ năng SFIA** | `ARCH` mức 5 · `SYSP` mức 5 |
| **Chế độ hỏng** | Vẽ một thành phần không gắn với yêu cầu nào, nói cuối cùng nhất quán mà không có hợp đồng với người dùng, coi bộ nhớ đệm là nguồn sự thật, và bỏ qua năng lực, bảo mật cùng đường quay lui |

Module không dạy kiến thức mới; nó buộc dùng lại toàn bộ chương trình dưới áp lực của một quy trình có thứ tự và của phản biện.

Hai phép thử chạy cho mọi thiết kế. **Phép thử bỏ thành phần:** gỡ một hộp ra thì mất bảo đảm nào; nếu không mất gì thì hộp đó không có lý do tồn tại. **Phép thử đổi ràng buộc:** gấp mười lưu lượng, yêu cầu xoá dữ liệu nghiêm ngặt, mất một vùng, hoặc cắt nửa ngân sách; thiết kế phải đổi được mà không mất tính đúng.

Bậc thang mười bài toán đi từ một dịch vụ đơn tới một nền tảng nhiều khách hàng; ba bài được cài đặt, ba bài được đo thử, bốn bài rà soát trên giấy.

### Lesson 405 · The ten-step design process `LT`
**Prerequisites.** Module 22: M21

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài mở module bằng một quy trình có thứ tự cố định, vì bỏ bước hoặc đảo bước là nguồn của phần lớn thiết kế hỏng. Mười bước: làm rõ người dùng cùng ca sử dụng, yêu cầu chức năng cùng phi chức năng và phi mục tiêu; lượng hoá lưu lượng, dữ liệu, thời hạn giữ, độ trễ, khả dụng, nhất quán, hai con số phục hồi và chi phí; định nghĩa giao diện, sự kiện, mô hình dữ liệu và quyền sở hữu; vẽ kiến trúc tối thiểu cùng đường dữ liệu trọng yếu; phát biểu bất biến và ranh giới nhất quán; tính năng lực từng thành phần rồi tìm nút thắt; liệt kê chế độ hỏng cùng phát hiện, giảm thiểu và phục hồi; bảo mật cùng quyền riêng tư cùng quản trị cùng quan sát được cùng triển khai cùng di trú; nêu phương án thay thế và đánh đổi cùng điều kiện thiết kế không còn phù hợp; và kiểm chứng bằng một thử nghiệm nhỏ rồi viết bản ghi quyết định. **Phi mục tiêu ở bước một là phần lọc mạnh nhất** và hay bị bỏ nhất.

**Outcome.** Chạy đủ mười bước cho một bài toán nhỏ và dừng được ở bước hai với các con số có căn cứ.

**Đánh giá.** Tầng *áp dụng*. Bài mở module, áp một quy trình vào một bài toán đã quen. Kiểm bằng rà soát mười bước; đạt khi mọi bước có đầu ra ghi lại và bước hai có con số kèm giả định chứ để trống.

**Lab.** Lấy bài toán rút gọn địa chỉ. Chạy đủ mười bước và nộp đầu ra từng bước. Ở bước một, viết ít nhất ba phi mục tiêu. Ở bước hai, mọi con số kèm giả định và nguồn. Đổi bài chéo: người khác đọc và tìm một thành phần chưa gắn với yêu cầu nào.

**Pitfalls.** Vẽ kiến trúc trước khi lượng hoá yêu cầu · bỏ phi mục tiêu · ghi con số mà không ghi giả định · nhảy tới phương án thay thế trước khi có kiến trúc tối thiểu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mười bước có đầu ra ghi lại, ít nhất ba phi mục tiêu, và mọi con số ở bước hai kèm giả định cùng nguồn.

### Lesson 406 · Quantifying requirements - traffic, data, latency, RPO and cost `TH`
**Prerequisites.** Lesson 405

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài rèn bước hai, vì đây là bước quyết định mọi con số sau. Sáu nhóm phải lượng hoá: số yêu cầu mỗi giây ở mức trung bình và mức đỉnh cùng tỉ số giữa chúng; lượng dữ liệu mỗi ngày, tổng dữ liệu theo thời hạn giữ, và tập dữ liệu làm việc; mục tiêu độ trễ phát biểu theo phân vị chứ theo trung bình; mục tiêu khả dụng cùng mô hình nhất quán mà người dùng quan sát được; hai con số phục hồi; và ngân sách chi phí. **Phân bố mới là thứ quyết định thiết kế, không phải giá trị trung bình**: một hệ có tỉ số đỉnh trên trung bình bằng mười cần thiết kế khác hẳn hệ có tỉ số bằng hai. Khoá nóng và khách hàng nóng phải ước lượng riêng. Mọi con số kèm giả định và kèm độ nhạy: nếu giả định sai gấp đôi thì kết luận nào đổi. Ba cách lấy con số khi chưa có hệ: từ hệ tương tự, từ quy mô nghiệp vụ, và từ giới hạn trên hiển nhiên.

**Outcome.** Lượng hoá sáu nhóm cho hai bài toán, kèm giả định, độ nhạy và ước lượng khoá nóng.

**Đánh giá.** Tầng *áp dụng*. Objective đòi con số có căn cứ và có biên độ chứ một con số đơn. Kiểm bằng rà soát chéo; đạt khi mọi con số có giả định và nguồn, tỉ số đỉnh trên trung bình được nêu, và độ nhạy chỉ ra được kết luận nào đổi.

**Lab.** Cho hai bài toán khác nhau về hình dạng tải. Lượng hoá sáu nhóm cho từng cái. Với mỗi con số, ghi cách lấy và giả định. Tính tỉ số đỉnh trên trung bình và ước lượng phân bố khoá. Chạy phân tích độ nhạy: nhân đôi hai giả định quan trọng nhất và ghi kết luận nào đổi.

**Pitfalls.** Thiết kế theo giá trị trung bình · phát biểu độ trễ bằng trung bình · bỏ ước lượng khoá nóng · ghi con số mà không ghi cách lấy.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Sáu nhóm có con số kèm giả định và nguồn ở cả hai bài toán, tỉ số đỉnh trên trung bình được nêu, và phân tích độ nhạy chỉ ra kết luận đổi.

### Lesson 407 · Invariants and consistency boundaries `TH`
**Prerequisites.** Lesson 406

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài rèn bước năm, và nó là bước phân biệt một thiết kế đúng với một sơ đồ hợp lý. Bất biến là mệnh đề luôn đúng bất kể thứ tự thao tác và bất kể lỗi; ví dụ số dư không âm, một khoá nghiệp vụ có đúng một bản ghi hiện hành theo lesson 157, hoặc tổng ở hai tầng phải khớp. **Bất biến quyết định ranh giới giao dịch và ranh giới phân vùng**: mọi thứ phải đúng cùng lúc thì phải nằm trong cùng một ranh giới nguyên tử; đặt chúng ở hai nơi thì bất biến đó không cưỡng chế được và phải chuyển sang bù trừ theo lesson 318. Từ đó suy ra câu hỏi thứ hai của bài: cái gì là nguồn sự thật và cái gì là dữ liệu dẫn xuất dựng lại được; **bộ nhớ đệm và dữ liệu dẫn xuất không bao giờ là nguồn sự thật**, và đường dựng lại phải mô tả được. Nhất quán cuối cùng phải kèm hợp đồng với người dùng về mức cũ tối đa, theo lesson 314.

**Outcome.** Phát biểu bất biến cho hai thiết kế và suy ra ranh giới giao dịch cùng đường dựng lại dữ liệu dẫn xuất.

**Đánh giá.** Tầng *phân tích*. Objective đòi suy ranh giới từ bất biến chứ đặt theo thói quen. Kiểm bằng bài phân tích; đạt khi mỗi bất biến chỉ ra đúng ranh giới cưỡng chế nó, mọi dữ liệu dẫn xuất có đường dựng lại, và mọi nhất quán cuối cùng có hợp đồng mức cũ.

**Lab.** Với hai thiết kế, liệt kê ít nhất năm bất biến mỗi cái. Với từng bất biến, chỉ ra nó được cưỡng chế ở đâu và chuyện gì xảy ra nếu hai thành phần liên quan nằm hai phân vùng. Phân loại mọi kho dữ liệu thành nguồn sự thật hay dẫn xuất, và mô tả đường dựng lại cho từng cái dẫn xuất. Với mỗi chỗ nhất quán cuối cùng, viết hợp đồng mức cũ tối đa.

**Pitfalls.** Coi bộ nhớ đệm là nguồn sự thật · nói cuối cùng nhất quán mà không có hợp đồng mức cũ · đặt ranh giới phân vùng trước khi phát biểu bất biến · không có đường dựng lại cho dữ liệu dẫn xuất.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mỗi bất biến chỉ ra đúng ranh giới cưỡng chế, mọi dữ liệu dẫn xuất có đường dựng lại, và mọi nhất quán cuối cùng có hợp đồng mức cũ.

### Lesson 408 · The capacity sheet - assumptions and sensitivity `TH`
**Prerequisites.** Lesson 407

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài rèn bước sáu và tạo ra một hiện vật bắt buộc cho mọi thiết kế về sau. Bảng năng lực tính cho từng thành phần: số yêu cầu mỗi giây nó phải chịu, số kết nối đồng thời, lượng byte mỗi ngày, tập dữ liệu làm việc phải nằm trong bộ nhớ, và băng thông mạng. Mỗi ô có công thức chứ một con số, để đổi giả định thì bảng tự cập nhật. Từ bảng suy ra hai thứ: thành phần nào chạm trần trước, và ở giả định nào nó chạm. **Biết nút thắt đầu tiên quan trọng hơn biết năng lực tổng**, vì nó cho biết nên đầu tư vào đâu và cho biết thiết kế còn dùng được tới quy mô nào. Ngưỡng theo giai đoạn: thay vì thiết kế cho quy mô xa, nêu ngưỡng mà kiến trúc phải đổi và đổi thành gì. Độ nhạy chỉ ra giả định nào ảnh hưởng lớn nhất, và đó là giả định cần kiểm bằng thử nghiệm nhỏ trước tiên.

**Outcome.** Lập bảng năng lực có công thức cho một thiết kế và chỉ ra nút thắt đầu tiên cùng ngưỡng đổi kiến trúc.

**Đánh giá.** Tầng *áp dụng*. Objective có hiện vật kiểm được và một kết luận cụ thể. Kiểm bằng rà soát bảng; đạt khi mọi ô có công thức, nút thắt đầu tiên được chỉ ra kèm giả định, và ít nhất hai ngưỡng đổi kiến trúc được nêu.

**Lab.** Lập bảng năng lực cho mọi thành phần của một thiết kế, mỗi ô là công thức tham chiếu tới các giả định ở lesson 406. Tìm thành phần chạm trần trước và ghi ở giả định nào. Nhân đôi ba giả định lần lượt và ghi nút thắt có đổi không. Nêu hai ngưỡng mà kiến trúc phải đổi kèm mô tả đổi thành gì.

**Pitfalls.** Ghi con số cố định thay vì công thức · tính năng lực tổng mà không tìm nút thắt · thiết kế thẳng cho quy mô xa nhất · bỏ tập dữ liệu làm việc khỏi bảng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mọi ô có công thức, nút thắt đầu tiên được chỉ ra kèm giả định, và ≥ 2 ngưỡng đổi kiến trúc được nêu kèm mô tả.

### Lesson 409 · Sequence 1 - a single stateful service `TH`
**Prerequisites.** Lesson 408

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bậc thứ nhất của bậc thang, và nó rèn thói quen truy một phép ghi cùng một phép đọc qua mọi thành phần. Một dịch vụ đơn có trạng thái gồm giao diện, logic, cơ sở dữ liệu và bộ nhớ đệm. Bốn câu hỏi cho mỗi thành phần: trạng thái nào được lưu bền, ranh giới thử lại ở đâu, điểm nhất quán ở đâu, và phục hồi lấy dữ liệu từ nguồn nào. Ba bài toán ở bậc này: rút gọn địa chỉ với sinh khoá, bộ nhớ đệm chuyển hướng, khoá nóng và hết hạn; bộ giới hạn tốc độ với trạng thái phân tán và đánh đổi giữa chính xác với khả dụng; và dịch vụ tệp với việc tách siêu dữ liệu khỏi khối dữ liệu, tải lên nhiều phần, toàn vẹn và vòng đời. **Bộ nhớ đệm làm hỏng tính đúng theo hai cách phải nêu: dữ liệu cũ và mất hiệu lực sai**, nên chính sách vô hiệu hoá phải viết ra chứ để mặc định.

**Outcome.** Truy một phép ghi và một phép đọc qua mọi thành phần của ba thiết kế bậc một.

**Đánh giá.** Tầng *áp dụng*. Objective là một thói quen truy vết áp cho mọi thiết kế sau. Kiểm bằng bài truy vết; đạt khi bốn câu hỏi có câu trả lời ở mọi thành phần của cả ba thiết kế và chính sách vô hiệu hoá bộ nhớ đệm được viết ra.

**Lab.** Thiết kế ba bài toán bậc một. Với mỗi cái, truy một phép ghi và một phép đọc qua mọi thành phần và trả lời bốn câu hỏi. Với bài rút gọn địa chỉ, tính năng lực và chỉ ra khoá nóng. Với bộ giới hạn tốc độ, nêu đánh đổi giữa đếm chính xác với khả dụng khi kho trạng thái chậm. Viết chính sách vô hiệu hoá bộ nhớ đệm.

**Pitfalls.** Thêm bộ nhớ đệm mà không có chính sách vô hiệu hoá · bỏ qua khoá nóng · không truy phép đọc riêng khỏi phép ghi · để ranh giới thử lại không xác định.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn câu hỏi có câu trả lời ở mọi thành phần của ba thiết kế, và chính sách vô hiệu hoá bộ nhớ đệm được viết ra.

### Lesson 410 · Sequence 2 - replicated and partitioned `TH`
**Prerequisites.** Lesson 409

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bậc thứ hai thêm nhiều bản sao và nhiều phân vùng, nên nó kéo theo toàn bộ M15. Bốn quyết định: định tuyến yêu cầu tới phân vùng nào; chọn giữa người dẫn và số đông theo lesson 312 và 315; xử lý tái phân bố khi thêm hoặc bớt nút theo lesson 313; và hành vi khi đọc phải bản sao cũ. Ba câu hỏi phải trả lời cho mọi thiết kế ở bậc này: mất một nút thì mất bảo đảm gì, phân vùng mạng thì bên nào tiếp tục phục vụ, và tái phân bố chạy trong lúc phục vụ thì ảnh hưởng ra sao. **Nói thêm một bản sao là không đủ; phải nói bản sao đồng bộ hay bất đồng bộ và lượng dữ liệu mất tối đa là bao nhiêu.** Bài toán ở bậc này là dịch vụ thông báo có nhiều kênh, có tuỳ chọn của người dùng, có khử trùng, có thử lại và có yêu cầu về thứ tự.

**Outcome.** Thiết kế một dịch vụ có bản sao và phân vùng, trả lời được ba câu hỏi và nêu lượng dữ liệu mất tối đa.

**Đánh giá.** Tầng *áp dụng*. Objective đòi nối lựa chọn sao chép với một con số rủi ro. Kiểm bằng rà soát thiết kế; đạt khi ba câu hỏi có câu trả lời cụ thể, lượng dữ liệu mất tối đa tính được, và cách xử lý khoá nóng được nêu.

**Lab.** Thiết kế dịch vụ thông báo nhiều kênh. Chọn cách phân vùng và cách sao chép kèm lý do. Trả lời ba câu hỏi. Tính lượng dữ liệu mất tối đa từ độ trễ sao chép. Mô tả quy trình tái phân bố có giới hạn tốc độ. Nêu chính sách khử trùng và yêu cầu về thứ tự mà người dùng quan sát được.

**Pitfalls.** Nói thêm bản sao mà không nói đồng bộ hay bất đồng bộ · bỏ qua ảnh hưởng của tái phân bố lên dịch vụ đang chạy · giả định thứ tự toàn cục · không nêu hành vi khi đọc phải bản sao cũ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba câu hỏi có câu trả lời cụ thể, lượng dữ liệu mất tối đa tính được từ độ trễ sao chép, và quy trình tái phân bố có giới hạn tốc độ.

### Lesson 411 · Sequence 3 - asynchronous workflow `TH`
**Prerequisites.** Lesson 410

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bậc thứ ba tách xử lý ra khỏi đường yêu cầu, và nó kéo theo M16 cùng M18. Ranh giới đồng bộ và bất đồng bộ là quyết định trung tâm: phần nào phải xong trước khi trả lời người dùng, phần nào làm sau. Bốn thứ phải thiết kế: trạng thái của bên tiêu thụ và cách nó tiến, thử lại cùng luỹ đẳng theo lesson 105, áp lực ngược khi bên tiêu thụ chậm hơn bên sản xuất, và bản ghi độc cùng hàng đợi lỗi. **Chuyển sang bất đồng bộ đổi hợp đồng với người dùng chứ chỉ đổi kiến trúc**: người dùng nhận lời hứa sẽ xử lý thay vì kết quả, nên giao diện phải có cách tra trạng thái và có cách báo khi thất bại. Bài toán ở bậc này là nền tảng nhật ký với nạp, đệm, đánh chỉ mục, lưu trữ lâu dài, truy vấn, thời hạn giữ và nhiều khách hàng.

**Outcome.** Thiết kế một luồng bất đồng bộ có hợp đồng người dùng rõ và xử lý được bên tiêu thụ chậm.

**Đánh giá.** Tầng *áp dụng*. Objective gồm một hệ quả về hợp đồng mà thiết kế hay bỏ qua. Kiểm bằng rà soát thiết kế; đạt khi ranh giới đồng bộ và bất đồng bộ có lý do, hợp đồng người dùng nêu cách tra trạng thái cùng cách báo thất bại, và áp lực ngược có cơ chế cụ thể.

**Lab.** Thiết kế nền tảng nhật ký. Chỉ ra ranh giới đồng bộ và bất đồng bộ cùng lý do. Viết hợp đồng người dùng cho phần bất đồng bộ gồm cách tra trạng thái và cách báo thất bại. Thiết kế áp lực ngược và chính sách bản ghi độc. Tính năng lực cho phần đệm khi bên tiêu thụ dừng một giờ.

**Pitfalls.** Chuyển sang bất đồng bộ mà không đổi hợp đồng với người dùng · không có cách tra trạng thái · để hàng đợi không giới hạn · bỏ chính sách bản ghi độc.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ranh giới đồng bộ và bất đồng bộ có lý do, hợp đồng người dùng đủ hai phần, và năng lực đệm khi bên tiêu thụ dừng một giờ tính được.

### Lesson 412 · Sequence 4 - an analytical platform `TH`
**Prerequisites.** Lesson 411

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bậc thứ tư là bậc gần nhất với công việc thật của chương trình, và nó gộp M11 tới M14D. Năm chặng: nạp dữ liệu, lưu trữ bất biến, chốt siêu dữ liệu, tính toán phân tán, và tầng phục vụ. Với mỗi chặng, nêu hợp đồng vào và hợp đồng ra, và nêu chặng đó chạy lại được từ đâu. Ba bài toán ở bậc này: nền tảng phân tích với hợp đồng sự kiện cùng quản trị; kho dữ liệu kết hợp với nạp theo lô cùng bắt thay đổi, chốt bảng, danh mục và cách ly tính toán; và phân tích dòng chảy với phân vùng, thời gian sự kiện, mốc nước, trạng thái và đích. **Yêu cầu riêng của bậc này là chứng minh tính đầy đủ, chứ chỉ vẽ luồng**: thiết kế phải chỉ ra đối soát chạy ở đâu và chênh lệch được quy về đoạn nào, theo lesson 284.

**Outcome.** Thiết kế một nền tảng phân tích có chốt đối soát ở mọi chặng và đường chạy lại rõ.

**Đánh giá.** Tầng *áp dụng*. Objective đòi tính đầy đủ chứ một sơ đồ luồng. Kiểm bằng rà soát thiết kế; đạt khi mỗi chặng có hợp đồng vào ra cùng đường chạy lại, và chốt đối soát đặt đủ để quy chênh lệch về một đoạn.

**Lab.** Thiết kế một trong ba bài toán bậc bốn. Với mỗi chặng, viết hợp đồng vào ra và đường chạy lại. Đặt chốt đối soát và chỉ ra một chênh lệch giả định được quy về đoạn nào. Tính năng lực cho chặng tốn nhất. Nêu cách cách ly tính toán giữa các khối lượng công việc.

**Pitfalls.** Vẽ luồng mà không có chốt đối soát · bỏ đường chạy lại ở một chặng · để mọi khối lượng công việc dùng chung một cụm tính toán · bỏ quản trị và quyền sở hữu khỏi thiết kế.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mỗi chặng có hợp đồng vào ra và đường chạy lại, và chốt đối soát đủ để quy một chênh lệch giả định về đúng đoạn.

### Lesson 413 · Sequence 5 - a multi-tenant platform `TH`
**Prerequisites.** Lesson 412

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bậc cao nhất, và nó thêm một chiều mà bốn bậc trước không có: nhiều khách hàng dùng chung hạ tầng. Tách mặt phẳng điều khiển khỏi mặt phẳng dữ liệu theo lesson 361. Bốn cơ chế bắt buộc: cách ly dữ liệu giữa các khách hàng cưỡng chế ở mọi lối vào; hạn mức để một khách hàng không ăn hết năng lực theo lesson 333; chính sách và ngoại lệ có chủ cùng hạn; và tự phục vụ để đội nền tảng không thành nút cổ chai. **Vấn đề đặc trưng là khách hàng ồn ào: một khách chạy khối lượng nặng làm mọi khách khác chậm**, và cách chặn là hạn mức cộng vách ngăn chứ trông chờ vào thiện chí. Quy chi phí về từng khách hàng cần gắn thẻ và đo theo đơn vị theo lesson 368. Thiết kế này còn phải nêu cách đội dùng nền tảng tự làm được việc mà không mở phiếu yêu cầu.

**Outcome.** Thiết kế nền tảng nhiều khách hàng có cách ly, hạn mức, quy chi phí và đường tự phục vụ.

**Đánh giá.** Tầng *đánh giá*. Objective gồm cả chiều tổ chức chứ chỉ kỹ thuật. Kiểm bằng rà soát thiết kế cộng ba tình huống; đạt khi cách ly cưỡng chế ở mọi lối vào, tình huống khách hàng ồn ào có cơ chế chặn cụ thể, và chi phí quy được về từng khách hàng.

**Lab.** Thiết kế nền tảng dữ liệu nhiều khách hàng. Liệt kê mọi lối vào và chỉ ra cách ly cưỡng chế ở từng lối. Thiết kế hạn mức và vách ngăn; mô phỏng tình huống khách hàng ồn ào và chỉ ra cơ chế chặn. Thiết kế cách quy chi phí về từng khách hàng. Mô tả đường tự phục vụ cho ba việc thường gặp nhất.

**Pitfalls.** Cách ly chỉ ở giao diện chính mà quên đường phụ · không có hạn mức nên một khách ăn hết năng lực · không quy được chi phí về khách hàng · để mọi thay đổi đi qua phiếu yêu cầu cho đội nền tảng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Cách ly cưỡng chế ở mọi lối vào, tình huống khách hàng ồn ào có cơ chế chặn cụ thể, chi phí quy được về từng khách hàng, và ba việc tự phục vụ được mô tả.

### Lesson 414 · The failure table and the remove-component test `TH`
**Prerequisites.** Lesson 413

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hai hiện vật bắt buộc cho mọi thiết kế, và cả hai đều lọc ra những thứ không có lý do tồn tại. Bảng chế độ hỏng có sáu cột: thành phần, tác nhân kích hoạt, triệu chứng, cách phát hiện, ứng phó tự động hay thủ công, và **hệ quả với dữ liệu**; cột cuối là cột hay thiếu nhất và là cột quan trọng nhất với một hệ dữ liệu, vì mất khả dụng khác mất dữ liệu. Phép thử bỏ thành phần: với từng hộp trong sơ đồ, giả sử gỡ nó ra và hỏi mất bảo đảm nào; **nếu không mất gì thì hộp đó chưa được biện minh** và phải gỡ hoặc phải viết ra bảo đảm nó giữ. Phép thử này bắt được ba thứ thừa hay gặp: một tầng đệm không ai cần, một hàng đợi giữa hai dịch vụ luôn đồng bộ, và một kho dữ liệu trùng chức năng với kho khác.

**Outcome.** Lập bảng chế độ hỏng sáu cột và chạy phép thử bỏ thành phần cho mọi hộp trong một thiết kế.

**Đánh giá.** Tầng *đánh giá*. Objective đòi biện minh từng thành phần chứ mô tả chúng. Kiểm bằng hai hiện vật; đạt khi mọi thành phần có ít nhất một dòng trong bảng hỏng kèm hệ quả với dữ liệu, và mọi hộp qua được phép thử bỏ thành phần hoặc bị gỡ.

**Lab.** Với một thiết kế đã làm, lập bảng chế độ hỏng đủ sáu cột cho mọi thành phần. Chạy phép thử bỏ thành phần cho từng hộp và ghi bảo đảm mất đi. Gỡ mọi hộp không biện minh được và vẽ lại sơ đồ. So số thành phần trước và sau.

**Pitfalls.** Bỏ cột hệ quả với dữ liệu · viết ứng phó mà không nói cách phát hiện · giữ thành phần vì kiến trúc tham khảo nào đó có nó · chạy phép thử bỏ thành phần chỉ cho vài hộp.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mọi thành phần có dòng trong bảng hỏng kèm hệ quả với dữ liệu, và mọi hộp còn lại đều qua phép thử bỏ thành phần.

### Lesson 415 · Cost model and unit economics in a design `TH`
**Prerequisites.** Lesson 414

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Chi phí là một chiều thiết kế ngang hàng với hiệu năng và độ tin cậy, nên nó có mô hình chứ một ước tính. Mô hình chi phí tính từ bảng năng lực ở lesson 408: mỗi thành phần có công thức chi phí theo các giả định, nên đổi giả định thì chi phí tự cập nhật. Chi phí trên mỗi đơn vị theo lesson 368 là con số dùng để so hai phương án và để phát hiện vấn đề khi quy mô tăng. **Ba thành phần chi phí không tỉ lệ với công việc hữu ích và hay bị bỏ sót: lưu lượng ra ngoài, năng lực nhàn rỗi, và chi phí của chính hệ đo lường.** Chi phí của độ tin cậy phải nêu tường minh: chạy nhiều vùng đắt gấp mấy lần và mua được gì. Ngưỡng chi phí theo giai đoạn giống ngưỡng năng lực: tới quy mô nào thì mô hình chi phí đổi và phải thiết kế lại.

**Outcome.** Lập mô hình chi phí theo công thức cho một thiết kế và so hai phương án theo chi phí trên mỗi đơn vị.

**Đánh giá.** Tầng *đánh giá*. Objective đòi so phương án bằng chi phí đơn vị chứ tổng ước tính. Kiểm bằng mô hình cộng bài so; đạt khi mọi ô là công thức, ba thành phần hay bị bỏ sót đều có mặt, và hai phương án so được ở ít nhất hai mức quy mô.

**Lab.** Lập mô hình chi phí theo công thức cho mọi thành phần của một thiết kế. Tính chi phí trên mỗi đơn vị. Dựng phương án thứ hai khác về kiến trúc và so ở hai mức quy mô cách nhau mười lần; chỉ ra mức mà thứ hạng đảo ngược nếu có. Tính riêng chi phí của độ tin cậy nhiều vùng và nêu nó mua được gì.

**Pitfalls.** Ước tính tổng mà không quy về đơn vị · bỏ lưu lượng ra ngoài · bỏ chi phí của hệ đo lường · so hai phương án ở một mức quy mô duy nhất.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mọi ô là công thức, ba thành phần hay bị bỏ sót đều có mặt, và hai phương án so được ở hai mức quy mô kèm điểm đảo ngược nếu có.

### Lesson 416 · Alternatives, trade-offs and reversibility `TH`
**Prerequisites.** Lesson 415

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài rèn bước chín, và nó là bước phân biệt một thiết kế với một lựa chọn đã định sẵn. Ba phương án thật, luôn gồm phương án không làm gì; **một phương án thật là phương án mà nếu ràng buộc đổi thì nó sẽ thắng**, nên hai phương án dựng lên chỉ để loại bỏ là dấu hiệu quyết định đã định trước. Với mỗi phương án, lượng hoá hệ quả theo cùng bộ tiêu chí. Phân loại quyết định theo mức đảo ngược: quyết định dễ đảo thì quyết nhanh và học từ thực tế; quyết định khó đảo thì cần thử nghiệm nhỏ trước và cần bản ghi quyết định. Ba loại chi phí của việc đảo ngược: chi phí kỹ thuật, chi phí di trú dữ liệu, và chi phí tổ chức. **Điều kiện thiết kế không còn phù hợp phải viết ra cùng lúc với quyết định**, vì viết sau thì không ai viết, và không có nó thì kiến trúc sống quá hạn.

**Outcome.** Trình ba phương án thật có lượng hoá và nêu điều kiện làm lựa chọn không còn phù hợp.

**Đánh giá.** Tầng *đánh giá*. Objective chống lại việc trình bày một quyết định đã định sẵn. Kiểm bằng rà soát chéo; đạt khi mỗi phương án có ít nhất một bối cảnh mà nó thắng, mọi hệ quả được lượng hoá theo cùng bộ tiêu chí, và điều kiện đảo ngược được nêu.

**Lab.** Với một quyết định kiến trúc thật, dựng ba phương án gồm cả không làm gì. Lượng hoá hệ quả theo cùng bộ tiêu chí. Với mỗi phương án, nêu một bối cảnh mà nó thắng. Phân loại quyết định theo mức đảo ngược và tính ba loại chi phí đảo ngược cho phương án chọn. Viết hai điều kiện làm lựa chọn không còn phù hợp.

**Pitfalls.** Dựng phương án rơm để loại · so các phương án theo bộ tiêu chí khác nhau · bỏ phương án không làm gì · không viết điều kiện thiết kế hết phù hợp.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mỗi phương án có một bối cảnh mà nó thắng, hệ quả lượng hoá theo cùng bộ tiêu chí, và hai điều kiện đảo ngược được nêu kèm chi phí.

### Lesson 417 · Migration design - dual run, cutover, rollback `TH`
**Prerequisites.** Lesson 416

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phần lớn thiết kế trong công việc thật là thiết kế cho một hệ đang chạy, nên di trú là một phần của thiết kế chứ một việc sau đó. Bốn giai đoạn: kiểm kê bên tiêu thụ theo lesson 264; chạy song song hai hệ và đối soát kết quả; chuyển đổi dần theo từng phần lưu lượng hoặc từng khách hàng; và giữ đường quay lui cho tới khi hệ cũ được gỡ. **Chạy song song là giai đoạn cho bằng chứng, và bỏ nó là bỏ cách duy nhất biết hệ mới đúng trước khi phụ thuộc vào nó.** Một lần chuyển đổi toàn bộ là chế độ hỏng đặc trưng vì nó không có đường lùi. Thời hạn giữ hệ cũ tính từ thời gian cần để phát hiện vấn đề, chứ từ mong muốn dọn sớm. Di trú dữ liệu có hai bài toán riêng: chuyển khối dữ liệu lịch sử, và giữ hai hệ đồng bộ trong lúc chuyển.

**Outcome.** Thiết kế kế hoạch di trú bốn giai đoạn có đối soát khi chạy song song và đường quay lui đã thử.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là bằng chứng từ giai đoạn chạy song song. Kiểm bằng rà soát kế hoạch cộng một lần diễn tập; đạt khi kiểm kê bên tiêu thụ đầy đủ, đối soát chạy song song có tiêu chí đạt, và quay lui được diễn tập.

**Lab.** Lập kế hoạch di trú cho một thay đổi kiến trúc thật. Kiểm kê bên tiêu thụ bằng khai báo cộng nhật ký truy vấn. Thiết kế giai đoạn chạy song song kèm tiêu chí đối soát để chuyển sang giai đoạn sau. Chia chuyển đổi theo từng phần. Diễn tập quay lui ở một môi trường thử. Tính thời hạn giữ hệ cũ từ thời gian phát hiện vấn đề.

**Pitfalls.** Chuyển đổi toàn bộ một lần · bỏ giai đoạn chạy song song vì tốn gấp đôi · gỡ hệ cũ theo lịch thay vì theo kiểm kê · không diễn tập quay lui.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Kiểm kê bên tiêu thụ đầy đủ, đối soát chạy song song có tiêu chí đạt, quay lui diễn tập thành công, và thời hạn giữ hệ cũ có căn cứ.

### Lesson 418 · Design review simulation - three passes `TH`
**Prerequisites.** Lesson 417

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài rèn năng lực rà soát, vì đọc thiết kế của người khác là cách nhanh nhất để thấy lỗ hổng trong thiết kế của mình. Ba lượt rà soát có trọng tâm khác nhau và phải chạy tách biệt: lượt một về tính đúng, kiểm bất biến cùng ngữ nghĩa giao diện và mô hình dữ liệu; lượt hai về vận hành, kiểm chế độ hỏng cùng quy mô cùng bảo mật cùng chi phí; lượt ba về ràng buộc đổi. Người rà soát phải truy được mọi thành phần về một yêu cầu hoặc một bảo đảm, và câu hỏi mặc định là thành phần này giữ bảo đảm nào. Ba câu hỏi lọc dùng được ở mọi lượt: bất biến nào quyết định ranh giới giao dịch, thành phần nào chạm trần trước và ở giả định nào, và mỗi phụ thuộc hỏng thì cái gì mất khả dụng hoặc mất nhất quán. **Rà soát mà chỉ ghi nhận đồng ý là một buổi diễn**; mỗi lượt phải ghi phản đối và ghi quyết định.

**Outcome.** Rà soát ba thiết kế của người khác theo ba lượt và ghi được phản đối cùng quyết định cho từng lượt.

**Đánh giá.** Tầng *đánh giá*. Objective đo năng lực phát hiện lỗ hổng chứ năng lực đồng ý. Kiểm bằng rà soát chéo; đạt khi mỗi thiết kế nhận ít nhất ba phát hiện có căn cứ ở các lượt khác nhau, và mọi phát hiện dẫn ra thành phần cùng bảo đảm liên quan.

**Lab.** Đổi thiết kế với ba học viên khác. Với mỗi thiết kế, chạy ba lượt riêng biệt và ghi biên bản gồm phản đối, câu hỏi chưa trả lời được, và quyết định. Dùng ba câu hỏi lọc ở mọi lượt. Nhận biên bản về thiết kế của mình và sửa; ghi rõ phát hiện nào chấp nhận, phát hiện nào từ chối cùng lý do.

**Pitfalls.** Gộp ba lượt thành một buổi · chỉ ghi nhận đồng ý · phát hiện mà không dẫn ra thành phần liên quan · từ chối phản đối mà không nêu lý do.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mỗi thiết kế nhận ≥ 3 phát hiện có căn cứ ở các lượt khác nhau, và biên bản ghi đủ phản đối cùng quyết định cho từng lượt.

### Lesson 419 · The changed-constraint defence `TH`
**Prerequisites.** Lesson 418

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài rèn năng lực quan trọng nhất của module: bảo vệ một quyết định rồi thay đổi nó khi ràng buộc đổi, mà không bám vào quyết định cũ. Bốn ràng buộc đổi chuẩn: lưu lượng gấp mười; yêu cầu xoá dữ liệu nghiêm ngặt theo quy định; mất một vùng; và cắt nửa ngân sách. Thêm hai ràng buộc về tổ chức: đội nhỏ lại một nửa, và thời hạn rút ngắn còn một phần ba. Với mỗi ràng buộc, ba câu hỏi: phần nào của thiết kế còn đúng, phần nào phải đổi, và đổi đó tốn gì. **Câu trả lời đúng thường không phải giữ nguyên thiết kế và cũng không phải vẽ lại từ đầu**, mà là chỉ ra đúng phần bị ảnh hưởng dựa trên bảng năng lực và bảng chế độ hỏng đã có. Hai thói quen cần bỏ: bảo vệ quyết định vì đã bỏ công vào nó, và đổi toàn bộ thiết kế vì một ràng buộc đổi.

**Outcome.** Điều chỉnh một thiết kế cho bốn ràng buộc đổi, mỗi lần chỉ đúng phần bị ảnh hưởng kèm chi phí.

**Đánh giá.** Tầng *đánh giá*. Objective đo năng lực thích ứng có căn cứ, và nó là tiêu chí ra của module. Kiểm bằng bốn tình huống đổi ràng buộc; đạt khi ít nhất ba lần chỉ đúng phần bị ảnh hưởng dẫn từ bảng năng lực hoặc bảng chế độ hỏng, và không lần nào vẽ lại toàn bộ khi không cần.

**Lab.** Người chấm đổi lần lượt bốn ràng buộc trên thiết kế đã làm. Với mỗi cái, trả lời ba câu hỏi trong 15 phút, dẫn từ bảng năng lực và bảng chế độ hỏng. Ghi chi phí của việc đổi. Với ràng buộc về tổ chức, chỉ ra phần nào của thiết kế phải bỏ đi thay vì làm chậm hơn.

**Pitfalls.** Bám vào quyết định cũ vì đã bỏ công · vẽ lại toàn bộ thiết kế khi một ràng buộc đổi · trả lời mà không dẫn từ bảng năng lực · bỏ qua ràng buộc về tổ chức.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** ≥ 3/4 lần chỉ đúng phần bị ảnh hưởng dẫn từ hiện vật đã có, mỗi lần kèm chi phí, và không lần nào vẽ lại toàn bộ khi không cần.

### Lesson 420 · Capstone design dossier - RFC, spike and ADRs `DA`
**Prerequisites.** Lesson 419

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Bài dự án khép module, và hồ sơ này là hiện vật chính để bảo vệ tốt nghiệp. Nộp gồm sáu phần: một bản đề xuất kỹ thuật từ sáu tới mười trang kèm sơ đồ; bảng năng lực có công thức và độ nhạy theo lesson 408; bảng chế độ hỏng sáu cột cùng mô hình mối đe doạ theo lesson 400 và 414; **một thử nghiệm nhỏ chạy được kiểm chứng giả định rủi ro nhất**, chứ một lập luận; ba bản ghi quyết định cho ba quyết định khó đảo ngược, mỗi bản có phương án thay thế và điều kiện xem lại; và kế hoạch di trú bốn giai đoạn theo lesson 417 cùng danh mục kiểm sẵn sàng vận hành và kế hoạch đo trong 30, 60, 90 ngày. Bài toán chọn ở bậc bốn hoặc bậc năm của bậc thang. Yêu cầu chấm nghiêm nhất: người rà soát phải truy được mọi thành phần về một yêu cầu hoặc một bảo đảm.

**Outcome.** Nộp hồ sơ thiết kế đủ sáu phần, có thử nghiệm nhỏ chạy được và mọi thành phần truy được về một yêu cầu.

**Đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module thành một hiện vật bảo vệ được. Kiểm bằng rà soát ba lượt cộng phép thử truy ngược; đạt khi mọi thành phần truy được về một yêu cầu hoặc bảo đảm, thử nghiệm nhỏ cho kết quả kiểm chứng giả định, và bốn ràng buộc đổi được trả lời.

**Lab.** Chọn một bài toán bậc bốn hoặc bậc năm. Dựng đủ sáu phần của hồ sơ. Chạy thử nghiệm nhỏ cho giả định rủi ro nhất và báo cáo kết quả kể cả khi nó bác bỏ giả định. Trình bày 30 phút và chịu ba lượt rà soát cùng bốn ràng buộc đổi.

**Pitfalls.** Viết thử nghiệm nhỏ thành một đoạn lập luận thay vì chạy thật · để một thành phần không truy được về yêu cầu nào · bỏ kế hoạch di trú vì thiết kế là hệ mới · giấu kết quả thử nghiệm khi nó bác bỏ giả định.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Sáu phần đầy đủ, mọi thành phần truy được về một yêu cầu hoặc bảo đảm, thử nghiệm nhỏ chạy thật có kết quả báo cáo trung thực, và bốn ràng buộc đổi được trả lời.

# MODULE M23 · MODERN AI ENGINEERING, BOUNDED

**Phase 10 · Lessons 421–430 · 20 giờ**

| | |
|---|---|
| **Objective cấp module** | Dùng mô hình ngôn ngữ như một thành phần có hợp đồng, có đánh giá, có ngân sách và có mô hình mối đe doạ; biết khi nào một phương án đơn giản hơn thắng |
| **Tiền đề** | M2 · M6 · M8 · M11 · M14 · M19 · M21 |
| **Exit criterion** | Mã do công cụ sinh ra không được hợp nhất khi chưa có kiểm thử, rà soát tĩnh và rà soát bảo mật; bộ đánh giá bắt được hồi quy; kiến trúc giải thích được khi nào tìm kiếm đơn giản thắng phương án tăng cường truy hồi |
| **Kỹ năng SFIA** | `DATS` mức 3 · `SCTY` mức 4 |
| **Chế độ hỏng** | Lấy vài lần chạy thử thành công làm kết quả đánh giá, dựa vào câu lệnh nhắc để bảo mật, và coi thành công khi trình diễn là sẵn sàng cho sản xuất |

Module ở **mức `C`**: biết khi nào nên dùng và khi nào không, chứ không phải xây mô hình. Ranh giới này là chủ ý và được kiểm ở phần đánh giá: nếu một phương án đơn giản hơn đạt cùng kết quả thì phương án phức tạp không được chọn.

Hai nguyên tắc chi phối toàn module. **Đầu ra của mô hình là dữ liệu không tin cậy**, nên nó phải được kiểm lược đồ và phải bị giới hạn quyền ở ranh giới công cụ. Và **vài lần chạy thử thành công không phải kết quả đánh giá**: phải có tập đối chứng, có số đo, và có bộ kịch bản đối kháng.

Nền tảng học máy chỉ ở mức nhận biết; đây không phải đường đi sâu về vận hành mô hình.

### Lesson 421 · The boundary of this module - what it is and is not `LT`
**Prerequisites.** Module 23: M22

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài mở module bằng việc đặt ranh giới, vì đây là chỗ dễ trôi nhất. Module này học cách dùng mô hình ngôn ngữ như một thành phần trong hệ dữ liệu: nó có hợp đồng giao diện, có độ trễ, có chi phí, có tỉ lệ lỗi, và có mô hình mối đe doạ riêng. Nó **không** dạy huấn luyện mô hình, không dạy vận hành mô hình ở mức chuyên sâu, và không thay công việc phân tích. Mô hình khái niệm tối thiểu cần có: đơn vị mã hoá văn bản và cửa sổ ngữ cảnh, cơ chế chú ý ở mức khái niệm, và ba giai đoạn huấn luyện ở mức nhận biết. Ba thuộc tính kỹ thuật có hệ quả thiết kế: **đầu ra không tất định nên phép thử phải chịu được biến thiên**; chi phí và độ trễ tỉ lệ với số đơn vị mã hoá nên chúng tính trước được; và cửa sổ ngữ cảnh là ràng buộc cứng nên việc chọn đưa gì vào là một bài toán thiết kế chứ một chi tiết.

**Outcome.** Phân định việc thuộc và không thuộc phạm vi module, và nêu ba hệ quả thiết kế của ba thuộc tính kỹ thuật.

**Đánh giá.** Tầng *hiểu*. Bài mở module, đặt ranh giới. Kiểm bằng bài phân định mười tình huống; đạt khi phân đúng ít nhất tám và ba hệ quả thiết kế được nêu cụ thể.

**Lab.** Cho mười tình huống công việc; phân loại thuộc phạm vi module, thuộc một module khác, hay không thuộc chương trình. Với ba thuộc tính kỹ thuật, viết một hệ quả thiết kế cụ thể cho từng cái. Tính trước chi phí và độ trễ của một lời gọi từ số đơn vị mã hoá ước lượng và đối chiếu với số đo thật.

**Pitfalls.** Trôi sang huấn luyện mô hình · coi đầu ra tất định nên viết phép thử so khớp chuỗi · bỏ qua ràng buộc cửa sổ ngữ cảnh khi thiết kế · ước lượng chi phí sau khi chạy thay vì trước.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân đúng ≥ 8/10 tình huống, ba hệ quả thiết kế được nêu cụ thể, và chi phí cùng độ trễ ước lượng trước khớp số đo thật trong sai số thoả thuận.

### Lesson 422 · AI-assisted engineering with verification `TH`
**Prerequisites.** Lesson 421

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Dùng công cụ sinh mã trong công việc thật, với kỷ luật kiểm chứng làm trung tâm. Câu lệnh nhắc và ngữ cảnh là một bản đặc tả: cung cấp giao diện, ràng buộc, kiểm thử và ví dụ thì kết quả dùng được; mô tả mơ hồ thì nhận về mã trông hợp lý mà sai. Cách dùng đúng là **yêu cầu giả thuyết và kiểm thử, rồi tự chạy, chứ áp bản vá một cách mù quáng**. Khi gỡ lỗi, làm sạch nhật ký trước khi đưa vào và tái hiện lỗi độc lập chứ tin lời giải thích. Rà soát mã sinh ra theo bốn trục: tính đúng, bảo mật, giấy phép, và nguồn gốc; đo hiệu năng của mã sinh ra thay vì giả định. Một điểm phải kiểm luôn: **thư viện và tham số do công cụ đề xuất có thể đã lỗi thời hoặc không tồn tại**, nên đối chiếu với tài liệu chính thức kèm phiên bản là bước bắt buộc.

**Outcome.** Dùng công cụ sinh mã cho ba nhiệm vụ với kỷ luật kiểm chứng và phát hiện được lỗi trong mã sinh ra.

**Đánh giá.** Tầng *áp dụng*. Objective đòi kiểm chứng chứ tiêu thụ. Kiểm bằng ba nhiệm vụ; đạt khi mọi đoạn mã sinh ra đều qua kiểm thử cùng rà soát bảo mật trước khi hợp nhất, và ít nhất một lỗi trong mã sinh ra được phát hiện bằng kiểm thử.

**Lab.** Chọn ba nhiệm vụ lập trình có tiêu chí rõ. Với mỗi cái, viết đặc tả gồm giao diện, ràng buộc và kiểm thử trước khi yêu cầu sinh mã. Chạy kiểm thử, rà soát tĩnh và rà soát bảo mật. Ghi lại mọi chỗ mã sinh ra sai, gồm cả tham số hoặc thư viện không tồn tại. Đo hiệu năng và so với bản viết tay.

**Pitfalls.** Hợp nhất mã sinh ra mà chưa có kiểm thử · dán nhật ký chứa bí mật vào công cụ · tin lời giải thích thay vì tái hiện lỗi · dùng tham số công cụ đề xuất mà không tra tài liệu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mọi đoạn mã sinh ra qua kiểm thử và rà soát bảo mật trước khi hợp nhất, và ≥ 1 lỗi trong mã sinh ra được kiểm thử phát hiện.

### Lesson 423 · The LLM API contract - structured output, tools, budgets `TH`
**Prerequisites.** Lesson 422

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Coi mô hình như một dịch vụ bên ngoài và áp đúng kỷ luật ở M8. Hợp đồng gồm: chọn mô hình theo năng lực, độ trễ, chi phí, quyền riêng tư và hỗ trợ công cụ, kèm ghim phiên bản và phương án dự phòng khi nhà cung cấp hỏng hoặc khai tử mô hình. Đầu ra có cấu trúc kèm kiểm lược đồ: **đầu ra sai lược đồ là chuyện bình thường phải xử lý chứ một sự cố**, nên cần thử lại có giới hạn và cần đường dự phòng. Gọi công cụ chỉ là mô hình đề nghị một lời gọi, và việc thực hiện thuộc về mã của ta; đây là chỗ đặt kiểm quyền ở lesson 428. Hết giờ, thử lại và hạn mức theo lesson 224, với lưu ý thử lại chỉ áp cho lỗi an toàn. Ngân sách số đơn vị mã hoá, ngân sách tốc độ và giới hạn đồng thời phải đặt trước. Câu lệnh nhắc và cấu hình là mã có phiên bản, gắn với bộ đánh giá của bản phát hành.

**Outcome.** Cài lớp gọi có kiểm lược đồ, ngân sách và dự phòng, chịu được ba chế độ hỏng của nhà cung cấp.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là hệ vẫn đúng dưới lỗi của bên ngoài. Kiểm bằng ba chế độ hỏng tiêm; đạt khi cả ba được xử lý không sập, đầu ra sai lược đồ không lọt xuống hạ nguồn, và ngân sách không bị vượt.

**Lab.** Cài lớp gọi có kiểm lược đồ đầu ra, thử lại có giới hạn, ngân sách đơn vị mã hoá và giới hạn đồng thời. Tiêm ba chế độ hỏng: hết giờ, vượt hạn mức, và đầu ra sai lược đồ. Chứng minh không đầu ra sai nào lọt xuống hạ nguồn. Đặt câu lệnh nhắc và cấu hình vào kho mã có phiên bản. Kiểm phương án dự phòng khi mô hình chính không dùng được.

**Pitfalls.** Phân tích đầu ra bằng cách tìm chuỗi thay vì kiểm lược đồ · thử lại mọi lỗi · không ghim phiên bản mô hình · để câu lệnh nhắc nằm ngoài kho mã.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba chế độ hỏng được xử lý không sập, không đầu ra sai lược đồ nào lọt hạ nguồn, ngân sách không bị vượt, và dự phòng hoạt động.

### Lesson 424 · Retrieval - chunking, embedding, filters and rerank `TH`
**Prerequisites.** Lesson 423

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Tầng truy hồi quyết định chất lượng câu trả lời nhiều hơn phần sinh văn bản, nên nó được học kỹ hơn. Đường đi: lấy tài liệu, phân tích, chia đoạn, nhúng thành véctơ, đánh chỉ mục, truy hồi, lọc, sắp xếp lại, rồi mới dựng ngữ cảnh. Chia đoạn theo ranh giới ngữ nghĩa cùng phần chồng lấn và giữ siêu dữ liệu; cấu trúc cha con giữ được ngữ cảnh mục lớn. Truy hồi thưa dựa trên từ khoá và truy hồi dày dựa trên véctơ bắt được hai loại truy vấn khác nhau, nên kết hợp thường thắng. Bộ sắp xếp lại đắt nhưng cải thiện rõ ở phần đầu danh sách. Hai điểm bắt buộc: **kho véctơ là một chỉ mục chứ nguồn sự thật**, nên dựng lại được từ nguồn; và **lọc theo quyền phải áp trước khi trả kết quả**, không phải sau, nếu không thì rò rỉ dữ liệu giữa các khách hàng. Đổi phiên bản mô hình nhúng buộc dựng lại toàn bộ chỉ mục.

**Outcome.** Dựng đường truy hồi có lọc theo quyền và đo được độ phủ ở k trước khi tới phần sinh văn bản.

**Đánh giá.** Tầng *áp dụng*. Objective đo tầng truy hồi riêng chứ đo kết quả cuối. Kiểm bằng tập đối chứng truy hồi; đạt khi độ phủ ở k đo được cho ba cấu hình, và phép thử phủ định về quyền không trả về tài liệu ngoài phạm vi.

**Lab.** Dựng tập tài liệu có phân quyền theo khách hàng. Cài ba cấu hình truy hồi: chỉ từ khoá, chỉ véctơ, và kết hợp có sắp xếp lại. Xây tập đối chứng gồm truy vấn và tài liệu đúng. Đo độ phủ ở k và độ chính xác cho cả ba. Chạy phép thử phủ định về quyền. Đổi phiên bản mô hình nhúng và đo ảnh hưởng khi chưa dựng lại chỉ mục.

**Pitfalls.** Coi kho véctơ là nguồn sự thật · lọc quyền sau khi truy hồi · chia đoạn theo số ký tự cố định cắt ngang câu · đổi mô hình nhúng mà không dựng lại chỉ mục.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Độ phủ ở k đo được cho ba cấu hình, phép thử phủ định về quyền không rò tài liệu, và ảnh hưởng của việc đổi mô hình nhúng được định lượng.

### Lesson 425 · Grounding, citation and abstention `TH`
**Prerequisites.** Lesson 424

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba cơ chế biến một câu trả lời trôi chảy thành một câu trả lời dùng được. Bám nguồn nghĩa là mọi khẳng định phải dẫn được về một đoạn văn bản cụ thể trong tài liệu, kèm phiên bản tài liệu. Trích dẫn ánh xạ từng khẳng định tới đoạn nguồn chứ tới cả tài liệu, vì trích dẫn ở mức tài liệu không kiểm chứng được. **Trích dẫn bịa là chế độ hỏng nguy hiểm nhất** vì nó tạo vẻ đáng tin: câu trả lời trông có căn cứ trong khi nguồn không nói điều đó; cách chặn là kiểm trích dẫn bằng máy, đối chiếu đoạn được dẫn với nội dung thật. Từ chối trả lời khi bằng chứng không đủ là một tính năng chứ một thất bại, và ngưỡng từ chối là một tham số phải đo theo lesson 426. Chính sách cho tài liệu mâu thuẫn hoặc đã cũ: trình bày cả hai kèm phiên bản chứ chọn bừa một bên.

**Outcome.** Cài kiểm trích dẫn bằng máy và cơ chế từ chối, chứng minh không trích dẫn bịa nào lọt.

**Đánh giá.** Tầng *áp dụng*. Objective có một tiêu chí nghiệm thu nhị phân về tính trung thực. Kiểm bằng tập đối chứng có tài liệu mâu thuẫn và câu hỏi không có đáp án; đạt khi không trích dẫn bịa nào lọt và tỉ lệ từ chối đúng trên nhóm câu không có đáp án vượt ngưỡng.

**Lab.** Xây tập đối chứng gồm câu hỏi có đáp án, câu hỏi không có đáp án trong tài liệu, và câu hỏi có hai tài liệu mâu thuẫn. Cài trích dẫn ở mức đoạn và kiểm trích dẫn bằng máy. Cài cơ chế từ chối có ngưỡng. Đo tỉ lệ trích dẫn bịa, tỉ lệ từ chối đúng và tỉ lệ từ chối nhầm. Áp chính sách cho tài liệu mâu thuẫn.

**Pitfalls.** Trích dẫn ở mức tài liệu · không kiểm trích dẫn bằng máy · coi từ chối là thất bại rồi ép mô hình luôn trả lời · chọn một tài liệu khi có mâu thuẫn mà không nói.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Không trích dẫn bịa nào lọt qua phép kiểm máy, tỉ lệ từ chối đúng vượt ngưỡng trên nhóm không có đáp án, và tài liệu mâu thuẫn được trình bày kèm phiên bản.

### Lesson 426 · The evaluation blueprint - five layers `TH`
**Prerequisites.** Lesson 425

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài đặt ra chuẩn đánh giá của module, thay cho việc thử vài câu rồi kết luận. Năm tầng, mỗi tầng có số đo riêng: tầng nạp tài liệu đo độ phủ phân tích, độ tươi, quyền truy cập và trùng lặp; tầng truy hồi đo độ phủ ở k, độ chính xác và tính đúng của bộ lọc; tầng sinh văn bản đo mức bám nguồn, tính đúng của nhiệm vụ, chất lượng trích dẫn và tỉ lệ từ chối; tầng hệ thống đo độ trễ phân vị, tỉ lệ lỗi, chi phí trên mỗi đơn vị và khả dụng; tầng an toàn đo kết quả trên bộ kịch bản đối kháng. **Đo tách từng tầng là điều kiện để biết sửa chỗ nào**, vì một câu trả lời sai có thể do truy hồi trượt hoặc do sinh văn bản sai, và hai nguyên nhân cần hai cách sửa. Tập đối chứng phải gắn với bản phát hành và chạy lại ở mỗi lần đổi câu lệnh nhắc, đổi mô hình hoặc đổi chỉ mục. Rà soát người cho phần không đo được bằng máy.

**Outcome.** Dựng bộ đánh giá năm tầng chạy tự động và bắt được hồi quy khi đổi một thành phần.

**Đánh giá.** Tầng *áp dụng*. Objective là một cửa chặn hồi quy có số đo theo tầng. Kiểm bằng ba thay đổi tiêm; đạt khi mỗi thay đổi làm đúng tầng tương ứng xuống điểm và bộ đánh giá chặn được bản phát hành.

**Lab.** Dựng bộ đánh giá năm tầng trên tập đối chứng cố định. Chạy lấy đường cơ sở. Tiêm ba thay đổi: đổi cách chia đoạn, đổi câu lệnh nhắc, và đổi phiên bản mô hình. Với mỗi cái, chỉ ra tầng nào xuống điểm. Đặt ngưỡng chặn phát hành và xác nhận nó chặn đúng. Thêm một vòng rà soát người cho phần không đo được.

**Pitfalls.** Thử vài câu rồi kết luận · chỉ đo kết quả cuối nên không biết sửa tầng nào · đổi tập đối chứng mỗi lần đánh giá · bỏ tầng chi phí và độ trễ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba thay đổi tiêm làm đúng tầng tương ứng xuống điểm, và bộ đánh giá chặn được bản phát hành theo ngưỡng.

### Lesson 427 · Baseline first - when simple search beats retrieval augmentation `TH`
**Prerequisites.** Lesson 426

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài chống lại việc mặc định chọn phương án phức tạp, và nó là bài thể hiện rõ nhất mức `C` của module. Quy trình bắt buộc: dựng đường cơ sở đơn giản nhất trước, đo trên cùng tập đối chứng, rồi mới thêm độ phức tạp và **chỉ giữ phần nào cải thiện đủ bù chi phí của nó**. Ba đường cơ sở phải thử: tìm kiếm theo từ khoá, tra cứu có cấu trúc trên dữ liệu đã có, và một quy tắc nghiệp vụ đơn giản. Bốn tình huống mà phương án đơn giản thắng: câu hỏi có đáp án nằm trong một trường dữ liệu; tập tài liệu nhỏ và ít đổi; yêu cầu độ trễ rất thấp; và yêu cầu giải thích được đến mức không chấp nhận sinh văn bản. Chi phí của độ phức tạp phải nêu tường minh: thêm thành phần phải vận hành, thêm chi phí trên mỗi truy vấn, thêm chế độ hỏng, và thêm bề mặt bảo mật ở lesson 428.

**Outcome.** So đường cơ sở với phương án tăng cường truy hồi trên cùng tập đối chứng và biện minh độ phức tạp bằng số.

**Đánh giá.** Tầng *đánh giá*. Objective đòi biện minh độ phức tạp chứ mặc định chọn nó. Kiểm bằng bài so; đạt khi ba đường cơ sở có số đo trên cùng tập đối chứng, và quyết định dùng hay không dùng phương án phức tạp dẫn được từ cặp cải thiện với chi phí.

**Lab.** Dựng ba đường cơ sở cho cùng bài toán. Đo trên cùng tập đối chứng với cùng số đo ở lesson 426. Dựng phương án tăng cường truy hồi và đo lại. Tính chi phí trên mỗi truy vấn và số thành phần phải vận hành cho từng phương án. Kết luận bằng cặp cải thiện với chi phí. Tìm một loại câu hỏi mà đường cơ sở thắng.

**Pitfalls.** Bắt đầu từ phương án phức tạp nhất · so hai phương án trên hai tập dữ liệu khác nhau · bỏ chi phí vận hành khỏi so sánh · kết luận bằng cảm nhận về chất lượng câu trả lời.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba đường cơ sở có số đo trên cùng tập đối chứng, quyết định dẫn từ cặp cải thiện với chi phí, và một loại câu hỏi mà đường cơ sở thắng được chỉ ra.

### Lesson 428 · Prompt injection, tool permission and tenant isolation `TH`
**Prerequisites.** Lesson 427

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài bảo mật của module, và nó dựa trên một nguyên tắc duy nhất: **mọi thứ mô hình đọc được đều là dữ liệu không tin cậy, gồm cả tài liệu được truy hồi**. Tiêm chỉ dẫn qua nội dung xảy ra khi một tài liệu chứa câu lệnh hướng mô hình làm việc khác; nó không chặn được bằng cách viết thêm câu lệnh nhắc, vì cả hai đều là văn bản trong cùng ngữ cảnh. Ba lớp phòng thủ thật: **kiểm quyền ở ranh giới công cụ chứ ở câu lệnh nhắc**, tức mã thực hiện lời gọi tự kiểm quyền của người dùng thật; danh sách cho phép cho công cụ và tham số; và phê duyệt của người cho thao tác không đảo ngược được. Rò rỉ dữ liệu ra ngoài qua một công cụ có khả năng gửi đi là ca hỏng nặng nhất. Cách ly giữa các khách hàng áp trước truy hồi theo lesson 424. Vòng lặp gọi công cụ không kiểm soát gây chi phí tăng vọt, nên cần giới hạn số bước và ngân sách.

**Outcome.** Tái hiện ba tấn công và chặn bằng ba lớp phòng thủ ở ranh giới công cụ, không bằng câu lệnh nhắc.

**Đánh giá.** Tầng *phân tích*. Objective đòi đặt chốt kiểm soát đúng chỗ. Kiểm bằng bộ 30 kịch bản đối kháng; đạt khi mọi kịch bản rò rỉ dữ liệu hoặc vượt quyền bị chặn ở ranh giới công cụ, và không phòng thủ nào chỉ dựa trên câu lệnh nhắc.

**Lab.** Dựng bộ 30 kịch bản đối kháng gồm tiêm chỉ dẫn qua tài liệu, cố lấy dữ liệu của khách hàng khác, và cố gọi công cụ ngoài quyền. Chạy trên hệ chưa có phòng thủ và đếm số kịch bản thành công. Thêm ba lớp phòng thủ và chạy lại. Chứng minh phòng thủ nằm ở mã chứ ở câu lệnh nhắc. Đặt giới hạn số bước gọi công cụ và ngân sách.

**Pitfalls.** Chặn tiêm chỉ dẫn bằng cách viết thêm vào câu lệnh nhắc · cho công cụ dùng quyền của dịch vụ thay vì của người dùng · không giới hạn số bước gọi công cụ · ghi cả nội dung nhạy cảm vào vết theo dõi.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mọi kịch bản rò rỉ hoặc vượt quyền bị chặn ở ranh giới công cụ, không phòng thủ nào chỉ dựa vào câu lệnh nhắc, và vòng lặp gọi công cụ có giới hạn.

### Lesson 429 · Serving - latency, cost, fallback and version lineage `TH`
**Prerequisites.** Lesson 428

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài vận hành của module, áp M21 vào một thành phần có đặc thù riêng. Độ trễ phân vị 95 chịu ảnh hưởng của số đơn vị mã hoá đầu ra nhiều hơn đầu vào, nên giới hạn độ dài đầu ra là đòn bẩy chính. Bộ nhớ đệm có hai mức: đệm theo câu hỏi giống hệt, và đệm theo kết quả truy hồi; **đệm phải tính tới quyền của người dùng, nếu không thì một người thấy câu trả lời dựng từ tài liệu của người khác**. Xử lý theo lô và hàng đợi cho khối lượng không cần tức thời. Đường dự phòng khi mô hình chính hỏng: mô hình khác, đường cơ sở đơn giản hơn ở lesson 427, hoặc trả lời rằng chưa phục vụ được. Truy vết nguồn gốc phải ghi đủ bốn thứ cho mỗi câu trả lời: phiên bản mô hình, phiên bản câu lệnh nhắc, phiên bản chỉ mục, và tập tài liệu đã dùng; thiếu bốn thứ này thì không điều tra được một câu trả lời sai.

**Outcome.** Đạt ngưỡng độ trễ và chi phí với đệm an toàn theo quyền và truy vết nguồn gốc đủ bốn thứ.

**Đánh giá.** Tầng *áp dụng*. Objective có ba tiêu chí nghiệm thu gồm một ca bảo mật. Kiểm bằng phép thử tải cộng phép thử đệm; đạt khi độ trễ phân vị 95 và chi phí trên mỗi truy vấn dưới ngưỡng, đệm không rò dữ liệu giữa người dùng, và mọi câu trả lời truy được bốn thứ.

**Lab.** Chạy tải và đo độ trễ phân vị cùng chi phí trên mỗi truy vấn. Giới hạn độ dài đầu ra và đo lại. Bật hai mức đệm và chạy phép thử phủ định: hai người dùng có quyền khác nhau hỏi cùng câu và kiểm không ai thấy tài liệu ngoài quyền. Cài ghi nguồn gốc bốn thứ. Tiêm lỗi nhà cung cấp và kiểm đường dự phòng.

**Pitfalls.** Đệm theo câu hỏi mà bỏ qua quyền người dùng · tối ưu độ trễ bằng cách bỏ bước truy hồi · không ghi phiên bản chỉ mục nên không điều tra được câu trả lời cũ · không có đường dự phòng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Độ trễ phân vị 95 và chi phí trên mỗi truy vấn dưới ngưỡng, đệm không rò dữ liệu giữa người dùng, và mọi câu trả lời truy được đủ bốn thứ.

### Lesson 430 · Grounded assistant project with a red-team suite `DA`
**Prerequisites.** Lesson 429

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Bài dự án khép module, lấy đúng yêu cầu dự án của hợp đồng nguồn: một trợ lý trả lời câu hỏi trên tài liệu kỹ thuật, có bám nguồn. Nộp gồm bảy hạng mục: nạp tài liệu có phiên bản và truy vết nguồn gốc từng đoạn; trả lời có cấu trúc kèm trích dẫn ở mức đoạn và **có từ chối khi bằng chứng không đủ**; tập đối chứng gồm câu hỏi bình thường, câu hỏi đối kháng, tài liệu đã cũ và tài liệu mâu thuẫn; số đo năm tầng theo lesson 426 gồm cả độ trễ phân vị 95 và chi phí; ba lớp phòng thủ ở lesson 428 cùng kết quả bộ 30 kịch bản đối kháng; so với đường cơ sở đơn giản theo lesson 427; và quy trình thử nghiệm dần khi đổi câu lệnh nhắc, đổi mô hình hoặc đổi chỉ mục, kèm đường quay lui. Bốn điều kiện tự động chưa đạt: lấy vài lần chạy thử làm đánh giá, phòng thủ chỉ bằng câu lệnh nhắc, rò rỉ dữ liệu nhạy cảm, và không có cơ chế từ chối cùng ngân sách cùng dự phòng.

**Outcome.** Nộp trợ lý đủ bảy hạng mục, vượt đường cơ sở có số đo, và không vi phạm bốn điều kiện tự động chưa đạt.

**Đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module. Kiểm bằng số đo năm tầng cộng bộ đối kháng; đạt khi mọi tầng có số đo, bộ 30 kịch bản không có kịch bản nào rò rỉ, và phần cải thiện so với đường cơ sở đủ bù chi phí tăng thêm.

**Lab.** Dựng trợ lý theo bảy hạng mục. Chạy bộ đánh giá năm tầng và bộ 30 kịch bản đối kháng. So với ba đường cơ sở. Thực hiện một lần đổi mô hình theo quy trình thử nghiệm dần rồi quay lui. Trình bày 20 phút và trả lời chất vấn về một câu trả lời sai: nó sai ở tầng nào và sửa thế nào.

**Pitfalls.** Trình diễn vài câu hỏi thuận lợi thay vì chạy bộ đánh giá · bỏ cơ chế từ chối để tỉ lệ trả lời cao · dựa vào câu lệnh nhắc để chặn tiêm chỉ dẫn · bỏ so sánh với đường cơ sở.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Năm tầng đều có số đo, không kịch bản đối kháng nào rò rỉ, cải thiện so với đường cơ sở đủ bù chi phí, và không vi phạm bốn điều kiện tự động chưa đạt.

# MODULE M24 · STAFF AND PRINCIPAL TRAJECTORY

**Phase 10 · Lessons 431–440 · 21 giờ**

| | |
|---|---|
| **Objective cấp module** | Chuyển từ làm xong việc sang thay đổi cách nhiều đội làm việc, bằng hiện vật có người đọc, có áp dụng và có kết quả đo được |
| **Tiền đề** | M1 tới M22, cộng ít nhất một hệ đã vận hành đủ lâu để có bằng chứng về sự cố, chi phí và thay đổi |
| **Exit criterion** | Ba bản đề xuất được rà soát, một bản được triển khai và đo sau khi áp dụng; một lần di trú có tương thích, quay lui, chủ sở hữu, số đo và bằng chứng bên tiêu thụ thật; **ít nhất hai kỹ sư hoặc hai đội làm được việc mà không cần tới mình**, nhờ giao diện, tài liệu và rào chắn tốt hơn |
| **Kỹ năng SFIA** | `ARCH` mức 5 · `ITMG` mức 5 |
| **Chế độ hỏng** | Tuyên bố tầm ảnh hưởng nhiều đội từ một danh mục cá nhân, đếm số tài liệu như là kết quả, giấu bất đồng và rủi ro, và không đo mức áp dụng |

Module này **không cấp danh hiệu**. Bậc cao đòi phạm vi, niềm tin và kết quả trong một tổ chức thật, nên phần lớn bằng chứng chỉ tạo ra được khi đi làm.

Cái module dạy được là **bộ hiện vật và tiêu chuẩn chất lượng của chúng**: cách khung một bài toán, cách viết một bản đề xuất có ba phương án thật, cách thiết kế một lần di trú, cách coi nền tảng như một sản phẩm, và cách đo kết quả thay vì đếm tài liệu.

Ranh giới bằng chứng được giữ nghiêm suốt module: **tách rõ cái làm trong lab, cái làm trong dự án cá nhân, và cái có tác động trong sản xuất**; gộp ba thứ này là một dạng nói quá.

### Lesson 431 · The competency ladder and what evidence means `LT`
**Prerequisites.** Module 24: M23

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài mở module bằng ba bậc năng lực và bằng chứng tương ứng của từng bậc. Bậc cao cấp sở hữu kết quả của một hệ có yêu cầu mơ hồ: chia nhỏ, ước lượng, giao hàng đầu cuối, trực và phục hồi; bằng chứng là một dịch vụ hoặc đường dữ liệu được sở hữu cùng một cải thiện đo được về cam kết, chi phí hoặc tính đúng. Bậc tiếp theo dẫn dắt kỹ thuật xuyên đội: nhận ra vấn đề hệ thống, lập bản đồ bên liên quan cùng động cơ cùng phụ thuộc, viết đề xuất, điều phối rà soát và giải quyết bất đồng, dựng kiến trúc đích cùng đường di trú từng bước, và coi nền tảng như sản phẩm. Bậc cao nhất định hướng toàn tổ chức. **Danh hiệu thay đổi theo công ty, còn bằng chứng thì không**: bằng chứng là quyết định, kết quả và mức đòn bẩy. Ranh giới bằng chứng phải giữ nghiêm: lab khác dự án cá nhân, và cả hai khác tác động trong sản xuất.

**Outcome.** Chấm bằng chứng hiện có của mình theo ba bậc và phân tách đúng ba loại bằng chứng.

**Đánh giá.** Tầng *hiểu*. Bài mở module, đặt chuẩn bằng chứng. Kiểm bằng bài tự chấm có rà soát chéo; đạt khi mọi mục bằng chứng được phân đúng ba loại và mỗi tuyên bố có một cách kiểm chứng từ bên ngoài.

**Lab.** Liệt kê mọi bằng chứng hiện có. Phân mỗi mục vào lab, dự án cá nhân, hay tác động trong sản xuất. Với mỗi mục thuộc loại thứ ba, ghi cách một người bên ngoài kiểm chứng được. Chấm theo ba bậc và chỉ ra khoảng trống lớn nhất. Đổi bài chéo: người khác đọc và đánh dấu mọi chỗ nói quá.

**Pitfalls.** Gộp bằng chứng lab với bằng chứng sản xuất · tuyên bố bậc cao từ việc học xong chương trình · đếm dự án thay vì nêu kết quả · không có cách để bên ngoài kiểm chứng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mọi mục bằng chứng phân đúng ba loại, mỗi tuyên bố về sản xuất có cách kiểm chứng từ bên ngoài, và rà soát chéo không tìm thấy chỗ nói quá.

### Lesson 432 · Problem framing on one page `TH`
**Prerequisites.** Lesson 431

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hiện vật đầu tiên và cũng là hiện vật quyết định nhất, vì phần lớn công việc sai hướng bắt đầu từ một bài toán chưa được khung đúng. Một trang gồm sáu phần: hiện trạng có bằng chứng từ sự cố, chi phí, thời gian của đội hoặc trải nghiệm người dùng; ảnh hưởng lượng hoá được; ai chịu ảnh hưởng và ai quyết định; ràng buộc gồm cả ràng buộc về tổ chức; phi mục tiêu; và tiêu chí thành công đo được. **Phần hiện trạng phải có dữ liệu chứ ý kiến**, và đây là phần phân biệt một bài toán thật với một sở thích kỹ thuật. Ba dấu hiệu một bài toán chưa được khung đúng: giải pháp đã có tên trước khi vấn đề được mô tả; không ai đo được nó đang tốn bao nhiêu; và không rõ ai sẽ quyết. Nối với lesson 1: phát biểu bài toán sáu phần áp ở đây với thêm chiều tổ chức.

**Outcome.** Khung ba bài toán thật thành ba trang một, mỗi trang có bằng chứng định lượng cho hiện trạng.

**Đánh giá.** Tầng *áp dụng*. Objective đòi bằng chứng chứ ý kiến. Kiểm bằng rà soát chéo; đạt khi cả ba trang có dữ liệu cho hiện trạng và ảnh hưởng, và mỗi trang nêu rõ người quyết định cùng tiêu chí thành công đo được.

**Lab.** Chọn ba vấn đề thật từ hệ đã dựng hoặc từ nơi làm việc. Với mỗi cái, thu bằng chứng định lượng cho hiện trạng: số sự cố, giờ công, chi phí, hoặc số đo trải nghiệm. Viết một trang đủ sáu phần. Đổi bài chéo và nhờ người khác tìm chỗ nào là ý kiến chứ dữ liệu. Sửa theo phản hồi.

**Pitfalls.** Đặt tên giải pháp trước khi mô tả vấn đề · mô tả hiện trạng bằng cảm nhận · bỏ phi mục tiêu · không nêu ai là người quyết định.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba trang đều có dữ liệu cho hiện trạng và ảnh hưởng, nêu rõ người quyết định, và có tiêu chí thành công đo được.

### Lesson 433 · The RFC with three real options `TH`
**Prerequisites.** Lesson 432

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bản đề xuất kỹ thuật là hiện vật trung tâm của việc dẫn dắt xuyên đội, và chất lượng của nó quyết định quyết định được đưa ra thế nào. Cấu trúc: bài toán cùng bằng chứng, ba phương án thật gồm cả không làm gì, hệ quả lượng hoá theo cùng bộ tiêu chí, khuyến nghị, kế hoạch triển khai, và điều kiện xem lại. Theo đúng lesson 416, **một phương án thật là phương án sẽ thắng trong một bối cảnh nào đó**; bản đề xuất bán sẵn một công cụ là dấu hiệu hỏng rõ nhất và người đọc nhận ra ngay. Quy trình rà soát: gửi bất đồng bộ trước để người đọc có thời gian, họp đồng bộ chỉ để giải quyết bất đồng, và **ghi lại phản đối kể cả phản đối bị bác**, vì đó là thứ cho phép xem lại quyết định về sau. Quyết định phải ghi ai quyết và quyết vào lúc nào. Ba lý do một bản đề xuất tốt vẫn không dẫn tới thay đổi.

**Outcome.** Nộp ba bản đề xuất được rà soát thật, trong đó một bản được triển khai và đo sau khi áp dụng.

**Đánh giá.** Tầng *đánh giá*. Objective đo cả hiện vật, quá trình dẫn tới quyết định, và kết quả sau khi áp dụng. Kiểm bằng ba bản đề xuất cộng số đo sau áp dụng; đạt khi cả ba được rà soát bởi người ngoài, mọi phản đối được ghi kèm cách xử lý, và bản được triển khai có số đo trước và sau.

**Lab.** Từ ba trang khung bài toán ở lesson 432, viết ba bản đề xuất đầy đủ. Gửi mỗi bản cho ít nhất ba người đọc và thu phản hồi bất đồng bộ. Tổ chức một buổi rà soát chỉ để giải quyết bất đồng. Ghi biên bản gồm mọi phản đối, cách xử lý từng phản đối, quyết định và người quyết. **Chọn một bản, triển khai nó, rồi đo kết quả sau khi có người dùng thật**: số đo trước, số đo sau, mức áp dụng, và phần chưa đạt. Viết điều kiện xem lại quyết định cho cả ba.

**Pitfalls.** Dựng phương án rơm · bỏ qua phản đối bị bác · họp trước khi người đọc kịp đọc · không ghi ai là người quyết · **coi bản đề xuất được duyệt là kết quả, trong khi kết quả là số đo sau khi có người dùng**.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba bản đề xuất đều được người ngoài rà soát, mỗi phương án có một bối cảnh mà nó thắng, mọi phản đối được ghi kèm cách xử lý, và bản được triển khai có số đo trước cùng sau khi áp dụng.

### Lesson 434 · Architecture decision records for irreversible choices `TH`
**Prerequisites.** Lesson 433

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bản ghi quyết định kiến trúc là hiện vật rẻ nhất và có giá trị lâu nhất, vì nó giữ lại bối cảnh mà tài liệu kiến trúc không giữ. Mỗi bản ghi gồm: bối cảnh lúc quyết, quyết định, phương án đã cân nhắc, hệ quả cả tốt lẫn xấu, và điều kiện xem lại. Chỉ viết cho quyết định khó đảo ngược theo phân loại ở lesson 416; viết cho mọi thứ làm bộ hồ sơ loãng và không ai đọc. **Giá trị lớn nhất của bản ghi là khi có người hỏi vì sao hồi đó lại chọn thế**, thường sau nhiều năm và người quyết đã đi; không có nó thì đội sau hoặc giữ một quyết định đã hết lý do, hoặc phá một quyết định vẫn còn lý do. Hệ quả xấu phải viết thật: một bản ghi chỉ liệt kê ưu điểm là một bản quảng cáo. Bản ghi bất biến: quyết định đổi thì viết bản mới và đánh dấu bản cũ đã bị thay thế, chứ sửa bản cũ.

**Outcome.** Viết ba bản ghi cho ba quyết định khó đảo ngược, mỗi bản có hệ quả xấu và điều kiện xem lại.

**Đánh giá.** Tầng *áp dụng*. Objective đòi trung thực về hệ quả xấu. Kiểm bằng rà soát chéo; đạt khi cả ba bản có ít nhất hai hệ quả xấu cụ thể và điều kiện xem lại kiểm được, và không bản nào viết cho quyết định dễ đảo.

**Lab.** Chọn ba quyết định khó đảo ngược trong hệ đã dựng. Viết bản ghi cho từng cái. Với mỗi bản, liệt kê ít nhất hai hệ quả xấu cụ thể và một điều kiện xem lại có thể kiểm bằng số đo. Đưa cho một người chưa tham gia quyết định và hỏi họ có hiểu vì sao chọn vậy không. Thay thế một bản ghi cũ và giữ bản cũ.

**Pitfalls.** Viết bản ghi cho mọi quyết định · chỉ liệt kê ưu điểm · sửa bản ghi cũ khi quyết định đổi · viết điều kiện xem lại mơ hồ không kiểm được.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba bản ghi có ≥ 2 hệ quả xấu cụ thể và điều kiện xem lại kiểm được bằng số đo, và người chưa tham gia hiểu được lý do chọn.

### Lesson 435 · Migration playbook with consumer inventory `TH`
**Prerequisites.** Lesson 434

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Di trú là nơi phần lớn sáng kiến kỹ thuật chết, nên nó có một sổ tay riêng. Năm phần: kiểm kê bên tiêu thụ với chủ sở hữu và mức dùng thật; ma trận tương thích cho từng nhóm bên tiêu thụ; chạy song song có tiêu chí đối soát theo lesson 417; chuyển đổi theo từng phần với đường quay lui; và khai tử có thời hạn cùng theo dõi mức dùng còn lại. **Kiểm kê phải dựa trên dữ liệu sử dụng thật chứ trên trí nhớ**, vì bên tiêu thụ luôn nhiều hơn người ta nghĩ, và những bên không ai nhớ chính là những bên sẽ hỏng. Hỗ trợ bên tiêu thụ là một phần của kế hoạch chứ một việc phát sinh: đường dẫn mẫu, công cụ chuyển đổi, tài liệu, và thời gian của người. Chế độ hỏng đặc trưng về tổ chức: di trú làm quá tải đội dùng, nên họ hoãn, nên hệ cũ sống mãi và ta phải nuôi hai hệ.

**Outcome.** Lập sổ tay di trú năm phần có kiểm kê từ dữ liệu thật và kế hoạch hỗ trợ bên tiêu thụ.

**Đánh giá.** Tầng *áp dụng*. Objective gồm cả chiều tổ chức chứ chỉ kỹ thuật. Kiểm bằng rà soát sổ tay; đạt khi kiểm kê dựa trên dữ liệu sử dụng thật, mọi nhóm bên tiêu thụ có đường chuyển đổi cùng chủ sở hữu, và kế hoạch có ước lượng thời gian của đội dùng.

**Lab.** Chọn một thay đổi cần di trú. Lập kiểm kê bên tiêu thụ từ nhật ký truy vấn cùng khai báo theo lesson 265. So với danh sách từ trí nhớ và ghi chênh lệch. Lập ma trận tương thích theo nhóm. Thiết kế chạy song song và chuyển đổi từng phần. Ước lượng thời gian mà mỗi đội dùng phải bỏ ra và lập kế hoạch hỗ trợ. Đặt thời hạn khai tử và cách theo dõi mức dùng còn lại.

**Pitfalls.** Kiểm kê bằng trí nhớ · chuyển đổi toàn bộ một lần · không tính thời gian của đội dùng · gỡ hệ cũ theo lịch thay vì theo mức dùng còn lại.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Kiểm kê dựa trên dữ liệu sử dụng thật với chênh lệch so với trí nhớ được ghi, mọi nhóm có đường chuyển đổi cùng chủ sở hữu, và kế hoạch có ước lượng thời gian đội dùng.

### Lesson 436 · Platform as product - paved road, guardrails, adoption `TH`
**Prerequisites.** Lesson 435

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Nền tảng nội bộ hỏng theo một cách đặc trưng: đúng về kỹ thuật mà không ai dùng. Coi nó như sản phẩm nghĩa là áp lại M11C cho người dùng nội bộ: hành trình người dùng, khả năng tìm thấy, tài liệu, và số đo mức dùng thật. Ba cơ chế: đường dẫn mẫu tức cách làm mặc định đã được bảo đảm sẵn về bảo mật và vận hành; rào chắn tức chốt kiểm soát tự động thay cho việc phê duyệt thủ công; và tự phục vụ để đội nền tảng không thành nút cổ chai. **Rào chắn tốt hơn phê duyệt vì nó mở rộng được và vì nó không phụ thuộc vào một người**; mỗi lần phải xin phép là một lần mất thời gian của cả hai bên. Đo mức áp dụng bằng chỉ số hợp lệ theo lesson 197: tỉ lệ đội dùng đường dẫn mẫu, thời gian tới thay đổi đầu tiên chạy được ở sản xuất, và tỉ lệ việc làm được không cần mở phiếu; số phiếu đã đóng không phải chỉ số.

**Outcome.** Dựng đường dẫn mẫu có rào chắn và chứng minh **hai kỹ sư hoặc hai đội** đưa được thay đổi lên sản xuất mà không cần tới mình.

**Đánh giá.** Tầng *đánh giá*. Objective đo bằng hành vi người dùng nội bộ chứ bằng tính năng đã xây. Kiểm bằng phép thử người; đạt khi **hai người thuộc hai đội khác nhau** đều đưa được thay đổi đầu tiên lên sản xuất trong giới hạn thời gian mà không hỏi mình, và ít nhất ba rào chắn thay được phê duyệt thủ công.

**Lab.** Chọn một quy trình mà đội dùng hay phải xin phê duyệt. Dựng đường dẫn mẫu gồm khuôn mẫu, tài liệu và ví dụ chạy được. Thay ít nhất ba điểm phê duyệt thủ công bằng rào chắn tự động. Nhờ hai người thuộc hai đội khác nhau dùng đường dẫn mẫu và bấm giờ tới thay đổi đầu tiên chạy được; đếm số lần họ phải hỏi mình. Đo ba chỉ số mức áp dụng và ghi mọi chỗ họ vấp; mỗi lần phải hỏi là một thiếu sót của tài liệu hoặc của rào chắn, sửa rồi đo lại với người thứ hai.

**Pitfalls.** Xây nền tảng rồi chờ người ta tới · đo bằng số phiếu đã đóng · giữ phê duyệt thủ công vì an tâm hơn · không có ví dụ chạy được trong tài liệu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Hai người thuộc hai đội khác nhau đều đưa được thay đổi đầu tiên lên sản xuất trong giới hạn thời gian mà không hỏi mình, ≥ 3 điểm phê duyệt được thay bằng rào chắn, và ba chỉ số mức áp dụng có số đo.

### Lesson 437 · Strategy memo - diagnosis, bets, sequence, revisit signals `TH`
**Prerequisites.** Lesson 436

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hiện vật của bậc cao nhất, và nó khác một bản đề xuất ở chỗ nó nói về nhiều năm và nhiều hệ. Năm phần: bối cảnh, chẩn đoán tức nêu đúng vấn đề cốt lõi chứ liệt kê triệu chứng, nguyên tắc dùng để ra quyết định về sau, các cược tức những chỗ chọn đầu tư và chấp nhận rủi ro, trình tự tức làm gì trước và vì sao, số đo, và rủi ro. **Chiến lược là một tập lựa chọn, nên một bản chiến lược không nói mình sẽ không làm gì thì chưa phải chiến lược**; đó là phép thử nhanh nhất để nhận ra một bản tầm nhìn đội lốt. Tín hiệu xem lại phải viết ra cùng lúc: điều gì xảy ra thì chiến lược này không còn đúng, và ai được quyền khởi động việc xem lại. Chi phí chìm là cái bẫy đặc trưng: chiến lược đã sai vì thị trường hoặc tổ chức đổi mà vẫn tiếp tục vì đã bỏ nhiều công vào.

**Outcome.** Viết một bản chiến lược có chẩn đoán, có phần không làm, và có tín hiệu xem lại cùng người khởi động.

**Đánh giá.** Tầng *đánh giá*. Objective đòi lựa chọn chứ mong muốn. Kiểm bằng rà soát chéo; đạt khi bản chiến lược nêu rõ ít nhất ba việc sẽ không làm, chẩn đoán chỉ ra vấn đề cốt lõi chứ triệu chứng, và tín hiệu xem lại kiểm được kèm người có quyền khởi động.

**Lab.** Chọn một phạm vi nhiều hệ. Viết bản chiến lược đủ năm phần. Trong phần các cược, nêu ít nhất ba việc sẽ không làm và lý do. Với mỗi cược, viết một tín hiệu cho biết nó sai kèm cách đo. Ghi ai được quyền khởi động việc xem lại. Đổi bài chéo và nhờ người khác tìm chỗ nào là tầm nhìn chứ lựa chọn.

**Pitfalls.** Viết tầm nhìn mà không có lựa chọn · liệt kê triệu chứng thay vì chẩn đoán · không nêu việc sẽ không làm · tín hiệu xem lại mơ hồ không đo được.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bản chiến lược nêu ≥ 3 việc sẽ không làm, chẩn đoán chỉ ra vấn đề cốt lõi, và mỗi cược có tín hiệu xem lại đo được cùng người khởi động.

### Lesson 438 · Influence, review and the bottleneck anti-pattern `LT`
**Prerequisites.** Lesson 437

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài về phần mà hiện vật không làm thay được. Ảnh hưởng không có thẩm quyền dựa trên ba thứ: bằng chứng, việc hiểu động cơ của người khác, và độ tin cậy tích luỹ từ những lần dự đoán đúng. Bất đồng nên được nêu ra chứ tránh; **giấu bất đồng và rủi ro làm quyết định trông đồng thuận rồi vỡ khi triển khai**. Hệ thống rà soát thiết kế cần thiết kế có chủ ý: ai rà cái gì, rà để làm gì, và làm sao rà soát không thành một cửa phê duyệt. Ba mẫu hỏng đặc trưng của bậc cao: trở thành nút cổ chai vì mọi thứ phải qua mình; giữ bối cảnh cho riêng mình nên đội không tự quyết được; và đi giải cứu các đội thay vì làm cho họ tự làm được. **Phép thử của mức đòn bẩy: sau khi mình rời đi, hai đội có tiếp tục làm đúng không**, nhờ giao diện, tài liệu và rào chắn tốt hơn chứ nhờ trí nhớ của ai đó.

**Outcome.** Nhận ra ba mẫu hỏng trong tình huống thật và thiết kế một hệ thống rà soát không thành cửa phê duyệt.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết chuẩn bị cho bài hồ sơ bằng chứng. Kiểm bằng bài phân tích ba tình huống cộng một thiết kế; đạt khi nhận đúng mẫu hỏng ở ít nhất hai tình huống và hệ thống rà soát nêu rõ cách nó không thành nút cổ chai.

**Lab.** Cho ba tình huống về một người dẫn dắt kỹ thuật; nhận ra mẫu hỏng trong từng cái và đề xuất cách đổi. Thiết kế một hệ thống rà soát thiết kế cho một tổ chức giả định: ai rà cái gì, tiêu chí nào cần rà và tiêu chí nào để rào chắn tự động lo. Áp phép thử mức đòn bẩy vào công việc của chính mình và chỉ ra chỗ mình đang là nút cổ chai.

**Pitfalls.** Coi mọi thứ phải qua mình là trách nhiệm · giấu bất đồng để họp trôi chảy · giải cứu đội khác thay vì cải thiện giao diện · đo ảnh hưởng bằng số buổi rà soát đã tham gia.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Nhận đúng mẫu hỏng ở ≥ 2/3 tình huống, hệ thống rà soát nêu rõ cách tránh thành nút cổ chai, và phép thử mức đòn bẩy được áp vào công việc của chính mình.

### Lesson 439 · The evidence dossier - baseline, decision, outcome, limits `TH`
**Prerequisites.** Lesson 438

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài gom toàn bộ hiện vật thành một hồ sơ bằng chứng dùng được khi ứng tuyển hoặc khi đề nghị thăng cấp. Ba sáng kiến trong hồ sơ không được chọn tuỳ ý: hợp đồng nguồn chỉ định hai loại bắt buộc, vì chúng là hai loại bằng chứng khó nguỵ tạo nhất. **Một là cắt chi phí hoặc cải thiện một cam kết dịch vụ có số đo**, kèm đánh đổi đã chấp nhận, vì nó buộc phải có đường cơ sở trước khi làm. **Hai là dẫn một buổi diễn tập sự cố và một phân tích sau sự cố xuyên ít nhất hai thành phần thuộc hai đội**, kèm bằng chứng hành động sau đó làm giảm tái diễn, vì nó buộc phải phối hợp ngoài phạm vi của mình. Sáng kiến thứ ba tự chọn. Mỗi mục có năm phần: đường cơ sở trước khi làm, quyết định cùng lý do, việc triển khai cùng mức áp dụng, kết quả đo được, và **giới hạn của lập luận nhân quả**; phần cuối là phần hiếm ai viết và là phần làm hồ sơ đáng tin: kết quả tốt có thể do nhiều nguyên nhân, và nói rõ điều đó mạnh hơn là tuyên bố chắc chắn. Ranh giới bằng chứng giữ nghiêm theo lesson 431. Cùng một sáng kiến trình bày cho ba nhóm người khác nhau: ban lãnh đạo cần phương án, mức rủi ro và kinh tế; kỹ sư cần đánh đổi kỹ thuật; người vận hành cần thay đổi trong công việc hằng ngày. **Ba bản trình bày khác về chi tiết nhưng không được khác về sự thật**, và đây là ranh giới đạo đức của bài.

**Outcome.** Lập hồ sơ năm phần cho ba sáng kiến, trong đó bắt buộc có một sáng kiến về chi phí hoặc cam kết dịch vụ và một buổi diễn tập xuyên hai thành phần, rồi trình bày một sáng kiến cho ba nhóm người.

**Đánh giá.** Tầng *đánh giá*. Objective đòi trung thực về giới hạn nhân quả. Kiểm bằng rà soát hồ sơ cộng ba lần trình bày; đạt khi hai loại sáng kiến bắt buộc đều có mặt kèm số đo trước và sau, mọi mục có giới hạn nhân quả nêu rõ, và ba bản trình bày nhất quán về sự thật khi đối chiếu.

**Lab.** Thực hiện sáng kiến bắt buộc thứ nhất: đo đường cơ sở, cắt chi phí hoặc cải thiện một cam kết dịch vụ, đo lại, và báo cáo đánh đổi đã chấp nhận. Thực hiện sáng kiến bắt buộc thứ hai: dẫn một buổi diễn tập sự cố xuyên hai thành phần thuộc hai đội, viết phân tích sau sự cố, rồi theo dõi xem hành động có làm giảm tái diễn không. Lập hồ sơ cho ba sáng kiến, mỗi cái đủ năm phần. Với mỗi kết quả, nêu ít nhất hai cách giải thích khác. Chọn một sáng kiến và chuẩn bị ba bản trình bày: mười phút cho ban lãnh đạo, sáu mươi phút cho kỹ sư, và một bản hướng dẫn cho người vận hành. Trình bày cả ba và nhờ người nghe đối chiếu xem có mâu thuẫn không.

**Pitfalls.** Tuyên bố nhân quả từ một tương quan · **đo sau khi làm mà không có đường cơ sở trước khi làm** · diễn tập trong phạm vi một đội rồi gọi là xuyên đội · giấu phần không thành công · đổi sự thật khi đổi người nghe · gộp bằng chứng lab vào phần kết quả sản xuất.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Hai loại sáng kiến bắt buộc đều có mặt với số đo trước và sau, mọi mục có giới hạn nhân quả nêu rõ cùng ít nhất hai cách giải thích khác, và ba bản trình bày được đối chiếu không có mâu thuẫn về sự thật.

### Lesson 440 · Graduation defence - one design, three audiences `KT`
**Prerequisites.** Lesson 439

**In-class (180 phút).** 135 phút làm bài độc lập · 45 phút chữa bài và phân tích lỗi theo nhóm

**Learn.** Bài bảo vệ tốt nghiệp của toàn chương trình. Không có nội dung mới; nó kiểm năng lực tổng hợp trên chính hồ sơ thiết kế đã làm ở lesson 420 cùng hồ sơ bằng chứng ở lesson 439.

**Outcome.** Bảo vệ một thiết kế đầu cuối trước ba nhóm người nghe, chịu được bốn ràng buộc đổi, và phân tách trung thực ba loại bằng chứng.

**Đánh giá.** Tầng *đánh giá*. Bài bảo vệ cuối cùng, đo năng lực thiết kế, năng lực truyền đạt và tính trung thực về bằng chứng.

**Lab.** Buổi 180 phút: 135 phút bảo vệ và chất vấn, 45 phút hội đồng nghị án và phản hồi. Hội đồng ba người. Bài chấm sáu phần: A (20đ) trình bày hồ sơ thiết kế, mọi thành phần truy được về một yêu cầu hoặc bảo đảm · B (20đ) bảo vệ bảng năng lực và bảng chế độ hỏng, chỉ ra nút thắt đầu tiên cùng hệ quả với dữ liệu · C (20đ) bốn ràng buộc đổi do hội đồng đưa ra; điều chỉnh đúng phần bị ảnh hưởng kèm chi phí · D (15đ) trình kế hoạch di trú có kiểm kê bên tiêu thụ, chạy song song và quay lui · E (15đ) cùng một sáng kiến trình bày mười phút cho ban lãnh đạo và mười phút cho người vận hành; hội đồng đối chiếu tính nhất quán · F (10đ) hồ sơ bằng chứng, phân tách ba loại và nêu giới hạn nhân quả.

**Pitfalls.** Bảo vệ quyết định cũ vì đã bỏ công vào nó · đổi sự thật khi đổi người nghe · tuyên bố tác động sản xuất từ bằng chứng lab · trình thiết kế có thành phần không gắn với yêu cầu nào.

**Self-study (2,4 giờ).** Không có bài tự học. Nếu không đạt, theo phụ lục khắc phục khi không đạt cổng

**Done when.** Đạt ≥ 70/100, phần A và C đều ≥ 60%. Hai bản trình bày ở phần E mâu thuẫn về sự thật thì phần đó bằng không; gộp bằng chứng lab vào phần tác động sản xuất thì phần F bằng không.


---

# PHỤ LỤC — TRẠNG THÁI BẢN NHÁP

| Hạng mục | Trạng thái |
|---|---|
| Bản đồ 29 module | Xong |
| Đặc tả bài | Xong 440/440 |
| Đồ thị phụ thuộc trong module | Chưa |
| Bộ dữ liệu và môi trường lab | Chưa |
| Đề các cổng có rubric | Thang điểm đã có trong đặc tả bài; chưa soạn đề |
| Gỡ chương trình Analytics Engineer khỏi `material/` | Chưa · cần bản chốt mới |
