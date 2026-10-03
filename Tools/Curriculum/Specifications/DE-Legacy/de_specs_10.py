# -*- coding: utf-8 -*-
"""DE M12 MySQL + M13 MongoDB + M14 Redis (mức B)."""

M12 = ("MySQL", 136, 143, """| | |
|---|---|
| **Objective cấp module** | Chỉ ra ba quyết định thiết kế của InnoDB khiến cùng một lược đồ cho hiệu năng khác PostgreSQL, và chứng minh bằng số đo trên cùng bộ dữ liệu |
| **Tiền đề** | M11 |
| **Exit criterion** | Báo cáo so sánh MySQL với PostgreSQL trên cùng use case, có số đo cho chỉ mục phức hợp, bế tắc, độ trễ bản sao và khôi phục |
| **Kỹ năng SFIA** | `DBAD` mức 3 |
| **Chế độ hỏng** | Mang giả định PostgreSQL sang MySQL, nhất là về chỉ mục và khoá, rồi lược đồ chạy chậm mà không hiểu vì sao |""",
"Mức `B`: làm lab và so sánh có căn cứ, không vận hành sản xuất. Module bám một trục duy nhất là khoá chính gom cụm của InnoDB, vì gần như mọi khác biệt với PostgreSQL suy ra từ đó. Bài cuối là báo cáo so sánh có số, và nó là đầu vào cho M18.")

