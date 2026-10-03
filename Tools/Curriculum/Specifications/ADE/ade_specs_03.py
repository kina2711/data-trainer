# -*- coding: utf-8 -*-
"""ADE Phase 3: M7 Software design and delivery + M8 Backend and API engineering."""

M7 = ("Software Design and Delivery", 89, 100, """| | |
|---|---|
| **Objective cấp module** | Xây một kho mã đổi được mà không phá hợp đồng, có chiến lược kiểm thử theo tầng, và có đường phát hành cùng đường lùi đáng tin |
| **Tiền đề** | M1 · M2, cộng M5 và M6 ở mức nền |
| **Exit criterion** | Đồ thị phụ thuộc không có tầng nghiệp vụ phụ thuộc khung hay cơ sở dữ liệu; đổi một bộ chuyển đổi mà phép kiểm lõi không sửa một dòng |
| **Kỹ năng SFIA** | `PROG` mức 4 · `TEST` mức 4 · `CFMG` mức 3 |
| **Chế độ hỏng** | Áp nguyên tắc thiết kế như luật tuyệt đối, chia lớp thật nhiều rồi mã khó đọc hơn; hoặc kiểm thử mô phỏng cả thành phần bên trong nên đổi cấu trúc là phép kiểm đỏ |""",
"""Module này quyết định mã của cả chương trình còn sửa được sau sáu tháng hay không. Nó cũng là nơi đặt ranh giới mà mọi module dữ liệu sau đều dựa vào: lõi nghiệp vụ không biết gì về nơi dữ liệu đến và đi.

Nguyên tắc xuyên suốt: mọi nguyên tắc thiết kế ở đây là **công cụ chẩn đoán**, dùng để phát hiện mã đang khó đổi ở chỗ nào, không phải luật áp lên mọi dòng.""")

