---
note_id: wiki.da-foundation.entity-attribute-record-and-grain
concept_key: ck.da.entity-attribute-record-and-grain
concept_key_status: canonical
note_type: concept-deep-dive
status: canonical
approved_by: second-brain-owner
approved_at: 2026-10-03
approval_scope: all-registered-notes
canonical_since: 2026-10-03
language: vi
created: 2026-10-02
last_verified: 2026-10-02
review_after: 2027-04-02
editorial_pass: humanized-v3
primary_question: Làm sao áp dụng entity, attribute, record và grain của một tập dữ liệu mà vẫn giữ được ngữ nghĩa và bằng chứng kiểm chứng?
source_ids:
  - src.book.kimball-ross-data-warehouse-toolkit.3e
relationships:
  builds_on: [wiki.da-foundation.data-lifecycle-seven-stages]
  prerequisite_of: [wiki.da-foundation.three-question-tiers-and-metric-tree]
  related_to: []
aliases: [Entities, attributes, records and grain]
tags: [wiki/data-analysis, da-foundation, module-1]
reference_path: Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-FOUNDATIONS-01/003-entity-attribute-record-and-grain.md
---

# Entities, attributes, records and grain

**Tóm tắt bản chất:** Grain là lời cam kết mỗi dòng đại diện cho điều gì; entity cho biết đối tượng, attribute mô tả đối tượng, còn record là lần biểu diễn cụ thể ở grain đã chọn. Giá trị của mô hình này nằm ở chỗ nó làm lộ nơi một kết luận có thể sai trước khi kết luận đi vào quyết định.

## Nỗi Đau & Động Lực

Một yêu cầu phân tích thường đến dưới dạng câu ngắn và một bảng đã có sẵn. Với **Entities, attributes, records and grain**, cám dỗ lớn nhất là mở công cụ rồi thao tác ngay. Cách đó tạo output nhanh nhưng để lại câu hỏi khó hơn: con số đang đại diện cho population nào, ở grain nào, qua những biến đổi nào và có đủ bằng chứng để người khác tái hiện hay không?

Chi phí của việc bỏ qua `entity, attribute, record và grain của một tập dữ liệu` không nằm ở một câu lệnh lỗi. Kết quả vẫn có thể chạy, biểu đồ vẫn đẹp và người nhận vẫn ra quyết định. Lỗi chỉ lộ khi một báo cáo thứ hai cho số khác, khi dữ liệu tháng mới xuất hiện, hoặc khi reviewer hỏi một trường hợp biên mà logic hiện tại không giải thích được. Khi ấy, phần tốn kém nhất là truy lại assumption đã không được ghi.

## Cơ Chế Tác Động

Grain là lời cam kết mỗi dòng đại diện cho điều gì; entity cho biết đối tượng, attribute mô tả đối tượng, còn record là lần biểu diễn cụ thể ở grain đã chọn.

Với `entity, attribute, record và grain của một tập dữ liệu`, cơ chế được bóc thành năm lớp. Lớp thứ nhất khóa **đối tượng và population**: ai hoặc sự kiện nào được tính, ai bị loại. Lớp thứ hai khóa **identity và grain**: một dòng hay một quan sát đại diện cho điều gì. Lớp thứ ba khóa **thời gian**: event time, processing time, timezone và cutoff. Lớp thứ tư khóa **phép biến đổi**: lọc, join, aggregate, ánh xạ và xử lý thiếu. Lớp cuối cùng khóa **quyết định**: người nhận sẽ làm gì nếu kết quả cao, thấp hoặc chưa đủ chắc chắn.

Một bảng chỉ an toàn để đếm hoặc join khi grain được phát biểu bằng câu đầy đủ và khóa ứng viên thực sự duy nhất ở grain đó. Vì vậy, trước mỗi phép tính cần viết một câu ngắn có thể bị bác bỏ. Ví dụ: “mỗi dòng đại diện cho một đơn đã thanh toán theo giờ Việt Nam, tính tại thời điểm chốt 07:00”. Câu này hữu ích hơn tên bảng vì nó cho reviewer biết phải kiểm uniqueness, status và cutoff ở đâu.

## Bản Đồ Quyết Định

