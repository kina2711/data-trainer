# Bản giảng dạy: Data Analyst thực sự làm gì?

## Cửa hàng bán ít hàng hơn

Một cửa hàng bán ít hàng hơn bình thường.

Người quản lý hỏi:

> Doanh thu giảm. Tôi nên làm gì?

Câu hỏi này còn thiếu thông tin:

- Doanh thu nào đang được nói tới?
- So với mốc nào?
- Giảm ở tất cả khách hàng hay chỉ một nhóm?
- Dữ liệu có bị thiếu không?
- Người quản lý có thể thay đổi giá, chương trình khuyến mãi hay cách giữ khách không?

Data Analyst làm rõ quyết định cần đưa ra trước khi mở công cụ vẽ biểu đồ.

> Data Analyst giúp một người đưa ra quyết định tốt hơn bằng dữ liệu có thể kiểm tra.

## Một công việc hoàn chỉnh trông như thế nào?

Một công việc phân tích hoàn chỉnh có một đường đi rõ ràng:

```text
Quyết định
  -> Câu hỏi
  -> Chỉ số
  -> Dữ liệu
  -> Phép kiểm
  -> Kết luận
  -> Hành động
```

Ta gọi đường đi này là một `decision trace`, tức là dấu vết từ quyết định đến bằng chứng.

Mỗi bước trả lời một câu hỏi:

1. Quyết định: Người dùng kết quả phải chọn điều gì?
2. Câu hỏi: Cần biết điều gì để chọn?
3. Chỉ số: Con số nào giúp phân biệt các lựa chọn?
4. Dữ liệu: Những bản ghi nào tạo ra con số đó?
5. Phép kiểm: Làm sao biết dữ liệu và phép tính không sai?
6. Kết luận: Bằng chứng cho phép nói điều gì?
7. Hành động: Ai sẽ làm gì sau khi đọc kết luận?

Nếu thiếu bước cuối, ta có một báo cáo nhưng chưa chắc có giá trị. Nếu thiếu bước kiểm, ta có một con số nhưng chưa chắc có bằng chứng.

### Dừng và hỏi

Nếu người quản lý nói chỉ cần làm dashboard, em sẽ hỏi câu nào trước?

Câu trả lời tốt:

> Anh hoặc chị sẽ dùng dashboard này để quyết định việc gì?

Câu hỏi đó không làm chậm công việc. Nó giúp tránh xây đúng dashboard nhưng sai mục đích.

## Sáu việc chính của một Data Analyst

Ta có thể chia công việc thành sáu phần: Ask, Prepare, Process, Analyze, Share và Act.

### Ask: hỏi cho rõ

Ask nghĩa là biến yêu cầu mơ hồ thành câu hỏi có ranh giới.

Yêu cầu ban đầu:

> Doanh thu đang giảm.

Câu hỏi rõ hơn:

> Doanh thu thuần của khách hàng mới trong kỳ hiện tại thay đổi thế nào so với kỳ đối chiếu, và phần thay đổi tập trung ở kênh nào?

Ta đã làm rõ:

- chỉ số là doanh thu thuần;
- nhóm cần xem là khách hàng mới;
- có kỳ hiện tại và kỳ đối chiếu;
- cần chia theo kênh;
- mục đích là tìm nơi cần hành động.

### Prepare: tìm đúng dữ liệu

Prepare nghĩa là xác định dữ liệu cần dùng và dữ liệu đó nằm ở đâu.

Ta có thể cần:

- bảng đơn hàng;
- bảng hoàn tiền;
- bảng khách hàng;
- bảng kênh tiếp thị;
- quy tắc xác định khách mới.

Ở bước này, Data Analyst phải hỏi về hạt dữ liệu. Hạt cho biết một dòng đại diện cho điều gì.

Ví dụ:

- một dòng là một đơn hàng;
- một dòng là một sản phẩm trong đơn hàng;
- một dòng là một lần thanh toán.

Nếu tưởng một dòng là một đơn hàng nhưng thực tế là một sản phẩm, phép cộng doanh thu có thể đếm một đơn nhiều lần.

### Process: làm dữ liệu dùng được

Process nghĩa là kiểm tra và xử lý lỗi trước khi phân tích.

Ta kiểm:

- khóa có bị trùng không;
- giá trị quan trọng có bị thiếu không;
- kiểu dữ liệu có đúng không;
- đơn bị hủy có được loại đúng không;
- tiền hoàn có bị bỏ quên không;
- phép nối bảng có làm nhân số dòng không.

Process bảo vệ nghĩa của con số bằng cách phát hiện và xử lý các lỗi này.

### Analyze: tìm mẫu và kiểm giả thuyết