L7 = [
(89,"From use case to contract and domain vocabulary","LT","Module 7: M2",
"Bài nối lesson 1 với thiết kế mã: sau khi có phát biểu bài toán thì bước tiếp là đặt tên cho các khái niệm và cố định hợp đồng. Từ vựng miền: dùng đúng từ mà người nghiệp vụ dùng, một khái niệm một tên, và không dịch qua lại giữa hai bộ từ vựng trong cùng một kho mã; mỗi lần dịch là một chỗ có thể sai. Ca sử dụng và tiêu chí chấp nhận theo lesson 1, nay gắn với một tên hàm hoặc một điểm vào cụ thể. Hợp đồng gồm bốn phần: kiểu dữ liệu vào ra, điều kiện trước, điều kiện sau, và hợp đồng lỗi tức hàm này có thể thất bại theo những cách nào. Phần cuối hay bị bỏ và là phần gây nhiều sự cố nhất, vì người gọi không biết phải xử lý gì. Hợp đồng dữ liệu ở đây là hợp đồng trong mã; hợp đồng giữa hai đội ở tầng cao hơn sẽ học ở M14C và M14D.",
"Viết hợp đồng bốn phần cho các điểm vào của một mô đun, với từ vựng khớp từ vựng nghiệp vụ.",
"Tầng *áp dụng*. Bài mở module, nối kỹ năng phát biểu bài toán ở M1 với cấu trúc mã. Kiểm bằng rà soát chéo với người đóng vai nghiệp vụ; đạt khi mọi điểm vào có đủ bốn phần và không có khái niệm nào mang hai tên.",
"Cho mô tả nghiệp vụ một hệ đặt hàng. Rút từ vựng miền thành danh sách thuật ngữ có định nghĩa. Viết hợp đồng bốn phần cho năm điểm vào chính. Đổi bài: một học viên đóng vai người nghiệp vụ đọc và chỉ ra chỗ nào tên trong mã không khớp tên họ dùng.",
"Bỏ hợp đồng lỗi · đặt tên kỹ thuật cho khái niệm nghiệp vụ · một khái niệm mang hai tên ở hai chỗ · viết điều kiện trước mà không kiểm ở đâu cả.",
"Năm điểm vào đều có đủ bốn phần, và người đóng vai nghiệp vụ không tìm được khái niệm nào mang hai tên."),

(90,"Cohesion, coupling and the direction of dependency","LT","Lesson 89",
"Hai đại lượng quyết định mã có sửa được không, và chúng đo được chứ chỉ cảm nhận. Độ gắn kết: các thứ trong một mô đun có cùng lý do thay đổi không. Độ phụ thuộc: đổi mô đun này buộc đổi bao nhiêu mô đun khác. Chiều phụ thuộc là thứ quan trọng nhất và hay bị làm sai: **lõi nghiệp vụ không được phụ thuộc vào khung, cơ sở dữ liệu hay định dạng tệp**, mà ngược lại. Lý do không phải thẩm mỹ mà là khả năng kiểm thử và khả năng thay thế: lõi không biết gì về cơ sở dữ liệu thì kiểm thử lõi không cần cơ sở dữ liệu, và đổi cơ sở dữ liệu không đụng lõi. Đảo ngược phụ thuộc là kỹ thuật đạt điều đó: lõi định nghĩa giao diện nó cần, tầng ngoài cài đặt giao diện đó. Che giấu thông tin: mô đun lộ ra ít nhất có thể, vì mọi thứ lộ ra đều thành hợp đồng mà người khác dựa vào.",
"Vẽ đồ thị phụ thuộc của một kho mã và chỉ ra mọi cạnh đi sai chiều.",
"Tầng *phân tích*. Objective đòi đọc cấu trúc thật và đánh giá nó theo tiêu chí, chứ nhớ định nghĩa. Kiểm bằng bài phân tích hai kho mã; đạt khi vẽ đúng đồ thị và chỉ ra đủ các cạnh sai chiều ở kho có vấn đề.",
"Cho hai kho mã, một có lõi phụ thuộc cơ sở dữ liệu và một đã đảo ngược. Vẽ đồ thị phụ thuộc cho cả hai bằng cách đọc phần nhập mô đun. Chỉ ra cạnh sai chiều. Với kho có vấn đề, đếm số tệp phải sửa nếu đổi cơ sở dữ liệu; làm tương tự với kho kia và so hai con số.",
"Chia lớp theo loại kỹ thuật thay vì theo lý do thay đổi · để lõi nhập thư viện cơ sở dữ liệu · lộ mọi thứ ra ngoài mô đun · đánh giá độ phụ thuộc bằng cảm nhận.",
"Đồ thị phụ thuộc vẽ đúng cho cả hai kho, chỉ đủ cạnh sai chiều, và hai con số tệp phải sửa chênh nhau rõ rệt."),

(91,"Ports and adapters in practice","TH","Lesson 90",
"Bài biến nguyên tắc ở lesson 90 thành cấu trúc thư mục cụ thể. Ba tầng và trách nhiệm: miền chứa quy tắc nghiệp vụ và không nhập gì từ bên ngoài; ứng dụng điều phối các ca sử dụng và định nghĩa cổng tức giao diện nó cần; bộ chuyển đổi cài đặt cổng bằng công nghệ cụ thể. Gốc kết nối là chỗ duy nhất biết cả ba và ghép chúng lại lúc khởi động. Phép thử thật của kiến trúc này không phải sơ đồ đẹp mà là **đổi bộ chuyển đổi mà phép kiểm lõi không sửa một dòng**; nếu phải sửa thì ranh giới đã rò rỉ. Ba dấu hiệu ranh giới rò rỉ: kiểu dữ liệu của thư viện cơ sở dữ liệu xuất hiện trong chữ ký hàm miền, lỗi của thư viện lọt ra ngoài chưa dịch, và cấu trúc bảng lộ nguyên vào tên thuộc tính miền. Cảnh báo về mức độ: kiến trúc này tốn công, và với một script một lần thì nó là thừa.",
"Tái cấu trúc một script thành ba tầng, rồi đổi bộ chuyển đổi lưu trữ mà không sửa phép kiểm lõi.",
"Tầng *áp dụng*. Objective là một phép biến đổi cấu trúc có tiêu chí nghiệm thu khách quan. Kiểm bằng phép thử đổi bộ chuyển đổi; đạt khi phép kiểm lõi không sửa dòng nào và vẫn xanh.",
"Tái cấu trúc công cụ nạp CSV ở lesson 32 thành ba tầng. Viết phép kiểm cho tầng miền không dùng tệp và không dùng cơ sở dữ liệu. Thay bộ chuyển đổi từ tệp sang PostgreSQL. Chứng minh phép kiểm lõi không sửa dòng nào. Đếm số tệp phải sửa cho lần thay đó.",
"Cho kiểu dữ liệu của thư viện lọt vào tầng miền · gọi thẳng cơ sở dữ liệu từ miền · dựng ba tầng cho một script dùng một lần · để lỗi thư viện lan ra ngoài chưa dịch.",
"Phép kiểm lõi không sửa dòng nào và vẫn xanh sau khi đổi bộ chuyển đổi, và tầng miền không nhập thư viện ngoài nào."),

(92,"Error design - expected failure against defect","TH","Lesson 91",
"Phân biệt quan trọng nhất trong thiết kế lỗi và cũng là phân biệt hay bị bỏ: thất bại dự kiến là phần của hợp đồng và người gọi phải xử lý; khiếm khuyết là lỗi lập trình và không nên bắt để chạy tiếp. Ví dụ với dữ liệu: tệp nguồn thiếu cột là thất bại dự kiến, còn chỉ số mảng vượt biên là khiếm khuyết. Hệ quả: bắt hết mọi ngoại lệ rồi ghi nhật ký và chạy tiếp là biến khiếm khuyết thành dữ liệu sai âm thầm. Phân loại thứ hai độc lập với phân loại trên và quyết định hành vi vận hành: lỗi thử lại được và lỗi vĩnh viễn, theo đúng phân loại ở lesson 30. Truyền ngữ cảnh: lỗi đi lên phải mang theo đủ thông tin để chẩn đoán mà không cần chạy lại, tức là dòng nào, tệp nào, giá trị nào. Dịch lỗi ở ranh giới theo lesson 15, nay đặt vào đúng tầng của kiến trúc ba tầng.",
"Phân loại lỗi theo hai trục và cài đặt cách xử lý đúng cho từng ô, chứng minh bằng thí nghiệm tiêm lỗi.",
"Tầng *áp dụng*. Objective là một thiết kế có bốn trường hợp kiểm được riêng. Kiểm bằng bốn loại lỗi tiêm; đạt khi cả bốn đi đúng đường và khiếm khuyết không bị nuốt.",
"Lập bảng hai trục cho mười lỗi có thể xảy ra trong pipeline nạp dữ liệu. Cài đặt xử lý cho từng ô. Tiêm bốn lỗi đại diện bốn ô và chứng minh đường đi đúng: thất bại dự kiến thử lại được thì thử lại, vĩnh viễn thì vào vùng cách ly, còn khiếm khuyết thì dừng và lộ ra.",
"Bắt mọi ngoại lệ rồi chạy tiếp · thử lại một lỗi dữ liệu vĩnh viễn · để lỗi lên tới tầng trên mà mất ngữ cảnh · coi mọi lỗi là thất bại dự kiến.",
"Bảng mười lỗi phân loại đủ hai trục, và bốn lỗi tiêm đều đi đúng đường với khiếm khuyết không bị nuốt."),

(93,"The test pyramid and where to place a double","TH","Lesson 92",
"Bài này chi tiết hoá lesson 19 bằng câu hỏi đặt phép kiểm ở tầng nào. Hình tháp hay hình thoi: nhiều phép kiểm nhanh ở dưới, ít phép kiểm chậm ở trên; với mã dữ liệu thì tầng tích hợp thường dày hơn hình tháp kinh điển vì phần lớn lỗi nằm ở chỗ ghép với cơ sở dữ liệu và định dạng tệp. Quy tắc đặt bộ thay thế và đây là quy tắc quan trọng nhất của bài: **chỉ thay thế ở ranh giới mình không sở hữu**, tức hệ ngoài; thay thế thành phần bên trong là tự kiểm mã giả của mình và làm mọi lần tái cấu trúc thành phép kiểm đỏ. Bộ dựng dữ liệu kiểm thử để phép kiểm đọc được và không lặp. Tính xác định theo lesson 19. Phép kiểm đặc tả dùng khi tái cấu trúc mã cũ chưa có phép kiểm: ghi lại hành vi hiện tại làm mốc trước khi sửa, kể cả hành vi đó có vẻ sai.",
"Đặt đúng tầng cho mười phép kiểm và chứng minh bộ kiểm không đỏ khi tái cấu trúc mà hành vi không đổi.",
"Tầng *đánh giá*. Objective đòi phán đoán về vị trí và phạm vi phép kiểm, chỗ hay làm sai theo hướng tốn kém. Kiểm bằng phép thử tái cấu trúc; đạt khi bộ kiểm vẫn xanh sau khi đổi cấu trúc nội bộ mà không sửa phép kiểm nào.",
"Cho mười tình huống cần kiểm. Đặt mỗi cái vào một tầng và nêu có dùng bộ thay thế không, ở ranh giới nào. Cài đặt chúng. Sau đó tái cấu trúc nội bộ một mô đun mà giữ nguyên hành vi, và chứng minh không phép kiểm nào phải sửa.",
"Thay thế thành phần bên trong · viết phép kiểm đầu cuối cho mọi thứ vì thấy chắc chắn hơn · bỏ tầng tích hợp vì chậm · tái cấu trúc mã cũ mà không có phép kiểm đặc tả.",
"Mười phép kiểm đặt đúng tầng, và sau khi tái cấu trúc nội bộ thì bộ kiểm xanh mà không sửa phép kiểm nào."),

(94,"Contract testing between a producer and a consumer","TH","Lesson 93",
"Khi hai thành phần do hai người hoặc hai đội viết, phép kiểm của mỗi bên không phát hiện được việc hai bên hiểu khác nhau về giao diện. Phép kiểm hợp đồng giải đúng chỗ đó: bên tiêu thụ khai báo nó cần gì, bên cung cấp chạy phép kiểm chứng minh nó đáp ứng, và hợp đồng đó nằm trong quy trình tích hợp liên tục của cả hai. Khác với phép kiểm đầu cuối: hợp đồng chạy nhanh, không cần dựng cả hệ, và chỉ ra chính xác trường nào không khớp. Thay đổi phá vỡ và thay đổi tương thích: thêm trường tuỳ chọn thì an toàn, xoá trường bắt buộc hoặc đổi kiểu thì không; đây là cùng bộ quy tắc sẽ gặp ở M14D khi nói về sổ đăng ký lược đồ. Quy trình đổi hợp đồng an toàn theo hai giai đoạn. Vì sao bài này quan trọng với người làm dữ liệu: mọi nguồn dữ liệu là một bên cung cấp, và không có hợp đồng thì họ đổi lược đồ lúc nào ta hỏng lúc đó.",
"Dựng phép kiểm hợp đồng giữa hai thành phần và chứng minh nó bắt được thay đổi phá vỡ trước khi triển khai.",
"Tầng *áp dụng*. Objective là một cơ chế kiểm được bằng thí nghiệm đổi lược đồ. Kiểm bằng ba thay đổi; đạt khi phép kiểm hợp đồng chặn đúng thay đổi phá vỡ và cho qua thay đổi tương thích.",
"Dựng một bên cung cấp và một bên tiêu thụ. Viết hợp đồng từ phía tiêu thụ và đưa vào quy trình của bên cung cấp. Thực hiện ba thay đổi: thêm trường tuỳ chọn, xoá trường bắt buộc, và đổi kiểu. Ghi lại phép kiểm hợp đồng phản ứng thế nào với từng cái. Thực hiện thay đổi phá vỡ theo quy trình hai giai đoạn mà không làm bên tiêu thụ lỗi.",
"Dùng phép kiểm đầu cuối thay cho hợp đồng · viết hợp đồng từ phía cung cấp nên nó chỉ mô tả cái đang có · đổi lược đồ rồi mới báo bên tiêu thụ.",
"Phép kiểm hợp đồng chặn đúng thay đổi phá vỡ, cho qua thay đổi tương thích, và quy trình hai giai đoạn hoàn tất không gây lỗi."),

(95,"Refactoring in small behaviour-preserving steps","TH","Lesson 94",
"Tái cấu trúc là đổi cấu trúc mà giữ nguyên hành vi, và hai chữ cuối là phần khó. Quy trình an toàn: có phép kiểm phủ hành vi hiện tại trước, đổi một bước nhỏ, chạy phép kiểm, nộp; lặp lại. Bước nhỏ nghĩa là mỗi lần đổi vẫn chạy được, chứ đập ra rồi dựng lại trong ba ngày. Với mã cũ chưa có phép kiểm thì dùng phép kiểm đặc tả ở lesson 93 để chốt hành vi hiện tại trước, kể cả hành vi có vẻ sai; sửa cái sai là một thay đổi riêng và phải nộp riêng. Các mẫu tái cấu trúc phổ biến dùng như công cụ chứ mục tiêu: **đưa vào một mẫu khi nó giải một sức ép có thật trong mã**, chứ vì mẫu đó nổi tiếng. Ba dấu hiệu mã cần tái cấu trúc và ba dấu hiệu đang tái cấu trúc quá đà. Cách tách tái cấu trúc khỏi sửa lỗi trong lịch sử Git để rà soát được, nối lại kỷ luật commit ở lesson 7.",
"Tái cấu trúc một mô đun rối bằng các bước nhỏ, mỗi bước chạy được và có phép kiểm xanh.",
"Tầng *áp dụng*. Objective đòi kỷ luật quy trình chứ kiến thức mới. Kiểm bằng lịch sử Git cộng bộ kiểm; đạt khi mọi commit đều chạy được và bộ kiểm xanh, và hành vi cuối giống hành vi đầu.",
"Nhận một mô đun 300 dòng không có phép kiểm. Viết phép kiểm đặc tả chốt hành vi hiện tại. Tái cấu trúc thành ba tầng theo lesson 91 bằng ít nhất sáu bước nhỏ, mỗi bước một commit chạy được. Chứng minh hành vi đầu ra không đổi trên cùng bộ dữ liệu.",
"Đập ra viết lại từ đầu · trộn sửa lỗi vào commit tái cấu trúc · tái cấu trúc khi chưa có phép kiểm nào · đưa mẫu thiết kế vào vì thấy hay.",
"Mọi commit đều chạy được với bộ kiểm xanh, và đầu ra trên bộ dữ liệu chuẩn khớp tuyệt đối với bản gốc."),

(96,"Static analysis, dependency and security scanning","TH","Lesson 95",
"Bốn loại kiểm tự động chạy trước khi mã tới tay người rà soát, để người rà soát dành thời gian cho phần máy không làm được. Định dạng tự động: chấm dứt tranh luận phong cách bằng một công cụ, không bàn nữa. Soát lỗi tĩnh: bắt lỗi thật như biến chưa dùng, so sánh luôn đúng, hoặc tài nguyên chưa đóng. Kiểm kiểu theo lesson 18. Quét phụ thuộc: thư viện có lỗ hổng đã công bố, và đây là loại rủi ro mà đội tự viết mã tốt vẫn dính. Quét bí mật cả lịch sử kho theo lesson 31. Ngưỡng chặn phải quyết trước chứ tuỳ hứng: mức nào chặn hợp nhất, mức nào chỉ cảnh báo; không đặt ngưỡng thì hoặc chặn mọi thứ rồi bị tắt, hoặc không chặn gì. Danh mục thành phần phần mềm ở mức nhận biết: biết mình đang chạy những thư viện nào là điều kiện để phản ứng khi có lỗ hổng mới công bố.",
"Dựng bộ kiểm tự động bốn loại với ngưỡng chặn rõ, và chứng minh nó bắt được lỗi ở cả bốn loại.",
"Tầng *áp dụng*. Objective là một cấu hình có tiêu chí nghiệm thu bằng phép thử tiêm. Kiểm bằng bốn vi phạm tiêm; đạt khi cả bốn bị chặn ở đúng bước và ngưỡng chặn được ghi lại thành tài liệu.",
"Thêm bốn loại kiểm vào quy trình ở lesson 31. Đặt ngưỡng chặn và ghi thành tài liệu ngắn. Tiêm bốn vi phạm: sai định dạng, một lỗi soát tĩnh thật, một thư viện có lỗ hổng đã biết, và một bí mật trong lịch sử. Chứng minh cả bốn bị chặn. Sinh danh mục thành phần và đọc nó.",
"Bật mọi luật rồi bị tắt vì quá ồn · chỉ quét mã hiện tại · không đặt ngưỡng chặn · coi quét phụ thuộc là việc làm một lần.",
"Bốn vi phạm đều bị chặn ở đúng bước, và tài liệu ngưỡng chặn nêu rõ mức nào chặn mức nào cảnh báo."),

(97,"Release - artifacts, versions and migration compatibility","TH","Lesson 96",
"Phát hành là chỗ mã gặp người dùng, và ba nguyên tắc quyết định nó có an toàn không. Sản phẩm dựng bất biến: dựng một lần, cùng một sản phẩm đó đi qua mọi môi trường; dựng lại cho từng môi trường là cách để môi trường sản xuất chạy thứ chưa ai kiểm. Đánh số phiên bản theo ngữ nghĩa và ý nghĩa với người dùng theo lesson 17. Tương thích khi di trú là phần khó nhất với hệ có dữ liệu: **mã mới phải chạy được với lược đồ cũ, và mã cũ phải chạy được với lược đồ mới**, ít nhất trong một cửa sổ, vì lúc triển khai thì hai phiên bản cùng chạy. Từ đó suy ra quy tắc đổi lược đồ hai giai đoạn: thêm trước, chuyển dữ liệu, đổi mã, rồi mới xoá cái cũ; gộp lại một bước là gây gián đoạn. Nhật ký thay đổi viết cho người dùng chứ chép lại danh sách commit.",
"Thực hiện một thay đổi lược đồ phá vỡ theo quy trình hai giai đoạn mà không gây gián đoạn.",
"Tầng *áp dụng*. Objective là một quy trình có tiêu chí nghiệm thu bằng việc dịch vụ không lỗi trong suốt quá trình. Kiểm bằng thí nghiệm triển khai có tải; đạt khi không yêu cầu nào thất bại và cả hai phiên bản cùng chạy được.",
"Dựng dịch vụ đọc ghi một bảng. Cần đổi tên một cột. Thực hiện theo hai giai đoạn trong lúc có tải liên tục: thêm cột mới, ghi cả hai, chuyển dữ liệu, đổi mã đọc, rồi xoá cột cũ. Ở mỗi bước, chạy đồng thời cả phiên bản cũ lẫn mới và đếm số yêu cầu thất bại.",
"Đổi tên cột trong một bước · dựng lại sản phẩm cho từng môi trường · xoá cột cũ ngay sau khi đổi mã · viết nhật ký thay đổi bằng danh sách commit.",
"Không yêu cầu nào thất bại qua toàn bộ quá trình, và cả hai phiên bản cùng chạy được ở mọi bước trung gian."),

(98,"Deployment strategies and rollback","TH","Lesson 97",
"Bốn cách đưa phiên bản mới ra và đánh đổi của từng cách. Thay thế tại chỗ: đơn giản, có gián đoạn, lùi lại chậm. Xanh và lam: chạy song song hai môi trường rồi chuyển lưu lượng, lùi lại tức thì nhưng tốn gấp đôi tài nguyên. Phát hành dần: đưa phiên bản mới cho một phần nhỏ người dùng, quan sát chỉ số, rồi mở rộng; đây là cách an toàn nhất và cũng đòi khả năng quan sát tốt nhất. Cờ tính năng: tách việc triển khai mã khỏi việc bật tính năng, nên lùi một tính năng không cần triển khai lại. Điều kiện để mọi cách trên hoạt động với hệ có dữ liệu: tương thích hai chiều theo lesson 97, vì lùi mã mà lược đồ đã đổi một chiều thì không lùi được. **Lùi lại phải được diễn tập chứ chỉ viết trong tài liệu**, và bài lab này chính là buổi diễn tập đó.",
"Chọn chiến lược triển khai cho một ràng buộc cho trước và diễn tập được một lần lùi thành công.",
"Tầng *đánh giá*. Objective đòi chọn theo ràng buộc tài nguyên và rủi ro, rồi chứng minh bằng diễn tập. Kiểm bằng bài chọn cộng diễn tập lùi; đạt khi chọn đúng ba tình huống và lùi hoàn tất trong hạn đã đặt.",
"Cho ba tình huống có ràng buộc khác nhau về tài nguyên, rủi ro và khả năng quan sát. Chọn chiến lược cho từng cái kèm lý do. Triển khai một phiên bản có lỗi bằng cách phát hành dần, phát hiện qua chỉ số, và lùi lại. Đo thời gian từ lúc triển khai tới lúc lùi xong.",
"Chọn phát hành dần mà không có chỉ số để quan sát · lùi mã khi lược đồ đã đổi một chiều · chưa bao giờ diễn tập lùi · dùng cờ tính năng rồi không bao giờ dọn.",
"Chọn đúng chiến lược cho cả ba tình huống, và diễn tập lùi hoàn tất trong hạn với số đo thời gian."),

(99,"Monolith, modular monolith and the cost of splitting","LT","Lesson 98",
"Bài chống lại một xu hướng tốn kém: chia nhỏ dịch vụ khi chưa cần. Ba dạng và điều kiện phù hợp. Khối đơn: một kho mã một sản phẩm triển khai, đơn giản nhất, và đủ cho phần lớn hệ dữ liệu ở quy mô vừa. Khối đơn có mô đun: vẫn một sản phẩm triển khai nhưng ranh giới mô đun được cưỡng chế, nên giữ được tính đơn giản vận hành mà vẫn sửa được; đây là lựa chọn mặc định đúng cho phần lớn đội. Nhiều dịch vụ: mỗi phần triển khai riêng, chia được theo đội và theo tải, đổi lại **thuế vận hành rất lớn** gồm mạng giữa các dịch vụ, dữ liệu phân tán, theo vết xuyên dịch vụ, và triển khai phối hợp. Ba điều kiện cần trước khi tách và ba dấu hiệu tách quá sớm. Sở hữu dữ liệu là ranh giới thật: hai dịch vụ cùng ghi một bảng thì chúng chưa thật sự tách.",
"Quyết định có nên tách dịch vụ hay không cho một tình huống cho trước và nêu điều kiện kích hoạt việc tách sau này.",
"Tầng *đánh giá*. Objective đòi cân chi phí vận hành với lợi ích tổ chức, chứ theo xu hướng. Kiểm bằng ba tình huống trong đó ít nhất hai không nên tách; đạt khi quyết định đúng cả ba và nêu điều kiện kích hoạt kiểm được.",
"Cho ba tình huống khác nhau về quy mô đội, tải và ranh giới nghiệp vụ. Quyết định dạng kiến trúc cho từng cái. Viết một tài liệu quyết định theo lesson 3 chọn khối đơn có mô đun cho một trong ba, nêu rõ ba điều kiện kích hoạt việc tách về sau.",
"Tách dịch vụ vì nghe hiện đại · để hai dịch vụ cùng ghi một bảng rồi gọi là đã tách · bỏ qua thuế vận hành khi so · viết điều kiện kích hoạt chung chung.",
"Quyết định đúng cả ba tình huống, và tài liệu quyết định nêu được ba điều kiện kích hoạt kiểm được."),

(100,"Delivery project - a modular package with a release path","DA","Lesson 99",
"Bài dự án khép module. Nâng công cụ ở lesson 32 thành một sản phẩm có kiến trúc và có đường phát hành. Danh mục kiểm tám điểm: ba tầng với đồ thị phụ thuộc không có cạnh sai chiều; hợp đồng bốn phần cho mọi điểm vào công khai; thiết kế lỗi hai trục; bộ kiểm đủ bốn tầng không mô phỏng thành phần bên trong; phép kiểm hợp đồng với một bên tiêu thụ; quy trình tự động bốn loại kiểm có ngưỡng chặn; sản phẩm dựng bất biến có đánh số phiên bản; và một lần di trú lược đồ hai giai đoạn đã diễn tập. Phép thử nghiệm thu gồm hai phần: đổi bộ chuyển đổi lưu trữ mà phép kiểm lõi không sửa dòng nào; và triển khai một phiên bản có lỗi rồi lùi lại trong hạn đã đặt. Nộp kèm một tài liệu quyết định cho lựa chọn kiến trúc, theo lesson 99.",
"Nộp một sản phẩm đạt tám điểm danh mục kiểm và qua được hai phép thử nghiệm thu.",
"Tầng *sáng tạo*. Bài tổng hợp toàn module thành một sản phẩm có kiến trúc và quy trình phát hành. Kiểm bằng hai phép thử cộng rà soát danh mục; đạt khi cả tám điểm có bằng chứng và cả hai phép thử qua.",
"Nâng công cụ thành sản phẩm đạt tám điểm. Nộp bảng danh mục kiểm, mỗi điểm dẫn tới tệp hoặc số đo. Thực hiện phép thử đổi bộ chuyển đổi và phép thử lùi. Nộp tài liệu quyết định kiến trúc.",
"Dựng ba tầng cho phần không cần · mô phỏng thành phần bên trong nên phép kiểm đỏ khi tái cấu trúc · bỏ phép thử lùi vì tốn thời gian · dẫn bằng chứng chung chung.",
"Tám điểm đều dẫn được tới tệp hoặc số đo, đổi bộ chuyển đổi không sửa phép kiểm lõi, và lùi hoàn tất trong hạn."),
]

