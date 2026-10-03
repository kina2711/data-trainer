---
chuong_trinh: Data Analyst
module: 1 — Introduction to the Data Analyst Role
lesson: 1
tieu_de: "What a Data Analyst actually does all day"
dang_bai: LT
thoi_luong_phut: 120
trang_thai: xong
---

# Lesson 1 — What a Data Analyst actually does all day

## Đặc tả từ roadmap

- **Chương trình:** Data Analyst
- **Module 1:** Introduction to the Data Analyst Role
- **Dạng bài:** `LT` Lý thuyết

**Prerequisites.** Module 1: Không

**In-class (120 phút).** 25 phút dẫn nhập từ một tình huống hỏng · 55 phút xây khái niệm và cơ chế · 25 phút phản ví dụ và ranh giới · 15 phút tổng kết

**Learn.** Năm nhóm công việc của một Data Analyst và tỉ lệ thời gian ước lượng cho từng nhóm theo mục 3.1: làm sạch và kiểm chứng 40%, lấy dữ liệu 20%, phân tích 20%, trình bày 15%, làm rõ yêu cầu 5%. Ranh giới trách nhiệm giữa Data Analyst và năm vai trò liền kề: Business Analyst, BI Analyst, Data Scientist, Analytics Engineer, Data Engineer, gồm cả vùng chồng lấn thường gây tranh chấp phạm vi. Ba loại tổ chức tuyển Data Analyst và khác biệt về nội dung công việc: công ty sản phẩm, công ty dịch vụ, doanh nghiệp truyền thống.

**Outcome.** Phân định trách nhiệm của sáu vai trò trong đội dữ liệu cho một danh sách nhiệm vụ cho trước, và định vị khoảng cách giữa năng lực hiện có của bản thân và ma trận ở mục 4.

**Đánh giá.** Tầng *hiểu*. Bài mở đầu chương trình, người học chưa có dữ liệu để thao tác, nên objective dừng ở mức phân định và giải thích. Kiểm bằng bài tập gán 15 nhiệm vụ cho sáu vai trò kèm một câu lý do mỗi nhiệm vụ; chấm theo đáp án cố định, đạt khi đúng ≥ 12/15 và lý do không mâu thuẫn với bảng ranh giới ở phụ lục H.

**Lab.** Đọc 10 tin tuyển dụng Data Analyst đang mở tại Việt Nam trên ITViec hoặc TopDev. Lập bảng tần suất: mỗi kỹ năng xuất hiện trong bao nhiêu tin. Đối chiếu bảng tần suất với bản đồ module ở mục 9 và chỉ ra kỹ năng nào chương trình không phủ.

**Pitfalls.** Quy vai trò Data Analyst về việc lập báo cáo · giả định thành thạo công cụ là điều kiện đủ · bỏ qua phần nghiệp vụ vì không đo được trực tiếp.

**Self-study (2 giờ).** 20 phút viết ghi chú chín phần · 40 phút đọc nguồn tham chiếu và tự giải thích lại · 25 phút trả lời bốn câu kiểm tra · 15 phút nhật ký lỗi

**Done when.** Nộp bảng tần suất kỹ năng từ 10 tin tuyển dụng có ghi nguồn và ngày truy cập, và bài gán nhiệm vụ đạt ≥ 12/15.

---

## I. Mục tiêu và chuẩn đầu ra

Hết buổi này, bạn phải **làm được** những việc sau. Mỗi việc có cách đo — nếu không đo được thì không tính là đạt.