L12 = [
(136,"InnoDB - the clustered primary key and what it changes","LT","Module 12: M11",
"InnoDB lưu dòng dữ liệu ngay trong lá của cây chỉ mục khoá chính, nên bảng chính là chỉ mục đó, khác hẳn mô hình đống của PostgreSQL ở lesson 123. Ba hệ quả suy ra từ một lựa chọn này. Một, thứ tự vật lý của dòng theo khoá chính, nên quét khoảng theo khoá chính rất rẻ còn chèn khoá ngẫu nhiên gây tách trang và phân mảnh; đây là lý do khoá tự tăng được khuyên dùng và khoá định danh ngẫu nhiên bị tránh. Hai, khoá chính lớn làm mọi chỉ mục phụ lớn theo, vì chỉ mục phụ lưu khoá chính thay vì con trỏ vật lý. Ba, không có khoá chính thì InnoDB tự tạo một khoá ẩn, nên bảng vẫn gom cụm nhưng theo một cột không kiểm soát được. Nhật ký hoàn tác lưu phiên bản cũ ở vùng riêng chứ không trong bảng, nên MySQL không có bài toán phình giống lesson 125 nhưng có bài toán nhật ký hoàn tác phình.",
"Giải thích ba hệ quả của khoá chính gom cụm, và dự đoán bảng nào trong ba lược đồ cho trước sẽ phân mảnh nặng nhất.",
"Tầng *phân tích*. Objective đòi suy từ một lựa chọn thiết kế ra nhiều hệ quả đo được. Đạt khi dự đoán đúng bảng phân mảnh nặng nhất và khi số đo phân mảnh sau khi chèn xác nhận thứ hạng dự đoán cho cả ba bảng.",
"Tạo ba bảng cùng lược đồ nhưng khoá chính khác nhau: tự tăng, định danh ngẫu nhiên, và khoá phức hợp rộng. Dự đoán thứ hạng phân mảnh. Chèn 5 triệu dòng vào mỗi bảng theo thứ tự ngẫu nhiên. Đo kích thước bảng, kích thước chỉ mục phụ, và thời gian chèn. So với dự đoán.",
"Dùng định danh ngẫu nhiên làm khoá chính trong InnoDB · để bảng không có khoá chính · mang giả định mô hình đống của PostgreSQL sang.",
"Dự đoán đúng thứ hạng phân mảnh cho cả ba bảng, xác nhận bằng số đo kích thước và thời gian chèn."),

(137,"Secondary indexes and the double lookup","TH","Lesson 136",
"Chỉ mục phụ lưu giá trị cột cộng khoá chính, nên tra cứu qua chỉ mục phụ là hai bước: tìm trong chỉ mục phụ ra khoá chính, rồi tìm trong cây khoá chính ra dòng. Chi phí bước hai là lý do chỉ mục phủ có giá trị lớn hơn ở MySQL so với ở PostgreSQL: khi mọi cột cần đều nằm trong chỉ mục phụ, bước hai biến mất hoàn toàn. Quy tắc tiền tố trái áp dụng như lesson 111, nhưng kết hợp với khoá chính ngầm ở cuối chỉ mục phụ tạo ra cơ hội phủ mà người quen PostgreSQL hay bỏ lỡ. Chỉ mục trên tiền tố chuỗi cho cột văn bản dài và mất mát kèm theo. Chỉ mục giảm dần và trường hợp nó cần. Chọn lọc của cột và thứ tự cột trong chỉ mục phức hợp: đặt cột chọn lọc cao trước là quy tắc mặc định nhưng không đúng khi truy vấn lọc khoảng trên cột đó.",
"Thiết kế chỉ mục phủ cho ba truy vấn và chứng minh bước tra cứu thứ hai biến mất, bằng kế hoạch thực thi và số đo.",
"Tầng *áp dụng*. Objective có tiêu chí đọc được từ kế hoạch. Đạt khi cả ba truy vấn chuyển sang dùng chỉ mục phủ, xác nhận bằng dấu hiệu trong kế hoạch, và khi thời gian giảm đo được. Thiết kế đúng mà kế hoạch không cho thấy phủ thì chưa đạt.",
"Bảng 20 triệu dòng. Ba truy vấn ban đầu dùng chỉ mục phụ có tra cứu hai bước. Thiết kế chỉ mục phủ cho từng cái. Đọc kế hoạch xác nhận. Đo thời gian trước sau. Thử đảo thứ tự cột trong một chỉ mục phức hợp có lọc khoảng và quan sát nó hỏng.",
"Thêm cột vào chỉ mục cho phủ mà không đo chi phí ghi · đặt cột lọc khoảng trước cột lọc bằng · tạo chỉ mục tiền tố quá ngắn nên chọn lọc kém.",
"Cả ba truy vấn dùng chỉ mục phủ xác nhận bằng kế hoạch, và thời gian giảm đo được."),

(138,"Buffer pool, redo and undo","TH","Lesson 137",
"Bộ đệm của InnoDB theo mô hình ở lesson 110 nhưng có danh sách hai vùng mới và cũ để chống ô nhiễm bởi quét toàn bảng, một cơ chế PostgreSQL xử lý khác. Tỉ lệ trúng và cách đọc. Nhật ký làm lại có kích thước cố định và ghi vòng, khác PostgreSQL ghi theo tệp mới; hệ quả: nhật ký làm lại quá nhỏ gây điểm kiểm tra liên tục và chặn ghi, một nút cổ chai phổ biến và dễ sửa. Nhật ký hoàn tác giữ phiên bản cũ cho đọc nhất quán, và nó phình khi có giao dịch mở lâu, cùng nguyên nhân với lesson 116 nhưng biểu hiện ở chỗ khác. Bộ đệm thay đổi hoãn cập nhật chỉ mục phụ cho trang chưa nằm trong bộ đệm, một tối ưu ghi không có tương đương trực tiếp ở PostgreSQL. Xả bộ đệm và tham số điều khiển tốc độ. Thời điểm đồng bộ nhật ký khi xác nhận và ba mức đánh đổi giữa bền vững với thông lượng, nối lại lesson 16.",
"Tìm nút cổ chai ghi bằng cách chỉnh kích thước nhật ký làm lại và mức đồng bộ, và định lượng đánh đổi giữa bền vững với thông lượng.",
"Tầng *đánh giá*. Objective đòi chọn một mức bền vững có hệ quả nghiệp vụ. Đạt khi có bảng ba mức đồng bộ kèm thông lượng và lượng dữ liệu mất khi ngắt điện đo thật, và khi lựa chọn cuối dẫn được về yêu cầu điểm phục hồi ở lesson 119.",
"Chạy tải ghi nặng với nhật ký làm lại nhỏ, quan sát chặn ghi. Tăng dần và đo thông lượng. Chạy ba mức đồng bộ, mỗi mức ngắt điện máy ảo và đếm giao dịch mất. Mở một giao dịch dài và đo nhật ký hoàn tác phình.",
"Để nhật ký làm lại ở kích thước mặc định cho tải ghi nặng · hạ mức đồng bộ để nhanh mà không tính lượng dữ liệu mất · bỏ qua nhật ký hoàn tác phình vì bảng không phình.",
"Bảng ba mức đồng bộ có thông lượng và số giao dịch mất đo thật, và lựa chọn dẫn được về yêu cầu điểm phục hồi."),

(139,"Locking, isolation and deadlocks in InnoDB","TH","Lesson 138",
"Mức cô lập mặc định của MySQL là đọc lặp lại, khác mặc định đọc đã xác nhận của PostgreSQL, và giả định sai về điều này là nguồn lỗi khi chuyển hệ. Khoá hàng đặt trên bản ghi chỉ mục chứ không trên dòng dữ liệu, nên một cập nhật không dùng chỉ mục sẽ khoá mọi hàng nó quét qua, kể cả hàng không thoả điều kiện; đây là khác biệt vận hành lớn và là nguyên nhân phổ biến của tranh chấp bất ngờ. Khoá khoảng và khoá kề chặn chèn vào khoảng để ngăn đọc ảo ở mức đọc lặp lại, và chúng gây bế tắc theo cách không có ở PostgreSQL. Đọc nhất quán không khoá so với đọc có khoá tường minh. Phát hiện bế tắc và chọn nạn nhân theo mô hình ở lesson 117. Đọc nhật ký bế tắc của InnoDB để biết hai giao dịch giữ khoá nào trên chỉ mục nào. Thời gian chờ khoá và phân biệt hết thời gian chờ với bế tắc, hai lỗi khác nhau.",
"Tái hiện một bế tắc do khoá khoảng gây ra, đọc nhật ký để xác định chỉ mục và khoảng bị khoá, và chứng minh cập nhật không dùng chỉ mục khoá thừa hàng.",
"Tầng *phân tích*. Objective đòi chẩn đoán một cơ chế khoá riêng của InnoDB. Đạt khi xác định đúng chỉ mục và khoảng từ nhật ký bế tắc, và khi đếm được số hàng bị khoá bởi một cập nhật không dùng chỉ mục lớn hơn số hàng thoả điều kiện.",
"Dựng kịch bản bế tắc do khoá khoảng ở mức đọc lặp lại. Đọc nhật ký bế tắc, xác định chỉ mục và khoảng. Chạy một cập nhật lọc trên cột không có chỉ mục, đếm số hàng bị khoá qua khung nhìn hệ thống, so với số hàng thoả điều kiện. Thêm chỉ mục và đo lại.",
"Giả định mặc định là đọc đã xác nhận như PostgreSQL · cập nhật lọc trên cột không có chỉ mục trên bảng lớn · nhầm hết thời gian chờ khoá với bế tắc.",
"Xác định đúng chỉ mục và khoảng từ nhật ký, và số hàng bị khoá lớn hơn số hàng thoả điều kiện đo được."),

(140,"The binary log - replication and change capture","TH","Lesson 139",
"Nhật ký nhị phân ghi thay đổi ở mức logic và tách biệt với nhật ký làm lại ở mức vật lý, khác PostgreSQL dùng chung một nhật ký cho cả hai mục đích. Ba định dạng và khác biệt thực tế: theo câu lệnh gọn nhưng không tất định với hàm phụ thuộc ngữ cảnh, theo hàng an toàn nhưng tốn dung lượng, và hỗn hợp tự chọn. Định dạng theo hàng là điều kiện bắt buộc cho bắt thay đổi dữ liệu đáng tin, nên đây là bài đặt nền cho chặng 6. Ảnh trước và ảnh sau của một hàng trong sự kiện cập nhật, và vì sao có cả hai mới dựng lại được trạng thái. Định danh giao dịch toàn cục giúp chuyển đổi dự phòng không mất dấu vị trí. Thời gian giữ nhật ký nhị phân và hệ quả khi bản sao hoặc công cụ bắt thay đổi tụt quá xa: mất nhật ký thì phải nạp lại toàn bộ. Đọc nhật ký nhị phân bằng công cụ để xem sự kiện thô.",
"Cấu hình nhật ký nhị phân ở định dạng theo hàng, đọc sự kiện thô của một cập nhật, và chỉ ra ảnh trước cùng ảnh sau.",
"Tầng *áp dụng*. Objective có sản phẩm kiểm được trực tiếp. Đạt khi đọc được sự kiện thô và chỉ đúng ảnh trước ảnh sau cho ba loại thao tác, và khi chứng minh được định dạng theo câu lệnh cho kết quả khác trên một câu lệnh không tất định.",
"Bật nhật ký nhị phân theo hàng. Chạy chèn, cập nhật, xoá. Đọc sự kiện thô, chỉ ảnh trước và sau. Đổi sang định dạng theo câu lệnh, chạy một câu lệnh dùng hàm thời gian hiện tại, áp lên bản sao và so kết quả. Đặt thời gian giữ nhật ký ngắn rồi để bản sao tụt lại, quan sát hậu quả.",
"Dùng định dạng theo câu lệnh cho bắt thay đổi dữ liệu · đặt thời gian giữ nhật ký nhị phân quá ngắn · giả định nhật ký nhị phân giống nhật ký làm lại.",
"Chỉ đúng ảnh trước và sau cho ba loại thao tác, và chứng minh được định dạng theo câu lệnh cho kết quả khác."),

(141,"Replication, replica lag and failover","TH","Lesson 140",
"Bản sao của MySQL là bản sao logic dựa trên nhật ký nhị phân ở lesson 140, khác bản sao vật lý mặc định của PostgreSQL. Hai luồng trên bản sao: một luồng nhận sự kiện về nhật ký chuyển tiếp, một luồng áp sự kiện, và độ trễ có thể nằm ở luồng nào trong hai luồng đó, nên đo phải phân biệt hai chỉ số. Áp song song nhiều luồng và điều kiện an toàn để giữ thứ tự. Bản sao bán đồng bộ và cửa sổ mất dữ liệu còn lại. Độ trễ đo theo giây so với đo theo vị trí nhật ký, hai con số nói hai chuyện và con số theo giây gây hiểu nhầm khi bản chính rỗi. Bản sao phân kỳ do ghi trực tiếp vào bản sao, và vì sao phải đặt bản sao ở chế độ chỉ đọc. Chuyển đổi dự phòng và định danh giao dịch toàn cục. Dựng lại bản sao sau phân kỳ bằng nạp lại hoặc bằng công cụ đồng bộ, và chi phí của từng cách.",
"Đo độ trễ bản sao phân biệt hai luồng, và tái hiện một trường hợp độ trễ theo giây bằng không trong khi bản sao vẫn tụt lại.",
"Tầng *phân tích*. Objective đòi thấy được giới hạn của một chỉ số hay dùng. Đạt khi đo được hai chỉ số riêng cho hai luồng, và khi tái hiện được ca độ trễ theo giây bằng không nhưng vị trí nhật ký chênh lệch, giải thích được nguyên nhân.",
"Dựng bản chính và bản sao. Chạy tải ghi nặng, đo độ trễ theo cả hai cách và tách hai luồng. Dừng luồng áp, quan sát hai chỉ số phân kỳ. Cho bản chính rỗi trong lúc bản sao còn tồn đọng, quan sát độ trễ theo giây về không. Bật áp song song và đo lại.",
"Chỉ theo dõi độ trễ theo giây · để bản sao cho phép ghi · bật áp song song mà không kiểm điều kiện giữ thứ tự.",
"Đo được hai chỉ số riêng cho hai luồng, và tái hiện được ca độ trễ theo giây bằng không mà vị trí vẫn chênh."),

(142,"EXPLAIN in MySQL and where it differs","TH","Lesson 141",
"Cột trong kết quả giải thích kế hoạch của MySQL và ý nghĩa vận hành của từng cột, đặc biệt kiểu truy cập, chỉ mục khả dụng so với chỉ mục được chọn, số dòng ước lượng, tỉ lệ lọc, và phần thông tin thêm. Tỉ lệ lọc là con số hay bị bỏ qua nhất: số dòng ước lượng nhân tỉ lệ lọc mới ra số dòng thật sự đi lên trên. Ba chuỗi trong phần thông tin thêm cần nhận ra ngay: dùng bảng tạm, dùng sắp xếp riêng, và dùng chỉ mục thuần. Chế độ phân tích thật có từ các phiên bản gần đây và cho số dòng thật cùng thời gian, tương tự lesson 129, nhưng phải kiểm phiên bản đang chạy chứ không giả định có. Bộ tối ưu hoá MySQL đơn giản hơn của PostgreSQL ở một số phép viết lại, nên cách viết truy vấn ảnh hưởng nhiều hơn. Gợi ý chỉ mục và gợi ý bộ tối ưu hoá, cùng nguyên tắc chỉ dùng khi đã hiểu nguyên nhân, nối lại lesson 128.",
"Đọc một kế hoạch MySQL và tính số dòng thật sự đi lên trên từ số dòng ước lượng nhân tỉ lệ lọc, rồi đối chiếu với số đo.",
"Tầng *phân tích*. Objective nhắm vào con số hay bị bỏ qua nhất trong kế hoạch MySQL. Đạt khi tính đúng số dòng cho bốn truy vấn với sai số dưới 30% so với số thật, và khi nhận ra đúng ba chuỗi cảnh báo trong phần thông tin thêm khi chúng xuất hiện.",
"Chạy sáu truy vấn, đọc kế hoạch. Với mỗi cái tính số dòng ước lượng nhân tỉ lệ lọc, so với số dòng thật từ chế độ phân tích. Tìm ba truy vấn có bảng tạm, sắp xếp riêng, và chỉ mục thuần. Kiểm phiên bản MySQL đang chạy có chế độ phân tích thật không.",
"Đọc số dòng ước lượng mà bỏ tỉ lệ lọc · thêm gợi ý chỉ mục để ép kế hoạch thay vì sửa nguyên nhân · giả định phiên bản đang chạy có mọi tính năng mới.",
"Tính đúng số dòng cho bốn truy vấn sai số dưới 30%, và nhận ra đúng ba chuỗi cảnh báo."),

(143,"MySQL against PostgreSQL - a measured comparison","TH","Lesson 142",
"Không có cơ chế mới. Bài gộp module: chạy cùng một use case trên hai hệ và lập báo cáo so sánh có số. Sáu trục đo, mỗi trục gắn với một bài đã học: thiết kế chỉ mục phức hợp và chỉ mục phủ từ lesson 137, hành vi khoá và bế tắc từ lesson 139, chi phí ghi theo mức bền vững từ lesson 138, cơ chế bắt thay đổi từ lesson 140, độ trễ bản sao từ lesson 141, và khôi phục từ lesson 119. Nguyên tắc so sánh: cùng phần cứng, cùng dữ liệu, cùng truy vấn, và mỗi ô trong bảng phải dẫn một số đo chứ không dẫn một khẳng định. Chỗ hai hệ gần như không khác và không đáng tốn thời gian so. Kết luận phải phát biểu theo tải chứ không theo hệ: nói hệ nào hợp tải nào, không nói hệ nào tốt hơn. Báo cáo này là một trong bảy đầu vào của bài bảo vệ ở M18.",
"Lập báo cáo so sánh sáu trục giữa MySQL và PostgreSQL trên cùng use case, mỗi ô dẫn một số đo từ lab của mình.",
"Tầng *đánh giá*. Objective đòi so sánh có bằng chứng và kết luận theo tải. Kiểm bằng rà soát chéo: một học viên khác phải truy được mỗi ô về một số đo cụ thể. Đạt khi ít nhất 10 trên 12 ô đứng vững sau rà soát, và khi kết luận phát biểu theo tải chứ không xếp hạng hai hệ.",
"Chạy cùng use case đơn hàng 20 triệu dòng trên hai hệ, cùng phần cứng. Đo sáu trục. Lập bảng sáu nhân hai. Đổi báo cáo chéo và rà soát từng ô. Viết kết luận nêu hai tải cụ thể và hệ nào hợp hơn cho từng tải, kèm lý do từ số đo.",
"So sánh trên phần cứng khác nhau · kết luận hệ nào tốt hơn nói chung · để trống ô rồi ghi tương đương mà chưa đo.",
"Ít nhất 10 trên 12 ô đứng vững sau rà soát chéo, và kết luận phát biểu theo tải kèm lý do từ số đo."),
]