M8 = ("Backend and API Engineering", 101, 112, """| | |
|---|---|
| **Objective cấp module** | Vận hành đúng một giao diện lập trình web có trạng thái dưới ràng buộc đồng thời, sự cố và bảo mật |
| **Tiền đề** | M5 · M6 · M7 |
| **Exit criterion** | Không sinh tác động kép khi máy khách thử lại trong hợp đồng đã định; bất biến giao dịch được kiểm bằng phép chạy song song; có mô hình mối đe doạ và sổ tay chẩn đoán |
| **Kỹ năng SFIA** | `PROG` mức 4 · `SYSP` mức 4 · `TEST` mức 4 |
| **Chế độ hỏng** | Xây giao diện chạy đúng khi gọi lần lượt rồi hỏng khi có hai máy khách gọi cùng lúc, vì ranh giới giao dịch và khoá bất biến chưa được thiết kế |""",
"""Module này là module cuối trước khi vào tầng dữ liệu, và nó là nơi người học lần đầu chịu trách nhiệm về một hệ có trạng thái dưới tải thật.

**Ghi chú về phụ thuộc.** Hợp đồng nguồn nêu module này cần SQL cơ bản và cho phép học song song phần đầu của M9. Ở đây SQL chỉ dùng ở mức đọc ghi và giao dịch; phần kế hoạch thực thi, chỉ mục và tối ưu thuộc M9 và M10, nên bài 95 chỉ dùng giao dịch chứ chưa đòi đọc kế hoạch.

Dự án của module là một giao diện điều khiển công việc, và nó được dùng lại làm nguồn dữ liệu cho pipeline tham chiếu từ M14B trở đi.""")

