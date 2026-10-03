---
chuong_trinh: Data Engineer
ma: DE
phien_ban: "5.0-draft"
trang_thai: draft
cap_do_dau_ra: Junior — Senior
so_bai: 422
cap_nhat: 2026-09-21
---

# CHƯƠNG TRÌNH DATA ENGINEER — BẢN NHÁP

> **Bản nháp để rà soát, không phải roadmap chính thức.**
> Roadmap chính thức vẫn là `material/data-engineer/roadmap/roadmap.md` (bản cũ, 102 bài).
> Bản này chứa **422/422 bài**, tức module M1 tới M40: đặc tả đã đủ 40 module.

**422 bài · 40 module · 844 giờ trên lớp · không yêu cầu kiến thức đầu vào**

| | |
|---|---|
| **Vị trí đầu ra** | Data Engineer · Platform Engineer · Data Architect (đích mở rộng) |
| **Cấp độ đạt được** | Junior vững tới Senior; Staff và Principal cần kinh nghiệm thực tế ngoài chương trình |
| **Điều kiện đầu vào** | Không. Giả định chưa biết lập trình |
| **Thời lượng** | 422 bài × 2 giờ trên lớp = 844 giờ · cộng tự học 2,4 giờ mỗi bài = 1012 giờ · tổng ~1856 giờ |
| **Nhịp học** | 12 giờ/tuần → ~34 tháng · 15 giờ/tuần → ~27 tháng |
| **Nguồn thiết kế** | `ROADMAP_DATA_ENGINEER_0_TO_ARCHITECT.md` (9 chặng) và `List học.md` (22 level) |
| **Ánh xạ khung năng lực** | SFIA 9 (2024): `DTAN`, `PROG`, `SYSP`, `NTAS`, `HPCC`, `DATM`, `TEST`, `CFMG`, `DBAD`, `ARCH` |

---

## 1. Bản đồ 40 module

| Chặng | Module | Tên | Mức | Bài |
|---|---|---|---|---:|
| 0 | **M1** | Introduction to the Data Engineer Role and the Learning System |  | 5 |
| 1 | **M2** | Computers - CPU, memory, storage and the cost of a computation |  | 12 |
| 1 | **M3** | Operating systems and Linux |  | 12 |
| 1 | **M4** | Networking for data engineers |  | 10 |
| 1 | **M5** | Algorithms and data structures for data work |  | 10 |
| 1 | **M6** | Concurrency, parallelism and correctness under contention |  | 12 |
| 2 | **M7** | Python for data engineering |  | 16 |
| 2 | **M8** | Software engineering - Git, testing, packaging, APIs |  | 14 |
| 3 | **M9** | SQL from zero to advanced |  | 16 |
| 3 | **M10** | The life of a query - database internals |  | 14 |
| 3 | **M11** | PostgreSQL | `A` | 14 |
| 3 | **M12** | MySQL | `B` | 8 |
| 3 | **M13** | MongoDB | `B` | 8 |
| 3 | **M14** | Redis | `B` | 7 |
| 3 | **M15** | BigQuery | `B` | 8 |
| 3 | **M16** | ClickHouse | `B` | 8 |
| 3 | **M17** | Elasticsearch | `B` | 8 |
| 3 | **M18** | Choosing a database - polyglot design and defence |  | 6 |
| 4 | **M19** | Data modeling and warehousing |  | 14 |
| 4 | **M20** | Batch ingestion, accuracy and data quality |  | 16 |
| 5 | **M21** | Orchestration foundations - DAG, state, schedule, backfill |  | 6 |
| 5 | **M22** | Apache Airflow | `A` | 12 |
| 5 | **M23** | Dagster | `A` | 12 |
| 5 | **M24** | Prefect | `A` | 12 |
| 5 | **M25** | Choosing an orchestrator - the evidence matrix (Kestra `C` ở đây) |  | 6 |
| 5 | **M26** | Data contracts and dataset handover |  | 10 |
| 6 | **M27** | Messaging foundations - delivery semantics, ordering, DLQ, replay |  | 6 |
| 6 | **M28** | RabbitMQ | `B` | 8 |
| 6 | **M29** | Apache Kafka | `A` | 14 |
| 6 | **M30** | Choosing a message system - queue against log |  | 4 |
| 6 | **M31** | Change data capture with Debezium | `B` | 8 |
| 6 | **M32** | Stream processing - Spark Structured Streaming and Flink | `A`/`B` | 12 |
| 7 | **M33** | Storage, file formats and the lakehouse |  | 14 |
| 7 | **M34** | Spark and distributed processing | `A` | 14 |
| 7 | **M35** | Docker | `A` | 8 |
| 7 | **M36** | Kubernetes | `B` | 10 |
| 7 | **M37** | Cloud and infrastructure as code | `A`+`B` | 12 |
| 7 | **M38** | Operations, observability, security and cost |  | 14 |
| 8 | **M39** | System design and distributed systems |  | 16 |
| 9 | **M40** | Capstone - build and defend a data platform |  | 6 |

Cổng kiểm tra đã đặc tả: lesson 5 · lesson 29 · lesson 61 · lesson 91 · lesson 188 · lesson 218 · lesson 266 · lesson 276 · lesson 308 · lesson 328 · lesson 400 · lesson 416 · lesson 422.

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

**Thang Bloom.** Sáu tầng dùng trong trường `Đánh giá`: *nhớ*, *hiểu*, *áp dụng*, *phân tích*, *đánh giá*, *sáng tạo*. Tầng quyết định hình thức kiểm hợp lệ; một objective tầng *áp dụng* không kiểm được bằng câu hỏi nhiều lựa chọn.

---

# MODULE 1 · INTRODUCTION TO THE DATA ENGINEER ROLE AND THE LEARNING SYSTEM

**Lessons 1–5 · 10 giờ**

| | |
|---|---|
| **Objective cấp module** | Vẽ được đường đi của một bản ghi từ hệ thống nguồn tới bảng điều khiển, và chỉ ra năm chỗ nó hỏng được cùng phép đo phát hiện từng chỗ |
| **Tiền đề** | Không |
| **Exit criterion** | Giải thích đường đi đó cho một người mới trong 5 phút, và trả lời được vì sao phải có chất lượng, quyền sở hữu, giám sát và bảo mật |
| **Kỹ năng SFIA** | `DTAN` mức 2 |
| **Chế độ hỏng** | Coi đây là module dẫn nhập rồi học lướt, nên tới chặng 4 không phát biểu được hợp đồng của một pipeline |

Module không cài công cụ nào. Nó dựng bản đồ để 417 bài sau có chỗ neo, và dựng hệ thống ghi chép mà cả chương trình dựa vào. Bốn bài đầu đi từ ranh giới nghề tới cách học; bài cuối là cổng 0.

### Lesson 1 · What a Data Engineer does and where the boundary sits `LT`
**Prerequisites.** Module 1: Không

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Sáu vai trò trong tổ chức dữ liệu và ranh giới trách nhiệm: Data Engineer, Analytics Engineer, Data Analyst, Data Scientist, Platform Engineer, Data Architect. Ba vùng chồng lấn hay gây tranh chấp phạm vi và cách các tổ chức thật chia chúng: ai sở hữu bảng thô, ai sở hữu bảng phục vụ, ai sở hữu định nghĩa chỉ số. Sản phẩm bàn giao của Data Engineer là một tập dữ liệu có hợp đồng, không phải một bảng điều khiển. Ba loại tổ chức tuyển Data Engineer và khác biệt về nội dung công việc: công ty sản phẩm có dữ liệu sự kiện lớn, doanh nghiệp truyền thống có nhiều hệ thống giao dịch cũ, và công ty dịch vụ làm dự án cho khách. Phân bổ thời gian thực tế của nghề theo bản nguồn: phần lớn thời gian nằm ở làm cho pipeline chạy đúng lại sau khi hỏng, không nằm ở viết pipeline mới.

**Outcome.** Phân định trách nhiệm của sáu vai trò cho một danh sách nhiệm vụ cho trước, và định vị khoảng cách giữa năng lực hiện có của bản thân và ma trận năng lực ở mục 4.

**Đánh giá.** Tầng *hiểu*. Bài mở chương trình, người học chưa có dữ liệu để thao tác, nên objective dừng ở phân định và giải thích. Kiểm bằng bài gán 18 nhiệm vụ cho sáu vai trò kèm một câu lý do mỗi nhiệm vụ; chấm theo bảng ranh giới ở phụ lục, đạt khi đúng ≥ 14/18 và lý do không mâu thuẫn với bảng.

**Lab.** Đọc 10 tin tuyển dụng Data Engineer đang mở tại Việt Nam trên ITViec hoặc TopDev. Lập bảng tần suất công nghệ: mỗi công nghệ xuất hiện trong bao nhiêu tin. Đối chiếu với bản đồ 40 module ở mục 9 và chỉ ra công nghệ nào chương trình không phủ, công nghệ nào chương trình phủ mà tin không nhắc.

**Pitfalls.** Quy vai trò Data Engineer về viết pipeline · giả định thành thạo công cụ là điều kiện đủ · bỏ qua phần vận hành vì nó không có trong tiêu đề tin tuyển dụng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Nộp bảng tần suất từ 10 tin có ghi nguồn và ngày truy cập, và bài gán nhiệm vụ đạt ≥ 14/18.

### Lesson 2 · The path of one record - source to dashboard `LT`
**Prerequisites.** Lesson 1

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bảy chặng của một bản ghi: sự kiện nghiệp vụ, hệ thống nguồn, thu thập, lưu trữ thô, biến đổi, lớp phục vụ, và ứng dụng tiêu thụ. Với mỗi chặng, cơ chế mất mát, cơ chế nhân bản, và cơ chế diễn giải sai đặc trưng của chặng đó. Phân biệt ba cặp khái niệm mà người mới hay gộp: ETL với ELT theo chỗ đặt phép biến đổi, theo lô với theo luồng theo đơn vị xử lý chứ không theo tốc độ, và hệ thống giao dịch với hệ thống phân tích theo mẫu truy cập. Ba lớp dữ liệu thường gặp và trách nhiệm của từng lớp: thô giữ nguyên như nguồn để tái tạo được, lớp giữa làm sạch và chuẩn hoá, lớp phục vụ hướng người dùng. Vì sao một con số trên bảng điều khiển là kết quả của một chuỗi quyết định thiết kế, không phải một quan sát trực tiếp.

**Outcome.** Tái dựng đường đi bảy chặng từ trí nhớ và chỉ ra ít nhất một cơ chế sai lệch cụ thể tại mỗi chặng.

**Đánh giá.** Tầng *hiểu*. Objective là tái dựng và giải thích cơ chế, chưa thao tác trên hệ thống nào. Kiểm bằng bài vẽ lại sơ đồ và điền cơ chế sai lệch; đạt khi đủ bảy chặng và ít nhất năm chặng có cơ chế đúng, chấm theo bảng đối chiếu.

**Lab.** Vẽ đường đi của một đơn hàng từ lúc khách bấm đặt tới lúc con số doanh thu hiện trên bảng điều khiển. Nêu 5 nơi dữ liệu có thể sai và với mỗi nơi, một phép đo phát hiện được nó. Đổi bài với một học viên khác và tìm chặng người kia bỏ sót.

**Pitfalls.** Vẽ đường đi tuyến tính mà bỏ qua chỗ dữ liệu bị ghi lại nhiều lần · nhầm theo luồng với nhanh · cho rằng lớp thô là bản sao y hệt nguồn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Sơ đồ đủ bảy chặng, ít nhất năm chặng có cơ chế sai lệch đúng, và 5 phép đo phát hiện đều thực hiện được.

### Lesson 3 · Declaring a use case - owner, grain, consumer, freshness `TH`
**Prerequisites.** Lesson 2

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Chín thuộc tính phải khai báo trước khi xây bất cứ thứ gì: chủ dữ liệu, hệ thống nguồn, hạt dữ liệu, người tiêu thụ, độ tươi yêu cầu, mức đúng đắn yêu cầu, quyền truy cập, thời gian lưu giữ, và người chịu trách nhiệm khi hỏng. Hạt dữ liệu là thuộc tính chặn: phát biểu bằng một câu có dạng một dòng là một gì, và kiểm chứng bằng phép đếm. Phân biệt độ tươi với độ trễ và với tần suất chạy, ba thứ hay bị gộp. Mức đúng đắn phát biểu được bằng ngưỡng chứ không bằng tính từ: sai lệch cho phép là bao nhiêu phần trăm, đo bằng cách nào, đối chiếu với nguồn nào. Thủ tục từ chối một yêu cầu không trả lời được bằng dữ liệu hiện có, và vì sao từ chối sớm rẻ hơn xây rồi bỏ. Ba use case mẫu dùng xuyên suốt chương trình: đơn hàng, thanh toán, tồn kho.

**Outcome.** Viết bản khai báo đủ chín thuộc tính cho một yêu cầu phát biểu mơ hồ, sao cho người thứ hai triển khai được không cần hỏi lại.

**Đánh giá.** Tầng *áp dụng*. Sản phẩm là một tài liệu có tiêu chí kiểm được. Kiểm bằng rà soát chéo: một học viên khác đọc bản khai báo và viết ra hiểu biết của mình về hạt và người tiêu thụ; đạt khi hai bên khớp và không có câu hỏi làm rõ nào phát sinh.

**Lab.** Nhận ba yêu cầu phát biểu mơ hồ cho ba use case mẫu. Viết ba bản khai báo đủ chín thuộc tính. Đổi bài chéo, người nhận viết lại hạt và người tiêu thụ theo cách mình hiểu. Mọi chênh lệch phải sửa vào bản khai báo.

**Pitfalls.** Phát biểu hạt bằng tên bảng thay vì bằng một câu · để mức đúng đắn ở dạng tính từ · bỏ trống người chịu trách nhiệm khi hỏng vì chưa có ai.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba bản khai báo đạt rà soát chéo, không phát sinh câu hỏi làm rõ nào.

### Lesson 4 · How to learn this - evidence, recall and a knowledge repo `TH`
**Prerequisites.** Lesson 3

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Chương trình dài hơn hai năm, nên cách ghi chép quyết định phần lớn kết quả. Cấu trúc kho kiến thức sáu thư mục và việc của từng thư mục: khái niệm, lab, dự án, quyết định kiến trúc, sổ tay xử lý, và rà soát. Khuôn một ghi chú chín phần theo bản nguồn: định nghĩa, vấn đề nó giải, cơ chế bên trong, đường đi của một yêu cầu hoặc một bản ghi, lựa chọn và đánh đổi, lỗi thường gặp, cách quan sát, lab, câu hỏi kiểm tra. Bốn câu tự hỏi sau mỗi khái niệm: nó tồn tại để làm gì, nó sai theo cách nào, làm sao biết nó sai, khi nào dùng thứ khác. Ôn lại sau 1, 7 và 30 ngày. Thang sáu mức theo dõi năng lực: chưa học, giải thích được, làm theo hướng dẫn, tự làm, xử lý ca lạ, áp dụng thực tế. Nguyên tắc không suy ra mức thành thạo từ việc đã đọc: mỗi mức phải có bằng chứng kèm ngày. Cảnh báo từ bản nguồn: không tạo 150 kho rỗng.

**Outcome.** Dựng kho kiến thức sáu thư mục và viết một ghi chú chín phần hoàn chỉnh cho một khái niệm đã học ở lesson 2 hoặc 3.

**Đánh giá.** Tầng *áp dụng*. Objective là một sản phẩm có khuôn kiểm được. Kiểm bằng rà soát: ghi chú phải đủ chín phần, phần đường đi phải có một ví dụ cụ thể, và phần lab phải chạy lại được bởi người khác. Ghi chú đủ chín tiêu đề nhưng phần cơ chế chỉ chép lại định nghĩa thì không đạt.

**Lab.** Dựng kho kiến thức sáu thư mục có quản lý phiên bản. Viết một ghi chú chín phần cho khái niệm hạt dữ liệu hoặc đường đi bảy chặng. Lập bảng theo dõi năng lực sáu mức cho 40 module, đánh dấu mức hiện tại và để trống cột bằng chứng.

**Pitfalls.** Tạo cấu trúc thư mục rỗng rồi không viết gì · chép định nghĩa vào phần cơ chế · đánh dấu đã hiểu mà không có bằng chứng kèm ngày.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Kho có đủ sáu thư mục, một ghi chú chín phần đạt rà soát, và bảng theo dõi năng lực có cột bằng chứng.

### Lesson 5 · Gate 0 - explain the data path and defend the four disciplines `KT`
**Prerequisites.** Lesson 4

**In-class (120 phút).** 75 phút làm bài độc lập · 45 phút chữa bài và phân tích lỗi theo nhóm

**Learn.** Không có nội dung mới. Cổng 0 của chương trình.

**Outcome.** Giải thích đường đi của dữ liệu cho một người không làm kỹ thuật trong 5 phút, và bảo vệ được vì sao cần chất lượng, quyền sở hữu, giám sát và bảo mật, bằng hậu quả cụ thể chứ bằng nguyên tắc chung.

**Đánh giá.** Tầng *đánh giá*. Cổng đo năng lực giải thích và bảo vệ, không đo trí nhớ, nên không kiểm bằng đề trắc nghiệm. Thang điểm: A 25đ đường đi bảy chặng · B 20đ năm chỗ hỏng và phép đo · C 20đ bốn kỷ luật, mỗi kỷ luật một hậu quả cụ thể khi thiếu · D 15đ bản khai báo use case · E 20đ trả lời chất vấn. Đạt khi ≥ 70/100 và phần E ≥ 50%.

**Lab.** Trình bày 5 phút cho một người đóng vai quản lý không làm kỹ thuật, hỏi đáp 10 phút. Người nghe được phép hỏi vì sao không làm đơn giản hơn ở bất kỳ chặng nào.

**Pitfalls.** Dùng thuật ngữ mà người nghe không có · bảo vệ bốn kỷ luật bằng nguyên tắc chung thay vì bằng hậu quả · không trả lời được câu vì sao không làm đơn giản hơn.

**Self-study (2,4 giờ).** Không có bài tự học. Nếu không đạt, theo phụ lục khắc phục khi không đạt cổng

**Done when.** Đạt ≥ 70/100 và phần E ≥ 50%.

# MODULE 2 · COMPUTERS - CPU, MEMORY, STORAGE AND THE COST OF A COMPUTATION

**Lessons 6–17 · 24 giờ**

| | |
|---|---|
| **Objective cấp module** | Ước lượng bậc độ lớn thời gian của một thao tác dữ liệu trước khi chạy, rồi đo và giải thích chênh lệch bằng cơ chế phần cứng |
| **Tiền đề** | M1 |
| **Exit criterion** | Tự giải thích vì sao một phép kết có thể tràn ra đĩa, vì sao nhiều chỉ mục làm ghi chậm, và vì sao thêm RAM không cứu được một truy vấn tệ |
| **Kỹ năng SFIA** | `HPCC` mức 2 · `SYSP` mức 2 |
| **Chế độ hỏng** | Học thuộc tên các tầng bộ nhớ đệm mà không bao giờ đo, nên tới chặng 7 không chẩn đoán được nút cổ chai của một công việc Spark |

Module đo là chính. Mọi khẳng định về hiệu năng trong 12 bài đều phải kiểm bằng một phép đo chạy trên máy người học. Bốn bài đầu về biểu diễn dữ liệu là nơi sinh ra lỗi âm thầm; ba bài giữa về bộ xử lý; năm bài cuối về bộ nhớ, đĩa và phép đo.

### Lesson 6 · Bits, bytes, integers and the overflow that does not announce itself `LT`
**Prerequisites.** Module 2: M1

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Nhị phân và thập lục phân, bit và byte, và cách đọc một dãy byte thô. Số nguyên có dấu và không dấu, biểu diễn bù hai, và dải giá trị của từng độ rộng. Tràn số: cơ chế một phép cộng cho ra số âm, và vì sao phần lớn ngôn ngữ không báo lỗi khi việc đó xảy ra. Ba chỗ tràn số gặp thật trong công việc dữ liệu: khoá tự tăng 32 bit chạm trần, tổng luỹ kế theo giây trong bảng số nguyên, và dấu thời gian Unix 32 bit. Chuyển kiểu thu hẹp và mất dữ liệu âm thầm khi ép từ 64 bit xuống 32 bit. Đọc kích thước dữ liệu theo bậc: một triệu dòng nhân một trăm byte là bao nhiêu, và vì sao ước lượng bậc độ lớn quan trọng hơn con số chính xác khi quyết định kiến trúc.

**Outcome.** Ước lượng kích thước một tập dữ liệu từ số dòng và lược đồ, và định vị chỗ tràn số trong ba đoạn mã cho trước.

**Đánh giá.** Tầng *áp dụng*. Objective gồm một phép ước lượng và một phép định vị lỗi, cả hai kiểm được bằng đáp án. Kiểm bằng bài ước lượng ba tập dữ liệu, đạt khi sai trong phạm vi một bậc độ lớn, cộng bài định vị tràn số đúng cả ba đoạn.

**Lab.** Viết chương trình gây tràn số nguyên 32 bit rồi quan sát kết quả. Ước lượng kích thước ba tập dữ liệu từ lược đồ, sau đó sinh dữ liệu thật và đo, so với ước lượng. Đọc ba đoạn mã và chỉ dòng nào tràn được cùng điều kiện gây tràn.

**Pitfalls.** Giả định số nguyên luôn đủ rộng · ước lượng bằng cách nhân số dòng với số cột mà quên độ rộng kiểu · coi cảnh báo ép kiểu là nhiễu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba ước lượng đều sai trong phạm vi một bậc độ lớn, và định vị đúng chỗ tràn ở cả ba đoạn mã.

### Lesson 7 · Floating point, decimal, and why money is never a float `TH`
**Prerequisites.** Lesson 6

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Biểu diễn dấu phẩy động theo chuẩn IEEE 754: dấu, số mũ, phần định trị. Vì sao 0,1 cộng 0,2 không bằng 0,3, và vì sao đây không phải lỗi của ngôn ngữ mà là hệ quả của biểu diễn nhị phân. Sai số tích luỹ khi cộng một triệu giá trị nhỏ, và cơ chế khiến thứ tự cộng đổi thì kết quả đổi, nên phép tổng trên hệ phân tán không tất định nếu dùng dấu phẩy động. Kiểu thập phân có độ chính xác xác định và chi phí của nó. Quy tắc cho tiền: lưu bằng số nguyên đơn vị nhỏ nhất hoặc bằng kiểu thập phân có khai báo độ chính xác, không bao giờ bằng dấu phẩy động. So sánh hai số thực bằng ngưỡng sai số thay vì bằng dấu bằng. Ba chỗ sai số lọt vào báo cáo tài chính: tổng theo nhóm, tỉ lệ phần trăm, và làm tròn trước khi cộng thay vì sau khi cộng.

**Outcome.** Chứng minh bằng thực nghiệm rằng một phép tổng dấu phẩy động cho kết quả khác nhau theo thứ tự cộng, và sửa nó bằng kiểu thập phân.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí đúng sai tuyệt đối, kiểm bằng chạy thật. Đạt khi bản thực nghiệm cho ra hai kết quả khác nhau trên cùng tập số, và bản sửa bằng kiểu thập phân cho cùng một kết quả ở mọi thứ tự cộng. Giải thích đúng mà không chạy được thì chưa đạt.

**Lab.** Sinh một triệu giá trị tiền nhỏ. Cộng theo thứ tự tăng dần, giảm dần và ngẫu nhiên bằng dấu phẩy động, ghi ba kết quả. Đổi sang kiểu thập phân, lặp lại, xác nhận ba kết quả bằng nhau. Đo chênh lệch thời gian chạy giữa hai kiểu.

**Pitfalls.** Dùng dấu phẩy động cho tiền vì nó nhanh hơn · so sánh hai số thực bằng dấu bằng · làm tròn từng dòng trước khi cộng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba thứ tự cộng cho ba kết quả khác nhau ở dấu phẩy động và một kết quả duy nhất ở kiểu thập phân, có số đo thời gian kèm theo.

### Lesson 8 · Text encoding, UTF-8 and endianness `TH`
**Prerequisites.** Lesson 6

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bảng mã và điểm mã: khác biệt giữa ký tự, điểm mã và byte. UTF-8 là mã hoá độ dài thay đổi: một ký tự tiếng Việt có dấu chiếm nhiều byte hơn một ký tự ASCII, nên độ dài chuỗi tính theo ký tự khác độ dài tính theo byte, và cắt chuỗi theo byte làm hỏng ký tự. Chuẩn hoá Unicode và vì sao hai chuỗi trông giống hệt nhau lại không bằng nhau: cùng một chữ có dấu biểu diễn được bằng một điểm mã hoặc bằng hai điểm mã ghép. Hậu quả trực tiếp cho công việc dữ liệu: khoá kết không khớp, phép đếm giá trị phân biệt ra sai số. Ký tự đầu tệp đánh dấu thứ tự byte và cách nó làm hỏng cột đầu tiên khi đọc CSV. Thứ tự byte lớn nhỏ và chỗ nó xuất hiện: định dạng tệp nhị phân và giao thức mạng. Phát hiện bảng mã của một tệp lạ và vì sao việc đó chỉ là phỏng đoán.

**Outcome.** Định vị nguyên nhân khi hai chuỗi tiếng Việt trông giống nhau nhưng không khớp khi kết, và sửa bằng chuẩn hoá Unicode.

**Đánh giá.** Tầng *phân tích*. Objective là truy nguyên một lỗi có nhiều nguyên nhân khả dĩ, không phải làm theo hướng dẫn. Kiểm bằng ba tệp mỗi tệp hỏng vì một nguyên nhân khác nhau: bảng mã sai, chuẩn hoá khác nhau, ký tự đánh dấu đầu tệp. Đạt khi định vị đúng cả ba và dẫn được bằng chứng ở mức byte.

**Lab.** Nhận ba tệp CSV tiếng Việt hỏng theo ba cách. Với mỗi tệp, xem nội dung ở mức byte, định vị nguyên nhân, sửa, và chứng minh phép kết khớp sau khi sửa. Đo số cặp khớp thêm sau chuẩn hoá.

**Pitfalls.** Đếm độ dài chuỗi bằng byte rồi cắt giữa ký tự · giả định mọi tệp là UTF-8 · bỏ qua ký tự đánh dấu đầu tệp rồi tên cột đầu có ký tự lạ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Định vị đúng nguyên nhân cả ba tệp với bằng chứng ở mức byte, và phép kết khớp sau khi sửa.

### Lesson 9 · Dates, times and timezones as a source of silent error `TH`
**Prerequisites.** Lesson 6

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Dấu thời gian Unix, múi giờ, và độ lệch múi giờ không phải là múi giờ. Giờ mùa hè tạo ra hai bất thường mỗi năm: một giờ không tồn tại và một giờ xuất hiện hai lần, nên dấu thời gian cục bộ không phải khoá duy nhất. Quy tắc vận hành: lưu bằng UTC, chuyển sang giờ địa phương ở tầng hiển thị, và luôn ghi rõ múi giờ trong lược đồ. Bốn chỗ lệch múi giờ lọt vào báo cáo: ranh giới ngày khác nhau giữa hai hệ thống, phép gộp theo ngày trên dữ liệu UTC cho một tổ chức ở múi giờ khác, phép so cùng kỳ năm trước khi năm nhuận, và tuần ISO khác tuần lịch thường. Định dạng ngày mơ hồ giữa kiểu ngày trước tháng và tháng trước ngày: cơ chế sai không phát tín hiệu, nên tồn tại được qua nhiều kỳ báo cáo. Độ phân giải dấu thời gian và mất mát khi ép từ micro giây xuống giây. Đặc thù Việt Nam: Tết âm lịch dịch chuyển giữa tháng dương lịch làm phép so cùng kỳ lệch.

**Outcome.** Chuyển một cột ngày trộn nhiều định dạng và nhiều múi giờ về một chuẩn thống nhất, và chứng minh không bản ghi nào bị hoán đổi ngày với tháng.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí kiểm chứng được bằng đối chứng. Đạt khi bảng sau chuẩn hoá khớp từng dòng với bảng đối chứng, và khi người học chỉ ra được số bản ghi từng mơ hồ cùng cách phân giải. Không kiểm bằng câu hỏi vì lỗi này chỉ lộ ra trên dữ liệu thật.

**Lab.** Nhận một tệp có cột ngày trộn ba định dạng và hai múi giờ, trong đó 40 bản ghi rơi vào vùng mơ hồ ngày tháng. Chuẩn hoá về UTC. Đếm và phân giải từng bản ghi mơ hồ có nêu căn cứ. So với bảng đối chứng.

**Pitfalls.** Ép kiểu ngày bằng thư viện tự đoán định dạng rồi tin kết quả · lưu giờ địa phương không kèm múi giờ · gộp theo ngày trên dữ liệu UTC cho tổ chức ở múi giờ khác.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng sau chuẩn hoá khớp từng dòng với đối chứng, và 40 bản ghi mơ hồ đều có căn cứ phân giải.

### Lesson 10 · The CPU instruction cycle, registers and pipelines `LT`
**Prerequisites.** Lesson 6

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Chu kỳ lệnh: nạp, giải mã, thực thi, ghi lại. Thanh ghi là mức lưu trữ nhanh nhất và ít nhất. Đường ống lệnh cho phép nhiều lệnh ở các chặng khác nhau cùng lúc, và điều kiện đường ống bị xả. Dự đoán nhánh: cơ chế, và vì sao một vòng lặp có nhánh khó đoán chạy chậm hơn hẳn vòng lặp có nhánh dễ đoán trên cùng số phép tính. Tập lệnh đơn dòng nhiều dữ liệu và lý do các công cụ phân tích hiện đại cố sắp dữ liệu sao cho dùng được nó, đây là một phần lý do lưu trữ theo cột thắng cho tải phân tích. Xung nhịp và số lệnh mỗi chu kỳ, và vì sao so sánh xung nhịp giữa hai bộ xử lý khác kiến trúc là vô nghĩa. Thang bậc độ lớn cần thuộc: một lệnh, một lần truy cập bộ nhớ đệm cấp một, một lần truy cập bộ nhớ chính, một lần đọc đĩa thể rắn, một lần đi mạng trong trung tâm dữ liệu.

**Outcome.** Sắp xếp năm thao tác theo bậc độ lớn thời gian và dùng thang đó để ước lượng thời gian một vòng lặp trước khi chạy.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết, chưa có công cụ đo sâu, nên objective dừng ở chỗ dùng được thang bậc. Kiểm bằng bài sắp xếp và bài ước lượng; đạt khi sắp đúng thứ tự năm thao tác và ước lượng vòng lặp sai trong phạm vi một bậc so với số đo thật.

**Lab.** Học thuộc thang bậc độ lớn năm mức. Viết hai vòng lặp cùng số phép tính, một có nhánh dễ đoán một có nhánh khó đoán, ước lượng trước rồi đo. Giải thích chênh lệch bằng dự đoán nhánh.

**Pitfalls.** So sánh hai bộ xử lý bằng xung nhịp · cho rằng số phép tính bằng nhau thì thời gian bằng nhau · bỏ qua chi phí nạp dữ liệu khi đếm phép tính.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Sắp đúng thứ tự năm thao tác, và ước lượng vòng lặp sai trong phạm vi một bậc so với số đo.

### Lesson 11 · Cache hierarchy, cache lines and locality `TH`
**Prerequisites.** Lesson 10

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba cấp bộ nhớ đệm và tỉ lệ dung lượng với độ trễ giữa chúng. Dòng bộ nhớ đệm là đơn vị nạp: đọc một byte thì nạp cả dòng, nên truy cập tuần tự rẻ hơn truy cập ngẫu nhiên rất nhiều dù cùng số byte. Cục bộ theo không gian và cục bộ theo thời gian. Hệ quả trực tiếp cho công việc dữ liệu: duyệt mảng theo thứ tự lưu nhanh hơn duyệt ngược thứ tự, và đây là một phần lý do lưu trữ theo cột nhanh hơn lưu trữ theo dòng cho phép gộp trên một cột. Chia sẻ giả: hai luồng ghi vào hai biến khác nhau nằm cùng một dòng bộ nhớ đệm làm chậm nhau, một lỗi hiệu năng không nhìn thấy trong mã. Đo tỉ lệ trượt bộ nhớ đệm bằng công cụ đếm sự kiện phần cứng. Vì sao cấu trúc dữ liệu liên kết bằng con trỏ chậm hơn mảng dù cùng độ phức tạp tiệm cận.

**Outcome.** Đo chênh lệch thời gian giữa duyệt tuần tự và duyệt ngẫu nhiên trên cùng lượng dữ liệu, và giải thích chênh lệch bằng dòng bộ nhớ đệm.

**Đánh giá.** Tầng *phân tích*. Objective đòi giải thích một số đo bằng cơ chế, không chỉ tạo ra số đo. Kiểm bằng báo cáo: phải có số đo cho ít nhất ba kích thước dữ liệu bắc qua ranh giới bộ nhớ đệm, và phải chỉ ra chỗ đường cong thời gian gãy cùng lý do. Có số mà không giải thích được chỗ gãy thì chưa đạt.

**Lab.** Viết chương trình duyệt mảng theo ba cách: tuần tự, nhảy bước bằng kích thước dòng bộ nhớ đệm, và ngẫu nhiên. Chạy ở năm kích thước dữ liệu từ nhỏ hơn bộ nhớ đệm cấp một tới lớn hơn cấp ba. Vẽ đường cong thời gian và chỉ chỗ gãy.

**Pitfalls.** Đo một kích thước dữ liệu rồi kết luận chung · quên làm nóng bộ nhớ đệm trước khi đo · so sánh hai chương trình khác nhau về số phép tính rồi quy hết cho bộ nhớ đệm.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Có số đo ở năm kích thước, đường cong có chỗ gãy rõ, và chỗ gãy giải thích được bằng ranh giới cấp bộ nhớ đệm.

### Lesson 12 · Core against thread, context switch and the cost of switching `LT`
**Prerequisites.** Lesson 10

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Lõi vật lý, luồng phần cứng và luồng phần mềm là ba thứ khác nhau và thường bị gộp làm một. Đa luồng đồng thời cho phép một lõi chạy hai luồng phần cứng, và vì sao nó tăng thông lượng cho tải chờ bộ nhớ nhưng không tăng cho tải tính toán thuần. Bộ lập lịch của hệ điều hành và lát thời gian. Chuyển ngữ cảnh: những gì phải lưu và khôi phục, chi phí trực tiếp và chi phí gián tiếp do bộ nhớ đệm bị làm nguội. Hệ quả vận hành: số luồng lớn hơn số lõi rất nhiều làm giảm thông lượng chứ không tăng, và đây là lỗi cấu hình phổ biến của tiến trình thực thi trong công cụ điều phối. Tải nghẽn tính toán so với tải nghẽn vào ra, cách phân biệt bằng số đo, và vì sao hai loại này cần số luồng khác nhau. Mối liên hệ tới chặng sau: số phân vùng trong Spark và số tiến trình thực thi trong công cụ điều phối đều là cùng một bài toán.

**Outcome.** Phân loại một tải là nghẽn tính toán hay nghẽn vào ra bằng số đo, và chọn số luồng phù hợp với loại tải đó.

**Đánh giá.** Tầng *phân tích*. Objective là phân loại có bằng chứng rồi suy ra quyết định cấu hình. Kiểm bằng hai tải dựng sẵn, một loại mỗi tải; đạt khi phân loại đúng cả hai, dẫn được số đo làm bằng chứng, và số luồng chọn ra cho thông lượng cao nhất trong bảng thực nghiệm của chính mình.

**Lab.** Dựng hai tải: một tính toán thuần, một đọc tệp nhiều. Chạy mỗi tải ở 1, 2, 4, 8, 16, 64 luồng. Đo thông lượng và mức dùng bộ xử lý. Vẽ hai đường cong, chỉ điểm cực đại của từng cái và giải thích vì sao hai điểm khác nhau.

**Pitfalls.** Đặt số luồng bằng số lõi cho mọi loại tải · tăng số luồng tới khi máy đứng rồi kết luận máy yếu · đo thông lượng mà không đo mức dùng bộ xử lý.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân loại đúng cả hai tải có số đo kèm theo, và hai đường cong có điểm cực đại khác nhau được giải thích.

### Lesson 13 · RAM - latency, bandwidth, heap and stack `LT`
**Prerequisites.** Lesson 11

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Độ trễ và băng thông là hai đại lượng khác nhau và tối ưu cho cái này thường đánh đổi cái kia. Ngăn xếp và vùng nhớ động: cách cấp phát, cách thu hồi, và vì sao cấp phát trên ngăn xếp gần như miễn phí còn trên vùng nhớ động thì không. Phân mảnh vùng nhớ động và cơ chế khiến một tiến trình còn nhiều bộ nhớ trống vẫn không cấp phát được khối lớn. Thu gom rác và tạm dừng do nó gây ra, cùng lý do một công việc xử lý dữ liệu lớn trong ngôn ngữ có thu gom rác có thể đứng vài giây không rõ nguyên nhân. Chi phí bộ nhớ thật của một cấu trúc dữ liệu so với kích thước dữ liệu thuần: phần đầu của đối tượng, con trỏ, và hệ số phình của từ điển băm. Ước lượng bộ nhớ cần cho một bảng trong bộ nhớ từ số dòng và lược đồ, và vì sao ước lượng đó luôn phải nhân hệ số an toàn.

**Outcome.** Ước lượng bộ nhớ cần cho một bảng trong bộ nhớ từ lược đồ, rồi đo thật và giải thích hệ số phình.

**Đánh giá.** Tầng *áp dụng*. Objective gồm ước lượng và đối chiếu với số đo. Kiểm bằng ba cấu trúc dữ liệu khác nhau chứa cùng dữ liệu; đạt khi ước lượng sai trong phạm vi hệ số hai và khi người học chỉ ra được nguồn gốc phần phình cho ít nhất hai trong ba cấu trúc.

**Lab.** Nạp cùng một triệu bản ghi vào ba cấu trúc: danh sách các từ điển, mảng theo cột, và khung dữ liệu. Ước lượng trước, đo bộ nhớ thật sau. Giải thích chênh lệch. Gây phân mảnh bằng cách cấp phát rồi giải phóng xen kẽ, quan sát.

**Pitfalls.** Ước lượng bằng số byte dữ liệu thuần · bỏ qua phần đầu của đối tượng trong ngôn ngữ động · coi bộ nhớ trống theo báo cáo hệ điều hành là bộ nhớ cấp phát được.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba ước lượng sai trong phạm vi hệ số hai, và nguồn gốc phần phình giải thích được cho ít nhất hai cấu trúc.

### Lesson 14 · Virtual memory, paging, page faults, swap and OOM `TH`
**Prerequisites.** Lesson 13

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bộ nhớ ảo tách địa chỉ chương trình nhìn thấy khỏi địa chỉ vật lý. Trang, bảng trang và bộ đệm tra cứu địa chỉ. Lỗi trang nhẹ và lỗi trang nặng: cái đầu rẻ, cái sau phải đọc đĩa nên đắt gấp nhiều bậc. Vùng hoán đổi: khi nào hệ điều hành dùng nó, và vì sao một tiến trình rơi vào hoán đổi thì thà chết còn hơn chạy tiếp, bởi thông lượng sụt xuống mức không dùng được. Cơ chế giết tiến trình khi cạn bộ nhớ: tiến trình nào bị chọn và vì sao nó thường không phải tiến trình gây ra vấn đề. Đọc dấu vết trong nhật ký hệ thống để xác nhận một tiến trình bị giết vì cạn bộ nhớ chứ không phải vì lỗi mã. Giới hạn bộ nhớ theo nhóm tiến trình và mối liên hệ tới giới hạn tài nguyên của vùng chứa ở chặng 7. Ánh xạ tệp vào bộ nhớ và khi nào nó có lợi.

**Outcome.** Phân biệt một tiến trình bị giết vì cạn bộ nhớ với một tiến trình chết vì lỗi mã, bằng bằng chứng trong nhật ký hệ thống.

**Đánh giá.** Tầng *phân tích*. Objective là chẩn đoán phân biệt hai nguyên nhân giống nhau ở bề mặt. Kiểm bằng ba ca dựng sẵn: một cạn bộ nhớ, một lỗi mã, một rơi vào hoán đổi và chậm chứ chưa chết. Đạt khi phân loại đúng cả ba và dẫn được dòng nhật ký hoặc số đo cho từng ca.

**Lab.** Dựng ba ca trong máy ảo có giới hạn bộ nhớ. Ca một cấp phát tới khi bị giết. Ca hai lỗi mã. Ca ba nạp tập dữ liệu lớn hơn bộ nhớ và quan sát hoán đổi. Với mỗi ca, thu nhật ký hệ thống và số đo lỗi trang nặng.

**Pitfalls.** Kết luận hết bộ nhớ chỉ vì tiến trình chết · bỏ qua trạng thái hoán đổi rồi tưởng máy chậm do bộ xử lý · tăng bộ nhớ mà không xem tiến trình nào thật sự chiếm.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân loại đúng cả ba ca với dòng nhật ký hoặc số đo lỗi trang nặng làm bằng chứng.

### Lesson 15 · Disks - HDD, SSD, NVMe and the sequential against random gap `TH`
**Prerequisites.** Lesson 13

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Đĩa từ có bộ phận cơ nên thời gian tìm kiếm chi phối, còn ổ thể rắn không có nên khoảng cách giữa đọc tuần tự và đọc ngẫu nhiên hẹp lại nhưng không biến mất. Ba đại lượng và quan hệ giữa chúng: số thao tác vào ra mỗi giây, thông lượng, và độ trễ. Vì sao tối ưu một đại lượng thường làm xấu đại lượng khác. Độ sâu hàng đợi và cơ chế ổ thể rắn chỉ đạt thông lượng công bố khi có đủ yêu cầu song song. Kích thước khối và chi phí của việc đọc một dòng nhỏ trong một khối lớn. Hệ quả trực tiếp cho công việc dữ liệu: vấn đề nhiều tệp nhỏ, và vì sao đọc một nghìn tệp một mê ga byte chậm hơn nhiều so với đọc một tệp một ghi ga byte dù cùng tổng dung lượng. Ba loại lưu trữ và mẫu truy cập của từng loại: lưu trữ khối, lưu trữ tệp, lưu trữ đối tượng. Độ trễ của lưu trữ đối tượng so với đĩa cục bộ và hệ quả lên thiết kế ở chặng 7.

**Outcome.** Đo khoảng cách giữa đọc tuần tự và đọc ngẫu nhiên trên máy của mình, và ước lượng thời gian đọc một tập dữ liệu chia thành nhiều tệp nhỏ trước khi chạy.

**Đánh giá.** Tầng *áp dụng*. Objective gồm một phép đo và một phép ước lượng dùng kết quả đo. Kiểm bằng bài dự đoán rồi đối chứng: đạt khi ước lượng thời gian đọc một nghìn tệp nhỏ sai trong phạm vi hệ số hai so với số đo thật.

**Lab.** Đo đọc tuần tự và đọc ngẫu nhiên ở bốn độ sâu hàng đợi. Chia một tập dữ liệu một ghi ga byte thành một tệp, một trăm tệp, và mười nghìn tệp. Ước lượng thời gian đọc từng cách trước khi chạy, rồi đo.

**Pitfalls.** Đo mà không vô hiệu hoá bộ đệm trang nên đo lại tốc độ bộ nhớ · so sánh số thao tác vào ra mỗi giây giữa hai ổ mà bỏ qua độ sâu hàng đợi · chia nhỏ tệp để chạy song song mà không tính chi phí mở tệp.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Có số đo ở bốn độ sâu hàng đợi, và ước lượng thời gian đọc mười nghìn tệp nhỏ sai trong phạm vi hệ số hai.

### Lesson 16 · Durability - fsync, write amplification and filesystems `TH`
**Prerequisites.** Lesson 15

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ghi thành công không có nghĩa dữ liệu đã nằm trên đĩa. Chuỗi bộ đệm giữa lời gọi ghi và mặt đĩa: bộ đệm của ứng dụng, bộ đệm trang của hệ điều hành, bộ đệm của thiết bị. Lời gọi đồng bộ hoá ép xuống tới đâu, chi phí của nó, và vì sao một cơ sở dữ liệu gọi nó ở mỗi lần xác nhận giao dịch. Mất dữ liệu khi mất điện ở từng mức bộ đệm. Khuếch đại ghi: ghi một byte làm thiết bị ghi nhiều hơn một byte, cơ chế ở ổ thể rắn do xoá theo khối, và cơ chế ở cơ sở dữ liệu do nhật ký ghi trước cộng với ghi dữ liệu. Hệ quả: nhiều chỉ mục làm mỗi lần chèn tốn nhiều lần ghi hơn, đây là vế thứ hai của tiêu chí ra module. Hệ tệp và nhật ký của nó. Ghi nguyên tử bằng ghi tệp tạm rồi đổi tên, mẫu dùng lại suốt chương trình. Không gian đĩa đầy và bốn triệu chứng nó gây ra ở tầng ứng dụng.

**Outcome.** Chứng minh bằng thực nghiệm chi phí của lời gọi đồng bộ hoá, và cài đặt ghi nguyên tử bằng mẫu ghi tệp tạm rồi đổi tên.

**Đánh giá.** Tầng *áp dụng*. Objective gồm một số đo và một sản phẩm mã. Đạt khi bảng số đo cho thấy chênh lệch thông lượng giữa có và không có đồng bộ hoá, và khi cài đặt ghi nguyên tử sống sót qua thực nghiệm giết tiến trình giữa chừng mà không để lại tệp dở.

**Lab.** Ghi một trăm nghìn bản ghi theo ba chế độ: không đồng bộ, đồng bộ mỗi bản ghi, đồng bộ mỗi một nghìn bản ghi. Đo thông lượng. Cài đặt ghi nguyên tử bằng tệp tạm và đổi tên, rồi giết tiến trình giữa chừng 10 lần và xác nhận không lần nào để lại tệp dở.

**Pitfalls.** Tin rằng ghi xong là an toàn · gọi đồng bộ hoá mỗi bản ghi rồi kết luận đĩa chậm · ghi đè trực tiếp lên tệp đích nên mất cả bản cũ khi hỏng giữa chừng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng ba chế độ có số thông lượng, và 10 lần giết tiến trình không để lại tệp dở nào.

### Lesson 17 · Measuring - benchmark a computation and locate the bottleneck `TH`
**Prerequisites.** Lesson 16

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phép đo sai còn tệ hơn không đo, vì nó cho kết luận sai mà có vẻ có căn cứ. Sáu nguồn nhiễu phải kiểm soát: bộ đệm nóng hay nguội, tải nền, điều chỉnh xung nhịp theo nhiệt, thời gian khởi động của môi trường chạy, biến thiên giữa các lần chạy, và kích thước dữ liệu không đại diện. Đo nhiều lần và báo trung vị cùng phân vị 95, không báo trung bình, vì phân bố thời gian chạy lệch phải. Bốn số đo tối thiểu cho mọi phép đo hiệu năng: thời gian, mức dùng bộ xử lý, bộ nhớ đỉnh, và lượng vào ra. Quy trình định vị nút cổ chai theo bốn bước: đo bốn số trên, tìm tài nguyên bão hoà, đổi một biến duy nhất, đo lại. Vì sao đổi hai biến cùng lúc làm phép đo mất giá trị. Ghi lại phép đo sao cho lặp lại được: lệnh chạy, dữ liệu, phần cứng, phiên bản, và kết quả thô.

**Outcome.** Thiết kế và chạy một phép đo có kiểm soát nhiễu cho một thao tác dữ liệu, rồi định vị tài nguyên bão hoà bằng bốn số đo.

**Đánh giá.** Tầng *đánh giá*. Objective đòi thiết kế một phép đo và biện minh các lựa chọn kiểm soát nhiễu, không có một đáp án duy nhất. Kiểm bằng rà soát chéo: một học viên khác chạy lại theo tài liệu và phải ra kết quả trong phạm vi sai số mà người thiết kế công bố. Chạy lại không ra thì phép đo chưa đủ tài liệu.

**Lab.** Thiết kế phép đo cho một thao tác gộp trên năm triệu dòng. Kiểm soát đủ sáu nguồn nhiễu, nêu rõ cách kiểm soát từng nguồn. Chạy 10 lần, báo trung vị và phân vị 95 cùng bốn số đo. Đưa tài liệu cho người khác chạy lại.

**Pitfalls.** Báo trung bình thay vì trung vị · chạy một lần rồi kết luận · đổi cả kích thước dữ liệu lẫn số luồng trong cùng một lần thử.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Người khác chạy lại theo tài liệu ra kết quả trong phạm vi sai số đã công bố, và tài nguyên bão hoà được chỉ ra có bằng chứng.

# MODULE 3 · OPERATING SYSTEMS AND LINUX

**Lessons 18–29 · 24 giờ**

| | |
|---|---|
| **Objective cấp module** | Nhận một sự cố pipeline chậm hoặc chết và chứng minh bằng số đo nó nghẽn ở bộ xử lý, bộ nhớ, đĩa hay mạng |
| **Tiền đề** | M2 |
| **Exit criterion** | Đạt Cổng 1 ≥ 70/100: chẩn đoán đúng bốn ca sự cố dựng sẵn, mỗi ca dẫn được số đo làm bằng chứng |
| **Kỹ năng SFIA** | `SYSP` mức 3 · `USUP` mức 2 |
| **Chế độ hỏng** | Học thuộc danh sách lệnh mà không bao giờ diễn tập sự cố, nên lúc hệ thống thật hỏng thì gõ lệnh ngẫu nhiên |

Bảy bài đầu là cơ chế hệ điều hành, bốn bài giữa là công cụ dòng lệnh, bài cuối là cổng 1. Mọi cơ chế đều được kiểm bằng một diễn tập sự cố chứ không bằng câu hỏi lý thuyết, vì đây là module mà kiến thức chỉ có giá trị lúc hệ thống đang hỏng.

### Lesson 18 · Kernel space, user space and the system call boundary `LT`
**Prerequisites.** Module 3: M2

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Hai không gian đặc quyền và lý do tách: một tiến trình lỗi không được phép làm sập máy. Lời gọi hệ thống là cổng duy nhất để chương trình yêu cầu nhân làm việc, và mọi thao tác đọc tệp, gửi mạng, cấp phát bộ nhớ đều đi qua đó. Chi phí một lời gọi hệ thống so với một lời gọi hàm thường, theo thang bậc độ lớn ở lesson 10. Hệ quả trực tiếp cho công việc dữ liệu: đọc tệp từng byte gọi hệ thống một triệu lần, đọc theo khối gọi một nghìn lần, và chênh lệch đó lớn hơn chênh lệch do đĩa. Theo dõi lời gọi hệ thống của một tiến trình để biết nó thật sự làm gì, kỹ thuật dùng khi mã nguồn không sẵn hoặc nhật ký không đủ. Trình điều khiển thiết bị và hệ tệp ảo: vì sao mọi thứ trong Linux trình bày được như tệp, gồm cả thông tin tiến trình và thiết bị.

**Outcome.** Đếm số lời gọi hệ thống của hai cách đọc cùng một tệp, và giải thích chênh lệch thời gian bằng số đếm đó.

**Đánh giá.** Tầng *phân tích*. Objective đòi nối một số đếm với một chênh lệch thời gian, không chỉ nhắc lại định nghĩa. Kiểm bằng báo cáo có hai cột số: số lời gọi hệ thống và thời gian, cho ít nhất ba kích thước khối đọc. Đạt khi chỉ ra được quan hệ giữa hai cột và ước lượng được chi phí trung bình một lời gọi.

**Lab.** Đọc một tệp 500 mê ga byte theo bốn kích thước khối: 1 byte, 512 byte, 4 ki lô byte, 1 mê ga byte. Với mỗi cách, đếm lời gọi hệ thống bằng công cụ theo dõi và đo thời gian. Lập bảng và ước lượng chi phí một lời gọi.

**Pitfalls.** Theo dõi lời gọi hệ thống trên tải thật rồi tưởng số đo là bình thường, trong khi công cụ theo dõi làm chậm tiến trình nhiều lần · đọc từng byte rồi đổ lỗi cho đĩa · bỏ qua bộ đệm của thư viện khi đếm.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng bốn kích thước khối có cả số lời gọi lẫn thời gian, và ước lượng chi phí một lời gọi nằm trong phạm vi một bậc so với thang ở lesson 10.

### Lesson 19 · Processes, threads and the scheduler `LT`
**Prerequisites.** Lesson 18

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Tiến trình có không gian địa chỉ riêng, luồng dùng chung không gian địa chỉ của tiến trình. Hệ quả: luồng trao đổi dữ liệu rẻ nhưng làm hỏng nhau dễ, tiến trình thì ngược lại. Cây tiến trình, tiến trình cha con, và tiến trình mồ côi bị nhận nuôi. Tiến trình xác sống: cơ chế sinh ra và vì sao nó không tốn tài nguyên nhưng vẫn là dấu hiệu mã sai. Bộ lập lịch hoàn toàn công bằng và ý niệm thời gian chạy ảo. Độ ưu tiên và giá trị nhường. Trạng thái tiến trình và ý nghĩa vận hành của từng trạng thái, trong đó trạng thái ngủ không ngắt được là trạng thái đáng lo nhất vì nó thường nghĩa là đang chờ vào ra và không giết được. Trung bình tải là gì và vì sao nó không phải phần trăm dùng bộ xử lý, một hiểu nhầm phổ biến dẫn tới chẩn đoán sai. Mối liên hệ tới chặng sau: mỗi tiến trình thực thi của công cụ điều phối là một tiến trình, và giới hạn số luồng của nó là bài toán ở lesson 12.

**Outcome.** Đọc trạng thái và trung bình tải của một máy đang chạy và kết luận nó nghẽn ở đâu, phân biệt với trường hợp chỉ có nhiều tiến trình đang ngủ.

**Đánh giá.** Tầng *phân tích*. Objective là chẩn đoán từ số đo, và bẫy chính là nhầm trung bình tải với mức dùng bộ xử lý. Kiểm bằng ba ca: một nghẽn bộ xử lý thật, một trung bình tải cao do chờ vào ra, một nhiều tiến trình ngủ. Đạt khi phân loại đúng cả ba và giải thích được vì sao trung bình tải không đủ để kết luận.

**Lab.** Dựng ba ca tải trên máy ảo. Với mỗi ca đọc trung bình tải, bảng trạng thái tiến trình và mức dùng bộ xử lý theo từng lõi. Kết luận. Sau đó tạo một tiến trình xác sống và một tiến trình mồ côi, quan sát cây tiến trình.

**Pitfalls.** Kết luận quá tải bộ xử lý từ trung bình tải · cố giết tiến trình ở trạng thái ngủ không ngắt được · đọc mức dùng bộ xử lý tổng mà không xem theo từng lõi.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân loại đúng cả ba ca, và giải thích được vì sao trung bình tải cao không đồng nghĩa nghẽn bộ xử lý.

### Lesson 20 · File descriptors, pipes and redirection `TH`
**Prerequisites.** Lesson 19

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bộ mô tả tệp là số nguyên trỏ tới một mục trong bảng của tiến trình, và ba bộ mô tả mặc định. Mọi thứ đọc ghi được đều có bộ mô tả: tệp, ống dẫn, ổ cắm mạng, thiết bị. Giới hạn số bộ mô tả mỗi tiến trình, và lỗi hết bộ mô tả: triệu chứng, nguyên nhân thường gặp là rò rỉ do không đóng kết nối, và cách xác nhận bằng cách liệt kê bộ mô tả đang mở. Ống dẫn nối đầu ra của tiến trình này vào đầu vào của tiến trình kia, và vì sao một chuỗi ống dẫn chạy song song chứ không tuần tự. Áp lực ngược trong ống dẫn: tiến trình đọc chậm làm tiến trình ghi bị chặn, và đây là cơ chế điều tiết tự nhiên, cùng ý tưởng với áp lực ngược trong hệ thống luồng ở chặng 6. Chuyển hướng đầu ra và đầu lỗi, cùng lỗi phổ biến khi gộp hai luồng sai thứ tự. Mã thoát của một chuỗi ống dẫn mặc định lấy từ lệnh cuối, và hệ quả là lỗi ở giữa chuỗi bị nuốt mất.

**Outcome.** Dựng một chuỗi ống dẫn xử lý dữ liệu lớn hơn bộ nhớ, và chứng minh lỗi ở giữa chuỗi không bị nuốt mất.

**Đánh giá.** Tầng *áp dụng*. Objective có sản phẩm chạy được và một tiêu chí đúng sai tuyệt đối về lan truyền lỗi. Đạt khi chuỗi xử lý xong tệp lớn hơn bộ nhớ và khi bơm lỗi vào lệnh giữa chuỗi thì mã thoát khác không. Chuỗi chạy được mà nuốt lỗi thì không đạt.

**Lab.** Dựng chuỗi ống dẫn lọc, biến đổi và gộp một tệp 5 ghi ga byte trên máy có 2 ghi ga byte bộ nhớ. Bơm lỗi vào lệnh giữa chuỗi, xác nhận mã thoát khác không. Viết chương trình rò rỉ bộ mô tả tệp, quan sát tới khi hết giới hạn.

**Pitfalls.** Gộp đầu lỗi vào đầu ra sai thứ tự nên mất thông báo lỗi · tin mã thoát của chuỗi ống dẫn mà không bật chế độ bắt lỗi giữa chuỗi · mở kết nối trong vòng lặp mà không đóng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chuỗi xử lý xong tệp lớn hơn bộ nhớ, và lỗi bơm vào lệnh giữa chuỗi làm mã thoát khác không.

### Lesson 21 · Signals and what happens when a process is killed `TH`
**Prerequisites.** Lesson 19

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Tín hiệu là cơ chế thông báo không đồng bộ tới tiến trình. Nhóm tín hiệu quan trọng cho công việc dữ liệu: yêu cầu kết thúc lịch sự, ngắt từ bàn phím, kết thúc cưỡng bức không chặn được, treo, và tín hiệu người dùng tự định nghĩa. Bắt tín hiệu và dọn dẹp trước khi thoát: đóng kết nối, ghi nốt bộ đệm, xoá tệp tạm, cập nhật điểm kiểm tra. Vì sao tín hiệu kết thúc cưỡng bức không bắt được, và hệ quả là mọi thiết kế phải chịu được việc bị dừng đột ngột ở bất kỳ điểm nào. Trình tự dừng lịch sự chuẩn: gửi yêu cầu kết thúc, chờ một khoảng, rồi mới cưỡng bức, và đây chính là trình tự công cụ điều phối vùng chứa dùng. Nhóm tiến trình và cơ chế tín hiệu tới cả nhóm, lý do một tiến trình con có thể sống sót khi cha chết. Mối liên hệ tới ghi nguyên tử ở lesson 16: bị giết giữa chừng là ca kiểm thử bắt buộc, không phải ca hiếm.

**Outcome.** Viết một tiến trình xử lý dữ liệu dừng lịch sự khi nhận yêu cầu kết thúc, và chứng minh nó không để lại trạng thái dở khi bị giết cưỡng bức.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí kiểm chứng bằng thực nghiệm lặp lại. Đạt khi 20 lần giết ở thời điểm ngẫu nhiên không lần nào để lại tệp dở hoặc bản ghi trùng, và khi tiến trình ghi được nhật ký dọn dẹp ở trường hợp kết thúc lịch sự.

**Lab.** Viết tiến trình đọc một triệu bản ghi và ghi ra tệp, có bắt tín hiệu để ghi điểm kiểm tra. Giết lịch sự 10 lần và cưỡng bức 10 lần ở thời điểm ngẫu nhiên. Sau mỗi lần, chạy lại từ điểm kiểm tra và đối soát tổng số bản ghi.

**Pitfalls.** Bắt tín hiệu rồi làm việc nặng trong hàm xử lý tín hiệu · giả định chỉ bị dừng lịch sự · ghi điểm kiểm tra sau khi ghi dữ liệu nên chạy lại bị trùng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** 20 lần giết không lần nào để lại tệp dở hay bản ghi trùng, và tổng bản ghi sau chạy lại luôn khớp.

### Lesson 22 · The page cache and why the second read is fast `TH`
**Prerequisites.** Lesson 18

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bộ đệm trang giữ nội dung tệp vừa đọc trong bộ nhớ trống, nên lần đọc thứ hai không chạm đĩa. Hệ quả cho phép đo: mọi con số đo hiệu năng đĩa đều vô nghĩa nếu không khai báo bộ đệm nóng hay nguội, nối lại nguyên tắc ở lesson 17. Cách xoá bộ đệm trước khi đo. Bộ nhớ trống theo báo cáo hệ điều hành gồm cả bộ đệm trang, nên con số bộ nhớ trống thấp thường không phải vấn đề, một hiểu nhầm dẫn tới việc mua thêm RAM không cần thiết. Ghi trả sau và cửa sổ mất dữ liệu nó tạo ra, nối lại lesson 16. Gợi ý cho nhân về mẫu truy cập tệp và khi nào đáng dùng. Đọc trước tuần tự và vì sao nó làm đọc tuần tự nhanh hơn dự đoán từ số đo đĩa thuần. Ánh xạ tệp vào bộ nhớ dùng chung cơ chế bộ đệm trang. Hệ quả ở chặng sau: cơ sở dữ liệu có bộ đệm riêng, nên có hai tầng đệm chồng nhau và cấu hình sai làm dữ liệu nằm hai nơi tốn gấp đôi bộ nhớ.

**Outcome.** Đo cùng một phép đọc ở trạng thái đệm nguội và đệm nóng, và giải thích con số bộ nhớ trống của hệ điều hành cho một máy đang chạy.

**Đánh giá.** Tầng *áp dụng*. Objective gồm một phép đo có kiểm soát và một phép đọc số liệu hệ thống. Đạt khi chênh lệch nóng nguội đo được và khi người học phân tách đúng con số bộ nhớ thành phần dùng thật, phần đệm, và phần trống thật, trên một máy có tải.

**Lab.** Đo đọc một tệp 2 ghi ga byte ở trạng thái nguội và nóng, lặp ba lần mỗi trạng thái. Đọc và phân tách con số bộ nhớ của máy. Chạy một tải đọc nhiều tệp, quan sát bộ đệm trang lớn dần và bộ nhớ trống nhỏ dần.

**Pitfalls.** Đo hiệu năng đĩa mà quên xoá bộ đệm · báo động vì bộ nhớ trống thấp trong khi phần lớn là bộ đệm · cấu hình bộ đệm cơ sở dữ liệu bằng toàn bộ RAM rồi máy rơi vào hoán đổi.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chênh lệch nóng nguội có số đo ba lần mỗi trạng thái, và phân tách đúng ba phần của con số bộ nhớ.

### Lesson 23 · Users, groups, permissions and ACLs `TH`
**Prerequisites.** Lesson 18

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Định danh người dùng và nhóm, quyền đọc ghi thực thi cho chủ sở hữu, nhóm và người khác. Ý nghĩa của quyền thực thi trên thư mục khác hẳn trên tệp: nó cho phép đi vào chứ không phải chạy. Mặt nạ tạo tệp và vì sao tệp mới có quyền khác mong đợi. Bit đặt định danh nhóm trên thư mục để tệp mới thừa kế nhóm, mẫu dùng cho thư mục dữ liệu nhiều người ghi. Danh sách kiểm soát truy cập khi mô hình ba nhóm không đủ. Quyền bị từ chối là một trong năm sự cố diễn tập bắt buộc, và quy trình chẩn đoán: kiểm quyền trên tệp, rồi quyền thực thi trên từng thư mục cha, rồi định danh mà tiến trình thật sự chạy dưới. Tài khoản dịch vụ và nguyên tắc đặc quyền tối thiểu: tiến trình pipeline không chạy dưới quyền quản trị, và lý do đây là điều kiện bắt buộc chứ không phải khuyến nghị. Hệ quả ở chặng 7: định danh trong vùng chứa và chuyện tệp ghi ra máy chủ thuộc về ai.

**Outcome.** Chẩn đoán một lỗi quyền bị từ chối tới đúng nguyên nhân trong ba nguyên nhân khả dĩ, và thiết lập thư mục dữ liệu nhiều người ghi mà tệp mới thừa kế đúng nhóm.

**Đánh giá.** Tầng *phân tích*. Objective là chẩn đoán phân biệt, vì triệu chứng giống nhau ở cả ba nguyên nhân. Kiểm bằng ba ca: thiếu quyền trên tệp, thiếu quyền thực thi trên thư mục cha, và tiến trình chạy dưới định danh khác dự kiến. Đạt khi định vị đúng cả ba và dẫn được lệnh kiểm chứng.

**Lab.** Dựng ba ca quyền bị từ chối. Với mỗi ca chẩn đoán và sửa, ghi lại lệnh kiểm chứng. Sau đó dựng một thư mục dữ liệu cho hai tài khoản dịch vụ cùng ghi, cấu hình sao cho tệp mới luôn thừa kế đúng nhóm và quyền.

**Pitfalls.** Sửa bằng cách cấp quyền cho tất cả · chạy pipeline dưới quyền quản trị cho nhanh · quên kiểm quyền thực thi trên thư mục cha.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Định vị đúng cả ba nguyên nhân có lệnh kiểm chứng, và thư mục nhiều người ghi cho tệp mới thừa kế đúng nhóm.

### Lesson 24 · Namespaces and cgroups - the mechanism under containers `LT`
**Prerequisites.** Lesson 23

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Không gian tên cô lập cái tiến trình nhìn thấy: tiến trình, điểm gắn hệ tệp, mạng, định danh người dùng, tên máy. Nhóm điều khiển giới hạn cái tiến trình dùng được: bộ xử lý, bộ nhớ, vào ra, số tiến trình. Hai cơ chế này cộng lại là vùng chứa; vùng chứa không phải máy ảo, và khác biệt then chốt là dùng chung nhân. Hệ quả vận hành quan trọng nhất: giới hạn bộ nhớ của nhóm điều khiển gây ra cơ chế giết tiến trình ở lesson 14 nhưng chỉ trong phạm vi nhóm, nên một vùng chứa chết vì cạn bộ nhớ trong khi máy chủ còn thừa RAM. Giới hạn bộ xử lý theo hạn ngạch và cơ chế điều tiết: tiến trình không bị chậm đều mà bị dừng từng đợt, nên biểu đồ độ trễ có gai thay vì dốc lên đều. Đọc thông số nhóm điều khiển từ bên trong tiến trình và vì sao một số môi trường chạy đọc nhầm số lõi của máy chủ thay vì hạn ngạch, dẫn tới đặt số luồng sai. Mối liên hệ tới lesson 12 và tới chặng 7.

**Outcome.** Giải thích vì sao một tiến trình bị giết vì cạn bộ nhớ trong khi máy chủ còn RAM trống, và vì sao độ trễ có gai khi bị điều tiết bộ xử lý.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết đặt nền cho chặng 7, người học chưa dựng vùng chứa nên objective dừng ở giải thích cơ chế. Kiểm bằng hai ca dựng sẵn bằng nhóm điều khiển trực tiếp, không qua công cụ vùng chứa; đạt khi giải thích đúng cả hai hiện tượng và chỉ ra được thông số nhóm điều khiển tương ứng.

**Lab.** Dùng nhóm điều khiển trực tiếp, không qua công cụ vùng chứa. Đặt giới hạn bộ nhớ 256 mê ga byte cho một tiến trình rồi cho nó cấp phát tới khi bị giết, trong khi máy còn nhiều RAM. Đặt hạn ngạch bộ xử lý 20% rồi đo độ trễ theo thời gian, quan sát gai.

**Pitfalls.** Nhầm vùng chứa với máy ảo · đặt số luồng theo số lõi máy chủ trong khi hạn ngạch thấp hơn nhiều · kết luận máy chủ hết bộ nhớ khi thấy vùng chứa bị giết.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Giải thích đúng cả hai hiện tượng và chỉ đúng thông số nhóm điều khiển gây ra từng cái.

### Lesson 25 · The shell - quoting, expansion and the errors they cause `TH`
**Prerequisites.** Lesson 20

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Thứ tự vỏ lệnh xử lý một dòng: khai triển ngoặc, khai triển ký hiệu thư mục nhà, khai triển tham số, thay thế lệnh, khai triển số học, tách từ, rồi khai triển tên tệp. Thứ tự này giải thích gần như mọi lỗi vỏ lệnh khó hiểu. Tách từ là nguồn lỗi lớn nhất: một biến chứa khoảng trắng không đặt trong nháy kép bị tách thành nhiều tham số, nên đường dẫn có dấu cách làm hỏng script. Nháy đơn so với nháy kép: cái nào chặn khai triển nào. Ký tự đại diện khớp tên tệp trước khi lệnh chạy, nên lệnh nhận danh sách đã khai triển và không biết ký tự đại diện tồn tại. Trường hợp danh sách tệp dài quá giới hạn tham số và cách vòng qua. Biến môi trường so với biến vỏ lệnh và cách chúng truyền hoặc không truyền xuống tiến trình con. Mã thoát và ba cờ bắt lỗi nên bật đầu mọi script. Vì sao phân tích đầu ra của lệnh liệt kê tệp là mẫu sai.

**Outcome.** Sửa một script hỏng khi gặp đường dẫn có dấu cách và khi thư mục rỗng, và giải thích lỗi bằng thứ tự khai triển.

**Đánh giá.** Tầng *phân tích*. Objective đòi truy lỗi về đúng chặng trong thứ tự khai triển, không chỉ sửa cho chạy. Kiểm bằng bốn script hỏng theo bốn cơ chế khác nhau; đạt khi sửa được cả bốn và nêu đúng chặng khai triển gây ra ít nhất ba trong bốn.

**Lab.** Nhận bốn script hỏng: một do biến không đặt nháy, một do ký tự đại diện không khớp gì, một do thay thế lệnh nuốt dòng mới, một do phân tích đầu ra lệnh liệt kê tệp. Sửa cả bốn, nêu chặng khai triển gây lỗi. Chạy trên thư mục có tên tệp chứa dấu cách và ký tự tiếng Việt.

**Pitfalls.** Không đặt biến trong nháy kép · bỏ qua trường hợp thư mục rỗng nên ký tự đại diện thành chuỗi nguyên văn · viết script không bật cờ bắt lỗi.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn script chạy đúng trên thư mục có tên tệp chứa dấu cách và tiếng Việt, và nêu đúng chặng khai triển cho ít nhất ba lỗi.

### Lesson 26 · Text processing - grep, awk, sed, sort, xargs, jq `TH`
**Prerequisites.** Lesson 25

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Công cụ dòng lệnh xử lý dữ liệu lớn hơn bộ nhớ vì chúng chạy theo luồng, nên một chuỗi ống dẫn thường nhanh hơn nạp cả tệp vào công cụ phân tích. Biểu thức chính quy và ba mức độ hỗ trợ khác nhau giữa các công cụ. Công cụ xử lý theo trường: mô hình mẫu và hành động, biến dựng sẵn, và các phép gộp viết được chỉ bằng một dòng. Công cụ biên tập theo luồng cho thay thế và xoá dòng. Sắp xếp ngoài bộ nhớ: cơ chế chia tệp thành mảnh, sắp từng mảnh rồi trộn, đây chính là sắp xếp ngoài ở lesson 33 và là cơ chế Spark dùng khi tràn ra đĩa. Vì sao vị trí ngôn ngữ ảnh hưởng thứ tự sắp và làm phép nối hai tệp đã sắp bị sai. Truyền danh sách tham số an toàn khi tên tệp chứa ký tự đặc biệt. Xử lý JSON theo luồng cho tệp lớn. Đếm và đối soát bằng dòng lệnh như phép kiểm chéo độc lập với pipeline, một thói quen dùng suốt chương trình.

**Outcome.** Trả lời năm câu hỏi nghiệp vụ trên một tệp nhật ký 10 ghi ga byte chỉ bằng chuỗi ống dẫn, trên máy có 4 ghi ga byte bộ nhớ.

**Đánh giá.** Tầng *áp dụng*. Objective có ràng buộc cứng về bộ nhớ nên kiểm được bằng chạy thật. Đạt khi cả năm câu trả lời đúng so với đáp án đối chứng và không lệnh nào bị giết vì cạn bộ nhớ. Kết quả đúng mà phải nạp cả tệp vào bộ nhớ thì không đạt.

**Lab.** Nhận tệp nhật ký 10 ghi ga byte trên máy giới hạn 4 ghi ga byte. Trả lời năm câu: số yêu cầu theo giờ, 10 đường dẫn chậm nhất theo phân vị 95, tỉ lệ lỗi theo mã trạng thái, số người dùng phân biệt, và khoảng thời gian có gai lỗi. Đối chiếu với đáp án.

**Pitfalls.** Nạp cả tệp rồi bị giết vì cạn bộ nhớ · sắp xếp mà quên đặt vị trí ngôn ngữ nên phép nối sai · dùng biểu thức chính quy tham lam khớp quá nhiều mà không phát hiện.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Năm câu trả lời khớp đáp án đối chứng, và không lệnh nào bị giết vì cạn bộ nhớ.

### Lesson 27 · Writing a shell script that fails loudly `TH`
**Prerequisites.** Lesson 26

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Script im lặng khi hỏng là chế độ hỏng nguy hiểm nhất của tự động hoá, vì nó tạo ra niềm tin sai rằng công việc đã chạy. Ba cờ bắt lỗi và đúng cái mỗi cờ bắt: dừng khi lệnh lỗi, dừng khi dùng biến chưa đặt, và lan lỗi qua chuỗi ống dẫn, cờ thứ ba chữa đúng vấn đề ở lesson 20. Bẫy dọn dẹp chạy khi thoát bất kể lý do, và cách dùng nó để xoá tệp tạm và nhả khoá. Khoá tệp để chặn hai lần chạy chồng nhau, mẫu bắt buộc cho công việc theo lịch, và là vấn đề mà công cụ điều phối ở chặng 5 giải bằng cơ chế khác. Ghi nhật ký có dấu thời gian và mã định danh lần chạy, để nối được nhật ký của một lần chạy khi nhiều lần chạy xen kẽ. Mã thoát có nghĩa và quy ước dùng dải nào. Kiểm tra điều kiện tiên quyết đầu script. Tham số hoá bằng biến môi trường có giá trị mặc định. Vì sao script quá 100 dòng nên chuyển sang Python, và tiêu chí chuyển.

**Outcome.** Viết một script theo lịch mà khi hỏng thì dừng ngay và báo, không chạy tiếp âm thầm, và không bao giờ có hai lần chạy chồng nhau.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí kiểm bằng thực nghiệm bơm lỗi. Đạt khi năm kịch bản hỏng đều làm script dừng với mã thoát khác không và ghi nhật ký nêu nguyên nhân, và khi chạy đồng thời hai lần thì lần thứ hai từ chối chạy. Script chạy đúng ở đường thuận không chứng minh được gì.

**Lab.** Viết script nạp dữ liệu có kiểm tra điều kiện tiên quyết, khoá tệp, bẫy dọn dẹp và nhật ký có mã định danh lần chạy. Bơm năm lỗi: thiếu biến môi trường, tệp nguồn không tồn tại, lệnh giữa chuỗi ống dẫn lỗi, hết dung lượng đĩa, và bị giết giữa chừng. Chạy đồng thời hai lần.

**Pitfalls.** Quên cờ lan lỗi qua chuỗi ống dẫn nên lỗi giữa chuỗi bị nuốt · dọn dẹp ở cuối script nên không chạy khi thoát sớm · khoá bằng tệp mà không xoá khi bị giết.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Năm kịch bản hỏng đều dừng với mã thoát khác không và nhật ký nêu nguyên nhân, và lần chạy thứ hai bị từ chối.

### Lesson 28 · Observing a running system - top, vmstat, iostat, ss, lsof `TH`
**Prerequisites.** Lesson 22

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bốn tài nguyên và công cụ đọc từng cái, cùng chỉ số nào trong mỗi công cụ thật sự có nghĩa. Bộ xử lý: phân tách thời gian người dùng, thời gian nhân, thời gian chờ vào ra và thời gian bị đánh cắp, trong đó chờ vào ra cao nghĩa là nghẽn đĩa chứ không phải nghẽn bộ xử lý. Bộ nhớ: phân tách dùng thật, bộ đệm, và hoán đổi, nối lại lesson 22. Đĩa: mức dùng, độ sâu hàng đợi, thời gian phục vụ, trong đó mức dùng 100% không nhất thiết là bão hoà với ổ thể rắn. Mạng: kết nối theo trạng thái, hàng đợi gửi và nhận, và số kết nối ở trạng thái chờ đóng. Liên kết ngược từ số đo về tiến trình: tệp nào đang mở, ổ cắm nào thuộc tiến trình nào. Quy trình phân loại bốn bước cho một sự cố chậm, theo thứ tự loại trừ. Nguyên tắc: ghi lại số đo trước khi sửa, vì sửa xong thì không còn bằng chứng.

**Outcome.** Phân loại một sự cố chậm về đúng một trong bốn tài nguyên bằng quy trình bốn bước, và dẫn số đo làm bằng chứng.

**Đánh giá.** Tầng *phân tích*. Objective là chẩn đoán có bằng chứng, chuẩn bị trực tiếp cho cổng. Kiểm bằng bốn ca, mỗi ca nghẽn một tài nguyên; đạt khi phân loại đúng ít nhất ba trên bốn và mỗi lần dẫn được ít nhất hai số đo độc lập. Đoán đúng mà chỉ dẫn một số đo thì tính là chưa vững.

**Lab.** Dựng bốn ca tải nghẽn bốn tài nguyên khác nhau. Với mỗi ca chạy quy trình bốn bước, ghi số đo trước khi kết luận. Lập sổ tay một trang: triệu chứng, lệnh chạy, chỉ số cần đọc, kết luận rút ra.

**Pitfalls.** Đọc mức dùng bộ xử lý tổng mà bỏ qua thời gian chờ vào ra · kết luận đĩa bão hoà từ mức dùng 100% trên ổ thể rắn · sửa trước rồi mới đo nên mất bằng chứng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân loại đúng ít nhất ba trên bốn ca, mỗi lần có ít nhất hai số đo độc lập, và nộp sổ tay một trang.

### Lesson 29 · Gate 1 - prove whether a slow pipeline is CPU, RAM, disk or network `KT`
**Prerequisites.** Lesson 28

**In-class (120 phút).** 75 phút làm bài độc lập · 45 phút chữa bài và phân tích lỗi theo nhóm

**Learn.** Không có nội dung mới. Cổng 1 của chương trình, đo năng lực chẩn đoán trên hệ thống đang chạy.

**Outcome.** Nhận bốn sự cố chưa từng thấy và chứng minh bằng số đo mỗi sự cố nghẽn ở tài nguyên nào, rồi đề xuất một thay đổi kèm dự đoán định lượng về tác động.

**Đánh giá.** Tầng *đánh giá*. Cổng đo chẩn đoán và quyết định dưới ràng buộc thời gian, không đo trí nhớ lệnh. Thang điểm: A 30đ phân loại đúng bốn ca · B 25đ bằng chứng số đo cho từng ca · C 20đ đề xuất thay đổi và dự đoán định lượng · D 15đ giải thích cơ chế phần cứng hoặc hệ điều hành đứng sau · E 10đ sổ tay đủ để người khác lặp lại. Đạt khi ≥ 70/100, phần A ≥ 50% và phần B ≥ 50%. Chẩn đoán đúng mà không có bằng chứng không được tính điểm phần A.

**Lab.** 120 phút trên bốn máy ảo, mỗi máy một sự cố cài sẵn, không có tài liệu về sự cố. Nộp cho mỗi ca: số đo thu được, kết luận, thay đổi đề xuất, dự đoán định lượng. Sau đó thực hiện thay đổi và đo lại để đối chiếu với dự đoán.

**Pitfalls.** Sửa trước khi đo · kết luận từ một chỉ số duy nhất · đề xuất thêm phần cứng mà không dự đoán được nó cải thiện bao nhiêu.

**Self-study (2,4 giờ).** Không có bài tự học. Nếu không đạt, theo phụ lục khắc phục khi không đạt cổng

**Done when.** Đạt ≥ 70/100, phần A ≥ 50% và phần B ≥ 50%.

# MODULE 4 · NETWORKING FOR DATA ENGINEERS

**Lessons 30–39 · 20 giờ**

| | |
|---|---|
| **Objective cấp module** | Chẩn đoán một lỗi kết nối hoặc một pipeline chậm vì mạng tới đúng chặng, và viết ứng dụng khách HTTP chịu được nguồn không ổn định |
| **Tiền đề** | M3 |
| **Exit criterion** | Ứng dụng khách nạp hết 100.000 bản ghi từ một API cố ý trả lỗi 20% mà không mất và không trùng bản ghi nào |
| **Kỹ năng SFIA** | `NTAS` mức 2 · `PROG` mức 3 |
| **Chế độ hỏng** | Coi mạng là thứ luôn chạy, nên viết vòng lặp gọi API không có thời gian chờ và pipeline treo vô hạn lúc nửa đêm |

Module không dạy mạng cho người quản trị hạ tầng. Nó dạy đúng phần mà một pipeline chạm tới: vì sao kết nối treo, vì sao thử lại làm hỏng thêm, và vì sao độ trễ quan trọng hơn băng thông khi nạp dữ liệu theo trang.

### Lesson 30 · Addresses, subnets, routing and DNS `LT`
**Prerequisites.** Module 4: M3

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Địa chỉ IP, mặt nạ mạng con, và cách đọc ký hiệu độ dài tiền tố. Địa chỉ riêng và địa chỉ công cộng, chuyển đổi địa chỉ mạng, và vì sao một dịch vụ chạy được trên máy cá nhân lại không truy cập được từ nơi khác. Bảng định tuyến và cổng mặc định. Phân giải tên miền: thứ tự tra cứu, bộ nhớ đệm ở nhiều tầng, và thời gian sống của bản ghi. Ba sự cố dữ liệu có gốc ở phân giải tên miền: bộ nhớ đệm giữ địa chỉ cũ sau khi dịch vụ chuyển, thời gian phân giải cộng vào độ trễ mỗi kết nối nếu không dùng lại kết nối, và một bản ghi trỏ nhiều địa chỉ làm tải phân bố không đều. Vì sao tên máy trong tệp cấu hình an toàn hơn địa chỉ IP viết cứng. Khác biệt giữa không kết nối được, hết thời gian chờ, và bị từ chối, ba triệu chứng chỉ ba nguyên nhân khác nhau.

**Outcome.** Phân biệt ba loại lỗi kết nối và truy mỗi loại về đúng chặng: phân giải tên, định tuyến, hay dịch vụ không lắng nghe.

**Đánh giá.** Tầng *phân tích*. Objective là chẩn đoán phân biệt, vì ba lỗi có thông báo gần giống nhau ở tầng ứng dụng. Kiểm bằng ba ca dựng sẵn; đạt khi định vị đúng cả ba và dẫn được lệnh kiểm chứng cho từng chặng.

**Lab.** Dựng ba ca trong máy ảo: tên miền không phân giải được, địa chỉ phân giải được nhưng không định tuyến tới, và cổng không có gì lắng nghe. Với mỗi ca, chẩn đoán theo thứ tự phân giải tên, định tuyến, cổng. Ghi lệnh kiểm chứng từng chặng.

**Pitfalls.** Kết luận dịch vụ chết khi thật ra tên miền không phân giải được · viết cứng địa chỉ IP vào cấu hình · bỏ qua bộ nhớ đệm phân giải tên khi dịch vụ vừa đổi địa chỉ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Định vị đúng cả ba ca, mỗi ca có lệnh kiểm chứng cho đúng chặng.

### Lesson 31 · TCP - handshake, retransmission and flow control `LT`
**Prerequisites.** Lesson 30

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bắt tay ba bước và chi phí thời gian của nó: một vòng khứ hồi trước khi gửi được byte dữ liệu đầu tiên. Hệ quả trực tiếp: mở kết nối mới cho mỗi yêu cầu làm nạp dữ liệu theo trang chậm gấp nhiều lần so với dùng lại kết nối. Truyền lại khi mất gói và thời gian chờ truyền lại tăng dần. Cửa sổ nhận và điều khiển luồng: bên nhận chậm làm bên gửi tự giảm tốc, cùng ý tưởng với áp lực ngược ở lesson 20. Tích băng thông và độ trễ: vì sao đường truyền băng thông cao nhưng độ trễ lớn không đạt thông lượng công bố nếu cửa sổ nhỏ. Đóng kết nối và trạng thái chờ đóng: vì sao một máy chủ vừa chịu tải lớn lại hết cổng dù không còn kết nối hoạt động. Phân biệt độ trễ với thông lượng bằng một ví dụ định lượng. Giao thức không kết nối và ba trường hợp nó hợp.

**Outcome.** Ước lượng thời gian nạp 10.000 trang dữ liệu có và không dùng lại kết nối, rồi đo và giải thích chênh lệch bằng số vòng khứ hồi.

**Đánh giá.** Tầng *áp dụng*. Objective gồm ước lượng và đối chứng bằng số đo. Đạt khi ước lượng sai trong phạm vi hệ số hai, và khi người học chỉ ra được số vòng khứ hồi của từng cách. Giải thích đúng mà không có số đo thì chưa đạt.

**Lab.** Đo độ trễ khứ hồi tới một máy chủ. Ước lượng thời gian nạp 10.000 trang theo hai cách. Viết hai ứng dụng khách: một mở kết nối mới mỗi yêu cầu, một dùng nhóm kết nối. Đo cả hai. Quan sát số kết nối ở trạng thái chờ đóng trong lúc chạy cách thứ nhất.

**Pitfalls.** Mở kết nối mới mỗi yêu cầu · so sánh hai đường truyền bằng băng thông mà bỏ qua độ trễ · không đặt giới hạn cho nhóm kết nối nên mở quá nhiều.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ước lượng sai trong phạm vi hệ số hai, và số kết nối ở trạng thái chờ đóng quan sát được ở cách không dùng lại kết nối.

### Lesson 32 · TLS, certificates and the errors they produce `TH`
**Prerequisites.** Lesson 31

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Mã hoá khi truyền và ba thứ nó bảo đảm: bí mật, toàn vẹn, và xác thực danh tính máy chủ. Chuỗi chứng chỉ và cơ quan cấp gốc. Bốn lỗi chứng chỉ thường gặp và nguyên nhân từng cái: hết hạn, tên không khớp, chuỗi không đầy đủ, và cơ quan cấp không được tin. Vì sao tắt kiểm chứng chứng chỉ là cách sửa sai và nó mở ra tấn công xen giữa. Kho chứng chỉ tin cậy của hệ thống và của môi trường chạy ngôn ngữ, hai kho khác nhau nên một chương trình báo lỗi trong khi trình duyệt vẫn vào được. Chứng chỉ phía khách cho xác thực hai chiều, mẫu gặp khi nối tới hệ thống ngân hàng. Chi phí bắt tay mã hoá cộng thêm vào bắt tay kết nối, và lý do dùng lại kết nối còn quan trọng hơn. Thời điểm hệ thống sai làm chứng chỉ trông như chưa hiệu lực, một lỗi hay gặp trong vùng chứa.

**Outcome.** Chẩn đoán bốn lỗi chứng chỉ về đúng nguyên nhân và sửa đúng chỗ, không sửa bằng cách tắt kiểm chứng.

**Đánh giá.** Tầng *phân tích*. Objective là chẩn đoán phân biệt với một đáp án sai hấp dẫn là tắt kiểm chứng. Kiểm bằng bốn ca; đạt khi định vị đúng cả bốn và không ca nào được sửa bằng cách tắt kiểm chứng. Một ca sửa bằng tắt kiểm chứng thì cả bài không đạt.

**Lab.** Dựng bốn ca lỗi chứng chỉ bằng máy chủ cục bộ. Với mỗi ca đọc chuỗi chứng chỉ, định vị nguyên nhân, sửa đúng chỗ. Thêm một ca đồng hồ hệ thống lệch một năm và quan sát triệu chứng.

**Pitfalls.** Tắt kiểm chứng chứng chỉ để cho chạy · thêm chứng chỉ vào kho hệ thống trong khi môi trường chạy dùng kho riêng · bỏ qua chứng chỉ trung gian nên chuỗi đứt.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Định vị đúng cả bốn nguyên nhân, và không ca nào sửa bằng cách tắt kiểm chứng.

### Lesson 33 · HTTP - methods, status codes and what they mean for a loader `TH`
**Prerequisites.** Lesson 32

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Cấu trúc một yêu cầu và một phản hồi. Phương thức và tính bất biến khi lặp lại: phương thức nào lặp lại an toàn, phương thức nào không, và vì sao điều đó quyết định phương thức nào thử lại được. Nhóm mã trạng thái và hành động đúng cho từng nhóm khi nạp dữ liệu: chuyển hướng phải theo hay không, lỗi phía khách không được thử lại vì thử lại cũng lỗi, lỗi phía máy chủ thử lại được, và riêng mã quá nhiều yêu cầu phải tôn trọng tiêu đề nói chờ bao lâu. Ba lỗi khác nhau bị gộp thành một trong nhiều ứng dụng khách: kết nối hỏng, hết thời gian chờ, và máy chủ trả lỗi. Tiêu đề quan trọng cho nạp dữ liệu: kiểu nội dung, nén, phân trang, giới hạn tốc độ, và định danh yêu cầu để truy vết. Nén khi truyền và đánh đổi giữa bộ xử lý với băng thông. Tải theo dòng thay vì tải hết vào bộ nhớ, bắt buộc khi phản hồi lớn hơn bộ nhớ.

**Outcome.** Phân loại 12 mã trạng thái và loại lỗi thành thử lại được hay không, và cài đặt xử lý đúng cho từng nhóm.

**Đánh giá.** Tầng *áp dụng*. Objective gồm một phép phân loại có đáp án và một cài đặt kiểm được. Đạt khi bảng phân loại đúng ít nhất 10 trên 12, và khi ứng dụng khách xử lý đúng cả ba nhóm trong thực nghiệm bơm lỗi. Phân loại đúng mà cài đặt thử lại cả lỗi phía khách thì không đạt.

**Lab.** Dựng một máy chủ giả trả về 12 tình huống: các mã trạng thái, kết nối bị ngắt giữa chừng, và phản hồi chậm hơn thời gian chờ. Viết ứng dụng khách phân loại và xử lý đúng từng cái. Ghi nhật ký phân loại cho mỗi lần gọi.

**Pitfalls.** Thử lại lỗi phía khách · bỏ qua tiêu đề chờ bao lâu rồi bị chặn · tải hết phản hồi vào bộ nhớ khi nó lớn hơn RAM.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng phân loại đúng ít nhất 10 trên 12, và ứng dụng khách xử lý đúng cả ba nhóm trong thực nghiệm.

### Lesson 34 · Timeouts, retries, backoff and jitter `TH`
**Prerequisites.** Lesson 33

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Không đặt thời gian chờ là lỗi thiết kế phổ biến nhất trong mã nạp dữ liệu, vì mặc định của nhiều thư viện là chờ vô hạn. Bốn loại thời gian chờ và cái nào chặn cái nào: chờ kết nối, chờ byte đầu, chờ giữa hai byte, và chờ toàn bộ yêu cầu. Chỉ đặt loại đầu là chưa đủ, vì kết nối mở được rồi máy chủ vẫn treo. Thử lại với khoảng chờ tăng theo cấp số nhân và lý do cộng thêm nhiễu ngẫu nhiên: không có nhiễu thì mọi ứng dụng khách thử lại cùng lúc và tạo bão tải, làm dịch vụ vừa hồi phục lại sập. Ngân sách thử lại và giới hạn trên tổng thời gian. Cầu dao: sau bao nhiêu lỗi liên tiếp thì ngừng gọi, chờ bao lâu rồi thử nửa vời. Khoá bất biến để máy chủ nhận ra yêu cầu lặp và không xử lý hai lần, cơ chế bắt buộc khi thử lại phương thức không bất biến. Vì sao thử lại không điều kiện gây cả bão tải lẫn bản ghi trùng, hai hậu quả cùng lúc.

**Outcome.** Viết ứng dụng khách có đủ bốn loại thời gian chờ, thử lại có nhiễu và khoá bất biến, rồi chứng minh nó không sinh bản ghi trùng khi máy chủ lỗi 20%.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí đúng sai tuyệt đối kiểm bằng đối soát. Đạt khi nạp hết 100.000 bản ghi từ máy chủ lỗi 20%, số bản ghi đích bằng đúng số nguồn, không trùng và không thiếu. Chạy xong mà lệch một bản ghi là không đạt.

**Lab.** Dựng máy chủ giả lỗi 20% gồm cả treo không phản hồi. Viết ứng dụng khách nạp 100.000 bản ghi. Đối soát số bản ghi. Sau đó tắt nhiễu ngẫu nhiên và chạy 50 ứng dụng khách cùng lúc, quan sát bão tải.

**Pitfalls.** Chỉ đặt thời gian chờ kết nối · thử lại không có nhiễu · thử lại phương thức không bất biến mà không có khoá bất biến.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Nạp hết 100.000 bản ghi từ máy chủ lỗi 20%, đối soát khớp tuyệt đối, và quan sát được bão tải khi tắt nhiễu.

### Lesson 35 · Pagination, rate limits and resumable loading `TH`
**Prerequisites.** Lesson 34

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba kiểu phân trang và đánh đổi: theo số trang đơn giản nhưng sai khi dữ liệu thay đổi giữa chừng, theo con trỏ ổn định hơn, theo khoảng thời gian phù hợp cho nạp gia tăng. Cơ chế bỏ sót và lặp bản ghi khi dùng phân trang theo số trang trên tập đang được ghi thêm, một lỗi âm thầm vì tổng số vẫn trông hợp lý. Giới hạn tốc độ: theo cửa sổ cố định, theo cửa sổ trượt, và theo xô thẻ, cùng cách đọc tiêu đề còn lại bao nhiêu lượt. Tự giới hạn phía khách thay vì chờ bị chặn. Điểm kiểm tra để nạp lại được từ chỗ dừng: lưu gì, lưu lúc nào, và vì sao lưu sau khi ghi dữ liệu chứ không trước. Nối lại lesson 21: bị giết giữa chừng là ca kiểm thử bắt buộc. Nạp song song nhiều trang và điều kiện an toàn. Phát hiện lược đồ nguồn đổi giữa lúc đang nạp.

**Outcome.** Nạp một tập dữ liệu có phân trang mà nguồn vẫn đang được ghi thêm, và chứng minh không bỏ sót không lặp bản ghi nào.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí đối soát tuyệt đối trên một tình huống khó. Đạt khi tập đích khớp với tập nguồn tại thời điểm chốt, không thiếu không trùng, và khi giết tiến trình giữa chừng rồi chạy lại vẫn ra kết quả đó.

**Lab.** Dựng API có phân trang trên bảng đang được ghi thêm 100 bản ghi mỗi giây. Nạp bằng phân trang theo số trang, đối soát và ghi lại số bỏ sót. Đổi sang phân trang theo con trỏ, đối soát lại. Giết tiến trình ba lần giữa chừng và chạy lại từ điểm kiểm tra.

**Pitfalls.** Dùng phân trang theo số trang trên tập đang thay đổi · lưu điểm kiểm tra trước khi ghi dữ liệu · chạy song song nhiều trang mà không kiểm tra thứ tự con trỏ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tập đích khớp tuyệt đối với nguồn tại thời điểm chốt, và ba lần giết giữa chừng đều chạy lại ra đúng kết quả đó.

### Lesson 36 · Connection pools, load balancers and proxies `LT`
**Prerequisites.** Lesson 31

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Nhóm kết nối giữ sẵn kết nối đã mở để tránh chi phí bắt tay ở lesson 31. Ba tham số và hậu quả khi đặt sai: kích thước tối đa, thời gian sống của kết nối, và thời gian chờ lấy kết nối từ nhóm. Nhóm quá nhỏ làm yêu cầu xếp hàng, nhóm quá lớn làm phía máy chủ hết kết nối, và đây là bài toán giống hệt giới hạn song song ở lesson 12. Kết nối chết trong nhóm: cơ chế một kết nối bị phía kia đóng mà phía này không biết, và cách phát hiện bằng phép kiểm trước khi dùng. Bộ cân bằng tải ở hai tầng và hệ quả khác nhau của từng tầng lên kết nối bền. Vì sao bộ cân bằng tải làm một yêu cầu dài bị ngắt sau thời gian chờ rỗi, một nguyên nhân phổ biến của lỗi kết nối bị đặt lại trong công việc chạy lâu. Máy chủ trung gian và cách nó đổi tiêu đề. Gắn phiên theo máy chủ và vì sao nó thường là dấu hiệu thiết kế có trạng thái.

**Outcome.** Chọn kích thước nhóm kết nối cho một tải cho trước bằng thực nghiệm, và giải thích vì sao một công việc chạy lâu bị ngắt kết nối giữa chừng.

**Đánh giá.** Tầng *phân tích*. Objective gồm một quyết định có số đo và một chẩn đoán. Kiểm bằng bảng thực nghiệm ít nhất bốn kích thước nhóm, cộng một ca công việc dài bị ngắt. Đạt khi chọn được kích thước cho thông lượng cao nhất và giải thích đúng nguyên nhân ca bị ngắt.

**Lab.** Chạy một tải truy vấn ở bốn kích thước nhóm kết nối, đo thông lượng và độ trễ phân vị 95. Sau đó dựng một máy chủ trung gian có thời gian chờ rỗi 60 giây, chạy một truy vấn 5 phút, quan sát kết nối bị đặt lại và tìm cách xử lý.

**Pitfalls.** Đặt nhóm kết nối lớn cho chắc · không kiểm kết nối trước khi dùng nên gặp kết nối chết · đổ lỗi cho cơ sở dữ liệu khi máy chủ trung gian mới là thứ ngắt.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng bốn kích thước nhóm có thông lượng và độ trễ, và ca công việc dài bị ngắt được giải thích đúng nguyên nhân.

### Lesson 37 · Latency against throughput, and where data pipelines pay `LT`
**Prerequisites.** Lesson 36

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Hai đại lượng và vì sao tối ưu cái này thường làm xấu cái kia. Độ trễ cộng dồn theo số vòng khứ hồi, nên một pipeline gọi API 10.000 lần tuần tự bị chi phối bởi độ trễ chứ không bởi băng thông, dù tổng dữ liệu nhỏ. Thông lượng bị chi phối bởi băng thông khi chuyển khối lớn. Cách nhận ra mình đang ở chế độ nào: nhân số yêu cầu với độ trễ khứ hồi và so với thời gian chạy thật. Bốn đòn bẩy giảm độ trễ tổng theo thứ tự hiệu quả: gộp nhiều bản ghi vào một yêu cầu, chạy song song, dùng lại kết nối, và đặt máy tính gần nguồn dữ liệu. Vì sao gộp gần như luôn thắng chạy song song khi nguồn có giới hạn tốc độ. Chi phí truyền dữ liệu giữa các vùng và giữa các nhà cung cấp, một khoản đắt bất ngờ ở chặng 7. Độ trễ của lưu trữ đối tượng so với đĩa cục bộ, nối lại lesson 15, và hệ quả lên thiết kế đọc nhiều tệp nhỏ.

**Outcome.** Xác định một pipeline đang bị chi phối bởi độ trễ hay bởi băng thông, và chọn đòn bẩy phù hợp kèm dự đoán định lượng.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn giữa các phương án và biện minh bằng số, không có đáp án chung. Kiểm bằng hai pipeline, một mỗi chế độ; đạt khi phân loại đúng cả hai, chọn đòn bẩy phù hợp, và dự đoán cải thiện sai trong phạm vi hệ số hai so với kết quả sau khi áp dụng.

**Lab.** Nhận hai pipeline: một gọi API 10.000 lần lấy ít dữ liệu, một tải 50 ghi ga byte trong ít lần gọi. Đo và phân loại từng cái. Chọn đòn bẩy, dự đoán cải thiện, áp dụng, đo lại, so với dự đoán.

**Pitfalls.** Tăng băng thông cho pipeline bị chi phối bởi độ trễ · chạy song song trong khi nguồn có giới hạn tốc độ · bỏ qua chi phí truyền dữ liệu giữa các vùng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân loại đúng cả hai pipeline, và dự đoán cải thiện sai trong phạm vi hệ số hai so với số đo sau khi áp dụng.

### Lesson 38 · Observing the network - ss, tcpdump and reading a capture `TH`
**Prerequisites.** Lesson 37

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Đọc bảng kết nối theo trạng thái và ý nghĩa vận hành của từng trạng thái, nối lại lesson 28. Hàng đợi gửi và hàng đợi nhận: hàng đợi gửi lớn nghĩa là phía kia đọc chậm, hàng đợi nhận lớn nghĩa là ứng dụng của mình đọc chậm, và phân biệt này quyết định sửa ở đâu. Số kết nối ở trạng thái chờ đóng và giới hạn cổng tạm. Bắt gói tin ở mức đủ dùng: lọc theo máy và cổng, lưu ra tệp, và đọc lại. Bốn thứ nhìn ra được từ một bản bắt gói: bắt tay có thành công không, byte đầu tiên về sau bao lâu, có truyền lại không, và ai đóng kết nối trước. Nguyên tắc bảo mật: bản bắt gói chứa dữ liệu thật nên phải xử lý như dữ liệu nhạy cảm, và không bao giờ nộp vào kho mã. Khi nào cần bắt gói và khi nào nhật ký ứng dụng đã đủ, vì bắt gói tốn công và thường không cần.

**Outcome.** Đọc một bản bắt gói và xác định ai đóng kết nối trước cùng byte đầu tiên về sau bao lâu, rồi kết luận lỗi nằm ở phía khách hay phía máy chủ.

**Đánh giá.** Tầng *phân tích*. Objective là rút kết luận từ bằng chứng ở mức gói tin. Kiểm bằng ba bản bắt gói dựng sẵn: một máy chủ đóng trước, một khách hết thời gian chờ, một mất gói gây truyền lại. Đạt khi kết luận đúng cả ba và dẫn được gói cụ thể làm bằng chứng.

**Lab.** Dựng ba ca và bắt gói cho từng ca. Đọc lại, với mỗi ca xác định bốn thứ nêu trong bài và kết luận phía nào gây lỗi. Sau đó đọc bảng kết nối của một máy đang chịu tải và phân biệt hàng đợi gửi với hàng đợi nhận.

**Pitfalls.** Bắt gói trên mọi giao diện không lọc rồi tệp quá lớn · nộp bản bắt gói có dữ liệu thật vào kho mã · kết luận từ nhật ký ứng dụng khi hai phía nói hai chuyện khác nhau.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Kết luận đúng cả ba bản bắt gói với gói cụ thể làm bằng chứng, và phân biệt đúng hai loại hàng đợi trên máy có tải.

### Lesson 39 · Building a resilient HTTP loader `TH`
**Prerequisites.** Lesson 38

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Không có cơ chế mới. Bài gộp: ghép mọi thứ từ lesson 33 tới 38 thành một thành phần dùng lại được trong cả chương trình. Danh mục bắt buộc của một ứng dụng khách nạp dữ liệu: bốn loại thời gian chờ, thử lại có nhiễu và ngân sách, cầu dao, khoá bất biến, tự giới hạn tốc độ, nhóm kết nối có kiểm kết nối chết, phân trang theo con trỏ, điểm kiểm tra nạp lại được, nhật ký có định danh yêu cầu, và số đo phát ra ngoài. Tách cấu hình khỏi mã. Kiểm thử một ứng dụng khách mạng mà không phụ thuộc mạng thật: máy chủ giả có thể bơm từng loại lỗi. Vì sao kiểm thử chỉ với đường thuận không chứng minh gì, nối lại nguyên tắc ở lesson 27.

**Outcome.** Đóng gói một ứng dụng khách HTTP có đủ 10 mục trong danh mục, và chứng minh bằng bộ kiểm thử bơm lỗi rằng nó không mất và không trùng bản ghi.

**Đánh giá.** Tầng *sáng tạo*. Objective là thiết kế một thành phần dưới ràng buộc cho trước, không phải làm theo mẫu. Kiểm bằng hai lớp: bộ kiểm thử bơm đủ tám loại lỗi phải xanh, và đối soát 100.000 bản ghi phải khớp tuyệt đối. Thiếu một mục trong danh mục mà vẫn qua kiểm thử thì phải giải thích được vì sao mục đó không cần cho ca này.

**Lab.** Đóng gói ứng dụng khách thành một mô đun dùng lại được. Viết bộ kiểm thử với máy chủ giả bơm tám loại lỗi: các mã trạng thái, treo, ngắt giữa chừng, giới hạn tốc độ, lược đồ đổi, và trang trùng. Nạp 100.000 bản ghi, đối soát. Giao mô đun cho học viên khác dùng cho nguồn khác.

**Pitfalls.** Kiểm thử bằng cách gọi API thật · gộp cấu hình vào mã · coi bộ kiểm thử xanh ở đường thuận là đủ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bộ kiểm thử tám loại lỗi xanh, đối soát 100.000 bản ghi khớp tuyệt đối, và học viên khác dùng lại được cho nguồn khác.

# MODULE 5 · ALGORITHMS AND DATA STRUCTURES FOR DATA WORK

**Lessons 40–49 · 20 giờ**

| | |
|---|---|
| **Objective cấp module** | Chọn cấu trúc dữ liệu và thuật toán cho một bài toán dữ liệu theo chi phí thật đo được, không theo độ phức tạp tiệm cận một mình |
| **Tiền đề** | M2 |
| **Exit criterion** | Giải năm bài toán dữ liệu kinh điển trên tập lớn hơn bộ nhớ, mỗi bài nêu được độ phức tạp và chi phí thật đã đo |
| **Kỹ năng SFIA** | `PROG` mức 3 |
| **Chế độ hỏng** | Học độ phức tạp tiệm cận như một môn thi, nên chọn cấu trúc theo lý thuyết rồi ngạc nhiên vì mảng thắng danh sách liên kết |

Module không dạy thuật toán cho phỏng vấn. Mọi bài đều gắn với một thao tác dữ liệu thật: khử trùng, lấy N cao nhất, kết bảng, phân trang, và sắp xếp dữ liệu lớn hơn bộ nhớ. Mỗi lựa chọn phải đo, vì hằng số và cục bộ bộ nhớ đệm ở lesson 11 thường lật ngược kết luận từ độ phức tạp tiệm cận.

### Lesson 40 · Big-O and why it is not the whole cost `LT`
**Prerequisites.** Module 5: M2

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Độ phức tạp tiệm cận nói tốc độ tăng khi dữ liệu lớn dần, không nói thời gian chạy. Hằng số ẩn và vì sao một thuật toán bậc n log n có hằng số nhỏ thắng một thuật toán bậc n có hằng số lớn trên mọi kích thước thực tế. Cục bộ bộ nhớ đệm là hằng số lớn nhất trong công việc dữ liệu, nối lại lesson 11: duyệt mảng bậc n nhanh hơn duyệt danh sách liên kết bậc n nhiều lần. Phân tích khấu hao và ví dụ mảng động. Độ phức tạp bộ nhớ và đánh đổi giữa thời gian với bộ nhớ. Trường hợp trung bình so với trường hợp xấu nhất, và vì sao trường hợp xấu nhất quan trọng khi dữ liệu do người ngoài kiểm soát. Quy trình chọn: ước lượng bằng độ phức tạp để loại phương án tệ hẳn, rồi đo hai ba phương án còn lại trên dữ liệu thật. Nguyên tắc không tối ưu khi chưa đo, nối lại lesson 17.

**Outcome.** Dự đoán thứ hạng thời gian chạy của ba cài đặt bằng độ phức tạp, rồi đo và giải thích chỗ dự đoán sai bằng hằng số hoặc cục bộ bộ nhớ đệm.

**Đánh giá.** Tầng *phân tích*. Objective đòi giải thích chênh lệch giữa lý thuyết và số đo, không chỉ đo. Kiểm bằng ba cài đặt cùng bài toán ở bốn kích thước dữ liệu; đạt khi có số đo đầy đủ và khi giải thích được ít nhất một chỗ thứ hạng thực tế khác thứ hạng lý thuyết.

**Lab.** Cài ba cách tìm phần tử trong tập: quét mảng tuyến tính, tìm nhị phân trên mảng đã sắp, và tra từ điển băm. Dự đoán thứ hạng. Đo ở bốn kích thước từ 100 tới 10 triệu phần tử. Giải thích chỗ quét tuyến tính thắng trên tập nhỏ.

**Pitfalls.** Chọn cấu trúc chỉ bằng độ phức tạp tiệm cận · đo một kích thước rồi kết luận · bỏ qua chi phí dựng chỉ mục khi so tra cứu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Có số đo ba cài đặt ở bốn kích thước, và giải thích được ít nhất một chỗ thứ hạng thực tế khác lý thuyết.

### Lesson 41 · Arrays, lists and the memory layout that decides speed `TH`
**Prerequisites.** Lesson 40

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Mảng lưu liên tục nên duyệt tuần tự tận dụng dòng bộ nhớ đệm và đọc trước; danh sách liên kết lưu rải rác nên mỗi bước là một lần nhảy bộ nhớ. Hệ quả đo được: duyệt danh sách liên kết chậm hơn duyệt mảng nhiều lần dù cùng bậc. Chèn và xoá: danh sách liên kết rẻ về lý thuyết nhưng tìm tới vị trí đã tốn bậc n. Mảng động và chi phí cấp phát lại, phân tích khấu hao. Bố trí theo dòng so với bố trí theo cột cho một tập bản ghi: cùng dữ liệu, hai bố trí, và phép gộp trên một cột nhanh hơn hẳn ở bố trí theo cột. Đây là nền của định dạng cột ở chặng 7 và của lý do kho phân tích dùng lưu trữ theo cột, nối lại lesson 11. Mảng có kiểu so với mảng đối tượng trong ngôn ngữ động, và hệ số phình ở lesson 13. Lát cắt và bản sao ẩn.

**Outcome.** Đo chênh lệch giữa bố trí theo dòng và theo cột cho một phép gộp trên một cột, và giải thích bằng dòng bộ nhớ đệm.

**Đánh giá.** Tầng *phân tích*. Objective nối một số đo với cơ chế đã học ở lesson 11. Đạt khi có số đo cho cả hai bố trí ở ít nhất ba kích thước, và khi người học ước lượng được số dòng bộ nhớ đệm phải nạp cho mỗi bố trí rồi so với chênh lệch đo được.

**Lab.** Lưu một triệu bản ghi 20 cột theo hai bố trí. Gộp trên một cột. Đo cả hai ở ba kích thước. Ước lượng số dòng bộ nhớ đệm phải nạp cho từng bố trí, so với chênh lệch thời gian. Lặp lại với phép lọc nhiều cột và quan sát chênh lệch thu hẹp.

**Pitfalls.** Dùng danh sách liên kết vì chèn rẻ mà quên chi phí tìm vị trí · so hai bố trí bằng một phép gộp rồi kết luận cột luôn thắng · quên bản sao ẩn khi cắt lát.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Số đo hai bố trí ở ba kích thước, và ước lượng số dòng bộ nhớ đệm nhất quán với chênh lệch đo được.

### Lesson 42 · Hash maps - the workhorse, and where they break `TH`
**Prerequisites.** Lesson 41

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hàm băm, xô, và hệ số tải. Xung đột và hai cách xử lý: nối chuỗi và dò tuyến tính, cùng đặc tính bộ nhớ đệm khác nhau của chúng. Cấp phát lại khi hệ số tải vượt ngưỡng, và vì sao chèn một triệu phần tử có vài lần dừng dài thay vì chậm đều. Khai báo trước dung lượng để tránh cấp phát lại, một tối ưu rẻ và hay bị bỏ qua. Trường hợp xấu nhất bậc n khi khoá bị chọn ác ý hoặc khi hàm băm kém, và hậu quả bảo mật. Chi phí bộ nhớ thật của một từ điển so với dữ liệu thuần, nối lại lesson 13. Khoá phải bất biến và vì sao dùng đối tượng thay đổi được làm khoá là lỗi. Ứng dụng trong công việc dữ liệu: khử trùng theo khoá, kết bảng bằng băm, và đếm giá trị phân biệt. Kết bằng băm: dựng bảng băm từ bảng nhỏ rồi quét bảng lớn, và điều kiện bảng nhỏ phải vừa bộ nhớ, nối tới lesson 44.

**Outcome.** Cài khử trùng một tập 50 triệu bản ghi bằng bảng băm, đo bộ nhớ đỉnh, và chỉ ra ngưỡng kích thước mà cách này không còn vừa bộ nhớ.

**Đánh giá.** Tầng *áp dụng*. Objective gồm một cài đặt và một phép xác định ngưỡng bằng đo. Đạt khi khử trùng đúng so với đáp án và khi ngưỡng nêu ra được kiểm chứng bằng một lần chạy vượt ngưỡng cho thấy tiến trình bị giết vì cạn bộ nhớ.

**Lab.** Khử trùng 50 triệu bản ghi bằng từ điển băm. Đo bộ nhớ đỉnh và thời gian, có và không khai báo trước dung lượng. Ước lượng ngưỡng vỡ bộ nhớ, rồi chạy vượt ngưỡng để kiểm chứng. Quan sát các lần dừng do cấp phát lại.

**Pitfalls.** Không khai báo trước dung lượng nên cấp phát lại nhiều lần · giả định từ điển luôn vừa bộ nhớ · dùng đối tượng thay đổi được làm khoá.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Khử trùng đúng so với đáp án, có số đo bộ nhớ đỉnh, và ngưỡng vỡ bộ nhớ được kiểm chứng bằng một lần chạy thật.

### Lesson 43 · Sorting, external sort and why it shows up everywhere `TH`
**Prerequisites.** Lesson 42

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Sắp xếp là nền của nhiều thao tác dữ liệu: khử trùng, kết theo thứ tự, gộp nhóm, và phân trang ổn định. Sắp xếp ổn định và vì sao nó cần khi sắp nhiều khoá lần lượt. Sắp xếp so sánh có cận dưới n log n, và các thuật toán không so sánh vượt cận đó với điều kiện nào. Sắp xếp ngoài bộ nhớ cho dữ liệu lớn hơn RAM: chia thành mảnh vừa bộ nhớ, sắp từng mảnh, ghi ra đĩa, rồi trộn nhiều đường. Số đường trộn và đánh đổi với số lần đọc ghi đĩa. Đây chính là cơ chế công cụ dòng lệnh ở lesson 26 dùng và là cơ chế Spark dùng khi tràn ra đĩa ở chặng 7, nên hiểu ở đây thì ở đó không phải học lại. Ước lượng số byte đọc ghi cho một lần sắp ngoài. Phân trang ổn định cần khoá sắp duy nhất, nếu không thì bản ghi nhảy giữa các trang, nối lại lesson 35.

**Outcome.** Cài sắp xếp ngoài cho một tệp lớn hơn bộ nhớ và ước lượng số byte đọc ghi trước khi chạy, rồi đo.

**Đánh giá.** Tầng *áp dụng*. Objective gồm cài đặt và ước lượng đối chứng. Đạt khi tệp kết quả sắp đúng hoàn toàn, chạy trên máy giới hạn bộ nhớ nhỏ hơn tệp, và ước lượng số byte đọc ghi sai trong phạm vi hệ số hai so với số đo.

**Lab.** Sắp một tệp 20 ghi ga byte trên máy giới hạn 2 ghi ga byte bộ nhớ. Ước lượng số byte đọc ghi trước. Cài chia mảnh và trộn nhiều đường. Đo số byte thật. Thử ba số đường trộn khác nhau và so tổng thời gian.

**Pitfalls.** Nạp cả tệp rồi bị giết · trộn hai đường nên đọc ghi nhiều lần không cần thiết · phân trang theo khoá không duy nhất nên bản ghi nhảy trang.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tệp kết quả sắp đúng hoàn toàn trên máy có bộ nhớ nhỏ hơn tệp, và ước lượng byte đọc ghi sai trong phạm vi hệ số hai.

### Lesson 44 · Join algorithms - nested loop, hash join, sort-merge join `LT`
**Prerequisites.** Lesson 43

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Ba thuật toán kết và điều kiện mỗi cái thắng. Vòng lặp lồng bậc tích hai bảng, chỉ hợp khi một bảng rất nhỏ hoặc có chỉ mục trên bảng trong. Kết bằng băm dựng bảng băm từ bảng nhỏ rồi quét bảng lớn, nhanh nhất khi bảng nhỏ vừa bộ nhớ, và tràn ra đĩa khi không vừa, đây là cơ chế đứng sau tiêu chí ra của M2. Kết trộn sắp yêu cầu cả hai bên đã sắp theo khoá, rẻ khi dữ liệu vốn đã sắp hoặc đã phân vùng theo khoá. Phát tán bảng nhỏ tới mọi nút trong hệ phân tán và ngưỡng kích thước để làm việc đó, nối tới chặng 7. Lệch khoá: một giá trị khoá chiếm phần lớn bản ghi làm một nút hoặc một xô nhận hết việc, và ba cách xử lý. Nhân bản dòng khi khoá không duy nhất ở một bên, nối tới chặng 3. Ước lượng số bản ghi kết quả trước khi chạy từ bản số quan hệ.

**Outcome.** Chọn thuật toán kết cho ba tình huống có ràng buộc khác nhau và biện minh bằng kích thước bảng, bộ nhớ sẵn có và trạng thái sắp xếp.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn giữa ba phương án và biện minh, không có đáp án chung. Kiểm bằng ba tình huống cho trước; đạt khi mỗi lựa chọn nêu được điều kiện quyết định và khi dự đoán thuật toán nào nhanh hơn được xác nhận bằng một lần chạy thật cho ít nhất hai tình huống.

**Lab.** Cài cả ba thuật toán kết. Chạy trên ba tình huống: bảng nhỏ với bảng lớn vừa bộ nhớ, hai bảng lớn đã sắp, và hai bảng lớn chưa sắp. Đo cả ba thuật toán trên cả ba tình huống, lập bảng chín ô. Tạo lệch khoá và quan sát.

**Pitfalls.** Dùng kết bằng băm khi bảng nhỏ không vừa bộ nhớ · bỏ qua lệch khoá nên một xô nhận hết việc · không ước lượng số dòng kết quả trước khi chạy.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng chín ô có số đo đầy đủ, và dự đoán thuật toán nhanh hơn đúng cho ít nhất hai trong ba tình huống.

### Lesson 45 · Heaps, top-K and streaming selection `TH`
**Prerequisites.** Lesson 42

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Đống nhị phân và hai thao tác cơ bản với chi phí log n. Bài toán lấy N cao nhất từ một luồng: giữ đống kích thước N thay vì sắp toàn bộ, và so sánh chi phí n log N với n log n khi N nhỏ hơn n rất nhiều. Điều kiện cách này thắng và điểm hoà. Hàng đợi ưu tiên cho lập lịch công việc, mẫu dùng lại ở chặng 5. Lấy N cao nhất theo nhóm và cách làm khi số nhóm lớn. Phân vị trên luồng không giữ được toàn bộ dữ liệu: vì sao phân vị chính xác cần toàn bộ dữ liệu, và các cấu trúc tóm tắt cho phân vị xấp xỉ với sai số có cận. Nối tới chặng 4 và 6: chỉ số phân vị 95 trên bảng điều khiển thường là xấp xỉ, và biết nó xấp xỉ là điều kiện để đọc đúng. Đếm giá trị phân biệt xấp xỉ và đánh đổi bộ nhớ với sai số.

**Outcome.** Cài lấy N cao nhất bằng đống trên một luồng lớn hơn bộ nhớ, và xác định bằng thực nghiệm điểm hoà so với cách sắp toàn bộ.

**Đánh giá.** Tầng *áp dụng*. Objective gồm cài đặt và xác định một ngưỡng bằng đo. Đạt khi kết quả đúng so với đáp án và khi điểm hoà nêu ra được xác nhận bằng bảng số đo ở ít nhất bốn giá trị N.

**Lab.** Lấy 100 bản ghi lớn nhất từ một luồng 100 triệu bản ghi bằng đống, bộ nhớ giới hạn. So với cách sắp toàn bộ. Chạy ở bốn giá trị N: 10, 1.000, 100.000, 10 triệu. Xác định điểm hoà. Cài thêm phân vị xấp xỉ và đo sai số so với phân vị chính xác.

**Pitfalls.** Sắp toàn bộ để lấy 10 phần tử lớn nhất · giữ đống kích thước N khi N gần bằng n · báo cáo phân vị xấp xỉ như phân vị chính xác.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Kết quả đúng so với đáp án, và điểm hoà được xác nhận bằng bảng số đo ở bốn giá trị N.

### Lesson 46 · Trees, B-trees and why databases use them `LT`
**Prerequisites.** Lesson 45

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Cây tìm kiếm nhị phân và vấn đề mất cân bằng. Cây B và cây B cộng: nút chứa nhiều khoá để mỗi lần đọc nút lấy về một khối đĩa đầy, nên chiều cao cây rất thấp và số lần chạm đĩa ít. Đây là lý do cây B là cấu trúc chỉ mục mặc định của cơ sở dữ liệu quan hệ, và là nền cho chặng 3. Lá nối nhau trong cây B cộng cho phép quét theo khoảng hiệu quả. Chi phí ghi: mỗi lần chèn phải cập nhật chỉ mục, và nhiều chỉ mục nhân chi phí ghi lên, đây là vế thứ hai của tiêu chí ra M2. Tách và gộp nút, và phình chỉ mục. Cây trộn có cấu trúc nhật ký: ghi vào bộ nhớ rồi xả ra đĩa theo tầng, tối ưu cho ghi nhiều, và khuếch đại đọc đổi lấy khuếch đại ghi thấp. Bảng đối chiếu hai họ cấu trúc theo tải ghi nhiều hay đọc nhiều, nền cho việc chọn cơ sở dữ liệu ở chặng 3.

**Outcome.** Giải thích vì sao thêm chỉ mục làm truy vấn nhanh lên mà làm ghi chậm đi, bằng số lần chạm đĩa cho mỗi thao tác.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết đặt nền cho chặng 3, người học chưa có cơ sở dữ liệu để đo sâu, nên objective dừng ở giải thích bằng cơ chế. Kiểm bằng bài ước lượng số lần chạm đĩa cho bốn thao tác trên cây B với chiều cao cho trước, cộng một thực nghiệm nhỏ. Đạt khi ước lượng đúng cả bốn.

**Lab.** Tính chiều cao cây B cho một tỉ khoá với hệ số nhánh cho trước. Ước lượng số lần chạm đĩa cho bốn thao tác: tìm một khoá, quét khoảng, chèn không tách nút, chèn có tách nút. Cài một cây B đơn giản, đếm số lần truy cập nút thật, so với ước lượng.

**Pitfalls.** Cho rằng cây nhị phân và cây B khác nhau về độ phức tạp · thêm chỉ mục cho mọi cột · bỏ qua chi phí ghi khi thiết kế chỉ mục.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ước lượng đúng số lần chạm đĩa cho cả bốn thao tác, xác nhận bằng số đếm từ cài đặt thật.

### Lesson 47 · Bloom filters, sketches and bounded-error answers `TH`
**Prerequisites.** Lesson 42

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bộ lọc Bloom trả lời câu hỏi phần tử này có trong tập không với hai tính chất bất đối xứng: không bao giờ báo thiếu, nhưng có thể báo thừa với xác suất tính được. Hệ quả sử dụng: dùng nó để loại nhanh trường hợp chắc chắn không có, rồi mới tra nguồn thật cho phần còn lại. Ba tham số và quan hệ giữa chúng: số phần tử, số bit, tỉ lệ báo thừa. Tính số bit cần cho một tỉ lệ báo thừa mục tiêu. Ba chỗ nó xuất hiện trong hệ dữ liệu: bỏ qua tệp không chứa khoá khi quét, giảm tra cứu tầng dưới trong cây trộn có cấu trúc nhật ký, và lọc trước khi kết phân tán. Cấu trúc tóm tắt cho đếm giá trị phân biệt và cho phân vị, nối lại lesson 45. Nguyên tắc chung của câu trả lời có sai số có cận: phải công bố sai số cùng câu trả lời, nếu không thì người đọc hiểu nhầm là chính xác. Khi nào không được dùng xấp xỉ: đối soát tài chính và kiểm toán.

**Outcome.** Tính số bit cần cho một tỉ lệ báo thừa mục tiêu, cài bộ lọc Bloom, và đo tỉ lệ báo thừa thật so với lý thuyết.

**Đánh giá.** Tầng *áp dụng*. Objective gồm một phép tính và một kiểm chứng bằng thực nghiệm. Đạt khi tỉ lệ báo thừa đo được khớp lý thuyết trong phạm vi sai số thống kê, và khi người học nêu đúng hai tình huống không được dùng xấp xỉ.

**Lab.** Tính số bit cho một triệu phần tử với tỉ lệ báo thừa mục tiêu 1%. Cài bộ lọc. Kiểm bằng một triệu truy vấn phần tử không có trong tập, đếm tỉ lệ báo thừa thật. Dùng nó để giảm số lần tra cứu trong một phép kết và đo mức giảm.

**Pitfalls.** Tin kết quả báo có mà không tra nguồn thật · đặt số bit theo cảm tính · dùng xấp xỉ cho đối soát tài chính.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tỉ lệ báo thừa đo được khớp lý thuyết trong sai số thống kê, và nêu đúng hai tình huống cấm dùng xấp xỉ.

### Lesson 48 · Partitioning, hashing and distributing work `LT`
**Prerequisites.** Lesson 44

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Chia dữ liệu thành phần để xử lý song song, và ba cách chia với đặc tính khác nhau. Chia theo băm khoá cho phân bố đều khi khoá đa dạng, và đảm bảo mọi bản ghi cùng khoá về cùng một phần, điều kiện bắt buộc cho kết và gộp nhóm phân tán. Chia theo khoảng giữ được thứ tự nên quét khoảng rẻ, nhưng lệch khi dữ liệu không đều. Chia vòng tròn cho phân bố đều nhất nhưng không giữ được tính chất nào. Lệch phân vùng: một giá trị khoá chiếm phần lớn bản ghi, triệu chứng là một tác vụ chạy lâu hơn hẳn phần còn lại, và ba cách xử lý gồm thêm hậu tố ngẫu nhiên vào khoá lệch. Băm nhất quán và vì sao nó giảm số bản ghi phải di chuyển khi thêm bớt nút. Xáo trộn dữ liệu giữa các nút là thao tác đắt nhất trong xử lý phân tán, và mọi tối ưu ở chặng 7 đều quy về giảm nó. Số phần bao nhiêu là hợp lý.

**Outcome.** Chọn cách chia phần cho ba bài toán khác nhau và dự đoán bài nào sẽ bị lệch, rồi kiểm chứng bằng phân bố kích thước phần thật.

**Đánh giá.** Tầng *phân tích*. Objective đòi dự đoán lệch từ đặc tính dữ liệu rồi kiểm chứng. Kiểm bằng ba tập dữ liệu có phân bố khoá khác nhau; đạt khi dự đoán đúng tập nào lệch và khi đo được hệ số lệch giữa phần lớn nhất và phần trung vị.

**Lab.** Chia ba tập dữ liệu theo ba cách, mỗi tập một phân bố khoá khác nhau gồm một tập có khoá lệch nặng. Đo kích thước từng phần, tính hệ số lệch. Với tập lệch, áp dụng thêm hậu tố ngẫu nhiên và đo lại.

**Pitfalls.** Chia theo khoảng trên khoá lệch · chọn số phần bằng số lõi mà không tính tới lệch · quên rằng gộp nhóm phân tán đòi cùng khoá về cùng phần.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Dự đoán đúng tập nào lệch, và hệ số lệch đo được giảm sau khi thêm hậu tố ngẫu nhiên.

### Lesson 49 · Five classic data problems at scale `TH`
**Prerequisites.** Lesson 48

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Không có cơ chế mới. Bài gộp module: giải năm bài toán kinh điển trên dữ liệu lớn hơn bộ nhớ, mỗi bài dùng ít nhất một cấu trúc hoặc thuật toán đã học. Khử trùng 500 triệu bản ghi. Lấy 1.000 bản ghi lớn nhất theo nhóm. Kết hai bảng 100 triệu dòng trong đó một bảng có khoá lệch. Sắp và phân trang ổn định trên tập đang được ghi thêm. Đếm giá trị phân biệt xấp xỉ với sai số công bố. Với mỗi bài, quy trình bắt buộc: ước lượng độ phức tạp và bộ nhớ, chọn phương án, dự đoán thời gian chạy, chạy, đo bốn số theo lesson 17, và giải thích chênh lệch giữa dự đoán với số đo.

**Outcome.** Giải năm bài toán trên dữ liệu lớn hơn bộ nhớ, mỗi bài kèm ước lượng trước và số đo sau, và giải thích được mọi chênh lệch quá một bậc độ lớn.

**Đánh giá.** Tầng *sáng tạo*. Objective là thiết kế lời giải dưới ràng buộc bộ nhớ, không phải làm theo mẫu. Kiểm hai lớp: kết quả năm bài đúng so với đáp án đối chứng, và báo cáo có ước lượng trước cho cả năm. Đúng kết quả mà không có ước lượng trước thì đạt một nửa, vì mục tiêu module là chọn có căn cứ chứ không phải ra kết quả.

**Lab.** Giải năm bài trên máy giới hạn 4 ghi ga byte bộ nhớ với dữ liệu 50 ghi ga byte. Nộp cho mỗi bài: ước lượng, phương án và lý do, dự đoán thời gian, bốn số đo, và phần giải thích chênh lệch.

**Pitfalls.** Chạy trước rồi mới ước lượng · chọn phương án theo thói quen mà không xét ràng buộc bộ nhớ · bỏ qua bài có khoá lệch vì nó chạy xong dù chậm.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Năm kết quả khớp đáp án đối chứng, có ước lượng trước cho cả năm, và mọi chênh lệch quá một bậc đều giải thích được.

# MODULE 6 · CONCURRENCY, PARALLELISM AND CORRECTNESS UNDER CONTENTION

**Lessons 50–61 · 24 giờ**

| | |
|---|---|
| **Objective cấp module** | Viết chương trình xử lý dữ liệu chạy đồng thời mà chứng minh được không mất và không nhân bản bản ghi, và định vị được tranh chấp khi nó xảy ra |
| **Tiền đề** | M3 · M5 |
| **Exit criterion** | Đạt Cổng 2 ≥ 70/100: vẽ dòng thời gian chỉ ra một tranh chấp cụ thể, và giải thích vì sao thử lại không điều kiện gây cả bão tải lẫn bản ghi trùng |
| **Kỹ năng SFIA** | `PROG` mức 4 · `TEST` mức 3 |
| **Chế độ hỏng** | Chạy thử vài lần thấy đúng rồi kết luận không có tranh chấp, trong khi tranh chấp chỉ lộ ra dưới tải và ở môi trường khác |

Module khó nhất chặng 1, và là module mà lỗi tốn kém nhất về sau. Bốn bài đầu dựng khái niệm, năm bài giữa là cơ chế đồng bộ và các chế độ hỏng, ba bài cuối là mẫu hàng đợi có giới hạn, áp lực ngược và cổng 2. Mọi khẳng định về tính đúng đắn phải chứng minh bằng đối soát dưới tải, không bằng vài lần chạy thử.

### Lesson 50 · Concurrency, parallelism and asynchrony are three things `LT`
**Prerequisites.** Module 6: M3 · M5

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Ba khái niệm bị gộp làm một trong phần lớn cách nói thông thường. Đồng thời là cấu trúc chương trình cho phép nhiều việc đang dở cùng lúc; song song là thực thi nhiều việc đúng cùng một thời điểm trên nhiều lõi; bất đồng bộ là mô hình lập trình không chặn khi chờ. Một chương trình đồng thời chạy được trên một lõi; một chương trình song song cần nhiều lõi; một chương trình bất đồng bộ có thể không song song chút nào. Định luật Amdahl: phần tuần tự đặt cận trên cho mức tăng tốc, nên 10% tuần tự thì dù bao nhiêu lõi cũng không nhanh quá 10 lần. Hệ quả cho công việc dữ liệu: nhiều pipeline có phần tuần tự lớn ở khâu ghi hoặc khâu đối soát, và thêm nhân công không cứu được. Chọn mô hình theo loại tải, nối lại lesson 12: tải nghẽn vào ra hợp với bất đồng bộ hoặc nhiều luồng, tải nghẽn tính toán cần nhiều tiến trình. Khoá thông dịch toàn cục trong một số môi trường chạy Python và hệ quả thực tế của nó.

**Outcome.** Phân loại một tải rồi chọn mô hình đồng thời phù hợp, và ước lượng cận trên mức tăng tốc bằng định luật Amdahl.

**Đánh giá.** Tầng *áp dụng*. Objective gồm một phép phân loại và một phép tính có đáp án. Kiểm bằng ba tải và ba phép tính cận trên; đạt khi chọn đúng mô hình cho cả ba và khi mức tăng tốc đo được không vượt cận trên đã tính.

**Lab.** Đo phần tuần tự của ba pipeline bằng cách đo thời gian từng giai đoạn. Tính cận trên mức tăng tốc cho từng cái. Chạy mỗi pipeline ở 1, 2, 4, 8 nhân công, đo mức tăng tốc thật, vẽ đường cong và so với cận trên.

**Pitfalls.** Gọi mọi thứ chạy nhanh hơn là song song · thêm nhân công cho pipeline có phần tuần tự lớn · dùng nhiều luồng cho tải nghẽn tính toán trong môi trường chạy có khoá thông dịch toàn cục.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chọn đúng mô hình cho cả ba tải, và mức tăng tốc đo được không vượt cận trên đã tính cho tải nào.

### Lesson 51 · Critical sections and race conditions `LT`
**Prerequisites.** Lesson 50

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Vùng tới hạn là đoạn mã truy cập trạng thái dùng chung mà chỉ được một luồng vào tại một thời điểm. Tranh chấp xảy ra khi kết quả phụ thuộc thứ tự thực thi mà thứ tự đó không được bảo đảm. Vì sao một phép tăng biến đếm không phải một thao tác mà là ba: đọc, cộng, ghi, và mất cập nhật xảy ra ở khe giữa ba bước đó. Ba loại tranh chấp thường gặp trong công việc dữ liệu: hai nhân công cùng lấy một công việc trong hàng đợi, hai tiến trình cùng ghi một tệp đích, và kiểm tra rồi hành động trên hệ tệp với khe giữa hai bước. Vì sao tranh chấp không lộ ra khi chạy thử: cửa sổ rất hẹp nên xác suất thấp, và xác suất đó tăng theo tải và đổi theo máy. Vẽ dòng thời gian hai luồng để chứng minh một tranh chấp tồn tại, kỹ thuật kiểm được và là yêu cầu của cổng. Tranh chấp không phải lỗi ngẫu nhiên mà là lỗi thiết kế có thể lập luận ra trước khi chạy.

**Outcome.** Vẽ dòng thời gian hai luồng chứng minh một tranh chấp trong một đoạn mã cho trước, trước khi chạy nó.

**Đánh giá.** Tầng *phân tích*. Objective là lập luận ra lỗi từ mã, không phải quan sát lỗi khi chạy. Kiểm bằng bốn đoạn mã, ba có tranh chấp một không; đạt khi chỉ đúng cả bốn và với ba đoạn có lỗi thì vẽ được dòng thời gian cho ra kết quả sai. Chạy rồi mới biết không tính điểm.

**Lab.** Đọc bốn đoạn mã, phân loại có hay không có tranh chấp, vẽ dòng thời gian cho từng đoạn có lỗi. Sau đó chạy mỗi đoạn 100.000 lần với 8 luồng, đếm số lần kết quả sai, so với dự đoán. Chạy lại trên máy khác và so tỉ lệ.

**Pitfalls.** Kết luận không có tranh chấp vì chạy 10 lần đều đúng · cho rằng một phép gán là thao tác nguyên tử · sửa bằng cách thêm thời gian ngủ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân loại đúng cả bốn đoạn và vẽ được dòng thời gian cho ba đoạn có lỗi, trước khi chạy.

### Lesson 52 · Mutexes, semaphores and condition variables `TH`
**Prerequisites.** Lesson 51

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Khoá loại trừ cho phép đúng một luồng vào vùng tới hạn. Chi phí của khoá: tranh chấp khoá làm luồng phải chờ, và vùng tới hạn càng dài thì mức song song càng thấp. Nguyên tắc giữ khoá ngắn nhất có thể, và cái giá khi chia nhỏ vùng tới hạn quá mức. Đèn hiệu giới hạn số luồng vào cùng lúc, dùng để giới hạn số kết nối hoặc số yêu cầu đồng thời, nối lại lesson 36. Biến điều kiện cho luồng chờ tới khi một điều kiện thành đúng mà không quay vòng tốn bộ xử lý. Đánh thức giả và vì sao phải kiểm điều kiện trong vòng lặp chứ không trong câu lệnh điều kiện. Khoá đọc ghi cho tải đọc nhiều. Thao tác nguyên tử và khi nào chúng đủ thay cho khoá. Khoá trên nhiều tiến trình: khoá tệp ở lesson 27 và khoá phân tán ở chặng 6, cùng bài toán ở ba quy mô. Khoá phân tán không đáng tin tuyệt đối vì đồng hồ và mạng, nên thiết kế vẫn phải chịu được hai bên cùng chạy.

**Outcome.** Sửa một đoạn mã có tranh chấp bằng cơ chế đồng bộ phù hợp, và đo chi phí thông lượng mà cơ chế đó gây ra.

**Đánh giá.** Tầng *áp dụng*. Objective gồm sửa lỗi và đo cái giá, vì chọn cơ chế mà không biết giá là chọn mù. Đạt khi 100.000 lần chạy 8 luồng không ra kết quả sai nào, và khi có bảng thông lượng trước và sau cho thấy chi phí đồng bộ.

**Lab.** Sửa ba đoạn mã có tranh chấp ở lesson 51 bằng ba cơ chế khác nhau. Với mỗi đoạn, chạy 100.000 lần với 8 luồng và đếm lỗi. Đo thông lượng trước và sau. Thử thu hẹp vùng tới hạn và đo lại.

**Pitfalls.** Giữ khoá suốt cả hàm · kiểm điều kiện bằng câu lệnh điều kiện thay vì vòng lặp nên dính đánh thức giả · dùng khoá cho biến đếm trong khi thao tác nguyên tử là đủ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** 100.000 lần chạy 8 luồng không lỗi, và có bảng thông lượng trước sau cho thấy chi phí đồng bộ.

### Lesson 53 · Deadlock, livelock and starvation `TH`
**Prerequisites.** Lesson 52

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bế tắc cần đủ bốn điều kiện đồng thời, và phá một điều kiện là đủ để ngăn. Cách phá thực tế nhất trong công việc dữ liệu: quy định thứ tự lấy khoá toàn cục, nên mọi luồng lấy khoá theo cùng một thứ tự. Bế tắc trong cơ sở dữ liệu: hai giao dịch lấy khoá hàng theo thứ tự ngược nhau, cơ chế phát hiện tự động và chọn nạn nhân, nối tới chặng 3. Khoá sống: các luồng liên tục nhường nhau và không ai tiến được, và vì sao nó khó phát hiện hơn bế tắc vì hệ thống vẫn bận. Đói: một luồng không bao giờ tới lượt do chính sách ưu tiên. Thời gian chờ khoá như một mạng an toàn: thà lỗi còn hơn treo, nối lại nguyên tắc ở lesson 34. Chẩn đoán bế tắc trên hệ thống đang chạy: đọc ngăn xếp luồng và tìm vòng chờ. Thiết kế tránh bế tắc quan trọng hơn phát hiện bế tắc.

**Outcome.** Gây ra một bế tắc có chủ đích, chẩn đoán nó từ ngăn xếp luồng, và sửa bằng quy định thứ tự lấy khoá.

**Đánh giá.** Tầng *phân tích*. Objective gồm chẩn đoán từ bằng chứng và sửa có nguyên tắc. Đạt khi định vị được vòng chờ từ ngăn xếp luồng, và khi bản sửa chạy một triệu vòng với 16 luồng không treo lần nào. Sửa bằng cách thêm thời gian chờ mà không phá vòng chờ chỉ đạt một nửa.

**Lab.** Viết chương trình hai luồng lấy hai khoá theo thứ tự ngược nhau, chạy tới khi treo. Lấy ngăn xếp luồng, định vị vòng chờ. Sửa bằng thứ tự khoá toàn cục, chạy một triệu vòng với 16 luồng. Sau đó gây bế tắc trong cơ sở dữ liệu và quan sát cơ chế chọn nạn nhân.

**Pitfalls.** Sửa bế tắc bằng cách thêm thời gian ngủ · không đặt thời gian chờ khoá nên treo vô hạn · tăng số luồng khi thấy chậm trong khi nguyên nhân là tranh chấp khoá.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Định vị được vòng chờ từ ngăn xếp luồng, và bản sửa chạy một triệu vòng với 16 luồng không treo.

### Lesson 54 · Atomicity, memory visibility and why a variable looks stale `LT`
**Prerequisites.** Lesson 52

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Nguyên tử nghĩa là không quan sát được trạng thái nửa chừng; khả kiến nghĩa là thay đổi của luồng này luồng kia nhìn thấy. Hai tính chất khác nhau và một chương trình có thể có cái này mà thiếu cái kia. Bộ nhớ đệm mỗi lõi và vì sao một luồng ghi biến mà luồng khác đọc ra giá trị cũ. Giao thức nhất quán bộ nhớ đệm làm việc đó cuối cùng cũng đồng bộ, nhưng cuối cùng là bao lâu thì không có bảo đảm. Sắp xếp lại lệnh bởi bộ biên dịch và bởi bộ xử lý: cả hai được phép đổi thứ tự miễn kết quả trên một luồng không đổi, nhưng trên nhiều luồng thì đổi. Hàng rào bộ nhớ và biến có đánh dấu không đệm. Vì sao một vòng lặp chờ cờ hiệu có thể chạy mãi dù cờ đã được đặt. Thao tác so sánh rồi hoán đổi và cấu trúc không khoá, cùng cảnh báo: viết cấu trúc không khoá đúng là việc khó và hiếm khi cần trong công việc dữ liệu. Nối tới chặng 6: cùng vấn đề khả kiến xuất hiện ở quy mô phân tán dưới tên nhất quán.

**Outcome.** Giải thích vì sao một luồng đọc ra giá trị cũ dù luồng khác đã ghi, và chỉ ra cơ chế nào trong ba cơ chế gây ra điều đó.

**Đánh giá.** Tầng *hiểu*. Objective là giải thích cơ chế, vì cài đặt cấu trúc không khoá vượt phạm vi module. Kiểm bằng ba đoạn mã, mỗi đoạn hỏng vì một cơ chế: bộ nhớ đệm chưa đồng bộ, sắp xếp lại lệnh, và thao tác không nguyên tử. Đạt khi chỉ đúng cơ chế cho cả ba.

**Lab.** Viết vòng lặp chờ cờ hiệu không đánh dấu, chạy với tối ưu hoá bật, quan sát nó chạy mãi. Thêm đánh dấu, quan sát nó dừng. Đọc ba đoạn mã và chỉ cơ chế gây lỗi cho từng đoạn. Đo chi phí của hàng rào bộ nhớ.

**Pitfalls.** Gộp nguyên tử với khả kiến làm một · tin rằng ghi xong là luồng khác thấy ngay · viết cấu trúc không khoá khi một khoá là đủ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chỉ đúng cơ chế gây lỗi cho cả ba đoạn mã, và quan sát được vòng lặp chờ cờ hiệu chạy mãi rồi dừng sau khi sửa.

### Lesson 55 · Thread safety and immutable data `TH`
**Prerequisites.** Lesson 54

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** An toàn luồng là thuộc tính của một đoạn mã dưới truy cập đồng thời, và nó không phải thuộc tính của ngôn ngữ. Ba cách đạt được, theo thứ tự nên ưu tiên: không chia sẻ trạng thái, chia sẻ dữ liệu bất biến, và chia sẻ dữ liệu thay đổi được có đồng bộ. Cách thứ nhất và thứ hai không cần khoá nên không có tranh chấp khoá và không có bế tắc, đó là lý do chúng đứng trước. Dữ liệu bất biến trong xử lý dữ liệu: mỗi phép biến đổi sinh ra tập mới thay vì sửa tại chỗ, và đây là mô hình mà Spark dùng ở chặng 7. Cái giá là bộ nhớ và số lần sao chép. Trạng thái cục bộ theo luồng cho những thứ không chia sẻ được như kết nối cơ sở dữ liệu. Thư viện có an toàn luồng hay không là câu phải tra tài liệu chứ không đoán, và kết nối cơ sở dữ liệu gần như luôn không an toàn luồng, một lỗi rất phổ biến. Kiểm tra an toàn luồng bằng chạy tải đồng thời và đối soát, không bằng đọc mã.

**Outcome.** Chuyển một đoạn xử lý dữ liệu chia sẻ trạng thái thay đổi được sang mô hình không chia sẻ hoặc bất biến, và đo chênh lệch thông lượng.

**Đánh giá.** Tầng *áp dụng*. Objective gồm một phép tái cấu trúc và một phép đo cái giá. Đạt khi bản mới cho kết quả đúng dưới 16 luồng qua 100 lần chạy, và khi có bảng thông lượng cùng bộ nhớ đỉnh của cả hai bản để thấy đánh đổi.

**Lab.** Nhận một đoạn gộp dữ liệu dùng từ điển chia sẻ có khoá. Viết lại theo hai cách: mỗi luồng một từ điển riêng rồi gộp cuối, và dùng cấu trúc bất biến. Chạy cả ba bản với 16 luồng, 100 lần, đối soát kết quả. Đo thông lượng và bộ nhớ đỉnh.

**Pitfalls.** Dùng chung một kết nối cơ sở dữ liệu cho nhiều luồng · giả định thư viện an toàn luồng vì nó phổ biến · kiểm an toàn luồng bằng cách đọc mã.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Cả ba bản cho kết quả đúng qua 100 lần chạy 16 luồng, và có bảng thông lượng cùng bộ nhớ đỉnh.

### Lesson 56 · Bounded queues and the producer-consumer pattern `TH`
**Prerequisites.** Lesson 55

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hàng đợi có giới hạn là cấu trúc trung tâm của mọi pipeline chạy đồng thời. Bên sản xuất đẩy vào, bên tiêu thụ lấy ra, hàng đợi tách nhịp hai bên. Giới hạn kích thước là phần quan trọng nhất và hay bị bỏ: hàng đợi không giới hạn biến chênh lệch tốc độ thành tăng trưởng bộ nhớ, và tiến trình chết vì cạn bộ nhớ ở lesson 14 thay vì chậm lại. Hàng đợi đầy làm bên sản xuất bị chặn, đó chính là áp lực ngược, cùng cơ chế với ống dẫn ở lesson 20 và với cửa sổ nhận ở lesson 31. Chọn kích thước hàng đợi: đủ lớn để hấp thụ dao động, đủ nhỏ để lỗi lộ ra sớm và để giới hạn dữ liệu mất khi chết. Tín hiệu kết thúc và cách đóng hàng đợi sạch sẽ để bên tiêu thụ biết dừng. Nhiều bên tiêu thụ và bảo đảm mỗi phần tử được xử lý đúng một lần. Xác nhận sau khi xử lý xong chứ không khi lấy ra, nguyên tắc quyết định giữa mất và trùng, nối thẳng tới chặng 6.

**Outcome.** Cài mẫu sản xuất tiêu thụ có hàng đợi giới hạn và chứng minh bằng đối soát rằng không mất và không nhân bản bản ghi dưới tải.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí đối soát tuyệt đối dưới tải. Đạt khi chạy một triệu bản ghi với 8 bên tiêu thụ, số bản ghi ra bằng đúng số vào, không trùng, lặp lại 20 lần đều đúng. Một lần lệch là không đạt vì đây chính là lỗi module tồn tại để ngăn.

**Lab.** Cài sản xuất tiêu thụ với hàng đợi giới hạn 1.000. Chạy một triệu bản ghi với 8 bên tiêu thụ, đối soát, lặp 20 lần. Đổi sang hàng đợi không giới hạn với bên tiêu thụ chậm, quan sát bộ nhớ tăng tới khi bị giết. Đo thông lượng ở bốn kích thước hàng đợi.

**Pitfalls.** Dùng hàng đợi không giới hạn · xác nhận phần tử khi lấy ra thay vì khi xử lý xong · quên tín hiệu kết thúc nên bên tiêu thụ treo.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** 20 lần chạy một triệu bản ghi với 8 bên tiêu thụ đều đối soát khớp tuyệt đối.

### Lesson 57 · Backpressure and what to do when downstream is slow `LT`
**Prerequisites.** Lesson 56

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Áp lực ngược là tín hiệu từ hạ nguồn chậm truyền ngược lên thượng nguồn. Bốn phản ứng khi hạ nguồn không theo kịp và hậu quả của từng cái: chặn thượng nguồn giữ được toàn vẹn nhưng đẩy vấn đề lên trên, đệm thêm chỉ hoãn vấn đề và đổi nó thành cạn bộ nhớ, loại bớt bản ghi làm mất dữ liệu nên chỉ chấp nhận được cho một số loại dữ liệu, và mở rộng hạ nguồn là cách đúng nhưng chậm. Tiêu chí chọn theo loại dữ liệu: dữ liệu giao dịch không được loại, dữ liệu đo lường thì loại được. Vì sao hệ thống không có áp lực ngược sụp theo kiểu thác đổ thay vì chậm dần: hàng đợi phình, bộ nhớ cạn, tiến trình chết, việc dồn sang nút còn lại, nút đó cũng chết. Phát hiện áp lực ngược qua số đo: độ sâu hàng đợi tăng đều là chỉ báo sớm nhất, và nó phải được phát ra ngoài. Nối tới chặng 6: độ trễ tiêu thụ trong hệ thống luồng là cùng chỉ báo đó.

**Outcome.** Chọn phản ứng phù hợp với áp lực ngược cho ba loại dữ liệu khác nhau và nêu hậu quả của lựa chọn.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn giữa bốn phương án theo ràng buộc nghiệp vụ, không có đáp án chung. Kiểm bằng ba tình huống: dữ liệu thanh toán, dữ liệu đo lường, dữ liệu nhật ký gỡ lỗi. Đạt khi mỗi lựa chọn nêu được hậu quả chấp nhận và hậu quả từ chối, và khi mô phỏng xác nhận hệ thống không sụp kiểu thác đổ.

**Lab.** Dựng pipeline ba chặng, làm chặng cuối chậm đi 10 lần. Thử bốn phản ứng, đo bộ nhớ, thông lượng và số bản ghi mất cho từng cái. Với ba loại dữ liệu, chọn phản ứng và viết một đoạn nêu hậu quả. Phát độ sâu hàng đợi ra ngoài và vẽ đồ thị.

**Pitfalls.** Tăng kích thước đệm khi thấy hàng đợi đầy · loại bản ghi giao dịch để giữ thông lượng · không phát độ sâu hàng đợi nên không có chỉ báo sớm.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba lựa chọn đều nêu được hậu quả hai chiều, và mô phỏng cho thấy hệ thống chậm dần thay vì sụp kiểu thác đổ.

### Lesson 58 · Async IO - event loop, coroutines and when it wins `TH`
**Prerequisites.** Lesson 50

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Vòng lặp sự kiện chạy trên một luồng và chuyển qua lại giữa các tác vụ tại điểm chờ. Hệ quả: một tác vụ chiếm bộ xử lý mà không nhường làm đứng toàn bộ vòng lặp, và đây là chế độ hỏng đặc trưng của mô hình bất đồng bộ. Hàm đồng quy và điểm nhường. Gọi hàm chặn bên trong mã bất đồng bộ là lỗi phổ biến nhất: nó chặn cả vòng lặp chứ không chỉ tác vụ đó, và cách phát hiện là đo thời gian giữa hai vòng lặp. Đẩy việc chặn sang nhóm luồng riêng. Giới hạn số tác vụ đồng thời bằng đèn hiệu, nếu không thì mở mười nghìn kết nối cùng lúc. Huỷ tác vụ và dọn dẹp, nối lại lesson 21. Khi nào bất đồng bộ thắng nhiều luồng: rất nhiều kết nối chờ vào ra, chi phí một tác vụ thấp hơn một luồng nhiều. Khi nào không thắng: ít kết nối, hoặc tải nghẽn tính toán. Trộn hai mô hình trong một chương trình và cái giá về độ phức tạp.

**Outcome.** Viết ứng dụng khách bất đồng bộ gọi 10.000 yêu cầu có giới hạn đồng thời, và phát hiện được một lời gọi chặn lọt vào vòng lặp.

**Đánh giá.** Tầng *áp dụng*. Objective gồm một sản phẩm và một phép chẩn đoán. Đạt khi 10.000 yêu cầu hoàn tất với số kết nối đồng thời không vượt giới hạn đặt ra, và khi người học đo được thời gian đứng vòng lặp trước và sau khi đẩy lời gọi chặn ra ngoài.

**Lab.** Viết ứng dụng khách bất đồng bộ gọi 10.000 yêu cầu, đèn hiệu giới hạn 50 đồng thời. Đếm kết nối thật bằng công cụ ở lesson 38. Cố ý gọi một hàm chặn trong vòng lặp, đo thời gian đứng. Đẩy nó sang nhóm luồng, đo lại. So thông lượng với bản nhiều luồng.

**Pitfalls.** Gọi hàm chặn trong mã bất đồng bộ · không giới hạn số tác vụ đồng thời · dùng bất đồng bộ cho tải nghẽn tính toán.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** 10.000 yêu cầu hoàn tất không vượt giới hạn đồng thời, và thời gian đứng vòng lặp giảm đo được sau khi đẩy lời gọi chặn ra.

### Lesson 59 · Processes, shared memory and multiprocessing for CPU work `TH`
**Prerequisites.** Lesson 58

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Nhiều tiến trình cho tải nghẽn tính toán, vì mỗi tiến trình có bộ thông dịch riêng nên không bị khoá thông dịch toàn cục chặn. Cái giá: mỗi tiến trình tốn bộ nhớ riêng, và truyền dữ liệu giữa các tiến trình phải tuần tự hoá. Chi phí tuần tự hoá thường lớn hơn người ta tưởng và có thể nuốt hết lợi ích song song khi dữ liệu lớn mà tính toán nhẹ, nên phải đo tỉ lệ giữa hai phần. Bộ nhớ chia sẻ để tránh sao chép, và mảng chia sẻ cho dữ liệu số. Sao chép khi ghi khi tạo tiến trình con và vì sao bộ nhớ thật tăng dần chứ không tăng ngay. Nhóm tiến trình và kích thước khối khi chia việc: khối quá nhỏ thì chi phí điều phối lớn, quá lớn thì mất cân bằng tải. Truyền dữ liệu qua tệp hoặc bộ nhớ chia sẻ thay vì qua hàng đợi khi dữ liệu lớn. Tiến trình con chết và cơ chế phát hiện, nối lại lesson 21.

**Outcome.** Chọn giữa nhiều luồng và nhiều tiến trình cho một tải cho trước bằng số đo, và xác định kích thước khối cho thông lượng cao nhất.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn có căn cứ và tinh chỉnh một tham số, không có đáp án chung. Kiểm bằng bảng thực nghiệm: hai mô hình nhân ba kích thước khối nhân hai loại tải. Đạt khi lựa chọn dẫn được về số đo, và khi chi phí tuần tự hoá được tách ra khỏi thời gian tính toán.

**Lab.** Chạy một tải tính toán trên 10 triệu bản ghi theo hai mô hình, mỗi mô hình ba kích thước khối. Đo thời gian, bộ nhớ đỉnh, và riêng phần tuần tự hoá. Lặp lại với tải nghẽn vào ra. Lập bảng và chọn cấu hình cho từng loại tải.

**Pitfalls.** Dùng nhiều tiến trình cho tải nghẽn vào ra · truyền khung dữ liệu lớn qua hàng đợi tiến trình · chọn kích thước khối bằng cảm tính.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng thực nghiệm đủ hai mô hình nhân ba kích thước khối nhân hai loại tải, và chi phí tuần tự hoá được tách riêng.

### Lesson 60 · Proving correctness under load - the reconciliation habit `TH`
**Prerequisites.** Lesson 56

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Chạy thử vài lần không chứng minh gì, vì tranh chấp có xác suất thấp và phụ thuộc máy. Bốn kỹ thuật chứng minh tính đúng đắn dưới tải. Một là đối soát: đếm bản ghi vào và ra, tổng theo khoá nghiệp vụ, và kiểm tính duy nhất của khoá, nối lại nguyên tắc ở chặng 4. Hai là kiểm thử bất biến: phát biểu tính chất phải luôn đúng rồi sinh đầu vào ngẫu nhiên để thử phá. Ba là bơm lỗi có chủ đích: giết tiến trình, làm chậm mạng, làm đầy đĩa ở thời điểm ngẫu nhiên và lặp nhiều lần. Bốn là chạy dưới công cụ phát hiện tranh chấp. Số lần lặp cần thiết để có ý nghĩa thống kê, và vì sao 10 lần là không đủ. Chạy trên nhiều cấu hình máy vì số lõi đổi thì cửa sổ tranh chấp đổi. Ghi lại hạt giống ngẫu nhiên để tái hiện được ca hỏng. Nguyên tắc: một pipeline chưa bị bơm lỗi là một pipeline chưa biết mình hỏng thế nào.

**Outcome.** Thiết kế và chạy một bộ chứng minh tính đúng đắn cho một pipeline đồng thời, dùng cả bốn kỹ thuật.

**Đánh giá.** Tầng *sáng tạo*. Objective là thiết kế một bộ kiểm chứng dưới ràng buộc, không phải chạy một bộ có sẵn. Kiểm bằng rà soát chéo: một học viên khác dùng bộ đó trên pipeline của mình và phải tìm ra được ít nhất một lỗi đã cài sẵn. Bộ không phát hiện được lỗi cài sẵn thì chưa đủ mạnh.

**Lab.** Viết bộ chứng minh cho pipeline ở lesson 56: đối soát, kiểm thử bất biến, bơm lỗi 200 lần ở thời điểm ngẫu nhiên, và chạy dưới công cụ phát hiện tranh chấp. Nhận pipeline của học viên khác có ba lỗi cài sẵn, chạy bộ của mình, báo cáo lỗi tìm được.

**Pitfalls.** Chạy 10 lần rồi kết luận đúng · bơm lỗi ở thời điểm cố định nên bỏ sót cửa sổ hẹp · không ghi hạt giống nên không tái hiện được ca hỏng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bộ chứng minh tìm ra ít nhất một trong ba lỗi cài sẵn trong pipeline của học viên khác.

### Lesson 61 · Gate 2 - race timeline and the retry storm `KT`
**Prerequisites.** Lesson 60

**In-class (120 phút).** 75 phút làm bài độc lập · 45 phút chữa bài và phân tích lỗi theo nhóm

**Learn.** Không có nội dung mới. Cổng 2 của chương trình.

**Outcome.** Định vị một tranh chấp trong mã chưa từng thấy và vẽ dòng thời gian chứng minh nó, rồi giải thích vì sao thử lại không điều kiện gây đồng thời bão tải và bản ghi trùng.

**Đánh giá.** Tầng *đánh giá*. Cổng đo năng lực lập luận về mã đồng thời và về hệ quả hệ thống, không đo trí nhớ API. Thang điểm: A 25đ định vị tranh chấp trong ba đoạn mã lạ · B 20đ dòng thời gian chứng minh cho một tranh chấp · C 20đ sửa và chứng minh bằng đối soát dưới tải · D 20đ giải thích bão tải và bản ghi trùng bằng cơ chế · E 15đ chọn phản ứng áp lực ngược cho một tình huống cho trước. Đạt khi ≥ 70/100, phần A ≥ 50% và phần C ≥ 50%.

**Lab.** 150 phút. Ba đoạn mã lạ, một pipeline có lỗi cài sẵn, và một tình huống thiết kế. Sửa xong phải chứng minh bằng 200 lần chạy có bơm lỗi, không phải bằng lập luận.

**Pitfalls.** Sửa bằng cách thêm khoá quanh mọi thứ rồi thông lượng sụp · chứng minh bằng lập luận thay vì bằng đối soát · giải thích bão tải mà bỏ mất vế bản ghi trùng.

**Self-study (2,4 giờ).** Không có bài tự học. Nếu không đạt, theo phụ lục khắc phục khi không đạt cổng

**Done when.** Đạt ≥ 70/100, phần A ≥ 50% và phần C ≥ 50%.

# MODULE 7 · PYTHON FOR DATA ENGINEERING

**Lessons 62–77 · 32 giờ**

| | |
|---|---|
| **Objective cấp module** | Viết một công việc dữ liệu bằng Python xử lý được tệp lớn hơn bộ nhớ, chạy lại an toàn, và ghi nhật ký đủ để chẩn đoán khi hỏng |
| **Tiền đề** | M5 · M6 |
| **Exit criterion** | Công cụ dòng lệnh nạp API có phân trang, điểm kiểm tra và giới hạn tốc độ, chạy hai lần cho kết quả bằng chạy một lần |
| **Kỹ năng SFIA** | `PROG` mức 3 |
| **Chế độ hỏng** | Học Python như ngôn ngữ phân tích rồi nạp cả tệp vào bộ nhớ, nên tới chặng 4 không xử lý nổi nguồn 50 ghi ga byte |

Module không dạy Python tổng quát. Nó dạy đúng phần một công việc dữ liệu cần: xử lý theo luồng, quản lý tài nguyên, và ghi nhật ký chẩn đoán được. Mọi bài đều chạy trên dữ liệu lớn hơn bộ nhớ máy để thói quen nạp hết vào RAM không hình thành được.

### Lesson 62 · Python basics for data work - types, control flow, functions `TH`
**Prerequisites.** Module 7: M5 · M6

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Kiểu dựng sẵn và điều đáng chú ý với công việc dữ liệu: số nguyên độ rộng tuỳ ý nên không tràn như lesson 6 nhưng tốn bộ nhớ hơn, số thực là dấu phẩy động nên mang đúng vấn đề ở lesson 7, và chuỗi là dãy điểm mã nên độ dài khác số byte như lesson 8. Kiểu thập phân cho tiền. Biến trỏ tới đối tượng chứ không chứa giá trị, và hệ quả: gán một danh sách cho biến khác không sao chép, nên sửa một chỗ đổi cả hai. Sao chép nông và sao chép sâu. Đối số mặc định là đối tượng thay đổi được là bẫy kinh điển và nó sống qua các lần gọi. Hàm, tham số vị trí và tham số khoá, và quy ước đặt tham số có ý nghĩa. Truyền tham chiếu đối tượng và hệ quả khi hàm sửa đối số. Phép so sánh danh tính và phép so sánh giá trị, cùng lý do so sánh với giá trị rỗng phải dùng danh tính.

**Outcome.** Định vị trong năm đoạn mã chỗ nào một đối tượng bị chia sẻ ngoài ý muốn, và sửa bằng sao chép đúng mức.

**Đánh giá.** Tầng *phân tích*. Objective là truy một lớp lỗi có nguyên nhân chung, không phải viết mã mới. Kiểm bằng năm đoạn mã, bốn đoạn có lỗi chia sẻ đối tượng theo bốn cơ chế khác nhau. Đạt khi chỉ đúng cả năm và sửa được bốn đoạn lỗi mà không đổi hành vi đúng.

**Lab.** Đọc năm đoạn mã: đối số mặc định thay đổi được, gán danh sách lồng nhau, sao chép nông trên từ điển lồng, hàm sửa đối số của người gọi, và một đoạn đúng. Dự đoán kết quả từng đoạn trước khi chạy, rồi chạy đối chiếu. Sửa bốn đoạn lỗi.

**Pitfalls.** Dùng danh sách rỗng làm đối số mặc định · dùng sao chép nông cho cấu trúc lồng · so sánh với giá trị rỗng bằng phép so sánh giá trị.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Dự đoán trước khi chạy khớp kết quả cho cả năm đoạn, và bốn đoạn lỗi được sửa mà hành vi đúng không đổi.

### Lesson 63 · Collections and choosing the right one `TH`
**Prerequisites.** Lesson 62

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bốn cấu trúc dựng sẵn và đặc tính chi phí của từng cái, nối trực tiếp lesson 41 và 42: danh sách cho truy cập theo chỉ số và duyệt tuần tự, bộ cho kiểm tra thành viên và phép toán tập hợp, từ điển cho tra cứu theo khoá, bộ giá trị bất biến nên dùng làm khoá được. Kiểm tra thành viên trên danh sách là bậc n còn trên bộ là hằng số, và đây là một trong những sửa lỗi hiệu năng hay gặp nhất trong mã xử lý dữ liệu. Chi phí bộ nhớ thật của từng cấu trúc, nối lại lesson 13. Hàng đợi hai đầu cho thêm bớt ở cả hai phía. Bộ đếm cho đếm tần suất. Từ điển có giá trị mặc định. Bộ giá trị có tên và lúc nào nên chuyển sang lớp dữ liệu ở lesson 67. Cách duyệt nhiều cấu trúc song song và cách duyệt kèm chỉ số. Biểu thức tạo danh sách, tạo bộ và tạo từ điển, cùng ngưỡng mà chúng trở nên khó đọc.

**Outcome.** Chọn cấu trúc dữ liệu cho năm thao tác cho trước và chứng minh lựa chọn bằng số đo thời gian và bộ nhớ.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn có biện minh giữa nhiều phương án đều chạy được. Kiểm bằng bảng năm thao tác nhân ít nhất hai cấu trúc mỗi thao tác, có số đo. Đạt khi mỗi lựa chọn dẫn được về số đo, không chấp nhận lý do theo thói quen.

**Lab.** Năm thao tác trên 10 triệu bản ghi: kiểm tra thành viên, đếm tần suất, khử trùng, tra cứu theo khoá, và thêm bớt hai đầu. Cài mỗi thao tác bằng ít nhất hai cấu trúc, đo thời gian và bộ nhớ đỉnh. Lập bảng và chọn.

**Pitfalls.** Kiểm tra thành viên trên danh sách trong vòng lặp · dùng từ điển khi chỉ cần bộ · nối chuỗi trong vòng lặp bằng phép cộng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng năm thao tác có số đo cho ít nhất hai cấu trúc mỗi thao tác, và mọi lựa chọn dẫn được về số đo.

### Lesson 64 · Iterators, generators and processing data larger than memory `TH`
**Prerequisites.** Lesson 63

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Giao thức lặp và khác biệt giữa một đối tượng lặp được với một bộ lặp. Hàm sinh trả về từng phần tử một thay vì dựng cả danh sách, nên bộ nhớ không phụ thuộc số phần tử. Đây là công cụ trung tâm của module: nó biến mọi bài toán nạp cả tệp vào bộ nhớ thành bài toán chảy qua bộ nhớ. Biểu thức sinh so với biểu thức tạo danh sách, khác nhau một ký tự và khác nhau về bộ nhớ nhiều bậc. Xâu chuỗi nhiều hàm sinh thành một đường ống, và tính chất chỉ chạy khi có người lấy. Hệ quả cần cẩn thận: bộ sinh chỉ duyệt được một lần, và một lỗi phổ biến là duyệt hai lần rồi lần thứ hai rỗng. Thư viện công cụ lặp: gộp nhóm, cắt lát, nối, và ghép cặp. Trả về bộ sinh từ hàm đọc tệp thay vì trả về danh sách, mẫu bắt buộc trong mọi mã nạp dữ liệu của chương trình.

**Outcome.** Viết lại một đoạn nạp cả tệp vào bộ nhớ thành đường ống hàm sinh, và chứng minh bộ nhớ đỉnh không tăng theo kích thước tệp.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí kiểm chứng tuyệt đối bằng số đo bộ nhớ. Đạt khi bộ nhớ đỉnh gần như không đổi qua bốn kích thước tệp tăng dần, và khi kết quả khớp bản nạp toàn bộ trên tệp nhỏ nhất. Chạy được mà bộ nhớ vẫn tăng theo kích thước thì không đạt.

**Lab.** Nhận đoạn mã nạp cả tệp rồi lọc và gộp. Viết lại thành đường ống hàm sinh. Chạy trên bốn tệp 1, 5, 20, 50 ghi ga byte với máy 4 ghi ga byte. Đo bộ nhớ đỉnh từng lần. Cố ý duyệt bộ sinh hai lần và quan sát lần thứ hai rỗng.

**Pitfalls.** Dùng biểu thức tạo danh sách thay vì biểu thức sinh · duyệt bộ sinh hai lần · gọi hàm đếm độ dài trên bộ sinh rồi mất dữ liệu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bộ nhớ đỉnh gần như không đổi qua bốn kích thước tệp, và kết quả khớp bản nạp toàn bộ trên tệp nhỏ nhất.

### Lesson 65 · Exceptions - what to catch, what to let crash `TH`
**Prerequisites.** Lesson 64

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Cây phân cấp ngoại lệ và nguyên tắc bắt hẹp nhất có thể. Bắt quá rộng nuốt mất lỗi lập trình và biến chúng thành lỗi dữ liệu giả, một trong những cách tệ nhất để gỡ lỗi. Ba nhóm lỗi và cách xử lý khác nhau, nối lại lesson 74 của chặng trước: lỗi tạm thời thì thử lại, lỗi dữ liệu thì tách bản ghi ra bảng lỗi và chạy tiếp, lỗi lập trình thì để chương trình chết ngay. Nguyên tắc không loại bản ghi lỗi trong im lặng: mỗi bản ghi bị loại phải kèm lý do và đếm được. Khối cuối cùng luôn chạy và chỗ nó thua trình quản lý ngữ cảnh ở lesson 66. Ngoại lệ tự định nghĩa để mã gọi phân biệt được, nối tới lesson 90 của chặng trước. Chuỗi ngoại lệ giữ nguyên nguyên nhân gốc thay vì che mất nó. Ghi vết ngăn xếp vào nhật ký thay vì in ra. Vì sao bắt rồi ghi nhật ký rồi ném lại thường là mẫu thừa tạo nhật ký trùng.

**Outcome.** Phân loại 12 tình huống lỗi thành ba nhóm và cài đặt xử lý đúng cho từng nhóm, trong đó bản ghi lỗi được tách ra kèm lý do.

**Đánh giá.** Tầng *áp dụng*. Objective gồm phân loại có đáp án và cài đặt kiểm được bằng đối soát. Đạt khi phân loại đúng ít nhất 10 trên 12, và khi chạy trên tệp có 5% bản ghi hỏng thì tổng bản ghi đầu vào bằng bản ghi sạch cộng bản ghi lỗi, không sai một dòng.

**Lab.** Nhận tệp 1 triệu bản ghi trong đó 5% hỏng theo sáu kiểu. Phân loại 12 tình huống lỗi thành ba nhóm. Viết trình nạp tách bản ghi lỗi ra bảng riêng kèm lý do. Đối soát phép cộng. Chèn một lỗi lập trình và xác nhận chương trình chết ngay chứ không nuốt.

**Pitfalls.** Bắt ngoại lệ gốc rồi bỏ qua · loại bản ghi lỗi mà không đếm · ném lại ngoại lệ mới làm mất nguyên nhân gốc.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân loại đúng ít nhất 10 trên 12, và phép cộng đối soát khớp tuyệt đối trên tệp 1 triệu bản ghi.

### Lesson 66 · Context managers and resource cleanup `TH`
**Prerequisites.** Lesson 65

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Tài nguyên phải được nhả kể cả khi có lỗi, và đây là chỗ khối cuối cùng đủ dùng nhưng dễ quên. Trình quản lý ngữ cảnh gắn việc nhả vào cấu trúc mã nên không quên được. Ba tài nguyên bắt buộc dùng nó trong công việc dữ liệu: tệp, kết nối cơ sở dữ liệu, và khoá. Rò rỉ bộ mô tả tệp nối lại lesson 20: vòng lặp mở tệp không đóng sẽ hết giới hạn. Viết trình quản lý ngữ cảnh riêng bằng hai phương thức hoặc bằng bộ trang trí. Lồng nhiều trình quản lý trong một câu lệnh. Trình quản lý ngữ cảnh cho giao dịch cơ sở dữ liệu: xác nhận khi thoát bình thường, hoàn tác khi có ngoại lệ, và vì sao viết tay dễ quên nhánh hoàn tác. Trình quản lý ngữ cảnh cho tệp tạm và mẫu ghi nguyên tử ở lesson 16: tạo tệp tạm, ghi, đổi tên khi thoát bình thường, xoá khi lỗi. Kết hợp với tín hiệu ở lesson 21: bị giết cưỡng bức thì trình quản lý ngữ cảnh không chạy, nên vẫn cần dọn dẹp lúc khởi động.

**Outcome.** Viết một trình quản lý ngữ cảnh ghi nguyên tử và chứng minh nó không để lại tệp dở ở cả trường hợp lỗi lẫn trường hợp bị giết.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí kiểm bằng thực nghiệm lặp lại, nối tiếp lesson 16 nhưng ở tầng mã. Đạt khi 30 lần bơm lỗi và 30 lần giết cưỡng bức đều không để lại tệp dở, và khi lần khởi động sau dọn được tệp tạm còn sót từ lần bị giết.

**Lab.** Viết trình quản lý ngữ cảnh ghi nguyên tử. Bơm ngoại lệ giữa chừng 30 lần và giết cưỡng bức 30 lần. Kiểm tra thư mục đích sau mỗi lần. Thêm bước dọn tệp tạm lúc khởi động và xác nhận nó chạy. Viết thêm một trình quản lý ngữ cảnh cho giao dịch cơ sở dữ liệu.

**Pitfalls.** Mở tệp trong vòng lặp mà không dùng trình quản lý ngữ cảnh · giả định trình quản lý ngữ cảnh chạy khi bị giết cưỡng bức · quên nhánh hoàn tác khi viết tay.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** 30 lần bơm lỗi và 30 lần giết đều không để lại tệp dở, và bước dọn lúc khởi động xử lý được tệp tạm còn sót.

### Lesson 67 · Dataclasses, type hints and making shape explicit `TH`
**Prerequisites.** Lesson 66

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Gợi ý kiểu không được thực thi lúc chạy, chúng là tài liệu cho người đọc và đầu vào cho công cụ kiểm kiểu tĩnh ở lesson 83. Giá trị thật của chúng trong mã dữ liệu: khai báo hình dạng của một bản ghi ở một chỗ thay vì để nó ngầm trong các lượt truy cập từ điển rải khắp mã. Lớp dữ liệu sinh sẵn hàm khởi tạo và phép so sánh, và tuỳ chọn đóng băng để bất biến, nối lại lesson 55. Lớp dữ liệu so với từ điển cho một bản ghi: lớp bắt được lỗi gõ sai tên trường lúc kiểm kiểu còn từ điển thì không, nhưng từ điển linh hoạt hơn khi lược đồ nguồn thay đổi. Tiêu chí chọn giữa hai cái theo tầng: dùng từ điển ở biên nhận dữ liệu thô, chuyển sang lớp dữ liệu sau khi đã xác thực. Kiểu tuỳ chọn và vì sao khai báo rõ trường nào có thể rỗng quan trọng hơn khai báo kiểu của nó. Thư viện xác thực dữ liệu lúc chạy và ranh giới với gợi ý kiểu tĩnh.

**Outcome.** Chuyển một đoạn mã dùng từ điển thô sang lớp dữ liệu có gợi ý kiểu, và chỉ ra ba lỗi mà công cụ kiểm kiểu bắt được sau khi chuyển.

**Đánh giá.** Tầng *áp dụng*. Objective gồm một phép tái cấu trúc và một bằng chứng cụ thể về lợi ích. Đạt khi công cụ kiểm kiểu báo đúng ba lỗi cố ý cài vào và không báo lỗi giả ở phần còn lại. Chuyển xong mà công cụ kiểm kiểu không bắt được gì thì chưa đạt.

**Lab.** Nhận đoạn mã 200 dòng xử lý bản ghi đơn hàng bằng từ điển thô. Chuyển sang lớp dữ liệu có gợi ý kiểu. Cài ba lỗi: gõ sai tên trường, dùng sai kiểu, quên xử lý trường rỗng. Chạy công cụ kiểm kiểu và xác nhận nó bắt đủ ba.

**Pitfalls.** Gắn gợi ý kiểu rồi tưởng nó được kiểm lúc chạy · dùng lớp dữ liệu ở biên nhận dữ liệu thô nên vỡ khi nguồn đổi lược đồ · bỏ qua việc khai báo trường có thể rỗng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Công cụ kiểm kiểu bắt đúng ba lỗi cài sẵn và không báo lỗi giả ở phần còn lại.

### Lesson 68 · Modules, packages and imports `TH`
**Prerequisites.** Lesson 67

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Mô đun là một tệp, gói là một thư mục có tệp khởi tạo. Đường dẫn tìm kiếm mô đun và thứ tự tra cứu, nguyên nhân của phần lớn lỗi không tìm thấy mô đun. Nhập tuyệt đối so với nhập tương đối và vì sao nhập tuyệt đối dễ đọc và dễ di chuyển hơn. Nhập vòng: cơ chế, triệu chứng, và ba cách phá vòng. Mã ở tầng ngoài mô đun chạy lúc nhập, nối thẳng tới bẫy ở chặng 5 khi công cụ điều phối đọc lại tệp định nghĩa đồ thị nhiều lần mỗi phút. Khối bảo vệ điểm vào và vì sao nó bắt buộc khi dùng nhiều tiến trình ở lesson 59. Cấu trúc gói cho một dự án dữ liệu: tách phần đọc nguồn, phần biến đổi, phần ghi đích, và phần điều phối, để phần biến đổi kiểm thử được mà không cần cơ sở dữ liệu. Cài gói ở chế độ chỉnh sửa được để nhập từ thư mục kiểm thử. Ranh giới giữa mô đun và cấu hình.

**Outcome.** Tổ chức một script một tệp thành gói có bốn phần tách bạch, sao cho phần biến đổi kiểm thử được không cần cơ sở dữ liệu.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí kiểm được: phần biến đổi phải chạy kiểm thử mà không kết nối gì. Đạt khi bộ kiểm thử cho phần biến đổi chạy xanh với mạng bị chặn và không có cơ sở dữ liệu, và khi toàn bộ gói vẫn chạy được đầu cuối.

**Lab.** Nhận script 400 dòng làm mọi thứ trong một tệp. Tách thành gói bốn phần. Viết kiểm thử cho phần biến đổi, chạy với mạng bị chặn. Tạo một nhập vòng có chủ đích, quan sát lỗi, rồi phá vòng bằng một trong ba cách.

**Pitfalls.** Đặt mã nặng ở tầng ngoài mô đun · dùng nhập tương đối nhiều tầng rồi không di chuyển tệp được · trộn phần biến đổi với phần kết nối nên không kiểm thử được.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Kiểm thử phần biến đổi chạy xanh khi chặn mạng và không có cơ sở dữ liệu, và gói vẫn chạy được đầu cuối.

### Lesson 69 · Reading and writing CSV and JSON correctly `TH`
**Prerequisites.** Lesson 68

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** CSV không có chuẩn thống nhất, nên mọi giả định về nó đều phải kiểm. Bốn tham số quyết định kết quả và phải khai báo rõ: ký tự phân cách, ký tự bao chuỗi, ký tự thoát, và ký tự xuống dòng. Trường chứa chính ký tự phân cách, trường chứa dấu xuống dòng, và cơ chế chúng làm số cột thay đổi giữa các dòng. Bảng mã và ký tự đánh dấu đầu tệp, nối lại lesson 8. Không có kiểu dữ liệu trong CSV nên mọi thứ là chuỗi, và việc tự đoán kiểu là nguồn lỗi âm thầm: số điện thoại mất số 0 đầu, mã sản phẩm thành số khoa học. Đọc CSV theo luồng bằng bộ đọc chuẩn thay vì nạp hết. JSON và JSON theo dòng: cái sau xử lý theo luồng được còn cái trước thì không, nên định dạng theo dòng là lựa chọn mặc định cho dữ liệu lớn. JSON lồng sâu và làm phẳng có kiểm soát. Số lớn trong JSON mất độ chính xác khi qua dấu phẩy động, nối lại lesson 7.

**Outcome.** Đọc một tệp CSV có đủ bốn loại bẫy và chứng minh số dòng cùng số cột đúng, không để công cụ tự đoán kiểu.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí đối chứng tuyệt đối. Đạt khi số dòng và số cột khớp đáp án, và khi bốn cột bẫy giữ nguyên giá trị gốc dưới dạng chuỗi. Một cột bị tự đoán kiểu làm mất số 0 đầu là không đạt.

**Lab.** Nhận tệp CSV có trường chứa ký tự phân cách, trường chứa dấu xuống dòng, cột số điện thoại có số 0 đầu, và cột mã dài 18 chữ số. Đọc theo luồng, khai báo rõ bốn tham số, tắt tự đoán kiểu. Đối chiếu số dòng, số cột và giá trị bốn cột bẫy.

**Pitfalls.** Tách dòng bằng dấu phẩy thay vì dùng bộ đọc CSV · để công cụ tự đoán kiểu · nạp cả tệp JSON lồng vào bộ nhớ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Số dòng và số cột khớp đáp án, và bốn cột bẫy giữ nguyên giá trị gốc.

### Lesson 70 · Parquet and columnar files `TH`
**Prerequisites.** Lesson 69

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Định dạng cột lưu dữ liệu theo cột thay vì theo dòng, nối thẳng lesson 41. Ba hệ quả đo được: nén tốt hơn vì giá trị cùng cột giống nhau, đọc một phần cột không phải đọc cả dòng, và phép gộp trên một cột tận dụng dòng bộ nhớ đệm. Cấu trúc tệp: nhóm dòng, khối cột, và siêu dữ liệu ở cuối tệp. Thống kê nhỏ nhất lớn nhất theo nhóm dòng cho phép bỏ qua cả nhóm khi lọc, cơ chế gọi là cắt tỉa và là nền của phân vùng ở chặng 7. Kích thước nhóm dòng và đánh đổi: nhóm lớn nén tốt và cắt tỉa thô, nhóm nhỏ ngược lại. Lược đồ nằm trong tệp nên kiểu dữ liệu không bị đoán như CSV. Thuật toán nén và đánh đổi giữa tỉ lệ nén với thời gian bộ xử lý. Vấn đề nhiều tệp nhỏ, nối lại lesson 15: mỗi tệp có phần đầu và phần siêu dữ liệu nên chia quá nhỏ thì phần thừa lấn át dữ liệu.

**Outcome.** Đo chênh lệch kích thước và thời gian đọc giữa CSV và định dạng cột trên cùng dữ liệu, và chứng minh cắt tỉa theo thống kê có hiệu lực.

**Đánh giá.** Tầng *phân tích*. Objective đòi nối số đo với cơ chế bên trong định dạng. Đạt khi có bảng số đo cho ít nhất ba kiểu truy vấn, và khi người học chứng minh được cắt tỉa hoạt động bằng cách so số byte đọc thật với kích thước tệp, không chỉ bằng thời gian.

**Lab.** Chuyển một tập 20 ghi ga byte từ CSV sang định dạng cột ở ba kích thước nhóm dòng. Chạy ba truy vấn: lấy một cột, lọc theo khoảng hẹp trên cột đã sắp, và gộp toàn bảng. Đo kích thước tệp, số byte đọc thật và thời gian cho từng cấu hình.

**Pitfalls.** Chia dữ liệu thành hàng nghìn tệp nhỏ · ghi không sắp theo cột lọc nên cắt tỉa vô hiệu · chọn nén mạnh nhất mà không đo chi phí bộ xử lý.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng số đo đủ ba truy vấn nhân ba kích thước nhóm dòng, và cắt tỉa được chứng minh bằng số byte đọc thật.

### Lesson 71 · Chunking and streaming large files `TH`
**Prerequisites.** Lesson 70

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba chiến lược xử lý dữ liệu lớn hơn bộ nhớ và điều kiện áp dụng. Xử lý theo luồng từng bản ghi cho bộ nhớ hằng số nhưng chỉ làm được phép biến đổi không cần nhìn toàn cục. Xử lý theo khối cân bằng giữa bộ nhớ và chi phí gọi, và là lựa chọn mặc định. Chia để trị cho phép toán cần toàn cục như sắp xếp và gộp nhóm trên khoá nhiều giá trị, nối lại lesson 43 và 48. Chọn kích thước khối bằng thực nghiệm: quá nhỏ thì chi phí gọi lấn át, quá lớn thì bộ nhớ đỉnh lớn và rủi ro bị giết. Phép gộp tăng dần giữ trạng thái nhỏ: tổng, đếm, nhỏ nhất, lớn nhất làm được theo luồng; trung vị và đếm giá trị phân biệt chính xác thì không, nối lại lesson 45 và 47. Ghi ra theo khối và điểm kiểm tra sau mỗi khối để chạy lại được, nối lại lesson 35. Đọc nhiều tệp như một luồng liên tục và giữ được thông tin tệp nguồn cho mỗi bản ghi.

**Outcome.** Chọn kích thước khối cho thông lượng cao nhất trong ràng buộc bộ nhớ cho trước, và cài phép gộp tăng dần giữ trạng thái nhỏ.

**Đánh giá.** Tầng *đánh giá*. Objective đòi tinh chỉnh một tham số có đánh đổi hai chiều và biện minh bằng số. Đạt khi bảng thực nghiệm có ít nhất bốn kích thước khối kèm thời gian và bộ nhớ đỉnh, khi lựa chọn không vượt ràng buộc bộ nhớ, và khi kết quả gộp khớp đáp án.

**Lab.** Xử lý 50 ghi ga byte với giới hạn 3 ghi ga byte bộ nhớ. Chạy ở bốn kích thước khối. Đo thông lượng và bộ nhớ đỉnh. Cài bốn phép gộp tăng dần và một phép cần toàn cục, xử lý phép cuối bằng chia để trị. Thêm điểm kiểm tra sau mỗi khối và thử giết giữa chừng.

**Pitfalls.** Chọn kích thước khối bằng cảm tính · tích luỹ kết quả từng khối vào một danh sách trong bộ nhớ · ghi điểm kiểm tra trước khi ghi dữ liệu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng bốn kích thước khối có thời gian và bộ nhớ đỉnh, lựa chọn nằm trong ràng buộc, và kết quả gộp khớp đáp án.

### Lesson 72 · Database drivers, cursors and parameterized queries `TH`
**Prerequisites.** Lesson 71

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Trình điều khiển và giao diện chuẩn. Kết nối, con trỏ, và vòng đời của cả hai. Con trỏ phía máy chủ trả về từng khối thay vì tải hết kết quả về máy khách, bắt buộc khi kết quả lớn hơn bộ nhớ, và đây là lỗi hay gặp: truy vấn chạy được trên bảng nhỏ rồi chết trên bảng lớn. Truy vấn tham số hoá và cơ chế chèn mã độc khi ghép chuỗi: không chỉ là vấn đề bảo mật mà còn là vấn đề đúng đắn khi dữ liệu chứa dấu nháy. Ghi theo lô và chênh lệch thông lượng so với ghi từng dòng, thường nhiều bậc. Giao dịch, xác nhận và hoàn tác; chế độ tự xác nhận và vì sao nó làm ghi theo lô mất ý nghĩa. Kết nối không an toàn luồng, nối lại lesson 55: mỗi luồng một kết nối riêng hoặc dùng nhóm kết nối, nối lại lesson 36. Thời gian chờ ở tầng truy vấn và tầng kết nối. Đóng tài nguyên bằng trình quản lý ngữ cảnh ở lesson 66.

**Outcome.** Đọc một kết quả truy vấn lớn hơn bộ nhớ bằng con trỏ phía máy chủ, và đo chênh lệch thông lượng giữa ghi từng dòng với ghi theo lô.

**Đánh giá.** Tầng *áp dụng*. Objective gồm một ràng buộc cứng về bộ nhớ và một phép đo. Đạt khi đọc hết 100 triệu dòng trên máy 4 ghi ga byte không bị giết, và khi bảng thông lượng cho thấy chênh lệch giữa ba kích thước lô.

**Lab.** Truy vấn 100 triệu dòng trên máy 4 ghi ga byte. Thử đọc thường, quan sát bị giết. Chuyển sang con trỏ phía máy chủ. Ghi kết quả vào bảng đích theo ba kích thước lô, đo thông lượng. Thử ghép chuỗi truy vấn với dữ liệu chứa dấu nháy và quan sát.

**Pitfalls.** Ghép chuỗi để dựng truy vấn · để chế độ tự xác nhận khi ghi theo lô · dùng chung một kết nối cho nhiều luồng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đọc hết 100 triệu dòng trên máy 4 ghi ga byte không bị giết, và bảng thông lượng có ba kích thước lô.

### Lesson 73 · Memory profiling and finding the leak `TH`
**Prerequisites.** Lesson 72

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bộ nhớ tăng đều là triệu chứng, không phải chẩn đoán. Ba nguyên nhân khác nhau cho cùng triệu chứng: tích luỹ có chủ đích, giữ tham chiếu ngoài ý muốn, và phân mảnh. Đếm tham chiếu và thu gom rác theo chu kỳ; chu kỳ tham chiếu và cơ chế nó giữ đối tượng sống. Ba nơi tham chiếu bị giữ ngoài ý muốn trong mã dữ liệu: bộ nhớ đệm không có giới hạn, danh sách tích luỹ trong vòng lặp, và bao đóng bắt biến lớn. Công cụ đo: chụp ảnh bộ nhớ theo thời gian, so hai ảnh chụp, và tìm loại đối tượng tăng nhiều nhất. Đo bộ nhớ theo dòng mã cho hàm nghi ngờ. Bộ nhớ trả về hệ điều hành chậm hơn bộ nhớ được giải phóng trong tiến trình, nên số đo của hệ điều hành và của môi trường chạy khác nhau và cả hai đều đúng. Quy trình bốn bước tìm rò rỉ, và nguyên tắc tái hiện được trước khi sửa.

**Outcome.** Định vị nguyên nhân một rò rỉ bộ nhớ về đúng một trong ba nhóm, và chứng minh bằng ảnh chụp bộ nhớ trước và sau khi sửa.

**Đánh giá.** Tầng *phân tích*. Objective là chẩn đoán phân biệt ba nguyên nhân có cùng triệu chứng. Kiểm bằng ba chương trình rò rỉ theo ba cơ chế; đạt khi định vị đúng cả ba và dẫn được ảnh chụp bộ nhớ chỉ ra loại đối tượng tăng.

**Lab.** Nhận ba chương trình rò rỉ: bộ nhớ đệm không giới hạn, danh sách tích luỹ trong vòng lặp, và bao đóng giữ khung dữ liệu lớn. Với mỗi cái, chụp ảnh bộ nhớ theo thời gian, so sánh, định vị, sửa, chụp lại. So số đo của hệ điều hành với số đo của môi trường chạy.

**Pitfalls.** Kết luận rò rỉ từ số đo của hệ điều hành một mình · thêm lời gọi thu gom rác thủ công để chữa triệu chứng · sửa mà không tái hiện được trước.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Định vị đúng cả ba nguyên nhân, mỗi cái có ảnh chụp bộ nhớ trước sau chỉ ra loại đối tượng tăng.

### Lesson 74 · Logging with correlation IDs `TH`
**Prerequisites.** Lesson 73

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Nhật ký là thứ duy nhất còn lại khi công việc chạy lúc ba giờ sáng và hỏng. Năm mức nhật ký và tiêu chí dùng từng mức, trong đó mức cảnh báo bị lạm dụng nhiều nhất. Nhật ký có cấu trúc dạng khoá giá trị thay vì câu văn: câu thì người đọc được, khoá giá trị thì máy lọc được, và khi có hàng nghìn dòng mỗi lần chạy thì lọc quan trọng hơn đọc. Mã định danh tương quan gắn vào mọi dòng nhật ký của một lần chạy, để nối được nhật ký khi nhiều lần chạy xen kẽ, và truyền được xuống cả lời gọi mạng ở chặng sau. Bốn thứ mọi công việc dữ liệu phải ghi: số bản ghi vào, số bản ghi ra, số bản ghi bị loại kèm lý do, và thời lượng từng giai đoạn. Không ghi dữ liệu cá nhân vào nhật ký, và cách che trường nhạy cảm. Không dùng lệnh in: nó không có mức, không có dấu thời gian, và không chuyển hướng được. Xoay vòng nhật ký và mất nhật ký cũ.

**Outcome.** Thêm nhật ký có cấu trúc và mã định danh tương quan cho một công việc, sao cho một lần chạy hỏng truy được toàn bộ dòng của chính nó trong nhật ký chung.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí kiểm được bằng thao tác lọc. Đạt khi chạy 20 lần đồng thời rồi lọc theo một mã định danh ra đúng dòng của lần chạy đó, và khi bốn số bắt buộc đều có mặt. Nhật ký đẹp mà không lọc được thì không đạt.

**Lab.** Thêm nhật ký có cấu trúc cho trình nạp ở lesson 65. Chạy 20 lần đồng thời ghi vào cùng một tệp. Lọc theo mã định danh của một lần chạy và xác nhận ra đúng dòng của nó. Thêm che trường nhạy cảm và xác nhận bằng cách tìm chuỗi trong nhật ký.

**Pitfalls.** Dùng lệnh in thay cho nhật ký · ghi câu văn nên không lọc được · ghi cả bản ghi gốc vào nhật ký khi gỡ lỗi rồi lộ dữ liệu cá nhân.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Lọc theo mã định danh ra đúng dòng của một lần chạy trong 20 lần đồng thời, và bốn số bắt buộc đều có.

### Lesson 75 · Configuration, environment variables and secrets `TH`
**Prerequisites.** Lesson 74

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba loại giá trị và chỗ đặt tương ứng: hằng số của mã thì để trong mã, tham số đổi theo môi trường thì để trong cấu hình, thông tin xác thực thì để trong kho bí mật. Thứ tự ưu tiên khi một giá trị xuất hiện nhiều nơi: tham số dòng lệnh, biến môi trường, tệp cấu hình, giá trị mặc định. Vì sao viết cứng đường dẫn và tên máy chủ trong mã làm công việc không chạy được ở môi trường khác. Xác thực cấu hình lúc khởi động thay vì để lỗi nổ ra giữa chừng: thiếu một biến môi trường phải làm chương trình dừng ngay với thông báo rõ. Bí mật không bao giờ nằm trong kho mã, và lịch sử kho vẫn giữ chúng sau khi xoá, nối tới lesson 78. Tệp môi trường cục bộ và bắt buộc đưa vào danh sách bỏ qua. Bí mật trong biến môi trường lộ qua danh sách tiến trình và qua nhật ký gỡ lỗi. Xoay vòng bí mật và vì sao mã phải đọc lại được thay vì đọc một lần lúc khởi động.

**Outcome.** Tách một công việc đang viết cứng cấu hình thành ba lớp, và chứng minh bằng quét rằng không bí mật nào nằm trong kho mã hay nhật ký.

**Đánh giá.** Tầng *áp dụng*. Objective gồm một phép tái cấu trúc và một bằng chứng quét. Đạt khi công việc chạy được ở hai môi trường mà không sửa dòng mã nào, và khi quét toàn bộ lịch sử kho mã cùng nhật ký không ra thông tin xác thực nào.

**Lab.** Nhận công việc viết cứng chuỗi kết nối và đường dẫn. Tách ba lớp. Thêm xác thực cấu hình lúc khởi động. Chạy ở hai môi trường khác nhau không sửa mã. Quét lịch sử kho mã và nhật ký bằng công cụ tìm bí mật.

**Pitfalls.** Nộp tệp môi trường vào kho mã · in toàn bộ cấu hình lúc khởi động kể cả bí mật · để lỗi thiếu cấu hình nổ ra giữa chừng thay vì lúc khởi động.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chạy được ở hai môi trường không sửa mã, và quét lịch sử kho mã cùng nhật ký không ra bí mật nào.

### Lesson 76 · Command line interfaces for data jobs `TH`
**Prerequisites.** Lesson 75

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Công việc dữ liệu chạy bằng lệnh, nên giao diện dòng lệnh là hợp đồng giữa nó với công cụ điều phối ở chặng 5. Bốn nhóm tham số mọi công việc nên có: khoảng dữ liệu xử lý, đường dẫn nguồn và đích, chế độ chạy thử, và mức nhật ký. Tham số khoảng ngày nối thẳng tới ngày logic ở chặng 5: công việc nhận ngày từ ngoài chứ không đọc đồng hồ hệ thống. Chế độ chạy thử in ra việc sẽ làm mà không ghi gì, và nó phải thật sự không ghi. Mã thoát có nghĩa theo quy ước ở lesson 27, vì công cụ điều phối chỉ nhìn mã thoát. Thông báo trợ giúp tự sinh và giá trị mặc định hiển thị được. Lệnh con khi một công cụ làm nhiều việc. Xác thực tham số sớm và thông báo lỗi nói rõ giá trị nào sai. Đọc tham số từ tệp khi danh sách dài. Không hỏi tương tác: công việc chạy tự động không có ai gõ trả lời.

**Outcome.** Đóng gói một công việc thành công cụ dòng lệnh có đủ bốn nhóm tham số, và chứng minh chế độ chạy thử không ghi gì.

**Đánh giá.** Tầng *áp dụng*. Objective có sản phẩm và tiêu chí kiểm chứng rõ. Đạt khi chế độ chạy thử chạy xong mà bảng đích và tệp đích không đổi một byte, và khi ba giá trị tham số sai đều bị từ chối lúc khởi động với thông báo nói rõ giá trị nào sai.

**Lab.** Đóng gói trình nạp thành công cụ dòng lệnh. Chạy chế độ chạy thử, so ảnh chụp thư mục đích và bảng đích trước sau. Thử ba tham số sai: ngày sai định dạng, đường dẫn không tồn tại, mức nhật ký không hợp lệ. Xác nhận mã thoát đúng quy ước.

**Pitfalls.** Đọc ngày từ đồng hồ hệ thống thay vì nhận từ tham số · chế độ chạy thử vẫn ghi vào bảng tạm · hỏi tương tác khi thiếu tham số.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chế độ chạy thử không đổi một byte ở đích, và ba tham số sai đều bị từ chối lúc khởi động với thông báo cụ thể.

### Lesson 77 · Python project - a resumable API loader `DA`
**Prerequisites.** Lesson 76

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Không có nội dung mới. Dự án gộp M7, và nó dùng lại ứng dụng khách HTTP đã đóng gói ở lesson 39. Yêu cầu đầu ra: công cụ dòng lệnh nạp dữ liệu từ một API có phân trang vào cơ sở dữ liệu, xử lý theo luồng nên bộ nhớ không tăng theo kích thước nguồn, có điểm kiểm tra để chạy lại từ chỗ dừng, tách bản ghi lỗi kèm lý do, ghi nhật ký có cấu trúc và mã định danh tương quan, cấu hình ba lớp, và chế độ chạy thử. Tiêu chí đối soát: tổng bản ghi nguồn bằng bản ghi sạch cộng bản ghi lỗi, và chạy hai lần cho kết quả bằng chạy một lần.

**Outcome.** Đóng gói một trình nạp API chạy lại được, và chứng minh bằng đối soát rằng chạy hai lần cho kết quả bằng chạy một lần.

**Đánh giá.** Tầng *sáng tạo*. Objective là thiết kế một hệ thống nhỏ dưới nhiều ràng buộc cùng lúc, không phải ghép mẫu. Chấm theo năm mục: đối soát khớp 30đ, chạy lại từ điểm kiểm tra 25đ, xử lý lỗi và tách bản ghi hỏng 20đ, nhật ký và cấu hình 15đ, tài liệu 10đ. Đạt khi ≥ 70/100 và mục đối soát ≥ 70% của nó, vì đối soát sai thì mọi phần còn lại không cứu được.

**Lab.** Nạp 2 triệu bản ghi từ API lỗi 15% có phân trang và giới hạn tốc độ, trên máy 2 ghi ga byte bộ nhớ. Giết tiến trình 5 lần ở thời điểm ngẫu nhiên, mỗi lần chạy lại từ điểm kiểm tra. Chạy toàn bộ lần thứ hai. Đối soát cả hai điều kiện.

**Pitfalls.** Giữ trạng thái trong bộ nhớ nên mất khi bị giết · ghi điểm kiểm tra trước khi ghi dữ liệu · bỏ qua bản ghi lỗi mà không đếm.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Đạt ≥ 70/100, mục đối soát ≥ 70%, và chạy hai lần cho kết quả bằng chạy một lần.

# MODULE 8 · SOFTWARE ENGINEERING - GIT, TESTING, PACKAGING

**Lessons 78–91 · 28 giờ**

| | |
|---|---|
| **Objective cấp module** | Giao một kho mã mà người khác sao về, chạy một lệnh dựng môi trường, và tái hiện đúng kết quả của mình |
| **Tiền đề** | M7 |
| **Exit criterion** | Đạt Cổng 3 ≥ 70/100: người khác sao kho, chạy một lệnh, CI xanh, và dữ liệu sau hai lần chạy bằng sau một lần |
| **Kỹ năng SFIA** | `PROG` mức 4 · `TEST` mức 3 · `CFMG` mức 3 |
| **Chế độ hỏng** | Viết kiểm thử giả lập mọi thứ nên bộ kiểm thử xanh trong khi pipeline thật ghi sai vào cơ sở dữ liệu |

Module biến mã chạy được thành mã giao được. Bốn bài đầu về Git và kho mã, hai bài giữa về môi trường và công cụ tĩnh, năm bài về kiểm thử ở bốn tầng, hai bài về phát hành và tài liệu, bài cuối là cổng 3. Nguyên tắc xuyên suốt: không giả lập thứ có thể chạy thật, vì giả lập cơ sở dữ liệu là cách chắc chắn nhất để bỏ sót lỗi cơ sở dữ liệu.

### Lesson 78 · Git internals - objects, commits and what a branch really is `LT`
**Prerequisites.** Module 8: M7

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bốn loại đối tượng và quan hệ giữa chúng: khối dữ liệu giữ nội dung tệp, cây giữ cấu trúc thư mục, lần nộp giữ một cây cộng con trỏ tới lần nộp cha, và thẻ. Mọi đối tượng được đặt tên bằng băm nội dung, nên nội dung giống nhau thì chỉ lưu một lần và lịch sử không sửa được mà không đổi mọi băm sau đó. Nhánh chỉ là một con trỏ tới một lần nộp, không phải một bản sao thư mục, và hiểu điều này làm phần lớn thao tác Git hết bí ẩn. Con trỏ đầu và trạng thái đầu rời. Ba vùng: thư mục làm việc, vùng chờ, kho. Vì sao dữ liệu đã nộp vẫn nằm trong lịch sử sau khi xoá tệp, nối thẳng tới bí mật ở lesson 75 và tới lý do phải quét toàn bộ lịch sử chứ không chỉ trạng thái hiện tại. Kích thước kho phình vì nộp tệp dữ liệu lớn, và vì sao không sửa được bằng cách xoá tệp. Danh sách bỏ qua và tệp lớn nên để ngoài.

**Outcome.** Giải thích vì sao xoá một tệp bí mật rồi nộp lại không làm nó biến mất, và chứng minh bằng cách lấy lại nội dung đó từ lịch sử.

**Đánh giá.** Tầng *hiểu*. Objective là giải thích cơ chế và chứng minh hệ quả của nó, không phải thao tác Git nâng cao. Kiểm bằng thực nghiệm: đạt khi lấy lại được nội dung tệp đã xoá từ lịch sử và chỉ ra được đối tượng nào còn giữ nó.

**Lab.** Tạo kho mới, nộp một tệp chứa chuỗi bí mật, xoá tệp, nộp lại. Lấy lại nội dung bí mật từ lịch sử. Liệt kê các đối tượng và chỉ ra khối dữ liệu giữ nội dung đó. Nộp một tệp 200 mê ga byte, xoá, đo kích thước kho trước và sau.

**Pitfalls.** Tin rằng xoá tệp là xoá khỏi lịch sử · nộp tệp dữ liệu lớn vào kho mã · coi nhánh là một bản sao thư mục.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Lấy lại được nội dung bí mật từ lịch sử và chỉ đúng đối tượng giữ nó, kèm số đo kích thước kho trước sau.

### Lesson 79 · Branching, merging, rebasing and resolving conflicts `TH`
**Prerequisites.** Lesson 78

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Gộp tạo một lần nộp có hai cha nên giữ nguyên lịch sử thật; sắp xếp lại viết lại các lần nộp lên trên đỉnh nhánh khác nên lịch sử thẳng nhưng băm đổi. Hệ quả và quy tắc: không sắp xếp lại nhánh đã đẩy lên và người khác đang dùng. Xung đột xảy ra khi hai nhánh sửa cùng vùng, và cách đọc dấu xung đột. Ba loại xung đột trong dự án dữ liệu và cách xử lý: xung đột mã thì giải bằng đọc, xung đột tệp phụ thuộc thì giải bằng dựng lại từ khai báo, xung đột tệp sinh tự động thì giải bằng sinh lại chứ không sửa tay. Chiến lược nhánh cho nhóm nhỏ: nhánh ngắn hạn từ nhánh chính, gộp qua yêu cầu kéo, xoá sau khi gộp. Vì sao nhánh sống lâu tích tụ xung đột theo cấp số nhân. Chọn lấy một lần nộp lẻ. Hoàn tác an toàn bằng lần nộp đảo ngược thay vì viết lại lịch sử. Nhật ký tham chiếu để cứu lần nộp tưởng đã mất.

**Outcome.** Giải ba loại xung đột bằng ba cách khác nhau, và hoàn tác một thay đổi đã đẩy mà không viết lại lịch sử.

**Đánh giá.** Tầng *áp dụng*. Objective gồm ba thao tác có tiêu chí đúng sai rõ. Đạt khi cả ba xung đột được giải mà bộ kiểm thử vẫn xanh, và khi thay đổi đã đẩy được hoàn tác mà băm của các lần nộp cũ không đổi.

**Lab.** Dựng ba xung đột: hai người sửa cùng hàm, hai người thêm phụ thuộc khác nhau, hai người đổi tệp khoá phụ thuộc sinh tự động. Giải từng cái bằng cách phù hợp. Đẩy một lần nộp lỗi rồi hoàn tác bằng lần nộp đảo ngược. Dùng nhật ký tham chiếu cứu một nhánh đã xoá.

**Pitfalls.** Sửa tay tệp khoá phụ thuộc khi xung đột · sắp xếp lại nhánh người khác đang dùng · giải xung đột bằng cách giữ một bên mà không đọc bên kia.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba xung đột giải xong bộ kiểm thử vẫn xanh, và hoàn tác không làm đổi băm các lần nộp cũ.

### Lesson 80 · Pull requests, code review and what to look for in data code `TH`
**Prerequisites.** Lesson 79

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Yêu cầu kéo là đơn vị rà soát, và kích thước của nó quyết định chất lượng rà soát: quá 400 dòng thì người rà soát chuyển sang đọc lướt. Mô tả yêu cầu kéo phải nêu vì sao chứ không nêu cái gì, vì cái gì đã nằm trong khác biệt mã. Danh mục rà soát riêng cho mã dữ liệu, mười điểm khác với rà soát mã ứng dụng thường: mô hình có bất biến khi chạy lại không, có đọc đồng hồ hệ thống không, bản ghi lỗi có bị loại im lặng không, có đối soát số lượng không, giao dịch có được đóng không, truy vấn có tham số hoá không, có nạp cả tệp vào bộ nhớ không, kiểu số cho tiền có đúng không, múi giờ có khai báo không, và bí mật có lọt vào không. Nhận xét rà soát nên nêu hệ quả thay vì nêu sở thích. Phân biệt điều kiện chặn với gợi ý. Tự rà soát trước khi mở yêu cầu kéo. Rà soát là nơi truyền chuẩn của nhóm, không phải nơi bắt lỗi chính tả.

**Outcome.** Rà soát một yêu cầu kéo mã dữ liệu bằng danh mục mười điểm và phân loại mỗi phát hiện thành chặn hay gợi ý.

**Đánh giá.** Tầng *đánh giá*. Objective đòi phán đoán mức nghiêm trọng, không có đáp án máy móc. Kiểm bằng một yêu cầu kéo cài sẵn bảy vấn đề thuộc bảy điểm khác nhau; đạt khi tìm được ít nhất năm trên bảy và khi phân loại chặn hay gợi ý khớp với đáp án cho ít nhất bốn phát hiện.

**Lab.** Nhận yêu cầu kéo 300 dòng cài sẵn bảy vấn đề. Rà soát theo danh mục mười điểm, viết nhận xét nêu hệ quả, phân loại chặn hay gợi ý. Đổi bài chéo: người khác rà soát yêu cầu kéo của bạn và so số phát hiện.

**Pitfalls.** Nhận xét về sở thích định dạng thay vì về hệ quả · duyệt yêu cầu kéo 2.000 dòng · đánh dấu mọi phát hiện là chặn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tìm được ít nhất năm trên bảy vấn đề cài sẵn, và phân loại chặn hay gợi ý khớp đáp án cho ít nhất bốn.

### Lesson 81 · Repository layout for a data project `TH`
**Prerequisites.** Lesson 80

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Cấu trúc thư mục là hợp đồng ngầm với người đọc tiếp theo, nên nó phải nói được ngay cái gì nằm ở đâu. Bốn thư mục lõi và trách nhiệm: mã nguồn, kiểm thử, cấu hình, tài liệu. Tách mã nguồn khỏi thư mục gốc để nhập mô đun không phụ thuộc thư mục đang đứng, nối lại lesson 68. Không để dữ liệu trong kho mã, kể cả dữ liệu mẫu lớn, nối lại lesson 78; thay bằng script sinh dữ liệu có hạt giống cố định. Tệp đầu vào duy nhất và một lệnh chạy toàn bộ, đây chính là điều kiện của cổng 3. Tách phần thuần tuý biến đổi khỏi phần vào ra để kiểm thử được không cần hạ tầng, nối tới lesson 84. Thư mục cho quyết định kiến trúc và sổ tay xử lý, nối lại lesson 4. Tệp bỏ qua đủ rộng: tệp môi trường, tệp tạm, đầu ra sinh ra, và thư mục môi trường ảo. Tệp chủ sở hữu mã khi nhóm lớn dần.

**Outcome.** Tổ chức một dự án dữ liệu theo cấu trúc bốn thư mục lõi sao cho một lệnh chạy được toàn bộ và kiểm thử biến đổi không cần hạ tầng.

**Đánh giá.** Tầng *áp dụng*. Objective có hai tiêu chí kiểm được bằng chạy thật. Đạt khi một lệnh duy nhất dựng môi trường và chạy đầu cuối trên máy sạch, và khi bộ kiểm thử phần biến đổi chạy xanh với mạng bị chặn.

**Lab.** Tổ chức lại dự án ở lesson 77. Viết tệp đầu vào duy nhất. Thay dữ liệu mẫu đính kèm bằng script sinh có hạt giống cố định. Chạy trên máy ảo sạch bằng một lệnh. Chạy kiểm thử biến đổi với mạng bị chặn.

**Pitfalls.** Để tệp dữ liệu mẫu 500 mê ga byte trong kho · đặt mã nguồn ngay thư mục gốc nên nhập mô đun phụ thuộc chỗ đứng · quên đưa thư mục môi trường ảo vào danh sách bỏ qua.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Một lệnh dựng và chạy được đầu cuối trên máy sạch, và kiểm thử biến đổi xanh khi chặn mạng.

### Lesson 82 · Dependency management, pinning and reproducible environments `TH`
**Prerequisites.** Lesson 81

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phụ thuộc trực tiếp và phụ thuộc bắc cầu; phần lớn rủi ro nằm ở cái sau vì không ai đọc chúng. Khoảng phiên bản so với ghim chính xác: khoảng cho cập nhật tự động nhưng làm hai lần cài ra hai môi trường khác nhau, ghim cho tái lập được nhưng phải cập nhật bằng tay. Tệp khai báo cho phụ thuộc trực tiếp và tệp khoá cho toàn bộ cây đã giải, và cả hai đều phải nộp vào kho. Băm của gói trong tệp khoá để phát hiện gói bị thay. Môi trường ảo và cô lập giữa các dự án, nối lại lesson 24 về nhóm điều khiển và không gian tên: cùng ý tưởng cô lập ở tầng khác. Lệnh cài đặt lặp lại được từ tệp khoá thay vì từ tệp khai báo. Xung đột phụ thuộc và vì sao thêm một thư viện có thể hạ cấp một thư viện khác. Quét lỗ hổng bảo mật trong cây phụ thuộc. Quy trình nâng cấp có kiểm soát: nâng một thứ, chạy kiểm thử, nộp riêng.

**Outcome.** Dựng lại đúng môi trường của người khác từ tệp khoá, và chứng minh hai lần cài trên hai máy cho cùng danh sách phiên bản.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí đối chứng tuyệt đối. Đạt khi danh sách phiên bản đã giải trên hai máy khác nhau khớp từng dòng, và khi cài từ tệp khai báo không ghim cho ra khác biệt đo được để thấy lý do phải khoá.

**Lab.** Cài từ tệp khai báo không ghim trên hai máy cách nhau một tuần, so danh sách phiên bản. Sinh tệp khoá, cài lại trên cả hai, so lại. Thêm một thư viện và quan sát nó hạ cấp thư viện khác. Chạy quét lỗ hổng.

**Pitfalls.** Chỉ nộp tệp khai báo mà không nộp tệp khoá · cập nhật hàng loạt phụ thuộc trong một lần nộp · cài thẳng vào môi trường hệ thống.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Danh sách phiên bản trên hai máy khớp từng dòng khi cài từ tệp khoá, và khác biệt đo được khi cài không ghim.

### Lesson 83 · Lint, format and type check in one command `TH`
**Prerequisites.** Lesson 82

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba loại công cụ tĩnh và cái mỗi loại bắt: định dạng lo hình thức nên không tranh cãi được, kiểm tra tĩnh bắt lỗi khả nghi như biến không dùng và ngoại lệ bắt quá rộng ở lesson 65, kiểm kiểu bắt lỗi kiểu nhờ gợi ý kiểu ở lesson 67. Chúng bắt được gì và không bắt được gì: không công cụ nào bắt được lỗi logic hay lỗi dữ liệu, nên chúng là điều kiện cần chứ không phải đủ. Cấu hình tập trung ở một tệp và nộp vào kho để cả nhóm dùng chung. Chạy tự động trước mỗi lần nộp, và vì sao chạy ở máy cá nhân trước rẻ hơn chạy ở CI. Áp dụng dần cho kho mã cũ bằng cách bật từng quy tắc thay vì bật hết rồi ngập trong cảnh báo. Bỏ qua một cảnh báo phải kèm lý do viết tại chỗ, không bỏ qua toàn cục. Kiểm kiểu nghiêm ngặt dần theo mô đun. Thời gian chạy của cả ba phải dưới một ngưỡng để người ta còn chạy.

**Outcome.** Cấu hình ba công cụ tĩnh chạy bằng một lệnh dưới 30 giây, và áp dụng dần cho một kho mã cũ mà không phải sửa hết cùng lúc.

**Đánh giá.** Tầng *áp dụng*. Objective có ràng buộc thời gian và ràng buộc áp dụng dần, cả hai kiểm được. Đạt khi một lệnh chạy cả ba dưới 30 giây trên kho mã của dự án, và khi kho mã cũ đi từ hàng trăm cảnh báo xuống 0 mà mỗi bước nộp đều xanh.

**Lab.** Cấu hình ba công cụ vào một tệp và một lệnh. Đo thời gian chạy. Áp lên kho mã cũ có 400 cảnh báo: bật từng nhóm quy tắc, sửa, nộp, lặp lại cho tới 0. Cài móc chạy trước khi nộp. Thử bỏ qua một cảnh báo kèm lý do tại chỗ.

**Pitfalls.** Bật mọi quy tắc cùng lúc rồi tắt hết vì quá nhiều · bỏ qua cảnh báo ở mức toàn cục · tin rằng ba công cụ xanh nghĩa là mã đúng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Một lệnh chạy cả ba dưới 30 giây, và kho mã cũ về 0 cảnh báo với mọi bước nộp trung gian đều xanh.

### Lesson 84 · Unit tests for pure transformation functions `TH`
**Prerequisites.** Lesson 83

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hàm thuần nhận đầu vào trả đầu ra không chạm thế giới ngoài, nên kiểm thử nó nhanh và tất định. Đây là lý do tách phần biến đổi khỏi phần vào ra ở lesson 68 và 81: để phần lớn logic nằm trong hàm thuần. Cấu trúc một kiểm thử ba phần: dựng, chạy, khẳng định. Một kiểm thử kiểm một điều, và tên kiểm thử nói điều kiện cùng kết quả mong đợi. Dữ liệu cố định nhỏ và đặt ngay trong kiểm thử để đọc được, không nạp từ tệp ngoài. Sáu trường hợp biên bắt buộc cho mọi biến đổi dữ liệu: đầu vào rỗng, một bản ghi, giá trị rỗng ở mọi cột, giá trị trùng, giá trị biên của khoảng số, và ngày ở ranh giới múi giờ. Kiểm thử tham số hoá cho nhiều bộ đầu vào. Độ phủ là chỉ báo chứ không phải mục tiêu: 100% độ phủ với khẳng định yếu không chứng minh gì. Kiểm thử phải chạy nhanh để người ta còn chạy thường xuyên.

**Outcome.** Viết kiểm thử đơn vị cho một biến đổi phủ đủ sáu trường hợp biên, và chứng minh chúng bắt được lỗi bằng cách cố ý làm hỏng mã.

**Đánh giá.** Tầng *áp dụng*. Objective đòi chứng minh bộ kiểm thử có tác dụng, không chỉ đòi viết kiểm thử. Kiểm bằng kiểm thử đột biến thủ công: cài năm lỗi nhỏ vào mã biến đổi. Đạt khi bộ kiểm thử bắt được ít nhất bốn trên năm. Độ phủ cao mà không bắt được lỗi thì không đạt.

**Lab.** Viết kiểm thử đơn vị cho hàm chuẩn hoá và gộp ở lesson 77, phủ sáu trường hợp biên. Đo thời gian chạy toàn bộ. Cài năm lỗi nhỏ: đảo dấu so sánh, lệch một đơn vị, bỏ xử lý giá trị rỗng, sai múi giờ, sai thứ tự làm tròn. Chạy và đếm số lỗi bị bắt.

**Pitfalls.** Viết kiểm thử chỉ cho đường thuận · nạp dữ liệu kiểm thử từ tệp lớn ngoài · dùng độ phủ làm mục tiêu thay vì làm chỉ báo.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bộ kiểm thử bắt ít nhất bốn trên năm lỗi cài sẵn, và chạy toàn bộ dưới ngưỡng thời gian đã đặt.

### Lesson 85 · Integration tests against a real database `TH`
**Prerequisites.** Lesson 84

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Kiểm thử tích hợp chạy trên hạ tầng thật vì lỗi cơ sở dữ liệu chỉ lộ ra ở cơ sở dữ liệu. Giả lập cơ sở dữ liệu là cách chắc chắn nhất để bỏ sót lỗi kiểu dữ liệu, lỗi ràng buộc, lỗi giao dịch và lỗi cú pháp riêng của hệ đó. Dựng cơ sở dữ liệu tạm cho kiểm thử bằng vùng chứa dùng một lần, khởi tạo lược đồ, chạy, rồi bỏ. Cô lập giữa các kiểm thử: mỗi kiểm thử một lược đồ riêng hoặc hoàn tác giao dịch sau mỗi kiểm thử, và đánh đổi giữa hai cách. Dữ liệu mồi tối thiểu đủ để kiểm điều đang kiểm, không mồi cả cơ sở dữ liệu. Kiểm thử phải chạy lại được nhiều lần mà cho cùng kết quả, nên không phụ thuộc thứ tự chạy và không phụ thuộc dữ liệu còn sót. Tốc độ: kiểm thử tích hợp chậm hơn đơn vị nhiều bậc nên chia hai nhóm chạy riêng, nối tới lesson 88. Điều gì nên kiểm ở tầng này và điều gì để tầng dưới.

**Outcome.** Viết kiểm thử tích hợp chạy trên cơ sở dữ liệu thật dùng một lần, và chứng minh chúng chạy lại được nhiều lần cho cùng kết quả bất kể thứ tự.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí kiểm được bằng chạy lặp và chạy xáo thứ tự. Đạt khi chạy bộ kiểm thử 10 lần liên tiếp và 5 lần với thứ tự ngẫu nhiên đều cho cùng kết quả, và khi ít nhất một kiểm thử bắt được lỗi mà kiểm thử đơn vị giả lập không bắt được.

**Lab.** Viết kiểm thử tích hợp cho phần ghi của dự án lesson 77, dùng vùng chứa cơ sở dữ liệu dùng một lần. Chạy 10 lần liên tiếp và 5 lần xáo thứ tự. Cài một lỗi vi phạm ràng buộc khoá và xác nhận bản giả lập không bắt được còn bản thật bắt được.

**Pitfalls.** Giả lập cơ sở dữ liệu để chạy nhanh · dùng chung một cơ sở dữ liệu giữa các kiểm thử nên phụ thuộc thứ tự · mồi cả cơ sở dữ liệu cho mỗi kiểm thử.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** 10 lần chạy liên tiếp và 5 lần xáo thứ tự đều cùng kết quả, và ít nhất một lỗi chỉ bản thật bắt được.

### Lesson 86 · Property-based testing for data transformations `TH`
**Prerequisites.** Lesson 85

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Kiểm thử theo ví dụ kiểm những trường hợp người viết nghĩ ra; kiểm thử theo tính chất phát biểu điều phải luôn đúng rồi để máy sinh đầu vào tìm phản ví dụ. Nó mạnh đúng ở chỗ con người yếu: các tổ hợp không ai nghĩ tới. Năm tính chất hay dùng cho biến đổi dữ liệu: số dòng ra có quan hệ xác định với số dòng vào, tổng theo khoá nghiệp vụ được bảo toàn, chạy hai lần bằng chạy một lần, thứ tự đầu vào không ảnh hưởng kết quả, và biến đổi rồi đảo ngược trả về bản gốc. Tính chất thứ ba chính là bất biến khi chạy lại và là tiêu chí xuyên suốt chương trình. Sinh dữ liệu có ràng buộc để đầu vào hợp lệ. Thu nhỏ phản ví dụ về trường hợp nhỏ nhất còn hỏng, tính năng làm kỹ thuật này đáng dùng. Ghi lại hạt giống để tái hiện ca hỏng, nối lại lesson 60. Khi nào kiểm thử theo tính chất không hợp: khi không phát biểu được tính chất nào rõ ràng.

**Outcome.** Phát biểu năm tính chất cho một biến đổi và tìm phản ví dụ cho ít nhất một tính chất bị vi phạm.

**Đánh giá.** Tầng *phân tích*. Objective đòi phát biểu tính chất đúng và đọc được phản ví dụ, không chỉ chạy công cụ. Đạt khi năm tính chất phát biểu được bằng mã chạy được, và khi tìm ra phản ví dụ cho lỗi cài sẵn cùng bản thu nhỏ của nó.

**Lab.** Phát biểu năm tính chất cho biến đổi ở lesson 77. Chạy với 10.000 đầu vào sinh tự nhiên. Cài một lỗi chỉ hỏng khi có giá trị rỗng trong khoá gộp. Chạy lại, đọc phản ví dụ và bản thu nhỏ. Ghi hạt giống, tái hiện.

**Pitfalls.** Phát biểu tính chất quá yếu nên không bao giờ hỏng · sinh đầu vào không hợp lệ rồi kiểm thử hỏng vì lý do sai · không ghi hạt giống nên không tái hiện được.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Năm tính chất phát biểu bằng mã chạy được, và tìm ra phản ví dụ cùng bản thu nhỏ cho lỗi cài sẵn.

### Lesson 87 · Contract tests for schemas `TH`
**Prerequisites.** Lesson 86

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hợp đồng lược đồ phát biểu hình dạng dữ liệu hai bên thoả thuận, và kiểm thử hợp đồng kiểm nó tự động ở biên. Hai hướng cần kiểm và chúng khác nhau: nguồn có còn cung cấp đúng thứ mình giả định không, và mình có còn tạo ra đúng thứ hạ nguồn giả định không. Nội dung một hợp đồng: tên cột, kiểu, trường bắt buộc, dải giá trị hợp lệ, và ngữ nghĩa khoá. Thay đổi tương thích ngược so với thay đổi phá vỡ: thêm cột tuỳ chọn thì tương thích, xoá cột hay đổi kiểu thì phá vỡ. Ba phản ứng khi nguồn thêm cột và tiêu chí chọn, nối tới chặng 4. Kiểm hợp đồng chạy ở đâu: ở CI trên mẫu dữ liệu cố định, và ở thời điểm chạy thật trên dữ liệu thật, hai chỗ bắt hai loại vấn đề khác nhau. Phiên bản hoá hợp đồng và thời gian chuyển tiếp khi đổi. Vì sao phát hiện sớm rẻ hơn nhiều so với phát hiện ở bảng điều khiển.

**Outcome.** Viết hợp đồng lược đồ cho một nguồn và một đích, và chứng minh kiểm thử bắt được cả thay đổi phá vỡ lẫn thay đổi tương thích, phân loại đúng từng loại.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí phân loại kiểm được. Đạt khi sáu thay đổi lược đồ được phân loại đúng cả sáu, trong đó thay đổi phá vỡ làm kiểm thử đỏ còn thay đổi tương thích thì không, và khi kiểm ở thời điểm chạy bắt được một vấn đề mà kiểm ở CI không bắt được.

**Lab.** Viết hợp đồng cho nguồn và đích của dự án lesson 77. Cài sáu thay đổi: thêm cột tuỳ chọn, thêm cột bắt buộc, xoá cột, đổi kiểu, đổi ngữ nghĩa khoá, nới dải giá trị. Chạy kiểm hợp đồng ở CI và ở thời điểm chạy, so kết quả.

**Pitfalls.** Chỉ kiểm hợp đồng ở CI nên không bắt được dữ liệu thật lệch · coi mọi thay đổi lược đồ là phá vỡ · không phiên bản hoá hợp đồng nên đổi là vỡ ngay.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Sáu thay đổi phân loại đúng cả sáu, và kiểm ở thời điểm chạy bắt được vấn đề mà CI không bắt.

### Lesson 88 · Continuous integration that runs in under ten minutes `TH`
**Prerequisites.** Lesson 87

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** CI chỉ có giá trị nếu người ta chờ nó, nên thời gian chạy là ràng buộc thiết kế chứ không phải kết quả. Bốn giai đoạn theo thứ tự chi phí tăng dần và nguyên tắc dừng sớm: công cụ tĩnh, kiểm thử đơn vị, kiểm thử tích hợp, kiểm thử hợp đồng. Chạy song song các giai đoạn độc lập. Bộ nhớ đệm phụ thuộc giữa các lần chạy và cách khoá bộ đệm theo tệp khoá ở lesson 82. Dịch vụ phụ trợ cho kiểm thử tích hợp và chờ tới khi sẵn sàng thay vì ngủ một khoảng cố định. Bí mật trong CI và nguyên tắc không in ra nhật ký, nối lại lesson 75. Kiểm thử chập chờn là thứ giết CI nhanh nhất: nguyên nhân thường gặp là phụ thuộc thời gian, phụ thuộc thứ tự, và tranh chấp ở lesson 51; quy trình xử lý là cách ly rồi sửa chứ không phải thử lại tự động. Ngân sách thời gian cho từng giai đoạn và cắt gì khi vượt. CI xanh là điều kiện gộp, không phải gợi ý.

**Outcome.** Dựng CI chạy đủ bốn giai đoạn dưới 10 phút, và xử lý một kiểm thử chập chờn tới nguyên nhân gốc thay vì thử lại.

**Đánh giá.** Tầng *áp dụng*. Objective có ràng buộc thời gian cứng và một tiêu chí về cách xử lý. Đạt khi CI chạy đủ bốn giai đoạn dưới 10 phút, và khi kiểm thử chập chờn cài sẵn được truy về nguyên nhân gốc với bằng chứng, không được xử lý bằng thử lại.

**Lab.** Dựng CI bốn giai đoạn cho dự án. Đo thời gian từng giai đoạn. Thêm bộ nhớ đệm phụ thuộc và đo lại. Cài một kiểm thử chập chờn do tranh chấp, chạy CI 30 lần, quan sát tỉ lệ đỏ, truy nguyên và sửa.

**Pitfalls.** Thêm thử lại tự động cho kiểm thử chập chờn · chạy kiểm thử tích hợp trước kiểm thử đơn vị · ngủ một khoảng cố định để chờ dịch vụ phụ trợ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** CI chạy đủ bốn giai đoạn dưới 10 phút, và kiểm thử chập chờn được truy về nguyên nhân gốc có bằng chứng.

### Lesson 89 · Tags, releases and versioning a data job `TH`
**Prerequisites.** Lesson 88

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phiên bản hoá ngữ nghĩa và ba thành phần của nó, cùng câu hỏi đặc thù cho công việc dữ liệu: cái gì tính là thay đổi phá vỡ khi sản phẩm là một bảng chứ không phải một thư viện. Ba loại thay đổi phá vỡ ở tầng dữ liệu: đổi lược đồ đầu ra, đổi ngữ nghĩa một cột mà không đổi tên, và đổi hạt của bảng. Loại thứ hai nguy hiểm nhất vì không có tín hiệu kỹ thuật nào. Thẻ gắn vào một lần nộp và khác nhánh ở chỗ nó không di chuyển. Nhật ký thay đổi viết cho người dùng dữ liệu chứ không cho lập trình viên: nêu số nào đổi và đổi từ khi nào. Gắn phiên bản mã vào dữ liệu đầu ra để truy được bảng này do bản nào sinh ra, một thực hành rẻ và cứu được nhiều giờ điều tra. Quay lui mã không quay lui được dữ liệu đã ghi, nên phải có kế hoạch chạy lại. Môi trường và quy trình phát hành, chuẩn bị cho chặng 7.

**Outcome.** Phát hành một phiên bản có thẻ và nhật ký thay đổi, và gắn được phiên bản mã vào dữ liệu đầu ra để truy ngược.

**Đánh giá.** Tầng *áp dụng*. Objective có sản phẩm và một tiêu chí truy ngược kiểm được. Đạt khi từ một dòng dữ liệu bất kỳ trong bảng đích truy được về đúng lần nộp sinh ra nó, và khi nhật ký thay đổi nêu được thay đổi ngữ nghĩa bằng ngôn ngữ người dùng dữ liệu hiểu.

**Lab.** Phát hành ba phiên bản liên tiếp của công việc, trong đó một phiên bản đổi ngữ nghĩa một cột. Gắn phiên bản mã vào mỗi dòng đầu ra. Chọn ngẫu nhiên 10 dòng trong bảng và truy về lần nộp. Viết nhật ký thay đổi cho người dùng dữ liệu.

**Pitfalls.** Coi đổi ngữ nghĩa cột là thay đổi nhỏ vì lược đồ không đổi · viết nhật ký thay đổi bằng ngôn ngữ lập trình viên · tin rằng quay lui mã là quay lui dữ liệu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Truy được 10 dòng ngẫu nhiên về đúng lần nộp sinh ra chúng, và nhật ký thay đổi nêu rõ thay đổi ngữ nghĩa.

### Lesson 90 · Documentation that survives - README, ADR, runbook `TH`
**Prerequisites.** Lesson 89

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba loại tài liệu phục vụ ba câu hỏi khác nhau và không thay thế nhau. Tài liệu giới thiệu trả lời làm sao chạy được: bảy phần gồm mục đích, yêu cầu, cài đặt, dữ liệu, cách chạy, đầu ra, và giới hạn đã biết. Bản ghi quyết định kiến trúc trả lời vì sao làm thế này: bối cảnh, các phương án đã cân nhắc, lý do loại từng phương án, và tín hiệu khiến nên xem lại. Phần phương án bị loại là phần có giá trị nhất và là phần hay bị bỏ. Sổ tay xử lý trả lời hỏng thì làm gì: triệu chứng, cách xác nhận, các bước xử lý, và cách biết đã xong. Sổ tay viết cho người trực lúc ba giờ sáng không có ngữ cảnh, nên mỗi bước phải là lệnh chạy được chứ không phải mô tả. Tiêu chí duy nhất để đánh giá tài liệu: người khác làm theo được mà không hỏi. Tài liệu chết vì không cập nhật, và cách chống là để nó gần mã và kiểm trong CI.

**Outcome.** Viết ba loại tài liệu cho dự án của mình, và chứng minh bằng quan sát rằng người khác chạy được và xử lý được sự cố mà không hỏi.

**Đánh giá.** Tầng *đánh giá*. Objective đo bằng người dùng thật, không bằng danh sách mục đã điền. Kiểm bằng quan sát: hai người chưa từng thấy dự án, một người chạy theo tài liệu giới thiệu, một người xử lý sự cố theo sổ tay. Đạt khi cả hai hoàn thành mà không đặt câu hỏi nào, có ghi chép điểm vướng.

**Lab.** Viết ba loại tài liệu. Đưa cho hai học viên khác: một người chạy dự án từ đầu, một người nhận một sự cố cài sẵn và xử lý theo sổ tay. Ghi lại mọi chỗ họ vướng hoặc phải hỏi. Sửa tài liệu theo điểm vướng rồi thử lại với người thứ ba.

**Pitfalls.** Viết bản ghi quyết định mà bỏ phần phương án bị loại · viết sổ tay bằng mô tả thay vì lệnh chạy được · để tài liệu ở nơi khác kho mã nên nó lạc hậu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Hai người chưa từng thấy dự án hoàn thành việc của mình mà không hỏi, có ghi chép điểm vướng.

### Lesson 91 · Gate 3 - clone, one command, same result `KT`
**Prerequisites.** Lesson 90

**In-class (120 phút).** 75 phút làm bài độc lập · 45 phút chữa bài và phân tích lỗi theo nhóm

**Learn.** Không có nội dung mới. Cổng 3 của chương trình, và nó đo thứ khó giả: một kho mã người khác dùng được.

**Outcome.** Giao một kho mã mà người chưa từng thấy sao về, chạy một lệnh dựng môi trường, chạy công việc, và thu được đúng kết quả của mình, với CI xanh và dữ liệu sau hai lần chạy bằng sau một lần.

**Đánh giá.** Tầng *đánh giá*. Cổng đo tính giao được của một sản phẩm, nên người chấm là một học viên khác chứ không phải người viết. Thang điểm: A 25đ một lệnh dựng và chạy được trên máy sạch · B 20đ kết quả khớp đối chứng · C 20đ chạy hai lần bằng chạy một lần · D 20đ CI xanh đủ bốn giai đoạn dưới 10 phút · E 15đ ba loại tài liệu đủ để người chấm không phải hỏi. Đạt khi ≥ 70/100, phần A và phần C đều ≥ 70% của chúng.

**Lab.** Đổi kho mã chéo với một học viên khác. Người nhận chạy trên máy ảo sạch, ghi lại mọi chỗ phải hỏi hoặc phải sửa. Chạy công việc hai lần, đối soát. Mỗi câu hỏi phải đặt ra là một điểm trừ ở phần E.

**Pitfalls.** Giả định người chấm có sẵn công cụ mình đang dùng · để bước cài đặt phải làm tay ở giữa · bộ kiểm thử xanh trên máy mình nhưng đỏ trên máy sạch.

**Self-study (2,4 giờ).** Không có bài tự học. Nếu không đạt, theo phụ lục khắc phục khi không đạt cổng

**Done when.** Đạt ≥ 70/100, phần A và phần C đều ≥ 70%.

# MODULE 9 · SQL FROM ZERO TO ADVANCED

**Lessons 92–107 · 32 giờ**

| | |
|---|---|
| **Objective cấp module** | Viết truy vấn nhiều bảng trên lược đồ chưa từng thấy và chứng minh bằng phép đếm rằng kết quả không mất dòng và không nhân dòng |
| **Tiền đề** | M7 |
| **Exit criterion** | Thư viện 30 truy vấn trên tập đơn hàng ít nhất 1 triệu dòng, mỗi truy vấn có phép kiểm chứng độc lập kèm theo |
| **Kỹ năng SFIA** | `DBAD` mức 3 · `PROG` mức 3 |
| **Chế độ hỏng** | Viết được truy vấn ra số rồi tin luôn, không kiểm chứng, nên số sai đi tiếp xuống hạ nguồn mà không ai biết |

Module dạy SQL như ngôn ngữ sản xuất chứ không như công cụ khám phá. Nguyên tắc xuyên suốt: mọi truy vấn phải có một cách kiểm chứng độc lập, thường là phép đếm trước và sau. Tám bài đầu là nền, bốn bài giữa là kết và cửa sổ, bốn bài cuối là giao dịch, ghi bất biến và nhận diện mẫu sai.

### Lesson 92 · The relational model and relational algebra `LT`
**Prerequisites.** Module 9: M7

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Quan hệ là một tập bộ, và hệ quả của việc nó là tập: không có thứ tự và không có phần tử trùng, trong khi bảng SQL thật thì có cả hai, nên SQL là xấp xỉ của mô hình quan hệ chứ không phải hiện thân của nó. Sáu phép toán đại số quan hệ nền: chọn, chiếu, tích, hợp, hiệu, đổi tên, và cách mọi truy vấn phức tạp phân rã về chúng. Phép kết là tích cộng phép chọn, một cách trình bày giải thích được số dòng kết quả trước khi chạy, nối lại lesson 44. Khoá chính, khoá ngoại, khoá phức hợp, và khoá nghiệp vụ so với khoá thay thế. Bản số quan hệ một một, một nhiều, nhiều nhiều và bảng trung gian. Toàn vẹn thực thể và toàn vẹn tham chiếu như ràng buộc do hệ quản trị giữ chứ không do ứng dụng giữ. Vì sao đại số quan hệ đáng học: bộ tối ưu hoá viết lại truy vấn dựa trên các luật tương đương của nó, nội dung của lesson 112.

**Outcome.** Phân rã một truy vấn SQL cho trước thành chuỗi phép toán đại số quan hệ, và dự đoán số dòng kết quả từ bản số quan hệ.

**Đánh giá.** Tầng *phân tích*. Objective là phân rã và suy luận, không phải viết truy vấn. Kiểm bằng năm truy vấn: phân rã đúng và dự đoán số dòng sai không quá 10% so với kết quả chạy thật cho ít nhất bốn trên năm.

**Lab.** Nhận lược đồ đơn hàng năm bảng có khai báo bản số. Với năm truy vấn cho trước, phân rã thành phép toán đại số và dự đoán số dòng trước khi chạy. Chạy, so sánh, giải thích chênh lệch. Tìm một cặp bảng nhiều nhiều và chỉ bảng trung gian.

**Pitfalls.** Dự đoán số dòng bằng cách nhân số dòng hai bảng · coi bảng SQL là tập nên bỏ qua dòng trùng · giả định khoá ngoại luôn có ràng buộc khai báo.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân rã đúng và dự đoán số dòng sai không quá 10% cho ít nhất bốn trên năm truy vấn.

### Lesson 93 · DDL - tables, types, keys and constraints `TH`
**Prerequisites.** Lesson 92

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Chọn kiểu dữ liệu là quyết định khó đổi về sau và ảnh hưởng cả dung lượng lẫn tính đúng đắn. Ba quy tắc rút từ chặng 1: tiền dùng kiểu thập phân có khai báo độ chính xác chứ không dấu phẩy động, nối lại lesson 7; dấu thời gian luôn kèm múi giờ, nối lại lesson 9; mã định danh có số 0 đầu là chuỗi chứ không phải số, nối lại lesson 69. Chuỗi độ dài cố định so với độ dài thay đổi và chi phí thật của từng loại. Kiểu liệt kê và đánh đổi khi giá trị mới xuất hiện. Năm loại ràng buộc và cái mỗi loại bảo vệ: khoá chính, duy nhất, khoá ngoại, kiểm tra giá trị, không rỗng. Ràng buộc đặt ở cơ sở dữ liệu chứ không ở ứng dụng, vì ứng dụng có nhiều bản còn cơ sở dữ liệu chỉ có một. Hành vi khi xoá bản ghi cha: chặn, xoá lan, hay đặt rỗng, và hệ quả nghiệp vụ của từng cái. Giá trị mặc định và cột sinh tự động.

**Outcome.** Thiết kế và cài đặt lược đồ cho một mô tả nghiệp vụ, và chứng minh ràng buộc chặn được năm loại dữ liệu sai.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí kiểm bằng chạy thật. Đạt khi năm lệnh chèn dữ liệu sai đều bị từ chối bởi đúng ràng buộc tương ứng, và khi ba lựa chọn kiểu dữ liệu nhạy cảm được biện minh bằng bài học ở chặng 1.

**Lab.** Nhận mô tả nghiệp vụ bán hàng. Viết lệnh tạo bảng đủ năm loại ràng buộc. Thử chèn năm bản ghi sai: trùng khoá, khoá ngoại không tồn tại, tiền âm, ngày kết thúc trước ngày bắt đầu, cột bắt buộc rỗng. Xác nhận từng cái bị chặn bởi ràng buộc nào.

**Pitfalls.** Dùng dấu phẩy động cho tiền · để ràng buộc ở tầng ứng dụng cho linh hoạt · dùng xoá lan cho bảng giao dịch rồi mất dữ liệu lịch sử.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Năm lệnh chèn sai đều bị đúng ràng buộc từ chối, và ba lựa chọn kiểu nhạy cảm đều có lý do.

### Lesson 94 · SELECT, WHERE and logical execution order `TH`
**Prerequisites.** Lesson 93

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Sáu mệnh đề và thứ tự thực thi logic, khác hẳn thứ tự viết. Thứ tự này suy ra gần như mọi quy tắc còn lại của SQL, nên học nó một lần thì không phải nhớ các quy tắc rời rạc. Hai hệ quả trực tiếp: bí danh cột dùng được trong mệnh đề sắp xếp nhưng không dùng được trong mệnh đề lọc, và mệnh đề lọc chạy trước phép gộp còn mệnh đề lọc nhóm chạy sau. Toán tử so sánh, khoảng, tập, và khớp mẫu. Khớp mẫu có ký tự đại diện ở đầu không dùng được chỉ mục, nối tới lesson 113. Giới hạn số dòng và phân trang theo độ lệch: vì sao độ lệch lớn chậm dần và cách thay bằng phân trang theo con trỏ, nối lại lesson 35. Lấy giá trị phân biệt và vì sao cần nó thường là dấu hiệu phép kết đang nhân dòng chứ không phải yêu cầu nghiệp vụ. Dự đoán số dòng trả về trước khi chạy như một thói quen bắt buộc.

**Outcome.** Dự đoán số dòng trả về của một truy vấn lọc trước khi chạy, và giải thích sai lệch giữa dự đoán và kết quả bằng thứ tự thực thi logic.

**Đánh giá.** Tầng *áp dụng*. Objective đòi dự đoán trước rồi đối chứng, đây là thói quen module muốn hình thành. Kiểm bằng tám truy vấn; đạt khi dự đoán đúng ít nhất sáu, và khi hai lần sai đều giải thích được bằng thứ tự thực thi chứ không bằng đoán.

**Lab.** Nhận tám truy vấn trên tập 1 triệu dòng. Dự đoán số dòng từng truy vấn trước khi chạy, ghi lại. Chạy, đối chiếu. Với mỗi lần sai, truy về mệnh đề nào gây ra. Thử dùng bí danh trong mệnh đề lọc và quan sát lỗi. Đo thời gian phân trang ở độ lệch 100 và 1 triệu.

**Pitfalls.** Dùng bí danh cột trong mệnh đề lọc · thêm lấy giá trị phân biệt để chữa nhân dòng thay vì sửa phép kết · phân trang bằng độ lệch lớn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Dự đoán đúng ít nhất sáu trên tám, và hai lần sai đều truy được về mệnh đề gây ra.

### Lesson 95 · NULL and three-valued logic `TH`
**Prerequisites.** Lesson 94

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Giá trị rỗng biểu thị sự vắng mặt của giá trị chứ không phải một giá trị, nên mọi phép so sánh với nó cho kết quả không xác định chứ không cho đúng hay sai. Logic ba trạng thái và bảng chân trị của ba phép nối. Hành vi của giá trị rỗng trong số học, so sánh, nối chuỗi, kiểm tra thuộc tập, hàm gộp, gộp nhóm và sắp xếp, mỗi chỗ một quy tắc riêng. Cơ chế khiến mệnh đề lọc khác một giá trị loại luôn các dòng rỗng, lỗi âm thầm vì kết quả vẫn trông hợp lý. Kiểm tra thuộc tập với tập con chứa giá trị rỗng và lý do phép phủ định cho tập rỗng. Các hàm xử lý: thay giá trị rỗng, biến giá trị thành rỗng, và so sánh coi rỗng bằng rỗng. Ba nghĩa nghiệp vụ khác nhau bị gộp chung vào một biểu diễn: chưa nhập, không áp dụng, và bằng không; phân biệt ba nghĩa này là việc thiết kế chứ không phải việc truy vấn.

**Outcome.** Dự đoán đúng giá trị của biểu thức chứa giá trị rỗng, và chọn cách xử lý khớp với nghĩa nghiệp vụ trong ba nghĩa.

**Đánh giá.** Tầng *áp dụng*. Objective gồm dự đoán có đáp án và một quyết định ngữ nghĩa. Đạt khi dự đoán đúng ít nhất 10 trên 12 biểu thức, và khi ba tình huống nghiệp vụ được xử lý đúng theo nghĩa của từng cái, có nêu lý do.

**Lab.** Dự đoán kết quả 12 biểu thức chứa giá trị rỗng trước khi chạy. Chạy đối chiếu. Nhận ba tình huống: cột chiết khấu chưa nhập, cột ngày huỷ không áp dụng, cột số lượng bằng không bị lưu thành rỗng. Xử lý từng cái và nêu lý do.

**Pitfalls.** So sánh với giá trị rỗng bằng dấu bằng · dùng phủ định thuộc tập khi tập con có thể chứa rỗng · thay mọi giá trị rỗng bằng không cho tiện.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Dự đoán đúng ít nhất 10 trên 12 biểu thức, và ba tình huống nghiệp vụ được xử lý đúng theo nghĩa kèm lý do.

### Lesson 96 · Functions, casting and the errors they hide `TH`
**Prerequisites.** Lesson 95

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hàm chuỗi, hàm số, hàm ngày, và điểm chung cần chú ý: hàm bọc quanh cột làm chỉ mục trên cột đó vô hiệu, nối tới lesson 113. Ép kiểu ngầm và bảng ưu tiên kiểu: khi so sánh chuỗi với số, hệ quản trị tự ép một bên, và lựa chọn đó quyết định cả kết quả lẫn khả năng dùng chỉ mục. Ép kiểu tường minh và biến thể có bắt lỗi trả về rỗng thay vì dừng truy vấn. Hàm ngày và cắt về mốc thời gian; trích xuất thành phần ngày. Chênh lệch hai dấu thời gian trả về kiểu khoảng chứ không phải số, và cách chuyển. Múi giờ trong hàm ngày, nối lại lesson 9: cùng một hàm cho hai kết quả khác nhau tuỳ cấu hình phiên. Chia nguyên và chia thực, và lỗi mất phần lẻ khi cả hai vế là số nguyên. Làm tròn và thứ tự làm tròn với phép cộng, nối lại lesson 7. Hàm riêng của từng hệ quản trị và chi phí khi chuyển hệ.

**Outcome.** Chuẩn hoá dữ liệu bẩn ngay trong truy vấn, và chỉ ra ba chỗ ép kiểu ngầm đang làm chỉ mục vô hiệu hoặc làm sai kết quả.

**Đánh giá.** Tầng *phân tích*. Objective gồm một sản phẩm và một phép truy lỗi ẩn. Đạt khi kết quả chuẩn hoá khớp bản đối chứng, và khi định vị đúng cả ba chỗ ép kiểu ngầm, mỗi chỗ dẫn được bằng chứng từ kế hoạch thực thi hoặc từ kết quả sai.

**Lab.** Chuẩn hoá một bảng có cột ngày dạng chuỗi ba định dạng, cột tiền có dấu phân cách, và cột mã có khoảng trắng thừa. Đối chiếu bản đối chứng. Sau đó đọc ba truy vấn có ép kiểu ngầm, định vị và sửa. Đo thời gian trước sau.

**Pitfalls.** Bọc hàm quanh cột trong mệnh đề lọc · chia hai số nguyên rồi mất phần lẻ · làm tròn từng dòng trước khi cộng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Kết quả chuẩn hoá khớp bản đối chứng, và ba chỗ ép kiểu ngầm được định vị có bằng chứng.

### Lesson 97 · CASE and conditional classification `TH`
**Prerequisites.** Lesson 96

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Dạng đơn giản và dạng tìm kiếm của biểu thức điều kiện. Cơ chế dừng ở nhánh khớp đầu tiên và hệ quả: thứ tự nhánh quyết định kết quả, nên hai truy vấn cùng tập nhánh nhưng khác thứ tự cho hai kết quả khác nhau. Thiếu nhánh mặc định sinh ra giá trị rỗng, nối lại lesson 95, và đây là nguồn lỗi âm thầm khi phân nhóm vì bản ghi rơi ra ngoài mọi nhóm. Bốn ứng dụng: phân nhóm nghiệp vụ, sắp xếp tuỳ biến, gộp có điều kiện, và xoay bảng thủ công. Gộp có điều kiện là mẫu quan trọng nhất: nó biến nhiều lần quét thành một lần quét, nối tới lesson 107. Biểu thức điều kiện lồng nhau và ngưỡng mà nó hết đọc được, cùng cách thay bằng bảng ánh xạ. Kiểm chứng bắt buộc sau mọi phép phân nhóm: tổng theo nhóm phải bằng tổng toàn bộ, phép kiểm rẻ và bắt được cả lỗi thiếu nhánh mặc định lẫn lỗi nhánh chồng lấn.

**Outcome.** Phân loại bản ghi thành nhóm nghiệp vụ và chứng minh bằng phép cộng rằng không bản ghi nào rơi ra ngoài hoặc bị đếm hai lần.

**Đánh giá.** Tầng *áp dụng*. Objective có phép kiểm chứng tuyệt đối đi kèm. Đạt khi tổng theo nhóm bằng đúng tổng toàn bộ trên tập 1 triệu dòng, và khi người học phát hiện được lỗi cài sẵn về thứ tự nhánh bằng chính phép kiểm đó.

**Lab.** Phân loại 1 triệu đơn hàng thành sáu nhóm giá trị. Kiểm bằng phép cộng. Nhận một truy vấn phân nhóm cài sẵn hai lỗi: thiếu nhánh mặc định và hai nhánh chồng lấn. Dùng phép kiểm phát hiện cả hai. Viết lại bằng gộp có điều kiện một lần quét và đo thời gian so với nhiều lần quét.

**Pitfalls.** Bỏ nhánh mặc định vì nghĩ đã phủ hết · đặt nhánh rộng trước nhánh hẹp · quét nhiều lần thay vì gộp có điều kiện.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tổng theo nhóm bằng tổng toàn bộ trên 1 triệu dòng, và phát hiện được cả hai lỗi cài sẵn bằng phép kiểm.

### Lesson 98 · GROUP BY as a grain transformation `TH`
**Prerequisites.** Lesson 97

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Gộp nhóm là một phép biến đổi hạt: đầu vào một hạt, đầu ra một hạt khác, và phát biểu được hai hạt đó là cách hiểu đúng mệnh đề này. Từ cách trình bày đó suy ra quy tắc mọi cột trong danh sách chọn phải nằm trong mệnh đề gộp hoặc trong hàm gộp, thay vì phải nhớ nó như một điều luật. Ba biến thể đếm và tập bản ghi mỗi biến thể tính: đếm toàn bộ dòng, đếm giá trị khác rỗng trong một cột, và đếm giá trị phân biệt. Cách hàm gộp bỏ qua giá trị rỗng và hệ quả lên trung bình: trung bình bỏ qua rỗng nhưng tính cả số không, hai thứ khác nhau. Lọc trước gộp so với lọc sau gộp và chi phí khác nhau của hai chỗ. Gộp trên biểu thức. Tập gộp nhiều chiều và gộp cuộn ở mức nhận biết. Phát biểu hạt trước và sau mỗi phép gộp như một thói quen bắt buộc của module.

**Outcome.** Phát biểu hạt trước và sau mỗi phép gộp trong một chuỗi truy vấn, và chọn đúng biến thể đếm theo câu hỏi nghiệp vụ.

**Đánh giá.** Tầng *áp dụng*. Objective gồm một phát biểu kiểm được và một lựa chọn có đáp án. Đạt khi phát biểu hạt đúng cho cả bốn bước của chuỗi, kiểm chứng bằng phép đếm, và khi chọn đúng biến thể đếm cho sáu câu hỏi nghiệp vụ.

**Lab.** Nhận chuỗi bốn phép gộp lồng nhau. Phát biểu hạt trước và sau từng bước bằng một câu, kiểm chứng mỗi phát biểu bằng phép đếm. Trả lời sáu câu hỏi nghiệp vụ, mỗi câu chọn một biến thể đếm và nêu lý do. So kết quả ba biến thể trên cùng cột có giá trị rỗng và trùng.

**Pitfalls.** Dùng đếm toàn bộ dòng khi câu hỏi là đếm khách hàng phân biệt · lọc sau gộp khi lọc trước gộp làm được · quên rằng trung bình bỏ qua rỗng nhưng tính số không.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phát biểu hạt đúng cho cả bốn bước có phép đếm kiểm chứng, và chọn đúng biến thể đếm cho sáu câu hỏi.

### Lesson 99 · JOIN - the mechanism and cardinality `LT`
**Prerequisites.** Lesson 98

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Phép kết trình bày như tích Descartes cộng một điều kiện lọc, nối lại lesson 92, và kết chéo là trường hợp không có điều kiện. Bốn kiểu kết đối chiếu trên một cặp bảng bốn nhân ba tính bằng tay, vì tính tay một lần thì không phải nhớ bảng quy tắc. Bản số quan hệ quyết định số dòng kết quả, và công thức ước lượng cho ba trường hợp một một, một nhiều, nhiều nhiều. Kết bán phần và kết loại trừ diễn đạt bằng kiểm tra tồn tại, và vì sao chúng khác kết thường ở chỗ không nhân dòng. Đọc sơ đồ quan hệ để chọn đường kết. Tự kết cho quan hệ phân cấp. Điều kiện kết đặt ở mệnh đề kết so với ở mệnh đề lọc: với kết trong thì tương đương, với kết ngoài thì không, và đây là một trong những lỗi SQL tốn kém nhất vì nó âm thầm biến kết ngoài thành kết trong. Dự đoán số dòng trước khi chạy.

**Outcome.** Suy ra kiểu kết cần dùng từ một phát biểu nghiệp vụ, và dự đoán số dòng kết quả trước khi chạy từ bản số quan hệ.

**Đánh giá.** Tầng *phân tích*. Objective đòi suy luận từ nghiệp vụ sang cấu trúc và ước lượng định lượng. Đạt khi chọn đúng kiểu kết cho sáu phát biểu và dự đoán số dòng sai không quá 10% cho ít nhất năm trên sáu.

**Lab.** Tính bằng tay bốn kiểu kết trên cặp bảng bốn nhân ba, đối chiếu với kết quả chạy. Nhận sáu phát biểu nghiệp vụ, chọn kiểu kết và dự đoán số dòng. Chạy đối chiếu. Đặt điều kiện bảng phải ở mệnh đề lọc trên một kết ngoài và quan sát nó thành kết trong.

**Pitfalls.** Đặt điều kiện bảng phải vào mệnh đề lọc của kết ngoài · dự đoán số dòng bằng số dòng bảng lớn hơn · dùng kết thường khi chỉ cần kiểm tra tồn tại.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chọn đúng kiểu kết cho sáu phát biểu, và dự đoán số dòng sai không quá 10% cho ít nhất năm.

### Lesson 100 · JOIN - fan-out, multi-table and verification by counting `TH`
**Prerequisites.** Lesson 99

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Nhân bản dòng là chế độ hỏng nguy hiểm nhất của phép kết vì kết quả vẫn trông hợp lý: bảng bên phải có nhiều dòng khớp làm mỗi dòng bên trái nhân lên, nên mọi phép tổng sau đó bị thổi phồng. Ba cách phát hiện: đếm dòng trước và sau mỗi phép kết, kiểm tính duy nhất của khoá kết ở bên phải, và so tổng một cột không nên đổi. Ba cách xử lý: gộp trước khi kết, dùng kết bán phần khi chỉ cần kiểm tồn tại, và sửa khoá kết khi nó không đúng hạt. Kết ba bảng trở lên và thứ tự đọc: mỗi phép kết sinh ra một kết quả trung gian có hạt riêng, nên phải phát biểu hạt sau từng bước như lesson 98. Bản ghi mồ côi và toàn vẹn tham chiếu khi ràng buộc không được khai báo. Quy trình kiểm chứng bắt buộc của module: đếm dòng trước và sau mỗi phép kết, và không truy vấn nào được nộp nếu thiếu phép đếm đó.

**Outcome.** Viết truy vấn kết nhiều bảng và chứng minh bằng phép đếm rằng kết quả không mất dòng và không nhân dòng.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí chứng minh tuyệt đối. Đạt khi truy vấn năm bảng cho kết quả đúng đáp án và khi nộp kèm phép đếm cho từng bước kết. Kết quả đúng mà không có phép đếm thì không đạt, vì module tồn tại để hình thành thói quen đó.

**Lab.** Viết truy vấn kết năm bảng trên tập 1 triệu dòng, trong đó hai bảng có quan hệ nhiều nhiều. Nộp kèm phép đếm sau từng bước. Nhận ba truy vấn cài sẵn nhân dòng, phát hiện và sửa bằng ba cách khác nhau. Tìm bản ghi mồ côi trong một bảng không có ràng buộc khai báo.

**Pitfalls.** Tin kết quả vì nó trông hợp lý · chữa nhân dòng bằng lấy giá trị phân biệt · kết trên cột không phải khoá ở hạt bên phải.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Truy vấn năm bảng đúng đáp án và có phép đếm kèm cho từng bước kết.

### Lesson 101 · Subqueries, CTEs and recursive CTEs `TH`
**Prerequisites.** Lesson 100

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba vị trí đặt truy vấn con và ý nghĩa khác nhau của từng vị trí. Truy vấn con tương quan chạy lại cho mỗi dòng ngoài, nên chi phí nhân lên theo số dòng, và đây là một trong bốn mẫu sai ở lesson 107. Khác biệt ngữ nghĩa giữa kiểm tra tồn tại, kiểm tra thuộc tập, và phép kết khi tập con chứa giá trị rỗng, nối lại lesson 95. Biểu thức bảng chung đặt tên cho một bước và cho phép xâu chuỗi nhiều bước, làm truy vấn đọc được theo trình tự suy nghĩ. Quy ước đặt tên theo hạt của kết quả thay vì theo thao tác, vì tên nói hạt thì người đọc kiểm được ngay. Biểu thức bảng chung không phải bảng tạm: nó có thể được nội tuyến vào truy vấn chính và tính lại nhiều lần, hoặc được vật chất hoá, tuỳ hệ quản trị và tuỳ phiên bản, nên phải đọc kế hoạch thực thi để biết. Biểu thức bảng chung đệ quy cho cây phân cấp và điều kiện dừng.

**Outcome.** Tái cấu trúc một truy vấn lồng nhiều tầng thành chuỗi biểu thức bảng chung đặt tên theo hạt, giữ nguyên kết quả và đạt rà soát chéo về độ đọc được.

**Đánh giá.** Tầng *áp dụng*. Objective gồm một phép tái cấu trúc có tiêu chí kết quả không đổi và một tiêu chí do người khác chấm. Đạt khi kết quả khớp từng dòng với bản gốc và khi một học viên khác đọc bản mới giải thích lại được mục đích từng bước mà không hỏi.

**Lab.** Nhận truy vấn lồng bốn tầng 150 dòng. Tái cấu trúc thành chuỗi biểu thức bảng chung đặt tên theo hạt. Đối chiếu kết quả từng dòng. Đổi bài chéo để người khác giải thích lại. Đọc kế hoạch thực thi xem biểu thức bảng chung được nội tuyến hay vật chất hoá. Viết một truy vấn đệ quy cho cây danh mục.

**Pitfalls.** Đặt tên biểu thức bảng chung theo thao tác thay vì theo hạt · dùng truy vấn con tương quan trên bảng lớn · viết đệ quy không có điều kiện dừng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Kết quả khớp từng dòng với bản gốc, và học viên khác giải thích lại được từng bước mà không hỏi.

### Lesson 102 · Window functions - ranking and positioning `TH`
**Prerequisites.** Lesson 101

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Khác biệt nền tảng với gộp nhóm: gộp nhóm thu gọn số dòng, hàm cửa sổ giữ nguyên số dòng và thêm cột tính trên một nhóm dòng liên quan. Cấu trúc mệnh đề cửa sổ với phân vùng và sắp xếp, và ý nghĩa của từng phần. Bốn hàm xếp hạng và khác biệt chỉ biểu hiện khi có giá trị trùng: đánh số liên tục, xếp hạng có nhảy bậc, xếp hạng không nhảy bậc, và chia phân vị. Chọn hàm nào là quyết định nghiệp vụ về cách xử lý giá trị trùng chứ không phải lựa chọn kỹ thuật. Mẫu lấy N dòng đầu mỗi nhóm, bài toán xuất hiện liên tục trong công việc dữ liệu. Hàm cửa sổ không dùng được trong mệnh đề lọc vì nó chạy sau bước lọc trong thứ tự thực thi logic ở lesson 94, và đường vòng là bọc trong biểu thức bảng chung. Khử trùng bằng đánh số và câu hỏi giữ dòng nào, một quyết định nghiệp vụ phải khai báo rõ.

**Outcome.** Giải bài toán lấy N dòng đầu theo nhóm, và chọn giữa bốn hàm xếp hạng theo yêu cầu nghiệp vụ về xử lý giá trị trùng.

**Đánh giá.** Tầng *áp dụng*. Objective gồm một cài đặt và một lựa chọn có đáp án phụ thuộc yêu cầu. Đạt khi kết quả lấy N dòng đầu khớp đáp án, và khi bốn tình huống trùng giá trị được gán đúng hàm xếp hạng kèm lý do nghiệp vụ.

**Lab.** Lấy 5 đơn hàng lớn nhất mỗi khách trên 1 triệu dòng. Nhận bốn tình huống có giá trị trùng, chọn hàm xếp hạng cho từng cái và nêu lý do. Thử dùng hàm cửa sổ trong mệnh đề lọc, quan sát lỗi, rồi vòng qua bằng biểu thức bảng chung. Khử trùng và khai báo rõ quy tắc giữ dòng.

**Pitfalls.** Dùng đánh số liên tục khi nghiệp vụ cần giữ cả các dòng bằng điểm · đặt hàm cửa sổ trong mệnh đề lọc · khử trùng mà không khai báo giữ dòng nào.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Kết quả lấy N dòng đầu khớp đáp án, và bốn tình huống trùng được gán đúng hàm kèm lý do nghiệp vụ.

### Lesson 103 · Window functions - frames, running totals and period comparison `TH`
**Prerequisites.** Lesson 102

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Mệnh đề khung xác định tập dòng mà hàm tính trên đó, và phần lớn người dùng không biết nó tồn tại vì có khung mặc định. Khung mặc định khi có sắp xếp là từ đầu phân vùng tới dòng hiện tại, nên tổng luỹ kế chạy đúng mà không khai báo gì, nhưng giá trị cuối thì sai vì khung dừng ở dòng hiện tại. Đếm theo dòng so với đếm theo giá trị: hai cách cho kết quả khác nhau khi có giá trị trùng ở cột sắp xếp, và ví dụ định lượng cho khác biệt đó. Hàm lấy dòng trước và dòng sau cho so kỳ trước và cùng kỳ năm trước. Tổng luỹ kế và trung bình trượt. Vấn đề kỳ khuyết: tháng không có giao dịch biến mất khỏi kết quả nên mọi phép so kỳ lệch một bậc, và cách xử lý bằng bảng lịch nối trái. Đây là lỗi hay gặp nhất trong báo cáo theo thời gian và nó không có tín hiệu kỹ thuật nào.

**Outcome.** Dựng báo cáo có tăng trưởng so kỳ, luỹ kế và trung bình trượt, cho kết quả đúng cả ở những kỳ không có giao dịch.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí đúng sai tuyệt đối trên một ca khó. Đạt khi kết quả khớp bản đối chứng ở mọi kỳ, gồm cả ba kỳ khuyết dữ liệu cố ý. Báo cáo đúng ở kỳ có dữ liệu mà lệch ở kỳ khuyết là không đạt.

**Lab.** Dựng báo cáo doanh thu 36 tháng trong đó ba tháng không có giao dịch. Tính tăng trưởng so kỳ trước, so cùng kỳ năm trước, luỹ kế và trung bình trượt ba tháng. Đối chiếu bản đối chứng. So kết quả đếm theo dòng với đếm theo giá trị trên cột có giá trị trùng.

**Pitfalls.** Không nối bảng lịch nên kỳ khuyết biến mất · tin khung mặc định mà không khai báo · dùng đếm theo giá trị khi cần đếm theo dòng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Kết quả khớp bản đối chứng ở mọi kỳ, gồm cả ba kỳ khuyết dữ liệu.

### Lesson 104 · Set operations and data quality queries `TH`
**Prerequisites.** Lesson 103

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phép hợp có khử trùng so với phép hợp giữ nguyên, và chi phí ẩn của việc khử trùng trên tập lớn. Phép giao và phép hiệu dùng để đối chiếu hai nguồn, công cụ chính khi đối soát ở chặng 4. Ba loại trùng lặp và cách phát hiện từng loại: trùng toàn bộ cột, trùng khoá nghiệp vụ, và trùng mờ do khác biểu diễn chuỗi, nối lại lesson 8 về chuẩn hoá Unicode. Sáu chiều chất lượng dữ liệu và một truy vấn đo cho từng chiều: đầy đủ, duy nhất, hợp lệ, nhất quán, chính xác, kịp thời. Chiều chính xác là chiều duy nhất không đo được bằng quy tắc nội bộ, nó cần một nguồn đối chứng độc lập, và đây là điều phải nói rõ thay vì giả vờ đo được. Bản ghi mồ côi và toàn vẹn tham chiếu khi không có ràng buộc khai báo. Bộ truy vấn kiểm chất lượng viết một lần dùng lại được cho bảng bất kỳ.

**Outcome.** Lập báo cáo chất lượng định lượng trên sáu chiều cho một bảng chưa từng thấy, và nói rõ chiều nào không đo được bằng quy tắc nội bộ.

**Đánh giá.** Tầng *phân tích*. Objective gồm đo và một phán đoán về giới hạn của phép đo. Đạt khi sáu chiều đều có số, khi định vị đúng loại lỗi cài sẵn trong bảng, và khi nêu rõ chiều chính xác cần nguồn đối chứng. Báo cáo đủ sáu số mà không nêu giới hạn thì thiếu phần quan trọng nhất.

**Lab.** Nhận bảng 2 triệu dòng cài sẵn bốn loại lỗi. Viết bộ truy vấn đo sáu chiều. Chạy và lập báo cáo có số. Định vị bốn loại lỗi. Dùng phép hiệu đối chiếu với một bảng nguồn độc lập cho chiều chính xác. Đóng gói bộ truy vấn thành dùng lại được cho bảng khác.

**Pitfalls.** Báo cáo chiều chính xác bằng quy tắc nội bộ · dùng phép hợp có khử trùng khi không cần khử · bỏ qua trùng mờ vì trùng khoá đã bằng không.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Sáu chiều đều có số, bốn loại lỗi cài sẵn được định vị, và giới hạn của chiều chính xác được nêu rõ.

### Lesson 105 · Transactions, isolation levels and the three read phenomena `TH`
**Prerequisites.** Lesson 104

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Giao dịch là đơn vị nguyên tử: hoặc mọi thay đổi có hiệu lực hoặc không thay đổi nào có hiệu lực. Bốn đảm bảo và ví dụ phản chứng cho từng cái bằng một giao dịch chuyển tiền bị ngắt giữa chừng. Ba hiện tượng đọc và điều kiện xuất hiện: đọc bẩn khi đọc được thay đổi chưa xác nhận, đọc không lặp lại khi cùng truy vấn cho hai kết quả trong một giao dịch, và đọc ảo khi tập dòng thoả điều kiện thay đổi. Bốn mức cô lập và hiện tượng nào bị chặn ở mức nào; mức mặc định khác nhau giữa các hệ quản trị và đây là chỗ giả định sai gây lỗi khi chuyển hệ. Cô lập cao hơn không miễn phí: nó đổi bằng tranh chấp khoá và tỉ lệ giao dịch bị huỷ, nối lại lesson 52. Giao dịch dài giữ khoá lâu và chặn người khác, một nguyên nhân phổ biến của hệ thống trông như treo. Chế độ tự xác nhận và vì sao nó làm ghi theo lô mất ý nghĩa, nối lại lesson 72.

**Outcome.** Tái hiện ba hiện tượng đọc bằng hai phiên chạy song song, và chỉ ra mức cô lập nào chặn được hiện tượng nào.

**Đánh giá.** Tầng *phân tích*. Objective đòi dựng được điều kiện xuất hiện chứ không chỉ nhớ bảng. Đạt khi tái hiện được cả ba hiện tượng bằng hai phiên, và khi bảng đối chiếu bốn mức cô lập nhân ba hiện tượng được điền đúng bằng thực nghiệm chứ không bằng tài liệu.

**Lab.** Mở hai phiên song song. Dựng kịch bản cho từng hiện tượng ở mức cô lập thấp nhất. Nâng dần mức và ghi lại hiện tượng nào biến mất. Điền bảng bốn nhân ba bằng kết quả quan sát. Đo tỉ lệ giao dịch bị huỷ ở mức cao nhất dưới tải song song.

**Pitfalls.** Tin mức cô lập mặc định giống nhau giữa các hệ · đặt mức cao nhất cho an toàn mà không đo tỉ lệ huỷ · giữ giao dịch mở trong lúc gọi mạng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tái hiện được cả ba hiện tượng, và bảng bốn nhân ba được điền bằng kết quả thực nghiệm.

### Lesson 106 · Upsert, merge and idempotent writes `TH`
**Prerequisites.** Lesson 105

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ghi bất biến khi chạy lại là yêu cầu của mọi pipeline, nối lại lesson 74 của chặng 1, và ở tầng SQL nó có ba cách cài đặt. Chèn có xử lý xung đột: chèn nếu chưa có, cập nhật hoặc bỏ qua nếu đã có, và điều kiện bắt buộc là phải có ràng buộc duy nhất trên khoá, nếu không thì hệ quản trị không biết thế nào là xung đột. Trộn theo khoá cho cả chèn, cập nhật và xoá trong một câu lệnh, cùng cạm bẫy khi nguồn có dòng trùng khoá: một số hệ báo lỗi, một số chọn tuỳ ý, nên phải khử trùng nguồn trước. Xoá theo khoảng rồi chèn lại cho phân vùng, và điều kiện nguyên tử: hai câu lệnh trong một giao dịch, nếu không thì có cửa sổ bảng rỗng. Chọn cách nào theo ba yếu tố: có khoá duy nhất không, tỉ lệ dòng thay đổi, và có cần xử lý xoá không. Kiểm chứng bắt buộc: chạy hai lần và so từng dòng.

**Outcome.** Cài ghi bất biến bằng ba cách, và chứng minh bằng đối chiếu từng dòng rằng chạy hai lần cho kết quả bằng chạy một lần.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí đối chứng tuyệt đối và ba cài đặt để so. Đạt khi cả ba cách đều qua phép chạy hai lần, và khi người học chọn được cách phù hợp cho ba tình huống có ràng buộc khác nhau kèm lý do.

**Lab.** Cài ba cách ghi bất biến cho bảng đích 5 triệu dòng. Chạy mỗi cách hai lần, đối chiếu từng dòng. Cố ý đưa nguồn có dòng trùng khoá vào phép trộn và quan sát hành vi. Bỏ giao dịch quanh xoá rồi chèn và quan sát cửa sổ bảng rỗng. Chọn cách cho ba tình huống.

**Pitfalls.** Dùng chèn có xử lý xung đột khi chưa có ràng buộc duy nhất · trộn từ nguồn chưa khử trùng · xoá rồi chèn ngoài giao dịch.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Cả ba cách qua phép chạy hai lần đối chiếu từng dòng, và ba tình huống được chọn cách phù hợp kèm lý do.

### Lesson 107 · Query anti-patterns and how to recognise them `TH`
**Prerequisites.** Lesson 106

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Sáu mẫu sai phổ biến, mỗi mẫu kèm triệu chứng, cơ chế, và cách sửa. Truy vấn một cộng n: lấy danh sách rồi lặp gọi truy vấn cho từng phần tử, thường phát sinh từ mã ứng dụng chứ không từ SQL, và cách phát hiện là đếm số truy vấn trong một lần chạy. Chọn mọi cột khi chỉ cần vài cột: tốn băng thông, chặn chỉ mục chỉ phủ, và làm mã vỡ khi lược đồ thêm cột. Thiếu bộ lọc hoặc bộ lọc không dùng được chỉ mục do bọc hàm quanh cột, nối lại lesson 96. Phân trang theo độ lệch lớn, nối lại lesson 94. Phép kết nổ bản số do khoá kết sai hạt, nối lại lesson 100. Truy vấn con tương quan trên bảng lớn, nối lại lesson 101. Quy trình nhận diện: đọc mã trước, rồi đo, rồi đọc kế hoạch thực thi ở lesson 113. Nguyên tắc không tối ưu khi chưa đo, nối lại lesson 17 và 40.

**Outcome.** Nhận diện sáu mẫu sai trong một kho mã cho trước và sửa chúng, chứng minh cải thiện bằng số đo trước và sau.

**Đánh giá.** Tầng *phân tích*. Objective là truy lỗi hiệu năng về đúng mẫu rồi sửa có đối chứng. Đạt khi tìm được ít nhất năm trên sáu mẫu cài sẵn, và khi mỗi bản sửa có số đo trước sau cho thấy cải thiện. Sửa mà không đo thì không tính, kể cả khi sửa đúng.

**Lab.** Nhận một kho mã cài sẵn sáu mẫu, trong đó mẫu một cộng n nằm ở tầng ứng dụng. Đếm số truy vấn mỗi lần chạy để phát hiện nó. Sửa từng mẫu, đo trước sau. Lập bảng sáu dòng: mẫu, triệu chứng, cách phát hiện, cách sửa, cải thiện đo được.

**Pitfalls.** Sửa theo cảm nhận mà không đo · thêm chỉ mục cho mọi cột trong mệnh đề lọc · chọn mọi cột rồi lọc cột ở tầng ứng dụng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tìm ít nhất năm trên sáu mẫu, và mỗi bản sửa có số đo trước sau cho thấy cải thiện.

# MODULE 10 · THE LIFE OF A QUERY - DATABASE INTERNALS

**Lessons 108–121 · 28 giờ**

| | |
|---|---|
| **Objective cấp module** | Truy một truy vấn chậm hoặc một sự cố cơ sở dữ liệu về đúng chặng trong vòng đời truy vấn, bằng kế hoạch thực thi và số đo chứ bằng phỏng đoán |
| **Tiền đề** | M9 · M2 |
| **Exit criterion** | Chẩn đoán sáu ca dựng sẵn về đúng chặng, và diễn tập một lần khôi phục từ bản sao lưu có đo thời điểm phục hồi và thời lượng phục hồi |
| **Kỹ năng SFIA** | `DBAD` mức 4 · `SYSP` mức 3 |
| **Chế độ hỏng** | Tối ưu bằng cách sửa cú pháp truy vấn hoặc thêm chỉ mục theo cảm tính, vì chưa bao giờ đọc kế hoạch thực thi |

Module lấy một sơ đồ làm trục và mười bốn bài đi dọc nó:

```text
Ứng dụng khách → xác thực và nhóm kết nối → phân tích cú pháp → kiểm tra và gắn tham số
→ viết lại → bộ tối ưu hoá (thống kê, ước lượng bản số, chi phí) → kế hoạch vật lý
→ bộ thực thi (quét, lọc, kết, gộp, sắp) → bộ đệm ↔ đĩa
→ trả kết quả qua mạng → xác nhận hoặc hoàn tác → nhật ký ghi trước và điểm kiểm tra
→ bản sao và sao lưu
```

Mọi khẳng định về hiệu năng trong module phải kèm kế hoạch thực thi và số đo, không kèm lập luận về cú pháp.

### Lesson 108 · The life of a query - twelve stages end to end `LT`
**Prerequisites.** Module 10: M9 · M2

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Đi dọc sơ đồ một lần, mỗi chặng nêu việc nó làm và chế độ hỏng đặc trưng của nó. Chặng kết nối: hết kết nối, nối lại lesson 36. Phân tích cú pháp: lỗi cú pháp, và chi phí phân tích lại khi truy vấn không tham số hoá nên mỗi lần là một chuỗi khác. Gắn tham số: truy vấn chuẩn bị sẵn dùng lại kế hoạch, và trường hợp kế hoạch dùng lại không còn tối ưu khi tham số đổi phân bố. Viết lại: bộ tối ưu hoá biến đổi truy vấn theo luật tương đương của đại số quan hệ ở lesson 92, nên truy vấn viết cách nào thường không quan trọng bằng dữ liệu trông thế nào. Bộ tối ưu hoá chọn kế hoạch theo chi phí ước lượng, và mọi sai lầm của nó bắt nguồn từ ước lượng bản số sai. Bộ thực thi và các toán tử vật lý. Bộ đệm và đĩa. Trả kết quả và chi phí mạng. Xác nhận, nhật ký ghi trước, điểm kiểm tra, bản sao. Phân biệt kế hoạch logic với kế hoạch vật lý.

**Outcome.** Định vị một sự cố cơ sở dữ liệu về đúng chặng trong mười hai chặng, và nêu phép đo xác nhận cho chặng đó.

**Đánh giá.** Tầng *phân tích*. Objective là phân loại có bằng chứng, đặt nền cho mười ba bài sau. Kiểm bằng sáu mô tả sự cố; đạt khi định vị đúng ít nhất năm và mỗi lần nêu được một phép đo xác nhận thực hiện được, không chấp nhận phép đo chung chung như xem nhật ký.

**Lab.** Vẽ lại sơ đồ mười hai chặng từ trí nhớ. Nhận sáu mô tả sự cố: hết kết nối, truy vấn chậm dần theo thời gian, một truy vấn chậm hẳn sau khi nạp dữ liệu mới, kết quả trả về chậm dù truy vấn nhanh, ghi chậm sau khi thêm chỉ mục, và cơ sở dữ liệu đứng sau khi mất điện. Định vị từng cái và nêu phép đo.

**Pitfalls.** Kết luận truy vấn chậm mà chưa loại trừ chặng mạng và chặng kết nối · quy mọi thứ về thiếu chỉ mục · dùng xem nhật ký làm phép đo.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Định vị đúng ít nhất năm trên sáu sự cố, mỗi lần kèm một phép đo xác nhận thực hiện được.

### Lesson 109 · Pages, tuples and how a row is stored `LT`
**Prerequisites.** Lesson 108

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Trang là đơn vị đọc ghi của cơ sở dữ liệu, thường vài ki lô byte, và mọi thao tác quy về đọc ghi trang chứ không quy về đọc ghi dòng. Cấu trúc một trang: phần đầu, mảng con trỏ dòng, vùng trống, và dữ liệu dòng mọc ngược từ cuối. Hệ quả: cập nhật một dòng nhỏ vẫn phải ghi cả trang, nối lại khuếch đại ghi ở lesson 16. Bố trí một dòng: phần đầu dòng, bản đồ giá trị rỗng, rồi các cột theo thứ tự lưu. Thứ tự cột ảnh hưởng dung lượng do căn lề, nên sắp cột theo độ rộng giảm dần tiết kiệm được vài phần trăm trên bảng lớn. Giá trị quá lớn không vừa trang được lưu ngoài dòng, và chi phí đọc thêm khi truy cập chúng. Hệ số lấp đầy trang và chỗ trống để lại cho cập nhật tại chỗ. Bảng phình do dòng chết chưa được thu hồi, chuẩn bị cho lesson 118. Lưu theo dòng so với lưu theo cột, nối lại lesson 41 và 70.

**Outcome.** Ước lượng số trang một bảng chiếm từ lược đồ và số dòng, rồi đo thật và giải thích chênh lệch.

**Đánh giá.** Tầng *áp dụng*. Objective gồm ước lượng và đối chứng bằng số đo hệ thống. Đạt khi ước lượng sai trong phạm vi 30% so với số trang thật, và khi người học chỉ ra được nguồn gốc của phần chênh, thường là căn lề và phần đầu trang.

**Lab.** Tạo ba bảng 5 triệu dòng cùng dữ liệu nhưng khác thứ tự cột. Ước lượng số trang từ lược đồ. Đo số trang thật bằng khung nhìn hệ thống. So ba bảng và giải thích chênh lệch bằng căn lề. Cập nhật 10% số dòng và đo lại kích thước.

**Pitfalls.** Ước lượng dung lượng bằng tổng độ rộng cột nhân số dòng · giả định cập nhật một cột chỉ ghi một cột · bỏ qua giá trị lưu ngoài dòng khi tính.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ước lượng sai trong phạm vi 30% so với số trang thật, và nguồn gốc phần chênh được chỉ ra.

### Lesson 110 · The buffer pool and the two-tier cache problem `TH`
**Prerequisites.** Lesson 109

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bộ đệm giữ trang vừa dùng trong bộ nhớ, và tỉ lệ trúng là chỉ số quan trọng nhất của nó. Chính sách thay thế và vì sao một lần quét toàn bảng lớn có thể đẩy mọi trang nóng ra ngoài, hiện tượng gọi là làm ô nhiễm bộ đệm, cùng cách các hệ quản trị chống lại nó. Trang bẩn và thời điểm ghi xuống đĩa, chuẩn bị cho điểm kiểm tra ở lesson 118. Hai tầng đệm chồng nhau: bộ đệm của cơ sở dữ liệu và bộ đệm trang của hệ điều hành ở lesson 22, nên cùng một trang có thể nằm hai nơi và tốn gấp đôi bộ nhớ. Hệ quả cấu hình: đặt bộ đệm bằng toàn bộ RAM là sai, phải chừa cho hệ điều hành và cho bộ nhớ làm việc của truy vấn. Bộ nhớ làm việc cho phép sắp và phép kết, và điều gì xảy ra khi không đủ: tràn ra đĩa, đây chính là vế thứ nhất của tiêu chí ra M2. Đọc tỉ lệ trúng và số trang đọc từ đĩa trên hệ thống đang chạy.

**Outcome.** Đo tỉ lệ trúng bộ đệm trước và sau một lần quét toàn bảng lớn, và chỉ ra ngưỡng bộ nhớ làm việc mà phép sắp bắt đầu tràn ra đĩa.

**Đánh giá.** Tầng *phân tích*. Objective đòi nối số đo với cơ chế và tìm một ngưỡng. Đạt khi có số đo tỉ lệ trúng ở ba thời điểm cho thấy hiện tượng ô nhiễm, và khi ngưỡng tràn đĩa được xác định bằng thực nghiệm ở ít nhất bốn giá trị bộ nhớ làm việc.

**Lab.** Làm nóng bộ đệm bằng tải truy vấn thường. Đo tỉ lệ trúng. Quét toàn bảng lớn hơn bộ đệm. Đo lại ngay sau và sau khi chạy tải thường 10 phút. Chạy một phép sắp ở bốn giá trị bộ nhớ làm việc, tìm ngưỡng tràn đĩa bằng kế hoạch thực thi.

**Pitfalls.** Đặt bộ đệm bằng toàn bộ RAM · đọc tỉ lệ trúng ngay sau khi khởi động rồi kết luận · bỏ qua bộ nhớ làm việc khi tính dung lượng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Số đo tỉ lệ trúng ở ba thời điểm cho thấy ô nhiễm bộ đệm, và ngưỡng tràn đĩa xác định được ở bốn giá trị.

### Lesson 111 · Index structures - B-tree, LSM and inverted `LT`
**Prerequisites.** Lesson 110

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Cây B cộng và ba tính chất làm nó thành chỉ mục mặc định: chiều cao thấp nên ít lần chạm đĩa, lá nối nhau nên quét khoảng rẻ, và cân bằng tự động, nối lại lesson 46. Chỉ mục phủ và quét chỉ mục thuần khi mọi cột cần đều nằm trong chỉ mục. Chỉ mục phức hợp và quy tắc tiền tố trái: thứ tự cột quyết định truy vấn nào dùng được, nên một chỉ mục ba cột không thay thế được ba chỉ mục một cột. Chọn lọc của cột và vì sao chỉ mục trên cột ít giá trị phân biệt thường vô dụng. Cây trộn có cấu trúc nhật ký: ghi vào bộ nhớ rồi xả ra đĩa theo tầng, tối ưu cho ghi nhiều, đổi khuếch đại ghi thấp lấy khuếch đại đọc cao, nối tới ClickHouse ở M16. Chỉ mục ngược cho tìm kiếm toàn văn, nối tới Elasticsearch ở M17. Chi phí ghi của chỉ mục: mỗi chỉ mục thêm một cây phải cập nhật, đây là vế thứ hai của tiêu chí ra M2.

**Outcome.** Chọn cấu trúc chỉ mục và thứ tự cột cho năm mẫu truy vấn, và dự đoán truy vấn nào dùng được chỉ mục nào trước khi chạy.

**Đánh giá.** Tầng *đánh giá*. Objective đòi thiết kế chỉ mục có đánh đổi đọc ghi, không có đáp án chung. Đạt khi dự đoán đúng ít nhất bốn trên năm truy vấn về việc chỉ mục có được dùng không, xác nhận bằng kế hoạch thực thi, và khi chi phí ghi được đo trước sau khi thêm chỉ mục.

**Lab.** Tạo bảng 10 triệu dòng. Thiết kế chỉ mục cho năm mẫu truy vấn. Dự đoán truy vấn nào dùng chỉ mục nào, rồi đọc kế hoạch thực thi để xác nhận. Đo thời gian chèn 1 triệu dòng khi có 0, 2, 5 chỉ mục. Thử một chỉ mục trên cột giới tính và quan sát nó không được dùng.

**Pitfalls.** Tạo chỉ mục cho mọi cột trong mệnh đề lọc · đảo thứ tự cột trong chỉ mục phức hợp · thêm chỉ mục mà không đo chi phí ghi.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Dự đoán đúng ít nhất bốn trên năm truy vấn xác nhận bằng kế hoạch, và có số đo chi phí ghi theo số chỉ mục.

### Lesson 112 · Statistics, cardinality estimation and why plans go wrong `TH`
**Prerequisites.** Lesson 111

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bộ tối ưu hoá chọn kế hoạch theo chi phí ước lượng, và chi phí ước lượng dựa trên ước lượng số dòng, nên mọi kế hoạch tồi đều truy về một ước lượng bản số sai. Thống kê gồm gì: số dòng, số giá trị phân biệt, biểu đồ phân bố, tỉ lệ giá trị rỗng, và các giá trị xuất hiện nhiều nhất. Thu thập thống kê tự động và điều kiện kích hoạt, cùng lý do thống kê lạc hậu sau một lần nạp lớn. Bốn nguyên nhân ước lượng sai: thống kê cũ, dữ liệu lệch mà biểu đồ không đủ chi tiết, tương quan giữa hai cột mà bộ tối ưu hoá giả định độc lập, và hàm bọc quanh cột làm mất thống kê. Nguyên nhân thứ ba là nguyên nhân khó nhất: lọc theo tỉnh và theo quận là hai điều kiện tương quan, nhân hai chọn lọc ra con số nhỏ hơn thực tế nhiều lần. So ước lượng với số dòng thật trong kế hoạch là cách chẩn đoán trực tiếp nhất.

**Outcome.** So ước lượng số dòng với số dòng thật trong kế hoạch thực thi, và truy sai lệch lớn về đúng một trong bốn nguyên nhân.

**Đánh giá.** Tầng *phân tích*. Objective là chẩn đoán phân biệt bốn nguyên nhân có cùng triệu chứng. Kiểm bằng bốn ca dựng sẵn; đạt khi truy đúng ít nhất ba, mỗi lần dẫn được con số ước lượng và con số thật từ kế hoạch.

**Lab.** Dựng bốn ca: nạp 5 triệu dòng rồi chạy ngay khi thống kê chưa cập nhật, bảng có một giá trị chiếm 80%, hai cột tương quan chặt, và mệnh đề lọc bọc hàm quanh cột. Với mỗi ca, đọc kế hoạch, so ước lượng với thật, truy nguyên. Cập nhật thống kê và đo lại.

**Pitfalls.** Ép bộ tối ưu hoá dùng kế hoạch mình muốn thay vì sửa thống kê · đọc chi phí ước lượng mà không đọc số dòng · cập nhật thống kê rồi không đo lại.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Truy đúng ít nhất ba trên bốn nguyên nhân, mỗi lần dẫn được ước lượng và số thật từ kế hoạch.

### Lesson 113 · Reading an execution plan - logical against physical `TH`
**Prerequisites.** Lesson 112

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Kế hoạch logic nói làm gì, kế hoạch vật lý nói làm thế nào, và chỉ cái sau mới nói được truy vấn sẽ chạy bao lâu. Đọc kế hoạch từ trong ra ngoài và từ dưới lên. Bốn nhóm toán tử và ý nghĩa vận hành: truy cập dữ liệu gồm quét toàn bảng, quét chỉ mục, tra chỉ mục rồi lấy dòng; kết; gộp; và sắp. Quét toàn bảng không phải luôn xấu: khi lấy phần lớn bảng thì nó rẻ hơn tra chỉ mục từng dòng, và ngưỡng đó tính được. Chế độ phân tích thật so với chế độ chỉ ước lượng: cái đầu chạy truy vấn nên cho số dòng thật và thời gian thật, cái sau không chạy nên chỉ có ước lượng. Bốn con số phải đọc trong mỗi nút: số dòng ước lượng, số dòng thật, số lần lặp, và thời gian. Số lần lặp nhân thời gian là chi phí thật của nút, và bỏ qua nó là lỗi đọc kế hoạch phổ biến nhất. Bộ đệm chia sẻ đọc được và đọc từ đĩa. Chỗ tràn ra đĩa hiện trong kế hoạch.

**Outcome.** Đọc một kế hoạch thực thi và chỉ ra nút tốn nhất cùng lý do, phân biệt được nút chậm với nút chạy nhiều lần.

**Đánh giá.** Tầng *phân tích*. Objective đòi định vị chi phí thật, và bẫy chính là nhầm thời gian một lần với tổng chi phí. Kiểm bằng bốn kế hoạch, trong đó hai kế hoạch có nút tốn nhất là nút chạy nhiều lần chứ không phải nút chậm nhất. Đạt khi chỉ đúng cả bốn.

**Lab.** Chạy bốn truy vấn ở chế độ phân tích thật. Với mỗi kế hoạch, lập bảng bốn con số cho từng nút, tính chi phí thật, chỉ nút tốn nhất. Hai kế hoạch có nút chạy 10.000 lần mỗi lần 0,1 mili giây. Xác định ngưỡng mà quét toàn bảng rẻ hơn tra chỉ mục.

**Pitfalls.** Đọc kế hoạch ước lượng rồi kết luận về thời gian thật · chọn nút có thời gian một lần lớn nhất làm nút tốn nhất · coi quét toàn bảng luôn là lỗi.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chỉ đúng nút tốn nhất ở cả bốn kế hoạch, gồm hai ca nút tốn nhất là nút chạy nhiều lần.

### Lesson 114 · Join execution - which algorithm the planner picks and why `TH`
**Prerequisites.** Lesson 113

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba thuật toán kết ở lesson 44 xuất hiện trong kế hoạch dưới tên toán tử vật lý, và bài này nối lý thuyết đó với thực tế. Điều kiện bộ tối ưu hoá chọn từng cái: vòng lặp lồng khi bảng ngoài nhỏ và bảng trong có chỉ mục, kết băm khi không có chỉ mục phù hợp và bảng dựng vừa bộ nhớ làm việc, kết trộn sắp khi cả hai bên đã sắp theo khoá kết. Thứ tự kết khi có nhiều bảng: số cách sắp xếp tăng theo giai thừa nên bộ tối ưu hoá cắt tỉa không gian tìm kiếm, và với truy vấn nhiều bảng nó có thể bỏ lỡ kế hoạch tốt nhất. Kết băm tràn ra đĩa khi bảng dựng lớn hơn bộ nhớ làm việc, nối lại lesson 110: đây là câu trả lời đầy đủ cho vế thứ nhất của tiêu chí ra M2. Lệch khoá kết làm một nhóm băm nhận phần lớn dòng, nối lại lesson 48. Kết lồng nhau trên bảng lớn là triệu chứng của ước lượng bản số sai chứ không phải lựa chọn của bộ tối ưu hoá.

**Outcome.** Giải thích vì sao bộ tối ưu hoá chọn một thuật toán kết cụ thể trong một kế hoạch, và làm nó đổi lựa chọn bằng cách đổi một điều kiện.

**Đánh giá.** Tầng *phân tích*. Objective đòi hiểu quy luật chọn đủ để tác động vào nó có chủ đích. Đạt khi giải thích đúng lựa chọn ở ba kế hoạch, và khi làm bộ tối ưu hoá đổi sang thuật toán khác bằng cách đổi đúng một điều kiện, ba lần với ba điều kiện khác nhau.

**Lab.** Dựng ba truy vấn kết cho ra ba thuật toán khác nhau. Giải thích từng lựa chọn. Với mỗi cái, đổi đúng một điều kiện để bộ tối ưu hoá chọn thuật toán khác: thêm chỉ mục, đổi bộ nhớ làm việc, và sắp sẵn dữ liệu. Ép kết băm tràn ra đĩa và quan sát trong kế hoạch.

**Pitfalls.** Ép thuật toán kết bằng gợi ý thay vì sửa nguyên nhân · tăng bộ nhớ làm việc toàn cục để chữa một truy vấn · bỏ qua lệch khoá khi kết băm chậm bất thường.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Giải thích đúng lựa chọn ở ba kế hoạch, và ba lần làm bộ tối ưu hoá đổi thuật toán bằng một điều kiện.

### Lesson 115 · Partition pruning and predicate pushdown `TH`
**Prerequisites.** Lesson 114

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phân vùng chia một bảng logic thành nhiều bảng vật lý theo một khoá, và lợi ích chính không phải tốc độ đọc mà là cắt tỉa: bộ tối ưu hoá bỏ qua cả phân vùng không thoả điều kiện, nên chi phí tỉ lệ với dữ liệu cần chứ không với dữ liệu có. Ba kiểu phân vùng và mẫu truy cập hợp với từng kiểu, nối lại lesson 48. Điều kiện cắt tỉa hoạt động: mệnh đề lọc phải nằm trên chính khoá phân vùng và không bị bọc hàm, nối lại lesson 96, nên phân vùng theo ngày mà lọc theo hàm trích tháng thì cắt tỉa vô hiệu. Đẩy vị từ xuống: đưa điều kiện lọc xuống càng sớm càng tốt trong cây kế hoạch để giảm dòng đi lên trên. Hai chỗ nó không đẩy được: qua hàm cửa sổ và qua một số dạng truy vấn con. Xoá phân vùng cũ bằng thao tác siêu dữ liệu thay vì xoá dòng, nhanh hơn nhiều bậc. Quá nhiều phân vùng làm lập kế hoạch chậm, nên có giới hạn trên hợp lý.

**Outcome.** Chứng minh cắt tỉa phân vùng có hiệu lực bằng số phân vùng được quét, và tìm một truy vấn làm cắt tỉa vô hiệu rồi sửa.

**Đánh giá.** Tầng *phân tích*. Objective đòi chứng minh bằng số đo trong kế hoạch chứ không bằng thời gian. Đạt khi chỉ ra được số phân vùng quét trong kế hoạch cho ba truy vấn, và khi định vị đúng nguyên nhân cắt tỉa vô hiệu rồi sửa cho nó hoạt động trở lại.

**Lab.** Tạo bảng phân vùng theo ngày 36 phân vùng, 50 triệu dòng. Chạy ba truy vấn và đọc số phân vùng quét trong kế hoạch. Viết một truy vấn bọc hàm quanh khoá phân vùng, quan sát quét hết, rồi sửa. Xoá một phân vùng bằng thao tác siêu dữ liệu và so thời gian với xoá dòng.

**Pitfalls.** Đánh giá cắt tỉa bằng thời gian chạy thay vì bằng số phân vùng quét · bọc hàm quanh khoá phân vùng · tạo phân vùng theo ngày cho bảng giữ 10 năm mà không gộp.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Số phân vùng quét đọc được từ kế hoạch cho ba truy vấn, và ca cắt tỉa vô hiệu được định vị và sửa.

### Lesson 116 · MVCC, locking and what isolation costs `LT`
**Prerequisites.** Lesson 115

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Điều khiển đồng thời nhiều phiên bản cho người đọc thấy một ảnh chụp nhất quán mà không chặn người ghi, và ngược lại. Cơ chế: mỗi dòng có nhiều phiên bản kèm dấu giao dịch, và mỗi giao dịch thấy phiên bản hợp lệ với ảnh chụp của nó. Hệ quả vận hành quan trọng nhất: cập nhật không sửa tại chỗ mà tạo phiên bản mới, nên bảng phình và cần thu hồi dòng chết, nối lại lesson 109. Giao dịch mở lâu chặn việc thu hồi mọi dòng chết sinh ra sau khi nó bắt đầu, nên một phiên quên đóng làm cả cơ sở dữ liệu phình. Khoá ở ba mức: hàng, trang, bảng; và leo thang khoá khi số khoá hàng vượt ngưỡng. Khoá chia sẻ và khoá độc quyền, ma trận tương thích. Chờ khoá và hàng đợi chờ. Bốn mức cô lập ở lesson 105 cài đặt bằng gì: mức thấp dùng ảnh chụp, mức cao dùng khoá hoặc phát hiện xung đột rồi huỷ. Cô lập cao đổi bằng tỉ lệ huỷ chứ không bằng thời gian chờ.

**Outcome.** Giải thích vì sao một giao dịch mở lâu làm cơ sở dữ liệu phình, và chỉ ra giao dịch đó bằng khung nhìn hệ thống.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết nối cơ chế với một triệu chứng vận hành cụ thể. Đạt khi giải thích đúng chuỗi nhân quả từ giao dịch mở tới phình bảng, và khi định vị được giao dịch cũ nhất đang mở cùng thời lượng của nó trên một hệ thống có tải.

**Lab.** Mở một giao dịch và để đó. Chạy tải cập nhật 30 phút. Đo kích thước bảng và số dòng chết theo thời gian. Định vị giao dịch cũ nhất bằng khung nhìn hệ thống. Đóng nó, chạy thu hồi, đo lại. Quan sát leo thang khoá khi cập nhật số dòng lớn trong một giao dịch.

**Pitfalls.** Để phiên mở trong công cụ khách rồi đi ăn trưa · tăng ngưỡng leo thang khoá để chữa tranh chấp · kết luận phình bảng do dữ liệu tăng mà không xem dòng chết.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Giải thích đúng chuỗi nhân quả, và định vị được giao dịch cũ nhất đang mở cùng thời lượng.

### Lesson 117 · Deadlocks - detection, victims and prevention `TH`
**Prerequisites.** Lesson 116

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bế tắc trong cơ sở dữ liệu là trường hợp cụ thể của bế tắc ở lesson 53, với bốn điều kiện giống hệt. Khác biệt: hệ quản trị có bộ phát hiện chạy định kỳ, tìm vòng chờ trong đồ thị chờ khoá, rồi chọn một giao dịch làm nạn nhân và huỷ nó. Tiêu chí chọn nạn nhân khác nhau giữa các hệ, thường là giao dịch làm ít việc nhất. Hệ quả cho ứng dụng: giao dịch bị huỷ là chuyện bình thường phải xử lý bằng thử lại, không phải lỗi hệ thống, nên mã ghi phải có vòng thử lại; nhưng thử lại chỉ đúng khi giao dịch bất biến, nối lại lesson 106. Ba nguyên nhân bế tắc phổ biến trong công việc dữ liệu: cập nhật nhiều dòng theo thứ tự khác nhau ở hai tiến trình, nâng cấp khoá chia sẻ thành độc quyền, và khoá khoảng khi chèn. Phòng ngừa: quy định thứ tự cập nhật toàn cục, giữ giao dịch ngắn, và gom cập nhật thành một câu lệnh. Đọc nhật ký bế tắc để biết hai giao dịch đang chờ khoá nào.

**Outcome.** Gây bế tắc cơ sở dữ liệu có chủ đích, đọc nhật ký bế tắc để xác định hai khoá gây vòng chờ, và phòng ngừa bằng thứ tự cập nhật.

**Đánh giá.** Tầng *phân tích*. Objective gồm chẩn đoán từ nhật ký và một bản sửa có nguyên tắc. Đạt khi xác định đúng hai khoá gây vòng chờ từ nhật ký, và khi bản sửa chạy 10.000 giao dịch song song không sinh bế tắc nào. Sửa bằng cách chỉ thêm thử lại thì chỉ đạt một nửa.

**Lab.** Dựng hai tiến trình cập nhật hai bảng theo thứ tự ngược nhau. Chạy tới khi có bế tắc. Bật nhật ký bế tắc, đọc, xác định hai khoá. Sửa bằng thứ tự cập nhật toàn cục, chạy 10.000 giao dịch song song. Thêm vòng thử lại cho phần còn lại và xác nhận nó bất biến.

**Pitfalls.** Coi giao dịch bị huỷ là lỗi hệ thống · chỉ thêm thử lại mà không phá vòng chờ · thử lại một giao dịch không bất biến.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Xác định đúng hai khoá gây vòng chờ từ nhật ký, và bản sửa chạy 10.000 giao dịch song song không bế tắc.

### Lesson 118 · Write-ahead log, checkpoints and crash recovery `TH`
**Prerequisites.** Lesson 117

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Nguyên tắc ghi trước: mọi thay đổi ghi vào nhật ký và đồng bộ xuống đĩa trước khi trang dữ liệu được ghi, nên sau sự cố có đủ thông tin để dựng lại. Đây là cách cơ sở dữ liệu đạt được tính bền vững mà không phải đồng bộ mọi trang dữ liệu ở mỗi lần xác nhận, nối lại lesson 16. Nội dung một bản ghi nhật ký và số thứ tự. Điểm kiểm tra: ghi mọi trang bẩn xuống đĩa và đánh dấu một mốc, để phục hồi chỉ phải chạy lại từ mốc đó thay vì từ đầu. Đánh đổi: điểm kiểm tra thưa thì phục hồi lâu, dày thì tốn vào ra lúc chạy bình thường, và đây là tham số phải chọn theo thời lượng phục hồi mục tiêu. Ba pha phục hồi sau sự cố: phân tích, chạy lại, hoàn tác. Nhật ký cũng là nguồn cho bản sao ở lesson 120 và cho bắt thay đổi dữ liệu ở chặng 6. Nhật ký đầy đĩa làm cơ sở dữ liệu dừng ghi, một sự cố vận hành phổ biến.

**Outcome.** Đo thời gian phục hồi sau sự cố ở ba cấu hình điểm kiểm tra, và giải thích đánh đổi bằng số đo vào ra lúc chạy bình thường.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn một tham số có đánh đổi hai chiều và biện minh bằng số. Đạt khi có bảng ba cấu hình kèm cả thời gian phục hồi lẫn vào ra lúc chạy bình thường, và khi lựa chọn cuối dẫn được về một thời lượng phục hồi mục tiêu cho trước.

**Lab.** Chạy tải ghi liên tục. Với ba khoảng điểm kiểm tra khác nhau, đo vào ra lúc chạy bình thường, rồi ngắt điện máy ảo và đo thời gian phục hồi. Lập bảng. Chọn cấu hình cho thời lượng phục hồi mục tiêu 2 phút. Làm đầy phân vùng nhật ký và quan sát hệ thống dừng ghi.

**Pitfalls.** Đặt điểm kiểm tra thưa để giảm vào ra mà không đo thời gian phục hồi · để nhật ký chung phân vùng với dữ liệu · tin rằng xác nhận thành công nghĩa là trang dữ liệu đã xuống đĩa.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng ba cấu hình có cả thời gian phục hồi lẫn vào ra, và lựa chọn cuối dẫn được về thời lượng mục tiêu.

### Lesson 119 · Backup, point-in-time restore and measuring RPO and RTO `TH`
**Prerequisites.** Lesson 118

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hai đại lượng quyết định thiết kế sao lưu và chúng thường bị nhầm: điểm phục hồi là lượng dữ liệu chấp nhận mất tính bằng thời gian, thời lượng phục hồi là thời gian chấp nhận hệ thống ngừng. Hai con số này do nghiệp vụ quyết định chứ không do kỹ thuật, và mọi lựa chọn kỹ thuật suy ra từ chúng. Sao lưu logic so với sao lưu vật lý: cái đầu di chuyển được giữa phiên bản, cái sau nhanh hơn nhiều trên dữ liệu lớn. Sao lưu toàn phần, vi sai và tăng dần. Phục hồi tới một thời điểm bằng bản sao lưu nền cộng nhật ký ghi trước từ lesson 118, và đây là lý do phải giữ nhật ký chứ không chỉ giữ bản sao lưu. Nguyên tắc duy nhất về sao lưu: một bản sao lưu chưa phục hồi thử không phải là bản sao lưu. Diễn tập phục hồi định kỳ và đo thời gian thật. Ba lỗi làm bản sao lưu vô dụng: cùng đĩa với dữ liệu, không mã hoá, và không ai biết mật khẩu giải mã.

**Outcome.** Phục hồi cơ sở dữ liệu tới một thời điểm cụ thể trong quá khứ, và đo điểm phục hồi cùng thời lượng phục hồi đạt được thật.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí kiểm bằng diễn tập thật, không bằng lập luận. Đạt khi phục hồi tới đúng thời điểm chỉ định và dữ liệu khớp ảnh chụp đối chứng tại thời điểm đó, và khi nộp hai con số đo được chứ không phải hai con số cam kết.

**Lab.** Chạy tải ghi và chụp ảnh đối chứng ở ba mốc thời gian. Lấy sao lưu nền, giữ nhật ký. Xoá cơ sở dữ liệu. Phục hồi tới mốc thứ hai. So từng dòng với ảnh chụp mốc đó. Đo thời gian từ lúc bắt đầu tới lúc phục vụ được. Lặp lại một lần nữa và so hai lần đo.

**Pitfalls.** Lấy sao lưu mà không bao giờ phục hồi thử · để bản sao lưu cùng đĩa với dữ liệu · báo cáo điểm phục hồi cam kết thay vì đo được.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Dữ liệu sau phục hồi khớp ảnh chụp đối chứng tại mốc chỉ định, và hai con số là số đo được từ diễn tập.

### Lesson 120 · Replication, replica lag and read-after-write `TH`
**Prerequisites.** Lesson 119

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bản sao vật lý truyền nhật ký ghi trước từ lesson 118, bản sao logic truyền thay đổi ở mức dòng; cái đầu giống hệt bản chính, cái sau chọn được bảng và chuyển được giữa phiên bản, và nó chính là nền của bắt thay đổi dữ liệu ở chặng 6. Đồng bộ so với bất đồng bộ: đồng bộ không mất dữ liệu khi bản chính chết nhưng mỗi lần xác nhận phải chờ bản sao, bất đồng bộ nhanh nhưng có cửa sổ mất dữ liệu bằng đúng độ trễ. Độ trễ bản sao: nguyên nhân, cách đo, và vì sao nó tăng vọt khi có giao dịch ghi lớn. Đọc sau ghi: ứng dụng ghi vào bản chính rồi đọc ngay từ bản sao có thể không thấy dữ liệu vừa ghi, một lỗi khó tái hiện vì nó phụ thuộc thời điểm. Ba cách xử lý và đánh đổi. Chuyển đổi dự phòng thủ công và tự động, cùng rủi ro hai bản cùng nhận ghi. Tách tải đọc sang bản sao và điều kiện an toàn.

**Outcome.** Đo độ trễ bản sao dưới ba mức tải và tái hiện được lỗi đọc sau ghi, rồi sửa bằng một trong ba cách.

**Đánh giá.** Tầng *phân tích*. Objective gồm đo và tái hiện một lỗi phụ thuộc thời điểm, việc khó hơn đọc tài liệu. Đạt khi tái hiện được lỗi đọc sau ghi ít nhất 5 lần trong 100 lần thử, và khi bản sửa cho 0 lần trong 1.000 lần thử.

**Lab.** Dựng bản chính và một bản sao bất đồng bộ. Đo độ trễ ở ba mức tải ghi. Chạy một giao dịch ghi lớn và quan sát độ trễ tăng vọt. Viết kịch bản ghi rồi đọc ngay từ bản sao, chạy 100 lần, đếm số lần không thấy dữ liệu. Sửa và chạy 1.000 lần.

**Pitfalls.** Tách tải đọc sang bản sao mà không xét đọc sau ghi · dùng bản sao bất đồng bộ khi nghiệp vụ không chấp nhận mất dữ liệu · đo độ trễ lúc không có tải.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tái hiện lỗi đọc sau ghi ít nhất 5 lần trong 100 thử, và bản sửa cho 0 lần trong 1.000 thử.

### Lesson 121 · Schema migrations without downtime `TH`
**Prerequisites.** Lesson 120

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Thay đổi lược đồ trên bảng lớn đang phục vụ là thao tác rủi ro nhất trong vận hành cơ sở dữ liệu, vì một số thao tác giữ khoá bảng và chặn mọi truy cập. Phân loại thao tác theo mức khoá: thao tác chỉ đổi siêu dữ liệu chạy tức thì, thao tác phải viết lại bảng mất thời gian tỉ lệ kích thước, và thao tác giữ khoá độc quyền chặn cả đọc. Cùng một lệnh có thể rơi vào nhóm khác nhau tuỳ phiên bản, nên phải kiểm trên bản sao trước. Tạo chỉ mục không chặn ghi và chi phí kèm theo. Mẫu mở rộng rồi thu hẹp cho thay đổi phá vỡ: thêm cột mới, ghi cả hai, chuyển dữ liệu nền, chuyển đọc, rồi mới bỏ cột cũ; bốn bước này triển khai riêng và mỗi bước quay lui được. Thời gian chờ khoá cho lệnh đổi lược đồ để nó thất bại thay vì chặn cả hệ thống. Quay lui một di trú đã chạy: mã quay lui được còn dữ liệu thì không, nối lại lesson 89.

**Outcome.** Thực hiện một thay đổi lược đồ phá vỡ trên bảng 50 triệu dòng đang có tải, không gây ngừng phục vụ, theo mẫu mở rộng rồi thu hẹp.

**Đánh giá.** Tầng *sáng tạo*. Objective là thiết kế một quy trình nhiều bước dưới ràng buộc không ngừng phục vụ, không phải chạy một lệnh. Đạt khi tải đọc ghi chạy suốt quá trình không có lỗi nào và độ trễ phân vị 95 không vượt hai lần mức nền, và khi mỗi trong bốn bước quay lui được độc lập.

**Lab.** Bảng 50 triệu dòng có tải đọc ghi liên tục. Đổi kiểu một cột từ số nguyên sang chuỗi theo mẫu bốn bước. Đo lỗi và độ trễ phân vị 95 suốt quá trình. Thử quay lui ở từng bước. Trước đó, chạy lệnh đổi kiểu trực tiếp trên bản sao và đo thời gian khoá.

**Pitfalls.** Chạy lệnh đổi lược đồ trực tiếp trên bảng lớn giờ cao điểm · bỏ thời gian chờ khoá nên lệnh chặn cả hệ thống · bỏ cột cũ ở cùng lần triển khai với chuyển đọc.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tải chạy suốt không lỗi và độ trễ phân vị 95 không vượt hai lần mức nền, và cả bốn bước đều quay lui được.

# MODULE 11 · POSTGRESQL IN DEPTH

**Lessons 122–135 · 28 giờ**

| | |
|---|---|
| **Objective cấp module** | Vận hành một cụm PostgreSQL ở mức sản xuất: chẩn đoán kế hoạch lệch, xử lý phình bảng, chỉnh thu hồi tự động, phục hồi tới một thời điểm, và di trú lược đồ không ngừng phục vụ |
| **Tiền đề** | M10 |
| **Exit criterion** | Sáu diễn tập đều đạt: kế hoạch lệch ước lượng, phình bảng, giao dịch dài, sao lưu và phục hồi tới thời điểm, độ trễ bản sao, và di trú không ngừng phục vụ |
| **Kỹ năng SFIA** | `DBAD` mức 4 · `SYSP` mức 4 |
| **Chế độ hỏng** | Chỉnh tham số theo bài hướng dẫn trên mạng mà không đo, nên cấu hình trông hợp lý nhưng không khớp tải thật |

PostgreSQL là hệ duy nhất trong bảy hệ được học ở mức `A`, tức xây và vận hành được. M10 đã dạy cơ chế chung; module này đi vào cái PostgreSQL làm khác và cái chỉ lộ ra khi vận hành thật. Mọi tham số chỉnh trong module phải kèm số đo trước và sau trên tải của chính người học.

### Lesson 122 · Installing, configuring and the parameters that matter `TH`
**Prerequisites.** Module 11: M10

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Cài đặt và bố trí thư mục: dữ liệu, nhật ký ghi trước, và nhật ký hệ thống nên nằm trên phân vùng riêng, lý do ở lesson 118. Tệp cấu hình chính và tệp xác thực kết nối, cùng thứ tự áp dụng. Phân loại tham số theo cách nạp lại: một số áp dụng ngay, một số cần nạp lại cấu hình, một số cần khởi động lại, và biết loại nào là điều kiện để chỉnh an toàn trên hệ đang chạy. Mười tham số ảnh hưởng nhiều nhất và cái mỗi tham số đánh đổi: bộ đệm chia sẻ, bộ nhớ làm việc, bộ nhớ bảo trì, kích thước nhật ký tối đa, khoảng điểm kiểm tra, chi phí trang ngẫu nhiên, số kết nối tối đa, số công nhân song song, tham số thu hồi tự động, và mức ghi nhật ký. Quy tắc của module: không chép giá trị từ bài hướng dẫn, mỗi tham số phải có số đo trước và sau trên tải của mình. Khung nhìn cấu hình để biết giá trị hiện hành đến từ tệp nào.

**Outcome.** Chỉnh năm tham số cho một tải cho trước và chứng minh cải thiện bằng số đo trước và sau, nêu rõ tham số nào cần khởi động lại.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn giá trị có đánh đổi và biện minh bằng số, không có cấu hình đúng chung. Đạt khi năm tham số đều có số đo trước sau trên cùng tải, khi phân loại đúng tham số nào cần khởi động lại, và khi ít nhất một tham số được giữ nguyên vì số đo cho thấy đổi không có lợi.

**Lab.** Dựng cụm PostgreSQL với ba phân vùng riêng. Chạy tải chuẩn và ghi số nền. Chỉnh năm tham số từng cái một, đo lại sau mỗi lần. Lập bảng. Thử chỉnh một tham số cần khởi động lại bằng lệnh nạp lại và quan sát nó không có hiệu lực. Đọc khung nhìn cấu hình xem giá trị đến từ đâu.

**Pitfalls.** Chép cấu hình từ bài hướng dẫn · đổi nhiều tham số cùng lúc rồi không biết cái nào có tác dụng · đặt bộ đệm chia sẻ bằng phần lớn RAM, nối lại lesson 110.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Năm tham số đều có số đo trước sau, phân loại đúng loại nạp lại, và ít nhất một tham số được giữ nguyên có lý do.

### Lesson 123 · Heap, page, tuple and the visibility map `LT`
**Prerequisites.** Lesson 122

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bảng lưu dưới dạng đống không sắp thứ tự, nên thứ tự dòng trả về không có bảo đảm nếu không có mệnh đề sắp xếp. Cấu trúc trang tám ki lô byte theo mô hình ở lesson 109. Định danh dòng vật lý gồm số trang và số vị trí, và vì sao nó đổi khi dòng được cập nhật. Cập nhật tại chỗ chỉ xảy ra khi trang còn chỗ và cột được cập nhật không có chỉ mục, cơ chế tối ưu giảm được việc cập nhật chỉ mục; khi không thoả thì dòng mới sang trang khác và mọi chỉ mục phải cập nhật. Bản đồ khả kiến đánh dấu trang mà mọi dòng đều thấy được bởi mọi giao dịch, và nó cho phép quét chỉ mục thuần bỏ qua bước lấy dòng từ đống, nên nó là điều kiện để chỉ mục phủ có tác dụng. Bản đồ không gian trống. Cột quá lớn lưu ngoài dòng có nén, và chi phí giải nén khi đọc. Hệ số lấp đầy và khi nào nên hạ nó xuống.

**Outcome.** Giải thích vì sao quét chỉ mục thuần có lúc nhanh có lúc không, bằng trạng thái bản đồ khả kiến của bảng.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết nhưng objective nối cơ chế với một hiện tượng đo được. Đạt khi giải thích đúng chuỗi nhân quả và khi thực nghiệm cho thấy cùng một truy vấn đổi từ quét chỉ mục thuần sang quét có lấy dòng sau khi cập nhật dữ liệu.

**Lab.** Tạo bảng 5 triệu dòng có chỉ mục phủ. Chạy thu hồi để cập nhật bản đồ khả kiến. Chạy truy vấn và xác nhận quét chỉ mục thuần trong kế hoạch. Cập nhật 20% số dòng. Chạy lại truy vấn, quan sát số lần lấy dòng từ đống tăng. Chạy thu hồi rồi đo lại.

**Pitfalls.** Giả định thứ tự dòng ổn định khi không có mệnh đề sắp xếp · tin chỉ mục phủ luôn cho quét thuần · bỏ qua ảnh hưởng của cập nhật lên bản đồ khả kiến.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Thực nghiệm cho thấy truy vấn đổi chế độ quét sau khi cập nhật, và chuỗi nhân quả được giải thích đúng.

### Lesson 124 · MVCC in PostgreSQL - xmin, xmax and tuple visibility `TH`
**Prerequisites.** Lesson 123

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** PostgreSQL cài điều khiển đồng thời nhiều phiên bản bằng cách giữ phiên bản cũ ngay trong bảng chứ không đưa sang vùng riêng như một số hệ khác, và lựa chọn thiết kế này giải thích gần như mọi đặc thù vận hành của nó. Hai cột hệ thống ghi giao dịch tạo và giao dịch xoá của mỗi phiên bản dòng. Quy tắc khả kiến: một giao dịch thấy phiên bản nào dựa trên ảnh chụp của nó và trạng thái hai giao dịch đó. Đọc trực tiếp hai cột hệ thống để quan sát cơ chế thay vì chỉ đọc mô tả. Hệ quả thứ nhất: cập nhật là chèn phiên bản mới cộng đánh dấu phiên bản cũ, nên bảng lớn lên dù số dòng logic không đổi, dẫn thẳng tới lesson 125. Hệ quả thứ hai: đếm số dòng phải quét vì không có bộ đếm sẵn, khác với một số hệ khác. Hệ quả thứ ba: giao dịch chỉ đọc cũng giữ ảnh chụp và chặn thu hồi, nối lại lesson 116.

**Outcome.** Quan sát trực tiếp cơ chế nhiều phiên bản bằng hai cột hệ thống, và dự đoán phiên bản nào một giao dịch nhìn thấy trước khi chạy.

**Đánh giá.** Tầng *phân tích*. Objective đòi suy luận về khả kiến chứ không chỉ mô tả cơ chế. Kiểm bằng sáu tình huống hai phiên; đạt khi dự đoán đúng ít nhất năm và mỗi lần dẫn được giá trị hai cột hệ thống làm bằng chứng.

**Lab.** Mở hai phiên. Chèn, cập nhật, xoá một dòng ở phiên một và đọc hai cột hệ thống sau mỗi thao tác. Ở phiên hai, dự đoán thấy phiên bản nào trước khi truy vấn, rồi truy vấn đối chiếu. Lặp cho sáu tình huống ở hai mức cô lập. Đếm số phiên bản vật lý của một dòng sau 10 lần cập nhật.

**Pitfalls.** Tin rằng cập nhật sửa dòng tại chỗ · dùng đếm số dòng làm phép kiểm nhanh trên bảng lớn · cho rằng giao dịch chỉ đọc không ảnh hưởng gì.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Dự đoán đúng ít nhất năm trên sáu tình huống, mỗi lần dẫn được giá trị hai cột hệ thống.

### Lesson 125 · Bloat, VACUUM and autovacuum tuning `TH`
**Prerequisites.** Lesson 124

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phình là dung lượng chiếm bởi phiên bản dòng chết chưa được thu hồi, và nó là hệ quả trực tiếp của thiết kế ở lesson 124 chứ không phải lỗi. Đo phình: so kích thước bảng với kích thước ước lượng từ số dòng và lược đồ, nối lại lesson 109. Thu hồi thường đánh dấu không gian dùng lại được nhưng không trả về hệ điều hành; thu hồi toàn phần trả về được nhưng giữ khoá độc quyền nên không dùng được trên bảng đang phục vụ. Thu hồi tự động và ba tham số quyết định nó chạy khi nào: ngưỡng theo số dòng, tỉ lệ theo kích thước bảng, và số tiến trình song song. Vì sao cấu hình mặc định quá thưa cho bảng lớn: ngưỡng theo tỉ lệ nghĩa là bảng một tỉ dòng phải có 200 triệu dòng chết mới chạy. Chỉnh theo từng bảng thay vì toàn cục. Giới hạn chi phí thu hồi và cơ chế nó tự dừng để không ảnh hưởng tải, cùng hệ quả là nó không đuổi kịp trên bảng ghi nhiều.

**Outcome.** Đo phình của một bảng, chỉnh thu hồi tự động cho riêng bảng đó, và chứng minh phình được giữ dưới ngưỡng dưới tải ghi liên tục.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn tham số cho một bảng cụ thể và chứng minh bằng theo dõi theo thời gian. Đạt khi tỉ lệ phình được giữ dưới 20% qua 60 phút tải ghi liên tục, và khi người học nêu được vì sao cấu hình toàn cục mặc định không đủ cho bảng này bằng phép tính ngưỡng.

**Lab.** Tạo bảng 20 triệu dòng, chạy tải cập nhật liên tục. Đo phình mỗi 5 phút trong 60 phút với cấu hình mặc định. Tính ngưỡng kích hoạt mặc định cho bảng này. Chỉnh tham số riêng cho bảng, chạy lại 60 phút, vẽ hai đường cong. Thử thu hồi toàn phần và đo thời gian khoá.

**Pitfalls.** Chạy thu hồi toàn phần trên bảng đang phục vụ · chỉnh ngưỡng toàn cục để chữa một bảng · tin rằng thu hồi trả dung lượng về hệ điều hành.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tỉ lệ phình dưới 20% qua 60 phút tải ghi, và phép tính ngưỡng cho thấy vì sao mặc định không đủ.

### Lesson 126 · Transaction ID wraparound and why it can stop the database `LT`
**Prerequisites.** Lesson 125

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Định danh giao dịch là số nguyên 32 bit nên nó quay vòng, và đây là nơi lesson 6 về tràn số gặp lại ở quy mô hệ thống. Cơ chế: khả kiến so sánh định danh theo thứ tự vòng, nên một giao dịch quá cũ sẽ trông như ở tương lai và dữ liệu cũ biến mất. Để ngăn điều đó, PostgreSQL đóng băng phiên bản dòng đủ cũ, và việc đóng băng do thu hồi thực hiện. Hệ quả: thu hồi không phải tuỳ chọn hiệu năng mà là yêu cầu để cơ sở dữ liệu sống. Ba mức cảnh báo khi tuổi giao dịch tăng dần và hành vi ở mức cuối: hệ thống từ chối mọi lệnh ghi để tự bảo vệ, một sự cố dừng hoàn toàn. Ba nguyên nhân thường gặp đẩy tuổi lên: giao dịch mở rất lâu, khe bản sao bỏ quên, và bảng bị loại khỏi thu hồi tự động. Theo dõi tuổi giao dịch như một chỉ số vận hành bắt buộc. Phiên bản mới hơn có định danh 64 bit ở một số nhánh, nhưng phải kiểm phiên bản đang chạy chứ không giả định.

**Outcome.** Giải thích chuỗi nhân quả từ một giao dịch mở lâu tới việc cơ sở dữ liệu từ chối ghi, và nêu ba chỉ số cần theo dõi để chặn trước.

**Đánh giá.** Tầng *hiểu*. Objective là giải thích cơ chế và rút ra chỉ số theo dõi; gây ra sự cố thật tốn hàng giờ nên không đặt trong lab. Đạt khi chuỗi nhân quả nêu đủ bốn mắt xích, và khi ba chỉ số nêu ra đều truy vấn được trên cụm đang chạy với ngưỡng cảnh báo cụ thể.

**Lab.** Đọc tuổi giao dịch của mọi cơ sở dữ liệu và bảng trên cụm. Mở một giao dịch và để 30 phút, quan sát tuổi không giảm được cho các bảng. Tạo một khe bản sao rồi bỏ quên, quan sát tác động. Viết ba truy vấn theo dõi kèm ngưỡng cảnh báo. Kiểm phiên bản đang chạy dùng định danh mấy bit.

**Pitfalls.** Giả định phiên bản đang chạy đã dùng định danh 64 bit · tắt thu hồi tự động cho bảng lớn để tiết kiệm vào ra · tạo khe bản sao cho công cụ thử nghiệm rồi quên xoá.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chuỗi nhân quả nêu đủ bốn mắt xích, và ba truy vấn theo dõi chạy được kèm ngưỡng cảnh báo cụ thể.

### Lesson 127 · Index types - B-tree, GIN, GiST, BRIN and when each wins `TH`
**Prerequisites.** Lesson 126

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bốn họ chỉ mục và bài toán mỗi họ giải. Cây B cho so sánh và khoảng, mặc định và phủ phần lớn nhu cầu, nối lại lesson 111. Chỉ mục đảo tổng quát cho giá trị chứa nhiều phần tử: mảng, tài liệu JSON, và tìm kiếm toàn văn; chi phí ghi cao hơn nhiều và có cơ chế hoãn cập nhật để giảm. Chỉ mục tìm kiếm tổng quát cho dữ liệu không xếp thứ tự tuyến tính được như hình học và khoảng thời gian. Chỉ mục phạm vi khối lưu giá trị nhỏ nhất và lớn nhất theo nhóm trang, nên nó rất nhỏ nhưng chỉ hiệu quả khi dữ liệu vật lý tương quan với cột chỉ mục, điều kiện thường đúng với bảng chỉ chèn theo thời gian. Chỉ mục một phần cho truy vấn luôn kèm một điều kiện cố định. Chỉ mục trên biểu thức khi truy vấn bọc hàm quanh cột, nối lại lesson 96. Tạo chỉ mục không chặn ghi và điều kiện nó thất bại giữa chừng để lại chỉ mục không hợp lệ.

**Outcome.** Chọn họ chỉ mục cho năm mẫu truy vấn, và chứng minh lựa chọn bằng kích thước chỉ mục, thời gian truy vấn và chi phí ghi.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn có đánh đổi ba chiều, không có đáp án chung. Đạt khi năm lựa chọn đều có ba số đo, và khi ít nhất một lựa chọn đi ngược trực giác được giải thích bằng số, ví dụ chỉ mục phạm vi khối thắng cây B trên bảng theo thời gian.

**Lab.** Tạo bảng 50 triệu dòng có cột thời gian tăng dần, cột JSON, và cột văn bản. Tạo bốn họ chỉ mục cho năm mẫu truy vấn. Đo kích thước chỉ mục, thời gian truy vấn, và thời gian chèn 1 triệu dòng. So chỉ mục phạm vi khối với cây B trên cột thời gian. Tạo chỉ mục không chặn ghi trong lúc có tải.

**Pitfalls.** Dùng cây B cho mọi thứ · tạo chỉ mục phạm vi khối trên cột không tương quan với thứ tự vật lý · tạo chỉ mục nặng trên bảng ghi nhiều mà không đo chi phí ghi.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Năm lựa chọn đều có ba số đo, và ít nhất một lựa chọn đi ngược trực giác được giải thích bằng số.

### Lesson 128 · The planner - cost parameters, statistics targets and extended statistics `TH`
**Prerequisites.** Lesson 127

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bộ lập kế hoạch tính chi phí bằng một mô hình có tham số, và bốn tham số chi phí quyết định phần lớn lựa chọn: chi phí trang tuần tự, chi phí trang ngẫu nhiên, chi phí xử lý một dòng, và chi phí xử lý một toán tử. Tỉ lệ giữa chi phí trang ngẫu nhiên và tuần tự mặc định phản ánh đĩa từ, nên trên ổ thể rắn nó làm bộ lập kế hoạch tránh chỉ mục quá mức, nối lại lesson 15. Đây là một trong ít tham số mà đổi mặc định thường đúng, nhưng vẫn phải đo. Mục tiêu thống kê điều khiển độ chi tiết của biểu đồ phân bố, và tăng nó cho cột lệch giúp ước lượng bản số chính xác hơn, nối lại lesson 112. Thống kê mở rộng khai báo tương quan giữa nhiều cột, giải đúng nguyên nhân thứ ba trong bốn nguyên nhân ước lượng sai. Vô hiệu hoá một loại toán tử để kiểm giả thuyết trong lúc chẩn đoán, và vì sao không được để lại trong sản xuất.

**Outcome.** Sửa một kế hoạch tồi bằng cách chỉnh đúng nguyên nhân trong ba nguyên nhân, và chứng minh ước lượng bản số cải thiện chứ không chỉ thời gian.

**Đánh giá.** Tầng *phân tích*. Objective đòi sửa nguyên nhân chứ không sửa triệu chứng, và bẫy chính là ép kế hoạch bằng cách vô hiệu hoá toán tử. Đạt khi ba ca đều được sửa bằng đúng cơ chế, và khi số dòng ước lượng tiến gần số dòng thật, đọc từ kế hoạch trước và sau.

**Lab.** Dựng ba ca kế hoạch tồi: tỉ lệ chi phí trang không hợp ổ thể rắn, cột lệch có biểu đồ quá thô, và hai cột tương quan. Sửa từng ca bằng chỉnh tham số chi phí, tăng mục tiêu thống kê, và khai báo thống kê mở rộng. So ước lượng với số thật trước sau. Thử vô hiệu hoá toán tử để kiểm giả thuyết rồi bật lại.

**Pitfalls.** Để vô hiệu hoá toán tử trong cấu hình sản xuất · chỉnh tham số chi phí mà không đo trên ổ thật · tăng mục tiêu thống kê toàn cục thay vì cho cột cần.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba ca sửa đúng cơ chế, và số dòng ước lượng tiến gần số thật đọc được từ kế hoạch trước sau.

### Lesson 129 · EXPLAIN in PostgreSQL - buffers, timing and JIT `TH`
**Prerequisites.** Lesson 128

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Các tuỳ chọn của lệnh giải thích kế hoạch và cái mỗi tuỳ chọn thêm vào. Chế độ phân tích thật chạy truy vấn nên phải bọc trong giao dịch có hoàn tác khi truy vấn ghi, nếu không sẽ ghi thật. Tuỳ chọn bộ đệm cho biết số trang đọc từ bộ đệm chia sẻ và số trang đọc từ đĩa, và đây là số đo hữu ích nhất mà phần lớn người dùng không bật. Tỉ lệ giữa hai con số đó là tỉ lệ trúng của chính truy vấn, cụ thể hơn tỉ lệ trúng toàn cục ở lesson 110. Đọc số lần lặp và nhân với thời gian mỗi lần, nối lại lesson 113. Dấu hiệu tràn ra đĩa hiện trong kế hoạch kèm dung lượng, cho biết cần tăng bộ nhớ làm việc bao nhiêu. Công nhân song song và vì sao thời gian tổng không bằng tổng thời gian các nhánh. Biên dịch tức thời bật ở ngưỡng chi phí và có thể làm truy vấn ngắn chậm hơn vì chi phí biên dịch, một hiện tượng gây bối rối khi mới gặp.

**Outcome.** Đọc một kế hoạch có đủ bộ đệm và thời gian, và rút ra ba kết luận hành động được: cần chỉ mục nào, cần bộ nhớ làm việc bao nhiêu, và tỉ lệ trúng của truy vấn.

**Đánh giá.** Tầng *phân tích*. Objective đòi chuyển số đo thành hành động cụ thể có định lượng. Đạt khi ba kết luận đều kèm con số, và khi dự đoán cải thiện sau khi áp dụng sai không quá hệ số hai so với số đo thật.

**Lab.** Chạy năm truy vấn với đầy đủ tuỳ chọn. Với mỗi cái, lập bảng: trang từ bộ đệm, trang từ đĩa, tỉ lệ trúng, có tràn đĩa không và bao nhiêu, số lần lặp nút tốn nhất. Rút ba kết luận kèm số, áp dụng, đo lại. Chạy một truy vấn ngắn ở ngưỡng bật biên dịch tức thời và quan sát.

**Pitfalls.** Chạy chế độ phân tích thật trên truy vấn ghi ngoài giao dịch · đọc kế hoạch mà không bật tuỳ chọn bộ đệm · cộng thời gian các nhánh song song.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba kết luận đều kèm con số, và dự đoán cải thiện sai không quá hệ số hai so với số đo thật.

### Lesson 130 · Partitioning - declarative partitions, pruning and maintenance `TH`
**Prerequisites.** Lesson 129

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phân vùng khai báo và ba kiểu: theo khoảng, theo danh sách, theo băm, nối lại lesson 115. Cắt tỉa lúc lập kế hoạch so với cắt tỉa lúc chạy, cái sau áp dụng khi điều kiện chỉ biết lúc chạy, và đọc được trong kế hoạch. Khoá phân vùng phải nằm trong khoá chính, ràng buộc kéo theo hệ quả thiết kế: khoá chính thành phức hợp. Gắn và tháo phân vùng là thao tác siêu dữ liệu nên gần như tức thì, đây là cách xoá dữ liệu cũ đúng cách thay vì xoá dòng. Gắn một bảng có sẵn làm phân vùng đòi kiểm ràng buộc, và cách tránh quét toàn bảng bằng khai báo ràng buộc trước. Chỉ mục trên bảng phân vùng tạo ra chỉ mục con trên từng phân vùng. Phân vùng mặc định và rủi ro của nó: một dòng sai khoá rơi vào đó và chặn việc gắn phân vùng mới. Số phân vùng hợp lý và chi phí lập kế hoạch khi quá nhiều. Tự động hoá tạo phân vùng theo lịch.

**Outcome.** Chuyển một bảng lớn sang phân vùng theo khoảng, và chứng minh cắt tỉa hoạt động cùng việc tháo phân vùng cũ nhanh hơn xoá dòng nhiều bậc.

**Đánh giá.** Tầng *áp dụng*. Objective có hai tiêu chí đo được. Đạt khi số phân vùng quét đọc từ kế hoạch đúng như mong đợi cho ba truy vấn, và khi thời gian tháo một phân vùng nhỏ hơn thời gian xoá số dòng tương đương ít nhất một bậc độ lớn.

**Lab.** Chuyển bảng 100 triệu dòng sang phân vùng theo tháng. Chạy ba truy vấn, đọc số phân vùng quét. So thời gian tháo một phân vùng với xoá số dòng tương đương. Chèn một dòng sai khoá vào phân vùng mặc định rồi thử gắn phân vùng mới, quan sát lỗi. Viết script tạo phân vùng theo lịch.

**Pitfalls.** Quên đưa khoá phân vùng vào khoá chính · để phân vùng mặc định nhận dòng sai rồi không gắn được phân vùng mới · tạo phân vùng theo ngày cho dữ liệu giữ 10 năm.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Số phân vùng quét đúng mong đợi cho ba truy vấn, và tháo phân vùng nhanh hơn xoá dòng ít nhất một bậc.

### Lesson 131 · WAL, checkpoints and tuning for write-heavy loads `TH`
**Prerequisites.** Lesson 130

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Nhật ký ghi trước của PostgreSQL theo mô hình ở lesson 118, và bài này chỉnh nó cho tải ghi nặng. Bốn tham số và đánh đổi: kích thước nhật ký tối đa quyết định khoảng cách giữa hai điểm kiểm tra, mục tiêu hoàn thành điểm kiểm tra trải việc ghi ra thời gian để tránh gai vào ra, khoảng thời gian điểm kiểm tra, và bộ đệm nhật ký. Ghi toàn trang sau mỗi điểm kiểm tra: lần sửa đầu tiên của một trang sau điểm kiểm tra phải ghi cả trang vào nhật ký để chống rách trang khi mất điện, nên điểm kiểm tra dày làm dung lượng nhật ký tăng vọt, một quan hệ phản trực giác. Gai vào ra lúc điểm kiểm tra và cách nhận ra trong biểu đồ giám sát. Nhật ký chưa lưu trữ chất đống khi lệnh lưu trữ hỏng, làm đầy đĩa và dừng cơ sở dữ liệu, một sự cố vận hành kinh điển. Mức nhật ký tối thiểu cho tải nạp một lần và rủi ro kèm theo.

**Outcome.** Chỉnh bốn tham số nhật ký cho một tải ghi nặng và chứng minh gai vào ra lúc điểm kiểm tra giảm, không đổi bằng việc tăng thời gian phục hồi quá mục tiêu.

**Đánh giá.** Tầng *đánh giá*. Objective đòi cân hai ràng buộc ngược nhau. Đạt khi độ lệch chuẩn của vào ra theo thời gian giảm ít nhất 30% so với cấu hình gốc, và khi thời gian phục hồi đo được vẫn dưới mục tiêu đã đặt ở lesson 118.

**Lab.** Chạy tải ghi nặng 30 phút, ghi biểu đồ vào ra theo giây với cấu hình mặc định, xác định gai điểm kiểm tra. Chỉnh bốn tham số, chạy lại, so hai biểu đồ và tính độ lệch chuẩn. Ngắt điện và đo thời gian phục hồi. Thử đặt điểm kiểm tra rất dày và đo dung lượng nhật ký sinh ra.

**Pitfalls.** Đặt điểm kiểm tra dày để giảm thời gian phục hồi rồi dung lượng nhật ký tăng vọt · để lệnh lưu trữ hỏng im lặng · đặt mức nhật ký tối thiểu trên cụm có bản sao.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Độ lệch chuẩn vào ra giảm ít nhất 30%, và thời gian phục hồi đo được vẫn dưới mục tiêu.

### Lesson 132 · Physical replication, streaming and failover `TH`
**Prerequisites.** Lesson 131

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bản sao vật lý truyền nhật ký ghi trước theo mô hình ở lesson 120. Bản sao nóng cho phép đọc trên bản sao, và xung đột phục hồi: một truy vấn dài trên bản sao chặn việc áp nhật ký, nên hệ thống phải chọn huỷ truy vấn hoặc để bản sao tụt lại, và hai tham số điều khiển lựa chọn đó. Khe bản sao giữ nhật ký cho tới khi bản sao nhận, tránh mất nhật ký nhưng gây đầy đĩa khi bản sao chết, nối lại lesson 126. Phản hồi từ bản sao về bản chính để hoãn thu hồi, giải xung đột phục hồi nhưng gây phình trên bản chính, một đánh đổi phải chọn có ý thức. Xác nhận đồng bộ và các mức của nó. Chuyển đổi dự phòng: nâng bản sao thành bản chính, và vấn đề bản chính cũ sống lại gây hai bản cùng nhận ghi. Dựng lại bản sao cũ sau chuyển đổi bằng công cụ đồng bộ thay vì sao chép toàn bộ. Đo độ trễ theo byte và theo thời gian, hai con số nói hai chuyện khác nhau.

**Outcome.** Dựng bản sao trực tuyến, gây xung đột phục hồi có chủ đích, và thực hiện chuyển đổi dự phòng rồi dựng lại bản sao cũ.

**Đánh giá.** Tầng *áp dụng*. Objective gồm ba thao tác vận hành có tiêu chí kiểm được. Đạt khi tái hiện được xung đột phục hồi và giải bằng đúng tham số, khi chuyển đổi dự phòng xong ứng dụng ghi được vào bản chính mới, và khi bản sao cũ được dựng lại mà không sao chép toàn bộ dữ liệu.

**Lab.** Dựng bản chính và bản sao nóng. Chạy truy vấn dài trên bản sao trong lúc bản chính cập nhật nhiều, quan sát truy vấn bị huỷ. Chỉnh tham số theo hai hướng và so hậu quả. Nâng bản sao thành bản chính. Dựng lại bản chính cũ thành bản sao bằng công cụ đồng bộ, đo lượng dữ liệu truyền.

**Pitfalls.** Bật phản hồi từ bản sao mà không theo dõi phình trên bản chính · để khe bản sao cho bản sao đã chết · dựng lại bản sao bằng cách sao chép toàn bộ thư mục dữ liệu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tái hiện và giải được xung đột phục hồi, chuyển đổi dự phòng thành công, và dựng lại bản sao cũ không sao chép toàn bộ.

### Lesson 133 · Logical replication and publication-subscription `TH`
**Prerequisites.** Lesson 132

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bản sao logic giải mã nhật ký ghi trước thành thay đổi mức dòng rồi phát đi, khác bản sao vật lý ở chỗ nó chọn được bảng, chuyển được giữa phiên bản chính, và bên nhận ghi được. Ấn phẩm và thuê bao. Điều kiện bảng tham gia: phải có định danh bản ghi, thường là khoá chính, nếu không thì cập nhật và xoá không truyền được. Ba hành vi khi thiếu khoá chính và cách khai báo định danh thay thế. Giải mã logic là nền của bắt thay đổi dữ liệu ở chặng 6, nên module này là chỗ học cơ chế trước khi gặp công cụ. Ảnh chụp ban đầu khi thuê bao bắt đầu và chi phí của nó trên bảng lớn. Xung đột trên bên nhận khi có ghi cục bộ, và cơ chế thuê bao dừng lại chờ can thiệp. Độ trễ và khe giải mã, cùng rủi ro đầy đĩa giống lesson 132. Thay đổi lược đồ không tự truyền, nên phải phối hợp thủ công, một hạn chế quan trọng.

**Outcome.** Dựng bản sao logic cho một tập bảng, và chỉ ra ba hạn chế khiến nó không thay thế được bản sao vật lý cho mục đích dự phòng.

**Đánh giá.** Tầng *phân tích*. Objective gồm một cài đặt và một phán đoán về ranh giới áp dụng. Đạt khi bản sao logic chạy và dữ liệu khớp, và khi ba hạn chế nêu ra đều được chứng minh bằng một thực nghiệm chứ không bằng trích dẫn tài liệu.

**Lab.** Dựng ấn phẩm cho ba bảng và thuê bao trên cụm khác. Đối soát dữ liệu. Tạo một bảng không có khoá chính, thử cập nhật và quan sát. Đổi lược đồ ở bên phát và quan sát bên nhận. Ghi cục bộ gây xung đột và quan sát thuê bao dừng. Đo thời gian ảnh chụp ban đầu trên bảng 20 triệu dòng.

**Pitfalls.** Dùng bản sao logic làm dự phòng toàn cụm · thêm bảng không có khoá chính vào ấn phẩm · đổi lược đồ một bên rồi tưởng bên kia tự theo.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bản sao logic chạy và dữ liệu khớp, và ba hạn chế đều có thực nghiệm chứng minh.

### Lesson 134 · Connection management, pooling and why PostgreSQL needs it `TH`
**Prerequisites.** Lesson 133

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** PostgreSQL tạo một tiến trình hệ điều hành cho mỗi kết nối, khác với mô hình luồng của một số hệ khác, và lựa chọn thiết kế này quyết định mọi thứ về quản lý kết nối. Chi phí một kết nối: bộ nhớ riêng, thời gian tạo tiến trình, và chi phí chuyển ngữ cảnh khi số tiến trình lớn, nối lại lesson 12. Hệ quả: số kết nối tối đa đặt cao không làm hệ thống chịu tải tốt hơn mà làm nó chậm đi, và ngưỡng hợp lý thường thấp hơn nhiều so với trực giác. Nhóm kết nối bên ngoài và ba chế độ gộp: theo phiên, theo giao dịch, theo câu lệnh, cùng tính năng nào mất đi ở từng chế độ. Chế độ theo giao dịch là mặc định hợp lý nhưng làm truy vấn chuẩn bị sẵn và bảng tạm không dùng được như thường. Kết nối rỗi trong giao dịch là trạng thái nguy hiểm nhất: nó giữ khoá và chặn thu hồi, nối lại lesson 116 và 125. Thời gian chờ để tự đóng kết nối rỗi trong giao dịch.

**Outcome.** Tìm số kết nối cho thông lượng cao nhất bằng thực nghiệm, và chứng minh nhóm kết nối bên ngoài giữ được thông lượng khi số ứng dụng khách vượt xa số đó.

**Đánh giá.** Tầng *đánh giá*. Objective đòi tìm một điểm cực đại và chứng minh giá trị của một thành phần thêm vào. Đạt khi có đường cong thông lượng theo số kết nối ở ít nhất sáu điểm cho thấy cực đại rồi giảm, và khi với 1.000 ứng dụng khách thì có nhóm kết nối giữ được ít nhất 80% thông lượng đỉnh còn không có thì sụp.

**Lab.** Chạy tải ở 10, 25, 50, 100, 200, 500 kết nối trực tiếp, đo thông lượng và độ trễ phân vị 95. Vẽ đường cong, xác định cực đại. Dựng nhóm kết nối chế độ theo giao dịch, chạy 1.000 ứng dụng khách qua nó, so với 1.000 kết nối trực tiếp. Thử truy vấn chuẩn bị sẵn qua nhóm và quan sát.

**Pitfalls.** Đặt số kết nối tối đa rất cao cho chắc · dùng chế độ theo giao dịch mà vẫn dựa vào bảng tạm · không đặt thời gian chờ cho kết nối rỗi trong giao dịch.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đường cong sáu điểm cho thấy cực đại rồi giảm, và nhóm kết nối giữ ít nhất 80% thông lượng đỉnh ở 1.000 ứng dụng khách.

### Lesson 135 · PostgreSQL operations project - diagnose, tune, recover `DA`
**Prerequisites.** Lesson 134

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Không có nội dung mới. Dự án gộp M11, gồm đúng sáu diễn tập trong tiêu chí ra module: một kế hoạch lệch ước lượng phải truy về nguyên nhân và sửa; một bảng phình phải đo và chỉnh thu hồi tự động cho riêng nó; một giao dịch dài phải định vị và chặn bằng thời gian chờ; một lần phục hồi tới thời điểm phải đo được điểm phục hồi và thời lượng phục hồi thật; độ trễ bản sao phải đo dưới ba mức tải và giải được một xung đột phục hồi; và một di trú lược đồ phá vỡ phải chạy không ngừng phục vụ theo mẫu bốn bước ở lesson 121. Nộp kèm sổ tay xử lý cho cả sáu tình huống theo khuôn ở lesson 90, mỗi bước là lệnh chạy được.

**Outcome.** Hoàn thành sáu diễn tập vận hành trên một cụm PostgreSQL có tải, mỗi diễn tập nộp số đo trước và sau cùng một mục sổ tay xử lý dùng lại được.

**Đánh giá.** Tầng *sáng tạo*. Objective là dựng một bộ quy trình vận hành dưới ràng buộc thật, không phải chạy sáu bài tập rời. Chấm theo sáu mục 15đ mỗi mục cộng 10đ cho tính nhất quán của sổ tay. Đạt khi ≥ 70/100 và không mục nào dưới 50%, vì một diễn tập bỏ trống nghĩa là sự cố đó chưa từng được luyện.

**Lab.** Cụm PostgreSQL có tải đọc ghi liên tục và một bản sao. Sáu diễn tập theo thứ tự tuỳ chọn, mỗi diễn tập tối đa 90 phút. Sau khi xong, đưa sổ tay cho một học viên khác và để họ thực hiện lại hai diễn tập bất kỳ theo tài liệu.

**Pitfalls.** Chỉnh tham số theo bài hướng dẫn thay vì theo số đo của mình · bỏ diễn tập phục hồi vì tốn thời gian · viết sổ tay bằng mô tả thay vì lệnh chạy được.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Đạt ≥ 70/100, không mục nào dưới 50%, và học viên khác thực hiện lại được hai diễn tập theo sổ tay.

# MODULE 12 · MYSQL

**Lessons 136–143 · 16 giờ**

| | |
|---|---|
| **Objective cấp module** | Chỉ ra ba quyết định thiết kế của InnoDB khiến cùng một lược đồ cho hiệu năng khác PostgreSQL, và chứng minh bằng số đo trên cùng bộ dữ liệu |
| **Tiền đề** | M11 |
| **Exit criterion** | Báo cáo so sánh MySQL với PostgreSQL trên cùng use case, có số đo cho chỉ mục phức hợp, bế tắc, độ trễ bản sao và khôi phục |
| **Kỹ năng SFIA** | `DBAD` mức 3 |
| **Chế độ hỏng** | Mang giả định PostgreSQL sang MySQL, nhất là về chỉ mục và khoá, rồi lược đồ chạy chậm mà không hiểu vì sao |

Mức `B`: làm lab và so sánh có căn cứ, không vận hành sản xuất. Module bám một trục duy nhất là khoá chính gom cụm của InnoDB, vì gần như mọi khác biệt với PostgreSQL suy ra từ đó. Bài cuối là báo cáo so sánh có số, và nó là đầu vào cho M18.

### Lesson 136 · InnoDB - the clustered primary key and what it changes `LT`
**Prerequisites.** Module 12: M11

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** InnoDB lưu dòng dữ liệu ngay trong lá của cây chỉ mục khoá chính, nên bảng chính là chỉ mục đó, khác hẳn mô hình đống của PostgreSQL ở lesson 123. Ba hệ quả suy ra từ một lựa chọn này. Một, thứ tự vật lý của dòng theo khoá chính, nên quét khoảng theo khoá chính rất rẻ còn chèn khoá ngẫu nhiên gây tách trang và phân mảnh; đây là lý do khoá tự tăng được khuyên dùng và khoá định danh ngẫu nhiên bị tránh. Hai, khoá chính lớn làm mọi chỉ mục phụ lớn theo, vì chỉ mục phụ lưu khoá chính thay vì con trỏ vật lý. Ba, không có khoá chính thì InnoDB tự tạo một khoá ẩn, nên bảng vẫn gom cụm nhưng theo một cột không kiểm soát được. Nhật ký hoàn tác lưu phiên bản cũ ở vùng riêng chứ không trong bảng, nên MySQL không có bài toán phình giống lesson 125 nhưng có bài toán nhật ký hoàn tác phình.

**Outcome.** Giải thích ba hệ quả của khoá chính gom cụm, và dự đoán bảng nào trong ba lược đồ cho trước sẽ phân mảnh nặng nhất.

**Đánh giá.** Tầng *phân tích*. Objective đòi suy từ một lựa chọn thiết kế ra nhiều hệ quả đo được. Đạt khi dự đoán đúng bảng phân mảnh nặng nhất và khi số đo phân mảnh sau khi chèn xác nhận thứ hạng dự đoán cho cả ba bảng.

**Lab.** Tạo ba bảng cùng lược đồ nhưng khoá chính khác nhau: tự tăng, định danh ngẫu nhiên, và khoá phức hợp rộng. Dự đoán thứ hạng phân mảnh. Chèn 5 triệu dòng vào mỗi bảng theo thứ tự ngẫu nhiên. Đo kích thước bảng, kích thước chỉ mục phụ, và thời gian chèn. So với dự đoán.

**Pitfalls.** Dùng định danh ngẫu nhiên làm khoá chính trong InnoDB · để bảng không có khoá chính · mang giả định mô hình đống của PostgreSQL sang.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Dự đoán đúng thứ hạng phân mảnh cho cả ba bảng, xác nhận bằng số đo kích thước và thời gian chèn.

### Lesson 137 · Secondary indexes and the double lookup `TH`
**Prerequisites.** Lesson 136

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Chỉ mục phụ lưu giá trị cột cộng khoá chính, nên tra cứu qua chỉ mục phụ là hai bước: tìm trong chỉ mục phụ ra khoá chính, rồi tìm trong cây khoá chính ra dòng. Chi phí bước hai là lý do chỉ mục phủ có giá trị lớn hơn ở MySQL so với ở PostgreSQL: khi mọi cột cần đều nằm trong chỉ mục phụ, bước hai biến mất hoàn toàn. Quy tắc tiền tố trái áp dụng như lesson 111, nhưng kết hợp với khoá chính ngầm ở cuối chỉ mục phụ tạo ra cơ hội phủ mà người quen PostgreSQL hay bỏ lỡ. Chỉ mục trên tiền tố chuỗi cho cột văn bản dài và mất mát kèm theo. Chỉ mục giảm dần và trường hợp nó cần. Chọn lọc của cột và thứ tự cột trong chỉ mục phức hợp: đặt cột chọn lọc cao trước là quy tắc mặc định nhưng không đúng khi truy vấn lọc khoảng trên cột đó.

**Outcome.** Thiết kế chỉ mục phủ cho ba truy vấn và chứng minh bước tra cứu thứ hai biến mất, bằng kế hoạch thực thi và số đo.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí đọc được từ kế hoạch. Đạt khi cả ba truy vấn chuyển sang dùng chỉ mục phủ, xác nhận bằng dấu hiệu trong kế hoạch, và khi thời gian giảm đo được. Thiết kế đúng mà kế hoạch không cho thấy phủ thì chưa đạt.

**Lab.** Bảng 20 triệu dòng. Ba truy vấn ban đầu dùng chỉ mục phụ có tra cứu hai bước. Thiết kế chỉ mục phủ cho từng cái. Đọc kế hoạch xác nhận. Đo thời gian trước sau. Thử đảo thứ tự cột trong một chỉ mục phức hợp có lọc khoảng và quan sát nó hỏng.

**Pitfalls.** Thêm cột vào chỉ mục cho phủ mà không đo chi phí ghi · đặt cột lọc khoảng trước cột lọc bằng · tạo chỉ mục tiền tố quá ngắn nên chọn lọc kém.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Cả ba truy vấn dùng chỉ mục phủ xác nhận bằng kế hoạch, và thời gian giảm đo được.

### Lesson 138 · Buffer pool, redo and undo `TH`
**Prerequisites.** Lesson 137

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bộ đệm của InnoDB theo mô hình ở lesson 110 nhưng có danh sách hai vùng mới và cũ để chống ô nhiễm bởi quét toàn bảng, một cơ chế PostgreSQL xử lý khác. Tỉ lệ trúng và cách đọc. Nhật ký làm lại có kích thước cố định và ghi vòng, khác PostgreSQL ghi theo tệp mới; hệ quả: nhật ký làm lại quá nhỏ gây điểm kiểm tra liên tục và chặn ghi, một nút cổ chai phổ biến và dễ sửa. Nhật ký hoàn tác giữ phiên bản cũ cho đọc nhất quán, và nó phình khi có giao dịch mở lâu, cùng nguyên nhân với lesson 116 nhưng biểu hiện ở chỗ khác. Bộ đệm thay đổi hoãn cập nhật chỉ mục phụ cho trang chưa nằm trong bộ đệm, một tối ưu ghi không có tương đương trực tiếp ở PostgreSQL. Xả bộ đệm và tham số điều khiển tốc độ. Thời điểm đồng bộ nhật ký khi xác nhận và ba mức đánh đổi giữa bền vững với thông lượng, nối lại lesson 16.

**Outcome.** Tìm nút cổ chai ghi bằng cách chỉnh kích thước nhật ký làm lại và mức đồng bộ, và định lượng đánh đổi giữa bền vững với thông lượng.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn một mức bền vững có hệ quả nghiệp vụ. Đạt khi có bảng ba mức đồng bộ kèm thông lượng và lượng dữ liệu mất khi ngắt điện đo thật, và khi lựa chọn cuối dẫn được về yêu cầu điểm phục hồi ở lesson 119.

**Lab.** Chạy tải ghi nặng với nhật ký làm lại nhỏ, quan sát chặn ghi. Tăng dần và đo thông lượng. Chạy ba mức đồng bộ, mỗi mức ngắt điện máy ảo và đếm giao dịch mất. Mở một giao dịch dài và đo nhật ký hoàn tác phình.

**Pitfalls.** Để nhật ký làm lại ở kích thước mặc định cho tải ghi nặng · hạ mức đồng bộ để nhanh mà không tính lượng dữ liệu mất · bỏ qua nhật ký hoàn tác phình vì bảng không phình.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng ba mức đồng bộ có thông lượng và số giao dịch mất đo thật, và lựa chọn dẫn được về yêu cầu điểm phục hồi.

### Lesson 139 · Locking, isolation and deadlocks in InnoDB `TH`
**Prerequisites.** Lesson 138

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Mức cô lập mặc định của MySQL là đọc lặp lại, khác mặc định đọc đã xác nhận của PostgreSQL, và giả định sai về điều này là nguồn lỗi khi chuyển hệ. Khoá hàng đặt trên bản ghi chỉ mục chứ không trên dòng dữ liệu, nên một cập nhật không dùng chỉ mục sẽ khoá mọi hàng nó quét qua, kể cả hàng không thoả điều kiện; đây là khác biệt vận hành lớn và là nguyên nhân phổ biến của tranh chấp bất ngờ. Khoá khoảng và khoá kề chặn chèn vào khoảng để ngăn đọc ảo ở mức đọc lặp lại, và chúng gây bế tắc theo cách không có ở PostgreSQL. Đọc nhất quán không khoá so với đọc có khoá tường minh. Phát hiện bế tắc và chọn nạn nhân theo mô hình ở lesson 117. Đọc nhật ký bế tắc của InnoDB để biết hai giao dịch giữ khoá nào trên chỉ mục nào. Thời gian chờ khoá và phân biệt hết thời gian chờ với bế tắc, hai lỗi khác nhau.

**Outcome.** Tái hiện một bế tắc do khoá khoảng gây ra, đọc nhật ký để xác định chỉ mục và khoảng bị khoá, và chứng minh cập nhật không dùng chỉ mục khoá thừa hàng.

**Đánh giá.** Tầng *phân tích*. Objective đòi chẩn đoán một cơ chế khoá riêng của InnoDB. Đạt khi xác định đúng chỉ mục và khoảng từ nhật ký bế tắc, và khi đếm được số hàng bị khoá bởi một cập nhật không dùng chỉ mục lớn hơn số hàng thoả điều kiện.

**Lab.** Dựng kịch bản bế tắc do khoá khoảng ở mức đọc lặp lại. Đọc nhật ký bế tắc, xác định chỉ mục và khoảng. Chạy một cập nhật lọc trên cột không có chỉ mục, đếm số hàng bị khoá qua khung nhìn hệ thống, so với số hàng thoả điều kiện. Thêm chỉ mục và đo lại.

**Pitfalls.** Giả định mặc định là đọc đã xác nhận như PostgreSQL · cập nhật lọc trên cột không có chỉ mục trên bảng lớn · nhầm hết thời gian chờ khoá với bế tắc.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Xác định đúng chỉ mục và khoảng từ nhật ký, và số hàng bị khoá lớn hơn số hàng thoả điều kiện đo được.

### Lesson 140 · The binary log - replication and change capture `TH`
**Prerequisites.** Lesson 139

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Nhật ký nhị phân ghi thay đổi ở mức logic và tách biệt với nhật ký làm lại ở mức vật lý, khác PostgreSQL dùng chung một nhật ký cho cả hai mục đích. Ba định dạng và khác biệt thực tế: theo câu lệnh gọn nhưng không tất định với hàm phụ thuộc ngữ cảnh, theo hàng an toàn nhưng tốn dung lượng, và hỗn hợp tự chọn. Định dạng theo hàng là điều kiện bắt buộc cho bắt thay đổi dữ liệu đáng tin, nên đây là bài đặt nền cho chặng 6. Ảnh trước và ảnh sau của một hàng trong sự kiện cập nhật, và vì sao có cả hai mới dựng lại được trạng thái. Định danh giao dịch toàn cục giúp chuyển đổi dự phòng không mất dấu vị trí. Thời gian giữ nhật ký nhị phân và hệ quả khi bản sao hoặc công cụ bắt thay đổi tụt quá xa: mất nhật ký thì phải nạp lại toàn bộ. Đọc nhật ký nhị phân bằng công cụ để xem sự kiện thô.

**Outcome.** Cấu hình nhật ký nhị phân ở định dạng theo hàng, đọc sự kiện thô của một cập nhật, và chỉ ra ảnh trước cùng ảnh sau.

**Đánh giá.** Tầng *áp dụng*. Objective có sản phẩm kiểm được trực tiếp. Đạt khi đọc được sự kiện thô và chỉ đúng ảnh trước ảnh sau cho ba loại thao tác, và khi chứng minh được định dạng theo câu lệnh cho kết quả khác trên một câu lệnh không tất định.

**Lab.** Bật nhật ký nhị phân theo hàng. Chạy chèn, cập nhật, xoá. Đọc sự kiện thô, chỉ ảnh trước và sau. Đổi sang định dạng theo câu lệnh, chạy một câu lệnh dùng hàm thời gian hiện tại, áp lên bản sao và so kết quả. Đặt thời gian giữ nhật ký ngắn rồi để bản sao tụt lại, quan sát hậu quả.

**Pitfalls.** Dùng định dạng theo câu lệnh cho bắt thay đổi dữ liệu · đặt thời gian giữ nhật ký nhị phân quá ngắn · giả định nhật ký nhị phân giống nhật ký làm lại.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chỉ đúng ảnh trước và sau cho ba loại thao tác, và chứng minh được định dạng theo câu lệnh cho kết quả khác.

### Lesson 141 · Replication, replica lag and failover `TH`
**Prerequisites.** Lesson 140

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bản sao của MySQL là bản sao logic dựa trên nhật ký nhị phân ở lesson 140, khác bản sao vật lý mặc định của PostgreSQL. Hai luồng trên bản sao: một luồng nhận sự kiện về nhật ký chuyển tiếp, một luồng áp sự kiện, và độ trễ có thể nằm ở luồng nào trong hai luồng đó, nên đo phải phân biệt hai chỉ số. Áp song song nhiều luồng và điều kiện an toàn để giữ thứ tự. Bản sao bán đồng bộ và cửa sổ mất dữ liệu còn lại. Độ trễ đo theo giây so với đo theo vị trí nhật ký, hai con số nói hai chuyện và con số theo giây gây hiểu nhầm khi bản chính rỗi. Bản sao phân kỳ do ghi trực tiếp vào bản sao, và vì sao phải đặt bản sao ở chế độ chỉ đọc. Chuyển đổi dự phòng và định danh giao dịch toàn cục. Dựng lại bản sao sau phân kỳ bằng nạp lại hoặc bằng công cụ đồng bộ, và chi phí của từng cách.

**Outcome.** Đo độ trễ bản sao phân biệt hai luồng, và tái hiện một trường hợp độ trễ theo giây bằng không trong khi bản sao vẫn tụt lại.

**Đánh giá.** Tầng *phân tích*. Objective đòi thấy được giới hạn của một chỉ số hay dùng. Đạt khi đo được hai chỉ số riêng cho hai luồng, và khi tái hiện được ca độ trễ theo giây bằng không nhưng vị trí nhật ký chênh lệch, giải thích được nguyên nhân.

**Lab.** Dựng bản chính và bản sao. Chạy tải ghi nặng, đo độ trễ theo cả hai cách và tách hai luồng. Dừng luồng áp, quan sát hai chỉ số phân kỳ. Cho bản chính rỗi trong lúc bản sao còn tồn đọng, quan sát độ trễ theo giây về không. Bật áp song song và đo lại.

**Pitfalls.** Chỉ theo dõi độ trễ theo giây · để bản sao cho phép ghi · bật áp song song mà không kiểm điều kiện giữ thứ tự.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đo được hai chỉ số riêng cho hai luồng, và tái hiện được ca độ trễ theo giây bằng không mà vị trí vẫn chênh.

### Lesson 142 · EXPLAIN in MySQL and where it differs `TH`
**Prerequisites.** Lesson 141

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Cột trong kết quả giải thích kế hoạch của MySQL và ý nghĩa vận hành của từng cột, đặc biệt kiểu truy cập, chỉ mục khả dụng so với chỉ mục được chọn, số dòng ước lượng, tỉ lệ lọc, và phần thông tin thêm. Tỉ lệ lọc là con số hay bị bỏ qua nhất: số dòng ước lượng nhân tỉ lệ lọc mới ra số dòng thật sự đi lên trên. Ba chuỗi trong phần thông tin thêm cần nhận ra ngay: dùng bảng tạm, dùng sắp xếp riêng, và dùng chỉ mục thuần. Chế độ phân tích thật có từ các phiên bản gần đây và cho số dòng thật cùng thời gian, tương tự lesson 129, nhưng phải kiểm phiên bản đang chạy chứ không giả định có. Bộ tối ưu hoá MySQL đơn giản hơn của PostgreSQL ở một số phép viết lại, nên cách viết truy vấn ảnh hưởng nhiều hơn. Gợi ý chỉ mục và gợi ý bộ tối ưu hoá, cùng nguyên tắc chỉ dùng khi đã hiểu nguyên nhân, nối lại lesson 128.

**Outcome.** Đọc một kế hoạch MySQL và tính số dòng thật sự đi lên trên từ số dòng ước lượng nhân tỉ lệ lọc, rồi đối chiếu với số đo.

**Đánh giá.** Tầng *phân tích*. Objective nhắm vào con số hay bị bỏ qua nhất trong kế hoạch MySQL. Đạt khi tính đúng số dòng cho bốn truy vấn với sai số dưới 30% so với số thật, và khi nhận ra đúng ba chuỗi cảnh báo trong phần thông tin thêm khi chúng xuất hiện.

**Lab.** Chạy sáu truy vấn, đọc kế hoạch. Với mỗi cái tính số dòng ước lượng nhân tỉ lệ lọc, so với số dòng thật từ chế độ phân tích. Tìm ba truy vấn có bảng tạm, sắp xếp riêng, và chỉ mục thuần. Kiểm phiên bản MySQL đang chạy có chế độ phân tích thật không.

**Pitfalls.** Đọc số dòng ước lượng mà bỏ tỉ lệ lọc · thêm gợi ý chỉ mục để ép kế hoạch thay vì sửa nguyên nhân · giả định phiên bản đang chạy có mọi tính năng mới.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tính đúng số dòng cho bốn truy vấn sai số dưới 30%, và nhận ra đúng ba chuỗi cảnh báo.

### Lesson 143 · MySQL against PostgreSQL - a measured comparison `TH`
**Prerequisites.** Lesson 142

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Không có cơ chế mới. Bài gộp module: chạy cùng một use case trên hai hệ và lập báo cáo so sánh có số. Sáu trục đo, mỗi trục gắn với một bài đã học: thiết kế chỉ mục phức hợp và chỉ mục phủ từ lesson 137, hành vi khoá và bế tắc từ lesson 139, chi phí ghi theo mức bền vững từ lesson 138, cơ chế bắt thay đổi từ lesson 140, độ trễ bản sao từ lesson 141, và khôi phục từ lesson 119. Nguyên tắc so sánh: cùng phần cứng, cùng dữ liệu, cùng truy vấn, và mỗi ô trong bảng phải dẫn một số đo chứ không dẫn một khẳng định. Chỗ hai hệ gần như không khác và không đáng tốn thời gian so. Kết luận phải phát biểu theo tải chứ không theo hệ: nói hệ nào hợp tải nào, không nói hệ nào tốt hơn. Báo cáo này là một trong bảy đầu vào của bài bảo vệ ở M18.

**Outcome.** Lập báo cáo so sánh sáu trục giữa MySQL và PostgreSQL trên cùng use case, mỗi ô dẫn một số đo từ lab của mình.

**Đánh giá.** Tầng *đánh giá*. Objective đòi so sánh có bằng chứng và kết luận theo tải. Kiểm bằng rà soát chéo: một học viên khác phải truy được mỗi ô về một số đo cụ thể. Đạt khi ít nhất 10 trên 12 ô đứng vững sau rà soát, và khi kết luận phát biểu theo tải chứ không xếp hạng hai hệ.

**Lab.** Chạy cùng use case đơn hàng 20 triệu dòng trên hai hệ, cùng phần cứng. Đo sáu trục. Lập bảng sáu nhân hai. Đổi báo cáo chéo và rà soát từng ô. Viết kết luận nêu hai tải cụ thể và hệ nào hợp hơn cho từng tải, kèm lý do từ số đo.

**Pitfalls.** So sánh trên phần cứng khác nhau · kết luận hệ nào tốt hơn nói chung · để trống ô rồi ghi tương đương mà chưa đo.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ít nhất 10 trên 12 ô đứng vững sau rà soát chéo, và kết luận phát biểu theo tải kèm lý do từ số đo.

# MODULE 13 · MONGODB

**Lessons 144–151 · 16 giờ**

| | |
|---|---|
| **Objective cấp module** | Mô hình hoá một miền nghiệp vụ bằng tài liệu, và chỉ ra ba tình huống mô hình tài liệu thắng mô hình quan hệ cùng ba tình huống ngược lại, có số đo |
| **Tiền đề** | M11 |
| **Exit criterion** | Mô hình đơn hàng chạy được, đo được chênh lệch có và không có chỉ mục, xử lý được một lần chuyển đổi dự phòng và một thay đổi lược đồ |
| **Kỹ năng SFIA** | `DBAD` mức 3 · `DTAN` mức 3 |
| **Chế độ hỏng** | Nhúng mọi thứ vào một tài liệu vì thấy tiện, rồi tài liệu lớn dần vượt giới hạn và mọi cập nhật phải ghi lại cả tài liệu |

Mức `B`. Module bám một câu hỏi thiết kế duy nhất là nhúng hay tham chiếu, vì phần lớn thành bại của một lược đồ tài liệu nằm ở đó. Sáu bài giữa là truy vấn, tổng hợp và vận hành; hai bài cuối là phân mảnh và giới hạn vận hành.

### Lesson 144 · The document model - embedding against referencing `LT`
**Prerequisites.** Module 13: M11

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Tài liệu là một bản ghi tự mô tả có cấu trúc lồng, và bộ sưu tập không bắt buộc mọi tài liệu cùng hình dạng. Lược đồ linh hoạt không có nghĩa không có lược đồ: nó chỉ chuyển việc thực thi lược đồ từ lúc ghi sang lúc đọc, và ứng dụng vẫn phải giả định một hình dạng. Nhúng đặt dữ liệu liên quan trong cùng tài liệu: một lần đọc lấy đủ, không có phép kết, nhưng tài liệu lớn dần và mọi cập nhật ghi lại phần lớn tài liệu. Tham chiếu đặt ở tài liệu riêng: cập nhật độc lập, nhưng cần nhiều lần đọc hoặc một phép kết ở tầng tổng hợp. Ba tiêu chí quyết định: quan hệ chứa hay quan hệ liên kết, tỉ lệ đọc trên ghi, và bản số quan hệ có chặn trên hay không. Bản số không chặn trên là dấu hiệu rõ nhất phải tham chiếu, vì tài liệu sẽ lớn không giới hạn. Giới hạn kích thước tài liệu và giới hạn độ sâu lồng. Giao dịch nhiều tài liệu có nhưng đắt hơn và không nên là mặc định.

**Outcome.** Chọn nhúng hay tham chiếu cho sáu quan hệ trong một miền nghiệp vụ, và biện minh bằng ba tiêu chí chứ không bằng cảm nhận.

**Đánh giá.** Tầng *đánh giá*. Objective đòi quyết định thiết kế có đánh đổi, không có đáp án chung. Kiểm bằng rà soát chéo sáu quyết định; đạt khi ít nhất năm quyết định nêu được cả ba tiêu chí và nêu được hậu quả của lựa chọn ngược lại.

**Lab.** Nhận miền nghiệp vụ thương mại điện tử có sáu quan hệ: đơn và dòng hàng, đơn và khách, khách và địa chỉ, sản phẩm và đánh giá, sản phẩm và danh mục, đơn và lịch sử trạng thái. Quyết định từng cái theo ba tiêu chí. Ước lượng kích thước tài liệu sau một năm cho mỗi lựa chọn nhúng.

**Pitfalls.** Nhúng quan hệ có bản số không chặn trên · tham chiếu mọi thứ vì quen mô hình quan hệ · dùng giao dịch nhiều tài liệu làm mặc định.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ít nhất năm trên sáu quyết định nêu đủ ba tiêu chí và hậu quả của lựa chọn ngược lại.

### Lesson 145 · Modelling an order domain as documents `TH`
**Prerequisites.** Lesson 144

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Chuyển quyết định ở lesson 144 thành lược đồ chạy được. Quy ước đặt tên trường và vì sao tên trường lưu trong mọi tài liệu nên tên dài tốn dung lượng thật ở quy mô lớn. Kiểu dữ liệu của MongoDB và ba chỗ hay sai: số thập phân cho tiền chứ không dùng số thực nhị phân, nối lại lesson 7; ngày giờ lưu theo chuẩn có múi giờ, nối lại lesson 9; và định danh tài liệu có thể dùng khoá nghiệp vụ thay cho định danh tự sinh khi khoá nghiệp vụ ổn định. Xác thực lược đồ ở tầng cơ sở dữ liệu để chặn tài liệu sai hình dạng, biến lược đồ ngầm thành lược đồ khai báo. Mẫu nhúng một phần: giữ vài trường thường đọc của tài liệu tham chiếu để tránh lần đọc thứ hai, đổi lấy việc phải cập nhật hai chỗ. Mẫu nhóm theo thời gian cho dữ liệu chuỗi thời gian. Ước lượng dung lượng từ lược đồ và số tài liệu.

**Outcome.** Cài đặt lược đồ tài liệu cho miền đơn hàng có xác thực ở tầng cơ sở dữ liệu, và chứng minh nó chặn được bốn loại tài liệu sai hình dạng.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí kiểm bằng chạy thật. Đạt khi bốn tài liệu sai đều bị từ chối bởi luật xác thực tương ứng, và khi ba lựa chọn kiểu dữ liệu nhạy cảm được biện minh bằng bài học ở chặng 1.

**Lab.** Cài lược đồ cho miền ở lesson 144. Thêm luật xác thực. Thử chèn bốn tài liệu sai: thiếu trường bắt buộc, tiền dạng số thực, ngày không có múi giờ, và mảng vượt giới hạn phần tử. Nạp 5 triệu tài liệu và đo dung lượng thật so với ước lượng.

**Pitfalls.** Dùng số thực nhị phân cho tiền · bỏ xác thực lược đồ vì đã có kiểm tra ở ứng dụng · đặt tên trường dài trong bộ sưu tập hàng trăm triệu tài liệu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn tài liệu sai đều bị đúng luật xác thực từ chối, và ba lựa chọn kiểu nhạy cảm có lý do.

### Lesson 146 · Indexes and the query planner `TH`
**Prerequisites.** Lesson 145

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Chỉ mục một trường, chỉ mục phức hợp, và quy tắc tiền tố tương tự lesson 111. Chỉ mục trên trường trong mảng sinh một mục cho mỗi phần tử, nên một tài liệu có mảng 1.000 phần tử tạo 1.000 mục chỉ mục, và chỉ được một chỉ mục loại này trong một chỉ mục phức hợp. Chỉ mục một phần và chỉ mục thưa, cùng khác biệt giữa hai loại. Chỉ mục văn bản và chỉ mục không gian ở mức biết có. Bộ lập kế hoạch chạy thử nhiều kế hoạch ứng viên trên một phần dữ liệu rồi chọn cái tốt nhất và lưu vào bộ đệm kế hoạch, khác cách tiếp cận dựa trên chi phí của PostgreSQL ở lesson 128; hệ quả là kế hoạch trong bộ đệm có thể không còn tốt khi dữ liệu đổi, và có cơ chế đánh giá lại. Đọc kế hoạch và ba chỉ số quan trọng: số tài liệu khảo sát, số mục chỉ mục khảo sát, và số tài liệu trả về. Tỉ lệ giữa số khảo sát và số trả về là thước đo hiệu quả chỉ mục.

**Outcome.** Thiết kế chỉ mục cho năm mẫu truy vấn và chứng minh hiệu quả bằng tỉ lệ số tài liệu khảo sát trên số tài liệu trả về.

**Đánh giá.** Tầng *áp dụng*. Objective có một thước đo cụ thể thay cho thời gian chạy. Đạt khi năm truy vấn đều đạt tỉ lệ khảo sát trên trả về dưới 2, và khi người học chỉ ra được một truy vấn mà chỉ mục trên mảng làm kích thước chỉ mục tăng vọt.

**Lab.** Bộ sưu tập 10 triệu tài liệu có mảng dòng hàng. Chạy năm truy vấn không chỉ mục, ghi ba chỉ số. Thiết kế chỉ mục, chạy lại, tính tỉ lệ. Tạo chỉ mục trên trường trong mảng và đo kích thước chỉ mục. Thử tạo chỉ mục phức hợp có hai trường mảng và quan sát lỗi.

**Pitfalls.** Đánh giá chỉ mục bằng thời gian thay vì bằng tỉ lệ khảo sát · tạo chỉ mục trên mảng lớn mà không đo dung lượng · tin bộ đệm kế hoạch luôn giữ kế hoạch tốt nhất.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Năm truy vấn đều đạt tỉ lệ khảo sát trên trả về dưới 2, và ca chỉ mục mảng tăng vọt dung lượng được chỉ ra.

### Lesson 147 · The aggregation pipeline `TH`
**Prerequisites.** Lesson 146

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Đường ống tổng hợp là chuỗi giai đoạn, mỗi giai đoạn nhận luồng tài liệu và phát ra luồng tài liệu, mô hình giống chuỗi ống dẫn ở lesson 20 và chuỗi hàm sinh ở lesson 64. Các giai đoạn thường dùng và thứ tự đặt chúng quyết định hiệu năng: đặt giai đoạn lọc và giới hạn sớm nhất có thể để giảm tài liệu đi xuống, đây chính là đẩy vị từ xuống ở lesson 115. Chỉ giai đoạn lọc và sắp xếp ở đầu đường ống mới dùng được chỉ mục, sau đó thì không, nên vị trí của chúng là ràng buộc cứng chứ không phải gợi ý. Giai đoạn tra cứu thực hiện phép kết trái và chi phí của nó, cùng lý do nó không thay thế được việc thiết kế lược đồ đúng ở lesson 144. Giai đoạn bung mảng và hiện tượng nhân dòng, cùng bản chất với lesson 100. Giới hạn bộ nhớ mỗi giai đoạn và tuỳ chọn cho phép tràn ra đĩa. Giai đoạn ghi kết quả ra bộ sưu tập, dùng cho khung nhìn vật chất hoá.

**Outcome.** Viết một đường ống tổng hợp cho năm câu hỏi nghiệp vụ, và tối ưu bằng cách đặt lại thứ tự giai đoạn, chứng minh bằng số tài liệu khảo sát.

**Đánh giá.** Tầng *áp dụng*. Objective gồm một sản phẩm và một phép tối ưu có bằng chứng. Đạt khi năm câu trả lời khớp đáp án đối chứng tính bằng SQL trên cùng dữ liệu, và khi ít nhất hai đường ống giảm số tài liệu khảo sát rõ rệt sau khi đặt lại thứ tự giai đoạn.

**Lab.** Trả lời năm câu hỏi nghiệp vụ bằng đường ống tổng hợp trên 10 triệu tài liệu. Đối chiếu với đáp án tính bằng SQL trên cùng dữ liệu nạp vào PostgreSQL. Với hai đường ống, đặt giai đoạn lọc ở cuối rồi chuyển lên đầu, đo số tài liệu khảo sát hai lần. Chạy một đường ống vượt giới hạn bộ nhớ.

**Pitfalls.** Đặt giai đoạn lọc sau giai đoạn tra cứu · dùng giai đoạn bung mảng mà không kiểm nhân dòng · tin rằng mọi giai đoạn đều dùng được chỉ mục.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Năm câu trả lời khớp đáp án SQL, và hai đường ống giảm số tài liệu khảo sát sau khi đặt lại thứ tự.

### Lesson 148 · Write concern, read concern and what they cost `TH`
**Prerequisites.** Lesson 147

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Mức bảo đảm ghi quy định bao nhiêu nút phải xác nhận trước khi lệnh ghi trả về, và nó là chỗ người dùng chọn vị trí của mình trên trục giữa bền vững và độ trễ. Ba mức thường dùng và cửa sổ mất dữ liệu của từng mức. Tuỳ chọn ghi nhật ký kết hợp với số nút xác nhận tạo ra ma trận lựa chọn, và mặc định không phải mức an toàn nhất. Mức bảo đảm đọc quy định đọc thấy dữ liệu ở mức cam kết nào, và đọc từ nút phụ có thể thấy dữ liệu sau đó bị quay lui nếu mức bảo đảm đọc thấp. Đọc sau ghi trong MongoDB và cách phiên nhân quả giải quyết nó, so với ba cách ở lesson 120. Quay lui khi nút chính cũ sống lại với dữ liệu chưa nhân bản: cơ chế, tệp quay lui, và vì sao mức bảo đảm ghi thấp làm việc này xảy ra. Đo chi phí thật của từng mức trên tải của mình thay vì đọc khuyến nghị.

**Outcome.** Đo độ trễ ghi ở ba mức bảo đảm và định lượng cửa sổ mất dữ liệu của từng mức bằng thực nghiệm giết nút chính.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn một mức có hệ quả nghiệp vụ, kèm số đo hai chiều. Đạt khi có bảng ba mức kèm cả độ trễ phân vị 95 lẫn số bản ghi mất khi giết nút chính, và khi lựa chọn cuối dẫn được về yêu cầu điểm phục hồi ở lesson 119.

**Lab.** Dựng tập bản sao ba nút. Chạy tải ghi ở ba mức bảo đảm, đo độ trễ phân vị 95. Với mỗi mức, giết nút chính giữa chừng và đếm số bản ghi mất sau khi bầu lại. Đọc tệp quay lui. Tái hiện đọc sau ghi trên nút phụ rồi sửa bằng phiên nhân quả.

**Pitfalls.** Để mức bảo đảm ghi mặc định cho dữ liệu giao dịch · đọc từ nút phụ mà không xét mức bảo đảm đọc · bỏ qua tệp quay lui sau chuyển đổi dự phòng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng ba mức có độ trễ và số bản ghi mất đo thật, và lựa chọn dẫn được về yêu cầu điểm phục hồi.

### Lesson 149 · Replica sets and failover `TH`
**Prerequisites.** Lesson 148

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Tập bản sao gồm một nút chính nhận ghi và các nút phụ nhân bản từ nhật ký thao tác. Nhật ký thao tác là bộ đệm vòng có kích thước cố định, nên nút phụ tụt quá xa sẽ không đuổi kịp và phải nạp lại toàn bộ, cùng vấn đề với lesson 140. Bầu chọn nút chính mới: điều kiện đa số, thời gian phát hiện, và vì sao cụm hai nút không chịu được mất một nút. Nút trọng tài và cảnh báo khi dùng nó thay cho nút dữ liệu thứ ba. Độ ưu tiên thành viên để điều khiển nút nào được làm chính. Nút ẩn và nút trễ có chủ đích, dùng để chống lỗi người vận hành xoá nhầm dữ liệu. Tuỳ chọn đọc từ nút nào và hệ quả về tính nhất quán, nối lại lesson 148. Theo dõi độ trễ nhân bản và kích thước nhật ký thao tác như hai chỉ số vận hành bắt buộc. Chuyển đổi dự phòng có kiểm soát để bảo trì, khác chuyển đổi do sự cố.

**Outcome.** Thực hiện chuyển đổi dự phòng có kiểm soát và chuyển đổi do sự cố, đo thời gian gián đoạn ghi của từng loại.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí đo được trực tiếp. Đạt khi đo được thời gian gián đoạn ghi cho cả hai loại chuyển đổi, và khi chứng minh được cụm hai nút không bầu được nút chính mới khi mất một nút còn cụm ba nút thì được.

**Lab.** Dựng tập bản sao ba nút với tải ghi liên tục. Chuyển đổi có kiểm soát, đo gián đoạn. Giết nút chính, đo gián đoạn. Hạ xuống hai nút, giết một, quan sát cụm không bầu được. Tính kích thước nhật ký thao tác đủ cho bao nhiêu giờ tải hiện tại.

**Pitfalls.** Dùng cụm hai nút cộng trọng tài cho dữ liệu quan trọng · để nhật ký thao tác kích thước mặc định cho tải ghi nặng · không đo thời gian gián đoạn trước khi cam kết mức dịch vụ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đo được gián đoạn ghi cho cả hai loại chuyển đổi, và chứng minh được khác biệt giữa cụm hai nút và ba nút.

### Lesson 150 · Sharding - shard keys and the choices you cannot undo `LT`
**Prerequisites.** Lesson 149

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Phân mảnh chia dữ liệu ngang qua nhiều cụm theo một khoá, và khoá phân mảnh là quyết định khó đảo ngược nhất trong MongoDB. Ba tính chất của một khoá tốt: bản số đủ lớn, phân bố đều, và khớp mẫu truy vấn thường gặp. Khoá tăng đơn điệu như dấu thời gian làm mọi lệnh ghi dồn vào một mảnh, cùng vấn đề với lesson 136 nhưng ở quy mô cụm. Phân mảnh theo khoảng giữ được quét khoảng rẻ nhưng dễ lệch; phân mảnh theo băm phân bố đều nhưng mất quét khoảng, nối lại lesson 48. Khoá phức hợp để cân hai tính chất. Truy vấn không chứa khoá phân mảnh phải hỏi mọi mảnh rồi gộp, nên chi phí tỉ lệ số mảnh chứ không giảm theo. Cân bằng lại và chi phí di chuyển đoạn dữ liệu trong lúc phục vụ. Khi nào chưa cần phân mảnh: phần lớn tải vừa một cụm bản sao, và phân mảnh sớm thêm phức tạp mà không thêm năng lực.

**Outcome.** Đánh giá bốn khoá phân mảnh ứng viên theo ba tính chất, và chỉ ra tình huống một khoá tốt cho ghi lại tồi cho đọc.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn dưới đánh đổi và nhận ra xung đột giữa hai mục tiêu. Đạt khi bốn ứng viên được chấm theo cả ba tính chất, khi chỉ ra đúng khoá tăng đơn điệu gây dồn ghi, và khi nêu được một khoá tốt cho ghi nhưng làm truy vấn thường gặp phải hỏi mọi mảnh.

**Lab.** Nhận bốn khoá ứng viên cho bộ sưu tập đơn hàng: dấu thời gian, định danh khách băm, định danh khách cộng dấu thời gian, và định danh đơn tự sinh. Chấm theo ba tính chất. Với ba truy vấn thường gặp, xác định truy vấn nào phải hỏi mọi mảnh ứng với từng khoá. Lập bảng bốn nhân ba.

**Pitfalls.** Chọn dấu thời gian làm khoá phân mảnh · phân mảnh khi dữ liệu còn vừa một cụm bản sao · chọn khoá tối ưu cho ghi mà không xét mẫu đọc.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn ứng viên chấm đủ ba tính chất, và bảng bốn nhân ba chỉ đúng truy vấn nào phải hỏi mọi mảnh.

### Lesson 151 · Document growth, schema change and operational limits `TH`
**Prerequisites.** Lesson 150

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Tài liệu lớn dần là chế độ hỏng đặc trưng của mô hình nhúng, và nó có ba hậu quả cùng lúc: chạm giới hạn kích thước, mỗi cập nhật ghi lại phần lớn tài liệu, và dịch chuyển tài liệu khi không còn vừa chỗ cũ. Đo phân bố kích thước tài liệu theo thời gian như một chỉ số cảnh báo sớm. Mẫu ngoài dòng khi một mảng nhúng vượt ngưỡng: chuyển sang tham chiếu và giữ một phần nhúng, nối lại lesson 145. Thay đổi lược đồ trên bộ sưu tập lớn: ba chiến lược là chuyển đổi lúc đọc, chuyển đổi nền theo lô, và giữ trường phiên bản trong tài liệu để ứng dụng xử lý nhiều hình dạng cùng lúc. Chiến lược thứ ba là mẫu thực dụng nhất và ít bị nhắc tới nhất. Giới hạn vận hành cần biết trước khi thiết kế: kích thước tài liệu, độ sâu lồng, số bộ sưu tập, và giới hạn của giai đoạn tổng hợp. Cập nhật tại chỗ trên một phần tử mảng thay vì ghi lại cả mảng.

**Outcome.** Phát hiện một bộ sưu tập có tài liệu lớn dần bằng phân bố kích thước, và chuyển mảng nhúng sang tham chiếu mà không ngừng phục vụ.

**Đánh giá.** Tầng *áp dụng*. Objective có hai tiêu chí kiểm được. Đạt khi phân bố kích thước cho thấy xu hướng tăng và nêu được thời điểm ước tính chạm giới hạn, và khi chuyển đổi hoàn tất với tải đọc ghi chạy suốt không lỗi, dùng trường phiên bản để xử lý hai hình dạng cùng lúc.

**Lab.** Bộ sưu tập 5 triệu tài liệu có mảng lịch sử trạng thái tăng dần. Đo phân bố kích thước ở ba mốc, ngoại suy thời điểm chạm giới hạn. Chuyển mảng sang bộ sưu tập riêng theo ba bước, dùng trường phiên bản, giữ tải chạy suốt. Đo thời gian cập nhật một phần tử trước và sau.

**Pitfalls.** Nhúng mảng không chặn trên rồi chờ tới khi lỗi · chuyển đổi lược đồ bằng một lần cập nhật hàng loạt trên bộ sưu tập lớn · ghi lại cả mảng khi chỉ đổi một phần tử.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân bố kích thước cho thấy xu hướng và thời điểm chạm giới hạn, và chuyển đổi xong với tải chạy suốt không lỗi.

# MODULE 14 · REDIS

**Lessons 152–158 · 14 giờ**

| | |
|---|---|
| **Objective cấp module** | Thiết kế một lớp đệm có ngưỡng đo được, và trả lời được câu hỏi khi nào nên bỏ lớp đệm đó đi |
| **Tiền đề** | M11 |
| **Exit criterion** | Lớp đệm có tỉ lệ trúng đo được, chịu được ồ ạt nạp lại, và có phương án khi mất sạch dữ liệu đệm |
| **Kỹ năng SFIA** | `DBAD` mức 3 · `SYSP` mức 3 |
| **Chế độ hỏng** | Dùng Redis làm nguồn dữ liệu bền vững mà chưa thiết kế độ bền, rồi mất dữ liệu khi khởi động lại |

Mức `B`. Redis khác sáu hệ còn lại ở chỗ nó không phải nơi lưu dữ liệu gốc trong phần lớn kiến trúc, nên câu hỏi trung tâm của module không phải dùng thế nào mà là khi nào nên có và khi nào nên bỏ. Bài cuối đo hiệu quả lớp đệm và nêu điều kiện gỡ bỏ.

### Lesson 152 · In-memory data structures and what each one is for `TH`
**Prerequisites.** Module 14: M11

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Năm cấu trúc chính và bài toán mỗi cấu trúc giải, nối lại lesson 63 nhưng ở tầng dịch vụ mạng. Chuỗi cho giá trị đơn và bộ đếm nguyên tử. Băm cho đối tượng nhiều trường, cho phép đọc ghi một trường mà không tải cả đối tượng. Danh sách cho hàng đợi đơn giản, cùng cảnh báo rằng nó không phải hệ thống hàng đợi thật vì thiếu xác nhận và thử lại, nối tới chặng 6. Tập cho kiểm tra thành viên và phép toán tập hợp. Tập có điểm cho bảng xếp hạng và cho hàng đợi ưu tiên theo thời gian. Chi phí thời gian của từng lệnh và vì sao phải tra trước khi dùng: một số lệnh là tuyến tính theo kích thước cấu trúc và chúng chặn cả máy chủ vì mô hình một luồng. Quy ước đặt tên khoá và vì sao thiết kế không gian khoá quan trọng: khoá là giao diện duy nhất, không có lược đồ và không có chỉ mục.

**Outcome.** Chọn cấu trúc cho năm bài toán đệm và chứng minh lựa chọn bằng số đo bộ nhớ và độ trễ.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn có đánh đổi hai chiều. Đạt khi năm lựa chọn đều có số đo bộ nhớ và độ trễ phân vị 95, và khi ít nhất một lựa chọn tránh được một lệnh có chi phí tuyến tính, nêu rõ lệnh nào bị tránh và vì sao.

**Lab.** Năm bài toán: đệm đối tượng khách, bộ đếm lượt xem, danh sách sản phẩm vừa xem, kiểm tra một khoá có trong tập cấm không, và bảng xếp hạng bán chạy. Cài mỗi bài bằng ít nhất hai cấu trúc. Đo bộ nhớ và độ trễ. Chạy một lệnh tuyến tính trên cấu trúc một triệu phần tử và đo thời gian chặn.

**Pitfalls.** Dùng chuỗi lưu JSON rồi phải tải cả đối tượng để đọc một trường · chạy lệnh liệt kê toàn bộ khoá trên máy chủ sản xuất · dùng danh sách làm hàng đợi công việc thật.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Năm lựa chọn đều có số đo bộ nhớ và độ trễ, và ít nhất một lựa chọn tránh được một lệnh tuyến tính có nêu lý do.

### Lesson 153 · Expiry, eviction policies and the memory ceiling `TH`
**Prerequisites.** Lesson 152

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Thời gian sống đặt trên khoá và ba cách hết hạn xảy ra: kiểm khi truy cập, quét chủ động theo mẫu ngẫu nhiên, và loại bỏ khi chạm trần bộ nhớ. Hệ quả của cách thứ hai: khoá đã hết hạn vẫn chiếm bộ nhớ một thời gian, nên bộ nhớ dùng không giảm ngay sau khi đặt thời gian sống ngắn. Trần bộ nhớ và tám chính sách loại bỏ, chia hai nhóm: chỉ loại khoá có thời gian sống, hoặc loại mọi khoá. Chọn nhóm nào là quyết định kiến trúc: nhóm thứ hai biến Redis thành bộ đệm thuần, nhóm thứ nhất giữ được dữ liệu không có thời gian sống nhưng rủi ro đầy bộ nhớ và từ chối ghi. Chính sách dùng gần đây nhất so với dùng nhiều nhất và tải nào hợp với cái nào. Không đặt trần bộ nhớ là lỗi cấu hình phổ biến nhất và nó dẫn tới bị hệ điều hành giết, nối lại lesson 14. Đo phân bố thời gian sống và tỉ lệ khoá bị loại.

**Outcome.** Chọn chính sách loại bỏ và trần bộ nhớ cho một tải cho trước, và chứng minh hệ thống không bị giết cũng không từ chối ghi khi dữ liệu vượt trần.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn dưới hai rủi ro đối lập. Đạt khi chạy tải vượt trần 3 lần mà tiến trình không bị giết và không lệnh ghi nào bị từ chối, và khi bảng so ít nhất ba chính sách kèm tỉ lệ trúng của từng cái.

**Lab.** Đặt trần bộ nhớ thấp hơn tập dữ liệu ba lần. Chạy tải với ba chính sách loại bỏ khác nhau, đo tỉ lệ trúng và số khoá bị loại. Thử chính sách không loại gì và quan sát lệnh ghi bị từ chối. Bỏ trần bộ nhớ và quan sát tiến trình bị giết. Đo độ trễ giữa lúc khoá hết hạn và lúc bộ nhớ thật giảm.

**Pitfalls.** Không đặt trần bộ nhớ · dùng chính sách chỉ loại khoá có thời gian sống trong khi phần lớn khoá không có · tin bộ nhớ giảm ngay khi khoá hết hạn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tải vượt trần 3 lần không làm tiến trình bị giết và không lệnh ghi nào bị từ chối, và có bảng so ba chính sách.

### Lesson 154 · Persistence - snapshots, append-only file and what you lose `TH`
**Prerequisites.** Lesson 153

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hai cơ chế bền vững và đánh đổi khác nhau. Ảnh chụp định kỳ ghi toàn bộ tập dữ liệu ra tệp: nhỏ gọn, khởi động lại nhanh, nhưng mất mọi thay đổi từ ảnh chụp cuối. Tệp chỉ ghi thêm ghi từng lệnh: mất ít hơn nhiều, nhưng tệp lớn dần và khởi động lại chậm vì phải chạy lại lệnh. Ba mức đồng bộ của tệp chỉ ghi thêm và cửa sổ mất dữ liệu tương ứng, cùng cấu trúc với lesson 16 và 138. Viết lại tệp chỉ ghi thêm để nén lịch sử, và chi phí bộ nhớ lúc viết lại do sao chép tiến trình. Dùng cả hai cơ chế cùng lúc. Điểm phục hồi thật của Redis trong từng cấu hình, và vì sao nó thường tệ hơn một cơ sở dữ liệu quan hệ. Kết luận kiến trúc rút ra: coi Redis là nguồn dữ liệu gốc chỉ hợp lý khi đã đo điểm phục hồi và nghiệp vụ chấp nhận con số đó, còn mặc định nên coi nó là lớp đệm mất được.

**Outcome.** Đo điểm phục hồi thật ở bốn cấu hình bền vững bằng thực nghiệm giết tiến trình, và kết luận cấu hình nào đủ để giữ dữ liệu gốc.

**Đánh giá.** Tầng *đánh giá*. Objective đòi kết luận về một quyết định kiến trúc dựa trên số đo. Đạt khi bốn cấu hình đều có số bản ghi mất và thời gian khởi động lại đo thật, và khi kết luận nêu rõ ngưỡng nghiệp vụ nào chấp nhận được cấu hình nào.

**Lab.** Chạy tải ghi 10.000 lệnh mỗi giây. Với bốn cấu hình bền vững, giết tiến trình đột ngột và đếm số lệnh mất, rồi đo thời gian khởi động lại. Lập bảng. Chạy viết lại tệp chỉ ghi thêm trong lúc tải cao và đo bộ nhớ đỉnh.

**Pitfalls.** Dùng Redis làm nguồn gốc với cấu hình mặc định · bật tệp chỉ ghi thêm mà không đo thời gian khởi động lại · viết lại tệp lúc bộ nhớ đã gần trần.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn cấu hình có số lệnh mất và thời gian khởi động lại đo thật, và kết luận nêu ngưỡng nghiệp vụ tương ứng.

### Lesson 155 · Cache-aside, stampede and cache consistency `TH`
**Prerequisites.** Lesson 154

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba mẫu đệm và trách nhiệm khác nhau: đọc qua ứng dụng, đọc qua lớp đệm, và ghi xuyên qua. Mẫu đọc qua ứng dụng là mẫu phổ biến nhất và là mẫu module tập trung vào. Ồ ạt nạp lại xảy ra khi một khoá nóng hết hạn và hàng nghìn yêu cầu cùng lúc đi xuống cơ sở dữ liệu, có thể làm sập nó; ba cách chống là khoá nạp lại, nạp lại trước khi hết hạn, và thêm nhiễu ngẫu nhiên vào thời gian sống, mẫu nhiễu này cùng ý tưởng với lesson 34. Nhất quán giữa đệm và nguồn: xoá khoá khi ghi thay vì cập nhật khoá, vì cập nhật tạo cửa sổ tranh chấp giữa hai thao tác không nguyên tử, nối lại lesson 51. Thứ tự xoá đệm và ghi nguồn, cùng cửa sổ không nhất quán còn lại trong mỗi thứ tự. Đệm giá trị rỗng để chống truy vấn lặp cho khoá không tồn tại. Thời gian sống là công cụ nhất quán chính: mọi thiết kế đệm cuối cùng đều dựa vào nó để tự sửa.

**Outcome.** Tái hiện ồ ạt nạp lại và chặn nó bằng một trong ba cách, chứng minh bằng số yêu cầu đi xuống cơ sở dữ liệu.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí đếm được. Đạt khi tái hiện được ít nhất 500 yêu cầu cùng đi xuống cơ sở dữ liệu khi khoá nóng hết hạn, và khi bản sửa hạ con số đó xuống dưới 5 trong cùng kịch bản.

**Lab.** Dựng lớp đệm đọc qua ứng dụng cho một khoá nóng. Cho 1.000 ứng dụng khách đồng thời, đặt thời gian sống ngắn, đếm số yêu cầu xuống cơ sở dữ liệu tại thời điểm hết hạn. Cài một trong ba cách chống, đo lại. Tái hiện đệm không nhất quán bằng cách cập nhật khoá thay vì xoá.

**Pitfalls.** Cập nhật khoá đệm thay vì xoá · đặt cùng thời gian sống cho mọi khoá nên chúng hết hạn cùng lúc · không đệm giá trị rỗng nên truy vấn lặp cho khoá không tồn tại.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tái hiện được ít nhất 500 yêu cầu cùng xuống cơ sở dữ liệu, và bản sửa hạ xuống dưới 5.

### Lesson 156 · Hot keys, big keys and blocking commands `TH`
**Prerequisites.** Lesson 155

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Redis xử lý lệnh trên một luồng, nên một lệnh chậm chặn mọi lệnh khác, và đây là nguồn gốc của ba vấn đề trong bài. Khoá nóng: một khoá nhận phần lớn lưu lượng, làm một nút hoặc một lõi bão hoà trong khi phần còn lại rỗi, cùng bản chất với lệch phân vùng ở lesson 48; ba cách xử lý là chia khoá thành nhiều bản, đệm cục bộ ở tầng ứng dụng, và giảm tần suất truy cập. Khoá lớn: một cấu trúc hàng triệu phần tử làm mọi lệnh chạm nó thành chậm, và xoá nó cũng chặn, nên có lệnh xoá nền. Lệnh chặn cần tránh trên máy chủ sản xuất và lệnh quét thay thế. Đo độ trễ theo phân vị chứ không theo trung bình, vì một lệnh chặn làm đuôi phân bố dài ra mà trung bình không thấy, nối lại lesson 17. Nhật ký lệnh chậm và cách đọc nó. Quy mô theo chiều ngang bị giới hạn bởi khoá nóng vì thêm nút không giúp gì.

**Outcome.** Định vị một khoá nóng và một khoá lớn trên hệ thống đang chạy, và chứng minh chúng làm đuôi phân bố độ trễ dài ra.

**Đánh giá.** Tầng *phân tích*. Objective đòi chẩn đoán bằng phân vị chứ không bằng trung bình. Đạt khi định vị đúng cả khoá nóng lẫn khoá lớn bằng công cụ, và khi số đo cho thấy phân vị 99 tăng rõ rệt trong khi trung bình gần như không đổi.

**Lab.** Dựng tải có một khoá nhận 80% lưu lượng và một khoá chứa một triệu phần tử. Đo độ trễ trung bình và phân vị 99. Dùng công cụ tìm khoá nóng và khoá lớn. Chạy một lệnh chặn trên khoá lớn và đo tác động lên phân vị 99. Xoá khoá lớn bằng lệnh thường rồi bằng lệnh xoá nền, so thời gian chặn.

**Pitfalls.** Theo dõi độ trễ trung bình · chạy lệnh liệt kê toàn bộ khoá để tìm khoá lớn · thêm nút để chữa khoá nóng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Định vị đúng khoá nóng và khoá lớn, và số đo cho thấy phân vị 99 tăng trong khi trung bình gần như không đổi.

### Lesson 157 · Replication, sentinel and cluster mode `LT`
**Prerequisites.** Lesson 156

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Ba mức tổ chức và bài toán mỗi mức giải. Nhân bản chính phụ bất đồng bộ cho đọc mở rộng và dự phòng, với cửa sổ mất dữ liệu bằng độ trễ, cùng mô hình lesson 120. Người canh gác giám sát và tự chuyển đổi dự phòng, cần đa số để tránh chia đôi cụm. Chế độ cụm phân mảnh dữ liệu theo khe băm, cho mở rộng ghi; hệ quả là lệnh chạm nhiều khoá chỉ chạy được khi các khoá cùng khe, và thẻ khoá là cách ép chúng cùng khe. Không có giao dịch xuyên mảnh. Phân biệt ba nhu cầu để chọn đúng mức: cần dự phòng thì nhân bản đủ, cần tự chuyển đổi thì thêm người canh gác, cần vượt bộ nhớ một máy mới cần cụm. Sai lầm thường gặp là dựng cụm khi chỉ cần nhân bản, chuốc thêm ràng buộc khoá cùng khe mà không được lợi gì. Chia đôi cụm và mất ghi khi hai bên cùng nhận.

**Outcome.** Chọn mức tổ chức cho ba yêu cầu khác nhau, và nêu ràng buộc mà chế độ cụm áp lên cách viết lệnh.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết vì dựng cụm đầy đủ vượt phạm vi mức `B`. Đạt khi chọn đúng mức cho ba yêu cầu kèm lý do, và khi chỉ ra được hai lệnh không chạy được ở chế độ cụm cùng cách sửa bằng thẻ khoá.

**Lab.** Nhận ba yêu cầu: chịu được mất một máy, tự phục hồi không cần người, và tập dữ liệu vượt bộ nhớ một máy. Chọn mức cho từng cái. Dựng nhân bản chính phụ và đo độ trễ. Trên một cụm thử nghiệm, chạy hai lệnh chạm nhiều khoá, quan sát lỗi, sửa bằng thẻ khoá.

**Pitfalls.** Dựng chế độ cụm khi chỉ cần nhân bản · giả định giao dịch chạy xuyên mảnh · dùng người canh gác số chẵn nên không có đa số.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chọn đúng mức cho ba yêu cầu kèm lý do, và chỉ ra được hai lệnh cần thẻ khoá cùng cách sửa.

### Lesson 158 · Measuring a cache - hit rate, p95 and when to remove it `TH`
**Prerequisites.** Lesson 157

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Không có cơ chế mới. Bài gộp module và nó đặt câu hỏi ngược với phần còn lại: khi nào nên bỏ lớp đệm. Bốn chỉ số đo một lớp đệm: tỉ lệ trúng, độ trễ phân vị 95 của đường có đệm và đường không đệm, tải giảm được ở cơ sở dữ liệu, và chi phí vận hành gồm cả bộ nhớ lẫn thời gian người. Tỉ lệ trúng một mình không kết luận được gì: tỉ lệ trúng 95% trên một truy vấn vốn đã nhanh thì lớp đệm không đáng tồn tại. Phép tính lợi ích ròng: thời gian tiết kiệm nhân số lượt trừ chi phí. Ba điều kiện nên bỏ lớp đệm: nguồn đã đủ nhanh sau khi thêm chỉ mục, tỉ lệ trúng thấp kéo dài, và chi phí nhất quán vượt lợi ích. Rủi ro lớp đệm trở thành phụ thuộc cứng: hệ thống không sống nổi khi mất đệm, và phép thử là tắt đệm trong giờ thấp điểm rồi đo. Kế hoạch cho tình huống mất sạch dữ liệu đệm.

**Outcome.** Đo bốn chỉ số của một lớp đệm và kết luận nên giữ hay nên bỏ, kèm phép thử tắt đệm để xác nhận hệ thống sống được.

**Đánh giá.** Tầng *đánh giá*. Objective đòi kết luận về sự tồn tại của một thành phần, không chỉ tối ưu nó. Đạt khi bốn chỉ số đều có số, khi phép tính lợi ích ròng được trình bày, và khi phép thử tắt đệm chạy thật cho biết hệ thống sống được hay không.

**Lab.** Đo bốn chỉ số cho lớp đệm dựng ở lesson 155. Tính lợi ích ròng. Thêm chỉ mục cho truy vấn nguồn rồi đo lại, xem lợi ích còn bao nhiêu. Tắt đệm hoàn toàn trong 10 phút dưới tải và đo. Viết kế hoạch cho tình huống mất sạch dữ liệu đệm, gồm cả cách nạp lại dần thay vì cùng lúc.

**Pitfalls.** Báo cáo tỉ lệ trúng một mình · giữ lớp đệm vì đã dựng rồi · không bao giờ thử tắt đệm nên không biết hệ thống có sống được không.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn chỉ số đều có số, có phép tính lợi ích ròng, và phép thử tắt đệm chạy thật cho kết luận rõ ràng.

# MODULE 15 · BIGQUERY

**Lessons 159–166 · 16 giờ**

| | |
|---|---|
| **Objective cấp module** | Dự đoán lượng dữ liệu quét và chi phí của một truy vấn trước khi chạy, rồi giảm nó bằng phân vùng, phân cụm và vật chất hoá |
| **Tiền đề** | M11 |
| **Exit criterion** | Giảm chi phí một bộ truy vấn ít nhất 70% bằng thiết kế bảng, có số byte quét trước và sau, và không vượt hạn mức chi tiêu đã đặt |
| **Kỹ năng SFIA** | `DBAD` mức 3 · `FMIT` mức 2 |
| **Chế độ hỏng** | Chạy truy vấn thử nghiệm trên bảng lớn mà không xem ước lượng byte quét, rồi nhận hoá đơn bất ngờ |

Mức `B`. Đây là module duy nhất trong bảy hệ chạy trên dịch vụ đám mây tính tiền thật, nên có một ràng buộc cứng: **đặt hạn mức chi tiêu và cảnh báo ngân sách trước khi chạy truy vấn đầu tiên**, và mọi lab thiết kế để chạy trong bậc miễn phí hoặc môi trường thử nghiệm. Ai không có tài khoản đám mây thì làm phần thiết kế và ước lượng, bỏ phần đo thật, và ghi rõ là chưa chạy được.

### Lesson 159 · Serverless columnar warehouse - the model and what it changes `LT`
**Prerequisites.** Module 15: M11

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Tách lưu trữ khỏi tính toán là khác biệt nền tảng so với sáu hệ còn lại: không có máy chủ để chỉnh tham số, không có bộ đệm để cấu hình, không có chỉ mục để tạo. Mọi đòn bẩy hiệu năng chuyển sang ba thứ: bố trí dữ liệu, lượng dữ liệu quét, và cách viết truy vấn. Lưu trữ theo cột theo mô hình ở lesson 70, nên chọn ít cột là đòn bẩy giảm chi phí trực tiếp và đây là lý do chọn mọi cột ở đây đắt hơn hẳn so với ở cơ sở dữ liệu quan hệ. Đơn vị tính toán và hai mô hình định giá: theo lượng dữ liệu quét và theo dung lượng tính toán đặt trước, cùng ngưỡng chuyển đổi. Ước lượng byte quét trước khi chạy bằng chế độ chạy thử, thao tác bắt buộc trước mọi truy vấn trong module. Giới hạn và hạn ngạch. Vì sao khái niệm chỉ mục không tồn tại ở đây và cái gì thay thế nó, dẫn sang lesson 161.

**Outcome.** Ước lượng byte quét và chi phí của năm truy vấn trước khi chạy, và giải thích vì sao chọn ít cột giảm chi phí ở đây nhiều hơn ở PostgreSQL.

**Đánh giá.** Tầng *hiểu*. Bài mở module, objective dừng ở ước lượng và giải thích cơ chế. Đạt khi năm ước lượng khớp con số chế độ chạy thử đưa ra, và khi giải thích đúng quan hệ giữa lưu trữ theo cột với chi phí. Ai không có tài khoản thì làm phần ước lượng trên lược đồ và ghi rõ chưa đo thật.

**Lab.** Đặt hạn mức chi tiêu và cảnh báo ngân sách trước tiên. Trên một bảng công khai, chạy chế độ chạy thử cho năm truy vấn khác nhau về số cột và bộ lọc. Ghi byte quét ước lượng. Chạy thật, so byte quét thực tế. Tính chi phí từng truy vấn theo đơn giá hiện hành, ghi rõ ngày tra đơn giá.

**Pitfalls.** Chạy truy vấn trước khi đặt hạn mức chi tiêu · dùng chọn mọi cột để xem thử dữ liệu · tìm cách tạo chỉ mục theo thói quen từ hệ quan hệ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Năm ước lượng khớp con số chế độ chạy thử, và quan hệ giữa lưu trữ cột với chi phí được giải thích đúng.

### Lesson 160 · Bytes scanned - the one number that decides cost `TH`
**Prerequisites.** Lesson 159

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Chi phí ở mô hình theo lượng quét tỉ lệ thẳng với byte quét, nên tối ưu ở đây là bài toán giảm byte chứ không phải giảm thời gian, và hai mục tiêu đó không luôn cùng hướng. Bốn đòn bẩy theo thứ tự hiệu quả: chọn ít cột, lọc trên cột phân vùng, lọc trên cột phân cụm, và giới hạn dữ liệu trước khi kết. Điều không giảm byte quét dù trông như giảm: mệnh đề giới hạn số dòng trả về không giảm byte quét vì dữ liệu vẫn phải đọc, một hiểu nhầm rất phổ biến và tốn tiền. Bộ đệm kết quả truy vấn cho truy vấn giống hệt trong khoảng thời gian, miễn phí nhưng vô hiệu khi truy vấn có hàm không tất định. Bảng tạm và bảng trung gian: viết kết quả ra bảng rồi dùng lại rẻ hơn tính lại nhiều lần. Xem byte quét thật sau khi chạy và so với ước lượng. Theo dõi chi phí theo người dùng và theo truy vấn bằng khung nhìn siêu dữ liệu.

**Outcome.** Giảm byte quét của một bộ năm truy vấn bằng bốn đòn bẩy, và chứng minh mệnh đề giới hạn số dòng không giảm byte quét.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí đếm được bằng đơn vị byte. Đạt khi tổng byte quét của năm truy vấn giảm ít nhất 60%, và khi thực nghiệm cho thấy thêm mệnh đề giới hạn không đổi byte quét. Giảm thời gian mà không giảm byte thì không tính.

**Lab.** Ghi byte quét nền cho năm truy vấn. Áp bốn đòn bẩy từng cái một, đo sau mỗi bước. Thêm mệnh đề giới hạn 10 dòng vào một truy vấn quét 50 ghi ga byte và so byte quét trước sau. Chạy lại một truy vấn giống hệt và quan sát bộ đệm kết quả, rồi thêm hàm thời gian hiện tại và quan sát nó mất hiệu lực.

**Pitfalls.** Dùng mệnh đề giới hạn để giảm chi phí · tối ưu thời gian mà không nhìn byte · lặp lại một truy vấn nặng nhiều lần thay vì ghi ra bảng trung gian.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tổng byte quét giảm ít nhất 60%, và thực nghiệm cho thấy mệnh đề giới hạn không đổi byte quét.

### Lesson 161 · Partitioning and clustering - the replacement for indexes `TH`
**Prerequisites.** Lesson 160

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phân vùng chia bảng theo một cột thời gian hoặc số nguyên, và lọc trên cột đó cho phép bỏ qua cả phân vùng, cùng cơ chế cắt tỉa ở lesson 115. Điều kiện cắt tỉa hoạt động giống hệt ở đó: bộ lọc phải trên chính cột phân vùng và không bọc hàm, nối lại lesson 96. Phân cụm sắp dữ liệu trong mỗi phân vùng theo tối đa bốn cột, cho phép bỏ qua khối dữ liệu không liên quan; nó không phải chỉ mục vì không có cấu trúc tra cứu riêng, nó chỉ là thứ tự vật lý. Thứ tự cột phân cụm quan trọng như thứ tự cột chỉ mục phức hợp ở lesson 111. Hiệu quả phân cụm giảm dần khi dữ liệu mới được thêm vào và tự phục hồi bằng tiến trình nền. Yêu cầu bắt buộc lọc phân vùng để chặn truy vấn quét cả bảng. Hết hạn phân vùng để tự xoá dữ liệu cũ. Chi phí thiết kế sai: phân vùng theo cột bản số cao tạo quá nhiều phân vùng nhỏ, nối lại lesson 15.

**Outcome.** Thiết kế phân vùng và phân cụm cho một bảng và bộ truy vấn cho trước, và chứng minh cắt tỉa hoạt động bằng byte quét.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn cột và thứ tự có đánh đổi giữa các truy vấn khác nhau. Đạt khi byte quét của bộ truy vấn giảm ít nhất 70% so với bảng không phân vùng, và khi người học nêu được truy vấn nào bị thiệt vì lựa chọn này cùng lý do.

**Lab.** Nạp 100 triệu dòng sự kiện vào ba bảng: không phân vùng, phân vùng theo ngày, và phân vùng cộng phân cụm ba cột. Chạy bộ sáu truy vấn trên cả ba, ghi byte quét. Viết một truy vấn bọc hàm quanh cột phân vùng và quan sát cắt tỉa mất hiệu lực. Bật yêu cầu bắt buộc lọc phân vùng và thử truy vấn thiếu bộ lọc.

**Pitfalls.** Phân vùng theo cột bản số cao · đặt cột phân cụm theo thứ tự tuỳ ý · bọc hàm quanh cột phân vùng trong bộ lọc.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Byte quét giảm ít nhất 70% so với bảng không phân vùng, và truy vấn bị thiệt được nêu kèm lý do.

### Lesson 162 · Reading the query plan - stages, slots and shuffle `TH`
**Prerequisites.** Lesson 161

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Kế hoạch thực thi trình bày theo giai đoạn chứ không theo cây toán tử như lesson 113, vì thực thi phân tán theo từng đợt. Mỗi giai đoạn có số bản ghi vào ra, thời gian chờ, thời gian đọc, thời gian tính, và thời gian ghi; phân bố bốn con số này chỉ ra nút cổ chai nằm ở đâu. Xáo trộn dữ liệu giữa các giai đoạn là thao tác đắt nhất, cùng kết luận với lesson 48, và nó xuất hiện khi kết hoặc gộp nhóm trên cột không phân cụm. Lệch dữ liệu hiện ra ở chênh lệch giữa thời gian công nhân chậm nhất và trung bình trong một giai đoạn, và đây là cách phát hiện trực tiếp nhất. Đơn vị tính toán và hàng đợi khi hết đơn vị. Kết phát tán khi một bảng đủ nhỏ, tương tự lesson 44. Ba dấu hiệu trong kế hoạch cần nhận ra ngay: giai đoạn lặp lại nhiều lần, một giai đoạn chiếm phần lớn thời gian, và tỉ lệ bản ghi ra trên vào tăng vọt.

**Outcome.** Đọc kế hoạch theo giai đoạn và định vị nút cổ chai, phân biệt được lệch dữ liệu với thiếu đơn vị tính toán.

**Đánh giá.** Tầng *phân tích*. Objective đòi phân biệt hai nguyên nhân có cùng triệu chứng là truy vấn chậm. Kiểm bằng ba truy vấn: một lệch khoá kết, một xáo trộn lớn, một chờ đơn vị tính toán. Đạt khi định vị đúng cả ba và dẫn được con số từ kế hoạch cho từng ca.

**Lab.** Chạy ba truy vấn dựng sẵn. Với mỗi cái, lập bảng bốn con số cho từng giai đoạn. Định vị nút cổ chai. Với ca lệch, so thời gian công nhân chậm nhất và trung bình. Sửa ca lệch bằng thêm hậu tố ngẫu nhiên vào khoá kết và đo lại.

**Pitfalls.** Kết luận thiếu tài nguyên khi thật ra lệch dữ liệu · đọc tổng thời gian mà không xem phân bố theo giai đoạn · bỏ qua xáo trộn khi tối ưu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Định vị đúng nút cổ chai cho cả ba truy vấn, mỗi ca dẫn được con số từ kế hoạch.

### Lesson 163 · Materialized views, scheduled queries and precomputation `TH`
**Prerequisites.** Lesson 162

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba cách tính trước và điều kiện chọn từng cái. Khung nhìn thường không lưu gì nên không giảm byte quét, chỉ giảm lặp mã. Khung nhìn vật chất hoá lưu kết quả và tự cập nhật tăng dần khi bảng nguồn đổi, nên truy vấn đọc nó quét ít byte hơn nhiều; đổi lại có ràng buộc về loại phép gộp dùng được và chi phí lưu trữ cộng chi phí cập nhật. Truy vấn theo lịch ghi kết quả ra bảng, linh hoạt hơn nhưng phải tự quản lý tính mới. Tự động dùng khung nhìn vật chất hoá: bộ tối ưu hoá có thể viết lại truy vấn trên bảng gốc thành truy vấn trên khung nhìn, nên người dùng cuối hưởng lợi mà không phải đổi mã. Phép tính lợi ích ròng: byte tiết kiệm mỗi lần đọc nhân số lần đọc, trừ chi phí lưu và chi phí cập nhật; cùng khung tính với lesson 158. Bảng tổng hợp thủ công khi ràng buộc của khung nhìn vật chất hoá không cho phép.

**Outcome.** Chọn giữa ba cách tính trước cho ba tình huống có tần suất đọc khác nhau, và chứng minh lựa chọn bằng phép tính lợi ích ròng.

**Đánh giá.** Tầng *đánh giá*. Objective đòi quyết định dựa trên một phép tính có hai vế. Đạt khi ba lựa chọn đều có phép tính lợi ích ròng bằng số, và khi ít nhất một tình huống kết luận là không nên tính trước vì tần suất đọc quá thấp.

**Lab.** Ba tình huống: bảng đọc 500 lần mỗi ngày, 5 lần mỗi ngày, và 1 lần mỗi tuần. Với mỗi cái, đo byte quét của truy vấn gốc, tạo khung nhìn vật chất hoá, đo byte quét mới và chi phí cập nhật. Tính lợi ích ròng. Kiểm xem truy vấn trên bảng gốc có tự được viết lại không.

**Pitfalls.** Tạo khung nhìn vật chất hoá cho truy vấn ít đọc · quên tính chi phí cập nhật khi nguồn đổi liên tục · dùng khung nhìn thường rồi tưởng nó giảm chi phí.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba lựa chọn đều có phép tính lợi ích ròng bằng số, và ít nhất một tình huống kết luận không nên tính trước.

### Lesson 164 · Loading data - batch, streaming and the cost of each `TH`
**Prerequisites.** Lesson 163

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bốn đường nạp dữ liệu và đặc tính khác nhau: nạp theo lô từ tệp thường miễn phí nhưng có độ trễ, chèn theo luồng tính tiền và có độ trễ thấp, truyền dữ liệu liên tục từ nguồn, và truy vấn trực tiếp trên tệp ngoài không cần nạp. Chọn đường nào là quyết định về độ trễ đổi lấy chi phí, và phần lớn tải phân tích không cần độ trễ thấp nên nạp theo lô là mặc định đúng. Bộ đệm luồng và khoảng thời gian dữ liệu vừa chèn chưa sửa hoặc xoá được, một ràng buộc hay gây bất ngờ. Bất biến khi chạy lại ở đây: chèn theo luồng không có khoá duy nhất nên phải khử trùng ở tầng sau hoặc dùng mã định danh chèn, nối lại lesson 106. Bảng ngoài trỏ vào tệp trên lưu trữ đối tượng và khi nào nó hợp: dữ liệu ít truy vấn, hoặc dùng chung với công cụ khác. Định dạng tệp và ảnh hưởng lên tốc độ nạp, nối lại lesson 70.

**Outcome.** Chọn đường nạp cho ba yêu cầu độ trễ khác nhau, và đo chi phí cùng độ trễ thật của từng đường.

**Đánh giá.** Tầng *đánh giá*. Objective đòi cân độ trễ với chi phí. Đạt khi ba đường nạp đều có số đo độ trễ và chi phí, và khi lựa chọn cho từng yêu cầu dẫn được về hai con số đó chứ không về thói quen.

**Lab.** Nạp cùng 10 triệu bản ghi bằng ba đường: theo lô từ tệp, chèn theo luồng, và bảng ngoài. Đo thời gian tới khi truy vấn được và chi phí từng cách. Thử sửa một dòng vừa chèn theo luồng và quan sát ràng buộc. Chèn trùng có chủ đích và thiết kế cách khử trùng.

**Pitfalls.** Dùng chèn theo luồng cho tải phân tích hằng ngày · giả định dữ liệu vừa chèn theo luồng sửa được ngay · nạp tệp không nén khi mạng là nút cổ chai.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba đường nạp đều có số đo độ trễ và chi phí, và lựa chọn dẫn được về hai con số đó.

### Lesson 165 · Access control, data governance and cost attribution `TH`
**Prerequisites.** Lesson 164

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phân quyền theo bốn tầng và nguyên tắc đặc quyền tối thiểu, nối lại lesson 23. Phân quyền ở mức tập dữ liệu, mức bảng, mức cột, và mức hàng; hai mức sau cho phép một bảng phục vụ nhiều nhóm với phạm vi khác nhau. Tài khoản dịch vụ cho pipeline và nguyên tắc mỗi pipeline một tài khoản riêng để truy được ai làm gì. Khung nhìn được uỷ quyền để cho truy cập kết quả mà không cho truy cập bảng gốc, mẫu thay thế cho việc sao chép dữ liệu. Gắn thẻ dữ liệu nhạy cảm và che ở mức cột. Nhật ký kiểm toán ghi mọi truy vấn kèm người chạy và byte quét, nên nó vừa là công cụ bảo mật vừa là công cụ phân bổ chi phí. Gắn nhãn cho truy vấn và bảng để quy chi phí về nhóm. Hạn mức chi tiêu ở nhiều mức và cảnh báo ngân sách, thứ đáng ra phải đặt từ lesson 159.

**Outcome.** Thiết lập phân quyền cho ba nhóm người dùng có phạm vi khác nhau, và quy được chi phí truy vấn về từng nhóm bằng nhật ký kiểm toán.

**Đánh giá.** Tầng *áp dụng*. Objective có hai sản phẩm kiểm được. Đạt khi ba nhóm chỉ truy cập được đúng phạm vi của mình, xác nhận bằng thử truy cập ngoài phạm vi và bị từ chối, và khi bảng chi phí theo nhóm tổng lại bằng tổng chi phí thật.

**Lab.** Ba nhóm: phân tích được xem mọi cột trừ cột định danh cá nhân, vận hành chỉ xem dữ liệu 7 ngày gần nhất, và đối tác chỉ xem một tập hàng. Cài phân quyền theo cột, theo hàng, và khung nhìn được uỷ quyền. Thử truy cập ngoài phạm vi cho từng nhóm. Gắn nhãn truy vấn và lập bảng chi phí theo nhóm từ nhật ký kiểm toán.

**Pitfalls.** Cấp quyền ở mức dự án cho tiện · dùng một tài khoản dịch vụ cho mọi pipeline · sao chép dữ liệu ra bảng riêng thay vì dùng khung nhìn được uỷ quyền.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba nhóm bị từ chối đúng khi truy cập ngoài phạm vi, và bảng chi phí theo nhóm tổng bằng tổng chi phí thật.

### Lesson 166 · Reducing the cost of a query set by seventy percent `TH`
**Prerequisites.** Lesson 165

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Không có cơ chế mới. Bài gộp module: nhận một bộ truy vấn tốn kém và giảm chi phí bằng mọi đòn bẩy đã học, theo thứ tự chi phí thực hiện tăng dần. Trước tiên là thứ không đổi dữ liệu: bớt cột, thêm bộ lọc, dùng lại bộ đệm kết quả. Sau đó là thứ đổi bố trí: phân vùng và phân cụm ở lesson 161. Cuối cùng là tính trước ở lesson 163. Nguyên tắc của bài: mỗi thay đổi đo riêng và ghi lại, vì gộp nhiều thay đổi rồi đo một lần thì không biết cái nào có tác dụng, nối lại lesson 17. Kiểm chứng bắt buộc: kết quả truy vấn sau khi tối ưu phải khớp từng dòng với kết quả gốc, vì giảm chi phí bằng cách vô tình đọc thiếu dữ liệu là sai chứ không phải tối ưu. Báo cáo cuối là một trong bảy đầu vào của M18.

**Outcome.** Giảm tổng byte quét của một bộ truy vấn ít nhất 70% mà kết quả khớp từng dòng với bản gốc, và ghi được đóng góp riêng của từng thay đổi.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chuỗi quyết định có đo từng bước cùng một ràng buộc đúng đắn tuyệt đối. Đạt khi tổng byte quét giảm ít nhất 70%, khi mọi kết quả khớp từng dòng với bản gốc, và khi bảng đóng góp cho thấy riêng từng thay đổi. Giảm đủ mà kết quả lệch một dòng là không đạt.

**Lab.** Nhận bộ 10 truy vấn trên bảng 500 ghi ga byte. Ghi byte quét nền và kết quả gốc. Áp từng thay đổi một, đo sau mỗi bước, đối chiếu kết quả từng dòng. Lập bảng đóng góp. Kiểm hạn mức chi tiêu không bị vượt trong suốt quá trình.

**Pitfalls.** Gộp nhiều thay đổi rồi đo một lần · giảm chi phí bằng cách thu hẹp phạm vi dữ liệu mà không báo · quên đối chiếu kết quả sau khi đổi bố trí bảng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tổng byte quét giảm ít nhất 70%, mọi kết quả khớp từng dòng với bản gốc, và bảng đóng góp tách riêng từng thay đổi.

# MODULE 16 · CLICKHOUSE

**Lessons 167–174 · 16 giờ**

| | |
|---|---|
| **Objective cấp module** | Chọn khoá sắp xếp và khoá phân vùng cho một tải sự kiện, và chẩn đoán truy vấn chậm bằng số phần dữ liệu đọc |
| **Tiền đề** | M11 |
| **Exit criterion** | Nạp 200 triệu sự kiện, đạt độ trễ truy vấn dưới ngưỡng đặt trước, và sửa được một truy vấn đọc quá nhiều phần dữ liệu |
| **Kỹ năng SFIA** | `DBAD` mức 3 |
| **Chế độ hỏng** | Chọn khoá sắp xếp theo thói quen khoá chính của hệ quan hệ, rồi mọi truy vấn quét toàn bảng mà vẫn tưởng nhanh vì máy khoẻ |

Mức `B`. ClickHouse tối ưu cho một tải rất hẹp là phân tích trên dữ liệu chỉ chèn thêm, và nó đánh đổi gần như mọi thứ khác để đạt điều đó. Module bám hai quyết định thiết kế quyết định tất cả: khoá sắp xếp và khoá phân vùng. Bài cuối là chẩn đoán và sửa một truy vấn đọc thừa.

### Lesson 167 · MergeTree - parts, merges and the sorting key `LT`
**Prerequisites.** Module 16: M11

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Họ bảng chính lưu dữ liệu thành các phần đã sắp theo khoá sắp xếp, và tiến trình nền trộn các phần nhỏ thành phần lớn, cấu trúc cùng họ với cây trộn có cấu trúc nhật ký ở lesson 111. Mỗi lần chèn tạo một phần mới, nên chèn từng dòng tạo hàng triệu phần và giết hệ thống; quy tắc là chèn theo lô lớn, và đây là ràng buộc quan trọng nhất khi thiết kế pipeline nạp. Khoá sắp xếp quyết định thứ tự vật lý trong mỗi phần và là thứ duy nhất gần giống chỉ mục; chỉ mục thưa lưu một mục cho mỗi khối vài nghìn dòng thay vì mỗi dòng, nên nó rất nhỏ nhưng chỉ định vị được tới khối. Hệ quả: lọc trên tiền tố của khoá sắp xếp thì bỏ qua được phần lớn khối, lọc trên cột không nằm trong khoá thì phải đọc hết. Khoá chính ở đây là tiền tố của khoá sắp xếp chứ không ràng buộc duy nhất, khác hẳn nghĩa ở hệ quan hệ.

**Outcome.** Giải thích vì sao chèn từng dòng làm hệ thống sụp, và dự đoán truy vấn nào bỏ qua được khối từ một khoá sắp xếp cho trước.

**Đánh giá.** Tầng *phân tích*. Objective đòi suy từ cấu trúc lưu trữ ra hành vi truy vấn. Đạt khi dự đoán đúng ít nhất bốn trên năm truy vấn về việc có bỏ qua khối được không, xác nhận bằng số khối đọc thật, và khi thực nghiệm chèn từng dòng cho thấy số phần tăng vọt.

**Lab.** Tạo bảng với khoá sắp xếp ba cột. Dự đoán năm truy vấn có bỏ qua khối được không. Chạy và đọc số khối đọc thật. Chèn 100.000 dòng từng dòng một và đếm số phần, so với chèn theo lô 10.000 dòng. Quan sát tiến trình trộn chạy.

**Pitfalls.** Chèn từng dòng như với hệ quan hệ · tưởng khoá chính ở đây ràng buộc duy nhất · lọc trên cột không nằm trong tiền tố khoá sắp xếp rồi tưởng có chỉ mục.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Dự đoán đúng ít nhất bốn trên năm truy vấn xác nhận bằng số khối đọc, và thực nghiệm chèn từng dòng cho thấy số phần tăng vọt.

### Lesson 168 · Choosing the sorting key and the partition key `TH`
**Prerequisites.** Lesson 167

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hai khoá phục vụ hai mục đích khác nhau và hay bị gộp. Khoá phân vùng chia dữ liệu thành nhóm quản lý được, thường theo tháng, và mục đích chính là vận hành: xoá dữ liệu cũ bằng thao tác siêu dữ liệu và giới hạn phạm vi trộn. Phân vùng theo ngày cho bảng giữ nhiều năm tạo quá nhiều phân vùng và làm chậm mọi thứ, một lỗi phổ biến. Khoá sắp xếp quyết định hiệu năng truy vấn, và quy tắc chọn thứ tự cột: cột lọc bằng và bản số thấp đặt trước, cột bản số cao đặt sau, ngược với trực giác từ chỉ mục quan hệ ở lesson 111. Lý do: bản số thấp trước cho phép bỏ qua nhiều khối hơn ở bước đầu. Cột thời gian thường đặt cuối. Chỉ mục nhảy cho cột không nằm trong khoá sắp xếp, cho phép bỏ qua khối dựa trên thống kê nhỏ nhất lớn nhất, ý tưởng giống chỉ mục phạm vi khối ở lesson 127. Đổi khoá sắp xếp sau khi có dữ liệu gần như không làm được, nên đây là quyết định phải đúng từ đầu.

**Outcome.** Chọn khoá sắp xếp và khoá phân vùng cho một tải sự kiện cho trước, và chứng minh lựa chọn bằng số khối đọc của bộ truy vấn thường gặp.

**Đánh giá.** Tầng *đánh giá*. Objective đòi quyết định khó đảo ngược dựa trên mẫu truy vấn. Đạt khi so được ít nhất ba phương án khoá sắp xếp trên cùng bộ truy vấn với số khối đọc, và khi lựa chọn cuối nêu được truy vấn nào bị thiệt cùng lý do.

**Lab.** Nạp 50 triệu sự kiện vào ba bảng có ba khoá sắp xếp khác nhau, cùng khoá phân vùng theo tháng. Chạy bộ sáu truy vấn trên cả ba, ghi số khối đọc và độ trễ. Thử phân vùng theo ngày và đếm số phân vùng sau một năm dữ liệu. Thêm chỉ mục nhảy cho một cột ngoài khoá và đo lại.

**Pitfalls.** Đặt cột bản số cao đầu khoá sắp xếp · phân vùng theo ngày cho dữ liệu nhiều năm · coi khoá phân vùng là công cụ tăng tốc truy vấn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba phương án khoá sắp xếp có số khối đọc so được, và lựa chọn cuối nêu truy vấn bị thiệt kèm lý do.

### Lesson 169 · Vectorized execution and why it is fast `LT`
**Prerequisites.** Lesson 168

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Thực thi theo khối cột thay vì theo dòng: mỗi toán tử nhận một khối vài nghìn giá trị của một cột và xử lý cả khối, nên chi phí gọi hàm chia đều cho nhiều giá trị và dữ liệu nằm liên tục trong bộ nhớ. Đây là chỗ lesson 11 về dòng bộ nhớ đệm và lesson 10 về tập lệnh đơn dòng nhiều dữ liệu cho ra hiệu quả đo được. Nén theo cột và các thuật toán chuyên cho từng kiểu dữ liệu: cột có ít giá trị phân biệt nén rất tốt, cột thời gian tăng dần nén bằng hiệu số. Chọn kiểu dữ liệu hẹp nhất đủ dùng là đòn bẩy trực tiếp lên cả dung lượng lẫn tốc độ, khác với hệ quan hệ nơi khác biệt nhỏ hơn. Kiểu từ điển cho cột chuỗi lặp nhiều. Giải nén tốn bộ xử lý nên có đánh đổi giữa tỉ lệ nén với tốc độ đọc, và thuật toán nén chọn được theo cột. Vì sao mô hình này tệ cho truy vấn lấy một dòng theo khoá.

**Outcome.** Giải thích vì sao thực thi theo khối cột nhanh hơn theo dòng, và chứng minh ảnh hưởng của lựa chọn kiểu dữ liệu lên dung lượng và tốc độ.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết nối cơ chế với số đo. Đạt khi giải thích đúng ba yếu tố làm nó nhanh, và khi thực nghiệm cho thấy đổi kiểu dữ liệu hẹp hơn giảm cả dung lượng lẫn thời gian truy vấn đo được.

**Lab.** Tạo hai bảng cùng dữ liệu nhưng khác kiểu: một dùng kiểu rộng mặc định, một dùng kiểu hẹp nhất đủ và kiểu từ điển cho cột lặp. So dung lượng sau nén và thời gian truy vấn gộp. Thử ba thuật toán nén cho một cột và đo tỉ lệ nén với thời gian đọc. Chạy một truy vấn lấy một dòng theo khoá và so với PostgreSQL.

**Pitfalls.** Dùng kiểu rộng mặc định cho mọi cột · chọn nén mạnh nhất mà không đo chi phí bộ xử lý · dùng ClickHouse cho tải lấy một dòng theo khoá.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba yếu tố được giải thích đúng, và thực nghiệm cho thấy kiểu hẹp hơn giảm cả dung lượng lẫn thời gian.

### Lesson 170 · Materialized views and incremental aggregation `TH`
**Prerequisites.** Lesson 169

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Khung nhìn vật chất hoá ở đây khác hẳn nghĩa ở hệ quan hệ: nó là một trình kích hoạt chạy khi chèn, tính trên khối dữ liệu vừa chèn rồi ghi kết quả vào bảng đích. Hệ quả quan trọng: nó chỉ thấy dữ liệu mới, không thấy dữ liệu đã có, nên tạo khung nhìn trên bảng đã đầy dữ liệu sẽ không có gì, và phải nạp lại lịch sử bằng tay. Hệ quả thứ hai: nó không thấy thao tác xoá và cập nhật. Họ bảng gộp trộn các dòng cùng khoá khi trộn, cho phép gộp tăng dần mà không cần đọc lại toàn bộ; kết quả chỉ đúng sau khi trộn xong nên truy vấn phải dùng phép gộp cuối để gộp nốt phần chưa trộn, và quên điều này là nguồn số sai âm thầm. Kiểu trạng thái gộp cho các phép gộp phức tạp như đếm phân biệt xấp xỉ, nối lại lesson 47. Chuỗi nhiều khung nhìn vật chất hoá và rủi ro khó lần vết.

**Outcome.** Dựng khung nhìn vật chất hoá gộp tăng dần, và chứng minh kết quả đúng cả trước và sau khi tiến trình trộn chạy.

**Đánh giá.** Tầng *áp dụng*. Objective có bẫy đúng đắn cụ thể là đọc trước khi trộn xong. Đạt khi truy vấn trên bảng đích cho kết quả khớp phép gộp trực tiếp trên bảng nguồn ở cả hai thời điểm, ngay sau khi chèn và sau khi trộn. Đúng sau khi trộn mà sai trước đó là không đạt.

**Lab.** Tạo bảng sự kiện và khung nhìn vật chất hoá gộp theo giờ vào bảng họ gộp. Chèn 10 triệu sự kiện. Truy vấn bảng đích ngay, so với gộp trực tiếp trên nguồn. Ép trộn rồi truy vấn lại. Sửa truy vấn bằng phép gộp cuối. Tạo một khung nhìn trên bảng đã có dữ liệu và quan sát nó trống.

**Pitfalls.** Truy vấn bảng họ gộp mà không dùng phép gộp cuối · tạo khung nhìn vật chất hoá rồi tưởng nó xử lý cả dữ liệu cũ · trông chờ khung nhìn phản ánh thao tác xoá.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Kết quả khớp phép gộp trực tiếp ở cả hai thời điểm, trước và sau khi trộn.

### Lesson 171 · TTL, data lifecycle and mutations `TH`
**Prerequisites.** Lesson 170

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Thời gian sống khai báo ở mức bảng hoặc mức cột, và ba hành động khi hết hạn: xoá dòng, chuyển sang ổ đĩa rẻ hơn, hoặc gộp lại ở mức thô hơn. Hành động thứ ba là mẫu giữ dữ liệu chi tiết ngắn hạn và dữ liệu tổng hợp dài hạn, thay thế cho việc viết pipeline dọn dẹp. Thời gian sống thực thi khi trộn chứ không theo lịch chính xác, nên dữ liệu quá hạn còn tồn tại một thời gian, cùng đặc tính với lesson 153. Cập nhật và xoá là thao tác nặng vì chúng viết lại cả phần dữ liệu, nên chúng được gọi là biến đổi và chạy bất đồng bộ; đây là lý do ClickHouse không hợp cho tải sửa dữ liệu thường xuyên. Theo dõi biến đổi đang chạy và huỷ khi cần. Xoá theo phân vùng là thao tác siêu dữ liệu nên nhanh hơn xoá theo điều kiện nhiều bậc, cùng kết luận với lesson 130. Họ bảng thay thế để cập nhật bằng cách chèn phiên bản mới.

**Outcome.** Thiết kế vòng đời dữ liệu ba tầng bằng thời gian sống, và chứng minh xoá theo phân vùng nhanh hơn xoá theo điều kiện nhiều bậc.

**Đánh giá.** Tầng *áp dụng*. Objective có hai tiêu chí đo được. Đạt khi ba tầng vòng đời hoạt động đúng sau khi ép trộn, và khi chênh lệch thời gian giữa xoá theo phân vùng với xoá theo điều kiện đạt ít nhất một bậc độ lớn.

**Lab.** Bảng 100 triệu sự kiện. Khai báo thời gian sống ba tầng: chi tiết 30 ngày, gộp theo giờ tới 1 năm, xoá sau đó. Ép trộn và kiểm từng tầng. So thời gian xoá một tháng dữ liệu bằng xoá phân vùng với bằng xoá theo điều kiện. Chạy một biến đổi cập nhật và theo dõi tiến độ.

**Pitfalls.** Trông chờ thời gian sống chạy đúng giờ · dùng cập nhật và xoá thường xuyên như với hệ quan hệ · xoá dữ liệu cũ bằng điều kiện thay vì bằng phân vùng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba tầng vòng đời hoạt động đúng sau khi ép trộn, và xoá theo phân vùng nhanh hơn ít nhất một bậc.

### Lesson 172 · Ingestion at scale - batching, buffering and backpressure `TH`
**Prerequisites.** Lesson 171

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ràng buộc chèn theo lô từ lesson 167 quyết định thiết kế cả pipeline nạp. Ba cách thoả ràng buộc đó: gom lô ở tầng ứng dụng, dùng bảng đệm nhận chèn nhỏ rồi tự xả theo lô, và nạp từ hệ thống luồng bằng bộ máy tích hợp. Cách thứ hai tiện nhưng dữ liệu trong bảng đệm mất khi tiến trình chết, nên nó không hợp dữ liệu không được mất. Kích thước lô và tần suất là hai tham số đánh đổi giữa độ trễ với số phần tạo ra, chọn bằng thực nghiệm giống lesson 71. Chèn bất đồng bộ và xác nhận trả về trước khi dữ liệu xuống đĩa. Chèn trùng và tính bất biến: có cơ chế loại bỏ khối chèn trùng dựa trên tổng kiểm tra trong một cửa sổ, nên chèn lại cùng một lô là an toàn, nhưng chỉ trong cửa sổ đó. Áp lực ngược khi tiến trình trộn không đuổi kịp tốc độ chèn: triệu chứng là số phần tăng dần và cuối cùng hệ thống từ chối chèn, nối lại lesson 57.

**Outcome.** Thiết kế đường nạp thoả ràng buộc chèn theo lô, và tái hiện được tình huống trộn không đuổi kịp rồi xử lý.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí kiểm bằng thực nghiệm ở hai chiều. Đạt khi đường nạp giữ số phần ổn định qua 30 phút chèn liên tục, và khi tái hiện được ca hệ thống từ chối chèn do quá nhiều phần rồi khôi phục bằng đúng biện pháp.

**Lab.** Dựng đường nạp gom lô ở tầng ứng dụng, chạy 30 phút, theo dõi số phần theo thời gian. Thử ba kích thước lô và so độ trễ với số phần. Ép tạo quá nhiều phần bằng chèn lô nhỏ tần suất cao, quan sát hệ thống từ chối. Chèn lại cùng một lô hai lần và kiểm số dòng.

**Pitfalls.** Chèn từng dòng qua bảng đệm cho dữ liệu không được mất · tăng tần suất chèn để giảm độ trễ mà không theo dõi số phần · dựa vào cơ chế loại trùng ngoài cửa sổ của nó.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Số phần ổn định qua 30 phút chèn, và ca từ chối chèn được tái hiện rồi khôi phục bằng đúng biện pháp.

### Lesson 173 · Distributed tables, replication and the operational surface `LT`
**Prerequisites.** Lesson 172

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Nhân bản ở mức bảng chứ không mức máy chủ, và nó dùng một dịch vụ điều phối bên ngoài để giữ đồng thuận về danh sách phần dữ liệu. Nhân bản bất đồng bộ và cửa sổ mất dữ liệu, cùng mô hình lesson 120. Bảng phân tán là một lớp định tuyến không chứa dữ liệu, đứng trước các bảng cục bộ trên nhiều cụm; truy vấn qua nó được gửi tới mọi cụm rồi gộp kết quả. Khoá phân mảnh quyết định dữ liệu về cụm nào, và gộp nhóm trên cột không phải khoá phân mảnh cần gộp hai bước, nối lại lesson 48. Ghi qua bảng phân tán là bất đồng bộ và có thể mất, nên ghi thẳng vào bảng cục bộ an toàn hơn, một chi tiết vận hành quan trọng. Kết phân tán và chi phí của nó, cùng lý do phát tán bảng chiều nhỏ tới mọi cụm là mẫu phổ biến. Khi nào chưa cần phân tán: một máy hiện đại xử lý được tải lớn hơn nhiều người tưởng.

**Outcome.** Nêu ba khác biệt giữa bảng phân tán và bảng cục bộ ảnh hưởng tới tính đúng đắn, và chỉ ra khi nào một cụm một máy là đủ.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết vì dựng cụm nhiều máy vượt phạm vi mức `B`. Đạt khi ba khác biệt nêu ra đều liên quan tới đúng đắn chứ không chỉ hiệu năng, và khi ngưỡng cần phân tán được phát biểu bằng số dựa trên đo đạc ở lesson 168.

**Lab.** Dựng hai nút với một bảng nhân bản và một bảng phân tán. Ghi qua bảng phân tán rồi giết tiến trình, đếm dòng mất. Ghi thẳng vào bảng cục bộ và so. Chạy gộp nhóm trên cột không phải khoá phân mảnh và đọc kế hoạch. Từ số đo lesson 168, ước lượng ngưỡng dữ liệu cần phân tán.

**Pitfalls.** Ghi qua bảng phân tán cho dữ liệu không được mất · phân tán khi một máy còn thừa sức · gộp nhóm trên cột không phải khoá phân mảnh mà không biết có hai bước.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba khác biệt đều liên quan tới đúng đắn, và ngưỡng cần phân tán phát biểu được bằng số.

### Lesson 174 · Diagnosing a query that reads too many parts `TH`
**Prerequisites.** Lesson 173

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Không có cơ chế mới. Bài gộp module: chẩn đoán và sửa truy vấn chậm theo một quy trình bốn bước. Bước một đọc số phần và số khối truy vấn đã đọc, con số quan trọng nhất và tương đương với byte quét ở lesson 160. Bước hai xác định nguyên nhân trong bốn nguyên nhân: bộ lọc không chạm tiền tố khoá sắp xếp, hàm bọc quanh cột khoá, quá nhiều phần do trộn không đuổi kịp ở lesson 172, hoặc phân vùng quá nhỏ và quá nhiều. Bước ba sửa đúng nguyên nhân. Bước bốn đo lại và đối chiếu kết quả từng dòng. Nhật ký truy vấn ghi số phần đọc, byte đọc, bộ nhớ dùng và thời gian cho mọi truy vấn, nên nó là nguồn chẩn đoán chính. Giới hạn bộ nhớ mỗi truy vấn và hành vi khi vượt. Báo cáo cuối là một trong bảy đầu vào của M18.

**Outcome.** Chẩn đoán bốn truy vấn chậm về đúng nguyên nhân bằng số phần đọc, sửa, và chứng minh kết quả không đổi.

**Đánh giá.** Tầng *phân tích*. Objective là chẩn đoán phân biệt bốn nguyên nhân cùng triệu chứng. Đạt khi định vị đúng ít nhất ba trên bốn, mỗi lần dẫn số phần đọc từ nhật ký truy vấn, và khi kết quả sau sửa khớp từng dòng với trước sửa.

**Lab.** Nhận bốn truy vấn chậm trên bảng 200 triệu dòng, mỗi truy vấn chậm vì một nguyên nhân khác nhau. Với mỗi cái, đọc nhật ký truy vấn lấy số phần và số khối. Định vị, sửa, đo lại, đối chiếu kết quả. Chạy một truy vấn vượt giới hạn bộ nhớ và quan sát.

**Pitfalls.** Kết luận máy yếu khi số phần đọc mới là nguyên nhân · sửa bằng thêm tài nguyên · quên đối chiếu kết quả sau khi sửa truy vấn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Định vị đúng ít nhất ba trên bốn nguyên nhân có số phần đọc làm bằng chứng, và kết quả sau sửa khớp từng dòng.

# MODULE 17 · ELASTICSEARCH

**Lessons 175–182 · 16 giờ**

| | |
|---|---|
| **Objective cấp module** | Thiết kế ánh xạ và bộ phân tích cho một tải tìm kiếm, và chẩn đoán được ba sự cố vận hành đặc trưng: quá nhiều mảnh, áp lực bộ nhớ, và độ trễ làm mới |
| **Tiền đề** | M11 |
| **Exit criterion** | Tìm kiếm nhật ký tiếng Việt cho kết quả đúng, đổi được ánh xạ bằng lập chỉ mục lại không ngừng phục vụ, và sửa được một cụm quá nhiều mảnh |
| **Kỹ năng SFIA** | `DBAD` mức 3 · `SYSP` mức 3 |
| **Chế độ hỏng** | Dùng Elasticsearch làm nguồn dữ liệu gốc hoặc làm kho phân tích chung, rồi gặp mất dữ liệu và chi phí bộ nhớ không kiểm soát |

Mức `B`. Elasticsearch giải một bài toán hẹp là tìm kiếm toàn văn và lọc trên dữ liệu bán cấu trúc, và mọi đặc tính vận hành của nó suy ra từ chỉ mục ngược cùng mô hình phân đoạn bất biến. Module bám hai thứ đó. Ba bài cuối là vận hành, vì đây là hệ mà sự cố vận hành hay gặp nhất trong bảy hệ.

### Lesson 175 · The inverted index and why search is a different problem `LT`
**Prerequisites.** Module 17: M11

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Chỉ mục ngược ánh xạ từ khoá tới danh sách tài liệu chứa nó, ngược với chỉ mục cây B ánh xạ khoá tới vị trí dòng, nối lại lesson 111. Hệ quả: tìm tài liệu chứa một từ là tra một lần rồi đọc danh sách, chi phí tỉ lệ số tài liệu khớp chứ không tỉ lệ kích thước tập. Đây là lý do tìm kiếm toàn văn trên hệ quan hệ bằng khớp mẫu có ký tự đại diện ở đầu luôn chậm, nối lại lesson 94. Từ điển từ khoá và danh sách vị trí, cùng dung lượng chúng chiếm. Chấm điểm liên quan và ba yếu tố của nó: tần suất từ trong tài liệu, độ hiếm của từ trong tập, và độ dài tài liệu. Hệ quả quan trọng cho công việc dữ liệu: kết quả có thứ tự theo điểm chứ không theo giá trị, nên nó trả lời câu hỏi cái nào liên quan nhất chứ không trả lời câu hỏi có bao nhiêu cái. Phân biệt ngữ cảnh truy vấn có chấm điểm với ngữ cảnh lọc không chấm điểm và được đệm.

**Outcome.** Giải thích vì sao chỉ mục ngược nhanh cho tìm kiếm mà chậm cho gộp nhóm, và phân biệt ngữ cảnh truy vấn với ngữ cảnh lọc bằng số đo.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết nối cấu trúc với hành vi. Đạt khi giải thích đúng hai chiều của chỉ mục ngược, và khi thực nghiệm cho thấy cùng một điều kiện đặt trong ngữ cảnh lọc nhanh hơn rõ rệt so với đặt trong ngữ cảnh truy vấn khi chạy lặp.

**Lab.** Nạp 5 triệu bản ghi nhật ký. Chạy một tìm kiếm toàn văn và so với khớp mẫu tương đương trên PostgreSQL. Chạy cùng một điều kiện lọc trong hai ngữ cảnh, mỗi cái 100 lần, so độ trễ. Chạy một phép gộp nhóm trên 5 triệu tài liệu và so với ClickHouse.

**Pitfalls.** Dùng Elasticsearch làm kho phân tích chung · đặt điều kiện lọc vào ngữ cảnh truy vấn nên mất bộ đệm · trông chờ thứ tự kết quả theo giá trị.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Hai chiều của chỉ mục ngược được giải thích đúng, và thực nghiệm cho thấy chênh lệch giữa hai ngữ cảnh.

### Lesson 176 · Analyzers, tokenizers and Vietnamese text `TH`
**Prerequisites.** Lesson 175

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bộ phân tích biến văn bản thành từ khoá và nó chạy ở hai thời điểm: lúc lập chỉ mục và lúc truy vấn. Hai lần phải dùng cùng một bộ phân tích, nếu không thì từ khoá sinh ra không khớp và tìm không ra, một lỗi âm thầm vì không có thông báo. Ba thành phần: bộ lọc ký tự, bộ tách từ, và bộ lọc từ khoá. Bộ tách từ theo khoảng trắng hợp tiếng Anh nhưng không hợp tiếng Việt vì tiếng Việt có từ ghép nhiều âm tiết, nên tách theo khoảng trắng cho ra âm tiết chứ không cho ra từ. Ba cách xử lý tiếng Việt và đánh đổi: giữ nguyên âm tiết rồi dựa vào truy vấn cụm từ, dùng ghép n âm tiết, hoặc dùng bộ tách từ tiếng Việt chuyên dụng. Chuẩn hoá dấu và chữ hoa chữ thường, nối lại lesson 8 về chuẩn hoá Unicode. Từ dừng và vì sao loại chúng có hại cho một số truy vấn. Kiểm bộ phân tích bằng giao diện phân tích thử trước khi lập chỉ mục.

**Outcome.** Thiết kế bộ phân tích cho nhật ký tiếng Việt và chứng minh nó tìm đúng bằng một tập kiểm chứng có đáp án.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí đối chứng bằng tập kiểm chứng. Đạt khi đạt ít nhất 90% độ chính xác trên 50 truy vấn có đáp án, và khi chứng minh được trường hợp dùng khác bộ phân tích ở hai thời điểm làm tìm không ra.

**Lab.** Dựng tập 50 truy vấn tiếng Việt có đáp án trên 1 triệu bản ghi. Thử ba cách xử lý tiếng Việt, đo độ chính xác từng cách. Dùng giao diện phân tích thử xem từ khoá sinh ra cho ba câu mẫu. Cố ý đặt bộ phân tích truy vấn khác bộ phân tích lập chỉ mục và quan sát kết quả rỗng.

**Pitfalls.** Tách tiếng Việt theo khoảng trắng rồi tìm cụm từ không ra · đổi bộ phân tích mà không lập chỉ mục lại · loại từ dừng rồi mất truy vấn cụm từ chứa chúng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đạt ít nhất 90% độ chính xác trên 50 truy vấn có đáp án, và chứng minh được ca lệch bộ phân tích.

### Lesson 177 · Mapping, dynamic mapping and field explosion `TH`
**Prerequisites.** Lesson 176

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ánh xạ khai báo kiểu của từng trường, và ánh xạ động tự suy kiểu từ tài liệu đầu tiên chứa trường đó. Ánh xạ động tiện lúc thử nghiệm nhưng nguy hiểm trong sản xuất vì hai lý do: kiểu suy sai từ một tài liệu bất thường rồi cố định mãi, và trường mới tự động thêm làm số trường tăng không kiểm soát. Nổ số trường là sự cố kinh điển: nhật ký có trường tên động theo dữ liệu tạo ra hàng nghìn trường, làm siêu dữ liệu cụm phình và cụm chậm. Cách chặn: tắt ánh xạ động, đặt giới hạn số trường, và dùng kiểu đối tượng phẳng cho dữ liệu không biết trước hình dạng. Hai kiểu cho chuỗi và khác biệt quyết định: kiểu văn bản được phân tích nên tìm kiếm được nhưng không gộp nhóm và không sắp xếp được; kiểu từ khoá không phân tích nên khớp chính xác, gộp nhóm và sắp xếp được. Khai báo cả hai cho một trường bằng trường con là mẫu mặc định. Ánh xạ không sửa được sau khi lập chỉ mục, chỉ thêm trường mới được.

**Outcome.** Thiết kế ánh xạ tường minh cho nhật ký ứng dụng và chứng minh nó chặn được nổ số trường, so với ánh xạ động.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí đếm được. Đạt khi nạp cùng tập dữ liệu vào hai chỉ mục, chỉ mục động vượt 1.000 trường còn chỉ mục tường minh giữ dưới 50, và khi giải thích đúng vì sao một trường kiểu văn bản không gộp nhóm được.

**Lab.** Nạp 2 triệu bản ghi nhật ký có trường động vào hai chỉ mục: một ánh xạ động, một ánh xạ tường minh có giới hạn trường. Đếm số trường mỗi bên. Thử gộp nhóm trên trường kiểu văn bản và quan sát lỗi, rồi dùng trường con kiểu từ khoá. Thử sửa kiểu một trường đã có và quan sát nó không làm được.

**Pitfalls.** Để ánh xạ động trong sản xuất · dùng kiểu văn bản cho trường cần gộp nhóm · trông chờ sửa được kiểu trường sau khi đã lập chỉ mục.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chỉ mục động vượt 1.000 trường còn tường minh dưới 50, và ca gộp nhóm trên kiểu văn bản được giải thích đúng.

### Lesson 178 · Segments, refresh and the near-real-time illusion `TH`
**Prerequisites.** Lesson 177

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phân đoạn là đơn vị lưu trữ bất biến: ghi mới vào bộ đệm trong bộ nhớ, định kỳ tạo phân đoạn mới, và phân đoạn nhỏ được trộn thành lớn, cấu trúc cùng họ với lesson 167. Làm mới là thao tác biến bộ đệm thành phân đoạn tìm kiếm được, mặc định mỗi một giây, nên dữ liệu vừa ghi không tìm thấy ngay; đây là nghĩa chính xác của gần thời gian thực và là nguồn hiểu nhầm phổ biến khi kiểm thử. Nhật ký giao dịch bảo đảm bền vững giữa hai lần làm mới, cùng vai trò với nhật ký ghi trước ở lesson 118. Xoá là đánh dấu chứ không xoá thật, và không gian chỉ thu hồi khi trộn, nên tỉ lệ tài liệu đã xoá là một chỉ số cần theo dõi. Cập nhật là xoá cộng chèn lại cả tài liệu, nên cập nhật một trường vẫn ghi lại toàn bộ. Tăng khoảng làm mới cho tải nạp lớn và tắt hẳn khi nạp một lần, một đòn bẩy nạp nhanh hay bị bỏ qua.

**Outcome.** Đo độ trễ giữa lúc ghi và lúc tìm thấy, và tăng thông lượng nạp bằng cách chỉnh khoảng làm mới.

**Đánh giá.** Tầng *áp dụng*. Objective có hai số đo cụ thể. Đạt khi đo được độ trễ ghi tới tìm thấy ở ba cấu hình làm mới, và khi thông lượng nạp tăng ít nhất 50% khi tắt làm mới trong lúc nạp lô lớn.

**Lab.** Ghi một tài liệu rồi truy vấn ngay trong vòng lặp, đo độ trễ tới khi tìm thấy, lặp 100 lần ở ba khoảng làm mới. Nạp 10 triệu tài liệu với làm mới mặc định, rồi với làm mới tắt, so thông lượng. Cập nhật một trường của 1 triệu tài liệu và đo tỉ lệ tài liệu đã xoá.

**Pitfalls.** Kiểm thử ghi rồi đọc ngay mà không tính khoảng làm mới · để làm mới mặc định khi nạp khối lượng lớn · cập nhật một trường thường xuyên như với hệ quan hệ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Độ trễ ghi tới tìm thấy đo được ở ba cấu hình, và thông lượng nạp tăng ít nhất 50% khi tắt làm mới.

### Lesson 179 · Shards, replicas and the too-many-shards problem `TH`
**Prerequisites.** Lesson 178

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Chỉ mục chia thành mảnh chính, mỗi mảnh là một chỉ mục Lucene độc lập, và mảnh sao là bản sao của mảnh chính. Số mảnh chính cố định khi tạo chỉ mục và không đổi được, nên đây là quyết định khó đảo ngược thứ hai sau ánh xạ. Quá nhiều mảnh là sự cố phổ biến nhất của Elasticsearch: mỗi mảnh tốn bộ nhớ cho siêu dữ liệu và tốn tài nguyên cho trộn, nên một cụm hàng chục nghìn mảnh nhỏ chậm hơn hẳn cụm ít mảnh lớn dù cùng dữ liệu. Quy tắc kích thước mảnh hợp lý và cách tính số mảnh từ tổng dung lượng dự kiến. Nguyên nhân gốc thường là tạo chỉ mục theo ngày cho dữ liệu ít, cùng sai lầm với phân vùng theo ngày ở lesson 168. Vòng đời chỉ mục và chính sách cuộn theo kích thước thay vì theo thời gian, cách chữa đúng. Phân bổ mảnh và cân bằng lại. Mảnh sao tăng khả năng đọc và tăng dung lượng gấp đôi.

**Outcome.** Tính số mảnh hợp lý cho một khối lượng dữ liệu dự kiến, và sửa một cụm quá nhiều mảnh bằng chính sách cuộn theo kích thước.

**Đánh giá.** Tầng *đánh giá*. Objective đòi một phép tính và một quyết định vận hành. Đạt khi số mảnh tính ra nằm trong khoảng hợp lý theo quy tắc kích thước, và khi sau khi áp chính sách cuộn thì số mảnh giảm ít nhất 10 lần với cùng khối lượng dữ liệu, kèm số đo độ trễ truy vấn trước sau.

**Lab.** Dựng cụm có 5.000 mảnh nhỏ bằng cách tạo chỉ mục theo ngày cho dữ liệu ít. Đo bộ nhớ cụm và độ trễ truy vấn. Tính số mảnh hợp lý cho khối lượng đó. Áp chính sách cuộn theo kích thước, lập chỉ mục lại, đo lại. Thử đổi số mảnh chính của một chỉ mục đã có và quan sát nó không làm được.

**Pitfalls.** Tạo chỉ mục theo ngày cho dữ liệu vài trăm mê ga byte mỗi ngày · đặt số mảnh cao để phòng xa · thêm mảnh sao khi nút cổ chai là bộ nhớ chứ không phải đọc.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Số mảnh tính ra nằm trong khoảng hợp lý, và sau khi áp chính sách cuộn số mảnh giảm ít nhất 10 lần kèm số đo độ trễ.

### Lesson 180 · Heap pressure, circuit breakers and cluster health `TH`
**Prerequisites.** Lesson 179

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Elasticsearch chạy trên máy ảo có thu gom rác, nên bộ nhớ vùng đống là tài nguyên khan hiếm nhất và phần lớn sự cố quy về nó, nối lại lesson 13. Quy tắc kích thước vùng đống và lý do không đặt quá ngưỡng nén con trỏ. Phần bộ nhớ còn lại dành cho bộ đệm trang của hệ điều hành mà Lucene dựa vào, nối lại lesson 22, nên đặt vùng đống bằng toàn bộ RAM là sai theo hai hướng cùng lúc. Bốn thứ chiếm vùng đống nhiều nhất: siêu dữ liệu mảnh, dữ liệu trường cho gộp nhóm trên trường kiểu văn bản, bộ đệm truy vấn, và kết quả trung gian của gộp nhóm sâu. Cầu dao chặn thao tác dự kiến vượt ngưỡng bộ nhớ và trả lỗi thay vì để tiến trình chết, và đọc thông báo cầu dao là cách chẩn đoán trực tiếp. Tạm dừng do thu gom rác kéo dài làm nút bị coi là chết và bị loại khỏi cụm, gây cân bằng lại và làm mọi thứ tệ hơn. Ba trạng thái sức khoẻ cụm và nghĩa của từng cái.

**Outcome.** Chẩn đoán một cụm áp lực bộ nhớ về đúng một trong bốn nguyên nhân, và chỉnh cấu hình để cầu dao chặn thay vì nút chết.

**Đánh giá.** Tầng *phân tích*. Objective là chẩn đoán phân biệt bốn nguyên nhân cùng triệu chứng. Kiểm bằng ba ca dựng sẵn; đạt khi định vị đúng ít nhất hai và mỗi lần dẫn được số đo bộ nhớ theo thành phần, và khi sau khi chỉnh thì thao tác nặng bị cầu dao chặn thay vì làm nút chết.

**Lab.** Dựng ba ca: gộp nhóm trên trường kiểu văn bản, gộp nhóm sâu nhiều tầng, và quá nhiều mảnh. Với mỗi ca đọc phân bố bộ nhớ vùng đống theo thành phần. Chỉnh ngưỡng cầu dao và chạy lại ca nặng nhất, xác nhận bị chặn. Đặt vùng đống bằng toàn bộ RAM và quan sát hiệu năng giảm.

**Pitfalls.** Đặt vùng đống bằng toàn bộ RAM · gộp nhóm trên trường kiểu văn bản · tăng vùng đống để chữa khi nguyên nhân là quá nhiều mảnh.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Định vị đúng ít nhất hai trên ba ca có số đo bộ nhớ theo thành phần, và cầu dao chặn được thao tác nặng.

### Lesson 181 · Reindexing and changing a mapping without downtime `TH`
**Prerequisites.** Lesson 180

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ánh xạ không sửa được nên đổi kiểu một trường đòi lập chỉ mục lại toàn bộ, thao tác tốn thời gian tỉ lệ khối lượng dữ liệu. Bí danh chỉ mục là lớp gián tiếp giữa ứng dụng và chỉ mục vật lý, và nó là thứ cho phép làm việc này không ngừng phục vụ: ứng dụng luôn trỏ vào bí danh, còn bí danh chuyển từ chỉ mục cũ sang chỉ mục mới bằng một thao tác nguyên tử. Quy trình bốn bước: tạo chỉ mục mới với ánh xạ mới, lập chỉ mục lại dữ liệu cũ, bắt kịp phần ghi mới phát sinh trong lúc lập lại, rồi chuyển bí danh. Bước ba là bước khó và có hai cách: ghi đôi vào cả hai chỉ mục, hoặc lập lại theo khoảng thời gian rồi chạy bù phần chênh. Đây cùng mẫu mở rộng rồi thu hẹp với lesson 121. Tăng tốc lập chỉ mục lại bằng tắt làm mới và bỏ mảnh sao tạm thời, nối lại lesson 178. Theo dõi tiến độ và khôi phục khi thất bại giữa chừng.

**Outcome.** Đổi kiểu một trường trên chỉ mục 20 triệu tài liệu đang có tải, không ngừng phục vụ và không mất tài liệu nào.

**Đánh giá.** Tầng *sáng tạo*. Objective là thiết kế một quy trình nhiều bước dưới ràng buộc không ngừng phục vụ. Đạt khi số tài liệu chỉ mục mới bằng số cũ cộng số ghi phát sinh trong lúc chuyển, không lệch một tài liệu, và khi truy vấn qua bí danh không lỗi lần nào suốt quá trình.

**Lab.** Chỉ mục 20 triệu tài liệu có tải ghi 500 tài liệu mỗi giây và tải đọc liên tục. Đổi kiểu một trường theo quy trình bốn bước qua bí danh. Đếm tài liệu ở cả hai chỉ mục và đối soát. Ghi lại số lỗi truy vấn suốt quá trình. Đo thời gian lập chỉ mục lại có và không tắt làm mới.

**Pitfalls.** Cho ứng dụng trỏ thẳng vào tên chỉ mục thay vì bí danh · bỏ qua phần ghi phát sinh trong lúc lập lại · để mảnh sao bật trong suốt quá trình lập lại.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Số tài liệu đối soát khớp tuyệt đối, và không lỗi truy vấn nào qua bí danh suốt quá trình.

### Lesson 182 · Log search at scale - a working system `TH`
**Prerequisites.** Lesson 181

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Không có cơ chế mới. Bài gộp module: dựng một hệ tìm kiếm nhật ký hoàn chỉnh dùng mọi thứ đã học. Yêu cầu: ánh xạ tường minh có giới hạn trường từ lesson 177, bộ phân tích tiếng Việt đạt ngưỡng chính xác từ lesson 176, chính sách vòng đời cuộn theo kích thước từ lesson 179, khoảng làm mới chỉnh theo tải nạp từ lesson 178, và giám sát bộ nhớ vùng đống theo thành phần từ lesson 180. Tiêu chí vận hành: số mảnh giữ trong ngưỡng khi dữ liệu tăng qua ba tháng mô phỏng, và độ trễ truy vấn phân vị 95 dưới ngưỡng đặt trước. Phần kết luận bắt buộc: nêu rõ ba loại truy vấn nên chuyển sang hệ khác thay vì cố làm ở đây, thường là gộp nhóm lớn, kết nhiều nguồn, và báo cáo chính xác tuyệt đối. Báo cáo là một trong bảy đầu vào của M18.

**Outcome.** Dựng hệ tìm kiếm nhật ký đạt ngưỡng độ chính xác và độ trễ, và nêu ba loại truy vấn nên chuyển sang hệ khác kèm lý do.

**Đánh giá.** Tầng *sáng tạo*. Objective là thiết kế một hệ dưới nhiều ràng buộc cùng lúc, cộng một phán đoán về ranh giới áp dụng. Chấm theo bốn mục: độ chính xác tìm kiếm 30đ, chỉ số vận hành 30đ, quy trình đổi ánh xạ 20đ, và phần nêu ranh giới 20đ. Đạt khi ≥ 70/100 và phần nêu ranh giới ≥ 50%, vì biết khi nào không dùng là một nửa giá trị của module.

**Lab.** Dựng hệ tìm kiếm cho 200 triệu dòng nhật ký tiếng Việt mô phỏng ba tháng. Đo độ chính xác trên tập 50 truy vấn có đáp án, số mảnh theo thời gian, và độ trễ phân vị 95. Chạy một lần đổi ánh xạ qua bí danh. Viết phần nêu ba loại truy vấn nên chuyển sang hệ khác kèm số đo so sánh.

**Pitfalls.** Mở rộng dần sang làm cả báo cáo phân tích trên cùng cụm · bỏ phần nêu ranh giới vì hệ đang chạy tốt · đo độ trễ lúc cụm rỗi.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đạt ≥ 70/100 và phần nêu ranh giới ≥ 50%, với ba loại truy vấn có số đo so sánh.

# MODULE 18 · CHOOSING A DATABASE - POLYGLOT DESIGN AND DEFENCE

**Lessons 183–188 · 12 giờ**

| | |
|---|---|
| **Objective cấp module** | Thiết kế một sơ đồ dữ liệu nhiều hệ cho một ứng dụng thật và bảo vệ mọi lựa chọn bằng số đo từ bảy module trước |
| **Tiền đề** | M11 · M12 · M13 · M14 · M15 · M16 · M17 |
| **Exit criterion** | Đạt Cổng 4 ≥ 70/100: bảo vệ sơ đồ đa hệ trước hội đồng, giữ vững hoặc đổi kết luận có lý do khi một ràng buộc bị thay giữa buổi |
| **Kỹ năng SFIA** | `ARCH` mức 4 · `DBAD` mức 4 |
| **Chế độ hỏng** | Chọn hệ theo công nghệ đang thịnh hành hoặc theo một bài so sánh trên mạng, rồi không bảo vệ được khi bị hỏi về tải cụ thể |

Module chỉ chạy được vì bảy module trước đã đo trên cùng một use case. Không cùng bài toán thì đây là bài liệt kê tính năng, không phải bài so sánh, cùng ràng buộc với M25 và M31. Năm bài dựng tiêu chí và đối soát, bài cuối là Cổng 4.

### Lesson 183 · Seven systems, one use case - assembling the evidence `TH`
**Prerequisites.** Module 18: M11 · M12 · M13 · M14 · M15 · M16 · M17

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Tập hợp số đo từ bảy module thành một bảng duy nhất, và đây là bước lộ ra chỗ đo không so được: khác phần cứng, khác khối lượng dữ liệu, khác định nghĩa chỉ số. Chín trục đo và cách chuẩn hoá từng trục để so được: mô hình dữ liệu tự nhiên cho miền nghiệp vụ, thông lượng ghi, độ trễ đọc theo khoá, độ trễ truy vấn phân tích, khả năng kết nhiều nguồn, bảo đảm giao dịch, điểm phục hồi và thời lượng phục hồi, công sức vận hành, và chi phí. Nguyên tắc chuẩn hoá: cùng khối lượng dữ liệu, cùng phần cứng hoặc quy về đơn vị tài nguyên, và cùng định nghĩa chỉ số, nhất là phân vị. Ô nào chưa đo được thì ghi là chưa đo, không ghi là tương đương. Ba trục không đo được bằng lab ngắn và phải ghi rõ giới hạn: độ ổn định dài hạn, chất lượng hệ sinh thái công cụ, và chi phí nhân sự.

**Outcome.** Lập bảng chín trục nhân bảy hệ từ số đo của chính mình, và đánh dấu rõ ô nào chưa đo được cùng lý do.

**Đánh giá.** Tầng *phân tích*. Objective đòi chuẩn hoá số đo để chúng so được, việc khó hơn thu thập. Đạt khi ít nhất 45 trên 63 ô có số đo từ lab, khi mọi ô còn lại được đánh dấu chưa đo kèm lý do, và khi ba trục không đo được bằng lab ngắn được nêu rõ.

**Lab.** Thu số đo từ bảy module. Với mỗi trục, kiểm ba điều kiện chuẩn hoá và ghi lại ô nào vi phạm. Đo bổ sung cho ô thiếu khi chi phí chấp nhận được. Lập bảng chín nhân bảy. Đổi bảng chéo với một học viên khác và rà soát điều kiện chuẩn hoá.

**Pitfalls.** Điền ô bằng con số từ tài liệu nhà cung cấp · ghi tương đương cho ô chưa đo · so độ trễ trung bình của hệ này với phân vị 95 của hệ kia.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ít nhất 45 trên 63 ô có số đo từ lab, ô còn lại đánh dấu chưa đo kèm lý do, và ba trục ngoài tầm lab được nêu.

### Lesson 184 · The decision matrix - workload shapes, not system rankings `LT`
**Prerequisites.** Lesson 183

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Câu hỏi đúng không phải hệ nào tốt hơn mà là tải nào hợp hệ nào, và đổi cách hỏi là nội dung chính của bài. Sáu hình dạng tải và hệ hợp với từng cái: giao dịch nhiều ghi nhỏ cần ràng buộc, đọc theo khoá độ trễ thấp, phân tích quét lớn, tìm kiếm toàn văn, dữ liệu hình dạng thay đổi, và chuỗi sự kiện chỉ chèn thêm. Bảy yếu tố phải cân trước khi chọn, theo thứ tự tôi đề nghị: hình dạng dữ liệu và mẫu truy cập, yêu cầu nhất quán, khối lượng và tốc độ tăng, điểm phục hồi và thời lượng phục hồi, kỹ năng đội, chi phí vận hành, và cuối cùng mới là hiệu năng thô. Đặt hiệu năng cuối là có chủ đích: nó là yếu tố dễ đo nhất nên hay bị cân nặng quá mức, trong khi kỹ năng đội và chi phí vận hành quyết định thành bại nhiều hơn. Ba dấu hiệu một lựa chọn sai: phải viết nhiều mã để bù thiếu sót của hệ, phải đồng bộ thủ công giữa hai hệ, và không ai trong đội chẩn đoán được khi hỏng.

**Outcome.** Ánh xạ sáu hình dạng tải sang hệ phù hợp, và giải thích vì sao hiệu năng thô đặt cuối trong bảy yếu tố.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết dựng khung quyết định cho ba bài sau. Đạt khi ánh xạ đúng ít nhất năm trên sáu hình dạng kèm lý do từ bảng ở lesson 183, và khi lập luận về thứ tự bảy yếu tố nêu được ít nhất hai hậu quả cụ thể của việc cân hiệu năng quá mức.

**Lab.** Nhận sáu mô tả tải thật. Ánh xạ từng cái sang một hoặc hai hệ, dẫn ô cụ thể trong bảng lesson 183. Với hai tải, viết kịch bản chọn theo hiệu năng thô và chỉ ra hậu quả sau một năm. Thảo luận nhóm ba dấu hiệu lựa chọn sai từ kinh nghiệm lab.

**Pitfalls.** Xếp hạng bảy hệ từ tốt tới tệ · chọn theo công nghệ đang thịnh hành · bỏ qua kỹ năng đội vì nghĩ có thể học.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ánh xạ đúng ít nhất năm trên sáu hình dạng có dẫn chứng, và lập luận về thứ tự nêu hai hậu quả cụ thể.

### Lesson 185 · Polyglot architecture - synchronising two systems `TH`
**Prerequisites.** Lesson 184

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Dùng nhiều hệ là chuyện bình thường, nhưng mỗi hệ thêm vào là một bài toán đồng bộ, và chi phí đó thường bị bỏ qua lúc thiết kế. Ba cách đồng bộ và đánh đổi: ghi đôi từ ứng dụng đơn giản nhưng không nguyên tử nên hai hệ lệch khi một bên lỗi, bắt thay đổi dữ liệu từ nguồn gốc đáng tin hơn và là nội dung chặng 6, và đồng bộ theo lô định kỳ rẻ nhất nhưng độ trễ cao. Mẫu hộp thư đi để ghi đôi trở nên đáng tin: ghi dữ liệu và ghi bản tin vào cùng một giao dịch, rồi một tiến trình riêng đọc bản tin và đẩy sang hệ thứ hai. Nguồn sự thật phải chỉ định rõ một hệ duy nhất, và mọi hệ khác là bản dẫn xuất dựng lại được; không có quy tắc này thì khi hai bên lệch không ai biết bên nào đúng. Đối soát định kỳ giữa hai hệ như một phép kiểm bắt buộc, nối lại lesson 104. Ba câu hỏi phải trả lời trước khi thêm hệ thứ hai.

**Outcome.** Thiết kế đường đồng bộ giữa hai hệ cho một use case, chỉ định nguồn sự thật, và cài phép đối soát phát hiện được lệch.

**Đánh giá.** Tầng *áp dụng*. Objective có sản phẩm và một phép kiểm chứng. Đạt khi đường đồng bộ chạy và phép đối soát phát hiện được lệch do lỗi bơm vào, và khi tài liệu chỉ rõ nguồn sự thật cùng cách dựng lại hệ dẫn xuất từ nó.

**Lab.** Đồng bộ đơn hàng từ PostgreSQL sang Elasticsearch để tìm kiếm. Cài ghi đôi trần, bơm lỗi ở bên thứ hai, đo số bản ghi lệch. Cài lại bằng mẫu hộp thư đi, lặp thí nghiệm. Viết phép đối soát chạy hằng giờ. Xoá sạch hệ dẫn xuất và dựng lại từ nguồn sự thật, đo thời gian.

**Pitfalls.** Ghi đôi trực tiếp từ ứng dụng cho dữ liệu quan trọng · không chỉ định nguồn sự thật · thêm hệ thứ ba trước khi giải xong bài toán đồng bộ giữa hai hệ đầu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đường đồng bộ chạy và phép đối soát phát hiện được lệch bơm vào, và hệ dẫn xuất dựng lại được từ nguồn sự thật.

### Lesson 186 · Designing the schema for an e-commerce platform `TH`
**Prerequisites.** Lesson 185

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Không có cơ chế mới. Bài thiết kế: nhận mô tả một nền tảng thương mại điện tử có sáu nhóm yêu cầu khác nhau về hình dạng tải, và thiết kế sơ đồ dữ liệu cho nó. Sáu nhóm chọn có chủ đích để không một hệ nào phủ hết: đặt hàng và thanh toán cần giao dịch, danh mục sản phẩm hình dạng thay đổi, tìm kiếm sản phẩm bằng tiếng Việt, phiên người dùng độ trễ thấp, sự kiện hành vi khối lượng lớn, và báo cáo doanh thu quét lớn. Đầu ra gồm bốn phần: sơ đồ các hệ và dữ liệu nào ở đâu, đường đồng bộ giữa chúng theo lesson 185, phát biểu nguồn sự thật, và phép tính chi phí vận hành ước lượng. Ràng buộc bắt buộc: mỗi hệ đưa vào phải dẫn được ít nhất hai ô trong bảng lesson 183 làm lý do, và phải nêu phương án một hệ duy nhất cùng lý do loại nó.

**Outcome.** Thiết kế sơ đồ dữ liệu đa hệ cho sáu nhóm yêu cầu, mỗi hệ dẫn được hai ô số đo làm lý do, kèm phương án một hệ bị loại.

**Đánh giá.** Tầng *sáng tạo*. Objective là thiết kế dưới ràng buộc nhiều chiều. Chấm theo năm mục: ánh xạ tải sang hệ 25đ, đường đồng bộ và nguồn sự thật 25đ, dẫn chứng số đo 20đ, phép tính chi phí vận hành 15đ, và phương án bị loại 15đ. Đạt khi ≥ 70/100 và mục dẫn chứng ≥ 50%.

**Lab.** Nhận mô tả nền tảng kèm số liệu: 50.000 đơn mỗi ngày, 2 triệu sản phẩm, 100 triệu sự kiện mỗi ngày, đội 4 người. Thiết kế sơ đồ đủ bốn phần. Viết phương án một hệ duy nhất và lý do loại. Đổi bài chéo và rà soát dẫn chứng từng hệ.

**Pitfalls.** Đưa cả bảy hệ vào sơ đồ vì đã học cả bảy · bỏ phần chi phí vận hành vì khó ước lượng · không xét phương án một hệ duy nhất.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đạt ≥ 70/100 và mục dẫn chứng ≥ 50%, với mỗi hệ dẫn được hai ô số đo.

### Lesson 187 · Preparing the defence - assumptions and what would change them `TH`
**Prerequisites.** Lesson 186

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bảo vệ một thiết kế không phải chứng minh nó đúng mà là nêu rõ nó đúng trong điều kiện nào. Ba loại phát biểu phải tách bạch: số đo, giả định, và suy luận. Số đo là thứ đã chạy; giả định là thứ nhận từ đề bài hoặc tự đặt; suy luận là thứ rút ra từ hai cái kia. Lẫn lộn ba loại là lỗi bảo vệ phổ biến nhất. Với mỗi giả định, phát biểu tín hiệu khiến phải xem lại: khối lượng vượt ngưỡng nào, độ trễ yêu cầu xuống mức nào, đội mất người nào. Đây là nội dung của một bản ghi quyết định kiến trúc ở lesson 90, và phần phương án bị loại là phần có giá trị nhất. Chuẩn bị cho ba câu hỏi chắc chắn bị hỏi: vì sao không dùng một hệ cho tất cả, vì sao không dùng hệ đang thịnh hành, và nếu khối lượng gấp mười thì sao. Tập trả lời bằng số chứ bằng lập luận chung. Nhượng bộ đúng phần chưa đủ bằng chứng là dấu hiệu bảo vệ tốt, không phải dấu hiệu yếu.

**Outcome.** Viết bản ghi quyết định kiến trúc cho sơ đồ của mình, tách bạch ba loại phát biểu và nêu tín hiệu xem lại cho từng giả định.

**Đánh giá.** Tầng *đánh giá*. Objective đòi phân loại độ chắc chắn của chính lập luận mình. Kiểm bằng rà soát chéo: một học viên khác đọc và phải phân loại lại được ba loại phát biểu. Đạt khi ít nhất 80% phát biểu được phân loại khớp giữa hai người, và khi mọi giả định đều có tín hiệu xem lại phát biểu bằng số.

**Lab.** Viết bản ghi quyết định cho sơ đồ ở lesson 186. Gắn nhãn từng phát biểu là số đo, giả định, hay suy luận. Với mỗi giả định, viết tín hiệu xem lại bằng số. Đổi bài chéo để người khác phân loại lại. Tập trả lời ba câu hỏi chắc chắn bị hỏi, mỗi câu dưới hai phút.

**Pitfalls.** Trình bày giả định như số đo · viết tín hiệu xem lại bằng tính từ · chuẩn bị bảo vệ mọi thứ thay vì chuẩn bị nhượng bộ phần chưa đủ bằng chứng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ít nhất 80% phát biểu được phân loại khớp giữa hai người, và mọi giả định có tín hiệu xem lại bằng số.

### Lesson 188 · Gate 4 - defend a polyglot schema under changing constraints `KT`
**Prerequisites.** Lesson 187

**In-class (120 phút).** 75 phút làm bài độc lập · 45 phút chữa bài và phân tích lỗi theo nhóm

**Learn.** Không có nội dung mới. Cổng 4 của chương trình, đóng chặng 3.

**Outcome.** Bảo vệ một sơ đồ dữ liệu đa hệ trước hội đồng, và điều chỉnh hoặc giữ vững kết luận có lý do khi hội đồng thay một ràng buộc giữa buổi.

**Đánh giá.** Tầng *đánh giá*. Cổng đo năng lực thiết kế và bảo vệ dưới chất vấn, không đo trí nhớ về bảy hệ. Thang điểm: A 20đ sơ đồ và ánh xạ tải sang hệ · B 20đ dẫn chứng số đo từ lab của chính mình · C 15đ đường đồng bộ và nguồn sự thật · D 15đ giả định và tín hiệu xem lại · E 30đ phản ứng khi ràng buộc bị đổi. Đạt khi ≥ 70/100 và phần E ≥ 50%. Phần E nặng nhất vì thiết kế đúng trong một điều kiện là dễ, còn biết điều kiện nào lật ngược nó mới là năng lực kiến trúc.

**Lab.** Trình bày 20 phút, chất vấn 25 phút. Hội đồng gồm một kỹ sư dữ liệu đi làm, một người đóng vai chủ sản phẩm, và một người đóng vai vận hành. Giữa buổi hội đồng đổi một ràng buộc: khối lượng gấp mười, hoặc yêu cầu điểm phục hồi xuống 5 phút, hoặc đội mất người duy nhất biết một hệ.

**Pitfalls.** Bảo vệ hệ mình thích thay vì hệ hợp ràng buộc · giữ nguyên kết luận khi ràng buộc mới đã lật ngược lập luận · đổi kết luận khi bị chất vấn mà không có bằng chứng mới.

**Self-study (2,4 giờ).** Không có bài tự học. Nếu không đạt, theo phụ lục khắc phục khi không đạt cổng

**Done when.** Đạt ≥ 70/100 và phần E ≥ 50%.

# MODULE 19 · DATA MODELING AND WAREHOUSING

**Lessons 189–202 · 28 giờ**

| | |
|---|---|
| **Objective cấp module** | Thiết kế một lược đồ kho dữ liệu từ mô tả nghiệp vụ, phát biểu và kiểm chứng được hạt của mọi bảng, và bàn giao nó cho người dựng mart mà không phải giải thích thêm |
| **Tiền đề** | M18 |
| **Exit criterion** | Lược đồ sao cài đặt được, có chiều thay đổi chậm và bảng lịch, và đạt rà soát chéo về khả năng bàn giao |
| **Kỹ năng SFIA** | `DTAN` mức 4 · `DBAD` mức 3 |
| **Chế độ hỏng** | Thiết kế đẹp trên giấy mà không khai báo được hạt bằng một câu, nên mọi bảng phía sau kế thừa sự mơ hồ đó |

Ranh giới với chương trình Analytics Engineer: Data Engineer thiết kế và bàn giao tập dữ liệu có hợp đồng; mart theo miền nghiệp vụ, semantic layer và định nghĩa chỉ số thuộc về Analytics Engineer. Module này dạy mô hình chiều đủ sâu để bàn giao đúng, không dạy để sở hữu mart. Bảy bài đầu là mô hình hoá, bốn bài giữa là kiến trúc phân lớp và bàn giao, hai bài cuối là thiết kế vật lý và dự án.

### Lesson 189 · Normalization and where denormalization is deliberate `LT`
**Prerequisites.** Module 19: M18

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Ba dị thường thao tác và cách dạy đi từ dị thường quan sát được tới quy tắc, không theo chiều ngược lại: gặp một bảng phẳng rồi thử thêm, sửa, xoá và thấy nó hỏng ở đâu. Phụ thuộc hàm và cách phát hiện từ chính dữ liệu bằng truy vấn đếm. Dạng chuẩn một và giá trị nguyên tử: một cột chứa danh sách ngăn bởi dấu phẩy làm mọi phép lọc và gộp theo phần tử trở nên không tin được. Dạng chuẩn hai và phụ thuộc đầy đủ vào khoá. Dạng chuẩn ba và phụ thuộc bắc cầu. Dạng chuẩn Boyce Codd ở mức nhận biết. Phi chuẩn hoá có chủ đích: điều kiện áp dụng, chi phí đi kèm, và điều kiện bắt buộc là phải có cơ chế giữ cho bản sao nhất quán. Phân biệt phi chuẩn hoá có chủ đích với thiếu chuẩn hoá do không biết: cái đầu có tài liệu nêu lý do, cái sau thì không.

**Outcome.** Chuẩn hoá một bảng phẳng tới dạng chuẩn ba và chỉ ra dị thường nào được loại bỏ ở bước nào.

**Đánh giá.** Tầng *áp dụng*. Objective là một thủ tục có tiêu chí đúng sai rõ. Đạt khi lược đồ kết quả không còn phụ thuộc bắc cầu nào, kiểm bằng truy vấn phát hiện phụ thuộc hàm, và khi ba dị thường được gán đúng bước loại bỏ chúng.

**Lab.** Nhận bảng phẳng 40 cột chứa đơn hàng, khách, sản phẩm và địa chỉ. Thử ba thao tác gây dị thường và ghi lại hỏng thế nào. Chuẩn hoá từng bước tới dạng chuẩn ba, sau mỗi bước chạy truy vấn phát hiện phụ thuộc hàm còn lại. Tìm một cột chứa danh sách và tách nó ra.

**Pitfalls.** Chuẩn hoá theo quy tắc mà không kiểm phụ thuộc hàm trên dữ liệu thật · phi chuẩn hoá mà không ghi lý do · để cột chứa danh sách ngăn bởi dấu phẩy.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Lược đồ kết quả không còn phụ thuộc bắc cầu kiểm bằng truy vấn, và ba dị thường gán đúng bước loại bỏ.

### Lesson 190 · OLTP against OLAP - access patterns decide structure `LT`
**Prerequisites.** Lesson 189

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Sáu chiều khác biệt giữa hệ thống giao dịch và hệ thống phân tích: mẫu truy cập, mức chuẩn hoá, hạt dữ liệu, tần suất ghi, nhóm người dùng, và chỉ số hiệu năng mục tiêu. Mỗi chiều dẫn ra một quyết định thiết kế khác nhau, nên cùng một dữ liệu có hai lược đồ hợp lý khác nhau ở hai nơi, và đây là lý do sao chép nguyên lược đồ giao dịch sang kho phân tích luôn cho kết quả tệ. Lưu theo dòng so với lưu theo cột và hệ quả lên phép gộp, nối lại lesson 41 và 169. Hậu quả vận hành của việc chạy báo cáo nặng trên hệ thống sản xuất: tranh chấp khoá ở lesson 116, ô nhiễm bộ đệm ở lesson 110, và độ trễ tăng cho giao dịch. Kho dữ liệu, hồ dữ liệu và lakehouse ở mức thuật ngữ đủ để trao đổi, chi tiết ở M34. Bốn mức độ trễ dữ liệu và chi phí tương ứng, cùng nguyên tắc chọn mức thấp nhất mà nghiệp vụ thật sự cần.

**Outcome.** Chọn loại hệ thống cho một tình huống cho trước và biện minh bằng ít nhất ba trong sáu chiều khác biệt.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn có biện minh nhiều chiều. Kiểm bằng bốn tình huống; đạt khi chọn đúng cả bốn và mỗi lần nêu ít nhất ba chiều, không chấp nhận lý do chung như phân tích thì dùng kho.

**Lab.** Nhận bốn tình huống có yêu cầu độ trễ và mẫu truy cập khác nhau. Chọn loại hệ thống và nêu ba chiều cho từng cái. Sau đó chạy một báo cáo gộp nặng trên PostgreSQL đang có tải giao dịch, đo độ trễ giao dịch trước và trong lúc chạy báo cáo.

**Pitfalls.** Sao chép nguyên lược đồ giao dịch sang kho phân tích · chọn độ trễ thấp nhất có thể thay vì mức nghiệp vụ cần · chạy báo cáo trên bản chính vì tiện.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chọn đúng cả bốn tình huống, mỗi lần nêu ít nhất ba chiều, và có số đo tác động lên độ trễ giao dịch.

### Lesson 191 · Dimensional modeling - the four Kimball steps `LT`
**Prerequisites.** Lesson 190

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bốn bước theo thứ tự cố định: chọn quy trình nghiệp vụ, khai báo hạt, xác định chiều, xác định độ đo. Thứ tự này không đảo được, và bước hai là bước chặn: chọn sai hạt thì ba bước sau đều phải làm lại. Chọn quy trình nghiệp vụ nghĩa là chọn một sự kiện nghiệp vụ có thật, không chọn một phòng ban hay một báo cáo; chọn theo báo cáo là sai lầm phổ biến vì báo cáo đổi còn quy trình thì không. Bảng sự kiện chứa khoá ngoại và độ đo, không chứa thuộc tính mô tả. Bảng chiều rộng, phi chuẩn, giàu thuộc tính, và cố ý lặp dữ liệu vì mục tiêu là đọc nhanh và đọc dễ chứ không phải tiết kiệm dung lượng. Vì sao mô hình chiều vẫn sống sau ba mươi năm dù phần cứng đã đổi hoàn toàn: nó tối ưu cho khả năng hiểu của con người, và đó là ràng buộc không đổi theo phần cứng. Ranh giới trong chương trình: Data Engineer dựng lớp này để bàn giao, Analytics Engineer dựng mart lên trên.

**Outcome.** Áp bốn bước lên một mô tả nghiệp vụ và phát biểu hạt của bảng sự kiện bằng một câu không mơ hồ.

**Đánh giá.** Tầng *áp dụng*. Objective có sản phẩm kiểm được bằng rà soát. Đạt khi phát biểu hạt là một câu có dạng một dòng là một sự kiện gì, và khi một học viên khác đọc câu đó rồi suy ra đúng bảng sự kiện có bao nhiêu dòng cho một tập dữ liệu mẫu.

**Lab.** Nhận mô tả nghiệp vụ giao hàng. Áp bốn bước theo thứ tự. Viết phát biểu hạt bằng một câu. Đổi bài chéo: người khác đọc câu đó và dự đoán số dòng bảng sự kiện cho tập mẫu 1.000 sự kiện. So dự đoán với số thật. Thử chọn quy trình theo một báo cáo và chỉ ra nó hỏng ở đâu khi báo cáo đổi.

**Pitfalls.** Chọn quy trình nghiệp vụ theo một báo cáo có sẵn · nhảy sang xác định chiều trước khi khai báo hạt · đặt thuộc tính mô tả vào bảng sự kiện.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phát biểu hạt là một câu, và người khác suy ra đúng số dòng bảng sự kiện từ câu đó.

### Lesson 192 · Declaring the grain and verifying it `TH`
**Prerequisites.** Lesson 191

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hạt là phát biểu về ý nghĩa của một dòng, và nó phải kiểm chứng được chứ không chỉ phát biểu được. Ba cách kiểm chứng và cái mỗi cách bắt: đếm số dòng phân biệt theo tập cột định danh hạt phải bằng tổng số dòng, phép đếm theo nhóm không được ra nhóm nào lớn hơn một, và tổng một độ đo cộng được phải khớp tổng ở nguồn. Phát biểu hạt sai theo hai hướng: mịn hơn thực tế làm bảng có dòng trùng, thô hơn thực tế làm mất chi tiết không lấy lại được. Hướng thứ hai không có cách sửa ngoài làm lại từ nguồn, nên nó tốn kém hơn. Hạt thay đổi khi nghiệp vụ thay đổi và quy trình xử lý: tạo bảng mới thay vì sửa hạt bảng cũ. Trộn hai hạt trong một bảng và cách phát hiện: một cột độ đo có giá trị lặp lại theo nhóm là dấu hiệu. Hạt của bảng chiều cũng phải khai báo và hay bị bỏ qua.

**Outcome.** Kiểm chứng phát biểu hạt bằng ba phép kiểm, và phát hiện một bảng bị trộn hai hạt trong một tập dữ liệu cho trước.

**Đánh giá.** Tầng *phân tích*. Objective đòi phát hiện lỗi hạt chứ không chỉ khai báo. Đạt khi ba phép kiểm chạy được trên năm bảng, và khi phát hiện đúng bảng bị trộn hạt cùng chỉ ra cột nào lặp lại theo nhóm làm bằng chứng.

**Lab.** Nhận năm bảng, trong đó một bảng trộn hai hạt và một bảng có phát biểu hạt mịn hơn thực tế. Chạy ba phép kiểm cho từng bảng. Định vị hai bảng có vấn đề. Với bảng trộn hạt, chỉ cột lặp lại và đề xuất tách. Viết ba phép kiểm thành truy vấn dùng lại được cho bảng bất kỳ.

**Pitfalls.** Phát biểu hạt rồi không kiểm · sửa hạt của bảng đang có người dùng thay vì tạo bảng mới · bỏ qua hạt của bảng chiều.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba phép kiểm chạy trên năm bảng, và bảng trộn hạt được phát hiện kèm cột lặp làm bằng chứng.

### Lesson 193 · Fact tables - three types and additivity `TH`
**Prerequisites.** Lesson 192

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba loại bảng sự kiện và điều kiện dùng từng loại: giao dịch ghi một dòng cho mỗi sự kiện, ảnh chụp định kỳ ghi trạng thái theo chu kỳ cố định, và ảnh chụp tích luỹ ghi một dòng cho mỗi thực thể rồi cập nhật khi nó qua các mốc. Loại thứ ba là loại duy nhất trong ba loại có cập nhật, nên nó phá vỡ giả định chỉ chèn thêm của phần lớn kiến trúc và phải xử lý riêng. Ba loại độ đo theo tính cộng được: cộng được theo mọi chiều, bán cộng được không cộng theo thời gian như số dư và tồn kho, và không cộng được như tỉ lệ và phần trăm. Hậu quả khi cộng nhầm: cộng số dư theo thời gian ra con số vô nghĩa nhưng trông hợp lý, và đây là lỗi báo cáo hay gặp. Độ đo phái sinh và nơi nên tính chúng: tính ở tầng bàn giao hay để Analytics Engineer tính, cùng tiêu chí chọn. Bảng sự kiện không có độ đo cho sự kiện chỉ cần đếm.

**Outcome.** Phân loại độ đo theo tính cộng được và chọn đúng loại bảng sự kiện cho ba bài toán, nêu hậu quả khi chọn sai.

**Đánh giá.** Tầng *áp dụng*. Objective gồm hai phép phân loại có đáp án. Đạt khi phân loại đúng ít nhất 10 trên 12 độ đo, chọn đúng loại bảng cho cả ba bài toán, và khi tính được con số sai sinh ra từ việc cộng nhầm một độ đo bán cộng được.

**Lab.** Nhận 12 độ đo và phân loại theo tính cộng được. Nhận ba bài toán: đơn hàng, số dư tài khoản cuối ngày, và đơn hàng qua năm mốc trạng thái. Chọn loại bảng cho từng cái. Cộng số dư theo thời gian trên tập thật và so với cách tính đúng, ghi lại chênh lệch.

**Pitfalls.** Cộng độ đo bán cộng được theo thời gian · dùng bảng giao dịch cho bài toán theo dõi qua các mốc · lưu tỉ lệ vào bảng sự kiện rồi cộng chúng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân loại đúng ít nhất 10 trên 12 độ đo, chọn đúng ba loại bảng, và tính được chênh lệch do cộng nhầm.

### Lesson 194 · Dimension tables and surrogate keys `TH`
**Prerequisites.** Lesson 193

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bảng chiều rộng và giàu thuộc tính, và lý do thêm thuộc tính rẻ hơn nhiều so với thêm bảng: mỗi thuộc tính là một cách cắt lát dữ liệu mà người dùng không phải kết thêm. Khoá thay thế là khoá do kho sinh ra, tách khỏi khoá nghiệp vụ của hệ nguồn, và ba lý do cần nó: hệ nguồn có thể tái dùng khoá, hợp nhất nhiều nguồn có khoá trùng, và chiều thay đổi chậm cần nhiều dòng cho cùng một thực thể, nối tới lesson 195. Khoá băm từ khoá nghiệp vụ và đánh đổi: tính được ở nhiều nơi nên không cần tra cứu, nhưng cạm bẫy khi băm từ cột có thể rỗng vì hai bản ghi khác nhau ra cùng băm. Chuẩn hoá giá trị rỗng trước khi băm là bắt buộc. Chiều dùng chung giữa nhiều bảng sự kiện và vì sao nó là điều kiện để so sánh chéo. Chiều rác gom các cờ bản số thấp. Chiều suy biến là khoá nghiệp vụ giữ lại trong bảng sự kiện. Chiều vai trò dùng một bảng cho nhiều vai trò.

**Outcome.** Thiết kế bảng chiều dùng chung được cho nhiều bảng sự kiện, và chứng minh khoá băm xử lý đúng trường hợp có giá trị rỗng.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí kiểm bằng thực nghiệm. Đạt khi chiều dùng được cho hai bảng sự kiện khác nhau mà không phải đổi, và khi thực nghiệm cho thấy khoá băm không chuẩn hoá giá trị rỗng sinh ra va chạm còn bản chuẩn hoá thì không.

**Lab.** Thiết kế chiều khách hàng dùng chung cho bảng sự kiện đơn hàng và bảng sự kiện hỗ trợ. Sinh khoá băm từ ba cột trong đó một cột có giá trị rỗng. Chạy trên 1 triệu bản ghi và đếm va chạm. Chuẩn hoá giá trị rỗng rồi chạy lại. Tạo một chiều rác từ năm cờ bản số thấp.

**Pitfalls.** Băm từ cột có thể rỗng mà không chuẩn hoá · dùng khoá nghiệp vụ làm khoá chiều · tạo bảng chiều riêng cho mỗi bảng sự kiện.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chiều dùng được cho hai bảng sự kiện không phải đổi, và thực nghiệm cho thấy khác biệt va chạm trước sau chuẩn hoá.

### Lesson 195 · Slowly changing dimensions - types and implementation `TH`
**Prerequisites.** Lesson 194

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài toán phát biểu bằng một ví dụ định lượng được: khách chuyển từ vùng A sang vùng B, và nếu bảng chiều ghi đè thì toàn bộ doanh thu lịch sử của khách đó nhảy sang vùng B, làm báo cáo theo vùng của mọi kỳ trước đổi. Bốn loại xử lý và hậu quả báo cáo cụ thể của từng loại: loại không cho đổi, loại ghi đè mất lịch sử, loại thêm dòng mới giữ lịch sử, và loại thêm cột giữ một giá trị trước đó. Cài đặt loại thêm dòng mới bằng khoá thay thế cộng ba cột hiệu lực từ, hiệu lực đến, và cờ bản ghi hiện hành. Mẫu tải: phát hiện thay đổi bằng so sánh cột hoặc bằng dấu thời gian, đóng dòng cũ, mở dòng mới, và cả ba bước phải trong một giao dịch. Truy vấn trạng thái hiện hành so với truy vấn tại một thời điểm trong quá khứ. Chọn loại nào là quyết định nghiệp vụ chứ không kỹ thuật, và phải hỏi người dùng dữ liệu.

**Outcome.** Cài đặt chiều thay đổi chậm loại thêm dòng mới, và chứng minh báo cáo lịch sử không đổi sau khi thuộc tính chiều thay đổi.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí đối chứng tuyệt đối. Đạt khi báo cáo doanh thu theo vùng cho ba kỳ quá khứ cho kết quả y hệt trước và sau khi 10% khách đổi vùng, và khi truy vấn tại một thời điểm trong quá khứ trả về đúng trạng thái của thời điểm đó.

**Lab.** Dựng chiều khách hàng loại thêm dòng mới. Chạy báo cáo doanh thu theo vùng ba kỳ, ghi kết quả. Cho 10% khách đổi vùng và chạy tải chiều. Chạy lại báo cáo và so từng dòng. Truy vấn trạng thái khách tại một ngày trong quá khứ. Thử cài bằng loại ghi đè và ghi lại chênh lệch.

**Pitfalls.** Dùng loại ghi đè cho thuộc tính mà báo cáo lịch sử phụ thuộc · quên cờ bản ghi hiện hành nên truy vấn hiện tại phải lọc theo ngày · đóng dòng cũ và mở dòng mới ngoài giao dịch.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Báo cáo ba kỳ quá khứ không đổi sau khi 10% khách đổi vùng, và truy vấn tại thời điểm quá khứ trả đúng trạng thái.

### Lesson 196 · The calendar dimension and Vietnamese fiscal reality `TH`
**Prerequisites.** Lesson 195

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bảng lịch thường là bảng chiều đầu tiên được dựng trong một kho dữ liệu, vì gần như mọi bảng sự kiện đều kết với nó. Cách sinh bằng script có hạt giống cố định thay vì nhập tay. Tập thuộc tính tối thiểu: ngày, tuần, tháng, quý, năm theo lịch dương; ngày làm việc và ngày nghỉ; tuần theo chuẩn quốc tế; và các thuộc tính theo năm tài chính khi nó lệch năm dương lịch. Đặc thù Việt Nam mà bảng lịch mẫu nước ngoài không có: Tết âm lịch dịch chuyển giữa tháng dương lịch nên phép so cùng kỳ năm trước theo tháng dương bị lệch nặng ở quý một, và cách xử lý là thêm thuộc tính đánh dấu kỳ Tết cùng ngày tương ứng năm trước theo âm lịch. Ngày nghỉ bù và tuần làm việc sáu ngày ở một số ngành. Chiều vai trò: cùng bảng lịch dùng cho ngày đặt, ngày giao và ngày thanh toán, nối lại lesson 194. Chiều thời gian trong ngày tách riêng khi cần phân tích theo giờ.

**Outcome.** Dựng bảng lịch đầy đủ cho doanh nghiệp Việt Nam, và chứng minh phép so cùng kỳ năm trước không bị Tết âm lịch làm lệch.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí đối chứng trên một ca khó và đặc thù. Đạt khi phép so cùng kỳ cho quý một của ba năm liên tiếp khớp bản đối chứng tính theo kỳ Tết, và khi bảng lịch dùng được làm chiều vai trò cho ba cột ngày khác nhau.

**Lab.** Sinh bảng lịch 10 năm bằng script. Thêm thuộc tính Tết âm lịch cho ba năm. Chạy báo cáo so cùng kỳ quý một theo tháng dương và theo kỳ Tết, so hai kết quả với bản đối chứng. Dùng bảng lịch làm chiều vai trò cho ngày đặt, ngày giao, ngày thanh toán trong cùng một truy vấn.

**Pitfalls.** Dùng bảng lịch mẫu nước ngoài không có Tết · so cùng kỳ theo tháng dương cho quý một · tạo ba bảng lịch riêng cho ba vai trò ngày.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** So cùng kỳ quý một ba năm khớp bản đối chứng, và bảng lịch dùng được cho ba vai trò ngày.

### Lesson 197 · Star schema against snowflake and the bus matrix `TH`
**Prerequisites.** Lesson 196

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Lược đồ sao đặt bảng sự kiện ở giữa và các chiều phi chuẩn xung quanh; lược đồ bông tuyết chuẩn hoá tiếp các chiều thành nhiều bảng. Bông tuyết sạch hơn về lý thuyết nhưng thực hành thiên về sao, và ba lý do: ít phép kết hơn nên truy vấn nhanh và dễ viết, người dùng hiểu được cấu trúc mà không cần sơ đồ, và dung lượng tiết kiệm được từ chuẩn hoá chiều là không đáng kể so với bảng sự kiện. Điều kiện bị ép dùng bông tuyết: chiều rất lớn có thuộc tính lặp nhiều, hoặc công cụ hạ nguồn yêu cầu. Ma trận xe buýt là bảng quy trình nghiệp vụ nhân chiều dùng chung, và nó là công cụ lập kế hoạch: mỗi ô đánh dấu cho biết hai quy trình nào so sánh chéo được với nhau. Nhiều bảng sự kiện ở hạt khác nhau và cách so sánh chúng: không kết trực tiếp mà gộp từng bảng về hạt chung rồi mới kết, vì kết trực tiếp gây nhân dòng, nối lại lesson 100.

**Outcome.** Chuyển một lược đồ chuẩn hoá thành lược đồ sao, lập ma trận xe buýt, và so sánh hai bảng sự kiện khác hạt mà không nhân dòng.

**Đánh giá.** Tầng *áp dụng*. Objective gồm ba sản phẩm, trong đó cái thứ ba có tiêu chí đúng sai tuyệt đối. Đạt khi lược đồ sao cài đặt được và trả lời được năm câu hỏi phân tích, khi ma trận xe buýt chỉ ra đúng chiều dùng chung, và khi phép so hai bảng sự kiện cho kết quả khớp bản đối chứng.

**Lab.** Chuyển lược đồ chuẩn hoá 12 bảng thành lược đồ sao. Trả lời năm câu hỏi phân tích trên nó. Lập ma trận xe buýt cho ba quy trình nghiệp vụ. So sánh bảng sự kiện đơn hàng với bảng sự kiện trả hàng ở hai hạt khác nhau, đối chiếu bản đối chứng. Thử kết trực tiếp và ghi lại số dòng bị nhân.

**Pitfalls.** Kết trực tiếp hai bảng sự kiện khác hạt · chuẩn hoá chiều vì thấy dữ liệu lặp · lập ma trận xe buýt sau khi đã xây xong thay vì trước.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Lược đồ sao trả lời được năm câu hỏi, ma trận xe buýt đúng chiều dùng chung, và phép so hai bảng khớp đối chứng.

### Lesson 198 · Medallion layers - raw, cleaned, curated `LT`
**Prerequisites.** Lesson 197

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Ba lớp và trách nhiệm tách bạch của từng lớp. Lớp thô giữ nguyên như nguồn, không sửa gì, và mục đích duy nhất là tái tạo được mọi thứ phía sau từ nó; hệ quả là nó chỉ chèn thêm và không bao giờ ghi đè, nối tới lesson 206. Lớp sạch làm chuẩn hoá kiểu, chuẩn hoá giá trị rỗng, khử trùng, và áp quy tắc chất lượng; nó vẫn giữ hạt của nguồn và chưa có logic nghiệp vụ. Lớp phục vụ là nơi mô hình chiều ở bảy bài trước sống, và nó hướng người dùng dữ liệu. Ranh giới hay bị vi phạm nhất là đưa logic nghiệp vụ vào lớp sạch, làm lớp đó không dùng lại được cho mục đích khác. Ba câu hỏi để kiểm một phép biến đổi thuộc lớp nào. Quy ước đặt tên cho từng lớp. Ranh giới bàn giao với Analytics Engineer thường đặt ở cuối lớp sạch hoặc đầu lớp phục vụ, và đặt ở đâu là thoả thuận giữa hai vai trò chứ không có đáp án chung.

**Outcome.** Phân loại 15 phép biến đổi vào đúng lớp, và nêu ranh giới bàn giao phù hợp cho hai kiểu tổ chức khác nhau.

**Đánh giá.** Tầng *hiểu*. Objective là phân loại theo tiêu chí và một phán đoán về ranh giới tổ chức. Đạt khi phân loại đúng ít nhất 12 trên 15, và khi hai ranh giới bàn giao đề xuất đều nêu được hậu quả cho cả hai vai trò.

**Lab.** Nhận 15 phép biến đổi: ép kiểu ngày, khử trùng theo khoá nghiệp vụ, tính doanh thu thuần sau chiết khấu, chuẩn hoá tên tỉnh, gán phân khúc khách, và các phép khác. Phân loại vào ba lớp. Với hai kiểu tổ chức khác nhau, đề xuất ranh giới bàn giao và nêu hậu quả.

**Pitfalls.** Đưa logic nghiệp vụ vào lớp sạch · ghi đè lớp thô khi nguồn sửa dữ liệu · đặt ranh giới bàn giao mà không thoả thuận với vai trò bên kia.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân loại đúng ít nhất 12 trên 15, và hai ranh giới bàn giao đều nêu hậu quả cho cả hai vai trò.

### Lesson 199 · Data Vault at a level sufficient to recognise it `LT`
**Prerequisites.** Lesson 198

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Ba loại bảng và việc của từng cái: bảng trung tâm giữ khoá nghiệp vụ, bảng liên kết giữ quan hệ giữa các khoá, và bảng vệ tinh giữ thuộc tính kèm dấu thời gian. Mục tiêu thiết kế khác hẳn mô hình chiều: nó tối ưu cho khả năng nạp song song, khả năng kiểm toán, và khả năng thêm nguồn mới mà không sửa cấu trúc cũ, đổi lấy việc truy vấn phức tạp hơn nhiều. Hệ quả: nó không phải lớp phục vụ, nó là lớp trung gian, và vẫn cần dựng mô hình chiều lên trên để người dùng đọc được. Điều kiện một tổ chức nên cân nhắc: nhiều nguồn có khoá nghiệp vụ chồng lấn, yêu cầu kiểm toán chặt, và đội đủ lớn để chịu chi phí phức tạp. Điều kiện không nên: đội nhỏ, ít nguồn, hoặc chưa có mô hình chiều chạy được. Mức yêu cầu của bài là nhận ra một lược đồ dạng này khi gặp và nêu được ba loại bảng, không phải thiết kế một cái.

**Outcome.** Nhận ra một lược đồ dạng này khi gặp và nêu điều kiện tổ chức nào nên cân nhắc nó, cùng cái nó đánh đổi.

**Đánh giá.** Tầng *hiểu*. Objective ở mức nhận biết, vì thiết kế một lược đồ dạng này vượt phạm vi Data Engineer bàn giao dữ liệu. Đạt khi phân loại đúng ba loại bảng trong một lược đồ mẫu, và khi nêu được ba điều kiện nên và hai điều kiện không nên, mỗi cái kèm lý do.

**Lab.** Đọc một lược đồ mẫu 15 bảng và phân loại từng bảng vào ba loại. Viết một truy vấn lấy trạng thái hiện tại của một thực thể từ lược đồ đó và so độ phức tạp với truy vấn tương đương trên lược đồ sao. Viết nửa trang nêu điều kiện nên và không nên.

**Pitfalls.** Kết luận nó tốt hơn mô hình chiều · coi nó là lớp phục vụ cho người dùng cuối · đề xuất nó cho đội bốn người chưa có kho chạy được.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân loại đúng ba loại bảng trong lược đồ mẫu, và nêu ba điều kiện nên cùng hai điều kiện không nên kèm lý do.

### Lesson 200 · Modelling for handover - what the Analytics Engineer needs `TH`
**Prerequisites.** Lesson 199

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Sản phẩm bàn giao của Data Engineer là tập dữ liệu có hợp đồng, và bài này định nghĩa hợp đồng đó ở phần mô hình. Mười một khai báo mà người nhận cần, nối tới lesson 216 nơi chúng thành hợp đồng đầy đủ: hạt, khoá nghiệp vụ, lược đồ và kiểu, múi giờ, ngữ nghĩa của cập nhật và xoá, độ tươi, mức đầy đủ, mức chính xác, lineage, chủ sở hữu, và thời gian lưu giữ. Ba khai báo hay bị bỏ nhất và hậu quả: ngữ nghĩa cập nhật và xoá không rõ làm người nhận không biết dữ liệu có thay đổi hồi tố không; múi giờ không khai báo làm mọi phép gộp theo ngày lệch; và mức chính xác không nêu làm người nhận tưởng số đã đối soát. Cung cấp dữ liệu mẫu cố định cho người nhận viết kiểm thử, nối lại lesson 84. Tài liệu cột viết cho người không có ngữ cảnh. Thông báo trước khi đổi lược đồ và thời gian chuyển tiếp. Vì sao bàn giao tốt rẻ hơn nhiều so với trả lời câu hỏi lặp lại.

**Outcome.** Bàn giao một tập dữ liệu kèm mười một khai báo, và chứng minh người nhận dựng được mart lên trên mà không đặt câu hỏi nào.

**Đánh giá.** Tầng *đánh giá*. Objective đo bằng người nhận thật chứ không bằng danh sách đã điền. Kiểm bằng quan sát: một học viên khác nhận tập dữ liệu và tài liệu, dựng một mart nhỏ, ghi lại mọi câu phải hỏi. Đạt khi không quá một câu hỏi và khi mart dựng ra cho số khớp bản đối chứng.

**Lab.** Bàn giao ba bảng của lược đồ sao ở lesson 197 kèm mười một khai báo và dữ liệu mẫu cố định. Người nhận dựng một mart doanh thu theo vùng và ghi lại mọi câu hỏi. So số của mart với bản đối chứng. Sửa tài liệu theo câu hỏi rồi bàn giao lại cho người thứ hai.

**Pitfalls.** Bỏ khai báo ngữ nghĩa cập nhật và xoá · viết tài liệu cột bằng cách chép lại tên cột · bàn giao mà không kèm dữ liệu mẫu cố định.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Người nhận đặt không quá một câu hỏi và mart dựng ra khớp bản đối chứng.

### Lesson 201 · Warehouse physical design - partitioning, clustering, sort keys `TH`
**Prerequisites.** Lesson 200

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Thiết kế logic ở chín bài trước quyết định đúng đắn; thiết kế vật lý quyết định chi phí và tốc độ, và hai thứ này tách bạch được. Ba đòn bẩy và ánh xạ sang từng hệ đã học: phân vùng ở lesson 115 và 130, phân cụm hoặc khoá sắp xếp ở lesson 161 và 168, và chọn kiểu dữ liệu hẹp ở lesson 169. Chọn khoá phân vùng cho bảng sự kiện: cột ngày của sự kiện nghiệp vụ chứ không phải ngày nạp, và lý do là truy vấn lọc theo ngày nghiệp vụ. Ngoại lệ khi hai ngày lệch nhau nhiều do dữ liệu tới muộn, nối tới lesson 205. Bảng chiều thường nhỏ nên không cần phân vùng, và phát tán chúng tới mọi nút trong hệ phân tán. Nén và ảnh hưởng của thứ tự sắp xếp lên tỉ lệ nén. Đo trước khi tối ưu và đo lại sau, nối lại lesson 17. Thiết kế vật lý phụ thuộc hệ đích nên phải làm sau khi chọn hệ ở M18, không làm trước.

**Outcome.** Thiết kế vật lý cho một lược đồ sao trên hai hệ đích khác nhau, và chứng minh cải thiện bằng số đo riêng cho từng đòn bẩy.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn có đánh đổi và đo riêng từng thay đổi. Đạt khi ba đòn bẩy đều có số đo riêng trên cả hai hệ, và khi lựa chọn khoá phân vùng được biện minh bằng mẫu truy vấn chứ bằng thói quen.

**Lab.** Nạp lược đồ sao 100 triệu dòng vào hai hệ đích. Áp ba đòn bẩy từng cái một, đo sau mỗi bước trên cả hai hệ. So khoá phân vùng theo ngày nghiệp vụ với theo ngày nạp trên bộ sáu truy vấn. Đo ảnh hưởng của thứ tự sắp xếp lên tỉ lệ nén.

**Pitfalls.** Phân vùng theo ngày nạp · làm thiết kế vật lý trước khi chọn hệ đích · gộp ba đòn bẩy rồi đo một lần.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba đòn bẩy có số đo riêng trên cả hai hệ, và lựa chọn khoá phân vùng biện minh bằng mẫu truy vấn.

### Lesson 202 · Modeling and loading project `DA`
**Prerequisites.** Lesson 201

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Không có nội dung mới. Dự án gộp M19: nhận một cơ sở dữ liệu nguồn chuẩn hoá, thiết kế và cài đặt lược đồ sao đầy đủ, dựng ba lớp theo lesson 198, và bàn giao theo lesson 200. Yêu cầu đầu ra: phát biểu hạt kiểm chứng được cho mọi bảng, ít nhất một chiều thay đổi chậm loại thêm dòng mới, bảng lịch có xử lý Tết âm lịch, pipeline nạp gia tăng chạy lại được, và bộ kiểm chứng ba phép kiểm hạt ở lesson 192 chạy tự động. Tiêu chí đối soát: tổng độ đo cộng được trong bảng sự kiện khớp tổng ở nguồn cho cả ba kỳ, và chạy lại pipeline hai lần cho kết quả bằng chạy một lần.

**Outcome.** Thiết kế và cài đặt một kho dữ liệu ba lớp từ một nguồn chuẩn hoá, và chứng minh đối soát khớp cùng tính bất biến khi chạy lại.

**Đánh giá.** Tầng *sáng tạo*. Objective là thiết kế một hệ dưới nhiều ràng buộc. Chấm theo năm mục: phát biểu và kiểm chứng hạt 25đ, mô hình chiều và chiều thay đổi chậm 25đ, pipeline nạp bất biến 20đ, đối soát khớp 20đ, tài liệu bàn giao 10đ. Đạt khi ≥ 70/100 và mục đối soát ≥ 70% của nó.

**Lab.** Nhận cơ sở dữ liệu nguồn 15 bảng, 50 triệu dòng. Thiết kế lược đồ sao, cài ba lớp, viết pipeline nạp gia tăng. Chạy hai lần và đối soát. Nộp bộ kiểm chứng hạt chạy tự động và tài liệu bàn giao mười một khai báo.

**Pitfalls.** Bỏ lớp thô để tiết kiệm dung lượng · phát biểu hạt mà không viết phép kiểm tự động · đối soát một kỳ rồi kết luận.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Đạt ≥ 70/100, mục đối soát ≥ 70%, và chạy hai lần cho kết quả bằng chạy một lần.

# MODULE 20 · BATCH INGESTION, ACCURACY AND DATA QUALITY

**Lessons 203–218 · 32 giờ**

| | |
|---|---|
| **Objective cấp module** | Xây một pipeline nạp theo lô chạy lại được ngày bất kỳ cho cùng kết quả, và chứng minh nó phát hiện được dữ liệu sai thay vì chuyển tiếp âm thầm |
| **Tiền đề** | M19 |
| **Exit criterion** | Đạt Cổng 5 ≥ 70/100: xoá, nhân bản và đổi lược đồ 1% dữ liệu, pipeline phải phát hiện, cô lập, sửa và chạy bù được |
| **Kỹ năng SFIA** | `DTAN` mức 4 · `TEST` mức 4 |
| **Chế độ hỏng** | Pipeline chạy xanh mỗi ngày trong khi số liệu sai dần, vì không có phép đối soát nào với nguồn độc lập |

Module này là chỗ mọi thứ từ chặng 1 tới 3 hợp lại thành một sản phẩm chạy được. Nguyên tắc xuyên suốt: **một pipeline chưa bị phá hoại có chủ đích là một pipeline chưa biết mình hỏng thế nào**, nối lại lesson 60. Sáu bài đầu là cơ chế nạp, bốn bài giữa là chất lượng và độ chính xác, bốn bài sau là hợp đồng và vận hành, hai bài cuối là dự án và Cổng 5.

### Lesson 203 · Source types and what each one makes hard `LT`
**Prerequisites.** Module 20: M19

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Năm loại nguồn và khó khăn đặc trưng của từng loại. Cơ sở dữ liệu giao dịch: dễ đọc nhất nhưng đọc nặng ảnh hưởng hệ sản xuất, nối lại lesson 190, và không có dấu vết xoá nếu ứng dụng xoá cứng. Giao diện lập trình web: phân trang, giới hạn tốc độ và lược đồ đổi không báo, đã giải ở M4 nên bài này chỉ nhắc lại ràng buộc. Tệp trên thư mục hoặc kho đối tượng: đơn giản nhất nhưng hay thiếu tệp, trùng tệp, và tệp ghi dở bị đọc giữa chừng. Dịch vụ bên thứ ba: ít kiểm soát nhất, hạn ngạch và thay đổi không báo trước. Nhật ký ứng dụng: khối lượng lớn, hình dạng không ổn định, và thường không có khoá nghiệp vụ. Ba câu hỏi phải trả lời cho mọi nguồn trước khi viết dòng mã nào: làm sao biết có dữ liệu mới, làm sao biết dữ liệu cũ đã đổi, và làm sao biết dữ liệu đã bị xoá. Câu thứ ba hay không có câu trả lời và đó là thông tin quan trọng.

**Outcome.** Trả lời ba câu hỏi phát hiện thay đổi cho năm nguồn, và chỉ ra nguồn nào không trả lời được câu hỏi về xoá.

**Đánh giá.** Tầng *phân tích*. Objective là khảo sát có cấu trúc trước khi thiết kế. Đạt khi ba câu hỏi được trả lời cho cả năm nguồn bằng bằng chứng từ khảo sát thật, và khi ít nhất một nguồn được kết luận là không phát hiện được xoá kèm phương án bù.

**Lab.** Khảo sát năm nguồn dựng sẵn. Với mỗi nguồn, tìm cơ chế phát hiện dữ liệu mới, dữ liệu sửa, và dữ liệu xoá. Ghi lại bằng chứng: cột dấu thời gian nào, nhật ký nào, hay không có gì. Với nguồn không phát hiện được xoá, đề xuất phương án đối chiếu định kỳ.

**Pitfalls.** Giả định cột dấu thời gian cập nhật luôn được ứng dụng ghi đúng · bỏ qua câu hỏi về xoá vì nguồn không có cơ chế · đọc trực tiếp bản chính của hệ sản xuất.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba câu hỏi trả lời cho cả năm nguồn có bằng chứng, và nguồn không phát hiện được xoá có phương án bù.

### Lesson 204 · Full load against incremental - choosing a strategy `LT`
**Prerequisites.** Lesson 203

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Nạp toàn bộ đọc lại mọi thứ mỗi lần: đơn giản, tự sửa sai, và bất biến khi chạy lại theo định nghĩa; đổi lại là chi phí tỉ lệ tổng dữ liệu chứ không tỉ lệ dữ liệu mới. Nạp gia tăng chỉ đọc phần thay đổi: rẻ nhưng phải tự bảo đảm mọi tính chất mà nạp toàn bộ có sẵn. Ba chiến lược gia tăng và điều kiện áp dụng: theo con trỏ tăng dần dùng khoá hoặc dấu thời gian, theo ảnh chụp so sánh hai lần chụp, và theo bắt thay đổi từ nhật ký, cái thứ ba ở chặng 6. Quy tắc chọn không theo trực giác: bắt đầu bằng nạp toàn bộ và chỉ chuyển sang gia tăng khi đo được chi phí không chấp nhận được, vì gia tăng đổi chi phí tính toán lấy chi phí độ phức tạp và rủi ro đúng đắn. Ngưỡng chuyển thường ở đâu. Mẫu lai: gia tăng hằng ngày cộng nạp toàn bộ hằng tuần để tự sửa sai tích luỹ, mẫu rẻ và giải quyết phần lớn rủi ro của gia tăng.

**Outcome.** Chọn chiến lược nạp cho ba bảng có đặc tính khác nhau và biện minh bằng chi phí đo được chứ bằng thói quen.

**Đánh giá.** Tầng *đánh giá*. Objective đòi quyết định có đánh đổi giữa chi phí với rủi ro đúng đắn. Đạt khi ba lựa chọn đều có số đo chi phí nạp toàn bộ làm cơ sở so sánh, và khi ít nhất một bảng được kết luận là giữ nạp toàn bộ vì chi phí vẫn chấp nhận được.

**Lab.** Ba bảng: 500 nghìn dòng đổi 1% mỗi ngày, 200 triệu dòng đổi 0,1% mỗi ngày, và 5 triệu dòng đổi 60% mỗi ngày. Đo thời gian và chi phí nạp toàn bộ cho từng bảng. Chọn chiến lược. Cài mẫu lai cho bảng thứ hai và đo chi phí tuần.

**Pitfalls.** Chuyển sang gia tăng vì thấy chuyên nghiệp hơn · nạp gia tăng mà không có cơ chế tự sửa sai định kỳ · chọn chiến lược trước khi đo chi phí nạp toàn bộ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba lựa chọn có số đo chi phí nạp toàn bộ làm cơ sở, và ít nhất một bảng giữ nạp toàn bộ có lý do.

### Lesson 205 · Watermarks, cursors and the late-arriving problem `TH`
**Prerequisites.** Lesson 204

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Con trỏ là giá trị đánh dấu đã đọc tới đâu, và lưu nó ở đâu quyết định pipeline chạy lại được hay không: lưu trong bảng trạng thái riêng, không lưu trong bộ nhớ và không suy ra từ dữ liệu đích. Thời điểm cập nhật con trỏ là sau khi ghi dữ liệu thành công, không phải trước, nối lại lesson 35. Dữ liệu tới muộn là bản ghi có dấu thời gian nghiệp vụ cũ nhưng xuất hiện ở nguồn sau khi con trỏ đã vượt qua, nên lần nạp sau bỏ sót nó vĩnh viễn. Ba nguyên nhân: hệ nguồn ghi trễ, múi giờ lệch, và giao dịch dài xác nhận muộn hơn dấu thời gian của nó. Nguyên nhân thứ ba là nguyên nhân tinh vi nhất và nó xảy ra với mọi cơ sở dữ liệu. Cửa sổ nhìn lại: lùi con trỏ một khoảng mỗi lần chạy để bắt lại dữ liệu tới muộn, và điều kiện bắt buộc là phép ghi phải bất biến vì cùng bản ghi sẽ được xử lý nhiều lần, nối lại lesson 106. Chọn độ dài cửa sổ bằng đo phân bố độ trễ thật.

**Outcome.** Đo phân bố độ trễ tới muộn của một nguồn và chọn độ dài cửa sổ nhìn lại, rồi chứng minh không bỏ sót bản ghi nào.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí đối soát tuyệt đối. Đạt khi phân bố độ trễ đo được từ dữ liệu thật, và khi chạy 30 ngày mô phỏng với cửa sổ đã chọn thì tổng bản ghi đích khớp tổng nguồn, không thiếu một dòng.

**Lab.** Nguồn có 2% bản ghi tới muộn theo phân bố lệch phải. Đo phân bố độ trễ bằng cách so dấu thời gian nghiệp vụ với thời điểm xuất hiện. Chọn cửa sổ theo phân vị 99. Chạy 30 ngày mô phỏng không cửa sổ rồi có cửa sổ, đối soát cả hai. Đặt cửa sổ trên phép ghi không bất biến và quan sát nhân bản.

**Pitfalls.** Cập nhật con trỏ trước khi ghi dữ liệu · chọn cửa sổ nhìn lại bằng cảm tính · dùng cửa sổ nhìn lại với phép ghi không bất biến.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân bố độ trễ đo từ dữ liệu thật, và chạy 30 ngày với cửa sổ đã chọn cho đối soát khớp tuyệt đối.

### Lesson 206 · Immutable landing and why raw is never overwritten `TH`
**Prerequisites.** Lesson 205

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Lớp thô chỉ chèn thêm và không bao giờ sửa, và đây là ràng buộc kiến trúc chứ không phải khuyến nghị. Ba thứ nó cho phép: dựng lại mọi lớp sau từ nó khi logic biến đổi có lỗi, điều tra một số sai bằng cách xem dữ liệu đúng như nguồn gửi, và so sánh hai lần nạp để phát hiện nguồn sửa dữ liệu hồi tố. Cách tổ chức: phân vùng theo thời điểm nạp chứ không theo thời gian nghiệp vụ, vì mục đích là truy vết lần nạp. Đặt tên đối tượng gồm nguồn, thời điểm nạp, và mã lần chạy, để truy được dòng dữ liệu về lần chạy sinh ra nó, nối lại lesson 89. Giữ nguyên định dạng nguồn hay chuyển sang định dạng cột: đánh đổi giữa trung thực với chi phí lưu trữ, và mẫu thường dùng là giữ nguyên bản một thời gian ngắn rồi chuyển. Siêu dữ liệu lần nạp ghi kèm: số bản ghi, tổng kiểm tra, thời điểm bắt đầu và kết thúc. Thời gian lưu giữ lớp thô và chi phí, cùng lý do cắt nó là quyết định phải cân nhắc kỹ.

**Outcome.** Tổ chức lớp thô sao cho truy được một dòng ở lớp phục vụ về đúng tệp và lần chạy sinh ra nó, và dựng lại được lớp sau từ lớp thô.

**Đánh giá.** Tầng *áp dụng*. Objective có hai tiêu chí kiểm bằng thực nghiệm. Đạt khi chọn 10 dòng ngẫu nhiên ở lớp phục vụ và truy được cả 10 về đúng tệp thô và mã lần chạy, và khi xoá sạch lớp sau rồi dựng lại từ lớp thô cho kết quả khớp từng dòng.

**Lab.** Dựng lớp thô có quy ước đặt tên và siêu dữ liệu lần nạp. Chạy 10 lần nạp. Chọn 10 dòng ngẫu nhiên ở lớp phục vụ và truy ngược. Xoá lớp sạch và lớp phục vụ, dựng lại hoàn toàn từ lớp thô, đối chiếu. So hai lần nạp của cùng một ngày để phát hiện nguồn sửa hồi tố.

**Pitfalls.** Ghi đè tệp thô khi nạp lại cùng ngày · phân vùng lớp thô theo thời gian nghiệp vụ · bỏ siêu dữ liệu lần nạp vì thấy thừa.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Truy được cả 10 dòng về đúng tệp và lần chạy, và dựng lại lớp sau từ lớp thô khớp từng dòng.

### Lesson 207 · Atomic publish and the partially-written table `TH`
**Prerequisites.** Lesson 206

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Người đọc không bao giờ được thấy trạng thái nửa chừng, và ba mẫu đạt được điều đó. Ghi ra vị trí tạm rồi đổi tên hoặc hoán đổi, cùng ý tưởng với lesson 16 nhưng ở mức bảng. Ghi vào bảng bóng rồi hoán đổi bí danh, mẫu dùng ở lesson 181. Ghi trong một giao dịch khi hệ đích hỗ trợ, đơn giản nhất nhưng giới hạn bởi kích thước giao dịch. Với bảng phân vùng, hoán đổi ở mức phân vùng thay vì cả bảng, rẻ hơn nhiều bậc và là mẫu mặc định cho nạp hằng ngày, nối lại lesson 130. Cửa sổ không nguyên tử còn lại trong từng mẫu và cách đo nó. Người đọc đang chạy lúc hoán đổi: một số hệ cho truy vấn đang chạy đọc tiếp bản cũ, một số huỷ nó, và phải kiểm chứ không giả định. Thứ tự khi ghi nhiều bảng phụ thuộc nhau: công bố bảng chiều trước bảng sự kiện, nếu không thì có khoảng thời gian bảng sự kiện tham chiếu chiều chưa tồn tại.

**Outcome.** Cài công bố nguyên tử cho một bảng phân vùng, và chứng minh người đọc không bao giờ thấy trạng thái nửa chừng dưới tải đọc liên tục.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí kiểm bằng thực nghiệm lặp lại. Đạt khi chạy 50 lần công bố trong lúc có tải đọc liên tục mà không lần nào người đọc thấy số dòng bất thường, và khi thứ tự công bố bảng chiều trước bảng sự kiện được chứng minh cần thiết bằng một ca làm ngược.

**Lab.** Bảng phân vùng có tải đọc đếm số dòng mỗi 100 mili giây. Công bố một phân vùng 50 lần bằng ba mẫu khác nhau, ghi lại mọi số dòng bất thường người đọc thấy. Công bố bảng sự kiện trước bảng chiều một lần và ghi lại lỗi khoá ngoại hoặc dòng mồ côi.

**Pitfalls.** Xoá rồi chèn ngoài giao dịch · hoán đổi cả bảng khi chỉ đổi một phân vùng · công bố bảng sự kiện trước bảng chiều.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** 50 lần công bố không lần nào người đọc thấy số dòng bất thường, và ca công bố sai thứ tự được chứng minh gây lỗi.

### Lesson 208 · Deduplication and the business key `TH`
**Prerequisites.** Lesson 207

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Trùng lặp đến từ bốn nguồn khác nhau và mỗi nguồn cần cách xử lý khác: nguồn gửi lại do thử lại, pipeline chạy lại do lỗi, cửa sổ nhìn lại ở lesson 205, và nguồn thật sự có bản ghi trùng. Ba loại trùng theo mức độ giống nhau: trùng toàn bộ cột, trùng khoá nghiệp vụ nhưng khác nội dung, và trùng mờ do khác biểu diễn chuỗi, nối lại lesson 8. Khoá nghiệp vụ là khoá định danh thực thể theo nghĩa nghiệp vụ, khác khoá kỹ thuật của hệ nguồn; xác định nó đúng là điều kiện để khử trùng đúng, và nó phải hỏi người hiểu nghiệp vụ chứ không suy từ dữ liệu. Quy tắc giữ dòng nào khi trùng khoá nhưng khác nội dung phải khai báo rõ: giữ bản mới nhất theo cột nào, và cột đó có đáng tin không. Khử trùng ở đâu trong đường ống: ở lớp sạch chứ không ở lớp thô, vì lớp thô phải giữ nguyên như nguồn. Đếm và ghi nhật ký số bản ghi bị loại.

**Outcome.** Khử trùng một tập có đủ bốn nguồn trùng lặp, khai báo rõ khoá nghiệp vụ và quy tắc giữ dòng, và đếm được số bản ghi bị loại theo từng loại.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí đối soát và một yêu cầu khai báo. Đạt khi tổng bản ghi vào bằng bản ghi ra cộng bản ghi bị loại theo từng loại, và khi quy tắc giữ dòng được khai báo bằng văn bản và cho kết quả khớp bản đối chứng.

**Lab.** Tập 5 triệu bản ghi có đủ bốn nguồn trùng. Xác định khoá nghiệp vụ bằng khảo sát và hỏi mô tả nghiệp vụ. Khử trùng theo ba loại, đếm riêng từng loại. Đối soát phép cộng. So kết quả với bản đối chứng. Thử khử trùng ở lớp thô và chỉ ra nó phá vỡ tính tái tạo.

**Pitfalls.** Suy khoá nghiệp vụ từ dữ liệu mà không hỏi · khử trùng ở lớp thô · giữ bản mới nhất theo cột dấu thời gian mà chưa kiểm cột đó có đáng tin không.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phép cộng đối soát khớp theo từng loại trùng, và quy tắc giữ dòng khai báo bằng văn bản cho kết quả khớp đối chứng.

### Lesson 209 · Schema evolution at the ingestion boundary `TH`
**Prerequisites.** Lesson 208

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Lược đồ nguồn đổi là chuyện chắc chắn xảy ra, nên pipeline phải có hành vi khai báo trước cho từng loại thay đổi thay vì vỡ theo cách ngẫu nhiên. Sáu loại thay đổi và mức nghiêm trọng: thêm cột tuỳ chọn tương thích ngược, thêm cột bắt buộc phá vỡ, xoá cột phá vỡ, đổi kiểu phá vỡ, đổi tên là xoá cộng thêm nên phá vỡ, và đổi ngữ nghĩa mà không đổi cấu trúc là loại nguy hiểm nhất vì không có tín hiệu kỹ thuật nào. Ba chiến lược khi nguồn thêm cột và tiêu chí chọn: bỏ qua cột mới giữ pipeline ổn định nhưng mất dữ liệu, tự thêm vào đích giữ được dữ liệu nhưng lược đồ đích trôi dần, và dừng và báo an toàn nhất nhưng gây gián đoạn. Lựa chọn phụ thuộc lớp: lớp thô nên nhận tất cả, lớp sạch nên dừng và báo. Kiểm lược đồ ở biên nhận, nối lại lesson 87. Đối chiếu lược đồ nguồn theo lịch để phát hiện thay đổi trước khi nó gây lỗi.

**Outcome.** Khai báo hành vi cho sáu loại thay đổi lược đồ và chứng minh pipeline phản ứng đúng như khai báo cho cả sáu.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí kiểm bằng thực nghiệm đầy đủ. Đạt khi sáu loại thay đổi đều cho hành vi đúng như bảng khai báo, và khi loại đổi ngữ nghĩa được phát hiện bằng một phép kiểm phân bố chứ không bằng kiểm lược đồ.

**Lab.** Lập bảng khai báo hành vi cho sáu loại thay đổi ở hai lớp. Cài kiểm lược đồ ở biên. Bơm sáu thay đổi vào nguồn, ghi lại hành vi thật của pipeline. Với loại đổi ngữ nghĩa, thêm phép kiểm phân bố giá trị và xác nhận nó bắt được.

**Pitfalls.** Tự thêm cột mới vào lớp sạch · coi đổi tên cột là thay đổi nhỏ · không có phép kiểm nào cho loại đổi ngữ nghĩa.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Sáu loại thay đổi cho hành vi đúng như bảng khai báo, và loại đổi ngữ nghĩa bắt được bằng kiểm phân bố.

### Lesson 210 · Backfill and replay without double counting `TH`
**Prerequisites.** Lesson 209

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Chạy bù là chạy lại một dải thời gian trong quá khứ, và nó chỉ an toàn khi phép ghi bất biến, nối lại lesson 106 và 205. Ba câu hỏi trước mỗi lần chạy bù: các ngày độc lập hay phụ thuộc thứ tự, chạy được mấy ngày cùng lúc mà hệ đích chịu được, và logic mới có tương thích dữ liệu cũ không. Câu thứ ba hay bị bỏ: chạy bù bằng mã hiện tại lên dữ liệu ba tháng trước có thể cho kết quả khác với lúc đó nếu logic đã đổi, và đó có thể đúng ý hoặc không, nên phải quyết định rõ. Phát lại là chạy lại từ lớp thô khi phát hiện lỗi logic biến đổi, khác chạy bù ở chỗ nguồn là lớp thô chứ không phải hệ nguồn. Đây là lý do lớp thô ở lesson 206 tồn tại. Đánh dấu dữ liệu đã chạy bù để người dùng biết số lịch sử vừa đổi, và thông báo cho người đã dùng số cũ. Chạy bù một phần đồ thị phụ thuộc thay vì toàn bộ.

**Outcome.** Chạy bù 90 ngày cho một bảng có mô hình chiều thay đổi chậm, và chứng minh kết quả khớp bản chạy tuần tự từng ngày.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí đối chứng tuyệt đối trên một ca khó, vì chiều thay đổi chậm làm chạy bù phụ thuộc thứ tự. Đạt khi bảng sau chạy bù khớp từng dòng với bản đối chứng, và khi người học chỉ ra được vì sao ngày không độc lập trong ca này.

**Lab.** Sinh bản đối chứng bằng cách chạy tuần tự 90 ngày. Xoá bảng đích. Chạy bù 90 ngày. Đối chiếu từng dòng. Thử chạy bù song song và ghi lại sai lệch do chiều thay đổi chậm. Chạy phát lại từ lớp thô sau khi sửa một lỗi logic, so với chạy bù từ nguồn.

**Pitfalls.** Chạy bù song song các ngày cho bảng có chiều thay đổi chậm · chạy bù bằng logic mới mà không quyết định rõ có muốn thế không · quên thông báo cho người đã dùng số cũ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng sau chạy bù khớp từng dòng với bản đối chứng, và lý do ngày không độc lập được chỉ ra.

### Lesson 211 · Six dimensions of data quality and one that needs an oracle `LT`
**Prerequisites.** Lesson 210

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Sáu chiều và một truy vấn đo cho từng chiều: đầy đủ đo tỉ lệ giá trị có mặt và tỉ lệ bản ghi nhận được so với kỳ vọng, duy nhất đo trùng lặp theo khoá nghiệp vụ, hợp lệ đo tuân thủ định dạng và dải giá trị, nhất quán đo mâu thuẫn giữa các cột và giữa các bảng, kịp thời đo độ trễ so với cam kết, và chính xác đo khớp với thực tế. Chiều chính xác khác năm chiều còn lại về bản chất: năm chiều đầu đo được bằng quy tắc nội bộ, còn chính xác cần một nguồn đối chứng bên ngoài. Hệ quả: một bảng có thể đạt năm chiều mà vẫn sai hoàn toàn, và đây là chỗ nhiều hệ thống chất lượng dữ liệu dừng lại rồi tạo cảm giác an toàn giả. Ba loại nguồn đối chứng khả dụng: hệ thống độc lập đo cùng đại lượng, báo cáo do người khác lập, và xác nhận thủ công trên mẫu. Nói rõ chiều nào đang đo được và chiều nào chưa là yêu cầu của module.

**Outcome.** Đo sáu chiều cho một bảng và phát biểu rõ chiều chính xác đang được đo bằng nguồn nào hoặc chưa đo được.

**Đánh giá.** Tầng *hiểu*. Objective gồm đo và một phán đoán về giới hạn phép đo. Đạt khi sáu chiều đều có số, và khi phần về chiều chính xác nêu rõ nguồn đối chứng cụ thể hoặc tuyên bố chưa đo được kèm lý do. Báo cáo đủ sáu số mà nói chính xác đạt nhờ quy tắc nội bộ là không đạt.

**Lab.** Bảng 10 triệu dòng. Viết truy vấn đo cho từng chiều trong sáu chiều. Chạy và lập báo cáo có số. Tìm một nguồn đối chứng độc lập cho một đại lượng và đo chiều chính xác. Với hai đại lượng không có nguồn đối chứng, viết rõ là chưa đo được.

**Pitfalls.** Đo chiều chính xác bằng quy tắc nội bộ · gộp chiều hợp lệ với chiều chính xác · báo cáo chất lượng đạt khi năm chiều xanh mà chưa đối soát.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Sáu chiều đều có số, và phần chiều chính xác nêu rõ nguồn đối chứng hoặc tuyên bố chưa đo được kèm lý do.

### Lesson 212 · Accuracy - reconciliation against an independent source `TH`
**Prerequisites.** Lesson 211

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Đối soát là phép so một đại lượng tính bằng hai đường độc lập, và nó là cách duy nhất đo được chiều chính xác ở lesson 211. Bốn kỹ thuật và cái mỗi cái bắt: tổng kiểm tra số bản ghi bắt mất và thừa dòng, tổng theo khoá nghiệp vụ bắt sai giá trị, kiểm tra biên bắt giá trị ngoài dải, và kiểm tra thứ nguyên bắt sai đơn vị. Đối soát nguồn tới đích theo từng chặng thay vì chỉ ở cuối, để định vị được chặng nào làm sai. Ngưỡng chấp nhận và vì sao ngưỡng bằng không thường không thực tế cho dữ liệu có tới muộn, nối lại lesson 205; cách đặt ngưỡng theo phân bố chênh lệch lịch sử. Chênh lệch nhỏ tích luỹ theo thời gian và cách phát hiện bằng theo dõi xu hướng thay vì theo dõi giá trị tuyệt đối. Ba nguyên nhân chênh lệch thường gặp: khác định nghĩa giữa hai hệ, khác thời điểm chốt, và thật sự mất dữ liệu; phân biệt ba cái này trước khi kết luận.

**Outcome.** Đối soát một đại lượng qua ba chặng của pipeline, và truy một chênh lệch về đúng một trong ba nguyên nhân.

**Đánh giá.** Tầng *phân tích*. Objective là chẩn đoán phân biệt ba nguyên nhân có cùng triệu chứng. Kiểm bằng ba ca chênh lệch dựng sẵn; đạt khi truy đúng cả ba và mỗi lần dẫn được bằng chứng định lượng, không chấp nhận kết luận mất dữ liệu khi chưa loại trừ hai nguyên nhân kia.

**Lab.** Cài đối soát bốn kỹ thuật ở ba chặng của pipeline. Bơm ba chênh lệch: một do định nghĩa khác giữa hai hệ, một do thời điểm chốt lệch, và một do mất dữ liệu thật. Với mỗi ca, truy nguyên nhân và dẫn bằng chứng. Đặt ngưỡng chấp nhận từ phân bố chênh lệch 30 ngày lịch sử.

**Pitfalls.** Kết luận mất dữ liệu ngay khi thấy chênh lệch · đối soát chỉ ở cuối pipeline · đặt ngưỡng bằng không cho nguồn có dữ liệu tới muộn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Truy đúng cả ba nguyên nhân có bằng chứng định lượng, và ngưỡng đặt từ phân bố lịch sử.

### Lesson 213 · Quality rules, thresholds and where to put them `TH`
**Prerequisites.** Lesson 212

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba vị trí đặt phép kiểm và cái mỗi vị trí bắt: ở biên nhận bắt dữ liệu nguồn sai trước khi nó vào hệ, giữa các lớp bắt lỗi logic biến đổi, và ở đầu ra bắt lỗi tổng hợp trước khi tới người dùng. Đặt cả ba là lý tưởng nhưng tốn, nên phải chọn theo rủi ro. Phép kiểm chặn so với phép kiểm cảnh báo: cái đầu dừng pipeline, cái sau ghi nhận và chạy tiếp; chọn sai theo hướng nào cũng có hại. Đặt mọi phép kiểm là chặn làm pipeline dừng vì một cảnh báo nhỏ, đặt mọi phép kiểm là cảnh báo làm chúng bị bỏ qua sau hai tuần, nối lại lesson 80. Tiêu chí phân loại: dừng khi dữ liệu sai gây hại nhiều hơn dữ liệu trễ. Ngưỡng cố định so với ngưỡng động theo lịch sử, và vì sao ngưỡng cố định luôn hoặc quá nhạy hoặc quá điếc. Phép kiểm cũng cần được kiểm: một phép kiểm chưa bao giờ đỏ có thể là phép kiểm sai chứ không phải dữ liệu hoàn hảo.

**Outcome.** Phân loại 15 phép kiểm thành chặn hay cảnh báo và đặt vào đúng vị trí, rồi chứng minh mỗi phép kiểm bắt được lỗi nó nhắm tới.

**Đánh giá.** Tầng *đánh giá*. Objective đòi hai quyết định có đánh đổi, cộng một yêu cầu chứng minh. Đạt khi 15 phép kiểm đều có vị trí và mức nghiêm trọng kèm lý do, và khi bơm lỗi tương ứng làm ít nhất 13 phép kiểm đỏ đúng như thiết kế.

**Lab.** Nhận 15 phép kiểm. Phân loại và đặt vị trí cho từng cái. Với mỗi phép kiểm, bơm đúng loại lỗi nó nhắm tới và xác nhận nó đỏ. Đặt ngưỡng động từ 30 ngày lịch sử cho ba phép kiểm và so tỉ lệ báo động giả với ngưỡng cố định.

**Pitfalls.** Đặt mọi phép kiểm là chặn · dùng ngưỡng cố định cho chỉ số có mùa vụ · tin một phép kiểm chưa bao giờ đỏ là dấu hiệu tốt.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** 15 phép kiểm có vị trí và mức nghiêm trọng kèm lý do, và ít nhất 13 phép kiểm đỏ đúng khi bơm lỗi tương ứng.

### Lesson 214 · Quarantine, alerting and the silent-drop ban `TH`
**Prerequisites.** Lesson 213

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Nguyên tắc cứng của module: không bản ghi nào bị loại trong im lặng. Mọi bản ghi không qua được phép kiểm phải đi vào bảng cách ly kèm lý do, mã lần chạy, và bản ghi gốc nguyên vẹn, để sau đó sửa và nạp lại được. Phép cộng bắt buộc: tổng bản ghi vào bằng bản ghi sạch cộng bản ghi cách ly, không sai một dòng, nối lại lesson 65. Quy trình xử lý bảng cách ly: ai xem, bao lâu một lần, và cách nạp lại sau khi sửa; bảng cách ly không có người xem là bảng cách ly vô dụng. Cảnh báo phải nói được ba thứ: cái gì hỏng, ảnh hưởng tới ai, và bước đầu tiên nên làm, nối lại lesson 80. Gom cảnh báo cùng nguyên nhân thay vì gửi một cảnh báo cho mỗi bản ghi. Chỉ cảnh báo thứ người trực làm được gì đó; phần còn lại ghi vào báo cáo. Đo tỉ lệ cách ly theo thời gian như một chỉ số sức khoẻ nguồn.

**Outcome.** Cài cơ chế cách ly và chứng minh phép cộng khớp tuyệt đối, cùng một quy trình xử lý bảng cách ly có người thực hiện được.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí đối soát tuyệt đối cộng một tiêu chí về quy trình. Đạt khi phép cộng khớp trên tập có 8% bản ghi hỏng theo sáu kiểu, và khi một học viên khác theo quy trình sửa và nạp lại được ít nhất 90% bản ghi cách ly.

**Lab.** Tập 3 triệu bản ghi có 8% hỏng theo sáu kiểu. Cài cách ly kèm lý do và bản ghi gốc. Đối soát phép cộng. Viết quy trình xử lý. Đưa bảng cách ly và quy trình cho học viên khác, đo tỉ lệ họ sửa và nạp lại được. Viết ba cảnh báo mẫu đủ ba thứ.

**Pitfalls.** Loại bản ghi hỏng mà chỉ ghi số lượng · cách ly mà không giữ bản ghi gốc nên không sửa lại được · gửi một cảnh báo cho mỗi bản ghi hỏng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phép cộng khớp tuyệt đối, và học viên khác sửa cùng nạp lại được ít nhất 90% bản ghi cách ly theo quy trình.

### Lesson 215 · Distribution drift and detecting change that breaks nothing `TH`
**Prerequisites.** Lesson 214

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Loại lỗi nguy hiểm nhất là loại không làm gì hỏng: lược đồ đúng, ràng buộc đạt, phép kiểm xanh, nhưng phân bố dữ liệu đã đổi và số liệu không còn nghĩa như trước. Bốn ví dụ: một kênh bán hàng ngừng gửi dữ liệu nên tổng giảm mà không ai báo, mã trạng thái mới xuất hiện và rơi vào nhánh mặc định, đơn vị tiền tệ đổi mà cột không đổi, và tỉ lệ giá trị rỗng của một cột tăng từ 1% lên 40%. Bốn phép đo phát hiện trôi: phân bố tần suất của cột phân loại, phân vị của cột số, tỉ lệ giá trị rỗng, và số bản ghi theo nhóm nguồn. So với cửa sổ lịch sử thay vì với ngưỡng cố định. Phân biệt trôi thật với biến động mùa vụ, và đây là chỗ cần dữ liệu lịch sử đủ dài. Cảnh báo trôi nên là cảnh báo chứ không phải chặn, vì trôi có thể là thay đổi nghiệp vụ hợp lệ, và người phán đoán là người hiểu nghiệp vụ.

**Outcome.** Cài bốn phép đo trôi và phát hiện được bốn loại thay đổi âm thầm, phân biệt được với biến động mùa vụ.

**Đánh giá.** Tầng *phân tích*. Objective đòi phân biệt tín hiệu thật với nhiễu mùa vụ, việc khó hơn đặt ngưỡng. Đạt khi phát hiện được cả bốn loại thay đổi bơm vào, và khi ba biến động mùa vụ cố ý không gây cảnh báo giả.

**Lab.** Dữ liệu 18 tháng có mùa vụ theo tuần và theo Tết. Cài bốn phép đo trôi so với cửa sổ lịch sử. Bơm bốn loại thay đổi âm thầm vào các thời điểm khác nhau. Đếm số phát hiện đúng và số báo động giả trong ba kỳ mùa vụ cao điểm.

**Pitfalls.** Dùng ngưỡng cố định cho chỉ số có mùa vụ · đặt cảnh báo trôi là chặn · so với tuần trước thay vì với cùng kỳ năm trước cho dữ liệu có mùa vụ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phát hiện cả bốn loại thay đổi bơm vào, và ba kỳ mùa vụ không sinh báo động giả.

### Lesson 216 · The pipeline contract - eleven declarations `TH`
**Prerequisites.** Lesson 215

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hợp đồng của một pipeline là tài liệu người tiêu thụ dựa vào để dùng dữ liệu đúng, và mười một khai báo ở lesson 200 giờ được hoàn thiện bằng số đo từ chín bài vừa qua. Hạt và khoá nghiệp vụ từ lesson 192 và 208. Lược đồ và hành vi khi nó đổi từ lesson 209. Múi giờ từ lesson 9. Ngữ nghĩa cập nhật và xoá từ lesson 203. Độ tươi phát biểu bằng cam kết cụ thể có giờ chứ không bằng tính từ. Mức đầy đủ và mức chính xác bằng số đo từ lesson 211 và 212, kèm nguồn đối chứng. Lineage từ lesson 206. Chủ sở hữu là một người có tên chứ không phải một nhóm. Thời gian lưu giữ. Quy trình thông báo khi hợp đồng đổi và thời gian chuyển tiếp. Hợp đồng đặt cạnh mã và kiểm trong tích hợp liên tục, nối lại lesson 87 và 90. Vì sao hợp đồng viết xong rồi để đó thì vô dụng: nó phải có phép kiểm tự động, nếu không nó chỉ là lời hứa.

**Outcome.** Viết hợp đồng đủ mười một khai báo cho một pipeline, và gắn phép kiểm tự động cho ít nhất tám khai báo.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí đếm được và một yêu cầu về tính thực thi. Đạt khi mười một khai báo đều có nội dung cụ thể có số, và khi ít nhất tám khai báo có phép kiểm chạy trong tích hợp liên tục và đỏ đúng khi vi phạm.

**Lab.** Viết hợp đồng cho pipeline đơn hàng. Với mỗi khai báo, gắn một phép kiểm tự động nếu làm được, hoặc ghi rõ vì sao không. Vi phạm tám khai báo có phép kiểm và xác nhận từng cái đỏ. Đưa hợp đồng cho một học viên khác đóng vai người tiêu thụ và ghi lại câu hỏi phát sinh.

**Pitfalls.** Phát biểu độ tươi bằng tính từ · ghi chủ sở hữu là tên nhóm · viết hợp đồng mà không có phép kiểm tự động nào.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mười một khai báo đều có nội dung cụ thể có số, và ít nhất tám khai báo có phép kiểm đỏ đúng khi vi phạm.

### Lesson 217 · Batch platform v1 - end to end `DA`
**Prerequisites.** Lesson 216

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Không có cơ chế mới. Dự án gộp M20 và nó là sản phẩm đầu tiên của chương trình có đủ hình dạng một hệ thống thật. Yêu cầu: nạp từ PostgreSQL và một giao diện lập trình web vào lớp thô bất biến, qua lớp sạch có khử trùng và phép kiểm, tới lớp phục vụ theo mô hình chiều ở M19. Kèm theo: bản kê từng lô có số bản ghi và tổng kiểm tra, bộ phép kiểm ba vị trí ở lesson 213, bảng cách ly ở lesson 214, đối soát ba chặng ở lesson 212, hợp đồng mười một khai báo ở lesson 216, và sổ tay xử lý theo khuôn lesson 90. Tiêu chí bắt buộc: chạy lại ngày bất kỳ cho cùng kết quả, và phép cộng vào bằng sạch cộng cách ly khớp tuyệt đối ở mọi lô.

**Outcome.** Xây một nền tảng nạp theo lô đầu cuối, và chứng minh chạy lại ngày bất kỳ cho cùng kết quả cùng phép cộng đối soát khớp ở mọi lô.

**Đánh giá.** Tầng *sáng tạo*. Objective là dựng một hệ thống dưới nhiều ràng buộc đồng thời. Chấm theo sáu mục: tính bất biến khi chạy lại 25đ, đối soát ba chặng 20đ, cách ly và phép cộng 20đ, hợp đồng và phép kiểm 15đ, mô hình chiều 10đ, sổ tay 10đ. Đạt khi ≥ 70/100 và hai mục đầu đều ≥ 70% của chúng.

**Lab.** Nguồn 20 triệu dòng có 5% bản ghi hỏng và 2% tới muộn. Xây đủ ba lớp. Chạy 30 ngày mô phỏng. Chọn ngẫu nhiên 5 ngày và chạy lại, đối chiếu từng dòng. Kiểm phép cộng ở cả 30 lô. Nộp hợp đồng, sổ tay và báo cáo đối soát.

**Pitfalls.** Bỏ lớp thô để pipeline gọn hơn · đối soát một lần ở cuối · chạy lại một ngày rồi kết luận bất biến.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Đạt ≥ 70/100, hai mục đầu ≥ 70%, và 5 ngày chạy lại ngẫu nhiên đều khớp từng dòng.

### Lesson 218 · Gate 5 - break the data, prove you catch it `KT`
**Prerequisites.** Lesson 217

**In-class (120 phút).** 75 phút làm bài độc lập · 45 phút chữa bài và phân tích lỗi theo nhóm

**Learn.** Không có nội dung mới. Cổng 5 đóng chặng 4, và nó đo đúng một thứ: pipeline có phát hiện được khi dữ liệu sai hay không.

**Outcome.** Nhận một pipeline bị phá hoại theo ba cách trên 1% dữ liệu, phát hiện cả ba, cô lập phạm vi ảnh hưởng, sửa, và chạy bù, rồi chứng minh kết quả cuối khớp bản đối chứng.

**Đánh giá.** Tầng *đánh giá*. Cổng đo năng lực phát hiện và phục hồi, không đo năng lực xây. Thang điểm: A 30đ phát hiện cả ba loại phá hoại · B 20đ định vị phạm vi ảnh hưởng bằng lineage · C 20đ chạy bù cho kết quả khớp đối chứng · D 15đ thông báo cho người đã dùng số sai · E 15đ phép kiểm bổ sung để lần sau bắt sớm hơn. Đạt khi ≥ 70/100 và phần A ≥ 60%. Phần D nặng hơn vẻ ngoài vì nó là phần hay bị bỏ nhất.

**Lab.** 180 phút. Giám khảo xoá 1% bản ghi, nhân bản 1% bản ghi, và đổi lược đồ một cột ở nguồn, không báo trước làm gì và làm lúc nào. Nộp: thời điểm phát hiện từng loại, phạm vi ảnh hưởng, kết quả sau chạy bù đối chiếu bản đối chứng, thông báo gửi người dùng, và phép kiểm bổ sung.

**Pitfalls.** Phát hiện được mà không định vị được phạm vi · chạy bù xong không đối chiếu · bỏ phần thông báo vì đã sửa xong.

**Self-study (2,4 giờ).** Không có bài tự học. Nếu không đạt, theo phụ lục khắc phục khi không đạt cổng

**Done when.** Đạt ≥ 70/100 và phần A ≥ 60%.

# MODULE 21 · ORCHESTRATION FOUNDATIONS

**Lessons 219–224 · 12 giờ**

| | |
|---|---|
| **Objective cấp module** | Phát biểu một bài toán điều phối bằng từ vựng đồ thị, máy trạng thái và ngày logic, trước khi mở bất kỳ công cụ nào |
| **Tiền đề** | M20 |
| **Exit criterion** | Nhận sáu tình huống hỏng của một hệ chạy bằng cron, định vị đúng cơ chế cho cả sáu và nêu công cụ điều phối giải nó bằng cách nào |
| **Kỹ năng SFIA** | `PROG` mức 3 · `SYSP` mức 3 |
| **Chế độ hỏng** | Học thẳng vào công cụ, rồi coi mọi vấn đề điều phối là vấn đề cấu hình, nên đổi công cụ mà lỗi vẫn còn |

Module không mở công cụ nào. Nó dựng từ vựng để ba module công cụ sau có cái mà so sánh, và để M25 chấm được bằng tiêu chí thay vì bằng cảm nhận. Không có module này thì M25 tụt xuống thành bài liệt kê tính năng.

**Pipeline tham chiếu.** M22, M23 và M24 dựng lại cùng một pipeline: nạp từ PostgreSQL và một giao diện lập trình web có phân trang, ghi vào kho đối tượng, biến đổi, nạp lớp phục vụ, có phép kiểm chất lượng. Đó chính là nền tảng theo lô đã xây ở lesson 217. Cùng dữ liệu, cùng lỗi cài sẵn, cùng kịch bản giết tiến trình. Không cùng bài toán thì M25 không đo được gì.

### Lesson 219 · Why an orchestrator exists - cron and the failures it cannot handle `LT`
**Prerequisites.** Module 21: M20

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Cron biểu diễn được đúng một thứ: chạy lệnh này vào thời điểm này. Sáu tình huống nó không biểu diễn được, mỗi tình huống kèm hậu quả quan sát được trên pipeline ở lesson 217. Một là phụ thuộc: bước biến đổi phải chờ bước nạp xong, mà cron không biết bước nạp đã xong chưa nên chỉ đoán bằng cách đặt giờ muộn hơn, và cách đoán đó hỏng ngay khi nguồn chậm một lần. Hai là chồng lần chạy: lần chạy hai giờ chưa xong thì lần ba giờ đã khởi động, hai tiến trình cùng ghi một bảng, nối lại lesson 207. Ba là thử lại: cron không có khái niệm thất bại tạm thời. Bốn là chạy bù: mất ba ngày dữ liệu thì không có cách nào bảo cron chạy lại đúng ba ngày đó theo thứ tự, nối lại lesson 210. Năm là khả năng quan sát. Sáu là trạng thái: cron không biết lần chạy trước dừng ở đâu. Phân biệt lập lịch với điều phối: lập lịch trả lời khi nào, điều phối trả lời theo thứ tự nào và nếu hỏng thì sao.

**Outcome.** Định vị trong sáu tình huống cái nào gây ra một sự cố cho trước, dựa vào nhật ký và bảng kết quả chứ vào phỏng đoán.

**Đánh giá.** Tầng *phân tích*. Bài mở module, người học đã vận hành pipeline từ M20 nên có kinh nghiệm để soi lại, nhưng chưa có công cụ điều phối nào. Objective dừng ở phân rã một sự cố về đúng cơ chế. Kiểm bằng sáu hồ sơ sự cố có nhật ký và ảnh chụp bảng; đạt khi định vị đúng ít nhất năm và mỗi lần dẫn được bằng chứng, không chấp nhận đoán đúng mà không dẫn.

**Lab.** Chạy nền tảng lesson 217 bằng cron trong môi trường mô phỏng 30 ngày có sự cố. Nhận sáu hồ sơ sự cố. Với mỗi hồ sơ, chỉ ra tình huống nào trong sáu, dẫn dòng nhật ký hoặc số liệu làm bằng chứng, và nêu cron thiếu khả năng gì.

**Pitfalls.** Quy mọi sự cố về mã pipeline sai thay vì về cách nó được gọi · nhầm hai tiến trình chồng nhau với lỗi khoá của kho · cho rằng đặt giờ muộn hơn là cách giải quyết phụ thuộc.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Định vị đúng ít nhất năm trên sáu hồ sơ, mỗi lần dẫn được nhật ký hoặc số liệu làm bằng chứng.

### Lesson 220 · DAG, task dependency and the state machine of a run `LT`
**Prerequisites.** Lesson 219

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Đồ thị có hướng không chu trình làm mô hình cho công việc: đỉnh là một đơn vị chạy được, cạnh là quan hệ phải xong trước. Điều kiện phi chu trình và chuyện gì xảy ra khi đồ thị có chu trình lọt vào công cụ. Sắp xếp tô pô và lý do có nhiều thứ tự chạy hợp lệ cho cùng một đồ thị, từ đó suy ra chỗ chạy song song được. Đường găng: chuỗi dài nhất quyết định thời gian chạy tối thiểu, nên tối ưu một đỉnh không nằm trên đường găng không rút ngắn được gì, nối lại định luật Amdahl ở lesson 50. Máy trạng thái của một lần chạy: chờ lịch, đã xếp hàng, đang chạy, thành công, thất bại, chờ thử lại, bỏ qua, hết hạn; chuyển trạng thái nào hợp lệ và chuyển nào thì không. Phân biệt trạng thái một đỉnh với trạng thái cả lần chạy, và bốn quy tắc gộp thường gặp. Kích thước một đỉnh là quyết định thiết kế: đỉnh quá nhỏ thì chi phí điều phối lấn át, quá lớn thì hỏng phải chạy lại nhiều.

**Outcome.** Vẽ đồ thị phụ thuộc của nền tảng ở lesson 217, chỉ ra đường găng, và liệt kê các nhóm chạy song song được.

**Đánh giá.** Tầng *áp dụng*. Objective là thực hiện một thủ tục xác định trên hệ thống của chính mình. Đạt khi đồ thị phi chu trình, đường găng chỉ ra đúng với đồ thị đó, và nhóm song song khớp sắp xếp tô pô. Chấm bằng đối chiếu với đồ thị sinh tự động từ danh sách phụ thuộc khai báo.

**Lab.** Lấy nền tảng lesson 217. Vẽ đồ thị phụ thuộc bằng tay từ mã. Chỉ đường găng và các nhóm song song. Đo thời gian chạy tuần tự và ước lượng thời gian tối thiểu từ đường găng. Chạy song song theo nhóm đã xác định và so với ước lượng.

**Pitfalls.** Nhầm thứ tự viết mã với thứ tự phụ thuộc · tối ưu một bước không nằm trên đường găng · chia đỉnh quá nhỏ nên chi phí điều phối lấn át.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đồ thị phi chu trình khớp danh sách phụ thuộc khai báo, và thời gian chạy song song gần ước lượng từ đường găng.

### Lesson 221 · Logical date against wall-clock date; schedule against event trigger `LT`
**Prerequisites.** Lesson 220

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Ngày logic là khoảng dữ liệu mà lần chạy chịu trách nhiệm, còn ngày chạy thật là lúc tiến trình khởi động. Hai cái này gần như không bao giờ trùng, và đây là nguồn sai sót phổ biến nhất khi chạy bù, nối lại lesson 210. Hệ quả trực tiếp lên pipeline: mọi bước lọc theo thời gian phải lọc theo ngày logic, không theo đồng hồ hệ thống, nếu không thì chạy bù ngày hôm kia sẽ nạp dữ liệu hôm nay. Cách truyền ngày logic vào công việc qua tham số dòng lệnh, nối lại lesson 76. Lập lịch theo thời gian: biểu thức cron, múi giờ, và hai bất thường mà giờ mùa hè tạo ra, nối lại lesson 9. Lập lịch theo sự kiện: kích hoạt khi tệp xuất hiện, khi bảng nguồn cập nhật, khi một lần chạy khác kết thúc. Đánh đổi: lịch theo thời gian dễ suy luận và dễ chạy bù nhưng phải đoán độ trễ nguồn; theo sự kiện bám nguồn sát hơn nhưng khó trả lời câu hỏi lần chạy cho ngày mùng ba ở đâu. Mẫu lai có thời gian chờ tối đa.

**Outcome.** Chuyển một bước pipeline đang đọc đồng hồ hệ thống sang nhận ngày logic từ ngoài, và chứng minh bằng chạy bù rằng kết quả khớp bản chạy đúng ngày.

**Đánh giá.** Tầng *áp dụng*. Objective là phép biến đổi mã có tiêu chí đúng sai rõ, kiểm bằng chạy thật. Đạt khi chạy bù ba ngày quá khứ cho kết quả khớp từng dòng với bản đối chứng sinh khi chạy đúng vào ngày đó. Không kiểm bằng câu hỏi vì lỗi này chỉ lộ ra khi chạy.

**Lab.** Tìm mọi chỗ trong nền tảng lesson 217 đọc đồng hồ hệ thống. Chuyển sang nhận ngày logic qua tham số. Chạy bù ba ngày liên tiếp trong quá khứ. So từng dòng với bảng đối chứng. Thiết kế mẫu lai lịch theo giờ cộng cảm biến chờ nguồn có thời gian chờ tối đa.

**Pitfalls.** Đọc đồng hồ hệ thống trong bước biến đổi · đặt lịch theo giờ máy chủ rồi lệch một ngày với người dùng khác múi giờ · bỏ thời gian chờ tối đa cho cảm biến.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba ngày chạy bù khớp từng dòng với bảng đối chứng.

### Lesson 222 · Idempotency, retries, timeouts and what may be retried safely `LT`
**Prerequisites.** Lesson 221

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bất biến khi chạy lại đã gặp ở lesson 106, 205 và 217; bài này phát biểu nó thành điều kiện của điều phối. Quy tắc: một đỉnh chỉ được phép thử lại khi nó bất biến, nên tính bất biến không phải tính chất tốt mà là điều kiện để bật thử lại. Phân biệt thất bại tạm thời với thất bại xác định, nối lại lesson 65: lỗi mạng, hết thời gian chờ, kho bận là tạm thời và thử lại có nghĩa; lỗi cú pháp, thiếu cột, phép kiểm chất lượng không đạt là xác định, thử lại chỉ tốn thời gian và che mất tín hiệu. Khoảng chờ tăng dần và nhiễu ngẫu nhiên, nối lại lesson 34. Số lần thử lại theo loại đỉnh: đỉnh chờ nguồn thử nhiều, đỉnh biến đổi thử ít. Thời gian chờ ở hai mức, đỉnh và cả lần chạy, cùng lý do thiếu cái thứ hai làm một lần chạy treo chiếm chỗ mãi. Chạy tiếp từ chỗ hỏng so với chạy lại từ đầu, và điều kiện để chạy tiếp cho kết quả đúng.

**Outcome.** Phân loại các đỉnh trong pipeline thành bất biến và không bất biến, và đặt chính sách thử lại phù hợp cho từng loại.

**Đánh giá.** Tầng *phân tích*. Objective đòi phán đoán về tính chất của từng đỉnh rồi suy ra cấu hình. Đạt khi phân loại đúng cả tám đỉnh của nền tảng lesson 217, kiểm bằng chạy lại từng đỉnh và đối chiếu, và khi 12 thông báo lỗi được phân loại tạm thời hay xác định đúng ít nhất 10.

**Lab.** Với tám đỉnh của nền tảng, chạy lại từng đỉnh hai lần và đối chiếu để xác định tính bất biến. Sửa đỉnh nào chưa bất biến. Phân loại 12 thông báo lỗi. Đặt chính sách thử lại theo loại đỉnh. Bật thử lại cho một đỉnh chưa bất biến và quan sát nhân bản dữ liệu.

**Pitfalls.** Bật thử lại cho mọi đỉnh mà không kiểm tính bất biến · đặt cùng số lần thử lại cho mọi đỉnh · thử lại một phép kiểm chất lượng không đạt.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tám đỉnh phân loại đúng kiểm bằng chạy lại, và 12 thông báo lỗi phân loại đúng ít nhất 10.

### Lesson 223 · Backfill, catchup and concurrency limits `TH`
**Prerequisites.** Lesson 222

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Chạy bù là chạy lại một dải ngày logic trong quá khứ, đã gặp ở lesson 210; bài này thêm chiều điều phối. Bắt kịp là cơ chế tự động sinh các lần chạy còn thiếu kể từ ngày bắt đầu, và nó bật theo mặc định ở nhiều công cụ; hệ quả là bật một đồ thị có ngày bắt đầu sáu tháng trước sẽ sinh hàng trăm lần chạy cùng lúc và làm sập hệ đích. Ba câu hỏi trước mỗi lần chạy bù: các ngày độc lập hay phải theo thứ tự, chạy được mấy ngày cùng lúc mà hệ đích chịu được, và mọi đỉnh liên quan đã bất biến chưa. Giới hạn song song ở ba tầng: toàn hệ thống, một đồ thị, và một nhóm tài nguyên dùng chung; chỉ tầng thứ ba biểu diễn được ràng buộc chia sẻ giữa nhiều đồ thị, nên đây là chỗ khai báo số kết nối mà cơ sở dữ liệu chịu được, nối lại lesson 134. Theo dõi tiến độ một lần chạy bù dài và cách dừng giữa chừng mà không để lại trạng thái dở.

**Outcome.** Chạy bù 30 ngày cho nền tảng dưới giới hạn ba lần chạy đồng thời, và chứng minh kết quả khớp bản chạy tuần tự từng ngày.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí đúng sai tuyệt đối và chỉ kiểm được bằng chạy thật quy mô. Đạt khi bảng sau chạy bù khớp từng dòng với bản đối chứng sinh bằng chạy tuần tự 30 ngày. Lệch một dòng là không đạt, vì sai sót chạy bù đúng là thứ chỉ lộ ra ở quy mô này.

**Lab.** Sinh bản đối chứng bằng chạy tuần tự 30 ngày. Xoá bảng đích. Chạy bù 30 ngày với giới hạn ba lần chạy đồng thời. Giết một tiến trình giữa chừng và để hệ thống tự phục hồi. So từng dòng. Đo mức dùng kết nối cơ sở dữ liệu ở hai mức giới hạn song song.

**Pitfalls.** Bật bắt kịp mà không đặt giới hạn song song · chạy bù song song các ngày khi có chiều thay đổi chậm, nối lại lesson 210 · đặt giới hạn ở mức đồ thị rồi tưởng đã chặn ràng buộc chia sẻ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng sau chạy bù khớp từng dòng với bản đối chứng, kể cả sau khi một tiến trình bị giết.

### Lesson 224 · What an orchestrator is not - processing engine and message broker `LT`
**Prerequisites.** Lesson 223

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Ba loại hệ thống hay bị gộp và ranh giới giữa chúng. Công cụ điều phối quyết định cái gì chạy khi nào và theo thứ tự nào; nó không xử lý dữ liệu. Bộ máy xử lý biến đổi dữ liệu; Spark ở M35 là ví dụ. Hàng đợi bản tin chuyển bản tin giữa các dịch vụ; Kafka ở M29 là ví dụ. Ba dấu hiệu dùng sai công cụ điều phối và hậu quả: đẩy dữ liệu qua cơ chế truyền tham số giữa các đỉnh làm cơ sở dữ liệu siêu dữ liệu phình và chậm; xử lý từng bản ghi bằng một đỉnh mỗi bản ghi làm đồ thị hàng nghìn đỉnh; và dùng nó làm hàng đợi công việc thời gian thực trong khi nó lập lịch theo chu kỳ. Nguyên tắc phân công: công cụ điều phối gọi bộ máy xử lý và chờ kết quả, dữ liệu đi qua kho lưu trữ chứ không đi qua công cụ điều phối. Trường hợp không cần công cụ điều phối: một công việc duy nhất chạy theo lịch không phụ thuộc gì, cron là đủ và thêm công cụ chỉ thêm thứ phải vận hành.

**Outcome.** Phân loại 12 nhu cầu vào ba loại hệ thống, và nêu điều kiện một đội chưa cần công cụ điều phối riêng.

**Đánh giá.** Tầng *đánh giá*. Objective đòi phán đoán ranh giới, gồm cả phán đoán không dùng gì cả. Đạt khi phân loại đúng ít nhất 10 trên 12 nhu cầu kèm lý do, và khi điều kiện chưa cần công cụ điều phối nêu được bằng đặc tính cụ thể của công việc chứ bằng quy mô đội.

**Lab.** Nhận 12 nhu cầu thật và phân loại vào ba loại hệ thống. Với ba nhu cầu mơ hồ, nêu thêm câu hỏi cần hỏi để phân loại. Dựng một đồ thị đẩy 50 mê ga byte qua cơ chế truyền tham số giữa hai đỉnh và đo tác động lên cơ sở dữ liệu siêu dữ liệu.

**Pitfalls.** Đẩy dữ liệu qua cơ chế truyền tham số giữa các đỉnh · tạo một đỉnh cho mỗi bản ghi · dựng công cụ điều phối cho một công việc duy nhất không phụ thuộc gì.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân loại đúng ít nhất 10 trên 12 nhu cầu kèm lý do, và điều kiện chưa cần công cụ nêu bằng đặc tính công việc.

# MODULE 22 · APACHE AIRFLOW

**Lessons 225–236 · 24 giờ**

| | |
|---|---|
| **Objective cấp module** | Vận hành Airflow ở mức sản xuất: chẩn đoán bộ lập lịch đứng, chọn bộ thực thi có căn cứ, và chạy bù quy mô lớn dưới giới hạn tài nguyên |
| **Tiền đề** | M21 |
| **Exit criterion** | Pipeline tham chiếu chạy trên Airflow, chạy bù 90 ngày dưới giới hạn tài nguyên khớp bản đối chứng, và chẩn đoán được ba sự cố vận hành |
| **Kỹ năng SFIA** | `PROG` mức 4 · `SYSP` mức 4 |
| **Chế độ hỏng** | Dựng được đồ thị chạy xanh trên máy cá nhân rồi dừng ở đó, nên gặp cụm thật là không chẩn đoán được gì |

Airflow ở mức `A`, góc nhìn vận hành nền tảng. Chương trình Analytics Engineer cũng có module Airflow nhưng ở góc điều phối một dự án dbt; hai module không trùng bài nào. Hai bài đầu là cơ chế, tám bài giữa là tính năng và vận hành dưới ràng buộc, hai bài cuối là bộ thực thi và chẩn đoán cụm.

Mọi tham số cấu hình phụ thuộc phiên bản, nên phải đối chiếu tài liệu chính thức của đúng phiên bản đang cài chứ không theo bài hướng dẫn tìm được.

### Lesson 225 · Architecture - scheduler, metadata database, executor, worker `LT`
**Prerequisites.** Module 22: M21

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bốn thành phần và trách nhiệm tách bạch. Bộ lập lịch đọc tệp định nghĩa, dựng đồ thị, quyết định đỉnh nào đủ điều kiện chạy, và ghi quyết định xuống cơ sở dữ liệu siêu dữ liệu. Cơ sở dữ liệu siêu dữ liệu giữ toàn bộ trạng thái, nên nó vừa là nguồn sự thật duy nhất vừa là điểm hỏng chung và chỗ nghẽn khi đồ thị lớn; mọi kiến thức ở M11 áp dụng trực tiếp vào việc vận hành nó. Bộ thực thi quyết định đỉnh chạy ở đâu, chi tiết ở lesson 235. Tiến trình thực thi chạy đỉnh thật. Đường đi của một đỉnh qua bốn thành phần theo thứ tự, kèm chỗ nó kẹt được ở mỗi chặng. Giao diện web đọc từ cơ sở dữ liệu siêu dữ liệu chứ không hỏi tiến trình thực thi, nên nó hiển thị trạng thái đã ghi chứ không hiển thị tiến trình đang chạy thật. Ba triệu chứng vận hành và chặng tương ứng: đỉnh nằm mãi ở đã xếp hàng, đồ thị không xuất hiện, và giao diện chậm.

**Outcome.** Truy một đỉnh đang kẹt về đúng thành phần gây kẹt, dựa vào trạng thái trong cơ sở dữ liệu siêu dữ liệu và nhật ký của thành phần đó.

**Đánh giá.** Tầng *phân tích*. Bài lý thuyết nhưng objective là chẩn đoán, nên kiểm bằng ca bệnh chứ bằng định nghĩa. Ba ca dựng sẵn, mỗi ca kẹt ở một thành phần khác nhau; đạt khi chỉ đúng cả ba và dẫn được bằng chứng từ trạng thái hoặc nhật ký. Hỏi lại định nghĩa bốn thành phần không phải phép kiểm hợp lệ cho objective này.

**Lab.** Dựng Airflow bằng Docker Compose. Mở cơ sở dữ liệu siêu dữ liệu bằng ứng dụng khách SQL và đọc trực tiếp bảng trạng thái đỉnh. Nhận ba ca: đỉnh kẹt ở đã xếp hàng, đồ thị không hiện trong giao diện, giao diện chậm. Với mỗi ca, chỉ thành phần gây ra và dẫn bằng chứng.

**Pitfalls.** Đọc trạng thái từ giao diện rồi tưởng đó là tiến trình thật · khởi động lại cả cụm thay vì đọc nhật ký của đúng thành phần · sửa cấu hình theo hướng dẫn của phiên bản khác.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chỉ đúng thành phần cho cả ba ca, mỗi ca dẫn được trạng thái hoặc dòng nhật ký làm bằng chứng.

### Lesson 226 · DAG parsing, the top-level code trap and import time `TH`
**Prerequisites.** Lesson 225

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Tệp định nghĩa đồ thị được bộ lập lịch đọc lại theo chu kỳ, thường vài chục giây một lần. Hệ quả phản trực giác: mã ở tầng ngoài cùng của tệp chạy lại mỗi lần đọc, còn mã trong thân đỉnh chỉ chạy khi đỉnh chạy. Một lệnh gọi cơ sở dữ liệu hoặc lệnh gọi mạng đặt ở tầng ngoài sẽ được thực hiện hàng nghìn lần mỗi ngày, làm chậm bộ lập lịch cho mọi đồ thị trong cụm chứ không riêng đồ thị đó, nối thẳng bẫy ở lesson 68. Cách đo thời gian phân tích tệp và ngưỡng đáng lo. Ba mẫu sai thường gặp và cách sửa từng cái: đọc cấu hình từ kho dữ liệu ở tầng ngoài, sinh danh sách đỉnh bằng cách truy vấn bảng, và khởi tạo ứng dụng khách ở phạm vi mô đun. Biến và kết nối lưu trong cơ sở dữ liệu siêu dữ liệu, nên đọc chúng ở tầng ngoài cũng là một dạng của cùng cái bẫy. Số lượng tệp đồ thị và thời gian phân tích tổng, cùng ngưỡng cần chia cụm.

**Outcome.** Dựng đồ thị chạy pipeline tham chiếu và hạ thời gian phân tích tệp xuống dưới ngưỡng đo được sau khi sửa mã ở tầng ngoài.

**Đánh giá.** Tầng *áp dụng*. Có sản phẩm chạy được và một phép đo trước sau, nên kiểm bằng số. Đạt khi đồ thị chạy xanh và thời gian phân tích giảm xuống dưới một giây, có ảnh chụp số đo trước và sau. Giải thích được cái bẫy mà không hạ được số thì chưa đạt.

**Lab.** Nhận tệp đồ thị cố ý đặt ba lệnh gọi ở tầng ngoài. Đo thời gian phân tích. Sửa cả ba. Đo lại. Dựng đồ thị chạy pipeline tham chiếu, chạy xanh một lần. Sinh 200 tệp đồ thị và đo thời gian phân tích tổng của bộ lập lịch.

**Pitfalls.** Khởi tạo ứng dụng khách kho dữ liệu ở phạm vi mô đun · sinh đỉnh bằng truy vấn bảng trong lúc phân tích tệp · đặt lệnh nhập nặng ở đầu tệp rồi kết luận bộ lập lịch yếu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đồ thị chạy xanh, và thời gian phân tích tệp sau khi sửa dưới một giây có số đo trước sau.

### Lesson 227 · Task lifecycle and state transitions in the metadata database `TH`
**Prerequisites.** Lesson 226

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Vòng đời một lần chạy đỉnh đi qua các trạng thái ở lesson 220, và bài này đọc chúng trực tiếp từ bảng trong cơ sở dữ liệu siêu dữ liệu thay vì qua giao diện. Lần thử là đơn vị lưu nhật ký, nên một đỉnh thử lại ba lần có ba tệp nhật ký riêng, và đọc nhầm lần thử là lý do phổ biến khiến kết luận sai nguyên nhân. Cấu trúc thư mục nhật ký và cách tìm nhật ký khi giao diện không mở được. Ba lớp thông báo lỗi chồng lên nhau khi pipeline chạy trong Airflow: lỗi của hệ đích ở trong cùng, lỗi của mã pipeline ở giữa, lỗi của Airflow ở ngoài; quy tắc đọc từ trong ra ngoài vì lớp ngoài thường chỉ nói tiến trình con trả về mã khác không. Phân biệt đỉnh thất bại với đỉnh bị đánh dấu bỏ qua vì cha thất bại, và vì sao đếm đỉnh thất bại trong một lần chạy hỏng thường ra con số gây hiểu nhầm. Đánh dấu lại trạng thái bằng tay và khi nào việc đó chính đáng.

**Outcome.** Nhận một lần chạy hỏng và truy về đúng bước gây lỗi cùng dòng thông báo gốc, không dừng ở thông báo mã trả về khác không.

**Đánh giá.** Tầng *phân tích*. Objective là truy nguyên qua ba lớp trừu tượng. Kiểm bằng ba lần chạy hỏng dựng sẵn, mỗi lần hỏng vì một lớp khác nhau; đạt khi chỉ đúng bước và dẫn đúng dòng thông báo gốc cho cả ba. Nêu đúng bước mà dẫn thông báo của lớp ngoài thì tính là chưa đạt.

**Lab.** Nhận ba lần chạy hỏng: một do SQL sai, một do phép kiểm chất lượng không đạt, một do hết thời gian chờ hệ đích. Với mỗi lần, truy về bước và dòng thông báo gốc. Đọc trực tiếp bảng trạng thái đỉnh trong cơ sở dữ liệu siêu dữ liệu. Đẩy nhật ký ra kho lưu trữ ngoài và đọc lại sau khi xoá vùng chứa.

**Pitfalls.** Đọc nhật ký của lần thử đầu trong khi lỗi thật ở lần thử cuối · dừng ở thông báo mã trả về khác không · đếm cả đỉnh bị bỏ qua vào số đỉnh thất bại.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Truy đúng bước và dòng thông báo gốc cho cả ba lần chạy, và đọc lại được nhật ký sau khi xoá vùng chứa.

### Lesson 228 · Operators, hooks and connections `TH`
**Prerequisites.** Lesson 227

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Toán tử là khuôn cho một loại công việc, móc nối là lớp mã nói chuyện với một hệ ngoài, và kết nối là bản ghi cấu hình trong cơ sở dữ liệu siêu dữ liệu. Ba lớp này tách bạch để mã đỉnh không bao giờ chạm tới thông tin xác thực. Kết nối được mã hoá bằng một khoá đối xứng, nên mất khoá là mất toàn bộ kết nối và đổi khoá phải mã hoá lại. Ba nơi thông tin xác thực rò ra ngoài dù đã dùng kết nối: in ra nhật ký khi gỡ lỗi, truyền qua biến môi trường mà tiến trình con ghi lại, và nằm trong tệp cấu hình nộp vào kho mã; cách bịt từng nơi, nối lại lesson 75. Kho bí mật ngoài và điều kiện đáng chuyển sang. Phân biệt biến với kết nối: biến cho tham số cấu hình, kết nối cho thông tin xác thực. Viết toán tử riêng khi không có sẵn, và tiêu chí chọn giữa viết toán tử riêng với gọi lệnh trong toán tử chung. Quyền trên kết nối và ai trong đội xem được cái gì.

**Outcome.** Cấu hình pipeline lấy mọi thông tin xác thực từ kết nối lúc chạy, và chứng minh bằng quét rằng không thông tin xác thực nào trong kho mã hay nhật ký.

**Đánh giá.** Tầng *áp dụng*. Sản phẩm là cấu hình chạy được cộng bằng chứng quét. Kiểm hai lớp: chạy được, và quét toàn bộ kho mã cùng nhật ký bằng công cụ tìm bí mật, đạt khi không có kết quả nào. Không kiểm bằng câu hỏi vì lỗi rò rỉ chỉ lộ ra khi quét thật.

**Lab.** Chuyển pipeline tham chiếu sang lấy thông tin xác thực từ kết nối. Bật chế độ gỡ lỗi chi tiết, chạy lại, quét nhật ký. Quét toàn bộ lịch sử kho mã. Viết một toán tử riêng cho bước nạp từ giao diện lập trình web và so với cách gọi lệnh trong toán tử chung.

**Pitfalls.** Nộp tệp cấu hình có mật khẩu rồi xoá ở lần nộp sau mà quên lịch sử · in toàn bộ biến môi trường khi gỡ lỗi · nhét mật khẩu vào biến vì nhanh hơn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Pipeline chạy xanh với kết nối, và quét kho mã cùng nhật ký không ra thông tin xác thực nào.

### Lesson 229 · XCom, its size limit, and why data does not travel through it `TH`
**Prerequisites.** Lesson 228

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Cơ chế truyền giá trị giữa các đỉnh lưu trong cơ sở dữ liệu siêu dữ liệu, nên mọi giá trị truyền qua nó là một dòng trong bảng. Hệ quả và giới hạn: kích thước tối đa phụ thuộc kiểu cột của cơ sở dữ liệu nền, và vượt quá thì lỗi hoặc cắt cụt tuỳ phiên bản. Vấn đề thật không phải giới hạn mà là hiệu năng: đẩy dữ liệu qua đây làm bảng phình, làm giao diện chậm, và làm cơ sở dữ liệu siêu dữ liệu thành nút cổ chai cho cả cụm, đúng thứ đã cảnh báo ở lesson 224. Cái nên truyền qua nó: đường dẫn tệp, mã định danh lô, số bản ghi, cờ trạng thái. Cái không nên: bảng dữ liệu, nội dung tệp, danh sách dài. Mẫu đúng: dữ liệu đi qua kho lưu trữ, chỉ đường dẫn đi qua cơ chế truyền giá trị. Dọn dẹp bảng này định kỳ và hậu quả khi quên. Phụ thuộc ngầm giữa hai đỉnh qua cơ chế này mà không có cạnh trong đồ thị, một lỗi thiết kế làm thứ tự chạy không bảo đảm.

**Outcome.** Chuyển một đồ thị đang đẩy dữ liệu qua cơ chế truyền giá trị sang mẫu truyền đường dẫn, và đo tác động lên cơ sở dữ liệu siêu dữ liệu.

**Đánh giá.** Tầng *áp dụng*. Objective có một phép biến đổi và một phép đo tác động. Đạt khi kích thước bảng liên quan giảm ít nhất 95% sau khi chuyển, và khi thời gian tải giao diện danh sách lần chạy giảm đo được.

**Lab.** Dựng đồ thị đẩy 50 mê ga byte qua cơ chế truyền giá trị, chạy 100 lần. Đo kích thước bảng và thời gian tải giao diện. Chuyển sang truyền đường dẫn tới kho đối tượng, chạy lại 100 lần, đo lại. Tìm một phụ thuộc ngầm giữa hai đỉnh và thêm cạnh tường minh cho nó.

**Pitfalls.** Đẩy khung dữ liệu qua cơ chế truyền giá trị · dựa vào phụ thuộc ngầm thay vì khai báo cạnh · quên dọn bảng này nên nó phình theo thời gian.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Kích thước bảng giảm ít nhất 95%, và thời gian tải giao diện danh sách lần chạy giảm đo được.

### Lesson 230 · Sensors - poke against reschedule - and deferrable tasks `TH`
**Prerequisites.** Lesson 229

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Cảm biến là đỉnh chờ một điều kiện thành đúng, và nó là cách cài lập lịch theo sự kiện ở lesson 221. Hai chế độ và khác biệt quyết định: chế độ thăm dò giữ chỗ tiến trình thực thi suốt thời gian chờ, chế độ lên lịch lại nhả chỗ giữa hai lần kiểm. Hệ quả vận hành: 20 cảm biến chế độ thăm dò trên cụm có 16 chỗ làm mọi đỉnh khác không chạy được, một tình trạng bế tắc tài nguyên trông như hệ thống treo. Đây là sự cố phổ biến và nó không hiện ra như lỗi. Đỉnh hoãn lại đẩy việc chờ sang một tiến trình riêng nên không chiếm chỗ nào, giải quyết triệt để hơn chế độ lên lịch lại, nhưng đòi mã viết theo kiểu bất đồng bộ, nối lại lesson 58. Thời gian chờ tối đa cho cảm biến là bắt buộc, nếu không thì nó chờ vô hạn. Phân biệt cảm biến với thử lại: cảm biến chờ điều kiện ngoài, thử lại xử lý lỗi tạm thời. Mẫu thay thế: để hệ nguồn kích hoạt thay vì mình chờ.

**Outcome.** Tái hiện bế tắc tài nguyên do cảm biến chế độ thăm dò, và sửa bằng hai cách, đo số chỗ tiến trình thực thi bị chiếm ở mỗi cách.

**Đánh giá.** Tầng *phân tích*. Objective đòi tái hiện một sự cố không hiện ra như lỗi rồi sửa có đo. Đạt khi tái hiện được tình trạng không đỉnh nào chạy được dù cụm rỗi, và khi hai bản sửa đều hạ số chỗ bị chiếm xuống dưới hai, có số đo cho cả ba trạng thái.

**Lab.** Cụm 8 chỗ tiến trình thực thi. Dựng 10 cảm biến chế độ thăm dò chờ tệp chưa tới. Quan sát không đỉnh nào khác chạy được. Đo số chỗ bị chiếm. Chuyển sang chế độ lên lịch lại, đo lại. Chuyển sang đỉnh hoãn lại, đo lại. Bỏ thời gian chờ tối đa và quan sát.

**Pitfalls.** Dùng chế độ thăm dò cho cảm biến chờ lâu · bỏ thời gian chờ tối đa · dùng cảm biến khi hệ nguồn có thể kích hoạt trực tiếp.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tái hiện được bế tắc tài nguyên, và hai bản sửa hạ số chỗ bị chiếm xuống dưới hai có số đo.

### Lesson 231 · Dynamic task mapping `TH`
**Prerequisites.** Lesson 230

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Sinh số đỉnh phụ thuộc dữ liệu lúc chạy thay vì cố định lúc viết, giải bài toán nạp N tệp mà N chỉ biết khi chạy. Khác biệt then chốt với việc sinh đỉnh ở tầng ngoài tệp: cách đó chạy lúc phân tích nên dính bẫy ở lesson 226 và số đỉnh cố định cho tới lần phân tích sau; cách này chạy lúc thực thi nên số đỉnh phản ánh dữ liệu thật. Cách khai báo và giới hạn số đỉnh sinh ra, cùng lý do phải đặt giới hạn: một lỗi ở nguồn trả về 100.000 phần tử sẽ sinh 100.000 đỉnh và làm sập bộ lập lịch. Kết quả gộp từ các đỉnh sinh ra và cách xử lý khi một phần thất bại. Đánh đổi với việc để một đỉnh xử lý cả danh sách trong vòng lặp: nhiều đỉnh cho khả năng quan sát và thử lại riêng từng phần, một đỉnh cho chi phí điều phối thấp; ngưỡng chọn theo thời gian xử lý mỗi phần tử và tỉ lệ hỏng. Đây là cùng bài toán kích thước đỉnh ở lesson 220.

**Outcome.** Chuyển một đỉnh xử lý danh sách trong vòng lặp sang sinh đỉnh động, và xác định ngưỡng mà cách nào rẻ hơn bằng thực nghiệm.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn giữa hai cách có đánh đổi hai chiều. Đạt khi có bảng thực nghiệm ít nhất bốn kích thước danh sách kèm tổng thời gian và thời gian phát hiện lỗi, và khi ngưỡng chọn ra được biện minh bằng cả hai chỉ số chứ bằng một.

**Lab.** Đỉnh nạp N tệp, chạy ở N bằng 5, 50, 500, 5.000. Cài cả hai cách. Đo tổng thời gian chạy và thời gian từ lúc một tệp hỏng tới lúc biết tệp nào. Đặt giới hạn số đỉnh sinh ra và thử vượt giới hạn. Cho một tệp hỏng và so cách chạy lại ở hai cách.

**Pitfalls.** Sinh đỉnh ở tầng ngoài tệp bằng truy vấn · không đặt giới hạn số đỉnh sinh ra · chọn cách theo tổng thời gian mà bỏ thời gian phát hiện lỗi.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng bốn kích thước danh sách có cả hai chỉ số, và ngưỡng chọn ra biện minh bằng cả hai.

### Lesson 232 · Retries, timeouts, SLA and alerting `TH`
**Prerequisites.** Lesson 231

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Áp phân loại ở lesson 222 vào cấu hình thật. Thử lại đặt ở mức đỉnh với số lần khác nhau theo loại đỉnh. Khoảng chờ tăng dần và giới hạn trên. Thời gian chờ ở hai mức và lý do thiếu mức lần chạy làm một đồ thị treo chiếm chỗ mãi. Cam kết thời gian hoàn thành khác thời gian chờ tối đa ở chỗ nó không giết đỉnh mà chỉ báo trễ, một phân biệt hay bị nhầm. Cảnh báo phải nói ba thứ: cái gì hỏng, ảnh hưởng tới ai, bước đầu tiên nên làm, nối lại lesson 214. Mệt mỏi vì cảnh báo và hai cách chống: gom cảnh báo cùng nguyên nhân, và chỉ cảnh báo thứ người trực làm được gì đó. Hàm gọi khi thất bại và khi thử lại, dùng để gửi cảnh báo có ngữ cảnh thay vì thông báo mặc định. Phân biệt cảnh báo cho người trực với ghi nhận cho báo cáo. Đỉnh dọn dẹp chạy kể cả khi đỉnh trước thất bại, và quy tắc kích hoạt để làm việc đó.

**Outcome.** Cấu hình thử lại, thời gian chờ và cảnh báo cho pipeline tham chiếu sao cho lỗi tạm thời tự phục hồi không sinh cảnh báo, còn lỗi xác định sinh cảnh báo đủ ba thứ.

**Đánh giá.** Tầng *áp dụng*. Objective là cấu hình có tiêu chí đúng sai kiểm được bằng thực nghiệm. Kiểm bằng hai kịch bản bơm lỗi đối lập. Đạt khi kịch bản một chạy qua không cảnh báo, kịch bản hai sinh đúng một cảnh báo, và nội dung cảnh báo nêu được cả ba thứ.

**Lab.** Cấu hình đồ thị tham chiếu. Bơm lỗi mạng tự khỏi sau 20 giây, xác nhận tự phục hồi không cảnh báo. Bơm lỗi phép kiểm chất lượng không đạt, xác nhận đúng một cảnh báo. Viết hàm gọi khi thất bại để cảnh báo đủ ba thứ. Thêm đỉnh dọn dẹp chạy kể cả khi thất bại.

**Pitfalls.** Đặt cùng số lần thử lại cho mọi đỉnh · nhầm cam kết thời gian với thời gian chờ tối đa · cảnh báo mọi thất bại kể cả thứ tự khỏi.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Lỗi tạm thời không sinh cảnh báo, lỗi xác định sinh đúng một cảnh báo nêu đủ ba thứ.

### Lesson 233 · Backfill and catchup at scale `TH`
**Prerequisites.** Lesson 232

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Áp lesson 223 vào quy mô lớn hơn và vào đặc thù công cụ. Hai cách chạy bù: lệnh dòng lệnh và kích hoạt từ giao diện, cùng khác biệt về khả năng kiểm soát. Bắt kịp và ngày bắt đầu: đổi ngày bắt đầu của một đồ thị đang chạy gây hành vi khó đoán, nên quy tắc là tạo đồ thị mới thay vì đổi ngày bắt đầu. Chạy bù 90 ngày trên đồ thị 20 đỉnh sinh 1.800 lần chạy đỉnh, nên giới hạn song song và thứ tự ưu tiên quyết định nó mất bao lâu và có ảnh hưởng tải hằng ngày không. Tách nhóm tài nguyên cho chạy bù khỏi nhóm của sản xuất, nếu không thì chạy bù chiếm hết chỗ và công việc hằng ngày trễ. Theo dõi tiến độ và dừng giữa chừng sạch sẽ. Chạy bù một phần đồ thị bằng cách chọn tập đỉnh. Xoá trạng thái lần chạy cũ trước khi chạy lại và hậu quả nếu quên. Chạy bù khi logic đã đổi: quyết định có muốn kết quả theo logic mới không, nối lại lesson 210.

**Outcome.** Chạy bù 90 ngày cho đồ thị tham chiếu dưới giới hạn tài nguyên tách khỏi sản xuất, và chứng minh công việc hằng ngày không bị trễ.

**Đánh giá.** Tầng *áp dụng*. Objective có hai tiêu chí đồng thời, một về đúng đắn một về ảnh hưởng. Đạt khi kết quả 90 ngày khớp bản đối chứng, và khi thời gian hoàn thành công việc hằng ngày trong lúc chạy bù không vượt quá 20% so với mức nền.

**Lab.** Sinh bản đối chứng 90 ngày. Chạy bù với nhóm tài nguyên chung với sản xuất, đo độ trễ công việc hằng ngày. Tách nhóm tài nguyên riêng, chạy lại, đo lại. Đối chiếu kết quả. Dừng giữa chừng một lần và tiếp tục, xác nhận không trùng lặp.

**Pitfalls.** Chạy bù dùng chung nhóm tài nguyên với sản xuất · đổi ngày bắt đầu của đồ thị đang chạy · quên xoá trạng thái lần chạy cũ trước khi chạy lại.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Kết quả 90 ngày khớp bản đối chứng, và công việc hằng ngày không trễ quá 20% so với mức nền.

### Lesson 234 · Pools, priority weight and concurrency at three levels `TH`
**Prerequisites.** Lesson 233

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba tầng giới hạn song song và phạm vi của từng tầng, nối lại lesson 223. Nhóm tài nguyên là cơ chế duy nhất trong ba cái biểu diễn được ràng buộc dùng chung giữa nhiều đồ thị, nên đây là chỗ khai báo số kết nối mà cơ sở dữ liệu chịu được, lấy từ số đo ở lesson 134. Trọng số ưu tiên quyết định đỉnh nào lấy chỗ trước khi nhóm đầy, và cách dùng nó để đồ thị quan trọng không bị đồ thị chạy bù chặn. Hai triệu chứng của thiếu giới hạn: hệ đích báo hết kết nối, và truy vấn xếp hàng làm mọi thứ chậm đều chứ không hỏng hẳn, cái sau khó chẩn đoán hơn. Tìm số song song phù hợp bằng thực nghiệm thay vì đoán, cùng phương pháp lesson 134. Giới hạn ở mức đỉnh để một đỉnh không chạy quá nhiều lần chạy đồng thời. Cô lập tài nguyên giữa môi trường. Chi phí ở hệ đích tính tiền theo lượng quét: tăng song song không phải lúc nào cũng giảm tổng thời gian nhưng gần như luôn tăng tiền, nối lại lesson 160.

**Outcome.** Tìm mức song song phù hợp bằng thực nghiệm và chứng minh cấu hình chọn ra không làm hệ đích hết kết nối khi chạy bù đồng thời với lần chạy hằng ngày.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn một giá trị và biện minh bằng đánh đổi giữa thời gian với chi phí. Đạt khi có bảng thực nghiệm ít nhất bốn mức song song kèm ba số đo mỗi mức, và khi kịch bản kiểm chứng chạy đồng thời không sinh lỗi hết kết nối.

**Lab.** Chạy đồ thị tham chiếu ở bốn mức song song. Mỗi mức đo tổng thời gian, số kết nối cao nhất tới hệ đích, và chi phí hoặc lượng dữ liệu quét. Chọn một mức, khai báo nhóm tài nguyên. Chạy bù đồng thời với lần chạy hằng ngày và xác nhận không lỗi. Đặt trọng số ưu tiên và kiểm thứ tự lấy chỗ.

**Pitfalls.** Đặt giới hạn ở mức đồ thị rồi tưởng đã chặn ràng buộc dùng chung · tăng song song tới khi nhanh nhất mà không nhìn chi phí · để chạy bù dùng chung nhóm với sản xuất.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng bốn mức song song có đủ ba số đo, và chạy bù đồng thời với hằng ngày không sinh lỗi hết kết nối.

### Lesson 235 · Executors - Local, Celery, Kubernetes - and choosing between them `TH`
**Prerequisites.** Lesson 234

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bộ thực thi quyết định đỉnh chạy ở đâu, và ba lựa chọn có đặc tính vận hành khác hẳn nhau. Bộ thực thi cục bộ chạy đỉnh trên cùng máy với bộ lập lịch: đơn giản nhất, không có thành phần thêm, nhưng không mở rộng và một đỉnh nặng làm chậm bộ lập lịch. Bộ thực thi phân tán qua hàng đợi chạy đỉnh trên nhiều tiến trình thực thi thường trực: mở rộng được, chi phí khởi động thấp, nhưng thêm hàng đợi và các tiến trình thực thi phải vận hành, và mọi tiến trình thực thi phải có cùng phụ thuộc. Bộ thực thi trên cụm vùng chứa tạo một vùng chứa cho mỗi đỉnh: cô lập phụ thuộc hoàn toàn và tự co giãn, nhưng chi phí khởi động mỗi đỉnh vài giây tới vài chục giây nên đồ thị nhiều đỉnh ngắn trở nên rất chậm. Bốn tiêu chí chọn: số đỉnh mỗi ngày, thời gian chạy trung bình một đỉnh, mức độ khác nhau về phụ thuộc giữa các đỉnh, và năng lực vận hành của đội. Chi phí khởi động là yếu tố bị bỏ qua nhiều nhất.

**Outcome.** Chọn bộ thực thi cho ba tình huống khác nhau và chứng minh bằng số đo chi phí khởi động cùng thông lượng.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn giữa ba phương án theo bốn tiêu chí. Đạt khi có số đo chi phí khởi động và thông lượng cho ít nhất hai bộ thực thi, và khi ba lựa chọn đều dẫn được về số đo cộng năng lực vận hành chứ bằng danh tiếng công cụ.

**Lab.** Chạy cùng đồ thị tham chiếu trên bộ thực thi cục bộ và bộ thực thi phân tán. Đo chi phí khởi động một đỉnh và tổng thông lượng. Nếu có cụm vùng chứa thì đo thêm, nếu không thì ước lượng từ tài liệu và ghi rõ chưa đo. Ba tình huống: 50 đỉnh mỗi ngày mỗi đỉnh 10 giây, 5.000 đỉnh mỗi ngày mỗi đỉnh 30 phút, và các đỉnh cần thư viện xung đột nhau.

**Pitfalls.** Chọn bộ thực thi trên cụm vùng chứa cho đồ thị nhiều đỉnh ngắn · dùng bộ thực thi cục bộ cho sản xuất · bỏ qua yêu cầu mọi tiến trình thực thi có cùng phụ thuộc.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Có số đo chi phí khởi động và thông lượng cho ít nhất hai bộ thực thi, và ba lựa chọn dẫn được về số đo.

### Lesson 236 · Operating Airflow - deployment, upgrade, diagnosing a stuck scheduler `TH`
**Prerequisites.** Lesson 235

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Không có cơ chế mới. Bài gộp module, và nó đo đúng thứ phân biệt mức `A` với mức `B`: chẩn đoán được khi cụm hỏng. Bốn sự cố vận hành thường gặp và quy trình chẩn đoán cho từng cái. Bộ lập lịch đứng: kiểm thời gian phân tích tệp ở lesson 226, kiểm cơ sở dữ liệu siêu dữ liệu chậm, kiểm bế tắc cảm biến ở lesson 230, theo thứ tự đó. Đỉnh kẹt ở đã xếp hàng: kiểm chỗ tiến trình thực thi, nhóm tài nguyên, và trạng thái tiến trình thực thi. Cơ sở dữ liệu siêu dữ liệu phình: dọn bảng lịch sử và bảng truyền giá trị, áp kiến thức M11 về phình bảng. Giao diện chậm: thường là hệ quả của cái thứ ba. Nâng cấp phiên bản: di trú lược đồ cơ sở dữ liệu siêu dữ liệu, kiểm tương thích của mã đồ thị, và quy trình quay lui. Triển khai mã đồ thị: đồng bộ tệp tới mọi thành phần và cửa sổ không nhất quán giữa chúng. Sao lưu cơ sở dữ liệu siêu dữ liệu và thứ mất khi mất nó.

**Outcome.** Chẩn đoán ba sự cố cụm chưa từng thấy về đúng nguyên nhân theo quy trình, và thực hiện một lần nâng cấp phiên bản có quay lui được.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chẩn đoán dưới thời gian và một thao tác vận hành rủi ro. Chấm theo năm mục: chẩn đoán ba sự cố 45đ, nâng cấp thành công 20đ, quay lui được 15đ, sổ tay xử lý 10đ, và sao lưu cơ sở dữ liệu siêu dữ liệu 10đ. Đạt khi ≥ 70/100 và mục chẩn đoán ≥ 60%.

**Lab.** Cụm Airflow có tải. Giám khảo gây ba sự cố không báo trước. Chẩn đoán theo quy trình, ghi số đo trước khi sửa. Nâng cấp một phiên bản phụ, có di trú lược đồ. Quay lui về phiên bản cũ. Nộp sổ tay xử lý cho bốn sự cố theo khuôn lesson 90.

**Pitfalls.** Khởi động lại cụm khi gặp sự cố thay vì chẩn đoán · nâng cấp mà không sao lưu cơ sở dữ liệu siêu dữ liệu · triển khai mã đồ thị tới bộ lập lịch mà quên các tiến trình thực thi.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đạt ≥ 70/100 và mục chẩn đoán ≥ 60%, với sổ tay xử lý đủ bốn sự cố.

# MODULE 23 · DAGSTER

**Lessons 237–248 · 24 giờ**

| | |
|---|---|
| **Objective cấp module** | Mô hình hoá pipeline tham chiếu bằng đồ thị tài sản, và chỉ ra thao tác vận hành nào rẻ đi so với đồ thị tác vụ cùng lý do nằm ở mô hình |
| **Tiền đề** | M22 |
| **Exit criterion** | Pipeline tham chiếu chạy bằng đồ thị tài sản có phân mảnh và kiểm tra tài sản, vật chất hoá lại một phân mảnh, và đo được số bước phải chạy so với Airflow |
| **Kỹ năng SFIA** | `PROG` mức 4 · `DATM` mức 3 |
| **Chế độ hỏng** | Khai báo tài sản theo thói quen tác vụ, nên mất hết lợi thế của mô hình tài sản mà vẫn chịu chi phí học công cụ mới |

Dagster ở mức `A`, dựng lại đúng pipeline tham chiếu của M22. Khác biệt cần bám suốt module là đơn vị mô hình hoá: Airflow mô hình hoá việc phải làm, Dagster mô hình hoá thứ được tạo ra. Ba bài đầu là mô hình, sáu bài giữa là tính năng suy ra từ mô hình đó, ba bài cuối là tích hợp và vận hành.

### Lesson 237 · The asset as the unit of modelling, against the task `LT`
**Prerequisites.** Module 23: M22

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Một tài sản là một đối tượng dữ liệu bền vững có tên: một bảng, một tệp, một phân mảnh. Khai báo gồm tên, phụ thuộc vào tài sản nào, và hàm tính ra nó. Ba hệ quả suy ra từ lựa chọn này. Thứ nhất, đồ thị phụ thuộc phát biểu bằng bảng nào sinh ra bảng nào, nên nó trùng với lineage dữ liệu thay vì nằm song song với nó và phải giữ cho khớp bằng tay, nối lại lesson 206. Thứ hai, câu hỏi vận hành đổi dạng: ở Airflow hỏi đỉnh nào chạy lúc nào, ở đây hỏi bảng nào cũ, bảng nào sai, bảng nào cần dựng lại; ba câu sau gần với câu hỏi người dùng dữ liệu hỏi hơn. Thứ ba, dựng lại chọn lọc thành thao tác cơ bản chứ không phải mẹo, vì hệ thống biết bảng nào phụ thuộc bảng nào. Chỗ mô hình tài sản không hợp: việc không tạo ra dữ liệu bền vững, ví dụ gửi thông báo hay gọi dịch vụ ngoài; hai khái niệm cho loại đó ở lesson 239. Vật chất hoá là hành động tính lại một tài sản và ghi kết quả xuống.

**Outcome.** Đối chiếu đồ thị tác vụ của M22 với đồ thị tài sản cho cùng pipeline, và chỉ ra ba câu hỏi vận hành mà mô hình tài sản trả lời trực tiếp còn mô hình tác vụ phải suy ra.

**Đánh giá.** Tầng *phân tích*. Bài lý thuyết nhưng objective là phân rã khác biệt giữa hai mô hình, không phải nhắc lại định nghĩa. Kiểm bằng bản đối chiếu viết: ba câu hỏi phải là câu hỏi vận hành thật, và với mỗi câu phải nêu ở Airflow phải làm gì để trả lời. Liệt kê tính năng của Dagster không phải phép kiểm hợp lệ cho objective này.

**Lab.** Lấy đồ thị Airflow ở lesson 226. Vẽ đồ thị tài sản tương ứng cho cùng pipeline tham chiếu. Đặt ba câu hỏi vận hành thật: bảng nào cũ hơn 24 giờ, đổi lược đồ nguồn thì hỏng bảng nào, dựng lại một bảng giữa đồ thị thì phải dựng lại thêm gì. Với mỗi câu, nêu cách trả lời ở hai mô hình.

**Pitfalls.** Vẽ đồ thị tài sản y hệt đồ thị tác vụ rồi kết luận hai cái như nhau · coi mọi việc là tài sản kể cả việc không sinh dữ liệu · so sánh hai công cụ bằng tính năng thay vì bằng câu hỏi vận hành.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bản đối chiếu nêu đủ ba câu hỏi vận hành, mỗi câu có cách trả lời ở cả hai mô hình.

### Lesson 238 · Software-defined assets and the asset graph `TH`
**Prerequisites.** Lesson 237

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Khai báo tài sản bằng hàm có trang trí, và phụ thuộc suy ra từ tham số của hàm chứ từ khai báo riêng, nên đồ thị không lệch khỏi mã. Khoá tài sản và nhóm tài sản, cùng quy ước đặt tên theo hạt của kết quả thay vì theo thao tác, nối lại lesson 192. Tài sản ngoài là tài sản hệ thống biết có nhưng không tự tạo ra, dùng để nối đồ thị tới tận bảng nguồn; đây là chỗ lineage bắt đầu từ nguồn thật chứ từ bước đầu tiên của mình. Siêu dữ liệu gắn vào mỗi lần vật chất hoá: số dòng, dung lượng, và bất kỳ số nào đáng theo dõi, và chúng hiện thành đồ thị theo thời gian trong giao diện. Chọn tập tài sản để chạy bằng cú pháp chọn lọc theo tên, theo nhóm, theo thượng nguồn hoặc hạ nguồn. Mã ở tầng ngoài tệp cũng chạy lúc nạp định nghĩa, nên bẫy ở lesson 226 vẫn còn, chỉ khác tên gọi. Đồ thị nhiều tài sản và ngưỡng cần chia nhóm.

**Outcome.** Dựng lại pipeline tham chiếu thành đồ thị tài sản có tài sản ngoài cho nguồn, và chạy một nhánh bằng cú pháp chọn lọc.

**Đánh giá.** Tầng *áp dụng*. Sản phẩm chạy được với tiêu chí đếm được. Đạt khi đồ thị có đủ tài sản cho mọi bước cộng tài sản ngoài cho hai nguồn, và khi chạy một nhánh thì số tài sản vật chất hoá khớp số tài sản trong nhánh đó, đọc từ bản ghi chạy. Chạy được cả đồ thị không chứng minh được objective.

**Lab.** Dựng lại pipeline tham chiếu thành đồ thị tài sản. Khai báo hai nguồn thành tài sản ngoài. Gắn siêu dữ liệu số dòng cho mỗi tài sản. Chọn một nhánh giữa đồ thị và chạy nó, đọc bản ghi chạy xác nhận số tài sản. Đặt một lệnh gọi mạng ở tầng ngoài tệp và đo thời gian nạp định nghĩa.

**Pitfalls.** Khai báo phụ thuộc bằng chuỗi tên gõ tay rồi sai chính tả · bỏ tài sản ngoài nên đồ thị đứt ở tầng nguồn · đặt mã nặng ở tầng ngoài tệp.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đồ thị đủ tài sản cộng hai tài sản ngoài, và chạy một nhánh vật chất hoá đúng số tài sản của nhánh đó.

### Lesson 239 · Ops, jobs and graphs - when you still need them `TH`
**Prerequisites.** Lesson 238

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Không phải việc nào cũng sinh ra dữ liệu bền vững: gửi thông báo, gọi dịch vụ ngoài, dọn tệp tạm, kích hoạt hệ thống khác. Đơn vị tác vụ và công việc tồn tại cho đúng nhóm đó. Tiêu chí phân biệt dựa trên tác dụng phụ: nếu chạy lại hai lần và kết quả quan sát được là như nhau thì nhiều khả năng đó là tài sản; nếu chạy lại gây tác dụng phụ lặp lại thì đó là tác vụ. Tiêu chí này chính là tính bất biến ở lesson 222 nhìn từ góc mô hình hoá. Cách trộn hai thứ trong một hệ thống mà không rối: tài sản cho đường dữ liệu chính, tác vụ cho phần rìa. Đồ thị tác vụ khi một chuỗi việc cần chạy theo thứ tự nhưng không sinh bảng nào. Công việc vật chất hoá một tập tài sản, và đây là cầu nối: lịch chạy gắn vào công việc chứ gắn vào tài sản. Sai lầm theo chiều ngược: biến mọi thứ thành tác vụ vì quen Airflow, rồi mất toàn bộ lợi thế đã học ở lesson 237.

**Outcome.** Phân loại một danh sách việc thành tài sản và tác vụ theo tiêu chí tác dụng phụ, và cài đặt phần rìa bằng tác vụ trong khi giữ đường dữ liệu chính là tài sản.

**Đánh giá.** Tầng *áp dụng*. Objective gồm một phép phân loại có tiêu chí xác định cộng một sản phẩm. Kiểm hai phần: bảng phân loại 12 việc chấm theo tiêu chí tác dụng phụ, đạt khi đúng ít nhất 10; và hệ thống chạy được trong đó đường dữ liệu chính vẫn là tài sản. Phân loại đúng mà cài đặt biến hết thành tác vụ thì không đạt.

**Lab.** Nhận 12 việc trong pipeline tham chiếu: chạy bước biến đổi, gửi thông báo thành công, dọn bảng tạm, tải tệp lên kho đối tượng, kích hoạt làm mới bảng điều khiển, gọi giao diện lập trình web bên thứ ba, và các việc khác. Phân loại theo tiêu chí. Cài ba việc phần rìa bằng tác vụ, giữ đường dữ liệu chính là tài sản.

**Pitfalls.** Biến việc gửi thông báo thành tài sản vì tiện đặt vào đồ thị · biến mọi bước thành tác vụ vì quen Airflow · gắn lịch vào tài sản thay vì vào công việc.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng phân loại đúng ít nhất 10 trên 12, và hệ thống chạy được với đường dữ liệu chính là tài sản.

### Lesson 240 · Partitions - time, static and multi-dimensional `TH`
**Prerequisites.** Lesson 239

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phân mảnh chia một tài sản thành các lát độc lập, mỗi lát vật chất hoá riêng và có trạng thái riêng, nên hệ thống biết lát nào đã có lát nào chưa. Đây là chỗ mô hình tài sản trả lại lợi ích rõ nhất: chạy bù trở thành vật chất hoá các lát còn thiếu, không phải một chế độ chạy riêng như ở lesson 233. Định nghĩa phân mảnh theo thời gian và ràng buộc phân mảnh phải khớp hạt của bảng, nối lại lesson 192; khai báo theo ngày trong khi bảng gộp theo tuần sẽ ghi đè lẫn nhau, một lỗi âm thầm. Ánh xạ phân mảnh giữa các tài sản khi hạt đổi dọc đồ thị, ví dụ bảng ngày nuôi bảng tháng. Truyền cửa sổ thời gian của lát vào mã, nối thẳng ngày logic ở lesson 221. Bảng trạng thái phân mảnh trong giao diện và cách đọc để biết thiếu ngày nào. Phân mảnh tĩnh theo danh sách giá trị. Phân mảnh nhiều chiều và chi phí: số lát nhân lên rất nhanh nên phải cân nhắc trước khi khai báo.

**Outcome.** Khai báo phân mảnh theo ngày cho các tài sản của pipeline, và vật chất hoá lại đúng một ngày trong quá khứ mà không đụng tới ngày khác.

**Đánh giá.** Tầng *áp dụng*. Objective kiểm được bằng thực nghiệm có tiêu chí tuyệt đối. Đạt khi vật chất hoá lại ngày `T-5` làm đổi đúng các dòng của ngày đó, xác nhận bằng so dấu thời gian cập nhật của các ngày còn lại trước và sau. Một ngày khác bị đụng là không đạt.

**Lab.** Khai báo phân mảnh ngày cho các tài sản. Vật chất hoá 30 ngày. Ghi dấu thời gian cập nhật từng ngày. Vật chất hoá lại riêng ngày `T-5`. So dấu thời gian. Đo số bước phải chạy so với cách chạy bù ở lesson 233. Khai báo phân mảnh nhiều chiều theo ngày và vùng, đếm số lát sinh ra.

**Pitfalls.** Khai báo phân mảnh theo ngày cho bảng có hạt tuần · quên truyền cửa sổ phân mảnh vào mã nên vẫn lọc theo đồng hồ hệ thống · khai báo phân mảnh nhiều chiều rồi sinh hàng chục nghìn lát.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Vật chất hoá lại một ngày chỉ đổi dòng của ngày đó, xác nhận bằng dấu thời gian các ngày còn lại.

### Lesson 241 · Schedules and sensors `TH`
**Prerequisites.** Lesson 240

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Lịch chạy gắn vào công việc và sinh lần chạy theo chu kỳ, tương ứng lập lịch theo thời gian ở lesson 221. Cảm biến chạy một hàm kiểm tra theo chu kỳ ngắn và quyết định có kích hoạt hay không, tương ứng lập lịch theo sự kiện; khác cảm biến của Airflow ở lesson 230 ở chỗ nó không chiếm chỗ tiến trình thực thi vì nó chạy trong tiến trình nền riêng, nên bài toán bế tắc tài nguyên ở đó không tồn tại ở đây. Con trỏ của cảm biến để nhớ đã xử lý tới đâu giữa các lần kiểm, và lưu nó đúng cách là điều kiện để cảm biến không kích hoạt trùng. Cảm biến tài sản kích hoạt khi một tài sản thượng nguồn được vật chất hoá, cho phép nối hai đồ thị mà không cần lịch. Chính sách độ tươi khai báo yêu cầu bằng ngưỡng thời gian và tự thành cảnh báo khi vượt, chuyển khả năng quan sát từ việc đã chạy chưa sang việc dữ liệu có mới không. Cảm biến chạy lỗi và cách phát hiện, vì cảm biến hỏng thì không có gì kích hoạt và hệ thống im lặng.

**Outcome.** Cấu hình mẫu lai gồm lịch theo giờ và cảm biến chờ nguồn, và chứng minh cảm biến không kích hoạt trùng khi kiểm lại nhiều lần.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí kiểm bằng hai kịch bản đối lập cộng một tiêu chí về trùng lặp. Đạt khi nguồn tới sớm thì chạy ngay và nguồn không tới thì vẫn chạy đúng giờ chốt, và khi chạy cảm biến 200 vòng kiểm trên cùng một tệp chỉ sinh đúng một lần chạy.

**Lab.** Cấu hình lịch theo giờ cộng cảm biến chờ tệp. Kịch bản một: đặt tệp sớm 20 phút, xác nhận chạy ngay. Kịch bản hai: không đặt tệp, xác nhận vẫn chạy đúng giờ chốt. Chạy cảm biến 200 vòng trên cùng tệp và đếm số lần chạy sinh ra. Khai báo chính sách độ tươi và để một tài sản quá hạn.

**Pitfalls.** Không lưu con trỏ cảm biến nên kích hoạt trùng mỗi vòng kiểm · gắn lịch vào tài sản thay vì vào công việc · không theo dõi cảm biến lỗi nên hệ thống im lặng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Hai kịch bản đối lập cho đúng hành vi, và 200 vòng kiểm trên cùng tệp chỉ sinh một lần chạy.

### Lesson 242 · Resources, configuration and separating IO from logic `TH`
**Prerequisites.** Lesson 241

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Tài nguyên là đối tượng dùng chung khai báo một lần rồi tiêm vào tài sản cần nó: kết nối cơ sở dữ liệu, ứng dụng khách kho đối tượng, ứng dụng khách giao diện lập trình web. Hai lợi ích: mã tài sản không tự khởi tạo kết nối nên kiểm thử được bằng cách tiêm bản giả, nối lại lesson 84; và đổi cấu hình giữa các môi trường không phải sửa mã, nối lại lesson 75. Cấu hình có lược đồ và kiểm lúc nạp định nghĩa chứ lúc chạy, nên thiếu một trường bị bắt sớm. Ba tầng cấu hình và thứ tự ưu tiên. Tách phần vào ra khỏi phần logic: hàm tài sản nhận dữ liệu đã đọc và trả dữ liệu cần ghi, còn việc đọc ghi do bộ quản lý vào ra làm, chi tiết ở lesson 243. Hệ quả là phần logic thành hàm thuần và kiểm thử được không cần hạ tầng, đúng nguyên tắc ở lesson 68. Định nghĩa khác nhau cho môi trường phát triển và sản xuất bằng cách chọn tập tài nguyên.

**Outcome.** Tách một tài sản đang tự mở kết nối thành phần logic thuần cộng tài nguyên tiêm vào, và chứng minh phần logic kiểm thử được với mạng bị chặn.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí kiểm bằng thực nghiệm rõ ràng. Đạt khi bộ kiểm thử cho phần logic chạy xanh khi chặn mạng và không có cơ sở dữ liệu, và khi cùng mã chạy được ở hai môi trường chỉ bằng đổi tập tài nguyên, không sửa dòng nào.

**Lab.** Nhận ba tài sản tự mở kết nối. Tách thành logic thuần cộng tài nguyên. Viết kiểm thử cho phần logic, chạy với mạng bị chặn. Định nghĩa hai tập tài nguyên cho hai môi trường và chạy cùng mã ở cả hai. Bỏ một trường cấu hình bắt buộc và xác nhận nó bị bắt lúc nạp định nghĩa.

**Pitfalls.** Khởi tạo kết nối trong hàm tài sản · rẽ nhánh theo tên môi trường bên trong mã · trộn phần đọc ghi với phần biến đổi nên không kiểm thử được.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Kiểm thử phần logic xanh khi chặn mạng, và cùng mã chạy ở hai môi trường chỉ bằng đổi tập tài nguyên.

### Lesson 243 · IO managers and where data actually lands `TH`
**Prerequisites.** Lesson 242

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bộ quản lý vào ra là lớp quyết định giá trị trả về của một tài sản được ghi ở đâu và đọc lại thế nào, và nó là khái niệm dễ gây nhầm nhất của công cụ. Mặc định ghi vào hệ tệp cục bộ dạng tuần tự hoá, tiện cho thử nghiệm nhưng không phải thứ dùng cho sản xuất. Ba lựa chọn thật và điều kiện: ghi vào kho đối tượng theo định dạng cột, ghi vào bảng của kho dữ liệu, hoặc không dùng bộ quản lý vào ra và để hàm tài sản tự ghi rồi chỉ trả về siêu dữ liệu. Lựa chọn thứ ba là lựa chọn hay dùng nhất trong pipeline dữ liệu lớn, vì dữ liệu không nên đi qua tiến trình điều phối, đúng nguyên tắc ở lesson 224 và 229. Bộ quản lý vào ra theo phân mảnh và cách nó ánh xạ lát sang đường dẫn. Viết bộ quản lý vào ra riêng. Khi nào nên dùng và khi nào không: dùng cho tài sản nhỏ và trung bình, không dùng cho tài sản lớn hơn bộ nhớ tiến trình.

**Outcome.** Chọn cách ghi cho ba tài sản có kích thước khác nhau và chứng minh bằng đo bộ nhớ tiến trình rằng tài sản lớn không đi qua tiến trình điều phối.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn giữa ba phương án theo ràng buộc kích thước. Đạt khi ba lựa chọn đều có lý do dẫn về kích thước và bộ nhớ, và khi đo được bộ nhớ tiến trình điều phối gần như không tăng với tài sản 20 ghi ga byte trong khi tăng vọt nếu dùng bộ quản lý vào ra mặc định.

**Lab.** Ba tài sản kích thước 10 mê ga byte, 500 mê ga byte, và 20 ghi ga byte. Thử cả ba cách ghi cho từng tài sản, đo bộ nhớ đỉnh của tiến trình điều phối. Cài bộ quản lý vào ra riêng ghi vào kho đối tượng theo định dạng cột cho tài sản thứ hai. Với tài sản thứ ba, để hàm tự ghi và chỉ trả siêu dữ liệu.

**Pitfalls.** Dùng bộ quản lý vào ra mặc định cho tài sản lớn · trả về cả khung dữ liệu từ hàm tài sản khi dữ liệu lớn hơn bộ nhớ · viết bộ quản lý vào ra riêng khi ba cách có sẵn đã đủ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba lựa chọn có lý do dẫn về kích thước, và bộ nhớ tiến trình điều phối gần như không tăng với tài sản 20 ghi ga byte.

### Lesson 244 · Asset checks and data quality inside the graph `TH`
**Prerequisites.** Lesson 243

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Kiểm tra tài sản gắn phép kiểm chất lượng vào chính đồ thị thay vì để nó thành một bước riêng, nên kết quả kiểm hiện cạnh tài sản và người dùng hạ nguồn thấy bảng nào đang nghi ngờ mà không phải đọc nhật ký. Áp trực tiếp sáu chiều chất lượng ở lesson 211: mỗi chiều thành một kiểm tra gắn vào tài sản tương ứng. Kiểm tra chặn và kiểm tra không chặn, cùng tiêu chí chọn, nối lại lesson 213: chặn khi dữ liệu sai gây hại hơn dữ liệu trễ. Kiểm tra chạy cùng lúc vật chất hoá hay chạy riêng sau đó, cùng đánh đổi. Kiểm tra trên tài sản ngoài để bắt lỗi nguồn trước khi nó vào hệ, đúng vị trí thứ nhất trong ba vị trí ở lesson 213. Siêu dữ liệu kèm kết quả kiểm để người đọc biết lệch bao nhiêu chứ chỉ biết đạt hay không. Lịch sử kết quả kiểm theo thời gian, và đây là nơi phát hiện trôi phân bố ở lesson 215 mà không phải dựng hệ riêng.

**Outcome.** Gắn sáu chiều chất lượng thành kiểm tra tài sản, và chứng minh kiểm tra chặn dừng được đồ thị còn kiểm tra không chặn thì không.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí kiểm bằng thực nghiệm đối lập. Đạt khi sáu chiều đều có kiểm tra gắn đúng tài sản, và khi bơm cùng một lỗi vào hai tài sản có mức nghiêm trọng khác nhau thì một cái dừng đồ thị còn cái kia chạy tiếp và ghi nhận.

**Lab.** Gắn sáu kiểm tra cho các tài sản của pipeline, mỗi kiểm tra một chiều. Đặt ba chặn và ba không chặn theo tiêu chí. Bơm lỗi tương ứng từng cái và ghi hành vi. Gắn siêu dữ liệu lệch bao nhiêu vào kết quả. Xem lịch sử kết quả kiểm 30 ngày và tìm một xu hướng trôi.

**Pitfalls.** Đặt mọi kiểm tra là chặn rồi đồ thị dừng vì một cảnh báo nhỏ · chỉ báo đạt hay không mà không báo lệch bao nhiêu · gắn kiểm tra vào tài sản hạ nguồn trong khi lỗi ở nguồn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Sáu chiều có kiểm tra gắn đúng tài sản, và hai mức nghiêm trọng cho hành vi khác nhau khi bơm cùng lỗi.

### Lesson 245 · Backfilling partitions and selective materialization `TH`
**Prerequisites.** Lesson 244

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Chạy bù ở đây là vật chất hoá một tập lát, nên nó dùng chung cơ chế với chạy thường chứ không phải chế độ riêng, khác hẳn lesson 233. Ba cách chọn tập lát: theo dải thời gian, theo trạng thái thiếu, và theo chọn lọc thượng nguồn hạ nguồn. Cách thứ hai đáng chú ý: hệ thống biết lát nào chưa có nên chạy bù trở thành lấp chỗ trống, và người vận hành không phải tự tính dải ngày. Chạy bù theo chiều dọc so với theo chiều ngang: chạy hết một tài sản cho mọi ngày rồi sang tài sản sau, hay chạy hết mọi tài sản cho một ngày rồi sang ngày sau; hai thứ tự cho hai đặc tính khác nhau về khả năng phục hồi giữa chừng và về áp lực lên hệ đích. Giới hạn số lát chạy đồng thời, cùng bài toán lesson 234. Dựng lại hạ nguồn tự động khi một tài sản thượng nguồn thay đổi, và điều kiện nên bật. Theo dõi tiến độ một lần chạy bù lớn và dừng sạch sẽ.

**Outcome.** Chạy bù 90 ngày bằng cách lấp lát còn thiếu, và so số bước phải chạy với cách chạy bù ở Airflow trên cùng pipeline.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí đối chứng tuyệt đối cộng một phép so định lượng. Đạt khi kết quả 90 ngày khớp bản đối chứng từng dòng, và khi có bảng so số bước phải chạy giữa hai công cụ cho ba kịch bản chạy bù khác nhau. Đây là số đo dùng lại ở M25.

**Lab.** Xoá ngẫu nhiên 30 trong 90 lát. Chạy bù bằng cách lấp lát thiếu. Đối chiếu từng dòng với bản đối chứng. So số bước phải chạy với Airflow cho ba kịch bản: thiếu một ngày giữa, thiếu 30 ngày rải rác, và sửa logic một tài sản giữa đồ thị. Thử hai thứ tự chạy bù và đo thời gian.

**Pitfalls.** Tự tính dải ngày thay vì dùng trạng thái lát thiếu · chạy bù không giới hạn số lát đồng thời · bật dựng lại hạ nguồn tự động cho tài sản đổi liên tục.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Kết quả 90 ngày khớp từng dòng, và bảng so số bước với Airflow cho ba kịch bản.

### Lesson 246 · Lineage, the asset catalog and observability `TH`
**Prerequisites.** Lesson 245

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Đồ thị tài sản đã chứa sẵn thông tin mà ở nơi khác phải dựng công cụ riêng mới có: bảng nào sinh ra bảng nào, lần vật chất hoá cuối, kiểm tra nào đang hỏng, ai sở hữu, số dòng theo thời gian. Bảng danh mục là mặt tiền đọc được của những thứ đó. Ba câu hỏi người dùng hạ nguồn hay hỏi và cách danh mục trả lời trực tiếp: số này lấy từ đâu, bảng này cập nhật lần cuối lúc nào, và tôi đổi cột này thì hỏng cái gì. Câu thứ ba là phân tích tác động và nó đọc ngược đồ thị. Siêu dữ liệu gắn vào tài sản và vào mỗi lần vật chất hoá, cùng cách chúng hiện thành đồ thị theo thời gian. Mô tả cột và liên kết tới mã nguồn. Giới hạn: danh mục chỉ biết những gì đi qua nó, nên bảng ai đó tạo tay trong kho sẽ không xuất hiện, và đây là lý do phải có quy ước mọi bảng phục vụ đều đi qua đồ thị. Phân biệt với danh mục dữ liệu cấp tổ chức.

**Outcome.** Gắn đủ siêu dữ liệu để một người ngoài đội trả lời được ba câu hỏi hạ nguồn chỉ bằng danh mục, không hỏi ai.

**Đánh giá.** Tầng *đánh giá*. Objective đo bằng người dùng thật chứ bằng danh sách trường đã điền. Kiểm bằng quan sát: ba người chưa từng thấy hệ thống, mỗi người ba câu hỏi, ghi lại chỗ họ vướng thay vì hỏi họ thấy thế nào. Đạt khi ít nhất hai trên ba người trả lời được cả ba câu mà không cần hướng dẫn.

**Lab.** Gắn mô tả, chủ sở hữu, nhóm và số dòng cho mọi tài sản. Nối mô tả cột. Đưa danh mục cho ba người chưa từng thấy, giao ba câu hỏi, quan sát và ghi điểm vướng. Sửa theo điểm vướng rồi thử với người thứ tư. Tạo một bảng ngoài đồ thị và chỉ ra nó không có trong danh mục.

**Pitfalls.** Điền mô tả bằng cách chép lại tên tài sản · bỏ trường chủ sở hữu vì cả đội đều biết · tạo bảng phục vụ ngoài đồ thị.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ít nhất hai trên ba người ngoài đội trả lời được cả ba câu hỏi, có ghi chép điểm vướng.

### Lesson 247 · Integrating an external transformation tool - one graph instead of two `TH`
**Prerequisites.** Lesson 246

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Khi tầng biến đổi do đội khác sở hữu bằng công cụ riêng, có hai đồ thị: đồ thị điều phối và đồ thị bên trong công cụ đó. Ba cách nối và đánh đổi. Gọi nó như một bước đơn: đơn giản nhất, nhưng đồ thị điều phối chỉ thấy một đỉnh nên hỏng một mô hình phải mở nhật ký mới biết là mô hình nào. Đọc bản kê của công cụ và sinh một tài sản cho mỗi mô hình: hai đồ thị nhập làm một, thấy ngay mô hình nào hỏng và dựng lại đúng nhánh, nhưng phải giải bài toán bản kê có trước lúc nạp định nghĩa. Nối qua ranh giới dữ liệu: đội kia đọc tài sản mình bàn giao và mình không nhìn vào trong. Cách thứ ba là cách khớp với ranh giới trách nhiệm ở lesson 200: Data Engineer bàn giao tập dữ liệu có hợp đồng, đội phân tích sở hữu phần biến đổi phía sau. Chọn cách nào là quyết định tổ chức nhiều hơn kỹ thuật, và phải thoả thuận với đội kia chứ không tự quyết.

**Outcome.** Nối một công cụ biến đổi ngoài vào đồ thị bằng hai trong ba cách, và so thời gian từ lúc hỏng tới lúc biết bước nào hỏng.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn giữa các cách có đánh đổi cả kỹ thuật lẫn tổ chức. Đạt khi hai cách đều chạy và có số đo thời gian phát hiện lỗi, và khi lựa chọn cuối nêu được nó phù hợp với ranh giới trách nhiệm nào giữa hai đội.

**Lab.** Dựng một dự án biến đổi ngoài 20 bước. Nối vào đồ thị bằng cách gọi một bước đơn, đo thời gian từ lúc một bước hỏng tới lúc biết bước nào. Nối lại bằng cách sinh một tài sản cho mỗi bước, đo lại. Viết nửa trang nêu cách nào phù hợp với ranh giới trách nhiệm nào.

**Pitfalls.** Sinh tài sản từ bản kê bằng cách chạy công cụ lúc nạp định nghĩa · tự quyết cách nối mà không thoả thuận với đội sở hữu tầng biến đổi · gọi một bước đơn rồi than không quan sát được.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Hai cách đều chạy có số đo thời gian phát hiện lỗi, và lựa chọn cuối nêu được ranh giới trách nhiệm tương ứng.

### Lesson 248 · Operating Dagster - the daemon, code locations, deployment `TH`
**Prerequisites.** Lesson 247

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Không có cơ chế mới. Bài gộp module, đo năng lực vận hành. Tiến trình nền chạy lịch, cảm biến, và hàng đợi lần chạy; nó chết thì không có gì kích hoạt và hệ thống im lặng chứ không báo lỗi, nên theo dõi nó là chỉ số vận hành bắt buộc, cùng loại vấn đề với cảm biến lỗi ở lesson 241. Vị trí mã là đơn vị nạp định nghĩa, chạy trong tiến trình riêng; hệ quả là một vị trí mã lỗi không làm chết vị trí khác, và mỗi vị trí có phụ thuộc riêng, giải bài toán xung đột thư viện mà bộ thực thi phân tán của Airflow gặp ở lesson 235. Kho lưu trữ giữ trạng thái lần chạy, sự kiện và siêu dữ liệu tài sản; nó tương ứng cơ sở dữ liệu siêu dữ liệu ở lesson 225 và cần bảo trì tương tự. Triển khai mã mới và cửa sổ hai phiên bản cùng tồn tại. Ba sự cố vận hành và quy trình chẩn đoán: tiến trình nền chết, vị trí mã nạp lỗi, và kho lưu trữ phình.

**Outcome.** Chẩn đoán ba sự cố vận hành chưa từng thấy về đúng nguyên nhân, và triển khai một phiên bản mã mới không gián đoạn lịch chạy.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chẩn đoán dưới thời gian cộng một thao tác vận hành. Chấm theo bốn mục: chẩn đoán ba sự cố 45đ, triển khai không gián đoạn 20đ, sổ tay xử lý 20đ, và theo dõi tiến trình nền 15đ. Đạt khi ≥ 70/100 và mục chẩn đoán ≥ 60%.

**Lab.** Cụm Dagster có tải. Giám khảo gây ba sự cố không báo trước: giết tiến trình nền, đẩy mã lỗi vào một vị trí, và làm kho lưu trữ phình. Chẩn đoán theo quy trình, ghi số đo trước khi sửa. Triển khai phiên bản mã mới trong lúc lịch đang chạy. Nộp sổ tay xử lý và truy vấn theo dõi tiến trình nền.

**Pitfalls.** Không theo dõi tiến trình nền nên hệ thống im lặng · gộp mọi định nghĩa vào một vị trí mã · quên bảo trì kho lưu trữ như một cơ sở dữ liệu thật.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đạt ≥ 70/100 và mục chẩn đoán ≥ 60%, với sổ tay xử lý và truy vấn theo dõi tiến trình nền.

# MODULE 24 · PREFECT

**Lessons 249–260 · 24 giờ**

| | |
|---|---|
| **Objective cấp module** | Điều phối pipeline tham chiếu bằng Prefect, xử lý thất bại bằng trạng thái trả về, và tách định nghĩa luồng khỏi hạ tầng chạy nó |
| **Tiền đề** | M22 |
| **Exit criterion** | Pipeline tham chiếu chạy bằng Prefect có bản triển khai và nhóm công việc, xử lý đúng ba loại thất bại, và ghi được thời gian từ lúc bắt đầu tới lúc chạy được |
| **Kỹ năng SFIA** | `PROG` mức 4 |
| **Chế độ hỏng** | Viết luồng như một script Python rồi bỏ qua trạng thái trả về, nên thất bại đi qua mà hệ thống báo thành công |

Prefect ở mức `A`, dựng lại đúng pipeline tham chiếu. Khác biệt nền tảng với hai công cụ trước: luồng và tác vụ là hàm Python bình thường, không có lớp khai báo trung gian. Hệ quả là rào vào thấp nhất trong ba công cụ, và giá phải trả là kỷ luật xử lý trạng thái nằm ở người viết chứ ở hệ thống.

Tên đúng của công cụ là Prefect.

### Lesson 249 · Flows and tasks as plain Python functions `LT`
**Prerequisites.** Module 24: M22

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Một luồng là một hàm Python có trang trí, một tác vụ cũng vậy. Không có lớp khai báo riêng, không có tệp cấu hình bắt buộc, nên mã chạy được bằng trình thông dịch bình thường lẫn chạy được dưới sự quản lý của công cụ. Hệ quả thứ nhất: kiểm thử luồng bằng công cụ kiểm thử Python thông thường, không cần dựng hạ tầng, nối lại lesson 84. Hệ quả thứ hai và đáng chú ý hơn: trạng thái là giá trị trả về chứ không phải thứ hệ thống giữ hộ. Một tác vụ trả về đối tượng trạng thái, và mã gọi nó quyết định làm gì với trạng thái đó. Bốn trạng thái kết thúc và ý nghĩa của từng cái, gồm cả trạng thái báo bỏ qua có chủ đích khác với thất bại. Cơ chế khiến một tác vụ thất bại đi lọt: mã gọi không kiểm tra trạng thái trả về, luồng vẫn chạy tiếp và kết thúc xanh. Đây là chế độ hỏng đặc trưng của công cụ này và nó không tồn tại ở Airflow vì ở đó hệ thống tự quyết định. Đánh đổi tổng quát: tự do hơn thì kỷ luật phải tự mang.

**Outcome.** Chỉ ra trong một luồng cho trước chỗ một tác vụ thất bại đi lọt, và phát biểu cơ chế khiến luồng vẫn kết thúc xanh.

**Đánh giá.** Tầng *phân tích*. Objective là định vị một lỗi trong mã, không phải nhắc lại định nghĩa. Kiểm bằng ba đoạn luồng, mỗi đoạn có một chỗ thất bại đi lọt theo một cơ chế khác nhau. Đạt khi chỉ đúng dòng và phát biểu đúng cơ chế cho cả ba, và dự đoán phải đưa ra trước khi chạy.

**Lab.** Đọc ba đoạn luồng. Với mỗi đoạn, chỉ dòng mà thất bại đi lọt và phát biểu cơ chế, ghi lại trước khi chạy. Chạy cả ba xác nhận dự đoán. Mọi chênh lệch phải giải thích được. Viết một luồng nhỏ và chạy nó bằng trình thông dịch thường, không qua công cụ.

**Pitfalls.** Coi tác vụ như hàm thường rồi bỏ qua giá trị trả về · nhầm trạng thái bỏ qua có chủ đích với thất bại · gọi công cụ là Perfect.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chỉ đúng dòng và cơ chế cho cả ba đoạn, dự đoán trước khi chạy khớp kết quả.

### Lesson 250 · State as a first-class object, and handling it `TH`
**Prerequisites.** Lesson 249

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Trạng thái là đối tượng có kiểu, mang cả kết quả lẫn thông tin về cách tác vụ kết thúc. Lấy trạng thái thay vì lấy kết quả khi cần xử lý thất bại trong mã thay vì để luồng đổ. Ba mẫu xử lý và điều kiện dùng: để đổ và dựa vào thử lại cho lỗi tạm thời, bắt trạng thái và rẽ nhánh cho lỗi có phương án thay thế, và trả về trạng thái bỏ qua có chủ đích khi không có gì để làm. Mẫu thứ ba hay bị bỏ và nó là cách phân biệt không có dữ liệu với có lỗi, hai thứ khác nhau mà nhiều pipeline gộp làm một. Trạng thái của luồng gộp từ trạng thái các tác vụ theo quy tắc khai báo được, tương ứng bốn quy tắc gộp ở lesson 220. Nâng lỗi có kiểu để mã gọi phân biệt được, nối lại lesson 65. Ghi nhật ký có cấu trúc gắn với trạng thái, nối lại lesson 74. Móc nối chạy khi chuyển trạng thái, dùng cho cảnh báo có ngữ cảnh.

**Outcome.** Bọc ba bước của pipeline sao cho ba loại kết thúc cho ba trạng thái khác nhau, và chứng minh bằng ba lần chạy bơm lỗi.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí đúng sai tuyệt đối, kiểm bằng thực nghiệm. Đạt khi ba kịch bản bơm lỗi cho đúng ba trạng thái khác nhau, và khi kịch bản không có dữ liệu cho trạng thái bỏ qua chứ trạng thái thất bại. Hai kịch bản cho cùng một trạng thái là không đạt vì đó chính là lỗi bài này dạy cách tránh.

**Lab.** Bọc ba bước của pipeline tham chiếu. Bơm ba tình huống: lỗi kết nối tạm thời, lỗi dữ liệu xác định, và nguồn không có bản ghi mới. Xác nhận ba trạng thái khác nhau. Viết móc nối chuyển trạng thái để gửi cảnh báo có ngữ cảnh. Khai báo quy tắc gộp trạng thái luồng và kiểm bằng một tác vụ không bắt buộc thất bại.

**Pitfalls.** Gộp không có dữ liệu vào thất bại · bắt ngoại lệ quá rộng rồi nuốt mất lỗi lập trình · dựa vào trạng thái mặc định mà không khai báo quy tắc gộp.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba kịch bản cho ba trạng thái khác nhau, và kịch bản không có dữ liệu cho trạng thái bỏ qua.

### Lesson 251 · Deployments - separating the flow from where it runs `TH`
**Prerequisites.** Lesson 250

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bản triển khai là cầu nối giữa mã luồng và hạ tầng chạy nó. Cùng một luồng triển khai được nhiều lần với tham số, lịch và hạ tầng khác nhau, và đây là cách chạy cùng mã ở môi trường thử nghiệm lẫn sản xuất mà không rẽ nhánh trong mã, nối lại lesson 242. Phân biệt ba thứ hay bị gộp: định nghĩa luồng, bản triển khai, và một lần chạy. Nơi lưu mã luồng và cách tiến trình thực thi lấy được nó: từ kho mã, từ ảnh vùng chứa, hoặc từ kho đối tượng, cùng đánh đổi về tốc độ khởi động và khả năng tái lập. Tham số hoá bản triển khai để chạy bù nhận dải ngày từ ngoài thay vì sửa mã, nối lại lesson 221. Lịch gắn vào bản triển khai chứ gắn vào luồng, nên cùng luồng có hai lịch khác nhau ở hai môi trường. Phiên bản bản triển khai và cách quay lui. Bản triển khai là thứ tương ứng với đồ thị ở Airflow và với công việc ở Dagster, nên đây là điểm neo khi so ba công cụ ở M25.

**Outcome.** Triển khai cùng một luồng thành hai bản chạy trên hai hạ tầng khác nhau, và chạy bù một dải ngày bằng tham số truyền từ ngoài.

**Đánh giá.** Tầng *áp dụng*. Sản phẩm chạy được với tiêu chí đếm được. Đạt khi hai bản triển khai cùng trỏ về một định nghĩa luồng, chạy trên hai hạ tầng khác nhau, và một lần chạy bù nhận dải ngày qua tham số cho ra đúng số lần chạy tương ứng. Sửa mã để chạy bù là không đạt.

**Lab.** Triển khai luồng ở lesson 250 thành hai bản: một chạy bằng tiến trình, một chạy trong vùng chứa. Dựng hai nhóm công việc. Chạy bù 7 ngày bằng tham số. Xác nhận không dòng mã nào bị sửa giữa hai môi trường. Thử ba cách lưu mã luồng và đo thời gian khởi động từng cách.

**Pitfalls.** Rẽ nhánh theo tên môi trường bên trong mã luồng · gộp định nghĩa luồng với bản triển khai nên mỗi môi trường một bản mã · viết cứng dải ngày chạy bù vào luồng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Hai bản triển khai cùng một mã chạy trên hai hạ tầng, và chạy bù 7 ngày qua tham số sinh đúng 7 lần chạy.

### Lesson 252 · Work pools, workers and infrastructure `TH`
**Prerequisites.** Lesson 251

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Nhóm công việc là hàng đợi kèm khai báo hạ tầng; tiến trình thực thi kéo việc từ nhóm về chạy. Mô hình kéo thay vì đẩy, và hệ quả về mạng: tiến trình thực thi chủ động gọi ra nên chạy được sau tường lửa mà không cần mở cổng vào, khác mô hình của Airflow ở lesson 235. Ba kiểu hạ tầng và tiêu chí chọn: tiến trình trên máy có sẵn, vùng chứa riêng cho mỗi lần chạy, và công việc trên cụm điều phối vùng chứa; cùng ba lựa chọn với bộ thực thi ở lesson 235 nên so sánh được trực tiếp. Chi phí khởi động của từng kiểu và ảnh hưởng lên luồng nhiều tác vụ ngắn. Tiến trình thực thi có thẻ để định tuyến luồng cần tài nguyên đặc biệt. Giới hạn số lần chạy đồng thời đặt ở nhóm công việc, tương ứng nhóm tài nguyên ở lesson 234. Tiến trình thực thi chết và cơ chế phát hiện lần chạy mồ côi. Triển khai tiến trình thực thi và quy mô theo tải.

**Outcome.** Dựng hai nhóm công việc với hai kiểu hạ tầng, và đo chi phí khởi động cùng thông lượng của từng kiểu trên pipeline tham chiếu.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn hạ tầng có đánh đổi, và số đo dùng lại ở M25. Đạt khi có số đo chi phí khởi động và thông lượng cho ít nhất hai kiểu hạ tầng, và khi lựa chọn dẫn được về số đo cộng năng lực vận hành chứ bằng danh tiếng công cụ.

**Lab.** Dựng hai nhóm công việc: một chạy tiến trình, một chạy vùng chứa. Chạy pipeline tham chiếu trên cả hai, đo chi phí khởi động một tác vụ và tổng thông lượng. Đặt giới hạn số lần chạy đồng thời ở nhóm và kiểm. Giết một tiến trình thực thi giữa chừng và quan sát cơ chế phát hiện lần chạy mồ côi.

**Pitfalls.** Dùng hạ tầng vùng chứa cho luồng nhiều tác vụ ngắn · không đặt giới hạn đồng thời ở nhóm công việc · để tiến trình thực thi chạy mà không theo dõi lần chạy mồ côi.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Số đo chi phí khởi động và thông lượng cho ít nhất hai kiểu hạ tầng, và lựa chọn dẫn được về số đo.

### Lesson 253 · Schedules, event triggers and automations `TH`
**Prerequisites.** Lesson 252

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Lịch gắn vào bản triển khai, nên cùng luồng có hai lịch khác nhau ở hai môi trường. Ba kiểu lịch và tiêu chí chọn: biểu thức cron cho chu kỳ theo lịch dương, khoảng lặp cho chu kỳ đều, và lịch khai báo theo múi giờ có xử lý giờ mùa hè. Nối lại lesson 221: lịch quyết định khi nào chạy, tham số quyết định chạy cho khoảng dữ liệu nào, và hai thứ đó phải khớp nếu không sẽ lệch một chu kỳ. Kích hoạt theo sự kiện: luồng chạy khi một luồng khác kết thúc, khi một trạng thái xuất hiện, hoặc khi có tín hiệu từ ngoài. Tự động hoá là quy tắc dạng nếu thấy điều kiện này thì làm việc kia, và nó xử lý nhóm việc mà lịch không làm được: chạy lại khi thất bại, báo khi một lần chạy vượt thời lượng thường lệ, huỷ lần chạy treo. Mẫu lai cho pipeline dữ liệu: lịch theo giờ cộng kích hoạt khi nguồn báo đã nạp xong, lấy cái nào tới trước và chặn chạy trùng.

**Outcome.** Cấu hình mẫu lai gồm lịch theo giờ và kích hoạt theo sự kiện, sao cho nguồn tới sớm thì chạy sớm còn nguồn không tới thì vẫn chạy đúng giờ chốt.

**Đánh giá.** Tầng *áp dụng*. Objective là cấu hình có hành vi kiểm được bằng hai kịch bản đối lập. Đạt khi kịch bản nguồn tới sớm làm luồng chạy ngay, kịch bản nguồn không tới làm luồng vẫn chạy đúng giờ chốt, và không kịch bản nào sinh hai lần chạy chồng nhau.

**Lab.** Cấu hình lịch theo giờ cộng kích hoạt sự kiện. Kịch bản một: phát tín hiệu nguồn sẵn sàng sớm 20 phút, xác nhận chạy ngay. Kịch bản hai: không phát tín hiệu, xác nhận vẫn chạy đúng giờ chốt. Thêm tự động hoá huỷ lần chạy vượt gấp đôi thời lượng thường lệ và kiểm nó.

**Pitfalls.** Gắn lịch vào luồng thay vì vào bản triển khai · để lịch và tham số lệch nhau một chu kỳ · quên chặn chạy trùng nên cả sự kiện lẫn lịch cùng kích hoạt.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Hai kịch bản đối lập cho đúng hành vi, và không kịch bản nào sinh hai lần chạy chồng nhau.

### Lesson 254 · Retries, caching and result persistence `TH`
**Prerequisites.** Lesson 253

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Thử lại đặt ở mức tác vụ bằng tham số của hàm, và điều kiện để bật vẫn là tính bất biến ở lesson 222. Khoảng chờ tăng dần và nhiễu ngẫu nhiên. Điều kiện thử lại tuỳ biến để chỉ thử lại đúng loại lỗi tạm thời, giải trực tiếp vấn đề phân loại ở lesson 222 mà không phải bọc thủ công. Bộ nhớ đệm kết quả tác vụ: nếu đầu vào không đổi thì trả kết quả cũ thay vì chạy lại, và khoá đệm tính từ tham số theo hàm khai báo được. Đây là công cụ mạnh cho chạy bù và cho phát triển lặp, nhưng có hai bẫy: khoá đệm không tính tới dữ liệu nguồn đã đổi, và thời gian sống của đệm quá dài làm dữ liệu cũ đi. Lưu kết quả để lần chạy sau đọc lại và để tác vụ hạ nguồn nhận đầu vào mà không chạy lại thượng nguồn, cùng ràng buộc như lesson 243: kết quả lớn không nên đi qua tiến trình điều phối. Nơi lưu kết quả và cấu hình tuần tự hoá.

**Outcome.** Cấu hình thử lại có điều kiện và bộ nhớ đệm kết quả, và chứng minh đệm không trả kết quả cũ khi dữ liệu nguồn đã đổi.

**Đánh giá.** Tầng *áp dụng*. Objective có bẫy đúng đắn cụ thể là đệm quá tay. Đạt khi thử lại chỉ kích hoạt cho lỗi tạm thời và không kích hoạt cho lỗi xác định, và khi đổi dữ liệu nguồn mà không đổi tham số thì tác vụ vẫn chạy lại chứ không trả kết quả đệm.

**Lab.** Cấu hình thử lại có điều kiện cho ba loại lỗi. Bật đệm kết quả cho bước biến đổi. Chạy hai lần cùng tham số, xác nhận lần hai dùng đệm. Đổi dữ liệu nguồn mà giữ nguyên tham số, xác nhận nó vẫn chạy lại. Đo chênh lệch thời gian chạy bù có và không có đệm.

**Pitfalls.** Bật thử lại cho mọi loại lỗi · tính khoá đệm chỉ từ tham số mà bỏ trạng thái nguồn · lưu kết quả lớn qua tiến trình điều phối.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Thử lại chỉ kích hoạt cho lỗi tạm thời, và đổi dữ liệu nguồn làm tác vụ chạy lại chứ không dùng đệm.

### Lesson 255 · Subflows, task runners and concurrency `TH`
**Prerequisites.** Lesson 254

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Luồng con là một luồng gọi từ luồng khác, và nó có trạng thái riêng nên thử lại được cả cụm mà không chạy lại toàn bộ. Dùng luồng con để nhóm các bước thành đơn vị phục hồi, và đây là quyết định kích thước đỉnh ở lesson 220 nhìn từ góc Prefect. Bộ chạy tác vụ quyết định tác vụ chạy đồng thời thế nào: tuần tự, nhiều luồng, hay nhiều tiến trình; áp trực tiếp phân loại tải ở lesson 50 và 59, tải nghẽn vào ra hợp nhiều luồng, tải nghẽn tính toán cần nhiều tiến trình. Gửi tác vụ và chờ kết quả, cùng mẫu thu kết quả từ nhiều tác vụ song song. Giới hạn đồng thời ở ba mức: trong một luồng, trong một nhóm công việc, và toàn cục theo thẻ; mức thứ ba tương ứng nhóm tài nguyên ở lesson 234 và là chỗ khai báo ràng buộc dùng chung với hệ đích. Bộ chạy tác vụ trên cụm phân tán cho tải lớn. Chọn bộ chạy theo loại tải chứ theo mặc định.

**Outcome.** Chọn bộ chạy tác vụ cho hai loại tải khác nhau bằng số đo, và đặt giới hạn đồng thời toàn cục theo thẻ để bảo vệ hệ đích.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn theo loại tải với số đo, nối lại phương pháp lesson 12. Đạt khi có bảng thông lượng cho hai bộ chạy nhân hai loại tải, khi lựa chọn khớp loại tải, và khi giới hạn theo thẻ chặn được số kết nối tới hệ đích ở ngưỡng đặt ra.

**Lab.** Chạy pipeline có một phần nghẽn vào ra và một phần nghẽn tính toán. Thử ba bộ chạy tác vụ, đo thông lượng từng phần. Lập bảng. Tách phần nạp thành luồng con và thử lại riêng nó. Đặt giới hạn đồng thời theo thẻ cho các tác vụ chạm cơ sở dữ liệu và kiểm số kết nối cao nhất.

**Pitfalls.** Dùng bộ chạy nhiều luồng cho tải nghẽn tính toán · đặt giới hạn đồng thời trong luồng rồi tưởng đã chặn ràng buộc dùng chung · gộp mọi bước vào một luồng nên thử lại là chạy lại tất cả.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng hai bộ chạy nhân hai loại tải, và giới hạn theo thẻ chặn được số kết nối ở ngưỡng đặt ra.

### Lesson 256 · Blocks, variables and secret management `TH`
**Prerequisites.** Lesson 255

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Khối là cấu hình có kiểu, đặt tên, lưu ngoài mã và nạp vào lúc chạy. Khác biệt với biến thường: khối có lược đồ nên sai kiểu bị bắt sớm, và khối bí mật được mã hoá khi lưu. Ba nhóm cấu hình và chỗ đặt tương ứng, nối lại lesson 75: tham số đổi theo lần chạy truyền qua tham số bản triển khai; tham số đổi theo môi trường đặt trong biến hoặc khối; thông tin xác thực đặt trong khối bí mật. Ba nơi thông tin xác thực vẫn rò ra dù đã dùng khối bí mật: in đối tượng khối ra nhật ký, truyền qua biến môi trường mà tiến trình con ghi lại, và lưu giá trị đã giải mã vào hiện vật; cách bịt từng nơi. Tích hợp với kho bí mật ngoài và điều kiện đáng chuyển. Khối hạ tầng mô tả nơi luồng chạy, nối lại lesson 252. Quyền trên khối và ai trong đội đọc được cái gì. Xoay vòng bí mật và yêu cầu mã phải đọc lại được thay vì đọc một lần lúc khởi động.

**Outcome.** Chuyển toàn bộ thông tin xác thực sang khối bí mật, và chứng minh bằng quét rằng không giá trị nào trong kho mã, nhật ký hay hiện vật.

**Đánh giá.** Tầng *áp dụng*. Sản phẩm là cấu hình chạy được cộng bằng chứng quét. Kiểm hai lớp: luồng chạy xanh, và quét kho mã, nhật ký lẫn hiện vật bằng công cụ tìm bí mật, đạt khi không kết quả nào. Lỗi rò rỉ chỉ lộ ra khi quét thật nên không kiểm bằng câu hỏi.

**Lab.** Chuyển thông tin xác thực của pipeline tham chiếu sang khối bí mật. Bật ghi nhật ký chi tiết và chạy lại. Quét nhật ký, hiện vật và toàn bộ lịch sử kho mã. Sửa mọi chỗ rò rồi quét lại. Xoay vòng một bí mật và xác nhận lần chạy sau dùng giá trị mới không cần khởi động lại.

**Pitfalls.** In đối tượng khối ra nhật ký khi gỡ lỗi · lưu giá trị giải mã vào hiện vật · đọc bí mật một lần lúc khởi động nên xoay vòng không có hiệu lực.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Luồng chạy xanh, và quét kho mã, nhật ký lẫn hiện vật không ra thông tin xác thực nào.

### Lesson 257 · Artifacts, logging and observability `TH`
**Prerequisites.** Lesson 256

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hiện vật là đầu ra có cấu trúc gắn vào một lần chạy và xem được sau khi lần chạy kết thúc: bảng, đánh dấu, đường dẫn. Đây là chỗ đặt báo cáo chất lượng dữ liệu, số dòng theo bước, và chênh lệch so với lần chạy trước, thay vì để chúng trong nhật ký rồi phải đọc bằng mắt. Nhật ký có cấu trúc và lý do ghi khoá giá trị thay vì ghi câu, nối lại lesson 74; khi có 30 lần chạy một ngày thì lọc quan trọng hơn đọc. Ba mức nhật ký và tiêu chí dùng từng mức. Đưa nhật ký của luồng và nhật ký của tiến trình con về cùng một chỗ. Đo thời lượng từng tác vụ để biết chỗ nào chậm dần theo thời gian. Bốn chỉ số dùng chung với hai công cụ trước để M25 so được: tổng thời gian chạy, thời gian từ lúc hỏng tới lúc biết bước nào hỏng, thời gian chạy lại sau khi sửa một bước ở giữa, và số đỉnh hoặc tác vụ trong định nghĩa. Giới hạn khả năng quan sát ở tầng điều phối: nó biết luồng chạy bao lâu và hỏng ở đâu, không biết số trong bảng có đúng không.

**Outcome.** Ghi báo cáo chất lượng mỗi lần chạy thành hiện vật đọc được sau khi lần chạy kết thúc, và đo bốn chỉ số dùng chung với hai công cụ trước.

**Đánh giá.** Tầng *áp dụng*. Objective có sản phẩm và số đo cụ thể dùng lại ở M25. Đạt khi hiện vật xem được sau khi vùng chứa đã xoá và nội dung gồm số dòng theo bước cùng chênh lệch so lần trước, và khi bảng bốn chỉ số dùng đúng định nghĩa của lesson 226 và 245.

**Lab.** Ghi báo cáo chất lượng thành hiện vật dạng bảng. Xoá vùng chứa rồi mở lại hiện vật. Đo bốn chỉ số dùng chung. Ghi lại thời gian từ lúc bắt đầu module tới lúc luồng chạy được lần đầu, số đo này dùng ở M25. Gộp nhật ký luồng và nhật ký tiến trình con.

**Pitfalls.** Ghi báo cáo vào nhật ký rồi mất khi xoay vòng nhật ký · ghi câu văn thay vì khoá giá trị nên không lọc được · đo bốn chỉ số bằng định nghĩa khác với hai module trước.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Hiện vật xem được sau khi xoá vùng chứa, và bảng bốn chỉ số dùng đúng định nghĩa của hai module trước.

### Lesson 258 · Failure handling, notifications and crash hooks `TH`
**Prerequisites.** Lesson 257

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba tầng xử lý thất bại và cái mỗi tầng bắt: thử lại ở mức tác vụ cho lỗi tạm thời, xử lý trạng thái trong mã cho lỗi có phương án thay thế, và móc nối chuyển trạng thái cho việc thông báo. Móc nối chạy khi luồng hoặc tác vụ đổi trạng thái, nên nó là chỗ đặt cảnh báo có ngữ cảnh đầy đủ thay vì thông báo mặc định; nội dung phải nói ba thứ như lesson 232. Móc nối khi sập xử lý trường hợp tiến trình chết đột ngột, khác móc nối khi thất bại ở chỗ nó chạy trong điều kiện khắc nghiệt hơn, và nó không chạy được nếu máy bị giết cưỡng bức, nối lại lesson 21 và 66; nên vẫn cần dọn dẹp lúc khởi động. Tự động hoá gửi thông báo theo quy tắc, tách việc thông báo khỏi mã luồng. Gom cảnh báo cùng nguyên nhân. Lần chạy treo và phát hiện bằng tự động hoá theo thời lượng. Phân biệt luồng thất bại với luồng bị huỷ và với tiến trình thực thi chết, ba tình huống cần ba phản ứng khác nhau.

**Outcome.** Cấu hình ba tầng xử lý thất bại và chứng minh mỗi tầng bắt đúng loại tình huống của nó, gồm cả trường hợp tiến trình bị giết cưỡng bức.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí kiểm bằng bốn kịch bản khác nhau. Đạt khi bốn kịch bản cho bốn phản ứng đúng như thiết kế: lỗi tạm thời tự phục hồi không cảnh báo, lỗi xác định cảnh báo đủ ba thứ, tiến trình bị giết để lại dấu vết cho lần khởi động sau dọn, và lần chạy treo bị huỷ tự động.

**Lab.** Cấu hình ba tầng cho pipeline tham chiếu. Bơm bốn tình huống: lỗi mạng tự khỏi, lỗi dữ liệu xác định, giết cưỡng bức tiến trình, và một tác vụ treo vô hạn. Ghi phản ứng của hệ thống cho từng cái. Thêm bước dọn dẹp lúc khởi động và xác nhận nó xử lý dấu vết còn sót.

**Pitfalls.** Dựa vào móc nối khi sập cho trường hợp giết cưỡng bức · gộp luồng bị huỷ với luồng thất bại · đặt việc thông báo trong mã luồng thay vì trong móc nối.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn kịch bản cho bốn phản ứng đúng như thiết kế, gồm cả trường hợp giết cưỡng bức.

### Lesson 259 · Dynamic workflows and mapping `TH`
**Prerequisites.** Lesson 258

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Sinh số tác vụ phụ thuộc dữ liệu lúc chạy, tương ứng sinh đỉnh động ở lesson 231 nhưng tự nhiên hơn vì luồng là mã Python nên vòng lặp và điều kiện dùng được trực tiếp. Ánh xạ một tác vụ lên một danh sách để chạy song song, và cách thu kết quả. Giới hạn số tác vụ sinh ra và lý do phải đặt: một lỗi ở nguồn trả về 100.000 phần tử sẽ sinh 100.000 tác vụ. Xử lý khi một phần trong tập ánh xạ thất bại: để cả luồng đổ, bỏ qua phần hỏng và ghi nhận, hoặc thử lại riêng phần đó; ba lựa chọn và tiêu chí. Ánh xạ lồng nhau và chi phí của nó. Đánh đổi với việc để một tác vụ xử lý cả danh sách trong vòng lặp, cùng bài toán ở lesson 231: nhiều tác vụ cho khả năng quan sát và thử lại riêng, một tác vụ cho chi phí điều phối thấp. Ngưỡng chọn theo thời gian xử lý mỗi phần tử và tỉ lệ hỏng. Luồng con động khi mỗi phần tử cần một chuỗi bước chứ một bước.

**Outcome.** Chuyển một tác vụ xử lý danh sách trong vòng lặp sang ánh xạ động, và xác định ngưỡng mà cách nào rẻ hơn bằng thực nghiệm.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn giữa hai cách có đánh đổi hai chiều, và số đo so được với lesson 231. Đạt khi có bảng thực nghiệm ít nhất bốn kích thước danh sách kèm tổng thời gian và thời gian phát hiện lỗi, và khi ngưỡng chọn ra biện minh bằng cả hai chỉ số.

**Lab.** Tác vụ nạp N tệp, chạy ở N bằng 5, 50, 500, 5.000. Cài cả hai cách. Đo tổng thời gian và thời gian từ lúc một tệp hỏng tới lúc biết tệp nào. So bảng với kết quả lesson 231. Đặt giới hạn số tác vụ sinh ra và thử vượt. Cho một phần tử hỏng và thử ba cách xử lý.

**Pitfalls.** Không đặt giới hạn số tác vụ sinh ra · để cả luồng đổ khi một phần tử trong 5.000 hỏng · chọn cách theo tổng thời gian mà bỏ thời gian phát hiện lỗi.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng bốn kích thước danh sách có cả hai chỉ số, và ngưỡng chọn ra biện minh bằng cả hai.

### Lesson 260 · Operating Prefect - self-hosted against Cloud `TH`
**Prerequisites.** Lesson 259

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Không có cơ chế mới. Bài gộp module. Hai cách vận hành và đánh đổi: máy chủ tự dựng cho toàn quyền kiểm soát và dữ liệu không ra ngoài, nhưng phải vận hành máy chủ, cơ sở dữ liệu và bản sao lưu; dịch vụ đám mây bỏ được phần đó nhưng siêu dữ liệu lần chạy nằm ngoài và có chi phí theo mức dùng. Điều cần rõ ở cả hai cách: dữ liệu của mình không đi qua đó, chỉ siêu dữ liệu đi, nên câu hỏi tuân thủ là về siêu dữ liệu chứ về dữ liệu. Cơ sở dữ liệu của máy chủ tự dựng cần bảo trì như một cơ sở dữ liệu thật, áp kiến thức M11: phình, sao lưu, di trú khi nâng cấp. Ba sự cố vận hành và quy trình chẩn đoán: tiến trình thực thi không nhận việc, lần chạy mồ côi sau khi tiến trình thực thi chết, và cơ sở dữ liệu máy chủ phình. Triển khai phiên bản mã mới và cửa sổ hai phiên bản cùng tồn tại. Sao lưu và thứ mất khi mất cơ sở dữ liệu máy chủ.

**Outcome.** Chẩn đoán ba sự cố vận hành chưa từng thấy, và nêu tiêu chí chọn giữa máy chủ tự dựng với dịch vụ đám mây cho một đội cho trước.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chẩn đoán cộng một quyết định kiến trúc. Chấm theo bốn mục: chẩn đoán ba sự cố 45đ, tiêu chí chọn cách vận hành 25đ, sổ tay xử lý 20đ, và sao lưu 10đ. Đạt khi ≥ 70/100 và mục chẩn đoán ≥ 60%. Phần tiêu chí chọn phải nêu rõ cái gì đi ra ngoài và cái gì không.

**Lab.** Cụm Prefect tự dựng có tải. Giám khảo gây ba sự cố không báo trước. Chẩn đoán theo quy trình, ghi số đo trước khi sửa. Viết tiêu chí chọn cho hai đội khác nhau về quy mô và ràng buộc tuân thủ. Nộp sổ tay xử lý và quy trình sao lưu cơ sở dữ liệu máy chủ.

**Pitfalls.** Chọn dịch vụ đám mây mà không xác định siêu dữ liệu nào ra ngoài · bỏ bảo trì cơ sở dữ liệu máy chủ tự dựng · khởi động lại tiến trình thực thi khi gặp sự cố thay vì chẩn đoán.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đạt ≥ 70/100 và mục chẩn đoán ≥ 60%, với tiêu chí chọn nêu rõ cái gì ra ngoài.

# MODULE 25 · CHOOSING AN ORCHESTRATOR

**Lessons 261–266 · 12 giờ**

| | |
|---|---|
| **Objective cấp module** | Chấm ba công cụ điều phối trên chín chiều, mỗi ô dẫn một quan sát từ lab của chính mình, và bảo vệ một lựa chọn cho đội có ràng buộc cho trước |
| **Tiền đề** | M22 · M23 · M24 |
| **Exit criterion** | Ma trận chín chiều đạt rà soát chéo, mọi ô truy được về lab, và giữ vững hoặc đổi kết luận có lý do khi ràng buộc bị đổi giữa buổi |
| **Kỹ năng SFIA** | `ARCH` mức 4 |
| **Chế độ hỏng** | Chấm theo cảm nhận hoặc chép bảng so sánh của nhà cung cấp, cho ra kết luận không đứng vững khi ràng buộc đổi |

Module chỉ chạy được vì ba module trước đã dựng cùng một pipeline tham chiếu và đo cùng bốn chỉ số ở lesson 226, 245 và 257. Không cùng bài toán thì đây là bài liệt kê tính năng, không phải bài so sánh, cùng ràng buộc với M18 và M31.

Bốn bài đầu dựng tiêu chí và đo, bài thứ năm xét một công cụ ở mức `C`, bài cuối là buổi bảo vệ.

### Lesson 261 · Nine dimensions, and how to score each from lab evidence `LT`
**Prerequisites.** Module 25: M22 · M23 · M24

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Chín chiều đánh giá và cách chuyển từng chiều thành một phép đo thực hiện được. Khả năng mô hình hoá phụ thuộc: đồ thị công cụ có diễn tả được lineage dữ liệu không, hay phải giữ cho khớp bằng tay. Chạy bù và chạy lại chọn lọc: chạy lại một ngày tốn bao nhiêu thao tác và chạy lại bao nhiêu bước, số đo đã có ở lesson 233 và 245. Kích hoạt theo sự kiện: có sẵn hay phải tự dựng, và có chiếm tài nguyên chờ không, nối lại lesson 230 và 241. Khả năng quan sát: thời gian từ lúc hỏng tới lúc biết bước nào hỏng. Công sức vận hành: số thành phần phải chạy, đường nâng cấp, ai trực. Bảo mật: thông tin xác thực đặt ở đâu và ai đọc được. Quản lý phiên bản: định nghĩa nộp vào kho mã được bao nhiêu phần. Chi phí: hạ tầng cộng thời gian người. Kỹ năng đội: mất bao lâu để người thứ hai sửa được một pipeline. Nguyên tắc chấm: mỗi ô dẫn một quan sát có số hoặc có ảnh chụp từ lab của chính mình; ba nguồn không được dùng là bảng so sánh của nhà cung cấp, bài xếp hạng, và cảm nhận về cú pháp.

**Outcome.** Phát biểu cho từng chiều trong chín chiều một phép đo thực hiện được trên lab đã làm, kèm đơn vị đo.

**Đánh giá.** Tầng *hiểu*. Bài dựng tiêu chí, chưa đo, nên objective dừng ở chỗ chuyển một chiều mơ hồ thành một phép đo lặp lại được. Kiểm bằng rà soát: mỗi phép đo phải nêu làm gì, đo cái gì, đơn vị là gì, và người khác lặp lại được. Chiều nào chỉ có tính từ mà không có phép đo thì không tính.

**Lab.** Với mỗi chiều, viết một phép đo gồm thao tác, đại lượng và đơn vị. Đối chiếu với số đo đã có ở lesson 226, 245 và 257 xem chiều nào đã có sẵn dữ liệu. Đổi bài với một học viên khác và thử thực hiện phép đo của người kia trên lab của mình; phép đo nào không lặp lại được thì viết lại.

**Pitfalls.** Chấm bằng tính từ như mạnh, linh hoạt, dễ dùng · lấy số liệu từ tài liệu nhà cung cấp · đặt phép đo mà chỉ người viết mới thực hiện được.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chín phép đo đều nêu đủ thao tác, đại lượng và đơn vị, và người khác lặp lại được trên lab của họ.

### Lesson 262 · Modelling power - task graph against asset graph on one pipeline `TH`
**Prerequisites.** Lesson 261

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Trục cho khác biệt lớn nhất giữa ba công cụ, và lý do nằm ở mô hình chứ ở chất lượng cài đặt. Đồ thị tác vụ mô hình hoá việc phải làm, nên quan hệ giữa các bảng là thứ người viết phải khai báo riêng và giữ cho khớp. Đồ thị tài sản mô hình hoá thứ được tạo ra, nên quan hệ giữa các bảng chính là đồ thị. Prefect nằm ở giữa: mã Python thuần nên đồ thị suy ra từ lời gọi hàm, linh hoạt nhất nhưng không có khái niệm tài sản sẵn. Bốn câu hỏi vận hành dùng để đo trục này, và ba câu đầu đã đặt ở lesson 237: bảng nào cũ, đổi cột này hỏng cái gì, dựng lại một bảng giữa đồ thị phải dựng thêm gì, và lát nào còn thiếu. Với mỗi câu, đo số thao tác và thời gian để trả lời trên từng công cụ. Cảnh báo khi đọc số: một phần chênh lệch đến từ quyết định chia bước ở lesson 220 chứ từ công cụ, nên phải tách hai yếu tố trước khi kết luận.

**Outcome.** Đo bốn câu hỏi vận hành trên ba công cụ cho cùng pipeline, và tách phần chênh lệch do mô hình khỏi phần do quyết định chia bước.

**Đánh giá.** Tầng *phân tích*. Objective đòi phân rã khác biệt về đúng nguyên nhân, việc khó hơn thu thập số. Đạt khi bốn câu hỏi đều có số đo trên cả ba công cụ, và khi ít nhất một chênh lệch được tách rõ thành phần do mô hình và phần do cách chia bước, có lập luận kèm số.

**Lab.** Với bốn câu hỏi vận hành, đo số thao tác và thời gian trả lời trên ba công cụ. Lập bảng bốn nhân ba. Chạy lại phép đo với cách chia bước khác trên cùng công cụ, để tách hai yếu tố. Viết một đoạn nêu chênh lệch nào đến từ mô hình.

**Pitfalls.** Gán mọi chênh lệch cho công cụ · đo trên ba pipeline khác nhau · so bằng số tính năng thay vì bằng thời gian trả lời câu hỏi vận hành.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn câu hỏi có số đo trên cả ba công cụ, và ít nhất một chênh lệch được tách thành hai phần có lập luận.

### Lesson 263 · Backfill, replay and recovery compared under the same induced failure `TH`
**Prerequisites.** Lesson 262

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Trục thứ hai và là trục quan trọng nhất về vận hành, vì chạy bù và phục hồi là việc làm thường xuyên còn dựng pipeline là việc làm một lần. Ba kịch bản chuẩn áp lên cả ba công cụ với cùng dữ liệu và cùng lỗi: thiếu một ngày ở giữa dải, thiếu 30 ngày rải rác, và sửa logic một bước ở giữa đồ thị rồi phải dựng lại hạ nguồn. Với mỗi kịch bản, ba số đo: số thao tác người vận hành phải làm, số bước hệ thống phải chạy, và thời gian tới khi dữ liệu đúng trở lại. Số đo thứ nhất đo giao diện, thứ hai đo mô hình, thứ ba đo cả hai cộng hạ tầng. Kịch bản thứ tư khó hơn và phân hoá ba công cụ rõ nhất: giết tiến trình giữa chừng một lần chạy bù dài rồi tiếp tục, đo lượng việc bị làm lại. Ràng buộc bắt buộc: kết quả cuối của cả ba công cụ phải khớp cùng một bản đối chứng, nếu không thì số đo tốc độ vô nghĩa.

**Outcome.** Đo ba kịch bản chạy bù trên ba công cụ với cùng dữ liệu, và chứng minh kết quả cuối của cả ba khớp cùng một bản đối chứng.

**Đánh giá.** Tầng *phân tích*. Objective có ràng buộc đúng đắn làm điều kiện trước khi số tốc độ có nghĩa. Đạt khi kết quả cuối của cả ba công cụ khớp bản đối chứng từng dòng, và khi bảng ba kịch bản nhân ba công cụ có đủ ba số đo mỗi ô. Nhanh mà lệch một dòng thì ô đó không tính.

**Lab.** Sinh bản đối chứng 90 ngày. Với mỗi công cụ, chạy ba kịch bản và ghi ba số đo. Đối chiếu kết quả cuối từng dòng với bản đối chứng. Thêm kịch bản thứ tư: giết tiến trình giữa chừng chạy bù, đo lượng việc bị làm lại trên từng công cụ.

**Pitfalls.** So tốc độ trước khi đối chiếu kết quả · dùng dải ngày khác nhau cho ba công cụ · đo số thao tác người vận hành mà bỏ số bước hệ thống chạy.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Kết quả cuối cả ba công cụ khớp bản đối chứng từng dòng, và bảng ba nhân ba có đủ ba số đo mỗi ô.

### Lesson 264 · Operational cost - infrastructure, upgrade path and on-call load `TH`
**Prerequisites.** Lesson 263

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Trục ít được đo nhất nhưng quyết định nhiều nhất sau một năm. Bốn thành phần chi phí vận hành: hạ tầng phải chạy, thời gian nâng cấp, tải trực khi hỏng, và thời gian đưa người mới vào. Hạ tầng đo bằng số tiến trình phải chạy và tài nguyên chúng chiếm ở trạng thái rỗi, số đã có từ lesson 236, 248 và 260. Nâng cấp đo bằng số bước và có phải di trú lược đồ không, dữ liệu từ ba bài vận hành đó. Tải trực đo bằng số loại sự cố đặc trưng của công cụ và thời gian chẩn đoán trung bình, lấy từ chính ba bài vận hành. Thời gian đưa người mới vào đo bằng thực nghiệm: đưa pipeline cho một học viên chưa học công cụ đó và đo thời gian tới khi họ sửa được một lỗi. Chi phí giấy phép nếu có. Nguyên tắc: chi phí vận hành phần lớn là thời gian người chứ tiền hạ tầng, nên đo bằng giờ rồi mới quy ra tiền.

**Outcome.** Đo bốn thành phần chi phí vận hành cho ba công cụ, và quy chúng về cùng một đơn vị để so được.

**Đánh giá.** Tầng *đánh giá*. Objective đòi quy nhiều loại chi phí khác đơn vị về một thước đo chung, và nêu giả định của phép quy đó. Đạt khi bốn thành phần đều có số cho cả ba công cụ, và khi phép quy về đơn vị chung nêu rõ giả định về đơn giá giờ người và chu kỳ nâng cấp.

**Lab.** Đo tài nguyên rỗi của ba cụm. Đếm số bước nâng cấp từ ghi chép lesson 236, 248, 260. Liệt kê loại sự cố đặc trưng và thời gian chẩn đoán của từng cái. Đưa pipeline cho một học viên chưa học công cụ đó, giao một lỗi, đo thời gian họ sửa được. Quy tất cả về giờ người mỗi tháng và nêu giả định.

**Pitfalls.** Đo chi phí hạ tầng mà bỏ thời gian người · so chi phí mà không nêu giả định về đơn giá · bỏ phép thử thời gian đưa người mới vào vì tốn công.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn thành phần có số cho cả ba công cụ, và phép quy về đơn vị chung nêu rõ giả định.

### Lesson 265 · Kestra `C` - YAML-declared flows, and when a team wants no Python `LT`
**Prerequisites.** Lesson 261

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Kestra ở mức `C`: biết dùng đúng tình huống, không dựng lab. Luồng khai báo bằng YAML thay vì bằng Python, và hệ quả kéo theo. Điều kiện khiến một đội chọn hướng đó: người viết luồng không phải lập trình viên, tổ chức muốn định nghĩa rà soát được bởi người không đọc Python, hoặc muốn tránh phụ thuộc Python lan vào tầng điều phối. Giá phải trả: logic điều kiện phức tạp diễn đạt trong YAML dài dòng hơn và khó kiểm thử hơn, và tới một ngưỡng thì người ta viết Python bên trong YAML, lúc đó mất cả hai lợi thế. Nguyên tắc tổng quát áp được cho mọi công cụ khai báo: ngôn ngữ khai báo mạnh ở phần cấu trúc lặp lại, yếu ở phần logic rẽ nhánh nhiều. Cách đánh giá một công cụ ở mức `C` một cách trung thực: đọc tài liệu chính thức, xác định mô hình của nó, nêu điều kiện phù hợp, và nói rõ mình chưa chạy nên chưa biết gì về vận hành thật. Không kết luận về hiệu năng hay độ ổn định khi chưa có lab.

**Outcome.** Phát biểu điều kiện khiến một đội nên cân nhắc Kestra, và nói rõ kết luận nào không đưa ra được vì chưa có lab.

**Đánh giá.** Tầng *hiểu*. Công cụ ở mức `C` nên objective không thể là dựng hay đo. Kiểm bằng một đoạn viết: phải nêu mô hình của công cụ, điều kiện phù hợp hai chiều, và ít nhất hai kết luận cố ý không đưa ra kèm lý do thiếu bằng chứng. Đoạn viết khẳng định về hiệu năng hay độ ổn định thì không đạt, vì đó đúng là lỗi bài này dạy cách tránh.

**Lab.** Đọc tài liệu chính thức của Kestra. Viết nửa trang: mô hình của công cụ, ba điều kiện khiến đội nên cân nhắc, hai điều kiện khiến không nên, và ít nhất hai kết luận mình cố ý không đưa ra vì chưa chạy lab. Đối chiếu mô hình của nó với ba công cụ đã học.

**Pitfalls.** Kết luận về hiệu năng từ tài liệu tiếp thị · xếp Kestra vào ma trận lesson 261 như thể đã có lab · bỏ qua ngưỡng mà YAML bắt đầu chứa Python.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đoạn viết nêu đủ mô hình, điều kiện hai chiều, và ít nhất hai kết luận cố ý không đưa ra kèm lý do.

### Lesson 266 · The decision - defend one choice for a team with given constraints `KT`
**Prerequisites.** Lesson 265

**In-class (120 phút).** 75 phút làm bài độc lập · 45 phút chữa bài và phân tích lỗi theo nhóm

**Learn.** Không có nội dung mới. Buổi bảo vệ quyết định chọn công cụ điều phối.

**Outcome.** Chọn một công cụ điều phối cho một đội có ràng buộc cho trước, bảo vệ lựa chọn bằng ma trận bằng chứng, và điều chỉnh kết luận khi hội đồng đổi một ràng buộc giữa buổi.

**Đánh giá.** Tầng *đánh giá*. Bài kiểm của module, đo năng lực chọn giữa các phương án và bảo vệ dưới chất vấn. Không kiểm bằng đề có đáp án đúng vì chọn công cụ nào cũng đạt nếu lập luận đứng vững. Thang điểm: A 25đ ma trận chín chiều có bằng chứng từ lab · B 20đ lập luận từ ràng buộc đội tới lựa chọn · C 20đ nêu được cái mình đánh đổi · D 15đ điều kiện khiến nên xem lại quyết định · E 20đ giữ vững hoặc đổi kết luận có lý do khi ràng buộc bị đổi. Đạt khi ≥ 70/100 và phần E ≥ 60%.

**Lab.** Nhận mô tả một đội: số người, kỹ năng Python, ngân sách hạ tầng, yêu cầu độ trễ, số pipeline, ai trực khi hỏng. Trình bày 20 phút, chất vấn 20 phút. Giữa buổi hội đồng đổi một ràng buộc, ví dụ số pipeline tăng gấp mười, người duy nhất biết Python nghỉ việc, hoặc yêu cầu tuân thủ cấm siêu dữ liệu ra ngoài.

**Pitfalls.** Bảo vệ công cụ mình thích thay vì công cụ hợp ràng buộc · không nêu được mình đánh đổi cái gì · đổi kết luận khi bị chất vấn mà không có bằng chứng mới, hoặc giữ nguyên khi ràng buộc mới đã lật ngược lập luận.

**Self-study (2,4 giờ).** Không có bài tự học. Nếu không đạt, theo phụ lục khắc phục khi không đạt cổng

**Done when.** Đạt ≥ 70/100 và phần E ≥ 60%.

# MODULE 26 · DATA CONTRACTS AND DATASET HANDOVER

**Lessons 267–276 · 20 giờ**

| | |
|---|---|
| **Objective cấp module** | Bàn giao một tập dữ liệu có hợp đồng thực thi được, thương lượng được với đội nguồn, và đổi được hợp đồng mà không làm vỡ hạ nguồn |
| **Tiền đề** | M25 · M20 |
| **Exit criterion** | Đạt Cổng 6 ≥ 70/100: đổi lược đồ có kiểm soát, chạy bù 30 ngày, và bàn giao ba tập dữ liệu để người khác dựng mô hình mà không hỏi lại |
| **Kỹ năng SFIA** | `DTAN` mức 4 · `RLMT` mức 3 |
| **Chế độ hỏng** | Viết hợp đồng rồi để đó, không có phép kiểm tự động và không có ai ở đội nguồn biết nó tồn tại |

Module đóng chặng 5 và nó là chỗ vai trò Data Engineer gặp phần tổ chức. Hợp đồng mười một khai báo đã dựng ở lesson 216; module này làm bốn việc mà bài đó chưa làm: đánh phiên bản, thực thi, thương lượng, và bàn giao có diễn tập.

Phần lớn khó khăn ở đây không phải kỹ thuật. Đội nguồn không có động lực giữ hợp đồng nếu họ không thấy lợi, nên thuyết phục bằng hậu quả cụ thể là kỹ năng chính của module.

### Lesson 267 · From pipeline contract to data product `LT`
**Prerequisites.** Module 26: M25 · M20

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Hợp đồng ở lesson 216 mô tả một pipeline; sản phẩm dữ liệu mô tả một thứ có người dùng, có chủ sở hữu, có vòng đời và có cam kết. Bốn thứ một sản phẩm dữ liệu có mà một bảng không có: giao diện ổn định được đánh phiên bản, cam kết mức dịch vụ công bố, người chịu trách nhiệm có tên, và quy trình đổi. Phân biệt tập dữ liệu nội bộ với tập dữ liệu công khai trong tổ chức: cái đầu đổi tự do, cái sau đổi theo quy trình; đánh dấu rõ cái nào là cái nào là việc rẻ và tránh được nhiều tranh chấp. Ba vai trò quanh một sản phẩm dữ liệu và trách nhiệm của từng vai: đội nguồn sinh dữ liệu, Data Engineer biến đổi và bàn giao, đội tiêu thụ dùng nó. Ranh giới trách nhiệm khi số sai: ai điều tra trước, và quy tắc điều tra ngược từ đích về nguồn. Vì sao đầu tư vào hợp đồng rẻ hơn trả lời câu hỏi lặp lại, tính bằng giờ người mỗi tháng.

**Outcome.** Phân loại các tập dữ liệu hiện có thành nội bộ và công khai, và phát biểu bốn thuộc tính sản phẩm cho những cái công khai.

**Đánh giá.** Tầng *hiểu*. Bài dựng khung cho chín bài sau. Đạt khi phân loại có tiêu chí viết ra được chứ theo cảm tính, và khi bốn thuộc tính của ít nhất hai tập dữ liệu công khai đều cụ thể: phiên bản có số, cam kết có giờ, chủ sở hữu có tên, quy trình đổi có bước.

**Lab.** Lấy các bảng đầu ra của nền tảng ở lesson 217. Phân loại nội bộ hay công khai kèm tiêu chí. Với hai bảng công khai, viết bốn thuộc tính sản phẩm. Ước lượng số giờ mỗi tháng đội đang mất vì trả lời câu hỏi lặp lại về các bảng đó.

**Pitfalls.** Coi mọi bảng là công khai nên không đổi được gì · ghi chủ sở hữu là tên nhóm · phát biểu cam kết bằng tính từ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân loại có tiêu chí viết ra, và bốn thuộc tính của hai tập dữ liệu công khai đều cụ thể.

### Lesson 268 · Versioning a contract and the deprecation window `TH`
**Prerequisites.** Lesson 267

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Đánh phiên bản hợp đồng để hạ nguồn biết cái gì đổi và khi nào. Phân loại thay đổi theo mức ảnh hưởng, nối lại lesson 209: thêm cột tuỳ chọn tương thích ngược nên tăng phiên bản phụ; xoá cột, đổi kiểu, đổi tên phá vỡ nên tăng phiên bản chính; đổi ngữ nghĩa mà không đổi cấu trúc cũng phá vỡ và đây là loại nguy hiểm nhất vì không có tín hiệu kỹ thuật, nối lại lesson 89. Mẫu mở rộng rồi thu hẹp cho thay đổi phá vỡ, cùng bốn bước với lesson 121 và 181: thêm cái mới, ghi cả hai, chuyển người đọc, rồi bỏ cái cũ. Cửa sổ ngừng dùng là khoảng thời gian giữa bước ba và bước bốn, và nó phải công bố trước chứ không quyết định lúc sắp xoá. Cách biết ai còn dùng cột sắp bỏ: nhật ký truy vấn của kho dữ liệu, nối lại lesson 165. Chạy song song hai phiên bản và chi phí của nó. Bỏ phiên bản cũ và thủ tục xác nhận không còn ai dùng.

**Outcome.** Thực hiện một thay đổi phá vỡ theo mẫu bốn bước với cửa sổ ngừng dùng công bố trước, và xác nhận không còn ai dùng phiên bản cũ trước khi bỏ.

**Đánh giá.** Tầng *áp dụng*. Objective có quy trình nhiều bước với tiêu chí kiểm được ở từng bước. Đạt khi bốn bước đều triển khai riêng và quay lui được độc lập, và khi chứng minh được không còn truy vấn nào chạm cột cũ trong 14 ngày trước khi bỏ, bằng nhật ký truy vấn chứ bằng hỏi miệng.

**Lab.** Đổi kiểu một cột trong tập dữ liệu công khai theo bốn bước. Công bố cửa sổ ngừng dùng. Dùng nhật ký truy vấn tìm ai còn dùng cột cũ và liên hệ. Chờ tới khi không còn truy vấn nào trong 14 ngày rồi mới bỏ. Thử quay lui ở từng bước.

**Pitfalls.** Quyết định cửa sổ ngừng dùng lúc sắp xoá · hỏi miệng xem còn ai dùng không thay vì xem nhật ký truy vấn · gộp bước chuyển người đọc với bước bỏ cột cũ vào một lần triển khai.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn bước triển khai riêng và quay lui được, và nhật ký truy vấn xác nhận không ai dùng cột cũ trong 14 ngày.

### Lesson 269 · Enforcing a contract at the boundary `TH`
**Prerequisites.** Lesson 268

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hợp đồng không có phép kiểm tự động chỉ là lời hứa, nối lại lesson 216. Hai biên cần thực thi và cái mỗi biên bảo vệ: biên nhận kiểm nguồn có giữ đúng cam kết với mình không, biên phát kiểm mình có giữ đúng cam kết với hạ nguồn không. Nhiều đội chỉ làm biên thứ hai và bỏ biên thứ nhất, nên khi nguồn đổi thì phát hiện ở tận cuối. Ba nơi chạy phép kiểm và cái mỗi nơi bắt, nối lại lesson 213: trong tích hợp liên tục trên dữ liệu mẫu cố định, trong pipeline trên dữ liệu thật, và theo lịch riêng để phát hiện trôi khi pipeline không chạy. Hành vi khi vi phạm: chặn hay cảnh báo, và quy tắc chọn theo loại vi phạm chứ theo thói quen. Sinh phép kiểm tự động từ chính tài liệu hợp đồng thay vì viết tay hai nơi, tránh hai bản lệch nhau. Đo tỉ lệ vi phạm theo thời gian như chỉ số sức khoẻ quan hệ với đội nguồn. Báo cáo tuân thủ hợp đồng gửi định kỳ cho cả hai phía.

**Outcome.** Cài thực thi hợp đồng ở cả hai biên và chứng minh vi phạm ở biên nhận được phát hiện trước khi nó lan xuống hạ nguồn.

**Đánh giá.** Tầng *áp dụng*. Objective có tiêu chí kiểm bằng thực nghiệm so sánh. Đạt khi bơm một vi phạm vào nguồn thì biên nhận bắt được trong lần chạy đầu tiên, còn khi tắt biên nhận thì vi phạm đó đi tới tận bảng đích rồi mới lộ, đo bằng số bước dữ liệu sai đi qua.

**Lab.** Cài phép kiểm ở cả hai biên, sinh tự động từ tài liệu hợp đồng. Bơm ba vi phạm vào nguồn: thêm cột bắt buộc, đổi kiểu, và tỉ lệ giá trị rỗng tăng vọt. Đo số bước dữ liệu sai đi qua khi có và không có biên nhận. Chạy phép kiểm theo lịch riêng khi pipeline không chạy.

**Pitfalls.** Chỉ thực thi ở biên phát · viết phép kiểm tay tách rời tài liệu hợp đồng nên hai bản lệch · đặt mọi vi phạm là chặn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Vi phạm bị bắt ở biên nhận trong lần chạy đầu, và số bước dữ liệu sai đi qua giảm rõ khi bật biên nhận.

### Lesson 270 · Negotiating with the source team `TH`
**Prerequisites.** Lesson 269

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phần khó nhất của hợp đồng dữ liệu là tổ chức chứ kỹ thuật: đội nguồn không có động lực giữ hợp đồng nếu họ không thấy lợi, và họ thường không biết ai đang phụ thuộc vào bảng của họ. Ba thứ phải chuẩn bị trước khi nói chuyện: hậu quả cụ thể đã xảy ra với số liệu, danh sách người dùng cuối bị ảnh hưởng, và đề xuất cụ thể mình muốn họ làm gì. Trình bày bằng hậu quả nghiệp vụ chứ bằng thuật ngữ kỹ thuật: báo cáo doanh thu sai ba ngày thì nói thế, không nói lược đồ thay đổi gây lỗi ép kiểu. Bốn thứ có thể đổi lại để họ dễ nhận: mình nhận thông báo trước thay vì đòi họ không đổi, mình tự viết phép kiểm thay vì đòi họ viết, mình nhận cửa sổ chuyển đổi dài hơn, và mình giúp họ thấy ai đang dùng dữ liệu của họ. Ghi lại thoả thuận thành văn bản có người ký. Leo thang khi không thoả thuận được, và khi nào chấp nhận rằng mình phải tự chịu.

**Outcome.** Chuẩn bị và trình bày một đề xuất hợp đồng với đội nguồn, dùng hậu quả nghiệp vụ chứ thuật ngữ kỹ thuật, và đạt được một thoả thuận ghi thành văn bản.

**Đánh giá.** Tầng *đánh giá*. Objective đo bằng kết quả cuộc trao đổi chứ bằng nội dung chuẩn bị. Kiểm bằng đóng vai: một học viên khác đóng vai trưởng nhóm đội nguồn có ưu tiên riêng và động lực từ chối. Đạt khi đạt được thoả thuận có ít nhất hai điều khoản cụ thể, và khi người đóng vai xác nhận lập luận dựa trên hậu quả nghiệp vụ chứ thuật ngữ.

**Lab.** Chuẩn bị ba thứ cho một bảng nguồn thật: hậu quả đã xảy ra có số, danh sách người dùng bị ảnh hưởng lấy từ nhật ký truy vấn, và đề xuất cụ thể. Đóng vai 20 phút với một học viên khác. Ghi thoả thuận thành văn bản. Đổi vai và làm lại.

**Pitfalls.** Trình bày bằng thuật ngữ kỹ thuật · đòi đội nguồn không bao giờ đổi lược đồ · không chuẩn bị thứ gì đổi lại để họ dễ nhận.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đạt thoả thuận có ít nhất hai điều khoản cụ thể, và người đóng vai xác nhận lập luận dựa trên hậu quả nghiệp vụ.

### Lesson 271 · Serving the consumer - documentation, fixtures and sample queries `TH`
**Prerequisites.** Lesson 270

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bàn giao tốt đo bằng số câu hỏi người nhận phải đặt, nối lại lesson 200. Năm thứ người tiêu thụ cần và thứ tự ưu tiên: tài liệu cột viết cho người không có ngữ cảnh, dữ liệu mẫu cố định để họ viết kiểm thử, truy vấn mẫu cho ba câu hỏi thường gặp nhất, sơ đồ lineage tới nguồn, và cách liên hệ khi có vấn đề. Dữ liệu mẫu cố định là thứ hay bị bỏ nhất và giá trị cao nhất: nó cho người nhận viết kiểm thử mà không cần chạm dữ liệu thật, nối lại lesson 84 và 87. Tài liệu cột viết thế nào để dùng được: nêu ngữ nghĩa nghiệp vụ, dải giá trị hợp lệ, và cách xử lý giá trị rỗng, chứ không chép lại tên cột. Truy vấn mẫu tiết kiệm nhiều nhất vì nó trả lời trước ba câu hỏi chắc chắn được hỏi. Đặt tài liệu ở nơi người nhận tìm thấy chứ nơi mình tiện để. Đo mức dùng tài liệu và số câu hỏi lặp lại như chỉ số chất lượng bàn giao.

**Outcome.** Chuẩn bị gói bàn giao đủ năm thứ, và chứng minh bằng quan sát rằng người nhận dựng được thứ họ cần với không quá một câu hỏi.

**Đánh giá.** Tầng *đánh giá*. Objective đo bằng người nhận thật. Kiểm bằng quan sát: hai học viên khác nhận gói bàn giao và mỗi người dựng một thứ khác nhau trên tập dữ liệu, ghi lại mọi câu phải hỏi. Đạt khi tổng số câu hỏi của cả hai không quá hai, và khi cả hai viết được kiểm thử bằng dữ liệu mẫu cố định.

**Lab.** Chuẩn bị gói bàn giao đủ năm thứ cho một tập dữ liệu. Đưa cho hai học viên khác với hai yêu cầu khác nhau. Quan sát và ghi mọi câu hỏi cùng điểm vướng. Sửa gói theo điểm vướng. Đưa cho người thứ ba và đo lại.

**Pitfalls.** Chép tên cột vào ô mô tả · bàn giao mà không kèm dữ liệu mẫu cố định · đặt tài liệu ở kho riêng của đội mình.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tổng câu hỏi của hai người nhận không quá hai, và cả hai viết được kiểm thử bằng dữ liệu mẫu cố định.

### Lesson 272 · Service level objectives for data and how to publish them `TH`
**Prerequisites.** Lesson 271

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Cam kết mức dịch vụ cho dữ liệu khác cho dịch vụ trực tuyến ở chỗ nó nói về độ tươi và độ đúng chứ về thời gian phản hồi. Bốn chỉ số thường cam kết: dữ liệu sẵn sàng trước mấy giờ, độ đầy đủ tối thiểu, độ trễ tối đa của dữ liệu tới muộn, và tỉ lệ ngày đạt cam kết trong tháng. Chỉ số thứ tư là chỉ số nói thật nhất và hay bị bỏ: cam kết trước 6 giờ sáng mà đạt 70% số ngày thì cam kết đó vô nghĩa. Đo trước rồi mới cam kết: lấy phân bố 90 ngày lịch sử, cam kết ở phân vị mà mình thật sự đạt được, không cam kết ở mức mong muốn. Ngân sách vi phạm và cách dùng nó để quyết định khi nào dừng thêm tính năng mà đi sửa độ tin cậy. Công bố ở đâu để người dùng thấy: cạnh dữ liệu chứ trong tài liệu nội bộ. Báo cáo định kỳ mức đạt thật. Phân biệt cam kết với mục tiêu nội bộ: cam kết nới hơn mục tiêu để còn chỗ xoay xở.

**Outcome.** Đặt cam kết mức dịch vụ từ phân bố 90 ngày lịch sử, công bố nó, và báo cáo mức đạt thật sau 30 ngày.

**Đánh giá.** Tầng *đánh giá*. Objective đòi cam kết dựa trên số đo chứ trên mong muốn. Đạt khi bốn chỉ số đều đặt từ phân bố lịch sử có nêu phân vị chọn, và khi báo cáo 30 ngày cho thấy mức đạt thật nằm trong khoảng cam kết. Cam kết chặt hơn số liệu lịch sử là không đạt vì nó chắc chắn vi phạm.

**Lab.** Lấy phân bố 90 ngày của bốn chỉ số từ nền tảng lesson 217. Chọn phân vị và đặt cam kết cho từng chỉ số. Công bố cạnh dữ liệu. Chạy 30 ngày mô phỏng và báo cáo mức đạt thật. Tính ngân sách vi phạm còn lại. So cam kết với mục tiêu nội bộ.

**Pitfalls.** Cam kết ở mức mong muốn thay vì mức đo được · bỏ chỉ số tỉ lệ ngày đạt · công bố cam kết trong tài liệu nội bộ mà người dùng không thấy.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn chỉ số đặt từ phân bố lịch sử có nêu phân vị, và báo cáo 30 ngày cho mức đạt thật trong khoảng cam kết.

### Lesson 273 · Handling a contract breach - the seven-step incident process `TH`
**Prerequisites.** Lesson 272

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Quy trình bảy bước khi hợp đồng bị vi phạm và dữ liệu sai đã lan ra. Bước một chặn lan rộng: dừng pipeline hoặc chặn phát hành, quyết định trong vài phút chứ không chờ hiểu hết nguyên nhân. Bước hai thông báo sớm cho người đang dùng, kể cả khi chưa biết nguyên nhân; thông báo sớm với thông tin chưa đầy đủ tốt hơn thông báo muộn với thông tin đầy đủ. Bước ba chẩn đoán. Bước bốn sửa. Bước năm chạy bù, nối lại lesson 210 và 233. Bước sáu thông báo kết quả cho đúng những người đã nhận thông báo ở bước hai, gồm cả việc nói rõ số nào đã đổi. Bước bảy phân tích nguyên nhân gốc và thêm phép kiểm để lần sau bắt sớm hơn. Bước hai và bước sáu là hai bước hay bị bỏ nhất và cũng là hai bước quyết định niềm tin, vì người dùng nhớ mình có được báo hay không hơn là nhớ sự cố kéo dài bao lâu. Ghi nhật ký sự cố và đo thời gian từng bước.

**Outcome.** Xử lý một sự cố vi phạm hợp đồng theo đủ bảy bước, và đo thời gian từng bước.

**Đánh giá.** Tầng *áp dụng*. Objective có quy trình với tiêu chí kiểm được ở từng bước. Đạt khi cả bảy bước đều có bằng chứng thời gian, khi thông báo bước hai gửi trong vòng 30 phút kể từ lúc phát hiện, và khi thông báo bước sáu gửi đúng tập người đã nhận bước hai. Sửa xong nhanh mà bỏ hai bước thông báo thì không đạt.

**Lab.** Giám khảo bơm một vi phạm hợp đồng vào nguồn. Xử lý theo bảy bước, ghi dấu thời gian từng bước. Soạn và gửi hai thông báo thật cho danh sách người dùng lấy từ nhật ký truy vấn. Chạy bù và đối chiếu. Viết phân tích nguyên nhân gốc kèm phép kiểm bổ sung.

**Pitfalls.** Chờ hiểu hết nguyên nhân rồi mới thông báo · bỏ bước thông báo kết quả vì đã sửa xong · chạy bù mà không nói cho người dùng biết số lịch sử đã đổi.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảy bước có bằng chứng thời gian, thông báo bước hai trong 30 phút, và bước sáu gửi đúng tập người đã nhận.

### Lesson 274 · Conformed datasets - orders, payments, refunds `DA`
**Prerequisites.** Lesson 273

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Không có cơ chế mới. Dự án gộp module: dựng ba tập dữ liệu đã chuẩn hoá cho ba miền nghiệp vụ liên quan nhau, mỗi tập có hợp đồng đầy đủ. Ba miền chọn có chủ đích vì chúng dùng chung chiều và phải so sánh chéo được, nối lại ma trận xe buýt ở lesson 197: một đơn hàng có thể có nhiều thanh toán và nhiều lần hoàn tiền, nên hạt của ba tập khác nhau và phép so phải qua hạt chung. Yêu cầu cho mỗi tập: hạt kiểm chứng được, khoá nghiệp vụ khai báo, hợp đồng mười một khai báo có phiên bản, phép kiểm ở hai biên, cam kết mức dịch vụ đặt từ số liệu, gói bàn giao năm thứ, và sổ tay xử lý. Tiêu chí đối soát xuyên tập: tổng tiền thanh toán trừ tổng tiền hoàn phải khớp một đại lượng tính độc lập từ đơn hàng, ở cả ba kỳ.

**Outcome.** Dựng ba tập dữ liệu đã chuẩn hoá có hợp đồng đầy đủ, và chứng minh đối soát xuyên ba tập khớp ở cả ba kỳ.

**Đánh giá.** Tầng *sáng tạo*. Objective là thiết kế một bộ sản phẩm dữ liệu dưới nhiều ràng buộc đồng thời. Chấm theo sáu mục: hạt và khoá của ba tập 20đ, đối soát xuyên tập 25đ, hợp đồng và phép kiểm hai biên 20đ, cam kết mức dịch vụ 10đ, gói bàn giao 15đ, sổ tay 10đ. Đạt khi ≥ 70/100 và mục đối soát ≥ 70% của nó.

**Lab.** Nguồn có đơn hàng, thanh toán, hoàn tiền với quan hệ một nhiều. Dựng ba tập đã chuẩn hoá. Phát biểu và kiểm chứng hạt từng tập. Viết ba hợp đồng có phiên bản. Cài phép kiểm hai biên. Đặt cam kết từ số liệu 90 ngày. Đối soát xuyên tập ở ba kỳ.

**Pitfalls.** Đặt ba tập ở cùng một hạt cho tiện rồi mất chi tiết · đối soát từng tập riêng mà bỏ đối soát xuyên tập · viết một hợp đồng chung cho cả ba tập.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Đạt ≥ 70/100, mục đối soát ≥ 70%, và đối soát xuyên ba tập khớp ở cả ba kỳ.

### Lesson 275 · Handover rehearsal - someone else builds on your dataset `TH`
**Prerequisites.** Lesson 274

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Không có cơ chế mới. Bài diễn tập và nó đo thứ khó giả: một tập dữ liệu người khác dùng được mà không cần mình. Quy trình diễn tập: giao gói bàn giao cho một người chưa tham gia dự án, giao họ một yêu cầu nghiệp vụ cụ thể, để họ làm trong thời gian giới hạn, và ghi lại mọi câu hỏi cùng mọi chỗ họ hiểu sai. Ba loại câu hỏi và cái mỗi loại chỉ ra: câu hỏi về ngữ nghĩa chỉ ra tài liệu cột thiếu, câu hỏi về cách dùng chỉ ra thiếu truy vấn mẫu, câu hỏi về độ tin cậy chỉ ra thiếu cam kết mức dịch vụ hoặc thiếu thông tin lineage. Hiểu sai nguy hiểm hơn câu hỏi: người hỏi thì mình biết mà sửa, người hiểu sai thì dựng ra số sai mà không ai biết, nên phần đối chiếu kết quả của họ với bản đối chứng là phần quan trọng nhất của diễn tập. Lặp diễn tập với người thứ hai sau khi sửa. Đưa diễn tập vào quy trình chuẩn trước mỗi lần công bố tập dữ liệu mới.

**Outcome.** Chạy một buổi diễn tập bàn giao, phân loại mọi câu hỏi và hiểu sai, và sửa gói bàn giao rồi chứng minh cải thiện ở lần diễn tập thứ hai.

**Đánh giá.** Tầng *đánh giá*. Objective đo bằng hai vòng quan sát nên thấy được cải thiện chứ chỉ thấy trạng thái. Đạt khi vòng hai có số câu hỏi giảm ít nhất một nửa so với vòng một, và khi kết quả người nhận dựng ra ở vòng hai khớp bản đối chứng. Vòng một nhiều câu hỏi không phải điểm trừ; không cải thiện ở vòng hai mới là.

**Lab.** Giao gói bàn giao của lesson 274 cho một người chưa tham gia, cùng một yêu cầu nghiệp vụ. Quan sát 60 phút, ghi mọi câu hỏi và mọi chỗ hiểu sai. Đối chiếu kết quả họ dựng với bản đối chứng. Phân loại câu hỏi theo ba loại. Sửa gói. Lặp với người thứ hai và so hai vòng.

**Pitfalls.** Trả lời câu hỏi trong lúc diễn tập thay vì ghi lại rồi sửa tài liệu · bỏ phần đối chiếu kết quả vì họ không kêu gì · chỉ diễn tập một vòng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Vòng hai giảm ít nhất một nửa số câu hỏi, và kết quả người nhận dựng ra khớp bản đối chứng.

### Lesson 276 · Gate 6 - controlled schema change, 30-day backfill, clean handover `KT`
**Prerequisites.** Lesson 275

**In-class (120 phút).** 75 phút làm bài độc lập · 45 phút chữa bài và phân tích lỗi theo nhóm

**Learn.** Không có nội dung mới. Cổng 6 đóng chặng 5.

**Outcome.** Thực hiện một thay đổi lược đồ phá vỡ có kiểm soát trên tập dữ liệu đang có người dùng, chạy bù 30 ngày, và bàn giao cho người khác dựng mô hình mà không cần hỏi lại.

**Đánh giá.** Tầng *đánh giá*. Cổng đo ba năng lực cùng lúc: đổi có kiểm soát, phục hồi dữ liệu lịch sử, và bàn giao. Thang điểm: A 25đ thay đổi theo bốn bước với cửa sổ ngừng dùng công bố trước · B 20đ hạ nguồn không vỡ trong suốt quá trình, đo bằng số lỗi truy vấn · C 25đ chạy bù 30 ngày khớp bản đối chứng · D 20đ người nhận dựng được mô hình với không quá một câu hỏi · E 10đ thông báo gửi đúng tập người dùng ở cả hai thời điểm. Đạt khi ≥ 70/100, phần B và phần C đều ≥ 70% của chúng.

**Lab.** 180 phút. Tập dữ liệu có ba người dùng mô phỏng chạy truy vấn liên tục. Đổi kiểu một cột theo bốn bước. Chạy bù 30 ngày. Bàn giao cho một học viên khác chưa biết gì về tập này, họ dựng một mô hình theo yêu cầu cho trước. Đếm lỗi truy vấn của ba người dùng suốt quá trình.

**Pitfalls.** Gộp bước bỏ cột cũ vào cùng lần triển khai với bước chuyển người đọc · chạy bù mà không đối chiếu · bàn giao mà không kèm dữ liệu mẫu cố định.

**Self-study (2,4 giờ).** Không có bài tự học. Nếu không đạt, theo phụ lục khắc phục khi không đạt cổng

**Done when.** Đạt ≥ 70/100, phần B và phần C đều ≥ 70%.

# MODULE 27 · MESSAGING FOUNDATIONS

**Lessons 277–282 · 12 giờ**

| | |
|---|---|
| **Objective cấp module** | Phát biểu một bài toán truyền thông điệp bằng từ vựng ngữ nghĩa giao nhận, thứ tự, offset và phát lại, trước khi mở bất kỳ broker nào |
| **Tiền đề** | M26 |
| **Exit criterion** | Nhận sáu sự cố của một hệ nối bằng lời gọi trực tiếp, định vị đúng cơ chế cho cả sáu và nêu broker giải được cái nào, không giải được cái nào |
| **Kỹ năng SFIA** | `SYSP` mức 3 · `DTAN` mức 3 |
| **Chế độ hỏng** | Học thẳng vào một broker, rồi coi mọi vấn đề giao nhận là vấn đề cấu hình, nên đổi broker mà trùng bản ghi vẫn còn |

Module không mở broker nào. Nó dựng từ vựng để M28 và M29 có cái mà so sánh, và để M30 chấm được bằng tiêu chí thay vì bằng danh sách tính năng. Cùng ràng buộc với M21 trước khối điều phối và M9 · M10 trước khối cơ sở dữ liệu.

**Kịch bản tham chiếu chung.** M28 và M29 dựng lại cùng một bài toán: sự kiện đơn hàng sinh từ PostgreSQL của pipeline lesson 217, phát ra cho hai bên tiêu thụ độc lập là bộ nạp mart và bộ kiểm gian lận. Cùng ba lỗi cài sẵn: một thông điệp gửi trùng, một thông điệp tới sai thứ tự, một thông điệp hỏng không giải mã được. Cùng kịch bản giết tiến trình giữa chừng. Không cùng bài toán thì M30 không đo được gì.

### Lesson 277 · Why a message broker exists - coupling, backpressure and load spikes `LT`
**Prerequisites.** Module 27: M26

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bốn vấn đề của việc nối hai hệ bằng lời gọi trực tiếp, mỗi vấn đề kèm một hậu quả quan sát được trên pipeline lesson 217. Một là ràng buộc thời gian: bên gửi chỉ xong khi bên nhận xong, nên bên nhận chậm thì bên gửi chậm theo, và bên nhận chết thì bên gửi mất dữ liệu. Hai là ràng buộc số lượng: thêm bên tiêu thụ thứ hai thì phải sửa mã bên gửi, nối lại vấn đề phụ thuộc chéo ở lesson 220. Ba là đỉnh tải: bên gửi sinh 5.000 sự kiện trong một phút còn bên nhận xử lý được 500, phần chênh không có chỗ chứa nên hoặc mất hoặc làm sập bên nhận, nối lại hàng đợi có giới hạn và áp lực ngược ở M6. Bốn là phát lại: sửa lỗi logic xong thì không có cách nào cho dữ liệu cũ chạy lại, nối lại lesson 210. Broker giải bốn vấn đề đó bằng một cách duy nhất là chen một vùng lưu trữ có thứ tự vào giữa. Cái giá phải trả: thêm một hệ phải vận hành, thêm độ trễ, và mất tính nhất quán tức thời giữa hai bên.

**Outcome.** Định vị trong bốn vấn đề cái nào gây ra một sự cố cho trước, dẫn bằng nhật ký và số liệu chứ bằng phỏng đoán.

**Đánh giá.** Tầng *phân tích*. Bài mở module, người học đã vận hành pipeline theo lô từ M20 và biết áp lực ngược từ M6, nên có kinh nghiệm để soi lại nhưng chưa có broker nào. Objective dừng ở phân rã một sự cố về đúng cơ chế. Kiểm bằng sáu hồ sơ sự cố có nhật ký và biểu đồ tải; đạt khi định vị đúng ít nhất năm và mỗi lần dẫn được bằng chứng.

**Lab.** Nhận sáu hồ sơ sự cố của một hệ nối trực tiếp. Với mỗi hồ sơ, nêu vấn đề nào trong bốn vấn đề, bằng chứng nào trong nhật ký chỉ ra điều đó, và broker giải nó bằng cơ chế gì. Với hai hồ sơ cuối, broker không giải được; nêu vì sao.

**Pitfalls.** Cho rằng broker làm hệ thống nhanh hơn · quên rằng broker thêm một hệ phải trực · coi độ trễ tăng thêm là không đáng kể mà không đo.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Định vị đúng ≥ 5/6 hồ sơ, mỗi lần dẫn được bằng chứng từ nhật ký, và chỉ đúng hai hồ sơ broker không giải được.

### Lesson 278 · Delivery semantics - at most once, at least once, exactly once end to end `LT`
**Prerequisites.** Lesson 277

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Ba mức ngữ nghĩa giao nhận, định nghĩa bằng điều gì xảy ra khi có sự cố chứ bằng tên gọi. Nhiều nhất một lần: xác nhận trước khi xử lý, nên sự cố làm mất thông điệp. Ít nhất một lần: xử lý trước khi xác nhận, nên sự cố làm thông điệp được xử lý lại, và đây là mặc định của mọi broker dùng trong sản xuất. Đúng một lần là **tính chất của toàn tuyến, không phải một nút gạt của broker**: nó chỉ đạt được khi bên tiêu thụ ghi có tính bất biến, tức là ghi lại cho cùng kết quả, đúng cơ chế đã học ở lesson 106 và 207. Phân biệt ba chỗ có thể mất hoặc nhân đôi: giữa bên gửi và broker, trong broker, giữa broker và bên nhận. Bài toán hai vị tướng ở mức kết luận: không có giao thức nào cho phép hai bên biết chắc bên kia đã nhận, nên mọi hệ thực tế chọn ít nhất một lần cộng khử trùng ở đầu ghi. Khoá khử trùng lấy từ đâu: khoá nghiệp vụ ở lesson 208, không lấy từ mã thông điệp do broker sinh.

**Outcome.** Với một tuyến gửi và nhận cho trước, chỉ ra tuyến đó đạt mức ngữ nghĩa nào và nêu thay đổi nhỏ nhất để nâng lên đúng một lần đầu cuối.

**Đánh giá.** Tầng *đánh giá*. Người học đã có tính bất biến từ lesson 106 và 207, nên bài này ghép hai mảnh thành một phán đoán về toàn tuyến. Kiểm bằng năm sơ đồ tuyến có chú thích thứ tự xác nhận và ghi; đạt khi phân loại đúng ít nhất bốn và nêu được thay đổi nhỏ nhất, không chấp nhận câu trả lời bật một tuỳ chọn của broker.

**Lab.** Nhận năm sơ đồ tuyến. Với mỗi sơ đồ, phân loại mức ngữ nghĩa, chỉ ra chính xác chỗ mất hoặc nhân đôi xảy ra, và viết thay đổi nhỏ nhất đưa tuyến về đúng một lần đầu cuối. Một sơ đồ trong năm không nâng lên được nếu không đổi thiết kế bên nhận; nêu vì sao.

**Pitfalls.** Tin rằng bật một tuỳ chọn tên "exactly once" là xong · khử trùng bằng mã thông điệp của broker thay vì khoá nghiệp vụ · xác nhận trước khi ghi xong.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân loại đúng ≥ 4/5 sơ đồ và nêu đúng thay đổi nhỏ nhất, kể cả sơ đồ không nâng được.

### Lesson 279 · Ordering guarantees and the partition as the unit of order `LT`
**Prerequisites.** Lesson 278

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Thứ tự toàn cục tốn kém tới mức không hệ nào ở quy mô lớn cung cấp, vì nó buộc mọi thông điệp qua một điểm nối tiếp. Cái mọi broker cung cấp là thứ tự trong một đơn vị hẹp hơn: một hàng đợi, một phân vùng, một khoá. Hệ quả thiết kế: **chọn khoá phân vùng chính là chọn cái gì được bảo đảm thứ tự**. Đơn hàng cùng một mã khách phải cùng khoá thì mới thấy đúng trình tự tạo rồi huỷ; chọn khoá ngẫu nhiên thì hai sự kiện của cùng một đơn có thể tới ngược. Ba hậu quả của khoá lệch: một khoá nóng chiếm phần lớn lưu lượng làm mất tác dụng của việc chia phân vùng, đúng hiện tượng lệch dữ liệu sẽ gặp lại ở M34; số phân vùng đổi thì ánh xạ khoá đổi theo nên thứ tự cũ đứt; và thứ tự chỉ được bảo đảm khi mỗi phân vùng có đúng một bên tiêu thụ đang hoạt động. Phân biệt thứ tự tới với thứ tự sự kiện: dấu thời gian trong thông điệp và thứ tự trong hàng đợi là hai thứ khác nhau, sẽ dùng lại ở lesson 317.

**Outcome.** Chọn khoá phân vùng cho một luồng sự kiện cho trước và nêu bằng phản ví dụ điều gì hỏng nếu chọn khoá khác.

**Đánh giá.** Tầng *áp dụng*. Objective là một quyết định thiết kế có ràng buộc rõ, nên kiểm được bằng bài làm chứ bằng câu hỏi trắc nghiệm. Kiểm bằng ba luồng sự kiện có yêu cầu thứ tự khác nhau; đạt khi cả ba chọn đúng khoá và mỗi lần nêu được một phản ví dụ cụ thể.

**Lab.** Cho ba luồng sự kiện: thay đổi trạng thái đơn hàng, đo lường thiết bị, và nhật ký thao tác người dùng. Với mỗi luồng, chọn khoá phân vùng, nêu cái gì được bảo đảm thứ tự và cái gì không, rồi viết một phản ví dụ cho thấy hậu quả khi chọn khoá khác. Đo phân bố khoá trên dữ liệu mẫu và chỉ ra luồng nào có nguy cơ khoá nóng.

**Pitfalls.** Cho rằng broker giữ thứ tự toàn cục · chọn khoá ngẫu nhiên để chia đều rồi mất thứ tự · quên rằng tăng số phân vùng làm đứt thứ tự của khoá cũ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba luồng đều chọn đúng khoá, mỗi luồng có một phản ví dụ cụ thể, và chỉ đúng luồng có nguy cơ khoá nóng kèm số đo phân bố.

### Lesson 280 · Consumer groups, offsets and where progress is recorded `LT`
**Prerequisites.** Lesson 279

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Hai mô hình tiêu thụ và hệ quả vận hành của từng mô hình. Mô hình hàng đợi: thông điệp được lấy ra thì biến mất, nhiều bên tiêu thụ chia nhau công việc, muốn hai bên cùng đọc toàn bộ thì phải nhân bản dữ liệu ở phía broker. Mô hình nhật ký: thông điệp nằm lại theo chính sách lưu giữ, mỗi nhóm tiêu thụ giữ con trỏ riêng, nên thêm bên tiêu thụ thứ hai không đụng gì tới bên thứ nhất và đọc lại quá khứ là chuyện bình thường. Con trỏ tiến độ ghi ở đâu quyết định điều gì xảy ra khi bên tiêu thụ chết: ghi ở broker thì bên tiêu thụ khởi động lại đọc tiếp được nhưng có nguy cơ xử lý lại đoạn chưa xác nhận; ghi cùng chỗ với kết quả, trong cùng một giao dịch, thì tiến độ và dữ liệu không bao giờ lệch nhau, và đây là cách duy nhất đạt đúng một lần đầu cuối ở lesson 278. Cân bằng lại nhóm: khi một bên tiêu thụ vào hoặc ra, phần việc được chia lại, và trong lúc chia lại thì xử lý dừng; hệ quả là nhóm càng đông thì mỗi lần triển khai càng tốn thời gian dừng.

**Outcome.** Với một yêu cầu tiêu thụ cho trước, chọn mô hình hàng đợi hay nhật ký và nêu chỗ ghi tiến độ, kèm điều gì xảy ra khi bên tiêu thụ chết giữa chừng.

**Đánh giá.** Tầng *đánh giá*. Bài đòi cân nhắc đánh đổi giữa hai mô hình chứ nhớ định nghĩa, và đây là trục chính mà M30 sẽ chấm. Kiểm bằng bốn yêu cầu tiêu thụ có ràng buộc khác nhau; đạt khi cả bốn chọn đúng mô hình và mô tả đúng hành vi khi chết giữa chừng.

**Lab.** Cho bốn yêu cầu: nạp mart theo lô, kiểm gian lận theo thời gian thực, gửi thông báo cho khách, và dựng lại toàn bộ lịch sử sau khi sửa lỗi logic. Với mỗi yêu cầu, chọn mô hình, nêu chỗ ghi tiến độ, và mô tả điều gì xảy ra nếu bên tiêu thụ chết sau khi ghi kết quả nhưng trước khi xác nhận.

**Pitfalls.** Ghi tiến độ tách rời kết quả rồi tưởng đã đạt đúng một lần · quên thời gian dừng khi cân bằng lại nhóm · dùng mô hình hàng đợi cho nhu cầu phát lại rồi phát hiện dữ liệu đã biến mất.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn yêu cầu đều chọn đúng mô hình, nêu đúng chỗ ghi tiến độ, và mô tả đúng hậu quả của cái chết giữa chừng ở cả bốn.

### Lesson 281 · Dead letter queue, poison messages and replay `TH`
**Prerequisites.** Lesson 280

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Thông điệp hỏng là thông điệp mà bên tiêu thụ không xử lý được và sẽ không bao giờ xử lý được: sai định dạng, thiếu trường bắt buộc, tham chiếu tới bản ghi không tồn tại. Nếu chính sách là thử lại thì nó chặn cả phân vùng và thành một vòng lặp vô tận, đúng kiểu bão thử lại đã gặp ở lesson 61. Hàng đợi thư chết là chỗ chuyển những thông điệp đó ra khỏi đường chính, kèm ba thứ bắt buộc phải ghi cùng: nguyên nhân, số lần đã thử, và đủ ngữ cảnh để phát lại. Phân biệt ba loại lỗi và ba cách xử lý khác nhau: lỗi tạm thời thì thử lại có lùi theo hàm mũ, lỗi thông điệp thì đẩy sang thư chết, lỗi hệ thống hạ nguồn thì dừng tiêu thụ chứ đẩy sang thư chết vì sẽ đẩy nhầm cả luồng tốt. Phát lại từ thư chết sau khi sửa: điều kiện bắt buộc là bên tiêu thụ có tính bất biến, nếu không thì phát lại sinh trùng. Ngưỡng cảnh báo trên hàng đợi thư chết: tốc độ vào chứ tổng số, vì tổng số chỉ nói quá khứ.

**Outcome.** Phân loại một lỗi tiêu thụ thành ba loại và cấu hình đúng cách xử lý cho từng loại, rồi phát lại được từ thư chết mà không sinh trùng.

**Đánh giá.** Tầng *áp dụng*. Bài thực hành nối tiếp lesson 214 về vùng cách ly ở tầng theo lô, nay đặt lại trong ngữ cảnh luồng. Kiểm bằng lab có ba loại lỗi tiêm sẵn; đạt khi cả ba được định tuyến đúng và bản phát lại đối soát khớp tuyệt đối với bản đúng.

**Lab.** Trên một bên tiêu thụ có sẵn, tiêm ba loại lỗi: một thông điệp sai định dạng, một khoảng thời gian cơ sở dữ liệu đích không truy cập được, và một thông điệp tham chiếu khách hàng không tồn tại. Cấu hình để mỗi loại đi đúng đường. Sửa lỗi logic rồi phát lại toàn bộ thư chết; đối soát số bản ghi và tổng tiền với bản chạy đúng.

**Pitfalls.** Đẩy lỗi hạ nguồn sang thư chết nên mất cả luồng tốt · thử lại vô hạn cho thông điệp hỏng · phát lại khi bên tiêu thụ chưa bất biến · cảnh báo theo tổng số thay vì tốc độ vào.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba loại lỗi đi đúng ba đường, phát lại xong đối soát khớp tuyệt đối, và hàng đợi thư chết có cảnh báo theo tốc độ vào.

### Lesson 282 · What a broker is not - database, orchestrator and processing engine `LT`
**Prerequisites.** Lesson 281

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Ba cách dùng sai phổ biến, mỗi cách kèm dấu hiệu nhận biết sớm. Dùng broker làm cơ sở dữ liệu: giữ lưu giữ vĩnh viễn rồi truy vấn lịch sử bằng cách đọc lại từ đầu, hỏng vì không có chỉ mục nên mọi câu hỏi đều là quét toàn bộ, nối lại lesson 111 và 113. Dùng broker làm bộ điều phối: mã hoá thứ tự các bước bằng chuỗi hàng đợi nối nhau, hỏng vì không có chỗ nào nhìn thấy toàn bộ đồ thị, không chạy bù được, và trạng thái lần chạy nằm rải rác, đúng những thứ M21 đã dựng từ vựng để gọi tên. Dùng broker làm bộ xử lý: nhồi logic biến đổi vào bên tiêu thụ tới mức nó thành một công việc xử lý không có kiểm thử và không có khả năng chạy lại. Ranh giới nên giữ: broker chịu trách nhiệm vận chuyển và lưu giữ tạm có thứ tự; điều phối thuộc về M21 tới M25; biến đổi thuộc về M32 và M34; lưu trữ lâu dài thuộc về M33. Ba câu hỏi kiểm tra trước khi thêm một hàng đợi vào thiết kế.

**Outcome.** Nhận ra trong một thiết kế cho trước chỗ nào đang dùng broker sai vai và nêu thành phần đúng phải nhận việc đó.

**Đánh giá.** Tầng *phân tích*. Bài chốt module, người học đã có từ vựng điều phối từ M21 và từ vựng giao nhận từ năm bài trước, nên đủ để phán đoán ranh giới. Kiểm bằng bốn sơ đồ kiến trúc; đạt khi chỉ đúng ít nhất ba chỗ sai vai và nêu đúng thành phần thay thế.

**Lab.** Nhận bốn sơ đồ kiến trúc có thật về mặt cấu trúc. Với mỗi sơ đồ, chỉ ra chỗ broker đang làm việc của thành phần khác, nêu dấu hiệu quan sát được của cách dùng sai đó, và vẽ lại phần đó với thành phần đúng. Một trong bốn sơ đồ không sai; nhận ra và giải thích vì sao.

**Pitfalls.** Nối hàng đợi thành chuỗi để thay cho đồ thị phụ thuộc · giữ lưu giữ vĩnh viễn rồi coi broker là kho lịch sử · kết luận sơ đồ nào cũng sai vì đang học bài về cách dùng sai.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chỉ đúng ≥ 3/4 chỗ sai vai kèm dấu hiệu quan sát được, và nhận ra đúng sơ đồ không sai.

# MODULE 28 · RABBITMQ

**Lessons 283–290 · 16 giờ**

| | |
|---|---|
| **Objective cấp module** | Dựng và vận hành được kịch bản tham chiếu trên RabbitMQ ở mức `B`, đo bốn chỉ số của M30 và ghi lại bằng chứng |
| **Tiền đề** | M27 |
| **Exit criterion** | Kịch bản tham chiếu chạy đúng dưới cả ba lỗi cài sẵn, bốn chỉ số có số đo lặp lại được, và giải thích được định tuyến của mình bằng exchange, binding và khoá |
| **Kỹ năng SFIA** | `SYSP` mức 3 · `NTAS` mức 3 |
| **Chế độ hỏng** | Học cú pháp khai báo hàng đợi mà bỏ qua xác nhận và prefetch, rồi mất thông điệp hoặc làm bên tiêu thụ ngộp mà không biết vì sao |

Mức `B` theo quy ước ở mục 2: làm được lab và so sánh có căn cứ, không yêu cầu vận hành cụm sản xuất. RabbitMQ đứng trước Kafka vì mô hình hàng đợi ở lesson 280 dễ quan sát hơn mô hình nhật ký, và vì phần lớn hệ nội bộ ở Việt Nam bắt đầu từ một hàng đợi tác vụ chứ từ một nhật ký sự kiện.

Bốn chỉ số đo ở lesson 290 là bốn chỉ số M30 dùng để chấm: thông lượng ổn định, độ trễ đầu cuối ở phân vị 95, thời gian phục hồi sau khi giết tiến trình, và số thao tác để phát lại một ngày dữ liệu.

### Lesson 283 · Architecture - exchange, queue, binding and the routing decision `LT`
**Prerequisites.** Module 28: M27

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bên gửi trong RabbitMQ không gửi vào hàng đợi mà gửi vào exchange, và chính chi tiết này quyết định mọi thứ còn lại. Bốn thành phần và trách nhiệm tách bạch: exchange nhận thông điệp và quyết định chuyển đi đâu, binding là luật nối exchange với hàng đợi, hàng đợi là chỗ thông điệp nằm chờ, bên tiêu thụ lấy ra. Hệ quả của việc tách: thêm một bên tiêu thụ mới là thêm một hàng đợi và một binding, **mã bên gửi không đổi**, đúng vấn đề ràng buộc số lượng ở lesson 277. Vhost và cách nó chia tách môi trường. Kênh và vì sao mở một kết nối rồi nhiều kênh trên đó, thay vì nhiều kết nối, nối lại chi phí bắt tay ở M4. Giao thức AMQP 0-9-1 ở mức đủ để đọc nhật ký lỗi. So chiếu với từ vựng M27: RabbitMQ là hiện thân của mô hình hàng đợi, nên lấy ra là biến mất, và phát lại phải tự dựng chứ có sẵn.

**Outcome.** Vẽ được đường đi của một thông điệp từ bên gửi tới bên tiêu thụ, gọi đúng tên bốn thành phần và chỉ ra chỗ quyết định định tuyến xảy ra.

**Đánh giá.** Tầng *hiểu*. Bài mở module, chưa có lab đủ để đòi vận hành, nên objective dừng ở tái hiện cơ chế. Kiểm bằng bài vẽ lại có chú thích; đạt khi cả bốn thành phần đúng vai và chỉ đúng chỗ định tuyến, không chấp nhận bản vẽ nối thẳng bên gửi vào hàng đợi.

**Lab.** Cài RabbitMQ bằng container, bật giao diện quản trị. Khai báo một exchange, hai hàng đợi, hai binding. Gửi năm thông điệp, quan sát trên giao diện chúng vào hàng đợi nào. Vẽ lại đường đi có chú thích bốn thành phần, rồi xoá một binding và dự đoán trước khi chạy xem thông điệp đi đâu.

**Pitfalls.** Vẽ bên gửi nối thẳng vào hàng đợi · nhầm exchange với hàng đợi · mở một kết nối cho mỗi thao tác.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bản vẽ gọi đúng bốn thành phần, chỉ đúng chỗ định tuyến, và dự đoán đúng đích của thông điệp sau khi xoá binding.

### Lesson 284 · Four exchange types and the routing key `TH`
**Prerequisites.** Lesson 283

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bốn kiểu exchange là bốn luật định tuyến khác nhau, và chọn kiểu chính là chọn hình dạng của hệ. Direct: khớp khoá định tuyến đúng từng ký tự, dùng cho hàng đợi tác vụ chia theo loại việc. Fanout: bỏ qua khoá, chuyển cho mọi hàng đợi đã nối, đây là cách RabbitMQ làm phát một nhận nhiều. Topic: khớp khoá theo mẫu có ký tự đại diện, cho phép bên tiêu thụ tự chọn lát dữ liệu mình quan tâm mà bên gửi không cần biết. Headers: khớp theo thuộc tính, ít dùng, tốn hơn. Thiết kế khoá định tuyến là một quyết định lâu dài: khoá dạng phân cấp từ rộng tới hẹp thì về sau thêm bên tiêu thụ mới không phải đổi bên gửi, còn khoá phẳng thì mọi thay đổi đều chạm vào bên gửi. Exchange mặc định và vì sao gửi thẳng theo tên hàng đợi là một lối tắt nên tránh trong mã sản xuất.

**Outcome.** Chọn kiểu exchange và thiết kế khoá định tuyến cho một yêu cầu cho trước, rồi chứng minh thêm một bên tiêu thụ mới không phải sửa mã bên gửi.

**Đánh giá.** Tầng *áp dụng*. Objective là quyết định thiết kế có ràng buộc kiểm được bằng thực nghiệm, nên kiểm bằng lab chứ bằng lý thuyết. Kiểm bằng việc thêm bên tiêu thụ thứ ba sau khi đã chốt thiết kế; đạt khi mã bên gửi không đổi một dòng.

**Lab.** Dựng ba kịch bản: chia việc theo loại, phát một nhận nhiều, và lọc theo lát. Với mỗi kịch bản chọn kiểu exchange và viết khoá định tuyến. Sau khi chạy xong, giảng viên thêm một yêu cầu tiêu thụ mới; thực hiện bằng cách chỉ thêm hàng đợi và binding. Ghi lại phần khác biệt của mã bên gửi trước và sau.

**Pitfalls.** Dùng direct cho mọi thứ rồi phải sửa bên gửi mỗi lần thêm bên nhận · đặt khoá phẳng không phân cấp · gửi qua exchange mặc định trong mã sản xuất.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba kịch bản chọn đúng kiểu exchange, và phần khác biệt của mã bên gửi sau khi thêm bên tiêu thụ thứ ba bằng không.

### Lesson 285 · Acknowledgement, prefetch and flow control `TH`
**Prerequisites.** Lesson 284

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Xác nhận là chỗ ngữ nghĩa giao nhận ở lesson 278 trở thành cấu hình cụ thể. Chế độ tự động xác nhận cho nhiều nhất một lần và mất thông điệp khi bên tiêu thụ chết; chế độ thủ công cho ít nhất một lần. Ba lệnh và ba hệ quả: xác nhận thì thông điệp biến mất; từ chối có trả lại thì thông điệp quay vào hàng đợi và có thể lặp vô tận; từ chối không trả lại thì thông điệp đi tiếp theo cấu hình thư chết ở lesson 281. Prefetch là số thông điệp broker giao trước cho một bên tiêu thụ mà chưa cần xác nhận, và đây là núm điều khiển áp lực ngược của RabbitMQ. Prefetch bằng không nghĩa là không giới hạn, nên một bên tiêu thụ chậm sẽ ôm toàn bộ hàng đợi vào bộ nhớ rồi chết, đúng hiện tượng hàng đợi không giới hạn ở M6. Prefetch bằng một cho phân phối đều nhất nhưng thông lượng thấp nhất; chọn giá trị là chọn điểm trên đường đánh đổi, và phải đo chứ đoán.

**Outcome.** Đo được quan hệ giữa prefetch và hai đại lượng thông lượng và độ trễ phân vị 95, rồi chọn một giá trị có căn cứ từ số đo của chính mình.

**Đánh giá.** Tầng *đánh giá*. Bài đòi chọn một điểm trên đường đánh đổi dựa trên dữ liệu tự đo, chứ áp dụng một quy tắc có sẵn. Kiểm bằng bảng số đo ít nhất bốn mức prefetch; đạt khi có đường cong, có điểm chọn, và lý do chọn dẫn từ số trong bảng.

**Lab.** Chạy bên tiêu thụ ở bốn mức prefetch: 1, 10, 100 và không giới hạn. Với mỗi mức, đo thông lượng ổn định và độ trễ phân vị 95 trên cùng một tải. Giết tiến trình bên tiêu thụ giữa chừng ở từng mức và đếm số thông điệp bị xử lý lại. Chọn một mức và viết ba câu bảo vệ lựa chọn, dẫn số từ bảng.

**Pitfalls.** Để tự động xác nhận trong mã sản xuất · đặt prefetch không giới hạn · từ chối có trả lại cho thông điệp hỏng rồi tạo vòng lặp vô tận · chọn prefetch theo bài viết trên mạng thay vì theo số đo.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng có đủ bốn mức với cả hai đại lượng, số thông điệp xử lý lại được đếm ở từng mức, và lý do chọn dẫn được ít nhất hai con số từ bảng.

### Lesson 286 · Durability - persistent messages, quorum queues and what survives a restart `TH`
**Prerequisites.** Lesson 285

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bốn thứ phải cùng bền thì thông điệp mới sống qua một lần khởi động lại, và thiếu một thứ là mất: hàng đợi khai báo bền, thông điệp đánh dấu bền, bên gửi bật xác nhận từ broker, và đĩa thực sự ghi xong. Ba thứ đầu là cấu hình, thứ tư là vật lý và nối thẳng về `fsync` ở M2. Xác nhận từ broker cho bên gửi: không có nó thì bên gửi tưởng đã gửi thành công trong khi broker chưa ghi, đây là chỗ mất thông điệp phổ biến nhất mà nhật ký không ghi lại gì. Hàng đợi quorum dùng đồng thuận Raft để giữ nhiều bản sao, đổi lấy thông lượng thấp hơn và tốn đĩa hơn; hàng đợi cổ điển nhanh hơn nhưng mất khi nút giữ nó chết. Phân biệt bền với sẵn sàng cao: bền là sống qua khởi động lại, sẵn sàng cao là vẫn phục vụ khi một nút chết, và hai thứ cần hai cấu hình khác nhau. Cái giá đo được: bật đủ bốn thứ làm thông lượng giảm, và bài lab đo mức giảm đó.

**Outcome.** Cấu hình đủ bốn điều kiện bền và chứng minh bằng thực nghiệm rằng không thông điệp nào mất sau khi giết broker, kèm số đo mức giảm thông lượng.

**Đánh giá.** Tầng *áp dụng*. Objective là một cấu hình kiểm được bằng thí nghiệm hỏng, đúng kiểu đã dùng ở lesson 218. Kiểm bằng phép đếm trước và sau khi giết tiến trình; đạt khi số thông điệp khớp tuyệt đối và bảng đánh đổi có số.

**Lab.** Gửi 10.000 thông điệp. Giết tiến trình broker giữa chừng bằng tín hiệu cứng, khởi động lại, đếm số thông điệp còn lại. Chạy lại thí nghiệm ở bốn cấu hình: không bền, chỉ hàng đợi bền, bền đủ bốn điều kiện, và hàng đợi quorum. Lập bảng bốn cấu hình với số mất và thông lượng.

**Pitfalls.** Khai báo hàng đợi bền mà quên đánh dấu thông điệp bền · quên xác nhận từ broker cho bên gửi · nhầm bền với sẵn sàng cao · kết luận về độ bền mà chưa từng giết tiến trình.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Cấu hình bền đủ bốn điều kiện mất 0 thông điệp, và bảng bốn cấu hình có đủ số mất lẫn thông lượng.

### Lesson 287 · Dead letter exchange, TTL and delayed retry `TH`
**Prerequisites.** Lesson 286

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** RabbitMQ không có thử lại có lùi theo hàm mũ sẵn, nên phải dựng bằng cách ghép ba cơ chế, và chính việc phải tự ghép là một dữ kiện để M30 chấm. Exchange thư chết: hàng đợi khai báo chuyển thông điệp bị từ chối, hết hạn hoặc tràn sang một exchange khác. Thời gian sống đặt ở hai chỗ với nghĩa khác nhau: đặt trên hàng đợi là áp cho mọi thông điệp, đặt trên từng thông điệp là linh hoạt nhưng chỉ tính khi thông điệp tới đầu hàng đợi. Mẫu thử lại có độ trễ dựng từ hai thứ trên: thông điệp lỗi đi vào một hàng đợi chờ có thời gian sống, hết hạn thì thư chết đẩy ngược về hàng đợi chính, và số lần thử đếm bằng tiêu đề đính kèm. Dựng nhiều hàng đợi chờ với thời gian sống tăng dần cho ra lùi theo hàm mũ. Ba bẫy: thông điệp hết hạn chỉ được kiểm khi tới đầu hàng đợi nên hàng đợi dài làm độ trễ thực khác độ trễ cấu hình; vòng lặp thư chết khi cấu hình trỏ vòng lại chính nó; và đếm số lần thử bằng tiêu đề bị mất nếu tạo thông điệp mới thay vì chuyển tiếp.

**Outcome.** Dựng được thử lại có lùi theo hàm mũ với số lần tối đa, và chứng minh bằng nhật ký rằng khoảng cách giữa các lần thử tăng đúng như thiết kế.

**Đánh giá.** Tầng *sáng tạo*. Bài đòi ghép ba cơ chế rời thành một mẫu mà công cụ không cung cấp sẵn, nên cao hơn tầng áp dụng. Kiểm bằng nhật ký có dấu thời gian từng lần thử; đạt khi khoảng cách tăng đúng dãy thiết kế và thông điệp dừng đúng ở số lần tối đa.

**Lab.** Dựng chuỗi ba hàng đợi chờ với thời gian sống 5, 25 và 125 giây. Tiêm một thông điệp luôn lỗi và một thông điệp lỗi hai lần đầu rồi thành công. Đọc nhật ký, lập bảng dấu thời gian từng lần thử của cả hai. Chứng minh thông điệp luôn lỗi dừng ở lần thứ ba và nằm lại thư chết.

**Pitfalls.** Cấu hình thư chết trỏ vòng về chính hàng đợi gốc · đặt thời gian sống trên thông điệp rồi ngạc nhiên vì nó không hết hạn đúng giờ · tạo thông điệp mới khi thử lại nên mất số đếm.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng dấu thời gian cho thấy khoảng cách 5, 25, 125 giây, thông điệp luôn lỗi dừng đúng sau ba lần và nằm ở thư chết, thông điệp kia thành công ở lần ba.

### Lesson 288 · Consumer patterns - work queue, publish-subscribe and request-reply `TH`
**Prerequisites.** Lesson 287

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba mẫu tiêu thụ và điều kiện áp dụng của từng mẫu. Hàng đợi tác vụ: nhiều bên tiêu thụ cùng đọc một hàng đợi, broker chia việc, dùng khi công việc nặng và không cần thứ tự giữa các việc; prefetch ở lesson 285 quyết định chia đều tới đâu. Phát một nhận nhiều: mỗi bên tiêu thụ một hàng đợi riêng nối vào fanout hoặc topic, dùng khi nhiều hệ cần cùng một sự kiện; đây là chỗ RabbitMQ khác mô hình nhật ký rõ nhất, vì bên tiêu thụ mới chỉ nhận được sự kiện từ lúc nó có hàng đợi trở đi, quá khứ đã mất. Yêu cầu và trả lời: bên gửi đính kèm hàng đợi trả lời và mã tương quan, bên nhận trả kết quả về đó; dùng được nhưng thường là dấu hiệu nên dùng lời gọi trực tiếp, và ba câu hỏi để quyết định. Mã tương quan nối lại mã theo dõi ở lesson 74. Mẫu nào cũng phải trả lời được câu hỏi bên tiêu thụ mới tham gia thì thấy được gì.

**Outcome.** Chọn đúng mẫu cho một yêu cầu cho trước và nêu bên tiêu thụ tham gia sau thì thấy được gì, mất gì.

**Đánh giá.** Tầng *đánh giá*. Bài đòi so ba mẫu trên cùng một yêu cầu và chọn có lý do, chuẩn bị trực tiếp cho M30. Kiểm bằng ba yêu cầu kèm câu hỏi về bên tiêu thụ tham gia sau; đạt khi chọn đúng cả ba và trả lời đúng phần quá khứ bị mất.

**Lab.** Dựng cả ba mẫu trên kịch bản tham chiếu. Với mẫu phát một nhận nhiều, thêm một bên tiêu thụ sau khi đã phát 1.000 sự kiện và đếm chính xác nó nhận được bao nhiêu. Ghi lại con số đó; lesson 296 sẽ đo lại cùng phép thử trên Kafka.

**Pitfalls.** Dùng yêu cầu và trả lời cho việc lẽ ra gọi thẳng · tưởng bên tiêu thụ mới đọc được quá khứ · dùng một hàng đợi chung cho nhiều hệ rồi chúng tranh mất thông điệp của nhau.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba mẫu chạy được, và con số sự kiện mà bên tiêu thụ tham gia sau nhận được ghi đúng kèm giải thích vì sao bằng con số đó.

### Lesson 289 · Operating RabbitMQ - memory watermark, disk alarm and a stuck queue `TH`
**Prerequisites.** Lesson 288

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba cơ chế bảo vệ tự động và điều người vận hành nhìn thấy khi chúng kích hoạt. Ngưỡng bộ nhớ: vượt thì broker chặn bên gửi, và triệu chứng là bên gửi treo chứ báo lỗi, nên dễ bị chẩn đoán nhầm thành lỗi mạng. Cảnh báo đĩa: còn dưới ngưỡng thì broker cũng chặn. Giới hạn độ dài hàng đợi: tràn thì bỏ thông điệp cũ nhất hoặc đẩy sang thư chết tuỳ cấu hình. Bốn nguyên nhân làm hàng đợi ứ, kèm cách phân biệt bằng số đo: không có bên tiêu thụ, bên tiêu thụ chậm hơn bên gửi, bên tiêu thụ nhận rồi không xác nhận, và thông điệp hỏng chặn đầu. Ba chỉ số phải theo dõi liên tục: độ sâu hàng đợi, tốc độ vào trừ tốc độ ra, và số thông điệp chưa xác nhận. Vì sao cảnh báo theo tốc độ chênh lệch báo sớm hơn cảnh báo theo độ sâu, cùng nguyên tắc ngưỡng động ở tầng theo lô. Sổ tay xử lý cho ba tình huống hay gặp nhất.

**Outcome.** Chẩn đoán một hàng đợi đang ứ về đúng một trong bốn nguyên nhân, dẫn bằng số đo, và thực hiện đúng bước khắc phục.

**Đánh giá.** Tầng *phân tích*. Bài vận hành, người học đã có đủ cơ chế từ năm bài trước để suy ra nguyên nhân từ triệu chứng. Kiểm bằng bốn sự cố tiêm sẵn tính giờ; đạt khi chẩn đoán đúng ít nhất ba trong giới hạn thời gian và mỗi lần dẫn được số đo.

**Lab.** Giảng viên tiêm lần lượt bốn tình huống ứ, mỗi lần 10 phút. Với mỗi tình huống, ghi lại ba chỉ số, nêu nguyên nhân, thực hiện khắc phục, và xác nhận hàng đợi rút về bình thường. Đẩy bộ nhớ vượt ngưỡng một lần và ghi lại chính xác bên gửi biểu hiện thế nào.

**Pitfalls.** Chẩn đoán treo bên gửi thành lỗi mạng · cảnh báo theo độ sâu nên biết quá muộn · xoá hàng đợi để dọn thay vì tìm nguyên nhân · bỏ qua số thông điệp chưa xác nhận.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chẩn đoán đúng ≥ 3/4 tình huống trong giới hạn thời gian, mỗi lần dẫn số đo, và mô tả đúng biểu hiện của bên gửi khi vượt ngưỡng bộ nhớ.

### Lesson 290 · RabbitMQ on the reference scenario - measure and record the evidence `TH`
**Prerequisites.** Lesson 289

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài khép module: dựng trọn kịch bản tham chiếu ở M27 và ghi lại bằng chứng cho M30. Sự kiện đơn hàng từ PostgreSQL của pipeline lesson 217, hai bên tiêu thụ độc lập là bộ nạp mart và bộ kiểm gian lận, ba lỗi cài sẵn gồm một thông điệp trùng, một thông điệp tới sai thứ tự và một thông điệp hỏng. Bốn chỉ số phải đo, mỗi chỉ số kèm cách đo lặp lại được: thông lượng ổn định tính trên cửa sổ năm phút sau khi bỏ một phút đầu, độ trễ đầu cuối phân vị 95 đo từ dấu thời gian sinh sự kiện tới dấu thời gian ghi vào mart, thời gian phục hồi tính từ lúc giết tiến trình tới lúc tốc độ ra trở lại mức trước đó, và số thao tác để phát lại một ngày dữ liệu. Yêu cầu về bằng chứng: mỗi số phải kèm lệnh hoặc ảnh chụp tái lập được, vì lesson 261 đã đặt luật là mọi ô trong ma trận so sánh phải truy được về lab của chính mình. Phần khó riêng của RabbitMQ: phát lại một ngày không có sẵn nên phải ghi rõ cách mình tự dựng và chi phí của cách đó.

**Outcome.** Dựng xong kịch bản tham chiếu trên RabbitMQ, chạy đúng dưới cả ba lỗi cài sẵn, và nộp bốn chỉ số kèm cách đo lặp lại được.

**Đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module thành một hệ chạy được và một bộ bằng chứng, cao hơn tầng áp dụng vì phải tự thiết kế cách phát lại mà công cụ không cung cấp. Kiểm bằng rà soát chéo: một học viên khác chạy lại phép đo của bạn trên lab của họ; đạt khi cả bốn số tái lập được trong sai số 20%.

**Lab.** Dựng trọn kịch bản. Chạy dưới ba lỗi cài sẵn và chứng minh mart cuối không trùng, không thiếu, đúng thứ tự trạng thái đơn. Đo bốn chỉ số, ghi mỗi số kèm lệnh tái lập. Đổi hồ sơ đo với một học viên khác và chạy lại phép đo của họ.

**Pitfalls.** Đo ngay phút đầu khi hệ chưa ổn định · báo thông lượng đỉnh thay vì thông lượng ổn định · ghi số mà không ghi cách đo · bỏ qua chỉ số phát lại vì RabbitMQ không có sẵn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mart cuối đúng dưới cả ba lỗi, bốn chỉ số đều có cách đo kèm theo, và ≥ 3/4 số tái lập được trong sai số 20% khi người khác đo lại.

# MODULE 29 · APACHE KAFKA

**Lessons 291–304 · 28 giờ**

| | |
|---|---|
| **Objective cấp module** | Xây và vận hành được kịch bản tham chiếu trên Kafka ở mức `A`, giải thích mọi cấu hình đã chọn bằng cơ chế nhật ký phân vùng, và đo bốn chỉ số của M30 |
| **Tiền đề** | M28 |
| **Exit criterion** | Kịch bản tham chiếu chạy đúng dưới cả ba lỗi cài sẵn và dưới việc giết một broker, bốn chỉ số tái lập được, và bảo vệ được lựa chọn `acks` · số bản sao · khoá phân vùng bằng số đo |
| **Kỹ năng SFIA** | `SYSP` mức 4 · `NTAS` mức 4 · `HPCC` mức 3 |
| **Chế độ hỏng** | Học API bên gửi và bên nhận mà bỏ qua bản sao và offset, rồi mất dữ liệu khi một broker chết hoặc sinh trùng khi cân bằng lại nhóm |

Mức `A` theo quy ước ở mục 2: xây và vận hành được, không chỉ làm lab. Kafka là hiện thân của mô hình nhật ký ở lesson 280, nên module này đo lại đúng những phép thử đã làm trên RabbitMQ ở M28 để M30 có hai cột số đặt cạnh nhau.

Ba phép thử lặp lại nguyên văn từ M28: số sự kiện mà một bên tiêu thụ tham gia sau nhận được, đo ở lesson 288 và đo lại ở lesson 296; số thông điệp mất khi giết tiến trình, đo ở lesson 286 và đo lại ở lesson 298; và bốn chỉ số của kịch bản tham chiếu, đo ở lesson 290 và đo lại ở lesson 304.

### Lesson 291 · Architecture - broker, topic, partition and the log as the core structure `LT`
**Prerequisites.** Module 29: M28

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Kafka không phải hàng đợi mà là nhật ký chỉ ghi thêm được phân vùng, và mọi khác biệt với RabbitMQ đều suy ra từ một câu đó. Chủ đề là tên logic, phân vùng là đơn vị vật lý thật: mỗi phân vùng là một tệp nhật ký có thứ tự, mỗi bản ghi có một số thứ tự tăng dần gọi là offset. Đọc không xoá, nên nhiều nhóm tiêu thụ đọc cùng dữ liệu mà không đụng nhau, và đây là chỗ mô hình nhật ký giải sẵn vấn đề mà RabbitMQ phải dựng bằng fanout ở lesson 284. Ghi luôn nối vào cuối nên ghi tuần tự, nối thẳng về chênh lệch giữa ghi tuần tự và ghi ngẫu nhiên ở M2 và về nhật ký ghi trước ở lesson 118. Ba vai trong cụm: broker giữ phân vùng, một broker làm trưởng cho mỗi phân vùng, phần còn lại giữ bản sao. Phân đoạn tệp và chỉ mục offset ở mức đủ để hiểu vì sao tìm theo offset rẻ còn tìm theo nội dung thì không, cùng lý do với chỉ mục ở lesson 111.

**Outcome.** Vẽ được đường đi của một bản ghi từ bên gửi tới đĩa và tới bên tiêu thụ, gọi đúng tên chủ đề, phân vùng, offset và trưởng phân vùng.

**Đánh giá.** Tầng *hiểu*. Bài mở module, chưa đủ lab để đòi vận hành, nên objective dừng ở tái hiện cơ chế và nối nó với kiến thức lưu trữ đã có. Kiểm bằng bài vẽ có chú thích cộng ba câu hỏi vì sao; đạt khi bản vẽ đúng và trả lời được vì sao đọc không xoá dữ liệu.

**Lab.** Dựng cụm ba broker bằng container. Tạo một chủ đề ba phân vùng, gửi 100 bản ghi, xem tệp nhật ký trên đĩa và định vị phân đoạn. Chạy hai nhóm tiêu thụ độc lập trên cùng chủ đề và chứng minh cả hai đọc đủ 100 bản ghi. Vẽ lại kiến trúc có chú thích.

**Pitfalls.** Nhầm chủ đề với hàng đợi · tưởng đọc xong là bản ghi biến mất · nghĩ số phân vùng chỉ là chuyện hiệu năng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bản vẽ gọi đúng bốn khái niệm, hai nhóm tiêu thụ cùng đọc đủ 100 bản ghi, và giải thích đúng vì sao đọc không xoá.

### Lesson 292 · The producer path - batching, compression, acks and idempotent writes `TH`
**Prerequisites.** Lesson 291

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bên gửi không gửi từng bản ghi mà gom thành lô, và ba tham số quyết định hình dạng của lô: kích thước lô, thời gian chờ gom, và bộ nhớ đệm. Tăng thời gian chờ gom làm thông lượng tăng và độ trễ tăng theo, đây là đường đánh đổi phải đo chứ đoán, cùng dạng với prefetch ở lesson 285. Nén đặt ở bên gửi và giữ nguyên qua broker tới bên nhận, nên tiết kiệm cả đĩa lẫn băng thông; bốn thuật toán với ba mức đánh đổi giữa tỉ lệ nén và chi phí CPU. Tham số `acks` là chỗ ngữ nghĩa giao nhận ở lesson 278 thành cấu hình: `0` là gửi rồi quên, `1` là trưởng phân vùng đã ghi, `all` là đủ số bản sao tối thiểu đã ghi. Bên gửi bất biến bật lên thì Kafka tự khử trùng các lần thử lại trong cùng một phiên bằng số thứ tự nội bộ, **nhưng chỉ trong phiên đó**: bên gửi khởi động lại thì trùng vẫn có thể sinh, nên khử trùng theo khoá nghiệp vụ ở lesson 208 vẫn bắt buộc.

**Outcome.** Đo được quan hệ giữa thời gian chờ gom và cặp thông lượng, độ trễ phân vị 95, rồi chọn cấu hình có căn cứ từ số đo của chính mình.

**Đánh giá.** Tầng *đánh giá*. Bài đòi chọn một điểm trên đường đánh đổi từ dữ liệu tự đo, lặp lại đúng phương pháp đã dùng cho prefetch ở lesson 285 để hai cột số so được với nhau. Kiểm bằng bảng ít nhất bốn cấu hình; đạt khi có đường cong, có điểm chọn và lý do dẫn số.

**Lab.** Đo thông lượng và độ trễ phân vị 95 ở bốn giá trị thời gian chờ gom và ba thuật toán nén. Chạy lại ở `acks=1` và `acks=all` rồi ghi mức chênh thông lượng. Bật bên gửi bất biến, ép thử lại bằng cách ngắt mạng ngắn, đếm bản ghi trùng; rồi khởi động lại bên gửi giữa chừng và đếm lại.

**Pitfalls.** Để `acks=0` trong mã sản xuất · tin rằng bên gửi bất biến là đủ để khỏi khử trùng · so thông lượng giữa hai cấu hình nén khác nhau mà quên chi phí CPU.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng có đủ bốn mức thời gian chờ và ba thuật toán nén, chênh lệch giữa hai mức `acks` có số, và đếm đúng số trùng ở cả hai kịch bản thử lại.

### Lesson 293 · Partitioning and the key - throughput against order `TH`
**Prerequisites.** Lesson 292

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Số phân vùng đặt trần cho hai thứ cùng lúc: mức song song của bên tiêu thụ, vì một phân vùng chỉ được một bên tiêu thụ trong nhóm đọc, và phạm vi bảo đảm thứ tự ở lesson 279. Không có khoá thì bản ghi rải đều và mất thứ tự; có khoá thì cùng khoá vào cùng phân vùng và giữ thứ tự trong khoá đó. Bài toán khoá nóng: một mã khách chiếm phần lớn lưu lượng thì một phân vùng nặng hơn hẳn, và mức song song thực tế tụt về gần một, cùng hiện tượng lệch dữ liệu sẽ gặp lại ở lesson 349. Ba cách chữa và cái giá: thêm muối vào khoá thì mất thứ tự trong khoá, tách riêng khoá nóng thì thêm phức tạp vận hành, tăng phân vùng thì **ánh xạ khoá đổi nên thứ tự cũ đứt** và không lùi lại được vì Kafka không cho giảm số phân vùng. Chọn số phân vùng là quyết định khó sửa, nên phải ước lượng từ thông lượng đích chia cho thông lượng một phân vùng, cộng biên cho tăng trưởng.

**Outcome.** Chọn số phân vùng và khoá cho kịch bản tham chiếu, bảo vệ bằng số đo thông lượng, và trình bày được điều gì hỏng khi tăng phân vùng về sau.

**Đánh giá.** Tầng *đánh giá*. Objective là một quyết định khó đảo ngược, nên yêu cầu cao hơn tầng áp dụng: phải cân nhắc cả trạng thái tương lai. Kiểm bằng thí nghiệm tăng phân vùng giữa chừng; đạt khi dự đoán trước được hậu quả và số đo xác nhận dự đoán đó.

**Lab.** Đo thông lượng ở 1, 3, 6 và 12 phân vùng với cùng số bên tiêu thụ, rồi với số bên tiêu thụ bằng số phân vùng. Tạo khoá nóng chiếm 60% lưu lượng và đo lại. Viết dự đoán về thứ tự trước, rồi tăng phân vùng từ 3 lên 6 trên chủ đề đang chạy và kiểm chứng dự đoán bằng nhật ký.

**Pitfalls.** Đặt số phân vùng bằng một con số tròn mà không ước lượng · tăng phân vùng trên chủ đề có khoá mà không lường thứ tự đứt · thêm bên tiêu thụ vượt số phân vùng rồi tưởng nhanh hơn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng thông lượng đủ bốn mức phân vùng, đo được tác động của khoá nóng, và dự đoán về thứ tự khớp với nhật ký sau khi tăng phân vùng.

### Lesson 294 · The consumer group protocol - assignment, rebalance and its cost `TH`
**Prerequisites.** Lesson 293

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Nhóm tiêu thụ là cách Kafka chia phân vùng cho nhiều tiến trình, và điều phối viên nhóm nằm ở phía broker giữ việc chia đó. Cân bằng lại kích hoạt khi thành viên vào, ra, hoặc bị coi là chết; trong cân bằng lại kiểu dừng toàn bộ thì **mọi thành viên ngừng xử lý**, nên nhóm càng đông thì mỗi lần triển khai càng tốn thời gian dừng, đúng cảnh báo đã nêu ở lesson 280. Ba tham số quyết định khi nào một thành viên bị coi là chết, và vì sao đặt sai làm nhóm cân bằng lại liên tục: khoảng nhịp tim, thời gian chờ phiên, và khoảng tối đa giữa hai lần lấy dữ liệu. Nguyên nhân hay gặp nhất là xử lý một lô lâu hơn khoảng tối đa giữa hai lần lấy, nên thành viên bị đá ra ngay khi nó đang làm việc bình thường. Hai chiến lược chia giảm đau: chia dính giữ nguyên phần lớn phân vùng cũ, và thành viên tĩnh cho phép khởi động lại mà không kích hoạt chia lại. Đo chi phí cân bằng lại bằng thời gian từ lúc thành viên rời tới lúc tốc độ ra hồi phục.

**Outcome.** Chẩn đoán một nhóm đang cân bằng lại liên tục về đúng tham số gây ra, và giảm được thời gian dừng bằng cấu hình có số đo chứng minh.

**Đánh giá.** Tầng *phân tích*. Bài vận hành với triệu chứng dễ chẩn đoán nhầm, nên objective là truy ngược từ biểu hiện về nguyên nhân. Kiểm bằng sự cố tiêm sẵn tính giờ; đạt khi chẩn đoán đúng trong giới hạn thời gian và thời gian dừng đo được giảm sau khi sửa.

**Lab.** Đặt khoảng tối đa giữa hai lần lấy thấp hơn thời gian xử lý một lô và quan sát nhóm cân bằng lại liên tục. Đo thời gian dừng khi một thành viên rời ở nhóm ba và nhóm tám. Bật chia dính rồi đo lại. Bật thành viên tĩnh, khởi động lại một thành viên và ghi lại có kích hoạt chia lại không.

**Pitfalls.** Đặt thời gian chờ phiên rất lớn để né cân bằng lại rồi phát hiện thành viên chết mất nhiều phút mới bị nhận ra · xử lý lô dài mà không chỉnh tham số · kết luận về chi phí cân bằng lại mà chưa đo.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chẩn đoán đúng nguyên nhân trong giới hạn thời gian, và bảng thời gian dừng cho thấy chia dính hoặc thành viên tĩnh giảm được số đo đó.

### Lesson 295 · Offsets - where they live and committing them with the result `TH`
**Prerequisites.** Lesson 294

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Offset đã xử lý tới đâu được ghi vào một chủ đề nội bộ của Kafka, và chính sách ghi quyết định điều gì xảy ra khi bên tiêu thụ chết. Tự động ghi theo chu kỳ là mặc định và là nguồn sinh trùng lẫn mất dữ liệu phổ biến nhất: ghi sau khi lấy nhưng trước khi xử lý xong thì mất, ghi sau khi xử lý nhưng theo chu kỳ thì phần giữa hai lần ghi bị làm lại. Ghi thủ công sau khi xử lý xong cho ít nhất một lần, đúng định nghĩa ở lesson 278. Cách duy nhất đạt đúng một lần đầu cuối khi đích là cơ sở dữ liệu: **ghi offset vào chính cơ sở dữ liệu đó trong cùng một giao dịch với kết quả**, rồi khi khởi động lại thì đọc offset từ đó thay vì từ Kafka; đây là cách áp dụng trực tiếp nguyên tắc ghi bất biến ở lesson 106 và 207. Ba vị trí bắt đầu khi nhóm mới hoặc offset hết hạn, và vì sao mặc định đọc từ mới nhất làm mất dữ liệu trong lần triển khai đầu.

**Outcome.** Cài đặt được ghi offset cùng giao dịch với kết quả và chứng minh bằng thực nghiệm rằng giết tiến trình giữa chừng không sinh trùng và không mất bản ghi.

**Đánh giá.** Tầng *sáng tạo*. Bài đòi ghép cơ chế giao dịch của cơ sở dữ liệu với cơ chế offset của Kafka thành một mẫu mà không API nào cung cấp sẵn, nên cao hơn tầng áp dụng. Kiểm bằng đối soát sau khi giết tiến trình; đạt khi số bản ghi và tổng tiền khớp tuyệt đối.

**Lab.** Chạy ba cấu hình trên cùng tải: tự động ghi, ghi thủ công sau xử lý, và ghi cùng giao dịch với kết quả. Với mỗi cấu hình, giết bên tiêu thụ 5 lần ngẫu nhiên giữa chừng rồi đối soát bảng đích với nguồn. Lập bảng ba cấu hình với số trùng và số thiếu.

**Pitfalls.** Để tự động ghi offset trong mã sản xuất · ghi offset trước khi ghi kết quả · bắt đầu từ mới nhất ở lần triển khai đầu rồi mất dữ liệu · đối soát bằng số dòng mà quên tổng tiền.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng ba cấu hình có số trùng và số thiếu, và cấu hình cùng giao dịch cho 0 trùng 0 thiếu qua cả 5 lần giết.

### Lesson 296 · Retention, compaction and reading the past `TH`
**Prerequisites.** Lesson 295

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hai chính sách giữ dữ liệu phục vụ hai mục đích khác nhau. Giữ theo thời gian hoặc dung lượng: bản ghi cũ bị xoá theo phân đoạn, dùng cho luồng sự kiện. Nén theo khoá: giữ lại bản ghi mới nhất của mỗi khoá và xoá bản cũ hơn, biến chủ đề thành một ảnh chụp trạng thái hiện hành dựng lại được, và đây là nền của mẫu bảng thay đổi sẽ dùng ở M31. Bản ghi giá trị rỗng là dấu xoá, có thời gian giữ riêng để bên tiêu thụ chậm kịp thấy nó. Đọc lại quá khứ là thao tác bình thường: đặt lại offset của nhóm về đầu, về một offset cụ thể, hoặc về một dấu thời gian. Đây là chỗ khác biệt lớn nhất với RabbitMQ, nên **lặp lại nguyên văn phép thử ở lesson 288**: thêm một bên tiêu thụ sau khi đã phát 1.000 sự kiện và đếm nó nhận được bao nhiêu. Hai con số đặt cạnh nhau là bằng chứng chính của lesson 306. Giới hạn: phát lại chỉ đúng khi bên tiêu thụ bất biến, nếu không thì phát lại là nhân đôi.

**Outcome.** Đặt lại offset để phát lại một khoảng thời gian cho trước, và giải thích khác biệt số liệu giữa Kafka và RabbitMQ trong cùng phép thử bên tiêu thụ tham gia sau.

**Đánh giá.** Tầng *áp dụng*. Objective là một thao tác vận hành có kết quả kiểm được bằng phép đếm, cộng một so sánh đã có sẵn dữ liệu đối chứng. Kiểm bằng phép đếm và đối soát; đạt khi phát lại đúng khoảng yêu cầu và hai con số so sánh được giải thích đúng.

**Lab.** Phát 1.000 sự kiện rồi thêm một nhóm tiêu thụ mới và đếm số nhận được. Đặt con số đó cạnh con số đã ghi ở lesson 288. Dựng một chủ đề nén theo khoá cho bảng trạng thái khách hàng, gửi nhiều bản cập nhật cùng khoá, ép nén và chứng minh chỉ còn bản mới nhất. Phát lại đúng một ngày bằng cách đặt lại offset theo dấu thời gian và đối soát mart.

**Pitfalls.** Dùng nén theo khoá cho luồng sự kiện nên mất lịch sử · quên thời gian giữ dấu xoá · phát lại khi bên tiêu thụ chưa bất biến · đặt lại offset khi nhóm đang chạy.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bên tiêu thụ mới nhận đủ 1.000 và giải thích đúng chênh lệch với số ở lesson 288; chủ đề nén chỉ còn bản mới nhất mỗi khoá; phát lại một ngày đối soát khớp.

### Lesson 297 · Replication, ISR and what min.insync.replicas actually buys `LT`
**Prerequisites.** Lesson 296

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Mỗi phân vùng có một trưởng và các bản sao đi theo; tập bản sao đang bắt kịp gọi là ISR. Bản sao rơi khỏi ISR khi tụt quá xa so với trưởng, và tham số quyết định ngưỡng tụt đó. Ba tham số phải hiểu cùng nhau, vì đặt lẻ từng cái là nguồn mất dữ liệu âm thầm: hệ số nhân bản đặt khi tạo chủ đề, số bản sao tối thiểu phải ghi xong, và `acks` ở bên gửi tại lesson 292. Chỉ khi `acks=all` **và** số bản sao tối thiểu lớn hơn một thì mới thật sự có bảo đảm; đặt `acks=all` với số bản sao tối thiểu bằng một thì bảo đảm rơi về mức của một bản sao duy nhất. Bầu trưởng không sạch: cho phép một bản sao ngoài ISR lên làm trưởng thì cụm tiếp tục phục vụ nhưng **mất bản ghi đã xác nhận**, đây là lựa chọn giữa sẵn sàng và bền, nối lại phân biệt ở lesson 286. Quan hệ với độ trễ bản sao đã học ở lesson 120. Cách đọc trạng thái ISR để biết cụm đang khoẻ hay đang chỉ còn một bản sao thật sự.

**Outcome.** Với một bộ ba tham số cho trước, kết luận cụm chịu được mấy broker chết mà không mất bản ghi đã xác nhận, và chỉ ra cấu hình nào tạo bảo đảm giả.

**Đánh giá.** Tầng *đánh giá*. Objective đòi suy luận về tương tác của ba tham số chứ nhớ ý nghĩa từng cái, và đây là chỗ hay tạo bảo đảm giả trong hệ thật. Kiểm bằng sáu bộ tham số; đạt khi kết luận đúng ít nhất năm và nhận ra đủ các bộ tạo bảo đảm giả.

**Lab.** Nhận sáu bộ ba tham số. Với mỗi bộ, viết số broker chết tối đa mà không mất bản ghi đã xác nhận, và đánh dấu bộ nào tạo bảo đảm giả. Đọc trạng thái ISR của cụm đang chạy và nêu cụm hiện chịu được mấy broker chết. Bật bầu trưởng không sạch trên một chủ đề thử và mô tả đánh đổi.

**Pitfalls.** Đặt hệ số nhân bản cao mà để số bản sao tối thiểu bằng một · dùng `acks=all` rồi tưởng đã an toàn bất kể cấu hình broker · bật bầu trưởng không sạch trên chủ đề cần bền.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Kết luận đúng ≥ 5/6 bộ tham số và nhận ra đủ các bộ tạo bảo đảm giả.

### Lesson 298 · Durability under failure - kill a broker and count the messages `TH`
**Prerequisites.** Lesson 297

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài thí nghiệm hỏng, lặp lại đúng phương pháp đã dùng ở lesson 286 trên RabbitMQ để hai cột số so được với nhau. Ba kịch bản hỏng với ba biểu hiện khác nhau: giết broker không giữ trưởng của phân vùng đang ghi thì hầu như không thấy gì; giết broker đang giữ trưởng thì có một khoảng bầu lại trưởng, bên gửi thấy lỗi tạm thời và phải thử lại; giết đủ broker để ISR tụt dưới số bản sao tối thiểu thì bên gửi bị từ chối ghi, và **đây là hành vi đúng**, vì từ chối ghi còn hơn nhận rồi mất. Thời gian bầu lại trưởng đo được và phụ thuộc vào cấu hình phát hiện chết. Phân biệt ba loại số phải đếm sau thí nghiệm: bản ghi bên gửi tưởng đã gửi, bản ghi broker đã xác nhận, và bản ghi bên tiêu thụ thực nhận; chỉ khi cả ba khớp mới kết luận được không mất. Quy trình thí nghiệm lặp lại được: cố định tải, cố định thời điểm giết, chạy ba lần lấy trung vị.

**Outcome.** Đo được số bản ghi mất và thời gian phục hồi ở ba kịch bản hỏng, và kết luận cấu hình hiện tại chịu được kịch bản nào.

**Đánh giá.** Tầng *phân tích*. Bài đòi thiết kế và đọc một thí nghiệm hỏng chứ chạy một lệnh, nối tiếp phương pháp của cổng ở lesson 218. Kiểm bằng bảng ba kịch bản ba lần chạy; đạt khi ba số của mỗi kịch bản khớp nhau và kết luận dẫn được từ bảng.

**Lab.** Với cấu hình đủ bền, chạy ba kịch bản hỏng, mỗi kịch bản ba lần. Mỗi lần đếm cả ba loại số và đo thời gian phục hồi. Lập bảng và ghi trung vị. Chạy lại kịch bản hai với `acks=1` và ghi mức chênh. Đặt bảng này cạnh bảng ở lesson 286.

**Pitfalls.** Chỉ đếm số bản ghi ở đích mà quên số bên gửi tưởng đã gửi · chạy một lần rồi kết luận · coi việc bị từ chối ghi là lỗi cấu hình · quên cố định thời điểm giết nên ba lần không so được.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng ba kịch bản ba lần chạy đủ ba loại số, cấu hình đủ bền cho 0 mất ở kịch bản một và hai, và có số đo mức chênh khi hạ xuống `acks=1`.

### Lesson 299 · Schema registry and compatible change `TH`
**Prerequisites.** Lesson 298

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Kafka chở byte và không biết gì về cấu trúc bên trong, nên không có gì ngăn bên gửi đổi định dạng và làm mọi bên tiêu thụ hỏng cùng lúc. Sổ đăng ký lược đồ đặt một chốt ở giữa: bên gửi đăng ký lược đồ, bản ghi mang mã lược đồ, bên tiêu thụ tra để giải mã. Ba chế độ tương thích và ý nghĩa vận hành của từng chế độ: tương thích ngược cho phép bên tiêu thụ mới đọc dữ liệu cũ nên nâng cấp bên tiêu thụ trước; tương thích xuôi cho phép bên tiêu thụ cũ đọc dữ liệu mới nên nâng cấp bên gửi trước; tương thích đầy đủ cho cả hai và ràng buộc chặt nhất. Thay đổi nào an toàn và thay đổi nào phá vỡ, với quy tắc thực dụng: thêm trường có giá trị mặc định thì an toàn, xoá trường bắt buộc hoặc đổi kiểu thì không. Nối thẳng về tiến hoá lược đồ ở biên nhận dữ liệu tại lesson 209 và về hợp đồng dữ liệu ở M26: sổ đăng ký là cách cưỡng chế hợp đồng bằng máy thay vì bằng thoả thuận miệng.

**Outcome.** Chọn chế độ tương thích phù hợp với thứ tự triển khai của đội, và thực hiện được một thay đổi lược đồ phá vỡ mà không làm gián đoạn bên tiêu thụ đang chạy.

**Đánh giá.** Tầng *áp dụng*. Objective là một quy trình thay đổi có ràng buộc kiểm được bằng việc bên tiêu thụ cũ vẫn chạy. Kiểm bằng bài thực hiện thay đổi trên hệ đang chạy; đạt khi không bên tiêu thụ nào lỗi trong suốt quá trình.

**Lab.** Đăng ký lược đồ cho sự kiện đơn hàng. Thử ba thay đổi: thêm trường có mặc định, xoá trường bắt buộc, đổi kiểu một trường; ghi lại sổ đăng ký chấp nhận cái nào ở từng chế độ. Sau đó thực hiện thay đổi phá vỡ theo quy trình hai giai đoạn trên hệ đang chạy và chứng minh bên tiêu thụ cũ không lỗi lần nào.

**Pitfalls.** Đổi lược đồ mà không xét thứ tự triển khai · chọn tương thích đầy đủ rồi bị chặn mọi thay đổi cần thiết · coi sổ đăng ký là nơi lưu tài liệu thay vì một chốt cưỡng chế.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba thay đổi được phân loại đúng ở cả ba chế độ, và thay đổi phá vỡ hoàn tất mà bên tiêu thụ cũ không lỗi lần nào.

### Lesson 300 · Consumer lag - measuring it and alerting on the right signal `TH`
**Prerequisites.** Lesson 299

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Độ trễ tiêu thụ là hiệu giữa offset cuối của phân vùng và offset nhóm đã ghi, đo bằng số bản ghi. Đây là chỉ số sức khoẻ quan trọng nhất của một hệ luồng, nhưng đo sai cách thì báo động sai: độ trễ tính bằng bản ghi không nói được còn bao lâu mới đuổi kịp, vì một bản ghi có thể tốn một mili giây hoặc một giây. Hai chỉ số nên theo dõi cùng nhau: độ trễ theo bản ghi và độ trễ quy đổi ra thời gian, tính bằng độ trễ chia cho tốc độ xử lý hiện tại. Bốn nguyên nhân làm độ trễ tăng, phân biệt được bằng số đo, và ba trong bốn cái đã gặp dưới dạng khác ở lesson 289: bên tiêu thụ chậm hơn bên gửi, một phân vùng lệch tải, nhóm đang cân bằng lại liên tục, và hạ nguồn chậm. Đặt cảnh báo trên xu hướng tăng liên tục thay vì trên ngưỡng tuyệt đối, vì ngưỡng tuyệt đối hoặc quá nhạy lúc tải cao hoặc quá điếc lúc tải thấp, cùng nguyên tắc ngưỡng động đã dùng ở tầng theo lô.

**Outcome.** Đọc biểu đồ độ trễ và định vị đúng một trong bốn nguyên nhân, rồi đặt cảnh báo báo sớm hơn ngưỡng tuyệt đối trên cùng dữ liệu.

**Đánh giá.** Tầng *phân tích*. Bài đòi truy ngược từ hình dạng biểu đồ về cơ chế, kỹ năng trực tiếp dùng khi có sự cố. Kiểm bằng bốn sự cố tiêm sẵn; đạt khi định vị đúng ít nhất ba và cảnh báo mới báo trước cảnh báo ngưỡng ít nhất một khoảng đo được.

**Lab.** Dựng theo dõi độ trễ theo cả hai chỉ số. Giảng viên tiêm lần lượt bốn nguyên nhân. Với mỗi lần, ghi hình dạng biểu đồ, nêu nguyên nhân và bằng chứng. Đặt hai cảnh báo trên cùng dữ liệu lịch sử, một theo ngưỡng tuyệt đối và một theo xu hướng, rồi đo cái nào báo trước và trước bao lâu.

**Pitfalls.** Chỉ theo dõi độ trễ theo bản ghi · đặt ngưỡng tuyệt đối một con số tròn · bỏ qua độ trễ ở mức từng phân vùng nên không thấy lệch tải · tắt cảnh báo vì kêu nhiều thay vì sửa ngưỡng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Định vị đúng ≥ 3/4 nguyên nhân kèm bằng chứng, và cảnh báo theo xu hướng báo trước cảnh báo ngưỡng một khoảng đo được.

### Lesson 301 · Exactly-once with transactions, and its real boundary `TH`
**Prerequisites.** Lesson 300

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Kafka có giao dịch cho mẫu đọc rồi xử lý rồi ghi trong cùng một cụm: bên gửi giao dịch, ghi offset như một phần của giao dịch, và bên tiêu thụ đặt mức cô lập chỉ đọc bản ghi đã chốt. Điều này cho đúng một lần **trong phạm vi Kafka tới Kafka**. Ranh giới thật phải nói rõ: khi đích là cơ sở dữ liệu ngoài hoặc lời gọi tới hệ khác thì giao dịch của Kafka không bao trùm được, và cách duy nhất vẫn là ghi offset cùng giao dịch với kết quả như lesson 295, hoặc ghi có tính bất biến theo khoá nghiệp vụ. Cái giá đo được: giao dịch làm thông lượng giảm và độ trễ tăng vì phải chốt theo lô, và bài lab đo mức đó. Đây cũng là chỗ cần nói thẳng với đội: bật một cờ tên gọi hứa hẹn không làm hệ đúng một lần nếu tuyến đi ra ngoài Kafka, đúng kết luận đã rút ở lesson 278.

**Outcome.** Phân biệt được tuyến nào giao dịch Kafka bao trùm và tuyến nào không, rồi chọn đúng cơ chế cho từng tuyến kèm số đo chi phí.

**Đánh giá.** Tầng *đánh giá*. Objective là một phán đoán về ranh giới cơ chế, chỗ tài liệu nhà cung cấp hay gây hiểu nhầm. Kiểm bằng bốn tuyến khác nhau; đạt khi phân loại đúng cả bốn và có bảng chi phí đo được.

**Lab.** Cài đặt mẫu đọc rồi xử lý rồi ghi có giao dịch giữa hai chủ đề; giết tiến trình giữa chừng và chứng minh không trùng không thiếu. Đo thông lượng có và không có giao dịch. Cho bốn tuyến gồm Kafka tới Kafka, Kafka tới PostgreSQL, Kafka tới lời gọi web, và Kafka tới tệp; phân loại tuyến nào giao dịch bao trùm và viết cơ chế thay thế cho các tuyến còn lại.

**Pitfalls.** Tin rằng bật giao dịch là hệ thành đúng một lần bất kể đích · quên đặt mức cô lập ở bên tiêu thụ · bỏ qua chi phí thông lượng · dùng giao dịch cho tuyến ra ngoài Kafka rồi vẫn sinh trùng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mẫu trong Kafka cho 0 trùng 0 thiếu qua các lần giết, bảng chi phí có số, và phân loại đúng cả bốn tuyến kèm cơ chế thay thế.

### Lesson 302 · Kafka Connect - moving data without writing a consumer `TH`
**Prerequisites.** Lesson 301

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phần lớn việc chuyển dữ liệu vào hoặc ra Kafka là việc lặp lại, và viết lại một bên tiêu thụ cho mỗi đích là cách sinh ra mã không ai bảo trì. Connect là tầng chạy sẵn các trình nối: trình nối nguồn kéo vào Kafka, trình nối đích đẩy ra ngoài. Hai chế độ chạy và hệ quả vận hành: đơn lẻ dễ thử nhưng không chịu lỗi, phân tán thì cấu hình và offset nằm trong chính Kafka nên chịu được một nút chết. Trình biến đổi đơn giản cho những việc nhỏ như đổi tên trường hay che dữ liệu nhạy cảm; ranh giới phải giữ là **biến đổi có logic nghiệp vụ không thuộc về đây**, vì Connect không có kiểm thử và không có khả năng chạy lại như một công việc xử lý, cùng lập luận đã dùng khi nói về ranh giới của broker ở lesson 282. Xử lý bản ghi lỗi: chuyển sang chủ đề thư chết thay vì dừng cả trình nối. Khi nào tự viết bên tiêu thụ thì hợp lý hơn dùng Connect: ba tiêu chí quyết định.

**Outcome.** Dựng được một tuyến vào và một tuyến ra bằng Connect, cấu hình thư chết cho bản ghi lỗi, và nêu tiêu chí chọn giữa Connect và tự viết.

**Đánh giá.** Tầng *áp dụng*. Objective là dựng và cấu hình một thành phần có sẵn, chưa đòi thiết kế mới. Kiểm bằng tuyến chạy được cộng bài so sánh ngắn; đạt khi cả hai tuyến chạy, bản ghi lỗi vào thư chết, và tiêu chí chọn nêu được ba điểm.

**Lab.** Dựng trình nối nguồn từ PostgreSQL vào Kafka và trình nối đích từ Kafka ra kho đối tượng, chạy ở chế độ phân tán. Tiêm bản ghi sai định dạng và chứng minh trình nối không dừng mà đẩy sang thư chết. Giết một nút Connect và xác nhận công việc chuyển sang nút còn lại. Viết ba tiêu chí chọn giữa Connect và tự viết.

**Pitfalls.** Nhồi logic nghiệp vụ vào trình biến đổi đơn giản · chạy chế độ đơn lẻ trong sản xuất · để trình nối dừng vì một bản ghi lỗi · dùng Connect cho việc cần kiểm thử và chạy lại.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Hai tuyến chạy ở chế độ phân tán, bản ghi lỗi vào thư chết mà trình nối vẫn chạy, công việc chuyển nút thành công, và ba tiêu chí chọn được viết ra.

### Lesson 303 · Operating Kafka - sizing, rolling upgrade and a stuck group `TH`
**Prerequisites.** Lesson 302

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ước lượng quy mô từ ba đại lượng đầu vào: thông lượng ghi, hệ số nhân bản, và thời gian giữ; nhân lại ra dung lượng đĩa cần, cộng biên cho đỉnh tải và cho việc một broker chết làm phần còn lại gánh thêm. Vì sao đĩa thường hết trước khi CPU hết, và vì sao đặt thời gian giữ dài là quyết định tốn kém âm thầm. Nâng cấp cuốn chiếu: dừng từng broker một, chờ ISR đầy lại rồi mới sang broker kế, và lý do bỏ bước chờ là cách mất dữ liệu nhanh nhất. Quan sát tối thiểu phải có: độ trễ tiêu thụ ở lesson 300, số phân vùng thiếu bản sao, dung lượng đĩa còn lại, và số lần cân bằng lại nhóm mỗi giờ. Bốn sự cố hay gặp và cách phân biệt: nhóm kẹt vì cân bằng lại liên tục, nhóm kẹt vì một bản ghi hỏng chặn đầu, phân vùng thiếu bản sao kéo dài, và đĩa đầy làm broker dừng nhận ghi. Sổ tay xử lý cho từng sự cố, viết theo chuẩn đã dùng ở M26.

**Outcome.** Ước lượng được dung lượng đĩa cho một yêu cầu cho trước, thực hiện nâng cấp cuốn chiếu không mất bản ghi, và chẩn đoán một nhóm kẹt về đúng nguyên nhân.

**Đánh giá.** Tầng *áp dụng*. Bài vận hành tổng hợp, mọi cơ chế đã học ở các bài trước nên đây là bài ghép lại thành quy trình. Kiểm bằng ba phần: bảng ước lượng, nâng cấp thực tế có đếm bản ghi, và chẩn đoán tính giờ; đạt khi cả ba phần đạt.

**Lab.** Ước lượng đĩa cho 50.000 bản ghi mỗi giây, mỗi bản 1 KB, nhân bản 3, giữ 7 ngày, kèm biên. Thực hiện nâng cấp cuốn chiếu cụm ba broker trong lúc đang có tải, đếm bản ghi trước và sau. Giảng viên tiêm hai sự cố nhóm kẹt, mỗi lần 10 phút; chẩn đoán và khắc phục.

**Pitfalls.** Nâng cấp broker kế tiếp khi ISR chưa đầy lại · ước lượng đĩa mà quên hệ số nhân bản · chỉ theo dõi độ trễ mà bỏ phân vùng thiếu bản sao · khởi động lại cụm để chữa nhóm kẹt.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng ước lượng có đủ ba đại lượng và biên, nâng cấp cuốn chiếu mất 0 bản ghi, và chẩn đoán đúng ít nhất 1/2 sự cố trong giới hạn thời gian.

### Lesson 304 · Kafka on the reference scenario - measure and record the evidence `TH`
**Prerequisites.** Lesson 303

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài khép module, lặp lại nguyên văn yêu cầu của lesson 290 trên Kafka để M30 có hai cột số cùng đơn vị. Cùng kịch bản tham chiếu: sự kiện đơn hàng từ PostgreSQL của pipeline lesson 217, hai bên tiêu thụ độc lập, ba lỗi cài sẵn. Cùng bốn chỉ số với cùng cách đo: thông lượng ổn định trên cửa sổ năm phút sau khi bỏ một phút đầu, độ trễ đầu cuối phân vị 95, thời gian phục hồi sau khi giết tiến trình, và số thao tác để phát lại một ngày dữ liệu. Cảnh báo khi đọc hai cột: một phần chênh lệch đến từ cấu hình chứ từ bản chất công cụ, nên mỗi số phải ghi kèm cấu hình đã dùng, nếu không thì so sánh ở lesson 306 thành so sánh hai lần cấu hình khác nhau chứ hai công cụ. Phần khác biệt rõ nhất cần ghi riêng: phát lại một ngày trên Kafka là đặt lại offset, còn trên RabbitMQ phải tự dựng; ghi lại số thao tác của cả hai.

**Outcome.** Dựng xong kịch bản tham chiếu trên Kafka, chạy đúng dưới cả ba lỗi cài sẵn và dưới việc giết một broker, và nộp bốn chỉ số kèm cấu hình và cách đo.

**Đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module thành một hệ chạy được và một bộ bằng chứng so sánh được với M28. Kiểm bằng rà soát chéo như lesson 290; đạt khi ≥ 3/4 số tái lập được trong sai số 20% và mỗi số có cấu hình kèm theo.

**Lab.** Dựng trọn kịch bản. Chạy dưới ba lỗi cài sẵn cộng giết một broker giữa chừng, chứng minh mart cuối không trùng không thiếu đúng thứ tự. Đo bốn chỉ số, ghi kèm cấu hình và lệnh tái lập. Đặt bảng này cạnh bảng lesson 290 và đánh dấu những ô mà chênh lệch đến từ cấu hình chứ từ công cụ.

**Pitfalls.** Đo với cấu hình khác hẳn cấu hình đã dùng cho RabbitMQ rồi so hai cột · ghi số mà không ghi cấu hình · báo thông lượng đỉnh · bỏ qua chỉ số phát lại vì nó quá dễ trên Kafka.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mart cuối đúng dưới cả bốn tình huống hỏng, bốn chỉ số có cấu hình và cách đo kèm theo, và ≥ 3/4 số tái lập được trong sai số 20%.

# MODULE 30 · CHOOSING A MESSAGE SYSTEM

**Lessons 305–308 · 8 giờ**

| | |
|---|---|
| **Objective cấp module** | Chấm hai hệ truyền thông điệp trên sáu chiều, mỗi ô dẫn một quan sát từ lab của chính mình, và bảo vệ một lựa chọn cho đội có ràng buộc cho trước |
| **Tiền đề** | M28 · M29 |
| **Exit criterion** | Ma trận sáu chiều đạt rà soát chéo, mọi ô truy được về lab, và giữ vững hoặc đổi kết luận có lý do khi ràng buộc bị đổi giữa buổi |
| **Kỹ năng SFIA** | `ARCH` mức 4 |
| **Chế độ hỏng** | Chấm theo cảm nhận hoặc chép bảng so sánh của nhà cung cấp, cho ra kết luận không đứng vững khi ràng buộc đổi |

Module chỉ chạy được vì M28 và M29 đã dựng cùng một kịch bản tham chiếu và đo cùng bốn chỉ số ở lesson 290 và 304, cộng hai phép thử lặp lại ở lesson 288 với 296 và lesson 286 với 298. Không cùng bài toán thì đây là bài liệt kê tính năng, không phải bài so sánh, cùng ràng buộc với M18 và M25.

Ba bài đầu dựng tiêu chí và đo, bài cuối là buổi bảo vệ. Sáu chiều thay vì chín như M25 vì khối này có hai công cụ chứ ba, và vì hai chiều của M25 là mô hình hoá phụ thuộc và chạy bù không áp dụng ở đây.

### Lesson 305 · Six dimensions, and how to score each from lab evidence `LT`
**Prerequisites.** Module 30: M28 · M29

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Sáu chiều đánh giá và cách chuyển từng chiều thành một phép đo thực hiện được. Mô hình tiêu thụ: bên tiêu thụ mới tham gia thì thấy được gì, đo bằng phép đếm đã làm ở lesson 288 và 296. Phát lại: số thao tác và thời gian để chạy lại một ngày dữ liệu, số đã có ở lesson 290 và 304. Độ bền dưới sự cố: số bản ghi mất khi giết tiến trình, số đã có ở lesson 286 và 298. Thông lượng và độ trễ: hai số ở cùng một cấu hình so sánh được, kèm cảnh báo ở lesson 304 về chênh lệch do cấu hình. Công sức vận hành: số thành phần phải chạy, thao tác nâng cấp, và số chỉ số phải theo dõi. Kỹ năng đội: thời gian để người thứ hai sửa được một bên tiêu thụ. Nguyên tắc chấm giữ nguyên từ lesson 261: mỗi ô dẫn một quan sát có số hoặc có ảnh chụp từ lab của chính mình; ba nguồn không được dùng là bảng so sánh của nhà cung cấp, bài xếp hạng, và cảm nhận về cú pháp.

**Outcome.** Phát biểu cho từng chiều trong sáu chiều một phép đo thực hiện được trên lab đã làm, kèm đơn vị đo.

**Đánh giá.** Tầng *hiểu*. Bài dựng tiêu chí, chưa đo, nên objective dừng ở chỗ chuyển một chiều mơ hồ thành một phép đo lặp lại được. Kiểm bằng rà soát: mỗi phép đo phải nêu làm gì, đo cái gì, đơn vị là gì, và người khác lặp lại được. Chiều nào chỉ có tính từ mà không có phép đo thì không tính.

**Lab.** Với mỗi chiều, viết một phép đo gồm thao tác, đại lượng và đơn vị. Đối chiếu với số đã có ở lesson 286, 288, 290, 296, 298 và 304 xem chiều nào đã có sẵn dữ liệu và chiều nào còn thiếu. Đổi bài với một học viên khác và thử thực hiện phép đo của người kia trên lab của mình.

**Pitfalls.** Chấm bằng tính từ như nhanh, bền, dễ dùng · lấy số liệu từ tài liệu nhà cung cấp · đặt phép đo mà chỉ người viết mới thực hiện được.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Sáu phép đo đều nêu đủ thao tác, đại lượng và đơn vị, người khác lặp lại được, và chỉ đúng chiều nào còn thiếu dữ liệu.

### Lesson 306 · Fan-out, replay and the past - the axis that decides most designs `TH`
**Prerequisites.** Lesson 305

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Trục cho khác biệt lớn nhất giữa hai hệ, và lý do nằm ở mô hình lưu trữ chứ ở chất lượng cài đặt. Mô hình hàng đợi: lấy ra là biến mất, nên phát một nhận nhiều phải nhân bản ở phía broker và quá khứ không còn để đọc lại. Mô hình nhật ký: bản ghi nằm lại theo chính sách giữ, mỗi nhóm giữ con trỏ riêng, nên thêm bên tiêu thụ và đọc lại quá khứ là thao tác thường ngày. Hai con số đã đo ở lesson 288 và 296 là bằng chứng trực tiếp của trục này; đặt cạnh nhau và giải thích chênh lệch bằng cơ chế chứ bằng nhận xét. Ba câu hỏi vận hành dùng để đo trục: thêm một bên tiêu thụ mới tốn bao nhiêu thao tác và nó thấy được bao nhiêu quá khứ, phát lại một ngày tốn bao nhiêu thao tác, và sửa một lỗi logic rồi dựng lại dữ liệu ba tháng thì làm thế nào. Cảnh báo khi kết luận: một phần chênh lệch đến từ chính sách giữ đã chọn chứ từ công cụ, nên phải tách hai yếu tố trước khi kết luận.

**Outcome.** Trả lời ba câu hỏi vận hành trên cả hai hệ bằng số đo của chính mình, và giải thích chênh lệch bằng cơ chế lưu trữ.

**Đánh giá.** Tầng *phân tích*. Bài đòi quy chênh lệch quan sát được về nguyên nhân cơ chế, chứ ghi lại chênh lệch. Kiểm bằng bảng ba câu hỏi hai cột; đạt khi mỗi ô có số, và phần giải thích nêu đúng cơ chế chứ nêu tên công cụ.

**Lab.** Trên cả hai hệ, thực hiện ba việc: thêm một bên tiêu thụ mới và đếm số sự kiện quá khứ nó nhận được; phát lại một ngày và đếm số thao tác; dựng lại dữ liệu ba tháng sau khi sửa lỗi logic và ghi cách làm. Lập bảng hai cột. Với mỗi ô chênh lệch, viết một câu quy về cơ chế.

**Pitfalls.** Kết luận Kafka tốt hơn mà không nêu bài toán nào · quên rằng chính sách giữ do mình đặt chứ do công cụ · so số thao tác mà không so công sức dựng ban đầu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng ba câu hỏi hai cột đủ số, và mỗi ô chênh lệch có một câu quy về cơ chế lưu trữ chứ về tên công cụ.

### Lesson 307 · Operational cost and the team-skill constraint `TH`
**Prerequisites.** Lesson 306

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Chiều hay bị bỏ qua nhất và thường là chiều quyết định trong thực tế. Ba thành phần của công sức vận hành, đếm được chứ ước lượng: số tiến trình phải chạy và theo dõi, số thao tác trong một lần nâng cấp, và số chỉ số phải đặt cảnh báo. Dữ liệu đã có từ lesson 289 và 303. Chi phí hạ tầng ước lượng từ đĩa và bộ nhớ theo cách đã làm ở lesson 303, với lưu ý hệ số nhân bản làm đĩa nhân lên. Ràng buộc kỹ năng đội đo bằng một phép thử cụ thể: đưa một bên tiêu thụ đang chạy cho một học viên chưa làm module đó và tính thời gian tới khi họ sửa được một lỗi cho sẵn. Ba tình huống mà chiều này lật ngược kết luận của lesson 306: đội hai người không trực đêm, khối lượng dưới một nghìn sự kiện mỗi giây, và hệ chỉ có một bên tiêu thụ và không bao giờ cần phát lại. Nguyên tắc: chọn hệ mạnh hơn khả năng vận hành của đội là cách tạo ra sự cố mà không ai sửa được lúc ba giờ sáng.

**Outcome.** Đo ba thành phần công sức vận hành trên cả hai hệ và chỉ ra ít nhất một tình huống mà chiều này lật ngược kết luận của chiều trước.

**Đánh giá.** Tầng *đánh giá*. Objective đòi cân hai chiều mâu thuẫn nhau và kết luận theo ràng buộc, chứ cộng điểm. Kiểm bằng bảng đo cộng một tình huống lật ngược có lập luận; đạt khi ba thành phần đều có số và tình huống lật ngược đứng vững trước phản biện.

**Lab.** Đếm ba thành phần trên cả hai hệ. Thực hiện phép thử kỹ năng đội với một học viên chưa làm module tương ứng, tính giờ. Ước lượng chi phí hạ tầng cho cùng khối lượng. Viết một tình huống mà tổng các chiều này lật ngược kết luận của lesson 306, rồi bảo vệ nó trước hai phản biện của bạn cùng lớp.

**Pitfalls.** Ước lượng công sức bằng cảm nhận thay vì đếm · bỏ qua ràng buộc kỹ năng đội vì khó đo · cộng điểm các chiều như nhau mà không xét ràng buộc nào là chặn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba thành phần có số trên cả hai hệ, phép thử kỹ năng đội có kết quả tính giờ, và tình huống lật ngược đứng vững trước hai phản biện.

### Lesson 308 · The decision - defend one choice for a team with given constraints `KT`
**Prerequisites.** Lesson 307

**In-class (120 phút).** 75 phút làm bài độc lập · 45 phút chữa bài và phân tích lỗi theo nhóm

**Learn.** Buổi bảo vệ, cùng khuôn với lesson 266 ở khối điều phối. Mỗi học viên nhận một hồ sơ đội có ràng buộc cụ thể gồm khối lượng, số bên tiêu thụ, nhu cầu phát lại, quy mô đội, và khả năng trực. Nộp ma trận sáu chiều đã điền từ lab của chính mình, một khuyến nghị, và phần nêu rõ điều kiện nào làm khuyến nghị đó sai. Giữa buổi hội đồng đổi một ràng buộc; học viên phải hoặc giữ kết luận với lý do, hoặc đổi kết luận với lý do, và **cả hai đều được điểm nếu lập luận dẫn từ ma trận**. Cái không được điểm là đổi kết luận mà không nêu ô nào trong ma trận đã đổi giá trị.

**Outcome.** Bảo vệ được một lựa chọn cho hồ sơ đội cho trước, mọi ô trong ma trận truy được về lab của chính mình, và phản ứng đúng khi một ràng buộc bị đổi.

**Đánh giá.** Tầng *đánh giá*. Cổng của khối, kiểm năng lực ra quyết định có bằng chứng chứ kiểm trí nhớ về tính năng. Kiểm bằng buổi bảo vệ có đổi ràng buộc giữa chừng; thang điểm ở phần Đề gồm.

**Lab.** Nhận một hồ sơ đội: khối lượng sự kiện, số bên tiêu thụ, nhu cầu phát lại, quy mô đội, ai trực khi hỏng. Bài chấm năm phần: A (25đ) ma trận sáu chiều điền đủ, mỗi ô dẫn một quan sát từ lab · B (25đ) khuyến nghị kèm ba điều kiện làm nó sai · C (25đ) phản ứng khi hội đồng đổi một ràng buộc giữa buổi · D (15đ) chỉ ra hai ô mà chênh lệch đến từ cấu hình chứ từ công cụ · E (10đ) nêu một tình huống không nên dùng broker nào cả, theo lesson 282.

**Pitfalls.** Chép bảng so sánh của nhà cung cấp · đổi kết luận khi bị vặn mà không dẫn ô nào · bỏ phần E vì hết giờ · trình bày ma trận mà không ai kiểm được số.

**Self-study (2,4 giờ).** Không có bài tự học. Nếu không đạt, theo phụ lục khắc phục khi không đạt cổng

**Done when.** Đạt ≥ 70/100 và phần A ≥ 60%. Ô nào không truy được về lab thì không tính điểm ô đó.

# MODULE 31 · CHANGE DATA CAPTURE WITH DEBEZIUM

**Lessons 309–316 · 16 giờ**

| | |
|---|---|
| **Objective cấp module** | Thay một tuyến nạp gia tăng theo lô bằng CDC đọc nhật ký, và chứng minh tuyến mới bắt được cả ba thứ mà bản cũ bỏ sót |
| **Tiền đề** | M29 |
| **Exit criterion** | Tuyến CDC chạy qua một lần chụp đầu, một đợt thay đổi lược đồ nguồn và một lần khởi động lại, đối soát khớp tuyệt đối với bảng nguồn |
| **Kỹ năng SFIA** | `DBAD` mức 3 · `DTAN` mức 3 |
| **Chế độ hỏng** | Bật trình nối rồi coi là xong, không theo dõi khe sao chép, tới khi đĩa cơ sở dữ liệu nguồn đầy thì cả hệ sản xuất dừng |

Mức `B` theo quy ước ở mục 2. Module đứng sau M29 vì Debezium ghi ra Kafka và dùng trực tiếp chủ đề nén theo khoá ở lesson 296 làm bảng thay đổi.

Đây là lần thứ hai chương trình quay lại bài toán nạp gia tăng. Lần đầu ở lesson 204 và 205 giải bằng cột mốc và truy vấn định kỳ; module này giải bằng nhật ký giao dịch, và phần lớn giá trị nằm ở chỗ so hai cách trên cùng một nguồn chứ ở chỗ cài đặt công cụ.

### Lesson 309 · Why CDC exists - the cost of polling and the rows it misses `LT`
**Prerequisites.** Module 31: M29

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Truy vấn định kỳ theo cột mốc ở lesson 205 bỏ sót ba thứ, và cả ba đều im lặng. Một là bản ghi bị xoá: không còn dòng nào để truy vấn thấy, nên đích giữ lại bản ghi đã chết mãi mãi trừ khi có cờ xoá mềm. Hai là thay đổi trung gian: một đơn đổi trạng thái ba lần giữa hai lần quét thì đích chỉ thấy trạng thái cuối, và mọi phân tích về thời gian ở mỗi trạng thái đều sai. Ba là bản ghi cập nhật mà không đụng cột mốc, thường do sửa tay hoặc do một đường ghi khác quên cập nhật trường thời gian. Chi phí của truy vấn định kỳ cũng đáng kể: mỗi lần quét là một lần đọc trên cơ sở dữ liệu đang phục vụ sản xuất, và quét càng dày thì tải càng nặng, nên có một trần thực tế cho độ tươi. CDC đọc nhật ký giao dịch thay vì đọc bảng, nên thấy đủ ba thứ trên và gần như không thêm tải đọc. Cái giá: phụ thuộc vào cấu hình nội bộ của cơ sở dữ liệu nguồn, cần quyền cao, và thêm một hệ phải trực.

**Outcome.** Chỉ ra trong một tuyến nạp theo cột mốc cho trước những bản ghi nào bị bỏ sót, và định lượng mức sai lệch bằng số đếm trên dữ liệu thật.

**Đánh giá.** Tầng *phân tích*. Người học đã tự xây tuyến gia tăng ở M20 nên có hệ để soi lại; objective là tìm ra chỗ hỏng của chính công trình cũ chứ tiếp nhận một khẳng định. Kiểm bằng phép đếm đối chứng; đạt khi định lượng đúng cả ba loại bỏ sót.

**Lab.** Trên tuyến gia tăng đã dựng ở lesson 217, chạy một kịch bản gồm xoá 50 bản ghi, đổi trạng thái 200 đơn ba lần trong một chu kỳ quét, và cập nhật 30 bản ghi mà không đụng cột mốc. Sau một chu kỳ, đối soát đích với nguồn và đếm chính xác từng loại sai lệch.

**Pitfalls.** Kết luận truy vấn định kỳ luôn tệ hơn mà không xét tải và độ phức tạp · dùng xoá mềm rồi tưởng đã giải xong bài toán xoá · quét dày hơn để chữa mà không đo tải lên nguồn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đếm đúng cả ba loại bỏ sót với số khớp kịch bản đã tiêm, và nêu được mức tải thêm khi tăng tần suất quét.

### Lesson 310 · Reading the database log - logical decoding and the replication slot `LT`
**Prerequisites.** Lesson 309

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** CDC đọc chính cái nhật ký mà cơ sở dữ liệu vốn đã ghi để phục hồi sau sự cố ở lesson 118 và để sao chép sang bản sao ở lesson 120. Giải mã logic biến các bản ghi nhật ký ở dạng vật lý thành sự kiện có nghĩa: bảng nào, thao tác gì, giá trị trước và sau. Khe sao chép là con trỏ phía máy chủ ghi nhớ bên đọc đã tiêu thụ tới đâu, và **đây là chi tiết nguy hiểm nhất của cả module**: máy chủ không được xoá nhật ký mà khe chưa đọc tới, nên bên đọc dừng mà khe còn đó thì nhật ký dồn lại cho tới khi đầy đĩa và cơ sở dữ liệu sản xuất ngừng nhận ghi. Hai loại khe và khác biệt khi khởi động lại. Danh tính bản ghi quyết định sự kiện xoá và cập nhật mang theo bao nhiêu thông tin: mặc định chỉ có khoá chính, đặt đầy đủ thì có toàn bộ giá trị trước nhưng nhật ký phình. Mỗi hệ một cơ chế: MySQL dùng nhật ký nhị phân theo dòng, MongoDB dùng luồng thay đổi, và cả ba đã gặp ở M11 tới M13.

**Outcome.** Giải thích đường đi từ một lệnh cập nhật tới một sự kiện thay đổi, gọi đúng tên nhật ký, giải mã logic và khe, và nêu điều gì xảy ra khi bên đọc dừng.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết nối kiến thức nội bộ cơ sở dữ liệu đã có với một cơ chế mới, chưa đòi vận hành. Kiểm bằng bài giải thích cộng một thí nghiệm quan sát; đạt khi mô tả đúng đường đi và dự đoán đúng hậu quả của việc dừng bên đọc.

**Lab.** Bật giải mã logic trên PostgreSQL, tạo một khe, dùng công cụ dòng lệnh đọc trực tiếp sự kiện thô. Chạy chèn, cập nhật, xoá và đọc ra ba loại sự kiện. Đổi danh tính bản ghi và quan sát sự kiện xoá đổi nội dung ra sao. Dừng bên đọc 10 phút trong lúc có tải ghi và đo kích thước nhật ký dồn lại.

**Pitfalls.** Tạo khe rồi quên, để nó giữ nhật ký vô hạn · tưởng CDC không đụng gì tới nguồn · dùng danh tính bản ghi mặc định rồi không có giá trị trước để đối soát.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mô tả đúng ba thành phần trên đường đi, và số đo kích thước nhật ký dồn lại sau 10 phút dừng khớp với dự đoán về hướng tăng.

### Lesson 311 · Debezium architecture - connector, offset and the change event envelope `TH`
**Prerequisites.** Lesson 310

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Debezium là một trình nối nguồn chạy trên Kafka Connect ở lesson 302, nên mọi thứ đã học về chế độ phân tán, cấu hình và thư chết áp dụng nguyên vẹn. Nó giữ hai loại vị trí và trộn lẫn hai loại này là nguồn lỗi hay gặp: offset của trình nối ghi vị trí đã đọc tới trong nhật ký nguồn, còn offset của bên tiêu thụ ở lesson 295 là chuyện phía sau, hoàn toàn độc lập. Phong bì sự kiện thay đổi có cấu trúc cố định gồm trạng thái trước, trạng thái sau, siêu dữ liệu nguồn và loại thao tác. Bốn loại thao tác và ý nghĩa của trường trước trong từng loại: chèn thì trước rỗng, cập nhật thì có cả hai, xoá thì sau rỗng, đọc là loại riêng chỉ xuất hiện trong lần chụp đầu. Siêu dữ liệu nguồn mang số thứ tự trong nhật ký và dấu thời gian giao dịch, và đây là thứ dùng để sắp lại đúng thứ tự khi cần. Quy ước đặt tên chủ đề: mỗi bảng một chủ đề, khoá chính làm khoá bản ghi, nên thứ tự trong một hàng được bảo đảm theo đúng lập luận ở lesson 279.

**Outcome.** Đọc được một sự kiện thay đổi thô và nói đúng thao tác gì xảy ra trên hàng nào, dùng trường trước và sau để chứng minh.

**Đánh giá.** Tầng *áp dụng*. Bài thực hành đầu của module, đòi dùng đúng cấu trúc dữ liệu chứ thiết kế mới. Kiểm bằng bài đọc sự kiện có đáp án; đạt khi giải mã đúng ít nhất 9/10 sự kiện và giải thích được vì sao khoá chủ đề là khoá chính.

**Lab.** Dựng Debezium trên Kafka Connect đọc bảng đơn hàng. Sinh 10 thao tác hỗn hợp trên nguồn, bắt 10 sự kiện tương ứng, và với mỗi sự kiện viết ra thao tác gì trên hàng nào, dẫn bằng trường trước và sau. Đổi khoá chủ đề sang ngẫu nhiên và chứng minh thứ tự trong một hàng không còn được bảo đảm.

**Pitfalls.** Nhầm offset trình nối với offset bên tiêu thụ · bỏ qua trường thao tác nên xử lý sự kiện xoá như cập nhật · đặt khoá bản ghi khác khoá chính rồi mất thứ tự trong hàng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Giải mã đúng ≥ 9/10 sự kiện, và chứng minh được bằng thực nghiệm rằng đổi khoá làm mất thứ tự trong hàng.

### Lesson 312 · Snapshot and the handover to streaming `TH`
**Prerequisites.** Lesson 311

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Nhật ký giao dịch chỉ giữ một khoảng gần đây, nên CDC không thể dựng lại lịch sử từ đầu; phải chụp trạng thái hiện tại trước rồi mới chuyển sang đọc liên tục. Chỗ khó nằm ở mối nối giữa hai giai đoạn: chụp mất nhiều giờ trên bảng lớn, và trong lúc đó nguồn vẫn đang thay đổi, nên nếu mối nối sai thì hoặc mất thay đổi xảy ra giữa chừng hoặc nhân đôi chúng. Bốn chế độ chụp và tình huống dùng: chụp rồi chuyển sang luồng, chỉ chụp, chỉ luồng khi đích đã có sẵn dữ liệu, và chụp gia tăng theo lô nhỏ để không khoá bảng lâu. Tác động lên nguồn khi chụp: đọc nặng, và ở một số cấu hình có khoá đọc, nên phải chọn cửa sổ thời gian. Chụp gia tăng giải quyết bằng cách chia bảng thành cửa sổ khoá chính và xen kẽ với luồng, đổi lại logic phức tạp hơn. Vì sao khử trùng theo khoá nghiệp vụ ở lesson 208 vẫn cần: mối nối có thể phát lại một đoạn, và đích phải chịu được điều đó.

**Outcome.** Chạy được một lần chụp trên bảng đang có ghi và chứng minh bằng đối soát rằng không thay đổi nào bị mất hay nhân đôi ở mối nối.

**Đánh giá.** Tầng *áp dụng*. Objective là một thao tác vận hành có kết quả kiểm được bằng đối soát, đúng phương pháp của lesson 212. Kiểm bằng đối soát số dòng và tổng tiền sau khi chụp xong; đạt khi khớp tuyệt đối trong khi nguồn vẫn có ghi.

**Lab.** Chạy chụp trên bảng 2 triệu dòng trong lúc một tiến trình khác liên tục chèn và cập nhật. Sau khi chuyển sang luồng, đối soát đích với nguồn theo số dòng và tổng tiền. Đo thời gian chụp và tải thêm trên nguồn. Chạy lại bằng chế độ chụp gia tăng và so hai cột số.

**Pitfalls.** Chụp trong giờ cao điểm rồi làm chậm hệ sản xuất · dừng ghi ở nguồn để chụp cho an toàn · đối soát bằng số dòng mà quên tổng tiền · tin rằng mối nối luôn đúng nên không đối soát.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đối soát khớp tuyệt đối cả số dòng lẫn tổng tiền khi nguồn vẫn đang ghi, và có bảng so thời gian cùng tải giữa hai chế độ chụp.

### Lesson 313 · Schema change at the source and what reaches the consumer `TH`
**Prerequisites.** Lesson 312

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Thay đổi lược đồ ở nguồn đi thẳng vào sự kiện thay đổi, nên CDC là đường truyền rủi ro lược đồ nhanh nhất trong cả hệ: đội nguồn thêm cột lúc 10 giờ thì 10 giờ 01 đích đã nhận cấu trúc mới. Ba loại thay đổi và hành vi tương ứng: thêm cột thì sự kiện có thêm trường và bên tiêu thụ cũ bỏ qua được nếu lược đồ tương thích ngược ở lesson 299; đổi kiểu thì có thể phá vỡ và sổ đăng ký chặn; xoá cột thì bên tiêu thụ còn dùng cột đó sẽ hỏng. Debezium phát sự kiện thay đổi lược đồ vào một chủ đề riêng, và đây là chỗ nối CDC với hợp đồng dữ liệu ở M26: hợp đồng nói đội nguồn phải báo trước, sổ đăng ký cưỡng chế bằng máy, còn chủ đề lược đồ cho đích biết chuyện đã xảy ra. Ba cách xử lý khi nguồn đổi kiểu, theo đúng ba chiến lược đã đặt ở lesson 209 cho biên nạp theo lô: bỏ qua, tự thêm, hoặc dừng và báo.

**Outcome.** Thực hiện được ba loại thay đổi lược đồ ở nguồn và mô tả chính xác cái gì tới được bên tiêu thụ trong từng loại.

**Đánh giá.** Tầng *phân tích*. Bài đòi truy hậu quả từ một thay đổi ở đầu này sang biểu hiện ở đầu kia, xuyên qua ba thành phần. Kiểm bằng ba thí nghiệm có dự đoán viết trước; đạt khi cả ba dự đoán khớp quan sát, hoặc chênh thì giải thích được nguyên nhân.

**Lab.** Với tuyến CDC đang chạy và bên tiêu thụ đang ghi mart, viết dự đoán trước rồi thực hiện lần lượt: thêm một cột có mặc định, đổi kiểu một cột, xoá một cột đang được mart dùng. Với mỗi lần, ghi lại sự kiện lược đồ, hành vi của sổ đăng ký, và trạng thái bên tiêu thụ. Cấu hình lại theo chiến lược dừng và báo rồi lặp lại thí nghiệm xoá cột.

**Pitfalls.** Không bật sổ đăng ký nên thay đổi phá vỡ đi thẳng tới đích · bỏ qua chủ đề lược đồ · coi CDC là lý do không cần hợp đồng dữ liệu nữa.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba dự đoán khớp quan sát hoặc chênh có giải thích, và sau khi đổi chiến lược thì xoá cột làm tuyến dừng có cảnh báo thay vì ghi dữ liệu sai.

### Lesson 314 · Compacted topics as a changelog and rebuilding current state `TH`
**Prerequisites.** Lesson 313

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Chủ đề nén theo khoá ở lesson 296 và luồng CDC khớp nhau đúng một cách: khoá là khoá chính, giá trị là trạng thái sau, nên chủ đề nén trở thành ảnh chụp trạng thái hiện hành dựng lại được bất cứ lúc nào. Sự kiện xoá phát ra bản ghi giá trị rỗng để nén loại bỏ hẳn khoá đó. Hai cách dùng luồng thay đổi ở đích, và chọn sai là sai kiến trúc chứ sai cấu hình: dựng bảng trạng thái hiện hành bằng cách gộp theo khoá lấy bản mới nhất, hoặc giữ toàn bộ lịch sử thay đổi để dựng bảng chiều biến đổi chậm loại 2 đúng như cơ chế ở lesson 195. Luồng CDC là nguồn tự nhiên nhất cho loại 2 vì nó có đủ mốc thời gian của từng lần đổi, thứ mà nạp theo lô hằng ngày không bao giờ có. Điều kiện để dựng lại được: bên ghi phải bất biến theo lesson 106, và thứ tự trong một khoá phải được giữ theo lesson 279.

**Outcome.** Dựng được cả bảng trạng thái hiện hành lẫn bảng lịch sử loại 2 từ cùng một luồng CDC, và dựng lại được trạng thái sau khi xoá sạch đích.

**Đánh giá.** Tầng *sáng tạo*. Bài đòi ghép nén theo khoá, mô hình chiều và tính bất biến thành một thiết kế, chứ chạy một tính năng. Kiểm bằng việc xoá sạch bảng đích rồi dựng lại từ chủ đề; đạt khi bảng dựng lại khớp tuyệt đối với bản trước khi xoá.

**Lab.** Cấu hình chủ đề CDC nén theo khoá. Dựng hai đích từ cùng luồng: bảng trạng thái hiện hành và bảng loại 2 có cột hiệu lực từ và đến. Sinh một chuỗi thay đổi có cả xoá. Xoá sạch cả hai bảng đích rồi dựng lại hoàn toàn từ chủ đề và đối soát với bản đã lưu trước đó.

**Pitfalls.** Nén theo khoá trên chủ đề cần giữ lịch sử nên mất các bước trung gian · quên bản ghi rỗng nên bản ghi đã xoá sống lại khi dựng lại · dựng loại 2 mà không bất biến nên chạy lại sinh trùng dòng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Cả hai bảng dựng lại từ chủ đề khớp tuyệt đối với bản trước khi xoá, kể cả các khoá đã bị xoá ở nguồn.

### Lesson 315 · Operating CDC - slot growth, lag and the failure that fills the disk `TH`
**Prerequisites.** Lesson 314

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Chế độ hỏng nguy hiểm nhất của module, và nó đánh vào cơ sở dữ liệu sản xuất chứ vào hệ phân tích: bên đọc dừng, khe sao chép giữ nhật ký, nhật ký dồn, đĩa đầy, nguồn ngừng nhận ghi. Ba chỉ số phải theo dõi liên tục, và chỉ số đầu là chỉ số cảnh báo sớm duy nhất: dung lượng nhật ký mà khe đang giữ, độ trễ của trình nối tính bằng thời gian, và độ trễ tiêu thụ phía sau theo lesson 300. Ngưỡng nên đặt theo tốc độ tăng chứ theo giá trị tuyệt đối, cùng lập luận đã dùng ở lesson 300. Bốn nguyên nhân làm khe phình và cách phân biệt: trình nối chết, trình nối chạy nhưng chậm hơn tốc độ ghi, Kafka không nhận được nên trình nối chặn, và một giao dịch dài ở nguồn giữ nhật ký. Quy trình xử lý khẩn khi đĩa sắp đầy, và câu hỏi khó phải quyết trong vài phút: xoá khe để cứu nguồn và chấp nhận phải chụp lại từ đầu, hay cố cứu trình nối. Sổ tay xử lý viết theo chuẩn M26, có ngưỡng và có người chịu trách nhiệm.

**Outcome.** Chẩn đoán một khe đang phình về đúng một trong bốn nguyên nhân bằng số đo, và thực hiện đúng quy trình khẩn khi đĩa nguồn sắp đầy.

**Đánh giá.** Tầng *phân tích*. Bài vận hành có rủi ro thật lên hệ sản xuất, nên objective là chẩn đoán dưới áp lực thời gian. Kiểm bằng ba sự cố tiêm sẵn tính giờ; đạt khi chẩn đoán đúng ít nhất hai và quyết định khẩn có lập luận về đánh đổi.

**Lab.** Dựng theo dõi ba chỉ số với cảnh báo theo tốc độ tăng. Giảng viên tiêm ba tình huống làm khe phình, mỗi lần 10 phút. Với mỗi lần, ghi ba chỉ số, nêu nguyên nhân, xử lý. Ở tình huống cuối, đĩa mô phỏng còn 5%: viết quyết định và lập luận đánh đổi trong 3 phút.

**Pitfalls.** Chỉ theo dõi độ trễ mà bỏ dung lượng khe · đặt ngưỡng tuyệt đối · xoá khe theo phản xạ mà không tính chi phí chụp lại · để khe của môi trường thử trỏ vào nguồn sản xuất rồi quên.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chẩn đoán đúng ≥ 2/3 tình huống kèm số đo, và quyết định khẩn nêu được cả hai phía của đánh đổi kèm chi phí ước lượng.

### Lesson 316 · CDC into the reference pipeline - replacing an incremental batch load `TH`
**Prerequisites.** Lesson 315

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài khép module: thay tuyến nạp gia tăng theo cột mốc đã dựng ở lesson 217 bằng tuyến CDC, rồi chạy song song hai tuyến trên cùng nguồn để so. Bốn đại lượng phải đo trên cả hai tuyến: độ tươi tính từ lúc thay đổi xảy ra ở nguồn tới lúc thấy ở mart, tải thêm trên cơ sở dữ liệu nguồn, số bản ghi sai lệch theo ba loại ở lesson 309, và công sức vận hành tính bằng số thành phần cùng số chỉ số phải theo dõi. Chạy song song là bắt buộc chứ tuỳ chọn: chuyển thẳng rồi mới so là cách mất khả năng đối chứng. Kết luận phải nêu cả chiều ngược: CDC không phải lựa chọn đúng cho mọi nguồn, và ba tình huống nên giữ nạp theo lô gồm nguồn không cho bật giải mã logic, khối lượng thay đổi rất nhỏ, và đội không đủ người trực. Bằng chứng ghi lại theo chuẩn đã dùng ở lesson 290 và 304 để về sau đưa vào hồ sơ quyết định kiến trúc.

**Outcome.** Chạy song song hai tuyến trên cùng nguồn, đo bốn đại lượng, và đưa ra khuyến nghị kèm điều kiện làm khuyến nghị đó sai.

**Đánh giá.** Tầng *đánh giá*. Bài tổng hợp module thành một quyết định có bằng chứng, chuẩn bị cho hồ sơ kiến trúc ở M39. Kiểm bằng bảng bốn đại lượng hai cột cộng phần điều kiện đảo ngược; đạt khi mỗi ô có số và nêu được ít nhất hai điều kiện đảo ngược cụ thể.

**Lab.** Chạy song song tuyến CDC và tuyến theo cột mốc trên cùng nguồn trong 24 giờ có tải mô phỏng. Đo bốn đại lượng. Lập bảng hai cột. Viết khuyến nghị cho một đội cho trước kèm hai điều kiện làm khuyến nghị sai, và nêu tuyến nào trong ba tình huống ở phần Learn nên giữ nạp theo lô.

**Pitfalls.** Chuyển thẳng sang CDC rồi bỏ tuyến cũ nên không còn đối chứng · đo độ tươi mà quên tải lên nguồn · khuyến nghị CDC cho mọi trường hợp · ghi số mà không ghi cách đo.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng bốn đại lượng hai cột đủ số kèm cách đo, và khuyến nghị có ít nhất hai điều kiện đảo ngược cụ thể.

# MODULE 32 · STREAM PROCESSING

**Lessons 317–328 · 24 giờ**

| | |
|---|---|
| **Objective cấp module** | Viết một công việc xử lý luồng có trạng thái, đúng theo thời gian sự kiện, phục hồi được sau sự cố, và chứng minh tính đúng bằng thí nghiệm hỏng |
| **Tiền đề** | M29 · M31 |
| **Exit criterion** | Công việc chạy đúng dưới dữ liệu tới muộn, tới sai thứ tự và một lần giết tiến trình, kết quả khớp với bản tính theo lô trên cùng dữ liệu |
| **Kỹ năng SFIA** | `PROG` mức 4 · `HPCC` mức 3 |
| **Chế độ hỏng** | Viết công việc theo thời gian xử lý vì nó chạy được ngay, rồi kết quả đổi mỗi lần chạy lại và không ai đối soát được |

Module dạy **ngữ nghĩa xử lý luồng trước, engine sau**. Bốn khái niệm quyết định tính đúng là thời gian sự kiện, dấu nước, trạng thái và điểm kiểm tra; chúng giống nhau giữa các engine, còn cú pháp thì không. Flink là phương tiện cụ thể ở mức `B` vì nó là engine luồng thuần nên mọi khái niệm lộ ra trực tiếp.

**Ghi chú về thứ tự trong bản đồ.** Bản đồ đặt Spark Structured Streaming ở module này, nhưng Spark chỉ được dạy ở M34, tức sau đây 15 bài. Nên lesson 327 chỉ đối chiếu mô hình lô vi mô ở mức khái niệm và trỏ tới M34 cho phần nội bộ Spark. Nếu muốn dạy Structured Streaming đầy đủ ở đây thì phải đảo M34 lên trước M32.

Ràng buộc kế thừa từ lesson 282: broker vận chuyển, module này biến đổi. Mọi logic nghiệp vụ nhét vào bên tiêu thụ ở M29 lẽ ra thuộc về đây.

### Lesson 317 · Event time against processing time, and why order is not guaranteed `LT`
**Prerequisites.** Module 32: M29 · M31

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Ba mốc thời gian gắn với một sự kiện và ba mốc này gần như không bao giờ trùng: thời điểm việc xảy ra ngoài đời, thời điểm sự kiện được ghi, và thời điểm engine xử lý nó. Vấn đề đã được báo trước ở lesson 279: thứ tự trong hàng đợi là thứ tự tới, không phải thứ tự xảy ra. Bốn nguyên nhân làm sự kiện tới muộn hoặc sai thứ tự, và cả bốn đều bình thường chứ bất thường: thiết bị di động mất mạng rồi gửi bù, phân vùng khác nhau xử lý với tốc độ khác nhau, thử lại theo lesson 278 đẩy một sự kiện ra sau, và đồng hồ giữa các máy lệch nhau. Hệ quả: một công việc tính doanh thu theo giờ mà dùng thời gian xử lý sẽ cho kết quả **khác nhau mỗi lần chạy lại**, nên không đối soát được và không chạy bù được, mất luôn hai tính chất đã đặt làm bắt buộc ở lesson 222. Dùng thời gian sự kiện thì kết quả tái lập được, đổi lại phải quyết định chờ bao lâu, và đó là nội dung lesson 318.

**Outcome.** Chỉ ra trong một công việc cho trước chỗ nào dùng thời gian xử lý, và dự đoán kết quả sai lệch ra sao khi chạy lại trên cùng dữ liệu.

**Đánh giá.** Tầng *phân tích*. Bài mở module, người học đã có kinh nghiệm chạy bù và tính bất biến từ M21, nên đủ nền để thấy vì sao thời gian xử lý phá cả hai. Kiểm bằng ba công việc mẫu; đạt khi định vị đúng cả ba và dự đoán đúng hướng sai lệch.

**Lab.** Chạy một công việc gộp theo cửa sổ giờ dùng thời gian xử lý, trên một tập dữ liệu có 5% sự kiện tới muộn. Chạy ba lần với tốc độ nạp khác nhau và so ba kết quả. Sau đó chạy bản dùng thời gian sự kiện và so lại. Lập bảng chênh lệch theo từng cửa sổ giờ.

**Pitfalls.** Cho rằng dữ liệu của mình không tới muộn vì chưa từng đo · dùng thời gian xử lý vì nó chạy được ngay · so hai kết quả bằng tổng mà không so theo từng cửa sổ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba lần chạy theo thời gian xử lý cho ba kết quả khác nhau có số chứng minh, bản theo thời gian sự kiện cho cùng kết quả qua ba lần.

### Lesson 318 · Watermarks - bounding lateness and choosing the delay `LT`
**Prerequisites.** Lesson 317

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Dùng thời gian sự kiện đặt ra một câu hỏi không có lời giải hoàn hảo: đóng cửa sổ 9 giờ lúc nào, khi luôn có khả năng một sự kiện 9 giờ còn chưa tới. Dấu nước là lời hứa của engine rằng sẽ không còn sự kiện nào cũ hơn mốc này, và nó chỉ là một **ước lượng có chủ ý sai lệch về phía an toàn**. Chọn độ trễ cho phép là chọn một điểm trên đường đánh đổi giữa độ tươi và độ đầy đủ: chờ ngắn thì kết quả ra sớm nhưng thiếu, chờ dài thì đầy đủ nhưng chậm, và không có giá trị đúng phổ quát. Cách chọn có căn cứ thay vì đoán: đo phân bố độ trễ thật của luồng, lấy một phân vị cao làm độ trễ cho phép, rồi định lượng phần trăm sự kiện bị bỏ lại ở mức đó. Dấu nước trong hệ có nhiều phân vùng lấy theo phân vùng chậm nhất, nên một phân vùng không có dữ liệu làm dấu nước đứng yên và cửa sổ không bao giờ đóng, đây là chế độ hỏng tĩnh lặng phổ biến nhất của xử lý luồng.

**Outcome.** Chọn độ trễ cho phép từ phân bố độ trễ đo được của chính luồng, và định lượng phần trăm sự kiện bị bỏ lại ở mức đã chọn.

**Đánh giá.** Tầng *đánh giá*. Objective là chọn một điểm trên đường đánh đổi dựa trên dữ liệu tự đo, cùng phương pháp đã dùng cho prefetch ở lesson 285. Kiểm bằng biểu đồ phân bố cộng bảng ba mức; đạt khi có phân bố thật, có điểm chọn và có con số bị bỏ lại.

**Lab.** Đo phân bố độ trễ trên luồng CDC ở lesson 316 và vẽ biểu đồ. Chạy cùng công việc ở ba mức độ trễ cho phép, với mỗi mức ghi độ tươi kết quả và phần trăm sự kiện bị bỏ. Tạo một phân vùng không có dữ liệu và quan sát dấu nước đứng yên, ghi lại triệu chứng.

**Pitfalls.** Đặt độ trễ cho phép bằng một con số tròn · lấy phân vị 99 rồi mất hết tính kịp thời · không xử lý phân vùng rỗng nên cửa sổ treo vô hạn · kết luận về độ trễ mà chưa đo phân bố.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Biểu đồ phân bố dựng từ dữ liệu thật, bảng ba mức có cả độ tươi lẫn phần trăm bị bỏ, và mô tả đúng triệu chứng khi một phân vùng rỗng.

### Lesson 319 · Windows - tumbling, sliding and session `TH`
**Prerequisites.** Lesson 318

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba loại cửa sổ trả lời ba câu hỏi nghiệp vụ khác nhau, và chọn sai loại là sai câu hỏi chứ sai cài đặt. Cửa sổ cuốn chiếu chia thời gian thành các khoảng rời nhau, dùng cho báo cáo theo kỳ, mỗi sự kiện thuộc đúng một cửa sổ. Cửa sổ trượt chồng lấn nhau, dùng khi cần trung bình trượt hoặc phát hiện ngưỡng liên tục, và mỗi sự kiện thuộc nhiều cửa sổ nên chi phí trạng thái nhân lên theo tỉ lệ chồng lấn. Cửa sổ phiên gom theo khoảng lặng chứ theo mốc thời gian cố định, dùng cho hành vi người dùng, và độ dài mỗi phiên do dữ liệu quyết định nên không đoán trước được chi phí. Ba loại đều đóng theo dấu nước ở lesson 318. Chi phí trạng thái là thứ phải tính trước: số khoá nhân số cửa sổ đang mở nhân kích thước trạng thái mỗi cửa sổ, và cửa sổ trượt với phiên dài là hai cách làm tràn bộ nhớ nhanh nhất.

**Outcome.** Chọn đúng loại cửa sổ cho ba câu hỏi nghiệp vụ và ước lượng trước chi phí trạng thái, rồi đối chiếu ước lượng với số đo thật.

**Đánh giá.** Tầng *áp dụng*. Objective là quyết định thiết kế kèm ước lượng kiểm được bằng đo đạc. Kiểm bằng ba cài đặt cộng bảng so ước lượng với thực đo; đạt khi cả ba chọn đúng loại và ước lượng cùng bậc độ lớn với số đo.

**Lab.** Cài đặt ba công việc: doanh thu theo giờ, số đơn trong 15 phút gần nhất cập nhật mỗi phút, và độ dài phiên mua sắm. Với mỗi công việc, ước lượng chi phí trạng thái trước khi chạy, rồi đo bộ nhớ trạng thái thật. Lập bảng so ước lượng với thực đo và giải thích chỗ lệch.

**Pitfalls.** Dùng cửa sổ trượt cho báo cáo theo kỳ rồi đếm trùng · đặt cửa sổ phiên với khoảng lặng quá dài nên phiên không bao giờ đóng · không ước lượng trạng thái trước rồi tràn bộ nhớ trong sản xuất.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba công việc chọn đúng loại cửa sổ, và ước lượng trạng thái cùng bậc độ lớn với số đo thật ở ít nhất hai trong ba.

### Lesson 320 · State in a streaming job and where it is kept `LT`
**Prerequisites.** Lesson 319

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Công việc không trạng thái xử lý từng sự kiện độc lập và khởi động lại không mất gì; công việc có trạng thái nhớ thứ đã thấy, nên mọi câu hỏi về tính đúng đều quy về câu hỏi trạng thái sống ở đâu và sống sót ra sao. Ba loại trạng thái và cách chúng lớn lên: trạng thái theo khoá lớn theo số khoá riêng biệt, trạng thái cửa sổ lớn theo lesson 319, và trạng thái toán tử cho việc như theo dõi vị trí đọc. Nơi giữ trạng thái quyết định trần quy mô: giữ trong bộ nhớ thì nhanh nhưng bị giới hạn bởi RAM một nút, giữ trong kho nhúng trên đĩa cục bộ thì vượt RAM được và đổi lấy độ trễ cao hơn. Trạng thái không bao giờ được phép lớn vô hạn, nên mọi trạng thái theo khoá phải có chính sách hết hạn; thiếu chính sách đó là cách công việc chạy tốt sáu tuần rồi chết. Trạng thái là thứ làm việc mở rộng quy mô trở nên khó: thêm nút không chỉ chia việc mà phải chia lại trạng thái theo khoá, cùng vấn đề đã gặp khi tăng phân vùng ở lesson 293.

**Outcome.** Phân loại trạng thái trong một công việc cho trước và dự đoán nó lớn lên theo đại lượng nào, kèm chính sách hết hạn phù hợp.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết chuẩn bị cho hai bài thực hành tiếp theo; chưa đòi cài đặt phục hồi. Kiểm bằng bài phân tích bốn công việc mẫu; đạt khi phân loại đúng ít nhất ba và nêu đúng đại lượng làm trạng thái lớn lên.

**Lab.** Cho bốn công việc mẫu. Với mỗi công việc, phân loại trạng thái, viết công thức ước lượng kích thước theo đại lượng nghiệp vụ, và đề xuất chính sách hết hạn. Chạy một công việc không có chính sách hết hạn với dữ liệu khoá tăng dần và vẽ đồ thị trạng thái lớn theo thời gian.

**Pitfalls.** Cho rằng trạng thái nhỏ vì hiện tại nó nhỏ · dùng bộ nhớ làm nơi giữ trạng thái cho khoá không giới hạn · quên rằng thêm nút phải chia lại trạng thái.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân loại đúng ≥ 3/4 công việc kèm công thức ước lượng, và đồ thị cho thấy trạng thái không hết hạn lớn tuyến tính theo số khoá.

### Lesson 321 · Checkpointing, savepoints and recovery `TH`
**Prerequisites.** Lesson 320

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Điểm kiểm tra là ảnh chụp nhất quán của toàn bộ trạng thái cộng vị trí đọc ở nguồn, chụp định kỳ và tự động, để khi công việc chết thì khởi động lại từ ảnh chụp gần nhất chứ từ đầu. Chi tiết quyết định tính đúng: ảnh chụp phải gồm **cả trạng thái lẫn vị trí đọc trong cùng một lần chụp**, nếu tách rời thì khôi phục xong sẽ hoặc bỏ sót hoặc xử lý lại một đoạn, cùng lập luận đã dùng cho offset và kết quả ở lesson 295. Cơ chế chụp mà không dừng dòng dữ liệu dùng dấu mốc đi theo luồng, và engine chờ mọi đầu vào của một toán tử cùng thấy dấu mốc trước khi chụp phần của mình. Chu kỳ chụp là một đánh đổi đo được: chụp dày thì mất ít việc khi hỏng nhưng tốn thông lượng; chụp thưa thì ngược lại. Điểm lưu là ảnh chụp do người chủ động tạo, dùng khi nâng cấp mã hoặc đổi cấu hình, và đây là cơ chế cho phép sửa công việc mà không mất trạng thái. Khi nào trạng thái cũ không tương thích với mã mới.

**Outcome.** Khôi phục được công việc từ điểm kiểm tra sau khi giết tiến trình và chứng minh kết quả không thiếu không trùng, cùng bảng đánh đổi chu kỳ chụp.

**Đánh giá.** Tầng *áp dụng*. Objective là một thao tác vận hành kiểm được bằng đối soát, đúng phương pháp thí nghiệm hỏng đã dùng ở lesson 298. Kiểm bằng ba lần giết tiến trình; đạt khi cả ba lần đối soát khớp tuyệt đối.

**Lab.** Bật điểm kiểm tra cho công việc gộp theo cửa sổ. Giết tiến trình ba lần ở ba thời điểm khác nhau trong một cửa sổ, mỗi lần khôi phục rồi đối soát kết quả với bản chạy không bị ngắt. Chạy ở ba chu kỳ chụp và đo thông lượng cùng thời gian khôi phục. Tạo một điểm lưu, sửa logic công việc, khởi động lại từ điểm lưu đó.

**Pitfalls.** Chụp trạng thái mà không chụp vị trí đọc · đặt chu kỳ chụp rất dày rồi thắc mắc vì sao thông lượng thấp · khởi động lại từ đầu vì thấy nhanh hơn · đổi mã rồi khôi phục từ điểm lưu cũ mà không xét tương thích.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba lần giết tiến trình đều khôi phục và đối soát khớp tuyệt đối, bảng ba chu kỳ chụp có cả thông lượng lẫn thời gian khôi phục, và nâng cấp qua điểm lưu giữ nguyên trạng thái.

### Lesson 322 · Exactly-once in a streaming job - two-phase commit at the sink `TH`
**Prerequisites.** Lesson 321

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Điểm kiểm tra cho đúng một lần **trong phạm vi engine**: khôi phục thì trạng thái nội bộ trở về nhất quán. Nhưng dữ liệu đã ghi ra đích thì không rút lại được, nên đúng một lần đầu cuối chỉ đạt khi đích hợp tác, đúng kết luận đã rút hai lần ở lesson 278 và 301. Ba loại đích và ba cách xử lý: đích hỗ trợ giao dịch thì dùng chốt hai pha, engine ghi trong giao dịch và chỉ chốt khi điểm kiểm tra hoàn tất; đích hỗ trợ ghi bất biến theo khoá thì ghi lại cho cùng kết quả nên không cần giao dịch, đây là cách rẻ và bền nhất theo lesson 106; đích không hỗ trợ gì thì chỉ đạt được ít nhất một lần và phải khử trùng ở tầng sau. Cái giá của chốt hai pha: dữ liệu chỉ nhìn thấy được sau khi chốt, nên độ trễ đầu cuối bị neo vào chu kỳ điểm kiểm tra ở lesson 321, và đây là điều bất ngờ với nhiều đội. Cách chọn giữa ba cách, và vì sao ghi bất biến thường là câu trả lời đúng.

**Outcome.** Chọn đúng cơ chế cho một đích cho trước và chứng minh bằng thí nghiệm hỏng rằng kết quả không trùng không thiếu.

**Đánh giá.** Tầng *đánh giá*. Objective đòi phán đoán về ranh giới giữa engine và đích, chỗ tài liệu hay gây hiểu nhầm. Kiểm bằng ba đích khác loại cộng thí nghiệm hỏng; đạt khi chọn đúng cả ba và hai đích có bảo đảm đều qua được thí nghiệm.

**Lab.** Cài cùng công việc ghi ra ba đích: một cơ sở dữ liệu có giao dịch, một bảng có khoá nghiệp vụ cho phép ghi bất biến, và một tệp nối thêm. Với mỗi đích, giết tiến trình giữa chừng ba lần và đếm trùng cùng thiếu. Đo độ trễ đầu cuối ở cấu hình chốt hai pha và so với cấu hình ghi bất biến.

**Pitfalls.** Bật đúng một lần ở engine rồi tưởng đích cũng đúng một lần · dùng chốt hai pha cho đích không hỗ trợ · không lường độ trễ bị neo vào chu kỳ chụp · ghi tệp nối thêm rồi khẳng định không trùng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Hai đích có bảo đảm cho 0 trùng 0 thiếu qua ba lần giết, đích thứ ba định lượng được mức trùng, và có số đo độ trễ của hai cấu hình.

### Lesson 323 · Stream-to-stream joins and the buffer they require `TH`
**Prerequisites.** Lesson 322

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Kết hai luồng khác hẳn kết hai bảng: bảng đứng yên còn luồng thì không bao giờ kết thúc, nên phải trả lời câu hỏi chờ bao lâu cho bên kia tới. Kết theo khoảng thời gian là dạng dùng được: một sự kiện bên trái khớp với sự kiện bên phải cùng khoá trong một khoảng thời gian cho trước quanh nó. Khoảng đó quyết định trực tiếp hai thứ: tỉ lệ khớp được và lượng trạng thái phải giữ, vì engine buộc phải đệm mọi sự kiện chưa hết khoảng. Ước lượng trạng thái trước khi chạy: tốc độ sự kiện nhân độ dài khoảng nhân kích thước bản ghi, nhân đôi cho hai bên. Ba chế độ hỏng đặc trưng: khoảng quá hẹp thì mất phần lớn cặp khớp mà không báo lỗi gì, khoảng quá rộng thì trạng thái tràn, và một bên ngừng gửi thì dấu nước đứng lại theo lesson 318 nên không cặp nào được phát ra. Kết ngoài trong luồng chỉ phát được sau khi hết khoảng chờ, nên kết quả ra muộn hơn kết trong, điều này phải nói rõ với bên dùng.

**Outcome.** Chọn khoảng thời gian kết từ phân bố độ lệch đo được, ước lượng trạng thái trước, và định lượng tỉ lệ cặp bị mất ở khoảng đã chọn.

**Đánh giá.** Tầng *áp dụng*. Objective là quyết định thiết kế có hai hệ quả đo được, nối tiếp phương pháp chọn dấu nước ở lesson 318. Kiểm bằng ba mức khoảng; đạt khi có phân bố thật, ước lượng trạng thái cùng bậc với số đo, và tỉ lệ mất được định lượng.

**Lab.** Kết luồng đơn hàng với luồng thanh toán. Đo phân bố độ lệch thời gian giữa hai sự kiện cùng đơn. Chạy ở ba mức khoảng, mỗi mức đo tỉ lệ khớp, bộ nhớ trạng thái và độ trễ kết quả. Ngừng luồng thanh toán 5 phút và ghi lại hành vi của công việc.

**Pitfalls.** Đặt khoảng theo cảm tính · không đo phân bố độ lệch · coi cặp không khớp là lỗi dữ liệu trong khi là do khoảng hẹp · quên rằng kết ngoài phát muộn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng ba mức khoảng đủ ba đại lượng, ước lượng trạng thái cùng bậc với số đo, và mô tả đúng hành vi khi một luồng ngừng.

### Lesson 324 · Stream-to-table joins and the temporal correctness trap `TH`
**Prerequisites.** Lesson 323

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Làm giàu một luồng bằng dữ liệu tham chiếu là việc thường gặp nhất trong xử lý luồng, và cũng là chỗ sai âm thầm nhiều nhất. Cách ngây thơ là tra cứu bảng tham chiếu ở trạng thái hiện tại, và nó cho kết quả **không tái lập được**: chạy lại một tháng sau thì đơn hàng cũ được gắn giá hiện tại chứ giá lúc đó, nên chạy bù cho ra số khác lần chạy đầu, phá đúng tính chất đã đặt bắt buộc ở lesson 222. Cách đúng là kết theo thời điểm: dùng bản tham chiếu có hiệu lực tại thời điểm sự kiện, và điều này đòi bảng tham chiếu phải có lịch sử, tức là một bảng loại 2 như đã dựng từ CDC ở lesson 314. Ba cách nạp bảng tham chiếu vào công việc và đánh đổi: nạp toàn bộ vào bộ nhớ thì nhanh nhưng giới hạn kích thước và phải làm mới; tra cứu ngoài mỗi sự kiện thì luôn mới nhưng chậm và tạo tải lên hệ khác; nhận bảng dưới dạng luồng thay đổi thì đúng và tự cập nhật, và đây là chỗ M31 trả cổ tức.

**Outcome.** Cài đặt kết theo thời điểm dùng luồng thay đổi, và chứng minh bằng chạy bù rằng kết quả tái lập được.

**Đánh giá.** Tầng *sáng tạo*. Bài đòi ghép luồng CDC, bảng lịch sử và ngữ nghĩa thời gian sự kiện thành một thiết kế; cao hơn tầng áp dụng. Kiểm bằng phép chạy bù so hai lần; đạt khi hai lần chạy cách nhau cho kết quả khớp tuyệt đối.

**Lab.** Làm giàu luồng đơn hàng bằng bảng giá sản phẩm. Cài bản ngây thơ tra giá hiện tại và bản kết theo thời điểm dùng bảng loại 2 từ lesson 314. Đổi giá 20 sản phẩm. Chạy bù cùng khoảng dữ liệu trên cả hai bản và so kết quả với bản tính theo lô làm chuẩn.

**Pitfalls.** Tra cứu trạng thái hiện tại rồi chạy bù ra số khác · dùng bảng tham chiếu không có lịch sử · tra cứu ngoài mỗi sự kiện rồi làm nghẽn hệ nguồn · không so với bản theo lô làm chuẩn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bản kết theo thời điểm cho kết quả khớp tuyệt đối với bản theo lô ở cả hai lần chạy bù, bản ngây thơ định lượng được mức lệch.

### Lesson 325 · Late data - drop, side output or update the result `TH`
**Prerequisites.** Lesson 324

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Dấu nước ở lesson 318 đã đóng cửa sổ thì sự kiện tới sau đó phải đi đâu, và ba lựa chọn cho ba hệ quả nghiệp vụ khác nhau. Bỏ là mặc định của nhiều engine và là lựa chọn nguy hiểm nhất vì nó im lặng: số cuối thiếu mà không ai biết thiếu bao nhiêu. Đưa ra luồng phụ giữ lại sự kiện muộn để đếm, cảnh báo và đối soát, và đây là mức tối thiểu cho hệ có đối soát tài chính. Cập nhật lại kết quả cho số đúng nhất nhưng buộc đích phải chịu được ghi đè và buộc bên dùng chấp nhận số đã công bố có thể đổi, nên phải thoả thuận trước chứ quyết định một mình. Độ trễ cho phép sau dấu nước là tham số riêng, khác với độ trễ của dấu nước, và nhiều người nhầm hai cái. Nối với chất lượng dữ liệu ở M20: tỉ lệ sự kiện muộn là một chỉ số chất lượng phải theo dõi và đặt ngưỡng, cùng loại với các chiều ở lesson 211.

**Outcome.** Chọn đúng cách xử lý dữ liệu muộn theo yêu cầu nghiệp vụ, cài đặt được, và đo tỉ lệ sự kiện muộn để đặt ngưỡng cảnh báo.

**Đánh giá.** Tầng *đánh giá*. Objective đòi cân giữa độ chính xác và tính ổn định của số đã công bố, một quyết định có bên liên quan chứ thuần kỹ thuật. Kiểm bằng ba yêu cầu nghiệp vụ cộng cài đặt; đạt khi chọn đúng cả ba và có số đo tỉ lệ muộn.

**Lab.** Cài cả ba cách trên cùng công việc. Với dữ liệu có 5% sự kiện muộn, đo sai lệch kết quả của cách bỏ so với cách cập nhật. Đếm sự kiện ra luồng phụ và đặt cảnh báo theo tỉ lệ. Cho ba yêu cầu nghiệp vụ gồm báo cáo tài chính, bảng theo dõi vận hành và cảnh báo gian lận; chọn cách cho từng yêu cầu và nêu lý do.

**Pitfalls.** Để mặc định bỏ rồi không biết mất bao nhiêu · cập nhật lại số đã công bố mà không báo bên dùng · nhầm độ trễ cho phép với độ trễ dấu nước · không theo dõi tỉ lệ muộn như một chỉ số chất lượng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba cách chạy được, sai lệch của cách bỏ được định lượng, và ba yêu cầu nghiệp vụ được gán đúng cách kèm lý do.

### Lesson 326 · Backpressure, throughput and diagnosing a slow operator `TH`
**Prerequisites.** Lesson 325

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Áp lực ngược trong engine luồng là cơ chế tự bảo vệ: toán tử chậm làm toán tử trước nó chậm theo, lan ngược tới nguồn, và hệ giảm tốc thay vì tràn bộ nhớ. Đây là hành vi đúng, nên nhìn thấy áp lực ngược không phải sự cố mà là **triệu chứng chỉ đường tới nút thắt**. Quy trình chẩn đoán: tìm toán tử đầu tiên tính từ cuối luồng mà không bị áp lực ngược, đó chính là nút thắt, vì mọi thứ trước nó đều đang chờ nó. Bốn nguyên nhân thường gặp ở nút thắt và cách phân biệt bằng số đo: tra cứu ngoài đồng bộ theo lesson 324, trạng thái quá lớn làm mỗi lần truy cập tốn đĩa, lệch dữ liệu theo khoá đúng hiện tượng sẽ gặp lại ở lesson 349, và tuần tự hoá đắt. Phân biệt độ trễ với thông lượng: tăng mức song song làm thông lượng tăng nhưng có thể không làm độ trễ giảm, và với khoá lệch thì tăng song song gần như không giúp gì. Quan hệ với độ trễ tiêu thụ ở lesson 300: độ trễ tăng là dấu hiệu, áp lực ngược chỉ ra chỗ.

**Outcome.** Định vị toán tử nút thắt trong một công việc chậm bằng chỉ báo áp lực ngược, và quy nó về đúng một trong bốn nguyên nhân bằng số đo.

**Đánh giá.** Tầng *phân tích*. Bài vận hành, đòi truy ngược từ triệu chứng toàn cục về một thành phần cụ thể. Kiểm bằng ba công việc chậm tiêm sẵn tính giờ; đạt khi định vị đúng ít nhất hai nút thắt và quy đúng nguyên nhân.

**Lab.** Giảng viên đưa ba công việc chạy chậm, mỗi công việc một nguyên nhân khác nhau, mỗi lần 12 phút. Với mỗi công việc, đọc chỉ báo áp lực ngược, định vị nút thắt, nêu nguyên nhân kèm số đo, và sửa. Đo thông lượng trước và sau. Với công việc khoá lệch, tăng mức song song gấp đôi và chứng minh thông lượng gần như không đổi.

**Pitfalls.** Tăng tài nguyên toàn cục thay vì tìm nút thắt · coi áp lực ngược là lỗi cần tắt · kết luận nút thắt từ đồ thị CPU · tăng song song cho công việc lệch khoá rồi tưởng đã giải quyết.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Định vị đúng ≥ 2/3 nút thắt kèm nguyên nhân có số đo, và chứng minh được tăng song song không cứu được trường hợp lệch khoá.

### Lesson 327 · Spark Structured Streaming - the micro-batch model compared `TH`
**Prerequisites.** Lesson 326

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài đối chiếu hai mô hình thực thi, không phải bài dạy Spark; phần nội bộ Spark nằm ở M34 và bài này chỉ dùng mức đủ để chạy một công việc tương đương. Mô hình luồng thuần xử lý từng sự kiện khi nó tới; mô hình lô vi mô gom sự kiện thành lô nhỏ rồi chạy như một công việc theo lô, và mọi khác biệt về độ trễ suy ra từ đó. Điều quan trọng cần thấy: **bốn khái niệm ở lesson 317 tới 322 giữ nguyên ý nghĩa ở cả hai mô hình**, chỉ đổi cách hiện thực, nên học ngữ nghĩa trước là đúng thứ tự. Bảng đối chiếu bốn điểm: thời gian sự kiện và dấu nước có ở cả hai; cửa sổ có ở cả hai; trạng thái và điểm kiểm tra có ở cả hai với cơ chế khác nhau; độ trễ sàn thì khác hẳn vì lô vi mô bị neo vào chu kỳ lô. Ba tình huống lô vi mô là lựa chọn hợp lý: đội đã vận hành Spark cho phần theo lô nên dùng chung một engine, yêu cầu độ trễ tính bằng giây chứ mili giây, và cùng một mã dùng được cho cả lô lẫn luồng.

**Outcome.** Cài lại một công việc đã viết sang mô hình lô vi mô và đối chiếu bốn điểm, kèm số đo độ trễ sàn của cả hai.

**Đánh giá.** Tầng *phân tích*. Objective là quy khác biệt quan sát được về khác biệt mô hình thực thi chứ về tên sản phẩm. Kiểm bằng bảng đối chiếu bốn điểm cộng số đo; đạt khi kết quả nghiệp vụ hai bản khớp nhau và chênh lệch độ trễ được giải thích bằng cơ chế lô.

**Lab.** Cài lại công việc gộp theo cửa sổ ở lesson 319 bằng Structured Streaming. Chạy song song hai bản trên cùng dữ liệu và chứng minh kết quả nghiệp vụ khớp nhau. Đo độ trễ đầu cuối phân vị 95 của cả hai ở ba chu kỳ lô. Lập bảng đối chiếu bốn điểm.

**Pitfalls.** Kết luận engine này nhanh hơn engine kia mà không nêu yêu cầu độ trễ · so hai bản ở hai cấu hình khác nhau · học cú pháp mà bỏ qua chỗ bốn khái niệm ánh xạ sang · đi sâu vào nội bộ Spark ở bài này thay vì chờ M34.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Kết quả nghiệp vụ hai bản khớp tuyệt đối, bảng đối chiếu đủ bốn điểm, và chênh lệch độ trễ sàn có số kèm giải thích bằng chu kỳ lô.

### Lesson 328 · Gate 7 - a stateful job that survives late data, disorder and a kill `KT`
**Prerequisites.** Lesson 327

**In-class (120 phút).** 75 phút làm bài độc lập · 45 phút chữa bài và phân tích lỗi theo nhóm

**Learn.** Cổng của chặng 6. Bài kiểm toàn bộ khối từ M27 tới M32: bản thân việc chọn broker, cách đưa dữ liệu vào bằng CDC, và tính đúng của công việc xử lý luồng dưới các điều kiện thực tế. Không có nội dung mới.

**Outcome.** Nộp một công việc xử lý luồng có trạng thái chạy đúng dưới dữ liệu muộn, dữ liệu sai thứ tự và một lần giết tiến trình, với kết quả khớp bản tính theo lô.

**Đánh giá.** Tầng *đánh giá*. Cổng đo năng lực dựng hệ đúng dưới điều kiện hỏng chứ đo trí nhớ về API; hình thức là bài làm có đối soát và có chất vấn.

**Lab.** Nhận một luồng sự kiện có 7% tới muộn và 3% sai thứ tự, kèm bản tính theo lô làm chuẩn. Bài chấm năm phần: A (25đ) công việc dùng thời gian sự kiện, độ trễ dấu nước chọn từ phân bố đo được · B (25đ) kết quả khớp bản chuẩn trong sai số cho trước, sự kiện muộn được đếm chứ bỏ im lặng · C (20đ) giết tiến trình giữa chừng, khôi phục từ điểm kiểm tra, đối soát khớp tuyệt đối · D (20đ) định vị nút thắt trong một công việc chậm cho sẵn và sửa · E (10đ) nêu một tình huống nên dùng xử lý theo lô thay vì luồng, kèm lý do.

**Pitfalls.** Dùng thời gian xử lý cho nhanh rồi không đối soát được · để mặc định bỏ dữ liệu muộn · bỏ phần E vì hết giờ · nộp công việc chưa từng bị giết tiến trình lần nào.

**Self-study (2,4 giờ).** Không có bài tự học. Nếu không đạt, theo phụ lục khắc phục khi không đạt cổng

**Done when.** Đạt ≥ 70/100, phần B và C đều ≥ 60%. Không đạt thì làm lại phần đo ở M32 rồi bảo vệ lại.

# MODULE 33 · STORAGE, FILE FORMATS AND THE LAKEHOUSE

**Lessons 329–342 · 28 giờ**

| | |
|---|---|
| **Objective cấp module** | Chọn định dạng tệp, cách phân vùng và định dạng bảng cho một khối lượng truy vấn cho trước, và chứng minh lựa chọn bằng lượng dữ liệu thực sự được quét |
| **Tiền đề** | M32 |
| **Exit criterion** | Cùng một tập dữ liệu ở ba cách bố trí, đo được lượng byte quét và thời gian truy vấn của từng cách, và giải thích chênh lệch bằng cơ chế chứ bằng tên định dạng |
| **Kỹ năng SFIA** | `DATM` mức 4 · `HPCC` mức 3 |
| **Chế độ hỏng** | Chọn định dạng theo lời khuyên trên mạng, phân vùng theo cột có số giá trị phân biệt rất cao, rồi sinh hàng triệu tệp nhỏ và làm mọi truy vấn chậm đi |

Module trả lời một câu hỏi duy nhất ở nhiều tầng: **truy vấn này thực sự đọc bao nhiêu byte từ đĩa, và vì sao**. Định dạng tệp, cách nén, cách phân vùng và định dạng bảng đều là bốn cách trả lời khác nhau cho câu đó.

Mọi bài đo bằng cùng một đại lượng là số byte quét, nên các con số so được với nhau xuyên suốt module và dùng lại được ở M34 khi Spark đọc chính những tệp này.

### Lesson 329 · Three storage models - block, file and object `LT`
**Prerequisites.** Module 33: M32

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Ba mô hình lưu trữ với ba giao diện khác nhau, và chọn sai mô hình là sai ở tầng kiến trúc chứ ở tầng cấu hình. Lưu trữ khối đưa ra một dãy khối thô, hệ tệp hoặc cơ sở dữ liệu tự quản lý cấu trúc bên trên, độ trễ thấp nhất, gắn vào đúng một máy. Lưu trữ tệp đưa ra cây thư mục dùng chung qua mạng, tiện nhưng khó mở rộng. Lưu trữ đối tượng đưa ra một khoá phẳng trỏ tới một khối byte kèm siêu dữ liệu, mở rộng gần như không giới hạn, rẻ nhất trên mỗi đơn vị dung lượng, và đây là nền của mọi hồ dữ liệu. Bốn thuộc tính của lưu trữ đối tượng quyết định thiết kế phía trên nó: ghi là thay cả đối tượng chứ sửa tại chỗ, không có thao tác đổi tên thật, liệt kê thư mục tốn kém vì thư mục chỉ là tiền tố của khoá, và độ trễ mỗi yêu cầu cao hơn đĩa cục bộ hàng trăm lần. Nối lại chênh lệch đọc tuần tự và ngẫu nhiên ở M2: trên lưu trữ đối tượng, đọc một khối lớn rẻ hơn nhiều so với đọc nhiều khối nhỏ.

**Outcome.** Chọn mô hình lưu trữ cho ba khối lượng công việc cho trước và nêu thuộc tính nào của mô hình quyết định lựa chọn.

**Đánh giá.** Tầng *hiểu*. Bài mở module, nối kiến thức lưu trữ vật lý ở M2 với ba giao diện thực tế. Kiểm bằng ba khối lượng công việc; đạt khi chọn đúng cả ba và mỗi lần dẫn một thuộc tính cụ thể chứ một nhận xét chung.

**Lab.** Đo độ trễ và thông lượng của cùng một thao tác đọc 1 GB trên đĩa cục bộ và trên lưu trữ đối tượng, ở hai cách: một tệp lớn và một nghìn tệp nhỏ. Lập bảng bốn ô. Chọn mô hình cho ba khối lượng công việc gồm cơ sở dữ liệu giao dịch, kho tệp chia sẻ cho đội, và hồ dữ liệu phân tích.

**Pitfalls.** Coi lưu trữ đối tượng như một hệ tệp bình thường · giả định đổi tên là thao tác rẻ · thiết kế cho nhiều tệp nhỏ vì trên máy cục bộ thấy không sao.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng bốn ô có số đo thật, và ba khối lượng công việc được gán đúng mô hình kèm thuộc tính quyết định.

### Lesson 330 · Object storage semantics and what they break `LT`
**Prerequisites.** Lesson 329

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bốn thuộc tính ở lesson 329 phá vỡ ba giả định mà mã xử lý dữ liệu thường mang theo từ hệ tệp. Một là ghi tạm rồi đổi tên: mẫu phổ biến để công bố nguyên tử ở lesson 207 không dùng được vì đổi tên thực chất là sao chép rồi xoá, tốn thời gian tỉ lệ với kích thước và không nguyên tử. Hai là liệt kê để biết có gì: liệt kê một tiền tố có hàng triệu khoá tốn nhiều yêu cầu và có thể không phản ánh ngay thứ vừa ghi. Ba là sửa một phần tệp: không có, muốn đổi một dòng phải ghi lại cả đối tượng. Hệ quả trực tiếp: một công việc ghi nhiều tệp ra hồ dữ liệu rồi công bố bằng cách đổi tên thư mục sẽ **để lại trạng thái nửa chừng** nếu chết giữa chừng, và người đọc thấy bảng sai mà không có lỗi nào. Đây chính là bài toán sẽ dẫn tới định dạng bảng mở ở lesson 337. Ba cách sống chung trước khi có định dạng bảng: ghi vào thư mục tạm rồi ghi một tệp đánh dấu hoàn tất, dùng phân vùng theo ngày và chỉ công bố nguyên phân vùng, và giữ một sổ kê bên ngoài.

**Outcome.** Chỉ ra trong một quy trình ghi cho trước chỗ nào giả định sai về ngữ nghĩa lưu trữ đối tượng, và nêu hậu quả quan sát được.

**Đánh giá.** Tầng *phân tích*. Objective là truy một lỗi tiềm ẩn từ giả định sai tới biểu hiện thực tế, chuẩn bị nền cho lesson 337. Kiểm bằng ba quy trình ghi; đạt khi chỉ đúng ít nhất hai chỗ và mô tả đúng trạng thái nửa chừng.

**Lab.** Viết một công việc ghi 200 tệp ra lưu trữ đối tượng rồi công bố bằng cách đổi tên tiền tố. Giết tiến trình giữa chừng và quan sát trạng thái người đọc nhìn thấy. Đo thời gian đổi tên một tiền tố 10 GB. Cài lại bằng tệp đánh dấu hoàn tất và lặp lại thí nghiệm giết tiến trình.

**Pitfalls.** Dùng lại mẫu ghi tạm rồi đổi tên của hệ tệp · tin rằng liệt kê luôn thấy ngay tệp vừa ghi · sửa một dòng bằng cách đọc, sửa, ghi đè mà không khoá.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Thí nghiệm cho thấy trạng thái nửa chừng ở bản đổi tên, bản có tệp đánh dấu không có trạng thái đó, và có số đo thời gian đổi tên.

### Lesson 331 · Row against columnar layout and why analytics reads columns `LT`
**Prerequisites.** Lesson 330

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Cùng một bảng, hai cách xếp byte trên đĩa, và mọi khác biệt hiệu năng phân tích suy ra từ đó. Bố trí theo dòng gom mọi cột của một bản ghi cạnh nhau, tốt khi đọc hoặc ghi cả bản ghi, đây là cách cơ sở dữ liệu giao dịch làm và đã gặp ở M10. Bố trí theo cột gom mọi giá trị của một cột cạnh nhau, nên truy vấn chỉ dùng ba cột trong bốn mươi cột chỉ phải đọc ba, và tỉ lệ tiết kiệm bằng đúng tỉ lệ cột bỏ qua. Lợi ích thứ hai lớn không kém: giá trị cùng cột cùng kiểu và thường lặp nhiều, nên nén tốt hơn hẳn, và ít byte hơn nghĩa là ít thời gian đọc hơn. Cái giá: ghi thêm một bản ghi phải chạm vào nhiều chỗ, và đọc nguyên một bản ghi phải ghép từ nhiều nơi, nên bố trí theo cột dở cho khối lượng công việc giao dịch. Quy tắc thực dụng rút ra: kho phân tích dùng cột, hệ vận hành dùng dòng, và đây là lý do kỹ thuật cho việc tách hai hệ đã nêu ở lesson 172.

**Outcome.** Dự đoán tỉ lệ byte tiết kiệm được khi chuyển một truy vấn cho trước từ bố trí dòng sang cột, rồi đối chiếu dự đoán với số đo.

**Đánh giá.** Tầng *áp dụng*. Objective là một dự đoán định lượng kiểm được ngay bằng thực nghiệm. Kiểm bằng ba truy vấn; đạt khi dự đoán cùng bậc với số đo ở ít nhất hai trong ba.

**Lab.** Lưu cùng một bảng 40 cột ở hai định dạng dòng và cột. Với ba truy vấn dùng lần lượt 2, 8 và 40 cột, viết dự đoán tỉ lệ byte đọc trước, rồi đo thật. Lập bảng dự đoán và thực đo. Đo thêm kích thước tệp của hai định dạng.

**Pitfalls.** Cho rằng bố trí cột luôn nhanh hơn kể cả khi đọc mọi cột · so hai định dạng ở hai mức nén khác nhau · đo thời gian mà quên đo byte đọc.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng ba truy vấn có cả dự đoán lẫn thực đo, và dự đoán cùng bậc với thực đo ở ≥ 2/3 trường hợp.

### Lesson 332 · Parquet internals - row groups, column chunks, pages and statistics `TH`
**Prerequisites.** Lesson 331

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Parquet không phải một khối byte phẳng mà là một cấu trúc phân tầng, và biết cấu trúc đó là điều kiện để giải thích mọi số đo ở ba bài sau. Tệp chia thành nhóm dòng; trong mỗi nhóm dòng, mỗi cột là một đoạn cột; mỗi đoạn cột chia thành trang, là đơn vị nén và đọc nhỏ nhất. Chân tệp chứa siêu dữ liệu: lược đồ, vị trí từng đoạn, và **thống kê giá trị nhỏ nhất, lớn nhất, số rỗng cho từng đoạn**. Thống kê này là thứ cho phép bỏ qua cả nhóm dòng mà không đọc, và đó là cơ chế thật đứng sau việc đẩy điều kiện lọc xuống ở lesson 334. Kích thước nhóm dòng là đánh đổi: nhóm lớn thì nén tốt và ít siêu dữ liệu nhưng đơn vị bỏ qua thô, nhóm nhỏ thì lọc mịn hơn nhưng chi phí siêu dữ liệu tăng. Cách đọc chân tệp bằng công cụ dòng lệnh để tự kiểm chứng mọi khẳng định trên, thay vì tin vào tài liệu.

**Outcome.** Đọc được chân tệp Parquet và chỉ ra số nhóm dòng, kích thước từng đoạn cột và thống kê của cột dùng để lọc.

**Đánh giá.** Tầng *áp dụng*. Objective là một kỹ năng khảo sát cụ thể, điều kiện cần cho ba bài sau. Kiểm bằng bài đọc tệp có đáp án; đạt khi trả lời đúng ít nhất 5/6 câu về cấu trúc tệp.

**Lab.** Ghi cùng dữ liệu ra Parquet ở ba kích thước nhóm dòng. Với mỗi tệp, đọc chân tệp và ghi lại số nhóm dòng, kích thước mỗi đoạn cột, và thống kê của cột ngày. Trả lời sáu câu hỏi về cấu trúc. Sắp xếp dữ liệu theo cột ngày rồi ghi lại và so thống kê trước sau.

**Pitfalls.** Coi Parquet là hộp đen · đặt kích thước nhóm dòng mặc định mà không xét kích thước tệp · ghi dữ liệu chưa sắp xếp rồi thắc mắc vì sao thống kê không giúp lọc.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Trả lời đúng ≥ 5/6 câu, và chỉ ra được thống kê cột ngày hẹp lại rõ rệt sau khi sắp xếp.

### Lesson 333 · Compression and encoding - dictionary, run-length and the CPU trade `TH`
**Prerequisites.** Lesson 332

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hai tầng thu gọn dữ liệu và nhiều người gộp chúng làm một. Mã hoá khai thác cấu trúc của dữ liệu: từ điển thay giá trị lặp bằng chỉ số, mã hoá độ dài chuỗi lặp thay dãy giá trị giống nhau bằng cặp giá trị và số lần, mã hoá theo độ lệch cho số tăng dần. Nén là bước sau, áp lên byte đã mã hoá, và bốn thuật toán phổ biến trải trên đường đánh đổi giữa tỉ lệ nén và chi phí CPU khi giải nén. Điều quan trọng thực tế: mã hoá từ điển hiệu quả tới mức cột có ít giá trị phân biệt gần như miễn phí về dung lượng, nên **sắp xếp dữ liệu theo cột có ít giá trị phân biệt trước khi ghi** làm cả mã hoá lẫn nén tốt lên rõ rệt. Chọn thuật toán nén là chọn theo khối lượng công việc: dữ liệu đọc nhiều lần thì ưu tiên giải nén nhanh, dữ liệu lưu trữ lâu ít đọc thì ưu tiên tỉ lệ nén. Đo chứ đoán, và đo cả CPU chứ chỉ dung lượng.

**Outcome.** Chọn thuật toán nén và thứ tự sắp xếp cho một khối lượng công việc, dẫn bằng bảng đo dung lượng, thời gian đọc và CPU.

**Đánh giá.** Tầng *đánh giá*. Objective là chọn một điểm trên đường đánh đổi ba chiều từ số đo của chính mình. Kiểm bằng bảng ít nhất ba thuật toán nhân hai thứ tự sắp xếp; đạt khi có đủ ba đại lượng và lý do chọn dẫn số.

**Lab.** Ghi cùng dữ liệu với ba thuật toán nén, mỗi thuật toán ở hai trạng thái là chưa sắp xếp và đã sắp xếp theo cột ít giá trị phân biệt. Với mỗi tổ hợp, đo dung lượng tệp, thời gian đọc đầy đủ và CPU dùng khi đọc. Chọn một tổ hợp cho khối lượng công việc phân tích hằng ngày và viết ba câu bảo vệ.

**Pitfalls.** Chọn thuật toán nén theo tỉ lệ nén mà bỏ qua CPU · ghi dữ liệu chưa sắp xếp · so dung lượng mà quên thời gian đọc · kết luận từ một tệp mẫu quá nhỏ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng sáu tổ hợp đủ ba đại lượng, và lý do chọn dẫn được ít nhất hai con số từ bảng.

### Lesson 334 · Predicate pushdown and partition pruning - measuring what is read `TH`
**Prerequisites.** Lesson 333

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba tầng giảm lượng dữ liệu đọc, xếp từ thô tới mịn, và mỗi tầng dùng một cơ chế khác nhau. Cắt phân vùng dùng chính đường dẫn thư mục: điều kiện lọc trên cột phân vùng cho phép bỏ qua cả thư mục mà không mở tệp nào. Bỏ qua nhóm dòng dùng thống kê ở chân tệp tại lesson 332: điều kiện nằm ngoài khoảng nhỏ nhất tới lớn nhất thì bỏ qua cả nhóm. Cắt cột chỉ đọc đoạn cột cần dùng theo lesson 331. Ba tầng cộng lại có thể giảm lượng đọc hàng trăm lần, nhưng chỉ khi dữ liệu được bố trí phù hợp với cách truy vấn: **thống kê chỉ giúp khi dữ liệu đã sắp xếp theo cột lọc**, còn dữ liệu ngẫu nhiên thì mọi nhóm dòng đều chứa cả khoảng rộng nên không bỏ được nhóm nào. Cách kiểm chứng duy nhất đáng tin là đo số byte thực sự quét, có sẵn trong số liệu của engine, chứ nhìn thời gian chạy vì thời gian còn phụ thuộc bộ nhớ đệm.

**Outcome.** Đo được số byte quét của một truy vấn và quy phần giảm về đúng tầng cơ chế nào tạo ra nó.

**Đánh giá.** Tầng *phân tích*. Objective là phân rã một số đo tổng thành đóng góp của ba cơ chế, chứ chỉ ghi nhận truy vấn nhanh hơn. Kiểm bằng bảng bốn cách bố trí; đạt khi quy đúng phần giảm cho ít nhất ba trong bốn.

**Lab.** Lưu cùng dữ liệu ở bốn cách: không phân vùng chưa sắp xếp, không phân vùng đã sắp xếp, có phân vùng chưa sắp xếp, có phân vùng đã sắp xếp. Chạy cùng ba truy vấn trên cả bốn và đo số byte quét. Lập bảng và với mỗi ô giải thích phần giảm đến từ tầng nào.

**Pitfalls.** Đánh giá bằng thời gian chạy có bộ nhớ đệm · phân vùng theo cột không xuất hiện trong điều kiện lọc · sắp xếp theo cột không dùng để lọc · kết luận mà không đọc số liệu byte quét của engine.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng bốn cách bố trí nhân ba truy vấn đủ số byte quét, và quy đúng cơ chế cho ≥ 3/4 trường hợp giảm.

### Lesson 335 · The small files problem and compaction `TH`
**Prerequisites.** Lesson 334

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Chế độ hỏng phổ biến nhất của hồ dữ liệu, và nó tích tụ dần nên không ai thấy cho tới khi mọi truy vấn đều chậm. Nguyên nhân sinh tệp nhỏ: công việc luồng ghi mỗi vài phút một tệp, công việc theo lô có quá nhiều phân vùng đầu ra, và phân vùng theo cột có số giá trị phân biệt quá cao. Ba chi phí, và chi phí thứ ba là chi phí ẩn: mỗi tệp là ít nhất một yêu cầu tới lưu trữ đối tượng với độ trễ cố định theo lesson 329, mỗi tệp có chân tệp riêng nên phần siêu dữ liệu tăng tỉ lệ với số tệp, và lập lịch đọc hàng triệu tệp làm chính phần điều phối của engine thành nút thắt. Dồn tệp là công việc bảo trì bắt buộc chứ tuỳ chọn: gộp nhiều tệp nhỏ thành tệp cỡ mục tiêu, thường từ 128 MB tới 1 GB tuỳ engine. Chạy dồn thế nào để người đọc không thấy trạng thái nửa chừng là bài toán mà lesson 337 sẽ giải triệt để. Chỉ số phải theo dõi: kích thước tệp trung vị theo phân vùng, chứ tổng dung lượng.

**Outcome.** Đo được tác động của số tệp lên thời gian truy vấn ở cùng tổng dung lượng, và chạy dồn tệp đưa kích thước trung vị về khoảng mục tiêu.

**Đánh giá.** Tầng *áp dụng*. Objective là một thao tác bảo trì có kết quả đo được trước và sau. Kiểm bằng cặp số đo; đạt khi kích thước trung vị về khoảng mục tiêu và thời gian truy vấn giảm có số chứng minh.

**Lab.** Tạo cùng 10 GB dữ liệu ở ba cách: 20 tệp, 2.000 tệp và 200.000 tệp. Chạy cùng truy vấn trên cả ba và đo thời gian cùng số yêu cầu tới lưu trữ. Chạy dồn tệp trên bản tệ nhất và đo lại. Đặt một chỉ số theo dõi kích thước tệp trung vị theo phân vùng.

**Pitfalls.** Phân vùng theo cột có số giá trị phân biệt cao · để công việc luồng ghi trực tiếp vào bảng phân tích mà không dồn · theo dõi tổng dung lượng thay vì kích thước tệp · dồn tệp trong lúc có người đọc mà không có cơ chế bảo vệ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng ba cách có thời gian và số yêu cầu, sau khi dồn thì kích thước trung vị vào khoảng mục tiêu và thời gian truy vấn giảm có số.

### Lesson 336 · Partition layout design - choosing columns from query patterns `TH`
**Prerequisites.** Lesson 335

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phân vùng là quyết định khó sửa nhất trong bố trí dữ liệu vì đổi nó nghĩa là ghi lại toàn bộ. Nguyên tắc chọn: phân vùng theo cột **xuất hiện trong điều kiện lọc của phần lớn truy vấn**, và có số giá trị phân biệt đủ thấp để mỗi phân vùng còn đủ lớn. Hai chế độ hỏng đối xứng: quá ít giá trị phân biệt thì phân vùng khổng lồ nên cắt không được bao nhiêu; quá nhiều giá trị phân biệt thì sinh tệp nhỏ theo lesson 335. Quy tắc thực dụng để ước lượng: tổng dung lượng chia số phân vùng mong muốn phải ra kích thước tệp trong khoảng mục tiêu. Phân vùng nhiều tầng như năm rồi tháng rồi ngày: tiện cho cắt theo khoảng, nhưng mỗi tầng thêm một mức thư mục và làm liệt kê tốn hơn. Khi cột lọc có số giá trị phân biệt cao thì dùng sắp xếp hoặc gom cụm thay vì phân vùng, vì hai cách đó cho lọc mịn mà không tạo thư mục. Cách rút mẫu truy vấn từ nhật ký thật thay vì đoán, và vì sao thiết kế phân vùng phải xem lại sau sáu tháng.

**Outcome.** Thiết kế bố trí phân vùng từ nhật ký truy vấn thật, ước lượng kích thước tệp trước, và chứng minh bằng số byte quét rằng nó tốt hơn bố trí cũ.

**Đánh giá.** Tầng *sáng tạo*. Objective đòi tổng hợp mẫu truy vấn, ước lượng dung lượng và cơ chế cắt thành một thiết kế. Kiểm bằng so byte quét trước và sau trên cùng bộ truy vấn; đạt khi giảm có số và ước lượng kích thước tệp cùng bậc với thực tế.

**Lab.** Nhận nhật ký 200 truy vấn thật trên một bảng. Rút tần suất cột xuất hiện trong điều kiện lọc. Thiết kế bố trí phân vùng kèm ước lượng kích thước tệp. Ghi lại dữ liệu theo thiết kế mới, chạy lại cả 200 truy vấn, so tổng byte quét với bố trí cũ.

**Pitfalls.** Phân vùng theo mã định danh · phân vùng bốn tầng cho bảng nhỏ · thiết kế theo trực giác mà không đọc nhật ký truy vấn · quên ước lượng kích thước tệp.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tổng byte quét của 200 truy vấn giảm có số chứng minh, và kích thước tệp thực tế cùng bậc với ước lượng.

### Lesson 337 · Why a data lake needs transactions `LT`
**Prerequisites.** Lesson 336

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài gom bốn vấn đề đã gặp rải rác thành một phát biểu duy nhất: hồ dữ liệu là một đống tệp, và đống tệp không có khái niệm phiên bản nên không có thao tác nào là nguyên tử. Bốn biểu hiện, cả bốn đã xuất hiện ở các bài trước: công việc ghi chết giữa chừng để lại tệp nửa vời và người đọc thấy bảng sai theo lesson 330; dồn tệp ở lesson 335 không chạy được an toàn khi có người đọc; sửa hoặc xoá vài dòng để tuân thủ quy định buộc ghi lại cả phân vùng; và hai công việc cùng ghi một bảng thì kết quả không xác định. Vì sao thêm một cơ sở dữ liệu vào giữa không giải được: dữ liệu vẫn nằm ở tệp, và bất kỳ ai đọc thẳng tệp đều vòng qua mọi bảo đảm. Lời giải chung của cả ba định dạng bảng mở: **thêm một tầng siêu dữ liệu trỏ tới danh sách tệp, và đổi bảng là đổi con trỏ siêu dữ liệu một cách nguyên tử**. Từ một ý đó suy ra hết các tính năng ở hai bài sau, nên hiểu ý này quan trọng hơn thuộc tên tính năng.

**Outcome.** Quy bốn biểu hiện hỏng về cùng một nguyên nhân gốc, và phát biểu được cơ chế chung của định dạng bảng mở.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết tổng hợp, người học đã gặp cả bốn biểu hiện nên đây là bài đặt tên cho thứ họ đã thấy. Kiểm bằng bài quy nguyên nhân; đạt khi quy đúng cả bốn về cùng gốc và phát biểu đúng cơ chế con trỏ.

**Lab.** Tái hiện cả bốn biểu hiện trên một bảng Parquet thường: giết công việc ghi giữa chừng, dồn tệp trong lúc đọc, xoá 100 dòng theo yêu cầu tuân thủ, và chạy hai công việc ghi song song. Với mỗi biểu hiện, ghi lại người đọc nhìn thấy gì.

**Pitfalls.** Nghĩ bốn biểu hiện là bốn lỗi khác nhau cần bốn cách chữa · tin rằng đặt lịch chạy lệch giờ là đủ để tránh ghi song song · thêm quy ước đặt tên thay cho một tầng siêu dữ liệu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tái hiện được cả bốn biểu hiện với mô tả người đọc thấy gì, và quy đúng cả bốn về nguyên nhân không có thao tác nguyên tử.

### Lesson 338 · Open table formats - the metadata layer and atomic pointer swap `LT`
**Prerequisites.** Lesson 337

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Ba định dạng bảng mở phổ biến khác nhau ở chi tiết nhưng giống nhau ở cơ chế cốt lõi, và học cơ chế thì đọc tài liệu định dạng nào cũng nhanh. Cấu trúc chung ba tầng: tệp dữ liệu vẫn là Parquet như đã học; tệp kê khai liệt kê tệp dữ liệu nào thuộc phiên bản nào, kèm thống kê ở mức tệp; và con trỏ gốc chỉ tới kê khai hiện hành. Ghi là tạo tệp dữ liệu mới, tạo kê khai mới, rồi **đổi con trỏ gốc bằng một thao tác nguyên tử**; người đọc đang đọc phiên bản cũ không bị ảnh hưởng vì tệp cũ vẫn còn. Từ cơ chế đó suy ra bốn tính năng mà không cần nhớ riêng: ảnh chụp và du hành thời gian là giữ lại các kê khai cũ; ghi đồng thời là kiểm tra con trỏ chưa đổi trước khi đổi, đúng kiểu kiểm soát đồng thời lạc quan ở lesson 105; xoá và cập nhật vài dòng là ghi tệp mới và đánh dấu tệp cũ hết hiệu lực; và thống kê ở mức tệp trong kê khai cho phép bỏ qua tệp mà không mở chân tệp.

**Outcome.** Suy ra được bốn tính năng của định dạng bảng mở từ cơ chế ba tầng, thay vì liệt kê chúng như danh sách rời.

**Đánh giá.** Tầng *hiểu*. Objective là nắm cơ chế đủ để tự suy ra tính năng, tiêu chí đã dùng cho mọi module công cụ. Kiểm bằng bài suy luận; đạt khi giải thích đúng ít nhất ba trong bốn tính năng bằng cơ chế con trỏ và kê khai.

**Lab.** Tạo một bảng ở định dạng bảng mở, ghi ba lần, và sau mỗi lần đọc thẳng tệp siêu dữ liệu để xem kê khai và con trỏ đổi ra sao. Xoá 10 dòng và quan sát tệp dữ liệu cũ vẫn còn nguyên. Chạy hai công việc ghi song song và quan sát một bên bị từ chối.

**Pitfalls.** Học danh sách tính năng mà bỏ qua cơ chế · tin rằng xoá dòng là xoá byte ngay · nghĩ ba định dạng khác nhau về bản chất.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Giải thích đúng ≥ 3/4 tính năng bằng cơ chế, và quan sát được con trỏ đổi qua ba lần ghi.

### Lesson 339 · Time travel, schema evolution and partition evolution `TH`
**Prerequisites.** Lesson 338

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba tính năng trực tiếp giải những bài toán đã tồn đọng từ các module trước. Du hành thời gian đọc bảng ở một phiên bản hoặc một thời điểm, dùng cho ba việc: đối soát lại một báo cáo cũ, khôi phục sau khi ghi sai, và chạy lại một công việc trên đúng dữ liệu nó đã thấy, thứ mà lesson 324 cần để kết quả tái lập được. Tiến hoá lược đồ thêm, xoá, đổi tên cột mà không ghi lại dữ liệu, vì kê khai ánh xạ cột theo mã định danh chứ theo vị trí; đây là lời giải cho bài toán đã đặt ở lesson 209 và 313. Tiến hoá phân vùng đổi cách phân vùng cho dữ liệu mới mà giữ nguyên dữ liệu cũ, nên sửa được quyết định phân vùng sai ở lesson 336 mà không phải ghi lại toàn bộ. Giới hạn phải biết: du hành thời gian chỉ còn trong phạm vi ảnh chụp chưa bị dọn, và dọn ảnh chụp là việc bắt buộc ở lesson 340, nên phải chọn thời gian giữ có chủ ý chứ để mặc định.

**Outcome.** Dùng du hành thời gian để khôi phục sau một lần ghi sai, và đổi lược đồ cùng cách phân vùng mà không ghi lại dữ liệu cũ.

**Đánh giá.** Tầng *áp dụng*. Objective là ba thao tác vận hành có kết quả kiểm được bằng đối soát. Kiểm bằng ba bài thực hành; đạt khi cả ba thành công và bản khôi phục khớp tuyệt đối với bản trước khi ghi sai.

**Lab.** Ghi đè nhầm một phân vùng bằng dữ liệu sai, rồi khôi phục bằng du hành thời gian và đối soát với bản đã lưu. Thêm một cột và đổi tên một cột, chứng minh không tệp dữ liệu nào được ghi lại. Đổi phân vùng từ theo tháng sang theo ngày cho dữ liệu mới và chạy truy vấn bắc qua cả hai vùng.

**Pitfalls.** Dựa vào du hành thời gian như cơ chế sao lưu duy nhất · đổi lược đồ mà không xét bên tiêu thụ · để thời gian giữ ảnh chụp mặc định rồi mất khả năng khôi phục đúng lúc cần.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bản khôi phục khớp tuyệt đối, đổi lược đồ không sinh ghi lại dữ liệu, và truy vấn bắc qua hai cách phân vùng cho kết quả đúng.

### Lesson 340 · Table maintenance - compaction, snapshot expiry and orphan files `TH`
**Prerequisites.** Lesson 339

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Định dạng bảng mở giải bài toán nguyên tử nhưng sinh ba việc bảo trì mới, và bỏ cả ba là cách làm bảng chậm dần rồi tốn tiền dần. Dồn tệp vẫn cần theo lesson 335, nhưng nay chạy an toàn được vì kết quả công bố bằng đổi con trỏ. Hết hạn ảnh chụp xoá các kê khai cũ và tệp dữ liệu chỉ thuộc về chúng; không chạy thì dung lượng tăng vô hạn vì mọi phiên bản đều được giữ, chạy quá mạnh tay thì mất khả năng du hành thời gian ở lesson 339, nên thời gian giữ là một quyết định có đánh đổi phải ghi vào tài liệu. Dọn tệp mồ côi xoá tệp nằm trong kho nhưng không kê khai nào trỏ tới, thường do công việc ghi chết giữa chừng; đây là thao tác nguy hiểm nhất vì xoá nhầm là mất dữ liệu, nên luôn chạy ở chế độ liệt kê trước. Lập lịch ba việc này như một phần của hệ điều phối ở M22, có theo dõi và có cảnh báo khi chúng không chạy.

**Outcome.** Lập lịch và chạy được ba việc bảo trì, đặt thời gian giữ ảnh chụp có lý do, và chứng minh dung lượng cùng thời gian truy vấn được giữ ổn định.

**Đánh giá.** Tầng *áp dụng*. Objective là dựng một quy trình bảo trì định kỳ có số đo trước và sau. Kiểm bằng phép đo qua nhiều chu kỳ; đạt khi cả ba việc chạy tự động và dung lượng không tăng đơn điệu.

**Lab.** Chạy một công việc ghi mỗi 5 phút trong hai giờ để sinh tệp nhỏ và nhiều ảnh chụp. Đo dung lượng và thời gian truy vấn theo thời gian. Lập lịch ba việc bảo trì trong Airflow. Chạy dọn tệp mồ côi ở chế độ liệt kê trước rồi mới xoá. Đo lại và vẽ đồ thị.

**Pitfalls.** Không lập lịch bảo trì · đặt hết hạn ảnh chụp quá ngắn rồi mất khả năng khôi phục · chạy dọn mồ côi ngay mà không liệt kê trước · dọn mồ côi trong lúc một công việc ghi đang chạy.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba việc bảo trì chạy tự động có theo dõi, đồ thị cho thấy dung lượng và thời gian truy vấn ổn định, và thời gian giữ ảnh chụp có lý do ghi lại.

### Lesson 341 · Lakehouse layout for the reference pipeline `TH`
**Prerequisites.** Lesson 340

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài ghép: chuyển tầng lưu trữ của pipeline tham chiếu sang định dạng bảng mở và áp toàn bộ quyết định bố trí đã học. Ba tầng medallion ở lesson 198 nay có nghĩa cụ thể về mặt lưu trữ: tầng đồng giữ nguyên bản gốc bất biến, thường là định dạng nguồn; tầng bạc là bảng mở đã làm sạch, phân vùng theo ngày sự kiện; tầng vàng là bảng mở hướng nghiệp vụ, bố trí theo mẫu truy vấn thật ở lesson 336. Quyết định phải ghi lại cho từng tầng: định dạng tệp, thuật toán nén, cột phân vùng, cột sắp xếp, kích thước tệp mục tiêu, thời gian giữ ảnh chụp. Mỗi quyết định kèm lý do và số đo, vì đây là đầu vào trực tiếp cho hồ sơ kiến trúc ở M39. Luồng CDC ở M31 và công việc luồng ở M32 nay ghi vào bảng mở, nên phần dồn tệp cho dữ liệu luồng là bắt buộc và phải lập lịch.

**Outcome.** Chuyển ba tầng sang định dạng bảng mở với bộ quyết định bố trí đầy đủ, và chứng minh tổng byte quét của bộ truy vấn chuẩn giảm.

**Đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module thành một thiết kế có sáu quyết định cho ba tầng. Kiểm bằng bảng quyết định cộng số đo trước sau; đạt khi mọi ô có lý do và tổng byte quét giảm có số.

**Lab.** Chuyển ba tầng sang bảng mở. Lập bảng sáu quyết định cho từng tầng, mỗi ô kèm lý do và số đo hỗ trợ. Chạy bộ truy vấn chuẩn trước và sau, so tổng byte quét và thời gian. Lập lịch bảo trì cho cả ba tầng.

**Pitfalls.** Áp cùng một bố trí cho cả ba tầng · quên dồn tệp cho dữ liệu từ luồng · ghi quyết định mà không ghi lý do · đo thời gian mà quên byte quét.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng 18 ô quyết định đều có lý do, tổng byte quét của bộ truy vấn chuẩn giảm có số, và bảo trì cả ba tầng đã lập lịch.

### Lesson 342 · Choosing storage - warehouse, lake or lakehouse `DA`
**Prerequisites.** Lesson 341

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Bài dự án khép module: chọn kiến trúc lưu trữ cho ba tình huống có ràng buộc khác nhau và bảo vệ bằng số đo của chính mình. Ba phương án và điểm mạnh thật của từng phương án: kho dữ liệu cho hiệu năng truy vấn ổn định và vận hành đơn giản, đổi lại chi phí trên mỗi đơn vị dung lượng cao và khó chứa dữ liệu phi cấu trúc; hồ dữ liệu cho chi phí thấp và linh hoạt định dạng, đổi lại không có bảo đảm giao dịch theo lesson 337; lakehouse ở giữa, đổi lại thêm việc bảo trì ở lesson 340 và phụ thuộc vào engine hỗ trợ định dạng bảng. Ba tình huống: một đội năm người chỉ có dữ liệu bảng và truy vấn theo ngày; một công ty có cả nhật ký thô lẫn dữ liệu bảng, khối lượng hàng chục terabyte; và một hệ phải giữ dữ liệu bảy năm cho tuân thủ nhưng chỉ truy vấn phần nóng. Yêu cầu: mỗi khuyến nghị kèm ít nhất ba số đo lấy từ lab của chính mình.

**Outcome.** Đưa ra khuyến nghị lưu trữ cho ba tình huống, mỗi khuyến nghị dẫn ít nhất ba số đo từ lab và nêu điều kiện làm nó sai.

**Đánh giá.** Tầng *đánh giá*. Bài dự án đo năng lực ra quyết định kiến trúc có bằng chứng, chuẩn bị cho M39. Kiểm bằng rà soát chéo giữa học viên; đạt khi mọi số truy được về lab và mỗi khuyến nghị có điều kiện đảo ngược.

**Lab.** Với ba tình huống cho trước, viết khuyến nghị kèm bảng số đo trích từ các lab trong module. Mỗi khuyến nghị nêu hai điều kiện làm nó sai. Rà soát chéo với một học viên khác: họ chọn một số bất kỳ trong bài bạn và bạn phải chỉ ra lab nào sinh ra số đó.

**Pitfalls.** Khuyến nghị lakehouse cho mọi tình huống · dẫn số từ tài liệu nhà cung cấp · bỏ qua chi phí vận hành bảo trì · viết điều kiện đảo ngược chung chung.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Ba khuyến nghị đều có ≥ 3 số đo truy được về lab, mỗi khuyến nghị có hai điều kiện đảo ngược cụ thể, và qua được rà soát chéo.

# MODULE 34 · SPARK AND DISTRIBUTED PROCESSING

**Lessons 343–356 · 28 giờ**

| | |
|---|---|
| **Objective cấp module** | Viết, chẩn đoán và tối ưu được công việc Spark trên dữ liệu vượt bộ nhớ một máy, và giải thích mọi tối ưu bằng kế hoạch thực thi chứ bằng kinh nghiệm truyền miệng |
| **Tiền đề** | M33 |
| **Exit criterion** | Ba công việc chậm cho sẵn được chẩn đoán đúng nút thắt và sửa đạt ngưỡng hiệu năng, mỗi lần dẫn bằng kế hoạch thực thi và số liệu |
| **Kỹ năng SFIA** | `HPCC` mức 4 · `PROG` mức 4 |
| **Chế độ hỏng** | Học API DataFrame rồi coi Spark là pandas chạy trên cụm, nên không hiểu xáo trộn và đổ lỗi mọi chuyện cho thiếu bộ nhớ |

Mức `A`. Module đọc chính những tệp đã bố trí ở M33, nên mọi số đo byte quét ở đó dùng lại được ở đây.

Lesson 354 dạy Structured Streaming ở mức đầy đủ. Lesson 327 ở M32 đã đối chiếu mô hình lô vi mô ở mức khái niệm khi chưa có Spark; bài này là chỗ trả nợ phần nội bộ.

### Lesson 343 · When not to distribute - one big machine against a cluster `LT`
**Prerequisites.** Module 34: M33

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài mở module bằng câu hỏi ngược, và đây là câu hỏi mà phần lớn tài liệu bỏ qua. Một máy hiện nay có thể có hàng trăm gigabyte bộ nhớ và đĩa thể rắn rất nhanh, nên dữ liệu dưới vài trăm gigabyte thường xử lý trên một máy nhanh hơn và rẻ hơn một cụm, vì không có chi phí truyền qua mạng và không có chi phí vận hành cụm. Bốn chi phí của phân tán mà người mới hay bỏ qua: truyền dữ liệu qua mạng chậm hơn đọc bộ nhớ nhiều bậc, cần đồng bộ giữa các nút, gỡ lỗi khó hơn hẳn vì lỗi xảy ra ở một nút trong nhiều nút, và phải vận hành thêm một hệ. Ba dấu hiệu cho thấy thật sự cần phân tán: dữ liệu vượt bộ nhớ và đĩa một máy, thời gian xử lý một máy vượt cửa sổ cho phép, hoặc cần chịu lỗi khi một máy chết. Mô hình chia rồi gộp và giới hạn của nó: phần việc không chia được sẽ đặt trần cho mọi nỗ lực thêm máy.

**Outcome.** Quyết định có cần phân tán hay không cho bốn khối lượng công việc cho trước, dẫn bằng ước lượng dung lượng và thời gian.

**Đánh giá.** Tầng *đánh giá*. Objective là một quyết định kiến trúc có ràng buộc rõ, và là chỗ nhiều đội sai ngay từ đầu. Kiểm bằng bốn khối lượng công việc trong đó ít nhất một không nên phân tán; đạt khi quyết định đúng ít nhất ba và nhận ra trường hợp không nên phân tán.

**Lab.** Chạy cùng một phép biến đổi trên 50 GB bằng một máy lớn và bằng cụm bốn nút, đo thời gian và chi phí ước tính. Lặp lại với 5 GB. Cho bốn khối lượng công việc và quyết định phân tán hay không, kèm ước lượng.

**Pitfalls.** Dùng cụm vì dữ liệu nghe có vẻ lớn · bỏ qua chi phí vận hành khi so · quên rằng phần không chia được đặt trần cho việc thêm máy.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Quyết định đúng ≥ 3/4 khối lượng công việc kèm ước lượng, và nhận ra đúng trường hợp một máy thắng.

### Lesson 344 · Architecture - driver, executor and where your code actually runs `LT`
**Prerequisites.** Lesson 343

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Hiểu nhầm phổ biến nhất khi mới học Spark là nghĩ mã chạy ở một chỗ. Thực tế có hai nơi: trình điều khiển chạy phần dựng kế hoạch và điều phối, trình thực thi chạy phần xử lý dữ liệu thật trên từng phần dữ liệu. Hệ quả trực tiếp và hay gây lỗi: biến khai báo ở trình điều khiển được sao chép sang trình thực thi chứ dùng chung, nên gán vào một biến bên trong hàm xử lý không có tác dụng gì ở trình điều khiển; và gọi một thao tác thu về trên dữ liệu lớn sẽ kéo toàn bộ về trình điều khiển rồi làm nó chết. Trình quản lý cụm cấp tài nguyên và có nhiều lựa chọn, trong đó Kubernetes ở M36. Phân vùng là đơn vị song song: một phân vùng do một lõi xử lý tại một thời điểm, nên số phân vùng đặt trần cho mức song song đúng như số phân vùng Kafka ở lesson 293. Biến phát tán và bộ đếm là hai cơ chế chính thức để chia sẻ dữ liệu giữa hai nơi.

**Outcome.** Chỉ ra với một đoạn mã cho trước phần nào chạy ở trình điều khiển, phần nào ở trình thực thi, và dự đoán lỗi nếu nhầm.

**Đánh giá.** Tầng *phân tích*. Objective là truy hành vi lỗi về mô hình thực thi, kỹ năng nền cho mọi bài gỡ lỗi sau. Kiểm bằng năm đoạn mã trong đó ba đoạn có lỗi do nhầm nơi chạy; đạt khi chỉ đúng ít nhất bốn.

**Lab.** Cho năm đoạn mã. Với mỗi đoạn, đánh dấu phần chạy ở đâu và dự đoán kết quả. Chạy thật và so với dự đoán. Chạy một thao tác thu về trên bảng 20 GB và quan sát trình điều khiển chết, đọc thông báo lỗi.

**Pitfalls.** Dùng biến đếm thường trong hàm xử lý · gọi thu về để xem dữ liệu · nghĩ trình điều khiển cũng xử lý dữ liệu · nhầm số lõi với số phân vùng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chỉ đúng ≥ 4/5 đoạn mã kèm dự đoán khớp thực tế, và mô tả đúng thông báo lỗi khi trình điều khiển hết bộ nhớ.

### Lesson 345 · DataFrame, the lazy plan and the catalyst optimiser `TH`
**Prerequisites.** Lesson 344

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Spark không chạy ngay khi gọi phép biến đổi mà dựng một kế hoạch, và chỉ chạy khi gặp một thao tác hành động. Tính trễ là thứ cho phép bộ tối ưu nhìn toàn bộ chuỗi rồi sắp xếp lại, ví dụ đẩy điều kiện lọc xuống sát nguồn để tận dụng cắt phân vùng ở lesson 334. Bốn giai đoạn của kế hoạch: kế hoạch logic chưa phân giải, kế hoạch logic đã phân giải, kế hoạch logic đã tối ưu, và kế hoạch vật lý. Đọc được bốn giai đoạn này là kỹ năng chẩn đoán chính của cả module. Vì sao DataFrame nhanh hơn RDD cho phần lớn việc: bộ tối ưu hiểu được cấu trúc nên tối ưu được, còn với RDD thì mã người dùng là hộp đen. Hệ quả tương tự cho hàm do người dùng định nghĩa: nó chặn tối ưu và buộc chuyển đổi dữ liệu qua lại, nên thường chậm hơn hàm dựng sẵn nhiều lần, đúng cảnh báo sẽ đo ở lesson 352.

**Outcome.** Đọc kế hoạch thực thi và chỉ ra bộ tối ưu đã đẩy điều kiện lọc xuống đâu, cắt cột nào, và vì sao.

**Đánh giá.** Tầng *áp dụng*. Objective là một kỹ năng đọc cụ thể, điều kiện cần cho mọi bài tối ưu sau. Kiểm bằng ba truy vấn có kế hoạch khác nhau; đạt khi đọc đúng vị trí đẩy lọc và cắt cột ở cả ba.

**Lab.** Với ba truy vấn trên bảng ở M33, in cả bốn giai đoạn kế hoạch. Với mỗi truy vấn, chỉ ra điều kiện lọc được đẩy xuống đâu và những cột nào bị cắt. Viết lại một truy vấn bằng hàm do người dùng định nghĩa và so kế hoạch cùng thời gian chạy với bản dùng hàm dựng sẵn.

**Pitfalls.** Đọc kế hoạch logic mà tưởng là kế hoạch vật lý · viết hàm tự định nghĩa cho việc hàm dựng sẵn làm được · gọi một hành động giữa chuỗi biến đổi rồi tự cắt mất cơ hội tối ưu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đọc đúng vị trí đẩy lọc và cắt cột ở cả ba truy vấn, và có số đo chênh lệch giữa hàm tự định nghĩa và hàm dựng sẵn.

### Lesson 346 · Transformations, actions and the shuffle boundary `TH`
**Prerequisites.** Lesson 345

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phép biến đổi chia làm hai loại theo việc dữ liệu có phải đi qua mạng hay không, và ranh giới này quyết định gần như toàn bộ hiệu năng. Biến đổi hẹp như lọc hay thêm cột xử lý trong một phân vùng, không cần dữ liệu từ phân vùng khác, nên chạy song song hoàn toàn và ghép chuỗi lại được. Biến đổi rộng như gộp nhóm, kết bảng, sắp xếp cần gom dữ liệu cùng khoá về một chỗ, và đó là xáo trộn: ghi ra đĩa, truyền qua mạng, đọc lại. Spark chia công việc thành các giai đoạn tại mỗi ranh giới xáo trộn, nên **đếm số giai đoạn trong kế hoạch là cách nhanh nhất để biết có bao nhiêu lần xáo trộn**. Nguyên tắc thiết kế rút ra: lọc càng sớm càng tốt để ít dữ liệu đi qua xáo trộn; gộp hai phép gộp nhóm thành một nếu cùng khoá; tránh sắp xếp toàn cục nếu chỉ cần thứ tự trong nhóm. Đọc giao diện Spark để thấy số giai đoạn, số tác vụ và dữ liệu xáo trộn của từng giai đoạn.

**Outcome.** Đếm số lần xáo trộn của một truy vấn từ kế hoạch, và viết lại truy vấn để giảm số đó mà giữ nguyên kết quả.

**Đánh giá.** Tầng *áp dụng*. Objective là một phép biến đổi mã có kết quả đo được bằng số giai đoạn và dữ liệu xáo trộn. Kiểm bằng ba truy vấn; đạt khi giảm được số xáo trộn ở ít nhất hai mà kết quả vẫn khớp tuyệt đối.

**Lab.** Với ba truy vấn cho sẵn, đếm số giai đoạn và đo dung lượng xáo trộn từ giao diện Spark. Viết lại từng truy vấn để giảm xáo trộn, đo lại, và đối soát kết quả với bản gốc.

**Pitfalls.** Sắp xếp toàn cục khi chỉ cần thứ tự trong nhóm · gộp nhóm nhiều lần trên cùng khoá · đánh giá bằng thời gian chạy mà không xem dung lượng xáo trộn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Giảm được số lần xáo trộn ở ≥ 2/3 truy vấn với kết quả khớp tuyệt đối, kèm số đo dung lượng xáo trộn trước và sau.

### Lesson 347 · Reading the Spark UI and the physical plan `TH`
**Prerequisites.** Lesson 346

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Giao diện Spark là nguồn sự thật duy nhất khi chẩn đoán, và biết đọc nó phân biệt người tối ưu có căn cứ với người đổi tham số theo cảm tính. Năm chỗ phải biết xem: danh sách công việc và giai đoạn để thấy giai đoạn nào tốn thời gian; biểu đồ thời gian của các tác vụ trong một giai đoạn để thấy phân bố có lệch không; số liệu dung lượng đọc, ghi và xáo trộn của từng giai đoạn; kế hoạch vật lý kèm số liệu thực tế; và trang trình thực thi để thấy bộ nhớ cùng thời gian dọn rác. Ba dấu hiệu đọc được ngay từ biểu đồ thời gian tác vụ: phân bố đều thì hệ khoẻ, một tác vụ dài hẳn thì lệch dữ liệu ở lesson 349, nhiều tác vụ rất ngắn thì tệp nhỏ hoặc quá nhiều phân vùng. Nguyên tắc chẩn đoán: bắt đầu từ giai đoạn tốn thời gian nhất, rồi mới đi vào tác vụ, chứ đoán từ mã.

**Outcome.** Từ giao diện Spark của một công việc chậm, định vị giai đoạn tốn nhất và phân loại hình dạng phân bố tác vụ thành một trong ba dấu hiệu.

**Đánh giá.** Tầng *phân tích*. Objective là kỹ năng chẩn đoán từ dữ liệu quan sát, dùng lại ở ba bài sau. Kiểm bằng ba công việc chậm; đạt khi định vị đúng giai đoạn ở cả ba và phân loại đúng dấu hiệu ở ít nhất hai.

**Lab.** Chạy ba công việc chậm cho sẵn, mỗi công việc một nguyên nhân. Với mỗi công việc, chụp lại năm chỗ trong giao diện, định vị giai đoạn tốn nhất, và phân loại hình dạng phân bố tác vụ. Chưa sửa, chỉ chẩn đoán.

**Pitfalls.** Đoán nguyên nhân từ mã mà không mở giao diện · nhìn tổng thời gian mà không xem phân bố tác vụ · bỏ qua số liệu dung lượng xáo trộn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Định vị đúng giai đoạn tốn nhất ở cả ba công việc và phân loại đúng dấu hiệu ở ≥ 2/3.

### Lesson 348 · The shuffle - why it dominates cost `TH`
**Prerequisites.** Lesson 347

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Xáo trộn là thao tác đắt nhất trong Spark và hiểu cơ chế của nó giải thích phần lớn các mẹo tối ưu. Ba pha: bên ghi phân loại dữ liệu theo khoá đích rồi ghi ra đĩa cục bộ; dữ liệu truyền qua mạng; bên đọc gom các mảnh cùng khoá lại. Bốn chi phí cộng dồn: tuần tự hoá, ghi đĩa, truyền mạng, và đọc cùng gộp. Số phân vùng sau xáo trộn là tham số quan trọng nhất và mặc định thường sai với dữ liệu thật: quá ít thì mỗi phân vùng quá lớn nên tràn ra đĩa, quá nhiều thì sinh hàng loạt tác vụ rất ngắn và chi phí lập lịch át phần xử lý. Quy tắc ước lượng: dung lượng xáo trộn chia số phân vùng nên ra khoảng vài trăm megabyte mỗi phân vùng. Thực thi truy vấn thích ứng có thể tự gộp phân vùng sau xáo trộn dựa trên số liệu thật lúc chạy, nên bật nó lên giải được phần lớn trường hợp đặt tham số sai, nhưng vẫn phải hiểu để chẩn đoán khi nó không giúp.

**Outcome.** Chọn số phân vùng sau xáo trộn từ ước lượng dung lượng, và định lượng mức cải thiện so với giá trị mặc định.

**Đánh giá.** Tầng *áp dụng*. Objective là một quyết định tham số có căn cứ ước lượng, kiểm được bằng đo đạc. Kiểm bằng bảng bốn giá trị; đạt khi có đường cong, giá trị chọn gần tối ưu và giải thích được hai đầu đường cong.

**Lab.** Chạy một công việc có xáo trộn lớn ở bốn giá trị số phân vùng, đo thời gian, dung lượng tràn ra đĩa và số tác vụ. Vẽ đường cong. Bật thực thi truy vấn thích ứng và đo lại, so với giá trị tốt nhất tự chọn.

**Pitfalls.** Để số phân vùng mặc định cho mọi công việc · tăng số phân vùng rất lớn để cho chắc · bỏ qua dung lượng tràn ra đĩa khi đánh giá.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng bốn giá trị đủ ba đại lượng, giá trị chọn nằm gần điểm tối ưu của đường cong, và có số so với chế độ thích ứng.

### Lesson 349 · Data skew - diagnosis and four remedies `TH`
**Prerequisites.** Lesson 348

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Nguyên nhân số một khiến công việc chạy lâu bất thường, và đã được nhắc tới hai lần ở lesson 293 và 326 dưới dạng khác. Biểu hiện trên giao diện rất đặc trưng: 199 tác vụ xong trong hai phút còn một tác vụ chạy năm tiếng. Nguyên nhân là phân bố khoá lệch, thường do giá trị rỗng gom về một phân vùng, một khách hàng lớn chiếm phần lớn giao dịch, hoặc một giá trị mặc định được dùng cho mọi bản ghi thiếu dữ liệu. Chẩn đoán bằng cách đếm số bản ghi theo khoá và xem phân vị cao nhất, chứ nhìn tổng. Bốn cách chữa và cái giá của từng cách: thêm muối vào khoá rồi gộp hai bước, tách riêng khoá nóng xử lý bằng kết phát tán, lọc bỏ giá trị rỗng trước khi kết nếu nghiệp vụ cho phép, và bật xử lý lệch tự động của chế độ thích ứng. Nguyên tắc: **thêm máy không chữa được lệch dữ liệu**, vì một khoá vẫn phải nằm trên một nút, và đây là điều cần nói rõ khi ai đó đề nghị tăng cụm.

**Outcome.** Chẩn đoán lệch dữ liệu từ giao diện, định lượng mức lệch bằng phân bố khoá, và chữa bằng một trong bốn cách kèm số đo cải thiện.

**Đánh giá.** Tầng *phân tích*. Objective đòi truy từ triệu chứng về phân bố dữ liệu rồi chọn cách chữa phù hợp với ràng buộc nghiệp vụ. Kiểm bằng công việc lệch tiêm sẵn; đạt khi định lượng đúng mức lệch và thời gian chạy giảm ít nhất một nửa.

**Lab.** Nhận một công việc kết bảng có khoá lệch. Đếm phân bố khoá và ghi tỉ lệ của khoá lớn nhất. Thử cả bốn cách chữa, mỗi cách đo thời gian và ghi hạn chế của nó. Chứng minh bằng thực nghiệm rằng tăng gấp đôi số trình thực thi gần như không cải thiện.

**Pitfalls.** Tăng tài nguyên để chữa lệch · thêm muối mà quên bước gộp thứ hai nên sai kết quả · lọc bỏ giá trị rỗng mà không hỏi nghiệp vụ · kết luận lệch từ tổng thời gian mà không xem phân bố tác vụ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mức lệch được định lượng bằng phân bố khoá, ít nhất một cách chữa giảm thời gian ≥ 50% với kết quả khớp, và có số chứng minh thêm máy không giúp.

### Lesson 350 · Joins - broadcast, sort-merge and choosing between them `TH`
**Prerequisites.** Lesson 349

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba chiến lược kết trong Spark với ba điều kiện áp dụng khác nhau. Kết phát tán gửi bảng nhỏ tới mọi trình thực thi rồi kết cục bộ, **không có xáo trộn**, nên nhanh hơn nhiều bậc; điều kiện là bảng nhỏ phải vừa bộ nhớ trình thực thi. Kết sắp xếp gộp xáo trộn cả hai bảng theo khoá rồi gộp, là mặc định cho hai bảng lớn. Kết băm xáo trộn dựng bảng băm phía một bên, dùng khi một bên nhỏ hơn đáng kể nhưng vẫn quá lớn để phát tán. Spark chọn dựa trên ước lượng kích thước, và ước lượng sai là nguyên nhân phổ biến làm công việc chậm: thống kê cũ hoặc bảng sinh từ phép biến đổi phức tạp thì ước lượng lệch xa. Ba cách can thiệp: cập nhật thống kê bảng, đặt gợi ý kết trong truy vấn, và chỉnh ngưỡng phát tán. Cảnh báo: phát tán bảng quá lớn làm trình thực thi hết bộ nhớ, nên gợi ý là dao hai lưỡi và phải kèm số đo kích thước thật.

**Outcome.** Đọc kế hoạch để biết Spark chọn chiến lược kết nào, đánh giá lựa chọn đó đúng hay sai bằng kích thước thật, và can thiệp khi sai.

**Đánh giá.** Tầng *đánh giá*. Objective đòi phán đoán về quyết định của bộ tối ưu chứ chấp nhận nó. Kiểm bằng ba phép kết trong đó một phép bộ tối ưu chọn sai; đạt khi nhận ra trường hợp chọn sai và can thiệp cho kết quả nhanh hơn.

**Lab.** Chạy ba phép kết với kích thước bảng khác nhau, đọc kế hoạch để biết chiến lược được chọn, và đo thời gian. Với phép kết mà bộ tối ưu chọn sai, cập nhật thống kê rồi đo lại; nếu vẫn sai thì đặt gợi ý. Thử phát tán một bảng quá lớn và ghi lại lỗi.

**Pitfalls.** Đặt gợi ý phát tán mà không đo kích thước bảng · để thống kê cũ · tăng ngưỡng phát tán rất cao cho chắc · kết luận chiến lược từ tên phép kết trong mã.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đọc đúng chiến lược ở cả ba phép kết, can thiệp đúng chỗ bộ tối ưu chọn sai và có số cải thiện, và mô tả đúng lỗi khi phát tán bảng quá lớn.

### Lesson 351 · Partitioning, bucketing and file layout for Spark `TH`
**Prerequisites.** Lesson 350

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài nối M33 với M34: bố trí dữ liệu trên đĩa quyết định Spark phải làm bao nhiêu việc. Ba khái niệm dễ lẫn nhau: phân vùng trên đĩa là thư mục theo giá trị cột, phân vùng trong bộ nhớ là đơn vị song song lúc chạy, và gom cụm là chia dữ liệu theo băm của khoá thành số tệp cố định khi ghi. Gom cụm giải một bài toán cụ thể: hai bảng cùng gom cụm theo cùng khoá và cùng số cụm thì kết được mà **không cần xáo trộn**, nên phép kết lặp đi lặp lại giữa hai bảng lớn rẻ hẳn đi. Cái giá: ghi tốn hơn, và mọi bên ghi phải tuân cùng quy ước. Điều chỉnh số phân vùng trong bộ nhớ bằng hai cách khác nhau về bản chất: gộp lại không xáo trộn nhưng có thể để phân bố lệch, chia lại có xáo trộn nhưng cho phân bố đều. Quy tắc chọn kích thước tệp đầu ra để tránh vấn đề tệp nhỏ ở lesson 335.

**Outcome.** Thiết kế bố trí đầu ra cho một chuỗi công việc nối nhau sao cho phép kết lặp lại không phải xáo trộn, và đo mức tiết kiệm.

**Đánh giá.** Tầng *sáng tạo*. Objective đòi thiết kế bố trí phục vụ một mẫu truy vấn tương lai chứ tối ưu một truy vấn đơn lẻ. Kiểm bằng so số lần xáo trộn và thời gian trước sau; đạt khi phép kết hết xáo trộn và kích thước tệp trong khoảng mục tiêu.

**Lab.** Hai bảng lớn được kết với nhau trong năm công việc khác nhau. Ghi lại chúng có gom cụm theo khoá kết, rồi chạy lại cả năm công việc và đo tổng thời gian cùng dung lượng xáo trộn. So chi phí ghi thêm với phần tiết kiệm. Thử gộp lại và chia lại rồi so phân bố phân vùng.

**Pitfalls.** Nhầm phân vùng trên đĩa với phân vùng trong bộ nhớ · gom cụm với số cụm khác nhau giữa hai bảng nên vẫn xáo trộn · dùng gộp lại rồi để phân bố lệch nặng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phép kết sau khi gom cụm không còn xáo trộn có số chứng minh, và bảng so chi phí ghi thêm với phần tiết kiệm qua năm công việc.

### Lesson 352 · Caching, persistence and when it hurts `TH`
**Prerequisites.** Lesson 351

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Giữ lại kết quả trung gian trong bộ nhớ giúp khi cùng một kết quả được dùng nhiều lần, và hại khi không phải vậy. Cơ chế: đánh dấu giữ lại thì lần hành động đầu tiên tính xong sẽ lưu, các lần sau đọc lại thay vì tính lại. Các mức lưu trữ và đánh đổi: chỉ bộ nhớ thì nhanh nhất nhưng thiếu chỗ là mất và phải tính lại, bộ nhớ và đĩa thì an toàn hơn nhưng chậm hơn, có tuần tự hoá thì tốn ít bộ nhớ hơn và tốn CPU hơn. Ba tình huống giữ lại là sai: dữ liệu chỉ dùng một lần, dữ liệu quá lớn nên đẩy thứ khác ra khỏi bộ nhớ, và chuỗi biến đổi rẻ tới mức tính lại còn nhanh hơn đọc lại. Quan hệ với điểm kiểm tra: giữ lại vẫn phụ thuộc vào dòng dõi nên mất bộ nhớ thì tính lại được, còn đặt điểm kiểm tra cắt hẳn dòng dõi và ghi ra kho bền, dùng khi chuỗi biến đổi quá dài. Luôn giải phóng khi không dùng nữa, vì bộ nhớ bị giữ là bộ nhớ lấy mất của phép xáo trộn.

**Outcome.** Quyết định có nên giữ lại một kết quả trung gian hay không dựa trên số lần dùng và chi phí tính lại, kèm số đo cả hai chiều.

**Đánh giá.** Tầng *đánh giá*. Objective đòi cân nhắc chứ áp dụng một quy tắc, vì giữ lại sai làm chậm đi. Kiểm bằng ba tình huống trong đó ít nhất một không nên giữ lại; đạt khi quyết định đúng cả ba và có số đo chứng minh.

**Lab.** Với ba chuỗi công việc khác nhau, đo thời gian có và không có giữ lại, và đo cả ảnh hưởng lên bộ nhớ dành cho xáo trộn. Với tình huống không nên giữ lại, định lượng phần chậm đi. Thử ba mức lưu trữ trên cùng dữ liệu.

**Pitfalls.** Giữ lại mọi DataFrame trung gian theo thói quen · giữ lại dữ liệu quá lớn rồi làm xáo trộn tràn đĩa · quên giải phóng · đánh giá chỉ bằng thời gian lần chạy thứ hai.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba quyết định đúng kèm số đo, phần chậm đi của trường hợp giữ lại sai được định lượng, và có bảng so ba mức lưu trữ.

### Lesson 353 · Memory management and reading an out-of-memory failure `TH`
**Prerequisites.** Lesson 352

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bộ nhớ một trình thực thi chia thành các vùng có mục đích khác nhau, và biết vùng nào hết mới sửa đúng chỗ. Vùng thực thi phục vụ xáo trộn, kết và sắp xếp; vùng lưu trữ phục vụ dữ liệu giữ lại ở lesson 352; hai vùng này mượn lẫn nhau được nhưng có mức sàn. Ngoài ra còn bộ nhớ ngoài vùng quản lý cho thư viện gốc và cho mã Python, thứ thường bị quên khi đặt cấu hình. Bốn nguyên nhân hết bộ nhớ và cách phân biệt qua thông báo lỗi: một phân vùng quá lớn do lệch dữ liệu ở lesson 349, phát tán bảng quá lớn ở lesson 350, thu về dữ liệu lớn ở trình điều khiển theo lesson 344, và giữ lại quá nhiều. Tràn ra đĩa là cơ chế tự bảo vệ chứ lỗi: nó làm chậm nhưng cứu công việc, nên thấy tràn là tín hiệu cần chỉnh chứ cần báo động. Cách đọc thông báo lỗi để biết hết bộ nhớ ở trình điều khiển hay trình thực thi, và ở vùng nào.

**Outcome.** Từ một thông báo lỗi hết bộ nhớ, quy về đúng một trong bốn nguyên nhân và sửa đúng cấu hình hoặc đúng mã.

**Đánh giá.** Tầng *phân tích*. Objective là chẩn đoán từ thông báo lỗi, kỹ năng dùng trực tiếp khi trực. Kiểm bằng bốn sự cố tiêm sẵn tính giờ; đạt khi quy đúng ít nhất ba và sửa được ít nhất hai mà không chỉ tăng bộ nhớ.

**Lab.** Giảng viên tiêm bốn công việc hết bộ nhớ vì bốn nguyên nhân khác nhau, mỗi lần 12 phút. Với mỗi lần, đọc thông báo lỗi, quy nguyên nhân, sửa, và ghi lại đã sửa bằng cách nào. Đo dung lượng tràn đĩa trước và sau ở một công việc.

**Pitfalls.** Tăng bộ nhớ cho mọi lỗi hết bộ nhớ · quên bộ nhớ ngoài vùng quản lý khi chạy Python · coi tràn ra đĩa là lỗi cần loại bỏ hoàn toàn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Quy đúng ≥ 3/4 nguyên nhân, và ≥ 2/4 trường hợp được sửa bằng cách khác chứ chỉ tăng bộ nhớ.

### Lesson 354 · Structured Streaming - the micro-batch engine in depth `TH`
**Prerequisites.** Lesson 353

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài trả nợ phần nội bộ mà lesson 327 chỉ đối chiếu ở mức khái niệm. Mô hình bảng không giới hạn: luồng đến được xem như các dòng liên tục thêm vào một bảng, và truy vấn chạy trên bảng đó như truy vấn theo lô, nên phần lớn API dùng chung với xử lý lô. Cơ chế thực thi theo lô vi mô: engine chia luồng thành các lô nhỏ, mỗi lô là một công việc Spark đầy đủ với các giai đoạn và xáo trộn như đã học, và đây là lý do độ trễ sàn bị neo vào chu kỳ lô. Bốn khái niệm ở M32 ánh xạ sang đâu: thời gian sự kiện và dấu nước khai báo trực tiếp, cửa sổ dùng cùng cú pháp với lô, trạng thái giữ trong kho trạng thái của trình thực thi, và điểm kiểm tra ghi ra kho bền cùng offset nguồn đúng nguyên tắc ở lesson 321. Ba chế độ xuất và điều kiện dùng. Bên ghi cho đúng một lần đòi đích bất biến, đúng kết luận đã rút ở lesson 322.

**Outcome.** Cài đặt một công việc Structured Streaming có trạng thái, chỉ ra bốn khái niệm của M32 nằm ở đâu, và đo độ trễ sàn theo chu kỳ lô.

**Đánh giá.** Tầng *áp dụng*. Objective là chuyển ngữ nghĩa đã nắm ở M32 sang một engine cụ thể, có đối chứng sẵn từ lesson 327. Kiểm bằng so kết quả với bản Flink và bảng độ trễ; đạt khi kết quả nghiệp vụ khớp và ánh xạ bốn khái niệm đúng cả bốn.

**Lab.** Cài lại công việc ở lesson 319 bằng Structured Streaming, chạy trên cùng dữ liệu và đối soát với kết quả bản Flink. Chỉ ra vị trí của bốn khái niệm trong mã và trong cấu hình. Đo độ trễ đầu cuối ở ba chu kỳ lô. Giết tiến trình và khôi phục từ điểm kiểm tra, đối soát.

**Pitfalls.** Coi Structured Streaming là engine luồng thuần · quên cấu hình điểm kiểm tra ra kho bền · dùng chế độ xuất sai với phép gộp có trạng thái · so độ trễ với Flink mà không nêu chu kỳ lô.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Kết quả nghiệp vụ khớp bản Flink, bốn khái niệm được định vị đúng, và bảng độ trễ ba chu kỳ lô có số.

### Lesson 355 · Cluster sizing, dynamic allocation and cost `TH`
**Prerequisites.** Lesson 354

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ước lượng quy mô cụm từ bốn đại lượng: dung lượng dữ liệu đọc, tỉ lệ phình khi giải nén và chuyển sang biểu diễn trong bộ nhớ, dung lượng xáo trộn, và cửa sổ thời gian cho phép. Hai cách chia sai phổ biến và hệ quả: nhiều trình thực thi rất nhỏ thì chi phí lập lịch và bản sao dữ liệu phát tán tăng; ít trình thực thi rất lớn thì dọn rác lâu và một trình thực thi chết mất nhiều việc. Khoảng hợp lý cho số lõi mỗi trình thực thi và lý do. Cấp phát động thêm bớt trình thực thi theo nhu cầu thật, tiết kiệm rõ với công việc có tải không đều, nhưng cần dịch vụ xáo trộn ngoài để dữ liệu xáo trộn không mất khi trình thực thi bị thu hồi. Máy giá thấp có thể bị thu hồi giữa chừng: rẻ hơn nhiều nhưng chỉ dùng được khi công việc chịu được mất trình thực thi, nên hợp với xử lý lô và không hợp với luồng độ trễ thấp. Tính chi phí cho một lần chạy và so các cấu hình bằng tiền chứ bằng thời gian.

**Outcome.** Ước lượng cấu hình cụm cho một công việc cho trước và so ba cấu hình bằng cả thời gian lẫn chi phí tiền.

**Đánh giá.** Tầng *đánh giá*. Objective đòi tối ưu theo hai mục tiêu mâu thuẫn là thời gian và tiền, chứ chỉ theo thời gian. Kiểm bằng bảng ba cấu hình; đạt khi có cả hai đại lượng và lựa chọn nêu rõ đang tối ưu theo mục tiêu nào.

**Lab.** Ước lượng cấu hình cho một công việc đọc 500 GB. Chạy ba cấu hình khác nhau về số và kích thước trình thực thi, đo thời gian và tính chi phí. Bật cấp phát động trên công việc có tải không đều và đo tiết kiệm. Chạy một lần trên máy giá thấp và ghi lại chuyện gì xảy ra khi một trình thực thi bị thu hồi.

**Pitfalls.** Chọn cấu hình chỉ theo thời gian chạy · dùng trình thực thi rất lớn cho chắc · bật cấp phát động mà không có dịch vụ xáo trộn ngoài · dùng máy giá thấp cho công việc luồng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng ba cấu hình có cả thời gian lẫn chi phí, và lựa chọn nêu rõ mục tiêu tối ưu kèm số hỗ trợ.

### Lesson 356 · Spark on the reference pipeline - batch and streaming `DA`
**Prerequisites.** Lesson 355

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Bài dự án khép module: chuyển phần biến đổi của pipeline tham chiếu sang Spark, cả nhánh theo lô lẫn nhánh luồng, đọc và ghi trên bố trí lakehouse ở lesson 341. Yêu cầu bắt buộc: nhánh lô và nhánh luồng dùng chung phần lớn mã biến đổi, vì đó là lý do chính để chọn một engine làm cả hai. Ba ngưỡng hiệu năng phải đạt và đều đo được: thời gian chạy nhánh lô trong cửa sổ cho trước, độ trễ đầu cuối nhánh luồng dưới ngưỡng, và chi phí một lần chạy dưới ngân sách. Hồ sơ nộp kèm: kế hoạch thực thi của hai truy vấn nặng nhất, ảnh chụp giao diện cho thấy phân bố tác vụ đều, bảng cấu hình cụm kèm lý do, và nhật ký một lần chẩn đoán có thật trong quá trình làm. Điểm quan trọng khi chấm: mọi tối ưu phải dẫn được về một quan sát trong giao diện hoặc kế hoạch, không chấp nhận tối ưu vì đọc được ở đâu đó.

**Outcome.** Nộp pipeline chạy được cả hai nhánh đạt ba ngưỡng, với mỗi tối ưu dẫn được về một quan sát cụ thể.

**Đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module thành một hệ chạy được dưới ràng buộc hiệu năng và chi phí. Kiểm bằng chạy thật trên dữ liệu chuẩn cộng rà soát hồ sơ; đạt khi cả ba ngưỡng đạt và mọi tối ưu có bằng chứng.

**Lab.** Chuyển phần biến đổi sang Spark cho cả hai nhánh. Đạt ba ngưỡng. Nộp hồ sơ gồm hai kế hoạch thực thi, ảnh chụp phân bố tác vụ, bảng cấu hình kèm lý do, và một nhật ký chẩn đoán. Rà soát chéo: một học viên khác chọn một tối ưu bất kỳ và bạn phải chỉ ra quan sát dẫn tới nó.

**Pitfalls.** Sao chép cấu hình từ bài viết trên mạng · tối ưu trước khi đo · để nhánh lô và nhánh luồng thành hai bản mã rời nhau · nộp số mà không nộp kế hoạch thực thi.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Cả ba ngưỡng đạt trên dữ liệu chuẩn, hai nhánh dùng chung phần biến đổi, và mọi tối ưu trong hồ sơ dẫn được về một quan sát.

# MODULE 35 · DOCKER

**Lessons 357–364 · 16 giờ**

| | |
|---|---|
| **Objective cấp module** | Đóng gói được một thành phần dữ liệu thành ảnh chạy lại giống nhau trên máy khác, và giải thích mọi dòng trong tệp định nghĩa bằng cơ chế lớp |
| **Tiền đề** | M34 |
| **Exit criterion** | Người khác chạy ảnh của bạn trên máy họ cho cùng kết quả, ảnh dưới ngưỡng dung lượng, và không có bí mật nào nằm trong lớp ảnh |
| **Kỹ năng SFIA** | `SYSP` mức 3 · `PROG` mức 3 |
| **Chế độ hỏng** | Chép một tệp định nghĩa mẫu, cài mọi thứ trong một lớp, nhét mật khẩu vào biến môi trường lúc dựng, rồi đẩy ảnh có bí mật lên kho công khai |

Mức `A`. Module ngắn vì nó phục vụ ba module sau chứ đứng riêng: Kubernetes ở M36 chạy ảnh, cloud ở M37 triển khai ảnh, và mọi lab từ đây trở đi đóng gói bằng ảnh.

Lesson 91 đã đặt tiêu chí *clone, một lệnh, cùng kết quả*; module này là cách đạt tiêu chí đó khi thành phần có phụ thuộc hệ thống chứ chỉ thư viện Python.

### Lesson 357 · Why containers - the dependency problem and what an image is `LT`
**Prerequisites.** Module 35: M34

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài toán gốc đã gặp nhiều lần: mã chạy trên máy này và hỏng trên máy kia vì phiên bản thư viện hệ thống, biến môi trường hoặc phiên bản runtime khác nhau. Môi trường ảo Python ở lesson 89 giải phần thư viện Python nhưng không giải phần hệ thống, và phần lớn công cụ dữ liệu đều có phụ thuộc hệ thống. Ảnh là một hệ tệp đóng gói sẵn cộng siêu dữ liệu về lệnh chạy; container là một tiến trình chạy trên nhân của máy chủ nhưng nhìn thấy hệ tệp của ảnh. Phân biệt với máy ảo: container dùng chung nhân nên nhẹ và khởi động nhanh, đổi lại không cách ly bằng máy ảo và phải cùng loại nhân. Ba thứ container **không** giải: không làm mã chạy nhanh hơn, không sửa lỗi phụ thuộc mà chỉ đóng băng chúng, và không tự cho khả năng mở rộng. Vì sao điều này quan trọng với dữ liệu: một công việc Spark hay một trình nối có hàng chục phụ thuộc hệ thống, nên đóng gói là cách duy nhất để chạy lại được sau một năm.

**Outcome.** Giải thích khác biệt giữa ảnh và container, và chỉ ra ba loại phụ thuộc mà môi trường ảo không giải được còn container thì có.

**Đánh giá.** Tầng *hiểu*. Bài mở module, nối vấn đề đã trải qua ở M8 với một cơ chế mới. Kiểm bằng bài giải thích cộng một thí nghiệm tái hiện; đạt khi tái hiện được lỗi phụ thuộc hệ thống và chứng minh container sửa được.

**Lab.** Viết một script phụ thuộc vào một thư viện hệ thống ở phiên bản cụ thể. Chạy trên hai máy có phiên bản khác nhau và ghi lại lỗi. Đóng gói thành ảnh và chạy lại trên cả hai máy. So thời gian khởi động container với thời gian khởi động một máy ảo.

**Pitfalls.** Nghĩ container là máy ảo nhẹ · tin rằng đóng gói làm mã nhanh hơn · dùng container mà vẫn phụ thuộc vào tệp trên máy chủ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tái hiện được lỗi phụ thuộc hệ thống trên hai máy, bản đóng gói chạy giống nhau trên cả hai, và nêu đúng ba thứ container không giải.

### Lesson 358 · Images, layers and a Dockerfile that rebuilds fast `TH`
**Prerequisites.** Lesson 357

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ảnh gồm nhiều lớp xếp chồng, mỗi lệnh trong tệp định nghĩa tạo một lớp, và lớp được lưu đệm theo thứ tự. Hệ quả chi phối cách viết: **đặt thứ ít thay đổi lên trước, thứ hay thay đổi xuống sau**, vì một lớp đổi thì mọi lớp sau nó phải dựng lại. Sai lầm điển hình là chép toàn bộ mã nguồn trước rồi mới cài phụ thuộc, khiến mỗi lần sửa một dòng mã là cài lại toàn bộ phụ thuộc. Tệp bỏ qua lúc dựng quyết định thứ gì được gửi tới trình dựng, và thiếu nó thì thư mục dữ liệu hàng gigabyte bị gửi theo. Phân biệt hai lệnh chạy lệnh lúc khởi động và lý do chọn dạng mảng thay vì dạng chuỗi: dạng chuỗi chạy qua shell nên tiến trình chính không nhận được tín hiệu dừng, dẫn thẳng tới vấn đề ở lesson 359. Ghim phiên bản ảnh nền bằng thẻ cụ thể chứ thẻ mới nhất, vì thẻ mới nhất làm bản dựng hôm nay khác bản dựng hôm qua và phá tính tái lập.

**Outcome.** Viết tệp định nghĩa có thứ tự lớp đúng, và chứng minh bằng số đo rằng sửa một dòng mã không kích hoạt cài lại phụ thuộc.

**Đánh giá.** Tầng *áp dụng*. Objective là một kỹ năng viết có kết quả đo được bằng thời gian dựng lại. Kiểm bằng cặp số đo; đạt khi thời gian dựng lại sau khi sửa mã giảm rõ rệt và ảnh nền được ghim phiên bản.

**Lab.** Viết hai tệp định nghĩa cho cùng một ứng dụng: một bản chép mã trước, một bản cài phụ thuộc trước. Sửa một dòng mã và đo thời gian dựng lại của cả hai. Thêm tệp bỏ qua và đo lại dung lượng gửi tới trình dựng. Đổi thẻ ảnh nền từ mới nhất sang bản cụ thể.

**Pitfalls.** Chép mã trước khi cài phụ thuộc · dùng thẻ mới nhất · quên tệp bỏ qua nên gửi cả thư mục dữ liệu · dùng dạng chuỗi cho lệnh khởi động.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Thời gian dựng lại sau khi sửa mã giảm rõ rệt có số, dung lượng gửi tới trình dựng giảm, và ảnh nền đã ghim phiên bản.

### Lesson 359 · Running containers - processes, signals and exit codes `TH`
**Prerequisites.** Lesson 358

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Container là một tiến trình, nên mọi thứ đã học về tiến trình ở M3 áp dụng nguyên vẹn, và ba chi tiết hay bị bỏ qua gây hỏng trong sản xuất. Một là tiến trình số một: tiến trình chính trong container nhận tín hiệu dừng, nên nếu nó là shell thì tín hiệu không tới được chương trình thật và container bị giết cứng sau thời gian chờ, làm công việc đang ghi dở bị cắt ngang. Hai là mã thoát: hệ điều phối dựa vào mã thoát để biết công việc thành công hay thất bại, nên chương trình phải trả mã đúng, đúng yêu cầu đã đặt ở lesson 96. Ba là nhật ký ra luồng chuẩn chứ ghi tệp trong container, vì hệ thu thập nhật ký đọc luồng chuẩn và tệp trong container biến mất khi container chết. Kiểm tra sức khoẻ và khác biệt giữa kiểm tra tiến trình còn sống với kiểm tra ứng dụng còn phục vụ được. Giới hạn tài nguyên ở mức container và điều gì xảy ra khi vượt giới hạn bộ nhớ.

**Outcome.** Đóng gói một công việc sao cho nó dừng sạch khi nhận tín hiệu, trả đúng mã thoát, và ghi nhật ký ra luồng chuẩn.

**Đánh giá.** Tầng *áp dụng*. Objective là ba yêu cầu vận hành kiểm được bằng thí nghiệm dừng và đọc mã thoát. Kiểm bằng ba phép thử; đạt khi cả ba đạt và container dừng trong thời gian chờ.

**Lab.** Đóng gói một công việc ghi dữ liệu. Gửi tín hiệu dừng giữa chừng ở hai bản, một dùng dạng chuỗi và một dùng dạng mảng, đo thời gian dừng và kiểm tra dữ liệu có bị cắt dở không. Cho công việc thất bại và kiểm mã thoát. Đặt giới hạn bộ nhớ thấp và ghi lại sự kiện khi vượt.

**Pitfalls.** Dùng shell làm tiến trình chính · nuốt ngoại lệ rồi vẫn thoát mã không · ghi nhật ký vào tệp trong container · không đặt giới hạn tài nguyên.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bản dạng mảng dừng sạch trong thời gian chờ và dữ liệu không cắt dở, mã thoát đúng ở cả hai trường hợp, và nhật ký đọc được từ luồng chuẩn.

### Lesson 360 · Networking and volumes - where the data actually lives `TH`
**Prerequisites.** Lesson 359

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hệ tệp của container biến mất khi container bị xoá, nên mọi dữ liệu cần sống lâu hơn phải nằm ngoài. Hai cách đưa ra ngoài và khác biệt thực tế: khối lượng do nền tảng quản lý, hợp cho dữ liệu; gắn thư mục máy chủ, tiện khi phát triển nhưng buộc container phụ thuộc vào bố trí máy chủ nên không dùng trong sản xuất. Quyền sở hữu tệp giữa người dùng trong container và người dùng trên máy chủ là nguồn lỗi phổ biến khi ghi dữ liệu. Mạng: mỗi container có địa chỉ riêng trong mạng ảo, và các container cùng mạng gọi nhau bằng tên chứ bằng địa chỉ, nên phụ thuộc giữa các thành phần khai báo bằng tên dịch vụ. Cổng chỉ cần công bố ra ngoài khi có người ngoài mạng cần gọi vào. Vì sao container chạy Spark hoặc Kafka cần chú ý địa chỉ quảng bá: thành phần tự báo địa chỉ của mình cho bên khác, và báo sai thì bên ngoài không kết nối được dù cổng đã mở, đây là lỗi hay gặp nhất khi dựng cụm bằng container.

**Outcome.** Đóng gói một thành phần có trạng thái sao cho dữ liệu sống qua việc xoá và tạo lại container, và hai container gọi được nhau bằng tên.

**Đánh giá.** Tầng *áp dụng*. Objective là hai cấu hình kiểm được bằng thí nghiệm xoá và gọi. Kiểm bằng hai phép thử; đạt khi dữ liệu còn nguyên sau khi tạo lại và kết nối theo tên thành công.

**Lab.** Chạy PostgreSQL trong container với khối lượng. Ghi dữ liệu, xoá container, tạo lại và kiểm dữ liệu còn nguyên. Chạy thêm một container ứng dụng, cho nó kết nối tới cơ sở dữ liệu bằng tên dịch vụ. Cố ý đặt sai địa chỉ quảng bá của một thành phần và ghi lại triệu chứng.

**Pitfalls.** Lưu dữ liệu trong hệ tệp container · gắn thư mục máy chủ trong sản xuất · công bố mọi cổng ra ngoài · quên quyền sở hữu tệp nên container không ghi được.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Dữ liệu còn nguyên sau khi xoá và tạo lại, hai container gọi nhau bằng tên thành công, và mô tả đúng triệu chứng khi địa chỉ quảng bá sai.

### Lesson 361 · Multi-stage builds and image size `TH`
**Prerequisites.** Lesson 360

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ảnh lớn tốn ba thứ: thời gian tải về mỗi lần khởi động một tác vụ mới, dung lượng kho ảnh, và diện tích bị tấn công vì càng nhiều gói càng nhiều lỗ hổng. Dựng nhiều giai đoạn tách môi trường biên dịch khỏi môi trường chạy: giai đoạn đầu có trình biên dịch và công cụ phát triển, giai đoạn cuối chỉ chép kết quả sang một ảnh nền tối giản. Với công cụ dữ liệu thường giảm được nhiều lần dung lượng. Ba kỹ thuật bổ sung: chọn ảnh nền gọn, gộp các lệnh cài đặt và dọn bộ đệm gói trong cùng một lớp vì dọn ở lớp sau không xoá được byte ở lớp trước, và không cài công cụ gỡ lỗi vào ảnh sản xuất. Quét lỗ hổng như một bước trong tích hợp liên tục và ngưỡng chặn phát hành. Cảnh báo về ảnh nền quá tối giản với công cụ dữ liệu: một số thư viện cần thư viện hệ thống chuẩn nên chọn nền sai làm mất nhiều giờ gỡ lỗi khó hiểu.

**Outcome.** Giảm dung lượng ảnh xuống dưới ngưỡng bằng dựng nhiều giai đoạn mà ứng dụng vẫn chạy đúng, kèm kết quả quét lỗ hổng.

**Đánh giá.** Tầng *áp dụng*. Objective là một tối ưu có ngưỡng rõ và có ràng buộc không được làm hỏng chức năng. Kiểm bằng cặp số đo cộng bộ kiểm thử; đạt khi dưới ngưỡng, kiểm thử xanh và số lỗ hổng mức cao bằng không.

**Lab.** Đo dung lượng ảnh ban đầu. Chuyển sang dựng hai giai đoạn, đo lại. Gộp lệnh cài và dọn bộ đệm trong một lớp, đo lại. Chạy bộ kiểm thử trên ảnh cuối. Quét lỗ hổng trước và sau, lập bảng.

**Pitfalls.** Dọn bộ đệm ở lớp sau rồi tưởng đã giảm dung lượng · chọn ảnh nền quá tối giản rồi thiếu thư viện hệ thống · để công cụ gỡ lỗi trong ảnh sản xuất.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Dung lượng dưới ngưỡng, bộ kiểm thử xanh trên ảnh cuối, và bảng quét lỗ hổng cho thấy không còn lỗ hổng mức cao.

### Lesson 362 · Secrets and configuration in containers `TH`
**Prerequisites.** Lesson 361

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Quy tắc đã đặt từ lesson 89 và 2038 áp dụng ở đây với một cái bẫy riêng: **mọi thứ đưa vào lúc dựng đều nằm lại trong lớp ảnh và ai tải ảnh về đều đọc được**, kể cả khi lệnh sau đó xoá tệp đi, vì lớp trước vẫn còn. Nên không bao giờ truyền bí mật bằng đối số dựng hoặc chép tệp bí mật vào ảnh. Ba cách đúng theo thứ tự ưu tiên: lấy từ kho bí mật lúc chạy, gắn vào lúc chạy dưới dạng tệp tạm, và truyền qua biến môi trường lúc chạy, cách cuối tiện nhất nhưng biến môi trường lộ ra khi ai đó xem thông tin tiến trình. Phân biệt cấu hình với bí mật: cấu hình đưa vào ảnh được, bí mật thì không. Cách kiểm chứng ảnh không chứa bí mật: duyệt từng lớp và tìm chuỗi, và đưa bước quét này vào tích hợp liên tục. Xử lý khi phát hiện bí mật đã vào ảnh và ảnh đã đẩy lên kho: xoay bí mật là bắt buộc, xoá ảnh là chưa đủ.

**Outcome.** Đưa bí mật vào container đúng cách và chứng minh bằng cách duyệt lớp rằng ảnh không chứa bí mật nào.

**Đánh giá.** Tầng *áp dụng*. Objective là một yêu cầu bảo mật kiểm được bằng phép quét khách quan. Kiểm bằng quét lớp; đạt khi ảnh sạch và quy trình xử lý khi lộ được viết ra.

**Lab.** Cố ý dựng một ảnh có mật khẩu truyền qua đối số dựng, rồi duyệt lớp và trích ra mật khẩu đó để tự thấy vấn đề. Dựng lại bằng cách đưa bí mật lúc chạy. Quét lại và chứng minh sạch. Thêm bước quét bí mật vào quy trình tích hợp liên tục. Viết quy trình bốn bước khi phát hiện bí mật đã bị đẩy lên kho.

**Pitfalls.** Truyền bí mật bằng đối số dựng · xoá tệp bí mật ở lớp sau rồi tưởng đã an toàn · chỉ xoá ảnh mà không xoay bí mật · trộn lẫn cấu hình và bí mật.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Trích được mật khẩu từ ảnh sai để chứng minh vấn đề, ảnh đúng quét sạch, và quy trình xử lý khi lộ có đủ bước xoay bí mật.

### Lesson 363 · Compose for a local data stack `TH`
**Prerequisites.** Lesson 362

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Một hệ dữ liệu cần nhiều thành phần chạy cùng lúc, và dựng bằng tay từng cái là cách không lặp lại được. Tệp khai báo nhiều dịch vụ mô tả toàn bộ ngăn xếp ở một chỗ: ảnh, biến môi trường, khối lượng, mạng, và phụ thuộc khởi động. Phụ thuộc khởi động có một bẫy: khai báo thứ tự chỉ đảm bảo container khởi động theo thứ tự, **không đảm bảo dịch vụ bên trong đã sẵn sàng nhận kết nối**, nên phải dùng kiểm tra sức khoẻ ở lesson 359 hoặc vòng lặp chờ trong mã. Giá trị thật của cách này với chương trình: mọi lab từ M11 tới M34 dựng lại được bằng một lệnh, nên tiêu chí ở lesson 91 đạt được cho cả ngăn xếp chứ chỉ cho một script. Ranh giới phải giữ: cách này dành cho môi trường phát triển và kiểm thử tích hợp, không dành cho sản xuất, vì không có khả năng tự phục hồi, không có mở rộng, không có lập lịch, và đó là lý do M36 tồn tại.

**Outcome.** Dựng lại toàn bộ ngăn xếp dữ liệu của mình bằng một lệnh trên máy trống, và xử lý đúng vấn đề dịch vụ chưa sẵn sàng.

**Đánh giá.** Tầng *áp dụng*. Objective là tiêu chí *một lệnh, cùng kết quả* áp cho nhiều dịch vụ. Kiểm bằng phép thử trên máy trống do người khác chạy; đạt khi lệnh duy nhất dựng xong và bộ kiểm thử tích hợp xanh.

**Lab.** Viết tệp khai báo cho ngăn xếp gồm PostgreSQL, Kafka, kho đối tượng và một công việc xử lý. Cố ý bỏ kiểm tra sức khoẻ và quan sát công việc chết vì kết nối sớm. Thêm kiểm tra sức khoẻ và chạy lại. Đưa cho một học viên khác chạy trên máy trống.

**Pitfalls.** Dựa vào thứ tự khởi động thay vì kiểm tra sức khoẻ · ghim dữ liệu vào thư mục máy chủ · dùng cách này cho sản xuất · để cấu hình khác nhau giữa các máy.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Một lệnh dựng xong ngăn xếp trên máy trống của người khác, và bộ kiểm thử tích hợp xanh ở lần chạy đầu.

### Lesson 364 · Containerising the reference pipeline `TH`
**Prerequisites.** Lesson 363

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài khép module: đóng gói mọi thành phần của pipeline tham chiếu thành ảnh và dựng lại toàn bộ bằng một lệnh. Danh mục kiểm phải qua cho từng ảnh: ảnh nền ghim phiên bản, dựng nhiều giai đoạn, không chứa bí mật, chạy bằng người dùng không phải quản trị, tiến trình chính nhận được tín hiệu, nhật ký ra luồng chuẩn, kiểm tra sức khoẻ có nghĩa, và có nhãn ghi phiên bản mã nguồn. Gắn thẻ ảnh theo quy ước có thể truy ngược: thẻ theo mã nguồn chứ chỉ thẻ mới nhất, vì thẻ mới nhất làm không biết môi trường đang chạy bản nào. Đẩy ảnh lên kho riêng và đo thời gian tải về, vì thời gian đó cộng vào thời gian khởi động mỗi tác vụ ở M36. Bằng chứng nộp kèm: bảng danh mục kiểm cho từng ảnh, dung lượng từng ảnh, và kết quả một người khác dựng lại trên máy trống.

**Outcome.** Đóng gói toàn bộ pipeline đạt danh mục kiểm tám điểm cho mọi ảnh, và người khác dựng lại được trên máy trống.

**Đánh giá.** Tầng *áp dụng*. Bài tổng hợp module thành một bộ ảnh đạt chuẩn. Kiểm bằng danh mục kiểm cộng phép thử dựng lại; đạt khi mọi ảnh qua cả tám điểm và phép thử dựng lại thành công.

**Lab.** Đóng gói mọi thành phần. Lập bảng danh mục kiểm tám điểm cho từng ảnh. Gắn thẻ theo mã nguồn và đẩy lên kho riêng. Đo dung lượng và thời gian tải về từng ảnh. Đưa cho một học viên khác dựng lại trên máy trống và ghi lại mọi chỗ họ phải hỏi.

**Pitfalls.** Chạy container bằng quyền quản trị · gắn thẻ mới nhất · bỏ qua kiểm tra sức khoẻ cho thành phần không có cổng · nộp mà chưa ai dựng lại thử.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mọi ảnh qua cả tám điểm trong danh mục kiểm, và người khác dựng lại thành công trên máy trống mà không phải hỏi câu nào.

# MODULE 36 · KUBERNETES

**Lessons 365–374 · 20 giờ**

| | |
|---|---|
| **Objective cấp module** | Chạy được khối lượng công việc dữ liệu trên Kubernetes ở mức `B`, và chẩn đoán được một tác vụ không khởi động bằng sự kiện chứ bằng phỏng đoán |
| **Tiền đề** | M35 |
| **Exit criterion** | Một công việc theo lịch và một dịch vụ có trạng thái chạy đúng, sống qua việc xoá một tác vụ, và ba sự cố khởi động được chẩn đoán đúng |
| **Kỹ năng SFIA** | `SYSP` mức 3 · `NTAS` mức 3 |
| **Chế độ hỏng** | Chép tệp khai báo mẫu, không đặt yêu cầu và giới hạn tài nguyên, rồi tác vụ bị giết vì hết bộ nhớ hoặc chiếm hết nút mà không ai hiểu vì sao |

Mức `B`: chạy được khối lượng công việc và chẩn đoán được, không yêu cầu vận hành cụm.

Module trả lời trước một câu hỏi thực tế: phần lớn đội dữ liệu ở Việt Nam không tự vận hành Kubernetes mà dùng bản quản lý trên đám mây ở M37. Nhưng đọc được sự kiện và hiểu vòng lặp điều hoà là yêu cầu tối thiểu để chẩn đoán khi công việc của mình không chạy, và đó là phạm vi của module.

### Lesson 365 · What Kubernetes adds over Docker, and what it costs `LT`
**Prerequisites.** Module 36: M35

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Cách khai báo nhiều dịch vụ ở lesson 363 dừng lại ở bốn chỗ, và bốn chỗ đó chính là bốn thứ Kubernetes thêm vào: tự khởi động lại khi tiến trình chết và tự thay thế khi một máy chết; chạy nhiều bản sao và chia tải; xếp tác vụ lên máy còn tài nguyên thay vì người tự chọn; và cập nhật phiên bản mà không dừng phục vụ. Khái niệm trung tâm là **trạng thái mong muốn và vòng lặp điều hoà**: người khai báo muốn có gì, hệ liên tục so hiện trạng với mong muốn và hành động để thu hẹp khoảng cách. Hệ quả cần nhớ ngay: xoá một tác vụ do bộ điều khiển quản lý thì nó mọc lại, vì mong muốn không đổi. Cái giá phải nói thẳng: thêm rất nhiều khái niệm, cần người vận hành, và với đội nhỏ chạy vài công việc theo lịch thì cron trên một máy hoặc bộ điều phối ở M22 đơn giản hơn nhiều. Ba dấu hiệu cho thấy thật sự cần.

**Outcome.** Nêu bốn năng lực Kubernetes thêm vào so với chạy container đơn lẻ, và quyết định một tình huống cho trước có cần dùng không.

**Đánh giá.** Tầng *hiểu*. Bài mở module, đặt đúng kỳ vọng trước khi vào chi tiết. Kiểm bằng bốn tình huống trong đó ít nhất hai không nên dùng; đạt khi quyết định đúng ít nhất ba kèm lý do dẫn từ bốn năng lực.

**Lab.** Dựng một cụm một nút cục bộ. Chạy một tác vụ, xoá nó bằng tay và quan sát nó mọc lại. Dừng tiến trình bên trong và quan sát khởi động lại. Cho bốn tình huống và quyết định có nên dùng Kubernetes không.

**Pitfalls.** Dùng Kubernetes vì nó phổ biến · nghĩ nó thay thế được bộ điều phối · ngạc nhiên vì tác vụ xoá rồi mọc lại.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Quyết định đúng ≥ 3/4 tình huống kèm lý do, và quan sát được tác vụ mọc lại sau khi xoá.

### Lesson 366 · Pods, deployments and the reconciliation loop `LT`
**Prerequisites.** Lesson 365

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Tác vụ là đơn vị nhỏ nhất được xếp lịch, gồm một hoặc vài container dùng chung mạng và khối lượng. Không ai tạo tác vụ trực tiếp trong sản xuất; người ta khai báo một đối tượng cấp cao rồi bộ điều khiển tạo tác vụ. Ba loại đối tượng cho ba loại khối lượng công việc dữ liệu: triển khai cho dịch vụ không trạng thái với các bản sao thay thế được cho nhau; tập có trạng thái cho thành phần cần danh tính ổn định và kho riêng như cơ sở dữ liệu; công việc và công việc theo lịch cho tác vụ chạy rồi kết thúc, đúng dạng phần lớn công việc dữ liệu. Vòng lặp điều hoà chạy liên tục nên mọi thay đổi là khai báo chứ mệnh lệnh: sửa tệp khai báo và áp dụng, chứ gõ lệnh sửa trực tiếp, vì lệnh trực tiếp bị ghi đè ở lần áp dụng sau và làm hiện trạng lệch khỏi mã nguồn. Vòng đời tác vụ và các trạng thái, trong đó trạng thái chờ là trạng thái cần chẩn đoán ở lesson 373.

**Outcome.** Chọn đúng loại đối tượng cho ba khối lượng công việc dữ liệu và giải thích bằng yêu cầu danh tính và vòng đời.

**Đánh giá.** Tầng *hiểu*. Bài lý thuyết chuẩn bị cho các bài thực hành; chưa đòi vận hành. Kiểm bằng ba khối lượng công việc; đạt khi chọn đúng cả ba kèm lý do dẫn từ yêu cầu danh tính hoặc vòng đời.

**Lab.** Khai báo và chạy cả ba loại đối tượng: một dịch vụ không trạng thái, một cơ sở dữ liệu, và một công việc chạy rồi kết thúc. Với mỗi loại, xoá một tác vụ và quan sát hệ phản ứng. Sửa trực tiếp bằng lệnh rồi áp dụng lại tệp khai báo và quan sát thay đổi bị ghi đè.

**Pitfalls.** Dùng triển khai cho cơ sở dữ liệu · tạo tác vụ trực tiếp · sửa bằng lệnh trong sản xuất · dùng dịch vụ chạy mãi cho việc lẽ ra chạy rồi kết thúc.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba loại đối tượng chạy đúng, chọn đúng cả ba kèm lý do, và quan sát được thay đổi thủ công bị ghi đè.

### Lesson 367 · Services, DNS and reaching a workload `TH`
**Prerequisites.** Lesson 366

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Tác vụ có địa chỉ riêng nhưng địa chỉ đó đổi mỗi lần tác vụ được tạo lại, nên không thành phần nào được phép nhớ địa chỉ tác vụ. Dịch vụ là một tên ổn định trỏ tới tập tác vụ đang khoẻ, và chọn tác vụ nào bằng nhãn chứ bằng danh sách, nên tác vụ mới có đúng nhãn là tự vào tập. Ba loại dịch vụ theo phạm vi truy cập: chỉ trong cụm, mở cổng trên mọi nút, và xin một bộ cân bằng tải từ đám mây. Tên miền nội bộ theo quy ước cố định, nên thành phần gọi nhau bằng tên chứ bằng địa chỉ, đúng như ở lesson 360 nhưng ở quy mô cụm. Dịch vụ không có địa chỉ ảo dùng cho tập có trạng thái, vì ở đó mỗi bản sao cần được gọi đích danh, ví dụ ba nút Kafka. Ba nguyên nhân gọi không tới và cách phân biệt: nhãn không khớp, cổng khai báo sai, và tác vụ chưa qua kiểm tra sẵn sàng nên bị loại khỏi tập.

**Outcome.** Cho hai thành phần gọi được nhau bằng tên dịch vụ, và chẩn đoán đúng một dịch vụ không tới được trong ba nguyên nhân.

**Đánh giá.** Tầng *áp dụng*. Objective là cấu hình cộng chẩn đoán, kiểm được bằng phép gọi thật. Kiểm bằng ba sự cố kết nối tiêm sẵn; đạt khi chẩn đoán đúng ít nhất hai và kết nối thành công sau khi sửa.

**Lab.** Cho một ứng dụng gọi tới PostgreSQL bằng tên dịch vụ. Giảng viên tiêm ba sự cố kết nối theo ba nguyên nhân. Với mỗi lần, chẩn đoán bằng cách xem tập đích của dịch vụ và nhãn tác vụ, rồi sửa. Dựng một tập có trạng thái ba bản sao và gọi đích danh từng bản.

**Pitfalls.** Nhớ địa chỉ tác vụ trong cấu hình · để nhãn dịch vụ lệch nhãn tác vụ · quên kiểm tra sẵn sàng nên tác vụ nhận lưu lượng khi chưa sẵn sàng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chẩn đoán đúng ≥ 2/3 sự cố kết nối và kết nối thành công sau khi sửa, gọi được đích danh từng bản sao của tập có trạng thái.

### Lesson 368 · Configuration and secrets - ConfigMap, Secret and the boundary `TH`
**Prerequisites.** Lesson 367

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Tách cấu hình khỏi ảnh là nguyên tắc đã đặt ở lesson 362; Kubernetes cung cấp hai đối tượng cho hai loại. Đối tượng cấu hình giữ giá trị không nhạy cảm, đối tượng bí mật giữ giá trị nhạy cảm, và điểm phải nói thẳng: **đối tượng bí mật mặc định chỉ mã hoá dạng chuỗi chứ mã hoá thật**, nên ai đọc được đối tượng là đọc được bí mật, và phải bật mã hoá khi lưu cộng kiểm soát quyền thì mới thực sự an toàn. Hai cách đưa vào tác vụ và khác biệt vận hành: biến môi trường thì đơn giản nhưng đổi giá trị phải khởi động lại tác vụ và giá trị lộ ra khi xem thông tin tiến trình; gắn thành tệp thì cập nhật được mà không khởi động lại, hợp cho cấu hình đổi thường xuyên. Ba nguyên tắc giữ: không đưa bí mật vào tệp khai báo rồi nộp vào kho mã, dùng kho bí mật ngoài cho môi trường sản xuất, và phân quyền đọc bí mật theo từng không gian tên.

**Outcome.** Đưa cấu hình và bí mật vào tác vụ đúng cách, và chứng minh bằng thực nghiệm rằng cập nhật cấu hình không đòi dựng lại ảnh.

**Đánh giá.** Tầng *áp dụng*. Objective là hai cấu hình có ràng buộc bảo mật kiểm được. Kiểm bằng thí nghiệm cập nhật cộng kiểm quyền; đạt khi đổi cấu hình không dựng lại ảnh và tài khoản không có quyền thì đọc bí mật thất bại.

**Lab.** Đưa cấu hình vào bằng cả hai cách. Đổi một giá trị và quan sát khác biệt giữa hai cách. Tạo một tài khoản chỉ có quyền đọc cấu hình, thử đọc bí mật và ghi lại kết quả. Giải mã một đối tượng bí mật để tự thấy nó chỉ là chuỗi mã hoá cơ bản.

**Pitfalls.** Tin rằng đối tượng bí mật đã được mã hoá · nộp tệp khai báo chứa bí mật vào kho mã · dùng biến môi trường cho cấu hình đổi thường xuyên.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Đổi cấu hình có hiệu lực mà không dựng lại ảnh, tài khoản thiếu quyền bị từ chối đọc bí mật, và tự giải mã được đối tượng bí mật.

### Lesson 369 · Resource requests, limits and the OOMKilled event `TH`
**Prerequisites.** Lesson 368

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hai con số cho mỗi tài nguyên và nhầm lẫn giữa chúng là nguyên nhân phổ biến nhất khiến công việc dữ liệu chạy sai trên Kubernetes. Yêu cầu là lượng tài nguyên bộ xếp lịch dành riêng và dùng để quyết định đặt tác vụ lên nút nào; giới hạn là trần lúc chạy. Hai tài nguyên hành xử khác nhau khi vượt trần: vượt trần CPU thì tác vụ bị bóp tốc độ, còn **vượt trần bộ nhớ thì tác vụ bị giết**, và sự kiện ghi lại lý do đó. Đây là chỗ nối thẳng với M34: một trình thực thi Spark bị giết vì vượt trần bộ nhớ nhìn từ trong Spark giống hệt lỗi hết bộ nhớ, nên phải xem sự kiện ở tầng Kubernetes mới phân biệt được. Đặt yêu cầu quá thấp thì nút bị nhồi quá tải và mọi thứ chậm; đặt quá cao thì lãng phí và tác vụ không xếp được. Cách đặt có căn cứ: đo mức dùng thật qua nhiều lần chạy rồi lấy phân vị cao làm yêu cầu, cộng biên cho giới hạn.

**Outcome.** Đặt yêu cầu và giới hạn từ mức dùng đo được, và phân biệt một tác vụ bị giết vì vượt trần bộ nhớ với một lỗi hết bộ nhớ trong ứng dụng.

**Đánh giá.** Tầng *phân tích*. Objective đòi phân biệt hai hiện tượng giống nhau ở bề mặt, kỹ năng chẩn đoán xuyên tầng. Kiểm bằng hai sự cố có biểu hiện giống nhau; đạt khi phân biệt đúng cả hai và dẫn được bằng chứng từ sự kiện.

**Lab.** Chạy một công việc Spark trong Kubernetes với giới hạn bộ nhớ thấp và quan sát sự kiện bị giết. Chạy lại với giới hạn đủ nhưng dữ liệu lệch khoá để gây lỗi hết bộ nhớ trong Spark. So hai thông báo và chỉ ra cách phân biệt. Đo mức dùng thật qua năm lần chạy rồi đặt lại hai con số.

**Pitfalls.** Đặt yêu cầu bằng giới hạn cho mọi tác vụ · không đặt gì cả · thấy tác vụ bị giết là tăng bộ nhớ mà chưa xem sự kiện · quên bộ nhớ ngoài vùng quản lý của Spark.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân biệt đúng hai trường hợp kèm bằng chứng từ sự kiện, và hai con số đặt lại dựa trên phân bố mức dùng qua năm lần chạy.

### Lesson 370 · Jobs and CronJobs for data workloads `TH`
**Prerequisites.** Lesson 369

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phần lớn khối lượng công việc dữ liệu là chạy rồi kết thúc chứ chạy mãi, nên hai đối tượng này là thứ dùng nhiều nhất. Công việc chạy tác vụ tới khi thành công, với số lần thử lại và thời hạn tối đa; mã thoát ở lesson 359 là thứ quyết định thành công hay thất bại, nên chương trình trả mã sai làm hệ hiểu sai. Công việc theo lịch chạy theo biểu thức thời gian, và bốn tham số quyết định hành vi khi lịch chồng nhau: chính sách đồng thời quyết định cho chạy song song hay bỏ qua hay thay thế, hạn khởi động muộn, và số bản ghi giữ lại cho lần thành công và thất bại. Ba khác biệt so với bộ điều phối ở M22 cần nói rõ để không dùng nhầm: không có đồ thị phụ thuộc, không có chạy bù theo khoảng dữ liệu, và không có giao diện xem lịch sử lần chạy. Mẫu thường dùng trong thực tế: bộ điều phối giữ đồ thị và kích hoạt, Kubernetes chạy từng tác vụ, tức là hai thứ bổ sung nhau chứ thay thế nhau.

**Outcome.** Chạy một công việc dữ liệu theo lịch với chính sách đồng thời đúng, và nêu ba việc bộ điều phối làm mà đối tượng này không làm.

**Đánh giá.** Tầng *áp dụng*. Objective là cấu hình đúng cộng nhận ra ranh giới công cụ. Kiểm bằng thí nghiệm lịch chồng cộng bài so sánh; đạt khi hành vi khi chồng lịch đúng như chính sách đã chọn và nêu đủ ba khác biệt.

**Lab.** Chạy một công việc theo lịch mỗi phút mà thời gian chạy hai phút. Thử cả ba chính sách đồng thời và ghi lại hành vi từng chính sách. Cho công việc thất bại và quan sát số lần thử lại. Viết ba khác biệt so với bộ điều phối ở M22.

**Pitfalls.** Dùng công việc theo lịch thay cho bộ điều phối khi có phụ thuộc · để chính sách mặc định rồi hai lần chạy cùng ghi một bảng · giữ quá nhiều bản ghi lịch sử làm nặng cụm.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba chính sách đồng thời cho ba hành vi quan sát được đúng như mô tả, và nêu đủ ba khác biệt so với bộ điều phối.

### Lesson 371 · Storage - persistent volumes and stateful workloads `TH`
**Prerequisites.** Lesson 370

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Tác vụ là thứ tạm thời nên dữ liệu phải nằm ngoài nó, giống hệt lập luận ở lesson 360 nhưng thêm một tầng trừu tượng vì cụm có nhiều nút. Ba khái niệm nối nhau: yêu cầu khối lượng là thứ người dùng khai báo cần bao nhiêu và kiểu truy cập gì; khối lượng bền là tài nguyên thật; lớp lưu trữ quyết định cách cấp phát tự động. Ba kiểu truy cập và hệ quả: chỉ một nút ghi là kiểu phổ biến nhất và cũng là ràng buộc khiến tác vụ bị buộc vào một nút; nhiều nút cùng đọc ghi cần hệ tệp mạng và chậm hơn. Tập có trạng thái cấp cho mỗi bản sao một khối lượng riêng và giữ nguyên khi tác vụ được tạo lại, nhờ danh tính ổn định ở lesson 366. Chính sách khi xoá quyết định dữ liệu còn hay mất, và để mặc định sai là cách mất dữ liệu nhanh. Với dữ liệu phân tích, cách đúng thường là dùng kho đối tượng ở M33 chứ khối lượng bền, và chỉ dùng khối lượng cho thành phần có trạng thái thật.

**Outcome.** Chạy một thành phần có trạng thái với khối lượng riêng cho từng bản sao, và chứng minh dữ liệu sống qua việc xoá tác vụ.

**Đánh giá.** Tầng *áp dụng*. Objective là cấu hình lưu trữ kiểm được bằng thí nghiệm xoá. Kiểm bằng phép thử xoá tác vụ; đạt khi dữ liệu còn nguyên và mỗi bản sao giữ đúng khối lượng của nó.

**Lab.** Dựng một tập có trạng thái ba bản sao, mỗi bản ghi dữ liệu riêng. Xoá một tác vụ và kiểm bản thay thế có gắn đúng khối lượng cũ. Đổi chính sách khi xoá và quan sát khác biệt. Viết hai câu về khi nào nên dùng kho đối tượng thay cho khối lượng bền.

**Pitfalls.** Dùng khối lượng bền cho dữ liệu phân tích · để chính sách khi xoá là xoá · chọn kiểu truy cập nhiều nút ghi khi không cần · quên rằng kiểu một nút ghi buộc tác vụ vào một nút.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Dữ liệu còn nguyên sau khi xoá tác vụ, mỗi bản sao gắn đúng khối lượng cũ, và nêu đúng tiêu chí chọn giữa hai cách lưu.

### Lesson 372 · Scheduling, node pools and cost control `TH`
**Prerequisites.** Lesson 371

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bộ xếp lịch chọn nút dựa trên yêu cầu tài nguyên ở lesson 369 cộng các ràng buộc người vận hành đặt. Ba cơ chế điều khiển vị trí theo mức độ cứng dần: chọn nút theo nhãn, quy tắc ưa thích hoặc bắt buộc, và cơ chế đánh dấu nút cùng khai báo chấp nhận để dành riêng một nhóm nút cho một loại khối lượng công việc. Với dữ liệu, ba lý do thật để can thiệp: tách khối lượng nặng bộ nhớ khỏi khối lượng nặng CPU, dành nút có đĩa nhanh cho thành phần có trạng thái, và đưa công việc lô lên nhóm nút giá thấp. Máy giá thấp bị thu hồi bất cứ lúc nào, nên chỉ đặt lên đó khối lượng chịu được mất tác vụ, đúng kết luận đã rút ở lesson 355. Tự mở rộng số nút và độ trễ của nó: thêm nút mất vài phút, nên công việc cần chạy ngay phải có nút dự phòng. Ba đòn bẩy giảm chi phí và cách đo hiệu quả từng đòn bẩy.

**Outcome.** Đặt khối lượng công việc lên đúng nhóm nút bằng cơ chế phù hợp, và định lượng mức giảm chi phí khi chuyển công việc lô sang nút giá thấp.

**Đánh giá.** Tầng *áp dụng*. Objective là cấu hình có kết quả đo được bằng tiền và bằng vị trí tác vụ. Kiểm bằng kiểm tra vị trí cộng bảng chi phí; đạt khi tác vụ nằm đúng nhóm và có số giảm chi phí.

**Lab.** Tạo hai nhóm nút khác cấu hình. Dùng cả ba cơ chế để đặt ba loại khối lượng công việc lên đúng nhóm và kiểm chứng vị trí thật. Chuyển công việc lô sang nhóm giá thấp, mô phỏng thu hồi một nút và quan sát công việc phục hồi. Tính chi phí trước và sau.

**Pitfalls.** Đặt thành phần có trạng thái lên nút giá thấp · dùng ràng buộc cứng rồi tác vụ không xếp được · quên độ trễ khi tự mở rộng · tính chi phí mà bỏ qua phần tài nguyên đặt trước không dùng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba loại khối lượng công việc nằm đúng nhóm nút, công việc lô phục hồi sau khi nút bị thu hồi, và có bảng chi phí trước sau.

### Lesson 373 · Observability - logs, events and diagnosing a pending pod `TH`
**Prerequisites.** Lesson 372

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba nguồn thông tin cho ba loại câu hỏi, và dùng sai nguồn là lý do chẩn đoán lâu. Nhật ký container trả lời ứng dụng đang làm gì, nhưng mất khi tác vụ bị xoá nên cần hệ thu thập tập trung. Sự kiện trả lời **vì sao tác vụ không khởi động được**, và đây là nguồn bị bỏ qua nhiều nhất dù nó nói thẳng nguyên nhân. Mô tả đối tượng trả lời cấu hình hiện tại và trạng thái từng container. Năm nguyên nhân làm tác vụ kẹt ở trạng thái chờ, phân biệt được ngay từ sự kiện: không đủ tài nguyên trên nút nào, ràng buộc vị trí không thoả, không xin được khối lượng, kéo ảnh thất bại vì sai tên hoặc thiếu quyền, và hết hạn mức trong không gian tên. Ba trạng thái hỏng khác và ý nghĩa: khởi động lại liên tục thường là tiến trình chết ngay, lỗi tạo container thường là cấu hình sai, và bị giết vì vượt trần bộ nhớ ở lesson 369. Quy trình chẩn đoán bốn bước theo thứ tự cố định.

**Outcome.** Chẩn đoán một tác vụ không khởi động về đúng nguyên nhân bằng sự kiện, trong giới hạn thời gian.

**Đánh giá.** Tầng *phân tích*. Objective là kỹ năng chẩn đoán dùng trực tiếp khi trực. Kiểm bằng năm sự cố tiêm sẵn tính giờ; đạt khi chẩn đoán đúng ít nhất bốn và mỗi lần dẫn được dòng sự kiện cụ thể.

**Lab.** Giảng viên tiêm năm tác vụ hỏng theo năm nguyên nhân, mỗi lần 8 phút. Với mỗi lần, chạy quy trình bốn bước, ghi dòng sự kiện dẫn tới kết luận, và sửa. Dựng thu thập nhật ký tập trung và chứng minh nhật ký của một tác vụ đã xoá vẫn đọc được.

**Pitfalls.** Xem nhật ký trước khi xem sự kiện · xoá tác vụ để thử lại rồi mất bằng chứng · khởi động lại triển khai theo phản xạ · không có thu thập nhật ký tập trung.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chẩn đoán đúng ≥ 4/5 sự cố trong giới hạn thời gian kèm dòng sự kiện, và đọc được nhật ký của tác vụ đã bị xoá.

### Lesson 374 · Running a data workload on Kubernetes `TH`
**Prerequisites.** Lesson 373

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài khép module: đưa hai khối lượng công việc thật của pipeline tham chiếu lên cụm. Một là công việc theo lịch chạy phần biến đổi theo lô, dùng ảnh đã đóng gói ở lesson 364. Hai là một thành phần có trạng thái, và phải nêu rõ quyết định tự vận hành hay dùng dịch vụ quản lý kèm lý do, vì với phần lớn đội thì tự vận hành cơ sở dữ liệu trên Kubernetes là quyết định tốn kém. Danh mục kiểm phải qua: yêu cầu và giới hạn đặt từ số đo, kiểm tra sức khoẻ và sẵn sàng có nghĩa, cấu hình và bí mật tách khỏi ảnh, khối lượng bền cho phần có trạng thái, nhật ký ra hệ tập trung, và chính sách khởi động lại phù hợp. Ba phép thử phải qua: xoá một tác vụ và hệ tự phục hồi, cập nhật phiên bản ảnh mà không mất dữ liệu, và một lần chẩn đoán sự cố có thật ghi lại thành sổ tay.

**Outcome.** Chạy được hai khối lượng công việc trên cụm đạt danh mục kiểm sáu điểm và qua ba phép thử phục hồi.

**Đánh giá.** Tầng *áp dụng*. Bài tổng hợp module thành một triển khai đạt chuẩn. Kiểm bằng danh mục kiểm cộng ba phép thử; đạt khi cả sáu điểm đạt và cả ba phép thử qua.

**Lab.** Triển khai hai khối lượng công việc. Lập bảng danh mục kiểm sáu điểm. Thực hiện ba phép thử và ghi kết quả. Viết một quyết định ngắn về tự vận hành hay dùng dịch vụ quản lý cho phần có trạng thái, kèm hai lý do.

**Pitfalls.** Sao chép tệp khai báo mẫu mà không đặt tài nguyên · tự vận hành cơ sở dữ liệu mà chưa cân nhắc chi phí · bỏ kiểm tra sẵn sàng · nộp mà chưa thử xoá tác vụ lần nào.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Sáu điểm trong danh mục kiểm đều đạt, ba phép thử phục hồi đều qua, và quyết định về phần có trạng thái có hai lý do cụ thể.

# MODULE 37 · CLOUD AND INFRASTRUCTURE AS CODE

**Lessons 375–386 · 24 giờ**

| | |
|---|---|
| **Objective cấp module** | Dựng hạ tầng cho pipeline tham chiếu bằng mã khai báo, huỷ và dựng lại được, và giải thích mọi quyền đã cấp bằng nguyên tắc đặc quyền tối thiểu |
| **Tiền đề** | M36 |
| **Exit criterion** | Huỷ sạch rồi dựng lại toàn bộ hạ tầng bằng một lệnh, pipeline chạy lại được, và không tài khoản nào có quyền rộng hơn việc nó phải làm |
| **Kỹ năng SFIA** | `ARCH` mức 3 · `SYSP` mức 4 · `CFMG` mức 4 |
| **Chế độ hỏng** | Bấm tay trên giao diện để dựng, không ai biết môi trường gồm những gì, rồi không dựng lại được và không biết đang trả tiền cho cái gì |

Mức `A` cho một nhà cung cấp, mức `B` cho hai nhà còn lại theo quy ước ở mục 2: học ánh xạ dịch vụ theo chức năng chứ học thuộc tên.

Module này là chỗ mọi thứ đã dựng cục bộ từ M20 tới M36 được đưa lên hạ tầng thật, nên nó cũng là chỗ đầu tiên chi phí trở thành một ràng buộc đo được chứ một lời nhắc.

### Lesson 375 · The shared responsibility model and the four service groups `LT`
**Prerequisites.** Module 37: M36

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Dùng đám mây không bỏ được trách nhiệm vận hành mà chỉ dời ranh giới, và biết ranh giới nằm ở đâu quyết định đội phải làm gì. Với máy ảo, nhà cung cấp lo phần cứng và ảo hoá, đội lo hệ điều hành trở lên. Với cơ sở dữ liệu quản lý, nhà cung cấp lo thêm bản vá và sao lưu, đội vẫn lo lược đồ, chỉ mục, truy vấn và chi phí. Với dịch vụ không máy chủ, nhà cung cấp lo gần hết phần chạy, đội lo mã và cấu hình. Phần **không bao giờ dời đi được**: dữ liệu của ai người đó chịu trách nhiệm, gồm phân loại, quyền truy cập, mã hoá và tuân thủ. Bốn nhóm dịch vụ một đội dữ liệu dùng thường xuyên: tính toán, lưu trữ đối tượng, cơ sở dữ liệu quản lý, và mạng. Học theo chức năng thay vì theo tên riêng, vì tên đổi theo nhà cung cấp còn chức năng thì không, và đây là lý do lesson 385 lập bảng ánh xạ.

**Outcome.** Với một kiến trúc cho trước, chỉ ra phần nào thuộc trách nhiệm nhà cung cấp và phần nào thuộc đội, ở cả ba mức dịch vụ.

**Đánh giá.** Tầng *hiểu*. Bài mở module, đặt đúng kỳ vọng trước khi dựng. Kiểm bằng ba kiến trúc ở ba mức; đạt khi phân định đúng ở cả ba và nêu đúng phần không dời đi được.

**Lab.** Cho ba kiến trúc dùng máy ảo, cơ sở dữ liệu quản lý và dịch vụ không máy chủ. Với mỗi kiến trúc, lập bảng hai cột về trách nhiệm. Đọc thoả thuận mức dịch vụ của một dịch vụ lưu trữ thật và ghi lại nhà cung cấp cam kết gì và không cam kết gì.

**Pitfalls.** Nghĩ dùng dịch vụ quản lý là hết việc vận hành · cho rằng nhà cung cấp chịu trách nhiệm về dữ liệu · học thuộc tên dịch vụ thay vì chức năng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba bảng trách nhiệm phân định đúng, và trích được từ thoả thuận mức dịch vụ thật hai điều nhà cung cấp không cam kết.

### Lesson 376 · Identity and access - least privilege in practice `TH`
**Prerequisites.** Lesson 375

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Quyền là chỗ sai nguy hiểm nhất trên đám mây vì sai thì hoặc lộ dữ liệu hoặc xoá được thứ không nên xoá. Bốn khái niệm: danh tính là người hoặc khối lượng công việc, chính sách là tập quyền, vai là danh tính tạm mà một danh tính khác có thể nhận, và tài nguyên là thứ được bảo vệ. Nguyên tắc đặc quyền tối thiểu phát biểu cụ thể: mỗi danh tính chỉ được đúng những hành động nó thật sự gọi, trên đúng những tài nguyên nó thật sự chạm. Ba cách làm sai phổ biến: cấp quyền quản trị cho tiện, dùng khoá dài hạn thay vì vai tạm, và chia sẻ một danh tính cho nhiều dịch vụ nên không truy được ai làm gì. Danh tính cho khối lượng công việc là cách đúng để một tác vụ ở M36 gọi dịch vụ đám mây mà không cần khoá tĩnh. Cách thu hẹp quyền có phương pháp: bắt đầu từ quyền rộng trong môi trường thử, đọc nhật ký gọi thật, rồi viết chính sách đúng những hành động đã dùng.

**Outcome.** Viết chính sách đặc quyền tối thiểu cho một thành phần từ nhật ký gọi thật, và chứng minh nó đủ chạy nhưng không rộng hơn.

**Đánh giá.** Tầng *áp dụng*. Objective là một quy trình thu hẹp quyền có bằng chứng, kiểm được bằng thử cả chiều đủ lẫn chiều thừa. Kiểm bằng hai phép thử; đạt khi pipeline chạy xong và mọi hành động ngoài danh sách đều bị từ chối.

**Lab.** Chạy pipeline với quyền rộng trong môi trường thử, thu nhật ký gọi và rút danh sách hành động thật. Viết chính sách chỉ gồm các hành động đó trên đúng tài nguyên. Áp dụng và chạy lại. Thử ba hành động ngoài danh sách và xác nhận bị từ chối. Chuyển từ khoá tĩnh sang danh tính khối lượng công việc.

**Pitfalls.** Cấp quyền quản trị cho tiện rồi hẹn sẽ sửa sau · dùng ký tự đại diện cho tài nguyên · để khoá tĩnh trong biến môi trường · chia sẻ một danh tính cho nhiều dịch vụ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Pipeline chạy xong với chính sách hẹp, ba hành động ngoài danh sách đều bị từ chối, và không còn khoá tĩnh nào trong cấu hình.

### Lesson 377 · Cloud networking and the private path to data `TH`
**Prerequisites.** Lesson 376

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Mặc định của nhiều hướng dẫn là để dịch vụ dữ liệu có địa chỉ công khai, và đó là cách phổ biến nhất khiến cơ sở dữ liệu bị quét thấy rồi bị tấn công. Bốn khái niệm đủ dùng: mạng riêng ảo là không gian địa chỉ riêng; mạng con chia theo vùng sẵn sàng và theo mức công khai; bảng định tuyến quyết định đường ra; nhóm bảo mật là tường lửa ở mức tài nguyên. Bố trí chuẩn cho hệ dữ liệu: thành phần cần người ngoài gọi vào đặt ở mạng con công khai, cơ sở dữ liệu và kho nội bộ đặt ở mạng con riêng không có đường ra trực tiếp. Cách cho tài nguyên trong mạng riêng gọi ra ngoài mà không phơi mặt ra ngoài. Điểm cuối riêng cho dịch vụ của nhà cung cấp: cho phép gọi kho đối tượng mà lưu lượng không đi qua mạng công cộng, đồng thời giảm chi phí truyền dữ liệu. Ba câu hỏi kiểm tra trước khi mở bất kỳ cổng nào ra ngoài.

**Outcome.** Bố trí một hệ dữ liệu sao cho cơ sở dữ liệu không có đường vào từ mạng công cộng, và chứng minh bằng quét cổng từ bên ngoài.

**Đánh giá.** Tầng *áp dụng*. Objective là một cấu hình bảo mật kiểm được khách quan bằng quét. Kiểm bằng quét từ ngoài cộng phép thử kết nối từ trong; đạt khi ngoài không thấy cổng nào của cơ sở dữ liệu và trong vẫn kết nối được.

**Lab.** Dựng mạng riêng ảo có mạng con công khai và riêng. Đặt cơ sở dữ liệu ở mạng con riêng và ứng dụng ở mạng con công khai. Quét cổng từ một máy ngoài và ghi kết quả. Tạo điểm cuối riêng cho kho đối tượng và so chi phí truyền dữ liệu trước sau.

**Pitfalls.** Để cơ sở dữ liệu có địa chỉ công khai cho tiện kết nối · mở nhóm bảo mật cho mọi địa chỉ · quên điểm cuối riêng rồi trả phí truyền dữ liệu qua mạng công cộng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Quét từ ngoài không thấy cổng cơ sở dữ liệu, ứng dụng trong mạng vẫn kết nối được, và có số chênh chi phí truyền dữ liệu.

### Lesson 378 · Cloud object storage - classes, lifecycle and cost `TH`
**Prerequisites.** Lesson 377

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Kho đối tượng trên đám mây là bản thương mại của thứ đã học ở lesson 329, và ba yếu tố quyết định hoá đơn chứ chỉ dung lượng: dung lượng lưu, số yêu cầu, và lưu lượng ra khỏi vùng. Yếu tố thứ ba là chỗ đội hay bị bất ngờ, vì đọc dữ liệu về máy ngoài vùng tốn tiền nhiều hơn lưu trữ. Các lớp lưu trữ đổi giá lưu lấy giá truy cập và thời gian lấy ra: lớp nóng đắt lưu rẻ đọc, lớp lạnh ngược lại, lớp lưu trữ lâu dài rẻ nhất nhưng lấy ra mất hàng giờ và có phí lấy ra. Quy tắc vòng đời tự chuyển đối tượng sang lớp rẻ hơn theo tuổi và tự xoá theo chính sách lưu giữ, và đây là cách thực thi chính sách ở M38 bằng máy. Bẫy thường gặp: chuyển tệp nhỏ sang lớp lạnh có thể đắt hơn giữ nguyên vì có phí tối thiểu cho mỗi đối tượng, nên phải dồn tệp ở lesson 335 trước. Phiên bản đối tượng và vì sao bật nó mà không có quy tắc dọn làm dung lượng tăng âm thầm.

**Outcome.** Thiết kế quy tắc vòng đời cho dữ liệu của pipeline và ước lượng mức giảm chi phí, kèm cảnh báo về tệp nhỏ.

**Đánh giá.** Tầng *đánh giá*. Objective đòi cân giữa chi phí lưu và chi phí truy cập theo mẫu đọc thật. Kiểm bằng bảng ước lượng ba phương án; đạt khi có cả ba yếu tố chi phí và phương án chọn tính đến kích thước tệp.

**Lab.** Phân tích mẫu truy cập dữ liệu của pipeline theo tuổi. Thiết kế quy tắc vòng đời. Ước lượng hoá đơn ba phương án gồm giữ nguyên lớp nóng, chuyển sau 30 ngày, và chuyển sau 90 ngày, tính cả ba yếu tố. Tính riêng trường hợp dữ liệu gồm nhiều tệp nhỏ.

**Pitfalls.** Chỉ tính chi phí lưu mà quên phí yêu cầu và phí ra · chuyển tệp nhỏ sang lớp lạnh · bật phiên bản đối tượng mà không có quy tắc dọn · đặt vòng đời cho dữ liệu vẫn đang đọc thường xuyên.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng ba phương án tính đủ ba yếu tố chi phí, và phương án chọn nêu rõ điều kiện về kích thước tệp.

### Lesson 379 · Managed databases and the operations you still own `TH`
**Prerequisites.** Lesson 378

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Cơ sở dữ liệu quản lý bỏ giúp việc cài đặt, vá lỗi, sao lưu tự động và chuyển đổi khi hỏng, nhưng năm việc vẫn thuộc về đội và bỏ qua chúng là cách tốn tiền hoặc mất dữ liệu: thiết kế lược đồ và chỉ mục theo M10, viết truy vấn không làm nghẽn, chọn kích thước và kiểu máy, đặt chính sách sao lưu cùng thời gian giữ, và kiểm chứng khôi phục thật. Việc thứ năm là việc hay bị bỏ nhất: có bản sao lưu không có nghĩa là khôi phục được, và cách duy nhất biết là khôi phục thử, đúng nguyên tắc sẽ đặt ở lesson 395. Bản sao chỉ đọc và cách dùng đúng: đẩy tải phân tích sang bản sao để không làm nghẽn hệ giao dịch, kèm cảnh báo về độ trễ bản sao ở lesson 120. Triển khai nhiều vùng sẵn sàng đổi chi phí gấp đôi lấy khả năng chịu một vùng chết. Bốn chỉ số phải theo dõi trên cơ sở dữ liệu quản lý và ngưỡng nên đặt.

**Outcome.** Cấu hình một cơ sở dữ liệu quản lý cho pipeline và chứng minh khôi phục được từ bản sao lưu về một mốc thời gian cho trước.

**Đánh giá.** Tầng *áp dụng*. Objective là một quy trình vận hành có kết quả kiểm được bằng phép khôi phục thật. Kiểm bằng khôi phục về một mốc và đối soát; đạt khi dữ liệu khôi phục khớp trạng thái tại mốc đó.

**Lab.** Dựng cơ sở dữ liệu quản lý, bật sao lưu và khôi phục theo thời điểm. Ghi dữ liệu, ghi lại mốc thời gian, ghi tiếp rồi xoá nhầm một bảng. Khôi phục về mốc đã ghi và đối soát. Đo thời gian khôi phục. Dựng bản sao chỉ đọc và đo độ trễ bản sao dưới tải.

**Pitfalls.** Tin vào bản sao lưu mà chưa khôi phục thử lần nào · chạy truy vấn phân tích thẳng trên bản chính · chọn kích thước máy theo cảm tính · để thời gian giữ sao lưu mặc định.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Khôi phục về mốc thời gian cho trước và đối soát khớp, có số đo thời gian khôi phục, và có số đo độ trễ bản sao dưới tải.

### Lesson 380 · Managed data services - when they earn their price `LT`
**Prerequisites.** Lesson 379

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Nhà cung cấp có dịch vụ quản lý cho gần như mọi thứ đã học: kho dữ liệu, Spark, Kafka, bộ điều phối, sổ đăng ký lược đồ. Câu hỏi không phải dùng hay tự dựng mà là **ở khối lượng nào thì cái nào rẻ hơn tổng thể**, và tổng thể phải gồm cả thời gian người. Ba thành phần chi phí thường bị bỏ khi so: thời gian dựng ban đầu, thời gian vận hành và trực hằng tháng, và chi phí của một sự cố mà đội không đủ năng lực xử lý. Ba tình huống dịch vụ quản lý gần như luôn thắng: đội dưới năm người, khối lượng không đều nên tự dựng phải để dư công suất, và thành phần cần sẵn sàng cao mà đội chưa từng vận hành. Hai tình huống tự dựng thắng: khối lượng rất lớn và ổn định, và yêu cầu cấu hình mà bản quản lý không cho. Bẫy phụ thuộc nhà cung cấp là có thật nhưng thường bị phóng đại: mức độ phụ thuộc phụ thuộc vào việc dữ liệu và logic có nằm ở định dạng mở hay không, đúng lý do M33 chọn định dạng bảng mở.

**Outcome.** So tổng chi phí sở hữu giữa tự dựng và dịch vụ quản lý cho một thành phần, tính đủ ba thành phần chi phí thường bị bỏ.

**Đánh giá.** Tầng *đánh giá*. Objective đòi so hai phương án bằng tổng chi phí sở hữu chứ bằng giá niêm yết. Kiểm bằng bảng so cho hai khối lượng khác nhau; đạt khi tính đủ ba thành phần và kết luận đổi chiều theo khối lượng.

**Lab.** Chọn một thành phần đã tự dựng ở các module trước. Lập bảng tổng chi phí sở hữu cho tự dựng và cho bản quản lý, ở hai mức khối lượng cách nhau mười lần. Ước lượng thời gian người bằng số giờ đã bỏ ra thật trong các module trước. Nêu mức khối lượng mà kết luận đổi chiều.

**Pitfalls.** So bằng giá niêm yết · bỏ qua thời gian vận hành · kết luận một chiều cho mọi khối lượng · viện lý do phụ thuộc nhà cung cấp mà không xét định dạng dữ liệu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng so tính đủ ba thành phần ở hai mức khối lượng, và nêu được mức khối lượng mà kết luận đổi chiều.

### Lesson 381 · Infrastructure as code - declarative state and the plan `TH`
**Prerequisites.** Lesson 380

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bấm tay trên giao diện có ba hậu quả tích tụ: không ai biết môi trường gồm những gì, môi trường thử và sản xuất lệch nhau, và dựng lại sau sự cố mất nhiều ngày. Hạ tầng bằng mã giải cả ba bằng cách mô tả trạng thái mong muốn trong tệp nộp vào kho mã, cùng tư duy khai báo như ở lesson 366. Vòng lặp ba bước: viết mô tả, xem kế hoạch, áp dụng. **Bước xem kế hoạch là bước quan trọng nhất và cũng hay bị bỏ qua nhất**: nó nói chính xác cái gì sẽ tạo, sửa, và xoá, nên đọc kỹ nó là cách duy nhất tránh xoá nhầm tài nguyên có dữ liệu. Đọc kế hoạch cần biết phân biệt thay đổi tại chỗ với thay đổi buộc tạo lại, vì loại thứ hai với một cơ sở dữ liệu nghĩa là mất dữ liệu. Tệp trạng thái ghi hệ đang quản lý những gì, và vì sao nó chứa thông tin nhạy cảm nên phải lưu ở kho có mã hoá và có khoá. So với kịch bản mệnh lệnh: mã khai báo chạy lại nhiều lần cho cùng kết quả.

**Outcome.** Dựng một phần hạ tầng bằng mã, đọc được kế hoạch và chỉ ra thay đổi nào buộc tạo lại tài nguyên.

**Đánh giá.** Tầng *áp dụng*. Objective gồm một kỹ năng đọc có hậu quả trực tiếp tới an toàn dữ liệu. Kiểm bằng bài đọc kế hoạch có bẫy; đạt khi nhận ra đúng thay đổi buộc tạo lại trước khi áp dụng.

**Lab.** Dựng mạng và một kho đối tượng bằng mã. Sửa một thuộc tính sửa tại chỗ được và một thuộc tính buộc tạo lại, xem kế hoạch và phân loại hai thay đổi trước khi áp dụng. Xoá một tài nguyên bằng tay trên giao diện rồi chạy kế hoạch và quan sát hệ phát hiện lệch.

**Pitfalls.** Áp dụng mà không đọc kế hoạch · lưu tệp trạng thái trong kho mã · sửa bằng tay rồi quên cập nhật mã · nhầm thay đổi tại chỗ với thay đổi tạo lại.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân loại đúng hai loại thay đổi trước khi áp dụng, và hệ phát hiện đúng phần lệch sau khi sửa tay.

### Lesson 382 · Modules, state and working in a team `TH`
**Prerequisites.** Lesson 381

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Khi nhiều người cùng sửa hạ tầng, tệp trạng thái thành tài nguyên tranh chấp: hai người chạy áp dụng cùng lúc thì trạng thái hỏng. Kho trạng thái từ xa có khoá giải việc đó, và đây là điều kiện bắt buộc trước khi người thứ hai tham gia. Chia mã thành mô đun theo ranh giới thay đổi cùng nhau chứ theo loại tài nguyên: mạng đổi hiếm, cơ sở dữ liệu đổi vừa, ứng dụng đổi thường xuyên, nên tách ba tầng đó ra ba trạng thái riêng để thay đổi ở tầng nhanh không phải chạm vào tầng chậm và không có nguy cơ xoá nhầm. Tham số hoá theo môi trường để cùng mã dựng cả thử lẫn sản xuất, chỉ khác giá trị đầu vào; đây là cách duy nhất bảo đảm hai môi trường giống nhau. Ghim phiên bản của nhà cung cấp và của mô đun, cùng lý do ghim ảnh nền ở lesson 358. Đưa lệnh xem kế hoạch vào yêu cầu hợp nhất mã để người rà soát thấy hệ quả trước khi duyệt.

**Outcome.** Tổ chức mã hạ tầng thành nhiều trạng thái theo nhịp thay đổi, và dựng được hai môi trường giống nhau từ cùng một mã.

**Đánh giá.** Tầng *sáng tạo*. Objective đòi thiết kế cấu trúc mã theo ranh giới thay đổi, chứ áp dụng một khuôn có sẵn. Kiểm bằng phép so hai môi trường cộng phép thử thay đổi tầng nhanh; đạt khi hai môi trường khác nhau đúng phần tham số và thay đổi tầng ứng dụng không chạm trạng thái tầng mạng.

**Lab.** Chuyển mã sang kho trạng thái từ xa có khoá. Tách thành ba trạng thái theo nhịp thay đổi. Dựng hai môi trường từ cùng mã với hai bộ tham số và so khác biệt. Thay đổi một thuộc tính ở tầng ứng dụng và chứng minh kế hoạch không đụng tài nguyên mạng.

**Pitfalls.** Giữ mọi thứ trong một trạng thái khổng lồ · dùng trạng thái cục bộ khi làm nhóm · sao chép mã cho môi trường thứ hai thay vì tham số hoá · không ghim phiên bản.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Hai môi trường chỉ khác nhau ở phần tham số, và thay đổi tầng ứng dụng cho kế hoạch không chạm tài nguyên tầng mạng.

### Lesson 383 · Environments, drift and a destroy that must be safe `TH`
**Prerequisites.** Lesson 382

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Lệch cấu hình xảy ra khi thực tế khác mã, do sửa tay lúc xử lý sự cố hoặc do nhà cung cấp tự đổi. Phát hiện bằng cách chạy kế hoạch định kỳ trong tích hợp liên tục và cảnh báo khi kế hoạch không rỗng; đây là chỉ số sức khoẻ của kỷ luật hạ tầng bằng mã. Hai cách xử lý khi phát hiện và tiêu chí chọn: đưa thực tế về khớp mã, hoặc đưa mã về khớp thực tế nếu thay đổi tay là đúng. Lệnh huỷ là thứ nguy hiểm nhất trong module: nó xoá mọi thứ trạng thái đang quản lý, và chạy nhầm ở sản xuất là sự cố không lùi được. Ba lớp bảo vệ phải đặt trước khi ai đó chạy được lệnh huỷ: bảo vệ chống xoá trên tài nguyên có dữ liệu, tách quyền sao cho tài khoản thường không xoá được tài nguyên có trạng thái, và bắt buộc xem kế hoạch huỷ rồi có người thứ hai duyệt. Vì sao môi trường thử nên huỷ và dựng lại định kỳ: đó là cách duy nhất biết mã hạ tầng còn dựng lại được.

**Outcome.** Phát hiện lệch cấu hình tự động, và dựng được ba lớp bảo vệ sao cho lệnh huỷ không xoá được tài nguyên có dữ liệu.

**Đánh giá.** Tầng *áp dụng*. Objective gồm một cơ chế phát hiện và một cơ chế phòng vệ, cả hai kiểm được bằng thử nghiệm. Kiểm bằng thử huỷ có kiểm soát; đạt khi lệch được phát hiện tự động và lệnh huỷ bị chặn ở tài nguyên có dữ liệu.

**Lab.** Sửa tay một tài nguyên trên giao diện. Dựng bước chạy kế hoạch định kỳ và xác nhận nó báo lệch. Đặt bảo vệ chống xoá cho kho dữ liệu. Chạy lệnh huỷ ở môi trường thử và xác nhận nó dừng lại ở tài nguyên được bảo vệ. Huỷ sạch môi trường thử rồi dựng lại từ mã và chạy lại bộ kiểm thử.

**Pitfalls.** Không có cơ chế phát hiện lệch · chạy huỷ mà không xem kế hoạch · dùng cùng tài khoản cho thử và sản xuất · chưa bao giờ dựng lại môi trường thử từ đầu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Lệch được phát hiện tự động, lệnh huỷ bị chặn ở tài nguyên có dữ liệu, và môi trường thử dựng lại từ mã chạy được bộ kiểm thử.

### Lesson 384 · Cost - tagging, budgets and the bill that surprised the team `TH`
**Prerequisites.** Lesson 383

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Chi phí đám mây tăng âm thầm vì tài nguyên dựng ra thì nhớ mà tắt thì quên, và vì đơn vị tính phí nhỏ tới mức không ai thấy đắt cho tới khi cộng lại cuối tháng. Điều kiện tiên quyết để quản được là gắn nhãn: mọi tài nguyên phải có nhãn về môi trường, đội sở hữu và thành phần, cưỡng chế bằng chính sách chứ bằng nhắc nhở, và gắn ngay trong mã hạ tầng. Không có nhãn thì hoá đơn chỉ là một con số và không truy được về ai. Bốn nguồn chi phí bất ngờ thường gặp trong hệ dữ liệu: truyền dữ liệu ra khỏi vùng ở lesson 378, cụm để chạy qua đêm sau khi thử nghiệm, kho đối tượng có phiên bản mà không dọn, và nhật ký giữ quá lâu. Ngân sách và cảnh báo theo ngưỡng, kèm cảnh báo theo xu hướng vì ngưỡng tháng báo quá muộn. Chi phí trên mỗi đơn vị nghiệp vụ là chỉ số đáng theo dõi hơn tổng chi phí, vì nó tách phần tăng do tăng trưởng khỏi phần tăng do lãng phí.

**Outcome.** Gắn nhãn toàn bộ hạ tầng bằng mã, truy được chi phí về từng thành phần, và đặt cảnh báo bắt được một khoản tăng bất thường.

**Đánh giá.** Tầng *áp dụng*. Objective là một cơ chế quản trị kiểm được bằng việc truy ngược một khoản chi. Kiểm bằng phép truy ngược cộng thử cảnh báo; đạt khi mọi tài nguyên có nhãn và cảnh báo kích hoạt trước ngưỡng tháng.

**Lab.** Thêm nhãn bắt buộc vào mọi tài nguyên trong mã. Dựng chính sách từ chối tài nguyên thiếu nhãn. Lập báo cáo chi phí theo thành phần. Đặt ngân sách và hai cảnh báo, một theo ngưỡng và một theo xu hướng. Cố ý dựng một cụm đắt và bỏ chạy qua đêm, rồi kiểm cảnh báo nào báo trước.

**Pitfalls.** Gắn nhãn bằng tay · chỉ đặt cảnh báo theo ngưỡng tháng · theo dõi tổng chi phí mà không chia theo thành phần · quên tắt môi trường thử ngoài giờ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mọi tài nguyên có đủ nhãn và chính sách chặn được tài nguyên thiếu nhãn, và cảnh báo theo xu hướng báo trước cảnh báo ngưỡng có số.

### Lesson 385 · Mapping services across providers `LT`
**Prerequisites.** Lesson 384

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Bài duy nhất trong module nhìn ra ngoài một nhà cung cấp, và mục tiêu là đọc được tài liệu của nhà cung cấp khác mà không phải học lại từ đầu. Nguyên tắc: **ánh xạ theo chức năng, không theo tên**, vì chức năng ổn định còn tên thì đổi. Bảng ánh xạ cho tám chức năng đã dùng trong chương trình: lưu trữ đối tượng, kho dữ liệu, cơ sở dữ liệu quan hệ quản lý, Spark quản lý, Kafka quản lý, bộ điều phối quản lý, chạy container, và quản lý bí mật. Với mỗi chức năng, ghi tên của ba nhà cung cấp lớn cùng một khác biệt đáng chú ý, vì các dịch vụ tương đương về chức năng vẫn khác về mô hình tính phí hoặc giới hạn. Ba khác biệt có hệ quả thật khi chuyển nhà cung cấp: mô hình tính phí của kho dữ liệu, cách tính lưu lượng ra, và mức độ tương thích với định dạng bảng mở ở M33. Mức `C` ở đây theo đúng quy ước mục 2: biết dùng đúng tình huống, không đòi vận hành.

**Outcome.** Lập bảng ánh xạ tám chức năng sang ba nhà cung cấp, và nêu với mỗi chức năng một khác biệt có hệ quả thật.

**Đánh giá.** Tầng *hiểu*. Objective là năng lực đọc tài liệu chéo nhà cung cấp, không phải vận hành. Kiểm bằng bảng ánh xạ cộng bài đọc tài liệu; đạt khi đủ tám chức năng và mỗi dòng có một khác biệt cụ thể chứ một nhận xét chung.

**Lab.** Lập bảng tám chức năng nhân ba nhà cung cấp từ tài liệu chính thức đang hiện hành. Với mỗi chức năng, đọc trang giá của ít nhất hai nhà và ghi một khác biệt về mô hình tính phí. Cho ba yêu cầu kiến trúc và chọn dịch vụ tương ứng ở cả ba nhà.

**Pitfalls.** Học thuộc tên dịch vụ · chép bảng so sánh của bên thứ ba thay vì đọc tài liệu chính thức · kết luận nhà cung cấp nào tốt hơn mà không nêu khối lượng công việc.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng tám chức năng nhân ba nhà cung cấp đầy đủ, mỗi dòng có một khác biệt cụ thể dẫn từ tài liệu chính thức.

### Lesson 386 · Deploying the reference pipeline to the cloud `DA`
**Prerequisites.** Lesson 385

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Bài dự án khép module: đưa toàn bộ pipeline tham chiếu lên đám mây, dựng hoàn toàn bằng mã. Yêu cầu bắt buộc và mỗi yêu cầu đều kiểm được: mọi tài nguyên dựng bằng mã, không có tài nguyên nào tạo tay; hai môi trường thử và sản xuất từ cùng mã khác tham số; cơ sở dữ liệu không có đường vào từ mạng công cộng; mọi danh tính theo đặc quyền tối thiểu với chính sách rút từ nhật ký gọi thật; mọi tài nguyên có nhãn đầy đủ; và có ngân sách kèm cảnh báo. Phép thử nghiệm thu là phép thử huỷ và dựng lại: huỷ sạch môi trường thử, dựng lại bằng một lệnh, chạy lại pipeline và đối soát kết quả. Nộp kèm ước lượng hoá đơn tháng chia theo thành phần và một danh sách ba khoản có thể cắt kèm số tiền. Đây là hồ sơ đi thẳng vào phần chi phí của bài kiến trúc ở M39.

**Outcome.** Dựng toàn bộ hạ tầng bằng mã đạt sáu yêu cầu, và huỷ rồi dựng lại được môi trường thử bằng một lệnh.

**Đánh giá.** Tầng *sáng tạo*. Bài tổng hợp module thành một hạ tầng hoàn chỉnh dưới ràng buộc bảo mật và chi phí. Kiểm bằng phép thử huỷ và dựng lại cộng rà soát sáu yêu cầu; đạt khi cả sáu đạt và pipeline chạy lại được sau khi dựng lại.

**Lab.** Dựng toàn bộ hạ tầng bằng mã cho hai môi trường. Kiểm sáu yêu cầu bằng bảng có bằng chứng cho từng dòng. Huỷ sạch môi trường thử và dựng lại, chạy pipeline và đối soát. Nộp ước lượng hoá đơn theo thành phần và ba khoản cắt được kèm số tiền.

**Pitfalls.** Tạo tay vài tài nguyên rồi ghi vào mã sau · dùng chung một tài khoản cho hai môi trường · bỏ phép thử huỷ và dựng lại vì sợ · ước lượng hoá đơn mà không chia theo thành phần.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Sáu yêu cầu đều có bằng chứng, môi trường thử dựng lại bằng một lệnh và pipeline đối soát khớp, và ước lượng hoá đơn chia theo thành phần kèm ba khoản cắt được.

# MODULE 38 · OPERATIONS, OBSERVABILITY, SECURITY AND COST

**Lessons 387–400 · 28 giờ**

| | |
|---|---|
| **Objective cấp module** | Vận hành được nền tảng dữ liệu dưới sự cố: có mục tiêu mức dịch vụ đo được, cảnh báo đáng tin, quy trình xử lý sự cố, và khôi phục đã kiểm chứng |
| **Tiền đề** | M37 |
| **Exit criterion** | Qua được buổi diễn tập sự cố: phát hiện trong ngưỡng, chẩn đoán đúng, khắc phục, thông báo đúng đối tượng, và viết phân tích sau sự cố không đổ lỗi |
| **Kỹ năng SFIA** | `CFMG` mức 4 · `SYSP` mức 4 |
| **Chế độ hỏng** | Dựng theo dõi rồi để cảnh báo kêu suốt tới khi cả đội tắt thông báo, nên sự cố thật đi qua mà không ai biết |

Module này là phần phân biệt người xây được hệ với người vận hành được hệ, và là lý do trọng số 25% cho khả năng phục hồi trong thang điểm tốt nghiệp.

Nhiều cơ chế đã gặp lẻ tẻ ở các module trước: cảnh báo theo xu hướng ở lesson 300 và 315, quy trình bảy bước ở M26, thí nghiệm hỏng ở lesson 218 và 298. Module gom chúng thành một hệ vận hành có chuẩn và có bằng chứng.

### Lesson 387 · Service level indicators, objectives and agreements for data `LT`
**Prerequisites.** Module 38: M37

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Ba khái niệm hay bị dùng lẫn và phân biệt được chúng là điều kiện để nói chuyện với bên nghiệp vụ. Chỉ báo là một phép đo, mục tiêu là ngưỡng đội tự đặt cho chỉ báo đó, thoả thuận là cam kết với bên ngoài kèm hậu quả nếu vi phạm. Đội dữ liệu nên có mục tiêu trước, và chỉ ký thoả thuận khi đã đo đủ lâu để biết mình giữ được. Bốn chỉ báo hợp với nền tảng dữ liệu, khác với chỉ báo của dịch vụ trực tuyến: độ tươi tức dữ liệu mới tới đâu, độ đầy đủ tức bao nhiêu phần trăm bản ghi kỳ vọng đã có, độ đúng tức tỉ lệ qua kiểm chất lượng ở M20, và tính sẵn có của truy vấn. Cách đặt mục tiêu có căn cứ: đo phân bố hiện tại rồi đặt ngưỡng ở mức vừa đủ nghiêm để có ý nghĩa và vừa đủ lỏng để giữ được, chứ đặt con số tròn. Ngân sách lỗi là phần được phép vi phạm, và công dụng thật của nó là làm cơ sở quyết định tốc độ phát hành.

**Outcome.** Đặt mục tiêu mức dịch vụ cho pipeline từ phân bố đo được, và nêu ngân sách lỗi tương ứng cùng cách dùng nó.

**Đánh giá.** Tầng *áp dụng*. Objective là chuyển một yêu cầu mơ hồ thành ngưỡng đo được, nối tiếp kỷ luật ở M26. Kiểm bằng bốn chỉ báo có phân bố thật; đạt khi cả bốn có ngưỡng dẫn từ phân bố và có ngân sách lỗi tính ra số.

**Lab.** Đo phân bố bốn chỉ báo trên pipeline trong bảy ngày. Đặt mục tiêu cho từng chỉ báo dẫn từ phân bố. Tính ngân sách lỗi theo tháng cho từng cái. Viết một thoả thuận ngắn với bên dùng cho chỉ báo độ tươi, gồm cam kết, cách đo, và cái gì xảy ra khi vi phạm.

**Pitfalls.** Đặt mục tiêu bằng số tròn · cam kết mức không thực tế · lẫn mục tiêu nội bộ với cam kết ra ngoài · đặt mục tiêu cho chỉ báo chưa từng đo.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn mục tiêu đều dẫn từ phân bố bảy ngày, ngân sách lỗi tính ra số cụ thể, và thoả thuận nêu đủ cam kết, cách đo và hậu quả.

### Lesson 388 · What to instrument on a data platform `TH`
**Prerequisites.** Lesson 387

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Đo cái gì quyết định chẩn đoán được hay không, và đo sai chỗ là lý do sự cố kéo dài hàng giờ. Ba tầng phải có số đo và chỉ có tầng thứ ba mới nói được người dùng có vấn đề hay không: tầng hạ tầng gồm CPU, bộ nhớ, đĩa, mạng; tầng thành phần gồm độ trễ tiêu thụ ở lesson 300, khe sao chép ở lesson 315, dung lượng xáo trộn ở M34; tầng dữ liệu gồm bốn chỉ báo ở lesson 387. Nguyên tắc rút ra: **cảnh báo trên tầng dữ liệu vì đó là thứ người dùng cảm nhận, dùng hai tầng dưới để chẩn đoán**. Quy ước đặt tên và gắn nhãn cho số đo để cắt lát được theo pipeline, theo bảng và theo môi trường; thiếu nhãn thì có số mà không trả lời được câu hỏi nào. Ba loại số đo và khi nào dùng loại nào: bộ đếm cho việc đã xảy ra, thước đo cho giá trị hiện tại, biểu đồ phân bố cho độ trễ vì trung bình che mất đuôi phân bố.

**Outcome.** Dựng bộ số đo ba tầng cho pipeline với nhãn đủ để cắt lát, và chỉ ra số đo nào dùng để cảnh báo, số nào dùng để chẩn đoán.

**Đánh giá.** Tầng *áp dụng*. Objective là thiết kế bộ số đo phục vụ chẩn đoán, kiểm được bằng việc trả lời câu hỏi thật. Kiểm bằng năm câu hỏi chẩn đoán; đạt khi trả lời được ít nhất bốn chỉ bằng bảng điều khiển.

**Lab.** Gắn số đo ba tầng cho pipeline, dùng đúng ba loại số đo. Dựng một bảng điều khiển. Giảng viên đặt năm câu hỏi chẩn đoán và bạn phải trả lời chỉ bằng bảng điều khiển, không mở nhật ký. Ghi lại câu nào không trả lời được và thiếu số đo gì.

**Pitfalls.** Chỉ đo tầng hạ tầng · dùng trung bình cho độ trễ · quên gắn nhãn nên không cắt lát được · dựng bảng điều khiển đẹp mà không trả lời được câu hỏi nào.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Trả lời được ≥ 4/5 câu hỏi chẩn đoán chỉ bằng bảng điều khiển, và ghi rõ số đo còn thiếu cho câu không trả lời được.

### Lesson 389 · Logs, metrics and traces - and correlating across a pipeline `TH`
**Prerequisites.** Lesson 388

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ba loại tín hiệu trả lời ba loại câu hỏi và dùng một loại cho mọi việc là cách vừa tốn tiền vừa chẩn đoán chậm. Số đo trả lời có vấn đề không và ở đâu, rẻ để lưu, không có chi tiết từng sự kiện. Nhật ký trả lời chuyện gì đã xảy ra với một bản ghi cụ thể, đắt để lưu nên phải có chính sách giữ. Dấu vết trả lời thời gian tiêu ở đâu trong một chuỗi bước, quan trọng khi một yêu cầu đi qua nhiều thành phần. Mã theo dõi ở lesson 74 là thứ nối cả ba: một mã duy nhất đi theo dữ liệu từ nguồn qua mọi bước tới đích, để khi số sai ở mart thì truy ngược được tới lô nạp nào. Nhật ký có cấu trúc thay vì chuỗi tự do, vì có cấu trúc thì truy vấn được. Ba mức nhật ký và quy tắc dùng, cùng lý do ghi ở mức gỡ lỗi trong sản xuất là cách làm hoá đơn tăng mà không ai đọc.

**Outcome.** Truy ngược được một bản ghi sai ở mart về đúng lô nạp và bước biến đổi sinh ra nó, chỉ bằng mã theo dõi.

**Đánh giá.** Tầng *phân tích*. Objective là năng lực truy ngược xuyên thành phần, kỹ năng quyết định thời gian xử lý sự cố. Kiểm bằng ba bản ghi sai tiêm sẵn tính giờ; đạt khi truy đúng nguồn gốc ít nhất hai trong giới hạn thời gian.

**Lab.** Thêm mã theo dõi đi xuyên toàn bộ pipeline và ghi nhật ký có cấu trúc ở mọi bước. Giảng viên tiêm ba bản ghi sai ở mart, mỗi lần 10 phút. Truy ngược từng cái về lô nạp và bước sinh ra nó. Dựng dấu vết cho một yêu cầu đi qua bốn thành phần và chỉ ra bước tốn thời gian nhất.

**Pitfalls.** Ghi nhật ký dạng chuỗi tự do · không có mã theo dõi xuyên hệ · để mức gỡ lỗi trong sản xuất · lưu nhật ký vô thời hạn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Truy đúng nguồn gốc ≥ 2/3 bản ghi sai trong giới hạn thời gian, và dấu vết chỉ ra đúng bước tốn thời gian nhất.

### Lesson 390 · Alerting that people do not silence `TH`
**Prerequisites.** Lesson 389

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Mệt mỏi cảnh báo là chế độ hỏng của chính hệ theo dõi, và khi đội đã tắt thông báo thì mọi công sức dựng theo dõi thành vô ích. Bốn tiêu chí cho một cảnh báo đáng giữ: nó chỉ ra một vấn đề người dùng cảm nhận được, nó có người cụ thể chịu trách nhiệm, người đó làm được một việc cụ thể ngay, và nó hiếm khi sai. Cảnh báo không đủ bốn tiêu chí thì chuyển thành phiếu công việc hoặc số đo trên bảng điều khiển chứ đánh thức người. Phân biệt cảnh báo theo triệu chứng với cảnh báo theo nguyên nhân: báo theo triệu chứng tức dữ liệu trễ quá ngưỡng thì ít và đáng tin; báo theo nguyên nhân tức CPU cao thì nhiều và hay sai. Kỹ thuật giảm nhiễu: đặt ngưỡng theo xu hướng như đã làm ở lesson 300, yêu cầu vi phạm kéo dài một khoảng, gom cảnh báo cùng nguyên nhân, và tạm ẩn trong cửa sổ bảo trì. Đo chính hệ cảnh báo: tỉ lệ cảnh báo dẫn tới hành động, và xem lại hằng tháng.

**Outcome.** Rà bộ cảnh báo hiện có theo bốn tiêu chí, loại bỏ hoặc hạ cấp cái không đạt, và đo tỉ lệ cảnh báo dẫn tới hành động.

**Đánh giá.** Tầng *đánh giá*. Objective đòi phán đoán giữ hay bỏ từng cảnh báo theo tiêu chí, chứ thêm cảnh báo. Kiểm bằng bảng rà soát cộng số đo hai tuần; đạt khi mọi cảnh báo còn lại đạt cả bốn tiêu chí và tỉ lệ dẫn tới hành động tăng.

**Lab.** Lập danh sách mọi cảnh báo đang có, chấm theo bốn tiêu chí. Loại hoặc hạ cấp cái không đạt. Chuyển ít nhất hai cảnh báo từ nguyên nhân sang triệu chứng. Chạy hai tuần, đếm số cảnh báo và số lần dẫn tới hành động thật, so với hai tuần trước.

**Pitfalls.** Thêm cảnh báo cho mọi số đo · cảnh báo theo ngưỡng tài nguyên · để cảnh báo không có người chịu trách nhiệm · giảm nhiễu bằng cách tắt thông báo.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mọi cảnh báo còn lại đạt cả bốn tiêu chí, và tỉ lệ cảnh báo dẫn tới hành động của hai tuần sau cao hơn hai tuần trước có số.

### Lesson 391 · On-call, escalation and the incident commander `LT`
**Prerequisites.** Lesson 390

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Trực là một hệ thống tổ chức chứ một danh sách số điện thoại, và thiết kế kém làm người giỏi nghỉ việc. Bốn thành phần: lịch trực có người thay, đường leo thang khi người trực không xử lý được, mức độ nghiêm trọng quyết định tốc độ phản ứng, và cam kết thời gian phản hồi theo từng mức. Ba mức nghiêm trọng đủ dùng cho nền tảng dữ liệu, mỗi mức kèm ví dụ cụ thể và kỳ vọng thời gian. Vai người chỉ huy sự cố tách khỏi vai người sửa, và đây là chi tiết quyết định khi sự cố kéo dài: người chỉ huy điều phối, ghi dòng thời gian và liên lạc với bên ngoài, còn người sửa tập trung sửa; gộp hai vai thì hoặc mất liên lạc hoặc mất tập trung. Điều kiện để trực bền vững: sổ tay cho các sự cố hay gặp, quyền đủ để xử lý mà không phải chờ ai, và bù giờ. Ba dấu hiệu hệ trực đang hỏng và cần sửa trước khi mất người.

**Outcome.** Thiết kế lịch trực và đường leo thang cho một đội cho trước, phân mức nghiêm trọng cho năm sự cố mẫu.

**Đánh giá.** Tầng *hiểu*. Bài thiết kế tổ chức chứ kỹ thuật, nên objective dừng ở chỗ áp đúng khuôn vào một bối cảnh. Kiểm bằng bài phân mức cộng bản thiết kế; đạt khi phân đúng ít nhất bốn trong năm và bản thiết kế có đủ bốn thành phần.

**Lab.** Cho một đội bốn người và năm sự cố mẫu. Phân mức nghiêm trọng cho từng sự cố kèm lý do. Thiết kế lịch trực có người thay và đường leo thang hai cấp. Viết định nghĩa vai người chỉ huy sự cố cho đội này, nêu rõ việc họ làm và không làm.

**Pitfalls.** Gộp vai chỉ huy với vai sửa · đặt mọi sự cố ở mức cao nhất · lịch trực không có người thay · để người trực thiếu quyền xử lý.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phân đúng mức cho ≥ 4/5 sự cố kèm lý do, và bản thiết kế có đủ lịch trực, đường leo thang, ba mức nghiêm trọng và định nghĩa vai chỉ huy.

### Lesson 392 · Incident response - the seven steps under time pressure `TH`
**Prerequisites.** Lesson 391

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Quy trình bảy bước đã đặt ở M26 nay áp cho toàn nền tảng, và điểm khác là thứ tự phải giữ được dưới áp lực. Bước một là chặn lan rộng, làm trước cả chẩn đoán: dừng pipeline đang ghi sai còn hơn để nó ghi thêm một giờ. Bước hai thông báo sớm cho người dùng đang dùng số, vì thông báo muộn tốn kém hơn thông báo thừa. Bước ba chẩn đoán bằng ba tầng số đo ở lesson 388. Bước bốn khắc phục, ưu tiên khôi phục dịch vụ chứ tìm nguyên nhân gốc. Bước năm chạy lại lịch sử để sửa dữ liệu đã sai, và đây là chỗ tính bất biến ở lesson 222 trả cổ tức. Bước sáu thông báo kết quả cho đúng những người đã nhận thông báo ở bước hai. Bước bảy phân tích nguyên nhân gốc, làm sau khi hết áp lực chứ trong lúc sự cố. Hai thứ phải ghi ngay trong lúc xử lý vì sau sẽ quên: dòng thời gian và mọi thay đổi đã thực hiện.

**Outcome.** Chạy đúng bảy bước trong một sự cố mô phỏng tính giờ, giữ đúng thứ tự và ghi được dòng thời gian dùng được.

**Đánh giá.** Tầng *áp dụng*. Objective là thực hiện một quy trình dưới áp lực thời gian, kiểm được bằng quan sát. Kiểm bằng diễn tập tính giờ; đạt khi chặn lan rộng trước chẩn đoán, thông báo trong ngưỡng, và dòng thời gian đủ dựng lại được diễn biến.

**Lab.** Giảng viên gây một sự cố làm pipeline ghi dữ liệu sai vào mart. Đội chạy bảy bước với vai chỉ huy và vai sửa tách biệt. Tính giờ từng bước. Sau khi xong, dựng lại diễn biến chỉ bằng dòng thời gian đã ghi và kiểm xem có thiếu gì.

**Pitfalls.** Chẩn đoán trước khi chặn lan rộng · thông báo sau khi đã sửa xong · quên ghi dòng thời gian · tìm nguyên nhân gốc trong lúc còn đang cháy.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chặn lan rộng trước chẩn đoán, thông báo trong ngưỡng cam kết, và dòng thời gian đủ để người ngoài dựng lại diễn biến.

### Lesson 393 · Blameless postmortem and the action that actually lands `TH`
**Prerequisites.** Lesson 392

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phân tích sau sự cố có hai mục đích và chỉ một mục đích là đúng: học để hệ an toàn hơn, chứ xác định ai sai. Không đổ lỗi không phải lịch sự mà là kỹ thuật: khi đổ lỗi thì người ta giấu thông tin, và mất thông tin thì không học được, nên hệ kém an toàn đi. Cấu trúc một bản phân tích dùng được: tóm tắt tác động bằng số chứ bằng tính từ, dòng thời gian, phân tích nguyên nhân đi qua nhiều tầng chứ dừng ở tầng đầu, những gì đã chạy tốt, và hành động khắc phục. Kỹ thuật hỏi vì sao nhiều lần với cảnh báo: dừng khi tới một nguyên nhân mà hệ thống sửa được, chứ dừng ở lỗi người. Điều kiện để hành động khắc phục thực sự xảy ra: mỗi hành động có một người chịu trách nhiệm, có hạn, và được đưa vào kế hoạch công việc như mọi việc khác; hành động không có chủ và không có hạn là hành động không bao giờ làm. Theo dõi tỉ lệ hành động hoàn thành như một chỉ số sức khoẻ của đội.

**Outcome.** Viết một bản phân tích sau sự cố không đổ lỗi, truy nguyên nhân tới tầng hệ thống sửa được, và đặt hành động có chủ và có hạn.

**Đánh giá.** Tầng *đánh giá*. Objective đòi phán đoán về độ sâu của nguyên nhân và chất lượng hành động, chứ điền một mẫu. Kiểm bằng rà soát chéo; đạt khi nguyên nhân tới tầng hệ thống và mọi hành động có chủ, có hạn, và kiểm chứng được.

**Lab.** Viết bản phân tích cho sự cố ở lesson 392. Dùng kỹ thuật hỏi vì sao nhiều lần và ghi lại từng tầng. Đặt ba hành động khắc phục, mỗi hành động có chủ, hạn, và cách biết là đã xong. Rà soát chéo với nhóm khác: họ tìm chỗ nào trong bản của bạn còn ám chỉ lỗi cá nhân.

**Pitfalls.** Kết luận nguyên nhân là ai đó bất cẩn · viết hành động dạng "sẽ cẩn thận hơn" · không đặt hạn · bỏ phần những gì đã chạy tốt.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Nguyên nhân truy tới tầng hệ thống sửa được, ba hành động đều có chủ và hạn và cách kiểm chứng, và qua được rà soát chéo về ngôn ngữ không đổ lỗi.

### Lesson 394 · Failure mode analysis and cascading failure `TH`
**Prerequisites.** Lesson 393

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Phân tích chế độ hỏng làm trước khi sự cố xảy ra: với mỗi thành phần, liệt kê nó hỏng theo những cách nào, hệ phản ứng ra sao, và người dùng thấy gì. Làm có hệ thống thay vì theo trí nhớ, vì trí nhớ chỉ nhớ sự cố gần nhất. Điểm hỏng đơn lẻ là thành phần mà nó chết thì cả hệ dừng, và tìm ra chúng là kết quả chính của bài tập này. Hỏng xếp tầng là cơ chế một sự cố nhỏ thành sự cố lớn: một thành phần chậm làm thành phần gọi nó dồn yêu cầu, hết tài nguyên, rồi kéo theo thành phần kế tiếp. Ba cơ chế chặn xếp tầng: bộ ngắt mạch dừng gọi khi bên kia đang hỏng, vách ngăn cô lập tài nguyên cho từng loại việc, và giảm tải chủ động từ chối bớt để phần còn lại sống. Thử lại có hai chiều tác dụng: không có lùi theo hàm mũ và nhiễu ngẫu nhiên thì thử lại làm sự cố nặng thêm, đúng bão thử lại ở lesson 61 và cơ chế đã học ở lesson 34.

**Outcome.** Lập bảng chế độ hỏng cho pipeline, tìm ra điểm hỏng đơn lẻ, và chứng minh bằng thực nghiệm một cơ chế chặn xếp tầng hoạt động.

**Đánh giá.** Tầng *phân tích*. Objective là phân tích có hệ thống trước sự cố cộng một kiểm chứng thực nghiệm. Kiểm bằng bảng cộng thí nghiệm; đạt khi tìm ra ít nhất hai điểm hỏng đơn lẻ và cơ chế chặn được chứng minh bằng số đo.

**Lab.** Lập bảng chế độ hỏng cho mọi thành phần của pipeline, mỗi dòng gồm cách hỏng, phản ứng của hệ, và biểu hiện với người dùng. Đánh dấu điểm hỏng đơn lẻ. Tạo một hỏng xếp tầng bằng cách làm chậm một thành phần hạ nguồn. Thêm bộ ngắt mạch và lặp lại, đo khác biệt.

**Pitfalls.** Liệt kê chế độ hỏng theo trí nhớ · bỏ qua hỏng dạng chậm mà chỉ xét hỏng dạng chết · thêm thử lại mà không có lùi theo hàm mũ · coi xếp tầng là chuyện chỉ xảy ra ở hệ lớn.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng chế độ hỏng phủ mọi thành phần, tìm ra ≥ 2 điểm hỏng đơn lẻ, và có số đo chứng minh bộ ngắt mạch chặn được xếp tầng.

### Lesson 395 · Disaster recovery - RTO, RPO and a restore you have tested `TH`
**Prerequisites.** Lesson 394

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Hai con số quyết định mọi thiết kế khôi phục và **cả hai phải do nghiệp vụ quyết chứ kỹ thuật tự đặt**: mục tiêu thời gian khôi phục là chịu được bao lâu không có dịch vụ, mục tiêu điểm khôi phục là chịu mất bao nhiêu dữ liệu tính theo thời gian. Từ hai con số đó suy ra tần suất sao lưu, chiến lược nhân bản và ngân sách; đặt cả hai về không là yêu cầu bất khả thi về chi phí, nên phần việc thật là đàm phán. Ba mức chiến lược theo chi phí tăng dần: chỉ sao lưu và khôi phục, giữ một bản chờ tối thiểu, và chạy song song hai vùng. Nguyên tắc không thoả hiệp: **bản sao lưu chưa khôi phục thử thì chưa phải bản sao lưu**, và diễn tập khôi phục phải có lịch định kỳ chứ làm khi rảnh. Bốn thứ hay bị quên khỏi kế hoạch khôi phục và đều làm kế hoạch thất bại lúc cần: định nghĩa hạ tầng, bí mật, cấu hình bộ điều phối, và chính người biết quy trình.

**Outcome.** Xác định hai con số mục tiêu từ yêu cầu nghiệp vụ, chọn chiến lược tương ứng, và khôi phục thật đạt trong thời gian mục tiêu.

**Đánh giá.** Tầng *đánh giá*. Objective đòi nối một yêu cầu nghiệp vụ với một thiết kế kỹ thuật và chứng minh bằng diễn tập. Kiểm bằng diễn tập khôi phục tính giờ; đạt khi khôi phục xong trong thời gian mục tiêu và dữ liệu mất nằm trong điểm mục tiêu.

**Lab.** Phỏng vấn một người đóng vai bên nghiệp vụ để chốt hai con số. Chọn chiến lược và ước lượng chi phí. Diễn tập: xoá sạch môi trường sản xuất mô phỏng và khôi phục hoàn toàn, tính giờ. Kiểm bốn thứ hay quên có nằm trong kế hoạch không. Ghi lại khoảng cách giữa mục tiêu và thực tế.

**Pitfalls.** Kỹ thuật tự đặt hai con số · tin vào sao lưu chưa từng khôi phục · quên bí mật và định nghĩa hạ tầng khỏi kế hoạch · diễn tập trên môi trường không giống sản xuất.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Khôi phục hoàn tất trong thời gian mục tiêu với lượng dữ liệu mất trong ngưỡng, và bốn thứ hay quên đều có trong kế hoạch.

### Lesson 396 · Data security - classification, encryption and access `TH`
**Prerequisites.** Lesson 395

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bảo vệ dữ liệu bắt đầu bằng phân loại, vì không biết dữ liệu nào nhạy cảm thì không thể bảo vệ đúng mức và bảo vệ mọi thứ ở mức cao nhất thì không ai làm nổi. Ba tới bốn mức phân loại đủ dùng, mỗi mức kèm yêu cầu cụ thể về mã hoá, quyền và ghi nhật ký truy cập. Mã hoá ở hai trạng thái: khi lưu thường bật một công tắc và ít tranh cãi; khi truyền đòi cấu hình ở mọi chặng và hay bị hở ở chặng nội bộ vì nghĩ mạng riêng là an toàn. Quản lý khoá và vì sao khoá do khách hàng quản lý đổi mô hình trách nhiệm. Che và ẩn danh dữ liệu cho môi trường thử: sao chép dữ liệu sản xuất sang môi trường thử là cách lộ dữ liệu phổ biến nhất trong đội dữ liệu, nên phải che trước khi chép. Bảo mật ở mức dòng và mức cột. Ghi nhật ký truy cập cho dữ liệu nhạy cảm và biến nó thành thứ rà được, chứ chỉ bật rồi quên.

**Outcome.** Phân loại dữ liệu của pipeline, áp đúng yêu cầu bảo vệ cho từng mức, và dựng quy trình che dữ liệu cho môi trường thử.

**Đánh giá.** Tầng *áp dụng*. Objective là áp một khung phân loại thành cấu hình cụ thể kiểm được. Kiểm bằng rà soát cộng phép thử truy cập; đạt khi mọi bảng có mức phân loại, dữ liệu thử đã che, và tài khoản thiếu quyền bị từ chối.

**Lab.** Phân loại mọi bảng trong mart. Với mức cao nhất, bật mã hoá, hạn chế quyền và bật nhật ký truy cập. Dựng quy trình che dữ liệu khi chép sang môi trường thử và chứng minh không còn dữ liệu định danh. Thử truy cập bằng tài khoản thiếu quyền và ghi lại kết quả cùng bản ghi nhật ký.

**Pitfalls.** Chép thẳng dữ liệu sản xuất sang môi trường thử · nghĩ mạng riêng thì không cần mã hoá khi truyền · bật nhật ký truy cập mà không ai rà · phân loại mọi thứ ở mức cao nhất.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Mọi bảng có mức phân loại, dữ liệu môi trường thử đã che hết trường định danh, và truy cập trái phép bị từ chối có ghi nhật ký.

### Lesson 397 · Secrets management and rotation `TH`
**Prerequisites.** Lesson 396

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Quy tắc không bao giờ đặt bí mật trong mã đã nêu từ lesson 89 và nhắc lại ở lesson 362 và 368; bài này dựng hệ hoàn chỉnh. Kho bí mật tập trung với ba năng lực cần có: lưu có mã hoá, cấp quyền theo danh tính, và ghi nhật ký mọi lần đọc. Bí mật động là bước tiến đáng kể: kho tự tạo thông tin xác thực có thời hạn ngắn khi ứng dụng cần, nên không có bí mật dài hạn nào tồn tại để mà lộ. Xoay bí mật theo lịch và quy trình xoay không gián đoạn dùng hai bí mật song song trong cửa sổ chuyển tiếp. Quét bí mật trong mã và trong lịch sử kho mã, và lý do phải quét cả lịch sử: xoá ở lần nộp sau không xoá được ở lần nộp trước, nên bí mật vẫn nằm đó. Quy trình khi lộ với thứ tự bắt buộc: xoay trước, điều tra phạm vi sau, vì mỗi phút chậm là thêm rủi ro. Ba chỗ bí mật hay rò rỉ ngoài kho mã: nhật ký, thông báo lỗi, và biến môi trường trong ảnh chụp lỗi.

**Outcome.** Dựng hệ quản lý bí mật có xoay tự động, và thực hiện một lần xoay mà dịch vụ không gián đoạn.

**Đánh giá.** Tầng *áp dụng*. Objective là một cơ chế vận hành kiểm được bằng phép xoay có đo gián đoạn. Kiểm bằng phép xoay thật; đạt khi không yêu cầu nào thất bại trong cửa sổ xoay và quét lịch sử kho mã sạch.

**Lab.** Chuyển mọi bí mật của pipeline vào kho tập trung. Cấu hình ứng dụng lấy bí mật lúc chạy bằng danh tính khối lượng công việc. Thực hiện một lần xoay không gián đoạn và đếm số yêu cầu thất bại. Quét lịch sử kho mã tìm bí mật. Viết quy trình bốn bước khi lộ, đặt xoay ở bước một.

**Pitfalls.** Xoay bí mật bằng cách đổi rồi khởi động lại mọi thứ · chỉ quét mã hiện tại mà không quét lịch sử · điều tra trước khi xoay · ghi bí mật vào nhật ký lỗi.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Lần xoay không gây yêu cầu thất bại nào, quét lịch sử kho mã không còn bí mật, và quy trình khi lộ đặt xoay ở bước đầu.

### Lesson 398 · Privacy - PII, retention and the right to erasure `TH`
**Prerequisites.** Lesson 397

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Dữ liệu cá nhân đặt ra ba nghĩa vụ mà thiết kế kỹ thuật phải đỡ được, và đỡ sau thì rất đắt. Một là biết dữ liệu cá nhân nằm ở đâu: cần danh mục và gắn nhãn ở mức cột, nối với phân loại ở lesson 396 và với siêu dữ liệu ở M26. Hai là giữ đúng thời hạn: chính sách lưu giữ phải thực thi bằng máy qua quy tắc vòng đời ở lesson 378 và qua công việc dọn theo lịch, chứ bằng lời hứa. Ba là xoá theo yêu cầu, và đây là nghĩa vụ khó nhất về kỹ thuật vì dữ liệu một người đã lan qua nhiều bảng, nhiều bản sao lưu và nhiều tệp bất biến trên hồ. Ba kỹ thuật làm nó khả thi: mã hoá theo từng chủ thể rồi xoá khoá, đánh dấu xoá rồi dọn theo lô, và tách dữ liệu định danh sang một bảng riêng để chỉ phải xoá ở một chỗ. Định dạng bảng mở ở M33 giúp phần này vì xoá vài dòng không đòi ghi lại cả phân vùng. Ghi lại đã xoá gì và khi nào, vì phải chứng minh được.

**Outcome.** Định vị mọi dữ liệu cá nhân trong hệ, thực thi được chính sách lưu giữ bằng máy, và hoàn tất một yêu cầu xoá có bằng chứng.

**Đánh giá.** Tầng *áp dụng*. Objective là ba nghĩa vụ chuyển thành cơ chế kỹ thuật kiểm được. Kiểm bằng một yêu cầu xoá thực hiện đầu cuối; đạt khi không còn dấu vết chủ thể ở mọi bảng đích và có bản ghi chứng minh.

**Lab.** Gắn nhãn cột chứa dữ liệu cá nhân trên toàn mart. Dựng quy tắc vòng đời thực thi chính sách lưu giữ. Nhận một yêu cầu xoá cho một chủ thể và thực hiện đầu cuối, gồm cả bảng loại 2 ở lesson 314 và cả hồ dữ liệu. Chứng minh không còn dấu vết bằng truy vấn. Ghi lại bản ghi chứng minh.

**Pitfalls.** Xoá ở mart mà quên hồ dữ liệu và bản sao lưu · thực thi lưu giữ bằng quy trình thủ công · không gắn nhãn ở mức cột nên không biết tìm đâu · xoá mà không ghi lại bằng chứng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Truy vấn kiểm chứng không còn dấu vết chủ thể ở mọi đích, chính sách lưu giữ chạy tự động, và có bản ghi chứng minh việc xoá.

### Lesson 399 · Cost engineering for a data platform `TH`
**Prerequisites.** Lesson 398

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Chi phí là một yêu cầu phi chức năng ngang hàng với hiệu năng, và đội không đo nó thì nó tăng cho tới khi có người cắt ngân sách đột ngột. Bốn nguồn chi phí lớn của nền tảng dữ liệu, xếp theo mức hay bị lãng phí: tính toán để chạy không hoặc chạy quá lâu do chưa tối ưu ở M34, lưu trữ do giữ quá lâu và do tệp nhỏ ở lesson 335, truyền dữ liệu ra khỏi vùng ở lesson 378, và dịch vụ quản lý đặt kích thước dư. Chi phí trên mỗi đơn vị nghiệp vụ là chỉ số chính chứ tổng chi phí, vì nó phân biệt tăng do tăng trưởng với tăng do lãng phí; định nghĩa đơn vị nghiệp vụ phù hợp cho một nền tảng dữ liệu. Quy trình cắt chi phí có phương pháp: gắn nhãn và chia hoá đơn theo thành phần, xếp hạng theo chi phí, xử lý từ trên xuống, và đo lại. Ba khoản cắt được mà không ảnh hưởng dịch vụ và thường cắt được nhanh. Cảnh báo về tối ưu quá đà: cắt tới mức không còn biên an toàn thì sự cố kế tiếp đắt hơn phần đã tiết kiệm.

**Outcome.** Chia hoá đơn theo thành phần, xếp hạng theo chi phí, và thực hiện được ít nhất hai khoản cắt có số đo mà không vi phạm mục tiêu mức dịch vụ.

**Đánh giá.** Tầng *đánh giá*. Objective đòi tối ưu dưới ràng buộc không được hạ chất lượng dịch vụ. Kiểm bằng cặp số đo chi phí và mục tiêu mức dịch vụ; đạt khi chi phí giảm có số và mọi mục tiêu ở lesson 387 vẫn đạt.

**Lab.** Chia hoá đơn theo thành phần bằng nhãn ở lesson 384. Xếp hạng và chọn ba khoản đắt nhất. Thực hiện ít nhất hai khoản cắt. Đo lại chi phí và đo lại cả bốn chỉ báo mức dịch vụ để chứng minh không hạ chất lượng. Định nghĩa và tính chi phí trên mỗi đơn vị nghiệp vụ.

**Pitfalls.** Cắt chi phí bằng cách giảm tài nguyên tới mức mất biên an toàn · theo dõi tổng chi phí mà không chia thành phần · tối ưu khoản nhỏ trước khoản lớn · cắt xong không đo lại chất lượng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chi phí giảm có số, cả bốn chỉ báo mức dịch vụ vẫn đạt sau khi cắt, và có chỉ số chi phí trên mỗi đơn vị nghiệp vụ.

### Lesson 400 · Gate 8 - operate the platform under induced failure `KT`
**Prerequisites.** Lesson 399

**In-class (120 phút).** 75 phút làm bài độc lập · 45 phút chữa bài và phân tích lỗi theo nhóm

**Learn.** Cổng của chặng 7. Bài kiểm năng lực vận hành chứ năng lực xây: hệ đã có sẵn, việc của học viên là giữ nó chạy và xử lý đúng khi nó hỏng. Không có nội dung mới.

**Outcome.** Qua buổi diễn tập sự cố: phát hiện trong ngưỡng, chẩn đoán đúng, khắc phục, thông báo đúng đối tượng, và viết phân tích sau sự cố đạt rà soát.

**Đánh giá.** Tầng *đánh giá*. Cổng đo năng lực dưới áp lực thời gian, nên hình thức là diễn tập trực tiếp có tính giờ cộng sản phẩm viết.

**Lab.** Buổi diễn tập kéo dài 120 phút trên nền tảng đã dựng. Giảng viên gây ba sự cố ở ba mức nghiêm trọng khác nhau. Bài chấm năm phần: A (25đ) phát hiện qua cảnh báo trong ngưỡng, không phải do người dùng báo · B (25đ) chẩn đoán đúng nguyên nhân cả ba, dẫn bằng số đo · C (20đ) khắc phục và chạy lại lịch sử, đối soát khớp · D (20đ) thông báo đúng đối tượng đúng thời điểm, có dòng thời gian · E (10đ) phân tích sau sự cố truy tới tầng hệ thống, hành động có chủ và hạn.

**Pitfalls.** Chẩn đoán trước khi chặn lan rộng · phát hiện sự cố nhờ người dùng báo · sửa xong mà quên chạy lại lịch sử · bỏ phần thông báo vì bận sửa.

**Self-study (2,4 giờ).** Không có bài tự học. Nếu không đạt, theo phụ lục khắc phục khi không đạt cổng

**Done when.** Đạt ≥ 70/100, phần A và D đều ≥ 60%. Sự cố nào người dùng báo trước cảnh báo thì phần A của sự cố đó bằng không.

# MODULE 39 · SYSTEM DESIGN AND DISTRIBUTED SYSTEMS

**Lessons 401–416 · 32 giờ**

| | |
|---|---|
| **Objective cấp module** | Thiết kế một nền tảng dữ liệu từ yêu cầu mơ hồ, bảo vệ được mọi lựa chọn bằng ước lượng và đánh đổi, và giữ hoặc đổi kết luận có lý do khi ràng buộc đổi |
| **Tiền đề** | M38 |
| **Exit criterion** | Qua buổi rà soát thiết kế: ước lượng cùng bậc với thực tế, mọi lựa chọn dẫn được về một ràng buộc, và nêu được ba điều kiện làm thiết kế sai |
| **Kỹ năng SFIA** | `ARCH` mức 5 · `DTAN` mức 4 |
| **Chế độ hỏng** | Vẽ sơ đồ đầy công cụ mà không có ước lượng nào, nên không trả lời được vì sao chọn cái này thay vì cái kia khi bị hỏi |

Module không giới thiệu công cụ mới. Nó dạy cách ghép những thứ đã học thành một hệ có lý do, và cách bảo vệ lý do đó dưới chất vấn.

Tám bài đầu là nền lý thuyết hệ phân tán ở mức đủ để lập luận; tám bài sau là thiết kế và rà soát trên tình huống thật. Mọi ước lượng đều dùng lại số đo từ các lab đã làm, theo đúng luật đặt ở lesson 261.

### Lesson 401 · What distributed means, and the eight fallacies revisited `LT`
**Prerequisites.** Module 39: M38

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Hệ phân tán định nghĩa bằng hệ quả chứ bằng số máy: một hệ là phân tán khi một phần của nó có thể hỏng mà phần còn lại vẫn chạy, và khi đó xuất hiện những trạng thái không có ở hệ một máy. Tám ngộ nhận kinh điển đã gặp ở M4 nay được soi lại bằng kinh nghiệm thật: mạng không đáng tin, độ trễ khác không, băng thông có hạn, mạng không an toàn, hình trạng đổi, có nhiều người quản trị, chi phí vận chuyển khác không, mạng không đồng nhất. Với mỗi ngộ nhận, nối tới một sự cố cụ thể đã tự gặp trong chương trình. Vấn đề trung tâm: **không phân biệt được một nút chết với một nút chậm**, và mọi cơ chế phát hiện hỏng đều là phỏng đoán dựa trên thời gian chờ. Hệ quả trực tiếp là mọi thiết kế đều phải chọn sẽ sai theo hướng nào khi phỏng đoán sai: coi nút còn sống thì có thể treo, coi nút đã chết thì có thể xử lý hai lần.

**Outcome.** Nối mỗi ngộ nhận với một sự cố đã gặp trong chương trình, và giải thích vì sao không phân biệt được nút chết với nút chậm.

**Đánh giá.** Tầng *hiểu*. Bài mở module, soi lại kinh nghiệm đã có bằng một khung khái niệm. Kiểm bằng bài nối có dẫn chứng; đạt khi nối đúng ít nhất sáu ngộ nhận với sự cố cụ thể kèm số bài.

**Lab.** Với mỗi ngộ nhận trong tám, tìm một sự cố đã tự gặp ở các module trước, ghi số bài và biểu hiện. Với hai ngộ nhận không tìm được sự cố tương ứng, thiết kế một thí nghiệm nhỏ để tạo ra nó.

**Pitfalls.** Coi tám ngộ nhận là danh sách để thuộc · nghĩ mạng trong một trung tâm dữ liệu thì đáng tin · tin rằng thời gian chờ đủ dài sẽ phân biệt được chết với chậm.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Nối đúng ≥ 6/8 ngộ nhận với sự cố cụ thể kèm số bài, và giải thích đúng vì sao chết và chậm không phân biệt được.

### Lesson 402 · CAP, PACELC and what they do and do not tell you `LT`
**Prerequisites.** Lesson 401

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Định lý CAP hay bị dùng sai nên phải phát biểu chính xác: khi có phân mảnh mạng, hệ phải chọn giữa tiếp tục phục vụ với dữ liệu có thể cũ và từ chối phục vụ để giữ nhất quán. Ba điều CAP **không** nói và đây là phần quan trọng hơn: nó không nói chọn hai trong ba như cách vẽ tam giác phổ biến, nó không áp dụng khi mạng bình thường, và nó không phải thang đo chất lượng. PACELC bổ sung phần CAP bỏ trống: khi mạng bình thường, hệ vẫn phải chọn giữa độ trễ và nhất quán, và đây mới là lựa chọn ảnh hưởng tới thiết kế hằng ngày. Áp vào hệ dữ liệu: kho phân tích thường chấp nhận dữ liệu cũ vài phút nên chọn sẵn sàng; hệ ghi giao dịch thường chọn nhất quán. Phân mảnh là chuyện hiếm nhưng xảy ra, nên câu hỏi đúng cho thiết kế là hệ sẽ hành xử ra sao trong vài phút phân mảnh, chứ có chọn CAP hay không.

**Outcome.** Phát biểu đúng CAP cùng ba điều nó không nói, và với ba hệ cho trước nêu hệ đó nghiêng về phía nào khi phân mảnh và khi bình thường.

**Đánh giá.** Tầng *hiểu*. Objective gồm cả việc bác bỏ cách hiểu sai phổ biến, vì hiểu sai dẫn tới lập luận sai trong rà soát thiết kế. Kiểm bằng bài phân tích ba hệ; đạt khi phát biểu đúng và phân loại đúng ít nhất hai hệ ở cả hai tình huống.

**Lab.** Cho ba hệ đã dùng trong chương trình gồm PostgreSQL có bản sao, Kafka, và kho đối tượng. Với mỗi hệ, nêu hành vi khi phân mảnh và lựa chọn khi mạng bình thường, dẫn bằng cấu hình cụ thể đã đặt ở các module trước. Viết ba câu bác bỏ cách hiểu chọn hai trong ba.

**Pitfalls.** Dùng tam giác chọn hai trong ba · coi CAP là thang chất lượng · quên rằng lựa chọn khi mạng bình thường mới là lựa chọn hằng ngày.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Phát biểu đúng CAP kèm ba điều nó không nói, và phân loại đúng ≥ 2/3 hệ ở cả hai tình huống kèm cấu hình dẫn chứng.

### Lesson 403 · Consistency models from linearizable to eventual `LT`
**Prerequisites.** Lesson 402

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Nhất quán không phải bật tắt mà là một dải, và biết mình đang ở đâu trên dải quyết định bên dùng thấy gì. Bốn mức đủ dùng, xếp từ chặt tới lỏng: tuyến tính hoá nghĩa là hệ hành xử như chỉ có một bản sao duy nhất; nhất quán tuần tự giữ thứ tự nhưng cho phép chậm; nhất quán nhân quả giữ quan hệ nguyên nhân kết quả; nhất quán cuối cùng chỉ hứa các bản sao hội tụ nếu ngừng ghi. Bốn bảo đảm phiên thường đủ cho hệ thực tế và rẻ hơn nhiều: đọc thấy thứ mình vừa ghi, đọc đơn điệu, ghi đơn điệu, và đọc sau ghi. Với hệ dữ liệu, chỗ đau thường gặp đã gặp ở lesson 120: ghi vào bản chính rồi đọc ngay ở bản sao thì không thấy, nên pipeline đọc bản sao phải chịu được điều đó hoặc phải đọc bản chính cho bước kiểm chứng. Cái giá của nhất quán chặt là độ trễ và giảm sẵn sàng, nên chọn mức chặt cho mọi thứ là cách làm hệ chậm mà không thêm giá trị.

**Outcome.** Chọn mức nhất quán cần thiết cho từng phần của một hệ dữ liệu và nêu hậu quả quan sát được nếu chọn mức lỏng hơn.

**Đánh giá.** Tầng *đánh giá*. Objective đòi cân giữa độ chặt và chi phí theo từng phần chứ áp một mức cho cả hệ. Kiểm bằng bốn phần của một hệ; đạt khi chọn đúng ít nhất ba và mỗi lần nêu hậu quả cụ thể.

**Lab.** Cho một hệ gồm bốn phần: ghi giao dịch, đọc cho bảng điều khiển, kiểm chứng đối soát, và phân tích theo lô. Chọn mức nhất quán cho từng phần. Tái hiện hiện tượng đọc không thấy thứ vừa ghi trên bản sao và đo cửa sổ thời gian xảy ra hiện tượng đó.

**Pitfalls.** Chọn tuyến tính hoá cho mọi thứ · dùng nhất quán cuối cùng cho bước đối soát · không đo độ trễ bản sao rồi giả định nó nhỏ.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chọn đúng mức cho ≥ 3/4 phần kèm hậu quả cụ thể, và có số đo cửa sổ thời gian đọc không thấy thứ vừa ghi.

### Lesson 404 · Consensus - replicated log, leader election and quorum `LT`
**Prerequisites.** Lesson 403

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Đồng thuận là bài toán nhiều nút cùng thống nhất một giá trị dù có nút hỏng, và nó là nền của gần như mọi thứ đã dùng: bầu trưởng phân vùng trong Kafka ở lesson 297, hàng đợi quorum ở lesson 286, và bộ điều khiển trong Kubernetes ở lesson 366. Ý tưởng chung của các thuật toán thực dụng: bầu một trưởng, trưởng nhận mọi lệnh ghi và nhân bản thành một nhật ký có thứ tự, và một lệnh được coi là chốt khi đa số đã ghi. Vì sao đa số là ngưỡng: hai đa số bất kỳ luôn giao nhau nên không thể có hai quyết định mâu thuẫn cùng được chốt. Hệ quả thực tế cần nhớ khi thiết kế: cụm ba nút chịu được một nút chết, cụm năm nút chịu được hai, và **cụm chẵn nút không tốt hơn cụm lẻ nhỏ hơn liền kề**. Não phân đôi xảy ra khi hai phần cùng tin mình là trưởng, và cơ chế nhiệm kỳ cùng đa số là thứ ngăn nó. Cái giá: mỗi lần ghi phải chờ đa số nên độ trễ bị neo vào nút chậm thứ hai.

**Outcome.** Tính số nút chịu lỗi được của một cụm cho trước, và chỉ ra trong bốn hệ đã dùng chỗ nào đang dựa vào đồng thuận.

**Đánh giá.** Tầng *hiểu*. Objective là nắm cơ chế đủ để đọc cấu hình cụm và suy ra khả năng chịu lỗi. Kiểm bằng bài tính cộng bài định vị; đạt khi tính đúng cả bốn cấu hình và định vị đúng ít nhất ba hệ.

**Lab.** Cho bốn cấu hình cụm với số nút khác nhau, tính số nút chịu lỗi được và giải thích vì sao cụm bốn nút không hơn cụm ba nút. Trong bốn hệ đã dùng, chỉ ra chỗ nào dựa vào đồng thuận và đọc cấu hình thật để biết cụm hiện chịu được mấy nút chết.

**Pitfalls.** Dựng cụm chẵn nút · nghĩ thêm nút luôn tăng khả năng chịu lỗi · quên rằng độ trễ ghi phụ thuộc nút chậm thứ hai · tin rằng đồng thuận loại bỏ được mọi khả năng mất dữ liệu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tính đúng khả năng chịu lỗi cả bốn cấu hình, và định vị đúng ≥ 3/4 chỗ dựa vào đồng thuận trong hệ đã dựng.

### Lesson 405 · Time, ordering and causality in a distributed system `LT`
**Prerequisites.** Lesson 404

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Đồng hồ trên các máy khác nhau luôn lệch, nên dấu thời gian từ hai máy không so được một cách đáng tin, và đây là gốc của nhiều lỗi khó tìm. Hai loại đồng hồ và cách dùng đúng: đồng hồ theo giờ thật có thể nhảy lùi khi đồng bộ nên không được dùng để đo khoảng thời gian; đồng hồ đơn điệu chỉ tăng nên dùng để đo khoảng. Lỗi điển hình trong hệ dữ liệu: khử trùng hoặc chọn bản mới nhất bằng cách so dấu thời gian từ nhiều nguồn, và khi đồng hồ lệch thì chọn nhầm bản cũ. Thứ tự nhân quả và cách ghi nó mà không dựa vào đồng hồ: số thứ tự theo nguồn, hoặc đồng hồ logic. Nối lại thời gian sự kiện và thời gian xử lý ở lesson 317: đó chính là biểu hiện của vấn đề này ở tầng ứng dụng. Ba quy tắc thực dụng: không so dấu thời gian từ hai máy để quyết định thứ tự, dùng số thứ tự của nguồn khi có, và luôn lưu cả dấu thời gian nguồn lẫn dấu thời gian nhận.

**Outcome.** Chỉ ra trong một thiết kế cho trước chỗ nào đang dựa vào đồng hồ để quyết định thứ tự, và đề xuất cơ chế thay thế.

**Đánh giá.** Tầng *phân tích*. Objective là phát hiện một loại lỗi tiềm ẩn khó tái hiện, kỹ năng dùng trong rà soát thiết kế. Kiểm bằng ba thiết kế có lỗi; đạt khi chỉ đúng ít nhất hai và đề xuất cơ chế thay thế đúng.

**Lab.** Cho ba thiết kế dùng dấu thời gian để chọn bản ghi mới nhất. Với mỗi cái, chỉ ra kịch bản đồng hồ lệch làm nó chọn sai, và đề xuất thay thế. Mô phỏng lệch đồng hồ giữa hai nguồn và tái hiện một lần chọn sai trong bảng loại 2 ở lesson 314.

**Pitfalls.** Dùng dấu thời gian giờ thật để đo khoảng · so dấu thời gian từ hai nguồn để quyết định thứ tự · giả định đồng bộ đồng hồ là đủ chính xác.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chỉ đúng ≥ 2/3 thiết kế có lỗi kèm cơ chế thay thế, và tái hiện được một lần chọn sai do lệch đồng hồ.

### Lesson 406 · Partitioning and rebalancing at the system level `LT`
**Prerequisites.** Lesson 405

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Chia dữ liệu ra nhiều nút là cách duy nhất vượt giới hạn một máy, và ba chiến lược chia đã gặp dưới nhiều tên: theo khoảng khoá, theo băm của khoá, và theo danh mục tra cứu. Theo khoảng giữ được truy vấn theo dải nhưng dễ tạo điểm nóng khi khoá tăng dần, ví dụ khoá là dấu thời gian thì mọi ghi mới dồn vào một phân vùng. Theo băm chia đều hơn nhưng mất khả năng truy vấn theo dải. Bài toán chung đã gặp ba lần trong chương trình: phân vùng Kafka ở lesson 293, phân vùng Spark ở lesson 351, và phân vùng bảng ở lesson 336; điểm chung là **số phân vùng cố định thì cân bằng lại tốn kém, số phân vùng linh hoạt thì phức tạp hơn**. Băm nhất quán giảm lượng dữ liệu phải di chuyển khi thêm hoặc bớt nút. Cân bằng lại nên là thao tác có kiểm soát chứ tự động hoàn toàn, vì cân bằng lại lúc hệ đang tải nặng làm mọi thứ tệ hơn.

**Outcome.** Chọn chiến lược chia cho ba khối lượng công việc và nêu chi phí cân bằng lại khi thêm nút.

**Đánh giá.** Tầng *đánh giá*. Objective đòi chọn có cân nhắc giữa khả năng truy vấn và độ đều, chứ áp một chiến lược. Kiểm bằng ba khối lượng công việc; đạt khi chọn đúng cả ba và ước lượng đúng hướng chi phí cân bằng lại.

**Lab.** Cho ba khối lượng công việc có mẫu truy vấn khác nhau. Chọn chiến lược chia cho từng cái. Mô phỏng phân bố khoá thật và đo độ đều của hai chiến lược. Tính lượng dữ liệu phải di chuyển khi thêm một nút, với băm thường và với băm nhất quán.

**Pitfalls.** Chia theo khoá tăng dần rồi tạo điểm nóng · dùng băm khi cần truy vấn theo dải · cân bằng lại tự động lúc tải cao · quên chi phí di chuyển dữ liệu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chọn đúng chiến lược cho cả ba khối lượng công việc, và có số so lượng dữ liệu di chuyển giữa hai cách băm.

### Lesson 407 · Replication strategies and the read path `LT`
**Prerequisites.** Lesson 406

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Nhân bản phục vụ ba mục đích khác nhau và trộn lẫn chúng dẫn tới thiết kế sai: chịu lỗi, tăng khả năng đọc, và đặt dữ liệu gần người dùng. Ba kiểu và hệ quả: một trưởng nhiều bản sao là kiểu phổ biến nhất và đơn giản nhất về nhất quán, ghi qua một chỗ nên trưởng là nút thắt ghi; nhiều trưởng cho phép ghi ở nhiều nơi nhưng sinh xung đột phải giải; không trưởng dùng ghi và đọc theo đa số. Nhân bản đồng bộ bảo đảm không mất dữ liệu khi trưởng chết nhưng neo độ trễ ghi vào bản sao chậm nhất; bất đồng bộ nhanh nhưng có cửa sổ mất dữ liệu, và cửa sổ đó chính là điểm khôi phục ở lesson 395. Đường đọc là nơi quyết định người dùng thấy gì: đọc từ trưởng thì luôn mới nhưng không giảm tải, đọc từ bản sao thì giảm tải nhưng có thể cũ, đọc theo đa số thì mới nhưng tốn. Ba mẫu thực dụng cho hệ dữ liệu.

**Outcome.** Chọn kiểu nhân bản và đường đọc cho một yêu cầu cho trước, và nêu cửa sổ mất dữ liệu tương ứng.

**Đánh giá.** Tầng *đánh giá*. Objective đòi nối lựa chọn kỹ thuật với hai con số mục tiêu khôi phục ở lesson 395. Kiểm bằng ba yêu cầu; đạt khi chọn đúng cả ba và nêu đúng cửa sổ mất dữ liệu của từng lựa chọn.

**Lab.** Cho ba yêu cầu khác nhau về độ mới và độ chịu lỗi. Chọn kiểu nhân bản và đường đọc cho từng cái. Trên cụm PostgreSQL đã dựng, đo độ trễ ghi ở chế độ đồng bộ và bất đồng bộ, và đo cửa sổ mất dữ liệu bằng cách giết trưởng lúc đang ghi.

**Pitfalls.** Dùng bản sao để giảm tải mà không xét độ trễ bản sao · chọn nhân bản bất đồng bộ cho dữ liệu không được mất · nghĩ nhân bản thay được sao lưu.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Chọn đúng cả ba yêu cầu, và có số đo cửa sổ mất dữ liệu thực tế khi giết trưởng ở chế độ bất đồng bộ.

### Lesson 408 · Caching and invalidation in a data platform `TH`
**Prerequisites.** Lesson 407

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bộ nhớ đệm đổi độ mới lấy độ trễ và chi phí, nên câu hỏi thiết kế luôn là chấp nhận dữ liệu cũ tới mức nào. Bốn tầng đệm trong một nền tảng dữ liệu: đệm kết quả truy vấn ở tầng phục vụ, bảng tổng hợp dựng sẵn, đệm ở tầng ứng dụng, và đệm trang của hệ điều hành đã gặp ở M2. Ba chiến lược làm mới và điều kiện dùng: hết hạn theo thời gian là đơn giản nhất và đủ cho phần lớn bảng điều khiển; vô hiệu hoá theo sự kiện chính xác hơn nhưng đòi biết ai phụ thuộc vào cái gì, và đây là chỗ lineage ở M26 trả cổ tức; dựng lại theo lịch phù hợp với bảng tổng hợp. Ba vấn đề kinh điển: đệm rỗng đồng loạt khi nhiều yêu cầu cùng thấy hết hạn và cùng dựng lại, dữ liệu cũ phục vụ lâu hơn dự kiến vì quên vô hiệu hoá một nhánh, và đệm chứa dữ liệu nhạy cảm không được phân quyền. Đo tỉ lệ trúng đệm và chi phí tiết kiệm để biết đệm có đáng giữ không.

**Outcome.** Thiết kế tầng đệm cho bảng điều khiển với chiến lược làm mới phù hợp, và đo tỉ lệ trúng cùng độ mới thực tế.

**Đánh giá.** Tầng *áp dụng*. Objective là một thiết kế có hai đại lượng đo được và ràng buộc về độ mới. Kiểm bằng cặp số đo; đạt khi tỉ lệ trúng trên ngưỡng và độ mới trong cam kết ở lesson 387.

**Lab.** Thêm tầng đệm cho bảng điều khiển đọc mart. Thử cả ba chiến lược làm mới, với mỗi chiến lược đo tỉ lệ trúng, độ trễ và độ mới thực tế. Tạo tình huống đệm rỗng đồng loạt và quan sát tải lên kho. Thêm cơ chế chặn và đo lại.

**Pitfalls.** Đặt thời gian hết hạn dài cho dữ liệu cần mới · vô hiệu hoá theo sự kiện mà không có lineage đầy đủ · đệm dữ liệu nhạy cảm không phân quyền · giữ đệm mà chưa từng đo tỉ lệ trúng.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Tỉ lệ trúng trên ngưỡng, độ mới nằm trong cam kết, và cơ chế chặn đệm rỗng đồng loạt giảm được đỉnh tải có số.

### Lesson 409 · Idempotency, deduplication and the outbox pattern `TH`
**Prerequisites.** Lesson 408

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài gom một nguyên tắc đã xuất hiện ở tám module thành một bộ công cụ thiết kế. Ghi bất biến là điều kiện nền cho mọi thứ khác: thử lại an toàn, chạy bù an toàn, phát lại an toàn. Ba cách cài đặt và điều kiện áp dụng: khoá tự nhiên từ nghiệp vụ ở lesson 208 là cách bền nhất; khoá do bên gửi sinh dùng khi không có khoá nghiệp vụ; bảng đã xử lý dùng khi đích không hỗ trợ ghi đè theo khoá. Mẫu hộp thư đi giải một bài toán cụ thể và phổ biến: ghi vào cơ sở dữ liệu rồi phát một sự kiện là hai thao tác trên hai hệ, nên chết giữa chừng làm hai bên lệch nhau; giải bằng cách ghi sự kiện vào một bảng trong cùng giao dịch với dữ liệu, rồi một tiến trình riêng đọc bảng đó và phát đi, thường bằng CDC ở M31. Nhờ vậy chỉ còn một thao tác nguyên tử. Ba biến thể và chi phí của từng biến thể.

**Outcome.** Cài đặt mẫu hộp thư đi cho một tuyến ghi rồi phát sự kiện, và chứng minh bằng thí nghiệm hỏng rằng cơ sở dữ liệu và luồng không lệch nhau.

**Đánh giá.** Tầng *sáng tạo*. Objective đòi ghép giao dịch, CDC và ghi bất biến thành một mẫu giải bài toán hai hệ. Kiểm bằng thí nghiệm giết tiến trình; đạt khi qua mười lần giết mà không có sự kiện thiếu hoặc thừa so với bản ghi.

**Lab.** Cài tuyến ghi đơn hàng rồi phát sự kiện theo cách ngây thơ, giết tiến trình giữa hai thao tác và đếm mức lệch. Cài lại bằng mẫu hộp thư đi dùng CDC. Giết tiến trình mười lần ở các thời điểm khác nhau và đối soát số sự kiện với số bản ghi.

**Pitfalls.** Ghi cơ sở dữ liệu rồi phát sự kiện trong hai thao tác rời · dùng giao dịch phân tán khi mẫu hộp thư đi đủ · quên dọn bảng hộp thư nên nó phình.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bản ngây thơ định lượng được mức lệch, bản hộp thư đi qua mười lần giết mà số sự kiện khớp số bản ghi tuyệt đối.

### Lesson 410 · Backpressure and load shedding across services `TH`
**Prerequisites.** Lesson 409

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Áp lực ngược trong một engine đã gặp ở lesson 326; bài này mở rộng ra giữa các dịch vụ, nơi không có cơ chế tự động nào. Khi bên nhận chậm hơn bên gửi, có đúng bốn lựa chọn và phải chọn một cách có ý thức: đệm lại và chấp nhận độ trễ tăng, làm chậm bên gửi, từ chối bớt yêu cầu, hoặc giảm chất lượng dịch vụ. Đệm vô hạn là lựa chọn tệ nhất và cũng là mặc định phổ biến nhất, vì nó biến một sự cố chậm thành một sự cố hết bộ nhớ, đúng vấn đề hàng đợi không giới hạn ở M6. Giảm tải chủ động: từ chối một phần để phần còn lại được phục vụ đúng, và tiêu chí chọn từ chối cái gì phải do nghiệp vụ quyết chứ ngẫu nhiên. Hàng đợi có giới hạn cộng chính sách khi đầy là cách cài đặt thực tế. Nối với bộ ngắt mạch ở lesson 394: ngắt mạch bảo vệ bên gọi, giảm tải bảo vệ bên bị gọi, và hệ cần cả hai.

**Outcome.** Chọn và cài đặt chiến lược xử lý quá tải cho một tuyến, và chứng minh hệ suy giảm có kiểm soát thay vì sụp.

**Đánh giá.** Tầng *áp dụng*. Objective là một cơ chế phòng vệ kiểm được bằng thí nghiệm quá tải. Kiểm bằng phép thử tải gấp năm lần công suất; đạt khi hệ vẫn phục vụ phần được ưu tiên và không có thành phần nào hết bộ nhớ.

**Lab.** Đẩy tải gấp năm lần công suất vào tuyến xử lý. Quan sát hành vi với hàng đợi không giới hạn và ghi lại điều gì hỏng trước. Thay bằng hàng đợi có giới hạn cộng chính sách giảm tải theo mức ưu tiên nghiệp vụ. Đo tỉ lệ phục vụ của phần ưu tiên cao ở cả hai cấu hình.

**Pitfalls.** Để hàng đợi không giới hạn · giảm tải ngẫu nhiên thay vì theo ưu tiên nghiệp vụ · tăng tài nguyên thay vì đặt giới hạn · thử lại ngay khi bị từ chối.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Cấu hình có giới hạn giữ được tỉ lệ phục vụ của phần ưu tiên cao ở mức chấp nhận được, và không thành phần nào hết bộ nhớ.

### Lesson 411 · Estimating - back of the envelope for a data platform `TH`
**Prerequisites.** Lesson 410

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Ước lượng nhanh là kỹ năng phân biệt bản thiết kế có cơ sở với bản thiết kế là danh sách công cụ, và nó được hỏi trong gần như mọi buổi phỏng vấn thiết kế. Quy trình năm bước: từ số liệu nghiệp vụ suy ra số sự kiện mỗi giây, nhân kích thước bản ghi ra thông lượng byte, nhân thời gian giữ ra dung lượng, nhân hệ số nhân bản và hệ số phình khi xử lý, rồi quy ra số máy và chi phí. Bộ số mốc cần thuộc để ước lượng mà không tra: độ trễ đọc bộ nhớ, đọc đĩa thể rắn, gọi mạng trong trung tâm dữ liệu, gọi qua Internet, và thông lượng một nút Kafka hay một trình thực thi Spark, tất cả đều đã tự đo trong chương trình nên dùng số của chính mình. Nguyên tắc: đúng bậc độ lớn là đủ, và **mọi ước lượng phải nêu giả định**, vì người rà soát kiểm giả định chứ kiểm phép nhân. Ba chỗ hay sai: quên hệ số nhân bản, quên đỉnh tải so với trung bình, và quên dữ liệu phình khi giải nén.

**Outcome.** Ước lượng dung lượng, thông lượng và chi phí cho một yêu cầu nghiệp vụ cho trước, nêu rõ giả định, và cùng bậc với số đo thật.

**Đánh giá.** Tầng *áp dụng*. Objective là một quy trình tính có kiểm chứng được bằng đối chiếu với lab. Kiểm bằng so ước lượng với thực đo; đạt khi cùng bậc độ lớn ở ít nhất bốn trong năm đại lượng và mọi giả định được nêu.

**Lab.** Cho một yêu cầu nghiệp vụ. Ước lượng năm đại lượng theo quy trình năm bước, ghi rõ giả định từng bước. Đối chiếu với số đo thật từ các lab đã làm. Lập bảng ước lượng và thực đo, giải thích mọi chỗ lệch quá một bậc.

**Pitfalls.** Ước lượng mà không nêu giả định · dùng số trung bình cho đỉnh tải · quên hệ số nhân bản · tra số trên mạng thay vì dùng số đã tự đo.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ước lượng cùng bậc với thực đo ở ≥ 4/5 đại lượng, mọi giả định được nêu, và chỗ lệch quá một bậc có giải thích.

### Lesson 412 · Designing for a read-heavy analytics workload `TH`
**Prerequisites.** Lesson 411

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài thiết kế đầu, trên loại khối lượng công việc quen thuộc nhất. Yêu cầu: hàng trăm người dùng chạy truy vấn phân tích trên dữ liệu vài chục terabyte, độ tươi trong vài giờ là đủ, ngân sách có hạn. Quy trình thiết kế sáu bước dùng lại cho cả ba bài: làm rõ yêu cầu bằng câu hỏi, ước lượng theo lesson 411, vẽ luồng dữ liệu từ nguồn tới người dùng, chọn thành phần cho từng chặng kèm lý do, nêu chế độ hỏng và cách chặn, rồi nêu điều kiện làm thiết kế này sai. Các lựa chọn chính phải bảo vệ được: bố trí lưu trữ theo M33, tách tầng phục vụ khỏi tầng xử lý, chiến lược đệm và bảng tổng hợp theo lesson 408, và cách kiểm soát chi phí khi nhiều người chạy truy vấn nặng. Chỗ hay sai ở loại khối lượng công việc này: thiết kế cho đỉnh tải cùng lúc thay vì cho tải trung bình cộng khả năng co giãn.

**Outcome.** Trình bày một thiết kế đầy đủ sáu bước cho khối lượng công việc đọc nặng, và bảo vệ được ít nhất ba lựa chọn dưới chất vấn.

**Đánh giá.** Tầng *sáng tạo*. Objective là tổng hợp toàn chương trình thành một thiết kế có lý do. Kiểm bằng buổi trình bày có chất vấn; đạt khi sáu bước đầy đủ và ba lựa chọn được bảo vệ bằng ước lượng hoặc số đo.

**Lab.** Nhận yêu cầu, chạy sáu bước, trình bày trong 20 phút. Hai bạn cùng lớp chất vấn ba lựa chọn bất kỳ. Nộp bản thiết kế gồm sơ đồ luồng dữ liệu, bảng ước lượng, bảng chế độ hỏng, và ba điều kiện làm thiết kế sai.

**Pitfalls.** Vẽ sơ đồ trước khi làm rõ yêu cầu · liệt kê công cụ mà không nêu lý do · thiết kế cho đỉnh tải cùng lúc · bỏ phần điều kiện làm thiết kế sai.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bản thiết kế đủ sáu bước, ba lựa chọn được bảo vệ bằng ước lượng hoặc số đo, và nêu được ba điều kiện làm thiết kế sai.

### Lesson 413 · Designing a real-time pipeline under a latency budget `TH`
**Prerequisites.** Lesson 412

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài thiết kế thứ hai, với ràng buộc độ trễ làm đổi gần như mọi lựa chọn. Yêu cầu: phát hiện giao dịch bất thường trong vòng vài giây kể từ lúc phát sinh. Kỹ thuật trung tâm là **phân bổ ngân sách độ trễ**: chia tổng ngân sách cho từng chặng gồm sinh sự kiện, vận chuyển, xử lý, tra cứu làm giàu, và ghi kết quả; rồi kiểm tổng có vừa không. Phân bổ xong thì mỗi chặng thành một ràng buộc kiểm được, và chặng nào không đạt thì phải đổi thiết kế chứ hy vọng. Các lựa chọn phải bảo vệ: engine luồng thuần hay lô vi mô theo lesson 327 và 354, cách làm giàu không tra cứu đồng bộ theo lesson 324, chu kỳ điểm kiểm tra ảnh hưởng độ trễ đầu cuối theo lesson 322, và mức ngữ nghĩa giao nhận cần thiết. Câu hỏi phải trả lời được: chuyện gì xảy ra khi một chặng vượt ngân sách, và hệ suy giảm ra sao thay vì sụp.

**Outcome.** Phân bổ ngân sách độ trễ cho từng chặng, chứng minh tổng vừa ngân sách bằng số đo, và nêu hành vi suy giảm khi một chặng vượt.

**Đánh giá.** Tầng *sáng tạo*. Objective đòi thiết kế dưới một ràng buộc định lượng cứng. Kiểm bằng bảng ngân sách đối chiếu số đo; đạt khi tổng đo được nằm trong ngân sách và có phương án suy giảm cụ thể.

**Lab.** Nhận yêu cầu có ngân sách độ trễ. Phân bổ cho năm chặng. Với mỗi chặng, dẫn một số đo từ lab đã làm để chứng minh khả thi. Trình bày và chất vấn. Nêu hành vi của hệ khi chặng làm giàu vượt ngân sách gấp ba lần.

**Pitfalls.** Đặt ngân sách tổng mà không chia chặng · dùng tra cứu đồng bộ trong đường nóng · quên chu kỳ điểm kiểm tra khi tính độ trễ · không có phương án suy giảm.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bảng ngân sách năm chặng đều có số đo hỗ trợ, tổng nằm trong ngân sách, và có phương án suy giảm cụ thể.

### Lesson 414 · Designing for multi-tenancy and isolation `TH`
**Prerequisites.** Lesson 413

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Bài thiết kế thứ ba, trên ràng buộc ít được dạy nhưng gặp thường xuyên: nhiều khách hàng hoặc nhiều phòng ban dùng chung một nền tảng. Ba mức cô lập theo chi phí tăng dần: chung mọi thứ và tách bằng cột định danh, chung hạ tầng nhưng tách lược đồ hoặc cơ sở dữ liệu, và tách hoàn toàn. Bốn khía cạnh phải xét riêng chứ gộp: cô lập dữ liệu để bên này không đọc được dữ liệu bên kia, cô lập hiệu năng để một bên chạy truy vấn nặng không làm chậm bên khác, cô lập chi phí để tính được ai tốn bao nhiêu, và cô lập vận hành để nâng cấp cho một bên không ảnh hưởng bên khác. Vấn đề hàng xóm ồn ào và ba cơ chế chặn: hạn mức tài nguyên, hàng đợi riêng theo mức ưu tiên, và giới hạn tốc độ. Bảo mật mức dòng theo lesson 396 là cách rẻ nhất cho cô lập dữ liệu nhưng không cho cô lập hiệu năng, nên nói rõ nó giải được gì.

**Outcome.** Chọn mức cô lập cho bốn khía cạnh theo yêu cầu cho trước, và chứng minh bằng thí nghiệm rằng hàng xóm ồn ào không làm hỏng bên còn lại.

**Đánh giá.** Tầng *đánh giá*. Objective đòi quyết định riêng cho từng khía cạnh thay vì chọn một mức cho tất cả. Kiểm bằng bảng bốn khía cạnh cộng thí nghiệm; đạt khi bốn quyết định có lý do và thí nghiệm hàng xóm ồn ào cho kết quả trong ngưỡng.

**Lab.** Cho yêu cầu nhiều bên dùng chung. Quyết định mức cô lập cho từng khía cạnh trong bốn, kèm chi phí. Cài hạn mức tài nguyên. Chạy một truy vấn rất nặng ở bên A và đo ảnh hưởng lên độ trễ của bên B, trước và sau khi có hạn mức.

**Pitfalls.** Chọn một mức cô lập cho cả bốn khía cạnh · dùng bảo mật mức dòng rồi tưởng đã cô lập hiệu năng · không tính được chi phí theo từng bên · bỏ qua cô lập vận hành khi nâng cấp.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Bốn quyết định có lý do và chi phí kèm theo, và độ trễ bên B sau khi có hạn mức nằm trong ngưỡng dù bên A chạy truy vấn nặng.

### Lesson 415 · Writing an architecture decision record that survives review `TH`
**Prerequisites.** Lesson 414

**In-class (120 phút).** 20 phút ôn bài trước · 30 phút hướng dẫn từng bước · 55 phút tự làm · 15 phút rà lỗi chung

**Learn.** Tài liệu quyết định kiến trúc là thứ giữ lại lý do khi người ra quyết định đã rời đi, và đây là phần có giá trị dài hạn nhất của cả module. Cấu trúc năm phần: bối cảnh và ràng buộc, các phương án đã cân nhắc, quyết định, hệ quả gồm cả mặt tốt lẫn mặt xấu, và điều kiện xem lại. Phần các phương án bị loại là phần **giá trị nhất và hay bị bỏ nhất**: người đọc sau cần biết phương án kia đã được xét và loại vì lý do gì, nếu không họ sẽ đề xuất lại đúng phương án đó. Điều kiện xem lại làm tài liệu này khác một biên bản: ghi rõ mốc nào thì quyết định này nên được xét lại, ví dụ khi khối lượng vượt một ngưỡng hoặc khi đội vượt một quy mô. Viết ngắn và cụ thể; tài liệu mười trang không ai đọc. Nộp vào kho mã cùng mã nguồn, đánh số, và không sửa tài liệu cũ mà viết tài liệu mới thay thế nó.

**Outcome.** Viết một tài liệu quyết định kiến trúc đủ năm phần cho một lựa chọn đã làm, và qua được rà soát chéo về phần phương án bị loại.

**Đánh giá.** Tầng *áp dụng*. Objective là một sản phẩm viết theo chuẩn, kiểm được bằng rà soát của người không dự buổi quyết định. Kiểm bằng rà soát chéo; đạt khi người rà soát hiểu được lý do mà không cần hỏi thêm và điều kiện xem lại là kiểm được.

**Lab.** Chọn ba quyết định lớn đã làm trong các module trước. Viết tài liệu cho từng quyết định, đủ năm phần, mỗi tài liệu dưới hai trang. Đổi bài với một học viên khác: họ đọc và ghi lại mọi câu hỏi còn phải hỏi. Sửa cho tới khi không còn câu hỏi nào về lý do.

**Pitfalls.** Bỏ phần phương án bị loại · viết hệ quả chỉ có mặt tốt · đặt điều kiện xem lại chung chung · sửa tài liệu cũ thay vì viết bản thay thế.

**Self-study (2,4 giờ).** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Done when.** Ba tài liệu đủ năm phần và dưới hai trang, và người rà soát không còn câu hỏi nào về lý do quyết định.

### Lesson 416 · Design review - defend a design under changing constraints `KT`
**Prerequisites.** Lesson 415

**In-class (120 phút).** 75 phút làm bài độc lập · 45 phút chữa bài và phân tích lỗi theo nhóm

**Learn.** Cổng của chặng 8. Bài kiểm năng lực thiết kế và bảo vệ, không có nội dung mới.

**Outcome.** Bảo vệ được một thiết kế nền tảng dữ liệu dưới chất vấn, và phản ứng đúng khi hội đồng đổi một ràng buộc giữa buổi.

**Đánh giá.** Tầng *đánh giá*. Cổng đo năng lực ra quyết định kiến trúc có bằng chứng dưới chất vấn, nên hình thức là buổi bảo vệ trực tiếp.

**Lab.** Nhận một yêu cầu nền tảng dữ liệu chưa rõ ràng, 30 phút chuẩn bị, 30 phút bảo vệ. Bài chấm năm phần: A (20đ) làm rõ yêu cầu bằng câu hỏi đúng trước khi vẽ · B (25đ) ước lượng năm đại lượng, nêu giả định, cùng bậc với số đo đã có · C (25đ) lựa chọn thành phần, mỗi lựa chọn dẫn về một ràng buộc · D (20đ) hội đồng đổi một ràng buộc giữa buổi, phản ứng có lập luận · E (10đ) ba điều kiện làm thiết kế này sai. Cả hai hướng giữ và đổi kết luận đều được điểm nếu lập luận dẫn từ ước lượng.

**Pitfalls.** Vẽ sơ đồ trước khi hỏi · liệt kê công cụ không nêu lý do · đổi kết luận khi bị vặn mà không dẫn số nào · bỏ phần E.

**Self-study (2,4 giờ).** Không có bài tự học. Nếu không đạt, theo phụ lục khắc phục khi không đạt cổng

**Done when.** Đạt ≥ 70/100, phần B và D đều ≥ 60%. Lựa chọn nào không dẫn được về một ràng buộc thì không tính điểm.

# MODULE 40 · CAPSTONE - BUILD AND DEFEND A DATA PLATFORM

**Lessons 417–422 · 12 giờ**

| | |
|---|---|
| **Objective cấp module** | Xây và vận hành một nền tảng dữ liệu đầu cuối trên yêu cầu nghiệp vụ thật, rồi bảo vệ nó trước hội đồng dưới sự cố gây trực tiếp |
| **Tiền đề** | M39 |
| **Exit criterion** | Nền tảng chạy đúng đầu cuối, qua được sự cố hội đồng gây ra trong buổi bảo vệ, và mọi quyết định thiết kế dẫn được về một ràng buộc hoặc một số đo |
| **Kỹ năng SFIA** | `ARCH` mức 5 · `DTAN` mức 4 · `CFMG` mức 4 |
| **Chế độ hỏng** | Dồn toàn bộ vào phần xây, bỏ phần vận hành và tài liệu, rồi không xử lý được sự cố trong buổi bảo vệ |

Sáu bài tương ứng sáu giai đoạn, mỗi giai đoạn có sản phẩm nộp riêng. Đề bài lấy từ một yêu cầu nghiệp vụ thật chứ dữ liệu mẫu có sẵn.

Trọng số chấm phản ánh trọng tâm của cả chương trình: khả năng phục hồi và vận hành chiếm 25%, ngang với phần xây. Một nền tảng chạy đúng nhưng không phục hồi được sau sự cố **không đạt**, dù kết quả đúng.

### Lesson 417 · Scoping the platform and writing the contract `DA`
**Prerequisites.** Module 40: M39

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Giai đoạn một: biến một yêu cầu nghiệp vụ mơ hồ thành phạm vi có biên rõ và một hợp đồng dữ liệu. Sản phẩm nộp gồm bốn thứ: danh sách câu hỏi nghiệp vụ mà nền tảng phải trả lời được, xếp theo ưu tiên; bảng ước lượng năm đại lượng theo lesson 411 kèm giả định; hợp đồng dữ liệu cho mỗi nguồn theo chuẩn M26 gồm lược đồ, ngữ nghĩa, chất lượng, độ tươi và quy trình đổi; và mục tiêu mức dịch vụ cho bốn chỉ báo theo lesson 387. Yêu cầu về phạm vi: nêu rõ cái gì **không** làm, vì phạm vi không có biên là nguyên nhân số một khiến dự án tốt nghiệp không xong. Rà soát phạm vi với giảng viên đóng vai bên nghiệp vụ, và phạm vi chỉ được chốt sau khi qua rà soát này.

**Outcome.** Nộp phạm vi có biên rõ, ước lượng có giả định, hợp đồng cho mọi nguồn, và mục tiêu mức dịch vụ đo được.

**Đánh giá.** Tầng *đánh giá*. Giai đoạn đòi phán đoán về phạm vi dưới ràng buộc thời gian có hạn. Kiểm bằng rà soát phạm vi; đạt khi bốn sản phẩm đầy đủ và phần ngoài phạm vi được nêu rõ.

**Lab.** Nhận yêu cầu nghiệp vụ. Phỏng vấn giảng viên đóng vai bên nghiệp vụ để làm rõ. Nộp bốn sản phẩm. Qua buổi rà soát phạm vi, trong đó phải bảo vệ được cả phần đã loại khỏi phạm vi.

**Pitfalls.** Nhận mọi yêu cầu vào phạm vi · ước lượng mà không nêu giả định · bỏ phần hợp đồng vì thấy chưa cần · đặt mục tiêu mức dịch vụ bằng số tròn.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Bốn sản phẩm đầy đủ, phần ngoài phạm vi nêu rõ kèm lý do, và qua được buổi rà soát phạm vi.

### Lesson 418 · Build - ingestion and storage `DA`
**Prerequisites.** Lesson 417

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Giai đoạn hai: đưa dữ liệu từ nguồn về và bố trí lưu trữ. Yêu cầu bắt buộc: ít nhất hai loại nguồn khác nhau trong đó một nguồn là CDC theo M31 hoặc một luồng theo M29; tầng đồng bất biến giữ nguyên bản gốc; bố trí lưu trữ có quyết định đầy đủ sáu điểm theo lesson 341; và kiểm chất lượng ở biên nhận theo M20 với vùng cách ly cho bản ghi lỗi. Ba thứ phải chứng minh được ở cuối giai đoạn: nạp lại toàn bộ cho cùng kết quả, bản ghi lỗi vào vùng cách ly chứ bị bỏ im lặng, và số byte quét của bộ truy vấn chuẩn nằm trong ngưỡng nhờ bố trí. Nộp kèm bảng quyết định bố trí và số đo hỗ trợ từng quyết định.

**Outcome.** Nạp được dữ liệu từ hai loại nguồn vào bố trí lưu trữ đã thiết kế, với tính bất biến và kiểm chất lượng được chứng minh.

**Đánh giá.** Tầng *sáng tạo*. Giai đoạn xây có ba tính chất kiểm được bằng thực nghiệm. Kiểm bằng ba phép thử; đạt khi cả ba qua và bảng quyết định bố trí có số đo hỗ trợ.

**Lab.** Xây tuyến nạp cho hai loại nguồn. Chạy lại toàn bộ và đối soát để chứng minh tính bất biến. Tiêm bản ghi lỗi và chứng minh chúng vào vùng cách ly có lý do. Chạy bộ truy vấn chuẩn và đo byte quét. Nộp bảng quyết định bố trí.

**Pitfalls.** Bỏ tầng đồng bất biến để tiết kiệm dung lượng · nạp một loại nguồn cho nhanh · bỏ kiểm chất lượng ở biên · chọn bố trí theo thói quen mà không đo.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Ba phép thử đều qua, và mọi quyết định bố trí trong bảng có ít nhất một số đo hỗ trợ.

### Lesson 419 · Build - transformation, orchestration and quality `DA`
**Prerequisites.** Lesson 418

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Giai đoạn ba: biến dữ liệu thô thành lớp phục vụ, có điều phối và có kiểm chất lượng. Yêu cầu bắt buộc: mô hình chiều cho lớp phục vụ theo M19 với phát biểu hạt rõ cho từng bảng; điều phối bằng một trong ba công cụ ở M22 tới M24 với lựa chọn dẫn về ma trận ở lesson 266; mọi tác vụ bất biến khi chạy lại và chạy bù được theo khoảng dữ liệu; và bộ kiểm chất lượng có ngưỡng, có cảnh báo, có vùng cách ly. Phép thử nghiệm thu của giai đoạn: chạy bù 30 ngày dữ liệu và đối soát khớp tuyệt đối với bản chạy tuần tự, đây là phép thử mà không có tính bất biến thì không qua được. Nộp kèm đồ thị phụ thuộc và một tài liệu quyết định kiến trúc theo lesson 415 cho lựa chọn bộ điều phối.

**Outcome.** Xây lớp biến đổi có điều phối và kiểm chất lượng, và chạy bù 30 ngày cho kết quả khớp tuyệt đối.

**Đánh giá.** Tầng *sáng tạo*. Giai đoạn đòi tổng hợp mô hình hoá, điều phối và chất lượng dưới ràng buộc chạy bù. Kiểm bằng phép chạy bù; đạt khi đối soát khớp tuyệt đối và tài liệu quyết định qua rà soát.

**Lab.** Xây lớp biến đổi và đồ thị điều phối. Chạy bù 30 ngày và đối soát với bản chạy tuần tự. Tiêm ba lỗi chất lượng và chứng minh cả ba bị bắt và cách ly. Nộp đồ thị phụ thuộc và tài liệu quyết định cho lựa chọn bộ điều phối.

**Pitfalls.** Dùng thời gian chạy thay cho khoảng dữ liệu · bỏ phát biểu hạt · chọn bộ điều phối theo quen tay mà không dẫn ma trận · kiểm chất lượng không có ngưỡng.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Chạy bù 30 ngày đối soát khớp tuyệt đối, ba lỗi chất lượng đều bị bắt, và tài liệu quyết định qua rà soát.

### Lesson 420 · Operate - observability, failure drill and cost `DA`
**Prerequisites.** Lesson 419

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Giai đoạn bốn, giai đoạn phân biệt bài đạt với bài giỏi: đưa nền tảng vào trạng thái vận hành được. Yêu cầu bắt buộc theo M38: số đo ba tầng và bảng điều khiển trả lời được năm câu hỏi chẩn đoán; cảnh báo đạt bốn tiêu chí ở lesson 390; sổ tay xử lý cho ít nhất ba sự cố hay gặp; bảng chế độ hỏng có đánh dấu điểm hỏng đơn lẻ; kế hoạch khôi phục có hai con số mục tiêu và đã diễn tập thật; và hoá đơn ước lượng chia theo thành phần kèm hai khoản cắt được. Tự chạy một buổi diễn tập sự cố trước khi bảo vệ và nộp bản phân tích sau sự cố của buổi đó, vì đội chưa từng diễn tập thì gần như chắc chắn không qua được sự cố ở buổi bảo vệ.

**Outcome.** Đưa nền tảng vào trạng thái vận hành được đủ sáu yêu cầu, và tự chạy được một buổi diễn tập sự cố có phân tích sau sự cố.

**Đánh giá.** Tầng *sáng tạo*. Giai đoạn đòi dựng một hệ vận hành hoàn chỉnh và tự kiểm chứng nó. Kiểm bằng rà soát sáu yêu cầu cộng biên bản diễn tập; đạt khi cả sáu đạt và diễn tập có khôi phục thật trong thời gian mục tiêu.

**Lab.** Dựng đủ sáu yêu cầu. Tự tổ chức một buổi diễn tập sự cố: một người gây sự cố, phần còn lại xử lý theo bảy bước. Nộp biên bản diễn tập, dòng thời gian, và bản phân tích sau sự cố có hành động khắc phục có chủ và hạn.

**Pitfalls.** Dựng bảng điều khiển đẹp mà không trả lời được câu hỏi chẩn đoán · viết sổ tay sau khi bảo vệ · kế hoạch khôi phục chưa diễn tập · bỏ phần chi phí.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Sáu yêu cầu đều đạt, buổi diễn tập có khôi phục thật trong thời gian mục tiêu, và phân tích sau sự cố có hành động có chủ và hạn.

### Lesson 421 · Documentation, runbook and handover `DA`
**Prerequisites.** Lesson 420

**In-class (120 phút).** 15 phút chốt phạm vi · 85 phút làm dự án, giảng viên đi vòng · 20 phút trình bày chéo

**Learn.** Giai đoạn năm: làm cho người khác tiếp quản được. Bộ tài liệu tối thiểu: tài liệu kiến trúc có sơ đồ luồng dữ liệu, tập tài liệu quyết định cho mọi lựa chọn lớn theo lesson 415, hợp đồng dữ liệu cho bên dùng cuối gồm định nghĩa chỉ số và hạn chế diễn giải theo M26, sổ tay vận hành, và hướng dẫn dựng lại từ đầu. Phép thử nghiệm thu là phép thử bàn giao thật, giống phép thử ở lesson 275 nhưng ở quy mô nền tảng: một học viên khác nhận bộ tài liệu, dựng lại môi trường thử từ mã, chạy pipeline, và xử lý một sự cố có sẵn trong sổ tay; mọi câu họ phải hỏi đều được ghi lại và là điểm trừ. Nguyên tắc viết: tài liệu phục vụ người chưa biết bối cảnh, nên mọi từ viết tắt và mọi quy ước phải được định nghĩa ở chỗ người đọc gặp chúng.

**Outcome.** Nộp bộ tài liệu đủ để một người khác dựng lại và vận hành được nền tảng mà không phải hỏi.

**Đánh giá.** Tầng *đánh giá*. Giai đoạn đo chất lượng tài liệu bằng kết quả của người khác chứ bằng độ dày. Kiểm bằng phép thử bàn giao; đạt khi người nhận dựng lại được và xử lý được sự cố với số câu hỏi dưới ngưỡng.

**Lab.** Viết đủ năm loại tài liệu. Đưa cho một học viên chưa từng xem dự án của bạn. Họ dựng lại môi trường thử, chạy pipeline, và xử lý một sự cố theo sổ tay. Ghi lại mọi câu họ phải hỏi. Sửa tài liệu theo danh sách đó rồi thử lại với người thứ hai.

**Pitfalls.** Viết tài liệu cho chính mình đọc · bỏ hướng dẫn dựng lại từ đầu · sổ tay không có ngưỡng và không có người chịu trách nhiệm · bỏ phần hạn chế diễn giải.

**Self-study (2,4 giờ).** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Done when.** Người nhận dựng lại và vận hành được với số câu hỏi dưới ngưỡng, và lần thử thứ hai có ít câu hỏi hơn lần đầu.

### Lesson 422 · Capstone defence `KT`
**Prerequisites.** Lesson 421

**In-class (120 phút).** 75 phút làm bài độc lập · 45 phút chữa bài và phân tích lỗi theo nhóm

**Learn.** Buổi bảo vệ trước hội đồng, 120 phút. Không có nội dung mới.

**Outcome.** Bảo vệ được toàn bộ nền tảng: thiết kế, số đo, vận hành, và xử lý được một sự cố hội đồng gây ra ngay trong buổi.

**Đánh giá.** Tầng *đánh giá*. Bài kiểm cuối cùng, đo năng lực tổng hợp dưới chất vấn và dưới sự cố thật, nên hình thức là bảo vệ trực tiếp có can thiệp.

**Lab.** Bài chấm bảy phần: A (15đ) bối cảnh, phạm vi và ước lượng, có giả định · B (20đ) kiến trúc và các quyết định lớn, mỗi quyết định dẫn về một ràng buộc hoặc một số đo · C (15đ) chạy đầu cuối trên dữ liệu hội đồng đưa, đối soát khớp · D (25đ) **hội đồng gây một sự cố ngay trong buổi**: phát hiện qua cảnh báo, chẩn đoán, khắc phục, thông báo · E (10đ) chi phí và hai khoản cắt được · F (10đ) bàn giao: hội đồng hỏi một câu từ sổ tay và một câu từ hợp đồng dữ liệu · G (5đ) ba điều kiện làm thiết kế này sai.

**Pitfalls.** Dồn thời gian vào phần xây và bỏ phần vận hành · trình bày công cụ thay vì quyết định · chưa từng diễn tập sự cố trước · không biết chi phí của chính hệ mình.

**Self-study (2,4 giờ).** Không có bài tự học. Nếu không đạt, theo phụ lục khắc phục khi không đạt cổng

**Done when.** Đạt ≥ 75/100, phần D ≥ 60%, và phần C phải đối soát khớp. Nền tảng chạy đúng nhưng không phục hồi được ở phần D thì không đạt, dù các phần khác cao.


---

# PHỤ LỤC — TRẠNG THÁI BẢN NHÁP

| Hạng mục | Trạng thái |
|---|---|
| Bản đồ 40 module | Xong |
| Đặc tả bài M1–M40 | Xong 422/422 |
| Đồ thị phụ thuộc trong module | Chưa |
| Bộ dữ liệu và môi trường lab | Chưa |
| Đề các cổng có rubric | Thang điểm đã có trong đặc tả bài; chưa soạn đề |
