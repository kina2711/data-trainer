# -*- coding: utf-8 -*-
"""DE M15 BigQuery + M16 ClickHouse (mức B)."""

M15 = ("BigQuery", 159, 166, """| | |
|---|---|
| **Objective cấp module** | Dự đoán lượng dữ liệu quét và chi phí của một truy vấn trước khi chạy, rồi giảm nó bằng phân vùng, phân cụm và vật chất hoá |
| **Tiền đề** | M11 |
| **Exit criterion** | Giảm chi phí một bộ truy vấn ít nhất 70% bằng thiết kế bảng, có số byte quét trước và sau, và không vượt hạn mức chi tiêu đã đặt |
| **Kỹ năng SFIA** | `DBAD` mức 3 · `FMIT` mức 2 |
| **Chế độ hỏng** | Chạy truy vấn thử nghiệm trên bảng lớn mà không xem ước lượng byte quét, rồi nhận hoá đơn bất ngờ |""",
"""Mức `B`. Đây là module duy nhất trong bảy hệ chạy trên dịch vụ đám mây tính tiền thật, nên có một ràng buộc cứng: **đặt hạn mức chi tiêu và cảnh báo ngân sách trước khi chạy truy vấn đầu tiên**, và mọi lab thiết kế để chạy trong bậc miễn phí hoặc môi trường thử nghiệm. Ai không có tài khoản đám mây thì làm phần thiết kế và ước lượng, bỏ phần đo thật, và ghi rõ là chưa chạy được.""")