| # | Làm được gì | Đo bằng cách nào | Mức |
|---|---|---|---|
| 1 | Kể tên sáu vai trò trong một nhóm dữ liệu và trách nhiệm chính của từng vai | Viết ra giấy trong 5 phút, không nhìn tài liệu, đúng cả sáu | Bắt buộc |
| 2 | Nhìn một yêu cầu công việc bất kỳ và nói nó thuộc về vai nào | Cho 8 yêu cầu, phân đúng ≥ 6 | Bắt buộc |
| 3 | Ước lượng một ngày làm việc của DA phân bổ vào năm nhóm việc nào | Vẽ lại được biểu đồ 20/40/20/15/5 và giải thích vì sao làm sạch chiếm nhiều nhất | Bắt buộc |
| 4 | Đọc một tin tuyển dụng và tách được: yêu cầu công cụ, yêu cầu nghiệp vụ, yêu cầu giao tiếp | Làm trên 10 tin ở phần Lab | Bắt buộc |
| 5 | Chỉ ra mình đang thiếu kỹ năng nào so với thị trường | Nộp bảng tự đánh giá thang 1–5 cho 11 module | Bắt buộc |
| 6 | Giải thích vì sao hai vai khác nhau lại hay tranh nhau cùng một việc | Nêu được ít nhất hai vùng chồng lấn có thật | Nên có |

**Câu phải trả lời được mà không nhìn tài liệu khi kết thúc buổi:** *Data Analyst khác Data Engineer ở chỗ nào, và vì sao ranh giới đó hay bị tranh chấp?*

---

## II. Bối cảnh và vấn đề đặt ra

### Một tình huống hỏng có thật về mặt cấu trúc

Sáng thứ Hai, giám đốc kinh doanh nhắn: *"Doanh thu tháng 10 giảm 12%, tìm hiểu giúp anh vì sao."*

Một người mới vào nghề sẽ mở ngay công cụ, viết truy vấn, vẽ biểu đồ, và đến chiều gửi lại một bản báo cáo đẹp: doanh thu theo ngày, theo vùng, theo sản phẩm. Giám đốc nhìn xong hỏi lại: *"Rồi sao?"*

Bản báo cáo đó **không sai một con số nào**, và vẫn vô dụng. Lý do:

1. **Chưa hỏi 12% so với cái gì.** So với tháng 9? So với tháng 10 năm ngoái? So với kế hoạch? Ba mốc cho ba câu chuyện khác nhau, thậm chí trái ngược.
2. **Chưa kiểm tra con số 12% có thật không.** Tháng 10 có 31 ngày, tháng 9 có 30. Nếu hệ thống đếm theo tổng tháng mà không chuẩn hoá theo số ngày, một phần "giảm" là ảo. Ngược lại, nếu một chi nhánh mới ngừng đẩy dữ liệu từ ngày 20 thì con số giảm là **lỗi dữ liệu**, không phải lỗi kinh doanh.
3. **Chưa xác định ai sẽ làm gì với câu trả lời.** Nếu câu trả lời là "giảm do nhóm khách hàng cũ bỏ đi", người nhận sẽ gọi cho ai vào sáng mai? Nếu không trả lời được câu này, phân tích không dẫn tới hành động nào.

Khoảng cách giữa "chạy được truy vấn" và "trả lời được câu hỏi" chính là nội dung của cả chương trình 85 bài này. Buổi 1 không dạy bạn công cụ nào. Nó dạy bạn **biết mình đang làm nghề gì**, vì phần lớn người bỏ cuộc giữa chừng là do hiểu sai nghề ngay từ đầu.

### Vì sao buổi này quan trọng hơn vẻ ngoài của nó

Người mới thường muốn bỏ qua buổi lý thuyết để "vào học SQL luôn". Hậu quả thấy được sau vài tháng:

- Học rất nhiều công cụ nhưng khi phỏng vấn không trả lời được *"em đã giải quyết bài toán kinh doanh nào?"*
- Nhận việc rồi mới biết mình thích làm hệ thống chứ không thích làm phân tích, mất một năm đi sai hướng.
- Tranh việc với đồng nghiệp vì không ai biết ranh giới trách nhiệm nằm ở đâu.

---

## III. Cơ sở lý thuyết và cơ chế vận hành

### 3.1. Một ngày của Data Analyst phân bổ vào đâu

Năm nhóm công việc, kèm tỉ lệ thời gian điển hình:

| Nhóm việc | Tỉ lệ | Việc cụ thể |
|---|---|---|
| Lấy dữ liệu | 20% | Tìm bảng nào chứa cái mình cần, xin quyền truy cập, viết truy vấn, hỏi lại người nắm hệ thống |
| **Làm sạch và kiểm chứng** | **40%** | Xử lý thiếu, trùng, sai kiểu, sai đơn vị; đối chiếu tổng với nguồn khác; tìm ra vì sao hai báo cáo lệch nhau |
| Phân tích | 20% | Cắt lát theo chiều, so sánh, tìm quan hệ, kiểm định giả thuyết |
| Trình bày | 15% | Chọn biểu đồ, viết diễn giải, dựng dashboard, thuyết trình |
| Họp và trao đổi | 5% | Làm rõ yêu cầu, báo tiến độ, bảo vệ kết luận |

**Con số cần nhớ: 40%.** Phần lớn thời gian của nghề này là làm sạch và kiểm chứng dữ liệu, không phải phân tích. Đây là điều gây vỡ mộng nhiều nhất và cũng là lý do chương trình dành cả Module 4 cho mô hình hoá và chuẩn bị dữ liệu.

**Vì sao làm sạch lại tốn nhiều đến thế?** Dữ liệu trong doanh nghiệp không được sinh ra để phân tích. Nó được sinh ra để **hệ thống vận hành chạy được**: ghi đơn hàng, ghi giao dịch, ghi thao tác người dùng. Một hệ thống bán hàng chỉ cần biết đơn này đã thanh toán chưa; nó không quan tâm tên tỉnh được gõ là "Hà Nội", "Ha Noi" hay "HN". Đến khi bạn muốn đếm doanh thu theo tỉnh thì ba cách gõ đó thành ba tỉnh khác nhau. Mọi công việc làm sạch đều sinh ra từ khoảng cách giữa **mục đích ghi** và **mục đích đọc**.

### 3.2. Sáu vai trò trong một nhóm dữ liệu

Cách nhớ gọn: đi theo dòng đời của dữ liệu, từ lúc sinh ra đến lúc thành quyết định.

| Vai | Câu hỏi họ trả lời | Sản phẩm bàn giao | Công cụ chính |
|---|---|---|---|
| **Data Engineer** (DE) | Làm sao đưa dữ liệu từ nơi nó sinh ra về nơi dùng được, đúng giờ, không mất? | Đường ống dữ liệu, kho dữ liệu, hạ tầng | Python, SQL, Spark, Kafka, cloud |
| **Analytics Engineer** (AE) | Làm sao biến dữ liệu thô thành bảng sạch, có định nghĩa thống nhất, ai dùng cũng ra cùng một số? | Lớp mô hình dữ liệu, từ điển chỉ số | SQL, dbt, mô hình hoá |
| **Data Analyst** (DA) | Chuyện gì đã xảy ra, vì sao, và ta nên làm gì? | Phân tích, báo cáo, dashboard, khuyến nghị | SQL, Excel, BI, thống kê, Python |
| **BI Analyst** | Các chỉ số vận hành đang ở mức nào, theo dõi thế nào? | Hệ thống dashboard định kỳ | BI, SQL |
| **Business Analyst** (BA) | Nghiệp vụ cần gì, quy trình nên thay đổi ra sao? | Tài liệu yêu cầu, quy trình | Tài liệu, phỏng vấn, đôi khi SQL |
| **Data Scientist** (DS) | Dự báo điều gì sắp xảy ra, tối ưu ra sao? | Mô hình dự báo, thí nghiệm | Python, thống kê, học máy |

Một cách nói ngắn để nhớ:

> **DE xây đường. AE lát mặt đường và cắm biển. DA lái xe đi tìm câu trả lời. DS dự đoán đường phía trước. BA quyết định ta cần đi đâu. BI Analyst gắn đồng hồ đo lên xe.**