M13 = ("MongoDB", 144, 151, """| | |
|---|---|
| **Objective cấp module** | Mô hình hoá một miền nghiệp vụ bằng tài liệu, và chỉ ra ba tình huống mô hình tài liệu thắng mô hình quan hệ cùng ba tình huống ngược lại, có số đo |
| **Tiền đề** | M11 |
| **Exit criterion** | Mô hình đơn hàng chạy được, đo được chênh lệch có và không có chỉ mục, xử lý được một lần chuyển đổi dự phòng và một thay đổi lược đồ |
| **Kỹ năng SFIA** | `DBAD` mức 3 · `DTAN` mức 3 |
| **Chế độ hỏng** | Nhúng mọi thứ vào một tài liệu vì thấy tiện, rồi tài liệu lớn dần vượt giới hạn và mọi cập nhật phải ghi lại cả tài liệu |""",
"Mức `B`. Module bám một câu hỏi thiết kế duy nhất là nhúng hay tham chiếu, vì phần lớn thành bại của một lược đồ tài liệu nằm ở đó. Sáu bài giữa là truy vấn, tổng hợp và vận hành; hai bài cuối là phân mảnh và giới hạn vận hành.")

L13 = [
(144,"The document model - embedding against referencing","LT","Module 13: M11",
"Tài liệu là một bản ghi tự mô tả có cấu trúc lồng, và bộ sưu tập không bắt buộc mọi tài liệu cùng hình dạng. Lược đồ linh hoạt không có nghĩa không có lược đồ: nó chỉ chuyển việc thực thi lược đồ từ lúc ghi sang lúc đọc, và ứng dụng vẫn phải giả định một hình dạng. Nhúng đặt dữ liệu liên quan trong cùng tài liệu: một lần đọc lấy đủ, không có phép kết, nhưng tài liệu lớn dần và mọi cập nhật ghi lại phần lớn tài liệu. Tham chiếu đặt ở tài liệu riêng: cập nhật độc lập, nhưng cần nhiều lần đọc hoặc một phép kết ở tầng tổng hợp. Ba tiêu chí quyết định: quan hệ chứa hay quan hệ liên kết, tỉ lệ đọc trên ghi, và bản số quan hệ có chặn trên hay không. Bản số không chặn trên là dấu hiệu rõ nhất phải tham chiếu, vì tài liệu sẽ lớn không giới hạn. Giới hạn kích thước tài liệu và giới hạn độ sâu lồng. Giao dịch nhiều tài liệu có nhưng đắt hơn và không nên là mặc định.",
"Chọn nhúng hay tham chiếu cho sáu quan hệ trong một miền nghiệp vụ, và biện minh bằng ba tiêu chí chứ không bằng cảm nhận.",
"Tầng *đánh giá*. Objective đòi quyết định thiết kế có đánh đổi, không có đáp án chung. Kiểm bằng rà soát chéo sáu quyết định; đạt khi ít nhất năm quyết định nêu được cả ba tiêu chí và nêu được hậu quả của lựa chọn ngược lại.",
"Nhận miền nghiệp vụ thương mại điện tử có sáu quan hệ: đơn và dòng hàng, đơn và khách, khách và địa chỉ, sản phẩm và đánh giá, sản phẩm và danh mục, đơn và lịch sử trạng thái. Quyết định từng cái theo ba tiêu chí. Ước lượng kích thước tài liệu sau một năm cho mỗi lựa chọn nhúng.",
"Nhúng quan hệ có bản số không chặn trên · tham chiếu mọi thứ vì quen mô hình quan hệ · dùng giao dịch nhiều tài liệu làm mặc định.",
"Ít nhất năm trên sáu quyết định nêu đủ ba tiêu chí và hậu quả của lựa chọn ngược lại."),

(145,"Modelling an order domain as documents","TH","Lesson 144",
"Chuyển quyết định ở lesson 144 thành lược đồ chạy được. Quy ước đặt tên trường và vì sao tên trường lưu trong mọi tài liệu nên tên dài tốn dung lượng thật ở quy mô lớn. Kiểu dữ liệu của MongoDB và ba chỗ hay sai: số thập phân cho tiền chứ không dùng số thực nhị phân, nối lại lesson 7; ngày giờ lưu theo chuẩn có múi giờ, nối lại lesson 9; và định danh tài liệu có thể dùng khoá nghiệp vụ thay cho định danh tự sinh khi khoá nghiệp vụ ổn định. Xác thực lược đồ ở tầng cơ sở dữ liệu để chặn tài liệu sai hình dạng, biến lược đồ ngầm thành lược đồ khai báo. Mẫu nhúng một phần: giữ vài trường thường đọc của tài liệu tham chiếu để tránh lần đọc thứ hai, đổi lấy việc phải cập nhật hai chỗ. Mẫu nhóm theo thời gian cho dữ liệu chuỗi thời gian. Ước lượng dung lượng từ lược đồ và số tài liệu.",
"Cài đặt lược đồ tài liệu cho miền đơn hàng có xác thực ở tầng cơ sở dữ liệu, và chứng minh nó chặn được bốn loại tài liệu sai hình dạng.",
"Tầng *áp dụng*. Objective có tiêu chí kiểm bằng chạy thật. Đạt khi bốn tài liệu sai đều bị từ chối bởi luật xác thực tương ứng, và khi ba lựa chọn kiểu dữ liệu nhạy cảm được biện minh bằng bài học ở chặng 1.",
"Cài lược đồ cho miền ở lesson 144. Thêm luật xác thực. Thử chèn bốn tài liệu sai: thiếu trường bắt buộc, tiền dạng số thực, ngày không có múi giờ, và mảng vượt giới hạn phần tử. Nạp 5 triệu tài liệu và đo dung lượng thật so với ước lượng.",
"Dùng số thực nhị phân cho tiền · bỏ xác thực lược đồ vì đã có kiểm tra ở ứng dụng · đặt tên trường dài trong bộ sưu tập hàng trăm triệu tài liệu.",
"Bốn tài liệu sai đều bị đúng luật xác thực từ chối, và ba lựa chọn kiểu nhạy cảm có lý do."),

(146,"Indexes and the query planner","TH","Lesson 145",
"Chỉ mục một trường, chỉ mục phức hợp, và quy tắc tiền tố tương tự lesson 111. Chỉ mục trên trường trong mảng sinh một mục cho mỗi phần tử, nên một tài liệu có mảng 1.000 phần tử tạo 1.000 mục chỉ mục, và chỉ được một chỉ mục loại này trong một chỉ mục phức hợp. Chỉ mục một phần và chỉ mục thưa, cùng khác biệt giữa hai loại. Chỉ mục văn bản và chỉ mục không gian ở mức biết có. Bộ lập kế hoạch chạy thử nhiều kế hoạch ứng viên trên một phần dữ liệu rồi chọn cái tốt nhất và lưu vào bộ đệm kế hoạch, khác cách tiếp cận dựa trên chi phí của PostgreSQL ở lesson 128; hệ quả là kế hoạch trong bộ đệm có thể không còn tốt khi dữ liệu đổi, và có cơ chế đánh giá lại. Đọc kế hoạch và ba chỉ số quan trọng: số tài liệu khảo sát, số mục chỉ mục khảo sát, và số tài liệu trả về. Tỉ lệ giữa số khảo sát và số trả về là thước đo hiệu quả chỉ mục.",
"Thiết kế chỉ mục cho năm mẫu truy vấn và chứng minh hiệu quả bằng tỉ lệ số tài liệu khảo sát trên số tài liệu trả về.",
"Tầng *áp dụng*. Objective có một thước đo cụ thể thay cho thời gian chạy. Đạt khi năm truy vấn đều đạt tỉ lệ khảo sát trên trả về dưới 2, và khi người học chỉ ra được một truy vấn mà chỉ mục trên mảng làm kích thước chỉ mục tăng vọt.",
"Bộ sưu tập 10 triệu tài liệu có mảng dòng hàng. Chạy năm truy vấn không chỉ mục, ghi ba chỉ số. Thiết kế chỉ mục, chạy lại, tính tỉ lệ. Tạo chỉ mục trên trường trong mảng và đo kích thước chỉ mục. Thử tạo chỉ mục phức hợp có hai trường mảng và quan sát lỗi.",
"Đánh giá chỉ mục bằng thời gian thay vì bằng tỉ lệ khảo sát · tạo chỉ mục trên mảng lớn mà không đo dung lượng · tin bộ đệm kế hoạch luôn giữ kế hoạch tốt nhất.",
"Năm truy vấn đều đạt tỉ lệ khảo sát trên trả về dưới 2, và ca chỉ mục mảng tăng vọt dung lượng được chỉ ra."),

(147,"The aggregation pipeline","TH","Lesson 146",
"Đường ống tổng hợp là chuỗi giai đoạn, mỗi giai đoạn nhận luồng tài liệu và phát ra luồng tài liệu, mô hình giống chuỗi ống dẫn ở lesson 20 và chuỗi hàm sinh ở lesson 64. Các giai đoạn thường dùng và thứ tự đặt chúng quyết định hiệu năng: đặt giai đoạn lọc và giới hạn sớm nhất có thể để giảm tài liệu đi xuống, đây chính là đẩy vị từ xuống ở lesson 115. Chỉ giai đoạn lọc và sắp xếp ở đầu đường ống mới dùng được chỉ mục, sau đó thì không, nên vị trí của chúng là ràng buộc cứng chứ không phải gợi ý. Giai đoạn tra cứu thực hiện phép kết trái và chi phí của nó, cùng lý do nó không thay thế được việc thiết kế lược đồ đúng ở lesson 144. Giai đoạn bung mảng và hiện tượng nhân dòng, cùng bản chất với lesson 100. Giới hạn bộ nhớ mỗi giai đoạn và tuỳ chọn cho phép tràn ra đĩa. Giai đoạn ghi kết quả ra bộ sưu tập, dùng cho khung nhìn vật chất hoá.",
"Viết một đường ống tổng hợp cho năm câu hỏi nghiệp vụ, và tối ưu bằng cách đặt lại thứ tự giai đoạn, chứng minh bằng số tài liệu khảo sát.",
"Tầng *áp dụng*. Objective gồm một sản phẩm và một phép tối ưu có bằng chứng. Đạt khi năm câu trả lời khớp đáp án đối chứng tính bằng SQL trên cùng dữ liệu, và khi ít nhất hai đường ống giảm số tài liệu khảo sát rõ rệt sau khi đặt lại thứ tự giai đoạn.",
"Trả lời năm câu hỏi nghiệp vụ bằng đường ống tổng hợp trên 10 triệu tài liệu. Đối chiếu với đáp án tính bằng SQL trên cùng dữ liệu nạp vào PostgreSQL. Với hai đường ống, đặt giai đoạn lọc ở cuối rồi chuyển lên đầu, đo số tài liệu khảo sát hai lần. Chạy một đường ống vượt giới hạn bộ nhớ.",
"Đặt giai đoạn lọc sau giai đoạn tra cứu · dùng giai đoạn bung mảng mà không kiểm nhân dòng · tin rằng mọi giai đoạn đều dùng được chỉ mục.",
"Năm câu trả lời khớp đáp án SQL, và hai đường ống giảm số tài liệu khảo sát sau khi đặt lại thứ tự."),

(148,"Write concern, read concern and what they cost","TH","Lesson 147",
"Mức bảo đảm ghi quy định bao nhiêu nút phải xác nhận trước khi lệnh ghi trả về, và nó là chỗ người dùng chọn vị trí của mình trên trục giữa bền vững và độ trễ. Ba mức thường dùng và cửa sổ mất dữ liệu của từng mức. Tuỳ chọn ghi nhật ký kết hợp với số nút xác nhận tạo ra ma trận lựa chọn, và mặc định không phải mức an toàn nhất. Mức bảo đảm đọc quy định đọc thấy dữ liệu ở mức cam kết nào, và đọc từ nút phụ có thể thấy dữ liệu sau đó bị quay lui nếu mức bảo đảm đọc thấp. Đọc sau ghi trong MongoDB và cách phiên nhân quả giải quyết nó, so với ba cách ở lesson 120. Quay lui khi nút chính cũ sống lại với dữ liệu chưa nhân bản: cơ chế, tệp quay lui, và vì sao mức bảo đảm ghi thấp làm việc này xảy ra. Đo chi phí thật của từng mức trên tải của mình thay vì đọc khuyến nghị.",
"Đo độ trễ ghi ở ba mức bảo đảm và định lượng cửa sổ mất dữ liệu của từng mức bằng thực nghiệm giết nút chính.",
"Tầng *đánh giá*. Objective đòi chọn một mức có hệ quả nghiệp vụ, kèm số đo hai chiều. Đạt khi có bảng ba mức kèm cả độ trễ phân vị 95 lẫn số bản ghi mất khi giết nút chính, và khi lựa chọn cuối dẫn được về yêu cầu điểm phục hồi ở lesson 119.",
"Dựng tập bản sao ba nút. Chạy tải ghi ở ba mức bảo đảm, đo độ trễ phân vị 95. Với mỗi mức, giết nút chính giữa chừng và đếm số bản ghi mất sau khi bầu lại. Đọc tệp quay lui. Tái hiện đọc sau ghi trên nút phụ rồi sửa bằng phiên nhân quả.",
"Để mức bảo đảm ghi mặc định cho dữ liệu giao dịch · đọc từ nút phụ mà không xét mức bảo đảm đọc · bỏ qua tệp quay lui sau chuyển đổi dự phòng.",
"Bảng ba mức có độ trễ và số bản ghi mất đo thật, và lựa chọn dẫn được về yêu cầu điểm phục hồi."),

(149,"Replica sets and failover","TH","Lesson 148",
"Tập bản sao gồm một nút chính nhận ghi và các nút phụ nhân bản từ nhật ký thao tác. Nhật ký thao tác là bộ đệm vòng có kích thước cố định, nên nút phụ tụt quá xa sẽ không đuổi kịp và phải nạp lại toàn bộ, cùng vấn đề với lesson 140. Bầu chọn nút chính mới: điều kiện đa số, thời gian phát hiện, và vì sao cụm hai nút không chịu được mất một nút. Nút trọng tài và cảnh báo khi dùng nó thay cho nút dữ liệu thứ ba. Độ ưu tiên thành viên để điều khiển nút nào được làm chính. Nút ẩn và nút trễ có chủ đích, dùng để chống lỗi người vận hành xoá nhầm dữ liệu. Tuỳ chọn đọc từ nút nào và hệ quả về tính nhất quán, nối lại lesson 148. Theo dõi độ trễ nhân bản và kích thước nhật ký thao tác như hai chỉ số vận hành bắt buộc. Chuyển đổi dự phòng có kiểm soát để bảo trì, khác chuyển đổi do sự cố.",
"Thực hiện chuyển đổi dự phòng có kiểm soát và chuyển đổi do sự cố, đo thời gian gián đoạn ghi của từng loại.",
"Tầng *áp dụng*. Objective có tiêu chí đo được trực tiếp. Đạt khi đo được thời gian gián đoạn ghi cho cả hai loại chuyển đổi, và khi chứng minh được cụm hai nút không bầu được nút chính mới khi mất một nút còn cụm ba nút thì được.",
"Dựng tập bản sao ba nút với tải ghi liên tục. Chuyển đổi có kiểm soát, đo gián đoạn. Giết nút chính, đo gián đoạn. Hạ xuống hai nút, giết một, quan sát cụm không bầu được. Tính kích thước nhật ký thao tác đủ cho bao nhiêu giờ tải hiện tại.",
"Dùng cụm hai nút cộng trọng tài cho dữ liệu quan trọng · để nhật ký thao tác kích thước mặc định cho tải ghi nặng · không đo thời gian gián đoạn trước khi cam kết mức dịch vụ.",
"Đo được gián đoạn ghi cho cả hai loại chuyển đổi, và chứng minh được khác biệt giữa cụm hai nút và ba nút."),

(150,"Sharding - shard keys and the choices you cannot undo","LT","Lesson 149",
"Phân mảnh chia dữ liệu ngang qua nhiều cụm theo một khoá, và khoá phân mảnh là quyết định khó đảo ngược nhất trong MongoDB. Ba tính chất của một khoá tốt: bản số đủ lớn, phân bố đều, và khớp mẫu truy vấn thường gặp. Khoá tăng đơn điệu như dấu thời gian làm mọi lệnh ghi dồn vào một mảnh, cùng vấn đề với lesson 136 nhưng ở quy mô cụm. Phân mảnh theo khoảng giữ được quét khoảng rẻ nhưng dễ lệch; phân mảnh theo băm phân bố đều nhưng mất quét khoảng, nối lại lesson 48. Khoá phức hợp để cân hai tính chất. Truy vấn không chứa khoá phân mảnh phải hỏi mọi mảnh rồi gộp, nên chi phí tỉ lệ số mảnh chứ không giảm theo. Cân bằng lại và chi phí di chuyển đoạn dữ liệu trong lúc phục vụ. Khi nào chưa cần phân mảnh: phần lớn tải vừa một cụm bản sao, và phân mảnh sớm thêm phức tạp mà không thêm năng lực.",
"Đánh giá bốn khoá phân mảnh ứng viên theo ba tính chất, và chỉ ra tình huống một khoá tốt cho ghi lại tồi cho đọc.",
"Tầng *đánh giá*. Objective đòi chọn dưới đánh đổi và nhận ra xung đột giữa hai mục tiêu. Đạt khi bốn ứng viên được chấm theo cả ba tính chất, khi chỉ ra đúng khoá tăng đơn điệu gây dồn ghi, và khi nêu được một khoá tốt cho ghi nhưng làm truy vấn thường gặp phải hỏi mọi mảnh.",
"Nhận bốn khoá ứng viên cho bộ sưu tập đơn hàng: dấu thời gian, định danh khách băm, định danh khách cộng dấu thời gian, và định danh đơn tự sinh. Chấm theo ba tính chất. Với ba truy vấn thường gặp, xác định truy vấn nào phải hỏi mọi mảnh ứng với từng khoá. Lập bảng bốn nhân ba.",
"Chọn dấu thời gian làm khoá phân mảnh · phân mảnh khi dữ liệu còn vừa một cụm bản sao · chọn khoá tối ưu cho ghi mà không xét mẫu đọc.",
"Bốn ứng viên chấm đủ ba tính chất, và bảng bốn nhân ba chỉ đúng truy vấn nào phải hỏi mọi mảnh."),

(151,"Document growth, schema change and operational limits","TH","Lesson 150",
"Tài liệu lớn dần là chế độ hỏng đặc trưng của mô hình nhúng, và nó có ba hậu quả cùng lúc: chạm giới hạn kích thước, mỗi cập nhật ghi lại phần lớn tài liệu, và dịch chuyển tài liệu khi không còn vừa chỗ cũ. Đo phân bố kích thước tài liệu theo thời gian như một chỉ số cảnh báo sớm. Mẫu ngoài dòng khi một mảng nhúng vượt ngưỡng: chuyển sang tham chiếu và giữ một phần nhúng, nối lại lesson 145. Thay đổi lược đồ trên bộ sưu tập lớn: ba chiến lược là chuyển đổi lúc đọc, chuyển đổi nền theo lô, và giữ trường phiên bản trong tài liệu để ứng dụng xử lý nhiều hình dạng cùng lúc. Chiến lược thứ ba là mẫu thực dụng nhất và ít bị nhắc tới nhất. Giới hạn vận hành cần biết trước khi thiết kế: kích thước tài liệu, độ sâu lồng, số bộ sưu tập, và giới hạn của giai đoạn tổng hợp. Cập nhật tại chỗ trên một phần tử mảng thay vì ghi lại cả mảng.",
"Phát hiện một bộ sưu tập có tài liệu lớn dần bằng phân bố kích thước, và chuyển mảng nhúng sang tham chiếu mà không ngừng phục vụ.",
"Tầng *áp dụng*. Objective có hai tiêu chí kiểm được. Đạt khi phân bố kích thước cho thấy xu hướng tăng và nêu được thời điểm ước tính chạm giới hạn, và khi chuyển đổi hoàn tất với tải đọc ghi chạy suốt không lỗi, dùng trường phiên bản để xử lý hai hình dạng cùng lúc.",
"Bộ sưu tập 5 triệu tài liệu có mảng lịch sử trạng thái tăng dần. Đo phân bố kích thước ở ba mốc, ngoại suy thời điểm chạm giới hạn. Chuyển mảng sang bộ sưu tập riêng theo ba bước, dùng trường phiên bản, giữ tải chạy suốt. Đo thời gian cập nhật một phần tử trước và sau.",
"Nhúng mảng không chặn trên rồi chờ tới khi lỗi · chuyển đổi lược đồ bằng một lần cập nhật hàng loạt trên bộ sưu tập lớn · ghi lại cả mảng khi chỉ đổi một phần tử.",
"Phân bố kích thước cho thấy xu hướng và thời điểm chạm giới hạn, và chuyển đổi xong với tải chạy suốt không lỗi."),
]