| Tình trạng bằng chứng | Hành động | Vì sao |
|---|---|---|
| Grain, population và metric đều rõ | Tiến hành phân tích, giữ lại phép đối soát | Có oracle để phát hiện sai lệch |
| Một assumption ảnh hưởng semantics chưa rõ | Dừng và hỏi owner | Tự chọn mặc định sẽ đổi nghĩa kết quả |
| Dữ liệu thiếu nhưng ảnh hưởng định lượng được | Phân tích có điều kiện, công bố coverage | Người nhận biết giới hạn của kết luận |
| Hai nguồn cho số khác nhau | Truy ngược boundary gần nguồn | Sửa công thức cuối chỉ che lỗi upstream |
| Deadline ngắn hơn thời gian kiểm chứng | Co phạm vi hoặc trả lời “chưa đủ bằng chứng” | Tốc độ không thay thế correctness |

Quy tắc ưu tiên là: Phát biểu grain trước, kiểm uniqueness và fan-out sau join, rồi mới chọn aggregate; nếu cần hai grain thì tách hai bảng hoặc aggregate về cùng grain trước khi ghép. Chọn sai nhánh làm analytical debt tăng rất nhanh, vì bảng hoặc dashboard mới thường tái sử dụng assumption cũ mà không biết đó chỉ là giả định.

## Case Study Thực Chiến: một chỉ số bán hàng đổi nghĩa giữa đường

Trong case của L003, một cửa hàng nhận yêu cầu giải thích vì sao “khách hàng hoạt động” giảm từ 12.400 xuống 10.900. Bảng dashboard tính khách có ít nhất một đơn tạo trong tháng. Hệ thống vận hành lại dùng khách có ít nhất một đơn **đã thanh toán**, còn CRM tính người có phiên truy cập trong 30 ngày. Ba con số đều chạy đúng theo code của mình nhưng không cùng khái niệm; `entity, attribute, record và grain của một tập dữ liệu` là lăng kính dùng để gỡ nút thắt.

Nhóm phân tích bắt đầu bằng `entity, attribute, record và grain của một tập dữ liệu`. Họ ghi population, grain, status, timezone và cửa sổ đo; sau đó lập ba phép đếm song song trên cùng snapshot. Kết quả cho thấy số đơn tạo giảm 12%, số đơn thanh toán chỉ giảm 3%, còn lượt truy cập tăng 8%. Vấn đề không còn là “khách hoạt động giảm” mà là tỷ lệ chuyển từ tạo đơn sang thanh toán giảm ở một nhóm thiết bị.

Biến thể khó hơn của `Entities, attributes, records and grain` xuất hiện khi một đơn có thể thanh toán lại sau thất bại và bảng payment giữ nhiều attempt. Nếu join trực tiếp orders với payments rồi đếm khách, fan-out làm số khách tăng giả. Nhóm phải chọn attempt hợp lệ theo identity, aggregate payment về grain đơn hàng, rồi mới quay lại grain khách hàng. Case này cho thấy một metric không thể được cứu chỉ bằng tên rõ; cơ chế dữ liệu phía dưới phải khớp định nghĩa.

## Góc Khuất & Ngộ Nhận

**Hiểu lầm:** Có dữ liệu trong database nghĩa là sự kiện ngoài đời đã được ghi chính xác. **Thực tế:** Trộn grain đơn hàng với grain dòng hàng làm doanh thu hoặc số khách bị nhân lên; khóa nhìn có vẻ duy nhất trên mẫu nhỏ có thể vỡ khi dữ liệu đủ dài. **Vì sao nghe hợp lý:** database tạo cảm giác chắc chắn vì kiểu dữ liệu và truy vấn đều hợp lệ, trong khi lỗi thu thập hoặc định nghĩa không tạo syntax error.

**Hiểu lầm:** Một dashboard thống nhất giao diện thì các chỉ số bên trong cũng thống nhất nghĩa, kể cả khi đang xét `entity, attribute, record và grain của một tập dữ liệu`. **Thực tế:** mỗi metric vẫn cần population, grain, thời gian, công thức và owner riêng. **Vì sao nghe hợp lý:** cùng một màn hình che việc các ô số lấy từ pipeline và cutoff khác nhau.

