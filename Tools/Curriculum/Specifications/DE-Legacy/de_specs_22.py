# -*- coding: utf-8 -*-
"""DE M35 Docker + M36 Kubernetes."""

M35 = ("Docker", 357, 364, """| | |
|---|---|
| **Objective cấp module** | Đóng gói được một thành phần dữ liệu thành ảnh chạy lại giống nhau trên máy khác, và giải thích mọi dòng trong tệp định nghĩa bằng cơ chế lớp |
| **Tiền đề** | M34 |
| **Exit criterion** | Người khác chạy ảnh của bạn trên máy họ cho cùng kết quả, ảnh dưới ngưỡng dung lượng, và không có bí mật nào nằm trong lớp ảnh |
| **Kỹ năng SFIA** | `SYSP` mức 3 · `PROG` mức 3 |
| **Chế độ hỏng** | Chép một tệp định nghĩa mẫu, cài mọi thứ trong một lớp, nhét mật khẩu vào biến môi trường lúc dựng, rồi đẩy ảnh có bí mật lên kho công khai |""",
"""Mức `A`. Module ngắn vì nó phục vụ ba module sau chứ đứng riêng: Kubernetes ở M36 chạy ảnh, cloud ở M37 triển khai ảnh, và mọi lab từ đây trở đi đóng gói bằng ảnh.

Lesson 91 đã đặt tiêu chí *clone, một lệnh, cùng kết quả*; module này là cách đạt tiêu chí đó khi thành phần có phụ thuộc hệ thống chứ chỉ thư viện Python.""")