### 3.3. Ranh giới hay bị tranh chấp

Ba vùng chồng lấn gây xung đột thật trong công việc:

**Vùng 1 — DA và AE: "ai chịu trách nhiệm định nghĩa chỉ số?"**

Doanh thu có trừ hàng trả lại không? Có gồm phí vận chuyển không? Nếu mỗi DA tự quyết trong truy vấn của mình, mười báo cáo ra mười con số. AE sinh ra để chấm dứt chuyện đó: định nghĩa một lần, ở một chỗ, ai dùng cũng ra cùng một số. Xung đột xảy ra khi DA cần gấp và tự viết định nghĩa riêng, còn AE muốn mọi thứ đi qua lớp mô hình chung. **Đây là lý do Analytics Engineer tồn tại như một nghề riêng.**

**Vùng 2 — DA và DE: "ai xử lý dữ liệu bẩn?"**

DE nói: tôi đưa dữ liệu về nguyên trạng như nguồn, làm sạch là việc của phân tích. DA nói: nguồn sai kiểu dữ liệu và thiếu khoá, sửa ở đường ống mới đúng chỗ. Cả hai đều có lý. Nguyên tắc thực tế: **lỗi hệ thống sinh ra thì sửa ở đường ống, lỗi thuộc về cách hiểu nghiệp vụ thì xử lý ở lớp phân tích.**

**Vùng 3 — DA và BA: "ai gặp người dùng?"**

Ở công ty nhỏ không có BA, DA phải tự đi làm rõ yêu cầu. Ở công ty lớn, BA đứng giữa và DA chỉ nhận yêu cầu đã viết ra. DA nào chỉ biết chờ yêu cầu viết sẵn thì trần sự nghiệp rất thấp, vì phần giá trị cao nhất của nghề nằm ở chỗ **biết hỏi lại cho đúng**.

### 3.4. Ba loại công ty, ba nghề khác nhau cùng tên "Data Analyst"

| | Công ty sản phẩm | Công ty dịch vụ / tư vấn | Doanh nghiệp truyền thống |
|---|---|---|---|
| Ví dụ | Shopee, MoMo, VNG, Grab | BCG Gamma, agency, outsourcing | Ngân hàng, bán lẻ, sản xuất |
| Câu hỏi hay gặp | Tính năng mới có làm tăng giữ chân người dùng không? | Khách hàng này nên tối ưu khâu nào? | Chi nhánh nào đang lỗ và vì sao? |
| Nặng về | Phân tích sản phẩm, thí nghiệm A/B | Nhiều ngành, nhịp nhanh, làm slide | SQL, báo cáo định kỳ, quy trình |
| Dữ liệu | Rất lớn, hành vi người dùng | Mỗi dự án một nguồn khác nhau | Sạch hơn, hệ thống cũ, quy định chặt |
| Điểm mạnh cho người học | Học được văn hoá thí nghiệm | Tiếp xúc nhiều ngành rất nhanh | Nền SQL và nghiệp vụ vững |
| Điểm yếu | Dễ chỉ biết một sản phẩm | Ít đi sâu, áp lực thời gian | Công nghệ chậm đổi mới |

**Hệ quả cho bạn:** đừng hỏi "học DA ra làm gì". Hãy hỏi *"tôi muốn làm DA ở nhóm công ty nào"*, vì câu trả lời quyết định bạn nên dồn sức vào Module nào trước. Muốn vào công ty sản phẩm thì Module 7 (phân tích sản phẩm) và Module 8 (A/B) là then chốt. Muốn vào ngân hàng thì Module 3 (SQL) và Module 6 (Power BI) quan trọng hơn.

### 3.5. Thị trường Việt Nam — mốc tham khảo

Phần 3 của [roadmap Data Analyst](../../../../roadmap/roadmap.md) có bảng thị trường đầy đủ. Ba điều cần biết ngay ở buổi 1:

- Nhu cầu tuyển Data / AI / ML tại Việt Nam tăng mạnh theo năm; DA là **cửa vào phổ biến nhất** của ngành.
- Python đã chuyển từ "điểm cộng" sang "yêu cầu" ở nhiều tin tuyển dụng.
- Xu hướng phân tích tự phục vụ đẩy DA từ *người làm báo cáo* sang *người tạo điều kiện để người khác tự trả lời được*.

> Số liệu thị trường trong roadmap trích từ nguồn thứ cấp và **chưa được kiểm chứng độc lập**. Dùng làm mốc định hướng, không dùng làm căn cứ đàm phán tuyệt đối. Phần Lab bên dưới buộc bạn tự kiểm chứng bằng dữ liệu bạn thu thập.

---

## IV. Khung quyết định và tiêu chí lựa chọn

### 4.1. Nhận yêu cầu bất kỳ — đây có phải việc của DA không?

```
Yêu cầu đến
  │
  ├─ "Dữ liệu này chưa về kho / đường ống hỏng / chậm"      → Data Engineer
  ├─ "Hai báo cáo ra hai số khác nhau, cần thống nhất
  │   định nghĩa cho toàn công ty"                          → Analytics Engineer
  ├─ "Cần theo dõi chỉ số này hằng ngày, lâu dài"           → BI Analyst (DA dựng lần đầu)
  ├─ "Dự đoán khách hàng nào sắp rời bỏ"                    → Data Scientist
  ├─ "Quy trình duyệt đơn nên đổi thế nào"                  → Business Analyst
  └─ "Chuyện gì đã xảy ra, vì sao, ta nên làm gì"           → Data Analyst  ← của bạn
```

Ở công ty dưới 50 người, thường không có năm vai kia. DA làm hết. Điều đó không sai — nhưng phải **biết mình đang làm việc của vai nào**, để còn biết mình đang giỏi lên theo hướng nào.

### 4.2. Tự chọn hướng đi

| Nếu bạn... | Hướng hợp | Vì sao |
|---|---|---|
| Thích trả lời câu hỏi, thích trình bày, thích tiếp xúc nghiệp vụ | **Data Analyst** | Giá trị nằm ở diễn giải và thuyết phục |
| Thích xây thứ người khác dùng lại, ghét làm cùng một báo cáo hai lần | **Analytics Engineer** | Giá trị nằm ở tính tái sử dụng |
| Thích hệ thống, chịu được việc bị gọi lúc 3 giờ sáng khi đường ống hỏng | **Data Engineer** | Giá trị nằm ở độ tin cậy vận hành |
| Ngại viết code | Cân nhắc kỹ trước khi vào ngành | Cả ba hướng đều cần code; DA cần ít nhất SQL và Python cơ bản |

---

## V. Nghiên cứu tình huống: quay lại câu "doanh thu giảm 12%"

Cùng một yêu cầu, làm theo cách của người đã biết nghề.

**Bước 1 — Làm rõ trước khi chạm vào dữ liệu (10 phút, hỏi 4 câu).**

1. 12% là so với mốc nào? → *So với tháng 9.*
2. Anh sẽ dùng câu trả lời để làm gì? → *Quyết định có tăng ngân sách khuyến mãi tháng 11 không.*
3. Nếu kết luận là "do mùa vụ, không cần làm gì", anh có chấp nhận không? → *Có.*
4. Cần trả lời trước khi nào? → *Chiều mai.*

Bốn câu này đổi hoàn toàn phạm vi công việc: không cần dashboard, chỉ cần **một kết luận có căn cứ về việc có nên chi thêm tiền hay không**.

**Bước 2 — Kiểm chứng con số trước khi giải thích nó (30 phút).**

| Việc kiểm | Phát hiện |
|---|---|
| Số ngày trong tháng | Tháng 10 có 31 ngày, tháng 9 có 30 → tính theo doanh thu trung bình ngày, mức giảm còn khoảng 15% chứ không phải 12% |
| Dữ liệu có đủ không | Chi nhánh Đà Nẵng ngừng đồng bộ từ 20/10 → **thiếu 11 ngày dữ liệu của một chi nhánh** |
| Định nghĩa doanh thu | Báo cáo này trừ hàng trả lại, báo cáo kế toán thì không |