Analyze nghĩa là dùng dữ liệu để phân biệt các cách giải thích.

Ngoài mức giảm doanh thu, ta còn hỏi:

- số khách giảm hay số tiền mỗi khách giảm;
- khách mới và khách cũ khác nhau thế nào;
- kênh nào tạo phần giảm lớn nhất;
- thay đổi đến từ số đơn, giá trị đơn hay hoàn tiền;
- kết quả có còn đúng khi đổi cách chia nhóm không.

### Share: nói đúng mức bằng chứng

Ở bước Share, Data Analyst trình bày một chuỗi lập luận mà người khác có thể kiểm tra.

Một cách nói yếu:

> Kênh quảng cáo là nguyên nhân làm doanh thu giảm.

Một cách nói tốt hơn:

> Phần giảm tập trung ở khách mới đến từ kênh quảng cáo. Dữ liệu hiện tại cho thấy mối liên hệ, chưa đủ để khẳng định nguyên nhân. Nên kiểm tra thay đổi chiến dịch và chất lượng tracking trước khi điều chỉnh ngân sách.

### Act: biến kết quả thành việc có người chịu trách nhiệm

Act nghĩa là thống nhất hành động, người chịu trách nhiệm và tín hiệu dùng để xem lại quyết định.

Ví dụ:

- nhóm marketing kiểm tra thay đổi chiến dịch;
- nhóm dữ liệu kiểm tra tracking;
- người quản lý chưa cắt ngân sách cho đến khi hai phép kiểm hoàn tất;
- nếu dữ liệu mới bác bỏ giả thuyết, quyết định phải được xem lại.

Sáu phần tạo thành một vòng lặp. Nếu Process phát hiện dữ liệu thiếu, ta quay lại Prepare. Nếu Analyze cho thấy câu hỏi ban đầu quá rộng, ta quay lại Ask.

## Bốn lớp để biết một kết luận có đáng tin không

Trước khi nói kết quả đúng, hãy kiểm bốn lớp.

### Lớp 1: câu hỏi có đúng không?

Ví dụ, người quản lý cần quyết định cách giữ khách cũ nhưng ta lại phân tích khách mới. Phép tính có thể đúng mà câu trả lời vẫn vô ích.

### Lớp 2: dữ liệu có đúng phạm vi không?

Ta cần biết dữ liệu có đủ cửa hàng, đủ kênh và đúng trạng thái đơn hàng không.

### Lớp 3: phép tính có đúng không?

Ta cần kiểm công thức, phép nối, bộ lọc và hạt dữ liệu.

### Lớp 4: lời kết luận có vượt quá bằng chứng không?

Nếu dữ liệu chỉ cho thấy hai việc xảy ra cùng nhau, ta không được tự động nói việc này gây ra việc kia.

Một kết luận tốt phải qua cả bốn lớp.

## Ví dụ đầy đủ: vì sao con số giảm thay đổi sau khi kiểm dữ liệu?

Dashboard báo doanh thu giảm 12 phần trăm.

Data Analyst không vội gửi kết luận. Bạn ấy đối chiếu với dữ liệu giao dịch và phát hiện dashboard chưa trừ đúng một số khoản hoàn tiền ở kỳ đối chiếu. Sau khi sửa quy tắc, mức giảm còn 4 phần trăm.

Sau khi đối chiếu, bạn ấy chia kết quả theo nhóm khách:

| Nhóm | Thay đổi | Điều có thể nói |
|---|---:|---|
| Khách cũ | gần như không đổi | chưa cần can thiệp rộng |
| Khách mới | giảm rõ | cần điều tra tiếp |
| Khách mới từ quảng cáo | giảm mạnh nhất | đây là nơi ưu tiên kiểm tra |

Ta chưa được nói quảng cáo là nguyên nhân. Ta chỉ biết phần giảm tập trung ở nhóm đó.

Một truy vấn kiểm tra có thể bắt đầu như sau:

```sql
SELECT
    customer_group,
    acquisition_channel,
    SUM(order_amount - refund_amount) AS net_revenue
FROM order_facts
WHERE order_status = 'completed'
GROUP BY customer_group, acquisition_channel;
```

Truy vấn này chưa đủ để kết luận. Ta vẫn phải kiểm:

- một đơn có xuất hiện nhiều dòng không;
- `refund_amount` có cùng hạt với `order_amount` không;
- khách mới được định nghĩa theo lần mua đầu hay ngày tạo tài khoản;
- kênh có bị thiếu do lỗi tracking không.

### Dừng và hỏi

Nếu khách mới từ quảng cáo giảm mạnh nhất, ta có được nói quảng cáo làm doanh thu giảm không?

