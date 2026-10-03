# -*- coding: utf-8 -*-
"""DE M4 Networking + M5 Algorithms."""

M4 = ("Networking for Data Engineers", 30, 39, """| | |
|---|---|
| **Objective cấp module** | Chẩn đoán một lỗi kết nối hoặc một pipeline chậm vì mạng tới đúng chặng, và viết ứng dụng khách HTTP chịu được nguồn không ổn định |
| **Tiền đề** | M3 |
| **Exit criterion** | Ứng dụng khách nạp hết 100.000 bản ghi từ một API cố ý trả lỗi 20% mà không mất và không trùng bản ghi nào |
| **Kỹ năng SFIA** | `NTAS` mức 2 · `PROG` mức 3 |
| **Chế độ hỏng** | Coi mạng là thứ luôn chạy, nên viết vòng lặp gọi API không có thời gian chờ và pipeline treo vô hạn lúc nửa đêm |""",
"Module không dạy mạng cho người quản trị hạ tầng. Nó dạy đúng phần mà một pipeline chạm tới: vì sao kết nối treo, vì sao thử lại làm hỏng thêm, và vì sao độ trễ quan trọng hơn băng thông khi nạp dữ liệu theo trang.")

L4 = [
(30,"Addresses, subnets, routing and DNS","LT","Module 4: M3",
"Địa chỉ IP, mặt nạ mạng con, và cách đọc ký hiệu độ dài tiền tố. Địa chỉ riêng và địa chỉ công cộng, chuyển đổi địa chỉ mạng, và vì sao một dịch vụ chạy được trên máy cá nhân lại không truy cập được từ nơi khác. Bảng định tuyến và cổng mặc định. Phân giải tên miền: thứ tự tra cứu, bộ nhớ đệm ở nhiều tầng, và thời gian sống của bản ghi. Ba sự cố dữ liệu có gốc ở phân giải tên miền: bộ nhớ đệm giữ địa chỉ cũ sau khi dịch vụ chuyển, thời gian phân giải cộng vào độ trễ mỗi kết nối nếu không dùng lại kết nối, và một bản ghi trỏ nhiều địa chỉ làm tải phân bố không đều. Vì sao tên máy trong tệp cấu hình an toàn hơn địa chỉ IP viết cứng. Khác biệt giữa không kết nối được, hết thời gian chờ, và bị từ chối, ba triệu chứng chỉ ba nguyên nhân khác nhau.",
"Phân biệt ba loại lỗi kết nối và truy mỗi loại về đúng chặng: phân giải tên, định tuyến, hay dịch vụ không lắng nghe.",
"Tầng *phân tích*. Objective là chẩn đoán phân biệt, vì ba lỗi có thông báo gần giống nhau ở tầng ứng dụng. Kiểm bằng ba ca dựng sẵn; đạt khi định vị đúng cả ba và dẫn được lệnh kiểm chứng cho từng chặng.",
"Dựng ba ca trong máy ảo: tên miền không phân giải được, địa chỉ phân giải được nhưng không định tuyến tới, và cổng không có gì lắng nghe. Với mỗi ca, chẩn đoán theo thứ tự phân giải tên, định tuyến, cổng. Ghi lệnh kiểm chứng từng chặng.",
"Kết luận dịch vụ chết khi thật ra tên miền không phân giải được · viết cứng địa chỉ IP vào cấu hình · bỏ qua bộ nhớ đệm phân giải tên khi dịch vụ vừa đổi địa chỉ.",
"Định vị đúng cả ba ca, mỗi ca có lệnh kiểm chứng cho đúng chặng."),

(31,"TCP - handshake, retransmission and flow control","LT","Lesson 30",
"Bắt tay ba bước và chi phí thời gian của nó: một vòng khứ hồi trước khi gửi được byte dữ liệu đầu tiên. Hệ quả trực tiếp: mở kết nối mới cho mỗi yêu cầu làm nạp dữ liệu theo trang chậm gấp nhiều lần so với dùng lại kết nối. Truyền lại khi mất gói và thời gian chờ truyền lại tăng dần. Cửa sổ nhận và điều khiển luồng: bên nhận chậm làm bên gửi tự giảm tốc, cùng ý tưởng với áp lực ngược ở lesson 20. Tích băng thông và độ trễ: vì sao đường truyền băng thông cao nhưng độ trễ lớn không đạt thông lượng công bố nếu cửa sổ nhỏ. Đóng kết nối và trạng thái chờ đóng: vì sao một máy chủ vừa chịu tải lớn lại hết cổng dù không còn kết nối hoạt động. Phân biệt độ trễ với thông lượng bằng một ví dụ định lượng. Giao thức không kết nối và ba trường hợp nó hợp.",
"Ước lượng thời gian nạp 10.000 trang dữ liệu có và không dùng lại kết nối, rồi đo và giải thích chênh lệch bằng số vòng khứ hồi.",
"Tầng *áp dụng*. Objective gồm ước lượng và đối chứng bằng số đo. Đạt khi ước lượng sai trong phạm vi hệ số hai, và khi người học chỉ ra được số vòng khứ hồi của từng cách. Giải thích đúng mà không có số đo thì chưa đạt.",
"Đo độ trễ khứ hồi tới một máy chủ. Ước lượng thời gian nạp 10.000 trang theo hai cách. Viết hai ứng dụng khách: một mở kết nối mới mỗi yêu cầu, một dùng nhóm kết nối. Đo cả hai. Quan sát số kết nối ở trạng thái chờ đóng trong lúc chạy cách thứ nhất.",
"Mở kết nối mới mỗi yêu cầu · so sánh hai đường truyền bằng băng thông mà bỏ qua độ trễ · không đặt giới hạn cho nhóm kết nối nên mở quá nhiều.",
"Ước lượng sai trong phạm vi hệ số hai, và số kết nối ở trạng thái chờ đóng quan sát được ở cách không dùng lại kết nối."),

(32,"TLS, certificates and the errors they produce","TH","Lesson 31",
"Mã hoá khi truyền và ba thứ nó bảo đảm: bí mật, toàn vẹn, và xác thực danh tính máy chủ. Chuỗi chứng chỉ và cơ quan cấp gốc. Bốn lỗi chứng chỉ thường gặp và nguyên nhân từng cái: hết hạn, tên không khớp, chuỗi không đầy đủ, và cơ quan cấp không được tin. Vì sao tắt kiểm chứng chứng chỉ là cách sửa sai và nó mở ra tấn công xen giữa. Kho chứng chỉ tin cậy của hệ thống và của môi trường chạy ngôn ngữ, hai kho khác nhau nên một chương trình báo lỗi trong khi trình duyệt vẫn vào được. Chứng chỉ phía khách cho xác thực hai chiều, mẫu gặp khi nối tới hệ thống ngân hàng. Chi phí bắt tay mã hoá cộng thêm vào bắt tay kết nối, và lý do dùng lại kết nối còn quan trọng hơn. Thời điểm hệ thống sai làm chứng chỉ trông như chưa hiệu lực, một lỗi hay gặp trong vùng chứa.",
"Chẩn đoán bốn lỗi chứng chỉ về đúng nguyên nhân và sửa đúng chỗ, không sửa bằng cách tắt kiểm chứng.",
"Tầng *phân tích*. Objective là chẩn đoán phân biệt với một đáp án sai hấp dẫn là tắt kiểm chứng. Kiểm bằng bốn ca; đạt khi định vị đúng cả bốn và không ca nào được sửa bằng cách tắt kiểm chứng. Một ca sửa bằng tắt kiểm chứng thì cả bài không đạt.",
"Dựng bốn ca lỗi chứng chỉ bằng máy chủ cục bộ. Với mỗi ca đọc chuỗi chứng chỉ, định vị nguyên nhân, sửa đúng chỗ. Thêm một ca đồng hồ hệ thống lệch một năm và quan sát triệu chứng.",
"Tắt kiểm chứng chứng chỉ để cho chạy · thêm chứng chỉ vào kho hệ thống trong khi môi trường chạy dùng kho riêng · bỏ qua chứng chỉ trung gian nên chuỗi đứt.",
"Định vị đúng cả bốn nguyên nhân, và không ca nào sửa bằng cách tắt kiểm chứng."),

(33,"HTTP - methods, status codes and what they mean for a loader","TH","Lesson 32",
"Cấu trúc một yêu cầu và một phản hồi. Phương thức và tính bất biến khi lặp lại: phương thức nào lặp lại an toàn, phương thức nào không, và vì sao điều đó quyết định phương thức nào thử lại được. Nhóm mã trạng thái và hành động đúng cho từng nhóm khi nạp dữ liệu: chuyển hướng phải theo hay không, lỗi phía khách không được thử lại vì thử lại cũng lỗi, lỗi phía máy chủ thử lại được, và riêng mã quá nhiều yêu cầu phải tôn trọng tiêu đề nói chờ bao lâu. Ba lỗi khác nhau bị gộp thành một trong nhiều ứng dụng khách: kết nối hỏng, hết thời gian chờ, và máy chủ trả lỗi. Tiêu đề quan trọng cho nạp dữ liệu: kiểu nội dung, nén, phân trang, giới hạn tốc độ, và định danh yêu cầu để truy vết. Nén khi truyền và đánh đổi giữa bộ xử lý với băng thông. Tải theo dòng thay vì tải hết vào bộ nhớ, bắt buộc khi phản hồi lớn hơn bộ nhớ.",
"Phân loại 12 mã trạng thái và loại lỗi thành thử lại được hay không, và cài đặt xử lý đúng cho từng nhóm.",
"Tầng *áp dụng*. Objective gồm một phép phân loại có đáp án và một cài đặt kiểm được. Đạt khi bảng phân loại đúng ít nhất 10 trên 12, và khi ứng dụng khách xử lý đúng cả ba nhóm trong thực nghiệm bơm lỗi. Phân loại đúng mà cài đặt thử lại cả lỗi phía khách thì không đạt.",
"Dựng một máy chủ giả trả về 12 tình huống: các mã trạng thái, kết nối bị ngắt giữa chừng, và phản hồi chậm hơn thời gian chờ. Viết ứng dụng khách phân loại và xử lý đúng từng cái. Ghi nhật ký phân loại cho mỗi lần gọi.",
"Thử lại lỗi phía khách · bỏ qua tiêu đề chờ bao lâu rồi bị chặn · tải hết phản hồi vào bộ nhớ khi nó lớn hơn RAM.",
"Bảng phân loại đúng ít nhất 10 trên 12, và ứng dụng khách xử lý đúng cả ba nhóm trong thực nghiệm."),

(34,"Timeouts, retries, backoff and jitter","TH","Lesson 33",
"Không đặt thời gian chờ là lỗi thiết kế phổ biến nhất trong mã nạp dữ liệu, vì mặc định của nhiều thư viện là chờ vô hạn. Bốn loại thời gian chờ và cái nào chặn cái nào: chờ kết nối, chờ byte đầu, chờ giữa hai byte, và chờ toàn bộ yêu cầu. Chỉ đặt loại đầu là chưa đủ, vì kết nối mở được rồi máy chủ vẫn treo. Thử lại với khoảng chờ tăng theo cấp số nhân và lý do cộng thêm nhiễu ngẫu nhiên: không có nhiễu thì mọi ứng dụng khách thử lại cùng lúc và tạo bão tải, làm dịch vụ vừa hồi phục lại sập. Ngân sách thử lại và giới hạn trên tổng thời gian. Cầu dao: sau bao nhiêu lỗi liên tiếp thì ngừng gọi, chờ bao lâu rồi thử nửa vời. Khoá bất biến để máy chủ nhận ra yêu cầu lặp và không xử lý hai lần, cơ chế bắt buộc khi thử lại phương thức không bất biến. Vì sao thử lại không điều kiện gây cả bão tải lẫn bản ghi trùng, hai hậu quả cùng lúc.",
"Viết ứng dụng khách có đủ bốn loại thời gian chờ, thử lại có nhiễu và khoá bất biến, rồi chứng minh nó không sinh bản ghi trùng khi máy chủ lỗi 20%.",
"Tầng *áp dụng*. Objective có tiêu chí đúng sai tuyệt đối kiểm bằng đối soát. Đạt khi nạp hết 100.000 bản ghi từ máy chủ lỗi 20%, số bản ghi đích bằng đúng số nguồn, không trùng và không thiếu. Chạy xong mà lệch một bản ghi là không đạt.",
"Dựng máy chủ giả lỗi 20% gồm cả treo không phản hồi. Viết ứng dụng khách nạp 100.000 bản ghi. Đối soát số bản ghi. Sau đó tắt nhiễu ngẫu nhiên và chạy 50 ứng dụng khách cùng lúc, quan sát bão tải.",
"Chỉ đặt thời gian chờ kết nối · thử lại không có nhiễu · thử lại phương thức không bất biến mà không có khoá bất biến.",
"Nạp hết 100.000 bản ghi từ máy chủ lỗi 20%, đối soát khớp tuyệt đối, và quan sát được bão tải khi tắt nhiễu."),

(35,"Pagination, rate limits and resumable loading","TH","Lesson 34",
"Ba kiểu phân trang và đánh đổi: theo số trang đơn giản nhưng sai khi dữ liệu thay đổi giữa chừng, theo con trỏ ổn định hơn, theo khoảng thời gian phù hợp cho nạp gia tăng. Cơ chế bỏ sót và lặp bản ghi khi dùng phân trang theo số trang trên tập đang được ghi thêm, một lỗi âm thầm vì tổng số vẫn trông hợp lý. Giới hạn tốc độ: theo cửa sổ cố định, theo cửa sổ trượt, và theo xô thẻ, cùng cách đọc tiêu đề còn lại bao nhiêu lượt. Tự giới hạn phía khách thay vì chờ bị chặn. Điểm kiểm tra để nạp lại được từ chỗ dừng: lưu gì, lưu lúc nào, và vì sao lưu sau khi ghi dữ liệu chứ không trước. Nối lại lesson 21: bị giết giữa chừng là ca kiểm thử bắt buộc. Nạp song song nhiều trang và điều kiện an toàn. Phát hiện lược đồ nguồn đổi giữa lúc đang nạp.",
"Nạp một tập dữ liệu có phân trang mà nguồn vẫn đang được ghi thêm, và chứng minh không bỏ sót không lặp bản ghi nào.",
"Tầng *áp dụng*. Objective có tiêu chí đối soát tuyệt đối trên một tình huống khó. Đạt khi tập đích khớp với tập nguồn tại thời điểm chốt, không thiếu không trùng, và khi giết tiến trình giữa chừng rồi chạy lại vẫn ra kết quả đó.",
"Dựng API có phân trang trên bảng đang được ghi thêm 100 bản ghi mỗi giây. Nạp bằng phân trang theo số trang, đối soát và ghi lại số bỏ sót. Đổi sang phân trang theo con trỏ, đối soát lại. Giết tiến trình ba lần giữa chừng và chạy lại từ điểm kiểm tra.",
"Dùng phân trang theo số trang trên tập đang thay đổi · lưu điểm kiểm tra trước khi ghi dữ liệu · chạy song song nhiều trang mà không kiểm tra thứ tự con trỏ.",
"Tập đích khớp tuyệt đối với nguồn tại thời điểm chốt, và ba lần giết giữa chừng đều chạy lại ra đúng kết quả đó."),

(36,"Connection pools, load balancers and proxies","LT","Lesson 31",
"Nhóm kết nối giữ sẵn kết nối đã mở để tránh chi phí bắt tay ở lesson 31. Ba tham số và hậu quả khi đặt sai: kích thước tối đa, thời gian sống của kết nối, và thời gian chờ lấy kết nối từ nhóm. Nhóm quá nhỏ làm yêu cầu xếp hàng, nhóm quá lớn làm phía máy chủ hết kết nối, và đây là bài toán giống hệt giới hạn song song ở lesson 12. Kết nối chết trong nhóm: cơ chế một kết nối bị phía kia đóng mà phía này không biết, và cách phát hiện bằng phép kiểm trước khi dùng. Bộ cân bằng tải ở hai tầng và hệ quả khác nhau của từng tầng lên kết nối bền. Vì sao bộ cân bằng tải làm một yêu cầu dài bị ngắt sau thời gian chờ rỗi, một nguyên nhân phổ biến của lỗi kết nối bị đặt lại trong công việc chạy lâu. Máy chủ trung gian và cách nó đổi tiêu đề. Gắn phiên theo máy chủ và vì sao nó thường là dấu hiệu thiết kế có trạng thái.",
"Chọn kích thước nhóm kết nối cho một tải cho trước bằng thực nghiệm, và giải thích vì sao một công việc chạy lâu bị ngắt kết nối giữa chừng.",
"Tầng *phân tích*. Objective gồm một quyết định có số đo và một chẩn đoán. Kiểm bằng bảng thực nghiệm ít nhất bốn kích thước nhóm, cộng một ca công việc dài bị ngắt. Đạt khi chọn được kích thước cho thông lượng cao nhất và giải thích đúng nguyên nhân ca bị ngắt.",
"Chạy một tải truy vấn ở bốn kích thước nhóm kết nối, đo thông lượng và độ trễ phân vị 95. Sau đó dựng một máy chủ trung gian có thời gian chờ rỗi 60 giây, chạy một truy vấn 5 phút, quan sát kết nối bị đặt lại và tìm cách xử lý.",
"Đặt nhóm kết nối lớn cho chắc · không kiểm kết nối trước khi dùng nên gặp kết nối chết · đổ lỗi cho cơ sở dữ liệu khi máy chủ trung gian mới là thứ ngắt.",
"Bảng bốn kích thước nhóm có thông lượng và độ trễ, và ca công việc dài bị ngắt được giải thích đúng nguyên nhân."),

(37,"Latency against throughput, and where data pipelines pay","LT","Lesson 36",
"Hai đại lượng và vì sao tối ưu cái này thường làm xấu cái kia. Độ trễ cộng dồn theo số vòng khứ hồi, nên một pipeline gọi API 10.000 lần tuần tự bị chi phối bởi độ trễ chứ không bởi băng thông, dù tổng dữ liệu nhỏ. Thông lượng bị chi phối bởi băng thông khi chuyển khối lớn. Cách nhận ra mình đang ở chế độ nào: nhân số yêu cầu với độ trễ khứ hồi và so với thời gian chạy thật. Bốn đòn bẩy giảm độ trễ tổng theo thứ tự hiệu quả: gộp nhiều bản ghi vào một yêu cầu, chạy song song, dùng lại kết nối, và đặt máy tính gần nguồn dữ liệu. Vì sao gộp gần như luôn thắng chạy song song khi nguồn có giới hạn tốc độ. Chi phí truyền dữ liệu giữa các vùng và giữa các nhà cung cấp, một khoản đắt bất ngờ ở chặng 7. Độ trễ của lưu trữ đối tượng so với đĩa cục bộ, nối lại lesson 15, và hệ quả lên thiết kế đọc nhiều tệp nhỏ.",
"Xác định một pipeline đang bị chi phối bởi độ trễ hay bởi băng thông, và chọn đòn bẩy phù hợp kèm dự đoán định lượng.",
"Tầng *đánh giá*. Objective đòi chọn giữa các phương án và biện minh bằng số, không có đáp án chung. Kiểm bằng hai pipeline, một mỗi chế độ; đạt khi phân loại đúng cả hai, chọn đòn bẩy phù hợp, và dự đoán cải thiện sai trong phạm vi hệ số hai so với kết quả sau khi áp dụng.",
"Nhận hai pipeline: một gọi API 10.000 lần lấy ít dữ liệu, một tải 50 ghi ga byte trong ít lần gọi. Đo và phân loại từng cái. Chọn đòn bẩy, dự đoán cải thiện, áp dụng, đo lại, so với dự đoán.",
"Tăng băng thông cho pipeline bị chi phối bởi độ trễ · chạy song song trong khi nguồn có giới hạn tốc độ · bỏ qua chi phí truyền dữ liệu giữa các vùng.",
"Phân loại đúng cả hai pipeline, và dự đoán cải thiện sai trong phạm vi hệ số hai so với số đo sau khi áp dụng."),

(38,"Observing the network - ss, tcpdump and reading a capture","TH","Lesson 37",
"Đọc bảng kết nối theo trạng thái và ý nghĩa vận hành của từng trạng thái, nối lại lesson 28. Hàng đợi gửi và hàng đợi nhận: hàng đợi gửi lớn nghĩa là phía kia đọc chậm, hàng đợi nhận lớn nghĩa là ứng dụng của mình đọc chậm, và phân biệt này quyết định sửa ở đâu. Số kết nối ở trạng thái chờ đóng và giới hạn cổng tạm. Bắt gói tin ở mức đủ dùng: lọc theo máy và cổng, lưu ra tệp, và đọc lại. Bốn thứ nhìn ra được từ một bản bắt gói: bắt tay có thành công không, byte đầu tiên về sau bao lâu, có truyền lại không, và ai đóng kết nối trước. Nguyên tắc bảo mật: bản bắt gói chứa dữ liệu thật nên phải xử lý như dữ liệu nhạy cảm, và không bao giờ nộp vào kho mã. Khi nào cần bắt gói và khi nào nhật ký ứng dụng đã đủ, vì bắt gói tốn công và thường không cần.",
"Đọc một bản bắt gói và xác định ai đóng kết nối trước cùng byte đầu tiên về sau bao lâu, rồi kết luận lỗi nằm ở phía khách hay phía máy chủ.",
"Tầng *phân tích*. Objective là rút kết luận từ bằng chứng ở mức gói tin. Kiểm bằng ba bản bắt gói dựng sẵn: một máy chủ đóng trước, một khách hết thời gian chờ, một mất gói gây truyền lại. Đạt khi kết luận đúng cả ba và dẫn được gói cụ thể làm bằng chứng.",
"Dựng ba ca và bắt gói cho từng ca. Đọc lại, với mỗi ca xác định bốn thứ nêu trong bài và kết luận phía nào gây lỗi. Sau đó đọc bảng kết nối của một máy đang chịu tải và phân biệt hàng đợi gửi với hàng đợi nhận.",
"Bắt gói trên mọi giao diện không lọc rồi tệp quá lớn · nộp bản bắt gói có dữ liệu thật vào kho mã · kết luận từ nhật ký ứng dụng khi hai phía nói hai chuyện khác nhau.",
"Kết luận đúng cả ba bản bắt gói với gói cụ thể làm bằng chứng, và phân biệt đúng hai loại hàng đợi trên máy có tải."),

(39,"Building a resilient HTTP loader","TH","Lesson 38",
"Không có cơ chế mới. Bài gộp: ghép mọi thứ từ lesson 33 tới 38 thành một thành phần dùng lại được trong cả chương trình. Danh mục bắt buộc của một ứng dụng khách nạp dữ liệu: bốn loại thời gian chờ, thử lại có nhiễu và ngân sách, cầu dao, khoá bất biến, tự giới hạn tốc độ, nhóm kết nối có kiểm kết nối chết, phân trang theo con trỏ, điểm kiểm tra nạp lại được, nhật ký có định danh yêu cầu, và số đo phát ra ngoài. Tách cấu hình khỏi mã. Kiểm thử một ứng dụng khách mạng mà không phụ thuộc mạng thật: máy chủ giả có thể bơm từng loại lỗi. Vì sao kiểm thử chỉ với đường thuận không chứng minh gì, nối lại nguyên tắc ở lesson 27.",
"Đóng gói một ứng dụng khách HTTP có đủ 10 mục trong danh mục, và chứng minh bằng bộ kiểm thử bơm lỗi rằng nó không mất và không trùng bản ghi.",
"Tầng *sáng tạo*. Objective là thiết kế một thành phần dưới ràng buộc cho trước, không phải làm theo mẫu. Kiểm bằng hai lớp: bộ kiểm thử bơm đủ tám loại lỗi phải xanh, và đối soát 100.000 bản ghi phải khớp tuyệt đối. Thiếu một mục trong danh mục mà vẫn qua kiểm thử thì phải giải thích được vì sao mục đó không cần cho ca này.",
"Đóng gói ứng dụng khách thành một mô đun dùng lại được. Viết bộ kiểm thử với máy chủ giả bơm tám loại lỗi: các mã trạng thái, treo, ngắt giữa chừng, giới hạn tốc độ, lược đồ đổi, và trang trùng. Nạp 100.000 bản ghi, đối soát. Giao mô đun cho học viên khác dùng cho nguồn khác.",
"Kiểm thử bằng cách gọi API thật · gộp cấu hình vào mã · coi bộ kiểm thử xanh ở đường thuận là đủ.",
"Bộ kiểm thử tám loại lỗi xanh, đối soát 100.000 bản ghi khớp tuyệt đối, và học viên khác dùng lại được cho nguồn khác."),
]