L15 = [
(159,"Serverless columnar warehouse - the model and what it changes","LT","Module 15: M11",
"Tách lưu trữ khỏi tính toán là khác biệt nền tảng so với sáu hệ còn lại: không có máy chủ để chỉnh tham số, không có bộ đệm để cấu hình, không có chỉ mục để tạo. Mọi đòn bẩy hiệu năng chuyển sang ba thứ: bố trí dữ liệu, lượng dữ liệu quét, và cách viết truy vấn. Lưu trữ theo cột theo mô hình ở lesson 70, nên chọn ít cột là đòn bẩy giảm chi phí trực tiếp và đây là lý do chọn mọi cột ở đây đắt hơn hẳn so với ở cơ sở dữ liệu quan hệ. Đơn vị tính toán và hai mô hình định giá: theo lượng dữ liệu quét và theo dung lượng tính toán đặt trước, cùng ngưỡng chuyển đổi. Ước lượng byte quét trước khi chạy bằng chế độ chạy thử, thao tác bắt buộc trước mọi truy vấn trong module. Giới hạn và hạn ngạch. Vì sao khái niệm chỉ mục không tồn tại ở đây và cái gì thay thế nó, dẫn sang lesson 161.",
"Ước lượng byte quét và chi phí của năm truy vấn trước khi chạy, và giải thích vì sao chọn ít cột giảm chi phí ở đây nhiều hơn ở PostgreSQL.",
"Tầng *hiểu*. Bài mở module, objective dừng ở ước lượng và giải thích cơ chế. Đạt khi năm ước lượng khớp con số chế độ chạy thử đưa ra, và khi giải thích đúng quan hệ giữa lưu trữ theo cột với chi phí. Ai không có tài khoản thì làm phần ước lượng trên lược đồ và ghi rõ chưa đo thật.",
"Đặt hạn mức chi tiêu và cảnh báo ngân sách trước tiên. Trên một bảng công khai, chạy chế độ chạy thử cho năm truy vấn khác nhau về số cột và bộ lọc. Ghi byte quét ước lượng. Chạy thật, so byte quét thực tế. Tính chi phí từng truy vấn theo đơn giá hiện hành, ghi rõ ngày tra đơn giá.",
"Chạy truy vấn trước khi đặt hạn mức chi tiêu · dùng chọn mọi cột để xem thử dữ liệu · tìm cách tạo chỉ mục theo thói quen từ hệ quan hệ.",
"Năm ước lượng khớp con số chế độ chạy thử, và quan hệ giữa lưu trữ cột với chi phí được giải thích đúng."),

(160,"Bytes scanned - the one number that decides cost","TH","Lesson 159",
"Chi phí ở mô hình theo lượng quét tỉ lệ thẳng với byte quét, nên tối ưu ở đây là bài toán giảm byte chứ không phải giảm thời gian, và hai mục tiêu đó không luôn cùng hướng. Bốn đòn bẩy theo thứ tự hiệu quả: chọn ít cột, lọc trên cột phân vùng, lọc trên cột phân cụm, và giới hạn dữ liệu trước khi kết. Điều không giảm byte quét dù trông như giảm: mệnh đề giới hạn số dòng trả về không giảm byte quét vì dữ liệu vẫn phải đọc, một hiểu nhầm rất phổ biến và tốn tiền. Bộ đệm kết quả truy vấn cho truy vấn giống hệt trong khoảng thời gian, miễn phí nhưng vô hiệu khi truy vấn có hàm không tất định. Bảng tạm và bảng trung gian: viết kết quả ra bảng rồi dùng lại rẻ hơn tính lại nhiều lần. Xem byte quét thật sau khi chạy và so với ước lượng. Theo dõi chi phí theo người dùng và theo truy vấn bằng khung nhìn siêu dữ liệu.",
"Giảm byte quét của một bộ năm truy vấn bằng bốn đòn bẩy, và chứng minh mệnh đề giới hạn số dòng không giảm byte quét.",
"Tầng *áp dụng*. Objective có tiêu chí đếm được bằng đơn vị byte. Đạt khi tổng byte quét của năm truy vấn giảm ít nhất 60%, và khi thực nghiệm cho thấy thêm mệnh đề giới hạn không đổi byte quét. Giảm thời gian mà không giảm byte thì không tính.",
"Ghi byte quét nền cho năm truy vấn. Áp bốn đòn bẩy từng cái một, đo sau mỗi bước. Thêm mệnh đề giới hạn 10 dòng vào một truy vấn quét 50 ghi ga byte và so byte quét trước sau. Chạy lại một truy vấn giống hệt và quan sát bộ đệm kết quả, rồi thêm hàm thời gian hiện tại và quan sát nó mất hiệu lực.",
"Dùng mệnh đề giới hạn để giảm chi phí · tối ưu thời gian mà không nhìn byte · lặp lại một truy vấn nặng nhiều lần thay vì ghi ra bảng trung gian.",
"Tổng byte quét giảm ít nhất 60%, và thực nghiệm cho thấy mệnh đề giới hạn không đổi byte quét."),

(161,"Partitioning and clustering - the replacement for indexes","TH","Lesson 160",
"Phân vùng chia bảng theo một cột thời gian hoặc số nguyên, và lọc trên cột đó cho phép bỏ qua cả phân vùng, cùng cơ chế cắt tỉa ở lesson 115. Điều kiện cắt tỉa hoạt động giống hệt ở đó: bộ lọc phải trên chính cột phân vùng và không bọc hàm, nối lại lesson 96. Phân cụm sắp dữ liệu trong mỗi phân vùng theo tối đa bốn cột, cho phép bỏ qua khối dữ liệu không liên quan; nó không phải chỉ mục vì không có cấu trúc tra cứu riêng, nó chỉ là thứ tự vật lý. Thứ tự cột phân cụm quan trọng như thứ tự cột chỉ mục phức hợp ở lesson 111. Hiệu quả phân cụm giảm dần khi dữ liệu mới được thêm vào và tự phục hồi bằng tiến trình nền. Yêu cầu bắt buộc lọc phân vùng để chặn truy vấn quét cả bảng. Hết hạn phân vùng để tự xoá dữ liệu cũ. Chi phí thiết kế sai: phân vùng theo cột bản số cao tạo quá nhiều phân vùng nhỏ, nối lại lesson 15.",
"Thiết kế phân vùng và phân cụm cho một bảng và bộ truy vấn cho trước, và chứng minh cắt tỉa hoạt động bằng byte quét.",
"Tầng *đánh giá*. Objective đòi chọn cột và thứ tự có đánh đổi giữa các truy vấn khác nhau. Đạt khi byte quét của bộ truy vấn giảm ít nhất 70% so với bảng không phân vùng, và khi người học nêu được truy vấn nào bị thiệt vì lựa chọn này cùng lý do.",
"Nạp 100 triệu dòng sự kiện vào ba bảng: không phân vùng, phân vùng theo ngày, và phân vùng cộng phân cụm ba cột. Chạy bộ sáu truy vấn trên cả ba, ghi byte quét. Viết một truy vấn bọc hàm quanh cột phân vùng và quan sát cắt tỉa mất hiệu lực. Bật yêu cầu bắt buộc lọc phân vùng và thử truy vấn thiếu bộ lọc.",
"Phân vùng theo cột bản số cao · đặt cột phân cụm theo thứ tự tuỳ ý · bọc hàm quanh cột phân vùng trong bộ lọc.",
"Byte quét giảm ít nhất 70% so với bảng không phân vùng, và truy vấn bị thiệt được nêu kèm lý do."),

(162,"Reading the query plan - stages, slots and shuffle","TH","Lesson 161",
"Kế hoạch thực thi trình bày theo giai đoạn chứ không theo cây toán tử như lesson 113, vì thực thi phân tán theo từng đợt. Mỗi giai đoạn có số bản ghi vào ra, thời gian chờ, thời gian đọc, thời gian tính, và thời gian ghi; phân bố bốn con số này chỉ ra nút cổ chai nằm ở đâu. Xáo trộn dữ liệu giữa các giai đoạn là thao tác đắt nhất, cùng kết luận với lesson 48, và nó xuất hiện khi kết hoặc gộp nhóm trên cột không phân cụm. Lệch dữ liệu hiện ra ở chênh lệch giữa thời gian công nhân chậm nhất và trung bình trong một giai đoạn, và đây là cách phát hiện trực tiếp nhất. Đơn vị tính toán và hàng đợi khi hết đơn vị. Kết phát tán khi một bảng đủ nhỏ, tương tự lesson 44. Ba dấu hiệu trong kế hoạch cần nhận ra ngay: giai đoạn lặp lại nhiều lần, một giai đoạn chiếm phần lớn thời gian, và tỉ lệ bản ghi ra trên vào tăng vọt.",
"Đọc kế hoạch theo giai đoạn và định vị nút cổ chai, phân biệt được lệch dữ liệu với thiếu đơn vị tính toán.",
"Tầng *phân tích*. Objective đòi phân biệt hai nguyên nhân có cùng triệu chứng là truy vấn chậm. Kiểm bằng ba truy vấn: một lệch khoá kết, một xáo trộn lớn, một chờ đơn vị tính toán. Đạt khi định vị đúng cả ba và dẫn được con số từ kế hoạch cho từng ca.",
"Chạy ba truy vấn dựng sẵn. Với mỗi cái, lập bảng bốn con số cho từng giai đoạn. Định vị nút cổ chai. Với ca lệch, so thời gian công nhân chậm nhất và trung bình. Sửa ca lệch bằng thêm hậu tố ngẫu nhiên vào khoá kết và đo lại.",
"Kết luận thiếu tài nguyên khi thật ra lệch dữ liệu · đọc tổng thời gian mà không xem phân bố theo giai đoạn · bỏ qua xáo trộn khi tối ưu.",
"Định vị đúng nút cổ chai cho cả ba truy vấn, mỗi ca dẫn được con số từ kế hoạch."),

(163,"Materialized views, scheduled queries and precomputation","TH","Lesson 162",
"Ba cách tính trước và điều kiện chọn từng cái. Khung nhìn thường không lưu gì nên không giảm byte quét, chỉ giảm lặp mã. Khung nhìn vật chất hoá lưu kết quả và tự cập nhật tăng dần khi bảng nguồn đổi, nên truy vấn đọc nó quét ít byte hơn nhiều; đổi lại có ràng buộc về loại phép gộp dùng được và chi phí lưu trữ cộng chi phí cập nhật. Truy vấn theo lịch ghi kết quả ra bảng, linh hoạt hơn nhưng phải tự quản lý tính mới. Tự động dùng khung nhìn vật chất hoá: bộ tối ưu hoá có thể viết lại truy vấn trên bảng gốc thành truy vấn trên khung nhìn, nên người dùng cuối hưởng lợi mà không phải đổi mã. Phép tính lợi ích ròng: byte tiết kiệm mỗi lần đọc nhân số lần đọc, trừ chi phí lưu và chi phí cập nhật; cùng khung tính với lesson 158. Bảng tổng hợp thủ công khi ràng buộc của khung nhìn vật chất hoá không cho phép.",
"Chọn giữa ba cách tính trước cho ba tình huống có tần suất đọc khác nhau, và chứng minh lựa chọn bằng phép tính lợi ích ròng.",
"Tầng *đánh giá*. Objective đòi quyết định dựa trên một phép tính có hai vế. Đạt khi ba lựa chọn đều có phép tính lợi ích ròng bằng số, và khi ít nhất một tình huống kết luận là không nên tính trước vì tần suất đọc quá thấp.",
"Ba tình huống: bảng đọc 500 lần mỗi ngày, 5 lần mỗi ngày, và 1 lần mỗi tuần. Với mỗi cái, đo byte quét của truy vấn gốc, tạo khung nhìn vật chất hoá, đo byte quét mới và chi phí cập nhật. Tính lợi ích ròng. Kiểm xem truy vấn trên bảng gốc có tự được viết lại không.",
"Tạo khung nhìn vật chất hoá cho truy vấn ít đọc · quên tính chi phí cập nhật khi nguồn đổi liên tục · dùng khung nhìn thường rồi tưởng nó giảm chi phí.",
"Ba lựa chọn đều có phép tính lợi ích ròng bằng số, và ít nhất một tình huống kết luận không nên tính trước."),

(164,"Loading data - batch, streaming and the cost of each","TH","Lesson 163",
"Bốn đường nạp dữ liệu và đặc tính khác nhau: nạp theo lô từ tệp thường miễn phí nhưng có độ trễ, chèn theo luồng tính tiền và có độ trễ thấp, truyền dữ liệu liên tục từ nguồn, và truy vấn trực tiếp trên tệp ngoài không cần nạp. Chọn đường nào là quyết định về độ trễ đổi lấy chi phí, và phần lớn tải phân tích không cần độ trễ thấp nên nạp theo lô là mặc định đúng. Bộ đệm luồng và khoảng thời gian dữ liệu vừa chèn chưa sửa hoặc xoá được, một ràng buộc hay gây bất ngờ. Bất biến khi chạy lại ở đây: chèn theo luồng không có khoá duy nhất nên phải khử trùng ở tầng sau hoặc dùng mã định danh chèn, nối lại lesson 106. Bảng ngoài trỏ vào tệp trên lưu trữ đối tượng và khi nào nó hợp: dữ liệu ít truy vấn, hoặc dùng chung với công cụ khác. Định dạng tệp và ảnh hưởng lên tốc độ nạp, nối lại lesson 70.",
"Chọn đường nạp cho ba yêu cầu độ trễ khác nhau, và đo chi phí cùng độ trễ thật của từng đường.",
"Tầng *đánh giá*. Objective đòi cân độ trễ với chi phí. Đạt khi ba đường nạp đều có số đo độ trễ và chi phí, và khi lựa chọn cho từng yêu cầu dẫn được về hai con số đó chứ không về thói quen.",
"Nạp cùng 10 triệu bản ghi bằng ba đường: theo lô từ tệp, chèn theo luồng, và bảng ngoài. Đo thời gian tới khi truy vấn được và chi phí từng cách. Thử sửa một dòng vừa chèn theo luồng và quan sát ràng buộc. Chèn trùng có chủ đích và thiết kế cách khử trùng.",
"Dùng chèn theo luồng cho tải phân tích hằng ngày · giả định dữ liệu vừa chèn theo luồng sửa được ngay · nạp tệp không nén khi mạng là nút cổ chai.",
"Ba đường nạp đều có số đo độ trễ và chi phí, và lựa chọn dẫn được về hai con số đó."),

(165,"Access control, data governance and cost attribution","TH","Lesson 164",
"Phân quyền theo bốn tầng và nguyên tắc đặc quyền tối thiểu, nối lại lesson 23. Phân quyền ở mức tập dữ liệu, mức bảng, mức cột, và mức hàng; hai mức sau cho phép một bảng phục vụ nhiều nhóm với phạm vi khác nhau. Tài khoản dịch vụ cho pipeline và nguyên tắc mỗi pipeline một tài khoản riêng để truy được ai làm gì. Khung nhìn được uỷ quyền để cho truy cập kết quả mà không cho truy cập bảng gốc, mẫu thay thế cho việc sao chép dữ liệu. Gắn thẻ dữ liệu nhạy cảm và che ở mức cột. Nhật ký kiểm toán ghi mọi truy vấn kèm người chạy và byte quét, nên nó vừa là công cụ bảo mật vừa là công cụ phân bổ chi phí. Gắn nhãn cho truy vấn và bảng để quy chi phí về nhóm. Hạn mức chi tiêu ở nhiều mức và cảnh báo ngân sách, thứ đáng ra phải đặt từ lesson 159.",
"Thiết lập phân quyền cho ba nhóm người dùng có phạm vi khác nhau, và quy được chi phí truy vấn về từng nhóm bằng nhật ký kiểm toán.",
"Tầng *áp dụng*. Objective có hai sản phẩm kiểm được. Đạt khi ba nhóm chỉ truy cập được đúng phạm vi của mình, xác nhận bằng thử truy cập ngoài phạm vi và bị từ chối, và khi bảng chi phí theo nhóm tổng lại bằng tổng chi phí thật.",
"Ba nhóm: phân tích được xem mọi cột trừ cột định danh cá nhân, vận hành chỉ xem dữ liệu 7 ngày gần nhất, và đối tác chỉ xem một tập hàng. Cài phân quyền theo cột, theo hàng, và khung nhìn được uỷ quyền. Thử truy cập ngoài phạm vi cho từng nhóm. Gắn nhãn truy vấn và lập bảng chi phí theo nhóm từ nhật ký kiểm toán.",
"Cấp quyền ở mức dự án cho tiện · dùng một tài khoản dịch vụ cho mọi pipeline · sao chép dữ liệu ra bảng riêng thay vì dùng khung nhìn được uỷ quyền.",
"Ba nhóm bị từ chối đúng khi truy cập ngoài phạm vi, và bảng chi phí theo nhóm tổng bằng tổng chi phí thật."),

(166,"Reducing the cost of a query set by seventy percent","TH","Lesson 165",
"Không có cơ chế mới. Bài gộp module: nhận một bộ truy vấn tốn kém và giảm chi phí bằng mọi đòn bẩy đã học, theo thứ tự chi phí thực hiện tăng dần. Trước tiên là thứ không đổi dữ liệu: bớt cột, thêm bộ lọc, dùng lại bộ đệm kết quả. Sau đó là thứ đổi bố trí: phân vùng và phân cụm ở lesson 161. Cuối cùng là tính trước ở lesson 163. Nguyên tắc của bài: mỗi thay đổi đo riêng và ghi lại, vì gộp nhiều thay đổi rồi đo một lần thì không biết cái nào có tác dụng, nối lại lesson 17. Kiểm chứng bắt buộc: kết quả truy vấn sau khi tối ưu phải khớp từng dòng với kết quả gốc, vì giảm chi phí bằng cách vô tình đọc thiếu dữ liệu là sai chứ không phải tối ưu. Báo cáo cuối là một trong bảy đầu vào của M18.",
"Giảm tổng byte quét của một bộ truy vấn ít nhất 70% mà kết quả khớp từng dòng với bản gốc, và ghi được đóng góp riêng của từng thay đổi.",
"Tầng *đánh giá*. Objective đòi chuỗi quyết định có đo từng bước cùng một ràng buộc đúng đắn tuyệt đối. Đạt khi tổng byte quét giảm ít nhất 70%, khi mọi kết quả khớp từng dòng với bản gốc, và khi bảng đóng góp cho thấy riêng từng thay đổi. Giảm đủ mà kết quả lệch một dòng là không đạt.",
"Nhận bộ 10 truy vấn trên bảng 500 ghi ga byte. Ghi byte quét nền và kết quả gốc. Áp từng thay đổi một, đo sau mỗi bước, đối chiếu kết quả từng dòng. Lập bảng đóng góp. Kiểm hạn mức chi tiêu không bị vượt trong suốt quá trình.",
"Gộp nhiều thay đổi rồi đo một lần · giảm chi phí bằng cách thu hẹp phạm vi dữ liệu mà không báo · quên đối chiếu kết quả sau khi đổi bố trí bảng.",
"Tổng byte quét giảm ít nhất 70%, mọi kết quả khớp từng dòng với bản gốc, và bảng đóng góp tách riêng từng thay đổi."),
]