L35 = [
(357,"Why containers - the dependency problem and what an image is","LT","Module 35: M34",
"Bài toán gốc đã gặp nhiều lần: mã chạy trên máy này và hỏng trên máy kia vì phiên bản thư viện hệ thống, biến môi trường hoặc phiên bản runtime khác nhau. Môi trường ảo Python ở lesson 89 giải phần thư viện Python nhưng không giải phần hệ thống, và phần lớn công cụ dữ liệu đều có phụ thuộc hệ thống. Ảnh là một hệ tệp đóng gói sẵn cộng siêu dữ liệu về lệnh chạy; container là một tiến trình chạy trên nhân của máy chủ nhưng nhìn thấy hệ tệp của ảnh. Phân biệt với máy ảo: container dùng chung nhân nên nhẹ và khởi động nhanh, đổi lại không cách ly bằng máy ảo và phải cùng loại nhân. Ba thứ container **không** giải: không làm mã chạy nhanh hơn, không sửa lỗi phụ thuộc mà chỉ đóng băng chúng, và không tự cho khả năng mở rộng. Vì sao điều này quan trọng với dữ liệu: một công việc Spark hay một trình nối có hàng chục phụ thuộc hệ thống, nên đóng gói là cách duy nhất để chạy lại được sau một năm.",
"Giải thích khác biệt giữa ảnh và container, và chỉ ra ba loại phụ thuộc mà môi trường ảo không giải được còn container thì có.",
"Tầng *hiểu*. Bài mở module, nối vấn đề đã trải qua ở M8 với một cơ chế mới. Kiểm bằng bài giải thích cộng một thí nghiệm tái hiện; đạt khi tái hiện được lỗi phụ thuộc hệ thống và chứng minh container sửa được.",
"Viết một script phụ thuộc vào một thư viện hệ thống ở phiên bản cụ thể. Chạy trên hai máy có phiên bản khác nhau và ghi lại lỗi. Đóng gói thành ảnh và chạy lại trên cả hai máy. So thời gian khởi động container với thời gian khởi động một máy ảo.",
"Nghĩ container là máy ảo nhẹ · tin rằng đóng gói làm mã nhanh hơn · dùng container mà vẫn phụ thuộc vào tệp trên máy chủ.",
"Tái hiện được lỗi phụ thuộc hệ thống trên hai máy, bản đóng gói chạy giống nhau trên cả hai, và nêu đúng ba thứ container không giải."),

(358,"Images, layers and a Dockerfile that rebuilds fast","TH","Lesson 357",
"Ảnh gồm nhiều lớp xếp chồng, mỗi lệnh trong tệp định nghĩa tạo một lớp, và lớp được lưu đệm theo thứ tự. Hệ quả chi phối cách viết: **đặt thứ ít thay đổi lên trước, thứ hay thay đổi xuống sau**, vì một lớp đổi thì mọi lớp sau nó phải dựng lại. Sai lầm điển hình là chép toàn bộ mã nguồn trước rồi mới cài phụ thuộc, khiến mỗi lần sửa một dòng mã là cài lại toàn bộ phụ thuộc. Tệp bỏ qua lúc dựng quyết định thứ gì được gửi tới trình dựng, và thiếu nó thì thư mục dữ liệu hàng gigabyte bị gửi theo. Phân biệt hai lệnh chạy lệnh lúc khởi động và lý do chọn dạng mảng thay vì dạng chuỗi: dạng chuỗi chạy qua shell nên tiến trình chính không nhận được tín hiệu dừng, dẫn thẳng tới vấn đề ở lesson 359. Ghim phiên bản ảnh nền bằng thẻ cụ thể chứ thẻ mới nhất, vì thẻ mới nhất làm bản dựng hôm nay khác bản dựng hôm qua và phá tính tái lập.",
"Viết tệp định nghĩa có thứ tự lớp đúng, và chứng minh bằng số đo rằng sửa một dòng mã không kích hoạt cài lại phụ thuộc.",
"Tầng *áp dụng*. Objective là một kỹ năng viết có kết quả đo được bằng thời gian dựng lại. Kiểm bằng cặp số đo; đạt khi thời gian dựng lại sau khi sửa mã giảm rõ rệt và ảnh nền được ghim phiên bản.",
"Viết hai tệp định nghĩa cho cùng một ứng dụng: một bản chép mã trước, một bản cài phụ thuộc trước. Sửa một dòng mã và đo thời gian dựng lại của cả hai. Thêm tệp bỏ qua và đo lại dung lượng gửi tới trình dựng. Đổi thẻ ảnh nền từ mới nhất sang bản cụ thể.",
"Chép mã trước khi cài phụ thuộc · dùng thẻ mới nhất · quên tệp bỏ qua nên gửi cả thư mục dữ liệu · dùng dạng chuỗi cho lệnh khởi động.",
"Thời gian dựng lại sau khi sửa mã giảm rõ rệt có số, dung lượng gửi tới trình dựng giảm, và ảnh nền đã ghim phiên bản."),

(359,"Running containers - processes, signals and exit codes","TH","Lesson 358",
"Container là một tiến trình, nên mọi thứ đã học về tiến trình ở M3 áp dụng nguyên vẹn, và ba chi tiết hay bị bỏ qua gây hỏng trong sản xuất. Một là tiến trình số một: tiến trình chính trong container nhận tín hiệu dừng, nên nếu nó là shell thì tín hiệu không tới được chương trình thật và container bị giết cứng sau thời gian chờ, làm công việc đang ghi dở bị cắt ngang. Hai là mã thoát: hệ điều phối dựa vào mã thoát để biết công việc thành công hay thất bại, nên chương trình phải trả mã đúng, đúng yêu cầu đã đặt ở lesson 96. Ba là nhật ký ra luồng chuẩn chứ ghi tệp trong container, vì hệ thu thập nhật ký đọc luồng chuẩn và tệp trong container biến mất khi container chết. Kiểm tra sức khoẻ và khác biệt giữa kiểm tra tiến trình còn sống với kiểm tra ứng dụng còn phục vụ được. Giới hạn tài nguyên ở mức container và điều gì xảy ra khi vượt giới hạn bộ nhớ.",
"Đóng gói một công việc sao cho nó dừng sạch khi nhận tín hiệu, trả đúng mã thoát, và ghi nhật ký ra luồng chuẩn.",
"Tầng *áp dụng*. Objective là ba yêu cầu vận hành kiểm được bằng thí nghiệm dừng và đọc mã thoát. Kiểm bằng ba phép thử; đạt khi cả ba đạt và container dừng trong thời gian chờ.",
"Đóng gói một công việc ghi dữ liệu. Gửi tín hiệu dừng giữa chừng ở hai bản, một dùng dạng chuỗi và một dùng dạng mảng, đo thời gian dừng và kiểm tra dữ liệu có bị cắt dở không. Cho công việc thất bại và kiểm mã thoát. Đặt giới hạn bộ nhớ thấp và ghi lại sự kiện khi vượt.",
"Dùng shell làm tiến trình chính · nuốt ngoại lệ rồi vẫn thoát mã không · ghi nhật ký vào tệp trong container · không đặt giới hạn tài nguyên.",
"Bản dạng mảng dừng sạch trong thời gian chờ và dữ liệu không cắt dở, mã thoát đúng ở cả hai trường hợp, và nhật ký đọc được từ luồng chuẩn."),

(360,"Networking and volumes - where the data actually lives","TH","Lesson 359",
"Hệ tệp của container biến mất khi container bị xoá, nên mọi dữ liệu cần sống lâu hơn phải nằm ngoài. Hai cách đưa ra ngoài và khác biệt thực tế: khối lượng do nền tảng quản lý, hợp cho dữ liệu; gắn thư mục máy chủ, tiện khi phát triển nhưng buộc container phụ thuộc vào bố trí máy chủ nên không dùng trong sản xuất. Quyền sở hữu tệp giữa người dùng trong container và người dùng trên máy chủ là nguồn lỗi phổ biến khi ghi dữ liệu. Mạng: mỗi container có địa chỉ riêng trong mạng ảo, và các container cùng mạng gọi nhau bằng tên chứ bằng địa chỉ, nên phụ thuộc giữa các thành phần khai báo bằng tên dịch vụ. Cổng chỉ cần công bố ra ngoài khi có người ngoài mạng cần gọi vào. Vì sao container chạy Spark hoặc Kafka cần chú ý địa chỉ quảng bá: thành phần tự báo địa chỉ của mình cho bên khác, và báo sai thì bên ngoài không kết nối được dù cổng đã mở, đây là lỗi hay gặp nhất khi dựng cụm bằng container.",
"Đóng gói một thành phần có trạng thái sao cho dữ liệu sống qua việc xoá và tạo lại container, và hai container gọi được nhau bằng tên.",
"Tầng *áp dụng*. Objective là hai cấu hình kiểm được bằng thí nghiệm xoá và gọi. Kiểm bằng hai phép thử; đạt khi dữ liệu còn nguyên sau khi tạo lại và kết nối theo tên thành công.",
"Chạy PostgreSQL trong container với khối lượng. Ghi dữ liệu, xoá container, tạo lại và kiểm dữ liệu còn nguyên. Chạy thêm một container ứng dụng, cho nó kết nối tới cơ sở dữ liệu bằng tên dịch vụ. Cố ý đặt sai địa chỉ quảng bá của một thành phần và ghi lại triệu chứng.",
"Lưu dữ liệu trong hệ tệp container · gắn thư mục máy chủ trong sản xuất · công bố mọi cổng ra ngoài · quên quyền sở hữu tệp nên container không ghi được.",
"Dữ liệu còn nguyên sau khi xoá và tạo lại, hai container gọi nhau bằng tên thành công, và mô tả đúng triệu chứng khi địa chỉ quảng bá sai."),

(361,"Multi-stage builds and image size","TH","Lesson 360",
"Ảnh lớn tốn ba thứ: thời gian tải về mỗi lần khởi động một tác vụ mới, dung lượng kho ảnh, và diện tích bị tấn công vì càng nhiều gói càng nhiều lỗ hổng. Dựng nhiều giai đoạn tách môi trường biên dịch khỏi môi trường chạy: giai đoạn đầu có trình biên dịch và công cụ phát triển, giai đoạn cuối chỉ chép kết quả sang một ảnh nền tối giản. Với công cụ dữ liệu thường giảm được nhiều lần dung lượng. Ba kỹ thuật bổ sung: chọn ảnh nền gọn, gộp các lệnh cài đặt và dọn bộ đệm gói trong cùng một lớp vì dọn ở lớp sau không xoá được byte ở lớp trước, và không cài công cụ gỡ lỗi vào ảnh sản xuất. Quét lỗ hổng như một bước trong tích hợp liên tục và ngưỡng chặn phát hành. Cảnh báo về ảnh nền quá tối giản với công cụ dữ liệu: một số thư viện cần thư viện hệ thống chuẩn nên chọn nền sai làm mất nhiều giờ gỡ lỗi khó hiểu.",
"Giảm dung lượng ảnh xuống dưới ngưỡng bằng dựng nhiều giai đoạn mà ứng dụng vẫn chạy đúng, kèm kết quả quét lỗ hổng.",
"Tầng *áp dụng*. Objective là một tối ưu có ngưỡng rõ và có ràng buộc không được làm hỏng chức năng. Kiểm bằng cặp số đo cộng bộ kiểm thử; đạt khi dưới ngưỡng, kiểm thử xanh và số lỗ hổng mức cao bằng không.",
"Đo dung lượng ảnh ban đầu. Chuyển sang dựng hai giai đoạn, đo lại. Gộp lệnh cài và dọn bộ đệm trong một lớp, đo lại. Chạy bộ kiểm thử trên ảnh cuối. Quét lỗ hổng trước và sau, lập bảng.",
"Dọn bộ đệm ở lớp sau rồi tưởng đã giảm dung lượng · chọn ảnh nền quá tối giản rồi thiếu thư viện hệ thống · để công cụ gỡ lỗi trong ảnh sản xuất.",
"Dung lượng dưới ngưỡng, bộ kiểm thử xanh trên ảnh cuối, và bảng quét lỗ hổng cho thấy không còn lỗ hổng mức cao."),

(362,"Secrets and configuration in containers","TH","Lesson 361",
"Quy tắc đã đặt từ lesson 89 và 2038 áp dụng ở đây với một cái bẫy riêng: **mọi thứ đưa vào lúc dựng đều nằm lại trong lớp ảnh và ai tải ảnh về đều đọc được**, kể cả khi lệnh sau đó xoá tệp đi, vì lớp trước vẫn còn. Nên không bao giờ truyền bí mật bằng đối số dựng hoặc chép tệp bí mật vào ảnh. Ba cách đúng theo thứ tự ưu tiên: lấy từ kho bí mật lúc chạy, gắn vào lúc chạy dưới dạng tệp tạm, và truyền qua biến môi trường lúc chạy, cách cuối tiện nhất nhưng biến môi trường lộ ra khi ai đó xem thông tin tiến trình. Phân biệt cấu hình với bí mật: cấu hình đưa vào ảnh được, bí mật thì không. Cách kiểm chứng ảnh không chứa bí mật: duyệt từng lớp và tìm chuỗi, và đưa bước quét này vào tích hợp liên tục. Xử lý khi phát hiện bí mật đã vào ảnh và ảnh đã đẩy lên kho: xoay bí mật là bắt buộc, xoá ảnh là chưa đủ.",
"Đưa bí mật vào container đúng cách và chứng minh bằng cách duyệt lớp rằng ảnh không chứa bí mật nào.",
"Tầng *áp dụng*. Objective là một yêu cầu bảo mật kiểm được bằng phép quét khách quan. Kiểm bằng quét lớp; đạt khi ảnh sạch và quy trình xử lý khi lộ được viết ra.",
"Cố ý dựng một ảnh có mật khẩu truyền qua đối số dựng, rồi duyệt lớp và trích ra mật khẩu đó để tự thấy vấn đề. Dựng lại bằng cách đưa bí mật lúc chạy. Quét lại và chứng minh sạch. Thêm bước quét bí mật vào quy trình tích hợp liên tục. Viết quy trình bốn bước khi phát hiện bí mật đã bị đẩy lên kho.",
"Truyền bí mật bằng đối số dựng · xoá tệp bí mật ở lớp sau rồi tưởng đã an toàn · chỉ xoá ảnh mà không xoay bí mật · trộn lẫn cấu hình và bí mật.",
"Trích được mật khẩu từ ảnh sai để chứng minh vấn đề, ảnh đúng quét sạch, và quy trình xử lý khi lộ có đủ bước xoay bí mật."),

(363,"Compose for a local data stack","TH","Lesson 362",
"Một hệ dữ liệu cần nhiều thành phần chạy cùng lúc, và dựng bằng tay từng cái là cách không lặp lại được. Tệp khai báo nhiều dịch vụ mô tả toàn bộ ngăn xếp ở một chỗ: ảnh, biến môi trường, khối lượng, mạng, và phụ thuộc khởi động. Phụ thuộc khởi động có một bẫy: khai báo thứ tự chỉ đảm bảo container khởi động theo thứ tự, **không đảm bảo dịch vụ bên trong đã sẵn sàng nhận kết nối**, nên phải dùng kiểm tra sức khoẻ ở lesson 359 hoặc vòng lặp chờ trong mã. Giá trị thật của cách này với chương trình: mọi lab từ M11 tới M34 dựng lại được bằng một lệnh, nên tiêu chí ở lesson 91 đạt được cho cả ngăn xếp chứ chỉ cho một script. Ranh giới phải giữ: cách này dành cho môi trường phát triển và kiểm thử tích hợp, không dành cho sản xuất, vì không có khả năng tự phục hồi, không có mở rộng, không có lập lịch, và đó là lý do M36 tồn tại.",
"Dựng lại toàn bộ ngăn xếp dữ liệu của mình bằng một lệnh trên máy trống, và xử lý đúng vấn đề dịch vụ chưa sẵn sàng.",
"Tầng *áp dụng*. Objective là tiêu chí *một lệnh, cùng kết quả* áp cho nhiều dịch vụ. Kiểm bằng phép thử trên máy trống do người khác chạy; đạt khi lệnh duy nhất dựng xong và bộ kiểm thử tích hợp xanh.",
"Viết tệp khai báo cho ngăn xếp gồm PostgreSQL, Kafka, kho đối tượng và một công việc xử lý. Cố ý bỏ kiểm tra sức khoẻ và quan sát công việc chết vì kết nối sớm. Thêm kiểm tra sức khoẻ và chạy lại. Đưa cho một học viên khác chạy trên máy trống.",
"Dựa vào thứ tự khởi động thay vì kiểm tra sức khoẻ · ghim dữ liệu vào thư mục máy chủ · dùng cách này cho sản xuất · để cấu hình khác nhau giữa các máy.",
"Một lệnh dựng xong ngăn xếp trên máy trống của người khác, và bộ kiểm thử tích hợp xanh ở lần chạy đầu."),

(364,"Containerising the reference pipeline","TH","Lesson 363",
"Bài khép module: đóng gói mọi thành phần của pipeline tham chiếu thành ảnh và dựng lại toàn bộ bằng một lệnh. Danh mục kiểm phải qua cho từng ảnh: ảnh nền ghim phiên bản, dựng nhiều giai đoạn, không chứa bí mật, chạy bằng người dùng không phải quản trị, tiến trình chính nhận được tín hiệu, nhật ký ra luồng chuẩn, kiểm tra sức khoẻ có nghĩa, và có nhãn ghi phiên bản mã nguồn. Gắn thẻ ảnh theo quy ước có thể truy ngược: thẻ theo mã nguồn chứ chỉ thẻ mới nhất, vì thẻ mới nhất làm không biết môi trường đang chạy bản nào. Đẩy ảnh lên kho riêng và đo thời gian tải về, vì thời gian đó cộng vào thời gian khởi động mỗi tác vụ ở M36. Bằng chứng nộp kèm: bảng danh mục kiểm cho từng ảnh, dung lượng từng ảnh, và kết quả một người khác dựng lại trên máy trống.",
"Đóng gói toàn bộ pipeline đạt danh mục kiểm tám điểm cho mọi ảnh, và người khác dựng lại được trên máy trống.",
"Tầng *áp dụng*. Bài tổng hợp module thành một bộ ảnh đạt chuẩn. Kiểm bằng danh mục kiểm cộng phép thử dựng lại; đạt khi mọi ảnh qua cả tám điểm và phép thử dựng lại thành công.",
"Đóng gói mọi thành phần. Lập bảng danh mục kiểm tám điểm cho từng ảnh. Gắn thẻ theo mã nguồn và đẩy lên kho riêng. Đo dung lượng và thời gian tải về từng ảnh. Đưa cho một học viên khác dựng lại trên máy trống và ghi lại mọi chỗ họ phải hỏi.",
"Chạy container bằng quyền quản trị · gắn thẻ mới nhất · bỏ qua kiểm tra sức khoẻ cho thành phần không có cổng · nộp mà chưa ai dựng lại thử.",
"Mọi ảnh qua cả tám điểm trong danh mục kiểm, và người khác dựng lại thành công trên máy trống mà không phải hỏi câu nào."),
]