**Hiểu lầm:** Thêm nhiều lát cắt luôn giúp tìm nguyên nhân của L003. **Thực tế:** lát cắt trên metric chưa được khóa chỉ nhân số phiên bản của cùng một sai lệch. **Vì sao nghe hợp lý:** dashboard nhiều filter tạo cảm giác cuộc điều tra đang tiến triển dù câu hỏi gốc vẫn mơ hồ.

Trong `Entities, attributes, records and grain`, một trường hợp dễ bỏ sót là missing khác zero. Zero nói rằng đối tượng đã được quan sát và giá trị bằng không; missing nói rằng chưa có quan sát hoặc không ghép được. Ép missing thành zero làm mất dấu failure và thường đổi cả mẫu số. Trường hợp thứ hai là dữ liệu đến muộn: số của hôm nay có thể đúng theo snapshot hiện tại nhưng chưa đủ để so với kỳ đã đóng sổ.

## Nếu Bạn Dạy Lại Điều Này...

Khi dạy `entity, attribute, record và grain của một tập dữ liệu`, mở đầu bằng hai bảng cho cùng một doanh thu nhưng lệch 7%, không giải thích nguồn. Yêu cầu người học viết ba giả thuyết trước khi xem SQL. Bài tập seed là đổi đúng một constraint—cutoff, population hoặc grain—rồi buộc họ dự đoán con số nào đổi và phép kiểm nào bắt được thay đổi ấy.

## Ma trận kiểm chứng từng mệnh đề

Mỗi probe dưới đây là một phép thử có khả năng bác bỏ kết luận về `entity, attribute, record và grain của một tập dữ liệu`. Expected result phải được viết trước khi chạy; output không khớp thì giữ nguyên failure để điều tra, không sửa expected sau khi đã nhìn kết quả.

### Probe 1: Population và grain

**Mệnh đề cần kiểm.** Một bảng chỉ an toàn để đếm hoặc join khi grain được phát biểu bằng câu đầy đủ và khóa ứng viên thực sự duy nhất ở grain đó.

**Thiết kế phép thử cho `wiki.da-foundation.entity-attribute-record-and-grain`.** Probe 1 tạo fixture tối thiểu cho L003 ở trục `Population và grain`, gồm một happy path và một bản ghi chỉ khác tại boundary đang xét. Khóa snapshot, timezone, identity và công thức trước execution; sau đó ghi số dòng, số identity duy nhất và tổng kiểm soát ở cả đầu vào lẫn đầu ra.

**Bằng chứng cần giữ.** Với `Population và grain`, lưu truy vấn hoặc thao tác tái hiện, expected result, raw output, chênh lệch so với oracle và limitation. Probe 1 chỉ đạt khi reviewer độc lập có thể đi từ fixture đến cùng kết luận về `entity, attribute, record và grain của một tập dữ liệu` mà không cần hỏi tác giả chọn mặc định nào.

### Probe 2: Identity và uniqueness

**Mệnh đề cần kiểm.** Trộn grain đơn hàng với grain dòng hàng làm doanh thu hoặc số khách bị nhân lên; khóa nhìn có vẻ duy nhất trên mẫu nhỏ có thể vỡ khi dữ liệu đủ dài.

**Thiết kế phép thử cho `wiki.da-foundation.entity-attribute-record-and-grain`.** Probe 2 tạo fixture tối thiểu cho L003 ở trục `Identity và uniqueness`, gồm một happy path và một bản ghi chỉ khác tại boundary đang xét. Khóa snapshot, timezone, identity và công thức trước execution; sau đó ghi số dòng, số identity duy nhất và tổng kiểm soát ở cả đầu vào lẫn đầu ra.

**Bằng chứng cần giữ.** Với `Identity và uniqueness`, lưu truy vấn hoặc thao tác tái hiện, expected result, raw output, chênh lệch so với oracle và limitation. Probe 2 chỉ đạt khi reviewer độc lập có thể đi từ fixture đến cùng kết luận về `entity, attribute, record và grain của một tập dữ liệu` mà không cần hỏi tác giả chọn mặc định nào.

### Probe 3: Thời gian và cutoff