Không. Ta mới tìm thấy nơi chênh lệch tập trung. Để nói nguyên nhân, ta cần thêm bằng chứng và thiết kế phân tích phù hợp.

## Data Analyst khác các vai trò khác ở đâu?

Công cụ không quyết định vai trò. SQL có thể được Data Analyst, Data Engineer và Analytics Engineer cùng dùng.

Ta phân biệt bằng thứ mỗi vai trò phải bảo vệ.

| Vai trò | Điều phải bảo vệ | Sản phẩm thường tạo ra |
|---|---|---|
| Data Analyst | Kết luận có phù hợp với quyết định không | phân tích, metric, memo, dashboard |
| Data Engineer | Dữ liệu có được đưa đến đúng và phục hồi được không | pipeline, table, job, runbook |
| Analytics Engineer | Logic biến đổi và metric có nhất quán không | model, test, semantic layer |
| Data Scientist | Mô hình và suy luận có tổng quát được không | study, experiment, model |
| BI Engineer | Người dùng có đọc và tương tác đúng không | semantic model, report, dashboard |

Một người có thể làm nhiều vai trò. Khi đó vẫn phải nói rõ mình đang thực hiện vai trò nào và tiêu chí hoàn thành của phần việc đó là gì.

## Cách nói kết luận theo từng bậc

Ta dùng một thang kết luận để tránh nói quá.

1. Quan sát: Doanh thu thuần của nhóm khách mới thấp hơn kỳ đối chiếu.
2. Mô tả: Phần giảm tập trung ở kênh quảng cáo.
3. Giải thích có điều kiện: Nếu tracking ổn định và định nghĩa nhóm không đổi, thay đổi chiến dịch là một giả thuyết cần kiểm.
4. Khuyến nghị: Kiểm tracking và thay đổi chiến dịch trước khi đổi ngân sách.
5. Khẳng định nguyên nhân: Chỉ dùng khi có thiết kế và bằng chứng đủ mạnh.

Nhiều bài phân tích chỉ đủ bằng chứng cho bậc 1 hoặc bậc 2. Người phân tích dừng ở bậc mà bằng chứng hỗ trợ.

## Cùng viết một decision memo

Một memo ngắn có thể có cấu trúc sau:

```text
Quyết định cần hỗ trợ:
Có nên thay đổi ngân sách thu hút khách mới không?

Điều quan sát được:
Doanh thu thuần giảm chủ yếu ở khách mới từ kênh quảng cáo.

Bằng chứng:
Kết quả đã được đối chiếu với giao dịch và hoàn tiền.

Điều chưa biết:
Chưa xác nhận tracking và thay đổi cấu hình chiến dịch.

Hành động:
Kiểm tracking, đối chiếu thay đổi chiến dịch, sau đó xem lại quyết định.

Người chịu trách nhiệm:
Marketing owner và analytics owner.

Điều làm đổi quyết định:
Dữ liệu tracking bị thiếu hoặc kết quả không còn đúng khi dùng định nghĩa khách mới đã thống nhất.
```

Memo ghi rõ điều đã biết, điều chưa biết và người phải làm tiếp.

## Kiểm tra hiểu bài

Tự trả lời bằng lời của mình:

1. Vì sao Data Analyst không nên bắt đầu bằng dashboard?
2. Hạt dữ liệu là gì và vì sao hạt sai làm con số sai?
3. Quan sát khác nguyên nhân ở đâu?
4. Nếu dữ liệu thiếu, ta nên tiếp tục Analyze hay quay lại Prepare?
5. Một kết luận cần có những gì để người khác kiểm tra được?

Nếu chưa trả lời rõ, hãy quay lại `decision trace` và bốn lớp kiểm tra. Không cần nhớ mọi tên tiếng Anh. Cần hiểu đường đi từ quyết định đến bằng chứng và hành động.

## Điều cần mang theo

- Data Analyst hỗ trợ quyết định bằng output có thể kiểm tra.
- Một con số cần định nghĩa, hạt, phạm vi và phép đối chiếu.
- Quy trình Ask, Prepare, Process, Analyze, Share, Act có thể quay lại bước trước.
- Kết luận không được mạnh hơn bằng chứng.
- Công việc chỉ khép lại khi hành động, owner và điều kiện xem lại đã rõ.

## Đọc tiếp trong Second Brain

- [[wiki.da.operating-as-a-data-analyst|Vai trò và hệ điều hành công việc của Data Analyst]]
- [[wiki.data-product.decision-first-discovery|Bắt đầu từ quyết định cần hỗ trợ]]
- [[wiki.da.revenue-and-commerce-analytics|Phân tích doanh thu và thương mại]]