M16 = ("ClickHouse", 167, 174, """| | |
|---|---|
| **Objective cấp module** | Chọn khoá sắp xếp và khoá phân vùng cho một tải sự kiện, và chẩn đoán truy vấn chậm bằng số phần dữ liệu đọc |
| **Tiền đề** | M11 |
| **Exit criterion** | Nạp 200 triệu sự kiện, đạt độ trễ truy vấn dưới ngưỡng đặt trước, và sửa được một truy vấn đọc quá nhiều phần dữ liệu |
| **Kỹ năng SFIA** | `DBAD` mức 3 |
| **Chế độ hỏng** | Chọn khoá sắp xếp theo thói quen khoá chính của hệ quan hệ, rồi mọi truy vấn quét toàn bảng mà vẫn tưởng nhanh vì máy khoẻ |""",
"Mức `B`. ClickHouse tối ưu cho một tải rất hẹp là phân tích trên dữ liệu chỉ chèn thêm, và nó đánh đổi gần như mọi thứ khác để đạt điều đó. Module bám hai quyết định thiết kế quyết định tất cả: khoá sắp xếp và khoá phân vùng. Bài cuối là chẩn đoán và sửa một truy vấn đọc thừa.")

L16 = [
(167,"MergeTree - parts, merges and the sorting key","LT","Module 16: M11",
"Họ bảng chính lưu dữ liệu thành các phần đã sắp theo khoá sắp xếp, và tiến trình nền trộn các phần nhỏ thành phần lớn, cấu trúc cùng họ với cây trộn có cấu trúc nhật ký ở lesson 111. Mỗi lần chèn tạo một phần mới, nên chèn từng dòng tạo hàng triệu phần và giết hệ thống; quy tắc là chèn theo lô lớn, và đây là ràng buộc quan trọng nhất khi thiết kế pipeline nạp. Khoá sắp xếp quyết định thứ tự vật lý trong mỗi phần và là thứ duy nhất gần giống chỉ mục; chỉ mục thưa lưu một mục cho mỗi khối vài nghìn dòng thay vì mỗi dòng, nên nó rất nhỏ nhưng chỉ định vị được tới khối. Hệ quả: lọc trên tiền tố của khoá sắp xếp thì bỏ qua được phần lớn khối, lọc trên cột không nằm trong khoá thì phải đọc hết. Khoá chính ở đây là tiền tố của khoá sắp xếp chứ không ràng buộc duy nhất, khác hẳn nghĩa ở hệ quan hệ.",
"Giải thích vì sao chèn từng dòng làm hệ thống sụp, và dự đoán truy vấn nào bỏ qua được khối từ một khoá sắp xếp cho trước.",
"Tầng *phân tích*. Objective đòi suy từ cấu trúc lưu trữ ra hành vi truy vấn. Đạt khi dự đoán đúng ít nhất bốn trên năm truy vấn về việc có bỏ qua khối được không, xác nhận bằng số khối đọc thật, và khi thực nghiệm chèn từng dòng cho thấy số phần tăng vọt.",
"Tạo bảng với khoá sắp xếp ba cột. Dự đoán năm truy vấn có bỏ qua khối được không. Chạy và đọc số khối đọc thật. Chèn 100.000 dòng từng dòng một và đếm số phần, so với chèn theo lô 10.000 dòng. Quan sát tiến trình trộn chạy.",
"Chèn từng dòng như với hệ quan hệ · tưởng khoá chính ở đây ràng buộc duy nhất · lọc trên cột không nằm trong tiền tố khoá sắp xếp rồi tưởng có chỉ mục.",
"Dự đoán đúng ít nhất bốn trên năm truy vấn xác nhận bằng số khối đọc, và thực nghiệm chèn từng dòng cho thấy số phần tăng vọt."),

(168,"Choosing the sorting key and the partition key","TH","Lesson 167",
"Hai khoá phục vụ hai mục đích khác nhau và hay bị gộp. Khoá phân vùng chia dữ liệu thành nhóm quản lý được, thường theo tháng, và mục đích chính là vận hành: xoá dữ liệu cũ bằng thao tác siêu dữ liệu và giới hạn phạm vi trộn. Phân vùng theo ngày cho bảng giữ nhiều năm tạo quá nhiều phân vùng và làm chậm mọi thứ, một lỗi phổ biến. Khoá sắp xếp quyết định hiệu năng truy vấn, và quy tắc chọn thứ tự cột: cột lọc bằng và bản số thấp đặt trước, cột bản số cao đặt sau, ngược với trực giác từ chỉ mục quan hệ ở lesson 111. Lý do: bản số thấp trước cho phép bỏ qua nhiều khối hơn ở bước đầu. Cột thời gian thường đặt cuối. Chỉ mục nhảy cho cột không nằm trong khoá sắp xếp, cho phép bỏ qua khối dựa trên thống kê nhỏ nhất lớn nhất, ý tưởng giống chỉ mục phạm vi khối ở lesson 127. Đổi khoá sắp xếp sau khi có dữ liệu gần như không làm được, nên đây là quyết định phải đúng từ đầu.",
"Chọn khoá sắp xếp và khoá phân vùng cho một tải sự kiện cho trước, và chứng minh lựa chọn bằng số khối đọc của bộ truy vấn thường gặp.",
"Tầng *đánh giá*. Objective đòi quyết định khó đảo ngược dựa trên mẫu truy vấn. Đạt khi so được ít nhất ba phương án khoá sắp xếp trên cùng bộ truy vấn với số khối đọc, và khi lựa chọn cuối nêu được truy vấn nào bị thiệt cùng lý do.",
"Nạp 50 triệu sự kiện vào ba bảng có ba khoá sắp xếp khác nhau, cùng khoá phân vùng theo tháng. Chạy bộ sáu truy vấn trên cả ba, ghi số khối đọc và độ trễ. Thử phân vùng theo ngày và đếm số phân vùng sau một năm dữ liệu. Thêm chỉ mục nhảy cho một cột ngoài khoá và đo lại.",
"Đặt cột bản số cao đầu khoá sắp xếp · phân vùng theo ngày cho dữ liệu nhiều năm · coi khoá phân vùng là công cụ tăng tốc truy vấn.",
"Ba phương án khoá sắp xếp có số khối đọc so được, và lựa chọn cuối nêu truy vấn bị thiệt kèm lý do."),

(169,"Vectorized execution and why it is fast","LT","Lesson 168",
"Thực thi theo khối cột thay vì theo dòng: mỗi toán tử nhận một khối vài nghìn giá trị của một cột và xử lý cả khối, nên chi phí gọi hàm chia đều cho nhiều giá trị và dữ liệu nằm liên tục trong bộ nhớ. Đây là chỗ lesson 11 về dòng bộ nhớ đệm và lesson 10 về tập lệnh đơn dòng nhiều dữ liệu cho ra hiệu quả đo được. Nén theo cột và các thuật toán chuyên cho từng kiểu dữ liệu: cột có ít giá trị phân biệt nén rất tốt, cột thời gian tăng dần nén bằng hiệu số. Chọn kiểu dữ liệu hẹp nhất đủ dùng là đòn bẩy trực tiếp lên cả dung lượng lẫn tốc độ, khác với hệ quan hệ nơi khác biệt nhỏ hơn. Kiểu từ điển cho cột chuỗi lặp nhiều. Giải nén tốn bộ xử lý nên có đánh đổi giữa tỉ lệ nén với tốc độ đọc, và thuật toán nén chọn được theo cột. Vì sao mô hình này tệ cho truy vấn lấy một dòng theo khoá.",
"Giải thích vì sao thực thi theo khối cột nhanh hơn theo dòng, và chứng minh ảnh hưởng của lựa chọn kiểu dữ liệu lên dung lượng và tốc độ.",
"Tầng *hiểu*. Bài lý thuyết nối cơ chế với số đo. Đạt khi giải thích đúng ba yếu tố làm nó nhanh, và khi thực nghiệm cho thấy đổi kiểu dữ liệu hẹp hơn giảm cả dung lượng lẫn thời gian truy vấn đo được.",
"Tạo hai bảng cùng dữ liệu nhưng khác kiểu: một dùng kiểu rộng mặc định, một dùng kiểu hẹp nhất đủ và kiểu từ điển cho cột lặp. So dung lượng sau nén và thời gian truy vấn gộp. Thử ba thuật toán nén cho một cột và đo tỉ lệ nén với thời gian đọc. Chạy một truy vấn lấy một dòng theo khoá và so với PostgreSQL.",
"Dùng kiểu rộng mặc định cho mọi cột · chọn nén mạnh nhất mà không đo chi phí bộ xử lý · dùng ClickHouse cho tải lấy một dòng theo khoá.",
"Ba yếu tố được giải thích đúng, và thực nghiệm cho thấy kiểu hẹp hơn giảm cả dung lượng lẫn thời gian."),

(170,"Materialized views and incremental aggregation","TH","Lesson 169",
"Khung nhìn vật chất hoá ở đây khác hẳn nghĩa ở hệ quan hệ: nó là một trình kích hoạt chạy khi chèn, tính trên khối dữ liệu vừa chèn rồi ghi kết quả vào bảng đích. Hệ quả quan trọng: nó chỉ thấy dữ liệu mới, không thấy dữ liệu đã có, nên tạo khung nhìn trên bảng đã đầy dữ liệu sẽ không có gì, và phải nạp lại lịch sử bằng tay. Hệ quả thứ hai: nó không thấy thao tác xoá và cập nhật. Họ bảng gộp trộn các dòng cùng khoá khi trộn, cho phép gộp tăng dần mà không cần đọc lại toàn bộ; kết quả chỉ đúng sau khi trộn xong nên truy vấn phải dùng phép gộp cuối để gộp nốt phần chưa trộn, và quên điều này là nguồn số sai âm thầm. Kiểu trạng thái gộp cho các phép gộp phức tạp như đếm phân biệt xấp xỉ, nối lại lesson 47. Chuỗi nhiều khung nhìn vật chất hoá và rủi ro khó lần vết.",
"Dựng khung nhìn vật chất hoá gộp tăng dần, và chứng minh kết quả đúng cả trước và sau khi tiến trình trộn chạy.",
"Tầng *áp dụng*. Objective có bẫy đúng đắn cụ thể là đọc trước khi trộn xong. Đạt khi truy vấn trên bảng đích cho kết quả khớp phép gộp trực tiếp trên bảng nguồn ở cả hai thời điểm, ngay sau khi chèn và sau khi trộn. Đúng sau khi trộn mà sai trước đó là không đạt.",
"Tạo bảng sự kiện và khung nhìn vật chất hoá gộp theo giờ vào bảng họ gộp. Chèn 10 triệu sự kiện. Truy vấn bảng đích ngay, so với gộp trực tiếp trên nguồn. Ép trộn rồi truy vấn lại. Sửa truy vấn bằng phép gộp cuối. Tạo một khung nhìn trên bảng đã có dữ liệu và quan sát nó trống.",
"Truy vấn bảng họ gộp mà không dùng phép gộp cuối · tạo khung nhìn vật chất hoá rồi tưởng nó xử lý cả dữ liệu cũ · trông chờ khung nhìn phản ánh thao tác xoá.",
"Kết quả khớp phép gộp trực tiếp ở cả hai thời điểm, trước và sau khi trộn."),

(171,"TTL, data lifecycle and mutations","TH","Lesson 170",
"Thời gian sống khai báo ở mức bảng hoặc mức cột, và ba hành động khi hết hạn: xoá dòng, chuyển sang ổ đĩa rẻ hơn, hoặc gộp lại ở mức thô hơn. Hành động thứ ba là mẫu giữ dữ liệu chi tiết ngắn hạn và dữ liệu tổng hợp dài hạn, thay thế cho việc viết pipeline dọn dẹp. Thời gian sống thực thi khi trộn chứ không theo lịch chính xác, nên dữ liệu quá hạn còn tồn tại một thời gian, cùng đặc tính với lesson 153. Cập nhật và xoá là thao tác nặng vì chúng viết lại cả phần dữ liệu, nên chúng được gọi là biến đổi và chạy bất đồng bộ; đây là lý do ClickHouse không hợp cho tải sửa dữ liệu thường xuyên. Theo dõi biến đổi đang chạy và huỷ khi cần. Xoá theo phân vùng là thao tác siêu dữ liệu nên nhanh hơn xoá theo điều kiện nhiều bậc, cùng kết luận với lesson 130. Họ bảng thay thế để cập nhật bằng cách chèn phiên bản mới.",
"Thiết kế vòng đời dữ liệu ba tầng bằng thời gian sống, và chứng minh xoá theo phân vùng nhanh hơn xoá theo điều kiện nhiều bậc.",
"Tầng *áp dụng*. Objective có hai tiêu chí đo được. Đạt khi ba tầng vòng đời hoạt động đúng sau khi ép trộn, và khi chênh lệch thời gian giữa xoá theo phân vùng với xoá theo điều kiện đạt ít nhất một bậc độ lớn.",
"Bảng 100 triệu sự kiện. Khai báo thời gian sống ba tầng: chi tiết 30 ngày, gộp theo giờ tới 1 năm, xoá sau đó. Ép trộn và kiểm từng tầng. So thời gian xoá một tháng dữ liệu bằng xoá phân vùng với bằng xoá theo điều kiện. Chạy một biến đổi cập nhật và theo dõi tiến độ.",
"Trông chờ thời gian sống chạy đúng giờ · dùng cập nhật và xoá thường xuyên như với hệ quan hệ · xoá dữ liệu cũ bằng điều kiện thay vì bằng phân vùng.",
"Ba tầng vòng đời hoạt động đúng sau khi ép trộn, và xoá theo phân vùng nhanh hơn ít nhất một bậc."),

(172,"Ingestion at scale - batching, buffering and backpressure","TH","Lesson 171",
"Ràng buộc chèn theo lô từ lesson 167 quyết định thiết kế cả pipeline nạp. Ba cách thoả ràng buộc đó: gom lô ở tầng ứng dụng, dùng bảng đệm nhận chèn nhỏ rồi tự xả theo lô, và nạp từ hệ thống luồng bằng bộ máy tích hợp. Cách thứ hai tiện nhưng dữ liệu trong bảng đệm mất khi tiến trình chết, nên nó không hợp dữ liệu không được mất. Kích thước lô và tần suất là hai tham số đánh đổi giữa độ trễ với số phần tạo ra, chọn bằng thực nghiệm giống lesson 71. Chèn bất đồng bộ và xác nhận trả về trước khi dữ liệu xuống đĩa. Chèn trùng và tính bất biến: có cơ chế loại bỏ khối chèn trùng dựa trên tổng kiểm tra trong một cửa sổ, nên chèn lại cùng một lô là an toàn, nhưng chỉ trong cửa sổ đó. Áp lực ngược khi tiến trình trộn không đuổi kịp tốc độ chèn: triệu chứng là số phần tăng dần và cuối cùng hệ thống từ chối chèn, nối lại lesson 57.",
"Thiết kế đường nạp thoả ràng buộc chèn theo lô, và tái hiện được tình huống trộn không đuổi kịp rồi xử lý.",
"Tầng *áp dụng*. Objective có tiêu chí kiểm bằng thực nghiệm ở hai chiều. Đạt khi đường nạp giữ số phần ổn định qua 30 phút chèn liên tục, và khi tái hiện được ca hệ thống từ chối chèn do quá nhiều phần rồi khôi phục bằng đúng biện pháp.",
"Dựng đường nạp gom lô ở tầng ứng dụng, chạy 30 phút, theo dõi số phần theo thời gian. Thử ba kích thước lô và so độ trễ với số phần. Ép tạo quá nhiều phần bằng chèn lô nhỏ tần suất cao, quan sát hệ thống từ chối. Chèn lại cùng một lô hai lần và kiểm số dòng.",
"Chèn từng dòng qua bảng đệm cho dữ liệu không được mất · tăng tần suất chèn để giảm độ trễ mà không theo dõi số phần · dựa vào cơ chế loại trùng ngoài cửa sổ của nó.",
"Số phần ổn định qua 30 phút chèn, và ca từ chối chèn được tái hiện rồi khôi phục bằng đúng biện pháp."),

(173,"Distributed tables, replication and the operational surface","LT","Lesson 172",
"Nhân bản ở mức bảng chứ không mức máy chủ, và nó dùng một dịch vụ điều phối bên ngoài để giữ đồng thuận về danh sách phần dữ liệu. Nhân bản bất đồng bộ và cửa sổ mất dữ liệu, cùng mô hình lesson 120. Bảng phân tán là một lớp định tuyến không chứa dữ liệu, đứng trước các bảng cục bộ trên nhiều cụm; truy vấn qua nó được gửi tới mọi cụm rồi gộp kết quả. Khoá phân mảnh quyết định dữ liệu về cụm nào, và gộp nhóm trên cột không phải khoá phân mảnh cần gộp hai bước, nối lại lesson 48. Ghi qua bảng phân tán là bất đồng bộ và có thể mất, nên ghi thẳng vào bảng cục bộ an toàn hơn, một chi tiết vận hành quan trọng. Kết phân tán và chi phí của nó, cùng lý do phát tán bảng chiều nhỏ tới mọi cụm là mẫu phổ biến. Khi nào chưa cần phân tán: một máy hiện đại xử lý được tải lớn hơn nhiều người tưởng.",
"Nêu ba khác biệt giữa bảng phân tán và bảng cục bộ ảnh hưởng tới tính đúng đắn, và chỉ ra khi nào một cụm một máy là đủ.",
"Tầng *hiểu*. Bài lý thuyết vì dựng cụm nhiều máy vượt phạm vi mức `B`. Đạt khi ba khác biệt nêu ra đều liên quan tới đúng đắn chứ không chỉ hiệu năng, và khi ngưỡng cần phân tán được phát biểu bằng số dựa trên đo đạc ở lesson 168.",
"Dựng hai nút với một bảng nhân bản và một bảng phân tán. Ghi qua bảng phân tán rồi giết tiến trình, đếm dòng mất. Ghi thẳng vào bảng cục bộ và so. Chạy gộp nhóm trên cột không phải khoá phân mảnh và đọc kế hoạch. Từ số đo lesson 168, ước lượng ngưỡng dữ liệu cần phân tán.",
"Ghi qua bảng phân tán cho dữ liệu không được mất · phân tán khi một máy còn thừa sức · gộp nhóm trên cột không phải khoá phân mảnh mà không biết có hai bước.",
"Ba khác biệt đều liên quan tới đúng đắn, và ngưỡng cần phân tán phát biểu được bằng số."),

(174,"Diagnosing a query that reads too many parts","TH","Lesson 173",
"Không có cơ chế mới. Bài gộp module: chẩn đoán và sửa truy vấn chậm theo một quy trình bốn bước. Bước một đọc số phần và số khối truy vấn đã đọc, con số quan trọng nhất và tương đương với byte quét ở lesson 160. Bước hai xác định nguyên nhân trong bốn nguyên nhân: bộ lọc không chạm tiền tố khoá sắp xếp, hàm bọc quanh cột khoá, quá nhiều phần do trộn không đuổi kịp ở lesson 172, hoặc phân vùng quá nhỏ và quá nhiều. Bước ba sửa đúng nguyên nhân. Bước bốn đo lại và đối chiếu kết quả từng dòng. Nhật ký truy vấn ghi số phần đọc, byte đọc, bộ nhớ dùng và thời gian cho mọi truy vấn, nên nó là nguồn chẩn đoán chính. Giới hạn bộ nhớ mỗi truy vấn và hành vi khi vượt. Báo cáo cuối là một trong bảy đầu vào của M18.",
"Chẩn đoán bốn truy vấn chậm về đúng nguyên nhân bằng số phần đọc, sửa, và chứng minh kết quả không đổi.",
"Tầng *phân tích*. Objective là chẩn đoán phân biệt bốn nguyên nhân cùng triệu chứng. Đạt khi định vị đúng ít nhất ba trên bốn, mỗi lần dẫn số phần đọc từ nhật ký truy vấn, và khi kết quả sau sửa khớp từng dòng với trước sửa.",
"Nhận bốn truy vấn chậm trên bảng 200 triệu dòng, mỗi truy vấn chậm vì một nguyên nhân khác nhau. Với mỗi cái, đọc nhật ký truy vấn lấy số phần và số khối. Định vị, sửa, đo lại, đối chiếu kết quả. Chạy một truy vấn vượt giới hạn bộ nhớ và quan sát.",
"Kết luận máy yếu khi số phần đọc mới là nguyên nhân · sửa bằng thêm tài nguyên · quên đối chiếu kết quả sau khi sửa truy vấn.",
"Định vị đúng ít nhất ba trên bốn nguyên nhân có số phần đọc làm bằng chứng, và kết quả sau sửa khớp từng dòng."),
]