**Mệnh đề cần kiểm.** Grain là lời cam kết mỗi dòng đại diện cho điều gì; entity cho biết đối tượng, attribute mô tả đối tượng, còn record là lần biểu diễn cụ thể ở grain đã chọn.

**Thiết kế phép thử cho `wiki.da-foundation.entity-attribute-record-and-grain`.** Probe 3 tạo fixture tối thiểu cho L003 ở trục `Thời gian và cutoff`, gồm một happy path và một bản ghi chỉ khác tại boundary đang xét. Khóa snapshot, timezone, identity và công thức trước execution; sau đó ghi số dòng, số identity duy nhất và tổng kiểm soát ở cả đầu vào lẫn đầu ra.

**Bằng chứng cần giữ.** Với `Thời gian và cutoff`, lưu truy vấn hoặc thao tác tái hiện, expected result, raw output, chênh lệch so với oracle và limitation. Probe 3 chỉ đạt khi reviewer độc lập có thể đi từ fixture đến cùng kết luận về `entity, attribute, record và grain của một tập dữ liệu` mà không cần hỏi tác giả chọn mặc định nào.

### Probe 4: Định nghĩa metric

**Mệnh đề cần kiểm.** Phát biểu grain trước, kiểm uniqueness và fan-out sau join, rồi mới chọn aggregate; nếu cần hai grain thì tách hai bảng hoặc aggregate về cùng grain trước khi ghép.

**Thiết kế phép thử cho `wiki.da-foundation.entity-attribute-record-and-grain`.** Probe 4 tạo fixture tối thiểu cho L003 ở trục `Định nghĩa metric`, gồm một happy path và một bản ghi chỉ khác tại boundary đang xét. Khóa snapshot, timezone, identity và công thức trước execution; sau đó ghi số dòng, số identity duy nhất và tổng kiểm soát ở cả đầu vào lẫn đầu ra.

**Bằng chứng cần giữ.** Với `Định nghĩa metric`, lưu truy vấn hoặc thao tác tái hiện, expected result, raw output, chênh lệch so với oracle và limitation. Probe 4 chỉ đạt khi reviewer độc lập có thể đi từ fixture đến cùng kết luận về `entity, attribute, record và grain của một tập dữ liệu` mà không cần hỏi tác giả chọn mặc định nào.

### Probe 5: Đối soát độc lập

**Mệnh đề cần kiểm.** Câu grain, khóa ứng viên, phép kiểm uniqueness, số dòng trước–sau join và reconciliation tổng tiền theo oracle độc lập.

**Thiết kế phép thử cho `wiki.da-foundation.entity-attribute-record-and-grain`.** Probe 5 tạo fixture tối thiểu cho L003 ở trục `Đối soát độc lập`, gồm một happy path và một bản ghi chỉ khác tại boundary đang xét. Khóa snapshot, timezone, identity và công thức trước execution; sau đó ghi số dòng, số identity duy nhất và tổng kiểm soát ở cả đầu vào lẫn đầu ra.

**Bằng chứng cần giữ.** Với `Đối soát độc lập`, lưu truy vấn hoặc thao tác tái hiện, expected result, raw output, chênh lệch so với oracle và limitation. Probe 5 chỉ đạt khi reviewer độc lập có thể đi từ fixture đến cùng kết luận về `entity, attribute, record và grain của một tập dữ liệu` mà không cần hỏi tác giả chọn mặc định nào.

### Probe 6: Changed constraint

**Mệnh đề cần kiểm.** Thêm một đơn có nhiều dòng hàng hoặc một khách đổi thuộc tính phải làm learner nhận ra grain nào đổi và phép đếm nào cần sửa.

**Thiết kế phép thử cho `wiki.da-foundation.entity-attribute-record-and-grain`.** Probe 6 tạo fixture tối thiểu cho L003 ở trục `Changed constraint`, gồm một happy path và một bản ghi chỉ khác tại boundary đang xét. Khóa snapshot, timezone, identity và công thức trước execution; sau đó ghi số dòng, số identity duy nhất và tổng kiểm soát ở cả đầu vào lẫn đầu ra.