Đây là lúc 40% thời gian làm sạch phát huy tác dụng. Nếu bỏ qua bước này, mọi phân tích phía sau đều xây trên nền sai.

**Bước 3 — Tách phần ảo khỏi phần thật.**

Sau khi bù dữ liệu Đà Nẵng và chuẩn hoá theo số ngày: mức giảm thật là khoảng 4%, không phải 12%. Trong đó phần lớn rơi vào nhóm khách hàng mua lần đầu.

**Bước 4 — Trả lời đúng câu đã được hỏi.**

> Doanh thu tháng 10 giảm **4%** so với tháng 9 sau khi chuẩn hoá theo số ngày và bù phần dữ liệu thiếu của chi nhánh Đà Nẵng — không phải 12% như báo cáo gốc. Phần giảm tập trung ở nhóm khách mua lần đầu, trong khi nhóm khách cũ giữ nguyên. **Khuyến nghị:** nếu chi thêm ngân sách, chi vào kênh thu hút khách mới, không chi vào khuyến mãi đại trà. **Việc cần làm riêng:** chi nhánh Đà Nẵng đang mất dữ liệu 11 ngày, cần báo bộ phận hệ thống — lỗi này còn ảnh hưởng mọi báo cáo khác.

**Điều đáng chú ý:** giá trị lớn nhất mà người phân tích tạo ra ở đây không phải biểu đồ nào cả. Đó là việc **phát hiện con số ban đầu sai** và **tìm ra một lỗi hệ thống mà chưa ai biết**. Không có bước 2 thì công ty đã chi tiền để chữa một vấn đề không tồn tại.

---

## VI. Giới hạn và ngộ nhận phổ biến

**Ngộ nhận 1 — "Data Analyst là người làm báo cáo."**

- *Thực tế:* làm báo cáo chỉ là một phần của 15% thời gian trình bày. Phần lớn giá trị nằm ở chỗ chọn đúng câu hỏi và kiểm chứng số liệu.
- *Vì sao nghe hợp lý:* vì đó là phần duy nhất người ngoài nhìn thấy. Toàn bộ 40% làm sạch diễn ra âm thầm.
- *Hậu quả nếu tin theo:* bạn sẽ học công cụ vẽ biểu đồ và bỏ qua SQL, thống kê, nghiệp vụ — rồi dừng ở mức làm theo yêu cầu suốt sự nghiệp.

**Ngộ nhận 2 — "Học xong công cụ là làm được việc."**

- *Thực tế:* công cụ là điều kiện cần. Cùng một truy vấn SQL, người hiểu nghiệp vụ viết ra kết quả dùng được, người không hiểu viết ra con số vô nghĩa.
- *Vì sao nghe hợp lý:* vì công cụ đo được và có chứng chỉ, còn nghiệp vụ thì mơ hồ, khó đo.
- *Cách chương trình xử lý:* mỗi bài thực hành đều gắn với một câu hỏi kinh doanh cụ thể, không có bài nào chỉ luyện cú pháp.

**Ngộ nhận 3 — "Phần nghiệp vụ để sau cũng được."**

- *Thực tế:* nghiệp vụ là thứ lâu ngấm nhất, cần tích luỹ từ đầu. Công cụ mới học hai tuần là dùng được.
- *Vì sao nghe hợp lý:* vì tiến bộ về công cụ thấy ngay, còn tiến bộ về nghiệp vụ không có gì để khoe.

**Ngộ nhận 4 — "Số liệu tự nói lên sự thật."**