M5 = ("Algorithms and Data Structures for Data Work", 40, 49, """| | |
|---|---|
| **Objective cấp module** | Chọn cấu trúc dữ liệu và thuật toán cho một bài toán dữ liệu theo chi phí thật đo được, không theo độ phức tạp tiệm cận một mình |
| **Tiền đề** | M2 |
| **Exit criterion** | Giải năm bài toán dữ liệu kinh điển trên tập lớn hơn bộ nhớ, mỗi bài nêu được độ phức tạp và chi phí thật đã đo |
| **Kỹ năng SFIA** | `PROG` mức 3 |
| **Chế độ hỏng** | Học độ phức tạp tiệm cận như một môn thi, nên chọn cấu trúc theo lý thuyết rồi ngạc nhiên vì mảng thắng danh sách liên kết |""",
"Module không dạy thuật toán cho phỏng vấn. Mọi bài đều gắn với một thao tác dữ liệu thật: khử trùng, lấy N cao nhất, kết bảng, phân trang, và sắp xếp dữ liệu lớn hơn bộ nhớ. Mỗi lựa chọn phải đo, vì hằng số và cục bộ bộ nhớ đệm ở lesson 11 thường lật ngược kết luận từ độ phức tạp tiệm cận.")

L5 = [
(40,"Big-O and why it is not the whole cost","LT","Module 5: M2",
"Độ phức tạp tiệm cận nói tốc độ tăng khi dữ liệu lớn dần, không nói thời gian chạy. Hằng số ẩn và vì sao một thuật toán bậc n log n có hằng số nhỏ thắng một thuật toán bậc n có hằng số lớn trên mọi kích thước thực tế. Cục bộ bộ nhớ đệm là hằng số lớn nhất trong công việc dữ liệu, nối lại lesson 11: duyệt mảng bậc n nhanh hơn duyệt danh sách liên kết bậc n nhiều lần. Phân tích khấu hao và ví dụ mảng động. Độ phức tạp bộ nhớ và đánh đổi giữa thời gian với bộ nhớ. Trường hợp trung bình so với trường hợp xấu nhất, và vì sao trường hợp xấu nhất quan trọng khi dữ liệu do người ngoài kiểm soát. Quy trình chọn: ước lượng bằng độ phức tạp để loại phương án tệ hẳn, rồi đo hai ba phương án còn lại trên dữ liệu thật. Nguyên tắc không tối ưu khi chưa đo, nối lại lesson 17.",
"Dự đoán thứ hạng thời gian chạy của ba cài đặt bằng độ phức tạp, rồi đo và giải thích chỗ dự đoán sai bằng hằng số hoặc cục bộ bộ nhớ đệm.",
"Tầng *phân tích*. Objective đòi giải thích chênh lệch giữa lý thuyết và số đo, không chỉ đo. Kiểm bằng ba cài đặt cùng bài toán ở bốn kích thước dữ liệu; đạt khi có số đo đầy đủ và khi giải thích được ít nhất một chỗ thứ hạng thực tế khác thứ hạng lý thuyết.",
"Cài ba cách tìm phần tử trong tập: quét mảng tuyến tính, tìm nhị phân trên mảng đã sắp, và tra từ điển băm. Dự đoán thứ hạng. Đo ở bốn kích thước từ 100 tới 10 triệu phần tử. Giải thích chỗ quét tuyến tính thắng trên tập nhỏ.",
"Chọn cấu trúc chỉ bằng độ phức tạp tiệm cận · đo một kích thước rồi kết luận · bỏ qua chi phí dựng chỉ mục khi so tra cứu.",
"Có số đo ba cài đặt ở bốn kích thước, và giải thích được ít nhất một chỗ thứ hạng thực tế khác lý thuyết."),

(41,"Arrays, lists and the memory layout that decides speed","TH","Lesson 40",
"Mảng lưu liên tục nên duyệt tuần tự tận dụng dòng bộ nhớ đệm và đọc trước; danh sách liên kết lưu rải rác nên mỗi bước là một lần nhảy bộ nhớ. Hệ quả đo được: duyệt danh sách liên kết chậm hơn duyệt mảng nhiều lần dù cùng bậc. Chèn và xoá: danh sách liên kết rẻ về lý thuyết nhưng tìm tới vị trí đã tốn bậc n. Mảng động và chi phí cấp phát lại, phân tích khấu hao. Bố trí theo dòng so với bố trí theo cột cho một tập bản ghi: cùng dữ liệu, hai bố trí, và phép gộp trên một cột nhanh hơn hẳn ở bố trí theo cột. Đây là nền của định dạng cột ở chặng 7 và của lý do kho phân tích dùng lưu trữ theo cột, nối lại lesson 11. Mảng có kiểu so với mảng đối tượng trong ngôn ngữ động, và hệ số phình ở lesson 13. Lát cắt và bản sao ẩn.",
"Đo chênh lệch giữa bố trí theo dòng và theo cột cho một phép gộp trên một cột, và giải thích bằng dòng bộ nhớ đệm.",
"Tầng *phân tích*. Objective nối một số đo với cơ chế đã học ở lesson 11. Đạt khi có số đo cho cả hai bố trí ở ít nhất ba kích thước, và khi người học ước lượng được số dòng bộ nhớ đệm phải nạp cho mỗi bố trí rồi so với chênh lệch đo được.",
"Lưu một triệu bản ghi 20 cột theo hai bố trí. Gộp trên một cột. Đo cả hai ở ba kích thước. Ước lượng số dòng bộ nhớ đệm phải nạp cho từng bố trí, so với chênh lệch thời gian. Lặp lại với phép lọc nhiều cột và quan sát chênh lệch thu hẹp.",
"Dùng danh sách liên kết vì chèn rẻ mà quên chi phí tìm vị trí · so hai bố trí bằng một phép gộp rồi kết luận cột luôn thắng · quên bản sao ẩn khi cắt lát.",
"Số đo hai bố trí ở ba kích thước, và ước lượng số dòng bộ nhớ đệm nhất quán với chênh lệch đo được."),

(42,"Hash maps - the workhorse, and where they break","TH","Lesson 41",
"Hàm băm, xô, và hệ số tải. Xung đột và hai cách xử lý: nối chuỗi và dò tuyến tính, cùng đặc tính bộ nhớ đệm khác nhau của chúng. Cấp phát lại khi hệ số tải vượt ngưỡng, và vì sao chèn một triệu phần tử có vài lần dừng dài thay vì chậm đều. Khai báo trước dung lượng để tránh cấp phát lại, một tối ưu rẻ và hay bị bỏ qua. Trường hợp xấu nhất bậc n khi khoá bị chọn ác ý hoặc khi hàm băm kém, và hậu quả bảo mật. Chi phí bộ nhớ thật của một từ điển so với dữ liệu thuần, nối lại lesson 13. Khoá phải bất biến và vì sao dùng đối tượng thay đổi được làm khoá là lỗi. Ứng dụng trong công việc dữ liệu: khử trùng theo khoá, kết bảng bằng băm, và đếm giá trị phân biệt. Kết bằng băm: dựng bảng băm từ bảng nhỏ rồi quét bảng lớn, và điều kiện bảng nhỏ phải vừa bộ nhớ, nối tới lesson 44.",
"Cài khử trùng một tập 50 triệu bản ghi bằng bảng băm, đo bộ nhớ đỉnh, và chỉ ra ngưỡng kích thước mà cách này không còn vừa bộ nhớ.",
"Tầng *áp dụng*. Objective gồm một cài đặt và một phép xác định ngưỡng bằng đo. Đạt khi khử trùng đúng so với đáp án và khi ngưỡng nêu ra được kiểm chứng bằng một lần chạy vượt ngưỡng cho thấy tiến trình bị giết vì cạn bộ nhớ.",
"Khử trùng 50 triệu bản ghi bằng từ điển băm. Đo bộ nhớ đỉnh và thời gian, có và không khai báo trước dung lượng. Ước lượng ngưỡng vỡ bộ nhớ, rồi chạy vượt ngưỡng để kiểm chứng. Quan sát các lần dừng do cấp phát lại.",
"Không khai báo trước dung lượng nên cấp phát lại nhiều lần · giả định từ điển luôn vừa bộ nhớ · dùng đối tượng thay đổi được làm khoá.",
"Khử trùng đúng so với đáp án, có số đo bộ nhớ đỉnh, và ngưỡng vỡ bộ nhớ được kiểm chứng bằng một lần chạy thật."),

(43,"Sorting, external sort and why it shows up everywhere","TH","Lesson 42",
"Sắp xếp là nền của nhiều thao tác dữ liệu: khử trùng, kết theo thứ tự, gộp nhóm, và phân trang ổn định. Sắp xếp ổn định và vì sao nó cần khi sắp nhiều khoá lần lượt. Sắp xếp so sánh có cận dưới n log n, và các thuật toán không so sánh vượt cận đó với điều kiện nào. Sắp xếp ngoài bộ nhớ cho dữ liệu lớn hơn RAM: chia thành mảnh vừa bộ nhớ, sắp từng mảnh, ghi ra đĩa, rồi trộn nhiều đường. Số đường trộn và đánh đổi với số lần đọc ghi đĩa. Đây chính là cơ chế công cụ dòng lệnh ở lesson 26 dùng và là cơ chế Spark dùng khi tràn ra đĩa ở chặng 7, nên hiểu ở đây thì ở đó không phải học lại. Ước lượng số byte đọc ghi cho một lần sắp ngoài. Phân trang ổn định cần khoá sắp duy nhất, nếu không thì bản ghi nhảy giữa các trang, nối lại lesson 35.",
"Cài sắp xếp ngoài cho một tệp lớn hơn bộ nhớ và ước lượng số byte đọc ghi trước khi chạy, rồi đo.",
"Tầng *áp dụng*. Objective gồm cài đặt và ước lượng đối chứng. Đạt khi tệp kết quả sắp đúng hoàn toàn, chạy trên máy giới hạn bộ nhớ nhỏ hơn tệp, và ước lượng số byte đọc ghi sai trong phạm vi hệ số hai so với số đo.",
"Sắp một tệp 20 ghi ga byte trên máy giới hạn 2 ghi ga byte bộ nhớ. Ước lượng số byte đọc ghi trước. Cài chia mảnh và trộn nhiều đường. Đo số byte thật. Thử ba số đường trộn khác nhau và so tổng thời gian.",
"Nạp cả tệp rồi bị giết · trộn hai đường nên đọc ghi nhiều lần không cần thiết · phân trang theo khoá không duy nhất nên bản ghi nhảy trang.",
"Tệp kết quả sắp đúng hoàn toàn trên máy có bộ nhớ nhỏ hơn tệp, và ước lượng byte đọc ghi sai trong phạm vi hệ số hai."),

(44,"Join algorithms - nested loop, hash join, sort-merge join","LT","Lesson 43",
"Ba thuật toán kết và điều kiện mỗi cái thắng. Vòng lặp lồng bậc tích hai bảng, chỉ hợp khi một bảng rất nhỏ hoặc có chỉ mục trên bảng trong. Kết bằng băm dựng bảng băm từ bảng nhỏ rồi quét bảng lớn, nhanh nhất khi bảng nhỏ vừa bộ nhớ, và tràn ra đĩa khi không vừa, đây là cơ chế đứng sau tiêu chí ra của M2. Kết trộn sắp yêu cầu cả hai bên đã sắp theo khoá, rẻ khi dữ liệu vốn đã sắp hoặc đã phân vùng theo khoá. Phát tán bảng nhỏ tới mọi nút trong hệ phân tán và ngưỡng kích thước để làm việc đó, nối tới chặng 7. Lệch khoá: một giá trị khoá chiếm phần lớn bản ghi làm một nút hoặc một xô nhận hết việc, và ba cách xử lý. Nhân bản dòng khi khoá không duy nhất ở một bên, nối tới chặng 3. Ước lượng số bản ghi kết quả trước khi chạy từ bản số quan hệ.",
"Chọn thuật toán kết cho ba tình huống có ràng buộc khác nhau và biện minh bằng kích thước bảng, bộ nhớ sẵn có và trạng thái sắp xếp.",
"Tầng *đánh giá*. Objective đòi chọn giữa ba phương án và biện minh, không có đáp án chung. Kiểm bằng ba tình huống cho trước; đạt khi mỗi lựa chọn nêu được điều kiện quyết định và khi dự đoán thuật toán nào nhanh hơn được xác nhận bằng một lần chạy thật cho ít nhất hai tình huống.",
"Cài cả ba thuật toán kết. Chạy trên ba tình huống: bảng nhỏ với bảng lớn vừa bộ nhớ, hai bảng lớn đã sắp, và hai bảng lớn chưa sắp. Đo cả ba thuật toán trên cả ba tình huống, lập bảng chín ô. Tạo lệch khoá và quan sát.",
"Dùng kết bằng băm khi bảng nhỏ không vừa bộ nhớ · bỏ qua lệch khoá nên một xô nhận hết việc · không ước lượng số dòng kết quả trước khi chạy.",
"Bảng chín ô có số đo đầy đủ, và dự đoán thuật toán nhanh hơn đúng cho ít nhất hai trong ba tình huống."),

(45,"Heaps, top-K and streaming selection","TH","Lesson 42",
"Đống nhị phân và hai thao tác cơ bản với chi phí log n. Bài toán lấy N cao nhất từ một luồng: giữ đống kích thước N thay vì sắp toàn bộ, và so sánh chi phí n log N với n log n khi N nhỏ hơn n rất nhiều. Điều kiện cách này thắng và điểm hoà. Hàng đợi ưu tiên cho lập lịch công việc, mẫu dùng lại ở chặng 5. Lấy N cao nhất theo nhóm và cách làm khi số nhóm lớn. Phân vị trên luồng không giữ được toàn bộ dữ liệu: vì sao phân vị chính xác cần toàn bộ dữ liệu, và các cấu trúc tóm tắt cho phân vị xấp xỉ với sai số có cận. Nối tới chặng 4 và 6: chỉ số phân vị 95 trên bảng điều khiển thường là xấp xỉ, và biết nó xấp xỉ là điều kiện để đọc đúng. Đếm giá trị phân biệt xấp xỉ và đánh đổi bộ nhớ với sai số.",
"Cài lấy N cao nhất bằng đống trên một luồng lớn hơn bộ nhớ, và xác định bằng thực nghiệm điểm hoà so với cách sắp toàn bộ.",
"Tầng *áp dụng*. Objective gồm cài đặt và xác định một ngưỡng bằng đo. Đạt khi kết quả đúng so với đáp án và khi điểm hoà nêu ra được xác nhận bằng bảng số đo ở ít nhất bốn giá trị N.",
"Lấy 100 bản ghi lớn nhất từ một luồng 100 triệu bản ghi bằng đống, bộ nhớ giới hạn. So với cách sắp toàn bộ. Chạy ở bốn giá trị N: 10, 1.000, 100.000, 10 triệu. Xác định điểm hoà. Cài thêm phân vị xấp xỉ và đo sai số so với phân vị chính xác.",
"Sắp toàn bộ để lấy 10 phần tử lớn nhất · giữ đống kích thước N khi N gần bằng n · báo cáo phân vị xấp xỉ như phân vị chính xác.",
"Kết quả đúng so với đáp án, và điểm hoà được xác nhận bằng bảng số đo ở bốn giá trị N."),

(46,"Trees, B-trees and why databases use them","LT","Lesson 45",
"Cây tìm kiếm nhị phân và vấn đề mất cân bằng. Cây B và cây B cộng: nút chứa nhiều khoá để mỗi lần đọc nút lấy về một khối đĩa đầy, nên chiều cao cây rất thấp và số lần chạm đĩa ít. Đây là lý do cây B là cấu trúc chỉ mục mặc định của cơ sở dữ liệu quan hệ, và là nền cho chặng 3. Lá nối nhau trong cây B cộng cho phép quét theo khoảng hiệu quả. Chi phí ghi: mỗi lần chèn phải cập nhật chỉ mục, và nhiều chỉ mục nhân chi phí ghi lên, đây là vế thứ hai của tiêu chí ra M2. Tách và gộp nút, và phình chỉ mục. Cây trộn có cấu trúc nhật ký: ghi vào bộ nhớ rồi xả ra đĩa theo tầng, tối ưu cho ghi nhiều, và khuếch đại đọc đổi lấy khuếch đại ghi thấp. Bảng đối chiếu hai họ cấu trúc theo tải ghi nhiều hay đọc nhiều, nền cho việc chọn cơ sở dữ liệu ở chặng 3.",
"Giải thích vì sao thêm chỉ mục làm truy vấn nhanh lên mà làm ghi chậm đi, bằng số lần chạm đĩa cho mỗi thao tác.",
"Tầng *hiểu*. Bài lý thuyết đặt nền cho chặng 3, người học chưa có cơ sở dữ liệu để đo sâu, nên objective dừng ở giải thích bằng cơ chế. Kiểm bằng bài ước lượng số lần chạm đĩa cho bốn thao tác trên cây B với chiều cao cho trước, cộng một thực nghiệm nhỏ. Đạt khi ước lượng đúng cả bốn.",
"Tính chiều cao cây B cho một tỉ khoá với hệ số nhánh cho trước. Ước lượng số lần chạm đĩa cho bốn thao tác: tìm một khoá, quét khoảng, chèn không tách nút, chèn có tách nút. Cài một cây B đơn giản, đếm số lần truy cập nút thật, so với ước lượng.",
"Cho rằng cây nhị phân và cây B khác nhau về độ phức tạp · thêm chỉ mục cho mọi cột · bỏ qua chi phí ghi khi thiết kế chỉ mục.",
"Ước lượng đúng số lần chạm đĩa cho cả bốn thao tác, xác nhận bằng số đếm từ cài đặt thật."),

(47,"Bloom filters, sketches and bounded-error answers","TH","Lesson 42",
"Bộ lọc Bloom trả lời câu hỏi phần tử này có trong tập không với hai tính chất bất đối xứng: không bao giờ báo thiếu, nhưng có thể báo thừa với xác suất tính được. Hệ quả sử dụng: dùng nó để loại nhanh trường hợp chắc chắn không có, rồi mới tra nguồn thật cho phần còn lại. Ba tham số và quan hệ giữa chúng: số phần tử, số bit, tỉ lệ báo thừa. Tính số bit cần cho một tỉ lệ báo thừa mục tiêu. Ba chỗ nó xuất hiện trong hệ dữ liệu: bỏ qua tệp không chứa khoá khi quét, giảm tra cứu tầng dưới trong cây trộn có cấu trúc nhật ký, và lọc trước khi kết phân tán. Cấu trúc tóm tắt cho đếm giá trị phân biệt và cho phân vị, nối lại lesson 45. Nguyên tắc chung của câu trả lời có sai số có cận: phải công bố sai số cùng câu trả lời, nếu không thì người đọc hiểu nhầm là chính xác. Khi nào không được dùng xấp xỉ: đối soát tài chính và kiểm toán.",
"Tính số bit cần cho một tỉ lệ báo thừa mục tiêu, cài bộ lọc Bloom, và đo tỉ lệ báo thừa thật so với lý thuyết.",
"Tầng *áp dụng*. Objective gồm một phép tính và một kiểm chứng bằng thực nghiệm. Đạt khi tỉ lệ báo thừa đo được khớp lý thuyết trong phạm vi sai số thống kê, và khi người học nêu đúng hai tình huống không được dùng xấp xỉ.",
"Tính số bit cho một triệu phần tử với tỉ lệ báo thừa mục tiêu 1%. Cài bộ lọc. Kiểm bằng một triệu truy vấn phần tử không có trong tập, đếm tỉ lệ báo thừa thật. Dùng nó để giảm số lần tra cứu trong một phép kết và đo mức giảm.",
"Tin kết quả báo có mà không tra nguồn thật · đặt số bit theo cảm tính · dùng xấp xỉ cho đối soát tài chính.",
"Tỉ lệ báo thừa đo được khớp lý thuyết trong sai số thống kê, và nêu đúng hai tình huống cấm dùng xấp xỉ."),

(48,"Partitioning, hashing and distributing work","LT","Lesson 44",
"Chia dữ liệu thành phần để xử lý song song, và ba cách chia với đặc tính khác nhau. Chia theo băm khoá cho phân bố đều khi khoá đa dạng, và đảm bảo mọi bản ghi cùng khoá về cùng một phần, điều kiện bắt buộc cho kết và gộp nhóm phân tán. Chia theo khoảng giữ được thứ tự nên quét khoảng rẻ, nhưng lệch khi dữ liệu không đều. Chia vòng tròn cho phân bố đều nhất nhưng không giữ được tính chất nào. Lệch phân vùng: một giá trị khoá chiếm phần lớn bản ghi, triệu chứng là một tác vụ chạy lâu hơn hẳn phần còn lại, và ba cách xử lý gồm thêm hậu tố ngẫu nhiên vào khoá lệch. Băm nhất quán và vì sao nó giảm số bản ghi phải di chuyển khi thêm bớt nút. Xáo trộn dữ liệu giữa các nút là thao tác đắt nhất trong xử lý phân tán, và mọi tối ưu ở chặng 7 đều quy về giảm nó. Số phần bao nhiêu là hợp lý.",
"Chọn cách chia phần cho ba bài toán khác nhau và dự đoán bài nào sẽ bị lệch, rồi kiểm chứng bằng phân bố kích thước phần thật.",
"Tầng *phân tích*. Objective đòi dự đoán lệch từ đặc tính dữ liệu rồi kiểm chứng. Kiểm bằng ba tập dữ liệu có phân bố khoá khác nhau; đạt khi dự đoán đúng tập nào lệch và khi đo được hệ số lệch giữa phần lớn nhất và phần trung vị.",
"Chia ba tập dữ liệu theo ba cách, mỗi tập một phân bố khoá khác nhau gồm một tập có khoá lệch nặng. Đo kích thước từng phần, tính hệ số lệch. Với tập lệch, áp dụng thêm hậu tố ngẫu nhiên và đo lại.",
"Chia theo khoảng trên khoá lệch · chọn số phần bằng số lõi mà không tính tới lệch · quên rằng gộp nhóm phân tán đòi cùng khoá về cùng phần.",
"Dự đoán đúng tập nào lệch, và hệ số lệch đo được giảm sau khi thêm hậu tố ngẫu nhiên."),

(49,"Five classic data problems at scale","TH","Lesson 48",
"Không có cơ chế mới. Bài gộp module: giải năm bài toán kinh điển trên dữ liệu lớn hơn bộ nhớ, mỗi bài dùng ít nhất một cấu trúc hoặc thuật toán đã học. Khử trùng 500 triệu bản ghi. Lấy 1.000 bản ghi lớn nhất theo nhóm. Kết hai bảng 100 triệu dòng trong đó một bảng có khoá lệch. Sắp và phân trang ổn định trên tập đang được ghi thêm. Đếm giá trị phân biệt xấp xỉ với sai số công bố. Với mỗi bài, quy trình bắt buộc: ước lượng độ phức tạp và bộ nhớ, chọn phương án, dự đoán thời gian chạy, chạy, đo bốn số theo lesson 17, và giải thích chênh lệch giữa dự đoán với số đo.",
"Giải năm bài toán trên dữ liệu lớn hơn bộ nhớ, mỗi bài kèm ước lượng trước và số đo sau, và giải thích được mọi chênh lệch quá một bậc độ lớn.",
"Tầng *sáng tạo*. Objective là thiết kế lời giải dưới ràng buộc bộ nhớ, không phải làm theo mẫu. Kiểm hai lớp: kết quả năm bài đúng so với đáp án đối chứng, và báo cáo có ước lượng trước cho cả năm. Đúng kết quả mà không có ước lượng trước thì đạt một nửa, vì mục tiêu module là chọn có căn cứ chứ không phải ra kết quả.",
"Giải năm bài trên máy giới hạn 4 ghi ga byte bộ nhớ với dữ liệu 50 ghi ga byte. Nộp cho mỗi bài: ước lượng, phương án và lý do, dự đoán thời gian, bốn số đo, và phần giải thích chênh lệch.",
"Chạy trước rồi mới ước lượng · chọn phương án theo thói quen mà không xét ràng buộc bộ nhớ · bỏ qua bài có khoá lệch vì nó chạy xong dù chậm.",
"Năm kết quả khớp đáp án đối chứng, có ước lượng trước cho cả năm, và mọi chênh lệch quá một bậc đều giải thích được."),
]