**Bằng chứng cần giữ.** Với `Changed constraint`, lưu truy vấn hoặc thao tác tái hiện, expected result, raw output, chênh lệch so với oracle và limitation. Probe 6 chỉ đạt khi reviewer độc lập có thể đi từ fixture đến cùng kết luận về `entity, attribute, record và grain của một tập dữ liệu` mà không cần hỏi tác giả chọn mặc định nào.

### Probe 7: Missing và zero

**Mệnh đề cần kiểm.** Trộn grain đơn hàng với grain dòng hàng làm doanh thu hoặc số khách bị nhân lên; khóa nhìn có vẻ duy nhất trên mẫu nhỏ có thể vỡ khi dữ liệu đủ dài.

**Thiết kế phép thử cho `wiki.da-foundation.entity-attribute-record-and-grain`.** Probe 7 tạo fixture tối thiểu cho L003 ở trục `Missing và zero`, gồm một happy path và một bản ghi chỉ khác tại boundary đang xét. Khóa snapshot, timezone, identity và công thức trước execution; sau đó ghi số dòng, số identity duy nhất và tổng kiểm soát ở cả đầu vào lẫn đầu ra.

**Bằng chứng cần giữ.** Với `Missing và zero`, lưu truy vấn hoặc thao tác tái hiện, expected result, raw output, chênh lệch so với oracle và limitation. Probe 7 chỉ đạt khi reviewer độc lập có thể đi từ fixture đến cùng kết luận về `entity, attribute, record và grain của một tập dữ liệu` mà không cần hỏi tác giả chọn mặc định nào.

### Probe 8: Join fan-out

**Mệnh đề cần kiểm.** Một bảng chỉ an toàn để đếm hoặc join khi grain được phát biểu bằng câu đầy đủ và khóa ứng viên thực sự duy nhất ở grain đó.

**Thiết kế phép thử cho `wiki.da-foundation.entity-attribute-record-and-grain`.** Probe 8 tạo fixture tối thiểu cho L003 ở trục `Join fan-out`, gồm một happy path và một bản ghi chỉ khác tại boundary đang xét. Khóa snapshot, timezone, identity và công thức trước execution; sau đó ghi số dòng, số identity duy nhất và tổng kiểm soát ở cả đầu vào lẫn đầu ra.

**Bằng chứng cần giữ.** Với `Join fan-out`, lưu truy vấn hoặc thao tác tái hiện, expected result, raw output, chênh lệch so với oracle và limitation. Probe 8 chỉ đạt khi reviewer độc lập có thể đi từ fixture đến cùng kết luận về `entity, attribute, record và grain của một tập dữ liệu` mà không cần hỏi tác giả chọn mặc định nào.

### Probe 9: Dữ liệu đến muộn

**Mệnh đề cần kiểm.** Grain là lời cam kết mỗi dòng đại diện cho điều gì; entity cho biết đối tượng, attribute mô tả đối tượng, còn record là lần biểu diễn cụ thể ở grain đã chọn.

**Thiết kế phép thử cho `wiki.da-foundation.entity-attribute-record-and-grain`.** Probe 9 tạo fixture tối thiểu cho L003 ở trục `Dữ liệu đến muộn`, gồm một happy path và một bản ghi chỉ khác tại boundary đang xét. Khóa snapshot, timezone, identity và công thức trước execution; sau đó ghi số dòng, số identity duy nhất và tổng kiểm soát ở cả đầu vào lẫn đầu ra.

**Bằng chứng cần giữ.** Với `Dữ liệu đến muộn`, lưu truy vấn hoặc thao tác tái hiện, expected result, raw output, chênh lệch so với oracle và limitation. Probe 9 chỉ đạt khi reviewer độc lập có thể đi từ fixture đến cùng kết luận về `entity, attribute, record và grain của một tập dữ liệu` mà không cần hỏi tác giả chọn mặc định nào.

### Probe 10: Quyết định đảo chiều

**Mệnh đề cần kiểm.** Phát biểu grain trước, kiểm uniqueness và fan-out sau join, rồi mới chọn aggregate; nếu cần hai grain thì tách hai bảng hoặc aggregate về cùng grain trước khi ghép.