M36 = ("Kubernetes", 365, 374, """| | |
|---|---|
| **Objective cấp module** | Chạy được khối lượng công việc dữ liệu trên Kubernetes ở mức `B`, và chẩn đoán được một tác vụ không khởi động bằng sự kiện chứ bằng phỏng đoán |
| **Tiền đề** | M35 |
| **Exit criterion** | Một công việc theo lịch và một dịch vụ có trạng thái chạy đúng, sống qua việc xoá một tác vụ, và ba sự cố khởi động được chẩn đoán đúng |
| **Kỹ năng SFIA** | `SYSP` mức 3 · `NTAS` mức 3 |
| **Chế độ hỏng** | Chép tệp khai báo mẫu, không đặt yêu cầu và giới hạn tài nguyên, rồi tác vụ bị giết vì hết bộ nhớ hoặc chiếm hết nút mà không ai hiểu vì sao |""",
"""Mức `B`: chạy được khối lượng công việc và chẩn đoán được, không yêu cầu vận hành cụm.

Module trả lời trước một câu hỏi thực tế: phần lớn đội dữ liệu ở Việt Nam không tự vận hành Kubernetes mà dùng bản quản lý trên đám mây ở M37. Nhưng đọc được sự kiện và hiểu vòng lặp điều hoà là yêu cầu tối thiểu để chẩn đoán khi công việc của mình không chạy, và đó là phạm vi của module.""")