L8 = [
(101,"The request lifecycle end to end","LT","Module 8: M7",
"Bài mở module bằng cách nối mọi thứ đã học ở M5 và M6 thành một đường đi duy nhất: socket nhận kết nối, máy chủ phân luồng, bộ định tuyến chọn hàm xử lý, các lớp trung gian chạy trước và sau, hàm xử lý gọi tầng ứng dụng, tầng ứng dụng gọi kho dữ liệu, rồi phản hồi đi ngược lại. Mỗi chặng có một hạn chờ và một chỗ có thể hỏng, và vẽ được đường này là điều kiện để chẩn đoán về sau. Ba mô hình xử lý đồng thời của máy chủ và hệ quả: một tiến trình nhiều luồng, nhiều tiến trình, và vòng lặp sự kiện; chọn theo đúng quy tắc ở lesson 29. Lớp trung gian làm gì và thứ tự chạy của chúng quan trọng ra sao, đặc biệt lớp ghi nhật ký và lớp xác thực. Điểm kiểm sức khoẻ và điểm kiểm sẵn sàng là hai thứ khác nhau, theo phân biệt đã nêu ở lesson 82.",
"Vẽ đường đi của một yêu cầu qua bảy chặng và chỉ ra hạn chờ cùng chế độ hỏng của từng chặng.",
"Tầng *hiểu*. Bài mở module, tổng hợp kiến thức đã có thành một bản đồ. Kiểm bằng bài vẽ có chú thích; đạt khi đủ bảy chặng, mỗi chặng có hạn chờ và ít nhất một chế độ hỏng.",
"Dựng một dịch vụ tối thiểu có lớp trung gian ghi nhật ký. Gửi một yêu cầu và ghi lại dấu thời gian ở từng chặng bằng nhật ký có mã theo dõi. Vẽ đường đi có chú thích hạn chờ và chế độ hỏng. Phân biệt điểm kiểm sức khoẻ với điểm kiểm sẵn sàng bằng cách ngắt kết nối cơ sở dữ liệu và xem cái nào đổi trạng thái.",
"Vẽ sơ đồ mà bỏ qua lớp trung gian · dùng một điểm kiểm cho cả hai mục đích · không đặt hạn chờ ở chặng gọi cơ sở dữ liệu.",
"Sơ đồ đủ bảy chặng với hạn chờ và chế độ hỏng, và hai điểm kiểm phản ứng khác nhau khi mất kết nối cơ sở dữ liệu."),

(102,"API contract - resources, errors and versioning","TH","Lesson 101",
"Hợp đồng của giao diện là thứ người khác dựa vào, nên đổi nó là đổi thứ ngoài tầm kiểm soát của mình. Tài nguyên và đường dẫn: đặt tên theo danh từ nghiệp vụ, theo từ vựng miền ở lesson 89. Ngữ nghĩa phương thức và tính bất biến theo lesson 81, nay là quyết định thiết kế chứ chỉ kiến thức. Xác thực đầu vào ở ranh giới theo lesson 18, và trả lỗi nêu rõ trường nào sai chứ một thông báo chung. Phong bì lỗi thống nhất: mã lỗi ổn định cho máy đọc, thông điệp cho người đọc, và mã theo dõi để đối chiếu nhật ký. Phân trang, lọc và sắp xếp: ba kiểu phân trang và vì sao phân trang theo con trỏ an toàn hơn theo số trang khi dữ liệu đang đổi, nối lại lesson 84. Đánh phiên bản: ba cách và đánh đổi; nguyên tắc chung là **thêm thì được, bớt và đổi kiểu thì cần phiên bản mới**, cùng bộ quy tắc với lesson 94.",
"Thiết kế hợp đồng cho một tài nguyên có phân trang và phong bì lỗi thống nhất, và chứng minh hợp đồng ổn định khi thêm trường.",
"Tầng *áp dụng*. Objective là một thiết kế có tiêu chí nghiệm thu bằng phép kiểm hợp đồng ở lesson 94. Kiểm bằng ba thay đổi hợp đồng; đạt khi thêm trường không làm bên tiêu thụ lỗi và hai thay đổi phá vỡ bị phép kiểm chặn.",
"Thiết kế và cài giao diện cho tài nguyên công việc: tạo, xem, liệt kê có phân trang theo con trỏ, và huỷ. Viết đặc tả giao diện. Dựng phép kiểm hợp đồng từ phía một máy khách. Thực hiện ba thay đổi và ghi phản ứng của phép kiểm. Chèn bản ghi mới giữa lúc phân trang và chứng minh không trùng không sót.",
"Phân trang theo số trang · phong bì lỗi mỗi chỗ một kiểu · trả mã trạng thái chung cho mọi lỗi · đổi kiểu một trường mà giữ nguyên phiên bản.",
"Phân trang theo con trỏ không trùng không sót khi dữ liệu đổi, và ba thay đổi hợp đồng cho phản ứng đúng như thiết kế."),

(103,"Transaction boundaries and the unit of work","TH","Lesson 102",
"Ranh giới giao dịch là quyết định thiết kế chứ chi tiết cài đặt, và đặt sai là nguồn của dữ liệu không nhất quán. Nguyên tắc: **một ca sử dụng là một giao dịch**, mở ở tầng ứng dụng chứ ở tầng kho dữ liệu, vì tầng kho không biết ca sử dụng gồm mấy thao tác. Ba lỗi hay gặp: mỗi thao tác một giao dịch nên nửa chừng lỗi thì dữ liệu dở dang; giữ giao dịch mở trong lúc gọi hệ ngoài nên khoá bị giữ rất lâu; và gọi hệ ngoài bên trong giao dịch rồi giao dịch lùi mà tác động bên ngoài không lùi được. Lỗi thứ ba là bài toán hai hệ và lời giải của nó là mẫu hộp thư đi, đặt ở lesson 109. Hồ kết nối và quan hệ với ranh giới giao dịch: giao dịch giữ một kết nối, nên giao dịch dài làm cạn hồ, và triệu chứng là yêu cầu xếp hàng chờ kết nối chứ chờ cơ sở dữ liệu. Vấn đề truy vấn lặp và cách phát hiện bằng đếm số truy vấn cho mỗi yêu cầu.",
"Đặt đúng ranh giới giao dịch cho ba ca sử dụng và chứng minh không còn trạng thái dở dang khi lỗi giữa chừng.",
"Tầng *áp dụng*. Objective là một quyết định thiết kế kiểm được bằng thí nghiệm lỗi giữa chừng. Kiểm bằng ba ca sử dụng có tiêm lỗi; đạt khi không ca nào để lại trạng thái dở dang và số truy vấn cho mỗi yêu cầu nằm trong ngưỡng.",
"Cài ba ca sử dụng, mỗi cái ghi nhiều bảng. Tiêm lỗi ở giữa và đối soát để chứng minh không dở dang. Đếm số truy vấn cho mỗi yêu cầu và phát hiện truy vấn lặp, rồi sửa. Giữ một giao dịch mở trong lúc gọi hệ ngoài chậm và quan sát hồ kết nối cạn.",
"Mở giao dịch ở tầng kho dữ liệu · gọi hệ ngoài trong giao dịch · giữ giao dịch qua nhiều bước chờ người dùng · không đếm số truy vấn mỗi yêu cầu.",
"Ba ca sử dụng không để lại trạng thái dở dang khi lỗi, số truy vấn mỗi yêu cầu trong ngưỡng, và tái hiện được hồ kết nối cạn."),

(104,"Concurrency control - optimistic and pessimistic","TH","Lesson 103",
"Hai máy khách cùng sửa một bản ghi là tình huống bình thường, và không xử lý thì một bản cập nhật biến mất mà không ai biết. Cập nhật mất là chế độ hỏng cụ thể: cả hai đọc giá trị cũ, cả hai ghi, bản ghi sau đè bản trước. Hai cách chống và điều kiện dùng. Khoá lạc quan: mỗi bản ghi có số phiên bản, khi ghi thì kiểm phiên bản còn như lúc đọc không, khác thì từ chối và báo máy khách thử lại; hợp khi xung đột hiếm. Khoá bi quan: khoá bản ghi lúc đọc, giữ tới khi ghi xong; hợp khi xung đột nhiều, đổi lại giảm đồng thời và có nguy cơ khoá chết theo lesson 70. Mức cô lập giao dịch ở mức đủ dùng, phần chi tiết thuộc M10. Cách kiểm thử: phép kiểm tuần tự **không bao giờ** phát hiện được lỗi loại này, nên bắt buộc phải có phép kiểm chạy song song thật.",
"Chống được cập nhật mất bằng một trong hai cơ chế và chứng minh bằng phép kiểm chạy song song.",
"Tầng *áp dụng*. Objective là một cơ chế chỉ kiểm được bằng phép chạy song song, điểm mà phép kiểm thông thường bỏ sót. Kiểm bằng 1000 lần ghi đồng thời; đạt khi không có cập nhật nào bị mất và số lần từ chối khớp số xung đột thật.",
"Cài một điểm cập nhật không có kiểm soát đồng thời. Viết phép kiểm chạy 50 luồng cùng cập nhật và chứng minh có cập nhật bị mất. Cài khoá lạc quan và chạy lại. Cài khoá bi quan và chạy lại. So thông lượng hai cách ở hai mức tỉ lệ xung đột khác nhau.",
"Chỉ kiểm tuần tự rồi kết luận đúng · dùng khoá bi quan cho mọi thứ · trả lỗi xung đột mà không nói máy khách phải làm gì · giữ khoá qua nhiều yêu cầu.",
"Bản chưa sửa mất cập nhật có số chứng minh, cả hai cơ chế đều cho 0 cập nhật mất qua 1000 lần, và có bảng so thông lượng."),

(105,"Idempotency keys and deduplication state","TH","Lesson 104",
"Máy khách thử lại là chuyện chắc chắn xảy ra theo lesson 83, nên giao diện phải định nghĩa rõ thử lại nghĩa là gì. Khoá bất biến: máy khách sinh một khoá cho mỗi ý định, gửi kèm; máy chủ lưu khoá cùng kết quả, và lần gọi lại với cùng khoá thì trả lại kết quả cũ thay vì làm lại. Ba chi tiết quyết định đúng sai. Một là **lưu khoá và thực hiện tác động phải nằm trong cùng một giao dịch**, nếu không thì có khe hở giữa hai bước; đây là ứng dụng trực tiếp của lesson 103. Hai là thời gian giữ khoá và điều gì xảy ra sau khi hết hạn. Ba là hành vi khi hai yêu cầu cùng khoá tới đồng thời chứ nối tiếp: bản sau phải chờ hoặc bị từ chối, chứ tạo hai bản ghi. Hợp đồng phải ghi rõ trong tài liệu để máy khách biết mình được thử lại trong điều kiện nào và trong bao lâu.",
"Cài khoá bất biến đúng cả ba chi tiết và chứng minh không sinh tác động kép kể cả khi hai yêu cầu cùng khoá tới đồng thời.",
"Tầng *sáng tạo*. Objective đòi ghép giao dịch, lưu trạng thái và xử lý đồng thời thành một cơ chế mà thư viện không cho sẵn. Kiểm bằng ba thí nghiệm; đạt khi cả ba đều không sinh tác động kép.",
"Cài khoá bất biến cho điểm tạo công việc. Ba thí nghiệm: gọi lại cùng khoá sau khi thành công, gọi lại sau khi máy chủ chết giữa chừng, và gọi hai yêu cầu cùng khoá đồng thời. Với mỗi thí nghiệm, đếm số công việc thật được tạo. Viết phần hợp đồng mô tả điều kiện và thời hạn thử lại.",
"Lưu khoá ngoài giao dịch · để hai yêu cầu cùng khoá cùng đi qua · không nêu thời hạn trong hợp đồng · dùng dấu thời gian làm khoá bất biến.",
"Cả ba thí nghiệm đều tạo đúng một công việc, và hợp đồng nêu rõ điều kiện cùng thời hạn thử lại."),

(106,"Authentication, authorization and ownership checks","TH","Lesson 105",
"Hai việc khác nhau hay bị gộp: xác thực trả lời bạn là ai, uỷ quyền trả lời bạn được làm gì. Ba cách xác thực và đánh đổi: phiên lưu phía máy chủ, thẻ mang theo, và chuẩn uỷ quyền mở ở mức khái niệm. Giới hạn của thẻ tự chứa: nó không thu hồi được trước khi hết hạn, nên thời hạn phải ngắn và phải có cơ chế làm mới; đây là chi tiết hay bị bỏ và gây rủi ro thật. Uỷ quyền theo vai và kiểm quyền sở hữu là hai tầng phải có cả hai: có vai đọc công việc không có nghĩa được đọc công việc **của người khác**; thiếu tầng thứ hai là lỗ hổng phổ biến nhất trong giao diện tự viết. Nguyên tắc kiểm ở đâu: kiểm ở tầng ứng dụng chứ ở hàm xử lý, để mọi đường vào đều đi qua. Phép thử phủ định bắt buộc: với mỗi điểm vào, viết một phép kiểm chứng minh người không có quyền bị từ chối.",
"Cài hai tầng uỷ quyền và chứng minh bằng phép thử phủ định rằng người dùng không truy cập được tài nguyên của người khác.",
"Tầng *áp dụng*. Objective là một cơ chế bảo mật kiểm được bằng phép thử phủ định, chứ bằng việc đường đi thuận chạy được. Kiểm bằng phép thử phủ định cho mọi điểm vào; đạt khi mọi truy cập trái phép bị từ chối và có ghi nhật ký.",
"Cài xác thực bằng thẻ có thời hạn ngắn và cơ chế làm mới. Cài kiểm vai và kiểm quyền sở hữu. Với mỗi điểm vào, viết phép thử phủ định. Thử truy cập tài nguyên của người khác bằng thẻ hợp lệ và chứng minh bị từ chối. Thu hồi quyền một người dùng và đo bao lâu thẻ cũ còn dùng được.",
"Chỉ kiểm vai mà quên kiểm quyền sở hữu · đặt thời hạn thẻ rất dài cho tiện · kiểm quyền trong từng hàm xử lý nên sót đường vào · không viết phép thử phủ định.",
"Mọi điểm vào có phép thử phủ định và đều từ chối đúng, và đo được khoảng thời gian thẻ cũ còn hiệu lực sau khi thu hồi."),

(107,"Resilience - timeouts, circuit breakers and bulkheads","TH","Lesson 106",
"Bài áp các cơ chế đã học ở lesson 83 và 87 vào một dịch vụ có trạng thái. Hạn chờ ở mọi lời gọi ra ngoài, gồm cả lời gọi tới cơ sở dữ liệu, vì cơ sở dữ liệu chậm là nguyên nhân sập dịch vụ phổ biến hơn mạng chậm. Thử lại có giới hạn và chỉ cho thao tác bất biến theo lesson 105. Bộ ngắt mạch bảo vệ bản thân khỏi việc lãng phí tài nguyên vào lời gọi chắc chắn thất bại. Vách ngăn là cơ chế ít được dùng nhưng rất hiệu quả: chia hồ tài nguyên theo loại việc, để một loại việc chậm không chiếm hết hồ kết nối và làm chết mọi loại còn lại; với dịch vụ dữ liệu thì tách hồ cho truy vấn nhanh và truy vấn nặng là cách đơn giản nhất. Giảm tải và hàng đợi có giới hạn theo lesson 87. Thứ tự áp dụng: đặt hạn chờ trước, rồi mới tới các cơ chế còn lại, vì không có hạn chờ thì mọi cơ chế khác vô nghĩa.",
"Dựng bốn cơ chế chịu lỗi và chứng minh dịch vụ suy giảm có kiểm soát khi phụ thuộc hạ nguồn hỏng.",
"Tầng *áp dụng*. Objective là một tập cấu hình kiểm được bằng thí nghiệm hỏng hạ nguồn. Kiểm bằng ba kịch bản hỏng; đạt khi dịch vụ vẫn phục vụ phần không phụ thuộc và không cạn hồ kết nối.",
"Dựng bốn cơ chế. Ba kịch bản: cơ sở dữ liệu chậm gấp mười lần, một phụ thuộc ngoài chết hoàn toàn, và tải gấp năm lần công suất. Với mỗi kịch bản, đo tỉ lệ phục vụ của các điểm vào không phụ thuộc phần hỏng, và kiểm hồ kết nối có cạn không. Thêm vách ngăn tách hồ và đo lại.",
"Không đặt hạn chờ cho lời gọi cơ sở dữ liệu · dùng chung một hồ cho mọi loại truy vấn · thử lại thao tác không bất biến · bộ ngắt mạch không bao giờ đóng lại.",
"Ba kịch bản hỏng đều giữ được tỉ lệ phục vụ của phần không phụ thuộc, và vách ngăn ngăn được hồ kết nối cạn có số chứng minh."),

(108,"Observability for an API - RED metrics and tracing","TH","Lesson 107",
"Ba chỉ số tối thiểu cho mọi điểm vào: tốc độ yêu cầu, tỉ lệ lỗi, và phân bố thời gian xử lý. Báo phân vị chứ trung bình theo lesson 59 và 86. Chia theo điểm vào và theo mã trạng thái, vì tổng gộp che mất một điểm vào đang hỏng. Nhật ký có cấu trúc kèm mã yêu cầu theo lesson 20, và mã đó phải truyền sang cả lời gọi hạ nguồn để nối được toàn tuyến. Theo vết phân tán ở mức dùng được: một mã theo dõi đi qua nhiều thành phần cho biết thời gian tiêu ở đâu, và đây là thứ duy nhất trả lời được câu chậm ở chặng nào khi có nhiều chặng. Điểm kiểm sức khoẻ và sẵn sàng theo lesson 101, nay gắn với hành vi thật: sẵn sàng phải kiểm được kết nối cơ sở dữ liệu, nếu không thì bộ cân bằng tải gửi lưu lượng tới một bản sao đã hỏng. Ba câu hỏi chẩn đoán mà bộ chỉ số phải trả lời được.",
"Dựng bộ chỉ số và theo vết đủ để trả lời ba câu hỏi chẩn đoán mà không cần đọc mã.",
"Tầng *áp dụng*. Objective đo bằng khả năng trả lời câu hỏi chứ bằng số lượng biểu đồ. Kiểm bằng ba câu hỏi chẩn đoán trong lúc có sự cố tiêm sẵn; đạt khi trả lời được ít nhất hai chỉ bằng bảng điều khiển và theo vết.",
"Gắn ba chỉ số chia theo điểm vào và mã trạng thái. Truyền mã yêu cầu xuống hạ nguồn. Dựng theo vết cho tuyến gọi ba chặng. Giảng viên tiêm một sự cố ở một chặng và đặt ba câu hỏi chẩn đoán; trả lời chỉ bằng bảng điều khiển và theo vết. Kiểm điểm sẵn sàng phản ứng đúng khi mất kết nối cơ sở dữ liệu.",
"Báo thời gian xử lý trung bình · gộp mọi điểm vào vào một chỉ số · không truyền mã yêu cầu xuống hạ nguồn · để điểm sẵn sàng luôn trả về khoẻ.",
"Trả lời được ≥ 2/3 câu hỏi chẩn đoán chỉ bằng bảng điều khiển và theo vết, và điểm sẵn sàng đổi trạng thái khi mất cơ sở dữ liệu."),

(109,"The outbox pattern - one atomic write","TH","Lesson 108",
"Bài giải bài toán đã nêu ở lesson 103: ghi cơ sở dữ liệu rồi phát một sự kiện là hai thao tác trên hai hệ, nên chết giữa chừng làm hai bên lệch nhau và không có giao dịch nào bao được cả hai. Mẫu hộp thư đi biến hai thao tác thành một: ghi dữ liệu và ghi bản ghi sự kiện vào một bảng trong **cùng một giao dịch**, rồi một tiến trình riêng đọc bảng đó và phát đi. Vì chỉ còn một thao tác nguyên tử nên không có khe hở. Ba chi tiết cài đặt: đánh dấu đã phát thế nào để không phát lại vô hạn, xử lý khi phát thành công nhưng đánh dấu thất bại, và dọn bảng hộp thư để nó không phình. Bên nhận vẫn phải chịu được nhận trùng, vì mẫu này cho ít nhất một lần chứ đúng một lần. Ở M17, tiến trình đọc bảng hộp thư sẽ được thay bằng đọc thẳng nhật ký giao dịch; ở đây làm bản đơn giản trước.",
"Cài mẫu hộp thư đi và chứng minh bằng thí nghiệm giết tiến trình rằng cơ sở dữ liệu và luồng sự kiện không lệch nhau.",
"Tầng *sáng tạo*. Objective đòi ghép giao dịch với một tiến trình phát riêng thành một mẫu giải bài toán hai hệ. Kiểm bằng 20 lần giết tiến trình; đạt khi số sự kiện phát ra khớp số bản ghi tạo ra, không thiếu.",
"Cài bản ngây thơ ghi cơ sở dữ liệu rồi phát sự kiện, giết tiến trình giữa hai thao tác 20 lần và đếm mức lệch. Cài lại bằng hộp thư đi và lặp thí nghiệm. Xử lý trường hợp phát thành công nhưng đánh dấu thất bại. Thêm việc dọn bảng hộp thư theo lịch.",
"Ghi hai hệ trong hai thao tác rời · dùng giao dịch phân tán khi hộp thư đi đủ · quên dọn bảng hộp thư · giả định bên nhận không bao giờ nhận trùng.",
"Bản ngây thơ có mức lệch đo được, bản hộp thư đi không thiếu sự kiện nào qua 20 lần giết, và bảng hộp thư được dọn tự động."),

(110,"Load testing and capacity notes","TH","Lesson 109",
"Đo dịch vụ dưới tải là cách duy nhất biết nó chịu được bao nhiêu, và làm sai cách thì số đo vô nghĩa. Bốn đại lượng phải đo cùng nhau: thông lượng, thời gian xử lý ở ba phân vị, tỉ lệ lỗi, và mức bão hoà của tài nguyên nút thắt, thường là hồ kết nối. Chỉ đo thông lượng mà không đo tỉ lệ lỗi là cách báo cáo một con số đẹp trong khi dịch vụ đang từ chối phần lớn yêu cầu. Quy trình: tăng tải theo bậc, ở mỗi bậc chờ ổn định rồi mới đo, và tìm điểm mà thời gian xử lý bắt đầu tăng phi tuyến; điểm đó là công suất thật chứ điểm dịch vụ sập. Phân biệt ba loại phép thử: tải thường, tải đỉnh, và tải kéo dài để phát hiện rò rỉ. Ghi chú công suất viết ra thành tài liệu gồm công suất đo được, nút thắt, và ước lượng khi nào cần mở rộng; đây là đầu vào cho M22.",
"Đo được công suất thật của dịch vụ và xác định đúng tài nguyên nút thắt bằng số đo.",
"Tầng *phân tích*. Objective đòi đọc đường cong và định vị nút thắt chứ chỉ chạy công cụ tải. Kiểm bằng đường cong bốn đại lượng; đạt khi xác định đúng điểm công suất và chỉ đúng tài nguyên nút thắt.",
"Chạy tải tăng theo sáu bậc trên giao diện. Ở mỗi bậc đo cả bốn đại lượng. Vẽ đường cong và xác định điểm công suất. Chỉ ra tài nguyên nút thắt bằng số đo. Chạy tải kéo dài 30 phút và kiểm bộ nhớ cùng số kết nối có tăng đơn điệu không. Viết ghi chú công suất một trang.",
"Báo thông lượng đỉnh mà không báo tỉ lệ lỗi · đo ngay khi vừa tăng tải · không đo mức bão hoà hồ kết nối · bỏ phép thử kéo dài nên không phát hiện rò rỉ.",
"Đường cong bốn đại lượng đủ sáu bậc, xác định đúng điểm công suất và tài nguyên nút thắt, và phép thử kéo dài không cho thấy rò rỉ."),

(111,"The job-control API project","DA","Lesson 110",
"Bài dự án khép module, và sản phẩm của nó được dùng lại làm nguồn dữ liệu cho pipeline tham chiếu từ M14B. Xây giao diện điều khiển công việc: nộp công việc có khoá bất biến, truy trạng thái, huỷ, và một tiến trình thợ nhận việc theo cơ chế thuê có thời hạn, có thử lại và có hàng đợi thư chết. PostgreSQL là nguồn sự thật; chỉ thêm kho đệm nếu phép đo chứng minh cần, chứ thêm vì mặc định. Năm phép thử hỏng bắt buộc: nộp trùng, thợ chết sau khi đã gây tác động, cơ sở dữ liệu hết giờ, thuê hết hạn trong khi thợ vẫn sống, và triển khai phiên bản mới trong lúc có công việc đang chạy. Phép thử cuối là phép thử khó nhất và nối thẳng tới lesson 97 và 98. Nộp kèm ghi chú công suất theo lesson 110, mô hình mối đe doạ ngắn, và sổ tay chẩn đoán ba mục.",
"Nộp giao diện chạy đúng qua cả năm phép thử hỏng, có ghi chú công suất, mô hình mối đe doạ và sổ tay.",
"Tầng *sáng tạo*. Bài tổng hợp toàn module thành một dịch vụ có trạng thái chịu được sự cố. Kiểm bằng năm phép thử hỏng cộng rà soát tài liệu; đạt khi không phép thử nào sinh tác động kép hoặc mất công việc.",
"Xây giao diện theo đặc tả. Chạy năm phép thử hỏng và ghi kết quả từng cái. Chạy tải và viết ghi chú công suất. Viết mô hình mối đe doạ ngắn nêu ba mối đe doạ chính và cách chặn. Viết sổ tay ba mục gồm bão hoà, cơ sở dữ liệu hỏng, và triển khai lỗi.",
"Thêm kho đệm mà chưa đo · không có cơ chế thuê nên hai thợ cùng nhận một việc · bỏ phép thử triển khai khi đang chạy · sổ tay viết sau khi bảo vệ.",
"Năm phép thử hỏng đều không sinh tác động kép và không mất công việc, và ba tài liệu đều có nội dung kiểm được."),

(112,"Gate 3 - a correct service under concurrency and failure","KT","Lesson 111",
"Cổng của Phase 3. Bài kiểm hai năng lực: thiết kế mã sửa được ở M7, và vận hành dịch vụ có trạng thái ở M8. Không có nội dung mới.",
"Nộp một dịch vụ giữ đúng bất biến dưới truy cập đồng thời và dưới sự cố, với bằng chứng từ phép kiểm chạy song song.",
"Tầng *đánh giá*. Cổng đo năng lực xây hệ đúng dưới điều kiện thật, nên hình thức là bài làm có tiêm lỗi và có chất vấn.",
"Buổi 155 phút: 110 phút làm bài độc lập, 45 phút chữa bài. Nhận một đặc tả dịch vụ nhỏ. Bài chấm sáu phần: A (15đ) đồ thị phụ thuộc không có cạnh sai chiều và phép kiểm lõi không cần cơ sở dữ liệu · B (25đ) không sinh tác động kép khi máy khách thử lại, chứng minh bằng ba thí nghiệm · C (20đ) bất biến giữ đúng dưới 50 luồng đồng thời, chứng minh bằng phép kiểm chạy song song · D (15đ) hạn chờ và giới hạn thử lại đặt đủ, không khuếch đại · E (15đ) chẩn đoán một sự cố tiêm sẵn bằng chỉ số và theo vết · F (10đ) phép thử phủ định cho mọi điểm vào đều từ chối đúng.",
"Chỉ kiểm tuần tự rồi kết luận đúng · bỏ phần chẩn đoán vì hết giờ · thử lại mà không có khoá bất biến · để lõi phụ thuộc cơ sở dữ liệu.",
"Đạt ≥ 70/100, phần B và C đều ≥ 60%. Bất biến nào chỉ được chứng minh bằng phép kiểm tuần tự thì không tính điểm ở phần C."),
]