**Thiết kế phép thử cho `wiki.da-foundation.entity-attribute-record-and-grain`.** Probe 10 tạo fixture tối thiểu cho L003 ở trục `Quyết định đảo chiều`, gồm một happy path và một bản ghi chỉ khác tại boundary đang xét. Khóa snapshot, timezone, identity và công thức trước execution; sau đó ghi số dòng, số identity duy nhất và tổng kiểm soát ở cả đầu vào lẫn đầu ra.

**Bằng chứng cần giữ.** Với `Quyết định đảo chiều`, lưu truy vấn hoặc thao tác tái hiện, expected result, raw output, chênh lệch so với oracle và limitation. Probe 10 chỉ đạt khi reviewer độc lập có thể đi từ fixture đến cùng kết luận về `entity, attribute, record và grain của một tập dữ liệu` mà không cần hỏi tác giả chọn mặc định nào.

### Probe 11: Reviewer tái hiện

**Mệnh đề cần kiểm.** Câu grain, khóa ứng viên, phép kiểm uniqueness, số dòng trước–sau join và reconciliation tổng tiền theo oracle độc lập.

**Thiết kế phép thử cho `wiki.da-foundation.entity-attribute-record-and-grain`.** Probe 11 tạo fixture tối thiểu cho L003 ở trục `Reviewer tái hiện`, gồm một happy path và một bản ghi chỉ khác tại boundary đang xét. Khóa snapshot, timezone, identity và công thức trước execution; sau đó ghi số dòng, số identity duy nhất và tổng kiểm soát ở cả đầu vào lẫn đầu ra.

**Bằng chứng cần giữ.** Với `Reviewer tái hiện`, lưu truy vấn hoặc thao tác tái hiện, expected result, raw output, chênh lệch so với oracle và limitation. Probe 11 chỉ đạt khi reviewer độc lập có thể đi từ fixture đến cùng kết luận về `entity, attribute, record và grain của một tập dữ liệu` mà không cần hỏi tác giả chọn mặc định nào.

### Probe 12: Tình huống mới

**Mệnh đề cần kiểm.** Thêm một đơn có nhiều dòng hàng hoặc một khách đổi thuộc tính phải làm learner nhận ra grain nào đổi và phép đếm nào cần sửa.

**Thiết kế phép thử cho `wiki.da-foundation.entity-attribute-record-and-grain`.** Probe 12 tạo fixture tối thiểu cho L003 ở trục `Tình huống mới`, gồm một happy path và một bản ghi chỉ khác tại boundary đang xét. Khóa snapshot, timezone, identity và công thức trước execution; sau đó ghi số dòng, số identity duy nhất và tổng kiểm soát ở cả đầu vào lẫn đầu ra.

**Bằng chứng cần giữ.** Với `Tình huống mới`, lưu truy vấn hoặc thao tác tái hiện, expected result, raw output, chênh lệch so với oracle và limitation. Probe 12 chỉ đạt khi reviewer độc lập có thể đi từ fixture đến cùng kết luận về `entity, attribute, record và grain của một tập dữ liệu` mà không cần hỏi tác giả chọn mặc định nào.

## Tự Kiểm Tra Nhanh

1. Boundary nào phải được khóa trước tiên khi áp dụng `entity, attribute, record và grain của một tập dữ liệu`?

<details><summary>Đáp án</summary>

Một bảng chỉ an toàn để đếm hoặc join khi grain được phát biểu bằng câu đầy đủ và khóa ứng viên thực sự duy nhất ở grain đó.

</details>

2. Failure nào dễ tạo kết quả “xanh giả” nhất?

<details><summary>Đáp án</summary>

Trộn grain đơn hàng với grain dòng hàng làm doanh thu hoặc số khách bị nhân lên; khóa nhìn có vẻ duy nhất trên mẫu nhỏ có thể vỡ khi dữ liệu đủ dài.

</details>

3. Bằng chứng nào đủ để một reviewer tái hiện kết luận?

<details><summary>Đáp án</summary>

Câu grain, khóa ứng viên, phép kiểm uniqueness, số dòng trước–sau join và reconciliation tổng tiền theo oracle độc lập.

</details>

## Giới hạn và điều chưa cho phép kết luận