L36 = [
(365,"What Kubernetes adds over Docker, and what it costs","LT","Module 36: M35",
"Cách khai báo nhiều dịch vụ ở lesson 363 dừng lại ở bốn chỗ, và bốn chỗ đó chính là bốn thứ Kubernetes thêm vào: tự khởi động lại khi tiến trình chết và tự thay thế khi một máy chết; chạy nhiều bản sao và chia tải; xếp tác vụ lên máy còn tài nguyên thay vì người tự chọn; và cập nhật phiên bản mà không dừng phục vụ. Khái niệm trung tâm là **trạng thái mong muốn và vòng lặp điều hoà**: người khai báo muốn có gì, hệ liên tục so hiện trạng với mong muốn và hành động để thu hẹp khoảng cách. Hệ quả cần nhớ ngay: xoá một tác vụ do bộ điều khiển quản lý thì nó mọc lại, vì mong muốn không đổi. Cái giá phải nói thẳng: thêm rất nhiều khái niệm, cần người vận hành, và với đội nhỏ chạy vài công việc theo lịch thì cron trên một máy hoặc bộ điều phối ở M22 đơn giản hơn nhiều. Ba dấu hiệu cho thấy thật sự cần.",
"Nêu bốn năng lực Kubernetes thêm vào so với chạy container đơn lẻ, và quyết định một tình huống cho trước có cần dùng không.",
"Tầng *hiểu*. Bài mở module, đặt đúng kỳ vọng trước khi vào chi tiết. Kiểm bằng bốn tình huống trong đó ít nhất hai không nên dùng; đạt khi quyết định đúng ít nhất ba kèm lý do dẫn từ bốn năng lực.",
"Dựng một cụm một nút cục bộ. Chạy một tác vụ, xoá nó bằng tay và quan sát nó mọc lại. Dừng tiến trình bên trong và quan sát khởi động lại. Cho bốn tình huống và quyết định có nên dùng Kubernetes không.",
"Dùng Kubernetes vì nó phổ biến · nghĩ nó thay thế được bộ điều phối · ngạc nhiên vì tác vụ xoá rồi mọc lại.",
"Quyết định đúng ≥ 3/4 tình huống kèm lý do, và quan sát được tác vụ mọc lại sau khi xoá."),

(366,"Pods, deployments and the reconciliation loop","LT","Lesson 365",
"Tác vụ là đơn vị nhỏ nhất được xếp lịch, gồm một hoặc vài container dùng chung mạng và khối lượng. Không ai tạo tác vụ trực tiếp trong sản xuất; người ta khai báo một đối tượng cấp cao rồi bộ điều khiển tạo tác vụ. Ba loại đối tượng cho ba loại khối lượng công việc dữ liệu: triển khai cho dịch vụ không trạng thái với các bản sao thay thế được cho nhau; tập có trạng thái cho thành phần cần danh tính ổn định và kho riêng như cơ sở dữ liệu; công việc và công việc theo lịch cho tác vụ chạy rồi kết thúc, đúng dạng phần lớn công việc dữ liệu. Vòng lặp điều hoà chạy liên tục nên mọi thay đổi là khai báo chứ mệnh lệnh: sửa tệp khai báo và áp dụng, chứ gõ lệnh sửa trực tiếp, vì lệnh trực tiếp bị ghi đè ở lần áp dụng sau và làm hiện trạng lệch khỏi mã nguồn. Vòng đời tác vụ và các trạng thái, trong đó trạng thái chờ là trạng thái cần chẩn đoán ở lesson 373.",
"Chọn đúng loại đối tượng cho ba khối lượng công việc dữ liệu và giải thích bằng yêu cầu danh tính và vòng đời.",
"Tầng *hiểu*. Bài lý thuyết chuẩn bị cho các bài thực hành; chưa đòi vận hành. Kiểm bằng ba khối lượng công việc; đạt khi chọn đúng cả ba kèm lý do dẫn từ yêu cầu danh tính hoặc vòng đời.",
"Khai báo và chạy cả ba loại đối tượng: một dịch vụ không trạng thái, một cơ sở dữ liệu, và một công việc chạy rồi kết thúc. Với mỗi loại, xoá một tác vụ và quan sát hệ phản ứng. Sửa trực tiếp bằng lệnh rồi áp dụng lại tệp khai báo và quan sát thay đổi bị ghi đè.",
"Dùng triển khai cho cơ sở dữ liệu · tạo tác vụ trực tiếp · sửa bằng lệnh trong sản xuất · dùng dịch vụ chạy mãi cho việc lẽ ra chạy rồi kết thúc.",
"Ba loại đối tượng chạy đúng, chọn đúng cả ba kèm lý do, và quan sát được thay đổi thủ công bị ghi đè."),

(367,"Services, DNS and reaching a workload","TH","Lesson 366",
"Tác vụ có địa chỉ riêng nhưng địa chỉ đó đổi mỗi lần tác vụ được tạo lại, nên không thành phần nào được phép nhớ địa chỉ tác vụ. Dịch vụ là một tên ổn định trỏ tới tập tác vụ đang khoẻ, và chọn tác vụ nào bằng nhãn chứ bằng danh sách, nên tác vụ mới có đúng nhãn là tự vào tập. Ba loại dịch vụ theo phạm vi truy cập: chỉ trong cụm, mở cổng trên mọi nút, và xin một bộ cân bằng tải từ đám mây. Tên miền nội bộ theo quy ước cố định, nên thành phần gọi nhau bằng tên chứ bằng địa chỉ, đúng như ở lesson 360 nhưng ở quy mô cụm. Dịch vụ không có địa chỉ ảo dùng cho tập có trạng thái, vì ở đó mỗi bản sao cần được gọi đích danh, ví dụ ba nút Kafka. Ba nguyên nhân gọi không tới và cách phân biệt: nhãn không khớp, cổng khai báo sai, và tác vụ chưa qua kiểm tra sẵn sàng nên bị loại khỏi tập.",
"Cho hai thành phần gọi được nhau bằng tên dịch vụ, và chẩn đoán đúng một dịch vụ không tới được trong ba nguyên nhân.",
"Tầng *áp dụng*. Objective là cấu hình cộng chẩn đoán, kiểm được bằng phép gọi thật. Kiểm bằng ba sự cố kết nối tiêm sẵn; đạt khi chẩn đoán đúng ít nhất hai và kết nối thành công sau khi sửa.",
"Cho một ứng dụng gọi tới PostgreSQL bằng tên dịch vụ. Giảng viên tiêm ba sự cố kết nối theo ba nguyên nhân. Với mỗi lần, chẩn đoán bằng cách xem tập đích của dịch vụ và nhãn tác vụ, rồi sửa. Dựng một tập có trạng thái ba bản sao và gọi đích danh từng bản.",
"Nhớ địa chỉ tác vụ trong cấu hình · để nhãn dịch vụ lệch nhãn tác vụ · quên kiểm tra sẵn sàng nên tác vụ nhận lưu lượng khi chưa sẵn sàng.",
"Chẩn đoán đúng ≥ 2/3 sự cố kết nối và kết nối thành công sau khi sửa, gọi được đích danh từng bản sao của tập có trạng thái."),

(368,"Configuration and secrets - ConfigMap, Secret and the boundary","TH","Lesson 367",
"Tách cấu hình khỏi ảnh là nguyên tắc đã đặt ở lesson 362; Kubernetes cung cấp hai đối tượng cho hai loại. Đối tượng cấu hình giữ giá trị không nhạy cảm, đối tượng bí mật giữ giá trị nhạy cảm, và điểm phải nói thẳng: **đối tượng bí mật mặc định chỉ mã hoá dạng chuỗi chứ mã hoá thật**, nên ai đọc được đối tượng là đọc được bí mật, và phải bật mã hoá khi lưu cộng kiểm soát quyền thì mới thực sự an toàn. Hai cách đưa vào tác vụ và khác biệt vận hành: biến môi trường thì đơn giản nhưng đổi giá trị phải khởi động lại tác vụ và giá trị lộ ra khi xem thông tin tiến trình; gắn thành tệp thì cập nhật được mà không khởi động lại, hợp cho cấu hình đổi thường xuyên. Ba nguyên tắc giữ: không đưa bí mật vào tệp khai báo rồi nộp vào kho mã, dùng kho bí mật ngoài cho môi trường sản xuất, và phân quyền đọc bí mật theo từng không gian tên.",
"Đưa cấu hình và bí mật vào tác vụ đúng cách, và chứng minh bằng thực nghiệm rằng cập nhật cấu hình không đòi dựng lại ảnh.",
"Tầng *áp dụng*. Objective là hai cấu hình có ràng buộc bảo mật kiểm được. Kiểm bằng thí nghiệm cập nhật cộng kiểm quyền; đạt khi đổi cấu hình không dựng lại ảnh và tài khoản không có quyền thì đọc bí mật thất bại.",
"Đưa cấu hình vào bằng cả hai cách. Đổi một giá trị và quan sát khác biệt giữa hai cách. Tạo một tài khoản chỉ có quyền đọc cấu hình, thử đọc bí mật và ghi lại kết quả. Giải mã một đối tượng bí mật để tự thấy nó chỉ là chuỗi mã hoá cơ bản.",
"Tin rằng đối tượng bí mật đã được mã hoá · nộp tệp khai báo chứa bí mật vào kho mã · dùng biến môi trường cho cấu hình đổi thường xuyên.",
"Đổi cấu hình có hiệu lực mà không dựng lại ảnh, tài khoản thiếu quyền bị từ chối đọc bí mật, và tự giải mã được đối tượng bí mật."),

(369,"Resource requests, limits and the OOMKilled event","TH","Lesson 368",
"Hai con số cho mỗi tài nguyên và nhầm lẫn giữa chúng là nguyên nhân phổ biến nhất khiến công việc dữ liệu chạy sai trên Kubernetes. Yêu cầu là lượng tài nguyên bộ xếp lịch dành riêng và dùng để quyết định đặt tác vụ lên nút nào; giới hạn là trần lúc chạy. Hai tài nguyên hành xử khác nhau khi vượt trần: vượt trần CPU thì tác vụ bị bóp tốc độ, còn **vượt trần bộ nhớ thì tác vụ bị giết**, và sự kiện ghi lại lý do đó. Đây là chỗ nối thẳng với M34: một trình thực thi Spark bị giết vì vượt trần bộ nhớ nhìn từ trong Spark giống hệt lỗi hết bộ nhớ, nên phải xem sự kiện ở tầng Kubernetes mới phân biệt được. Đặt yêu cầu quá thấp thì nút bị nhồi quá tải và mọi thứ chậm; đặt quá cao thì lãng phí và tác vụ không xếp được. Cách đặt có căn cứ: đo mức dùng thật qua nhiều lần chạy rồi lấy phân vị cao làm yêu cầu, cộng biên cho giới hạn.",
"Đặt yêu cầu và giới hạn từ mức dùng đo được, và phân biệt một tác vụ bị giết vì vượt trần bộ nhớ với một lỗi hết bộ nhớ trong ứng dụng.",
"Tầng *phân tích*. Objective đòi phân biệt hai hiện tượng giống nhau ở bề mặt, kỹ năng chẩn đoán xuyên tầng. Kiểm bằng hai sự cố có biểu hiện giống nhau; đạt khi phân biệt đúng cả hai và dẫn được bằng chứng từ sự kiện.",
"Chạy một công việc Spark trong Kubernetes với giới hạn bộ nhớ thấp và quan sát sự kiện bị giết. Chạy lại với giới hạn đủ nhưng dữ liệu lệch khoá để gây lỗi hết bộ nhớ trong Spark. So hai thông báo và chỉ ra cách phân biệt. Đo mức dùng thật qua năm lần chạy rồi đặt lại hai con số.",
"Đặt yêu cầu bằng giới hạn cho mọi tác vụ · không đặt gì cả · thấy tác vụ bị giết là tăng bộ nhớ mà chưa xem sự kiện · quên bộ nhớ ngoài vùng quản lý của Spark.",
"Phân biệt đúng hai trường hợp kèm bằng chứng từ sự kiện, và hai con số đặt lại dựa trên phân bố mức dùng qua năm lần chạy."),

(370,"Jobs and CronJobs for data workloads","TH","Lesson 369",
"Phần lớn khối lượng công việc dữ liệu là chạy rồi kết thúc chứ chạy mãi, nên hai đối tượng này là thứ dùng nhiều nhất. Công việc chạy tác vụ tới khi thành công, với số lần thử lại và thời hạn tối đa; mã thoát ở lesson 359 là thứ quyết định thành công hay thất bại, nên chương trình trả mã sai làm hệ hiểu sai. Công việc theo lịch chạy theo biểu thức thời gian, và bốn tham số quyết định hành vi khi lịch chồng nhau: chính sách đồng thời quyết định cho chạy song song hay bỏ qua hay thay thế, hạn khởi động muộn, và số bản ghi giữ lại cho lần thành công và thất bại. Ba khác biệt so với bộ điều phối ở M22 cần nói rõ để không dùng nhầm: không có đồ thị phụ thuộc, không có chạy bù theo khoảng dữ liệu, và không có giao diện xem lịch sử lần chạy. Mẫu thường dùng trong thực tế: bộ điều phối giữ đồ thị và kích hoạt, Kubernetes chạy từng tác vụ, tức là hai thứ bổ sung nhau chứ thay thế nhau.",
"Chạy một công việc dữ liệu theo lịch với chính sách đồng thời đúng, và nêu ba việc bộ điều phối làm mà đối tượng này không làm.",
"Tầng *áp dụng*. Objective là cấu hình đúng cộng nhận ra ranh giới công cụ. Kiểm bằng thí nghiệm lịch chồng cộng bài so sánh; đạt khi hành vi khi chồng lịch đúng như chính sách đã chọn và nêu đủ ba khác biệt.",
"Chạy một công việc theo lịch mỗi phút mà thời gian chạy hai phút. Thử cả ba chính sách đồng thời và ghi lại hành vi từng chính sách. Cho công việc thất bại và quan sát số lần thử lại. Viết ba khác biệt so với bộ điều phối ở M22.",
"Dùng công việc theo lịch thay cho bộ điều phối khi có phụ thuộc · để chính sách mặc định rồi hai lần chạy cùng ghi một bảng · giữ quá nhiều bản ghi lịch sử làm nặng cụm.",
"Ba chính sách đồng thời cho ba hành vi quan sát được đúng như mô tả, và nêu đủ ba khác biệt so với bộ điều phối."),

(371,"Storage - persistent volumes and stateful workloads","TH","Lesson 370",
"Tác vụ là thứ tạm thời nên dữ liệu phải nằm ngoài nó, giống hệt lập luận ở lesson 360 nhưng thêm một tầng trừu tượng vì cụm có nhiều nút. Ba khái niệm nối nhau: yêu cầu khối lượng là thứ người dùng khai báo cần bao nhiêu và kiểu truy cập gì; khối lượng bền là tài nguyên thật; lớp lưu trữ quyết định cách cấp phát tự động. Ba kiểu truy cập và hệ quả: chỉ một nút ghi là kiểu phổ biến nhất và cũng là ràng buộc khiến tác vụ bị buộc vào một nút; nhiều nút cùng đọc ghi cần hệ tệp mạng và chậm hơn. Tập có trạng thái cấp cho mỗi bản sao một khối lượng riêng và giữ nguyên khi tác vụ được tạo lại, nhờ danh tính ổn định ở lesson 366. Chính sách khi xoá quyết định dữ liệu còn hay mất, và để mặc định sai là cách mất dữ liệu nhanh. Với dữ liệu phân tích, cách đúng thường là dùng kho đối tượng ở M33 chứ khối lượng bền, và chỉ dùng khối lượng cho thành phần có trạng thái thật.",
"Chạy một thành phần có trạng thái với khối lượng riêng cho từng bản sao, và chứng minh dữ liệu sống qua việc xoá tác vụ.",
"Tầng *áp dụng*. Objective là cấu hình lưu trữ kiểm được bằng thí nghiệm xoá. Kiểm bằng phép thử xoá tác vụ; đạt khi dữ liệu còn nguyên và mỗi bản sao giữ đúng khối lượng của nó.",
"Dựng một tập có trạng thái ba bản sao, mỗi bản ghi dữ liệu riêng. Xoá một tác vụ và kiểm bản thay thế có gắn đúng khối lượng cũ. Đổi chính sách khi xoá và quan sát khác biệt. Viết hai câu về khi nào nên dùng kho đối tượng thay cho khối lượng bền.",
"Dùng khối lượng bền cho dữ liệu phân tích · để chính sách khi xoá là xoá · chọn kiểu truy cập nhiều nút ghi khi không cần · quên rằng kiểu một nút ghi buộc tác vụ vào một nút.",
"Dữ liệu còn nguyên sau khi xoá tác vụ, mỗi bản sao gắn đúng khối lượng cũ, và nêu đúng tiêu chí chọn giữa hai cách lưu."),

(372,"Scheduling, node pools and cost control","TH","Lesson 371",
"Bộ xếp lịch chọn nút dựa trên yêu cầu tài nguyên ở lesson 369 cộng các ràng buộc người vận hành đặt. Ba cơ chế điều khiển vị trí theo mức độ cứng dần: chọn nút theo nhãn, quy tắc ưa thích hoặc bắt buộc, và cơ chế đánh dấu nút cùng khai báo chấp nhận để dành riêng một nhóm nút cho một loại khối lượng công việc. Với dữ liệu, ba lý do thật để can thiệp: tách khối lượng nặng bộ nhớ khỏi khối lượng nặng CPU, dành nút có đĩa nhanh cho thành phần có trạng thái, và đưa công việc lô lên nhóm nút giá thấp. Máy giá thấp bị thu hồi bất cứ lúc nào, nên chỉ đặt lên đó khối lượng chịu được mất tác vụ, đúng kết luận đã rút ở lesson 355. Tự mở rộng số nút và độ trễ của nó: thêm nút mất vài phút, nên công việc cần chạy ngay phải có nút dự phòng. Ba đòn bẩy giảm chi phí và cách đo hiệu quả từng đòn bẩy.",
"Đặt khối lượng công việc lên đúng nhóm nút bằng cơ chế phù hợp, và định lượng mức giảm chi phí khi chuyển công việc lô sang nút giá thấp.",
"Tầng *áp dụng*. Objective là cấu hình có kết quả đo được bằng tiền và bằng vị trí tác vụ. Kiểm bằng kiểm tra vị trí cộng bảng chi phí; đạt khi tác vụ nằm đúng nhóm và có số giảm chi phí.",
"Tạo hai nhóm nút khác cấu hình. Dùng cả ba cơ chế để đặt ba loại khối lượng công việc lên đúng nhóm và kiểm chứng vị trí thật. Chuyển công việc lô sang nhóm giá thấp, mô phỏng thu hồi một nút và quan sát công việc phục hồi. Tính chi phí trước và sau.",
"Đặt thành phần có trạng thái lên nút giá thấp · dùng ràng buộc cứng rồi tác vụ không xếp được · quên độ trễ khi tự mở rộng · tính chi phí mà bỏ qua phần tài nguyên đặt trước không dùng.",
"Ba loại khối lượng công việc nằm đúng nhóm nút, công việc lô phục hồi sau khi nút bị thu hồi, và có bảng chi phí trước sau."),

(373,"Observability - logs, events and diagnosing a pending pod","TH","Lesson 372",
"Ba nguồn thông tin cho ba loại câu hỏi, và dùng sai nguồn là lý do chẩn đoán lâu. Nhật ký container trả lời ứng dụng đang làm gì, nhưng mất khi tác vụ bị xoá nên cần hệ thu thập tập trung. Sự kiện trả lời **vì sao tác vụ không khởi động được**, và đây là nguồn bị bỏ qua nhiều nhất dù nó nói thẳng nguyên nhân. Mô tả đối tượng trả lời cấu hình hiện tại và trạng thái từng container. Năm nguyên nhân làm tác vụ kẹt ở trạng thái chờ, phân biệt được ngay từ sự kiện: không đủ tài nguyên trên nút nào, ràng buộc vị trí không thoả, không xin được khối lượng, kéo ảnh thất bại vì sai tên hoặc thiếu quyền, và hết hạn mức trong không gian tên. Ba trạng thái hỏng khác và ý nghĩa: khởi động lại liên tục thường là tiến trình chết ngay, lỗi tạo container thường là cấu hình sai, và bị giết vì vượt trần bộ nhớ ở lesson 369. Quy trình chẩn đoán bốn bước theo thứ tự cố định.",
"Chẩn đoán một tác vụ không khởi động về đúng nguyên nhân bằng sự kiện, trong giới hạn thời gian.",
"Tầng *phân tích*. Objective là kỹ năng chẩn đoán dùng trực tiếp khi trực. Kiểm bằng năm sự cố tiêm sẵn tính giờ; đạt khi chẩn đoán đúng ít nhất bốn và mỗi lần dẫn được dòng sự kiện cụ thể.",
"Giảng viên tiêm năm tác vụ hỏng theo năm nguyên nhân, mỗi lần 8 phút. Với mỗi lần, chạy quy trình bốn bước, ghi dòng sự kiện dẫn tới kết luận, và sửa. Dựng thu thập nhật ký tập trung và chứng minh nhật ký của một tác vụ đã xoá vẫn đọc được.",
"Xem nhật ký trước khi xem sự kiện · xoá tác vụ để thử lại rồi mất bằng chứng · khởi động lại triển khai theo phản xạ · không có thu thập nhật ký tập trung.",
"Chẩn đoán đúng ≥ 4/5 sự cố trong giới hạn thời gian kèm dòng sự kiện, và đọc được nhật ký của tác vụ đã bị xoá."),

(374,"Running a data workload on Kubernetes","TH","Lesson 373",
"Bài khép module: đưa hai khối lượng công việc thật của pipeline tham chiếu lên cụm. Một là công việc theo lịch chạy phần biến đổi theo lô, dùng ảnh đã đóng gói ở lesson 364. Hai là một thành phần có trạng thái, và phải nêu rõ quyết định tự vận hành hay dùng dịch vụ quản lý kèm lý do, vì với phần lớn đội thì tự vận hành cơ sở dữ liệu trên Kubernetes là quyết định tốn kém. Danh mục kiểm phải qua: yêu cầu và giới hạn đặt từ số đo, kiểm tra sức khoẻ và sẵn sàng có nghĩa, cấu hình và bí mật tách khỏi ảnh, khối lượng bền cho phần có trạng thái, nhật ký ra hệ tập trung, và chính sách khởi động lại phù hợp. Ba phép thử phải qua: xoá một tác vụ và hệ tự phục hồi, cập nhật phiên bản ảnh mà không mất dữ liệu, và một lần chẩn đoán sự cố có thật ghi lại thành sổ tay.",
"Chạy được hai khối lượng công việc trên cụm đạt danh mục kiểm sáu điểm và qua ba phép thử phục hồi.",
"Tầng *áp dụng*. Bài tổng hợp module thành một triển khai đạt chuẩn. Kiểm bằng danh mục kiểm cộng ba phép thử; đạt khi cả sáu điểm đạt và cả ba phép thử qua.",
"Triển khai hai khối lượng công việc. Lập bảng danh mục kiểm sáu điểm. Thực hiện ba phép thử và ghi kết quả. Viết một quyết định ngắn về tự vận hành hay dùng dịch vụ quản lý cho phần có trạng thái, kèm hai lý do.",
"Sao chép tệp khai báo mẫu mà không đặt tài nguyên · tự vận hành cơ sở dữ liệu mà chưa cân nhắc chi phí · bỏ kiểm tra sẵn sàng · nộp mà chưa thử xoá tác vụ lần nào.",
"Sáu điểm trong danh mục kiểm đều đạt, ba phép thử phục hồi đều qua, và quyết định về phần có trạng thái có hai lý do cụ thể."),
]