- *Thực tế:* số liệu luôn đi kèm cách đo và định nghĩa. Đổi định nghĩa "doanh thu" là đổi kết luận.
- *Vì sao nghe hợp lý:* vì con số trông khách quan.
- *Liên hệ:* toàn bộ Module 5 (thống kê) tồn tại để bạn biết khi nào một khác biệt là thật và khi nào chỉ là nhiễu.

### Giới hạn của chính buổi học này

Tỉ lệ 20/40/20/15/5 là **con số điển hình để định hướng**, không phải chuẩn đo. Thực tế dao động mạnh: tuần chạy báo cáo cuối tháng có thể 80% là trình bày; tuần tiếp nhận nguồn dữ liệu mới có thể 90% là làm sạch. Đừng dùng con số này để đánh giá ai.

---

## VII. Ghi chú phương pháp giảng dạy

**Phân bổ 120 phút**

| Thời gian | Nội dung | Cách làm |
|---|---|---|
| 0–25 | Tình huống "doanh thu giảm 12%" | Đưa nguyên yêu cầu, cho học viên tự nói sẽ làm gì. **Chưa** chữa. Ghi lại câu trả lời lên bảng để cuối buổi đối chiếu |
| 25–80 | Năm nhóm việc, sáu vai trò, ba vùng chồng lấn | Vẽ dòng đời dữ liệu lên bảng, thêm dần từng vai vào |
| 80–105 | Phản ví dụ và ranh giới | Đọc to 8 yêu cầu, học viên giơ tay phân vai. Chốt bằng cây quyết định ở mục 4.1 |
| 105–120 | Tổng kết | Quay lại bảng ghi lúc đầu buổi, cùng chỉ ra chỗ nào thiếu bước làm rõ và bước kiểm chứng |

**Lỗi học viên hay mắc ở buổi này**

- Nhầm Analytics Engineer với Data Engineer. Chốt bằng một câu: *AE viết SQL, DE viết hệ thống chạy SQL đó.*
- Cho rằng phải học hết cả ba hướng. Nói rõ: ba chương trình trong dự án này **độc lập**, chọn một và đi hết.
- Hỏi "lương bao nhiêu" ngay đầu buổi. Trả lời bằng mốc trong roadmap kèm nguyên văn cảnh báo về nguồn chưa kiểm chứng — đừng hứa con số.

**Nếu lớp đã có người đi làm:** đổi tình huống mở đầu thành một yêu cầu thật họ từng nhận, và cho họ kể lại kết cục. Hiệu quả hơn ví dụ dựng sẵn nhiều.

---

## VIII. Câu hỏi tự kiểm tra

**Câu 1.** Trong năm nhóm công việc, nhóm nào chiếm nhiều thời gian nhất, và vì sao?

<details><summary>Đáp án</summary>

Làm sạch và kiểm chứng, khoảng 40%. Nguyên nhân gốc: dữ liệu doanh nghiệp được sinh ra để **hệ thống vận hành chạy được**, không phải để phân tích. Hệ thống bán hàng không quan tâm tên tỉnh gõ là "Hà Nội" hay "HN", nhưng người đếm doanh thu theo tỉnh thì có. Mọi việc làm sạch đều sinh ra từ khoảng cách giữa mục đích ghi và mục đích đọc.
</details>

**Câu 2.** Một bạn nói: *"Công ty mình có DE rồi nên DA không cần làm sạch dữ liệu nữa."* Bạn phản biện thế nào?

<details><summary>Đáp án</summary>

Sai ở chỗ gộp hai loại lỗi làm một. Lỗi do hệ thống sinh ra — sai kiểu dữ liệu, thiếu khoá, đường ống mất dữ liệu — thì sửa ở đường ống, đúng là việc của DE. Nhưng lỗi thuộc về **cách hiểu nghiệp vụ** thì DE không sửa được: doanh thu có trừ hàng trả lại không, khách hàng "hoạt động" nghĩa là gì, đơn bị huỷ có tính không. Những thứ này phụ thuộc câu hỏi đang trả lời, nên phải xử lý ở lớp phân tích — hoặc chuẩn hoá một lần ở lớp AE nếu công ty có vai đó.
</details>