- Case study là fixture giảng dạy; chưa phải quan sát production của một doanh nghiệp cụ thể.
- Các con số minh họa chỉ chứng minh cơ chế, không phải benchmark ngành.
- Concept key `ck.da.entity-attribute-record-and-grain` đã được owner phê duyệt `canonical`; note thuộc canonical registry coverage. Trạng thái này không tự chứng minh learner mastery.
- Note ở trạng thái `review`; việc note tồn tại không chứng minh learner đã thành thạo.

## Reference
1. [[SRC-KIMBALL-ROSS-DW-TOOLKIT-3E]] — `src.book.kimball-ross-data-warehouse-toolkit.3e`

## Source coverage

| Source slice | Locator | Kiến thức giữ lại | Trạng thái |
|---|---|---|---|
| [[SRC-KIMBALL-ROSS-DW-TOOLKIT-3E]] | Chapters 1–3: business process, grain, dimensions và facts | Cơ chế, boundary và decision rule cho `entity, attribute, record và grain của một tập dữ liệu` | Đã phủ |

## Key takeaways
- Phát biểu grain trước, kiểm uniqueness và fan-out sau join, rồi mới chọn aggregate; nếu cần hai grain thì tách hai bảng hoặc aggregate về cùng grain trước khi ghép.
- Câu grain, khóa ứng viên, phép kiểm uniqueness, số dòng trước–sau join và reconciliation tổng tiền theo oracle độc lập.
- Kết luận chỉ có nghĩa trong population, grain, thời gian và version đã ghi.
- Khi constraint đổi, phải chạy lại probe liên quan thay vì tái sử dụng kết luận cũ.

Note tiếp theo mở rộng chuỗi bằng quan hệ `prerequisite_of` đã khai báo trong front matter.

<!-- ATOMIC-EXECUTION-CAPSULE:START -->

## Execution capsule — kiểm chứng `wiki.da-foundation.entity-attribute-record-and-grain`

> [!important] Phân loại mệnh đề
> Với `wiki.da-foundation.entity-attribute-record-and-grain`, sơ đồ, ví dụ và artifact về **Entities, attributes, records and grain** là **synthesis để kiểm chứng**; chúng không phải trích dẫn hay case nguyên văn của nguồn.

### Sơ đồ cơ chế và điểm kiểm soát

```mermaid
flowchart LR
    S["Nguồn: src.book.kimball-ross-data-warehouse-toolkit.3e"] --> B["Khóa boundary"]
    B --> M["Cơ chế: Entities, attributes, records and grain"]
    M --> D{"Đủ evidence?"}
    D -- "Có" --> A["Áp dụng có điều kiện"]
    D -- "Không" --> X["Dừng hoặc thu hẹp claim"]
    A --> R["Theo dõi reversal trigger"]
    R --> B
```

Đọc sơ đồ `wiki.da-foundation.entity-attribute-record-and-grain` từ trái sang phải: source chỉ cung cấp claim ban đầu cho **Entities, attributes, records and grain**; quyết định chỉ được đi tiếp sau khi boundary, evidence và điều kiện đảo quyết định đã hiện hữu.

### Artifact thực thi tối thiểu

```yaml
concept_id: "wiki.da-foundation.entity-attribute-record-and-grain"
concept: "Entities, attributes, records and grain"
primary_question: "Làm sao áp dụng entity, attribute, record và grain của một tập dữ liệu mà vẫn giữ được ngữ nghĩa và bằng chứng kiểm chứng?"
decision_contract:
  input_boundary: "Ghi population, thời điểm, owner và điều chưa biết"
  hard_constraints:
    - "Không vượt quyền hoặc privacy boundary"
    - "Không dùng cùng một assumption làm cả implementation và oracle"
  accept_when: "Có observation phân biệt được các lựa chọn"
  reversal_trigger: "Một hard constraint sai hoặc evidence mới đổi recommendation"
evidence_to_keep:
  - "input snapshot"
  - "chosen and rejected options"
  - "independent review result"
```

Artifact của `wiki.da-foundation.entity-attribute-record-and-grain` buộc người dùng ghi boundary, oracle và reversal trigger cho **Entities, attributes, records and grain**. Các giá trị minh họa phải được thay bằng evidence thật trước khi dùng cho quyết định.

<!-- ATOMIC-EXECUTION-CAPSULE:END -->