M14 = ("Redis", 152, 158, """| | |
|---|---|
| **Objective cấp module** | Thiết kế một lớp đệm có ngưỡng đo được, và trả lời được câu hỏi khi nào nên bỏ lớp đệm đó đi |
| **Tiền đề** | M11 |
| **Exit criterion** | Lớp đệm có tỉ lệ trúng đo được, chịu được ồ ạt nạp lại, và có phương án khi mất sạch dữ liệu đệm |
| **Kỹ năng SFIA** | `DBAD` mức 3 · `SYSP` mức 3 |
| **Chế độ hỏng** | Dùng Redis làm nguồn dữ liệu bền vững mà chưa thiết kế độ bền, rồi mất dữ liệu khi khởi động lại |""",
"Mức `B`. Redis khác sáu hệ còn lại ở chỗ nó không phải nơi lưu dữ liệu gốc trong phần lớn kiến trúc, nên câu hỏi trung tâm của module không phải dùng thế nào mà là khi nào nên có và khi nào nên bỏ. Bài cuối đo hiệu quả lớp đệm và nêu điều kiện gỡ bỏ.")

L14 = [
(152,"In-memory data structures and what each one is for","TH","Module 14: M11",
"Năm cấu trúc chính và bài toán mỗi cấu trúc giải, nối lại lesson 63 nhưng ở tầng dịch vụ mạng. Chuỗi cho giá trị đơn và bộ đếm nguyên tử. Băm cho đối tượng nhiều trường, cho phép đọc ghi một trường mà không tải cả đối tượng. Danh sách cho hàng đợi đơn giản, cùng cảnh báo rằng nó không phải hệ thống hàng đợi thật vì thiếu xác nhận và thử lại, nối tới chặng 6. Tập cho kiểm tra thành viên và phép toán tập hợp. Tập có điểm cho bảng xếp hạng và cho hàng đợi ưu tiên theo thời gian. Chi phí thời gian của từng lệnh và vì sao phải tra trước khi dùng: một số lệnh là tuyến tính theo kích thước cấu trúc và chúng chặn cả máy chủ vì mô hình một luồng. Quy ước đặt tên khoá và vì sao thiết kế không gian khoá quan trọng: khoá là giao diện duy nhất, không có lược đồ và không có chỉ mục.",
"Chọn cấu trúc cho năm bài toán đệm và chứng minh lựa chọn bằng số đo bộ nhớ và độ trễ.",
"Tầng *đánh giá*. Objective đòi chọn có đánh đổi hai chiều. Đạt khi năm lựa chọn đều có số đo bộ nhớ và độ trễ phân vị 95, và khi ít nhất một lựa chọn tránh được một lệnh có chi phí tuyến tính, nêu rõ lệnh nào bị tránh và vì sao.",
"Năm bài toán: đệm đối tượng khách, bộ đếm lượt xem, danh sách sản phẩm vừa xem, kiểm tra một khoá có trong tập cấm không, và bảng xếp hạng bán chạy. Cài mỗi bài bằng ít nhất hai cấu trúc. Đo bộ nhớ và độ trễ. Chạy một lệnh tuyến tính trên cấu trúc một triệu phần tử và đo thời gian chặn.",
"Dùng chuỗi lưu JSON rồi phải tải cả đối tượng để đọc một trường · chạy lệnh liệt kê toàn bộ khoá trên máy chủ sản xuất · dùng danh sách làm hàng đợi công việc thật.",
"Năm lựa chọn đều có số đo bộ nhớ và độ trễ, và ít nhất một lựa chọn tránh được một lệnh tuyến tính có nêu lý do."),

(153,"Expiry, eviction policies and the memory ceiling","TH","Lesson 152",
"Thời gian sống đặt trên khoá và ba cách hết hạn xảy ra: kiểm khi truy cập, quét chủ động theo mẫu ngẫu nhiên, và loại bỏ khi chạm trần bộ nhớ. Hệ quả của cách thứ hai: khoá đã hết hạn vẫn chiếm bộ nhớ một thời gian, nên bộ nhớ dùng không giảm ngay sau khi đặt thời gian sống ngắn. Trần bộ nhớ và tám chính sách loại bỏ, chia hai nhóm: chỉ loại khoá có thời gian sống, hoặc loại mọi khoá. Chọn nhóm nào là quyết định kiến trúc: nhóm thứ hai biến Redis thành bộ đệm thuần, nhóm thứ nhất giữ được dữ liệu không có thời gian sống nhưng rủi ro đầy bộ nhớ và từ chối ghi. Chính sách dùng gần đây nhất so với dùng nhiều nhất và tải nào hợp với cái nào. Không đặt trần bộ nhớ là lỗi cấu hình phổ biến nhất và nó dẫn tới bị hệ điều hành giết, nối lại lesson 14. Đo phân bố thời gian sống và tỉ lệ khoá bị loại.",
"Chọn chính sách loại bỏ và trần bộ nhớ cho một tải cho trước, và chứng minh hệ thống không bị giết cũng không từ chối ghi khi dữ liệu vượt trần.",
"Tầng *đánh giá*. Objective đòi chọn dưới hai rủi ro đối lập. Đạt khi chạy tải vượt trần 3 lần mà tiến trình không bị giết và không lệnh ghi nào bị từ chối, và khi bảng so ít nhất ba chính sách kèm tỉ lệ trúng của từng cái.",
"Đặt trần bộ nhớ thấp hơn tập dữ liệu ba lần. Chạy tải với ba chính sách loại bỏ khác nhau, đo tỉ lệ trúng và số khoá bị loại. Thử chính sách không loại gì và quan sát lệnh ghi bị từ chối. Bỏ trần bộ nhớ và quan sát tiến trình bị giết. Đo độ trễ giữa lúc khoá hết hạn và lúc bộ nhớ thật giảm.",
"Không đặt trần bộ nhớ · dùng chính sách chỉ loại khoá có thời gian sống trong khi phần lớn khoá không có · tin bộ nhớ giảm ngay khi khoá hết hạn.",
"Tải vượt trần 3 lần không làm tiến trình bị giết và không lệnh ghi nào bị từ chối, và có bảng so ba chính sách."),

(154,"Persistence - snapshots, append-only file and what you lose","TH","Lesson 153",
"Hai cơ chế bền vững và đánh đổi khác nhau. Ảnh chụp định kỳ ghi toàn bộ tập dữ liệu ra tệp: nhỏ gọn, khởi động lại nhanh, nhưng mất mọi thay đổi từ ảnh chụp cuối. Tệp chỉ ghi thêm ghi từng lệnh: mất ít hơn nhiều, nhưng tệp lớn dần và khởi động lại chậm vì phải chạy lại lệnh. Ba mức đồng bộ của tệp chỉ ghi thêm và cửa sổ mất dữ liệu tương ứng, cùng cấu trúc với lesson 16 và 138. Viết lại tệp chỉ ghi thêm để nén lịch sử, và chi phí bộ nhớ lúc viết lại do sao chép tiến trình. Dùng cả hai cơ chế cùng lúc. Điểm phục hồi thật của Redis trong từng cấu hình, và vì sao nó thường tệ hơn một cơ sở dữ liệu quan hệ. Kết luận kiến trúc rút ra: coi Redis là nguồn dữ liệu gốc chỉ hợp lý khi đã đo điểm phục hồi và nghiệp vụ chấp nhận con số đó, còn mặc định nên coi nó là lớp đệm mất được.",
"Đo điểm phục hồi thật ở bốn cấu hình bền vững bằng thực nghiệm giết tiến trình, và kết luận cấu hình nào đủ để giữ dữ liệu gốc.",
"Tầng *đánh giá*. Objective đòi kết luận về một quyết định kiến trúc dựa trên số đo. Đạt khi bốn cấu hình đều có số bản ghi mất và thời gian khởi động lại đo thật, và khi kết luận nêu rõ ngưỡng nghiệp vụ nào chấp nhận được cấu hình nào.",
"Chạy tải ghi 10.000 lệnh mỗi giây. Với bốn cấu hình bền vững, giết tiến trình đột ngột và đếm số lệnh mất, rồi đo thời gian khởi động lại. Lập bảng. Chạy viết lại tệp chỉ ghi thêm trong lúc tải cao và đo bộ nhớ đỉnh.",
"Dùng Redis làm nguồn gốc với cấu hình mặc định · bật tệp chỉ ghi thêm mà không đo thời gian khởi động lại · viết lại tệp lúc bộ nhớ đã gần trần.",
"Bốn cấu hình có số lệnh mất và thời gian khởi động lại đo thật, và kết luận nêu ngưỡng nghiệp vụ tương ứng."),

(155,"Cache-aside, stampede and cache consistency","TH","Lesson 154",
"Ba mẫu đệm và trách nhiệm khác nhau: đọc qua ứng dụng, đọc qua lớp đệm, và ghi xuyên qua. Mẫu đọc qua ứng dụng là mẫu phổ biến nhất và là mẫu module tập trung vào. Ồ ạt nạp lại xảy ra khi một khoá nóng hết hạn và hàng nghìn yêu cầu cùng lúc đi xuống cơ sở dữ liệu, có thể làm sập nó; ba cách chống là khoá nạp lại, nạp lại trước khi hết hạn, và thêm nhiễu ngẫu nhiên vào thời gian sống, mẫu nhiễu này cùng ý tưởng với lesson 34. Nhất quán giữa đệm và nguồn: xoá khoá khi ghi thay vì cập nhật khoá, vì cập nhật tạo cửa sổ tranh chấp giữa hai thao tác không nguyên tử, nối lại lesson 51. Thứ tự xoá đệm và ghi nguồn, cùng cửa sổ không nhất quán còn lại trong mỗi thứ tự. Đệm giá trị rỗng để chống truy vấn lặp cho khoá không tồn tại. Thời gian sống là công cụ nhất quán chính: mọi thiết kế đệm cuối cùng đều dựa vào nó để tự sửa.",
"Tái hiện ồ ạt nạp lại và chặn nó bằng một trong ba cách, chứng minh bằng số yêu cầu đi xuống cơ sở dữ liệu.",
"Tầng *áp dụng*. Objective có tiêu chí đếm được. Đạt khi tái hiện được ít nhất 500 yêu cầu cùng đi xuống cơ sở dữ liệu khi khoá nóng hết hạn, và khi bản sửa hạ con số đó xuống dưới 5 trong cùng kịch bản.",
"Dựng lớp đệm đọc qua ứng dụng cho một khoá nóng. Cho 1.000 ứng dụng khách đồng thời, đặt thời gian sống ngắn, đếm số yêu cầu xuống cơ sở dữ liệu tại thời điểm hết hạn. Cài một trong ba cách chống, đo lại. Tái hiện đệm không nhất quán bằng cách cập nhật khoá thay vì xoá.",
"Cập nhật khoá đệm thay vì xoá · đặt cùng thời gian sống cho mọi khoá nên chúng hết hạn cùng lúc · không đệm giá trị rỗng nên truy vấn lặp cho khoá không tồn tại.",
"Tái hiện được ít nhất 500 yêu cầu cùng xuống cơ sở dữ liệu, và bản sửa hạ xuống dưới 5."),

(156,"Hot keys, big keys and blocking commands","TH","Lesson 155",
"Redis xử lý lệnh trên một luồng, nên một lệnh chậm chặn mọi lệnh khác, và đây là nguồn gốc của ba vấn đề trong bài. Khoá nóng: một khoá nhận phần lớn lưu lượng, làm một nút hoặc một lõi bão hoà trong khi phần còn lại rỗi, cùng bản chất với lệch phân vùng ở lesson 48; ba cách xử lý là chia khoá thành nhiều bản, đệm cục bộ ở tầng ứng dụng, và giảm tần suất truy cập. Khoá lớn: một cấu trúc hàng triệu phần tử làm mọi lệnh chạm nó thành chậm, và xoá nó cũng chặn, nên có lệnh xoá nền. Lệnh chặn cần tránh trên máy chủ sản xuất và lệnh quét thay thế. Đo độ trễ theo phân vị chứ không theo trung bình, vì một lệnh chặn làm đuôi phân bố dài ra mà trung bình không thấy, nối lại lesson 17. Nhật ký lệnh chậm và cách đọc nó. Quy mô theo chiều ngang bị giới hạn bởi khoá nóng vì thêm nút không giúp gì.",
"Định vị một khoá nóng và một khoá lớn trên hệ thống đang chạy, và chứng minh chúng làm đuôi phân bố độ trễ dài ra.",
"Tầng *phân tích*. Objective đòi chẩn đoán bằng phân vị chứ không bằng trung bình. Đạt khi định vị đúng cả khoá nóng lẫn khoá lớn bằng công cụ, và khi số đo cho thấy phân vị 99 tăng rõ rệt trong khi trung bình gần như không đổi.",
"Dựng tải có một khoá nhận 80% lưu lượng và một khoá chứa một triệu phần tử. Đo độ trễ trung bình và phân vị 99. Dùng công cụ tìm khoá nóng và khoá lớn. Chạy một lệnh chặn trên khoá lớn và đo tác động lên phân vị 99. Xoá khoá lớn bằng lệnh thường rồi bằng lệnh xoá nền, so thời gian chặn.",
"Theo dõi độ trễ trung bình · chạy lệnh liệt kê toàn bộ khoá để tìm khoá lớn · thêm nút để chữa khoá nóng.",
"Định vị đúng khoá nóng và khoá lớn, và số đo cho thấy phân vị 99 tăng trong khi trung bình gần như không đổi."),

(157,"Replication, sentinel and cluster mode","LT","Lesson 156",
"Ba mức tổ chức và bài toán mỗi mức giải. Nhân bản chính phụ bất đồng bộ cho đọc mở rộng và dự phòng, với cửa sổ mất dữ liệu bằng độ trễ, cùng mô hình lesson 120. Người canh gác giám sát và tự chuyển đổi dự phòng, cần đa số để tránh chia đôi cụm. Chế độ cụm phân mảnh dữ liệu theo khe băm, cho mở rộng ghi; hệ quả là lệnh chạm nhiều khoá chỉ chạy được khi các khoá cùng khe, và thẻ khoá là cách ép chúng cùng khe. Không có giao dịch xuyên mảnh. Phân biệt ba nhu cầu để chọn đúng mức: cần dự phòng thì nhân bản đủ, cần tự chuyển đổi thì thêm người canh gác, cần vượt bộ nhớ một máy mới cần cụm. Sai lầm thường gặp là dựng cụm khi chỉ cần nhân bản, chuốc thêm ràng buộc khoá cùng khe mà không được lợi gì. Chia đôi cụm và mất ghi khi hai bên cùng nhận.",
"Chọn mức tổ chức cho ba yêu cầu khác nhau, và nêu ràng buộc mà chế độ cụm áp lên cách viết lệnh.",
"Tầng *hiểu*. Bài lý thuyết vì dựng cụm đầy đủ vượt phạm vi mức `B`. Đạt khi chọn đúng mức cho ba yêu cầu kèm lý do, và khi chỉ ra được hai lệnh không chạy được ở chế độ cụm cùng cách sửa bằng thẻ khoá.",
"Nhận ba yêu cầu: chịu được mất một máy, tự phục hồi không cần người, và tập dữ liệu vượt bộ nhớ một máy. Chọn mức cho từng cái. Dựng nhân bản chính phụ và đo độ trễ. Trên một cụm thử nghiệm, chạy hai lệnh chạm nhiều khoá, quan sát lỗi, sửa bằng thẻ khoá.",
"Dựng chế độ cụm khi chỉ cần nhân bản · giả định giao dịch chạy xuyên mảnh · dùng người canh gác số chẵn nên không có đa số.",
"Chọn đúng mức cho ba yêu cầu kèm lý do, và chỉ ra được hai lệnh cần thẻ khoá cùng cách sửa."),

(158,"Measuring a cache - hit rate, p95 and when to remove it","TH","Lesson 157",
"Không có cơ chế mới. Bài gộp module và nó đặt câu hỏi ngược với phần còn lại: khi nào nên bỏ lớp đệm. Bốn chỉ số đo một lớp đệm: tỉ lệ trúng, độ trễ phân vị 95 của đường có đệm và đường không đệm, tải giảm được ở cơ sở dữ liệu, và chi phí vận hành gồm cả bộ nhớ lẫn thời gian người. Tỉ lệ trúng một mình không kết luận được gì: tỉ lệ trúng 95% trên một truy vấn vốn đã nhanh thì lớp đệm không đáng tồn tại. Phép tính lợi ích ròng: thời gian tiết kiệm nhân số lượt trừ chi phí. Ba điều kiện nên bỏ lớp đệm: nguồn đã đủ nhanh sau khi thêm chỉ mục, tỉ lệ trúng thấp kéo dài, và chi phí nhất quán vượt lợi ích. Rủi ro lớp đệm trở thành phụ thuộc cứng: hệ thống không sống nổi khi mất đệm, và phép thử là tắt đệm trong giờ thấp điểm rồi đo. Kế hoạch cho tình huống mất sạch dữ liệu đệm.",
"Đo bốn chỉ số của một lớp đệm và kết luận nên giữ hay nên bỏ, kèm phép thử tắt đệm để xác nhận hệ thống sống được.",
"Tầng *đánh giá*. Objective đòi kết luận về sự tồn tại của một thành phần, không chỉ tối ưu nó. Đạt khi bốn chỉ số đều có số, khi phép tính lợi ích ròng được trình bày, và khi phép thử tắt đệm chạy thật cho biết hệ thống sống được hay không.",
"Đo bốn chỉ số cho lớp đệm dựng ở lesson 155. Tính lợi ích ròng. Thêm chỉ mục cho truy vấn nguồn rồi đo lại, xem lợi ích còn bao nhiêu. Tắt đệm hoàn toàn trong 10 phút dưới tải và đo. Viết kế hoạch cho tình huống mất sạch dữ liệu đệm, gồm cả cách nạp lại dần thay vì cùng lúc.",
"Báo cáo tỉ lệ trúng một mình · giữ lớp đệm vì đã dựng rồi · không bao giờ thử tắt đệm nên không biết hệ thống có sống được không.",
"Bốn chỉ số đều có số, có phép tính lợi ích ròng, và phép thử tắt đệm chạy thật cho kết luận rõ ràng."),
]