**Câu 3.** Phân vai cho bốn yêu cầu sau: (a) "Dashboard doanh thu load chậm 5 phút"; (b) "Hai phòng ban báo hai con số khách hàng khác nhau"; (c) "Vì sao tỉ lệ huỷ đơn tháng này tăng"; (d) "Dự đoán khách nào sắp ngừng dùng dịch vụ".

<details><summary>Đáp án</summary>

(a) **DE** — vấn đề hiệu năng hạ tầng và đường ống. (b) **AE** — hai định nghĩa chỉ số khác nhau, cần thống nhất một nguồn sự thật. (c) **DA** — giải thích chuyện đã xảy ra và vì sao. (d) **DS** — dự báo tương lai.

Lưu ý: ở công ty nhỏ có thể một người làm cả bốn. Câu hỏi kiểm tra bạn có phân biệt được **loại việc**, không phải phân biệt chức danh trên hợp đồng.
</details>

**Câu 4.** Giám đốc hỏi *"doanh thu giảm 12%, vì sao?"*. Kể ba việc bạn làm **trước khi** viết dòng truy vấn đầu tiên.

<details><summary>Đáp án</summary>

1. Hỏi 12% là so với mốc nào — tháng trước, cùng kỳ năm ngoái, hay kế hoạch. Ba mốc cho ba câu chuyện khác nhau.
2. Hỏi câu trả lời sẽ được dùng để quyết định việc gì, và hạn khi nào. Điều này quyết định phạm vi: một kết luận hay cả một dashboard.
3. Kiểm chứng bản thân con số 12%: số ngày trong tháng có bằng nhau không, dữ liệu có thiếu nguồn nào không, định nghĩa doanh thu ở hai kỳ có giống nhau không.

Bỏ qua bước 3 là lỗi tốn kém nhất: công ty có thể chi tiền để chữa một vấn đề không tồn tại.
</details>

---

## IX. Bài tập về nhà

Nội dung đầy đủ nằm trong `homework.md`. Tóm tắt:

**Phần A — Thu thập (60 phút).** Tìm **10 tin tuyển dụng Data Analyst thật tại Việt Nam** trên ITViec, TopDev, LinkedIn hoặc VietnamWorks. Ưu tiên tin đăng trong 3 tháng gần nhất. Lưu lại liên kết và ngày đăng của từng tin.

**Phần B — Lập bảng đếm.** Với mỗi tin, đánh dấu những kỹ năng được nêu, rồi cộng lại:

| Kỹ năng | Module phủ | Số tin / 10 |
|---|---|---|
| Excel nâng cao | M2 | |
| SQL | M3 | |
| Mô hình hoá và chuẩn bị dữ liệu | M4 | |
| Thống kê | M5 | |
| Power BI hoặc công cụ BI khác | M6 | |
| Hiểu nghiệp vụ và chỉ số sản phẩm | M7 | |
| A/B testing | M8 | |
| Python | M9 | |
| Trình bày, giao tiếp, tiếng Anh | M10 | |

**Phần C — Đối chiếu và kết luận (viết 200–300 từ).**

1. Kỹ năng nào xuất hiện nhiều nhất? Có khớp với thứ tự các module trong chương trình không?
2. Có kỹ năng nào thị trường đòi mà 11 module **không** phủ? Ghi ra.
3. Có module nào chương trình dạy mà **không** tin nào nhắc tới? Theo bạn vì sao chương trình vẫn giữ nó?

**Phần D — Tự đánh giá.** Chấm bản thân thang 1–5 cho từng module trong bảng trên. Lưu file này lại — cuối chương trình sẽ chấm lại để so.

**Đạt khi:** đủ 10 tin có liên kết thật, bảng đếm điền đủ, và phần C trả lời được cả ba câu — đặc biệt là câu 2 và 3, vì đó mới là phần cần suy nghĩ.
